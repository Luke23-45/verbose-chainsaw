# Plan 05 — Empirical review + Table 1 + Research gap (rewrite)

Source: `../detail/09_lit_review_empirical_table1_A.md`, `../detail/11_lit_review_gap_method_start_p6.md` (diagonal-marked Table 1; gap text)
Target: `src/proposal/sections/06_literature_review/06_literature_review.tex` — replace from `\subsection*{Empirical review}` through the end of the gap closing paragraph with the block below. Table stays (professor marked it for rework, not deletion — unlike Table 2 which must become paragraph, plan 08).

## Rules obeyed

- NO variable sub-headings; synthesis in running paragraphs (BVPS/ROA contradictions stated in text, not as headings).
- Every Table 1 row re-verified against `src/proposal/references.bib` (DOIs checked during research) and the reviewed printout. No invented studies. Timalsina 2026 kept as printed (bib notes no DOI — forthcoming in supervisor copy).
- P/E column kept in the table honestly (earlier studies DID use it) while the text keeps the exclusion logic for THIS study (plan 04).

## Paste-ready LaTeX (replaces empirical block through gap)

```latex
\subsection*{Empirical review}

Recent work on Nepalese commercial banks is summarized in Table~\ref{tab:meta}. The evidence is extensive but contested on the two variables this proposal isolates, ROA and BVPS. Internationally, \citet{malhotra2013} link book value, earnings, and the earnings multiple to NSE prices with dividend yield inverse, and \citet{almumani2014} confirms earnings, book value, and the multiple as bank-price correlates in Amman. In Nepal, \citet{bhattarai2014} finds earnings and the multiple positive with yield inverse over 2006--2014, and \citet{pradhan2016} find earnings, return on assets, and size significant with GDP the key macro variable over 2002/03--2013/14.

\citet{bajracharya2019} report earnings, dividends, and the multiple significant with return on assets insignificant and inflation negative over 2006/07--2015/16. \citet{niroula2021} finds earnings and the multiple significantly positive with return on equity and book value negative and insignificant across 18 banks over 2015/16--2019/20. \citet{gyawali2022} finds earnings, dividends, and the multiple significantly positive with return on assets and GDP insignificant over 2017--2021. \citet{joshi2023} find earnings, dividends, the multiple, and book value all positive and significant over 2012/13--2021/22.

Against this run, \citet{chhetri2023} finds the multiple, book value, return on assets, and inflation significantly positive in a 13-bank 2012--2022 panel, whereas \citet{pant2024} find only earnings and the multiple significantly positive with dividends and book value insignificantly negative over 2013/14--2023/24. The most recent bank-year evidence sharpens the contradiction this proposal targets: \citet{chaudhari2025} reports earnings and dividends significantly positive with return on assets significantly negative over 2014/15--2023/24, while governance evidence links capital adequacy and payout to earnings with board independence negative at the 10\% level \citep{dongol2024}.

% Ensure table-only references appear in the bibliography
\nocite{bajracharya2019,timalsina2026}

{\small
\begin{longtable}{>{\raggedright\arraybackslash}p{2.4cm}>{\raggedright\arraybackslash}p{4.3cm}>{\raggedright\arraybackslash}p{6.1cm}}
\caption{Meta table of related studies}
\label{tab:meta}\\
\toprule
Author & Objective & Major finding \\
\midrule
\endfirsthead
\caption*{Table~\ref{tab:meta} (continued)}\\
\toprule
Author & Objective & Major finding \\
\midrule
\endhead
Malhotra \& Tandon (2013) & NSE 100 determinants & BV, EPS, P/E positive. Dividend yield inverse \\
Bhattarai (2014) & NEPSE commercial banks 2006--2014 & EPS, P/E positive. Dividend yield inverse \\
Pradhan \& Dahal (2016) & Nepal banks + macro 2002/03--2013/14 & EPS, ROA, size significant at 1\%. GDP the key macro variable \\
Bajracharya \& Sawagvudcharee (2019) & Internal and external factors, 2006/07--2015/16 & EPS, DPS, P/E significant. ROA insignificant. Inflation negative significant \\
Niroula (2021) & Stock price behavior, 18 banks 2015/16--2019/20 & EPS and P/E significant positive. ROE and BVPS negative insignificant \\
Gyawali (2022) & 10 banks 2017--2021 & EPS, DPS, P/E significant positive. ROA and GDP insignificant \\
Joshi et al. (2023) & 7 banks 2012/13--2021/22 & EPS, DPS, P/E, BVPS all positive significant \\
Chhetri (2023) & 13 banks 2012--2022, panel & P/E, BVPS, ROA, inflation significant positive \\
Pant et al. (2024) & 7 banks 2013/14--2023/24 & EPS and P/E significant positive. DPS and BVPS insignificant negative \\
Dongol \& Shrestha (2024) & Corporate governance and EPS, 4 banks 2013/14--2022/23 & Capital adequacy and dividend payout positive on EPS. Board independence negative (10\% level) \\
Chaudhari (2025) & 10 banks 2014/15--2023/24 & EPS and DPS significant positive. ROA significant negative \\
Timalsina (2026) & 13 banks 2011/12--2023/24 & EPS, DPS, P/E, size, inflation positive. Interest rate negative \\
\bottomrule
\end{longtable}
} % end \small

Two additional dimensions are relevant. Bank regulation and capital structure shape earnings, which in turn influence prices \citep{bhattarai2024,dongol2024}. The merger wave of 2013--2020 and the major 2023 consolidation altered both earnings and price: sector-wide MPS fell by roughly 46\% after the mergers, driven by capital-increment share issues, while EPS and DPS were statistically unchanged \citep{adhikari2023,adhikari2023cbr}.

\subsection*{Research gap}

Three limitations remain. First, most studies end before the major 2023 consolidation, leaving valuation across the restructuring unexamined \citep{adhikari2023,chaudhari2025}. Second, results on ROA and BVPS directly contradict: \citeyearpar{chhetri2023} reports ROA significantly positive, \citeyearpar{chaudhari2025} significantly negative, and \citeyearpar{gyawali2022} positive but insignificant; on BVPS, \citeyearpar{joshi2023} find it significant while \citeyearpar{pant2024} find it negative and insignificant. Third, several specifications include P/E alongside MPS \citep{bhattarai2014,chhetri2023}, which is defined as MPS/EPS. This study excludes P/E to avoid definitional dependence.

This study examines a purposively selected sample across FY 2076/77 to FY 2081/82, spanning before, during, and after the major 2023 consolidation, estimating a unified model of EPS, DPS, BVPS, and ROA against post-disclosure prices while excluding multiples constructed directly from market price.
```

