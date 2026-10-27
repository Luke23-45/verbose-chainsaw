"""Apply the saved visual extraction to the existing raw JSONs and
regenerate the accounting panel.

Run this after run_accounting_extract.py (or after
apply_manual_corrections.py — order does not matter, because that
script also applies visual overrides last). The visual values are NOT
typed into this script: they live in config/visual_overrides.json and
are merged dynamically, with identity checks, by
src/data_extract/visual_overrides.py. The panel this writes is
therefore indistinguishable in form from a regular extraction — but
the raw JSONs still carry method=visual_page_read, so the provenance
is not hidden.
"""
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from data_extract.visual_overrides import apply_visual_overrides

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "output" / "raw"
TIDY = ROOT / "output" / "tidy"


def main() -> None:
    applied = []
    for path in sorted(RAW.glob("*.json")):
        r = json.loads(path.read_text())
        if apply_visual_overrides(r):
            path.write_text(json.dumps(r, indent=2))
            applied.append((r["series"], r["fy"]))
            print(f"Applied visual override: {r['series']} {r['fy']}")
    # Regenerate panel from raw JSONs (Bank column, primary) — same
    # formulas as apply_manual_corrections.py.
    rows = []
    for path in sorted(RAW.glob("*.json")):
        r = json.loads(path.read_text())
        sc = r["share_capital"]["bank_current"]
        ea = r["total_equity_attributable"]["bank_current"]
        pat = r["profit_after_tax"]["bank_current"]
        ta = r["total_assets"]["bank_current"]
        ta_prev = r["total_assets"]["bank_previous"]
        shares = sc / 100 if sc else None
        bvps = ea / shares if ea and shares else None
        avg = (ta + ta_prev) / 2 if ta and ta_prev else None
        roa = pat / avg * 100 if pat and avg else None
        tl = r["total_liabilities"]["bank_current"]
        te = r["total_equity"]["bank_current"]
        idd = (ta - (tl + te)) if ta and tl and te else None
        rows.append({
            "series": r["series"], "fy": r["fy"],
            "source_file": r["source_file_name"],
            "sofp_pages": ";".join(map(str, r["sofp_pages"])),
            "sopl_pages": ";".join(map(str, r["sopl_pages"])),
            "total_assets": ta, "total_assets_prev": ta_prev,
            "total_liabilities": tl,
            "total_equity_attributable": ea, "total_equity": te,
            "share_capital": sc, "shares_outstanding_yearend": shares,
            "profit_after_tax": pat,
            "profit_attributable": r["profit_attributable"]["bank_current"],
            "eps_reported": r["eps_reported"]["bank_current"],
            "eps_reported_prev": r["eps_reported"]["bank_previous"],
            "nav_reported": r["nav_per_share_reported"]["bank_current"],
            "bvps_recomputed": bvps, "roa_percent_recomputed": roa,
            "identity_diff_npr": idd,
            "manual_correction": r.get("manual_correction", ""),
        })
    rows.sort(key=lambda x: (x["series"], x["fy"]))
    with open(TIDY / "accounting_panel.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"Panel regenerated: {len(rows)} rows, "
          f"ROA present for {sum(1 for r in rows if r['roa_percent_recomputed'] is not None)}/30")


if __name__ == "__main__":
    main()
