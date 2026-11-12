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
    m1_vifs = vif_table(dataset.panel, ("eps", "bvps"))
    model2_frame = dataset.panel.assign(
        eps_post=dataset.panel["eps"] * dataset.panel["post"],
        bvps_post=dataset.panel["bvps"] * dataset.panel["post"],
    )
    m2_vifs = vif_table(model2_frame, ("eps", "bvps", "eps_post", "bvps_post"))
    bp = breusch_pagan(fit.results)
    bp_classical = breusch_pagan(fit.results, robust=False)
    cooks = cooks_distance(fit.results)
    threshold = cooks_threshold(fit.nobs)
    n_exceed = int((cooks > threshold).sum())
    rows = [
        (f"Model 1 VIF ({vif.term.upper()})", f"{vif.vif:.2f}", "-",
         f"tolerance {vif.tolerance:.3f}")
        for vif in m1_vifs
    ]
    rows += [
        (f"Model 2 VIF ({vif.term.upper()})", f"{vif.vif:.2f}", "-",
         f"tolerance {vif.tolerance:.3f}")
        for vif in m2_vifs
    ]
    rows += [
        ("Breusch-Pagan LM", f"{bp.lm_stat:.2f}", f"p = {bp.lm_pvalue:.3f}",
         "Koenker robust form; statsmodels robust=True"),
        ("Classical BP LM", f"{bp_classical.lm_stat:.2f}",
         f"p = {bp_classical.lm_pvalue:.3f}", "Normality-based classical variant"),
        ("Max Cook's D", f"{cooks.max():.3f}", f"4/n = {threshold:.3f}",
         f"{n_exceed} of {fit.nobs} observations exceed the threshold"),
    ]
    table = Table(
        id="T6_diagnostics",
        caption="Diagnostics for the baseline value-relevance model (Model 1)",
        headers=("Diagnostic", "Statistic", "p / threshold", "Note"),
        rows=tuple(rows),
        notes=(
            "VIFs are computed on the substantive regressors only (fixed-effect dummies "
            "excluded); Model 2 includes both interaction terms. The first LM row is the "
            "Koenker robust form and the second is classical Breusch-Pagan. HC3 changes "
            "the covariance estimate; it does not remove influential observations. See "
            "the Q-Q and leave-one-out diagnostics in F5 and Appendix E."
        ),
    )
    return save_table(table, "tables/T6_diagnostics")
