# Final Review of the Data Analysis (v2) — Closure, New Content, and Build

**Repository:** `~/workspace/verbose-chainsaw`, HEAD `b4339bb` ("Add Within-R2 formula to Ch3 (m20/s5, v35)").
**Review date:** 2026-11-14. **Reviewers:** coordinator + three independent subagents
(numeric recomputation, build + tests, minors closure).
**Read-only:** no file in the repo was modified except this review file, under
`docs/thesis_review/v2/`. No commits, no pushes, no edits to thesis, code, or tests.
Recomputation was done only in scratch under `~/workspace/final-review-scratch/`.

**Background:** the independent data-analysis review v1 (`docs/thesis_review/v1/`,
2026-11-12) recorded 14 Majors (M1–M14), 40 minors (m1–m40), and 8 suggestions
(s1–s8). Its items were implemented in commits `0283469`, `cbeda68`, `83aa36c`,
`e558dfb`, `0619d4a` (pushed), then `f716765` (surgical P2 patches, v33),
`ce3566c` (s1 + s2, v34), `b4339bb` (m20/s5, v35). The implementation log and plan
claim every v1 item is now closed. This review verifies that claim independently,
with zero tolerance for unverified claims.

**Status key:** **V** = VERIFIED (method stated), **I** = INFERRED (basis stated),
**U** = UNVERIFIED / CANNOT DETERMINE (reason stated).
Severity: Critical / Major / Minor / Suggestion, as in v1.

## 1. Scope, method, and limits

Four areas, one verdict each (§2). Method:

- **Closure (§3):** every v1 item checked against the current tree (thesis `.tex`,
  code, tests, generated outputs). The implementation log was treated as a claim to
  check, never as evidence. Majors and suggestions were checked by the coordinator;
  all 40 minors by an independent subagent.
- **New content (§4):** independent recomputation from scratch (own numpy QR-based
  OLS + own HC3 + own Wald F; statsmodels 0.14.6 only as cross-check) of every number
  added since v1, plus the highest-risk standing numbers. Scratch:
  `~/workspace/final-review-scratch/numeric/`.
- **Fresh-error scan (§5):** line-by-line read of `git diff 0619d4a..b4339bb`
  (the three post-push commits) for new errors, plus Ch4-vs-Ch5 number agreement
  and Table 8 note verification against the pipeline.
- **Build + tests (§6):** full pytest under the pinned 0.14.6 venv, and a fresh
  4-pass build from a new work dir, output as `thesis-full-ch1-5-v35-final-check.pdf`
  (the v35 PDF was not overwritten).

**Limits (carried from v1, unchanged):** extraction was not re-audited (ground truth
as agreed); figure pixels were not verified; R3/R4/R5/R7/R8 *coefficients* were not
independently recomputed by the v1 team, but this review's numeric agent did
recompute R5/R6 Wald tests and all R2–R9 post slopes from scratch, and the
coefficients in generated T5 were checked against the thesis tables. Settled design
decisions (MPS_RD design, the 5-day rule as a choice, HC3 as designated inference)
were not re-litigated.

## 2. Verdicts (one per area)

| Area | Verdict |
|---|---|
| 1. Closure verification | **NOT CLEAN — substantially closed with exceptions.** 13 of 14 Majors closed (M14 partial). 33 of 40 minors closed, 5 partial, 1 not closed, 1 not applicable as stated. 6 of 8 suggestions closed; 2 not adopted and undocumented. The implementation log's claim that "no review item remains open" is **not sustained as stated**. |
| 2. New-content verification | **ONE MATERIAL ERROR.** Everything reproduces exactly except the s1 M2 wild-bootstrap p-value: the thesis reports 0.031 (1/32); independent enumeration gives 0.062 (2/32). The error is a floating-point artifact, but the reported number and the derived "each decision flips" claim are wrong. All other new numbers (s2 post slopes, m20/s5 formula, descriptives corrections, Table 10 fix) and all standing numbers re-checked reproduce exactly. |
| 3. Fresh-error scan | **ONE NEW ERROR, plus one pre-existing defect still live.** The m14 edit dropped a period in the Chapter 4 Table 4 note. The App E flagged-observation tables (m19) are still out of descending Cook's-distance order. No other new errors in the three diffs: no wrong numbers, no broken LaTeX, no Ch4/Ch5 disagreements, no stale cross-references found. |
| 4. Build + tests | **CLEAN.** 30/30 tests pass under pinned statsmodels 0.14.6. Fresh build: 164 pages, 0 errors, 0 undefined references, 0 bibtex warnings, exactly one overfull (the standing 0.27353pt Chapter III overfull; the Table 10 overfull is gone, no new overfull). Every corrected value is present in the built PDF and every old wrong value is absent. |

