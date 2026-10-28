# Chapter 3 review — Research Methodology

**Chapter reviewed:** `docs/draft/thesis/chapter_03_research_methodology.md` (291 lines, read in full, word by word).
**Repo state:** `~/workspace/verbose-chainsaw`, HEAD `9a46350`.
**Reviewer rule for this file:** no thesis file, table, figure, or data file was edited, moved, or deleted to write this review. This file is the only output.
**LaTeX counterpart:** `src/thesis/chapters/chapter_03_research_methodology.tex` was used for sync-spotting only (Pass 6). No full LaTeX diff was done.

## Passes actually run (loop)

- **Pass 1 — Code-vs-text:** formulas, fixed effects, HC3, Wald, sample, window, Post definition, and R1–R8 compared against `data_analysis/analysis/stats/models.py`, `stats/robustness.py`, `stats/wald.py`, `dataset.py`, and `configs/base.yaml`.
- **Pass 2 — Proofread:** the whole chapter read line by line for grammar, duplicates, and symbol/term consistency.
- **Pass 3 — Numbers:** every Table 3.1 price, gap, date, EPS, BVPS, DPS, restatement amount, and df recomputed or compared against `data_analysis/data_extract/output/tidy/accounting_panel.csv`, `data_analysis/data_extract/output/manual_review/mps_rd_joined_panel.csv`, `config/dps.json`, and tables T1–T6 and A4–A6 (`.md` versions).
- **Pass 4 — Overstatement:** every verification, independence, official-source, causality, and completeness claim checked against what the cited evidence actually supports.
- **Pass 5 — Slop hunt:** every sentence asked whether it carries thesis-specific meaning or is deletable filler, repetition, or meta-comment.
- **Pass 6 — LaTeX sync:** passages flagged in the Markdown version spot-checked in the `.tex` version only.

## Classification

- **MUST-FIX:** wrong number, code-vs-text mismatch, overstatement presented as fact, or wrong df.
- **MINOR:** wording, grammar, repetition, or slop. No number changes.

## Correct passages (checked, briefly — no issue invented)

