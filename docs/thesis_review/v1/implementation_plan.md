# Implementation Plan: Data Analysis Review v1

**Purpose:** Convert the findings in [`data_analysis_review.md`](data_analysis_review.md) into a controlled implementation sequence for the thesis. This file began as a plan; implementation status is recorded at the end.

**Scope:** Methodological decisions, analysis reporting, thesis text, and the analysis pipeline/tests where traceability requires it. The extracted data remain the agreed ground truth. No extraction audit, redesign, or thesis rebuild is included in this planning stage.

**Plan basis:** Review findings checked against commit `0283469` and current source/output files (2026-11-12). The review file remains the findings register; this plan maps and sequences its findings rather than replacing them.

## Triple-check completed

I checked the current analysis code and thesis passages cited by the highest-priority findings, then independently reran the key specifications from the repository's analysis code under the locally available statsmodels 0.14.6:

- Model 2 on the stated 28-row sample: Wald F(2,14) = 2.9545, p = 0.08503.
- Model 2 with all 30 observed prices included: Wald F(2,16) = 4.7616, p = 0.02385.
- The code calls `het_breuschpagan` with its default `robust=True`; for Model 1 this reproduces the Koenker LM = 14.3695, p = 0.2132 reported in the review.
- The current R2–R9 code returns eight joint-test p-values. R6 is the sole unadjusted result below .05 (F = 5.8177, p = 0.02109). Holm adjustment across those eight tests gives R6 p = 0.16876.
- The review's current summary records 14 Major findings, 40 Minor findings, and 8 Suggestions. Its prior “working tree” description is historical; the present checkout is clean before this plan is added.

These checks validate the key review claims against the current code path. They do not independently reproduce every value in the 73 KB review, pixel-check figures, or establish the author's intended price-window/missingness assumptions. Those remain review limitations or author decisions described below.

## Principles for execution

1. Keep the review itself intact as the evidence record. Resolve each action by linking it to finding IDs and recording the final disposition.
2. Keep the existing raw data and extraction outputs fixed. Add no imputation or new data unless the author explicitly changes the agreed ground-truth scope.
3. Resolve assumptions that can change the headline result before editing conclusion language.
4. Separate the pre-specified primary Model 2 inference from sensitivity specifications. Show raw and multiplicity-adjusted sensitivity results transparently; do not silently change the primary 5% decision rule.
5. Where the author's intent cannot be inferred (price window, missingness mechanism, VIF convention), document the chosen rationale and its source instead of writing an unsupported explanation.
6. Make analysis/report changes first, regenerate only affected analysis tables/figures after those changes are approved, then edit the canonical thesis `.tex` sources. Do not make changes only in converted Markdown copies.

## Phase 1 — Resolve decisions that affect the headline conclusion

| Decision | Review findings | Work and decision record | Exit condition |
|---|---|---|---|
| Price freshness rule and two delayed rows | M4, M5, M14; Q1–Q2 | Record why five days is the intended freshness boundary and whether the estimand is an immediately post-deadline price or the next available price after a suspension. Keep the 28-row rule as the stated primary sample unless the author revises the design. Add a clearly labelled sensitivity that includes the two observed delayed prices (N=30; current code gives F=4.762, p=.024). Do not carry prices forward or treat 47/54-day prices as five-day observations without a defensible design decision. Describe the merger-related suspension and discuss plausible missingness/bias; do not label the mechanism MCAR/MAR/MNAR without author support. | Author/supervisor rationale is recorded; primary sample and sensitivity estimand are explicitly distinguished; any changed sample rule is approved before recalculation. |
| R6 and multiplicity | M3, M13; Q7 | Identify the family as the eight joint tests R2–R9 and state whether they are primary or sensitivity analyses. Retain unadjusted p-values for transparency, report a Holm-adjusted R6 p≈.169 as a sensitivity-family calibration, and explain that R6 is the only raw rejection, R5 does not reject at the same N/df, neither R6 interaction is individually significant, and the joint statistic is close enough to its critical value that a 29.5% reduction would remove the raw rejection. Correct the R6 leave-one-out attribution: the “1 of 28” result is baseline M2, while 16/23 R6 deletions remain below .05. | R6 wording reflects its sensitivity status and the multiplicity family; the primary hypothesis decision is not silently redefined. |
| Power / detectable effects | M1; Q6 | Add a design-sensitivity/MDE explanation with the assumptions, test, degrees of freedom, target power, and effect scale stated. Present the review's approximate thresholds only after recomputing and documenting the method. Phrase them as detectable-effect limits, not as proof that small or moderate effects are absent and not as retrospective “observed power.” | The thesis states what null findings can and cannot establish, with computation and assumptions traceable. |

