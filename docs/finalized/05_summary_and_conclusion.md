# Finalized review — Chapter V: Summary, Conclusion, and Implications, audited against docs/instructions

**Thesis version audited:** HEAD 8c96edc (pulled 2026-10-29).
Files checked, both versions:
`docs/draft/thesis/chapter_05_summary_and_conclusion.md` and
`src/thesis/chapters/chapter_05_summary_and_conclusion.tex`,
plus Chapter IV tables (T3/T4/T5) for every number Chapter V
repeats.
**Thesis files changed to write this review: NONE.** Applying any
fix still needs the author's approval, in both versions where the
passage appears in both.

**Standard applied:** `docs/instructions/instructions_for_paper.md`
— §8 Chapter V rules (§8.1 answer RQs directly, §8.2 formal
hypothesis decision table, §8.3 exactly three implication
domains), §2 traps (Trap 6 asterisk econometrics, Trap 7
causal language), §7 prose rules, §10 rubric. The instructions'
illustrative numbers (§6.2, §8.2) are NOT thesis numbers and
were not used as a check standard here.

## How this chapter was checked, so it can be re-checked

1. Read Chapter V in full, both versions, section by section.
2. Re-checked every Phase 2 Chapter V must-fix and minor
   against the 8c96edc text — most are now fixed (see Passes);
   one flagged phrase survives in a different section.
3. Checked every repeated number against Chapter IV / T3–T5
   (descriptives, Model 1/2, joint Wald, R6, R4 df, pooled
   comparison, correlations, VIF).
4. Grep-verified presence/absence claims (Hypothesis count,
   "universally", "verified parameter", "during merger
   processes", prohibited words, implication headings).
5. Anything not verified in this step is listed under
   "NOT verified — not counted as errors", not under
   Must-fix.

## Verdict for Chapter V

Chapter V is numerically faithful and its conclusions are now
honest — the sensitivity-dependent framing, the formal
hypothesis decisions, and the "almost all" scope are all fixed.
But it fails the instructions' Chapter V structure in two
explicit ways, and one Phase 2 phrase survives in the
implications section. Those three items are the must-fix list.
Everything else is minor.

## Must-fix (verified)

### 1. Implications are partitioned into five domains, not the exactly three §8.3 requires
- **Rule:** §8.3: "Partition implications into exactly
  three domains: investors; bank executives/boards;
  regulators (NRB, SEBON, NEPSE)."
- **Evidence (verified by headings):** §5.4 has five
  subsections: 5.4.1 Regulatory Authorities (NRB),
  5.4.2 Securities Market Regulators and Exchanges
  (SEBON and NEPSE), 5.4.3 Commercial Bank Executives
  and Boards, 5.4.4 Equity Investors / Analysts /
  Market Participants, 5.4.5 Academic Researchers and
  Accounting Standard Setters. §5.1's intro lists four
  groups (regulators, executives, investors, standard
  setters) — also not three, and inconsistent with §5.4's
  five.
- **Fix (structure only — preserve the substance):**
  merge 5.4.1 + 5.4.2 into one "Regulators (NRB, SEBON,
  NEPSE)" domain (NRB items, then SEBON/NEPSE items, in
  that order); keep 5.4.3 as executives/boards and 5.4.4
  as investors; move 5.4.5's academic-researcher material
  into §5.5 (future research, where it belongs) and its
  standard-setter recommendation (uniform NFRS restatement
  disclosure) into the Regulators domain. Update §5.1's
  intro list to the same three domains. Do NOT delete
  any implication to force the count — repartition them.
- **Why this is must-fix, not a preference:** §8.3 says
  "exactly three". Five is not a rounding difference.

### 2. §8.2 requires a formal hypothesis decision TABLE; Chapter V gives a list
- **Rule:** §8.2: Chapter V must "include a formal
  hypothesis decision table" (the instructions' example
  table has Hypothesis / Parameter / Estimate / Decision
  columns, with the joint test as its own row).
