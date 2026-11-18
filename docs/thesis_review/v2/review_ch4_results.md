# Independent Content Review — Chapter IV: Results and Discussion (v2)

**Dissertation:** *Value Relevance of Accounting Information Before and After the Banking Consolidation Wave: Evidence from Nepalese Commercial Banks*
**Repo:** `~/workspace/verbose-chainsaw`
**HEAD:** `2b4e10f` ("Add independent data-analysis review (v1)", 2026-11-14)
**Reviewed version:** the working tree as it stands, including uncommitted changes. This review was written against the working-tree text of `src/thesis/chapters/chapter_04_results_and_discussion.tex` (677 lines), not against HEAD. Where the working tree differs from what the v1 review (`docs/thesis_review/v1/data_analysis_review.md`) described, the working-tree text governs and the difference is noted.
**Review date:** 17 November 2026
**Reviewer role:** independent examiner, read-only content review of Chapter IV only.
**Output file:** `docs/thesis_review/v2/review_ch4_results.md` (this file; the only file created by this review).

## Scope and method

- Read in full: `src/thesis/chapters/chapter_04_results_and_discussion.tex` (all 677 lines).
- Read for cross-checking numbers only: `src/thesis/front/abstract.tex` (23 lines); the results paragraph of Chapter I (`src/thesis/chapters/chapter_01_introduction.tex:17`); the results-summary parts of Chapter V (`src/thesis/chapters/chapter_05_summary_and_conclusion.tex`, §§5.2.3–5.3, Tables and decision table).
- Read to check literature linkage only: the relevant passages of Chapter II (`src/thesis/chapters/chapter_02_literature_review.tex`, cited by line below) and the bibliography entries for works cited in Chapter IV.
- Read to check pointer targets only: Appendix B (dataset table, `src/thesis/appendices/appendix_b.tex`) and Appendix E (`src/thesis/appendices/appendix_e.tex`, Tables `tab:app_m1full`, `tab:app_m2full`, `tab:app_fetests`, `tab:app_robustfull`, `tab:app_robust_inf`, `tab:app_sensitivity` and their notes).
- Read to know what v1 established: `docs/thesis_review/v1/data_analysis_review.md`. Per the task, the statistics were **not** re-audited: no pipeline code was run, no dataset was re-estimated, and no p-value or standard error was recomputed from raw data. Arithmetic in this review is limited to text-internal consistency checks (e.g. coefficient ÷ standard error = t; percentage change from the printed table means; implied slopes as sums of printed coefficients) and to cross-location agreement of the same number.
- The one external source opened was the Faculty of Management, Tribhuvan University *Master's Degree Dissertation Guidelines* (2019), repo copy `docs/thesis_guidelines_reference/01_TU-FOM_Masters-Dissertation-Guidelines-2019.pdf`, pp. 14–15 (Chapter IV and Chapter V sections). No other external source was consulted.
- Plagiarism checking was **not** covered. No judgement is made about authorship or AI-tool use. Only observable, locatable issues in the text are reported.
- Nothing under `~/workspace/review-audit-scratch/` was read. No prior summary was used as evidence; every finding below cites a location I opened during this task.

## Verdict

**Ready with minor revisions.**

Reason: the headline numbers agree across the Chapter IV text, its tables, the abstract, Chapter I and Chapter V; the hypothesis decisions agree with the reported p-values; the covariance-sensitivity table (`tab:cov_sensitivity`) is present and its description matches the table; and the handling of the sensitivity-dependent R6 result in Chapter IV prose is careful and repeatedly qualified (unadjusted, Holm-adjusted p = 0.169, does not survive leave-one-bank perturbation). No finding below requires re-estimation, changes any hypothesis decision, or reverses any headline conclusion. The Major findings are all narrow, presentational or interpretive fixes: one table that signals significance without its multiplicity caveat (D-01), one discussion mechanism that contradicts the thesis's own reported correlation (D-02), and one over-promised sentence about confidence intervals (D-03). The remaining findings are Minor or Suggestions.

---

## 1. Inventory

### 1.1 Chapter IV sections — all REVIEWED

| Section | Lines | Content | Status |
|---|---|---|---|
| 4.1 Introduction | 3–28 | Chapter roadmap; FOM Guidelines (2019, pp. 14–15) cited as the organising rule; Results/Discussion split | REVIEWED |
| 4.2 Results | 30–594 | — | REVIEWED |
| 4.2.1 Descriptive Statistics | 32–99 | Table 4.1 + Figure 4.1 + bullet interpretation | REVIEWED |
| 4.2.2 Correlation Analysis and Multicollinearity Assessment | 100–164 | Table 4.2 + Figures 4.2–4.3 + interpretation + normality/Spearman note | REVIEWED |
| 4.2.3 Baseline Value Relevance: Model 1 Estimation | 166–216 | Equation, Table 4.3, coefficient/significance/fit bullets | REVIEWED |
| 4.2.4 Impact of Consolidation: Model 2 Estimation | 218–335 | Equation, Table 4.4, pre/interaction/implied/Wald items, Figures 4.4–4.5 | REVIEWED |
| 4.2.5 Hypothesis Testing | 336–393 | Table 4.5 + per-hypothesis evaluations + joint test | REVIEWED |
| 4.2.6 Robustness and Sensitivity Analyses (R1–R9) | 394–503 | Tables 4.6–4.7, Figure 4.6, R3–R9 bullets, bootstrap, price-window sensitivities | REVIEWED |
| 4.2.7 Econometric Diagnostics and Specification Comparison | 505–594 | Table 4.8, Figure 4.7, §4.2.7.1 spec comparison + Table 4.9 | REVIEWED |
| 4.3 Discussion | 596–677 | — | REVIEWED |
| 4.3.1 Value Relevance in the Pre-Consolidation Regime | 598–605 | Pre-regime slopes, non-establishment caveats | REVIEWED |
| 4.3.2 Regime Shift: Earnings and Book Value Slopes Post-Consolidation | 607–616 | Attenuation + three mechanism bullets + BVPS point-estimate bullet | REVIEWED |
| 4.3.3 Reconciling with Theoretical Frameworks | 618–637 | Kwon (2020), Ohlson (1995), dividend signalling, banking opacity | REVIEWED |
| 4.3.4 Comparative Context with Nepalese and International Empirical Studies | 639–659 | Prior Nepalese studies, Chaudhari/Pant/Timalsina, Almumani/Malhotra | REVIEWED |
| 4.3.5 Methodological Context: Transition Dynamics and Structural Discontinuities | 661–675 | R6, 5-day rule, BAFIA §59(2) anchor | REVIEWED |
| Chapter summary paragraph | 676–677 | Closing summary of §4.3 | REVIEWED |

