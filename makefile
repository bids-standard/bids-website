all: update

serve: update
	mkdocs serve

update: update_from_spec update_contributors update_datasets_examples tmp_figures

package.json:
	npm install `cat npm-requirements.txt`

update_from_spec:
	@echo "  ----------------------------------  "
	rm -fr docs/specification
	mkdir -p docs/specification/
	mkdir -p docs/specification/schema
	cp -r specification/src/schema docs/specification/
	cp specification/CODE_OF_CONDUCT.md docs/specification/code_of_conduct.md
	cp specification/CONTRIBUTING.md docs/specification/CONTRIBUTING.md
	cp specification/macros_doc.md docs/specification/macros_doc.md
	cp -r specification/commenting_images docs/specification/

update_contributors: package.json
	@echo "  ----------------------------------  "
	python tools/build/transfer_contributors.py
	npx all-contributors generate

update_datasets_examples:
	@echo "  ----------------------------------  "
	python data/datasets/examples/tools/print_dataset_listing.py docs/datasets/index.md


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
		./docs/*.md \
		./docs/blog \
		./docs/collaboration \
		./docs/contact \
		./docs/datasets \
		./docs/extensions/*md \
		./docs/faq/ \
		./docs/getting_started/*.md \
		./docs/getting_started/bids_apps/**/*.md \
		./docs/getting_started/folders_and_files/**/*.md \
		./docs/getting_started/resources/**/*.md \
		./docs/getting_started/tutorials/**/*.md \
		./docs/impact \
		./docs/standards/bids_app_specification \
		./docs/standards/bids_specification \
		./docs/standards/schema \
		./docs/standards/index.md \
		./docs/tools \
		--frail --rc-path .remarkrc
