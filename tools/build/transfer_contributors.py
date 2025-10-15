"""Transfer content of all_contributors from specification to website"""

import json
from rich import print

from bids_website.utils import root_dir


def main():

    print(" Transferring all contributors from specification.")

    input_file = root_dir() / "specification" / ".all-contributorsrc"
    output_file = root_dir() / ".all-contributorsrc"

    with open(input_file, "r") as f:
        content = json.load(f)
    contributors = content["contributors"]

    content = {
        "projectName": "bids-website",
        "projectOwner": "bids-standard",
        "repoType": "github",
        "files": ["docs/collaboration/contributors.md"],
        "imageSize": 150,
        "commit": True,
        "commitConvention": "angular",
        "contributors": contributors,
        "contributorsPerLine": 7,
        "linkToUsage": False,
    }

    with open(output_file, "w") as f:
        json.dump(content, f, indent="   ")


if __name__ == "__main__":
    main()