Roadmap check (VERIFIED): §4.1 lists seven Results subsections (§§4.2.1–4.2.7) and five Discussion subsections (§§4.3.1–4.3.5); the chapter contains exactly those. The §4.1 claim that the chapter is organised into Results and Discussion "in accordance with the Faculty of Management, Tribhuvan University *Master's Degree Dissertation Guidelines* (2019, pp. 14–15)" was checked against the repo copy of those Guidelines, pp. 14–15, which state Chapter IV is "Results and Discussion", that Results should "seek to answer the research questions posed or test the hypotheses" and report "the obtained value of the test statistic, the degree of freedom, etc.", and that Discussion should interpret results "in the light of theories and empirical studies", giving "care … to sources of potential bias, the imprecision of measures, the effect of sample size, and other methodological limitations". The chapter's structure matches that prescription.

### 1.2 Chapter IV tables — all REVIEWED (text, caption, note, in-text reference)

| Label | Lines | Caption (short) | Captioned | Referenced in text | Status |
|---|---|---|---|---|---|
| `tab:t1_descriptives` | 37–84 | Descriptive Statistics of Value-Relevance Variables | Yes | Yes, §4.2.1 (2×) | REVIEWED |
| `tab:t2_correlations` | 103–129 | Pearson Correlation Matrix (N = 28) | Yes | Yes, §4.2.2 | REVIEWED |
| `tab:t3_model1` | 175–209 | Model 1: Baseline Value Relevance (N = 28) | Yes | Yes, §4.2.3 (2×) | REVIEWED |
| `tab:t4_model2` | 232–279 | Model 2: Value Relevance Regime Shift (N = 28) | Yes | Yes, §4.2.4 (5×) | REVIEWED |
| `tab:hypotheses` | 343–373 | Summary of Operational Hypothesis Testing Decisions | Yes | Yes, §4.2.5 | REVIEWED |
| `tab:t5_robustness` | 400–435 | Robustness and Sensitivity Analysis Across Econometric Specifications | Yes | Yes, §4.2.6 (2×) | REVIEWED |
| `tab:cov_sensitivity` | 437–469 | Joint Regime-Shift Tests Under Alternative Covariance Estimators | Yes | Yes, §§4.2.5–4.2.6 | REVIEWED |
| `tab:t6_diagnostics` | 511–541 | Econometric Diagnostics for Baseline Value-Relevance Model | Yes | Yes, §4.2.7 | REVIEWED |
| `tab:spec_comp` | 568–590 | Specification Comparison Across Econometric Model Structures | Yes | Yes, §4.2.7 (3×) | REVIEWED |

Numbering check (VERIFIED): the tables appear in source order with LaTeX auto-numbering, so their compiled numbers follow presentation order; every table is captioned and referenced at least once, and every reference precedes or immediately accompanies its table. No orphan table and no dangling reference was found in Chapter IV. All cross-references to Appendix E (`tab:app_m1full`, `tab:app_m2full`, `tab:app_fetests`, `tab:app_robustfull`, `tab:app_sensitivity`) resolve to labels that exist in `src/thesis/appendices/appendix_e.tex` (checked: `tab:app_m1full` line 25, `tab:app_m2full` line 67, `tab:app_fetests` line 113, `tab:app_robustfull` line 148, `tab:app_sensitivity` line 567).

### 1.3 Chapter IV figures — REVIEWED (caption, note, in-text reference; plotted content spot-checked, see below)

| Label | Lines | File | Captioned | Referenced | Status |
|---|---|---|---|---|---|
| `fig:trends` | 86–98 | `figures/F6_trends.pdf` | Yes | Yes (2×) | REVIEWED — caption/note/reference; plotted content not visually inspected |
| `fig:scatter_matrix` | 142–152 | `figures/F1_scatter_matrix.pdf` | Yes | Yes | REVIEWED — caption/note/reference; plotted content not visually inspected |
| `fig:heatmap` | 154–164 | `figures/F2_correlation_heatmap.pdf` | Yes | Yes | REVIEWED — caption/note/reference; plotted content not visually inspected |
| `fig:value_relevance` | 310–320 | `figures/F3_value_relevance.pdf` | Yes | Yes | REVIEWED — caption/note/reference; **plotted content visually spot-checked** (see §4, Strength S-12) |
| `fig:coeff_forest` | 322–334 | `figures/F4_coefficient_forest.pdf` | Yes | Yes | REVIEWED — caption/note/reference; plotted content not visually inspected |
| `fig:robustness_forest` | 491–503 | `figures/A2_robustness_forest.pdf` | Yes | Yes | REVIEWED — caption/note/reference; plotted content not visually inspected |
| `fig:diagnostics` | 553–563 | `figures/F5_diagnostics.pdf` | Yes | Yes | REVIEWED — caption/note/reference; plotted content not visually inspected |

All seven figure files exist in `src/thesis/figures/` as both `.pdf` (the included file) and `.png`. Every figure is captioned, referenced in the text before or at its placement, and numbered consistently by LaTeX order of appearance. Limitation: except for `fig:value_relevance`, I did not visually inspect the plotted content against the caption/data, so I cannot verify from this review that the other six plots show what their captions claim (see Verification log). The underlying file names are non-sequential relative to presentation order (F6 first, then F1, F2, F3, F4, A2, F5); this is a file-naming artefact only and does not affect compiled numbering (see D-13).

---

## 2. Headline-number cross-check (Chapter IV text vs tables vs abstract / Ch. I / Ch. V)

All numbers below were read in each location; "agree" means identical to the printed rounding.

