# Reference: MPS_RD consolidation design (received 2026-10-27)

> Provenance note (added by Muse, not part of the guidance):
> This is a structured reference to a guidance message received
> in chat on 2026-10-27, recommending a new thesis design. It is
> NOT a verbatim reproduction and NOT an official supervisor
> ruling until Krishna confirms its origin. Literature cited
> in the guidance (Gurung and Dahal 2025, Giri 2024, Kwon and
> Wang 2020, Ohlson 1995) was not verified from the message
> alone and must be located and checked before citing.
> Two corrections from Muse's final audit apply to this
> design and override the guidance wording where they differ:
> (1) BAFIA Section 59(2) does not name Chaitra; end-of-Chaitra
> is the operationalization of its nine-month rule, not a
> statutory date; (2) FY2078-79 prices are post-merger entity
> prices for the four merged banks, so the pre period is
> contaminated by that row in a way the guidance's
> FY2079-80-only sensitivity does not cover.

## Recommended title

Accounting Value Relevance Across Nepal's 2023 Banking
Consolidation: Evidence from Selected Commercial Banks.

## Why this direction (guidance argument)

- Ordinary price-determinants models are already well covered
  in Nepal, so a routine EPS/BVPS/DPS regression adds little.
- The stronger question is whether the market's relative
  valuation of earnings and book value changed after mergers
  (precedent cited: Kwon and Wang 2020, on changes in value
  relevance after M&A; Ohlson 1995 as the valuation framework).
- The contribution is the change across the consolidation
  period, not newer data or another ratio.

## Dependent variable: MPS_RD

Market price per share at the reporting-deadline window.
Operational rule in the guidance:
- End of Chaitra in the fiscal year following the accounting
  year, corresponding to the BAFIA Section 59(2) nine-month
  publication deadline for audited statements.
- Actual NEPSE closing price on the first trading session
  after that deadline on which the bank's security records
  a valid trade.
- If trading is suspended or no valid price within a
  predefined short window, treat as missing, never carry
  forward a stale close.
- Check for known late disclosures; a legal deadline does
  not prove compliance.
- Explicitly NOT a verified first-trading-day-after-disclosure
  price, and must not be claimed as an immediate disclosure
  reaction. Feasibility of the fixed-date series must be
  validated before locking the design; if it cannot be
  recovered, do not relabel Ashadh-end prices as
  post-disclosure prices, use a lagged-fundamentals design
  with a revised title instead.

## Models

Model 1 (baseline):
MPS_RD_it = alpha + mu_i + lambda_t + beta_E*EPS_it +
beta_B*BVPS_it + eps_it.

Model 2 (change across consolidation):
MPS_RD_it = alpha + mu_i + lambda_t + beta_E*EPS_it +
beta_B*BVPS_it + delta_E*(EPS_it x Post_t) +
delta_B*(BVPS_it x Post_t) + eps_it.

i = bank, t = fiscal year, mu_i = bank fixed effects,
lambda_t = fiscal-year fixed effects, Post_t = 1 for
FY2079/80-FY2081/82, 0 for FY2076/77-FY2078/79.
Standalone Post is absorbed by year effects. Pre EPS
slope = beta_E, post = beta_E + delta_E; pre BVPS slope
= beta_B, post = beta_B + delta_B. Joint null:
H0: delta_E = delta_B = 0. Rejection = difference in
association, NOT proof mergers caused the change.

## Hypotheses (two-sided for H3, H4)

- H1: EPS positively associated with price (baseline).
- H2: BVPS positively associated with price (baseline).
- H3: EPS-price association differs pre vs post
  (delta_E != 0).
- H4: BVPS-price association differs pre vs post
  (delta_B != 0).

## Robustness in the guidance

1. ROA specification: replace EPS with ROA, recalculate
   correlation/VIF on the final sample before deciding
   whether both can go together.
2. Dividend specification: DPS separately, only where
   dividend information was available by the price date;
   secondary, not the main novelty.
3. Transition-year sensitivity: exclude FY2079/80.
4. Exclude P/E (mechanical: MPS/EPS).

## Estimation warnings in the guidance

- With 30 observations, bank + year fixed effects + four
  slopes, residual df about 16: small sample for
  interaction analysis. Report estimates, confidence
  intervals, and uncertainty, not just p-values and R2.
- Parsimonious fixed-effects specification, evidence
  described as exploratory, no causal claims.
- Harmonize EPS, BVPS, and prices for bonus shares,
  rights issues, merger share exchanges, and share-unit
  changes. Never silently replace missing/suspended-day
  prices with an older close.
- Cluster-robust inference unreliable with only five
  bank clusters; interpret uncertainty cautiously.

## Proposal wording

The guidance supplied ready-to-use proposal text (research
problem, general objective, three specific objectives,
three research questions, model specification, measurement
and estimation). That wording is in the chat message of
2026-10-27 and is not reproduced verbatim here; use the
design above and re-draft proposal text from it once
the supervisor approves, rather than copying the
guidance text as if it were already approved.
