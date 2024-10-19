# Tools for working with bids-website

This README file describes the tools under the `/tools` directory of the bids-website repository.

## Requirements

Install all Python requirements (listed in the `tools/pyproject.toml`)

```bash
pip install --editable tools[dev]
```
The editable install is required to be able to use relative path to the `/data` folder.

## Update the Gantt chart of completed BEPs

There are two ways of creating Gantt charts for a BIDS timeline.

Then, use one of the following two methods:

1. `python -u tools/bep_gantt_html_create` creates a file: `data/bids_timeline.html` that you can inspect in your browser.
   This file depends on the `tools/timeline.csv` data, which you should keep up to date.

1. `python -u tools/bep_gantt_mermaid_insert` directly inserts code
   for a "mermaid" Gantt chart into the Get Involved page of the website.
   You can inspect how that chart looks by building the website using Jekyll and serving locally.
   This code depends on data from the files `beps_completed.yml` files in the `data` directory.
   You should keep that file up to date.

## Updating grant writing kit info

### Citation Count

This script queries the [OpenCitations](https://opencitations.net/index/coci) API
to get the number of papers that cited a list of papers related to the [BIDS](https://bids.neuroimaging.io/) data organization standard.

The resulting citation count is then visualized using [Plotly](https://plotly.com/python/).

### Usage

1. Open the `count_citation.py` file and replace `YOUR-OPENCITATIONS-ACCESS-TOKEN` with your OpenCitations access token.

1. Run the script:

   ```bash
   python tools/count_citation.py
   ```

1. The citation count for each paper will be saved in a TSV file named `count_citation.tsv`
   in the same directory as the script.

1. A bar chart of the citation count will be displayed using your default browser.

## Interactive figures

- use plotly to create interactive HTML figures

- HTML figures are not committed and saved in a `tmp` folder in the root of the repo.

- HTML figures and other content that can be updated is "stored" in external files
  that are injected into markdown files using [snippets](https://facelessuser.github.io/pymdown-extensions/extensions/snippets/)

<!-- use snippet to include a file
https://facelessuser.github.io/pymdown-extensions/extensions/snippets/#snippets-notation
-->

```text
--8<-- "tmp/bids_timeline.html"
```
