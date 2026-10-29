# Finalized review — Chapter III: Research Methodology, audited against docs/instructions

**Thesis version audited:** HEAD 8c96edc (pulled 2026-10-29).
Files checked, both versions:
`docs/draft/thesis/chapter_03_research_methodology.md` and
`src/thesis/chapters/chapter_03_research_methodology.tex`,
plus the analysis code and tables they describe
(`data_analysis/analysis/stats/models.py`, `diagnostics.py`,
`outputs/tables/T2`, `T6`, `A4`) where a chapter claim is about
code or a table.
**Thesis files changed to write this review: NONE.** Applying any
fix still needs the author's approval, in both versions where the
passage appears in both.

**Standard applied:** `docs/instructions/instructions_for_paper.md`
— §2 traps (especially Trap 3 timing, Trap 4 small clusters,
Trap 5 df, Trap 7 causal language, Trap 8 missing-data protocol),
§5 sample/data rules, §6 robustness suite, §7 prose rules,
§10 rubric (especially items 2–10, 11–14). The instructions'
illustrative numbers (§6.2, §8.2) are NOT thesis numbers and
were not used as a check standard here.

## How this chapter was checked, so it can be re-checked

1. Read Chapter III in full, both versions, section by section.
2. Re-checked every Phase 2 Chapter III must-fix and minor
   against the 8c96edc text — most are now fixed (see Passes).
3. Checked chapter claims against code/tables where the chapter
   names them: estimation tool, HC3 formula, df counts, R1–R8
   sample sizes, VIF computation, A4 verification scope.
4. Did one targeted online check in this step (GBIME "largest
   bank" — see Minor M2), because that claim's citation date
   decides whether it is an error or a pass.
5. Anything not verified in this step is listed under
   "NOT verified — not counted as errors", not under Must-fix.

## Verdict for Chapter III

Chapter III is the strongest chapter against the instructions.
It now satisfies, in its own text, almost every methodology rule
the instructions impose: the four purposive hurdles, Bank-only
compilation, the 5-day freshness rule with both exclusions
documented, the BAFIA operationalization, the Post-absorption
equation, HC3 with the correct verb direction, Student's t on
residual df, the full R1–R8 suite with correct n and df, and
the pro-forma R7 / restated-EPS R8 disclosures. The remaining
issues are one precision error in a verification description,
plus wording minors — no wrong model, sample, price, df, or
tool claim remains in this chapter as written.

## Must-fix (verified)

### 1. Merolagani comparison described as "target-date" comparison — it is not, for 2 of 30 rows
- **Rule:** §5.2 (secondary sources reconciled honestly);
  §10 rubric 11 (numbers and descriptions match 100% across
  text, tables, and code).
- **Evidence (verified against A4 itself):** §3.4.3, point 3,
  says: "For every bank-year observation, closing market
  share prices on the target date were compared across
  ShareSansar and Merolagani ... Out of 30 target cells,
  29 demonstrated perfect zero-variance matching."
  A4 (`outputs/tables/A4_price_verification.md`, verified
  in the Phase 1 review) compares DATASET prices, and its
  two FY 2077/78 suspended rows are compared on their
  DELAYED resumption dates, not on the target date:
  HBL FY 2077/78, price date 2022-06-06, 358.90;
  NIB FY 2077/78, price date 2022-05-30, 367.70.
  Those two prices were then EXCLUDED from estimation by
  the freshness rule. On the target date (13 April 2022)
  neither security traded at all, so no target-date
  Merolagani comparison exists for them.
- **Fix:** Reword §3.4.3 point 3 to match A4 exactly, e.g.:
  "Dataset prices (28 clean observation-date prices plus
  the two delayed resumption prices, which were then
  excluded from estimation) were compared against
  Merolagani LTPs; 29 of 30 matched, the exception being
  NMB FY 2076/77 (dataset 437.00, Merolagani LTP 436.00,
  retained on ShareSansar's own full daily record, which
  is not independent verification)." The numbers (29/30,
  437/436, OHLC 432/439/428/437) are already correct in
  the chapter; only the scope phrase "on the target date"
  / "30 target cells" is wrong.
- **Both versions:** the §3.4.3 paragraph appears in both;
  fix in both. A4 itself is already correct and must not
  be changed to match the chapter's wording.

## Minor (verified, fix with the must-fix batch)

