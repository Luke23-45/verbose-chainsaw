"""Normalisation. Pure functions, fully tested.

- Money: NFRS statements state NPR '000 unless the header says
  otherwise. ``to_npr`` multiplies by 1,000 only when the unit as
  read is NPR '000; a value already in NPR passes through unchanged.
- Parentheses in statements mean negative; a dash or blank means
  'not stated', never zero — that distinction is preserved as None
  so validation can flag it instead of silently zeroing it.
"""

from __future__ import annotations

import re


def to_npr(value: float, unit_as_read: str) -> float:
    unit = unit_as_read.strip().lower()
    if unit in ("npr '000", "npr 000", "rs. '000", "in thousands"):
        return value * 1_000
    return value


def parse_number(text: str) -> float | None:
    """Parse a statement cell. Returns None for dash/blank (not
    stated), a float otherwise. Parentheses = negative."""
    if text is None:
        return None
    cleaned = text.strip().replace(",", "")
    if cleaned in ("", "-", "--", "–"):
        return None
    negative = cleaned.startswith("(") and cleaned.endswith(")")
    cleaned = cleaned.strip("()")
    if not re.fullmatch(r"-?\d+(\.\d+)?", cleaned):
        return None
    value = float(cleaned)
    return -value if negative else value
