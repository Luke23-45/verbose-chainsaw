# Plan 03 — Research questions as simple sentences

Source: `../detail/05_problem_statement_p2.md` ("Rewrite these question in a simple sentence")
Targets:
- `src/proposal/sections/02_problem_statement/02_problem_statement.tex` (questions block)
- `src/proposal/sections/03_objectives/03_objectives.tex` (objectives must mirror the questions 1:1 — supervisor checks this consistency first)

## Rule used

One question = one simple sentence = one clause, no commas stacking ideas. Keep every variable (EPS, DPS, BVPS, ROA, MPS-post) and the sample (sampled commercial banks) and the method hint (describe / associate / jointly explain). No new variables. No P/E (excluded everywhere by design).

## Old questions (3 long multi-clause — to be replaced)

1. What are the distributional characteristics, baseline levels, and trends of EPS, DPS, BVPS, ROA, and MPS-post across the sampled commercial banks?
2. How is each individual accounting fundamental (EPS, DPS, BVPS, and ROA) associated with post-disclosure market price per share (MPS-post)?
3. To what extent do the four accounting fundamentals jointly explain variation in MPS-post within a multiple linear regression framework?

## New questions (paste into `02_problem_statement.tex` enumerate)

```latex
\begin{enumerate}
  \item What are the levels and trends of EPS, DPS, BVPS, ROA, and $\mathit{MPS}^{post}$ in the sampled banks?
  \item How is each fundamental linked to $\mathit{MPS}^{post}$?
  \item How well do the four fundamentals jointly explain $\mathit{MPS}^{post}$?
\end{enumerate}
```

Each is one simple sentence (question). Coverage kept: Q1 = description of all five series; Q2 = bivariate link per fundamental; Q3 = joint multiple-regression explanatory power.

## Mirroring objectives (paste into `03_objectives.tex` enumerate — wording already simple, align verbs to new Qs)

```latex
\begin{enumerate}
  \item To describe the levels and trends of EPS, DPS, BVPS, ROA, and $\mathit{MPS}^{post}$ in the sampled banks.
  \item To measure the link between each fundamental and $\mathit{MPS}^{post}$.
  \item To estimate how well the four fundamentals jointly explain $\mathit{MPS}^{post}$.
\end{enumerate}
```

Keep the primary-objective paragraph above the list unchanged (it already states the six-year before/during/after-2023 window and names MPS-post as post-disclosure price).

## Consistency check (do before applying)

- Q1 ↔ Obj 1 (describe levels/trends) ↔ Descriptives in Methods (mean/SD/min/max).
- Q2 ↔ Obj 2 (link each fundamental) ↔ Pearson correlation in Methods.
- Q3 ↔ Obj 3 (jointly explain) ↔ OLS Eq.(1) + R²/F/t in Methods + H1–H4 (all four stay directional-positive with two-tailed 5% tests).
- Hypotheses H1–H4 wording unchanged (accepted on p.3 per `../detail/06_*`).

## Verify after apply

- `pdftotext` p.2: three one-line questions, each ending with "?". No "distributional characteristics, baseline levels" stack. No meaning lost.
