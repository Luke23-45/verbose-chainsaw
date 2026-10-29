# Finalized review — Chapter II: Literature Review, audited against docs/instructions

**Thesis version audited:** HEAD 8c96edc (pulled 2026-10-29).
Files checked, both versions:
`docs/draft/thesis/chapter_02_literature_review.md` and
`src/thesis/chapters/chapter_02_literature_review.tex`, plus
`src/thesis/references.bib` (now 57 entries) for the bibliography
items cited in this chapter.
**Thesis files changed to write this review: NONE.** Applying any
fix still needs the author's approval, in both versions where the
passage appears in both, and in the bib where the error is in the
bib.

**Standard applied:** `docs/instructions/instructions_for_paper.md`
— §1 theory discipline, §2 traps (especially Trap 1 circularity,
Trap 3 look-ahead, Trap 7 causal language), §4 literature rules
(thematic dialectic §4.1, synthesis matrix §4.2, gap formulation
§4.3), §5 data rules, §7 prose rules, §10 rubric. The instructions'
illustrative numbers (§6.2, §8.2) are NOT thesis numbers and were
not used as a check standard here (see the Chapter I review for
that warning).

## How this chapter was checked, so it can be re-checked

1. Read Chapter II in full, both versions, section by section.
2. Re-checked every Phase 2 / loop finding for this chapter
   against the 8c96edc text (several are now fixed — see Passes).
3. Grep-verified negative and presence claims (prohibited words,
   bib entry, Flannery in both versions, table coverage).
4. Did targeted online research in this step for three items
   only, because those three decide whether a claim is an error
   or a pass: (a) Dahal, Gurung & Ghimire (2025) — publisher
   (NEPJOL) abstract and page header, DOI 10.3126/ijmss.v6i1.75407;
   (b) NRB approval of bank financial statements before public
   issue — PKF Doing Business in Nepal and NRB-approval reporting;
   (c) Timalsina (2026) and Bhandari et al. (2026) — searches
   returned no publisher abstract for either, so those two
   remain UNVERIFIED, not disproven (see below).
5. Everything else not verified in this step is listed under
   "NOT verified — not counted as errors", not under Must-fix.
   That distinction is the author's no-slop rule applied to
   this review itself.

## Verdict for Chapter II

Chapter II's theory is sound and its regulatory framing is now
correct, but it fails the instructions' literature standard in
two structural ways, and it contains one proven bibliography
error. The Ohlson derivation re-derives correctly, the BAFIA
paraphrase is now right, Bhattarai is now right, and the gaps
are genuinely structural — those are real passes. What fails is:
(1) the empirical review is a chronological catalogue, not the
thematic dialectic §4.1 requires, and its synthesis is a table
with no synthesis discussion; (2) that table does not meet
§4.2's own mandatory columns or coverage; (3) the newly added
Dahal (2025) bibliography entry — the very entry Phase 2 asked
for — has the wrong title and the wrong author names, even
though its journal, volume, pages, and DOI are right.

## Must-fix (verified)

### 1. Dahal (2025) bibliography entry: wrong title, wrong authors
- **Rule:** §4.2 (formal APA citation); §10 rubric 11 (numbers
  and citations match 100% across text, tables, and code).
- **Evidence (publisher-verified in this step):** NEPJOL /
  ResearchGate page header for DOI 10.3126/ijmss.v6i1.75407,
  IJMSS Vol. 6, No. 1, January 2025, pp. 252–261, gives:
  title **"Impact of Financial Indicators on Nepalese
  Commercial Bank Stock Prices"**, authors **Pramod Dahal,
  Rajesh Gurung, Shiva Raj Ghimire**, 209 annual observations,
  FY 2013/14–2023/24, all NEPSE-listed commercial banks,
  variables P/E, BVPS, dividend rate, earnings yield,
  market-to-book; P/E and BVPS significantly positive.
- **What the thesis bib says (`references.bib`, entry
  `dahal2025`):** title "Impact of Financial Performance
  Indicators on Market Price of Commercial Banks in Nepal",
  authors "Dahal, K. P. and Gurung, C. B. and Ghimire, M."
  Journal, volume, number, pages (252–261), year, and DOI
  are correct; title and author first names/initials are not.
