"""Appendix E computation: full HC3 outputs for Models 1/2, R1-R8, joint FE
tests, diagnostics, leave-one-out and leave-one-bank sensitivity.

No statsmodels on this machine: OLS + MacKinnon-White HC3 are implemented
directly in numpy; t/F/chi2 p-values come from scipy.stats. Every number
that also appears in Chapter IV is verified against its printed value
before any LaTeX row is emitted. Nothing is hand-typed into tables.
"""
import json
import numpy as np
import pandas as pd
from scipy import stats
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
ROOT = str(REPO)
PANEL = ROOT + "/data_analysis/data_extract/output/manual_review/mps_rd_joined_panel.csv"
BONUSADJ = ROOT + "/data_analysis/data_extract/output/manual_review/mps_rd_joined_panel_bonusadj.csv"
DPS = ROOT + "/data_analysis/data_extract/config/dps.json"

p = pd.read_csv(PANEL)
clean = p[p["gap"] <= 5].copy().reset_index(drop=True)
assert len(clean) == 28, len(clean)
assert set(clean["post"]) == {0, 1}
# post must equal FY2079-80+ indicator
assert ((clean["fy"] >= "FY2079-80").astype(int) == clean["post"]).all()

BANKS = ["GBIME", "HBL", "KBL", "NIMB", "NMB"]
YEARS = sorted(clean["fy"].unique())
assert YEARS == ["FY2076-77", "FY2077-78", "FY2078-79", "FY2079-80", "FY2080-81", "FY2081-82"]


def design(df, slopes, ref_bank="GBIME", ref_year="FY2076-77", extra=None):
    """slopes: list of (name, values). Returns (names, X)."""
    names = ["Intercept"] + [s[0] for s in slopes]
    cols = [np.ones(len(df))] + [np.asarray(s[1], dtype=float) for s in slopes]
    for b in BANKS:
        if b != ref_bank and (df["bank"] == b).any():
            names.append(f"Bank {b}")
            cols.append((df["bank"] == b).astype(float).values)
    for y in YEARS:
        if y != ref_year and (df["fy"] == y).any():
            names.append(f"Year {y}")
            cols.append((df["fy"] == y).astype(float).values)
    if extra:
        for nm, v in extra:
            names.append(nm)
            cols.append(np.asarray(v, dtype=float))
    return names, np.column_stack(cols)


def fit(df, slopes, **kw):
    df = df.reset_index(drop=True)
    names, X = design(df, slopes, **kw)
    y = df["price"].values.astype(float)
    n, K = X.shape
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    e = y - X @ beta
    XtX_inv = np.linalg.inv(X.T @ X)
    h = np.einsum("ij,jk,ik->i", X, XtX_inv, X)
    assert np.all(h < 1.0), "leverage == 1 would break HC3"
    # HC3 meat: X' diag(e^2/(1-h)^2) X
    w = (e / (1 - h)) ** 2
    meat = (X * w[:, None]).T @ X
    V = XtX_inv @ meat @ XtX_inv
    se = np.sqrt(np.diag(V))
    dfree = n - K
    t = beta / se
    pv = 2 * stats.t.sf(np.abs(t), dfree)
    crit = stats.t.ppf(0.975, dfree)
    ci = np.column_stack([beta - crit * se, beta + crit * se])
    ssr = float(e @ e)
    sst = float(((y - y.mean()) ** 2).sum())
    r2 = 1 - ssr / sst
    adj = 1 - (1 - r2) * (n - 1) / dfree
    # within R^2: share of bank-and-year-adjusted variation explained by the
    # slopes = 1 - SSR_LSDV / SST_residuals-from-dummies-only regression.
    # (Naive two-way demeaning is inexact for this unbalanced panel, so the
    # dummies-only residual SST is the correct adjusted variation.)
    _, X0 = design(df, [])
    b0, *_ = np.linalg.lstsq(X0, y, rcond=None)
    e0 = y - X0 @ b0
    within_r2 = 1 - ssr / float(e0 @ e0)
    return dict(names=names, beta=beta, se=se, t=t, p=pv, ci=ci, V=V, X=X,
                e=e, h=h, n=n, K=K, df=dfree, r2=r2, adj=adj,
                within=within_r2, ssr=ssr)


