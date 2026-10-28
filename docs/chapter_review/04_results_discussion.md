# Chapter 4 review: Results and Discussion

## Scope and rules of this review

- Chapter reviewed, in full, word by word: `docs/draft/thesis/chapter_04_results_and_discussion.md`
  (427 lines, as counted by `wc -l`).
- Repository state at review time: HEAD `9a46350`. No thesis file, table,
  figure, or data file was edited, moved, or deleted to write this review.
  This review file is the only output.
- LaTeX counterpart used for sync-spotting only:
  `src/thesis/chapters/chapter_04_results_and_discussion.tex` (582 lines).
  No full LaTeX diff was done; see Pass 7.
- Evidence sources actually used, not trusted on reputation:
  `data_analysis/analysis/outputs/tables/` T1, T2, T3, T4, T5, T6, A5, A6;
  `data_analysis/data_extract/output/manual_review/mps_rd_joined_panel.csv`
  (30 rows, 28 clean under gap ≤ 5 days) and
  `mps_rd_joined_panel_bonusadj.csv`; figure generation code
  `data_analysis/analysis/assets/f1_scatter_matrix.py`,
  `f2_correlation_heatmap.py`, `f3_value_relevance.py`,
  `f4_coefficient_forest.py`, `f5_diagnostics.py`, `f6_trends.py`,
  `a2_robustness_forest.py`, `_diagnostics_panel.py`.
- Recomputation method, stated so it can be repeated: descriptives
  (mean, sample SD with ddof = 1, min, max) and Pearson correlations
  recomputed from the joined panel with a plain NumPy script in `/tmp`
  (not the thesis pipeline, not statsmodels); Model 2 and robustness
  specifications R2–R8 recomputed with an independent NumPy OLS/HC3
  implementation (HC3 sandwich, Student's t on residual df, Wald F by
  quadratic form on the interaction covariance). R7 used the bonus-adjusted
  panel file; R8 used the clean panel with the two documented substitutions
  (GBIME FY2076/77 EPS 15.33, NMB FY2077/78 EPS 14.76).
- Classification used throughout:
  MUST-FIX = wrong number, wrong table reference, figure-text mismatch,
  causal overreach, significance misstatement, or a wrong methods
  explanation. MINOR = wording, grammar, repetition, slop.
  If a passage is correct, that is said briefly. No issue was invented
  to fill a quota.

## Passes run (as instructed)

- Pass 1: full read — narrative order vs tables, and whether the
  discussion stays associational, exploratory, and sensitivity-dependent.
- Pass 2: line-by-line proofread — grammar, duplicated words, broken
  sentences, inconsistent terms and symbols.
- Pass 3: every number checked against tables/panel — descriptives,
  correlations and stars, Model 1 and Model 2 coefficients, SEs,
  t values, p values, CIs, R-squared, adjusted R-squared, df, Wald F
  and p (baseline and R6), robustness coefficients, diagnostics,
  specification comparison.
- Pass 4: every figure note and figure interpretation checked against
  the figure code — sample n, bivariate vs fixed-effects lines, CIs,
  diagnostics model, panel layout.
- Pass 5: every mechanism or explanation — labelled plausible/not
  estimated, or stated as an established cause?
- Pass 6: slop hunt — meta comments, filler, repetition, deletable
  sentences.
- Pass 7: LaTeX sync — spot-check only, whether flagged passages also
  appear in the .tex version.

## Verdict

The numbers in Chapter 4 are, with the third-decimal rounding notes in
Pass 3, correct. Every descriptive statistic in Table 4.1, every
correlation in Table 4.2, every Model 1 and Model 2 coefficient, SE,
t, p, CI, R-squared, df, Wald statistic, and every R2–R8 coefficient
and Wald statistic I recomputed matches the chapter and the analysis
tables. That is the strong part of this chapter, and it should be said
plainly: the chapter does not invent a result.

The chapter is nevertheless NOT ready to submit as written, because
its figure notes are wrong in four places, and those are the places an
examiner looks first after the tables. Figure 4.2 claims five variables
and regression lines that the F1 figure does not contain. Figure 4.3
claims asterisks that the F2 heatmap does not print. Figure 4.6 claims
all eight specifications and book-value parameters that the A2 figure
does not contain. Figure 4.7 swaps the top-left and top-right panels.
Each of those is a MUST-FIX, and each is cheap to fix by rewriting the
note to match the code. The remaining MUST-FIX items are wording, not
numbers: unlabelled causal explanations in the Results narrative, one
causal sentence in the hypothesis section, and a backwards description
of HC3. Fix the figure notes first, then those sentences, then the
minor items. Do not submit with the figure notes as they stand: a
chapter whose tables are right and whose figure captions describe a
different figure will be read as careless, however good the estimation
is.

## Pass 1: narrative order and scope — mostly correct, with the exceptions in Pass 5

Correct, and therefore not flagged as issues:

