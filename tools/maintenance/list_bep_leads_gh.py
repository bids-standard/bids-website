"""List the emails of the leader of each BEP."""

from bids_website.utils import bids_spec_dir, data_dir
from rich import print
from ruamel.yaml import YAML
from utils import load_citation, return_lead_from_citation_cff

yaml = YAML(typ="safe", pure=True)

files = [
    # data_dir() / "beps" / "beps_completed.yml",
    data_dir()
    / "beps"
    / "beps.yml",
]


def main(files):

    citation = load_citation(bids_spec_dir() / "CITATION.cff")

    for beps in files:

        with beps.open("r") as f:
            data = yaml.load(f)

        for bep in data:
            print(f'[blue]{bep["number"]} {bep["title"]}')
            for lead in bep["leads"]:

                skip = False

                status = "[red]NOT FOUND:"

                email_in_bids_wesbite = False
                if "email" in lead:
                    email_in_bids_wesbite = True

                email_in_citation_cff = False

                conflicting_emails = False

                if not lead["family-names"].strip():
                    status = "[yellow]SKIP:"
                    skip = True

                else:
                    contributor = return_lead_from_citation_cff(citation, lead)
                    if contributor is not None:
                        status = "[green]FOUND:"

                        if "email" in contributor:
                            email_in_citation_cff = True

                        if (
                            email_in_bids_wesbite
                            and email_in_citation_cff
                            and lead["email"] != contributor["email"]
                        ):
                            conflicting_emails = True

                print(
                    f'    {status} {lead["given-names"]} {lead["family-names"]}'
                )

                if not skip:
                    if email_in_bids_wesbite:
                        print(
                            "      [red]email should be in specification/CITATION.cff not in bids-wesbite data."
                        )

                    if not email_in_citation_cff:
                        print(
                            "      [red]no email in specification/CITATION.cff."
                        )

                    if conflicting_emails:
                        print(
                            "      [red]conflicting emails found:\n",
                            f"      [red]  - '{contributor['email']}' in specification/CITATION.cff\n"
                            f"      [red]   - '{lead['email']}' bids-wesbite data.",
                        )


if __name__ == "__main__":
    main(files)