def wald(res, idx):
    """Wald F for beta[idx] == 0 under HC3 covariance."""
    idx = list(idx)
    b = res["beta"][idx]
    Vsub = res["V"][np.ix_(idx, idx)]
    q = len(idx)
    F = float(b @ np.linalg.inv(Vsub) @ b) / q
    pv = float(stats.f.sf(F, q, res["df"]))
    return F, pv


def idx_of(res, *names):
    return [res["names"].index(nm) for nm in names]


# ---------------- baseline models ----------------
M1 = fit(clean, [("EPS", clean["eps"]), ("BVPS", clean["bvps"])])
M2 = fit(clean, [("EPS", clean["eps"]), ("BVPS", clean["bvps"]),
                 ("d_E", clean["eps"] * clean["post"]),
                 ("d_B", clean["bvps"] * clean["post"])])
# post combinations (delta method)
for res, bE, bB, dE, dB in [(M2, "EPS", "BVPS", "d_E", "d_B")]:
    iE, iB, idE, idB = idx_of(res, bE, bB, dE, dB)
    for lab, i1, i2 in [("post EPS", iE, idE), ("post BVPS", iB, idB)]:
        v = res["V"][i1, i1] + res["V"][i2, i2] + 2 * res["V"][i1, i2]
        se = np.sqrt(v)
        est = res["beta"][i1] + res["beta"][i2]
        t = est / se
        pv = 2 * stats.t.sf(abs(t), res["df"])
        res[lab] = (est, se, t, pv)

# ---------------- robustness ----------------
# R7: bvps_adj from dps.json bonus rule; cross-check vs the saved bonusadj panel
ba = pd.read_csv(BONUSADJ)
dps = json.load(open(DPS))["entries"]
bonus = {(d["series"], d["fy"]): d["bonus_percent"] for d in dps}
clean["bvps_adj"] = [row["bvps"] / (1 + bonus.get((row["bank"], row["fy"]), 0) / 100.0)
                      for _, row in clean.iterrows()]
_ba = ba.set_index(["bank", "fy"])["bvps_adj"]
_mismatch = [(r["bank"], r["fy"], r["bvps_adj"], _ba.loc[(r["bank"], r["fy"])])
             for _, r in clean.iterrows()
             if abs(r["bvps_adj"] - _ba.loc[(r["bank"], r["fy"])]) > 0.005]
print("bvps_adj vs saved bonusadj panel mismatches:", _mismatch if _mismatch else "NONE")
specs = {}
specs["R1"] = fit(clean, [("EPS", clean["eps"]), ("BVPS", clean["bvps"])])
specs["R2"] = M2
specs["R3"] = fit(clean, [("ROA", clean["roa"]), ("BVPS", clean["bvps"]),
                          ("d_ROA", clean["roa"] * clean["post"]),
                          ("d_B", clean["bvps"] * clean["post"])])
specs["R4"] = fit(clean, [("EPS", clean["eps"]), ("BVPS", clean["bvps"]),
                          ("d_E", clean["eps"] * clean["post"]),
                          ("d_B", clean["bvps"] * clean["post"])],
                   extra=[("DPS", clean["dps"])])
specs["R5"] = fit(clean[clean["fy"] != "FY2079-80"],
                   [("EPS", clean[clean["fy"] != "FY2079-80"]["eps"]),
                    ("BVPS", clean[clean["fy"] != "FY2079-80"]["bvps"]),
                    ("d_E", clean[clean["fy"] != "FY2079-80"]["eps"] *
                     clean[clean["fy"] != "FY2079-80"]["post"]),
                    ("d_B", clean[clean["fy"] != "FY2079-80"]["bvps"] *
                     clean[clean["fy"] != "FY2079-80"]["post"])])
specs["R6"] = fit(clean[clean["fy"] != "FY2078-79"],
                   [("EPS", clean[clean["fy"] != "FY2078-79"]["eps"]),
                    ("BVPS", clean[clean["fy"] != "FY2078-79"]["bvps"]),
                    ("d_E", clean[clean["fy"] != "FY2078-79"]["eps"] *
                     clean[clean["fy"] != "FY2078-79"]["post"]),
                    ("d_B", clean[clean["fy"] != "FY2078-79"]["bvps"] *
                     clean[clean["fy"] != "FY2078-79"]["post"])])
