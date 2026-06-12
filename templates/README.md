# <Dataset name>

<!-- One or two sentences a newcomer can read in 10 seconds: what was recorded,
     in whom, and why. The most common section in real READMEs, and the most
     common omission. -->
<PLAIN-LANGUAGE ONE-PARAGRAPH SUMMARY>

## Overview

<!-- In prose (no lists): state the scientific question / purpose, then the
     essentials — modality, number of participants and any groups, sessions/runs,
     task(s), approximate recording duration, the project name and years it ran
     (local time of day can matter for subject state), and the associated
     publication if any. -->
<ONE OR TWO PARAGRAPHS: PURPOSE, THEN THE ESSENTIALS — MODALITY, N AND GROUPS,
SESSIONS/RUNS, TASK(S), DURATION, PROJECT/YEARS, AND PUBLICATION>

### Experimental design (optional)
<!-- In prose: the variables that define the experiment — the independent
     (manipulated), dependent (measured), and control (held-fixed) variables.
     Omit for datasets without a designed manipulation (e.g. resting state). -->
<EXPERIMENTAL DESIGN: INDEPENDENT, DEPENDENT, AND CONTROL VARIABLES>

## Dataset contents and structure

<!-- Orient the reader to what they cannot infer from the standard BIDS layout:
     contents of derivatives/ and sourcedata/, extra or non-standard files, and
     any intentional deviation from BIDS. Pasting the bids-validator summary
     (data types + number of subjects) is an easy, accurate start. -->
<TOP-LEVEL CONTENTS, derivatives/, sourcedata/, NON-STANDARD FILES>

## Methods

<!-- If the dataset has an associated paper, you may copy or adapt its Methods
     section here, then trim it to what is relevant to the data as shared. -->

### Participants and recruitment
<!-- Recruitment, eligibility, grouping, and how many were excluded and why. Do
     NOT paste per-subject demographics — those belong in participants.tsv, and
     Control/Patient status belongs in its `group` column. Summarize and point. -->
<INCLUSION / EXCLUSION CRITERIA, GROUPS, EXCLUSIONS>

### Acquisition
<!-- Equipment and environment (e.g. shielded room, seating, any setup done when
     the subject arrived), plus the few parameters needed to understand the
     signals. Full machine-readable parameters belong in *_<modality>.json. -->
<DEVICE, CHANNELS/COILS, SAMPLING RATE, REFERENCE, FILTERS, ENVIRONMENT, KEY SETTINGS>

### Task and paradigm
<!-- What participants did and the trial structure, plus how tasks were organized
     across a session (order, counter-balancing, activities between tasks) —
     important because BIDS splits tasks into separate files. The canonical
     TaskName / TaskDescription live in task-<label>_*.json. -->
<PARADIGM, CONDITIONS, TIMING, TRIAL COUNTS, TASK ORDER / COUNTER-BALANCING>

### Stimuli (optional)
<!-- What was presented, and where stimulus files live (e.g. stimuli/). -->
<STIMULUS DESCRIPTION>

### Additional data acquired (optional)
<!-- Non-imaging data collected as part of the study: questionnaires, surveys,
     clinical measures, swabs. Note availability and location; standardized
     phenotypic data belong in a phenotype/ folder. -->
<OTHER DATA AND WHERE IT LIVES>

## Known issues, quality, and missing data

<!-- The highest-value section for downstream users. Give a short overall quality
     summary (with a link to e.g. an MRIQC report if available), then anything
     that affects analysis: missing/partial runs, excluded participants, bad
     channels, timing or trigger problems, equipment or protocol changes
     mid-study, a lesion or anomaly in one participant, or data that look normal
     but are not. Write "None known." if the dataset is clean. -->
<QUALITY SUMMARY + PER-SUBJECT / DATASET-WIDE CAVEATS, OR "None known.">

## How to use these data (optional)

<!-- Preprocessing already applied (and where it lives), recommended
     reference/montage, software + version, or analysis tips. -->
<PREPROCESSING NOTES / RECOMMENDATIONS>

## References and citation

<!-- A one-line "how to cite" and the key paper(s). The dataset DOI and
     machine-readable references also live in dataset_description.json
     (DatasetDOI, ReferencesAndLinks, HowToAcknowledge). -->
<PREFERRED CITATION; ASSOCIATED PAPER(S); DOI>

## Contact

<!-- The person responsible for additional information. A role + email + ORCID is
     more future-proof than a personal name alone. -->
<NAME / ROLE / EMAIL / ORCID>
