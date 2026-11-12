# Independent Review of the Data Analysis

**Thesis:** *Value Relevance of Accounting Information Before and After the Banking
Consolidation Wave: Evidence from Nepalese Commercial Banks* (Ohlson framework;
5 bank series x 6 fiscal years 2076/77-2081/82; analysis sample N = 28 bank-years).

**Reviewed state:** repository `verbose-chainsaw`, HEAD `6772ce6` ("polish thesis",
2026-11-05) **plus the uncommitted working tree** (staged v30 merge; unstaged v31/v32
edits; one untracked file `docs/thesis_supervisor/ohlson-value-relevance-pivot-2026-10-27.md`).
Reviewed **2026-11-12**. `origin/main` (`c2e58c6`, 2 commits ahead) was **not** pulled and
**not** reviewed. Nothing in this review changes, renames, deletes, or reformats any
thesis, code, data, or config file. The only file created by this review is this document.

**Reviewer note on method.** This review was produced by a coordinator plus 12 parallel
subagent researchers (11 method clusters + 1 dedicated recomputation agent), and every
load-bearing claim in it was then independently re-checked by the coordinator by reading
the thesis/code and by recomputing from the frozen panel CSV (see §9). One conflation in
the consolidated subagent report was caught and corrected during that re-check (see M3).
Status labels used throughout: **VERIFIED** (how it was checked is stated),
**INFERRED** (the basis is stated), **UNVERIFIED / CANNOT DETERMINE** (the reason is stated).

---

## 1. Scope, assumptions, ground rules

- **Scope.** Whether the thesis's *data analysis* is correct: methods, procedures,
  assumptions, implementation, reporting, and conclusions, judged against the thesis's own
  hypotheses and core objectives.
- **Extracted data treated as ground truth.** The extraction pipeline, the source register,
  the 30-row accounting panel, the DPS file, and the price series were **not** audited.
  Every recomputation in this review starts from the frozen panel
  (`data_analysis/data_extract/output/manual_review/mps_rd_joined_panel.csv`, 30 rows)
  exactly as the analysis code receives it. A wrong number in this review therefore means
  "wrong given the extracted data", not "wrong in the world".
- **Academic level / field.** Stated in the thesis itself, not assumed: a master's
  dissertation (MBS), Tribhuvan University Faculty of Management, governed by the FOM 2019
  thesis format guidelines with APA 6th referencing. Field: accounting value relevance
  (Ohlson residual-income valuation), Nepalese commercial banks, the 2023 consolidation wave.
- **Read-only.** No thesis, code, data, or config file was modified, renamed, deleted, or
  reformatted by any agent in this review. All recomputation ran in scratch outside the
  repository (`~/workspace/review-scratch/`, `~/workspace/review-venv/`, `/tmp`). `git status`
  was checked before and after writing this file; the only change attributable to the
  review is this file (see §9).
- **No hallucination rule applied.** Every claim about the thesis or the code cites its
  location (file path + section / line / table / figure). Every claim about a
  method, library, or standard comes from a source actually opened during the task
  (§9 lists them, with a provenance note) or from the review's own recomputation.
  Nothing in this document is written from memory.
- **Calibration.** A method that is valid in itself but does not answer the stated objective
  is recorded as a finding. No problem is invented; no real problem is hidden. There are
  **no Critical findings** (nothing found invalidates or reverses a reported number), but
  there are 14 Major findings that materially weaken what the headline conclusions can
  claim. The distinction matters and is kept throughout.

## 2. Understanding of the thesis

Locations are in the working-tree `.tex` files under `src/thesis/`.

### 2.1 Objectives, questions, hypotheses

- **Objectives** (Ch 1, `chapter_01_introduction.tex`, objectives list): (1) test the
  baseline value relevance of EPS and BVPS for MPS_RD; (2) test whether the
  EPS/BVPS-price relationship shifted after consolidation; (3) evaluate robustness and
  stability across alternative specifications (ROA substitution, DPS inclusion, dropping
  the FY 2079/80 transition year, dropping FY 2078/79 for entity-timing mismatch,
  bonus-adjusted BVPS, restated EPS). **Gap in the objectives as written:** the list has
  no bullet for R9 (dropping the single Kanchan-mismatched bank-year NMB FY 2076/77),
  although R9 is estimated and reported (finding m28).
- **Research questions** (Ch 1 / Ch 5): RQ1 — are EPS and BVPS significantly associated
  with MPS_RD in the baseline model? RQ2 — did the EPS/BVPS slopes shift after
  consolidation? RQ3 — are the inferences robust to specification choice?
- **Hypotheses** (Ch 1, hypotheses section; tested in Ch 4). All are tested **two-tailed
  at 5%** without directional signs, as the thesis states, even though Ohlson theory
  predicts positive slopes. Null / alternative pairs:
  - H1: EPS has no association with MPS_RD (H1_0: beta_E = 0) vs. H1_1: beta_E != 0.
  - H2: BVPS has no association with MPS_RD (H2_0: beta_B = 0) vs. H2_1: beta_B != 0.
  - H3: the EPS slope did not shift post-consolidation (H3_0: delta_E = 0).
  - H4: the BVPS slope did not shift post-consolidation (H4_0: delta_B = 0).
  - Joint test: H0: delta_E = delta_B = 0 (right-tail Wald F).
- **Variables.** Dependent: MPS_RD, closing price on the first trading session after the
  BAFIA reporting deadline with a valid trade, missing if suspended / no valid price
  within a 5-day window. Regressors: EPS, BVPS (own-current values; restated EPS only in
  R8), ROA (R3 substitute), DPS (R4 additive), Post_t (1 for FY 2079/80-2081/82).
  Fixed effects: bank (5 series) and fiscal year (6 years).
- **Unit of analysis / design / sample.** Bank-year panel, 5 banks x 6 FYs = 30 rows;
  analysis sample **N = 28** (13 pre, 15 post) after excluding HBL FY 2077/78 (gap 54 days)
  and NIMB FY 2077/78 (gap 47 days) under the 5-day freshness rule. Design: two-way
  fixed-effects OLS estimated by LSDV (dummy variables), MacKinnon-White HC3 robust
  standard errors, t(df) reference distributions, joint Wald F for the regime shift,
  Pearson correlations, VIF, Breusch-Pagan, Cook's distance, Q-Q normality plots, and a
  nine-specification robustness suite R1-R9.
- **Claimed conclusions** (Ch 5, `chapter_05_summary_and_conclusion.tex`): baseline null
  result — H1-H4 and the joint test all fail to reject at 5% (joint Wald F(2,14) = 2.954,
  p = 0.085); point estimates compress post-consolidation; the R6 exception (joint Wald
  F(2,10) = 5.818, p = 0.021) makes the regime-shift evidence "sensitivity-dependent,
  not conclusive"; descriptives show mean price -33.80%, mean EPS -40.11%, cash DPS
  -76.90%, BVPS +2.44%; no flight to book value (post BVPS slope -1.658); n = 28 / df = 14
  means "not demonstrated", not "proven zero"; non-causal framing throughout. The
  "Fail to Reject" language is used uniformly; the thesis never says "accept H0" or
  "prove no effect". That discipline is real and is recorded in §6 — but several
  narrative sentences around it overreach the estimates (M2, m32, m36).

## 3. Traceability matrix and coverage inventory

### 3.1 Traceability matrix

| Objective / RQ | Hypothesis | Variables | Method | Code location | Reported result | Conclusion in thesis |
|---|---|---|---|---|---|---|
| RQ1 baseline relevance | H1 (EPS), H2 (BVPS) | MPS_RD, EPS, BVPS | Model 1 two-way FE OLS + HC3, t(16) | `data_analysis/analysis/stats/models.py` `fit_model1`; asset `t3_model1.py` | Ch 4 Table 5; App E Table 19: EPS 2.095 (SE 4.096, p 0.616), BVPS 0.219 (SE 1.858, p 0.908) | Fail to reject H1, H2 |
| RQ2 regime shift | H3 (delta_E), H4 (delta_B), joint | EPS, BVPS, EPS x Post, BVPS x Post | Model 2 two-way FE OLS + HC3, t(14); joint Wald F | `stats/models.py` `fit_model2`; `stats/wald.py` `joint_zero_test`; asset `t4_model2.py` | Ch 4 Table 6; App E Table 20: delta_E -3.124 (p 0.448), delta_B -1.758 (p 0.175); Wald F(2,14) = 2.954, p = 0.085; post EPS 2.453 (p 0.298), post BVPS -1.658 (p 0.161) | Fail to reject H3, H4, joint at 5% |
| RQ3 robustness | — (same H3/H4/joint per spec) | as M2, plus ROA / DPS / BVPS_adj / restated EPS | R1-R9 suite, same estimator | `stats/robustness.py` `build_runs`; asset `t5_robustness.py` | Ch 4 Table 8; App E Tables 22-26: only R6 rejects (F = 5.818, p = 0.021) | "Sensitivity-dependent, not conclusive" |
| Descriptives | — | MPS_RD, EPS, BVPS, DPS, ROA | Means / SDs / % changes, full vs pre vs post | asset `t1_descriptives.py` | Ch 4 Table 3 (45 cells) | Price -33.80%, EPS -40.11%, DPS -76.90%, BVPS +2.44% |
| Correlations | — | MPS_RD, EPS, BVPS, ROA, DPS | Pearson r, two-tailed p | asset `t2_correlations.py` | Ch 4 Table 4 (10 pairs) | EPS-ROA r = 0.975; MPS-EPS r = 0.358 (p 0.061) |
| Diagnostics | — | residuals, regressors | VIF (slopes only), Breusch-Pagan, Cook's D 4/n, Q-Q plots | `stats/diagnostics.py` (`vif_table`, `breusch_pagan`, `cooks_distance`); asset `t6_diagnostics.py` | Ch 4 Table 9; App E Tables 27-30 | "Passed" (but see M6, M7, M8, M10) |
| Specification comparison | — | MPS_RD, EPS, BVPS | Pooled OLS vs bank-FE vs two-way FE, raw R^2 | asset `a5_specification_comparison.py` | Ch 4 Table 10 | R^2 0.136 -> 0.948 (see M11, M12) |
| Price design | — | MPS_RD | 5-day freshness rule, gap <= 5 | `analysis/dataset.py` (`price_rd = price.where(gap <= 5)`); config `price_freshness_days: 5` | Ch 4 Table 2; App A Table 12 | N = 28 clean; 2 delayed rows missing (see M4, M5, M14) |

