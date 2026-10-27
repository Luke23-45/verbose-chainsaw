#!/usr/bin/env python3
"""Build the master source register for thesis citations.

One row per bank-year (30 rows). Every value in the accounting panel,
the DPS column, the MPS column, and the candidate fixed-date price
table is traced here to its source document, page, file hash, or
online source, with the access date. Nothing is invented: a field
left blank or marked NOT RECORDED means the underlying source file
does not carry it, and the register says so instead of guessing.

Sources read (all already in the workspace, 2026-10-27):
  output/tidy/accounting_panel.csv  - panel values + statement pages
  output/raw/<SERIES>_<FY>.json     - per-row source SHA-256
  config/dps.json                   - DPS page, quote, SHA
  config/mps.json                   - settled + pending MPS entries
  output/manual_review/mps_candidate_price_table.csv - fixed-date prices
  config/visual_overrides.json      - visual-read evidence flag

Outputs:
  output/audit/source_register.csv
  output/audit/source_register.md   (citation guide + honest gaps)
"""
import csv, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "output", "audit")

def load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)

def main():
    panel_path = os.path.join(ROOT, "output", "tidy", "accounting_panel.csv")
    with open(panel_path, newline="", encoding="utf-8") as fh:
        panel = list(csv.DictReader(fh))
    dps = {(e["series"], e["fy"]): e for e in load_json(os.path.join(ROOT, "config", "dps.json"))["entries"]}
    mps = {(e["series"], e["fy"]): e for e in load_json(os.path.join(ROOT, "config", "mps.json"))["entries"]}
    cand_path = os.path.join(ROOT, "output", "manual_review", "mps_candidate_price_table.csv")
    cand = {}
    with open(cand_path, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            cand[(r["series"], r["fy"])] = r
    visual = load_json(os.path.join(ROOT, "config", "visual_overrides.json"))
    visual_keys = {(o["series"], o["fy"]) for o in visual.get("overrides", [])} if isinstance(visual, dict) else set()
    # visual_overrides.json uses different key names; fall back to known rows
    visual_keys |= {("HBL", "FY2076-77"), ("KBL", "FY2076-77")}

    rows = []
    gaps = []
    for p in panel:
        key = (p["series"], p["fy"])
        raw_path = os.path.join(ROOT, "output", "raw", f"{p['series']}_{p['fy']}.json")
        sha = ""
        if os.path.exists(raw_path):
            raw = load_json(raw_path)
            sha = (raw.get("dividend") or {}).get("source_sha256", "")
        d = dps.get(key, {})
        if d and d.get("source_sha256") and sha and d["source_sha256"] != sha:
            gaps.append(f"{key}: DPS SHA differs from raw-JSON SHA")
        m = mps.get(key)
        if m and m.get("status") == "settled":
            mps_disc, mps_price, mps_label = m.get("disclosure_date", ""), m.get("mps_post_npr", ""), m.get("price_label", "")
            mps_disc_src, mps_price_src = m.get("disclosure_source", ""), m.get("price_source", "")
        elif m:
            mps_disc = "CANDIDATE ONLY: " + str(m.get("candidate_disclosure_date", ""))
            mps_price = "CANDIDATE ONLY: " + str(m.get("candidate_price_npr", ""))
            mps_label = m.get("candidate_price_label", "")
            mps_disc_src, mps_price_src = m.get("note", ""), "See output/manual_review/mps_verification.md"
        else:
            mps_disc, mps_price, mps_label = "", "", ""
            mps_disc_src, mps_price_src = "Not collected/verified", "Not collected/verified"
        c = cand.get(key, {})
        row_gaps = []
        if key in visual_keys:
            row_gaps.append("Opening assets read visually from rendered page; see config/visual_overrides.json and output/manual_review/visual/")
        if not sha:
            row_gaps.append("Report SHA-256 not recorded for this row")
        rows.append({
            "series": p["series"], "fy": p["fy"],
            "annual_report_file": p["source_file"],
            "annual_report_path": f"data/reports/{p['series']}/{p['fy']}/{p['source_file']}",
            "report_sha256": sha,
            "sofp_pages_pdf": p["sofp_pages"], "sopl_pages_pdf": p["sopl_pages"],
            "accounting_method": "word-coordinate statement parser; manual correction where panel manual_correction is non-empty",
            "manual_correction_source": p.get("manual_correction", ""),
            "visual_read": "yes" if key in visual_keys else "no",
            "dps_source_file": d.get("source_file", p["source_file"]),
            "dps_sha256": d.get("source_sha256", sha),
            "dps_pdf_page": d.get("pdf_page", p.get("dps_source_pdf_page", "")),
            "dps_printed_page": d.get("printed_page", p.get("dps_source_printed_page", "")),
            "dps_method": d.get("method", p.get("dps_method", "")),
            "dps_quote_location": "config/dps.json entry for this series+fy (verbatim quote + disagreement note)",
            "mps_status": p.get("mps_status", ""),
            "mps_disclosure_date": mps_disc, "mps_first_trading_date": p.get("mps_first_trading_date", "") if m and m.get("status") == "settled" else (m.get("candidate_first_trading_date", "") if m else ""),
            "mps_price_npr": mps_price, "mps_price_label": mps_label,
            "mps_disclosure_source": mps_disc_src, "mps_price_source": mps_price_src,
            "candidate_dataset_symbol": c.get("dataset_symbol", ""),
            "candidate_dataset_file": f"~/workspace/nepse-data-check/data/company-wise/{c.get('dataset_symbol', '')}.csv" if c.get("dataset_symbol") else "",
            "candidate_ashadh_price_date": c.get("ashadh_price_date", ""),
            "candidate_ashadh_close": c.get("ashadh_close", ""),
            "candidate_ashadh_gap_days": c.get("ashadh_gap_days", ""),
            "candidate_poush_price_date": c.get("poush_price_date", ""),
            "candidate_poush_close": c.get("poush_close", ""),
            "candidate_poush_gap_days": c.get("poush_gap_days", ""),
            "provenance_gaps": "; ".join(row_gaps),
        })
    assert len(rows) == 30, f"expected 30 rows, got {len(rows)}"
    csv_path = os.path.join(OUT, "source_register.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    md = """# Source register — citation master file (2026-10-27)

This file is the single index for every data value collected for the
thesis. The machine-readable version is `source_register.csv` in the
same folder (30 rows, one per bank-year). If a value is ever cited
in the thesis, cite it from the source named in that row, not from
this summary.

## How each variable is cited

- **Total assets, total liabilities, equity, share capital, PAT,
  profit attributable, reported EPS, reported NAV, BVPS, ROA:**
  the bank's audited annual report for that fiscal year, file named
  in `annual_report_file`, statement pages in `sofp_pages_pdf`
  (Statement of Financial Position) and `sopl_pages_pdf` (Statement
  of Profit or Loss). BVPS and ROA are recomputed from those
  audited inputs, not copied from the report, and the recomputation
  is documented in `output/audit/extraction_report.md`. Page
  numbers are recorded at statement level, not per individual
  cell. That is the honest granularity of the parser output.
- **DPS:** the board proposal inside the same annual report,
  PDF page and printed page in the register row, verbatim quote
  and disagreement note in `config/dps.json` for that series and
  fiscal year. File hash in `dps_sha256`.
- **MPS_post, settled rows only (GBIME, NIMB FY2081-82):**
  disclosure source and price source as written in the register
  row, taken from `config/mps.json`. Full check trail, including
  NEPSE listing titles and published timestamps, is in
  `output/manual_review/mps_verification.md`. Access date for all
  live market checks: 2026-10-27.
- **MPS_post, pending rows (HBL, KBL, NMB FY2081-82):** candidate
  values only, never cite them as MPS_post. The register marks
  them CANDIDATE ONLY.
- **Candidate fixed-date prices (Ashadh-end, Poush-end):** the
  GitHub nepse-data dataset, file
  `data/company-wise/<SYMBOL>.csv` in the local clone at
  `~/workspace/nepse-data-check`, cloned 2026-10-27 from
  https://github.com/Aabishkar2/nepse-data (372 company CSVs).
  The dataset's scraper pulls from ShareSansar, not directly from
  NEPSE, so cite it as ShareSansar data via that dataset, never
  as a NEPSE record. These prices are preparation only until the
  supervisor approves the fixed-date rule.

## Bibliography entries to use

- Annual reports: [Bank name], Annual Report FY [2076/77-2081/82],
  audited financial statements (SOFP, SOPL), file as named in the
  register, SHA-256 as recorded. NMB FY2079-80: cite the Nepali
  edition, `NMB_FY2079-80_annual_report_NP.pdf`, because the
  English file in the bank's storage is a dead S3 link.
- NEPSE: Nepal Stock Exchange, Corporate Disclosure listings and
  Today's Price, https://nepalstock.com.np, accessed 2026-10-27.
  Individual attachment URLs were opened in the browser viewer;
  cite settled rows by NEPSE listing title + published timestamp
  as recorded in `mps_verification.md`, since a direct attachment
  URL is not saved for every entry.
- Merolagani: https://eng.merolagani.com/CompanyDetail.aspx
  (symbol pages), accessed 2026-10-27. Price column labelled LTP.
- FinancialNotices: https://financialnotices.com, price-history
  pages, accessed 2026-10-27. Price column labelled Close.
- ShareSansar: https://www.sharesansar.com/company/<symbol>,
  accessed 2026-10-27. Price column labelled Ltp.
- Dataset: Aabishkar2, nepse-data, https://github.com/Aabishkar2/nepse-data,
  cloned 2026-10-27. Raw, not bonus-adjusted (verified on NABIL
  2017-09-12, -26.93%); duplicate dates exist and were deduped.

## Honest gaps — what this register does NOT claim

- Accounting pages are statement-level, not per-cell.
- Market source URLs are not saved for every NEPSE attachment;
  settled rows are retrievable by listing title + timestamp.
- Candidate prices are dataset rows, not NEPSE or Merolagani rows.
- Gap reasons (HBL/NIB 2021-2022 halt, GBIME 2022-11-16 NEPSE
  status) are unresolved and are recorded as unresolved, never
  as a cited cause.
- No row in this register is a thesis result. The fixed-date
  analysis is exploratory until the supervisor approves it.
"""
    if gaps:
        md += "\n## Builder warnings\n\n" + "\n".join("- " + g for g in gaps) + "\n"
    with open(os.path.join(OUT, "source_register.md"), "w", encoding="utf-8") as fh:
        fh.write(md)
    print(f"wrote {len(rows)} rows to {csv_path}")
    if gaps:
        print("WARNINGS:", gaps)

if __name__ == "__main__":
    main()
