"""Joint hypothesis tests on fitted models, evaluated under the fitted
(HC3 robust) covariance so the Wald F follows the designated inference.

The principal test of the study lives here: H0: delta_E = delta_B = 0 in
Model 2, via results.f_test on the two interaction terms.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np


@dataclass(frozen=True)
class WaldResult:
    hypothesis: str
    f_stat: float
    p_value: float
    df_num: float
    df_den: float

    def describe(self) -> str:
        return (
            f"{self.hypothesis}: F({self.df_num:.0f}, {self.df_den:.0f}) = "
            f"{self.f_stat:.3f}, p = {self.p_value:.4f}"
        )


def _scalar(value: Any) -> float:
    return float(np.asarray(value, dtype=float).ravel()[0])


def joint_zero_test(results: Any, terms: tuple[str, ...]) -> WaldResult:
    if not terms:
        raise ValueError("joint_zero_test requires at least one term")
    constraint = ", ".join(f"{term} = 0" for term in terms)
    test = results.f_test(constraint)
    return WaldResult(
        hypothesis=f"H0: {constraint}",
        f_stat=_scalar(test.fvalue),
        p_value=_scalar(test.pvalue),
        df_num=_scalar(test.df_num),
        df_den=_scalar(test.df_denom),
    )
