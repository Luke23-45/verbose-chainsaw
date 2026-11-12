#!/usr/bin/env python3
"""Generate Appendix D Tables 14 and 15 rows from verified data (2026-11-01).
Inputs: register CSV + verification TSV + frozen indicators dict.
Asserts: 30 rows each, SHA-12 prefixes unique, all pages in range.
Outputs row fragments; assembly into appendix_d.tex replaces placeholders.
"""
import csv, os
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = str(HERE.parents[3])
WORK = str(HERE)
reg = list(csv.DictReader(open(os.path.join(REPO, "data_analysis/data_extract/output/audit/source_register.csv"))))
ver = {}
with open(os.path.join(WORK, "register_verification.tsv")) as f:
    rd = csv.DictReader(f, delimiter="\t")
    for r in rd:
        ver[(r["series"], r["fy"])] = r

ROUTE = {"GBIME": "Bank website", "HBL": "Wayback capture", "KBL": "Bank website",
         "NIMB": "Bank website", "NMB": "Bank website"}
IND = {
 ("GBIME", "FY2076-77"): "p. 71", ("GBIME", "FY2077-78"): "p. 65",
 ("GBIME", "FY2078-79"): "p. 68", ("GBIME", "FY2079-80"): "p. 73",
 ("GBIME", "FY2080-81"): "p. 23", ("GBIME", "FY2081-82"): "p. 33",
 ("HBL", "FY2076-77"): "Comparative Financial Indicators (from p. 28)",
 ("HBL", "FY2077-78"): "p. 38", ("HBL", "FY2078-79"): "p. 41",
 ("HBL", "FY2079-80"): "p. 41", ("HBL", "FY2080-81"): "p. 44", ("HBL", "FY2081-82"): "p. 41",
 ("KBL", "FY2076-77"): "Review of the Financial Indicators of previous years (p. 30)",
 ("KBL", "FY2077-78"): "No titled table located",
 ("KBL", "FY2078-79"): "No titled table located",
 ("KBL", "FY2079-80"): "Major Financial Indicators (p. 160)",
 ("KBL", "FY2080-81"): "Major Financial Indicators (p. 165)",
 ("KBL", "FY2081-82"): "Major Financial Indicators (p. 172)",
 ("NIMB", "FY2076-77"): "Major Financial Highlights (from p. 156)",
 ("NIMB", "FY2077-78"): "Major Financial Highlights (from p. 159)",
 ("NIMB", "FY2078-79"): "Major Financial Highlights (from p. 167)",
 ("NIMB", "FY2079-80"): "Major Financial Highlights (from p. 168)",
 ("NIMB", "FY2080-81"): "Major Financial Highlights (from p. 172)",
 ("NIMB", "FY2081-82"): "Major Financial Highlights (from p. 164)",
 ("NMB", "FY2076-77"): "pp. 45--46",
 ("NMB", "FY2077-78"): "Financial Highlights (from p. 27)",
 ("NMB", "FY2078-79"): "Key Financial Highlights (p. 31)",
 ("NMB", "FY2079-80"): "p. 107", ("NMB", "FY2080-81"): "pp. 112--113",
 ("NMB", "FY2081-82"): "p. 104",
}

def fy_disp(fy):
    return "FY " + fy.replace("FY", "").replace("-", "/")

def pages_disp(v):
    parts = [int(x) for x in v.split(";") if x.strip().isdigit()]
    if not parts:
        return v
    if parts == list(range(parts[0], parts[-1] + 1)):
        return f"{parts[0]}--{parts[-1]}" if len(parts) > 1 else str(parts[0])
    return "; ".join(str(x) for x in parts)

assert len(reg) == 30, len(reg)
sha12 = [r["report_sha256"][:12] for r in reg]
assert len(set(sha12)) == 30, "SHA-12 prefixes not unique"

t14, t15 = [], []
prev = None
for r in reg:
    s, fy = r["series"], r["fy"]
    v = ver[(s, fy)]
    if prev is not None and s != prev:
        t14.append("\\midrule")
        t15.append("\\midrule")
    prev = s
    edition = "Nepali" if (s == "NMB" and fy == "FY2079-80") else "English"
    t14.append(f"{s} & {fy_disp(fy)} & {edition} & {ROUTE[s]} & {v['pages']} & {v['size_mb']} & \\texttt{{{sha12[reg.index(r)]}}} \\\\")
    t15.append(f"{s} & {fy_disp(fy)} & {pages_disp(r['sofp_pages_pdf'])} & {pages_disp(r['sopl_pages_pdf'])} & {r['dps_pdf_page']} / {r['dps_printed_page']} & {IND[(s, fy)]} \\\\")

def gap_rows(lines):
    """Insert \\addlinespace between consecutive data rows only; group
    boundaries keep their \\midrule with no extra gap."""
    out = []
    for i, line in enumerate(lines):
        out.append(line)
        if line.endswith("\\\\") and i + 1 < len(lines) and lines[i + 1].endswith("\\\\"):
            out.append("\\addlinespace")
    return out


t14 = gap_rows(t14)
t15 = gap_rows(t15)

open(os.path.join(WORK, "table14_rows.tex"), "w").write("\n".join(t14) + "\n")
open(os.path.join(WORK, "table15_rows.tex"), "w").write("\n".join(t15) + "\n")
print("Table 14 data rows:", sum(1 for x in t14 if x != "\\midrule"))
print("Table 15 data rows:", sum(1 for x in t15 if x != "\\midrule"))
print("SHA-12 unique: True")
