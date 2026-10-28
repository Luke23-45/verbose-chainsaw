# Chapter II — Literature Review: review

- Chapter reviewed, in full, word by word: `docs/draft/thesis/chapter_02_literature_review.md`, 251 lines.
- Repository HEAD at review time: `9a46350`.
- LaTeX counterpart used for sync-spotting only: `src/thesis/chapters/chapter_02_literature_review.tex`, 352 lines.
- Evidence sources used: `src/thesis/references.bib` (55 entries), `docs/draft/thesis/chapter_03_research_methodology.md` (Ohlson derivation and model equations), `docs/draft/thesis/chapter_01_introduction.md` and `docs/draft/thesis/chapter_04_results_and_discussion.md` (consistency of what the literature is claimed to support).
- This review changed nothing in the thesis. No thesis file, table, figure, or data file was edited, moved, or deleted to write it. The only file written is this review.
- Line numbers below are lines of the Markdown chapter, unless a line is explicitly identified as a `.tex` line.
- Classification used throughout, exactly as assigned: MUST-FIX means a wrong derivation, a wrong citation, a finding misattributed, or a claim contradicted by the bibliography or by Chapters 1, 3, or 4. MINOR means wording, grammar, repetition, or slop. A passage not listed as an issue was either checked and found correct, or is listed in the "NOT checked" section at the end. No issue was invented to fill a quota.

## Passes run, and what each pass actually did

- Pass 1 — full read for argument: read all 251 lines in order, mapped every section to the gap it is supposed to support, and checked the gap list against Chapters 1, 3, and 4.
- Pass 2 — line-by-line proofread: read every line again for grammar, duplicated words, broken sentences, wrong terminology, and inconsistent citation style. Parenthetical `&` versus narrative `and` was checked against APA convention, not assumed to be an error.
- Pass 3 — every citation checked against `references.bib`: author, year, journal, volume, pages, and DOI where the bib entry gives them. Every specific numeric finding attributed to a paper (sample size, observation count, coefficient, percentage) was checked against what the bib entry actually establishes. Where the bib entry does not establish it, the finding is flagged as "needs check against the paper's full text" and is NOT claimed verified.
- Pass 4 — Ohlson derivation re-derived by hand from the clean-surplus / dividend-discount setup stated in the chapter, step by step, and compared with Chapter 3's model equations.
- Pass 5 — slop hunt: every sentence was tested for whether deleting it loses any specific content. Meta comments about the chapter, vague praise, and repetition are quoted verbatim.
- Pass 6 — LaTeX sync, spot-check only: passages flagged in Passes 1–5 were searched in the `.tex` version. This was NOT a full LaTeX diff, and this review does not claim the two versions are otherwise identical.

## Pass 1 verdict: the argument, in brief

The chapter does build to the gap; it is not only a list of papers. That is its main strength, and it should be said plainly before the faults.

The chain is: Ohlson (section 2.2.1) gives EPS and BVPS as the two pricing inputs; Kwon and Wang (2.2.2) gives the mechanism by which a merger should move weight between them; the P/E circularity section (2.2.6) gives the specification rule; the BAFIA section (2.3.2) gives the price-timing rule; the empirical sections (2.4.1–2.4.4) show that Nepalese results disagree with each other on EPS versus BVPS; and the gap section (2.5) then maps five gaps onto five design choices — regime interaction, no P/E, MPS_RD timing, entity-timing sensitivity, HC3 with disclosed degrees of freedom. Gap 1 maps to Chapter 1 hypotheses H3/H4 (interaction slopes), Gap 2 to the exclusion rule, Gap 3 to MPS_RD, Gap 4 to the sensitivity exclusions, and Gap 5 to the HC3-t inference and the $28 - 14 = 14$ df accounting. That mapping is real, and it matches Chapters 1, 3, and 4.

Two structural weaknesses, both MINOR, limit that strength:

- Sections 2.2.3 (dividend capitalization), 2.2.4 (signaling, agency, opacity), and 2.2.5 (EMH) are context, not tested theory. Nothing in them generates a hypothesis that Chapters 3 or 4 test. The only bridges offered are that DPS is a robustness variable (line 87) and that timing matters (line 100). A reader can fairly ask why three subsections of theory are present when the estimated model contains only EPS, BVPS, and their Post interactions. Either add one sentence per subsection stating exactly which design choice it justifies, or trim them. This is not a factual error; it is an argument-economy fault.
- The chapter never states hypotheses H1–H4 itself. Gap 1 (line 236) mentions $\beta_E$ and $\beta_B$ and the two periods, but a reader of Chapter II alone does not learn that Chapter I tests them two-tailed. That matters because Gap 1's wording is directional (see MINOR-11 below), while Chapter I's tests are explicitly two-tailed. The chapter should either name H1–H4 or explicitly say the interaction test is two-tailed.

## Pass 4 verdict: the Ohlson derivation is correct

I re-derived every step from the setup the chapter itself states. All of the following check out exactly, and no derivation step is flagged as wrong:

