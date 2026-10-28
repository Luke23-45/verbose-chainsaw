# Phase 2 loop log: 10 passes against the sources (2026-10-28)

The first Phase 2 review was rejected by the author as not acceptable:
a single pass, however long, is not enough for the heart of the thesis,
because one hallucinated claim can cause rejection. This file is the
record of the loop that was then run, pass by pass, against the sources.
Nothing in it is a claim from memory. Every pass names what was checked,
what it found, and what changed in the verdict as a result.

Thesis files changed to write this loop: NONE. Only review files in
`docs/chapter_review/` were written or edited. Applying any fix still
needs the author's approval for the actual edit, in both Markdown and
LaTeX where the error appears in both.

## Pass 1 — All chapter numbers vs independent recomputation from the panel

Script: fresh NumPy OLS with HC3 covariance and Student-t p-values
(computed via the incomplete-beta function, since scipy is unavailable
in the extraction venv), run directly on
`data_analysis/data_extract/output/manual_review/mps_rd_joined_panel.csv`,
clean filter gap <= 5 days.

Result: EXACT MATCH, no new error. Clean n = 28 (13 pre, 15 post).
Descriptives reproduce for price, EPS, BVPS, DPS, ROA in full/pre/post
(price full mean 254.34, pre 310.59, post 205.60; EPS 14.05/17.90/10.72;
BVPS 160.18/158.11/161.97; DPS 3.56/6.06/1.40; ROA 0.99/1.31/0.70).
Model 1: EPS 2.095 (SE 4.096, p 0.616), BVPS 0.219 (SE 1.858, p 0.908),
R-squared 0.948, df 16. Model 2: pre EPS 5.577 (3.560, p 0.140), pre BVPS
0.100 (1.306, p 0.940), delta_E -3.124 (4.003, p 0.448), delta_B -1.758
(1.231, p 0.175), R-squared 0.978, df 14, joint Wald F(2,14) = 2.954.
R6 (drop FY2078/79, n = 23, df 10): delta_B -2.611 (SE 1.517, p 0.116),
Wald F(2,10) = 5.818. Correlations: price-EPS 0.358, price-BVPS 0.217,
EPS-BVPS 0.372, EPS-ROA 0.975 — all as in the tables.
Note on R6 parameter count: dropping FY2078/79 leaves 13 estimated
parameters (one fiscal-year dummy drops with the year), so
23 - 13 = 10 df. That is consistent with the chapter's df 10; the
chapter does not state k = 14 for R6, so there is no contradiction.

## Pass 2 — Figure notes vs figure code AND rendered figures

Rendered PNGs were viewed, not only code read. Confirmed visually:
- F1 scatter matrix: only MPS_RD/EPS/BVPS, scatter + KDE on the
  diagonal, no regression lines, no DPS/ROA. The Chapter 4 note
  claiming 5 variables and linear fit lines is wrong.
- F2 heatmap: two-decimal values only, no significance asterisks.
  The note claiming asterisks is wrong.
- F5 diagnostics: top-left is (a) Normal Q-Q, top-right is
  (b) Residuals vs fitted. The note swapping them is wrong.
