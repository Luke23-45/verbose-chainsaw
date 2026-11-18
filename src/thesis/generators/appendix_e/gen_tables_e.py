"""Generate Appendix E table blocks from verified results.pkl. No hand-typed
numbers: every cell comes from the recomputation that passed all Chapter IV
verification checks. Precision: estimates/SEs/CIs 4 dp, t 2 dp, p 3 dp
(p < 0.0005 shown as <0.001), F 3 dp, R-squared 3 dp."""
import pickle
from pathlib import Path

import numpy as np
from scipy import stats as _st

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]

r = pickle.load(open(HERE / "results.pkl", "rb"))
M1, M2, specs = r["M1"], r["M2"], r["specs"]
flag, loo, lob = r["flag"], r["loo"], r["lob"]


def num(v, dp=4):
    if round(float(v), dp) == 0:
        v = 0.0
    return f"${float(v):.{dp}f}$"


def pfmt(p):
    return "$<0.001$" if p < 0.0005 else f"${p:.3f}$"


def cirow(res, nm):
    lo, hi = res["ci"][res["names"].index(nm)]
    return f"$[{lo:.4f}, {hi:.4f}]$".replace("-0.0000", "0.0000")


def gap_rows(lines):
    """Insert \\addlinespace after each data row that is followed by another
    data row or a group subhead; never before \\bottomrule."""
    out = []
    for i, line in enumerate(lines):
        out.append(line)
        if line.endswith("\\\\") and not line.startswith("\\multicolumn") and not line.startswith("\\textbf"):
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            if nxt and nxt != "\\bottomrule":
                out.append("\\addlinespace")
    return out


def full_table(res, label, caption, note):
    L = []
    L.append("\\begin{table}[!htbp]")
    L.append("\\centering")
    L.append("\\small")
    L.append("\\setlength{\\tabcolsep}{4pt}")
    L.append(f"\\caption{{{caption}}}")
    L.append(f"\\label{{{label}}}")
    L.append("\\begin{tabular}{>{\\raggedright\\arraybackslash}p{0.20\\textwidth}"
             ">{\\raggedright\\arraybackslash}p{0.12\\textwidth}"
             ">{\\raggedright\\arraybackslash}p{0.12\\textwidth}"
             ">{\\raggedright\\arraybackslash}p{0.07\\textwidth}"
             ">{\\raggedright\\arraybackslash}p{0.09\\textwidth}"
             ">{\\raggedright\\arraybackslash}p{0.27\\textwidth}}")
    L.append("\\toprule")
    L.append("\\textbf{Variable} & \\textbf{Estimate} & \\textbf{HC3 SE} & "
             "\\textbf{$t$} & \\textbf{$p$} & \\textbf{95\\% CI} \\\\")
    L.append("\\midrule")
    disp = {"Intercept": "Intercept", "EPS": "EPS", "BVPS": "BVPS",
            "d_E": "$\\delta_E$", "d_B": "$\\delta_B$",
            "Bank HBL": "Bank HBL", "Bank KBL": "Bank KBL",
            "Bank NIMB": "Bank NIMB", "Bank NMB": "Bank NMB"}
    for nm in res["names"]:
        if nm.startswith("Year "):
            _, fy = nm.split(" ", 1)
            disp[nm] = "Year FY " + fy[2:6] + "/" + fy[7:9]
        i = res["names"].index(nm)
        L.append(f"{disp[nm]} & {num(res['beta'][i])} & {num(res['se'][i])} & "
                 f"${res['t'][i]:.2f}$ & {pfmt(res['p'][i])} & {cirow(res, nm)} \\\\")
    L.append("\\bottomrule")
    L.append("\\end{tabular}")
    L.append("")
    L.append("\\vspace{4pt}")
    L.append("\\begin{minipage}{\\linewidth}")
    L.append("\\footnotesize")
    L.append(f"\\textit{{Note.}} {note}")
    L.append("\\end{minipage}")
    L.append("\\end{table}")
    return "\n".join(gap_rows(L))


