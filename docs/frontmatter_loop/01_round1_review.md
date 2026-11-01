# Front-matter loop — Round 1 review

Scope: pages before Chapter I only — title page, Certification of
Authorship, Report of Research Committee, Approval Sheet,
Acknowledgements, Table of Contents, List of Tables, List of Figures,
List of Abbreviations, Abstract. Chapters, references, and appendices
are out of scope for this phase and were not changed.

Standard: TU FOM "Master's Degree Dissertation Guidelines- 2019",
Chapter III prefatory order (p. 9) and Appendix B templates (pp. 23-26),
plus Paper and Typography (pp. 20-21): A4, margins 2.54/2.54/2.54/3.18 cm,
Times New Roman 12 pt, 1.5 spacing, 10 pt paragraph gap, front matter
Roman bottom-centre with title counted as i and unprinted, body Arabic
top-right from Chapter I page 1. Where the instructions file
(docs/instructions) disagrees with FOM 2019, FOM 2019 governs, because
it is the university document. Two such disagreements are recorded
below as resolved, not as defects.

## Passes (all checked, each page, each line)

- P1 Order and presence against FOM p. 9.
- P2 Each page's wording against its FOM Appendix B template.
- P3 Heading size, heading gap, paragraph gap, signature rules.
- P4 Single-page fit, estimated from A4 text height (29.70 − 2.54 − 2.54
  = 24.62 cm), 12 pt at 1.5 spacing (≈ 0.635 cm per line), plus stated gaps.
- P5 Abbreviations list against actual use in the printed thesis
  (chapters, appendices, front matter; abbreviations.tex itself excluded
  from the use count, so it cannot count itself as use).

## Defects found (Round 1)

### R1-1. Heading gaps are inconsistent across front pages.
- authorship.tex, research_committee.tex, approval_sheet.tex: 1.5 cm
  after the heading.
- acknowledgements.tex: 0.2 cm. abstract.tex: 0.1 cm.
- abbreviations.tex: 0.8 cm (kept, see R1-5).
A reader turning front pages sees headings jump up and down for no
reason. Acknowledgements (≈ 291 words) and abstract (≈ 350 words, two
paragraphs) both fit on one page even with a 1.5 cm gap (estimated
≈ 20 cm and ≈ 21 cm of the 24.62 cm text height), so the small gaps
have no fit justification. Fix: set both to 1.5 cm.

### R1-2. Paragraph gaps are inconsistent across front pages.
- Global setting (config/preamble.tex, and instructions §9.1): 10 pt.
- acknowledgements.tex and abstract.tex set a local 3 pt paragraph gap.
Every other front page inherits 10 pt. Fix: delete the two local
3 pt settings so all front pages inherit 10 pt. Fit impact is under
0.4 cm on each page; both pages still fit on one page.

### R1-3. Research Committee signature rules are different lengths.
- research_committee.tex: supervisor rows use a 7.5 cm rule, the Head
  of Research Committee row uses a 5.5 cm rule. All rules start at the
  same column, so their right edges differ by 2.0 cm on the same form.
Fix: make the Head row 7.5 cm as well. Total width (longest label +
7.5 cm) stays inside the 15.28 cm text width. The date rules below
(4.5 / 5.5 / 5.8 cm) are intentionally graduated because their labels
differ in length, so their right edges roughly align; they are not
changed.

### R1-4. Abbreviations list does not match actual use.
Used in the printed thesis but missing from the list:
- NPR (Nepalese Rupees) — used throughout chapters and tables.
- BOK (Bank of Kathmandu Limited) — Chapter III, "Bank of Kathmandu
  Limited (BOK)".
- NCC (Nepal Credit and Commerce Bank) — Chapters I, III, V, "NCC Bank".
- GDP (Gross Domestic Product) — Chapter II literature summaries.
- CAR (Capital Adequacy Ratio), CRR (Cash Reserve Ratio) — Chapter II,
  Niraula summary, both spelled out there and used as acronyms.