- A2 robustness forest: 7 rows (R1, R2, R4, R5, R6, R7, R8; R3
  omitted by the code's own footnote), EPS coefficient and
  delta_E only. The note claiming all 8 specs and book-value
  parameters is wrong.
- F6 trends: the price line does connect through the open
  (excluded) markers for HBL/NIMB FY2077/78, and the figure's own
  footnote explains them. The Chapter 4 note's silence on the
  connecting line is confirmed as a minor gap, not a wrong
  description of the data.
- A1 coverage map: 28 realized, 2 gaps (54d/47d), 4 entity-mismatch
  cells — matches the chapters.
Conclusion: Phase 2 must-fix item 1 stands in full, now verified
against the rendered figures as well as the code.

## Pass 3 — Literature claims vs bibliography + online sources

Checked online (publisher/search abstracts and full text where
available) on 2026-10-28:
- Dahal, Gurung & Ghimire (2025): VERIFIED as a real paper,
  Interdisciplinary Journal of Management and Social Sciences 6(1),
  DOI 10.3126/ijmss.v6i1.75407, 209 annual observations,
  FY2013/14-2023/24, all listed banks, P/E and BVPS significantly
  positive. So the Chapter 2 footnote's 209 is correct; only the
  missing bibliography entry is the error. Fix = add the entry
  (pages 252-261 per the Grafiati listing of the same article;
  confirm pages against the publisher PDF before submitting),
  not delete the footnote.
- Gurung & Dahal (2025): VERIFIED, Pravaha 31(1), pp. 1-12,
  DOI 10.3126/pravaha.v31i1.89145, 10 of 19 banks, FY2013/14-2023/24,
  DPR/P/E/EPS/BVPS/ROA significant, P/E most influential, IR and
  SR not significant. The chapter's summary of this paper matches
  the abstract. It is a DIFFERENT paper from Dahal, Gurung &
  Ghimire (2025); the chapter's distinction between them is correct.
- Kwon & Wang (2020): VERIFIED, Accounting & Finance 60(3),
  pp. 2717-2757, DOI 10.1111/acfi.12411; finding as stated (less
  weight on earnings, more on book value after M&A, stronger
  after SFAS 141(R)).
- Giri (2024): bib entry is CORRECT as written (Journal of
  Advanced Academic Research 11(1), pp. 12-23). An earlier search
  query suggesting "Asian" was the reviewer's error, not the
  thesis's; no correction to Giri's journal title is needed.
- Bhattarai (2014): READ IN FULL TEXT (NEPJOL PDF, Economic
  Journal of Development Issues 17 & 18, pp. 187-198). This
  UPGRADED a Phase 2 "needs check" into a PROVEN ERROR, see
  new must-fix item 14 below. The paper's sample is NINE named
  banks (Nabil, Nepal Investment, Standard Chartered, Everest,
  Bank of Kathmandu, Machhapuchchhre, Laxmi, Kumari, Siddhartha),
  years 2006-2014, variables DPR, DY, EPS, P/E, SIZE. It never
  states 35 observations anywhere in its text, it contains no
  BVPS and no DPS variable, and its market price is the
  fiscal-year-end closing price. The thesis's "14 banks, 35 obs,
  EPS/DPS-DY/P/E/BVPS" is wrong on bank count, on observation
  count (unverifiable in the paper and inconsistent with a
  9-bank sample), and on variables.
- Timalsina (2026): bib VERIFIED (The Management Review 2(1),
  pp. 305-316, DOI 10.3126/tmr.v2i1.96931). The chapter's
  13 banks / 169 observations / FY2011/12-2023/24 was NOT
  confirmed against the paper's full text in this loop (only
  the bib entry was checked); it remains "needs full-text
  check", not verified. Note 13 x 13 = 169, so the numbers are
  at least arithmetically consistent, unlike Bhattarai's.
- Bhandari et al. (2026): bib entry as previously verified
  (IRJMMC 7(1), pp. 190-205). The chapter's "all 19" census
  claim was NOT confirmed against the paper's full text in
  this loop; it remains "needs full-text check".

## Pass 4 — Ohlson derivation re-derived step by step

Every step in Chapter 2, section 2.2.1, re-derived by hand:
PVED, clean surplus BV_t = BV_{t-1} + NI_t - D_t, abnormal
earnings NI^a_t = NI_t - r*BV_{t-1}, RIV form
P_t = BV_t + sum E[NI^a]/(1+r)^tau under the transversality
condition, LID NI^a_{t+1} = omega*NI^a_t + v_t + eps,
v_{t+1} = gamma*v_t + eps, alpha_1 = omega/(R_f - omega),
alpha_2 = R_f/((R_f - omega)(R_f - gamma)), substitution
NI^a = (1+r)NI_t - r*BV_t - r*D_t, collection to
P_t = (1-k)BV_t + k(phi*NI_t - D_t) + alpha_2*v_t with
k = r*omega/(R_f - omega), phi = R_f/r, (1-k) =
(1+r)(1-omega)/(1+r-omega), k*phi = omega(1+r)/(1+r-omega).
All algebra is CORRECT. Two trivial notes, both minor, neither
a must-fix: (a) the strict "> 0" claim for the NI coefficient
fails at the boundary omega = 0 (then k*phi = 0); it holds for
omega > 0. (b) "mathematically necessary" overstates Ohlson
(sufficiency, not necessity) — already in the Phase 2 minor
list. The "three building blocks" followed by four numbered
items is CONFIRMED as a real counting error in the chapter text.

## Pass 5 — Legal/institutional claims vs BAFIA/NRB/merger sources online

