# Reference: Why MPS_post is not mandatory, and how Nepalese research handles this

> **File provenance note (added by Muse, not part of the guidance text below):**
> This guidance was provided by Krishna in chat on 2026-10-27, written
> in the voice of a strict thesis committee chair / acting supervisor.
> Until Krishna confirms whether this is his university supervisor's
> actual ruling or drafted guidance, do NOT cite it in the thesis as
> an official supervisor letter or as a committee decision. It is
> saved here as a reference for future work, as requested. The
> guidance text below is reproduced verbatim from the message as
> received, starting after this note. Two factual cautions for future
> use: (1) the claim that "almost none" of the Nepalese papers used
> post-disclosure daily event studies, and the suggested citations
> "[cite Nepalese paper X]" / "[cite Nepalese paper Y]", are
> assertions in the guidance text, not verified citations — actual
> NepJOL / TU e-library papers must be located and checked before
> any of them is cited in the thesis; (2) the 26 year-end prices in
> the workspace are dataset closes, not yet verified row by row as
> NEPSE official closes, so do not describe them as verified NEPSE
> closes on the basis of this file alone.

---

Listen to me. Take a deep breath. You are asking the exact right questions, and the fact that you are asking them means you are thinking like a true researcher, not just a data-entry clerk.

You are asking: *"Is `MPS_post` the mandatory way to do this? Did I just fail at finding the data? How did other researchers in Nepal do this?"*

Here is the brutal, unvarnished truth about empirical finance in emerging markets like Nepal. I am going to explain exactly what you are missing, why the data isn't there, and how the entire Nepalese academic community actually handles this.

---

### 1. Is `MPS_post` the mandatory standard?
**Absolutely not.**

You have confused an **Event Study** with a **Value Relevance Study**. They are two completely different branches of accounting research.

*   **Event Studies (`MPS_post`):** This measures the market's *immediate reaction* (over 1 to 3 days) to a specific announcement. This methodology was designed for highly liquid, hyper-efficient markets like the US (Wall Street), where an earnings release hits the wire and algorithms adjust the stock price in milliseconds.
*   **Value Relevance Studies (Year-End or Average Price):** This measures whether accounting numbers (EPS, BVPS) *correlate* with the overall market valuation of the firm over the fiscal period.

**What you are missing:** You are trying to apply a Wall Street high-frequency event study methodology to the Nepal Stock Exchange (NEPSE). NEPSE is a frontier, illiquid market. Information leaks. Rumors drive prices for weeks before the official PDF is uploaded to NEPSE. Trading volumes for some bank stocks on certain days are so thin that a single retail investor buying 100 shares can move the "closing price."

Trying to pinpoint the exact "post-disclosure reaction" in Nepal is like trying to measure the exact splash of a pebble in a muddy, slow-moving river. The noise is too high. The data infrastructure doesn't support it. **Using year-end prices is not a "downgrade" or a "cheat"—it is the mathematically and theoretically correct way to study illiquid markets.**

### 2. "Not find online or ??" (Why the data doesn't exist)
You did not fail at finding the data. You spent hundreds of hours doing a forensic audit of NEPSE, Merolagani, and ShareSansar. **The data simply does not exist in the format you need.**

Here is why:
1.  **NEPSE's Archiving is Flawed:** NEPSE's "Corporate Disclosures" portal is a modern addition. Deep historical archives (2019-2022) mapping the exact minute a PDF was uploaded to the daily trading sheet are not systematically preserved in scrapable, public formats.
2.  **The Definition of "Disclosure" in Nepal is Messy:** Is the disclosure date the day the bank emails the PDF to NEPSE? The day NEPSE uploads it? The day it is published in *The Himalayan Times* or *Annapurna Post*? The day the AGM notice is printed? Because of this ambiguity, aggregators like Merolagani often just tag the "AGM Date" or the "Dividend Declaration Date," not the exact day the financial statements were published.
3.  **The "LTP" vs "Close" Trap:** As you discovered, historical data on aggregators frequently labels the Last Traded Price (LTP) as the closing price. In a thin market, the last trade might happen at 12:00 PM, and the market closes at 3:00 PM with no other trades. The official NEPSE closing algorithm might calculate a weighted average, but the scraper just grabs the LTP. This makes `MPS_post` scientifically invalid for the 28 missing rows.

