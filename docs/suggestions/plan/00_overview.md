# Plan — staged rewrites before touching `src/proposal/`

Rule: `detail/` is FROZEN (professor's words). `plan/` holds our proposed new wording. `src/proposal/` is touched ONLY after you approve each plan file.

## Files to write here (one per fix, in this order)

1. `01_cover.md` — cover reorder (Submitted-to up, Submitted-by down) + degree line italic non-bold. Target: `src/proposal/front/titlepage.tex`. Source: `../detail/01_cover.md`.
2. `02_format_tu21.md` — TU p.21 checklist (Times 12, 1.5 spacing, margins, roman front + arabic body, TOC/LOT/LOF). Target: `src/proposal/main.tex`. Source: `../detail/02_table_of_content.md`.
3. `03_research_questions.md` — 3 questions as simple sentences. Targets: `sections/02_problem_statement/` + `03_objectives/`. Source: `../detail/05_problem_statement_p2.md`.
4. `04_lit_review_theoretical.md` — rewritten theory, NO variable sub-heads. Target: `sections/06_literature_review/`. Source: `../detail/07_lit_review_conceptual_A.md`.
5. `05_lit_review_empirical.md` — rewritten empirical + verified Table 1 (all 12 rows). Target: same lit-review file. Sources: `../detail/09_*`, `../detail/11_*`.
6. `06_methodology_design_panel.md` — answer "Why?" + defend/fix "panel data". Target: `sections/07_methodology/`. Source: `../detail/12_methodology_population_p7.md`.
7. `07_figure_framework.md` — standard-form Fig.1 (matches `../detail/16_*` sketch). Target: methodology file figure. Source: `../detail/14_*`.
8. `08_table2_paragraph.md` — Table 2 converted to paragraph. Target: same file. Source: `../detail/14_*`.
9. `09_assumption_checks.md` — qualify-for-test wording (VIF, heteroskedasticity, Cook's, N=5/T=6). Targets: methodology + stats. Sources: `../detail/15_*`, `../detail/16_*`.
10. `10_cover_lists_refs.md` — REBASED to HEAD 693a115: required 12 pt caption fix; optional cover/list/subhead/label alignments; 10A done, 10I + caption-split dropped; 10D rewritten on current null/β wording. Professor orders beat exemplar throughout.

## Status

- [ ] 01–09 drafted
- [ ] you approved each
- [ ] only then applied to `src/proposal/` + rebuilt + rechecked
