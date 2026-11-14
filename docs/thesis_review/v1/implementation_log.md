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
- The `assemble_e.py` source is tracked at `src/thesis/generators/appendix_e/assemble_e.py`, and the Appendix E prose and table-note edits are ported into the generator sources. Regenerating the fragments and re-assembling reproduces the tracked `appendix_e.tex` exactly, so a re-run no longer reverts the edits.
- Some low-impact pipeline wording and fit-statistic presentation items in the review (including the unused formula-name note and a full R1–R9 fit-statistics display in the main chapter) are not changed because they do not affect the implemented results or primary thesis conclusions.

## Surgical P2 patches (2026-11-13, on the author's instruction)

- 0.709 sentence (Ch4:450, Ch5:132): now reads "In the $N=30$ model with the observed delayed prices, the pre-period BVPS estimate ..." — the ambiguity the author flagged is removed.
- App C caption: "eight plotted EPS-channel specifications (R1, R2, and R4 through R9)".
- m1: App E reference-category paragraph already in the tracked appendix (ported in 0619d4a); no further change.
- m2: reference categories are now explicit in code — `C(bank, Treatment(reference='GBIME'))` and `C(fy, Treatment(reference='FY2076-77'))` in `stats/models.py` and `stats/robustness.py`. Same references patsy used by default, so no number changes.
- m3: model and robustness formulas now name `price_rd` instead of `price`; `dataset.py` also computes `price_rd` on the bonus-adjusted frame so R7 fits. The raw `price` column is kept for traceability and the F6 open-marker plot.
- m6: Ch 3 already states within-bank serial independence as an untested assumption (line 350); no change.
- m7: the phrase "Huber-White cluster SEs" no longer occurs anywhere in the thesis; Ch 3 already distinguishes cluster-robust from HC3.
- m14: the Spearman (rho = 0.295, p = 0.128) and Shapiro-Wilk (MPS_RD p < 0.001, DPS p = 0.001) checks were already in the Ch 4 correlation text; a normality clause was added to the Table 4 note pointing to them.
- m16: Ch 4 R9 paragraph now states HBL FY 2076/77 is not covered by R9 and is addressed only by the single-observation leave-one-out sensitivity in Appendix E (App E part was already ported).
- m21: the Table 10 paragraph now explains the Within-R² jump (0.152 to 0.642): dummies alone explain 93.9% of total variation; slopes add 0.93 pp in Model 1 but 3.9 pp in Model 2.
- m24: R1–R9 fit statistics (R², adjusted R², Within-R²) added to the Table 8 note, same values as the App E robustfull note.
- m26: no `_combo` remains anywhere in the analysis package; post-slope inference is centralized in `linear_combination` and tested.
- m30: the R6 identical-results sentence was already in the Ch 4 text; verified by recomputation — dropping only the 4 mismatched FY 2078/79 rows (n = 24) gives Wald F = 5.817708, p = 0.021095, identical to R6 to 6 decimals.
- m31: the unsourced "(for bonus issues or share splits)" parenthetical was removed from Ch 3; the sentence now states only the sourced fact (restatements as printed in subsequent annual reports). Q11 is closed by removal.
- m38: the Table 3 note already documents sample SD (ddof = 1) and the %-change formula; no change.
- m39: all five SD % changes were already reported in the prose. Correction found during verification: the printed % changes had been computed from 2dp-rounded SDs/means, not full precision. Corrected to full-precision values (verified twice, independently): MPS mean -33.81% (was -33.80%), NPR 105.00 (was 104.99); EPS mean -40.13% (was -40.11%), SD +63.95% (was +63.66%), CV 61.0% (was 60.9%); BVPS mean +2.45% (was +2.44%), NPR 3.87 (was 3.86), SD -15.30% (was -15.29%); DPS SD -16.62% (was -16.57%), CV 58.8% to 212.2% (was 58.7% to 212.1%); ROA mean -46.38% (was -46.56%), SD +97.49% (was "doubled"), CV 16.9% to 62.2% (was 16.8% to 62.9%). The same corrections were applied to the Ch 5 summary repeats and the Ch 4 Discussion EPS repeat.
- s3: R4 paragraph now states DPS enters as an additive control and cites the interacted variant (Model 2 + DPS + DPS x Post, df = 12): joint Wald F = 2.848, p = 0.097, the same non-rejection as additive R4. Verified by recomputation (F = 2.847907, p = 0.097244; DPS x Post coef -3.651, p = 0.735).
- s7: the phrase "trading window" no longer occurs anywhere; the notes already say "five calendar days" and "the first active session on or after the target".
- s8: DPS post median zero was already stated; no "halved" occurs anywhere in the thesis; the Assessment column was already dropped from Table 10.
- Table 10 overfull: fixed by reducing that table's `\tabcolsep` from 4pt to 3.5pt. The v33 build confirms the 2.68pt overfull is gone; only the standing 0.27pt Chapter III overfull remains.

