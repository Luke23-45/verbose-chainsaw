# Extraction report — accounting panel (SOFP + SOPL)

Date: 2026-10-27. Panel: `data_extract/output/tidy/accounting_panel.csv`
(30 rows). Raw per-PDF JSON: `data_extract/output/raw/<SERIES>_<FY>.json`.
Parser: `src/data_extract/statement_parser.py` (word-coordinate rows,
spread-page split, note-number anchors 4.1-4.41, both Group and Bank
columns extracted, Bank column primary for the panel).

## What is complete
- Total assets, total liabilities, total equity attributable,
  share capital, profit after tax, profit attributable, reported
  EPS, reported NAV per share: **30/30 bank-years present**.
- Recomputed BVPS (equity attributable / shares outstanding,
  shares = share capital / 100): **30/30**.
- Recomputed ROA (PAT / average total assets): **30/30**.
  The last two gaps were closed 2026-10-27 by visual extraction
  (see below): HBL FY2076-77 ROA 1.7899%, KBL FY2076-77 ROA
  0.8958%.
- DPS (cash dividend per share proposed for each FY, from board
  reports / AGM notices): **30/30** — 18 positive, 12 documented
  nil. See the DPS section below.

## Identity checks (G3) — pass
For every bank-year, total assets − (total liabilities + total
equity) = 0, except NMB FY2080-81, FY2081-82 and NMB FY2079-80,
and KBL FY2076-77 on its own-report values, where the difference
is **1 NPR** (printed rounding). No bank-year fails identity by
more than 1 NPR after the manual corrections below.

## BVPS vs printed NAV (G4) — explained, not hidden
- Most bank-years agree to within 0.01 NPR.
- NIMB: printed NAV is in whole rupees, so differences up to
  0.40 NPR are rounding to the nearest rupee (e.g. FY2081-82:
  recomputed 190.40, printed 190).
