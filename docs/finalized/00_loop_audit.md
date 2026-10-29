# Loop audit — the five finalized reviews checked against docs/instructions

**Date:** 2026-10-29. **Thesis version:** HEAD 8c96edc.
**What this file is:** a second-order audit. It does NOT change
any thesis chapter, table, figure, or bib entry, and it does NOT
edit the five review files in `docs/finalized/` — it records,
with evidence, which of their claims survive re-checking, which
were wrong, and what they missed. Items marked **Addition**
below are to be appended to the fix list; they are not yet in
the review files, and applying any of them to the thesis still
needs the author's approval, in both Markdown and LaTeX where
the passage appears in both.

**Standard:** `docs/instructions/instructions_for_paper.md`
in full — §1 theory, §2 Traps 1–8, §3 skim/roadmap, §4
literature, §5 sample/data, §6 tables/robustness, §7 prose,
§8 Chapter V, §9 formatting, §10 25-point rubric.
The instructions' illustrative numbers (§6.2, §8.2) were not
used as a check standard, as in the reviews themselves.

## Method — four passes, in order

- **Pass A — Coverage mapping.** Each instructions section
  and each rubric item was mapped to the chapter review(s)
  that were supposed to cover it, to find sections no review
  covered at all.
- **Pass B — Must-fix re-verification.** Every must-fix in
  reviews 01–05 (12 total) was re-checked against the chapter
  text by grep / direct reading, in both versions where the
  passage appears in both.
- **Pass C — Miss hunt.** Systematic sweeps across ALL five
  chapters, in both versions, for: prohibited vocabulary
  (including word stems, not just exact forms), "crucial
  role", "verified" claims, causal verbs, Chaitra/statutory
  wording, "during merger" wording, welfare/standard-setting
  claims, anthropomorphism, table-row counts and
  observation counts, and sample-proportion disclosure.
- **Pass D — Formatting (§9).** `src/thesis/main.tex` and
  `src/thesis/front/*.tex` were read for margins, typeface,
  sizes, spacing, paragraph layout, pagination, and front-
  matter order. No compiled PDF was produced in this loop,
  so compile-dependent claims are recorded as unverified,
  not as passes (see Open items).

## Headline verdict — strict and honest

- **The five reviews are substantially sound, but NOT
  complete.** All 12 must-fix items survive re-checking in
  substance (one line-number citation is corrected below).
  No must-fix was found to be false, and no chapter number
  was found to be wrong in the reviews.
- **The loop found 1 new must-fix-level addition, 3 new
  prose minors the reviews missed, and 2 corrections to
  review claims.** The most serious miss is not a prose
  word: it is a whole instructions requirement (§5.1 sample
  proportion) that no chapter meets and no review flagged
  as its own item.
- **Two scope gaps remain open and must not be read as
  passes:** (1) full-text verification of most literature
  studies, and (2) a full 57-entry bibliography audit.
  The reviews verified a small, named subset; the loop
  quantifies that subset below so nobody mistakes it for
  a complete audit.
- **Revised fix-list totals after this loop:** must-fix
  12 → **13** (one addition); minors 25 → **28** (three
  additions); plus 2 corrections to review text and 3 open
  items that are questions, not errors.

## Pass B — every original must-fix, re-verified

