from __future__ import annotations

import asyncio
import logging
import time
from typing import List, Tuple

from pdf_ocr_md.config import AppConfig
from pdf_ocr_md.markdown.postprocess import postprocess_markdown
from pdf_ocr_md.markdown.writer import build_markdown
from pdf_ocr_md.ocr.client import OcrClient
from pdf_ocr_md.ocr.prompts import get_prompt
from pdf_ocr_md.pdf.loader import get_pdf_page_count
from pdf_ocr_md.pdf.renderer import render_page_to_png_bytes
from pdf_ocr_md.pdf.scanner import scan_pdfs
from pdf_ocr_md.state_manager import load_state, save_state, clear_state, BatchStateManager
from pdf_ocr_md.types_ import FileConvertResult, PageOcrResult, PdfTask, ConversionState


logger = logging.getLogger(__name__)


async def _process_single_pdf(
    pdf_task: PdfTask,
    config: AppConfig,
    client: OcrClient,
    semaphore: asyncio.Semaphore,
    force_restart: bool = False,
) -> FileConvertResult:
    start = time.perf_counter()
    page_results: List[PageOcrResult] = []
    error: str | None = None

    prompt = get_prompt(config.ocr_prompt_preset)

    # 加载或初始化状态
    if force_restart:
        clear_state(pdf_task.output_md_path)
    state = load_state(pdf_task.output_md_path, pdf_path=pdf_task.pdf_path)

    # 确保输出目录存在（提前创建，避免状态文件写入失败）
    pdf_task.output_md_path.parent.mkdir(parents=True, exist_ok=True)

    # 获取页数（同步操作，放到线程池）
    batch_manager = None
    try:
        num_pages = await asyncio.to_thread(get_pdf_page_count, pdf_task.pdf_path)
        pdf_task.num_pages = num_pages
        state.total_pages = num_pages
        logger.info("开始处理 PDF：%s（%d 页）", pdf_task.pdf_path, num_pages)

        # 如果已完成，直接返回
        if state.is_complete:
            logger.info("PDF 已完成，跳过：%s", pdf_task.pdf_path)
            return FileConvertResult(
                pdf_task=pdf_task,
                page_results=[],
                success=True,
                error=None,
                elapsed_seconds=0.0,
            )

        # 创建批量状态管理器：根据总页数动态调整批次大小
        batch_size = min(5, max(1, num_pages // 10)) if num_pages else 5
        batch_manager = BatchStateManager(state, pdf_task.output_md_path, batch_size=batch_size)
        logger.info("PDF %s：总页数 %d，批次大小 %d", pdf_task.pdf_path.name, num_pages, batch_size)
    except Exception as exc:
        error = str(exc)
        logger.exception("获取 PDF 页数失败：%s", pdf_task.pdf_path)
        elapsed = time.perf_counter() - start
        return FileConvertResult(
            pdf_task=pdf_task,
            page_results=[],
            success=False,
            error=error,
            elapsed_seconds=elapsed,
        )

    # 如果 batch_manager 未创建，说明出错了
    if batch_manager is None:
        return FileConvertResult(
            pdf_task=pdf_task,
            page_results=[],
            success=False,
            error="批量状态管理器初始化失败",
            elapsed_seconds=time.perf_counter() - start,
        )

    # 只处理待处理的页
    pending_pages = state.pending_pages
    if not pending_pages:
        logger.info("没有待处理的页面：%s", pdf_task.pdf_path)
    else:
        logger.info("待处理页面：%s", pending_pages)

    # 创建所有待处理页的 OCR 任务（并发执行，共享全局信号量）
    async def ocr_one_page(page_number: int) -> PageOcrResult:
        async with semaphore:  # 全局信号量控制
            try:
                logger.info(
                    "开始 OCR：%s Page %d/%d",
                    pdf_task.pdf_path,
                    page_number,
                    num_pages,
                )
                image_bytes = await asyncio.to_thread(
                    render_page_to_png_bytes,
                    pdf_task.pdf_path,
                    page_number,
                )
                result = await client.ocr_page(
                    image_bytes=image_bytes,
                    page_number=page_number,
                    prompt=prompt,
                )
                if result.success:
                    logger.info(
                        "完成 OCR：%s Page %d",
                        pdf_task.pdf_path,
                        page_number,
                    )
                    # 使用批量管理器更新状态
                    batch_manager.add_completed(page_number)
                else:
                    logger.warning(
                        "OCR 失败：%s Page %d：%s",
                        pdf_task.pdf_path,
                        page_number,
                        result.error,
                    )
                    batch_manager.add_failed(page_number)
                return result
            except Exception as exc:  # noqa: BLE001
                logger.exception(
                    "处理页面失败：%s Page %d",
                    pdf_task.pdf_path,
                    page_number,
                )
                result = PageOcrResult(
                    page_number=page_number,
                    text=None,
                    success=False,
                    error=str(exc),
                )
                batch_manager.add_failed(page_number)
                return result

    # 并发执行待处理页的 OCR 任务
    page_tasks = [ocr_one_page(p) for p in pending_pages]
    page_results = await asyncio.gather(*page_tasks)

    # 强制写入剩余状态（程序退出前）
    batch_manager.force_flush()

    # 此时内存中的 state 已包含最新进度，且刚刚写回磁盘，
    # 无需再从磁盘重新读取，直接复用内存对象即可
    final_state = state

    # 构建完整页结果列表（按页号排序）
    all_page_results: List[PageOcrResult] = []
    
    # 创建页号到结果的映射
    page_result_map = {result.page_number: result for result in page_results}
    
    for p in range(1, num_pages + 1):
        if p in final_state.completed_pages:
            # 已完成的页，使用本次运行的 OCR 结果
            if p in page_result_map:
                all_page_results.append(page_result_map[p])
            else:
                # 如果是之前完成的页，创建一个空的成功结果（这种情况应该很少见）
                all_page_results.append(PageOcrResult(page_number=p, text="", success=True))
        elif p in final_state.failed_pages:
            all_page_results.append(PageOcrResult(page_number=p, text=None, success=False, error="Failed"))
        else:
            # 在本次运行中处理的结果
            if p in page_result_map:
                all_page_results.append(page_result_map[p])
            else:
                # 未处理的页
                all_page_results.append(PageOcrResult(page_number=p, text=None, success=False, error="Not processed"))

    elapsed = time.perf_counter() - start
    success = error is None and final_state.is_complete

    try:
        markdown = build_markdown(pdf_task, all_page_results)
        markdown = postprocess_markdown(markdown)
        pdf_task.output_md_path.parent.mkdir(parents=True, exist_ok=True)
        pdf_task.output_md_path.write_text(markdown, encoding="utf-8")
        logger.info("写入 Markdown：%s", pdf_task.output_md_path)
        # 完成后清理状态文件
        if final_state.is_complete:
            clear_state(pdf_task.output_md_path)
    except Exception as exc:  # noqa: BLE001
        logger.exception("写入 Markdown 失败：%s", pdf_task.output_md_path)
        error = (error or "") + f"; markdown 写入失败: {exc}"
        success = False

    return FileConvertResult(
        pdf_task=pdf_task,
        page_results=all_page_results,
        success=success,
        error=error,
        elapsed_seconds=elapsed,
    )


async def run(config: AppConfig, force_restart: bool = False) -> Tuple[List[FileConvertResult], dict]:
    """运行完整的 PDF → Markdown 转换流程。"""

    pdf_tasks = scan_pdfs(config.input_dir, config.output_dir)
    if not pdf_tasks:
        logger.warning("在目录 %s 下未发现任何 PDF 文件", config.input_dir)
        return [], {
            "total_files": 0,
            "success_count": 0,
            "failed_count": 0,
            "total_seconds": 0.0,
            "avg_seconds_per_file": 0.0,
        }

    logger.info("共发现 %d 个 PDF 文件", len(pdf_tasks))

    semaphore = asyncio.Semaphore(config.max_concurrency)
    start_all = time.perf_counter()

    async with OcrClient(config) as client:
        tasks = [
            _process_single_pdf(pdf_task, config, client, semaphore, force_restart)
            for pdf_task in pdf_tasks
        ]
        results = await asyncio.gather(*tasks)

    total_elapsed = time.perf_counter() - start_all
    success_count = sum(1 for r in results if r.success)
    failed_count = len(results) - success_count
    avg_seconds = total_elapsed / len(results) if results else 0.0

    stats = {
        "total_files": len(results),
        "success_count": success_count,
        "failed_count": failed_count,
        "total_seconds": total_elapsed,
        "avg_seconds_per_file": avg_seconds,
    }

    logger.info(
        "汇总：成功 %d 个，失败 %d 个，总用时 %.2f 秒，平均每文件 %.2f 秒",
        success_count,
        failed_count,
        total_elapsed,
        avg_seconds,
    )

    return results, stats
