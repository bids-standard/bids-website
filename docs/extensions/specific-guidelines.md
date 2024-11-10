Based on the evergrowing set of `BEP`s and the respective work and efforts conducted to develop them,
the community has identified a set of general guidelines that can be used to guide the corresponding processes.
These guidelines are not part of the [BIDS specification](https://bids-specification.readthedocs.io/en/stable/index.html),
but rather are recommended to be followed when developing a `BEP`.

These guidelines are not set in stone and can be modified as needed.

These guidelines are RECOMMENDED.

The goal is to establish a basis of consensus to ease agile approval of `BEP`s
that propose terms in line with these guidelines.

## Facilitate atomic changes

See [issue #371](https://github.com/bids-standard/bids-specification/issues/371) for motivation and discussion.
It is recommended to identify perspective entities and metadata fields to be added,
and research if they, or their synonyms, are  already considered in submitted PRs or other BEPs.
If those are new, propose a PR(s) introducing those to the BIDS schema so that:

-   they could be reviewed "independently" of the larger BEP
-   potentially be made aware of in other BEPs

## Formulate "BEP specific guidelines"

If multiple BEPs need coordination, this document (section below)
could be used to formulate guidelines for specific aspects to be followed by multiple BEPs.

## Guidelines for spatial derivatives

Within this section, guidelines for developing `BEP`s that include spatial derivatives are outlined and motivated.

### Problem statement

During the work on multiple `BEP`s that include `spatial derivatives`,
a repeated pattern in generating derivatives within several imaging modalities' workflows was identified where:

1.  A reference map that is used to encode spatial features and parameters is required.
    There is an antecedent of this in `BIDS` with BEP23 ([see below](#BEP-23-PET-Derivatives)).
    In that `BEP`, the proposed naming takes the pattern `_<suffix>ref` (for example `_boldref`, `_dwiref`...), and that solution has been suggested as a possibility in [issue #1532](https://github.com/bids-standard/bids-specification/issues/1532) of the specification repository.

1.  We have derived data that are no longer of the same type as the original,
    but for which we would like to keep the notion of the modality from which this was derived
    while also signaling that it is derived (that is `non-raw`).

### Motivation for guidelines

Many users are not equipped to understand fine distinctions between different classes of derivatives
(for example, those that are produced by a `model fit and` a `direct computation`).

### Guidelines

A specific suffix *pattern* is used : `_<suffix>map`, where `<suffix>` is a BIDS suffix used in the `raw` data
(for example, `dwi` or `bold`).
For example, the proposed pattern produces the suffices `_dwimap` or `_boldmap`.
`BEP`s may use this suffix pattern under the conditions specified below
and MUST specify the extension and metadata that are required with the suffix.

1.  The file descriptor does fall under one of the generic derivatives descriptors.

1.  No other descriptor exists in the `BIDS` specification.
    For example, `statmap` cannot be used, because it is already being used, or soon to be,
    for a [different specification](https://bids-standard.github.io/stats-models/walkthrough-1.html#from-run-outputs-to-subject-inputs).

This suffix pattern provides context through the concatenation of a raw data suffix and the word "`map`"
which implies that the file still contains spatially contiguous information
(in contrast to tabular/"tidy" data, with each row representing a brain region, for example).

This pattern is, in principle, generalizable across `BEP`s and derivatives in general:

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

### Examples

#### BEP 23: PET Derivatives

`BEP 23` has introduced Molecular Imaging Maps "`mimap`s" that correspond
to the conventions introduced by `BEP 001 (qMRI)`, such as `T1map`, `T2map`, and so on.

These generally will be distributed as mean/standard-deviation pairs,
for example: `sub-01_stat-mean_desc-5HT_mimap.nii.gz`/`sub-01_stat-std_desc-5HT_mimap.nii.gz`.

#### BEP 12: Functional MRI derivatives

`BEP 12` proposes a collection of summary statistics,
including `mean`, `standard deviation`, `temporal SNR`, `regional homogeneity`, and so on.
Following the example of `BEP 23`, it has adopted the proposal.

-   `<source_entities>_stat-<mean|std|...>_boldmap.nii.gz`