- HBL FY2076-77: recomputed 187.67, printed 187.72 (diff 0.05).
- NMB FY2081-82: recomputed 175.18, printed 174.49 (diff 0.69);
  the printed NAV is also inconsistent across years (its previous
  column, 156.93, does not match FY2080-81's current NAV, 157.74).
  The panel uses the methodology definition (equity / year-end
  shares), not the printed NAV, and this disagreement is flagged
  here for the professor rather than overwritten.

## EPS (G4) — reported EPS is the panel value
Reported EPS is used, because it is profit attributable /
weighted-average shares by definition. Recomputing EPS with
year-end shares differs by more than 0.50 NPR in five bank-years,
all merger/bonus years where weighted-average shares differ from
year-end shares: GBIME FY2076-77 and FY2079-80, HBL FY2079-80,
KBL FY2076-77, NIMB FY2079-80. Those differences are expected,
not errors, and the reported EPS is retained.

## Prior-year continuity (G5) — restatements flagged
Total assets and PAT previous columns match the prior year's
current column exactly in most cases. Exceptions are restatements
in the reports themselves (merger years and bonus-issue EPS
restatements under IAS 33), not extraction errors:
- GBIME FY2078-79 total assets previous column differs from
  FY2077-78 current by 718,438,769 NPR.
- HBL FY2080-81 total assets previous column differs from
  FY2079-80 current by 1,877,083,471 NPR (Civil Bank merger year).
- KBL FY2078-79 (9,587,393 NPR) and FY2079-80 (1,047,386,219 NPR,
  NCC Bank merger year).
- KBL FY2076-77: its own SOFP (visual read, below) shows current
  total assets 153,341,629,610 and liabilities 136,073,455,939,
  while the FY2077-78 report's previous column shows 145,971,942,062
  and 128,703,768,392 — a restatement of 7,369,687,548 NPR in both,
  exactly the own report's derivative financial instruments lines.
  The panel uses the own-report values.
- NMB EPS previous columns are restated for bonus issues (e.g.
  FY2078-79 EPS previous 14.76 vs FY2077-78 current 16.66); the
  panel uses each year's own current-column EPS.
The panel uses each bank-year's own current column throughout,
so a restatement in a later report never overwrites an earlier
year's value.

## Visual extraction (G7/G8) — HBL and KBL FY2076-77 opening assets
Their own reports use a legacy/custom-encoded font whose text
layer is gibberish, so the text parser cannot read their SOFP
pages at all. The rendered pages were read visually instead, and
the values were saved — not typed into the panel by hand — in
`config/visual_overrides.json`, which both
`scripts/run_accounting_extract.py` and
`scripts/apply_manual_corrections.py` load and merge into the raw
JSON at extract time (visual overrides are applied last, so a
later manual-corrections run cannot silently revert them). The
raw JSONs therefore carry `method: visual_page_read` for these
values; the panel looks like a regular extraction, but the
provenance is not hidden. Rendered page evidence is kept in
`output/manual_review/visual/`.
- **HBL FY2076-77**, SOFP PDF p43 (printed p41, Consolidated
  Statement of Financial Position as on 31 Asar 2077): Bank
  Asar 2076 (FY2075-76) total assets **133,151,142,073**; identity
  117,156,343,693 + 15,994,798,380 = 133,151,142,073 exact.
  Current column matches the FY2077-78 previous column exactly,
  confirming the earlier manual correction. ROA =
  2,586,722,710 / ((133,151,142,073 + 155,884,918,983) / 2)
  = **1.7899%**.
- **KBL FY2076-77**, SOFP PDF p49 (printed p53, Statement of
  Financial Position as on 31st Ashad 2077): Bank FY2075-76 total
  assets **105,311,485,153**; identity 93,592,399,626 +
  11,719,085,527 = 105,311,485,153 exact. The same page also shows
  the own-report current values (total assets 153,341,629,610,
  liabilities 136,073,455,939), which supersede the earlier manual
  correction taken from the FY2077-78 restated previous column
  (see restatement note above). ROA on the consistent own-report
  basis = 1,158,505,956 / ((105,311,485,153 + 153,341,629,610) / 2)
  = **0.8958%**. Mixing the restated current value with the
  own-report opening value would have given 0.9221% and is NOT
  used.

## Manual corrections (G7) — five bank-years
See `scripts/apply_manual_corrections.py` for sources and checks.
In short: HBL FY2076-77, KBL FY2076-77 and NMB FY2076-77 values
come from the FY2077-78 previous column (identity and BVPS exact);
NMB FY2077-78 PAT/EPS come from its SOPL p43 direct text;
NMB FY2079-80 PAT comes from its Nepali SOPL p39 direct text.
All five pass identity and, where applicable, BVPS checks.

## DPS extraction (2026-10-27) — complete, 30/30
Source of record: `config/dps.json`, merged dynamically by
`src/data_extract/dps_overrides.py` and `scripts/apply_dps.py`
(same pattern as visual overrides). Each entry carries source
file, SHA-256, PDF page, printed page, verbatim quote, status,
and a note recording any disagreement resolved. DPS = cash %
proposed for that FY (face value NPR 100, so DPS NPR == cash %);
bonus % is recorded separately and never added to DPS.
18 bank-years have a positive cash proposal, 12 are documented
nil (DPS = 0.00 on a stated no-dividend decision, never by default).
No bank-year is left unavailable.

Disagreements resolved in the open (lead-verified, not taken on
a reader's word):
- NIMB FY2078-79: proposal note (7.00% cash / 4% stock) wins over
  the summary table's swapped split (cash 4.0%, total still 11.0%),
  proved by FY2079-80 equity/distributable pages showing bonus
  issued 732,301,653 and cash paid 1,281,527,893 — the proposal-note
  amounts. DPS = 7.00.
- NMB FY2077-78: Board/AGM (12.50% stock / 3.30% cash) wins over the
  Chairman's 12% / 3.50%, which sums to 15.50, not the stated 15.80
  total; AGM amounts check exactly. DPS = 3.30.
- KBL FY2076-77: assigned to FY2076-77 despite a board-report year
  mislabel, proved by Note 5.13 date, p35, amount checks against
  panel share capital, and FY2077-78 equity paid amounts.
- KBL FY2080-81 nil: printed BOD date (2 Jan 2024) predates the
  FY2080/81 year-end and is not quoted as verified; the nil
  substance (negative retained earnings) is documented.
- HBL FY2076-77 (visual, legacy font) corroborated by FY2077-78
  Principal Indicators FY2019/2020 column (cash 6.00%, total 20.00%).
- NMB FY2079-80 (Nepali visual): lead-read the rendered Board
  section 8, PDF p14, directly; evidence image in
  `output/manual_review/visual/NMB_FY2079-80_p14.png`.

Pipeline verified 2026-10-27: fresh `run_accounting_extract.py`
(30 rows, 0 failures) → `apply_manual_corrections.py` → `apply_dps.py`
gives DPS 30/30, ROA 30/30, max identity diff 1 NPR; tests 6 passed.

## MPS_post merge (2026-10-27) — 2 settled, 3 pending, 25 unavailable
Source of record: `config/mps.json`; merge: `src/data_extract/mps_overrides.py`
(`apply_mps`); script: `scripts/apply_mps.py`. Pipeline is now
`run_accounting_extract.py` → `apply_manual_corrections.py` →
`apply_dps.py` → `apply_mps.py` (MPS is also wired into the runner,
so a fresh extract alone contains it; the standalone script
re-adds the panel columns after the manual step regenerates the
panel without them). Unlike DPS, a missing MPS entry is a status,
not an error, because MPS collection is incomplete by design;
a pending entry carries candidate fields only and the module
raises if a candidate is ever promoted to a real price/date.
Full live-verification trail:
`output/manual_review/mps_verification.md`.

- **GBIME FY2081-82 — settled.** Disclosure 2025-10-16 (NEPSE
  19th AGM Notice attachment, pages 2–3 contain the FY2081/82
  summary statement tables; October 15 alternative rejected —
  its files contain AGM/book-close information only, no tables).
  First trading day 2025-10-19, MPS_post **240.00**, labelled
  **LTP** (Merolagani datewise; NEPSE Close not verified,
  FinancialNotices window does not reach October 2025).
  Corporate action: 8% cash only, book close 2025-11-02, after
  the price date.
- **NIMB FY2081-82 — settled.** Disclosure 2025-12-24 (NEPSE
  39th AGM and book-close notice attachment 1, a single scanned
  page carrying summary-statement and indicators tables).
  First trading day 2025-12-28 (2025-12-25 Christmas holiday,
  Friday/Saturday weekend), MPS_post **193**, labelled **Close**
  (FinancialNotices Close agrees exactly with Merolagani LTP).
  No dividend (NEPSE dividend declaration 2025-12-22 and the
  NIMB cover letter both state no cash and no bonus); book
  close from 2026-01-02, after the price date.
- **Held as pending (user decision 2026-10-27; price blank in
  the panel, candidates recorded only in `mps.json`/raw JSON):**
  HBL FY2081-82 (candidate 191.90 on 2025-12-28; AGM notice
  only, no separate statement disclosure found, NEPSE-side
  search incomplete); KBL FY2081-82 (candidate 181.40 on
  2025-12-15; AGM notice only in December 2025, separate full
  statement found on aggregators dated 2026-02-11 with no
  verified NEPSE timestamp — implication unresolved); NMB
  FY2081-82 (candidate 256.10 on 2025-12-17, NEPSE Close
  confirmed; no separate statement disclosure found, disclosure
  rests on the cover letter's same-day newspaper-publication
  assertion).
- **Regression sample realised: 2/30.** EPS, DPS, BVPS and ROA
  are 30/30, so a bank-year enters the sample exactly when its
  MPS_post is settled. Excluded: the 3 pending rows above
  (MPS_post held, not missing by oversight) and 25 rows with
  MPS_post unavailable (disclosure/price not yet collected or
  verified). No imputation was used anywhere.

## What is NOT in this panel (still outstanding)
- **MPS_post (28 rows):** the 3 pending and 25 unavailable rows
  above. See `market.py` stub (now superseded for the 2 settled
  rows by `mps_overrides.py`).
- **Analysis**: gated. The `analysis/` folder stays empty until
  the MPS_post coverage decision is made and this report's flags
  are reviewed. A regression on n=2 is not run.

## Files
- `output/tidy/accounting_panel.csv` — 30 rows, Bank column.
- `output/raw/*.json` — Group and Bank, pages, labels, manual
  correction notes where applicable.
- `output/audit/inventory.csv` — 31 files, 5,663 pages.
