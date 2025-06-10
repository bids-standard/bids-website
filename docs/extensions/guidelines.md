# BEP guidelines

Based on the evergrowing set of BEPs and the respective work and efforts conducted to develop them,
the community has identified a set of general guidelines that can be used to guide the corresponding processes.

These guidelines are not part of the [BIDS specification][specification],
but rather are recommended to be followed when developing a BEP.

These guidelines are not set in stone and can be modified as needed. These guidelines are RECOMMENDED.
The goal is to establish a basis of consensus to ease agile approval of BEPs
that propose terms in line with these guidelines.

## Generic guidelines

### Get the community involved

Try to reach out to colleagues working with the type of data you are trying to add support for.
The more people looking at your extension the better it will become through discussions.

### Be consistent with the main specification

The main specification follows some general rules.
For example, see the [rules on participant labels](https://bids-specification.readthedocs.io/en/stable/02-common-principles.html#participant-names-and-other-labels).

Try not to deviate from BIDS conventions in your extension.

### Avoid backward incompatible changes

BIDS is already incorporated in many tools -
proposing a change that will render already released BIDS datasets not BIDS-compliant
will cause a lot of confusion
and will force developers to update their code.
We should strive to avoid such situations.

Having said that, one day we will have to break backwards compatibility.
If you have an idea for a backwards-incompatible change
please add it as an issue to the [BIDS 2.0 GitHub repository](https://github.com/bids-standard/bids-2-devel).

### Use existing and common practices/formats

It’s likely that certain data types are commonly stored in a particular way in your sub-field.
If this is the case try adopting this way
unless it makes your extension too inconsistent with the main specification.
A good example of such adoption is the
[bvec/bval file format](https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/01-magnetic-resonance-imaging-data.html#required-gradient-orientation-information)
for storing diffusion metadata.

### Try to link with other existing standards and ontologies

There are many standardization attempts out there.
When proposing your extension
consider gathering inspiration and directly linking to other standards.
A good example of this is linking metadata fields to corresponding DICOM tags.

### Facilitate atomic changes

See [issue #371](https://github.com/bids-standard/bids-specification/issues/371) for motivation and discussion.
It is recommended to identify perspective entities and metadata fields to be added,
and research if they, or their synonyms, are  already considered in submitted PRs or other BEPs.
If those are new, propose a PR(s) introducing those to the BIDS schema so that:

-   they could be reviewed "independently" of the larger BEP
-   potentially be made aware of in other BEPs

<!-- TODO link to example PR -->

### Limit flexibility, consider tool developers

One of the aims of BIDS is to make reusing data easier.
This means that when proposing an extension you need to put yourself
in the shoes of someone who will receive a BIDS dataset and attempt to analyze it.
Additionally, consider developers that will try to write tools that take BIDS datasets as inputs.
It is worth assessing how much additional code different ways of approaching your extension may cause.

The most common situation where the trade-off between flexibility and ease of
tool building comes up is in choosing file formats.
For example, allowing multiple different file formats to be used to represent the same data type is flexible,
but requires developers to provide support for all of them.
As an example, iEEG-BIDS and EEG-BIDS
surveyed the community <!--TODO find links  -->
to find out about most common formats and selected only a few formats based on usage and their openness.

## Make use of the the BIDS Schema

Working with the BIDS Schema will enable validation of your BEP.
For more information on translating your BEP into the schema,
visit [the schema guide](../standards/schema/index.md) on this site.

### Be consistent with other BEPs

A common dictionary (BIDS keys) is what makes BIDS successful,
it is thus essential to not create many new entities.
Many of the current BEPs have developed useful terms that we recommend here.

#### Existing entities

<!-- TODO autogenerate this table -->
| Entity        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| desc-<label>  | Alphanumeric label, for any use, up to pipelines to determine what are valuable, for example,  Common desc acronyms: lp30: low pass filtered at 30 Hz hp05: high-pass filtered at 0.5 Hz reref: re-references to another electrodemc: motion corrected sm: smoothed pvc: partial volume corrected McPvc: motion and partial volume corrected  Note: concatenation of the above is possible, preferable in the order in which they were applied when applicable: like McPvc, RerefLp30. PascalCase is recommended when concatenating descriptions |
| space-<label> | Name of space file is aligned to (standard or non-standard)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| res-<label>   | Identifier for spatial resolution (details in sidecar)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| den-<label>   | Identifier for mesh density (details in sidecar)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| label-<label> | Label of ROI described by mask file                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| hemi-{L\|R}   | File describes left or right hemibrain                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| seg-<label>   | As per current atlas definition a label the user MAY use to distinguish a different segmentations, like `atlas/atlas-DKT_space-FSaverage.nii` `sub-01/sub-01_space-T1_seg-DKT_dseg.nii` (are there current uses of the `atlas` key that would be broken changing to `seg`?)                                                                                                                                                                                                                                                                      |

#### Proposed entities

| Entity        | BEP(s)                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                   |
|---------------|------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| model-<label> | BEP016, BEP039                                                                           | Name of model generating derivative file                                                                                                                                                                                                                                                                                                                                                                      |
| param-<label> | BEP016, BEP039                                                                           | Name of parameter represented by file                                                                                                                                                                                                                                                                                                                                                                         |
| atlas-<label> | BEP003, BEP038                                                                           | Atlas is defined as per Merrian-Webster, a bound collection of maps (i.e. labeled brain regions) and metadata (tables, or textual matter) like `atlas-x_space-MNI305_ext` or `atlas-DKT_ext`                                                                                                                                                                                                                  |
| group-<label> | BEP039                                                                                   | Name of group combining over subjects                                                                                                                                                                                                                                                                                                                                                                         |
| node-<label>  | No BEP (BEP-002 working implementation)                                                  | Name of processing node generating derivative file                                                                                                                                                                                                                                                                                                                                                            |
| stat-<label>  | BEP016 (contemplated but not currently present in proposal), also useful for atlas BEP38 | The theory was that one could like computing the mean value across all values in a time series, or within a DWI shell, or the like. The particular aggregate statistic may not be an adequate descriptor; you could also need eg. the axis along which the aggregate was applied, which elements were or were not included in the aggregate... So it might be too much complexity to hand to a single entity? |
| meas-<label>  | BEP017,BEP23                                                                             | Description of the quantity described by the file when the suffix is insufficient (eg. binding value, relaxation time)                                                                                                                                                                                                                                                                                        |

### Derivatives BEP and provenance

The objective of BIDS is to promote data sharing,
ensuring that the information is easily accessible and reusable.
For this purpose, it is highly recommended to provide comprehensive provenance information
to ensure transparency and traceability
While full provenance can be used for full reproducibility, it is not a pre-requirement.
A suggested approach to developing the BEP involves envisioning each processing step,
including potential file names and JSON structures.
While this exercise might not precisely depict
the eventual output files and JSON configurations,
it's instrumental in capturing provenance
and identifying what files or information should be retained for optimal reuse in future studies.

!!! Note

    See the [FAQ on provenance](../faq/bids-extensions.md#provenance)

## Common pitfalls

### Relying on merging the extension on a set timeline

We have found it is very difficult to predict how long a BEP
will take to merge into the standard.
One challenge that has occurred in the past is a doctoral student requiring acceptance of their work
as a requirement for graduation.
We do not recommend yoking contributions to the BIDS community
(or any volunteer-led open source community) to strict timelines
to avoid the uncertainty around domain-specific community engagement,
feedback from other BIDS contributors, and responding to reviews.

### Not considering domain- or field-specific guidelines

In many neuroscience fields there have been past developments and efforts to implement standards,
either formally or informally.
If possible, BEPs should embrace these rather than trying to come up with alternative standards.
The BEP should therefore inventorize
and review past and existing work that may be relevant to the BEP.

### Not considering DICOM fields

Many of the modalities we use have an associated standard, like DICOM for instance.
While BIDS is not specifically about data format, a lot of metadata information
are stored in data files and there is rarely a good reason for using a different name
than one from other established standards.
In using DICOM it is reasonable to
[check what DICOM has already developed](https://www.dicomstandard.org/)
and see if there is overlap.
In a similar fashion, when relevant, we recommend having a `sourcedata/` directory in example datasets to include DICOM files.
You can delete the data and keep the header,
removing any [personally identifying information](https://www.datacenters.com/news/everything-you-need-to-know-about-pii-personal-identifiable-information),
also known as PII or "Personal Data"
under the [General Data Protection Regulation (GDPR)](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation).

### Not building up a user community to support the BEP

Merging BEPs only happens following a community review.
It is therefore helpful to get the stakeholders on board early
(that is while writing the BEP) rather than at the review stage.
Diversity in the team contributes to the quality of the extension proposal.
We recommend that the core team has representatives from 3 different labs,
preferably also with a mix of more junior and more senior contributors.
You may also consider requesting explicit support letters from external labs.

### Confusing operational definitions with ontological ones

A common pitfall in BEP development is the attempt to define neuroimaging constructs—such as "participant", "atlas", or "template"—as if writing a comprehensive ontology or reference manual for the field.
While this effort may be intellectually rigorous and well-intentioned, it does not align with the purpose of the BIDS specification.

!!! warning "BIDS is not a general-purpose neuroimaging ontology."

    BIDS is a pragmatic standard for organizing and describing data in a way that maximizes shareability, and supports automated tools, validation, and reproducible workflows.

BEPs should focus on definitions that are strictly necessary to enable BIDS to function. Definitions should be:

- **Operational**: they must serve a specific purpose in the file naming, metadata structure, or schema validation.
- **Internally consistent**: they should align with existing BIDS conventions and avoid redefining core concepts already in use.
- **Minimal and scoped**: they should avoid generalizing beyond what is needed for BIDS to interpret, validate, and process the data.

For example, rather than attempting to define what an experimental "run" means in all of neuroscience, BIDS specifies what qualifies as a `run-<index>` entity.
BEPs should make clear that the definitions they include are specific to BIDS and not intended to settle broader disciplinary debates.

Avoiding ontological overreach helps the community focus on implementation, adoption, and consensus-building, rather than epistemological disagreements that can delay or derail otherwise useful proposals.

## Specific guidelines

If multiple BEPs need coordination, this document (section below)
could be used to formulate guidelines for specific aspects to be followed by multiple BEPs.

### Guidelines for spatial derivatives

Within this section, guidelines for developing BEPs that include spatial derivatives are outlined and motivated.

#### Problem statement

During the work on multiple BEPs that include `spatial derivatives`,
a repeated pattern in generating derivatives within several imaging modalities' workflows was identified where:

1.  A reference map that is used to encode spatial features and parameters is required.
    There is an antecedent of this in `BIDS` with BEP23 ([see below](#BEP-23-PET-Derivatives)).
    In that BEP, the proposed naming takes the pattern `_<suffix>ref` (for example `_boldref`, `_dwiref`...),
    and that solution has been suggested
    as a possibility in [issue #1532](https://github.com/bids-standard/bids-specification/issues/1532) of the specification repository.

1.  We have derived data that are no longer of the same type as the original,
    but for which we would like to keep the notion of the modality from which this was derived
    while also signaling that it is derived (that is `non-raw`).

#### Motivation for guidelines

Many users are not equipped to understand fine distinctions between different classes of derivatives
(for example, those that are produced by a `model fit and` a `direct computation`).

#### Guidelines

A specific suffix *pattern* is used : `_<suffix>map`, where `<suffix>` is a BIDS suffix used in the `raw` data
(for example, `dwi` or `bold`).
For example, the proposed pattern produces the suffices `_dwimap` or `_boldmap`.
BEPs may use this suffix pattern under the conditions specified below
and MUST specify the extension and metadata that are required with the suffix.

1.  The file descriptor does fall under one of the generic derivatives descriptors.

1.  No other descriptor exists in the `BIDS` specification.
    For example, `statmap` cannot be used, because it is already being used, or soon to be,
    for a [different specification](https://bids-standard.github.io/stats-models/walkthrough-1.html#from-run-outputs-to-subject-inputs).

This suffix pattern provides context through the concatenation of a raw data suffix and the word "`map`"
which implies that the file still contains spatially contiguous information
(in contrast to tabular/"tidy" data, with each row representing a brain region, for example).

This pattern is, in principle, generalizable across BEPs and derivatives in general:

1.  A data process might have generated primary parameters that are either `3D (x,y,z)` or `4D (x,y,z,v)`.
    These parameters might be of help for further data analysis or data interpretation,
    and ultimately the data end user.
    Examples include "statistics" such as mean, std, and so on,
    or model derivatives, such as `DTI FA`.

1.  At the same time, the process might have generated secondary parameters.
    These are not strictly necessary for further processing or data interpretation,
    but they can be potentially useful to interpret the outputs of the data process,
    to track history of the processing, for reproducibility and ultimately
    for debugging purposes of the developer/modeler of the code.

#### Examples

##### BEP 23: PET Derivatives

`BEP 23` has introduced Molecular Imaging Maps "`mimap`s" that correspond
to the conventions introduced by `BEP 001 (qMRI)`, such as `T1map`, `T2map`, and so on.

These generally will be distributed as mean/standard-deviation pairs,
for example: `sub-01_stat-mean_desc-5HT_mimap.nii.gz`/`sub-01_stat-std_desc-5HT_mimap.nii.gz`.

##### BEP 12: Functional MRI derivatives

`BEP 12` proposes a collection of summary statistics,
including `mean`, `standard deviation`, `temporal SNR`, `regional homogeneity`, and so on.
Following the example of `BEP 23`, it has adopted the proposal.

-   `<source_entities>_stat-<mean|std|...>_boldmap.nii.gz`
