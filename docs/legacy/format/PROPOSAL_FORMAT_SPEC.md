# Proposal format — verified spec

**Status: Format A (FOM 2019, i–vii) is correct and is the ONLY authoritative
proposal format. Format B was investigated and rejected — see below.**

## Verification of provenance

The file `TU_FOM_Master_Dissertation_Guideline_2019.pdf` in this folder was
confirmed to be Tribhuvan University's own published copy:

```
Source : https://portal.tu.edu.np/downloads/Managementresearachcommittee_2026_04_29_17_20_02.pdf
SHA256 : 9D9ACA09586D0373D8221466AF03B4E36FFD14637901115CBE01CE62E943B446
Size   : 869437 bytes  (byte-identical to our copy)
Date   : upload dated 29 April 2026 -> currently in force
```

## Files in this folder

| File | Status |
|---|---|
| `TU_FOM_Master_Dissertation_Guideline_2019.pdf` / `.txt` | **Authoritative** — TU portal copy of the FOM 2019 guideline |
| `TU_PORTAL_FOM_Dissertation_Guidelines_2019.pdf` | Duplicate download of the same file, kept as provenance proof |
| `LBC_MBS_Dissertation_Guidelines.pdf` / `.txt` | LBC's **thesis** guideline. Contains **no proposal format** — only a "Proposal Defended Date" field. Useful later for the full thesis. |
| `LBC_Notice_Master_Level_Proposal_Writing_2026.webp` | Workshop announcement only. Not a format document. |

---

## The authoritative proposal structure

From pp. 8–9 of the FOM 2019 guideline. **Approximate length 8–12 pages.**

```
i.    Background of the study
ii.   Problem statement
iii.  Objectives of the study
iv.   Hypothesis (if any)
v.    Rationale of the study
vi.   Brief review of the literature
vii.  Research methodology
        1.1.1  Research design
        1.1.2  Population and sampling procedure
        1.1.3  Nature and sources of data collection
        1.1.4  Research framework and definition of variables
        1.1.5  Methods of analysis
References
```

> Supplied as roman numerals i–vii in the source document; methodology
> sub-parts given as `1.1.1`–`1.1.5`.

**Escape hatch:** the guideline states that sections within a chapter "may be
altered/ added/ or deleted upon the advice of the supervisor; but that must be
justified by the need of the study." Extra sections are permitted only if the
supervisor asks for them.

### Title rules

- Reflect the main idea; concise, incorporating the variables and their relationship
- Example of a good title: *"Credit Risk and Profitability of Commercial Banks in Nepal."*
- Avoid abbreviations and verbose openers: "A Study of …", "An Investigation into …",
  "An Understanding of …"
- Limit to **12 words**

### Typography (pp. 20–21)

| Item | Requirement |
|---|---|
| Page | A4 |
| Spacing | 1.5 |
| Margins | top 2.54 cm, bottom 2.54 cm, right 2.54 cm, **left 3.18 cm** |
| Font | Times New Roman 12 pt |
| Sidedness | Print on one side, **recto (right-odd) pages only** |
| Body page numbers | Arabic, **top right** |
| Front matter page numbers | lowercase Roman, **bottom centre** |
| Title page | counted but unnumbered |
| References | **APA sixth edition** (explicit in Ch. I and Appendix C — NOT 7th) |

---

## REJECTED: "Format B" (numbered 1.1–1.12)

Circulates as `Scribd document 521152228 "MBS-Proposal-Format"`.

**Verdict: a single student's submitted proposal, not a format template.**

Evidence against it:

1. The uploader is **"Anish Shrestha"**, an individual — not LBC, not TU, not FOM.
2. Its own description reads: *"This document contains a proposal **submitted**
   for a Master of Business Studies degree."* A submission, not a guideline.
3. LBC's own published PDF contains **no proposal structure whatsoever**, so it
   cannot corroborate B.
4. The earlier cover-page-wording argument proves nothing — every FOM proposal
   carries "Submitted to the Office of the Dean, Faculty of Management."
5. The numbering jumps 1.7 → 1.9 with no 1.8, a tell that it is a personal
   document rather than a maintained template.

Rejected structure, recorded so we do not re-investigate it:

```
1.1 Background of the Study
1.2 Problem Statement and Research Questions
1.3 Objectives of the Study
1.4 Significance of the Study
1.5 Literature Review (1.5.1 Conceptual Review, 1.5.2 Empirical Review)
1.6 Theoretical Framework
1.7 Hypothesis
1.9 Research Methodology (1.9.1–1.9.7)     <-- no 1.8
1.10 Limitation of the study
1.11 Organization of the study
1.12 Time Frame
```

Typography in B (1.5" left, 1.5" top, page numbers bottom-centre) also
contradicts the FOM guideline's 3.18 cm left, 2.54 cm top, page numbers top-right.
B reflects pre-2019 practice.

---

## Impact on existing work

All compliance gaps are fixed as of 2026-09-30 (build: 0 errors, 6 pages):

- `src/proposal/main.tex` — `article` class, flat sections numbered **i–vii**
  via `\thesection = \roman{section}`; methodology sub-heads printed **1.1.1–1.1.5**
  verbatim via `\msub` (they do not nest under vii in the guideline either).
- `src/proposal/sections/{01..07}_*/` — one dir per section, following the
  `index_name/index_name.tex` convention. Old `chapters/` layout **deleted**.
- Margins: `geometry{top=2.54cm,bottom=2.54cm,right=2.54cm,left=3.18cm}`.
- Body page numbers Arabic **top right** (`fancyhdr`); title page counted but
  unnumbered, so body starts at page **2**.
  - Gotcha found and fixed: `\thispagestyle{empty}` must live INSIDE
    `front/titlepage.tex` (before its page break), not after `\input`, or it
    blanks page 2's number.
- Font `newtxtext`/`newtxmath` (Times-like for pdflatex), 1.5 spacing via `\onehalfspacing`.
- References: **`apacite` + `natbibapa` (APA 6th)**; apacite prints its own
  heading, so no manual `\section*{References}` (that caused a duplicate).
- Lit-review sub-heads carry **no numbers** (custom `\titleformat` with empty
  labels); the `vi.1.1` leakage from default article numbering is gone.
- Verified via `pdftotext -layout`: headings i–vii, 1.1.1–1.1.5, equation,
  tables labelled Table 1/2, figure Fig. 1, single "References", pages numbered 2–6.

## Still open

- Final 5 banks and FY observation period (placeholder 2076/77–2081/82).
- Confirm FY 2081/82 annual reports exist before locking the period.