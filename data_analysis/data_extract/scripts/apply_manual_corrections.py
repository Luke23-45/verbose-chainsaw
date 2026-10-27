"""Manual corrections for bank-years the text parser could not read.

Every value below is taken from a direct, cited source, and every
one passes an independent check (identity, BVPS, or continuity
with the next year's previous column). Nothing here is estimated.

- HBL FY2076-77 and KBL FY2076-77: their own reports use a legacy
  / custom-encoded font whose text layer is gibberish. Values are
  the previous column of the FY2077-78 report (audited, same
  statements), which is why identity and BVPS hold exactly.
  Opening assets (FY2075-76 closing) are NOT in that previous
  column, so ROA for these two years stays blank, not approximated.
- NMB FY2076-77: its own SOFP is a rotated table (p44-45) whose
  word geometry breaks the parser. Values are the previous column
  of the FY2077-78 report, plus the FY2076-77 SOPL p46 for PAT/EPS,
  plus the FY2076-77 SOFP previous column (p44 text) for opening
  assets, so ROA is computable.
- NMB FY2077-78: SOFP parsed correctly; SOPL did not. PAT/EPS are
  from the FY2077-78 SOPL p43 direct text, and match the FY2078-79
  previous column for PAT.
- NMB FY2079-80: SOFP/EPS parsed correctly; PAT did not. PAT is
  from the Nepali SOPL p39 direct text, and matches the FY2080-81
  previous column for PAT.
- SUPERSEDED (2026-10-27, visual read): HBL/KBL FY2076-77 opening
  assets are now supplied by config/visual_overrides.json, applied
  last by this script, so they are no longer blank. KBL FY2076-77
  current total assets/liabilities in this file's original entry
  (the FY2077-78 restated previous column) are likewise superseded
  by the own-report visual values; see visual_overrides.json for
  the restatement evidence.
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


def bg(gc, gp, bc, bp):
    return {"group_current": gc, "group_previous": gp,
            "bank_current": bc, "bank_previous": bp}


CORRECTIONS = {
    ("HBL", "FY2076-77"): {
        "total_assets": bg(None, None, 155884918983, None),
        "total_liabilities": bg(None, None, 138295665371, None),
        "total_equity_attributable": bg(None, None, 17589253612, None),
        "total_equity": bg(None, None, 17589253612, None),
        "share_capital": bg(None, None, 9372281428, None),
        "profit_after_tax": bg(None, None, 2586722710, None),
        "profit_attributable": bg(None, None, 2586722710, None),
        "eps_reported": bg(None, None, 27.60, None),
        "nav_per_share_reported": bg(None, None, 187.72, None),
        "manual_correction": "Previous column of HBL FY2077-78 report SOFP pp48-49 / SOPL p49; "
        "identity 138295665371+17589253612=155884918983 exact; "
        "BVPS 17589253612/93722814.28=187.67 vs NAV 187.72 (diff 0.05, flagged for review, identity still exact). "
        "Opening assets now supplied by visual extraction (see visual note appended by apply_visual_overrides).",
    },
    ("KBL", "FY2076-77"): {
        "total_assets": bg(None, None, 145971942062, None),
        "total_liabilities": bg(None, None, 128703768392, None),
        "total_equity_attributable": bg(None, None, 17268173670, None),
        "total_equity": bg(None, None, 17268173670, None),
        "share_capital": bg(None, None, 12520049469, None),
        "profit_after_tax": bg(None, None, 1158505956, None),
        "profit_attributable": bg(None, None, 1158505956, None),
        "eps_reported": bg(None, None, 12.08, None),
        "nav_per_share_reported": bg(None, None, 137.92, None),
        "manual_correction": "Original manual entry used the previous column of KBL FY2077-78 report SOFP p34 / SOPL; "
        "that entry is SUPERSEDED by the own-report visual read (see visual note appended by apply_visual_overrides): "
        "own-report identity 136073455939+17268173670=153341629609, 1 NPR below printed total 153341629610 (rounding); "
        "BVPS 17268173670/125200494.69=137.92 exact.",
    },
    ("NMB", "FY2076-77"): {
        "total_assets": bg(None, 138684555985, 179451914903, 135470409573),
        "total_liabilities": bg(None, None, 158516529660, None),
        "total_equity_attributable": bg(None, None, 20935385243, None),
        "total_equity": bg(None, None, 20935385243, None),
        "share_capital": bg(None, None, 13950987467, None),
        "profit_after_tax": bg(None, None, 1712776521, None),
        "profit_attributable": bg(None, None, 1712776521, None),
        "eps_reported": bg(None, None, 12.62, None),
        "nav_per_share_reported": bg(None, None, 150.06, None),
        "manual_correction": "Previous column of NMB FY2077-78 report SOFP pp40-41; "
        "PAT/EPS from NMB FY2076-77 SOPL p46 direct text; "
        "opening assets 135470409573 from FY2076-77 SOFP p44 previous column; "
        "identity 158516529660+20935385243=179451914903 exact; "
        "BVPS 20935385243/139509874.67=150.06 exact.",
    },
    ("NMB", "FY2077-78"): {
        "profit_after_tax": bg(3019356613, None, 2711073708, None),
        "profit_attributable": bg(2923139410, None, 2711073708, None),
        "eps_reported": bg(17.96, None, 16.66, None),
        "manual_correction": "NMB FY2077-78 SOPL p43 direct text; "
        "PAT Bank 2711073708 matches FY2078-79 previous column exactly.",
    },
    ("NMB", "FY2079-80"): {
        "profit_after_tax": bg(3296678153, None, 3222547292, None),
        "profit_attributable": bg(3296678153, None, 3222547292, None),
        "manual_correction": "NMB FY2079-80 Nepali SOPL p39 direct text; "
        "PAT Bank 3222547292 matches FY2080-81 previous column exactly.",
    },
}


def main() -> None:
    for (series, fy), corr in CORRECTIONS.items():
        path = RAW / f"{series}_{fy}.json"
        data = json.loads(path.read_text())
        for key, val in corr.items():
            data[key] = val
        path.write_text(json.dumps(data, indent=2))
        print(f"Corrected {series} {fy}")
    # Visual overrides run LAST, so a manual-corrections run can never
    # silently revert a visually read value (see visual_overrides.py).
    # In particular KBL FY2076-77 current total assets/liabilities
    # stay at the own-report visual values, not the FY2077-78
    # restated previous column, and both HBL/KBL opening assets stay
    # filled for ROA.
    for path in sorted(RAW.glob("*.json")):
        data = json.loads(path.read_text())
        if apply_visual_overrides(data):
            path.write_text(json.dumps(data, indent=2))
            print(f"Applied visual override (after manual): "
                  f"{data['series']} {data['fy']}")
    # Regenerate panel from raw JSONs (Bank column, primary).
    rows = []
    for path in sorted(RAW.glob("*.json")):
        r = json.loads(path.read_text())
        series, fy = r["series"], r["fy"]
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
            "series": series, "fy": fy, "source_file": r["source_file_name"],
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
    print(f"Panel regenerated: {len(rows)} rows")


if __name__ == "__main__":
    main()
