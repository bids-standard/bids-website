---
hide:
    - navigation
---

## What is BIDS?

The Brain Imaging Data Structure (BIDS) is a community-led set of standards
for organizing, describing, sharing and analyze neuroimaging data.

It is organized around 3 pilars:

1.  standards
1.  collaboration
1.  tools

Its goal is to make neuroimaging data more accessible, shareable, and usable by researchers.
To achieve this goal, BIDS provides a simple and intuitive way to organize and describe neuroimaging data and associated data and metadata.
BIDS is based on simple file formats (often text-based) and folder structures that can easily be adopted by any researcher around the world with minimum effort.
BIDS is not a file format, but instead relies upon common standard file formats (e.g. nifti, json, tsv).
BIDS has two major components.
First, it specifies a naming convention for files and directories.
Second, it specifies conventions for the organization of metadata.
A robust validator allows researchers to easily check whether a dataset meets the standard.



### BIDS as a set of standards

<!-- a set standardized method of organizing data -->

The [BIDS specification][specification] is intentionally based on simple file formats and folder structures
to reflect current lab practices and make it accessible to a wide range of scientists coming from different backgrounds.

![BIDS-folder-organization](./assets/img/dicom-reorganization-transparent-black_1000x477.png#only-light)
![BIDS-folder-organization](./assets/img/dicom-reorganization-transparent-white_1000x477.png#only-dark)

### BIDS as a community effort

<!-- a large community of researchers contributed to make sure that it includes what is needed to make the data usable -->

BIDS is developed by the community for the community
and everybody can [become a part of the community](./extensions/index.md).

The most important part of BIDS are the users:
if more people use it, more data will be shared and the more powerful it will become.

<strong>We want to make it easy to learn</strong> and more adopted.

Since BIDS is platform independent
and still an adapting, growing tool, the greater the community, the better it will be.

### BIDS as an ecosystem of tools

<!-- A large ecosystem of tools and datasets based on BIDS has emerged, making BIDS the foundation for much neuroimaging analysis. -->

Since the inception of the BIDS specification that documents how to organize neuroimaging data,
a large ecosystem of tools and resources has evolved around BIDS.

A few of the key elements of this ecosystem are
the [BIDS specification][specification] with the nitty-gritty details,
the [starter kit](./getting_started/index.md) with a simple explanation how to work with it,
the [BIDS validator][bids_validator_gh] to automatically check datasets for adherence to the specification,
[BIDS Apps](./tools/bids-apps.md), a collection of portable neuroimaging pipelines that understand BIDS datasets.

A non-exhaustive list of further tools can be found in the [tools](./tools/index.md) section.

With the ongoing development of new tools and resources it is important to keep in mind
that the [BIDS specification][specification]
remains the standard according to which the entire ecosystem must adhere.

## Why use BIDS?

1) Efficient data usage: The use of a common format allows data to be more easily reused by other researchers, maximizing its utility.  2) Analysis pipelines: there is a growing number of data analysis software packages (BIDS-Apps) that can automatically process data organized according to BIDS; 3) Data sharing: Use of BIDS makes sharing by major repositories (e.g. OpenNeuro) very simple, enabling rapid and effective data sharing.

<div class="grid cards" markdown>

-   :material-account-group:{ .lg .middle } **For the public good**

    ---

    -   Lowers scientific waste
    -   Gives opportunity to less-funded researchers
    -   Improves efficiency
    -   Spurs innovation

-   :recycle:{ .lg .middle } **For yourself**

    ---

    -   You are likely the future user of the data and data analysis pipelines you’ve developed

    -   Enables and simplifies collaboration

    -   Reviewers and funding agencies like to see reproducible results

    -   Open-science based funding opportunities and awards available
        (for instance: OHBM Replication Award, Mozilla Open Science Fellowship,
        Google Summer of Code, and so on.)

</div>

By using this standard you will benefit in the following ways:

-   It will be easy for another researcher to work on your data.
    To understand the organization of the files and their format you will only need to refer them to this document.
    This is especially important if you are running your own lab and anticipate more than one person working on the same data over time.
    By using BIDS you will save time trying to understand and reuse data acquired by a graduate student or postdoc that has already left the lab.

-   There is a growing number of [data analysis software packages](./tools/index.md) that can understand data organized according to BIDS.

-   Databases such as [OpenNeuro.org][openneuro], [LORIS](http://www.loris.ca), [COINS](https://coins.trendscenter.org), [XNAT](https://central.xnat.org/), [SciTran](https://scitran.github.io/), and others will accept and export datasets organized according to BIDS.
    If you ever plan to share your data publicly (nowadays some journals require this) you can speed up the curation process by using BIDS.

-   There are [validation tools][bids_validator_gh] (also available [online][bids_validator]) that can check your dataset integrity and let you easily spot missing values.

## Foundational principles

### Reuse existing standards

BIDS strives to reuse existing standares, formats, methods and technologies
whenever possible to minimize complexity and facilitate adoption.

![BIDS-minder](./assets/img/BIDS-minder.svg)

###  Tackle most common use cases

BIDS aims to tackle the most commonly used neuroimaging data, derivatives, and models
(inspired by the [Pareto principle](https://en.wikipedia.org/wiki/Pareto_principle)).

### Community engagement

BIDS should enable and maximize community engagement in the creation and extension of the specification,
to ensure maximal adoption by the research community.

## Further information

-   Good introductions to the BIDS standard can be found in the initial BIDS paper
    as well as in the follow up papers for BIDS extensions.
    All of those are listed in [the BIDS specification](https://bids-specification.readthedocs.io/en/latest/introduction.html#citing-bids).

-   Look through some of the community's [presentations on BIDS](https://osf.io/yn93h/).

-   To assist you in putting together BIDS-related grant proposals,
    check our [impact section that contains numbers and statistics about BIDS](./impact/index.md).

**Leave comments about the site below:**

<meta property="og:title" content="BIDS"/>
<script src="javascripts/giscus.js"></script>

---

<div style="display: flex; justify-content: space-evenly; align-items: center; flex-wrap: wrap">
  <div>
    <a href="https://www.incf.org/">
      <img src="./assets/img/logos/INCF.png"
           alt="INCF"
           width=200px>
    </a>
  </div>
  <div>
    <a href="https://summerofcode.withgoogle.com/">
      <img src="./assets/img/logos/GSoC_220px.png"
           alt="GSOC"
           width=200px>
    </a>
  </div>
  <div>
    <a href="http://grantome.com/grant/NIH/R24-MH114705-01">
      <img src="./assets/img/logos/NIH.png"
           alt="NIH"
            width=200px>
    </a>
  </div>
  <div>
    <a href="https://www.arnoldventures.org/newsroom/laura-and-john-arnold-foundation-announces-3-8-million-grant-to-stanford-university-to-improve-the-quality-of-neuroscience-research">
      <img src="./assets/img/logos/arnold_foundation.png"
           alt="Arnold Ventures"
           width=200px>
    </a>
  </div>
</div>