**Overall verdict:** the thesis is **not final as written**. One Major fix (the M2
bootstrap p-value and its sentence, in Chapters 4 and 5 and in the test) plus a
small number of Minor fixes are required first. The core is sound: every headline
number re-checked reproduces exactly, and the qualitative conclusions are
unaffected by the bootstrap correction — in fact the correction strengthens the
"inconclusive, fragile decisions" conclusion.

## 3. Area 1 — Closure verification

### 3.1 Majors (M1–M14)

| ID | Verdict | Evidence (file + location) |
|---|---|---|
| M1 | CLOSED (V) | MDE paragraph in Ch3:365 and Ch5:108 (10.73 / 12.06 / 3.71 NPR, 80% power, df 14, "not evidence that smaller effects are absent"). Numbers re-verified by numeric recomputation (§4). |
| M2 | CLOSED (V) | "Earnings dominate" / "flight to book value" occur 0 times in the thesis. Ch5:123: "These estimates are imprecise and do not establish earnings dominance, a decline in either slope, or a negative book-value association." Ch4 Discussion item states the negative post-BVPS slope "cannot therefore be presented as an established empirical law". |
| M3 | CLOSED (V) | "Key Sensitivity Finding" occurs 0 times. Ch4:443: Holm 0.169, 29.5% margin, neither interaction significant, R5 fails, "sensitivity finding" framing. Same in Ch5:97,102,119,123,132. |
| M4 | CLOSED (V) | N=30 and both carry-forward pairs in Ch4:452 and Ch5:132, with the 0.100 → 0.709 attenuation and the stale-price caveat. Numbers re-verified (§4). |
| M5 | CLOSED (V) | Ch3:82–100 characterises both rows (same failed HBL–NIB merger, 54/47-day delays); Ch4:452 states the attenuation direction and that "their missingness mechanism and its direction cannot be established from these cases". The plan forbade labelling MNAR without author support, so explicit non-determination is the honest closure. |
| M6 | CLOSED (V) | Koenker named in Ch3:360; Ch4 Table 9 has both rows (Koenker LM 14.37 p=0.213 "Not rejected"; Classical LM 28.18 p=0.003 "Rejected"); Ch4:511 and App E:497 state both. The old "Passed" label is gone. Numbers re-verified (§4). |
| M7 | CLOSED (V) | "Mitigated via HC3" occurs 0 times. Ch4 Table 9 note: "HC3 adjusts the covariance estimate but does not remove or neutralize influential observations." |
| M8 | CLOSED (V) | "Residual standard deviation screening" occurs 0 times. Q-Q verdict + Shapiro (M1 p=0.045, M2 p=0.038) in Ch3:362 and Ch4:513. |
| M9 | CLOSED (V) | `data_analysis/analysis/stats/models.py:86` computes Within-R²; test at `tests/test_stats.py:102`. Values re-verified (§4). |
| M10 | CLOSED (V) | Ch3:359 restricts 1.16 to Model 1, lists M2 VIFs 10.33/2.28/15.15/24.13, states dummies excluded; `stats/diagnostics.py:25` `vif_table`; Ch4 Table 9 shows all M2 VIF rows. Q4 (whether slopes-only is the right convention) remains open as an author question, as v1 left it. |
| M11 | CLOSED (V) | Ch4 Table 10 has R², Adj. R², Within-R², df columns; :559 gives F(4,16)=2.23 p=0.112 and the Within-R² interpretation. |
| M12 | CLOSED (V) | Year-FE-only row in Table 10 (EPS 2.185 p=0.098, BVPS 0.555 p=0.420, R² 0.919, adj 0.891, df 20). Numbers re-verified (§4). |
| M13 | CLOSED (V) | Multiplicity stated in Ch4:443,634,641 and Ch5:97,102,119,123,132 (eight joint tests, Holm 0.169). Number re-verified (§4). |
| M14 | **PARTIAL (V)** | The knife-edge is fully disclosed (Ch3:86–88 rule; Ch3:219 and Ch4:452 consequentiality; N=30 sensitivity). **But no substantive rationale for the 5-day length itself exists anywhere in the thesis** — Ch5:132 calls it only "an operational rule". The length (vs 2, 10, or 30 days) remains unjustified. See finding F-M14. |

### 3.2 Minors (m1–m40) — independent subagent verdicts

