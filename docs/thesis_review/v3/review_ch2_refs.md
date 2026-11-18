# Independent content review (v3) — Chapter II (Literature Review) + citations and references

- **Thesis:** *Value Relevance of Accounting Information Before and After the Banking Consolidation Wave: Evidence from Nepalese Commercial Banks* (MBS dissertation, Asmita Subedi, Triveni International College; TU Faculty of Management).
- **Repo:** `~/workspace/verbose-chainsaw`. **HEAD:** `2b4e10f` (verified by `git rev-parse HEAD` in this task).
- **Files reviewed in full:** `src/thesis/chapters/chapter_02_literature_review.tex` (410 lines) and `src/thesis/references.bib` (746 lines, 75 entries).
- **Reviewer role:** scope reviewer, read-only. No thesis, code, data, config, v1, or v2 file was modified. No PDF build was performed. No commit, push, supervisor-bound text, or sending.
- **Date of review:** 18 November 2026.
- **Only file created by this review:** `docs/thesis_review/v3/review_ch2_refs.md`.

## 1. Scope and method

### 1.1 Scope

PART A — verify the fix loop's patches for the v2 findings in this scope, using the audit's corrected versions where they exist:

- M12 (Ch2 HC3 rewording limb).
- Minors m08, m10–m19 (m10 included although the task enumeration began at m11: it is a Chapter II finding, B-03 in the v2 scope review), m36, m37.
- Suggestions s08, s09.
- Table 2.1 rows and counts under m17, using the audit's corrected counts (10 rows lacking an observation count, 4 lacking any sample size; Pradhan 2003 "29 companies, 93 obs" wrongly listed in v2; Kwon 2020 omitted in v2).

PART B — fresh read of Chapter II + `references.bib` as they now stand, including new issues introduced by the loop's patches.

The v2 scope review for this area is `docs/thesis_review/v2/review_ch2_refs.md` (findings B-01–B-15); the consolidated v2 review is `docs/thesis_review/v2/content_review.md` §10; the hallucination audit is `docs/thesis_review/v2/verification_audit.md`. The loop's claims log (`~/workspace/review-audit-scratch/loop-v2/LOOP_STATUS.md`, `ROUND_1_B.md`, `ROUND_3.md`, `ROUND_4.md`) was read **only** to know what the loop claims it did. Per the task rules, none of those documents was treated as evidence for any thesis fact: every verdict below rests on a grep, count, or read of the thesis source re-run in this task, or on a source opened in this task and cited as such.

### 1.2 Method

1. Read `chapter_02_literature_review.tex` in full (410 lines) and `references.bib` in full (75 entries).
2. Re-ran every count by script against the current files: Table 2.1 rows and "not stated" flags; the 15-study EPS-and-BVPS count; the 19-key P/E lists; two-way citation integrity (all `.tex` files under `src/thesis/` vs all `.bib` keys); Wilkinson author count; brace balance in `references.bib`; article-title capitalisation scan.
3. For each assigned v2 finding, opened the cited thesis location and compared the current text with the finding, the audit correction, and the loop's claimed fix.
4. Verified m08 and m36 directly against the repo-held annual reports (`data/reports/NMB/FY2077-78/`, `data/reports/HBL/FY2079-80/`, `data/reports/NIMB/FY2079-80/`) with `pdftotext` + grep, re-running the loop's claimed verification rather than trusting it.
5. Spot-checked the new Barth/Holthausen entries and the value-relevance definition against the published text via web search (Barth et al. 2001, p. 79, quoted verbatim in search results); spot-checked the Almumani (2014) variable label against the published regression table via web search; spot-checked the Chhetri (2023) author name against the NepJOL journal page via web search.
6. Did **not** open the Pradhan & Dahal (2016) SSRN paper, the Sharma (2011), Bajracharya (2019), Niroula (2021), or Gyawali (2022) full texts in this task; source-level accuracy of the loop's added prose sentences for those studies is therefore recorded as UNVERIFIED by this reviewer (see §5), even though the thesis-internal prose/table consistency was verified.

**Status labels.** VERIFIED = read in the thesis source, counted by script, or checked against a source opened in this task, with the basis stated. INFERRED = conclusion drawn from stated evidence, with the basis given. UNVERIFIED = could not be established in this task, with the reason given; an UNVERIFIED item is never treated as wrong.

**Fix verdicts (Part A).** FIXED / PARTIALLY FIXED / NOT FIXED / INCORRECTLY FIXED / FALSE FINDING.

**Severities:** Critical / Major / Minor / Suggestion. **Revision scales:** Narrow / Substantive / Fundamental.

### 1.3 Counts re-run in this task (current working tree)

- `.bib` entries: **75** (was 72 at v2). New keys vs HEAD: `barth2001`, `holthausen2001`, `nmb2021report` (loop additions) plus six keys already present in the uncommitted working tree at v2 time (`gbime2023report`, `incometaxact2058`, `kbl2023report`, `nrb2013stats`, `nrb2023bsr`, `tht2023nrbmerger`). No key removed. No duplicate keys.
- Two-way citation check (correct multi-key parsing): **75 bib keys, 75 unique cited keys across the thesis, 0 cited-but-missing, 0 uncited**. Chapter II alone: **65 unique keys**.
- Table 2.1: **26 rows**; **19** flagged "Circular P/E inclusion"; the §2.4.5 and §2.5.2 P/E `\citep` lists each contain **19 keys** and match the flagged rows; **15** studies test both EPS and BVPS (see §3, m17 note on the Kwon `\&` trap); **10** rows carry a "not stated in the reviewed source" flag (grep count = 10).
- `references.bib` braces: **627 open / 627 close** — balanced.
- `and others`: **0 hits** in `references.bib`.
- Articles without a `doi` field: 9 (`sharma2011`, `malhotra2013`, `almumani2014`, `bajracharya2019`, `chaudhari2025`, `ross1977`, `bhattacharya1979`, `miller1961`, `jensen1986`) — same nine as v2 §6.4.

---

## 2. PART A — Verification of the loop's fixes for the assigned v2 findings

### 2.1 Summary table