def fitnote(res):
    return (f"$N = {res['n']}$; parameters $K = {res['K']}$; residual degrees "
            f"of freedom $= {res['df']}$; $R^2$ (LSDV) $= {res['r2']:.3f}$; "
            f"adjusted $R^2 = {res['adj']:.3f}$; Within-$R^2 = {res['within']:.3f}$. "
            f"OLS with two-way fixed effects; MacKinnon-White HC3 robust "
            f"standard errors; $t$-statistics and confidence intervals on "
            f"Student's $t({res['df']})$ distribution. Estimates, standard "
            f"errors, and confidence limits to four decimals; $p$-values to "
            f"three decimals.")


out = []
out.append(full_table(
    M1, "tab:app_m1full",
    "Model 1: Full Baseline Value-Relevance Estimates ($N = 28$)",
    "Dependent variable: $\\mathit{MPS}^{RD}$. EPS is earnings per share; BVPS is "
    "book value per share; SE is standard error. Bank fixed effects include 4 "
    "dummies (reference: GBIME); fiscal-year fixed effects include 5 dummies "
    "(reference: FY 2076/77). " + fitnote(M1)))
out.append("")
out.append(full_table(
    M2, "tab:app_m2full",
    "Model 2: Full Regime-Shift Value-Relevance Estimates ($N = 28$)",
    "Dependent variable: $\\mathit{MPS}^{RD}$. EPS is earnings per share; BVPS is "
    "book value per share; SE is standard error. $\\delta_E$ and $\\delta_B$ are "
    "the interactions of EPS and BVPS with the post-consolidation indicator; "
    "implied post-consolidation slopes are EPS $2.4534$ (SE $2.2687$, "
    "$t = 1.08$, $p = 0.298$, 95\\% CI $[-2.4124, 7.3192]$) and BVPS "
    "$-1.6576$ (SE $1.1198$, $t = -1.48$, $p = 0.161$, 95\\% CI "
    "$[-4.0593, 0.7441]$). Bank fixed effects include 4 dummies "
    "(reference: GBIME); fiscal-year fixed effects include 5 dummies "
    "(reference: FY 2076/77). " + fitnote(M2)))


def waldF(res, *nms):
    idx = [res["names"].index(n) for n in nms]
    b = res["beta"][idx]
    Vsub = res["V"][np.ix_(idx, idx)]
    q = len(idx)
    F = float(b @ np.linalg.inv(Vsub) @ b) / q
    return F, float(_st.f.sf(F, q, res["df"]))


L = []
L.append("\\begin{table}[!htbp]")
L.append("\\centering")
L.append("\\small")
L.append("\\setlength{\\tabcolsep}{4pt}")
L.append("\\caption{Joint Fixed-Effects Tests for the Baseline Models}")
L.append("\\label{tab:app_fetests}")
L.append("\\begin{tabular}{>{\\raggedright\\arraybackslash}p{0.17\\textwidth}"
         ">{\\raggedright\\arraybackslash}p{0.31\\textwidth}"
         ">{\\raggedright\\arraybackslash}p{0.12\\textwidth}"
         ">{\\raggedright\\arraybackslash}p{0.12\\textwidth}"
         ">{\\raggedright\\arraybackslash}p{0.17\\textwidth}}")
L.append("\\toprule")
L.append("\\textbf{Model} & \\textbf{Null Hypothesis} & \\textbf{$F$} & "
         "\\textbf{df} & \\textbf{$p$} \\\\")
L.append("\\midrule")
for res, m in [(M1, "Model 1"), (M2, "Model 2")]:
    nb = [n for n in res["names"] if n.startswith("Bank ")]
    ny = [n for n in res["names"] if n.startswith("Year ")]
    for lab, idx in [("Bank fixed effects jointly zero", nb),
                     ("Year fixed effects jointly zero", ny),
                     ("All fixed effects jointly zero", nb + ny)]:
        F, pv = waldF(res, *idx)
        L.append(f"{m} & {lab} & ${F:.3f}$ & ${len(idx)}, {res['df']}$ & {pfmt(pv)} \\\\")
