# Main-content loop — Round 2 fixes and LOOP CLOSE

Round 2 reviewers (five, fresh, from scratch): Ch I (`07`),
Ch V (`08`), Ch III (`09`), Ch II (`10`), Ch IV (`11`).
**Every chapter returned MUST-FIX: none.** Round 2 fixes
below are the parent's response to the minors the reviewers
raised, each verified by rebuild + visual check.

## Round 2 fixes applied (thesis files changed)

1. **Ch II Table 2.1 columns → raggedright** (widths
   unchanged, 0.17/0.16/0.15/0.17/0.20). Removes the
   justified narrow-column word stretching and the
   "Sample & Pe-riod" header hyphenation the Ch II
   reviewer confirmed on p. 50. Verified on the new
   p. 50 render: headers break at word boundaries only.
2. **Preamble `\emergencystretch` 1em → 2em** (with
   comment). Removes the Ch IV ~30 pt body overfulls,
   the Ch I 16.62 pt "pre-consolidation" overfull, and
   all Ch II overfulls. No wording changed anywhere.
3. **Ch IV Table 4.5 rebalanced** (Inference 0.12 →
   0.17; Hypothesis/Model/Decision → 0.11; total p-width
   still 0.61). The word "Indistinguishable" no longer
   passes the body edge on PDF p. 87; that overfull fell
   23.10 pt → 1.36 pt.
4. **`\sloppy` in the subsection before-code** (with
   comment). The 4.3.2 title now wraps ("Post-" /
   "Consolidation", PDF p. 95) instead of sticking
   16.17 pt into the margin. Scoped to subsections only.

## Final build state (4-pass script, Termes substitution in the copy only)

- **127 pages, A4, 0 LaTeX errors, 0 undefined
  references, 0 "Label(s) may have changed".**
- Chapter overfulls: Ch I 0, Ch II 0, Ch III 0.27 pt,
  Ch IV max 3.78 pt, Ch V 0. Residuals ≤ 1.3 mm are
  accepted as negligible; the two appendix overfulls
  (76.57 pt, 62.19 pt, appendix lines 14–55) belong to
  the appendices + references phase, not this loop.
- Nothing in this loop changed any number, finding,
  citation key, or sentence of prose. Files changed in
  Rounds 1–2: chapters 02, 03, 04, 05 and
  `config/preamble.tex` only. All changes uncommitted
  and unpushed — Krishna decides.

## Loop status: CLOSED for Chapters I–V

A full fresh review of every chapter now finds zero
fixable format defects. What remains is not loop work:

- **Decision D1 for Krishna:** enumerate labels are bold
  in Ch I/II and plain in Ch III/IV/V. Both render
  correctly; unifying them changes the visible style of
  2–3 chapters, so it was left for his pick (bold
  everywhere or plain everywhere) rather than imposed.
- **Deferred passes (own gates, only on his go-ahead):**
  notation/consistency pass (MPS forms, N/n case, P/E
  `=` vs `\equiv`, caption-N, header naming, asset tags,
  hardcoded section numbers, Ch I M2/M3/M5, Ch II
  N2, Ch III m-1/m-2, Ch IV m3–m5/m7–m9, Ch V M2–M4);
  floats cleanup pass (remove the 14 local
  `\captionsetup` duplicates document-wide, with a
  compile diff proving captions unchanged).
- **Open content items (not format):** EY/MTB expansions
  unverified against the Dahal (2025) paper (Table 2.1
  note states this honestly); Lamsal (2024) summary
  still unverified against the Lamsal paper; Table 2.1
  content completion (critique column, 6 missing obs,
  Kwon/Bhandari periods, Gurung & Dahal 110 vs
  "ten-year", Niraula inclusion, md↔tex sync) — all
  carried on the thesis fix list, none touched here.
- **Next phase:** appendices + references (known
  targets: the two appendix overfulls above).
