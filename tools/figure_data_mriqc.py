#!/usr/bin/env python

# from BIDS paper
#
# - MRIQC data are read from mriqc_results_summary.csv
#   - These data were generated from the original MRIQC web api dump
#     using `MRIQC_WepAPI_analysis.py`
#   - This requires substantial memory to run,
#     which is why we use the intermediate result to generate the figures
#

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# load MRIQC data
all_results_df = pd.read_csv("mriqc_results_summary.csv")

# individual plots for openneuro and mriqc
sns.set(font_scale=1.5)
sns.set_style("whitegrid")

all_results_df["Data type"] = all_results_df.datatype.replace(
    {"bold": "BOLD", "T1w": "T1-weighted"}
)
all_results_df["datetime"] = pd.to_datetime(all_results_df.month)

fig, ax = plt.subplots(figsize=(10, 6))

# plot datasets
color = "tab:green"
ax.set_xlabel("Date", fontsize=20)
ax.set_ylabel("Cumulative datasets")

line1 = sns.lineplot(
    x="datetime",
    y="nresults",
    hue="Data type",
    data=all_results_df,
    linewidth=3.2,
    ax=ax,
    palette=["red", "green"],
)


ax.set_title("MRIQC API data growth")
plt.tight_layout()
plt.savefig("figure2b.png", dpi=300)
