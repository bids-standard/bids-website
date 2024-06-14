"""Provide updates in repositories of the bids-standard GitHub organization.

NOTE: This script can take around 10 minutes to run. It's not very efficient.

Information of interest within 1 month time frame:
- PRs opened
- PRs merged (not just closed; and even if opened before time frame)
- Issues opened
- Issues closed (even if opened before time frame)

Maybe for future extensions:
- N files changed on master
- N additions, N deletions on master
- N users involved in issues and PRs

Requirements:
- PyGitHub (https://github.com/PyGithub/PyGithub)
- Matplotlib
- Seaborn
- Pandas

"""

import json

import pandas as pd
from github import Github
from tqdm import tqdm
from utils import plot_information, return_min_max_date

# Settings
# Set a token (or use None)
# NOTE: Never commit a token to git history
token = None
g = Github(login_or_token=token)

# Set a month and year of interest
month = 11  # integer, e.g., May = 5
year = 2024

user = "bids-standard"

# Set repositories of interest
repos = [
    "bids-specification",
    "bids-examples",
    "bids-validator",
    "bids-website",
    "bids-starter-kit",
    "bids-schema",
    "pybids",
    "bids-matlab",
]


def main(repos):
    """Make fig for maintainers report."""
    repos = [f"{user}/" + repo for repo in repos]

    # Parse information

    (mindate, maxdate) = return_min_max_date(month, year=year)

    # PRs/issues are ordered newest to oldest by creation date
    # we go through them in order, counting closed and created
    # once for each repo
    log = {}
    dfs = []
    for repo_name in tqdm(repos):
        log[repo_name] = {}
        repo = g.get_repo(repo_name)
        data = {
            "PRs": {"Opened": 0, "Closed": 0},
            "Issues": {"Opened": 0, "Closed": 0},
        }
        for item_type in ["PRs", "Issues"]:
            log[repo_name][item_type] = {}
            for state in ["opened", "closed"]:

                log[repo_name][item_type][state] = []

                if item_type == "PRs":
                    items = repo.get_pulls(
                        state="open" if state == "opened" else state
                    )
                else:
                    assert item_type == "Issues"
                    items = repo.get_issues(
                        state="open" if state == "opened" else state
                    )

                for item in items:

                    # if looking through issues, clean up: each PR is an issue as
                    # well, but we don't want to count these, see:
                    # https://github.com/PyGithub/PyGithub/issues/1744
                    if (item_type == "Issues") and (
                        item.pull_request is not None
                    ):
                        continue

                    added = False
                    if item.closed_at is not None:
                        if (item.closed_at >= mindate) and (
                            item.closed_at < maxdate
                        ):
                            if item_type == "PRs":
                                # ignore PRs that were closed but not merged
                                if not item.is_merged():
                                    continue
                            data[item_type]["Closed"] += 1
                            added = True
                    if (item.created_at >= mindate) and (
                        item.created_at < maxdate
                    ):
                        data[item_type]["Opened"] += 1
                        added = True

                    if added:
                        log[repo_name][item_type][state] += [item.html_url]

        df = pd.DataFrame(data).melt(ignore_index=False).reset_index()
        df["repo"] = repo_name.replace(f"{user}/", "")
        df.columns = ["state", "item_type", "value", "repo"]
        dfs.append(df)

    df = pd.concat(dfs)

    # print log for double checking / debugging
    print(json.dumps(log, indent=4))

    plot_information(df, month, print_to_file=True)


if __name__ == "__main__":
    main(repos)