**33 CLOSED:** m1 (App E:18 reference-category paragraph), m2 (explicit
`Treatment` references, `models.py:23–24`), m3 (`price_rd` in all formulas),
m4 ("Strictly within-year" 0 hits; Ch4:611 corrected), m5 (HC3 overclaim removed,
Ch3:349, Ch1:177), m6 (within-bank independence stated as untested limitation,
Ch3:350), m7 ("Huber-White cluster" 0 hits; Ch3:344 distinguishes), m8 (T4 note
"upper-tail test"; thesis Ch4:278 agrees), m9 (T5 includes R9), m10 (test asserts
R1–R9), m12 (pipeline "~20", Ch4:134; r=0.974656 → VIF 19.98), m13 (threshold
reconciled: screen at 5, "Below/Above screen" in Table 9), m14 (Spearman/Shapiro
in Ch4:138 + Table 4 note pointer; **but see F-T4NOTE for a new punctuation error
in that note**), m15 (DPS–MPS p now 0.679, Ch4:133), m16 (R9/HBL sentence,
Ch4:447), m17 ("bull market" 0 hits; Ch4:512 neutral), m20 (Ch3:351 Goodness of
Fit formulas), m21 (Ch4:559 jump interpreted; arithmetic verified), m22 (Table 6
Adj. R² 0.958), m23 (Table 10 with Within-R² alongside), m24 (Table 8 note fit
statistics, identical to App E; values verified against the pipeline by the
coordinator), m25 (Table 6 note now points CIs to App E, verified at App E:105),
m26 (`_combo` 0 hits; `linear_combination` centralised and tested), m27 (Ch2:401
"seven robustness variants plus two baseline specifications"; "eight plotted"
preserved in App C), m28 (R9 bullet in Ch1:66), m30 (R6 identical-results sentence,
Ch4:442), m31 ("bonus issues" 0 hits; Ch3 restatement sentence sourced only),
m35 ("eliminates look-ahead" 0 hits; Ch1:36 qualified), m36 (Ch5:117 RQ1 correct
direction), m37 (pooled EPS p 0.128 everywhere), m38 (Table 3 note ddof=1 +
%-change formula), m39 (all five SD % changes in Ch4 + Ch5; values depend on
full-precision SDs — verified by numeric recomputation, §4), m40
(`statsmodels==0.14.6` pinned; App D:318 records it).

**5 PARTIALLY CLOSED:**

- **m19 — PARTIAL.** Table 9 "Passed" is gone, the BP note is corrected, M2
  diagnostics are in App E. **But both App E flagged tables are still out of
  descending Cook's-distance order** (`appendix_e.tex:515–524`: 0.5519, 0.4124,
  0.2711, **0.1451, 0.2447**; `:544–554`: 0.4902, 0.3983, **0.1870, 0.2404**,
  0.1513). See finding F-M19.
- **m29 — PARTIAL.** Thesis side is clarified (Ch3:373, Table 8: R3/R4 are
  Model-2 variants). **But the proposal still says** "EPS is replaced with ROA in
  Models 1 and 2" (`src/proposal/sections/07_methodology/07_methodology.tex:190–191`).
  Note: the proposal is read-only by standing rule (no change without the author's
  explicit permission), so the thesis-side clarification is the achievable closure;
  the proposal-vs-code discrepancy stands verbatim in the repo.
- **m32 — PARTIAL.** Formal Ch5 answers are qualified (RQ2 :118; :123–128). **But
  two Implications sentences still state regime change from point estimates
  without qualification** (Ch5:187, :189). See finding F-M32.
- **m33 — PARTIAL.** MDE numbers are reported with caveats (Ch3:365, Ch5:108).
  **But nowhere does the thesis state effective N < 28 or that the MDE/power
  numbers are optimistic upper bounds** ("optimistic" / "upper bound" / "effective
  N" 0 hits in that context). See finding F-M33.
- **m34 — PARTIAL (location).** The fact is now stated in one place — App D:192
  (2 settled of 5 FY 2081/82; 3 pending; 25 unrecorded). It is **not in Chapter 3**,
  where the finding located the gap. Substance (stated once) is satisfied;
  placement is the residual quibble.

**1 NOT CLOSED:**

- **m18 — NOT CLOSED.** No threshold-dependence statement exists anywhere.
  "Influential Observations" is still a bare label for the single 4/N = 0.143
  threshold (Ch4:512; App E:509,538). The review's counts (D > 1 flags 0; 4/(n−K−1)
  flags 3 in M1 / 2 in M2, vs 5 each at 4/n) appear nowhere. See finding F-M18.

**1 NOT APPLICABLE AS STATED:**

- **m11 — N/A.** R4 p = 0.0997 printing as 0.100 is correct rounding to three
  decimals in a table whose p-values are all to three decimals. No change warranted.

### 3.3 Suggestions (s1–s8)

