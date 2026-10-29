# Finalized review — Chapter IV: Results and Discussion, audited against docs/instructions

**Thesis version audited:** HEAD 8c96edc (pulled 2026-10-29).
Files checked, both versions:
`docs/draft/thesis/chapter_04_results_and_discussion.md` and
`src/thesis/chapters/chapter_04_results_and_discussion.tex`,
plus the tables and figure code they describe
(`data_analysis/analysis/outputs/tables/T1–T6`, `A4–A6`,
`assets/f1_scatter_matrix.py`, `f2_correlation_heatmap.py`,
`a2_robustness_forest.py`, `f5_diagnostics.py`,
`_diagnostics_panel.py`).
**Thesis files changed to write this review: NONE.** Applying any
fix still needs the author's approval, in both versions where the
passage appears in both.

**Standard applied:** `docs/instructions/instructions_for_paper.md`
— §2 traps (especially Trap 2 R², Trap 4 small clusters,
Trap 5 df, Trap 6 asterisk econometrics, Trap 7 causal language,
Trap 8 sensitivity), §6 tables/figures/robustness
(§6.1 self-contained notes, §6.2 economic magnitudes and CIs,
§6.3 interaction mechanics, §6.4 robustness as falsification),
§7 prose rules, §10 rubric. The instructions' illustrative
numbers (§6.2, §8.2) are NOT thesis numbers and were not used
as a check standard here.

## How this chapter was checked, so it can be re-checked

1. Read Chapter IV in full, both versions, Results (§4.2)
   and Discussion (§4.3).
2. Re-checked every Phase 2 Chapter IV must-fix and minor
   against the 8c96edc text — all must-fix items are now
   fixed (see Passes).
3. Checked chapter claims against tables/code where the
   chapter names them: Table 4.1 percentages recomputed
   from Table 4.1 cells; Table 4.2 p-values checked against
   r and n = 28; Model 1/2, hypothesis, R1–R8, diagnostics,
   and specification-comparison tables checked against
   T3/T4/T5/T6/A5 and against the Phase 2 loop's independent
   recomputation record; figure notes checked against
   generation code (not rendered PDFs — see Scope limits).
4. Grep-verified prohibited vocabulary and the HC3/figure
   passages in both versions.
5. Anything not verified in this step is listed under
   "NOT verified — not counted as errors", not under
   Must-fix.

## Verdict for Chapter IV

**No must-fix found in this chapter step.** That is a
deliberate verdict, not an oversight: every Phase 2 Chapter IV
must-fix (four figure notes, causal language, HC3 verb,
"Controlled via HC3", Table 4.1 note) is verified fixed in
the 8c96edc text, and no new number, model, or causal error
was found in this step. What remains is a set of minors —
wording precision, one figure title, one notation slip, and
one uncomputed VIF range — listed below. Chapter IV's
numbers, hypothesis decisions, and R6 sensitivity framing
are correct as written and must not be "fixed".

## Must-fix

None. (See Minors and Passes.)

## Minor (verified, fix with the next edit batch)

### M1. Figure 4.6 title says R1–R8; the plot, note, and code say seven specifications
- Title in §4.2.6: "Figure 4.6: Robustness Forest Plot
  Across Specifications R1–R8 (Codebase Asset A2)".
- Note directly below it (correct): "across seven
  specifications (R1, R2, R4–R8; R3 omitted because ROA
  is on a different scale; $N = 28$ or $N = 23$)".
- Code verified: `a2_robustness_forest.py`,
  `EPS_RUN_IDS = ("R1", "R2", "R4", "R5", "R6", "R7", "R8")`
  — seven specs, EPS channel only, R3 excluded for scale.
- Fix: change the title to "Across Seven Specifications
  (R1, R2, R4–R8)". The note and the plot are already
  right; only the title contradicts them.

### M2. Chaitra as "statutory" without the word "operationalized" in three Chapter IV spots
- Table 4.1 note: "within the 5-day trading window
  following the statutory annual reporting deadline
  (end of Chaitra / mid-April)".
