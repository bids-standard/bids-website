# Objects

The Objects portion of the schema contains the following collection of schema files:

```text
src/schema/objects
├── columns.yaml
├── common_principles.yaml
├── datatypes.yaml
├── entities.yaml
├── extensions.yaml
├── files.yaml
├── formats.yaml
├── metadata.yaml
├── modalities.yaml
└── suffixes.yaml
```

Objects contain selectors, issues and error messages to raise during validation, descriptors, messages, and units.
  Every property needed describe a an entity in BIDS contained within an object's contents. We'll take a closer
  look below at a few specific objects to better introduce the structure that they represent and take on.

## BIDS terms

[`objects.common_principles`](https://github.com/bids-standard/bids-specification/blob/master/src/schema/objects/common_principles.yaml): Terms, such as "data acquisition" or "datatype", used throughout BIDS

??? "data acquisition"

    ```yaml
    data_acquisition:
    display_name: Data acquisition
    description: |
        A continuous uninterrupted block of time during which a brain scanning instrument was acquiring data according to
        particular scanning sequence/protocol.
    ```

??? "data type"

    ```yaml
    data_type:
    display_name: Data type
    description: |
        A functional group of different types of data.
        Data files are contained in a directory named for the data type.
        In raw datasets, the data type directory is nested inside subject and (optionally) session directories.
        BIDS defines the following data types:
            1.  `func` (task based and resting state functional MRI)
            2.  `dwi` (diffusion weighted imaging)
            3.  `fmap` (field inhomogeneity mapping data such as field maps)
            4.  `anat` (structural imaging such as T1, T2, PD, and so on)
            5.  `perf` (perfusion)
            6.  `meg` (magnetoencephalography)
            7.  `eeg` (electroencephalography)
            8.  `ieeg` (intracranial electroencephalography)
            9.  `beh` (behavioral)
            10. `pet` (positron emission tomography)
            11. `micr` (microscopy)
            12. `nirs` (near infrared spectroscopy)
    ```

## Name/value terms

[`objects.entities`](https://github.com/bids-standard/bids-specification/blob/master/src/schema/objects/entities.yaml): Entities (sub-01)

???+ subject

    ```yaml
    subject:
    name: sub
    display_name: Subject
    description: |
        A person or animal participating in the study.
    type: string
    format: label
    ```

[`objects.metadata`](https://github.com/bids-standard/bids-specification/blob/master/src/schema/objects/metadata.yaml): Sidecar fields ("PhaseEncodingDirection": "j")

??? "PhaseEncodingDirection"

    ```yaml
    PhaseEncodingDirection:
    name: PhaseEncodingDirection
    display_name: Phase Encoding Direction
    description: |
        The letters `i`, `j`, `k` correspond to the first, second and third axis of
        the data in the NIFTI file.
        The polarity of the phase encoding is assumed to go from zero index to
        maximum index unless `-` sign is present
        (then the order is reversed - starting from the highest index instead of
        zero).
        `PhaseEncodingDirection` is defined as the direction along which phase is was
        modulated which may result in visible distortions.
        Note that this is not the same as the DICOM term
        `InPlanePhaseEncodingDirection` which can have `ROW` or `COL` values.
    type: string
    enum:
        - i
        - j
        - k
        - i-
        - j-
        - k-
    ```

[`objects.columns`](https://github.com/bids-standard/bids-specification/blob/master/src/schema/objects/columns.yaml): TSV columns ("participant_id", ["sub-01", "sub-02", …])

??? "partcipant_id"

    ```yaml
    participant_id:
    name: participant_id
    display_name: Participant ID
    description: |
        A participant identifier of the form `sub-<label>`,
        matching a participant entity found in the dataset.
    type: string
    pattern: ^sub-[0-9a-zA-Z]+$
    ```

## Value terms

[`objects.datatypes`](https://github.com/bids-standard/bids-specification/blob/master/src/schema/objects/datatypes.yaml) (func)

???+ "func"

    ```yaml
    func:
    value: func
    display_name: Task-Based Magnetic Resonance Imaging
    description: |
        Task (including resting state) imaging data
    ```

[`objects.suffixes`](https://github.com/bids-standard/bids-specification/blob/master/src/schema/objects/suffixes.yaml) (bold)

??? "object.suffixes.bold"

    ```yaml
    bold:
    value: bold
    display_name: Blood-Oxygen-Level Dependent image
    description: |
        Blood-Oxygen-Level Dependent contrast (specialized T2\* weighting)
    ```

[`objects.extensions`](https://github.com/bids-standard/bids-specification/blob/master/src/schema/objects/extensions.yaml) (.nii.gz)

## Formats

[`objects.formats`](https://github.com/bids-standard/bids-specification/blob/master/src/schema/objects/formats.yaml): Types of values objects referenced in the schema can take (label, index, boolean)

???+ "boolean"

    ```yaml
    boolean:
    display_name: Boolean
    description: |
        A boolean.
        Must be either "true" or "false".
    pattern: '(true|false)'
    ```

## Files

[`objects.files`](https://github.com/bids-standard/bids-specification/blob/master/src/schema/objects/files.yaml): One-off files, not constructed from path components, like README

??? "README"

    ```yaml
    README:
    display_name: README
    file_type: regular
    description: |
        A REQUIRED text file, `README`, SHOULD describe the dataset in more detail.
        The `README` file MUST be either in ASCII or UTF-8 encoding and MAY have one of the extensions:
        `.md` ([Markdown](https://www.markdownguide.org/)),
        `.rst` ([reStructuredText](https://docutils.sourceforge.io/rst.html)),
        or `.txt`.
        A BIDS dataset MUST NOT contain more than one `README` file (with or without extension)
        at its root directory.
        BIDS does not make any recommendations with regards to the
        [Markdown flavor](https://www.markdownguide.org/extended-syntax/#lightweight-markup-languages)
        and does not validate the syntax of Markdown and reStructuredText.
        The `README` file SHOULD be structured such that its contents can be easily understood
        even if the used format is not rendered.
        A guideline for creating a good `README` file can be found in the
        [bids-starter-kit](https://github.com/bids-standard/bids-starter-kit/blob/master/templates/README).
    ```
