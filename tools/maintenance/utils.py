"""List the emails of the leader of each BEP."""

from pathlib import Path

from ruamel.yaml import YAML

yaml = YAML(typ="safe", pure=True)


def load_citation(citation_file: Path) -> dict:
    """Load `CITATION.cff` file."""
    with citation_file.open("r", encoding="utf8") as input_file:
        return yaml.load(input_file)


def return_lead_from_citation_cff(citation, lead):
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
            return contributor
    return None
