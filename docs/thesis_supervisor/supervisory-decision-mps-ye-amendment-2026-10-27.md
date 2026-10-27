# Supervisory decision: MPS_post not estimable, MPS_YE amendment approved (conditional)

> **File provenance note (added by Muse, not part of the decision text below):**
> This document was provided by Krishna in chat on 2026-10-27, presented
> in a supervisor's voice. The text itself states that its author had
> not independently verified live NEPSE / Merolagani / SEBON records in
> that chat, and that every external fact in it is conditional on the
> data status provided by Muse. Until Krishna confirms whether this is
> his university supervisor's actual ruling or drafted guidance, do
> NOT cite it in the thesis as an official supervisor letter. The
> decision text below is reproduced verbatim from the message as
> received, starting after this note.

---

Acting as your supervisor, I will give you exact, non-vague guidance.

I am not claiming that I have independently verified live NEPSE/Merolagani/SEBON records from the internet in this chat. Therefore, every external fact below is conditional on the data status you have provided. For your thesis, you must keep primary-source evidence for every observation you use.

## Final supervisory decision

### 1. Your original proposed regression is not estimable

Your proposed model is:

\[
MPS\_post_{i,t} = \beta_0 + \beta_1 EPS_{i,t} + \beta_2 DPS_{i,t} + \beta_3 BVPS_{i,t} + \beta_4 ROA_{i,t} + \varepsilon_{i,t}
\]

Parameters:

- Intercept: 1
- EPS: 1
- DPS: 1
- BVPS: 1
- ROA: 1

So:

\[
k = 5
\]

Your realized valid left-hand-side sample is:

\[
n = 2
\]

Therefore:

\[
df = n - k = 2 - 5 = -3
\]

That is not weak evidence. That is impossible estimation. OLS cannot estimate five parameters from two observations.

Even your reduced model:

\[
MPS\_post_{i,t} = \beta_0 + \beta_1 EPS_{i,t} + \beta_2 BVPS_{i,t} + \varepsilon_{i,t}
\]

has:

\[
k = 3
\]

\[
df = 2 - 3 = -1
\]

Also impossible.

So, under the current proposal rule, you cannot run the regression.

---

### 2. I do not approve substituting Ashadh-end price as MPS_post

The Ashadh-end candidate price is not `MPS_post`.

Your definition of `MPS_post` is:

> NEPSE closing price on the first NEPSE trading day with a calendar date strictly greater than the NEPSE disclosure date of that bank-year’s audited annual financial statements.

The Ashadh-end price is:

> NEPSE closing price on or before the fiscal year-end date.

These are different variables.

The timing is different:

- `MPS_post`: disclosure happens first, then price is observed.
- Ashadh-end price: price is observed before audited financial statement disclosure.

Therefore, Ashadh-end price cannot be used as `MPS_post` unless you are willing to falsify the variable definition. You must not do that in a thesis.

So my supervisory ruling is:

> **No. Ashadh-end candidate price may not be labelled, treated, or interpreted as MPS_post under the current proposal.**

---

### 3. But you may proceed with a formally amended dependent variable

You may use the Ashadh-end price only if you change the research design.

The new dependent variable must be named differently, for example:

\[
MPS\_YE
\]

or:

\[
P\_YE
\]

where:

\[
MPS\_YE_{i,t}
\]

means:

> NEPSE official closing price of the ordinary share on the last NEPSE trading day on or before the official fiscal year-end date, using the unadjusted price series.

Then the model becomes:

\[
MPS\_YE_{i,t} = \beta_0 + \beta_1 EPS_{i,t} + \beta_2 DPS_{i,t} + \beta_3 BVPS_{i,t} + \beta_4 ROA_{i,t} + u_{i,t}
\]

This is no longer a post-disclosure market reaction model.

It becomes an association/value-relevance model using fiscal year-end market price.

That is acceptable only if your proposal, title, objectives, hypotheses, methodology, and limitations are amended accordingly.

---

# Your exact data status and what is usable

## A. Usable MPS_post observations

Based on your statement, only two rows currently qualify as possible `MPS_post`:

1. **GBIME, FY2081/82**
   - Disclosure date: 2025-10-16
   - First trading date: 2025-10-19
   - Price: 240.00
   - Label: LTP

2. **NIMB, FY2081/82**
   - Disclosure date: 2025-12-24
   - First trading date: 2025-12-28
   - Price: 193
   - Label: Close

