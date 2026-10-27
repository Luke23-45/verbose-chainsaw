# Analysis — gated

Do not start work here yet.

This folder will hold the descriptive statistics, Pearson correlations
and pooled OLS from the proposal (methodology §07), reading only
`../data_extract/output/tidy/bank_year_panel.csv`.

It unlocks when, and only when, all of these are true:

1. `../data_extract/output/audit/extraction_report.md` exists and
   lists no unresolved validation failures.
2. `../data_extract/output/audit/missingness.csv` is reviewed, and
   every incomplete bank-year is excluded (not imputed) from the
   regression sample, with the realised sample size stated.
3. The market-data fields in `market.py` (NEPSE disclosure date,
   first trading day after it, `MPS_post`) are filled from NEPSE
   records — the PDFs alone do not complete the model dataset.

Until then, this folder stays empty on purpose. Starting the
regression on an unvalidated panel would bake extraction errors
into the thesis results.
