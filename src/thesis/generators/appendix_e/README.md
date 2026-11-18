# Appendix E generators

Generates Appendix E (Tables 20-31) and the Appendix C forest figure
from the frozen fitted results. All paths are resolved from this
directory, so the scripts run from any checkout of this repository.

## Regeneration pipeline

1. `compute_e.py` -> `results.pkl` — round 1: Models 1/2, R1-R8, joint
   fixed-effect tests, diagnostics, leave-one-out and leave-one-bank
   sensitivity. OLS + MacKinnon-White HC3 in numpy/scipy.
2. `compute_e2.py` -> `results2.pkl` — round 2: Model 2 diagnostics,
   Model 2 VIFs, joint fixed-effect tests for R3-R8, leave-one-year
   fits, post-consolidation confidence intervals.
3. `compute_r9.py` -> `results_r9.pkl` — R9 only (Model 2 excluding
   NMB FY 2076/77). Its result is merged into `results.pkl`.
4. `gen_tables_e.py` -> `tables_e_fragment.tex` — 6 table blocks
   (m1full, m2full, fetests, robustfull, flagged, sensitivity).
5. `gen_tables_e2.py` -> `tables_e2_fragment.tex` — 6 table blocks
   (robust_inf, robust_fe1, robust_fe2, robust_fetests, m2flagged, loy).
6. `assemble_e.py` -> `src/thesis/appendices/appendix_e.tex` — splices
   the 12 blocks into `appendix_e_prose.tex` at the `@@T01@@`..`@@T12@@`
   markers. It asserts 6 blocks per fragment and the label of every
   block; it overwrites `appendix_e.tex`.

## Rules

- Never hand-edit `appendix_e.tex` or either fragment. Edit the prose
  in `appendix_e_prose.tex` or the table notes in `gen_tables_e.py` /
  `gen_tables_e2.py`, then re-run steps 4-6 and check `git diff`.
  A re-run must reproduce the tracked `appendix_e.tex` exactly.
- `results.pkl`, `results2.pkl` and `results_r9.pkl` are checked in as
  frozen inputs so the table generators run without recomputing the
  fits. Recompute them only through `compute_e.py`, `compute_e2.py`
  and `compute_r9.py`, against the pinned `statsmodels==0.14.6`.
- `rebuild_a2.py` rebuilds `src/thesis/figures/A2_robustness_forest`
  (PDF + PNG) from the pickles.
- `patch_v29.py` is a historical one-off (mechanical v29
  substitutions, with asserted occurrence counts). Do not re-run it.