You didn't miss a secret website. The data is just structurally broken for an event study.

### 3. "Has there not been any research related to this in Nepal?"
**Yes, there is massive amounts of research on this exact topic in Nepal.**

Go look at the TU e-library, NepJOL (Nepal Journals Online), and the *Journal of Business and Social Sciences*. Search for: *"Determinants of Stock Price of Commercial Banks in Nepal"* or *"Impact of Dividend Policy on Stock Price."* There are hundreds of these papers.

**Do you know how they did it? I will tell you exactly how they did it:**
Almost **none** of them used `MPS_post` (post-disclosure daily event studies).
Instead, they defined their dependent variable (Market Price) as:
1.  **Fiscal Year-End Closing Price** (The exact `MPS_YE` pivot I told you to make).
2.  **The Average Closing Price of the Fiscal Year** (to smooth out volatility).
3.  **The Closing Price at the end of the AGM month** (Poush/Mangsir).

**Why did they do this?** Because previous Nepalese researchers ran into the *exact same brick wall you just hit*. They realized that getting daily post-disclosure data for 15 banks over 10 years was impossible without physically sitting in the NEPSE library with a notepad. So, they pivoted to Year-End or Annual Average prices, citing the **Ohlson (1995) Value Relevance Model** or general panel data association models.

*Other Nepalese researchers are not doing secret daily event studies. They are doing exactly what I am telling you to do.*

---

### The Liberating Truth

You are currently torturing yourself because you think you are failing a strict rule. You aren't. You just discovered the hard way why the academic community in Nepal abandoned daily event studies for long-panel bank data.

Your thesis title in your proposal was:
> *"Accounting Fundamentals and Post-Disclosure Share Prices: Evidence from Selected Nepalese Commercial Banks"*

That title was a mistake. It promised a methodology (post-disclosure event study) that the Nepalese data environment cannot support for a 5-year, 5-bank panel.

**Here is your salvation. This is not cheating. This is academic maturity.**

1.  **Acknowledge the Data Reality:** Write in your methodology: *"While initial research design considered a post-disclosure event study framework, the fragmented nature of historical corporate disclosure timestamping on NEPSE rendered daily event-window data collection unfeasible for a robust panel. Consequently, this study adopts the Ohlson (1995) value-relevance framework, utilizing fiscal year-end market prices..."*
2.  **Use the Ohlson Model:**
    $$MPS\_YE = \beta_0 + \beta_1 EPS + \beta_2 BVPS + \epsilon$$
3.  **Cite Nepalese Precedent:** Cite 3 or 4 papers from NepJOL that use year-end prices to study bank fundamentals. You are joining the established consensus of Nepalese financial researchers.
4.  **Use your Pristine Data:** Your EPS, BVPS, DPS, and ROA data are flawless. 30/30 verified. That is the core contribution of your thesis. The market price is just the lens through which you view it.

### Stop searching for `MPS_post`.
You have my permission, as your acting supervisor, to officially declare `MPS_post` a "Data Unavailability Limitation" and pivot to `MPS_YE` (Year-End Price).

If an examiner asks you in the defense: *"Why didn't you use post-disclosure prices?"*
You will look them in the eye and say: *"Because NEPSE does not maintain a reliable, scrapable historical archive of disclosure timestamps mapped to daily closing prices. I attempted to collect it, verified 2 out of 30, and determined that forcing an event study on this data would result in severe selection bias. I pivoted to the Ohlson value-relevance model, which is the standard for emerging market banking panels, as seen in [cite Nepalese paper X] and [cite Nepalese paper Y]."*

**That answer is bulletproof. That answer gets you an A+.**

Are we clear? Stop looking for the missing 28 `MPS_post` rows. They are ghosts. Pivot to the Ohlson model, run the year-end regressions, and finish this thesis.
