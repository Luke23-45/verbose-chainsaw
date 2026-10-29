# Fix verification: Krishna's thesis patches at 9279fb1 against the finalized review (docs/finalized/01-05 + 00_loop_audit)

Scope: git pull 2026-10-29, d5b9fb6..9279fb1, fast-forward, 6 commits, all by krishna subedi.
- a66b4ea Chapter I, d52dddf Chapter II + references.bib, 52f7fd3 Chapter III,
  ee45fe9 Chapter IV, f367ab6 Chapter V, 9279fb1 proposal methodology prose.
- 12 files changed, 277 insertions, 181 deletions. Every chapter was changed in BOTH
  Markdown (docs/draft/thesis/) and LaTeX (src/thesis/chapters/), plus references.bib.
- This file is review-only, untracked, NOT committed or pushed. No thesis file was
  changed by this verification.

## Headline verdict: NO, not all issues are correctly addressed

- Must-fix: **10 of 13 fully addressed, 2 partially addressed, 1 failed.**
- Minors: **25 of 28 addressed; 3 remain** (Ch1 M2, Ch2 M4, Ch5 M2).
- One failed must-fix is critical and must be corrected before any submission:
  the new Chapter I findings preview contains wrong p-values that contradict
  Chapter IV and the author's own new Table 5.1, and falsely imply a 5%
  significant pre-consolidation EPS slope.

## Must-fix verdicts, item by item

### Chapter I

1. Core-finding paragraph (Must-fix 1) — FAILED, critical.
   Added in both versions, but its p-values are wrong under the thesis HC3 estimator:
   - Preview says Model 1 beta_E = 2.095, p = 0.089. Correct (T3, Ch4, new Table 5.1): p = 0.616.
   - Preview says Model 1 beta_B = 0.219, p = 0.771. Correct: p = 0.908.
   - Preview says Model 2 pre beta_E = 5.577, p = 0.040. Correct (T4, Table 5.1): p = 0.140.
     The preview sentence "anchored primarily in operational earnings" on p = 0.040
     therefore falsely implies 5% significance. At p = 0.140 it is not significant.
   - Preview says delta_E = -3.124, p = 0.218. Correct: p = 0.448.
   - Correct in the preview: joint Wald F(2,14) = 2.954, p = 0.085; R6 F(2,10) = 5.818,
     p = 0.021; Model 1 df 16; Model 2 df 14.
   - Also incomplete against the suggested paragraph: pre BVPS (0.100, p = 0.940),
     delta_B (-1.758, p = 0.175) and the post slopes (EPS 2.453, BVPS -1.658) are omitted.
   Fix: replace all four p-values above with the HC3 values, in both versions, and
   add delta_B (or drop the significance implication for pre EPS).

2. Opening hook (Must-fix 2) — ADDRESSED.
   First sentence is now the stability question across reorganizations, not generic
   RIV theory. History (1976, 1993, 1994) still sits in paragraph 2, before the
   consolidation puzzle detail, but the chapter now opens on the puzzle, which is
   what section 3.2's hook test requires.

3. Merger dates citation (Must-fix 3) — ADDRESSED.
   Merger sentence now cites GBIME (2022), Himalayan Bank (2023), Kumari Bank (2022),
   NIMB (2023). (NRB, 2023) is kept only for the "exactly 20 licensed institutions"
   sentence, as instructed.

4. Sector-dominance proportion (Must-fix 4) — PARTIAL, not fully addressed.
   Improvement: Bhattarai (2014) is removed from the citation. Remaining gap: the
   sentence still claims "the largest single share" of market capitalization,
   turnover and ownership with NO proportion anywhere, citing only Pradhan & Dahal
   (2016) and Timalsina (2026), neither of which was verified for this claim.
   The same unproportioned claim also survives in Chapter V section 5.2.1
   (see carry-over below). Either add a verified proportion with source and year,
   or soften the claim to what those two citations actually support.