- §4.3.4: "the post-reporting-deadline statutory window
  under Section 59(2) of BAFIA (end of Chaitra / mid-April)".
- §4.3.5, point 3: "the nine-month statutory reporting
  deadline under Section 59(2) of BAFIA (end of Chaitra /
  mid-April)".
- The statute names nine months into the subsequent year,
  not Chaitra; Chapter III's correct template is
  "statutory nine-month deadline, operationalized at the
  end of Chaitra". Fix: insert "operationalized at" before
  "end of Chaitra" in each spot (or cross-refer to
  Chapter III's operationalization). Not a must-fix,
  because §4.3.5 also states "nine-month" and Chapter III
  defines the operationalization, so a cross-chapter reader
  can resolve it — but the instructions demand exactness
  on this exact point, and the template exists.

### M3. EPS–ROA VIF range "20.2 to 30.0" is uncomputed, and inconsistent across the thesis
- §4.2.2, point 2: "severe variance inflation
  ($\text{VIF} \approx 1 / (1 - 0.975^2) \approx 20.2$ to
  $30.0$ when other covariates are included)".
- Verified: bivariate VIF from $r = 0.975$ is 20.25
  (20.2 rounded) — exact. The "to 30.0" upper bound
  appears in NO output: diagnostics code computes VIF on
  substantive regressors only, FE dummies excluded, and
  T6 reports 1.16 for EPS/BVPS only. Chapter III says
  "≈ 20.3, rising to approximately 30 when conditioning
  on fixed effects"; T2's note says "variance inflation
  ~ 30" with no qualifier. Three versions of one claim,
  none computed.
- Fix (one sentence, in all three places): either compute
  the FE-conditioned EPS–ROA VIF and cite the output, or
  delete the 30 figure everywhere and keep the exact
  bivariate 20.3/20.2, which alone justifies never
  co-including EPS and ROA. No estimate depends on the
  30 figure, so this is a minor, not a must-fix.
  (Carried from Chapter III, Minor M3.)

### M4. Post-absorption equation in §4.2.4 uses parameters where dummies belong
- §4.2.4: "the stand-alone indicator $Post_t$ is an exact
  linear combination of the fiscal-year dummies
  ($\sum_{t \in Post} \lambda_t = Post_t$)".
- $\lambda_t$ are the fiscal-year fixed-effect PARAMETERS,
  not the dummy indicators. The correct equation, as
  Chapter III §3.6.2 states it, is
  $\mathit{Post}_t = D_{2079/80} + D_{2080/81} + D_{2081/82}$.
- Fix: replace the parenthetical with Chapter III's
  equation. The surrounding sentence ("exact linear
  combination of the fiscal-year dummies ... perfectly
  absorbed ... cannot be separately estimated") is
  correct; only the equation's symbols are wrong.

### M5. Table 4.6 note gives df for only three of eight specifications
- Table 4.6 note states df for R4 (13) and R5/R6 (10),
  but not for R1 (16) or R2/R3/R7/R8 (14), although
  §6.1 requires tables to be self-contained (N, estimator,
  SE type, df). Fix: add one sentence to the Table 4.6
  note: "Residual df: R1 16; R2, R3, R7, R8 14; R4 13;
  R5, R6 10." All df values are already stated in
  Chapter III; this is a note-completeness fix only.

### M6. "Eight-part robustness suite" naming (cross-reference to Chapter III, Minor M1)
- §4.1, point 6, and §4.2.6 intro call R1–R8 an
  "eight-part robustness suite". R1 is Model 1 baseline
  and R2 is Model 2 baseline; the robustness variants
  are R3–R8 (six), matching instructions §6.4.
  Fix in step with Chapter III: "eight-specification
  suite (R1–R2 baselines plus six robustness variants
  R3–R8)". All n and df in Table 4.6 are correct —
  naming only.

### M7. §4.3.2 mechanism 1's factual premise has no cited source
- Mechanism 1: "Contemporaneous industry reports and NRB
  supervisory data indicate that following consolidation,
  commercial banks experienced rising non-performing
  loans, driven by broad macroeconomic deceleration,
  construction sector stress, and stricter loan-loss
  provisioning requirements."
- No specific report or NRB publication is cited for the
  rising-NPL / construction-stress premise, although the
  paragraph is correctly framed as a "Plausible Mechanism"
  and correctly disclaims: "direct asset quality variables
  are not estimated in the econometric model", and the
  section intro states the patterns are "not as proven
  causal effects, but as suggestive structural tendencies".
- Fix: add one citation (NRB report / industry source with
  year) for the NPL premise, or soften the premise to
  "may have experienced". Not a must-fix, because the
  mechanism is explicitly non-estimated and the chapter
  does not present it as a result.

## Passes — verified compliances, including Phase 2 items now fixed (do NOT re-open)

- **Figure notes, all four Phase 2 errors: FIXED, verified
  against code.**
  - F1 / Figure 4.2 note now: "Pairwise scatter plots
    and univariate kernel density distributions for
    $MPS^{RD}$, EPS, and BVPS ($N = 28$)" — 3 variables,
    scatter + KDE, no fit-line claim. Correct.
  - F2 / Figure 4.3 note now: "Correlation heatmap
    displaying pairwise Pearson correlation coefficients"
    — no asterisk claim. Code verified:
    `f2_correlation_heatmap.py`, `annot=True, fmt=".2f"`
    — values only. Correct.
  - A2 / Figure 4.6 note: seven specs, R3 omitted for
    scale — correct (title is Minor M1 only).
  - F5 / Figure 4.7 note now: "(top-left) Normal Q-Q;
    (top-right) Residuals vs. Fitted; (bottom-left)
    Scale-Location; (bottom-right) Cook's distance" —
    matches `_diagnostics_panel.py` panel order
    (Q-Q, Residuals vs fitted, Scale-location, Cook's).
    Correct.
  - F3 / Figure 4.4 note (Phase 2 model): "Lines are
    descriptive bivariate OLS fits, not the two-way
    fixed-effects estimates in Table 4.4; the post-BVPS
    sign difference is the effect of absorbing year
    effects" — correct and the right warning.
  - F4 / Figure 4.5 note: Model 2 slopes, shifts, and
    implied post slopes with HC3 95% CIs on $t(14)$ —
    matches Table 4.4. Correct.
  - F6 / Figure 4.1 note: post shading, open markers for
    excluded HBL/NIMB FY 2077/78, and the honest
    disclosure that "connecting lines pass continuously
    through the excluded periods" — correct.
- **Causal language, Phase 2 items: FIXED.**
  - §4.2.1 descriptive explanations now use consistency
    language throughout: price compression "is consistent
    with broader macroeconomic tightening"; EPS dispersion
    "is consistent with post-merger integration dynamics"
    and "coincided with substantial earnings volatility";
    BVPS stability "is compatible with the accumulation
    of statutory reserves"; DPS contraction "coinciding
    with heightened regulatory capital conservation".
    No unlabelled causal explanation remains in Results.
  - §4.2.5, point 5: joint marginal significance "is
    consistent with non-trivial joint adjustments" —
    the old "induced" is gone.
  - §4.3.2 intro: patterns "interpreted not as proven
    causal effects, but as suggestive structural tendencies
    consistent with several economic and institutional
    mechanisms" — the correct framing, kept as the model.
  - §4.3.5, R6: "reported as an empirical association
    across calendar regimes, rather than as a causal
    merger effect" — correct.
- **HC3 verb in Chapter IV: FIXED.** §4.2.7, point 3:
  "the HC3 estimator divides squared residuals by
  $(1 - h_{ii})^2$, inflating high-leverage residuals to
  offset their artificially small OLS residuals."
  Formula and verb agree. Table 4.7's "Addressed via
  HC3 robust covariance estimation" (with the text's
  "without artificially trimming or modifying observed
  sample data") is acceptable: HC3 adjusts inference for
  leverage, it does not remove influence, and the chapter
  says so.
- **Table 4.1 note, aggregator wording: FIXED.** Note now
  ends: "Data recompiled from published annual reports
  and cross-checked aggregator market closing series."
  The old "verified market closing series" overclaim is
  gone.
- **Suspension wording in Chapter IV: PASS.** §4.2.1:
  "suspended during merger-related processes around the
  statutory reporting deadline (end of Chaitra 2078 BS /
  mid-April 2022), with trading resuming 54 days late ...
  and 47 days late". This is "merger-related", not
  "during merger negotiations" — the precise timeline
  (MoU, January 2022 rejection, April–June 2022 suspension
  and resumption) is in Chapter III §3.3.4, and Chapter IV's
  summary does not contradict it. §4.3.5, point 2,
  "suspended across extended merger processes" is the
  same approved form.
- **Numbers: PASS (chapter-vs.-table agreement in this
  step; independent recomputation in the Phase 2 loop).**
  - Table 4.1 percentages recomputed from Table 4.1
    cells in this step: price −33.80%, price SD −72.00%,
    EPS −40.11%, EPS SD +63.66%, BVPS +2.44%, DPS −76.90%,
    ROA −46.56% — all exact. DPS pre 13/13 positive,
    post 12/15 zero — exact.
  - Table 4.2: EPS–BVPS $r = 0.372, p = 0.051$;
    MPS–EPS $r = 0.358, p = 0.061$; MPS–BVPS
    $r = 0.217, p = 0.268$; ROA $r = 0.378, p = 0.047$;
    DPS $r = 0.082, p = 0.678$; EPS–ROA $r = 0.975$ —
    consistent with $n = 28$; Phase 2 loop recomputed
    all Table 4.2 correlations/stars exactly.
  - Tables 4.3/4.4: Model 1 (EPS 2.095, SE 4.096,
    $p = 0.616$; BVPS 0.219, SE 1.858, $p = 0.908$;
    $R^2$ 0.948, adj 0.912, df 16) and Model 2 (pre EPS
    5.577, pre BVPS 0.100, $\delta_E$ −3.124,
    $\delta_B$ −1.758, post EPS 2.453, post BVPS −1.658,
    joint Wald $F(2,14) = 2.954, p = 0.085$) — match
    T3/T4 and the loop recomputation exactly.
  - Table 4.5 hypothesis decisions: all four hypotheses
    "Fail to Reject $H_0$" at 5% in both Model 1 and
    Model 2 readings, joint test "Fail to Reject at 5%
    (Marginal at 10%)" — correct against Tables 4.3/4.4.
  - Table 4.6 / T5: R1–R8 coefficients, SEs, joint Wald
    values, and n (28 / 23) match T5, including R6
    $F(2,10) = 5.82, p = 0.021$, $\delta_B$ −2.611
    (SE 1.517, $t = -1.72, p = 0.116$).
  - Table 4.7 / T6: VIF 1.16 / 1.16, tolerance 0.862;
    Breusch-Pagan LM 14.37, $\chi^2(11) = 19.68$,
    $p = 0.213$; Cook's max 0.552 (HBL FY 2076/77),
    5 observations exceed $4/28 = 0.143$ — exact
    chapter-vs.-T6 agreement.
  - Table 4.8 / A5: pooled ($\beta_E$ 4.882, SE 3.099,
    $t = 1.58, p = 0.126$, $R^2$ 0.136, df 25), bank-FE-only
    (5.217, 1.432, $R^2$ 0.176, df 21), two-way
    (2.095, 0.219, $R^2$ 0.948, df 16) — df arithmetic
    (28−3, 28−7, 28−12) and the $R^2$ warning in §4.2.3
    ("almost entirely driven by the two-way fixed effects
    structure") satisfy Trap 2: no $R^2$ claim is made
    for the slopes.
- **Instructions §6: PASS.** §6.1: Tables 4.3/4.4/4.5
  notes give dependent variable, estimator, HC3, $t$
  df, two-tailed 5% rule, and parameter counts;
  Table 4.6 note gives HC3, R4/R5/R6 df, and the
  asterisk definition (Table 4.6 df completeness is
  Minor M5 only). §6.2: Results narrate economic
  magnitudes with CIs (e.g., EPS "NPR 2.10 per NPR 1.00
  of EPS", pre-EPS "5.58 times EPS"), not cell recitals.
  §6.3: β, δ, β+δ mechanics stated in §4.2.4 and Table 4.4.
  §6.4: robustness presented as falsification — R6
  changes the joint decision and the chapter says so
  plainly, without claiming baseline stability is
  "verified" (that overclaim lives in Chapter V, for
  its step).
- **Prose, §7.1/§7.2: PASS.** Grep: delve 0, pivotal 0,
  testament 0, beacon 0, tapestry 0, paramount 0,
  "game changer" 0, multifaceted 0, myriad 0,
  "it is important to note that" 0, utilize 0,
  facilitate 0. No prohibited word in Chapter IV.
- **Figure mapping in §4.1: PASS.** Figure 4.1→F6,
  4.2→F1, 4.3→F2, 4.4→F3, 4.5→F4, 4.6→A2, 4.7→F5 —
  matches the codebase assets.

## NOT verified in this step — not counted as errors

- **Diagnostics independent recomputation:** Table 4.7
  values were checked for chapter-vs.-T6 agreement in
  this step, not independently recomputed (the Phase 2
  loop also recorded chapter-vs.-T6 agreement only for
  diagnostics, because statsmodels/scipy were unavailable
  in that session; the same applies here — this VM's
  system Python has no statsmodels). Models, R1–R8,
  descriptives, and correlations WERE independently
  recomputed in the Phase 2 loop.
- **Rendered figures:** figure notes were checked against
  generation code, not against rendered PDFs/PNGs, in
  this step (the Phase 2 loop viewed rendered figures
  and found no number error).
- **Literature comparisons in §4.3.4:** Chaudhari (2025)
  "without P/E circularity", Pant (2024) negative BVPS,
  Timalsina (2026) "decoupled ... following the post-2023
  liquidity contraction", Almumani (2014) / Malhotra &
  Tandon (2013) emerging-market context — summarized
  from Chapter II's reviews, not re-verified against
  full texts in this step (except Bhattarai and
  Gurung & Dahal, verified in earlier steps).
- **Mechanism facts in §4.3.2 (points 2–4):** share-supply
  dilution, dividend-signal loss, and book-equity-as-
  stressed-assets are interpretations explicitly framed
  as suggestive, not estimated effects; their factual
  premises (bonus/share counts, DPS zeros, merger
  accounting) are panel-verified, but the interpretive
  link to pricing is, by the chapter's own disclaimer,
  not a tested result.
- **"Severe post-2021 NEPSE market correction" (§4.3.4):**
  used as background for the pooled-vs.-FE comparison;
  the price-level drop in the panel itself (mean MPS
  310.59 → 205.60) is verified, but the market-wide
  correction claim was not independently sourced here.

## Scope limits of this Chapter IV review

- No thesis, table, figure, code, or data file was changed.
- No compiled PDF was proofread; TU FOM formatting (§9)
  is not certified here.
- Next step, in the author's order: Chapter V, against
  the same instructions, starting with §8.1 (RQ answers
  by name), §8.2 (hypothesis decision table, joint Wald,
  R6 exception), §8.3 (exactly three implication domains),
  and the Phase 2 Chapter V items ("verified parameter
  stability", "during merger processes", "universally",
  "dispersed dissemination", H1–H4 by name).
