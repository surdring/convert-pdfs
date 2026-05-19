from __future__ import annotations

import asyncio
import base64
import logging
import random
from typing import Any, Dict, Optional

import httpx

from pdf_ocr_md.config import AppConfig
from pdf_ocr_md.types_ import PageOcrResult


logger = logging.getLogger(__name__)


class OcrClient:
    """基于 httpx 的异步 OCR 客户端。"""

    def __init__(self, config: AppConfig) -> None:
        self._config = config
        self._client: Optional[httpx.AsyncClient] = None

    def _build_timeout(self) -> httpx.Timeout:
        return httpx.Timeout(
            connect=self._config.connect_timeout,
            read=self._config.read_timeout,
            write=self._config.write_timeout,
            pool=self._config.pool_timeout,
        )

    async def __aenter__(self) -> "OcrClient":
        limits = httpx.Limits(
            max_connections=max(1, self._config.max_concurrency),
            max_keepalive_connections=max(1, self._config.max_concurrency),
        )
        self._client = httpx.AsyncClient(
            base_url=self._config.server_url.rstrip("/"),
            timeout=self._build_timeout(),
            limits=limits,
            trust_env=False,
        )
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        if self._client is not None:
            await self._client.aclose()
            self._client = None

    async def ocr_page(self, image_bytes: bytes, page_number: int, prompt: str) -> PageOcrResult:
        """对单页图片执行 OCR 并返回结果。"""

        assert self._client is not None, "OcrClient 未初始化，请使用 async with OcrClient(...)"

        b64 = base64.b64encode(image_bytes).decode("ascii")
        data_url = f"data:image/png;base64,{b64}"
        payload: Dict[str, Any] = {
            "model": self._config.model,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {"url": data_url},
                        },
                    ],
                }
            ],
            "stream": False,
        }

        logger.debug(
            "发送 OCR 请求：page=%d model=%s server=%s image_bytes=%d data_url_len=%d content_types=%s",
            page_number,
            self._config.model,
            self._config.server_url,
            len(image_bytes),
            len(data_url),
            [c.get("type") for c in payload.get("messages", [{}])[0].get("content", [])],
        )

        last_error: Optional[str] = None

        for attempt in range(1, self._config.max_retries + 2):
            try:
                resp = await self._client.post(
                    "/v1/chat/completions",
                    json=payload,
                )

                if resp.status_code == 400:
                    text = resp.text
                    if "context" in text and "exceeds" in text:
                        msg = "the request exceeds the available context size"
                        logger.warning("页面 %s 上下文超限：%s", page_number, text)
                        return PageOcrResult(
                            page_number=page_number,
                            text=None,
                            success=False,
                            error=msg,
                        )

                    last_error = f"HTTP 400: {text}"
                    break

                if resp.status_code != 200:
                    last_error = f"HTTP {resp.status_code}: {resp.text}"
                    if resp.status_code in {408, 425, 429} or resp.status_code >= 500:
                        logger.warning(
                            "OCR 请求失败（第 %d 次重试，页面 %d）：%s",
                            attempt,
                            page_number,
                            last_error,
                        )
                    else:
                        break
                else:
                    data = resp.json()
                    content = (
                        data.get("choices", [{}])[0]
                        .get("message", {})
                        .get("content", "")
                    )
                    if not isinstance(content, str):
                        content = str(content)

                    return PageOcrResult(
                        page_number=page_number,
                        text=content,
                        success=True,
                        error=None,
                        raw_response=data,
                    )

            except (httpx.RequestError, httpx.TimeoutException) as exc:
                last_error = repr(exc)
                logger.warning(
                    "OCR 请求异常（第 %d 次重试，页面 %d）：%s",
                    attempt,
                    page_number,
                    last_error,
                )

            if attempt <= self._config.max_retries:
                sleep_seconds = min(30.0, float(2 ** (attempt - 1)))
                sleep_seconds = sleep_seconds * (1.0 + random.random() * 0.2)
                await asyncio.sleep(sleep_seconds)

        return PageOcrResult(
            page_number=page_number,
            text=None,
            success=False,
            error=last_error or "OCR 请求失败",
        )
