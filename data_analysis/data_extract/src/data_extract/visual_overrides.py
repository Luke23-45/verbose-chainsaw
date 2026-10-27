"""Visual overrides: values read from rendered statement pages, merged
dynamically at extract time.

Why this exists: HBL and KBL FY2076-77 use a legacy/custom-encoded font
whose PDF text layer is gibberish, so the text parser cannot read their
own SOFP pages at all. The rendered pages are legible. The values were
read off the page images and checked by the accounting identity for
both columns before being saved.

How it works: the saved values live in config/visual_overrides.json
(the source of record, with source file, SHA-256, printed and PDF page
numbers, method, and identity checks). This module loads that file,
validates the identity for every entry (allowing at most 1 NPR printed
rounding), and merges the fields into a bank-year's raw record. The
merge is labelled ``method: visual_page_read`` in the raw JSON — it is
never disguised as text extraction.

Callers: run_accounting_extract.py applies this to each bank-year
right after the text parser, so a fresh extract already contains the
visual values; apply_manual_corrections.py applies it again AFTER its
own corrections, so a manual-corrections run can never silently revert
a visual value (notably KBL FY2076-77 current total assets/liabilities,
where the own report supersedes the FY2077-78 restated previous column).
"""
import json
from pathlib import Path

CONFIG = Path(__file__).resolve().parents[2] / "config" / "visual_overrides.json"

FIELDS = ("total_assets", "total_liabilities",
          "total_equity_attributable", "total_equity")


def load_overrides():
    data = json.loads(CONFIG.read_text())
    return {(o["series"], o["fy"]): o for o in data["overrides"]}


def _identity_diff(o, col):
    ta = o["total_assets"][col]
    tl = o["total_liabilities"][col]
    te = o["total_equity"][col]
    if None in (ta, tl, te):
        return None
    return ta - (tl + te)


def apply_visual_overrides(record):
    """Merge visual overrides into a raw bank-year record, in place.

    Returns True if an override was applied, False otherwise.
    Raises ValueError if an identity check fails beyond 1 NPR.
    """
    overrides = load_overrides()
    key = (record.get("series"), record.get("fy"))
    o = overrides.get(key)
    if o is None:
        return False
    for col in ("bank_current", "bank_previous",
                "group_current", "group_previous"):
        diff = _identity_diff(o, col)
        if diff is not None and abs(diff) > 1:
            raise ValueError(
                f"Visual override identity failed for {key} {col}: diff {diff}")
    for field in FIELDS:
        record[field] = dict(o[field])
    record["sofp_pages"] = [o["sofp_pdf_page"]]
    record["sopl_pages"] = [o["sopl_pdf_page"]]
    record["visual_extraction"] = {
        "method": "visual_page_read",
        "source_file": o["source_file"],
        "source_sha256": o["source_sha256"],
        "statement": o["statement"],
        "sofp_pdf_page": o["sofp_pdf_page"],
        "sofp_printed_page": o["sofp_printed_page"],
        "sopl_pdf_page": o["sopl_pdf_page"],
        "sopl_printed_page": o["sopl_printed_page"],
        "identity_check": o["identity_check"],
        "cross_check": o["cross_check"],
    }
    if o.get("supersedes"):
        record["visual_extraction"]["supersedes"] = o["supersedes"]
    note = "VISUAL EXTRACTION (page image, not text layer): " + o["note"]
    existing = record.get("manual_correction", "") or ""
    if "VISUAL EXTRACTION" not in existing:
        record["manual_correction"] = (existing + " " + note).strip() \
            if existing else note
    return True