| ID | Verdict | Evidence |
|---|---|---|
| s1 | CLOSED (V) | Wild-cluster bootstrap implemented (`stats/wild_bootstrap.py`), method in Ch3, results in Ch4/Ch5, test pins values. **But the M2 value it reports is wrong — see finding F-S1 (Major).** |
| s2 | CLOSED (V) | `post_slopes()` in `stats/robustness.py`; R5/R6 post slopes in Ch4; all R2–R9 post slopes verified (§4). |
| s3 | CLOSED (V) | Interacted-DPS sentence in Ch4 R4 paragraph (F=2.848, p=0.097). Number verified (§4). |
| s4 | **NOT ADOPTED (V)** | No note anywhere that R² is not comparable across different n ("comparab" 0 relevant hits in Ch4/App E). Not documented as deferred in the log. |
| s5 | CLOSED (V) | Ch3:351 Goodness of Fit explicitly distinguishes Within-R² from one-way within-R² and from demeaning. |
| s6 | **NOT ADOPTED (V)** | The phrase "which the HC3 intervals already reflect" remains verbatim in App E:499 and in the generator prose (`appendix_e_prose.tex:42`). The review's point (HC3 intervals reflect sampling variance under heteroskedasticity, not collinearity as such) was not addressed. Not documented as deferred. |
| s7 | CLOSED (V) | Table 2 note (Ch4:71): "five calendar days", "the first active session on or after the target". "Trading window" 0 hits. |
| s8 | CLOSED (V) | "Halved" 0 hits; DPS post median zero stated (Ch4:80, Ch5:75); Table 10 has no Assessment column. |

## 4. Area 2 — New-content verification (independent recomputation)

Primary method: own numpy QR OLS + own HC3 + own Wald F; statsmodels 0.14.6 only
as cross-check (agreed to ~1e-9 except the item-8 knife-edge). Panel:
`mps_rd_joined_panel.csv` (30 rows); `price_rd` = price where gap ≤ 5 (excluded HBL
FY2077-78 gap 54, NIMB FY2077-78 gap 47); post = FY2079/80 onward; NIB recoded
NIMB in source; references GBIME / FY2076-77. Sample confirmed n=28 (pre 13,
post 15).

| Item | Recomputed (6dp) | Thesis | Verdict |
|---|---|---|---|
| M1 EPS / BVPS | 2.094766 / 0.218807 | 2.095 / 0.219 | MATCH |
| M1 R² / adj / Within | 0.948098 / 0.912415 / 0.151754 | 0.948 / 0.912 / 0.152 | MATCH |
| M2 pre EPS / BVPS | 5.577061 / 0.100346 | 5.577 / 0.100 | MATCH |
| M2 δ_E / δ_B | −3.123687 / −1.757967 | −3.124 / −1.758 | MATCH |
| M2 post EPS / BVPS (p) | 2.453374 (0.297787) / −1.657622 (0.160946) | 2.453 (0.298) / −1.658 (0.161) | MATCH |
| M2 R² / adj / Within | 0.978078 / 0.957721 / 0.641723 | 0.978 / 0.958 / 0.642 | MATCH |
| M2 Wald F(2,14), p | 2.954481, 0.085027 | 2.954, 0.085 | MATCH |
| R6 Wald F(2,10), p | 5.817708, 0.021095 | 5.818, 0.021 | MATCH |
| R5 Wald F(2,10), p | 2.414358, 0.139470 | 2.41, 0.139 | MATCH |
| Holm-adjusted R6 p | 0.168758 | 0.169 | MATCH |
| 29.5% margin | 29.477% (F-crit 4.102821) | 29.5% | MATCH |
| N=30 Wald F(2,16), p; pre-BVPS | 4.761626, 0.023849; 0.708829 | 4.762, 0.024; 0.709 | MATCH |
| Carry-forward pair 1 F, p | 3.870470, 0.042558 | 3.870, 0.043 | MATCH |
| Carry-forward pair 2 F, p | 3.821406, 0.043991 | 3.821, 0.044 | MATCH |
| s2 R5 post EPS / BVPS (p) | 3.414863 (0.400755) / −2.080621 (0.315401) | 3.415 (0.401) / −2.081 (0.315) | MATCH |
| s2 R6 post EPS / BVPS (p) | 1.899717 (0.489736) / −1.809099 (0.212152) | 1.900 (0.490) / −1.809 (0.212) | MATCH |
| s2 other post slopes | All EPS-positive, BVPS-negative, all p>0.05 (R2–R9) | as claimed | MATCH |
| s1 R6 bootstrap p | 2/32 = 0.062500 | 0.062 (2/32) | MATCH |
| **s1 M2 bootstrap p** | **2/32 = 0.062500** | **0.031 (1/32)** | **MISMATCH — see F-S1** |
| Descriptives (all five vars) | Means/SDs/% changes/CVs as in §4.1 below | corrected values | MATCH |
| MDE β_E / δ_E / δ_B | 10.726495 / 12.060838 / 3.707868 | 10.73 / 12.06 / 3.71 | MATCH |
| BP Koenker M1 / classical M1 / Koenker M2 | 14.369458 (0.213220) / 28.183015 (0.003035) / 14.543038 (0.336741) | 14.37 (0.213) / 28.18 (0.003) / 14.54 (0.337) | MATCH |
| Shapiro M1 / M2 | W 0.924622 (0.045185) / 0.921554 (0.037899) | 0.9246 (0.045) / 0.9216 (0.038) | MATCH |
| Year-FE-only R² / adj; EPS / BVPS | 0.919171 / 0.890881; 2.185412 (0.098301) / 0.555336 (0.419720) | 0.919 / 0.891; 2.185 (0.098) / 0.555 (0.420) | MATCH |
| Bank-FE-given-year-FE F(4,16), p | 2.229284, 0.111660 | 2.23, 0.112 | MATCH |
| s3 interacted DPS F, p; DPS×Post | 2.847907, 0.097244; −3.651323 (0.734917) | 2.848, 0.097; −3.651 (0.735) | MATCH |
| Within-R² formula M1 / M2 | 0.151754 / 0.641723 | 0.152 / 0.642 | MATCH |
| Naive-demeaning R² M1 / M2 | 0.154331 / 0.503971 (differs) | n/a (formula matters) | CONFIRMED |

