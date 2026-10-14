# Format Gap List + Fix Plan: `src/proposal` vs Proposal Guidelines

**Guidelines:** `docs/reference/proposal/PROPOSAL_GUIDELINES.md` (measured from
`mbs-dissertation-proposal-sample_1.pdf`).
**Audited build:** `src/proposal/build/main.pdf` (15 pages; measured with PyMuPDF,
evidence lines cite `ours_lines.txt` line numbers).
**Method:** every gap below pairs a guideline value with a measured value from our PDF.
No inferred values.

Conventions: LM = left margin. Our body block: x = 90.1–523.3 pt (LM 31.8 mm, RM 25.4 mm).

---

## A. Must-fix gaps (visible deviation from the sample)

### A1. Body line spacing is narrower than the sample
- Guideline §2: true 1.5 spacing = **20.66 pt baseline pitch** for 12 pt text.
- Ours: `\onehalfspacing` = **17.96 pt pitch** (lines 59–61: 107.3 → 125.3 → 143.2).
- Fix (`main.tex`): replace `\onehalfspacing` with `\setstretch{1.5}` (≈ 21.75 pt pitch,
  standard LaTeX 1.5 — closest to both sample and FOM "1.5 everywhere").

### A2. Missing paragraph spacing
- Guideline §2: **+10 pt after each paragraph** (para-to-para gap 30.7 pt).
- Ours: `\parskip = 0` — paragraphs run together at line pitch (line 61 → 62:
  143.2 → 161.1 = 17.9, no extra gap).
- Fix: `\setlength{\parskip}{10pt}`. Use `enumitem` to zero out list spacing
  (`itemsep=0pt, topsep=0pt, parsep=0pt`) so list items keep single pitch like the
  sample (sample RQ/III items have no extra gap between items).
- Consequence: heading `aftersep` values must assume parskip no longer applies after
  headings — set section after = 8 pt (8 + nothing = sample §5: heading→body ≈ 18 pt
  after a ~16 pt heading line), subsection after = **8 pt** (currently 4 pt; sample
  L2→body gap 23.5 pt − 16.3 pt line ≈ 7–8 pt).
- Subsection before = **8 pt** (currently 12 pt; with preceding parskip 10 pt the total
  18 pt matches sample L2-before ≈ 18 pt). Section before stays 18 pt (10 + 18 = 28 ≈
  sample L1-before 21–28 pt).

### A3. Margins differ from the sample
- Guideline §1: LM **33.0 mm**, RM **≈ 24.2 mm**.
- Ours: LM 31.8 mm, RM 25.4 mm (FOM 2019 values).
- Fix: `\usepackage[top=2.54cm,bottom=2.54cm,right=2.4cm,left=3.3cm]{geometry}`.
- ⚠ Conflicts with FOM 2019 (L 3.18 / R 2.54). Per your instruction the **sample wins**
  for the proposal. Recorded here so it is not "corrected" back later.

### A4. Title page does not match the sample layout
Measured ours (lines 5–22) vs guideline §3:

| Item | Sample | Ours |
|---|---|---|
| Title size/case/position | 18 pt bold, title case, top y ≈ 73 | 16 pt bold, ALL CAPS, top y ≈ 141 |
| "A Dissertation Proposal" | 18 pt bold **underlined** | 14 pt bold, no underline |
| Block order | Submitted **by** (y≈327) → Submitted **to** (y≈520) | Submitted to → Submitted by (reversed) |
| "Submitted by/to" labels | 14 pt regular | 14 pt **bold** |
| Detail lines | 12 pt | 14 pt |
| Fulfillment/degree block | absent | present (italic block, lines 19–20) |
| Bottom lines | "Month, Year" / "Place", regular | "Pokhara, Nepal" / "October, 2026", bold |

- Fix (`front/titlepage.tex`): rewrite — 18 pt title-case title at top margin; underlined
  18 pt "A Dissertation Proposal"; Submitted-by block first; regular (non-bold) labels;
  12 pt detail lines; drop the fulfillment/degree block; bottom "Month, Year / Place"
  regular 14 pt.
- Content kept: student name/college/rolls, campus lines (reformatted into the sample's
  Submitted-to block shape: department/campus + dotted placeholder lines pattern).

### A5. TOC and References headings have the wrong weight/size
- Guideline §4/§5: TOC heading **16 pt regular** centered; References heading **14 pt bold**
  centered (sample p.12: 13.92 pt bold).
- Ours: both **16 pt bold** centered (lines 24, 442) — one shared numberless format.
- Fix: split the format — numberless `\section*` (TOC) → 16 pt regular centered;
  bibliography heading → 14 pt bold centered (patch the apacite heading or wrap
  `\bibliography` with a local `\titleformat`).

