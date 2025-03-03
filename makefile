all: install update

install:
	pip install -r requirements.txt

update: update_from_spec update_contributors update_datasets_examples tmp_figures update_bep_pages

package.json:
	npm install `cat npm-requirements.txt`

update_from_spec:
	@echo "  ----------------------------------  "
	rm -fr docs/specification
	mkdir -p docs/specification/
	cp specification/macros_doc.md docs/extensions/macros_doc.md

update_contributors: package.json
	@echo "  ----------------------------------  "
	python tools/build/transfer_contributors.py
	npx all-contributors generate

update_datasets_examples:
	@echo "  ----------------------------------  "
	python data/datasets/examples/tools/print_dataset_listing.py docs/datasets/examples.md

update_bep_pages:
	@echo "  ----------------------------------  "
	python tools/build/generate_bep_pages.py

# Figures
.PHONY: tmp/affiliations.html tmp/bids_timeline.html tmp/citation_per_year.html tmp/openneuro_data_growth.html

tmp_figures: tmp/affiliations.html tmp/bids_timeline.html tmp/citation_per_year.html tmp/openneuro_data_growth.html

tmp/affiliations.html:
	@echo "  ----------------------------------  "
	python tools/build/figure_affiliations.py

tmp/bids_timeline.html:
	@echo "  ----------------------------------  "
	python tools/build/figure_bep_gantt.py

tmp/citation_per_year.html:
	@echo "  ----------------------------------  "
	python tools/build/figure_citation.py

tmp/openneuro_data_growth.html:
	@echo "  ----------------------------------  "
	python tools/build/figure_data_openneuro.py


# Linting

lint: remark
	tox

remark: package.json
	npx remark \
		./docs \
		./templates \
		--frail \
		--rc-path .remarkrc


serve: update
	mkdocs serve -a localhost:8080
