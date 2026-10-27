# Full detail report: data collected, research done, and the MPS_post blocker

**Thesis:** *Accounting Fundamentals and Post-Disclosure Share Prices: Evidence from Selected Nepalese Commercial Banks*
**Date of work:** Tuesday, 2026-10-27 (all dates in this report are 2026-10-27 unless stated otherwise)
**Repository:** `~/workspace/verbose-chainsaw` (GitHub: Luke23-45/verbose-chainsaw, branch main)
**Author of this report:** Muse, from the working files listed in the Appendix. Every number below was re-read from those files on 2026-10-27 before writing, not copied from chat memory.
**Status labels used throughout:** *settled* = verified enough to use under the stated rule; *pending* = candidate values exist but the row is held and must never be used as data; *locator only* = an aggregator date or price exists but it is not settled; *unavailable* = not collected or not verified; *exploratory* = computed for preparation only, never a thesis result.

## 1. The thesis model, exactly as proposed

Dependent variable: **MPS_post**, post-disclosure market price per share, NPR.

> Post-disclosure market price per share, measured in NPR, is the closing price on the first NEPSE trading day with a calendar date strictly later than the NEPSE disclosure date for the corresponding audited annual financial statements. The same rule is applied to every sampled bank series and fiscal year. A retrospectively adjusted price series is not substituted.

Explanatory variables, all from audited annual reports:

- **EPS:** audited basic EPS where available; otherwise profit attributable to ordinary equity holders / weighted-average ordinary shares. Audited retrospective restatements after bonus issues or splits are retained.
- **DPS:** cash dividend per share recommended for that fiscal year and publicly disclosed by the MPS observation date. Used whether or not it was later approved or paid. A documented decision not to recommend cash is DPS = 0. If the recommendation cannot be established by the MPS date, DPS is unavailable, never zero by default. Bonus shares are not cash DPS. Cash % converts as cash % x NPR 100 face value.
- **BVPS:** ordinary shareholders' equity at fiscal year-end / ordinary shares outstanding at fiscal year-end.
- **ROA (%):** profit after tax / average total assets x 100, average = (opening + closing total assets) / 2.

Intended analysis: pooled OLS, descriptive and correlational, not causal:

```
MPS_post(i,t) = b0 + b1*EPS(i,t) + b2*DPS(i,t) + b3*BVPS(i,t) + b4*ROA(i,t) + e(i,t)
```

i = 5 bank series, t = FY2076/77 to FY2081/82, intended n = 30, parameters k = 5, intended degrees of freedom = 25. A bank-year enters the regression only if complete for all model variables. Missing or unverifiable values are reported as unavailable. Never impute.

Merger-transition rule: FY2079/80 is a merger-transition year. GBIME absorbed Bank of Kathmandu on 2023-01-09 (swap 1:1). HBL acquired Civil Bank on 2023-02-24 (swap 100:80.28). KBL absorbed NCC Bank on 2023-01-01 (swap 1:1). NIMB resulted from Nepal Investment Bank + Mega Bank on 2023-01-11 (swap 100:90). NMB is the unmerged reference bank. Record the reporting institution per bank-year and flag transition years; regression coefficients are not interpreted as merger effects.

