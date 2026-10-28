# Supervisor re-review: commit 57c78a0 (after the first-pass reviews)

Scope of this re-review: the Markdown draft chapters in `docs/draft/thesis/`
and the regenerated analysis tables T3, T4, and T5, as pulled at
57c78a0 ("feat: add thesis analysis assets, figures, tables, and chapter
drafts"). The five new LaTeX chapters in `src/thesis/chapters/` were NOT
reviewed in this pass; before submission, they must be checked for sync
with the Markdown chapters, because a conversion step can reintroduce
wording the Markdown revision removed.

Verdict: the revision fixes every must-fix item from the first-pass
reviews. The thesis is no longer submission-blocking on the items listed
below. What remains is minor wording and the carried-forward
confirm-from-PDF items. This is a genuine improvement, not a cosmetic one:
the pipeline change, the R6 correction, and the conclusion rewrites are
all verifiable in the new files.

## Fixed, verified in the new files

1. **t-based inference (was must-fix 1).** `data_analysis/analysis/stats/models.py`
   now fits with `cov_type="HC3", use_t=True`, exactly the fix the
   first-pass reviews prescribed. Regenerated tables match the
   first-pass corrected values: Model 1 EPS 2.095 (SE 4.096, CI
   [-6.587, 10.777], p = 0.616); Model 2 pre-EPS 5.577 (SE 3.560, CI
   [-2.059, 13.213], p = 0.140), pre-BVPS 0.100 (SE 1.306, CI
   [-2.700, 2.901], p = 0.940), delta_E -3.124 (SE 4.003, p = 0.448),
   delta_B -1.758 (SE 1.231, p = 0.175), post-EPS 2.453 (p = 0.298),
   post-BVPS -1.658 (p = 0.161); joint Wald F(2, 14) = 2.954, p = 0.085.
   Small third-decimal differences from the first-pass recomputation
   (for example 0.616 versus 0.617, 0.140 versus 0.139) are rounding from
   the printed two-decimal t values, not errors: recomputing from the
   unrounded coefficients reproduces the tables. Chapter 4's text now
   states "Student's t distribution" and "t(14)" where it previously
   implied normal inference.
2. **R6 delta_B (was must-fix 2).** Table 4.6 and Table T5 now report
   delta_B = -2.611 with HC3 SE = 1.517, exactly the first-pass
   recomputed value. Chapter 4 section 4.2.6 point 4 and Chapter 5
   section 5.2.3 point 5 now state t = -1.72, p = 0.116 on t(10), that
   neither individual interaction is significant at 10%, and that the
   R6 claim rests on the joint Wald test (F = 5.82, p = 0.021) alone.
   The wrong SE (1.328) and the wrong p (0.077) are gone from both
   chapters. Table T5 now reports delta standard errors for every
   specification, so this class of copying error is now checkable.
3. **Price-source attribution (was must-fix 3 and 4).** Chapter 3
   section 3.4.3 step 3 now states, correctly: dataset (ShareSansar)
   437.00, Merolagani LTP 436.00, retained on ShareSansar's full daily
   record (open 432, high 439, low 428, close 437.00), with the explicit
   statement that this is not independent verification because
   ShareSansar is the dataset's primary source, and that the official
   NEPSE close for 13 April 2021 remains unverified. Table 3.1's note
   now states the same: "official NEPSE floor trading archives were not
   independently verified, and NEPSE official closes remain unverified
   against exchange source records." The reversed sources and the false
   NEPSE claim are gone.
4. **Conclusions and causality (was must-fix 5).** Chapter 4 section
   4.3.5 and Chapter 5 section 5.3.1 now state, in matching words, that
   the baseline joint test does not reject stability at 5%
   (p = 0.085), that the R6 sensitivity rejects (p = 0.021), and that
   the evidence for a regime shift is "sensitivity-dependent rather
   than conclusive in the baseline" and "reported as an empirical
   association across calendar regimes, rather than as a causal merger
   effect." The words "conclusively rejected", "conclusively prove",
   and "caused a statistically significant structural break" no longer
   appear in Chapters 4 or 5. Chapter 5's "definitively resolves" claim
   is likewise gone.
5. **Hypothesis framing (was must-fix 6).** Chapter 4 Table 4.5 now
   states nulls as delta = 0 (and beta = 0 for the slopes), two-tailed
   at alpha = 0.05, with Model 1 and Model 2 decisions reported
   separately. The one-sided nulls and directional hypotheses from the
   first draft are gone.
6. **Stata/SPSS and "zero transcription error" (was must-fix 7 and 8).**
   Neither claim appears anywhere in the revised Chapter 3. The methods
   chapter now stands on the Python pipeline alone, which matches the
   artefacts in the repository.
7. **"Tripartite" (was must-fix 9).** Chapter 3 section 3.3.4 now
   describes a "merger-related suspension following the rejection of
   its proposed bilateral merger with Nepal Investment Bank at its
   29th AGM in January 2022", with resumption 6 June 2022 and a 54-day
   delay. "Tripartite" and "during merger negotiations" for the
   April-June 2022 window are gone.
8. **Ohlson derivation (was must-fix 10).** Chapter 2 now derives, with
   correct algebra: P_t = BV_t + alpha_1 x abnormal earnings + alpha_2
   x v_t, alpha_1 = omega / (R_f - omega); abnormal earnings =
   (1 + r) x NI_t - r x BV_t - r x D_t (via clean surplus); and
   P_t = (1 - k) x BV_t + k x (phi x NI_t - D_t) + alpha_2 x v_t, with
   k = r x alpha_1 and phi = R_f / r. This matches the corrected
   derivation in the second-pass review (06_methods_upgrades.md,
   section A.2). The empirical equation is unchanged, which is correct:
   it was always the standard specification; only its derivation was
   wrong.
9. **BAFIA wording and quotation (was must-fix, Chapter 2).** Chapter 2
   now distinguishes the two duties in Section 59(2): submission to
   NRB within three months with public details, and audited publication
   within nine months into the subsequent fiscal year. It then counts
   Shrawan through Chaitra to end-of-Chaitra and calls that counting
   the study's "institutional operationalization", not the statute's
   wording. The inaccurate block quotation and the "terminates exactly
   at end-of-Chaitra" wording are gone.
10. **SEBON directive claim (was must-fix, Chapter 5).** The claim that
    SEBON "subsequently revised its merger suspension directives in
    late 2022" is gone. Section 5.4.2 now makes the trading-continuity
    recommendation on its own, as a recommendation, without the
    unverified historical premise. The three-session / few-session halt
    recommendation is unaffected.
11. **Mechanisms as findings (was must-fix, Chapter 4).** Section 4.3.2
    now opens with the explicit umbrella: patterns "are interpreted not
    as proven causal effects, but as suggestive structural tendencies",
    mechanism 1 is headed "Plausible Mechanism" and states that "direct
    asset quality variables are not estimated in the econometric
    model", and the negative book-value point estimate is explicitly
    called an "exploratory point estimate" that "cannot therefore be
    presented as an established empirical law". This is the framing the
    first-pass review asked for.
12. **Chapter 1 consistency items.** The NMB-Kanchan acquisition
    (August 2020, about NPR 0.57 billion) is now stated in Chapter 1
    alongside the 2023-wave benchmark claim, and "open-source dataset"
    has been replaced by "documented, reproducible dataset and
    analytical codebase". The Adhikari 46.01% figure and the Joshi
    beta = 1.62 figure, which the first pass flagged as unverified,
    no longer appear in the revised chapters; they are treated here as
    resolved by removal, not by verification.

## Still open, minor (none submission-blocking on its own)

- **"This proves that..." (Chapter 4, specification comparison).** The
  pooled-versus-two-way-FE paragraph still says the comparison "proves
  that in unadjusted pooled regressions, accounting fundamentals can
  easily absorb broader macroeconomic cycles". The next sentence
  correctly notes pooled EPS is itself insignificant (t = 1.58,
  p = 0.126), which limits the claim, but "proves" should still be
  replaced with "shows". One word.
- **"Unmerged benchmark" without qualifier (Chapter 1, scope section).**
  Chapter 1's main text now qualifies NMB correctly, but the scope
  section still says "an unmerged benchmark" with no qualifier. Add
  "(in the 2023 wave)" for consistency with Chapters 2 and 3.
- **BAFIA lettering (Chapter 2).** The revised chapter labels the two
  duties "Section 59(2)(a)" and "Section 59(2)(b)". The statute's
  subsection (2) states two duties in two sentences; it does not letter
  them (a) and (b). Either drop the letters or write "the two duties
  stated in subsection (2)". Substance is correct; citation form is
  slightly over-precise.
- **Chapter 5 BAFIA shorthand.** Section 5.4.2 still says banks are
  "legally mandated to publish audited financial statements within
  nine months of fiscal year-end". That date is substantively the same
  (nine months after fiscal year-end is Chaitra-end), but for
  consistency use Chapter 2's precise wording: "within nine months
  into the subsequent fiscal year".
- **Carried forward, not re-checked in this pass.** The Timalsina 2026
  sample (13 banks, 169 observations) and the Bhandari et al. 2026
  wording were flagged in the first pass as confirm-from-PDF; they
  were not re-checked here. The new LaTeX chapters were not reviewed
  here at all (see scope note above). Neither item should be treated
  as verified by this re-review.

## Overall for the revision

The revision is honest work. It did not merely soften adjectives: it
changed the pipeline, regenerated the tables, corrected a standard
error, and rewrote the conclusions to match the baseline test. A
supervisor reading the revised Chapters 3, 4, and 5 will find the
claims the tables support, and will find the limits stated before they
have to ask for them. Fix the four minor wording items above, sync-check
the LaTeX chapters against the Markdown chapters, and this draft is in
a defensible state for supervisor submission, subject to the supervisor
still ruling on the aggregator-price definition, which no revision of
wording can settle.
