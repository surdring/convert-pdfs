from __future__ import annotations

from pathlib import Path

from pypdf import PdfReader


def get_pdf_page_count(pdf_path: Path) -> int:
    """返回 PDF 总页数。"""
    reader = PdfReader(str(pdf_path))
    return len(reader.pages)
