# Supervisor review: Chapter V, Summary, Conclusion, and Implications

Draft file: `docs/draft/thesis/chapter_05_summary_and_conclusion.md`
Verdict: This chapter does not faithfully summarize Chapter 4. It upgrades
every qualified result in Chapter 4 into an unqualified conclusion, repeats
the R6 standard-error error, and adds one unverified historical claim about
SEBON. A conclusion chapter that is stronger than its results chapter is a
serious defect, because it is the chapter most examiners read first after
the abstract. It must be rewritten to match Chapter 4, not the other way round.

## Strengths

- The summary of method (section 5.2.2) is accurate: sample, price window,
  5-day rule, 13/15 split, Model 1 and Model 2 equations, df 16 and 14, HC3.
  No method number in the summary contradicts Chapter 3.
- The descriptive summary (section 5.2.3, point 1) is accurate: price
  -33.80%, EPS -40.11%, DPS -76.90% with 12 of 15 post rows at zero, BVPS
  +2.44%. These were independently recomputed and match.
- The future-research section (5.5.2) is genuinely good: longer post horizon,
  full 20-bank population with a difference-in-differences design, ESG and
  governance variables, intraday event studies, and cross-sector comparison
  are all appropriate next steps, and the DiD suggestion correctly
  identifies what the current design lacks (a comparison group that the
  year fixed effects do not already absorb).

## Must fix

1. **"Conclusively rejected" (section 5.3.1).** The chapter concludes that
   "the assumption of temporal parameter stability that underpins
   conventional valuation research in Nepal is conclusively rejected."
   That is false for the baseline model. The baseline joint test is
   F(2, 14) = 2.954, p = 0.085, which fails to reject stability at the
   thesis's own 5% threshold. The only rejection at 5% is the R6
   sensitivity (F(2, 10) = 5.82, p = 0.021), which drops one year and has
   10 residual degrees of freedom. Correct conclusion: "The baseline does
   not reject parameter stability at 5%. After excluding the
   entity-mismatch year, the joint test rejects at 5%. The evidence for a
   regime shift is therefore sensitivity-dependent, not conclusive, and
   is reported as an association across calendar regimes." Every sentence
   in section 5.3 that depends on "conclusively rejected" must be rewritten
   to this form.
2. **"Definitively resolves" and the artifact claim (section 5.3.3).** The
   chapter says the thesis "definitively resolves the methodological
   controversies" and that prior studies' significant coefficients "were
   artifacts" of P/E circularity and omitted year fixed effects. See
   Chapter 4 review, item 6, for the full reasoning. In short: the thesis
   shows, in its own sample, that pooled EPS is not significant under HC3
   inference, so it cannot prove that prior significance was manufactured
   by pooling; and not every cited prior study used P/E. Rewrite to:
   "In this sample, pooled estimation gives a larger EPS point estimate
   (4.882) than two-way fixed effects (2.095), while explaining far less
   variance (R-squared 0.136 versus 0.948), illustrating how omitted
   macro-year variation can inflate accounting slopes. Studies that also
   included P/E as a regressor face the additional, mechanical circularity
   described in Chapters 2 and 3." That is a strong, true claim. The
   current version is stronger and false.