However, even these two must pass one final check.

### Important verification for GBIME

Your definition requires **NEPSE closing price**, not merely last traded price from a secondary source.

For GBIME, the price is labelled `LTP`.

You must verify whether 240.00 is the official NEPSE closing price for 2025-10-19.

If it is only a last traded price from a secondary feed and cannot be verified as NEPSE closing price, then GBIME FY2081/82 is not usable as `MPS_post`.

If GBIME fails verification, your realized `MPS_post` sample becomes:

\[
n = 1
\]

That is even worse.

So, for `MPS_post`, you must keep only observations where all three of the following are proven:

1. Official or otherwise acceptable NEPSE disclosure date.
2. First NEPSE trading day strictly after that disclosure date.
3. Official NEPSE closing price for that first trading day.

If any one of these is missing or unverified, the observation is not usable as `MPS_post`.

---

## B. Pending candidate rows are not data

You listed:

- HBL FY2081/82, candidate 191.90 on 2025-12-28
- KBL FY2081/82, candidate 181.40 on 2025-12-15
- NMB FY2081/82, candidate 256.10 on 2025-12-17

These are not usable as `MPS_post` yet.

Reason:

- HBL and KBL: candidate price only; disclosure anchor not established.
- NMB: NEPSE close may be confirmed, but disclosure anchor is unproven.

A price without a verified disclosure anchor cannot prove that the price date is the first trading day after disclosure.

So these remain:

> **Pending. Not usable as data.**

---

## C. Locator-only rows are not usable

You listed locator-only rows:

- GBIME FY2077/78
- GBIME FY2078/79
- GBIME FY2079/80
- NIMB FY2079/80
- NIMB FY2080/81

You also stated that one GBIME observation is dropped because the bank was suspended on the candidate price date.

These are not usable as `MPS_post` because:

- disclosure date comes from Merolagani, not verified NEPSE disclosure evidence;
- price is LTP only, not verified NEPSE closing price;
- the observation is not settled.

So these remain:

> **Locator only. Not usable as regression data.**

---

## D. No-disclosure rows are missing observations

You listed 20 rows with no disclosure date found.

Those rows cannot be used as `MPS_post`.

A missing disclosure date means the dependent variable cannot be constructed under your definition.

Do not guess disclosure dates. Do not use annual report dates unless your definition is formally changed. Do not infer dates from secondary websites unless they are accepted by your supervisor and university as primary-equivalent evidence.

These remain:

> **Missing. Not usable as MPS_post.**

---

# The Ashadh-end candidate price variable

You stated:

- Candidate Ashadh-end price: last dataset close on or before Ashadh-end target date.
- Clean subset: price date within 5 days of target date.
- Clean n = 26.
- Excluded for staleness:
  - GBIME FY2078/79, 31 days early
  - HBL FY2077/78, 64 days early
  - NIMB FY2077/78, 64 days early
  - NIMB FY2078/79, 36 days early

That is reasonable as a separate variable.

But it must be named differently.

Use:

\[
MPS\_YE
\]

or:

\[
P\_YE
\]

not:

\[
MPS\_post
\]

## Approved definition for the amended dependent variable

If you amend the thesis, I would approve the following definition:

> `MPS_YE` is the NEPSE official closing price, in NPR per ordinary share, on the last NEPSE trading day on or before the official fiscal year-end date. The price is unadjusted. The observation is accepted only if the price date is no more than five calendar days before the fiscal year-end date. If no such NEPSE closing price exists, the observation is treated as missing.

This gives you:

\[
n = 26
\]

assuming all 26 observations pass final verification.

With five parameters:

\[
k = 5
\]

\[
df = 26 - 5 = 21
\]

That is estimable.

It is still a small sample, but it is no longer impossible.

---

# Why substitution without amendment would be wrong

If you substitute Ashadh-end price into the original `MPS_post` model, you would be changing the economic meaning of the dependent variable.

## Original interpretation

The original model asks:

> Do EPS, DPS, BVPS, and ROA explain the market price immediately after audited financial statement disclosure?

This is a disclosure-response or post-disclosure association question.

## Ashadh-end interpretation

The Ashadh-end model asks:

> Do EPS, DPS, BVPS, and ROA for a fiscal year explain the market price at fiscal year-end, before the audited financial statements are disclosed?

That is a different question.

The Ashadh-end price may reflect:

