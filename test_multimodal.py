#!/usr/bin/env python3
from __future__ import annotations

# 用途：
# - 根据当前目录下的 config.toml（或 --config 指定的 TOML）配置，
#   调用 llama-server(OpenAI 兼容) 的 /v1/chat/completions 接口，
#   发送 "text + image_url(data:base64)" 的多模态请求，用于验证服务端是否正确启用 mmproj。
#
# 读取的配置项（来自 config.toml）：
# - [ocr].server_url      -> 服务地址（例如 http://172.16.100.211:8082）
# - [ocr].model           -> 模型别名（例如 chandra-ocr）
# - [ocr].prompt_preset   -> 默认提示词模板名（由 pdf_ocr_md/ocr/prompts.py 决定）
# - [retry].request_timeout/connect_timeout/read_timeout/write_timeout/pool_timeout -> httpx 超时
#
# 常用用法：
# - 最简单：
#   python test_multimodal.py --image /path/to/xxx.png
# - 输出完整 JSON 响应（方便检查服务端返回结构/用量等）：
#   python test_multimodal.py --image /path/to/xxx.png --print-json
# - 使用指定配置文件：
#   python test_multimodal.py --config /path/to/config.toml --image /path/to/xxx.png
# - 覆盖 prompt：
#   python test_multimodal.py --image /home/zhengxueen/workspace/convert-pdfs/test/微信图片_20230710151313.png --prompt "请识别图片中的文字并输出 Markdown"

import argparse
import asyncio
import base64
import json
import logging
from pathlib import Path

import httpx

from pdf_ocr_md.config import AppConfig
from pdf_ocr_md.ocr.prompts import get_prompt


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="测试 OCR 多模态 /v1/chat/completions")
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("config.toml"),
        help="配置文件路径（默认: config.toml）",
    )
    parser.add_argument("--image", type=Path, required=True, help="待测试的图片文件路径（png/jpg/webp 等）")
    parser.add_argument(
        "--prompt",
        default=None,
        help="自定义 prompt（不传则使用 config.toml 的 ocr.prompt_preset）",
    )
    parser.add_argument(
        "--prompt-preset",
        default=None,
        help="覆盖配置中的 prompt_preset（不传则使用 config.toml）",
    )
    parser.add_argument(
        "--print-json",
        action="store_true",
        help="输出完整 JSON 响应（默认仅输出 content）",
    )
    parser.add_argument(
        "--request-timeout",
        type=float,
        default=None,
        help="覆盖 config.toml 的 [retry].request_timeout（同时覆盖 read/write/pool 超时）",
    )
    return parser.parse_args()


def _guess_mime_type(path: Path) -> str:
    ext = path.suffix.lower()
    if ext in {".jpg", ".jpeg"}:
        return "image/jpeg"
    if ext == ".webp":
        return "image/webp"
    if ext == ".gif":
        return "image/gif"
    return "image/png"


def _build_timeout(config: AppConfig) -> httpx.Timeout:
    return httpx.Timeout(
        connect=config.connect_timeout,
        read=config.read_timeout,
        write=config.write_timeout,
        pool=config.pool_timeout,
    )


async def async_main() -> None:
    args = parse_args()
    config = AppConfig.load_from_toml(args.config)

    if args.request_timeout is not None:
        config.request_timeout = args.request_timeout
        config.read_timeout = args.request_timeout
        config.write_timeout = args.request_timeout
        config.pool_timeout = args.request_timeout

    prompt_preset = args.prompt_preset or config.ocr_prompt_preset
    prompt = args.prompt if args.prompt is not None else get_prompt(prompt_preset)

    image_bytes = args.image.read_bytes()
    b64 = base64.b64encode(image_bytes).decode("ascii")
    mime = _guess_mime_type(args.image)
    data_url = f"data:{mime};base64,{b64}"

    payload = {
        "model": config.model,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": data_url}},
                ],
            }
        ],
        "stream": False,
    }

    logging.getLogger(__name__).info(
        "testing multimodal: server=%s model=%s image=%s bytes=%d",
        config.server_url,
        config.model,
        str(args.image),
        len(image_bytes),
    )

    async with httpx.AsyncClient(
        base_url=config.server_url.rstrip("/"),
        timeout=_build_timeout(config),
        trust_env=False,
    ) as client:
        try:
            resp = await client.post("/v1/chat/completions", json=payload)
        except httpx.ReadTimeout as exc:
            raise SystemExit(
                "请求 ReadTimeout：服务端推理/排队时间可能超过 config.toml 的 [retry].request_timeout。"
                "可尝试将 request_timeout 提高到 180/300 秒，或检查 OCR 服务是否可达/是否繁忙。"
            ) from exc

    if resp.status_code != 200:
        raise SystemExit(f"HTTP {resp.status_code}: {resp.text}")

    data = resp.json()

    if args.print_json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
        return

    content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
    if not isinstance(content, str):
        content = str(content)
    print(content)


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s - %(message)s")
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