- BAFIA Section 59(2): VERIFIED against the Law Commission /
  kaanun.app text. Two duties: (i) submit balance sheet and
  P&L to NRB within three months of FY-end and publish details
  for the public within that period; (ii) make public the
  AUDITED balance sheet and P&L "within nine months of the
  next fiscal year". The statute does NOT name Chaitra, and
  the audited duty is PUBLICATION, not submission to NRB.
  Consequences: (a) Phase 2 Chaitra must-fix stands, and is
  strengthened — Chapter 2, section 2.3.2, contains a third
  Chaitra error not separately listed in Phase 2: it says
  counting Shrawan-Chaitra "establishes the end of Chaitra
  as the statutory publication deadline". (b) NEW must-fix
  item 15: Chapter 2, section 2.3.2, item 2 misstates the
  audited duty as "submit its audited balance sheet ... to
  NRB within nine months". Correct to "publish the audited
  statements for the public within nine months".
- Merger dates/ratios: VERIFIED externally for all four 2023
  mergers — GBIME-BoK joint operation 9 Jan 2023, 1:1
  (Investopaper/ICRA); HBL-Civil 24 Feb 2023, 100:80.28 (HBL's
  own introduction page); KBL-NCC 1 Jan 2023, 1:1 (as in the
  thesis; the loop did not re-open a KBL primary source, so
  this one rests on the thesis's bank citation plus the
  pattern of the other three); NIMB 11 Jan 2023, 100:90
  (Corporate Angle / Fiscal Nepal). NMB-Kanchan: acquisition,
  NRB final approval 9 Aug 2020, joint operation 23 Aug 2020,
  swap 100:85 (ShareSansar compilation, Fiscal Nepal,
  Investopaper). The DATES AND RATIOS in the thesis are
  therefore correct.
- DOWNGRADE to Phase 2 must-fix item 3: the merger items in
  Chapter 2 cite bank documents as well as (NRB, 2023)
  (GBIME 2022 AGM minutes, Kumari 2022 EGM, HBL 2023 annual
  report, NIMB 2023 annual report), so the item is narrowed:
  the remaining error is (NRB, 2023) being attached to
  claims its list entry cannot support, and — separately —
  the Kanchan AMOUNT, which has no cited source at all.
  The fix is to drop (NRB, 2023) from those sentences (keep
  the bank citations, after checking each bank document
  actually states the date/ratio) and to source or delete
  the Kanchan amount. See new must-fix item 16.
