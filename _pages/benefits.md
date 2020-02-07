---
---

# Benefits

By using this standard you will benefit in the following ways:

- It will be easy for another researcher to work on your data. To understand the organization of the files and their format you will only need to refer them to this document. This is especially important if you are running your own lab and anticipate more than one person working on the same data over time. By using BIDS you will save time trying to understand and reuse data acquired by a graduate student or postdoc that has already left the lab.
- There is a growing number of [data analysis software packages](#software) that can understand data organized according to BIDS.
- Databases such as [OpenNeuro.org](http://openneuro.org), [LORIS](http://www.loris.ca), [COINS](https://portal.mrn.org), [XNAT](https://central.xnat.org/), [SciTran](https://scitran.github.io/) and others will accept and export datasets organized according to BIDS. If you ever plan to share your data publicly (nowadays some journals require this) you can speed up the curation process by using BIDS.
- There are [validation tools](https://github.com/bids-standard/bids-validator) (also available [online](http://bids-standard.github.io/bids-validator/)) that can check your dataset integrity and let you easily spot missing values.

# Software currently supporting BIDS:

- [BIDS Apps](http://bids-apps.neuroimaging.io) (a growing set of portable containerized data processing pipelines that understand BIDS datasets)

A description of how to build containerized apps supporting BIDS inputs can be found in the [paper published in PLOS Computational Biology](http://doi.org/10.1371/journal.pcbi.1005209).

## Converters

- [AFNI BIDS-tools](https://github.com/nih-fmrif/BIDS-tools)
- [BIDS2ISATab](https://github.com/bids-standard/BIDS2ISATab)
- [BIDSto3col](https://github.com/bids-standard/bidsutils/tree/master/BIDSto3col)
- [BIDS2NDA](https://github.com/bids-standard/BIDS2NDA)
- [bidsify](https://github.com/NILAB-UvA/bidsify)
- [bidskit](https://github.com/jmtyszka/bidskit)
- [Data2Bids](https://github.com/SIMEXP/Data2Bids)
- [Dcm2Bids](https://github.com/cbedetti/Dcm2Bids)
- [DCM2NIIx](https://github.com/neurolabusc/dcm2niix)
- [DICM2NII](https://www.mathworks.com/matlabcentral/fileexchange/42997-dicom-to-nifti-converter--nifti-tool-and-viewer)
- [HeuDiConv](https://github.com/nipy/heudiconv)
- [OpenfMRI2BIDS](https://github.com/bids-standard/openfmri2bids)
- [ReproIn](https://github.com/ReproNim/reproin) (HeuDiConv-based turnkey solution)
- [bids2xar](https://github.com/lwallace23/bids2xar) (for XNAT import)
- [XNAT2BIDS](https://github.com/kamillipi/2bids)
- [Horos (Osirix) export plugin](https://github.com/mslw/horos-bids-output)
- [BIDS2NIDM](https://github.com/incf-nidash/PyNIDM/blob/master/nidm/experiment/tools/NIDM2BIDSMRI.py)
- [BIDScoin](https://github.com/Donders-Institute/bidscoin)
- [MNE-BIDS](http://mne-tools.github.io/mne-bids/) (MEG/EEG/iEEG)
- [EEGLAB](https://sccn.ucsd.edu/eeglab/index.php) with [plugin](https://github.com/arnodelorme/bids-matlab-tools) (MEG/EEG analysis package)

## Institution specific data management/conversion tools

- [dac2bids](https://github.com/dangom/dac2bids)
- [Autobids](https://github.com/khanlab/autobids) from the Centre for Functional and Metabolic Mapping (CFMM) at Western’s Robarts Research Institute
- [Biscuit](https://github.com/Macquarie-MEG-Research/Biscuit)
- [BiDirect_BIDS_Converter](https://github.com/wulms/BiDirect_BIDS_Converter) from the Institute of epidemiology and social medicine, University of Münster

## Quality Assessment

- [MRIQC](http://mriqc.readthedocs.org/)
- [QAP](http://preprocessed-connectomes-project.org/quality-assessment-protocol/)

## Other Tools

- [Automatic Analysis](https://github.com/rhodricusack/automaticanalysis) (fMRI processing toolbox)
- [BIDSHandler](https://github.com/Macquarie-MEG-Research/BIDSHandler) (Python module allowing complete manipulation of BIDS data)
- [Brainstorm](http://neuroimage.usc.edu/brainstorm/) (MEG/EEG analysis package)
- [C-PAC](http://fcp-indi.github.io/) (Configurable Pipeline for the Analysing Connectomes)
- [FMRIPREP](https://github.com/poldracklab/preprocessing-workflow) (preprocessing workflow)
- [OpenNeuro](http://openneuro.org) (repository)
- [PyBIDS](https://github.com/bids-standard/pybids) (Python module to harmonize access and manipulation)
