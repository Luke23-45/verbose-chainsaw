# Phase 2 chapter review: overall verdict

Thesis: VALUE RELEVANCE OF ACCOUNTING INFORMATION BEFORE AND AFTER THE
BANKING CONSOLIDATION WAVE: EVIDENCE FROM NEPALESE COMMERCIAL BANKS.
Repository state at review time: HEAD 9a46350, 2026-10-28.
Review directory: `docs/chapter_review/` (new. This is NOT the earlier
`docs/thesis_review_draft/` directory, which the author deleted after
its items were addressed. Nothing was restored from it, and no file
there was re-corrected here.)
Thesis files changed to write these reviews: NONE. Every file in
`docs/draft/thesis/`, `src/thesis/`, tables, figures, and data is
unchanged. The reviews below are the deliverable; applying any fix
still needs the author's approval for the actual edit, in both the
Markdown and the LaTeX version where the error appears in both.

## How this review was run, so it can be checked

Each chapter was read in full, word by word, in loops, not skimmed:
(1) full argument read, (2) line-by-line proofread, (3) every number
and factual claim checked against its source (tables T1-T6 and
A4-A6, the joined panel, the analysis code and config, or
`references.bib`), (4) slop and meta-comment hunt, (5) LaTeX
spot-check of flagged passages only. A second pass then re-checked
the headline flagged issues directly against the chapters, tables,
panel, code, and bibliography before this verdict was written.
Where the second pass downgraded a claim, the downgrade is stated
in the chapter file's summary below and in
`06_cross_chapter_and_latex_sync.md`; nothing in this verdict
relies on an unchecked assertion.

LOOP UPDATE, 2026-10-28 (after the author rejected the first
Phase 2 review as not acceptable): the review was then run
again as a 10-pass loop against the sources, by the main
reviewer, not delegated. Full record in
`07_loop_log.md`: (1) all chapter numbers recomputed from the
panel, (2) figure notes checked against rendered figures,
(3) literature claims checked online, (4) Ohlson re-derived,
(5) legal/institutional claims checked online, (6) systematic
slop/duplicate scan, (7) cross-chapter consistency,
(8) word-level Markdown-vs-LaTeX diff with grep spot-checks,
(9) every in-text citation vs bibliography, (10) R1-R8
recomputation plus pipeline tests. The loop found NO new
wrong number, and it found four new must-fix word errors
(items 14-17 below), narrowed two Phase 2 items, and upgraded
one "needs check" (Bhattarai 2014) into a proven error after
reading the paper in full text. The verdict below is updated
to include those loop findings; the original 13 items stand
except where the loop explicitly narrows them.

## One-line verdict

The thesis is numerically sound and its headline conclusion is
correct, but it is NOT submittable as written. The numbers in
Chapters 1, 3, 4, and 5 reproduce exactly, the Ohlson derivation
in Chapter 2 re-derives correctly, and the baseline conclusion
(sensitivity-dependent, not conclusive) is stated correctly in
Chapters 4 and 5. What would draw examiner objections is not
arithmetic. It is: figure notes that describe figures that do
not exist as described, citation hygiene in Chapter 2, a
software tool claimed but not used, two internal contradictions
(Chaitra as "statutory" vs operationalization; Chapter 5
"verified stability" vs R6), causal language in results
passages that the design cannot support, and over-wide
universality claims. Fix the must-fix list below and the thesis
is in a different, submittable state. Leave it, and an examiner
who checks one figure note or one bibliography entry will
reasonably doubt the rest.

## Chapter verdicts

### Chapter 1 — Introduction: PASS WITH FIXES
Skeleton matches Chapters 3-4 and the tables: 5 series, 6 years,
pre FY2076/77-2078/79 / post FY2079/80-2081/82, Models 1-2, H1-H4
plus joint test, R3-R8, N = 28 (13 pre / 15 post), 54- and 47-day
gaps, df 14. No number Chapter 1 reports about its own design
is wrong, and it makes no MPS_post or NEPSE-official-close claim.
Must-fix (full quotes and line numbers in `01_introduction.md`):
1. "No empirical study in Nepal has formally evaluated..." —
   soften to "no study identified in the literature reviewed
   in Chapter II".
2. Over-wide quantifiers "almost all / most / routinely" about
   prior studies — restrict to studies actually reviewed.
3. "Four of the five largest banking mergers" — no ranking
   evidence given; "most prominent" is the defensible wording.
