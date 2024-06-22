bibfile="$HOME/code/esch/library.bib"

pandoc $1 -o $1.pdf \
    -V documentclass=article \
    -V geometry:margin=1in \
    -V fontsize=12pt \
    -V linestretch=1.5 \
    --bibliography=$bibfile \
    --citeproc

open $1.pdf
