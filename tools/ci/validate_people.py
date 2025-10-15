"""Check
- leads of each BEP
"""

import sys

from bids_website.utils import (
    data_dir,
    load_citation,
    return_contributor_from_citation_cff,
)
from rich import print
from ruamel.yaml import YAML

yaml = YAML(typ="safe", pure=True)

files_to_check = [
    # data_dir() / "beps" / "beps_completed.yml",
    data_dir()
    / "beps"
    / "beps.yml",
]


def main(files_to_check):

    return_code = 0

    citation = load_citation()

    for file in files_to_check:

        print(f"\nchecking: {file}")

        with file.open("r") as f:
            data = yaml.load(f)

        for bep in data:

            has_email = False

            print(f'[blue]{bep["number"]} {bep["title"]}')
            for lead in bep["leads"]:

                status, email = check_lead(citation, lead)

                if status == "not found":
                    color = "red"
                    return_code = 1
                elif status == "skip":
                    color = "yellow"
                elif status == "found":
                    color = "green"

                print(
                    f'    [{color}]{status.upper()} {lead["given-names"]} {lead["family-names"]}'
                )

                if status in ["not found", "skip"]:
                    continue

                if email["in_bids_website"]:
                    return_code = 1
                    print(
                        "      [red]email should be in specification/CITATION.cff not in bids-website data."
                    )

                if email["in_citation_cff"]:
                    has_email = True
                else:
                    color = "yellow" if has_email else "red"
                    print(
                        f"      [{color}]no email in specification/CITATION.cff."
                    )

                if email["conflicting"]:
                    return_code = 1
                    print(
                        "      [red]conflicting emails found:\n",
                        f"      [red]  - '{email["in_citation_cff"]}' in specification/CITATION.cff\n"
                        f"      [red]   - '{email["in_bids_website"]}' bids-website data.",
                    )

            return_code |= not has_email

    sys.exit(return_code)


def check_lead(citation, lead):

    status = "not found"

    email = {
        "in_bids_website": lead.get("email", False),
        "in_citation_cff": False,
        "conflicting": False,
    }

    if not lead["family-names"].strip():
        status = "skip"

    else:
        contributor = return_contributor_from_citation_cff(citation, lead)
        if contributor is not None:
            status = "found"

            email["in_citation_cff"] = contributor.get("email", False)

            if (
                email["in_bids_website"]
                and email["in_citation_cff"]
                and lead["email"] != contributor["email"]
            ):
                email["conflicting"] = True

    return status, email


if __name__ == "__main__":
    main(files_to_check)