### Chapter II

5. Dahal (2025) bibliography entry (Must-fix 1) — ADDRESSED, exactly.
   references.bib now reads: Dahal, Pramod; Gurung, Rajesh; Ghimire, Shiva Raj;
   "Impact of Financial Indicators on Nepalese Commercial Bank Stock Prices";
   journal, volume 6(1), pages and DOI unchanged and correct.

6. Table 2.1 against section 4.2 (Must-fix 2) — PARTIAL, with new errors.
   Real progress: rows 17 to 20 (Bajracharya, Dahal et al. 2025, Bhandari et al. 2026
   added); most Nepalese rows now carry total observations; an explicit selection
   criterion is stated ("dependent variable is MPS, evaluating fundamental
   accounting indicators across commercial banks"); circular-P/E tags are now
   consistent across rows; Gap 2 P/E list now includes Lamsal and Silwal.
   Still failing, in order of seriousness:
   a. No dedicated Methodological Critique column. Critique is still only parenthetical
      tags inside Core Findings, plus "static pooling" on the Gurung & Dahal row.
      Section 4.2 makes the critique column mandatory.
   b. Total observations still missing for 6 of 20 rows: Pradhan (2003), Collins
      (1997), Kwon & Wang (2020), Sharma (2011), Adhikari (2023), Bhandari (2026,
      "Census" with years but no count).
   c. Lamsal (2024) and Gurung & Subedi (2024) are STILL absent from the table,
      although both meet the stated criterion on the thesis's own prose (Lamsal: DV
      MPS, EPS/P/E/DPS/BVPS; Gurung & Subedi: DV share prices, EPS/BVPS, 171 obs).
      The stated criterion therefore does not excuse them. Niraula (2026) is also
      absent; its prose does not state a DV explicitly, so either add it or state
      why it fails the criterion.
   d. NEW md-only author error: the Markdown table row reads "Bajracharya & Dangol
      (2019)". The bibliography and the chapter prose both say Bajracharya &
      Sawagvudcharee. The LaTeX table uses \citet{bajracharya2019} and renders
      correctly, so Markdown and LaTeX now disagree on this row. Fix the Markdown
      row to Sawagvudcharee.
   e. NEW unverified figures in the table: Bhattarai "72 obs (2006-2014)" — prose
      gives no observation count, and 9 banks x 9 years would be 81, not 72, so 72
      needs a page-level source or removal; Kwon & Wang "(1998-2014)" — years not
      in the chapter prose, needs a source; Bhandari "(2015-2024)" — years not in
      the prose, needs a source.
   f. Dahal row overstates its abstract: it claims "dividend rate significantly
      positive". The publisher abstract says P/E and BVPS are significantly positive
      and dividend rate only positively correlated, less pronounced. Change the row
      to match the abstract, or cite a significance result from the paper itself.
   g. Gurung & Dahal row says "110 obs" for a prose "ten-year period FY 2013/14 to
      2023/24". That span is 11 fiscal years, so 110 is arithmetically consistent
      with 11 years but inconsistent with the prose "ten-year" label. Align the
      prose label and the table count to the same year count.

7. Thematic dialectic (Must-fix 3) — ADDRESSED.
   New section 2.4.5 gives four thematic debates matching the instructions themes,
   including the EPS-dominant vs BVPS-dominant divergence (Bhandari/Chaudhari/
   Niroula/Pradhan & Dahal vs Chhetri/Silwal) with a contextual explanation
   (2015 capital mandate, stabilization, 2023 consolidation).

8. Prohibited word "pivotal" (Must-fix 4) — ADDRESSED.
   Changed to "central" in both versions; 0 hits remain.

### Chapter III

9. Merolagani comparison scope (Must-fix, Ch3) — ADDRESSED, exactly.
   Section 3.4.3 point 3 now reads "Dataset prices (28 clean observation-date prices
   plus the two delayed resumption prices, subsequently excluded under the five-day
   freshness rule) were compared against Merolagani LTPs", matching A4. A4 itself
   was not touched, correctly.

