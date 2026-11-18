# Verification review of the thesis issue audit (v1)

**Review date:** 18 November 2026
**Repo:** `~/workspace/verbose-chainsaw`, HEAD `10d85d8` ("docs: add thesis issue audit and remediation plan for v1")
**Audit reviewed:** `issues/v1/issues.md` (7 issues, I-01..I-07). **Plan reviewed:** `issues/v1/plan.md` (3 phases, 10 steps, priority order, exit criteria).
**Method:** One dedicated verifier per issue (seven verifiers, each working only its own issue), plus independent verification by the coordinator of the consequential verdicts: the coordinator re-ran the I-05 reproduction from scratch with two independent implementations, extracted the KBL reporting-date table and the GBIME largest-bank passages from the local PDFs, opened the Kumari PDF and the Sharma full text itself, and re-grepped the thesis for the key claims. The thesis source (`src/thesis/`) is unchanged by the recent pull (verified: `git diff a6cfb64..HEAD -- src/thesis/` is empty). No thesis, code, data, config, `issues.md`, or `plan.md` file was modified. The only file created by this review is this one (`issues/v1/review.md`).
**Verdict vocabulary:** CONFIRMED (the issue is real and accurate as stated) / CORRECTED (real but partly wrong — what is actually true is stated) / REFUTED (the claim is false, hallucinated, or unsupported).

## Summary

| Issue | Verdict |
|---|---|
| I-01 Prabhu exclusion reason | CONFIRMED (with qualifications) |
| I-02 SEBON/MoF source bullets | CONFIRMED |
| I-03 Kumari SGM document title | CORRECTED |
| I-04 Candidate identifiers and location | CONFIRMED |
| I-05 R9 / KBL FY 2076/77 timing sensitivity | CORRECTED |
| I-06 Sharma (2011) DPS sign | CORRECTED |
| I-07 GBIME 16th AGM minutes | CONFIRMED (with qualification) |

