# Data analysis

This folder is the analysis workspace for the thesis. It is deliberately
separate from `../data/`, which holds the raw audited PDFs and is never
edited by code in here.

## Layout

- `data_extract/` — the extraction pipeline. This is the only stage that
  reads the PDFs. It turns 30 audited reports into a validated, tidy
  bank-year panel, with a source page recorded for every value.
- `analysis/` — **gated, intentionally empty for now.** Descriptive
  statistics, correlations and the pooled OLS in the proposal
  (methodology §07) live here, and only start once
  `data_extract/output/audit/extraction_report.md` passes its checks.
  Nothing in `analysis/` may read a PDF directly; it reads only the tidy
  panel exported by `data_extract/`.

## The one rule that governs both stages

A bank-year is in the analysis only if it is complete for all model
variables. Unavailable or unverifiable observations are reported, never
imputed, and the realised sample size is stated. That rule comes straight
from the proposal methodology, and the extraction pipeline enforces it
with a missingness report rather than by filling gaps.

## What the PDFs alone cannot give you

The PDFs supply the accounting side: EPS, DPS (recommendation), BVPS and
the inputs to ROA. They do **not** supply the dependent variable,
post-disclosure market price per share (`MPS_post`), which needs the
NEPSE disclosure date and the first trading day after it. That is a
separate market-data input (see `data_extract/src/data_extract/market.py`),
and it is never invented from a PDF.