- market expectations;
- unaudited information;
- macroeconomic conditions;
- bank-specific news;
- anticipated dividends;
- sector-level price movements;
- liquidity conditions;
- information not yet formally disclosed.

It does not cleanly measure the market’s response to the audited annual financial statements.

Therefore, if you use Ashadh-end price but call it `MPS_post`, your thesis would be internally inconsistent.

That is not acceptable.

---

# Your two possible paths

You have two legitimate paths.

---

## Track A: Keep the original MPS_post model

This track preserves your proposal but requires solving the missing data problem.

### What you must do

You must obtain valid NEPSE disclosure dates and first-day closing prices for enough bank-year observations.

For the model to be mathematically estimable, you need at least:

\[
n > k
\]

Since:

\[
k = 5
\]

the absolute mathematical minimum is:

\[
n = 6
\]

which gives:

\[
df = 1
\]

But that is too weak for a thesis.

Your intended sample was:

\[
n = 30
\]

That is much better.

For a credible OLS regression, you should aim to restore the intended 30 observations, or at least obtain a defensibly large sample.

### Sources to verify

You should seek evidence in the following order:

1. **NEPSE official announcement/disclosure records**
   - Bank announcement date.
   - Financial statement disclosure date.
   - Archive page, PDF, screenshot, or official download.

2. **SEBON filings**
   - Audited financial statement filing date.
   - Annual report submission/disclosure record.

3. **Bank’s official investor relations or annual report records**
   - Publication date of audited financial statements.
   - Board meeting date approving financial statements.
   - Public notice date.

4. **NEPSE historical trading data**
   - Official closing price for the required date.
   - Trading status for the required date.
   - Suspension status if applicable.

5. **Archived web records**
   - Wayback Machine or other archived snapshots.
   - Only as supporting evidence, not as primary evidence unless your supervisor accepts it.

### Evidence required for each MPS_post observation

For every row you want to use as `MPS_post`, create a record with these fields:

| Field | Requirement |
|---|---|
| bank | Exact bank code |
| fy | Fiscal year |
| disclosure_date | Verified date |
| disclosure_source | NEPSE/SEBON/bank record |
| first_trading_date | Strictly after disclosure_date |
| price_date | Same as first_trading_date |
| price_value | NEPSE closing price |
| price_field | Close, not LTP unless verified as official close |
| evidence_file | PDF/screenshot/archive reference |
| status | usable / pending / missing |

### If Track A fails

If you cannot find sufficient verified disclosure dates and closing prices, then the honest thesis conclusion is:

> The proposed post-disclosure regression could not be performed because the dependent variable could not be constructed for a sufficient number of observations.

That is not cheating. That is research integrity.

But you cannot manufacture the missing dependent variable.

---

## Track B: Amend the thesis and use MPS_YE

This is the realistic path if your deadline is near and the 26 Ashadh-end prices are verifiable.

### Required amendment

You must formally change the dependent variable.

Do not say:

> We used Ashadh-end price as a proxy for MPS_post.

That is too vague and dangerous.

Say:

> The original dependent variable, MPS_post, could not be constructed for a sufficient number of observations because verified NEPSE disclosure dates and post-disclosure closing prices were unavailable for most bank-year observations. Therefore, the study was amended to use fiscal year-end market price, MPS_YE, as the dependent variable. The amended model examines the association between accounting fundamentals and fiscal year-end share price, rather than the market reaction to audited financial statement disclosure.

That is honest.

---

# Approved amended model

If you choose Track B, the approved model is:

\[
MPS\_YE_{i,t} = \beta_0 + \beta_1 EPS_{i,t} + \beta_2 DPS_{i,t} + \beta_3 BVPS_{i,t} + \beta_4 ROA_{i,t} + u_{i,t}
\]

where:

- `MPS_YE` = NEPSE official closing price on the last trading day on or before fiscal year-end, subject to the five-day freshness rule.
- `EPS` = reported basic EPS from audited SOPL, NPR per share.
- `DPS` = board-proposed cash dividend per ordinary share, NPR per share, calculated as cash percent multiplied by NPR 100 face value.
- `BVPS` = ordinary shareholders’ equity at year-end divided by ordinary shares outstanding at year-end.
- `ROA` = profit after tax divided by average total assets, multiplied by 100.

Sample:

\[
n = 26
\]

Parameters:

\[
k = 5
\]

Degrees of freedom:

\[
df = 21
\]