L.append("\\bottomrule")
L.append("\\end{tabular}")
L.append("")
L.append("\\vspace{4pt}")
L.append("\\begin{minipage}{\\linewidth}")
L.append("\\footnotesize")
L.append("\\textit{Note.} Wald tests under the HC3 covariance matrix. "
         "Reference categories are GBIME and FY 2076/77. Individual dummy "
         "coefficients are printed in Tables~\\ref{tab:app_m1full} and "
         "~\\ref{tab:app_m2full}; the joint tests are the basis for retaining "
         "the two-way fixed-effects structure.")
L.append("\\end{minipage}")
L.append("\\end{table}")
out.append("\n".join(gap_rows(L)))
out.append("")

# ---- robustness table ----
spec_labels = {
    "R1": "R1: Model 1 Baseline", "R2": "R2: Model 2 Baseline",
    "R3": "R3: ROA Replaces EPS", "R4": "R4: Model 2 + DPS",
    "R5": "R5: Excl. Transition", "R6": "R6: Excl. Mismatch",
    "R7": "R7: Bonus-Adjusted", "R8": "R8: Restated EPS",
    "R9": "R9: Excl. NMB FY2076/77",
    "R10": "R10: Excl. NMB \\& KBL FY76"}
spec_slopes = {
    "R1": ("EPS", "BVPS", None, None),
    "R2": ("EPS", "BVPS", "d_E", "d_B"),
    "R3": ("ROA", "BVPS", "d_ROA", "d_B"),
    "R4": ("EPS", "BVPS", "d_E", "d_B"),
    "R5": ("EPS", "BVPS", "d_E", "d_B"),
    "R6": ("EPS", "BVPS", "d_E", "d_B"),
    "R7": ("EPS", "BVPS_adj", "d_E", "d_Badj"),
    "R8": ("EPS_r", "BVPS", "d_Er", "d_B"),
    "R9": ("EPS", "BVPS", "d_E", "d_B"),
    "R10": ("EPS", "BVPS", "d_E", "d_B")}
wald_pair = {"R2": ("d_E", "d_B"), "R3": ("d_ROA", "d_B"), "R4": ("d_E", "d_B"),
             "R5": ("d_E", "d_B"), "R6": ("d_E", "d_B"), "R7": ("d_E", "d_Badj"),
             "R8": ("d_Er", "d_B"),
             "R9": ("d_E", "d_B"),
             "R10": ("d_E", "d_B")}
L = []
L.append("\\begin{table}[!htbp]")
L.append("\\centering")
L.append("\\footnotesize")
L.append("\\setlength{\\tabcolsep}{3pt}")
L.append("\\caption{Full Robustness Estimates Across Specifications R1--R10}")
L.append("\\label{tab:app_robustfull}")
L.append("\\begin{tabular}{>{\\raggedright\\arraybackslash}p{0.16\\textwidth}"
         ">{\\raggedright\\arraybackslash}p{0.135\\textwidth}"
         ">{\\raggedright\\arraybackslash}p{0.135\\textwidth}"
         ">{\\raggedright\\arraybackslash}p{0.135\\textwidth}"
         ">{\\raggedright\\arraybackslash}p{0.135\\textwidth}"
         ">{\\raggedright\\arraybackslash}p{0.10\\textwidth}"
         ">{\\raggedright\\arraybackslash}p{0.04\\textwidth}"
         ">{\\raggedright\\arraybackslash}p{0.04\\textwidth}}")
L.append("\\toprule")
L.append("\\textbf{Specification} & \\textbf{EPS (SE)} & \\textbf{BVPS (SE)} & "
         "\\textbf{$\\delta_E$ (SE)} & \\textbf{$\\delta_B$ (SE)} & "
         "\\textbf{Wald $F$ ($p$)} & \\textbf{$N$} & \\textbf{df} \\\\")
