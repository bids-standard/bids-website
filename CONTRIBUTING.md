# Contributing to the BIDS website

**Welcome to the BIDS website repository!**

_We're so excited you're here and want to contribute._

We hope that these guidelines are designed to make it as easy as possible to get involved.
If you have any questions that aren't discussed below, please let us know
by [opening an issue](https://github.com/bids-standard/bids-website/issues/new).

If you are not familiar with Git and GitHub,
check our [generic contributing guidelines](https://bids.neuroimaging.io/collaboration/bids_github/CONTRIBUTING.html).

If you want to contribute to the BIDS website,
make sure you also read the instructions below.

## Serving locally

### Requirements

- [uv](https://docs.astral.sh/uv/)
- node.js >= 14
- npm >= ???

<!-- TODO find minimal version of node and npm
For some quality checks and rare operations, you will need node.js and npm. -->

Even though this is not required,
having `make` installed will make it easier to easily serve the website locally.

### Quick setup with venv

For a minimal setup using Python's venv:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
mkdocs serve
```

### Install and serve

Fork and clone the repository and its submodules

```bash
git clone https://github.com/YOUR_USER_NAME/bids-website.git --recurse-submodules
```

Run `uv` to create a virtual environment in `.venv/`.

```bash
uv sync --frozen
```

Generate all the content required for the build:

-   copies some pages from the specification repo

-   updates the list of contributors

-   generates the page for each BEP based on its metadata

-   updates the list of BIDS examples

-   generates all the 'plotly' interactive plots as html files in the `tmp` folder
    that will be 'injected' in the website as snippets (with `--8<--`)

```bash
make update
```

Serve the website with the mkdocs.

```bash
uv run mkdocs serve
```

## Maintenance

### Requirements

Same as for the install but you will also need to install `tox`.

```bash
uv run tox
```

## Update all files

```bash
make update
```

## Run all formatting / linting tools

```bash
tox
make remark
```

### Using remark to format a file

If you have a completely new file that you want to lint,
you can use the following to get most of the markdown formatting done.

Some will still need some manual work.

```bash
npm run format -- path_to_file --ouput
```

## Upgrading dependencies

Rerun `uv sync`:

```bash
uv sync --upgrade
```