specs["R7"] = fit(clean, [("EPS", clean["eps"]), ("BVPS_adj", clean["bvps_adj"]),
                          ("d_E", clean["eps"] * clean["post"]),
                          ("d_Badj", clean["bvps_adj"] * clean["post"])])
rest = clean["eps"].copy()
for i, row in clean.iterrows():
    if (row["bank"], row["fy"]) == ("GBIME", "FY2076-77"):
        rest.loc[i] = 15.33
    if (row["bank"], row["fy"]) == ("NMB", "FY2077-78"):
        rest.loc[i] = 14.76
specs["R8"] = fit(clean, [("EPS_r", rest), ("BVPS", clean["bvps"]),
                          ("d_Er", rest * clean["post"]),
                          ("d_B", clean["bvps"] * clean["post"])])

# ---------------- diagnostics (Model 1) ----------------
# VIF variants
def vif_aux(yv, Xv):
    Xv = np.column_stack([np.ones(len(yv)), Xv])
    b, *_ = np.linalg.lstsq(Xv, yv, rcond=None)
    e = yv - Xv @ b
    r2a = 1 - (e @ e) / ((yv - yv.mean()) @ (yv - yv.mean()))
    return 1 / (1 - r2a)
vif_simple = vif_aux(clean["eps"].values, clean["bvps"].values[:, None])
# BP on Model 1: auxiliary regression of e^2 on all non-intercept regressors
Xb = np.column_stack([np.ones(28), M1["X"][:, 1:]])
bb, *_ = np.linalg.lstsq(Xb, M1["e"] ** 2, rcond=None)
eb = M1["e"] ** 2 - Xb @ bb
r2b = 1 - (eb @ eb) / (((M1["e"] ** 2) - (M1["e"] ** 2).mean()) @ ((M1["e"] ** 2) - (M1["e"] ** 2).mean()))
bp_lm = 28 * r2b
bp_p = float(stats.chi2.sf(bp_lm, 11))
# Cook's distance, Model 1
s2 = M1["ssr"] / M1["df"]
cook = (M1["e"] ** 2 / (M1["K"] * s2)) * (M1["h"] / (1 - M1["h"]) ** 2)
flag = clean[cook > 4 / 28].copy()
flag["cook"] = cook[cook > 4 / 28]
flag["lev"] = M1["h"][cook > 4 / 28]

# ---------------- sensitivities (Model 2) ----------------
def m2_on(df):
    ref_bank = "GBIME" if (df["bank"] == "GBIME").any() else sorted(df["bank"].unique())[0]
    return fit(df, [("EPS", df["eps"]), ("BVPS", df["bvps"]),
                    ("d_E", df["eps"] * df["post"]),
                    ("d_B", df["bvps"] * df["post"])], ref_bank=ref_bank)
loo = []
for i in range(28):
    r = m2_on(clean.drop(clean.index[i]))
    F, pv = wald(r, idx_of(r, "d_E", "d_B"))
    loo.append(dict(drop=f"{clean.loc[i, 'bank']} {clean.loc[i, 'fy']}",
                    dE=r["beta"][idx_of(r, 'd_E')[0]], dB=r["beta"][idx_of(r, 'd_B')[0]],
                    F=F, p=pv))
lob = []
for b in BANKS:
    sub = clean[clean["bank"] != b]
    r = m2_on(sub)
    F, pv = wald(r, idx_of(r, "d_E", "d_B"))
    lob.append(dict(bank=b, n=len(sub),
                    dE=r["beta"][idx_of(r, 'd_E')[0]], dB=r["beta"][idx_of(r, 'd_B')[0]],
                    dE_se=r["se"][idx_of(r, 'd_E')[0]], dB_se=r["se"][idx_of(r, 'd_B')[0]],
                    F=F, p=pv))

# ---------------- verification against Chapter IV ----------------
def chk(label, got, want, tol):
    ok = abs(got - want) <= tol
    print(f"{'PASS' if ok else 'FAIL'} {label}: got {got:.4f} want {want} tol {tol}")
    return ok
