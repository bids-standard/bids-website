---
---

# Benefits

By using this standard you will benefit in the following ways:

- It will be easy for another researcher to work on your data. To understand the organization of the files and their format you will only need to refer them to this document. This is especially important if you are running your own lab and anticipate more than one person working on the same data over time. By using BIDS you will save time trying to understand and reuse data acquired by a graduate student or postdoc that has already left the lab.
- There is a growing number of [data analysis software packages](#software) that can understand data organized according to BIDS.
- Databases such as [OpenNeuro.org](http://openneuro.org){:target="_blank"}, [LORIS](http://www.loris.ca){:target="_blank"}, [COINS](https://coins.trendscenter.org){:target="_blank"}, [XNAT](https://central.xnat.org/){:target="_blank"}, [SciTran](https://scitran.github.io/){:target="_blank"}, and others will accept and export datasets organized according to BIDS. If you ever plan to share your data publicly (nowadays some journals require this) you can speed up the curation process by using BIDS.
- There are [validation tools](https://github.com/bids-standard/bids-validator){:target="_blank"} (also available [online](http://bids-standard.github.io/bids-validator/){:target="_blank"}) that can check your dataset integrity and let you easily spot missing values.

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

- [BIDSHandler](https://github.com/Macquarie-MEG-Research/BIDSHandler){:target="_blank"} (Python module allowing complete manipulation of BIDS data)
- [bids-cfood](https://gitlab.indiscale.com/caosdb/src/crawler-cfoods/bids-cfood)
  a module to handle BIDS dataset for the caosDB data crawler.
- [bids2cite](https://github.com/Remi-Gau/bids2cite){:target="_blank"} a python package to interactively update `dataset_decription.json` and generate citation files (for example `datacite.yml`) for BIDS datasets.
- [bids-matlab](https://github.com/bids-standard/bids-matlab){:target="_blank"} (MATLAB/Octave tools to interact with datasets conforming to the BIDS format)
- [Brainstorm](http://neuroimage.usc.edu/brainstorm/){:target="_blank"} (MEG/EEG analysis package)
- [clpipe](https://clpipe.readthedocs.io/en/latest/index.html){:target="_blank"} streamlined processing pipeline for MRI data centered around BIDS.
- [cuBIDS](https://pypi.org/project/cubids/){:target="_blank"} a python package designed to facilitate reproducible curation of neuroimaging BIDS datasets.
- [GUI dataset description generator](https://github.com/tolik-g/BIDS){:target="_blank"} (GUI form that generates dataset_description.json)
- [Lead-DBS](https://www.lead-dbs.org/) A toolbox facilitating Deep Brain Stimulation electrode reconstructions and computer simulations supports BIDS conversion and ingestion of BIDS datasets.
- [OpenNeuro](http://openneuro.org){:target="_blank"} (repository)
- [PRFmodel](https://github.com/vistalab/PRFmodel){:target="_blank"} a set of tools to fit the fit population receptor field models to BIDS datasets.
- [PyBIDS](https://github.com/bids-standard/pybids){:target="_blank"} (Python module to harmonize access and manipulation)
- [spm_2_bids](https://github.com/cpp-lln-lab/spm_2_bids){:target="_blank"} a tool convert SPM preprocessed output to BIDS derivatives (trying to follow [BEP12](https://bids.neuroimaging.io/bep012){:target="_blank"})
