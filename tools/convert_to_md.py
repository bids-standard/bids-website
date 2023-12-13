"""Converting Steering Group meeting minutes to markdown.

This script does the following:

- rename files to YYYY-MM-DD-Steering-Group-minutes.*
- prettifies the html files
- process the markdown files by:
    - adding the front matter
    - removing the lines that are not relevant
    - using the html version of the tables instead of the markdown version
      because the pandoc version of the markdown tables is not very good
"""
import datetime
from pathlib import Path

from bs4 import BeautifulSoup
from rich import print

MONTH_MAPPING = {"Oct": "October", "Sept": "September"}
INPUT_FOLDER = Path(__file__).parent


def prettify_html(input_folder):
    """Make html prettier."""
    for file in input_folder.glob("*.html"):
        # Read the HTML file
        with open(file, "r") as f:
            html = f.read()
        # Create BeautifulSoup object
        soup = BeautifulSoup(html, "html.parser")
        # Pretty print the HTML
        pretty_html = soup.prettify()
        with open(file, "w") as f:
            f.write(pretty_html)


def rename_files(input_folder):
    """Rename steering group meeting files with the date."""
    print("Renaming files".upper())

    for file in input_folder.glob("*.md"):
        print(f" Processing {file}")

        with open(file, "r") as f:
            text = f.readlines()

        for line in text:
            if "Date" in line:
                line = line.replace("\n", "")

                year = str(file.name).split("_")[0]

                if len(year) > 4:
                    year = str(file.name).split("-")[0]

                month, day = line.split(" ")[2:]

                day = day.replace("th", "").replace("rd", "").replace("nd", "").replace("st", "")

                if month in MONTH_MAPPING:
                    month = MONTH_MAPPING[month]
                mnum = datetime.datetime.strptime(month, "%B").month

                new_name = f"{year}-{mnum:02d}-{int(day):02d}-Steering-Group-minutes.md"

                print(f"  {file} --> {new_name}")
                file.rename(new_name)

                hmtl_file = file.with_suffix(".html")
                if hmtl_file.exists():
                    print(f"  {hmtl_file} --> {Path(new_name).with_suffix('.html')}")
                    hmtl_file.rename(Path(new_name).with_suffix(".html"))

                break


def sanitize_md(input_folder):
    """Clean up the markdown files."""
    for file in input_folder.glob("*.md"):
        if str(file).endswith("README.md"):
            continue

        year = str(file.name).split("-")[0]
        month = str(file.name).split("-")[1]
        day = str(file.name).split("-")[2]

        with open(file, "r") as f:
            text = f.readlines()

        with open(file, "w") as f:
            add_front_matter_and_title(f, year, month, day)

            write_line = False

            for line in text:
                # skip lines that are not relevant
                if any(
                    x in line
                    for x in [
                        "Check your local time",
                        "arewemeetingyet",
                        "stanford.zoom",
                        "Password:",
                        "Time:",
                        "Room:",
                        "Attending:",
                    ]
                ):
                    continue

                # skip lines that are markdown tables
                if any(line.startswith(x) for x in ["|", "+-", "+="]):
                    continue

                if write_line:
                    f.write(line)

                if "Date" in line:
                    write_line = True
                    line = line.replace("\n", "")
                    f.write(f"{line}, {year}\n")
                    f.write("\n<!--more-->\n\n\n")
                    # add the table in html format for better rendering
                    print_table_from_html(file, f)


def add_front_matter_and_title(f, year, month, day):
    """Add the markdown header."""
    f.write(
        f"""---
title: Steering Group minutes
author:
display: true
---

# Steering Group minutes {year}/{month}/{day}

"""
    )


def print_table_from_html(input_file: Path, output_file):
    """Print a table."""
    html_file = input_file.with_suffix(".html")
    if html_file.exists():
        with open(html_file, "r") as f:
            text = f.readlines()
            print_line = False
            for line in text:
                if "<table>" in line:
                    print_line = True
                if "</table>" in line:
                    output_file.write(line)
                    print_line = False
                if print_line:
                    output_file.write(line)


def main():
    rename_files(INPUT_FOLDER)
    prettify_html(INPUT_FOLDER)
    sanitize_md(INPUT_FOLDER)


if __name__ == "__main__":
    main()