| v2 ID | Audit verdict | Loop's claimed fix (from loop log only) | This review's verification | Verdict |
|---|---|---|---|---|
| M12 | CONFIRMED | Ch2:407 reworded; HC3 no longer presented as the small-cluster answer | Qualification sentence added, but the lead clause still says the gap is addressed "by implementing MacKinnon-White HC3" (§2.2) | **PARTIALLY FIXED** |
| m08 | CONFIRMED | New bib entry `nmb2021report`; `\citep{nmb2021report}` added at Ch2:211; figures verified vs NMB report | Citation present; all four figures re-verified by this reviewer against the repo-held NMB FY 2077/78 report (§2.3) | **FIXED** |
| m10 (B-03) | CONFIRMED | Hand-typed author names removed from the L275 footnote, `\citet` kept | Footnote now reads `\citet{gurungdahal2025} … by \citet{dahal2025}`; doubling gone (§2.4) | **FIXED** |
| m11 (B-04) | CONFIRMED | Redundant `\citep{bhattarai2014}` removed at L300 and in §2.5.3; repeated sentence removed | Redundancy and repetition gone, but L300 "Bhattarai (2014)" is now plain text with **no** `\citet` command (§2.5) | **PARTIALLY FIXED** |
| m12 (B-05) | CONFIRMED | DOI added to `ohlson1995` | `doi = {10.1111/j.1911-3846.1995.tb00461.x}` present in `references.bib` (§2.6) | **FIXED** |
| m13 (B-06) | CONFIRMED | 40 article titles sentence-cased (Round 1); 16 @book/@techreport/@misc titles sentence-cased (Round 3); 4 official titles preserved; braces 627/627 | All titles verified individually; one miss remains — `wilkinson2016fair` still has "Guiding Principles" in Title Case (§2.7); otherwise as claimed | **PARTIALLY FIXED** |
| m14 (B-07) | CONFIRMED | "and others" replaced with the full 53-author list | 53 authors counted by script; first six and last (Mons, Barend) as claimed; "and others" 0 hits (§2.8) | **FIXED** |
| m15 (B-08) | CONFIRMED | "empirical panel" → "sequence of annual cross-sectional regressions" | New wording at L117; "forty-one-year empirical panel" 0 hits (§2.9) | **FIXED** |
| m16 (B-09) | CONFIRMED | `nrb2011` removed from the 2022–2023 forbearance citation | L202 cites `\citep{tht2023nrbmerger}` only; `nrb2011` still cited at the 2011 Bylaws bullet (§2.10) | **FIXED** |
| m17 (B-10) | CORRECTED (audit) | Flags added to the 9 rows lacking one, per the audit's corrected counts (10 rows lack an observation count; 4 lack any sample size) | 10 flags present; the 10 flagged rows are exactly the audit's list; Pradhan 2003 keeps "29 companies, 93 obs"; Kwon flag present (§2.11) | **FIXED** |
| m18 (B-11) | CONFIRMED | Every flagged variable mentioned in the prose | All six prose additions present at the claimed lines; thesis-internal consistency holds; source-level accuracy of the added sentences NOT re-verified by this reviewer except Almumani (§2.12); Almumani label issue is new finding N3 (§4) | **FIXED** (thesis-internal; source accuracy partly UNVERIFIED) |
| m19 (B-12) | CONFIRMED | Definition + Barth/Holthausen–Watts paragraph added (§2.2.2); new entries `barth2001`, `holthausen2001` | Paragraph present L105–107; both entries present, cited, and bibliographically correct; Barth definition verbatim-confirmed (§2.13) | **FIXED** |
| m36 (B-15) | UNVERIFIED (v2) | CLOSED, no patch: both ratios verified vs repo-held reports | Re-verified directly by this reviewer against the repo-held HBL and NIMB FY 2079/80 reports (§2.14) | **FIXED** (verified correct; no patch was needed) |
| m37 (B-14) | UNVERIFIED (v2) | NOT PATCHABLE — left unverified for the author | "168 obs" still at L338, still with no source confirmation, and no invented number substituted (§2.15) | **NOT FIXED** (deliberately; standing item, correctly left open) |
| s08 | CONFIRMED | Patched in Chapter I scope (ROUND_1_A) | Ch1 language finding; no Chapter II action claimed or needed — not applicable to this scope (§2.16) | **NOT APPLICABLE** (Ch2) |
| s09 (B-13) | CONFIRMED | NOT PATCHED — author input | No NFRS 9 value-relevance paragraph; no scale-effects / conservatism / omitted-variables discussion added (§2.17) | **NOT FIXED** (open suggestion) |

**Tally of the 16 assigned items in this scope (counting m10, which the task enumeration began after): 9 FIXED, 3 PARTIALLY FIXED (M12, m11, m13), 2 NOT FIXED (m37 deliberately open; s09 open suggestion), 1 NOT APPLICABLE to Chapter II (s08), 0 INCORRECTLY FIXED, 0 FALSE FINDING.** No assigned finding was silently "fixed" with invented content: the two items the loop left open (m37, s09) are still visibly open, and m36's closure rests on numbers this reviewer re-verified in the cited reports.

### 2.2 M12 — HC3 presented as the small-cluster answer — PARTIALLY FIXED

- **Location:** `src/thesis/chapters/chapter_02_literature_review.tex:407` (§2.5.5).
- **Current text (exact excerpt):** "This dissertation addresses this gap by implementing MacKinnon-White HC3 heteroskedasticity-robust standard errors, disclosing exact residual degrees of freedom ($28 - 14 = 14$ df), and framing findings as observed statistical associations rather than causal proofs. HC3 addresses heteroskedasticity, not within-bank correlation, so the within-bank independence assumption remains untested; the small-cluster limitation is handled by disclosing the degrees of freedom and reporting the sensitivity of the joint test across covariance estimators (Chapter~IV, Table~\ref{tab:cov_sensitivity}) and the wild-cluster bootstrap."
- **What changed:** the second sentence is new (confirmed by `git diff HEAD`, which shows the qualification sentence appended to the previously unqualified paragraph). It states the HC3/cluster distinction correctly and re-attributes the small-cluster handling to disclosure, sensitivity analysis, and the wild-cluster bootstrap.
- **What remains:** the first sentence still says the gap — introduced in the same paragraph as "the econometric hazards of small-cluster panel inference" with "standard cluster-robust standard errors suffer from severe downward bias when the number of clusters is small (in this study, $G = 5$)" — is addressed "by implementing MacKinnon-White HC3". A reader who stops at the first sentence still takes away the claim v2-M12 corrected. The fix is real but incomplete: the lead clause, not only the follow-up, needs the attribution corrected (e.g. "addresses this gap by disclosing … and reporting sensitivity …, using HC3 as the heteroskedasticity-robust estimator").
- **Severity:** Minor (wording precision; the correct statement is now present one sentence later). **Scale:** Narrow.
- **Status:** VERIFIED (read L407 in full; diffed against HEAD).

