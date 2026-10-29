# LaTeX architecture redesign — design document (no thesis files changed)

Date: 2026-10-29. Status: DESIGN ONLY. Nothing in `src/thesis/` has been
changed by this document. Implementing it needs Krishna's explicit approval,
and it must be done in the phases below, with a compile-and-diff gate after
each phase. A thesis edit is never a side effect of a redesign.

## 0. Implementation update (2026-10-29, config phase done)

On Krishna's instruction ("create a new dir where the config latex file
would sit and our thesis would use them"), the config phase was
implemented with one naming change from Section 2: instead of a
`.sty` at the thesis root plus `preamble/`, the config lives in
`src/thesis/config/` as plain `\input` files, which removes any
package-search risk. Files: `config/preamble.tex` (old `main.tex`
preamble, moved verbatim, plus the four shared assembly commands and
one new package, `threeparttable`, for the future table environment),
`config/metadata.tex`, `config/macros.tex` (defined, not yet used in
chapters), `config/floats.tex` (defined, not yet used in chapters).
`main.tex` is now assembly only; `front/titlepage.tex` reads metadata
commands with values copied character-for-character. Chapters, other
front pages, and appendices are untouched. Compile verification on a
TeX Live machine is still outstanding (no XeLaTeX on this VM) and
remains the gate before this phase is called done.

## 1. Diagnosis: what is actually wrong now (measured, not asserted)

The current structure is already partly modular (chapters, front matter,
appendices, figures, bibliography are separate files), so the problem is not
"one big file". The problem is where formatting decisions live.

### 1.1 `main.tex` does three jobs at once (244 lines)

1. Style: every package, every margin, font, spacing, heading format,
   TOC format, caption format, bibliography format, and page style.
2. Assembly: the order of front matter, chapters, references, appendices,
   and the page-numbering switches between them.
3. Mid-document style changes: the `plain` page style is defined once for
   front matter and then redefined inside the body for the main body, and
   the chapter heading format is redefined again just before the appendices.

Consequence: changing any style means editing the assembly file, and the
assembly file is the one file whose order must never be touched casually.

### 1.2 Formatting is repeated inside content files

Measured in `src/thesis/`:

- 13 `table` environments across chapters and appendices, plus 2 more
  `tabular` blocks in Chapter 2 that are not floats. Almost every table
  repeats the same sequence: `\centering`, `\small`, a local
  `\captionsetup`, a bold header row, then `\vspace{4pt}` and a
  `\footnotesize` italic "Note." inside a `minipage`. The local
  `\captionsetup` alone is repeated 14 times in chapter and appendix files.
- 10 `\includegraphics` calls with hard-coded widths from 0.72 to 0.92 of
  `\textwidth`. The 0.88 default also lives inside `convert_chapters.py`,
  so the converter and the hand-edited chapters can drift apart.
- Front-matter pages hard-code their own spacing: title page uses
  0.5, 2.5, 2.5, 0.8, 0.3 cm gaps; approval sheet, authorship, and research
  committee pages use 1.5, 2.5, 2.0, 3.5 cm gaps and signature rules of
  4.0, 4.5, 5.0, 5.5, 5.8, 6.5, 7.5 cm. There is no shared "front page"
  layout, so a spacing change has to be made page by page.
- Zero `\newcommand` definitions exist outside `main.tex`. Notation is
  typed inline everywhere: `$\mathit{MPS}^{RD}$` appears 38 times and
  `$\mathit{Post}_t$` 25 times in chapters alone, plus repeated
  `$\mu_i$`, `$\lambda_t$`, `$\beta_E$`, `$\beta_B$`, `$\delta_E$`,
  `$\delta_B$`. A notation change today is a find-and-replace across five
  chapters, with a real risk of missing one occurrence.
- `longtable` is loaded but never used (no `\begin{longtable}` in any
  chapter or appendix). It is dead weight in the preamble, kept only
  because nobody has proved it unused until now.
