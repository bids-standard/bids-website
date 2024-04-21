from pathlib import Path

import ruamel.yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

yaml = ruamel.yaml.YAML()
yaml.indent(mapping=2, sequence=4, offset=2)

ROOT = Path(__file__).parents[1]

TEMPLATES_DIR = ROOT / "templates"

WEBSITE_DATA_DIR = ROOT / "docs" / "website" / "_data"


def generate_converter_table():

    input_file = WEBSITE_DATA_DIR / "converters.yml"

    content = yaml.load(input_file)

    env = Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        autoescape=select_autoescape(),
        lstrip_blocks=True,
        trim_blocks=True,
    )

    template = env.get_template("converters_table.jinja")

    return template.render(include=content[0])


def main():
    generate_converter_table()


if __name__ == "__main__":
    main()
