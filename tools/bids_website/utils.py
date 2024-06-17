"""Functions that get reused across modules."""

from __future__ import annotations

import calendar
from datetime import datetime, timezone
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def root_dir():
    return Path(__file__).parents[2].absolute()


def bids_spec_dir():
    return root_dir() / "specification"


def data_dir():
    return root_dir() / "data"


def figures_dir():
    return root_dir() / "docs" / "assets" / "img"


def return_min_max_date(month, year=None):
    """Calculate min and maxdate for our time window of interest."""
    if year is None:
        year = datetime.now().year
    mindate = datetime(year, month, 1, tzinfo=timezone.utc)
    if month < 12:
        assert month >= 1, "month must be an int between 1 and 12"
        maxdate = datetime(year, month + 1, 1, tzinfo=timezone.utc)
    else:
        assert month == 12, "month must be an int between 1 and 12"
        maxdate = datetime(year + 1, 1, 1, tzinfo=timezone.utc)

    return mindate, maxdate


def plot_information(df: pd.DataFrame, month: int, print_to_file=True):
    """Plot maintainers report fig."""
    with sns.plotting_context("talk"):
        fig, axs = plt.subplots(
            2, 1, figsize=(10, 12), gridspec_kw={"hspace": 0.75}
        )
        plt.tight_layout()
        for i, item_type in enumerate(["PRs", "Issues"]):

            ax = axs.flat[i]

            sns.barplot(
                ax=ax,
                x="repo",
                y="value",
                hue="state",
                data=df[df["item_type"] == item_type],
            )

            if i > 0:
                ax.get_legend().remove()

            ax.set(xlabel="", title=item_type)
            ax.set_xticks(
                ax.get_xticks(), ax.get_xticklabels(), rotation=45, ha="right"
            )

    sns.despine(fig)
    fig.suptitle(f"BIDS: GitHub summary for {calendar.month_name[month]}")

    if print_to_file:
        fig.savefig("output_gh_summary.png", bbox_inches="tight")


def plot_neurostars(file, print_to_file=True):
    """Plot neurostars."""
    df = pd.read_csv(file, sep="\t")

    df["year_month"] = pd.to_datetime(df.year_month)

    with sns.plotting_context("talk"):
        fig, axs = plt.subplots(
            1, 1, figsize=(20, 12), gridspec_kw={"hspace": 0.75}
        )

        sns.lineplot(data=df, x="year_month", y="value", hue="key", ax=axs)

        plt.ylim([0, df.value.max()])

        sns.despine(fig)

        fig.suptitle("Neurostars summary for 'BIDS' tag")
        fig.show()

        if print_to_file:
            fig.savefig("output_neurostars.png", bbox_inches="tight")
