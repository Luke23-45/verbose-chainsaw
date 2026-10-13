# Reference Thesis — Extracted Format & Structure Spec

**Source (authoritative for this document):**
- `docs/reference/docx/Cover Part.docx` (1 page)
- `docs/reference/docx/Main Part.docx` (63 pages, 12,889 words per docProps)

**Reference work:** *Factors Affecting the Share Price of Nepalese Commercial Banks* — Narayan
Chaudhary Tharu, Lumbini Banijya Campus, Exam Roll 3020147, TU Regd. 7-2-302-404-2012, "A Thesis"
submitted to the Office of the Dean, Faculty of Management, Tribhuvan University, June 2020.
(M.B.S. thesis; same topic family as our study.)

Everything below was extracted programmatically from the OOXML (`python-docx` + raw
`document.xml`/`footer1.xml`/`numbering.xml`/`styles.xml`). Every number is stated in its native
unit with conversions. Nothing here is inferred.

---

## 1. Page setup (identical `sectPr` in BOTH files)

Raw XML: `<w:pgSz w:w="12240" w:h="15840"/>`
`<w:pgMar w:top="2160" w:right="1440" w:bottom="1440" w:left="2160" w:header="720" w:footer="720" w:gutter="0"/>`
`<w:docGrid w:linePitch="360"/>`

| Setting | Twips | Inches | cm |
|---|---|---|---|
| Page size | 12240 × 15840 | 8.5 × 11 | 21.59 × 27.94 (**US Letter**) |
| Top margin | 2160 | 1.5 | 3.81 |
| Bottom margin | 1440 | 1.0 | 2.54 |
| Left margin | 2160 | 1.5 | 3.81 |
| Right margin | 1440 | 1.0 | 2.54 |
| Header distance | 720 | 0.5 | 1.27 |
| Footer distance | 720 | 0.5 | 1.27 |
| Gutter | 0 | 0 | 0 |

- Orientation: portrait. `docGrid linePitch=360` (18 pt grid).
- Cover file: same margins, **no footer reference** (no page number on cover).
- Main file: one section only (no section breaks mid-document); footer ref `rId14` → `footer1.xml`.

> ⚠ These differ from the FOM 2019 guideline (A4; T/B/R 2.54 cm, L 3.18 cm). See §12.

## 2. Typography

**Body (dominant paragraph: 462 occurrences of this exact spacing):**

| Property | Value | Evidence |
|---|---|---|
| Font | Times New Roman, explicit on every run | 783 runs `w:rFonts` TNR |
| Body size | **12 pt** (`w:sz 24`) | 2861 `sz=24` runs incl. tables |
| Heading size | **14 pt** (`w:sz 28`) | 153 `sz=28` runs |
| Alignment | **Justified** (`w:jc both`) | 992 occurrences (`center` 490 = chapter heads, cover, textboxes) |
| Space before / after | **12 pt each** (`w:before="240" w:after="240"`, twentieths of pt) | — |
| Line spacing | **1.6 × line** (`w:line="384" w:lineRule="auto"`, 384/240) | dominant variant |
| Bold usage | headings, table captions, figure captions, `Model`, variable names, lead-in labels | 137 bold runs |

- `docDefaults` (11 pt, line 259 ≈ 1.08, after 160 = 8 pt) exists but is **overridden everywhere** — ignore it.
- Empty paragraphs inside VML text boxes use `after=0 line=240` (single) — not body text.
- SPSS-pasted tables use `after=0 line=320 atLeast` (≥16 pt) inside cells; the three hand-built
  tables (meta, variables, descriptive) use the body rule (before/after 12 pt, line 384).
- No italics/underline anywhere except none observed in headings; language `en-US`.
- **No footnotes, no endnotes** (both parts are empty).
- Blank-line filling: the author pads with empty paragraphs (runs of 5–13 empties before chapter
  headings), not `spacebefore` tricks.

## 3. Cover page (`Cover Part.docx`) — line-by-line

All paragraphs: **centered**, line spacing **1.5** (`ONE_POINT_FIVE`), `space_after=0`, TNR.

