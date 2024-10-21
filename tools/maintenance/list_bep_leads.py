"""List the emails of the leader of each BEP."""

import pandas as pd
from bids_website.utils import bids_spec_dir, data_dir
from ruamel.yaml import YAML
from utils import load_citation, return_contributor_from_citation_cff

beps = data_dir() / "beps" / "beps.yml"

with open(beps, "r") as f:
    yaml = YAML(typ="safe", pure=True)
    data = yaml.load(f)

citation = load_citation(bids_spec_dir() / "CITATION.cff")

output = {"bep": [], "lead": [], "email": []}

for bep in data:
    for lead in bep["leads"]:
        if not lead["family-names"].strip():
            continue

        contributor = return_contributor_from_citation_cff(citation, lead)
        if contributor is None:
            continue

        if "email" in contributor:
            output["bep"].append(f'{bep["number"]} - {bep["title"]}')
            output["lead"].append(
                f'{lead["given-names"]} {lead["family-names"]}'
            )
            output["email"].append(f'{contributor["email"]}')

df = pd.DataFrame(output)

df.to_csv("bep_leads.tsv", sep="\t", index=False)
