"""MPS_post merge: NEPSE-sourced market prices, merged dynamically
at extract time — the same pattern as visual_overrides and DPS.

Source of record: config/mps.json. Only bank-years the user has
approved as settled carry a price and a disclosure date. A pending
entry carries candidate fields ONLY, and they are never promoted
to mps_post_npr or disclosure_date by this module — a pending
row's panel price stays blank. A bank-year with no entry at all
is unavailable, never estimated, interpolated, or borrowed from
another date. That is a deliberate difference from DPS, whose
collection is complete (30/30) and where a missing entry raises:
MPS collection is incomplete by design, so absence is a status,
not an error.

Validation for a settled entry: disclosure date strictly before
first trading date, price positive, price label Close or LTP.
A pending entry that carries a real price/disclosure field raises,
because that would silently promote a held candidate.
"""
import json
from pathlib import Path

CONFIG = Path(__file__).resolve().parents[2] / "config" / "mps.json"


def load_mps():
    data = json.loads(CONFIG.read_text())
    return {(e["series"], e["fy"]): e for e in data["entries"]}


def apply_mps(record):
    """Merge the MPS entry into a raw bank-year record, in place.

    Returns the status applied: 'settled', 'pending', or
    'unavailable'. Raises ValueError on a malformed entry.
    """
    entries = load_mps()
    key = (record.get("series"), record.get("fy"))
    e = entries.get(key)
    if e is None:
        record["market"] = {
            "status": "unavailable",
            "note": "No MPS_post entry yet — disclosure date and price "
                    "not yet collected or verified from NEPSE records.",
        }
        return "unavailable"
    if e["status"] == "pending":
        if "mps_post_npr" in e or "disclosure_date" in e or "first_trading_date" in e:
            raise ValueError(f"Pending MPS entry for {key} carries a real "
                             f"price/date field — candidates must stay candidates")
        record["market"] = {
            "status": "pending",
            "candidate_disclosure_date": e.get("candidate_disclosure_date"),
            "candidate_first_trading_date": e.get("candidate_first_trading_date"),
            "candidate_price_npr": e.get("candidate_price_npr"),
            "candidate_price_label": e.get("candidate_price_label"),
            "note": e["note"],
        }
        return "pending"
    if e["status"] != "settled":
        raise ValueError(f"Unknown MPS status for {key}: {e['status']}")
    if not (e["disclosure_date"] < e["first_trading_date"]):
        raise ValueError(f"MPS disclosure date not before first trading date for {key}")
    if not (e["mps_post_npr"] > 0):
        raise ValueError(f"MPS price not positive for {key}")
    if e["price_label"] not in ("Close", "LTP"):
        raise ValueError(f"MPS price label not Close/LTP for {key}: {e['price_label']}")
    record["market"] = {
        "status": "settled",
        "disclosure_date": e["disclosure_date"],
        "first_trading_date": e["first_trading_date"],
        "mps_post_npr": e["mps_post_npr"],
        "price_label": e["price_label"],
        "listed_security": e["listed_security"],
        "disclosure_source": e["disclosure_source"],
        "price_source": e["price_source"],
        "corporate_action": e["corporate_action"],
        "note": e["note"],
    }
    return "settled"
