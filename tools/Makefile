clean:
	rm -f *.html
	rm -f *.md

all: clean
	bash convert_to_md.sh
	python3 convert_to_md.py
	mv *.md ../_posts