| # | Review item | Loop result |
|---|---|---|
| Ch1-1 | No core-finding paragraph (§3.1) | **UPHELD.** Grep: Ch1 contains zero coefficient values, zero Wald F, zero slope p-values; "Wald" only as a method name (Objective 2) and in the §1.7 Ch IV preview. |
| Ch1-2 | Opening order (§3.2) | **UPHELD.** §1.1 para 1 RIV theory, para 2 market history, puzzle in para 4. No sentence in paras 1–2 was listed as false, and the loop agrees. |
| Ch1-3 | Merger dates cited to (NRB, 2023) | **UPHELD in substance, line numbers CORRECTED** (see Correction C1). Dates are correct; the licensed-institutions list cannot support them. |
| Ch1-4 | Sector-dominance sentence, no proportion | **UPHELD.** No proportion in Ch1. See also Addition A1 (a different proportion, sample-vs-sector, missing in Ch3). |
| Ch2-1 | Dahal (2025) bib title/authors wrong | **UPHELD.** Publisher title/authors (NEPJOL, DOI 10.3126/ijmss.v6i1.75407) vs. bib title/authors differ; journal/vol/pages/DOI match. |
| Ch2-2 | Table 2.1 fails §4.2 | **UPHELD, recount exact.** Table rows counted by script: **17 rows**; only Giri's Sample cell gives total observations ("40 obs"); no critique column; six prose studies absent from the table (Bajracharya, Lamsal, Gurung & Subedi, Niraula, Bhandari, Dahal). Adhikari (2023) IS in prose (§2.4, merger paragraph) and in the table — correctly not listed as missing. |
| Ch2-3 | Catalogue, not dialectic (§4.1) | **UPHELD.** §2.4 is chronological (international / foundational / recent / contemporary); §2.4.5 heading "Synthesis" introduces only Table 2.1, with no synthesis discussion. |
| Ch2-4 | "pivotal" (§7.1) | **UPHELD.** Exactly 1 hit, §2.2.2 opening, both versions (md line 70; tex line 105 in the review's count). |
| Ch3-1 | Merolagani scope ("target date") | **UPHELD.** A4 compares dataset prices on dataset dates, including delayed resumption dates HBL 2022-06-06 and NIB 2022-05-30; Ch3 §3.4.3 says "on the target date" / "30 target cells". |
| Ch4 | (no must-fix) | **UPHELD as "none found" — with one exception found in Pass C** (see Addition A2, which is a prose minor, not a number/model must-fix; the "no must-fix" verdict on numbers, models, and causal claims stands). |
| Ch5-1 | Implications in 5 domains, not 3 (§8.3) | **UPHELD.** Headings counted: 5.4.1 NRB, 5.4.2 SEBON/NEPSE, 5.4.3 executives, 5.4.4 investors, 5.4.5 academic/standard-setters. §5.1 intro lists 4 groups — also not 3. |
| Ch5-2 | Hypothesis decisions as list, not table (§8.2) | **UPHELD.** §5.3.5 is a numbered list; substance matches Table 4.5 exactly (loop re-checked H1–H4 + joint values). |
| Ch5-3 | "During merger processes" in §5.4.2 | **UPHELD.** Exactly 1 surviving hit, md line 130 / tex line 151, both versions. |

## Additions — what the reviews missed (add to the fix list)

### Addition A1 — MUST: §5.1 sample-proportion disclosure is missing everywhere (Ch3 review miss)
- **Rule:** §5.1, second bullet: "Document the proportion
  of aggregate sector assets, equity, or market
  capitalization represented by the sampled institutions
  to substantiate sectoral relevance."
- **Evidence (grep-verified):** Chapter III contains NO
  proportion disclosure at all — grep for percent / share /
  proportion in Ch3 returns only the ROA percentage
  definition. Chapter III gives population (20) and sample
  (5 series), so a count proportion (5/20 = 25% by number)
  is derivable, but no assets/equity/market-cap share is
  stated anywhere in Ch3, and no chapter states the
  sampled banks' share of sector assets or market cap.
- **Why the reviews missed it:** Ch3's review recorded the
  §5.1 hurdle list as a pass and deferred "proportion" to
  Ch1 Must-fix 4 — but Ch1 Must-fix 4 is a DIFFERENT
  proportion (the banking sector's share of NEPSE), not
  the sample's share of the banking sector. Both are
  missing; only one was flagged.
- **Fix:** Add to Chapter III (§3.3.1 or §3.3.2) the sampled
  five banks' share of aggregate Class 'A' sector assets
  (and, if available, equity/market cap) for a stated
  reference year, sourced to NRB statistics, or state
  explicitly that only the count share (5 of 20) is claimed
  and that assets share was not computed. Do not invent
  an assets share from the panel alone — the panel has
  only the five banks, not the sector total.

### Addition A2 — Minor: "underscores" in Chapter IV (§7.1, Ch4 review miss)
- **Rule:** §7.1 prohibited list includes "underscores"
  (replacement: indicates, reveals, demonstrates, highlights).
- **Evidence (grep-verified, both versions):** Ch4 §4.3.5,
  point 2 (md line 423, tex line 576): "The exclusion of
  HBL and NIMB for FY 2077/78 underscores an institutional
  friction in Nepalese capital markets."
- **Why the review missed it:** Ch4's prose pass listed
  grep counts for delve, pivotal, testament, beacon,
  tapestry, paramount, "game changer", multifaceted,
  myriad, "it is important to note", utilize, facilitate —
  "underscores" was not in that grep list at all. The
  review's claim of a clean §7.1 pass for Ch4 is therefore
  wrong on this word.
- **Fix:** Change to "highlights" (or "illustrates").
  The same sentence's "extended merger processes" wording
  is NOT separately flagged here: it matches the
  merger-related-processes form the Ch4 review passed,
  and the loop does not upgrade it to a second error.

### Addition A3 — Minor: "crucial role" in Chapter V (§7.1, Ch5 review miss)
- **Rule:** §7.1 table row "paramount / crucial role"
  (replacement: substantial, significant, necessary,
  foundational).
- **Evidence (grep-verified, both versions):** Ch5 §5.3.3
  (md line 101, tex line 119): "This dissertation
  highlights the crucial role of econometric specification
  in evaluating accounting value relevance in frontier
  markets."
- **Why the review missed it:** Ch5's prose pass grepped
  "paramount" but not the phrase "crucial role" — a
  phrase-level prohibited item cannot be caught by a
  single-word grep for "paramount" alone.
- **Fix:** Change to "highlights the substantial influence
  of econometric specification" (or "the central importance"
  — "central" is the §7.1 replacement for "pivotal", not
  for this row; "substantial" is the listed replacement).

### Addition A4 — Minor: six "utiliz*" forms in Chapter II (§7.2, Ch2 review miss)
- **Rule:** §7.2: "use" instead of "utilize" (and its
  inflected forms).
- **Evidence (stem grep `utiliz*`, both versions):**
  Ch2 has **6** instances, all "Utilizing ..." at sentence
  starts in study summaries: Kwon & Wang (line 155),
  Sharma (157), Bajracharya (168), Joshi (181), Pant (192),
  Timalsina (198). Ch2's review claimed "utilize /
  facilitate: 0" — that claim is FALSE, because it grepped
  the exact form "utilize", which does not match
  "utilizing".
- **Fix:** Change each "Utilizing ..." to "Using ..."
  (e.g., "Utilizing pooled OLS" → "Using pooled OLS").
  This is a prose minor, not a factual error — but it
  means Ch2's §7.2 pass must be corrected, not just
  supplemented.
- **Same stem error, corrected count, in Ch3:** Ch3's
  review Minor M4 said grep count 3 and "at least 1
  instance". The stem count is **4** (lines 16
  "utilizing", 108 "utilized", 180 "utilizes", 186
  "utilized"). The minor was flagged, so this is a
  count correction, not a new item — but the fix must
  cover all four, not one.
