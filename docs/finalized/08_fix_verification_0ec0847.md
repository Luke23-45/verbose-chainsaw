# Fix verification round 2: Krishna's patches at 0ec0847 against 07_fix_verification_9279fb1

Scope: git pull 2026-10-29, 9279fb1..0ec0847, fast-forward, 4 thesis commits, all by
krishna subedi. Order in history: 0c0f2a6 (Ch1 suite terminology), 3dda4ec (Lamsal
findings), 7767752 (Ch1 preview p-values), f878f32 (sector softening), 0ec0847
(Table 2.1 tex rows + md author fix). 6 files changed, 19 insertions, 15 deletions.
This file is review-only, untracked, NOT committed or pushed. No thesis file was
changed by this verification.

## Headline verdict: much better, but NOT fully done

- Must-fix: **12 of 13 fully addressed. 1 remains partial: Chapter II Table 2.1.**
- The previous critical failure is fixed correctly and completely.
- Minors: still **3 open** (Ch1 hurdles, Ch2 Lamsal years/N, Ch5 fragmented premise),
  unchanged by this batch. T2 "~30" note also still open.
- New problem introduced by this batch: **Markdown and LaTeX Table 2.1 now disagree.**
  The LaTeX table (the compiled thesis) is 22 rows; the Markdown table is still 20 rows.
  Syncing Markdown to LaTeX is now the single remaining Table 2.1 job, plus the
  critique column and the six missing observation counts.

## What this batch fixed, verified item by item

1. Chapter I preview p-values (was FAILED, critical) — NOW FULLY ADDRESSED.
   Commit 7767752, both versions. New preview gives: Model 1 EPS 2.095, HC3 t = 0.51,
   p = 0.616; BVPS 0.219, t = 0.12, p = 0.908; Model 2 pre EPS 5.577, p = 0.140,
   pre BVPS 0.100, p = 0.940; delta_E -3.124, p = 0.448; delta_B -1.758, p = 0.175;
   post slopes EPS 2.453, BVPS -1.658; joint Wald F(2,14) = 2.954, p = 0.085;
   R6 F(2,10) = 5.818, p = 0.021. Every value matches Chapter IV tables and Table 5.1,
   and the language is now correct ("positive but statistically insignificant",
   "economically substantial but not statistically significant", "neither individual
   shift attains significance"). This fix is better than the suggested paragraph in
   the original review because it also adds the post slopes and t-statistics.

2. Sector-dominance proportion (was PARTIAL) — NOW ADDRESSED via softening.
   Commit f878f32, both versions, both chapters. "Largest single share" is gone from
   Chapter I and from Chapter V section 5.2.1. Both now say banks "constituting a
   major component" of market capitalization, turnover and ownership (Chapter V
   keeps the qualitative phrase "dominant institutional pillar" alongside that
   softened wording, which is not a measured share claim). This is the softening
   alternative the original review allowed ("soften and drop Bhattarai"; Bhattarai
   was already dropped). No proportion is claimed, and none must be quoted from this.

3. Chapter I suite terminology (minor, now fully closed).
   Commit 0c0f2a6, both versions: section 1.7 roadmap now says "eight-specification
   estimation and robustness suite (R1-R2 baselines plus six robustness variants
   R3-R8)", matching Chapters III-V. No "eight-part" remains in Chapter I.

4. Table 2.1 author error (was NEW error) — FIXED in Markdown.
   Commit 0ec0847, Markdown row only: "Bajracharya & Dangol" corrected to
   "Bajracharya & Sawagvudcharee", matching bib and prose. LaTeX already rendered
   correctly via \citet{bajracharya2019}.

5. Table 2.1 Dahal dividend claim (was NEW error) — FIXED in LaTeX only.
   Commit 0ec0847, LaTeX row only: now "P/E and BVPS significantly positive;
   dividend rate positively associated", matching the publisher abstract.
   Markdown row STILL reads "dividend rate significantly positive". See sync issue.

## Table 2.1: still partial, and now out of sync

LaTeX table is now 22 rows (cites, in order): pradhan2003, collins1997, kwon2020,
sharma2011, bhattarai2014, pradhan2016, bajracharya2019, silwal2019, niroula2021,
gyawali2022, chhetri2023, joshi2023, giri2024, lamsal2024, gurung2024, pant2024,
chaudhari2025, dahal2025, gurungdahal2025, timalsina2026, bhandari2026, adhikari2023.
Markdown table is still 20 rows: the same list minus lamsal2024 and gurung2024.

