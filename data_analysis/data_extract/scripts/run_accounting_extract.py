"""Run statement extraction over all 30 bank-years, write raw JSON
per PDF and a tidy accounting panel, with validation checks.

Sources: data/reports/<SERIES>/FYxxxx-xx/<SERIES>_FYxxxx-xx_annual_report.pdf
Exception: NMB FY2079-80 English file is a dead S3 link in the repo;
the usable file is ..._NP.pdf (Nepali edition, per the language
fallback rule). That file is used for that bank-year and flagged.
"""
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from data_extract.statement_parser import extract_bank_year
from data_extract.visual_overrides import apply_visual_overrides
from data_extract.dps_overrides import apply_dps
from data_extract.mps_overrides import apply_mps

ROOT = Path(__file__).resolve().parents[2]  # data_analysis/
REPO = ROOT.parent
REPORTS = REPO / "data" / "reports"
OUT = ROOT / "data_extract" / "output"
RAW = OUT / "raw"
TIDY = OUT / "tidy"
AUDIT = OUT / "audit"

SERIES = ["GBIME", "HBL", "KBL", "NIMB", "NMB"]
FYS = ["FY2076-77", "FY2077-78", "FY2078-79", "FY2079-80", "FY2080-81", "FY2081-82"]


def find_pdf(series: str, fy: str) -> Path | None:
    folder = REPORTS / series / fy
    named = folder / f"{series}_{fy}_annual_report.pdf"
    if named.exists() and named.stat().st_size > 10000:
        return named
    # Fallback: any real PDF in the folder, prefer _NP for NMB FY2079-80.
    cands = sorted(p for p in folder.glob("*.pdf") if p.stat().st_size > 10000)
    if cands:
        np_files = [p for p in cands if p.name.endswith("_NP.pdf")]
        return np_files[0] if np_files else cands[0]
    return None


def main() -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    TIDY.mkdir(parents=True, exist_ok=True)
    AUDIT.mkdir(parents=True, exist_ok=True)
    rows = []
    failures = []
    for series in SERIES:
        for fy in FYS:
            pdf = find_pdf(series, fy)
            if pdf is None:
                failures.append((series, fy, "no PDF found"))
                continue
            try:
                r = extract_bank_year(pdf)
            except Exception as exc:  # noqa: BLE001 - report, don't crash the run
                failures.append((series, fy, f"parser error: {exc}"))
                continue
            r["series"] = series
            r["fy"] = fy
            # Dynamic merge: saved visual extraction (config/
            # visual_overrides.json) is applied at extract time, so a
            # fresh extract already contains the visually read values
            # for the legacy-font bank-years, labelled as such.
            apply_visual_overrides(r)
            # DPS, same dynamic-merge pattern: config/dps.json is
            # applied at extract time, so a fresh extract already
            # contains the board-report dividend values, labelled.
            apply_dps(r)
            # MPS_post, same pattern: config/mps.json is applied at
            # extract time. Only user-approved settled entries carry
            # a price; pending rows stay blank, the rest unavailable.
            apply_mps(r)
            r["source_file_name"] = pdf.name
            (RAW / f"{series}_{fy}.json").write_text(json.dumps(r, indent=2))
            b = lambda d: d["bank_current"]  # noqa: E731
            # Derived values, Bank column, primary.
            sc = r["share_capital"]["bank_current"]
            ea = r["total_equity_attributable"]["bank_current"]
            pat = r["profit_after_tax"]["bank_current"]
            ta = r["total_assets"]["bank_current"]
            ta_prev = r["total_assets"]["bank_previous"]
            shares = sc / 100 if sc else None
            bvps = ea / shares if ea and shares else None
            avg_assets = (ta + ta_prev) / 2 if ta and ta_prev else None
            roa = pat / avg_assets * 100 if pat and avg_assets else None
            tl = r["total_liabilities"]["bank_current"]
            te = r["total_equity"]["bank_current"]
            identity_diff = (ta - (tl + te)) if ta and tl and te else None
            rows.append({
                "series": series, "fy": fy, "source_file": pdf.name,
                "sofp_pages": ";".join(map(str, r["sofp_pages"])),
                "sopl_pages": ";".join(map(str, r["sopl_pages"])),
                "total_assets": ta, "total_assets_prev": ta_prev,
                "total_liabilities": tl,
                "total_equity_attributable": ea,
                "total_equity": te,
                "share_capital": sc, "shares_outstanding_yearend": shares,
                "profit_after_tax": pat,
                "profit_attributable": r["profit_attributable"]["bank_current"],
                "eps_reported": r["eps_reported"]["bank_current"],
                "eps_reported_prev": r["eps_reported"]["bank_previous"],
                "nav_reported": r["nav_per_share_reported"]["bank_current"],
                "bvps_recomputed": bvps,
                "roa_percent_recomputed": roa,
                "identity_diff_npr": identity_diff,
            })
            print(f"{series} {fy}: TA={ta} PAT={pat} EPSrep={r['eps_reported']['bank_current']} iddiff={identity_diff}")
    with open(TIDY / "accounting_panel.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else [])
        w.writeheader()
        w.writerows(rows)
    with open(AUDIT / "extraction_failures.txt", "w") as f:
        for s, fy, msg in failures:
            f.write(f"{s} {fy}: {msg}\n")
    print(f"\nWrote {len(rows)} bank-years, {len(failures)} failures")
    for s, fy, msg in failures:
        print("FAIL", s, fy, msg)


if __name__ == "__main__":
    main()