## Verification performed (this round)

- `python -m pytest analysis/tests -q` under the pinned statsmodels 0.14.6 venv: 28/28 pass. (Two defects were found and fixed during this round: the Within-R² guard checked for the literal `"C(bank)"` substring, which the explicit `Treatment(...)` form no longer contains — now checks `"C(bank"`; and the bonus-adjusted frame lacked `price_rd`, which R7 needs — now computed in `dataset.py` by the same short-window rule.)
- Full pipeline regeneration (`analysis.scripts.generate`): 18 assets ok; all generated `.tex`/`.md` tables byte-identical to the committed versions, so the m2/m3 code changes move no number. Re-rendered figure binaries differ only by render noise and were reverted, not committed.
- Full thesis build v33 from the patched tree: 163 pp, 0 errors, 0 undefined, 0 bibtex warnings; build log on the VM at `~/workspace/frontmatter_build/work_v33c/build4.log`; PDF at `~/workspace/frontmatter_build/thesis-full-ch1-5-v33.pdf`. The corrected descriptives values were checked in the built PDF text (new values present, old values absent).

## Still deferred (not surgical)

- s1 (wild-cluster bootstrap) and s2 (post slopes per robustness spec) remain deferred: both add new analysis rather than correcting a reporting error.

## s1 and s2 implemented (2026-11-13, on the author's instruction)

- s2: post slopes are now computed in code — `post_slopes(run)` in `stats/robustness.py`, via the centralized `linear_combination` (HC3 covariance). Verified against the review's own recomputation: R5 post EPS 3.415 (SE 3.891, p = 0.401), post BVPS -2.081 (SE 1.969, p = 0.315); R6 post EPS 1.900 (SE 2.649, p = 0.490), post BVPS -1.809 (SE 1.357, p = 0.212). Both are now reported in the Ch 4 R5/R6 paragraphs. All eight post-slope pairs (R2–R9) keep the baseline signs (EPS positive, BVPS negative) and none is significant; R2 matches thesis Table 6 (2.453, -1.658).
- s1: wild-cluster bootstrap implemented in `stats/wild_bootstrap.py` — null imposed by fitting Model 1, restricted residuals resampled by bank with Rademacher weights, HC3 Wald statistic recomputed on each bootstrap sample. With G = 5 there are only 32 distinct sign patterns, so all 32 are enumerated (no RNG; fully deterministic). Results: Model 2 bootstrap p = 0.031 (1/32) vs HC3 p = 0.085; R6 bootstrap p = 0.062 (2/32) vs HC3 p = 0.021. Each HC3 decision flips under the bootstrap, each flip on a single pattern. Verified independently: a 9,999-draw random Rademacher bootstrap gives p = 0.029 (M2) and p = 0.066 (R6), consistent with the enumeration within Monte Carlo error, and the all-+1 pattern reproduces each observed Wald statistic exactly. Method described in Ch 3, results reported in Ch 4 and summarized in Ch 5. The check is inconclusive at G = 5 and does not overturn the HC3 inference; it confirms both joint-test decisions are fragile at this sample size.
- **Correction (final review v2, 2026-11-14): the M2 bootstrap p-value above was wrong.** In exact arithmetic the all−1 pattern must also reproduce the observed Wald exactly (interaction coefficients negate, residuals negate, HC3 covariance identical), so the count is mathematically ≥ 2 and the correct M2 value is **0.062 (2/32)**, not 0.031. The 1/32 was a last-ulp floating-point artifact: the statsmodels all−1 F\* fell 1.9e-13 below the observed statistic and was not counted (the 9,999-draw check quoted above suffers the same artifact). Only the R6 decision flips under the bootstrap; in exact arithmetic neither bootstrap p is below 0.05. Fixed in the v2 pass below (tolerance-robust comparison, corrected Ch4/Ch5 sentences, corrected test pin). The qualitative conclusion (inconclusive, does not overturn HC3) is unaffected and reinforced.
- Tests: 30/30 pass under the pinned statsmodels 0.14.6 venv (28 prior + 2 new: post-slope values, bootstrap determinism/coarseness/pins).
- Outputs regeneration: 18 assets ok; no generated .tex/.md table changed (the new functions are not called by the generators); figure binaries + manifest reverted, not committed.
- Full thesis build v34 from the patched tree: 163 pp, 0 errors, 0 undefined, 0 bibtex warnings, only the standing 0.27pt Chapter III overfull; build log on the VM at `~/workspace/frontmatter_build/work_v34/build4.log`; PDF at `~/workspace/frontmatter_build/thesis-full-ch1-5-v34.pdf`. New Ch 3/Ch 4/Ch 5 sentences verified present in the built PDF text.

## m20/s5 closed (2026-11-14)