- Kanchan amount check (panel arithmetic): NMB share capital
  FY2076/77 = 13,950,987,467; FY2077/78 = 16,325,960,853;
  rise = 2,374,973,386. Less the 13% bonus on the prior
  capital (1,813,628,371) = 561,345,015 beyond the bonus,
  i.e. about 0.56bn, not 0.57bn. Kanchan shares listed after
  acquisition = 4,967,655 shares x Rs 100 = 496,765,500
  (about 0.50bn). The thesis's 0.57bn matches neither the
  beyond-bonus panel arithmetic (0.56bn) nor the Kanchan
  listed shares (0.50bn). The 64.6m gap between those two
  figures is unexplained in the thesis. NEW must-fix item 16:
  either state the panel arithmetic exactly ("about
  NPR 0.56 billion beyond the 13% bonus, per the panel")
  with its method, or delete the amount. Do not keep 0.57bn
  as if sourced.

## Pass 6 — Slop, meta comments, duplicates, filler (systematic scan)

Script scan of all five chapters: no TODO/FIXME/placeholder/
XXX/TBD/"will be added" strings anywhere; no "In this chapter
will" meta-roadmap sentences. No exact duplicate sentence
(8+ words) appears in more than one chapter — the Phase 2
"repeated df/BAFIA passages" are paraphrase repeats, not
verbatim duplicates. Filler counts: "robust" appears 58 times
in total (Ch1 9, Ch2 4, Ch3 15, Ch4 24, Ch5 6), but most uses
are the technical terms HC3-robust / robustness suite, so
the count alone is not a slop finding. Sentences over 55
words number 70 by the script, but most hits are table rows
and headings counted as sentences; the script's long-sentence
count is therefore NOT a finding and is recorded here only
so it is not mistaken for one. The substantive slop findings
remain those in the Phase 2 chapter files (quoted sentences),
not new ones from this scan.

## Pass 7 — Cross-chapter consistency

- Sample, models, df, Wald, R6: consistent across Ch1/Ch3/
  Ch4/Ch5 in every spot check (28, 13/15, df 16/14, Wald
  F(2,14) = 2.954 p = 0.085, R6 F(2,10) = 5.82 p = 0.021).
- Hypotheses: Chapter 1 defines H1-H4 (plus a joint null
  written as H0 vs H1 — the H1 notation collision, already
  in the Phase 2 minor list, CONFIRMED: line 95 uses H1 for
  the joint alternative while H1 is also Hypothesis 1).
  Chapter 4, section 4.2.5 and Table 4.5 decide all four by
  name (all fail to reject at 5% in the baseline; joint test
  rejects only under R6). Chapter 5 contains ZERO mentions
  of "Hypothesis" at all (grep-confirmed). Phase 2 must-fix
  item 8 stands, and is stronger than stated: Chapter 5 does
  not merely fail to decide H1-H4 by name, it never mentions
  hypotheses.
- NEW minor, Chapter 5, section 5.2.2: the two excluded
  observations are described as "resulting from prolonged
  secondary market trading suspensions during merger
  processes around the April 2022 deadline". For HBL/NIB
  the merger had been REJECTED in January 2022, months before
  the April 2022 window, so "during merger processes" is
  misleading in the same way the Phase 1 "during merger
  negotiations" wording was. Reword to "merger-related
  suspension", matching Chapters 3-4.
- Chapter 5, section 5.2.1, claim that banks account for
  "the largest share of aggregate market capitalization"
  cites Bhattarai (2014), Pradhan & Dahal (2016), Timalsina
  (2026). Bhattarai (2014) does not establish that claim
  (see Pass 3). Minor: narrow the citation or drop it from
  that sentence.

## Pass 8 — Full Markdown vs LaTeX diff

Method: word-level diff of normalized text (citations removed,
tables and TikZ excluded), then every flagged block of 8+
words was spot-checked by grep in the actual files, because
the raw diff overstates differences (list numbering, BS dates,
equation markup, and lines containing "&" all misalign it).
Findings after spot-checking:
- NO large missing passage was found. The largest raw-diff
  "deletion" (a ~220-word Chapter 1 paragraph) IS present
  in the .tex file (line 13); it was dropped by the first
  diff script because the line contains "M\&A".
- CONFIRMED real divergence: Chapter 2 .tex opacity paragraph
  (line 139) reads "Morgan (2002) and Flannery et al. (2004)
  establish...", while the Markdown (line 93) reads "Morgan
  (2002) establishes...". Flannery 2004 is LaTeX-only in
  Chapter 2 (it also appears in Markdown Chapter 4, line 389,
  in a different paragraph). Needs a both-or-neither decision
  before submission. The Phase 2 flag stands, verified.
- Form divergence, not content divergence: the Dahal 209
  note is a footnote in .tex (Chapter 2, line 271) and an
  inline parenthetical note in Markdown (line 196). Same
  content; standardize the form when the bib entry is added.
- Small wording divergences found by the diff and confirmed:
  Chapter 4 Markdown "narrower, lower valuation band" vs
  .tex "narrower valuation band"; Chapter 1/5 .tex adds BS
  dates (e.g. 29 Poush 2050 BS) that Markdown omits. These
  are formatting-level, not errors, but they prove the two
  versions are NOT byte-identical in prose and that every
  must-fix must be applied in both and then re-diffed.
- The diff method used here is NOT a substitute for a final
  compiled-PDF proofread. It cannot certify table contents,
  figure placement, or equation rendering.

## Pass 9 — Every in-text citation vs bibliography

LaTeX side: CLEAN. `references.bib` has 55 entries; the
.tex chapters cite exactly those 55 keys; zero bib entries
uncited, zero cited keys missing from the bib. (This is
stronger than Phase 2, which only confirmed the one missing
entry by a targeted search.)
Markdown side: 49 author-year citation forms extracted; all
apparent "missing" matches except one are second/third
authors (Brown, Meckling, Modigliani, Weiss, Williams,
Thomas, Tandon, Napit, Saud, Singh, Shrestha, Ghimire),
corporate authors (NEPSE, NRB, Guidelines), or the hyphenated
MacKinnon-White. The ONE true missing entry is Dahal,
Gurung & Ghimire (2025) — Phase 2 must-fix item 2 stands,
and Pass 9 proves it is the ONLY missing entry by this
method. (Method limit: this checks surname+year presence,
not whether each cited paper's findings are summarized
correctly — that is Pass 3, and Bhattarai failed it.)

## Pass 10 — Independent R1-R8 recomputation + pipeline tests

Fresh NumPy OLS/HC3 recomputation of all eight robustness
specifications against T5, to three decimals, EXACT MATCH:
R1 EPS 2.095 (4.096), BVPS 0.219 (1.858); R2 EPS 5.577 (3.560),
BVPS 0.100 (1.306), delta_E -3.124 (4.003), delta_B -1.758
(1.231), Wald 2.95; R3 ROA 83.760 (79.852), BVPS 0.358 (1.381),
delta_ROA -43.570 (83.671), delta_B -1.901 (1.290), Wald 2.46;
R4 EPS 6.183 (4.508), BVPS -0.642 (1.378), delta_E -4.072
(5.151), delta_B -1.770 (1.335), DPS 4.458 (3.087), Wald 2.77;
R5 EPS 5.993 (4.635), BVPS -0.201 (1.849), delta_E -2.578
(5.521), delta_B -1.880 (1.419), Wald 2.41; R6 EPS 4.336
(3.724), BVPS 0.802 (1.328), delta_E -2.436 (4.755),
delta_B -2.611 (1.517), Wald 5.82; R7 EPS 5.775 (4.145),
BVPS 0.153 (1.632), delta_E -4.043 (4.446), delta_B -1.533
(1.595), Wald 2.37; R8 EPS 5.256 (3.016), BVPS 0.031 (1.300),
delta_E -2.860 (3.807), delta_B -1.812 (1.223), Wald 2.92.
Pipeline dataset tests: 11/11 pass (`test_dataset.py`).
No coefficient, price, DPS value, sample, or table number
was found wrong in any of the 10 passes. The loop's new
errors are all in WORDS about the numbers and the sources,
not in the numbers themselves — which is exactly why the
loop mattered: the arithmetic was never the risk; the
descriptions of it were.

## What the loop changed in the verdict

ADDED as must-fix (in priority order, appended to the
consolidated list as items 14-17):
14. Bhattarai (2014) — rewrite the Chapter 2 paragraph and
    Table 2.1 row: 9 named banks, 2006-2014, variables DPR,
    DY, EPS, P/E, SIZE (no BVPS, no DPS); delete "14 banks"
    and "35 observations" unless a source for them is
    produced (the paper itself gives neither). The
    circular-P/E point about Bhattarai stands — the paper
    does include P/E as a regressor — but the sample and
    variable description must be corrected.
15. BAFIA audited duty — Chapter 2, section 2.3.2, item 2:
    the audited duty is publication for the public within
    nine months, not submission to NRB. Correct it, and
    correct the same section's "establishes the end of
    Chaitra as the statutory publication deadline" to the
    operationalization wording.
16. Kanchan amount — Chapter 1 and Chapter 2: replace
    "approximately NPR 0.57 billion" with the exact panel
    arithmetic ("about NPR 0.56 billion beyond the 13%
    bonus") with its method stated, or delete the amount.
    The 0.57bn figure matches neither the panel arithmetic
    (0.56bn) nor Kanchan's listed shares (0.50bn).
17. Chapter 5, section 5.2.2: "during merger processes"
    for the April 2022 suspensions — reword to
    "merger-related suspension" (the HBL/NIB merger had
    been rejected in January 2022).
DOWNGRADED:
- Phase 2 item 3 (merger citations): narrowed. The dates
  and ratios are verified externally and the bank citations
  exist; only (NRB, 2023) attachment and the Kanchan amount
  remain as errors (now items 16 and the narrowed item 3).
- Phase 2 item 2 (Dahal entry): narrowed to "add the entry".
  The 209 figure is verified from the publisher abstract,
  so deletion of the footnote is no longer the preferred
  fix (pages still to confirm against the publisher PDF).
CONFIRMED, now with stronger evidence:
- Figure notes (item 1): rendered figures viewed.
- Chaitra wording (item 6): statute text read; a third
  Chaitra error found in Chapter 2, section 2.3.2.
- H1-H4 in Chapter 5 (item 8): Chapter 5 never mentions
  "Hypothesis" at all.
- Flannery both-or-neither (cross-chapter file): verified
  in .tex line 139 vs Markdown line 93.
- Ohlson derivation: re-derived, correct.
- Citation system: 55/55 LaTeX-consistent; Dahal 2025 is
  the only missing entry.
STILL NOT DONE, honestly stated:
- Full-text checks for Timalsina (2026) 169 observations
  and Bhandari et al. (2026) "all 19" (bib entries verified,
  findings summaries not).
- KBL-NCC 1 Jan 2023 / 1:1 against a KBL primary source
  (rests on the thesis's bank citation).
- Dahal, Gurung & Ghimire (2025) page numbers against the
  publisher PDF (252-261 from a secondary listing only).
- NEPSE official-close verification for any price row
  (standing Phase 1 limit, unchanged by this loop).
- Supervisor approval of the aggregator-price definition
  (standing Phase 1 limit, unchanged by this loop).
- A final compiled-PDF proofread after fixes are applied
  (the word-level diff cannot certify tables, figures, or
  equations).