- **Fix:** Correct the bib entry to the publisher title and
  authors above. The in-text form "Dahal, Gurung, and Ghimire
  (2025)" and the Chapter II footnote's journal/volume/pages/
  209-observation statements are correct and must NOT be
  changed. Do not "fix" the footnote to match the wrong bib
  entry — fix the bib to match the publisher.
- **Consequence for the review:** the Phase 2 item "add the
  Dahal entry" is now satisfied in existence but NOT in
  content. Until this fix, the thesis cites a paper under a
  title and authors that do not exist under that DOI.

### 2. Table 2.1 does not meet §4.2 — observations, critique, coverage
- **Rule:** §4.2 requires a "comprehensive, standardized"
  matrix with mandatory columns: Study & Author(s) (formal
  APA); Sample & Period (number of cross-sections, exact
  years, TOTAL OBSERVATIONS); Econometric Methodology;
  Key Variables; Core Findings AND Methodological Critique.
- **Evidence (verified by reading the table):**
  (a) **Total observations missing for 16 of 17 rows.**
  Only Giri (2024) gives "40 obs" in its Sample cell.
  Every other row gives banks and years only (e.g., Niroula
  18 banks 2015–2020, with no 90; Chaudhari 10 banks
  2014–2024, with no 100; Timalsina 13 banks 2011–2024,
  with no 169) — even though the §2.4 prose states those
  totals. A reader of the table alone cannot recover them.
  (b) **No separate critique column, and critique is
  incomplete where it appears.** The Findings column embeds
  "(Circular P/E)" for P/E rows only. It gives no critique
  for static pooling, Ashadh-end pricing, unadjusted
  standard errors, or small clusters for any row, although
  those are the thesis's own Gap 1/3/5 criticisms.
  (c) **Coverage omits valuation studies reviewed in the
  prose, with no stated selection criterion.** Table rows
  (17): Pradhan 2003, Collins 1997, Kwon & Wang 2020,
  Sharma 2011, Bhattarai 2014, Pradhan & Dahal 2016,
  Silwal & Napit 2019, Niroula 2021, Gyawali 2022,
  Chhetri 2023, Joshi 2023, Giri 2024, Pant 2024,
  Chaudhari 2025, Gurung & Dahal 2025, Timalsina 2026,
  Adhikari 2023. Missing, although reviewed in §2.4:
  Bajracharya & Sawagvudcharee (2019), Lamsal (2024),
  Gurung & Subedi (2024), Niraula et al. (2026),
  Bhandari et al. (2026), and Dahal et al. (2025) itself
  (present only as a footnote to Gurung & Dahal).
  The table intro calls it "curated", but §4.2 says
  "comprehensive" and no inclusion criterion is stated
  anywhere, so "curated" does not excuse the omissions.
- **Fix (author's choice, one of the two):** either (i)
  complete the table — add a total-observations figure to
  every row, add a Methodological Critique column (or
  critique notes per row), and add the six missing
  valuation studies; or (ii) state an explicit inclusion
  criterion in the table intro (e.g., studies whose
  dependent variable is MPS and which test EPS/BVPS —
  in which case Niraula's CAR/CRR study would need a
  stated reason for exclusion, and Dahal 2025 and
  Bhandari 2026 would still belong in it) and conform the
  rows to that criterion. Do not keep the table as
  "comprehensive" while it is curated without a criterion.

### 3. Empirical review is a catalogue, not a thematic dialectic — §4.1
- **Rule:** §4.1: organize around structural themes,
  methodological debates, and empirical contradictions —
  (1) earnings-power vs. net-asset-value debate, (2)
  circular multiples, (3) temporal misalignment,
  (4) static pooling — and explain WHY findings contradict
  each other, not merely that they do.
- **Evidence (verified by structure):** §2.4 is organized
  chronologically: §2.4.1 international, §2.4.2 foundational
  Nepalese, §2.4.3 recent (2021–2024), §2.4.4 contemporary
  (2024–2026). Each paragraph is a study summary (sample,
  method, findings). §2.4.5, titled "Synthesis of Empirical
  Literature", contains no synthesis discussion at all —
  it introduces Table 2.1 and stops. The thesis therefore
  never, in Chapter II, explains the central contradiction
  its own paragraphs display: EPS significant in Joshi,
  Pant, Chaudhari, Gurung & Dahal, but insignificant in
  Chhetri and Giri; BVPS positive-significant in Joshi and
  Chhetri, negative-insignificant in Niroula, Lamsal, and
  Pant. The thematic material exists, but only in §2.2.6
  (circularity), §2.3.2 (timing), and §2.5 (gaps) — not as
  a literature synthesis.
- **Fix:** Add a synthesis subsection (§2.4.5, before or
  after the table) organized by the four §4.1 themes,
  using the studies already reviewed, explaining the
  divergence (different periods, P/E circularity,
  Ashadh-end vs. later pricing, pooled vs. fixed effects,
  merger-era asset expansion) and stating what remains
  unresolved. Do NOT delete the chronological paragraphs
  to make room; add the synthesis. The gaps in §2.5
  already state the thesis's answers — the synthesis must
  state the debate they answer.

### 4. "pivotal" — prohibited vocabulary, §7.1
- **Rule:** §7.1 table: "pivotal / testament" are prohibited;
  replacement: "critical, central, evidence of, consistent
  with".
- **Evidence (grep-verified, both versions):** §2.2.2
  opening: "A pivotal theoretical question in accounting
  value relevance is whether ..." (.md line 70, .tex
  line 105).
