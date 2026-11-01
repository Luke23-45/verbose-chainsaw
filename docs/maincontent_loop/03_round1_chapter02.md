# Main-content loop — Round 1, Chapter II review (reviewer report + disposition)

Reviewer: per-chapter format review, no files edited. Parent verified
M1/M2/M3/M4 against source, log, and compiled PDF before disposition.

## MUST-FIX

### M1 — Table 2.1 loses its last 11 rows in the compiled thesis (CRITICAL)
- Source: lines 300–355, a single non-breaking `table` float
  (`[!htbp]`) with a `tabular`, no longtable, no repeated header.
- Compile log: `Float too large for page by 756.75287pt on input
  line 355` — more than a full text height (697.9 pt).
- Compiled PDF p. 50: table starts, is cut off at the bottom edge
  mid-row at the Chhetri (2023) row, no \bottomrule; the next page
  resumes with Research Gap prose. The 11 rows after Chhetri
  (joshi2023, giri2024, lamsal2024, gurung2024, pant2024,
  chaudhari2025, dahal2025, gurungdahal2025, timalsina2026,
  bhandari2026, adhikari2023) are not in the table as printed.
  Correction to the reviewer's search note: the author names do
  appear elsewhere in the PDF (prose and references), so name
  presence alone does not prove the rows survive — the float
  warning, the cutoff, and the missing \bottomrule do.
- Fix (format only, no content change): convert Table 2.1 to a
  `longtable` with a repeated header (firsthead + head), keeping
  every row, the caption, the label, and the \addlinespace pattern.
  This also corrects the earlier phase's source-only Table 2.1
  checks, which never compiled the table and therefore never saw
  the loss.

### M2 — Table 2.1 is overwide by ~25 pt
- Source line 306: five p-columns sum to 0.92 \textwidth; plus
  10 × 6 pt tabcolsep = 458.5 pt against a 433.1 pt text width.
- Log agrees: `Overfull \hbox (25.21185pt too wide) lines 306--355`.
- Fix with M1: narrow the columns to sum 0.85 \textwidth
  (Study 0.17, Sample 0.16, Methodology 0.15, Variables 0.17,
  Findings 0.20 → 368.2 + 60 = 428.2 pt, inside 433.1 pt).

### M3 — Footnote citation duplication
- Line 271 footnote: `Gurung and Dahal \citep{gurungdahal2025}` and
  `Dahal, Gurung, and Ghimire \citep{dahal2025}` render the names
  twice. Fix: change both \citep to \citet in that footnote only.
  Verified: no other Name + \citep duplication in the chapter.

### M4 — BAFIA list numbering differs from the chapter's other lists
- Line 186 `\begin{enumerate}` renders plain 1./2. while the four
  other enumerates use `[label=\textbf{\arabic*.}]`. Fix: add the
  same label option to line 186.

## MINOR

- N1 — Table 2.1 has no note and is not self-contained. DPR and DY
  are defined in prose (line 235: dividend payout ratio, dividend
  yield), but EY and MTB appear only in the dahal2025 row (line 344)
  and are defined nowhere in the chapter. Fix direction: add a
  short table note defining DPR, DY, and the other table
  abbreviations from prose where verifiable; EY/MTB must NOT be
  defined by guess — if they cannot be verified from the Dahal
  study or the thesis prose, the note must say so and the fix
  stops at flagging it, not inventing expansions.
- N2 — P/E identity uses `=` (lines 158, 366) and `\equiv`
  (line 289). Standardize to `=` in the notation pass.
- N3 — Justified narrow p-columns stretch word spacing (rendered
  p. 50). Cosmetic; decide after the longtable render whether
  ragged-right columns are warranted. Deferred to visual check.
- Notation inventory (for the later pass, not changed now):
  $MPS^{RD}$ here is plain superscript, not $\mathit{MPS}^{RD}$
  as in other chapters; $P_t$, $BV_t$, $NI_t$, $\omega$, $\gamma$,
  $\alpha_1$, $\alpha_2$, $k$, $\phi$ forms listed by the reviewer.

## Passes (reviewer, accepted)

Headings (5 sections, subsections 2.2.1–2.2.6, 2.3.1–2.3.3,
2.4.1–2.4.5, 2.5.1–2.5.5, no gaps); table caption above (correct
for tables), label after caption, single table so sequential;
local \captionsetup identical to global (floats pass, not a
defect); lists balanced (other than M4); equations balanced
(16 equation + 1 align); all 6 \ref targets and all 56 citation
keys resolve; zero \vspace/\hspace/\fontsize/\setlength in the
file; braces 381/381, all environments balanced.

## Correction to the phase inventory

Chapter II contains exactly ONE tabular inside ONE table float,
not a longtable and not two tabular blocks. The design phase's
"2 Ch2 tabular blocks" count was wrong.
