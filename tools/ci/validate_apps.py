"""Runs checks for each app."""

from pathlib import Path
from warnings import warn

import requests
import ruamel.yaml as yaml
from bids_website.utils import data_dir

beps = data_dir() / "tools" / "apps.yml"

yaml = yaml.YAML()

root_dir = Path(__file__).parent.parent

data = yaml.load(root_dir / "_config.yml")

missing_dh = []
invalid_dh = []


for app in data["apps"]:

    if app["status"] == "unmaintained":
        continue

    print(f"Checking {app['gh']}")

    if not app.get("dh"):
        missing_dh.append(app["gh"])
        continue

    url = f"https://registry.hub.docker.com/v2/repositories/{app['dh']}/"

    response = requests.get(url, auth=None)

    if response.status_code != 200:
        invalid_dh.append(app["gh"])

if missing_dh:
    warn(
        f"The following BIDS apps are missing a Docker hub image.\n{missing_dh}",
        stacklevel=2,
    )

if invalid_dh:
    raise ValueError(
        f"The following BIDS apps have invalid Docker hub image URL.\n{invalid_dh}"
    )
