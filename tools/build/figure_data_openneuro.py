#!/usr/bin/env python

# from BIDS paper
#
# - OpenNeuro data are obtained from the openneuro API
#
#

import json
import os
from collections import defaultdict
from datetime import datetime

import pandas as pd
import plotly.graph_objs as go
import requests
from plotly.subplots import make_subplots
from rich import print

from bids_website.utils import root_dir, data_dir

UPDATE = False

TMP_DIR = root_dir() / "tmp"
TMP_DIR.mkdir(parents=True, exist_ok=True)

scan_dict = {
    "anatomical": "anat",
    "structural": "anat",
    "functional": "func",
    "behavioral": "beh",
    "diffusion": "dwi",
    "perfusion": "perf",
}
age_dict = {
    (0, 10): "0-10",
    (11, 17): "11-17",
    (18, 25): "18-25",
    (26, 34): "26-34",
    (35, 50): "35-50",
    (51, 65): "51-65",
    (66, 1000): "66+",
}
bool_dict = {True: "yes", False: "no", None: "no"}
date_arg_format = "%m/%d/%Y"
date_input_format = "%Y-%m-%d"
date_output_format = "%-m/%-d/%Y"


def get_openneuro_datasets(query=None):
    print("Getting openneuro datasets...")
    headers = {
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Connection": "keep-alive",
        "DNT": "1",
        "Origin": "https://openneuro.org",
    }
    if query is None:
        query = """
        {
            edges {
                cursor,
                node {
                    id,
                    publishDate,
                    latestSnapshot {
                        tag,
                        dataset {
                            name,
                            publishDate,
                            metadata {
                            trialCount,
                            studyDesign,
                            studyDomain,
                            studyLongitudinal,
                            dataProcessed,
                            species,
                            associatedPaperDOI,
                            openneuroPaperDOI
                            dxStatus
                            }
                        },
                        description {
                            SeniorAuthor
                        },
                        summary {
                            subjects,
                            modalities,
                            secondaryModalities,
                            subjectMetadata {
                                age
                            },
                            tasks,
                            dataProcessed
                        }
                    }
                }
            }
        }
        """.replace(
            "\n", ""
        )

    data = '{"query":"query testq{datasets ' + query + '}"}'

    response = requests.post(
        "https://openneuro.org/crn/graphql", headers=headers, data=data
    )
    response = response.json()

    datasets = {}

    while True:
        for y in response["data"]["datasets"]["edges"]:

            datasets[y["node"]["id"]] = y

        if len(response["data"]["datasets"]["edges"]) < 25:
            break

        next_cur = y["cursor"]
        data = (
            f'{{"query": "query testq{{datasets(after: \\"{next_cur}\\") {query}'
            + '}"}'
        )
        response = requests.post(
            "https://openneuro.org/crn/graphql", headers=headers, data=data
        )
        response = response.json()

    return datasets


# utility functions to clean things up - from metadata_update.py
def format_modalities(all_modalities):
    Modalities_available_list = []
    if any("MRI_" in e for e in all_modalities):
        all_modalities.remove("MRI")
        for m in all_modalities:
            if "MRI" in m:
                scan_type = scan_dict[m.split("MRI_", 1)[1].lower()]
                new_m = "MRI - " + scan_type
                Modalities_available_list.append(new_m)
            else:
                Modalities_available_list.append(m)
    else:
        Modalities_available_list = all_modalities
    return ", ".join(Modalities_available_list)


def format_ages(raw_age_list):
    if raw_age_list:
        age_list = sorted([x["age"] for x in raw_age_list if x["age"]])
        formatted_list = [
            value
            for key, value in age_dict.items()
            if any(x for x in age_list if x >= key[0] and x <= key[1])
        ]
        return ", ".join(formatted_list)
    else:
        return ""


def format_name(name):
    if not name:
        return ""
    elif "," not in name:
        last = name.split(" ")[-1]
        first = " ".join(name.split(" ")[:-1])
        new_name = last + ", " + first
        return new_name
    else:
        return name