3. **R6 delta_B error repeated (section 5.2.3, point 5).** The chapter
   repeats Chapter 4's error: delta_B = -2.611 with "t = -1.97, p = 0.077".
   Correct values: HC3 SE about 1.52, t = -1.72, p = 0.116 on t(10)
   (0.085 on the normal approximation). The individual delta_B is not
   significant at 10% under the correct t distribution. The joint Wald
   result (F = 5.82, p = 0.021, n = 23) is correct and is the only R6 result
   that should be called significant. Fix this in both chapters, and in
   the abstract if the abstract repeats it (the abstract was not part of
   this review's five chapters; check it separately).
4. **SEBON late-2022 directive revision (section 5.4.2, point 1).** The
   chapter states: "Although SEBON subsequently revised its merger
   suspension directives in late 2022 to shorten suspension durations".
   This review found no source for a late-2022 SEBON directive revision in
   the project record, in the draft chapters, or in the analysis files.
   The verified record shows suspensions and resumptions in 2022
   (NIB 30 May, HBL 6 June, GBIME resumption December 2022 for non-basic
   shareholders), but that is not evidence of a directive revision.
   Either cite the directive (number, date, and what it changed) or delete
   the historical claim. The policy recommendation that follows it
   (limit halts to a few sessions, or to three sessions in section 5.5.1)
   is a legitimate recommendation and can stand on its own, as a
   recommendation, without the historical premise. Do not let a
   recommendation borrow authority from an unverified reform.
5. **Causal language throughout sections 5.3 and 5.4.** "Consolidation
   caused", "mergers did not generate efficiency", "amalgamations created
   institutions burdened by NPLs", and similar sentences present the
   regression associations as causal and mechanistic findings. The design
   is observational, with calendar-regime interactions absorbed by year
   fixed effects. Every such sentence must be reworded to associational
   language ("post-consolidation bank-years are associated with lower
   multiples", "the post period coincides with lower EPS and zero dividends")
   unless a causal claim is supported by a source outside the regression
   (for example, a bank's own reported NPL figure for that year, cited).
   This is not pedantry: it is the difference between a defensible
   exploratory thesis and a thesis that fails its own methods chapter.

## Clarify

- **"Due to regulatory capital adequacy constraints" (section 5.2.3,
  point 1, DPS collapse).** The DPS collapse (mean 6.06 to 1.40, 12 of 15
  post rows at zero) is a fact in the data. The cause ("due to regulatory
  capital adequacy constraints") is not estimated in any model and is not
  documented year by year in the thesis. Reword to "coinciding with
  post-merger capital retention and provisioning pressures" and, if the
  author wishes to keep the regulatory cause, cite the specific NRB
  dividend or capital directives that applied in FY 2079/80-2081/82.
  The same point applies to section 5.3.2's claim that high book value
  "masked unamortized merger goodwill, capitalized restructuring costs,
  and unprovisioned legacy credit exposures": without a goodwill or
  provisioning figure, this is interpretation, and must be labelled as such.
- **"Unmerged benchmark" (section 5.2.2).** The summary calls NMB "one
  unmerged benchmark banking series" and says it "maintained continuous,
  independent corporate operations throughout the 2023 wave". That is
  correct if read as "throughout the 2023 wave", and the chapter should
  keep that qualifier attached every time, with the Kanchan 2020
  qualification in a footnote, as Chapters 2 and 3 do. Without the
  qualifier, "unmerged" overstates NMB's history.
- **Implications versus conclusions (section 5.4).** Most of section 5.4 is
  correctly framed as implications and recommendations (AQRs, disclosure
  portals, core earnings metrics, three-session halt ceiling). That framing
  is appropriate and should be preserved. The problem is only where
  section 5.4 states a mechanism as if it were a finding (see must-fix 5).
  Keep the recommendations, label the mechanisms as interpretations, and
  the section becomes defensible.
- **"VIF = 1.16, confirming empirical independence" (section 5.2.3,
  point 2).** VIF 1.16 is correct for EPS-BVPS, but EPS and BVPS correlate
  at r = 0.372 (p = 0.051), which is moderate, not independent. Reword to
  "confirming that multicollinearity between EPS and BVPS is negligible",
  which is what VIF 1.16 actually shows.
- **R-squared attribution (section 5.2.3, point 3, and section 5.3.3).**
  The chapter says accounting fundamentals explain price variation "only
  moderately, while macro-temporal trends account for the overwhelming
  majority (R-squared = 0.948)". That is a fair reading of the pooled
  (0.136) versus two-way FE (0.948) comparison, but it should be stated as
  a comparison, not as a decomposition: the thesis does not decompose
  R-squared into a fundamentals share and a year-effects share. One
  sentence of qualification ("the increase from 0.136 to 0.948 when year
  dummies are added shows how much variation the year effects absorb")
  makes the claim precise.

## Verified in this chapter

- All summary numbers for descriptives, Model 1, Model 2, joint Wald,
  robustness Wald statistics, and specification comparison match Chapter 4
  and the independent recomputation, except for the p-values/intervals
  flagged in the overall review and the R6 delta_B text flagged above.
- The future-research directions do not contradict the limitations stated
  in Chapter 1.

## Overall for this chapter

Major revision. This is the chapter that determines whether the thesis
passes as honest exploratory work or fails as overclaimed work, because
it is the chapter that states conclusions. Rewrite sections 5.3.1 and
5.3.3 to the sensitivity-dependent, associational form, fix the R6
delta_B numbers, and either source or delete the SEBON directive claim.
After those fixes, the chapter's recommendations can stand as they are.
