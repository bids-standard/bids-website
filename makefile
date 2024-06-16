all: update

serve: update
	mkdocs serve

update: update_from_spec update_faq update_contributors update_datasets_examples

package.json:
	npm install `cat npm-requirements.txt`

update_from_spec:
	@echo "  ----------------------------------  "
	rm -fr docs/specification
	mkdir -p docs/specification/
	mkdir -p docs/specification/schema
	cp -r specification/src/schema docs/specification/
	cp specification/CODE_OF_CONDUCT.md docs/specification/CODE_OF_CONDUCT.md
	cp specification/CONTRIBUTING.md docs/specification/CONTRIBUTING.md
	cp specification/macros_doc.md docs/specification/macros_doc.md
	cp -r specification/commenting_images docs/specification/

update_faq:
	@echo "  ----------------------------------  "
	cd faq/general && faqtory build
	cd faq/eeg && faqtory build
	cd faq/mri && faqtory build
	cd faq/pheno && faqtory build
	cd faq/bep && faqtory build
	cd faq/apps && faqtory build

update_contributors: package.json
	@echo "  ----------------------------------  "
	python tools/build/transfer_contributors.py
	npx all-contributors generate

update_datasets_examples:
	@echo "  ----------------------------------  "
	python examples/tools/print_dataset_listing.py docs/datasets/index.md

# Linting

lint: remark
	tox

remark: package.json
	npx remark \
		faq \
		./docs/*.md \
		./docs/bep \
		./docs/blog \
		./docs/collaboration \
		./docs/datasets \
		./docs/faq/index.md \
		./docs/getting_started \
		./docs/standards \
		./docs/tools \
		--rc-path .remarkrc