- **Stem counts for the other chapters (loop-verified):**
  Ch1 = 1 ("utilizes", line 32 — as reviewed, correct);
  Ch4 = 0 (as reviewed, correct); Ch5 = 1 ("utilize",
  line 148 — as reviewed, correct). Facilitat* = 0 in
  all five chapters (as reviewed, correct).

## Corrections to review text (no thesis change implied)

### Correction C1 — Ch1 review line numbers for Must-fix 3 are wrong
- Ch1's review cites the merger-dates sentence as
  ".md line 26, .tex line 28". In the current files those
  lines are the pooled-OLS paragraph, not the merger
  sentence. The merger sentence is in the long §1.1
  paragraph: **md line 9, tex line 11** (verified by
  searching within those long lines: "Global IME Bank
  absorbed Bank of Kathmandu (9 January 2023);
  Himalayan Bank acquired Civil Bank (24 February 2023);
  Kumari Bank absorbed NCC Bank (1 January 2023); and
  Nepal Investment Bank amalgamated with Mega Bank Nepal
  to form NIMB (11 January 2023) (NRB, 2023)" / tex
  `\citep{nrb2023list}`).
- The must-fix itself is unaffected (dates correct,
  citation cannot support them; the "exactly 20" sentence
  in the same paragraph correctly keeps (NRB, 2023)).
  Lesson recorded: line numbers for long-paragraph
  chapters are fragile — future review citations should
  give section + quoted phrase, not line number alone.

