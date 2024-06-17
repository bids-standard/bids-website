"""Adds a dashboard in README that shows the status of all bids apps default branch CI runs."""

import ruamel.yaml as yaml
from pathlib import Path
import pandas as pd

yaml = yaml.YAML()

root_dir = Path(__file__).parent.parent

data = yaml.load(root_dir / "_config.yml")

name = []
status = []
ci = []
last_commit = []
version = []

for app in data["apps"]:
    name.append(f"[{app['gh']}](https://github.com/{app['gh']})")

    status.append(app.get("status", "unknown"))

    branch = app.get("branch", "master")

    if app.get("status") == "unmaintained":
        ci.append(
            "[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)"
        )

    else:

        if not app.get("ci"):
            image = f"https://circleci.com/gh/{ app['gh'] }.svg?style=shield"
            link = f"https://circleci.com/gh/{ app['gh'] }/tree/{ branch }"

        elif app["ci"] == "none":
            image = "https://img.shields.io/badge/CI-none-lightgrey"
            link = None

        elif app["ci"] == "travis":
            image = f"https://app.travis-ci.com/{ app['gh'] }.svg?branch={ branch }"
            link = f"https://app.travis-ci.com/{ app['gh'] }"

        elif app["ci"] == "gh":
            image = f"https://github.com/{ app['gh'] }/actions/workflows/{ app['workflow'] }.yml/badge.svg?branch={ branch }"
            link = f"https://github.com/{ app['gh'] }/actions/workflows/{ app['workflow'] }.yml/"

        else:
            image = "https://img.shields.io/badge/CI-UNKNOWN-darkgrey"
            link = None

        ci.append(f"[![CI]({image})]({link})")

    last_commit.append(
        f"![GitHub last commit](https://img.shields.io/github/last-commit/{app['gh']})"
    )

    version.append(
        f"![version tag](https://img.shields.io/github/v/tag/{ app['gh'].lower() }?label=version)"
    )

df = pd.DataFrame(
    {
        "name": name,
        "status": status,
        "ci": ci,
        "last commit": last_commit,
        "version": version,
    }
)

# append to readme
with open(root_dir / "README.md", "r") as f:
    readme = f.readlines()

with open(root_dir / "README.md", "w") as f:
    for line in readme:
        f.write(line)
        if line.startswith("<!-- INSERT DASHBOARD HERE -->"):
            f.write("\n\n")
            df.to_markdown(f, index=False)
            break
