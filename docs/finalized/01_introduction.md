# Finalized review — Chapter I: Introduction, audited against docs/instructions

**Thesis version audited:** HEAD 8c96edc (pulled 2026-10-29).
Files checked, both versions, line by line:
`docs/draft/thesis/chapter_01_introduction.md` (158 lines in this
version; the chapter is long paragraphs, so "line" below means a
Markdown line / paragraph block) and
`src/thesis/chapters/chapter_01_introduction.tex`.
**Thesis files changed to write this review: NONE.** Applying any
fix still needs the author's approval, in both versions where the
passage appears in both.

**Standard applied:** `docs/instructions/instructions_for_paper.md`
only — the 8 traps (§2), the Cochrane information pyramid and
15-minute skim test (§3), literature rules (§4), sample/data rules
(§5), results-reporting rules (§6), prose rules (§7), Chapter V
rules (§8, used here only to avoid misapplying them to Chapter I),
formatting (§9, not a prose test for Chapter I), and the 25-point
rubric (§10). Where the instructions give *illustrative* numbers,
they were NOT treated as thesis numbers (see the warning below).

## WARNING — do not "correct" the thesis to the instructions' numbers

The instructions contain worked examples that are NOT this thesis's
results and must never be copied into Chapter I (or Chapter IV):
§6.2 uses $\hat{\beta}_E = 6.43, p = 0.025$ and $\hat{\beta}_B = 0.78,
p = 0.370$ as a narrative example; §8.2's hypothesis table uses
$\hat{\beta}_E = +6.430$, $\delta_E = -14.619$, $\delta_B = +0.087$,
joint $F = 2.76, p = 0.098$. None of those is this thesis's estimate.
This thesis's verified numbers (Chapter IV / T4, independently
recomputed in the Phase 2 loop) are: Model 1 EPS 2.095, BVPS 0.219;
Model 2 pre EPS 5.577, pre BVPS 0.100, $\delta_E = -3.124$,
$\delta_B = -1.758$, joint Wald $F(2,14) = 2.954, p = 0.085$;
R6 joint Wald $F(2,10) = 5.818, p = 0.021$. Any findings paragraph
added to Chapter I under Must-fix 1 below must use THOSE numbers,
with the sensitivity-dependent framing, not the instructions'
examples.

## How this chapter was checked, so it can be re-checked

1. Read Chapter I in full, both versions, paragraph by paragraph.
2. Mapped every substantive claim to an instructions rule: the
   8 traps, the 25-point rubric, the prose list (§7.1–7.2).
3. Grep-verified the negative claims in this file (absence of
   results, absence of prohibited words, presence of a citation
   or a word in both versions). A claim marked "verified" below
   was checked by grep or by direct reading, not assumed.
4. Anything not verified in this step is listed under
   "NOT verified in this step — not counted as errors", not
   under Must-fix. That distinction is deliberate: listing an
   unverified attribution as an error would itself be slop,
   and it would create the regression this review is meant to
   prevent. Those items belong to the Chapter II step (for
   literature attributions) or the Chapter III/IV steps (for
   data and table claims), where their sources will be checked.

## Verdict for Chapter I

Chapter I is **econometrically honest and internally consistent,
but it fails the instructions' own Chapter I test**. Its models,
sample, df, freshness rule, exclusions, and non-causal framing all
comply with the traps and the rubric — that is a real pass, and
several Phase 2 items are verifiably fixed in this version (see
"Fixed since Phase 2"). What fails is structural, not arithmetic:
the instructions require the introduction itself, by page 2–3, to
deliver the core finding with exact magnitudes and significance
(§3.1, 15-minute skim test; §3 pyramid, level 1). Chapter I
delivers no finding at all — no coefficient, no Wald statistic,
no post-consolidation slope — only the *promise* of findings in
Chapter IV. An examiner applying the instructions' skim test
cannot pass Chapter I. Fix Must-fix 1 and the chapter changes
character; the remaining must-fix items are one wrong citation
attachment, one unsupported dominance sentence, and the opening
structure.

## Must-fix (verified)

