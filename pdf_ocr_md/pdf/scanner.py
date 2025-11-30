from __future__ import annotations

from pathlib import Path
from typing import List

from pdf_ocr_md.types_ import PdfTask


def scan_pdfs(input_root: Path, output_root: Path) -> List[PdfTask]:
    """递归扫描 input_root 下的所有 PDF 文件，并生成对应的输出任务。

    输出结构：
    - input_root/sub/file.pdf → output_root/sub/file/file.md
    - 即每个 PDF 在输出目录下生成一个同名目录，Markdown 文件放在其中
    """
    tasks: List[PdfTask] = []
    for pdf_path in input_root.rglob("*.pdf"):
        if pdf_path.is_file():
            relative = pdf_path.relative_to(input_root)
            # 输出目录：去掉 .pdf 后缀，作为目录名；Markdown 文件名为 file.md
            output_dir = output_root / relative.with_suffix("")
            output_md_path = output_dir / "file.md"
            tasks.append(PdfTask(pdf_path=pdf_path, output_md_path=output_md_path))
    return tasks
