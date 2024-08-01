"""List the emails of the leader of each BEP."""

from pathlib import Path

import pandas as pd
from bids_website.utils import bids_spec_dir, data_dir
from rich import print
from ruamel.yaml import YAML

yaml = YAML(typ="safe", pure=True)


def load_citation(citation_file: Path) -> dict:
    """Load `CITATION.cff` file."""
    with open(citation_file, "r", encoding="utf8") as input_file:
        return yaml.load(input_file)


citation = load_citation(bids_spec_dir() / "CITATION.cff")
print(citation)

beps = data_dir() / "beps" / "beps.yml"

with open(beps, "r") as f:
    data = yaml.load(f)

output = {"bep": [], "lead": [], "email": []}

for bep in data:
    for lead in bep["leads"]:
        output["bep"].append(f'{bep["number"]} - {bep["title"]}')
        output["lead"].append(f'{lead["name"]}')
        output["email"].append(f'{lead["email"]}')

df = pd.DataFrame(output)

df.to_csv("bep_leads.tsv", sep="\t", index=False)
