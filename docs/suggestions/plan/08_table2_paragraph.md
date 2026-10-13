# Plan 08 — Table 2 → paragraph (professor: "Write it in paragraph not in table")

Source: `../detail/14_methodology_figure_table_model.md` (right-margin note + `///` flourish pointing at Table 2)
Target: `src/proposal/sections/07_methodology/07_methodology.tex` — delete the whole `\begin{table}...\end{table}` (Description of variables) + the sentence "The operational measurements ... summarized in Table~2." Replace both with the paragraph below. Eq.(1) and its where-paragraph stay EXACTLY (ticked OK).

## Paste-ready LaTeX

Replace:
```latex
The operational measurements and descriptions of all variables analyzed in this
study are summarized in Table~\ref{tab:variables}.
```
plus the entire `table` environment (`\label{tab:variables}` included) with:

```latex
Post-disclosure market price per share ($\mathit{MPS}^{\mathit{post}}$) is the closing market price on the first NEPSE trading day following public disclosure of the corresponding audited annual financial statements through NEPSE. Earnings per share (EPS) is profit attributable to ordinary equity holders divided by weighted average ordinary shares outstanding during the period from the audited report. Dividend per share (DPS) is dividend per share reported for the corresponding fiscal year in the audited annual report. Book value per share (BVPS) is reported book value per share from the audited annual report. Return on assets (ROA) is reported return on assets (net profit after tax divided by total assets, multiplied by 100) from the audited annual report.
```

Definitions are word-identical to the deleted table cells — only the container changes (table → running paragraph). No numbers altered. No P/E added back.

## Consequences (handled, not hidden)

- `\label{tab:variables}` disappears; any `\ref{tab:variables}` elsewhere must be removed (only the lead sentence above referenced it — replaced). LOT drops from 2 tables to 1 (meta table only) — correct per order.
- Keep `\label{fig:framework}` and `\label{eq:main}` untouched.

## Verify after apply

- `grep "tab:variables"` returns zero hits in `src/proposal/`.
- LOT lists only "Meta table of related studies". No "Description of variables" row.
- Build 0 errors (longtable meta table unaffected).