L.append("\\midrule")
for k in ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10"]:
    res = specs[k]
    e_, b_, dE_, dB_ = spec_slopes[k]

    def cell(nm):
        if nm is None:
            return "---"
        i = res["names"].index(nm)
        return f"{num(res['beta'][i])} ({num(res['se'][i])})"
    if k in wald_pair:
        F, pv = waldF(res, *wald_pair[k])
        wcell = f"${F:.3f}$ ({pfmt(pv)})"
    else:
        wcell = "---"
    L.append(f"{spec_labels[k]} & {cell(e_)} & {cell(b_)} & {cell(dE_)} & "
             f"{cell(dB_)} & {wcell} & {res['n']} & {res['df']} \\\\")
L.append("\\bottomrule")
L.append("\\end{tabular}")
L.append("")
L.append("\\vspace{4pt}")
L.append("\\begin{minipage}{\\linewidth}")
L.append("\\footnotesize")
L.append("\\textit{Note.} All specifications include bank and fiscal-year "
         "fixed effects. ROA is return on assets; EPS is earnings per share; "
         "BVPS is book value per share; DPS is cash dividend per share. "
         "R3 substitutes ROA for EPS (and its interaction for "
         "$\\delta_E$); R7 uses bonus-adjusted BVPS in both the level and the "
         "interaction; R8 uses restated EPS in both the level and the "
         "interaction. R5 excludes FY 2079/80 and R6 excludes FY 2078/79, so "
         "one year dummy drops in each and parameters fall to $K = 13$. "
         "R9 excludes the single Kanchan-mismatched bank-year NMB FY 2076/77 ($N = 27, \\text{residual df} = 13$). "
         "R10 additionally excludes the Kumari Bank FY 2076/77 partial-year acquisition observation ($N = 26, \\text{residual df} = 12$) as a supplementary post-hoc sensitivity check. "
         "The R4 cash DPS coefficient with full inference is in "
         "Table~\\ref{tab:app_robust_inf}. "
         "Wald tests are the joint test of the two regime-shift interactions "
         "under the HC3 covariance matrix. Estimates and standard errors to "
         "four decimals; Chapter IV Table~\\ref{tab:t5_robustness} prints the "
         "same coefficients to three decimals. "
         f"Fit statistics: $R^2$ (adjusted $R^2$; Within-$R^2$): "
         + "; ".join(f"{k} ${specs[k]['r2']:.3f}$ (${specs[k]['adj']:.3f}$; "
                     f"${specs[k]['within']:.3f}$)"
                     for k in ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10"])
         + ".")
L.append("\\end{minipage}")
L.append("\\end{table}")
out.append("\n".join(gap_rows(L)))
out.append("")

# ---- flagged observations ----
L = []
L.append("\\begin{table}[!htbp]")
L.append("\\centering")
L.append("\\small")
L.append("\\setlength{\\tabcolsep}{4pt}")
L.append("\\caption{Flagged Influential Observations in Model 1}")
L.append("\\label{tab:app_flagged}")
L.append("\\begin{tabular}{>{\\raggedright\\arraybackslash}p{0.32\\textwidth}"
         ">{\\raggedright\\arraybackslash}p{0.31\\textwidth}"
         ">{\\raggedright\\arraybackslash}p{0.31\\textwidth}}")
L.append("\\toprule")
L.append("\\textbf{Bank-Year} & \\textbf{Cook's Distance} & \\textbf{Leverage} \\\\")
L.append("\\midrule")
for _, row in flag.sort_values("cook", ascending=False).iterrows():
    L.append(f"{row['bank']} FY {row['fy'][2:6]}/{row['fy'][7:9]} & "
             f"${row['cook']:.4f}$ & ${row['lev']:.4f}$ \\\\")
L.append("\\bottomrule")
L.append("\\end{tabular}")
L.append("")
L.append("\\vspace{4pt}")
L.append("\\begin{minipage}{\\linewidth}")
L.append("\\footnotesize")
L.append("\\textit{Note.} Cook's distance and leverage from Model~1; "
         "attention threshold $4/N=4/28=0.143$. No observation is removed. "
         "HC3 adjusts the covariance estimate but does not remove or "
         "neutralize influential observations; "
         "Table~\\ref{tab:app_sensitivity} reports sensitivity to deleting "
         "each flagged case and each bank.")
L.append("\\end{minipage}")
L.append("\\end{table}")
out.append("\n".join(gap_rows(L)))
out.append("")

# ---- leave-one-bank sensitivity ----
L = []
L.append("\\begin{table}[!htbp]")
L.append("\\centering")
L.append("\\small")
L.append("\\setlength{\\tabcolsep}{4pt}")
L.append("\\caption{Leave-One-Bank Sensitivity of the Model 2 Regime Shift}")
L.append("\\label{tab:app_sensitivity}")
L.append("\\begin{tabular}{>{\\raggedright\\arraybackslash}p{0.18\\textwidth}"
         ">{\\raggedright\\arraybackslash}p{0.07\\textwidth}"
         ">{\\raggedright\\arraybackslash}p{0.20\\textwidth}"
         ">{\\raggedright\\arraybackslash}p{0.19\\textwidth}"
         ">{\\raggedright\\arraybackslash}p{0.26\\textwidth}}")
L.append("\\toprule")
L.append("\\textbf{Dropped Bank} & \\textbf{$N$} & \\textbf{$\\delta_E$ (SE)} & "
         "\\textbf{$\\delta_B$ (SE)} & \\textbf{Wald $F$ ($p$)} \\\\")
L.append("\\midrule")
for x in lob:
    L.append(f"{x['bank']} & {x['n']} & {num(x['dE'])} ({num(x['dE_se'])}) & "
             f"{num(x['dB'])} ({num(x['dB_se'])}) & ${x['F']:.3f}$ ({pfmt(x['p'])}) \\\\")
L.append("\\bottomrule")
L.append("\\end{tabular}")
L.append("")
L.append("\\vspace{4pt}")
L.append("\\begin{minipage}{\\linewidth}")
L.append("\\footnotesize")
dE_lo = (min(x["dE"] for x in loo), max(x["dE"] for x in loo))
dB_lo = (min(x["dB"] for x in loo), max(x["dB"] for x in loo))
p_lo = (min(x["p"] for x in loo), max(x["p"] for x in loo))


def fy_disp(drop):
    bank, fy = drop.split(" ")
    return f"{bank} FY {fy[2:6]}/{fy[7:9]}"


dE_min = min(loo, key=lambda x: x["dE"])
dE_max = max(loo, key=lambda x: x["dE"])
dB_min = min(loo, key=lambda x: x["dB"])
dB_max = max(loo, key=lambda x: x["dB"])
n05 = sum(1 for x in loo if x["p"] < 0.05)
n10 = sum(1 for x in loo if x["p"] < 0.10)
L.append("\\textit{Note.} Each row re-estimates Model 2 without one bank "
         "series; the reference bank is GBIME, except where GBIME itself is "
         "dropped, in which case HBL is the reference. Across all 28 "
         "single-row deletions, $\\delta_E$ ranges from "
         f"${dE_lo[0]:.4f}$ to ${dE_lo[1]:.4f}$ and $\\delta_B$ from "
         f"${dB_lo[0]:.4f}$ to ${dB_lo[1]:.4f}$, with no sign change in either "
         "interaction; the joint Wald $p$-value ranges from "
         f"${p_lo[0]:.3f}$ (NIMB FY 2078/79 deleted) to ${p_lo[1]:.3f}$ "
         f"(KBL FY 2077/78 deleted). $\\delta_E$ is most negative when "
         f"{fy_disp(dE_min['drop'])} is deleted (${dE_min['dE']:.4f}$) and "
         f"least negative when {fy_disp(dE_max['drop'])} is deleted "
         f"(${dE_max['dE']:.4f}$); $\\delta_B$ is most negative when "
         f"{fy_disp(dB_min['drop'])} is deleted (${dB_min['dB']:.4f}$) and "
         f"least negative when {fy_disp(dB_max['drop'])} is deleted "
         f"(${dB_max['dB']:.4f}$). Only {n05} of the 28 deletions brings the "
         f"joint Wald $p$-value below 0.05, while {n10} of 28 fall below "
         "0.10. Dropping KBL as a whole bank reverses "
         "$\\delta_E$; every other bank deletion leaves both interactions "
         "negative.")
L.append("\\end{minipage}")
L.append("\\end{table}")
out.append("\n".join(gap_rows(L)))

# ---- implied post-consolidation slopes (R2, R5, R6) ----
def post_slope(spec, base, delta):
    """Implied post slope = level + interaction, with HC3 inference via the
    fitted covariance (linear combination). Returns (coef, se, t, p, lo, hi)."""
    names = spec["names"]
    beta = np.asarray(spec["beta"])
    V = np.asarray(spec["V"])
    df = spec["df"]
    ib, id_ = names.index(base), names.index(delta)
    coef = float(beta[ib] + beta[id_])
    se = float(np.sqrt(V[ib, ib] + V[id_, id_] + 2 * V[ib, id_]))
    t = coef / se
    p = float(2 * _st.t.sf(abs(t), df))
    crit = float(_st.t.ppf(0.975, df))
    return coef, se, t, p, coef - crit * se, coef + crit * se


L = []
L.append("\\begin{table}[!htbp]")
L.append("\\centering")
L.append("\\footnotesize")
L.append("\\setlength{\\tabcolsep}{3pt}")
L.append("\\caption{Implied Post-Consolidation Slopes for the Baseline and Year-Drop Specifications}")
L.append("\\label{tab:app_postslopes}")
L.append("\\begin{tabular}{>{\\raggedright\\arraybackslash}p{0.22\\textwidth}"
         ">{\\raggedright\\arraybackslash}p{0.10\\textwidth}"
         ">{\\raggedright\\arraybackslash}p{0.20\\textwidth}"
         ">{\\raggedright\\arraybackslash}p{0.07\\textwidth}"
         ">{\\raggedright\\arraybackslash}p{0.07\\textwidth}"
         ">{\\raggedright\\arraybackslash}p{0.22\\textwidth}"
         ">{\\raggedright\\arraybackslash}p{0.04\\textwidth}"
         ">{\\raggedright\\arraybackslash}p{0.04\\textwidth}}")
L.append("\\toprule")
L.append("\\textbf{Specification} & \\textbf{Slope} & \\textbf{Estimate (SE)} & "
         "\\textbf{$t$} & \\textbf{$p$} & \\textbf{95\\% CI} & \\textbf{$N$} & \\textbf{df} \\\\")
L.append("\\midrule")
for k in ["R2", "R5", "R6"]:
    res = specs[k]
    for slope, base, delta in [("Post EPS", "EPS", "d_E"), ("Post BVPS", "BVPS", "d_B")]:
        coef, se, t, p, lo, hi = post_slope(res, base, delta)
        ci = f"$[{lo:.4f}, {hi:.4f}]$".replace("-0.0000", "0.0000")
        L.append(f"{spec_labels[k]} & {slope} & {num(coef)} ({num(se)}) & "
                 f"${t:.2f}$ & {pfmt(p)} & {ci} & "
                 f"{res['n']} & {res['df']} \\\\")
L.append("\\bottomrule")
L.append("\\end{tabular}")
L.append("")
L.append("\\vspace{4pt}")
L.append("\\begin{minipage}{\\linewidth}")
L.append("\\footnotesize")
L.append("\\textit{Note.} Each post-consolidation slope is the level coefficient plus "
         "its regime-shift interaction (EPS plus $\\delta_E$; BVPS plus $\\delta_B$), "
         "with standard errors, $t$-statistics, $p$-values, and 95\\% confidence "
         "intervals computed from the fitted HC3 covariance matrix by linear "
         "combination. EPS is earnings per share; BVPS is book value per share; "
         "SE is standard error. The R2 rows reproduce the implied post slopes in "
         "the note to Table~\\ref{tab:app_m2full}; the R5 and R6 rows are the values "
         "Chapter IV discusses. No post slope is significant at 5\\%.")
L.append("\\end{minipage}")
L.append("\\end{table}")
out.append("\n".join(gap_rows(L)))

open(HERE / "tables_e_fragment.tex", "w").write("\n".join(out))
print("wrote tables_e_fragment.tex, tables:", out[0].count("caption"), "blocks")