allok = True
g = lambda res, nm: res["beta"][res["names"].index(nm)]
s = lambda res, nm: res["se"][res["names"].index(nm)]
pv_ = lambda res, nm: res["p"][res["names"].index(nm)]
allok &= chk("M1 EPS", g(M1, "EPS"), 2.095, 0.0005)
allok &= chk("M1 EPS SE", s(M1, "EPS"), 4.096, 0.0005)
allok &= chk("M1 EPS p", pv_(M1, "EPS"), 0.616, 0.0005)
allok &= chk("M1 BVPS", g(M1, "BVPS"), 0.219, 0.0005)
allok &= chk("M1 BVPS SE", s(M1, "BVPS"), 1.858, 0.0005)
allok &= chk("M1 BVPS p", pv_(M1, "BVPS"), 0.908, 0.0005)
allok &= chk("M1 R2", M1["r2"], 0.948, 0.0005)
allok &= chk("M1 adj", M1["adj"], 0.912, 0.0005)
allok &= chk("M1 within", M1["within"], 0.152, 0.0005)
allok &= chk("M2 EPS", g(M2, "EPS"), 5.577, 0.0005)
allok &= chk("M2 EPS SE", s(M2, "EPS"), 3.560, 0.0005)
allok &= chk("M2 BVPS", g(M2, "BVPS"), 0.100, 0.0005)
allok &= chk("M2 d_E", g(M2, "d_E"), -3.124, 0.0005)
allok &= chk("M2 d_B", g(M2, "d_B"), -1.758, 0.0005)
allok &= chk("M2 R2", M2["r2"], 0.978, 0.0005)
allok &= chk("M2 within", M2["within"], 0.642, 0.0005)
F2, p2 = wald(M2, idx_of(M2, "d_E", "d_B"))
allok &= chk("M2 Wald F", F2, 2.954, 0.0005)
allok &= chk("M2 Wald p", p2, 0.085, 0.0005)
allok &= chk("M2 post EPS", M2["post EPS"][0], 2.453, 0.0005)
allok &= chk("M2 post EPS p", M2["post EPS"][3], 0.298, 0.0005)
allok &= chk("M2 post BVPS", M2["post BVPS"][0], -1.658, 0.0005)
allok &= chk("M2 post BVPS p", M2["post BVPS"][3], 0.161, 0.0005)
allok &= chk("M1 EPS CI lo", M1["ci"][M1["names"].index("EPS"), 0], -6.587, 0.0005)
allok &= chk("M1 EPS CI hi", M1["ci"][M1["names"].index("EPS"), 1], 10.777, 0.0005)
allok &= chk("M1 BVPS CI lo", M1["ci"][M1["names"].index("BVPS"), 0], -3.720, 0.0005)
allok &= chk("M1 BVPS CI hi", M1["ci"][M1["names"].index("BVPS"), 1], 4.158, 0.0005)
allok &= chk("VIF simple", vif_simple, 1.16, 0.005)
allok &= chk("BP LM", bp_lm, 14.37, 0.005)
allok &= chk("BP p", bp_p, 0.213, 0.0005)
allok &= chk("Cook max", cook.max(), 0.552, 0.0005)
print("Cook flagged count:", int((cook > 4 / 28).sum()), "(want 5)")
allok &= (int((cook > 4 / 28).sum()) == 5)
print("Cook max row:", clean.loc[cook.argmax(), "bank"], clean.loc[cook.argmax(), "fy"])
# Table 10 robustness spot checks
t10 = {
    "R3": (("ROA", 83.760, 79.852), ("BVPS", 0.358, 1.381), ("d_ROA", -43.570, 83.671), ("d_B", -1.901, 1.290), 2.46, 0.121),
    "R4": (("EPS", 6.183, 4.508), ("BVPS", -0.642, 1.378), ("d_E", -4.072, 5.151), ("d_B", -1.770, 1.335), 2.77, 0.100),
    "R5": (("EPS", 5.993, 4.635), ("BVPS", -0.201, 1.849), ("d_E", -2.578, 5.521), ("d_B", -1.880, 1.419), 2.41, 0.139),
    "R6": (("EPS", 4.336, 3.724), ("BVPS", 0.802, 1.328), ("d_E", -2.436, 4.755), ("d_B", -2.611, 1.517), 5.82, 0.021),
    "R7": (("EPS", 5.775, 4.145), ("BVPS_adj", 0.153, 1.632), ("d_E", -4.043, 4.446), ("d_Badj", -1.533, 1.595), 2.37, 0.130),
    "R8": (("EPS_r", 5.256, 3.016), ("BVPS", 0.031, 1.300), ("d_Er", -2.860, 3.807), ("d_B", -1.812, 1.223), 2.92, 0.087),
}
for k, rows in t10.items():
    res = specs[k]
    for nm, want, se_want in rows[:4]:
        allok &= chk(f"{k} {nm}", g(res, nm), want, 0.0005)
        allok &= chk(f"{k} {nm} SE", s(res, nm), se_want, 0.0005)
    wnames = {"R3": ("d_ROA", "d_B"), "R4": ("d_E", "d_B"), "R5": ("d_E", "d_B"),
              "R6": ("d_E", "d_B"), "R7": ("d_E", "d_Badj"), "R8": ("d_Er", "d_B")}[k]
    F, pv = wald(res, idx_of(res, *wnames))
    allok &= chk(f"{k} Wald F", F, rows[4], 0.005)
    allok &= chk(f"{k} Wald p", pv, rows[5], 0.0005)
    allok &= (res["n"] == 28 or (k in ("R5", "R6") and res["n"] == 23))
    print(f"{k} n={res['n']} K={res['K']} df={res['df']} R2={res['r2']:.4f} within={res['within']:.4f}")
