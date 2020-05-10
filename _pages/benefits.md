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

- [AFNI BIDS-tools](https://github.com/nih-fmrif/BIDS-tools){:target="_blank"}
- [BIDS2ISATab](https://github.com/bids-standard/BIDS2ISATab){:target="_blank"}
- [BIDSto3col](https://github.com/bids-standard/bidsutils/tree/master/BIDSto3col){:target="_blank"}
- [BIDS2NDA](https://github.com/bids-standard/BIDS2NDA){:target="_blank"}
- [bidsify](https://github.com/NILAB-UvA/bidsify){:target="_blank"}
- [bidskit](https://github.com/jmtyszka/bidskit){:target="_blank"}
- [Data2Bids](https://github.com/SIMEXP/Data2Bids){:target="_blank"}
- [Dcm2Bids](https://github.com/cbedetti/Dcm2Bids){:target="_blank"}
- [DCM2NIIx](https://github.com/neurolabusc/dcm2niix){:target="_blank"}
- [DICM2NII](https://www.mathworks.com/matlabcentral/fileexchange/42997-dicom-to-nifti-converter--nifti-tool-and-viewer){:target="_blank"}
- [HeuDiConv](https://github.com/nipy/heudiconv){:target="_blank"}
- [OpenfMRI2BIDS](https://github.com/bids-standard/openfmri2bids){:target="_blank"}
- [ReproIn](https://github.com/ReproNim/reproin) (HeuDiConv-based turnkey solution){:target="_blank"}
- [bids2xar](https://github.com/lwallace23/bids2xar){:target="_blank"} (for XNAT import)
- [XNAT2BIDS](https://github.com/kamillipi/2bids){:target="_blank"}
- [Horos (Osirix) export plugin](https://github.com/mslw/horos-bids-output){:target="_blank"}
- [BIDS2NIDM](https://github.com/incf-nidash/PyNIDM/blob/master/nidm/experiment/tools/NIDM2BIDSMRI.py){:target="_blank"}
- [BIDScoin](https://github.com/Donders-Institute/bidscoin){:target="_blank"}
- [MNE-BIDS](http://mne-tools.github.io/mne-bids/){:target="_blank"} (MEG/EEG/iEEG)
- [EEGLAB](https://sccn.ucsd.edu/eeglab/index.php){:target="_blank"} with [plugin](https://github.com/arnodelorme/bids-matlab-tools){:target="_blank"} (MEG/EEG analysis package)
- [BrkRaw](https://github.com/dvm-shlee/bruker){:target="_blank"} (for preclinical Bruker MRI)

## Institution specific data management/conversion tools

- [dac2bids](https://github.com/dangom/dac2bids){:target="_blank"}
- [Autobids](https://github.com/khanlab/autobids){:target="_blank"} from the Centre for Functional and Metabolic Mapping (CFMM) at Western’s Robarts Research Institute
- [Biscuit](https://github.com/Macquarie-MEG-Research/Biscuit){:target="_blank"}
- [BiDirect_BIDS_Converter](https://github.com/wulms/BiDirect_BIDS_Converter){:target="_blank"} from the Institute of epidemiology and social medicine, University of Münster

## Quality Assessment

- [MRIQC](http://mriqc.readthedocs.org/){:target="_blank"}
- [QAP](http://preprocessed-connectomes-project.org/quality-assessment-protocol/){:target="_blank"}

## Other Tools

- [Automatic Analysis](https://github.com/rhodricusack/automaticanalysis){:target="_blank"} (fMRI processing toolbox)
- [BIDSHandler](https://github.com/Macquarie-MEG-Research/BIDSHandler){:target="_blank"} (Python module allowing complete manipulation of BIDS data)
- [Brainstorm](http://neuroimage.usc.edu/brainstorm/){:target="_blank"} (MEG/EEG analysis package)
- [C-PAC](http://fcp-indi.github.io/){:target="_blank"} (Configurable Pipeline for the Analysing Connectomes)
- [FMRIPREP](https://github.com/poldracklab/preprocessing-workflow){:target="_blank"} (preprocessing workflow)
- [OpenNeuro](http://openneuro.org){:target="_blank"} (repository)
- [PyBIDS](https://github.com/bids-standard/pybids){:target="_blank"} (Python module to harmonize access and manipulation)
- [bids-matlab](https://github.com/bids-standard/bids-matlab){:target="_blank"} (MATLAB/Octave tools to interact with datasets conforming to the BIDS format)
