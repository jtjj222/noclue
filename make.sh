#!/bin/bash

# Install pandoc in order for this script to run
# It will generate both the html and pdf versions of this book

# Destroy and prepare the output folder
rm -rf ./output
mkdir output

cp -r ./images ./output/images
cp -r ./stylesheets ./output/stylesheets
cp -r ./js ./output/js
cp -r ./examples ./output/examples

# TODO - Run any code examples and generate their outputs

# Generate the html document

# Generate an html table of contents for this book
printf "<ul>\n" > output/toc.html

for f in index.md chapters/*.md;
do
    # Get the name of this document, without chapters/ or .md
    root=`basename $f .md`
    # Generate an html table of contents for this chapter
    # Use tail and head to strip the first and last lines (<ul> and </ul>) so we can do that ourselves
    # Use sed to replace the links with the current document
    pandoc --toc --toc-depth=1 --template toc_template.html $f \
        | tail -n +2 \
        | head -n -1 \
        | sed -E 's/"#(.*)"/"'"$root"'.html"/' >> output/toc.html
done

printf "</ul>" >> output/toc.html

# Generate an html document for each markdown document in chapters/
# and also index.md (which becomes index.html)
# Replace the string $toc$ with our custom toc from above

for f in chapters/*.md index.md;
do
    # Get the name of this document, without chapters/ or .md
    root=`basename $f .md`
    # Output a standalone document, inserting toc
    pandoc -s -S --template html_template.html --no-highlight -c stylesheets/html.css $f | perl -pe 's/\$toc\$/`cat output\/toc.html`/ge' > output/$root.html
done

# Clean up
rm output/toc.html

