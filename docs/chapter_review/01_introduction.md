# Chapter review: Chapter I — Introduction

- Chapter reviewed, in full: `docs/draft/thesis/chapter_01_introduction.md` (158 lines)
- Repository HEAD at review time: `9a46350`
- LaTeX counterpart, spot-checked only (see Pass 5): `src/thesis/chapters/chapter_01_introduction.tex`
- Evidence sources used: `docs/draft/thesis/chapter_03_research_methodology.md`,
  `chapter_04_results_and_discussion.md`, `chapter_05_summary_and_conclusion.md`,
  `data_analysis/analysis/outputs/tables/T1_descriptives.md`,
  `T3_model1.md`, `T4_model2.md`, `T5_robustness.md`, `T6_diagnostics.md`,
  `A5_specification_comparison.md` (and `A4_price_verification.md` for the price
  definition), `data_analysis/data_extract/output/tidy/accounting_panel.csv`,
  `data_analysis/data_extract/output/manual_review/mps_rd_dps_announcement_dates.csv`,
  plus public web checks for the NEPSE/NRB history dates in section 1.1 only
  (see "Correct" and "NOT checked" below).
- This review changed nothing in the thesis. It is a review file only.
- Line numbers below are lines of `chapter_01_introduction.md`.
  Quotations are verbatim, including punctuation.

## Passes run (as instructed, as a loop)

- **Pass 1 — argument and promise check:** every objective, question, hypothesis,
  significance claim, and limitation was compared with what Chapters 3–4 and
  tables T1–T6/A5 actually do and report.
- **Pass 2 — line-by-line proofread:** grammar, duplicated words, broken
  sentences, terminology, and consistency of period dates, bank names, and
  MPS vs MPS_RD.
- **Pass 3 — numbers, dates, and facts:** every number and date in Chapter 1
  was checked against the panel, the tables, Chapters 3–5, or, for the
  section 1.1 institutional history only, public sources. Anything that
  could not be verified from those sources is flagged as unverified, not
  asserted to be false.
- **Pass 4 — slop hunt:** meta comments about the dissertation itself,
  filler, promotion, and repetition. Each quoted item is one I read in full
  context; a sentence is listed only if deleting or shortening it loses
  nothing, or if it overstates what the thesis delivers.
- **Pass 5 — LaTeX sync, spot-check only:** the passages flagged below were
  searched in the `.tex` version. This was NOT a full Markdown-to-LaTeX diff,
  and no claim is made that the two versions are otherwise identical.

## Short verdict

**Pass with fixes.** The chapter's skeleton is sound: the five bank series,
the six fiscal years, the pre/post split, the two models, the four
hypotheses plus the joint test, the eight-run robustness suite, the
sample of 28, and the limitations all match Chapters 3–4 and the tables.
No number that Chapter 1 itself reports about its own design is wrong
(see "Correct"). The must-fix items are not data errors. They are
over-wide literature claims, one publication-window claim contradicted
by the thesis's own announcement file, and significance language that
promises more than the non-significant baseline results in Chapter 4
deliver. Fix those, plus the one wording flaw carried over from the
data review, and the chapter is defensible. It does not need rework.

## Correct — verified, briefly (so the absence of an issue is not mistaken for a missed check)

- Sample and periods. Line 131: "reducing the clean estimation sample
  to $N = 28$ observations (13 pre-consolidation, 15 post-consolidation)"
  matches T1 (full 28, pre 13, post 15) and the panel (30 rows, 2
  window-excluded: HBL and NIMB FY2077/78).
- Suspension gaps. Line 131: HBL "54 days late", NIMB "47 days late",
  resumption 6 June 2022 and 30 May 2022 — matches Chapter 3 and the
  joined panel gaps (54 and 47).
- Degrees of freedom. Line 35 and line 134: "$28 - 14 = 14$ residual
  degrees of freedom" for Model 2, and $G = 5$ clusters — matches T4
  (df 14) and the model formulas in Chapter 3 (intercept + 4 bank
  dummies + 5 year dummies + 4 slopes = 14 parameters).
