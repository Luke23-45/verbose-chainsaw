# 04 — Examiner checklist

What thesis examiners actually assess, per the examiner-preparation
literature (Golding et al. 2014; Man 2020; McGill's published evaluation
criteria; Pat Thomson's "how an examiner reads a thesis"), converted into
a checklist for THIS thesis. Every item is written so it can be checked
by grep, by reading one section, or by recomputation.

The headline behaviors from the literature:

- Examiners **start with the conclusions and the abstract** and look for
  a clearly stated contribution before reading anything else (Thomson).
- They then **jump between chapters checking consistency** — of numbers,
  terminology, and claims (Golding et al.).
- Recurring failure themes in master's examiner reports: weak or absent
  research questions, literature summarized rather than synthesized,
  methodology narrated without justification, results without
  interpretation, conclusions outrunning the findings, and presentation
  slips that undermine trust in the whole (Man 2020; Golding et al.).
- Examiners judge whether the thesis is **the student's own work of
  adequate standard**, not whether it is publishable — precision and
  honesty weigh more than ambition (Golding et al.).

---

## A. First-read checks (abstract + Chapter V first)

| # | Check | Status | How to verify |
|---|---|---|---|
| A1 | Abstract states purpose, method, findings, implication; ≤ 1 page; ≤ 5 keywords | MET | front/abstract.tex; 5 keywords; one page |
| A2 | The contribution is stated in one sentence a non-specialist could repeat | MET | §5.3 and §1.1 carry the same contribution: first regime-interaction evaluation of EPS/BVPS value relevance across Nepal's 2023 consolidation wave with a reproducible reporting-deadline price protocol — verify the wording stays aligned when editing |
| A3 | Conclusions name what was learned, not what was done | MET | §5.3's conclusions carry findings + meaning; no chapter recitation |
| A4 | Hypotheses are decided by name | MET | Table 11 (H1–H4, joint, R6 row); §5.3.6 |
| A5 | Abstract numbers match Chapter IV/V | MET | 2.095/0.616; 5.577/0.140; 2.954/0.085; 5.82/0.021 — recheck after every rebuild |

## B. Cross-chapter consistency checks (examiner sampling behavior)

| # | Check | Status | How to verify |
|---|---|---|---|
| B1 | Sample: N = 28 (13/15) identical in I, III, IV, V, abstract | MET | grep "N = 28" / "13 pre" / "15 post" |
| B2 | Headline estimates identical in I (preview), IV (tables/text), V (Table 11) | MET | 2.095 (4.096); 0.219 (1.858); 5.577 (3.560); 0.100 (1.306); −3.124 (4.003); −1.758 (1.231); F(2,14) = 2.954, p = 0.085; F(2,10) = 5.82, p = 0.021 |
| B3 | Suite naming identical ("eight-specification estimation and robustness suite (R1–R2 baselines plus six robustness variants R3–R8)") | MET | I §1.7, III §3.6.5, IV §4.2.6, V §5.2.1 |
| B4 | One concept, one term (MPS^RD; consolidation wave; entity-timing mismatch; merger-related suspension) | MET | re-grep before submission; no "during merger negotiations" or "merger processes" residues |
| B5 | No later-chapter claim strengthening | MET | the governing rule in file 02; last violation fixed ("verified parameter stability") |
| B6 | Cross-references resolve and are \ref-based, not hardcoded numbers | MET | 4 conversions applied 2026-11-02; new sections must carry labels |

## C. Question-and-argument checks

| # | Check | Status | How to verify |
|---|---|---|---|
| C1 | Research questions explicit, answerable, and closed by the thesis | MET | RQ1–RQ3 close §1.2; answered by number in §5.3.1 |
| C2 | Each objective uses a performable verb and maps to a method | MET | estimate/test/evaluate → Model 1, Model 2 + joint test, R1–R8 |
| C3 | The literature chapter synthesizes (themes, debates, gap) rather than listing | MET | §2.2 by theory; §2.4.5 four debates; §2.5 five evidenced gaps; Table 2.1 with Critique column |
| C4 | The gap claimed is genuinely empty "within the reviewed literature" | MET | hedged formulations ("no empirical study identified in the literature reviewed in Chapter II") — keep the hedge scope in any edit |
| C5 | Every methodological choice names its alternative | MET | purposive vs probabilistic; no imputation vs imputation; HC3 vs cluster SEs; P/E exclusion algebra |
| C6 | Every claim proportionate to evidence (hedging ladder) | MET, 2 watch items | file 02 §2: "monumental scale" (V §5.2.1), "catastrophic multicollinearity" (I §1.5) |

## D. Presentation checks (trust multipliers)

| # | Check | Status | How to verify |
|---|---|---|---|
| D1 | No meta-comments, TODOs, placeholders, or code names in the rendered PDF | MET | full-text sweep done 2026-11; re-run before submission (pdftotext + grep for TODO, XXX, FIXME, "T5"-style asset names, double spaces) |
| D2 | Tables: caption above, number + title, note below, no overflow | MET | visual pass 2026-11-02; zero overfull boxes |
| D3 | Figures: caption above, number + title, note/source below, no overlap | MET | visual pass 2026-11-03 |
| D4 | Captions regular weight; italic titles per house convention | MET | preamble captionsetup |
| D5 | Every in-text citation has a bibliography entry and vice versa | MET | citation-vs-bib check in the phase loop; re-run after any edit |
| D6 | Reference list renders in APA 6 with hanging indent, single-spaced | MET | apacite setup; spot-check the rendered References pages |
| D7 | Page numbering: front matter roman bottom-centre, body arabic top-right, title unnumbered | MET | fancyhdr config; verify after any rebuild |
| D8 | No orphan headings; floats do not strand text | MET | float pages pinned to top; verify on rebuild |

## E. The five questions an examiner must be able to answer after one pass
(Golding et al. 2014 — the thesis must make these impossible to miss)

1. **What is the question?** — RQ1–RQ3, §1.2.
2. **Why is it worth asking?** — §1.2's four problems + §2.5's five gaps.
3. **What did you do?** — §3.6 + Table 2 + the R1–R8 suite.
4. **What did you find?** — §4.2 + §5.2.3's numbered findings.
5. **What does it mean and what now?** — §4.3 + §5.3/§5.4/§5.5.

Status: each question has a designated home section that answers it
directly. The thesis passes E1–E5 as of the 2026-11-03 build.

## F. Pre-submission pass order (recommended, based on the examiner
behavior above)

1. Read the abstract and Chapter V as a stranger. Fix anything that
   reads like inventory instead of contribution.
2. Sample one number from Chapter I and trace it to IV and V (the
   examiner behavior). Repeat with one term and one claim.
3. Run the D1 full-text sweep on a fresh build.
4. Re-render one table page and one figure page from the final PDF and
   eyeball them (trust multipliers first).
5. Only then read Chapters I–III in full.
