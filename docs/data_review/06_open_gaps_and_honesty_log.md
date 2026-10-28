# Data review 6: open gaps, and an honesty log for this audit

## Open gaps (things that would still fail the thesis if a supervisor
## or examiner pressed them, even after this phase 1 pass)

1. **NEPSE official closes: open, and decisive for framing.**
   No MPS_RD row has a verified NEPSE official close. The thesis
   must keep calling its prices cross-checked aggregator prices and
   must keep the analysis labelled draft/disclosed/exploratory
   until a supervisor accepts that definition. This audit did not
   close this gap, and no wording fix closes it either. Closing it
   requires NEPSE daily bulletins or an equivalent primary source,
   row by row, for 28 price dates.
2. **Per-row disclosure proof: open.** The Chaitra deadline argument
   proves a legal requirement, not that each bank's audited
   statements were public by its price date. The DPS announcement
   record supports timing eligibility for dividends, not for the
   full audited statements. Do not upgrade the deadline argument
   into a per-row publication claim in any future edit.
3. **Supervisor approval: open.** The supervisory guidance files in
   `docs/thesis_supervisor/` remain origin-UNCONFIRMED until the
   author confirms whether they are real supervisor rulings or
   drafted guidance. This audit did not confirm their origin, and
   nothing in it should be cited as supervisor approval.
4. **Source register: open and uncommitted.** Local modifications to
   `source_register.md` / `build_source_register.py` remain
   uncommitted and were not reviewed here. The committed register
   still carries older wording on the HBL/NIB halt and GBIME
   November 2022 status that later verification superseded. Review
   and commit (or discard) those modifications separately; do not
   let this data review be read as approving them.
5. **Full re-extraction: not done, and not claimed.** See verdict
   file, "What was NOT done". The original manual verification of
   all 30 bank-years (2026-10-27) is the basis for extraction
   correctness at page level; this audit's basis is recomputation
   from its outputs plus spot checks. If a future reviewer demands
   page-level re-verification, that is a separate, multi-day task,
   and it should be scoped and costed honestly, not pretended to
   have happened here.
6. **Timalsina 2026 sample and Bhandari et al. 2026 wording:**
   carried forward from the chapter reviews as confirm-from-PDF.
   Not data values, but literature claims that still need a PDF
   check before submission.
7. **LaTeX chapters: not audited in this phase.** Phase 1 audited
   data, extraction, analysis, and figures. The LaTeX chapters were
   checked for sync on four wording spots in the previous pull
   review, not audited in full. Phase 2 (chapter review) must
   either audit them in full or state explicitly that the Markdown
   chapters are the reviewed version and the LaTeX is a conversion
   to be diff-checked.

## Honesty log: how this audit was run, so the author can check it

- Every number in files 01-05 was either taken from a tool output
  in this session (pdfinfo page counts, panel recomputation script,
  analysis recomputation script, F3 slope recomputation, PDF text
  extraction, config counts) or read directly from a repository
  file (panel CSV, joined CSV, T1-T6/A4-A6 tables, figure code,
  rendered PNGs). No number was taken from the earlier chapter
  reviews on trust; the analysis recomputation was run again from
  the joined panel with a fresh script, and it reproduced the
  tables.
- Where an earlier review's claim and this audit's recomputation
  could have disagreed, the recomputation was reported, not the
  earlier claim. Example: Cook's distance. The earlier review
  reported max 0.552 for Model 1; this audit recomputed Model 2
  Cook's distance as max 0.490 and reported both, labelled by
  model, instead of overwriting one with the other.
- Where a finding is a rounding explanation (NIMB NAV gaps), it is
  labelled rounding and the numbers are given, so the author can
  check that rounding actually explains them (190.70 rounds to
  191, 198.28 rounds to 198, and so on).
- Where a finding is a definition limit rather than an error (EPS
  denominator timing, F3 bivariate versus FE slopes), it is
  labelled as such, with the numbers that show the limit, rather
  than upgraded into a data error or downgraded into silence.
- The scripts used in this audit were written to /tmp
  (`/tmp/audit_phase1.py`, `/tmp/audit_analysis.py`), not into the
  repository, so they do not pollute the thesis repo. They can be
  re-run by the author against the same CSVs to reproduce every
  recomputation in files 02 and 04. If the author re-runs them and
  gets different numbers, that disagreement should be reported
  back, not smoothed over.
- No thesis chapter, analysis table, figure, panel value, or price
  was changed by this audit. This directory contains reviews only.
  Any fix listed in the verdict file still needs the author's
  explicit approval and a separate edit, as with every previous
  review.
