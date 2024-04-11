---
---

# Benefits

By using this standard you will benefit in the following ways:

- It will be easy for another researcher to work on your data. To understand the organization of the files and their format you will only need to refer them to this document. This is especially important if you are running your own lab and anticipate more than one person working on the same data over time. By using BIDS you will save time trying to understand and reuse data acquired by a graduate student or postdoc that has already left the lab.
- There is a growing number of [data analysis software packages](#software) that can understand data organized according to BIDS.
- Databases such as [OpenNeuro.org](http://openneuro.org){:target="_blank"}, [LORIS](http://www.loris.ca){:target="_blank"}, [COINS](https://coins.trendscenter.org){:target="_blank"}, [XNAT](https://central.xnat.org/){:target="_blank"}, [SciTran](https://scitran.github.io/){:target="_blank"}, and others will accept and export datasets organized according to BIDS. If you ever plan to share your data publicly (nowadays some journals require this) you can speed up the curation process by using BIDS.
- There are [validation tools](https://github.com/bids-standard/bids-validator){:target="_blank"} (also available [online](http://bids-standard.github.io/bids-validator/){:target="_blank"}) that can check your dataset integrity and let you easily spot missing values.

## Publishing your dataset

If you are a journal editorand you want to encourage, authors to publish their data as BIDS
you can include such snippet on your website:

> For data documentation, it is advised to use the BIDS format (https://bids.neuroimaging.io/).
> It is recommended that the authors check the respective box in the submission form.
> It is recommended that authors use ‘BIDS’ as one of the key-words of the manuscript.
> And it is recommended that authors mention the version of the BIDS validator that was used to ensure BIDS compatibility.

### Journals that encourage using BIDS

- aperture: https://apertureneuro.org/for-authors

## Converters

{% include converters_table.html members=site.data.converters %}

{% include converters_table.html members=site.data.MEEG_converters %}

{% include converters_table.html members=site.data.from_BIDS_converters %}

{% include converters_table.html members=site.data.physio_converters %}

{% include converters_table.html members=site.data.other_converters %}

# Software currently supporting BIDS:

- [BIDS Apps](http://bids-apps.neuroimaging.io){:target="_blank"} (a growing set of portable containerized data processing pipelines that understand BIDS datasets)

A description of how to build containerized apps supporting BIDS inputs can be found in the [paper published in PLOS Computational Biology](http://doi.org/10.1371/journal.pcbi.1005209){:target="_blank"}.

## Other Tools

{% include list_tools.html tools=site.data.tools %}