## Phase 2 — Correct method and diagnostic reporting

| Work item | Review findings | Planned change | Acceptance check |
|---|---|---|---|
| Name the heteroskedasticity test variant | M6, m19; Q3 | State that the implementation uses the Koenker form (statsmodels default `robust=True`). Reconcile the “Passed” label with the classical BP result for M1 (LM=28.18, p=.003); report the chosen variant and, if useful, the alternative result without implying the test proves homoskedasticity. | Thesis description, table note, code parameters, and displayed values refer to the same variant. |
| Reframe influence and residual diagnostics | M7, M8, m17–m19 | Replace “Mitigated via HC3” with a precise statement: HC3 changes the covariance/standard errors, while the existing leave-one-out exercise is the influence sensitivity. Add a short reading of the Q-Q plots and the review's Shapiro results (M1 p=.045, M2 p=.038), or explain why only graphical assessment is retained. Define or remove “residual standard deviation screening.” | No claim says HC3 removes influential observations; diagnostic interpretation and procedure are stated plainly. |
| Limit VIF claims to the models actually assessed | M10, m13, Q4 | Restrict the approximately 1.16 statement to Model 1. Show or discuss Model 2 VIFs already disclosed in Appendix E and reconcile the threshold of 5 in methodology with the threshold of 10 used for the Table 9 pass label. State whether fixed-effect dummies are excluded and support the selected convention; leave the choice explicitly open until the author confirms it. | Each VIF statement identifies model, regressors included, threshold, and interpretation. |
| Qualify the interpretation of estimates | M2, m32, m36 | Describe relative slopes as point-estimate comparisons, include uncertainty where “earnings dominate” or “no flight to book value” is discussed, and avoid presenting insignificant estimates as established valuation patterns. Correct the backwards RQ1 sentence so year effects are included when explaining the high two-way-FE R². | Abstract/conclusions do not turn imprecise point estimates into established effects or confuse included and omitted year effects. |
| Clarify specification comparison | M11, M12, m21–m24; Q8 | Add the year-FE-only comparison (review result R²=.919) and the bank-FE-given-year-FE test (F(4,16)=2.23, p=.112), with adjusted and Within-R² context. Explain that raw R² changes with included fixed effects and should not be read as a direct measure of the substantive regressors' contribution. | Table/text distinguishes pooled, year-FE, and two-way-FE fits and identifies the comparison being made. |

## Phase 3 — Improve reproducibility and pipeline traceability

These are maintenance changes to the existing analysis project, not a rebuild of the thesis.

1. **Compute Within-R² in the analysis pipeline** (M9, m20–m21). Implement one documented definition consistent with the review's verified calculation, use it for the relevant model outputs, and add a focused test against an independently stated expected value or invariant. Remove hand-entered Within-R² values from generated table sources.
2. **Generate Model 2 VIFs from code** (M10, Q4). Add an explicit calculation for the Model 2 substantive slopes/interactions, document whether FE dummies are excluded, and cover the output with a focused test. Do not change the thesis's convention until the author resolves Q4.
3. **Pin and record the analysis environment** (m40). Record the exact supported Python and library versions used for the reported results. Keep current numeric outputs as regression references and verify them after dependency changes.
4. **Update stale robustness maintenance artifacts** (m9, m10). Update the test expectation from R1–R8 to R1–R9 and regenerate the generated T5 Markdown/TeX table so R9 appears. Confirm the thesis's current Table 8 already includes R9 before replacing any source text.
5. **Remove minor internal inconsistencies** (m8, m11–m15, m25–m26, m37–m40). Fix generated table wording and rounding only after confirming source precision; test post-slope computations if they remain reported; reconcile the correlation-script variance-inflation note and VIF thresholds.

**Acceptance checks:** the analysis test suite passes; generation/check mode reports no stale assets; all generated tables include the same specification set; key coefficients, standard errors, p-values, and Wald tests remain within the review's documented tolerances unless a resolved methodological decision intentionally changes the sample or model. Record any changed values and why.

## Phase 4 — Complete thesis traceability and wording