print("ALL VERIFICATION:", "PASS" if allok else "FAIL")
print()
print("Flagged observations (Cook > 4/28):")
for _, r in flag.iterrows():
    print(f"  {r['bank']} {r['fy']}: Cook={r['cook']:.4f} lev={r['lev']:.4f}")
print("Leave-one-out ranges (Model 2, 28 deletions):")
print(f"  d_E [{min(x['dE'] for x in loo):.4f}, {max(x['dE'] for x in loo):.4f}] "
      f"d_B [{min(x['dB'] for x in loo):.4f}, {max(x['dB'] for x in loo):.4f}] "
      f"Wald p [{min(x['p'] for x in loo):.4f}, {max(x['p'] for x in loo):.4f}] "
      f"sign flips d_E: {any(np.sign(x['dE']) > 0 for x in loo)}, "
      f"d_B: {any(np.sign(x['dB']) > 0 for x in loo)}, "
      f"any Wald p<0.05: {any(x['p'] < 0.05 for x in loo)}")
print("Leave-one-bank (Model 2):")
for x in lob:
    print(f"  drop {x['bank']}: n={x['n']} d_E={x['dE']:.4f} d_B={x['dB']:.4f} F={x['F']:.3f} p={x['p']:.4f}")
print("Joint FE Wald tests:")
for res, lab in [(M1, "M1"), (M2, "M2")]:
    nb = [i for i, nm in enumerate(res["names"]) if nm.startswith("Bank ")]
    ny = [i for i, nm in enumerate(res["names"]) if nm.startswith("Year ")]
    for tlab, idx in [("bank", nb), ("year", ny), ("both", nb + ny)]:
        F, pv = wald(res, idx)
        print(f"  {lab} {tlab}: F={F:.3f} df1={len(idx)} df2={res['df']} p={pv:.4f}")
print("R4 DPS coefficient:", g(specs["R4"], "DPS"), "SE", s(specs["R4"], "DPS"),
      "p", pv_(specs["R4"], "DPS"))
print("M1 leverage max:", M1["h"].max(), "M2 leverage max:", M2["h"].max())
print("M1 names:", M1["names"])
print("M2 names:", M2["names"])

# ---------------- dump JSON + LaTeX rows ----------------
import pickle
with open(HERE / "results.pkl", "wb") as f:
    pickle.dump(dict(M1=M1, M2=M2, specs=specs, flag=flag, loo=loo, lob=lob,
                     vif=vif_simple, bp=(bp_lm, bp_p), cook=cook), f)
print("saved results.pkl")