### A6. Roman lists are lowercase with the wrong indent
- Guideline §7: **uppercase** `I. / II. / III.`, numbers right-aligned (right edge ≈ 30 pt
  from LM), list text at **44.2 pt** from LM, wrapped lines same indent.
- Ours: lowercase `i. / ii. / iii.` at 11–15 pt from LM, text/wrap at **30 pt**
  (lines 107–112, 119–124).
- Fix (`02_…`, `03_…`): `enumitem` — `label=\Roman*.`, `align=right`,
  `leftmargin=44.2pt`, `labelsep` ≈ 14 pt, item text justified (already justified).

### A7. Hypothesis labels use math subscripts
- Guideline §8: `H1:` — roman, **not subscripted**, whole paragraph 12 pt; standard
  paragraph gap between items (sample: 30.7 pt item gap = line + 10 pt).
- Ours: `$H_1$:` (italic H, subscript numeral — lines 134–141) plus `\medskip` between
  items (extra, unmeasured gap on top of the paragraph gap).
- Fix (`04_hypothesis.tex`): roman `H1:`–`H4:` labels, remove `\medskip`, plain paragraph
  breaks. (Keep H1–H4: four hypotheses match our four IVs — see B6.)

### A8. Three section titles differ from the sample's fixed headings
- Guideline §5: `2. Statement of the problem` (ours: `Problem statement`),
  `4. Hypotheses` (ours: `Hypothesis`), `6. Review of Literature` (ours:
  `Brief review of the literature`), `7. Research Methodology` (ours: `Research
  methodology`), `5. Rationale of the Study` (ours: `… of the study`).
- Fix: rename to the exact sample strings (one-word edits in `02_`, `04_`, `05_`,
  `06_`, `07_` files).

### A9. Figure caption and box labels are bold 12 pt, not 11 pt italic
- Guideline §9: caption **below** figure, **11 pt italic**, indented 18 pt;
  "Independent variables" / "Dependent variable" labels **regular** 12 pt **below** the boxes.
- Ours: caption **12 pt bold**, full-width (line 344); both labels **bold**, and the IV
  label sits **above** the boxes (lines 343, 453).
- Fix: figure-only `\captionsetup{font={small,it}}` (11 pt italic), keep caption below;
  tikz label nodes `\normalsize` (drop `\bfseries`); move IV label below the IV boxes.
- Keep the `(Source: adapted from …)` note (academic-honesty requirement, absent from the
  sample) inside the same 11 pt italic caption — recorded deviation, not a defect.





### A10. Math renders in Computer Modern, not Times
- Guideline: everything Times New Roman (sample equations: TNR with true ~8 pt subscripts).
- Ours: `\mathit` → CMR12, symbols → NewTXMI/txmia (lines 124, 341, 389–392).
- Fix: `\usepackage{unicode-math}` + `\setmathfont{TeX Gyre Termes Math}` (Times-clone
  math under XeLaTeX); drop reliance on `newtxmath` for glyph shapes. Verify: recompile,
  re-extract fonts, confirm no `CMR`/`CMMI` remains.

### A11. URLs in References render in monospace
- Guideline §13: URLs in regular Times 12 pt (sample p.12).
- Ours: URL fragments in `LMMono12` (lines 476–477, 486–487) via hyperref `\url`.
- Fix: `\urlstyle{APACsame}` inside the refs group before `\bibliography`
  (apacite asserts its own `APACtt` mono style at begin-document, overriding a preamble
  `\urlstyle{same}` — verified: URLs stayed LMMono12 until this. Corrected 2026-10-13).

### A12. References hanging indent is short of 0.5 in
- Guideline §13: first line at LM, continuation at **+36 pt**.
- Ours: continuation at **+30 pt** (x = 120.0 vs 90.1, e.g. lines 444–445).
- Fix: plain `\setlength{\bibhang}{36pt}` in the preamble AFTER `\usepackage{apacite}`.
  Reason: with the `natbibapa` option natbib's list is in force (proven: continuation
  measured 29.9 pt = 2.5em despite `\bibleftmargin=36pt`), driven by `\bibhang`, and
  apacite's style hook runs exactly ONCE at package load (`\AtEndOfPackage`, apacite.sty
  l.1026-1035) — never again — so a direct set after the load sticks. Measured 129.4 pt
  (+35.9). Corrected 2026-10-13.

### A13. Body page numbers are bottom-center
- Sample: **no page numbers at all**. FOM 2019 (repo decision, EXTRACTED_SPEC §12):
  body Arabic **top right**, front matter Roman bottom-center — guideline wins over sample.