**Tally: 4 CONFIRMED, 3 CORRECTED, 0 REFUTED.** No issue was hallucinated. Every issue is real. The three corrections are: I-03 (the exact cover wording *is* recoverable, and it says "Special", not "Extraordinary"); I-05 (the headline numbers reproduce exactly, but the FY-end date, the day-count, and the Deva-date attribution are wrong); I-06 (the DPS-sign question is now resolved in the thesis's favour by the full text, but the proposed bibliography correction is wrong, and a BVPS nuance in the same sentence is real).

**Plan verdict:** 8 of 10 steps CORRECT (steps 1, 2, 4, 5, 7, 8, 9, 10); 2 NEEDS CHANGE (step 3 — the "four-day" window is three days; step 6 — the bibliography correction is wrong and the DPS question is now resolved, while a BVPS nuance is unaddressed). Priority order CORRECT. Exit criteria CORRECT, with one separate repo-health item noted (the deleted root `pytest.ini` — out of scope for the plan's issue list, but it must be restored before step 9 so the pipeline can be test-verified).

---

## I-01 — Prabhu Bank exclusion reason — CONFIRMED (with qualifications)

**What the thesis says.** `src/thesis/chapters/chapter_03_research_methodology.tex:31` (the whole of §3.3 was read):

> "From the total population of 20 licensed commercial banks, a purposive (judgmental) sample of five commercial bank series is selected. … these five institutions comprise four of the five Class `A' commercial bank combinations executed during the early-2023 wave (the fifth, Prabhu Bank's acquisition of Century Commercial Bank \citep{nrb2023bsr}, is not sampled) alongside an unmerged private commercial bank benchmark…"

The four selection criteria that follow (lines ~33–40) are: (1) participation in the 2023 consolidation wave (joint operations Jan–Feb 2023); (2) benchmark-series continuity (unmerged bank); (3) complete audited annual statements FY 2076/77–FY 2081/82 under NFRS; (4) active NEPSE listing with trading freshness. None of these criteria, as written, excludes Prabhu, and no sentence in §3.3 says why Prabhu fails any of them.

**Whole-thesis grep.** `grep -rn -i "prabhu\|century" src/thesis/` returns exactly **two** hits (independently re-run by the coordinator):
- `src/thesis/chapters/chapter_01_introduction.tex:30` — "Prabhu Bank acquired Century Commercial Bank (10 January 2023)" (in the list of the five combinations).
- `src/thesis/chapters/chapter_03_research_methodology.tex:31` — quoted above.

No hit in the front matter, appendices, config, or `references.bib`. **No passage anywhere in the thesis states a reason for the exclusion** — not data quality, continuity, comparability, or anything else.

**NRB Bank Supervision Report 2024.** Opened by the I-01 verifier (crawled 2026-11-18 14:28 UTC): the document is titled "Bank Supervision Report, 2023/2024", Kathmandu, March 2025. Table 4, "List of Commercial banks in Nepal" (p. 4): "18 Prabhu Bank Ltd. **2023/01/10\*** Babarmahal, Kathmandu", footnote (p. 5): "*Joint operation date after merger/acquisition." Text (p. 6): "…Century Commercial Bank Ltd. merged with Prabhu Bank Ltd.…". The coordinator's own retry of the same URL failed at the tool level ("browser.open requires a resolvable public HTTP(S) URL") — a tool failure, not a source failure — so the NRB Table 4 evidence in this review rests on the verifier's successful open, stated honestly here.

**Qualifications (do not change the verdict):**
1. The NRB report's verb for this pair is **"merged with"**, not "acquired by" (it reserves "was acquired by" for Civil→HBL). The direction is unambiguous — Prabhu is the surviving bank listed with the joint-operation date — so "Century as the acquired/absorbed bank" is a fair paraphrase, but the report itself does not use the word "acquired" for this pair.
2. The Prabhu Bank 22nd Annual Report PDF could **not** be opened (fetch timeout). The 10 January 2023 start is corroborated by NRB plus independent sources (ShareSansar, 10 Jan 2023; CARE Ratings Nepal), but the annual report itself was not directly verified. The issue's limb "Prabhu's own annual report likewise says…" is therefore indirectly corroborated, not directly verified.
3. Prabhu's FY 2076/77 audited annual report was not directly sighted (FY 2077/78–2081/82 audited confirmed via a secondary source). No evidence of a gap was found, and the thesis never claims a data-availability gap for Prabhu.
4. Prabhu is NEPSE-listed (the thesis itself states at Ch3:28 that of the 20 licensed institutions, 19 are listed and the one unlisted institution is Rastriya Banijya Bank — so by the thesis's own population claim, Prabhu is listed). `data/reports/` contains exactly five bank directories (GBIME, HBL, KBL, NIMB, NMB) — no Prabhu report was ever collected, but the absence of a local file is not itself a reason for exclusion.

**Sharpening detail (from the verifier, confirmed in the thesis):** `chapter_02_literature_review.tex:395` says the wave altered reporting "across five major merged institutions" while the thesis samples four, with no explanation of the difference; and Ch2:202–211 (§2.1, "The 2022–2023 Consolidation Wave") names only the four sampled merged banks plus NMB — Prabhu is not even named as omitted there.

**Verdict: CONFIRMED.** The issue is real and accurate as stated. The thesis names Prabhu–Century as the omitted fifth combination and gives no reason for the omission anywhere; the shared criteria do not on their face distinguish Prabhu.

---

## I-02 — Chapter III SEBON/MoF source bullets — CONFIRMED

**The bullets.** `src/thesis/chapters/chapter_03_research_methodology.tex:157–162` (read in full by the coordinator):

- Line 157: `\textbf{Contextual and Regulatory Data Sources:}`
- Line 159: `\item \textit{Nepal Rastra Bank (NRB):} Annual Banking and Financial Statistics and licensed financial institution directories … and the Bank and Financial Institutions Merger Bylaws …`
- Line 160: `\item \textit{Securities Board of Nepal (SEBON):} Annual reports, Capital Market Trends publications, and corporate disclosure directives.`
- Line 161: `\item \textit{Ministry of Finance (MoF), Government of Nepal:} \textit{Economic Survey} publications (FY 2076/77 through FY 2081/82).`

They sit under §3.4.2 "Sources of Data Collection" inside a section that calls them "data sources" — so "presented as sources used, not merely possible sources" is a fair reading. (Precision: the issue's "lines 157–162" range is accurate — 157 is the heading, 160–161 the two bullets, 162 `\end{itemize}`.) The bullets name publication *series/classes* — no specific document, year, title, or URL is named for SEBON or MoF.

**Bibliography.** `src/thesis/references.bib` (75 entries): case-insensitive greps for `sebon`, `ministry of finance`, `economic survey`, `capital market trends`, `MoF`, `securities board`, `survey`, `ministry` returned **zero hits** (independently re-run by the coordinator). The only "capital market" hit is Fama (1970), unrelated. Contrast: the NRB bullet *does* have bibliography entries (`nrb2013stats`, `nrb2023bsr`, `nrb2023list`, `nrb2011`, `nrb2015`) and is cited in Chapter I — the SEBON/MoF gap is specific, not a general pattern.

**All-chapter grep.** "Economic Survey": exactly one hit thesis-wide — the Ch3:161 bullet itself. "Ministry of Finance" / "MoF": exactly one hit — the same bullet. "SEBON" hits are all mentions, never a direct SEBON citation: Ch1:11 (formation/history cited to `\citep{nepse2017}`, a NEPSE publication), Ch1:161 and Ch1:207 (no citation), Ch2:177–180 (cited to `nepse2017`), Ch3:160 (the bullet), Ch5:10, 186, 194–198, 231 (no SEBON citation; line 197 cites `bafia2017`), `front/abbreviations.tex:112` (glossary), `front/acknowledgements.tex:20` (see below). Appendices: zero hits.

**Market-capitalization statistic.** `chapter_01_introduction.tex:11` (confirmed by the coordinator): "NEPSE is heavily dominated by the banking and financial institutions (BFIs) sector, with Class 'A' commercial banks accounting for more than 30\% of total market capitalization \citep{gurungdahal2025}." The same sentence with the same attribution recurs at `chapter_05_summary_and_conclusion.tex:19`. These are the only two occurrences of the ">30%" figure.

**Gurung & Dahal (2025).** Opened by the I-02 verifier (TU portal PDF, crawled 2026-11-18 13:28 UTC): it states the figure — "In the context of Nepal, commercial banking sector has significant dominance in the country's capital market with more than 30% of the total market capitalization representing from this sector alone (SEBON, 2023)" — and its reference list contains exactly "SEBON. (2023). Annual Report." — no fuller title, no fiscal year, no URL, no table number. **Precision added by this review:** the thesis does not identify the specific SEBON document, *and neither does its secondary source* — so retrieving the underlying SEBON table requires first identifying which annual report/table "SEBON. (2023). Annual Report." refers to.

**Source register and local copies.** `data_analysis/data_extract/output/audit/source_register.md` and `source_register.csv` (31 lines = header + 30 rows): zero hits for SEBON/MoF/Economic Survey/Capital Market Trends. Filename search across the repo returned nothing; `data/reports/` contains only the five bank directories. No SEBON or MoF publication copies exist in the repo.

**Acknowledgements.** `src/thesis/front/acknowledgements.tex:20`: "I am profoundly indebted to Nepal Rastra Bank (NRB), the Securities Board of Nepal (SEBON), and the Nepal Stock Exchange (NEPSE) for maintaining publicly accessible regulatory reports and trading archives." This thanks SEBON for *maintaining* publicly accessible reports — it implies the author drew on SEBON's publicly accessible reports but names no specific document. MoF is not mentioned anywhere in the acknowledgements or front matter.

**Verdict: CONFIRMED.** Every limb verified. This is a substantiated provenance/overstatement risk, not proof the author never consulted those sources (absence from the bibliography/register/repo proves no *documented* use, not no use).

---

## I-03 — Kumari SGM document title — CORRECTED

**Bibliography entry (exact).** `src/thesis/references.bib:296–302` (confirmed by the coordinator):

```bibtex
@misc{kumari2022sgm,
  author       = {{Kumari Bank Limited}},
  title        = {Extraordinary general meeting document, FY 2079/80 (merger proposals and share swap ratio)},
  year         = {2022},
  howpublished = {Official bank filing},
  url          = {https://backend.kumaribank.com/storage/agm-report/2022/12/1670847430_Extra_Ordinary_General_Meeting_2079-08-25_Kumari_Bank_Ltd..pdf}
}
```

**The PDF.** Opened by the I-03 verifier (`browser.open` retrieved it directly; 895 lines, crawled 2026-11-18 14:28 UTC) and independently opened by the coordinator (same 895-line extraction). The coordinator's own fetch confirms: the document is a scanned meeting record (the text layer is garbled Devanagari OCR), and "(Share Swap Ratio) 1:1" appears 3× (browser lines L117, L481, L502). The verifier additionally downloaded the file (486,454 bytes, SHA-256 `2bff67f88fba70f190bed4f758c1d59e657d9d9ad717407fe530f89559f2a81d`, Creator: Canon, CreationDate 2022-12-12) and rendered and visually read all 11 pages; `pdfinfo` confirms **Pages: 11**. `pdfimages -list` shows every page is a single full-page CCITT grayscale scan (~1678×2348 @200 dpi); `pdftotext` on p. 1 yields only 158 characters of garbled OCR.

**Contents verified (from the verifier's visual reading, cross-checked by the coordinator's text fetch where the text layer permits):**
- Meeting date **2079/08/25**: cover "२०७९/०८/२५"; p. 2 §1: "मिति : २०७९ साल मंसिर महिना २५ गते आइतबार (तदनुसार ११ डिसेम्बर २०२२)" — 25 Mangsir 2079, Sunday, 11 December 2022, 1:00 PM, Kumari Bank Ltd., Naxal office, Kathmandu.
- Numbered agenda/resolution sections: p. 2 §3, "क. विशेष प्रस्ताव" items (1)–(7); pp. 6–7 §12 gives proposals and passed resolutions (1)–(7); quorum 58.84% (p. 3); p. 11 §14 adjourns at 3:00 PM, signed by Ashwin Babu Shrestha (Company Secretary) and Amir Pratap J. B. Rana (Chairman).
- Merger resolutions: p. 6 item (1) merger report re Kumari Bank + Nepal Credit and Commerce Bank — "सो प्रस्तावलाई सभाले सर्वसम्मतिले पारित गर्यो" (passed unanimously); item (2) accepting the final agreement ("अन्तिम सम्झौतापत्र") and giving final approval for the merger — passed unanimously.
- **1:1 share swap ratio, confirmed twice over:** p. 2 agenda item (4) proposes "शेयर स्वाप अनुपात (Share Swap Ratio) १:१"; pp. 6–7 resolution (4) approves it unanimously.

**The correction — exact cover wording IS recoverable.** The issue says the first page is scanned and the exact cover wording "is not recoverable from the text layer." The first half is true; the second half is true *only of the text layer*. Visually reading the rendered scan (150 dpi full page, confirmed with a 300 dpi zoom of the title block), the cover is fully legible:

> **कुमारी बैंक लि. को विशेष साधारण सभाको निर्णय विवरणहरु (माईन्यूट) २०७९/०८/२५**

i.e. "Decisions/Resolutions of the Special General Meeting of Kumari Bank Ltd. (Minutes), 2079/08/25." P. 2 repeats the heading: "श्री कुमारी बैंक लिमिटेड को विशेष साधारण सभाको निर्णय विवरण (माईन्यूट)". The seal reads "KUMARI BANK LTD. CORPORATE OFFICE" (the only English on the cover).

**Consequence: "Special" is what the cover prints (विशेष = special). "Extraordinary" (which would be असाधारण) appears nowhere in the document — only in the bank's *filename* (`Extra_Ordinary_General_Meeting_…`). The existing bib title's "Extraordinary" is therefore not just generic but the wrong word.** The issue's proposed descriptive title ("Minutes of the Special General Meeting of Kumari Bank Limited held on 2079/08/25") is a faithful English rendering of the cover, not a verbatim transcription (the cover literally says "decision details (minutes)"). The coordinator did not independently re-read the cover visually (the text fetch cannot do that), so the cover wording in this review rests on the I-03 verifier's visual reading, cross-checked for consistency against the coordinator's own text fetch (scanned document, 1:1 ratio present, meeting content consistent).

**1 January 2023 joint-operation date — independently confirmed by both sources.** Kumari Bank corporate history: "Most recently, Nepal Credit and Commerce Bank Limited merged with Kumari Bank, and the unified entity has been operating under the name Kumari Bank Limited **since January 01, 2023**." NRB Bank Supervision Report 2024, Table 4: "9 Kumari Bank Ltd. **2023/01/01\***", footnote "*Joint operation date after merger/acquisition."

**Where the thesis cites this source (only two citations).** `chapter_02_literature_review.tex:209`: "Kumari Bank Limited (KBL): Amalgamated with Nepal Credit and Commerce Bank Limited (**swap ratio 1:1**) `\citep{kumari2022sgm,kbl2023report}`; unified commercial operations commenced on 1 January 2023 `\citep{nrb2023bsr}`." `chapter_03_research_methodology.tex:65`: "Statutory horizontal amalgamation with an equity **share swap ratio of 1:1** … `\citep{kumari2022sgm}`." Citing the date to NRB rather than the minutes is correct — the meeting (11 Dec 2022) predates the merger, and the minutes contain no joint-operation date.

**Verdict: CORRECTED.** The issue is real — the bibliography title is an imprecise generic description and the document is SGM minutes recording the merger resolutions including a 1:1 ratio — but the "exact cover title pending" limb is now resolved: the cover prints "Special", not "Extraordinary", and the proposed title with "Special" is confirmed correct against the cover.

---

## I-04 — Candidate identifiers and location — CONFIRMED

**`src/thesis/config/metadata.tex`** (read in full by the coordinator; lines 17–21):
- `\newcommand{\thesisauthor}{Asmita Subedi}`
- `\newcommand{\thesisroll}{67514/24}`
- `\newcommand{\thesisregistration}{7-2-48-1060-2018}`
- `\newcommand{\thesiscampus}{Triveni International College}`
- `\newcommand{\thesisdate}{November 2026}`

Also `\thesisdegree` = `Master of Business Studies (MBS)`, `\thesisfaculty` = `Faculty of Management`. "Pokhara, Nepal" is **not** in `metadata.tex` — it is hardcoded on the title pages (the issue does not claim otherwise).

**Proposal title page** — `src/proposal/front/titlepage.tex` (lines 25–33):
- Line 25: `Asmita Subedi`
- Line 26: `Triveni International College`
- Line 27: `Exam Roll No: 67514/24`
- Line 28: `T.U. Regd. No: 7-2-48-1060-2018`
- Line 32: `Pokhara, Nepal`
- Line 33: `November 2026`

The *values* match `metadata.tex` character for character. Two label-only differences (values unaffected): the proposal labels are "Exam Roll No:" and "T.U. Regd. No:" while the thesis title page renders "Roll No:" and "Registration No:"; the proposal prints the campus name bare, with no "Campus:" label.

**Every occurrence in the thesis front matter** (repo-wide grep for `67514`, `7-2-48-1060-2018`, `Triveni`, `Pokhara`, `November 2026`): `metadata.tex:18–21` (the macros); `front/titlepage.tex:23` (`Roll No: \thesisroll`), `:24` (`Registration No: \thesisregistration`), `:25` (`Campus: \thesiscampus`), `:29` (`Pokhara, Nepal`), `:30` (`\thesisdate`); `front/acknowledgements.tex:18` (Triveni International College, no identifiers) and `:30` (sign-off "Asmita Subedi"). No identifiers appear in `approval_sheet.tex`, `authorship.tex`, or `research_committee.tex` (names only; date boxes blank), and none appear anywhere in the chapters or appendices. All occurrences are consistent — the thesis title page renders the identifiers purely through the `metadata.tex` macros, so it cannot drift from them.

**Correctness against the college/TU record — cannot be established from the repo.** Filename and content searches found no candidate registration document, affiliation letter, admit card, or enrolment record. The only hits are the TU FOM guidelines PDF (a formatting document, not a candidate record) and the bank-report source register. The identifiers occur only in `metadata.tex`, the proposal title page, and `issues.md` itself — plus one coincidental binary match: the bare number `67514` occurs twice inside `data/reports/NIMB/FY2079-80/NIMB_FY2079-80_annual_report.pdf`, a bank annual report (a financial figure, not `67514/24`, and not a candidate record). No claim is made here that the identifiers are correct or incorrect against the college/TU record.

**Date.** "November 2026" is identical in `metadata.tex:21`, `front/titlepage.tex:30`, and `src/proposal/front/titlepage.tex:33`. The other "November 2026" strings in Appendix D are data re-verification dates, not the submission date.

**Verdict: CONFIRMED.** Every limb checks out. Workspace consistency is verified; correctness against the college/TU record is not established from the repo, as the issue states.

---

## I-05 — R9 / KBL FY 2076/77 timing sensitivity — CORRECTED

**R9 as the thesis describes it — CONFIRMED (NMB-only).** `src/thesis/chapters/chapter_03_research_methodology.tex:383`:

> "R9 (Excluding Kanchan-Mismatched Bank-Year): Re-estimates Model 2 excluding the single bank-year NMB FY 2076/77 ($n = 27$, residual degrees of freedom 13) whose pre-acquisition fundamentals are paired with a post-acquisition April 2021 price following the Kanchan Development Bank acquisition, to verify results are not driven by that timing mismatch. The parallel Kumari Bank FY 2076/77 case, whose EPS is likewise on a pre-acquisition weighted-average base while its April 2021 price reflects the combined bank following the Deva Bikas Bank acquisition, is not excluded here: its joint operations began on 28 Ashad 2077 BS, **three days before the fiscal year-end**, so its year-end balance sheet, and hence BVPS, already reflects the combined bank, whereas the Kanchan acquisition closed after the fiscal year-end, leaving NMB's entire FY 2076/77 fundamentals pre-acquisition."

`data_analysis/analysis/outputs/tables/T5_robustness.md:13,15`: R9 row `-3.445 (6.598)`, `-1.741 (1.477)`, `1.79 (0.205)`, `27`. Appendix E (`appendix_e.tex:169,176,532`): R9 `-3.4454 (6.5976)`, `-1.7414 (1.4767)`, `1.794 (0.205)`, `27`, `13`; "R9 excludes NMB FY 2076/77 only". The pipeline agrees: `data_analysis/analysis/stats/robustness.py` builds R9 as `panel[~((panel["bank"] == "NMB") & (panel["fy"] == "FY2076-77"))]` — NMB only.

**Deva dates — date confirmed, but TWO ERRORS in issues.md.**

*Error A — FY-end date and day-count (issues.md is wrong; the thesis is right).* Issues.md §I-05 says "KBL FY 2076/77 closed on 16 July 2020" and "joint operation began only four days before FY-end". The reports' own reporting-date tables say the opposite, confirmed by the coordinator's own extraction from `data/reports/KBL/FY2076-77/KBL_FY2076-77_annual_report.pdf`:

> "Reporting date — Nepalese calendar Ashadh 31, 2077 / Ashadh 31, 2076; English calendar **July 15, 2020** / July 16, 2019. Reporting period — Shrawan 01, 2076 to Ashadh 31, 2077 — **July 16, 2019 to July 15, 2020**."

"July 16, 2020" occurs **0 times** in the FY 2076/77 report. 16 July 2020 is Shrawan 1, 2077 — the first day of FY 2077/78. Hence 28 Ashadh 2077 = 12 July 2020, and the gap is **3 days, not 4**. Chapter III:383's "three days before the fiscal year-end" is correct; issues.md contradicts the thesis on this point. The issue's "12 July 2020" conversion itself is correct.

The joint-operation date itself is verified from the FY 2076/77 report (PDF p. 7): "The Bank acquired Deva Bikas Bank Limited and joint operation was started from Asadh 28, 2077." (Also PDF p. 30: "In the Fiscal Year 2076/77, the Bank acquired Dev Bikas Bank and started joint business transaction from 28th Ashad, 2077 BS"; note 5.9, PDF p. 114: acquisition accounting — Consideration Transferred 4,322,826,984; Net Assets Transferred 4,234,022,943; Goodwill 88,804,041; "Deva Bikas Bank has prepared its Financials as of 28th Ashad 2077; the assets and liabilities of Deva Bikas Bank has been [merged] in the books of Kumari Bank".) EPS 12.08 verified in the SOPL ("Basic earnings per share … 12.08").

*Error B — source attribution.* Issues.md says "Kumari Bank's FY 2077/78 annual report says Deva's joint operation began on Asadh 28, 2077". The local FY 2077/78 PDF (`data/reports/KBL/FY2077-78/KBL_FY2077-78_annual_report.pdf`, 220 pp.) contains **no** legible passage stating the joint-operation start date: only 6 "Deva" hits, none with a date, and its front-matter history section extracts as legacy-encoded gibberish. The FY 2077/78 report *does* corroborate the acquisition (goodwill Rs. 88,804,041, §5.16; "Bank had acquired Deva Bikas Bank on FY 2076/77"; share capital "2,965,919,029 added from acquisition" in FY 2076/77). **The correct citation for the date is the FY 2076/77 report** (which issues.md's own "Primary-source trail" also cites correctly).

**KBL FY 2076/77 identified as influential — CONFIRMED.** Appendix E `appendix_e.tex:528`: "Table tab:app_m2flagged lists the five observations above that threshold in Model 2; the largest is KBL FY 2076/77 at 0.4902." Appendix E:575 (Model 2 flagged table): `KBL FY 2076/77 & 0.4902 & 0.5073`; :548 (Model 1): `KBL FY 2076/77 & 0.4124 & 0.3494` (threshold 4/N = 0.143). Ch4:548: "Influential Observations: Five observations exceed the 4/N Cook's-distance attention threshold." Appendix E:618 (leave-one-out note): "δ_E is … least negative when KBL FY 2076/77 is deleted (−1.3925)".

**Reproduction — CONFIRMED EXACTLY (controls match; n=26 matches the issue to 4 dp).** The coordinator independently reproduced the numbers from scratch with two implementations (the repo's frozen pipeline — `analysis.dataset.build_dataset()` on the frozen joined panel `data_analysis/data_extract/output/manual_review/mps_rd_joined_panel.csv`, `fit_model2`, `joint_zero_test`, `statsmodels==0.14.6` — and a from-scratch numpy HC3 implementation of the same Model 2 design). The two paths agree to ~1e-10 on every figure. Script: `/tmp/i05-coord/repro_i05.py` (scratch only; no repo files created). No pytest was used (the root `pytest.ini` was deleted and pytest currently fails at collection — see §"Repo health" below).

| Spec | n | K | df | δ_E (HC3 SE) | δ_B (HC3 SE) | Wald F | p | R² |
|---|---|---|---|---|---|---|---|---|
| Control R2 (stored: −3.124 (4.003), −1.758 (1.231), F 2.954, p 0.085, R² 0.978) | 28 | 14 | 14 | −3.1236865500 (4.0031440731) | −1.7579671148 (1.2306879778) | 2.9544812171 | 0.0850268049 | 0.9780777791 |
| Control R9 (stored: −3.4454 (6.5976), −1.7414 (1.4767), F 1.7942, p 0.2051) | 27 | 14 | 13 | −3.4454046974 (6.5976066891) | −1.7414064956 (1.4767149336) | 1.7941825020 | 0.2050730079 | 0.9752264885 |
| **Variant n=26** (issue claims: −0.5575 (4.7405), −1.3078 (0.8446), F 1.5699, p 0.2479) | 26 | 14 | 12 | **−0.5574529309 (4.7404935795)** | **−1.3077987409 (0.8446260512)** | **1.5699364080** | **0.2479442923** | 0.9875116636 |
| Context: drop KBL FY2076-77 only | 27 | 14 | 13 | −1.3924558340 (3.3316716897) | −1.3443233450 (0.8045238327) | 2.5917351907 | 0.1129100923 | 0.9882639699 |

Both controls reproduce the stored R2 and R9 headline coefficients and joint tests within rounding (to 4 dp exactly), so the issue's provisional numbers are trustworthy: the n=26 variant matches the issue's −0.5575 (4.7405), −1.3078 (0.8446), F(2,12)=1.5699, p=0.2479 on every digit. The earnings interaction does move materially toward zero (−3.4454 → −0.5575); the joint test remains non-significant (p 0.2051 → 0.2479). The n=26 numbers are a provisional, non-pipeline estimate (no R10 path exists in the repo's robustness script); they are arithmetically exact but not yet a saved reproducible output, as issues.md itself notes.

**Deva vs NMB/Kanchan distinction — ACCURATE IN SUBSTANCE (with the 3-day correction).** Deva: joint operation 12 July 2020, **3 days** before FY-end 15 July 2020; year-end balance sheet already reflects the combined bank (goodwill, transferred net assets, Deva financials as of 28 Ashadh merged in), while EPS sits on a pre-acquisition weighted-average base (12.08) and the 13 April 2021 price follows months of joint operation. Partial-year exposure, not a wholly pre-acquisition year. Kanchan (verified in the NMB FY 2076/77 report): "The unified banking operation post-acquisition of Kanchan Development Bank Ltd. commenced from August 23, 2020" and "the bank has also acquired Kanchan Development Bank Ltd. in the FY 2077/78" — i.e. after the FY 2076/77 close, leaving NMB's entire FY 2076/77 fundamentals pre-acquisition. The distinction the issue draws is therefore accurate; only its "four days / 16 July" arithmetic is off by one day.

**Verdict: CORRECTED.** The issue is real and its headline numbers reproduce exactly, but two factual details are wrong by the primary sources: the FY-end date (15 July 2020, not 16 July) and the day-count (3 days, not 4) — the thesis is right on both — and the Deva-date attribution (the FY 2076/77 report, not the FY 2077/78 report).

---

## I-06 — Sharma (2011) DPS sign — CORRECTED

**Primary journal article page.** Opened by the I-06 verifier: https://www.researchersworld.com/index.php/rworld/article/view/303. Title (L0): `DETERMINANTS OF EQUITY SHARE PRICES IN INDIA`. Site/journal header (L2): `| Researchers World - International Refereed Social Sciences Journal`. The extraction did not display the author, volume/issue, pages, or abstract in the returned text; those were verified from the full-text copy below plus independent citing sources.

**Full article obtained — YES (via a different route).** The issue said the source page's PDF download timed out and the full text was not obtained. The I-06 verifier obtained the complete full text via the Scribd copy found by web search (https://www.scribd.com/doc/211008004/Determinants-of-Equity-Share-Prices-in-India, 328 lines, abstract through references and annexure, page footers [51]–[60]). **The coordinator independently opened the same Scribd copy and read it**, confirming the identity and the results quoted below. Identity match: header on every page "-Journal of Arts, Science & Commerce E-ISSN 2229-4686 ISSN 2231-4172"; footer "International Refereed Research Journal … Vol. II, Issue 4, Oct. 2011 [51]" (through [60]); author line "Dr. Sanjeet Sharma Assistant Professor Department of Commerce, Govt. College Haripur (Guler), Distt. Kangra, Himachal Pradesh, India."

**Abstract (exact wording, Scribd L6–L15, confirmed by the coordinator):** "The present study has been undertaken to examine the empirical relationship between equity share prices and explanatory variables such as: book value per share, dividend per share, earning per share, price earning ratio, dividend yield, dividend payout, size in terms of sale and net worth for the period 1993-94 to 2008-09. The results revealed that earning per share, dividend per share and book value per share has significant impact on the market price of share. Further, results of study indicated that dividend per share and earning per share being the strongest determinants of market price, so the results of the present study supports liberal dividend policy and suggests companies to pay regular dividends. This policy will affect market price of share in positive direction."

**Regression / correlation results for DPS (full text, confirmed by the coordinator):**
- Correlation, Table 2 (L158–L168): DPS is `P**` (positive, significant) in **all 16 years** 1993-94 to 2008-09. Text: "dividend per share, earning per share and book value per share have a significant positive correlation with market price of share in all the years under study."
- Regression (L168–L177): "it is found that dividend per share has been emerged significant with the positive hypothesized sign in thirteen out of sixteen years period under study, i.e., 1993-94, 1995-96, 1996-97, 1997-98, 1999-00, 2000-01, 2001-02, 2002-03, 2003-04, 2005-06, 2006-07, 2007-08 and 2008-09… dividend per share has positive and significant impact on market price of share."
- Conclusion (L230–L235) repeats the abstract wording verbatim. Table 3 (L199–L203) encodes DPS as `Y` (significant) in 13 of 16 years and `N` in 1994-95, 1998-99, 2005-06 — consistent with the text. Note: Table 3 shows only significance codes (Y/N with */**), **no numeric coefficient values**, so no DPS coefficient magnitude can be quoted; sign and significance are what the text states explicitly.

**Therefore: no DPS sign conflict exists in the full text.** The proposed "sign conflict" concern is refuted for DPS — the full text affirmatively supports a positive, significant DPS association.

**Thesis sentences about Sharma.** `src/thesis/chapters/chapter_02_literature_review.tex:228` (confirmed by the coordinator): "In emerging Asian equity markets, \citet{sharma2011} investigated the empirical relationship between accounting fundamentals and equity share prices across different industry groups in India over 1993/94 to 2008/09. The study found that earnings per share (EPS), book value per share (BVPS), and dividend per share (DPS) exhibited statistically significant positive associations with share prices, with EPS and DPS the strongest determinants." Table 2.1 synthesis row, `chapter_02_literature_review.tex:326`: "EPS, BVPS, and DPS exhibit significant positive associations with equity prices." Both characterize the DPS finding as **positive** — and the full text supports that characterisation for DPS. All Sharma mentions thesis-wide: Ch1:9 (bare citation), Ch2:228, Ch2:297 (P/E-circularity list), Ch2:306 (benchmark), Ch2:326 (Table 2.1), Ch2:398 (P/E list), `references.bib:11–19`. No Sharma mention exists in Chapters III, IV, or V.

**Bibliography entry — the issue's correction is WRONG.** `src/thesis/references.bib:11–19` (confirmed by the coordinator):

```bibtex
@article{sharma2011,
  author = {Sharma, S.},
  title = {Determinants of equity share prices in India},
  journal = {Journal of Arts, Science and Commerce},
  volume = {2},
  number = {4},
  pages = {51--60},
  year = {2011}
}
```

The issue claims the primary page gives the journal as "Researchers World - International Refereed Social Sciences Journal" and its correction route says "Update the journal field to the primary source's journal name." That is **incorrect**:
- The article itself prints its journal as **Journal of Arts, Science & Commerce** (header on every page, ISSN 2231-4172) — confirmed by the coordinator's own reading of the full text.
- The journal's full name is **Researchers World – Journal of Arts, Science and Commerce** (ISSN 2231-4172), confirmed by the coordinator's independent search: Scholar9 lists "Researchers World - Journal of Arts, Science & Commerce (RW-JASC)", P-ISSN 2231-4172, E-ISSN 2229-4686; multiple researchersworld.com article pages print the header "-Journal of Arts, Science & Commerce • E-ISSN 2229-4686 • ISSN 2231-4172".
- "International Refereed Social Sciences Journal" is a descriptor/tagline that appears alongside the journal name (it is the OJS site header on the primary page), **not** the journal title. "International Refereed Research Journal" is likewise a descriptor line in the article footer. Replacing the bib field with either would make the entry wrong.

**What is actually true:** the current bib journal field is substantively correct (right journal, right volume/issue/pages/year). At most it could be expanded to the fuller form `Researchers World – Journal of Arts, Science and Commerce`. The issue's proposed replacement must not be applied.

**New adjacent finding — BVPS nuance in the same sentence (verified by the coordinator from the full text).** The thesis sentence at Ch2:228 also claims **BVPS** had a "statistically significant positive" association. The full text complicates that: "Book value per share has influenced the market price of share significantly in eleven out of sixteen years. But it has shown both positive and negative association. Book value per share has shown positive association in eight years, viz., 1993-94, 1995-96, 2002-03, 2003-04, 2005-06, 2006-07, 2007-08 and 2008-09… The negative association has occurred in 1994-95, 1996-97 and 1997-98… However, it has remained insignificant during 1998-99, 1999-00, 2000-01, 2001-02 and 2004-05." (Scribd L181–L186.) That is a BVPS nuance in the same sentence, not a DPS issue — but the sentence as written is not fully supported for BVPS, and the Table 2.1 row (line 326) repeats the same blanket claim. See Suggestion S3 below.

**Verdict: CORRECTED.** The DPS-sign half is confirmed and now stronger than stated (the full text was obtained and supports the thesis's positive DPS characterisation). But the bibliographic half is wrong: the current journal name is substantively correct, and the issue's proposed replacement journal name is incorrect. The issue should not be recorded as written.

---

## I-07 — GBIME 16th AGM minutes — CONFIRMED (with qualification)

**Bibliography entry (exact).** `src/thesis/references.bib:281–287`:

```bibtex
@misc{gbime2022agm,
  author       = {{Global IME Bank Limited}},
  title        = {Minutes of the 16th annual general meeting},
  year         = {2022},
  howpublished = {Filed with Nepal Stock Exchange},
  url          = {https://www.nepalstock.com.np/api/nots/security/fetchFiles?fileLocation=gbime_user%2F2023-01-04%2F16th+AGM+Minute_1672813977990.PDF}
}
```

No access date, no retrieval note, no digest. The `year = {2022}` is consistent with the meeting date (9 December 2022); the `2023-01-04` in the URL is the NEPSE file path/upload date, not the meeting date.

**Retrieval attempts (exact results).** Direct fetch of the exact cited URL via `browser.open` on 18 November 2026 ~20:13 NPT **timed out, no HTTP status returned** — "browser.open failed: Page fetch timed out … failure_stage: source_fetch, kind: upstream_fetch_failed". **Nothing was visible** — no PDF content, no error page, no access-denied page. This is a timeout, not proof the URL is dead. One alternative route (web search `"16th AGM" Global IME Bank minutes merger Bank of Kathmandu`) found **no mirror or bank-hosted copy** of the minutes PDF. It returned corroborating news reports (Rising Nepal Daily, 10 Dec 2022; ShareSansar, 11 Dec 2022; Merolagani announcement page — the 16th AGM *notice*, not the minutes; myRepublica, 14 Dec 2022), all consistent with the 16th AGM having approved a 1:1 merger — none of them the document itself.

**Live-browser check: STILL NEEDED.** No subagent can use the live browser, and none did. The failed text fetch must not be presented as proof the URL is dead — it establishes only that the URL was not retrievable by the text-fetch route on 18 Nov 2026.

**What the thesis cites the minutes for.** The key `gbime2022agm` is cited in exactly two thesis sentences:
- `src/thesis/chapters/chapter_02_literature_review.tex:207` — "Global IME Bank Limited (GBIME): Amalgamated with Bank of Kathmandu Limited (swap ratio 1:1) `\citep{gbime2022agm,gbime2023report}`; unified commercial operations commenced on 9 January 2023 `\citep{nrb2023bsr}`."
- `src/thesis/chapters/chapter_03_research_methodology.tex:49` — "Consolidation Mechanism: Statutory merger with an equity share swap ratio of 1:1 `\citep{gbime2023report}`. Following amalgamation, GBIME was projected to become the largest commercial bank in Nepal by total asset scale and paid-up equity capital `\citep{gbime2022agm}`."

So the minutes support: (a) the **1:1 swap ratio**, jointly with the 17th annual report; and (b) the **"projected to become the largest bank by total asset scale and paid-up equity capital"** claim, as the **sole** citation for that sentence. The minutes are **not** cited for the 9 January 2023 date — that is cited to `nrb2023bsr`.

**Alternative verified support (qualification that lowers the stakes).** The 9 January 2023 date is verified in NRB Bank Supervision Report 2022/23 (`nrb2023bsr`), Table 1-4: "16 Global IME Bank Ltd. **2023/01/09\***", footnote "*Joint operation date after merger/acquisition." The 1:1 swap ratio and the largest-bank substance are verified in the local 17th annual report (`gbime2023report`; `data/reports/GBIME/FY2079-80/GBIME_FY2079-80_annual_report.pdf`): "The merger was concluded with the swap ratio determined at 100 shares for every 100 shares held at then Bank of Kathmandu Ltd. … Joint Operation of the two entities commenced from 25th Poush 2079 (9th January 2023)"; "the bank continues to have the largest paid-up capital of NRs. 35.77 billion (Mid-Jul 2023) in the industry" and "we have become 'The Largest bank in Nepal' with total assets exceeding NRs. 500 billion!" — both confirmed by the coordinator's own extraction from the local PDF. **Qualification:** the annual report confirms the *substance* (largest by assets and paid-up capital) as an achieved fact in FY 2022/23, not the *projection* framing ("was projected to become") that the minutes — a December 2022 pre-merger document — would support. The wording "projected" therefore still rests on the unseen minutes; the underlying fact does not. Nothing in the thesis's analysis (no regression input, no price, no EPS/BVPS value) depends on the minutes.

**Appendix D.** Appendix D says nothing about the minutes file (grep for `16th` and `minute` in `appendix_d.tex`: zero matches). Its Source Register covers only the 30 annual reports. There is no retrieval note, digest, read record, or access date for `gbime2022agm` anywhere in Appendix D. The minutes were not documented as read, and no digest exists to check a future retrieval against.

**Verdict: CONFIRMED.** The bib entry exists exactly as described, the NEPSE URL could not be opened on a fresh independent retry, and no content-level claim about the minutes is made (nor can one be, since the document was never seen). Material qualification: **no thesis fact depends solely on the minutes** — every fact they are cited for is also supported by a verified source — but the minutes citation itself remains unverified, and a live-browser retrieval is still outstanding.

---

## Plan review — per-step verdicts

| Step | Issue | Verdict | Reason |
|---|---|---|---|
| 1 | I-01 Prabhu rationale | CORRECT | Ask the author for the contemporaneous factual rationale and any selection record; if none, use transparent author-approved language (purposive, identifies the omitted fifth, acknowledges no objective basis); do not invent a data-availability or comparability explanation. Respects the hard rule against inventing a reason. "Purposive" matches the thesis's own word ("purposive (judgmental)", Ch3:31). |
| 2 | I-04 identity fields | CORRECT | Verify against an official college/TU record; change metadata only if the record conflicts; otherwise log that the author checked it. |
| 3 | I-05 R10 | NEEDS CHANGE | The step is right in substance (preserve R9; add an explicitly supplementary, post-hoc R10 excluding both NMB and KBL FY 2076/77; state acquisition accounting at year-end; partial-year exposure, not fully pre-acquisition; reproducible final estimate needed — the reproduction confirms the earnings interaction moves materially, −3.4454 → −0.5575). But it states "the short **four-day** window between Deva joint operation and FY-end" — the verified fact is **three days** (12 July → 15 July 2020 FY-end). Correct "four-day" to "three-day" (and FY-end 15 July 2020, not 16 July) everywhere the plan's wording is carried forward. |
| 4 | I-02 SEBON/MoF | CORRECT | Inventory source notes/bibliography; record exact publication, year, URL, and claim supported; add direct citations; remove or accurately qualify unsupported bullets; revise acknowledgements that overstate use; verify the >30% statistic against SEBON's primary table or leave it explicitly attributed to Gurung & Dahal. Precision to add (see Suggestion S6): Gurung & Dahal's own citation is the bare "SEBON. (2023). Annual Report." — no title, year, URL, or table — so identifying the primary table is itself a sub-task the step does not name. |
| 5 | I-03 Kumari title | CORRECT | Read the PDF cover visually; replace the generic bib title with the printed title; if the cover cannot be read, use the descriptive meeting-minutes title; keep the 1 January 2023 date and 1:1 ratio cited to the sources that establish them. The cover **can** be read (see I-03 above), so the first branch applies and the title is "Special", not "Extraordinary". |
| 6 | I-06 Sharma | NEEDS CHANGE | Two things are wrong and one is missing. (a) The bibliography correction is **wrong**: the current "Journal of Arts, Science and Commerce" is correct; do NOT change it to "Researchers World - International Refereed Social Sciences Journal" (a descriptor, not the journal title) — at most expand to "Researchers World – Journal of Arts, Science and Commerce". (b) The full article **has now been obtained** and supports the thesis's positive DPS characterisation, so the DPS-sign question is resolved — the step's "keep or revise only after this check" is now satisfiable, and "do not label the sign conflict confirmed" is confirmed as the right stance. (c) The step misses the **BVPS nuance**: Ch2:228's "statistically significant positive" claim for BVPS is not fully supported by the full text (significant 11/16 years, mixed signs) — see Suggestion S3. |
| 7 | I-07 GBIME minutes | CORRECT | One successful live-browser retrieval attempt; record URL, date, outcome; if successful, inspect cover and resolutions; if not, locate a NEPSE issuer mirror or bank-hosted copy; if still unavailable, switch to a source supporting the thesis claim and remove details unique to the unobserved minutes. Correct, and the fallback is now known to be cheap (see Suggestion S5). |
| 8 | Implement edits | CORRECT | Make accepted edits in the bibliography, Chapter III, and dependent Chapter I/IV/V text; preserve the audit trail; avoid silently changing the main sample. |
| 9 | R10 implementation + Holm | CORRECT | Implement and run R10 from the versioned analysis script and frozen dataset; record excluded rows, n=26, K=14, df=12, coefficients, HC3 inference, joint Wald; keep R9; regenerate dependent tables/figures; revise every cross-reference and interpretation; expand the Holm family to R2–R10 and update every adjusted p-value and related conclusion. The Holm expansion is correct and complete: the current family is the eight joint tests R2–R9 (Holm-adjusted R6 p = 0.169); adding R10 makes nine tests, so the R6 adjusted p-value (and any other adjusted values) will change and must be updated everywhere, including the abstract. The step correctly requires this. |
| 10 | Final consistency pass | CORRECT | Final cross-document consistency pass for sample description, exclusions, source citations, title-page metadata, bibliography, and abstract/conclusion claims; close an issue only after the changed source and rendered thesis agree. |

**Priority order: CORRECT.** P0 (I-01, I-02, I-04, I-05) — sampling transparency, source provenance, identity fields, and the material R10 sensitivity — are the items that affect defensibility before submission. P1 (I-03, I-06, I-07) — citation metadata, with no thesis fact resting solely on an unread file — is the right lower tier. The new evidence does not change the ordering: I-06's DPS question is now resolved and I-03's cover is now read, but both remain one-line metadata fixes; I-07 still needs the live-browser retry, still P1.

**Exit criteria: CORRECT as stated.** All seven criteria are correct and checkable: every issue marked resolved / author-approved limitation / unresolved with explicit reason; no empirical reason for Prabhu's exclusion unless the author supplies support; R9 and post-hoc R10 separately labeled with R10 reproducible and consistent multiplicity reporting; every description of the R1–R9 suite, eight joint tests, and robustness-table coverage reconciled with the added R10; direct- and secondary-source claims distinguishable; identifiers checked or honestly labeled unverified; no unchecked claim silently carried forward as verified. One gap is **not** a plan defect but a separate repo-health item (see below).

**Repo health — the deleted root `pytest.ini` (separate from the plan, not a plan gap).** The pull that created HEAD 10d85d8 deleted the root `pytest.ini`, and `python -m pytest` now fails at collection with 3 errors (`data_analysis/analysis/tests/test_stats.py`, `data_analysis/data_extract/tests/test_discovery.py`, `data_analysis/data_extract/tests/test_normalize.py`; confirmed by the coordinator — `pytest.ini` does not exist). This is **out of scope for the plan's issue list** — it is a consequence of the pull, not one of the seven audit issues — so the plan is not wrong for omitting it. But it **must be restored before step 9** so the R10 pipeline work can be test-verified: step 9 requires running the versioned analysis script and verifying the fit, and the test suite is the verification mechanism for that pipeline. Restore the root `pytest.ini` (the F19 fix) as a repo-health action, not as an eighth audit issue. See Suggestion S7.

---

## Suggestions I am absolutely right about

Each suggestion below is backed by the evidence gathered in this review. No speculation, no "probably".

**S1 — I-03: Use "Special" in the Kumari bib title; do not use "Extraordinary".**
Evidence: the cover, visually read from the rendered scan, prints "कुमारी बैंक लि. को विशेष साधारण सभाको निर्णय विवरणहरु (माईन्यूट) २०७९/०८/२५" — विशेष = Special. "Extraordinary" (असाधारण) appears nowhere in the document, only in the bank's filename. Concrete action: change the `kumari2022sgm` title to "Minutes of the Special General Meeting of Kumari Bank Limited held on 2079/08/25" (the issue's proposed descriptive title, now confirmed against the cover), or use the verbatim Devanagari cover line. The 1 January 2023 date and the 1:1 ratio stay cited to NRB and to the minutes respectively, as they already are.

**S2 — I-06: Do NOT apply the issue's journal correction.**
Evidence: the article prints its journal as "Journal of Arts, Science & Commerce" on every page (ISSN 2231-4172); the journal's full name is "Researchers World – Journal of Arts, Science and Commerce" (confirmed by the coordinator's independent ISSN search: Scholar9, "Researchers World - Journal of Arts, Science & Commerce (RW-JASC)", P-ISSN 2231-4172, E-ISSN 2229-4686). "International Refereed Social Sciences Journal" is the OJS site header / a descriptor, not the journal title. Concrete action: leave the `sharma2011` journal field as "Journal of Arts, Science and Commerce", or at most expand it to "Researchers World – Journal of Arts, Science and Commerce". Never replace it with "Researchers World - International Refereed Social Sciences Journal".

**S3 — I-06 (new): Qualify the BVPS claim in the Sharma sentence.**
Evidence: the full text (read by the coordinator) states BVPS "has influenced the market price of share significantly in eleven out of sixteen years. But it has shown both positive and negative association" — positive in eight years (1993-94, 1995-96, 2002-03, 2003-04, 2005-06, 2006-07, 2007-08, 2008-09), negative in 1994-95, 1996-97, 1997-98, insignificant in 1998-99, 1999-00, 2000-01, 2001-02, 2004-05. The thesis sentence at `chapter_02_literature_review.tex:228` ("EPS, BVPS, and DPS exhibited statistically significant positive associations with share prices") and the Table 2.1 row at line 326 ("EPS, BVPS, and DPS exhibit significant positive associations with equity prices") are therefore not fully supported for BVPS. Concrete action: reword both to reflect the mixed BVPS signs (e.g., "EPS and DPS exhibited statistically significant positive associations, while BVPS was significant in eleven of sixteen years with mixed signs"), or restrict the sentence to the abstract-level claim. The DPS limb needs no change — the full text supports it.

**S4 — I-05: Correct the day-count and FY-end date, and the Deva-date citation.**
Evidence: the KBL FY 2076/77 report's own reporting-date table (extracted by the coordinator): "Reporting date — Ashadh 31, 2077 — July 15, 2020. Reporting period — Shrawan 01, 2076 to Ashadh 31, 2077 — July 16, 2019 to July 15, 2020." "July 16, 2020" occurs 0 times in the report. Joint operation began Asadh 28, 2077 = 12 July 2020; gap = **3 days**, not 4. The thesis (Ch3:383) already says "three days" and is correct. Concrete action: change plan step 3's "four-day window" to "three-day window" (and FY-end 15 July 2020, not 16 July) everywhere the plan's wording is carried forward, and cite the Deva joint-operation date to the **FY 2076/77** report (PDF p. 7), not the FY 2077/78 report — the FY 2077/78 report contains no legible passage stating the date.

**S5 — I-07: If the live-browser retry fails, the fallback is cheap and specific.**
Evidence: the 9 January 2023 date is verified in NRB BSR Table 1-4; the 1:1 swap and the largest-bank substance are verified in the local GBIME 17th annual report (extracted by the coordinator: "largest paid-up capital of NRs. 35.77 billion (Mid-Jul 2023)", "we have become 'The Largest bank in Nepal' with total assets exceeding NRs. 500 billion!"). Only the "projected to become" *framing* in Ch3:49 rests on the unseen minutes. Concrete action: if the retry fails, replace the `gbime2022agm` citation in the Ch3:49 sentence with `gbime2023report` and reword "was projected to become" to the achieved fact; note in Appendix D that the minutes were not retrievable. No regression input, price, or EPS/BVPS value depends on the minutes.

**S6 — I-02: Name the sub-task of identifying the SEBON primary table.**
Evidence: Gurung & Dahal's own citation is the bare "SEBON. (2023). Annual Report." — no title, fiscal year, URL, or table number (verified from the PDF by the I-02 verifier). Concrete action: before plan step 4's "verify the >30% statement against SEBON's primary table", first identify *which* SEBON annual report and table the figure comes from (the most likely candidate is the SEBON Annual Report 2022/23, but that must be confirmed by opening it, not assumed). If it cannot be identified, the fallback in step 4 — leave the figure explicitly attributed to Gurung & Dahal as a secondary source — is the correct outcome.

**S7 — Repo health (separate from the plan): restore the root `pytest.ini` before step 9.**
Evidence: the pull deleted the root `pytest.ini`; the coordinator confirmed `pytest.ini` does not exist and `python -m pytest` fails at collection with 3 errors (`test_stats.py`, `test_discovery.py`, `test_normalize.py`). Concrete action: restore the root `pytest.ini` (the F19 fix) as a repo-health action so the test suite runs again, and run the suite before implementing R10 so the pipeline has a verified baseline. This is not an eighth audit issue and does not belong in the plan's issue list — but step 9's R10 work cannot be test-verified without it.

**S8 — I-01: Reconcile the "five major merged institutions" phrasing when implementing step 1.**
Evidence: `chapter_02_literature_review.tex:395` says the wave altered reporting "across five major merged institutions" while the thesis samples four, with no explanation of the difference. Concrete action: when the I-01 language is added (step 1), make Ch2:395 consistent with the four-sampled/one-omitted fact — either name Prabhu as the omitted fifth there too, or qualify the count. This is a one-sentence consistency fix, not a new finding.

---

## What remains for the author

- **Author input required:** I-01 (the real selection reason for omitting Prabhu/Century, if one was documented; if none, approval to state the omission as a purposive selection without inventing a factual reason); I-04 (a college/TU record confirming the roll number, registration number, institution, and "Pokhara, Nepal").
- **Live-browser retry still needed:** I-07 (one retry of the exact NEPSE URL in a normal live browser, result and date recorded). No subagent could do this.
- **Analysis work (plan steps 3 and 9):** R10 must be implemented in the versioned pipeline from the frozen dataset, with the n=26 numbers above as the expected values to reproduce (δ_E=−0.5575, δ_B=−1.3078, F(2,12)=1.5699, p=0.2479 — reproduced exactly by the coordinator, but not yet a saved pipeline output), the Holm family expanded to R2–R10, and every description of the R1–R9 suite, the eight joint tests, and the robustness-table coverage reconciled.
- **Bibliography/text fixes ready to apply:** I-03 (Kumari title → "Special"), I-06 (leave the journal field; qualify the BVPS sentence), I-02 (SEBON/MoF bullets — substantiate or remove/qualify; acknowledgements line 20), I-05 (three-day / 15 July corrections), I-01 (Ch2:395 count language).
- **Repo health:** restore the root `pytest.ini` before the R10 work (S7).
- **Nothing in this review changes the thesis source.** All fixes are for the author/plan to apply; this file is a verification record only.

## Verification log (what was checked, how, and what could not be verified)

- **Thesis source:** every cited thesis location was opened and quoted (file:line + exact excerpt) by the assigned verifier and, for the consequential claims, re-checked by the coordinator (Prabhu grep — 2 hits; Ch3:157–162 bullets; references.bib zero SEBON/MoF hits; metadata.tex; Kumari bib entry; Sharma bib entry and Ch2:228/326; R9 at Ch3:383; Appendix E diagnostics).
- **Primary sources opened:** NRB Bank Supervision Report 2024 (I-01 verifier; coordinator's retry failed at the tool level — noted in §I-01); Gurung & Dahal (2025) Pravaha PDF (I-02 verifier); Kumari SGM PDF (I-03 verifier, rendered all 11 pages; coordinator opened the same PDF via text fetch); KBL FY 2076/77 and FY 2077/78 annual reports (local PDFs, extracted by the I-05 verifier and the coordinator); NMB FY 2076/77 report (I-05 verifier); Sharma full text via Scribd (I-06 verifier; coordinator independently opened and read the same copy); GBIME 17th annual report (local PDF, extracted by the I-07 verifier and the coordinator); NRB Bank Supervision Report 2022/23 Table 1-4 (I-07 verifier); ISSN 2231-4172 search (coordinator).
- **Computations run:** I-05 reproduction — two independent implementations by the coordinator (repo pipeline + from-scratch numpy HC3), agreeing to ~1e-10; controls R2 and R9 reproduce the stored values exactly; the n=26 variant matches the issue's numbers to 4 dp. Script: `/tmp/i05-coord/repro_i05.py`. No pytest was used (it currently fails at collection).
- **Could not be verified:** the Prabhu 22nd Annual Report PDF (fetch timeout; indirectly corroborated only); Prabhu's FY 2076/77 audited annual report (not directly sighted); the GBIME 16th AGM minutes PDF (direct fetch timed out; no mirror found; live-browser retry still outstanding); the exact Devanagari cover wording of the Kumari minutes beyond the I-03 verifier's visual reading (the coordinator's text fetch confirms the document, its scanned nature, and the 1:1 ratio but cannot read the cover visually); correctness of the candidate identifiers against the college/TU record (no such record exists in the repo); whether the author consulted SEBON/MoF sources outside the repo (absence from the bibliography/register/repo proves no *documented* use, not no use).
- **Git status:** only `issues/v1/review.md` is new (plus the pre-existing untracked `docs/thesis_supervisor/` directory). HEAD remains `10d85d8`. Nothing else was created, modified, or built.
