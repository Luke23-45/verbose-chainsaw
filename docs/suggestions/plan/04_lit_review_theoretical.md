# Plan 04 — Theoretical review (rewrite, NO variable sub-headings)

Source: `../detail/07_lit_review_conceptual_A.md` (rewrite lit review; both theoretical & empirical; NO headings)
Target: `src/proposal/sections/06_literature_review/06_literature_review.tex` — replace everything from `\subsection*{Conceptual review}` through the DPS paragraph with the block below. Rename the opening sub-section to Theoretical review.

## Rules obeyed

- NO `\subsubsection` variable headings (EPS/DPS/BVPS/ROA headings deleted per order).
- Theory first, in running paragraphs: valuation baseline → information asymmetry/signaling → clean-surplus anchor → what ROA adds → why P/E is excluded.
- Every claim cited. New theory citations are all real, classic, verifiable works (add the 4 bib entries in the box at the bottom).

## Paste-ready LaTeX (replaces conceptual block)

```latex
\subsection*{Theoretical review}

Equity valuation starts from the present value of expected dividends \citep{miller1961}. Under full information and fixed investment policy, the split between dividends and retention does not itself create value, which gives the proposal its neutral benchmark: any association between accounting numbers and price must come from what those numbers reveal about future cash generation, not from the payout mechanics alone.

Nepalese banking is a setting with pronounced information asymmetry between insiders and outside investors, so the signaling channel is central. When managers hold private information, costly observable choices convey it credibly \citep{ross1977}: dividends signal anticipated performance because a weak firm cannot mimic a sustained payout without cost \citep{bhattacharya1979}. Steady earnings and dividends therefore reduce asymmetry and move prices even before the cash itself matters, which is why earnings power and payout behavior belong in the same specification as information proxies rather than as cash-flow arithmetic.

The accounting anchor is the clean-surplus relation formalized by \citet{ohlson1995}: market value equals book value plus the present value of expected abnormal earnings, so earnings and book value enter valuation jointly and dividends displace price dollar-for-dollar while leaving the abnormal-earnings sequence unchanged. In banking terms, earnings per share carries the flow signal on current profitability, book value per share carries the stock signal on net-asset backing and downside protection, and dividend per share carries the costly signal on solvency and cash generation. Return on assets adds the efficiency margin --- net income per unit of assets --- through which regulation, capital structure, and asset use shape the earnings that later capitalize into price \citep{bhattarai2024}.

Earlier specifications often added the price-earnings ratio alongside market price, but $\text{P/E} = \text{MPS} / \text{EPS}$ embeds the dependent variable in the regressor and creates direct definitional dependence. This proposal therefore restricts regressors to accounting measures that exist independently of secondary-market price, and tests their associations with post-disclosure price without a mechanically constructed multiple on both sides of the equation.
```

## Bib additions required (all real — verified via publisher records during research)

```bibtex
@article{ross1977,
  author  = {Ross, Stephen A.},
  title   = {The determination of financial structure: the incentive-signalling approach},
  journal = {The Bell Journal of Economics},
  volume  = {8},
  number  = {1},
  pages   = {23--40},
  year    = {1977}
}
@article{bhattacharya1979,
  author  = {Bhattacharya, Sudipto},
  title   = {Imperfect information, dividend policy, and the `bird in the hand' fallacy},
  journal = {The Bell Journal of Economics},
  volume  = {10},
  number  = {1},
  pages   = {259--270},
  year    = {1979}
}
@article{miller1961,
  author  = {Miller, Merton H. and Modigliani, Franco},
  title   = {Dividend policy, growth, and the valuation of shares},
  journal = {The Journal of Business},
  volume  = {34},
  number  = {4},
  pages   = {411--433},
  year    = {1961}
}
@article{ohlson1995,
  author  = {Ohlson, James A.},
  title   = {Earnings, book values, and dividends in equity valuation},
  journal = {Contemporary Accounting Research},
  volume  = {11},
  number  = {2},
  pages   = {661--687},
  year    = {1995}
}
```

## Verify after apply

- No `\subsubsection` remains in the file. Opening sub-section reads "Theoretical review".
- Citations resolve: ross1977, bhattacharya1979, miller1961, ohlson1995 + existing bhattarai2024 (all other keys in this block are from the 4 new bib entries).
- P/E exclusion sentence kept verbatim in logic (definitional dependence).