In the list but never used in the printed thesis (excluding the list
itself and code comments):
- CBS, CCyB, MIS, PPA, SGM, TOC, FOM, TU.
  (AQR is kept: Chapter V uses "asset quality reviews (AQRs)". BFI is
  kept: Chapter I uses "BFIs". MBS is kept: Approval Sheet and
  Acknowledgements use "(MBS)". MPS with superscript RD is kept: it is
  the thesis's own price notation, used throughout.)
Wrong expansion in the list:
- BFI reads "Banking and Financial Institution" (singular). The text
  uses the plural form, and the standard expansion is plural.
Fix: add the six missing entries, delete the eight unused entries,
correct BFI to plural, and re-alphabetise. Net list: 50 → 48 entries.
P/E is placed before PEAD (shorter form first, ignoring the slash),
and NCC is placed after NAV and before NEPSE (second letter C < E).

### R1-5. Abbreviations page fit is borderline (risk, not yet a defect).
At 50 single-spaced rows, the list was estimated at ≈ 23.0 cm of rows
plus heading and 0.8 cm gap ≈ 24.4 cm, against a 24.62 cm text height —
about one row of headroom. The R1-4 net reduction of two rows gives
≈ 0.85 cm more headroom. The 0.8 cm heading gap is therefore kept and
documented in the file as fit-driven, so a later reviewer does not
"standardise" it to 1.5 cm and push the list onto a second page. The
repeated longtable header is already present, so even a spill would
still be readable; the goal remains one page. Final fit must be
confirmed by an actual compile, not by this estimate.

## Passes (no defect — recorded so Round 2 does not re-open them)

- P-1 Front-matter order in main.tex matches FOM p. 9 exactly: Title,
  Certification, Research Committee, Approval, Acknowledgements, TOC,
  LOT, LOF, Abbreviations, Abstract.
- P-2 Title page matches the FOM Appendix B template: title, submission
  sentence, "by", name, roll, registration, campus, date at the foot
  via vfill. Title at 16 pt against 14 pt chapter headings is a
  hierarchy (title larger than chapter), not a defect.
- P-3 Authorship wording matches the FOM template word for word,
  including its own "nor it has been proposed" phrasing, which is not
  "corrected" because the template itself says it.
- P-4 Research Committee and Approval Sheet wording match their FOM
  templates in substance; the Approval Sheet's 2×2 signatory grid
  contains all four FOM signatories with the same line/title/Signature
  pattern, so it is kept (FOM shows a vertical example, it does not
  require a vertical layout).
- P-5 Abstract: two paragraphs, ≈ 350 words, under one page, exactly
  five keywords (Value Relevance, Commercial Banks, Bank Consolidation,
  Ohlson Model, Two-Way Fixed Effects). Its Model 1 / Model 2 / R6
  numbers match the verified Chapter IV values.
- P-6 Pagination: title counted as i and unprinted (titlepage
  environment + empty style), front matter Roman bottom-centre from
  page ii, body Arabic top-right from Chapter I page 1. Front pages
  use plain style while frontmatter is active, so they render Roman
  bottom-centre as required.
- P-7 TOC / LOT / LOF are single-spaced, as FOM requires for lists.
- P-8 Acknowledgements prose is not rewritten in a format phase; only
  its spacing is fixed (R1-1, R1-2).

## Resolved, not defects (FOM governs over the instructions file)

- X-1 Instructions §9.3 lists "Report of Viva-Voce Committee" and
  "Declaration of Authenticity". FOM p. 9 lists "Report of Research
  Committee" and no separate Declaration; Certification of Authorship
  is FOM's declaration page. The thesis follows FOM: no page is added,
  nothing is renamed. This closes loop open item O1 on FOM's own list.
- X-2 Instructions §9.3 requires each preliminary section to be
  "strictly single page". FOM itself requires the abstract to be
  limited to one page (p. 9) and gives no such blanket rule for every
  preliminary section. The loop therefore treats one page as the goal
  for every front page, and as a hard requirement only for the
  abstract. A spill in TOC/LOT/LOF (which grow with the document) would
  not be a format violation; a spill in a form page or the abstract
  would be.

## Items for the user / campus to confirm (not fixable from sources)

- U-1 Supervisor name: the FOM Research Committee template includes
  the supervisor's name inside its opening sentence ("guidance of
  supervisor …"). The thesis sentence omits a name because no name is
  given anywhere in the sources; the signature block is blank for
  handwriting. Do not invent a name. If the campus wants the name
  printed, supply it and it will be inserted in both places.
- U-2 Title-page submitting name (Asmita Subedi) remains unconfirmed,
  as before. It is not changed by this loop.

## Round 1 fix list (to implement next)

R1-1, R1-2, R1-3, R1-4. Nothing else.