### 4.1 Descriptives detail (full precision, ddof=1)

| Var | Pre mean / SD | Post mean / SD | Mean % | SD % | CV pre→post |
|---|---|---|---|---|---|
| MPS | 310.592308 / 119.459731 | 205.595333 / 33.451535 | −33.805% | −71.998% | 38.46→16.27 |
| EPS | 17.902308 / 3.985647 | 10.717333 / 6.534468 | −40.134% | +63.950% | 22.26→60.97 |
| BVPS | 158.108582 / 19.099117 | 161.974748 / 16.177338 | +2.445% | −15.298% | 12.08→9.99 |
| DPS | 6.060000 / 3.563463 | 1.400000 / 2.971291 | −76.898% | −16.618% | 58.80→212.24 |
| ROA | 1.313241 / 0.221822 | 0.704191 / 0.438082 | −46.378% | +97.492% | 16.89→62.21 |

All match the corrected thesis values. The old printed values were confirmed to
come from 2dp-rounded summary statistics (recomputing % changes from the rounded
means/SDs reproduces every old value, including ROA SD 0.22→0.44 = +100.00%,
the old "SD doubled").

### 4.2 Carry-forward provenance

Pair 1 (HBL 487 / NIMB 453, 12 May 2021): source rows found in
`mps_candidate_price_table.csv`. Pair 2 (HBL 484 / NIB 460, 13 May 2021): **not in
any CSV**; documented in `appendix_d.tex:188` and
`mps_candidate_price_table_README.md:158` as news/Merolagani-reported last prices.
Inputs were taken verbatim from that documentation; nothing invented. The
one-day/source discrepancy is honestly stated in the thesis.

### 4.3 The s1 M2 bootstrap mismatch (finding F-S1)

Independent numpy enumeration of all 32 Rademacher patterns gives **M2: 2/32 =
0.0625** (thesis: 1/32 = 0.03125). A 9,999-draw random Rademacher check gives
612/9999 = 0.0612 for **both** M2 and R6 — consistent with 2/32 within Monte Carlo
error (SE 0.0024) and ~12 SE from 1/32. The all-+1 pattern reproduces each observed
Wald exactly (diff 0.0) in both implementations.

**Root cause (verified):** in exact arithmetic the all−1 pattern *must* reproduce
F_obs exactly (y\* = 2·fitted_R − y ⇒ deltas negate, residuals negate, HC3
covariance identical, Wald identical), so the count is mathematically ≥ 2. The
thesis's 1/32 is a last-ulp floating-point artifact of the statsmodels path: M2
all−1 F\* = 2.9544812171019093 vs observed 2.9544812171020980 (diff −1.887e-13,
just below, not counted); R6 all−1 diff is +1.756e-12 (just above, counted).
(The earlier 9,999-draw check quoted in the implementation log, p = 0.029 for M2,
suffers the same artifact, because it used the same statsmodels comparison with
no tolerance.)

