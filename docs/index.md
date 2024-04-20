---
hide:
  - navigation
---

# About BIDS

Neuroimaging experiments result in complex data that can be arranged in many different ways.
For a long time, there was no consensus how to organize and share data obtained in neuroimaging experiments.
Even two researchers working in the same lab could opt to arrange their data in a different way.
Lack of consensus (or a standard) leads to misunderstandings and time wasted on rearranging data or rewriting scripts expecting certain structure.
With the Brain  Imaging Data Structure (BIDS), we describe a simple and easy to adopt way of organizing neuroimaging and behavioral data.

![BIDS-folder-organization](./assets/img/dicom-reorganization-transparent-white_1000x477.png)

BIDS was heavily inspired by the format used internally by the OpenfMRI repository that is now known as [OpenNeuro](https://openneuro.org).
While working on BIDS we consulted many neuroscientists to make sure it covers most common experiments, but at the same time is intuitive and easy to adopt.
The specification is intentionally based on simple file formats and folder structures to reflect current lab practices and make it accessible to a wide range of scientists coming from different backgrounds.

## BIDS is a community effort

BIDS is developed by the community for the community and everybody can [become a part of the community](https://bids.neuroimaging.io/get_involved.html).

## Specification vs. Ecosystem

Since the inception of the BIDS specification that documents how to organize neuroimaging data, a large ecosystem of tools and resources has evolved around BIDS.

A few of the key elements of this ecosystem are the [BIDS specification](http://bids-specification.readthedocs.io/) with the nitty-gritty details, the [BIDS starter kit](https://bids-standard.github.io/bids-starter-kit/) with a simple explanation how to work with it, the [BIDS validator](https://github.com/bids-standard/bids-validator) to automatically check datasets for adherence to the specification, [BIDS Apps](https://doi.org/10.1371/journal.pcbi.1005209), a collection of portable neuroimaging pipelines that understand BIDS datasets, and [OpenNeuro](https://openneuro.org/), as a database for BIDS formatted datasets.

A non-exhaustive list of further tools can be found in the [Benefits](https://bids.neuroimaging.io/benefits.html) section.

With the ongoing development of new tools and resources it is important to keep in mind that the [BIDS specification](http://bids-specification.readthedocs.io/) remains the standard according to which the entire ecosystem must adhere.

## Further Information

- Good introductions to the BIDS standard can be found in the initial [paper published in Nature Scientific Data](https://www.nature.com/articles/sdata201644), as well as in the follow up papers on specific modalities: [MEG](https://www.nature.com/articles/sdata2018110), [EEG](https://www.nature.com/articles/s41597-019-0104-8), [iEEG](https://www.nature.com/articles/s41597-019-0105-7), [genetics](https://doi.org/10.1093/gigascience/giaa104), [PET](https://doi.org/10.1038/s41597-022-01164-1), [microscopy](https://doi.org/10.3389/fnins.2022.871228), and [qMRI](https://doi.org/10.1038/s41597-022-01571-4).

- Look through some of the community's [presentations on BIDS](https://osf.io/yn93h/).

- Take a look at how the community [uses BIDS](https://medium.com/stanford-center-for-reproducible-neuroscience/bids-usage-survey-results-72637ff039c4).

- We have constructed a [grant writing kit](https://docs.google.com/document/d/1Q7JTOvUqt05YQfnbvGoP1SZQy_CGkNEVcsVZeS4D5_o/edit) to assist you in putting together BIDS-related grant proposals.

- We submitted an application to [The Neuro Open Science in action prize 2020](https://www.mcgill.ca/neuro/open-science/neuro-open-science-action-prize-2020). Please find our [associated application](./assets/BIDS-materials/2020_TheNeuro_OpenScienceInAction_application.pdf).