| Quantity | Ch. IV text | Ch. IV table | Abstract | Ch. I (:17) | Ch. V | Verdict |
|---|---|---|---|---|---|---|
| N = 28 (13 pre / 15 post; 2 dropped) | §4.2.1, lines 33–36 | Tab. 4.1 | Yes | — | §5.2.2 | VERIFIED — agree |
| MPS mean 254.34; pre 310.59; post 205.60; −33.81% | lines 71–72 | Tab. 4.1 | — | — | §5.2.3 | VERIFIED — agree; −33.81% reproduces from printed means (−33.80% by my arithmetic on rounded values; 0.01 pp rounding) |
| EPS mean 14.05; pre 17.90; post 10.72; −40.13% | line 73 | Tab. 4.1 | — | — | §5.2.3 | VERIFIED — agree |
| BVPS mean 160.18; pre 158.11; post 161.97; +2.45% | line 74 | Tab. 4.1 | — | — | §5.2.3 | VERIFIED — agree |
| DPS mean 6.06 → 1.40; −76.90%; 12 of 15 post = 0 | lines 80, 614 | Tab. 4.1 (means only) | — | — | §5.2.3 | VERIFIED — means agree; the "12 of 15 zero" count was verified by counting DPS = 0.00 post-consolidation rows in Appendix B (GBIME 1, HBL 3, KBL 3, NIMB 3, NMB 2 = 12); with 12 of 15 zero, median zero follows |
| ROA mean 1.31% → 0.70%; −46.38% | line 81 | Tab. 4.1 | — | — | — | VERIFIED — means agree; % change see D-09 |
| EPS–ROA r = 0.975; bivariate VIF ≈ 20 | lines 135–136 | Tab. 4.2 | — | — | §5.2.3 | VERIFIED — 1/(1−0.975²) = 20.4, consistent with "approximately 20" |
| EPS–BVPS r = 0.372, p = 0.051; Spearman ρ = 0.295, p = 0.127 | lines 137–140 | Tab. 4.2 | — | — | §5.2.3 | VERIFIED — agree |
| Model 1: β_E = 2.095 (SE 4.096), t = 0.51, p = 0.616; β_B = 0.219 (SE 1.858), t = 0.12, p = 0.908; R² = 0.948, adj. 0.912, within-R² 0.152, df 16 | lines 211–215 | Tab. 4.3 | Yes | Yes | §5.2.3 | VERIFIED — agree in all five locations; t = coef/SE checks (2.095/4.096 = 0.51; 0.219/1.858 = 0.12); 95% CIs in text (−6.587 to 10.777; −3.720 to 4.158) check against coef ± t-critical × SE |
| Model 2: β_E = 5.577 (3.560), p = 0.140; β_B = 0.100 (1.306), p = 0.940; δ_E = −3.124 (4.003), p = 0.448; δ_B = −1.758 (1.231), p = 0.175; implied post 2.453 (p = 0.298) and −1.658 (p = 0.161); Wald F(2,14) = 2.954, p = 0.085; R² = 0.978, adj. 0.958, within-R² 0.642, df 14 | lines 286–308 | Tab. 4.4 | Yes | Yes | §5.2.3 | VERIFIED — agree in all locations; implied slopes are exact sums of printed coefficients (5.577 − 3.124 = 2.453; 0.100 − 1.758 = −1.658); t = coef/SE checks for all six (1.57, 0.08, −0.78, −1.43, 1.08, −1.48) |
| Hypothesis decisions: H1–H4 all Fail to Reject; joint Fail to Reject | lines 377–392 | Tab. 4.5 | — | — | Tab. 5.1 | VERIFIED — decisions agree with p-values (all > 0.05) and with Ch. V Table `tab:hyp_decisions`, except Ch. V adds an R6 "Reject H0 (unadjusted; sensitivity only)" row that Chapter IV's Table 4.5 correctly does not contain |
| R1–R9 coefficients, SEs, Wald F/p, n | lines 474–482 | Tab. 4.6 | — | — | §5.2.3 | VERIFIED — text values match Tab. 4.6 and Appendix E `tab:app_robustfull` (4-dp values: e.g. R6 4.3360 (3.7239), −2.6108 (1.5174), F 5.818 (0.021)); R3–R6 p-values in text match Appendix E `tab:app_robust_inf` (R3 0.312/0.611/0.163; R4 0.443/0.208; R5 0.650/0.215; R6 0.620/0.116) |
| Covariance sensitivity: all eight R2–R9 reject at 5% under Classical/HC0/HC1/HC2; only R6 under HC3 | lines 391–392, 468 (note) | Tab. 4.7 | — | — | §5.2.3 | VERIFIED — every cell in Tab. 4.7 was read: Classical p max 0.012, HC0 max 0.002, HC1 max 0.027, HC2 max 0.025 (all < 0.05); HC3 column has only R6 at 0.021 < 0.05; HC3 column reproduces Tab. 4.6 Wald column exactly for all eight rows |
| R6: F(2,10) = 5.818, p = 0.021 unadjusted; Holm-adjusted p = 0.169; leave-one-bank F = 0.615–1.309, p = 0.329–0.572 | lines 478–479, 664–669 | Tabs. 4.6–4.7 | Yes (with Holm) | Yes (with Holm) | §5.2.3 | VERIFIED — agree in all locations; "29.5% decrease" (line 478) is arithmetically correct for the stated critical value 4.103 (1 − 4.103/5.818 = 29.5%); Ch. V's "41.8% above the critical value" is the same fact framed the other way (5.818/4.103 − 1 = 41.8%) — both correct, different framings |
| Diagnostics: VIFs 1.16 / 10.33 / 2.28 / 15.15 / 24.13; Koenker BP LM 14.37 (p = 0.213); classical BP 28.18 (p = 0.003); max Cook's D 0.552, cutoff 4/N = 0.143; Shapiro-Wilk W = 0.925 (p = 0.045) / 0.922 (p = 0.038) | lines 520–549 | Tab. 4.8 | — | — | — | VERIFIED — text matches Tab. 4.8; Shapiro-Wilk values match Appendix E line 503 (W = 0.9246/0.9216, p = 0.045/0.038); "five observations exceed 4/N" matches Appendix E line 497 (five flagged in Model 1, Table `tab:app_flagged`) |
| Spec comparison: pooled β_E = 4.882 (p = 0.128), R² = 0.136; year-FE R² = 0.919; two-way R² = 0.948; within-R² 0.152 → 0.642; FE-only R² 93.9% | lines 594 | Tab. 4.9 | — | — | §5.2.3 | VERIFIED except the FE-only 93.9% and F(4,16) = 2.23, which are text-only (see D-08); 0.93 pp and 3.9 pp increments are arithmetically consistent with 93.9% (0.948 − 0.939 = 0.009; 0.978 − 0.939 = 0.039) |

**Attribution check (VERIFIED):** the extreme-value attributions in §4.2.1 were checked against the Appendix B dataset table: MPS max 520.00 = HBL FY 2076/77; EPS max 27.60 = HBL FY 2076/77, min 0.02 = KBL FY 2080/81; BVPS range 132.71 (KBL FY 2080/81) to 190.70 (NIMB FY 2076/77) on the 28-row sample; DPS pre min 2.00 (GBIME FY 2076/77), max 12.50 (KBL FY 2078/79); post DPS max 8.00 (GBIME). Note the excluded NIMB FY 2077/78 row carries BVPS 198.28 and the excluded HBL FY 2077/78 row carries EPS 28.07, both outside the Table 4.1 ranges — consistent with Table 4.1 being computed on the 28 realised rows, though the text does not say so explicitly.

**V1-difference note (VERIFIED by reading current text):** two issues prominent in the v1 review do **not** occur in the current working-tree Chapter IV. (i) v1 F06 (β_E read as a "5.58 times earnings" P/E multiple) — current line 286 reads "a one-rupee increase in EPS is associated with a 5.58-rupee increase in price, conditional on book value and the fixed effects", which is the correct partial-slope reading. (ii) v1 F04 (HC3 described as correcting "small-cluster downward bias") — that phrase does not occur in current Chapter IV or the current abstract. (iii) v1's traceability row 23 refers to a "power subsection" in Chapter IV; the current Chapter IV contains no MDE/power statement (see D-12/Suggestion). These are recorded as differences between the v1 snapshot and the working tree, not as new findings.

---

## 3. Findings

Severity: Critical / Major / Minor / Suggestion. Revision scale: Narrow / Substantive / Fundamental. Status: VERIFIED (how) / INFERRED (basis) / UNVERIFIED (why not).