### 1. No core finding in the introduction — §3.1 skim test fails
- **Rule:** §3.1, item 2: by page 2–3 the reader must know the
  central empirical finding — exact magnitudes and significance —
  and what it teaches that prior literature missed. §3 pyramid,
  level 1: the core finding comes first.
- **Evidence (grep-verified):** Chapter I contains no Model 1 or
  Model 2 coefficient value, no Wald $F$ value, no $p$-value for
  any slope, and no post-consolidation slope. "Wald" occurs only
  twice: once as a method name in Specific Objective 2, once in
  the §1.7 preview of Chapter IV. The chapter states the
  questions, objectives, and hypotheses, then stops.
- **Fix:** Add one findings paragraph at the end of §1.1 or the
  start of §1.5, using ONLY the verified thesis numbers in the
  warning above, and framed exactly as the thesis frames them
  elsewhere: baseline interaction does NOT reject at 5%
  (joint Wald $F(2,14) = 2.954, p = 0.085$), so the result is
  sensitivity-dependent, with R6 as the stated exception
  ($F(2,10) = 5.818, p = 0.021$). Do not write "conclusive",
  "proved", or "verified stability" here — Chapter V's
  "verified parameter stability" error (Phase 2 item 8) must
  not be reintroduced in Chapter I. State Model 2 df (14) and,
  for completeness, Model 1 df (16) in the same paragraph;
  Chapter I currently states Model 2 df 14 only.
- **Both versions:** the paragraph must be added to .md and .tex.

### 2. Opening violates §3.2 — textbook, then history, puzzle last
- **Rule:** §3.2: do not begin with elementary textbooks or
  historical trivia; hook the economic problem immediately.
  The suggested hook is exactly this thesis's tension: does the
  market keep pricing earnings, or shift to book value, when
  consolidation makes earnings transitory?
