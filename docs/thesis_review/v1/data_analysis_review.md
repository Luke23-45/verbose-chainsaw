# Independent Review of the Data Analysis

**Dissertation:** *Value Relevance of Accounting Information Before and After the Banking Consolidation Wave: Evidence from Nepalese Commercial Banks*
**Reviewed artifact:** repository at commit `2d195bfb9e5a14dc8d4bf927cb7aeadf9ec465a1` (Sat Nov 14 01:58:44 2026 +0000)
**Review date:** 14 November 2026
**Review file:** `docs/thesis_review/v1/data_analysis_review.md` (new; no other file created, modified, renamed, or deleted)
**Mode:** read-only, independent, adversarial-but-fair methodological review

---

## Bottom line

The computational pipeline is unusually good: every reported coefficient, standard error, test statistic, $R^2$, Cook's distance, leverage value, Holm adjustment and power calculation that I re-derived reproduced to rounding, and the code, the frozen data extract and the thesis agree. The problems are almost entirely *inferential and interpretive*, not arithmetic:

1. **The headline "no regime shift" result is a product of one covariance-estimator choice.** Under classical, HC0, HC1 and HC2 covariances **all eight** joint tests R2–R9 reject at 5%; under HC3 **only R6** does. The thesis reports HC3 only and never shows this sensitivity, even though its own robust Breusch–Pagan test does not reject homoskedasticity.
2. **The one 5% rejection (R6) is created by deleting rows the thesis already knows are entity-mismatched**, is not multiplicity-adjusted (Holm $p=0.169$), and collapses to $p=0.329$–$0.572$ when any single bank is removed. Yet Table 5.1 records it as "Reject $H_0$".
3. **The wild-cluster bootstrap cannot discriminate**: with 5 clusters and 32 Rademacher patterns, the minimum attainable $p$ is $2/32=0.0625$, which is exactly what is reported for both models. The "check" is mechanically forced, and the code says so.
4. Several claims are simply wrong as written: HC3 does **not** correct "small-cluster downward bias"; the observed R6 $F$ is 41.8% (not 29.5%) above the critical value; $\hat\beta_E$ is not a P/E multiple (~5.6) but a partial slope (sample P/E is ~18); and Chapter V asserts a post-consolidation book-value discount that the thesis elsewhere says is statistically unsupported.

None of this is hidden fraud. The thesis is often candid about its limitations. The problem is that disclosure is used in place of correction: limitations are stated, then the conclusion is written as if they did not bind.

---

## 1. Scope, mandate, and evidentiary rules

### 1.1 What was reviewed

In scope:

- All thesis chapters and front matter (`src/thesis/front/abstract.tex`, `src/thesis/chapters/chapter_01`–`chapter_05`, `src/thesis/appendices/appendix_b`, `_d`, `_e`, `src/thesis/references.bib`).
- The analysis pipeline (`data_analysis/analysis/dataset.py`, `stats/models.py`, `stats/wald.py`, `stats/wild_bootstrap.py`, `stats/diagnostics.py`, `stats/robustness.py`, `scripts/verify.py`, `scripts/generate.py`, `tests/test_stats.py`, `config/base.yaml`, `ANALYSIS_PLAN.md`).
- Generated artifacts referenced by the thesis (`data_analysis/analysis/assets/t1`–`t6`, `a2`, `a4`, `a6`, `f3`, `f4`).
- The frozen extraction output used as analysis input (`data_analysis/data_extract/output/manual_review/mps_rd_joined_panel.csv`, `..._bonusadj.csv`).

Out of scope, by instruction and by choice:

