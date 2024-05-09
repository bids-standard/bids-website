update: update_from_spec update_from_examples

build: update_from_spec update_from_examples update_faq

serve: build
	mkdocs serve

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

package.json:
	npm install `cat npm-requirements.txt`

remark: package.json
	npx remark faq ./docs/*.md ./docs/blog ./docs/tools ./docs/collaboration ./docs/FAQ ./docs/standards --rc-path .remarkrc
