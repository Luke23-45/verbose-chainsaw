"""A4: MPS_RD price verification — dataset close vs Merolagani LTP for every
bank-year, joined by (bank, price_date) with the pre-merger NIB symbol mapped
to NIMB.  Documents the independent cross-check behind the price column.
"""
from __future__ import annotations

from analysis.dataset import AnalysisDataset
from analysis.render.tables import Table, save_table

SYMBOL_ALIASES = {"NIB": "NIMB"}


def generate(dataset: AnalysisDataset) -> list:
    status = dataset.price_status.rename(columns={"series": "bank"})
    merolagani = dataset.merolagani.copy()
    merolagani["bank"] = merolagani["symbol"].replace(SYMBOL_ALIASES)
    merged = status.merge(
        merolagani[["bank", "price_date", "merolagani_ltp", "outcome"]],
        on=["bank", "price_date"],
        how="left",
        validate="1:1",
    )
    unresolved = merged["merolagani_ltp"].isna()
    if unresolved.any():
        row = merged.loc[unresolved].iloc[0]
        raise ValueError(
            f"A4: no Merolagani row for {row['bank']} on {row['price_date']}; "
            "the price-verification join must cover every bank-year"
        )
    rows = []
    for row in merged.itertuples():
        rows.append((
            row.bank,
            row.fy,
            str(row.price_date),
            f"{row.close_dataset:,.2f}",
            f"{row.merolagani_ltp:,.2f}",
            str(row.outcome),
        ))
    n_match = sum(1 for r in rows if r[5] == "match")
    table = Table(
        id="A4_price_verification",
        caption="MPS_RD price verification: dataset close vs Merolagani last traded price",
        headers=("Bank", "FY", "Price date", "Dataset close (NPR)", "Merolagani LTP (NPR)", "Outcome"),
        rows=tuple(rows),
        notes=(
            f"Dataset close and Merolagani LTP agree on {n_match} of {len(rows)} bank-years. "
            "For NMB FY2076-77, the dataset recorded 437.00, whereas Merolagani reported LTP 436.00; "
            "437.00 was retained on the basis of ShareSansar's full daily record, but because "
            "ShareSansar is the dataset's primary source, this does not represent independent verification, "
            "and NEPSE official close remains unverified. Pre-merger NIMB rows trade under the NIB symbol on Merolagani."
        ),
    )
    return save_table(table, "tables/A4_price_verification")
