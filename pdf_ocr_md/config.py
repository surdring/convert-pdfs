from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import toml

@dataclass
class AppConfig:
    input_dir: Path
    output_dir: Path
    server_url: str = "http://0.0.0.0:8082"
    model: str = "chandra-ocr"
    max_concurrency: int = 4
    max_retries: int = 3
    request_timeout: float = 60.0
    log_level: str = "INFO"
    ocr_prompt_preset: str = "default"

    @classmethod
    def load_from_toml(cls, config_path: Path) -> "AppConfig":
        """从 TOML 文件加载配置"""
        data = toml.load(config_path)
        input_dir = Path(data["input"]["dir"])
        output_dir = Path(data["output"]["dir"])
        ocr = data.get("ocr", {})
        concurrency = data.get("concurrency", {})
        retry = data.get("retry", {})
        logging = data.get("logging", {})
        return cls(
            input_dir=input_dir,
            output_dir=output_dir,
            server_url=ocr.get("server_url", "http://0.0.0.0:8082"),
            model=ocr.get("model", "chandra-ocr"),
            max_concurrency=concurrency.get("max_concurrency", 4),
            max_retries=retry.get("max_retries", 3),
            request_timeout=retry.get("request_timeout", 60.0),
            log_level=logging.get("level", "INFO"),
            ocr_prompt_preset=ocr.get("prompt_preset", "default"),
        )

def build_config_from_args(args) -> AppConfig:
    """从命令行参数构建配置（保留兼容性）"""
    return AppConfig(
        input_dir=args.input_dir,
        output_dir=args.output_dir,
        server_url=args.server_url,
        model=args.model,
        max_concurrency=args.max_concurrency,
        max_retries=args.max_retries,
        request_timeout=args.request_timeout,
        log_level=getattr(args, "log_level", "INFO"),
        ocr_prompt_preset=getattr(args, "ocr_prompt_preset", "default"),
    )
