from __future__ import annotations

from typing import List

from pdf_ocr_md.types_ import PageOcrResult, PdfTask


def build_markdown(pdf_task: PdfTask, page_results: List[PageOcrResult]) -> str:
    """根据单个 PDF 的页级 OCR 结果生成完整 Markdown 文本。"""

    lines: List[str] = []
    title = pdf_task.pdf_path.stem
    lines.append(f"# {title}")
    lines.append("")

    failed_pages: List[PageOcrResult] = []

    for result in sorted(page_results, key=lambda r: r.page_number):
        lines.append(f"## Page {result.page_number}")
        lines.append("")

        if result.success and result.text:
            lines.append(result.text.rstrip())
        else:
            failed_pages.append(result)
            lines.append(f"> [OCR FAILED] Page {result.page_number}")
            if result.error:
                lines.append(f"> 错误信息: {result.error}")

        lines.append("")

    if failed_pages:
        lines.append("## OCR 失败页列表")
        lines.append("")
        for r in failed_pages:
            if r.error:
                lines.append(f"- Page {r.page_number}: {r.error}")
            else:
                lines.append(f"- Page {r.page_number}")
        lines.append("")

    return "\n".join(lines)