- The Results order follows the tables: descriptives (Table 4.1),
  correlations (Table 4.2), Model 1 (Table 4.3), Model 2 (Table 4.4),
  hypotheses (Table 4.5), robustness (Table 4.6), diagnostics and
  specification comparison (Tables 4.7, 4.8). The introduction's
  seven-subsection list (lines 9–17) matches sections 4.2.1–4.2.7.
- The introduction's figure map (line 18) is correct:
  "Figure 4.1 maps to codebase asset F6, Figure 4.2 to F1, Figure 4.3
  to F2, Figure 4.4 to F3, Figure 4.5 to F4, Figure 4.6 to A2, and
  Figure 4.7 to F5." Each in-text figure reference matches that map.
- The headline framing is, in the places that matter most, correctly
  associational. Line 366 (see Pass 5) explicitly says the patterns
  are "interpreted not as proven causal effects, but as suggestive
  structural tendencies", and line 421 says the R6 evidence "is
  reported as an empirical association across calendar regimes, rather
  than as a causal merger effect." Those two sentences are the reason
  the chapter is not classified as causally overreaching overall.
  The overreach that remains is local, in sentences that state causes
  without that qualifier, listed in Pass 5.

## Pass 2: proofread

No duplicated word was found by a scripted scan of all 427 lines.
No broken sentence was found. Two genuine proofread errors were found:

### MINOR-1 — "three" factors, four bullets (line 399)

> "This divergence reflects three critical methodological factors:"

The bullets that follow are four, not three: (1) exclusion of
circular P/E multiples, (2) omission of macro-year fixed effects,
(3) standardized reporting-deadline measurement, (4) sample
harmonization. Change "three" to "four", or fold one bullet in.
This error also appears in the LaTeX version (see Pass 7).

### MINOR-2 — "unconditioned" (line 96)

> "neither bivariate association achieves statistical significance at the 5% level in the unconditioned sample."

"Unconditioned" is understandable but non-standard here; the chapter
elsewhere says "unadjusted" (for example line 96 itself begins "In raw,
unadjusted bivariate correlations"). Change to "unadjusted sample"
for consistency.

### MINOR-3 — symbol inconsistency in a figure title (line 204)

> "Figure 4.4: MPS_RD against Accounting Fundamentals Pre vs. Post Consolidation (Codebase Asset F3)"

Everywhere else the chapter writes the dependent variable as
$MPS^{RD}$. The underscore form appears only in this figure title.
Change to $MPS^{RD}$ for consistency. (The figure code itself uses
the label "MPS_RD (NPR)"; the inconsistency is in the chapter title,
not in the figure data.)

No other terminology inconsistency was found that changes meaning:
"pre-consolidation" / "post-consolidation" are used consistently
(34 / 22 occurrences of the hyphenated forms, zero unhyphenated
forms in a scripted count).

## Pass 3: every number — correct, with two third-decimal rounding notes that are NOT errors

### Descriptives (Table 4.1, lines 37–56) — all 60 cells match

My recomputation from the joined panel (28 clean rows, 13 pre,
15 post) reproduces T1 exactly, cell for cell, including:
MPS_RD full 254.34 (SD 98.82, 136.90–520.00), pre 310.59 (119.46,
176.00–520.00), post 205.60 (33.45, 136.90–251.13); EPS full 14.05
(6.52, 0.02–27.60), pre 17.90 (3.99, 12.08–27.60), post 10.72 (6.53,
0.02–22.06); BVPS full 160.18 (17.37, 132.71–190.70), pre 158.11
(19.10, 136.13–190.70), post 161.97 (16.18, 132.71–190.40); DPS full
3.56 (3.98, 0.00–12.50), pre 6.06 (3.56, 2.00–12.50), post 1.40 (2.97,
0.00–8.00); ROA full 0.99 (0.47, 0.00–1.79), pre 1.31 (0.22,
0.90–1.79), post 0.70 (0.44, 0.00–1.51).

Percentage changes in the narrative are also exact:
price erosion (310.59 − 205.60) / 310.59 = 33.80% (NPR 104.99);
price SD fall (119.46 − 33.45) / 119.46 = 72.00%;
EPS contraction (17.90 − 10.72) / 17.90 = 40.11%;
EPS SD rise (6.53 − 3.99) / 3.99 = 63.66%;
BVPS rise (161.97 − 158.11) / 158.11 = 2.44% (NPR 3.86);
DPS fall (6.06 − 1.40) / 6.06 = 76.90%;
ROA fall (1.31 − 0.70) / 1.31 = 46.56%.
The descriptive claims "all sampled banks distributed cash dividends"
pre-consolidation (pre DPS minimum 2.00) and "12 observations recorded
exactly zero cash dividends" post-consolidation (12 of 15 post DPS
values equal 0) both check out against the panel. The extremes
"Kumari Bank in FY 2080/81" EPS 0.02 and "HBL in FY 2076/77" price
520.00 and EPS 27.60 check out against A6.

### Correlations (Table 4.2, lines 83–98) — match, stars correct

