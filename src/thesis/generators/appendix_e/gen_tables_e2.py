"""Generate the six round-2 Appendix E tables from verified results.

Tables: robustness inference (R3-R9), robustness dummies (R3-R5),
robustness dummies (R6-R9), joint FE tests (R3-R9), Model 2 flagged
observations, leave-one-year sensitivity. Every cell comes from
results.pkl / results2.pkl; nothing is hand-typed.
"""
import pickle
from pathlib import Path

import numpy as np
from scipy import stats as _st

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]

r = pickle.load(open(HERE / "results.pkl", "rb"))
r2 = pickle.load(open(HERE / "results2.pkl", "rb"))
specs = r["specs"]
flag2, loy, fe_tests = r2["flag2"], r2["loy"], r2["fe_tests"]
bp_lm, bp_p = r2["bp"]


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
        if line.endswith("\\\\") and not line.startswith("\\multicolumn") and not line.startswith("\\textbf") and not line.startswith("\\label"):
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            if nxt and nxt != "\\bottomrule":
                out.append("\\addlinespace")
    return out


SIXCOL = ("\\begin{tabular}{>{\\raggedright\\arraybackslash}p{0.20\\textwidth}"
          ">{\\raggedright\\arraybackslash}p{0.12\\textwidth}"
          ">{\\raggedright\\arraybackslash}p{0.12\\textwidth}"
          ">{\\raggedright\\arraybackslash}p{0.07\\textwidth}"
          ">{\\raggedright\\arraybackslash}p{0.09\\textwidth}"
          ">{\\raggedright\\arraybackslash}p{0.27\\textwidth}}")


def open_table(caption, label, small="\\small", tabcolsep=4, tabular=SIXCOL):
    return ["\\begin{table}[!htbp]", "\\centering", small,
            f"\\setlength{{\\tabcolsep}}{{{tabcolsep}pt}}",
            f"\\caption{{{caption}}}", f"\\label{{{label}}}", tabular,
            "\\toprule"]


def open_longtable(caption, label, header, tabular=SIXCOL):
    """Longtable opening with the header repeated on every page (same
    pattern as Chapter II Table 2.1 and Appendix D Tables 14-15). The
    caller closes with \\end{longtable}} and puts the note after it,
    calling note_block with end_table=False."""
    lt = tabular.replace("\\begin{tabular}", "\\begin{longtable}", 1)
    return ["{\\small",
            "\\setlength{\\tabcolsep}{4pt}",
            lt,
            f"\\caption{{{caption}}}",
            f"\\label{{{label}}}\\\\",
            "\\toprule",
            header,
            "\\midrule",
            "\\endfirsthead",
            header,
            "\\midrule",
            "\\endhead"]


def note_block(text, end_table=True):
    out = ["", "\\vspace{4pt}", "\\begin{minipage}{\\linewidth}",
           "\\footnotesize", f"\\textit{{Note.}} {text}",
           "\\end{minipage}"]
    if end_table:
        out.append("\\end{table}")
    return out


def full_rows(res, names_disp):
    """Rows for a 6-column full-inference table; names_disp maps internal
    name -> display label; order follows res['names'] filtered to the map."""
    L = []
    for nm, disp in names_disp:
        i = res["names"].index(nm)
        L.append(f"{disp} & {num(res['beta'][i])} & {num(res['se'][i])} & "
                 f"${res['t'][i]:.2f}$ & {pfmt(res['p'][i])} & {cirow(res, nm)} \\\\")
    return L


def header6():
    return ("\\textbf{Variable} & \\textbf{Estimate} & \\textbf{HC3 SE} & "
            "\\textbf{$t$} & \\textbf{$p$} & \\textbf{95\\% CI} \\\\")


out = []

# ---- 1. Robustness inference R3-R8 ----
spec_inf = {
    "R3": ("R3: ROA Replaces EPS",
           [("ROA", "ROA"), ("BVPS", "BVPS"),
            ("d_ROA", "$\\delta_{ROA}$"), ("d_B", "$\\delta_B$")]),
    "R4": ("R4: Model 2 + DPS",
           [("EPS", "EPS"), ("BVPS", "BVPS"), ("d_E", "$\\delta_E$"),
            ("d_B", "$\\delta_B$"), ("DPS", "DPS")]),
    "R5": ("R5: Excl. Transition",
           [("EPS", "EPS"), ("BVPS", "BVPS"), ("d_E", "$\\delta_E$"),
            ("d_B", "$\\delta_B$")]),
    "R6": ("R6: Excl. Mismatch",
           [("EPS", "EPS"), ("BVPS", "BVPS"), ("d_E", "$\\delta_E$"),
            ("d_B", "$\\delta_B$")]),
    "R7": ("R7: Bonus-Adjusted",
           [("EPS", "EPS"), ("BVPS_adj", "BVPS (bonus-adjusted)"),
            ("d_E", "$\\delta_E$"),
            ("d_Badj", "$\\delta_B$ (bonus-adjusted)")]),
    "R8": ("R8: Restated EPS",
           [("EPS_r", "EPS (restated)"), ("BVPS", "BVPS"),
            ("d_Er", "$\\delta_E$ (restated)"), ("d_B", "$\\delta_B$")]),
    "R9": ("R9: Excl. NMB FY2076/77",
           [("EPS", "EPS"), ("BVPS", "BVPS"), ("d_E", "$\\delta_E$"),
            ("d_B", "$\\delta_B$")]),
}
L = open_longtable("Robustness Coefficient Inference (R3--R9)",
                   "tab:app_robust_inf", header6())
