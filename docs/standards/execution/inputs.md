# Input specification

Inputs to BIDS apps may be specified as JSON objects that map input ids to
values. The objects found within the required inputs list have the following
fields, described fully in
[https://github.com/boutiques/boutiques/blob/0.5.25/schema/README.md#inputs](https://github.com/boutiques/boutiques/blob/0.5.25/schema/README.md#inputs)
([source](https://github.com/boutiques/boutiques/blob/0.5.25/tools/python/boutiques/schema/descriptor.schema.json#L247-L448)):

## List of relevant inputs object properties for the BIDS Application specification

| Field name        | Requirement Level | Data type | Description                                                                                                                                                                                                                                                      |
|-------------------|-------------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                | REQUIRED          | String    | The argument ID.  Alphanumeric values and underscores only.  CamelCase is recommended.                                                                                                                                                                           |
| name              | REQUIRED          | String    | Plain text name of input for display.  Can contain spaces.                                                                                                                                                                                                       |
| type              | REQUIRED          | String    | One of {"String", "File", "Flag", "Number"}.                                                                                                                                                                                                                     |
| command-line-flag | OPTIONAL          | String    | For non-positional arguments, the flag which is associated with the argument on the command-line.                                                                                                                                                                |
| list              | OPTIONAL          | Boolean   | Indicates whether or not the input field is a list of inputs.  One of {true, false}.  If omitted, it will be interpreted as false (for example non-list input).                                                                                                  |
| optional          | OPTIONAL          | Boolean   | Indicates whether or not the input field is required.  One of {true, false}.  If omitted, will be interpreted as false (for example non-optional input).                                                                                                         |
| value-choices     | OPTIONAL          | List      | List of possible values that the parameter may take.                                                                                                                                                                                                             |
| value-key         | OPTIONAL          | String    | String to replace in command-line template string.  If specified, this MUST NOT be either a superset or subset of the value-key attribute associated with another object in the descriptor; to ensure this, brackets are typically used (for example "[value]"). |

### List of group object properties and their role within the BIDS Application specification

In addition to describing inputs themselves, groups of inputs and their relationships can be defined as follows:

| Field name         | Requirement Level | Data type | Description                                                                                      |
|--------------------|-------------------|-----------|--------------------------------------------------------------------------------------------------|
| id                 | REQUIRED          | String    | A short, unique, informative identifier containing only alphanumeric characters and underscores. |
| members            | REQUIRED          | List      | IDs of the input parameters belonging to this group.                                             |
| name               | REQUIRED          | String    | A human-readable name for the input group.                                                       |
| description        | RECOMMENDED       | String    | Description of the input group.                                                                  |
| all-or-none        | OPTIONAL          | Boolean   | True if all parameters included in this group need to be included together. .                    |
| mutually-exclusive | OPTIONAL          | Boolean   | True if only one input in the group may be selected at runtime.                                  |
| one-is-required    | OPTIONAL          | Boolean   | True if at least one of the inputs in the group must be selected.                                |

## Required arguments

BIDS Applications MUST provide the following arguments. Notes that "Argument ID"
is what is required to exist as the state "id" in the Boutiques descriptor, and
will be validated, while the example CLI Flag provides a possible way this could
be expressed in the tool's interface.

### List of custom object properties and roles within the BIDS Application specification

| Argument ID    | CLI Flag            | Requirement Level | Data type | Description                                                                                                                                                                                                                                                                            |
|----------------|-------------------- |-------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AnalysisLevel  | `--analysis-level`  | REQUIRED          | String    | String with value-choices which are a subset of {run, session, subject, dataset, meta}.  The app may support one or more of these analysis levels.  A default may be set, and unsupported analysis levels should return an exit code of 17, consistent with the definition in Table 7. |
| Help           | `--help`            | REQUIRED          | Flag      | Flag that specifies whether or not to show the help-text that describes how the tool may be correctly used.                                                                                                                                                                            |
| InputDataset   | `--input-dataset`   | REQUIRED          | List      | List of URIs/paths of the BIDS datasets to be processed.  Whether or not the order of listed datasets is important MUST be specified in the parameter description.  The tool MUST NOT reorder the user-specified list.                                                                 |
| OutputLocation | `--output-location` | REQUIRED          | List      | One URI/path to the location where all outputs will be stored.                                                                                                                                                                                                                         |
| ToolVersion    | `--version`         | REQUIRED          | Flag      | Returns the version of the tool being used.                                                                                                                                                                                                                                            |

## Backwards compatibility

If an app wishes to maintain backwards compatibility with BIDS-Apps 1.0,
then the following command-line should be valid:

```bash
    bids-app InputDataset OutputLocation AnalysisLevel [options]
```

In this case, InputDataset is limited to a list of length one. It is worth
noting that all legacy apps can be supported in this spec, they just need to
write a descriptor which maps the inputs as they are expected and defined, here,
to their associated values in the original application.

## Reserved arguments

The ability to filter BIDS entities (for example subject, session, or run) allows for
the selection of subsets of datasets. To be extensible as new entities are added
to the BIDS specification, the reserved arguments are defined here as a rule
which maps to BIDS entities, rather than specifying the moving goalpost of an
exhaustive list. The arguments may be specified as follows:

-   The argument ID SHOULD be in CamelCase, with the form &lt;entity>Label or
    &lt;entity>Index, depending on whether the associated values are constrained
    to be alphanumeric or numeric, respectively.

-   The argument MUST accept values referring to labels/indices, as consistent
    with the above, in either the form of a list or a file containing a
    line-delimited list. The items provided SHOULD NOT include the entity label in
    addition to the labels/indices.

While several examples exist within Table 5, to the following demonstrates how
the above rules can be applied for the BIDS entity "subject":

ID: `SubjectLabel`

CLI flag: `--subject-label`

Acceptable and equivalent usages:

```bash
    --subject-label 01 02 03
    --subject-label subject_ids.txt
```

Contents of `subject_ids.txt`:

```text
01
02
03
```

In all cases where such arguments are defined and applied, only files in the
BIDS dataset that have a value for the specified entities will be subject to
filtering. That is, if a file does not have a given entity (for example entity value
for it is &lt;None>), the file will be included.

Applications are not required to support these arguments, but MUST NOT assign
these arguments to other meanings. To reduce conflicts, BIDS Applications SHOULD
avoid using this convention except for entities that are anticipated to be
standardized.

Example of an Interface descriptor: see 4.1.

For example, suppose we have an application with the following descriptor:

`example_app.json`:

```json
{
    "name": "Example BIDS App",
    "command-line": "bids-app [InputDataset] [OutputLocation] [AnalysisLevel] [ParticipantLabel] [OurRandomSeed]""inputs": [
        {
            "id": "InputDataset",
            "name": "Input datasets",
            "value-key": "[InputDataset]",
            "type": "File",
            "list": true,
            "optional": false,
            "command-line-flag": "--input-datasets"
        },
        {
            "id": "OutputLocation",
            "name": "Output location",
            "value-key": "[OutputLocation]",
            "type": "File",
            "optional": false,
            "command-line-flag": "--output-location"
        },
        {
            "id": "AnalysisLevel",
            "name": "Analysis level",
            "value-key": "[AnalysisLevel]",
            "type": "String",
            "optional": false,
            "value-choices": [
                "run",
                "session",
                "subject",
                "dataset"
            ],
            "default": "session",
            "command-line-flag": "--analysis-level"
        },
        {
            "id": "SubjectLabel",
            "name": "Subject labels",
            "value-key": "[SubjectLabel]",
            "type": "String",
            "list": true,
            "optional": true,
            "command-line-flag": "--subject-label"
        },
        {
            "id": "RandomSeed",
            "name": "Seed for pseudorandom number generator",
            "value-key": "[RandomSeed]",
            "type": "Number",
            "optional": true,
            "command-line-flag": "--random-seed"
        }
    ]
}
```

`input_params.json`

```json
{
  "InputDataset": ["/path/to/bids", "/path/to/derivatives"],
  "OutputLocation": "/path/to/output",
  "AnalysisLevel": "subject",
  "SubjectLabel": ["01", "02"],
  "RandomSeed": "0xB1D5CAF3"
}
```
