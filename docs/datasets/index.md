# Datasets

BIDS compliant data can be found under many of the common neural data sharing
websites/databases. Below are some links to BIDS compliant data. Sourcedata (pre-BIDS)
are sometimes also available and these data can be used to test (or to build tutorials)
of how source data are converted to BIDS.

## Where to find BIDS datasets

Many public repositories for neuroimaging data are accepting (and in some cases requiring) data submitted in BIDS format.
Below is a small sample of some main resources for finding BIDS datasets that may be used in your analyses.

!!! note "Tools to help discover datasets"

    - The [Neurobagel query tool](https://query.neurobagel.org/?node=All) is a web interface for searching across a BIDS datasets based on various subject clinical-demographic and imaging
        parameters.
    - [BIDS-eye](https://bidseye.xyz/) is search engine and database that automatically crawls large public neuroimaging data lakes, indexes the metadata and makes them easily searchable.
    - the [Datalad registry](https://registry.datalad.org/overview/?query=metadata%5Bbids_dataset%5D%3A%22%22&sort=update-desc) can help you discover Public Datalad dataset including those that are BIDS datasets

[OpenNeuro][openneuro]:
If you're looking for full data files to run the validator on or simply compare to your
own _bidsified_ data try searching here. Datasets here are (by and large) publicly available and conform to BIDS.

[publicnEUro](https://publicneuro.eu/) is a data repository for BIDS datasets.
The principle is similar to OpenNeuro, where each dataset is shared independently.
Once shared, a DOI is available for citation, and the link allows users to access the data.
The platform is GDPR compliant, allowing us to share brain imaging data in a way that is as FAIR as possible.
The catalog keeps all metadata open and therefore findable.
Because EU data have to be protected, publicnEUro provide the necessary privacy protections by controlling user access.

[The NIMH Data Archive](https://nda.nih.gov/): The NIMH archive hosts many datasets and results
that follow BIDS naming structure. There isn't an easy search feature for finding BIDS data as of
yet, but larger datasets, such as the Adolescent Brain Cognitive Development (ABCD) study, provide
BIDS compliant data.

[NITRC](https://www.nitrc.org/xnat/index.php): the Neuroimaging Tools & Resources Collaboratory is another
resource for finding BIDS compliant datasets. The Neuroimaging Data Repository section provides
access to public datasets such as the Autism Brain Imaging Data Exchange (ABIDE) dataset.

## Brainhack Western 2018 dataset

These data, compiled at the Brainhack Western 2018 event can be used to test or create BIDS
apps. An example of sourcedata
[ds001](https://drive.google.com/drive/folders/15GiGHqit0gFFblOUuL2hSoWEJVw6q1M5)
(non-BIDS compliant NIfTi files) and raw data
[ds001_BIDS](https://drive.google.com/drive/folders/1A3TbarHbtXqx7FfW0UbWWuY1GflF3630) converted
to BIDS format are provided.

## Mother of unification studies

A 204-subject multimodal (MEG, MRI, fMRI) [dataset](https://doi.org/10.34973/37n0-yc51) to study language processing.

## BIDS examples with empty raw data files

[BIDS examples datasets](./examples.md) contain empty (example) raw data files
and can assist you in converting your own dataset into a BIDS compliant dataset,
or to run some tests with your code...

## Small or easily downloadable BIDS datasets

If you’re looking for smaller, quicker-to-download BIDS datasets for testing or tutorials, the resources below might help. These examples are typically small, publicly available, and come in a clear BIDS format.

| Dataset Name                                                | Description                                                                                     | Link                                                       | Size    | Source     |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------| ---------------------------------------------------------- | --------| ---------- |
| **Rhyme Judgment (OpenNeuro ds000003)**                    | A 13-subject fMRI dataset for rhyme vs. pseudo-rhyme word judgment. Good for validator tests.   | [OpenNeuro ds000003](https://openneuro.org/datasets/ds000003)  | ~391MB  | OpenNeuro  |
| **Brainstorm MEG sample (OpenNeuro ds000246)**             | A 1-subject MEG dataset (auditory oddball) with corresponding MRI. Excellent for MEG-BIDS tests.| [OpenNeuro ds000246](https://openneuro.org/datasets/ds000246)  | ~2.29GB  | OpenNeuro  |
| **CIMBI [11C]DASB PET (OpenNeuro ds001420)**               | A PET dataset (2 subjects) measuring serotonin transporter. Demonstrates PET-BIDS format. | [OpenNeuro ds001420](https://openneuro.org/datasets/ds001420)  | ~579MB  | OpenNeuro  |
| **ASL-BIDS sample**                                        | A collection of minimal ASL datasets (total ~31MB) demonstrating different ASL sequences.       | [OSF project](https://osf.io/3npsa/)                      | ~31MB   | OSF        |

These datasets are publicly available under their respective licenses. Always consult each dataset’s documentation or README for details.