### M1. "Eight-part robustness suite" miscounts what is robustness
- §3.6.5 calls R1–R8 an "eight-part robustness suite".
  R1 is Model 1 baseline and R2 is Model 2 baseline;
  the robustness VARIANTS are R3–R8 (six), matching the
  instructions' §6.4 list (ROA substitution, DPS inclusion,
  transition exclusion, entity-mismatch exclusion, bonus
  adjustment, restated EPS). The specification comparison
  in §3.6.6 (pooled vs. bank-FE vs. two-way) is a seventh
  robustness angle, also outside R1–R8. Fix: call R1–R8
  an "eight-specification suite (R1–R2 baselines plus
  six robustness variants R3–R8)", or rename the section
  accordingly. All n and df in the R1–R8 list are correct
  (R1/R2/R3/R4/R7/R8 n = 28; R5/R6 n = 23; R4 df 13) —
  this is naming, not arithmetic. (This settles Chapter I,
  Minor M3, for Chapter III's own wording; Chapter I's
  "eight-part" preview should then be aligned with the
  corrected Chapter III wording.)

### M2. GBIME "largest bank" claim cited to a 2022 document
- §3.3.3, GBIME profile: "Following amalgamation, GBIME
  emerged as the largest commercial bank in Nepal by total
  asset scale and paid-up equity capital (Global IME Bank,
  2022)."
- **Substance verified in this step:** post-merger GBIME
  was indeed the largest by paid-up capital (post-merger
  ~NPR 35.7–36.1 bn, ahead of NIMB ~34.1 bn; total assets
  ~NPR 500 bn at merger, later ~NPR 675 bn) — the claim
  itself is not false.
- **Citation timing is the problem:** a 2022 source
  predates the January 2023 amalgamation, so it can at
  most support a pre-merger projection ("will be the
  largest", as the June 2022 merger announcement put it),
  not a post-merger fact in past tense. Fix: either
  re-cite the largest claim to a post-merger source
  (e.g., NRB statistics or a post-merger annual report),
  or reword to the 2022 projection ("was projected to
  become the largest"). Do not delete the claim — it is
  true; only its citation tense is off.

### M3. EPS–ROA VIF "approximately 30 when conditioning on fixed effects" is uncomputed
- §3.5.2, ROA: "EPS and ROA correlate at $r = 0.975$
  (yielding a bivariate VIF of $1/(1-r^2) \approx 20.3$,
  rising to approximately 30 when conditioning on fixed
  effects)".
- **Verified:** bivariate VIF ≈ 20.3 is exact from
  $r = 0.975$. The "≈ 30" figure appears in NO output:
  `diagnostics.py` computes VIF on substantive regressors
  ONLY, fixed-effect dummies excluded, and T6 reports
  VIF 1.16 for EPS/BVPS — there is no EPS+ROA VIF, with
  or without fixed effects, in the outputs. T2's note
  ("variance inflation ~ 30") has the same uncomputed
  figure, without the bivariate qualifier.
- **Fix:** either compute the FE-conditioned EPS–ROA VIF
  and cite the output, or delete "rising to approximately
  30" and keep the exact bivariate 20.3 (which alone
  justifies never co-including EPS and ROA, the decision
  that actually matters). The same reconciliation belongs
  in the Chapter IV step for T2's note. Not a must-fix,
  because no specification co-includes EPS and ROA, so
  no estimate depends on the 30 figure.

### M4. "Utilized" — §7.2 prefers "use"
- At least one verified instance, both versions:
  §3.5.2 BVPS reconciliation rule, "Printed NAV ...
  is utilized as an audit reconciliation check".
  Change to "is used". Grep count for utilize-forms in
  the chapter is 3; the other forms are the same
  preference, not prohibited vocabulary (see Passes).

### M5. Identification phrase needs its bank-demeaning qualifier
- §3.2, point 4: "slope coefficients are identified
  exclusively from within-year cross-sectional variation
  among the sampled commercial banks."
- With two-way fixed effects, identification comes from
  variation AFTER removing bank means AND year means.
  "Within-year cross-sectional" alone could be read as
  ignoring the bank demeaning. Fix: add "after removing
  bank means" (e.g., "from within-bank variation net of
  common year shocks"). This is a precision wording fix,
  not a model error — the model equations themselves
  (§3.6.1–3.6.2) are correct.

## Passes — verified compliances, including Phase 2 items now fixed (do NOT re-open)

- **Phase 2 must-fix 1, Group equity: FIXED.** §3.4.1 now
  reads: "In the Global IME Bank raw extractions, Group
  total equity equals equity attributable to equity
  holders and excludes non-controlling interest
  (NPR 211.28 million in FY 2076/77); Group-level figures
  are never utilized in panel regressions." Scoped to
  GBIME, exact amount, Bank-only compilation stated.
  The general sentence that was false for HBL/NMB is gone.
- **Phase 2 must-fix 2, reference distribution: FIXED.**
  §3.6.3 now states: "All $t$-statistics, $p$-values, and
  parameter confidence intervals are referred to Student's
  $t$ distribution on residual degrees of freedom
  ($t(14)$ for Model 2, $t(16)$ for Model 1), avoiding
  asymptotic normal approximations." Code uses
  `use_t=True`; chapter and code now agree in words.
- **Phase 2 must-fix 3, tools: FIXED.** §3.6.7 now reads:
  Python (`pandas`, `numpy`) for extraction/assembly;
  Python (`statsmodels`, `seaborn`, `matplotlib`) for
  modelling/diagnostics/visualization. Grep of
  `data_analysis/analysis/` Python files: `linearmodels`
  0 matches, Excel/openpyxl 0 matches; `statsmodels`
  is imported in `models.py`. The false tool claims are
  gone, and the true tools are named.
- **Phase 2 must-fix 4, Chaitra: FIXED in Chapter III.**
  No passage in Chapter III calls end-of-Chaitra the
  statutory deadline. §3.5.2 defines MPS_RD as following
  the statutory nine-month deadline, "Operationalized at
  the end of Chaitra (mid-April)"; §3.3.4 calls it "the
  study's operationalized reporting deadline (end of
  Chaitra)". That is the correct template throughout.
