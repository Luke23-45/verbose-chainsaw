# Implementation log: data analysis review v1

## Follow-up verification

- Refit Model 2 on all 30 observed prices using the repository pipeline: (F(2,16)=4.761626), (p=0.023849), pre-period BVPS (=0.708829). This confirms the reported (4.762), (0.024), and (0.709) sensitivity values.
- Recomputed the single-coefficient MDEs with the noncentral-(t) distribution at two-sided (α=0.05), 80% power, and (df=14): 10.728 NPR (pre-period EPS), 12.062 NPR (δE), and 3.708 NPR (δB). The thesis reports these as 10.73, 12.06, and 3.71 NPR.
- Recomputed the EPS–ROA bivariate VIF from the unrounded 28-row analysis sample: (r=0.974656), VIF (=19.982). The review's 16.9 value applies the formula to rounded (r=0.97); the updated generator reports approximately 20.
- R6's previously recorded statistic (F=5.8177) against the (df=(2,10)) 5% critical value of about 4.103 gives a 29.5% reduction margin. The Holm-adjusted p-value remains 0.169 as already independently reproduced in the original implementation plan.
- Refit both carry-forward pairs on the 30-row panel: HBL/NIB 487/453 (12 May 2021) gives F=3.870470, p=0.042558; the alternative 484/460 pair (reported 13 May 2021) gives F=3.821406, p=0.043991. The pairs differ by one day/source and both are stale relative to the April 2022 price target.

## Changes applied

- Regenerated T2–T6 and A5 table outputs from the existing pipeline; T5 now includes R9, T3/T4 include Within-R², T4 includes adjusted R², T6 includes classical BP and Model 2 VIFs, and A5 includes the year-FE model, coefficient SEs and p-values, adjusted R², and Within-R² where applicable.
- Updated the partial-generation behavior so the output manifest retains hashes for assets not selected in a targeted generation run.
- Corrected the Chapter 4/Table 10 specifications, reporting precision, diagnostic interpretation, sensitivity results, descriptive-statistics method, and non-normality caveat. Added the post hoc MDE explanation and R6 fragility/sensitivity wording across relevant chapters.
- Named both carry-forward input pairs and their provenance discrepancy in the thesis, clarified that both are stale-price scenarios, aligned the robustness-figure count wording, and brought the hand-maintained Chapter 4 T4/T6 tables into line with generated values (Adjusted R² and Model 2 VIF rows).
- Centralized post-slope linear-combination inference and added a focused test. Recorded statsmodels 0.14.6 in Appendix D.
- Updated Appendix E prose for reference-category interpretation, Shapiro-Wilk/Q-Q results, and leave-one-out attribution.
- The five-digit R4 result 0.0997 is intentionally still printed as 0.100 to three decimals; that is correct rounding. It is not changed to a four-digit value in a table whose p-values are otherwise printed to three decimals.

## Verification performed

- Selected table generation completed successfully for T2, T3, T4, T5, T6, and A5.
- `analysis.scripts.verify`: all 18 assets present; all 72 recorded output hashes consistent.
- `python -m pytest analysis/tests -q`: passed (exit code 0).
- No thesis PDF build was run.

## Deferred or unavailable items

- Optional suggestions that would add a new estimator or specification (wild-cluster bootstrap, reporting R5/R6 post-slopes, and an interacted DPS variant) are deferred; the last changes the model rather than correcting a reporting discrepancy.
- The external `assemble_e.py` source mentioned in the audit is absent from the repository and the checked parent project directory. Appendix E's tracked `.tex` source is updated, but whether the external assembler overwrites it remains unverified.
- Some low-impact pipeline wording and fit-statistic presentation items in the review (including the unused formula-name note and a full R1–R9 fit-statistics display in the main chapter) are not changed because they do not affect the implemented results or primary thesis conclusions.
