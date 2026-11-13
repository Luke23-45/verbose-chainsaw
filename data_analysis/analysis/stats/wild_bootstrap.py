"""Wild-cluster bootstrap sensitivity for the joint regime-shift Wald test.

At G = 5 banks the cluster-robust covariance is unreliable, so HC3 is the
designated inference. This module adds a small-sample sensitivity check in the
spirit of Cameron, Gelbach & Miller (2008): impose the null (restricted fit),
resample the restricted residuals by cluster with Rademacher (+1/-1) weights,
refit the unrestricted model, and recompute the HC3 Wald statistic. The
bootstrap p-value is the share of bootstrap Wald statistics at least as large
as the observed one.

With 5 clusters there are only 2**5 = 32 distinct weight vectors, so all of
them are enumerated (no RNG; the result is fully deterministic) and the
bootstrap p-value is a multiple of 1/32. That coarseness is a limitation of
the check, not a defect in the enumeration, and is reported alongside the
result. The all-+1 pattern reproduces the original sample, so its bootstrap
Wald statistic equals the observed one and is counted in the numerator.
"""
from __future__ import annotations

import itertools
from dataclasses import dataclass

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

from analysis.stats.models import FitResult
from analysis.stats.wald import joint_zero_test


@dataclass(frozen=True)
class WildBootstrapResult:
    label: str
    observed_f: float
    observed_p: float
    bootstrap_p: float
    n_boot: int
    n_exceed: int
    n_clusters: int

    def describe(self) -> str:
        return (
            f"{self.label}: HC3 Wald F = {self.observed_f:.3f} "
            f"(p = {self.observed_p:.3f}); wild-cluster bootstrap "
            f"p = {self.bootstrap_p:.3f} ({self.n_exceed}/{self.n_boot} "
            f"patterns, G = {self.n_clusters})"
        )


def rademacher_patterns(n_clusters: int) -> list[tuple[int, ...]]:
    """All 2**n Rademacher (+1/-1) weight vectors, in a fixed order."""
    if n_clusters < 1:
        raise ValueError("rademacher_patterns requires at least one cluster")
    return list(itertools.product((1, -1), repeat=n_clusters))


def wild_cluster_bootstrap_wald(
    fit_result: FitResult,
    frame: pd.DataFrame,
    restricted_formula: str,
    terms: tuple[str, str],
    cluster_col: str = "bank",
    dependent: str = "price_rd",
) -> WildBootstrapResult:
    """Wild-cluster bootstrap p-value for a joint zero test on ``terms``.

    ``fit_result`` is the unrestricted fit on ``frame``; ``restricted_formula``
    is the same specification with the tested terms omitted (the null-imposed
    fit whose residuals are resampled). The Wald statistic is recomputed with
    the HC3 covariance on every bootstrap refit, matching the observed test.
    """
    observed = joint_zero_test(fit_result.results, terms)
    restricted = smf.ols(restricted_formula, data=frame).fit()
    fitted = np.asarray(restricted.fittedvalues, dtype=float)
    resid = np.asarray(restricted.resid, dtype=float)
    clusters = sorted(frame[cluster_col].unique().tolist())
    cluster_index = np.array(
        [clusters.index(value) for value in frame[cluster_col]], dtype=int
    )
    constraint = ", ".join(f"{term} = 0" for term in terms)
    patterns = rademacher_patterns(len(clusters))
    n_exceed = 0
    for pattern in patterns:
        weights = np.array([pattern[i] for i in cluster_index], dtype=float)
        star = frame.copy()
        star[dependent] = fitted + resid * weights
        boot = smf.ols(fit_result.formula, data=star).fit(cov_type="HC3", use_t=True)
        f_star = float(
            np.asarray(boot.f_test(constraint).fvalue, dtype=float).ravel()[0]
        )
        if f_star >= observed.f_stat:
            n_exceed += 1
    return WildBootstrapResult(
        label=fit_result.label,
        observed_f=observed.f_stat,
        observed_p=observed.p_value,
        bootstrap_p=n_exceed / len(patterns),
        n_boot=len(patterns),
        n_exceed=n_exceed,
        n_clusters=len(clusters),
    )
