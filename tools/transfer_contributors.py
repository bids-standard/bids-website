"""Transfer content of all_contributors from specification to website"""

import json
from pathlib import Path

input_file = (
    Path(__file__).parents[1] / "specification" / ".all-contributorsrc"
)
output_file = Path(__file__).parents[1] / ".all-contributorsrc"

with open(input_file, "r") as f:
    content = json.load(f)
contributors = content["contributors"]

with open(output_file, "r") as f:
    content = json.load(f)
content["contributors"] = contributors
with open(output_file, "w") as f:
    json.dump(content, f, indent="   ")
