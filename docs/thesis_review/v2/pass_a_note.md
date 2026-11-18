# Pass A note — examiner's first look (written BEFORE reading Chapters II–IV or the appendices)

Date: 2026-11-17. Read only: `src/thesis/front/abstract.tex`,
`src/thesis/chapters/chapter_01_introduction.tex`,
`src/thesis/chapters/chapter_05_summary_and_conclusion.tex`.
This note was written before any other thesis file was opened and has not been edited afterwards.

## What I understood the thesis to be about
A master's dissertation testing whether the market value relevance of two
accounting numbers — earnings per share (EPS) and book value per share (BVPS)
— changed for Nepalese commercial banks across the 2023 banking
consolidation wave. The framework is Ohlson's (1995) residual income
valuation model. The design is a panel of five commercial bank series over
six fiscal years (FY 2076/77–2081/82), with share prices measured on or
after the statutory reporting deadline under BAFIA Section 59(2) (the
MPS^RD measure), two-way fixed effects, and HC3 robust inference. The
clean estimation sample is N = 28 bank-years after two observations were
dropped for merger-related trading suspensions.

## What it claims
- Baseline (Model 1): EPS slope 2.095 (p = 0.616) and BVPS slope 0.219
  (p = 0.908) — positive but statistically insignificant.
- Regime shift (Model 2): pre-consolidation EPS 5.577 (p = 0.140), BVPS
  0.100 (p = 0.940); implied post-consolidation slopes 2.453 (EPS) and
  -1.658 (BVPS), neither significant. The joint Wald test fails to reject
  structural stability at 5% under the pre-specified HC3 covariance
  (F(2,14) = 2.954, p = 0.085).
- The headline result is explicitly HC3-specific: the same test rejects
  under classical, HC0, HC1 and HC2. One sensitivity (R6, dropping
  FY 2078/79) rejects unadjusted (p = 0.021) but not after Holm adjustment
  (p = 0.169). The evidence for a regime shift is therefore
  sensitivity-dependent, not conclusive.
- The interpretation offered is that post-merger capital dilution coincides
  with compressed implied slopes rather than a flight to book value.
- The conclusion draws extensive policy implications (asset-quality
  reviews, trading-halt limits, centralised electronic filings) and
  recommendations for future research.

## Questions the introduction raises (to check against the body)
1. The headline "no regime shift" is HC3-specific. Does the body show the
   full sensitivity table, and is the dependence on the estimator handled
   honestly throughout (not only in the abstract)?
2. Five combinations commenced joint operations in Jan–Feb 2023, but the
   sample covers four of them plus one unmerged bank. Why is the fifth
   (Prabhu–Century) excluded? The introduction gives no reason.
3. The sample is five purposively chosen series out of 20 licensed banks.
   How far can any conclusion travel beyond these five?
4. The introduction already reports the headline estimates (EPS 2.095,
   BVPS 0.219, joint F = 2.954) before the results chapter. Is that
   front-loading appropriate, and do the numbers in Ch I match Ch IV?
5. The conclusion's policy implications are long and specific, yet the
   empirical results are null. Are the implications genuinely supported by
   the evidence, or do they overreach what a null result can carry?
6. Given null results, what exactly is the contribution — the empirical
   finding, or the methodological protocol (MPS^RD pricing window, P/E
   exclusion, HC3 discipline)? The introduction claims both; the body must
   show which one holds up.
7. The introduction says the thesis "resolves methodological limitations
   in prior Nepalese literature". That is a strong claim for a null-result
   study; the literature chapter must substantiate the prior flaws
   (P/E circularity, Ashadh-end pricing) with evidence, not assertion.