for k in ["R3", "R4", "R5", "R6", "R7", "R8", "R9"]:
    title, rows = spec_inf[k]
    L.append(f"\\multicolumn{{6}}{{l}}{{\\textbf{{{title}}}}} \\\\*")
    L.extend(full_rows(specs[k], rows))
L.append("\\bottomrule")
L.append("\\end{longtable}}")
L.extend(note_block(
    "R1 and R2 inference is in Tables~\\ref{tab:app_m1full} and "
    "~\\ref{tab:app_m2full}. Fixed-effect dummies for R3--R9 are in "
    "Tables~\\ref{tab:app_robust_fe1} and~\\ref{tab:app_robust_fe2}. "
    "Estimates, standard errors, and confidence limits to four decimals; "
    "t-statistics to two decimals; p-values to three decimals.", end_table=False))
out.append("\n".join(gap_rows(L)))
out.append("")

# ---- 2/3. Robustness dummies ----
def dummy_rows(res):
    rows = []
    for nm in res["names"]:
        if nm.startswith("Bank "):
            disp = nm
        elif nm.startswith("Year "):
            _, fy = nm.split(" ", 1)
            disp = "Year FY " + fy[2:6] + "/" + fy[7:9]
        else:
            continue
        i = res["names"].index(nm)
        rows.append(f"{disp} & {num(res['beta'][i])} & {num(res['se'][i])} & "
                    f"${res['t'][i]:.2f}$ & {pfmt(res['p'][i])} & {cirow(res, nm)} \\\\")
    return rows


for label, caption, group in [
        ("tab:app_robust_fe1",
         "Robustness Fixed-Effect Dummy Coefficients (R3--R5)",
         ["R3", "R4", "R5"]),
        ("tab:app_robust_fe2",
         "Robustness Fixed-Effect Dummy Coefficients (R6--R9)",
         ["R6", "R7", "R8", "R9"])]:
    # Both dummy tables are longtables. fe1 is too tall to fit as a float
    # in the space left after Table 23, and a deferred float would print
    # after Table 25 (out of order); fe2 never fit one page at all.
    is_long = True
    if is_long:
        L = open_longtable(caption, label, header6())
    else:
        L = open_table(caption, label)
        L.append(header6())
        L.append("\\midrule")
    titles = {"R3": "R3: ROA Replaces EPS", "R4": "R4: Model 2 + DPS",
              "R5": "R5: Excl. Transition", "R6": "R6: Excl. Mismatch",
              "R7": "R7: Bonus-Adjusted", "R8": "R8: Restated EPS",
              "R9": "R9: Excl. NMB FY2076/77"}
    sub_end = "\\\\*" if is_long else "\\\\"
    for k in group:
        L.append(f"\\multicolumn{{6}}{{l}}{{\\textbf{{{titles[k]}}}}} {sub_end}")
        L.extend(dummy_rows(specs[k]))
    L.append("\\bottomrule")
    if is_long:
        L.append("\\end{longtable}}")
    else:
        L.append("\\end{tabular}")
    L.extend(note_block(
        "Reference categories are GBIME and FY 2076/77. R5 excludes FY "
        "2079/80 and R6 excludes FY 2078/79, so the corresponding year "
        "dummy is absent in each. R9 drops only one bank-year, so all dummies are present. Joint fixed-effect tests for R3--R9 are "
        "in Table~\\ref{tab:app_robust_fetests}. Estimates, standard "
        "errors, and confidence limits to four decimals; t-statistics to "
        "two decimals; p-values to three decimals.", end_table=not is_long))
    out.append("\n".join(gap_rows(L)))
    out.append("")

# ---- 4. Joint FE tests R3-R8 (Table 21 layout) ----
L = open_table("Joint Fixed-Effects Tests for the Robustness Specifications",
               "tab:app_robust_fetests")
L[2] = "\\small"
# replace tabular spec with the 5-column one used by Table 21
L[6] = ("\\begin{tabular}{>{\\raggedright\\arraybackslash}p{0.17\\textwidth}"
        ">{\\raggedright\\arraybackslash}p{0.31\\textwidth}"
        ">{\\raggedright\\arraybackslash}p{0.12\\textwidth}"
        ">{\\raggedright\\arraybackslash}p{0.12\\textwidth}"
        ">{\\raggedright\\arraybackslash}p{0.17\\textwidth}}")
L.append("\\textbf{Specification} & \\textbf{Null Hypothesis} & \\textbf{$F$} & "
         "\\textbf{df} & \\textbf{$p$} \\\\")
