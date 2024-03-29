"""Creates a Gantt chart for the completed BEPs"""
from __future__ import annotations

from pathlib import Path

import pandas as pd
from ruamel.yaml import YAML
from rich import print


INCLUDE_PATCHES = False
START_DATE = "2014-10"
DATE_FORMAT = "%Y-%m"
Y_AXIS_VALUE = ""


def root_dir() -> Path:
    return Path(__file__).parent.parent


def data_dir() -> Path:
    return root_dir() / "_data"


def target_file() -> Path:
    return root_dir() / "_pages" / "get_involved.md"


def get_bep_timeline() -> pd.DataFrame:
    completd_beps = data_dir() / "beps_completed.yml"

    with open(completd_beps, "r") as f:
        yaml = YAML(typ="safe", pure=True)
        data = yaml.load(f)

    df = []

    # iterate over data in reverse order
    for bep in data:
        StartDoc = bep.get("google_doc_created")
        StartPR = bep.get("pull_request_created")
        Finish = bep["pull_request_merged"]

        BEP = f"{bep['number']} - {bep['title']}  "

        if StartDoc and StartPR:
            df.append(
                dict(
                    BEP=BEP,
                    Start=StartDoc,
                    Finish=StartPR,
                    Resource="Google Doc",
                )
            )
        if StartPR and Finish:
            df.append(
                dict(
                    BEP=BEP,
                    Start=StartPR,
                    Finish=Finish,
                    Resource="Pull Request",
                )
            )
        if not StartPR:
            df.append(
                dict(
                    BEP=BEP,
                    Start=StartDoc,
                    Finish=Finish,
                    Resource="Google Doc",
                )
            )

    df = pd.DataFrame(df)

    return df


def main():
    df = get_bep_timeline()

    text = """```mermaid
gantt
    title completed BEP timeline
    dateFormat YYYY-MM
    tickInterval 6month
    axisFormat %b-%Y
"""

    for bep in df.BEP.unique():
        bep_df = df[df.BEP == bep]
        google_start = bep_df[bep_df.Resource == "Google Doc"].Start.values[0]
        google_end = bep_df[bep_df.Resource == "Google Doc"].Finish.values[0]

        text += f"""    section BEP{bep[:3]}
            Google doc    :{google_start}, {google_end}
"""

        pr_df = bep_df[bep_df.Resource == "Pull Request"]
        if len(pr_df) > 0:
            pr_start = pr_df.Start.values[0]
            pr_end = pr_df.Finish.values[0]

            text += f"""            Pull request  :{pr_start}, {pr_end}
"""

    text += "```\n"

    print(text)

    # insert into target file
    with open(target_file(), "r") as f:
        lines = f.readlines()

    inser_mermaid_here = False
    with open(target_file(), "w") as f:
        for line in lines:
            if line.startswith("<!-- MERMAID GANTT CHART STARTS -->"):
                inser_mermaid_here = True
                f.write("<!-- MERMAID GANTT CHART STARTS -->\n")
                f.write(text)
            if line.startswith("<!-- MERMAID GANTT CHART ENDS -->"):
                inser_mermaid_here = False

            if not inser_mermaid_here:
                f.write(line)


if __name__ == "__main__":
    main()