- Metadata is repeated: title, author, roll number, registration number,
  campus, and date appear in the `main.tex` comments, in
  `front/titlepage.tex`, and in prose. The submitting name on the title
  page is still an unconfirmed item; a metadata file would make correcting
  it a one-line change instead of a hunt, but this design does not change
  the value.

### 1.3 Build is undocumented and unrepeatable as configured

- Engine is XeLaTeX plus BibTeX (stated in a `main.tex` comment), but
  there is no `latexmkrc`, no build script, and no output directory.
- The repo `.gitignore` does not exclude `.aux`, `.log`, `.out`, `.toc`,
  `.lof`, `.lot`, or `.pdf`, so compiling in place pollutes the working
  tree with untracked build artifacts.
- No compiled thesis PDF exists in the repo, and no baseline PDF has ever
  been produced from the current sources. That is the first risk to close:
  a restructure cannot be proved output-identical without a baseline.

### 1.4 What is NOT wrong, and must not be "fixed" by this redesign

- The `report` class, XeLaTeX, `apacite` with `natbibapa` (APA 6th, as
  FOM 2019 requires), Times New Roman, the FOM margins, 1.5 spacing,
  and the chapter/front-matter order are all correct and must be preserved
  exactly. This redesign changes where decisions live, not the decisions.
- Chapter files are mostly clean prose plus tables. They do not need
  rewriting; they need mechanical, auditable substitutions only.
- `convert_chapters.py` generated the chapter files from Markdown, but
  the chapters have since been hand-edited (the fix rounds). Re-running
  the converter now would overwrite hand edits. Either freeze the
  converter (chapters are now the source of truth) or update it to emit
  the new semantic commands. Never re-run it silently.

## 2. Target architecture

The rule the new structure enforces: **a chapter, front-matter, or
appendix file contains words, numbers, equations, and references, plus
semantic commands. It contains no package loading, no margin, font, or
spacing value, no heading format, and no repeated table/figure layout.**
Changing the look of the thesis means editing one style file and the
metadata file. Changing the content means editing a chapter file and
never touching the style.

### 2.1 File tree (after migration)

```
src/thesis/
  main.tex                    # ~55 lines: class + style package + assembly ONLY
  tufom-thesis.sty            # the ONLY style file; sectioned, commented
  preamble/
    metadata.tex              # single source of truth for title/author/etc.
    macros.tex                # notation + semantic commands (loaded by .sty)
    floats.tex                # table + figure environments (loaded by .sty)
  chapters/                   # unchanged content, mechanical swaps only
    chapter_01_introduction.tex
    chapter_02_literature_review.tex
    chapter_03_research_methodology.tex
    chapter_04_results_and_discussion.tex
    chapter_05_summary_and_conclusion.tex
  front/                      # words + signature labels; layout via .sty commands
    titlepage.tex  authorship.tex  research_committee.tex
    approval_sheet.tex  acknowledgements.tex
    abbreviations.tex  abstract.tex
  appendices/                 # appendix_a/b/c.tex
  tables/                     # PHASE 5 ONLY, optional: long tables moved out
  figures/                    # PDFs/PNGs, unchanged
  references.bib              # unchanged
  latexmkrc                   # XeLaTeX + BibTeX, output to build/
  .gitignore                  # build artifacts excluded (or repo-root entries)
  build/                      # generated only, never committed
```

### 2.2 Why a `.sty`, not a `.cls`, and why not `subfiles`

- A custom class (`.cls`) would replace `\documentclass{report}` and
  force re-verification of everything the class touches. A package
  (`.sty`) gives the same separation with a smaller blast radius: the
  class, engine, and citation system stay exactly as they are.
- The `subfiles` package lets each chapter compile alone, but chapters
  here are fragments, not standalone documents, and adding a document
  class header to every chapter adds boilerplate and path fragility for
  no benefit. Keep `\input` for chapters and state the rule explicitly:
  chapters are never compiled alone; only `main.tex` is compiled.