| # | Text | Size | Bold |
|---|---|---|---|
| 1 | `FACTORS AFFECTING THE SHARE PRICE OF NEPALESE COMMERCIAL BANKS` | **16 pt** | **bold** |
| 2 | *(empty)* | | |
| 3 | `A Thesis` | 14 pt | **bold** |
| 4 | *(empty)* | | |
| 5 | `Submitted to` | 14 pt | **bold** |
| 6 | *(empty)* | | |
| 7 | `Office of the Dean` | 14 pt | plain |
| 8 | `Faculty of Management` | 14 pt | plain |
| 9 | `Tribhuvan University` | 14 pt | plain |
| 10–11 | *(2 empties)* | | |
| 12 | `By` | 14 pt | **bold** |
| 13 | `Narayan Chaudhary Tharu` | 14 pt | plain |
| 14 | `Lumbini Banijya Campus` | 14 pt | plain |
| 15 | `Exam Roll No: 3020147` | 14 pt | plain |
| 16 | `T.U. Regd. No: 7-2-302-404-2012` | 14 pt | plain |
| 17–18 | *(2 empties)* | | |
| 19 | `In partial fulfillment of the requirements for the Degree of` | 14 pt | plain |
| 20 | `Master of Business Studies (M.B.S.)` | 14 pt | **bold** |
| 21–22 | *(2 empties)* | | |
| 23 | `Butwal, Nepal` | 14 pt | **bold** |
| 24 | `June, 2020` | 14 pt | **bold** |

Block order: **TITLE → A Thesis → Submitted to (Dean/FoM/TU) → By (name/campus/roll/regd) →
fulfillment line → degree → place, date.** No approval/signature page inside these two files.

## 4. Heading hierarchy

Chapter headings are **two centered lines**, TNR 14 pt **bold**:

```
CHAPTER- I            ← centered, 14 bold
INTRODUCTION          ← centered, 14 bold
```

Variants found (verbatim, inconsistent): `CHAPTER- I`, `CHAPTER- II`, `CHAPTER- III`,
`CHAPTER-IV` (no space), `CHAPTER –V` (en dash).

Section / subsection headings: **justified, TNR 14 pt bold**, style = `Normal`
(**typed manually — no Word heading styles, no auto TOC**):

- Level 1: `1.2 Statement of Problem` — number typed as a separate run (`'1.2' + ' ' + text`).
  - Exception: `Background of the Study` is auto-numbered via list `numId 1` → absNum 6,
    ilvl 1, `lvlText="%1.%2"` → renders as `1.1`.
- Level 2: `2.1 Conceptual Review`, `2.1.1 Sock Prices` — same 14 pt bold justified.
- Level 3: `4.3.1 Earning per share and Market price per share` — **12 pt bold justified**
  (step down from 14 pt at x.y.z, except `3.4.1 Model Specification` which is 14 pt bold).
- Bold 12 pt labels (not headings): `Variables and their measurement`,
  `Model`, `Model Interpretation of <var> in relation to Market per share`,
  variable names inside §3.6 (`Earnings Per Share`, …).

No heading uses `space_before ≠ 12 pt`; headings are separated from body only by the standard
12 pt before/after — **no extra vertical space above headings**.

## 5. Page breaks

Exactly **5 explicit page breaks** (`<w:br w:type="page"/>`, in empty paragraphs):

1. Before `CHAPTER- II`
2. Before `Table 2.1: Meta Table Showing Review of Related Studies` (mid Ch. II — stray)
3. Before `CHAPTER- III`
4. Before `Figure 4.2 shows average dividend per share…` (mid Ch. IV — stray)
5. Before `BIBLIOGRAPHY`

