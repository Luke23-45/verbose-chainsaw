"""DPS merge: values read from board-report / AGM pages, merged
dynamically at extract time — the same pattern as visual_overrides.

Source of record: config/dps.json (one entry per bank-year, with
source file, SHA-256, PDF page, quote, status, and a note recording
any disagreement that was resolved). The merge is labelled with its
method (text_page_read or visual_page_read) in the raw JSON — it is
never disguised as statement-table extraction.

Validation: DPS NPR must equal cash % (face value NPR 100) within
0.001, and a documented-nil entry must have cash % 0. No entry is
ever defaulted to zero: every one of the 30 entries in dps.json was
resolved from its own report, and a missing entry raises, it does
not fill a blank.
"""
import json
from pathlib import Path

CONFIG = Path(__file__).resolve().parents[2] / "config" / "dps.json"


def load_dps():
    data = json.loads(CONFIG.read_text())
    return {(e["series"], e["fy"]): e for e in data["entries"]}


def apply_dps(record):
    """Merge the DPS entry into a raw bank-year record, in place.

    Returns True if an entry was applied. Raises ValueError if no
    entry exists for the bank-year or if DPS != cash %.
    """
    entries = load_dps()
    key = (record.get("series"), record.get("fy"))
    e = entries.get(key)
    if e is None:
        raise ValueError(f"No DPS entry for {key} — DPS stays unavailable, never zero-filled")
    if abs(e["dps_npr"] - e["cash_percent"]) > 0.001:
        raise ValueError(f"DPS != cash % for {key}: {e['dps_npr']} vs {e['cash_percent']}")
    if e["status"] == "documented-nil" and e["cash_percent"] != 0:
        raise ValueError(f"Documented-nil DPS entry with non-zero cash % for {key}")
    record["dividend"] = {
        "method": e["method"],
        "source_file": e["source_file"],
        "source_sha256": e["source_sha256"],
        "cash_percent": e["cash_percent"],
        "bonus_percent": e["bonus_percent"],
        "dps_npr": e["dps_npr"],
        "status": e["status"],
        "pdf_page": e["pdf_page"],
        "printed_page": e["printed_page"],
        "quote": e["quote"],
        "note": e["note"],
    }
    return True
