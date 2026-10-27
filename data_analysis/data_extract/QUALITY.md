# Quality gates — professor-grade, non-negotiable

These gates are the standard for this extraction. A panel that fails
any gate is not emitted, and a bank-year that fails a gate is not
silently repaired. This document is the checklist the final
extraction report must answer, gate by gate.

## G1 — Provenance for every value
Every panel cell carries: source PDF (with SHA-256), PDF page(s),
extraction method (text layer / table / OCR / manual), confidence,
and unit as read. A value without provenance is rejected by the
writer. No number enters the panel on the basis of "it looked right".

## G2 — Both columns, one declared primary
Where a statement prints Group and Bank columns, both are extracted
into `output/raw/`. The panel uses one declared primary (Bank column,
see note below) and the other is kept for sensitivity checking.
Switching primary must not require re-extraction.

Note on primary: per-share measures (EPS, BVPS) are defined on the
bank's own shares, so the Bank column is primary. Group figures are
retained in raw JSON so the choice is auditable and reversible, and
the final report must state it explicitly for the professor.

## G3 — Accounting identities, exactly
For every bank-year, in the primary column:
- Total assets = total liabilities + total equity
- Total liabilities + equity = the printed "Total Liabilities and
  Equity" line
- Share capital + reserves + retained earnings reconcile to total
  equity attributable to equity holders (within published rounding)

Tolerance is published rounding only (statement units), stated in
the report. A failure is a parser bug or a misread column, not a
rounding footnote to wave through.

## G4 — Recompute, never copy
EPS, BVPS and ROA are recomputed from audited inputs:
- EPS = profit attributable / weighted-average ordinary shares
- BVPS = ordinary equity / shares outstanding at year-end
- ROA = PAT / average total assets x 100

Each recomputed value is compared with the reported ratio in the
same report. A disagreement beyond tolerance goes to manual review
with both numbers cited. The reported ratio is never the panel value
on its own.

## G5 — Prior-year continuity (no loss, no drift)
For every series, the prior-year column of year t+1 must equal the
current-year column of year t, for total assets, total liabilities,
total equity and PAT — except where the report itself restates a
prior year, in which case the restatement note is recorded and the
restated figure is the one used, with both figures kept in raw JSON.
A silent break in continuity means a column was misread.

## G6 — Completeness, counted not claimed
The final report states, per bank and per variable, how many of the
6 bank-years are present, and lists every missing cell by name.
Missing means unavailable (documented, e.g. no dividend
recommendation established) — never imputed, never zero-filled
except the one documented case in the methodology: a documented
decision to recommend no cash dividend, which is DPS = 0 with its
source cited.

## G7 — Manual verification, every bank-year
Automated checks are necessary but not sufficient. Before the panel
is declared final, each of the 30 bank-years is checked by reading
the source statement pages and confirming, by eye, the key lines:
total assets, total liabilities, total equity, PAT, profit
attributable, share capital, and the reported EPS. The verification
log records who/what checked each bank-year and any correction made.
Sampling is not accepted: 30 bank-years, 30 checks.

## G8 — No silent fallbacks
- A dash or blank in a statement means "not stated", never zero.
- An OCR value is low-confidence and goes to manual review.
- A legacy-font page (NMB FY 2079/80 Nepali) is never read from its
  text layer.
- Visual page reading is the one approved exception to text-layer
  extraction, and only under these conditions: the value is read
  from a rendered page image, saved in config/visual_overrides.json
  with source file, SHA-256, printed and PDF page numbers, merged
  dynamically at extract time, labelled method=visual_page_read in
  the raw JSON, and checked by the accounting identity for both
  columns. It is never typed directly into the panel.
- A parser that cannot find a statement page fails loudly for that
  bank-year; it does not borrow a value from a summary table, a
  quarterly statement, or another year.

## G9 — Reproducibility
- Every source PDF is hashed (SHA-256 in inventory.csv).
- The extraction code version and config are recorded with the run.
- Pure functions (units, FY mapping, EPS/BVPS/ROA, identities) are
  unit-tested; parsers are tested on fixture pages.
- Re-running extraction on the same PDFs must reproduce the same
  panel, or the difference must be explained in the report.

## G10 — The panel is not the analysis
Even a fully verified panel does not complete the model dataset:
MPS_post comes from NEPSE records, not PDFs (see market.py). The
analysis folder stays gated until the market fields are filled from
NEPSE and the extraction report passes G1–G9.

## Pilot check already done (GBIME FY 2080/81, SOFP)
Group: 548,625,844,867 (liabilities) + 63,153,517,329 (equity)
  = 611,779,362,196 (total assets) — exact.
Bank: 543,110,969,431 + 61,407,147,643 = 604,518,117,074 — exact.
This is the standard every other bank-year will be held to.
