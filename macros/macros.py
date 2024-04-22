from pathlib import Path

import ruamel.yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

yaml = ruamel.yaml.YAML()
yaml.indent(mapping=2, sequence=4, offset=2)

ROOT = Path(__file__).parents[1]

TEMPLATES_DIR = ROOT / "templates"

WEBSITE_DATA_DIR = ROOT / "data"


def return_jinja_env():
    return Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        autoescape=select_autoescape(),
        lstrip_blocks=True,
        trim_blocks=True,
    )


def generate_converter_table(file):
    input_file = WEBSITE_DATA_DIR / file
    content = yaml.load(input_file)
    env = return_jinja_env()
    template = env.get_template("converters_table_md.jinja")
    return template.render(include=content[0])


def generate_tools_table(file):
    input_file = WEBSITE_DATA_DIR / file
    content = yaml.load(input_file)
    env = return_jinja_env()
    template = env.get_template("tools_table_md.jinja")
    return template.render(include=content)


def generate_members_table(file):
    input_file = WEBSITE_DATA_DIR / file
    content = yaml.load(input_file)
    env = return_jinja_env()
    template = env.get_template("members_table_html.jinja")
    return template.render(include=content[0])


def main():
    print(generate_members_table(file="steering.yml"))


if __name__ == "__main__":
    main()
