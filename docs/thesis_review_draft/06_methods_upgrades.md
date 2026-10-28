# Supervisor review, second pass: methods and process upgrades

This file does two things the first-pass reviews did not: (1) it records
what the second, online-checked pass changed or confirmed in the first-pass
reviews, so the author can see that the reviews themselves were audited;
and (2) it proposes excellent, creative methods and processes that would
strengthen this thesis beyond merely fixing its errors. Nothing in this
file changes `docs/draft/thesis/`. It is a review and a proposal, not a
rewrite. Items marked "do" are recommended for this thesis. Items marked
"do not" are traps that look excellent and would weaken it.

## A. Second-pass audit of the first-pass reviews: what changed, what held

1. **HC3 p-values: confirmed, and the fix is now exact.** The first pass
   said the tables use the normal distribution. The second pass confirmed
   the mechanism from statsmodels documentation: fitting with
   `cov_type="HC3"` without `use_t=True` reports a z column (normal);
   with `use_t=True` it reports Student's t on residual df. The thesis
   pipeline (`data_analysis/analysis/stats/models.py`, `_fit`) calls
   `.fit(cov_type="HC3")` with no `use_t` argument. The fix is therefore
   one argument, `use_t=True`, plus regeneration of every table and every
   p-value and interval quoted in the text. The first-pass reviews have
   been updated with this exact fix. No first-pass p-value correction was
   found to be wrong in the second pass.
2. **Ohlson derivation: confirmed, and now corrected in full.** The first
   pass said the draft's beta formulas were not a valid exact derivation.
   The second pass derived the correct form from the Ohlson price equation
   P_t = BV_t + alpha_1 x abnormal earnings_t + alpha_2 x v_t, with
   alpha_1 = omega / (R_f - omega), R_f = 1 + r, and clean surplus
   BV_t = BV_{t-1} + EPS_t - DPS_t. The correct weighted-average form is
   P_t = (1 - k) x BV_t + k x (phi x EPS_t - DPS_t) + alpha_2 x v_t, with
   k = r x omega / (R_f - omega) and phi = R_f / r. Hence the EPS
   coefficient is omega x (1 + r) / (R_f - omega) and the BVPS coefficient
   is 1 - r x omega / (R_f - omega). The draft's beta_1 is alpha_1 itself
   and its beta_2 matches neither coefficient. Chapter 2's review has been
   updated with these formulas. The empirical equation itself
   (P = alpha_0 + alpha_1 x BV + alpha_2 x EPS + error, EPS as a proxy for
   abnormal earnings, other information in the error term) is the standard
   value-relevance specification in the literature and does not need to
   change; only its claimed exact derivation does.