- The Within-R² formula was still missing from Chapter 3 (the review's m20: "No Within-R² formula anywhere; definition verbal only; Ch 3 defines no R²"). A "Goodness of Fit" item was added to Ch 3 §3.6.5 stating both formulas: $R^2 = 1 - \text{SSR}_{\text{LSDV}} / \text{SST}$ and $\text{Within-}R^2 = 1 - \text{SSR}_{\text{LSDV}} / \text{SSR}_{\text{dummies}}$, with the explicit note that it is not the one-way within-$R^2$ and is not computed by demeaning (s5). This matches the code (`models.py` computes `1 - results.ssr / fe_only.ssr`) and the Ch 4 verbal definitions. Full thesis build v35: 164 pp, 0 errors, 0 undefined, 0 bibtex warnings, only the standing 0.27pt overfull; build log at `~/workspace/frontmatter_build/work_v35/build4.log`; PDF at `~/workspace/frontmatter_build/thesis-full-ch1-5-v35.pdf`. The new paragraph was verified present in the built PDF text. No review item remains open.

## Final review v2 and its fixes (2026-11-14)

- Independent final review at `docs/thesis_review/v2/final_review.md` (coordinator + 3 subagents, read-only). Verdicts: closure NOT CLEAN as stated (13/14 Majors, 33/40 minors, 6/8 suggestions); new content ONE MATERIAL ERROR; fresh-error scan ONE NEW ERROR + one pre-existing defect; build + tests CLEAN (30/30, 164 pp, 0 errors). Findings: 0 Critical, 1 Major (F-S1), 8 Minor, 2 Suggestion. All fixed in this pass:
- **F-S1 (Major):** M2 bootstrap p 0.031 → **0.062 (2/32)**; Ch4/Ch5 "each decision flips" corrected to "only the R6 decision flips"; test pin 1/32 → 2/32, n_exceed 1 → 2; comparison made tolerance-robust (`F* >= F_obs - 1e-9`) with the exact-arithmetic reason documented in the module docstring. Verified by direct recomputation (all−1 diff −1.887e-13 for M2, +1.756e-12 for R6). Both bootstrap p-values are now 0.062; tests 30/30.
- **F-T4NOTE:** missing period restored in the Ch 4 Table 4 note (m14 edit artifact).
- **F-M19:** App E flagged tables now in descending Cook's-D order via a sort in `gen_tables_e.py` / `gen_tables_e2.py`; regenerated fragments + `appendix_e.tex` change only in those two tables (M1: 0.5519, 0.4124, 0.2711, 0.2447, 0.1451; M2: 0.4902, 0.3983, 0.2404, 0.1870, 0.1513).
- **F-M18:** threshold-dependence sentence added to the Ch 3 Cook's-D item (D > 1: 0; 4/(n−K−1): 3 in M1, 2 in M2; 4/n: 5 each — counts verified by recomputation).
- **F-M32:** the two Ch 5 Implications sentences qualified ("as suggested by the imprecise point estimates"; "the imprecise estimates are consistent with").
- **F-M33:** effective-N sentence added to the Ch 3 MDE paragraph (effective N < 28, MDEs are optimistic upper bounds).
- **F-M14:** explicit disclaimer added after the Ch 3 five-day rule (the length is an un-derived operational choice; no rationale on record). No rationale was invented.
- **F-M34:** disclosure-date coverage stated in Ch 3 (investigated only for the five FY 2081/82 bank-years; 2 settled, 3 pending, 25 unrecorded), matching App D.
- **F-S4:** R²-comparability note added to the Ch 4 Table 8 note (not comparable across n=23 vs n=28).
- **F-S6:** App E collinearity sentence reworded in the generator prose (HC3 intervals reflect sampling variance under heteroskedasticity, not collinearity as such); regenerated.
- **F-M29:** documented here, no text change — the proposal is read-only by standing rule, so its "Models 1 and 2" wording stands; the thesis side is clarified. Only the author can close this (proposal correction with his explicit permission).
- **Q9 residue:** generator note `table_map_frozen.md` now says `statsmodels==0.14.6`.
- **Still open (author questions, not fixable here):** Q4 (VIF slopes-only convention — disclosed, no authority cited); figure pixels unverified (v1 limit, unchanged); carry-forward pair 2 provenance (documented in App D/README, not in any CSV).
- Tests: 30/30 pass under the pinned statsmodels 0.14.6 venv. Full thesis build v36: 164 pp, 0 errors, 0 undefined, 0 bibtex warnings, only the standing 0.27pt Chapter III overfull; build log at `~/workspace/frontmatter_build/work_v36/build4.log`; PDF at `~/workspace/frontmatter_build/thesis-full-ch1-5-v36.pdf`. Corrected bootstrap sentences and the Table 4 note period verified present in the built PDF text; no old wrong value remains.
