"""Testing plotting functions."""

import pandas as pd
from bids_website.utils import plot_information


def test_ploting():
    """Test plotting."""
    dfs = []
    month = 9

    data = {
        "PRs": {"Opened": 1, "Closed": 2},
        "Issues": {"Opened": 3, "Closed": 4},
    }
    df = pd.DataFrame(data).melt(ignore_index=False).reset_index()
    df["repo"] = "bids-specification"
    df.columns = ["state", "item_type", "value", "repo"]

    data = {
        "PRs": {"Opened": 1, "Closed": 2},
        "Issues": {"Opened": 3, "Closed": 4},
    }
    df = pd.DataFrame(data).melt(ignore_index=False).reset_index()
    df["repo"] = "bids-schema"
    df.columns = ["state", "item_type", "value", "repo"]

    dfs.append(df)
    df = pd.concat(dfs)

    print(df)

    plot_information(df, month)
