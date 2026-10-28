# Data review 4: analysis models, tables, and diagnostics

## Question

Do the analysis tables follow from the joined panel, under the
inference the thesis claims, or do they follow from some other
sample, some other estimator, or some other distribution?

## Method

- Independent recomputation from `mps_rd_joined_panel.csv`, clean
  sample only (gap <= 5, n = 28), with explicit bank dummies
  (GBIME reference) and year dummies (FY2076/77 reference), OLS,
  MacKinnon-White HC3 covariance computed from leverages, and
  Student's t on residual degrees of freedom for p-values and
  intervals. No thesis pipeline code was reused for the
  recomputation; the pipeline was used only as the thing being
  checked.
- Compared the recomputation to T1 (descriptives), T2 (correlations),
  T3 (Model 1), T4 (Model 2), T5 (robustness coefficients and Wald),
  T6 (diagnostics), A5 (specification comparison), and A6 (analysis
  dataset).

## Findings: descriptives and correlations (T1, T2)

- **PASS, exact.** Every mean, standard deviation, minimum, and
  maximum in T1 reproduces, including MPS_RD full 254.34 (SD 98.82),
  pre 310.59 (SD 119.46), post 205.60 (SD 33.45); EPS 14.05 (SD 6.52);
  BVPS 160.18 (SD 17.37); DPS 3.56 (SD 3.98); ROA 0.99 (SD 0.47), and
  every pre/post split. Derived percentage changes in the thesis
  text (price -33.80%, EPS -40.11%, DPS -76.90%, ROA -46.56%) are
  arithmetically correct from these means.
- **PASS, exact.** Every correlation in T2 reproduces, including
  MPS_RD-EPS 0.358 (p = 0.061), MPS_RD-BVPS 0.217 (p = 0.268),
  MPS_RD-ROA 0.378 (p = 0.047), EPS-BVPS 0.372 (p = 0.051), EPS-DPS
  0.612 (p < 0.01), EPS-ROA 0.975 (p < 0.001). The EPS-ROA correlation
  is the reason ROA never appears alongside EPS: the bivariate VIF
  from r = 0.975 is about 20, and the four-variable exploratory VIFs
  were about 30 (EPS) and 27 (ROA). T2's note ("variance inflation
  ~ 30") refers to the multivariate figure; the bivariate figure is
  about 20. Both are in the thesis in different places; neither is
  wrong, but the thesis should state which model each VIF comes
  from in the same sentence, as the chapter review already noted.

## Findings: Model 1 and Model 2 (T3, T4)

- **PASS, exact (within third-decimal rounding).** Model 1: EPS
  2.095 (SE 4.096, CI [-6.587, 10.777], p = 0.616), BVPS 0.219
  (SE 1.858, CI [-3.720, 4.158], p = 0.908), R-squared 0.948, df 16.
  Model 2: pre-EPS 5.577 (SE 3.560, CI [-2.059, 13.213], p = 0.140),
  pre-BVPS 0.100 (SE 1.306, CI [-2.700, 2.901], p = 0.940),
  delta_E -3.124 (SE 4.003, p = 0.448), delta_B -1.758 (SE 1.231,
  p = 0.175), post-EPS 2.453 (SE 2.269, p = 0.298), post-BVPS -1.658
  (SE 1.120, p = 0.161), R-squared 0.978, df 14, joint Wald
  F(2, 14) = 2.954, p = 0.085. These are the t-based values, not the
  normal-approximation values from the pre-57c78a0 tables. The
  pipeline fix (`use_t=True`) is verified by the tables themselves,
  not merely by reading the code.
- **Degrees of freedom: PASS.** Model 1: 1 intercept + 4 bank dummies
  + 5 year dummies + 2 slopes = 12 parameters, 28 - 12 = 16 residual
  df. Model 2: +2 interactions = 14 parameters, 14 residual df.
  The standalone Post effect is absorbed by the year dummies, as
  the thesis states; it is not separately estimated, and no table
  reports it as if it were.
- **No coefficient is significant at 5% in either baseline model.**
  This is a finding about the data, not a flaw in the tables: the
  tables report it plainly, and the thesis conclusions (after the
  57c78a0 revision) report it plainly. Any future edit that makes
  a baseline coefficient look significant by switching back to
  normal p-values, by dropping year dummies, or by cherry-picking
  R6 would be a regression in honesty, not an improvement.

## Findings: robustness (T5) and specification comparison (A5)

- **PASS on the values checked.** T5 coefficients and Wald
  statistics for R1-R8 match the earlier independent recomputation
  (R3 ROA 83.760, delta_ROA -43.570, Wald 2.46, p = 0.121; R4 EPS
  6.183, delta_E -4.072, Wald 2.77, p = 0.100; R5 EPS 5.993,
  delta_E -2.578, Wald 2.41, p = 0.139; R6 EPS 4.336, BVPS 0.802,
  delta_E -2.436 (SE 4.755), delta_B -2.611 (SE 1.517), Wald 5.82,
  p = 0.021; R7 and R8 as tabled). T5 now reports delta standard
  errors for every specification, which is what makes this check
  possible; the pre-57c78a0 table did not, which is how the R6
  delta_B error survived.
- **R8 rows: PASS, with the clarification already in the thesis.**
  In-sample R8 substitutions are GBIME FY2076/77 (15.33) and NMB
  FY2077/78 (14.76). The pipeline config also lists HBL FY2077/78
  (27.60), but that row is window-excluded, so it cannot affect
  any R8 estimate. Table A6 flags all three rows in the full
  dataset; T5's note lists the two in-sample rows. The thesis
  explains this; keep the explanation wherever R8 is discussed.
- **A5: PASS.** Pooled EPS 4.882 (SE 3.099, R-squared 0.136, df 25),
  bank-FE-only EPS 5.217 (SE 5.360, R-squared 0.176, df 21),
  two-way FE EPS 2.095 (R-squared 0.948, df 16). The R-squared jump
  from 0.136 to 0.948 when year dummies are added is real, and it
  is the thesis's strongest evidence that year effects, not
  accounting slopes, drive most price variation in this sample.
  It is also the reason the thesis must not claim that accounting
  fundamentals "explain" 94.8% of price variation: the year
  dummies explain most of it, and the thesis's revised wording
  correctly presents the comparison as a comparison, not a
  decomposition.

## Findings: diagnostics (T6)

- **PASS.** VIF 1.16 for EPS and BVPS (tolerance 0.862), computed on
  substantive regressors only, matches the recomputed EPS-BVPS
  correlation (1 / (1 - 0.372^2) = 1.16). Breusch-Pagan LM 14.37
  (p = 0.213) is reported for disclosure; HC3 is the designated
  answer to heteroskedasticity, not the Breusch-Pagan result.
- **Cook's distance: PASS, with a clarification to prevent a false
  alarm.** T6 reports max Cook's D 0.552, 5 of 28 above 4/28 = 0.143,
  for Model 1 (k = 12). An independent recomputation for Model 2
  (k = 14) gives max 0.490 at KBL FY2076/77, also 5 above threshold.
  These are different models, so the two maxima differ legitimately.
  T6 correctly labels itself as Model 1 diagnostics. Do not
  "correct" T6 to 0.490, and do not cite T6's 0.552 as a Model 2
  diagnostic. If a future table reports Model 2 diagnostics, it
  must compute Cook's D with k = 14 and label it as such.

## Verdict for this file

Analysis models and tables: PASS. The tables follow from the joined
panel under the claimed estimator and distribution, with no
sample, estimator, or distribution substitution found. The only
analysis-related fix in this phase is the A4 note (see file 03),
which is a verification note, not a model value.