This is mathematically estimable.

---

# Interpretation rules for the amended model

You must be very careful in the thesis.

## Do not say

- “post-disclosure market reaction”
- “market response to audited financial statements”
- “price after disclosure”
- “investors reacted to EPS/DPS/BVPS/ROA”

unless you have genuine `MPS_post` data.

## Say instead

- “association between accounting fundamentals and fiscal year-end market price”
- “value relevance of accounting information at fiscal year-end”
- “relationship between reported accounting measures and year-end share price”
- “association, not causal market reaction”

Example:

> The amended dependent variable is the fiscal year-end market price. Because this price is observed before the audited financial statements are publicly disclosed, the results should be interpreted as an association between accounting fundamentals and year-end market valuation, not as evidence of a post-disclosure market reaction.

That is correct.

---

# Special warning about DPS in the amended model

There is a timing issue with DPS.

Your DPS variable is:

> board-proposed cash dividend per share.

The board proposal is usually made after fiscal year-end, together with or after the audited financial statements.

But `MPS_YE` is observed at fiscal year-end.

Therefore, the market price at fiscal year-end may not yet know the officially proposed dividend.

So if DPS is significant in the `MPS_YE` model, you must not claim that the market reacted to the proposed dividend.

You should say:

> DPS may capture anticipated dividend policy or expectations of future dividend announcements, rather than a known board-proposed dividend at the fiscal year-end date.

This is important.

I recommend running a robustness check without DPS:

\[
MPS\_YE_{i,t} = \beta_0 + \beta_1 EPS_{i,t} + \beta_2 BVPS_{i,t} + \beta_3 ROA_{i,t} + u_{i,t}
\]

Report both:

1. Main amended model with all four accounting variables.
2. Robustness model excluding DPS due to disclosure timing.

This will protect you in the viva/defense.

---

# What sample size should you use?

Use the clean subset only:

\[
n = 26
\]

Do not use the four stale observations as year-end prices unless you formally change the definition and disclose the issue.

The four stale observations are:

| Bank-year | Days early |
|---|---:|
| GBIME FY2078/79 | 31 |
| HBL FY2077/78 | 64 |
| NIMB FY2077/78 | 64 |
| NIMB FY2078/79 | 36 |

A price 31 to 64 days before fiscal year-end is not a clean fiscal year-end price.

So my ruling is:

> Exclude the four stale observations from the main `MPS_YE` sample. Report them in the data-selection table as excluded for staleness.

If one of the 26 clean observations later fails NEPSE closing-price verification, remove it and report the reduced sample.

Do not keep an observation just because it is convenient.

---

# Do not mix the two dependent variables

This is a strict rule.

You must not create one regression sample containing:

- some `MPS_post` observations;
- some `MPS_YE` observations;
- some candidate prices;
- some locator-only prices.

That would create an inconsistent dependent variable.

You may, however, do this:

1. Main analysis using `MPS_YE`, n = 26.
2. Separate appendix table showing the two verified `MPS_post` observations descriptively.
3. Separate data-availability audit showing why `MPS_post` was not feasible.

But you must not combine them into one dependent variable.

---

# Recommended final design for your thesis

Given what you have told me, the safest defensible path is:

## Main model

\[
MPS\_YE_{i,t} = \beta_0 + \beta_1 EPS_{i,t} + \beta_2 DPS_{i,t} + \beta_3 BVPS_{i,t} + \beta_4 ROA_{i,t} + u_{i,t}
\]

Sample:

\[
n = 26
\]

Estimation:

- Pooled OLS as baseline.
- Robust standard errors, preferably HC3 because sample is small.
- Do not cluster by bank with only five banks unless you use a small-cluster correction or bootstrap. Ordinary cluster-robust variance with five clusters is unreliable.

Diagnostics:

- VIF for multicollinearity.
- Residual normality plot.
- Residuals versus fitted values.
- Cook’s distance / leverage.
- Pairwise correlation matrix.
- Robustness excluding DPS.
- Robustness with bank dummy variables if degrees of freedom remain acceptable.

If you add bank dummies:

- 5 banks means 4 bank dummies.
- Total parameters become 9.
- df becomes:

\[
26 - 9 = 17
\]

That is still estimable but weaker.

If you add year dummies too:

- 6 years means 5 year dummies.
- Total parameters become:

\[
1 + 4 + 4 + 5 = 14
\]

\[
df = 26 - 14 = 12
\]

