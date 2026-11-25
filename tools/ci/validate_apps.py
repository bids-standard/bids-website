"""Runs checks for each BIDS app."""

from warnings import warn

import requests
from bids_website.utils import data_dir
from ruamel import yaml

yaml = yaml.YAML()

file = data_dir() / "tools" / "apps.yml"
data = yaml.load(file)

missing_image = []
invalid_image = []


def ghcr_image_exists(image: str) -> bool:
    """Check that image has tags on GitHub Container Registry."""
    image = image.lower()
    token = (
        requests.get(f"https://ghcr.io/token?scope=repository:{image}:pull")
        .json()
        .get("token")
    )
    response = requests.get(
        f"https://ghcr.io/v2/{image}/tags/list",
        headers={"Authorization": f"Bearer {token}"},
    )
    return response.status_code == 200


for app in data["apps"]:
    if app["status"] == "unmaintained":
        continue

    print(f"Checking {app['gh']}")

    if app.get("dh"):
        url = f"https://registry.hub.docker.com/v2/repositories/{app['dh']}/"
        valid = requests.get(url, auth=None).status_code == 200
    elif app.get("ghcr"):
        valid = ghcr_image_exists(app["ghcr"])
    else:
        missing_image.append(app["gh"])
        continue

    if not valid:
        invalid_image.append(app["gh"])

if missing_image:
    warn(
        "The following BIDS apps are missing "
        f"a Docker hub or ghcr.io image.\n{missing_image}",
        stacklevel=2,
    )

if invalid_image:
    raise ValueError(
        "The following BIDS apps have "
        f"invalid Docker hub or ghcr.io image.\n{invalid_image}"
    )
