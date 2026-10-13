# Plan 07 — Figure 1 in standard form (matches professor sketch)

Source: `../detail/14_methodology_figure_table_model.md` ("Present the research framework in a standard form") + `../detail/16_handdrawn_framework_guide.md` (sketch template)
Target: `src/proposal/sections/07_methodology/07_methodology.tex` — `figure` environment with `tikzpicture` (replaces the 4-top-boxes → 1-bottom-bar diagram).

## Standard form (what the sketch orders)

Left column = Independent variables (EPS, DPS, BVPS, ROA). Right box = Dependent variable (MPS-post). Arrows independent → dependent. Labels "Independent variables" / "Dependent variable". Caption "Figure 1: Research framework (Source: ...)" with source completed. This is the layout in the professor's hand sketch (file 16), not the current wide 4-across top row.

## Paste-ready LaTeX (replaces the whole `\begin{figure}...\end{figure}`)

```latex
\begin{figure}[h]
\centering
\begin{tikzpicture}[node distance=0.45cm,
  ind/.style={rectangle, draw, minimum width=3.4cm, minimum height=0.7cm, text centered, font=\small},
  dep/.style={rectangle, draw, minimum width=3.6cm, minimum height=1.7cm, text centered, font=\small, fill=gray!10},
  arrow/.style={thick,->,>=stealth}]
  \node[ind] (eps)  {EPS};
  \node[ind, below=of eps] (dps)  {DPS};
  \node[ind, below=of dps] (bvps) {BVPS};
  \node[ind, below=of bvps] (roa) {ROA};
  \node[dep, right=2.2cm of bvps] (mps) {$\mathit{MPS}^{\mathit{post}}$};
  \draw[arrow] (eps.east)  -- ([yshift=18pt]mps.west);
  \draw[arrow] (dps.east)  -- ([yshift=6pt]mps.west);
  \draw[arrow] (bvps.east) -- ([yshift=-6pt]mps.west);
  \draw[arrow] (roa.east)  -- ([yshift=-18pt]mps.west);
  \node[above=0.2cm of eps, font=\small\itshape] {Independent variables};
  \node[below=0.25cm of mps, font=\small\itshape] {Dependent variable};
\end{tikzpicture}
\caption{Research framework (Source: adapted from Pradhan and Dahal, 2016)}
\label{fig:framework}
\end{figure}
```

Requires the existing preamble `\usetikzlibrary{shapes,arrows,positioning}` (already in `main.tex` — no new package). Dependent box height is 1.7cm (half-height ≈ 24pt) so the ±18pt/±6pt arrow landings hit the box edge; an 0.85cm box would leave the outer arrows floating.

## Verify after apply

- PDF Figure 1: 4 stacked left boxes (EPS/DPS/BVPS/ROA) with 4 arrows into 1 right box (MPS-post). "Independent variables" above left column, "Dependent variable" below right box. Caption + label intact so `Figure~\ref{fig:framework}` still resolves. LOF entry unchanged (1 figure).
