"""The robustness suite of methodology section 07, step 4, as fitted runs.

Baseline Model 1 and Model 2 are included as reference rows; every variant is
Model 2 based unless stated otherwise:
(a) ROA replaces EPS (EPS-ROA r ~ 0.975 forbids co-inclusion),
(b) eligible cash DPS added as an additive regressor (df 14 -> 13),
(c) excluding the transition year FY2079-80 and, separately, excluding
    FY2078-79 (pre-merger fundamentals vs post-merger April 2023 price),
(d) bonus-adjusted BVPS,
(e) restated EPS, used as printed with the substituted rows flagged.
"""
from __future__ import annotations

from dataclasses import dataclass

from analysis.common import config
from analysis.dataset import AnalysisDataset
from analysis.stats.models import FitResult, fit_model1, fit_model2, fit_spec

MODEL2_ROA_FORMULA = "price ~ roa + bvps + roa:post + bvps:post + C(bank) + C(fy)"
MODEL2_ROA_TERMS = ("roa", "bvps", "roa:post", "bvps:post")
MODEL2_DPS_FORMULA = "price ~ eps + bvps + dps + eps:post + bvps:post + C(bank) + C(fy)"
MODEL2_DPS_TERMS = ("eps", "bvps", "dps", "eps:post", "bvps:post")
MODEL2_BONUS_FORMULA = "price ~ eps + bvps_adj + eps:post + bvps_adj:post + C(bank) + C(fy)"
MODEL2_BONUS_TERMS = ("eps", "bvps_adj", "eps:post", "bvps_adj:post")


@dataclass(frozen=True)
class RobustnessRun:
    id: str
    label: str
    note: str
    result: FitResult
    earnings_term: str  # "eps" or "roa": the coefficient standing in for earnings power
    bvps_term: str      # "bvps" or "bvps_adj"

    def earnings(self):
        return self.result.term(self.earnings_term)

    def bvps(self):
        return self.result.term(self.bvps_term)

    def has_deltas(self) -> bool:
        return "eps:post" in self.result.term_map() or "roa:post" in self.result.term_map()


def build_runs(dataset: AnalysisDataset) -> list[RobustnessRun]:
    acfg = config.get_config()["analysis"]
    transition = acfg["transition_fy"]
    mismatch_fy = acfg["entity_mismatch_fy"]

    panel = dataset.panel
    runs: list[RobustnessRun] = []

    m1 = fit_model1(panel, "Model 1 (two-way FE)")
    runs.append(RobustnessRun("R1", m1.label, "baseline reference", m1, "eps", "bvps"))

    m2 = fit_model2(panel, "Model 2 (two-way FE + interactions)")
    runs.append(RobustnessRun("R2", m2.label, "baseline reference", m2, "eps", "bvps"))

    roa = fit_spec(
        "(a) ROA replaces EPS", MODEL2_ROA_FORMULA, panel, MODEL2_ROA_TERMS
    )
    runs.append(
        RobustnessRun(
            "R3",
            roa.label,
            "ROA (PAT / average total assets) substitutes for EPS; never co-included (r ~ 0.975)",
            roa,
            "roa",
            "bvps",
        )
    )

    dps = fit_spec("(b) Model 2 + DPS", MODEL2_DPS_FORMULA, panel, MODEL2_DPS_TERMS)
    runs.append(
        RobustnessRun(
            "R4",
            dps.label,
            "eligible cash DPS added as an additive regressor (df 14 -> 13)",
            dps,
            "eps",
            "bvps",
        )
    )

    excl_transition = panel[panel["fy"] != transition]
    c1 = fit_model2(excl_transition, "(c1) Model 2 excluding transition year")
    runs.append(
        RobustnessRun(
            "R5",
            c1.label,
            f"first post year {transition} excluded (transition-year effects)",
            c1,
            "eps",
            "bvps",
        )
    )

    excl_mismatch = panel[panel["fy"] != mismatch_fy]
    c2 = fit_model2(excl_mismatch, "(c2) Model 2 excluding FY2078-79")
    runs.append(
        RobustnessRun(
            "R6",
            c2.label,
            "FY2078-79 excluded (pre-merger fundamentals vs post-merger April 2023 price)",
            c2,
            "eps",
            "bvps",
        )
    )

    bonus = fit_spec(
        "(d) Model 2, bonus-adjusted BVPS", MODEL2_BONUS_FORMULA, dataset.bonusadj, MODEL2_BONUS_TERMS
    )
    runs.append(
        RobustnessRun(
            "R7",
            bonus.label,
            "BVPS adjusted for proposed bonus issues: BVPS_adj = BVPS / (1 + bonus%), a pro-forma forward capitalization adjustment",
            bonus,
            "eps",
            "bvps_adj",
        )
    )

    restated = fit_model2(dataset.restated, "(e) Model 2, restated EPS")
    flagged = [
        f"{r.bank} {r.fy}"
        for r in dataset.restated.loc[dataset.restated["eps_is_restated"]].itertuples()
    ]
    runs.append(
        RobustnessRun(
            "R8",
            restated.label,
            "restated basic EPS used as printed"
            + (f"; substituted rows: {', '.join(flagged)}" if flagged else ""),
            restated,
            "eps",
            "bvps",
        )
    )

    return runs


def interaction_terms(run: RobustnessRun) -> tuple[str, str]:
    """(delta_E, delta_B) term names for the run's specification."""
    prefix = run.earnings_term
    base = run.bvps_term
    return f"{prefix}:post", f"{base}:post"
