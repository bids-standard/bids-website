"""Sort and validate converters."""

from pathlib import Path

import ruamel.yaml

yaml = ruamel.yaml.YAML()
yaml.indent(mapping=2, sequence=4, offset=2)

ROOT = Path(__file__).parents[2]

TEMPLATES_DIR = ROOT / "templates"

WEBSITE_DATA_DIR = ROOT / "data"

input_file = WEBSITE_DATA_DIR / "tools" / "converters.yml"

content = yaml.load(input_file)

content.sort(key=lambda x: x["name"])

with input_file.open("w") as f:
    yaml.dump(content, f)
