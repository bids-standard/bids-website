"""Ping the neurostars API.

Pings neurostars discourse API to:

- get all of topics for a list of tags
- saves the requests content to TSV for each tag
- prints some info for each tag
    - nb of topics
    - nb new topics
    - nb posts
    - nb new posts
    - nb of topics with no reply
    - nb of topics with accepted answer
    - mean nb of posts per topic

- for the BIDS tag it prints those data for:
    - the last month
    - the last X months

- outputs a summary table with the above info for each tag
- outputs a summary table with only the tags with new activity

OUTPUT:

- neurostars_summary_stats.tsv
- neurostars_short_summary_stats.tsv


API doc: https://docs.discourse.org/
"""

from datetime import datetime
from typing import Optional

import pandas as pd
import requests
from bids_website.utils import plot_neurostars, return_min_max_date
from rich import print

"""
list of tags
GET https://neurostars.org/tags.json
"""


verbose = True

# Gets only the first 2 pages of topics if True
debug = False

# Set a month and year of interest
month = 12  # integer, e.g., May = 5
year = 2023


def tags(debug=False):
    """Return tags."""
    if debug:
        return ["pybids", "bids-app"]
    else:
        return [
            "bids",
            "bids-specification",
            "bids-validator",
            "bids-app",
            "bidskit",
            "pybids",
            "bidsonym",
            "dcm2bids",
            "heudiconv",
            "mriqc",
            "fmriprep-report",
            "fmriprep",
            "dmriprep",
            "qsiprep",
            "aslprep",
            "smriprep",
            "dtiprep",
            "nipreps",
            "niprep",
            "fitlins",
            "openneuro",
            "openneuro-cli",
        ]


def tags_combine():
    """Combine tags."""
    return {
        "nipreps": [
            "fmriprep-report",
            "fmriprep",
            "dmriprep",
            "qsiprep",
            "aslprep",
            "smriprep",
            "dtiprep",
            "nipreps",
            "niprep",
        ],
        "openneuro": ["openneuro", "openneuro-cli"],
    }


def print_note(month, year, nb_topics, nb_posts):
    """Print note."""
    (mindate, maxdate) = return_min_max_date(month, year)
    monthname = datetime(year, month, 1).strftime("%B")
    print(f"Neurostats stats for {monthname} {year}")
    print(f"{nb_topics} new topics overall over the last 30 days")
    print(f"{nb_posts} new posts overall over the last 30 days")
    print(
        f"New topics for given tags counted between {mindate.date()} "
        f"and {maxdate.date()}"
    )
    print(f"Included queried tags:{tags()}")
    print(
        """
Note:
- some topics have several tags so they may be counted twice
- some topics may not be tagged so numbers here may be an underestimation
- tags with no new topics or posts are not included in the summary table below"""
    )


def shorten_table(summary_tsv):
    """Create a smaller version of the output table.

    - removes some extra columns
    - rename some columns
    - keep tags that have new topics or new posts
    """
    columns_to_drop = [
        "mean_nb_post_per_topic",
        "percent_no_reply",
        "percent_accepted_answer",
    ]

    columns_to_rename = {
        "topics_with_accepted_answer": "topics_with_answer",
    }

    short_summary = pd.read_csv(summary_tsv, sep="\t", index_col="tag")

    short_summary = short_summary.drop(columns=columns_to_drop)
    for col in columns_to_rename:
        short_summary = short_summary.rename(
            columns={col: columns_to_rename[col]}
        )
    for col in short_summary.columns.to_list():
        short_summary = short_summary.rename(
            columns={col: col.replace("_", " ")}
        )

    mask = (short_summary["new topics"] != 0) | (
        short_summary["new posts"] != 0
    )
    short_summary = short_summary[mask]

    short_summary.to_csv(
        "neurostars_short_summary_stats.tsv", sep="\t", index=True
    )


def nb_months_backlog(debug):
    """Return number of months backlog."""
    return 2 if debug else 11


def retrun_nb_posts_and_topics_in_last_30_days():
    """Return number of posts and topics in last 30 days."""
    url = "https://neurostars.org/about.json"
    response = requests.get(url)
    nb_topics = response.json()["about"]["stats"]["topics_30_days"]
    nb_posts = response.json()["about"]["stats"]["posts_30_days"]

    return nb_topics, nb_posts


def get_topics_for_tag(tag: str, debug=False, verbose=False) -> pd.DataFrame:
    """Return a dataframe of neurostars topics for a given tag.

    :param tag: neurostars tag
    :type tag: string
    :param debug: if ``True``, only gets topics of the first 2 pages. Defaults to False.
    :type debug: bool, optional
    :param verbose: defaults to False
    :type verbose: bool, optional
    :return: _description_
    :rtype: pandas.DataFrame
    """
    base_url = f"https://neurostars.org/tag/{tag}.json"

    if verbose:
        print(f"\nGET {base_url}")

    page = 0

    df = None

    dfs = []

    url = f"{base_url}"

    response = requests.get(url)

    nb_topics = 0
    if response.status_code == 200:
        nb_topics = response.json()["topic_list"]["tags"][0]["topic_count"]

    if nb_topics == 0:
        print(f"\n[red]No topic for: {url}[/red]")
        return

    while True:

        url = f"{base_url}?page={page}"

        response = requests.get(url)

        if response.status_code != 200:
            print(f"[red]request failed: {url}[/red]")
            break

        if debug and page == 3:
            break

        if verbose:
            print(f"[red]Page {page}[/red]")

        if len(response.json()["topic_list"]["topics"]) == 0:
            break

        for i, topic in enumerate(response.json()["topic_list"]["topics"]):
            if verbose:
                print(
                    f"{i}. {topic['created_at']} | "
                    f"{topic['posts_count']} | {topic['title']}"
                )

            nb_new_posts = return_nb_new_posts_for_topic(topic)
            topic["nb_new_posts"] = nb_new_posts

            df = pd.json_normalize(topic)
            dfs.append(df)

        page += 1

    if dfs != []:
        df = pd.concat(dfs)

    return df, nb_topics


