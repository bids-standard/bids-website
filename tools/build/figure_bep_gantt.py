"""Creates a Gantt chart for the completed BEPs.

Also include a timeline of the main BIDS events.
"""

from __future__ import annotations

from datetime import datetime

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from bids_website.utils import data_dir, root_dir
from pyzotero import zotero
from ruamel.yaml import YAML

INCLUDE_PATCHES = False
START_DATE = "2014-10"
DATE_FORMAT = "%Y-%m"
Y_AXIS_VALUE = ""

# save as html
# NOTE: This file is ignored in git (see .gitignore)
OUTPUT_DIR = root_dir() / "tmp"


def create_bep_timeline(bep_type: str) -> type[go.Figure]:

    input_file = data_dir() / "beps" / "beps.yml"
    if bep_type == "merged BEPs":
        input_file = data_dir() / "beps" / "beps_completed.yml"

    with open(input_file, "r") as f:
        yaml = YAML(typ="safe", pure=True)
        data = yaml.load(f)

    validate_bep_metadata(data)

    df = []

    for bep in reversed(data):
        StartDoc = bep.get("google_doc_created")
        StartPR = bep.get("pull_request_created")
        Finish = bep["pull_request_merged"]

        display_name = (
            bep.get("display") if bep.get("display") else bep.get("title")
        )
        BEP = f"{bep['number']}-{display_name}"

        if bep_type != "draft BEPs" and StartDoc and StartPR:
            df.append(
                dict(
                    BEP=BEP,
                    Start=StartDoc,
                    Finish=StartPR,
                    Resource="Google Doc",
                )
            )

        if StartDoc and not StartPR:
            if bep_type == "draft BEPs":
                df.append(
                    dict(
                        BEP=BEP,
                        Start=StartDoc,
                        # use today as a placeholder for the PR creation date
                        # in format "YYYY-MM"
                        Finish=datetime.now().strftime("%Y-%m"),
                        Resource="Google Doc",
                    )
                )
            # Some very old merged BEPs never had a PR
            elif bep_type == "merged BEPs":
                df.append(
                    dict(
                        BEP=BEP,
                        Start=StartDoc,
                        Finish=Finish,
                        Resource="Google Doc",
                    )
                )

        if bep_type == "merged BEPs" and StartPR and Finish:
            df.append(
                dict(
                    BEP=BEP,
                    Start=StartPR,
                    Finish=Finish,
                    Resource="Pull Request",
                )
            )

        if bep_type == "proposed BEPs" and StartPR:
            df.append(
                dict(
                    BEP=BEP,
                    Start=StartPR,
                    # use today as a placeholder for the PR creation date
                    Finish=datetime.now().strftime("%Y-%m"),
                    Resource="Pull Request",
                )
            )

    df = pd.DataFrame(df)

    fig = px.timeline(
        df,
        x_start="Start",
        x_end="Finish",
        y="BEP",
        color="Resource",
        title="BIDS timeline",
    )

    return fig


def validate_bep_metadata(all_beps):
    for bep in all_beps:
        for required_key in [
            "title",
            "google_doc_created",
            "pull_request_created",
            "pull_request_merged",
        ]:
            if required_key not in bep:
                raise ValueError(
                    f"Missing required key {required_key} in BEP {bep['number']}"
                )


def plot_time_line(fig: go.Figure) -> type[go.Figure]:
    dates = [datetime.strptime(START_DATE, DATE_FORMAT), datetime.now()]
    y = [Y_AXIS_VALUE, Y_AXIS_VALUE]

    fig.add_trace(
        go.Scatter(
            x=dates,
            y=y,
            mode="lines",
            showlegend=False,
            line=dict(color="black", width=2),
            hoverinfo="skip",
        )
    )

    return fig


def plot_releases(
    fig: go.figure,
    timeline: pd.DataFrame,
    include_patches: bool = INCLUDE_PATCHES,
) -> type[go.Figure]:
    mask = timeline["type"] == "release"
    if not include_patches:
        mask = mask & (timeline["name"].str.endswith("0"))
    bids_releases = timeline["name"][mask].tolist()
    bids_releases_dates = timeline["date"][mask].tolist()

    dates = [datetime.strptime(d, DATE_FORMAT) for d in bids_releases_dates]
    y = [Y_AXIS_VALUE for _ in dates]

    fig.add_trace(
        go.Scatter(
            name="Releases",
            x=dates,
            y=y,
            mode="markers+text",
            marker=dict(color="black", size=10),
            text=bids_releases,
            hoverinfo="x+text",
            textposition="bottom center",
        ),
    )

    return fig


def add_publications_to_timeline(fig: go.Figure) -> type[go.Figure]:
    """Get publication info from Zotero and add to timeline."""
    zot = zotero.Zotero(library_id="5111637", library_type="group")
    items = zot.everything(zot.top())

    titles = []
    dois = []
    dates = []
    for item in items:
        titles.append(item["data"].get("title", "n/a"))
        dois.append(item["data"].get("DOI", "n/a"))
        dates.append(item["data"].get("date", "n/a"))

    fig.add_trace(
        go.Scatter(
            name="Publications",
            x=dates,
            y=[Y_AXIS_VALUE for _ in dates],
            mode="markers",
            marker=dict(color="blue", size=10),
            hoverinfo="x+text",
            text=titles,
        ),
    )

    return fig


def main():

    for bep_type in ["merged BEPs", "proposed BEPs", "draft BEPs"]:
        fig = create_bep_timeline(bep_type=bep_type)

        if bep_type == "merged BEPs":
            fig = plot_time_line(fig)

            timeline = pd.read_csv(data_dir() / "timeline.csv")

            fig = plot_releases(fig, timeline, include_patches=INCLUDE_PATCHES)

            # Add events timeline
            sub_df = timeline[timeline["type"] == "event"]

            fig.add_trace(
                go.Scatter(
                    name="Event",
                    x=sub_df["date"],
                    y=[Y_AXIS_VALUE for _ in sub_df["date"]],
                    mode="markers",
                    marker=dict(color="green", size=10),
                    hoverinfo="x+text",
                    text=sub_df["name"],
                ),
            )

        fig.update_yaxes(visible=True, showticklabels=False)

        fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))

        if bep_type == "merged BEPs":
            fig = add_publications_to_timeline(fig)

        fig.update_layout(legend_font_size=15)
        fig.update_layout(title=dict(font=dict(size=30)))
        fig.update_layout(yaxis=dict(tickfont=dict(size=15)))

        # save as html
        # NOTE: This file is ignored in git (see .gitignore)
        OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
        fig.write_html(
            OUTPUT_DIR / f"{bep_type.replace(' ', '_')}_timeline.html"
        )


if __name__ == "__main__":
    main()
