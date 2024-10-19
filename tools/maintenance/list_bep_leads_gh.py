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

beps = data_dir() / "beps" / "beps.yml"

with open(beps, "r") as f:
    data = yaml.load(f)

output = {"bep": [], "lead": [], "email": []}

for bep in data:
    print(f'[blue]{bep["number"]} {bep["title"]}')
    for lead in bep["leads"]:

        skip = False

        status = "[red]NOT FOUND:"

        email_in_bids_wesbite = False
        if "email" in lead:
            email_in_bids_wesbite = True

        email_in_citation_cff = False

        has_github = False

        conflicting_emails = False

        if not lead["family-names"].strip():
            status = "[yellow]SKIP:"
            skip = True

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

                    if "email" in contributor:
                        email_in_citation_cff = True

                    if (
                        email_in_bids_wesbite
                        and email_in_citation_cff
                        and lead["email"] != contributor["email"]
                    ):
                        conflicting_emails = True

                    break

        print(f'    {status} {lead["given-names"]} {lead["family-names"]}')

        if not skip:
            if email_in_bids_wesbite:
                print(
                    "      [red]email should be in specification/CITATION.cff not in bids-wesbite data."
                )

            if not email_in_citation_cff:
                print("      [red]no email in specification/CITATION.cff.")

            if conflicting_emails:
                print(
                    "      [red]conflicting emails found:\n",
                    f"      [red]  - '{contributor['email']}' in specification/CITATION.cff\n"
                    f"      [red]   - '{lead['email']}' bids-wesbite data.",
                )
