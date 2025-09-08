# BIDS Standards

The current set of BIDS Standards provide outlines and guidance
for file naming and organization, statistical modeling of neuroimaging data,
and applications created to be used with BIDS data.
These standards are intended to be updated and evolve as methods and data types change,
but current documentation on BIDS standards can be found in the sections below.

You can find further information for:

-   the [BIDS specification](./bids_specification/index.md)
-   the [BIDS schema](./schema/index.md)
-   the [BIDS statistical model specification](.//bids_stats_model/index.md)
-   the [BIDS apps specification](./bids_app_specification/index.md)

The following figure shows the relationship between the BIDS specification, validator implementations, and the BIDS schema:

```mermaid
---
config:
  layout: dagre
---
flowchart TB
 subgraph s6["<a href=https://github.com/bids-standard/bids-specification>bids-standard/bids-specification</a>"]
        markdown@{ label: "<a href='https://github.com/bids-standard/bids-specification/tree/v1.10.0/src'>src/</a><br>markdown" }
        bidsschematools@{ label: "<a href='https://github.com/bids-standard/bids-specification/tree/v1.10.0/tools/schemacode'>tools/schemacode/</a><br/>bidsschematools" }
        schema@{ label: "<a href='https://github.com/bids-standard/bids-specification/tree/v1.10.0/src/schema'>src/schema/</a><br>YAMLs" }
  end
 subgraph s2["<a href=https://bids-specification.readthedocs.io>bids-specification.readthedocs.io</a>"]
        specification["specification html"]
        schema.json@{ label: "<a href='https://bids-specification.readthedocs.io/en/v1.10.0/schema.json'>schema.json</a>" }
  end
 subgraph s_jsr["<a href=https://jsr.io/@bids/schema>https://jsr.io/@bids/schema</a>"]
        schema.json-jsr["schema.json"]
  end
 subgraph s5["<a href=https://bids.neuroimaging.io>bids.neuroimaging.io</a>"]
        s2
  end
 subgraph subGraph5["legacy-validator @ v1.15.1"]
        Node.js["Node.js"]
        regex["filename patterns"]
        web1@{ label: "<a href=\"https://bids-standard.github.io/legacy-validator/\">web</a>" }
        cli1["cli"]
  end
 subgraph subGraph6["bids-validator ≥ v2.0"]
        web@{ label: "<a href=\"https://bids-standard.github.io/bids-validator/\">web</a>" }
        deno["deno"]
        cli["cli"]
  end
 subgraph subGraph7["python-validator ≥ v1.14.7"]
        python["python"]
        library["library"]
        cli3["cli"]
  end
    schema -. is interpreted by .-> bidsschematools
    markdown -- is interpreted by --> mkdocs@{ label: "<a href=''>mkdocs</a>" }
    bidsschematools -- provides MACROS for --> mkdocs
    mkdocs -- renders HTML --> specification
    schema -- is instance of --> bids-schema@{ label: "<a href=\"https://bids-website.readthedocs.io/en/latest/standards/schema/index.html\">BIDS Schema</a>" }
    bids-schema -. is implemented by .-> deno & bidsschematools & python
    bids-schema -. is reflected in .-> metaschema.json@{ label: "<a href='https://github.com/bids-standard/bids-specification/blob/master/src/metaschema.json'>metaschema.json</a><br/>JSON Schema" }
    schema.json -- is instance of --> bids-schema & metaschema.json
    schema.json-jsr -- is instance of --> bids-schema & metaschema.json
    bidsschematools -- compiles YAMLs as --> schema.json & schema.json-jsr
    regex --> Node.js
    Node.js --> web1 & cli1
    deno --> web & cli
    python --> library & cli3
    specification -. is interpreted by .-> regex
    schema.json-jsr -. is interpreted by .-> deno
    bidsschematools -- is used by --> python
    markdown@{ shape: docs}
    bidsschematools@{ shape: proc}
    schema@{ shape: docs}
    schema.json@{ shape: doc}
    schema.json-jsr@{ shape: doc}
    Node.js@{ shape: subproc}
    web1@{ shape: rect}
    web@{ shape: rect}
    deno@{ shape: subproc}
    python@{ shape: subproc}
    mkdocs@{ shape: proc}
    bids-schema@{ shape: rect}
    metaschema.json@{ shape: doc}
```