**Consequence:** in exact arithmetic **neither** bootstrap p is below 0.05 (both
0.0625). The thesis's Ch4 sentence "Each decision therefore flips under the
bootstrap, and each flip hangs on a single pattern out of 32" is wrong for M2 —
the M2 decision does **not** flip (HC3 0.085 and bootstrap 0.0625 both fail to
reject at 5%). The Ch5 sentence ("flipping each HC3 decision on a single
pattern") is likewise wrong for M2. The qualitative conclusion (inconclusive;
does not overturn HC3; decisions fragile) is unaffected and in fact reinforced.

## 5. Area 3 — Fresh-error scan (diff 0619d4a..b4339bb)

Every changed line in the three commits was read. Verified clean: R5/R6
post-slope arithmetic (5.993−2.578=3.415; −0.201−1.880=−2.081; 4.336−2.436=1.900;
0.802−2.611=−1.809); m21 arithmetic (dummies-only R² 0.9387 → 93.9%; M1 adds
0.93pp, M2 adds 3.9pp); Table 8 note fit statistics match the pipeline exactly
(all nine R²/adj/Within values, §3.2); Ch4/Ch5 descriptives agree; no old values
remain anywhere in `src/thesis/`; Ch3 formulas match the code; the wild-bootstrap
code is correct on read (null-imposed restricted fit, per-bank Rademacher weights,
HC3 Wald on each refit); `$\times$` in the R4 sentence is a correct single
backslash (0 double-backslash occurrences); the `_fit` Within-R² guard change
(`"C(bank"` / `"C(fy"`) preserves the intended behaviour for pooled/bank-only/
year-only fits (Within-R² stays None there); `dataset.py` computes `price_rd` on
the bonus-adjusted frame by the same short-window rule.

**New errors found in the diff: one** (F-T4NOTE). The m19 ordering defect predates
the three diffs but is still live (F-M19).

## 6. Area 4 — Build + tests

- **Tests:** 30/30 pass (22.45s) under the pinned venv; statsmodels confirmed
  0.14.6. 0 failed, 0 skipped, 0 errors. Run twice.
- **Fresh build** (`work_v35_final_check/`, output
  `thesis-full-ch1-5-v35-final-check.pdf`, 766,016 bytes; v35 PDF untouched):
  **164 pages, 0 TeX errors, 0 undefined references, 0 LaTeX warnings, 0 bibtex
  warnings.** Exactly **1 overfull**: `0.27353pt` in Chapter III (standing).
  The Table 10 overfull (2.68pt) is **gone**; no new overfull appeared.
  (38 underfull warnings in build4.log — cosmetic, not reported as findings.)
- **PDF content:** all new values present (33.81% ×2, 40.13% ×3, 63.95% ×2,
  97.49% ×1, 15.30% ×2, 16.62% ×2, 46.38% ×1, 3.415 ×1, 1.900 ×2, "wild-cluster
  bootstrap" ×3, 0.031 ×5, 0.062 ×2, "Goodness of Fit" ×2); all old wrong values
  absent (33.80%, 40.11%, 63.66%, 46.56%, "SD doubled" — 0 each).
- **Environment caveat (not a thesis defect):** the first build attempt failed
  (48 pages, 1,128 errors) because the VM's TeX/font state had degraded
  (`xelatex` transiently unfindable; `fonts-texgyre` missing). A system
  package-restore reinstalled the fonts and the clean rebuild succeeded. The
  thesis builds fine, but the VM's TeX environment is fragile — a future build
  should re-verify fonts first (`fc-list | grep -i termes`, `kpsewhich`).

## 7. Findings register

### Major (1)

**F-S1 — M2 wild-bootstrap p-value is wrong (0.031 vs 0.062); the "each decision
flips" claim is wrong for M2.** [Area 2, §4.3; also s1 closure, §3.3]
*Severity: Major. Status: VERIFIED (independent numpy enumeration + 9,999-draw
check + exact-arithmetic proof of the all−1 identity + statsmodels replication
of the artifact).*
Thesis Ch4 reports "For Model 2 the bootstrap p-value is 0.031 (1 of 32
patterns), below the HC3 p = 0.085" and "Each decision therefore flips under the
bootstrap, and each flip hangs on a single pattern out of 32"; Ch5 repeats
"flipping each HC3 decision on a single pattern". Correct value is 0.062 (2 of
32). In exact arithmetic neither bootstrap p is below 0.05, so the M2 decision
does not flip at all; only R6 flips. The test at
`tests/test_stats.py` pins the wrong value (`bootstrap_p == pytest.approx(1/32)`,
`n_exceed == 1`). The qualitative conclusion (inconclusive, does not overturn
HC3) is unaffected and reinforced — but the reported statistic and the derived
claim must be corrected before the thesis is final.

### Minor (8)