### 2.3 m08 — NMB–Kanchan figures uncited — FIXED

- **Location:** `src/thesis/chapters/chapter_02_literature_review.tex:211`; `src/thesis/references.bib` (`nmb2021report`).
- **Current text (exact excerpt, L211):** "(Note: NMB had previously acquired Kanchan Development Bank Limited in August 2020, adding approximately NPR 0.50 billion in new shares issued to Kanchan shareholders at the 85\% swap ratio, alongside a 13\% bonus share capitalization, in FY 2077/78 \citep{nmb2021report}, but remained independent during the 2022--2023 wave)."
- **Bib entry (exact):** `@techreport{nmb2021report, author = {{NMB Bank Limited}}, title = {Annual report 2020/21}, institution = {NMB Bank Limited}, year = {2021}}`.
- **Re-verification by this reviewer** (not the loop's): `pdftotext` on the repo-held `data/reports/NMB/FY2077-78/NMB_FY2077-78_annual_report.pdf`:
  - Date: "commenced unified operations post-acquisition of erstwhile Kanchan Development Bank Ltd. from August 23, 2020" — matches "August 2020".
  - Amount: "496,765,500" (share-capital table) = NPR 496.77m ≈ "approximately NPR 0.50 billion" — matches.
  - Swap: "addition of Capital from acquisition with Erstwhile KADBL at SWAP ratio of 1:0.85" — matches "85\% swap ratio".
  - Bonus: "Issuance of 13\% Bonus Shares from FY 2076/77" in the share-capital history — matches the 13% figure. Small wording nuance: the thesis attaches the 13% bonus to "FY 2077/78", while the report's history row describes the issuance as "from FY 2076/77" (the row itself sits in the FY 2077/78 report). This is the same reading the loop recorded; it is not a factual error as written, only a fiscal-year attribution that could be read either way. Not raised as a finding.
- **Severity:** Minor (as v2). **Scale:** Narrow. **Status:** VERIFIED (thesis source + repo-held report opened in this task).

### 2.4 m10 (B-03) — Footnote repeats author names already printed by `\citet` — FIXED

- **Location:** `src/thesis/chapters/chapter_02_literature_review.tex:275`.
- **Current text (exact excerpt):** "`\footnote{\citet{gurungdahal2025}, published in \textit{Pravaha} (vol.~31, no.~1, pp.~1--12), is distinct from the comprehensive panel study by \citet{dahal2025} in the \textit{Interdisciplinary Journal of Management and Social Sciences} (vol.~6, no.~1, pp.~252--261), which examined 209 bank-year observations across all listed commercial banks.}`"
- Grep: "Gurung and Dahal \citet" = 0 hits; "Dahal, Gurung, and Ghimire \citet" = 0 hits. The doubling is gone; the footnote now renders the author names once, via `\citet`.
- **Status:** VERIFIED.

### 2.5 m11 (B-04) — Redundant parenthetical citation + repeated sentence — PARTIALLY FIXED

- **Location:** `src/thesis/chapters/chapter_02_literature_review.tex:300` (§2.4.5) and §2.5.3 (L401 area).
- **Current text (exact excerpt, L300):** "Bhattarai (2014) measures equity share prices at fiscal-year-end (Ashadh-end / mid-July)."
- **What changed:** the redundant `\citep{bhattarai2014}` is gone (grep: no `\citep{bhattarai2014}` attached to either sentence), and the near-verbatim repeated sentence in §2.5.3 is gone — that paragraph now opens "Because audited annual financial statements are not prepared, audited, and published until months after Ashadh-end, …". Grep: "Bhattarai (2014) measures" = 1 hit (L300 only).
- **What remains:** L300 now states a sourced factual claim about Bhattarai (2014) in plain text with **no citation command at all** — neither the removed `\citep` nor a narrative `\citet{bhattarai2014}`. The v2 fix envisaged dropping the `\citep` after a narrative citation; the loop dropped the citation entirely instead. The entry is not orphaned (`bhattarai2014` is cited elsewhere in the chapter, e.g. L237 `\citet{bhattarai2014}` and the Table 2.1 row at L336), so two-way integrity is unaffected, but the specific sentence is now uncited at its point of use. The same pattern (plain-text author-year without a cite command) also occurs at L224, "Employing the Ohlson (1995) valuation framework" — pre-existing, not loop-introduced; see new finding N4 in §4.
- **Severity:** Minor. **Scale:** Narrow. **Status:** VERIFIED.

### 2.6 m12 (B-05) — Ohlson (1995) DOI omitted — FIXED

- **Location:** `src/thesis/references.bib` (`ohlson1995`).
- **Current entry (exact excerpt):** "`doi = {10.1111/j.1911-3846.1995.tb00461.x}`" alongside author, title "Earnings, book values, and dividends in equity valuation", journal *Contemporary Accounting Research*, volume 11, number 2, pages 661–687, year 1995. The DOI is the one v2 confirmed from the CityU record.
- **Status:** VERIFIED.

### 2.7 m13 (B-06) — Article-title capitalisation inconsistent (APA 6th sentence case) — PARTIALLY FIXED

- **What the loop claimed:** 40 article titles sentence-cased in Round 1; 16 @book/@techreport/@misc titles sentence-cased in Round 3, preserving 4 official titles (bafia2017, companiesact2006, incometaxact2058, nrb2011); braces balanced 627/627.
- **What this reviewer verified, title by title:**
  - All 50 `@article` titles were read. 49 are in sentence case (first word and proper nouns capitalised; first word after a colon capitalised, e.g. "Factors affecting the share price: Evidence from Nepalese commercial banks"). Proper nouns/acronyms are preserved, braced where needed (`{Nepal}`, `{Nepal Stock Exchange}`, `{SFAS}`, `{FAIR}`).
  - **One miss:** `wilkinson2016fair` — "`title = {The {FAIR} Guiding Principles for scientific data management and stewardship}`". "Guiding Principles" remain in Title Case; sentence case requires "guiding principles". The loop's Round 1 list of titles "already in sentence case" included `wilkinson2016fair`, which was wrong: only the acronym {FAIR} was protected, the remaining title words were never lowercased. See new finding N1 (§4).
  - All 24 @book/@techreport/@misc entries were read (1 book, 8 techreports, 15 misc). The 16 changed titles are sentence case as claimed: `pant2016` ("Social science research and thesis writing"); `nrb2013stats`, `nrb2023bsr`, `nrb2023list` (with `{Nepal Rastra Bank}` braced), `gbime2023report`, `kbl2023report`, `hbl2023report`, `nimb2023report`, `nmb2021report`; `gbime2022agm`, `kumari2022sgm`, `nepse2017` (with `{NEPSE}` braced), `nrb2015`, `aea2026datacode`, `sharesansar2022nib`, `sharesansar2022gbime` (with `{Nepal Investment Bank}` / `{Global IME Bank}` / `{Bank of Kathmandu}` / `{NEPSE}` braced). No proper noun was damaged in any of the 16: the brace scan found the expected protected nouns intact.
  - The 4 preserved official titles are unchanged as claimed: `bafia2017` ("Banks and Financial Institutions Act, 2073 (2017)"), `companiesact2006` ("Companies Act, 2063 (2006)"), `incometaxact2058` ("Income Tax Act, 2058 (2002)"), `nrb2011` ("Bank and Financial Institutions Merger Bylaws, 2068"). Preserving these as published short titles is defensible.
  - Braces: 627 open / 627 close — balanced, as claimed.
  - Two judgement calls, neither raised as an error: (i) `acharya2026merger` now reads "… Evidence from a least developed country" — "least developed country" lowercased, which is correct sentence case (the UN category is not a proper noun in APA 6th title case rules as applied here); (ii) `kumari2022sgm` was retitled from "Minutes of the Special General Meeting, FY 2079/80" (HEAD) to "Extraordinary general meeting document, FY 2079/80 (merger proposals and share swap ratio)" — the cited URL's own filename is `1670847430_Extra_Ordinary_General_Meeting_2079-08-25_Kumari_Bank_Ltd..pdf`, so "Extraordinary" follows the source file; the new title is descriptive rather than the document's own title, which is a style matter, not a factual error.
- **Severity:** Minor. **Scale:** Narrow. **Status:** VERIFIED (every title read in this task).

### 2.8 m14 (B-07) — `wilkinson2016fair` "and others" — FIXED

- **Location:** `src/thesis/references.bib` (`wilkinson2016fair`).
- **Verification by script:** the author field splits on " and " into **53 authors**; first six are Wilkinson, Dumontier, Aalbersberg, Appleton, Axton, Baak; last author is "Mons, Barend". "and others" = 0 hits in the whole `.bib`. This matches the published author list (v2 confirmed the list ends with Mons, B.).
- **Note:** whether `apacite` renders this as first six + ellipsis + last author (the APA 6th rule v2 invoked) can only be judged from rendered output, which was not built (per task rules). The `.bib`-level encoding is now correct for that rendering. **Status:** VERIFIED at source level; rendering INFERRED (not checked).

### 2.9 m15 (B-08) — Collins described as an "empirical panel" — FIXED

- **Location:** `src/thesis/chapters/chapter_02_literature_review.tex:117`.
- **Current text (exact excerpt):** "`\citet{collins1997}` similarly demonstrate across a forty-one-year sequence of annual cross-sectional regressions that the relative value relevance of earnings versus book values shifts systematically …"
- Grep: "forty-one-year empirical panel" = 0 hits. **Status:** VERIFIED.

### 2.10 m16 (B-09) — 2011 Merger Bylaws cited for a 2022–2023 forbearance claim — FIXED

- **Location:** `src/thesis/chapters/chapter_02_literature_review.tex:202`.
- **Current text (exact excerpt):** "NRB actively encouraged horizontal ``big mergers'' through moral suasion and regulatory forbearance (such as temporary leniency on Credit-to-Deposit ratios and branch overlapping) `\citep{tht2023nrbmerger}`; …"
- Grep: "nrb2011,tht2023nrbmerger" = 0 hits. `nrb2011` remains cited at the 2011 Bylaws bullet (L197 area), so the entry is not orphaned.
- **Note:** "moral suasion" and "big mergers" remain the thesis's own characterisations (v2 established they are not the news article's words). That was not part of the required fix, and no reason is given in the thesis for either characterisation; recorded here as a statement of fact, not a finding. **Status:** VERIFIED.