- **Evidence (reading order, verified):** §1.1 paragraph 1 is
  generic RIV theory (Ohlson, clean surplus). Paragraph 2 is
  Nepal market history (Securities Exchange Centre 1976,
  NEPSE/SEBON 1993, floor trading 13 January 1994). The
  consolidation-shift puzzle does not arrive until paragraph 4
  ("A central theoretical and empirical issue ... whether the
  valuation relationship ... remains stable across major
  corporate reorganizations").
- **Fix:** Move the paragraph-4 tension to the opening, or
  compress paragraphs 1–2 into a short theoretical anchor
  after the hook. This is a structural reorder, not a factual
  correction — no sentence in paragraphs 1–2 is listed here as
  false (their historical facts are under "NOT verified",
  below). Do not delete the history; relocate it.

### 3. Merger dates cited to (NRB, 2023) — wrong citation, right dates
- **Rule:** §10 rubric item 12 (corporate actions audited
  against primary sources); §4.2 (formal APA citation).
- **Evidence (verified in the Phase 2 loop, re-confirmed here
  in both versions):** §1.2, problem 1, lists all four
  joint-operation dates (GBIME–Bank of Kathmandu 9 January
  2023; HBL–Civil 24 February 2023; KBL–NCC 1 January 2023;
  NIB–Mega forming NIMB 11 January 2023) cited to
  `(NRB, 2023)` alone — in .tex, `\citep{nrb2023list}`.
  That bib entry is the October 2023 list of licensed
  institutions. It cannot support joint-operation dates.
  The dates themselves were verified externally in the loop
  and are correct; only the citation attachment is wrong.
- **Fix:** Cite the bank documents for the dates (as Chapter II
  does for the same mergers), and drop `(NRB, 2023)` from
  this sentence. **Do not** drop it from the §1.1 sentence
  "reduced ... to exactly 20 licensed institutions
  (NRB, 2023)" — a licensed-institutions list DOES support a
  population count, and removing it there would be a
  regression.
- **Both versions:** .md line 26, .tex line 28.

### 4. Sector-dominance sentence: no proportion, citation does not carry it
- **Rule:** §5.1: disclose the proportion of sector assets,
  equity, or market capitalization represented, to substantiate
  sectoral relevance. §4.2: citations must support the claim.
- **Evidence (verified):** §1.1, final sentence of paragraph 2:
  "Class 'A' commercial banks historically commanding the
  largest single share of aggregate market capitalization,
  total annual trading turnover, and public equity ownership
  (Bhattarai, 2014; Pradhan & Dahal, 2016; Timalsina, 2026)."
  No proportion, share, or year is given anywhere in Chapter I.
  And Bhattarai (2014) — read in full in the Phase 2 loop —
  does not establish market-capitalization dominance at all
  (it is a 9-bank price regression study). Pradhan & Dahal
  (2016) and Timalsina (2026) were not verified for this claim
  in this step.
- **Fix (one of the two, not both vaguely):** either (a) give a
  verified proportion with its source and year (e.g., banks'
  share of NEPSE market capitalization in a stated year, from
  NEPSE/SEBON data), or (b) soften the sentence to a sourced,
  proportion-free claim (e.g., banks as a major NEPSE
  component) and remove Bhattarai (2014) from its citations.
  Do not keep "largest single share" on these citations as
  written.

## Minor (verified, fix with the must-fix batch)

### M1. "utilizes" — §7.2 prefers "use"
- One instance, both versions: §1.2, problem 3, "published
  literature predominantly utilizes fiscal-year-end ...
  closing market prices" (.md line 32, .tex line 34).
  Change to "uses". This is the ONLY §7.2 Latinate instance
  found; "facilitate" is 0, "It was observed" is 0.

### M2. Purposive selection hurdles not stated in Chapter I — §5.1
- Chapter I says "five purposively selected" series and names
  the four merged series plus the NMB benchmark, but it never
  lists the selection hurdles the instructions require:
  Class 'A' status; participation vs. benchmark status;
  continuous audited reports across the horizon; verifiable
  prices in the freshness window. Those hurdles belong
  primarily to Chapter III, so this is minor for Chapter I —
  but if Chapter III (next steps) does not list them either,
  it becomes a must-fix there. Do not invent hurdles here;
  carry the check forward.

### M3. "Eight-part robustness suite" wording — settle in Chapter IV step
- §1.7 describes Chapter IV as presenting "the eight-part
  robustness suite", while §1.3 lists six robustness variants
  (ROA, DPS, FY 2079/80 exclusion, FY 2078/79 exclusion,
  bonus-adjusted, restated EPS). Both can be true if "eight"
  counts specifications R1–R8 (baseline + interaction + six
  variants), but Chapter I never says that. Not listed as an
  error: the Chapter IV step must confirm the count against
  T5 before any wording change, or a "fix" here could create
  an inconsistency with Chapter IV.

## Passes — verified compliances (do NOT "fix" these)

These were checked because a careless audit against the
instructions could break them. Each is a pass, with its evidence:

- **Trap 1, circularity (§2, rubric 1): PASS.** Chapter I
  correctly excludes price-derived multiples from its own
  design and correctly identifies the P/E circularity
  ($\text{P/E} = \text{MPS}/\text{EPS}$) in prior studies.
  Its own models use EPS and BVPS only. (Whether every
  prior study listed actually included P/E is a Chapter II
  verification item, not a Chapter I design error.)
- **Trap 2, scale / $R^2$ (§2, rubric 19): PASS.** Chapter I
  makes no $R^2$ claim and no cross-regime $R^2$ comparison.
  It relies, as the instructions require, on interaction
  parameters and the joint Wald test.
- **Trap 3, look-ahead (§2, rubric 2–3): PASS, wording correct.**
  §1.2 problem 3 and §1.5 both say the nine-month BAFIA
  deadline is "operationalized at the end of Chaitra" — the
  correct template. The statute names no month, and Chapter I
  does not claim it does. The 5-day freshness rule is stated
  (§1.5) with missing-not-imputed treatment.
- **Trap 4, small clusters (§2, rubric 7): PASS.** $G = 5$,
  MacKinnon-White HC3, and "exploratory indicators rather
  than definitive asymptotic proofs" are all stated (§1.2
  problem 4, §1.6 limitation 3). Chapter I contains no
  backwards HC3 verb (that error is in Chapters III/IV, not
  here) and no unadjusted-OLS reporting.
