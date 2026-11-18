# Independent content review — Chapter V + Appendices B, C, E (v2)

**Thesis:** Value relevance of accounting information (EPS, BVPS) across the 2023 Nepalese
commercial banking consolidation wave (MBS dissertation, Tribhuvan University, Faculty of
Management).
**Repo:** `~/workspace/verbose-chainsaw`. **HEAD:** `2b4e10f` (2026-11-14, "Add independent
data-analysis review (v1)"). **Version reviewed:** the working tree as it stands, including
uncommitted changes (see §12). **Review date:** 17 November 2026.
**Reviewer role:** independent examiner, read-only. No repo file was modified, renamed,
deleted, or reformatted; no build or compilation was run.

**Scope.** In full: `src/thesis/chapters/chapter_05_summary_and_conclusion.tex` (Ch5, 249
lines), `src/thesis/appendices/appendix_b.tex` (86 lines), `src/thesis/appendices/appendix_c.tex`
(23 lines), `src/thesis/appendices/appendix_e.tex` (620 lines), and
`src/thesis/generators/appendix_e/appendix_e_prose.tex` (53 lines, generator template for
Appendix E). For bookend/traceability checks only: `src/thesis/chapters/chapter_01_introduction.tex`
(203 lines) and `src/thesis/front/abstract.tex` (23 lines). Cross-check sources:
`src/thesis/chapters/chapter_04_results_and_discussion.tex` and
`src/thesis/chapters/chapter_03_research_methodology.tex` (both read in full);
`src/thesis/chapters/chapter_02_literature_review.tex` (consulted by targeted search only,
not read in full); `src/thesis/front/abbreviations.tex` (read in full);
`src/thesis/appendices/appendix_d.tex` (consulted by targeted search only);
`data_analysis/analysis/outputs/tables/A6_analysis_dataset.md` (consulted once, to check a
number — see E-14). The only prior review I was permitted to read
(`docs/thesis_review/v1/data_analysis_review.md`) was **not** read; nothing in
`~/workspace/review-audit-scratch/` was read. Every finding below comes from a file I opened
during this task.

**Status vocabulary (used exactly once per finding).** VERIFIED = I read the text, opened the
source, or cross-checked the locations named. INFERRED = the basis is stated and the claim
goes beyond what was directly observed. UNVERIFIED / CANNOT DETERMINE = I could not do the
check, and why is stated. Plagiarism checking is **not** covered by this review.

## Verdicts (exactly one each)

| Item | Verdict |
|---|---|
| (i) Chapter V (Summary, Conclusion, and Implications) | **Ready with minor revisions** |
| (ii) Appendices B, C, E together | **Ready with minor revisions** |

*Rationale in one line each.* (i) Every conclusion I traced follows from the Ch4 evidence it
rests on, the null results are reported honestly with their exact p-values and the HC3
dependence stated, and the implications are conspicuously hedged; the one Major finding
(E-01) is a narrow omission — a limitations paragraph — not a defect in any conclusion.
(ii) Appendix B reproduces the analysis dataset completely and consistently, and Appendix E
is a thorough, internally consistent audit record; the revisions needed are a body pointer
and corrected framing for Appendix C (E-05), a notation fix (E-07), and small completeness
notes (E-06, E-08).

## 1. Traceability matrix

### 1.1 Research questions (Ch1 → Ch5)

| RQ (Ch1) | Ch1 location | Answered in Ch5 | Ch5 location | Assessment |
|---|---|---|---|---|
| RQ1: Are EPS and BVPS associated with post-reporting-deadline prices ($MPS^{RD}$)? | `chapter_01_introduction.tex`, line 44 | Yes — direct answer: no statistically significant association (EPS p = 0.616; BVPS p = 0.908) | §5.3.1, line 117 | VERIFIED. Matches Ch4 Table `tab:t3_model1` and App E Table `tab:app_m1full`. |
| RQ2: Did EPS/BVPS associations differ pre- vs post-consolidation? | Ch1, line 46 (see note below) | Yes — direct answer: interactions negative but insignificant; joint test F(2,14) = 2.954, p = 0.085, fail to reject at 5% | §5.3.1, line 118; §5.3.2, line 123 | VERIFIED. Matches Ch4 Table `tab:t4_model2` and App E Table `tab:app_m2full`. |
| RQ3: Are baseline and interaction findings robust to alternative specifications? | Ch1, line 46 | Yes — direct answer: sensitivity-dependent; only unadjusted R6 rejects (F(2,10) = 5.82, p = 0.021; Holm-adjusted p = 0.169) | §5.3.1, line 119; §5.2.3, lines 97–102 | VERIFIED against Ch4 Table `tab:t5_robustness` and App E Table `tab:app_robustfull`. See E-02: the RQ3 wording as restated in Ch5 (§5.2.1, line 33) omits the Kanchan sensitivity (R9). |

Note on RQ2/RQ3 Ch1 locations: Ch1 states RQ2 and RQ3 in the problem-statement list; the
grep I ran located RQ3 verbatim at Ch1 line 46 ("Are the baseline and consolidation-interaction
findings robust to alternative operating profitability specifications, inclusion of eligible
dividend disclosures, adjustment for bonus share capitalization, retrospective earnings
restatements, and the econometric exclusion of structural transition periods?"). RQ2 is the
item immediately preceding it in the same list. I read the full Ch1 file; the RQ wordings
above are quoted from it.

### 1.2 Specific objectives (Ch1 §"Objectives of the Study", lines 52–76 → Ch5)

| Specific objective (Ch1) | Ch5 coverage | Assessment |
|---|---|---|
| (i) Estimate baseline value relevance of EPS/BVPS in two-way FE framework | §5.2.1, line 36 (objective (i)); §5.2.3 Model 1 bullet; §5.3.6 H1/H2 | VERIFIED — answered. |
| (ii) Test whether slopes differed pre/post via δ_E, δ_B and joint Wald test | §5.2.1, line 36 (objective (ii)); §5.2.3 Model 2 bullets; §5.3.6 H3/H4/joint | VERIFIED — answered. |
| (iii) Evaluate robustness across 7 variants: ROA substitution; DPS inclusion; exclude FY 2079/80 (transition); exclude FY 2078/79 (entity-timing); bonus-adjusted metrics; restated EPS; exclude NMB FY 2076/77 (Kanchan) | §5.2.1, line 36 (objective (iii), "nine-specification suite R1–R9"); §5.2.3 robustness bullets, lines 97–102 (all seven named, with R4/R9 df = 13) | VERIFIED — answered for all seven. Note the asymmetry: the *objectives* paragraph in Ch5 covers all seven, but the *RQ3* restatement in the same subsection (line 33) names only six and omits Kanchan (E-02). |

### 1.3 Hypotheses (aim → hypothesis → where addressed → result → conclusion)

All hypotheses are two-tailed at α = 0.05 (Ch1, §"Hypotheses of the Study"). Ch5 §5.3.6,
Table `tab:hyp_decisions` (lines 138–166) plus the itemised decisions (lines 168–178):

| Hypothesis | Ch1 null | Addressed (Ch4) | Result reported in Ch5 | Decision in Ch5 | Conclusion drawn | Assessment |
|---|---|---|---|---|---|---|
| H1: EPS relevance | H₀: β_E = 0 (Model 1) | Ch4 §4.2.3, Table `tab:t3_model1`; §4.2.5, Table `tab:hypotheses` | Model 1: 2.095 (SE 4.096), p = 0.616; Model 2 pre: 5.577 (3.560), p = 0.140 | Fail to Reject H₀ | "Accounting earnings do not exhibit a statistically significant association … in the two-way fixed-effects specification" (§5.3.6, line ~170) | VERIFIED. Numbers match Ch4 and App E Tables `tab:app_m1full`/`tab:app_m2full` exactly (2.0948/5.5771 at 4dp). |
| H2: BVPS relevance | H₀: β_B = 0 (Model 1) | Ch4 §4.2.3, §4.2.5 | Model 1: 0.219 (1.858), p = 0.908; Model 2 pre: 0.100 (1.306), p = 0.940 | Fail to Reject H₀ | "Book value per share exerts no statistically significant incremental pricing effect" (§5.3.6, line 174) | VERIFIED on numbers. Language note: "exerts" is a causal verb in an otherwise associational thesis — see E-13 (Suggestion). |
| H3: EPS regime shift | H₀: δ_E = 0 (Model 2) | Ch4 §4.2.4, Table `tab:t4_model2`; §4.2.5 | −3.124 (4.003), p = 0.448 | Fail to Reject H₀ | "The individual compression in the earnings valuation slope … is not statistically significant" | VERIFIED. |
| H4: BVPS regime shift | H₀: δ_B = 0 (Model 2) | Ch4 §4.2.4, §4.2.5 | −1.758 (1.231), p = 0.175 | Fail to Reject H₀ | "The individual shift in the book value valuation slope is not statistically significant" | VERIFIED. |
| Joint (composite) | H₀: δ_E = δ_B = 0 | Ch4 §4.2.4, Table `tab:t4_model2`; §4.2.6, Table `tab:cov_sensitivity` | Baseline F(2,14) = 2.954, p = 0.085; R6 (sensitivity) F(2,10) = 5.818, p = 0.021 unadjusted, Holm-adjusted p = 0.169 | Fail to Reject H₀ (baseline); "Reject H₀ (unadjusted; sensitivity only)" for R6 | "The evidence for a regime shift is therefore sensitivity-dependent and not conclusive" (§5.3.6, line 177) | VERIFIED on numbers. Presentation note: the table gives opposite decisions for the same joint null in adjacent rows — see E-04. |

**No aim without an answer, and no conclusion without support, was found in Ch5.** Every
conclusion in §5.3 traces to a Ch4 result cited above. The one structural gap is E-01
(limitations not restated), not an unsupported conclusion.

## 2. Abstract bookend check

Read `src/thesis/front/abstract.tex` in full (23 lines) and checked each substantive claim
against the body:

- "both earnings (β_E = 2.095, p = 0.616) and book value (β_B = 0.219, p = 0.908) exhibit
  positive but statistically insignificant slopes (R² = 0.948)" — VERIFIED: Ch4 Table
  `tab:t3_model1`; Ch5 §5.2.3 and §5.3.6.
- "pre-consolidation earnings slope … 5.577, p = 0.140 … implied slopes to 2.453 for EPS
  (p = 0.298) and −1.658 for BVPS (p = 0.161)" — VERIFIED: Ch4 Table `tab:t4_model2`;
  Ch5 §5.2.3; App E Table `tab:app_m2full` note (2.4534, p = 0.298; −1.6576, p = 0.161).
- "baseline joint Wald test fails to reject … (F(2,14) = 2.954, p = 0.085), a result
  specific to that estimator" — VERIFIED: Ch4 Table `tab:cov_sensitivity` (all eight joint
  tests R2–R9 reject at 5% under classical/HC0/HC1/HC2, only R6 under HC3); Ch5 §5.2.3.
- "purging the entity-timing asymmetry in Specification R6 (N = 23) yields a statistically
  significant joint test (F(2,10) = 5.82, p = 0.021, unadjusted; Holm-adjusted p = 0.169
  across eight tests)" — VERIFIED: Ch4 §4.2.6 and Table `tab:t5_robustness`; Ch5 §5.2.3.
- "The study provides policy implications for regulatory asset quality reviews, trading halt
  limits, and centralized electronic corporate filings" — VERIFIED: all three appear in
  Ch5 §5.4/§5.5 (AQR bullet §5.4; trading-suspension bullets §5.4 and §5.5; centralised
  portal bullets §5.4 and §5.5).
- **One wording gap (E-11, Minor):** "with post-merger capital dilution coinciding with
  compressed implied slopes rather than book-value substitution" (abstract, line 17). The
  body (Ch5 §5.3.3, lines 125–127) says of the theoretical substitution that "these data
  do not establish whether this theoretical substitution occurred or how market participants
  treated expanded book equity" — i.e. the body does not rule substitution out, while the
  abstract's "rather than book-value substitution" can be read as ruling it out. The
  "capital dilution" half is a fair summary of Ch4 §4.3.2 ("Capital Expansion and Share
  Supply"), which is itself hedged as a plausible mechanism.
- **No abstract claim was found that appears nowhere in the body.** Keywords (Value
  Relevance, Commercial Banks, Bank Consolidation, Ohlson Model, Two-Way Fixed Effects)
  all reflect body content.

## 3. Chapter V evaluation

### 3(a) Do the conclusions follow from the evidence?

Yes — checked conclusion-by-conclusion against Ch4 (see §1.3 and the claims register in
§7). Spot checks beyond the hypothesis table:

- Descriptive claims in §5.2.3 (lines 71–76) were **recomputed from the 30 rows printed
  in Appendix B** with a Python script (`/tmp/check_stats.py`, sample SD, ddof=1): MPS mean
  −33.81%, SD −72.00%; EPS mean −40.13%, SD +63.95%, CV 22.3%→61.0%; DPS mean −76.90%,
  SD −16.62%, CV 58.8%→212.2%, post median 0, 12 of 15 zeros; BVPS mean +2.45%,
  SD −15.31% (thesis prints −15.30%, a 0.01pp rounding difference); full-sample MPS mean
  254.34. **All VERIFIED** to the printed precision. Correlations: EPS–ROA r = 0.9745
  (thesis 0.975), VIF ≈ 19.83 (thesis ≈ 20); EPS–BVPS r = 0.3718 (thesis 0.372,
  p = 0.051 as reported in Ch4); MPS–DPS r = 0.0818 (thesis 0.082, p = 0.679). VERIFIED.
- "The observed F is 41.8% above the 5% critical value" (§5.3.5, line 132): VERIFIED by
  computation — scipy `F(2,10)` 5% critical value = 4.1028; 5.818/4.1028 − 1 = 41.8%.
  The companion Ch4 statement ("a 29.5% decrease … would remove the raw rejection") is
  the same arithmetic from the other side (1 − 4.1028/5.818 = 29.5%). VERIFIED.
- "In the R6 sample, dropping any single bank leaves the joint test far from rejection
  (F = 0.615–1.309, p = 0.329–0.572)" (§5.2.3, line 102): VERIFIED — identical range in
  Ch4 §4.2.6 (R6 bullet).
- "Including the two delayed observations changes the baseline joint test to
  F(2,16) = 4.762 (p = 0.024)" (§5.3.5, line 132): VERIFIED — Ch4 §4.2.6 and §4.3.5.
  The two stale-price scenarios ($487/453$ → F = 3.870, p = 0.043; $484/460$ →
  F = 3.821, p = 0.044) also match Ch4 §4.2.6 verbatim. VERIFIED.
- "A wild-cluster bootstrap … gives p = 0.062 for both the baseline and R6" (§5.3.5,
  line 132): VERIFIED as a faithful repeat of Ch4 §4.2.6 ("0.062 (2 of 32 patterns)").
  I did **not** recompute the bootstrap; the thesis's own arithmetic (smallest attainable
  p = 2/32 = 0.0625) is correctly stated. Rounding note: 2/32 = 0.0625, reported as 0.062
  — see E-10 (Suggestion).
- "with year effects only, the earnings slope is 2.185 (SE 1.260, p = 0.098), and adding
  bank effects raises its standard error to 4.096" (§5.2.3): VERIFIED against Ch4 Table
  `tab:spec_comp` (Year FE + EPS/BVPS: 2.185 (1.260), p = 0.098; Two-Way FE: 2.095
  (4.096), p = 0.616).
- Post hoc design-sensitivity thresholds (§5.2.3, line 108: 10.73 / 12.06 / 3.71 NPR):
  VERIFIED as a repeat of Ch3 §"Econometric Estimation…" and Ch1/Ch4 statements of the
  same figures; I did not recompute the power arithmetic from the HC3 standard errors.
  The framing ("not observed-power estimates"; "do not rule out effects smaller than
  those magnitudes") is correct and honest.

### 3(b) Interpretation, linkage to questions and literature

- Ch5 interprets rather than restates: §5.3.2–§5.3.5 explicitly refuse the readings the
  point estimates invite ("do not establish earnings dominance, a decline in either
  slope, or a negative book-value association", line 123; "Results are reported as
  associations across calendar periods, not as an established causal merger impact",
  line 123). VERIFIED.
- Literature linkage: §5.2.1 and §5.3.3 link back to Ohlson (1995), Feltham & Ohlson
  (1995), Collins et al. (1997) and Kwon & Wang (2020). I confirmed via targeted search
  that Ch2 treats all of these substantively (Ohlson RIV framework, Ch2 line 23;
  Collins 1997 forty-one-year panel, Ch2 lines 115, 222; Kwon 2020 post-merger framework,
  Ch2 lines 107, 224) and that the Nepalese studies named in Ch5 §5.2.1
  (Chaudhari 2025, Chhetri 2023, Timalsina 2026, Gurung & Dahal 2025) are reviewed in
  Ch2 (lines 250, 271, 273, 277). The Ch5 claim that "almost all published Nepalese
  studies employed static, full-sample pooled or one-way random-effects regressions"
  matches Ch2's synthesis (line 301: "almost all existing studies estimate static,
  full-period average coefficients"). VERIFIED (by search, not full read of Ch2).
- The one literature-facing overstatement risk is the abstract's (E-11), not Ch5's own text.

### 3(c) Implications — supported or overreaching?

I read §5.4 (lines 180–221) and §5.5 (lines 222–249) in full. The implications are
**unusually well hedged for a null-result thesis**, and each risky recommendation is
explicitly fenced. Representative exact wording:

- "The imprecise point estimates suggest a downward compression in the earnings slope
  and no positive book value pricing anchor post-consolidation. Whether this coincides
  with market caution regarding the asset quality of merged commercial banks is a
  hypothesis: no asset-quality variable is estimated in this study." (§5.4, NRB/AQR bullet)
- "the imprecise estimates do not establish that horizontal amalgamations were accompanied
  by substantial earnings transitoriness — no transitoriness parameter was estimated — or
  by an attenuation of the valuation slopes, since neither interaction is statistically
  significant." (§5.4, consolidation-policy bullet)
- "The sharp reduction in cash dividend distributions post-consolidation removed an
  observable cash flow signal for bank equities, though DPS was never shown to anchor
  valuation (its correlation with price is r = 0.082, p = 0.679)." (§5.4, dividend bullet)
- "this study does not establish that current reporting is non-uniform, so the
  recommendation rests on transparency grounds rather than on a documented deficiency."
  (§5.4, NFRS restatement bullet)
- "Given that the recovery performance, provisioning coverage, and write-offs of acquired
  legacy loan portfolios are unmeasured in this study and therefore an acknowledged
  evidence gap, Nepal Rastra Bank could consider mandating …" (§5.5, policy bullet 1)

**Assessment: no overreach found.** The recommendations that are stated flatly are the
ones the evidence does support: limiting trading suspensions (54-day suspensions are an
observed fact, §5.2.2/§5.3.5), a centralised disclosure portal (the thesis documents
unverified release dates), and excluding P/E from price regressions (a mathematical
point). The remaining recommendations are framed as transparency proposals, not as
responses to measured deficiencies, and say so. The macro-temporal implication ("common
fiscal-year shocks exert a dominant influence … year fixed effects raise R² from 0.136 to
0.919") is correctly fenced in the same bullet ("the specific channels … are not
identified by this study, since no macroeconomic variable is in any model"). VERIFIED.

### 3(d) Limitations and future work

- Future work (§5.5, lines 233–249) is specific and consistent with the design: longer
  post-consolidation panels (5–10 years), expansion to all 19 NEPSE-listed banks with a
  DiD design "if such a cohort can be identified among the 19 listed banks", ESG/non-financial
  disclosure, intraday event studies, cross-sectoral comparison. The DiD suggestion
  correctly notes the identification problem rather than assuming a control cohort exists.
  VERIFIED as consistent with Ch1/Ch3 (19 of 20 licensed banks listed; purposive n = 5).
- **Gap — E-01 (Major, Narrow):** Ch5 contains **no consolidated limitations
  restatement**. Two Ch1 limitations are not carried into Ch5 at all (see §6). The
  limitations that *are* carried over are handled well (HC3-specificity, §5.2.3/§5.3.5;
  calendar-period vs causal, §5.3.2 line 123; entity-timing, §5.3.5; 5-day rule as
  "operational rule", §5.3.5; no prospective power analysis, §5.2.3 line 108; within-bank
  independence untested, §5.2.3). So this is a completeness gap in the concluding
  chapter, not a misrepresentation.

### 3(e) The hypothesis-decisions table

Table `tab:hyp_decisions` (§5.3.6, lines 138–166): every estimate, SE, p-value and
decision was checked against Ch4 Table `tab:hypotheses` and App E Tables
`tab:app_m1full`/`tab:app_m2full`/`tab:app_robustfull`. All eight rows agree (H1 Model 1
2.095 (4.096) p = 0.616; H1 Model 2 pre 5.577 (3.560) p = 0.140; H2 Model 1 0.219 (1.858)
p = 0.908; H2 Model 2 pre 0.100 (1.306) p = 0.940; H3 −3.124 (4.003) p = 0.448;
H4 −1.758 (1.231) p = 0.175; joint F(2,14) = 2.954, p = 0.085; R6 F(2,10) = 5.818,
p = 0.021). The table note correctly states α = 0.05 two-tailed, joint tests upper-tail,
HC3 covariance, and the three residual dfs (16/14/10). VERIFIED. Presentation issue: E-04.
Note also that Ch5's table **adds** the R6 sensitivity row, which Ch4's Table
`tab:hypotheses` does not contain — the addition is legitimate (it is labelled
"sensitivity only") but is the source of E-04.

## 4. Appendices B, C, E evaluation

### Appendix B — Complete Analysis Dataset (`appendix_b.tex`, lines 1–86)

- **Completeness: VERIFIED.** Table `tab:app_dataset` prints all 30 planned bank-years
  (5 banks × 6 fiscal years), with the two window-excluded observations (HBL FY 2077/78,
  NIMB FY 2077/78) flagged `Excluded` with footnotes giving the delayed resumption prices
  (NPR 358.90 and NPR 367.70) and delays (54 and 47 days). Realised N = 28 (13 pre / 15
  post) matches Ch1, Ch3, Ch4 and Ch5 throughout. All five variables (MPS^RD, EPS, BVPS,
  DPS, ROA) are present for every row; no value is imputed. The table note (lines 82–85)
  documents: the 5-day freshness rule; BVPS recomputation and the six NIMB whole-integer
  rounding variances (0.08–0.40 NPR) plus the two flagged unrounded differences (HBL
  FY 2076/77, 187.67 vs 187.72; NMB FY 2081/82, 175.18 vs 174.49) — all matching Ch3's
  BVPS definition section verbatim in substance; the EPS/BVPS share-base divergence in
  merger year FY 2079/80; and the R8 restated-EPS substitution (GBIME FY 2076/77, NMB
  FY 2077/78).
- **Consistency with Ch3/Ch4: VERIFIED.** Prices match Ch3 Table `tab:mps_rd` cell by cell
  (spot-checked: GBIME 450.00/299.70/189.00/179.00/218.69/238.00; HBL 520.00/Excluded/
  231.00/183.00/231.07/208.50; the delayed prices 358.90/367.70 match Ch3 footnotes).
  Descriptive statistics recomputed from these printed values reproduce Ch4 Table
  `tab:t1_descriptives` exactly (see §3(a)).
- **Caption/label/reference: VERIFIED.** Caption "Empirical Dataset: Accounting
  Fundamentals and Market Prices by Bank-Year", label `tab:app_dataset`; the intro text
  (line 6) references it correctly. Ch4 line 19 points the reader here ("the analytical
  figures embedded in this chapter are computed from the dataset printed in
  Appendix~B"). Ch5 does not reference Appendix B (no "Appendix" string occurs in Ch5
  at all — grep count 0); a pointer from Ch5 §5.2.2 to Appendix B would help the reader,
  but this is a Suggestion, not a defect, since Ch4 already points there.
- **Issues:** E-06 (R7/R8 inputs not printed in Appendix B itself), E-07 (upright
  `$MPS^{RD}$` here vs `$\mathit{MPS}^{RD}$` in the body).

### Appendix C — Model 2 Residual Diagnostics and Robustness Plots (`appendix_c.tex`, lines 1–23)

- **Contents: VERIFIED as present.** Figure `fig:app_robustness_forest` (caption:
  "Comparative Coefficient Forest Plot Across Eight Robustness Specifications (R1, R2,
  R4–R9)", file `figures/A2_robustness_forest.pdf`) and Figure
  `fig:app_model2_diagnostics` (caption: "Econometric Diagnostic Panel for Model 2
  Residuals", file `figures/A3_model2_diagnostics.pdf`). Both PDF files exist in
  `src/thesis/figures/` (verified by directory listing; the same A2 file is also used by
  Ch4 Figure `fig:robustness_forest`). Both figures are captioned and labelled, and the
  appendix text references each by `\ref` (lines 7, 13).
- **Issues — E-05 (Minor, Narrow), VERIFIED:**
  1. **Orphan appendix.** No `\ref{app:diagnostics_robustness}` and no textual mention
     of "Appendix C" occurs anywhere in the chapters, front matter, or `main.tex`
     (grep across `src/thesis/chapters/`, `src/thesis/front/`, `src/thesis/main.tex`
     returned nothing). Ch4 §4.2.7 discusses diagnostics and points to Appendix E
     tables, but never to Appendix C. A reader has no route from the body to these
     figures.
  2. **Intro overstates coverage.** Line 5: "the comparative earnings-channel robustness
     forest across the full ninefold sensitivity suite (R1 through R9)". The forest plots
     **eight** specifications (R1, R2, R4–R9); R3 is omitted because ROA is on a
     different scale. That reason is stated in Ch4 (Figure `fig:robustness_forest` note)
     but **not** in Appendix C. Line 7 correctly says "eight plotted EPS-channel
     specifications", so the appendix contradicts itself between lines 5 and 7.
  3. **No explanatory notes.** Neither figure carries a note: the diagnostics figure does
     not identify its four panels (contrast Ch4 Figure `fig:diagnostics` for Model 1,
     whose note names all four panels and the Cook's-distance threshold), and the forest
     figure does not say which quantities are plotted (earnings coefficient and EPS×Post
     interaction with 95% HC3 intervals — stated only in the Ch4 note). A reader opening
     Appendix C alone cannot interpret either figure.
- **Not visually reviewed:** I verified the figure files exist; I did not open or render
  the PDFs, so I cannot confirm the plots' contents match their captions. See §8/§11.

### Appendix E — Detailed Estimation Outputs (`appendix_e.tex`, lines 1–620)

- **Completeness: VERIFIED.** Twelve tables, all captioned and labelled: `tab:app_m1full`,
  `tab:app_m2full`, `tab:app_fetests`, `tab:app_robustfull`, `tab:app_robust_inf`,
  `tab:app_robust_fe1`, `tab:app_robust_fe2`, `tab:app_robust_fetests`, `tab:app_flagged`,
  `tab:app_m2flagged`, `tab:app_sensitivity`, `tab:app_loy`. The intro (lines 4–5) states
  the appendix's status honestly: "an audit record, not a replication package … it does
  not by itself rerun them", and "No code is shared with this thesis". Precision
  conventions are stated (4dp estimates/SEs/CIs, 2dp t, 3dp p) and followed in the tables
  I spot-checked.
- **Internal consistency: VERIFIED (spot-checked throughout).**
  - Parameter/df accounting (§"Estimation Audit", lines 6–14): Model 1 K = 12, df = 16;
    Model 2 K = 14, df = 14; R4 K = 15, df = 13; R5/R6 K = 13, df = 10; R3/R7/R8 K = 14,
    df = 14; R9 K = 14, df = 13 (N = 27). All agree with Ch3, Ch4 Table
    `tab:t5_robustness` note, and the table notes in Appendix E itself.
  - Headline coefficients agree with Ch4 to rounding: Model 1 EPS 2.0948 (Ch4 2.095),
    BVPS 0.2188 (0.219); Model 2 EPS 5.5771 (5.577), BVPS 0.1003 (0.100),
    δ_E −3.1237 (−3.124), δ_B −1.7580 (−1.758); implied post slopes 2.4534 (2.453) and
    −1.6576 (−1.658). The appendix's own rounding disclaimer (line 5) covers last-digit
    differences. VERIFIED.
  - Robustness suite (Table `tab:app_robustfull`, lines 147–180): all nine rows' F and p
    match Ch4 Table `tab:t5_robustness` (R2 2.954/0.085 … R6 5.818/0.021 … R9 1.794/0.205);
    R²/adjusted/Within-R² strings match Ch4's note exactly (R1 0.948/0.912/0.152 …
    R6 0.992/0.983/0.876). VERIFIED.
  - "Only R6 … reaches the 5 percent level (F = 5.818, p = 0.021). The remaining joint
    p-values range from 0.085 (R2) to 0.205 (R9)" (line 141): VERIFIED against the table.
  - R4 DPS coefficient 4.4580 (SE 3.0869, p = 0.172) is printed only here (line 141 and
    Table `tab:app_robust_inf`); Ch4 Table `tab:t5_robustness` does not print it, as the
    appendix itself discloses. VERIFIED, no contradiction.
  - Fixed-effect joint tests (Tables `tab:app_fetests`, `tab:app_robust_fetests`): bank
    dummies jointly insignificant in both baseline models (Model 1 p = 0.280, Model 2
    p = 0.080), year dummies jointly significant (p < 0.001) — matches the prose
    (lines 18–20) and Ch4 §4.2.7's HC3 Wald figure 1.395 (p = 0.280). VERIFIED.
  - Diagnostics prose (§"Diagnostics and Sensitivity", lines 495–507): Model 1 Koenker BP
    LM 14.37 (p = 0.213), classical 28.18 (p = 0.003); Model 2 Koenker 14.54 on 13 df
    (p = 0.337); Shapiro–Wilk W = 0.9246 (p = 0.045) and W = 0.9216 (p = 0.038);
    Model 2 VIFs 10.33/2.28/15.15/24.13 — all match Ch4 Table `tab:t6_diagnostics` and
    §4.2.7. The flagged-observation tables list exactly five rows each above the
    4/28 = 0.143 threshold, with maxima 0.5519 (Model 1, HBL FY 2076/77) and 0.4902
    (Model 2, KBL FY 2076/77) matching the prose. VERIFIED.
  - Sensitivity prose (line 501): "Across bank deletions, only KBL reverses the earnings
    interaction" — VERIFIED against Table `tab:app_sensitivity` (dropping KBL gives
    δ_E = +1.6527; all other bank deletions leave δ_E negative). "The headline
    interactions keep their signs under every single-row deletion and every year
    deletion" — VERIFIED against the note to Table `tab:app_sensitivity` (δ_E range
    −5.2039 to −1.3925; δ_B −2.3071 to −1.0526) and Table `tab:app_loy` (all δ_E, δ_B
    negative).
- **Cross-references within Appendix E: VERIFIED.** All 17 distinct `\ref` targets used
  in Appendix E resolve to labels defined in the thesis (`tab:app_m1full`,
  `tab:app_m2full`, `tab:app_fetests`, `tab:app_robustfull`, `tab:app_robust_inf`,
  `tab:app_robust_fe1`, `tab:app_robust_fe2`, `tab:app_robust_fetests`,
  `tab:app_flagged`, `tab:app_m2flagged`, `tab:app_sensitivity`, `tab:app_loy`,
  `tab:t5_robustness`, `tab:t6_diagnostics`). Ch4 also references Appendix E tables
  correctly (e.g. Ch4 line 334: Tables `tab:app_m1full` and `tab:app_m2full`; line 503:
  Tables `tab:app_robustfull`–`tab:app_sensitivity`).
- **Generator note (INFERRED, not a thesis defect):** `generators/appendix_e/appendix_e_prose.tex`
  is the prose template for this appendix; it contains `@@T01@@`–`@@T12@@` table
  placeholders and duplicates the same labels. It is a build input, not compiled into
  the thesis (`main.tex` inputs `appendices/appendix_e.tex`), and the compiled appendix
  is complete — so this is an observation about provenance, not a finding against the
  thesis. I did not verify that re-running the generator reproduces `appendix_e.tex`.
- **Issues:** E-06 (R7/R8 inputs), E-07 (notation — Appendix E itself uses
  `$\mathit{MPS}^{RD}$`, consistent with the body; the inconsistency sits in Appendix B
  and Ch1–Ch3).

## 5. Cross-cutting consistency (whole thesis)

### 5.1 Terminology

- **MPS^RD vs MPS_RD vs "market price":** No `MPS_RD` (underscore) form occurs anywhere
  in the thesis (grep). Two renderings of the defined symbol coexist — see E-07. The
  term "market price" / "Market Price per Share" is used consistently for the same
  concept; no conflicting definition was found.
- **"Consolidation wave" vs "regime shift":** used distinctly and consistently — "wave"
  for the 2022–2023 corporate event, "regime shift" for the statistical parameter change
  (Ch5: "regime shift" 3×, "consolidation wave" 6×, always in the appropriate sense).
  No conflation found.
- **"Dissertation" vs "thesis":** Ch5 uses "dissertation" 7 times and "thesis" 0 times;
  Ch1–Ch4 likewise use "dissertation" (the TU Guidelines' term). Consistent.
- **Chapter numbering:** Roman numerals throughout (Chapter I, Chapter IV, Section 5.2) —
  consistent.
- **"Regime" labels:** Pre = FY 2076/77–2078/79, Post = FY 2079/80–2081/82, identically
  in Ch1, Ch3, Ch4, Ch5, App B and App E. VERIFIED.

### 5.2 Abbreviations — method and result

**Method:** extracted all 97 entries from `src/thesis/front/abbreviations.tex`; searched
the five chapters + all appendices + abstract for each entry with a plural-tolerant
word-boundary match; then inspected the first occurrence in body order for a sample of
15 abbreviations (NPR, SEBON, NEPSE, NFRS, ROA, DPS, BVPS, EPS, HC3, VIF, OLS, RIV, ESG,
DP, DYR, BFI, ICAN, ASB, DiD, AQR).

**Results (VERIFIED by the scripted count):**
- 96 of 97 listed abbreviations occur in the body; the exception is **MBS**, which occurs
  only in `src/thesis/config/metadata.tex` (`\thesisdegree{Master of Business Studies
  (MBS)}`) — i.e. it is the degree line, not a body abbreviation. Not an error; see E-08.
- **Duplicate definitions in the list:** `DP` and `DPR` are both defined as "Dividend
  Payout Ratio"; `DY` and `DYR` are both "Dividend Yield" / "Dividend Yield Ratio".
  In the body, `DP` occurs once (Ch2 literature-synthesis table, Almumani row, as a
  variable label) against `DPR` 9 times; `DYR` occurs twice against `DY` 9 times.
  See E-08.
- **Abbreviations used but not listed:** none found in scope. All-caps tokens in
  Ch5/App B/C/E not in the list were `III`, `IV` (chapter numerals), `IME` (part of
  "Global IME Bank"), and `RD` (part of the MPS^RD superscript) — none are abbreviations.
- **Listed but never used in the body (beyond MBS):** none.
- **First-use expansion (sample):** SEBON, NEPSE, ROA, DPS, BVPS, EPS, RIV, ASB, DiD,
  AQR and BFI are all expanded at first use. HC3 (first use: Ch1 background summary
  paragraph, "under the pre-specified HC3 covariance"), OLS ("pooled OLS"), VIF
  (Ch1 organisation section), NFRS ("under NFRS 9 / IFRS 9", Ch2), NPR (Ch1, "NPR 2.0
  billion"), ICAN (only use: Ch5 §5.4, bare) and ESG (first use: Ch5 §5.5 heading, bare)
  first appear **unexpanded** and rely on the front list. No institutional rule requiring
  first-use expansion was found in the guideline passages I read (the Guidelines require
  an Abbreviations list as preliminary matter and require abbreviations used in a *table*
  to be explained below the table — see E-08). See E-09 (Suggestion).

### 5.3 Notation

- β_E, β_B, δ_E, δ_B, μ_i, λ_t, Post_t: defined identically in Ch1 (hypotheses), Ch3
  (equations `eq:fe_model1`/`eq:fe_model2`, `eq:post_def`), Ch4 and Ch5. Post_t = 1 for
  FY 2079/80–2081/82, 0 otherwise, everywhere. The standalone Post_t main effect being
  absorbed by year fixed effects is stated identically in Ch3, Ch4 and Ch5 (§5.2.2).
  VERIFIED.
- Residual dfs: 16 (Model 1), 14 (Model 2), 13 (R4, R9), 10 (R5, R6) — identical in
  Ch1, Ch3, Ch4, Ch5 and App E. VERIFIED.
- One inconsistency: E-07 (MPS^RD rendering).

### 5.4 Numbers, dates, sample sizes, names

- N = 28 realised / 30 planned; 13 pre / 15 post; G = 5 banks; 20 licensed / 19 listed;
  five banks (GBIME, HBL, KBL, NIMB, NMB) with the same merger characterisations in
  Ch1, Ch3, Ch5 and App B — VERIFIED consistent. Merger dates (Kumari–NCC 1 Jan 2023;
  GBIME–BOK 9 Jan 2023; NIB–Mega 11 Jan 2023; HBL–Civil 24 Feb 2023; Prabhu–Century
  10 Jan 2023, unsampled) appear in Ch1 and Ch3 identically; Ch5 does not restate the
  dates (it says "early 2023 (mid-FY 2079/80)" and "January–February 2023" via the R6
  discussion) — no contradiction.
- NMB/Kanchan: "approximately NPR 0.50 billion … at the 85% swap ratio, alongside a 13%
  bonus share distribution, in FY 2077/78" (Ch5 §5.2.2, line 42) vs "NPR 496.77 million
  … 85% swap ratio … 13% bonus share distribution of NPR 1,878.21 million" (Ch3) —
  consistent (496.77m ≈ 0.50bn). VERIFIED.
- 32 licensed banks in FY 2011/12 → 20 by mid-October 2023: identical in Ch1, Ch3 and
  Ch5 §5.4. VERIFIED.
- FY mapping FY 2076/77–2081/82 = 2019/20–2024/25: identical in Ch3, Ch4, Ch5 (§5.2.2).
  VERIFIED.
- One cross-cutting number that does **not** reproduce from the printed data: E-14 (Ch4
  ROA SD change; Ch5 does not repeat it).

### 5.5 Cross-references — sample and method

**Method:** collected every `\ref{…}` in the four in-scope files (Ch5: 3 refs; App B: 1;
App C: 2; App E: 17 distinct targets) and checked each label is defined exactly once in
the compiled thesis sources; also checked the body-to-appendix pointers named in §4.

**Result: VERIFIED — all sampled references resolve to the right numbered item.**
Ch5 → `tab:hyp_decisions` (its own table) and `tab:cov_sensitivity` (Ch4 joint-test
table, the table Ch5's sentence is about). App B → `tab:app_dataset` (its own table).
App C → both its own figures. App E → all 14 of its own tables plus Ch4 Tables
`tab:t5_robustness` and `tab:t6_diagnostics` (both exist and are the tables the sentences
discuss). One apparent duplicate-label count (`tab:app_m1full` defined twice, etc.) is
explained by the generator template `appendix_e_prose.tex` carrying the same labels; it
is not compiled, so no duplicate-label error arises in the thesis. I did not compile,
so this is a source-level check only.

## 6. Findings register

Severity: Critical / Major / Minor / Suggestion. Revision scale: Narrow (a sentence,
paragraph, note or label) / Substantive (reworking a section or table) / Fundamental
(re-analysis or re-design). Status is exactly one of VERIFIED / INFERRED / UNVERIFIED.

### E-01 — No consolidated limitations restatement in Chapter V

- **Location:** `src/thesis/chapters/chapter_05_summary_and_conclusion.tex`, §5.3–§5.5
  (whole concluding chapter); contrast `src/thesis/chapters/chapter_01_introduction.tex`,
  §"Limitations of the Study" (lines 164–191).
- **Severity:** Major. **Revision scale:** Narrow (add one short limitations paragraph,
  e.g. at the end of §5.3 or the start of §5.5).
- **Status:** VERIFIED — I read both sections in full and ran a grep for
  `generaliz|leakage|verified|publication date` over Ch5: the only hit is the DPS
  sentence (line 75). Neither of the two limitations below appears anywhere in Ch5.
- **Evidence:** Ch1 states (line 171): "the sample cannot be generalized to the entire
  commercial banking industry, development banks, finance companies, or non-financial
  listed sectors. Findings apply directly to the selected institutions and their
  specific consolidation contexts." Ch1 also states (limitations, §"Institutional
  Reporting Compliance and Information Leakage"): "Actual publication dates were
  verified in the reviewed records for only 2 of the 30 bank-years; for the remaining
  observations, the statutory deadline does not establish when the information became
  public." Ch5 §5.3.5 discusses the 5-day rule and freshness sensitivity at length but
  never restates the 2-of-30 verification limit; and no sentence in Ch5 states the
  generalizability boundary.
- **Impact:** Would change how the conclusions are read, not any conclusion itself. The
  concluding chapter is where an examiner looks for the study's own assessment of its
  limits; as written, the two limits that most qualify the headline design (purposive
  n = 5; unverified release dates for 28 of 30 bank-years) are absent from the chapter
  that draws the conclusions. The limitations Ch5 *does* carry (HC3-specificity,
  calendar-vs-causal, entity-timing, power) are handled well, which makes the omission
  conspicuous rather than systemic.

### E-02 — RQ3 as restated in Chapter V omits the Kanchan sensitivity (R9)

- **Location:** Ch5 §5.2.1, line 33; contrast Ch1 objectives (lines 54–76) and Ch5
  §5.2.3, line 97.
- **Severity:** Minor. **Revision scale:** Narrow (add "and the Kanchan-acquisition
  timing sensitivity" to the line-33 list).
- **Status:** VERIFIED — read the three locations.
- **Evidence:** Line 33: "How sensitive are the estimated valuation coefficients to
  transition-year effects, entity-timing mismatches, operating profitability
  substitutions, inclusion of eligible dividend disclosures, bonus share adjustments, and
  restated earnings?" — six items, no Kanchan. Ch1's specific objective 3 lists all seven
  variants including "Sensitivity analysis excluding the NMB FY 2076/77 bank-year with the
  Kanchan acquisition timing mismatch", and Ch5 §5.2.3 line 97 does name "Kanchan-mismatched
  bank-year removal (R9, residual df = 13)". (Ch1's own RQ3, line 46, is likewise narrower
  than its objectives — it mentions neither entity-timing nor Kanchan explicitly — so the
  gap originates in Ch1 and is only partly repaired in Ch5, which adds entity-timing but
  still drops Kanchan.)
- **Impact:** Traceability only. A reader tracking RQ3 → R9 finds no link in the question
  as restated, though the answer (§5.3.1, line 119) covers R9 via the suite-level statement.

### E-03 — "Four amalgamated series representing the major corporate combinations" omits the unsampled fifth combination

- **Location:** Ch5 §5.2.2, line 41.
- **Severity:** Minor. **Revision scale:** Narrow (add "four of the five").
- **Status:** VERIFIED — read Ch5 line 41, Ch1 line 30, Ch3 sampling section (line 29).
- **Evidence:** Line 41: "Four amalgamated banking series representing the major corporate
  combinations of the early-2023 wave: …". Ch1 line 30 lists **five** combinations
  commencing joint operations in January–February 2023, including "Prabhu Bank acquired
  Century Commercial Bank (10 January 2023)", and Ch3 states the sample comprises "four
  of the five Class 'A' commercial bank combinations executed during the early-2023 wave
  (the fifth, Prabhu Bank's acquisition of Century Commercial Bank, is not sampled)".
  Ch5 never mentions the unsampled fifth combination.
- **Impact:** Slight overstatement of sample coverage in the chapter's design summary; no
  estimate or conclusion depends on it.

### E-04 — Hypothesis-decisions table gives opposite decisions for the same joint null in adjacent rows

- **Location:** Ch5 §5.3.6, Table `tab:hyp_decisions`, lines 158–160 (Joint Regime Shift
  rows); contrast Ch4 Table `tab:hypotheses`.
- **Severity:** Minor. **Revision scale:** Narrow (add a table-note sentence, or move the
  R6 row out of the decision column into a clearly separated sensitivity row).
- **Status:** VERIFIED — read both tables; all numbers check out (§3(e)).
- **Evidence:** Row 1: "Joint Regime Shift | Model 2 Joint Wald | H₀: δ_E=δ_B=0 |
  F(2,14) = 2.954, p = 0.085 | Fail to Reject H₀". Row 2 (immediately below):
  "(Composite Test) | R6 Joint Wald (Sens.) | H₀: δ_E=δ_B=0 | F(2,10) = 5.818,
  p = 0.021 | Reject H₀ (unadjusted; sensitivity only)". Ch4's Table `tab:hypotheses`
  has no R6 row, so the dual-decision presentation is new in Ch5. The text (§5.3.6,
  line 177) resolves it correctly — "The evidence for a regime shift is therefore
  sensitivity-dependent and not conclusive" — but a reader scanning the table's
  "Empirical Decision" column alone can take away "Reject H₀" as the study's decision
  on the joint hypothesis, which contradicts the baseline row directly above it and the
  Holm-adjusted p = 0.169 reported in the same chapter.
- **Impact:** Presentation only; the correct interpretation is stated in the surrounding
  text, but the table is the item most likely to be quoted.

### E-05 — Appendix C is unreferenced from the body, overstates its coverage, and its figures carry no explanatory notes

- **Location:** `src/thesis/appendices/appendix_c.tex`, lines 1–23 (whole file).
- **Severity:** Minor. **Revision scale:** Narrow (one pointer sentence in Ch4 §4.2.7 or
  Ch5 §5.2.3; correct line 5; add two short figure notes).
- **Status:** VERIFIED — grepped `src/thesis/chapters/`, `src/thesis/front/` and
  `src/thesis/main.tex` for `Appendix~C`, `Appendix C` and `app:diagnostics_robustness`
  (no hits); read Appendix C in full; verified both figure files exist in
  `src/thesis/figures/`.
- **Evidence:** Line 5: "the comparative earnings-channel robustness forest across the
  full ninefold sensitivity suite (R1 through R9)" vs line 7: "the coefficient forest
  plot contrasting parameter estimates … across the eight plotted EPS-channel
  specifications (R1, R2, and R4 through R9)". R3 is omitted (ROA on a different scale)
  — the reason is given in Ch4's Figure `fig:robustness_forest` note but not here.
  Figure `fig:app_model2_diagnostics` has no note identifying its four panels
  (contrast Ch4 Figure `fig:diagnostics`, whose note names all four panels and the
  4/N threshold); Figure `fig:app_robustness_forest` has no note stating what is plotted.
- **Impact:** Usability/completeness. The figures are the only Model 2 diagnostics in the
  thesis, and nothing points the reader to them; a reader opening Appendix C alone
  cannot interpret them.

### E-06 — Appendix B is not self-contained for the R7/R8 robustness inputs

- **Location:** `src/thesis/appendices/appendix_b.tex`, note lines 82–85.
- **Severity:** Minor. **Revision scale:** Narrow (add the two restated EPS values and the
  bonus ratios, or a pointer to Appendix D §D.4).
- **Status:** VERIFIED for the absence in Appendix B; the restated values were VERIFIED
  present in Appendix D (`appendix_d.tex`, line 261: "Global IME Bank FY 2076/77 reported
  EPS 17.99, restated 15.33; NMB Bank FY 2077/78 reported 16.66, restated 14.76;
  Himalayan Bank FY 2077/78 reported 28.07, restated 27.60"). Whether the bonus ratios
  used in R7 are printed anywhere in the thesis is UNVERIFIED — a targeted grep of
  `appendix_d.tex` for "bonus" found only the codebook line (line 248, "bonus shares
  recorded separately and excluded") and the R7 definition (line 320); I did not read
  all of Appendix D.
- **Evidence:** Appendix B's note says "Variant R8 substitutes restated basic EPS for
  GBIME FY 2076/77 and NMB FY 2077/78" without giving the substituted values, and says
  nothing about the R7 bonus adjustment (formula: BVPS/(1 + bonus ratio), Ch4 Table
  `tab:t5_robustness` note) or its input ratios. The appendix's own heading promises
  the "Complete Analysis Dataset".
- **Impact:** Completeness/auditability only. The values exist in Appendix D (R8) and the
  estimates are fully printed in Appendix E; no result changes.

### E-07 — Two renderings of the MPS^RD symbol

- **Location:** Throughout: `$\mathit{MPS}^{RD}$` in Ch4/Ch5/App E; `$MPS^{RD}$` (upright
  math-italic letters, no `\mathit`) in Ch1 (RQ1 line 44; objective line 56; rationale
  line 148), Ch2 (lines 191, 399, 407), Ch3 Table `tab:mps_rd` caption (line 106), and
  Appendix B (lines 6, 13, 16, 84).
- **Severity:** Minor. **Revision scale:** Narrow (global replace to one form).
- **Status:** VERIFIED — grep across `src/thesis/chapters/`, `src/thesis/appendices/`,
  `src/thesis/front/`; no `MPS_RD` underscore form occurs anywhere.
- **Evidence:** e.g. Ch5 line 31: "($\mathit{MPS}^{RD}$)" vs App B line 6: "($MPS^{RD}$)".
  In LaTeX these render differently (word in text-italic vs three math-italic variables
  with a superscript), so the defined dependent variable changes appearance between the
  front chapters/Appendix B and the results chapters.
- **Impact:** Presentation/consistency only; the meaning is unambiguous everywhere.

### E-08 — Abbreviations list: duplicate definitions; table-note expansion missing in scope tables

- **Location:** `src/thesis/front/abbreviations.tex` (lines 60–61 `DP`/`DPR`; lines 64–65
  `DY`/`DYR`); Ch5 Table `tab:hyp_decisions` note; App B Table `tab:app_dataset` note
  (lines 82–85); App E table notes.
- **Severity:** Minor. **Revision scale:** Narrow.
- **Status:** VERIFIED — read the abbreviations file in full (97 entries); scripted count
  of body occurrences (see §5.2); read the TU Guidelines extract below.
- **Evidence:** The list defines both `DP` and `DPR` as "Dividend Payout Ratio" and both
  `DY` ("Dividend Yield") and `DYR` ("Dividend Yield Ratio") for the same concept; body
  use is `DP` 1× vs `DPR` 9×, `DYR` 2× vs `DY` 9×. `MBS` is listed but occurs in the
  body only via `src/thesis/config/metadata.tex` (degree line), never in chapter text.
  Separately, the TU Guidelines (repo copy, extracted text) state: "If abbreviations
  have been used in the table, they must be explained below the table." In-scope tables
  do not fully do this: App B's note explains MPS^RD and BVPS but not the EPS/DPS/ROA
  column headers; Ch5's hypothesis table uses "SE" in a column header without expansion
  in its note (the note expands α, df and HC3, but not SE); App E tables likewise use
  EPS/BVPS in the Variable column with notes that explain δ but not the headers. The
  abbreviations *are* defined in the front list and in Ch3's codebook, so a reader can
  decode them — this is a formal-compliance nit, not a barrier.
- **Impact:** List hygiene and formal compliance only.

### E-09 — Several abbreviations first appear unexpanded in the body

- **Location:** e.g. HC3 (first use Ch1 background summary, "under the pre-specified HC3
  covariance"); OLS ("pooled OLS", Ch1 problem statement); VIF (Ch1 organisation
  section); NFRS ("under NFRS 9 / IFRS 9", Ch2); NPR (Ch1, "NPR 2.0 billion"); ICAN
  (only use, Ch5 §5.4); ESG (first use, Ch5 §5.5 heading).
- **Severity:** Suggestion. **Revision scale:** Narrow.
- **Status:** VERIFIED for the occurrences (first-occurrence contexts inspected for a
  20-abbreviation sample, §5.2); INFERRED that no rule requires expansion — the guideline
  passages I read contain no first-use-expansion rule (they require the Abbreviations
  list as preliminary matter and table-note expansion; and "avoid using abbreviations"
  refers to the *title*).
- **Evidence:** Counter-examples in the same thesis show the convention is usually
  followed (SEBON, NEPSE, ROA, DPS, BVPS, EPS, RIV, ASB, DiD, AQR, BFI all expanded
  at first use). The unexpanded cases rely solely on the front list, which a reader who
  starts at Chapter I may not have read.
- **Impact:** Readability only; no meaning is lost.

### E-10 — Wild-cluster bootstrap p reported as 0.062; exact fraction is 2/32 = 0.0625

- **Location:** Ch5 §5.3.5, line 132; Ch4 §4.2.6 (same figure).
- **Severity:** Suggestion. **Revision scale:** Narrow (report 0.0625, or note rounding).
- **Status:** VERIFIED — arithmetic (2/32 = 0.0625 exactly) and both text locations read;
  the thesis itself states the exact fraction in the same sentence ("the smallest
  attainable p-value is 2/32 = 0.0625").
- **Evidence:** "A wild-cluster bootstrap … gives p = 0.062 for both the baseline and R6
  … with 32 patterns the smallest attainable p-value is 2/32 = 0.0625". To three decimals
  under round-half-up, 0.0625 is 0.063; the thesis prints 0.062 in both chapters.
- **Impact:** None on any conclusion (0.062 and 0.0625 are both above 0.05 and the check
  is explicitly called inconclusive).

### E-11 — Abstract wording on book-value substitution is stronger than the body

- **Location:** `src/thesis/front/abstract.tex`, line 17; contrast Ch5 §5.3.3,
  lines 125–127.
- **Severity:** Minor. **Revision scale:** Narrow (reword the abstract clause).
- **Status:** VERIFIED — read both locations in full.
- **Evidence:** Abstract: "with post-merger capital dilution coinciding with compressed
  implied slopes rather than book-value substitution." Body: "The negative
  post-consolidation BVPS point estimate … is statistically insignificant (p = 0.161),
  so these data do not establish whether this theoretical substitution occurred or how
  market participants treated expanded book equity." The body does not rule substitution
  out; the abstract's "rather than" can be read as ruling it out. (The "capital dilution
  coinciding" half is fair: Ch4 §4.3.2 discusses capital expansion/share supply as a
  plausible mechanism, hedged as such.)
- **Impact:** A reader who reads only the abstract takes away a firmer claim than the
  body supports. No Ch5 conclusion is affected.

### E-12 — Chapter V's four-section structure vs the Guidelines' three-section organisation

- **Location:** Ch5 §5.1 (Introduction), line 6.
- **Severity:** Minor. **Revision scale:** Narrow (supervisor confirmation; no text change
  needed if accepted).
- **Status:** VERIFIED — I opened the repo copy of the Guidelines
  (`docs/thesis_guidelines_reference/01_TU-FOM_Masters-Dissertation-Guidelines-2019.pdf`,
  pp. 14–15, extracted with pdftotext): "Chapter V — Summary and Conclusion … it is
  organized in three sections: Summary. … Conclusion. … Implications. The research may
  have number of implications … They may be reported as recommendations and areas for
  future research."
- **Evidence:** Ch5 line 6: "The Master's Degree Dissertation Guidelines (2019, p. 15) …
  organize the concluding chapter into three sections — Summary, Conclusion, and
  Implications, with recommendations and areas for future research reported under
  Implications. This chapter follows that structure and, for clarity of presentation,
  separates the recommendations and future-research material into its own section."
  The thesis discloses the deviation, all three required sections are present with the
  required content, and the guideline wording ("may be reported as recommendations…")
  is permissive. The four-section split is a formal deviation to confirm with the
  supervisor, not a content gap.
- **Impact:** Formal compliance only; no claim or conclusion changes.

### E-13 — Causal verb in the H2 conclusion sentence

- **Location:** Ch5 §5.3.6, line 174.
- **Severity:** Suggestion. **Revision scale:** Narrow (one word).
- **Status:** VERIFIED — read the sentence in context.
- **Evidence:** "Book value per share exerts no statistically significant incremental
  pricing effect in the baseline specification." The thesis is otherwise careful to say
  "association" (e.g. §5.3.2, line 123: "Results are reported as associations across
  calendar periods, not as an established causal merger impact"). "Exerts" implies a
  causal effect; "shows" or "has" would match the thesis's own language.
- **Impact:** Wording only; the statistical content (no significant association) is correct.

### E-14 — Ch4 ROA dispersion change does not reproduce from the printed dataset (cross-cutting observation; Ch5 does not repeat the figure)

- **Location:** Ch4 §4.2.1, line 81 (descriptive bullet for ROA); data source App B /
  `data_analysis/analysis/outputs/tables/A6_analysis_dataset.md`.
- **Severity:** Minor. **Revision scale:** Narrow if it is an error (one number); none if
  it is a rounding artefact.
- **Status:** UNVERIFIED / CANNOT DETERMINE — I recomputed from the printed 2-decimal
  ROA values in both Appendix B and the A6 dataset table (identical values): pre SD
  0.2213, post SD 0.4382, giving an SD increase of **+97.99%** and a pre CV of 16.8%,
  against Ch4's printed "+97.49%" and "16.9%". (The mean decline, −46.38% vs my
  −46.37%, is ordinary rounding.) The gap is consistent with Ch4 having been computed
  from unrounded pipeline ROA values — ROA is printed to only 2 decimals, and values
  near 0.00–1.79 carry rounding error up to ±0.005 — but I did not run the estimation
  pipeline and the unrounded values are not printed anywhere I read, so I cannot
  determine whether this is a rounding artefact or an error. All other descriptive
  percentages I recomputed matched exactly (§3(a)), which is why this single 0.5pp gap
  is worth flagging rather than assuming.
- **Evidence:** Ch4 line 81: "the SD rose by 97.49% and the coefficient of variation rose
  from 16.9% to 62.2%." My recomputation (script `/tmp/check_stats.py`, run against both
  Appendix B rows and the A6 table): SD +97.99%, CV 16.8% → 62.2%.
- **Impact:** None on Chapter V — Ch5 repeats only the EPS–ROA correlation (r = 0.975,
  VIF ≈ 20), which I verified (r = 0.9745, VIF = 19.83). Flagged here only because the
  task's cross-cutting brief covers numbers consistency across chapters.

## 7. Claims register — substantive claims in Chapter V

Each claim below is from Ch5; "Evidence" names the Ch4/App E location that supports it.
All were checked; none was found unsupported. (Interpretive/hedged claims are listed with
their hedge.)

| # | Ch5 claim (paraphrased; exact wording in §3/§6 where quoted) | Location | Evidence | Status |
|---|---|---|---|---|
| C-01 | EPS and BVPS positive but insignificant in Model 1 (2.095, p = 0.616; 0.219, p = 0.908) | §5.2.3, §5.3.1, §5.3.6 | Ch4 Table `tab:t3_model1`; App E `tab:app_m1full` | VERIFIED |
| C-02 | Pre-consolidation slopes 5.577 (p = 0.140) / 0.100 (p = 0.940); implied post 2.453 (p = 0.298) / −1.658 (p = 0.161) | §5.2.3, §5.3.2 | Ch4 Table `tab:t4_model2`; App E `tab:app_m2full` note | VERIFIED |
| C-03 | Joint test F(2,14) = 2.954, p = 0.085; does not reject at 5%, marginal at 10%; HC3-specific (rejects under classical/HC0/HC1/HC2 for all R2–R9) | §5.2.3, §5.3.1 | Ch4 Table `tab:cov_sensitivity`; App E `tab:app_robustfull` | VERIFIED |
| C-04 | R6 is the only raw rejection among eight joint tests R2–R9 under HC3; Holm-adjusted p = 0.169 | §5.2.3, §5.3.1, §5.3.5, §5.3.6 | Ch4 §4.2.6, Tables `tab:t5_robustness`/`tab:cov_sensitivity` | VERIFIED |
| C-05 | Descriptive regime shifts (MPS −33.81%, EPS −40.13%, DPS −76.90%, BVPS +2.45%, with SD/CV changes) | §5.2.3, lines 71–76 | Recomputed from App B rows (§3(a)); Ch4 Table `tab:t1_descriptives` | VERIFIED |
| C-06 | EPS–ROA r = 0.975, VIF ≈ 20; EPS–BVPS r = 0.372, p = 0.051; Model 1 VIFs ≈ 1.16; Model 2 VIFs 10.33/2.28/15.15/24.13; full-design VIFs 5.70/12.32 and 14.82/12.46/27.34/259.32 | §5.2.3 | Ch4 Table `tab:t2_correlations`, Table `tab:t6_diagnostics` + note; recomputed r = 0.9745/0.3718 | VERIFIED |
| C-07 | Bank FE (not year FE) drive the Model 1 imprecision: year-FE-only slope 2.185 (SE 1.260, p = 0.098); adding bank FE raises SE to 4.096 | §5.2.3 | Ch4 Table `tab:spec_comp` | VERIFIED |
| C-08 | R² 0.948 (adj. 0.912); 0.136 pooled → 0.919 year-FE-only → 0.948 two-way | §5.2.3 | Ch4 Table `tab:spec_comp` | VERIFIED |
| C-09 | No prospective power analysis; post hoc detectable effects 10.73 / 12.06 / 3.71 NPR; non-rejections do not rule out smaller effects | §5.2.3, line 108 | Ch3 econometric section; Ch4 (same figures) | VERIFIED as repeat; power arithmetic not recomputed |
| C-10 | R6 F(2,10) = 5.82, p = 0.021 (N = 23); δ_B = −2.611 (p = 0.116); R5 does not reject (F = 2.41, p = 0.139); leave-one-bank in R6 sample F = 0.615–1.309 | §5.2.3, lines 98–102 | Ch4 §4.2.6, Table `tab:t5_robustness`; App E `tab:app_robustfull` | VERIFIED |
| C-11 | Including delayed observations → F(2,16) = 4.762 (p = 0.024); stale-price scenarios F = 3.870 (p = 0.043) and 3.821 (p = 0.044); N = 30 pre-period BVPS 0.709 vs 0.100 | §5.3.5, line 132 | Ch4 §4.2.6, §4.3.5 | VERIFIED |
| C-12 | Wild-cluster bootstrap p = 0.062 both tests; smallest attainable 2/32 = 0.0625; flip mechanically forced; inconclusive | §5.3.5, line 132 | Ch4 §4.2.6 | VERIFIED as repeat; bootstrap not recomputed (see E-10) |
| C-13 | F is 41.8% above the 5% critical value (R6) | §5.3.5, line 132 | Computed: F(2,10) crit. 4.1028 (scipy); Ch4 "29.5% decrease" is the same arithmetic | VERIFIED |
| C-14 | No evidence for earnings dominance, slope decline, or negative BVPS association; results are calendar-period associations, not causal merger impact | §5.3.2, line 123 | Ch1 hypotheses/limitations; Ch4 §4.3.1–§4.3.2 | VERIFIED |
| C-15 | Book-value substitution under Ohlson/Collins theory not established by these data | §5.3.3, lines 125–127 | Ch4 §4.3.3 (Kwon/Ohlson reconciliation) | VERIFIED |
| C-16 | Sample rule is consequential; 5-day cutoff is an operational rule | §5.3.5, line 132 | Ch1 limitations; Ch3 §"Sample Size…" ("un-derived operational choice") | VERIFIED |
| C-17 | N = 28 (13 pre / 15 post); two exclusions HBL/NIMB FY 2077/78, 54/47 days late, 6 Jun / 30 May 2022 | §5.2.2 | Ch3 Table `tab:mps_rd`; App B footnotes | VERIFIED |
| C-18 | Implication-level hedges (AQR hypothesis; no transitoriness parameter; DPS never shown to anchor valuation, r = 0.082, p = 0.679; NFRS recommendation rests on transparency, not a documented deficiency) | §5.4 | Ch4 §4.3.2, Table `tab:t2_correlations` (DPS–MPS r = 0.082, p = 0.679 — recomputed r = 0.0818) | VERIFIED |

## 8. Inventory

### Chapter V — sections (all REVIEWED; read in full)

| Section | Lines | Status |
|---|---|---|
| §5.1 Introduction | 3–13 | REVIEWED |
| §5.2 Summary of the Study | 14–109 | REVIEWED |
| §5.2.1 Research Overview, Problem, and Objectives | 16–37 | REVIEWED |
| §5.2.2 Methodology and Research Design Synthesis | 38–67 | REVIEWED |
| §5.2.3 Summary of Major Empirical Findings | 68–109 | REVIEWED |
| §5.3 Conclusions | 110–179 | REVIEWED |
| §5.3.1 Direct Answers to Research Questions | 114–121 | REVIEWED |
| §5.3.2 Regime Differences in Accounting Valuation Slopes | 122–124 | REVIEWED |
| §5.3.3 Behaviour of Book Value and Earnings Slopes Across Regimes | 125–127 | REVIEWED |
| §5.3.4 Econometric Discipline: Specification Sensitivity and Macro-Year Variation | 128–130 | REVIEWED |
| §5.3.5 Archival Timing and Data Integrity in Frontier Market Research | 131–133 | REVIEWED |
| §5.3.6 Formal Decisions on Research Hypotheses (+ Table `tab:hyp_decisions`) | 134–179 | REVIEWED |
| §5.4 Implications of the Study (3 subsections: regulators; executives/boards; investors/analysts) | 180–221 | REVIEWED |
| §5.5 Recommendations and Directions for Future Research (policy recommendations; future inquiry) | 222–249 | REVIEWED |

### Appendix B — 1 table

| Item | Location | Status |
|---|---|---|
| Table `tab:app_dataset` (30 rows, 8 cols + note) | lines 9–85 | REVIEWED (read in full; values recomputed, §3(a)) |

### Appendix C — 2 figures

| Item | Location | Status |
|---|---|---|
| Figure `fig:app_robustness_forest` (A2_robustness_forest.pdf) | lines 9–14 | REVIEWED as text; figure file existence verified; **contents NOT visually reviewed** (PDF not opened/rendered) |
| Figure `fig:app_model2_diagnostics` (A3_model2_diagnostics.pdf) | lines 16–21 | REVIEWED as text; file existence verified; **contents NOT visually reviewed** |

### Appendix E — 12 tables + prose

| Item | Location | Status |
|---|---|---|
| §Estimation Audit (prose) | lines 6–14 | REVIEWED |
| Table `tab:app_m1full` | lines 24–64 | REVIEWED |
| Table `tab:app_m2full` | lines 66–110 | REVIEWED |
| Table `tab:app_fetests` | lines 112–137 | REVIEWED |
| §Robustness Estimates (prose) | lines 139–145 | REVIEWED |
| Table `tab:app_robustfull` | lines 147–181 | REVIEWED |
| Table `tab:app_robust_inf` (longtable, R3–R9) | lines 183–266 | REVIEWED |
| Table `tab:app_robust_fe1` (R3–R5) | lines 268–341 | REVIEWED |
| Table `tab:app_robust_fe2` (R6–R9) | lines 343–436 | REVIEWED |
| Table `tab:app_robust_fetests` | lines 438–493 | REVIEWED |
| §Diagnostics and Sensitivity (prose) | lines 495–507 | REVIEWED |
| Table `tab:app_flagged` | lines 509–536 | REVIEWED |
| Table `tab:app_m2flagged` | lines 538–564 | REVIEWED |
| Table `tab:app_sensitivity` | lines 566–593 | REVIEWED |
| Table `tab:app_loy` | lines 595–620 | REVIEWED |

### NOT REVIEWED (with reason)

- **Visual contents of the two Appendix C figures and of Ch4 figures** (F1–F6, A2): the
  figure PDFs were not opened or rendered; only file existence and the surrounding text
  were checked. The task forbade building/compiling the thesis; viewing the existing
  PDFs would have been permitted but was not done — this is a stated gap, not a
  prohibition I relied on.
- **Recomputation of regression estimates** (coefficients, SEs, p-values, F-tests): no
  estimation code was run and no pipeline output was re-estimated. All numeric checks
  in this review are cross-checks between printed locations and recomputation from the
  printed Appendix B dataset (descriptives/correlations only). The thesis itself states
  Appendix E is an audit record, not a replication package, and no code is shared with
  it.
- **Chapters II and Appendix D in full:** consulted by targeted search only (see §11).
  Ch2's literature claims relevant to Ch5 were verified by search; App D was searched
  for the R8 values and bonus-ratio question only.
- **The v1 prior review** (`docs/thesis_review/v1/data_analysis_review.md`): not read,
  per the independence instruction (it was permitted only if scope needed it; it did not).

## 9. VERIFIED strengths in scope

1. **Null results reported without spin.** Every non-rejection carries its exact statistic
   and p-value, in Ch5, Ch4 and App E identically; the joint test's HC3-dependence is
   stated in all three places, including the fact that all eight joint tests reject under
   classical/HC0/HC1/HC2. How verified: line-by-line comparison of Ch5 §5.2.3/§5.3.6
   against Ch4 Tables `tab:t4_model2`/`tab:t5_robustness`/`tab:cov_sensitivity` and App E
   Tables `tab:app_m2full`/`tab:app_robustfull`.
2. **The R6 sensitivity is fenced on every appearance.** Unadjusted p = 0.021 is always
   accompanied by Holm-adjusted p = 0.169, the leave-one-bank failure, and the
   "sensitivity only" label (Ch5 lines 97–102, 119, 123, 132, 160, 177; Ch4 §4.2.6).
   How verified: read all six Ch5 occurrences and the Ch4 R6 bullet.
3. **Descriptive statistics reproduce exactly from the printed dataset.** All §5.2.3
   percentages and the correlation/VIF figures recomputed from Appendix B rows match to
   printed precision (§3(a)). How verified: Python recomputation from the 30 parsed
   Appendix B rows (script in `/tmp/check_stats.py`).
4. **Implications are fenced to the evidence.** §5.4/§5.5 repeatedly name what was *not*
   measured (asset quality, transitoriness, macro channels, non-recurring adjustments)
   before recommending anything on that topic (exact quotes in §3(c)). How verified: full
   read of §5.4–§5.5.
5. **Appendix E is a genuine audit record.** Full dummy coefficients, joint FE tests,
   robustness inference, flagged observations, leave-one-bank and leave-one-year tables,
   with an explicit rounding policy and an explicit "audit record, not a replication
   package" disclaimer. Internal spot-checks (§4) found no inconsistencies.
6. **Appendix B is complete and self-documenting for the estimation sample.** All 30
   planned rows, both exclusions flagged with delayed prices, BVPS reconciliation
   variances disclosed (including the two unresolved 0.05/0.69 NPR differences) rather
   than overwritten. How verified: full read + price spot-check against Ch3 Table
   `tab:mps_rd`.
7. **Causal language is disciplined.** "Results are reported as associations across
   calendar periods, not as an established causal merger impact" (§5.3.2); the same
   restriction is in Ch1 and Ch3. The single exception is one verb (E-13).
8. **Cross-references in scope all resolve.** Every `\ref` in Ch5/App B/C/E points to an
   existing label for the item the sentence discusses (§5.5).

## 10. Open questions (for the author/supervisor — I could not determine these)

1. Does the Faculty of Management accept a four-section Chapter V (recommendations /
   future research split out) against the Guidelines' three-section organisation (E-12)?
   The Guidelines text I opened (p. 15) is permissive ("may be reported as…"), but only
   the supervisor/institution can confirm.
2. Is the Ch4 ROA dispersion figure (+97.49%) computed from unrounded pipeline values,
   or is it an error (E-14)? Only the pipeline values can settle it.
3. Are the R7 bonus ratios printed anywhere in the thesis (E-06)? I searched Appendix D
   by keyword but did not read it in full.
4. Is there an institutional rule on first-use expansion of abbreviations, or is reliance
   on the front Abbreviations list the accepted convention (E-09)? No such rule was found
   in the guideline passages I read.

## 11. Verification log

### What I read (fully, during this task)

- `src/thesis/chapters/chapter_05_summary_and_conclusion.tex` (249 lines)
- `src/thesis/appendices/appendix_b.tex` (86 lines)
- `src/thesis/appendices/appendix_c.tex` (23 lines)
- `src/thesis/appendices/appendix_e.tex` (620 lines)
- `src/thesis/generators/appendix_e/appendix_e_prose.tex` (53 lines)
- `src/thesis/chapters/chapter_01_introduction.tex` (203 lines)
- `src/thesis/front/abstract.tex` (23 lines)
- `src/thesis/chapters/chapter_04_results_and_discussion.tex` (677 lines)
- `src/thesis/chapters/chapter_03_research_methodology.tex` (392 lines)
- `src/thesis/front/abbreviations.tex` (133 lines)
- `src/thesis/main.tex` (appendix/chapter inclusion lines, for structure)
- `docs/thesis_guidelines_reference/01_TU-FOM_Masters-Dissertation-Guidelines-2019.pdf`
  (28 pages; pp. 14–16 read via pdftotext extract; full text searched for
  "abbreviation" and "table" guidance)

### What I consulted by targeted search (not full read)

- `src/thesis/chapters/chapter_02_literature_review.tex` (grep for Ohlson/Collins/Kwon/
  Chaudhari/Gurung-Dahal/Timalsina/NFRS/MPS^RD passages)
- `src/thesis/appendices/appendix_d.tex` (grep for restated EPS values, bonus ratios,
  R7 definition)
- `src/thesis/references.bib` (existence check for the 12 keys cited in Ch5 — all present)
- `data_analysis/analysis/outputs/tables/A6_analysis_dataset.md` (ROA/EPS/BVPS/DPS/MPS
  columns, for E-14)
- `src/thesis/figures/` (directory listing confirming A2/A3 PDFs exist)

### What I computed

- Descriptive statistics, CVs, percentage changes and three correlations from the 30
  Appendix B rows (Python `statistics`, sample SD; script at `/tmp/check_stats.py` —
  scratch only, not in the repo).
- F(2,10) 5% critical value 4.1028 via scipy; 5.818/4.1028 − 1 = 41.8%;
  1 − 4.1028/5.818 = 29.5%.
- Abbreviation audit: 97 list entries vs body occurrences (plural-tolerant regex);
  duplicate-definition check; first-occurrence contexts for a 20-abbreviation sample.
- Cross-reference audit: all `\ref` targets in the four in-scope files checked against
  `\label` definitions in the thesis sources.
- Terminology counts: "regime shift" 3× / "consolidation wave" 6× in Ch5; "dissertation"
  7× / "thesis" 0× in Ch5; "Appendix" 0× in Ch5.

### What I could not do, and why

- **Compile/build the thesis or check rendered output** (page numbers, table/figure
  numbering in the PDF, overfull boxes): forbidden by the task (read-only, no build).
  All cross-reference checks are therefore source-level only.
- **Visually inspect figure contents** (App C figures; Ch4 figures): not done (see §8).
- **Recompute regression estimates**: no estimation code was run; the thesis states no
  code is shared with it, and Appendix E is an audit record, not a replication package.
- **Verify the TU Guidelines from the institution's own website**: I used the repo's own
  copy of the 2019 Guidelines PDF instead (a published institutional document held in
  the repo). I did not open an external TU/FOM web page for it; the p. 15 claim in Ch5
  was verified against that repo copy. No other external source was needed: no finding
  in this review rests on an external standard beyond the Guidelines passage quoted
  above.
- **Plagiarism / authorship / AI-tool assessment**: explicitly out of scope; not attempted.

### Sources consulted (fully read vs snippet-only)

| Source | Use | Extent |
|---|---|---|
| TU FOM, *Master's Degree Dissertation Guidelines* (2019), repo copy `docs/thesis_guidelines_reference/01_TU-FOM_Masters-Dissertation-Guidelines-2019.pdf` | Ch5 §5.1 three-section claim (E-12); table abbreviation rule (E-08) | pp. 14–16 fully read (extract); full text searched for "abbreviation"/"table" |
| Thesis files listed under "What I read (fully)" | All findings | Fully read |
| Ch2, App D, references.bib, A6 dataset, figures dir (see above) | Targeted checks | Snippet/search only |
| No other external sources were consulted. No web search was needed: every standard or guideline claim in this review is grounded in the repo copy of the Guidelines above. | | |

## 12. Read-only compliance and git status confirmation

- No repo file was modified, renamed, deleted, or reformatted during this review. All
  scratch work (statistics script, Guidelines text extract) was run in `/tmp` only. The
  thesis was not built or compiled.
- `git status` was run in the repo at the start of the task (before any writing) and again
  after writing this file. The list of modified tracked files is **identical** in both
  runs — all of those modifications pre-date this task (uncommitted working-tree changes
  in the version under review). The only file I created is this one:
  `docs/thesis_review/v2/review_ch5_back.md` (965 lines).
- Note on the directory: `docs/thesis_review/v2/` was already untracked and already
  contained `pass_a_note.md` when I started; it also contains sibling reviewers' files
  (`review_ch3_method.md`, `review_ch4_results.md`, `review_criteria_compliance.md`,
  `review_front_ch1.md`, timestamps 15:26–15:27) created in parallel by other agents
  during this same review round. I did not create, modify, or read those files; my sole
  creation in the repo is `review_ch5_back.md`.
