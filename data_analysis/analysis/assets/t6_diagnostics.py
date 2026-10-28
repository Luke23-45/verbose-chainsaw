"""T6: diagnostics for Model 1 (methodology step 5) — variance inflation
factors and tolerance for the substantive regressors, the Breusch-Pagan /
Cook-Weisberg heteroskedasticity test, and Cook's distance against the 4/n
attention threshold.  Residual normality is judged from the Q-Q plot (F5).
"""
from __future__ import annotations

from analysis.dataset import AnalysisDataset
from analysis.render.tables import Table, save_table
from analysis.stats.diagnostics import (
    breusch_pagan,
    cooks_distance,
    cooks_threshold,
    vif_table,
)
from analysis.stats.models import fit_model1


def generate(dataset: AnalysisDataset) -> list:
    fit = fit_model1(dataset.panel, "Model 1")
    vifs = vif_table(dataset.panel, ("eps", "bvps"))
    bp = breusch_pagan(fit.results)
    cooks = cooks_distance(fit.results)
    threshold = cooks_threshold(fit.nobs)
    n_exceed = int((cooks > threshold).sum())
    rows = [
        (f"VIF ({vif.term.upper()})", f"{vif.vif:.2f}", "-",
         f"tolerance {vif.tolerance:.3f}")
        for vif in vifs
    ]
    rows += [
        ("Breusch-Pagan LM", f"{bp.lm_stat:.2f}", f"p = {bp.lm_pvalue:.3f}",
         "Cook-Weisberg test for heteroskedasticity"),
        ("Max Cook's D", f"{cooks.max():.3f}", f"4/n = {threshold:.3f}",
         f"{n_exceed} of {fit.nobs} observations exceed the threshold"),
    ]
    table = Table(
        id="T6_diagnostics",
        caption="Diagnostics for the baseline value-relevance model (Model 1)",
        headers=("Diagnostic", "Statistic", "p / threshold", "Note"),
        rows=tuple(rows),
        notes=(
            "VIF computed on the substantive regressors only (fixed-effect dummies excluded). "
            "HC3 robust inference is the designated answer to heteroskedasticity; the "
            "Breusch-Pagan test is reported for disclosure. Residual normality: see the "
            "Q-Q panel of F5; Cook's-distance influence is examined there per observation."
        ),
    )
    return save_table(table, "tables/T6_diagnostics")