- PVED, line 24: $P_t = \sum_{\tau=1}^{\infty} E_t[D_{t+\tau}] / (1+r)^\tau$. Correct.
- CSR, lines 29–31: $BV_t = BV_{t-1} + NI_t - D_t$, hence $D_t = NI_t - (BV_t - BV_{t-1})$. Correct.
- Residual income, line 36: $NI_t^a = NI_t - r \cdot BV_{t-1}$. Correct.
- RIV form, line 38, under the stated transversality condition. Correct.
- LID, lines 42–43: $NI_{t+1}^a = \omega NI_t^a + v_t + \epsilon_{1,t+1}$ and $v_{t+1} = \gamma v_t + \epsilon_{2,t+1}$, with $0 \le \omega < 1$ and $0 \le \gamma < 1$. Correct as stated.
- Closed form, lines 47–48: $P_t = BV_t + \alpha_1 NI_t^a + \alpha_2 v_t$ with $\alpha_1 = \omega / (R_f - \omega)$ and $\alpha_2 = R_f / ((R_f - \omega)(R_f - \gamma))$, $R_f = 1 + r$. Correct.
- Substitution, lines 50–51: $BV_{t-1} = BV_t - NI_t + D_t$, hence $NI_t^a = (1+r)NI_t - r \cdot BV_t - r \cdot D_t$. Correct: $NI_t - r(BV_t - NI_t + D_t) = NI_t + rNI_t - rBV_t - rD_t$.
- Collected form, lines 55–56: $P_t = (1-k)BV_t + k(\phi \cdot NI_t - D_t) + \alpha_2 v_t$ with $k = r\alpha_1 = r\omega / (R_f - \omega)$ and $\phi = R_f / r = (1+r)/r$. Correct: $k\phi = \alpha_1(1+r)$, and $k(\phi NI_t - D_t) = \alpha_1(1+r)NI_t - \alpha_1 r D_t$, matching the line 53 expansion.
- Coefficients, lines 59–61: $(1-k) = (1+r)(1-\omega)/(1+r-\omega) > 0$ and $k\phi = \omega(1+r)/(1+r-\omega) > 0$, given $r > 0$ and $\omega < 1$. Correct.
- Empirical equation, line 64: $P_{it} = \beta_0 + \beta_1 EPS_{it} + \beta_2 BVPS_{it} + \varepsilon_{it}$. This matches Chapter 3's Model 1 (Chapter 3, line 217: $MPS^{RD}_{it} = \alpha + \mu_i + \lambda_t + \beta_E EPS_{it} + \beta_B BVPS_{it} + \varepsilon_{it}$) up to the fixed effects, which Chapter 2 does not claim to derive, and the interaction form in Chapter 3, line 234, adds $\delta_E$ and $\delta_B$ exactly as Gap 1 requires. No contradiction between Chapters 2 and 3 was found in the model equations.

Two derivation-adjacent wording faults remain, both MINOR, neither a broken algebra step:

- MINOR-D1, line 65: "where earnings per share ($EPS_{it}$) serves as the empirical proxy for abnormal earning capacity". After the line 50–55 substitution, the structural coefficient is on contemporaneous net income $NI_t$, not on abnormal earnings $NI_t^a$; the abnormal-earnings effect is already folded into the book-value coefficient $(1-k)$. EPS proxies $NI_t$ in this form, not $NI_t^a$ directly. Reword to "serves as the empirical proxy for contemporaneous earnings" or explain the folding explicitly.
- MINOR-D2, line 63: "impounds dividend effects into the constant and error term". That is a frank statement of an omission, not an error, but it sits uneasily with line 87 and the DPS robustness specification: dividends are omitted from the baseline and then reintroduced as a regressor. The chapter should say in one sentence why that sequence is legitimate (baseline follows Collins et al.; DPS is a sensitivity, not a structural term), rather than leaving the reader to notice the tension.

## MUST-FIX issues

### MUST-1 — A paper cited in a footnote has no bibliography entry at all

Chapter line 196:

> "*(Note: Gurung and Dahal (2025) in Pravaha is distinct from Dahal, Gurung, and Ghimire (2025) in the Interdisciplinary Journal of Management and Social Sciences, which evaluated 209 observations across all listed commercial banks).*"

There is no entry in `references.bib` for Dahal, Gurung, and Ghimire (2025). The bib contains `gurungdahal2025` (Gurung and Dahal, Pravaha, vol. 31(1), pp. 1–12, DOI 10.3126/pravaha.v31i1.89145) and `gurung2024` (Gurung and Subedi), but a search of the whole bib file returns no Dahal–Gurung–Ghimire entry, no Interdisciplinary Journal of Management and Social Sciences 2025 entry for that author set, and no 209-observation source. The footnote therefore cites a paper the reader cannot look up, and its one specific number — 209 observations — is established by nothing in the repo. Fix by adding a complete, verified bib entry for that paper and confirming the 209 figure from its full text, or by deleting the footnote's second half. Do not keep the number on the strength of this chapter alone.

### MUST-2 — The Chaitra deadline is stated as statutory, contradicting Chapter 3's corrected framing

Chapter line 129:

> "Because commercial bank fiscal years in Nepal terminate at Ashadh-end (mid-July), counting nine months into the subsequent financial year (from Shrawan through Chaitra) establishes the end of Chaitra (mid-April) as the statutory publication deadline."

Chapter 3, as corrected in the current HEAD, is careful to say the statute requires publication within nine months into the subsequent fiscal year and that end-of-Chaitra is the study's operationalization of that period; the statute does not name Chaitra. Chapter 2 line 129 says the opposite in effect: that counting the nine months "establishes" Chaitra-end "as the statutory publication deadline". The same paragraph then correctly calls it an operationalization, so the paragraph contradicts itself as well as Chapter 3. Fix line 129 to: counting nine months gives a period ending at Chaitra-end, which this study operationalizes as the observation cutoff. The Shrawan-through-Chaitra count itself (nine months inclusive) is correct and is not disputed.