- **Evidence:** §5.3.5, "Formal Decisions on Research
  Hypotheses", is a five-item numbered LIST (H1, H2, H3,
  H4, joint test). Its substance is correct (see Passes)
  — every estimate, p-value, and decision matches
  Chapter IV Table 4.5 — but it is not a table, and a
  reader following the instructions' Chapter V checklist
  will look for a table and not find one.
- **Fix:** Convert §5.3.5's list into a summary table
  (columns: Hypothesis, Parameter/Model, Null, Estimate,
  p-value, Decision at α = 0.05), with the joint test as
  its own row, matching Table 4.5's values exactly.
  The list's prose sentences can be kept as the table's
  accompanying text, or cut once the table carries them.
  Do not change any estimate or decision in the conversion.

### 3. "During merger processes" survives in §5.4.2 — the exact Phase 2 phrase
- **Rule:** Phase 2 loop item 17 (still governing until
  fixed): the HBL/NIB suspension must be described as
  "merger-related", because the HBL–NIB merger was
  REJECTED at HBL's 29th AGM in January 2022, months
  before the April–June 2022 suspension window.
- **Evidence (grep-verified, both versions):** §5.4.2,
  point 1 (.md line 130, .tex line 151): "the extended
  suspension of secondary market trading during merger
  processes, which froze trading for up to 54 days past
  statutory reporting deadlines."
