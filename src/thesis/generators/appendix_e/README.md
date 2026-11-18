# Appendix E generators

Generates Appendix E (Tables 20-31) and the Appendix C forest figure
from the frozen fitted results. All paths are resolved from this
directory, so the scripts run from any checkout of this repository.

## Regeneration pipeline

1. `compute_e.py` -> `results.pkl`: round 1, Models 1/2 and R1-R8,
   joint fixed-effect tests, diagnostics, leave-one-out and leave-one-bank
   sensitivity. OLS + MacKinnon-White HC3 in numpy/scipy.
2. `compute_r9.py` -> `results_r9.pkl`: R9, Model 2 excluding NMB
   FY 2076/77. Its result is merged into `results.pkl`.
3. `compute_r10.py` -> `results_r10.pkl`: supplementary post-hoc R10,
   Model 2 excluding NMB and KBL FY 2076/77. Its result is merged into
   `results.pkl`.
4. `compute_e2.py` -> `results2.pkl`: Model 2 diagnostics, VIFs, joint
   fixed-effect tests for R2-R10, leave-one-year fits, and
   post-consolidation confidence intervals. Run after steps 1-3; the
   script stops with a clear error if any required fit is missing.
5. `gen_tables_e.py` -> `tables_e_fragment.tex`: 6 table blocks
   (m1full, m2full, fetests, robustfull, flagged, sensitivity).
6. `gen_tables_e2.py` -> `tables_e2_fragment.tex`: 6 table blocks
   (robust_inf, robust_fe1, robust_fe2, robust_fetests, m2flagged, loy).
7. `assemble_e.py` -> `src/thesis/appendices/appendix_e.tex`: splices
   the 12 blocks into `appendix_e_prose.tex` at the `@@T01@@`..`@@T12@@`
   markers. It asserts 6 blocks per fragment and the label of every
   block; it overwrites `appendix_e.tex`.

## Rules

- Never hand-edit `appendix_e.tex` or either fragment. Edit the prose
  in `appendix_e_prose.tex` or the table notes in `gen_tables_e.py` / `gen_tables_e2.py`,
  then re-run steps 5-7 and check `git diff`. A re-run must reproduce
  the tracked `appendix_e.tex` exactly.
- `results.pkl`, `results2.pkl`, `results_r9.pkl` and `results_r10.pkl`
  are checked in as frozen inputs so the table generators run without
  recomputing the fits. Recompute them through `compute_e.py`,
  `compute_r9.py`, `compute_r10.py`, and `compute_e2.py`, in the order
  above.
- `rebuild_a2.py` rebuilds `src/thesis/figures/A2_robustness_forest`
  (PDF + PNG) from the pickles.
- `patch_v29.py` is a historical one-off (mechanical v29
  substitutions, with asserted occurrence counts). Do not re-run it.