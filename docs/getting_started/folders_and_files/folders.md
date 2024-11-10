The BIDS format is essentially a way to structure your data / metadata within a hierarchy of folders.
This makes it easy to browse from a computer, as well as to automatically parse a BIDS folder with a program.
The BIDS structure makes minimal assumptions about the tools needed to interact with the data that's inside.

The files in present in BIDS dataset are organized into a hierarchy of folders that have specific naming conventions.

The rest of this page describes how these folders are structured.

## Overview

There are four main levels of the folder hierarchy, these are:

```text
project/
└── subject
    └── session
        └── datatype
```

With the exception of the top-level `project` folder,
all sub-folders have a specific structure to their name (described below).
Here's an example of how this hierarchy looks:

```text
myProject/
└── sub-01
    └── ses-01
        └── anat
```

Here is the folder name structure of each level:

## project

Can have any name, this should be descriptive for the dataset contained in the folder.

## subject

Structure: `sub-<participant label>`

One folder per subject in this dataset.
Labels should be unique for each subject.

## session

Structure: `ses-<session label>`

In general, a `session` represents a recording session, and subjects will stay in the scanner or headset during that session.
You might have multiple sessions per subject if you collected data from them on several occasions.
If there is only a single session per subject, this level of the hierarchy may be omitted.

For more details, refer to this {ref}`section of the FAQ <faq_session>`.

## datatype

Represents different types of data. Must be one of:

-   `anat`: anatomical MRI data
-   `func`: functional MRI data
-   `fmap`: fieldmap data
-   `dwi`: diffusion MRI data
-   `perf`: arterial spin labeling data
-   `eeg`: electroencephalography data
-   `meg`: magnetoencephalography data
-   `ieeg`: intracranial EEG data
-   `beh`: behavioral data
-   `pet`: positron emission tomography data
-   `micr`: microscopy data
-   `nirs`: near-infrared spectroscopy data
-   `motion`: motion capture data
-   `mrs`: magnetic resonance spectroscopy data

The name for the datatype depends on the recording modality.

<!-- https://www.tablesgenerator.com/html_tables# -->

<div align="center">
<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;margin:0px auto;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-mri{border-color:#000000;color:var(--mri);font-size:18px; text-align:center;vertical-align:middle}
.tg .tg-micr{border-color:#000000;color:var(--micr);font-size:18px; text-align:center;vertical-align:middle}
.tg .tg-pet{border-color:#000000;color:var(--pet);font-size:18px; text-align:center;vertical-align:middle}
.tg .tg-meeg{border-color:#000000;color:var(--meeg);font-size:18px;text-align:center;vertical-align:middle}
.tg .tg-beh{border-color:#000000;color:var(--beh);font-size:18px; text-align:center;vertical-align:middle}
.tg .tg-nirs{border-color:#000000;color:var(--nirs);font-size:18px; text-align:center;vertical-align:middle}
.tg .tg-motion{border-color:#000000;color:var(--motion);font-size:18px; text-align:center;vertical-align:middle}
.tg .tg-mrs{border-color:#000000;color:var(--mrs);font-size:18px; text-align:center;vertical-align:middle}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-va6w"></th>
    <th class="tg-xuqq" colspan="8"><span style="font-weight:bold"><b>modality</b></span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-xuqq" rowspan="5"><span style="font-weight:bold"><b>datatype</b></span></td>
    <td class="tg-mri"><b>MRI</b></td>
    <td class="tg-pet"><b>PET</b></td>
    <td class="tg-meeg"><span style="font-style:normal;text-decoration:none"><b>meeg</b></span></td>
    <td class="tg-beh"><b>behavioral</b></td>
    <td class="tg-micr"><b>microscopy</b></td>
    <td class="tg-nirs"><b>NIRS</b></td>
    <td class="tg-motion"><b>motion</b></td>
    <td class="tg-mrs"><b>MRS</b></td>
  </tr>
  <tr>
    <td class="tg-mri">anat</td>
    <td class="tg-pet">pet</td>
    <td class="tg-meeg">eeg</td>
    <td class="tg-beh">beh</td>
    <td class="tg-micr">micr</td>
    <td class="tg-nirs">nirs</td>
    <td class="tg-motion">motion</td>
    <td class="tg-mrs">mrs</td>
  </tr>
  <tr>
    <td class="tg-mri">func<br></td>
    <td class="tg-pet"></td>
    <td class="tg-meeg">meg</td>
    <td class="tg-beh"></td>
    <td class="tg-micr"></td>
    <td class="tg-micr"></td>
    <td class="tg-motion"></td>
    <td class="tg-mrs"></td>
  </tr>
  <tr>
    <td class="tg-mri">dwi</td>
    <td class="tg-pet"></td>
    <td class="tg-meeg">ieeg</td>
    <td class="tg-beh"></td>
    <td class="tg-micr"></td>
    <td class="tg-micr"></td>
    <td class="tg-motion"></td>
    <td class="tg-mrs"></td>
  </tr>
  <tr>
    <td class="tg-mri">perf</td>
    <td class="tg-pet"></td>
    <td class="tg-meeg"></td>
    <td class="tg-beh"></td>
    <td class="tg-micr"></td>
    <td class="tg-micr"></td>
    <td class="tg-motion"></td>
    <td class="tg-mrs"></td>
  </tr>
</tbody>
</table>
</div>

## BIDS folder example

Below is the folder hierarchy for one of the
[BIDS example datasets](https://github.com/INCF/BIDS-examples). It has multiple
subjects of data, and includes metadata files (`.tsv` and `.json`) both between-
and within-subjects.

Note that it has one session per subject, so this level is omitted.

```text
ds001
├── dataset_description.json
├── participants.tsv
├── sub-01
│   ├── anat
│   │   ├── sub-01_inplaneT2.nii.gz
│   │   └── sub-01_T1w.nii.gz
│   └── func
│       ├── sub-01_task-balloonanalogrisktask_run-01_bold.nii.gz
│       ├── sub-01_task-balloonanalogrisktask_run-01_events.tsv
│       ├── sub-01_task-balloonanalogrisktask_run-02_bold.nii.gz
│       ├── sub-01_task-balloonanalogrisktask_run-02_events.tsv
│       ├── sub-01_task-balloonanalogrisktask_run-03_bold.nii.gz
│       └── sub-01_task-balloonanalogrisktask_run-03_events.tsv
├── sub-02
│   ├── anat
│   │   ├── sub-02_inplaneT2.nii.gz
│   │   └── sub-02_T1w.nii.gz
│   └── func
│       ├── sub-02_task-balloonanalogrisktask_run-01_bold.nii.gz
│       ├── sub-02_task-balloonanalogrisktask_run-01_events.tsv
│       ├── sub-02_task-balloonanalogrisktask_run-02_bold.nii.gz
│       ├── sub-02_task-balloonanalogrisktask_run-02_events.tsv
│       ├── sub-02_task-balloonanalogrisktask_run-03_bold.nii.gz
│       └── sub-02_task-balloonanalogrisktask_run-03_events.tsv
...
...
└── task-balloonanalogrisktask_bold.json
```