- **Fix:** Change to "A central theoretical question ...".
  This is the ONLY §7.1 prohibited word found in Chapter II
  (delve, underscores, showcasing, testament, beacon,
  tapestry, paramount, game changer, multifaceted, myriad,
  "it is important to note that", utilize, facilitate:
  all 0 by grep).

## Minor (verified, fix with the must-fix batch)

### M1. Ohlson NI coefficient "> 0" fails at the ω = 0 boundary
- §2.2.1 states the NI coefficient $k \cdot \phi =
  \omega(1+r)/(1+r-\omega) > 0$, while the same section
  allows $0 \le \omega < 1$. At $\omega = 0$, $k \cdot \phi = 0$.
  The BV coefficient $(1-k) > 0$ holds for all $\omega < 1$
  and is correct. Fix: write $k \cdot \phi \ge 0$ (strictly
  positive for $\omega > 0$), or restrict the claim to
  $\omega > 0$. The derivation itself is correct (re-derived
  in the Phase 2 loop); this is an edge-case statement fix
  only, in both versions.

### M2. Gap 2 P/E list is selective, not exhaustive, against Chapter II's own text
- Gap 2 lists Bhattarai, Chhetri, Giri, Gurung & Dahal,
  Joshi, Pant, Timalsina as the P/E-including studies.
  Chapter II's own §2.4 paragraphs also describe P/E as a
  regressor for Silwal & Napit (2019) (§2.4.2: MPS on BVPS,
  ROE, P/E) and Lamsal (2024) (§2.4.3: EPS, P/E significant).
  Neither appears in Gap 2. Fix: add "including" before the
  Gap 2 list, or add Silwal and Lamsal to it. Not a
  must-fix, because the list may be illustrative — but as
  written it reads as the complete set, and it is not.

### M3. Table 2.1 Pradhan & Dahal row drifts from its §2.4 paragraph
- §2.4.2 paragraph: size and EPS are the most consistent
  determinants; "macroeconomic variables exhibited secondary
  explanatory power". Table row: "Bank size and EPS are the
  primary positive determinants of market prices; ROA is
  secondary." ROA-as-secondary is not in the paragraph.
  Fix: align the table row with the paragraph (macro
  secondary), or verify the "ROA secondary" claim against
  the paper itself in a later check and then keep it with
  that source. Do not change the paragraph to match the
  table without that check.

### M4. Lamsal (2024) paragraph gives no sample size or years
- §2.4.3: "seven commercial banks ... over a multi-year
  period" — no years, no total observations, although
  every neighbouring paragraph gives both. Fix: add the
  years and observation count from the paper, or remove
  Lamsal from the detailed review and keep it only as a
  cited example. This is also covered in substance by
  Must-fix 2 (total observations in the table).

## Passes — verified compliances (do NOT "fix" these)

- **Bhattarai (2014) FIXED.** §2.4.2 and Table 2.1 now read:
  9 named banks (Nabil, Nepal Investment, Standard
  Chartered, Everest, Bank of Kathmandu, Machhapuchchhre,
  Laxmi, Kumari, Siddhartha), 2006–2014, variables DPR, DY,
  EPS, P/E, SIZE, EPS and P/E positive, DY inverse. No
  "14 banks", no "35 observations", no BVPS, no DPS.
  This matches the full-text read in the Phase 2 loop.
  The circular-P/E point about Bhattarai stands.