L.append("\\midrule")
for k in ["R3", "R4", "R5", "R6", "R7", "R8", "R9"]:
    t = fe_tests[k]
    L.append(f"{k} & Bank fixed effects jointly zero & ${t['bank'][0]:.3f}$ & "
             f"${t['n_bank']}, {t['df']}$ & {pfmt(t['bank'][1])} \\\\")
    L.append(f"{k} & Year fixed effects jointly zero & ${t['year'][0]:.3f}$ & "
             f"${t['n_year']}, {t['df']}$ & {pfmt(t['year'][1])} \\\\")
    L.append(f"{k} & All fixed effects jointly zero & ${t['both'][0]:.3f}$ & "
             f"${t['n_bank'] + t['n_year']}, {t['df']}$ & {pfmt(t['both'][1])} \\\\")
L.append("\\bottomrule")
L.append("\\end{tabular}")
L.extend(note_block(
    "Wald tests under the HC3 covariance matrix. Reference categories are "
    "GBIME and FY 2076/77. Denominator degrees of freedom equal the "
    "specification residual degrees of freedom in "
    "Table~\\ref{tab:app_robustfull}."))
out.append("\n".join(gap_rows(L)))
out.append("")

# ---- 5. Model 2 flagged observations ----
L = open_table("Flagged Influential Observations in Model 2",
               "tab:app_m2flagged")
L[6] = ("\\begin{tabular}{>{\\raggedright\\arraybackslash}p{0.32\\textwidth}"
        ">{\\raggedright\\arraybackslash}p{0.31\\textwidth}"
        ">{\\raggedright\\arraybackslash}p{0.31\\textwidth}}")
L.append("\\textbf{Bank-Year} & \\textbf{Cook's Distance} & \\textbf{Leverage} \\\\")
L.append("\\midrule")
for _, row in flag2.iterrows():
    L.append(f"{row['bank']} FY {row['fy'][2:6]}/{row['fy'][7:9]} & "
             f"${row['cook']:.4f}$ & ${row['lev']:.4f}$ \\\\")
L.append("\\bottomrule")
L.append("\\end{tabular}")
L.extend(note_block(
    "Cook's distance and leverage from Model~2; attention threshold "
    "$4/N=4/28=0.143$. The Koenker robust Breusch-Pagan LM statistic on Model~2 "
    f"residuals is ${bp_lm:.2f}$ on 13 degrees of freedom "
    f"($p={bp_p:.3f}$). No observation is removed. HC3 adjusts the covariance "
    "estimate but does not remove or neutralize influential observations; "
    "Tables~\\ref{tab:app_sensitivity} and~\\ref{tab:app_loy} report sensitivity "
    "to deleting flagged cases, banks, and years."))
out.append("\n".join(gap_rows(L)))
out.append("")

# ---- 6. Leave-one-year sensitivity ----
L = open_table("Leave-One-Year Sensitivity of the Model 2 Regime Shift",
               "tab:app_loy")
L[6] = ("\\begin{tabular}{>{\\raggedright\\arraybackslash}p{0.18\\textwidth}"
        ">{\\raggedright\\arraybackslash}p{0.07\\textwidth}"
        ">{\\raggedright\\arraybackslash}p{0.20\\textwidth}"
        ">{\\raggedright\\arraybackslash}p{0.19\\textwidth}"
        ">{\\raggedright\\arraybackslash}p{0.26\\textwidth}}")
L.append("\\textbf{Dropped Year} & \\textbf{$N$} & \\textbf{$\\delta_E$ (SE)} & "
         "\\textbf{$\\delta_B$ (SE)} & \\textbf{Wald $F$ ($p$)} \\\\")
L.append("\\midrule")
for y in ["FY2076-77", "FY2077-78", "FY2078-79", "FY2079-80", "FY2080-81", "FY2081-82"]:
    x = loy[y]
    disp = f"FY {y[2:6]}/{y[7:9]}"
    L.append(f"{disp} & {x['n']} & {num(x['dE'])} ({num(x['dE_se'])}) & "
             f"{num(x['dB'])} ({num(x['dB_se'])}) & ${x['F']:.3f}$ ({pfmt(x['p'])}) \\\\")
L.append("\\bottomrule")
L.append("\\end{tabular}")
L.extend(note_block(
    "Each row re-estimates Model 2 without one fiscal year; the reference "
    "year is FY 2076/77 except where FY 2076/77 itself is dropped, in which "
    "case FY 2077/78 is the reference. The FY 2078/79 and FY 2079/80 rows "
    "repeat R6 and R5 from Table~\\ref{tab:app_robustfull}. No deletion "
    "changes the sign of either interaction."))
out.append("\n".join(gap_rows(L)))

open(HERE / "tables_e2_fragment.tex", "w").write("\n".join(out))
print("wrote tables_e2_fragment.tex")
for t in out:
    if "\\caption" in t:
        print(" -", t.split("\\caption{")[1].split("}")[0][:60])