- The `.sty` lives at the thesis root, not in a subdirectory, so LaTeX
  finds it without `TEXINPUTS` tricks. The `preamble/` subfiles it loads
  are an internal organisation of that one package, not separate packages
  with their own load order. Load order is the reason not to split the
  preamble into five independent `\usepackage` calls: `hyperref` must
  come late, `apacite` settings must come after `apacite`, and
  `fontspec`/`unicode-math` order matters. One package, one order,
  sectioned with comments, is the safe form of "dedicated directory".

### 2.3 What goes in `tufom-thesis.sty` (in this order)

1. Identification: `\NeedsTeXFormat{LaTeX2e}`,
   `\ProvidesPackage{tufom-thesis}[2026-10-29 TU FOM MBS dissertation style]`.
   A date/version line, so a future reader can tell which style produced
   which PDF.
2. Packages, in the current order, grouped and commented: fonts and
   geometry; spacing and lists; headings and TOC; floats and tables;
   maths and diagrams; captions; citations; hyperref last.
   `longtable` is dropped in Phase 1 only after the diff gate proves
   nothing used it. Nothing else is added in Phase 1.
3. FOM format values, each with its source comment: margins
   (2.54/2.54/2.54/3.18 cm), Times New Roman 12 pt, 1.5 spacing, flush-left
   paragraphs with 10 pt paragraph gap, single-spaced lists, tables, TOC,
   LOT, LOF, and bibliography (with 36 pt hanging indent and 6 pt
   bibliography separation, as now).
4. Heading formats for chapter, section, subsection, subsubsection,
   exactly as now, plus the appendix heading format, defined once here
   instead of redefined mid-document. The appendix format is selected by
   the `\appendix` switch, not by a second `\titleformat` in `main.tex`.
5. Page styles, defined once: `frontmatter` (Roman, bottom centre),
   `mainbody` (Arabic, top right), and the chapter-start `plain` style
   handled by a single switch instead of two definitions. `main.tex`
   only selects which style is active, it never defines one.
6. TOC/LOT/LOF formats, as now.
7. `\input{preamble/macros}` and `\input{preamble/floats}` at the end of
   the package, after the packages they depend on.

### 2.4 `preamble/metadata.tex` — one source of truth

Commands (values unchanged in migration; the file only centralises them):

```
\thesistitle{...}  \thesisauthor{...}  \thesisroll{...}
\thesisregistration{...}  \thesiscampus{...}  \thesisdate{...}
\thesisdegree{...}  \thesisfaculty{...}
```

Front pages read these commands instead of retyping the values. The
title page, authorship page, and any prose that names the candidate or
campus then cannot drift apart. Correcting the submitting name, if it
ever needs correcting, becomes a one-line metadata change, reviewed and
approved like any other thesis edit. This file holds no formatting.

### 2.5 `preamble/macros.tex` — notation and semantic commands

Principle: name a command for what a symbol means, not how it looks.
Changing the look then means editing one definition, and a typo in a
chapter becomes a compile error instead of a silent wrong symbol.

| New command | Replaces (current inline form) | Meaning |
|---|---|---|
| `\MPSRD` | `$\mathit{MPS}^{RD}$` (38 uses) | Market price at reporting deadline |
| `\Post` | `$\mathit{Post}_t$` (25 uses) | Consolidation period indicator |
| `\bankFE` | `$\mu_i$` | Bank fixed effect |
| `\yearFE` | `$\lambda_t$` | Fiscal-year fixed effect |
| `\betaE`, `\betaB` | `$\beta_E$`, `$\beta_B$` | Pre-consolidation slopes |
| `\deltaE`, `\deltaB` | `$\delta_E$`, `$\delta_B$` | Regime-shift coefficients |
| `\EPS`, `\BVPS`, `\ROA`, `\DPS` | `EPS`, `BVPS`, `ROA`, `DPS` in maths contexts where they are currently typed as bare text inside `$...$` | Variable names, kept upright and consistent |
| `\NPR` | `NPR` in text where a unit is meant | Nepalese Rupees unit |
| `\FY{2076/77}` | `FY 2076/77` typed text | Fiscal-year label, one format everywhere |

