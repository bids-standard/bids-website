from pathlib import Path

import ruamel.yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

yaml = ruamel.yaml.YAML()
yaml.indent(mapping=2, sequence=4, offset=2)

ROOT = Path(__file__).parents[1]

TEMPLATES_DIR = ROOT / "templates"

WEBSITE_DATA_DIR = ROOT / "data"


def return_jinja_env() -> Environment:
    return Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        autoescape=select_autoescape(),
        lstrip_blocks=True,
        trim_blocks=True,
    )


def generate_converter_table(file: str) -> str:
    input_file = WEBSITE_DATA_DIR / file
    content = yaml.load(input_file)
    env = return_jinja_env()
    template = env.get_template("converters_table_md.jinja")
    return template.render(include=content[0])


def generate_tools_table(file: str) -> str:
    input_file = WEBSITE_DATA_DIR / file
    content = yaml.load(input_file)
    env = return_jinja_env()
    template = env.get_template("tools_table_md.jinja")
    return template.render(include=content)


def generate_members_table(file: str) -> str:
    input_file = WEBSITE_DATA_DIR / file
    content = yaml.load(input_file)
    env = return_jinja_env()
    template = env.get_template("members_table_html.jinja")
    return template.render(include=content[0])


def generate_beps_table(file: str, type: str | None = None) -> str:
    input_file = WEBSITE_DATA_DIR / file
    content = yaml.load(input_file)
    env = return_jinja_env()
    template = env.get_template("beps_table_md.jinja")
    return template.render(include=content, type=type)


def generate_grants_table():
    input_file = WEBSITE_DATA_DIR / "grants.yml"
    content = yaml.load(input_file)
    env = return_jinja_env()
    template = env.get_template("grants_table_md.jinja")
    return template.render(include=content, type=type)


def main():
    print(generate_beps_table(file="beps.yml"))


if __name__ == "__main__":
    main()
