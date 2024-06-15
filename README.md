[![Documentation Status](https://readthedocs.org/projects/bids-website/badge/?version=latest)](https://bids-website.readthedocs.io/en/latest/?badge=latest)

# The one true BIDS website

View it here: https://bids-website.readthedocs.io/en/latest/?badge=latest

## Serving locally

### Requirements

<!-- TODO determines minimum python version -->
- python 3.X

## Install

Clone the repo and its submodules

```bash
git clone https://github.com/bids-standard/bids-website.git --recurse-submodules
```

Create a virtual environment using `conda`, `venv` of what other environment management tool you prefer.

Install all the dependencies.

```bash
pip install -r requirements.txt
```

Serve the website with the mkdocs.
```bash
mkdocs serve
```

## Maintenance

### Requirements

Same as for the install but you will also need to install `tox`.

```bash
pip install tox
```

<!-- TODO find minimal version of node and npm -->
For some quality checks and rare operations, you will need node.js and npm.
