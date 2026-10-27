"""Apply DPS to existing raw JSONs and add DPS columns to the panel.

Order of the documented pipeline:
  run_accounting_extract.py -> apply_manual_corrections.py -> this script
This script is idempotent: re-running it re-applies the same DPS
entries from config/dps.json and re-adds the same columns.
"""
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from data_extract.dps_overrides import apply_dps

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "output" / "raw"
TIDY = ROOT / "output" / "tidy"

DPS_FIELDS = ["dps_cash_percent", "dps_bonus_percent", "dps_npr",
              "dps_status", "dps_source_pdf_page",
              "dps_source_printed_page", "dps_method"]


def main() -> None:
    for path in sorted(RAW.glob("*.json")):
        data = json.loads(path.read_text())
        apply_dps(data)
        path.write_text(json.dumps(data, indent=2))
        print(f"Applied DPS: {data['series']} {data['fy']} = {data['dividend']['dps_npr']}")
    panel = TIDY / "accounting_panel.csv"
    rows = list(csv.DictReader(open(panel)))
    for row in rows:
        data = json.loads((RAW / f"{row['series']}_{row['fy']}.json").read_text())
        d = data["dividend"]
        row.update({
            "dps_cash_percent": d["cash_percent"],
            "dps_bonus_percent": d["bonus_percent"],
            "dps_npr": d["dps_npr"],
            "dps_status": d["status"],
            "dps_source_pdf_page": d["pdf_page"],
            "dps_source_printed_page": d["printed_page"],
            "dps_method": d["method"],
        })
    fieldnames = list(rows[0].keys())
    for f in DPS_FIELDS:
        if f not in fieldnames:
            fieldnames.append(f)
    with open(panel, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
    print(f"Panel updated: {len(rows)} rows, DPS columns added")


if __name__ == "__main__":
    main()
