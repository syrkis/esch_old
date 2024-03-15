file_base=$(echo $1 | sed 's/\.md//')

pandoc $1 -o $file_base.pdf \
    -V geometry:margin=1in \
    --template=/Users/syrkis/code/esch/templates/resume.tex \
    -V fontsize=12pt \
    -V linestretch=1.5 \
    -V documentclass=letter \
    --pdf-engine=xelatex \
    -V pagestyle=empty

open $file_base.pdf