- **Table 3.1, all 28 realised prices:** compared cell by cell to `mps_rd_joined_panel.csv` — zero mismatches. Gaps HBL FY2077/78 = 54 days (price date 2022-06-06) and NIMB FY2077/78 = 47 days (2022-05-30) match the joined panel. Clean sample n = 28, 13 pre, 15 post, recomputed from the joined panel. Entity-mismatch rows are exactly the four FY2078/79 rows (GBIME, HBL, KBL, NIMB); NMB is correctly not flagged.
- **Model 1 and Model 2 formulas and df:** Model 1 `price ~ eps + bvps + C(bank) + C(fy)` (models.py line 21), Model 2 adds `eps:post + bvps:post` (line 22); K = 12, df = 16 and K = 14, df = 14 as written; R4 K = 15, df = 13 as written. Wald is `f_test` on the two interaction terms (wald.py line 38), 2 numerator df, as written. Reference categories GBIME and FY2076/77 match the first sorted levels of the code's categorical terms.
- **HC3 with t (code side):** `_fit` uses `fit(cov_type="HC3", use_t=True)` (models.py line 60). The code is correct; the gap is in what Chapter 3 says about it — see MUST-FIX 2 below.
- **R1–R8 definitions:** R1/R2 baselines, R3 ROA-for-EPS, R4 Model 2 + DPS, R5 excluding FY2079/80 (n = 23), R6 excluding FY2078/79 (n = 23), R7 bonus formula, and R8 restated-EPS set all match `robustness.py` and `configs/base.yaml` (restated: GBIME FY2076-77 15.33, NMB FY2077-78 14.76, HBL FY2077-78 27.60, the last out of sample).
- **EPS restatements in §3.6.5:** own-current vs next-year previous-column comparison over all 25 transitions finds exactly three restatements — GBIME 17.99 → 15.33, HBL 28.07 → 27.60, NMB 16.66 → 14.76 — exactly as written. No other restatement is hidden.
- **Balance-sheet restatement amounts in §3.4.3 item 5:** recomputed from raw previous columns vs panel own-current values — 718,438,769; 1,877,083,471; 1,047,386,219; −7,369,687,548; 9,587,393 — matching the chapter's rounded millions (718.44; 1,877.08; 1,047.39; −7,369.69; 9.59).
- **EPS denominator examples (§3.5.2):** PAT divided by year-end shares from the panel gives GBIME 18.71, NIMB 10.90, HBL 7.22 against reported 22.06, 13.92, 9.18 — exactly as written.
- **NIMB NAV pairs (§3.5.2):** recomputed BVPS vs printed NAV — 190.70 vs 191.00, 198.28 vs 198.00, 185.67 vs 186.00, 176.31 vs 176.00, 190.40 vs 190.00 — exactly as written; NMB FY2081/82 175.18 vs 174.49, gap 0.69, stays flagged as written. (NIMB FY2079/80, gap 0.08, is correctly not in the 0.28–0.40 list.)
- **Panel identities (§3.4.1):** maximum absolute Bank identity difference in the panel is 1.0 NPR — the "within a ≤ 1 NPR rounding tolerance" claim for Bank identities holds.
- **DPS eligibility (§3.5.2):** all 28 clean-sample rows have a DPS value, and the announcement-date file shows every announcement date on or before its price date. The 18 proposed / 12 documented-nil split in `config/dps.json` matches the chapter's framing. NMB FY2076/77 price reconciliation (dataset 437.00, Merolagani LTP 436.00, ShareSansar OHLC 432/439/428/437.00) matches Table A4.
- **Price-source honesty in Table 3.1 and §3.4.3 item 3:** the chapter explicitly states NEPSE official closes were not independently verified and that ShareSansar agreement "does not represent independent verification". That framing is correct and must be kept. No price in this chapter is presented as a verified NEPSE official close, and no Ashadh-end, year-end, or reporting-deadline price is labelled MPS_post.
- **Dates:** 12 April 2024 was a Friday and 14 April 2024 a Sunday, so the §3.3.4 note that Sunday 14 April 2024 was the first subsequent trading session (gap 2) is correct. NMB share-capital growth FY2076/77 → FY2077/78 is 17.02% against a 13% bonus, leaving 561,345,015 — consistent with the chapter's "approximately NPR 0.57 billion".
- **Diagnostics in §3.6.4:** VIF on substantive regressors only, Breusch-Pagan via `het_breuschpagan`, Cook's distance with the 4/n threshold (`cooks_threshold` returns 4.0/n; 4/28 ≈ 0.143), and Q-Q data all exist in `stats/diagnostics.py` and are used by the T6/diagnostics assets. The diagnostic list is not invented.

## MUST-FIX issues

### MUST-FIX 1 — Group-equity sentence is false as a general statement (line 110)

Chapter text, verbatim (line 110):

> "Group-level schedules in raw extractions reflect equity attributable to equity holders and exclude non-controlling interest (e.g., NPR 211.28 million in Global IME Bank FY 2076/77); consequently, Group-level figures are never utilized in panel regressions."

Check actually done: in `data_analysis/data_extract/output/raw/*.json`, GBIME Group total equity equals attributable equity in all six years (so the GBIME example is true: FY2076/77 gap 211,277,477). But for HBL Group FY2079/80, FY2080/81, FY2081/82 and NMB Group FY2077/78–FY2081/82, Group total equity differs from attributable equity by a positive non-controlling interest (for example NMB FY2078/79: 538,470,376). In those rows the raw Group total does include NCI. The sentence as written states the GBIME pattern as if it held for Group schedules generally. It does not.

Fix: scope the sentence to GBIME, for example: "In the GBIME raw extractions, Group total equity equals equity attributable to equity holders and excludes non-controlling interest (NPR 211.28 million in FY 2076/77)." The consequential claim — Group figures are never used in the regressions, and all accounting variables are Bank-level — is correct and should stay.

### MUST-FIX 2 — §3.6.3 never states the reference distribution: t, not normal (lines 253–267)

Chapter text, verbatim (line 266, the HC3 paragraph):

> "To ensure conservative, reliable inference, standard errors, $t$-statistics, and confidence intervals are computed using MacKinnon-White (1985) HC3 heteroskedasticity-robust standard errors"

The section reports df (14, and 13 for R4) but never says the t-statistics and confidence intervals are referred to Student's t on residual df. The code does this (`use_t=True`, models.py line 60), and Tables T3/T4 are t-based, but a reader of Chapter 3 alone cannot tell whether the intervals use 1.96 or t(14)/t(16). This chapter previously carried exactly that normal-approximation error; leaving the distribution unnamed leaves the same ambiguity open.