### 3.2 Coverage inventory — what was reviewed, and what was not

- **Reviewed in full:** every tabulated analysis result (Tables 3-10, App E Tables 19-30
  values as recomputed; see §9 for the 383-value programmatic check and the per-cluster
  recomputations), every method in §4, the freshness-rule implementation, the robustness
  suite logic, the test suite, and the generated table outputs.
- **Reviewed at generator level only:** Figures F1-F6 and A1-A3. Their generator scripts
  (`data_analysis/analysis/assets/f1_*.py` … `f6_*.py`, `a1_*.py` … `a3_*.py`) read the
  same fitted/panel objects whose numbers were recomputed (spot-checked: `f4_coefficient_forest.py`
  builds its forest from `fit_model2` + `t_test` combos; `a2_robustness_forest.py` builds
  its forest from `build_runs`, including R9; `f6_trends.py` plots the panel). **The
  rendered PDF figures were not re-extracted pixel by pixel and matched to the tables.**
  Status: **UNVERIFIED** at pixel level; no discrepancy is alleged. Reason: no
  figure-value extraction was performed; the generator-level trace is the evidence.
- **NOT REVIEWED by design:** the extraction pipeline and its outputs (ground truth per
  §1); Chapter 2 literature/theory except where it makes methodological claims
  (P/E circularity proof, BAFIA operationalisation, the §2.5 robustness-count sentence);
  front matter; bibliography content.
- **NOT REVIEWED (outside the dedicated recomputation's scope):** the R3/R4/R5/R7/R8
  *coefficients* were not independently recomputed by the dedicated agent; their Wald
  F/p values **were** reproduced exactly by cluster (c) running the repository's own
  statsmodels 0.14.4 code. Status: coefficients **UNVERIFIED** by independent
  recomputation (no error alleged; the code path is the same `build_runs` used for the
  verified specs).

---

## 4. Method-by-method review

Exactly one verdict per method. Severity: **Critical** = invalidates or could reverse a
reported conclusion; **Major** = materially weakens validity or reliability;
**Minor** = does not change conclusions; **Suggestion** = optional improvement.

### (a) Two-way fixed-effects OLS via LSDV vs within-demeaning — **Correct with caveats**

- **What is done and where.** Models 1-2 are estimated by OLS with explicit bank and
  fiscal-year dummies (`C(bank) + C(fy)`), i.e. the least-squares dummy-variable (LSDV)
  estimator: `data_analysis/analysis/stats/models.py`, `fit_model1` / `fit_model2`
  (`smf.ols(...).fit(cov_type="HC3", use_t=True)`). References GBIME and FY 2076/77.
- **Why used.** Two-way FE removes time-invariant bank heterogeneity and common
  year shocks, so slopes are identified from within-bank, within-year variation.
- **Evidence (VERIFIED).** Independent numpy recomputation (QR-based OLS) reproduces
  LSDV slopes exactly; the within (demeaned) estimator gives identical slopes to 4 dp.
  The dummy trap is correctly avoided (design ranks 12/14; a full dummy set is
  rank-deficient by exactly 2). `Post` is exactly collinear with the year dummies (rank
  stays 14 with Post added), so no Post main effect is estimable — correctly omitted.
  Thin identifying variation for delta (15 post observations) is a caveat, not an error.
- **Issues.**
  - **m1 (Minor, VERIFIED).** Model 2 post-year dummies / intercept are evaluated at
    EPS = BVPS = 0, far outside the data; the Appendix E gloss invites misreading
    (+64/+141/+159 vs M1 -262/-199/-199). Location: App E full Model 2 table and its
    note. Impact: presentation only; no coefficient affected.
  - **m2 (Minor, VERIFIED).** The reference category is implicit in code (`C(bank)` /
    `C(fy)` bare, patsy default) rather than stated. No conclusion at risk.
  - **m3 (Minor, VERIFIED).** Model formulas name `price`, not `price_rd` — latent only;
    all callers pass the filtered panel (`dataset.py`). No number affected.
  - **m4 (Minor, VERIFIED).** "Strictly within-year cross-sectional variation"
    (Ch 3; Ch 4 §4.2.7, line 596) overstates one side of the identification. Wording only.
- **Sources consulted.** Review-team sources: Wooldridge Ch 14 (via notes pages);
  Stata `xtreg` documentation and Statalist threads on within-R^2 (see §9 provenance note).

### (b) HC3 robust standard errors, t(df), small-sample behaviour; why not cluster-robust (G = 5) — **Correct with caveats**

- **What is done and where.** `models.py:60`, `cov_type="HC3"`, `use_t=True`. HC3 is the
  conservative heteroskedasticity-robust choice; no clustering (G = 5 banks).
- **Why used.** Heteroskedasticity-robust inference with a finite-sample correction;
  cluster-robust SEs with 5 clusters are severely downward-biased.
- **Evidence (VERIFIED).** Independent numpy HC3 reproduces Tables 5-6 exactly (see §9).
  HC3 is decisive for the headline: under HC0 the M2 Wald p = 0.0007, HC1 p = 0.011,
  **HC3 p = 0.085** — the null results are *produced by* the HC3 choice. Not clustering
  with G = 5 is decisively correct: bank-clustered CR1 SEs are far smaller (EPS 1.844 vs
  3.560), Wald p = 0.008 — clustering would manufacture significance. Leverage is
  extreme: h 0.357-0.932, mean 0.50, max HBL FY 2076/77 (HC3 weight ~216x).
  t(df) is conservative vs the normal approximation (Wald chi^2 approx p = 0.052 vs
  F p = 0.085).
- **Issues.**
  - **m5 (Minor, VERIFIED).** "Reliable finite-sample inference" / "protection" is
    overclaimed for HC3 (Ch 1:176; Ch 3). HC3 corrects the variance estimate; it does
    not make df = 14 inference reliable in general.
  - **m6 (Minor, INFERRED).** Within-bank error independence is assumed, never
    stated or tested (residual lag-1 correlation -0.30, weak evidence either way).
    Basis: no autocorrelation diagnostic exists in `stats/diagnostics.py` or Ch 3.
  - **m7 (Minor, VERIFIED).** "Huber-White cluster SEs" (Ch 3) conflates two different
    estimators. Wording only.
  - **m40 (Minor, VERIFIED).** statsmodels is unpinned (`>= 0.14` in `requirements.txt`;
    App D §D.6 records no exact version). The recomputation was run under 0.14.4
    (cluster c, repo code) and 0.15.0 (coordinator, numpy cross-check) with identical
    results, so this is a reproducibility gap, not a numeric error.
  - **s1 (Suggestion).** A wild-cluster-bootstrap sensitivity would be a useful
    small-sample check at G = 5. Not required for the verdict.
- **Sources consulted.** Review-team sources: MacKinnon & White (1985); Long & Ervin
  (2000); MacKinnon (2013); Cameron & Miller (2015); Cameron, Gelbach & Miller (2008);
  statsmodels documentation (0.14.0 / 0.14.4 / 0.15.0). See §9 provenance note.

### (c) Joint Wald F under robust covariance — **Correct with caveats**

- **What is done and where.** H0: delta_E = delta_B = 0 tested with `results.f_test`
  under the HC3 covariance: `data_analysis/analysis/stats/wald.py`, `joint_zero_test`.
  Reported in Ch 4 Tables 6/7/8, App E, Ch 5, consistently.
- **Why used.** It is the right test for the joint regime-shift hypothesis; the
  individual t-tests cannot answer it.
- **Evidence (VERIFIED).** Verified three ways: independent numpy Wald computation;
  the dedicated agent's statsmodels 0.15.0 cross-check (max |statsmodels - numpy| =
  6.3e-11); and cluster (c) running the repository's own statsmodels 0.14.4 code
  (`build_runs` + `joint_zero_test`). All 8 Wald F/p/df reproduce exactly: R2 2.954/0.085,
  R3 2.463/0.121, R4 2.767/0.100, R5 2.414/0.139, **R6 5.818/0.021**, R7 2.365/0.130,
  R8 2.915/0.087, R9 1.794/0.205. Star convention correct (M2 unstarred, R6 starred);
  consistent across Tables 6/7/8, App E, Ch 5. Classical (non-robust) Wald F for M2 =
  9.573, p = 0.0024 — would reject; HC3 is decisive here as in (b).
- **Issues.**
  - **m8 (Minor, VERIFIED).** A generated Table 4 note mislabels the Wald "two-tailed";
    the thesis text correctly says right-tail (Ch 4 Table 6 note, line 275).
    Generated artefact only.
  - **m9 (Minor, VERIFIED).** Generated Table 5 outputs are stale and omit R9:
    `data_analysis/analysis/outputs/tables/T5_robustness.{tex,md}` contain 0 occurrences
    of "R9" (checked 2026-11-12). The thesis Table 8 itself is current.
  - **m10 (Minor, VERIFIED).** Unit test `test_stats.py:72` (and :88-91) asserts run ids
    == R1..R8; `build_runs` now returns R1..R9, so the test fails on the working tree.
    Test maintenance only — running the suite in scratch gives 25 passed, 1 failed on
    exactly this assertion; no thesis number is affected.
  - **m11 (Minor, VERIFIED).** R4 p = 0.0997 prints as 0.100, on the 10% boundary.
    Rounding only; the value is reported as 0.100 in Table 8.
  - Multiplicity concerning this test family is **M13** (§5 / method (h)).
- **Sources consulted.** Review-team sources: statsmodels documentation (`f_test`,
  `OLSResults`, 0.13.5 / 0.14.4 / 0.15.0); Wooldridge Ch 6/14 (via notes pages).
  See §9 provenance note.

