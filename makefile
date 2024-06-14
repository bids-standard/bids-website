update: serve build update_from_spec update_from_examples update_faq remark

serve: build
	mkdocs serve

build: update_from_spec update_from_examples update_faq

update_from_spec:
	rm -fr docs/specification
	mkdir -p docs/specification/
	mkdir -p docs/specification/schema
	cp -r specification/src/schema docs/specification/
	cp specification/CODE_OF_CONDUCT.md docs/specification/CODE_OF_CONDUCT.md
	cp specification/CONTRIBUTING.md docs/specification/CONTRIBUTING.md
	cp specification/macros_doc.md docs/specification/macros_doc.md
	cp -r specification/commenting_images docs/specification/

update_from_examples:
	rm -fr docs/examples
	mkdir -p docs/examples
	cp -r examples/README.md docs/examples/README.md

update_faq:
	cd faq/general && faqtory build
	cd faq/eeg && faqtory build
	cd faq/mri && faqtory build
	cd faq/pheno && faqtory build
	cd faq/bep && faqtory build
	cd faq/apps && faqtory build

remark: package.json
	npx remark faq ./docs/*.md ./docs/blog ./docs/tools ./docs/collaboration ./docs/faq/index.md ./docs/standards --rc-path .remarkrc

package.json:
	npm install `cat npm-requirements.txt`

update_contributors:
	python tools/transfer_contributors.py
	npx all-contributors generate
