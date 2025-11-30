from __future__ import annotations

import json
import logging
import threading
from pathlib import Path
from typing import Dict

from pdf_ocr_md.types_ import ConversionState

logger = logging.getLogger(__name__)

_STATE_FILE_SUFFIX = ".convert_state.json"
_DEFAULT_BATCH_SIZE = 5


def _state_file_path(output_md_path: Path) -> Path:
    """返回对应的状态文件路径"""
    return output_md_path.with_suffix(_STATE_FILE_SUFFIX)


def load_state(output_md_path: Path, pdf_path: Path | None = None) -> ConversionState:
    """从状态文件加载转换进度，如果不存在则返回空状态
    
    Args:
        output_md_path: Markdown 文件路径
        pdf_path: 原始 PDF 文件路径（用于新状态初始化）
    """
    state_path = _state_file_path(output_md_path)
    if not state_path.exists():
        # 使用传入的 pdf_path 或默认推导
        default_pdf_path = pdf_path or output_md_path.with_suffix(".pdf")
        return ConversionState(pdf_path=default_pdf_path)

    try:
        data = json.loads(state_path.read_text(encoding="utf-8"))
        state = ConversionState(
            pdf_path=Path(data["pdf_path"]),
            completed_pages=set(data.get("completed_pages", [])),
            failed_pages=set(data.get("failed_pages", [])),
            total_pages=data.get("total_pages"),
        )
        logger.info(
            "加载转换状态：%s，已完成 %d 页，失败 %d 页",
            state_path,
            len(state.completed_pages),
            len(state.failed_pages),
        )
        return state
    except Exception as exc:
        logger.warning("读取状态文件失败，将重新开始：%s", exc)
        default_pdf_path = pdf_path or output_md_path.with_suffix(".pdf")
        return ConversionState(pdf_path=default_pdf_path)


def save_state(state: ConversionState, output_md_path: Path) -> None:
    """保存转换进度到状态文件（原子写入）"""
    state_path = _state_file_path(output_md_path)
    data = {
        "pdf_path": str(state.pdf_path),
        "completed_pages": sorted(state.completed_pages),
        "failed_pages": sorted(state.failed_pages),
        "total_pages": state.total_pages,
    }
    try:
        # 确保目录存在
        state_path.parent.mkdir(parents=True, exist_ok=True)
        # 先写临时文件，再原子重命名
        tmp_path = state_path.with_suffix(".tmp")
        tmp_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        tmp_path.replace(state_path)
    except Exception as exc:
        logger.warning("保存状态文件失败：%s", exc)


def clear_state(output_md_path: Path) -> None:
    """删除状态文件，用于强制重新开始"""
    state_path = _state_file_path(output_md_path)
    if state_path.exists():
        state_path.unlink()
        logger.info("已删除状态文件：%s", state_path)


def list_states_with_progress(output_dir: Path) -> Dict[str, ConversionState]:
    """列出输出目录下所有状态文件及其进度（用于调试）"""
    states = {}
    for state_file in output_dir.rglob(_STATE_FILE_SUFFIX):
        try:
            state = load_state(state_file.with_suffix(""))  # 去掉 .json 后缀
            states[str(state.pdf_path.relative_to(output_dir))] = state
        except Exception:
            continue
    return states


class GlobalBatchStateManager:
    """全局批量状态管理器：所有 PDF 共享同一个计数器"""
    
    def __init__(self, batch_size: int = _DEFAULT_BATCH_SIZE):
        self.batch_size = batch_size
        self._pending_writes = 0
        self._lock = threading.Lock()  # 线程安全
        logger.info("初始化全局批量状态管理器：批次大小=%d", batch_size)
    
    def add_completed(self, state: ConversionState, output_md_path: Path, page_number: int) -> None:
        """标记页面完成，并根据批次大小决定是否写入"""
        with self._lock:
            state.add_completed(page_number)
            self._pending_writes += 1
            logger.debug("页面 %d 完成，待写入计数=%d", page_number, self._pending_writes)
            if self._pending_writes >= self.batch_size:
                logger.info("达到批次大小 %d，写入状态文件", self.batch_size)
                self._flush_unlocked(state, output_md_path)
    
    def add_failed(self, state: ConversionState, output_md_path: Path, page_number: int) -> None:
        """标记页面失败，立即写入（失败页较少，优先保存）"""
        with self._lock:
            logger.info("页面 %d 失败，立即写入状态", page_number)
            state.add_failed(page_number)
            self._flush_unlocked(state, output_md_path)
    
    def _flush_unlocked(self, state: ConversionState, output_md_path: Path) -> None:
        """内部方法：不加锁的刷新（调用者已加锁）"""
        if self._pending_writes > 0:
            logger.info("写入状态文件，已完成 %d 页", len(state.completed_pages))
            save_state(state, output_md_path)
            self._pending_writes = 0
    
    def flush(self, state: ConversionState, output_md_path: Path) -> None:
        """立即写入状态文件"""
        with self._lock:
            self._flush_unlocked(state, output_md_path)
    
    def force_flush(self, state: ConversionState, output_md_path: Path) -> None:
        """强制写入（程序退出时调用）"""
        with self._lock:
            logger.info("强制写入剩余状态，待写入计数=%d", self._pending_writes)
            self._flush_unlocked(state, output_md_path)


# 保持原有类以兼容现有代码
class BatchStateManager(GlobalBatchStateManager):
    """批量状态管理器：减少 I/O 次数（向后兼容）"""
    def __init__(self, state: ConversionState, output_md_path: Path, batch_size: int = _DEFAULT_BATCH_SIZE):
        super().__init__(batch_size)
        self.state = state
        self.output_md_path = output_md_path
    
    def add_completed(self, page_number: int) -> None:
        """标记页面完成，并根据批次大小决定是否写入"""
        super().add_completed(self.state, self.output_md_path, page_number)
    
    def add_failed(self, page_number: int) -> None:
        """标记页面失败，立即写入（失败页较少，优先保存）"""
        super().add_failed(self.state, self.output_md_path, page_number)
    
    def flush(self) -> None:
        """立即写入状态文件"""
        super().flush(self.state, self.output_md_path)
    
    def force_flush(self) -> None:
        """强制写入（程序退出时调用）"""
        super().force_flush(self.state, self.output_md_path)
