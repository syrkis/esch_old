#!/bin/bash

# Configuration
file_base=$1
config_json=$2

# Create a temporary file for intermediate processing
template=$(echo $config_json | jq -r '.template')

# Enable autoEqnLabels by modifying the YAML header of the input Markdown
tmp_file=$(mktemp).md
ls
echo "Creating temporary file $tmp_file"
sed '1s/^---$/---\nautoEqnLabels: true/' "$file_base".md > "$tmp_file"


# Convert the modified Markdown to LaTeX with Pandoc
pandoc "$tmp_file" -o "$file_base.tex" --table \
    --template="$template" \
    --biblatex \
    --slide-level=3 \
    --filter=pandoc-crossref

# Compile the LaTeX file with pdflatex and biber
pdflatex "$file_base.tex"
biber "$file_base"
pdflatex "$file_base.tex"
pdflatex "$file_base.tex"

# Cleanup intermediate files and the temporary Markdown file
rm -f "$file_base".{aux,log,nav,out,snm,toc,bcf,blg,run.xml,bbl,tex} "$tmp_file" > /dev/null 2>&1

# Open the final PDF file
open "$file_base".pdf