# Data review 5: figures and curve types

## Question

Do the figures show what their captions say they show, are the
curve types correct for the question each figure answers, and does
any figure contradict a table?

## Method

- Read the generation code for F1 (scatter matrix), F2 (correlation
  heatmap), F3 (value-relevance scatter), F4 (coefficient forest),
  F5 (diagnostics, Model 1), F6 (trends), A1 (coverage map), A2
  (robustness forest), and A3 (diagnostics, Model 2).
- Viewed the rendered PNGs for F3, F4, and F6.
- Recomputed F3's per-period bivariate OLS slopes and compared them
  to Model 2's two-way fixed-effects slopes.
- Checked figure-to-text mapping (Chapter 4 Figure 4.1 = F6, 4.2 = F1,
  4.3 = F2, 4.4 = F3, 4.5 = F4, 4.6 = A2, 4.7 = F5) against the
  chapter's own crosswalk sentence.

## Findings by figure

### F1 scatter matrix (Chapter 4, Figure 4.2): PASS, descriptive

Seaborn pairplot on the analysis sample (n = 28), pairwise scatters,
linear fit lines, and univariate kernel densities for MPS_RD, EPS,
BVPS, DPS, and ROA. Curve type is correct for a descriptive
pairwise display: the fit lines are bivariate OLS, not model
estimates, and the caption says "linear fit lines". No table is
contradicted, because no table claims these bivariate slopes.

### F2 correlation heatmap (Chapter 4, Figure 4.3): PASS

Pearson correlations on the analysis sample, with significance stars
(* p < 0.05, ** p < 0.01, two-tailed). Values match T2 exactly as
recomputed. Colour scale is a standard diverging scale; no value is
hidden by colour choice, because the table carries the numbers.

### F3 value-relevance scatter (Chapter 4, Figure 4.4): CLARIFY (see below)

- **Points: PASS.** Rendered PNG viewed: 28 points, pre (blue) and
  post (vermillion), EPS panel and BVPS panel, axes MPS_RD (NPR)
  against EPS (NPR) and BVPS (NPR). Point positions match the joined
  panel (for example the pre-period HBL point at EPS 27.60, price
  520, is the top point in the EPS panel).
- **Lines: descriptive bivariate OLS per period, with 95% CI bands
  from seaborn's default (normal-based) bivariate fit.** The code
  is explicit about this (`sns.regplot`, per-period subsets), and
  the chapter caption says "OLS regression lines". That is honest
  as far as it goes, but it does not go far enough.
- **MUST CLARIFY: the lines are not the model slopes, and one sign
  flips.** Recomputed bivariate slopes: pre EPS 4.175, pre BVPS
  2.269, post EPS 0.305, post BVPS 0.803. Model 2 two-way FE slopes:
  pre EPS 5.577, pre BVPS 0.100, post EPS 2.453, post BVPS -1.658.
  The post-BVPS line in F3 slopes upward while Model 2's implied
  post-BVPS slope is negative. Both are correct answers to different
  questions: F3 asks "how do price and BVPS move together within
  each period, ignoring banks and years?"; Model 2 asks "how do
  price and BVPS move together within a bank-year, after absorbing
  bank and year effects and holding EPS constant?" The difference
  is the year-fixed-effects absorption story that is central to
  the thesis. Without a warning sentence, a reader (and an examiner)
  will reasonably read F3 as visual evidence for Model 2 and
  conclude the figure contradicts the table. Add to the F3 caption
  and to the Chapter 4 figure note: "Lines are descriptive
  bivariate OLS fits, not the two-way fixed-effects estimates in
  Table 4.4; the post-BVPS sign difference is the effect of
  absorbing year effects." This is a caption fix, not a figure
  regeneration: the figure itself is correct for its stated
  descriptive purpose.
- **CI bands: descriptive only.** F3's shaded bands are seaborn
  bivariate OLS confidence bands, not HC3-t bands. The caption does
  not claim HC3 for F3, so this is not an error, but the same
  warning sentence prevents a reader from importing HC3-t
  interpretation into F3.

### F4 coefficient forest (Chapter 4, Figure 4.5): PASS, and visually decisive

- Code uses Model 2 fit estimates and their HC3 confidence
  intervals (via `fit.term` and `t_test` combinations), regenerated
  after the `use_t=True` fix, so intervals are t-based.