Fix: add one sentence in §3.6.3, for example: "All t-statistics, p-values, and confidence intervals use Student's t on residual degrees of freedom (t(14) for Model 2, t(16) for Model 1), not the normal approximation."

### MUST-FIX 3 — `linearmodels` is claimed but never used (line 291)

Chapter text, verbatim (line 291):

> "Econometric modeling, robust HC3 covariance estimation, diagnostic testing, and visualization are executed using Python (`statsmodels`, `linearmodels`, `seaborn`, `matplotlib`)."

Check actually done: a search of `data_analysis/analysis/` Python files for `linearmodels` returns zero matches. Estimation is `statsmodels` formula OLS (`smf.ols`, models.py). A claimed tool with no code behind it is a code-vs-text mismatch, and an examiner who greps the repo will find it.

Fix: delete `linearmodels` from line 291.

### MUST-FIX 4 — §3.3.4 presents end-of-Chaitra as the statutory deadline; §3.5.2 correctly calls it an operationalization (lines 76 and 173)

Chapter text, verbatim (line 76, the freshness rule):

> "*If a security was suspended from trading or recorded zero valid transactions within a five-day calendar window following the statutory reporting deadline (end of Chaitra / mid-April), the observation is coded as missing and excluded from the regression sample.*"

Chapter text, verbatim (line 173, the MPS_RD operational measurement):

> "*Operational Measurement:* Operationalized at the end of Chaitra (mid-April) of the subsequent fiscal year."

The chapter's own §3.5.2 wording is the honest one: end-of-Chaitra is the study's operationalization of the nine-month audited-publication duty in BAFIA Section 59(2) as described in §3.5.2 (line 172). Line 76, by contrast, writes the deadline as if the statute itself set end-of-Chaitra. The task instruction for this review was to check the chapter's statement of the two duties against what it claims and not to import outside law; on the chapter's own terms, lines 76 and 173 contradict each other in attribution. I did not verify the statute text independently in this task (see NOT checked).

Fix: change line 76 to match line 173, for example: "within a five-day calendar window following the study's operationalized reporting deadline (end of Chaitra / mid-April)". Do not change the dates, the window, or the sample — only the attribution.

### MUST-FIX 5 — "official secondary capital market trading archives" contradicts the chapter's own price-source disclosure (line 110)

Chapter text, verbatim (line 110, opening sentence of §3.4.1):

> "This dissertation relies exclusively on quantitative secondary data extracted from audited financial disclosures and official secondary capital market trading archives."

The chapter itself, in the Table 3.1 note (line 98) and §3.4.3 item 3 (line 132), says prices were retrieved from aggregators (ShareSansar and Merolagani; FinancialNotices for FY2081/82) and that "official NEPSE floor trading archives were not independently verified, and NEPSE official closes remain unverified". Calling the price source "official … archives" in §3.4.1 invites the opposite reading. This is a wording-only fix; no price value changes.

Fix: replace "official secondary capital market trading archives" with "capital market data aggregators" in line 110.

### MUST-FIX 6 — HC3 description reverses the leverage adjustment (line 267)

Chapter text, verbatim (line 267):

> "where $h_{ii} = x_i (X'X)^{-1} x_i'$ represents the leverage of observation $i$. HC3 heavily discounts high-leverage observations, providing reliable finite-sample inference in small panel samples."

The HC3 formula printed immediately above this sentence divides each squared residual by $(1 - h_{ii})^2$. High leverage therefore inflates the adjusted residual and makes inference more conservative; it does not discount high-leverage observations. The formula is correct; the verb describing it is backwards.

Fix: replace "heavily discounts high-leverage observations" with "inflates the residuals of high-leverage observations, making inference more conservative". The code and the estimates are unaffected.

## MINOR issues

### MINOR 1 — Diagram symbol typo: `l_t` for λ (line 162)

Chapter text, verbatim (line 162, conceptual-framework diagram):

> "|  - Fiscal-Year Fixed Effects (l_t) |"

Everywhere else the chapter uses $\lambda_t$ (for example line 166: "fiscal-year fixed effects ($\lambda_t$)"). The diagram uses a lowercase letter L. Fix to $\lambda_t$.

### MINOR 2 — Post-absorption equation mixes coefficients with dummies (lines 238–240)

