#!/bin/bash

# Ensure an input file is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <input_markdown_file>"
    exit 1
fi

# Configuration
Platenpath="$HOME/code/press"
file_base=$(echo "$1" | sed 's/\.md//')

# Create a temporary file for intermediate processing
tmp_file=$(mktemp)

# Enable autoEqnLabels by modifying the YAML header of the input Markdown
sed '1s/^---$/---\nautoEqnLabels: true/' "$1" > "$tmp_file"

# Convert the modified Markdown to LaTeX with Pandoc
if ! pandoc "$tmp_file" -o "$file_base.tex" --table \
    --template="$Platenpath/templates/paper.tex" \
    --biblatex \
    --slide-level=3 \
    --filter=pandoc-crossref; then
    echo "Pandoc conversion failed"
    exit 1
fi

# Compile the LaTeX file with pdflatex and biber
if ! pdflatex "$file_base.tex"; then
    echo "pdflatex failed"
    exit 1
fi

if ! biber "$file_base"; then
    echo "biber failed"
    exit 1
fi

if ! pdflatex "$file_base.tex"; then
    echo "pdflatex failed"
    exit 1
fi

if ! pdflatex "$file_base.tex"; then
    echo "pdflatex failed"
    exit 1
fi

# Cleanup intermediate files and the temporary Markdown file
rm -f "$file_base".{aux,log,nav,out,snm,toc,bcf,blg,run.xml,bbl} "$tmp_file" > /dev/null 2>&1

# Open the final PDF file
open "$file_base.pdf"
