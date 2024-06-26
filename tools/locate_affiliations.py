"""List affiliations of authors in citation.cff and locate them.

- read citation.cff
- list affiliations
- locate longitude and latitude of each affiliation
- write to file
"""

from __future__ import annotations

import re

import pandas as pd
import ruamel.yaml
from bids_website.utils import bids_spec_dir, data_dir
from geopy.geocoders import Nominatim
from rich import print

yaml = ruamel.yaml.YAML(typ="rt")

UPDATE = False


def main():
    with open(bids_spec_dir() / "CITATION.cff") as f:
        cff = yaml.load(f)

    affiliations = [
        author["affiliation"]
        for author in cff["authors"]
        if "affiliation" in author
    ]

    columns = ["address", "city", "country", "longitude", "latitude"]
    df = {
        "affiliation": sorted(list(set(affiliations))),
        "address": [],
        "city": [],
        "country": [],
        "longitude": [],
        "latitude": [],
    }

    geolocator = Nominatim(user_agent="my_request")
    for affiliation_ in df["affiliation"]:
        print(f"\nLocating: {affiliation_}")
        location = get_location(geolocator, affiliation_)
        if location is None:
            print(f" could not locate: {affiliation_}")
            for column in columns:
                df[column].append("n/a")
            continue
        print(" address: ", location.address)
        df["city"].append(location.raw["address"].get("city"))
        df["country"].append(location.raw["address"].get("country"))
        df["address"].append(location.address)
        df["longitude"].append(location.longitude)
        df["latitude"].append(location.latitude)

    df = pd.DataFrame(df)

    output_file = data_dir() / "people" / "affiliations.tsv"
    df.to_csv(output_file, index=False, sep="\t")

    output_file = data_dir() / "people" / "affiliations.md"

    with open(output_file, "w") as f:
        f.write(f"- Number of affiliations: {len(affiliations)}\n")

        nb_countries = len(set(df["country"]))
        f.write(f"- Number of countries: {nb_countries}\n")

        nb_without_affiliation = sum(
            "affiliation" not in author for author in cff["authors"]
        )
        f.write(
            f"- Number of contributors without affiliation: {nb_without_affiliation}\n"
        )

        unknown_affiliations = df["address"].isna().sum()
        f.write(f"- Number of unknown affiliations: {unknown_affiliations}\n")


def get_location(geolocator, affiliation):
    location = geolocator.geocode(
        affiliation, language="english", namedetails=True, addressdetails=True
    )
    if location is not None:
        return location

    if "," not in affiliation:
        return None

    # parse country
    country = affiliation.split(",")[-1].strip()

    # parse city and avoid zip code
    if len(affiliation.split(",")) >= 2:
        city = affiliation.split(",")[-2].strip()
    if (
        city
        and len(affiliation.split(",")) >= 3
        and (city.isupper() or re.match("[0-9]", city))
    ):
        city = affiliation.split(",")[-3].strip()

    address = f"{city}, {country}" if country else f"{city}"
    if address:
        print(f" using: {address}")
        location = geolocator.geocode(
            city, language="english", namedetails=True, addressdetails=True
        )
        if location is not None:
            return location

    return None


if __name__ == "__main__":
    main()