Fixed in LaTeX only by 0ec0847:
- Lamsal (2024) row added: 7 Banks, multi-year panel, Descriptive/Multiple OLS,
  MPS/EPS/P/E/DPS/BVPS, EPS/P/E/BVPS positive, DPS inverse, circular P/E.
- Gurung & Subedi (2024) row added as \citet{gurung2024}: 16 Banks, 171 obs
  (2007-2023), Stepwise Multiple OLS, MPS/EPS/BVPS/DPS, EPS and BVPS significant
  positive, DPS insignificant, no P/E.
- Bhattarai "72 obs" removed: LaTeX row now reads "9 Banks (2006-2014)" with no
  observation count. Markdown row STILL reads "9 Banks, 72 obs (2006-2014)".

Still failing in BOTH versions:
- No dedicated Methodological Critique column. Header is still Study & Year,
  Sample & Period, Methodology, Key Variables, Core Empirical Findings.
  Critique remains only as parenthetical tags inside Findings.
- Total observations still missing for 6 rows: Pradhan (2003), Collins (1997),
  Kwon & Wang (2020), Sharma (2011), Adhikari (2023), Bhandari (2026, "Census"
  with years but no count).
- Unverified period figures still present: Kwon & Wang "(1998-2014)", Bhandari
  "(2015-2024)". Neither period appears in the chapter prose.
- Gurung & Dahal "110 obs" still sits next to a prose "ten-year period
  FY 2013/14 to 2023/24", which spans 11 fiscal years. Align the label and count.

Sync job (Markdown must be brought to the LaTeX table, or the two versions will
diverge at submission): add the Lamsal and Gurung & Subedi rows to Markdown,
remove "72 obs" from the Markdown Bhattarai row, and fix the Markdown Dahal row
to "dividend rate positively associated".

## Lamsal (2024) findings change: internally consistent, externally unverified

Commit 3dda4ec, both versions, prose only: Lamsal paragraph now says EPS, P/E and
BVPS had positive associations and DPS displayed an inverse relationship, replacing
the previous "EPS and P/E significant positive, BVPS insignificant negative".
The new prose matches the new LaTeX table row, so prose and table agree in LaTeX.
Accuracy against the Lamsal paper itself was NOT verified in this round (no
full-text check of Lamsal was in the finalized review scope, and none was done here).
Do not cite this verification as proof the new Lamsal summary is correct; it is a
changed study summary that still needs a page-level check against the paper.
The Lamsal minor (M4) also remains open on a separate point: prose and table still
say only "multi-year panel" with no years and no observation count.

## Not touched by this batch (still open, from round 1)

- Ch1 minor M2: purposive selection hurdles still not listed in Chapter I itself.
- Ch5 minor M2: Chapter V section 5.4.2 point 5 "fragmented corporate disclosures"
  premise still uncited.
- T2 note still reads "variance inflation ~ 30", while chapters now say ~20.2.
- Niraula (2026) still absent from Table 2.1 in both versions; its prose does not
  state a DV explicitly, so either add it or state why it fails the selection
  criterion. This is now the only prose valuation study still unaccounted for by
  the table, given Lamsal and Gurung & Subedi are in (LaTeX).

## Commit-message note (not a thesis error)

Commit 0ec0847 is titled "feat: add Chapter 2 literature review on RIV and M&A
valuation dynamics". Its actual diff is three Table 2.1 row edits in LaTeX and one
author-name fix in Markdown. The message overstates the change. Harmless for the
thesis text, but misleading in the audit trail; a future reader hunting for a new
RIV/M&A section will not find one in that commit.

## What remains, in order

1. Sync Markdown Table 2.1 to LaTeX Table 2.1 (Lamsal row, Gurung & Subedi row,
   Bhattarai obs removal, Dahal dividend wording).
2. Add a real Methodological Critique column and total observations for the six
   missing rows, and source or remove the Kwon and Bhandari period figures.
3. Page-check the new Lamsal summary against the Lamsal paper, and add its years
   and observation count (or drop it from detail).
4. Clear the three remaining minors and the T2 note, then re-run a Markdown-vs-LaTeX
   sync check on Table 2.1 specifically, since this batch proved the two versions
   can drift apart in a single commit.