### (d) Pearson correlation + VIF — **Correct with caveats**

- **What is done and where.** Table 4 Pearson correlations (`assets/t2_correlations.py`);
  VIF on substantive regressors only, FE dummies excluded
  (`stats/diagnostics.py:25-34` `vif_table`; called only with `("eps", "bvps")` in
  `assets/t6_diagnostics.py:21` and in tests). Ch 3 screen: VIF > 5 or tolerance < 0.20.
- **Evidence (VERIFIED).** All 10 Table 4 correlations + stars reproduce (|Δr| ≤ 0.001);
  M1 VIF 1.16 exact; EPS-ROA r = 0.974656, bivariate VIF 19.98 ≈ 20 exact; M2 VIFs
  EPS 10.33, BVPS 2.28, delta_E 15.15, delta_B 24.13 exact (recomputed by coordinator
  2026-11-12, `~/workspace/review-scratch/verify_majors.py`).
- **Issues.**
  - **M10 (Major, VERIFIED).** Ch 3 (line 357) overgeneralises VIF ≈ 1.16 to "the
    estimated models": *"in the estimated models, substantive regressors exhibit VIF
    ≈ 1.16, well below diagnostic thresholds."* The 1.16 figure is the Model 1
    slopes-only VIF. Model 2 VIFs breach the Ch 3 screen (5) on 3 of 4 slopes (10.33 /
    15.15 / 24.13). Appendix E discloses the M2 VIFs and explains them as mechanical,
    resting inference on the joint Wald test — so the thesis contains both the
    overgeneralisation and its correction, in different places. Impact: misleading
    summary in the methodology chapter; no conclusion changes, because the M2
    inference never rested on the VIF screen.
  - **m12 (Minor, VERIFIED).** The pipeline note says "variance inflation ~ 30"
    (`assets/t2_correlations.py:55-57` and the generated T2 table). Wrong: 1/(1-0.97^2)
    = 16.9; VIF 30 would need r = 0.9832. The thesis text correctly says ~20.
    Pipeline artefact only.
  - **m13 (Minor, VERIFIED).** Threshold inconsistent: screen at 5 in Ch 3 vs "Passed"
    at 10 in Ch 4 Table 9 (lines 478-480: VIF 1.16, cutoff < 10.0).
  - **m14 (Minor, VERIFIED).** Pearson p-values assume normality; that fails for MPS_RD
    (Shapiro p = 0.000, skew +1.45) and DPS (p = 0.001). EPS-BVPS r = 0.372, p = 0.051
    becomes Spearman rho = 0.295, p = 0.128. No starred conclusion turns on this.
  - **m15 (Minor, VERIFIED).** DPS-MPS p printed 0.678 (Ch 4, line 133) vs recomputed
    0.678979 → 0.679. Off by 0.001; cause undetermined; no conclusion change.
  - **Open question (not a finding).** Whether computing VIFs on slopes only, excluding
    FE dummies, is the right convention is **CANNOT DETERMINE** from the sources opened
    in this review (see §8, Q4). The thesis discloses the method (Ch 3; T6 note). For
    scale, with dummies included the auxiliary regressions give M1: EPS 5.7, BVPS 12.32;
    M2: EPS 14.82, BVPS 12.46, EPS x Post 27.34, BVPS x Post 259.32 (coordinator
    recomputation, 2026-11-12). The M2 VIFs have **no code path** in the repository:
    `vif_table` is called only for ("eps", "bvps") — the M2 values are hand-computed.
    That is a traceability gap (see also M9), not a numeric error: the values reproduce.
  - **s6 (Suggestion).** App E's "HC3 intervals already reflect [collinearity]" is
    loosely worded; HC3 intervals reflect sampling variance under heteroskedasticity,
    not collinearity as such.
- **Sources consulted.** Review-team sources: O'Brien (2007) on VIF; SciPy `pearsonr`
  documentation; statsmodels `variance_inflation_factor` documentation. See §9
  provenance note.

### (e) Breusch-Pagan; Cook's D 4/n, max D = 0.552; Q-Q normality — **Correct with caveats**

- **What is done and where.** `stats/diagnostics.py:47-48` `breusch_pagan`
  (`het_breuschpagan(resid, model.exog)` — no `robust=` argument); Cook's distance via
  `OLSInfluence(...).cooks_distance`, threshold 4/n = 0.143; Q-Q plots in App C / Ch 4
  Figure 5. Reported in Ch 4 Table 9 and App E Tables 27-30.
- **Evidence (VERIFIED).** BP (Koenker/default) M1 LM 14.3695, p = 0.2132, df = 11,
  chi^2_0.95 = 19.68 — matches Table 9; M2 LM 14.5430, p = 0.3367, df = 13 — matches
  App E. Cook's D exact: M1 max 0.5519 (HBL FY 2076/77, leverage 0.6766), 5 flagged;
  M2 max 0.4902 (KBL FY 2076/77), 5 flagged.
