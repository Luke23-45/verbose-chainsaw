"""Extract dividend-proposal candidate snippets from the 30 annual reports.

This is a locator, NOT the DPS extraction itself. It finds pages where
the text mentions dividend together with a proposal/recommendation/
distribution/AGM word, and saves the surrounding lines so a human can
read them closely and decide, per bank-year:
  - cash dividend % proposed FOR THAT FY (not paid in that year for
    the previous FY, and not the previous column of a two-year table)
  - bonus share % (recorded separately, never added to DPS)
  - whether the proposal is a documented nil cash recommendation
    (DPS = 0) or simply not established (DPS stays unavailable)

Legacy-font reports (HBL FY2076-77, NMB FY2079-80 Nepali) have no
usable English text layer and will return few/no candidates here;
those are flagged for visual reading, as with the SOFP work.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # data_analysis/
REPORTS = ROOT.parent / "data" / "reports"
OUT = ROOT / "data_extract" / "output" / "manual_review" / "dps_candidates.json"

SERIES = ["GBIME", "HBL", "KBL", "NIMB", "NMB"]
FYS = ["FY2076-77", "FY2077-78", "FY2078-79", "FY2079-80", "FY2080-81", "FY2081-82"]
KEY = re.compile(r"propos|recommend|distribut|annual general|AGM|bonus", re.I)
DIV = re.compile(r"dividend", re.I)


def find_pdf(series, fy):
    folder = REPORTS / series / fy
    named = folder / f"{series}_{fy}_annual_report.pdf"
    if named.exists() and named.stat().st_size > 10000:
        return named
    cands = sorted(p for p in folder.glob("*.pdf") if p.stat().st_size > 10000)
    if not cands:
        return None
    np_files = [p for p in cands if p.name.endswith("_NP.pdf")]
    return np_files[0] if np_files else cands[0]


def main():
    import pymupdf
    results = {}
    for series in SERIES:
        for fy in FYS:
            pdf = find_pdf(series, fy)
            if pdf is None:
                results[f"{series} {fy}"] = {"error": "no PDF"}
                continue
            doc = pymupdf.open(pdf)
            cands = []
            for i, page in enumerate(doc):
                txt = page.get_text()
                if not DIV.search(txt):
                    continue
                lines = [ln.strip() for ln in txt.splitlines() if ln.strip()]
                for j, ln in enumerate(lines):
                    if DIV.search(ln) and KEY.search(" ".join(lines[max(0, j - 2):j + 3])):
                        snippet = " ".join(lines[max(0, j - 2):j + 3])
                        if len(snippet) > 40:
                            cands.append({"pdf_page": i + 1, "snippet": snippet[:900]})
                        break  # one snippet per page is enough for locating
            results[f"{series} {fy}"] = {
                "source_file": pdf.name,
                "pages": len(doc),
                "candidate_pages": sorted({c["pdf_page"] for c in cands}),
                "candidates": cands,
            }
            print(f"{series} {fy}: {len(cands)} candidate pages")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(results, indent=2, ensure_ascii=False))
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
