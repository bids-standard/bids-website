#!/bin/bash

# Convert from .docx to markdown.
# - requires to have pandoc installed
#
# from https://github.com/llbbl/scripts/blob/main/util/convert_all_word_files.sh

YEAR="2021"

# save current working directory to variable
cwd=$(pwd)/inputs/${YEAR}

# find all .docx files in current directory
find $cwd -name "*.docx" -type f -print0 | while IFS= read -r -d $'\0' line; do

    # remove spaces in filename
    ns_filename=$(echo $line | sed 's/ /_/g')

    # get filename from input
    the_filename=$(basename -s .docx $ns_filename)

    # convert word to markdown
    echo "pandoc --from docx --to markdown \"$line\" -o ${YEAR}_$the_filename.md"
    pandoc --from docx --to markdown "$line" -o ${YEAR}_$the_filename.md
    pandoc --from docx --to html "$line" -o ${YEAR}_$the_filename.html
done