### Correction C2 — Ch4 review §7.1 pass and Ch2/Ch5 prose passes are overstated
- Ch4's §7.1 pass is corrected by Addition A2
  ("underscores").
- Ch2's §7.2 pass is corrected by Addition A4
  (six "utilizing" forms).
- Ch5's §7.1 pass is corrected by Addition A3
  ("crucial role").
- No other prose-pass claim was found false: full stem
  sweeps in this loop confirm delve/delving 0, showcase*
  0, testament 0, beacon 0, tapestry 0, paramount 0,
  "game changer" 0, multifaceted 0, myriad 0,
  "it is important to note that" 0, pivotal 1 (Ch2 only,
  already flagged), "crucial role" 1 (Ch5 only, Addition
  A3), "underscores" 1 (Ch4 only, Addition A2).

## Pass D — §9 formatting: what the reviews scoped out, now checked

**Source settings PASS (verified in `main.tex`):**
- Margins: top/bottom/right 2.54 cm, left 3.18 cm
  (`geometry`, line 13) — exactly §9.1.
- Typeface: Times New Roman (`fontspec` /
  `\setmainfont`), 12 pt document class — §9.1.
- Chapter headings `\large\bfseries` (≈14.4 pt at 12 pt
  base, within 14–16 pt), section headings
  `\normalsize\bfseries` (12 pt) — §9.1.
- Line spacing: `\setstretch{1.5}`, paragraph layout
  flush left (`\parindent` 0 pt) with `\parskip` 10 pt —
  §9.1.
- Tables: `tabular`/`longtable` forced
  `\singlespacing`; TOC/LOT/LOF groups
  `\singlespacing` — §9.1.
- Pagination: front matter Roman, bottom center
  (`frontmatter` style, page counter set to 2, title
  counted as i unnumbered); main body Arabic, top right
  (`mainbody` style, page counter reset to 1 at
  Chapter I) — §9.2.
- Front-matter order in `main.tex`: Title → Authorship
  (Certification) → Research Committee → Approval Sheet
  → Acknowledgements → TOC → LOT → LOF →
  Abbreviations → Abstract — matches §9.3 order
  EXCEPT for the Declaration question below.
- Abstract: 340 words, 5 keywords listed — within the
  single-page / ≤5-keyword shape (§9.3 item 10) on word
  count, but page fit is compile-dependent (see Open).
- Citations mechanism: `apacite` with `natbibapa`,
  `\citet`/`\citep` used throughout — §10 rubric 24
  mechanism passes; CONTENT does not yet (see Open).

**NOT verified by this loop (compile-dependent):**
- Single-page fit for Certification, Viva-Voce/Research
  Committee, Approval Sheet, Acknowledgements, Abstract
  (each file starts with `\clearpage`, but fit needs a
  compiled PDF — no thesis PDF exists in the repo; only
  figure PDFs were found).
- 0-error compilation (rubric 25) — not attempted in
  this loop; the thesis has not been compiled here.

## Open items — questions, NOT errors (do not add to the fix list as must-fix)

### Open O1 — Front-matter Declaration of Authenticity
- §9.3 item 4 requires "Declaration of Authenticity
  (strictly single page)". The thesis front matter has
  "Report of Research Committee" and "Approval Sheet"
  but NO file titled Declaration of Authenticity.
  Whether TU FOM 2019 as applied by the author's
  institution requires a separate Declaration, or whether
  Approval Sheet / Research Committee covers it, was
  NOT established in this loop. **Action:** author to
  confirm against his institution's actual front-matter
  template before submission. Do not add or delete a
  front-matter section on the basis of the instructions
  file alone.

### Open O2 — Bibliography audit is incomplete (57 entries, ~7 checked)
- Bib entries verified in the finalized phase (content,
  not just existence): Dahal (2025) — wrong, flagged;
  Gurung & Dahal (2025) — abstract-verified; Giri (2024)
  — journal verified; Kwon & Wang (2020) — verified;
  Timalsina (2026) — bib verified, findings not;
  Bhandari (2026) — bib verified, findings not.
  The remaining ~50 entries (including Sharma, Malhotra,
  Almumani, Pradhan, Pant, Gyawali, Niroula, Bajracharya,
  Chhetri, Joshi, Bhattarai 2024, Pant 2024, Dongol,
  Adhikari ×2, Chaudhari, Gurung & Subedi, Niraula,
  Lamsal, and all theory/methods references) were NOT
  audited entry-by-entry in the finalized reviews.
  Rubric 24 (APA 6th) therefore cannot be marked YES
  for the whole bib yet. This is a scope limit, not a
  claim that those entries are wrong.