- **Issues.**
  - **M6 (Major, VERIFIED).** The reported Breusch-Pagan is the **Koenker/studentized
    variant, never named anywhere** in the thesis. The code passes no `robust=` argument
    and statsmodels' default is Koenker (`robust=True`): opened source, statsmodels
    0.15.0 documentation for `het_breuschpagan`
    (https://www.statsmodels.org/stable/generated/statsmodels.stats.diagnostic.het_breuschpagan.html —
    "Flag indicating whether to use the Koenker version of the test (default) …
    or the original Breusch-Pagan version which assumes residuals are normally
    distributed"). The variant matters: **classical BP on M1 rejects: LM 28.18,
    p = 0.003** (coordinator recomputation, 2026-11-12, statsmodels 0.15.0), reversing
    Table 9's "Passed" for M1 (M2 classical 17.12, p = 0.194, still fails to reject).
    The F-statistic agrees with fail-to-reject under either variant (p = 0.212 both),
    which is presumably why the discrepancy went unnoticed. Impact: Table 9's M1
    "Passed" is variant-dependent and undisclosed; the heteroskedasticity conclusion
    for M1 is not robust to the test variant. (HC3 inference itself does not depend on
    this test passing.)
  - **M7 (Major, VERIFIED).** "Mitigated via HC3" misstates influence handling
    (Ch 4 Table 9, line 484: Cook's Distance row, status "Mitigated via HC3"). HC3
    changes standard errors only; point estimates are untouched — deleting HBL FY 2076/77
    moves M2 EPS 5.577 → 6.787 and its SE 3.560 → 7.258. Genuine mitigation is the
    leave-one-out sensitivity in the App E note (deleting HBL FY 2076/77: delta_E -4.211,
    delta_B -1.674, Wald F = 1.917, p = 0.186). Same mislabelling pattern in Ch 1:176
    for heteroskedasticity is fine ("mitigates heteroskedasticity by deploying HC3");
    the error is specifically attaching HC3 to *influence*. Impact: wording error; the
    sensitivity analysis itself exists and is sound.
  - **M8 (Major, VERIFIED).** Normality is promised but never assessed in words. Ch 3:360
    lists "Normal Q-Q probability plots and residual standard deviation screening";
    "residual standard deviation screening" is defined nowhere (only occurrence in the
    thesis, confirmed by grep). Q-Q plots are presented (Ch 4 Figure 5 note, line 512)
    with no verdict. Supplementary Shapiro-Wilk (coordinator recomputation, scipy):
    M1 W = 0.9246, p = 0.045; M2 W = 0.9216, p = 0.038 — both reject normality at 5%.
    Impact: gap, no false claim; but the t/F reference distributions assume normal
    errors, so an unassessed failed assumption sits under every p-value. (HC3 does not
    cure non-normality.)
  - **m16 (Minor, VERIFIED).** R9 does not cover HBL FY 2076/77 (it drops NMB FY 2076/77);
    coverage of that point is only via leave-one-out ranges in a note.
  - **m17 (Minor, VERIFIED).** "Extreme price realizations / 2021 bull market" is wrong
    for 2 of the 5 Cook's-flagged points (KBL FY 2079/80 price 136.90 = sample minimum;
    KBL FY 2076/77 leverage below the mean, residual-driven).
  - **m18 (Minor, VERIFIED).** "Influential" is threshold-dependent: D > 1 flags 0 points
    in both models; 4/(n-K-1) flags 3 (M1) / 2 (M2), vs 5 each at 4/n.
  - **m19 (Minor, VERIFIED).** App E flagged table is out of descending order; Table 9
    "Passed" overstates non-rejection (failing to reject is not passing); the BP note
    says "across fitted values and regressors" but the code regresses on regressors
    only; M2 diagnostics appear only in App E.
- **Sources consulted.** statsmodels `het_breuschpagan` documentation 0.15.0 — **opened
  in full by the coordinator during this review** (see §9). Review-team sources:
  Breusch & Pagan (1979) and Koenker (1981) via documentation/secondary sources.
  See §9 provenance note.

### (f) Within-R^2 definition and interpretation — **Correct with caveats**

- **What is done and where.** Within-R^2 = 1 - SSR_LSDV / SSR_dummies-only, i.e. the
  share of bank-and-year-adjusted variation explained by the slopes. Reported in
  Tables 5/6 (M1 0.152, M2 0.642) and App E for R1-R9. Definition is verbal only
  (App E note; Ch 4 Table 5 note line 205, Table 6 note line 275); **no formula appears
  anywhere in the thesis** and Ch 3 defines no R^2 at all.
- **Evidence (VERIFIED).** The definition is mathematically correct: it equals the R^2
  of the Frisch-Waugh-Lovell within regression (proved by algebra, verified numerically
  by cluster (f)). All Within-R^2 values reproduce (M1 0.1518 vs 0.152; M2 0.6417 vs
  0.642; R1-R9 all within ±0.0005). Naive single-pass double-demeaning would give M2
  Within-R^2 0.504 (vs 0.642) and badly wrong interactions (delta_E -5.29 vs -3.12) —
  the thesis avoids it by using LSDV. Decomposition: dummies alone explain 93.9% of
  total variance; slopes add 0.93 pp (M1) / 3.9 pp (M2).
- **Issues.**
  - **M9 (Major, VERIFIED).** Within-R^2 is computed **nowhere in the analysis code**;
    all values are hand-entered, unguarded by any test. `FitResult` carries only LSDV
    R^2 / adj R^2. Evidence: grep for "within" across `data_analysis/analysis/stats/`
    and `assets/` returns only the freshness-window phrase in `t1_descriptives.py:59`.
    Impact: traceability risk, not a numeric error — the values reproduce, but there is
    no pipeline protection against a transcription error.
  - **m20 (Minor, VERIFIED).** No Within-R^2 formula anywhere; definition verbal only
    (App E:12); Ch 3 defines no R^2.
  - **m21 (Minor, VERIFIED).** Within-R^2 is never interpreted in prose (Ch 4: 4
    occurrences, all table rows/notes; Ch 5: 0). The 0.152 → 0.642 jump is unexplained.
  - **m22 (Minor, VERIFIED).** M2 adjusted R^2 (0.958) appears only in App E, not in
    Ch 4 Table 6.
  - **m23 (Minor, VERIFIED).** The pooled-vs-FE contrast (0.136 vs 0.948) is drawn on
    unadjusted R^2 without Within-R^2 alongside.
  - **m24 (Minor, VERIFIED).** R1-R9 fit statistics appear only in App E.
  - **s5 (Suggestion).** The bare "Within-R^2" label is ambiguous vs Stata's one-way
    within-R^2; a one-line definition in Ch 3 would fix it.
  - **Correction to the brief's premise (VERIFIED).** The thesis does **not** state the
    formula "1 - SSR_LSDV / SST of dummies-only residuals" and does **not** warn against
    naive two-way demeaning ("demeaning" occurs once, App D:316, about estimation;
    "naive" once, Ch 2:399, about clustered SEs). The review's account above uses the
    definition as actually written in the thesis.
- **Sources consulted.** Review-team sources: Stata `xtreg` documentation; Statalist
  threads on within-R^2; Wooldridge Ch 14 (via notes pages). See §9 provenance note.

### (g) Linear combinations for implied post slopes (beta + delta) and HC3 SEs — **Correct with caveats**

- **What is done and where.** Post slopes beta + delta with SEs via `results.t_test`
  on the HC3 covariance: `assets/t4_model2.py` `_combo` (also duplicated in
  `f4_coefficient_forest.py`; a third copy in `t5_robustness.py` is dead code). Reported
  in Ch 4 Table 6 and App E.
- **Evidence (VERIFIED).** Post slopes exact beta + delta; SEs correctly include the
  large negative Cov(beta, delta) (EPS: Cov -11.7769; ignoring it would inflate the EPS
  SE 2.4x, BVPS 1.6x); t(14) p-values exact; CIs match App E to 4 dp (EPS [-2.4124,
  7.3192]; BVPS [-4.0593, 0.7441]).
- **Issues.**
  - **M2 (part) (Major, VERIFIED).** "No flight to book value" is phrased as a finding
    from a non-significant point estimate: post BVPS -1.658 (p = 0.161) with CI admitting
    +0.74, i.e. 7x the pre slope (0.100). A CI that wide admits the opposite of the
    claim. See M2 in §5/§7 for the full narrative-overreach finding.
  - **m25 (Minor, VERIFIED).** The Table 6 note claims post-slope CIs "are reported in
    the text" but they appear nowhere in Ch 4 text (only in App E).
  - **m26 (Minor, VERIFIED).** The post-slope computation is untested, and `_combo` is
    duplicated across three files (one dead). Maintenance risk only.
  - **s2 (Suggestion).** The robustness suite never reports post slopes. The review's
    own recomputation: R5 post EPS 3.415 (p = 0.401), post BVPS -2.081 (p = 0.315);
    R6 post EPS 1.900 (p = 0.490), post BVPS -1.809 (p = 0.212) — same signs, still
    insignificant, even though R6's joint Wald rejects. Reporting them would have made
    the R6 discussion more complete.
- **Sources consulted.** Review-team sources: statsmodels `t_test` documentation;
  Brambor, Clark & Golder (2006) on interaction interpretation. See §9 provenance note.

### (h) Robustness suite logic R1-R9; multiple testing — **Correct with caveats**

- **What is done and where.** Nine specifications: R1 = Model 1, R2 = Model 2, R3 = ROA
  for EPS, R4 = Model 2 + DPS (df 13), R5 = drop FY 2079/80 (df 10), R6 = drop FY 2078/79
  (df 10), R7 = bonus-adjusted BVPS, R8 = restated EPS, R9 = Model 2 dropping only NMB
  FY 2076/77 (n = 27, df = 13). `stats/robustness.py` `build_runs`; Ch 4 Table 8;
  App E Tables 22-26.
- **Evidence (VERIFIED).** All 9 specs are implemented exactly as described; all
  reproduce exactly (max diff 0.0000 at printed precision, cluster (h) + cluster (c)
  Wald reproduction). The suite is pre-specified in the committed proposal
  (`07_methodology`, lines 65, 68, 188-194), including R9 — not post-hoc. Sign stability
  is real (delta_E, delta_B negative in all 8 M2 specs). The conclusion
  "sensitivity-dependent rather than conclusive" is the right sentence.
- **Issues.**
  - **M3 (Major, VERIFIED — with a correction to the consolidated subagent report).**
    R6 is presented as a "Key Sensitivity Finding" without its fragility. The fragility
    case, correctly stated, is: (i) R6 is the **only** rejection among 8 joint Wald
    tests (see M13); (ii) F = 5.818 vs the 5% critical value 4.103 — only a 29.5% fall
    erases significance; (iii) neither interaction is individually significant in R6
    (delta_B p = 0.116, delta_E p = 0.620 — Ch 4 §4.2.6's statement of this is correct);
    (iv) R5, at the same N/df, gives F = 2.41, p = 0.139. **Correction:** the
    consolidated subagent report attributed to R6 a leave-one-out result ("only 1 of 28
    single-row deletions brings the joint Wald p < 0.05; range 0.035-0.291") that in
    fact belongs to the **baseline** M2, not to R6. The coordinator re-ran both
    leave-one-out exercises (2026-11-12, `~/workspace/review-scratch/verify_majors.py`):
    baseline M2 — exactly 1 of 28 deletions below 0.05 (NIMB FY 2078/79, p = 0.035;
    range 0.035-0.291; KBL FY 2077/78 p = 0.291); R6's own sample — 16 of 23 deletions
    below 0.05 (range 0.013-0.634). So R6's rejection is *not* single-observation
    fragile within its own sample; the baseline is one observation away from
    significance, which is a different (and also important) fragility. Impact: the
    single rejection in the suite cannot carry the weight the text gives it; the
    "Key Sensitivity Finding" framing needs the multiplicity and margin qualifications.
  - **M13 (Major, VERIFIED).** Multiplicity is never mentioned anywhere in the thesis
    (grep over `src/thesis/` for bonferroni | holm | fdr | family-wise | multiple
    testing | multiple comparison: **no matches**). Eight joint Wald tests are run and
    only R6 rejects; under independence P(>= 1 false rejection) = 1 - 0.95^8 ≈ 34%;
    Bonferroni threshold 0.00625; Bonferroni/Holm-adjusted R6 p = 0.168. Impact: the R6
    rejection reads as stronger evidence than the family of tests supports.
  - **m27 (Minor, VERIFIED).** Ch 2 line 401 says "eight robustness checks"; the suite
    is nine (7 variants + 2 baselines = 9 specs). Already wrong at HEAD. Ch 4 line 447
    ("eight robustness specifications (R1, R2, and R4 through R9)") is **correct** — the
    forest plot genuinely shows eight specs (R3 omitted, ROA scale) — and must not be
    changed. This finding is recorded here regardless of the pending one-word-fix
    decision for the Ch 2 line.
  - **m28 (Minor, VERIFIED).** Ch 1 objectives omit the R9 bullet (see §2.1).
  - **m29 (Minor, VERIFIED).** The proposal says ROA/DPS in "Models 1 and 2" but they
    are implemented only as Model-2 variants (R3, R4).
  - **m30 (Minor, VERIFIED).** R6 drops the whole FY 2078/79 including 1 non-mismatched
    row; dropping only the 4 mismatched rows gives numerically identical results (the
    year dummy absorbs the singleton). No number affected.
  - **m31 (Minor, INFERRED).** R8's per-row cause attribution ("bonus issues") is
    unsourced in the thesis. Basis: no source is cited for that attribution in the
    R8 note or text.
  - **s3 (Suggestion).** R4 DPS is additive-only with no stated reason (interacted
    variant, review recomputation: Wald F = 2.848, p = 0.097 vs R4 2.767/0.100).
  - **s4 (Suggestion).** R^2 is not comparable across different n (R6 R^2 = 0.992 vs
    R2 0.978 is partly mechanical).
- **Sources consulted.** Review-team sources: standard multiple-testing references
  (Bonferroni / Holm / BH) via textbook and notes sources; the in-repo proposal file.
  See §9 provenance note.

### (i) Power / sample-size adequacy (N = 28, df = 14/10/13) — **Correct with caveats**

- **What is done and where.** Nothing formal. The thesis discloses df exactly everywhere
  (M1 df 16, M2 df 14, R4/R9 df 13, R5/R6 df 10) and uses "not demonstrated, not proven
  zero" language — but no power or minimum-detectable-effect (MDE) analysis exists
  anywhere. The word "power" in the statistical sense occurs **zero times** (grep:
  "statistical power" 0 occurrences across all chapters and appendices).
- **Evidence (VERIFIED by the coordinator's own computation, 2026-11-12, scipy
  noncentral t).** Single-coefficient MDE at 80% power, two-sided alpha = 0.05, is
  d ≈ 3.0 SEs (df 14: 3.01; df 10: 3.11). Raw MDEs: beta_E (M2) 10.73 NPR vs estimate
  5.58; delta_E 12.06 vs -3.12; delta_B 3.71 vs -1.76; post EPS 6.84; post BVPS 3.37.
  Joint Wald MDE lambda = 12.03 (F(2,14)), 13.21 (F(2,10)); even Cohen's "large"
  f^2 = 0.35 has power only 0.46-0.71 (convention-dependent).
- **Issues.**
  - **M1 (Major, VERIFIED).** No power / MDE analysis anywhere, although the headline
    findings are nulls. Every fail-to-reject is consistent with both "no effect" and
    "substantial effect" (e.g. delta_E MDE 12.06 NPR is ~4x the estimated -3.12).
    Impact: limits what the null results can claim; does not change any number.
  - **M2 (Major, VERIFIED).** The "earnings dominate book value" narrative is built on
    insignificant point estimates: beta_E CI [-2.06, 13.21] (5.577 ± t(14, 0.975) 2.145
    x 3.560); beta_B CI ≈ [-2.70, 2.90] includes large values. Same issue for "no
    flight to book value" (method (g)) and the unqualified Ch 5 regime-change
    statements (m32). Impact: narrative overreach; the estimates themselves are correct.
  - **m32 (Minor, VERIFIED).** Unqualified point-estimate regime-change statements in
    Ch 5 (e.g. the compression narrative stated without CIs). Wording only.
  - **m33 (Minor, INFERRED).** Effective N < 28 (G = 5 clusters; HC3 not cluster-robust),
    so the power numbers above are optimistic upper bounds. Basis: design structure,
    not a computed quantity.
  - Null-result language itself is disciplined ("Fail to Reject" uniform; no "accept
    H0" / "prove no effect") — recorded as a strength in §6.
- **Sources consulted.** Review-team sources: statsmodels `FTestPower` documentation;
  Hoenig & Heisey (2001); Wasserstein & Lazar (2016) ASA statement; Sterne et al.
  (2009) BMJ. See §9 provenance note.

### (j) MPS_RD 5-day freshness rule; missing-data mechanism; look-ahead — **Correct with caveats**

- **What is done and where.** Protocol: price on the first trading session after the
  BAFIA reporting deadline with a valid trade; missing if suspended / no valid price
  within a 5-day window. Implemented exactly as written (`dataset.py:137-138`,
  `gap <= 5`, config `price_freshness_days: 5`); prices only after the deadline; stale
  prices never imputed; verification limits disclosed candidly (App A note, App D §D.8).
- **Evidence (VERIFIED).** Protocol direction is right. Realised gaps in the 30-row panel
  are only 0, 2, 47, 54 days (coordinator check of the panel CSV, 2026-11-12), so **any
  window 2-46 days yields identical N = 28**. The two excluded rows are HBL FY 2077/78
  (gap 54, price 358.90) and NIMB FY 2077/78 (gap 47, price 367.70).
- **Issues.**
  - **M14 (Major, VERIFIED).** The 5-day length is never justified anywhere in the
    thesis. Because realised gaps are 0/2 vs 47/54, the operative choice is not the
    window length at all — it is the binary exclude/include decision for the 47/54-day
    rows, and that decision is undefended. Impact: the protocol's operative choice has
    no stated basis.
  - **M4 (Major, VERIFIED by the coordinator's own recomputation).** No sensitivity
    analysis for the two exclusions exists — and the headline baseline decision flips
    if they are re-included: **N = 30: Wald F(2,16) = 4.762, p = 0.024** (significant
    at 5%); stale-price carry-forward F = 3.870, p = 0.043. (Recomputed 2026-11-12 from
    the panel CSV with an independent LSDV + HC3 implementation; baseline N = 28
    reproduced first as F = 2.954, p = 0.085.) The thesis hedging softens this, but the
    formal Ch 5 "Fail to Reject" would reverse under this one sensitivity. Impact: the
    headline conclusion is knife-edge on the exclusion decision. This is the single
    most consequential finding in the review, because unlike the other Majors it moves
    a reported conclusion.
  - **M5 (Major, VERIFIED in its checkable parts; mechanism INFERRED).** Missingness is
    plausibly MNAR and never characterised. Checkable parts, verified from the panel
    CSV: both excluded rows are parties to the same failed HBL-NIB merger, and the
    missing rows are extreme on observed X — HBL FY 2077/78 EPS 28.07 is the highest
    EPS in the full 30-row panel; NIMB FY 2077/78 BVPS 198.28 is the highest BVPS in
    the full panel. (The MOU date 13 May 2021 and the 335-day suspension lead are as
    reported by the review team from the thesis's own suspension evidence; the thesis
    never names the missingness mechanism or a bias direction.) Direction, computed:
    exclusion attenuates the pre BVPS slope (0.100 vs 0.709 when included) and weakens
    joint evidence (p = 0.085 vs 0.024) — i.e. conservative in that direction, but
    unstated. Impact: unstated threat to validity; the direction happens to be
    conservative.
  - **m34 (Minor, VERIFIED).** Actual publication dates are verified for only 2 of 30
    bank-years; this is not stated in one place in Ch 3.
  - **m35 (Minor, VERIFIED).** "Eliminates look-ahead bias" overstates: prices are
    measured 3-6 months after disclosure; post-disclosure news is embedded; year FE
    absorb only common moves.
  - **s7 (Suggestion).** Ch 4 Table 2 note says "5-day trading window" vs "calendar"
    elsewhere; "following the deadline" vs the gap-0 realisation needs half a sentence.
- **Sources consulted.** Review-team sources: MacKinlay (1997); Scholes & Williams
  (1977) / Dimson (1979); Madura et al. (2006) on thin trading / staleness. See §9
  provenance note.

### (k) Descriptives + pooled-OLS vs FE specification comparison — **Correct with caveats**

- **What is done and where.** Table 3 descriptives (`assets/t1_descriptives.py`); Table 10
  specification comparison (`assets/a5_specification_comparison.py`): pooled OLS, bank-FE,
  two-way FE.
- **Evidence (VERIFIED).** All 45 Table 3 cells and all 7 % changes reproduce exactly
  (both from printed App B values and full-precision CSV); 12/15 zero-DPS count verified;
  all `tab:spec_comp` coefficients / SEs / R^2 / df replicate to 3 dp. Year-FE-only fit,
  independently computed by the coordinator (2026-11-12): beta_E = 2.185 (SE 1.260,
  p = 0.098), beta_B = 0.555 (p = 0.420), R^2 = 0.919, adj 0.891, Within-R^2 0.296,
  df = 20 — matching the review team's computation exactly.
- **Issues.**
  - **M11 (Major, VERIFIED).** The specification comparison headlines raw LSDV R^2
    (0.136 → 0.948) as the specification demonstration, with no adjusted R^2, no
    Within-R^2, and no F-test of the FEs in §4.2.7 / Ch 5 — although the correct tests
    exist in App E (year FE F = 17.03, p < 0.001; bank FE F = 1.395, p = 0.280;
    coordinator's classical F(9,16) = 27.80, p < 0.001). Ch 4:544 states the 0.136 →
    0.948 jump without any adjusted or within figure alongside. (Adjusted R^2 does
    appear in Tables 5/6 themselves; the gap is in the *comparison* as presented.)
    Impact: overstates the specification demonstration in the main text.
  - **M12 (Major, VERIFIED by the coordinator's own fit).** The year-FE-only row is
    omitted: year dummies alone give R^2 = 0.919; bank FE add only 0.029 and are jointly
    insignificant given year FE (F(4,16) = 2.23, p = 0.112). Impact: the "fixed effects
    matter" story is really a "year effects matter" story, and the thesis never shows it.
  - **m36 (Minor, VERIFIED).** Ch 5 RQ1 sentence is backwards (line 115): "Omitted
    macro-year price shocks account for the high explanatory power reported in static
    pooled studies." Pooled R^2 is low (0.136); high R^2 appears only when year FE are
    *included*.
  - **m4 (Minor, VERIFIED).** "Strictly within-year cross-sectional variation" is
    imprecise (same wording issue as method (a)).
  - **m37 (Minor, VERIFIED as a discrepancy; cause UNVERIFIED).** Pooled EPS p printed
    0.126 (Ch 4:544, 596) vs recomputed 0.128 (t = 1.58 both). Cause undetermined.
  - **m38 (Minor, VERIFIED).** Descriptives method undocumented (sample SD ddof = 1;
    %-change formula unstated).
  - **m39 (Minor, VERIFIED).** Selective dispersion reporting: SD % changes only for
    MPS/EPS; BVPS -15.29%, DPS -16.57%, ROA +100% omitted; CVs show EPS 22.3% → 60.9%,
    ROA 16.8% → 62.9%, DPS 58.7% → 212.1%.
  - **s8 (Suggestion).** DPS-post median is 0 (mean 1.40 misleading); "halved" for
    -46.56% is loose; the spec-table "Assessment" column is editorial.
  - **Correction to the brief's premise (VERIFIED).** The brief's premise that the
    year-FE-only fit "was computed but NOT added" is **not supported**: no trace of it
    exists in code, tests, outputs, or text. The fit in this review is new
    (coordinator computation above), not a recovery of omitted work.
- **Sources consulted.** Review-team sources: Gelman, Hill & Yajima (2012). See §9
  provenance note.

---

## 5. Cross-cutting issues

1. **The numbers reproduce everywhere they were checked.** Independent numpy
   implementations across 11 clusters plus the dedicated agent; cluster (c) ran the
   repository's own statsmodels 0.14.4 code and reproduced all Wald values; the
   coordinator re-ran the headline numbers under statsmodels 0.15.0. 383 values checked
   programmatically by the dedicated agent — zero exceedances at the stated tolerance.
   No coefficient, SE, t, p, R^2, Within-R^2, or Wald value was found wrong beyond
   print-rounding (the three 0.001-level p discrepancies — m15, m37, R4's 0.0997 →
   0.100 — are immaterial and cross no boundary).
2. **HC3 is decisive.** Classical Wald F = 9.573 (p = 0.0024) vs HC3 2.954 (p = 0.085)
   for M2; HC0 p = 0.0007, HC1 p = 0.011; bank-clustered CR1 p = 0.008. The "fail to
   reject" conclusions are properties of the conservative robust inference, which the
   thesis justifies correctly — but the thesis overclaims what HC3 delivers ("reliable",
   "protection", "mitigated via HC3").
3. **Two knife-edges, not one.** The R6 rejection is fragile in the multiplicity/margin
   sense (M3, M13), and the *baseline* decision flips if the two excluded rows are
   re-included (M4, p = 0.024). The thesis's hedging ("sensitivity-dependent") is
   directionally right but is not attached to either knife-edge with numbers.
4. **Leverage is extreme throughout.** Mean h = 0.50 (= K/N), max 0.932 (HBL FY 2076/77),
   9/28 above 0.5. HC3 weights and Cook's D are dominated by a few points — which is
   why M7/M8 (influence wording, unassessed normality) matter more here than they would
   in a large sample.
5. **Traceability gaps (no numbers wrong, but not pipeline-reproducible).** Within-R^2
   hand-entered (M9); Model 2 VIFs have no code path (§4(d)); generated Table 5 outputs
   stale, omitting R9 (m9); stale unit test asserting R1-R8 (m10); statsmodels unpinned,
   exact version unrecorded (m40).
6. **Recurring wording overstatements.** "Mitigated via HC3" for influence (M7);
   "reliable finite-sample inference" / "protection" (m5); "eliminates look-ahead bias"
   (m35); "strictly within-year cross-sectional variation" (m4); Ch 3 VIF 1.16
   overgeneralisation (M10); Ch 5 RQ1 backwards sentence (m36). None changes a number;
   together they overstate how much the design establishes.
7. **Power / MDE absent (M1).** The design detects only d ≈ 3 SEs at 80% power; the
   "earnings dominate" narrative rests on insignificant point estimates (M2).
8. **Multiplicity never mentioned (M13)** anywhere in the thesis (grep-verified).
9. **Two brief corrections recorded.** The thesis does **not** state the Within-R^2 formula
   "1 - SSR_LSDV / SST of dummies-only residuals" and does **not** warn against naive
   two-way demeaning (§4(f)); the year-FE-only fit was **not** computed-but-omitted — no
   trace of it exists (§4(k)).

## 6. What is correct (verified strengths)

These items were verified, not merely not-criticised; they are a required part of this review.

1. **Every reported number reproduces.** 383 thesis values checked programmatically
   (dedicated agent, tolerance in §9) with zero exceedances; every cluster's independent
   recomputation agrees. The thesis's arithmetic is trustworthy given the extracted data.
2. **LSDV is the right estimator and is implemented correctly.** Slopes equal the within
   estimator; the dummy trap is avoided; Post's collinearity with year dummies is handled
   by omission, correctly.
3. **HC3 + t(df) is the right inference choice, and not clustering at G = 5 is decisively
   correct.** Clustering would manufacture significance (Wald p = 0.008); HC3 is what
   makes the null results null.
4. **The joint Wald F is the right test for the regime-shift hypothesis**, correctly
   implemented under the HC3 covariance, consistently reported, with the star convention
   correctly applied (M2 unstarred, R6 starred).
5. **Post slopes correctly use the HC3 covariance**, including the large negative
   Cov(beta, delta) — a subtle point the code gets right.
6. **Within-R^2 is defined correctly** and equals the FWL within R^2; the thesis avoids
   the naive double-demeaning error that would have corrupted the interactions.
7. **The robustness suite is pre-specified, not post-hoc** (committed proposal, including
   R9), and sign stability across specs is real.
8. **The freshness protocol is implemented exactly as written**, stale prices are never
   imputed, and the verification limits are disclosed candidly (App A note, App D §D.8).
9. **Null-result language is disciplined** ("Fail to Reject" uniform; no "accept H0" /
   "prove no effect"), and df are disclosed exactly everywhere.
10. **The leave-one-out sensitivity in the App E note exists and is sound** — it is the
    genuine influence mitigation that the "Mitigated via HC3" label misattributes.
11. **The thesis contains its own corrections in several places** (App E discloses the M2
    VIFs; Ch 4 §4.2.6 correctly notes neither R6 interaction is significant; the
    "sensitivity-dependent, not conclusive" sentence is the right conclusion) — the
    problems are that these correct statements are not the ones headlined, or are
    contradicted elsewhere (M10, M3).

## 7. Findings summary table

Status: **V** = VERIFIED (method stated in §4/§9), **I** = INFERRED (basis stated),
**U** = UNVERIFIED / CANNOT DETERMINE (reason stated).

### Major findings

| ID | Location | Severity | Status | One-line description |
|---|---|---|---|---|
| M1 | Ch 1-5 (absence); §4(i) | Major | V | No power / MDE analysis anywhere although headline findings are nulls; design detects only d ≈ 3 SEs at 80% power |
| M2 | Ch 4-5 narrative; §4(i), (g) | Major | V | "Earnings dominate book value" / "no flight to book value" built on insignificant point estimates with wide CIs |
| M3 | Ch 4 R6 discussion; §4(h) | Major | V | R6 rejection presented as "Key Sensitivity Finding" without fragility (multiplicity, 29.5% F-margin, neither interaction significant, R5 fails); LOO attribution corrected — see §4(h) |
| M4 | Ch 5 conclusion; §4(j) | Major | V | Baseline decision flips if the 2 excluded rows are re-included (N = 30: Wald F = 4.762, p = 0.024); no sensitivity analysis exists |
| M5 | Ch 3 / Ch 4 Table 2; §4(j) | Major | V/I | Missingness plausibly MNAR (same failed merger; rows extreme on X) and never characterised; direction conservative but unstated |
| M6 | Ch 4 Table 9 (BP row); `stats/diagnostics.py:48`; §4(e) | Major | V | Reported BP is the Koenker variant, never named; classical BP on M1 rejects (LM 28.18, p = 0.003), reversing "Passed" |
| M7 | Ch 4 Table 9:484; §4(e) | Major | V | "Mitigated via HC3" misstates influence handling; HC3 changes SEs only |
| M8 | Ch 3:360; Ch 4 Fig. 5; §4(e) | Major | V | Normality promised but never assessed in words; Shapiro rejects (M1 p = 0.045, M2 p = 0.038); "residual SD screening" undefined |
| M9 | App E / Tables 5-6; §4(f) | Major | V | Within-R^2 computed nowhere in code; all values hand-entered, unguarded by any test |
| M10 | Ch 3:357; §4(d) | Major | V | VIF ≈ 1.16 overgeneralised to "the estimated models" although M2 VIFs breach the screen on 3 of 4 slopes |
| M11 | Ch 4 §4.2.7 / Table 10; §4(k) | Major | V | Spec table headlines raw LSDV R^2 (0.136 → 0.948) with no adjusted R^2, Within-R^2, or FE F-test in the main text |
| M12 | Ch 4 §4.2.7 (absence); §4(k) | Major | V | Year-FE-only row omitted: year dummies alone give R^2 = 0.919; bank FE add 0.029, jointly insignificant (F = 2.23, p = 0.112) |
| M13 | Whole thesis (absence); §4(h) | Major | V | Multiplicity never mentioned (grep-verified); 8 joint Wald tests, only R6 rejects; adjusted R6 p = 0.168 |
| M14 | Ch 3 / `dataset.py`; §4(j) | Major | V | 5-day freshness length never justified; realised gaps are 0/2 vs 47/54, so the binary exclude/include decision is the knife-edge |

### Minor findings

| ID | Location | Severity | Status | One-line description |
|---|---|---|---|---|
| m1 | App E Model 2 table/note | Minor | V | Post-year dummies / intercept evaluated at EPS = BVPS = 0; gloss invites misreading |
| m2 | `stats/models.py` | Minor | V | Reference category implicit in code (patsy default) |
| m3 | `stats/models.py` | Minor | V | Formulas name `price` not `price_rd` (latent; callers pass filtered panel) |
| m4 | Ch 3; Ch 4:596 | Minor | V | "Strictly within-year cross-sectional variation" overstates one side |
| m5 | Ch 1:176; Ch 3 | Minor | V | "Reliable finite-sample inference" / "protection" overclaimed for HC3 |
| m6 | Ch 3 (absence) | Minor | I | Within-bank error independence assumed, never stated/tested |
| m7 | Ch 3 | Minor | V | "Huber-White cluster SEs" conflates two estimators |
| m8 | Generated Table 4 note | Minor | V | Wald mislabelled "two-tailed" (thesis text correct) |
| m9 | `outputs/tables/T5_robustness.*` | Minor | V | Generated Table 5 outputs stale, omit R9 (0 occurrences) |
| m10 | `tests/test_stats.py:72,88-91` | Minor | V | Test asserts R1-R8 only; fails on current code (25 passed, 1 failed in scratch) |
| m11 | Ch 4 Table 8 (R4) | Minor | V | R4 p = 0.0997 prints as 0.100 (10% boundary) |
| m12 | `assets/t2_correlations.py:55-57` | Minor | V | Pipeline note "variance inflation ~ 30" is wrong (correct ~16.9); thesis text says ~20 |
| m13 | Ch 3 vs Ch 4 Table 9 | Minor | V | VIF threshold inconsistent: screen at 5 vs "Passed" at 10 |
| m14 | Ch 4 Table 4 | Minor | V | Pearson p-values assume normality; fails for MPS_RD and DPS |
| m15 | Ch 4:133 | Minor | V | DPS-MPS p printed 0.678 vs recomputed 0.679 (cause undetermined) |
| m16 | Ch 4 / App E | Minor | V | R9 does not cover HBL FY 2076/77; coverage only via leave-one-out ranges |
| m17 | Ch 4 Cook's discussion | Minor | V | "Extreme price / 2021 bull market" wrong for 2 of 5 flagged points |
| m18 | Ch 4 Table 9 | Minor | V | "Influential" is threshold-dependent (D > 1 flags 0; 4/(n-K-1) flags 3/2) |
| m19 | App E; Ch 4 Table 9 | Minor | V | Flagged table out of order; "Passed" overstates non-rejection; BP note vs code; M2 diagnostics App E only |
| m20 | Whole thesis (absence) | Minor | V | No Within-R^2 formula anywhere; definition verbal only; Ch 3 defines no R^2 |
| m21 | Ch 4-5 | Minor | V | Within-R^2 never interpreted in prose; 0.152 → 0.642 jump unexplained |
| m22 | Ch 4 Table 6 | Minor | V | M2 adjusted R^2 (0.958) only in App E |
| m23 | Ch 4 §4.2.7 | Minor | V | Pooled-vs-FE contrast on unadjusted R^2 without Within-R^2 alongside |
| m24 | App E only | Minor | V | R1-R9 fit statistics only in App E |
| m25 | Ch 4 Table 6 note | Minor | V | Note claims post-slope CIs "are reported in the text" — they are not (App E only) |
| m26 | `t4_model2.py` etc. | Minor | V | Post-slope computation untested; `_combo` duplicated (third copy dead code) |
| m27 | Ch 2:401 | Minor | V | "Eight robustness checks" miscount (suite is nine); Ch 4:447 "eight specifications" is correct, do not change |
| m28 | Ch 1 objectives | Minor | V | Objectives omit the R9 bullet |
| m29 | Proposal vs code | Minor | V | Proposal says ROA/DPS in "Models 1 and 2"; implemented only as Model-2 variants |
| m30 | Ch 4 R6 | Minor | V | R6 drops whole FY 2078/79 incl. 1 non-mismatched row; identical results either way |
| m31 | Ch 4 R8 note | Minor | I | R8 per-row cause attribution ("bonus issues") unsourced |
| m32 | Ch 5 | Minor | V | Unqualified point-estimate regime-change statements |
| m33 | Design (structure) | Minor | I | Effective N < 28 (G = 5); power numbers are optimistic upper bounds |
| m34 | Ch 3 | Minor | V | Publication dates verified for only 2 of 30 bank-years; not stated in one place |
| m35 | Ch 3 | Minor | V | "Eliminates look-ahead bias" overstates |
| m36 | Ch 5:115 | Minor | V | RQ1 sentence backwards (pooled R^2 is low; high R^2 needs year FE *included*) |
| m37 | Ch 4:544,596 | Minor | V/U | Pooled EPS p printed 0.126 vs recomputed 0.128; cause undetermined |
| m38 | Ch 4 Table 3 | Minor | V | Descriptives method undocumented (sample SD ddof = 1; %-change formula unstated) |
| m39 | Ch 4 Table 3 | Minor | V | Selective dispersion reporting (SD % changes only for MPS/EPS) |
| m40 | `requirements.txt`; App D §D.6 | Minor | V | statsmodels unpinned (>= 0.14); exact version used unrecorded |

### Suggestions (optional improvements)

| ID | Location | Description |
|---|---|---|
| s1 | §4(b) | Wild-cluster-bootstrap sensitivity as a small-sample check (G = 5) |
| s2 | §4(g) | Report post slopes for the robustness specs |
| s3 | §4(h) | R4 DPS interacted variant (Wald F = 2.848, p = 0.097), or state why additive-only |
| s4 | §4(h) | Note R^2 is not comparable across different n |
| s5 | §4(f) | Define "Within-R^2" explicitly; bare label is ambiguous vs Stata's one-way within-R^2 |
| s6 | §4(d) | Reword App E "HC3 intervals already reflect [collinearity]" |
| s7 | §4(j) | Ch 4 Table 2 note: "5-day trading window" vs "calendar"; "following the deadline" vs gap-0 realisation |
| s8 | §4(k) | DPS-post median is 0 (mean 1.40 misleading); "halved" for -46.56%; spec-table "Assessment" column is editorial |

---

## 8. Open questions for the author and items that could not be determined

1. **Q1 — 5-day window.** What justifies 5 days, as opposed to any other window — and,
   given realised gaps are 0/2 vs 47/54, what justifies *excluding* rather than
   including (or carrying forward) the two 47/54-day rows? (M14, M4.) This is the
   highest-value open question: the answer moves the headline conclusion.
2. **Q2 — Missingness mechanism.** Were HBL FY 2077/78 and NIMB FY 2077/78 suspended for
   the same failed-merger reason, and what missingness mechanism (MCAR / MAR / MNAR) does
   the author assume? What is the assumed bias direction of excluding them? (M5.)
3. **Q3 — Breusch-Pagan variant.** Was the Koenker variant chosen deliberately? If so, it
   should be named, and the classical variant's M1 rejection (LM 28.18, p = 0.003) should
   be reported or the F-statistic version used instead. (M6.)
4. **Q4 — VIF convention.** Is the slopes-only VIF (dummies excluded) the author's intended
   convention, and on what authority? **CANNOT DETERMINE** from the sources opened in
   this review; the thesis discloses the method but cites no authority for it, and the
   with-dummies numbers (M1 BVPS 12.32; M2 BVPS x Post 259.32) are large. The review
   does not verdict this sub-question either way.
5. **Q5 — Normality.** What is the author's verdict on residual normality, given the Q-Q
   plots and Shapiro-Wilk rejections (M1 p = 0.045, M2 p = 0.038)? What is "residual
   standard deviation screening" (Ch 3:360)? (M8.)
6. **Q6 — Power.** What effect sizes was the design powered to detect, and what should a
   reader conclude from the nulls — "no effect" or "effect smaller than the MDE"? (M1.)
7. **Q7 — Multiplicity.** Was any multiplicity adjustment considered for the 8 joint Wald
   tests, and if not, why does R6 (adjusted p = 0.168) merit "Key Sensitivity Finding"
   framing? (M13, M3.)
8. **Q8 — Year effects.** Why is there no year-FE-only row in Table 10, given year dummies
   alone explain R^2 = 0.919 and bank FE add nothing significant? (M12, M11.)
9. **Q9 — Exact software versions.** Which exact statsmodels version produced the reported
   numbers? (m40.) **UNVERIFIED** — the thesis and the repository record only `>= 0.14`.
10. **Q10 — Rounding discrepancies.** What produced the 0.001-0.002 differences: DPS-MPS p
    0.678 vs 0.679, pooled EPS p 0.126 vs 0.128 (m15, m37)? **CANNOT DETERMINE** — both
    recomputations agree with each other and not with the printed value; neither crosses
    a significance boundary.
11. **Q11 — R8 attribution.** What is the source for attributing the restated-EPS rows to
    "bonus issues"? (m31.)
12. **Items not determined by design.** Pixel-level figure verification (see §3.2);
    R3/R4/R5/R7/R8 *coefficients* by independent recomputation (Wald values verified,
    §3.2); the exact statsmodels version (Q9); the author's intent on Q4.

## 9. Verification log

### 9.1 What was run (coordinator's own verification, 2026-11-12)

All scratch work outside the repository; repository files were only read.

- **Independent OLS + HC3 recomputation** (`/tmp/review-ols.py`, QR-based, numpy + scipy
  only, from the frozen panel CSV): every thesis number for M1/M2 reproduced exactly to
  printed precision — coefficients, SEs, t, p, R^2, adj R^2, Within-R^2, Wald F/p,
  post slopes and CIs; R3-R9 coefficients/SEs and all Wald F/p exact, including R6
  F = 5.818, p = 0.021 and R9 F = 1.794, p = 0.205; BP LM 14.37, p = 0.213 (11 df);
  Cook's max 0.5519 (HBL FY 2076/77), 5 exceeding 0.143; VIF slopes-only M1 1.16/1.16,
  M2 10.33/2.28/15.15/24.13; correlations via scipy `pearsonr`; descriptive means match.
  **Tolerance used:** coefficients/SEs to 0.01, p to 0.005, Wald F to 0.02.
  (Implementation note: naive (X'X)^-1 HC3 is numerically unstable with dummies and
  ~150-scale regressors; the QR-based computation is exact.)
- **Major-findings verification** (`~/workspace/review-scratch/verify_majors.py`,
  statsmodels 0.15.0, venv `~/workspace/review-venv`): N = 30 re-inclusion Wald
  F(2,16) = 4.762, p = 0.024 (baseline N = 28 reproduced first: F = 2.954, p = 0.085);
  pre BVPS 0.100 → 0.709 on inclusion; BP Koenker vs classical for M1 (14.37/0.213 vs
  28.18/0.003) and M2 (14.54/0.337 vs 17.12/0.194); VIF slopes-only vs with-dummies
  (M1 EPS 5.7 / BVPS 12.32; M2 14.82 / 12.46 / 27.34 / 259.32); MDEs at 80% power
  (d = 3.01 SEs at df 14; beta_E 10.73, delta_E 12.06, delta_B 3.71 NPR); Shapiro-Wilk
  M1 W = 0.9246, p = 0.045; M2 W = 0.9216, p = 0.038; DPS-MPS p = 0.678979;
  EPS-ROA r = 0.974656, VIF 19.98; gaps {0, 2, 47, 54}; max EPS HBL FY 2077/78 28.07,
  max BVPS NIMB FY 2077/78 198.28; year-FE-only fit R^2 = 0.919 (EPS 2.185, p = 0.098;
  BVPS 0.555, p = 0.420, df = 20); bank-FE-given-year-F F(4,16) = 2.23, p = 0.112.
- **Leave-one-out, both exercises** (same script): baseline M2 — 1 of 28 deletions below
  0.05 (NIMB FY 2078/79, p = 0.035; range 0.035-0.291); R6's own sample — 16 of 23
  below 0.05 (range 0.013-0.634). This corrects the consolidated subagent report's
  attribution (see M3).
- **Test suite** (scratch copy of `data_analysis`, excluding `.venv`): **25 passed,
  1 failed** — `test_robustness_runs_cover_methodology_step4` asserts run ids == R1..R8
  but `build_runs` returns R1..R9 (stale assertion, not a thesis-number error). The
  sanity-gate test (M1/M2 numbers vs the exploratory audit) passes. `generate --check`
  OK (coverage 28; window-excluded HBL/NIMB FY 2077/78; entity-mismatch = the 4
  FY 2078/79 rows). `verify.py` OK (18 assets, all declared outputs present and
  consistent vs the manifest).
- **Text/code checks by grep and reading (2026-11-12):** multiplicity terms 0 matches;
  "statistical power" 0 matches; "within" absent from `stats/` + `assets/` (except the
  freshness-window phrase); Ch 3:357 VIF sentence, Ch 2:401 "eight", Ch 4:447 "eight
  specifications", Ch 4 Table 9 rows (VIF "Passed" < 10.0; BP "Passed"; Cook's
  "Mitigated via HC3"), Ch 5:115 RQ1 sentence, T5 outputs 0 occurrences of "R9",
  `test_stats.py:72` R1-R8 assertion, `t2_correlations.py:56` "~ 30", `vif_table`
  called only for ("eps", "bvps"), Ch 1 objectives with no R9 bullet, "residual
  standard deviation screening" only at Ch 3:360.

### 9.2 What the review team (subagents) ran

- **Dedicated recomputation agent:** independent numpy/scipy OLS + HC3 + Wald (no repo
  stats module imported), cross-checked against statsmodels 0.15.0 (max |statsmodels -
  numpy| = 6.3e-11 over all coefficients/SEs/t/p; R^2/Wald/post slopes agree to ≤ 1e-9).
  **383 thesis values checked programmatically — zero exceedances.** Tolerance:
  coef/SE/CI ±0.0005, t ±0.005, p ±0.0005, R^2/adj R^2/Within-R^2/Wald F ±0.0005 (half
  the last printed unit; genuine numerical noise ~1e-10). Largest deviations are exactly
  what print-rounding predicts. All 96 printed 95% CI limits agree. Sample realisation
  verified: exactly HBL FY 2077/78 (gap 54) and NIMB FY 2077/78 (gap 47) excluded;
  n = 28 (13 pre, 15 post); R6 n = 23, k = 13, df = 10; R9 n = 27, k = 14, df = 13.
  Scratch: `/tmp/recomp/` (since partly lost with the tmpfs; the primary recomputation
  is version-independent numpy code, so this does not affect any result).
- **Cluster (c)** ran the repository's own statsmodels 0.14.4 code (`build_runs` +
  `joint_zero_test`) and reproduced all 8 Wald F/p/df exactly. Clusters (d)/(e)/(f)/(k)
  independently reproduced the correlations, VIFs, BP, Cook's D, Within-R^2,
  descriptives, and spec-comparison numbers.

### 9.3 What could not be run, and why

- R3/R4/R5/R7/R8 *coefficients* were not independently recomputed by the dedicated agent
  (outside its scope); their Wald F/p were reproduced by cluster (c). No error alleged.
- Pixel-level verification of rendered Figures F1-F6 / A1-A3 was not performed (see §3.2).
- The `statsmodels` version that produced the reported numbers is unrecorded (Q9); results
  were reproduced under both 0.14.4 and 0.15.0 with identical outcomes.
- Two statsmodels installs during the review failed with "No space left on device"
  (`/tmp` is a 512 MB tmpfs that filled); a lean install into `~/workspace/review-venv`
  with `TMPDIR=~/workspace/review-tmp` succeeded. This affected logistics only.

### 9.4 Sources consulted

**Opened in full by the coordinator during this review:**

- statsmodels 0.15.0 documentation, `statsmodels.stats.diagnostic.het_breuschpagan` —
  https://www.statsmodels.org/stable/generated/statsmodels.stats.diagnostic.het_breuschpagan.html
  — signature `het_breuschpagan(resid, exog_het, robust=True)`; "Flag indicating whether
  to use the Koenker version of the test (default) … or the original Breusch-Pagan
  version which assumes residuals are normally distributed." This is the source for M6's
  mechanism. References therein: Breusch & Pagan (1979), *Econometrica* 47(5):1287-1294;
  Koenker (1981), *Journal of Econometrics* 17(1):107-112.

**Opened by subagent researchers during the task (titles as reported in their handoffs;
URLs were not retained in the consolidated report — flagged here, and no load-bearing
claim in this review rests solely on them):** MacKinnon & White (1985); Long & Ervin
(2000); MacKinnon (2013); Cameron & Miller (2015); Cameron, Gelbach & Miller (2008);
Wooldridge, *Introductory Econometrics*, Ch 6/14 (via notes pages); Stata `xtreg`
documentation and Statalist threads on within-R^2; statsmodels documentation
(0.13.5 / 0.14.0 / 0.14.4 / 0.15.0) for `f_test`, `t_test`,
`variance_inflation_factor`, `OLSResults`, `FTestPower`, `sandwich_covariance`;
O'Brien (2007) on VIF; SciPy `pearsonr` documentation; Brambor, Clark & Golder (2006);
Hoenig & Heisey (2001); Wasserstein & Lazar (2016) ASA statement; Sterne et al. (2009)
BMJ; MacKinlay (1997); Scholes & Williams (1977) / Dimson (1979); Madura et al. (2006);
Gelman, Hill & Yajima (2012). **Caveat:** several subagents opened some of these only via
search-result excerpts; those are not presented here as full opens, and the verdicts in
§4 rest on the thesis text, the code, and the recomputations in §9.1-9.2, not on the
authority of any unopened source.

**In-repo sources read in full:** the entire thesis (abstract, Ch 1-5, App A-E, working
tree); `data_analysis/analysis/` (stats, dataset, loaders, configs, assets, tests);
the committed proposal's methodology section; `requirements.txt`; the analysis README.

## 10. Recommended actions, prioritized and NOT applied

Nothing in this section has been applied. No file was changed. Each item needs the
author's decision (and, for thesis text, the supervisor-bound approval the author
requires).

### P0 — before the thesis is defended as written

1. **Report power / MDE** (M1). Add a short power/MDE paragraph: at 80% power the design
   detects only ~3 SEs (beta_E MDE 10.73 NPR, delta_E 12.06, delta_B 3.71), and state what
   the nulls can and cannot claim.
2. **Qualify R6 and add a multiplicity note** (M3, M13). State the Bonferroni/Holm-adjusted
   R6 p = 0.168, the 29.5% F-margin, that neither R6 interaction is significant, and that
   R5 at the same N/df fails to reject. Downgrade "Key Sensitivity Finding" framing.
3. **Add the two-exclusion sensitivity** (M4, M5, M14). Report the N = 30 fit (Wald
   F(2,16) = 4.762, p = 0.024) and the carry-forward variant (F = 3.870, p = 0.043);
   justify the 5-day window or the exclusion decision; name the missingness mechanism
   and the bias direction (exclusion attenuates pre BVPS 0.100 → 0.709 when included).
4. **Name the BP variant and report the classical result** (M6). Either name Koenker and
   show classical M1 (LM 28.18, p = 0.003), or report the F-statistic version
   (p = 0.212 either way), and correct Table 9's M1 "Passed".
5. **Fix the Ch 3 VIF sentence** (M10). Restrict the ≈ 1.16 claim to Model 1; point to the
   App E M2 VIFs (10.33 / 2.28 / 15.15 / 24.13) where they are disclosed.

### P1 — material corrections and traceability

6. **Fix "Mitigated via HC3"** (M7). Replace with the leave-one-out sensitivity as the
   influence mitigation (App E note already contains it).
7. **Assess normality in words** (M8). Give a verdict on the Q-Q plots; report the
   Shapiro-Wilk results or state why they are not used; define or delete "residual
   standard deviation screening".
8. **Fix Ch 2:401 "eight robustness checks" → "nine"** (m27). (A separate one-word-fix
   decision is already pending with the author; this item records the same miscount
   independently. Do **not** touch Ch 4:447 — it is correct.)
9. **Fix the Ch 5 RQ1 sentence** (m36). High R^2 appears only when year FE are *included*,
   not when they are omitted.
10. **Show the year-FE-only row and the FE F-tests in the main text** (M11, M12). Year
    dummies alone: R^2 = 0.919; bank FE given year FE: F(4,16) = 2.23, p = 0.112. Add
    adjusted / Within-R^2 to the Table 10 discussion.
11. **Put Within-R^2 in the code** (M9). Compute it in the pipeline and test it; add the
    formula to Ch 3 (m20). Same for the M2 VIFs (add a code path; §4(d)).
12. **Qualify the narrative sentences** (M2, m32). Attach CIs to "earnings dominate" and
    "no flight to book value"; the post BVPS CI admits +0.74.
13. **Fix the stale test and stale generated outputs** (m10, m9). Update
    `test_stats.py:72` to R1..R9; regenerate T5 outputs so they include R9.

### P2 — minor wording, rounding, and suggestions

14. Correct the pipeline "~ 30" note to ~20 (m12); reconcile the VIF threshold 5 vs 10
    (m13); correct the DPS-MPS p 0.678 → 0.679 and pooled EPS p 0.126 → 0.128, or
    establish their source (m15, m37); fix the Table 6 note on post-slope CIs (m25);
    add the R9 bullet to Ch 1 objectives (m28); fix the remaining minors m1-m8, m14,
    m16-m19, m21-m26, m29-m31, m33-m35, m38-m40 as listed in §7.
15. Consider suggestions s1-s8 (wild-cluster bootstrap; post slopes per robustness spec;
    R4 interacted variant or a stated reason; R^2 comparability note; Within-R^2 label;
    App E HC3 wording; Table 2 note wording; DPS median reporting).

---

*End of review. Verdict summary: all 11 methods reviewed are **Correct with caveats**;
no method is Incorrect; 0 Critical, 14 Major, 40 Minor findings, 8 suggestions. The
numbers are right; what needs work before defence is what the numbers are allowed to
claim — power, the two knife-edges (R6/multiplicity and the two excluded rows), the
Breusch-Pagan variant, and the VIF/influence/normality reporting.*