That is possible but may overfit with only 26 observations.

So I recommend:

- Baseline: pooled OLS.
- Robustness: bank dummies only, if justified.
- Do not make two-way fixed effects your main model unless your supervisor specifically requires it.

---

# Exact thesis wording you can use

## Statement explaining the original blocker

You can write:

> The original proposal specified the dependent variable as the NEPSE closing price on the first trading day strictly after the NEPSE disclosure date of the audited annual financial statements. During data construction, only two bank-year observations could be verified under this definition. With five parameters to estimate, the model was not identifiable because the degrees of freedom were negative. Therefore, the proposed post-disclosure regression could not be estimated using the original dependent variable.

This is accurate.

---

## Statement explaining the amendment

You can write:

> Due to the unavailability of verified NEPSE disclosure dates and post-disclosure closing prices for the majority of bank-year observations, the dependent variable was amended to fiscal year-end market price, denoted MPS_YE. MPS_YE is defined as the NEPSE official closing price of the ordinary share on the last NEPSE trading day on or before the fiscal year-end date, subject to a maximum freshness window of five calendar days. This amendment changes the research question from a post-disclosure market reaction analysis to an association analysis between accounting fundamentals and fiscal year-end market price.

This is honest and defensible.

---

## Limitation paragraph

You can write:

> The use of fiscal year-end market price as the dependent variable has an important limitation. The audited financial statements, including reported EPS, DPS, BVPS, and ROA, are generally disclosed after fiscal year-end. Therefore, the year-end price may not directly incorporate the audited accounting numbers. Instead, it may reflect market expectations and other information available at the fiscal year-end date. Consequently, the results should be interpreted as evidence of association rather than as evidence of a causal market reaction to audited financial statement disclosure.

This is necessary.

---

# What you must not do

You must not do any of the following:

1. Do not label Ashadh-end price as `MPS_post`.
2. Do not use pending candidate prices as finalized `MPS_post`.
3. Do not use locator-only rows as regression observations.
4. Do not use Merolagani-only disclosure dates as final proof if your definition requires NEPSE disclosure date.
5. Do not impute missing `MPS_post` values from year-end prices.
6. Do not mix `MPS_post` and `MPS_YE` in the same regression.
7. Do not include stale year-end prices in the main sample without a formal definition change and explicit disclosure.
8. Do not claim post-disclosure market reaction if the price is observed before disclosure.
9. Do not silently drop observations. Every exclusion must be reported.
10. Do not adjust numbers to make the regression work.

---

# Formal approval language

You can use this as a supervisory-style approval note.

> The proposed dependent variable, MPS_post, cannot be estimated because only two observations satisfy the required definition, while the model contains five parameters. Therefore, the proposed MPS_post regression is not feasible.
>
> Substituting Ashadh-end candidate price for MPS_post under the current proposal is not approved because it changes the dependent variable and the interpretation of the study.
>
> Use of Ashadh-end price is approved only as a separate dependent variable, MPS_YE, after formal amendment of the research question, title, objectives, hypotheses, methodology, and limitations. The amended model may be estimated using the clean fiscal year-end price sample, subject to verification that each price is a NEPSE official closing price and that each price date is within five calendar days of the fiscal year-end target date.
>
> The amended analysis must be interpreted as an association/value-relevance analysis using fiscal year-end price, not as a post-disclosure market reaction analysis.

---

# My practical recommendation

If your thesis deadline is near, choose Track B.

That means:

1. Stop trying to force the 26 Ashadh-end prices into `MPS_post`.
2. Amend the dependent variable to `MPS_YE`.
3. Use the clean n = 26 sample.
4. Rewrite the research question as an association/value-relevance question.
5. Add the limitation that year-end price precedes audited disclosure.
6. Run OLS with diagnostics.
7. Keep the two verified `MPS_post` observations only as evidence of your original data-collection effort, not as part of the main regression.

If your university refuses to allow the amendment, then the honest result is:

> The proposed regression could not be performed due to insufficient verified post-disclosure price data.

That is better than presenting a mislabeled variable.

---

# Final instruction as supervisor

My instruction is:

> Proceed only with the amended `MPS_YE` model if your proposal can be formally amended. Do not present Ashadh-end price as `MPS_post`. If the amendment is not allowed, you must either collect sufficient verified `MPS_post` data or report that the proposed regression is infeasible.

That is the correct, defensible thesis path.
