all: update

install: .venv node_modules

.venv:
	uv sync --frozen

update: update_from_spec update_contributors update_datasets_examples tmp_figures update_bep_pages

node_modules:
	npm install

update_from_spec:
	@echo "  ----------------------------------  "
	rm -fr docs/specification
	mkdir -p docs/specification/
	cp specification/macros_doc.md docs/extensions/macros_doc.md

update_contributors: .venv node_modules
	@echo "  ----------------------------------  "
	uv run tools/build/transfer_contributors.py
	npm run all-contributors

update_datasets_examples: .venv
	@echo "  ----------------------------------  "
	uv run data/datasets/examples/tools/print_dataset_listing.py docs/datasets/examples.md

update_bep_pages: .venv
	@echo "  ----------------------------------  "
	uv run tools/build/generate_bep_pages.py

# Figures
.PHONY: tmp/affiliations.html tmp/bids_timeline.html tmp/citation_per_year.html tmp/openneuro_data_growth.html

tmp_figures: tmp/affiliations.html tmp/bids_timeline.html tmp/citation_per_year.html tmp/openneuro_data_growth.html

tmp/affiliations.html: .venv
	@echo "  ----------------------------------  "
	uv run tools/build/figure_affiliations.py

tmp/bids_timeline.html: .venv
	@echo "  ----------------------------------  "
	uv run tools/build/figure_bep_gantt.py

tmp/citation_per_year.html: .venv
	@echo "  ----------------------------------  "
	uv run tools/build/figure_citation.py

tmp/openneuro_data_growth.html: .venv
	@echo "  ----------------------------------  "
	uv run tools/build/figure_data_openneuro.py


# Linting

lint: remark
	tox

remark: node_modules
	npm run remark

serve: update
	uv run mkdocs serve -a localhost:8080