4. Board publication "between Ashwin and Poush" stated flatly
   (line 108). Second-pass note: this is NOT a proven
   contradiction — the announcement file's dividend dates are
   not audited-highlights dates, and 29 of 30 dividend dates
   do fall in the window (only NIMB FY2079/80, 2024-02-02,
   Magh, is outside). The fix is to soften line 108 to
   "typically", matching line 143, which already hedges
   correctly. Do not delete the sentence as false.
5. Significance language promising investor/NRB guidance while
   the baseline is non-significant at 5% (joint Wald p = 0.085)
   — temper to exploratory, sensitivity-dependent associations;
   delete "most extensive ... in its history".
6. "Six to nine months later" in the same paragraph as the
   October-January window — Ashadh-end to October-January
   is 3-6 months; 6-9 months only reaches the Chaitra ceiling.
   Resolve to one lag definition.
Minor (11 in file): H1 notation collision, "Huber-White cluster
estimators" conflation, "confirm" for a two-tailed test, plural
"peer institutions" for single benchmark NMB, NMB Kanchan
0.57bn ambiguity (panel total rise is ~2.37bn; 0.57bn is the
amount beyond the 13% bonus — clarify, do not delete),
promotional slop, repeated df/BAFIA passages, unaudited
"strict compliance / complete strict APA 6th" claims.

### Chapter 2 — Literature Review: THEORY SOUND, CITATION HYGIENE NOT
Ohlson derivation re-derived step by step and correct in every
step, and the five gaps map genuinely onto the design choices.
Must-fix (full quotes in `02_literature_review.md`):
1. Line 196 footnote: Dahal, Gurung, and Ghimire (2025),
   209 observations, has NO bibliography entry at all. Add a
   verified entry and confirm 209 from the paper, or delete
   that half of the footnote. (Second pass confirmed: no
   Dahal-Ghimire entry in `references.bib`.)
2. Line 129: calls end-of-Chaitra "the statutory publication
   deadline", contradicting Chapter 3's corrected framing
   (statute: nine months into the subsequent year; Chaitra-end
   is the operationalization). The nine-month Shrawan-Chaitra
   count itself is correct.
3. Lines 138-142: merger dates/swap ratios and the NMB Kanchan
   acquisition (August 2020, ~NPR 0.57 billion) are cited to
   `(NRB, 2023)`, whose bib entry (`nrb2023list`) is only the
   October 2023 list of licensed institutions — it cannot
   support either claim. Dates/ratios belong to the bank
   filings alone; Kanchan needs its own source or deletion.
4. Deliberately no fourth must-fix: the file states this
   rather than inventing one. Remaining citation problems are
   unverified attributions, not proven misattributions.
Minor (15-item fix list in file): "three building blocks"
followed by four; "tangible net assets" for BVPS (which
includes goodwill); "linear transformation of itself" for
P/E; "mathematically necessary"; "reporting ceilings" and
"mandatory cash dividend distributions" (wording checks, not
proven falsehoods); Gap 1 directional wording vs Chapter 4
(post BVPS slope -1.658, not an anchor); "directly bridges
each gap" overstating a baseline Wald result that does not
reject at 5%; Table 2.1 omissions with no selection criterion
and missing "(Circular P/E)" tags; five quoted slop sentences.
NOT checked: the full text of any cited paper, bank report,
NRB document, or NEPSE publication — every specific sample
size/finding is therefore listed as "needs check against the
paper's full text" (starting with Bhattarai 2014's 35
observations, which cannot come from a balanced 14-bank x
2006-2014 panel and needs its construction explained), not
claimed verified.

### Chapter 3 — Methodology: NUMBERS SOUND, DESCRIPTION ERRORS REMAIN
Every Table 3.1 price, gap, date, EPS, BVPS, DPS, restatement
amount, and df recomputed matches the panel, joined panel, or
tables, and the code matches the stated models, 5-day window,
Post definition, and R1-R8 suite. Key honesty statements are
correct: NEPSE official closes explicitly unverified,
ShareSansar agreement explicitly not independent verification,
estimates framed as associations, not causal merger effects.
Must-fix (full quotes in `03_methodology.md`):
1. Line 110 Group-equity sentence is false as a general
   statement — GBIME Group total equals attributable equity,
   but HBL/NMB Group totals include NCI (e.g. NMB FY2078/79:
   538,470,376). Scope it to GBIME. (This is the same flaw
   flagged in the Phase 1 loop resolution check; the new
   sentence did not fix the scope.)
