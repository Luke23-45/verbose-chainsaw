# Plan 10 — Exemplar alignment: cover, lists, caption (REBASED to HEAD 693a115)

Scope: gap-analysis patches 2–5, re-verified against current sources after three polish
commits landed mid-session (a2e71b9, 4c83c1c, 693a115: new POST-DISCLOSURE title, supervisor
cover block, xelatex + real Times New Roman, rewritten 04/07). **Patch 1 (page trim) is
DROPPED — page limit skipped per your instruction.**

Legend: **[REQUIRED]** = mandated by FOM 2019 text. **[OPTIONAL]** = exemplar-backed style
alignment used only where FOM and professor are silent (10C–10H, C1–C5); decline any single
optional item without blocking the rest.

Sources (NOT professor orders — evidence only, applied only where professor is silent):
- `docs/reference/EXTRACTED_SPEC.md` §§2–3, 6, 11 (accepted FOM thesis: TNR 16 pt bold title,
  bold `A Thesis`/`Submitted to`/`By`/place-date, plain fulfillment line, lowerRoman `i.` RQ +
  objectives lists, plain `H1:` lines, 12 pt hanging-indent bibliography).
- Online cross-check 2026-10-13: FOM 2019 still current (portal.tu.edu.np, fomecd.edu.np —
  matches our local copy); MBS proposal format doc ("main heading 16 pt, sub heading 14 pt,
  body 12 pt"); FOM 2019 line 782 ("uniform typeface and font size… 12-point"); FOM Appendix C
  (table/figure rules). SOMTU teaching notes are NON-authoritative background only (different
  school, user-uploaded copy) — no patch below relies on them; 10C rests on the FOM exemplar's
  `numbering.xml` alone.

## Conflict resolutions (professor beats exemplar — these items are NOT in this plan)

1. **Degree block stays exactly as-is** (`\textit{…Degree of…M.B.S.}`). Professor's frozen
   order (detail/01_cover.md #2) says "must NOT be bold — set it in italic". The exemplar's
   bold-upright degree line is overruled. The "In partial fulfillment…" line shares that block
   (professor's bracket points at it) — also untouched.
2. **Wording untouched everywhere.** "A Dissertation Proposal" keeps professor-approved text
   (circled + ticked); only its weight changes plain → bold (formatting, not wording).
3. **No content/meaning changes.** RQ, objective, and H-wording are byte-identical; only list
   labels (arabic → roman) and H-line structure (bullets → plain paragraphs) change.
4. **One new package: `caption`** (10F only; loaded before `hyperref`; affects exactly the one
   existing `\caption`). Roman labels need no package (group-scoped `\renewcommand`).
5. **Only 10F's size fix is guideline-mandated** (uniform 12 pt rule). All size / roman / bold
   choices are OPTIONAL exemplar alignments, relabeled as such after external review.

## Patch 10A — DROPPED (already in source)

Verified: `main.tex` bibliography group has `\singlespacing` + `\bibliography{references}`
with NO `\bibliographytypesize` line (removed by the 2026-10-13 polish commits). References
already render at document 12 pt. No action.

## Patch 10B — cover formatting (5 sub-edits, degree block untouched)

Target: `src/proposal/front/titlepage.tex`. Block order, all wording, all `\vspace` rhythm,
roll/regd/name/campus lines: UNCHANGED.

**C1 — title 16 pt** (exemplar 16.0 pt; professor silent). OLD:
```latex
{\large\bfseries ACCOUNTING FUNDAMENTALS AND POST-DISCLOSURE SHARE PRICES:\\[4pt] EVIDENCE FROM SELECTED NEPALESE COMMERCIAL BANKS\par}
```
NEW:
```latex
{\fontsize{16}{19}\selectfont\bfseries ACCOUNTING FUNDAMENTALS AND POST-DISCLOSURE SHARE PRICES:\\[4pt] EVIDENCE FROM SELECTED NEPALESE COMMERCIAL BANKS\par}
```
(HEAD title = 12 words — at the "within 12 words" boundary, still compliant.)

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

**C4 — "Submitted by" bold, rest plain** (exemplar bolds its agent line; HEAD wording
preserved exactly). OLD:
```latex
{Submitted by\\[6pt]
Asmita Subedi\\[6pt]
Triveni International College\\[6pt]
Exam Roll No: 67514/24\\[6pt]
T.U. Regd. No: 7-2-48-1060-2018\par}
```
NEW:
```latex
{{\bfseries Submitted by}\\[6pt]
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

## Patch 10C — RQ and objective lists to roman i., ii., iii. [OPTIONAL]

Targets: `sections/02_problem_statement/02_problem_statement.tex`,
`sections/03_objectives/03_objectives.tex`. Items byte-identical; only the counter format
changes (matches exemplar `numbering.xml` lowerRoman `%1.` → `i.`). FOM is silent on list
markers and the professor reviewed question content, not numbering — style alignment only.
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

## Patch 10D — hypotheses: drop bullets, keep CURRENT wording verbatim [OPTIONAL]

Target: `sections/04_hypothesis/04_hypothesis.tex`. Rationale: exemplar prints plain `Hn:`
lines; bullets avoided for sub-points. The HEAD wording (null-hypothesis + β notation,
committed 2026-10-13) is preserved EXACTLY — only the `itemize` structure goes. The first
draft of this patch quoted a superseded wording and is withdrawn; applying it would revert
approved text. Lead-in paragraph unchanged.

OLD (current file, `itemize` block):
```latex
\begin{itemize}
  \item $H_1$: The conditional association between earnings per share (EPS) and
    $\mathit{MPS}^{post}$ is expected to be positive ($\beta_1>0$).
  \item $H_2$: The conditional association between dividend per share (DPS) and
    $\mathit{MPS}^{post}$ is expected to be positive ($\beta_2>0$).
  \item $H_3$: The conditional association between book value per share (BVPS)
    and $\mathit{MPS}^{post}$ is expected to be positive ($\beta_3>0$).
  \item $H_4$: The conditional association between return on assets (ROA) and
    $\mathit{MPS}^{post}$ is expected to be positive ($\beta_4>0$).
\end{itemize}
```
NEW (same four sentences, plain paragraphs):
```latex
\noindent $H_1$: The conditional association between earnings per share (EPS) and
$\mathit{MPS}^{post}$ is expected to be positive ($\beta_1>0$).
\medskip

\noindent $H_2$: The conditional association between dividend per share (DPS) and
$\mathit{MPS}^{post}$ is expected to be positive ($\beta_2>0$).
\medskip

\noindent $H_3$: The conditional association between book value per share (BVPS)
and $\mathit{MPS}^{post}$ is expected to be positive ($\beta_3>0$).
\medskip

\noindent $H_4$: The conditional association between return on assets (ROA) and
$\mathit{MPS}^{post}$ is expected to be positive ($\beta_4>0$).
```

## Patch 10E — cover body text 12 pt → 14 pt [OPTIONAL]

Target: `src/proposal/front/titlepage.tex`. Every non-title run in the exemplar cover is
14.0 pt. The supervisor block (lines 8–11) has no exemplar counterpart and stays 12 pt — so
the switch goes AFTER it; the title sets its own 16 pt and is unaffected; `\vspace` rhythm
and `\vfill` unaffected.

OLD (titlepage.tex lines 8–11):
```latex
{Supervisor: Shankar Thapa\\[4pt]
Contact: 9847339708\par}

\vspace{0.8cm}
```
NEW:
```latex
{Supervisor: Shankar Thapa\\[4pt]
Contact: 9847339708\par}

\vspace{0.8cm}
\fontsize{14}{17}\selectfont
```

## Patch 10F — figure caption to 12 pt bold [REQUIRED for size; layout unchanged]

Why: base-article `\@makecaption` renders our only caption at `\small` (~11 pt), upright —
violates FOM "uniform 12-point" and mismatches the exemplar (12 pt, fully bold, justified).
Guideline Appendix C: figure number + descriptive title BELOW the figure ✓ (already true);
source/note on its own line below (exemplar pattern; Appendix C requires notes below tables —
same convention applied to the figure).

Target 1 — `src/proposal/main.tex` (insert BEFORE `\usepackage{hyperref}`; caption must load
before hyperref):
```latex
% OLD
\bibliographystyle{apacite}
\usepackage{hyperref}
```
```latex
% NEW
\bibliographystyle{apacite}
\usepackage{caption}
\captionsetup{font={normalsize,bf},justification=justified,singlelinecheck=false}
\usepackage{hyperref}
```
(`font={normalsize,bf}` = whole caption 12 pt bold like the exemplar; `singlelinecheck=false`
forces justified instead of LaTeX's auto-center for one-line captions. Only one `\caption`
exists in the document, so nothing else is affected.)

Target 2 — NONE (layout kept). The caption text and in-caption source stay exactly as
approved — splitting the layout is declined after review (it would newly center the source
line under active `\centering`, an unverified appearance change, for exemplar-cosmetic
reasons only). The Target-1 package fix alone renders the approved caption at 12 pt bold
justified. Year 2016 kept (verified `pradhan2016` SSRN key).

## Patch 10G — lit-review subsection heads 12 pt → 14 pt [OPTIONAL]

Target: `src/proposal/main.tex`. The three `\subsection*` heads in section vi
(Theoretical / Empirical / Research gap) are the direct counterparts of the exemplar's
2.1/2.2/2.3 heads (14 pt bold). Verified: `\subsection` is used ONLY in `06_*` (3×), so
this touches nothing else. Sentence case kept (matches the guideline's own casing style).
`\subsubsection` is unused anywhere — its format line is left alone.

```latex
% OLD (line 47)
\titleformat{\subsection}{\normalfont\bfseries}{}{0pt}{}
```
```latex
% NEW
\titleformat{\subsection}{\normalfont\bfseries\large}{}{0pt}{}
```

## Patch 10H — framework labels bold-upright, boxes unfilled [OPTIONAL]

Target: `sections/07_methodology/07_methodology.tex`. Measured exemplar: labels 12 pt
BOLD upright (`Independent Variable` / `Dependent Variable`), boxes unfilled. Ours: italic
labels + `gray!10` fill. Wording (`Independent variables` / `Dependent variable`) is KEPT —
it follows the approved Fig. 1 rebuild, and plural is factually correct for 4 IVs.

Replacement 1 — OLD (line 100):
```latex
  dep/.style={rectangle, draw, minimum width=4.0cm, minimum height=1.7cm, text centered, font=\normalsize, fill=gray!10},
```
NEW:
```latex
  dep/.style={rectangle, draw, minimum width=4.0cm, minimum height=1.7cm, text centered, font=\normalsize},
```
Replacement 2 — OLD (lines 112–113):
```latex
  \node[above=0.2cm of eps, font=\normalsize\itshape] {Independent variables};
  \node[below=0.25cm of mps, font=\normalsize\itshape] {Dependent variable};
```
NEW:
```latex
  \node[above=0.2cm of eps, font=\normalsize\bfseries] {Independent variables};
  \node[below=0.25cm of mps, font=\normalsize\bfseries] {Dependent variable};
```

## Patch 10I — DROPPED (casing not prescribed)

External review stands: guideline lines 315–319 list "Table of contents" as a required
prefatory section but do not prescribe display capitalization (Appendix B even writes "List
of Contents"). "Table of Contents" stays. No action.

## Verify after apply (only after your approval; build only on your order)

- Pre-apply guard: re-run the structure counts below against HEAD first; abort any patch
  whose OLD block no longer matches (concurrent commits landed mid-session before — that is
  how the first draft of this plan went stale).
- Build: `.\build.ps1 -Target proposal` → 0 errors; `main.log` 0 `^!`, 0 `undefined`.
  (Note: engine is now xelatex + real Times New Roman — build script must support it.)
- Cover: title 16 pt; `A Dissertation Proposal`, `Submitted to`, `Submitted by`,
  `Pokhara, Nepal / October, 2026` bold; supervisor block untouched (12 pt plain); degree
  block STILL italic non-bold; cover body otherwise 14 pt.
- Body: RQ + objectives labelled i., ii., iii. with identical items; H1–H4 as plain
  unbulleted lines with identical null/β wording.
- TOC (`i–vii`, `1.1.1–1.1.5`, `References`) and references section unchanged by these
  patches (10A already in source).
- `git diff --stat`: exactly 6 files (`main.tex`, `titlepage.tex`, `02_…`, `03_…`,
  `04_…`, `07_…`). No `.bib`, no lit-review body, no 01/05 touched.
- Structure counts (must hold): `tabular` envs = 0, `\caption` = 1, `\label` in 02/03/04 = 0,
  `\subsection` users = only `06_*` (3×).
- Caption: approved in-caption text renders 12 pt bold justified (source stays inside it).
- 06 heads visibly larger (14 pt, only if 10G taken); framework labels bold upright, DV box
  white (only if 10H taken).
