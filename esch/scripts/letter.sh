#!/bin/bash

file_base="$1"
config_json="$2"

# if the markdown header has a date field, save it into letter_date
letter_date=$(echo $config_json | jq -r '.date')
template=$(echo $config_json | jq -r '.template')
bibfile=$(echo $config_json | jq -r '.bibfile')

# Create a temporary file for intermediate processing
tmp_file=$(mktemp).md
sed "/—$/s/$/\\\\hfill $letter_date/" $file_base.md > $tmp_file.md

pandoc $tmp_file.md -o $file_base.pdf \
    -V geometry:margin=1in \
    -V fontsize=12pt \
    -V linestretch=1.5 \
    -V documentclass=letter \
    --bibliography=$bibfile \
    --csl=/Users/syrkis/Zotero/styles/apa.csl \
    --citeproc \
    -V pagestyle=empty

# Cleanup intermediate files and the temporary Markdown file
# rm -f "$tmp_file".{aux,log,nav,out,snm,toc,bcf,blg,run.xml,bbl,tex} "$tmp_file.md" > /dev/null 2>&1
# Open the final PDF file
open "$file_base".pdf
