# Plan 01 — Cover page (professor swap + no-bold italic)

Source: `../detail/01_cover.md` (image `74604651...`)
Target: `src/proposal/front/titlepage.tex` (full-file replacement below)

## Finding on recheck

Current `titlepage.tex` ALREADY has the corrected order (Submitted-to block lines 16–19 BEFORE Submitted-by block lines 23–27). The reviewed printout had them reversed — so the swap order the professor demanded is already in place. Do NOT swap back.

Remaining cover fixes:
1. Degree line is bold context + regular text — professor orders non-bold italic.
2. Reviewed printout reads "A Dissertation Proposal" (circled + ticked = approved). Current tex reads "A Thesis Proposal". TU FOM guideline calls the document a "dissertation proposal" (proposal for dissertation writing, pp.7–8). Change to the approved wording.

## New `titlepage.tex` (paste entire file)

```latex
\begin{titlepage}
\thispagestyle{empty}
\begin{center}
% Even vertical rhythm: fixed top margin, equal stretch between blocks,
% fixed bottom margin. Within-block lines share one line gap.
\vspace*{1.5cm}

{\large\bfseries FUNDAMENTAL DETERMINANTS OF SHARE PRICES:\\[4pt] EVIDENCE FROM NEPALESE COMMERCIAL BANKS\par}

\vspace{1.2cm}

{A Dissertation Proposal\par}

\vspace{1.2cm}

{Submitted to\\[6pt]
Office of the Dean\\[6pt]
Faculty of Management\\[6pt]
Tribhuvan University\par}

\vspace{1.2cm}

{By\\[6pt]
Asmita Subedi\\[6pt]
Triveni International College\\[6pt]
Exam Roll No: 67514/24\\[6pt]
T.U. Regd. No: 7-2-48-1060-2018\par}

\vspace{1.2cm}

{\textit{In partial fulfillment of the requirements for the Degree of\\[6pt]
Master of Business Studies (M.B.S.)}\par}

\vfill

{Pokhara, Nepal\\[6pt]
October, 2026\par}

\vspace*{1.5cm}
\end{center}
\end{titlepage}
```

Changes vs current file: line 12 `A Thesis Proposal` → `A Dissertation Proposal`; lines 31–32 wrapped in `\textit{...}` (italic, non-bold). Order of Submitted-to / Submitted-by unchanged (already correct). Title, name, roll/reg, Pokhara October 2026 unchanged.

## Verify after apply

- `pdflatex` title page: "A Dissertation Proposal", Submitted-to above Submitted-by, degree line italic non-bold.
- No other file touched by this plan.