- **Trap 5, degrees of freedom (§2, rubric 8): PASS for Model 2.**
  "$28 - 14 = 14$ residual degrees of freedom" is stated
  twice (§1.2 problem 4, §1.6 limitation 3), and the
  parameter count (bank FE + year FE + four slopes = 14)
  matches the instructions' own Trap 5 arithmetic exactly.
  (Model 1 df 16 is not stated in Chapter I — see Must-fix 1,
  where it should be added alongside the findings paragraph,
  not as a standalone correction.)
- **Trap 6, asterisk econometrics (§2, rubric 19): PASS by
  absence, with a condition.** Chapter I reports no
  coefficients, so it cannot commit asterisk-hunting — but
  that is also why Must-fix 1 exists: when the findings
  paragraph is added, it must interpret economic magnitudes
  (rupees of price per rupee of EPS/BVPS, post slopes as
  $\beta + \delta$), not just $p$-values.
- **Trap 7, pseudo-causal creep (§2, rubric 9): PASS.**
  §1.4 states joint-test results are "interpreted strictly
  as observed differences in statistical associations across
  calendar regimes, rather than as causal impacts of bank
  mergers"; §1.6 limitation 4 lists the concurrent
  confounders the instructions require (macroeconomic shifts,
  interest-rate fluctuations, NEPSE broad-index cycles,
  post-pandemic adjustments). "Restructuring induced by the
  2023 consolidation wave" (§1.1) describes the historical
  restructuring itself, not a regression causal effect, and
  is not counted as causal creep.
- **Trap 8, survivorship / truncation (§2, rubric 4, 13): PASS.**
  §1.6 limitation 2 documents BOTH exclusions with exact
  suspension end-dates and lateness (HBL FY 2077/78, until
  6 June 2022, 54 days late; NIB FY 2077/78, until 30 May
  2022, 47 days late), coded missing, not imputed. Clean
  $N = 28$ (13 pre, 15 post) is stated consistently.
- **Hypotheses, objectives, questions map completely: PASS.**
  RQ1 → Objective 1 → H1, H2 (baseline, Model 1). RQ2 →
  Objective 2 → H3, H4 plus the joint null
  ($H_{0,\text{joint}}: \delta_E = \delta_B = 0$). RQ3 →
  Objective 3 → all six robustness variants. All hypotheses
  are two-tailed at $\alpha = 0.05$ without imposed signs,
  as stated. The Phase 2 $H_1$ notation collision is FIXED:
  the joint alternative is now written $H_{a,\text{joint}}$,
  not $H_1$.
- **Fixed since Phase 2 (verified in this version, do not
  re-open):** Kanchan is now "approximately NPR 0.56 billion
  beyond its 13% bonus share distribution" (loop item 16,
  fixed); "No empirical study identified in the literature
  reviewed in Chapter II" (softened, not universal);
  "four of the country's most prominent" (prominence, not a
  largest-mergers ranking); "typically published between
  Ashwin and Poush" plus §1.6 limitation 6's explicit
  "observed corporate practice rather than audited proof"
  disclosure; "established peer institution" (singular, for
  single benchmark NMB); BAFIA audited duty written as
  publication, not submission. Reverting any of these would
  be a regression.
- **AI-slop vocabulary (§7.1, rubric 23): PASS except M1.**
  Grep of the full chapter: delve 0, underscores 0,
  showcasing 0, pivotal 0, testament 0, beacon 0, tapestry 0,
  paramount 0, "game changer" 0, multifaceted 0, myriad 0,
  "it is important to note that" 0. "Robust" occurs 7 times,
  almost entirely as the technical terms (HC3-robust,
  robustness suite) — not slop. No agentless-passive
  "It was observed" and no anthropomorphism ("data speak",
  "regression finds") was found.
