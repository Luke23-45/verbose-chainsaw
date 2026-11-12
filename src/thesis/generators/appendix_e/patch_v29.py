"""Mechanical v29 substitutions: eight->nine suite, R8->R9 ranges, R9 labels.
Every pair asserts its expected occurrence count; the script aborts on any
mismatch so a missed or double-applied edit is caught, not silently passed.
Content insertions (new rows/paragraphs) are done separately by hand edit.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
W = str(HERE) + "/"
T = str(REPO / "src/thesis") + "/"
EN = chr(8213)  # en-dash, used in the App C long caption

# (path, old, new, expected_count)
PAIRS = [
    # ---- gen_tables_e.py: robustfull ----
    (W + "gen_tables_e.py",
     r'''"R7": "R7: Bonus-Adjusted", "R8": "R8: Restated EPS"}''',
     r'''"R7": "R7: Bonus-Adjusted", "R8": "R8: Restated EPS",
    "R9": "R9: Excl. NMB FY2076/77"}''', 1),
    (W + "gen_tables_e.py",
     r'''"R8": ("EPS_r", "BVPS", "d_Er", "d_B")}''',
     r'''"R8": ("EPS_r", "BVPS", "d_Er", "d_B"),
    "R9": ("EPS", "BVPS", "d_E", "d_B")}''', 1),
    (W + "gen_tables_e.py",
     r'''"R8": ("d_Er", "d_B")}''',
     r'''"R8": ("d_Er", "d_B"),
             "R9": ("d_E", "d_B")}''', 1),
    (W + "gen_tables_e.py",
     r"""Full Robustness Estimates Across Specifications R1--R8""",
     r"""Full Robustness Estimates Across Specifications R1--R9""", 1),
    (W + "gen_tables_e.py",
     r"""for k in ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8"]:""",
     r"""for k in ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9"]:""", 1),
    (W + "gen_tables_e.py",
     r"""for k in ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8"])""",
     r"""for k in ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9"])""", 1),
    (W + "gen_tables_e.py",
     r"""one year dummy drops in each and parameters fall to $K = 13$. """,
     r"""one year dummy drops in each and parameters fall to $K = 13$. """
     r"""R9 excludes the single Kanchan-mismatched bank-year NMB FY 2076/77, """
     r"""so no dummy drops and parameters remain $K = 14$. """, 1),
    # ---- gen_tables_e2.py ----
    (W + "gen_tables_e2.py",
     r"""robustness inference (R3-R8)""",
     r"""robustness inference (R3-R9)""", 1),
    (W + "gen_tables_e2.py",
     r"""robustness dummies (R6-R8)""",
     r"""robustness dummies (R6-R9)""", 1),
    (W + "gen_tables_e2.py",
     r"""joint FE tests (R3-R8)""",
     r"""joint FE tests (R3-R9)""", 1),
    (W + "gen_tables_e2.py",
     r'''"R8": ("R8: Restated EPS",
           [("EPS_r", "EPS (restated)"), ("BVPS", "BVPS"),
            ("d_Er", "$\delta_E$ (restated)"), ("d_B", "$\delta_B$")]),''',
     r'''"R8": ("R8: Restated EPS",
           [("EPS_r", "EPS (restated)"), ("BVPS", "BVPS"),
            ("d_Er", "$\delta_E$ (restated)"), ("d_B", "$\delta_B$")]),
    "R9": ("R9: Excl. NMB FY2076/77",
           [("EPS", "EPS"), ("BVPS", "BVPS"), ("d_E", "$\delta_E$"),
            ("d_B", "$\delta_B$")]),''', 1),
    (W + "gen_tables_e2.py",
     r"""for k in ["R3", "R4", "R5", "R6", "R7", "R8"]:""",
     r"""for k in ["R3", "R4", "R5", "R6", "R7", "R8", "R9"]:""", 2),
    (W + "gen_tables_e2.py",
     r"""Robustness Coefficient Inference (R3--R8)""",
     r"""Robustness Coefficient Inference (R3--R9)""", 1),
    (W + "gen_tables_e2.py",
     r"""Fixed-effect dummies for R3--R8""",
     r"""Fixed-effect dummies for R3--R9""", 1),
    (W + "gen_tables_e2.py",
     r"""Robustness Fixed-Effect Dummy Coefficients (R6--R8)""",
     r"""Robustness Fixed-Effect Dummy Coefficients (R6--R9)""", 1),
    (W + "gen_tables_e2.py",
     r"""         ["R6", "R7", "R8"])]""",
     r"""         ["R6", "R7", "R8", "R9"])]""", 1),
    (W + "gen_tables_e2.py",
     r'''"R7": "R7: Bonus-Adjusted", "R8": "R8: Restated EPS"}''',
     r'''"R7": "R7: Bonus-Adjusted", "R8": "R8: Restated EPS",
              "R9": "R9: Excl. NMB FY2076/77"}''', 1),
    (W + "gen_tables_e2.py",
     r"""dummy is absent in each. Joint fixed-effect tests for R3--R8 are """,
     r"""dummy is absent in each. R9 drops only one bank-year, so all """
     r"""dummies are present. Joint fixed-effect tests for R3--R9 are """, 1),
    # ---- appendix_e_prose.tex ----
    (W + "appendix_e_prose.tex",
     r"""the full eight-specification robustness suite""",
     r"""the full nine-specification robustness suite""", 1),
    (W + "appendix_e_prose.tex",
     r"""for R3 through R8""",
     r"""for R3 through R9""", 2),
    (W + "appendix_e_prose.tex",
     r"""range from 0.085 (R2) to 0.139 (R5)""",
     r"""range from 0.085 (R2) to 0.205 (R9)""", 1),
    # ---- chapters / appendices: suite phrases ----
    (T + "chapters/chapter_05_summary_and_conclusion.tex",
     r"""eight-specification estimation and robustness suite (R1--R2 baselines plus six robustness variants R3--R8)""",
     r"""nine-specification estimation and robustness suite (R1--R2 baselines plus seven robustness variants R3--R9)""", 1),
    (T + "chapters/chapter_01_introduction.tex",
     r"""eight-specification estimation and robustness suite (R1--R2 baselines plus six robustness variants R3--R8)""",
     r"""nine-specification estimation and robustness suite (R1--R2 baselines plus seven robustness variants R3--R9)""", 1),
    (T + "chapters/chapter_01_introduction.tex",
     r"""reports the results of the eight-specification estimation and robustness suite;""",
     r"""reports the results of the nine-specification estimation and robustness suite;""", 1),
    (T + "chapters/chapter_03_research_methodology.tex",
     r"""eight-specification estimation and robustness suite (R1--R2 baselines plus six robustness variants R3--R8)""",
     r"""nine-specification estimation and robustness suite (R1--R2 baselines plus seven robustness variants R3--R9)""", 1),
    (T + "chapters/chapter_04_results_and_discussion.tex",
     r"""eight-specification suite (R1--R2 baselines plus six robustness variants R3--R8)""",
     r"""nine-specification suite (R1--R2 baselines plus seven robustness variants R3--R9)""", 1),
    (T + "chapters/chapter_03_research_methodology.tex",
     r"""an eight-specification suite comprising the two baseline models (R1--R2) and six robustness variants (R3--R8)""",
     r"""a nine-specification suite comprising the two baseline models (R1--R2) and seven robustness variants (R3--R9)""", 1),
    (T + "chapters/chapter_04_results_and_discussion.tex",
     r"""an eight-specification suite comprising the two baseline models (R1--R2) and six robustness variants (R3--R8)""",
     r"""a nine-specification suite comprising the two baseline models (R1--R2) and seven robustness variants (R3--R9)""", 1),
    (T + "chapters/chapter_03_research_methodology.tex",
     r"""structured eight-specification suite comprising the two baseline models and six robustness variants (Specifications R1 to R8)""",
     r"""structured nine-specification suite comprising the two baseline models and seven robustness variants (Specifications R1 to R9)""", 1),
    (T + "chapters/chapter_03_research_methodology.tex",
     r"""The Eight-Specification Estimation and Robustness Suite""",
     r"""The Nine-Specification Estimation and Robustness Suite""", 1),
    (T + "chapters/chapter_04_results_and_discussion.tex",
     r"""Robustness and Sensitivity Analyses (R1 through R8)""",
     r"""Robustness and Sensitivity Analyses (R1 through R9)""", 2),
    (T + "appendices/appendix_c.tex",
     r"""eightfold sensitivity suite (R1 through R8)""",
     r"""ninefold sensitivity suite (R1 through R9)""", 1),
    (T + "appendices/appendix_c.tex",
     r"""Comparative Coefficient Forest Plot (R1--R8)""",
     r"""Comparative Coefficient Forest Plot (R1--R9)""", 1),
    (T + "appendices/appendix_c.tex",
     "Across Robustness Specifications R1" + EN + "R8",
     "Across Robustness Specifications R1" + EN + "R9", 1),
    (T + "appendices/appendix_d.tex",
     r"""The eight-specification suite is:""",
     r"""The nine-specification suite is:""", 1),
    (T + "appendices/appendix_d.tex",
     r"""R8, Model 2 with restated EPS as defined in Section D.4.""",
     r"""R8, Model 2 with restated EPS as defined in Section D.4; R9, Model 2 excluding the single Kanchan-mismatched bank-year NMB FY 2076/77 ($N = 27$, residual degrees of freedom 13).""", 1),
    (T + "appendices/appendix_d.tex",
     r"""Run specifications R1 through R8 as defined in Section D.6.""",
     r"""Run specifications R1 through R9 as defined in Section D.6.""", 1),
    # ---- Ch4 forest plot wording ----
    (T + "chapters/chapter_04_results_and_discussion.tex",
     r"""across seven robustness specifications (R1, R2, and R4 through R8)""",
     r"""across eight robustness specifications (R1, R2, and R4 through R9)""", 1),
    (T + "chapters/chapter_04_results_and_discussion.tex",
     r"""Robustness Forest Plot Across Seven Specifications (R1, R2, R4--R8)""",
     r"""Robustness Forest Plot Across Eight Specifications (R1, R2, R4--R9)""", 1),
    (T + "chapters/chapter_04_results_and_discussion.tex",
     r"""across seven specifications (R1, R2, R4--R8; R3 omitted because ROA is on a different scale; $N = 28$ or $N = 23$)""",
     r"""across eight specifications (R1, R2, R4--R9; R3 omitted because ROA is on a different scale; $N = 28$, $N = 27$, or $N = 23$)""", 1),
    # ---- Ch4 Table 8 note ----
    (T + "chapters/chapter_04_results_and_discussion.tex",
     r"""Residual degrees of freedom: R1 16; R2, R3, R7, R8 14; R4 13; R5, R6 10.""",
     r"""Residual degrees of freedom: R1 16; R2, R3, R7, R8 14; R4, R9 13; R5, R6 10.""", 1),
    (T + "chapters/chapter_04_results_and_discussion.tex",
     r"""R8: Restated basic EPS substituted for GBIME FY 2076/77 and NMB FY 2077/78 ($N = 28$).""",
     r"""R8: Restated basic EPS substituted for GBIME FY 2076/77 and NMB FY 2077/78 ($N = 28$). R9: Single Kanchan-mismatched bank-year NMB FY 2076/77 dropped ($N = 27$).""", 1),
    # ---- Ch5 content ----
    (T + "chapters/chapter_05_summary_and_conclusion.tex",
     r"""The eight-specification suite (R1--R8) did not reject parameter stability at the 5\% level across ROA substitution (R3), cash dividend inclusion (R4, residual $\text{df} = 13$), transition-year removal (R5), bonus share dilution (R7), and restated basic earnings (R8), except under Specification R6""",
     r"""The nine-specification suite (R1--R9) did not reject parameter stability at the 5\% level across ROA substitution (R3), cash dividend inclusion (R4, residual $\text{df} = 13$), transition-year removal (R5), bonus share dilution (R7), restated basic earnings (R8), and Kanchan-mismatched bank-year removal (R9, residual $\text{df} = 13$), except under Specification R6""", 1),
    (T + "chapters/chapter_05_summary_and_conclusion.tex",
     r"""bonus share dilution adjustments (R7), and restated basic earnings (R8).""",
     r"""bonus share dilution adjustments (R7), restated basic earnings (R8), and Kanchan-mismatched bank-year removal (R9).""", 1),
    (T + "chapters/chapter_05_summary_and_conclusion.tex",
     r"""prices are measured post-disclosure""",
     r"""prices are measured after the statutory reporting deadline""", 1),
]

failed = 0
for path, old, new, expect in PAIRS:
    text = open(path).read()
    n = text.count(old)
    if n != expect:
        print(f"FAIL {path.split('/')[-1]}: expected {expect}, found {n} for: {old[:70]!r}")
        failed += 1
        continue
    open(path, "w").write(text.replace(old, new))
    print(f"ok {path.split('/')[-1]}: {old[:60]!r} x{n}")
print("FAILED" if failed else "ALL PATCHES APPLIED")
sys.exit(1 if failed else 0)