### D-01 — Table 4.6 signals R6 as significant with no multiplicity caveat in the table itself
- **Location:** `src/thesis/chapters/chapter_04_results_and_discussion.tex`, Table `tab:t5_robustness`, R6 row line 420; table note lines 433–435.
- **Severity:** Major. **Revision scale:** Narrow. **Status:** VERIFIED — read the table row, its note, and the surrounding prose (lines 477–479).
- **Evidence:** R6 cell reads "`\textbf{5.818 (0.021)\textsuperscript{*}}`" (bolded, starred) and the note states only "`\textsuperscript{*} Significant at $p < 0.05$`", with no mention of Holm adjustment anywhere in the table or its note. The prose at line 478 does qualify it: "Holm adjustment across that family gives $p = 0.169$. The R6 result therefore remains a sensitivity finding and does not provide multiplicity-adjusted evidence of a regime shift."
- **Impact:** A reader who reads only Table 4.6 — the chapter's robustness summary — takes away a significant regime-shift finding. The qualification exists but lives only in prose. This is the Chapter IV analogue of the decision-table issue v1 recorded for Chapter V; Chapter IV's own hypothesis table (`tab:hypotheses`) correctly omits R6, so the inconsistency is confined to Table 4.6's presentation. Fixing it (unbold, or add "unadjusted; Holm-adjusted p = 0.169" to the note) changes no claim or conclusion, only how the table reads.

### D-02 — Dividend-cessation mechanism contradicts the thesis's own DPS–price correlation, and Chapter IV never notes the tension
- **Location:** `src/thesis/chapters/chapter_04_results_and_discussion.tex`, §4.3.2 line 614 and §4.3.3 line 634.
- **Severity:** Major. **Revision scale:** Substantive (one mechanism bullet needs re-framing, not just a word change). **Status:** VERIFIED — read both passages and Table 4.2 (lines 118, 131–133).
- **Evidence:** Line 614: "In the pre-consolidation period, regular cash dividends provided an observable benchmark for equity valuations (mean DPS = NPR 6.06). … The withdrawal of regular dividend payments removed an observable cash flow signal." Line 634: "cash dividends historically functioned as an observable verification of accounting profits. When regulatory capital constraints forced banks to eliminate cash dividends post-consolidation, the absence of this verification signal coincided with the attenuation of the earnings slope." But Table 4.2 reports DPS–price correlation "`0.082`" (line 118) and the text at lines 131–133 reports it as "`$r = 0.082, p = 0.679$`" — essentially no linear association between DPS and price in this sample. Chapter IV never acknowledges that the variable invoked as a valuation benchmark shows no price association in its own data.
- **Impact:** Would change an interpretive claim, not a numerical conclusion. The mechanism as written invites the reader to treat dividend loss as an explanation for earnings-slope attenuation, while the thesis's own evidence gives no support for dividends anchoring valuation here. Chapter V does flag this ("DPS was never shown to anchor valuation (its correlation with price is $r = 0.082$, $p = 0.679$)", §5.4.1), so the caveat exists in the thesis but is absent exactly where the mechanism is argued. Narrowest fix: add one sentence in §4.3.2 noting the near-zero DPS–price correlation and that the dividend mechanism is therefore a theoretical hypothesis, not something the sample corroborates.

### D-03 — Model 2 introduction promises confidence intervals "reported in the text"; interaction and implied-slope CIs are not in Chapter IV text
- **Location:** `src/thesis/chapters/chapter_04_results_and_discussion.tex`, line 232 (introductory sentence to Table `tab:t4_model2`); Table 4.4 note, lines ~276–278.
- **Severity:** Major. **Revision scale:** Narrow. **Status:** VERIFIED — read line 232, the full Model 2 enumerated items (lines 284–308), and the Table 4.4 note.
- **Evidence:** Line 232: "`$t$-statistics, $p$-values, and confidence intervals are reported in the text.`" The Model 2 text items report t and p throughout, and one CI (pre-consolidation β_E, "[−2.059, 13.213]", line 286), but no CI for δ_E, δ_B, or either implied post-consolidation slope. The Table 4.4 note itself contradicts the promise: "`their confidence intervals are printed in Appendix E, Table~\ref{tab:app_m2full}`".
- **Impact:** Would change compliance with the chapter's own reporting claim (and with the TU Guidelines' instruction, pp. 14–15, to "include sufficient information to help the reader to fully understand the analyses" for inferential tests). The numbers exist in Appendix E (verified: `tab:app_m2full` note gives implied-slope CIs [−2.4124, 7.3192] and [−4.0593, 0.7441]); the fix is either to print the CIs in the text or to correct line 232 to point to Appendix E. (For contrast, the equivalent promise for Model 1 is kept: both Model 1 CIs are printed in the text at lines 213–214.)

### D-04 — Framing sentences overstate all-insignificant results
- **Location:** `src/thesis/chapters/chapter_04_results_and_discussion.tex`, line 282 and line 608.
- **Severity:** Minor. **Revision scale:** Narrow. **Status:** VERIFIED — read both sentences with the items that follow them.
- **Evidence:** Line 282: "The empirical estimates in Table~\ref{tab:t4_model2} provide substantive evidence regarding structural changes in valuation dynamics:" — the enumerated items that follow report six estimates, none significant at 5% (p = 0.140, 0.940, 0.448, 0.175, 0.298, 0.161) and a joint test at p = 0.085. Line 608: "the empirical estimates reveal a noticeable attenuation of the implied slopes" — again of point estimates whose differences are not significant (the same paragraph then correctly hedges: "these patterns are interpreted not as proven causal effects, but as suggestive structural tendencies", line 610).
- **Impact:** Would change wording, not any claim or conclusion. The hedging that follows each sentence limits the damage, but a lead sentence should not promise "substantive evidence" of changes the evidence does not establish. Replacing "substantive evidence regarding structural changes" with "estimates relevant to the question of structural change" (and "noticeable attenuation" with "attenuation in point estimates") would align the framing with the results.

### D-05 — Hypothesis table uses inconsistent language for identical decisions
- **Location:** `src/thesis/chapters/chapter_04_results_and_discussion.tex`, Table `tab:hypotheses`, lines 353–363.
- **Severity:** Minor. **Revision scale:** Narrow. **Status:** VERIFIED — read all seven rows of the table.
- **Evidence:** H1 (Model 1) inference: "`Positive slope; insignificant under $t(16)$`"; H1 (Model 2): "`Positive slope; insignificant at 5\% ($t(14)$)`"; H2 (Model 2): "`Indistinguishable from zero under $t(14)$`"; H3: "`Downward shift; insignificant under $t(14)$`"; H4: "`Downward shift; insignificant under $t(14)$`". All five are the same formal decision (Fail to Reject, p > 0.05), yet H1/H3/H4 are described by the direction of their insignificant point estimates while H2 (Model 2) is described as indistinguishable from zero. (H2 Model 1 reads "`Insignificant under $t(16)$`" — neutral.)
- **Impact:** Would change wording only. Directional language attached to insignificant estimates ("positive slope", "downward shift") risks a reader carrying away the point-estimate direction as a finding. Use one neutral formulation for all Fail-to-Reject rows.