- Rendered PNG viewed: six rows (pre EPS, pre BVPS, delta EPS,
  delta BVPS, post EPS, post BVPS), all six intervals cross zero.
  The figure therefore visually confirms what the tables say: no
  Model 2 coefficient is significant at 5%. A figure that showed
  any interval excluding zero would contradict T4; this one does
  not. The legend (pre slope / interaction / implied post slope)
  matches the row colours.
- One rendering note, minor: the legend overlaps the post-EPS
  interval's right tail in the PNG at this size. It does not hide
  any point estimate or interval endpoint, but moving the legend
  outside the plot area would be cleaner for the final PDF.

### F5 diagnostics, Model 1 (Chapter 4, Figure 4.7): PASS

Four panels (residuals vs fitted, Normal Q-Q, scale-location,
Cook's distance) from the Model 1 fit, via the shared diagnostics
panel code. The Q-Q panel is the thesis's stated basis for judging
residual normality (T6's note says so explicitly, rather than
reporting a formal normality test statistic). That is a defensible
choice at n = 28 with 12 parameters, provided the thesis does not
elsewhere claim a formal normality test passed; it does not.

### F6 trends (Chapter 4, Figure 4.1): PASS, with one visual subtlety

- Rendered PNG viewed: five panels (MPS_RD, EPS, BVPS, DPS, ROA)
  by bank series across six fiscal years, post-consolidation years
  shaded from FY2079/80 onward, legend in the sixth cell. Panel
  values match the panel: price collapse after the merger wave,
  EPS break, DPS halt to zero for most post rows, BVPS anchored.
  The code draws all 30 bank-years (`panel_all`), not just the
  analysis sample, which is correct for a trends figure.
- **Open markers for excluded prices: code-correct, visually
  subtle.** The code draws window-excluded raw prices (HBL and NIMB
  FY2077/78) as open markers on the MPS_RD panel, with a footnote
  explaining them. At PNG resolution the open markers are hard to
  distinguish from filled markers. This is not a data error, but
  for the final PDF, increase the open-marker size or add a
  direct label at those two points, so the auditability the code
  intends is actually visible to a reader.
- **X-axis: PASS.** Fiscal-year labels 2076-77 through 2081-82,
  post shading starting at the fourth tick (FY2079/80), consistent
  with the post definition.

### A1 coverage map, A2 robustness forest, A3 diagnostics (appendix): PASS on code

- A1: bank-by-year coverage grid (realised / window-excluded /
  entity-mismatch), matching the manifest coverage block (28
  realised, 13 pre, 15 post, HBL/NIMB FY2077/78 excluded, four
  FY2078/79 mismatch rows).
- A2: robustness forest for the EPS channel across R1-R8, from the
  same robustness fits as T5. The joint Wald story (only R6
  significant) is visible in the forest only via the delta panels;
  the figure does not itself plot Wald p-values, so it must not be
  cited as showing "only R6 rejects" without T5 alongside it.
- A3: Model 2 diagnostics panel, same code family as F5, applied
  to Model 2. No separate Model 2 Cook's table exists in T6 (which
  is Model 1); A3 is the Model 2 diagnostic record, and it should
  be cited as such if Model 2 influence is discussed.

## Curve-type verdict (the question the author asked directly)

- Scatter / pairplot (F1, F3 points): correct for description.
- Bivariate OLS lines (F1, F3 lines): correct for description,
  incorrect if read as model estimates. F1's caption is safe;
  F3's caption needs the warning sentence above.
- Heatmap (F2): correct for correlations.
- Forest plots with HC3-t intervals (F4, A2): correct for model
  inference, and F4's intervals are t-based after regeneration.
- Line trends with shading (F6): correct for longitudinal
  description, including the excluded-price open markers.
- Diagnostics panels (F5, A3): correct for residual and influence
  checking.

No figure was found to plot a wrong variable, a wrong sample, or a
fitted curve from a different model than its caption claims, except
for the F3 caption gap, which is a labelling gap, not a plotting
error. No figure needs regeneration for a numbers reason; F3 needs
a caption sentence, F4 needs a legend move (optional), F6 needs
larger open markers (optional, for visibility).
