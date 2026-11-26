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

    if app.get("dh"):
        image = app["dh"]
        url = f"https://registry.hub.docker.com/v2/repositories/{image}/"
        valid = requests.get(url, auth=None).status_code == 200
    elif app.get("ghcr"):
        image = f"ghcr.io/{app['ghcr']}"
        valid = ghcr_image_exists(app["ghcr"])
    else:
        print(f"Checked {app['gh']}: no image")
        missing_image.append(app["gh"])
        continue

    print(f"Checked {app['gh']}: {image} {'ok' if valid else 'NOT FOUND'}")
    if not valid:
        invalid_image.append(f"{app['gh']} ({image})")

if missing_image:
    warn(
        "The following BIDS apps are missing "
        f"a Docker hub or ghcr.io image.\n{missing_image}",
        stacklevel=2,
    )

if invalid_image:
    raise ValueError(
        "The following BIDS apps have "
        f"Docker hub or ghcr.io image which was not found.\n{invalid_image}"
    )
