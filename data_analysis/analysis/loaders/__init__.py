"""Typed loaders for the frozen data_extract outputs.

One loader per input family.  Every loader validates presence, columns and
dtypes, raising FileNotFoundError/ValueError naming the offending file or
line.  Loaders return plain DataFrames; joining and rule application happen in
analysis.dataset — never here.
"""
from analysis.loaders.panel import (
    load_bonusadj,
    load_merolagani,
    load_panel,
    load_price_status,
)

__all__ = ["load_bonusadj", "load_merolagani", "load_panel", "load_price_status"]
