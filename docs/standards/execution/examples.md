# Example BIDS App

This section describes a BIDS Application named bids-app that can only operate
at the participant analysis leveland accepts a numeric seed for a random number
generator.

## Interface descriptor

```json
{
  "name": "Example BIDS App",
  "tool-version": "0.0.1",
  "schema-version": "0.5",
  "custom": {
    "BIDSApplicationVersion": "2.0"
  },
  "command-line": "bids-app [InputDataset] [OutputLocation] [AnalysisLevel] [ParticipantLabel] [RandomSeed]",
  "inputs": [
    {
      "id": "InputDataset",
      "name": "Input datasets",
      "value-key": "[InputDataset]",
      "type": "File",
      "list": true,
      "optional": false,
      "command-line-flag": "--input-dataset"
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
      "optional": true,
      "value-choices": ["participant"],
      "default-value": "participant",
      "command-line-flag": "--analysis-level"
    },
    {
      "id": "SubjectLabel",
      "name": "Participant labels",
      "value-key": "[ParticipantLabel]",
      "type": "String",
      "list": true,
      "optional": true,
      "command-line-flag": "--participant-label"
    },
    {
      "id": "OurRandomSeed",
      "name": "Seed for pseudorandom number generator",
      "description": "Example parameter that may be relevant.",
      "value-key": "[OurRandomSeed]",
      "type": "Number",
      "optional": true,
      "command-line-flag": "--random-seed"
    }
  ]
}
```

## Invocation definition

Two example input definitions follow:

`input_params1.json`

```json
{
  "InputDataset": ["/path/to/bids", "/path/to/derivatives"],
  "OutputLocation": "/path/to/output",
  "AnalysisLevel": "participant",
  "SubjectLabel": ["01", "02"],
  "RandomSeed": 2983578366
}
```

`input_params2.json`

```json
{
  "InputDataset": ["/path/to/bids", "/path/to/derivatives"],
  "OutputLocation": "/path/to/output",
  "AnalysisLevel": "participant"
}
```

### BIDS App compatible example

Before the BIDS Application specification existed there were BIDS Apps.
Attention has been paid to ensure that BIDS Exec apps can be compatible with
existing BIDS Apps.

For example, the term participant was widely used in BIDS Apps, whereas subject
is the preferred term in BIDS. To allow backwards compatibility here you can
use:

```json
{
  "id": "SubjectLabel",
  "name": "Participant labels",
  "value-key": "[ParticipantLabel]",
  "type": "String",
  "list": true,
  "optional": true,
  "command-line-flag": "--participant-label"
}
```
