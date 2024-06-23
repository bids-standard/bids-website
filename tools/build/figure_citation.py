from __future__ import annotations

import pandas as pd
import plotly.express as px
from bids_website.utils import data_dir, root_dir

INPUT_FILE = data_dir() / "count_citation.tsv"

TMP_DIR = root_dir() / "tmp"
TMP_DIR.mkdir(parents=True, exist_ok=True)


def main():
    df = pd.read_csv(INPUT_FILE, sep="\t")
    df = df.replace(
        "Guidelines for the content and format of PET brain data in publications and archives",
        "PET Guidelines",
    )
    plot_citation_count(df)


def plot_citation_count(df: pd.DataFrame):
    """
    Use Plotly to create a bar chart of the citation count per year stacked by paper.
    """
    # taken from https://colorbrewer2.org/#type=qualitative&scheme=Paired&n=12
    cmap = [
        "#a6cee3",
        "#1f78b4",
        "#b2df8a",
        "#33a02c",
        "#fb9a99",
        "#e31a1c",
        "#fdbf6f",
        "#ff7f00",
        "#cab2d6",
        "#6a3d9a",
        "#ffff99",
        "#b15928",
    ]
    cmap.reverse()

    fig = px.bar(
        df,
        x="years",
        y="nb_citations",
        color="papers",
        title="Citation count per year",
        labels={"years": "Year", "nb_citations": "Number of citations"},
        color_discrete_sequence=cmap,
    )

    fig.update_layout(margin=dict(l=0, r=0, t=40, b=0))

    fig.write_html(TMP_DIR / "citation_per_year.html")


if __name__ == "__main__":
    main()