Rules for this file: no formatting-only shortcuts (no `\bold{...}` that
just wraps `\textbf`); every macro gets a one-line comment stating its
meaning; no macro is defined in a chapter. Macros that would change
rendering (for example, changing `MPS` from italic to upright) are NOT
introduced in migration: the first version of each macro must expand to
exactly the current inline form, so the PDF does not change. A notation
restyle, if ever wanted, is a separate, approved decision after migration.

### 2.6 `preamble/floats.tex` — tables and figures

One table environment and one figure command replace all repeated layout:

- `thesistable` environment: wraps `table` + `threeparttable` +
  booktabs, applies `\small` and the standard caption setup, and provides
  a `\tablenote{...}` for the note that is currently a hand-built
  `\vspace{4pt}` + `\footnotesize` + `minipage`. Table content (header
  row, data rows) stays in the chapter; only the scaffolding moves.
  Long tables, if any are ever needed, use `threeparttablex`, which is
  the longtable companion — do not force a long table into
  `threeparttable`, it will break.
- `\thesisfigure[width]{file}{caption}{label}`: one command, default
  width 0.88 `\textwidth` (the current converter default and the most
  common width in the thesis). The one genuinely different width, the
  0.72 heatmap in Chapter 4, keeps its width as an explicit optional
  argument with a comment saying why it is narrower. Widths are no
  longer scattered across ten call sites.
- Caption style (bold, justified, single-line check off) is set once in
  the `.sty`, never repeated per table or figure again. The 14 repeated
  local `\captionsetup` calls are deleted in this phase.
- Tables stay in their chapters in Phases 1–4. Moving large tables to
  `tables/` is an optional Phase 5, only if a table becomes hard to read
  inside a chapter; it changes nothing about layout and must not be
  bundled with the style migration.

### 2.7 `front/` pages — words stay, layout moves

Front pages keep their text, names, signature labels, and order. What
moves to the `.sty` is the repeated layout: a shared `\frontheading`
for the centred bold page title, a shared `\frontgap` set (named gaps,
not raw centimetre values in each file), and a `\signatureline{label}`
command that produces one ruled line at the standard width. A reader
comparing two front pages then sees the same commands, and a spacing
change is one edit in the `.sty`, not seven edits across seven files.
Front pages must never load a package or set a margin.

### 2.8 `main.tex` after migration (target, ~55 lines)

```
\documentclass[12pt,a4paper,oneside]{report}
\usepackage{tufom-thesis}
\input{preamble/metadata}
\begin{document}
  \input{front/titlepage}
  \pagestyle{frontmatter} \pagenumbering{roman} \setcounter{page}{2}
  \input{front/authorship} ... (front matter, in FOM order)
  \tableofcontents \listoftables \listoffigures
  \input{front/abbreviations} \input{front/abstract}
  \clearpage \pagestyle{mainbody} \pagenumbering{arabic} \setcounter{page}{1}
  \input{chapters/chapter_01_introduction} ... (I–V)
  \bibliography{references}   (with the existing singlespacing + APA setup,
                               now expressed as one style command)
  \appendix
  \input{appendices/appendix_a} ...
\end{document}
```

No `\titleformat`, no `\captionsetup`, no `\setlength`, no page-style
definition, and no package loading appears here. If a future style change
requires editing `main.tex`, the architecture has failed; that is the test.

### 2.9 Build: `latexmkrc` + output directory

```
$pdf_mode = 1;
$pdflatex = 'xelatex -interaction=nonstopmode -synctex=0 %O %S';
$bibtex_use = 2;
$out_dir = 'build';
$aux_dir = 'build';
```

