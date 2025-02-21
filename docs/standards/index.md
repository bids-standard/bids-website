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
graph LR;
    subgraph bids-specification-repo["<a href=https://github.com/bids-standard/bids-specification>bids-standard/bids-specification</a>"];
        markdown
        schema -.is interpreted by.-> bidsschematools
    end

    markdown --is interpreted by--> mkdocs
    bidsschematools --provides MACROS for--> mkdocs
    mkdocs --renders HTML--> specification

    schema --is instance of-->bids-schema
    bids-schema -.is implemented by.->deno & bidsschematools
    bids-schema -.is reflected in.-> metaschema.json
    schema.json --is instance of-->bids-schema

    subgraph bids.neuroimaging.io["<a href=https://bids.neuroimaging.io>bids.neuroimaging.io</a>"]
        subgraph bids-specification-website["<a href=https://bids-specification.readthedocs.io>bids-specification.readthedocs.io</a>"];
            specification
            bidsschematools --compiles YAMLs as--> schema.json
        end
        subgraph stats-models["<a href=https://bids-standard.github.io/stats-models/>stats-models standard</a>"]
        end
        subgraph bids-apps["<a href=https://bids-standard.github.io/execution-spec/>bids-apps standard</a>"]
        end
    end

    subgraph "legacy-validator @ v1.15.1";
        regex["filename patterns"] --> Node.js
        Node.js --> web1["<a href=https://bids-standard.github.io/legacy-validator/>web</a>"]
        Node.js --> cli1[cli]
    end
    subgraph "bids-validator ≥ v2.0";
        deno --> web["<a href=https://bids-standard.github.io/bids-validator/>web</a>"]
        deno --> cli
    end
    subgraph "python-validator ≥ v1.14.7"; 
        python 
        python --> library
        python --> cli3[cli]
    end

    bids-schema -.is implemented by.->python

    specification -. is interpreted by .-> regex
    schema.json -.is interpreted by.-> deno
    schema.json --is instance of-->metaschema.json
    bidsschematools --is used by--> python
    
    markdown@{label: "<a href="https://github.com/bids-standard/bids-specification/tree/v1.10.0/src">src/</a><br>markdown", shape: docs}
    schema@{label: "<a href="https://github.com/bids-standard/bids-specification/tree/v1.10.0/src/schema">src/schema/</a><br>YAMLs", shape: docs}
    mkdocs@{label: "<a href="">mkdocs</a>", shape: proc}
    bidsschematools@{label: "<a href="https://github.com/bids-standard/bids-specification/tree/v1.10.0/tools/schemacode">tools/schemacode/</a><br/>bidsschematools", shape: proc}
    schema.json@{label: "<a href="https://bids-specification.readthedocs.io/en/v1.10.0/schema.json">schema.json</a>", shape: doc}
    metaschema.json@{label: "<a href="https://github.com/bids-standard/bids-specification/blob/master/src/metaschema.json">metaschema.json</a><br/>JSON Schema", shape: doc}
    bids-specification-repo@{label: "<a href='xxx'>bids-specification@github</a>"}
    specification@{label: specification html}
    bids-schema@{label: "<a href=https://bids-website.readthedocs.io/en/latest/standards/schema/index.html>BIDS Schema</a>"}
    Node.js@{shape: subproc}
    python@{shape: subproc}
    deno@{shape: subproc}
```