Chapter text, verbatim (lines 238–240):

> "Because Model 2 includes a full set of fiscal-year fixed effects ($\lambda_t$), the standalone consolidation indicator ($\mathit{Post}_t$) is a deterministic linear combination of the post-consolidation year dummy indicators:"
> "$$\mathit{Post}_t = \lambda_{2079/80} + \lambda_{2080/81} + \lambda_{2081/82}$$"

$\lambda$ denotes the fixed-effect coefficients in this chapter's own notation, not the dummy indicators. The substantive point is correct — a standalone Post term is collinear with the year dummies and is correctly omitted from the code formula — but the equation as written equates an indicator with a sum of coefficients. Fix: write the right-hand side as the sum of the three post-year dummy indicators (for example $D_{2079/80} + D_{2080/81} + D_{2081/82}$), or state the absorption in words without the equation.

### MINOR 3 — "mathematically … appropriate" for purposive sampling (line 33)

Chapter text, verbatim (line 33):

> "Purposive sampling is mathematically and conceptually appropriate because the core research objective focuses specifically on evaluating accounting value relevance across the prominent commercial banking consolidations that reshaped the financial sector in early 2023, while requiring longitudinal data continuity across both pre- and post-merger regimes."

Purposive (judgmental) sampling is a judgment choice, not a mathematically derived one. The justification that follows (focus on the 2023 consolidations, continuity across regimes) is a conceptual justification. Fix: delete "mathematically and", leaving "conceptually appropriate".

### MINOR 4 — Uncited "standard Nepalese banking valuation convention" (line 110)

Chapter text, verbatim (line 110, same sentence as MUST-FIX 1/5):

> "adhering to standard Nepalese banking valuation convention where non-banking subsidiaries are segregated from the licensed commercial bank's capital adequacy and regulatory return metrics."

No source is cited in the chapter for this convention. The Bank-level choice itself is consistently applied and correctly disclosed; only the claim that it is "standard convention" is unsupported in the text. Fix: either cite the convention or soften to "the study adopts a standalone Bank-level basis".

### MINOR 5 — VIF "≈ 30" for EPS–ROA is not the bivariate figure (line on ROA, §3.5.2)

Chapter text, verbatim (§3.5.2, ROA treatment):

> "Because EPS and ROA correlate at $r = 0.975$ (variance inflation factor $\approx 30$), they are never co-included in the same regression to prevent severe multicollinearity."

Check actually done: from r = 0.975 alone, 1/(1 − r²) = 20.25, not ≈ 30. A multivariate VIF with the fixed effects and other regressors can be higher, and Tables T2/T5 also use "~30"/"~ 30" language, but Chapter 3 names no specification that yields ≈ 30. The substantive decision — never co-include EPS and ROA — is correct and is followed in the code (R3 substitutes, never adds). Fix: either name the specification that gives ≈ 30 or write "variance inflation factor ≈ 20 from the bivariate correlation alone, higher once fixed effects are included". I am not asserting a different exact VIF, because I did not estimate that multivariate specification in this task.

### MINOR 6 — Microsoft Excel claimed with no artefact in the repo (line 291)

Chapter text, verbatim (line 291):

> "Data extraction, audit reconciliation, and panel assembly are executed in Python (`pandas`, `numpy`) and Microsoft Excel."

Check actually done: a search of the extraction and analysis Python scripts for Excel artefacts (`openpyxl`, `xlsx`) returns nothing, and no Excel workbook is listed among the evidence files for this task. Manual Excel work outside the repo may exist — I did not prove it does not — so this is flagged as unverified, not as false. Fix: either name the workbook/file that Excel produced or delete "and Microsoft Excel".

### MINOR 7 — VIF screening rule states a threshold but no action (§3.6.4 item 1)

Chapter text, verbatim (§3.6.4 item 1):

> "Variance Inflation Factors (VIF) and tolerance statistics ($1/\text{VIF}$) computed on substantive regressors. Regressors exhibiting $\text{VIF} > 5$ or tolerance $< 0.20$ are screened for collinearity."

The code computes VIF and tolerance (`vif_table`, diagnostics.py lines 25–46) but implements no threshold action, and Table T6 reports VIF 1.16 for both regressors, far below the threshold, so the rule is never triggered in this study. "Screened" here means, in practice, reported and inspected. Fix: add "and reported; no regressor in this study exceeds the threshold" or delete the threshold sentence. No estimate changes.

