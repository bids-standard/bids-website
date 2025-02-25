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
    subgraph bids-specification-repo["<a href=https://github.com/bids-standard/bids-specification>bids-standard/bids-specification</a>"]
        markdown@{ label: "<a href='https://github.com/bids-standard/bids-specification/tree/v1.10.0/src'>src/</a><br>markdown" }
        bidsschematools@{ label: "<a href='https://github.com/bids-standard/bids-specification/tree/v1.10.0/tools/schemacode'>tools/schemacode/</a><br/>bidsschematools" }
        schema@{ label: "<a href='https://github.com/bids-standard/bids-specification/tree/v1.10.0/src/schema'>src/schema/</a><br>YAMLs" }
    end
    subgraph s2["<a href=https://bids-specification.readthedocs.io>bids-specification.readthedocs.io</a>"]
        specification["specification html"]
        schema.json@{ label: "<a href='https://bids-specification.readthedocs.io/en/v1.10.0/schema.json'>schema.json</a>" }
    end
    subgraph s3["<a href=https://bids-standard.github.io/stats-models/>stats-models standard</a>"]
    end
    subgraph s4["<a href=https://bids-standard.github.io/execution-spec/>bids-apps standard</a>"]
    end
    subgraph s5["<a href=https://bids.neuroimaging.io>bids.neuroimaging.io</a>"]
        s2
        s3
        s4
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
    schema -- is instance of --> bids-schema["<a href=https://bids-website.readthedocs.io/en/latest/standards/schema/index.html>BIDS Schema</a>"]
    bids-schema -. is implemented by .-> deno & bidsschematools & python
    bids-schema -. is reflected in .-> metaschema.json@{ label: "<a href='https://github.com/bids-standard/bids-specification/blob/master/src/metaschema.json'>metaschema.json</a><br/>JSON Schema" }
    schema.json -- is instance of --> bids-schema & metaschema.json
    bidsschematools -- compiles YAMLs as --> schema.json
    regex --> Node.js
    Node.js --> web1 & cli1
    deno --> web & cli
    python --> library & cli3
    specification -. is interpreted by .-> regex
    schema.json -. is interpreted by .-> deno
    bidsschematools -- is used by --> python

    markdown@{ shape: docs}
    schema@{ shape: docs}
    bidsschematools@{ shape: proc}
    mkdocs@{ shape: proc}
    deno@{ shape: subproc}
    metaschema.json@{ shape: doc}
    schema.json@{ shape: doc}
    Node.js@{ shape: subproc}
    web1@{ shape: rect}
    web@{ shape: rect}
    python@{ shape: subproc}
```