Language rule (Krishna's decision, 2026-10-27): English first, Nepali as fallback when English is unavailable. Language does not change the underlying audited data.

## 2. Annual reports collected: 30 of 30

Target from `data/README.md`: 30 audited annual reports, 5 series x 6 fiscal years FY2076/77 to FY2081/82. Final verified state: **30/30 present, 314 MB**, checklist updated to 30 done, 0 unchecked. Discovery dry run inventoried 31 files (30 real PDFs + 1 known non-PDF, see below), 5,663 pages (5,084 text-layer, 579 image-only).

- **GBIME:** 6/6 English, 126-352 pages.
- **HBL:** 6/6, retrieved from Wayback Machine captures of the bank's own annual-report listing, because its live site refused or reset connections.
- **KBL:** 6/6, from Kumari Bank reports pages and backend storage. Its FY2076/77 first download was a 904-byte blocked-page HTML file, successfully re-fetched as a real 188-page PDF.
- **NIMB:** 6/6, from nimb.com.np. Pre-merger years are Nepal Investment Bank Ltd reports, as the checklist requires.
- **NMB:** 6/6 already in the repository.

One accepted caveat: `data/reports/NMB/FY2079-80/NMB_FY2079-80_annual_report.pdf` is not a PDF. It is a small pre-existing S3 NoSuchKey XML error file (a dead English link in NMB's own storage). The usable report is the Nepali edition beside it, `NMB_FY2079-80_annual_report_NP.pdf`, 150 pages. The set is therefore 29 English reports + 1 Nepali fallback. That Nepali file has a legacy non-Unicode font whose text layer produces Latin-looking gibberish for labels; it was never read through a guessed font mapping. Its numerals, note numbers, statement structure, and direct page reading are usable with explicit verification.

Annual-report PDFs cannot supply MPS_post. That variable requires, separately from NEPSE: audited-statement disclosure date, first trading day strictly after that date, closing price on that day, dividend-recommendation source and status, and share-capital actions between fiscal year-end and the price date. No parser may invent market data or substitute a PDF price for MPS_post.

## 3. Extraction system and quality standard

Location: `~/workspace/verbose-chainsaw/data_analysis/data_extract/`. Tools: PyMuPDF (text layer, word coordinates), pdfplumber as supporting route, pandas, PyYAML, pytest. Tesseract/OCR fallback only. LLM extraction was deliberately rejected as source of record. Venv Python: `data_analysis/data_extract/.venv/bin/python`, tests need `PYTHONPATH=src`, 6 tests pass.

Quality standard (Krishna's call, professor-grade, recorded in `data_extract/QUALITY.md` as gates G1-G10):

1. G1 Provenance: every value carries source file, hash, page, method, confidence, unit as read.
2. G2 Both columns: extract Group and Bank where both print; Bank is primary; Group stays in raw JSON so the choice is auditable and reversible.
3. G3 Exact identities: total assets = total liabilities + total equity, allowing only stated published rounding.
4. G4 Recompute, never copy: EPS, BVPS, ROA recomputed from audited inputs and compared with reported values; disagreements go to review, never averaged away.
5. G5 Prior-year continuity: prior-year columns in year t+1 should match year t current columns unless the report itself restates; restatements recorded, and each year uses its own current column. A later restatement never overwrites an earlier year's value.
6. G6 Counted completeness: counts per bank and variable, every missing cell named; never impute; DPS zero only for a documented nil recommendation.
7. G7 Manual verification: all 30 bank-years checked against key statement lines, not a sample.
8. G8 No silent fallbacks: dash or blank = "not stated", not zero; OCR low-confidence flagged; legacy-font text never guessed. Amendment (visual reading): visual page reading is an approved exception only when the value is read from a rendered page image, saved in `config/visual_overrides.json` with source file, SHA-256, printed and PDF page numbers, merged dynamically at extract time, labelled `method=visual_page_read` in raw JSON, and checked by the accounting identity for both columns. Never typed directly into the panel.
9. G9 Reproducibility: hash sources, record config and code, unit-test pure functions, repeatable outputs.
10. G10 Separation: a verified accounting panel does not complete the model dataset; MPS_post and DPS are separate, and analysis stays gated.

Parser discoveries that shaped the implementation (in `src/data_extract/statement_parser.py`):

- NFRS statements print four numeric columns in order: Group current, Group previous, Bank current, Bank previous.
- Note numbers are language-independent anchors: SOFP 4.1-4.28, SOPL 4.29-4.41. NIMB writes 4.01, 4.02, normalised to 4.1, 4.2.
- Ordinary text extraction is unreliable: HBL text order can be column-ordered; labels wrap; some subtotal rows duplicate each number twice; some PDFs hold two printed pages per PDF page.
- GBIME pages are spreads (about 1190 pt wide); the parser splits at the midpoint before row reconstruction.
- Word-coordinate row reconstruction worked well for most English and Nepali reports.
- KBL audited statements are not where simple title searches suggest; the Kumari FY2080/81 interim/condensed SOFP on p.162 must not be mistaken for the audited annual SOFP.
- Some Global IME EPS/NAV rows have only two numbers, Bank current and Bank previous: EPS FY2080/81 Bank current 16.99, previous 22.06; NAV FY2080/81 Bank current 169.97, previous 165.09.
- NMB FY2076/77 SOFP is a rotated/sideways table whose word geometry breaks ordinary reconstruction.
- HBL FY2076/77 and KBL FY2076/77 have legacy/custom-encoded text layers whose labels are effectively gibberish.
- Use statement position for total rows because total labels differ by language and font.
- Bank is the primary panel column. Reported EPS is the panel EPS; year-end-share recomputation is a diagnostic only (definition uses weighted-average shares).

Pilot verification, GBIME FY2080/81, both identities exact: Group 548,625,844,867 + 63,153,517,329 = 611,779,362,196; Bank 543,110,969,431 + 61,407,147,643 = 604,518,117,074.

Pipeline order, documented and verified: `scripts/run_accounting_extract.py` -> `scripts/apply_manual_corrections.py` -> `scripts/apply_dps.py` -> `scripts/apply_mps.py`. The manual step regenerates the panel from raw JSONs without DPS/MPS columns, so DPS and MPS must be re-added last. Raw JSONs keep the `market` dict throughout.

## 4. Accounting extraction: 30 of 30

Panel: `data_extract/output/tidy/accounting_panel.csv` (30 rows). Raw: `output/raw/<SERIES>_<FY>.json`. Report: `output/audit/extraction_report.md`.

Present for 30/30: total assets, total liabilities, total equity attributable, total share capital, profit after tax, profit attributable, reported EPS, reported NAV per share. Derived: shares outstanding = share capital / NPR 100; recomputed BVPS 30/30; recomputed ROA 30/30 after the visual phase (28/30 before it).

Panel summary across all 30 rows (recomputed from the panel file): EPS mean 14.79, sd 6.81, min 0.02, max 28.07. BVPS mean 162.39, sd 18.48, min 132.71, max 198.28. ROA mean 1.04%, sd 0.48, min 0.00%, max 1.79%. Total assets range NPR 153,341,629,610 to NPR 688,080,397,999.

Identity outcome: exact at integer level for most years; only 1 NPR printed-rounding differences in NMB FY2079/80, NMB FY2080/81, NMB FY2081/82, and (after visual correction) KBL FY2076/77. No bank-year differs by more than 1 NPR. Maximum absolute identity difference in the panel as re-read: 1.0 NPR.

BVPS vs printed NAV: most agree to about 0.01 NPR; NIMB prints NAV in whole NPR (differences up to about 0.40 are rounding). Flagged disagreements, not overwritten:

- HBL FY2076/77: recomputed BVPS 187.67 vs printed NAV 187.72 (diff 0.05).
- NMB FY2081/82: recomputed BVPS 175.18 vs printed NAV 174.49 (diff 0.69); its printed previous-year NAV 156.93 also mismatches FY2080/81's printed current NAV 157.74.

EPS: reported EPS retained. Year-end-share recomputation differed by more than 0.50 NPR in exactly five flagged years, documented not "fixed": GBIME FY2076/77 (recomputed 15.33, reported 17.99), GBIME FY2079/80 (18.71 / 22.06), HBL FY2079/80 (7.22 / 9.18), KBL FY2076/77 (9.25 / 12.08), NIMB FY2079/80 (10.90 / 13.92).

### Manual corrections (in `scripts/apply_manual_corrections.py`, sources in the panel's manual_correction column)

- **HBL FY2076/77:** from previous column of HBL FY2077/78 audited report, SOFP pp.48-49, SOPL p.49: total assets Bank 155,884,918,983; total liabilities 138,295,665,371; equity attributable = total equity 17,589,253,612; share capital 9,372,281,428; PAT = profit attributable 2,586,722,710; EPS 27.60; NAV 187.72. Identity exact.
- **KBL FY2076/77:** from previous column of KBL FY2077/78 audited report, SOFP p.34 and its SOPL, later superseded for total assets and total liabilities by the visual read (see below): equity attributable = total equity 17,268,173,670; share capital 12,520,049,469; PAT = attributable 1,158,505,956; EPS 12.08; NAV 137.92.
- **NMB FY2076/77:** FY2077/78 previous columns (SOFP pp.40-41) + own SOPL p.46 + own SOFP p.44 previous column for opening assets: total assets 179,451,914,903; opening total assets 135,470,409,573; total liabilities 158,516,529,660; equity 20,935,385,243; share capital 13,950,987,467; PAT = attributable 1,712,776,521; EPS 12.62; NAV 150.06. Identity exact, BVPS 150.06, ROA about 1.0877%.
- **NMB FY2077/78:** parser SOFP correct (total assets Bank 231,546,858,432; share capital 16,325,960,853; NAV 146.66); PAT/EPS from own SOPL p.43 text: PAT Group 3,019,356,613, PAT Bank 2,711,073,708; attributable Group 2,923,139,410, Bank 2,711,073,708; EPS Group 17.96, Bank 16.66. Bank PAT matches FY2078/79 previous column exactly. Continuity note: FY2078/79's previous-column EPS is 14.76, not 16.66, an IAS 33 bonus-issue restatement; panel uses each year's own current EPS.
- **NMB FY2079/80:** parser SOFP/EPS correct (total assets Bank 287,777,140,694; EPS 17.55); PAT from Nepali SOPL p.39 text: PAT Group 3,296,678,153, Bank 3,222,547,292; attributable set to the same values. Bank PAT matches the FY2080/81 previous column exactly.

### Visual extraction: the two ROA gaps, closed 2026-10-27

- **HBL FY2076/77 SOFP is PDF p43, printed p41:** Total Assets Group 2077 156,917,788,247 / Group 2076 133,862,215,596 / Bank 2077 155,884,918,983 / Bank 2076 133,151,142,073. Bank SOPL is PDF p44 (printed p42), PAT Bank 2,586,722,710. Source SHA-256: 3b3ed73d00cac45eb1da78ca2ff18a25cced9df37b23d754f37c40dfa7db76ca. Opening Bank total assets = 133,151,142,073. ROA = 1.7899%.
- **KBL FY2076/77 SOFP is PDF p49, printed p53; SOPL PDF p50, printed p54.** Source SHA-256: a86ac977fc7f6a065baa6aa9b4f3a764672a17abe2605d1c35d96ee695324f43. Opening Bank total assets = 105,311,485,153.
- **Material correction from the visual read, KBL FY2076/77 current year:** own-report values are total assets 153,341,629,610 and total liabilities 136,073,455,939, not the FY2077/78 previous-column values. Difference 7,369,687,548 NPR in both total assets and total liabilities, exactly the derivative financial instruments lines. The FY2077/78 previous column is a restatement. Per gate G5 the panel was corrected. Identity on own values: 136,073,455,939 + 17,268,173,670 = 153,341,629,609 (1 NPR below printed total, rounding). ROA on the consistent own-report basis = 0.8958%.
- Mechanism: `config/visual_overrides.json` + `src/data_extract/visual_overrides.py` (validates identity within 1 NPR, merges, labels `method=visual_page_read`) + `scripts/apply_visual_overrides.py`. Wired into both `run_accounting_extract.py` and `apply_manual_corrections.py` (applied last). Evidence images in `output/manual_review/visual/`.
- Verification: fresh full extract (30 bank-years, 0 failures) then manual corrections gives ROA 30/30, max identity diff 1 NPR, tests 6 passed.

### Continuity and restatement findings (report restatements, not extraction errors)

- GBIME FY2078/79 previous total assets 346,141,698,952 vs FY2077/78 current 345,423,260,183 (diff 718,438,769).
- HBL FY2080/81 previous total assets 334,269,983,478 vs FY2079/80 current 332,392,900,007 (diff 1,877,083,471; Civil Bank merger period).
- KBL FY2078/79 previous vs FY2077/78 current differed by 9,587,393; KBL FY2079/80 previous total assets 213,155,824,611 vs FY2078/79 current 212,108,438,392 (diff 1,047,386,219; NCC merger period).
- NMB EPS previous columns restate for bonus issues (see manual corrections above).
- EPS restatement audit (panel, previous column in year t+1 vs current column in year t): GBIME FY2076/77 (17.99 vs 15.33), HBL FY2077/78 (28.07 vs 27.60), NMB FY2077/78 (16.66 vs 14.76). NMB FY2076/77 is recorded as restated by the audit script against a blank previous column, so that one entry is ambiguous and is flagged as such here, not asserted.

## 5. DPS extraction: 30 of 30

Locator: `scripts/extract_dps_candidates.py` -> `output/manual_review/dps_candidates.json`. Five parallel readers (one per bank) read full board-report and AGM pages under locked rules; every flagged disagreement was lead-verified independently before merging. Returns in `output/manual_review/dps_tables_review.md`.

Implementation (dynamic-merge pattern): source of record `config/dps.json` (file, SHA-256, PDF page, printed page, verbatim quote, status, method, disagreement notes; built by `scripts/build_dps_config.py`); merge `src/data_extract/dps_overrides.py` (validates DPS NPR == cash % within 0.001, documented-nil must have cash % 0, missing entry raises rather than zero-filling) + `scripts/apply_dps.py`. Pipeline order: run -> manual corrections -> dps.

Final verification 2026-10-27: DPS 30/30, ROA 30/30, max identity diff 1 NPR, tests 6 passed. Panel DPS status counts as re-read: proposed 18, documented-nil 12. Panel DPS mean 3.59, sd 3.78, min 0.00, max 12.50.

### DPS results (cash %, which equals DPS in NPR; FY2076/77 to FY2081/82; bonus % stored separately, never added)

| Series | FY76/77 | FY77/78 | FY78/79 | FY79/80 | FY80/81 | FY81/82 |
|---|---|---|---|---|---|---|
| GBIME | 2.00 | 3.50 | 10.60 | 8.00 | 0.00 | 8.00 |
| HBL | 6.00 | 4.62 | 11.11 | 0.00 | 0.00 | 0.00 |
| KBL | 3.15 | 2.67 | 12.50 | 0.00 | 0.00 | 0.00 |
| NIMB | 5.50 | 3.389 | 7.00 | 0.00 | 0.00 | 0.00 |
| NMB | 3.20 | 3.30 | 8.25 | 0.00 | 0.00 | 5.00 |

Notes: GBIME FY2080/81 is bonus-only, 5.50% bonus, cash 0.00, confirmed by AGM/Dividends table, PDF p54. NIMB FY2077/78 cash is printed to three decimals, recorded exactly as 3.389.

### Disagreement-resolution log (lead-verified 2026-10-27)

- **NIMB FY2078/79:** proposal note p145, 7.00% cash / 4% stock (amounts NPR 1,281,527,893 / 732,301,653), wins over the 5-year summary table p146 (cash 4.0%, split swapped; total 11.0% agrees). Proof: NIMB FY2079/80 equity/distributable pages (pp.54, 119) show bonus issued 732,301,653 and cash dividend paid 1,281,527,893, exactly the proposal-note amounts.
- **NMB FY2077/78:** Board section 8 p17 and AGM notice (12.50% stock / 3.30% cash, total 15.80%; AGM amounts check exactly: cash 538,756,708.14, bonus 2,040,745,106.58 on paid-up 16,325,960,852.66) win over Chairman p8 (12% / 3.50%, sums to 15.50, not 15.80).
- **KBL FY2076/77:** assigned to FY2076/77 despite a board-report year mislabel ("for FY2075/76"), proved by Note 5.13 (BOD 6 Nov 2020), p35, amount checks against panel share capital, and FY2077/78 equity statement (bonus issued 1,358,425,367, cash paid 394,381,558, lead-checked). Subsidiary proposals excluded throughout KBL.
- **KBL FY2080/81 nil:** printed BOD date 2 January 2024 predates FY2080/81 year-end and is not quoted as verified; the nil substance is documented and accepted.
- **HBL FY2076/77 (visual):** 14% bonus + 6% cash, corroborated by FY2077/78 Principal Indicators p38.
- **NMB FY2079/80 nil (Nepali visual):** lead read rendered Board section 8, PDF p14 / printed p14, directly (evidence image `output/manual_review/visual/NMB_FY2079-80_p14.png`): decision to retain distributable profit without distributing dividend; AGM notice pp.6-7 has no dividend agenda item.
- **NMB FY2080/81 trap avoided:** a 17% cash dividend on p22 is by a subsidiary, not NMB itself; correctly not used.
- **GBIME summary-table trap:** GBIME summary tables show the previous AGM's approved dividend alongside the current proposal; picking the approved column gives the previous year's figures.
- GBIME FY2081/82 lead-verified: board p108 and Distribution of Profit p121 both 8.00% cash only, amount 3,049,268,209.28.

## 6. MPS_post: deep research, then live verification

Research directory: `~/workspace/research_notes/mps-post-nepse-disclosure-prices-20261027-0148/` (report.md plus notes files). Presentation artifact slug `mps-post-research` (a presentation, not a verification). Research mission: exact section 07 definition; source hierarchy NEPSE first, bank second, Merolagani/ShareSansar locators only; no adjusted series, no year-end, principal-indicator, or unaudited substitutions; never guess, never zero-fill.

Research coverage outcome: 4 priced, 5 locator-only, 1 candidates-no-price, 20 unavailable. No row was NEPSE-primary-verified at that stage.

Research-priced values (all FY2081/82, locator-corroborated only at research stage): NMB disclosure 2025-12-16 -> price date 2025-12-17 -> NPR 256.10 (two sources agreed); GBIME disclosure candidates 2025-10-16 -> 2025-10-19 -> 240.00 (primary) vs 2025-10-15 -> 2025-10-16 -> 236.00 (alternative); HBL disclosure candidate 2025-12-24 -> 2025-12-28 -> 191.90; NIMB disclosure candidate 2025-12-24 -> 2025-12-28 -> 193.

Locator-only research rows: GBIME FY2077/78 disclosure 2021-11-19 (Merolagani id=40885); GBIME FY2078/79 2022-11-15 (id=45325); GBIME FY2079/80 2023-11-18 (id=51246); NIMB FY2079/80 2024-02-29 (id=52897, candidate price date 2024-03-03); NIMB FY2080/81 2025-02-04 (id=58305, candidate price date 2025-02-05).

KBL FY2081/82 at research stage: primary candidate disclosure 2025-12-14 -> price date 2025-12-15; alternative 2025-12-12 -> 2025-12-14; prices not obtained (live-browser budget exhausted). A ShareSansar announcement dated 2026-02-11 post-dates the January 2026 AGM and was not treated as the disclosure anchor at research stage.

Unavailable 20 rows at research stage: GBIME FY2076/77 and FY2080/81; HBL FY2076/77-2080/81 (all five); KBL FY2076/77-2080/81 (all five); NIMB/NIBL FY2076/77-2078/79 (pre-merger; symbol continuity NIBL -> NIMB per year still to confirm at that stage); NMB FY2076/77-2080/81 (all five). Dividend board dates, AGM dates, and AGM-conclusion reports were deliberately not used as disclosure dates.

Method findings: Merolagani datewise lookup works only with autocomplete symbol selection (plain ordinary-share entry, avoiding bonds/promoter entries). Price labels differ by source (Merolagani LTP, FinancialNotices Close, NEPSE Close Price* and LTP). NEPSE price-lookup reach to 2020 was not established at research stage. No-trade-day handling was not established from a NEPSE source; the report recommended distinguishing (a) first calendar day the market was open from (b) first day the stock itself traded, never silently carrying a previous close forward. Trading calendar 2020-2025: Sunday-Thursday, Friday/Saturday weekend, plus Nepali public holidays; the Monday-Friday shift effective 2026-04-06 must not be applied retrospectively. Disclosure rules: audited annual statements within 5 months of FY-end (SEBON Listing Regulations Ch.6 Reg.22); quarterly reports within 30 days/one month (unaudited); price-sensitive/Schedule 16 events immediate (within 2-3 days), including dividend/bonus decisions with at least 7 days' notice before book closure; a Companies Act 6-month tension exists and must be flagged if a deadline is cited.

Values that must NOT be substituted for MPS_post: NMB principal-indicator "Market Value Per Share" (FY2077/78: 440; 2078/79: 261; 2079/80: 226; 2080/81: 218; 2081/82: 270); GBIME quarter-end market prices (Q4 FY2076/77: 239.00; Q1 FY2080/81: 202; Ashad-end 2080: 186); unverified thesis-excerpt GBIME MPS figures.

Research boundaries: public sources only, no sign-in/payment/downloads; a constructed NEPSE API URL returned HTTP 401 on 2026-10-27 and was not retried or bypassed; FinancialNotices' verification page was treated as a blocked fetch, not circumvented.

### Live verification, batches 1-3 (all findings in `output/manual_review/mps_verification.md`)

**Batch 1, HBL, NIMB, KBL FY2081/82 prices and NEPSE listings:**

- **HBL:** NEPSE Corporate Disclosure listing shows "33th AGM Notice of Himalayan Bank [HBL]", published 2025-12-24 10:24:55, approved 10:26:47; separate book-close information same day 15:25:37. Merolagani AGM detail (id 63402) headline announces the AGM only; its agenda lists FY2081/82 financial highlights. First trading day 2025-12-28 (2025-12-25 Christmas holiday on NEPSE holiday listing; Fri/Sat weekend). Price 2025-12-28 confirmed in two agreeing sources: FinancialNotices CLOSE 191.90 (open 186, high 191.90, low 186, volume 82,306) and Merolagani LTP 191.90, same volume. No dividend confirmed by a separate NEPSE entry dated 2025-12-23 at that stage.
- **NIMB:** NEPSE shows "39th AGM and book close notice of NIMB", published 2025-12-24 10:02:00, approved 10:02:40. Merolagani detail (id 63413) explicitly states the bank published its annual financial statement for FY2081/82. Price 2025-12-28 confirmed in two agreeing sources: FinancialNotices CLOSE 193 (open 189, high 193, low 188.6, volume 133,425) and Merolagani LTP 193.00, same open/high/low/volume.
- **KBL:** NEPSE shows "Information about call 25th AGM of Kumari Bank Ltd. [KBL]", published 2025-12-14 10:18:27, approved 10:20:06. The competing 2025-12-12 date is the approved date of a separate book-close notice (published 2025-12-11), not the published date of the AGM call. Favoured price: 181.40 on 2025-12-15 (FinancialNotices CLOSE 181.40, open 178.8, high 182.9, low 178.3, volume 192,234; Merolagani LTP 181.40, same volume). Alternative, if disclosure 2025-12-12: 178.80 on 2025-12-14 (FinancialNotices CLOSE 178.80; Merolagani LTP 178.80). NEPSE also lists a KBL "No Dividend Declaration" for FY2081/82, published 2025-11-12.

**Batch 2, the five locator-only prices, plus NEPSE filter test.** All five prices are Merolagani LTP-labelled only; no Close-labelled figure was obtained for any of these dates, and FinancialNotices' history window runs only 2025-10-28 to 2026-10-07, so it cannot cross-check them.

- **GBIME FY2077/78:** disclosed 2021-11-19 (Fri); first trading day 2021-11-21 (Sun; row quantity 59,246 proves trading); LTP 376.70 (high 378, low 373, open 378).
- **GBIME FY2078/79, problem row:** disclosed 2022-11-15 (Tue); strict-definition first trading day 2022-11-16 (Wed, market open proven by a NICA row) but Merolagani has no GBIME row for 2022-11-16, and none through 2022-12-06; first day GBIME itself next traded was 2022-12-07, LTP 221.40 (high 240, low 220, open 240, quantity 143,676). Reason for the gap not verified at that stage; the December 7 figure must not be substituted unqualified as MPS_post. (Reason later verified as merger suspension, see Section 11.)
- **GBIME FY2079/80:** disclosed 2023-11-18 (Sat); 2023-11-19 no row for GBIME or NICA (market did not trade that Sunday; holiday name not verified); first trading day 2023-11-20 (Mon, quantity 76,289); LTP 207.00 (high 212, low 206, open 212).
- **NIMB FY2079/80:** disclosed 2024-02-29 (Thu); candidate 2024-03-03 (Sun) confirmed as a trading day (row quantity 73,472); LTP 160.50 (high 165.70, low 160, open 165).
- **NIMB FY2080/81:** disclosed 2025-02-04 (Tue); candidate 2025-02-05 (Wed) confirmed as a trading day (row quantity 71,186); LTP 213.00 (high 215.90, low 210.50, open 213).
- **NEPSE filter test:** NEPSE Today's Price with autocomplete-selected GBIME still returned nothing for 2020-01-06, 2021-11-21, and 2025-02-05 (page stayed on the Oct 26, 2026 list). At that stage it was reported that NEPSE could not be used as the price source via that filter. See Batch 3 correction below (the filter is flaky, not uniformly broken).

**Batch 3, NMB and GBIME FY2081/82:**

- **NMB:** NEPSE listing shows "30th Annual General Meeting Notice [NMB]", published 2025-12-16 10:22:31, approved 10:27:53, AGM 2026-01-08, AGM No. 30. Separate 2025-12-15 entry is a different book-close notice (book close 2025-12-24, cash 5%, bonus 5%); dividend declaration entry 2025-11-23 also shows 5% cash + 5% bonus. Price is NEPSE-primary: NEPSE Today's Price filtered to 2025-12-17 with autocomplete-selected NMB returned a single row: Close Price* 256.10, open 253.90, high 256.50, low 252.20, quantity 66,790, value 17,007,529.50, trades 225, LTP 256.10, previous close 252.10, average 254.64. Merolagani LTP 256.10 and FinancialNotices CLOSE 256.1 agree exactly. Correction recorded: NEPSE's filter did work for this single date even though its page header still read Oct 26, 2026. The filter is flaky, not uniformly broken. Book closure 2025-12-24 is after the price date, so the bonus adjustment does not affect it.
- **GBIME:** resolved in favour of 2025-10-16 on aggregator evidence plus NEPSE consistency, not NEPSE-primary content at that stage. ShareSansar announcement timestamped Oct 16, 2025 states the bank announced its 19th AGM (26 Kartik 2082) and published its FY2081/82 financial highlights. NEPSE shows a distinct 19th AGM notice published 2025-10-16 10:07:09, approved 10:07:57, AGM 2025-11-12, book close 2025-11-02, cash 8%. The two NEPSE entries published 2025-10-15 (19:30 and 19:36, both approved the morning of 2025-10-16) show AGM/book-close/dividend fields only; the Oct 15 published date must not be collapsed into Oct 16 just because approval came Oct 16 morning. Prices are LTP only: Merolagani 2025-10-19 LTP 240.00 (open 236, high 244.40, low 231.40, quantity 285,064); 2025-10-16 LTP 236.00 (open 236, high 237.50, low 232.50, quantity 212,927). NEPSE Close for GBIME was not verified (filter would not apply on five tabs); FinancialNotices reaches back only to 2025-10-28, covering neither date. Corporate action: 8% cash only, no bonus (NEPSE dividend declaration 2025-10-11 and AGM notice both show cash 8%, no bonus line).

### NEPSE attachment checks (opened and read in the browser viewer only, under Krishna's explicit approvals)

- **HBL 33rd AGM notice (published 2025-12-24):** 1-page scanned Nepali newspaper notice, meeting 2082 Poush 30 (2026-01-14). Contains no FY2081/82 statement or highlights table or figures; agenda item 2 only lists the auditor's report with balance sheet as of Asadh 2082 and profit-and-loss/cash-flow statements for discussion/approval. Conclusion: AGM notice only. 2025-12-24 is therefore not proven as the audited-statement disclosure date from this attachment.
- **KBL 25th AGM call (published 2025-12-14):** 2 pages (cover letter + scanned newspaper notice, meeting 2082 Poush 30, 11:00 a.m., Amrapali Banquet). Contains no FY2081/82 highlights or statement figures/tables; agenda item 2 only lists the FY2081/82 statements for approval; the notice says the annual-report booklet may be obtained from the website/company-secretary office. Booklet not included. Conclusion: AGM-call notice only.
- **NIMB dividend declaration (published 2025-12-22):** 1-page letter dated 2082/9/07. Declares no dividend for FY2081/82 in its own words: board meeting 629 approved the audited FY2081/82 statements for presentation to the 39th AGM and for NRB approval, and no proposal was made regarding cash or bonus distribution. Cash = none, bonus = none, confirmed from the document itself. Consistent with DPS 0.
- **NMB 30th AGM notice (published 2025-12-16):** 2 pages. Page 1 cover letter says the 30th AGM (2082 Poush 24, Tribhuvan Army Officers Club) notice and summary annual financial statement were published that day, 2082/09/01, in Nepal Samacharpatra. Page 2 is the scanned AGM notice. Financial tables: no, only a summary-statement heading with introductory lines at the very foot of page 2, no table or figures. Conclusion: intermediate. Disclosure on 2025-12-16 rests on the cover-letter assertion plus the NEPSE posting, not on tables inside the file. Book close 2025-12-24; dividend 5% cash + 5% bonus per NEPSE entry body (bonus text in the scan was not legibly readable, so cited from the entry body).
- **GBIME 19th AGM notice (published 2025-10-16):** 3 pages. Page 1 cover letter dated 2082/06/30 says the 19th AGM (2082 Kartik 26) public notice was published that day in Annapurna Post, book closure one day 2082 Kartik 16. Pages 2-3 do contain large summary financial-statement tables for FY2081/82 alongside the AGM notice, with a continuation page. Conclusion: yes. The one FY2081/82 attachment that itself carries the financial content, so 2025-10-16 is supported by the file itself. Dividend confirmed inside: agenda item 4 proposes 8% cash on paid-up capital (incl. tax), no bonus proposal seen; book close 2025-11-02, AGM 2025-11-12.
- **GBIME Oct 15 comparison file (19:30 entry):** 3 pages; contains no statement/highlights tables, only AGM/book-close information. The tables appear only in the Oct 16 document.
- **NIMB 39th AGM notice (published 2025-12-24):** two attachments, each 1 page in the viewer. Attachment 1 (AGM notice): single scanned page whose banner is the 39th AGM notice and summary annual financial statement of NIMB; left portion AGM notice text, right portion large multi-column financial tables, lower left a smaller indicators/highlights table (total assets, loans, deposits, net profit, capital adequacy, credit-to-deposit, customers, market shares, branches, ATMs). Individual figures not reliably legible at viewer zoom and not quoted. Conclusion: yes. The attachment itself contains FY2081/82 summary-statement and highlights tables, so NIMB joins GBIME as proven by file content for 2025-12-24. Attachment 2 (cover letter, dated 2082/09/08): does not state a summary statement was published in a newspaper and names no newspaper; it says the book-close notice will be published 2082/09/09 (= 2025-12-24), and states no cash dividend and no bonus share, confirming the dividend finding a second time. Book close from 2026-01-02 until the AGM is after the price date 2025-12-28, so no adjustment issue.

### Separate-disclosure searches (FY2081/82)

- **KBL:** a separate statement disclosure was found on aggregators, dated 2026-02-11, not Nov-Dec 2025. Merolagani id 64258, FY 081-082, tag Financial Statement, announcement date 2026/02/11 (2082/10/28); ShareSansar same item, Feb 11, 2026. NEPSE published timestamp not obtained. NEPSE security-name filter returned unrelated rows in this view and pagination has no direct page URL (415 pages at 20 entries/page; reaching Dec 2025/Feb 2026 pages by clicking about 60-70 pages was not completed). Do not treat Feb 11, 2026 as a verified NEPSE timestamp. The mirrored Merolagani attachment (viewed in browser; NEPSE attachment not opened) is a scanned multi-table annual statement: Statement of Financial Position, Statement of Cash Flows, Capital Adequacy Ratio, table for the year ended 32 Asadh 2082, Group and Bank columns for FY2081-82 and FY2080-81, incl. Profit for the year. No newspaper name/date readable from the portion viewed. KBL Nov-Dec 2025 window on Merolagani: only Nov 13, 2025 dividend information, Dec 12, 2025 book-closure notice, Dec 14, 2025 25th AGM notice, no statement entry. Next entries: Jan 26, 2026 AGM minutes, then Feb 11, 2026 statement. KBL website reports page lists the 25th annual report 2081/82 (English) and synopsis with no publication dates; its notices pages returned Not Found. Implication unresolved (needs Krishna's decision, not assumed): either Feb 11, 2026 is the statement disclosure, in which case the Dec 15, 2025 price (181.40) is before disclosure and fails section 07; or Feb 11 is the full annual-report filing after the Jan 14 AGM, and the pre-AGM summary disclosure was elsewhere (newspaper/booklet) and was not found on NEPSE/aggregators. The document's full-statement character leans toward the second reading, but that is not proven.
- **HBL:** no separate FY2081/82 statement/highlights disclosure found in the sources checked. Merolagani FY081-082 list around the AGM period shows only Dec 24, 2025 AGM notice and May 22, 2026 AGM minutes, plus Aug 12, 2025 provisional Q4 statement; filtering to "Annual Report" type returned no matches. ShareSansar search for HBL published-annual returned only an FY2077/78 item (Apr 12, 2022). HBL bank website unreachable (connection reset, not a bot check). This negative result is limited: not proof no NEPSE entry exists, because the bank-filtered NEPSE search could not be completed.
- **NMB:** no separate NEPSE disclosure carrying FY2081/82 statement/highlights tables was found, and no separate NEPSE entry for the Nepal Samacharpatra summary statement was found, within the sources/ranges searched. NEPSE filtered list for NMB, page 1 (2026-10-08 back to 2024-02-05): only three NMB entries in Nov-Dec 2025: Nov 23, 2025 dividend declaration, Dec 15, 2025 book-close information, Dec 16, 2025 30th AGM notice. Candidates opened: book-close letter Dec 15 (1 page, no tables; book close Dec 24, 2025, cash 5%, bonus 5%); dividend letter Nov 23 (1 page, 5% cash + 5% bonus, no tables); Aug 24, 2025 information entry (Malaysia representative office, no tables); Jan 27, 2026 AGM minute (cover + 11-page minute, sampled pages 4, 7, 11, narrative/attendance, no statement tables observed; sampled, not page-by-page audited). Aggregators/website (not NEPSE filings): Merolagani Dec 16, 2025 entry is the same AGM event; its Dec 28, 2025 entry reports only that NMB published its annual report, with no corresponding NEPSE entry dated Dec 28; Aug 12, 2025 entry is the provisional Q4 statement. ShareSansar Dec 16, 2025 entry states NMB announced its 30th AGM and published its annual financial statement for FY2081/82, but its detail page contains only that sentence, no attachment, no newspaper named. ShareSansar does list a separate prior-year entry on 2025-02-06 for the FY2080/81 annual statement; no equivalent separate FY2081/82 entry was found in the 50 entries examined (2026-10-17 to 2024-12-17). NMB website: AGM notice category lists only "30th AGM Notice" for FY2081/82; annual-report page lists the FY2081/82 annual reports (Nepali/English) as website publications, not NEPSE entries, files not opened. Limitation: NEPSE page 2 was not read, but by descending order it would contain entries before 2024-02-05 and therefore cannot contain a FY2081/82 disclosure.

### Final FY2081/82 disclosure standing after all live checks

- **GBIME, proven by file content** (2025-10-16); price 240.00 on 2025-10-19 is LTP-only, NEPSE Close not verified.
- **NIMB, proven by file content** (2025-12-24); price 193 on 2025-12-28, Close (FinancialNotices) agrees with LTP (Merolagani).
- **NMB, intermediate:** no separate disclosure; rests on cover-letter assertion of same-day newspaper publication (2025-12-16) + ShareSansar wording; price is NEPSE-Close confirmed (256.10, 2025-12-17).
- **HBL, AGM notice only;** no separate disclosure found in sources checked, NEPSE side incomplete.
- **KBL, AGM notice only in Dec 2025;** separate full statement on aggregators dated 2026-02-11 (NEPSE timestamp unverified), implication unresolved.

## 7. MPS_post merge into the panel

Implemented in the DPS pattern, on Krishna's approval: "Yes, merge GBIME and NIMB FY2081/82 into the panel as settled, and hold HBL, KBL, and NMB as pending."

- Source of record: `config/mps.json`, 2 settled entries (GBIME, NIMB FY2081-82) and 3 pending entries (HBL, KBL, NMB FY2081-82) carrying candidate fields only (candidate disclosure date, candidate first trading date, candidate price, candidate price label, and a note recording why the row is held).
- Merge module: `src/data_extract/mps_overrides.py` (`apply_mps`). Deliberate difference from DPS: a missing MPS entry is a status ("unavailable"), not an error, because MPS collection is incomplete by design. The module raises if a pending entry ever carries a real `mps_post_npr` / `disclosure_date` / `first_trading_date` field (preventing silent promotion of a candidate). Settled validation: disclosure date strictly before first trading date, price positive, price label Close or LTP.
- Script: `scripts/apply_mps.py` (idempotent). Also wired into `scripts/run_accounting_extract.py` after `apply_dps`. Documented pipeline order is now: run -> manual corrections -> dps -> mps. (`apply_manual_corrections.py` regenerates the panel from raw JSONs without DPS/MPS columns, so MPS must be re-added last; raw JSONs keep the `market` dict throughout.)
- Panel columns added: `mps_post_npr, mps_disclosure_date, mps_first_trading_date, mps_price_label, mps_status, mps_disclosure_source, mps_price_source, mps_note`. Full disclosure/price sources and corporate-action notes live in the raw JSON `market` dict and in `config/mps.json`.
- Settled entries as merged:
  - **GBIME FY2081-82:** disclosure 2025-10-16, first trading 2025-10-19, price 240.00, label LTP, security "GBIME (Global IME Bank Limited, ordinary share)", corporate action "8% cash only, no bonus; book close 2025-11-02, after the price date", note records LTP-only status and the Oct 15 alternative rejection.
  - **NIMB FY2081-82:** disclosure 2025-12-24, first trading 2025-12-28, price 193, label Close, security "NIMB (Nepal Investment Mega Bank Limited, ordinary share)", corporate action "No dividend (dividend declaration 2025-12-22 and cover letter both state no cash and no bonus); book close from 2026-01-02 until the AGM, after the price date".
  - Pending candidates recorded (never in panel price/date fields): HBL candidate 191.90 on 2025-12-28; KBL candidate 181.40 on 2025-12-15; NMB candidate 256.10 on 2025-12-17 (NEPSE Close).
- Verification after a fresh full pipeline run 2026-10-27: 30 rows, 0 failures, DPS 30/30, ROA 30/30, max identity diff 1 NPR, tests 6 passed. Accounting and DPS untouched. Panel result as re-read: MPS settled 2, pending 3, unavailable 25; pending rows have blank price/disclosure/trading/label in the panel.
- `output/audit/extraction_report.md` updated with a full MPS section.

Realized regression sample under the proposal rule: 2/30 (GBIME and NIMB FY2081-82 only), because EPS, DPS, BVPS, ROA are all 30/30, so a bank-year enters the sample exactly when its MPS_post is settled. Excluded: 3 pending (held, not overlooked) and 25 unavailable. No regression was run on n=2; the `analysis/` folder remains gated. Pooled OLS with four explanatory variables plus an intercept needs observations well above 6 just to be estimable.

## 8. Third-party fixed-date plan: what was pasted, and Muse's evaluation

Krishna pasted a long plan from another source (its own voice: "Send me the 30-row sheet and I'll build the price table. I can also draft the message to your supervisor."). Its substance:

- It tested online sources and reported: a public GitHub dataset (nepse-data) with one CSV per symbol, about 370 companies, history back to 1995, refreshed almost daily, running to 2026-10-26; all five banks present (GBIME from Sept 2012; KBL, NMB, HBL from 2011; NIMB from Feb 2023; pre-merger NIB filed under `NIB`, Mar 2011-Jan 2023).
- Accuracy claim: NABIL highest/lowest close and trade prices for Jul 2015-Jul 2019 match a ShareSansar article exactly (2,700 / 682 / 2,794 / 678), one stock only.
- Raw-not-adjusted claim: e.g. NABIL fell 26.9% on 2017-09-12, an ex-bonus-style drop.
- Holes it reported: KBL 64 trading rows in 2016 (vs about 230 normal); GBIME 123 rows in 2022 and 126 in 2019; NIB 88 rows in 2021 and 36 in 2022 (probably pre-merger wind-down, unverified by it). GBIME: no rows Nov 8-Dec 6, 2022, next row Dec 7 (close 221.4); the file lists only traded days, so it cannot show whether NEPSE's daily report carries a close for Nov 16.
- Fundamentals: advised against planning around ShareHub's API (needs an issued account, allow-listed server IP, licence; ratios endpoint returns only latest values).
- Precedent cited: one study with 209 bank-year observations across all listed commercial banks FY2013/14-2023/24 (Dahal, Gurung & Ghimire 2025, NepJOL); another with seven banks 2012/13-2018/19 (Saud, TU e-library). Sources it listed: github.com/Aabishkar2/nepse-data; sharehubnepal.com/data/nepse-data-documentation; nepjol.info/index.php/ijmss/article/view/75407; elibrary.tucl.edu.np/handle/123456789/10077; a ShareSansar NABIL overview (Jul 2019).
- Its plan: (1) get the supervisor's OK today for a fixed, pre-specified price date for all 30 bank-years, with disclosure-date pricing kept as a robustness subsample, a method change, not to be made silently; (2) freeze the rule before any regression, primary: last close on or before the last day of Ashadh, with a Poush-end price and the disclosure-date subsample reported as checks, never picking the primary after seeing results; weakness acknowledged (price precedes publication, tests association not market reaction); (3) build the price table (last trading day on or before each target date; flag rows where that day is more than 5 days early or falls in a gap; about 10 rows spot-checked on NEPSE/ShareSansar); (4) share-basis audit (flag ex-bonus-style drops near each price date); (5) analysis: descriptives, correlations with VIF, primary model Price ~ EPS + BVPS, extended + DPS + ROA, HC3 robust errors, bank fixed effects as a check, no clustered errors with only 6 clusters, log-price robustness; (6) write-up naming merger breaks and n about 30.
- Its pending-row stance: keep HBL and KBL out of the disclosure subsample; include NMB only if the newspaper notice can be cited; for GBIME, if the dataset's close equals the LTP, use the dataset and "the labeling question goes away."
- Its stated limits: it had not seen the 30-row sheet; "all 30 computable" depends on dates falling in covered periods; the dataset is a community scrape of NEPSE, not an official source; it did not search exhaustively for historical disclosure dates and found no systematic source; ShareHub's announcements feed exists but is licensed; at n about 30 treat the regression as exploratory.

Muse's evaluation given to Krishna 2026-10-27 (standing, not superseded):

- The core is right and is also the whole risk: under the proposal as written the sample is still 2; the larger sample exists only if the dependent variable changes to a fixed year-end price, which requires supervisor approval first and must not be changed silently.
- The plan helps on price availability, and Krishna does not need to send his sheet anywhere. Muse already has the panel in the workspace and can build the price versions there.
- Two claims corrected: (a) "labeling question goes away" is wrong. Equality of dataset close and LTP on a traded day does not turn a community scrape into a NEPSE Close Price, and the plan itself said the README does not state raw vs adjusted; the dataset is a locator with spot checks, not a replacement source. (b) "EPS and BVPS should sit on the same share base for most rows" must be audited row by row, not assumed (panel EPS is reported/often bonus-restated; BVPS uses year-end shares).
- Precedent studies show 30-200 is a normal sample size for the topic; they do not prove the supervisor will accept a rule swap.
- NMB nuance: citing "the newspaper notice" requires the actual Nepal Samacharpatra issue, not just the cover letter asserting publication.
- At evaluation time Muse had not yet verified the dataset itself (372 files, coverage dates, raw status, NABIL check were then the plan's claims, not verified facts). That gap was closed in the next step (Section 9).
- Krishna's response to the offered options was profane frustration and a directive to search, deep-research, and do the verification work rather than ask. That directive was followed: Sections 9-11 below are the verification work.

## 9. GitHub nepse-data dataset: verified first-hand 2026-10-27

Clone: `~/workspace/nepse-data-check` (public HTTPS clone, about 41 MB, `--depth 1`, cloned 2026-10-27). Key verified facts:

- **372 company CSVs** under `data/company-wise/`, named by symbol. README columns: `published_date, open, high, low, close, per_change, traded_quantity, traded_amount, status` (status is derived: 1/-1/0 from close vs open). README says data are collected and updated on an almost daily basis via GitHub Actions (5 runs/day Sun-Fri). Neither the README nor the code states whether prices are raw or adjusted.
- **Origin chain correction:** the scraper code (`src/allDataScrapper.py`, `src/dailyDataScrapper.py`, `src/constants/url.py`) pulls from **ShareSansar** (`sharesansar.com/company-price-history` and `sharesansar.com/today-share-price`), **not** directly from NEPSE. So the chain is NEPSE -> ShareSansar -> GitHub dataset; cite ShareSansar via the dataset, not NEPSE directly, unless a price is spot-checked on NEPSE itself.
- **Coverage verified:** GBIME 2,786 rows, first 2012-09-26, last 2026-10-26; HBL 3,265 rows, first 2011-04-18; KBL 3,338 rows, first 2011-03-20; NMB 3,180 rows, first 2011-03-29; NIMB 839 rows, first 2023-02-23, last 2026-10-26; NIB 2,344 rows, first 2011-03-24 (close 598.0), last 2023-01-10 (close 251.0). NIB -> NIMB continuity: NIB ends 2023-01-10, NIMB starts 2023-02-23 (first close 216.0). The Jan-Feb 2023 gap is the merger transition.
- **Duplicate dates exist** in the files: GBIME 10 duplicate dates (e.g. 2012-10-01 appears twice, identical), HBL 11, KBL 10, NIB 8, NMB 6, NABIL 10; NIMB 0. Any use must dedupe by date (candidate table dedupes, first row kept).
- **Raw, not adjusted, verified:** NABIL 2017-09-11 close 1630.0 (-0.24%) -> 2017-09-12 close 1191.0, per_change -26.93% (the plan's 26.9% claim verified).
- **NABIL spot check verified exactly:** Jul 2015-Jul 2019 max close 2700.0, min close 682.0, max high 2794.0, min low 678.0, the plan's four numbers.
- **Per-year row counts verified (plan's holes confirmed, plus more):** KBL 2016: 64; GBIME 2022: 123, 2019: 126, 2020: 171; NIB 2021: 88, 2022: 36, 2023: 8; HBL 2021: 88, 2022: 142, 2020: 184; NMB 2015: 31, 2019: 132, 2014: 174; most banks 2020: 184 (COVID). Normal years run about 225-245 rows.
- **Gaps longer than 30 days (2020 onward), verified from the files:**
  - GBIME: 2019-07-04 (295.0) -> 2020-01-20 (277.0), 200 days; 2020 COVID gaps 51 and 47 days; **2022-06-15 (251.4) -> 2022-12-07 (221.4), 175 days**; 2023-01-08 -> 2023-02-22, 45 days. This corrects both the plan and Muse's earlier description: the GBIME 2022 suspension starts in June 2022, not November (last five trades before resumption: 2022-06-09 266.0, 06-10 265.0, 06-13 265.0, 06-14 258.6, 06-15 251.4; first trades from Dec 7: 221.4, Dec 11 214.2, Dec 12 214.0).
  - HBL: 2020 COVID gaps 51 and 47 days; **2021-05-12 (487.0) -> 2022-06-06 (358.9), 390 days**. HBL 2021 months: Jan-Apr about 19-20 rows each, May 9, Jun-Dec 0. A year-long halt for a major bank is implausible as a market suspension on its own, and looks like a scrape gap until checked against aggregators (see Section 11, where the reason was found).
  - NIB: 2020 COVID gaps 51 and 47 days; **2021-05-12 (453.0) -> 2022-05-30 (367.7), 383 days** (same monthly pattern as HBL); 2022-06-10 (265.0) -> 2022-11-22 (267.0), 165 days. Note: Merolagani's table gives NIB 2021-05-13 at 460.00, one day and one price different from the dataset's last row; see Section 11 discrepancy note.
  - KBL: 2020 COVID gaps only (51 and 47 days); 2022-09-25 (186.0) -> 2022-11-27 (198.6), 63 days.
  - NMB: 2020 COVID gaps only (51 and 47 days).
  - Large-drop scan: no drops at or below -15% for GBIME/HBL/KBL/NIMB/NIB/NMB in 2020-2026 in the dataset.

## 10. Candidate fixed-date price table: built, NOT merged into the panel

Files: `data_analysis/data_extract/output/manual_review/mps_candidate_price_table.csv` (30 rows) + notes file `mps_candidate_price_table_README.md` in the same folder. Construction: fundamentals (EPS, DPS, BVPS, ROA) copied from `accounting_panel.csv`; Ashadh-end price = last dataset close on or before the Ashadh-end target date; Poush-end price = last dataset close on or before the Poush-end target; disclosure column shows the two settled panel rows and the three pending candidates, marked as such. Dataset symbol for NIMB pre-merger years (FY2076-77 to FY2078-79) is NIB; FY2079-80 onward is NIMB.

Target dates used (BS to AD conversions, to be confirmed against a Nepali calendar before thesis use): Ashadh-end: FY2076-77 2020-07-15, FY2077-78 2021-07-15, FY2078-79 2022-07-16, FY2079-80 2023-07-16, FY2080-81 2024-07-15, FY2081-82 2025-07-16. Poush-end: 14 January of 2020, 2021, 2022, 2023, 2024, 2025 for the six FYs respectively. A plus/minus 1 day target shift only changes a price if a trading day falls between.

### All 30 Ashadh-end prices (price date, close, gap days), as re-read from the candidate table

| Series | FY76/77 | FY77/78 | FY78/79 | FY79/80 | FY80/81 | FY81/82 |
|---|---|---|---|---|---|---|
| GBIME | 2020-07-15, 239.0, 0d | 2021-07-15, 441.0, 0d | 2022-06-15, 251.4, 31d | 2023-07-16, 186.0, 0d | 2024-07-15, 194.2, 0d | 2025-07-16, 259.57, 0d |
| HBL | 2020-07-15, 540.0, 0d | 2021-05-12, 487.0, 64d | 2022-07-15, 299.2, 1d | 2023-07-16, 212.8, 0d | 2024-07-15, 204.2, 0d | 2025-07-16, 237.3, 0d |
| KBL | 2020-07-15, 186.0, 0d | 2021-07-15, 371.0, 0d | 2022-07-15, 191.0, 1d | 2023-07-16, 165.0, 0d | 2024-07-15, 153.7, 0d | 2025-07-16, 219.77, 0d |
| NIMB | 2020-07-15, 431.0, 0d | 2021-05-12, 453.0, 64d | 2022-06-10, 265.0, 36d | 2023-07-16, 173.8, 0d | 2024-07-15, 175.1, 0d | 2025-07-16, 231.02, 0d |
| NMB | 2020-07-15, 397.0, 0d | 2021-07-15, 440.0, 0d | 2022-07-15, 261.0, 1d | 2023-07-16, 226.0, 0d | 2024-07-15, 218.0, 0d | 2025-07-16, 269.72, 0d |

Clean Ashadh sample under a 5-day freshness rule: 26/30. Excluded: GBIME FY2078-79 (31d, merger suspension), HBL FY2077-78 (64d, dataset gap, reason now known, Section 11), NIMB FY2077-78 (64d), NIMB FY2078-79 (36d).

Poush-end prices of note: GBIME FY2076-77 Poush target Jan 14, 2020 falls in the 200-day dataset gap. Last trade 2019-07-04 295.0, 194 days early, not usable from the dataset. GBIME FY2079-80 Poush 2023-01-08 210.4 (6d early, merger-completion gap). HBL FY2078-79 Poush is 2021-05-12 487.0 (247 days early, dataset gap). NIMB/NIB FY2078-79 Poush likewise 2021-05-12 453.0 (247 days early). KBL FY2079-80 Poush 2022-12-29 190.0 (16d early). NIMB FY2079-80 Poush is unavailable in the NIMB file (first NIMB row 2023-02-23) and must not be filled with the pre-merger NIB price (swap 100:90). NIB's last trade was 2023-01-10 at 251.0. Poush blank count in the candidate table as re-read: 1 row (NIMB FY2079-80).

Status communicated to Krishna: this table is preparation only; using Ashadh-end or Poush-end as the primary variable still changes the proposal's definition and still needs supervisor approval before it goes near a regression; nothing from it has touched the panel, which still stands at 2 settled MPS_post rows.

### Share-basis scan (partial audit, 2026-10-27)

File: `output/manual_review/mps_share_basis_scan.csv` (30 rows), built from the candidate table; method note appended to `mps_candidate_price_table_README.md`. Method: for each candidate price, record price-day and next-day percentage change and any drop at or below -9% in the next 20 trading days. Caveat stated in the notes: trading-day windows mislead inside gaps. The -9.99% drops in June 2022 for HBL/NIMB and the -9.29% GBIME drop on 2022-12-07 are resumption drops after long suspensions, not clean ex-bonus drops the day after a price date; the Aug 6, 2024 -9% drops for HBL/NIMB look market-wide, not bank-specific. No clean ex-bonus-style drop was found immediately after a candidate price date in calendar terms. This scan does not replace checking each bonus ex-date against each price date from bonus announcements. That announcement check is still open, except for one verified input below.

Flagged rows from the Ashadh to Poush comparison (bonus at or above 10% and price fell more than 5%): GBIME FY2077-78 (bonus 10.0%, 441.0 -> 339.0, -23.1%); NIMB FY2076-77 (bonus 13.0%, 431.0 -> 405.0, -6.0%); NMB FY2076-77 (bonus 13.0%, 397.0 -> 359.0, -9.6%). Other notable rows: HBL FY2078-79 Poush figure (487.0) is the stale gap price (+62.8% apparent change is a gap artefact, not a real move); GBIME FY2081-82 bonus 0.0% yet Ashadh -> Poush -14.5% (market move, not bonus); KBL FY2077-78 bonus 6.0%, -23.5% (market/merger-period move, below the 10% bonus flag threshold).

Verified since the scan: GBIME FY2077/78 book close 29 Nov 2021 (Merolagani announcement id 40885: book close 2021/11/29, 2078/08/13, cash 3.5%, bonus 10%, AGM 2021-12-13). Note: book close is not itself the ex-date; the ex-date still needs the settlement rule applied. NMB FY2076/77 book close 31 Dec 2020 (as claimed by the third-party critique, no source given) was NOT verified in this pass. NIMB FY2076/77 book close was NOT verified in this pass (the critique itself admits it did not surface it).

## 11. Gap investigations: what was checked, what was found, what was corrected

### HBL and NIB, May 2021 to June 2022

Browser checks (read-only, no sign-in/payment/download/CAPTCHA) on Merolagani and ShareSansar price history, plus Krishna's own dataset check (verified against the local dataset clone, all symbols counted):

- Merolagani: HBL no rows on 2021-07-15, 2021-10-15, 2021-12-15, 2022-01-14, 2022-03-15, 2022-05-15. Boundary rows match the dataset exactly: 2021-05-12 LTP 487.00 and 2022-06-06 LTP 358.90. NIB no rows on 2021-07-15 and 2022-01-14; table jumps from 2021-05-13 LTP 460.00 directly to 2022-05-30 LTP 367.70.
- ShareSansar: HBL no rows on 2021-07-15, 2022-01-14, 2022-03-15 (3,273 total entries, control 2026-10-26 Ltp 202.00 returns a row); NIB no rows on 2021-07-15, 2022-01-14, 2022-03-15 (2,338 total entries). Correction to earlier wording: the dataset IS a ShareSansar scrape, so this is two aggregator sources (Merolagani and ShareSansar), not three independent ones. The gap is not unique to the dataset, but that alone does not prove a real suspension.
- Krishna's dataset check, verified: 2021-07-15: 177 symbols traded, KBL/NMB/GBIME present, HBL and NIB absent (stock-specific absence). 2022-03-15: 190 symbols traded, same pattern. 2022-01-14: 0 symbols traded, market-wide closure, NOT an HBL/NIB gap date. Remove 2022-01-14 from the gap evidence list; the Merolagani/ShareSansar "no row" on that date is expected (it was a Friday, weekend under the then Sunday-Thursday trading week).
- Announcement titles reviewed at that stage gave no reason. Relevant titles only: HBL 2022-01-03 adjusted price 398.75 for 21.38% bonus on a previous close of 484.00 (484 x 100/121.38 = 398.75, exact); HBL 2022-06-06 "Transactions Release Except Basic Shareholders"; NIB 2021-11-22 adjusted price 408.49 for 12.611% bonus on a previous close of 460.00 (exact); NIB 2022-02-15 listing of those bonus shares; NIB 2022-05-30 "Transaction Release" on the resumption date. The NIB Transaction Release detail (2022-05-30) was viewed: it concerns release of securities trading except for basic shareholders effective 2079/02/16 and states no merger or other reason for the preceding halt in its own text. HBL's 2022-06-06 Transactions Release detail was NOT opened (optional).
- **Reason now verified from news sources (third-party critique checked against live search, 2026-10-27):** HBL and NIB signed a merger MoU/agreement on 13 May 2021; NEPSE suspended trading of both from 13 May 2021; HBL shareholders rejected the proposal at the 4 Jan 2022 AGM; NIB trading resumed 30 May 2022 and HBL trading resumed 6 Jun 2022, in both cases to the general public except basic/core shareholders. Sources: The Himalayan Times, 14 Jan 2022, "HBL-NIBL merger chapter closes as Himalayan's shareholders reject proposal" (https://thehimalayantimes.com/business/hbl-nibl-merger-chapter-closes-as-himalayans-shareholders-reject-proposal); Khabarhub, Jun 2022, "NEPSE resumes stock trading of Himalayan Bank" (https://english.khabarhub.com/2022/06/256136/); ShareSansar, 30 May 2022, "Trading of Nepal Investment Bank Resumes After 12 Months To General Public But Restricted To Basic Shareholders" (https://www.sharesansar.com/newsdetail/trading-of-nepal-investment-bank-resumes-after-12-months-to-general-public-but-restricted-to-basic-shareholders-of-the-company-2022-05-30). This supersedes the earlier "reason unresolved" wording for this gap. The earlier wording was scoped to announcement titles reviewed, not to all sources, and that scope is recorded here so the correction is transparent.
- **Minor discrepancy noted, not hidden:** news reports give HBL last price 484 and NIB last price 460 as of 13 May 2021, while the dataset's last rows are HBL 12 May 2021 at 487.00 and NIB 12 May 2021 at 453.00, and Merolagani gives NIB 13 May 2021 at 460.00. The suspension date and reason are consistent; the one-day/one-price difference between dataset and news/Merolagani is not resolved here.

### GBIME, November 2022, and the GBIME FY2078/79 disclosure row

- Dataset and Merolagani context: no GBIME rows from 2022-06-15 to 2022-12-06, next row 2022-12-07 close 221.4. Krishna's dataset check, verified: 2022-11-16: 199 symbols traded, HBL/NMB/NABIL present, GBIME and KBL absent. Market was open, GBIME had no trade row that day in the dataset.
- NEPSE daily report for 2022-11-16: NOT VERIFIED from NEPSE. NEPSE Today's Price filter did not apply the 2022-11-16 date (table stayed on Oct 26, 2026); calendar-picker clicks on the 2022 cell did not change the dialog in four attempts; Downloads pages 1-2 contain general documents only, no daily market report for that date identified; Floor Sheet shows current-day contracts only and cannot select 2022-11-16. So NEPSE shows no GBIME close, no suspended status, and no omission finding for that date in that check.
- **Suspension reason now verified in substance from news sources:** GBIME and Bank of Kathmandu signed a merger MoU on 16 Jun 2022 (swap 1:1) and trading was suspended; trading resumed 7 Dec 2022 except basic shareholders. Sources: Corporate Khabar, 16 Jun 2022, "Merger agreement of Global IME Bank and Bank of Kathmandu" (https://english.corporatekhabar.com/merger-agreement-of-global-ime-bank-and-bank-of-kathmandu/); ShareSansar, 6 Dec 2022, "Share Trading of Global IME Bank and Bank of Kathmandu Released on NEPSE" (https://www.sharesansar.com/newsdetail/share-trading-of-global-ime-bank-and-bank-of-kathmandu-released-on-nepse-2022-12-06). This is a news-source finding, NOT a NEPSE daily-report record. The NEPSE filter check itself still failed, as stated. One ShareSansar item says halted "from 15 Oct 2022", which does not match the dataset (no GBIME rows Jun-Dec); the June MoU suspension is the one consistent with the dataset.
- Consequence for the disclosure subsample: GBIME FY2078/79 (disclosed 2022-11-15, strict first trading day 2022-11-16) is dropped to unavailable in the robustness subsample, per Krishna's decision. November 16 was a market trading day, but GBIME itself was suspended, so it has no price that day, and December 7 would be a deviation (first day the stock itself traded), not the strict rule. It does not touch the primary (fixed-date) sample, where GBIME FY2078/79 is already excluded for 31-day staleness.

### Third-party critique: verdict after verification (2026-10-27)

A second pasted critique claimed several "not found" statements were false or overstated. Each claim was checked against live sources before accepting it:

1. **HBL/NIB halt reason: VERIFIED, critique correct in substance.** See above. Muse's earlier wording was scoped to titles reviewed; the critique dropped that scope, but the reason itself is now documented.
2. **GBIME Nov 16, 2022 close: VERIFIED in substance, with a correction to the critique.** Suspension from the June 2022 merger fits the dataset; no close is expected. It is still not a NEPSE daily-report record.
3. **NMB Nepal Samacharpatra Mangsir 26 notice: NOT VERIFIED, critique overstated.** A search found no such notice, and Mangsir 26, 2082 is about 12 Dec 2025 (Mangsir 1 = 17 Nov 2025), not 16 Dec 2025 (Poush 1). A Mangsir 26 notice, even if it existed, would not prove the 16 Dec summary-statement publication. The cover-letter-only status for NMB stands.
4. **KBL Feb 11, 2026 NEPSE timestamp: critique AGREES with Muse.** No direct NEPSE filing found.
5. **Bonus book-close dates: PARTLY VERIFIED.** GBIME FY2077/78 book close 29 Nov 2021 verified (Section 10). NMB FY2076/77 book close 31 Dec 2020 (unsourced in the critique) not verified in this pass. NIMB FY2076/77 book close not verified (critique itself admits it did not surface it). Book close is not the ex-date; the settlement rule is still needed.

## 12. Exploratory analysis on candidate Ashadh-end prices: exploratory only

Computed with plain Python + numpy OLS (HC3 robust standard errors) on the candidate table. Exploratory only; the fixed-date method change still needs supervisor approval; these numbers must never be presented as thesis results without that caveat. Full output in `output/manual_review/mps_exploratory_analysis.txt`, notes in `output/manual_review/mps_exploratory_analysis_README.md`. The `analysis/` folder remains gated and unused.

- Ashadh clean sample: 26/30 (excluded for gap more than 5 days: GBIME FY2078-79 31d, HBL FY2077-78 64d, NIMB FY2077-78 64d, NIMB FY2078-79 36d).
- Descriptives (Ashadh clean sample, n=26): Price mean 266.25, sd 104.15, min 153.70, max 540.00. EPS mean 13.54, sd 6.48, min 0.02, max 27.60. BVPS mean 159.26, sd 17.29, min 132.71, max 190.70. DPS mean 3.16, sd 3.80, min 0.00, max 12.50. ROA mean 0.95, sd 0.46, min 0.00, max 1.79.
- Pearson correlations with Price: EPS 0.530, BVPS 0.242, DPS 0.286, ROA 0.557. Inter-correlations: EPS-ROA 0.974 (near-collinear), EPS-DPS 0.572, DPS-ROA 0.557, EPS-BVPS 0.344, BVPS-DPS 0.094, BVPS-ROA 0.225.
- OLS Price ~ EPS + BVPS (n=26): R2 0.285, adj R2 0.223; const 90.999 (HC3 se 192.775, t 0.47); EPS 8.140 (se 3.576, t 2.28); BVPS 0.409 (se 1.252, t 0.33).
- OLS Price ~ EPS + BVPS + DPS + ROA (n=26): R2 0.348, adj R2 0.224; const -59.940 (se 207.304, t -0.29); EPS -13.537 (se 19.485, t -0.69); BVPS 1.411 (se 1.402, t 1.01); DPS 0.280 (se 6.697, t 0.04); ROA 299.600 (se 240.804, t 1.24). The EPS sign flip and inflated errors are the EPS-ROA collinearity showing up.
- Log-price OLS (Price ~ EPS + BVPS on log price): R2 0.286, adj R2 0.224; const 4.900 (se 0.615, t 7.96); EPS 0.027 (se 0.011, t 2.41); BVPS 0.002 (se 0.004, t 0.39).
- VIF (extended model): EPS 30.87, ROA 27.52, BVPS 1.60, DPS 1.52. EPS and ROA are effectively the same signal in this sample (expected: ROA is approximately EPS/BVPS mechanically); the extended model cannot separate them at n=26.
- Consequence for any amended model: the full four-variable model must be reported with VIFs, but its individual EPS and ROA coefficients must not be presented as separable effects. The defensible primary reading is EPS plus BVPS, with ROA reported separately, and DPS reported with its timing caveat (see Section 14).

## 13. Source register and citations: the master file

On Krishna's instruction ("for every data that we collected, are you sure that you are making or keeping the record of the source, because we need to do the citations later, and create that file"), a master source register was built and committed:

- Files: `data_analysis/data_extract/output/audit/source_register.csv` (30 rows, one per bank-year) + `source_register.md` (citation guide).
- Builder (reproducible, not hand-typed): `data_analysis/data_extract/scripts/build_source_register.py`, reading the panel, raw JSONs, `config/dps.json`, `config/mps.json`, and the candidate table.
- Each row traces: annual report file and path, report SHA-256, SOFP and SOPL PDF pages, accounting method, manual-correction source, visual-read flag, DPS source file, DPS SHA-256, DPS PDF and printed pages, DPS method, DPS quote location (`config/dps.json` entry), MPS status, MPS disclosure date or CANDIDATE ONLY marker, MPS first trading date, MPS price or CANDIDATE ONLY marker, MPS price label, MPS disclosure source, MPS price source, candidate dataset symbol and file, candidate Ashadh and Poush price dates, closes, and gap days, and provenance gaps.
- Verification of the register as built: 30 rows, 0 blank report SHA-256, 0 blank DPS pages, visual rows correctly flagged (HBL FY2076-77, KBL FY2076-77). Pending MPS rows are marked CANDIDATE ONLY inside the register itself, so they cannot be cited as settled by mistake.
- Bibliography entries in the register guide: annual reports by bank and fiscal year, file as named, SHA-256 as recorded (NMB FY2079-80: cite the Nepali edition, because the English file is a dead S3 link); NEPSE, nepalstock.com.np, accessed 2026-10-27; Merolagani, eng.merolagani.com CompanyDetail pages, accessed 2026-10-27, price column labelled LTP; FinancialNotices, financialnotices.com, accessed 2026-10-27, price column labelled Close; ShareSansar, sharesansar.com/company/<symbol>, accessed 2026-10-27, price column labelled Ltp; dataset, Aabishkar2 nepse-data, github.com/Aabishkar2/nepse-data, cloned 2026-10-27, raw not bonus-adjusted, duplicate dates deduped, cite as ShareSansar data via that dataset, never as a NEPSE record.
- Honest gaps recorded in the register guide: accounting pages are statement-level, not per-cell; market source URLs are not saved for every NEPSE attachment (settled rows are retrievable by listing title + published timestamp, as recorded in `mps_verification.md`, since a direct attachment URL is not saved for every entry); candidate prices are dataset rows, not NEPSE or Merolagani rows; gap reasons that were unresolved at register build time are recorded as unresolved, never as a cited cause (note: the HBL/NIB and GBIME suspension reasons verified later, in Section 11, post-date the committed register and need a follow-up commit to be reflected in it; the working notes in `mps_candidate_price_table_README.md` already carry those corrections).
- Git status of the register: committed locally as e277983, "Add master source register for thesis citations (30 bank-years)", 2 files, 108 insertions, branch main 1 commit ahead of origin/main, NOT pushed (Krishna chose commit only, not commit-and-push). Local repo author identity was set for that commit to Krishna Subedi / krishnasubedi219@gmail.com because git had no identity configured on this machine; Krishna to correct if a different git email is wanted. The builder script itself was not included in that commit (only the two register files as approved).

## 14. The blocker, formally

Original model: MPS_post(i,t) = b0 + b1*EPS + b2*DPS + b3*BVPS + b4*ROA + e. Parameters k = 5 (intercept + 4 slopes).

Realized valid left-hand-side sample under the proposal rule: n = 2 (GBIME FY2081-82, NIMB FY2081-82).

Degrees of freedom: df = n - k = 2 - 5 = -3. OLS cannot estimate five parameters from two observations. Reduced model MPS_post = b0 + b1*EPS + b2*BVPS + e has k = 3, df = 2 - 3 = -1, also impossible. This is not weak evidence. It is impossible estimation.

Even the two settled rows carry a final check: the definition requires NEPSE closing price, not merely last traded price from a secondary source. GBIME's price is labelled LTP (240.00, Merolagani, NEPSE Close not verified). If 240.00 cannot be verified as the official NEPSE closing price for 2025-10-19, GBIME FY2081/82 is not usable as MPS_post, and the realized sample falls to n = 1. For MPS_post, an observation is usable only if all three are proven: (1) official or otherwise acceptable NEPSE disclosure date, (2) first NEPSE trading day strictly after that disclosure date, (3) official NEPSE closing price for that first trading day. If any one is missing or unverified, the observation is not usable as MPS_post.

## 15. Supervisory guidance received in chat on 2026-10-27, and Muse's position on it

Two long guidance messages in a supervisor's voice were provided by Krishna in chat on 2026-10-27. The first was saved, at Krishna's request, to `docs/thesis_supervisor/supervisory-decision-mps-ye-amendment-2026-10-27.md` (directory name corrected from the typed "thesis_supervior" to "thesis_supervisor"; file is untracked in git, not committed). The second, blunter message was not separately saved; its content is summarised here. Both messages state, in their own text, that their author had not independently verified live NEPSE/Merolagani/SEBON records in that chat and that external facts in them are conditional on the data status provided by Muse. **Until Krishna confirms whether these are his university supervisor's actual rulings or drafted guidance, they must NOT be cited in the thesis as official supervisor letters.** The summary below is of the guidance content, not a claim about its official status.

Rulings in the guidance, in substance:

- Original MPS_post regression is not estimable (n = 2, k = 5, df = -3; reduced model df = -1). Agreed: arithmetic, see Section 14.
- Ashadh-end price may NOT be labelled, treated, or interpreted as MPS_post under the current proposal. Agreed: different variable, different timing, different question.
- Ashadh-end price MAY be used only as a formally amended, differently named dependent variable, MPS_YE (or P_YE): NEPSE official closing price of the ordinary share on the last NEPSE trading day on or before the official fiscal year-end date, unadjusted, accepted only if the price date is no more than five calendar days before the fiscal year-end date; if no such price exists, the observation is missing. Agreed as a design, with the qualification below.
- Amended model: MPS_YE(i,t) = b0 + b1*EPS + b2*DPS + b3*BVPS + b4*ROA + u. Sample n = 26 (clean subset only), k = 5, df = 21, estimable but small. Agreed, with qualifications below.
- Interpretation must be association/value relevance at fiscal year-end, never post-disclosure market reaction, never "investors reacted to EPS/DPS/BVPS/ROA". Agreed.
- DPS timing warning: board-proposed DPS is usually proposed after fiscal year-end, together with or after audited statements, while MPS_YE is observed at fiscal year-end, so the market price at year-end may not yet know the officially proposed dividend. DPS significance must be described as anticipated dividend policy or expectations, not as reaction to a known proposal. Robustness model without DPS is recommended: MPS_YE = b0 + b1*EPS + b2*BVPS + b3*ROA + u. Agreed, and this robustness model is necessary, not optional.
- Exclude the four stale observations from the main MPS_YE sample and report them as excluded for staleness: GBIME FY2078/79 (31d), HBL FY2077/78 (64d), NIMB FY2077/78 (64d), NIMB FY2078/79 (36d). If a clean observation later fails NEPSE closing-price verification, remove it and report the reduced sample. Agreed.
- Do not mix MPS_post and MPS_YE, pending candidates, or locator-only prices in one regression. Main analysis MPS_YE n = 26; the two verified MPS_post observations may appear only descriptively in an appendix; a data-availability audit explains why MPS_post was not feasible. Agreed.
- Estimation guidance: pooled OLS baseline, HC3 robust standard errors because the sample is small, do not cluster by bank with only five banks unless a small-cluster correction or bootstrap is used (ordinary cluster-robust variance with five clusters is unreliable). Diagnostics: VIF, residual normality plot, residuals vs fitted, Cook's distance/leverage, correlation matrix, robustness excluding DPS, robustness with bank dummies if degrees of freedom remain acceptable. Bank dummies: 5 banks = 4 dummies, total parameters 9, df = 26 - 9 = 17, still estimable but weaker. Two-way fixed effects: 4 bank + 5 year dummies, total parameters 14, df = 26 - 14 = 12, possible but may overfit at n = 26. Recommendation in the guidance: baseline pooled OLS, robustness bank dummies only if justified, do not make two-way fixed effects the main model unless the supervisor specifically requires it. Agreed on the arithmetic and the caution.
- If the amendment is refused by the university, the honest result is that the proposed regression could not be performed due to insufficient verified post-disclosure price data, or the thesis must be rescoped (change sample, period, question, dependent variable, or convert to a descriptive/data-availability study, or change topic). Agreed: a regression on n = 2 must never be submitted.
- Exact thesis wording supplied in the guidance for the blocker statement, the amendment statement, and the limitation paragraph is reproduced in the saved supervisory file (Section: Exact thesis wording you can use). Those wordings are accurate as statements of the situation and may be used, subject to the origin caveat above.

Muse's qualifications to the guidance (stated to Krishna in chat, recorded here so they are not lost):

1. n = 26 is dataset n = 26, not yet NEPSE-verified n = 26. The guidance itself makes approval conditional on each price being a NEPSE official closing price within five days. The 26 prices are dataset closes (ShareSansar scrape), not verified NEPSE closes row by row. If verification drops rows, n drops and the sample must be restated. Until then, every MPS_YE price must keep its dataset label.
2. The full four-variable MPS_YE model will not behave cleanly: EPS-ROA correlation 0.974, VIF EPS 30.87, ROA 27.52 (Section 12). The guidance recommends VIF diagnostics, which is good, but still presents the four-variable model as the main model. The defensible primary reading is EPS plus BVPS, with ROA reported separately, because ROA is mechanically close to EPS/BVPS in this sample. Individual EPS and ROA coefficients from the joint model must not be presented as separable effects.
3. The strict NEPSE-close standard applied to GBIME's MPS_post price must also apply to MPS_YE prices. A loose standard for MPS_YE and a strict standard for MPS_post would be inconsistent.

## 16. What remains, in order

1. **Krishna, confirm the origin of the supervisory guidance.** Is the saved decision his university supervisor's actual ruling, or drafted guidance to take to the supervisor? That decides whether it can be cited as approval and whether the proposal amendment can proceed on its authority. Until confirmed, treat Track B as guidance, not as granted approval.
2. **Krishna, approve or amend the supervisor message, then send it.** The draft in `output/manual_review/supervisor_message_draft.md` states the proposal rule, the 2 verified rows, the held rows, the dataset verification including gaps, the proposed Ashadh-end primary rule with Poush-end and disclosure subsample as checks, and the limit that an Ashadh price tests association, not reaction. It is written without em dashes and without semicolons. It has not been sent anywhere. If the guidance in Section 15 is already the supervisor's ruling, this step becomes: confirm the amendment in writing with the supervisor's office instead of asking from scratch. Do not assume which one applies; Krishna to confirm.
3. **Verify each of the 26 clean MPS_YE prices as a NEPSE official closing price, or state the verification status row by row.** Until that is done, the amended sample is n = 26 dataset prices, not n = 26 NEPSE closes. This is the largest remaining verification job for Track B. GBIME FY2081/82's LTP check (is 240.00 the NEPSE close for 2025-10-19?) is the same kind of check, for the MPS_post appendix, and it decides whether MPS_post is n = 2 or n = 1 descriptively.
4. **Finish the share-basis ex-date check.** GBIME FY2077/78 book close 29 Nov 2021 is verified; derive its ex-date under the applicable settlement rule and compare it with the Ashadh and Poush price dates. Verify NMB FY2076/77 and NIMB FY2076/77 book closes from a sourced record (the 31 Dec 2020 date for NMB in the critique is unsourced and is not accepted here). Record per row whether the price and the panel EPS/BVPS are on a comparable share basis, marking incomparable rows per section 07 rather than adjusting them.
5. **Update the source register with the Section 11 corrections and commit the follow-up.** The committed register (e277983) still records the HBL/NIB halt reason and the GBIME November 2022 status as unresolved; the working notes already carry the verified merger reasons. A follow-up commit should also include the builder script (`scripts/build_source_register.py`) and the supervisory decision file (`docs/thesis_supervisor/supervisory-decision-mps-ye-amendment-2026-10-27.md`), both currently untracked, if Krishna approves those commits. Separately, decide whether to push the register commit to GitHub; Krishna previously chose commit only, so nothing has been pushed.
6. **Only after amendment approval and price verification: run the thesis analysis for MPS_YE.** Baseline pooled OLS with HC3, descriptives, correlation matrix, VIF, residual diagnostics, robustness without DPS, robustness with bank dummies only if justified. Report the four stale exclusions, the EPS-ROA collinearity, the DPS timing limitation, and the merger breaks in the write-up. Keep the `analysis/` folder gated until that point; do not present the exploratory numbers in Section 12 as thesis results.
7. **Do not do:** send the 30-row sheet to any third party (the panel is already in the workspace and the price tables are already built here); chase further gap reasons (the two material gaps now have reasons, and the plan does not need the rest resolved); promote any pending or locator MPS_post row into data; mix MPS_post and MPS_YE in one regression; label any Ashadh-end price as MPS_post; impute any missing price or disclosure date.

## Appendix: file index for this report

- Thesis proposal: `~/workspace/verbose-chainsaw/src/proposal/sections/07_methodology/07_methodology.tex`, `.../03_objectives/03_objectives.tex`, `.../front/titlepage.tex`
- Reports and checklist: `~/workspace/verbose-chainsaw/data/reports/`, `~/workspace/verbose-chainsaw/data/README.md`
- Extraction root: `~/workspace/verbose-chainsaw/data_analysis/data_extract/` (QUALITY.md, README.md, config/, src/, tests/, scripts/, output/)
- Panel: `.../data_extract/output/tidy/accounting_panel.csv`
- Raw JSONs: `.../data_extract/output/raw/`
- Audit report: `.../data_extract/output/audit/extraction_report.md`
- DPS source of record: `.../data_extract/config/dps.json`; builder: `.../data_extract/scripts/build_dps_config.py`
- MPS source of record: `.../data_extract/config/mps.json`; merge: `.../data_extract/src/data_extract/mps_overrides.py`, `.../data_extract/scripts/apply_mps.py`
- Visual overrides: `.../data_extract/config/visual_overrides.json`; evidence: `.../data_extract/output/manual_review/visual/`
- MPS verification trail: `.../data_extract/output/manual_review/mps_verification.md`
- Candidate fixed-date work: `.../data_extract/output/manual_review/mps_candidate_price_table.csv`, `.../mps_candidate_price_table_README.md`, `.../mps_share_basis_scan.csv`
- Exploratory analysis: `.../data_extract/output/manual_review/mps_exploratory_analysis.txt`, `.../mps_exploratory_analysis_README.md`
- Source register: `.../data_extract/output/audit/source_register.csv`, `.../data_extract/output/audit/source_register.md`; builder: `.../data_extract/scripts/build_source_register.py`
- Supervisor decision file (origin unconfirmed, see Section 15): `~/workspace/verbose-chainsaw/docs/thesis_supervisor/supervisory-decision-mps-ye-amendment-2026-10-27.md`
- Supervisor message draft (not sent): `.../data_extract/output/manual_review/supervisor_message_draft.md`
- MPS_post deep research: `~/workspace/research_notes/mps-post-nepse-disclosure-prices-20261027-0148/report.md` and its `notes/` files; presentation artifact slug `mps-post-research`
- GitHub dataset clone (verified copy): `~/workspace/nepse-data-check` (data under `data/company-wise/<SYMBOL>.csv`; scraper under `src/`)
- This report: `~/workspace/verbose-chainsaw/data_analysis/data_extract/output/audit/full_report_data_and_research_2026-10-27.md`

Git status at report time: only the source register is committed (e277983, 1 commit ahead of origin/main, not pushed). Untracked or modified, not committed: `data/README.md` (modified), `data/reports/GBIME/`, `data/reports/HBL/`, `data/reports/KBL/`, `data/reports/NIMB/`, the whole `data_analysis/` tree except the committed register files, and `docs/thesis_supervisor/`. No commit or push of those items has been made, and none will be made without Krishna's approval for each step.
