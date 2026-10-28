# Cross-chapter review and LaTeX sync note

Companion to `00_overall_verdict.md`. This file collects only
issues that cross chapter boundaries or the Markdown/LaTeX
boundary. Chapter-specific issues stay in their chapter files.
Nothing here changes the thesis; it is a review note only.

## Cross-chapter contradictions (fix in every place listed)

1. **Chaitra: statutory vs operationalization.** Chapter 2
   line 129 calls end-of-Chaitra "the statutory publication
   deadline" and then, in the next paragraph, calls it the
   study's operationalization. Chapter 3 line 76 presents
   end-of-Chaitra as the statutory deadline while line 173
   correctly calls it an operationalization. Chapter 1
   line 108 says "operationalizing the statutory nine-month
   reporting deadline ... at the end of Chaitra", which is
   the correct structure and should be the template:
   statute = nine months into the subsequent fiscal year;
   end-of-Chaitra = the study's operationalization. Fix
   Chapters 2 and 3 to that wording; do not let any chapter
   imply the statute names Chaitra.
2. **HC3 direction, twice.** Chapter 3 line 267 ("heavily
   discounts") and Chapter 4 line 322 ("weights by
   $(1-h)^2$, effectively downweighting") make the same
   backwards claim about the same formula, which divides
   squared residuals by $(1-h_{ii})^2$ and therefore
   inflates high-leverage residuals. Fix both, in both
   versions, with identical correct wording, or an examiner
   will find the second one after the first is fixed.
3. **Group equity scope.** Chapter 3 line 110 is the only
   place the Group-equity claim appears, but its wording
   ("Group-level schedules in raw extractions reflect equity
   attributable ... and exclude non-controlling interest")
   is contradicted by the raw files for HBL/NMB Group rows,
   where total equity does include NCI. Scope it to GBIME
   (see `00_overall_verdict.md`, Chapter 3 item 1). No other
   chapter repeats the claim, so this is a single-place fix
   with a cross-file cause.
4. **H1-H4 lifecycle.** Chapter 1 defines H1-H4. Chapter 4
   decides them (baseline: all fail to reject at 5%; joint
   test rejects only under R6). Chapter 5 never names them.
   Add the decision paragraph/table in Chapter 5 section
   5.3 so the thesis closes the loop it opened. Do not
   change Chapter 4's decisions to fit Chapter 5; change
   Chapter 5 to report them.
5. **"Verified stability" vs R6.** Chapter 5 line 81 says the
   robustness suite "verified parameter stability"; the
   next paragraph in the same section reports R6 rejecting
   at 5% (F(2,10) = 5.82, p = 0.021). Chapter 4 states the
   same pair correctly (baseline non-rejection, R6
   rejection, sensitivity-dependent). Chapter 5 must be
   brought into line with Chapter 4, not the other way round.
6. **Universality drift.** Chapter 1: "no study", "almost
   all", "most", "routinely". Chapter 5 line 24 upgrades
   Chapter 1's "almost exclusively" to "universally".
   Chapter 2 line 250: "directly bridges each gap" upgrades
   a baseline Wald result that does not reject at 5%.
   Rule for all three chapters: a later chapter may not
   strengthen an earlier chapter's claim. Fix by downgrading
   the later wording to the earlier wording.
7. **Figure-note pattern.** The correct notes (F3, F4) and
   the wrong notes (F1, F2, A2, F5) are all in Chapter 4,
   but the cause is cross-cutting: notes were apparently
   written from memory of what a figure should show, not
   from its generation code. After fixing the four notes,
   re-check every remaining figure note (F6, A1, A3) against
   its code before submission, even though no error was
   found in them in this review — the pattern, not just the
   instances, is the risk.
8. **Causal language governance.** Chapter 4 section 4.3.2
   ("not as proven causal effects, but as suggestive
   structural tendencies") is the governing disclaimer, and
   Chapter 5 correctly stays within it. The violations are
   local: Chapter 4 lines 61-64 and 253, and any mechanism
   sentence that states a cause without a hedge. Fix the
   local sentences; do not weaken the section 4.3.2
   disclaimer, which is what makes the rest defensible.
9. **"Official" price language.** Chapter 3 line 110
   ("official secondary capital market trading archives")
   and Chapter 4 Table 4.1 note ("verified market closing
   series") both overstate the aggregator position that
   Chapters 3 and 4 otherwise state correctly (cross-checked
   aggregator prices, NEPSE official closes unverified).
   Replace both with "cross-checked aggregator" wording.
   This is the same standing limit as Phase 1; no new
   verification was done or is claimed here.

## LaTeX sync: what was and was not checked

- Checked by spot-grep of flagged passages only: Chapter 1
  flagged passages (e.g. "four of the five largest",
  Ashwin-Poush, investor bullet) appear in
  `chapter_01_introduction.tex`; Chapter 2 flagged passages
  mostly appear in both, with two Markdown-only artefacts
  (Gurung footnote form, "2023cbr" citation) and one
  LaTeX-only addition (Flannery 2004 citation in the
  opacity paragraph, absent from Markdown — check whether
  it belongs in both or neither); Chapter 3 must-fix 1, 3,
  4, 5 appear in `.tex` in the same wording; Chapter 4
  figure-note errors, "three factors", and swapped F5
  labels appear in `.tex`; Chapter 5 must-fix passages
  appear in `.tex` at the line numbers given in its file.
- NOT checked: a full line-by-line Markdown-to-LaTeX diff
  for any chapter, the front matter, appendices, or
  `references.bib` rendering. A passage not flagged in
  this review is therefore NOT certified as in sync.
  Before submission, run a full diff (e.g. via the
  conversion script's output) and resolve every divergence
  that is not pure LaTeX formatting.

## Numbers that agree across chapters (second-pass spot checks)

- Sample: 28 clean (13 pre / 15 post) in Chapters 1, 3, 4, 5.
- Model 2: pre EPS 5.577, pre BVPS 0.100, delta_E -3.124,
  delta_B -1.758, Wald F(2,14) = 2.954, p = 0.085, in
  Chapters 4 and 5 and tables T4/T5.
- R6: Wald F(2,10) = 5.82, p = 0.021, delta_B -2.611
  (SE 1.517), in Chapters 4 and 5 and table T5.
- DPS collapse: pre mean 6.06, post mean 1.40, -76.90%,
  12 of 15 post rows zero, in Chapters 4 and 5.
No cross-chapter number drift was found in these spot
checks. That statement covers the spot checks listed here,
not every number in the thesis — the chapter files contain
the full per-chapter number checks.