- **The extraction stage is treated as ground truth.** I did not audit PDF parsing, OCR, page selection, or the manual review sheets. If a number is wrong in `mps_rd_joined_panel.csv`, this review will not catch it.
- The literature review, the theoretical model derivation, writing quality, formatting, and the proposal are consulted only where they define what the analysis was supposed to test.
- I did not modify, regenerate, rename, delete, or reformat anything inside the repository. All recomputation happened in `C:\Users\Hellx\AppData\Local\Temp\opencode\review_repro\` using standalone scripts that read the frozen CSVs; no repository module was imported, so no `__pycache__` was written into the tree. The only repository-side execution was a read-only run of the existing test suite (Section 9.1), which wrote nothing.

**Path convention.** Citations such as `chapter_04:286` mean `src/thesis/chapters/chapter_04_results_and_discussion.tex`, line 286; `chapter_03`, `chapter_05` follow the same pattern. `abstract` = `src/thesis/front/abstract.tex`. `appendix_d`/`appendix_e` = `src/thesis/appendices/appendix_d.tex` / `appendix_e.tex`. `dataset.py`, `models.py`, `wald.py`, `wild_bootstrap.py`, `diagnostics.py`, `robustness.py` = the module of that name under `data_analysis/analysis/` (with `stats/` for the last five). `proposal/07_methodology.tex` = `src/proposal/sections/07_methodology/07_methodology.tex`. Full paths are given where a file falls outside these families.

### 1.2 Status and severity vocabulary

Every substantive claim below carries one of:

| Tag | Meaning |
|---|---|
| **VERIFIED** | Re-derived from the frozen data in scratch space and matched the thesis to rounding; or established directly by reading the cited source text. |
| **INFERRED** | Follows from verified facts plus an explicit argument, but was not itself computed or directly observed. |
| **UNVERIFIED-CANNOT DETERMINE** | Could not be checked with available access/time; the review takes no position. |

Severity:

| Severity | Meaning |
|---|---|
| **Critical** | Invalidates or materially re-frames a headline conclusion or a formal hypothesis decision. |
| **Major** | Substantially weakens a reported result or misstates the method; a reader relying on the statement would be misled. |
| **Minor** | Local error, inconsistency, or omitted caveat that does not reverse a conclusion. |
| **Suggestion** | Improvement that would strengthen the work but is not a defect. |

### 1.3 The benchmark

Findings are judged against the thesis's own hypotheses and objectives (`chapter_01_introduction.tex:70–136`), not against an external standard of what the study "should" have been. Where I invoke econometric best practice, I cite a source I actually opened (Section 9.2).

---

## 2. Understanding of the thesis: claims and what would falsify them

The study asks whether EPS and BVPS are priced in Nepalese bank equities, and whether those pricing relations shifted after the 2023 consolidation wave. The empirical object is a bank-year panel of 5 banks × 6 fiscal years, reduced to $N=28$ by a 5-day price-freshness rule (`dataset.py:6–12`; `chapter_03_research_methodology.tex:221`).

**Model 1** (`chapter_03:271`; `chapter_04:179`, `tab:t3_model1`):

$$\text{Price}_{it}=\alpha+\beta_E \text{EPS}_{it}+\beta_B \text{BVPS}_{it}+\mu_i+\lambda_t+\varepsilon_{it}$$

**Model 2** (`chapter_03:293`; `chapter_04:236`, `tab:t4_model2`):

$$\text{Price}_{it}=\alpha+\beta_E \text{EPS}_{it}+\beta_B \text{BVPS}_{it}+\delta_E(\text{EPS}_{it}\cdot\text{Post}_t)+\delta_B(\text{BVPS}_{it}\cdot\text{Post}_t)+\mu_i+\lambda_t+\varepsilon_{it}$$

**Hypotheses** (`chapter_01:79–130`): $H_1:\beta_E=0$, $H_2:\beta_B=0$, $H_3:\delta_E=0$, $H_4:\delta_B=0$, plus a joint $H_0:\delta_E=\delta_B=0$. The formal decisions are in `chapter_05:140–177`, `tab:hyp_decisions`.

**Inference**: OLS on the LSDV design, MacKinnon–White HC3 covariance, Student $t$ with residual df (16 for Model 1, 14 for Model 2, 10 for R6). HC3 is pre-specified in the proposal (`src/proposal/07_methodology.tex:187`) and defended in `chapter_03:346`.

What would falsify the thesis's stated conclusion ("no conclusive regime shift"):

- a joint test that rejects under a defensible covariance estimator other than HC3 (it does, for all eight specifications);
- a joint test that rejects in the baseline sample without deleting rows (it does not, under any estimator: baseline $p$ ranges from .0007 to .085);
- a rejection that survives reasonable perturbation of the sample (R6 does not survive dropping any single bank, and is not multiplicity-adjusted).

That framing matters: the thesis's *conclusion* is conservative, but the *evidence* is more fragile than the conclusion admits, and in one direction the fragility points the other way (toward a regime shift, not away from one).

---

## 3. Traceability matrix and coverage

Each row maps a thesis claim to the code that produces it, to my independent check, and to a verdict. "Match" means agreement to the thesis's printed rounding.

| # | Thesis claim (location) | Producing code | Independent check | Verdict |
|---|---|---|---|---|
| 1 | $N=28$ clean bank-years, 13 pre / 15 post, 2 window-excluded (`chapter_03:221`; `appendix_d:182–188`) | `dataset.py:6–12, 82` | Counted rows with `gap<=5`; 28 rows; 2 rows with gap > 5 (HBL and NIMB FY2077/78) | Match |
| 2 | Table 4.1 descriptives (`chapter_04:41`) | `assets/t1_descriptives.*` | Recomputed means/SDs full, pre, post from CSV | Match |
| 3 | Percentage changes in means/SDs (`chapter_05:73`) | derived | Recomputed from unrounded data: price −33.81%, EPS −40.13%, EPS SD +63.95%, BVPS +2.45%, BVPS SD −15.30%, DPS −76.90%, DPS SD −16.62%, ROA −46.38%, ROA SD +97.49% | Match (thesis's 97.49% is right) |
| 4 | Table 4.2 correlations and $p$-values (`chapter_04:107`) | `assets/t2_correlations.*` | Recomputed Pearson $r$ and two-sided $p$ | Match |
| 5 | Model 1 coefficients, HC3 SE, $t$, $p$, $R^2$, adj. $R^2$ (`tab:t3_model1`) | `stats/models.py` | Re-fit LSDV with `cov_type="HC3", use_t=True`; $\beta_E=2.0948$ (4.0955), $p=.616$; $\beta_B=.2188$ (1.8582), $p=.908$; $R^2=.9479$; adj. $.9124$; df 16 | Match |
| 6 | Model 2 coefficients and interactions (`tab:t4_model2`) | `stats/models.py` | $\beta_E=5.5771$ (3.5603); $\beta_B=.1003$ (1.3057); $\delta_E=-3.1237$ (4.0031); $\delta_B=-1.7580$ (1.2307); df 14 | Match |
| 7 | Implied post slopes 2.453 / -1.658 (`chapter_04:257, 296`; `chapter_05:92`) | derived | Recomputed; SEs 2.2687 and 1.1198; $p=.298/.161$ | Match |
| 8 | Joint Wald $F(2,14)=2.954$, $p=.085$ (`chapter_04:559` context; `chapter_05:93`) | `stats/wald.py` | Recomputed HC3 Wald | Match |
| 9 | Within-$R^2$ .1518 / .6417; increments 0.93pp / 3.9pp (`chapter_03:353`; `chapter_04:559` context) | `stats/models.py:82–86` | Recomputed FE-only $R^2=.9388$; Model 1 increment $.00929$; Model 2 increment $.03927$ | Match |
| 10 | Specification comparison incl. pooled OLS 4.882 ($R^2=.136$) and FE joint tests (`tab:spec_comp`) | `assets/t5` / `t6` | Recomputed pooled and FE-only fits | Match (see F12 on test labeling) |
| 11 | Breusch–Pagan robust 14.369 ($p=.213$), classical 28.183 ($p=.003$) (`chapter_04:494`) | `stats/diagnostics.py` | Recomputed both variants | Match |
| 12 | Cook's distance / leverage flagged rows (`appendix_e:513–559`) | `stats/diagnostics.py` | Recomputed; M1 0.5519/0.4124/0.2711/0.2447/0.1451; M2 0.4902/0.3983/0.2404/0.1870/0.1513 | Exact match |
| 13 | Shapiro-Wilk .92462 ($p=.045$) / .92155 ($p=.038$) (`chapter_04:513`; `appendix_e:503`) | `stats/diagnostics.py` | Recomputed | Match |
| 14 | VIF table 1.16 / 10.33 / 2.28 / 15.15 / 24.13 (`chapter_04:485–492`) | `stats/diagnostics.py:25–36` | Reproduced substantive-only VIFs exactly; **full-design** VIFs differ sharply | Partial (F05) |
| 15 | Holm-adjusted smallest $p=0.169$ (`chapter_04:443`; `chapter_05:102`) | `stats/robustness.py` | Recomputed `multipletests(..., method="holm")` across R2–R9 | Match |
| 16 | Leave-one-out: 1/28 $p<.05$, 17/28 $p<.10$, ranges (`appendix_e:587`) | `stats/robustness.py` | Recomputed all 28 single-row deletions | Match |
| 17 | Leave-one-bank table $p=.244$–$.686$ (`appendix_e:572–580`) | `stats/robustness.py` | Recomputed Model 2 leave-one-bank | Match |
| 18 | Leave-one-year table; only FY2078/79 rejects (`appendix_e:601–611`) | `stats/robustness.py` | Recomputed; other five years $p=.114$–$.384$ | Match |
| 19 | R6 $N=23$, $F(2,10)=5.818$, $p=.021$ (`chapter_05:98–102`) | `stats/robustness.py:34` | Recomputed on `fy != FY2078-79`; exact | Match |
| 20 | R7 bonus adjustment $\beta_E=5.775$ etc. (`chapter_04:445`) | `stats/robustness.py:123–135` | Recomputed; coefficients match; **only BVPS is adjusted** | Partial (F08) |
| 21 | $N=30$ sensitivity $F=4.762$, $p=.024$, BVPS slope 0.709 (`chapter_05:132`) | `stats/robustness.py` | Recomputed with delayed prices | Match |
| 22 | Stale-price scenarios 3.870 (.043) and 3.821 (.044) (`chapter_05:132`) | `stats/robustness.py` | Recomputed both price pairs | Match |
| 23 | MDEs 10.73 / 12.06 / 3.71 (`chapter_04`, power subsection) | derived | Recomputed with $t_{.975,df}$ + noncentral-free formula; 10.73/12.06/3.71 | Match |
| 24 | Wild bootstrap $p=.062$ for baseline and R6 (`chapter_05:132`) | `stats/wild_bootstrap.py` | Re-enumerated 32 patterns; both 2/32 | Match (but see F03) |
| 25 | HC3 formula and leverage check (`appendix_d:318`) | `stats/models.py` | Compared against statsmodels HC3 and the sandwich vignette | Match |
| 26 | Reproducibility recipe (`appendix_d:333–338`; `scripts/verify.py`) | pipeline | Recomputed the checkpoints independently; 30 analysis tests + 6 extraction tests pass | Match with caveat (F19) |

Coverage: 24 of the 26 claim groups are fully reproduced; 2 are partially reproduced because the reported quantity is correct but its scope or interpretation is not (VIF, R7). No reported number failed to reproduce.

---

## 4. Method-by-method review

Verdicts use the mandated set: **Correct**, **Correct with caveats**, **Questionable**, **Incorrect**, **Cannot determine**.

### M01. Sample construction, price-freshness rule, and panel balance — *Correct with caveats*

The rule is: take the first active NEPSE session after the nine-month publication deadline, provided it is within five calendar days; otherwise treat the price as missing, never impute (`dataset.py:6–12`; `appendix_d:182–188`). This is implemented faithfully, and the 28-row frame is exactly 30 minus the two late-resumption cells. Excluding rather than imputing is the right default, and the two excluded cells are named.

Caveat: I could not verify the deadline arithmetic (nine months from fiscal year-end under BAFIA §59(2)), the NEPSE trading calendar, or the actual session dates, because that requires the legal text and exchange calendar, neither of which is in the repository. Those are UNVERIFIED-CANNOT DETERMINE. The thesis does document the rule and its consequences (`appendix_d:182–190`).

### M02. Descriptive statistics (Table 4.1) — *Correct*

All means, standard deviations, minima and maxima reproduce from the frozen CSV, including the pre/post splits and the percentage changes quoted in `chapter_05:73`. The 97.49% ROA standard-deviation increase, which looks like a typo, is arithmetically correct.

### M03. Correlation analysis (Table 4.2) — *Correct*

Pearson correlations and two-sided $p$-values reproduce. The use of the EPS–ROA correlation ($r=.975$) to justify substituting ROA for EPS in R3 is sound and is stated as a design decision rather than a data-driven search.

Minor caveat, folded into F15: with $N=28$, the table reports many unadjusted $p$-values and no multiplicity control; this is conventional for a descriptive table, but the thesis elsewhere is careful about multiplicity, so the asymmetry is worth noting.

### M04. Model 1: two-way fixed effects, HC3, $t(16)$ — *Correct with caveats*

The LSDV estimates, HC3 standard errors, $t$ statistics, $p$-values, $R^2$ and adjusted $R^2$ all reproduce. The df accounting (28 observations, 12 parameters, 16 residual df) is correct and is stated explicitly (`appendix_d:318–320`). Using $t$ rather than normal critical values is appropriate at this df.

Caveats: (i) HC3 at $N=28$ with a maximum leverage of 0.6766 is very conservative, and the model's non-rejection is not robust to the covariance choice in the joint test (F01); (ii) the non-significance of $\beta_E$ is attributed in the abstract and Chapter V to year effects, but bank effects are what destroy the precision (F09); (iii) the level specification and the absence of any serial-correlation diagnostic (F17, F10).

### M05. Model 2: interaction specification — *Correct with caveats*

Every coefficient, standard error, implied post-period slope and the joint Wald statistic reproduce. The interaction terms are the right way to test a slope shift, and the thesis correctly reports the *implied* post slopes rather than only the interaction, which many applied papers fail to do.

Caveats: the model is nearly collinear by construction (post is a linear combination of the year dummies, so the interactions inherit that dependence; see F05); the individual interaction tests have very low power (MDE for $\delta_E$ is 12.06 against a point estimate of −3.12); and the joint test's conclusion depends entirely on the covariance estimator (F01).

### M06. $R^2$, within-$R^2$, and incremental fit — *Correct*

The LSDV $R^2$ is defined correctly (`chapter_03:353`), and the within-$R^2$ values (.1518 for Model 1, .6417 for Model 2) reproduce from the code at `stats/models.py:82–86`. The incremental contributions (0.93pp and 3.9pp over a year-FE-only model with $R^2=.9388$) are also correct, and the thesis is right to warn that the raw $R^2$ is dominated by the fixed effects (`chapter_05:105`). This is one of the stronger parts of the analysis.

### M07. Joint Wald test and the covariance-estimator choice — *Incorrect (as stated)*

The arithmetic is right; the inferential claim is not. I re-estimated all eight joint tests R2–R9 under five covariance estimators:

| Spec | $N$ | Classical $F$ ($p$) | HC0 $F$ ($p$) | HC1 $F$ ($p$) | HC2 $F$ ($p$) | HC3 $F$ ($p$) |
|---|---|---|---|---|---|---|
| R2 baseline | 28 | 9.573 (.0024) | 12.654 (.0007) | 6.327 (.0110) | 6.243 (.0115) | 2.954 (.0850) |
| R3 ROA | 28 | 9.111 (.0029) | 11.520 (.0011) | 5.760 (.0150) | 5.405 (.0182) | 2.463 (.1212) |
| R4 DPS | 28 | 12.997 (.0008) | 17.401 (.0002) | 8.079 (.0052) | 7.691 (.0062) | 2.767 (.0997) |
| R5 transition yr | 23 | 7.170 (.0117) | 12.245 (.0020) | 5.324 (.0266) | 5.700 (.0223) | 2.414 (.1395) |
| R6 mismatch yr | 23 | 28.949 (.0001) | 49.113 (≈0) | 21.353 (.0002) | 17.411 (.0006) | 5.818 (.0211) |
| R7 bonus adj. | 28 | 8.271 (.0043) | 10.634 (.0016) | 5.317 (.0191) | 5.220 (.0202) | 2.365 (.1303) |
| R8 restated EPS | 28 | 8.868 (.0033) | 11.801 (.0010) | 5.901 (.0138) | 5.932 (.0136) | 2.915 (.0874) |
| R9 Kanchan | 27 | 9.108 (.0034) | 12.291 (.0010) | 5.918 (.0149) | 4.998 (.0245) | 1.794 (.2051) |

**Every specification rejects at 5% under classical, HC0, HC1 and HC2. Under HC3, only R6 rejects.** The thesis reports only the HC3 column and therefore reports "no regime shift" for seven of eight specifications. This is not a computational error; it is a reporting choice that determines the headline result.

The choice of HC3 is defensible and pre-specified (`proposal/07_methodology.tex:187`), and HC3 is the conventional recommendation for small samples (Long & Ervin 2000, as summarised in the sandwich vignette, §3). But three things make the omission serious rather than stylistic:

1. The thesis's own *robust* Breusch–Pagan test does not reject homoskedasticity ($p=.213$; `chapter_04:494`), so the heteroskedasticity that motivates HC3 is not established by the diagnostic the thesis prefers. The classical BP does reject ($p=.003$), so the evidence is genuinely mixed — which is exactly why the sensitivity must be shown.
2. HC3 is the most conservative of the HC family, and in this design the maximum leverage is 0.9324 (Model 2, HBL FY2076/77), so a single observation receives HC3 weight $1/(1-h)^2\approx 296$. At that point HC3 is not a mild correction.
3. The difference between "reject" and "do not reject" is the entire finding. A reader cannot evaluate the conclusion without the alternative columns.

Impact: the claim that the baseline data "fail to reject structural stability" is true only under HC3. Under four other standard estimators, the same data reject. Severity: **Critical** (F01).

### M08. Multiplicity control (Holm) — *Correct with caveats*

Holm across the eight joint tests gives an adjusted minimum of 0.1688, matching `chapter_04:443` and `chapter_05:102`. The procedure is implemented correctly (`multipletests(..., method="holm")`) and the family is defined explicitly (R2–R9). This is better practice than most theses at this level.

Caveat: the family stops at the joint tests. The thesis also reports the ten correlation coefficients, the four hypothesis $t$-tests, two BP variants, two normality tests, and nine robustness coefficients, none adjusted. That is normal for exploratory tables, but it means "Holm-adjusted $p=0.169$" should not be read as "the only multiplicity-corrected result in the thesis" (F15).

### M09. Wild-cluster bootstrap — *Questionable*

The code enumerates all $2^5=32$ Rademacher weight patterns, imposes the null, resamples restricted residuals by cluster, refits, and recomputes the HC3 Wald statistic (`wild_bootstrap.py:61–107`). I reproduced $p=2/32=0.0625$ for both the baseline and R6. The implementation is deterministic and internally consistent.

The problem is that the exercise cannot answer the question it is presented as answering:

- With 32 patterns and the observed statistic counted, **the smallest attainable $p$ is $2/32=0.0625$**. The all-$+1$ pattern reproduces the sample and the all-$-1$ pattern reproduces the statistic in absolute value, so both always count. A $p$-value of .0625 is therefore the floor, not a finding.
- Consequently, "the bootstrap flips only the R6 decision" is mechanically forced: no bootstrap $p$ in this design can fall below .05, so R6's HC3 $p=.021$ must "flip" and the baseline's $p=.085$ must not. The comparison carries no information about cluster-robust inference.
- The test statistic inside the bootstrap is HC3, not a cluster-robust statistic (`wild_bootstrap.py:91`), so this is a wild bootstrap of an HC3 Wald test, not the cluster-robust wild bootstrap of Cameron–Miller. It preserves within-cluster residual patterns in the DGP but does not repair the few-cluster covariance problem.
- Webb (2014) shows that Rademacher weights are a poor choice with few clusters and recommends six-point weights, which would give $6^5=7776$ patterns and a far finer $p$-value grid. That alternative is not discussed.

The thesis calls the check "inconclusive at this cluster count" (`chapter_05:132`), which is honest, but the surrounding narrative still treats it as evidence that the HC3 result is not overturned. It is not evidence of anything beyond the floor. Severity: **Major** (F03).

### M10. Robustness suite R1–R9 (excluding R7) — *Correct with caveats*

I reproduced R1–R6, R8 and R9 coefficients and joint tests. The suite varies the sample (R5, R6, R9), the regressor set (R3, R4), and measurement (R8). The leave-one-out and leave-one-year tables reproduce, including the claim that only 1 of 28 single-row deletions yields $p<.05$ and 17 of 28 yield $p<.10$ (`appendix_e:587`).

Caveat: the suite varies *samples and regressors* but not the *inference* (covariance, serial correlation, functional form). That is the central cross-cutting weakness (Section 5.2). A robustness suite that never perturbs the assumption doing the work is not robust to that assumption.

### M11. R7 bonus-capitalisation adjustment — *Questionable*

R7 changes only BVPS: `bvps_adj = bvps / (1 + bonus/100)` (`robustness.py:123–135`). EPS and price are left unadjusted. That is not a bonus-dilution adjustment of the valuation relation; it is a rescaling of one regressor while the dependent variable and the other regressor remain on the old share base. If a bonus issue splits the share, price and EPS should be adjusted on the same factor, or the regression should be run in per-pre-bonus-share units consistently.

The estimates move more than the word "virtually identical" suggests: $\beta_B$ rises from 0.100 to 0.153, $\delta_B$ moves from −1.758 to −1.533, and the joint $F$ falls from 2.954 to 2.365 ($p$ from .085 to .130). The reported $\beta_E=5.775$ (SE 4.145) does reproduce. Severity: **Major** (F08).

### M12. Influence diagnostics (Cook's distance, leverage) — *Correct*

The flagged tables in `appendix_e:513–559` match my recomputation exactly, including the ordering. The $4/N$ threshold is described as a screening rule, not a deletion rule, and the thesis explicitly says HC3 does not neutralise influential observations (`chapter_04:504`). That is the right posture.

Caveat: the diagnostics are reported but not acted on or stress-tested. The highest-leverage rows are HBL FY2076/77 (0.6766 in Model 1, 0.9324 in Model 2). Given that R6's rejection is the only one, a leave-one-observation check on the R6 sample would have been the natural next step. Related: F13.

### M13. Heteroskedasticity diagnostics — *Correct*

Both BP variants reproduce (robust 14.369, $p=.213$; classical 28.183, $p=.003$), and the thesis correctly refuses to pretend they agree (`chapter_04:511`). Reporting both is good practice.

The inferential consequence is not drawn: because the robust variant does not reject, the case for maximal-conservative HC3 is weaker than the thesis implies, and the covariance sensitivity in F01 becomes more important, not less.

### M14. Residual normality (Shapiro–Wilk) — *Correct with caveats*

The statistics and $p$-values reproduce (.92462/.0452; .92155/.0379). With $N=28$ the test has low power, and at $t(14)$–$t(16)$ the $t$ approximation is not very sensitive to moderate non-normality, so the rejection is not fatal.

Caveat: the thesis rejects normality at 5% but does not discuss what follows. In a small sample, non-normality plus HC3 plus high leverage is a combination that argues for bootstrap or randomisation inference, which is exactly the tool the thesis uses badly (M09).

### M15. VIF and collinearity — *Questionable*

The reported VIFs (1.16 for both Model 1 regressors; 10.33/2.28/15.15/24.13 for Model 2) reproduce exactly — but they are computed on the substantive regressors only, with the fixed-effect dummies excluded (`diagnostics.py:25–36`; disclosed at `chapter_03:361` and `chapter_04:504`). On the **fitted design**, the numbers are:

| Design | EPS | BVPS | EPS×Post | BVPS×Post | Worst year dummy |
|---|---|---|---|---|---|
| Model 1 (12 columns) | 5.70 | **12.32** | — | — | 3.92 |
| Model 2 (14 columns) | 14.82 | 12.46 | 27.34 | **259.32** | 118.21 |

So "Model 1 VIF ... Below screen" (`chapter_04:485–487`) is false for the model actually estimated, and Model 2 has a fourth regressor far above any screen (259), which the table does not show. The Model 2 year-dummy VIFs of 89–118 confirm that post-period identification is entangled with the year effects.

This matters for interpretation: the thesis attributes the imprecision of the individual interactions to small $N$, but a large part of it is design collinearity. The disclosure ("excluding fixed-effect dummies") is present, but a reader who reads the table's verdict column will draw the wrong conclusion. Severity: **Major** (F05).

### M16. Power / minimum detectable effects — *Correct with caveats*

The MDEs (10.73 for Model 1 $\beta_E$, 12.06 for Model 2 $\delta_E$, 3.71 for $\delta_B$) reproduce with $t_{.975,df}$ critical values. Reporting MDEs at all is commendable and rare.

Caveat: these are post hoc, computed from the realised HC3 standard errors and design. They are not ex ante power calculations, and they inherit the HC3 conservatism: under a classical covariance the MDEs would be roughly half as large. Presented as "the study could only detect effects of size X", they overstate the design's weakness. Severity: **Minor** (F14).

### M17. Specification comparison and fixed-effect tests — *Correct with caveats*

The pooled OLS, year-FE and two-way FE comparison reproduces, including $R^2$ .136/.919/.948 and the joint tests. The substantive conclusion (bank effects add little to fit conditional on year effects) is correct.

Caveat: the narrative reports $F(4,16)=2.23$ ($p=.112$, classical incremental $F$) while Appendix E reports $1.395$ ($p=.280$, HC3 Wald) for the same restriction, without explaining that the difference is the covariance matrix (`chapter_04:559`; `appendix_e:118`). Both are insignificant, so nothing turns on it, but the juxtaposition is confusing. Severity: **Minor** (F12).

### M18. Price-freshness sensitivity ($N=30$, stale prices) — *Correct*

The $N=30$ model with the two delayed prices ($F=4.762$, $p=.024$; BVPS slope 0.709) and the two stale-price scenarios ($F=3.870$, $p=.043$; $F=3.821$, $p=.044$) all reproduce. The thesis correctly labels these as rule-violating scenarios rather than baseline results, and correctly notes that including them flips the baseline joint test. This is a genuinely informative sensitivity and is handled well.

### M19. Serial correlation — *Questionable (impact cannot be determined)*

The thesis assumes within-bank independence of errors and says so (`chapter_03:352`), but no serial-correlation diagnostic is reported: no Durbin–Watson, no Wooldridge test, no cluster-robust or HAC comparison (a repository-wide search finds no such test). With $T=6$, a levels specification, and persistent bank fundamentals, first-order autocorrelation is plausible.

I cannot determine the direction or size of the resulting bias without the test, so the impact is UNVERIFIED-CANNOT DETERMINE. But the omission is verified, and it is material because HC3 is not robust to within-cluster correlation. If residuals are positively autocorrelated, HC3 standard errors are too small and even the HC3 non-rejections are overstated; if the within-bank variation is dominated by the fixed effects, the bias may be modest. Either way, the thesis cannot currently rule out the first case. Severity: **Major** (F10).

### M20. Interpretation of $\hat\beta_E$ as a valuation multiple — *Incorrect*

`chapter_04:286` says the pre-consolidation earnings slope means "equity investors priced commercial bank shares at approximately 5.58 times reported earnings per share", and Chapter V is organised under "Valuation Multiple Compression" (`chapter_05:88`). $\hat\beta_E$ is the partial derivative of price with respect to EPS holding BVPS and the fixed effects constant. It is not price/EPS. In this sample the mean price is NPR 254.3 and mean EPS is NPR 14.05, so the actual price-to-earnings ratio is about 18.1 (median 17.6); a "5.58 times earnings" multiple is not in the data.

The error is not merely verbal: it makes the magnitudes sound implausibly cheap and supports the "multiple compression" narrative. The correct statement is that a one-rupee increase in EPS is associated with a 5.58-rupee increase in price, conditional on book value. Severity: **Major** (F06).

### M21. Reproducibility assets and documentation — *Correct with caveats*

The pipeline is genuinely reproducible: frozen CSVs, deterministic scripts, asset generators, a `verify.py` that checks the printed numbers, and 36 tests that pass (30 analysis, 6 extraction) when run with the right `PYTHONPATH`. `appendix_d` gives a step-by-step recipe, and `data_analysis/analysis/requirements.txt` pins `statsmodels==0.14.6`, which matches the environment in which the numbers reproduce.

Caveats: `pytest` from the repository root fails collection (three import errors) because the packages are not installed and the `src` layouts are not on the path; there is no root-level `pytest.ini`/`conftest.py` or `pyproject.toml` test configuration. And `appendix_d:4` states the thesis is "submitted without any accompanying repository or code", which is inconsistent with the repository that produced every number. Severity: **Minor** (F19, F16).

---

## 5. Cross-cutting issues

### 5.1 The inference is estimator-contingent, and only one estimator is shown

F01 is not an isolated slip; it is the organising fact of the results chapter. The baseline $p$-value moves from .0007 to .085 depending on the covariance matrix, and the study's conclusion moves with it. Every downstream statement ("fail to reject", "marginal at 10%", "sensitivity-dependent") is a statement about the HC3 column. A thesis that pre-specifies HC3 is entitled to lead with it, but not to withhold the fact that the result is not robust to the choice.

### 5.2 The robustness suite perturbs the sample but not the assumption doing the work

R1–R9 vary rows, regressors and measurement. None varies the covariance estimator, the serial-correlation assumption, the functional form (levels vs logs), or the price deflation. The one assumption that actually determines the answer — HC3 — is held fixed across all nine specifications and then "robustness" is claimed on the basis of the nine. This is the most important methodological criticism in the review after F01 itself.

### 5.3 Disclosure is used as a substitute for correction

Several limitations are disclosed and then contradicted:

- HC3's conservatism is acknowledged, but the abstract still says the result "corrects for small-cluster downward bias" (F04).
- The BVPS post-slope is said to be insignificant and not evidence of a negative association (`chapter_05:92`; `chapter_04:580`), but `chapter_05:207` asserts that "market participants discounted book equity post-consolidation" as a basis for policy (F07).
- R6 is called "an unadjusted sensitivity result" with Holm $p=0.169$ (`chapter_05:102`), but Table 5.1 records "Reject $H_0$ (at 5%)" (F02).
- The VIF exclusion is footnoted, but the table's verdict column still says "Below screen" (F05).
- The bootstrap's coarseness is conceded in a code comment (`wild_bootstrap.py:11–20`), but the narrative treats the exercise as informative (F03).

Individually each is defensible; collectively they mean a reader who reads only the abstract, the tables and the conclusion gets a materially different picture from a reader who reads the caveats.

### 5.4 The design cannot answer the question at conventional power, and the thesis knows it

Residual df of 10–16, maximum leverage above 0.93, MDEs of 12.06 for the interaction of interest, and 15 post-period observations. The honest conclusion is "the design is underpowered", not "there is no regime shift". The thesis says this in places, but the abstract's framing ("The evidence demonstrates ... sensitivity-dependent rather than conclusive") still implies that a conclusive answer was within reach.

### 5.5 Construct validity: three different things are called "the regime shift"

The thesis tests (a) a change in the conditional price–fundamentals relation, (b) a change in the price level after consolidation, and (c) a change in the sample composition caused by mergers. Model 2 identifies (a) only under the assumption that the bank and year effects fully absorb (b) and that the merged entities' post-period fundamentals are measured on a consistent share base. The known FY2078/79 entity mismatch violates that assumption, which is the most likely reason R6 moves so much. The thesis documents the mismatch well; it does not fully separate the three channels.

### 5.6 Multiplicity and the garden of forking paths

Nine specifications × two interactions × several samples produce many chances for a 5% rejection. Under the reported HC3 inference, one appears (R6), and it is the one produced by deleting the known-defective rows after the baseline specification was fixed. The Holm correction across R2–R9 is the right instinct, but the formal decision table still records the unadjusted rejection. A pre-registered single primary test would have avoided the problem; the thesis comes close to this by naming Model 2's joint test "principal", but then reports R6 as a rejection anyway.

### 5.7 Reproducibility is strong where it exists, and absent where it matters

The code reproduces the numbers, but there is no archived output of the covariance-sensitivity analysis, no leverage-adjusted HC3 diagnostics, and no record of the alternative estimators. The infrastructure to do this exists (`stats/models.py` already accepts `cov_type`); the analysis simply does not use it.

---

## 6. What is correct

This is not a low-quality analysis. The following were checked and are right, and several are better than typical practice at this level:

1. **The sample rule is implemented exactly as stated**, with exclusion rather than imputation for stale prices, and the two excluded cells are named (`dataset.py:6–12`; `appendix_d:184–188`).
2. **The panel is balanced and correctly counted**: 28 realised bank-years, 13 pre and 15 post (`dataset.py:9`).
3. **All descriptive statistics and percentage changes reproduce**, including the counter-intuitive 97.49% ROA dispersion increase (`chapter_05:73`).
4. **All correlations and $p$-values reproduce** (`tab:t2_correlations`).
5. **Model 1 and Model 2 coefficients, HC3 standard errors, $t$ statistics and $p$-values reproduce to rounding**, with correct df (16 and 14) and correct $t$ rather than normal inference (`tab:t3_model1`, `tab:t4_model2`).
6. **Implied post-period slopes are reported and reproduce** (2.453 and -1.658), rather than leaving the reader to add coefficients (`chapter_04:257, 296`; `chapter_05:92`).
7. **$R^2$, adjusted $R^2$, within-$R^2$ and the incremental contributions are all correct**, and the thesis correctly warns that raw $R^2$ is dominated by the fixed effects (`chapter_03:353`; `chapter_05:105`).
8. **Both Breusch–Pagan variants are reported and the conflict is acknowledged** (`chapter_04:494, 511`).
9. **Cook's distances and leverage values match exactly**, and the $4/N$ rule is treated as a screen, not a deletion criterion (`appendix_e:513–559`; `chapter_04:504`).
10. **Shapiro–Wilk statistics and $p$-values reproduce**.
11. **The Holm adjustment is implemented correctly** and yields 0.1688 (`chapter_04:443`).
12. **The leave-one-out, leave-one-bank and leave-one-year tables reproduce**, including the unusually honest statement that only 1 of 28 single-row deletions rejects (`appendix_e:587`).
13. **The wild bootstrap is deterministic, correctly enumerated, and documented as coarse** (`wild_bootstrap.py:11–20`), even though its inferential value is nil (F03).
14. **The $N=30$ and stale-price sensitivities reproduce** and are correctly labelled as rule-violating scenarios rather than baseline results (`chapter_05:132`).
15. **The MDEs reproduce**, and reporting them is good practice.
16. **The entity-timing mismatch is identified before estimation and documented** (`chapter_04:442, 634`; `appendix_d:287`; `data_analysis/analysis/ANALYSIS_PLAN.md:15`), which is why R6 exists at all.
17. **The reproducibility apparatus is real**: frozen inputs, deterministic scripts, a verification script, and a passing test suite (`appendix_d:333–338`).
18. **The thesis is candid about many limitations** — serial independence, HC3 conservatism, VIF scope, R6's multiplicity, the bootstrap's coarseness. The problem is what happens after the disclosure (Section 5.3), not the disclosure itself.

---

## 7. Findings

### 7.1 Summary table

| ID | Severity | Finding | Location | Status |
|---|---|---|---|---|
| F01 | **Critical** | All eight joint tests reject at 5% under classical/HC0/HC1/HC2; only R6 rejects under HC3. Sensitivity is never reported, so the headline "no regime shift" is an artefact of one covariance choice. | `chapter_04:443, 511`; `chapter_05:93, 158`; `abstract:17` | VERIFIED |
| F02 | **Major** | The only 5% rejection depends on deleting the rows the thesis knows are entity-mismatched; it is not multiplicity-adjusted and collapses when any single bank is dropped, yet is recorded as "Reject $H_0$". | `chapter_04:443, 634`; `chapter_05:98–102, 160`; `abstract:17`; `appendix_e:601–611` | VERIFIED |
| F03 | **Major** | The wild-cluster bootstrap sits at its structural floor ($2/32=0.0625$) for both models, so it cannot discriminate; the "R6 flips" result is mechanically forced. | `chapter_05:132`; `wild_bootstrap.py:11–20, 97–98` | VERIFIED |
| F04 | **Major** | The abstract and Chapter V claim HC3 corrects "small-cluster downward bias". HC3 is heteroskedasticity-robust, not cluster-robust; the thesis says so elsewhere. | `abstract:15`; `chapter_05:66`; `chapter_03:346, 352` | VERIFIED |
| F05 | **Major** | Reported VIFs exclude fixed-effect dummies. Actual design VIFs are 5.70/12.32 (Model 1) and 14.82/12.46/27.34/259.32 (Model 2). "Below screen" is false for the estimated model, and the worst regressor is unreported. | `chapter_04:485–492, 504, 510`; `chapter_03:361`; `diagnostics.py:25–36` | VERIFIED |
| F06 | **Major** | $\hat\beta_E$ is interpreted as a P/E multiple ("5.58 times earnings"). It is a partial slope; the sample P/E is ≈18.1. | `chapter_04:286`; `chapter_05:88`; `abstract:17` | VERIFIED |
| F07 | **Major** | Chapter V asserts that investors "discounted book equity post-consolidation", contradicting the thesis's own statement that the BVPS post-slope is insignificant and does not establish a negative association. | `chapter_05:207` vs `chapter_05:92`, `chapter_04:580` | VERIFIED |
| F08 | **Major** | R7 adjusts only BVPS for bonus dilution, leaving EPS and price unadjusted; "virtually identical" overstates the change and the test is not a clean dilution test. | `robustness.py:123–135`; `chapter_04:445` | VERIFIED |
| F09 | **Major** | Model 1's non-significance is attributed to year effects, but year-FE-only leaves $\beta_E$ at 2.185 (SE 1.260, $p\approx.098$); adding bank FE triples the SE to 4.096. | `abstract:17`; `chapter_05:86, 173` | VERIFIED |
| F10 | **Major** | No serial-correlation diagnostic or robust alternative is reported, despite a $T=6$ levels panel and an explicit independence assumption. | `chapter_03:352`; pipeline-wide absence | VERIFIED (omission); impact UNVERIFIED |
| F11 | **Minor** | "The observed F is only 29.5% above the 5% critical value" is wrong: 5.818/4.103 = 1.418, i.e. 41.8% above. 29.5% is the *decrease* needed (correct at `chapter_04:443`). | `chapter_05:132` | VERIFIED |
| F12 | **Minor** | The 2.23 and 1.395 bank-FE statistics are the classical and HC3 versions of the same restriction, presented in different places without explanation. | `chapter_04:559`; `appendix_e:118` | VERIFIED |
| F13 | **Minor** | A 24-row variant that drops only the four mismatched rows reproduces R6's coefficients exactly but has leverage 1.0 and a numerically exact fit row, making HC3 degenerate (year-dummy SEs ≈205). Not disclosed. | `robustness.py:34`; `appendix_e:601–611` | VERIFIED |
| F14 | **Minor** | MDEs are post hoc, conditional on the realised HC3 standard errors, and presented as if they were ex ante power. | `chapter_04` power subsection | VERIFIED |
| F15 | **Minor** | Holm is applied only to R2–R9; all other reported tests are unadjusted, and the formal decision table still uses the unadjusted R6 result. | `chapter_04:443`; `chapter_05:144–160` | VERIFIED |
| F16 | **Minor** | Appendix D states the thesis is submitted "without any accompanying repository or code", but the repository is the source of every reported number. | `appendix_d:4` | VERIFIED |
| F17 | **Minor** | The dependent variable and regressors are nominal NPR levels with no deflation or log form; year effects mitigate but do not eliminate scale/inflation confounding. | `chapter_03:271–300` | INFERRED |
| F18 | **Suggestion** | No theory-implied restriction or benchmark is tested; all inference is "coefficient equals zero", never "coefficient is consistent with the residual-income model". | `chapter_03:271–330`; `chapter_05:173–177` | INFERRED |
| F19 | **Minor** | The test suite does not run from the repository root (three collection errors); it passes only with package-specific `PYTHONPATH`. | repo root; `data_analysis/**/tests` | VERIFIED |
| F20 | **Suggestion** | No placebo/pre-trend or rolling-break analysis; the only evidence of a break is a sample deletion, which cannot distinguish a regime shift from a composition effect. | `chapter_04:420–450` | INFERRED |

Counts: **1 Critical, 9 Major, 8 Minor, 2 Suggestion**.

### 7.2 Detailed findings

#### F01 — Joint-test inference is covariance-estimator dependent, and the sensitivity is withheld (Critical)

**Location.** `chapter_04_results_and_discussion.tex:443` (R6 narrative), `:511` (diagnostics discussion), Table 4.6; `chapter_05_summary_and_conclusion.tex:93` (joint test), `:158` (decision table); `abstract.tex:17`.

**Evidence.** Re-estimation of all eight joint tests under five covariance estimators, reported in the table in Section M07. Under classical, HC0, HC1 and HC2, every one of R2–R9 rejects at 5%. Under HC3, only R6 does. The HC3 column is the only one reported. The thesis's own Koenker BP test does not reject homoskedasticity ($p=.213$; `chapter_04:494`). Maximum leverage in Model 2 is 0.9324 (recomputed; HBL FY2076/77), implying an HC3 weight of ≈296 on one row. HC3 is pre-specified (`proposal/07_methodology.tex:187`) and its conservatism is acknowledged (`chapter_03:346`), but no alternative covariance is ever shown.

**Status.** VERIFIED (recomputed independently; statsmodels 0.14.6, matching `requirements.txt`).

**Impact.** The study's central empirical claim — that the data do not reject structural stability — holds only under the most conservative estimator in the family. A reader is entitled to see that the same data reject under four standard alternatives. This is the difference between "the evidence is weak" and "the evidence is contrary under conventional inference". It does not prove a regime shift, but it does mean the thesis cannot claim the absence of one.

#### F02 — The only rejection rests on an ex post deletion and is recorded as a formal rejection (Major)

**Location.** `chapter_04:443, 634`; `chapter_05:98–102` and Table 5.1 row at `:160`; `abstract.tex:17`; `appendix_e:601–611`.

**Evidence.** R6 deletes the five FY2078/79 bank-years, which pair standalone pre-merger fundamentals with April 2023 post-merger prices (`chapter_04:442, 634`; `appendix_d:287`). The deletion is motivated by a real, documented defect — the mismatch is flagged in `data_analysis/analysis/ANALYSIS_PLAN.md:15` before estimation — and the thesis explains why the fifth (unaffected) row is also dropped (`chapter_04:442`). But R6 as a reported specification does not appear in the proposal (no mention of "entity", "mismatch", "R6" or FY2078/79 in `src/proposal/`), so it functions as a robustness variant rather than a pre-specified primary test, and the baseline retains the knowingly contaminated rows. Recomputations: (i) dropping only the four merged banks' mismatched rows (24 rows) reproduces R6's coefficients exactly, so the result does not depend on also dropping the non-merged bank; (ii) in the R6 sample, dropping any one bank yields $F=0.615$–$1.309$, $p=0.329$–$0.572$; (iii) the thesis's own full-sample leave-one-bank table gives $p=.244$–$.686$ (`appendix_e:572–580`); (iv) the leave-one-year table shows every other year deletion gives $p=.114$–$.384$ (`appendix_e:601–611`); (v) Holm-adjusted $p=0.169$. Despite all of this, Table 5.1 records "Reject $H_0$ (at 5%)".

**Status.** VERIFIED (i and ii recomputed; iii–v reproduced from thesis tables).

**Impact.** The one statistically significant result is fragile in every dimension that matters: sample perturbation, bank composition, multiplicity and estimator choice. Presenting it as a formal rejection in the decision table overstates the evidence. The prose elsewhere is appropriately cautious, which makes the table row the problem.

#### F03 — The wild-cluster bootstrap is at its floor (Major)

**Location.** `chapter_05:132`; `data_analysis/analysis/stats/wild_bootstrap.py:11–20, 54–58, 85–98`.

**Evidence.** With $G=5$, Rademacher weights give $2^5=32$ patterns. The all-$+1$ pattern reproduces the observed sample and the all-$-1$ pattern reproduces the observed statistic in absolute value, so at least 2 of 32 always count: $\min p = 0.0625$. I reproduced $p=2/32$ for both the baseline and R6. The code comment concedes the coarseness and the counting convention. The statistic recomputed inside the bootstrap is HC3, not cluster-robust (`wild_bootstrap.py:91`). Webb (2014) documents the poor properties of Rademacher weights with few clusters and proposes six-point weights ($6^5=7776$ patterns here).

**Status.** VERIFIED (re-enumerated all 32 patterns; p-value arithmetic confirmed).

**Impact.** The bootstrap cannot produce a 5% rejection for any specification, so the reported "flip" of R6 and non-flip of the baseline are arithmetically predetermined. The check should either be removed or replaced with a finer-support bootstrap that can actually discriminate.

#### F04 — HC3 is described as correcting "small-cluster downward bias" (Major)

**Location.** `abstract.tex:15`; `chapter_05_summary_and_conclusion.tex:66`; contradicted at `chapter_03:346, 352`.

**Evidence.** The abstract says the study resolves prior limitations "by ... correcting for small-cluster downward bias"; Chapter V says "To safeguard against small-cluster downward bias ($G=5$), all inferential statistical tests ... were conducted using the MacKinnon–White HC3 ... estimator". HC3 is a heteroskedasticity-consistent estimator; it does not cluster. `chapter_03:346` explicitly says "Cluster-robust covariance estimators are distinct from HC3 and can have unreliable finite-sample behavior when the number of clusters is small ($G=5$)", and `:352` says the panel is "too small to support a reliable cluster-robust correction".

**Status.** VERIFIED (text against text; the econometric distinction is standard and is documented in the sandwich vignette and Cameron & Miller 2015).

**Impact.** This is a false methodological claim in the two most-read parts of the thesis. It also obscures the real issue: because HC3 is not cluster-robust, within-bank dependence is unaddressed (F10), and the abstract's claim of a small-cluster correction is exactly backwards.

#### F05 — VIFs are computed on a design that excludes the fixed effects (Major)

**Location.** `chapter_04:485–492` (Table 4.6), `:504` (note), `:510` (narrative); `chapter_03:361`; `stats/diagnostics.py:25–36`.

**Evidence.** Recomputed full-design VIFs: Model 1 EPS 5.70, BVPS 12.32; Model 2 EPS 14.82, BVPS 12.46, EPS×Post 27.34, BVPS×Post 259.32; Model 2 year dummies 89.81/104.68/118.21. Reported values are 1.16/1.16 and 10.33/2.28/15.15/24.13. The note discloses that FE dummies are excluded.

**Status.** VERIFIED (recomputed on the exact LSDV design matrices).

**Impact.** The table's "Below screen" verdict for Model 1 is wrong for the model that produced the reported coefficients, and the most severe collinearity in Model 2 (BVPS×Post, VIF 259) is not shown at all. Because the individual interaction estimates are the object of $H_3$/$H_4$, understating their variance inflation materially affects the interpretation of precision.

#### F06 — The earnings slope is reported as a P/E multiple (Major)

**Location.** `chapter_04:286`; `chapter_05:88` (heading "Valuation Multiple Compression"); `abstract.tex:17`.

**Evidence.** "Equity investors priced commercial bank shares at approximately 5.58 times reported earnings per share." The model is $\text{Price}=\alpha+\beta_E\text{EPS}+\beta_B\text{BVPS}+\mu_i+\lambda_t+\varepsilon$; $\hat\beta_E$ is a partial slope in NPR per NPR, not a ratio. Sample means: price 254.34, EPS 14.05, implying P/E ≈18.1 (median 17.6). Coefficients verified.

**Status.** VERIFIED (model algebra and sample moments recomputed).

**Impact.** A 5.58 "multiple" is not a feature of these data, and the "multiple compression" framing built on it is not supported by the estimates. The correct interpretation (a one-rupee EPS increment is associated with a 5.58-rupee price increment, conditional on BVPS and the fixed effects) is less dramatic but defensible.

#### F07 — The conclusion asserts a book-value discount the analysis says is unsupported (Major)

**Location.** `chapter_05:207`, against `chapter_05:92` and `chapter_04:580`.

**Evidence.** `chapter_05:207`: "Because market participants discounted book equity post-consolidation, commercial bank management should enhance voluntary footnote disclosures..." `chapter_05:92`: the implied post slope of −1.658 "do[es] not establish a decline in either slope or a negative book-value association". `chapter_04:580`: the negative implied BVPS slope "is statistically insignificant ... It cannot therefore be..." The post-slope $p$-value is .161.

**Status.** VERIFIED (direct contradiction between thesis passages).

**Impact.** A policy recommendation is justified by an effect the thesis elsewhere says is not established. This is the clearest instance of the disclosure-then-contradiction pattern in Section 5.3.

#### F08 — R7 adjusts only one side of the bonus-dilution relation (Major)

**Location.** `data_analysis/analysis/stats/robustness.py:123–135`; `chapter_04:445`.

**Evidence.** `bvps_adj = bvps / (1 + bonus/100)`; EPS and price are untouched. Recomputed: $\beta_B$ 0.100→0.153, $\delta_B$ −1.758→−1.533, joint $F$ 2.954→2.365 ($p$ .085→.130); the reported $\beta_E=5.775$ (SE 4.145) is correct. The text calls the estimates "virtually identical".

**Status.** VERIFIED (code read and re-run).

**Impact.** The robustness check does not test what it claims to test (whether bonus issues distort the value-relevance relation); it tests a one-sided rescaling. The description "virtually identical" is also too strong for a 50% change in $\beta_B$ and a 20% change in the joint $F$.

#### F09 — Model 1's non-significance is misattributed to year effects (Major)

**Location.** `abstract.tex:17`; `chapter_05:86, 173`.

**Evidence.** The abstract says the insignificant slopes show "that common fiscal-year fixed effects absorb macro-temporal price movements". Recomputed: with year effects only, $\beta_E=2.1854$ (SE 1.2603, $p\approx.098$ on $t(20)$); with bank effects added, $\beta_E=2.0948$ (SE 4.0955, $p=.616$ on $t(16)$). The point estimate barely moves; the standard error triples. Bank FE absorb the cross-bank EPS variation that identifies $\beta_E$.

**Status.** VERIFIED (recomputed both specifications on the 28-row sample).

**Impact.** The stated mechanism is wrong. This matters for the thesis's diagnosis of why prior Nepalese studies found significant value relevance: it is not "macro-year absorption" but the removal of cross-sectional variation by bank effects, which is a much more consequential design choice.

#### F10 — No serial-correlation diagnostic (Major)

**Location.** `chapter_03:352` (assumption stated); no diagnostic anywhere in `stats/` or the appendices.

**Evidence.** A repository-wide search for Durbin–Watson, Wooldridge, HAC/Newey–West or cluster-robust alternatives finds only the textual acknowledgement. The design is a levels panel with $T=6$ and persistent fundamentals.

**Status.** VERIFIED that no test is reported; the magnitude and direction of any bias are UNVERIFIED-CANNOT DETERMINE.

**Impact.** HC3 does not correct within-bank correlation. If residuals are positively autocorrelated, the reported standard errors are too small and the HC3 non-rejections are themselves overstated. The thesis cannot currently exclude this, and the omission is more serious than the ones it does disclose.

#### F11 — "29.5% above the critical value" is wrong (Minor)

**Location.** `chapter_05:132`.

**Evidence.** $5.8177/4.1028=1.4178$, i.e. 41.8% above. The 29.5% figure is the proportional decrease that would bring the statistic to the critical value: $1-4.1028/5.8177=0.2948$, which is correctly stated at `chapter_04:443` ("a 29.5% decrease ... would remove the raw rejection").

**Status.** VERIFIED.

**Impact.** A factual error in the conclusion, in the direction of understating how far the one rejection sits above the threshold. It does not change the decision.

#### F12 — Two bank-FE statistics with different nulls are juxtaposed (Minor)

**Location.** `chapter_04:559`; `appendix_e:118`.

**Evidence.** $F(4,16)=2.23$ ($p=.112$, `chapter_04:559`) is the classical incremental $F$ for the four bank dummies; $1.395$ ($p=.280$, `appendix_e:118`) is the HC3 Wald statistic for the same restriction. Both are insignificant; neither location explains that the two numbers differ because of the covariance matrix, not because they test different hypotheses.

**Status.** VERIFIED (both figures reproduced under the respective covariance estimators).

**Impact.** Reader confusion rather than a wrong conclusion.

#### F13 — The 24-row variant makes HC3 degenerate (Minor)

**Location.** `robustness.py:34`; `chapter_04:442`; `appendix_e:601–611`.

**Evidence.** Dropping only the four merged banks' FY2078/79 rows (24 rows) reproduces R6's coefficients exactly — the thesis says so at `chapter_04:442` ("numerically identical estimates") — but one row (NMB FY2078/79) has leverage 1.0 and a residual of ≈$3\times10^{-12}$: it is the only observation in its year and is fitted exactly by the year dummy. The HC3 weight $1/(1-h)^2$ is then undefined in the limit, and year-dummy standard errors explode to ≈205. The HC3 joint $F$ is still 5.8177 ($p=.0211$). The coefficient identity is disclosed; the covariance degeneracy is not.

**Status.** VERIFIED (recomputed).

**Impact.** The R6 result is numerically fragile even where the coefficients are stable. This is not disclosed, and it reinforces F02.

#### F14 — MDEs are post hoc (Minor)

**Location.** `chapter_04` power/MDE subsection.

**Evidence.** The MDEs use the realised residual df and the realised HC3 standard errors. They reproduce (10.73, 12.06, 3.71) but are conditional on the design and the covariance choice.

**Status.** VERIFIED (recomputed) for the numbers; INFERRED for the "ex ante power" reading.

**Impact.** The design looks less powerful than it would under a classical covariance. Presented correctly, the MDEs support the "underpowered" conclusion; presented as they are, they overstate it.

#### F15 — Multiplicity control is narrower than the claims (Minor)

**Location.** `chapter_04:443`; `chapter_05:144–160`.

**Evidence.** Holm covers R2–R9 only. Correlation tests, the four hypothesis $t$-tests, the two BP variants, the two normality tests and the nine robustness coefficients are unadjusted. Table 5.1 uses the unadjusted R6 $p$-value.

**Status.** VERIFIED.

**Impact.** The thesis's multiplicity discipline is better than average but is applied to one family only, and the formal decision table falls outside that family.

#### F16 — Repository statement contradicts the artifact (Minor)

**Location.** `appendix_d:4`.

**Evidence.** "This appendix is the reproducibility record for a thesis submitted without any accompanying repository or code." The repository contains the pipeline, the frozen data and the generated assets.

**Status.** VERIFIED.

**Impact.** Documentation inconsistency; a reader may conclude the code is unavailable when it is not.

#### F17 — Levels, nominal NPR, no deflation or log form (Minor)

**Location.** `chapter_03:271–300`.

**Evidence.** Both sides of the regression are nominal per-share NPR levels. Year effects absorb common nominal growth but not bank-specific scale or inflation-driven re-rating.

**Status.** INFERRED (no deflation/log specification exists to test the counterfactual).

**Impact.** The coefficient magnitudes and the post-period shift may partly reflect scale and price-level changes rather than a change in the valuation relation. The year effects provide substantial protection, which is why this is Minor rather than Major.

#### F18 — No test of a theory-implied restriction (Suggestion)

**Location.** `chapter_03:271–330`; `chapter_05:173–177`.

**Evidence.** Every hypothesis is a zero restriction. The residual-income framework also implies sign and magnitude restrictions on the book-value coefficient, and the thesis never tests any of them, so "value relevance" is operationalised only as "coefficient differs from zero".

**Status.** INFERRED (the absence is verified; the specific restriction is not asserted here because Ohlson 1995 full text was not accessible — see Section 9.3).

**Impact.** The analysis cannot distinguish "the model is correctly specified but imprecise" from "the model is misspecified relative to the theory".

#### F19 — Tests do not run from the repository root (Minor)

**Location.** Repository root; `data_analysis/analysis/tests`, `data_analysis/data_extract/tests`.

**Evidence.** `python -m pytest` from the root yields three collection errors (`ModuleNotFoundError` for `data_extract.normalize`, `tests.conftest`, `analysis.stats...`). With `PYTHONPATH=analysis` and cwd `data_analysis/analysis`, 30 tests pass; with `PYTHONPATH=data_extract/src`, 6 extraction tests pass.

**Status.** VERIFIED (both invocations run).

**Impact.** A replicator following the obvious command gets errors, which undermines the reproducibility claim even though the tests themselves pass.

#### F20 — No placebo or pre-trend analysis (Suggestion)

**Location.** `chapter_04:420–450`.

**Evidence.** The only evidence of a break is a year deletion. There is no placebo "post" date, no pre-period break test, and no event-study plot.

**Status.** INFERRED.

**Impact.** With 15 post observations and one treated period, a placebo break test in the pre-period would have been the cheapest way to show that the R6 pattern is not an artefact of the design. Its absence is a missed opportunity rather than an error.

---

## 8. Open questions

These are questions the review cannot answer from the repository and that would change the assessment if answered differently.

1. **Legal deadline arithmetic.** Were the nine-month deadlines computed from the fiscal year-end or from the AGM date, and do they match BAFIA §59(2) and the actual NEPSE session calendar? (`appendix_d:182–190` describes the rule but not the derivation.) UNVERIFIED-CANNOT DETERMINE.
2. **The two delayed observations.** HBL and NIMB FY2077/78 resume trading well outside the five-day window. The thesis excludes them from the baseline and includes them only in the $N=30$ sensitivity. Is the delayed price a genuine market price for the same entity, or a stale quote? `appendix_d:188` suggests the former, but I could not check the underlying market data.
3. **Whether the four mismatched rows are the complete and correct set.** `appendix_d:287` names them (GBIME, HBL, KBL, NIMB), and `chapter_04:442` explains the five-row R6. The remaining question is whether the merger completion dates confirm that only FY2078/79 is affected and that no post-period row carries the same standalone/consolidated mismatch. The `entity_mismatch` flag in the frozen CSV is taken as correct.
4. **Whether the author noticed the HC3 degeneracy in the 24-row variant.** The thesis correctly says the four-row exclusion gives numerically identical estimates (`chapter_04:442`), but the surviving single-year observation is fitted exactly (leverage 1.0), so the HC3 variance of the year dummy is numerically undefined. Was the covariance checked, or only the coefficients? (See F13.)
5. **Intended meaning of "small-cluster" in the abstract.** Is this a wording error for "small-sample", or does the author believe HC3 is cluster-robust? The answer determines whether F04 is a drafting slip or a conceptual error.
6. **Which covariance estimator the author would regard as primary if HC3 were not pre-specified.** The proposal fixes HC3 (`proposal/07_methodology.tex:187`), so this is counterfactual, but the answer would clarify whether the "no regime shift" conclusion is a pre-registered commitment or a post hoc rationalisation.
7. **Whether the MDEs were computed before or after seeing the estimates.** If before, they are a legitimate design statement; if after, they are descriptive.
8. **Whether the 30 reports' extracted figures were independently checked.** Out of scope by instruction, but it is the largest remaining single point of failure.

---

## 9. Verification log

### 9.1 Environment and method

- Python 3.14.5; numpy 2.4.6; pandas 3.0.3; scipy 1.17.1; statsmodels 0.14.6 (matches the pin in `data_analysis/analysis/requirements.txt`).
- All recomputation in `C:\Users\Hellx\AppData\Local\Temp\opencode\review_repro\`, using standalone scripts that read `data_analysis/data_extract/output/manual_review/mps_rd_joined_panel.csv` and `..._bonusadj.csv` directly. No repository package was imported, so no bytecode or cache was written into the tree.
- Design matrices were built with `patsy`/`statsmodels` formulas identical to `stats/models.py`; HC3 fits used `cov_type="HC3", use_t=True` to match the pipeline's $t$ inference.
- Tolerances: coefficients/SE to 1e-4; $p$-values to the thesis's printed rounding; $R^2$ to 1e-4.

Scripts used (all in scratch):

| Script | Purpose |
|---|---|
| `repro.py`, `repro2.py` | Coefficients, SEs, $R^2$, joint tests for Models 1–2 and R1–R9 |
| `desc.py` | Table 4.1 descriptives and percentage changes |
| `cooks.py`, `lev.py`, `lev_rows.py` | Cook's distances, leverage, flagged rows |
| `hc_all.py`, `cov.py` | Joint tests under classical/HC0/HC1/HC2/HC3 |
| `vif.py`, `vif1.py` | Substantive-only and full-design VIFs |
| `f_test.py` | Fixed-effect joint tests and specification comparison |
| `n30.py` | $N=30$ and stale-price scenarios |
| `slopes.py` | Implied post-period slopes and their SEs |
| `extra.py` | Holm, leave-one-out, MDEs, normality, BP |
| `consolidated.py` | Consolidated re-run of VIFs, leverage, covariance table, R6 23/24-row comparison |
| `yearonly_t.py` | Year-FE-only vs two-way FE comparison for F09 |
| `r6lob.py` | Leave-one-bank in the R6 sample for F02 |
| `pe.py` | Sample price/EPS ratios for F06 |

### 9.2 External sources actually opened

1. Zeileis, A. *Econometric Computing with HC and HAC Covariance Matrix Estimators* (sandwich package vignette). https://cran.r-project.org/web/packages/sandwich/vignettes/sandwich.pdf — used for the HC0–HC3 definitions, the HC3 leverage weighting $1/(1-h_{ii})^2$, and the reference to Long & Ervin (2000) recommending HC3 in small samples.
2. Cameron, A. C., & Miller, D. L. (2015). *A Practitioner's Guide to Cluster-Robust Inference*. Journal of Human Resources 50(2), 317–372. https://cameron.econ.ucdavis.edu/research/Cameron_Miller_JHR_2015_February.pdf — used for the few-cluster problem, the $G=50$ rule of thumb, and the wild-cluster bootstrap recommendation.
3. Webb, M. D. (2014). *Reworking Wild Bootstrap Based Inference for Clustered Errors*. Queen's Economics Department Working Paper 1315. https://www.econ.queensu.ca/sites/econ.queensu.ca/files/qed_wp_1315.pdf — used for the $2^G$ support of Rademacher weights and the six-point weight alternative.
4. statsmodels documentation, `RegressionResults.get_robustcov_results` (HC0–HC3), https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.RegressionResults.get_robustcov_results.html — used to confirm the HC3 implementation and the $t$/$F$ reference distributions.
5. statsmodels documentation, `het_breuschpagan`, https://www.statsmodels.org/stable/generated/statsmodels.stats.diagnostic.het_breuschpagan.html — used to confirm that `robust=True` is the Koenker studentised variant.
6. statsmodels documentation, `variance_inflation_factor`, https://www.statsmodels.org/stable/generated/statsmodels.stats.outliers_influence.variance_inflation_factor.html — used to confirm that the function returns the VIF of a column conditional on the other columns supplied, which is why excluding dummies changes the result.
7. statsmodels documentation, `OLSInfluence`, https://www.statsmodels.org/stable/generated/statsmodels.stats.outliers_influence.OLSInfluence.html — used for the leverage/Cook's distance definitions.
8. statsmodels documentation, `multipletests`, https://www.statsmodels.org/stable/generated/statsmodels.stats.multitest.multipletests.html — used to confirm the Holm implementation.
9. Crossref record for Ohlson, J. A. (1995), *Earnings, Book Values, and Dividends in Equity Valuation*, Contemporary Accounting Research 11(2), doi:10.1111/j.1911-3846.1995.tb00461.x — bibliographic confirmation only; **full text not opened**.
10. Crossref record for Cook, R. D. (1977), *Detection of Influential Observation in Linear Regression*, Technometrics 19(1), doi:10.1080/00401706.1977.10489493 — bibliographic confirmation only; the $4/N$ threshold is a convention, not a result of that paper.
11. Crossref record for MacKinnon, J. G., & White, H. (1985), *Some Heteroskedasticity-Consistent Covariance Matrix Estimators with Improved Finite Sample Properties*, Journal of Econometrics 29(3), 305–325, doi:10.1016/0304-4076(85)90045-3 — bibliographic confirmation only; **full text not opened**.

### 9.3 What could not be run or opened

- **PDF extraction of the 30 annual reports.** Out of scope by instruction; the frozen CSV is treated as ground truth. This is the largest unverified layer.
- **NEPSE trading calendar and session dates.** No exchange calendar in the repository; the freshness-rule dates were taken as given.
- **BAFIA §59(2) text.** The nine-month deadline was not independently checked against the statute.
- **Ohlson (1995) full text.** Only the Crossref record was accessible. The theoretical claim that the residual-income framework implies a particular book-value coefficient is therefore marked UNVERIFIED and is not used as a basis for a finding beyond F18's generic "no restriction is tested".
- **MacKinnon & White (1985) full text.** Only bibliographic metadata was accessible; the HC3 attribution is taken from the thesis and from the sandwich vignette / statsmodels documentation, not from the original paper.
- **`websearch`.** Returned HTTP 402 in this environment; all source retrieval was by direct URL and `Invoke-WebRequest` + `pdftotext`. One attempted MacKinnon–White download resolved to an unrelated Queen's working paper and was discarded; one attempted Ohlson download returned a 3 KB error page and was discarded.
- **Formal power analysis.** Only the thesis's MDE formula was reproduced; no simulation-based power analysis was run.

### 9.4 Read-only confirmation

`git status` at the start of the review was clean at commit `2d195bfb`. At the end of the review, the only untracked path is `docs/thesis_review/v1/` containing this file. No thesis source, analysis code, data file, configuration, asset or test was modified, renamed, deleted or reformatted. The test runs used `PYTHONDONTWRITEBYTECODE=1` and `-p no:cacheprovider`, and were executed from the package directories so that no cache directory was created in the repository.

---

## 10. Prioritized recommended actions (not applied)

Nothing below has been implemented. They are ordered by how much they would change the thesis's evidential standing.

### Priority 0 — must address before the inference can stand

1. **Report the covariance sensitivity (F01).** Add a table with classical, HC0, HC1, HC2 and HC3 for all eight joint tests. State plainly that the "no regime shift" conclusion is HC3-specific, and explain why HC3 is retained (pre-specification, small-sample recommendation) despite the contrary results. If the conclusion survives, it must survive explicitly, not by omission.
2. **Reconcile the R6 decision with its own caveats (F02, F15).** Either remove the "Reject $H_0$" row from Table 5.1, or relabel it as an unadjusted, non-pre-specified sensitivity that does not survive multiplicity correction or leave-one-bank deletion. Report the leave-one-bank result for the R6 sample ($p=.329$–$.572$), which is currently missing.
3. **Correct the small-cluster claim (F04).** Replace "correcting for small-cluster downward bias" in the abstract and Chapter V with an accurate description: HC3 addresses heteroskedasticity, not clustering; within-bank dependence is assumed, not corrected.

### Priority 1 — substantially strengthens or repairs reported results

4. **Replace or drop the wild bootstrap (F03).** Use Webb's six-point weights ($6^5=7776$ patterns) or a score bootstrap, and report the number of patterns and the attainable minimum $p$. If the Rademacher version is retained, state the $2/32$ floor explicitly and stop describing the result as informative.
5. **Report full-design VIFs alongside the substantive-only ones (F05).** Add the FE dummies to the VIF computation, or report condition numbers for the full design. Discuss the 259 VIF on BVPS×Post and what it implies for the precision of $\delta_B$.
6. **Fix the multiple interpretation (F06).** Replace "5.58 times earnings" with the partial-slope interpretation, and either drop the "valuation multiple compression" framing or define the multiple properly and report it separately.
7. **Remove or support the post-consolidation book-value discount claim (F07).** Either delete `chapter_05:207` or rewrite it as a hypothesis for future research.
8. **Rebuild R7 as a consistent bonus adjustment (F08).** Adjust price, EPS and BVPS on the same share base (or run in per-pre-bonus-share units), and re-describe the result without "virtually identical".
9. **Correct the year-effect attribution (F09).** State that bank fixed effects, not year effects, absorb the identifying variation, and report the year-FE-only estimate (2.185, SE 1.260) for transparency.
10. **Add a serial-correlation diagnostic (F10).** Wooldridge test for AR(1) in panel data, or a comparison with bank-clustered / Driscoll–Kraay standard errors. If the panel is too short for cluster-robust inference (as the thesis argues), say what that implies for the reliability of all reported standard errors, not only for the joint test.

### Priority 2 — corrections and clarifications

11. Fix the 29.5% / 41.8% error (F11).
12. Explain the 2.23 vs 1.395 distinction or drop one (F12).
13. Disclose the 24-row leverage-1.0 degeneracy (F13).
14. Describe the MDEs as post hoc and HC3-conditional, or recompute them under a classical covariance (F14).
15. Correct the Appendix D repository statement (F16).
16. Add a deflated or log specification as a robustness check (F17).
17. Add a root-level `pyproject.toml`/`pytest.ini` or install the packages so `pytest` works from the root (F19).
18. Add a pre-period placebo break test (F20).
19. Test at least one theory-implied restriction or benchmark, or state explicitly that all hypotheses are zero restrictions (F18).

### What would change the review's bottom line

If the author can show that (a) the covariance sensitivity is as reported here and (b) the HC3 choice is defended on pre-specification and small-sample grounds with the alternatives disclosed, then F01 becomes a presentational issue rather than a critical one. Nothing else in the review would move the assessment as much. Conversely, if the six-point-weight bootstrap or a bank-clustered alternative also fails to reject in the baseline, the "no conclusive regime shift" conclusion would be materially strengthened — which is precisely why those analyses should have been run.