- **Phase 2 must-fix 5, aggregator wording: FIXED.**
  Table 3.1 note now reads: prices "retrieved from capital
  market data aggregators (ShareSansar and Merolagani;
  cross-checked against FinancialNotices for FY 2081/82).
  Note that official NEPSE floor trading archives were
  not independently verified, and NEPSE official closes
  remain unverified." No "official archives" as a source
  claim remains. (The FinancialNotices scope — FY 2081/82
  only — is correctly stated here.)
- **Phase 2 must-fix 6, HC3 verb: FIXED.** §3.6.3 now
  reads: "Dividing squared residuals by $(1-h_{ii})^2$
  inflates the influence of high-leverage observations,
  yielding conservative standard error estimates."
  Formula and verb now agree; the backwards
  "discounts/downweights" wording is gone from this
  chapter (Chapter IV's instance remains for its step).
- **Selection criteria, §5.1: PASS — and this closes
  Chapter I, Minor M2.** §3.3.2 lists all four hurdles:
  (1) 2023-wave participation, (2) unmerged benchmark
  continuity, (3) complete audited NFRS statements for
  all six years submitted to NRB, (4) NEPSE listing with
  the 5-day freshness rule. Population (20 licensed
  Class 'A' banks) and sample (5 series) are both stated.
  §5.1's proportion-of-sector disclosure is NOT in
  Chapter III either — that gap belongs to Chapter I,
  Must-fix 4, not here.
- **Traps: PASS.** Trap 1: P/E strictly excluded (§3.5.2,
  §5). Trap 3: MPS_RD after the deadline, 5-day rule,
  missing-not-imputed (§3.3.4, §3.5.2). Trap 4: $G = 5$,
  HC3, exploratory framing (§3.2 point 5, §3.6.3).
  Trap 5: df stated for Model 1 (16), Model 2 (14),
  R4 (13) (§3.6.1–3.6.3, §3.6.5). Trap 7: observational,
  non-experimental, associations not causal impacts
  (§3.2 points 3 and 5). Trap 8: explicit missingness
  protocol, both exclusions with dates and lateness
  (§3.3.4), entity-mismatch retained in baseline and
  tested in R6 (§3.3.4 note c, §3.6.5 R6).
- **Post absorption: CORRECT.** §3.6.2: $\mathit{Post}_t =
  D_{2079/80} + D_{2080/81} + D_{2081/82}$ — the exact
  linear combination, with the dummy-trap consequence
  stated. The Phase 2 "indicator equated to a sum of
  coefficients" error is gone.
- **Restatements, denominator timing, NAV rounding:
  COMPLETE and CORRECT.** §3.4.3 lists all five
  restatements (GBIME 718.44m, HBL 1,877.08m, KBL
  1,047.39m, KBL −7,369.69m, KBL 9.59m / 0.005%) with
  the own-current rule. §3.5.2 gives the EPS-denominator
  timing disclosure with exact examples (GBIME 22.06 vs.
  18.71, NIMB 13.92 vs. 10.90, HBL 9.18 vs. 7.22).
  §3.5.2 gives all five NIMB integer-rounding pairs and
  flags NMB FY 2081/82 (175.18 vs. 174.49, gap 0.69) as
  unresolved. R7 is correctly called a pro-forma forward
  adjustment (§3.6.5 R7); R8 correctly lists GBIME
  17.99→15.33 and NMB 16.66→14.76 in-sample, with HBL
  28.07→27.60 out-of-sample and excluded (§3.6.5 R8).
  The wrong "29.80" figure appears nowhere in this chapter.
- **Table 3.1 numbers: PASS.** All 28 clean prices, 2
  missing cells, observation dates (including 14 April
  2024, Friday-Chaitra-end note), entity-mismatch
  footnote c, and N = 28 (13/15) match the joined panel
  and the Phase 1/2 recomputations. (Table 3.1's note on
  verification scope is Must-fix 1's wording issue, not
  a number issue.)
- **Primary-audit rule, §5.2: PASS.** §3.4.1–3.4.3:
  accounting variables from audited reports, Bank-only,
  identities ≤ 1 NPR, aggregator discrepancies resolved
  in favour of audited accounts, NMB 437/436 retained on
  ShareSansar's own record with the explicit
  "does not represent independent verification" qualifier.
- **Prose, §7.1: PASS except M4.** Prohibited words by
  grep: delve 0, underscores 0, showcasing 0, pivotal 0,
  testament 0, beacon 0, tapestry 0, paramount 0,
  "game changer" 0, multifaceted 0, myriad 0,
  "it is important to note that" 0, facilitate 0.
  Diagram uses $\lambda_t$ correctly (the Phase 2
  "$l_t$" minor does not survive in this version's text).
- **Suspension wording in Chapter III: PASS.** §3.3.4
  says "merger-related trading suspensions" and, for
  HBL, "following the rejection ... at its 29th AGM in
  January 2022. Trading remained suspended until 6 June
  2022" — the correct post-rejection framing, not
  "during merger negotiations". (Chapter V's "during
  merger processes" remains for its step.)

## NOT verified in this step — not counted as errors

- **"Largest" for NIMB and other profile adjectives:**
  "one of the largest corporate banking portfolios"
  (NIMB, §3.3.3) is vague, not a ranking claim, and was
  not treated as an error. GBIME's largest claim is
  Minor M2 (citation timing only).
- **Bank-profile details beyond dates/ratios:** branch
  network expansions, deposit-base claims, "complementary
  branch networks" — cited to bank documents in the
  text, not independently re-verified here. Dates and
  swap ratios were verified in the Phase 2 loop.
- **NRB population history (32 → 20):** cited to
  (NRB, 2023) / NRB directories in §3.3.1, not
  re-verified here; it is consistent across Chapters I–III.
- **SEBON / MoF Economic Survey as contextual sources
  (§3.4.2):** listed as contextual, not as empirical
  inputs; no claim in Chapter III depends on a specific
  SEBON/MoF figure, so no verification was attempted.
- **"Approved by NRB" as a publication step:** Chapter III
  does not make this claim (Chapter II's version was
  verified in practice in the Chapter II step); nothing
  to check here.
- **Diagnostics beyond VIF:** Breusch-Pagan, Cook's
  distance threshold $4/28 \approx 0.143$, Q-Q normality
  (§3.6.4) are stated as protocol, not as results — the
  results themselves (T6 values) belong to the Chapter IV
  step, where chapter-vs.-table agreement will be checked.
- **§3.6.6 specification comparison results:** pooled and
  bank-FE-only estimates are described as comparators;
  their values live in A5/T5 and belong to the Chapter IV
  step.

## Scope limits of this Chapter III review

- No thesis, table, figure, code, or data file was changed.
- No compiled PDF was proofread; TU FOM formatting (§9)
  is not certified here.
- Next step, in the author's order: Chapter IV, against
  the same instructions, starting with the figure notes
  (F1/F2/A2/F5), the HC3 verb instance in Chapter IV,
  causal language, the T2 "~30" VIF note (see Minor M3),
  and chapter-vs.-table agreement for every number.
