"""The proposal's value-relevance models, estimated by OLS with HC3.

Model 1 (methodology eq. 1):
    MPS_RD_it = alpha + mu_i + lambda_t + bE*EPS_it + bB*BVPS_it + e_it
Model 2 (eq. 2) adds dE*(EPS x Post) + dB*(BVPS x Post); the Post main effect
is absorbed by the fiscal-year fixed effects and therefore does not appear as
a separate term.

Fixed effects enter as explicit C(bank) + C(fy) dummy terms; inference uses
MacKinnon-White HC3 standard errors (methodology section 07: with G = 5 banks
cluster-robust covariance is unreliable, so HC3 is the designated inference).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import pandas as pd
import statsmodels.formula.api as smf

MODEL1_FORMULA = "price ~ eps + bvps + C(bank) + C(fy)"
MODEL2_FORMULA = "price ~ eps + bvps + eps:post + bvps:post + C(bank) + C(fy)"
MODEL1_TERMS = ("eps", "bvps")
MODEL2_TERMS = ("eps", "bvps", "eps:post", "bvps:post")


@dataclass(frozen=True)
class TermEstimate:
    term: str
    coef: float
    se: float
    tvalue: float
    pvalue: float
    ci_low: float
    ci_high: float


@dataclass(frozen=True)
class FitResult:
    label: str
    formula: str
    terms: tuple[TermEstimate, ...]
    rsquared: float
    rsquared_adj: float
    nobs: int
    df_resid: float
    results: Any = field(compare=False)  # statsmodels wrapper, for f_test and diagnostics

    def term(self, name: str) -> TermEstimate:
        for estimate in self.terms:
            if estimate.term == name:
                return estimate
        raise KeyError(f"{self.label}: no tracked term {name!r}; tracked: {[e.term for e in self.terms]}")

    def term_map(self) -> dict[str, TermEstimate]:
        return {estimate.term: estimate for estimate in self.terms}


def _fit(label: str, formula: str, frame: pd.DataFrame, terms: tuple[str, ...]) -> FitResult:
    results = smf.ols(formula, data=frame).fit(cov_type="HC3", use_t=True)
    ci = results.conf_int()
    estimates = tuple(
        TermEstimate(
            term=term,
            coef=float(results.params[term]),
            se=float(results.bse[term]),
            tvalue=float(results.tvalues[term]),
            pvalue=float(results.pvalues[term]),
            ci_low=float(ci.loc[term, 0]),
            ci_high=float(ci.loc[term, 1]),
        )
        for term in terms
    )
    return FitResult(
        label=label,
        formula=formula,
        terms=estimates,
        rsquared=float(results.rsquared),
        rsquared_adj=float(results.rsquared_adj),
        nobs=int(results.nobs),
        df_resid=float(results.df_resid),
        results=results,
    )


def fit_spec(
    label: str, formula: str, frame: pd.DataFrame, terms: tuple[str, ...]
) -> FitResult:
    """Fit an arbitrary HC3-OLS specification (used by the robustness suite)."""
    return _fit(label, formula, frame, terms)


def fit_model1(frame: pd.DataFrame, label: str = "Model 1") -> FitResult:
    return _fit(label, MODEL1_FORMULA, frame, MODEL1_TERMS)


def fit_model2(frame: pd.DataFrame, label: str = "Model 2") -> FitResult:
    return _fit(label, MODEL2_FORMULA, frame, MODEL2_TERMS)


def fit_pooled(frame: pd.DataFrame, label: str = "Pooled OLS") -> FitResult:
    return _fit(label, "price ~ eps + bvps", frame, MODEL1_TERMS)


def fit_bank_fe(frame: pd.DataFrame, label: str = "Bank FE only") -> FitResult:
    return _fit(label, "price ~ eps + bvps + C(bank)", frame, MODEL1_TERMS)
