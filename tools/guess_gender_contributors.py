"""Guess gender of contributors to BIDS.

Use the bids specification citation.cff file as input.
"""

from __future__ import annotations

import gender_guesser.detector as gender
import ruamel.yaml
from bids_website.utils import bids_spec_dir, data_dir

yaml = ruamel.yaml.YAML(typ="rt")


def main():

    with (bids_spec_dir() / "CITATION.cff").open() as f:
        cff = yaml.load(f)

    results = {
        "male": 0,
        "female": 0,
        "andy": 0,
        "unknown": 0,
        "mostly_male": 0,
        "mostly_female": 0,
    }

    d = gender.Detector()
    for author in cff["authors"]:
        guess = d.get_gender(author["given-names"])
        print(f"{author['given-names']}: {guess}")
        results[guess] += 1

    output_file = data_dir() / "people" / "gender.md"

    with output_file.open("w") as f:
        f.writelines(f"- {key}: {results[key]}\n" for key in results)


if __name__ == "__main__":
    main()
