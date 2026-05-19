#!/usr/bin/env python3
"""批量将目录中的 PDF 文件通过 AIStudio(layout-parsing) OCR 转为 Markdown（异步实现）。
 
 该脚本会递归扫描输入目录下的 PDF，将每个 PDF 作为一次请求发送到 AIStudio 的 layout-parsing API：
 - 请求头使用 token 鉴权（Authorization: token xxx）
 - 请求体将 PDF 文件 base64 编码后提交（fileType=0）
 - 将返回结果中的 markdown 文本合并后写入 .md
 - 可选下载 markdown 引用图片与 outputImages
 
 用法示例：
 
 1) 推荐：用环境变量提供 token（避免命令行历史泄露）
 
     export AISTUDIO_TOKEN="<your token>"
     python convert_pdfs_to_md_aistudio.py \
       --input-dir /path/to/PDFS \
       --output-dir /path/to/PDFS_OUTPUT
 
 2) 覆盖 API 地址 / 并发 / 超时（接口处理整份 PDF，建议超时设置偏大）：
 
     export AISTUDIO_TOKEN="<your token>"
     python convert_pdfs_to_md_aistudio.py \
       --input-dir /path/to/PDFS \
       --output-dir /path/to/PDFS_OUTPUT \
       --api-url https://xxxx.aistudio-app.com/layout-parsing \
       --max-concurrency 3 \
       --request-timeout 300
 
 3) 下载图片（markdown.images / outputImages）：
 
     export AISTUDIO_TOKEN="<your token>"
     python convert_pdfs_to_md_aistudio.py \
       --input-dir /path/to/PDFS \
       --output-dir /path/to/PDFS_OUTPUT \
       --download-images \
       --download-output-images
 
 重要提醒：
 
 - token 建议通过环境变量 AISTUDIO_TOKEN 提供；不建议硬编码进脚本，也不建议直接写入命令行参数。
 - 如果接口返回 429/5xx 或偶发网络错误，脚本会按 max_retries 进行重试。
 - 如果你发现大量 PDF 跑起来很慢，优先调小 max_concurrency，避免触发限流。
 """

from __future__ import annotations

import argparse
import asyncio
import base64
import logging
import os
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

import httpx

from pdf_ocr_md.logging_utils import setup_logging
from pdf_ocr_md.pdf.scanner import scan_pdfs
from pdf_ocr_md.types_ import PdfTask


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="批量将目录中的 PDF 文件通过 AIStudio(layout-parsing) OCR 转为 Markdown（异步实现）",
    )

    parser.add_argument("--input-dir", type=Path, required=True, help="输入 PDF 根目录（递归扫描 *.pdf）")
    parser.add_argument("--output-dir", type=Path, required=True, help="输出 Markdown 根目录")

    parser.add_argument(
        "--api-url",
        default="https://qddeq5jcbdo0acd6.aistudio-app.com/layout-parsing",
        help="AIStudio layout-parsing API URL",
    )
    parser.add_argument(
        "--token",
        default=None,
        help="AIStudio token（建议通过环境变量 AISTUDIO_TOKEN 提供；命令行可能被 shell history 记录）",
    )

    parser.add_argument("--max-concurrency", type=int, default=3, help="最大并发 PDF 数")
    parser.add_argument("--max-retries", type=int, default=5, help="最大重试次数")
    parser.add_argument("--request-timeout", type=float, default=300.0, help="单次请求超时时间（秒）")

    parser.add_argument(
        "--force-restart",
        action="store_true",
        help="强制重新转换（覆盖已存在的输出 md 文件）",
    )

    parser.add_argument(
        "--use-doc-orientation-classify",
        action="store_true",
        help="启用版面方向分类（对应 optional_payload.useDocOrientationClassify）",
    )
    parser.add_argument(
        "--use-doc-unwarping",
        action="store_true",
        help="启用文档去弯曲（对应 optional_payload.useDocUnwarping）",
    )
    parser.add_argument(
        "--use-chart-recognition",
        action="store_true",
        help="启用图表识别（对应 optional_payload.useChartRecognition）",
    )

    parser.add_argument(
        "--download-images",
        action="store_true",
        help="下载 markdown 引用的图片到本地（res['markdown']['images']）",
    )
    parser.add_argument(
        "--download-output-images",
        action="store_true",
        help="下载输出图像（res['outputImages']）",
    )

    parser.add_argument("--log-level", default="INFO", help="日志级别：DEBUG/INFO/WARNING/ERROR")

    return parser.parse_args()


