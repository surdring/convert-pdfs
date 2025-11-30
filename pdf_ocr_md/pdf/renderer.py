from __future__ import annotations

from pathlib import Path

import fitz  # PyMuPDF


def render_page_to_png_bytes(pdf_path: Path, page_number: int) -> bytes:
    """将指定页面渲染为 PNG 格式的二进制数据。

    page_number 从 1 开始计数。
    """
    if page_number < 1:
        raise ValueError("page_number 从 1 开始")

    with fitz.open(pdf_path) as doc:
        if page_number > doc.page_count:
            raise ValueError(f"页面号 {page_number} 超过总页数 {doc.page_count}")
        page = doc.load_page(page_number - 1)
        pix = page.get_pixmap()
        return pix.tobytes("png")