## Slop hunt (Pass 5) — quoted, deletable or filler

These are MINOR. None changes a number.

1. Generic opening, no thesis-specific content (lines 5–6):

> "Scientific research in empirical finance and financial accounting is distinguished by the formalization, transparency, and reproducibility of its methodological design. The research methodology establishes the systematic protocol through which research questions are investigated, theoretical constructs are operationalized into observable metrics, empirical data are collected and audited, and statistical models are specified and estimated."

Deletable or reducible to one sentence; everything after it in the chapter says the same thing concretely.

2. Roadmap that restates the section headings (lines 8–12):

> "Structured in strict compliance with the *Master's Degree Dissertation Guidelines (2019)* of the Faculty of Management, Tribhuvan University (pp. 13–14), this chapter is organized into five interrelated sections:"
> "* **Section 3.2: Research Design** outlines the epistemological and econometric architecture of the study, specifying its quantitative, correlational, comparative, and longitudinal panel dimensions."
> "* **Section 3.3: Population, Sample, and Sampling Procedure** defines the commercial banking population, justifies the purposive sampling design, presents the institutional profiles of the five selected bank series, discloses the 5-day freshness rule for trading records, and presents the realized price observation matrix."
> "* **Section 3.4: Nature and Sources of Data, and Data Collection Procedure** details the primary financial statement inputs, market price series aggregators, regulatory publications, and the audit reconciliation protocols utilized to verify data integrity."
> "* **Section 3.5: Research Framework and Definition of Variables** delineates the conceptual valuation framework, establishes the operational definitions and measurement rules for dependent, independent, moderating, and robustness variables, and justifies the mathematical exclusion of price-derived ratios (P/E)."
> "* **Section 3.6: Methods of Analysis and Econometric Specification** details the baseline (Model 1) and regime-shift (Model 2) two-way fixed-effects panel regression models, formulates the MacKinnon-White HC3 robust inference procedure, accounts for finite-sample degrees of freedom, outlines econometric diagnostic tests, and specifies the eight-part robustness suite."

Each bullet paraphrases its own heading. Keep at most the compliance sentence and the section list, or delete the bullets.

3. Puffery in the population paragraph (line 30):

> "Over the past decade, successive consolidation mandates executed by NRB dramatically compressed the commercial banking sector from an apex of 32 institutions in FY 2011/12 to 20 commercial banks by mid-October 2023 (Asoj 2080 BS) (NRB, 2023). These 20 licensed institutions constitute the universal population of the modern Nepalese commercial banking industry."

"dramatically", "apex", and "universal population" add emphasis, not information. The numbers themselves (32 → 20) are cited to NRB 2023 but were NOT independently verified in this task (see NOT checked). Do not delete the numbers on slop grounds; delete the adjectives if the sentence is tightened.

4. Repetition of the freshness rule: the 5-day rule is stated in full in §3.3.4 (line 76), again as the MPS_RD operational measurement (§3.5.2, line 173), and its consequence (n = 28, missing coded, never imputed) is repeated in §3.3.4 and §3.5.2. Repetition across a methodology chapter is partly structural, but one of the two full statements can be shortened to a cross-reference without loss.

No meta comments about the writing process, no "as an AI" style remarks, and no placeholder text were found in the chapter.

## Pass 6 — LaTeX sync (spot-check only, not a full diff)

Checked in `src/thesis/chapters/chapter_03_research_methodology.tex`:

- MUST-FIX 1 (Group sentence), MUST-FIX 4 (line 76 freshness rule), MUST-FIX 5 (line 110 "official" wording), and MUST-FIX 3 (line 291, `linearmodels` in line 374 of the `.tex` file) all appear in the `.tex` version in the same wording. Any fix to them must be applied in both versions.
- MUST-FIX 2 (t-distribution) and MUST-FIX 6 (HC3 "discounts") were not separately located by line in the `.tex` file in this pass; the spot-check covered the flagged Markdown passages above, and the `.tex` HC3 section should be checked for the same two sentences before submission, because the `.tex` chapter was converted from the same text.
- One sync difference in the author's favour: the diagram typo in MINOR 1 (`l_t`, Markdown line 162) does not appear in the `.tex` diagram as searched — the `.tex` version should still be confirmed visually, but the Markdown version is the one that needs the fix.
- The corrected items from the previous loop (HBL 28.07, merger-related wording, A4/A6 notes) are present in both versions as far as this spot-check reached; no new divergence between versions was found in the passages checked.

