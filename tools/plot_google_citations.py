from __future__ import annotations

import pandas as pd
import plotly.express as px
from utils import data_dir

input_file = data_dir() / "citation_google_scholar.tsv"

df = pd.read_csv(input_file, sep="\t")

df["papers"] = df.paper

df = pd.wide_to_long(df, stubnames="year_", i="paper", j="year")

df = df.rename(columns={"year_": "nb_citations"})
df = df.reset_index(level=["year"])
print(df)
print(df.columns)

fig = px.bar(
    df,
    x="year",
    y="nb_citations",
    color="papers",
    title="Citation count per year",
    labels={"years": "Year", "nb_citations": "Number of citations"},
)
fig.show()