**No explicit break before CHAPTER-IV or CHAPTER-V** (relied on flow — a defect, §11).
`w:pageBreakBefore` count: 0. `w:lastRenderedPageBreak` (Word's cached soft breaks): 58.

## 6. Lists (numbering.xml)

| List | numId → absNum | Format | Indent (left / hanging) |
|---|---|---|---|
| Research questions (2 items) | 2 → 8 | **lowerRoman** `%1.` → `i.`, `ii.` | 1080 / 360 tw (0.75" / 0.25") |
| Objectives (2 items) | 3 → 9 | **lowerRoman** `%1.` → `i.`, `ii.` | 1080 / 360 tw |
| Limitations (5 items) | 4 → 3 | decimal `%1.` → `1.` | 720 / 360 tw (0.5" / 0.25") |
| Sample banks (5 items) | 5 → 5 | decimal `%1.` | 720 / 360 tw |
| Major findings (13 items) | 7 → 4 | **bullet** `•` (`\uf0b7`, Symbol font) | 720 / 360 tw |
| Recommendations (5 items) | 9 → 1 | **bullet** | 720 / 360 tw |

- List paragraphs keep body formatting: TNR 12 pt, justified, 1.6 spacing, 12 pt before/after.
- RQ text pattern (verbatim): `Is there any relationship between EPS, DPS, P/E ratio, BVPS, ROA
  and MPS?` / `Do the EPS, DPS, P/E Ratio, BVPS and ROA affect the MPS?`
- Objective pattern: `To investigate the relationship between …` / `To examine the effect of …`
  (objectives mirror RQs but are **not** 1:1 sentences — 2 RQs / 2 objectives).
- Lead-in lines: problem statement ends `…this study deals with the following issues:` ;
  objectives: `The major objective of this study is to examine the factors affecting the share
  prices of Nepalese commercial banks. The specific objectives of this study are:`

## 7. Tables

24 tables total.

**Hand-built (TNR 12, justified, before/after 12 pt, line 1.6):**

| # | Table | Size | Style |
|---|---|---|---|
| t0 | `Table 2.1: Meta Table Showing Review of Related Studies` | 9×4 (`S.N. | Author(S) | Objective | Major Findings`) | **Table Grid** |
| t1 | `Table 3.2: Description of variables` | 8×4 (`S.N. | Variables | Description | Measurement`) | **Table Grid** |
| t8 | `Table 4.7: Descriptive statistics…` | 7×5 (`Variables | Minimum | Maximum | Mean | S.D.`) | **Table Grid** |

- **Caption ABOVE the table**, TNR **12 pt bold**, justified, `before=12pt after=12pt`:
  `Table 2.1: Meta Table Showing Review of Related Studies`,
  `Table 3.2: Description of variables`, `Table 4.7: Descriptive statistics for selected …`.
- **Source line BELOW the table**: `Source: Annual Report of concern Banks` — TNR 12 pt plain,
  manually right-positioned with ~40 leading spaces (not a right tab).
- SPSS output tables (t2–t7, t9–t23: Model Summary / ANOVA / Coefficients / Correlations pasted
  from SPSS): style `Normal Table`, cell text TNR 12, `line=320 atLeast`, `after=0`, justified;
  SPSS footnote rows retained verbatim (`a. Dependent Variable: Market Per Share`).
- Data tables t2–t7: 11×8 (`Year/Bank | NIBL | KBL | HBL | GIBL | NMBL | Mean | S.D.`) =
  header + 8 fiscal-year rows (2068/69–2075/76, `Mean`/`S.D` per-year columns) + trailing
  per-bank `Mean` and `S.D` rows (structure pattern for all six indicator tables).

## 8. Figures

- **6 figures = embedded Excel charts** (`word/charts/chart1–6.xml` + 6 embedded
  `Microsoft_Excel_Worksheet*.xlsx`) — figures 4.1–4.6 (EPS, DPS, P/E, ROA, BVPS, MPS).
- **Caption BELOW the chart**, TNR **12 pt bold**, justified, verbatim pattern:
  `Figure 4.1 shows average earning per share of different commercial banks of Nepal.`
  (statement form, not `Figure 4.1: Title`).
- Immediately after: a plain 12 pt interpretation paragraph
  (`Figure 4.2 shows the fluctuation pattern of the Divided per share over the study period…`).
- Sometimes a *second* bold caption-style line appears above the chart
  (`Figure 4.3 shows the average P/E ratio … (in rupees).`) — duplicated captions are a defect.
- **Theoretical framework figure (§1.5)** = VML shapes (7 drawings in body idx 26–35):
  - Labels above: `Independent Variable` (left) / `Dependent Variable` (right), plain text.
  - Five IV rectangles: `Earnings per share (EPS)`, `Dividend per share (DPS)`,
    `Price to Earnings Ratio (P/E)`, `Book value per share (BVPS)`, `Return on assets (ROA)`.
  - Connectors/arrows → one DV rectangle: `Market price per share (MPS)`.
  - Below: `Source: Pradhan and Dahal,2014` — TNR 12 pt plain.

## 9. Model equation

Label line above (12 pt **bold**): `Model `

Equation paragraph (justified, TNR 12 pt), verbatim:

```
MPS = α+β1EPS+β2DPS + β3P/E + β4BVPS + β5 ROA + ei  ………………………(1)
```

- Greek letters α/β typed directly (Unicode), subscripts NOT used (flat `β1`).
- Ellipsis characters `…` padded manually before the right-aligned `(1)` — no tab stops observed.
- Followed by bold label `Variables and their measurement`, then pointer sentence
  `The description of dependent and independent variables used in the study and their definition
  and measurement are shown in table 3.2.`, then Table 3.2.

## 10. Hypotheses (§3.6)

Per variable block, in this exact order:

1. Variable name — TNR **12 pt bold**, justified: `Earnings Per Share`
2. Justification paragraph citing 2–4 studies, ending `Based on it, the study develops the
   following hypothesis` (or `…the following hypothesis.`)
3. Hypothesis line — TNR 12 pt **plain**, justified: `H1: There is a positive relationship
   between EPS and MPS`

Order: EPS→H1, DPS→H2, P/E→H3, ROA→H4, BVPS→H5. (H1 lacks the final period; H2–H5 have it —
defect.)

## 11. Bibliography (`BIBLIOGRAPHY`)

- Heading: `BIBLIOGRAPHY`, centered, TNR **14 pt bold**, on its own page (explicit break).
- Entries: TNR **12 pt**, justified, **hanging indent left = 457200 EMU (1.27 cm / 0.5"),
  first-line = −457200 EMU**, `line 1.6`, before/after 12 pt.
- Alphabetical by author surname (Aurangzeb → … → Van Horn). 22 entries.
- Dominant entry pattern: `Author, I. (Year). Title of article. Journal Name, vol(x), pages.`
  e.g. `Malhotra, N., &Tandon, K. (2013). Determinants of stock prices: Empirical evidence from
  NSE 100 companies. IRACST- International Journal of Research in Management & Technology 3(3),
  86-95.`
- Book pattern: `Author, I. (Year). Title. City: Publisher.`
- **Do not replicate its completeness** — many in-text citations are missing from the
  bibliography (e.g. Lama 2016, Pradhan 2017, Uddin & Rahman 2013, Geetha & Swaminathan 2015,
  Modigliani & Miller 1958…) and `Thapa & Rana` is cited as 2013 in text but 2011 in the
  bibliography. Replicate the *format*, verify every entry.

## 12. Footer / page numbering

- `footer1.xml`: single paragraph, `style=Footer`, **`w:jc center`**, contains field
  `PAGE \* MERGEFORMAT` (cached value "65"). → **page number centered at bottom** on every page.
- Cover: no footer at all.
- **Conflict with FOM 2019 guideline** (`TU_FOM_Master_Dissertation_Guideline_2019.txt`, lines
  785–790): body pages must be Arabic numerals **top right**; front matter Roman numerals
  bottom-center; title page counted but unprinted. The reference docx puts Arabic bottom-center
  for the body — guideline wins for our document (our proposal already follows the guideline).

## 13. Conflicts: reference docx vs FOM 2019 guideline (guideline wins)

| Item | Reference docx | FOM 2019 (authoritative) |
|---|---|---|
| Paper | US Letter 21.59×27.94 | **ISO A4** (B4 only if needed) |
| Margins | T/L 3.81, B/R 2.54 cm | **T/B/R 2.54, L 3.18 cm** |
| Body line spacing | 1.6 + 12 pt before/after | **1.5 everywhere** (single only in TOC/charts/tables/quotes/references) |
| Body page number | bottom center | **top right (Arabic)**; front matter bottom center (Roman) |
| Font | TNR 12 body / **14 bold headings** | TNR **uniform 12 pt** ("uniform typeface and font size") |
| Captions | table title above / figure caption below ✓ | table titles **above**, figure captions **below** ✓ |
| Typing side | (not stated) | recto only |

Where the reference and guideline agree (caption placement, TNR, 12 pt body, hanging-indent
bibliography style, chapter structure) — replicate with confidence.

## 14. Chapter-by-chapter replication blueprint

**Cover** (§3) → page break → **Main Part**:

- **CHAPTER- I / INTRODUCTION** (starts doc)
  - `Background of the Study` (auto 1.1) — 8 justified 12 pt paragraphs, author-year in-text
    citations in parentheses: `(Mosley & Singer, 2018)`, `(Bhattarai, 2014)`, `(Shrestha &Subedi
    2014)`, `(Thapa & Rana, 2013)`
  - `1.2 Statement of Problem` — 3 paragraphs + 2 roman-numbered issues (§6)
  - `1.3 Objectives of the Study` — lead-in + 2 roman items (§6)
  - `1.4 Significance of the Study` — 1 paragraph
  - `1.5   Theoretical Framework` — definitional paragraph + framework figure + `Source:` line
  - `1.6 Limitations of the Study` — lead-in + 5 decimal items
  - `1.7 Organization of the Study` — `The study is divided into five chapters.` + one
    `Chapter – X: Title` + one description paragraph per chapter (5 chapters)
- **CHAPTER- II / REVIEW OF LITERATURE** (explicit break)
  - 3 opening paragraphs (definition of review of literature → approach → topic link)
  - `2.1 Conceptual Review` — intro paragraph
    - `2.1.1 Sock Prices` … `2.1.7 Return on assets` — history/definition + citations per concept
      (NEPSE history, determinants, EPS, DPS, P/E, BVPS, ROA)
  - `2.2 Empirical Review` — one paragraph per study (Sharma 2011 → Pradhan 2017),
    then **Table 2.1 meta table** (S.N./Author/Objective/Major Findings, 8 studies)
  - `2.3 Research Gap` — 1 paragraph
- **CHAPTER- III / RESEARCH METHODOLOGY** (explicit break)
  - Intro paragraph (definition of methodology)
  - `3.1 Research Design` — 2 paragraphs (descriptive + causal-comparative)
  - `3.2 Sampling Procedure` — 1 sentence (5 banks, convenient sampling, 2068/69–2075/76) +
    5 decimal-listed bank names
  - `3.3 Nature and Sources of Data` — 1 paragraph (secondary data sources)
  - `3.4 Method of Data Analysis` — 1 paragraph (descriptive/correlation/regression, SPSS 23)
    - `3.4.1 Model Specification` — intro + `Model ` + Eq. (1) + `Variables and their
      measurement` + pointer + **Table 3.2**
  - `3.5 Analysis Plan` — 1 paragraph (analysis steps)
  - `3.6 Research Hypothesis and Selection of Proxy Variable` — lead-in + 5 variable blocks
    (§10)
- **CHAPTER-IV / PRESENTATION AND ANALYSIS OF DATA** (no explicit break — add one when
  replicating)
  - Intro paragraph (5-section map of the chapter)
  - `4.1 Financial Indicator Tools` → `4.1.1 Earning per share` … `4.1.5 Book Value Per Share`
    + misnumbered `4.6 Market price per share` (should be 4.1.6) — **per-variable block:**
      1. narrative referencing the table (`The earning per share for the period … has been
         presented in table. Table 4.1 shows that …`)
      2. caption `Table no. 4.1: …` (12 bold) + table + `Source:` line
      3. 2–4 more narrative paragraphs (within-bank ranges, SD commentary)
      4. bold caption `Figure 4.1 shows average …` + chart + interpretation paragraph
  - `4.2 Correlation Analysis` — lead-in paragraph + **Table 4.8** (SPSS Pearson matrix) +
    interpretation paragraph
  - `4.3 Regression Analysis` → `4.3.1`–`4.3.5` one block per variable:
      1. SPSS tables (Model Summary / ANOVA / Coefficients) — pasted, `Normal Table`
      2. hypothesis-decision paragraph: `Since the p value (0.042) of t- statistic is less than
         0.05, there is no ground to accept the null hypothesis. Therefore, the alternative
         hypothesis is accepted i.e., … significant at 0.05 level of significance.`
      3. bold `Model Interpretation of <var> in relation to Market per share`
      4. flat equation lines: `y = a+bx` → `<VAR> = constant + slope x` → `EPS = 666.522+(-8.472)
         EPS` → `P-value = (0.042)` → `R = .324    R2 = .105`
      5. two interpretation sentences (slope meaning; R² meaning)
    - `4.3.6 Overall Regression Analysis` — same pattern with 5-predictor equation
  - `4.4 Major Findings of the Study` — 13 **bullet** items (p-value decisions + R² + descriptive
    means)
- **CHAPTER –V / SUMMARY, CONCLUSION AND RECOMMENDATIONS** (no explicit break — add one)
  - `5.1 Summary` — 2 paragraphs (chapter plan recap + data/tools recap)
  - `5.2 Conclusion` — 2 justified paragraphs (relationship summary + usefulness)
  - `5.3 Recommendation` — lead-in + 5 **bullet** items (future-variable, longer panel, other
    industries, bigger sample, more research)
- **BIBLIOGRAPHY** (explicit break) — §11

Statistical narrative conventions to reuse: highest/lowest rankings with values in parentheses
(`highest for NIBL (33.03 rupees), followed by HBL (29.54 rupees) & lowest for the KBL (15.27
rupees)`), explicit trend sentences (`has decreased to X in <year> from Y in <year>`), SD
commentary (`The variation … as indicated by SD is lowest for … followed by … However, the
highest SD … is for …`).

## 15. Reference defects — replicate the intent, not the bug

1. `4.6 Market price per share` — should be `4.1.6` (breaks numbering under 4.1).
2. `Table 3.2` with no `Table 3.1` in the document.
3. `2.1.1 Sock Prices` — typo for "Stock Prices".
4. Chapter labels inconsistent: `CHAPTER-IV` (no space), `CHAPTER –V` (en dash).
5. Caption inconsistency: `Table no. 4.1` vs `Table 4.1` vs `Table 4.7:`.
6. Figure 4.5 caption says "average **return on assets**" (copy-paste; it is BVPS).
7. H1 missing terminal period; H2–H5 have it.
8. No page break before CHAPTER-IV and CHAPTER-V; stray breaks before Table 2.1 and Figure 4.2.
9. Duplicate figure caption lines (above AND below some charts).
10. `Figure 4.2` narrative: "increases in year 2072/73" conflicts with its own table ordering —
    verify any number before reusing.
11. Bibliography incomplete vs in-text (§11) and `Thapa & Rana` year mismatch (2013 vs 2011).
12. Section 1.1 heading is a live auto-list (`numId 1`) while 1.2–1.7 are typed text —
    mixing auto/manual numbering breaks if headings move.
13. Equations use flat `β1` (no subscripts) and manually padded ellipses instead of tab stops.
14. Correlation narrative in 4.2 states an internally inconsistent reading of negative
    coefficients — do not copy the reasoning, copy only the reporting structure.

## 16. Not present in these files (must come from elsewhere)

- Preliminary/prefatory pages: approval sheet, declaration, acknowledgement, abstract,
  **table of contents, list of tables, list of figures** — Main Part starts directly at
  `CHAPTER- I`. For these, follow FOM 2019 (roman ii, iii… bottom-center; 1.5 spacing in TOC
  per guideline line 771) and our existing `docs/format/PROPOSAL_FORMAT_SPEC.md`.
- Appendices, charts list, vita — absent.
