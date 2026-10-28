# Data-Analysis Package — PhaseForge-style Asset Pipeline for the Thesis

## Goal

Build the data-analysis stage in the (currently gated, empty) `data_analysis/analysis/` folder, replicating the architecture of PhaseForge `studies/analysis`: a Python package that regenerates every thesis figure/table from the frozen extraction outputs via one CLI, with fail-closed validation and traceable outputs. All statistical content follows `src/proposal/sections/07_methodology/07_methodology.tex` (5-step protocol) exactly.

## Architecture

Run from `data_analysis/` as `python -m analysis.scripts.generate` (mirrors PhaseForge's `python -m studies.analysis.scripts.generate`). One-way data flow: **loaders → dataset → assets → render**.

```
data_analysis/analysis/
├── README.md                # rewritten: architecture + usage (replaces stale gate notice)
├── ANALYSIS_PLAN.md         # versioned asset plan (mirror of PhaseForge's redesign_analysis_plan.md)
├── requirements.txt         # pandas, numpy, statsmodels, scipy, seaborn, matplotlib, PyYAML, pytest
├── __init__.py
├── configs/base.yaml        # input paths, variable roles, gap rule, transition FYs, restated-EPS overrides, style
├── common/                  # config.py (YAML loader + path resolvers, env override THESIS_ANALYSIS_CONFIG),
│                            #   style.py (seaborn/matplotlib theme, Okabe-Ito, Agg), io.py (atomic writes, typed CSV)
├── loaders/panel.py         # typed loaders: joined panel, bonusadj, price-status, merolagani check
├── dataset.py               # AnalysisDataset: load once, apply rules, coverage report, typed accessors
├── stats/                   # models.py, wald.py, diagnostics.py, robustness.py (pure, unit-testable)
├── render/                  # figures.py (save → PDF+PNG, forest primitive), tables.py (Table → booktabs .tex + .md twins)
├── assets/                  # AssetSpec registry + one module per figure/table
├── scripts/                 # generate.py CLI, verify.py (presence + sha256 manifest check)
├── tests/                   # pytest: synthetic 30-row panel, regression recovery, registry integrity
└── outputs/                 # generation_manifest.json, figures/{main,appendix}/, tables/
```

## Input data contract (never read PDFs)

Primary input: `../data_extract/output/manual_review/mps_rd_joined_panel.csv` (30 rows: `bank, fy, post, price, price_date, gap, eps, bvps, dps, roa, entity_mismatch`). Supporting: `mps_rd_joined_panel_bonusadj.csv` (bvps_adj, bonus), `mps_rd_candidate_price_table.csv` (status), `mps_rd_merolagani_verification.csv`.

Rules applied at the dataset layer (verified against the actual files):
- **Short-window rule**: rows with `gap > 5` → price treated as missing, never imputed (HBL FY2077-78 gap=54, NIMB FY2077-78 gap=47). Analysis sample n=28 (13 pre, 15 post).
- Coverage validation: 5 banks × 6 FYs = 30 intended; strict mode raises on any mismatch, duplicates, or missing columns.
- FY2078-79 `entity_mismatch` rows stay in the baseline; excluded only in the mandated robustness variant.
- Restated-EPS values (GBIME FY2076-77, NMB FY2077-78, HBL FY2077-78) are first re-verified from `mps_rd_final_audit_2026-10-27.md`, then encoded in `base.yaml` with provenance comments.

## Asset registry (16 assets)

**Main tables** — T1 descriptives (mean/SD/min/max, full + pre/post columns); T2 Pearson correlation matrix (MPS_RD, EPS, BVPS, DPS, ROA); T3 Model 1 estimates (β_E, β_B, HC3 SEs, 95% CIs, R², n); T4 Model 2 (β's + δ_E, δ_B, implied post slopes, joint Wald F + p, df=14); T5 robustness suite (ROA-for-EPS, +DPS, excl. FY2079-80, excl. FY2078-79, bonus-adj BVPS, restated EPS — spec-by-spec coefficients); T6 diagnostics (VIF/tolerance, Breusch-Pagan, Cook's D summary, pooled-OLS vs bank-FE vs two-way-FE comparison).

**Main figures** — F1 seaborn scatter matrix (pairplot, hue = pre/post); F2 correlation heatmap (seaborn); F3 value-relevance panels (MPS vs EPS and MPS vs BVPS, pre/post colors, fitted lines); F4 coefficient forest (β's and δ's with 95% HC3 CIs — the H1–H4 visual); F5 diagnostics panel for Model 1 (Q-Q, resid-vs-fitted, scale-location, Cook's D).

**Appendix** — A1 coverage map (5×6 bank×FY grid: realized / missing / entity-mismatch); A2 robustness coefficient forest; A3 Model 2 diagnostics; A4 Merolagani price-verification table (29/30 exact + resolved NMB cell); A5 bonus-adjustment estimates.

Output naming mirrors the registry: `F4_coefficient_forest.{pdf,png}`, `T3_model1.{tex,md}`, under `figures/main|appendix/` and `tables/`.

## Statistical decisions (fixed by the proposal)

- Estimation: statsmodels OLS with explicit `C(bank) + C(fy)` dummies, `cov_type="HC3"` (MacKinnon-White) — chosen over linearmodels because HC3 and the robust joint Wald test are first-class there. Model 2 adds `eps:post` + `bvps:post`; `Post` main effect absorbed by year FE.
- Joint H0: δ_E = δ_B = 0 via `f_test` under HC3 (classical F reported as secondary only).
- EPS and ROA are never co-included (r≈0.975, VIF≈30); P/E excluded entirely.
- Two-tailed 5%; exploratory, non-causal wording in every caption/notes field.
- Sanity gate: results must reproduce the exploratory numpy audit (Model 1 R²≈0.948, β_E≈2.095, β_B≈0.219; Model 2 R²≈0.978, δ_E≈−3.124, δ_B≈−1.758) before any asset is generated.

## Conventions carried over from PhaseForge

AssetSpec dataclass + ASSET_REGISTRY drives both `generate` and `verify`; fail-closed errors naming the offending file/cell; `--check` dry-run, `--allow-partial` escape hatch; per-asset try/except with non-zero exit; deferred imports inside `generate()`; twin outputs (PDF+PNG 300 DPI with embedded fonts, booktabs .tex + .md written atomically); `generation_manifest.json` with sha256 per output; Okabe-Ito palette, Agg backend, shared `paper_style()`; env-var config redirect for tests.

## Deviations (documented in README)

- seaborn added as the primary statistical-plotting layer (your requirement); matplotlib retained for forest/Q-Q primitives. PhaseForge uses neither pandas nor seaborn — here pandas + seaborn are the backbone.
- statsmodels instead of hand-rolled statistics (the proposal names statsmodels explicitly).
- `requirements.txt` + global pip (your choice — no venv); I'll first verify which packages are actually importable and pip-install only the missing ones.
- No pyproject/uv; plain package invoked via `python -m` from `data_analysis/`.

## Implementation steps

1. Verify global Python env: import pandas/numpy/statsmodels/seaborn/matplotlib/PyYAML; pip-install what's missing. Re-verify restated-EPS values and bonusadj columns against the audit docs.
2. Package skeleton: `__init__.py` files, `configs/base.yaml`, `common/` (config, style, io).
3. `loaders/panel.py` + `dataset.py` with coverage checks; write `tests/` for the gap rule and coverage.
4. `stats/` layer; run the sanity gate against the exploratory audit numbers.
5. `render/` layer (figures + table twins).
6. 16 asset modules + registry.
7. `scripts/generate.py` + `verify.py`; run `--check`, then the full generation; write the manifest.
8. Rewrite `analysis/README.md` (ungate), write `ANALYSIS_PLAN.md`, run pytest green. Commits made only when you ask.

## Caveats (noted, not blocking)

- The final audit still lists supervisor approval and NEPSE official-close verification as pending; you've instructed to proceed, so assets remain re-generable the moment any input is amended.
- Stata/SPSS are named in the proposal as parallel tools; this pipeline is the Python leg, and its booktabs `.tex` tables drop straight into the LaTeX thesis.