2. Section 3.6.3 never states the reference distribution —
   code uses `use_t=True`, but the chapter never says
   intervals use Student's t on residual df, not 1.96.
3. Line 291 claims `linearmodels` — zero matches in
   `data_analysis/analysis/` Python files (second pass
   confirmed); estimation is statsmodels OLS. Delete it.
4. Line 76 presents end-of-Chaitra as the statutory deadline,
   while line 173 correctly calls it an operationalization —
   internal contradiction. Unify on the Chapter 3 line 173
   wording everywhere.
5. Line 110 "official secondary capital market trading
   archives" contradicts the chapter's own aggregator /
   NEPSE-unverified disclosure. Delete or replace with
   "capital market data aggregators".
6. Line 267 says HC3 "heavily discounts high-leverage
   observations" — the printed formula divides by
   $(1-h_{ii})^2$, which inflates high-leverage residuals;
   the verb is backwards. (Same error in Chapter 4, line 322.)
Minor (7 in file): diagram `l_t` for lambda; Post-absorption
equation equating an indicator to a sum of coefficients;
"mathematically" appropriate purposive sampling; uncited
"standard Nepalese banking valuation convention"; VIF "~30"
vs bivariate 20.25 with no specification named; Microsoft
Excel claimed with no Excel artefact found in repo scripts;
VIF screening threshold stated with no action (T6 VIF is
1.16, never triggered).
NOT checked: BAFIA Section 59(2) text itself; all 5,663
report pages re-read; live aggregator/NEPSE re-fetch; NRB
population history, GBIME "largest bank" claim, merger
dates/ratios, and literature citations against primary
sources; analysis test suite run; rendered figures re-viewed;
full LaTeX diff.

### Chapter 4 — Results and Discussion: NUMBERS CORRECT, FIGURE NOTES WRONG
All 60 Table 4.1 descriptive cells, all Table 4.2 correlations
and stars, Model 1, Model 2, hypotheses, R2-R8, diagnostics,
and specification comparison reproduced by independent
recomputation (see file for full values; two third-decimal
rounding notes only, explicitly NOT errors). Must-fix (full
quotes in `04_results_discussion.md`):
1. Figure 4.2 note (line 106): claims 5 variables and linear
   fit lines. F1 code plots only MPS_RD/EPS/BVPS, scatter +
   KDE, no regression lines. (Second pass confirmed from
   `f1_scatter_matrix.py`: vars are MPS_RD, EPS, BVPS only.)
2. Figure 4.3 note (line 112): claims asterisks for
   significance. F2 heatmap code annotates two-decimal values
   only, no asterisks. (Second pass confirmed.)
3. Figure 4.6 text/note (lines 289, 295): claims all eight
   specifications and book-value parameters. A2 code plots
   7 specs (R3 omitted) and EPS coefficient + delta_E only.
   (Second pass confirmed: EPS_RUN_IDS excludes R3.)
4. Figure 4.7 note (line 330): swaps top-left/top-right —
   code order is top-left Normal Q-Q, top-right Residuals vs
   fitted. (Second pass confirmed from
   `_diagnostics_panel.py` PANEL_TITLES and axis order.)
5. Unlabelled causal explanations in Results (lines 61-64):
   "reflects macroeconomic tightening", "induced earnings
   volatility", "reflects statutory reserves", "driven by
   regulatory restrictions" — none is a regressor. Soften to
   consistency statements or move under the section 4.3.2
   disclaimer.
6. Line 253: "corporate consolidation induced non-trivial
   joint adjustments" after a fail-to-reject at 5% — change
   "induced" to "is consistent with".
7. Line 322: HC3 "weights by $(1-h)^2$, effectively
   downweighting" high-leverage observations — backwards, as
   in Chapter 3. Also Table 4.7 "Controlled via HC3" overclaims.
