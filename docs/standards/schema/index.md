## What is the Schema?

The BIDS schema is a machine readable representation of the BIDS Standard
written in [YAML](https://en.wikipedia.org/wiki/YAML).
It is (by and large) the BIDS Specification, but written in a declarative form.
For a full accounting of all methods, operators, and options provided to the user
by the Schema we encourage you to look at the developer documentation
contained within the source code here on [GitHub][schema_readme.md].

The schema is split into three major divisions:

-   `objects` - Contains definitions of BIDS concepts and entities

-   `rules` - Rules for validation of file path names, file/directory contents
    (including sidecar and other metadata)

-   `meta` - Contains rules and definitions for the schema itself as well as defining
    a "context" object to which rules can be applied.

The schema is organized in the file structure in the tree seen below:

```text
src/schema
├── BIDS_VERSION
├── meta
│   └── context.yaml
├── objects
│   ├── columns.yaml
│   ├── ...
│   └── suffixes.yaml
├── rules
│   ├── checks
│   │   ├── asl.yaml
│   │   ├── ...
│   │   └── mri.yaml
│   ├── ...
│   └── suffixes.yaml
└── SCHEMA_VERSION
```

## Where is the Schema?

The schema source code lives within the [BIDS Specification][schema_source];
a deferenced JSON'ified version can be found at the following url ->
[bids-specification.readthedocs.io/en/stable/schema.json][jsonified_schema].

## Schema documentation

A full description of the schema can be found in the [documentation][bidsschematools_rtd]
for [bidsschematools][bidsschematools_pypi], the Python package developed to interact
with the schema that is bundled with the specification.

## History of the Schema

If you're just returning to BIDS, creating a new BEP, or simply curious as to the timeline and history
of the transition from markdown to a yaml schema to render and use the BIDS Specification
you are encouraged to browse the links below:

The schema began as a [pull request][start_of_schema] to convert an entity table
into a machine readable format and then began to grow in scope.
Additional work towards the schematization of the specification
has proceeded steadily (and in sometimes in bursts during Schema Sprints
<sup>[1][bids sprint 1 discussion], [2][bids sprint 2 discussion], [3][bids sprint 3 discussion]</sup>) since.

## Motivations and Goals

-   Machine readablity ensures interoperability with other tools and utilities

-   Uniform implementation between tools that use BIDS.
    Previously, other tools relied on their own data structures implemented from an interpretation of the specification.

-   Easier maintenance of the specification, tools, and other applications
    <sup>[1][start_of_schema], [5][bids_schema_validation_for_datatypes]</sup>

-   Improve the process of writing BEPs

## Extending the Schema and Validator

Past BIDS Extension Proposals (BEPs) have required extending the specification itself as well as the BIDS Validator.
After rendering the BEP into markdown it was incumbent on the BEP leads or maintainers
to then update the Validator with rules and logic to handle the new BEP.
This double entry is a byproduct of the fact that the Validator was built in javascript
to run both locally and from within the browser to validate BIDS data.

Efforts have been made to eliminate needing to implement a BEP in both a mark-up language
and in javascript to satisfy the Validator.
These two steps can be reduced into one
by using the machine readable schema; one single input is then used for the specification, the Validator,
or any other software or tool that interacts with BIDS.
A change now made to a BEP, the spec in general, is now a change made and updated within the validator

<!-- [state_of_the_schema_presentation]: https://docs.google.com/presentation/d/1ldEbElaFm__jtkLoEcn2PQ-LGj1dfmdjWxDvE11eiNk/edit?usp=sharing -->
[start_of_schema]: https://github.com/bids-standard/bids-specification/issues/466
[bids_schema_validation_for_datatypes]: https://github.com/bids-standard/bids-validator/pull/1325

[bids sprint 1 discussion]: https://bit.ly/pdx-bids-sprint
[bids sprint 2 discussion]: https://docs.google.com/document/d/1UmcNlv5Ly9Ko6UStJBPV4UGVARjdNtZWRx9OVTLsE7Q/edit?usp=sharing
[bids sprint 3 discussion]: https://docs.google.com/presentation/d/1j7kWyRpk3VPY7r4tsEzuAQ-jmn83iZkmXYtdriCJptg/edit?usp=sharing

[jsonified_schema]: https://bids-specification.readthedocs.io/en/stable/schema.json
[schema_readme.md]: https://github.com/bids-standard/bids-specification/blob/master/src/schema/README.md
[schema_source]: https://github.com/bids-standard/bids-specification/src/schema
[bidsschematools_pypi]: https://pypi.org/project/bidsschematools/
[bidsschematools_rtd]: https://bidsschematools.readthedocs.io/en/latest/?badge=latest
