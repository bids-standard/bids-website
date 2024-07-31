The structure of the BIDS schema as seen from a top-level file view:

```text
schema
├── BIDS_VERSION
├── SCHEMA_VERSION
├── meta
│   ├── context.yaml
│   └── expression_tests.yaml
├── objects
│   ├── columns.yaml
│   ├── ...
│   └── suffixes.yaml
└── rules
    ├── checks
    ├── ...
    └── tabular_data
```

The BIDS Schema can be be divided into three major components:

1.  [Objects](https://github.com/bids-standard/bids-specification/blob/master/src/schema/objects) (`objects.*`)
    -   Definitions of BIDS concepts

    -   Source of definitions rendered in the specification,
        for example in the [glossary](https://bids-specification.readthedocs.io/en/stable/glossary.html)

1.  [Rules](https://github.com/bids-standard/bids-specification/tree/master/src/schema/rules) (`rules.*`)
    -   Validation rules for entity ordering, sidecar values, and both common and modality specific rules
    -   Source of filename templates and tables describing sidecar fields and TSV Columns

1.  [Meta](https://github.com/bids-standard/bids-specification/tree/master/src/schema/meta) (`meta.*`)
    -   Defines a "context" object to which rules can be applied
    -   Expandable to definitions, tests, or rules related to the schema itself

!!! note

    object dot notation like `rules.checks.*` is used when referencing parts of the schema throughout this document.
    Bracket notation such as `objects['columns'][*]` is equally valid, but more difficult to read._

    The character: `*`, represents a [glob](https://man7.org/linux/man-pages/man7/glob.7.html)
    and is used to denote matching any string/object_.

Examples of [Objects](schema_meta.md), [Rules](schema_rules.md), and [Meta](schema_meta.md) are detailed in the aforementioned linked sections.

Examples are hyperlinked to parts of the schema (source code) where applicable, simply click on the blue
links to reach those parts of the schema.

Specific examples from the schema can be expanded or hidden by clicking on blue _boxes_ to show or hide them.

???+ "show or hide this example"

    ```yaml
    this_example:
        - list item 1
        - list item 2
    ```
