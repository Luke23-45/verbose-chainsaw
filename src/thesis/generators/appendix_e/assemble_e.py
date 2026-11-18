"""Assemble appendix_e.tex: prose + 13 table blocks in position order.

frag1 (gen_tables_e.py): m1full, m2full, fetests, robustfull, flagged,
                           sensitivity, postslopes
frag2 (gen_tables_e2.py): robust_inf, robust_fe1, robust_fe2, robust_fetests,
                           m2flagged, loy
Position order: T01..T03 = frag1[0..2]; T04 = frag1[3]; T05 = frag1[6];
                T06..T09 = frag2[0..3]; T10 = frag1[4]; T11 = frag2[4];
                T12 = frag1[5]; T13 = frag2[5]
"""
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
W = str(HERE) + "/"


def blocks(path):
    text = open(path).read()
    # Tables start with \begin{table}; longtables start with {\small
    # followed by \begin{longtable}. Both must split into their own block.
    parts = [p for p in re.split(r"(?=\\begin\{table\})|(?=\{\\small)", text) if p.strip()]
    return parts


f1 = blocks(W + "tables_e_fragment.tex")
f2 = blocks(W + "tables_e2_fragment.tex")
assert len(f1) == 7, len(f1)
assert len(f2) == 6, len(f2)

order = [
    (f1[0], "tab:app_m1full"), (f1[1], "tab:app_m2full"),
    (f1[2], "tab:app_fetests"), (f1[3], "tab:app_robustfull"),
    (f1[6], "tab:app_postslopes"),
    (f2[0], "tab:app_robust_inf"), (f2[1], "tab:app_robust_fe1"),
    (f2[2], "tab:app_robust_fe2"), (f2[3], "tab:app_robust_fetests"),
    (f1[4], "tab:app_flagged"), (f2[4], "tab:app_m2flagged"),
    (f1[5], "tab:app_sensitivity"), (f2[5], "tab:app_loy"),
]
for blk, lab in order:
    assert lab in blk, lab

prose = open(W + "appendix_e_prose.tex").read()
for i, (blk, _) in enumerate(order, 1):
    marker = f"@@T{i:02d}@@"
    assert marker in prose, marker
    prose = prose.replace(marker, blk.rstrip())
assert "@@T" not in prose, "unreplaced marker"

out = str(REPO / "src/thesis/appendices/appendix_e.tex")
open(out, "w").write(prose)
print("wrote", out)
print("tables in file:", prose.count("\\begin{table}"))
print("labels:", re.findall(r"\\label\{(tab:app_[a-z0-9_]+)\}", prose))