3. **BAFIA quotation: upgraded from "check the quote" to "replace the
   quote".** The first pass flagged the Chaitra wording and said to check
   the quotation. The second pass checked Section 59 of BAFIA 2073 against
   the Law Commission / kaanun.app text. Section 59(2) imposes two duties:
   submit the balance sheet and profit and loss account to NRB within
   three months of fiscal year-end, with details published for the public
   within that period as prescribed by NRB; and publish the audited
   balance sheet and profit and loss account within nine months of the
   next fiscal year, in the prescribed format. The draft's block quotation
   ("within nine months of the completion of each financial year ...
   after obtaining the approval of the Rastra Bank") matches neither
   clause and must be replaced with the actual text or turned into an
   unquoted paraphrase. Chapter 2's review has been updated accordingly.
   The end-of-Chaitra operationalization still follows from the second
   duty (nine months into the next fiscal year, Shrawan to Chaitra, ends
   at Chaitra-end), but it is the thesis's counting, not the statute's
   wording. The thesis should also distinguish the 3-month unaudited duty
   from the 9-month audited duty, because a reader who knows the 3-month
   clause will otherwise think the thesis chose the wrong deadline.
4. **HBL-NIB "tripartite": confirmed wrong, and sharpened.** The first pass
   said the negotiation was bilateral. The second pass confirmed, from
   contemporaneous reporting: MoU signed 13 May 2021, rejected at HBL's
   29th AGM on 14 January 2022 (75% required, about 42% against, including
   the Employees Provident Fund, after a due-diligence dispute: DDA swap
   1:1 versus EPF's independent 1:0.78). Chapter 3's review has been
   updated with those dates and with a further point: because the merger
   was already rejected in January 2022, describing the April-June 2022
   suspension as "during merger negotiations" is misleading. Use
   "merger-related suspension". A contemporaneous digest notes that
   NRB's Merger Bylaw 2011 allows dividend, branch, and share-transaction
   restrictions for banks that fail to unify after an MoU; that is a
   plausible mechanism for a post-rejection suspension, not a proven cause
   for HBL/NIB, and must not be stated as the cause without a specific
   NRB order.
5. **No other first-pass error was found.** In particular: the Cook's
   distance correction (maximum 0.552, 5 observations above 0.143, once
   the parameter count is correctly 12) was already recorded as the
   reviewer's own earlier arithmetic error in the Chapter 4 review, and it
   stands. The R6 delta_B correction (SE about 1.52, t = -1.72,
   p = 0.116 on t(10)) was re-derived from the same HC3 code path that
   reproduces every published standard error in Tables 4.3, 4.4, and 4.6
   exactly, so it is not an artefact of a different estimator. The
   Gurung and Dahal, Giri, Kwon and Wang, and Timalsina literature checks
   were not contradicted by the second pass.

## B. Excellent methods to add (creative, but disciplined)

### 1. An inference ladder, not a single standard error (do)

Headline: HC3 with `use_t=True` on residual df, exactly as the thesis
promises. Sensitivity 1: jackknife / leave-one-out, which is already
implicit in HC3 (HC3 is a jackknife estimator: it weights each squared
residual by 1/(1 - h_ii)^2, i.e. by its leave-one-out prediction error).
Make that implicit property explicit: report leave-one-bank-out and
leave-one-year-out Model 2 estimates in a small table. The thesis already
knows the most important leave-one-out result and does not report it as
such: dropping NMB (the only 2023-unmerged series) collapses precision.
Reporting it, rather than discovering it in the viva, turns a weakness
into a transparency strength. Sensitivity 2: wild cluster bootstrap-t
(see item 2). Report all three on the same joint Wald test, and let the
reader see whether the conclusion survives the ladder. If it does not,
say so; that is the point of a ladder.

### 2. Wild cluster bootstrap, with its G = 5 caveat stated (do, carefully)

Cameron, Gelbach, and Miller (2008) showed the wild cluster bootstrap-t
can behave well with as few as five clusters, and it is the standard
answer to "cluster-robust fails with few clusters". It is therefore the
right sensitivity for a thesis with G = 5 banks. But do not present it
as a cure. With G = 5 and Rademacher (two-point) weights, there are only
2^5 = 32 unique bootstrap resamples, so bootstrap p-values are coarse
and 999 draws are 999 draws from 32 possibilities. If the thesis adds a
wild bootstrap, it should use Webb (six-point) weights, which give many
more unique resamples, impose the null when forming bootstrap residuals
(as Cameron et al. recommend), and report the number of unique resamples
alongside the p-value. A wild-bootstrap p-value reported without that
caveat is less honest than the HC3-t p-value it is meant to check.

### 3. A pre-registered sensitivity hierarchy and a multiple-testing note (do)

The thesis has eight robustness specifications, and one of them (R6)
rejects at 5% while the baseline does not. That pattern is exactly what
multiple testing produces by chance: with eight specifications, one
rejection at 5% is not, by itself, surprising under the null. The thesis
should therefore rank its specifications before looking at their
p-values: baseline (Model 2) as the pre-committed headline; R5 and R6 as
pre-committed institutional sensitivities (transition year, entity
mismatch) with a stated reason for each; R3, R4, R7, R8 as definitional
sensitivities. Then report, in one paragraph, how many of the eight
joint tests reject at 5% (one: R6), at 10% (baseline and R8 are near it),
and what that pattern implies. This does not weaken R6; it protects it,
because a reader who sees the hierarchy will trust R6 more than a reader
who suspects it was chosen because it was the one that worked.

### 4. A justified specification curve (do, narrowly)

A specification curve plots the estimate (here delta_E, delta_B, and the
joint Wald p-value) across every defensible specification, sorted by
effect size, instead of reporting one chosen specification. For this
thesis, the defensible dimensions are small and theory-driven, which is
the right size for a curve: fixed-effects structure (pooled, bank-only,
two-way); price window (first trading day, 3-day, 5-day freshness);
EPS (own-current, restated); BVPS (recomputed, printed NAV); DPS
(included, excluded); year exclusions (none, transition year,
entity-mismatch year). That is a few dozen specifications, not billions,
and each one is defensible. Report the curve, the median estimate, and
the share of specifications in which the joint test rejects at 5%.
Do not do the opposite: an indiscriminate multiverse that varies
everything at once, including indefensible choices (for example,
including P/E, or imputing missing prices), and then averages over it.
The recent literature is explicit that an unjustified multiverse
"drowns valid models in misspecified ones" and erodes trust. The curve
is excellent only when its dimensions are justified in advance.

### 5. A placebo / permutation test for the calendar regime (do)

Because Post is a calendar indicator absorbed by year fixed effects,
the joint Wald test's null distribution is not obviously the F
distribution in a sample of 28 with 14 parameters. A permutation test
gives the thesis a second, assumption-light p-value: randomly reassign
the Post labels across fiscal years (or randomly reassign merger timing
across banks), re-estimate Model 2, and record the joint Wald statistic
each time. The share of permutations with a Wald statistic at least as
large as the observed 2.954 (baseline) or 5.82 (R6 sample) is a
permutation p-value that does not rely on asymptotic normality or on
the t distribution. If the permutation p-value agrees with the F
p-value, the thesis gains credibility for free. If it disagrees, the
thesis has learned something important about its own identification.
Either outcome belongs in the thesis.

### 6. A returns / scale sensitivity (do, as robustness only)

Value-relevance research has a known scale problem: price-level
regressions can look strong because large banks have large prices, large
earnings, and large book values together. One strand of the literature
therefore recommends returns (or price changes, or log prices) as the
dependent variable, or a lagged price control, as a sensitivity. The
thesis should add one such sensitivity, clearly labelled as a
sensitivity, not a replacement headline: re-estimate Model 2 with
log MPS_RD, and separately with MPS_RD growth, and report whether the
sign pattern (negative interactions) survives. If it does not survive,
that is informative, not fatal: the thesis's question is about price
levels at a reporting deadline, and the level model is the standard
Ohlson empirical specification. But an examiner will raise the scale
question, and a one-table answer is better than a paragraph of defence.

### 7. A causal-design upgrade, stated as future work, not smuggled into
### this thesis (do, in Chapter 5 only)

The current design cannot identify a causal merger effect: it has one
never-merged series (NMB, itself Kanchan-merged in 2020), five banks
total, and a calendar Post indicator that year fixed effects absorb.
The excellent next design is a difference-in-differences / event-study
design over all 20 surviving banks, with never-merged and minimally
merged banks as controls, staggered merger timing, and an event window
around each merger's joint-operation date. Chapter 5 already gestures
at this. Make it precise: name the control group, the staggered timing,
and the pre-trend test that the current design cannot run (because it
has only three pre years and one control series). Stating the next
design precisely is what makes the current design's non-causal framing
credible, rather than a disclaimer pasted over a causal conclusion.

## C. Excellent process upgrades (how the analysis is done, not just what)

### 8. Freeze the analysis plan and log deviations (do)

The thesis already has `data_analysis/analysis/ANALYSIS_PLAN.md`. Turn it
into a frozen plan: date-stamp it, hash the joined panel and the plan
together, and add a deviations log in which every post-plan choice
(R6's year exclusion, the R8 row list, the 5-day window) is recorded with
its reason and its date. A frozen plan with a deviations log is worth
more than a plan that silently matches the final code, because it lets
an examiner distinguish a pre-committed sensitivity from a
specification chosen after seeing its p-value. R6 is the case in point:
it is institutionally motivated, but it was not obviously pre-committed,
and a deviations log is how the thesis proves its motivation.

### 9. A reproducibility test that would have caught the main error (do)

Add three automated tests to the analysis test suite, each of which
fails on the current pipeline and passes after the fix:
(a) a test that recomputes one confidence interval from its coefficient
and standard error using the t critical value on residual df, and
asserts the table's interval matches it (this test fails today, because
the table uses 1.96);
(b) a test that asserts every delta standard error in Table 4.6 is
computed from the delta's own covariance row, not copied from another
coefficient (this test fails today for R6 delta_B);
(c) a test that asserts the price-source note in Chapter 3 and the
price-verification note in Table A4 agree on the NMB FY 2076/77 cell
(dataset 437.00, Merolagani 436.00, NEPSE unverified) (this test fails
today, because Chapter 3 reverses the sources). Tests that encode the
review's findings are how a thesis stops regressing when it is next
edited, which is exactly what happened to the BAFIA wording between the
proposal and the draft.

### 10. A measurement appendix for the one verification that is still open (do)

The single largest remaining data gap is NEPSE official-close
verification for MPS_RD. The excellent process is not to claim it, but
to publish the protocol for closing it: for each of the 28 clean rows,
the NEPSE daily bulletin (or SEBON filing) to request, the date to
request it for, and the field to record (official close versus last
traded price). Add that protocol as an appendix table, with the column
"official close: not yet obtained" filled honestly for all 28 rows.
An appendix that says "not yet obtained, here is how to obtain it" is
stronger than a methodology chapter that implies it was obtained, and
it gives the supervisor a concrete next task that does not require
re-running any regression.

### 11. A "what would change my conclusion" table (do, one page)

For each of the thesis's five most load-bearing choices, state in one
row what would have to be true for the conclusion to flip: (1) if
official NEPSE closes differed from aggregator closes by more than a
few rupees on the price dates; (2) if the FY 2078/79 entity mismatch
were resolved by restating fundamentals to the merged entity rather
than by dropping the year; (3) if year fixed effects were replaced by
explicit macro controls (policy rate, NEPSE index) and the interactions
survived; (4) if the wild bootstrap or permutation p-value for the
joint test fell below 0.05 in the baseline; (5) if a 20-bank DiD found
no interaction. This table is the most creative and the most honest
single addition the thesis can make: it tells the examiner, in advance,
exactly how to falsify it, which is the definition of a falsifiable
thesis.

## D. What not to do (traps)

- Do not add a cluster-robust standard error with G = 5 as the headline
  and call the problem solved. Cluster-robust inference with five
  clusters over-rejects; that is why the thesis chose HC3 in the first
  place. The wild bootstrap is a sensitivity, not a replacement headline,
  for the reason in item 2.
- Do not add a specification curve with indefensible specifications in
  it (P/E as a regressor, imputed prices, Ashadh-end prices) and then
  average over them. The curve's credibility comes from its dimensions
  being defensible, not from its size.
- Do not add a returns model as the headline and drop the price-level
  model. The thesis's question, as approved in the proposal, is about
  price levels at a reporting deadline. A returns sensitivity strengthens
  it; a returns headline changes the question.
- Do not "fix" the baseline by dropping NMB, dropping HBL, or dropping
  any bank because its inclusion weakens the result. Leave-one-bank-out
  is a diagnostic to report, not a selection rule to apply.
- Do not re-run the analysis until a specification gives p < 0.05 and
  then report only that specification. That is the exact behaviour the
  sensitivity hierarchy in item 3 exists to prevent, and it is how a
  thesis that is currently honest becomes dishonest.
