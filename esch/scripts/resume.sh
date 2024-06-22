#!/bin/bash
file_base=$1
config_json=$2

template=$(echo $config_json | jq -r '.template')
echo $template
echo $file_base

pandoc $file_base.md -o $file_base.pdf \
    -V geometry:margin=1in \
    --template=$template \
    -V fontsize=12pt \
    -V linestretch=1.5 \
    -V documentclass=letter \
    --pdf-engine=xelatex \
    -V pagestyle=empty

open $file_base.pdf