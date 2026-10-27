# Source register — citation master file (2026-10-27)

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
