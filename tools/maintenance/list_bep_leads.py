"""List the emails of the leader of each BEP."""

import pandas as pd
from bids_website.utils import data_dir
from ruamel.yaml import YAML

beps = data_dir() / "beps" / "beps.yml"

with open(beps, "r") as f:
    yaml = YAML(typ="safe", pure=True)
    data = yaml.load(f)

output = {"bep": [], "lead": [], "email": []}

for bep in data:
    for lead in bep["leads"]:
        output["bep"].append(f'{bep["number"]} - {bep["title"]}')
        output["lead"].append(f'{lead["name"]}')
        output["email"].append(f'{lead["email"]}')

df = pd.DataFrame(output)

df.to_csv("bep_leads.tsv", sep="\t", index=False)
