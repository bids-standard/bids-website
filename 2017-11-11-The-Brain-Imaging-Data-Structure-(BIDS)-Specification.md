---
title: The Brain Imaging Data Structure (BIDS) Specification
layout: post
author: krzysztof.gorgolewski
permalink: /the-brain-imaging-data-structure-(bids)-specification/
source-id: 1HFUkAEE-pB-angVcYe6pf_-fVf4sCpOHKesUvfb8Grc
published: true
---
The Brain Imaging Data Structure (BIDS) Specification

version 1.0.2 (working copy)

 Available under the CC-BY 4.0 International license.

Browse example datasets: 

[https://github.com/INCF/BIDS-examples](https://github.com/INCF/BIDS-examples)

Download example datasets: [https](https://drive.google.com/folderview?id=0B2JWN60ZLkgkMGlUY3B4MXZIZW8&usp=sharing)[://drive.google.com/folderview?id=0B2JWN60ZLkgkMGlUY3B4MXZIZW8&usp=sharing](https://drive.google.com/folderview?id=0B2JWN60ZLkgkMGlUY3B4MXZIZW8&usp=sharing) 

# 1 Changelog

* Added SequenceName field.

* Added support for describing events with Hierarchical Event Descriptors [[8.5 Task events](#heading=h.daip42kp5ndz)]

* Added VolumeTiming and AcquisitionDuration fields [[8.4 Task (including resting state) imaging data](#heading=h.r8mrcau3kkcq)].

* Added DwellTime field.

**1.0.****2**

* Added support for high resolution (anatomical) T2star images [[8.3 Anatomy imaging data](#heading=h.fm6ipijipc08)]

* Added support for multiple defacing masks [[8.3 Anatomy imaging data](#heading=h.fm6ipijipc08)]

* Added optional key and metadata field for contrast enhanced structural scans [[8.3 Anatomy imaging data](#heading=h.fm6ipijipc08)]

* Added DelayTime field [[8.4 Task (including resting state) imaging data](#heading=h.r8mrcau3kkcq)]

* Added support for multi echo BOLD data [[8.4 Task (including resting state) imaging data](#heading=h.r8mrcau3kkcq)]

**1.0.1**

* Added InstitutionName field [[8.4 Task (including resting state) imaging data](#heading=h.r8mrcau3kkcq)]

* Added InstitutionAddress field [[8.4 Task (including resting state) imaging data](#heading=h.r8mrcau3kkcq)]

* Added DeviceSerialNumber field [[8.4 Task (including resting state) imaging data](#heading=h.r8mrcau3kkcq)]

* Added NumberOfVolumesDiscardedByUser and NumberOfVolumesDiscardedByScanner field [[8.4 Task (including resting state) imaging data](#heading=h.r8mrcau3kkcq)]

* Added TotalReadoutTime to functional images metadata list  [[8.4 Task (including resting state) imaging data](#heading=h.r8mrcau3kkcq)].

**1.0.1****-rc1**

* Added T1 Rho maps [[8.3 Anatomy imaging data](#heading=h.fm6ipijipc08)]

* Added support for phenotypic information split into multiple files [[8.11 Participant key file]](#heading=h.pi5iigxxt8vy)

* Added recommendations for multi site datasets

* Added SoftwareVersions.

* Added run-<run_index> to the phase encoding maps. Improved the description.

* Added InversionTime metadata key.

* Clarification on the source vs raw language.

* Added trial_type column to the event files.

* Added missing  sub-<participant_label> in behavioural data file names

* Added ability to store stimuli files.

* Clarified the language describing allowed subject labels.

* Added quantitative proton density maps.

**1.0.0**

* Added ability to specify fieldmaps acquired with multiple parameter sets.

* Added ability to have multiple runs of the same fieldmap.

* Added FLASH anatomical images.

**1.0.0-rc4**

* Replaced links to neurolex with explicit DICOM Tags.

* Added sourcedata.

* Added data dictionaries.

* Be more explicit about contents of JSON files for structural (anatomical) scans.

**1.0.0-rc3**

* Renamed PhaseEncodingDirection values from "x", “y”, “z” to “i”, “j”, “k” to avoid confusion with FSL parameters

* Renamed SliceEncodingDirection values from "x", “y”, “z” to “i”, “j”, “k”

**1.0.0-rc2**

* Removed the requirement that TSV files cannot include more than two consecutive spaces.

* Refactor of the definitions sections (copied from the manuscript)

* Make support for uncompressed .nii files more explicit.

* Added BIDSVersion to dataset.json

* Remove the statement that SliceEncodingDirection is necessary for slice time correction

* Change dicom converter recommendation from dcmstack to dcm2nii and dicm2nii following interactions with the community (see [https://github.com/moloney/dcmstack/issues/39](https://github.com/moloney/dcmstack/issues/39) and [https://github.com/neurolabusc/dcm2niix/issues/4](https://github.com/neurolabusc/dcm2niix/issues/4))

* Added section on behavioral experiments with no accompanying MRI acquisition

* Add _magnitude.nii[.gz] image for GE type fieldmaps.

* Replaced EchoTimeDifference with EchoTime1 and EchoTime2 (SPM toolbox requires this input).

* Added support for single band reference image for DWI.

* Added DatasetDOI field in the dataset description.

* Added description of more metadata fields relevant to DWI fieldmap correction.

* PhaseEncodingDirection is now expressed in "x", “y” etc. instead of “PA” “RL” for DWI scans (so it's the same as BOLD scans)

* Added rec-<label> flag to BOLD files to distinguish between different reconstruction algorithms (analogous to anatomical scans).

* Added recommendation to use _physio suffix for continuous recordings of motion parameters obtained by the scanner side reconstruction algorithms.

**1.0.0-rc1**

* Initial release

# 2 Table of contents

[[TOC]]

# 3 Introduction

## 3.1 Motivation

Neuroimaging experiments result in complicated data that can be arranged in many different ways. So far there is no consensus how to organize and share data obtained in neuroimaging experiments. Even two researchers working in the same lab can opt to arrange their data in a different way. Lack of consensus (or a standard) leads to misunderstandings and time wasted on rearranging data or rewriting scripts expecting certain structure. Here we describe a simple and easy to adopt way of organising neuroimaging and behavioural data. By using this standard you will benefit in the following ways:

* It will be easy for another researcher to work on your data. To understand the organisation of the files and their format you will only need to refer them to this document. This is especially important if you are running your own lab and anticipate more than one person working on the same data over time. By using BIDS you will save time trying to understand and reuse data acquired by a graduate student or postdoc that has already left the lab.

* There are a growing number of data analysis software packages that can understand data organised according to BIDS (see [http://bids.neuroimaging.io](http://bids.neuroimaging.io) for the most up to date list).

* Databases such as OpenfMRI.org accept datasets organised according to BIDS. If you ever plan to share your data publicly (nowadays some journals require this) you can minimize the additional time and energy spent on publication, and speed up the curation process by using BIDS to structure and describe your data right after acquisition.

* There are [validation](https://github.com/Squishymedia/BIDS-Validator)[ tools](https://github.com/Squishymedia/BIDS-Validator) that can check your dataset integrity and let you easily spot missing values.

BIDS is heavily inspired by the format used internally by OpenfMRI.org and has been supported by the International Neuroinformatics Coordinating Facility and the Neuroimaging Data Sharing Task Force. While working on BIDS we consulted many neuroscientists to make sure it covers most common experiments, but at the same time is intuitive and easy to adopt. The specification is intentionally based on simple file formats and folder structures to reflect current lab practices and make it accessible to wide range of scientists coming from different backgrounds. (NOTE:  For review of other data organization standards in neuroimaging see Appendix.)

## 3.2 Definitions

The keywords "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this  document are to be interpreted as described in [[RFC2119](https://www.ietf.org/rfc/rfc2119.txt)].

Throughout this protocol we use a list of different MRI related terms. To avoid misunderstanding we clarify them here.

1. **Dataset** - a set of neuroimaging and behavioural data acquired for a purpose of a particular study. A dataset consists of data acquired from one or more subjects, possibly from multiple sessions.

2. **Subject** - a person or animal participating in the study.

3. **Session **- a logical grouping of neuroimaging and behavioural data consistent across subjects. Session can (but doesn't have to) be synonymous to a visit in a longitudinal study. In general, subjects will stay in the scanner during one session. However if a subject has to leave the scanner room and then be re-positioned on the scanner bed, the set of MRI acquisitions will still be considered as a session and match sessions acquired in other subjects. Similarly in situations where different type of data is obtained over several visits (for example fMRI on one day followed by DWI the day after) those can be grouped in one session. Defining multiple sessions is appropriate when several identical or similar data acquisitions are planned and performed on all -or most- subjects, often in the case of some intervention between sessions (e.g., training).

4. **MRI acquisition **- a continuous uninterrupted block of time during which an MRI scanner was acquiring data according to particular scanning sequence/protocol.

5. **Data type** - a functional group of different types of  MRI data. In BIDS we define four data types: func (task based and resting state functional MRI), dwi (diffusion weighted imaging), fmap (field inhomogeneity mapping data such as field maps), anat (structural imaging such as T1, T2, etc.)

6. **Task **-  a set of structured activities performed by the participant. Tasks are usually accompanied by stimuli and responses, and can greatly vary in complexity. For the purpose of this protocol we consider the so-called "resting state" a task. In context of MR, a task is always tied to one MRI acquisition. Therefore, even if during one acquisition the subject performed multiple conceptually different behaviours (with different sets of instructions) they will be considered one (combined) task.

7. **Event** - a stimulus or subject response recorded during a task. Each event has an onset time and duration. Note that not all tasks will have recorded events (e.g., resting state).

8. **Run** - an uninterrupted repetition of an MRI acquisition that has the same acquisition parameters and task (however events can change from run to run due to different subject response or randomized nature of the stimuli).

## 3.3 Compulsory, optional, and additional data and metadata

The following standard describes a way of arranging data and writing down metadata for a subset of neuroimaging experiments. Some aspects of the standard are compulsory. For example a particular file name format is required when storing structural scans. Some aspects are regulated but optional. For example a T2 volume does not need to be included, but when it is available it should be saved under a particular file name specified in the standard.

This standard aspires to describe a majority of datasets, but acknowledges that there will be cases that do not fit. In such cases one can include additional files and subfolders to the existing folder structure following common sense. For example one may want to include eye tracking data in a vendor specific format that is not covered by this standard. The most sensible place to put it is next to the continuous recording file with the same naming scheme but different extensions. The solutions will change from case to case and publicly available datasets will be reviewed to include common data types in the future releases of the BIDS spec.

## 3.4 Source vs. raw vs. derived data

BIDS in its current form is designed to harmonize and describe raw (unprocessed or minimally processed due to file format conversion) data. During analysis such data will be transformed and partial as well as final results will be saved. Derivatives of the raw data (other than products of DICOM to NIfTI conversion) MUST be kept separate from the raw data. This way one can protect the raw data from accidental changes by file permissions. In addition it is easy to distinguish partial results from the raw data and share the latter. Similar rules apply to source data which is defined as data before harmonization and/or file format conversion (for example E-Prime event logs or DICOM files).

This specification currently does not go into details of recommending a particular naming scheme for including different types of source data (raw event logs, parameter files, etc. before conversion to BIDS) and data derivatives (correlation maps, brain masks, contrasts maps, etc.). However, in the case that these data are to be included:

1.  These data MUST be kept in separate "sourcedata" and “derivatives” folders each with a similar folder structure as presented below for the BIDS-managed data. For example: derivatives/fmriprep/sub-01/ses-pre/sub-01_ses-pre_mask.nii.gz or sourcedata/sub-01/ses-pre/func/sub-01_ses-pre_task-rest_bold.dicom.tgz or sourcedata/sub-01/ses-pre/func/MyEvent.sce.

2. A README file SHOULD be found at the root of the "sourcedata" or the “derivatives” folder (or both). This file should describe the nature of the raw data or the derived data. In the case of the existence of a “derivatives” folder, we RECOMMEND to include details about the software stack and settings used to generate the results. Non-imaging objects to improve reproducibility are encouraged (scripts, setting files, etc.).

3. We RECOMMEND to include the PDF print-out with the actual sequence parameters generated by the scanner in the  "sourcedata" folder.

## 3.5 The Inheritance Principle

Any metadata file (.json, .bvec, .tsv, etc.) may be defined at any directory level, but no more than one applicable file may be defined at a given level (Example 1).  The values from the top level are inherited by all lower levels unless they are overridden by a file at the lower level. For example, sub-*_task-rest_bold.json may be specified at the participant level, setting TR to a specific value. If one of the runs has a different TR than the one specified in that file, another sub*_task-rest_bold.json file can be placed within that specific series directory specifying the TR for that specific run.

There is no notion of "unsetting" a key/value pair. For example if there is a JSON file corresponding to particular participant/run defining a key/value and there is a JSON file on the root level of the dataset that does not define this key/value it will not be “unset” for all subjects/runs. 

Files for a particular participant can exist only at participant level directory, i.e /dataset/sub-*/[ses-*]/sub-*_T1w.json. Similarly, any  file that is not specific to a participant is to be declared only at top level of dataset for eg: task-sist_bold.json must be placed under /dataset/task-sist_bold.json 

Example 1: Two JSON files at same level that are applicable for NIfTI file. 

      sub-01/

ses-test/

	sub-test_task-overtverbgeneration_bold.json

sub-test_task-overtverbgeneration_run-02_bold.json

	anat/

sub-01_ses-test_T1w.nii.gz

func/

sub-01_ses-test_task-overtverbgeneration_run-01_bold.nii.gz

sub-01_ses-test_task-overtverbgeneration_run-02_bold.nii.gz

In the above example, two JSON files are listed under sub-01/ses-test/, which are each applicable to sub-01_ses-test_task-overtverbgeneration_run-02_bold.nii.gz, violating the constraint that no more than one file may be defined at a given level of the directory structure. Instead task-overtverbgeneration_run-02_bold.json should have been under sub-01/ses-test/func/.

Example 2:  Multiple run and rec with same acquisition (acq) parameters acq-test1

  sub-01/

        anat/

        func/

                 sub-01_task-xyz_acq-test1_run-01_bold.nii.gz

      sub-01_task-xyz_acq-test1_run-02_bold.nii.gz

      sub-01_task-xyz_acq-test1_rec-recon1_bold.nii.gz

      sub-01_task-xyz_acq-test1_rec-recon2_bold.nii.gz

      sub-01_task-xyz_acq-test1_bold.json

For the above example, all NIfTI files are acquired with same scanning parameters (acq-test1). Hence a JSON file describing the acq parameters will apply to different runs and rec files.  Also if the JSON file (task-xyz_acq-test1_bold.json) is defined at dataset top level  directory, it  will be applicable to all task runs with test1 acquisition parameter. 

Case 2:  Multiple json files at different levels for same task and acquisition parameters

       sub-01/

   task-xyz_acq-test1_bold.json

         anat/

         func/

                  sub-01/func/sub-01_task-xyz_acq-test1_run-01_bold.nii.gz

      sub-01/func/sub-01_task-xyz_acq-test1_rec-recon1_bold.nii.gz

      sub-01/func/sub-01_task-xyz_acq-test1_rec-recon2_bold.nii.gz

      sub-01/sub-01_task-xyz_acq-test1_bold.json

In the above example, the fields from task-xyz_acq-test1_bold.json file will apply to all bold runs. However, if there is a key with different value in sub-01/func/sub-01_task-xyz_acq-test1_run-01_bold.json , the new value will be applicable for that particular run/task NIfTI file/s. 

## 3.6 Extensions

The BIDS specification can be extended in a backwards compatible way  and will evolve over time. A number of extensions are currently being worked on: 

<table>
  <tr>
    <td>Extension label</td>
    <td>Title</td>
    <td>Moderators/leads</td>
  </tr>
  <tr>
    <td>BEP001</td>
    <td>Structural acquisitions that include multiple contrasts (multi echo, flip angle, inversion time) sequences</td>
    <td>Chris Gorgolewski</td>
  </tr>
  <tr>
    <td>BEP002</td>
    <td>The BIDS Models Specification</td>
    <td>Tal Yarkoni</td>
  </tr>
  <tr>
    <td>BEP003</td>
    <td>Common Derivatives</td>
    <td>Chris Gorgolewski</td>
  </tr>
  <tr>
    <td>BEP004</td>
    <td>Susceptibility Weighted Imaging (SWI)</td>
    <td>looking for a volunteer</td>
  </tr>
  <tr>
    <td>BEP005</td>
    <td>Arterial Spin Labeling (ASL)</td>
    <td>Henk-Jan Mutsaerts and Michael Chappell</td>
  </tr>
  <tr>
    <td>BEP006</td>
    <td>Electroencephalography (EEG)</td>
    <td>Cyril R Pernet and Robert Oostenveld</td>
  </tr>
  <tr>
    <td>BEP008</td>
    <td>Magnetoencephalography (MEG)</td>
    <td>Guiomar Niso</td>
  </tr>
  <tr>
    <td>BEP009</td>
    <td>Positron Emission Tomography (PET)</td>
    <td>Melanie Ganz</td>
  </tr>
  <tr>
    <td>BEP010</td>
    <td>intracranial Electroencephalography (iEEG)</td>
    <td>Dora Hermes and Chris Holdgraf</td>
  </tr>
  <tr>
    <td>BEP011</td>
    <td>The structural preprocessing derivatives</td>
    <td>Andrew Hoopes</td>
  </tr>
  <tr>
    <td>BEP012</td>
    <td>The functional preprocessing derivatives</td>
    <td>Camille Maumet and Chris Markiewicz</td>
  </tr>
  <tr>
    <td>BEP013</td>
    <td>The resting state fMRI derivatives</td>
    <td>Steven Giavasis</td>
  </tr>
  <tr>
    <td>BEP014</td>
    <td>The affine transformations and nonlinear field warps</td>
    <td>looking for a volunteer</td>
  </tr>
  <tr>
    <td>BEP015</td>
    <td>Mapping file</td>
    <td>Eric Earl and Camille Maumet</td>
  </tr>
  <tr>
    <td>BEP016</td>
    <td>The diffusion weighted imaging derivatives</td>
    <td>Franco Pestilli and Oscar Esteban</td>
  </tr>
  <tr>
    <td>BEP017</td>
    <td>Generic BIDS connectivity data schema</td>
    <td>Eugene Duff and Paul McCarthy</td>
  </tr>
  <tr>
    <td>BEP018</td>
    <td>Genetic information</td>
    <td>Cyril R Pernet, Clara Moreau, and Thomas Nichols</td>
  </tr>
  <tr>
    <td>BEP019</td>
    <td>DICOM Metadata</td>
    <td>Satrajit Ghosh</td>
  </tr>
</table>


When an extension reaches maturity it is merged into the main body of the specification. If you would like to contribute to BIDS please consult the [BIDS Contributor Guide](https://docs.google.com/document/d/1pWmEEY-1-WuwBPNy5tDAxVJYQ9Een4hZJM06tQZg8X4/edit?usp=sharing).

All of the ideas that are not backwards compatible and thus will have to wait for BIDS 2.0 are listed [here](https://docs.google.com/document/d/1LEgsMiisGDe1Gv-hBp1EcLmoz7AlKj6VYULUgDD3Zdw/edit#heading=h.o1yeo3xixq7n).

# 4 File Format specification

## 4.1 Imaging files

All imaging data MUST be stored using the NIfTI file format, it is RECOMMENDED to use compressed NIfTI files (.nii.gz), either 1.0 or 2.0 version. Imaging data SHOULD be converted to the NIfTI format using a tool that provides as much of the NIfTI header information (such as orientation and slice timing information) as possible. Since the NIfTI standard offers limited support for the various image acquisition parameters available in DICOM files, we RECOMMEND  users to provide additional meta information extracted from DICOM files in a sidecar JSON file (with the same filename as the .nii[.gz] file, but with a .json extension). Extraction of BIDS compatible metadata can be performed using dcm2nii ([https://www.nitrc.org/projects/dcm2nii/](https://www.nitrc.org/projects/dcm2nii/)) and dicm2nii ([http://www.mathworks.com/matlabcentral/fileexchange/42997-dicom-to-nifti-converter/content/dicm2nii.m](http://www.mathworks.com/matlabcentral/fileexchange/42997-dicom-to-nifti-converter/content/dicm2nii.m)) DICOM to NIfTI converters. A provided validator ([https://github.com/INCF/bids-validator](https://github.com/INCF/bids-validator)) will check for conflicts between the JSON file and the data recorded in the NIfTI header.

## 4.2 Tabular files

Tabular data MUST be saved as tab delimited values (.tsv) files, aka csv files where commas are replaced by tabs. Tabs MUST  be true tab characters and MUST NOT be a series of space characters. Each TSV file MUST start with a header line listing the names of all columns (with the exception for physiological and other continuous acquisition data - see below for details). Names MUST be separated with tabs. String values containing tabs MUST be escaped using double quotes. Missing values MUST be coded as "n/a".

### 4.2.1 Example: (NOTE:  Note that to make the display clearer, the second row does contain two successive tabs, which should not happen in an actual BIDS tsv file. )

onset	duration	response_time	correct	stop_trial	go_trial

200	20		0			n/a		n/a		n/a

Tabular files MAY be optionally accompanied by a simple data dictionary in a JSON format (see below). The data dictionaries MUST have the same name as their corresponding tabular files but with .json extensions. Each entry in the data dictionary has a name corresponding to a column name and the following fields:

* LongName - Long (unabbreviated) name of the column.

* Description - Description of the the column.

* Levels - For  categorical variables: a dictionary of possible values (keys) and their descriptions (values).  

* Units - Measurement units.

* UnitsTermURL - URL pointing to a formal definition of the units used in an ontology available on the web.

* TermURL - URL pointing to a formal definition of this type of data in an ontology available on the web.

### 4.2.2 Example:

{

  "education": {

    "LongName": "Education level",

    "Description": "Education level, self-rated by participant",

    "Levels": {

      "1": "Finished primary school",

      "2": "Finished secondary school",

      "3": "Student at university",

      "4": "Has degree from university"

    }

  },

  "bmi": {

    "LongName": "Body mass index",

    "Units": "kilograms per squared meters",

    "TermURL": "http://purl.bioontology.org/ontology/SNOMEDCT/60621009"

  }

}

## 4.3 Key/value files (dictionaries)

JavaScript Object Notation(JSON) files MUST be used for storing key/value pairs. Extensive documentation of the format can be found here: [http://json.org/](http://json.org/). Several editors have built-in support for JSON syntax highlighting that aids manual creation of such files. An online editor for JSON with built-in validation is available at: [http://jsoneditoronline.org](http://jsoneditoronline.org). JSON files MUST be in UTF-8 encoding.

### 4.3.1 Example:

{

    "RepetitionTime": 3.0,

    "Instruction": "Lie still and keep your eyes open"

}

# 5 Participant names and other labels

BIDS uses custom user defined labels in several situations (naming of participants, sessions, acquisition schemes etc.) Labels MUST only consist of letters (lower or upper case) and/or numbers. If numbers are used we RECOMMEND  zero padding ("01" instead of “1” if you have more than nine subjects) to make alphabetical sorting more intuitive. Please note that sub- prefix is not part of the subject label, but must be included in file names (similarly to other key names).

# 6 Units

# All units MUST be specified as per International System of Units (abbreviated as SI, from the French Système international (d'unités)) unless otherwise specified. In particular:

Elapsed time MUST be expressed in seconds unless otherwise specified. Please note that some DICOM parameters have been traditionally expressed in milliseconds. Those need to be converted to seconds.

Frequency should be expressed in Hertz.

Describing dates and timestamps:

* Date time information MUST be expressed in the following format YYYY-MM-DDThh:mm:ss (one of the [ISO8601](https://en.wikipedia.org/wiki/ISO_8601) date-time formats). For example: 2009-06-15T13:45:30

* Time stamp information MUST be expressed in the following format: 13:45:30 

* Dates can be shifted by a random number of days for privacy protection reasons. To distinguish real dates from shifted dates always use year 1900 or earlier when including shifted years. For longitudinal studies please remember to shift dates within one subject by the same number of days to maintain the interval information. Example: 1867-06-15T13:45:30

* Age SHOULD be given as the number of years since birth at the time of scanning (or first scan in case of multi session datasets). Using higher accuracy (weeks) should be avoided due to privacy protection.

# 7 Directory structure

Overall directories hierarchy is

* sub-<participant_label>[/ses-<session_label>]/<data_type>/

* [code/]

* [derivatives/]

* [stimuli/]

* [sourcedata/]

where [] depicts OPTIONAL content (the same nomenclature is used throughout the spec). Session level is OPTIONAL, first we detail single session example. See below (section 9) for an example with multiple sessions.

## 7.1 Single session example

This is an example of the folder and file structure. Because there is only one session, the session level is not required by the format. For details on individual files see descriptions in the next section:

* **sub-control01**

    * **anat**

        * sub-control01_T1w.nii.gz

        * sub-control01_T1w.json

        * sub-control01_T2w.nii.gz

        * sub-control01_T2w.json

    * **func**

        * sub-control01_task-nback_bold.nii.gz

        * sub-control01_task-nback_bold.json

        * sub-control01_task-nback_events.tsv

        * sub-control01_task-nback_physio.tsv.gz

        * sub-control01_task-nback_physio.json

        * sub-control01_task-nback_sbref.nii.gz

    * **dwi**

        * sub-control01_dwi.nii.gz

        * sub-control01_dwi.bval

        * sub-control01_dwi.bvec

    * **fmap**

        * sub-control01_phasediff.nii.gz

        * sub-control01_phasediff.json

        * sub-control01_magnitude1.nii.gz

    * sub-control01_scans.tsv

    * Additional files and folders containing raw data may be added as needed for special cases.  They should be named using all lowercase with a name that reflects the nature of the scan (e.g., "calibration").  Naming of files within the directory should follow the same scheme as above (e.g., “sub-control01_calibration_Xcalibration.nii.gz”)

* **code**

    * deface.py

* **derivatives**

    * README

* participants.tsv

* dataset_description.json

* README

* CHANGES

# 8 Detailed file descriptions

## 8.1 Dataset description

Template: dataset_description.json, README, and CHANGES

A JSON file describing the dataset. Every dataset MUST include this file with the following mandatory fields: 

* Name: name of the dataset

* BIDSVersion: The version of the BIDS standard that was used

In addition the following fields MAY be provided:

* License: what license is this dataset distributed under? The use of license name abbreviations is suggested for specifying a license. A list of common licenses with suggested abbreviations can be found in A[ppendix I](#heading=h.8bxgvc9yrtig).

* Authors: List of individuals who contributed to the creation/curation of the dataset

* Acknowledgements: who should be acknowledge in helping to collect the data

* HowToAcknowledge:Instructions how researchers using this dataset should acknowledge the original authors. This field can also be used to define a publication that should be cited in publications that use the dataset,

* Funding:List of sources of funding (grant numbers)

* ReferencesAndLinks: a list of references to publication that contain information on the dataset, or links.

* DatasetDOI: the Document Object Identifier of the dataset (not the corresponding paper).

### 8.1.1 Example:

{

    "Name": "The mother of all experiments",

    "BIDSVersion":  "1.0.1",

    "License": "CC0",

    "Authors": ["Paul Broca", "Carl Wernicke"],

    "Acknowledgements": "Special thanks to Korbinian Brodmann for help in formatting this dataset in BIDS. We thank Alan Lloyd Hodgkin and Andrew Huxley for helpful comments and discussions about the experiment and manuscript; Hermann Ludwig Helmholtz for administrative support; and Claudius Galenus for providing data for the medial-to-lateral index analysis.",

    "HowToAcknowledge": "Please cite this paper: https://www.ncbi.nlm.nih.gov/pubmed/001012092119281",

    "Funding": ["National Institute of Neuroscience Grant F378236MFH1", "National Institute of Neuroscience Grant 5RMZ0023106"],

    "ReferencesAndLinks": ["https://www.ncbi.nlm.nih.gov/pubmed/001012092119281", "Alzheimer A., & Kraepelin, E. (2015). Neural correlates of presenile dementia in humans. Journal of Neuroscientific Data, 2, 234001. http://doi.org/1920.8/jndata.2015.7"],

    "DatasetDOI": "10.0.2.3/dfjj.10"

}

In addition a free form text file (README) describing the dataset in more details SHOULD be provided. Version history of the dataset (describing changes, updates and corrections) MAY be provided in a form of a CHANGES text file. This file MUST follow the following the CPAN Changelog convention: [http://search.cpan.org/~haarg/CPAN-Changes-0.400002/lib/CPAN/Changes/Spec.pod](http://search.cpan.org/~haarg/CPAN-Changes-0.400002/lib/CPAN/Changes/Spec.pod). README and CHANGES files MUST be either in ASCII or UTF-8 encoding.

### 8.1.2 Example:

1.0.1 2015-08-27  

  - Fixed slice timing information.

1.0.0 2015-08-17

  - Initial release.

## 8.2 Code

Template: 

code/*

Source code of scripts that were used to prepare the dataset (for example if it was anonymized or defaced) MAY be stored here. (NOTE:  Storing actual source files with the data is preferred over links to external source repositories to maximize long term preservation (which would suffer if an external repository would not be available anymore).) Extra care should be taken to avoid including original IDs or any identifiable information with the source code. There are no limitations or recommendation on the language and or code organization of these scripts at the moment.

## 8.3 Magnetic Resonance Imaging data

### 8.3.1 Common metadata fields

MR Data described in  sections 8.3.x share the following RECOMMENDED metadata fields (stored in sidecar JSON files). MRI acquisition parameters are divided into several categories based on[ "A checklist for fMRI acquisition methods reporting in the literature"](https://thewinnower.com/papers/977-a-checklist-for-fmri-acquisition-methods-reporting-in-the-literature) by Ben Inglis:

* Scanner Hardware

    * Manufacturer: Manufacturer of the equipment that produced the composite instances. Corresponds to DICOM Tag 0008, 0070 "Manufacturer” .

    * ManufacturersModelName: Manufacturer`s model name of the equipment that produced the composite instances. Corresponds to DICOM Tag 0008, 1090 "Manufacturers Model Name".

    * MagneticFieldStrength: Nominal field strength of MR magnet in Tesla. Corresponds to DICOM Tag 0018,0087 "Magnetic Field Strength" .

    * DeviceSerialNumber: The serial number of the equipment that produced the composite instances. Corresponds to DICOM Tag 0018, 1000 "DeviceSerialNumber”. A pseudonym can also be used to prevent the equipment from being identifiable, so long as each pseudonym is unique within the dataset.

    * StationName: Institution defined name of the machine that produced the composite instances. Corresponds to DICOM Tag 0008, 1010 "Station Name"

    * SoftwareVersions: Manufacturer's designation of software version of the equipment that produced the composite instances. Corresponds to DICOM Tag 0018, 1020 "Software Versions".

    * HardcopyDeviceSoftwareVersion:** (Deprecated)** Manufacturer's designation of the software of the device that created this Hardcopy Image (the printer). Corresponds to DICOM Tag 0018, 101A "Hardcopy Device Software Version".

    * ReceiveCoilName: Information describing the receiver coil (Note: This isn't a consistent field name across vendors. This name is the dcmstack output from a GE dataset, but it doesn’t seem to be simply coded into the dcmstack output for a Siemens scan). This doesn’t correspond to a term in the DICOM ontology .

    * ReceiveCoilActiveElements: Information describing the active/selected elements of the receiver coil.  Probably also not a term in the DICOM ontology.  For Siemens, coil elements are typically activated in "blocks", and Siemen's calls this the “Coil String” in its private DICOM fields.  The “Coil String” specifying the activated blocks could go here (e.g,. “HEA;HEP” for the Siemens standard 32 ch coil when both blocks are activated).

    * GradientSetType: It should be possible to infer the gradient coil from the scanner model. If not,*e.g.* because of a custom upgrade or use of a gradient insert set, then the specifications of the actual gradient coil should be reported independently.

    * MRTransmitCoilSequence: This is a relevant field if a non-standard transmit coil is used. Corresponds to DICOM Tag 0018, 9049 "MR Transmit Coil Sequence".

    * MatrixCoilMode: (If used) A method for reducing the number of independent channels by combining in analog the signals from multiple coil elements. There are typically different default modes when using un-accelerated or accelerated (*e.g.* GRAPPA, SENSE) imaging.

    * CoilCombinationMethod:Almost all fMRI studies using phased-array coils use root-sum-of-squares (rSOS) combination, but other methods exist. The image reconstruction is changed by the coil combination method (as for the matrix coil mode above), so anything non-standard should be reported.

* Sequence Specifics

    * PulseSequenceType: A general description of the pulse sequence used for the scan (i.e. MPRAGE, Gradient Echo EPI, Spin Echo EPI, Multiband gradient echo EPI).

    * ScanningSequence: Description of the type of data acquired. Corresponds to DICOM Tag 0018, 0020 "Sequence Sequence".

    * SequenceVariant: Variant of the ScanningSequence. Corresponds to DICOM Tag 0018, 0021 "Sequence Variant".

    * ScanOptions: Parameters of ScanningSequence. Corresponds to DICOM Tag 0018, 0022 "Scan Options".

    * SequenceName: Manufacturer's designation of the sequence name. Corresponds to DICOM Tag 0018, 0024 "Sequence Name".

    * PulseSequenceDetails: Information beyond pulse sequence type that identifies the specific pulse sequence used (i.e. "Standard Siemens Sequence distributed with the VB17 software," "Siemens WIP ### version #.##,” or “Sequence written by X using a version compiled on MM/DD/YYYY”).

* In-Plane Spatial Encoding

    * NumberShots: The number of RF excitations need to reconstruct a slice or volume. Please mind that  this is not the same as Echo Train Length which denotes the number of lines of k-space collected after an excitation. 

    * ParallelReductionFactorInPlane: The parallel imaging (e.g, GRAPPA) factor. Use the denominator of the fraction of k-space encoded for each slice. For example, 2 means half of k-space is encoded. Corresponds to DICOM Tag 0018, 9069 "Parallel Reduction Factor In-plane".

    * ParallelAcquisitionTechnique: The type of parallel imaging used (e.g. GRAPPA, SENSE). Corresponds to DICOM Tag 0018, 9078 "Parallel Acquisition Technique". 

    * PartialFourier: The fraction of partial Fourier information collected. Corresponds to DICOM Tag 0018, 9081 "Partial Fourier”.

    * PartialFourierDirection: The direction where only partial Fourier information was collected. Corresponds to DICOM Tag 0018, 9036 "Partial Fourier Direction".

    * PhaseEncodingDirection: Possible values: "i", “j”, “k”, “i-”, “j-”, “k-”. The letters “i”, “j”, “k” correspond to the first, second and third axis of the data in the NIFTI file. The polarity of the phase encoding is assumed to go from zero index to maximum index unless '-' sign is present (then the order is reversed - starting from the highest index instead of zero). PhaseEncodingDirection is defined as the direction along which phase is was modulated which may result in visible distortions. Note that this is not the same as the DICOM term InPlanePhaseEncodingDirection which can have “ROW” or “COL” values. **This parameter is REQUIRED if corresponding fieldmap data is present or when using multiple runs with different phase encoding directions (which can be later used for field inhomogeneity correction).**

    * EffectiveEchoSpacing: The "effective" sampling interval, specified in seconds, between lines in the phase-encoding direction, defined based on the size of the **reconstructed image** in the phase direction.  It is frequently, but incorrectly, referred to as  “dwell time” (see DwellTime parameter below for actual dwell time).  It is  required for unwarping distortions using field maps**. **Note that beyond just in-plane acceleration, a variety of other manipulations to the phase encoding need to be accounted for properly, including partial fourier, phase oversampling, phase resolution, phase field-of-view and interpolation. (NOTE:  Conveniently, for Siemen's data, this value is easily obtained as 1/[BWPPPE * ReconMatrixPE], where BWPPPE is the “BandwidthPerPixelPhaseEncode in DICOM tag (0019,1028) and  ReconMatrixPE is the size of the actual reconstructed data in the phase direction (which is NOT reflected in a single DICOM tag for all possible aforementioned scan manipulations). See here and here.) **This parameter is REQUIRED if corresponding fieldmap data is present.** 

    * TotalReadoutTime:This is actually the "effective" total readout time , defined as the readout duration, specified in seconds, that would have generated data with the given level of distortion.  It is NOT the actual, physical duration of the readout train.  If EffectiveEchoSpacing has been properly computed, it is just EffectiveEchoSpacing * (ReconMatrixPE - 1). (NOTE:  We use the “FSL definition”, i.e, the time between the center of the first “effective” echo and the center of the last “effective” echo.) . **This parameter is REQUIRED if corresponding “field/distortion” maps acquired with opposing phase encoding directions are present  (see 8.9.4).**

* Timing Parameters:

    * EchoTime: The echo time (TE) for the acquisition, specified in seconds. **This parameter is REQUIRED if corresponding fieldmap data is present or the data comes from a multi echo sequence.** Corresponds to DICOM Tag 0018, 0081 "Echo Time"  (please note that the DICOM term is in milliseconds not seconds).

    * InversionTime: The inversion time (TI) for the acquisition, specified in seconds. Inversion time is the time after the middle of inverting RF pulse to middle of excitation pulse to detect the amount of longitudinal magnetization. Corresponds to DICOM Tag 0018, 0082 "Inversion Time"  (please note that the DICOM term is in milliseconds not seconds).

    * SliceTiming: The time at which each slice was acquired within each volume (frame) of  the acquisition.  Slice timing is not slice order -- rather, it  is a list of times (in JSON format) containing the time (in seconds) of each slice acquisition in relation to the beginning of volume acquisition.  The list goes through the slices along the slice axis in the slice encoding dimension (see below). Note that to ensure the proper interpretation of the SliceTiming field, it is important to check if the (optional) SliceEncodingDirection exists. In particular,  if SliceEncodingDirection is negative, the entries in SliceTiming are defined in reverse order with respect to the slice axis (i.e., the final entry in the SliceTiming list is the time of acquisition of slice 0). **This parameter is REQUIRED for sparse sequences that do not have the DelayTime field set.** **In addition without this parameter slice time correction will not be possible.**

    * SliceEncodingDirection: Possible values: "i", “j”, “k”, “i-”, “j-”, “k-” (the axis of the NIfTI data along which slices were acquired, and the direction in which SliceTiming is  defined with respect to). "i", "j", "k" identifiers correspond to the first, second and third axis of the data in the NIfTI file. A '-' sign indicates that the contents of SliceTiming are defined in reverse order -- that is, the first entry corresponds to the slice with the largest index, and the final entry corresponds to slice index zero. When present ,the axis defined by SliceEncodingDirection  needs to be consistent with the ‘slice_dim’ field in the NIfTI header. When absent, the entries in SliceTiming must be in the order of increasing slice index as defined by the NIfTI header. 

    * DwellTime:  Actual dwell time (**in seconds**) of the receiver per point in the readout direction, including any oversampling.  For Siemens, this corresponds to DICOM field (0019,1018) (in ns).   This value is necessary for the (optional) readout distortion correction of anatomicals in the HCP Pipelines.  It also usefully provides a handle on the readout bandwidth, which isn't captured in the other metadata tags.  Not to be confused with "EffectiveEchoSpacing", and the frequent mislabeling of echo spacing (which is spacing in the phase encoding direction) as “dwell time” (which is spacing in the readout direction).

* RF & Contrast

    * FlipAngle: Flip angle for the acquisition, specified in degrees. Corresponds to: DICOM Tag 0018, 1314 "Flip Angle".

* Slice Acceleration

    * MultibandAccelerationFactor: The multiband factor, for multiband acquisitions.

* Institution information

    * InstitutionName: The name of the institution in charge of the equipment that produced the composite instances. Corresponds to DICOM Tag 0008, 0080 "InstitutionName”.

    * InstitutionAddress: The address of the institution in charge of the equipment that produced the composite instances. Corresponds to DICOM Tag 0008, 0081 "InstitutionAddress”.

    * InstitutionalDepartmentName: The department in the  institution in charge of the equipment that produced the composite instances. Corresponds to DICOM Tag 0008, 1040 "Institutional Department Name”.

When adding additional metadata please use the camelcase version of [DICOM ontology terms](http://neurolex.org/wiki/Category:DICOM_term) whenever possible.

### 8.3.2 Anatomy imaging data

Template:

sub-<participant_label>/[ses-<session_label>/]

anat/

sub-<participant_label>[_ses-<session_label>][_acq-<label>][_ce-<label>][_rec-<label>][_run-<index>][_mod-<label>]_<modality_label>.nii[.gz]

Anatomical (structural) data acquired for that participant. Currently supported modalities include:

<table>
  <tr>
    <td>Name</td>
    <td>modality_label</td>
    <td>Description</td>
  </tr>
  <tr>
    <td>T1 weighted</td>
    <td>T1w</td>
    <td></td>
  </tr>
  <tr>
    <td>T2 weighted</td>
    <td>T2w</td>
    <td></td>
  </tr>
  <tr>
    <td>T1 Rho map</td>
    <td>T1rho</td>
    <td>Quantitative T1rho brain imaging http://www.ncbi.nlm.nih.gov/pubmed/24474423
                 	http://www.ncbi.nlm.nih.gov/pmc/articles/PMC4346383/
</td>
  </tr>
  <tr>
    <td>T1 map</td>
    <td>T1map</td>
    <td>quantitative T1 map</td>
  </tr>
  <tr>
    <td>T2 map</td>
    <td>T2map</td>
    <td>quantitative T2 map</td>
  </tr>
  <tr>
    <td>T2*</td>
    <td>T2star</td>
    <td>High resolution T2* image</td>
  </tr>
  <tr>
    <td>FLAIR</td>
    <td>FLAIR</td>
    <td></td>
  </tr>
  <tr>
    <td>FLASH</td>
    <td>FLASH</td>
    <td></td>
  </tr>
  <tr>
    <td>Proton density</td>
    <td>PD</td>
    <td></td>
  </tr>
  <tr>
    <td>Proton density map</td>
    <td>PDmap</td>
    <td></td>
  </tr>
  <tr>
    <td>Combined PD/T2</td>
    <td>PDT2</td>
    <td></td>
  </tr>
  <tr>
    <td>Inplane T1</td>
    <td>inplaneT1</td>
    <td>T1-weighted anatomical image matched to functional acquisition</td>
  </tr>
  <tr>
    <td>Inplane T2</td>
    <td>inplaneT2</td>
    <td>T2-weighted anatomical image matched to functional acquisition</td>
  </tr>
  <tr>
    <td>Angiography</td>
    <td>angio</td>
    <td></td>
  </tr>
  <tr>
    <td>Defacing mask</td>
    <td>defacemask</td>
    <td>Mask used for defacing. The optional "mod-<modality_label>" can be used to distinguish between different modalities referenced by a defacemask image.</td>
  </tr>
</table>


If several scans of the same modality are  acquired they MUST be indexed with a suffix: _run-01, _run-02, _run-03 etc. When there is only one scan of a given type the suffix MAY be omitted. Please note that diffusion imaging data is stored elsewhere (see below). 

The OPTIONAL "acq-<label>" key/value pair corresponds to a custom label the user MAY use to distinguish a different set of parameters used for acquiring the same modality. For example this should be used when a study includes two T1w images - one full brain low resolution and and one restricted field of view but high resolution. In such case two files could have the following names: sub-01_acq-highres_T1w.nii.gz and sub-01_acq-lowres_T1w.nii.gz,however the user is free to choose any other label than “highres” and “lowres” as long as they are consistent across subjects and sessions. In case different sequences are used to record the same modality (e.g. RARE and FLASH for T1w) this field can also be used to make that distinction. At what level of detail to make the distinction (e.g. just between RARE and FLASH, or between RARE, FLASH, and FLASHsubsampled) remains at the discretion of the researcher.

Similarly the OPTIONAL "ce-<label>" key/value can be used to distinguish sequences using different contrast enhanced images. The label is the name of the contrast agent. The key “ContrastBolusIngredient” MAY be also be added in the JSON file, with the same label. 

Similarly the OPTIONAL "rec-<label>" key/value can be used to distinguish different reconstruction algorithms (for example ones using motion correction). The OPTIONAL “mod-<label>” corresponds to modality label for eg: T1w, inplaneT1, referenced by a defacmask image. Eg: sub-01_mod-T1w_defacemask.nii.gz.

Some meta information about the acquisition MAY be provided in an additional JSON file. See **Common MR metadata fields** for a list of terms and their definitions. There are also some OPTIONAL JSON fields specific to anatomical scans:

* ContrastBolusIngredient:  Active ingredient of agent.  Values MUST be one of: IODINE, GADOLINIUM, CARBON DIOXIDE, BARIUM. Corresponds to DICOM Tag 0018,1048.

### 8.3.3 Task (including resting state) imaging data

Template:

sub-<participant_label>/[ses-<session_label>/]

func/

     sub-<participant_label>[_ses-<session_label>]_task-<task_label>[_acq-<label>][_rec-<label>][_run-<index>][_echo-<index>]_bold.nii[.gz]

Imaging data acquired during BOLD imaging. This includes but is not limited to task based fMRI **as well as resting state fMRI (i.e. rest is treated as another task)**. For task based fMRI a corresponding task events file (see below) MUST be provided (please note that this file is not necessary for resting state scans).  For multiband acquisitions, one MAY also save the single-band reference image as type "sbref" (e.g. sub-control01_task-nback_sbref.nii.gz).

Each task has a unique label MUST only include of letters and/or numbers (other characters including spaces and underscores are not allowed). Those labels MUST be consistent across subjects and sessions. 

If more than one run of the same task has been acquired a key/value pair: _run-01, _run-02, _run-03 etc. MUST be used. If only one run was acquired the suffix can be omitted. In the context of functional imaging a run is defined as the same task, but in some cases it can mean different set of stimuli (for example randomized order) and participant responses.

The OPTIONAL "acq-<label>" key/value pair corresponds to a custom label one may use to distinguish different set of parameters used for acquiring the same task. For example this should be used when a study includes two resting state images - one single band and one multiband. In such case two files could have the following names: sub-01_task-rest_acq-singleband_bold.nii.gz and sub-01_task-rest_acq-multiband_bold.nii.gz, however the user is MAY choose any other label than “singleband” and “multiband” as long as they are consistent across subjects and sessions and consist only of the legal label characters.

Similarly the optional "rec-<label>" key/value can be used to distinguish different reconstruction algorithms (for example ones using motion correction).

Multi echo data MUST  be split into one file per echo. Each file shares the same name with the exception of the _echo-<index> key/value. For example:

sub-01/

func/

   sub-01_task-cuedSGT_run-1_echo-1_bold.nii.gz

   sub-01_task-cuedSGT_run-1_echo-1_bold.json

	   sub-01_task-cuedSGT_run-1_echo-2_bold.nii.gz

   sub-01_task-cuedSGT_run-1_echo-2_bold.json

   sub-01_task-cuedSGT_run-1_echo-3_bold.nii.gz

   sub-01_task-cuedSGT_run-1_echo-3_bold.json

Please note that the <index> denotes the number/index of the echo not the echo time value which needs to be stored in a separate JSON file (see below).

Some meta information about the acquisition MUST be provided in an additional JSON file. 

Required fields: 

* RepetitionTime: The time in seconds between the beginning of an acquisition of one volume and the beginning of acquisition of the volume following it (TR). Please note that this definition includes time between scans (when no data has been acquired) in case of sparse acquisition schemes. This value needs to be consistent with the 'pixdim[4]' field (after accounting for units stored in ‘xyzt_units’ field) in the NIfTI header. This field is mutually exclusive with VolumeTiming. Corresponds to DICOM Tag 0018, 0080 "Repetition Time" (please note that the DICOM term is in milliseconds not seconds).

* VolumeTiming: The time at which each volume was acquired during the acquisition. It is described using a list of times (in JSON format) referring to the onset of each volume in the BOLD series. The list must have the same length as the BOLD series, and the values must be non-negative and monotonically increasing. This field is mutually exclusive with RepetitionTime and DelayTime. If defined, this requires acquisition time (TA) be defined via either SliceTiming or AcquisitionDuration be defined.

* TaskName: Name of the task. No two tasks should have the same name. Task label ( "task-<task_label>")  included in the file name is derived from this field by removing all non alphanumeric ([a-zA-Z0-9]) characters. For example task name “faces n-back” will corresponds to task label “facesnback”.  An optional but recommended convention is to name resting state task using labels beginning with "rest".

Other RECOMMENDED metadata:

* Timing Parameters:

    * NumberOfVolumesDiscardedByScanner: Number of volumes ("dummy scans") discarded by the user (as opposed to those discarded by the user post hoc) before saving the imaging file. For example, a sequence that automatically discards the first 4 volumes before saving would have this field as 4.  A sequence that doesn't discard dummy scans would have this set to 0.  **Please note that the onsets recorded in the _event.tsv file should always refer to the beginning of the acquisition of the first volume in the corresponding imaging file - independent of the value of NumberOfVolumesDiscardedByScanner field.**

    * NumberOfVolumesDiscardedByUser: Number of volumes ("dummy scans") discarded by the user before including the file in the dataset. If possible, including all of the volumes is strongly recommended. **Please note that the onsets recorded in the _event.tsv file should always refer to the beginning of the acquisition of the first volume in the corresponding imaging file - independent of the value of NumberOfVolumesDiscardedByUser field.**

    * DelayTime: User specified time (in seconds) to delay the acquisition of data for the following volume. If the field is not present it is assumed to be set to zero. Corresponds to Siemens CSA header field lDelayTimeInTR.  **This field is REQUIRED for sparse sequences using the RepetitionTime field that do not have the SliceTiming field set to allowed for accurate calculation of  "acquisition time". This field is mutually exclusive with VolumeTiming.**

    * AcquisitionDuration: Duration (in seconds) of volume acquisition. Corresponds to DICOM Tag 0018,9073 "Acquisition Duration". **This field is REQUIRED for sequences that are described with the VolumeTiming field and that not have the SliceTiming field set to allowed for accurate calculation of  "acquisition time". This field is mutually exclusive with RepetitionTime.**

* fMRI task information

    * Instructions: Text of the instructions given to participants before the scan. This is especially important in context of resting state fMRI and distinguishing between eyes open and eyes closed paradigms.

    * TaskDescription: Longer description of the task.

    * CogAtlasID: URL of the corresponding [Cognitive Atlas](http://www.cognitiveatlas.org/) Task term.

    * CogPOID: URL of the corresponding [CogPO](http://www.cogpo.org/) term.

See **[8.3.1.** ](#heading=h.5u721tt1h9pe)**[Common MR metadata field**s](#heading=h.5u721tt1h9pe) for a list of additional terms and their definitions.

#### 8.3.3.1 Example:

sub-control01/

func/

sub-control01_task-nback_bold.json

{

    "TaskName": "N Back",

    "RepetitionTime": 0.8,

    "EchoTime": 0.03,

    "FlipAngle": 78,

    "SliceTiming": [0.0, 0.2, 0.4, 0.6, 0.0, 0.2, 0.4, 0.6, 0.0, 0.2, 0.4, 0.6, 0.0, 0.2, 0.4, 0.6],

    "MultibandAccelerationFactor": 4,

    "ParallelReductionFactorInPlane": 2,

    "PhaseEncodingDirection": "j",

    "InstitutionName": "Stanford University",    "InstitutionAddress: "450 Serra Mall, Stanford, CA 94305-2004, USA",    "DeviceSerialNumber": "11035"

}

If this information is the same for all participants, sessions and runs it can be provided in task-<task_label>_bold.json (in the root directory of the dataset). However, if the information differs between subjects/runs it can be specified in the sub-<participant_label>/func/sub-<participant_label>_task-<task_label>[_acq-<label>][_run-<index>]_bold.json file. If both files are specified fields from the file corresponding to a particular participant, task and run takes precedence.

### 8.3.4 Diffusion imaging data

Template:

sub-<participant_label>/[ses-<session_label>/]

dwi/

sub-<participant_label>[_ses-<session_label>][_acq-<label>][_run-<index>]_dwi.nii[.gz]

sub-<participant_label>/[ses-<session_label>/]

dwi/

sub-<participant_label>[_ses-<session_label>][_acq-<label>][_run-<index>]_dwi.bval

sub-<participant_label>/[ses-<session_label>/]

dwi/

sub-<participant_label>[_ses-<session_label>][_acq-<label>][_run-<index>]_dwi.bvec

sub-<participant_label>/[ses-<session_label>/]

dwi/

sub-<participant_label>[_ses-<session_label>][_acq-<label>][_run-<index>]_dwi.json

Diffusion-weighted imaging data acquired for that participant. The optional "acq-<label>" key/value pair corresponds to a custom label the user may use to distinguish different set of parameters. For example this should be used when a study includes two diffusion images - one single band and one multiband. In such case two files could have the following names: sub-01_acq-singleband_dwi.nii.gz and sub-01_acq-multiband_dwi.nii.gz, however the user is free to choose any other label than “singleband” and “multiband” as long as they are consistent across subjects and sessions.

For multiband acquisitions, one can also save the single-band reference image as type "sbref" (e.g. dwi/sub-control01_sbref.nii[.gz]).

The bvec and bval files are in the FSL format (NOTE:  http://fsl.fmrib.ox.ac.uk/fsl/fsl4.0/fdt/fdt_dtifit.html): The bvec files contain 3 rows with n space-delimited floating-point numbers (corresponding to the n volumes in the relevant NIfTI file). The first row contains the x elements, the second row contains the y elements and third row contains the z elements of a unit vector in the direction of the applied diffusion gradient, where the i-th elements in each row correspond together to the i-th volume with [0,0,0] for non-diffusion-weighted volumes.

#### 8.3.4.1 bvec example:

0 0 0.021828 -0.015425 -0.70918 -0.2465 

0 0 0.80242 0.22098 -0.00063106 0.1043 

0 0 -0.59636 0.97516 -0.70503 -0.96351 

The bval file contains the b-values (in s/mm2 ) corresponding to the volumes in the relevant NIfTI file), with 0 designating non-diffusion-weighted volumes, space-delimited.  

#### 8.3.4.2 bval example:

0 0 2000 2000 1000 1000

.bval and .bvec files can be saved on any level of the directory structure and thus define those values for all sessions and/or subjects in one place (see Inheritance principle).

See **Common MR metadata fields** for a list of additional terms that can be included in the corresponding JSON file.

Example JSON file:

#### 8.3.4.3 JSON example:

{

    "PhaseEncodingDirection": "j-",

    "TotalReadoutTime": 0.095

}

### 8.3.5 Fieldmap data

Data acquired to correct for B0 inhomogeneities can come in different forms. The current version of this standard considers four different scenarios. Please note that in all cases fieldmap data can be linked to a specific scan(s) it was acquired for by filling the IntendedFor field in the corresponding JSON file. For example:

{

   "IntendedFor": "func/sub-01_task-motor_bold.nii.gz"

}

The IntendedFor field may contain one or more filenames with paths relative to the subject subfolder. The path needs to use forward slashes instead of backward slashes.  Here's an example with multiple target scans:

{

   "IntendedFor": ["ses-pre/func/sub-01_task-motor_run-01_bold.nii.gz",

                   "ses-post/func/sub-01_task-motor_run-01_bold.nii.gz"]

}

The IntendedFor field is optional and in case the fieldmaps do not correspond to any particular scans it does not have to be filled.

Multiple fieldmaps can be stored. In such case the "_run-01", “_run-02” should be used. The optional “acq-<label>” key/value pair corresponds to a custom label the user may use to distinguish different set of parameters.

#### 8.3.5.1 Case 1: Phase difference image and at least one magnitude image

Template:

sub-<participant_label>/[ses-<session_label>/]

fmap/

sub-<label>[_ses-<session_label>][_acq-<label>][_run-<run_index>]_phasediff.nii[.gz]

sub-<participant_label>/[ses-<session_label>/]

fmap/

sub-<label>[_ses-<session_label>][_acq-<label>][_run-<run_index>]_phasediff.json

sub-<participant_label>/[ses-<session_label>/]

fmap/

sub-<label>[_ses-<session_label>][_acq-<label>][_run-<run_index>]_magnitude1.nii[.gz]

**(optional)**

sub-<participant_label>/[ses-<session_label>/]

fmap/

sub-<label>[_ses-<session_label>][_acq-<label>][_run-<run_index>]_magnitude2.nii[.gz]

This is a common output for build in fieldmap sequence on Siemens scanners. In this particular case the sidecar JSON file has to define the Echo Times of the two phase images used to create the difference image. For example:

{

    "EchoTime1": 0.00600,

    "EchoTime2": 0.00746,

    "IntendedFor": "func/sub-01_task-motor_bold.nii.gz"

}

#### 8.3.5.2 Case 2: Two phase images and two magnitude images

Template:

sub-<participant_label>/[ses-<session_label>/]

fmap/

sub-<label>[_ses-<session_label>][_acq-<label>][_run-<run_index>]_phase1.nii[.gz]

sub-<participant_label>/[ses-<session_label>/]

fmap/

sub-<label>[_ses-<session_label>][_acq-<label>][_run-<run_index>]_phase1.json

sub-<participant_label>/[ses-<session_label>/]

fmap/

sub-<label>[_ses-<session_label>][_acq-<label>][_run-<run_index>]_phase2.nii[.gz]

sub-<participant_label>/

fmap/

sub-<label>[_ses-<session_label>][_acq-<label>][_run-<run_index>]_phase2.json

sub-<participant_label>/[ses-<session_label>/]

fmap/

sub-<label>[_ses-<session_label>][_acq-<label>][_run-<run_index>]_magnitude1.nii[.gz]

sub-<participant_label>/[ses-<session_label>/]

fmap/

sub-<label>[_ses-<session_label>][_acq-<label>][_run-<run_index>]_magnitude2.nii[.gz]

Similar to the case above, but instead of a precomputed phase difference map two separate phase images are presented. The two sidecar JSON file need to specify corresponding EchoTime values. For example:

{

    "EchoTime": 0.00746,

    "IntendedFor": "func/sub-01_task-motor_bold.nii.gz"

}

#### 8.3.5.3 Case 3: A single, real fieldmap image (showing the field inhomogeneity in each voxel)

Template:

sub-<participant_label>/[ses-<session_label>/]

fmap/

sub-<label>[_ses-<session_label>][_acq-<label>][_run-<run_index>]_magnitude.nii[.gz]

sub-<participant_label>/[ses-<session_label>/]

fmap/

sub-<label>[_ses-<session_label>][_acq-<label>][_run-<run_index>]_fieldmap.nii[.gz]

sub-<participant_label>/[ses-<session_label>/]

fmap/

sub-<label>[ses-<session_label>][_acq-<label>][_run-<run_index>]_fieldmap.json

In some cases (for example GE) the scanner software will output a precomputed fieldmap denoting the B0 inhomogeneities along with a magnitude image used for coregistration. In this case the sidecar JSON file needs to include the units of the fieldmap. The possible options are: "Hz", “rad/s”, or “Tesla”. For example:

{

    "Units": "rad/s",

    "IntendedFor": "func/sub-01_task-motor_bold.nii.gz"

}

#### 8.3.5.4 Case 4: Multiple phase encoded directions ("pepolar")

Template:

sub-<participant_label>/[ses-<session_label>/]

fmap/

sub-<label>[_ses-<session_label>][_acq-<label>]_dir-<dir_label>[_run-<run_index>]_epi.nii[.gz]

sub-<participant_label>/[ses-<session_label>/]

fmap/

sub-<label>[_ses-<session_label>][_acq-<label>]_dir-<dir_label>[_run-<run_index>]_epi.json

The phase-encoding polarity (PEpolar) technique combines two or more Spin Echo EPI scans with different phase encoding directions to estimate the underlying inhomogeneity/deformation map. Examples of tools using this kind of images are FSL TOPUP, AFNI 3dqwarp and SPM . In such a case, the phase encoding direction is specified in the corresponding JSON file as one of: "i", “j”, “k”, “i-”, “j-, “k-”. For these differentially phase encoded sequences, one also needs to specify the Total Readout Time defined as the time (**in seconds**) from the center of the first echo to the center of the last echo (aka “FSL definition” - see [here](http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/topup/Faq#How_do_I_know_what_phase-encode_vectors_to_put_into_my_--datain_text_file.3F) and [here](http://lcni.uoregon.edu/kb-articles/kb-0003) how to calculate it). For example

{

    "PhaseEncodingDirection": "j-",

    "TotalReadoutTime": 0.095,

    "IntendedFor": "func/sub-01_task-motor_bold.nii.gz"

}

dir_label value can be set to arbitrary alphanumeric label ([a-zA-Z0-9]+ for example "LR" or “AP”) that can help users to distinguish between different files, but should not be used to infer any scanning parameters (such as phase encoding directions) of the corresponding sequence. Please rely only on the JSON file to obtain scanning parameters. _epi files can be a 3D or 4D - in the latter case all timepoints share the same scanning parameters.  To indicate which run is intended to be used with which functional or diffusion scan the IntendedFor field in the JSON file should be used.

## 8.4 Task events

Template: 

sub-<participant_label>/[ses-<session_label>]

func/

<matches>_events.tsv

<matches>_events.json

Where <matches> corresponds to task file name. For example: sub-control01_task-nback. It is also possible to have a single _events.tsv file describing events for all participants and runs (see section "4.2 Inheritance rule"). As with all other tabular data, _events.files may be accompanied by a JSON file describing the columns in detail (see Section 4.2).

The purpose of this file is to describe timing and other properties of events recorded during the scan. Events MAY be either stimuli presented to the participant or participant responses. A single event file MAY include any combination of stimuli and response events. Events MAY overlap in time.  Each task events file REQUIRES a corresponding task imaging data file (but a single events file MAY be shared by multiple imaging data files - see Inheritance rule). The tabular files consists of one row per event and a set of REQUIRED and OPTIONAL columns:

<table>
  <tr>
    <td>Column name</td>
    <td>Description</td>
  </tr>
  <tr>
    <td>onset</td>
    <td>REQUIRED.  Onset (in seconds) of the event  measured from the beginning of the acquisition of the first volume in the corresponding task imaging data file.  If any acquired scans have been discarded before forming the imaging data file, ensure that a time of 0 corresponds to the first image stored. In other words negative numbers in "onset" are allowed.</td>
  </tr>
  <tr>
    <td>duration</td>
    <td>REQUIRED. Duration of the event (measured  from onset) in seconds.  Must always be either zero or positive. A "duration" value of zero implies that the delta function or event is so short as to be effectively modeled as an impulse.</td>
  </tr>
  <tr>
    <td>trial_type</td>
    <td>OPTIONAL. Primary categorisation of each trial to identify them as instances of the experimental conditions. For example: for a response inhibition task, it could take on values "go" and "no-go" to refer to response initiation and response inhibition experimental conditions.</td>
  </tr>
  <tr>
    <td>response_time</td>
    <td>OPTIONAL. Response time measured in seconds. A negative response time can be used to represent preemptive responses and “n/a” denotes a missed response.</td>
  </tr>
  <tr>
    <td>stim_file</td>
    <td>OPTIONAL. Represents the location of the stimulus file (image, video, sound etc.) presented at the given onset time. There are no restrictions on the file formats of the stimuli files, but they should be stored in the /stimuli folder (under the root folder of the dataset; with optional subfolders). The values under the stim_file column correspond to a path relative to “/stimuli”. For example “images/cat03.jpg” will be translated to “/stimuli/images/cat03.jpg”.</td>
  </tr>
  <tr>
    <td>HED</td>
    <td>OPTIONAL. Hierarchical Event Descriptor (HED) Tag. See Appendix II for details.</td>
  </tr>
</table>


An arbitrary number of additional columns can be added. Those allow describing other properties of events that could be later referred in modelling and hypothesis extensions of BIDS.

In case of multi-echo task run, a single _events.tsv file will suffice for all echoes.  

### 8.4.1 Example:

sub-control01/

func/

sub-control01_task-stopsignal_events.tsv

onset		duration	trial_type	response_time  stim_file

1.2		0.6		go		1.435          images/red_square.jpg

5.6		0.6		stop		1.739          images/blue_square.jpg 

References to existing databases can also be encoded using additional columns. Example 2 includes references to the Karolinska Directed Emotional Faces (KDEF) database (NOTE:  http://www.emotionlab.se/resources/kdef):

### 8.4.2 Example:

sub-control01/

func/

sub-control01_task-emoface_events.tsv

onset		duration	trial_type	identifier	database 	response_time

1.2		0.6		afraid	AF01AFAF	kdef		1.435

5.6		0.6		angry		AM01AFAN	kdef		1.739

5.6		0.6		sad		AF01ANSA	kdef		1.739

For multi-echo files events.tsv file is applicable to all echos of particular run.

### 8.4.3 Example:

sub-01_task-cuedSGT_run-01_events.tsv

sub-01_task-cuedSGT_run-01_echo-1_bold.nii.gz

sub-01_task-cuedSGT_run-01_echo-2_bold.nii.gz

sub-01_task-cuedSGT_run-01_echo-3_bold.nii.gz

## 8.5 Physiological and other continuous recordings

Template: 

sub-<participant_label>/[ses-<session_label>/]

func/

<matches>[_recording-<label>]_physio.tsv.gz

and

sub-<participant_label>/[ses-<session_label>/]

func/

<matches>[_recording-<label>]_physio.json

sub-<participant_label>/[ses-<session_label>/]

func/

<matches>[_recording-<label>]_stim.tsv.gz

and

sub-<participant_label>/[ses-<session_label>/]

func/

<matches>[_recording-<label>]_stim.json

Optional: yes

Where <matches> corresponds to task file name without the _bold.nii[.gz] suffix. For example: sub-control01_task-nback_run-01. If the same continuous recording has been used for all subjects (for example in the case where they all watched the same movie) one file can be used and placed in the root directory. For example: task-movie_stim.tsv.gz

Physiological recordings such as cardiac and respiratory signals and other continuous measures (such as parameters of a film or audio stimuli) can be specified using two files: a gzip compressed TSV file with data (without header line) and a JSON for storing start time, sampling frequency, and name of the columns from the TSV. Please note that in contrast to other TSV files this one does not include a header line. Instead the name of columns are specified in the JSON file. This is to improve compatibility with existing software (FSL PNM) as well as make support for other file formats possible in the future.  Start time should be expressed in seconds in relation to the time of** start of acquisition** of the first volume in the corresponding imaging file (negative values are allowed). Sampling frequency should be expressed in Hz. Recordings with different sampling frequencies and/or starting times should be stored in separate files. The following naming conventions should be used for column names:

* cardiac: continuous pulse measurement

* respiratory: continuous breathing measurement

* trigger: continuous measurement of the scanner trigger signal

Any combination of those three can be included as well as any other stimuli related continuous variables (such as low level image properties in a video watching paradigm).

Physiological recordings (including eye tracking) should use the _physio suffix, and signals related to the stimulus should use _stim suffix. For motion parameters acquired from scanner side motion correction please use _physio suffix.

More than one continuous recording file can be included (with different sampling frequencies). In such case use different labels. For example:  _recording-contrast, _recording-saturation. The full file name could then look like this: sub-control01_task-nback_run-02_recording-movie_stim.tsv.gz

For multi-echo data, physio.tsv file is applicable to all echos of particular run.

For eg: 

sub-01_task-cuedSGT_run-01_physio.tsv.gz

sub-01_task-cuedSGT_run-01_echo-1_bold.nii.gz

sub-01_task-cuedSGT_run-01_echo-2_bold.nii.gz

sub-01_task-cuedSGT_run-01_echo-3_bold.nii.gz

### 8.5.1 Example:

sub-control01/

func/

sub-control01_task-nback_physio.tsv.gz (after decompression)

34		110			0

44		112			0

23		100			1

sub-control01/

func/

sub-control01_task-nback_physio.json

{

    "SamplingFrequency": 100.0,

    "StartTime": -22.345,

    "Columns": ["cardiac", "respiratory", "trigger"]

}

## 8.6 Behavioral experiments (with no MRI)

Template: 

sub-<participant_label>/[ses-<session_label>/]

beh/

sub-<participant_label>[_ses-<session_label>]_task-<task_name>_events.tsv

sub-<participant_label>/[ses-<session_label>/]

beh/

sub-<participant_label>[_ses-<session_label>]_task-<task_name>_beh.tsv

sub-<participant_label>/[ses-<session_label>/]

beh/

sub-<participant_label>[_ses-<session_label>]_task-<task_name>_beh.json

sub-<participant_label>/[ses-<session_label>/]

beh/

sub-<participant_label>[_ses-<session_label>]_task-<task_name>_physio.tsv.gz

sub-<participant_label>/[ses-<session_label>/]

beh/

sub-<participant_label>[_ses-<session_label>]_task-<task_name>_physio.json

sub-<participant_label>/[ses-<session_label>/]

beh/

sub-<participant_label>[_ses-<session_label>]_task-<task_name>_stim.tsv.gz

sub-<participant_label>/[ses-<session_label>/]

beh/

sub-<participant_label>[_ses-<session_label>]_task-<task_name>_stim.json

In addition to logs from behavioral experiments performed along MRI acquisitions one can also include data from experiments performed outside of the scanner. The results of those experiments can be stored in the beh folder using the same formats for event timing (_events.tsv), metadata (_beh.json), physiological (_physio.tsv.gz, _physio.json) and other continuous recordings (_stim.tsv.gz, _stim.json) as for tasks performed during MRI acquisitions. Additionally, events files that do not include the mandatory 'onset' and ‘duration’ columns can still be included, but should be labelled _beh.tsv rather than _events.tsv.

## 8.7 Scans file

Template:

sub-<participant_label>/[ses-<session_label>/]

sub-<participant_label>[_ses-<session_label>]_scans.tsv 

Optional: yes

The purpose of this file is to describe timing and other properties of each imaging acquisition sequence (each run .nii[.gz] file) within one session. Each .nii[.gz] file should be described by at most one row. Relative paths to files should be used under a compulsory "filename" header. 

If acquisition time is included it should be under "acq_time" header. Datetime should be expressed in the following format 2009-06-15T13:45:30 (year, month, day, hour (24h), minute, second; this is equivalent to the RFC3339 “date-time” format, time zone is always assumed as local time). For anonymization purposes all dates within one subject should be shifted by a randomly chosen (but common across all runs etc.) number of days. This way relative timing would be preserved, but chances of identifying a person based on the date and time of their scan would be decreased. Dates that are shifted for anonymization purposes should be set to a year 1900 or earlier to clearly distinguish them from unmodified data. Shifting dates is recommended, but not required.

Additional fields can include external behavioural measures relevant to the scan. For example vigilance questionnaire score administered after a resting state scan.

### 8.7.1 Example:

filename							acq_time

func/sub-control01_task-nback_bold.nii.gz	1877-06-15T13:45:30

func/sub-control01_task-motor_bold.nii.gz	1889-06-15T13:55:33

## 8.8 Participant file

Template:

(single session case)

participants.tsv

participants.json

phenotype/<measurement_tool_name>.tsv

phenotype/<measurement_tool_name>.json

Optional: Yes

The purpose of this file is to describe properties of participants such as age, handedness, sex, etc. In case of single session studies this file has one compulsory column participant_id that consists of sub-<participant_label>, followed by a list of optional columns describing participants. Each participant needs to be described by one and only one row.

### 8.8.1 participants.tsv example:

participant_id	age	sex	group

sub-control01	34	M	control

sub-control02	12	F	control

sub-patient01	33	F	patient

If the dataset includes multiple sets of participant level measurements (for example responses from multiple questionnaires) they can be split into individual files separate from participants.tsv. Those measurements should be kept in phenotype/ folder and end with the .tsv extension. They can include arbitrary set of columns, but one of them has to be participant_id with matching sub-<participant_label>.

As with all other tabular data, those additional phenotypic information files can be accompanied by a JSON file describing the columns in detail (see Section 4.2). In addition to the column description, a section describing the measurement tool (as a whole) can be added under the name "MeasurementToolMetadata". This section consists of two keys: "Description" - a free text description of the tool, and "TermURL" a link to an entity in an ontology corresponding to this tool. For example (content of phenotype/acds_adult.json):

{

    "MeasurementToolMetadata": {

        "Description": "Adult ADHD Clinical Diagnostic Scale V1.2",

        "TermURL": "http://www.cognitiveatlas.org/task/id/trm_5586ff878155d"

    },

    "adhd_b": {

        "Description": "B. CHILDHOOD ONSET OF ADHD (PRIOR TO AGE 7)",

        "Levels": {

            "1": "YES",

            "2": "NO"

        }

    },

    "adhd_c_dx": {

        "Description": "As child met A, B, C, D, E and F diagnostic criteria",

        "Levels": {

            "1": "YES",

            "2": "NO"

        }

    },

}

Please note that in this example "MeasurementToolMetadata" includes information about the questionnaire and "adhd_b" and "adhd_c_dx" correspond to individual columns.

In addition to the keys available to describe columns in all tabular files (LongName, Description, Levels, Units, and TermURL) the participants.json file as well as phenotypic files can also include column descriptions with  Derivative field that, when set to true, indicates that values in the corresponding column is a transformation of values from other columns (for example a summary score based on a subset of items in a questionnaire)..

# 9 Longitudinal studies with multiple sessions (visits)

Multiple sessions (visits) are encoded by adding an extra layer of directories and file names in the form of ses-<session_label>. Session label can consist only of alphanumeric characters [a-zA-Z0-9] and should be consistent across subjects. If numbers are used in session labels we recommend using zero padding (for example ses-01, ses-11 instead of ses-1, ses-11). This makes results of alphabetical sorting more intuitive. Acquisition time of session can be defined in the sessions file (see below for details).

The extra session layer (at least one /ses-<session_label> subfolder) should be added for all subjects if at least one subject in the dataset has more than one session. Skipping the session layer for only some subjects in the dataset is not allowed.

* **sub-control01**

    * **ses-predrug**

        * **anat**

            * sub-control01_ses-predrug_T1w.nii.gz

            * sub-control01_ses-predrug_T1w.json

            * sub-control01_ses-predrug_T2w.nii.gz

            * sub-control01_ses-predrug_T2w.json

        * **func**

            * sub-control01_ses-predrug_task-nback_bold.nii.gz

            * sub-control01_ses-predrug_task-nback_bold.json

            * sub-control01_ses-predrug_task-nback_events.tsv

            * sub-control01_ses-predrug_task-nback_cont-physio.tsv.gz

            * sub-control01_ses-predrug_task-nback_cont-physio.json

            * sub-control01_ses-predrug_task-nback_sbref.nii.gz

        * **dwi**

            * sub-control01_ses-predrug_dwi.nii.gz

            * sub-control01_ses-predrug_dwi.bval

            * sub-control01_ses-predrug_dwi.bvec

        * **f****map**

            * sub-control01_ses-predrug_phasediff.nii.gz

            * sub-control01_ses-predrug_phasediff.json

            * sub-control01_ses-predrug_magnitude1.nii.gz

        * sub-control01_ses-predrug_scans.tsv

    * **ses-postdrug**

        * **func**

            * sub-control01_ses-postdrug_task-nback_bold.nii.gz

            * sub-control01_ses-postdrug_task-nback_bold.json

            * sub-control01_ses-postdrug_task-nback_events.tsv

            * sub-control01_ses-postdrug_task-nback_cont-physio.tsv.gz

            * sub-control01_ses-postdrug_task-nback_cont-physio.json

            * sub-control01_ses-postdrug_task-nback_sbref.nii.gz

        * **f****map**

            * sub-control01_ses-postdrug_phasediff.nii.gz

            * sub-control01_ses-postdrug_phasediff.json

            * sub-control01_ses-postdrug_magnitude1.nii.gz

        * sub-control01_ses-postdrug_scans.tsv

    * sub-control01_sessions.tsv

* participants.tsv

* dataset_description.json

* README

* CHANGES

## 9.1 Sessions file

Template:

sub-<participant_label>/

sub-<participant_label>_sessions.tsv

Optional: Yes

In case of multiple sessions there is an option of adding an additional participant key files describing variables changing between sessions. In such case one file per participant should be added. These files need to include compulsory "session_id" column and describe each session by one and only one row. Column names in per participant key files have to be different from group level participant key column names.

### 9.1.1 Multiple sessions example:

session_id		acq_time			systolic_blood_pressure

ses-predrug		2009-06-15T13:45:30	120

ses-postdrug	2009-06-16T13:45:30	100

ses-followup	2009-06-17T13:45:30	110

# 10 Multi-site or multi-center studies

This version of the BIDS specification does not explicitly cover studies with data coming from multiple sites or multiple centers (such extension is planned in BIDS 2.0.0).  There are however ways to model your data without any loss in terms of metadata.

## 10.1 Option 1: Treat each site/center as a separate dataset.

The simplest way of dealing with multiple sites is to treat data from each site as a separate and independent BIDS dataset with a separate participants.tsv and other metadata files. This way you can feed each dataset individually to BIDS Apps and everything should just work.

## 10.2 Option 2: Combining sites/centers into one dataset

Alternatively you can combine data from all sites into one dataset. To identify which site each subjects comes from you can add a "site" column in the participants.tsv file indicating the source site. This solution allows you to analyze all of the subjects together in one dataset. One caveat is that subjects from all sites will have to have unique labels. To enforce that and improve readability you can use a subject label prefix identifying the site. For example sub-NUY001, sub-MIT002, sub-MPG002 etc. Remember that hyphens and underscores are not allowed in subject labels.

 

# 11 Appendix I: Licenses

This section lists a number of common licenses for datasets and defines suggested abbreviations for use in the dataset metadata specifications

<table>
  <tr>
    <td>PD</td>
    <td>Public Domain</td>
    <td>No license required for any purpose; the work is not subject to copyright in any jurisdiction.</td>
  </tr>
  <tr>
    <td>PDDL</td>
    <td>Open Data Commons Public Domain Dedication and License</td>
    <td>License to assign public domain like permissions without giving up the copyright: http://opendatacommons.org/licenses/pddl/</td>
  </tr>
  <tr>
    <td>CC0</td>
    <td>Creative Commons Zero 1.0 Universal.</td>
    <td>Use this if you are a holder of copyright or database rights, and you wish to waive all your interests in your work worldwide: https://creativecommons.org/about/cc0</td>
  </tr>
</table>


# 12 Appendix II: Hierarchical Event Descriptor (HED) Tags

Each event can be assigned one or more Hierarchical Event Descriptor (HED) Tag (see [https://github.com/BigEEGConsortium/HED/wiki/HED-Schema](https://github.com/BigEEGConsortium/HED/wiki/HED-Schema) for more details) under the optional HED column. HED is a controlled vocabulary of terms describing events in a behavioural paradigm. It was originally developed with EEG in mind, but is applicable to all behavioural experiments. Each level of the hierarchical tags are delimited with a forward slash ("/"). Multiple tags are delimited with a comma. Parentheses (brackets) group tags and enable specification of multiple items and their attributes in a single HED string (see section 2.4 in [HED Tagging Strategy Guide](http://www.hedtags.org/downloads/HED%20Tagging%20Strategy%20Guide.pdf) - [http://www.hedtags.org/downloads/HED%20Tagging%20Strategy%20Guide.pdf](http://www.hedtags.org/downloads/HED%20Tagging%20Strategy%20Guide.pdf)). For more information about HED and tools available to validate and match HED strings, please visit [www.hedtags.org](http://www.hedtags.org). 

Since dedicated fields already exist for the overall task classification (CogAtlasID and CogPOID) in the sidecar JSON files HED tags from the Paradigm subcategory should not be used to annotate events.

## 12.1 Example:

sub-control01/

func/

sub-control01_task-emoface_events.tsv

<table>
  <tr>
    <td>onset</td>
    <td>duration</td>
    <td>trial_type</td>
    <td>HED</td>
  </tr>
  <tr>
    <td>1.2</td>
    <td>0.6</td>
    <td>fixationCross</td>
    <td>Event/Category/Experimental stimulus, Event/Label/CrossFix, Event/Description/A cross appears at screen center to serve as a fixation point, Sensory presentation/Visual, Item/Object/2D Shape/Cross, Attribute/Visual/Fixation point, Attribute/Visual/Rendering type/Screen, Attribute/Location/Screen/Center</td>
  </tr>
  <tr>
    <td>5.6</td>
    <td>0.008</td>
    <td>target</td>
    <td>Event/Label/Target image, Event/Description/A white airplane as the RSVP target superimposed on a satellite image is displayed., Event/Category/Experimental stimulus, (Item/Object/Vehicle/Aircraft/Airplane, Participant/Effect/Cognitive/Target, Sensory presentation/Visual/Rendering type/Screen/2D), (Item/Natural scene/Arial/Satellite, Sensory presentation/Visual/Rendering type/Screen/2D)</td>
  </tr>
  <tr>
    <td>500</td>
    <td>0.008</td>
    <td>nontarget</td>
    <td>Event/Label/Non-target image, Event/Description/A non-target image is displayed for about 8 milliseconds, Event/Category/Experimental stimulus, (Item/Natural scene/Arial/Satellite, Participant/Effect/Cognitive/Expected/Non-target, Sensory presentation/Visual/Rendering type/Screen/2D), Attribute/Onset</td>
  </tr>
</table>


Alternatively if the same HED tags apply to a group of events with the same trial_type they can be specified in the corresponding data dictionary (_events.json file) using the following syntax:

## 12.2 Example:

{

  "trial_type": {

    "HED": {

      "fixationCross": "Event/Category/Experimental stimulus, Event/Label/CrossFix, Event/Description/A cross appears at screen center to serve as a fixation point, Sensory presentation/Visual, Item/Object/2D Shape/Cross, Attribute/Visual/Fixation point, Attribute/Visual/Rendering type/Screen, Attribute/Location/Screen/Center",

      "target": "Event/Label/Target image, Event/Description/A white airplane as the RSVP target superimposed on a satellite image is displayed., Event/Category/Experimental stimulus, (Item/Object/Vehicle/Aircraft/Airplane, Participant/Effect/Cognitive/Target, Sensory presentation/Visual/Rendering type/Screen/2D), (Item/Natural scene/Arial/Satellite, Sensory presentation/Visual/Rendering type/Screen/2D)",

      "nontarget": "Event/Label/Non-target image, Event/Description/A non-target image is displayed for about 8 milliseconds, Event/Category/Experimental stimulus, (Item/Natural scene/Arial/Satellite, Participant/Effect/Cognitive/Expected/Non-target, Sensory presentation/Visual/Rendering type/Screen/2D), Attribute/Onset"

    }

  }

}

# 13 Appendix III: Contributors

Legend (source: [https://github.com/kentcdodds/all-contributors](https://github.com/kentcdodds/all-contributors)) 

<table>
  <tr>
    <td>Emoji</td>
    <td>Represents</td>
  </tr>
  <tr>
    <td>💬</td>
    <td>Answering Questions (on the mailing list, NeuroStars, GitHub, or in person)</td>
  </tr>
  <tr>
    <td>🐛</td>
    <td>Bug reports</td>
  </tr>
  <tr>
    <td>📝</td>
    <td>Blogposts</td>
  </tr>
  <tr>
    <td>💻</td>
    <td>Code</td>
  </tr>
  <tr>
    <td>📖</td>
    <td>Documentation and specification</td>
  </tr>
  <tr>
    <td>🎨</td>
    <td>Design</td>
  </tr>
  <tr>
    <td>💡</td>
    <td>Examples</td>
  </tr>
  <tr>
    <td>📋</td>
    <td>Event Organizers</td>
  </tr>
  <tr>
    <td>💵</td>
    <td>Financial Support</td>
  </tr>
  <tr>
    <td>🔍</td>
    <td>Funding/Grant Finders</td>
  </tr>
  <tr>
    <td>🤔</td>
    <td>Ideas & Planning</td>
  </tr>
  <tr>
    <td>🚇</td>
    <td>Infrastructure (Hosting, Build-Tools, etc)</td>
  </tr>
  <tr>
    <td>🔌</td>
    <td>Plugin/utility libraries</td>
  </tr>
  <tr>
    <td>👀</td>
    <td>Reviewed Pull Requests</td>
  </tr>
  <tr>
    <td>🔧</td>
    <td>Tools</td>
  </tr>
  <tr>
    <td>🌍</td>
    <td>Translation</td>
  </tr>
  <tr>
    <td>⚠️</td>
    <td>Tests</td>
  </tr>
  <tr>
    <td>✅</td>
    <td>Tutorials</td>
  </tr>
  <tr>
    <td>📢</td>
    <td>Talks</td>
  </tr>
  <tr>
    <td>📹</td>
    <td>Videos</td>
  </tr>
</table>


The following individuals have contributed to the Brain Imaging Data Structure ecosystem (in alphabetical order).

If you contributed to the BIDS ecosystem and your name is not listed please add it.

Tibor Auer 💬📖💡🔧📢

Sylvain Baillet 📖🔍

Elizabeth Bock 📖💡

Eric Bridgeford 📖🔧

Teon L. Brooks 📖💻

Suyash Bhogawar 📖💡⚠️🔧💬

Vince D. Calhoun 📖

Alexander L. Cohen 🐛💻📖💬

R. Cameron Craddock 📖📢

Samir Das 📖

Alejandro de la Vega 🐛💻⚠️

Eugene P. Duff 📖

Elizabeth DuPre 📖💡

Eric A. Earl 🤔

Anders Eklund  📖📢💻

Guillaume Flandin 📖💻

Satrajit S. Ghosh 📖💻

Tristan Glatard 📖💻

Mathias Goncalves 💻🔧📢

Krzysztof J. Gorgolewski 📖💻💬🤔🔍📢📝💡🔍🔌

Alexandre Gramfort 📖💡

Yaroslav O. Halchenko 📖📢

Daniel A. Handwerker 📖

Michael Hanke 📖🤔🔧🐛📢

Michael P. Harms 📖⚠️🔧

Richard N. Henson 📖

Dora Hermes📖💻✅

Katja Heuer 🔧

Chris Holdgraf📖

International Neuroinformatics Coordinating Facility 💵📋

Mainak Jas 📖💻

David Keator 📖

Gregory Kiar 📖💻🎨🔧

Laura and John Arnold Foundation 💵

Xiangrui Li 📖💻

Vladimir Litvak 📖

Dan Lurie 🤔📖🔧🔌💻💬

Camille Maumet 📖

Christopher J. Markiewicz 💬📖💻

Jeremy Moreau 📖💡

Zachary Michael 📖

Michael P. Milham 💡🔍

National Institute of Mental Health 💵

B. Nolan Nichols 📖

Thomas E. Nichols 📖

Guiomar Niso 📖💡

Robert Oostenveld 📖🔧📢💡

Dianne Patterson 📖

John Pellman 📖

Cyril Pernet 💬 📖 💡📋

Dmitry Petrov 📖💻

Russell A. Poldrack 📖🔍📢

Jean-Baptiste Poline 📖📢🤔🎨

Ariel Rokem 📖

Gunnar Schaefer 📖

Jan-Mathijs Schoffelen 📖

Vanessa Sochat 📖

Francois Tadel 📖🔌💡

Roberto Toro 🔧

William Triplett 📖

Jessica A. Turner 📖

Joseph Wexler 📖💡

Gaël Varoquaux 📖

