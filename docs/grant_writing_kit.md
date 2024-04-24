---
hide:
-   navigation
---

# BIDS grant writing kit

This document intends to convey how the BIDS Steering and Maintainers Group can
support your proposed BIDS grant. In an effort to express the impact of BIDS in
the brain imaging community, we have shared several of our traffic metrics.

## How the BIDS team can help you

If you are in the process of putting together a grant, **please email/message
the pillar lead** that is most closely associated with your proposed grant so we
may help support this. Our organization is structured into 3 pillars: standard,
tools, and collaboration.

The respective leads are:

-   Stefan Appelhoff ([stefan.appelhoff@mailbox.org](mailto:stefan.appelhoff@mailbox.org)),
-   Chris Markiewicz ([markiewicz@stanford.edu](mailto:markiewicz@stanford.edu))

Our range of support covers activities such as: meeting with the Steering and
Maintainers Groups to assisting with connecting you with other BIDS grant
writers or related initiatives to receiving a letter of support from the
Steering Group.

Regarding **requesting a letter of support** - please submit a drafted letter of
support to the collaboration lead (???) so we may review internally.

Please include how you plan on giving back to the BIDS community. The primary
mechanism is to support a member of your team to become a BIDS Maintainer.
Letters of support are approved by the Steering Group. This process may take 2-4
weeks to complete.

