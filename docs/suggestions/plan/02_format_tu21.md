# Plan 02 — TU guideline strict format (p.21 checklist)

Source: `../detail/02_table_of_content.md` ("Follow the TU guidelines Strictly", "Font size 12 & Times New-Roman", "Page 21")
Target: `src/proposal/main.tex` (preamble + front matter only — body text untouched here)

## TU FOM 2019 p.20–21 rules (from `docs/format/TU_FOM_Master_Dissertation_Guideline_2019.txt` lines 765–795)

| Item | TU requirement | Current status | Action in this plan |
|---|---|---|---|
| Paper | ISO A4 white bond, recto (one side) only | `a4paper,oneside` — OK | keep |
| Font | Times New Roman 12pt uniform | `12pt` + `newtxtext/newtxmath` (Times clone for pdflatex) — OK | keep, no Cambria/Calibri |
| Spacing | 1.5 everywhere; SINGLE only in TOC/charts/tables/references | `\onehalfspacing`; TOC/LOT/LOF + references wrapped in `\singlespacing` — OK | keep |
| Margins | top 2.54 / bottom 2.54 / right 2.54 / LEFT 3.18 cm | `geometry{top=2.54cm,bottom=2.54cm,right=2.54cm,left=3.18cm}` — OK | keep |
| Front pages | counted, lowercase roman (ii, iii, iv...), bottom centre; title = i counted unnumbered | roman ii,iii,iv bottom centre; title empty — OK | keep |
| Body pages | arabic 1,2,3... at TOP RIGHT from first body page through end | currently bottom-centre throughout (campus habit) — NOT TU-strict | **FIX below**: body arabic top-right; front stays bottom-centre |
| TOC heading | "Table of contents" (guideline p.9) | article default prints "Contents" — NOT TU-strict | **FIX below**: rename to "Table of Contents" (+ LOT/LOF names) |
| Proposal length | 8–12 pages approx. (p.8) | currently 15 with TOC/LOT/LOF | flag only — re-write (plans 04–05) should trim toward 12; do not pad |
| References | APA 6th | `apacite` + `natbibapa` — OK | keep |

## Edits to `main.tex`

### (a) TOC/LOT/LOF headings → TU wording (add after `\usepackage` block, before `\begin{document}`)

```latex
% TU-strict front-matter headings (guideline p.9)
\renewcommand{\contentsname}{Table of Contents}
\renewcommand{\listtablename}{List of Tables}
\renewcommand{\listfigurename}{List of Figures}
```

### (b) Page numbers: front bottom-centre, body top-right (replace the fancyhdr block)

Current block (bottom-centre for everything):
```latex
\pagestyle{fancy}
\fancyhf{}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0pt}
```
Replace with:
```latex
% TU p.21: front matter roman bottom-centre; body arabic top-right.
\pagestyle{fancy}
\fancyhf{}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0pt}
% Body top-right is activated after the front matter with \fancyfoot{} + \fancyhead[R].
```
And in the front→body transition (after `\endgroup` closing the TOC/LOT/LOF singlespace group, before `% --- Main body`):
```latex
% --- Main body i-vii ---
% Body restarts at arabic 1 per FOM p.21, numbers at top right.
\pagenumbering{arabic}
\setcounter{page}{1}
\fancyhf{}
\fancyhead[R]{\thepage}
\renewcommand{\headrulewidth}{0pt}
```
Front matter keeps the earlier `\fancyfoot[C]` (roman ii, iii, iv at bottom centre). Body switches to `\fancyhead[R]` (arabic 1,2,3... at top right). Title page stays `\thispagestyle{empty}` (counted i, unnumbered).

## Verify after apply

- Title = unnumbered; TOC = ii, LOT = iii, LOF = iv (bottom centre); body = 1,2,3... (top right).
- "Table of Contents" / "List of Tables" / "List of Figures" headings in TU wording.
- Margins/font/spacing unchanged. Build still 0 errors.
