# BIDS Impact

BIDS document  intends to convey how the BIDS Steering and Maintainers Group can
support your proposed BIDS grant. In an effort to express the impact of BIDS in
the brain imaging community, we have shared several of our traffic metrics.

## Measuring BIDS Impact

### Datasets

Over the years, the number of shared datasets available to the public has 
greatly increased. At its heart, adoption of the BIDS standard across datasets 
aids in the sharing of data and collaboration of research through the standardization 
of descriptive files names and the organization of data. BIDS organized datasets are 
available through public repositories such as [Openneuro.org](https://openneuro.org/) 
and the number of publicly available BIDS datasets continues to grow every year. 

<!-- use snippet to include a file
https://facelessuser.github.io/pymdown-extensions/extensions/snippets/#snippets-notation
-->

--8<-- "tmp/openneuro_data_growth.html"

### Citation Count

As the adoption of the BIDS standard across neuroimaging datasets has grown, so have 
citations for work that uses BIDS data and BIDS apps. To aid in searching for publications 
relevant to the BIDS standard, we have included some examples of BIDS references that are 
centralized in a [zotero group](https://www.zotero.org/groups/5111637/bids)

<!-- use snippet to include a file
https://facelessuser.github.io/pymdown-extensions/extensions/snippets/#snippets-notation
-->

--8<-- "tmp/citation_per_year.html"

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

For the number of docker pulls of specific BIDS apps, please check the
[BIDS app dashboard](https://bids-website.readthedocs.io/en/latest/tools/bids-apps.html).

### Contributors

Our list of contributors are captured in our
[contributor appendix](https://bids-specification.readthedocs.io/en/latest/99-appendices/01-contributors.html).
We update the contributor appendix every specification release. As of July 2023,
we have over 300 credited contributors.

A brief account of contributors per repository, estimated demographics and affiliations 
of contributors, and Github dependents counts are provided below:

| repository        | all-contributors                                                                                                                  | github                                                                                            |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| bids-standard     | ![GitHub contributors (via allcontributors.org)](https://img.shields.io/github/all-contributors/bids-standard/bids-specification) | ![GitHub Repo stars](https://img.shields.io/github/contributors/bids-standard/bids-specification) |
| bids-starter-kit  | ![GitHub contributors (via allcontributors.org)](https://img.shields.io/github/all-contributors/bids-standard/bids-starter-kit)   | ![GitHub Repo stars](https://img.shields.io/github/contributors/bids-standard/bids-starter-kit)   |
| bids-validator    | ![GitHub contributors (via allcontributors.org)](https://img.shields.io/github/all-contributors/bids-standard/bids-validator)     | ![GitHub Repo stars](https://img.shields.io/github/contributors/bids-standard/bids-validator)     |
| pybids            |                                                                                                                                   | ![GitHub Repo stars](https://img.shields.io/github/contributors/bids-standard/pybids)             |
| bids-matlab       | ![GitHub contributors (via allcontributors.org)](https://img.shields.io/github/all-contributors/bids-standard/bids-matlab)        | ![GitHub Repo stars](https://img.shields.io/github/contributors/bids-standard/bids-matlab)        |
| statistical model |                                                                                                                                   | ![GitHub Repo stars](https://img.shields.io/github/contributors/bids-standard/stats-models)       |

#### Gender of contributors

Guessed with [gender-guesser](https://pypi.org/project/gender-guesser/)

<!-- use snippet to include a file
https://facelessuser.github.io/pymdown-extensions/extensions/snippets/#snippets-notation
-->

--8<-- "data/people/gender.md"

#### Contributors affiliations

<!-- use snippet to include a file
https://facelessuser.github.io/pymdown-extensions/extensions/snippets/#snippets-notation
-->

--8<-- "data/people/affiliations.md"

<!-- use snippet to include a file
https://facelessuser.github.io/pymdown-extensions/extensions/snippets/#snippets-notation
-->

--8<-- "tmp/affiliations.html"

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

## BIDS History

Since its origin, the BIDS standard has revolutionized the way in which neuroimaging
research is done. The origin of the BIDS standard is commonly traced back to 2014, 
when a social media post ignited a deeper discussion about a new way of sharing 
data, that would ultimately lead to a set of standards that would improve scientific 
collaboration efforts. 

Following this initial discussion (and on the shoulders of many many volunteer hours 
by maintainers and the community at large) the BIDS standard saw significant adoption 
in the neuroimaging research landscape and continues to expand every day. A more complete 
history and discussion about the future of the BIDS landscape can be found in this 
[recent publication](https://pmc.ncbi.nlm.nih.gov/articles/PMC10516110/).

The BIDS standard continues to be adopted by a larger share of the community each year. 
We have seen a large and growing number of visitors to the BIDS website. A large number of
BIDS users also continue to explore the BIDS Specification and contribute to the community every month. 

We also document centers, institutes, and databases around the world that have implemented BIDS as
their organizational structure. While the list continues to grow, an initial list of centers and the associated
BIDS initiatives or database can be found 
[here](https://docs.google.com/spreadsheets/d/1aySjPpEGGQwFcOavkQdcvk2t2UMXt_zoTzWLWUmq20M/edit#gid=0).

### Website and Specification traffic dashboards

In order to measure the volume of traffic to our website and the
[ReadTheDocs rendering of the specification](https://bids-specification.readthedocs.io/en/stable/),
we utilize Google Analytics.

For visualizing our metrics, we have put together 2 dashboards:

1.  [the website](https://datastudio.google.com/u/0/reporting/eab164ba-9f98-46e8-bee8-1f4f5328dc6e/page/V5leB)
1.  [the specification](https://datastudio.google.com/u/0/reporting/57bf46f1-034c-4d8b-9fe2-3a2243e469c5/page/w1leB)

The default time period is set to the past 6 months. This can be changed by
adjusting the time period in the upper left corner. Please feel free to use any
of these figures in your grant! If there are additional statistics not currently
conveyed, please reach out to or the BIDS maintainters via a GitHub issue, or by email
 ([bids.maintenance@gmail.com](mailto:bids.maintenance@gmail.com)).

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

We also track the interest and usage of the BIDS standard via discussions on Neurostars 
to help us estimate trends in usage. Below is a snapshot as of ??? (date).  
<!--
TODO add automation to update every 6 months
-->

| tag            | nb topics | nb posts | topics with no reply | topics with answer |
|:---------------|----------:|---------:|---------------------:|-------------------:|
| bids           |       716 |     3404 |                  114 |                211 |
| bids-validator |        80 |      488 |                    1 |                 28 |
| pybids         |        29 |      175 |                    3 |                 12 |
| dcm2bids       |        92 |      529 |                    4 |                 53 |
| heudiconv      |       102 |      454 |                   17 |                 23 |
| mriqc          |       141 |      604 |                   32 |                 37 |
| fmriprep       |      1286 |     7727 |                  145 |                445 |
| qsiprep        |       170 |     1063 |                   12 |                 76 |
| aslprep        |        21 |       74 |                    5 |                  8 |
| nilearn        |       585 |     2454 |                   90 |                182 |
| fitlins        |        19 |      129 |                    2 |                  5 |
| openneuro      |        95 |      479 |                   15 |                 28 |

### Mailing list volume

As of July 1, 2020, we have 183 people signed up for our
[BIDS email list](https://forms.gle/JFo2aEkYbKY4EbmE6) and 412 members on our
[google group](https://groups.google.com/forum/#!forum/bids-discussion).


## How the BIDS team can help you

If you are in the process of putting together a grant, **please email/message
the pillar lead** that is most closely associated with your proposed grant or the 
BIDS maintainters email ([bids.maintenance@gmail.com](mailto:bids.maintenance@gmail.com)) 
so we may help support this. Our organization is structured into 3 pillars: standard,
tools, and collaboration.

Our range of support covers activities such as: meeting with the Steering and
Maintainers Groups to assisting with connecting you with other BIDS grant
writers or related initiatives to receiving a letter of support from the
Steering Group.

Regarding **requesting a letter of support** - please submit a drafted letter of
support to the collaboration lead or the BIDS maintainters email 
([bids.maintenance@gmail.com](mailto:bids.maintenance@gmail.com)) so we may review internally.

Please include how you plan on giving back to the BIDS community. The primary
mechanism is to support a member of your team to become a BIDS Maintainer.
Letters of support are approved by the Steering Group. This process may take 2-4
weeks to complete.

We kindly ask you to please **share your grant online** - successful or not.
This will signal to the rest of the community what avenues we have pursued and
what our fellow colleagues are planning on doing next. These can be grants that
directly extend our support into a new domain, grants that help BIDS (for example
OpenNeuro), or unsuccessful grant applications.

For example, please find our [NIH-R24 Brain Initiative BIDS-Derivatives grant](https://osf.io/c3dgx/).

A listing of the previous grants can be found [here](../collaboration/acknowledgments.md)

## Citing BIDS in your project 
You can find information on citing BIDS standards for specific modalities and 
citing BIDS in general 
[in the specification](https://bids-specification.readthedocs.io/en/latest/introduction.html#citing-bids)

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
