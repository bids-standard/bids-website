---
---

# Get involved in making BIDS better

The easiest way to contribute to BIDS is to ask questions you have about
the specification on [Neurostars](https://neurostars.org){:target="_blank"}. If your
question has a [bids tag](https://neurostars.org/search?q=tags%3Abids){:target="_blank"}
it will be much easier for others to find the answer.

You can also get involved by _answering_ questions on
[Neurostars](https://neurostars.org/search?q=tags%3Abids){:target="_blank"}!

You can contribute to the BIDS specification by opening
[Issues](https://github.com/bids-standard/bids-specification/issues){:target="_blank"} and
propose changes via [Pull
Requests](https://github.com/bids-standard/bids-specification/pulls){:target="_blank"} on
[GitHub](https://github.com/bids-standard/bids-specification){:target="_blank"}.

To make improvements to the website that you are reading right now, you
can also open an
[Issue](https://github.com/bids-standard/bids-website/issues){:target="_blank"} and
propose changes via [Pull
Requests](https://github.com/bids-standard/bids-website/pulls){:target="_blank"} at its
[GitHub repository](https://github.com/bids-standard/bids-website){:target="_blank"}.

There are so many ways to help us build this community.
You could help someone else learn the benefits of BIDS, give a talk in
your local organisation, or [build a BIDS
App](https://bids-apps.neuroimaging.io/){:target="_blank"}!

The only requirement is that everyone who contributes adheres to our
[BIDS Code of Conduct](https://github.com/bids-standard/bids-specification/blob/master/CODE_OF_CONDUCT.md){:target="_blank"}.

Thank you for your contributions!

## Extending the BIDS specification

The BIDS specification can be extended in a backwards compatible way and
will evolve over time. These are accomplished with BIDS Extension
Proposals (BEPs), which are community-driven processes.

Do you want to extend BIDS to a new modality or set of data types?
Please draft a BIDS Extension Proposal (BEP) following the [BIDS
Extension Proposals
Guide](https://docs.google.com/document/d/1pWmEEY-1-WuwBPNy5tDAxVJYQ9Een4hZJM06tQZg8X4){:target="_blank"}.

You can also contribute to ongoing BIDS Extension Proposals. Below is a
table of currently-active BEPs. The "Extension label" column provides a
direct link to the documentation.

Please find our [latest BEP update](https://docs.google.com/presentation/d/1uvxJaGgrk58HBWRqLzJTwHjpJKFLGM7YTiNvGwvjMOA/edit?usp=sharing){:target:"_blank"}
presented in the [Open Science Room](https://ohbm.sparkle.space/in/opensciencesig){:target:"_blank"} at [OHBM](https://www.humanbrainmapping.org/i4a/pages/index.cfm?pageid=4041){:target:"_blank"}.

Note that all of the extension ideas that are not backwards compatible and thus
will have to wait for BIDS 2.0 are listed
[here](https://docs.google.com/document/d/1LEgsMiisGDe1Gv-hBp1EcLmoz7AlKj6VYULUgDD3Zdw){:target="_blank"}.

| Extension label                                                 | Title                                                                                                      | Moderators/ leads                                                | Summary                                                                                                                                                                                                                                   | Blocking point(s)                                                                      |
| --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| [BEP002](https://bids.neuroimaging.io/bep002){:target:"_blank"} | The BIDS Models Specification                                                                              | Tal Yarkoni , Chris Markiewcz                                    | Reworked structure - list of steps is now a directed,graph, [Model zoo](https://github.com/bids-standard/model-zoo){:target:"_blank"}, Abstracted transformations, to ease interoperability of implementations                         | Stat Models released v1.0.0-rc1 in June 2021 - Please review! |
| [BEP004](https://bids.neuroimaging.io/bep004){:target:"_blank"} | Susceptibility Weighted Imaging (SWI)                                                                      | Available                                                        | Looking for a new leader.                                                                                                                                                                                                              | Searching for a new leader.                                                            |
| [BEP011](https://bids.neuroimaging.io/bep011){:target:"_blank"} | The structural preprocessing derivatives                                                                   | Viviana Siless                                                   | Features Surfaces, Scalar maps on Surfaces, and Morphometrics. Opened [pull request](https://github.com/bids-standard/bids-specification/pull/518){:target:"_blank"}. Need to conform with final Common Derivatives and gather community feedback. | Blocked by BIDS-validator extending and PyBIDS implementation for common derivatives |
| [BEP012](https://bids.neuroimaging.io/bep012){:target:"_blank"} | The functional preprocessing derivatives                                                                   |Chris Markiewicz                                                  | Opened the [pull request](https://github.com/bids-standard/bids-specification/pull/519){:target:"_blank"}. Features Derivative images (mean, ALFF, ReHo, etc.), Time series (confounds, decompositions, etc.) | Blocked by BIDS-validator extending and PyBIDS implementation |
| [BEP013](https://bids.neuroimaging.io/bep013){:target:"_blank"} | The resting state fMRI derivatives                                                                         | Steven Giavasis                                                  | Merged into BEP012.                                                                                                                                                                                                                    | None.                                                                                  |
| [BEP014](https://bids.neuroimaging.io/bep014){:target:"_blank"} | The affine transformations and nonlinear field warps                                                       | Oscar Esteban                                                    | Creating file format (X5) to store spatial transforms. [There is a software prototype - NiTransforms](https://osf.io/8aq7b/){:target:"_blank"} demonstrates implementation of this BEP. NiTransforms has been tested and integrated to work within fMRIPrep | In progress. |
| [BEP016](https://bids.neuroimaging.io/bep016){:target:"_blank"} | The diffusion weighted imaging derivatives                                                                 | Franco Pestilli and Oscar Esteban                                | Being discussed [here](https://github.com/bids-standard/bids-bep016){:target:"_blank"}. Coordinating with BEP017. Difussion-weighted model description merged, but must comply to [this](https://github.com/bids-standard/bids-bep016/issues/7){:target:"_blank"}. Upcoming integration across DWI, Tractography, Tractometry, and Connectivity (from fMRI and DWI) |          None.                                                                              |
| [BEP017](https://bids.neuroimaging.io/bep017){:target:"_blank"} | Generic BIDS connectivity data schema                                                                      | Eugene Duff                                                      | [Current state](https://bids.neuroimaging.io/bep017){:target:"_blank}. Intended as a meeting point for minimal harmonisation of connectivity-based formats across modalities. Seeking use cases spanning modalities and input defining connectivity based formats | None. |
| [BEP019](https://bids.neuroimaging.io/bep019){:target:"_blank"} | DICOM Metadata                                                                                             | Satrajit Ghosh                                                   | Not active. Could be a NIDM extension rather than in BIDS.                                                                                                                                                                             | None.                                                                                  |
| [BEP020](https://bids.neuroimaging.io/bep020){:target:"_blank"} | Eye Tracking including Gaze Position and Pupil Size(ET)                                                    | Dejan Draschkow                                                  | BEP close to PR submission, examples and validator under development. Seeking additional BEP lead to help incoporate into standard contact [dejan](mailto:dejan.draschow@psy.ox.ac.uk) to get involved.                                | None.                                                                                  |
| [BEP021](https://bids.neuroimaging.io/bep021){:target:"_blank"} | Common Electrophysiological Derivatives                                                                    | Stefan Appelhoff, Arnaud Delorme, Dora Hermes, Mainak Jas, Guiomar Niso, Robert Oostenveld, and Cyril Pernet | Discussion [here](https://github.com/bids-standard/bep021){:target:"_blank"} UCSD to include head models with BIDS EEG data. Developments of BIDS M/EEG pipelines will trigger discussion on storing derived data. | Mostly on hold.             |
| [BEP022](https://bids.neuroimaging.io/bep022){:target:"_blank"} | Magnetic Resonance Spectroscopy (MRS)                                                                      | Mark Mikkelsen, William Clarke and Martin Wilson                 | Group discussions [here](https://forum.mrshub.org/t/bids-for-spectroscopy/83){:target:"_blank"} and [here](https://forum.mrshub.org/t/nifti-mrs-discussion-thread/443){:target:"_blank"}. Developed NifTI standard for MRS data - presented abstract at ISMRM; manuscript in preparation. | None.                                                                                      |
| [BEP023](https://bids.neuroimaging.io/bep023){:target:"_blank"} | PET Preprocessing derivatives                                                                              | Martin Noergaard, Graham Searle, Melanie Ganz                    | Work in progress following BEP009 incorporation into spec. Coord. kickoff scheduled Sept. 2021 to capture various experimental designs and needs for preprocessing and pharmacokinetic modeling. Focused on staying aligned with derivatives for MRI (structural, functional, ASL, diffusion) | Progressing and soliciting input from senior PET experts. |
| [BEP024](https://bids.neuroimaging.io/bep024){:target:"_blank"} | Computed Tomography scan (CT)                                                                              | Hugo Boniface                                                    | Lead seeking more contributors and experts.                                                                                                                                                                    | None.                                                                                  |
| [BEP025](https://bids.neuroimaging.io/bep025){:target:"_blank"} | Medical Imaging Data structure (MIDS)                                                                      | Jose Manuel Saborit Torres, Maria de la Iglesia Vayá             | Enhancing [BEP025 preprint](https://arxiv.org/abs/2010.00434){:target:"_blank"}. Provided [automated tool](https://github.com/BIMCV-CSUSP/MIDS){:target:"_blank"} to convert projects uploaded to XNAT platforms to BIDS/MIDS. Example datasets: [Massive Image Data Anatomy Spine](https://bimcv.cipf.es/bimcv-projects/project-midas/){:target:"_blank"}, [BIMCV-COVID19+](https://bimcv.cipf.es/bimcv-projects/bimcv-covid19/){:target:"_blank"}, and [BIMCV-COVID19-](https://bimcv.cipf.es/bimcv-projects/bimcv-covid19/#1590859488150-148be708-c3f3){:target:"_blank"}. Included Kaggle Challenge [SIIM-FISABIO-RSNA COVID-19 Detection](https://www.kaggle.com/c/siim-covid19-detection/overview){:target:"_blank"} | None.
| [BEP026](https://bids.neuroimaging.io/bep026){:target:"_blank"} | Microelectrode Recordings                                                                                  |                                                                  | BEP is open to new leadership, see also [BEP032 (animal electrophys)](https://bids.neuroimaging.io/bep032){:target:"_blank"} | Searching for a new leader. | 
| [BEP027](https://bids.neuroimaging.io/bep027){:target:"_blank"} | BIDS Applications 2.0                                                                                      | Chris Markiewicz and Greg Kiar                                   | Focusing on: command-line conventions, I/O interface descriptors, and common behavior (e.g., exit codes for failure modes); relies upon the Boutiques standard. Re-conception of BIDS Apps| None.                                                                           |
| [BEP028](https://bids.neuroimaging.io/bep028){:target:"_blank"} | Provenance                                                                                                 | Satra Ghosh and Camille Maumet                                   | BEP aims to provide a description of data manipulation and transformations steps related to a BIDS data element via BIDS structured sidecar JSON-LD files. Can be used to describe provenance at different levels of granularity. Dicussions held in[this repository](https://github.com/bids-standard/BEP028_BIDSprov){:target:"_blank"}. A set of [examples](https://github.com/bids-standard/BEP028_BIDSprov/tree/master/examples){:target:"_blank"} and [user stories](https://github.com/bids-standard/BEP028_BIDSprov/issues/48){:target:"_blank"} are being refined. | None.                                                                                  |
| [BEP029](https://bids.neuroimaging.io/bep029){:target:"_blank"} | Virtual and physical motion data                                                                           | Sein Jeung and Julius Welzel                                     | BEP is developing and starting to finalize as discussions concerning example datasets are completed.  | None. |
| [BEP030](https://bids.neuroimaging.io/bep030){:target:"_blank"} | Near Infrared Spectroscopy (NIRS)                                                                          | Robert Luke and Luca Pollonini                                   | BEP presented at the society for fNIRS conference. Have developed SNRIF data format. Opened as [pull request](https://forum.mrshub.org/t/nifti-mrs-discussion-thread/443){:target:"_blank"}. Primarily for continuous wave NIRS (CW-NIRS), but want to ensure not to preclude future extensions. Examples and validator efforts in progress. Inviting colleagues from time- and frequency-domain fNIRS to review proposal.| None.                                                                                  |
| [BEP031](https://bids.neuroimaging.io/bep031){:target:"_blank"} | Microscopy                                                                                                 | Marie-Hélène Bourget and Julien Cohen-Adad                       | BEP is finalizing proposal and community review, preparing to submit to specification in Fall 2021. Metadata related pull requests for [sample entity and samples.tsv](https://github.com/bids-standard/bids-specification/pull/812){:target:"_blank"} and [participants.tsv](https://github.com/bids-standard/bids-specification/pull/816){:target:"_blank"}. | None.                                                                                  |
| [BEP032](https://bids.neuroimaging.io/bep032){:target:"_blank"} | Animal electrophysiology                                                                                   | Sylvain Takerkart and Julia Sprenger                             | New BEP, collecting comments and community feedback which may be submitted [here](https://github.com/INCF/neuroscience-data-structure/issues), directly to [Sylvain](mailto:sylvain.takerkart@univ-amu.fr) & [Julia](mailto:julia.sprenger@univ-amu.fr), or [here](https://www.incf.org/sig/incf-working-group-standardized-data){:target:"_blank"} during the ~monthly meeting. Example datasets [here](https://gin.g-node.org/NeuralEnsemble/BEP032-examples){:target:"_blank"}. Supporting early stage interaction with: [ProbeInterface & SpikeInterface](https://github.com/SpikeInterface){:target:"_blank"}, [AnDO](https://github.com/INT-NIT/AnDO){:target:"_blank"}, Interoperability with NWB and NIX data/metadata formats.                                                                                                                    | None.                                           |
| [BEP033](https://bids.neuroimaging.io/bep033){:target:"_blank"} | Advanced Diffusion Weighted Imaging (aDWI)                                                                 | James Gholam, Leandro Beltrachini and Filip Szczepankiewicz      | New BEP, seeking contributors and collecting community feedback relating to: priority sequences to support, best supported binary structured formats (e.g. CBOR? HDF5? MsgPack?) Comments may be submitted directly on the document. Generating example datasets [here](https://github.com/JAgho/MISP_plot/tree/main){:target:"_blank"} and Determining best practice w/ vendors to record data in-sequence | None.                                           |


### Completed BEPs

When an extension reaches maturity it is merged into the main body of
the specification.  Below is a table of BEPs that have been merged in
the main body of the specification.

| Extension label                                                 | Title                                      | Moderators/leads                                  |
| --------------------------------------------------------------- | ------------------------------------------ | ------------------------------------------------- |
| [BEP001](https://bids.neuroimaging.io/bep001){:target:"_blank"} | Structural acquisitions that include multiple contrasts (multi echo, flip angle, inversion time) sequences | Gilles de Hollander and Kirstie Whitaker                         |
| [BEP003](https://bids.neuroimaging.io/bep003){:target:"_blank"} | Common Derivatives                         | Chris Markiewicz                                  |
| [BEP005](https://bids.neuroimaging.io/bep005){:target:"_blank"} | Arterial Spin Labeling (ASL)               | Henk-Jan Mutsaerts, Patricia Clement, Jan Petr, Marco Castellaro |
| [BEP006](https://bids.neuroimaging.io/bep006){:target:"_blank"} | Electroencephalography (EEG)               | Cyril Pernet, Stefan Appelhoff, Robert Oostenveld |
| [BEP007](https://bids.neuroimaging.io/bep007){:target:"_blank"} | Hierarchical Event Descriptor (HED) Tags   | Chris Gorgolewski                                 |
| [BEP008](https://bids.neuroimaging.io/bep008){:target:"_blank"} | Magnetoencephalography (MEG)               | Guiomar Niso                                      |
| [BEP009](https://bids.neuroimaging.io/bep009){:target:"_blank"} | Positron Emission Tomography (PET)         | Melanie Ganz                                      |
| [BEP010](https://bids.neuroimaging.io/bep010){:target:"_blank"} | intracranial Electroencephalography (iEEG) | Chris Holdgraf, Dora Hermes                       |
| [BEP018](https://bids.neuroimaging.io/bep018){:target:"_blank"} | Genetic information                        | Cyril R Pernet, Clara Moreau, Thomas Nichols      |

Some proposals that set out to extend the BIDS specification have instead become tools for handling BIDS. See the table below.

| Extension label                                                 | Title        | Moderators/leads                               | Tool name                                                                 |
| --------------------------------------------------------------- | ------------ | ---------------------------------------------- | ------------------------------------------------------------------------- |
| [BEP015](https://bids.neuroimaging.io/bep015){:target:"_blank"} | Mapping file | Eric Earl, Camille Maumet, and Vasudev Raguram | [File mapper](https://github.com/DCAN-Labs/file-mapper){:target:"_blank"} |
