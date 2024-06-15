# add filename templates to the docs/getting_started/files.md
from pathlib import Path

from bidsschematools import render, schema
from rich import print

from bids_website.utils import root_dir


datatypes = [
    "anat",
    "func",
    "dwi",
    "fmap",
    "perf",
    "beh",
    "eeg",
    "ieeg",
    "meg",
    "pet",
    "nirs",
    "motion",
]


def main():

    input_file = (
        root_dir()
        / "docs"
        / "getting_started"
        / "folders_and_files"
        / "files.md"
    )

    print(f"add filename templates to {input_file}")

    schema_obj = schema.load_schema()

    with open(input_file, "r") as f:
        lines = f.readlines()

    with open(input_file, "w") as f:
        writing_template = False
        for line in lines:
            if line.startswith("<!-- "):
                for datatype_ in datatypes:
                    if line.startswith(
                        f"<!-- {datatype_.upper()} TEMPLATE STARTS"
                    ):
                        writing_template = True
                        f.write(line)
                        codeblock = render.make_filename_template(
                            dstype="raw",
                            schema=schema_obj,
                            src_path=Path(
                                "https://bids-specification.readthedocs.io/en/latest/"
                            ),
                            pdf_format=False,
                            datatypes=[datatype_],
                        )
                        codeblock = codeblock.replace(
                            "../../..",
                            "https://bids-specification.readthedocs.io/en/latest",
                        )
                        f.write(codeblock)
                    if line.startswith(
                        f"<!-- {datatype_.upper()} TEMPLATE ENDS"
                    ):
                        f.write(line)
                        writing_template = False

            else:
                if not writing_template:
                    f.write(line)


if __name__ == "__main__":
    main()
