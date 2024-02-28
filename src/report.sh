file_base=$(echo $1 | sed 's/\.md//')
bibfile="$HOME/code/esch/library.bib"

pandoc $1 -o $file_base.pdf \
    -V documentclass=article \
    -V geometry:margin=1in \
    -V fontsize=12pt \
    -V linestretch=1.2 \
    --bibliography=$bibfile \
    --citeproc

open $file_base.pdf