10. Sample proportion, loop Addition A1 (new Must-fix) — ADDRESSED via the
    loop-allowed alternative.
    New text states the count proportion exactly (25.0%, 5 of 20, NRB 2023) and
    states explicitly that "aggregate Class 'A' sector asset and market-capitalization
    shares are not claimed or evaluated". That is the explicit non-claim the loop
    audit accepted as an alternative to computing an asset share. It is not an
    asset-share disclosure, and must not be quoted as one.

### Chapter IV — no must-fix items

All Chapter IV minors below are addressed; no must-fix was outstanding.

### Chapter V

11. Three-domain implications, section 8.3 (Must-fix 1) — ADDRESSED by structure.
    Headings are now exactly three: 5.4.1 Regulatory Authorities (NRB, SEBON, NEPSE),
    5.4.2 Executives and Boards, 5.4.3 Investors and Market Participants. Section 5.1
    intro lists the same three. Watch item, not a failure: item 7 inside 5.4.1 is an
    ASB/ICAN (standard-setter) recommendation, placed under a Regulators heading.
    That is defensible as regulatory, but it is not NRB/SEBON/NEPSE; do not let it
    grow into a fourth domain heading.

12. Hypothesis decision table, section 8.2 (Must-fix 2) — ADDRESSED, values correct.
    New Table 5.1 (Hypothesis, Model/Parameter, Null, Estimate (SE)/Stat., Decision)
    plus the joint test as its own row and the R6 sensitivity row. Every value was
    checked against Chapter IV: H1 2.095 (4.096) p = 0.616 and 5.577 (3.560) p = 0.140;
    H2 0.219 (1.858) p = 0.908 and 0.100 (1.306) p = 0.940; H3 -3.124 (4.003) p = 0.448;
    H4 -1.758 (1.231) p = 0.175; joint F(2,14) = 2.954 p = 0.085; R6 F(2,10) = 5.818
    p = 0.021. All decisions at alpha = 0.05 are correct.

13. "During merger processes" (Must-fix 3) — ADDRESSED.
    0 hits in Markdown and LaTeX. The Chapter V suspension wording now uses
    "merger-related trading suspensions" throughout.

## Minors: 25 of 28 addressed

Addressed (checked in current text, both versions where applicable):
- Ch1 M1 "utilizes" to "uses": Ch1 utiliz* count now 0 in both versions.
- Ch1 M3 suite naming: "eight-part" is gone from Ch1; Ch3/Ch4/Ch5 now use
  "eight-specification suite (R1-R2 baselines plus six robustness variants R3-R8)".
- Ch2 M1 Ohlson NI coefficient: now >= 0, "strictly positive for omega > 0".
- Ch2 M2 Gap 2 P/E list: now includes Lamsal (2024) and Silwal & Napit (2019).
- Ch2 M3 Pradhan & Dahal table row: now "macro controls secondary", matching prose.
- Ch3 M1 suite naming: as above.
- Ch3 M2 GBIME "largest bank": now framed as 2022 projection, "subsequently
  confirmed upon unified operations (NRB, 2023)". Substance was web-verified in
  the loop; the NRB 2023 citation is thin for a size ranking, but the wording is
  no longer a bare 2022-source present-tense claim.
- Ch3 M3 VIF range: the uncomputed "~30 / 20-30" range is gone from the chapters;
  Ch4 and Ch5 now give only the exact bivariate VIF ~20.2 from r = 0.975.
  Residual, outside the chapters: T2's note still reads "variance inflation ~ 30".
  Fix the T2 note when tables are regenerated, or the table and chapters disagree.
- Ch3 M4 utiliz* (4 forms): Ch3 utiliz* count now 0 in both versions.
- Ch3 M5 identification phrase: now "(after removing both bank-specific and
  fiscal-year means)".