**F-T4NOTE — Missing period in the Chapter 4 Table 4 note (new error from the
m14 edit).** [Area 3]
*Severity: Minor. Status: VERIFIED (read at Ch4:127).*
The note now reads "…Market Price per Share at Reporting Deadline
($\mathit{MPS}^{RD}$) Pearson $p$-values assume normality; the Shapiro-Wilk and
Spearman checks are reported in the text." — the full stop after
"($\mathit{MPS}^{RD}$)" was dropped when the sentence was appended. Fix: insert
". " after ")": "…($\mathit{MPS}^{RD}$). Pearson $p$-values assume normality; …".

**F-M19 — App E flagged-observation tables still out of descending Cook's-distance
order.** [Area 1, m19]
*Severity: Minor. Status: VERIFIED (read at `appendix_e.tex:515–524` and
`:544–554`).*
M1 table: 0.5519, 0.4124, 0.2711, **0.1451, 0.2447** (last two swapped; correct
order ends 0.2447, 0.1451). M2 table: 0.4902, 0.3983, **0.1870, 0.2404**, 0.1513
(middle two swapped; correct order 0.4902, 0.3983, 0.2404, 0.1870, 0.1513).
Pre-existing defect, not introduced by the three diffs, but never fixed. Fix in
the generator (not by hand-editing the generated table) and regenerate to confirm.

**F-M18 — "Influential" is still threshold-dependent with no statement to that
effect.** [Area 1, m18]
*Severity: Minor. Status: VERIFIED (grep: no threshold-dependence statement
anywhere).*
One sentence would close it, e.g. in Ch4 or Ch3: D > 1 flags 0 observations in
both models; 4/(n−K−1) flags 3 (M1) / 2 (M2), vs 5 each at 4/n = 0.143.

**F-M32 — Two Chapter 5 Implications sentences still state regime change from
point estimates without qualification.** [Area 1, m32]
*Severity: Minor. Status: VERIFIED (read at Ch5:187, :189).*
:187 "The observed downward compression in earnings multiples and the lack of a
positive book value pricing anchor post-consolidation coincide with market
caution…"; :189 "the empirical evidence indicates that horizontal amalgamations
were accompanied by substantial earnings transitoriness and valuation
compression." The formal RQ answers are qualified; these two sentences are not.

**F-M33 — Effective N < 28 / MDE optimism never stated.** [Area 1, m33]
*Severity: Minor. Status: VERIFIED (grep: "optimistic" / "upper bound" /
"effective N" 0 hits in that context).*
One sentence in Ch3 or Ch5: with G = 5 banks the effective N is below 28, so the
reported MDEs are optimistic upper bounds.

**F-M14 — No substantive rationale for the 5-day freshness length.** [Area 1, M14]
*Severity: Minor. Status: VERIFIED (no rationale found in Ch3 or App D).*
The rule is stated, disclosed as operational, and its consequence is shown
(N=30 flips the decision). What is missing is any reason for 5 days rather than
any other window. Either record the author's rationale or state explicitly that
the length is an un-derived operational choice.

**F-M34 — Publication-date coverage stated in App D, not Chapter 3.**
*Severity: Minor. Status: VERIFIED (App D:192 states it; Ch3 has no "2 of 30"
statement).*
Substance (stated in one place) is satisfied; placement is the residual quibble.

**F-M29 — Proposal still says ROA/DPS are in "Models 1 and 2".**
*Severity: Minor. Status: VERIFIED (`src/proposal/.../07_methodology.tex:190–191`).*
Thesis side is clarified; the proposal is read-only by standing rule, so this
can only be closed by the author (either a proposal correction with his explicit
permission, or a thesis footnote noting the deviation — none exists now).

### Suggestion (2)

**F-S4 — R² comparability across different n not noted.** [Area 1, s4]
*Severity: Suggestion. Status: VERIFIED (no such note anywhere).*
One sentence where R5/R6 (n=23) are compared with the n=28 specs: R² is not
comparable across different n. Not adopted, not documented as deferred.

**F-S6 — App E "HC3 intervals already reflect [collinearity]" wording unchanged.**
[Area 1, s6]
*Severity: Suggestion. Status: VERIFIED (App E:499; generator prose:42).*
Per v1 §4(d): HC3 intervals reflect sampling variance under heteroskedasticity,
not collinearity as such. Reword or document why the current wording stands. Not
adopted, not documented as deferred.

## 8. Open questions (carried forward)

- **Q1 (5-day window):** partially open — see F-M14. The design choice stands;
  only the rationale for the length is missing.
- **Q4 (VIF convention):** open as v1 left it — the thesis discloses the
  slopes-only convention (dummies excluded) but cites no authority; the review
  does not verdict it either way.