### 2.11 m17 (B-10) — Table 2.1 rows give no sample size / observation count — FIXED (against the audit's corrected counts)

- **Audit correction applied:** v2 listed six rows and wrongly included Pradhan (2003) among them while omitting Kwon (2020). The audit's true counts are 10 rows lacking an observation count and 4 lacking any sample size.
- **Verification by this reviewer (re-counted from the table, L322–378):** the phrase "not stated in the reviewed source" occurs **10 times** in the table. The 10 flagged rows are exactly: Collins (1997) — firm count; Kwon (2020) — N and period; Sharma (2011) — firm count; Malhotra (2013) — observation count; Almumani (2014) — bank count; Bhattarai (2014) — observation count; Lamsal (2024) — observation count; Bhattarai (2024, MPS) — observation count; Bhandari (2026) — observation count; Adhikari et al. (2023) — observation count.
  - Rows lacking an observation count: those 10 — matches the audit.
  - Rows lacking **any** sample size (no firm/bank count at all): Collins, Kwon, Sharma, Almumani — 4, matches the audit. (Malhotra gives 95 firms; Bhattarai 2014 gives 9 banks; Lamsal, Bhattarai 2024 MPS, Bhandari, Adhikari give bank counts — so they lack only the observation count, not the sample size.)
  - Pradhan (2003), L334, retains "Listed firms, 29 companies, 93 obs, 6 yrs (1994--1999)" — correctly **not** flagged.
  - Kwon (2020), L324, retains "(N and period not stated in the reviewed source)".
