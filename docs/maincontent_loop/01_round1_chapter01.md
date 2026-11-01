# Main-content loop — Round 1, Chapter I review (reviewer report + disposition)

Reviewer: per-chapter format review, no files edited. Verified by parent
against the chapter file before disposition below.

## Reviewer findings

- MUST-FIX: none. Zero \ref/\eqref, all 34 citation keys resolve in
  references.bib (57 entries), all 8 labels unique across chapters +
  appendices, braces 193/193, environments balanced (enumerate 5/5,
  itemize 9/9, equation 9/9), zero hardcoded formatting commands, no
  tables/figures/footnotes.
- MINOR M1: 9 displayed hypothesis equations (lines 81–134) are
  numbered (1.1)–(1.9) but never labelled or cited.
- MINOR M2: `Model~2` tie used once (line 17) vs plain `Model 1/2`
  elsewhere.
- MINOR M3: fiscal-year ranges written both as `FY 2076/77--2078/79`
  and as `FY 2076/77 to FY 2081/82`.
- MINOR M4: lead-in paragraphs before lists (lines 42, 54) — check
  only on compiled pages for stranding at a page foot.
- MINOR M5: notation typeface split — line 33 uses upright
  $\text{MPS}_{it}$ / $\text{EPS}_{it}$ / $\text{P/E}_{it}$ while the
  rest uses $MPS^{RD}$; $\mathit{Post}_t$ occurs once (line 196).
- MINOR M6 (observation): TOC chapter line renders `CHAPTER I:
  Introduction` while the body heading renders `CHAPTER I` /
  `INTRODUCTION` — preamble behaviour, not a chapter defect.

## Parent disposition (do not re-open without new evidence)

- M1: KEPT, not a fix. Numbered hypothesis equations are legitimate
  even when uncited; adding unused labels or unnumbering them would
  be churn. No change.
- M2, M3, M5: DEFERRED to the later notation/consistency pass
  (macros + range style), to be applied uniformly across all
  chapters in one pass, not chapter by chapter.
- M4: CHECK at compile-visual stage (Chapter I pages in the compiled
  PDF); add a keep-with-next guard only if a lead-in actually strands.
- M6: KEPT. TOC title-case vs body uppercase is the preamble's
  designed TOC style.
- Chapter I PASSES Round 1 with no format fix applied.