- **Fix:** Change to "merger-related trading suspensions"
  — the exact wording already used in §5.2.2 of this
  chapter ("prolonged merger-related secondary market
  trading suspensions around the April 2022 deadline")
  and in Chapters III–IV. The "up to 54 days" figure is
  correct (HBL, 6 June 2022) and must stay.
- **Note:** §5.5.1, point 2 ("trading halts during
  corporate combinations") is generic future policy, not
  the HBL/NIB event, and is NOT flagged.

## Minor (verified, fix with the must-fix batch)

### M1. RQ answers are present in substance but not labelled RQ1/RQ2/RQ3 in §5.3
- §8.1 requires Chapter V to "answer each research
  question directly". §5.2.1 lists the three research
  questions; §5.3 answers them in substance (RQ1: H1/H2
  fail to reject, §5.3.5 items 1–2; RQ2: joint baseline
  fail, R6 reject, §5.3.1/§5.3.5 item 5; RQ3: sensitivity
  suite, §5.2.3 items 5–6 and §5.3.4) — but §5.3 never
  names "RQ1", "RQ2", or "RQ3", so the mapping is left
  to the reader. Fix: add explicit RQ labels to the
  §5.3.1/§5.3.4/§5.3.5 headings or a short three-line
  RQ-answer paragraph at the head of §5.3. Not a
  must-fix, because no RQ is left unanswered in substance.

### M2. "Fragmented corporate disclosures" premise in §5.4.2 is still uncited
- §5.4.2, point 2: "To eliminate fragmented corporate
  disclosures and ensure uniform public access, SEBON
  and NEPSE should operationalize a centralized
  electronic disclosure portal..."
- This replaces the old Phase 2 premise ("public
  dissemination remains dispersed across corporate
  websites and print media", which had no supporting
  passage anywhere in Chapters I–IV). The new wording
  is softer and generic, but "fragmented" as an existing
  fact is still uncited. Fix: cite a SEBON/NEPSE
  disclosure-practice source, or rephrase as a proposal
  ("A centralized portal would reduce fragmentation
  risk") rather than as an existing condition. Not a
  must-fix, because it is a recommendation rationale, not
  a result — but it will be read as a factual premise
  unless cited or softened. (This replaces, and does not
  reopen, the old "dispersed dissemination" item: the
  old specific channels claim is gone.)

### M3. "Eight-part robustness suite" naming (cross-reference)
- §5.2.1, objective (iii), and §5.2.3, point 5, call
  R1–R8 an "eight-part robustness suite". As in
  Chapters III–IV: R1/R2 are baselines, R3–R8 are the
  six robustness variants. Fix in step with Chapters
  III–IV to "eight-specification suite". All n and df
  in §5.2.3 are correct — naming only.

### M4. Identification phrase, same as Chapters III–IV
- §5.3.3: "slope coefficients are identified strictly
  from within-year cross-sectional differentiation."
  Add the bank-demeaning qualifier ("after removing bank
  means") as in Chapter III, Minor M5 / Chapter IV.
  The model equations in §5.2.2 are correct; wording only.

### M5. VIF "≈ 20–30" again (cross-reference)
- §5.2.3, point 2: "catastrophic multicollinearity
  ($\text{VIF} \approx 20\text{--}30$)". Same uncomputed
  upper bound as Chapters III–IV and T2. Fix in step
  with those chapters: exact bivariate ≈ 20.3, or a
  computed FE-conditioned figure. No estimate depends
  on it (EPS and ROA are never co-included).

### M6. "Utilize" — §7.2 prefers "use"
- One verified instance, §5.4.4, point 2: "Valuation
  models should utilize normalized operational metrics".
  Change to "should use". (Grep count for utilize-forms
  in the chapter: 1.)

## Passes — verified compliances, including Phase 2 items now fixed (do NOT re-open)

- **"Verified parameter stability": FIXED.** The phrase
  appears 0 times by grep. §5.2.3, point 5 now reads:
  "The robustness suite (R1–R8) did not reject parameter
  stability at the 5% level across ROA substitution (R3),
  cash dividend inclusion (R4, residual df = 13),
  transition-year removal (R5), bonus share dilution
  (R7), and restated basic earnings (R8), except under
  Specification R6..., where the joint Wald test rejected
  parameter stability." §5.3.1 and §5.3.5 item 5 both
  state the evidence is "sensitivity-dependent rather
  than conclusive in the baseline" and "documented as an
  empirical association across calendar periods, rather
  than as an established causal merger impact". The
  contradiction that made the old wording a must-fix
  is gone.
- **H1–H4 by name: FIXED.** "Hypothesis" appears 13 times
  by grep (was 0 in the Phase 2 loop). §5.3.5 decides
  H1 (β_E, Model 1 2.095 p = 0.616; Model 2 pre 5.577
  p = 0.140 — fail to reject), H2 (β_B, 0.219 p = 0.908;
  pre 0.100 p = 0.940 — fail to reject), H3 (δ_E −3.124
  p = 0.448 — fail to reject), H4 (δ_B −1.758 p = 0.175
  — fail to reject), and the joint test (baseline
  F(2,14) = 2.954 p = 0.085 fail; R6 F(2,10) = 5.82
  p = 0.021 reject) — all matching Chapter IV Table 4.5.
  (Format is Must-fix 2; substance is a pass.)
- **"Universally": FIXED.** 0 occurrences by grep.
  §5.2.1, gap 1, now reads "Almost all published
  Nepalese studies employed static, full-sample pooled
  regressions" — matching Chapter I's "almost all".
- **"During merger processes" in §5.2.2: FIXED.**
  §5.2.2 now reads "prolonged merger-related secondary
  market trading suspensions around the April 2022
  deadline" with correct 54-day (HBL) and 47-day (NIMB)
  lateness. Only the §5.4.2 instance (Must-fix 3) survives.
- **Numbers: PASS (all repeated values match Chapter IV).**
  Descriptives (254.34; 310.59 → 205.60, −33.80%;
  SD 119.46 → 33.45, −72.00%; EPS 17.90 → 10.72,
  −40.11%, SD 3.99 → 6.53, +63.66%; DPS 6.06 → 1.40,
  −76.90%, 12/15 zero; BVPS 158.11 → 161.97, +2.44%);
  correlations (EPS–ROA 0.975, EPS–BVPS 0.372
  p = 0.051, VIF 1.16); Model 1 (2.095 / 0.219,
  R² 0.948, adj 0.912, df 16, pooled R² 0.136);
  Model 2 (pre 5.577 / 0.100, δ −3.124 / −1.758,
  post 2.453 / −1.658, joint F(2,14) = 2.954
  p = 0.085); R6 (F(2,10) = 5.82 p = 0.021, N = 23,
  δ_B −2.611 SE 1.517 p = 0.116); R4 df 13; pooled
  EPS 4.882 (t = 1.58 p = 0.126); df 28−12 = 16 and
  28−14 = 14. No number drift in Chapter V.
- **BAFIA wording in Chapter V: PASS.** §5.2.2:
  "legally mandates that commercial banks publish their
  audited annual balance sheets and profit and loss
  accounts within nine months into the subsequent fiscal
  year—operationalized at the end of Chaitra (mid-April)".
  This is the correct template (statutory nine months +
  operationalization), unlike the Chapter IV spots in
  Minor M2 of that chapter's review.
- **Kanchan in Chapter V: PASS.** §5.2.2: "adding
  approximately NPR 0.56 billion beyond its 13% bonus
  share distribution to share capital in FY 2077/78" —
  matches the panel arithmetic and Chapters II–III.
- **Causal language in conclusions: PASS.** §5.3.1:
  "documented as an empirical association across calendar
  periods, rather than as an established causal merger
  impact." §5.3.2: the negative BVPS point estimate is
  qualified as "though statistically insignificant at
  p = 0.161" and introduced as "A plausible economic
  interpretation". No conclusion claims a causal merger
  effect.
- **Trap 2 (R²): PASS.** §5.2.3, point 3, and §5.3.3
  both use R² (0.948 vs. pooled 0.136) to show how much
  variation year effects absorb, never as evidence that
  the slopes are significant — and both state the slopes
  are insignificant in the same passages.
- **Prose, §7.1: PASS except M6.** Grep: delve 0,
  pivotal 0, testament 0, beacon 0, tapestry 0,
  paramount 0, "game changer" 0, multifaceted 0,
  myriad 0, "it is important to note that" 0,
  facilitate 0.

## NOT verified in this step — not counted as errors

- **Sector-dominance sentence (§5.2.1):** "historically
  accounting for the largest share of aggregate market
  capitalization, annual trading turnover, and retail
  investor participation (Pradhan & Dahal, 2016;
  Timalsina, 2026)". The old Bhattarai citation for this
  claim was proven wrong in the Phase 2 loop and is now
  gone from this sentence. Whether Pradhan & Dahal
  (2016) or Timalsina (2026) establish the dominance
  claim — and what proportion, in what year — was NOT
  verified against full texts in this step, so it is
  listed here, not as an error. **Carry-over:** when
  Chapter I, Must-fix 4, is fixed with a verified
  proportion and source, propagate that exact wording
  and citation to this §5.2.1 sentence, or the two
  chapters will contradict each other.
- **Gap attributions in §5.2.1 (points 1–4):** "almost
  all ... static pooled", P/E lists (Bhattarai, Giri,
  Joshi, Pant), Ashadh-end practice, small-cluster
  neglect — these repeat Chapter II's gap claims, which
  were checked for internal consistency (not full-text
  verification for every study) in the Chapter II step.
  Not re-verified here.
- **Implication premises (§5.4.1–5.4.4):** AQR
  usefulness, dividend-anchor loss, goodwill/goodwill
  composition of post-merger book equity, macro-temporal
  dominance of prices — these are interpretations and
  recommendations, explicitly framed as such, not
  estimated results. Their factual premises (DPS zeros,
  book-equity expansion, year-effect R²) are
  panel-verified; the policy link is normative, not a
  tested claim.
- **Future-research feasibility (§5.5.2):** DiD with all
  20 banks, intraday event studies, ESG value relevance —
  stated as avenues, not as findings; no feasibility
  claim was checked.

## Scope limits of this Chapter V review

- No thesis, table, figure, code, or data file was changed.
- No compiled PDF was proofread; TU FOM formatting (§9)
  is not certified here.
- **This completes the finalized review, Chapters I–V.**
  Consolidated next step, in the author's order: apply
  the fixes only on his approval, in both Markdown and
  LaTeX where the passage appears in both, and in the
  bib where the error is in the bib (Chapter II,
  Must-fix 1). Chapter-by-chapter must-fix counts:
  Ch I 4, Ch II 4, Ch III 1, Ch IV 0, Ch V 3 — 12 total,
  plus minors (Ch I 3, Ch II 4, Ch III 5, Ch IV 7,
  Ch V 6 — 25 total). The Chapter I and Chapter II
  must-fix lists, and the Chapter V §8 structure items,
  are the ones that change what an examiner will conclude
  about the thesis; the rest are wording precision.