- **Counts cross-check:** the "fifteen studies" claim (§2.4.5, L292) was recomputed: a naive string count of the Key Variables column gives 14 because the Kwon row contains an escaped `\&` ("US M\&A Firms") that splits a naive `&`-delimited parse, and Giri's row says "Net Worth Per Share" rather than "BVPS". Reading both rows, the true count is 15 (Collins, Kwon, Sharma, Malhotra, Almumani, Pradhan 2016, Niroula, Chhetri, Joshi, Giri, Lamsal, Gurung, Bhattarai 2024 MPS, Pant, Gurung & Dahal) — the claim stands.
- **Open item carried forward:** the loop log records a secondary-source discrepancy for Almumani (2014) — Pandey & Sunar assert "seven Jordanian banks and 49 observations", while v2 (which opened the full text) records the bank count as not stated. The "not stated" flag was kept. This reviewer did not re-open the Almumani full text; the discrepancy is unresolved and remains for the author to confirm against the full text. See §5.
- **Status:** VERIFIED (counts re-run in this task).

### 2.12 m18 (B-11) — Table 2.1 "Key Variables" lists variables the prose never mentions — FIXED (thesis-internal; source accuracy partly UNVERIFIED)

- **Verification:** each flagged variable is now mentioned in the prose paragraph for its study:
  - Sharma (2011), L228: "Sharma also tested the price-earnings ratio, dividend yield, dividend payout, and firm size (measured by sales and net worth) as explanatory variables."
  - Almumani (2014), L228: "Dividend per share and dividend payout (DPR) were also tested but had insignificant effects."
  - Bajracharya (2019), L241: "Bank rate (BR) and market capitalization (Ln MC) were also included as external factors."
  - Niroula (2021), L250: "Dividend yield (DY) and return on assets (ROA) were likewise included in the model but had negligible effects."
  - Gyawali (2022), L252: "GDP had a positive but insignificant effect on share prices, while inflation had a negative and insignificant effect."
  - Gurung & Subedi (2024), L262: "… while dividend per share and total assets (TA) were statistically insignificant …"
- **Limits of this verification:** this reviewer verified the prose/table match (thesis-internal) for all six. Source-level accuracy of the added sentences was **not** re-verified by this reviewer for Sharma, Bajracharya, Niroula, Gyawali, or Gurung & Subedi (their sources were not opened in this task; the loop log asserts they were verified against abstracts/full texts). One added sentence **was** checked against its source in this task — Almumani — and it produced new finding N3 (§4): the source's variable label is "DP", not "DPR". The Almumani "insignificant effects" substance is confirmed (source regression table: DP B = 0.016, p = 0.803; source text: "other variables (DPS and DP) have insignificant impact on MP").
- **Status:** VERIFIED (prose/table match); source accuracy UNVERIFIED except Almumani (see N3).

### 2.13 m19 (B-12) — No formal "value relevance" definition; Barth / Holthausen–Watts absent — FIXED

- **Location:** `src/thesis/chapters/chapter_02_literature_review.tex:105–107` (start of §2.2.2).
- **Current text (exact excerpt):** "In the extant literature, an accounting amount is defined as value relevant if it has a predicted association with equity market values `\citep{barth2001}`. This dissertation adopts that definition: earnings per share and book value per share are value relevant to the extent that they predict the market price per share of Nepalese commercial banks. Whether such associations inform standard setting is itself contested: `\citet{holthausen2001}` conclude that value-relevance research offers little insight for standard setters, while `\citet{barth2001}` argue that it assesses how well accounting amounts reflect information used by equity investors and provides insights into questions of interest to standard setters."
- **Bib entries (exact):**
  - `barth2001`: Barth, Beaver & Landsman (2001), "The relevance of the value relevance literature for financial accounting standard setting: Another view", *Journal of Accounting and Economics* 31(1–3), 77–104, DOI 10.1016/S0165-4101(01)00019-2.
  - `holthausen2001`: Holthausen & Watts (2001), "The relevance of the value relevance literature for financial accounting standard setting", *Journal of Accounting and Economics* 31(1–3), 3–75, DOI 10.1016/S0165-4101(01)00029-5.
- **External check by this reviewer:** the Barth et al. (2001) full text (via search results) gives, at p. 79: "In the extant literature, an accounting amount is defined as value relevant if it has a predicted association with equity market values." — the thesis's definition sentence is verbatim. The same source states the paper's abstract position ("value relevance research assesses how well accounting amounts reflect information used by equity investors, and provides insights into questions of interest to standard setters") and records Holthausen & Watts' conclusion ("value relevance research offers little or no insight for standard setting"). The Barth DOI is confirmed by the paper's printed PII S0165-4101(01)00019-2. The Holthausen DOI was **not** directly resolved in this task (a `doi.org` fetch failed and was not retried, per instructions); its volume/pages are confirmed by the Barth paper's own reference list ("Holthausen, R.W., Watts, R.L., 2001. … Journal of Accounting and Economics 31, this issue"), and the DOI follows the same PII pattern — but direct DOI resolution remains UNVERIFIED.
- **Citation counts in Chapter II:** `barth2001` cited 2×, `holthausen2001` cited 1×; both entries are cited, so neither is orphaned. Francis & Schipper (1999) and Kothari (2001) were not added; the loop records this as deliberate (not needed for the definition/debate paragraph). The finding as written — definition plus the Barth/Holthausen–Watts exchange — is satisfied without them.
- **Placement note (observation, not a finding):** the paragraph sits at the start of §2.2.2 (M&A valuation dynamics) rather than §2.2.1 (the RIV framework, where the term is first used at L105 of the old numbering). The placement is coherent — the definition frames the M&A question that follows — so no change is proposed.
- **Status:** VERIFIED except the Holthausen DOI resolution (UNVERIFIED as stated).

