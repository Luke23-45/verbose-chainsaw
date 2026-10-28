# Analysis — publication asset pipeline

Python package that regenerates every thesis figure and table for the
value-relevance study from the frozen `data_extract` outputs.  The
architecture mirrors the PhaseForge `studies/analysis` pipeline (packaged
assets, one CLI, fail-closed checks, traceable outputs); the statistical
content follows `src/proposal/sections/07_methodology/07_methodology.tex`
exactly.

## Data flow (one-way)

`loaders -> dataset -> assets -> render`.  Assets never touch the
filesystem; they receive an `AnalysisDataset` built once per run.

| Path | Responsibility |
|---|---|
| `configs/base.yaml` | inputs, sample rules, output locations, style |
| `common/` | config loader (env override `THESIS_ANALYSIS_CONFIG`), Okabe-Ito style, atomic I/O |
| `loaders/panel.py` | typed loaders for the manual-review CSVs |
| `dataset.py` | `AnalysisDataset`: short-window rule, coverage report, typed accessors |
| `stats/` | models (two-way FE OLS + HC3), joint Wald test, diagnostics, robustness suite |
| `render/` | figure save (PDF + PNG twins), table save (booktabs `.tex` + `.md` twins) |
| `assets/` | `ASSET_REGISTRY` + one module per figure/table |
| `scripts/` | `generate.py`, `verify.py` |
| `outputs/` | generated assets + `generation_manifest.json` (sha256 per output) |

## Usage

From `data_analysis/`:

```
python -m analysis.scripts.generate --check     # dataset build + coverage only
python -m analysis.scripts.generate             # render all 18 assets
python -m analysis.scripts.generate --asset T3,F4
python -m analysis.scripts.generate --section appendix --figures-only
python -m analysis.scripts.verify               # presence + sha256 contract
```

Tests run against a synthetic 30-row study (the real inputs are never touched
by the test suite):

```
cd analysis && python -m pytest
```

### Dependencies and Environment
Running the complete asset generation and test suite requires:
`python >= 3.10`, `numpy`, `pandas`, `scipy`, `statsmodels`, `patsy`, `matplotlib`, `seaborn`, `pytest`, `pyyaml`.

To execute the test suite with python module resolution:
```powershell
cd data_analysis
$env:PYTHONPATH=".;analysis"
pytest analysis/tests
```
The generation manifest (`generation_manifest.json`) records relative asset paths and SHA-256 hashes to guarantee cross-machine reproducibility.
```

## Inputs (frozen; this package never writes them)

- `../data_extract/output/manual_review/mps_rd_joined_panel.csv` (primary)
- `mps_rd_joined_panel_bonusadj.csv`, `mps_rd_candidate_price_table.csv`,
  `mps_rd_merolagani_verification.csv`

PDFs are never read here; the extraction stage is the single source of data.

## Frozen analysis rules (proposal section 07)

- MPS_RD observed more than 5 days from the reporting deadline is missing,
  never imputed — the analysis sample is n = 28 (13 pre FY2076/77-FY2078/79,
  15 post FY2079/80-FY2081/82) of 30 intended bank-years.
- OLS with explicit `C(bank) + C(fy)` dummy terms, MacKinnon-White HC3 robust
  covariance (no clustering: G = 5 banks is too few, per the proposal).
- Principal test: joint Wald F of H0: delta_E = delta_B = 0 in Model 2.
- Robustness suite: ROA-for-EPS (EPS and ROA are never co-included, r ~ 0.975),
  + eligible cash DPS, excluding transition FY2079-80, excluding FY2078-79
  (entity-timing mismatch), bonus-adjusted BVPS, restated EPS as printed.
- P/E is excluded by construction (mechanical MPS/EPS overlap).

## Conventions and deviations from PhaseForge

- seaborn is the statistical plotting layer (pairplot, heatmap); matplotlib
  retained for forest and diagnostics primitives.  PhaseForge uses neither
  seaborn nor pandas — here they are the backbone.
- statsmodels instead of hand-rolled statistics (the proposal names
  statsmodels explicitly).
- `requirements.txt` + the global Python environment (no venv/pyproject) —
  consistent with the `data_extract` sibling.
- Outputs are regenerated, not hand-edited; every output's sha256 is recorded
  in `generation_manifest.json` and checked by `verify.py`.

## Asset plan

See [ANALYSIS_PLAN.md](ANALYSIS_PLAN.md) for the versioned figure/table
design document and the recorded design adjustments.