def main():

    # get metadata from the openneuro API
    if UPDATE or not (TMP_DIR / "datasets.json").exists():
        datasets = get_openneuro_datasets()
        if UPDATE:
            with open(TMP_DIR / "datasets.json", "w") as f:
                json.dump(datasets, f, indent=4)
    else:
        with open(TMP_DIR / "datasets.json") as f:
            datasets = json.load(f)

    # get metadata into a format suitable to generate a dataframe
    output = []

    for accession_Number, y in datasets.items():
        Dataset_made_public_datetime = datetime.strptime(
            y["node"]["publishDate"][:10], date_input_format
        )
        Dataset_URL = os.path.join(
            "https://openneuro.org/datasets/",
            accession_Number,
            "versions",
            y["node"]["latestSnapshot"]["tag"],
        )
        Dataset_name = y["node"]["latestSnapshot"]["dataset"]["name"]
        Dataset_made_public = Dataset_made_public_datetime.strftime(
            date_output_format
        )
        Most_recent_snapshot_date = datetime.strptime(
            y["node"]["latestSnapshot"]["dataset"]["publishDate"][:10],
            date_input_format,
        ).strftime(date_output_format)
        if y["node"]["latestSnapshot"]["summary"] is not None:
            Number_of_subjects = len(
                y["node"]["latestSnapshot"]["summary"]["subjects"]
            )
            Modalities_available = format_modalities(
                y["node"]["latestSnapshot"]["summary"]["secondaryModalities"]
                + y["node"]["latestSnapshot"]["summary"]["modalities"]
            )
            Ages = format_ages(
                y["node"]["latestSnapshot"]["summary"]["subjectMetadata"]
            )
            Tasks_completed = ", ".join(
                y["node"]["latestSnapshot"]["summary"]["tasks"]
            )
        else:
            Number_of_subjects = None
            Modalities_available = None
            Ages = None
            Tasks_completed = None

        if y["node"]["latestSnapshot"]["dataset"]["metadata"] is not None:
            DX_status = y["node"]["latestSnapshot"]["dataset"]["metadata"][
                "dxStatus"
            ]
            Number_of_trials = y["node"]["latestSnapshot"]["dataset"][
                "metadata"
            ]["trialCount"]
            Study_design = y["node"]["latestSnapshot"]["dataset"]["metadata"][
                "studyDesign"
            ]
            Domain_studied = y["node"]["latestSnapshot"]["dataset"][
                "metadata"
            ]["studyDomain"]
            Longitudinal = (
                "Yes"
                if y["node"]["latestSnapshot"]["dataset"]["metadata"][
                    "studyLongitudinal"
                ]
                == "Longitudinal"
                else "No"
            )
            Processed_data = (
                "Yes"
                if y["node"]["latestSnapshot"]["dataset"]["metadata"][
                    "dataProcessed"
                ]
                else "No"
            )
            Species = y["node"]["latestSnapshot"]["dataset"]["metadata"][
                "species"
            ]
            DOI_of_paper_associated_with_DS = y["node"]["latestSnapshot"][
                "dataset"
            ]["metadata"]["associatedPaperDOI"]
            DOI_of_paper_because_DS_on_OpenNeuro = y["node"]["latestSnapshot"][
                "dataset"
            ]["metadata"]["openneuroPaperDOI"]
        else:
            DX_status = ""
            Number_of_trials = ""
            Study_design = ""
            Domain_studied = ""
            Longitudinal = ""
            Processed_data = ""
            Species = ""
            DOI_of_paper_associated_with_DS = ""
            DOI_of_paper_because_DS_on_OpenNeuro = ""

        Senior_Author = format_name(
            y["node"]["latestSnapshot"]["description"]["SeniorAuthor"]
        )
        line_raw = [
            accession_Number,
            Dataset_URL,
            Dataset_name,
            Dataset_made_public,
            Most_recent_snapshot_date,
            Number_of_subjects,
            Modalities_available,
            DX_status,
            Ages,
            Tasks_completed,
            Number_of_trials,
            Study_design,
            Domain_studied,
            Longitudinal,
            Processed_data,
            Species,
            DOI_of_paper_associated_with_DS,
            DOI_of_paper_because_DS_on_OpenNeuro,
            Senior_Author,
        ]
        line = ["" if x is None else str(x) for x in line_raw]
        output.append(line)

    # create data frame
    colnames = [
        "AccessionNumber",
        "Dataset URL",
        "Dataset name",
        "ReleaseDate",
        "Most recent snapshot date (MM/DD/YYYY)",
        "NSubjects",
        "Modalities",
        "DX status(es)",
        "Ages (range)",
        "Tasks completed?",
        "# of trials (if applicable)",
        "Study design",
        "Domain studied",
        "Longitudinal?",
        "Processed data?",
        "Species",
        "DOI of paper associated with DS (from submitter lab)",
        "DOI of paper because DS on OpenNeuro",
        "Senior Author (lab that collected data) Last, First",
    ]

    metadata = pd.DataFrame(output, columns=colnames)
    metadata["NSubjects"] = [
        None if i == "" else int(i) for i in metadata["NSubjects"]
    ]
    metadata["ReleaseDate"] = pd.to_datetime(metadata["ReleaseDate"])

    # Clean up data to create plots
    df_sorted = metadata.sort_values("ReleaseDate")
    df_sorted["ones"] = 1
    df_sorted["cumulative"] = df_sorted["ones"].cumsum()
    df_sorted["cumulative_subjects"] = df_sorted["NSubjects"].cumsum()
    dates = df_sorted["ReleaseDate"].unique()

    print("Earliest dataset:", dates.min())
    print("Latest dataset:", dates.max())

    # fix dates to reflect fact that early datasets were all from openneuro
    # df_sorted.loc[df_sorted['ReleaseDate'] < pd.Timestamp(2018,8,1), 'ReleaseDate'] = '2018-08-01'
    # df_sorted

    datasets = defaultdict(int)
    subjects = defaultdict(int)

    for date, nsub in metadata[["ReleaseDate", "NSubjects"]].values:
        datasets[date.strftime("%Y-%m-%d")] += 1
        subjects[date.strftime("%Y-%m-%d")] += nsub

    datadict = defaultdict(list)
    for k in datasets.keys():
        datadict["ReleaseDate"].append(k)
        datadict["n_datasets"].append(datasets[k])
        datadict["n_subjects"].append(subjects[k])

    df_plotting = pd.DataFrame(datadict)
    df_plotting["ReleaseDate"] = pd.to_datetime(df_plotting["ReleaseDate"])
    df_plotting = df_plotting.set_index("ReleaseDate").sort_values(
        by="ReleaseDate"
    )

    df_plotting["cumsum_datasets"] = df_plotting["n_datasets"].cumsum()
    df_plotting["cumsum_subjects"] = df_plotting["n_subjects"].cumsum()

    release_dates = df_plotting.index.astype(int)

    df_plotting["release_dates"] = pd.to_datetime(release_dates)

    df_plotting.to_csv(
        data_dir() / "openneuro_datasets.tsv", sep="\t", index=False
    )

    # end_year = 24  # set to current year + 1
    # # July 2 is the midpoint of year
    # midyears = pd.to_datetime([f"20{yr}-07-02" for yr in range(18, end_year)]).astype(int)
    # midyears

    release_datetimes = pd.to_datetime(release_dates)

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    for col in ["cumsum_datasets", "cumsum_subjects"]:
        secondary_y = False
        if col == "cumsum_subjects":
            secondary_y = True

        fig.add_trace(
            go.Scatter(
                name=col.replace("cumsum_", ""),
                x=release_datetimes,
                y=df_plotting[col],
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
