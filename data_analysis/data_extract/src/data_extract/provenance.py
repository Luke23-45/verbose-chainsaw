"""Provenance: every value carries its source, or it is not a value.

A panel cell without file + page + method + confidence is rejected
by writers.py. Confidence levels: 'high' (text layer, ruled table),
'medium' (text layer, unruled text), 'low' (OCR or legacy-font file).
Low-confidence cells go to manual_review/ regardless of whether
they also pass the numeric checks.
"""

from __future__ import annotations

import dataclasses


@dataclasses.dataclass
class Value:
    value: float | str | None
    source_file: str
    page: int | None
    method: str  # text_layer | table | ocr | manual
    confidence: str  # high | medium | low
    unit_as_read: str = ""
    note: str = ""

    def as_dict(self) -> dict:
        return dataclasses.asdict(self)
