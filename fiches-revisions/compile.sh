# Compile cheat sheets to PDF with pandoc
for f in *.md; do
    pandoc -f markdown -t pdf --mathjax --table-of-contents -o "${f%.md}.pdf" --listings -H ./listings-setup.tex --pdf-engine=xelatex "$f"
done

echo "Done."