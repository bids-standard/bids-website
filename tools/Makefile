.PHONY: clean

all: clean build

clean:
	rm -f *.html
	find . -type f -name '*.md' -not -name 'README.md' -delete

build:
	bash convert_to_md.sh
	python3 convert_to_md.py
	mv *.md ../_posts
