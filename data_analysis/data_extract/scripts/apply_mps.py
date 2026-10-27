"""Apply MPS_post to existing raw JSONs and add MPS columns to the panel.

Order of the documented pipeline:
  run_accounting_extract.py -> apply_manual_corrections.py -> apply_dps.py -> this script
This script is idempotent: re-running it re-applies the same MPS
entries from config/mps.json and re-adds the same columns.
Only settled entries fill mps_post_npr; pending rows keep a blank
price with status 'pending', and all other rows are 'unavailable'.
"""
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from data_extract.mps_overrides import apply_mps

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "output" / "raw"
TIDY = ROOT / "output" / "tidy"

MPS_FIELDS = ["mps_post_npr", "mps_disclosure_date", "mps_first_trading_date",
              "mps_price_label", "mps_status", "mps_disclosure_source",
              "mps_price_source", "mps_note"]


def main() -> None:
    counts = {"settled": 0, "pending": 0, "unavailable": 0}
    for path in sorted(RAW.glob("*.json")):
        data = json.loads(path.read_text())
        status = apply_mps(data)
        counts[status] += 1
        path.write_text(json.dumps(data, indent=2))
        m = data["market"]
        print(f"Applied MPS: {data['series']} {data['fy']} = {status}"
              + (f" {m['mps_post_npr']}" if status == "settled" else ""))
    panel = TIDY / "accounting_panel.csv"
    rows = list(csv.DictReader(open(panel)))
    for row in rows:
        data = json.loads((RAW / f"{row['series']}_{row['fy']}.json").read_text())
        m = data["market"]
        row.update({
            "mps_post_npr": m.get("mps_post_npr", ""),
            "mps_disclosure_date": m.get("disclosure_date", ""),
            "mps_first_trading_date": m.get("first_trading_date", ""),
            "mps_price_label": m.get("price_label", ""),
            "mps_status": m["status"],
            "mps_disclosure_source": m.get("disclosure_source", ""),
            "mps_price_source": m.get("price_source", ""),
            "mps_note": m["note"],
        })
    fieldnames = list(rows[0].keys())
    for f in MPS_FIELDS:
        if f not in fieldnames:
            fieldnames.append(f)
    with open(panel, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
    print(f"Panel updated: {len(rows)} rows, MPS settled={counts['settled']} "
          f"pending={counts['pending']} unavailable={counts['unavailable']}")


if __name__ == "__main__":
    main()
