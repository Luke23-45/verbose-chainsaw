# Plan 10 — Exemplar/online alignment: cover formatting, roman lists, 12 pt references

Scope: patches 2–5 from the gap analysis. **Patch 1 (page trim) is DROPPED — page limit
skipped per your 2026-10-13 instruction.** Body (sections i–vii) is 10 arabic pages, already
inside FOM's "approximate 8–12 pages" (title + TOC are prefatory and conventionally uncounted).

Sources (NOT professor orders — evidence only, applied only where professor is silent):
- `docs/reference/EXTRACTED_SPEC.md` §§2–3, 6, 11 (accepted FOM thesis: TNR 16 pt bold title,
  bold `A Thesis`/`Submitted to`/`By`/place-date, plain fulfillment line, lowerRoman `i.` RQ +
  objectives lists, plain `H1:` lines, 12 pt hanging-indent bibliography).
- Online cross-check 2026-10-13: FOM 2019 still current (portal.tu.edu.np, fomecd.edu.np —
  matches our local copy); MBS proposal format doc ("main heading 16 pt, sub heading 14 pt,
  body 12 pt"); SOMTU rules ("write objectives in roman number i, ii, iii"; "never use bullets,
  use roman numbers"; "Font size TNR 12"); FOM 2019 line 782 ("uniform typeface and font size…
  12-point").

## Conflict resolutions (professor beats exemplar — these items are NOT in this plan)

1. **Degree block stays exactly as-is** (`\textit{…Degree of…M.B.S.}`). Professor's frozen
   order (detail/01_cover.md #2) says "must NOT be bold — set it in italic". The exemplar's
   bold-upright degree line is overruled. The "In partial fulfillment…" line shares that block
   (professor's bracket points at it) — also untouched.
2. **Wording untouched everywhere.** "A Dissertation Proposal" keeps professor-approved text
   (circled + ticked); only its weight changes plain → bold (formatting, not wording).
3. **No content/meaning changes.** RQ, objective, and H-wording are byte-identical; only list
   labels (arabic → roman) and H-line structure (bullets → plain paragraphs) change.
4. **No new packages.** Roman labels via group-scoped `\renewcommand` (no `enumitem`), so
   `07_methodology` enumerates and global list spacing are unaffected.

## Patch 10A — references back to 12 pt

Target: `src/proposal/main.tex` (bibliography group only; `\singlespacing` stays — guideline
allows single spacing for references).

```latex
% OLD (lines 112-116)
\begingroup
\singlespacing
\renewcommand{\bibliographytypesize}{\small}
\bibliography{references}
\endgroup
```
```latex
% NEW
\begingroup
\singlespacing
\bibliography{references}
\endgroup
```

One deleted line. Effect: apacite entries render at document 12 pt (uniform per FOM line 782)
instead of ~11 pt. Expected side effect: references section grows ~0.5–1 page. No .bib change,
no citation change, no TOC change.

## Patch 10B — cover formatting (5 sub-edits, degree block untouched)

Target: `src/proposal/front/titlepage.tex`. Block order, all wording, all `\vspace` rhythm,
roll/regd/name/campus lines: UNCHANGED.

**C1 — title 16 pt** (exemplar 16.0 pt; professor silent). OLD:
```latex
{\large\bfseries ACCOUNTING FUNDAMENTALS AND SHARE PRICES:\\[4pt] EVIDENCE FROM SELECTED NEPALESE COMMERCIAL BANKS\par}
```
NEW:
```latex
{\fontsize{16}{19}\selectfont\bfseries ACCOUNTING FUNDAMENTALS AND SHARE PRICES:\\[4pt] EVIDENCE FROM SELECTED NEPALESE COMMERCIAL BANKS\par}
```

**C2 — "A Dissertation Proposal" bold** (exemplar bolds its thesis line; wording kept). OLD:
```latex
{A Dissertation Proposal\par}
```
NEW:
```latex
{\bfseries A Dissertation Proposal\par}
```

**C3 — "Submitted to" bold, rest of block plain** (exemplar exact). OLD:
```latex
{Submitted to\\[6pt]
Office of the Dean\\[6pt]
Faculty of Management\\[6pt]
Tribhuvan University\par}
```
NEW:
```latex
{{\bfseries Submitted to}\\[6pt]
Office of the Dean\\[6pt]
Faculty of Management\\[6pt]
Tribhuvan University\par}
```

**C4 — "By" bold, rest plain** (exemplar exact). OLD:
```latex
{By\\[6pt]
Asmita Subedi\\[6pt]
Triveni International College\\[6pt]
Exam Roll No: 67514/24\\[6pt]
T.U. Regd. No: 7-2-48-1060-2018\par}
```
NEW:
```latex
{{\bfseries By}\\[6pt]
Asmita Subedi\\[6pt]
Triveni International College\\[6pt]
Exam Roll No: 67514/24\\[6pt]
T.U. Regd. No: 7-2-48-1060-2018\par}
```

**C5 — place/date bold** (exemplar exact). OLD:
```latex
{Pokhara, Nepal\\[6pt]
October, 2026\par}
```
NEW:
```latex
{\bfseries Pokhara, Nepal\\[6pt]
October, 2026\par}
```

## Patch 10C — RQ and objective lists to roman i., ii., iii.

Targets: `sections/02_problem_statement/02_problem_statement.tex`,
`sections/03_objectives/03_objectives.tex`. Items byte-identical; only the counter format
changes (matches exemplar `numbering.xml` lowerRoman `%1.` → `i.` and SOMTU rule).
No `\label` on any item and nothing `\ref`s them (verified: only `fig:framework`/`eq:main`
refs exist) — safe.

OLD (02, lines 24–29; same wrapper pattern for 03, lines 8–13):
```latex
The study addresses the following questions:
\begin{enumerate}
  \item What levels and fiscal-year patterns do EPS, DPS, BVPS, ROA, and post-disclosure market price per share show in the sampled bank series?
  \item How is each of EPS, DPS, BVPS, and ROA associated with post-disclosure market price per share?
  \item How are EPS, DPS, BVPS, and ROA jointly associated with post-disclosure market price per share?
\end{enumerate}
```
NEW (wrap in group; items unchanged):
```latex
The study addresses the following questions:
{\renewcommand{\theenumi}{\roman{enumi}}
\begin{enumerate}
  \item What levels and fiscal-year patterns do EPS, DPS, BVPS, ROA, and post-disclosure market price per share show in the sampled bank series?
  \item How is each of EPS, DPS, BVPS, and ROA associated with post-disclosure market price per share?
  \item How are EPS, DPS, BVPS, and ROA jointly associated with post-disclosure market price per share?
\end{enumerate}}
```
Apply the identical wrapper to the 03 objectives enumerate (three items unchanged).
`07_methodology` enumerates stay arabic (procedure steps — out of scope).

## Patch 10D — hypotheses: drop bullets, keep wording and `$H_n$` form

Target: `sections/04_hypothesis/04_hypothesis.tex`. Exemplar prints `H1:`–`H5:` as plain
12 pt lines (no bullets); SOMTU bans bullets for sub-points. `$H_1$` math form is kept
(italic math is the quantitative convention; only the `itemize` structure goes).
Lead-in paragraph (lines 3–7) unchanged.

OLD (lines 8–17):
```latex
\begin{itemize}
  \item $H_1$: There is a significant positive relationship between earnings per
    share (EPS) and post-disclosure market price per share ($\mathit{MPS}^{post}$).
  \item $H_2$: There is a significant positive relationship between dividend per
    share (DPS) and post-disclosure market price per share ($\mathit{MPS}^{post}$).
  \item $H_3$: There is a significant positive relationship between book value
    per share (BVPS) and post-disclosure market price per share ($\mathit{MPS}^{post}$).
  \item $H_4$: There is a significant positive relationship between return on
    assets (ROA) and post-disclosure market price per share ($\mathit{MPS}^{post}$).
\end{itemize}
```
NEW:
```latex
\noindent $H_1$: There is a significant positive relationship between earnings per
share (EPS) and post-disclosure market price per share ($\mathit{MPS}^{post}$).
\medskip

\noindent $H_2$: There is a significant positive relationship between dividend per
share (DPS) and post-disclosure market price per share ($\mathit{MPS}^{post}$).
\medskip

\noindent $H_3$: There is a significant positive relationship between book value
per share (BVPS) and post-disclosure market price per share ($\mathit{MPS}^{post}$).
\medskip

\noindent $H_4$: There is a significant positive relationship between return on
assets (ROA) and post-disclosure market price per share ($\mathit{MPS}^{post}$).
```

## Verify after apply (only after your approval; build only on your order)

- Build: `.\build.ps1 -Target proposal` → 0 errors; `main.log` 0 `^!`, 0 `undefined`.
- Cover: title visibly larger (16 pt); `A Dissertation Proposal`, `Submitted to`, `By`,
  `Pokhara, Nepal / October, 2026` bold; degree block STILL italic non-bold.
- Body: RQ + objectives labelled i., ii., iii.; H1–H4 as plain unbulleted lines.
- References: 12 pt (same size as body); TOC (`i–vii`, `1.1.1–1.1.5`, `References`) unchanged.
- `git diff --stat`: exactly 4 files (`main.tex`, `titlepage.tex`, `02_…`, `03_…`,
  `04_…` = 5 files). No `.bib`, no methodology, no lit-review touched.
