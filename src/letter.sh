# if the markdown header has a date field, save it into letter_date
letter_date=$(sed -n 's/^date: \(.*\)$/\1/p' $1)
file_base=$(echo $1 | sed 's/\.md//')
bibfile="$HOME/code/esch/library.bib"
Zoteropath="$HOME/Zotero"

# If letter_date is empty, use today's date
if [ -z "$letter_date" ]; then
    letter_date=$(date +"%B %e, %Y")
fi

# Replace the pattern and generate tmp.md
sed "/—$/s/$/\\\\hfill $letter_date/" $1 > tmp.md

pandoc tmp.md -o $file_base.pdf \
    -V geometry:margin=1in \
    -V fontsize=12pt \
    -V linestretch=1.5 \
    -V documentclass=letter \
    --bibliography=$bibfile \
    --csl=$Zoteropath/styles/apa.csl \
    --citeproc \
    -V pagestyle=empty

rm tmp.md && open $file_base.pdf