- Ours: bottom-center everywhere (TOC `ii` line 56; body `1`–`11` lines 94, 128, …).
- Fix: body pages `\fancyhead[R]{\thepage}` + empty footer; keep TOC `ii` bottom-center;
  title page unnumbered (already ✓).

---

## B. Intentional deviations — keep, do not "fix"

| # | Item | Authority |
|---|---|---|
| B1 | TOC entries filled (sample TOC page is blank) | Guidelines §4 prescribes filling it |
| B2 | References match the sample (SUPERSEDED 2026-10-13, see refs-style): 1.5 within entries + 6 pt between (`\setstretch{1.5}` group, `\bibsep=6pt`). FOM 2019 lines 769-770 order 1.5 "in references"; the same passage's line 771 says "single" — self-contradictory, so sample + explicit instruction govern. `\interlinepenalty` keep-together removed. Verified: pitch 21.7, gaps 27.6 |
| B3 | TOC single-spaced | FOM 2019 p.20 (already implemented, lines 97–101) |
| B4 | §6 subsections 6.1 Theoretical review / 6.2 Empirical review / 6.3 Research gap (sample §6 is flat prose) | Navigation aid; listed in TOC |
| B5 | Decimal bank list (7.2) + numbered analysis protocol (7.5) — no sample equivalent | Standard structure, sample-silent |
| B6 | Four hypotheses H1–H4 (sample has three) | Follows our four IVs |
| B7 | Model equation centered + numbered `(1)` (sample: left-aligned, unnumbered) | Cross-referenced as Eq. 1 in four places; renumbering the prose costs more than it saves |
| B8 | Content extensions (feasibility screen, diagnostics, transition-year rules) | Research substance, not format |

## C. Length warning (decision required before final compile)

- Ours now: **15 pages** (title + TOC + 11 body + 2 refs), body **3,932 words**.
- Sample: **12 pages**, body **2,991 words**. FOM proposal range: 8–12 pages.
- Fixes A1 + A2 **increase** page count (~+15–20% → ≈ 17 pages total).
- Options: (C-a) trim body to ≈ 3,000 words after the format fixes and re-measure;
  (C-b) confirm with campus that 13–15 pages is acceptable for this topic and record it.
  Recommended: implement A-fixes first, measure exact pages, then trim once to target 12.

---

## A4 implementation plan (title page rewrite — IMPLEMENTED 2026-10-13; fulfillment KEPT per user)

### A4.0 Measured targets (sample p.1, block tops, pt from page top)

| Block | Sample top | Size/style |
|---|---|---|
| Title, 2 lines | 73 / 104 | 18 pt bold, centered, title case |
| `A Dissertation Proposal` | 228 | 18 pt bold **underlined**, centered |
| `Submitted by` | 327 | 14 pt regular, centered |
| Student block, 4 lines @ ~16 pt pitch | 353 | 12 pt regular, centered |
| `Submitted to` | 520 | 14 pt regular, centered |
| Department block, 4 lines @ ~16 pt pitch | 547 | 12 pt regular, centered |
| `Month, Year` | 721 | 14 pt regular, centered |
| `Place` | 740 | 14 pt regular, centered |

Bottom-to-top gaps: title→proposal 103 pt (3.6 cm); proposal→Submitted by 78 pt
(2.7 cm); Submitted by→student block ~10 pt; student block→Submitted to 107 pt
(3.7 cm); Submitted to→dept block ~10 pt; dept block→date ~113 pt (flexible joint).

### A4.1 Content mapping (ours → sample shape)

- Title → title case, 18 pt bold, natural line breaks (no manual `\\`):
  `Accounting Fundamentals and Post-Disclosure Share Prices: Evidence from
  Selected Nepalese Commercial Banks`
- Proposal line → `\underline{A Dissertation Proposal}`, 18 pt bold.
- Submitted-**by** block first (sample order), 12 pt: Asmita Subedi / Triveni
  International College / Exam Roll No: 67514/24 / T.U. Regd. No: 7-2-48-1060-2018.
  (No Campus Roll No. line — do not invent one.)
- Submitted-**to** block: see decision D1.
- Bottom block, sample order (date then place): `October, 2026` / `Pokhara, Nepal`,
  14 pt regular (current file has them bold + reversed — fix both).
- DELETE the `In partial fulfillment… (M.B.S.)` block (absent from sample).

### A4.2 Layout recipe (`front/titlepage.tex` rewrite)