def get_posts_for_topic(topic_id: str) -> pd.DataFrame:
    """Get posts for topic."""
    url = f"https://neurostars.org/t/{topic_id}/posts.json"

    response = requests.get(url)

    if response.status_code != 200:
        print(f"[red]request failed: {url}[/red]")
        return None

    posts = response.json()["post_stream"]["posts"]
    df = pd.json_normalize(posts)
    return df


def return_nb_new_posts_for_topic(topic: dict) -> int:
    """Return number of new posts for topic."""
    last_posted_at = topic["last_posted_at"]
    last_posted_at.replace("Z", "+00:00")
    last_posted_at = datetime.strptime(
        last_posted_at, "%Y-%m-%dT%H:%M:%S.%f%z"
    )

    beginning_month = datetime(year, month, 1).astimezone()

    if last_posted_at < beginning_month:
        return 0

    topic_id = topic["id"]
    df_post = get_posts_for_topic(topic_id)

    return return_nb_posts_since_month(df_post, month, year)


def return_nb_posts_since_month(
    df: pd.DataFrame, month: int, year: int
) -> int:
    """Return number of posts since month."""
    (mindate, maxdate) = return_min_max_date(month, year)
    created_at = pd.to_datetime(df["created_at"]).dt.date
    is_newly_created = (created_at > mindate.date()) & (
        created_at < maxdate.date()
    )
    return is_newly_created.sum()


def return_topics_for_month(df: pd.DataFrame, month: int, year: int):
    """Return topics for month."""
    (mindate, maxdate) = return_min_max_date(month, year)
    created_at = pd.to_datetime(df["created_at"]).dt.date
    return (created_at > mindate.date()) & (created_at < maxdate.date())


def return_stats(df: pd.DataFrame, nb_topics: Optional[int] = None) -> dict:
    """Return stats."""
    if nb_topics is None:
        nb_topics = len(df)
    stats = {
        "nb_topics": nb_topics,
        "no_reply": len(df[df["posts_count"] == 1]),
        "nb_posts": df["posts_count"].sum(),
        "sum_nb_new_posts": df["nb_new_posts"].sum(),
        "accepted_answer": len(
            df[df["has_accepted_answer"] == True]  # noqa: E712
        ),
    }

    return stats


def main():
    """Ping the neurostars API."""
    summary = {
        "tag": [],
        "nb_topics": [],
        "new_topics": [],
        "nb_posts": [],
        "new_posts": [],
        "topics_with_no_reply": [],
        "topics_with_accepted_answer": [],
    }

    for tag in tags(debug):

        (df, nb_topics) = get_topics_for_tag(tag, debug=debug, verbose=verbose)

        if verbose:
            print(f"[underline]neurostars tag '{tag}'[underline]")

        summary["tag"].append(tag)
        summary["nb_topics"].append(nb_topics)

        if df is not None:

            df.to_csv(f"{tag}.tsv", index=False, sep="\t")

            stats = return_stats(df, nb_topics)

            recent_topic = return_topics_for_month(df, month, year)

            summary["new_topics"].append(recent_topic.sum())
            summary["new_posts"].append(stats["sum_nb_new_posts"])
            summary["nb_posts"].append(stats["nb_posts"])
            summary["topics_with_no_reply"].append(stats["no_reply"])
            summary["topics_with_accepted_answer"].append(
                stats["accepted_answer"]
            )

            tmp_month = month
            tmp_year = year
            monthly_stats = {
                "year_month": [],
                "key": [],
                "value": [],
            }
            for _ in range(1, nb_months_backlog(debug)):

                topic_in_that_month = return_topics_for_month(
                    df, tmp_month, tmp_year
                )
                df_this_month = df[topic_in_that_month]

                stats = return_stats(df_this_month)

                for key in ["nb_topics", "no_reply", "accepted_answer"]:
                    monthly_stats["year_month"].append(
                        datetime(tmp_year, tmp_month, 1).strftime("%Y-%m")
                    )
                    monthly_stats["key"].append(key)
                    monthly_stats["value"].append(stats[key])

                tmp_month = tmp_month - 1
                if tmp_month <= 0:
                    tmp_month = 12
                    tmp_year = tmp_year - 1

            monthly_stats = pd.DataFrame.from_dict(monthly_stats)

            if tag == "bids":
                monthly_stats.to_csv("neurostars_monthly_stats.tsv", sep="\t")
                plot_neurostars(
                    "neurostars_monthly_stats.tsv", print_to_file=True
                )

    summary = pd.DataFrame(data=summary)
    summary["mean_nb_post_per_topic"] = summary.apply(
        lambda row: row.nb_posts / row.nb_topics, axis=1
    )
    summary["percent_no_reply"] = summary.apply(
        lambda row: row.topics_with_no_reply / row.nb_topics * 100, axis=1
    )
    summary["percent_accepted_answer"] = summary.apply(
        lambda row: row.topics_with_accepted_answer / row.nb_topics * 100,
        axis=1,
    )

    summary.to_csv("neurostars_summary_stats.tsv", sep="\t", index=False)

    (nb_topics, nb_posts) = retrun_nb_posts_and_topics_in_last_30_days()

    shorten_table("neurostars_summary_stats.tsv")

    print_note(month, year, nb_topics, nb_posts)
    print(summary)


if __name__ == "__main__":
    main()
