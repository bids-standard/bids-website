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
