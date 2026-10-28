# Supervisor review: Chapter IV, Results and Discussion

Draft file: `docs/draft/thesis/chapter_04_results_and_discussion.md`
Verdict: The numbers in the tables are, with two exceptions, exactly right.
The discussion is where the thesis fails its own standard. It upgrades a
suggestive, sensitivity-dependent joint result into a conclusive causal
claim, it reports a wrong standard error for the key sensitivity, and it
presents untested mechanisms as explanations. This chapter needs the most
rewriting of any chapter, even though it needs no new data.

## Numbers verified by independent recomputation

All from the joined panel, clean sample n = 28, using an independent OLS/HC3
implementation (not the thesis pipeline):

- Table 4.1 descriptives: every mean, standard deviation, minimum, and maximum
  reproduced exactly, including MPS_RD 254.34 (SD 98.82), pre 310.59 (SD 119.46),
  post 205.60 (SD 33.45), EPS 14.05 (SD 6.52), BVPS 160.18 (SD 17.37),
  DPS 3.56 (SD 3.98), ROA 0.99 (SD 0.47), and every pre/post split.
  Percentage changes stated in the text are correct: price -33.80%,
  EPS -40.11%, DPS -76.90%, ROA -46.56%, price SD -72.00%, EPS SD +63.66%.
  Post-consolidation zero-DPS count is correct: 12 of 15.
- Table 4.2 correlations: MPS_RD-EPS 0.358 (p = 0.061), MPS_RD-BVPS 0.217
  (p = 0.268), MPS_RD-DPS 0.082 (p = 0.678), MPS_RD-ROA 0.378 (p = 0.047),
  EPS-BVPS 0.372 (p = 0.051), EPS-ROA 0.975 (p < 0.001), EPS-DPS 0.612
  (p < 0.001). All reproduced. The EPS-ROA bivariate VIF is 1/(1-0.975^2)
  = about 20, consistent with the chapter's "about 20 to 30" range when
  multivariate VIFs are included.
- Table 4.3 (Model 1): EPS 2.095 (SE 4.096), BVPS 0.219 (SE 1.858),
  R-squared 0.948, adjusted 0.912, df 16. Reproduced exactly.
- Table 4.4 (Model 2): pre-EPS 5.577 (SE 3.560), pre-BVPS 0.100 (SE 1.306),
  delta_E -3.124 (SE 4.003), delta_B -1.758 (SE 1.231), post-EPS 2.453
  (SE 2.269), post-BVPS -1.658 (SE 1.120), R-squared 0.978, df 14, joint Wald
  F(2, 14) = 2.954, p = 0.085. Coefficients and standard errors reproduced
  exactly. P-values and confidence intervals did not (see must-fix 1).
- Table 4.6 robustness coefficients: R3 (ROA 83.760, SE 79.852; delta_ROA
  -43.570; delta_B -1.901; Wald 2.46, p = 0.121), R4 (EPS 6.183, SE 4.508;
  BVPS -0.642, SE 1.378; delta_E -4.072; delta_B -1.770; Wald 2.77, p = 0.100),
  R5 (EPS 5.993; delta_E -2.578; delta_B -1.880; Wald 2.41, p = 0.139),
  R6 (EPS 4.336; BVPS 0.802; delta_E -2.436; delta_B -2.611; Wald 5.82,
  p = 0.021) reproduced exactly for coefficients and Wald statistics.
- Table 4.7 diagnostics: VIF 1.16 for both EPS and BVPS (tolerance 0.862),
  Breusch-Pagan LM 14.37 (p = 0.213) as reported, Cook's maximum 0.552 at HBL
  FY 2076/77 with 5 observations above 0.143. Reproduced exactly when Cook's
  distance uses the correct parameter count (12). An earlier, incorrect
  recomputation in this review used 2 parameters and gave 3.312; that was
  the reviewer's error, not the thesis's, and it is recorded here so the
  correction is auditable.
- Table 4.8 specification comparison: pooled EPS 4.882 (SE 3.099),
  R-squared 0.136; bank-FE-only EPS 5.217 (SE 5.360), R-squared 0.176;
  two-way FE EPS 2.095, R-squared 0.948. Reproduced exactly.

## Must fix

