"""Guess gender of contributors to BIDS.

Use the bids specification citation.cff file as input.
"""

from __future__ import annotations

import gender_guesser.detector as gender
import ruamel.yaml
from utils import bids_spec_dir

with open(bids_spec_dir() / "CITATION.cff") as f:
    cff = ruamel.yaml.load(f, Loader=ruamel.yaml.RoundTripLoader)

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

print()

for key in results:
    print(f"- {key}: {results[key]}")