- Hypotheses and joint test. Lines 63–96: H1/H2 as Model 1 slopes
  $\beta_E = 0$, $\beta_B = 0$; H3/H4 as interaction differences
  $\delta_E = 0$, $\delta_B = 0$; joint $H_0: \delta_E = 0$ and
  $\delta_B = 0$, two-tailed at 5% — matches T3, T4, and Chapter 4
  (joint $F(2, 14) = 2.954$, $p = 0.085$, fail to reject at 5%).
  The non-causal caveat on line 96 ("interpreted strictly as observed
  differences in statistical associations across calendar regimes,
  rather than as causal impacts of bank mergers") matches Chapter 4
  and Chapter 5 and is the correct framing. No causal merger-effect
  claim is made in Chapter 1's hypothesis section.
- Objectives and robustness. Lines 45–59: the six sensitivity items
  (ROA substitution, DPS, exclude FY2079/80, exclude FY2078/79,
  bonus-adjusted, restated EPS) are exactly R3–R8 in T5; with the two
  baseline/interaction models they make the eight-run suite that
  Chapter 3 and section 1.7 describe. Research Questions 1–3 (lines
  39–41) map onto objectives 1–3 without adding a question the
  thesis does not answer.
- Merger dates and NMB status. Line 26: GBIME–Bank of Kathmandu
  9 January 2023, HBL–Civil 24 February 2023, KBL–NCC 1 January 2023,
  NIB–Mega 11 January 2023 — consistent with Chapter 3 and the
  panel's merger record. Line 11's statement that NMB "did not
  undergo horizontal amalgamation during the 2022–2023 consolidation
  wave" is correct for that wave; its 2020 Kanchan acquisition is
  disclosed in the same sentence (see MINOR-7 for the wording
  ambiguity about the 0.57 billion figure).
- Institutional history, broadly. Line 9: 32 banks by FY2011/12,
  Merger Bylaws 2011, capital mandate NPR 2.0 billion to NPR 8.0
  billion in Monetary Policy FY2015/16 within two years, and 32 to
  20 banks overall — all consistent with public NRB reporting
  found in the web check for this review (32 by mid-June 2012;
  2 billion to 8 billion by mid-July 2017). The exact "mid-October
  2023 (Asoj 2080)" dating of the 20-bank count rests on the
  cited NRB (2023) source and was not independently verified to
  the month in this review (see NOT checked).
- NEPSE history. Line 7: Securities Exchange Centre 1976,
  conversion to NEPSE in 1993, trading floor 13 January 1994 —
  consistent with public NEPSE-history sources found in the web
  check. The BS conversions (2033 BS, 29 Poush 2050 BS) were not
  independently day-checked and are carried on the cited
  NEPSE (2017) source (see NOT checked).
- Terminology. Chapter 1 uses MPS for prior studies' dependent
  variable and MPS_RD for this study's post-reporting-deadline
  price, and does not label any Ashadh-end, year-end, or
  reporting-deadline price as MPS_post. No MPS_post claim appears
  in this chapter. No dataset close is presented as a NEPSE
  official close in this chapter.
- Proofread. No duplicated-word typo (e.g. "the the") and no
  broken sentence was found on the full read. Bank names and
  abbreviations (GBIME, HBL, KBL, NIMB, NMB) are used consistently,
  and the pre/post period dates (FY2076/77–2078/79 and
  FY2079/80–2081/82) are the same everywhere they appear.

## MUST-FIX

### MUST-1 — Universal literature claim: "no empirical study in Nepal has formally evaluated…"
Line 26, verbatim:

> "To date, no empirical study in Nepal has formally evaluated whether the valuation coefficients of EPS and BVPS shifted between the pre-consolidation (FY 2076/77–2078/79) and post-consolidation (FY 2079/80–2081/82) periods using an explicit regime-interaction econometric framework."

Why it must fix: this is a universal negative. Nothing in the
evidence sources for this review proves that no study anywhere
has done this, and Chapter 2 was not in this review's evidence
set, so this review cannot verify the absence either. An examiner
needs only one counterexample. Fix: soften to what the thesis
actually did — "No study identified in the literature reviewed
in Chapter II has formally evaluated…" — and make Chapter 2
carry the search that justifies even that version. The same
softening applies to the grouped quantifiers in MUST-2.

### MUST-2 — Over-wide quantifiers about "almost all" / "most" / "routinely" prior studies
Lines 13, 26, 29, 32, 35, verbatim in part:

> "existing empirical research on Nepalese commercial banking valuation has almost exclusively focused on static, sample-average regressions" (line 13)
> "Almost all published Nepalese studies employ pooled OLS or static panel regression designs" (line 26)
> "A widespread practice in existing Nepalese banking literature is the inclusion of the price-earnings (P/E) ratio alongside fundamental accounting variables" (line 29)
> "Most published studies utilize fiscal-year-end (Ashadh-end / mid-July) closing market prices or annual volume-weighted average prices" (line 32)
> "Previous research in Nepal has routinely ignored these inferential hazards" (line 35)

Why it must fix: each of these is presented as a fact about the
whole Nepalese literature, but the cited lists name only a
handful of studies, and the original papers were not in this
review's evidence set. The P/E and Ashadh-end criticisms may
well be right for the named studies, but "almost all", "most",
and "routinely" go beyond the named evidence. Fix: restrict
every such sentence to the studies actually reviewed, e.g.
"Among the studies reviewed in Chapter II…", or add the
Chapter 2 audit that counts how many of the reviewed studies
do each thing. Do not delete the criticisms — they motivate
the design — but do not let them claim the whole literature
on the strength of a partial list. This is a wording fix, not
a finding that any named study is misdescribed; misdescription
of an individual named study, if any, is in NOT checked.

### MUST-3 — "Four of the five largest banking mergers" — ranking with no ranking evidence
Line 26, verbatim:

> "between January and February 2023, four of the five largest banking mergers in recent Nepalese history commenced joint operations"

Why it must fix: Chapter 1 gives no ranking (by assets, capital,
branches, or any other measure) that puts these four among the
five largest, and line 11 calls the same four only "four of the
country's most prominent commercial banking series". "Largest"
is a stronger, measurable claim than "prominent". Fix: use the
line 11 wording here too — "four prominent commercial banking
series" — or cite a ranking source that actually ranks them.
The four merger dates in the same sentence are correct and
need no change.

### MUST-4 — Board publication window stated flatly, and contradicted by the thesis's own announcement file
Line 108, verbatim:

> "In actual banking practice, commercial bank boards publish audited financial highlights and dividend recommendations between Ashwin and Poush (October to January), with formal AGM approval preceding the Chaitra statutory ceiling."

Why it must fix: (a) The thesis's own DPS announcement file
(`mps_rd_dps_announcement_dates.csv`, 30 rows) has 29 rows in
September–January and one row outside that window: NIMB
FY2079/80, dividend declaration dated 2024-02-02 (Magh).
"Between Ashwin and Poush" as a flat statement is therefore
not true of every observation in the thesis's own file.
(b) More importantly, that file records dividend declarations
and AGM dates, not audited-highlights publication dates, so
it does not prove the audited-highlights window either.
Line 143 already hedges the same point correctly ("typically
released… this pattern reflects observed corporate practice
rather than audited proof of disclosure timing for every
individual observation"). Fix: make line 108 match line 143 —
"typically", "in the disclosures examined", and no claim that
AGM approval always precedes the Chaitra ceiling. The Chaitra
deadline argument itself does not need this window claim at
all: the design rests on the statutory deadline, not on
boards publishing in Ashwin–Poush, so the sentence can also
simply be deleted with no loss to the argument.

### MUST-5 — Significance language promises more than Chapter 4 delivers
Lines 102, 115, 117, verbatim in part:

> "As Nepal's commercial banking sector emerges from the most extensive structural consolidation wave in its history, understanding how capital markets perceive and price accounting disclosures is critical…" (line 102)
> "Equips investors on NEPSE with empirical evidence regarding the relative reliability of earnings versus book values when valuing consolidated financial institutions" (line 115)
> "Provides the central bank with empirical feedback on how capital markets evaluate institutions that underwent policy-driven consolidation" (line 117)

Why it must fix: Chapter 4's baseline results are
non-significant at 5% — Model 1 EPS $p = 0.616$, BVPS
$p = 0.908$ (T3); Model 2 interactions $p = 0.448$ and
$p = 0.175$, joint Wald $p = 0.085$ (T4), i.e. fail to reject
at 5%. Chapter 1 may describe the study's purpose, but it
must not present the findings as if they already establish
reliable earnings-versus-book-value guidance for investors
or feedback for NRB. Fix: temper section 1.5 to the actual
outcome — exploratory, non-significant-at-5% associations,
sensitivity-dependent at best (R6 only) — and delete or
soften "most extensive … in its history" (line 102), which
is a superlative with no comparison to earlier waves in
Chapter 1. The stakeholder bullets can stay if they are
framed as what the study was designed to inform, not what
its results prove.

### MUST-6 — "Six to nine months later" contradicts the same paragraph's October–January window
Line 108, verbatim in part:

> "the study resolves the persistent temporal flaw of prior Nepalese studies that paired Ashadh-end market prices with financial reports published six to nine months later. In actual banking practice, commercial bank boards publish audited financial highlights and dividend recommendations between Ashwin and Poush (October to January)…"

Why it must fix: Ashadh-end is mid-July. October–January
publication is three to six months later, not six to nine.
Six to nine months reaches the Chaitra statutory ceiling
(mid-April), which is a deadline, not the publication date
the same paragraph asserts. Fix: write "published up to
nine months later, by the Chaitra statutory ceiling" if
the ceiling is meant, or "three to six months later" if
the October–January practice is meant. Do not leave both
numbers standing in the same paragraph for the same lag.
This is a minor numerical inconsistency in wording, but
it sits in the chapter's central methodological justification,
so it is classified must-fix rather than minor.

## MINOR

### MINOR-1 — Notation collision: H1 means two different things
Lines 70–96: Hypothesis 1 is labelled ($H_1$) and its
alternative is also labelled ($H_1$), while the joint
alternative on line 94–96 is again $H_1$. A reader cannot
tell from the symbol alone whether $H_1$ means "Hypothesis
1's alternative" or "the joint alternative". Fix: label
alternatives $H_{a,1}$ … $H_{a,4}$ and the joint alternative
$H_{a,\text{joint}}$ (or equivalent), keeping $H_1$–$H_4$
for the hypotheses themselves. Meaning is recoverable from
context, so this is minor, but an examiner will notice it.

### MINOR-2 — "Huber-White cluster estimators" conflates two estimators
Line 35, verbatim in part:

> "standard cluster-robust standard errors (such as Huber-White cluster estimators) perform poorly… when the number of clusters is small ($G = 5$)"

Fix: Huber–White is the heteroskedasticity-robust sandwich;
cluster-robust is its clustered generalisation, and the
cited authority for small-cluster failure is Cameron,
Gelbach, & Miller (2008), not Huber–White. Write
"standard cluster-robust (sandwich) standard errors" and
drop the Huber–White attribution for the cluster case.
The $G = 5$ point itself and the HC3 choice are correct.

### MINOR-3 — "Confirm" overstates what a two-tailed test at 5% can do
Line 63, verbatim in part:

> "all hypotheses are tested two-tailed at the 5% level of significance ($\alpha = 0.05$) without imposing directional signs, thereby allowing the empirical data to confirm or refute the theoretical predictions."

Fix: "confirm" → "support or fail to support". A
non-rejection does not confirm a theory, and Chapter 1
itself correctly says elsewhere that results are
associations, not proofs.

### MINOR-4 — Plural "peer institutions" for a single benchmark
Line 11, verbatim in part:

> "Concurrently, established peer institutions such as NMB Bank Limited (NMB) maintained operational continuity…"

Fix: "institution" (singular) or "peer series", since NMB
is the only benchmark series in the sample. The substance
— NMB did not merge in the 2022–2023 wave — is correct.

### MINOR-5 — "Escalate" and "rigid" in the capital-mandate sentence
Line 9, verbatim in part:

> "requiring all Class 'A' commercial banks to escalate their minimum paid-up equity capital from NPR 2.0 billion to NPR 8.0 billion within a rigid two-year window"

Fix: "escalate" → "increase"; delete "rigid" (it adds
emphasis, not information). The numbers and the two-year
window are correct.

### MINOR-6 — Vague metaphor: "crossed a major merger boundary"
Line 11, verbatim in part:

> "four of the country's most prominent commercial banking series… crossed a major merger boundary between January and February 2023"

Fix: replace with the plain fact Chapter 1 already states
on line 26 — the four series commenced joint operations
with their merger partners in January–February 2023.
"Boundary" is doing no analytical work here.

### MINOR-7 — NMB Kanchan figure is ambiguous, not wrong
Line 11, verbatim in part:

> "Although NMB had previously acquired Kanchan Development Bank Limited in August 2020 (adding approximately NPR 0.57 billion to its equity base in FY 2077/78)"

Check: the panel shows NMB share capital rising from
NPR 13,950,987,467 (FY2076/77) to NPR 16,325,960,853
(FY2077/78), a total rise of about NPR 2.37 billion, of
which about NPR 0.57 billion is the amount beyond the
13% bonus issue and attributable to the Kanchan
acquisition. The 0.57 billion figure is therefore
defensible as the acquisition contribution, but the
sentence as written can be read as the total addition.
Fix: write "adding approximately NPR 0.57 billion beyond
the 13% bonus issue" (if that is the intended meaning)
so the reader cannot mistake it for the total rise.

### MINOR-8 — Promotional slop in the significance section
Line 108, verbatim in part:

> "establishes a clean methodological benchmark for capital market research in Nepal."

Line 111, verbatim in part:

> "this study restores mathematical and statistical integrity to the empirical modeling."

Line 102, item 1 (paraphrased in the quote below is the
verbatim sentence):

> "It moves the Nepalese empirical literature beyond routine, descriptive ratio regressions into formal accounting valuation theory."

Why minor, not must-fix: none of these is a number or a
factual claim about the data, but none of them earns its
place either. "Benchmark" is unproven (no adoption is
shown), "restores integrity" is praise for the author's
own design, and "routine, descriptive" dismisses the
literature Chapter 1 is supposed to be engaging with.
Fix: delete all three sentences or replace each with a
plain statement of what was done ("The study excludes
price-derived multiples and uses HC3 inference with
$t$ on residual degrees of freedom").

### MINOR-9 — Repetition: the same three points appear in three places
- Degrees-of-freedom / $G = 5$ / HC3: line 35 (problem
  statement, item 4) and line 134 (limitations, item 3),
  in near-identical terms. Repetition between a problem
  statement and a limitations section is conventional, so
  this is not counted as slop, but one of the two passages
  can be shortened to a cross-reference with no loss.
- BAFIA / Chaitra deadline: line 32, line 108, and line
  143. Same advice: keep the full statement once (line 32),
  shorten the later two to "the Chaitra deadline defined
  in section 1.2".
- Ohlson framework: line 5 (background), lines 63–64
  (hypotheses anchor), and section 1.5 item 1. This
  repetition is functional (theory, then hypotheses,
  then contribution) and is not flagged for deletion.

### MINOR-10 — "Strict compliance" / "strict" / "complete" claims are not audited in this review
Line 149, verbatim in part:

> "structured in strict compliance with the *Master's Degree Dissertation Guidelines (2019)* of the Faculty of Management, Tribhuvan University"

Line 157, verbatim in part:

> "a complete **References** section compiled in strict APA 6th edition format provides full bibliographic details for all cited literature, statutes, and reports."

Fix: soften "strict compliance" and "complete … strict"
to "in accordance with" and "in APA 6th edition format"
unless a separate guidelines-and-bibliography audit has
actually checked every guideline item and every reference
entry. The LaTeX main file does state APA 6th edition
and the bibliography file contains 55 entries, but this
review did not audit them entry by entry (see NOT checked),
so Chapter 1 should not claim a strictness it has not
demonstrated here.

### MINOR-11 — Section 1.7 is meta by design, and that is acceptable
Line 149–157 (the whole "Organization of the Study"
section) is, by definition, writing about the dissertation
itself. It is not counted as slop: the cited Faculty of
Management guidelines require an organization section, and
its chapter summaries match Chapters 2–5 as spot-checked
(signaling and agency in Chapter 2; eight-part suite in
Chapter 3; VIF, Breusch–Pagan, Cook's distance, and
normality diagnostics in Chapter 4). Two filler words
can still go: "comprehensive" (line 149, "five
comprehensive chapters") and "in-depth academic discussion"
in the Chapter IV bullet — delete both adjectives; the
content of the bullets is what matters.

## Pass 5 — LaTeX sync (spot-check only, NOT a full diff)

The following flagged passages were found in
`src/thesis/chapters/chapter_01_introduction.tex`, in the
same wording (modulo LaTeX markup and citation commands),
so any fix must be applied in both versions:

- MUST-3 "four of the five largest banking mergers" — tex line 28.
- MUST-4 / MUST-6 Ashwin–Poush window and "six to nine months
  later" — tex line 145.
- MUST-5 significance bullets ("Equips investors…") — tex line 153.
- Line 143 limitation hedge ("typically released… rather than
  audited proof") — tex line 183.
- MUST-1 / MUST-2 literature quantifiers — tex line 28 and the
  corresponding problem-statement passages (spot-checked, not
  line-mapped in full).

No LaTeX-only contradiction was found in the spot-checked
passages. Because this was a spot-check, the absence of other
LaTeX divergences is NOT claimed (see NOT checked).

## Fix list, in priority order

1. MUST-4: fix or delete the Ashwin–Poush publication-window
   sentence (line 108) to match the hedged line 143 and the
   thesis's own announcement file (one Magh date).
2. MUST-5: temper section 1.5 significance language to the
   actual Chapter 4 outcome (baseline non-significant at 5%,
   joint Wald $p = 0.085$); delete "most extensive … in its
   history".
3. MUST-1: soften "no empirical study in Nepal has formally
   evaluated…" to "no study identified in the literature
   reviewed in Chapter II…".
4. MUST-2: restrict "almost all / most / routinely" literature
   claims to the studies actually reviewed in Chapter II.
5. MUST-3: change "four of the five largest" to "four
   prominent" (or cite a ranking).
6. MUST-6: resolve "six to nine months later" against the
   October–January window in the same paragraph.
7. MINOR-1: fix the $H_1$ notation collision.
8. MINOR-7: clarify the NMB 0.57 billion figure as the amount
   beyond the 13% bonus issue.
9. MINOR-2, MINOR-3, MINOR-4, MINOR-5, MINOR-6: terminology
   and wording fixes listed above.
10. MINOR-8, MINOR-9, MINOR-10, MINOR-11: delete promotional
    sentences, shorten repeated passages to cross-references,
    soften "strict / complete" claims, delete "comprehensive"
    and "in-depth academic".
11. Apply every fix above in BOTH the Markdown chapter and
    the LaTeX chapter (Pass 5 shows the flagged passages
    exist in both).

## NOT checked — explicitly, so this review is never misread as covering them

- The full text of Chapter 2 and the original papers behind
  every literature summary in Chapter 1 (Chhetri 2023,
  Chaudhari 2025, Gyawali 2022, Joshi et al. 2023, Pant et
  al. 2024, Bhandari et al. 2026, Giri 2024, Gurung & Dahal
  2025, Bhattarai 2014, Pradhan & Dahal 2016, Silwal & Napit
  2019, Timalsina 2026). Their findings, samples, and
  P/E and Ashadh-end practices were NOT verified against
  the originals in this review; Chapter 1's summaries of
  them rest on their citations and on Chapter 2.
- The exact month-level dating of the "exactly 20 banks by
  mid-October 2023 (Asoj 2080)" claim against a primary NRB
  bank list (web reporting confirms 32 to 20 overall, but
  not the exact month in this review).
- The BS-date conversions (2033 BS, 29 Poush 2050 BS, 2068 BS,
  2072/73 BS, 2079 BS, 2080 BS) day by day against a Nepali
  calendar; they were carried on their cited sources.
- Every entry of the References bibliography against APA
  6th edition, and every item of the Faculty of Management
  (2019) guidelines against the chapter structure.
- NEPSE official closing prices: Chapter 1 makes no such
  claim, and none was checked here. Prices in this thesis
  remain cross-checked aggregator prices (ShareSansar via
  the dataset, Merolagani LTP), not verified NEPSE official
  closes — that limit is stated in Chapter 3 and is not
  contradicted by Chapter 1.
- A full Markdown-to-LaTeX diff (Pass 5 was a spot-check
  only, as stated above).
- Any thesis file, table, figure, or data file was not
  edited, moved, or deleted in this review. The only file
  written was this review file.

## LOOP ADDENDUM (2026-10-28, 10-pass loop, see 07_loop_log.md)

- Kanchan amount UPGRADED from minor to must-fix item 16:
  panel arithmetic gives 0.56bn beyond the 13% bonus
  (rise 2,374,973,386 less bonus 1,813,628,371 =
  561,345,015), while Kanchan's listed shares are 0.50bn
  (4,967,655 x Rs 100). The thesis's 0.57bn matches neither.
  Replace with the exact arithmetic and method, or delete.
- Merger dates/ratios verified externally in the loop
  (GBIME 9 Jan 2023 1:1, HBL 24 Feb 2023 100:80.28,
  NIMB 11 Jan 2023 100:90); the remaining citation error is
  the (NRB, 2023) attachment, not the facts.