### 2.14 m36 (B-15) — HBL/NIMB swap ratios unverified — FIXED (verified correct; no patch needed)

- **Locations:** `src/thesis/chapters/chapter_02_literature_review.tex:208` (HBL) and `:210` (NIMB).
- **Current text (exact excerpts):** L208: "unified commercial operations commenced on 24 February 2023 (swap ratio 100:80.28) `\citep{hbl2023report}`." L210: "unified commercial operations commenced on 11 January 2023 (swap ratio 100:90) `\citep{nimb2023report}`."
- **Re-verification by this reviewer** (`pdftotext` on the repo-held cited reports):
  - HBL FY 2079/80 report: "erstwhile Civil Bank Limited at swap ratio of 80.28% and commenced joint operation for customers from 12th Falgun [2079]" — 100:80.28 confirmed.
  - NIMB FY 2079/80 report: "from 27th Poush 2079 by issuing 150,887,519 equity shares in the swap ratio of 100:90" — 100:90 confirmed.
- No patch was needed and none was made; the finding is closed by verification, not by editing. **Status:** VERIFIED.

### 2.15 m37 (B-14) — Pradhan & Dahal (2016) "168 obs" unconfirmed — NOT FIXED (deliberately; standing item)

- **Location:** `src/thesis/chapters/chapter_02_literature_review.tex:338` (Table 2.1).
- **Current text (exact excerpt):** "`\citet{pradhan2016}` & 14 Banks, 168 obs (2002--2014) & Pooled Panel OLS & …"
- The prose (L239–241) still states 14 banks over 2002/03–2013/14 with no observation count. The figure is arithmetically consistent (14 × 12 = 168) but that arithmetic is not a source confirmation, and no source confirmation was added: the loop log records m37 as "still unverified (author to confirm)" and the number was **not** silently replaced or re-justified. This reviewer did not open the Pradhan & Dahal SSRN paper, so the figure remains UNVERIFIED. Correctly left open; the author must confirm it against the source before submission.
- **Status:** VERIFIED as still unverified (thesis source read; no confirming text exists in the thesis).

### 2.16 s08 — Language and clarity (Chapter I) — NOT APPLICABLE to Chapter II

- The consolidated v2 finding s08 concerns Chapter I throughout (very long single-paragraph blocks, dense nominal style, evaluative adjectives). The loop log records its Chapter I patch under ROUND_1_A. No Chapter II language action was claimed, and none is needed for this scope: Chapter II's prose was read in full for Part B and no s08-type language defect in Chapter II was identified as a numbered finding. Not counted as fixed or unfixed for this scope.

### 2.17 s09 (B-13) — Alternative perspectives thin — NOT FIXED (open suggestion)

- **What would have closed it:** (a) a discussion of whether NFRS 9 / IFRS 9 adoption itself changes value relevance; (b) competing explanations for the EPS-vs-BVPS divergence (scale effects, conservatism, omitted correlated variables) weighed against the persistence explanation.
- **Current state (verified by grep over the full chapter):**
  - "NFRS 9" occurs once, at L112, only as a harmonisation task in mergers: "unifying impairment provisioning methodologies under NFRS 9 / IFRS 9". No discussion of IFRS/NFRS adoption as a value-relevance question exists anywhere in the chapter.
  - "scale effect", "conservatism", "omitted" (in the omitted-variables sense): 0 hits. The EPS-vs-BVPS divergence is still explained only through earnings persistence, non-recurring items, negative earnings, and intangible intensity (L113–115, L292–296).
- The loop log records s09 as "author input" (not patchable by the loop). It remains open as a Suggestion; it changes no claim or conclusion.
- **Status:** VERIFIED (absence verified by full-chapter grep).

---

## 3. Cross-checks re-run for Part B (thesis-internal consistency)

- **Two-way citation integrity:** 75/75, 0 orphans in either direction (re-run, §1.3). Chapter II cites 65 unique keys.
- **Synthesis counts:** 15 studies testing both EPS and BVPS (recomputed, §2.11); 19 rows flagged "Circular P/E inclusion" = 19 keys in each of the two §2.4.5/§2.5.2 lists (L297, L398) — reconciled.
- **Table 2.1 vs prose:** no row contradicts the prose on a finding. Spot-checks re-run in this task: Gurung & Subedi TA now in prose (L262) and table (L358); Niroula DY/ROA now in prose (L250) and table (L346); Bajracharya BR/Ln MC now in prose (L241) and table (L340); Sharma P/E/DY/DPR/size now in prose (L228) and table (L326); Gyawali GDP/INF now in prose (L252) and table (L348); Giri "40 obs claimed; ANOVA implies 36" in table (L354) matches prose (L258 area); Dahal "Dividend rate" label in table (L368) is explained in the table note (L386) as following Dahal et al.'s own label.
- **Ohlson derivation:** not re-derived in this task (v2 verified the algebra; no loop patch touched the equations — `git diff` shows no change to the equation block). Recorded as not re-checked, not as verified.
- **Reference-list rendering:** not checked (no build, per task rules). All APA 6th statements about rendered output in this review are therefore INFERRED from the `.bib` source, and are labelled as such where made.

---

## 4. PART B — New issues found in the fresh read

### N1 — Wilkinson (2016) article title still in Title Case after the m13 sentence-casing pass (loop-introduced residue; m13 partially fixed)

- **Location:** `src/thesis/references.bib` (`wilkinson2016fair`, title field).
- **Severity:** Minor. **Revision scale:** Narrow.
- **Status:** VERIFIED.
- **Evidence (exact excerpt):** "`title = {The {FAIR} Guiding Principles for scientific data management and stewardship}`".
- **Detail:** the m13 pass lowercased the rest of the title ("for scientific data management and stewardship") but left "Guiding Principles" capitalised. Under APA 6th sentence case the title should read "The {FAIR} guiding principles for scientific data management and stewardship". The loop's Round 1 log lists `wilkinson2016fair` among titles "already in sentence case", which is incorrect — only the braced acronym was protected. This is the single remaining article-title capitalisation defect in the file (all other 49 article titles verified sentence case, §2.7). `apacite` renders `.bib` titles as stored (braced words excepted), so this will appear in the rendered reference list as Title Case for those two words; that rendering consequence is INFERRED (no build performed).

