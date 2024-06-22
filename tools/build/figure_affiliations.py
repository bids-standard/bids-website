"""Plot affiliations on map."""

from __future__ import annotations

import pandas as pd
import plotly.express as px
from bids_website.utils import data_dir, root_dir

OUTPUT_DIR = root_dir() / "tmp"


def main():

    output_file = data_dir() / "people" / "affiliations.tsv"

    df = pd.read_csv(output_file, sep="\t")

    fig = px.scatter_geo(
        df,
        lat=df.latitude,
        lon=df.longitude,
        hover_name="address",
        projection="natural earth",
    )

    fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))

    # save as html
    # NOTE: This file is ignored in git (see .gitignore)
    OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
    fig.write_html(OUTPUT_DIR / "affiliations.html")


if __name__ == "__main__":
    main()
