# Dataset name, same as in dataset_description.json

Write one or two sentences a newcomer can read in 10 seconds: what was recorded,
in whom, and why.

## Overview

State the scientific question / purpose, then summarize the essentials — modality,
number of participants and any groups, sessions/runs, task(s), approximate
recording duration, the project name and years it ran, and the associated
publication (if any).

### Experimental design (optional)

State the variables that define the experiment — the independent (manipulated),
dependent (measured), and control (held-fixed) variables. This does not apply to
datasets without a designed manipulation (e.g. resting state).

## Dataset contents and structure

Orient the reader to what they cannot infer from the standard BIDS layout, for
example contents of derivatives/ and sourcedata/, extra or non-standard files,
and any intentional deviation from BIDS.

## Methods

If the dataset has an associated paper, you may copy or adapt its Methods
section here, then trim it to what is relevant to the data as shared.

### Participants and recruitment

Recruitment, eligibility, grouping, and how many were excluded and why. Do
NOT paste per-subject demographics — those belong in participants.tsv, and
Control/Patient status belongs in its `group` column. Only summarize.

### Acquisition

Short description of the equipment and environment (e.g. shielded room,
seated/supine for MEG, any setup done when the subject arrived), plus the
few parameters needed to understand the signals. Full machine-readable
parameters belong in *_<modality>.json.

### Task and paradigm

What participants did and the trial structure, plus how tasks were organized
across a session (order, counter-balancing, activities between tasks). The
canonical TaskName / TaskDescription live in task-<label>_*.json and events
live in *_events.tsv

### Stimuli (optional)

What was presented, and where stimulus files live (e.g. stimuli/).

### Additional data acquired (optional)

Non-imaging data collected as part of the study: questionnaires, surveys,
clinical measures, swabs. Note availability and location; standardized
phenotypic data belong in a phenotype/ folder.

## Known issues, quality, and missing data

This is the highest-value section for data reuse. Give a short overall
quality summary (with a link to e.g. an MRIQC report if available), then
anything that affects analysis: missing/partial runs, excluded participants,
bad channels, timing or trigger problems, equipment or protocol changes
mid-study,  a lesion or anomaly in one participant, or data that look
normal but are not. Write "None known." if the dataset is clean.

## How to use these data (optional)

Preprocessing already applied (and where it lives), recommended
reference/montage, software + version, or analysis tips.

## References and citation

A one-line "how to cite" and the key paper(s). The dataset DOI and
machine-readable references also live in dataset_description.json

## Contact

The person or team that can give additional information.
A role + email + ORCID is more future-proof than a personal name alone.
