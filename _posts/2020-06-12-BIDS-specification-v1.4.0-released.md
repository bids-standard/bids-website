---
title: BIDS-Specification v1.4.0 released!
author: Chris Markiewicz and Franklin Feingold
display: true
---

# BIDS-Specification v1.4.0 released

The BIDS community is proud to announce the release of BIDS v1.4.0. BIDS now supports the  common principles for describing derivative datasets.

Derivatives are the outputs of preprocessing pipelines, capturing data and meta-data sufficient for a researcher to understand and (critically) reuse those outputs in subsequent pipelines.

<!--more-->

Common principles for derivative datasets:

- Derivative datasets describe the contents of the dataset, the methods by which it was generated, and the original dataset(s) that were used to generate it. This metadata is mandatory at the dataset level and optional at the file level.
- Derivative files must be distinguishable from raw files. A generic description (desc-) entity allows this if no other entity applies.
- The spatial interpretation of data, if applicable, can be specified with a space entity and SpatialReference metadata.

An initial set of imaging derivatives - binary masks and discrete or probabilistic segmentations - are also specified in this initial offering.

We had a long journey to get to here...

The need to specify BIDS Derivatives was identified during the early stages of BIDS specification, and a BIDS Extension Proposal (BEP) was started in February 2016, prior to the release of BIDS 1.0 in June 2016.

Development of the proposal was largely based on the experience of developing BIDS Apps. As multiple applications produced similar or equivalent derivatives, common naming schemes were added to the proposal to facilitate reuse of the derivatives. For example, the Configurable Pipeline for the Analysis of Connectomes (C-PAC) and fMRIPrep took similar inputs and had a broad overlap in their outputs, and so made sense to coordinate.

An August 2017 meeting at Stanford led to an agreement to divide the increasingly large BEP into a series of BEPs, most focused on particular modalities or use cases.

In July 2018, [a survey](http://reproducibility.stanford.edu/bids-processed-data-survey-results/){:target="_blank"} of the neuroimaging community was taken to establish priorities (essential, desirable or inessential) for structural, functional and diffusion MRI derivatives. The results of the survey were posted in advance of an [August 2018 workshop](http://reproducibility.stanford.edu/bids-processed-meeting-summary/){:target="_blank"} of 31 participants, where sub-proposals were pushed toward completion and common principles were established. In December 2018, [Release Candidate 1](https://docs.google.com/document/d/17ebopupQxuRwp7U7TFvS6BH03ALJOgGHufxK8ToAvyI/edit#){:target="_blank"} was published, including all imaging modalities, for implementation and feedback.

In July 2019, a [“Common Derivatives” proposal](https://github.com/bids-standard/bids-specification/pull/265){:target="_blank"} was re-introduced establishing more general principles, to be followed by subsequent modality-specific and non-imaging proposals. Common Derivatives entered final review in May 2020 and were released as part of BIDS 1.4.0 in June 2020.

Releasing the common principles for derivative datasets will enable further progress into our modality specific derivative initiatives such as, [electopsychological](https://github.com/bids-standard/bep021){:target="_blank"}, PET, and [diffusion MRI](https://github.com/bids-standard/bids-bep016){:target="_blank"}. Our immediate attention will shift to focus on specifying anatomical and functional derivatives (Look out for the pull requests soon!). [BEP 028 (provenance)](https://github.com/bids-standard/bids-specification/pull/487){:target="_blank"} is a closely related effort that we hope to see progress quickly as well!

We would like to thank our incredible community of contributors and members that helped push this extension over the finish line!