1. **P-values and confidence intervals use the normal distribution, not
   t(df) (Tables 4.3, 4.4, 4.5, and the robustness discussion).** Every
   coefficient interval in this chapter is coefficient +/- 1.96 x SE, and
   every coefficient p-value matches the normal distribution, not the
   t distribution on the stated residual df. Examples:
   - Model 2 pre-EPS: draft CI [-1.401, 12.555] = 5.577 +/- 1.96 x 3.560.
     Correct t(14) CI: [-2.059, 13.213]. Draft p = 0.117 (normal); correct
     t(14) p = 0.139.
   - Model 2 delta_B: draft p = 0.153 (normal); correct t(14) p = 0.175.
   - Model 2 post-BVPS: draft p = 0.139 (normal); correct t(14) p = 0.161.
   - Model 1 EPS: draft p = 0.609 (normal); correct t(16) p = 0.617.
   No baseline 5% decision changes, because all baseline coefficients are
   insignificant under either distribution. But the chapter repeatedly
   cites residual df (14, 16, 13, 10) as if the inference used them, while
   the intervals and p-values do not. Fix the pipeline to use the t
   distribution and regenerate every table and every p-value and
   interval quoted in the text. The exact fix, confirmed against
   statsmodels documentation in the second review pass, is to pass
   `use_t=True` when fitting with `cov_type="HC3"`: without it,
   statsmodels reports a z column (normal distribution); with it, it
   reports Student's t on residual df. The thesis pipeline calls
   `.fit(cov_type="HC3")` without `use_t=True`, which is why every
   interval is coefficient +/- 1.96 x SE. One argument change, plus
   regeneration, fixes the whole class of error. Do not leave a methods
   chapter that promises t(df) inference and a results chapter that
   delivers normal inference.
2. **R6 delta_B standard error, t, and p are wrong (section 4.2.6, point 4,
   and repeated in section 4.3.5).** The chapter reports delta_B = -2.611
   with "HC3 SE = 1.328, t = -1.97, p = 0.077". The SE 1.328 is the
   pre-consolidation BVPS coefficient's standard error from Table 4.6, not
   the delta_B standard error. Independently recomputed delta_B HC3 SE is
   about 1.52, giving t = -1.72, p = 0.116 on t(10) (0.085 on the normal
   approximation). Consequences:
   - The individual delta_B is not significant at 10% under the correct
     t distribution. The chapter's claim that it is (p = 0.077) must be
     deleted.
   - The joint Wald test for R6 is unaffected: F(2, 10) = 5.82, p = 0.021
     is correct. The chapter must rest its R6 claim on the joint test
     alone, not on the individual delta_B.
   - Table 4.6 itself is not wrong on this point: it reports delta values
     without delta standard errors, so a reader cannot check delta_B from
     the table. Add delta standard errors (and t/p) to Table 4.6 for every
     specification, so this class of error cannot recur silently.
3. **"Conclusively prove" and causal language (sections 4.3.5 point 1 and
   4.3 conclusion).** The chapter says R6 "conclusively prove[s] that the
   2023 consolidation wave caused a statistically significant structural
   break". Three separate problems:
   - "Caused" contradicts the thesis's own non-experimental, associational
     design, stated in Chapters 1 and 3. The design cannot identify a
     causal merger effect; year fixed effects absorb every other
     contemporaneous shock, and the interaction is a calendar-regime
     difference, not a merger treatment effect.
   - "Conclusively" contradicts the baseline result. The baseline joint test
     fails to reject at 5% (p = 0.085). A sensitivity that drops one year
     (n = 23, df = 10) and then rejects does not retroactively make the
     baseline conclusive; it makes the finding sensitivity-dependent.
   - "Prove" is the wrong verb for any single regression result, let alone
     one with df = 10.
   Rewrite to: "In the baseline, the joint test does not reject stability
   at 5% (p = 0.085). After excluding the entity-mismatch year, the joint
   test rejects at 5% (p = 0.021). The evidence for a regime shift is
   therefore suggestive in the baseline and significant only in the
   sensitivity; it is reported as an association across calendar regimes,
   not as a causal effect of mergers."
4. **Hypothesis table inconsistency (section 4.2.5, Table 4.5 and text).**
   Table 4.5 states nulls as beta_E <= 0 and beta_B <= 0 (one-sided), its
   note says "two-tailed alpha = 0.05", and the detailed text states H1 and
   H2 as beta > 0 (directional). Chapter 1 states two-tailed tests of
   beta != 0. Unify on Chapter 1: null beta = 0, two-tailed. Decisions are
   unchanged (all fail to reject at 5%), but the table as written describes
   three different tests at once. Also, H1 and H2 in Table 4.5 are evaluated
   on Model 2 pre-slopes, while Chapter 1's H1 and H2 read as baseline
   (Model 1) hypotheses. State explicitly that H1/H2 are tested on both
   Model 1 (overall slopes 2.095 and 0.219, both insignificant) and Model 2
   pre-slopes (5.577 and 0.100, both insignificant), and that the decision
   is the same either way. As written, a reader cannot tell which model
   the hypothesis belongs to.
