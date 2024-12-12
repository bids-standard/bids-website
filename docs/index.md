---
title: BIDS
---

Neuroimaging experiments result in complex data that can be arranged in many different ways.
For a long time, there was no consensus how to organize and share
data obtained in neuroimaging experiments.
Even two researchers working in the same lab could opt to arrange their data in a different way.
Lack of consensus (or a standard) leads to misunderstandings and time wasted on rearranging data
or rewriting scripts expecting certain structure.
With the Brain  Imaging Data Structure (BIDS),
we describe a simple and easy to adopt way of organizing neuroimaging and behavioral data.

![BIDS-folder-organization](./assets/img/dicom-reorganization-transparent-black_1000x477.png#only-light)
![BIDS-folder-organization](./assets/img/dicom-reorganization-transparent-white_1000x477.png#only-dark)

BIDS was heavily inspired by the format used internally by the OpenfMRI repository
that is now known as [OpenNeuro][openneuro].
While working on BIDS we consulted many neuroscientists to make sure it covers most common experiments,
but at the same time is intuitive and easy to adopt.
The specification is intentionally based on simple file formats and folder structures
to reflect current lab practices and make it accessible to a wide range of scientists coming from different backgrounds.

## BIDS is a community effort

BIDS is developed by the community for the community
and everybody can [become a part of the community](./extensions/index.md).

The most important part of BIDS are the users:
if more people use it, more data will be shared and the more powerful it will become.

<strong>We want to make it easy to learn</strong> and more adopted.

Since BIDS is platform independent
and still an adapting, growing tool, the greater the community, the better it will be.

## Specification vs. Ecosystem

Since the inception of the BIDS specification that documents how to organize neuroimaging data,
a large ecosystem of tools and resources has evolved around BIDS.

A few of the key elements of this ecosystem are
the [BIDS specification](http://bids-specification.readthedocs.io/) with the nitty-gritty details,
<!-- markdown-link-check-disable -->
the [starter kit](./getting_started/index.md) with a simple explanation how to work with it,
<!-- markdown-link-check-enable -->
the [BIDS validator](https://github.com/bids-standard/bids-validator) to automatically check datasets for adherence to the specification,
[BIDS Apps](https://doi.org/10.1371/journal.pcbi.1005209), a collection of portable neuroimaging pipelines that understand BIDS datasets,
and [OpenNeuro][openneuro] as a database for BIDS formatted datasets.

A non-exhaustive list of further tools can be found in the [tools](./tools/index.md) section.

With the ongoing development of new tools and resources it is important to keep in mind
that the [BIDS specification](http://bids-specification.readthedocs.io/) remains
the standard according to which the entire ecosystem must adhere.

## Philosophy

Another part is that BIDS is striving to not reinventing other standards and metadata ontologies but reuse them:

![BIDS-minder](./assets/img/BIDS-minder.svg)

## Benefits

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

-   Databases such as [OpenNeuro.org](http://openneuro.org), [LORIS](http://www.loris.ca), [COINS](https://coins.trendscenter.org), [XNAT](https://central.xnat.org/), [SciTran](https://scitran.github.io/), and others will accept and export datasets organized according to BIDS.
    If you ever plan to share your data publicly (nowadays some journals require this) you can speed up the curation process by using BIDS.

-   There are [validation tools](https://github.com/bids-standard/bids-validator) (also available [online](http://bids-standard.github.io/bids-validator/)) that can check your dataset integrity and let you easily spot missing values.

## Further information

-   Good introductions to the BIDS standard can be found in the initial
   [paper published in Nature Scientific Data](https://www.nature.com/articles/sdata201644),
   as well as in the follow up papers on specific modalities:
   [MEG](https://www.nature.com/articles/sdata2018110),
   [EEG](https://www.nature.com/articles/s41597-019-0104-8),
   [iEEG](https://www.nature.com/articles/s41597-019-0105-7),
   [genetics](https://doi.org/10.1093/gigascience/giaa104),
   [PET](https://doi.org/10.1038/s41597-022-01164-1),
   [microscopy](https://doi.org/10.3389/fnins.2022.871228),
   and [qMRI](https://doi.org/10.1038/s41597-022-01571-4).

-   Look through some of the community's [presentations on BIDS](https://osf.io/yn93h/).

-   Take a look at how the community [uses BIDS](https://medium.com/stanford-center-for-reproducible-neuroscience/bids-usage-survey-results-72637ff039c4).

-   We have constructed a [grant writing kit](./impact/index.md)
    to assist you in putting together BIDS-related grant proposals.

-   We submitted an application to [The Neuro Open Science in action prize 2020](https://www.mcgill.ca/neuro/open-science/neuro-open-science-action-prize-2020).
    Please find our [associated application](./assets/BIDS-materials/2020_TheNeuro_OpenScienceInAction_application.pdf).

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
