---
---

# Benefits

By using this standard you will benefit in the following ways:

- It will be easy for another researcher to work on your data. To understand the organization of the files and their format you will only need to refer them to this document. This is especially important if you are running your own lab and anticipate more than one person working on the same data over time. By using BIDS you will save time trying to understand and reuse data acquired by a graduate student or postdoc that has already left the lab.
- There is a growing number of [data analysis software packages](#software) that can understand data organized according to BIDS.
- Databases such as [OpenNeuro.org](http://openneuro.org){:target="_blank"}, [LORIS](http://www.loris.ca){:target="_blank"}, [COINS](https://portal.mrn.org){:target="_blank"}, [XNAT](https://central.xnat.org/){:target="_blank"}, [SciTran](https://scitran.github.io/){:target="_blank"}, and others will accept and export datasets organized according to BIDS. If you ever plan to share your data publicly (nowadays some journals require this) you can speed up the curation process by using BIDS.
- There are [validation tools](https://github.com/bids-standard/bids-validator){:target="_blank"} (also available [online](http://bids-standard.github.io/bids-validator/){:target="_blank"}) that can check your dataset integrity and let you easily spot missing values.

# Software currently supporting BIDS:

- [BIDS Apps](http://bids-apps.neuroimaging.io){:target="_blank"} (a growing set of portable containerized data processing pipelines that understand BIDS datasets)

A description of how to build containerized apps supporting BIDS inputs can be found in the [paper published in PLOS Computational Biology](http://doi.org/10.1371/journal.pcbi.1005209){:target="_blank"}.

## Converters

{% include converters_table.html members=site.data.converters %}

{% include converters_table.html members=site.data.MEEG_converters %}

{% include converters_table.html members=site.data.institution_converters %}

{% include converters_table.html members=site.data.from_BIDS_converters %}

{% include converters_table.html members=site.data.other_converters %}

## Quality Assessment

- [MRIQC](http://mriqc.readthedocs.org/){:target="_blank"}
- [QAP](http://preprocessed-connectomes-project.org/quality-assessment-protocol/){:target="_blank"}

## Other Tools

- [Automatic Analysis](https://github.com/automaticanalysis/automaticanalysis){:target="_blank"} (multimodal MATLAB toolbox processing fMRI, DTI/DKI, and M/EEG)
- [BIDSHandler](https://github.com/Macquarie-MEG-Research/BIDSHandler){:target="_blank"} (Python module allowing complete manipulation of BIDS data)
- [Brainstorm](http://neuroimage.usc.edu/brainstorm/){:target="_blank"} (MEG/EEG analysis package)
- [C-PAC](http://fcp-indi.github.io/){:target="_blank"} (Configurable Pipeline for the Analysing Connectomes)
- [FMRIPREP](https://github.com/poldracklab/preprocessing-workflow){:target="_blank"} (preprocessing workflow)
- [OpenNeuro](http://openneuro.org){:target="_blank"} (repository)
- [PyBIDS](https://github.com/bids-standard/pybids){:target="_blank"} (Python module to harmonize access and manipulation)
- [bids-matlab](https://github.com/bids-standard/bids-matlab){:target="_blank"} (MATLAB/Octave tools to interact with datasets conforming to the BIDS format)
- [GUI dataset description generator](https://github.com/tolik-g/BIDS){:target="_blank"} (GUI form that generates dataset_description.json)