### D-06 — Table 4.8 "Below screen" verdict for Model 1 is true only for the substantive-regressor screen, whose threshold is not stated in Chapter IV
- **Location:** `src/thesis/chapters/chapter_04_results_and_discussion.tex`, Table `tab:t6_diagnostics`, lines 520–522 (rows) and 539 (note); narrative lines 545–546.
- **Severity:** Minor. **Revision scale:** Narrow. **Status:** VERIFIED — read the table, its note, the narrative, and Chapter III line 361, which states the threshold.
- **Evidence:** Table rows read "Model 1 VIF (EPS) … 1.16 … Below screen" and likewise BVPS. The table note (line 539) discloses: "VIFs are computed on the named substantive regressors only, excluding fixed-effect dummies. On the full fitted design … the VIFs are 5.70 (EPS) and 12.32 (BVPS) for Model~1 … the Model~1 'Below screen' verdict therefore applies only to the substantive-regressor screen, not to the fitted design." The threshold itself (VIF > 5) is stated only in Chapter III (line 361), not in Chapter IV — so a Chapter IV reader cannot tell from the table what "screen" means, and on the full fitted design Model 1 BVPS (12.32) exceeds the VIF > 5 threshold.
- **Impact:** Would change presentation, not a conclusion. The disclosure in the note is real and the narrative (lines 545–546) correctly says the VIFs "are screens … not pass/fail tests" and attributes imprecision partly to "design collinearity, not only the small sample". The residual risk is confined to a reader scanning the Assessment column. Fix: state the threshold in the table note and qualify the Model 1 cells (e.g. "Below screen (substantive regressors only)").

### D-07 — Two further significant correlations in Table 4.2 are never interpreted; the Spearman/normality note is thinner than its wording suggests
- **Location:** `src/thesis/chapters/chapter_04_results_and_discussion.tex`, Table `tab:t2_correlations` lines 103–129; interpretation lines 131–140.
- **Severity:** Minor. **Revision scale:** Narrow. **Status:** VERIFIED — read the table and the three interpretation bullets.
- **Evidence:** The table shows EPS–DPS "`0.612\textsuperscript{**}`" and ROA–DPS "`0.595\textsuperscript{**}`" (lines 118, 120), both significant at 1%. The text discusses only the MPS correlations, EPS–ROA (0.975) and EPS–BVPS (0.372). Neither DPS correlation is mentioned anywhere in §4.2.2, although the DPS correlations bear on R4 (adding DPS, line 475) and on the dividend discussion in §4.3.2. Separately, the table note says "the Shapiro-Wilk and Spearman checks are reported in the text", but the text reports Shapiro-Wilk only as p-values for MPS and DPS (line 140) and a single Spearman pair (EPS–BVPS, ρ = 0.295, p = 0.127); no W statistics appear in Chapter IV (they are in Appendix E line 503: W = 0.9246/0.9216).
- **Impact:** Would change completeness of reporting, not any conclusion. One sentence noting the EPS–DPS and ROA–DPS associations (and why they do or do not matter for R4) would close the gap.

### D-08 — Several numbers appear only as assertions in Chapter IV prose, with no table source in the chapter
- **Location:** `src/thesis/chapters/chapter_04_results_and_discussion.tex`, lines 475, 476, 479, 487, 594.
- **Severity:** Minor. **Revision scale:** Narrow. **Status:** UNVERIFIED — these numbers occur once in Chapter IV prose and in no Chapter IV table; I could not locate them in Appendix E either (checked `tab:app_robustfull` and `tab:app_robust_inf`); Chapter V repeats some of them, which is repetition, not independent verification. I did not re-estimate anything, so I take no position on whether they are correct.
- **Evidence:** (a) Line 475: interacted-DPS variant "joint regime-shift test is $F(2,12)=2.85$ ($p=0.097$)". (b) Lines 476, 479: R5/R6 implied-slope SEs and p-values (R5: 3.415 (SE 3.891, p = 0.401) and −2.081 (SE 1.969, p = 0.315); R6: 1.900 (SE 2.649, p = 0.490) and −1.809 (SE 1.357, p = 0.212)) — the point estimates are exact sums of the Table 4.6 coefficients (VERIFIED arithmetically), but their SEs/p-values are text-only. (c) Line 487: N = 30 re-inclusion F(2,16) = 4.762 (p = 0.024), stale-price Fs 3.870 (p = 0.043) and 3.821 (p = 0.044), and the N = 30 pre-period BVPS slope 0.709. (d) Line 594: FE-only R² of 93.9% and the classical bank-FE test F(4,16) = 2.23 (p = 0.112) — the HC3 version (1.395, p = 0.280) is printed in Appendix E `tab:app_fetests`, but the classical 2.23 appears nowhere else in the thesis I opened.
- **Impact:** Would change traceability, not any claim. A reader cannot check these numbers without re-running the analysis. Printing them in Appendix E (or citing the table that holds them) would close the gap.

### D-09 — Descriptive percentage changes are not reproducible from the printed Table 4.1 values
- **Location:** `src/thesis/chapters/chapter_04_results_and_discussion.tex`, lines 71–81 (bullets) vs Table `tab:t1_descriptives`, lines 43–81.
- **Severity:** Minor. **Revision scale:** Narrow. **Status:** UNVERIFIED / CANNOT DETERMINE from Chapter IV alone — recomputing the percentages from the table's two-decimal values does not reproduce four of the text's figures (arithmetic shown below); whether the text is right depends on unrounded inputs I did not re-audit. I take no position on correctness.
- **Evidence (my arithmetic on the printed rounded values):** EPS SD change (6.53−3.99)/3.99 = +63.66%, text says +63.95%; DPS SD change (2.97−3.56)/3.56 = −16.57%, text says −16.62%; ROA mean change (0.70−1.31)/1.31 = −46.56%, text says −46.38%; ROA SD change (0.44−0.22)/0.22 = +100.00%, text says +97.49%. By contrast the mean changes for MPS (−33.80% vs −33.81%), EPS (−40.11% vs −40.13%), BVPS (+2.44% vs +2.45%) and DPS (−76.90%) and the MPS SD change (−72.00%) do reproduce to rounding, and all coefficients of variation quoted (EPS 22.3%→61.0%, DPS 58.8%→212.2%, ROA 16.9%→62.2%) reproduce from the printed values.
- **Impact:** Would change traceability only; no conclusion turns on a 0.3–2.5 percentage-point difference in a descriptive change. The gaps are consistent with the percentages having been computed from unrounded data while the table prints two decimals (the table note does state the percentage-change formula). A footnote to that effect, or one extra decimal in the table, would remove the apparent discrepancy.