- Keep `\begin{titlepage}` + `\thispagestyle{empty}` as first line (main.tex NOTE:
  it must precede the environment's page break).
- Remove `\vspace*{1.5cm}` top/bottom and all `plus 1fill` glues.
- Scope the whole page: `\singlespacing` + `\setlength{\parskip}{0pt}` (neutralises
  global 1.5 stretch and 10 pt parskip; spacing becomes fully explicit).
- Fixed chain (nominal; verify §A4.3, adjust once):
  1. Title `{\fontsize{18}{22}\selectfont\bfseries ...}` at text-area top (no vspace).
  2. `\vspace{3.2cm}` → proposal line.
  3. `\vspace{2.7cm}` → `Submitted by` (14 pt).
  4. `\vspace{0.35cm}` → student block `{\fontsize{12}{16}\selectfont ...}` (pitch 16 ≈ sample 15.9).
  5. `\vspace{3.7cm}` → `Submitted to` (14 pt).
  6. `\vspace{0.35cm}` → dept block (12/16).
  7. `\vspace{\fill}` → date/place block (pins bottom; absorbs title-length variance).
  8. Date → place: `\\[2pt]` (≈ sample 18.5 pt pitch).
- Dotted placeholder lines: NOT needed — our values are known (sample's dots are
  handwriting placeholders).

### A4.3 Verification (after compile)

- Title occupies exactly 1 page (currently spills to 2).
- Block tops within ±20 pt of targets (proposal ~228, subby ~327, subto ~520,
  date ~715); sizes 18/18/14/12 exact; labels non-bold.
- Visual render crop: underline present under proposal line; all lines centered.
- If proposal/subby/subto drift > 20 pt (our title line count differs), adjust only
  vspace #1 once, re-measure.

### A4.4 Decisions required before implementation

- **D1 — Submitted-to block:** (a) sample pattern `Research Department / Triveni
  International College` [RECOMMENDED — matches a campus-level proposal], vs
  (b) keep current `Office of the Dean / Faculty of Management / Tribhuvan
  University` (thesis-cover pattern, absent from the sample).
- **D2 — Bottom order:** date-then-place per sample (swap current). Recommend yes.
- **D3 — Delete fulfillment/degree block.** Recommend yes (absent from sample).
- **D4 — No Campus Roll No. line** (we have no value; sample has the line). Recommend
  omit rather than invent.

## Fix plan (implementation order)

**Phase 1 — preamble only (`main.tex`), no content edits**
1. A3 geometry → `left=3.3cm,right=2.4cm` (top/bottom unchanged).
2. A1 `\onehalfspacing` → `\setstretch{1.5}`.
3. A2 `\setlength{\parskip}{10pt}` + `\usepackage{enumitem}` with global
   `\setlist{nosep,leftmargin=*}` baseline, then per-list indents (A6: roman lists
   `label=\Roman*.,align=right,leftmargin=44.2pt`; itemize text indent 36 pt to match
   sample bullet text at +36 pt — ours is currently +30 pt, lines 320–326).
4. A5 split numberless heading format (TOC regular 16 / bib heading bold 14).
5. A10 unicode-math + Termes Math; A11 `\urlstyle{same}`; A12 `\bibhang=36pt`.
6. A13 page-number placement (fancyhead[R] for body; TOC stays bottom-center roman).
7. A9 caption setup for figures (`font={small,it}`); A2-related `titlespacing` tweak:
   subsection after 4 pt → 8 pt, subsection before 12 pt → 8 pt.

**Phase 2 — content files**
8. A4 rewrite `front/titlepage.tex` per the table (18 pt title-case title, underlined
   proposal line, by-before-to order, 12 pt details, no fulfillment block).
9. A8 rename the five headings (one-line edits each).
10. A7 `04_hypothesis.tex`: roman labels, drop `\medskip`.
11. A9 `07_methodology.tex`: un-bold tikz labels, IV label below boxes, caption text to
    `Figure 1. …` pattern keeping the source note.

**Phase 3 — verify (no eyeballing)**
12. Recompile (`xelatex → bibtex → xelatex ×2`), confirm zero errors/warnings about
    fonts or overfull boxes.
13. Re-run the PyMuPDF measurement (same script as this audit) and check: body pitch
    ≈ 21.75 pt, para gap ≈ +10 pt, LM x = 93.6 pt, right edge ≈ 526.7 pt, heading sizes
    14 pt / TOC 16 pt regular / refs-heading 14 pt bold, roman numerals uppercase at
    44.2 pt text indent, caption 11 pt italic, no CMR/LMMono fonts, page numbers top-right.
14. Record final page count → triggers decision C-a vs C-b.

**Phase 4 — length (only after Phase 3 numbers exist)**
15. If over 12 pages: trim body toward ≈ 3,000 words (candidate cuts: compress 7.2 bank
    list, shorten diagnostics item 4, tighten literature paragraphs) — or record C-b.
