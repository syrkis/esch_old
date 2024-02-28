#!/bin/bash

# Check for required arguments
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <input_markdown_file>"
    exit 1
fi

# Configuration
Zoteropath="$HOME/text/Zotero"
Presspath="$HOME/code/esch"
input_file="$1"
base_name="${input_file%.md}"

# Create a temporary file with mktemp
temp_md=$(mktemp)


# Convert Markdown to TeX
pandoc "$temp_md" -o "$base_name.tex" \
    -t beamer --dpi=300 \
    --listings \
    --template="$Presspath/templates/magazine.tex" \
    --metadata link-citations=true \
    --slide-level=3 \
    --biblatex \
    --lua-filter="$Presspath/filters/header.lua" \
    --filter pandoc-crossref

# Add allowframebreaks to all frames
python "$Presspath/filters/frames.py" "$base_name.tex"

# Remove \passthrough commands to allow inline `code`.
python "$Presspath/filters/passthrough.py" "$base_name.tex"


if ! pdflatex "$base_name.tex"; then
    echo "pdflatex failed"
    exit 1
fi

if ! biber "$base_name"; then
    echo "biber failed"
    exit 1
fi

if ! pdflatex "$base_name.tex"; then
    echo "pdflatex failed"
    exit 1
fi

if ! pdflatex "$base_name.tex"; then
    echo "pdflatex failed"
    exit 1
fi

# Cleanup intermediate files
rm -f "$base_name".{aux,bbl,bcf,blg,log,nav,out,run.xml,snm,toc,vrb} "$temp_md" > /dev/null 2>&1

# Open the PDF
open "$base_name.pdf"
