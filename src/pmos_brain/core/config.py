"""Configuration management."""
import os
from pathlib import Path
from typing import Any, Optional, Dict
import yaml

class Config:
    """Configuration loader."""
    def __init__(self, config_path: Optional[Path] = None):
        self._config: Dict[str, Any] = {}
        if config_path and config_path.exists():
            self._config = yaml.safe_load(config_path.read_text()) or {}
    
    def get(self, key: str, default: Any = None) -> Any:
        keys = key.split(".")
        value = self._config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k)
            else:
                return default
        return value if value is not None else default

_config: Optional[Config] = None

def get_config() -> Config:
    global _config
    if _config is None:
        _config = Config()
    return _config
