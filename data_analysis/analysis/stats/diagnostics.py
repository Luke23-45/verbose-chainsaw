"""Regression diagnostics required by methodology section 07, step 5:
variance inflation factors and tolerance, the Breusch-Pagan/Cook-Weisberg
heteroskedasticity test, Cook's distance for influential observations, and
normal Q-Q data for the residual plots.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np
import pandas as pd
from scipy import stats as sps
from statsmodels.stats import diagnostic
from statsmodels.stats.outliers_influence import OLSInfluence, variance_inflation_factor


@dataclass(frozen=True)
class VifRow:
    term: str
    vif: float
    tolerance: float


def vif_table(frame: pd.DataFrame, terms: tuple[str, ...]) -> list[VifRow]:
    """VIF and tolerance for the substantive regressors (not the FE dummies)."""
    if len(set(terms)) != len(terms):
        raise ValueError(f"vif_table: duplicate terms {terms}")
    exog = np.column_stack(
        [np.ones(len(frame))] + [frame[t].to_numpy(dtype=float) for t in terms]
    )
    rows = []
    for i, term in enumerate(terms, start=1):
        vif = float(variance_inflation_factor(exog, i))
        rows.append(VifRow(term=term, vif=vif, tolerance=1.0 / vif))
    return rows


@dataclass(frozen=True)
class HeteroskedasticityResult:
    lm_stat: float
    lm_pvalue: float
    f_stat: float
    f_pvalue: float


def breusch_pagan(results: Any) -> HeteroskedasticityResult:
    lm, lm_p, f, f_p = diagnostic.het_breuschpagan(results.resid, results.model.exog)
    return HeteroskedasticityResult(
        lm_stat=float(lm), lm_pvalue=float(lm_p), f_stat=float(f), f_pvalue=float(f_p)
    )


def cooks_distance(results: Any) -> np.ndarray:
    return np.asarray(OLSInfluence(results).cooks_distance[0], dtype=float)


def cooks_threshold(n: int) -> float:
    """Conventional attention threshold 4/n for Cook's distance."""
    return 4.0 / n


def qq_data(results: Any) -> tuple[np.ndarray, np.ndarray, tuple[float, float]]:
    """(theoretical quantiles, ordered residuals, (slope, intercept) of the
    fitted normal line)."""
    (osm, osr), (slope, intercept, _r) = sps.probplot(results.resid, dist="norm")
    return np.asarray(osm), np.asarray(osr), (float(slope), float(intercept))