### MUST-3 — Merger dates and swap ratios are cited to a source that cannot support them; the Kanchan amount is cited to the same source

Chapter lines 138–141 cite each merger's date and swap ratio to a bank filing plus `(NRB, 2023)`, for example line 138:

> "**Global IME Bank Limited (GBIME):** Amalgamated with Bank of Kathmandu Limited; unified commercial operations commenced on 9 January 2023 (swap ratio 1:1) (Global IME Bank, 2022; NRB, 2023)."

The bib entry behind `(NRB, 2023)` is `nrb2023list`: "List of Banks and Financial Institutions Licensed by Nepal Rastra Bank (as of Mid-October 2023)". A list of licensed institutions as of October 2023 does not, by its title or content as recorded in the bib, establish a January 2023 commencement date or a 1:1 swap ratio, and it does not establish the other three mergers' dates and ratios either. The bank filings (`gbime2022agm`, `kumari2022sgm`, `hbl2023report`, `nimb2023report`) are the correct source type for dates and ratios. Fix by citing dates and ratios to the bank filings alone, and reserving `(NRB, 2023)` for the claim it can support, namely the October 2023 bank population in line 144 (whose count itself still needs checking against the list document; see the "needs check" list below).

The same fault, sharper, is line 142:

> "(Note: NMB had previously acquired Kanchan Development Bank Limited in August 2020, adding approximately NPR 0.57 billion to share capital in FY 2077/78, but remained independent during the 2023 wave) (NRB, 2023)."

The October 2023 NRB list cannot establish an August 2020 acquisition or a NPR 0.57 billion share-capital addition in FY 2077/78. Either cite the NMB annual report or acquisition filing that actually records those facts, or delete the amount and date and keep only the qualitative point that NMB did not merge in 2023. The NPR 0.57 billion figure is not verified by anything in the bib and must not stand on this citation.

### MUST-4 — No fourth MUST-FIX was found, and that is stated deliberately

For the avoidance of doubt: after Passes 3 and 4, no other citation was found to be contradicted by its bib entry, and no other derivation step was found to be wrong. The remaining citation problems are unverified attributions (listed below as "needs check against the paper's full text"), not proven misattributions, and they are not promoted to MUST-FIX on suspicion alone. Inventing a fourth MUST-FIX would itself be a review error.

## MINOR issues

### Proofread and terminology

- MINOR-P1, line 20: "The mathematical foundation of the Ohlson framework rests on three interrelated structural building blocks:" — the chapter then numbers four blocks (PVED, CSR, residual income, LID, lines 22, 27, 34, 40). Change "three" to "four". This passage also appears in the `.tex` version (line 25), so fix both.
- MINOR-P2, line 125: "Specifically, Section 59(2) delineates two distinct reporting duties stated in subsection (2):" — "delineates" and "stated in subsection (2)" say the same thing twice. Delete one half. Same wording in the `.tex` version (line 185).
- MINOR-P3, line 93: "standardized regulatory reporting ceilings indispensable for credible market valuation." — "reporting ceilings" has no defined meaning in this chapter. If "standards" or "requirements" is meant, use that word. The same phrase appears in the `.tex` version (line 139).
- MINOR-P4, line 92: "In commercial banking, mandatory cash dividend distributions and transparent audited balance sheets mitigate agency conflicts…" — cash dividends in Nepalese banking are board-proposed and subject to NRB approval; they are not shown in this chapter to be mandatory. This is flagged as a wording check, not as a proven falsehood: reword to "declared cash dividend distributions" unless a source for mandatory distribution is produced. Same wording in the `.tex` version (line 138).
- MINOR-P5, line 76: "the stock of tangible net assets—book value per share (BVPS)". BVPS as computed in this thesis is total equity divided by shares outstanding; it is not restricted to tangible assets, and post-merger book value includes goodwill and purchase-price adjustments (line 74 itself mentions goodwill). Delete "tangible" or replace with "net assets". Same wording in the `.tex` version (line 112).
- MINOR-P6, line 111: "Rearranging this equation reveals that $MPS_{it}$ is being regressed on a linear transformation of itself." — $MPS_{it}/EPS_{it}$ is a ratio involving $MPS_{it}$, not a linear transformation of $MPS_{it}$ alone. Replace "a linear transformation of itself" with "a function of itself". The circularity argument itself is correct; only this phrase overstates its form. Same wording in the `.tex` version (line 168).
- MINOR-P7, line 67: "they serve as mathematically necessary and theoretically complementary inputs in equity pricing." — "mathematically necessary" is too strong: Ohlson shows EPS and BVPS enter under the stated LID assumptions, not that no other valuation representation is possible. Replace "mathematically necessary" with "theoretically motivated". Same wording in the `.tex` version (line 100).
- MINOR-P8, line 65, see MINOR-D1 above (EPS as proxy for abnormal earning capacity). Listed once, here and in Pass 4, to avoid double-counting.
- Citation style, checked and found CORRECT, not an issue: narrative citations use "and" ("Gurung and Dahal (2025)", line 196), parenthetical citations use "&" ("(Gurung & Dahal, 2025)", lines 236, 239), and table rows use "&" ("**Gurung & Dahal (2025)**", line 225). That is standard APA convention, not inconsistency, and no fix is needed. Likewise, "Collins, Maydew, and Weiss (1997)" on first mention (line 153) followed by "Collins et al. (1997)" (lines 76, 78) is correct.