- **Q2/Q3/Q5/Q6/Q7/Q8/Q9/Q10/Q11:** closed by the implemented text, except Q9's
  residue: an internal generator note (`generators/appendix_d/table_map_frozen.md:79`)
  still says "statsmodels >= 0.14" (not thesis-facing; fix opportunistically).
- **Carry-forward pair 2 provenance:** documented in App D and the candidate-table
  README as news/Merolagani-reported prices; not present in any CSV, so it is not
  independently verifiable from data files. Accepted as documented, with the
  discrepancy honestly stated.
- **Figure pixels:** still unverified (v1 limit, unchanged).

## 9. Recommended actions (prioritised)

**P0 — before the thesis is final:**
1. **Correct the M2 bootstrap (F-S1).** In Ch4 and Ch5 change the M2 bootstrap
   p-value 0.031 (1/32) → 0.062 (2/32); correct "each decision flips" (only R6
   flips; in exact arithmetic neither bootstrap p is below 0.05); fix the test
   pin (`tests/test_stats.py`: 1/32 → 2/32, `n_exceed == 1` → `== 2`); make the
   bootstrap comparison tolerance-robust (e.g. count `F* >= F_obs - 1e-9`) so the
   all−1 pattern counts as the mathematics requires; re-run the test suite;
   rebuild (v36) and verify the corrected sentences in the PDF.
2. **Insert the missing period in the Ch4 Table 4 note (F-T4NOTE).**

**P1 — should be fixed in the same pass:**
3. Reorder the two App E flagged tables into descending Cook's D (F-M19) via the
   generator; regenerate and confirm the tracked `appendix_e.tex` changes only
   in those two rows.
4. Add the m18 threshold-dependence sentence (D > 1: 0; 4/(n−K−1): 3/2).
5. Qualify the two Ch5 Implications sentences (F-M32).
6. State effective N < 28 / MDE optimism (F-M33).
7. Record or explicitly disclaim a rationale for the 5-day length (F-M14).

**P2 — small, do with the above:**
8. Add the s4 R²-comparability note; reword or explicitly retain the s6 App E
   sentence; note the m34 placement and m29 proposal-deviation decisions in the
   log (adopted/deferred, with rationale). Fix the stale "statsmodels >= 0.14"
   generator note.

## 10. Verification log

- **Coordinator:** read v1 §§4, 7, 8, 10 and the implementation log/plan in full;
  read `git diff 0619d4a..b4339bb` line by line (thesis + code + tests); verified
  M1–M14 and s1–s8 closure by grep + reading; verified Table 8 note fit
  statistics against the pipeline (`build_runs`, all nine R²/adj/Within match);
  verified Ch4/Ch5 number agreement and absence of old values in `src/thesis/`;
  verified the Ch3 Within-R² formulas against `models.py:86`.
- **Numeric subagent:** independent numpy QR OLS + own HC3 + own Wald F, pinned
  venv (numpy 2.5.4, statsmodels 0.14.6, scipy 1.18.1); scratch
  `~/workspace/final-review-scratch/numeric/` (`verify.py`,
  `verify_results.json`, `crosscheck.py`, `crosscheck_statsmodels.json`,
  `wild_diag.py`). 10 of 11 items MATCH at printed precision; item 8 (M2
  bootstrap) MISMATCH with root cause identified and replicated.
- **Build/test subagent:** pytest 30/30 (twice), statsmodels 0.14.6 confirmed;
  fresh build in `~/workspace/frontmatter_build/work_v35_final_check/` →
  `thesis-full-ch1-5-v35-final-check.pdf` (164 pp, 0 errors, 0 undefined,
  0 bibtex warnings, 1 standing overfull); PDF string counts for new/old values.
- **Minors subagent:** all 40 minors checked against the tree with file+line
  evidence; 33 closed, 5 partial, 1 not closed, 1 not applicable as stated.
- **Final `git status` check (run after writing this file):** HEAD `b4339bb`;
  working tree clean except the pre-existing untracked
  `docs/thesis_supervisor/ohlson-value-relevance-pivot-2026-10-27.md` and the new
  untracked `docs/thesis_review/v2/` (this file only). Nothing else was changed.

---

*End of final review. Verdict summary: the implementation closed 13/14 Majors,
33/40 minors, and 6/8 suggestions, and every headline number re-checked
reproduces exactly — but the claim that "no review item remains open" is not
sustained, and the thesis is not final as written: the M2 wild-bootstrap p-value
is wrong (0.031 vs 0.062) with a wrong derived claim in Chapters 4 and 5, plus
eight Minor and two Suggestion items. Fix P0 first; the rest is a single
short pass.*