Minor (12 in file): "three" factors but four bullets;
"unconditioned"; figure-title symbol MPS_RD vs MPS^{RD};
mechanism 3 stated as cause without source/hedge; Kwon and
Wang "indicate that amalgamations generate" overstatement;
R5 "demonstrates" and R6 "clean specification"; "unbiased
benchmark" / "econometrically mandatory"; Table 4.1 note
"verified market closing series" (should be "cross-checked
aggregator"); Wald tests called "two-tailed"; discussion
openings reprinting full SE/t/p apparatus; F6 note silent
that the price line connects through open markers; emotive
adjectives.
Correct framing to keep as the model: section 4.3.2 ("not as
proven causal effects, but as suggestive structural
tendencies") and the R6 "empirical association ... rather
than as a causal merger effect" sentence, plus the F3 and F4
notes, which are correct.
NOT checked: rendered figure PDFs/PNGs (code only); Cook's /
Breusch-Pagan / VIF independent recomputation (statsmodels /
scipy unavailable in that session — chapter-vs-T6 agreement
only); literature accuracy for cited prior studies, NRB
directive, and prior-study sample descriptions; Chapters 1/3
and proposal; full LaTeX diff; NEPSE official-close
verification and supervisor approval (standing limits).

### Chapter 5 — Summary and Conclusion: NUMERICALLY FAITHFUL, SUBSTANTIVELY NOT YET SUBMITTABLE
No number drift found: Model 1, Model 2, post slopes, Wald
F(2,14) = 2.954, p = 0.085, R6 F(2,10) = 5.82, p = 0.021, R4
df = 13, pooled EPS 4.882, correlations, VIF 1.16, all
descriptives, sample 28/13/15, df 16/14 all match Chapter 4
and T3/T4/T5. Percentage changes reproduce from Chapter 4's
rounded means (unrounded differ by at most 0.29pp, a shared
rounding artefact, not a Chapter 5 error). Must-fix (full
quotes in `05_summary_conclusion.md`):
1. Line 81 — "verified parameter stability" contradicts R6.
   Failure to reject in R3/R4/R5/R7/R8 does not verify
   stability, and R6 in the next paragraph rejects it at 5%.
   Reword to non-rejection plus a pointer to R6. (Second
   pass confirmed both passages.)
2. Hypotheses H1-H4 never decided by name. Chapter 1 defines
   them, Chapter 4 decides them (all fail to reject at 5% in
   the baseline; joint test rejects only under R6), Chapter 5
   never uses H1-H4 at all. (Second pass confirmed: no H1-H4
   mention in Chapter 5.) Add an explicit decision
   paragraph/table in section 5.3.
3. Line 124 — new unverified premise: "public dissemination
   remains dispersed across corporate websites and print
   media" has no supporting passage in Chapters 1, 3, or 4.
   Cite a source or reword as a proposal.
4. Line 24 — "universally". Chapter 1 says "almost
   exclusively" / "almost all", not universally. Change to
   "almost all".
Minor (7 in file): "primarily priced" from two insignificant
slopes (qualify as point-estimate pattern); delete "exactly"
before VIF = 1.16; "conclusions are established" overstates
the sensitivity-dependent result; "ceilings" restricting
halts to a "minimum" number (change to "maximum" / "at most
a few sessions"); "cross-sectional difference-in-differences"
(delete "cross-sectional" — DiD is a panel design); trailing
space; R7 pro-forma timing note in Chapter 3 but not repeated
in the T5 note (not counted as a Chapter 5 error).
NOT checked: full LaTeX diff; refitting Models 1/2 from the
raw panel in that review; Chapters 1-4 in full (only cited
passages); bibliography entries for Chapter 5 citations; TU
Guidelines p. 15 claim against the guideline itself; NRB
32-to-20 history beyond Chapter 3's citation; rendered
PDF/figures other than T3/T4/T5; feasibility of proposed
future work.

## Consolidated must-fix list (priority order)

1. Chapter 4 figure notes: correct F1 (3 variables, no fit
   lines), F2 (no asterisks), A2 (7 specs, EPS only), F5
   (Q-Q top-left, Residuals top-right) — in both versions.
2. Chapter 2 bibliography: add the missing Dahal, Gurung,
   and Ghimire (2025) entry with 209 verified from the paper,
   or delete that footnote half.
3. Chapter 2 / Chapter 3 citations: remove `(NRB, 2023)`
   support for merger dates/ratios and Kanchan; cite bank
   filings / a Kanchan source, or delete the amount.
4. Chapter 3 line 291: delete `linearmodels` (and Excel if
   no artefact can be produced).
5. Chapter 3 + Chapter 4 HC3 verb: replace "discounts /
   downweights" with the correct direction (division by
   $(1-h)^2$ inflates high-leverage squared residuals).
6. Chaitra wording, everywhere: statute = nine months into
   the subsequent year; end-of-Chaitra = operationalization.
   Fix Chapter 2 line 129, Chapter 3 line 76, and any
   Chapter 1 echo of the statutory phrasing.
7. Chapter 3 line 110: scope the Group-equity sentence to
   GBIME, and replace "official secondary capital market
   trading archives" with aggregator wording.
8. Chapter 5 line 81: replace "verified parameter stability"
   with non-rejection plus R6 pointer; add the H1-H4
   decision paragraph/table.
9. Chapter 4 causal language: soften lines 61-64 and line 253
   ("induced" to "is consistent with"); keep section 4.3.2
   disclaimer as the governing framing.
10. Chapter 1 universality and significance: soften "no study",
    "almost all / most / routinely", "four of the five
    largest", and investor/NRB guidance to the exploratory,
    sensitivity-dependent result actually obtained.
11. Chapter 1 line 108: change "between Ashwin and Poush"
    to "typically between Ashwin and Poush", matching
    line 143; resolve the 3-6 vs 6-9 month lag to one
    definition.
12. Chapter 5 line 124: source the "dispersed dissemination"
    premise or reword it as a proposal; line 24: "universally"
    to "almost all".
13. Chapter 3 section 3.6.3: state that intervals use
    Student's t on residual df, not 1.96.
14. Chapter 2 Bhattarai (2014) (LOOP, proven by full-text
    read): rewrite the paragraph and Table 2.1 row — 9 named
    banks, 2006-2014, variables DPR, DY, EPS, P/E, SIZE (no
    BVPS, no DPS). Delete "14 banks" and "35 observations"
    unless a source for them is produced; the paper gives
    neither. The circular-P/E point about Bhattarai stands.
15. Chapter 2 section 2.3.2 BAFIA (LOOP, statute text read):
    the audited duty is publication for the public within
    nine months, not submission to NRB; and the same
    section's "establishes the end of Chaitra as the
    statutory publication deadline" must become the
    operationalization wording.
16. Kanchan amount (LOOP, panel arithmetic): Chapter 1 and
    Chapter 2 "approximately NPR 0.57 billion" matches
    neither the beyond-bonus panel arithmetic (0.56bn) nor
    Kanchan's listed shares (0.50bn). Replace with the exact
    panel arithmetic and method, or delete the amount.
17. Chapter 5 section 5.2.2 (LOOP): "during merger processes"
    for the April 2022 suspensions — reword to
    "merger-related suspension" (the HBL/NIB merger had been
    rejected in January 2022).
Loop narrowing of earlier items: item 2 is now "add the
Dahal, Gurung & Ghimire (2025) entry" (209 verified from the
publisher abstract; pages 252-261 still to confirm against
the publisher PDF) rather than "add or delete"; item 3 is
narrowed to dropping (NRB, 2023) from the merger sentences
(the dates/ratios are verified externally and bank citations
exist) plus the Kanchan amount (now item 16).
Then the minor lists in each chapter file, in the order
given there. No must-fix item changes a coefficient, price,
DPS value, sample, or table number.

## What was NOT done, stated so it is never misread

- No compiled-PDF proofread after fixes (fixes are not yet
  applied, so this cannot exist yet). The word-level diff
  in the loop cannot certify tables, figures, or equations.
- No re-read of all 5,663 report pages, no live
  aggregator/NEPSE re-fetch.
- Full-text checks still outstanding after the loop:
  Timalsina (2026) 169 observations, Bhandari et al. (2026)
  "all 19", KBL-NCC 1 Jan 2023 / 1:1 against a KBL primary
  source, Dahal, Gurung & Ghimire (2025) page numbers
  against the publisher PDF.
- No thesis, table, figure, or data file was changed, in
  Phase 2 or in the loop. Reviews only.

## Phase 2 conclusion (after the loop)

Phase 2 is complete as a review, and the loop is complete as
a check on that review. The thesis does not need
re-extraction or re-estimation: 10 passes found no wrong
coefficient, price, DPS value, sample, or table number.
It needs the 17 must-fix items above, applied in both
versions, plus the minor lists. After those, the remaining
open items are the standing limits from Phase 1 (NEPSE
official-close verification never done; supervisor approval
of the aggregator-price definition still the gate for
final, non-draft framing) and the full-text literature
checks listed as NOT checked above. The loop's most
important correction to the first review is a warning in
itself: the first review listed Bhattarai 2014 as "needs
check"; the paper, read in full, proves the thesis's
description of it wrong. Any literature summary not yet
read in full text should be treated the same way until it
is checked.
