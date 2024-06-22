#!/bin/bash

file_base=$1
config_json=$2

template=$(echo $config_json | jq -r '.template')
filters=$(echo $config_json | jq -r '.filters')

# Create a temporary file with mktemp

# inject self promotion
python "$filters/bio.py" "$file_base.md"

# Convert Markdown to TeX
pandoc "$file_base.md" -o "$file_base.tex" \
    -t beamer --dpi=300 \
    --listings \
    --template="$template" \
    --metadata link-citations=true \
    --slide-level=3 \
    --biblatex \
    --lua-filter="$filters/header.lua" \
    --filter pandoc-crossref


# Add allowframebreaks to all frames
python "$filters/frames.py" "$file_base.tex"

# Remove \passthrough commands to allow inline `code`.
python "$filters/passthrough.py" "$file_base.tex"

# Replace 'pdflatex' with 'lualatex' or 'lualatex'
if ! lualatex "$file_base.tex"; then
    echo "lualatex failed"
    exit 1
fi

if ! biber "$file_base"; then
    echo "biber failed"
    exit 1
fi

if ! lualatex "$file_base.tex"; then
    echo "lualatex failed"
    exit 1
fi

if ! lualatex "$file_base.tex"; then
    echo "lualatex failed"
    exit 1
fi

# Cleanup intermediate files
rm -f "$file_base".{aux,log,nav,out,snm,toc,bcf,blg,run.xml,bbl,tex} > /dev/null 2>&1

# Open the final PDF file
open "$file_base".pdf