- Ch4 M1 Figure 4.6 title: now "Across Seven Specifications (R1, R2, R4-R8)".
- Ch4 M2 Chaitra "statutory" without operationalization: Table 4.1 note, section
  4.3.4 and section 4.3.5 point 3 now all use the operationalized wording.
- Ch4 M3 VIF range: as Ch3 M3 above.
- Ch4 M4 Post notation: now Post_t = D_2079/80 + D_2080/81 + D_2081/82.
- Ch4 M5 Table 4.6 df note: now lists R1 16; R2, R3, R7, R8 14; R4 13; R5, R6 10.
- Ch4 M6 suite naming: as above.
- Ch4 M7 NPL premise: section 4.3.2 mechanism 1 now cites (NRB, 2023) for rising
  NPLs, still framed as a "Plausible Mechanism", non-estimated.
- Ch5 M1 RQ labels: new section 5.3.1 "Direct Answers to Research Questions" with
  labelled Answers to Research Questions 1, 2 and 3.
- Ch5 M3 suite naming: as above.
- Ch5 M4 identification phrase: section 5.3.4 now carries the same
  "(after removing both bank-specific and fiscal-year means)" qualifier.
- Ch5 M5 VIF range: now only the exact bivariate ~20.2.
- Ch5 M6 "utilize": Ch5 utiliz* count now 0.
- Loop A2 Ch4 "underscores" to "highlights": 0 hits.
- Loop A3 Ch5 "crucial role" to "substantial influence": 0 hits.
- Loop A4 Ch2 six "utilizing" forms to "using": Ch2 utiliz* count now 0.

Still open (minors, not must-fix):
- Ch1 M2: purposive selection hurdles are still not listed in Chapter I itself
  (they are listed in Ch3 section 3.3.2, which is why this stays a Ch1-only minor).
- Ch2 M4: Lamsal (2024) paragraph still gives no years or observation count
  ("a multi-year period", seven banks). Add from the paper or drop from detail.
- Ch5 M2: section 5.4.2 point 5 "fragmented corporate disclosures" premise is
  still uncited. Cite SEBON/NEPSE practice or rephrase as a proposal.

## Carry-over that was NOT done

When Chapter I Must-fix 4 is fixed with a verified proportion, propagate that exact
wording and citation to Chapter V section 5.2.1. As of 9279fb1, Chapter V section
5.2.1 still makes the same unproportioned "largest share" claim (Pradhan & Dahal
2016; Timalsina 2026), so the two chapters will still agree only in being equally
unproportioned. Fixing Chapter I alone will leave Chapter V behind.

## Out of scope, noted not judged

Commit 9279fb1 also changes src/proposal/sections/07_methodology/07_methodology.tex
(utilize variations to use, 3 lines). That is proposal text, not thesis text, and was
not part of the finalized review's fix list. It was not verified here beyond noting
it is a prose-only change. Proposal edits remain the author's call, not a review fix.

## What must happen next, in order

1. Fix the Chapter I preview p-values (Must-fix 1 failure above) in BOTH versions.
   This is the only item that makes the thesis internally contradictory as it stands.
2. Finish Table 2.1 properly: add a real Methodological Critique column, add total
   observations for the six missing rows, add Lamsal and Gurung & Subedi (or state
   why they fail the criterion), fix the Markdown Dangol row, and source or remove
   the Bhattarai 72, Kwon 1998-2014 and Bhandari 2015-2024 figures and the Dahal
   dividend-rate significance claim.
3. Add a verified sector proportion to Chapter I Must-fix 4 and copy it to
   Chapter V section 5.2.1, or soften both claims.
4. Clear the three remaining minors (Ch1 hurdles, Ch2 Lamsal years/N, Ch5 fragmented
   premise) and the T2 "~30" note.
5. Only then re-run a chapter-vs-table number check, because the Chapter I preview
   error proves a new number can enter after a table check has passed.
