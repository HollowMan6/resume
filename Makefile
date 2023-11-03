# Makefile to build PDF and Markdown cv from YAML.
#
# Brandon Amos <http://bamos.github.io> and
# Ellis Michael <http://ellismichael.com> and
# Songlin Jiang <http://hollowman6.github.io>

WEBSITE_DIR=gh-pages
WEBSITE_PDF=$(WEBSITE_DIR)/CV-Songlin-Jiang.pdf
WEBSITE_MD=$(WEBSITE_DIR)/README.md

TEMPLATES=$(shell find templates -type f)

BUILD_DIR=build
TEX=$(BUILD_DIR)/cv.tex
PDF=$(BUILD_DIR)/cv.pdf
MD=$(BUILD_DIR)/cv.md

ifneq ("$(wildcard cv.hidden.yaml)","")
	YAML_FILES = cv.yaml cv.hidden.yaml
else
	YAML_FILES = cv.yaml
endif

.PHONY: all public viewpdf stage jekyll push clean

all: $(PDF) $(MD)

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

public: $(BUILD_DIR) $(TEMPLATES) $(YAML_FILES) generate.py
	./generate.py cv.yaml

$(TEX) $(MD): $(TEMPLATES) $(YAML_FILES) generate.py publications/*.bib
	./generate.py $(YAML_FILES)

$(PDF): $(TEX)
	# TODO: Hack for biber on OSX.
	rm -rf /var/folders/8p/lzk2wkqj47g5wf8g8lfpsk4w0000gn/T/par-62616d6f73

	latexmk -pdf -cd- -jobname=$(BUILD_DIR)/cv $(BUILD_DIR)/cv
	latexmk -c -cd $(BUILD_DIR)/cv

deps:
	pip3 install -r requirements.txt
	sudo apt install latexmk biber texlive-fonts-extra texlive-latex-extra

viewpdf: $(PDF)
	gnome-open $(PDF)

stage: $(PDF) $(MD)
	cp $(PDF) $(WEBSITE_PDF)
	cp $(MD) $(WEBSITE_MD)

jekyll: stage
	cd $(WEBSITE_DIR) && bundle exec jekyll server

push: stage
	git -C $(WEBSITE_DIR) add $(WEBSITE_PDF) $(WEBSITE_MD)
	git -C $(WEBSITE_DIR) commit -m "Update cv."
	git -C $(WEBSITE_DIR) push

clean:
	rm -rf *.db $(BUILD_DIR)/cv*