Apply after Phases 1–3 are resolved so prose and numbers are synchronized.

- Add the R9 robustness objective where the objectives enumerate robustness analyses (m28); correct “eight robustness checks” to “nine” in Chapter 2 (m27). Preserve the accurate Chapter 4 phrase referring to the eight plotted specifications.
- Clarify that ROA and DPS are Model 2 robustness variants, consistent with implementation (m29).
- Fix the phrase “eliminates look-ahead bias” to a calibrated description of the reporting-deadline pricing protocol (m35); verify publication-date coverage statements and describe their limits (m34).
- Resolve the minor reporting items m1–m7, m16–m18, m20–m26, m30–m31, m33, m38–m39 from the review register. For every text change, keep the claim tied to the cited table, model, or diagnostic. Do not add a causal claim.
- Consider suggestions s1–s8 individually. These are optional and should be either adopted with a documented rationale or marked deferred; they are not prerequisites for changing the main conclusion.

## Execution order and deliverables

1. Record author/supervisor decisions for the Phase 1 questions.
2. Recompute only analyses affected by those decisions in the existing analysis pipeline; retain a run log with environment/version, inputs, command, and outputs.
3. Implement traceability changes and focused tests in the analysis project; regenerate only affected analysis tables/figures.
4. Update the canonical thesis `.tex` passages, tables, and appendix notes using the finalized output values.
5. Run the analysis verification checks and a targeted consistency review of every changed thesis claim against its generated output. This is a verification of the changes, not permission to rebuild the whole thesis.
6. Update the review action register with `done`, `deferred`, or `not adopted` and a short rationale for each finding ID. Keep the review file as the original independent assessment.

## Out of scope for this plan

- Rechecking source-document extraction or revising the frozen panel.
- Re-estimating the thesis around a new design or expanding the research question.
- Treating a delayed market price as fresh by assumption or imputing a missing price without a documented decision.
- Changing conclusions solely to obtain statistical significance.
- Rebuilding the full thesis document during this review/planning task.

## Findings coverage map

- **Primary decisions and headline interpretation:** M1–M6, M10–M14, m32–m36.
- **Analysis pipeline and reproducibility:** M9–M10, m8–m15, m20, m25–m26, m37, m40.
- **Thesis consistency and presentation:** M7–M8, M11–M12, m1–m7, m16–m39, s1–s8.
- **Items not resolved by review alone:** Q1–Q11 remain author questions where intent, provenance, or exact environment cannot be inferred. Pixel-level figure verification and independent coefficient recomputation for R3/R4/R5/R7/R8 remain explicitly limited as recorded in the review.

---

**Implementation status:** First surgical patch set was committed at `0283469`; the follow-up patches are applied and recorded in [`implementation_log.md`](implementation_log.md). Selected analysis tables were regenerated and checked against the manifest; the analysis tests pass. The full thesis was built from `83aa36c` (162 pp, 0 errors; build log on the VM at `~/workspace/frontmatter_build/work_83aa36c/build4.log`). The `assemble_e.py` source is tracked at `src/thesis/generators/appendix_e/assemble_e.py`, and Appendix E generator synchronization is verified: regenerating the fragments and re-assembling reproduces the tracked `appendix_e.tex` exactly. The surgical P2 patches (0.709 sentence, App C caption, m2/m3 code, m14/m16/m21/m24/m31, s3, descriptives full-precision corrections, Table 10 overfull fix) are applied and recorded in the log; the full thesis was built as v33 from the patched tree (163 pp, 0 errors; build log at `~/workspace/frontmatter_build/work_v33c/build4.log`). s1 (wild-cluster bootstrap) and s2 (post slopes per robustness spec) are now also implemented and recorded in the log; the full thesis was built as v34 (163 pp, 0 errors; build log at `~/workspace/frontmatter_build/work_v34/build4.log`). m20/s5 (Within-R² formula in Ch 3) is implemented; v35 built (164 pp, 0 errors). An independent final review v2 (`docs/thesis_review/v2/final_review.md`) found 1 Major (F-S1: M2 bootstrap p-value) + 8 Minor + 2 Suggestion items; all are fixed and recorded in the log, and the full thesis was built as v36 (164 pp, 0 errors; build log at `~/workspace/frontmatter_build/work_v36/build4.log`). Remaining open items are author questions only: Q4 (VIF convention), the m29 proposal wording (proposal is read-only), and figure-pixel verification.