5. **Mechanisms presented as findings (sections 4.3.1, 4.3.2, 4.3.3).**
   The discussion attributes the coefficient pattern to an NPL surge,
   provisioning burdens, goodwill recognition, unprovisioned legacy loans,
   regulatory forbearance, and capital overhang. None of those variables
   is in the dataset, and none is estimated in any table. These are
   plausible mechanisms, and they may well be true, but in this thesis
   they are interpretations, not results. Every such sentence must be
   reworded to "consistent with", "a plausible mechanism that this study
   does not test", or supported with a cited, dated source for that
   specific bank-year (for example, an NRB or annual-report NPL figure).
   In particular, the claim in section 4.3.2 that "higher reported book
   value frequently masked unamortized merger goodwill" must not stand as
   a finding without a goodwill figure for at least one bank. The negative
   post-BVPS slope (-1.658, p = 0.161 under t) is itself insignificant;
   building a four-mechanism theory on an insignificant, negative point
   estimate, and presenting it as the explanation, inverts the order of
   evidence.
6. **Prior-literature overgeneralization (section 4.3.4, point 1).** The
   chapter says prior studies' significant results are "directly explained"
   by P/E circularity and omitted year fixed effects, and that the pooled
   slope is "entirely spurious". That is too strong on two counts:
   - The thesis shows, in its own sample, that pooled EPS (4.882, SE 3.099)
     is itself not significant at 5% under HC3 inference (t about 1.58).
     Pooled estimation inflates the point estimate relative to two-way FE
     (2.095), but it does not, in this sample, manufacture significance.
     The thesis cannot therefore prove that prior studies' significance
     came from pooling alone, without re-estimating their data.
   - Not every prior study cited used P/E, and the chapter's own list
     includes studies it does not show to have used P/E (for example,
     Chaudhari 2025, whose variables are EPS, DPS, ROA, size, and macro
     factors). Restrict the circularity claim to the studies that actually
     used P/E, name them, and soften the rest to "may have been inflated
     by omitted macro-year variation, as the specification comparison in
     Table 4.8 illustrates for this sample".
   - Specific numbers that must be sourced or removed: Bhattarai 2014 as
     "14 commercial banks" (Chapter 2 gives 35 bank-years; reconcile both
     numbers in one place) and Joshi, Ghimire, and Singh 2023 BVPS
     "beta = 1.62, p < 0.01" (this review did not verify that coefficient
     from the Joshi paper; confirm it from the paper or delete the
     specific value and keep the directional summary).

## Clarify

- **"Asymptotic p-value" (section 4.2.4, point 4).** The Wald F p-value is
  from the F(2, 14) distribution under the HC3 covariance, not an asymptotic
  approximation. Call it the F-distribution p-value. This is terminology,
  but in a chapter that already has a distribution problem (item 1), it
  matters.
- **"Marginal significance at 10%" (sections 4.2.4, 4.2.5).** The thesis
  pre-specifies alpha = 0.05. Reporting p = 0.085 as "marginal at 10%" is
  acceptable as description, but it must not be upgraded in later chapters
  to evidence of a shift. Chapter 5 does upgrade it (see its review).
  Keep the 10% language descriptive and keep the 5% decision as the
  decision.
- **Figure numbering.** Text Figures 4.1 to 4.7 map to analysis assets
  F6, F1, F2, F3, F4, F5, and A2 respectively. Add a one-line crosswalk in
  the chapter introduction or in each figure note, so a reader matching
  text figures to pipeline assets does not think a figure is missing.
- **Model 1 equation (section 4.2.3).** The equation omits the intercept
  alpha that Chapter 3 includes. With reference-category dummies, the
  intercept is the GBIME/FY 2076/77 baseline. Add alpha back, or state
  that the equation is written with the intercept absorbed into the fixed
  effects. Consistency across chapters matters more than the notation
  choice.
- **Kwon and Wang divergence.** The chapter's discussion (section 4.3.3)
  says the findings "strongly resonate" with Kwon and Wang, then correctly
  notes that book value did not act as an anchor in Nepal. The resonance
  is real for earnings (declining relevance, more noise) and opposite for
  book value (declining, even negative, rather than rising). State the
  divergence in the first sentence of that discussion, not only in the
  second half, or a reader will take "strongly resonate" as the conclusion.

## Overall for this chapter

Major revision of the discussion, minor revision of the tables (once the
inference distribution is fixed and delta standard errors are added to
Table 4.6). The tables, except for p-values, intervals, and the R6 delta_B
text, are correct. The discussion, as written, claims more than the tables
support. Rewrite the discussion to the level the tables support, and this
chapter becomes the thesis's best defence, because it will have shown its
own limits before an examiner has to.
