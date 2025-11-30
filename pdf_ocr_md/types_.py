from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional, Set


@dataclass
class PdfTask:
    pdf_path: Path
    output_md_path: Path
    num_pages: Optional[int] = None


@dataclass
class PageTask:
    pdf_task: PdfTask
    page_number: int


@dataclass
class PageOcrResult:
    page_number: int
    text: Optional[str]
    success: bool
    error: Optional[str] = None
    raw_response: Optional[dict] = None


@dataclass
class FileConvertResult:
    pdf_task: PdfTask
    page_results: List[PageOcrResult] = field(default_factory=list)
    success: bool = False
    error: Optional[str] = None
    elapsed_seconds: float = 0.0


@dataclass
class ConversionState:
    """单个 PDF 的转换进度状态"""
    pdf_path: Path
    completed_pages: Set[int] = field(default_factory=set)
    failed_pages: Set[int] = field(default_factory=set)
    total_pages: Optional[int] = None

    @property
    def is_complete(self) -> bool:
        if self.total_pages is None:
            return False
        return len(self.completed_pages) >= self.total_pages

    @property
    def pending_pages(self) -> List[int]:
        if self.total_pages is None:
            return []
        return [p for p in range(1, self.total_pages + 1) if p not in self.completed_pages and p not in self.failed_pages]

    def add_completed(self, page_number: int) -> None:
        self.completed_pages.add(page_number)
        self.failed_pages.discard(page_number)

    def add_failed(self, page_number: int) -> None:
        self.failed_pages.add(page_number)
        self.completed_pages.discard(page_number)
