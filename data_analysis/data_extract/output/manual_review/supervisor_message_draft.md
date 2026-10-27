# DRAFT — message to supervisor — DO NOT SEND until Krishna approves the wording

Subject: Request to change the MPS_post price date rule

Dear Sir,

I am writing to request approval for a change to the price date rule in my proposal before I run the regression.

My proposal defines MPS_post as the closing price on the first NEPSE trading day strictly after the NEPSE disclosure date for the audited annual financial statements. I have collected EPS, DPS, BVPS, and ROA for all 30 bank years. For MPS_post under the proposal rule, I have verified only two bank years from the NEPSE documents themselves. Those are Global IME Bank FY2081/82 and Nepal Investment Mega Bank FY2081/82. Three further FY2081/82 rows are held because their NEPSE attachments are AGM notices only, with no statement tables inside, and a separate statement disclosure was not found for them in the sources I checked. For the older years, I found no systematic source for disclosure dates in this pass.

I therefore propose the following change, to be fixed before any regression.

Primary rule: use the last close on or before the last day of Ashadh for each fiscal year, taken from a public historical price dataset that I have verified against your banks. I checked the dataset myself. It covers all five banks, it is raw and not bonus adjusted, and I verified one spot check exactly. I also found gaps that I have flagged, including a merger suspension for Global IME Bank from June to December 2022 and a gap for Himalayan Bank from May 2021 to June 2022 that Merolagani confirms on the same dates, so it is not a dataset only error. The reason for that year long halt is still unresolved. Two checks are still open, a ShareSansar price history check for Himalayan Bank and Nepal Investment Bank, and whether the NEPSE daily report for 16 November 2022 lists a Global IME Bank close.

Robustness checks: I will also report a Poush end price and the disclosure date subsample of two verified rows. I will report all three versions and I will not choose the primary rule after seeing the results.

One model point from exploratory work on the candidate Ashadh end prices, using only the 26 rows whose price date is within five days of the Ashadh end target. EPS and ROA correlate at 0.974 in that sample, with variance inflation factors of 30.87 for EPS and 27.52 for ROA when all four variables are used together, so the four variable model is not credible on this sample. If you approve the Ashadh end rule, I propose the primary model as price on EPS and BVPS only, with ROA reported separately, not in the same regression as EPS.

I understand this changes the meaning of the dependent variable. The Ashadh end price comes before the figures were public, so it tests association, not market reaction to disclosure. I will state that limit in the write up.

Please let me know if you approve this change, or if you would prefer that I continue with the disclosure date rule only.

Thank you for your guidance.

Krishna Subedi