def _get_token(args: argparse.Namespace) -> str:
    token = args.token or os.environ.get("AISTUDIO_TOKEN")
    if not token:
        raise SystemExit("缺少 token：请使用 --token 或设置环境变量 AISTUDIO_TOKEN")
    return token


async def _read_and_b64encode(path: Path) -> str:
    data = await asyncio.to_thread(path.read_bytes)
    return base64.b64encode(data).decode("ascii")


def _safe_rel_path(p: str) -> Path:
    # 避免出现以 / 开头导致写到根目录
    p = p.lstrip("/\\")
    return Path(p)


async def _download_one(
    client: httpx.AsyncClient,
    url: str,
    dest_path: Path,
    semaphore: asyncio.Semaphore,
    logger: logging.Logger,
) -> None:
    async with semaphore:
        resp = await client.get(url)
        if resp.status_code != 200:
            logger.warning("图片下载失败：%s HTTP %d", url, resp.status_code)
            return
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        await asyncio.to_thread(dest_path.write_bytes, resp.content)


def _build_timeout(request_timeout: float) -> httpx.Timeout:
    # 该 API 是一次性处理整份 PDF，因此 read/write/pool 都按同一超时处理
    return httpx.Timeout(connect=10.0, read=request_timeout, write=request_timeout, pool=request_timeout)


async def _post_with_retry(
    client: httpx.AsyncClient,
    api_url: str,
    payload: Dict[str, Any],
    headers: Dict[str, str],
    max_retries: int,
    logger: logging.Logger,
) -> Dict[str, Any]:
    last_error: Optional[str] = None

    for attempt in range(1, max_retries + 2):
        try:
            resp = await client.post(api_url, json=payload, headers=headers)
        except (httpx.RequestError, httpx.TimeoutException) as exc:
            last_error = repr(exc)
            if attempt <= max_retries:
                sleep_seconds = min(30.0, float(2 ** (attempt - 1)))
                sleep_seconds = sleep_seconds * (1.0 + 0.2)
                logger.warning("请求异常，准备重试（%d/%d）：%s", attempt, max_retries, last_error)
                await asyncio.sleep(sleep_seconds)
                continue
            raise

        if resp.status_code == 200:
            return resp.json()

        last_error = f"HTTP {resp.status_code}: {resp.text}"
        retryable = resp.status_code in {408, 425, 429} or resp.status_code >= 500
        if retryable and attempt <= max_retries:
            sleep_seconds = min(30.0, float(2 ** (attempt - 1)))
            sleep_seconds = sleep_seconds * (1.0 + 0.2)
            logger.warning("请求失败，准备重试（%d/%d）：%s", attempt, max_retries, last_error)
            await asyncio.sleep(sleep_seconds)
            continue

        raise SystemExit(last_error)

    raise SystemExit(last_error or "请求失败")


