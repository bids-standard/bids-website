"""List the emails of the leader of each BEP."""

from pathlib import Path

from bids_website.utils import bids_spec_dir, data_dir
from rich import print
from ruamel.yaml import YAML

yaml = YAML(typ="safe", pure=True)


def load_citation(citation_file: Path) -> dict:
    """Load `CITATION.cff` file."""
    with open(citation_file, "r", encoding="utf8") as input_file:
        return yaml.load(input_file)


def find_contributor(content: dict, given_names: str, family_names: str):
    citation


citation = load_citation(bids_spec_dir() / "CITATION.cff")
print(citation)

beps = data_dir() / "beps" / "beps.yml"

with open(beps, "r") as f:
    data = yaml.load(f)

output = {"bep": [], "lead": [], "email": []}

for bep in data:
    print(f'[blue]{bep["number"]} {bep["title"]}')
    for lead in bep["leads"]:
        status = "[red]NOT FOUND:"
        has_email = False
        has_github = False
        if not lead["family-names"].strip():
            status = "[yellow]SKIP:"
        else:
            for contributor in citation["authors"]:
                if (
                    "family-names" not in contributor
                    or "given-names" not in contributor
                ):
                    continue
                if (
                    lead["family-names"] == contributor["family-names"]
                    and lead["given-names"] == contributor["given-names"]
                ):
                    status = "[green]FOUND:"
                    break
        print(f'    {status} {lead["given-names"]} {lead["family-names"]}')