- **BAFIA §2.3.2 FIXED.** The two duties are now stated
  correctly: (1) submit balance sheet and P&L to NRB
  within three months, publishing summary details within
  that period; (2) publish the AUDITED statements for the
  public within nine months into the subsequent year.
  Counting Shrawan–Chaitra to end-of-Chaitra is presented
  as the study's operationalization, not as statutory text.
  The statute names no month, and Chapter II no longer
  claims it does.
- **NRB approval phrase is NOT an error.** §2.2.5 and
  Chapter I mention "NRB approval" before publication.
  That is not presented as a §59(2) duty (the §2.3.2 duty
  list correctly omits it), and it is supported in
  practice: PKF Doing Business in Nepal states BFI annual
  financial statements are "subject to review and approval
  from these authorities before being issued to the
  public", and NRB-approval reporting for bank accounts
  is standard. Do not delete the approval phrase on
  BAFIA grounds; if anything, §2.3.2 could add one
  sentence distinguishing the §59 duties from the
  approval practice, but that is optional, not a fix.
- **Kanchan FIXED in Chapter II.** §2.3.3: "adding
  approximately NPR 0.56 billion to paid-up capital beyond
  its 13% bonus share capitalization in FY 2077/78" —
  matching the panel arithmetic from the loop.
  Merger dates/ratios in §2.3.3 are cited to bank
  documents only (GBIME 2022 AGM, HBL 2023 report,
  Kumari 2022 EGM, NIMB 2023 report); (NRB, 2023) is used
  only for the "exactly 20" population sentence, where
  the licensed-institutions list supports it.
- **Dahal footnote is correct in content.** §2.4.4
  footnote correctly distinguishes Gurung & Dahal (2025),
  Pravaha 31(1), pp. 1–12, from Dahal, Gurung & Ghimire
  (2025), IJMSS 6(1), pp. 252–261, 209 observations, all
  listed banks. Only the bib entry (Must-fix 1) is wrong.
  Gurung & Dahal (2025) summary itself matches its
  publisher abstract (10 banks, FY 2013/14–2023/24,
  DPR/P/E/EPS/BVPS/ROA significant, bank fixed effects,
  static full-sample — correctly noted as the closest
  precedent that still omits an interaction test).
- **Flannery both-or-neither RESOLVED.** §2.2.4 now reads
  "Morgan (2002) and Flannery et al. (2004) establish ..."
  in BOTH versions (.md line 93, .tex line 139 via
  \citet). The Phase 2 divergence is gone.
- **"Four building blocks" FIXED.** §2.2.1 now says "four
  interrelated structural building blocks" and lists four.
  The Phase 2 "three followed by four" error is gone.
  "Tangible net assets" for BVPS: 0 occurrences in this
  chapter by grep.
- **Ohlson derivation CORRECT (except M1 edge case).**
  PVED → CSR → RIV under transversality → LID →
  $\alpha_1, \alpha_2$ → substitution → $P_t = (1-k)BV_t +
  k(\phi NI_t - D_t) + \alpha_2 v_t$, with $k, \phi$,
  $(1-k)$ algebra all checking out (Phase 2 loop pass 4,
  re-confirmed by reading in this step).
- **Circularity theory CORRECT.** §2.2.6 algebra
  ($\text{P/E} = \text{MPS}/\text{EPS}$, MPS regressed on
  a function of itself, $E[\text{P/E} \cdot \varepsilon]
  \ne 0$) is correct, and the thesis's own design excludes
  price-derived multiples (Trap 1 pass).