### Argument, consistency, and table-vs-prose faults

- MINOR-A1, line 236, directional wording versus two-tailed tests: "major corporate amalgamations impair earnings persistence through integration costs and loan harmonization, leading rational markets to shift valuation weight toward balance-sheet equity." Chapter 1 (lines 65, 82–91) states the interaction hypotheses are tested two-tailed without imposing directional signs, and Chapter 4 (lines 379–382) reports that book value did not in fact serve as an anchor in this sample (implied post slope −1.658). Chapter 2's sentence reads as a prediction that the shift will occur. Soften to "predicting a possible shift" or add "tested two-tailed" in Gap 1, so Chapter 2 does not appear to pre-commit to the direction Chapter 4 then reports against.
- MINOR-A2, line 250: "this dissertation directly bridges each of the identified gaps in the literature." — "directly bridges" overstates what the results as reported in Chapter 4 establish: the baseline joint Wald test does not reject at 5% (Chapter 4's reported $F = 2.954$, $p = 0.085$), and the regime-shift evidence is sensitivity-dependent. Replace "directly bridges" with "addresses" or "is designed to address".
- MINOR-A3, Table 2.1 completeness: the table is introduced at line 205 as "a structured, comparative synthesis of the key empirical studies reviewed", but it omits studies given full prose paragraphs — Bajracharya and Sawagvudcharee (2019, line 168), Gurung and Subedi (2024, line 187), Niraula, Shilpakar, and Shrestha (2026, line 200), Bhandari, Pradhan, and Ghimire (2026, line 200), Bhattarai (2024, line 200), and Dongol and Shrestha (2024, line 200) — and it omits the international studies Malhotra and Tandon (2013) and Almumani (2014) (line 157). "Key" gives latitude for selection, but the selection criterion is never stated. Either add the omitted rows or add one sentence stating the table covers a selected subset and why those studies were selected. Do not present the table as if it were the full reviewed set.
- MINOR-A4, Table 2.1 "Circular P/E" tags are inconsistent with the chapter's own gap list. The table tags Bhattarai (2014), Chhetri (2023), Joshi et al. (2023), Pant et al. (2024), and Timalsina (2026) with "(Circular P/E)", but not Giri (2024, line 222) or Gurung & Dahal (2025, line 225), although both rows list P/E among the variables examined and Gap 2 (line 239) explicitly lists both Giri (2024) and Gurung & Dahal (2025) among the P/E users. Add the tag to both rows or remove the tag convention and rely on Gap 2 alone.
- MINOR-A5, Table 2.1 versus prose, Gurung & Dahal (2025): prose line 196 says dividend payout ratio (DPR), P/E, EPS, BVPS, and ROA all exerted statistically significant impacts; table line 225 lists DPR among the variables but its findings column says only "EPS, BVPS, ROA, and P/E are significant", dropping DPR. Restore DPR to the findings column or explain its omission.
- MINOR-A6, Table 2.1 versus prose, Timalsina (2026): prose line 198 says firm size and inflation were significantly positive and GDP growth insignificant; table line 226 omits firm size, inflation, and GDP entirely. The table is a summary, so omission alone is not an error, but a summary that drops two significant variables misleads. Add them or mark the findings column as abbreviated.
- MINOR-A7, line 166, internal inconsistency in one paragraph: "The authors analyzed the impact of firm size, earnings per share, return on assets, and dividend per share on market equity valuation. Their empirical findings identified bank size and EPS as the most consistent and statistically significant positive determinants of share prices, while macroeconomic variables exhibited secondary explanatory power." — macroeconomic variables were not in the list of variables just analyzed. Either macroeconomic variables were also analyzed and should be added to the list, or the second sentence's claim about them should be deleted or sourced.
- MINOR-A8, headings overlap: section 2.4.3 is headed "(2021–2024)" and section 2.4.4 "(2024–2026)", so 2024 papers appear in both sections (for example Chhetri/Giri/Gurung & Subedi in 2.4.3 and Pant in 2.4.4). The organising criterion is evidently "spans the consolidation wave" versus "does not", not year alone. Rename the headings to say so, for example "(2021–2024, pre-wave samples)" and "(2024–2026, wave-spanning samples)", or the overlap will look like a filing error.
- MINOR-A9, line 213, table-only variable: the Kwon & Wang (2020) table row lists "Post Dummy" among the variables, but prose line 155 describes only a "panel spanning pre- and post-merger observations" and never mentions a post dummy. The table entry may be correct, but it is not established by anything in this chapter or in the bib entry (whose title mentions SFAS 141(R) only). Confirm from the paper's full text or delete "Post Dummy" from the table row.

### Slop hunt (Pass 5) — quoted verbatim, each deletable with no loss of specific content

- SLOP-1, line 5: "A rigorous literature review serves as the intellectual cornerstone of academic inquiry: it establishes the theoretical mechanisms through which accounting metrics map into market valuations, traces the historical evolution of empirical methodologies, identifies contradictions and divergences in prior findings, and illuminates the unaddressed conceptual and empirical boundaries that constitute the research gap." — a meta comment about the chapter itself. The chapter's actual mechanisms, history, contradictions, and gap follow in the sections themselves; this sentence adds no specific content. Delete it.
- SLOP-2, line 67: "The theoretical implications of the Ohlson framework are profound for banking research." — vague praise with no specific implication attached; the specific implications follow in the same paragraph. Delete the sentence or replace it with the first specific implication.
- SLOP-3, line 117: "Understanding this regulatory architecture is vital for contextualizing corporate reporting disclosures, merger timelines, and observation windows:" — a meta justification for the section. The section's content justifies itself. Delete it.
- SLOP-4, line 233: "A critical and systematic evaluation of the theoretical foundations, regulatory frameworks, and empirical literature reveals several profound conceptual, methodological, and econometric gaps that directly motivate this dissertation:" — "critical", "systematic", and "profound" are self-praise, and the gaps follow immediately below. Delete the adjectives or the sentence.
- SLOP-5, line 151: "International empirical research across developed and emerging capital markets provides extensive documentation regarding the association between financial accounting disclosures and equity valuation:" — a throat-clearing sentence that says only that literature exists. The studies follow. Delete it.
- Not slop, and not flagged: the Kwon and Wang discussion appears twice (theory, lines 72–76; empirical, line 155) and the Collins discussion appears twice (theory, line 78; empirical, line 153). That repetition is structural — theory section versus empirical section — and each occurrence adds different content (mechanism versus finding). Deleting either would lose content, so neither is listed as slop.

### Pass 3: citation-by-citation result

- Bib entries match the text for author, year, journal, volume, pages, and DOI where the bib gives them, for: Ohlson (1995, Contemporary Accounting Research 11(2), 661–687); Feltham and Ohlson (1995, same journal 11(2), 689–731); Collins, Maydew, and Weiss (1997, Journal of Accounting and Economics 24(1), 39–67, DOI 10.1016/S0165-4101(97)00015-3); Kwon and Wang (2020, Accounting & Finance 60(3), 2717–2757, DOI 10.1111/acfi.12411); Miller and Modigliani (1961); Gordon (1959); Walter (1963); Ross (1977); Bhattacharya (1979); John and Williams (1985); Jensen and Meckling (1976); Jensen (1986); Morgan (2002); Fama (1970); Ball and Brown (1968); Beaver (1968); Bernard and Thomas (1989); Cameron, Gelbach, and Miller (2008, Review of Economics and Statistics 90(3), 414–427); MacKinnon and White (1985, the HC3 source, Journal of Econometrics 29(3), 305–325); and every Nepalese empirical paper listed in the "needs check" paragraph below, insofar as author and year are concerned. No author-year mismatch was found between text and bib for any cited paper except the missing Dahal–Gurung–Ghimire entry (MUST-1) and the "2023cbr" formatting point below.
- The Companies Act, 2006 (line 123) has no bib entry, while BAFIA 2017 does (`bafia2017`). Either add a Companies Act entry or cite it as a statute without a bib entry consistently; as it stands the two statutes are treated differently without explanation. MINOR.
- Formatting point, Markdown only: line 202, "Adhikari, Kavanagh, and Hampson (2023cbr)". "2023cbr" is the bib key (`adhikari2023cbr`), not a citation year. In the `.tex` version this passage is a proper citation command, `\citet{adhikari2023cbr}`, so the compiled thesis may render correctly; but the Markdown draft as written reads as if the year were "2023cbr". In the Markdown, write "Adhikari, Kavanagh, and Hampson (2023)" and disambiguate the two Adhikari papers by title or by 2023a/2023b if the style requires it. MINOR, because the `.tex` rendering is not shown to be wrong.
- Formatting point, Markdown only: line 196, "Gurung and Dahal (2025) investigated ten commercial banks … (Pravaha, vol. 31(1), pp. 1–12).* Among the studies reviewed…" followed by "*(Note: …).*". The stray asterisk after "1–12)." and the inline italic note are a Markdown conversion artefact: the `.tex` version (line 271) renders this correctly as a `\footnote{…}`. Fix the Markdown to match the `.tex` footnote, and do not "fix" the `.tex`, which is already correct. MINOR.
- The bib header comment (lines beginning "All metadata below was verified against the publisher record…") is a bib-internal note, not chapter text, and is not counted as a chapter issue. The bib contains two entries not cited in Chapter II (`flannery2004`, `pant2016`); uncited bib entries are not a Chapter II fault, and no action is required on that account in this chapter.

### Pass 3: specific findings that are NOT verified by the bib and must be checked against the papers' full texts

The bib entry for each of these papers gives author, journal, and pages, but not the sample size, period, method, or finding the chapter attributes to it. None of the following is claimed verified in this review, and none is claimed false. Each must be confirmed from the paper itself before submission, because an examiner will check the most prominent ones first:

- Collins et al. (1997), line 153: "across thousands of firm-year observations" — bib gives no observation count.
- Sharma (2011), line 157: BSE 30, 1993/94 to 2007/08, pooled OLS and panel, EPS/BVPS/DPS significant — bib gives journal and pages only.
- Malhotra and Tandon (2013), line 157: 95 firms, NSE 100, 2007 to 2012 — bib gives title "NSE 100 companies" but no count of 95 and no period.
- Almumani (2014), line 157: Amman Stock Exchange banks, 2005–2011 — bib gives title and pages only, no period.
- Pradhan (2003), line 162: listed enterprises, 1992–1997, descriptive and correlational, cash dividends stronger than retained earnings — bib is a book chapter with no period, method, or finding recorded.
- Bhattarai (2014), line 164: 14 banks, 35 pooled bank-year observations, 2006 to 2014 — bib gives journal and pages only. Note the arithmetic that makes this check urgent: 14 banks over 2006–2014 cannot yield 35 observations in a balanced panel, so the 35 must come from an unbalanced or restricted sample that the chapter never explains. Confirm the 35 and the reason for it from the paper, or the number will look like an error even if it is correct.
- Pradhan and Dahal (2016), line 166: 14 banks, 2002/03 to 2013/14, pooled panel — bib is an SSRN paper with no sample recorded.
- Bajracharya and Sawagvudcharee (2019), line 168: ten banks, 2006/07 to 2015/16, pooled OLS, EPS/DPS significant, ROA/ROE insignificant — bib gives journal and pages only.
- Silwal and Napit (2019), line 170: ten banks, 100 observations, FY 2065/66 to 2074/75 — internally consistent (10 × 10 = 100), but the bib gives no sample, so the count itself is still unchecked against the paper.
- Niroula (2021), line 175: 18 banks, 90 observations — internally consistent (18 × 5 = 90), unchecked against the paper.
- Gyawali (2022), line 177: ten banks, 50 observations — internally consistent (10 × 5 = 50), unchecked against the paper.
- Chhetri (2023), line 179: 13 banks, 143 observations — internally consistent (13 × 11 = 143), unchecked against the paper.
- Joshi, Ghimire, and Singh (2023), line 181: seven banks, 70 observations — internally consistent (7 × 10 = 70), unchecked against the paper.
- Giri (2024), line 185: four banks, 40 observations — internally consistent (4 × 10 = 40), unchecked against the paper. The bib entry (Journal of Advanced Academic Research 11(1), 12–23, DOI 10.3126/jaar.v11i1.65518) matches author and year, but not the sample.
- Gurung and Subedi (2024), line 187: 16 banks, 171 observations, 2007 to 2023, stepwise regression — 171 is less than a balanced 16 × 17 = 272, so an unbalanced panel is implied but never explained; bib gives journal and pages only.
- Pant, Joshi, and Saud (2024), line 192: seven banks, 77 observations — internally consistent (7 × 11 = 77), unchecked against the paper.
- Chaudhari (2025), line 194: ten banks, 100 observations — internally consistent (10 × 10 = 100), unchecked against the paper. The chapter's causal gloss ("equity investors penalized low-margin asset expansion") is an interpretation of a negative ROA coefficient, not a finding quoted from the paper; keep it labelled as interpretation or source it.
- Gurung and Dahal (2025), line 196: ten banks, FY 2013/14 to 2023/24, Hausman test, bank fixed effects, DPR/P/E/EPS/BVPS/ROA significant — bib gives journal and pages only; the Hausman claim and the significance list are unchecked against the paper.
- Timalsina (2026), line 198: 13 banks, 169 observations — internally consistent (13 × 13 = 169), unchecked against the paper. The bib entry (The Management Review 2(1), 305–316, DOI 10.3126/tmr.v2i1.96931) matches author and year, but not the sample.
- Niraula, Shilpakar, and Shrestha (2026), line 200: 16 banks, 80 observations — internally consistent (16 × 5 = 80), unchecked against the paper.
- Bhandari, Pradhan, and Ghimire (2026), line 200: "census study of all 19 NEPSE-listed commercial banks" — bib gives journal and pages only, no bank count, no period, no observation count. The "all 19" figure is the least sourced specific number in the contemporary section and must be confirmed from the paper.
- Bhattarai (2024), line 200: "evaluated capital adequacy regulations and commercial bank performance" — bib title is "Bank Regulations and Earnings Per Share of Commercial Banks in Nepal: An Observation". "Capital adequacy" is a narrowing of "bank regulations" that the bib title does not establish. Confirm from the paper or revert to "bank regulations and earnings per share".
- Dongol and Shrestha (2024), line 200: "investigated corporate governance mechanisms and financial stability" — bib title says "Performance of Nepalese Commercial Banks", not "financial stability". Confirm from the paper or revert to "performance".
- Adhikari, Kavanagh, and Hampson (2023), lines 202 and 227: seven merged banks, 2013 to 2020, post-merger price declines, reduced dividends, high EPS volatility, no immediate synergies — bib gives journal and pages for both Adhikari papers but no sample, period, or finding. Unchecked against the papers.
- Collins et al. (1997), line 78 and table line 212: described as a "forty-year empirical panel" / "Ohlson RIV Panel OLS". The bib gives a 1953–1993 span, which supports "forty-year", but it does not establish that the estimation was a panel regression as opposed to annual cross-sections. Confirm the method label from the paper before keeping "Panel OLS" in the table.
- Regulatory and institutional specifics, lines 120, 129, 134–135, 144, 100: Securities Exchange Centre sponsorship and 13 January 1994 trading start (cited to NEPSE, 2017, a souvenir publication — plausible source type, unchecked against that publication); boards "typically" releasing highlights between Ashwin and Poush (line 129, no citation at all); the 2015 capital mandate from NPR 2.0 billion to NPR 8.0 billion (line 134, cited to NRB, 2015, whose bib entry is only the Monetary Policy document title — amounts unchecked); moral suasion, CD-ratio and branch-overlap forbearance, and Finance Act tax exemptions (line 135, no citation at all); "exactly 20" banks by mid-October 2023 (line 144, cited to the NRB list — count unchecked against the list itself); illiquidity, retail-dominated trading, delayed filings, and the absence of a unified announcement timestamp registry (line 100, no citation at all); and the Ashadh-end pricing claim for Bhattarai (2014), Pradhan & Dahal (2016), and Silwal & Napit (2019) in Gap 3 (line 242) — none of those three prose paragraphs states a price date, so the claim is unchecked against those papers. None of these is claimed false; every one of them needs either a citation or a softening to "in the studies reviewed" / "as operationalized here".

## Pass 6 verdict: LaTeX sync, spot-check only

Flagged passages were searched in `src/thesis/chapters/chapter_02_literature_review.tex`. Results, passage by passage:

- Present in both versions, fix both: "three interrelated structural building blocks" (`.tex` line 25); "mathematically necessary" (`.tex` line 100); "tangible net assets" (`.tex` line 112); "linear transformation of itself" (`.tex` line 168); "most concentrated" (`.tex` line 337); "mandatory cash dividend distributions" and "reporting ceilings" (`.tex` lines 138–139); the Chaitra and Group passages were not re-checked line-by-line in `.tex` for this review beyond the passages listed here, and no claim is made about them.
- Markdown-only faults, `.tex` already correct: the Gurung and Dahal footnote is a proper `\footnote{…}` in `.tex` (line 271) and a broken inline italic note in Markdown (line 196); the Adhikari companion citation is a proper `\citet{adhikari2023cbr}` command in `.tex` (line 277) and reads as the year "2023cbr" in Markdown (line 202). Fix the Markdown in both cases; do not "fix" the `.tex`.
- Sync difference in the other direction: the `.tex` opacity paragraph (line 139) cites both Morgan (2002) and Flannery (2004), while the Markdown paragraph (line 93) cites Morgan (2002) alone. The bib contains `flannery2004` (Journal of Financial Economics 71(3), 419–460). Either the Markdown dropped a citation in conversion, or the `.tex` added one after the Markdown was frozen. Reconcile the two versions so the same claim carries the same citations.
- This was a spot-check, not a full diff. No claim is made that the `.tex` and Markdown versions are otherwise identical.

## Passes 1–5: passages checked and found correct (brief, as assigned)

- The Ohlson algebra, lines 24–61: correct in every step (see Pass 4).
- The P/E circularity algebra, lines 105–111: correct except for the single phrase flagged in MINOR-P6. The definitional identity $P/E = MPS/EPS$ and the endogeneity conclusion follow.
- The BAFIA nine-month count, Shrawan through Chaitra inclusive: nine months, correct. The fault is only the word "statutory" attached to Chaitra-end (MUST-2).
- Internal arithmetic of observation counts, where the chapter gives both banks and years: Silwal & Napit 10 × 10 = 100; Niroula 18 × 5 = 90; Gyawali 10 × 5 = 50; Chhetri 13 × 11 = 143; Joshi 7 × 10 = 70; Giri 4 × 10 = 40; Pant 7 × 11 = 77; Chaudhari 10 × 10 = 100; Timalsina 13 × 13 = 169; Niraula 16 × 5 = 80. All multiply out. That checks arithmetic, not the papers themselves; see the "needs check" list.
- Merger dates and swap ratios as stated (GBIME 9 January 2023, 1:1; HBL 24 February 2023, 100:80.28; KBL 1 January 2023, 1:1; NIMB 11 January 2023, 100:90) are consistent with Chapter 1 and Chapter 3 and with the bank-filing bib entries. The fault is only the added `(NRB, 2023)` citation (MUST-3), not the dates or ratios themselves.
- Citation style for narrative versus parenthetical "and"/"&" is correct (see MINOR section).
- The gap-to-design mapping (Gap 1 → interaction, Gap 2 → no P/E, Gap 3 → MPS_RD, Gap 4 → sensitivity, Gap 5 → HC3/df) matches Chapters 1, 3, and 4.

## Verdict

The chapter is substantively sound in its theory and its argument, and unsound in its citation hygiene. The Ohlson derivation is correct, the gap structure is real, and the model equations agree with Chapter 3. What would get this chapter marked down by an examiner is not the theory but the references: one cited paper is missing from the bibliography entirely, two specific claims are cited to a source that cannot support them, one statutory claim contradicts Chapter 3's own corrected framing, and a long tail of specific sample sizes and findings is asserted without any source in the repo that establishes them. Fix the MUST-FIX items first, then work through the "needs check" list paper by paper — starting with Bhattarai (2014)'s 35 observations and Bhandari (2026)'s "all 19" — and only then treat the chapter as submission-ready. The MINOR items are real but none of them, alone, would fail the chapter; the MUST-FIX items, left as they are, would each be a legitimate examiner objection.

## Fix list, in priority order

1. MUST-1: Add a verified bib entry for Dahal, Gurung, and Ghimire (2025) and confirm the 209-observation figure from its full text, or delete the footnote's second half (line 196).
2. MUST-3 (Kanchan half first, because it is a number): Source the August 2020 Kanchan acquisition and the NPR 0.57 billion figure (line 142) from the NMB report or acquisition filing, or delete the date and amount.
3. MUST-3 (merger half): Cite merger dates and swap ratios (lines 138–141) to the bank filings alone; reserve (NRB, 2023) for the October 2023 bank population (line 144), and confirm the "exactly 20" count against the NRB list itself.
4. MUST-2: Reword line 129 so Chaitra-end is the study's operationalization of the nine-month rule, not "the statutory publication deadline". Apply the same wording in the `.tex` version.
5. MINOR-P1: "three" → "four" building blocks (line 20, both versions).
6. MINOR-A4 and MINOR-A5: Fix Table 2.1 — add "(Circular P/E)" to the Giri (2024) and Gurung & Dahal (2025) rows, and restore DPR to the Gurung & Dahal findings column (lines 222, 225).
7. MINOR-A3 and MINOR-A6: Either complete Table 2.1 with the omitted prose studies or state its selection criterion in one sentence; add firm size, inflation, and GDP to the Timalsina row or mark the column abbreviated (lines 205, 226).
8. MINOR-P3, P4, P5, P6, P7: Replace "reporting ceilings" (line 93), "mandatory cash dividend distributions" (line 92, unless sourced), "tangible net assets" (line 76), "linear transformation of itself" (line 111), and "mathematically necessary" (line 67), in both versions where the passage appears in both.
9. MINOR-A1 and MINOR-A2: Soften Gap 1's directional shift wording to a two-tailed prediction (line 236) and replace "directly bridges" with "addresses" (line 250).
10. MINOR-A7 and MINOR-A8: Resolve the macroeconomic-variables sentence in the Pradhan & Dahal paragraph (line 166) and rename the 2.4.3/2.4.4 headings so the 2024 overlap is explained (lines 172, 189).
11. MINOR formatting, Markdown only: Repair the Gurung footnote asterisks (line 196) to match the `.tex` footnote, and write the Adhikari companion citation without the bib key "2023cbr" (line 202). Reconcile the Flannery (2004) citation in the opacity paragraph between Markdown (line 93) and `.tex` (line 139).
12. MINOR-D1/D2: Reword the EPS-proxy sentence (line 65) to contemporaneous earnings, and add one sentence explaining why dividends are omitted from the baseline and reintroduced as a DPS sensitivity (lines 63, 87).
13. SLOP-1 to SLOP-5: Delete the five quoted slop sentences (lines 5, 67 first sentence, 117, 151, 233 first sentence).
14. Paper-by-paper verification, in this order: Bhattarai (2014) 35 observations and its sample construction; Bhandari (2026) "all 19"; Timalsina (2026) 169; Gurung & Dahal (2025) Hausman and significance list; the 2015 capital mandate amounts; the Finance Act incentives and CD-ratio forbearance claims (line 135, currently uncited); the Ashadh-end pricing claim for Bhattarai, Pradhan & Dahal, and Silwal & Napit (line 242); and then the remaining "needs check" items in the Pass 3 list. Do not mark any of them verified until the paper itself has been read.
15. Companies Act, 2006 (line 123): add a bib entry or explain the different treatment from BAFIA 2017.

## NOT checked

- The full text of any cited paper, journal article, bank annual report, NRB document, or NEPSE publication. Every "needs check" item above is unchecked for exactly this reason, and no finding attributed to a paper is claimed verified in this review unless the bib entry itself records it (author, year, journal, volume, pages, DOI).
- The full LaTeX diff between the Markdown chapter and the `.tex` chapter. Pass 6 was a spot-check of flagged passages only.
- Chapters 1, 3, and 4 in full. They were consulted only for the passages cited above (hypotheses and two-tailed framing in Chapter 1; model equations in Chapter 3; Wald result and Kwon/Ohlson reconciliation in Chapter 4). Nothing in this review certifies those chapters.
- The thesis data, tables, figures, or analysis pipeline. Those were reviewed in the earlier Phase 1 data review and are not re-certified here.
- Whether the "to the best of the researcher's knowledge" claim in Gap 1 (line 236) is exhaustively true across all Nepalese literature. It is scoped to "the extensive corpus of studies reviewed" in this chapter, and this review checked only that corpus.
- The rendered PDF of the thesis. Line numbers, footnote rendering, and citation rendering in the PDF may differ from the Markdown and `.tex` sources checked here.

## LOOP ADDENDUM (2026-10-28, 10-pass loop, see 07_loop_log.md)

- Bhattarai (2014) UPGRADED from "needs full-text check" to
  PROVEN ERROR, new must-fix item 14: paper read in full
  (NEPJOL, EJDI 17 & 18, pp. 187-198). Sample is 9 named
  banks, 2006-2014, variables DPR, DY, EPS, P/E, SIZE.
  No BVPS, no DPS, no "35 observations" anywhere in the
  paper. Rewrite the paragraph (line 164) and Table 2.1 row.
  The circular-P/E point about Bhattarai stands.
- Dahal, Gurung & Ghimire (2025) 209 VERIFIED from the
  publisher abstract (IJMSS 6(1), DOI
  10.3126/ijmss.v6i1.75407, FY2013/14-2023/24, all listed
  banks). Must-fix item 2 is now "add the entry" (pages
  252-261 to confirm against the publisher PDF).
- BAFIA Section 59(2) text read: audited duty is
  PUBLICATION within nine months, not submission to NRB
  (new must-fix item 15), and section 2.3.2 contains a
  third Chaitra error ("establishes the end of Chaitra as
  the statutory publication deadline").
- Ohlson derivation re-derived step by step: CORRECT.
- LaTeX citation system: 55/55 consistent; Dahal 2025 is
  the ONLY missing entry by surname+year check.
- LaTeX-only Flannery 2004 in the opacity paragraph
  confirmed (.tex line 139 vs Markdown line 93).
