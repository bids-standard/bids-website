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


## Acknowledgments

This work has been done by the community of [individual contributors](https://bids-specification.readthedocs.io/en/stable/appendices/contributors.html). Their work was
supported by the

| Support source | Description of the contributions |
| ----- | -----|
| [International Neuroinformatics Coordinating Facility](https://www.incf.org/) | [Neuroimaging Data Sharing Task Force](https://web.archive.org/web/20170813183704/http://wiki.incf.org/mediawiki/index.php/Neuroimaging_Task_Force) collated initial group of people to push pilot BIDS development and promotion|
| Laura and John Arnold Foundation | |
| [NIMH R24MH114705](https://reporter.nih.gov/project-details/9411944) | BIDS common derivatives BEP |
| [NSF OAC-1760950](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1760950) | |
| [NIMH 1R24MH117295](https://reporter.nih.gov/project-details/9795271) | DANDI archive contributed development of Microscopy BEP|
| [NIMH 2P41EB019936](https://reporter.nih.gov/project-details/10334133) | ReproNim project contributed various enhancements and fixes|
| [NIMH MH117179](https://reporter.nih.gov/project-details/10145071) | OpenNeuro archive contributed various enhancements and fixes|
| [NIMH 1ZIAMH002977-01](https://reporter.nih.gov/project-details/10489085) |  OpenNeuroPET project contributed various enhancements and fixes |
| [NIMH 5R01MH126699-02](https://reporter.nih.gov/project-details/10460628) | [Brain Connectivity Project](https://pestillilab.github.io/bids-connectivity/)|
| [NIMH MH109682](https://reporter.nih.gov/project-details/9982125) | NeuroScout|
| Novo Nordisk Foundation NNF20OC0063277 | |
| [NIMH 1RF1MH126700-01A1](https://reporter.nih.gov/project-details/10480619) | Hierarchical Event Descriptors (HED)|
| [NIBIB 1R01EB020740](https://reporter.nih.gov/project-details/9053094) | Nipype|
| [The Neuro-Irv and Helga Cooper Foundation](https://www.mcgill.ca/neuro/open-science/open-science-awards-and-prizes/neuro-irv-and-helga-cooper-foundation-open-science-prizes) | 2023 International Open Science Prize|

![INCF-badge](./assets/img/incf-badge_281x210.png)

<a href="https://summerofcode.withgoogle.com/"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/GSoC.png/220px-GSoC.png" width="125" height="125" title="GSOC" alt="GSOC"></a>
<a href="https://www.incf.org/"><img src="https://www.eudat.eu/sites/default/files/styles/medium/public/logo/INCF_0.png?itok=uRT54XCM" width="200" height="125" title="INCF" alt="INCF"></a>
<a href="https://www.arnoldventures.org/newsroom/laura-and-john-arnold-foundation-announces-3-8-million-grant-to-stanford-university-to-improve-the-quality-of-neuroscience-research"><img src="https://www.arnoldventures.org/static/img/logo-on-light.svg" width="200" height="125" title="Arnold Ventures" alt="Arnold Ventures"></a>
<a href="http://grantome.com/grant/NIH/R24-MH114705-01"><img src="http://grantome.com/images/funders/NIH.png" width="125" height="125" title="NIH" alt="NIH"></a>
