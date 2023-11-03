Forked from [Brandon Amos's CV](https://github.com/bamos/cv).

This repo contains the source for my CV:

+ [generate.py](generate.py) creates a [website](http://hollowman6.github.io/resume)
  and [PDF](http://hollowman6.github.io/resume/cv.pdf)
  from a shared [YAML source](cv.yaml)
  by using Jinja templates.
+ The publications are rendered from a single
  [BibTeX](publications/all.bib) file.
  The abstracts are displayed in the website output
  and the selected publications here are highlighted.
+ The [YAML source](cv.yaml) links to all author websites,
  which will automatically be added to the
  publication lists in the website and PDF.
+ GitHub stars are automatically scraped and cached on disk.


# Building and running
Dependencies are included in `requirements.txt` and can be installed
using `pip` with `pip3 install -r requirements.txt` (Run `make deps`
to install all dependencies on Ubuntu at once).
`make` will call [generate.py](generate.py) and
build the LaTeX documents with `latexmk` and `biber`.
The Makefile can also:

1. Stage to my website with `make stage`,
2. Start a local jekyll server of my website with updated
  documents with `make jekyll`, and
3. Push updated documents to my website with `make push`.

# What to modify
Change the content in `cv.yaml`.
You should also look through the template files to make sure there isn't any
special-case code that needs to be modified.
The `Makefile` can also start a Jekyll server and push the
new documents to another repository with `make jekyll` and `make push`.

## Warnings
1. Strings in `cv.yaml` should be LaTeX (though, the actual LaTeX formatting
   should be in the left in the templates as much as possible).
2. If you do include any new LaTeX commands, make sure that one of the
   `REPLACEMENTS` in `generate.py` converts them properly.
3. The LaTeX templates use modified Jinja delimiters to avoid overlaps with
   normal LaTeX. See `generate.py` for details.
