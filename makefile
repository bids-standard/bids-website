update_from_spec:
	rm -fr docs/specification
	mkdir -p docs/specification/
	mkdir -p docs/specification/schema
	cp -r specification/src/schema docs/specification/
	cp -r specification/CODE_OF_CONDUCT.md docs/specification/CODE_OF_CONDUCT.md
	cp -r specification/CONTRIBUTING.md docs/specification/CONTRIBUTING.md
	cp -r specification/macros_doc.md docs/specification/macros_doc.md
	cp -r specification/commenting_images docs/specification/