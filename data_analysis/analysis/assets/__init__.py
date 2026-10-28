"""Asset registry: every planned figure and table declared exactly once.

The registry is the publication contract: scripts.generate renders from it,
scripts.verify checks presence and hashes against it, and ANALYSIS_PLAN.md
documents the design of each entry.  Output paths are relative to paper_root
and include the suffix.

IDs follow paper position: T1-T6 main tables, F1-F6 main figures, A1-A6
appendix assets.
"""
from __future__ import annotations

from dataclasses import dataclass
from importlib import import_module


@dataclass(frozen=True)
class AssetSpec:
    id: str
    kind: str      # figure | table
    section: str   # main | appendix
    title: str
    priority: str  # P0 | P1 | P2
    module: str    # module name under analysis.assets
    outputs: tuple[str, ...]
    generator_attr: str = "generate"


def _spec(**kwargs) -> AssetSpec:
    return AssetSpec(**kwargs)


ASSET_REGISTRY: dict[str, AssetSpec] = {}
for spec in (
    _spec(id="T1", kind="table", section="main",
          title="Descriptive statistics", priority="P0",
          module="t1_descriptives",
          outputs=("tables/T1_descriptives.tex", "tables/T1_descriptives.md")),
    _spec(id="T2", kind="table", section="main",
          title="Pearson correlation matrix", priority="P0",
          module="t2_correlations",
          outputs=("tables/T2_correlations.tex", "tables/T2_correlations.md")),
    _spec(id="T3", kind="table", section="main",
          title="Model 1: baseline value-relevance estimates (two-way FE, HC3)", priority="P0",
          module="t3_model1",
          outputs=("tables/T3_model1.tex", "tables/T3_model1.md")),
    _spec(id="T4", kind="table", section="main",
          title="Model 2: consolidation interactions and the joint Wald test", priority="P0",
          module="t4_model2",
          outputs=("tables/T4_model2.tex", "tables/T4_model2.md")),
    _spec(id="T5", kind="table", section="main",
          title="Robustness suite", priority="P0",
          module="t5_robustness",
          outputs=("tables/T5_robustness.tex", "tables/T5_robustness.md")),
    _spec(id="T6", kind="table", section="main",
          title="Diagnostics for Model 1", priority="P1",
          module="t6_diagnostics",
          outputs=("tables/T6_diagnostics.tex", "tables/T6_diagnostics.md")),
    _spec(id="F1", kind="figure", section="main",
          title="Scatter matrix of MPS_RD, EPS and BVPS by period", priority="P1",
          module="f1_scatter_matrix",
          outputs=("figures/main/F1_scatter_matrix.pdf", "figures/main/F1_scatter_matrix.png")),
    _spec(id="F2", kind="figure", section="main",
          title="Correlation heatmap", priority="P1",
          module="f2_correlation_heatmap",
          outputs=("figures/main/F2_correlation_heatmap.pdf", "figures/main/F2_correlation_heatmap.png")),
    _spec(id="F3", kind="figure", section="main",
          title="Value-relevance scatter panels, pre vs post", priority="P0",
          module="f3_value_relevance",
          outputs=("figures/main/F3_value_relevance.pdf", "figures/main/F3_value_relevance.png")),
    _spec(id="F4", kind="figure", section="main",
          title="Coefficient forest: pre slopes, interactions, implied post slopes", priority="P0",
          module="f4_coefficient_forest",
          outputs=("figures/main/F4_coefficient_forest.pdf", "figures/main/F4_coefficient_forest.png")),
    _spec(id="F5", kind="figure", section="main",
          title="Diagnostics panel for Model 1", priority="P1",
          module="f5_diagnostics",
          outputs=("figures/main/F5_diagnostics.pdf", "figures/main/F5_diagnostics.png")),
    _spec(id="F6", kind="figure", section="main",
          title="Variable trends by bank series", priority="P1",
          module="f6_trends",
          outputs=("figures/main/F6_trends.pdf", "figures/main/F6_trends.png")),
    _spec(id="A1", kind="figure", section="appendix",
          title="Data coverage map (bank x fiscal year)", priority="P1",
          module="a1_coverage_map",
          outputs=("figures/appendix/A1_coverage_map.pdf", "figures/appendix/A1_coverage_map.png")),
    _spec(id="A2", kind="figure", section="appendix",
          title="Robustness coefficient forest (EPS channel)", priority="P1",
          module="a2_robustness_forest",
          outputs=("figures/appendix/A2_robustness_forest.pdf", "figures/appendix/A2_robustness_forest.png")),
    _spec(id="A3", kind="figure", section="appendix",
          title="Diagnostics panel for Model 2", priority="P2",
          module="a3_model2_diagnostics",
          outputs=("figures/appendix/A3_model2_diagnostics.pdf", "figures/appendix/A3_model2_diagnostics.png")),
    _spec(id="A4", kind="table", section="appendix",
          title="MPS_RD price verification (Merolagani cross-check)", priority="P2",
          module="a4_price_verification",
          outputs=("tables/A4_price_verification.tex", "tables/A4_price_verification.md")),
    _spec(id="A5", kind="table", section="appendix",
          title="Specification comparison: pooled OLS vs bank FE vs two-way FE", priority="P2",
          module="a5_specification_comparison",
          outputs=("tables/A5_specification_comparison.tex", "tables/A5_specification_comparison.md")),
    _spec(id="A6", kind="table", section="appendix",
          title="Analysis dataset by bank-year", priority="P2",
          module="a6_analysis_dataset",
          outputs=("tables/A6_analysis_dataset.tex", "tables/A6_analysis_dataset.md")),
):
    if spec.id in ASSET_REGISTRY:
        raise ValueError(f"duplicate asset id {spec.id}")
    ASSET_REGISTRY[spec.id] = spec


def load_generator(spec: AssetSpec):
    module = import_module(f"analysis.assets.{spec.module}")
    generator = getattr(module, spec.generator_attr, None)
    if generator is None:
        raise AttributeError(f"{module.__name__}: no generator {spec.generator_attr!r}")
    return generator
