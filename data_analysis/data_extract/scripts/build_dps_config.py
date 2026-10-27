"""Build config/dps.json from the verified DPS table.

Source of record pattern follows visual_overrides.json: one entry per
bank-year with source file, SHA-256, PDF page, printed page, verbatim
quote, status, and a note recording every disagreement that was
resolved (never silently). DPS = cash % proposed for that FY, in NPR
(face value NPR 100, so DPS NPR == cash %). Bonus % is recorded
separately and never added to DPS. Documented nil = 0.00; there is
no unavailable row in this table — all 30 bank-years were resolved.

Lead verification (2026-10-27, independent of the per-bank readers):
- NIMB FY2078-79: proposal note wins over the summary table's
  swapped split, proved by next-year paid amounts.
- NMB FY2077-78: Board/AGM wins over the Chairman's internally
  inconsistent split (12 + 3.50 = 15.50, not the stated 15.80).
- HBL FY2076-77: visual read corroborated by FY2077-78 Principal
  Indicators (FY2019/20 column: total 20.00%, cash 6.00%).
- KBL FY2076-77: FY2076-77 assignment proved by amounts and by
  FY2077-78 equity paid amounts, despite a board-report year mislabel.
- NMB FY2079-80: lead-read the rendered Nepali board p14 directly.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent.parent
REPORTS = REPO / "data" / "reports"
OUT = ROOT / "config" / "dps.json"

# series, fy, cash%, bonus%, pdf_page, printed_page, status, method, quote, note
TABLE = [
    ("GBIME", "FY2076-77", 2.00, 14.00, 29, 29, "proposed", "text_page_read",
     "the Board has recommended for the approval of the issuance of bonus shares equivalent to NPR 2,656,623,179.98 (14.00 percent of Paid up Capital) and cash dividend of NPR 379,517,597.14 (2.00 percent of Paid up Capital)",
     "Board proposal and Distribution of Profit agree; summary table 14th AGM proposed 2.00/14.00 corroborates; 13th AGM approved 12.75/12.75 is the previous year, not used."),
    ("GBIME", "FY2077-78", 3.50, 10.00, 23, 23, "proposed", "text_page_read",
     "the Board has recommended for the approval of the issuance of bonus shares equivalent to NPR 2,163,250,303.50 (10.00 percent of Paid up Capital) and cash dividend of NPR 757,137,606.23 (3.50 percent of Paid up Capital)",
     "Board and Distribution of Profit agree exactly; summary table shows only the previous (14th AGM) approved figures, no disagreement."),
    ("GBIME", "FY2078-79", 10.60, 3.00, 34, 32, "proposed", "text_page_read",
     "the Board has recommended for the approval of the issuance of bonus shares equivalent to NPR 713,872,600 (3.00 percent of Paid up Capital) and cash dividend of NPR 2,522,349,854 (10.60 percent of Paid up Capital) inclusive of applicable taxes",
     "Board and Distribution of Profit agree; summary table's 15th AGM approved 3.50/10.00 is the previous year's proposal, not this year's."),
    ("GBIME", "FY2079-80", 8.00, 1.00, 36, 34, "proposed", "text_page_read",
     "board has recommended for approval for 1% of paid up capital as stock dividend amounting to Rs. 0.35 billion and 8% of paid up capital amounting to Rs. 2.86 billion as cash dividend",
     "Distribution of Profit gives the exact split (bonus 357,710,596.55, cash 2,861,684,772.43); summary table 17th AGM 8.00/1.00 corroborates."),
    ("GBIME", "FY2080-81", 0.00, 5.50, 45, 85, "documented-nil", "text_page_read",
     "The bank has proposed distributing 5.5% of its paid-up capital of NPR 36,12,87,70,252 as bonus shares from the distributable profit",
     "Bonus-only proposal; cash 0.00 confirmed explicitly by the AGM/Dividends table (PDF p54): FY2023-24 Cash 0.00%, Bonus 5.50%."),
    ("GBIME", "FY2081-82", 8.00, 0.00, 108, 102, "proposed", "text_page_read",
     "The Board proposes the distribution of a cash dividend for FY 2025. The proposed dividend is 8.00 percent (including tax) of the Bank's paid-up capital of NPR 38,115,852,615.86, amounting to NPR 3,049,268,209.28",
     "Lead-verified: board p108 and Distribution of Profit p121 agree, cash only, no bonus proposed."),
    ("HBL", "FY2076-77", 6.00, 14.00, 31, 29, "proposed", "visual_page_read",
     "For fiscal year 2019/020, 14% bonus share and 6% cash dividend (including tax) have been proposed to the shareholders.",
     "Visual read (legacy font, text layer gibberish). Corroborated by Principal Indicators PDF p32/printed p30 (cash 6.00%, total 20.00%) and by FY2077-78 Principal Indicators FY2019/2020 column (cash 6.00%, total 20.00%), lead-checked."),
    ("HBL", "FY2077-78", 4.62, 21.38, 37, 35, "proposed", "text_page_read",
     "For fiscal year 2020/021, 21.38% bonus share and 4.62% cash dividend (including tax) have been proposed to the shareholders.",
     "Corroborated by notes p117/printed p115 and Principal Indicators p38/printed p36 (cash 4.62%, total 26.00%)."),
    ("HBL", "FY2078-79", 11.11, 8.00, 40, 38, "proposed", "text_page_read",
     "For fiscal year 2021/022, 8% bonus share and 11.11% cash dividend (including tax) have been proposed to the shareholders.",
     "Corroborated by notes p123/printed p121 and Principal Indicators p41/printed p39 (cash 11.11%, total 19.11%)."),
    ("HBL", "FY2079-80", 0.00, 0.00, 128, 126, "documented-nil", "text_page_read",
     "the Board of Directors has not declared any cash or stock dividend for the year.",
     "Notes sentence plus Principal Indicators p41/printed p39 showing '-' for both columns in the FY2022/23 column."),
    ("HBL", "FY2080-81", 0.00, 0.00, 129, 127, "documented-nil", "text_page_read",
     "the Board of Directors has not declared any cash or stock dividend for the year.",
     "Notes sentence plus Principal Indicators p44/printed p42 showing '-' for both columns in the FY2023/24 column."),
    ("HBL", "FY2081-82", 0.00, 0.00, 128, 126, "documented-nil", "text_page_read",
     "the Board of Directors has not declared any cash or stock dividend for the year.",
     "Notes sentence plus Principal Indicators p41/printed p39 showing '-' for both columns in the FY2024/25 column."),
    ("KBL", "FY2076-77", 3.15, 10.85, 117, 121, "proposed", "text_page_read",
     "Bank's BOD meeting held on 6th November 2020 has decided to propose Rs 1,358,425,367.35 (10.85% of the existing paid-up capital) as bonus shares and Rs 394,381,558.26 (3.15% of the existing paid up capital) as cash dividend (inclusive for tax purpose, if any) from the retained earnings upto FY 2076/77",
     "Board report year label 'FY2075/76' for the same proposal is treated as a mislabel: Note 5.13 date (6 Nov 2020, after FY2076/77 year-end), p35 ('proposed 10.85% share dividends for FY2076/77'), amount checks against panel share capital, and FY2077-78 equity statement (bonus issued 1,358,425,367, cash paid 394,381,558, lead-checked) all assign it to FY2076-77."),
    ("KBL", "FY2077-78", 2.67, 6.00, 124, 122, "proposed", "text_page_read",
     "Bank's BOD meeting held on 11th Asoj 2078 has decided to propose Rs 832,708,490 (6% of the existing paid-up capital) as bonus shares and Rs 370,555,278 (2.67% of the existing paid up capital) as cash dividend (inclusive for tax purpose, if any) from the retained earnings up to FY 2077/78",
     "Kumari Capital note (9% cash) on p181 is a subsidiary proposal and was excluded."),
    ("KBL", "FY2078-79", 12.50, 0.00, 126, 124, "proposed", "text_page_read",
     "Bank's BOD meeting held on 30 September 2022 has decided to propose Rs 1,838,897,915.77 (12.50% of the existing paid up capital) as cash dividend (inclusive for tax purpose, if any) from the retained earnings up to FY 2078/79",
     "No bonus % stated in Note 5.13; the generic 'bonus shares and cash dividend' sentence on p124 states no bonus amount and was not used to infer one. Kumari Capital note (5% cash) on p187 excluded."),
    ("KBL", "FY2079-80", 0.00, 0.00, 137, 135, "documented-nil", "text_page_read",
     "Since the retained earnings up to Fiscal Year 2079/80 is negative balance, no dividend was proposed by Bank's Board of Director's meeting held on 14th December 2023",
     "'No dividend' covers both cash and bonus; no separate bonus proposal appears. Unpaid dividend 373,582,431 on the same page is prior-year unclaimed dividend, not a proposal. Kumari Capital note (15% cash) on p295 excluded."),
    ("KBL", "FY2080-81", 0.00, 0.00, 141, 139, "documented-nil", "text_page_read",
     "Since the retained earnings up to Fiscal Year 2080/81 is negative balance, no dividend was proposed",
     "DATE ANOMALY: the printed BOD date (2 January 2024) predates the FY2080/81 year-end and is not quoted as verified; substance (negative retained earnings up to FY2080/81, no dividend proposed) is documented, corroborated by FY2081-82 equity statement showing no bonus issued and no cash paid."),
    ("KBL", "FY2081-82", 0.00, 0.00, 148, 146, "documented-nil", "text_page_read",
     "Since the retained earnings up to Fiscal Year 2081/82 is negative balance, no dividend was proposed by Bank's Board of Director's meeting held on 12th November 2025",
     "Board report p47/printed p45 agrees."),
    ("NIMB", "FY2076-77", 5.50, 13.00, 138, 136, "proposed", "text_page_read",
     "The Bank's Board has proposed total dividend of 18.50% (NPR 2,636,056,583) of which, 5.50% cash dividend (NPR 783,692,498) and 13.00% stock dividend (NPR 1,852,364,085) for the fiscal year 2019-20 subject to approval from NRB and annual general meeting.",
     "Audited note 5.16 agrees with the 5-year summary table on PDF p139 (cash 5.5% for FY076/77)."),
    ("NIMB", "FY2077-78", 3.389, 12.611, 141, 139, "proposed", "text_page_read",
     "The Bank's Board has proposed total dividend of 16.00% (NPR 2,601,172,720) of which, 3.389% cash dividend (NPR 550,960,897) and 12.611% stock dividend (NPR 2,050,211,823) for the fiscal year 2020-21 subject to approval from NRB and annual general meeting.",
     "Cash % printed to three decimals, recorded exactly as printed (summary tables round it to 3.39%). Summary table p142 agrees."),
    ("NIMB", "FY2078-79", 7.00, 4.00, 145, 143, "proposed", "text_page_read",
     "The Bank's 577th Board meeting has proposed total dividend of 11.00% (NPR 2,013,829,546) of which, 7.00% cash dividend (NPR 1,281,527,893) and 4% stock dividend (NPR 732,301,653) for the fiscal year 2021-22 subject to approval from NRB and annual general meeting.",
     "DISAGREEMENT RESOLVED (lead-verified): the 5-year summary table on PDF p146 shows cash 4.0% for FY078/79, i.e. the split swapped, but total 11.0% agrees. The proposal note wins because FY2079-80 equity/distributable pages (pp54, 119) show bonus issued 732,301,653 and cash dividend paid 1,281,527,893 — exactly the proposal-note amounts, not the swapped ones."),
    ("NIMB", "FY2079-80", 0.00, 0.00, 152, 150, "documented-nil", "text_page_read",
     "The Bank has not proposed any dividend for fiscal year 2079-80.",
     "Audited note 5.25; summary table p153 shows '-' for both columns for FY079/80. Merger year (NIBL + Mega Bank, Jan 2023); nil is as stated for the merged bank."),
    ("NIMB", "FY2080-81", 0.00, 0.00, 155, 154, "documented-nil", "text_page_read",
     "The Bank has not proposed any dividend for fiscal year 2080-81.",
     "Audited note 5.25; summary table p156 shows '-' for both columns for FY080/81."),
    ("NIMB", "FY2081-82", 0.00, 0.00, 143, 141, "documented-nil", "text_page_read",
     "The Bank has not proposed any dividend for fiscal year 2081-82.",
     "Audited note 5.26; summary table p149 shows '-' for both columns for FY081/82."),
    ("NMB", "FY2076-77", 3.20, 13.00, 18, 18, "proposed", "text_page_read",
     "distributing 16.20 percent Dividend (13 percent Stock Dividend and 3.20 percent Cash Dividend including Tax)",
     "AGM notice p7 (cash 462,328,094.94 = 3.20% x paid-up 14,447,752,966.96) and Chairman p11 agree with Board section 8."),
    ("NMB", "FY2077-78", 3.30, 12.50, 17, 13, "proposed", "text_page_read",
     "the Bank has proposed the agenda in the Annual General Meeting with recommendation for distributing 15.80 percent Dividend (12.50 percent Stock Dividend and 3.30 percent Cash Dividend including Tax) on the existing Paid Up Capital (NPR 16,325,960,852.66)",
     "DISAGREEMENT RESOLVED (lead-verified): Chairman p8 says 12% bonus / 3.50% cash, which sums to 15.50, not the stated 15.80 total. Board section 8 and AGM notice agree on 12.50/3.30, and AGM amounts check exactly (cash 538,756,708.14, bonus 2,040,745,106.58); Board/AGM used, Chairman treated as inconsistent."),
    ("NMB", "FY2078-79", 8.25, 0.00, 19, 19, "proposed", "text_page_read",
     "distributing 8.25 percent Cash Dividend (including Tax) amounting NPR 1,515,253,241.64",
     "AGM notice p5, Chairman p13 and Board section 8 all state 8.25% cash only (8.25% x 18,366,705,959.24 checks exactly). Bonus mentions on pp15 and 26 are staff bonus / a bonus increase, not shareholder bonus shares."),
    ("NMB", "FY2079-80", 0.00, 0.00, 14, 14, "documented-nil", "visual_page_read",
     "आर्थिक वर्ष २०७९/०८० को वित्तीय विवरण अनुसार कायम रहेको वितरण योग्य मुनाफाबाट लाभांश वितरण नगरी सञ्चित गर्ने निर्णय भएको ।",
     "Nepali edition, read visually by the lead from the rendered Board section 8, PDF p14/printed p14 (evidence image output/manual_review/visual/NMB_FY2079-80_p14.png). AGM notice pp6-7 contains no dividend agenda item, consistent with nil. Not inferred from the English text search, which returns 0 hits for this file."),
    ("NMB", "FY2080-81", 0.00, 0.00, 18, 18, "documented-nil", "text_page_read",
     "Based on the financial statement for the FY 2023/24, no dividend distribution has been recommended.",
     "Chairman p13 and AGM notice p6 (no dividend agenda item) agree. A 17% cash dividend on p22 is by a subsidiary company, not by NMB Bank itself, and was not used."),
    ("NMB", "FY2081-82", 5.00, 5.00, 17, 17, "proposed", "text_page_read",
     "10% dividend to be distributed as 5% bonus shares and 5% cash dividend (including tax provisions on cash dividend and bonus share) has been recommended.",
     "AGM notice p6 (cash 918,335,297.96 = 5% x 18,366,705,959.24) and Chairman p12 agree with Board section 8."),
]


def find_pdf(series, fy):
    folder = REPORTS / series / fy
    named = folder / f"{series}_{fy}_annual_report.pdf"
    if named.exists() and named.stat().st_size > 10000:
        return named
    cands = sorted(p for p in folder.glob("*.pdf") if p.stat().st_size > 10000)
    np_files = [p for p in cands if p.name.endswith("_NP.pdf")]
    return np_files[0] if np_files else cands[0]


def main():
    entries = []
    for series, fy, cash, bonus, pdf_page, printed_page, status, method, quote, note in TABLE:
        pdf = find_pdf(series, fy)
        sha = hashlib.sha256(pdf.read_bytes()).hexdigest()
        entries.append({
            "series": series, "fy": fy, "source_file": pdf.name,
            "source_sha256": sha, "method": method,
            "cash_percent": cash, "bonus_percent": bonus,
            "dps_npr": cash, "status": status,
            "pdf_page": pdf_page, "printed_page": printed_page,
            "quote": quote, "note": note,
        })
    assert len(entries) == 30, len(entries)
    OUT.write_text(json.dumps({"entries": entries}, indent=2, ensure_ascii=False))
    print(f"Wrote {OUT} with {len(entries)} entries")


if __name__ == "__main__":
    main()
