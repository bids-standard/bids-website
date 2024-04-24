# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# This notebook performs analysis of a dump of MRIQC web API data
# to plot usage statistics over time.
#
# Note that at present this requires a large amount of memory
# given the size of the database;
# it should run successfully on a system with 64GB of RAM.
#
# Before executing the notebook,
# you must first expand the archive containing the data:
# `tar zxvf mriqc_2023-06-12.tar.gz`
#
# taken from https://osf.io/x7fh8/?view_only=
#
# MRIQC web API doc: https://mriqc.nimh.nih.gov/docs/api

import datetime

# %%
import json
from json import JSONDecodeError

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pandas import Timestamp

# %%
# after https://stackoverflow.com/questions/57267694/round-pandas-date-to-nearest-year-month


def round_date_to_nearest_month(ts: Timestamp) -> Timestamp:
    return Timestamp(ts.year, ts.month, 1)


def round_date_to_nearest_year(ts: Timestamp) -> Timestamp:
    return Timestamp(ts.year, 1, 1)


# %%
def fixdate(timelong):
    return pd.to_datetime(
        datetime.datetime.fromtimestamp(int(timelong) // 1e3).strftime(
            "%m/%d/%Y, %H:%M:%S"
        )
    )


def fix_scannername(model):
    try:
        model = model.lower()
    except AttributeError:
        return None
    if "prisma" in model:
        modelname = "Prisma"
    elif "trio" in model:
        modelname = "Trio"
    elif "verio" in model:
        modelname = "Verio"
    elif "skyra" in model:
        modelname = "Skyra"
    elif "mr750" in model:
        modelname = "MR750"
    elif "allegra" in model:
        modelname = "Allegra"
    elif "hdx" in model:
        modelname = "SignaHDx"
    elif "ingenia" in model:
        modelname = "Ingenia"
    else:
        modelname = None
    return modelname


def get_data(datafile, drop_duplicates=True):

    datatype = "bold" if "bold" in datafile else "T1w"
    results = []
    problems = 0

    with open(datafile) as f:
        for line in f.readlines():
            try:
                results.append(json.loads(line.strip()))
            except JSONDecodeError:
                problems += 1

    print(
        f"found {len(results)} results in json, problems decoding {problems} records"
    )
    return results, datatype


def clean_data(results, datatype, drop_duplicates=True):
    assert datatype in ["bold", "T1w"]
    results_clean = []
    expand_vars = ["bids_meta", "provenance"]
    for r in results:
        for ev in expand_vars:
            if ev not in r:
                continue
            for k, v in r[ev].items():
                r[k] = v
            del r[ev]
        results_clean.append(r)

    results_df = pd.DataFrame(results_clean)
    results_df["_created"] = pd.to_datetime(
        [i["_created"]["$date"] for i in results_clean]
    )
    if "MultibandAccelerationFactor" in results_df:
        results_df["MultibandAccelerationFactor"] = np.nan_to_num(
            results_df["MultibandAccelerationFactor"]
        ).astype("int")
    results_df = results_df.assign(
        month=[round_date_to_nearest_month(i) for i in results_df._created],
        year=[round_date_to_nearest_year(i) for i in results_df._created],
        datatype=datatype,
    )

    results_df = results_df.sort_values(by="month")
    # clean up
    # results_df = results_df.query('MagneticFieldStrength < 15')

    results_df = results_df.assign(
        Scanner=[fix_scannername(i) for i in results_df.ManufacturersModelName]
    )
    fs = np.array(results_df["MagneticFieldStrength"].values.tolist())

    results_df["MagneticFieldStrength"] = np.where(
        fs > 100, fs / 10000, fs
    ).tolist()

    results_df["MagneticFieldStrength"] = np.around(
        results_df.MagneticFieldStrength, 1
    )

    if drop_duplicates:
        ds_size_orig = results_df.shape[0]
        results_df = results_df.drop_duplicates(subset="md5sum", keep="last")
        print(f"dropped {ds_size_orig - results_df.shape[0]} duplicates")
    print(f"final size: {results_df.shape}")
    results_df = results_df.assign(
        nresults=np.arange(1, results_df.shape[0] + 1)
    )
    return results_df


# %%
bold_results, datatype = get_data("mriqc_2023-06-12/bold.json")
bold_results_df = clean_data(bold_results, datatype)

# %%
t1w_results, datatype = get_data("mriqc_2023-06-12/T1w.json")
t1w_results_df = clean_data(t1w_results, datatype)


# %%
all_results_df = pd.concat((bold_results_df, t1w_results_df))
all_results_df = all_results_df.sort_values(by="month").reset_index()
all_results_df.shape
all_results_df.to_csv("mriqc_results_summary.csv")

# %%
sns.lineplot(
    x="month", y="nresults", hue="datatype", data=all_results_df, linewidth=2
)
plt.xlabel("Date", fontsize=16)
plt.ylabel("Number of results", fontsize=16)
plt.tight_layout()
plt.savefig("all_n_vs_date.png", dpi=300)