### Open O3 — Literature full-text verification is incomplete
- Full-text verified: Bhattarai (2014) only.
  Abstract-verified: Dahal (2025), Gurung & Dahal (2025).
  All other study summaries (including Timalsina's 169
  obs, Bhandari's "all 19" census, Pradhan & Dahal's
  Ashadh-end pricing, Silwal's Ashadh-end pricing, and
  the P/E-inclusion attributions for Chhetri/Joshi/Pant/
  Giri/Lamsal) remain internally consistent with Chapter
  II's own paragraphs but NOT externally verified in the
  finalized phase. The reviews correctly listed these as
  unverified; the loop confirms that listing was complete
  for the studies named, and adds no new unverified study
  to it.

## Checked-now passes (loop considered these, found no miss)

- **§1.1 welfare/standard-setting claims:** sweep for
  optimal / welfare / "efficiency verified" across all
  chapters: 0 hits. No leap from β ≠ 0 to optimality is
  made anywhere. (The reviews did not explicitly sweep
  §1.1; the loop did, and it passes.)
- **§3.2 roadmap:** Ch1 §1.7 entries preview intellectual
  purpose for each chapter (background/problem, theory,
  design, findings, synthesis), not bare titles. Passes
  §3.2's "not merely its title" rule. (Opening-order
  failure in Ch1 Must-fix 2 is a separate §3.2 issue and
  stands.)
- **§6.1 table-note completeness, Ch4:** Table 4.6 df
  gap was already Ch4 Minor M5; all other Ch4 table
  notes give estimator, HC3, N, and df or residual df
  in the table itself. No further table-note gap found.
- **Figure 4.1 continuous lines through excluded periods:**
  checked against the F6 note, which explicitly discloses
  "the connecting lines pass continuously through the
  excluded periods; the open markers designate observations
  excluded from regression estimation". Disclosure is
  honest; no instructions rule requires broken lines, so
  this is recorded as a pass, not a new minor.
- **Anthropomorphism (§7.2):** sweep for data/tables/
  regressions as agents ("data speak", "table believes",
  "regression finds"): hits are benign academic usage
  ("research documents divergence", "Table provides a
  synthesis") — not the prohibited forms. Pass.
- **Causal verbs (§2 Trap 7):** sweep for caused /
  "mergers improved" / "consolidation caused" across all
  chapters: only Ch1 §1.1 "restructuring induced by the
  2023 consolidation wave" (historical event, not a
  regression effect — already passed in the Ch1 review).
  No new causal creep found.
- **Chaitra/statutory wording:** sweep across all chapters
  confirms the Ch4 Minor M2 spots and the Ch5 correct
  template; no additional statutory-Chaitra claim was
  found in Ch1, Ch2, or Ch3 beyond those already flagged
  or passed.
- **Rubric items 1–14 (econometrics/data):** all covered
  by Ch3/Ch4 reviews and upheld in Pass B, except rubric
  11's bib/table/code match for literature numbers (see
  Open O2/O3) and rubric 14's EPS–ROA VIF upper bound
  (already a minor in Ch3/Ch4/Ch5 reviews, now with the
  corrected stem counts above).

## Revised totals

- **Must-fix: 13** (original 12 + Addition A1).
- **Minors: 28** (original 25 + Additions A2, A3, A4).
- **Corrections to review text: 2** (C1 line numbers;
  C2 prose passes) — these correct the reviews, not the
  thesis.
- **Open questions: 3** (O1 front-matter Declaration;
  O2 bib audit scope; O3 literature full-text scope).
- **Thesis files changed by this loop: NONE.**
  **Review files changed by this loop: NONE** — additions
  and corrections above are recorded here for the author
  to approve before they are appended to reviews 01–05
  or applied to the thesis.