### N2 — m11 residue: the Bhattarai (2014) sentence at L300 is now uncited at its point of use

- **Location:** `src/thesis/chapters/chapter_02_literature_review.tex:300`.
- **Severity:** Minor. **Revision scale:** Narrow.
- **Status:** VERIFIED.
- **Evidence (exact excerpt):** "Bhattarai (2014) measures equity share prices at fiscal-year-end (Ashadh-end / mid-July)."
- **Detail:** see §2.5. The redundancy and the repetition are fixed, but the sentence lost its citation instead of gaining a narrative `\citet{bhattarai2014}`. The claim (Bhattarai measured prices at fiscal-year-end) is supported elsewhere in the chapter (L237 `\citet{bhattarai2014}` paragraph states the same price measure), so nothing is unsupported in the chapter as a whole — the defect is local to this sentence. Fix: replace the plain-text "Bhattarai (2014)" with `\citet{bhattarai2014}`.

### N3 — Almumani (2014): the source's variable label "DP" has been standardised to "DPR" in both prose and table (loop-introduced label change)

- **Location:** `src/thesis/chapters/chapter_02_literature_review.tex:228` (prose) and `:330` (Table 2.1).
- **Severity:** Minor. **Revision scale:** Narrow.
- **Status:** VERIFIED (thesis source read; Almumani source checked via web search in this task).
- **Evidence (thesis excerpts):** L228: "Dividend per share and dividend payout (DPR) were also tested but had insignificant effects." L330 (Key Variables column): "Price, EPS, BVPS, P/E, DPS, DPR, Size".
- **Evidence (source):** the Almumani (2014) full text (International Journal of Business and Social Science 5(1), 91–104) regression table lists the variable as "DP" (B = 0.016, t = 0.251, Sig. 0.803) and its text states "other variables (DPS and DP) have insignificant impact on MP". A secondary summary glosses DP as "dividend payout per share". The v2 review (B-11) recorded the variable as "DP … a real variable in the source".
- **Detail:** "DPR" is the thesis's own abbreviation for dividend payout *ratio* (table note, L386: "DPR = dividend payout ratio"), used for Bhattarai (2014) and Gurung & Dahal (2025). Whether Almumani's DP is a ratio or a per-share amount is not stated in the material opened; the thesis now presents it as DPR in both places without noting the relabelling. The substantive claim (insignificant) is correct; only the label departs from the source. Fix: restore the source label "DP" in the Almumani row and prose sentence (with a brief gloss if needed), or add a note that the thesis standardises DP to DPR.

### N4 — Two plain-text author-year mentions without a citation command (pre-existing pattern, not loop-introduced; suggestion)

- **Locations:** `src/thesis/chapters/chapter_02_literature_review.tex:224` and `:300`.
- **Severity:** Suggestion. **Revision scale:** Narrow.
- **Status:** VERIFIED.
- **Evidence (exact excerpts):** L224: "Employing the Ohlson (1995) valuation framework, the authors addressed concerns …" L300: "Bhattarai (2014) measures equity share prices at fiscal-year-end (Ashadh-end / mid-July)."
- **Detail:** both are narrative author-year mentions with no `\citet` command. L300 is the m11 residue (N2); L224 predates the loop (present at HEAD) and was not flagged by v2. Both works are cited elsewhere in the chapter, so no entry is orphaned and no claim is unsupported at chapter level. Converting both to `\citet` would make the citation practice uniform. This is a style suggestion only.

### N5 — "Five major merged institutions" still counts a non-merged bank (remaining v2 finding M01/B-01, standing limitation — observed in the fresh read, not in the assigned Part A list)

- **Location:** `src/thesis/chapters/chapter_02_literature_review.tex:395` (§2.5.1) vs `:205–211` (§2.3.3).
- **Severity:** Minor. **Revision scale:** Narrow.
- **Status:** VERIFIED.
- **Evidence (exact excerpts):** L395: "altering reporting boundaries, asset bases, and capital structures across five major merged institutions." §2.3.3 names four merged entities (GBIME, HBL, Kumari, NIMB) plus NMB, which "Maintained continuous corporate operations without participating in the early-2023 consolidation wave, serving as the benchmark series" (L211). NMB is not a merged institution, so the five-item list in §2.3.3 does not support "five major merged institutions" in §2.5.1; the fifth early-2023 combination (Prabhu–Century, in Chapter I) is not named in §2.3.3.
- **Detail:** this is v2 Major M01's Chapter II instance (B-01). The loop log records M01 as a standing limitation requiring author input (the reason Prabhu was excluded from the sample is not stated anywhere in the thesis), and it was not patched. It is reported here as a remaining issue observed in the fresh read, not as a new finding and not as a verdict on the loop (the loop was barred from inventing the reason). The study's design (four merged banks plus NMB benchmark) is unaffected; only the count wording is inconsistent.

### N6 — Pre-existing DOI gap noted, not loop-introduced: `bajracharya2019` has no DOI although HEAD carried one (UNVERIFIED whether the DOI is valid)

- **Location:** `src/thesis/references.bib` (`bajracharya2019`).
- **Severity:** Suggestion (at most). **Revision scale:** Narrow.
- **Status:** UNVERIFIED.
- **Evidence:** the current entry has no `doi` field. `git diff HEAD` shows HEAD carried `doi = {10.3126/njmsr.v2i1.36868}`, removed in the uncommitted working tree before v2 (v2 §6.4 already listed `bajracharya2019` among the ten article entries without a DOI). A web search for that DOI string in this task returned no confirming record for this article, so whether the DOI is valid (and the removal a loss) or invalid (and the removal correct) could not be established. No error is asserted; the author should check the DOI against the journal record. This is recorded so the removal is not mistaken for a loop action.

