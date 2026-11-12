import os, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = str(HERE.parents[3])
import csv
rows = list(csv.DictReader(open(os.path.join(REPO, "data_analysis/data_extract/output/audit/source_register.csv"))))
pats = ["financial indicator", "key financial indicator", "financial highlights", "key ratios", "ratio analysis"]
for r in rows:
    p = os.path.join(REPO, r["annual_report_path"])
    try:
        out = subprocess.run(["pdftotext", "-layout", p, "-"], capture_output=True, text=True, timeout=180).stdout
    except Exception:
        print(r["series"], r["fy"], "TEXT-ERR"); continue
    pages = out.split("\x0c")
    hits = []
    for i, pg in enumerate(pages, start=1):
        low = pg.lower()
        for pat in pats:
            if pat in low:
                # snippet: first matching line
                for line in pg.splitlines():
                    if pat in line.lower():
                        hits.append((i, pat, line.strip()[:90])); break
                break
    print(f"{r['series']} {r['fy']}: {hits[:4]}")
