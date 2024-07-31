## Can I combine BIDS and neurodata without border (NWB)?

BIDS and [NWB](https://www.nwb.org/) are compatible.

An NWB data file is an allowed format in the iEEG-BIDS data structure.
This means that one subject (AAA) with a session (BBB)
can have a BIDS folder with raw iEEG data in NWB format:

```text
/sub-AAA/ses-BBB/ieeg/sub-AAA_ses-BBB_task-rest_ieeg.nwb
```

The same subject can have another session (CCC) with raw fMRI data in BIDS:

```text
/sub-AAA/ses-CCC/func/sub-AAA_ses-CCC_task-rest_bold.nii.gz
```

## How can I cite BIDS?

See the specification website for the
[main publications](https://bids-specification.readthedocs.io/en/latest/01-introduction.html#citing-bids)
related to BIDS and its extensions.

BIDS references are centralized in a [zotero group](https://www.zotero.org/groups/5111637/bids).

## How do I convert my data to BIDS?

We strongly recommend you pick a BIDS converter to help you convert your data.

A list of converters can be found [on the BIDS website](../tools/converters/index.md)

Also look at [the list of tutorials and information about conversions](../getting_started/tutorials/conversion/index.md).

## How should I organize data for hyperscanning data?

Hyperscanning is simultaneous fMRI with multiple subjects (see this [paper](https://doi.org/10.1006/nimg.2002.1150)).

-   See this [issue](https://github.com/bids-standard/bids-specification/issues/402)
  in the bids specification repository for typical hyperscanning data.

See an example below with fMRI data:

```text
sub-01/
    ses-dyadic1/
        func/
            sub-01_ses-dyadic1_*
sub-02/
    ses-dyadic1/
        func/
            sub-02_ses-dyadic1_*
sub-03/
    ses-dyadic2/
        func/
            sub-03_ses-dyadic2_*
sub-04/
    ses-dyadic2/
        func/
            sub-04_ses-dyadic2_*
```

-   See this [post on neurostars](https://neurostars.org/t/bids-structure-for-longitudinal-dyadic-data/26173)
    for hyperscanning longitunal data.

See an example below with fMRI data:

```text
sub-S001/
    ses-1/
        func/
            sub-S001_ses-1_task-video_acq-dyad001_bold.nii.gz
    ses-2/
sub-S002/
    ses-1/
        func/
            sub-S002_ses-1_task-video_acq-dyad001_bold.nii.gz
    ses-2/
sub-S003/
    ses-1/
        func/
            sub-S003_ses-1_task-video_acq-dyad002_bold.nii.gz
    ses-2/
```

-   See this [thread on the bids discussion forum](https://groups.google.com/g/bids-discussion/c/v660DuzOf3w/m/q-0PLHt5BgAJ)

## How to import Excel files to TSV file?

See [our sections on TSV files](../getting_started/folders_and_files/metadata.md#tsv-files) for more information.

See also this bids tool to import and export a `participants.tsv` file:
[bids-matlab-tools](https://github.com/sccn/bids-matlab-tools/blob/master/bids_spreadsheet2participants.m)

## How to specify the micro sign in MATLAB?

BIDS requires physical units to be specified according to the SI unit symbol and
possibly prefix symbol (for example: mV, μV for milliVolt and microVolt).

The symbol used to indicate `µ` has unicode U+00B5, which is in MATLAB:

```matlab
char(181)
```

or

```matlab
native2unicode(181, 'latin1')
```

## I had to split the testing of one of my participants across 2 days, should I use 2 different session folders to organize the data of that participant?

No. The `session` level in the BIDS folder hierarchy can be used to group data
that go "logically" together: this means that you can put in the same `session` folder
data that were acquired on different days,
but that are "linked" to one another in a way that make sense to how you want to organize your data.

If you want to keep track of what data was acquired when you can use the
[`scans.tsv` files](https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#scans-file).

For some examples, see this
[issue in the bids-starter kit](https://github.com/bids-standard/bids-starter-kit/issues/193).

If you deal with EEG data, you may want to read this
[comment in another issue](https://github.com/bids-standard/bids-starter-kit/issues/265#issuecomment-1082240834)
as well before considering combining recordings acquired on different occasions
within the same `session` folder.

## Is there a machine readable version of the BIDS specification?

Yes. The BIDS specification exist as a schema.
The BIDS schema is a machine readable representation of the BIDS Standard.
It is (by and large) the BIDS Specification, but written in a declarative form.

The BIDS schema is available in two machine readable formats:

-   as a set of [YAML](https://en.wikipedia.org/wiki/YAML) files in the [BIDS specification repository](https://github.com/bids-standard/bids-specification/src/schema)
-   as a [single json file](https://bids-specification.readthedocs.io/en/stable/schema.json)

A light-weight introduction to the schema can be found [here](https://bids-extensions.readthedocs.io/en/latest/schema/).

A full description of the schema can be found on this [website](https://bidsschematools.readthedocs.io/en/latest/?badge=latest)
where you will also find the documentation for the python package
to interact with the schema, [bidsschematools](https://pypi.org/project/bidsschematools/).

## Is your data type not covered in the current BIDS specification?

BIDS extensions proposals [(BEPs)](../extensions/beps.md)
aim to extend the BIDS specification to new data types.
A list of extensions ongoing and completed proposals can be found [here](../extensions/beps.md).

Guidelines for contributing to these extensions or starting your own can be found
in the [BIDS Extension Proposals Guide](../extensions/src/docs/index.md).

If only part of your data is covered under BIDS,
an option to allow additional files
currently not covered in BIDS to pass the validator is
the [.bidsignore](https://github.com/bids-standard/bids-validator/blob/master/bids-validator/README.md) file,
which works just like [.gitignore](https://git-scm.com/docs/gitignore).
It allows you to list all the files (or directories, with wildcards)
that are not BIDS compliant and should be ignored by the validator.
Of course you should still try to adhere to upcoming BEPs
and the general BIDS philosophy for file names and metadata where possible,
but this gives a little extra flexibility.

## What does [this word] mean?

We're building a glossary to de-jargonise some of the terms you need to know to
work with data in BIDS format. Check it out [here](../getting_started/resources/glossary.md).

## What is a `json` file?

You can find more information about `json` (and `tsv`) files in the
[Metadata-file-formats](../getting_started/folders_and_files/metadata.md#json) page.

## What liense should I choose for my dataset?

If you want to know more about what license to choose for your dataset,
see the [turing way](https://the-turing-way.netlify.app/reproducible-research/licensing/licensing-data.html#data-licenses)
page dedicated to this topic.

If you plan to put your dataset on [openneuro](https://openneuro.org/),
you should use a CC0 or a PDDL license as explained in their [FAQ](https://openneuro.org/faq).

<hr>

Generated by [FAQtory](https://github.com/willmcgugan/faqtory)
