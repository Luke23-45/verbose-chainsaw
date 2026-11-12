# Appendix D — FROZEN table map and first-mention order (2026-11-01, step 1)

Decision: Appendix D after Appendix C, in the thesis only (no repo, no code).
Existing last numbers verified at d4b626b: Table 13, Figure 11.
New tables: Tables 14-18. New figures: NONE (the sample flow is a table, not a figure).

## Tables
- Table 14 — Annual report identification register (30 rows).
  Columns: Series | FY | Report file | Edition / language | Retrieval route |
  PDF pages | Size (MB) | SHA-256 (first 12 hex).
  Row key: Series + FY (shared with Appendices A and B).
- Table 15 — Statement locators (30 rows).
  Columns: Series | FY | SOFP (PDF pp.) | SOPL (PDF pp.) | DPS (PDF p.,
  printed p.) | Indicators / highlights locator.
  Indicators column rule: the PDF page on which the printed EPS and NAV for
  that row were both located in the highlights/indicators table, where such a
  page was confirmed; otherwise the named section (with its start page where
  confirmed). Confirmed both-pages: GBIME 71, 65, 68, 73, 23, 33;
  HBL 38, 41, 41, 44, 41 (FY2077/78-FY2081/82); NMB FY2079/80 p. 107 (Nepali),
  FY2081/82 p. 104; NMB spans FY2076/77 pp. 45-46, FY2080/81 pp. 112-113.
  Section-level: HBL FY2076/77 Comparative Financial Indicators (from p. 28);
  KBL FY2076/77 Review of the Financial Indicators of previous years (p. 30),
  FY2077/78 and FY2078/79 no titled indicators table located in text search,
  FY2079/80 p. 160, FY2080/81 p. 165, FY2081/82 p. 172 (Major Financial
  Indicators headings); NIMB Major Financial Highlights (from pp. 156/159/
  167/168/172/164); NMB FY2077/78 Financial Highlights (from p. 27), FY2078/79
  Key Financial Highlights (p. 31).
- Table 16 — Statute and calendar sources.
  Rows: BAFIA Section 59(2) three-month submission duty; BAFIA Section 59(2)
  nine-month publication duty (the event clock); NEPSE trading calendar
  (Sunday-Friday sessions, holidays); nepse-data dataset (Aabishkar2);
  ShareSansar; Merolagani; FinancialNotices.
  Columns: Source | What it supplies | Access / terms line.
- Table 17 — Variable codebook.
  Rows: MPS_RD, EPS, BVPS, ROA, DPS, Post.
  Columns: Variable | Definition | Formula / construction | Source field |
  Rule | Unit.
- Table 18 — Sample construction log.
  Block 1 (exclusions, arithmetic closes): 30 bank-years collected;
  minus HBL FY2077/78 (54 days, merger-related suspension);
  minus NIMB FY2077/78 (47 days, merger-related suspension);
  equals 28 analysis rows.
  Block 2 (treatments and disclosures, subtract nothing): NIB to NIMB series
  mapping; FY2078/79 entity mismatch (pre-merger reports priced post-merger
  symbols); merger-transition year FY2079/80; own-current rule and restatement
  treatment (R8 only); DPS nil rule.

## First mentions (frozen)
- Chapter III section 3.4 gains a pointer sentence to Appendix D and
  Tables 14-16 (sources and provenance).
- Chapter III section 3.5 gains a pointer sentence to Table 17 (codebook).
- Chapter III section 3.3.4 gains a pointer sentence to Table 18 (sample log).
- Appendix D introduction mentions Tables 14-18 by number.
- Each Appendix D section mentions its own table by number.
- No table or figure in Appendix D is mentioned only in its caption.

## Verified facts the draft must use (step 2, 2026-11-01)
- 30 files exist; all SHA-256 recomputations match the register; all
  SOFP/SOPL/DPS pages within range; DPS pages match dps.json 30/30;
  total 5,663 pages; 314 MiB on disk.
- Reports collected October 2026 (register dated 2026-10-27); per-report
  retrieval dates were not recorded, so D.2 states the collection window
  and the re-verification date 2026-11-01, never a per-file date.
- HBL reports came from Wayback captures of the bank's own listing
  (28th-33rd AR pattern); individual snapshot URLs/timestamps were not
  recorded, so D.2 gives the pattern and route, not invented URLs.
- GBIME suspension gap corrected: last trade 15 Jun 2022 (close 251.4),
  no rows 16 Jun-6 Dec 2022, resumption 7 Dec 2022 (close 221.4).
  HBL gap: last trade 12 May 2021 (487.0), no rows 13 May 2021-5 Jun 2022,
  resumption 6 Jun 2022 (358.9). NIB gap: last trade 12 May 2021 (453.0),
  no rows 13 May 2021-29 May 2022, resumption 30 May 2022 (367.7).
- Halt evidence tier: merger MoU dates, shareholder rejection, resumption
  dates (news sources) plus dataset boundaries (primary price data).
  NEPSE-notice-level confirmation is outstanding and is stated as such.
- Joined panel: 30 rows, 28 clean (gap <= 5), 2 excluded.
- HC3 design: dummy-variable LSDV (explicit bank + year dummies).
  Model 1: n=28, k=12, df=16, max leverage 0.6766.
  Model 2: n=28, k=14, df=14, max leverage 0.9324. No leverage equals 1.
  Software: analysis requirements specify statsmodels >= 0.14 (Python);
  no exact version is claimed.
- Dataset: Aabishkar2 nepse-data, https://github.com/Aabishkar2/nepse-data,
  clone of 2026-10-27, series current to 2026-10-26, columns
  published_date/open/high/low/close/per_change/traded_quantity/
  traded_amount/status, scraper pulls from ShareSansar, no LICENSE file
  in the repository (terms line states this).
- Target deadlines (verified from Table 2 observation minus gap):
  FY2076/77 13 Apr 2021; FY2077/78 13 Apr 2022; FY2078/79 13 Apr 2023;
  FY2079/80 12 Apr 2024; FY2080/81 13 Apr 2025; FY2081/82 13 Apr 2026.
  Event clock: nine-month publication duty, read as FY-end + 9 months =
  Chaitra-end of the following fiscal year, mid-April AD.
