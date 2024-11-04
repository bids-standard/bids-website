from pathlib import Path

import ruamel.yaml
from bidsschematools import render, schema
from jinja2 import Environment, FileSystemLoader, select_autoescape
from rich import print

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


def generate_converter_table(file: str, data_type: str) -> str:
    input_file = WEBSITE_DATA_DIR / "tools" / file
    content = yaml.load(input_file)
    env = return_jinja_env()
    template = env.get_template("converters_table_md.jinja")
    return template.render(include=content, data_type=data_type)


def generate_tools_table(file: str, category=None) -> str:
    input_file = WEBSITE_DATA_DIR / "tools" / file
    content = yaml.load(input_file)
    env = return_jinja_env()
    template = env.get_template("tools_table_md.jinja")
    return template.render(include=content, category=category)


def generate_members_table(file: str) -> str:
    input_file = WEBSITE_DATA_DIR / "people" / file
    content = yaml.load(input_file)
    env = return_jinja_env()
    template = env.get_template("members_table_html.jinja")
    return template.render(include=content[0])


def generate_beps_table(file: str, type: str | None = None) -> str:
    input_file = WEBSITE_DATA_DIR / "beps" / file
    content = yaml.load(input_file)
    env = return_jinja_env()
    template = env.get_template("beps_table_md.jinja")
    return template.render(include=content, type=type)


def generate_working_groups_table(file: str, status: str | None = None) -> str:
    input_file = WEBSITE_DATA_DIR / file
    content = yaml.load(input_file)
    env = return_jinja_env()
    template = env.get_template("working_group_table_md.jinja")
    return template.render(include=content, status=status)


def generate_grants_table():
    input_file = WEBSITE_DATA_DIR / "grants.yml"
    content = yaml.load(input_file)
    env = return_jinja_env()
    template = env.get_template("grants_table_md.jinja")
    return template.render(include=content)


def generate_apps_table():
    input_file = WEBSITE_DATA_DIR / "tools" / "apps.yml"
    content = yaml.load(input_file)
    env = return_jinja_env()
    template = env.get_template("apps_table_md.jinja")
    return template.render(include=content, type=type)


def generate_filename_templates():
    """Create filename templates for all datatypes of all modalities."""

    schema_obj = schema.load_schema()

    modalities = schema_obj.rules.modalities

    to_render = [
        {
            "name": x,
            "description": schema_obj.objects.modalities[x]["description"],
            "datatypes": [
                {
                    "name": dt,
                    "filenames": filename_template_for(schema_obj, dt),
                }
                for dt in modalities[x]["datatypes"]
            ],
        }
        for x in modalities
    ]

    env = return_jinja_env()
    template = env.get_template("filename_templates_md.jinja")
    return template.render(include=to_render)


def filename_template_for(schema_obj, datatype):
    """Create filename templates for a single datatype."""
    filenames = render.make_filename_template(
        dstype="raw",
        schema=schema_obj,
        src_path=Path("https://bids-specification.readthedocs.io/en/latest/"),
        pdf_format=False,
        datatypes=[datatype],
    )
    filenames = filenames.replace(
        "../../..",
        "https://bids-specification.readthedocs.io/en/latest",
    )
    return filenames


def main():
    print(generate_converter_table(file="converters.yml", data_type="MRI"))


if __name__ == "__main__":
    main()
