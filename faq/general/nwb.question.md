---
title: "Can I combine BIDS and neurodata without border (NWB)?"
---

BIDS and [NWB](https://www.nwb.org/) are compatible.

An NWB data file is an allowed format in the iEEG-BIDS data structure.
This means that one subject (AAA) with a session (BBB)
can have a BIDS folder with raw iEEG data in NWB format:

```text
/sub-AAA/ses-BBB/ieeg/sub-AAA_ses-BBB_task-rest_ieeg.nwb
```

The same subject can have another session (CCC) with raw fMRI data in BIDS:

```text
/sub-AAA/ses-CCC/func/sub-AAA_ses-CCC_task-rest_bold.nii.gz
```
