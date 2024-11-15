"""Generate a page for each BEP based on its metadata."""

import ruamel.yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
from rich import print

from bids_website.utils import root_dir

yaml = ruamel.yaml.YAML()
yaml.indent(mapping=2, sequence=4, offset=2)

TEMPLATES_DIR = root_dir() / "templates"

WEBSITE_DATA_DIR = root_dir() / "data"


def return_jinja_env() -> Environment:
    return Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        autoescape=select_autoescape(),
        lstrip_blocks=True,
        trim_blocks=True,
    )


def generate_bep_page(bep: dict) -> str:
    env = return_jinja_env()
    template = env.get_template("bep_page_md.jinja")
    content = template.render(bep=bep)
    output_file = (
        root_dir() / "docs" / "extensions" / "beps" / f"bep_{bep['number']}.md"
    )
    output_file.parent.mkdir(exist_ok=True, parents=True)
    output_file.write_text(content)
    print(f" generated: {output_file}")


BEPS = yaml.load(WEBSITE_DATA_DIR / "beps" / "beps.yml")

for bep in BEPS:
    print(bep["number"])
    assert "google_doc" in bep or "pull_request" in bep
    generate_bep_page(bep)