- **§8.3 tripartite implications: NOT APPLICABLE to Chapter I.**
  The instructions require three stakeholder domains for
  Chapter V implications. Chapter I §1.5 lists five
  stakeholder groups (investors, bank management, NRB,
  SEBON/NEPSE, researchers) as rationale, not as Chapter V
  implications. Do not "fix" §1.5 down to three domains;
  the tripartite check belongs to the Chapter V step.
- **§6.1 table notes / §9 formatting: OUT OF SCOPE for
  Chapter I prose.** Chapter I contains no regression table.
  Table-note completeness and TU FOM typography/pagination
  are checked in the Chapter IV step and in a compiled-PDF
  step, not here.

## NOT verified in this step — not counted as errors

Deliberately excluded from Must-fix, to be settled in their
own steps with their own sources. Listing any of these as a
Chapter I error now would violate the author's no-slop rule:

- **Problem-statement study summaries (§1.2, paragraph 2):**
  Chhetri (2023) ROA positive-significant; Chaudhari (2025)
  ROA negative-significant; Gyawali (2022) ROA positive-
  insignificant; Joshi et al. (2023) BVPS strong positive;
  Pant et al. (2024) BVPS insignificant negative; Bhandari
  et al. (2026) EPS predominant; Chhetri/Giri EPS negligible
  or secondary. These inherit Chapter II's verification
  status. They are not re-checked here.
- **P/E-inclusion attributions (§1.2, problem 2):** Bhattarai
  (2014) is verified (P/E is in its model — Phase 2 loop,
  full-text read). Chhetri, Giri, Gurung & Dahal, Joshi, and
  Pant attributions are NOT verified in this step; the
  Chapter II step must check each paper's specification
  before any of them is called an error or confirmed.
- **Ashadh-end pricing attributions (§1.2, problem 3):**
  Bhattarai, Pradhan & Dahal, Silwal & Napit — not verified
  in this step; Chapter II step.
- **"Prior studies largely left small-cluster hazards
  unaddressed" (§1.2, problem 4):** a literature claim;
  Chapter II step.
- **Historical institutional facts (§1.1):** 32 licensed banks
  by FY 2011/12; 20 by mid-October 2023; NPR 2.0bn → 8.0bn
  capital mandate (FY 2015/16, two-year window); Securities
  Exchange Centre 1976; NEPSE/SEBON 1993; floor trading
  13 January 1994 (29 Poush 2050 BS); "approved by NRB" as a
  step before publication (§1.2, problem 3). All are cited
  to NRB/Adhikari/NEPSE sources in the text and were not
  independently re-verified in this step. The "approved by
  NRB" phrase is the one to watch in the Chapter II/III
  steps: if NRB approval is not in fact a publication step,
  it becomes an issue then, not now.
- **EPS–ROA collinearity magnitude in §1.5, point 3**
  ($r = 0.975$, "VIF between approximately 20 and 30 depending
  on model specification"): $r = 0.975$ is recomputed-verified
  (Phase 2 loop). The VIF range is not re-verified in this
  step; the Chapter IV step must settle it against T6
  (bivariate VIF from $r$ alone is 20.25) before the wording
  is changed.
- **§1.7 "eight-part robustness suite":** see Minor M3.
- **Citations in Chapter I as a system:** no full
  bibliography audit was done in this step (that was done
  for LaTeX in the Phase 2 loop: 55/55, Dahal 2025 the only
  gap, now to be re-checked after the 8c96edc bib addition
  of 19 lines in the Chapter II step).

## Scope limits of this Chapter I review

- No thesis, table, figure, or data file was changed.
- No compiled PDF was proofread; TU FOM margins, typeface,
  spacing, and pagination (§9) are not certified here.
- No new online source was needed for the must-fix items:
  Must-fix 1–4 rest on the instructions text itself, on
  grep evidence from Chapter I, and on verifications already
  recorded in the Phase 2 loop (merger dates, Bhattarai
  full text, panel arithmetic). The unverified items above
  were left unverified on purpose, for their own steps.
- Next step, in the author's order: Chapter II, against the
  same instructions, starting with the literature
  attributions listed above as unverified.
