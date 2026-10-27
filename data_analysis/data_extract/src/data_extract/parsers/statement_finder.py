"""Locate statement pages by keyword anchor, then verify.

An anchor match only nominates a candidate page. The caller must still
confirm the statement title and that the table's year columns match
the bank-year being extracted (NFRS statements print two years side
by side; reading the wrong column is the classic silent error here).
"""

from __future__ import annotations

from ..config import load_yaml


def find_pages(pages: list[dict], statement: str) -> list[int]:
    anchors = load_yaml("extraction_rules.yaml")["statement_anchors"][statement]
    hits = []
    for page in pages:
        text = page["text"].lower()
        if any(anchor in text for anchor in anchors):
            hits.append(page["page"])
    return hits
