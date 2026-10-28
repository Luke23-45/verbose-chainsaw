"""Configuration loading and path resolution.

Single source of truth for input paths, sample rules and output locations.
The config file is configs/base.yaml; tests redirect it with the
THESIS_ANALYSIS_CONFIG environment variable (call get_config.cache_clear()
after changing the variable within one process).  All path values in the YAML
are resolved relative to the analysis stage root (the parent of this package,
i.e. data_analysis/).
"""
from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
STAGE_ROOT = PACKAGE_ROOT.parent
CONFIG_PATH = PACKAGE_ROOT / "configs" / "base.yaml"
CONFIG_ENV = "THESIS_ANALYSIS_CONFIG"


@lru_cache(maxsize=1)
def get_config() -> dict[str, Any]:
    path = Path(os.environ.get(CONFIG_ENV, str(CONFIG_PATH)))
    if not path.is_file():
        raise FileNotFoundError(f"Analysis config not found: {path}")
    with path.open("r", encoding="utf-8") as handle:
        config = yaml.safe_load(handle)
    if not isinstance(config, dict):
        raise ValueError(f"Analysis config must be a YAML mapping: {path}")
    return config


def resolve(relative: str | Path) -> Path:
    path = Path(relative)
    return path if path.is_absolute() else STAGE_ROOT / path


def data_file(key: str) -> Path:
    """Path of a named data input (panel, bonusadj, price_status, merolagani)."""
    return resolve(get_config()["data"]["root"]) / get_config()["data"][key]


def paper_root() -> Path:
    return resolve(get_config()["output"]["paper_root"])


def manifest_path() -> Path:
    return paper_root() / get_config()["output"]["manifest_name"]


def analysis_setting(key: str) -> Any:
    return get_config()["analysis"][key]