We kindly ask you to please **share your grant online** - successful or not.
This will signal to the rest of the community what avenues we have pursued and
what our fellow colleagues are planning on doing next. These can be grants that
directly extend our support into a new domain, grants that help BIDS (for example
OpenNeuro), or unsuccessful grant applications. For example, please find our
[NIH-R24 Brain Initiative BIDS-Derivatives grant](https://osf.io/c3dgx/).

A listing of the previous grants can be found here:

https://bids.neuroimaging.io/acknowledgments.html

## dashboards

### Datasets

![](./images/openneuro_data_growth.png)

### Citation Count

BIDS references are centralized in a zotero group:
https://www.zotero.org/groups/5111637/bids

You can also find them on this page:
https://bids-specification.readthedocs.io/en/latest/introduction.html#citing-bids

![](./images/newplot.png)

#### Citation according to google scholar

<!--
original
https://docs.google.com/spreadsheets/d/1rz3mQl5qvYBVvqJlWhSg1c9qS09ayG8GmyOqS8JZxWc/edit#gid=0

updated tsv in this folder
-->

![](./images/google_citations.png)

### GitHub stars

| repository        | stars                                                                                      |
| ----------------- | ------------------------------------------------------------------------------------------ |
| bids-standard     | ![GitHub Repo stars](https://img.shields.io/github/stars/bids-standard/bids-specification) |
| bids-starter-kit  | ![GitHub Repo stars](https://img.shields.io/github/stars/bids-standard/bids-starter-kit)   |
| bids-validator    | ![GitHub Repo stars](https://img.shields.io/github/stars/bids-standard/bids-validator)     |
| pybids            | ![GitHub Repo stars](https://img.shields.io/github/stars/bids-standard/pybids)             |
| bids-matlab       | ![GitHub Repo stars](https://img.shields.io/github/stars/bids-standard/bids-matlab)        |
| statistical model | ![GitHub Repo stars](https://img.shields.io/github/stars/bids-standard/stats-models)       |
| fmriprep          | ![GitHub Repo stars](https://img.shields.io/github/stars/nipreps/fmriprep)                 |
| mriqc             | ![GitHub Repo stars](https://img.shields.io/github/stars/nipreps/mriqc)                    |
| qsiprep           | ![GitHub Repo stars](https://img.shields.io/github/stars/PennLINC/qsiprep)                 |

### Downloads

| package           | downloads                                                                                                                |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------ |
| bids-validator    | ![npm](https://img.shields.io/npm/dm/bids-validator) ![Docker Pulls](https://img.shields.io/docker/pulls/bids/validator) |
| pybids            | ![PyPI - Downloads](https://img.shields.io/pypi/dm/pybids)                                                               |
| bids-schema       | ![PyPI - Downloads](https://img.shields.io/pypi/dm/bidsschematools)                                                      |
| statistical model | ![PyPI - Downloads](https://img.shields.io/pypi/dm/bsmschema)                                                            |

For the number of docker pulls of the BIDS apps, please check the
[BIDS app dashboard](https://bids-apps.neuroimaging.io/apps/).

### Contributors

Our list of contributors are captured in our
[contributor appendix](https://bids-specification.readthedocs.io/en/latest/99-appendices/01-contributors.html).
We update the contributor appendix every specification release. As of July 2023,
we have over 300 credited contributors.

| repository        | all-contributors                                                                                                                  | github                                                                                            |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| bids-standard     | ![GitHub contributors (via allcontributors.org)](https://img.shields.io/github/all-contributors/bids-standard/bids-specification) | ![GitHub Repo stars](https://img.shields.io/github/contributors/bids-standard/bids-specification) |
| bids-starter-kit  | ![GitHub contributors (via allcontributors.org)](https://img.shields.io/github/all-contributors/bids-standard/bids-starter-kit)   | ![GitHub Repo stars](https://img.shields.io/github/contributors/bids-standard/bids-starter-kit)   |
| bids-validator    | ![GitHub contributors (via allcontributors.org)](https://img.shields.io/github/all-contributors/bids-standard/bids-validator)     | ![GitHub Repo stars](https://img.shields.io/github/contributors/bids-standard/bids-validator)     |
| pybids            |                                                                                                                                   | ![GitHub Repo stars](https://img.shields.io/github/contributors/bids-standard/pybids)             |
| bids-matlab       | ![GitHub contributors (via allcontributors.org)](https://img.shields.io/github/all-contributors/bids-standard/bids-matlab)        | ![GitHub Repo stars](https://img.shields.io/github/contributors/bids-standard/bids-matlab)        |
| statistical model |                                                                                                                                   | ![GitHub Repo stars](https://img.shields.io/github/contributors/bids-standard/stats-models)       |

#### Gender of contributors

Guessed with: https://pypi.org/project/gender-guesser/

-   male: 177
-   female: 47
-   andy: 6
-   unknown: 80
-   mostly_male: 13
-   mostly_female: 2

#### Contributors affiliations

Number of known affiliations: 148

Number of authors without affiliation: 171

Number of unkwon affiliations: 19

![](./images/affiliations.png)

### GitHub dependents

<!--
TODO add automation to update regularly.

pip install -U github-dependents-info
github-dependents-info --repo bids-standard/pybids --badgemarkdownfile ./dashboard.md
-->

<!-- gh-dependents-info-used-by-start -->

<!-- gh-dependents-info-used-by-end -->

| repository | dependents                                                                                                                                                        |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| pybids     | [![](https://img.shields.io/static/v1?label=Used%20by&message=596&color=informational&logo=slickpic)](https://github.com/bids-standard/pybids/network/dependents) |

## Measuring BIDS Impact

### Impact summary

Since its origin, the BIDS has revolutionized the way in which neuroimaging
research is done.

~??? users visiting the website, and ~??? users exploring the BIDS
Specification, over the past ??? months.

Currently, ???
[reported](https://docs.google.com/spreadsheets/d/1aySjPpEGGQwFcOavkQdcvk2t2UMXt_zoTzWLWUmq20M/edit#gid=0)
centers, institutes and databases around the world that have implemented BIDS as
their organizational structure.

### Website and Specification traffic dashboards

In order to measure the volume of traffic to our
[website](https://bids.neuroimaging.io/) and the
[ReadTheDocs rendering of the specification](https://bids-specification.readthedocs.io/en/stable/),
we utilize Google Analytics.

For visualizing our metrics, we have put together 2 dashboards:

1.  [the website](https://datastudio.google.com/u/0/reporting/eab164ba-9f98-46e8-bee8-1f4f5328dc6e/page/V5leB)
1.  [the specification](https://datastudio.google.com/u/0/reporting/57bf46f1-034c-4d8b-9fe2-3a2243e469c5/page/w1leB)

The default time period is set to the past 6 months. This can be changed by
adjusting the time period in the upper left corner. Please feel free to use any
of these figures in your grant! If there are additional statistics not currently
conveyed, please reach out to (???).

### BIDS usage

We ran
[a survey](https://reproducibility.stanford.edu/bids-usage-survey-results/) in
June 2019 to evaluate the uptake of BIDS in the community. We received feedback
from 116 global researchers.

We have a
[google doc](https://docs.google.com/spreadsheets/d/1aySjPpEGGQwFcOavkQdcvk2t2UMXt_zoTzWLWUmq20M/edit#gid=0)
that is crowdsourcing imaging centers, institutes, databases around the world
that have implemented BIDS as their organizational structure.

### Neurostars

<!--
TODO add automation to update every 6 months
-->

| tag                | nb topics | nb posts | topics with no reply | topics with answer |
| :----------------- | --------: | -------: | -------------------: | -----------------: |
| bids               |       602 |     2918 |                   91 |                167 |
| bids-specification |         5 |       22 |                    0 |                  4 |
| bids-validator     |        69 |      414 |                    1 |                 23 |
| bids-app           |        18 |       99 |                    2 |                  9 |
| bidskit            |         4 |       11 |                    2 |                  0 |
| pybids             |        23 |      132 |                    3 |                 10 |
| bidsonym           |         1 |        1 |                    1 |                  0 |
| dcm2bids           |        54 |      276 |                    2 |                 25 |
| heudiconv          |        77 |      349 |                   12 |                 16 |
| mriqc              |       127 |      547 |                   28 |                 34 |
| fmriprep-report    |         8 |       37 |                    0 |                  2 |
| fmriprep           |       530 |     2792 |                   81 |                145 |
| dmriprep           |         8 |       13 |                    5 |                  0 |
| qsiprep            |        86 |      525 |                    7 |                 31 |
| aslprep            |         7 |       29 |                    1 |                  3 |
| smriprep           |         2 |        7 |                    0 |                  0 |
| dtiprep            |         1 |        7 |                    0 |                  1 |
| nipreps            |         6 |       26 |                    3 |                  2 |
| niprep             |         1 |        1 |                    1 |                  0 |
| nilearn            |       474 |     2024 |                   69 |                137 |
| fitlins            |        15 |       79 |                    2 |                  4 |
| openneuro          |        79 |      423 |                   10 |                 22 |
| openneuro-cli      |         1 |        2 |                    0 |                  0 |

### Mailing list volume

As of July 1, 2020, we have 183 people signed up for our
[BIDS email list](https://forms.gle/JFo2aEkYbKY4EbmE6) and 412 members on our
[google group](https://groups.google.com/forum/#!forum/bids-discussion).

<!--
## Future steps: TODO

- add country of origin to contributor appendix
- nb of datasets (openneuro or else):
  - where are they from
  - gender of dataset authors
- Enhance news and events when collaboration pillar is established
- Sharing previous BIDS grants: when the organizational design is completed, we
  can establish a common area to place this information.
-->
