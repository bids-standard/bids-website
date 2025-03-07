#!/usr/bin/env python
#
# Detect Latin abbreviations that can be difficult for screenreaders
# and non-native English speakers
#
# This script initially adopted from The Turing Way from in October 2020.
# doi:10.5281/zenodo.3233853
# https://github.com/alan-turing-institute/the-turing-way/blob/af98c94/tests/no-bad-latin.py

import argparse
import fnmatch
import os
import re
from pathlib import Path

from pull_files import filter_files
from rich import print

ABSOLUTE_HERE = Path(__file__).parents[2]
# switch ignore list to unix style glob matching instead of single file name
IGNORE_LIST = ["**/contributors.md"]


def parse_args():
    """Construct command line interface for parsing Pull Request number"""
    DESCRIPTION = """Script to check for latin phrases in Markdown files.

If no pull request number is provided, all relevant text files in the
bids-specification are checked."""

    parser = argparse.ArgumentParser(description=DESCRIPTION)

    parser.add_argument(
        "--pull-request",
        type=str,
        default=None,
        help="If the script is being run on a Pull Request, parse the PR number",
    )

    return parser.parse_args()


def remove_comments(text_string):
    """Function to omit  html comment identifiers in a text string using
    regular expression matches

    Arguments:
        text_string {string} -- The text to be matched

    Returns:
        {string} -- The input text string with html comments removed
    """
    p = re.sub("(?s)<!--(.*?)-->", "", text_string)
    return p


def get_lines(text_string, sub_string):
    """Get individual lines in a text file

    Arguments:
        text_string {string} -- The text string to test
        sub_string {string} -- The conditional string to perform splitting on

    Returns:
        {list} -- A list of split strings
    """
    lines = [line for line in text_string.split("\n") if sub_string in line]
    return lines


def construct_error_message(files_dict):
    """Function to construct an error message pointing out where bad latin
    phrases appear in lines of text

    Arguments:
        files_dict {dictionary} -- Dictionary of failing files containing the
                                   bad latin phrases and offending lines

    Returns:
        {string} -- The error message to be raised
    """
    error_message = ["Bad latin found in the following files:\n"]

    error_message.extend(
        f"{file}:\t{info['latin_type']}\tfound in line\t[{info['line']}]\n"
        for file, info in files_dict.items()
    )

    return "\n".join(error_message)


def read_and_check_files(files):
    """Function to read in files, remove html comments and check for bad latin
    phrases

    Arguments:
        files {list} -- List of filenames to be checked

    Returns:
        {dict} -- Dictionary: Top level keys are absolute filepaths to files
                  that failed the check. Each of these has two keys:
                  'latin_type' containing the unwanted latin phrase, and 'line'
                  containing the offending line.
    """
    failing_files = {}
    bad_latin = [
        " i.e.",
        " i.e ",
        " ie ",
        " e.g.",
        " e.g",
        " e.t.c.",
        " etc",
        " et cetera",
    ]

    for filename in files:
        print(filename)
        if True in [
            fnmatch.fnmatch(filename, pattern) for pattern in IGNORE_LIST
        ]:
            pass
        else:
            try:
                with open(
                    os.path.join(ABSOLUTE_HERE, filename),
                    encoding="utf8",
                    errors="ignore",
                ) as f:
                    text = f.read()
                    text = remove_comments(text)

                    for latin_type in bad_latin:
                        if latin_type in text.lower():
                            lines = get_lines(text.lower(), latin_type)
                            for line in lines:
                                failing_files[os.path.abspath(filename)] = {
                                    "latin_type": latin_type,
                                    "line": line,
                                }
            except FileNotFoundError:
                pass

    print(f"Checked {len(files)} files. {len(failing_files)} with problems.")
    return failing_files


def get_all_files(directory=None):
    """Get a list of files to be checked. Ignores images, javascript, css files.

    Keyword Arguments:
        directory {string} -- The directory containing the files to check

    Returns:
        {list} -- List of files to check
    """
    if directory is None:
        directory = os.path.join(ABSOLUTE_HERE, "docs")
    print(f"Looking for files in {directory}")
    files = []
    for rootdir, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(".md"):
                files.append(os.path.join(rootdir, filename))

    return files


def main():
    """Main function"""
    args = parse_args()

    if args.pull_request is not None:
        files = filter_files(args.pull_request)
    else:
        files = get_all_files()

    failing_files = read_and_check_files(files)

    if bool(failing_files):
        error_message = construct_error_message(failing_files)
        raise Exception(error_message)


if __name__ == "__main__":
    main()
