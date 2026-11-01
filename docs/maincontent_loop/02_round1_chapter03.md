# Main-content loop — Round 1, Chapter III review (reviewer report + disposition)

Reviewer: per-chapter format review, no files edited; fresh compile of
a copy confirmed Table 3.1 (p. 46) and Figure 3.1 (p. 49) render.
Parent verified M-1, m-5, m-7 against source before disposition.

## Reviewer findings

- MUST-FIX M-1: Figure 3.1 caption is ABOVE the TikZ diagram
  (lines 175–177 caption vs 178–201 picture). FOM pp. 20–21:
  figures have numbers and captions UNDER the figures; tables have
  titles above. Fix: move \caption + \label to after
  \end{tikzpicture}, before \end{figure}. In-text reference line 172
  unaffected.
- MINOR m-1: Table 3.1 caption uses plain $MPS^{RD}$ vs body
  $\mathit{MPS}^{RD}$ (7×) — notation pass.
- MINOR m-2: $N = 28$ (5×) vs $n = 28$ (6×) for the same total;
  subsamples $n = 13/15/23$, bank count $N = 5$ — notation pass
  (convention to settle: $N$ for totals, $n$ for subsamples, which
  makes the six $n = 28$ items the ones to change).
- MINOR m-3: 7 labelled equations never cross-referenced — KEPT
  (dead labels, not dangling; same disposition as Chapter I M1).
- MINOR m-4: local \captionsetup (lines 103, 175) duplicates the
  global setting exactly — floats cleanup pass, document-wide, not
  a Chapter III-only edit.
- MINOR m-5: variable block lead-in missing — every variable
  subsubsection opens with a bold `\textbf{...:}` lead-in line
  except "Strict Exclusion of Price-Derived Multiples" (line 253),
  whose paragraph starts plain. Fix: add bold lead-in
  `\textbf{Price-to-Earnings (P/E) Ratio:}` on its own line before
  that paragraph, matching the sibling pattern.
- MINOR m-6: 9 body overfulls 0.27–10.02 pt, none in floats, none
  causing a spill — recorded, not fixed (rewording is prose,
  \sloppy loosens spacing).
- MINOR m-7: quotation single-spacing gap — the thesis's only
  \begin{quote} (line 86, freshness rule) is set at body 1.5
  spacing, while FOM p. 20 lists quotations among single-spaced
  elements. Preamble has \AtBeginEnvironment hooks for tabular and
  longtable but none for quote. Fix in preamble: add
  \AtBeginEnvironment{quote}{\singlespacing} beside lines 44–45.
- MINOR m-8: bank-profile sub-list lengths differ (4/4/4/4/2) —
  NOT a defect (benchmark bank has no merger mechanism).

## Passes (reviewer, accepted)

Table 3.1 caption above (correct for tables), complete, Table 3.1
numbering, columns fit, note markers ^a–^d explained; headings no
skip (3.1–3.6, subsections, subsubsections only under 3.5.2);
roadmap titles match section titles verbatim; lists balanced with
consistent lead-ins; equations numbered 3.1–3.13 sequentially;
zero dangling references (tab:mps_rd, fig:framework, Section 3.3.4,
Section 2.2.6, all 11 citation keys resolve); braces 397/397, all
environments balanced; TikZ picture ≈ 11.8 cm inside text width.

## Correction to the phase inventory

Chapter III contains a figure (TikZ Figure 3.1), so the chapter
figure count is 8 in total (7 \includegraphics in Chapter IV +
1 TikZ in Chapter III), not 7. The brief's "no figures" for
Chapter III was wrong; the reviewer caught it.