## Verdict

Chapter 3 is, on its numbers, sound. Every price, gap, date, EPS, BVPS, DPS, restatement amount, and degree of freedom I recomputed matches the panel, the joined panel, or the tables, and the code matches the stated models, window, Post definition, and robustness suite. The chapter also gets its most important honesty statements right: NEPSE official closes are explicitly unverified, ShareSansar agreement is explicitly not independent verification, and estimates are framed as associations, not causal merger effects.

It is not yet submission-clean, because six MUST-FIX items remain, all wording or description errors rather than wrong estimates: the Group-equity generalisation, the unnamed t-distribution, the phantom `linearmodels` claim, the Chaitra-as-statute attribution in §3.3.4, the "official archives" phrase, and the reversed HC3 leverage verb. None of them changes a coefficient, a price, or the sample. Fix those six, then the seven MINOR items, and this chapter will match its own evidence.

## Fix list in priority order

1. MUST-FIX 1 — Scope the Group-equity sentence to GBIME (line 110, both versions).
2. MUST-FIX 2 — State Student's t on residual df in §3.6.3 (both versions).
3. MUST-FIX 3 — Delete `linearmodels` from line 291 (both versions).
4. MUST-FIX 4 — Change §3.3.4 line 76 to the operationalized-deadline wording used in line 173 (both versions).
5. MUST-FIX 5 — Replace "official secondary capital market trading archives" with "capital market data aggregators" (line 110, both versions).
6. MUST-FIX 6 — Correct "discounts high-leverage observations" to the inflation/conservative wording (line 267, both versions; check the `.tex` HC3 section too).
7. MINOR 1 — Fix diagram `l_t` to $\lambda_t$ (line 162).
8. MINOR 2 — Fix the Post-absorption equation to sum dummy indicators, not coefficients (lines 238–240).
9. MINOR 3 — Delete "mathematically and" from the purposive-sampling sentence (line 33).
10. MINOR 4 — Cite or soften the "standard Nepalese banking valuation convention" claim (line 110).
11. MINOR 5 — Name the specification behind VIF "≈ 30" or use the bivariate figure with its qualification (§3.5.2 ROA treatment).
12. MINOR 6 — Name the Excel workbook or delete "and Microsoft Excel" (line 291).
13. MINOR 7 — Clarify the VIF screening action, noting no regressor exceeds the threshold (§3.6.4 item 1).
14. Slop items 1–4 — Cut the generic opening, the roadmap bullets, the population adjectives, and one redundant full freshness statement.

## NOT checked (explicitly — never to be read as checked)

- The full text of BAFIA Section 59(2) was NOT independently verified in this task. The review checks the chapter against itself (line 173's "operationalized" vs line 76's "statutory deadline") and against the chapter's own description of the nine-month duty. Whether the statute names Chaitra, and the exact wording of its two duties, remains unverified here.
- All 5,663 report pages were NOT re-read. Panel values were recomputed from the panel's own columns and compared to the joined panel; PDF text was not re-read page by page in this task.
- Merolagani, ShareSansar, FinancialNotices, and NEPSE were NOT re-fetched live in this task. Price agreement is taken from Table A4 and the joined panel, exactly as the chapter presents it (cross-aggregator agreement, not official verification).
- NRB population history (32 institutions in FY 2011/12 → 20 by mid-October 2023), the "largest commercial bank" claim for GBIME, merger swap ratios and joint-operation dates, and the literature citations (Pant 2016, Cameron et al. 2008, MacKinnon-White 1985, Ohlson 1995, Kwon and Wang 2020, and the Master's Degree Dissertation Guidelines 2019, pp. 13–14) were NOT independently verified against their primary sources in this task. They are cited in the chapter; citation is not verification.
- The analysis test suite was NOT run in this task, and the rendered figures (F1–F6, A1–A3) were NOT re-viewed. Figure and table generation code was read for the diagnostics and robustness items cited, but this review does not certify the figures.
- The LaTeX chapter was NOT fully diffed against the Markdown chapter. Only the flagged passages listed in Pass 6 were spot-checked.