- **Gaps are structural, not geographical/chronological
  (§4.3) — PASS.** The five gaps (regime shift, circularity,
  temporal alignment, entity-timing, small-cluster
  inference) each name a methodological flaw and the
  design response, and they match the instructions' §4.3
  list plus the thesis-specific entity-timing gap. Gap 1's
  "to the best of the researcher's knowledge and within
  the extensive corpus of studies reviewed" is the correct
  scope hedge (cf. Chapter I's fixed wording).
- **Causal language in Chapter II: PASS.** Theoretical
  sections use "suggests", "may", "potentially", and
  conditional framing; no regression causal claim is made
  in this chapter (the design's non-causal framing is
  stated in Chapter I and will be checked in Chapter IV).
- **§2.1 organization matches the chapter: PASS.** Four
  sections promised (2.2 theory, 2.3 legal/regulatory,
  2.4 empirical, 2.5 gap) are the four sections present.

## NOT verified in this step — not counted as errors

- **Timalsina (2026) sample/findings:** 13 banks,
  FY 2011/12–2023/24, 169 observations, findings as
  summarized in §2.4.4 and Table 2.1. Bib entry verified
  (Management Review 2(1), pp. 305–316, DOI
  10.3126/tmr.v2i1.96931). Sample/findings NOT verified
  against the paper's full text in this step: the online
  search in this step returned no publisher abstract for
  Timalsina. 13 × 13 = 169 is arithmetically consistent,
  but consistency is not verification.
- **Bhandari et al. (2026) "census of all 19" and findings:**
  bib verified (IRJMMC 7(1), pp. 190–205, DOI
  10.3126/irjmmc.v7i1.93032). Census claim and
  "earnings indicators and dividend payout primary"
  NOT verified in this step: the online search returned
  no publisher abstract. Not disproven — unverified.
- **P/E-inclusion attributions for Chhetri, Giri, Joshi,
  Pant, Timalsina, Gurung & Dahal:** Chapter II's own
  §2.4 paragraphs describe P/E as a regressor for each
  (Chhetri: MPS on EPS/P/E/BVPS/ROA; Joshi: EPS/DPS/BVPS/P/E;
  Pant: EPS/DPS/BVPS/P/E; Giri: DPS/EPS/P/E/net worth;
  Timalsina: EPS/DPS/P/E/ROA/size/macro; Gurung & Dahal:
  publisher abstract lists P/E among significant impacts).
  Those paragraph-level descriptions were NOT checked
  against each paper's full text in this step, except
  Bhattarai (full text) and Gurung & Dahal (abstract).
  Gap 2's list therefore rests on Chapter II's own
  summaries for five of its seven names — a reason to
  check, not a reason to call it wrong now.
- **Ashadh-end pricing attributions (Gap 3):** Bhattarai
  verified (fiscal-year-end closing price, full text).
  Pradhan & Dahal (2016) and Silwal & Napit (2019)
  Ashadh-end/annual-average pricing NOT verified in this
  step.
- **All other study summaries:** Collins, Kwon & Wang
  (bib/finding verified in the loop: Accounting & Finance
  60(3), pp. 2717–2757, DOI 10.1111/acfi.12411),
  Sharma, Malhotra & Tandon, Almumani, Pradhan (2003),
  Pradhan & Dahal (2016), Bajracharya & Sawagvudcharee,
  Silwal & Napit, Niroula, Gyawali, Lamsal, Gurung &
  Subedi, Niraula et al., Adhikari et al. (2023/2023b),
  Bhattarai (2024), Dongol & Shrestha (2024) — samples
  and findings as summarized in §2.4 were NOT re-verified
  against full texts in this step, except where noted
  above. Internal consistency (paragraph vs. table) was
  checked; paper-level accuracy was not, except for the
  items in Must-fix 1 and the Passes.
- **Historical/regulatory facts:** SEC 1976, NEPSE/SEBON
  1993, floor trading 13 January 1994, 2011 Merger Bylaws,
  2015 capital mandate (2.0 → 8.0 bn, by end FY 2073/74),
  2022–2023 "big mergers" incentives — cited to NRB/NEPSE
  sources in the text, not independently re-verified here.
- **Dahal (2025) findings in the thesis body:** the thesis
  does not summarize Dahal 2025's findings in §2.4 prose
  (only the footnote). That is an omission covered by
  Must-fix 2 (table coverage), not a false statement:
  the thesis claims nothing about Dahal 2025's findings
  that the publisher abstract contradicts.

## Scope limits of this Chapter II review

- No thesis, table, figure, bib, or data file was changed.
- No compiled PDF was proofread; TU FOM formatting (§9)
  and APA 6th rendering (§10 rubric 24) are not certified
  here — the bib error in Must-fix 1 is a content error
  (title/authors), not a rendering judgment.
- Next step, in the author's order: Chapter III, against
  the same instructions, starting with the sample-selection
  hurdles (Chapter I, Minor M2), the Group/Bank and
  aggregator wording, HC3, df, and the robustness suite
  as specified in Chapter II §2.5 and Chapter III itself.