One command, `latexmk`, from `src/thesis/`, performs the XeLaTeX →
BibTeX → XeLaTeX → XeLaTeX sequence and puts every artifact in
`build/`, which is git-ignored. The manual sequence (xelatex, bibtex,
xelatex, xelatex) is documented in the thesis README section as the
fallback. No PDF is committed; the PDF is a build product, and the
sources plus this config are the reproducible input. Note for this
machine: XeLaTeX and latexmk are not installed on this VM, so the
compile gates must run on a machine with a TeX Live installation (or
the user's own machine / Overleaf), not here. Claiming a local compile
here would be false.

## 3. Migration plan (phases, each with its own commit and gate)

Phase 0 — Baseline, before any restructure.
Copy the tree to a scratch location, compile with the documented
sequence, and save: the PDF, the log, the page count, and the extracted
text. If the baseline does not compile cleanly, stop: fix compilation
first, as its own commit, and never mix a compile fix into a restructure.

Phase 1 — Move the preamble verbatim into `tufom-thesis.sty`.
No value changes, no package changes except proving `longtable`
unused. `main.tex` becomes class + package + assembly. Gate: new PDF
must match the baseline page-for-page in extracted text and page count,
and the log must show no new warnings.

Phase 2 — Metadata.
Add `preamble/metadata.tex`, make front pages read it, change no value.
Gate: title page and front matter render identically; metadata values
checked against the baseline PDF text, character for character.

Phase 3 — Macros.
Replace inline notation with the Section 2.5 commands, chapter by
chapter, with a checklist counting replacements (38 + 25 + the rest).
Gate: extracted text identical to baseline; a grep for the old inline
forms returns zero in chapters.

Phase 4 — Floats.
Replace repeated table scaffolding with `thesistable` + `\tablenote`
and figure calls with `\thesisfigure`. Gate: LOT and LOF identical to
baseline, every table and figure still present, notes still attached to
their tables, no float moved to a different page by a layout change
(a page shift here means the phase failed, even if the text matches).

Phase 5 — Front-matter layout + optional table move.
Replace per-page spacing and signature rules with shared commands.
Check the previously unverified FOM item: each front-matter section
fits on a single page. Only then, if wanted, move long tables to
`tables/`. Gate: front matter page count identical to baseline, each
front section on one page, or the deviation is reported as a finding,
not silently accepted.

Rollback at any phase: revert that phase's commit only. Because each
phase is output-identical by construction, reverting one phase never
requires re-editing content.

## 4. Explicit non-goals (do not bundle these in)

- No switch to biblatex/Biber, LuaLaTeX, `tabularray`, or any new
  citation or table system. Each would change output and needs its own
  justification and approval; the current stack is correct for FOM 2019.
- No font, margin, spacing, heading, or caption restyle. The thesis
  look stays exactly as approved; only the location of its definition
  changes.
- No wording, number, citation key, figure, or table-content change.
  If a migration phase appears to "fix" a typo or a number, stop: that
  is a content edit and needs its own approval.
- No re-running `convert_chapters.py` during migration. If the
  converter is updated to emit semantic commands, that is a separate
  commit, tested on a copy, and it must never overwrite hand edits.
- No new configurability for its own sake: no package options, no
  "draft/final" modes, no institution switch. This thesis has one
  institution, one format, and one style file. Options are added only
  when a second real use exists.

## 5. Verification checklist (applies to every phase)

- [ ] Compiles with zero errors on a TeX Live machine (log inspected,
      not just "a PDF appeared").
- [ ] Page count identical to baseline; extracted text identical
      (diff of `pdftotext` output, ignoring only timestamps).
- [ ] TOC, LOT, LOF identical to baseline.
- [ ] All 62 labels resolve (no undefined references in the log).
- [ ] Bibliography: same entry count, same APA 6th rendering.
- [ ] Front matter: same order, same page numbering (Roman bottom
      centre, then Arabic top right from Chapter I, page 1).
- [ ] No chapter, front, or appendix file loads a package, sets a
      margin/font/spacing, or defines a command (grep gate).
- [ ] `git status` shows only the intended files; `build/` is ignored.

## 6. Decision needed before any work starts

Approve or amend: (a) the `.sty` + `preamble/` shape in Section 2,
(b) the macro list in Section 2.5, (c) the phase order and gates in
Section 3, and (d) whether Phase 5's optional table move is wanted at
all. Implementation starts only after that approval, and only in the
phases above.
