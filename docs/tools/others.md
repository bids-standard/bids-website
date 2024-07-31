# Tools

## Indexing and querying

These tools help index the content of BIDS datasets and return a listing of files that match a certain query
(for example "Give me all the files from subject `01` and `13` for datatypes `anat` and `eeg`.")

{{ MACROS___generate_tools_table(file="tools.yml", category="index and query") }}

## File handling

These tools help you work with certain specific BIDS files or may help you rename them.

{{ MACROS___generate_tools_table(file="tools.yml", category="file handling") }}

## Data annotation

These tools make it easier to curate the metadata of your BIDS dataset.

{{ MACROS___generate_tools_table(file="tools.yml", category="data annotation") }}

## Analysis

These packages or toolboxes are BIDS "friendly" and contain functionalities
that will make your life easeir if you work with BIDS datasets.

{{ MACROS___generate_tools_table(file="tools.yml", category="analysis") }}

## Others

{{ MACROS___generate_tools_table(file="tools.yml") }}