Table 4.2 matches T2 exactly: MPS_RD–EPS 0.358, MPS_RD–BVPS 0.217,
MPS_RD–DPS 0.082, MPS_RD–ROA 0.378*, EPS–BVPS 0.372, EPS–DPS 0.612**,
EPS–ROA 0.975**, BVPS–ROA 0.278, DPS–ROA 0.595**. My recomputed
two-tailed p-values agree with the chapter's p-values (EPS–price
0.061, BVPS–price 0.268, ROA–price 0.047, DPS–price 0.678, EPS–BVPS
0.051, EPS–ROA < 0.001) within third-decimal rounding; see the rounding
note below. The stars in Table 4.2 are therefore correct, and the
VIF discussion in line 97 (1 / (1 − 0.975²) ≈ 20.2, "to 30.0 when
other covariates are included") is consistent with T2's note
("variance inflation ~ 30"). The EPS–BVPS VIF of 1.16 in Table 4.7
also checks: 1 / (1 − 0.372²) = 1.16.

### Model 1 (Table 4.3, lines 126–144) — match

EPS 2.095 (SE 4.096, t 0.51, p 0.616, CI [−6.587, 10.777]),
BVPS 0.219 (SE 1.858, t 0.12, p 0.908, CI [−3.720, 4.158]),
R² 0.948, adjusted R² 0.912, df 16, parameter count 1 + 4 + 5 + 2 = 12.
All match T3. The narrative rounding "NPR 2.10" and "NPR 0.22" for
the two slopes is correct rounding of 2.095 and 0.219.

### Model 2 (Table 4.4, lines 160–197) — match

Pre EPS 5.577 (3.560, t 1.57, p 0.140, CI [−2.059, 13.213]),
pre BVPS 0.100 (1.306, t 0.08, p 0.940, CI [−2.700, 2.901]),
δ_E −3.124 (4.003, t −0.78, p 0.448, CI [−11.710, 5.462]),
δ_B −1.758 (1.231, t −1.43, p 0.175, CI [−4.398, 0.882]),
post EPS 2.453 (2.269, t 1.08, p 0.298, CI [−2.412, 7.319]),
post BVPS −1.658 (1.120, t −1.48, p 0.161, CI [−4.059, 0.744]),
R² 0.978, df 14, joint Wald F(2, 14) = 2.954, p = 0.085.
All match T4, and my independent HC3 recomputation reproduces
every coefficient, SE, t, and p above to the printed precision, and
the Wald F = 2.954, p = 0.085. The statement that the stand-alone
Post main effect "is perfectly absorbed by the year fixed effects
and cannot be separately estimated" is correct: Post is an exact
linear combination of the post-year dummies.

### Hypotheses (Table 4.5, lines 225–253) — match

Every row matches Tables 4.3/4.4: H1 Model 1 (2.095, p 0.616),
H1 Model 2 (5.577, p 0.140), H2 Model 1 (0.219, p 0.908),
H2 Model 2 (0.100, p 0.940), H3 (−3.124, p 0.448),
H4 (−1.758, p 0.175), joint Wald (F(2, 14) = 2.954, p 0.085),
all "Fail to Reject H0" at 5%. The claim that H1/H2 decisions are
identical under Model 1 and Model 2 is true on these numbers.

### Robustness (Table 4.6, lines 263–287) — coefficients and Wald match; p-values recomputed for R3–R8 match

Table 4.6 matches T5 on every coefficient, SE, Wald F, p (for the
Wald column), and n. My independent recomputation additionally
reproduces the p-values the narrative reports for specifications
whose p-values are not printed in T5:
- R3: ROA 83.760 (79.852, p 0.312), δ_ROA −43.570 (83.671, p 0.611),
  δ_B −1.901 (1.290, p 0.163), Wald F(2, 14) = 2.46, p 0.121.
- R4: EPS 6.183 (4.508, p 0.193), BVPS −0.642 (1.378, p 0.649),
  δ_E −4.072 (5.151, p 0.443), δ_B −1.770 (1.335, p 0.208),
  Wald 2.77, p 0.100, df 13.
- R5: EPS 5.993 (4.635, p 0.225), δ_E −2.578 (5.521, p 0.650),
  δ_B −1.880 (1.419, p 0.215), Wald F(2, 10) = 2.41, p 0.139.
- R6: EPS 4.336 (3.724), BVPS 0.802 (1.328), δ_E −2.436 (4.755,
  p 0.620), δ_B −2.611 (1.517, t −1.72, p 0.116),
  Wald F(2, 10) = 5.82, p 0.021.
- R7 (bonus-adjusted panel): EPS 5.775 (4.145, p 0.185),
  δ_E −4.043 (4.446, p 0.379), δ_B −1.533 (1.595, p 0.353),
  Wald 2.37, p 0.130.
- R8 (restated panel): EPS 5.256 (3.016, p 0.103),
  δ_E −2.860 (3.807, p 0.465), δ_B −1.812 (1.223, p 0.161),
  Wald 2.92, p 0.087.
Note, for completeness only: the narrative for R7 and R8 does not
report the main BVPS slope p-values (R7: 0.927; R8: 0.981 by my
recomputation). That is an omission of two non-significant p-values,
not a wrong number, and Table 4.6 likewise omits them. Not flagged
as an issue.

### Diagnostics and specification comparison (Tables 4.7–4.8, lines 305–346) — match T6/A5

VIF EPS 1.16, VIF BVPS 1.16, tolerance 0.862; Breusch-Pagan LM 14.37,
p 0.213, χ²(11) critical value 19.68 at 5%; Cook's maximum 0.552,
threshold 4/28 = 0.143, 5 observations exceeding. All match T6.
Pooled EPS 4.882 (3.099), BVPS 0.552 (1.259), R² 0.136, df 25;
bank-FE-only EPS 5.217 (5.360), BVPS 1.432 (2.727), R² 0.176, df 21;
two-way FE EPS 2.095 (4.096), BVPS 0.219 (1.858), R² 0.948, df 16.
All match A5, including the df arithmetic (28 − 3 = 25, 28 − 7 = 21,
28 − 12 = 16).

### Third-decimal rounding notes — NOT errors, recorded so they are not mistaken for mismatches

- BVPS–price correlation p: chapter line 96 says 0.268. Recomputation
  from the full-precision r (0.2168) gives 0.267–0.268 depending on
  whether r is rounded to 0.217 first. This is rounding, not a
  mismatch, and it does not affect any significance decision.
- Pooled EPS p: chapter lines 346 and 401 say t = 1.58, p = 0.126.
  From the unrounded ratio 4.882 / 3.099 = 1.575, the two-tailed p
  on t(25) is 0.128; from the rounded t = 1.58 it is 0.127. The
  chapter's 0.126 is within 0.002 of either, and the conclusion
  ("not statistically significant") is unaffected. Not flagged
  as an issue, but the author should recompute p from unrounded
  values if a future revision touches that paragraph.

## Pass 4: figure notes vs figure code — four MUST-FIX mismatches

### MUST-FIX-1 — Figure 4.2 note claims five variables and fit lines that F1 does not contain (line 106)

Chapter text (line 106):

> "*Note.* Pairwise scatter plots, linear fit lines, and univariate kernel density distributions for $MPS^{RD}$, EPS, BVPS, DPS, and ROA ($N = 28$)."

Figure code (`f1_scatter_matrix.py`): `VARS_RENAME = {"price_rd": "MPS_RD", "eps": "EPS", "bvps": "BVPS"}`,
`vars=list(VARS_RENAME.values())`, `diag_kind="kde"`, and a plain
`seaborn.pairplot` with no `kind="reg"`. The figure therefore shows
exactly three variables (MPS_RD, EPS, BVPS), with scatter panels and
KDE diagonals, and no linear fit lines and no DPS or ROA panels.
The preceding sentence (line 100, "Figure 4.2 presents the bivariate
scatter plot matrix among all variables") is wrong for the same
reason: it is not "all variables". Rewrite the note to:
"Pairwise scatter plots and univariate kernel density distributions
for MPS_RD, EPS, and BVPS (N = 28)." If DPS and ROA panels are wanted,
the figure code must change, not just the note; as the figure stands,
the note must shrink to match it.

### MUST-FIX-2 — Figure 4.3 note claims asterisks that F2 does not print (line 112)

Chapter text (line 112):

> "*Note.* Correlation heatmap displaying pairwise Pearson correlation coefficients among value-relevance variables. Asterisks indicate statistical significance levels (\\* $p < 0.05$, \\*\\* $p < 0.01$)."

Figure code (`f2_correlation_heatmap.py`): `sns.heatmap(corr, annot=True, fmt=".2f", ...)`
over the five variables (MPS_RD, EPS, BVPS, DPS, ROA). The annotations
are two-decimal correlation values only; no asterisks are added to
any cell. The variables part of the note is correct (F2 does cover
all five variables, unlike F1), but the asterisks sentence describes
Table 4.2, not Figure 4.3. Delete the asterisks sentence from the
Figure 4.3 note, or add asterisks to the figure code and regenerate.
As written, a reader looking for asterisks in the heatmap will not
find them.

### MUST-FIX-3 — Figure 4.6 text and note claim eight specifications and book-value parameters that A2 does not contain (lines 289, 295)

Chapter text (line 289):

> "Figure 4.6 presents a coefficient forest plot summarizing parameter estimates and confidence intervals across all eight robustness specifications."

Chapter text (line 295):

> "*Note.* Forest plot comparing estimated earnings and book value slope parameters, regime interaction shifts, and 95% HC3 confidence intervals across robustness specifications R1 through R8 ($N = 28$ or $N = 23$)."

Figure code (`a2_robustness_forest.py`): `EPS_RUN_IDS = ("R1", "R2", "R4", "R5", "R6", "R7", "R8")`
— seven specifications, with R3 explicitly omitted because ROA is
"measured in percentage points" and "not on this scale". The left
panel plots the earnings coefficient only; the right panel plots
δ_E (EPS × Post) only. There is no book-value slope panel and no
δ_B panel, and R1 has no interaction row on the right. Rewrite to:
"Forest plot of the EPS-channel estimates (earnings coefficient and
EPS × Post interaction) with 95% HC3 confidence intervals across
seven specifications (R1, R2, R4–R8; R3 omitted because ROA is on a
different scale; N = 28 or N = 23)." The current wording would make
an examiner expect a BVPS forest that is not in the figure.

### MUST-FIX-4 — Figure 4.7 note swaps the top two panels (line 330)

Chapter text (line 330):

> "*Note.* Four-panel diagnostic suite for Model 1: (top-left) Residuals vs. Fitted values assessing linearity; (top-right) Normal Q-Q plot assessing error normality; (bottom-left) Scale-Location plot ...; (bottom-right) Cook's distance ..."

Figure code (`_diagnostics_panel.py`): `ax_qq, ax_res, ax_scale, ax_cooks = axes.ravel()`
with `PANEL_TITLES = ("(a) Normal Q-Q", "(b) Residuals vs fitted", "(c) Scale-location", "(d) Cook's distance")`.
In row-major order that is: top-left Normal Q-Q, top-right
Residuals vs fitted, bottom-left Scale-location, bottom-right
Cook's distance. The chapter note has the top two reversed.
The bottom two positions in the note are correct. The introductory
sentence at line 324 lists the panels in the same swapped order
("(Residuals vs Fitted, Normal Q-Q, Scale-Location, and Cook's
Distance)"); if that sentence is meant as a list rather than a
layout, it is harmless, but the note's explicit "(top-left)" /
"(top-right)" labels are wrong and must be swapped.

### Figure notes that ARE correct (checked, not flagged)

- Figure 4.1 / F6 (lines 70–74): five variables, six fiscal years,
  post shading FY2079/80–2081/82, open markers for the two
  window-excluded prices. Code (`f6_trends.py`) uses `panel_all`
  (30 rows), draws all five panels, shades from the first post year,
  and draws the excluded prices as open markers. One incompleteness,
  classified MINOR below: the note does not say the price line
  itself connects through the open markers (code draws the full
  line, then overlays the open marker). The note is not wrong about
  the markers; it is silent about the line.
- Figure 4.4 / F3 (lines 204–207): bivariate per-period OLS lines,
  explicitly "not the two-way fixed-effects estimates in Table 4.4",
  with the post-BVPS sign difference attributed to absorbing year
  effects. Code (`f3_value_relevance.py`) does exactly this:
  `sns.regplot` on each period subset, `dataset.panel` (n = 28).
  This note is the model for how the other figure notes should read.
- Figure 4.5 / F4 (lines 210–213): pre slopes, interactions, implied
  post slopes, HC3 95% CIs on t(14), N = 28, df 14. Code
  (`f4_coefficient_forest.py`) builds exactly those six rows,
  including the two linear combinations by t-test under the HC3
  covariance. Correct.

## Pass 5: mechanisms and explanations — the disclaimer is good; the unlabelled causes are not

### Correct framing (not flagged)

Line 366, the opening of section 4.3.2:

> "Because neither individual interaction term achieves statistical significance at conventional thresholds, and the joint Wald test in the baseline sample is marginally significant at 10% ($p = 0.085$), these patterns are interpreted not as proven causal effects, but as suggestive structural tendencies consistent with several economic and institutional mechanisms operating in Nepal's post-merger banking environment:"

Line 371, mechanism 4, likewise says the negative BVPS slope "cannot
therefore be presented as an established empirical law" and calls it
"an exploratory point estimate". Mechanism 1 (line 368) is labelled
"(Plausible Mechanism)" and ends "though direct asset quality
variables are not estimated in the econometric model." Mechanism 2
(line 369) hedges with "may have factored". Those four passages are
how the rest of the chapter should be written.

### MUST-FIX-5 — unlabelled causal explanations in the Results narrative (lines 61–64)

These four sentences sit in section 4.2.1, before any disclaimer,
and state causes as facts. None of the cited causes is a regressor
in any model in this chapter (no macro-tightening variable, no NPL
variable, no reserve variable, no regulatory-restriction variable):

Line 61:

> "This price compression reflects both broader macroeconomic tightening in Nepal and a general market repricing of commercial bank equities toward a narrower, lower valuation band."

Line 62:

> "This divergence indicates that post-merger integration, marked by non-performing loan (NPL) recognition, provisioning burdens, and harmonization adjustments, induced substantial earnings volatility across surviving entities."

Line 63:

> "The stability of BVPS reflects the accumulation of statutory reserves and regulatory capital requirements mandated by NRB, even as cash dividend distributions were halted."

Line 64:

> "Across the 15 post-consolidation bank-years, 12 observations recorded exactly zero cash dividends, driven by regulatory restrictions on capital distribution, elevated credit-loss provisioning, and dividend withholding to preserve regulatory capital adequacy ratios."

The numbers in each sentence are correct (see Pass 3). The causal
verbs ("reflects", "induced", "driven by") are the problem. Soften
each to a consistency statement ("is consistent with", "is
compatible with") or move the explanations into section 4.3.2 under
the existing disclaimer. As written, a reader cannot tell which parts
of section 4.2.1 are estimated results and which are interpretation.

### MUST-FIX-6 — "induced" in the hypothesis section (line 253)

> "While the study cannot reject the null hypothesis of parameter stability at the strict 5% level, the marginal significance ($p < 0.10$) indicates that corporate consolidation induced non-trivial joint adjustments across accounting valuation multiples."

This sentence follows a correct fail-to-reject at 5% and then uses
the causal verb "induced" for a joint test that is itself only
marginally significant at 10%. Change "induced" to "is consistent
with" (matching line 366). The same point applies, in weaker form,
to line 285's "purging the entity-timing asymmetry reveals a
statistically significant joint structural difference" and to the
label "clean specification" for R6: R6 drops one year; it does not
purge every timing or measurement limitation (aggregator prices,
n = 23, df = 10). Those two phrases are classified MINOR below
because the surrounding paragraphs already say the evidence is
sensitivity-dependent; line 253 has no such qualifier in its own
sentence and is therefore MUST-FIX.

### MINOR-4 — mechanism 3 stated as a cause without a source or hedge (line 370)

> "Following consolidation, capital conservation requirements and regulatory provisioning mandates led banks to suspend cash distributions (mean DPS fell to NPR 1.40, with 12 of 15 post-consolidation bank-years recording zero cash dividends)."

The DPS numbers are correct. The causal claim ("led banks to
suspend") has no citation in the sentence and no "may have" hedge,
unlike mechanisms 1, 2, and 4. Either cite the specific NRB
requirement or hedge to "coincided with". Do not present it as an
estimated result: no regulatory variable is in any model.

### MINOR-5 — Kwon and Wang comparison overstates what insignificant estimates "indicate" (section 4.3.3, item 1)

> "our findings indicate that corporate amalgamations generate accounting noise and structural disruption that reduce the valuation relevance of earnings."

The interaction estimates behind this sentence are δ_E = −3.124
(p = 0.448) and δ_B = −1.758 (p = 0.175), both insignificant, with
a joint test that fails at 5%. "Indicate that amalgamations
generate" is stronger than those estimates support. Change to
"are consistent with the view that amalgamations can generate".
The literature accuracy of the Kwon and Wang summary itself was NOT
checked (see "NOT checked" below); only the strength of the
inference from this chapter's own estimates is flagged here.

### MINOR-6 — "demonstrates" in R5, and "clean specification" in R6 (lines 282, 285)

Line 282:

> "This demonstrates that the negative interaction shifts are not solely driven by temporary integration write-offs in the immediate post-merger fiscal year."

R5's own interaction p-values are 0.650 and 0.215 and its Wald
p = 0.139, all insignificant. "Demonstrates" is too strong for a
sensitivity check whose estimates do not reject anything. Change
to "is consistent with the shifts not being solely driven by".
Line 285's "clean specification" for R6 should become "the
FY2078/79-excluded specification" to avoid implying R6 is free of
the chapter's other limitations.

### MINOR-7 — "unbiased benchmark" and "econometrically mandatory" (lines 342, 334)

Table 4.8 assessment column:

> "Rigorously absorbs both unobserved bank heterogeneity and macro-year shocks; unbiased benchmark."

Two-way fixed effects control for time-invariant bank effects and
common year effects only. They do not by themselves make the
estimates unbiased in the presence of the chapter's own disclosed
limitations (aggregator prices, entity mismatch in the baseline,
measurement timing). Change "unbiased benchmark" to "preferred
benchmark" or "most controlled specification". Similarly, line 334:

> "To demonstrate why two-way fixed effects estimation is econometrically mandatory, Table 4.8 compares ..."

"Mandatory" overstates what a specification comparison can show.
Change to "preferred" or "chosen". Neither change affects any number.

### MINOR-8 — Table 4.1 note says "verified market closing series" (line 57)

> "Data recompiled from published annual reports and verified market closing series."

Elsewhere the thesis discloses that prices are cross-checked
aggregator prices and that NEPSE official closes were never
verified. The bare word "verified" in this note, without the
qualifier "cross-checked aggregator", invites the reading the
thesis elsewhere disavows. Change to "cross-checked aggregator
market closing series". This is wording, not a wrong value, and
is therefore MINOR, but an examiner who reads this note in
isolation will take it as a stronger claim than the thesis can
support.

### MINOR-9 — Wald tests called "two-tailed" (lines 197, 237)

Line 197: "Under the designated two-tailed 5% significance threshold,
the null hypothesis of structural stability cannot be rejected
($p = 0.085 > 0.05$)." Line 237 (Table 4.5 note): "All tests evaluated
at two-tailed $\\alpha = 0.05$." The t-tests for individual
coefficients are two-tailed; a Wald F test is by construction a
right-tail test (reject for large F). The p-values themselves are
correct. Remove "two-tailed" from the Wald rows / note, or write
"at $\\alpha = 0.05$ (two-tailed t-tests; right-tail F test)".
Not a significance error in the numbers; a significance-description
error in the words.

## Pass 6: slop hunt

No meta comments were found: no text about the writing process, no
"as discussed above" filler that substitutes for an argument, no
placeholder text, no authorial aside. The chapter's roadmap
(lines 9–18) is standard thesis structure, not slop, and is not
flagged.

Repetition that is genuinely deletable with no loss:

### MINOR-10 — verbatim re-reporting of Model 2 in the Discussion openings

Section 4.3.1 opens by reprinting the Model 2 pre slopes with full
SEs, t values, and p-values already given in Table 4.4 and
section 4.2.4:

> "In the pre-consolidation regime (FY 2076/77 through FY 2078/79), the estimated valuation multiple for earnings per share was $\\hat{\\beta}_E = 5.577$ (HC3 SE = 3.560, $t = 1.57, p = 0.140$ on $t(14)$), whereas the multiple for book value per share was $\\hat{\\beta}_B = 0.100$ (HC3 SE = 1.306, $t = 0.08, p = 0.940$ on $t(14)$)."

Section 4.3.2 opens the same way for the interactions and implied
post slopes (δ_E = −3.124, p = 0.448; δ_B = −1.758, p = 0.175;
post EPS 2.453, p = 0.298; post BVPS −1.658, p = 0.161). The numbers
are correct, and a short reminder is legitimate in a Discussion.
Reprinting the full SE/t/p apparatus a second time is not: compress
each opening to one sentence referencing Table 4.4 ("As reported in
Table 4.4, ...") and spend the saved lines on interpretation, which
is what the Discussion is for. The same applies, in smaller degree,
to the final summary paragraph (line 427), which restates the R6
conclusion already stated at line 421 and in section 4.2.6; it can
be cut to a single closing sentence without losing any result.

### MINOR-11 — Figure 4.1 note incompleteness (line 74)

> "Window-excluded prices for HBL and NIMB in FY 2077/78 are represented as open markers."

True, and the figure code does draw those open markers. What the
note does not say is that the price line itself is drawn through
all six years including the excluded points, with the open marker
overlaid (`f6_trends.py`: the price panel plots the full series,
then plots the excluded points again with `mfc="none"`). Add
"the connecting line passes through the excluded points; only the
marker denotes exclusion" or change the code to break the line.
As written, a reader may infer the line breaks at the gap. It does
not.

### MINOR-12 — emotive adjectives that add no information

Examples, not errors, listed so the author can decide whether to
keep them: "severe secular decline" (line 61), "precipitous
collapse" (line 64), "extraordinarily high coefficient of
determination" (line 144), "catastrophic variance inflation"
(line 97), "massive macro-market repricing" (line 144). None changes
a number. In a results chapter, "large" with the number beside it
carries the same information with less editorialising. Deleting or
softening these adjectives loses nothing.

## Pass 7: LaTeX sync (spot-check only, not a full diff)

Spot-checked passages were found in the .tex version with the same
content as the Markdown version, including the same errors:

- Figure 4.2 note (tex line 146): same five-variable, fit-line
  wording as MUST-FIX-1.
- Figure 4.3 note (tex line 158): same asterisks sentence as
  MUST-FIX-2.
- Figure 4.6 text (tex line 409): same "across all eight robustness
  specifications" as MUST-FIX-3.
- Figure 4.7 note (tex line 469): same swapped top-left/top-right
  labels as MUST-FIX-4.
- "Three critical methodological factors" (tex line 548): same
  count error as MINOR-1.
- The R8 / HBL sentence, the Wald values, and the R6 values were
  spot-checked and match the Markdown chapter; no LaTeX-only
  numeric divergence was found in the passages spot-checked.

Conclusion for Pass 7: every fix in the numbered list below must be
applied in BOTH the Markdown chapter and the .tex chapter, or the
two versions will diverge again. A full LaTeX diff was NOT done
and is NOT claimed here.

## Pass 3 (continued): a methods explanation that is wrong — MUST-FIX

### MUST-FIX-7 — HC3 described backwards (line 322), and "controlled via HC3" (Table 4.7)

Chapter text (line 322):

> "Deployment of HC3 standard errors explicitly addresses this leverage, as HC3 weights squared residuals by $(1 - h_{ii})^2$, effectively downweighting influential high-leverage observations."

This is backwards in both the factor and the direction. The HC3
sandwich divides squared residuals by $(1 - h_{ii})^2$ — that is,
it multiplies them by $1 / (1 - h_{ii})^2$, which is larger, not
smaller, for high-leverage observations (h close to 1). The purpose
is to correct for the fact that high-leverage OLS residuals are
artificially small, not to downweight those observations. HC3 also
does not "control" or remove influential observations; it adjusts
standard errors. Table 4.7's assessment "Controlled via HC3 robust
inference" for Cook's distance (line 315) makes the same overclaim
in short form. Rewrite line 322 to: "HC3 divides squared residuals
by $(1 - h_{ii})^2$, inflating high-leverage residuals to offset
their artificially small OLS residuals; it adjusts standard errors
but does not remove or downweight influential observations."
No table number changes. The diagnostic values themselves (max
Cook's D 0.552, 5 exceeding 0.143, BP LM 14.37, p 0.213) are correct
as reported in T6; only the HC3 explanation is wrong.

## Fix list, in priority order

1. MUST-FIX-1 — Rewrite the Figure 4.2 note to three variables
   (MPS_RD, EPS, BVPS), scatter + KDE only, no fit lines; fix the
   line 100 sentence "among all variables" the same way. Both versions.
2. MUST-FIX-2 — Delete the asterisks sentence from the Figure 4.3
   note (or add asterisks to F2 and regenerate). Both versions.
3. MUST-FIX-3 — Rewrite the Figure 4.6 text and note to seven
   EPS-channel specifications (R1, R2, R4–R8; R3 omitted), earnings
   coefficient and δ_E only. Both versions.
4. MUST-FIX-4 — Swap the top-left/top-right labels in the
   Figure 4.7 note (top-left Normal Q-Q, top-right Residuals vs
   fitted). Both versions.
5. MUST-FIX-5 — Soften the four causal sentences in section 4.2.1
   (lines 61–64) to consistency statements, or move them under the
   section 4.3.2 disclaimer.
6. MUST-FIX-6 — Change "induced" to "is consistent with" in
   line 253.
7. MUST-FIX-7 — Correct the HC3 description in line 322 and the
   "Controlled via HC3" assessment in Table 4.7.
8. MINOR-1 — "three" to "four" methodological factors (line 399).
   Both versions.
9. MINOR-8 — "verified market closing series" to "cross-checked
   aggregator market closing series" (line 57).
10. MINOR-9 — Remove "two-tailed" from the Wald F description
    (lines 197, 237).
11. MINOR-4 — Hedge or cite mechanism 3 (line 370).
12. MINOR-5 — Soften the Kwon and Wang "indicate that amalgamations
    generate" sentence to "are consistent with".
13. MINOR-6 — Soften "demonstrates" (line 282) and "clean
    specification" (line 285).
14. MINOR-7 — "unbiased benchmark" to "preferred benchmark"
    (line 342); "econometrically mandatory" to "preferred" (line 334).
15. MINOR-2, MINOR-3 — "unconditioned" to "unadjusted" (line 96);
    figure title MPS_RD to $MPS^{RD}$ (line 204).
16. MINOR-10, MINOR-11, MINOR-12 — Compress the Discussion openings
    that reprint full SE/t/p apparatus; add the F6 line-through
    clarification; consider softening the emotive adjectives.
    These are polish, not submission blockers.

## NOT checked (stated plainly so it is never misread as checked)

- Rendered figure PDFs/PNGs were NOT viewed in this review. Figure
  checks were against generation code only. A rendered figure could
  in principle differ from what its code intends (for example a
  stale output file); the manifest hashes for the figure files were
  not verified here.
- Cook's distance per-observation identities, Breusch-Pagan, and VIF
  were NOT independently recomputed from raw data in this review,
  because statsmodels/scipy were not available in this session's
  Python environments. They were checked chapter-vs-T6 only, where
  they agree exactly. The per-observation claim "maximum Cook's D
  of 0.552 (HBL FY 2076/77)" is therefore reported as
  chapter-consistent-with-T6, not as independently recomputed.
- Literature accuracy was NOT checked: Bhattarai (2014), Bhandari
  et al. (2026), Joshi et al. (2023), Chhetri (2023), Giri (2024),
  Pant et al. (2024), Chaudhari (2025), Timalsina (2026), Kwon and
  Wang (2020), Ohlson (1995), Bhattacharya (1979), John and Williams
  (1985), Morgan (2002), Flannery et al. (2004), Almumani (2014),
  Malhotra and Tandon (2013), the NRB 2015 NPR 8.0 billion directive,
  and the sample descriptions of prior studies (for example
  "14 commercial banks over 2006–2014 comprising 35 pooled bank-year
  observations") were not verified against their sources in this
  review. Only the strength of inference drawn from this chapter's
  own estimates was assessed for those passages.
- Chapter 1's hypothesis statements, Chapter 3's methodology, and
  the proposal were NOT re-checked here; hypothesis labels H1–H4
  were checked only for internal consistency with Tables 4.3/4.4.
- The LaTeX version was NOT fully diffed against the Markdown
  chapter (Pass 7 was spot-checks only).
- NEPSE official-close verification, per-row disclosure proof, and
  supervisor approval are NOT re-litigated here; they are standing
  limits from the data review, and nothing in Chapter 4 removes them.
  Chapter 4's own framing as associational and exploratory is
  consistent with those limits, except for the specific sentences
  flagged in Pass 5.