## Verification log (so you never fail on sources)

- Malhotra 2013 / Bhattarai 2014 / Pradhan 2016 / Bajracharya 2019 / Niroula 2021 / Gyawali 2022 / Joshi 2023 / Bhattarai 2024 / Pant 2024 / Dongol 2024 / Adhikari 2023 ×2 — all in `references.bib` with DOI/publisher verified (see bib header comment).
- Chhetri 2023 panel finding (P/E, BVPS, ROA, inflation sig positive; EPS/size/GDP/BMS insig) confirmed against QJMSS publisher PDF (`nepjol.info/.../56298/42368`).
- Pant 2024 finding (EPS + P/E sig positive; DPS + BVPS insig negative; R²≈0.947) confirmed against SISD publisher PDF (`aasmr.org/sisd/Vol.5.No.2.08.pdf`).
- Chaudhari 2025 finding (EPS + DPS sig positive; ROA sig negative; SIZE/IR/GDP insig) confirmed against IJBSD publisher PDF (`musindia.org/.../IJBSD-201-1-...pdf`).
- Merger 46% MPS fall + EPS/DPS unchanged + 239 institutions + 32→20 banks confirmed against Adhikari et al. 2023a/b and NRB merger lists / Republica / Annapurna Express merger-week reports (Jan 2023: Kumari+NCC Jan 1; Global IME+BoK Jan 9; NIMB+Mega Jan 11; Himalayan+Civil Feb).

## Verify after apply

- `pdflatex` Table 1 = 12 rows exactly as above; `\nocite` keeps Bajracharya/Timalsina in References.
- No `\subsubsection` in file. Sub-sections read Theoretical / Empirical / Research gap (starred, out of TOC).
