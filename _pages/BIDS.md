---
---

A SIMPLE WAY TO ORGANIZE YOUR NEUROIMAGING DATA.
[//]: # (This letters should be big, I don't know how you can change fontsize for a specific paragraph)


# Why is BIDS needed?

Neuroimaging experiments result in complicated data that can be arranged in many different ways.
So far there is no consensus how to organize and share data obtained in neuroimaging experiments.
Even two researchers working in the same lab can opt to arrange their data in a different way.
Lack of consensus (or a standard) leads to misunderstandings and time wasted on rearranging data or rewriting scripts expecting certain structure.
With the Brain  Imaging Data Structure (BIDS), we describe a simple and easy to adopt way of organizing neuroimaging and behavioral data.

![BIDS-folder-organization](./assets/img/dicom-reorganization-transparent-white_1000x477.png){: .center-image }


# What is BIDS?

The Brain Imaging Data Structure (BIDS) is a community-led standard for organizing, describing and sharing neuroimaging data.  


BIDS was heavily inspired by the format used internally by the OpenfMRI repository that is now known as [OpenNeuro](https://openneuro.org){:target="_blank"}.
While working on BIDS we consulted many neuroscientists to make sure it covers most common experiments, but at the same time is intuitive and easy to adopt.
The specification is intentionally based on simple file formats and folder structures to reflect current lab practices and make it accessible to a wide range of scientists coming from different backgrounds.

## BIDS is a community effort

BIDS is developed by the community for the community and everybody can [become a part of the community](https://bids.neuroimaging.io/get_involved.html).

## Specification vs. Ecosystem

Since the inception of the BIDS specification that documents how to organize neuroimaging data, a large ecosystem of tools and resources has evolved around BIDS.

A few of the key elements of this ecosystem are the [BIDS-validator](https://github.com/bids-standard/bids-validator){:target="_blank"}, to automatically check datasets for adherence to the specification, [OpenNeuro](https://openneuro.org/){:target="_blank"}, as a database for BIDS formatted datasets, and [BIDS-Apps](https://doi.org/10.1371/journal.pcbi.1005209){:target="_blank"}, a collection of portable neuroimaging pipelines that understand BIDS datasets.

A non-exhaustive list of further tools can be found in the [Benefits](https://bids.neuroimaging.io/benefits.html) section.

With the ongoing development of new tools and resources it is important to keep in mind that the BIDS specification remains the standard according to which the entire ecosystem must adhere.

# Benefits

By using this standard you will benefit in the following ways:

- It will be easy for another researcher to work on your data. To understand the organization of the files and their format you will only need to refer them to this document. This is especially important if you are running your own lab and anticipate more than one person working on the same data over time. By using BIDS you will save time trying to understand and reuse data acquired by a graduate student or postdoc that has already left the lab.
- There is a growing number of [data analysis software packages](#software) that can understand data organized according to BIDS.
- Databases such as [OpenNeuro.org](http://openneuro.org){:target="_blank"}, [LORIS](http://www.loris.ca){:target="_blank"}, [COINS](https://portal.mrn.org){:target="_blank"}, [XNAT](https://central.xnat.org/){:target="_blank"}, [SciTran](https://scitran.github.io/){:target="_blank"}, and others will accept and export datasets organized according to BIDS. If you ever plan to share your data publicly (nowadays some journals require this) you can speed up the curation process by using BIDS.
- There are [validation tools](https://github.com/bids-standard/bids-validator){:target="_blank"} (also available [online](http://bids-standard.github.io/bids-validator/){:target="_blank"}) that can check your dataset integrity and let you easily spot missing values.


[//]: # (Now it should come a button linking to BIDS Tools: "Learn more BIDS Tools")


## Further Information

- Good introductions to the BIDS standard can be found in the initial [paper published in Nature Scientific Data](https://www.nature.com/articles/sdata201644){:target="_blank"}, as well as in the follow up papers on specific modalities: [MEG](https://www.nature.com/articles/sdata2018110){:target="_blank"}, [EEG](https://www.nature.com/articles/s41597-019-0104-8){:target="_blank"}, and [iEEG](https://www.nature.com/articles/s41597-019-0105-7){:target="_blank"}.

- Look through some of the community's [presentations on BIDS](https://osf.io/yn93h/){:target="_blank"}.

- We have constructed a [grant writing kit](https://docs.google.com/document/d/1Q7JTOvUqt05YQfnbvGoP1SZQy_CGkNEVcsVZeS4D5_o/edit){:target="_blank"} to assist grant writers putting together BIDS related grant proposals.

- Take a look at how the community [uses BIDS](https://medium.com/stanford-center-for-reproducible-neuroscience/bids-usage-survey-results-72637ff039c4){:target="_blank"}.

- We submitted an application to [The Neuro Open Science in action prize 2020](https://www.mcgill.ca/neuro/open-science/neuro-open-science-action-prize-2020){:target="_blank"}. Please find our [associated application](./BIDS-materials/2020_TheNeuro_OpenScienceInAction_application.pdf){:target="_blank"}.

- Sign up to receive occasional [updates by email](https://docs.google.com/forms/d/1ZLi5qRTuX11KGK7qIidSdZvznFoXAqr2wh6003okv-0/){:target="_blank"} and follow BIDS on [Twitter](https://twitter.com/BIDSstandard?ref_src=twsrc%5Etfw){:target="_blank"}.