### D-10 — "These studies establish the EPS/BVPS price relationship" overstates two studies the thesis itself flags as circular
- **Location:** `src/thesis/chapters/chapter_04_results_and_discussion.tex`, line 658.
- **Severity:** Minor. **Revision scale:** Narrow. **Status:** VERIFIED — read line 658 and Chapter II lines 226, 295, and the synthesis-table rows for Almumani (2014) and Malhotra (2013).
- **Evidence:** Line 658: "These studies establish the EPS/BVPS price relationship in comparable markets, though neither tested whether value relevance changes across a consolidation regime." The two studies are Almumani (2014) and Malhotra (2013), both of which include the price-to-earnings ratio as a regressor — Chapter II lists both among the studies with "Circular P/E inclusion" (line 295 list; synthesis table rows, Ch. II lines 326–328) and Chapter IV itself (§4.3.4, line 645) treats P/E inclusion as "mechanical circularity and inflated statistical significance". The sentence notes the consolidation-regime limitation but not the circularity limitation that applies to the very relationship being "established".
- **Impact:** Would change wording, not a conclusion. "Are consistent with" plus a short P/E caveat would align the sentence with the thesis's own critique.

### D-11 — Definitive causal wording in the theory bullets ("forced", "widening standard errors")
- **Location:** `src/thesis/chapters/chapter_04_results_and_discussion.tex`, lines 634 and 636.
- **Severity:** Minor. **Revision scale:** Narrow. **Status:** VERIFIED — read both bullets and the contrasting "coincided with" wording in Chapter I (limitations) and Chapter V.
- **Evidence:** Line 634: "When regulatory capital constraints forced banks to eliminate cash dividends post-consolidation, the absence of this verification signal coincided with the attenuation of the earnings slope." "Forced" asserts a causal mechanism; the thesis elsewhere says only that guidelines "coincided with" dividend suspensions (Ch. IV line 614; Ch. I), and no evidence in Chapter IV shows constraints forcing elimination. Line 636: "When market participants cannot independently verify loan portfolio quality, they discount reported accounting metrics, widening standard errors and attenuating valuation slopes." Investor discounting cannot widen an estimator's standard errors — standard errors are a property of the sample and estimator, not of investor behaviour; the sentence conflates a pricing claim with a statistical one.
- **Impact:** Would change wording, not any conclusion. Both bullets are otherwise properly framed as theory (the section's purpose), and §4.3.2's lead (line 610) already says the patterns are "not … proven causal effects".

### D-12 — No detectable-effect / power statement in Chapter IV
- **Location:** Absence in `src/thesis/chapters/chapter_04_results_and_discussion.tex` (whole chapter searched for "power", "MDE", "detectable" — only hit is the unrelated "Goodness of Fit" discussion of R²); contrast Chapter V, §5.2.3 closing paragraph.
- **Severity:** Suggestion. **Revision scale:** Narrow. **Status:** VERIFIED — searched the chapter text for power/MDE/detectable-effect language and found none; Chapter V states approximate detectable effects of 10.73 NPR (Model 2 pre-period EPS slope), 12.06 NPR (EPS interaction) and 3.71 NPR (BVPS interaction).
- **Evidence:** Chapter IV reports six non-rejections and repeatedly stresses imprecision, but never states what magnitude of effect the design could detect. A Chapter IV-only reader therefore cannot judge whether "fail to reject" means "no effect" or "effect smaller than the design can see".
- **Impact:** Would strengthen interpretation, not change any conclusion. One sentence in §4.2.4 or §4.2.5 carrying the Chapter V detectable-effect figures would close it.

### D-13 — Figure file names are non-sequential relative to presentation order (cosmetic)
- **Location:** `src/thesis/figures/` vs `src/thesis/chapters/chapter_04_results_and_discussion.tex` lines 86–563.
- **Severity:** Suggestion. **Revision scale:** Narrow (rename files or leave as-is). **Status:** VERIFIED — listed the figures directory and the include order.
- **Evidence:** Presentation order is F6 (trends), F1 (scatter), F2 (heatmap), F3 (value relevance), F4 (forest), A2 (robustness forest), F5 (diagnostics). Compiled figure numbers follow LaTeX order of appearance and are therefore sequential and correct; only the underlying file names are out of order.
- **Impact:** None on the compiled thesis. Noted only so the file-naming is not mistaken for a numbering error.

---

## 4. Verified strengths (in scope)

- **S-01 — Covariance sensitivity is shown, not withheld.** Table `tab:cov_sensitivity` (lines 437–469) prints all five estimators for all eight joint tests, and its note states the key fact plainly: "Under the classical, HC0, HC1 and HC2 covariances, all eight joint tests R2–R9 reject at 5%; under HC3, only R6 rejects." The prose (§4.2.5 line 391–392; §4.2.6 note line 468) repeats it, and the HC3 column was verified to reproduce Table 4.6 exactly. The baseline non-rejection is thereby presented as estimator-specific in Chapter IV itself. How verified: read every cell of Table 4.7 and compared its HC3 column with Table 4.6.
- **S-02 — R6 is handled as a sensitivity finding in Chapter IV prose, three times over.** Line 478 (unadjusted p = 0.021; Holm p = 0.169; leave-one-bank collapse; "does not provide multiplicity-adjusted evidence"), lines 664–669 (§4.3.5: "not significant after Holm adjustment … reported as an association across calendar regimes, not as a causal merger effect"), and lines 676–677 (closing summary). How verified: read all three passages.
- **S-03 — The degenerate four-row R6 variant is disclosed.** Lines 477–478 state that dropping only the four mismatched rows gives numerically identical estimates but is "numerically degenerate for inference" (leverage 1.0, residual ≈ 0, year-dummy SEs ≈ 205) and that "the covariance matrix in that variant is not reliable". How verified: read the passage.
- **S-04 — The wild-cluster bootstrap is reported as mechanically forced, not as evidence.** Line 485: "With 32 patterns the smallest attainable $p$-value is $2/32 = 0.0625$, so this bootstrap cannot produce a 5% rejection for any specification; the R6 flip is therefore mechanically forced, not evidence about cluster-robust inference. The check is inconclusive at $G = 5$." How verified: read the passage.
- **S-05 — R7 is described honestly as a one-sided rescaling.** Line 480: "the BVPS slope rises from 0.100 to 0.153 and the joint $F$ falls by about 20%; the check is therefore a one-sided rescaling of BVPS, not a full bonus-dilution adjustment". The 20% figure checks arithmetically ((2.365−2.954)/2.954 = −19.9%). How verified: read the passage and checked the arithmetic.
- **S-06 — Price-window sensitivities disclose the unresolved discrepancy.** Line 487 reports both stale-price pairs (487/453 dated 12 May 2021; 484/460 dated 13 May 2021), calls them "stale-price scenarios, not observations meeting the five-day rule", and states the missingness mechanism "cannot be established from these cases". The 487/453 pair is corroborated in Appendix D line 188 (dataset boundaries). How verified: read line 487 and Appendix D line 188.
- **S-07 — VIF scope and design collinearity are disclosed in the table note and narrative.** Table 4.8 note (line 539) prints the full-design VIFs (Model 1: 5.70/12.32; Model 2: 14.82/12.46/27.34/259.32; largest year-dummy VIF 118.21) and the narrative (lines 545–546) attributes imprecision to "design collinearity, not only the small sample". How verified: read the note and narrative (residual issue is only the unqualified "Below screen" cell — see D-06).
- **S-08 — Both Breusch–Pagan variants are reported and their conflict is not hidden.** Table 4.8 (Koenker LM 14.37, p = 0.213, "Not rejected"; classical LM 28.18, p = 0.003, "Rejected") and line 546: "The diagnostic conclusion therefore depends on the variant. HC3 is used for inference, but it does not establish constant variance or guarantee small-sample validity." How verified: read table and narrative.
- **S-09 — Non-rejection is never written as proof of no effect in the hypothesis section.** §4.2.5 (lines 377–392) consistently uses "fails to reject the null hypothesis", and the BVPS discussion (line 288, repeated line 380–383) states the wide CI means the study "cannot establish whether book value had a negligible, positive, or negative association". No sentence in Chapter IV asserts that a null is proven. How verified: read §4.2.5 in full and searched the chapter for "prov*" language (only hit is line 610, "not as proven causal effects").
- **S-10 — Generalisation is bounded.** Chapter I limitations (read for context) state the five-bank sample "cannot be generalized to the entire commercial banking industry"; Chapter IV §4.3.5 (line 669) and the closing summary (lines 676–677) report results "as an association across calendar regimes, not as a causal merger effect" and state "These analyses do not establish a causal merger effect." How verified: read the passages.
- **S-11 — Literature summaries in §4.3.4 match Chapter II.** Chaudhari (2025) (Ch. IV line 653 vs Ch. II line 271: EPS/DPS positive, ROA negative, inflation p = 0.037, interest/GDP insignificant); Pant (2024) (line 654 vs Ch. II line 269: BVPS negative, insignificant); Timalsina (2026) (line 655 vs Ch. II line 277: EPS/DPS/P/E/size/inflation positive, interest negative); Almumani (2014)/Malhotra (2013) (line 658 vs Ch. II line 226: r = 0.84 for Almumani); Kwon (2020) (lines 621–627 vs Ch. II lines 107–112, 224: earnings relevance declines, book value anchors); Bhattarai (2014)/Joshi (2023) sample sizes (line 648 vs Ch. II lines 235, 254: 9 banks 2006–2014; 7 banks 2012/13–2021/22); Ohlson equation (line ~629 vs Ch. II lines 51–52: same residual-income formula up to notation, R = 1 + r). Bibliography entries exist for all works cited in §4.3.3–4.3.4 (checked in `src/thesis/references.bib`: kwon2020, bhattacharya1979, john1985, morgan2002, flannery2004, chaudhari2025, pant2024, timalsina2026, almumani2014, malhotra2013). How verified: read each passage in both chapters and grepped the bibliography.
- **S-12 — Figure 4.4 (value relevance) visually matches its caption.** I opened `src/thesis/figures/F3_value_relevance.png`: two panels (MPS vs EPS; MPS vs BVPS), blue pre-consolidation and orange post-consolidation points with fitted lines and shaded bands, n = 28. The post-consolidation BVPS line is approximately flat in the raw scatter, consistent with the caption note that the negative implied post slope (−1.658) is the fixed-effects estimate, not the bivariate fit ("the post-BVPS sign difference is the effect of absorbing year effects"). How verified: visual inspection of the PNG.
- **S-13 — Chapter I front-loads the same numbers Chapter IV reports.** Chapter I line 17 reports EPS 2.095 (p = 0.616), BVPS 0.219 (p = 0.908), δ_E −3.124 (p = 0.448), δ_B −1.758 (p = 0.175), joint F(2,14) = 2.954 (p = 0.085), R6 F(2,10) = 5.818 (p = 0.021), Holm p = 0.169 — all identical to Chapter IV. (Whether front-loading results in Chapter I is desirable is a style question outside this review's scope; the numbers agree.) How verified: read Ch. I line 17 and compared each figure with Chapter IV.

---

## 5. Claims register (substantive interpretive claims in Chapter IV)

| # | Claim (location) | Evidence in the thesis | Assessment |
|---|---|---|---|
| C-01 | No statistically significant EPS/BVPS association in Model 1 (§4.2.3, lines 211–215) | β_E p = 0.616, β_B p = 0.908 (Tab. 4.3); consistent across abstract/Ch. I/Ch. V | Supported |
| C-02 | No significant pre-consolidation slopes in Model 2 (§4.2.4, lines 286–288) | p = 0.140 / 0.940, wide CIs (β_E CI [−2.059, 13.213]) | Supported; text correctly refuses to infer "no association" |
| C-03 | No significant individual regime shifts (§4.2.4, lines 290–291; §4.2.5) | δ_E p = 0.448, δ_B p = 0.175; joint F p = 0.085 | Supported as non-rejections |
| C-04 | Baseline joint test is "suggestive rather than conclusive" (line 308) | p = 0.085 under HC3; rejects under four other covariances (Tab. 4.7) | Supported, and the estimator-dependence is shown |
| C-05 | R6 is a sensitivity finding, not multiplicity-adjusted evidence (lines 478–479, 664–669) | Holm p = 0.169; leave-one-bank p = 0.329–0.572; R5 at same n/df does not reject | Supported in prose; table presentation lags (D-01) |
| C-06 | Earnings-slope attenuation is "consistent with" asset-quality/provisioning pressure (§4.3.2, line 612) | No NPL/provisioning/macro variable estimated; text flags "hypothesis, not a finding" | Hypothesis only, correctly labelled; specific drivers unsourced (D-12) |
| C-07 | Capital expansion / share supply diluted per-share metrics (§4.3.2, line 613) | Mean EPS fell 40.13% (Tab. 4.1); amalgamations expanded equity base (Ch. I) | Descriptive facts support the premise; the pricing inference ("may have factored") is hedged |
| C-08 | Dividend cessation removed an observable cash-flow signal (§4.3.2, line 614; §4.3.3, line 634) | DPS mean fell 76.90%; 12 of 15 post = 0 (App. B) | Facts supported; valuation-role inference contradicted by DPS–price r = 0.082 (D-02) |
| C-09 | Book value did not assume the anchoring role Kwon predicts (§4.3.3, lines 625–627) | Implied post BVPS −1.658, p = 0.161 | Supported as a non-finding ("does not establish whether book value served as an asset anchor") |
| C-10 | Prior Nepalese studies' significance partly reflects P/E circularity and omitted year effects (§4.3.4, lines 643–648) | P/E circularity demonstrated in Ch. II (§2.2.6, line 295 list); pooled-vs-FE comparison in Tab. 4.9 (pooled EPS 4.882, p = 0.128 — itself insignificant) | Partly supported; the text itself concedes the pooling explanation "is not established by this study's comparison" |
| C-11 | The 5-day rule / BAFIA anchor reduces date-selection ambiguity but does not verify release dates (§4.3.5, lines 671–673) | Ch. I/Ch. II: release dates verified for only 2 of 30 bank-years | Supported; correctly qualified |
| C-12 | "The estimated slopes are consistent with lower earnings and book-value associations after consolidation" (lines 676–677) | Point estimates lower in both cases; CIs include no change and increases | Literally true ("consistent with") but weak; the sentence immediately adds the imprecision and non-rejection caveats |

---

## 6. Open questions (outside Chapter IV, noted not decided)

1. **Institutional requirements:** No outcome categories or pass/fail criteria for Chapter IV were found in the repo beyond the TU Guidelines' Chapter IV prescription (Results then Discussion; report test statistics with degrees of freedom; interpret against theory and prior studies with care for bias, imprecision and sample size). I therefore applied no external grading rubric. Whether the thesis meets any additional faculty/campus-specific requirement was not determined.
2. **Prabhu–Century exclusion:** Chapter I (§1.1) lists five combinations commencing joint operations in Jan–Feb 2023, of which the sample covers four plus unmerged NMB. Chapter IV does not address why the fifth (Prabhu–Century) is excluded; that rationale, if it exists, lives in Chapter III/sample design, outside this review's scope.
3. **Figure content:** Six of seven figures were checked for caption/reference/numbering only; their plotted content was not visually verified (see §1.3 and Verification log).
4. **Unrounded data:** Percentage changes that do not reproduce from the printed two-decimal table (D-09) and the text-only numbers (D-08) could not be settled from the thesis text alone; settling them would require the unrounded analysis output, which this review did not re-audit by design.

---

## 7. Verification log

**Files read in full during this task:**
- `src/thesis/chapters/chapter_04_results_and_discussion.tex` (677 lines, all sections, tables, figures, notes)
- `src/thesis/front/abstract.tex` (23 lines)
- `src/thesis/chapters/chapter_01_introduction.tex` (203 lines; results paragraph line 17 used for cross-checks; remainder read for context on hypotheses, limitations and the Prabhu–Century question)
- `src/thesis/chapters/chapter_05_summary_and_conclusion.tex` (249 lines; §§5.2.3–5.3 and decision table used for cross-checks)
- `docs/thesis_review/v1/data_analysis_review.md` (read to know what v1 established; not used as evidence — every finding above re-checks the current working-tree text)
- `docs/thesis_review/v2/pass_a_note.md` (read; its questions were used as prompts to check, not as evidence)

**Files read in part (targeted passages only):**
- `src/thesis/chapters/chapter_02_literature_review.tex` — Ohlson (lines 23–70), Kwon (107–112, 224), signalling/opacity (137–139), P/E circularity (295, 396), Bhattarai (235, 298), Joshi (254), Pant (269), Chaudhari (271), Timalsina (277), synthesis table (322–370), research gap (392–404)
- `src/thesis/chapters/chapter_03_research_methodology.tex` — VIF threshold (line 361) only, via targeted search
- `src/thesis/appendices/appendix_b.tex` — dataset table (all 30 rows; DPS zeros counted; extreme-value attributions checked)
- `src/thesis/appendices/appendix_e.tex` — `tab:app_robustfull` (lines 148–183), `tab:app_robust_inf` R3–R6 rows, `tab:app_fetests` (line 118: 1.395), `tab:app_sensitivity` note (line 587: joint p range 0.035–0.291), flagged-observations note (line 497), Shapiro–Wilk note (line 503)
- `src/thesis/appendices/appendix_d.tex` — line 188 (delayed-price boundaries 487/453) only, via targeted search
- `src/thesis/references.bib` — existence of entries for works cited in §4.3.3–4.3.4 (kwon2020, bhattacharya1979, john1985, morgan2002, flannery2004, chaudhari2025, pant2024, timalsina2026, almumani2014, malhotra2013), via targeted search
- `src/thesis/figures/F3_value_relevance.png` — visually inspected
- `src/thesis/figures/` — directory listing confirming all seven included PDFs (and PNGs) exist

**Sources consulted (external):**
- Faculty of Management, Tribhuvan University, *Master's Degree Dissertation Guidelines* (2019), repo copy `docs/thesis_guidelines_reference/01_TU-FOM_Masters-Dissertation-Guidelines-2019.pdf`, **pp. 14–15 fully read** (via `pdftotext -f 14 -l 15`). Used only for the Chapter IV structural prescription quoted in §1.1. No URL is given because the source used was the repo-local copy; no other external source was opened, and no external claim in this review rests on a snippet.

**What I could not do and why:**
- Did not re-audit the statistics (no code run, no re-estimation, no p-value recomputation from raw data) — outside the assigned scope, which is whether the text reports and interprets the analysis consistently.
- Did not visually verify six of seven figures' plotted content — only `fig:value_relevance` was opened as an image; the rest were checked for existence, caption, note and in-text reference.
- Did not compile or build the thesis (forbidden by the task), so compiled table/figure numbers, cross-reference resolution and page layout were not verified — numbering consistency was assessed from source order and LaTeX auto-numbering.
- Did not verify the four percentage changes in D-09 or the text-only numbers in D-08 against unrounded data — they are not reproducible from the printed thesis text, and re-audit was out of scope.
- Did not check plagiarism, authorship, or AI-tool use — out of scope by instruction.
- Did not read anything under `~/workspace/review-audit-scratch/`.

**Arithmetic performed (scratch, /tmp only; no repo files touched):** percentage changes and coefficients of variation from Table 4.1 printed values; t = coefficient ÷ SE for all Model 1/Model 2 coefficients; implied slopes as coefficient sums; R7 joint-F change (−19.9%); R6 critical-value framings (29.5% decrease / 41.8% above, both consistent with F-critical ≈ 4.103); bivariate VIF from r = 0.975 (20.4); 95% CI spot-checks from coefficients, SEs and t-critical values. All scratch work was done in the shell/`/tmp`; no scratch files were left in the repo.

**Counts:** 13 findings (D-01–D-13): 2 Major, 8 Minor, 3 Suggestion. 0 Critical. 13 verified strengths (S-01–S-13). Claims register: 12 claims.

## 8. Final check — repository state

`git status` was run in `~/workspace/verbose-chainsaw` after this file was written (17 Nov 2026, ~21:26 NPT). Result:

- **The only file created by this review is `docs/thesis_review/v2/review_ch4_results.md`.** No repo file was modified, renamed, deleted or reformatted by this review; the thesis was not built or compiled; all scratch arithmetic was done in the shell/`/tmp`.
- The `git status` output shows the same set of modified (`M`) files that was present at the start of this task (pre-existing uncommitted working-tree changes, including to `src/thesis/chapters/chapter_04_results_and_discussion.tex` itself) — none of those modifications are mine.
- Two other files exist in `docs/thesis_review/v2/` alongside mine (`review_ch5_back.md`, `review_front_ch1.md`, both timestamped 15:26 UTC on 17 Nov 2026). They were **not** created by this review: at the start of this task the directory contained only `pass_a_note.md`. They appeared during this task's window and are evidently parallel reviewers' outputs for other chapters. This review created nothing else in the repo.
