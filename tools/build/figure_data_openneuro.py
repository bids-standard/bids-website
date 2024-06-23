#!/usr/bin/env python

# from BIDS paper
#
# - OpenNeuro data are obtained from the openneuro API
#

import pandas as pd
import plotly.graph_objs as go

from plotly.subplots import make_subplots

from bids_website.utils import root_dir, data_dir

TMP_DIR = root_dir() / "tmp"


def main():

    df = pd.read_csv(
        data_dir() / "openneuro_datasets.tsv",
        sep="\t",
    )

    # end_year = 24  # set to current year + 1
    # # July 2 is the midpoint of year
    # midyears = pd.to_datetime([f"20{yr}-07-02" for yr in range(18, end_year)]).astype(int)
    # midyears

    df["cumsum_datasets"] = df["n_datasets"].cumsum()
    df["cumsum_subjects"] = df["n_subjects"].cumsum()

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    for col in ["cumsum_datasets", "cumsum_subjects"]:
        secondary_y = False
        if col == "cumsum_subjects":
            secondary_y = True

        fig.add_trace(
            go.Scatter(
                name=col.replace("cumsum_", ""),
                x=df["release_dates"],
                y=df[col],
                mode="lines",
            ),
            secondary_y=secondary_y,
        )
    fig.update_layout(title="Openneuro data growth", hovermode="x")
    fig.update_yaxes(
        title_text="Cumulative datasets", secondary_y=False, nticks=10
    )
    fig.update_yaxes(
        title_text="Cumulative subjects", secondary_y=True, nticks=10
    )
    fig.update_xaxes(title_text="date")

    fig.update_layout(margin=dict(l=0, r=0, t=40, b=0))

    fig.write_html(TMP_DIR / "openneuro_data_growth.html")


if __name__ == "__main__":
    main()
