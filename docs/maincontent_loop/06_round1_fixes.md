# Main-content loop — Round 1 fixes applied (format only, compile-verified)

All fixes below change layout, numbering display, or cross-reference
targets only. No number, finding, citation key, or table/figure
content was changed, except where a fix itself required a target
change (MF1 reference target, M1 intro-list titles aligned to the
actual headings, which are the source of truth). Thesis files
changed in this round: chapters 02, 03, 04, 05 and
config/preamble.tex. (Front-matter and main.tex diffs in git
status belong to earlier phases, not this round.)

## Chapter II
- M1: Table 2.1 converted from a non-breaking `table` float to a
  `longtable` with a repeated header (firsthead + head). All 22
  rows preserved (count verified); the 11 rows previously lost
  off-page (joshi2023 onward) now print across pages 50–51+ with
  the header repeated.
- M2: column widths narrowed 0.18/0.18/0.16/0.18/0.22 to
  0.17/0.16/0.15/0.17/0.20 (sum 0.85 \textwidth; +60 pt tabcolsep
  = 428.2 pt, inside 433.13 pt).
- M3: footnote line 271, both \citep changed to \citet (names
  no longer duplicated).
- M4: BAFIA enumerate (line 186) given the chapter's bold-label
  option `[label=\textbf{\arabic*.}]`.
- N1: table note added after the longtable defining MPS, EPS,
  BVPS, DPS, ROA, ROE, DPR, DY, P/E, OLS, RIV, M\&A, BSE from
  thesis prose. EY and MTB are reproduced as labelled in the
  Dahal row with an explicit statement that their expansions are
  not defined in the thesis text — OPEN ITEM, not invented.

## Chapter III
- M-1: Figure 3.1 caption moved from above the TikZ diagram to
  below it (after \end{tikzpicture}, before \end{figure});
  \label stays immediately after \caption; in-text reference
  unaffected. Caption now renders below the diagram (verified
  visually, PDF p. 64).
- m-5: bold lead-in `\textbf{Price-to-Earnings (P/E) Ratio:}`
  added before the Strict Exclusion paragraph, matching the
  sibling variable blocks.
- m-7 (preamble): `\AtBeginEnvironment{quote}{\singlespacing}`
  added beside the tabular/longtable hooks (FOM p. 20 lists
  quotations as single-spaced; this thesis has exactly one quote
  block, the freshness rule).
- Visual find (not in the reviewer report): the TikZ
  "Fundamental Independent Variables" label overlapped the
  Fixed Effects Control box's top edge. Fixed by lowering the
  fe box from y = -1.5 to y = -1.9 (arrow endpoint unchanged);
  verified visually, no other node moved.

## Chapter IV
- MF1: line-296 reference `tab:model2_vr` (undefined, rendered
  "??") changed to `tab:t4_model2`, the Model 2 table — the
  two-way fixed-effects estimates the note contrasts with the
  bivariate OLS lines.
- MF2: Table 4.4 spec `lcccccc` (7 cols) corrected to `lccccc`
  (6 cols, matching every row).
- MF3 (all six overwide tables reworked; widths verified by
  compile, zero overfull remaining):
  - 4.3: col 1 to p{0.17\textwidth} (was l; narrowed twice:
    0.21 left +10.88 pt, 0.17 clears it).
  - 4.4: col 1 to p{0.26\textwidth}.
  - 4.5: all text columns to p with raggedright (Hypothesis
    0.13, Model 0.12, Null 0.11, Decision 0.13, Inference 0.12;
    Estimate/p-value stay centered). Decision widened 0.11 to
    0.13 and Inference narrowed 0.14 to 0.12 after the first
    render still hyphenated "Re-ject"; final render shows
    "Fail to / Reject" cleanly. Long words ("insignificant")
    still hyphenate in the 0.12 Inference column — unavoidable
    at that width, accepted.
  - 4.6: local \tabcolsep 4 pt + p-columns 0.19/0.13/0.12/0.14/
    0.12/0.12 + centered n column.
  - 4.7: col 1 to raggedright p{0.22\textwidth} (0.26 left
    +13.00 pt, 0.22 clears it).
  - 4.8: local \tabcolsep 4 pt + Specification p{0.18\textwidth}
    + Assessment raggedright p{0.20\textwidth}.
- MF4: chapter numbers now Roman in body AND TOC, sections /
  tables / figures / equations stay Arabic, appendices stay
  Alph. Implementation in config/preamble.tex:
  `\thechapter` = \Roman{chapter}; \thesection, \thetable,
  \thefigure, \theequation pinned to \arabic{chapter} forms;
  \thesisAppendixHeadings restores chapter-based forms after
  \appendix (so appendix tables are A.1, not 6.1). Verified:
  body "CHAPTER IV", TOC "CHAPTER I: Introduction", sections
  "4.1", "Table 4.1/4.8", "Table A.1", "Figure A.1", appendix
  heading "APPENDIX A". A bare global \thechapter change was
  NOT used, per the reviewer's warning.
- m1: Introduction Results list items 3–6 aligned verbatim to
  the actual subsection titles (4.2.3, 4.2.4, 4.2.5, 4.2.6).
- m4: Table 4.2 header $\mathit{MPS}^{RD}$ wrapped in \textbf,
  matching EPS/BVPS/DPS/ROA headers.

## Chapter V
- F1: Table 5.1 widths 0.22/0.18/0.15/0.20/0.15 narrowed to
  0.21/0.17/0.14/0.19/0.14 (sum 0.85; +60 pt = 428.2 pt).
  The 16.51 pt overfull is gone.

## Compile verification (build script, TeX Gyre Termes substituted
## for Times New Roman in the copy only, as in the front-matter phase)
- Final build: 127 pages, A4, 0 LaTeX errors, 0 undefined
  references, 0 "Float too large" warnings, 0 overfulls in any
  chapter table range (4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 5.1, 2.1).
- Visually inspected: Table 2.1 continuation page (repeated
  header, lost rows restored, margins respected), Chapter IV
  heading page (Roman chapter, Arabic section), Figure 3.1
  page (caption below, label overlap fixed), Table 4.5 page
  (margins respected, no mid-word hyphenation except long
  words in the narrow Inference column).

## Deferred to later passes (NOT done in Round 1)
- Notation/consistency pass: MPS form variants, N/n case,
  $F$ without df, $\delta_{ROA}$ form, bare $\mathit{MPS}$,
  unhatted table parameters vs hatted prose, P/E `=` vs
  `\equiv`, caption-N inconsistency, Table 4.3/4.4 header
  naming (Parameter/Coefficient vs Model Parameter / Term),
  figure-note codebase-asset tags vs table notes, hardcoded
  "Section~" literals (Ch IV 16×, Ch V), Ch I M2/M3/M5,
  Ch II N2/N3, Ch III m-1/m-2, Ch IV m3/m6/m9/m10, Ch V M2.
- Floats cleanup pass: remove the 14 local \captionsetup
  duplicates of the global setting (document-wide, with a
  compile diff proving captions unchanged).
- Document-wide tolerance decision for body-text overfulls
  (Ch III m-6, Ch IV m5, Ch V M1; largest ~30 pt) — rewording
  is out of scope; \emergencystretch/\sloppy to be evaluated
  only with a compile check.
- Dead equation labels (Ch I M1, Ch III m-3): kept, not a defect.
- Ch IV m7 (subsubsection TOC-orphaned at tocdepth 2): kept;
  changing tocdepth changes the whole TOC, a campus decision.
- Open content items for Krishna (not format): EY/MTB
  expansions against the Dahal (2025) paper; Lamsal (2024)
  summary page-check (from the earlier fix rounds).
