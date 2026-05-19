#!/usr/bin/env python3
 """批量将目录中的 PDF 文件通过 vLLM(PaddleOCR-VL-1.5) OCR 转为 Markdown（异步实现）。
 
 该脚本复用项目内的异步流水线（扫描 PDF、逐页渲染、并发调用 /v1/chat/completions、写入 Markdown、断点续传）。
 
 用法示例：
 
 1) 最常用：读取 config.toml（但用命令行强制指向 vLLM 服务）
 
     python convert_pdfs_to_md_vllm.py --server-url http://127.0.0.1:8011 --model PaddleOCR-VL-1.5
 
 2) 覆盖输入输出目录：
 
     python convert_pdfs_to_md_vllm.py \
       --input-dir /path/to/PDFS \
       --output-dir /path/to/PDFS_OUTPUT \
       --server-url http://127.0.0.1:8011 \
       --model PaddleOCR-VL-1.5
 
 3) 覆盖并发与超时（vLLM 推理可能较慢，建议超时设置偏大）：
 
     python convert_pdfs_to_md_vllm.py \
       --server-url http://127.0.0.1:8011 \
       --model PaddleOCR-VL-1.5 \
       --max-concurrency 3 \
       --request-timeout 300
 
 重要提醒：
 
 - 如果 vLLM 容器使用了 --network=host，并且脚本运行在同一台宿主机上，server_url 用：
   http://127.0.0.1:8011
 - 如果脚本运行在其它机器上，则 server_url 必须改为宿主机可访问的 IP：
   http://<宿主机IP>:8011
 - 遇到请求超时，优先调大 --request-timeout（会同步覆盖 read/write/pool 超时）。
 """

from __future__ import annotations

import argparse
import asyncio
import logging
from pathlib import Path

from pdf_ocr_md.config import AppConfig, build_config_from_args
from pdf_ocr_md.logging_utils import setup_logging
from pdf_ocr_md.orchestrator import run as run_pipeline


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="批量将目录中的 PDF 文件通过 vLLM(PaddleOCR-VL-1.5) OCR 转为 Markdown（异步实现）",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("config.toml"),
        help="配置文件路径（默认: config.toml；如不存在则必须提供 --input-dir/--output-dir）",
    )

    parser.add_argument("--input-dir", type=Path, help="覆盖配置文件中的输入目录")
    parser.add_argument("--output-dir", type=Path, help="覆盖配置文件中的输出目录")
    parser.add_argument(
        "--server-url",
        default="http://127.0.0.1:8011",
        help="vLLM OCR 服务地址（默认: http://127.0.0.1:8011）",
    )
    parser.add_argument(
        "--model",
        default="PaddleOCR-VL-1.5",
        help='vLLM served model name（默认: "PaddleOCR-VL-1.5"）',
    )
    parser.add_argument("--max-concurrency", type=int, help="覆盖配置文件中的最大并发数")
    parser.add_argument("--max-retries", type=int, help="覆盖配置文件中的最大重试次数")
    parser.add_argument("--request-timeout", type=float, help="覆盖配置文件中的请求超时时间")
    parser.add_argument("--log-level", help="覆盖配置文件中的日志级别")
    parser.add_argument("--ocr-prompt-preset", help="覆盖配置文件中的 OCR 提示词模板")
    parser.add_argument(
        "--force-restart",
        action="store_true",
        help="强制重新开始所有转换（删除已有状态文件）",
    )
    return parser.parse_args()


def load_config(args: argparse.Namespace) -> AppConfig:
    """加载配置：优先使用 TOML，命令行参数可覆盖；默认指向 vLLM(PaddleOCR-VL-1.5) 服务。"""

    config_path = args.config
    if config_path.exists():
        config = AppConfig.load_from_toml(config_path)
    else:
        if not args.input_dir or not args.output_dir:
            raise FileNotFoundError(
                f"配置文件不存在: {config_path}；且未提供 --input-dir/--output-dir"
            )

        shim = argparse.Namespace(
            input_dir=args.input_dir,
            output_dir=args.output_dir,
            server_url=args.server_url,
            model=args.model,
            max_concurrency=args.max_concurrency or 3,
            max_retries=args.max_retries or 10,
            request_timeout=args.request_timeout or 300.0,
            log_level=args.log_level or "INFO",
            ocr_prompt_preset=args.ocr_prompt_preset or "default",
        )
        config = build_config_from_args(shim)

    if args.input_dir:
        config.input_dir = args.input_dir
    if args.output_dir:
        config.output_dir = args.output_dir

    config.server_url = args.server_url
    config.model = args.model

    if args.max_concurrency is not None:
        config.max_concurrency = args.max_concurrency
    if args.max_retries is not None:
        config.max_retries = args.max_retries
    if args.request_timeout is not None:
        config.request_timeout = args.request_timeout
        config.read_timeout = args.request_timeout
        config.write_timeout = args.request_timeout
        config.pool_timeout = args.request_timeout
    if args.log_level:
        config.log_level = args.log_level
    if args.ocr_prompt_preset:
        config.ocr_prompt_preset = args.ocr_prompt_preset

    return config


async def async_main(config: AppConfig, force_restart: bool = False) -> None:
    logger = logging.getLogger(__name__)
    results, stats = await run_pipeline(config, force_restart=force_restart)

    logger.info(
        "转换完成：成功 %d 个，失败 %d 个，总文件 %d，用时 %.2f 秒，平均每文件 %.2f 秒",
        stats["success_count"],
        stats["failed_count"],
        stats["total_files"],
        stats["total_seconds"],
        stats["avg_seconds_per_file"],
    )

    failed = [r for r in results if not r.success]
    if failed:
        logger.warning("以下 PDF 转换失败（共 %d 个）：", len(failed))
        for r in failed:
            logger.warning("- %s: %s", r.pdf_task.pdf_path, r.error)


def main() -> None:
    args = parse_args()
    config = load_config(args)
    setup_logging(config.log_level)
    try:
        asyncio.run(async_main(config, force_restart=args.force_restart))
    except KeyboardInterrupt:
        logging.getLogger(__name__).info("收到中断信号，已退出")


if __name__ == "__main__":
    main()