async def _process_single_pdf(
    pdf_task: PdfTask,
    api_url: str,
    token: str,
    timeout: httpx.Timeout,
    max_retries: int,
    force_restart: bool,
    optional_payload: Dict[str, Any],
    download_images: bool,
    download_output_images: bool,
    logger: logging.Logger,
) -> Tuple[PdfTask, bool, Optional[str]]:
    output_md_path = pdf_task.output_md_path

    if output_md_path.exists() and not force_restart:
        logger.info("输出已存在，跳过：%s", output_md_path)
        return pdf_task, True, None

    try:
        file_b64 = await _read_and_b64encode(pdf_task.pdf_path)
    except Exception as exc:  # noqa: BLE001
        return pdf_task, False, f"读取/编码 PDF 失败: {exc}"

    headers = {
        "Authorization": f"token {token}",
        "Content-Type": "application/json",
    }

    required_payload: Dict[str, Any] = {
        "file": file_b64,
        "fileType": 0,
    }

    payload = {**required_payload, **optional_payload}

    async with httpx.AsyncClient(timeout=timeout, trust_env=False) as client:
        try:
            data = await _post_with_retry(
                client=client,
                api_url=api_url,
                payload=payload,
                headers=headers,
                max_retries=max_retries,
                logger=logger,
            )
        except Exception as exc:  # noqa: BLE001
            return pdf_task, False, f"请求失败: {exc}"

        result = data.get("result")
        if not isinstance(result, dict):
            return pdf_task, False, "响应中缺少 result 字段"

        lprs = result.get("layoutParsingResults")
        if not isinstance(lprs, list) or not lprs:
            return pdf_task, False, "响应中 layoutParsingResults 为空"

        markdown_texts: List[str] = []
        markdown_image_items: List[Tuple[str, str]] = []
        output_image_items: List[Tuple[str, str, int]] = []

        for i, res in enumerate(lprs):
            if not isinstance(res, dict):
                continue
            md = res.get("markdown") or {}
            if isinstance(md, dict):
                text = md.get("text")
                if isinstance(text, str) and text.strip():
                    markdown_texts.append(text.rstrip())

                images = md.get("images")
                if isinstance(images, dict):
                    for img_path, img_url in images.items():
                        if isinstance(img_path, str) and isinstance(img_url, str):
                            markdown_image_items.append((img_path, img_url))

            out_images = res.get("outputImages")
            if isinstance(out_images, dict):
                for img_name, img_url in out_images.items():
                    if isinstance(img_name, str) and isinstance(img_url, str):
                        output_image_items.append((img_name, img_url, i))

        title = pdf_task.pdf_path.stem
        combined_md = "# " + title + "\n\n" + "\n\n".join(markdown_texts) + "\n"

        try:
            output_md_path.parent.mkdir(parents=True, exist_ok=True)
            await asyncio.to_thread(output_md_path.write_text, combined_md, "utf-8")
        except Exception as exc:  # noqa: BLE001
            return pdf_task, False, f"写入 Markdown 失败: {exc}"

        if not (download_images or download_output_images):
            return pdf_task, True, None

        img_sem = asyncio.Semaphore(8)
        download_tasks: List[asyncio.Task[None]] = []

        if download_images:
            for img_path, img_url in markdown_image_items:
                dest = output_md_path.parent / _safe_rel_path(img_path)
                download_tasks.append(
                    asyncio.create_task(_download_one(client, img_url, dest, img_sem, logger))
                )

        if download_output_images:
            for img_name, img_url, idx in output_image_items:
                dest = output_md_path.parent / f"{img_name}_{idx}.jpg"
                download_tasks.append(
                    asyncio.create_task(_download_one(client, img_url, dest, img_sem, logger))
                )

        if download_tasks:
            await asyncio.gather(*download_tasks, return_exceptions=True)

    return pdf_task, True, None


async def async_main(args: argparse.Namespace) -> None:
    logger = logging.getLogger(__name__)

    token = _get_token(args)
    timeout = _build_timeout(args.request_timeout)

    optional_payload = {
        "useDocOrientationClassify": bool(args.use_doc_orientation_classify),
        "useDocUnwarping": bool(args.use_doc_unwarping),
        "useChartRecognition": bool(args.use_chart_recognition),
    }

    tasks = scan_pdfs(args.input_dir, args.output_dir)
    if not tasks:
        raise SystemExit(f"未找到 PDF：{args.input_dir}")

    logger.info("发现 %d 个 PDF，开始转换...", len(tasks))

    sem = asyncio.Semaphore(max(1, int(args.max_concurrency)))

    async def run_one(t: PdfTask) -> Tuple[PdfTask, bool, Optional[str]]:
        async with sem:
            logger.info("处理 PDF：%s", t.pdf_path)
            return await _process_single_pdf(
                pdf_task=t,
                api_url=args.api_url,
                token=token,
                timeout=timeout,
                max_retries=int(args.max_retries),
                force_restart=bool(args.force_restart),
                optional_payload=optional_payload,
                download_images=bool(args.download_images),
                download_output_images=bool(args.download_output_images),
                logger=logger,
            )

    results = await asyncio.gather(*(run_one(t) for t in tasks))

    ok = [r for r in results if r[1]]
    bad = [r for r in results if not r[1]]

    logger.info("转换完成：成功 %d 个，失败 %d 个，总文件 %d", len(ok), len(bad), len(results))
    if bad:
        for t, _, err in bad:
            logger.error("失败：%s：%s", t.pdf_path, err)


def main() -> None:
    args = parse_args()
    setup_logging(args.log_level)
    try:
        asyncio.run(async_main(args))
    except KeyboardInterrupt:
        logging.getLogger(__name__).info("收到中断信号，已退出")


if __name__ == "__main__":
    main()
