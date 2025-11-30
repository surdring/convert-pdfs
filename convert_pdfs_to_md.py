#!/usr/bin/env python3
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
        description="批量将目录中的 PDF 文件通过 OCR 转为 Markdown（异步实现）",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("config.toml"),
        help="配置文件路径（默认: config.toml）",
    )
    # 保留命令行参数以覆盖配置文件（可选）
    parser.add_argument("--input-dir", type=Path, help="覆盖配置文件中的输入目录")
    parser.add_argument("--output-dir", type=Path, help="覆盖配置文件中的输出目录")
    parser.add_argument("--server-url", help="覆盖配置文件中的 OCR 服务地址")
    parser.add_argument("--model", help="覆盖配置文件中的模型别名")
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
    """加载配置：优先使用 TOML，命令行参数可覆盖"""
    config_path = args.config
    if not config_path.exists():
        raise FileNotFoundError(f"配置文件不存在: {config_path}")
    
    config = AppConfig.load_from_toml(config_path)
    
    # 命令行参数覆盖（如果提供）
    if args.input_dir:
        config.input_dir = args.input_dir
    if args.output_dir:
        config.output_dir = args.output_dir
    if args.server_url:
        config.server_url = args.server_url
    if args.model:
        config.model = args.model
    if args.max_concurrency is not None:
        config.max_concurrency = args.max_concurrency
    if args.max_retries is not None:
        config.max_retries = args.max_retries
    if args.request_timeout is not None:
        config.request_timeout = args.request_timeout
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


def main() -> None:
    args = parse_args()
    config = load_config(args)
    setup_logging(config.log_level)
    asyncio.run(async_main(config, force_restart=args.force_restart))


if __name__ == "__main__":
    main()