**Part B tally: 6 items — 3 Minor (N1, N2, N3), 1 Minor remaining/stale (N5), 1 Suggestion (N4), 1 Suggestion-level open check (N6, UNVERIFIED).** No Critical or Major issue was found in the fresh read. No new issue changes a claim, a conclusion, or the chapter's argument.

---

## 5. What could not be verified

1. **Pradhan & Dahal (2016) "168 obs" (m37).** The SSRN paper was not opened in this task. The figure (Table 2.1, L338) is arithmetically consistent (14 × 12) but unconfirmed against the source. Author to confirm.
2. **Source-level accuracy of the loop's added prose sentences for Sharma (2011), Bajracharya (2019), Niroula (2021), Gyawali (2022), and Gurung & Subedi (2024) (m18).** Their sources were not opened in this task. Thesis-internal prose/table consistency was verified for all six; the Almumani sentence was checked against its source (see N3). The remaining five added sentences rely on the loop log's assertion that they were verified against abstracts/full texts — not re-verified here.
3. **Almumani (2014) bank count / observation count.** The loop log records a secondary-source claim of "seven Jordanian banks and 49 observations" (Pandey & Sunar) against v2's "not stated" (v2 opened the full text). The Almumani full text was not re-opened in this task; the "not stated" flag was kept. Author to confirm against the full text.
4. **Holthausen & Watts (2001) DOI** (`10.1016/S0165-4101(01)00029-5`). Volume/pages confirmed via the Barth paper's reference list; direct DOI resolution was not completed (a `doi.org` fetch failed and was not retried). The DOI follows the same PII pattern as the confirmed Barth DOI, but that is inference, not resolution.
5. **Whether the HEAD DOI for `bajracharya2019` (10.3126/njmsr.v2i1.36868) is valid** (N6). Web search in this task returned no confirming record. The other eight article entries without DOIs were not checked for DOI existence either (as in v2 §8.2); absence of a DOI field is not treated as an error for any of them.
6. **Rendered output.** No build was performed (per task rules). Reference-list alphabetisation, hanging indents, italics, `et al.` rendering, and the `apacite` rendering of the 53-author Wilkinson entry and of the sentence-cased titles are CANNOT DETERMINE from source alone. Findings that depend on rendering (notably N1's visible effect) are labelled INFERRED where they go beyond the `.bib` source.
7. **Ohlson derivation algebra.** Not re-derived in this task; v2 verified it and no loop patch touched the equation block (confirmed by diff). Recorded as not re-checked.
8. **Gap-claim completeness.** The "no study has tested the regime shift" claim (§2.5.1) is verified only within the reviewed corpus, as in v2 (C-18). A search outside that corpus was outside this review's scope.
9. **Chapter II page count vs the FOM Guidelines' "10 to 20 pages should suffice" guide.** Cannot be determined without a build.

---

## 6. Verification log

**Read in full during this task:**
- `src/thesis/chapters/chapter_02_literature_review.tex` (410 lines).
- `src/thesis/references.bib` (746 lines; 75 entries).
- `docs/thesis_review/v2/content_review.md` §10 (finding table) and `docs/thesis_review/v2/review_ch2_refs.md` (B-01–B-15, §§1–9) — read to extract the assigned findings, not as evidence.
- `docs/thesis_review/v2/verification_audit.md` — read for the corrected counts (m17) and verdicts.
- `~/workspace/review-audit-scratch/loop-v2/LOOP_STATUS.md`, `ROUND_1_B.md`, `ROUND_3.md`, `ROUND_4.md` — read only for the loop's claimed fixes, not as evidence.

**Counts re-run by script in this task:** 75 `.bib` keys; 75 unique cited keys across the thesis; 65 unique keys in Chapter II; 0 cited-but-missing; 0 uncited; 26 Table 2.1 rows; 19 "Circular P/E inclusion" flags = 19 keys in each P/E list; 15 studies testing both EPS and BVPS (manual resolution of the Kwon `\&` and Giri "Net Worth Per Share" rows); 10 "not stated in the reviewed source" flags; Wilkinson 53 authors; braces 627/627; "and others" 0 hits.

**Sources opened in this task (thesis-external):**
- Repo-held reports via `pdftotext`: NMB FY 2077/78 annual report (Kanchan: 23 August 2020; 496,765,500; swap 1:0.85; 13% bonus shares); HBL FY 2079/80 annual report ("swap ratio of 80.28%"); NIMB FY 2079/80 annual report ("swap ratio of 100:90").
- Web search: Barth et al. (2001) full text (definition verbatim, p. 79; abstract position; Holthausen & Watts conclusion; Barth PII S0165-4101(01)00019-2); Almumani (2014) full text (regression table: DP B = 0.016, p = 0.803; "DPS and DP have insignificant impact"); Chhetri (2023) NepJOL page (author "Raja Chhetri", *Quest Journal of Management and Social Sciences* 5(1), 107–118, DOI 10.3126/qjmss.v5i1.56298 — confirming the working tree's "Chhetri, Raja" against HEAD's "Chhetri, Rajan Thapa", which was wrong).
- Attempted and not completed: direct `doi.org` resolution of the Holthausen DOI (fetch failed, not retried); web search for the Bajracharya DOI 10.3126/njmsr.v2i1.36868 returned no confirming record.

**Not read:** anything else under `~/workspace/review-audit-scratch/` beyond the four loop files listed above; `docs/thesis_review/v1/`; Chapters I, III, IV, V (searched only by the grep counts reported above where a cross-chapter fact was needed, e.g. `nmb2021report` citations); appendices; the rendered PDF (no build performed).

**Git status confirmation (run after writing this file):** HEAD `2b4e10f`. `git status --porcelain` shows the pre-existing set of modified tracked files unchanged apart from this review's single new untracked file. **The only file this review created is `docs/thesis_review/v3/review_ch2_refs.md`.** No repo file was created, modified, renamed, deleted, or reformatted by this review. Scratch text extractions were kept in `/tmp` only (`/tmp/hbl.txt`, `/tmp/nimb.txt`, `/tmp/nmb.txt`).
