file_base=$(echo $1 | sed 's/\.md//')
Presspath="$HOME/code/press"

pandoc $1 -o $file_base.pdf \
    --template="$Presspath/templates/daily.tex" \
    -V pagestyle:empty

open $file_base.pdf
