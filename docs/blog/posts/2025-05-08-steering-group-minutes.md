---
date: 2025-05-08
slug: "Steering Group minutes"
author: anonymous
categories:
-   steering group minutes
---

## Participants

- Yaroslav Halchenko
- Camille Maumet
- Dora Hermes
- Eric Earl
- Anthony Galassi
- Melissa Kline Struhl
- Brian Leonard

## Agenda

1. Melissa Kline Struhl - Psych-DS Guest
    - https://psych-ds.github.io/
3. Response to MEDD regarding new format `5 min`
4. OHBM business`10 min`
5. Maintainers updates `10 min`
    - Maintainers need more members recruited
6. (after end) Copenhagen Maintainers Meeting updates `15 min`

## Meeting Minutes

### Psych-DS

Melissa Kline Struhl

- comes from the SIPS community, they recognized there was a mis-match in skillset for researchers in psych to adhere to BIDS. 
     - Do everything in excel, most often small datasets
- the replication crisis has motivated their community to build/adopt standards like BIDS
- community is working towards making their research more FAIR
- dataset_description.json uses JSON-LD schema.org https://schema.org/
- data likely contains information form multiple subjects in a single file (ex: excel or csv with all subject data)
    - this data is typically stored in the 'data' folder
    - use csv file format for tabular data
- for researchers who do not use machine-redable workflows to provide a road into that
- Psych-DS is currently developing a validator schema.org/Dataset https://psych-ds.github.io/validator
- Example usecases of interaction with BIDS
    - extracting behavioural data to be analyzed separatly
    - or inject behavioural data into a BIDS dataset
- they are a data format for the BRAIN Initiative BBQS (data coordinating for behavioral data)
- Discussion: 
    - DH: BIDS has events files, does psych-DS plan to include something similar for data like reaction times, etc 
    - MKS: It hasnt been built yet, but that is a very likely use case to work towards
    - EA: what about data dictionary? it looks like anything is a data dictionary? 
    - MKS: in the current examples, users are given options of simple of variable names. But the documentation points users to be able to assemble more complex datasets (https://psychds-docs.readthedocs.io/en/latest/guides/4_data_dictionary/) they do not require pulling variables from established onotologies but they do require variables to be defined
    - DH: re data dictionary, are you considering heriarchical event descriptors?
    - MKS: we are aware of the option, yes we would like ot use heirarchical event descriptors is the data support it. 
    - Psych-DS is also working on conversation tools to convert data BIDs-->Psych-DS and Psych-DS-->BIDS
    - EA:  are you considering to include additional file formats beyond csv.  csv only can become problematic if the data contains commas. 
-NEXT STEPS: BEP 36 can reach out to Eric Earl for moving it forward.


### Response to MED regarding new format

- Dora felt that she has a COI, thus was not an appropriate person to respond on behalf of BIDS.
- Camille:  it sounds like people are using MED, so perhaps we should revisit our response to include steps that would need to occur for MED to be involved with BIDS
- Dora: instead of saying 'no', we should provide a path forward for MED that the developers of the format should be responsible for. 
- DH & CM would like to ammend the email. we will continue the discussion on mattermost. https://github.com/bids-standard/bids-specification/issues/2055

### OHBM

- townhall - is this day one or another time?
- 2 BIDS-related events in OHBM
    - BIDS opening - day one
    - BIDS townhall - for BIDS to decide

### Maintainers updates

- Maintainers need more members recruited
    - Up one (Julia), but down 2 going on 3 or 4 (Rémi out for now, Stefan living life without BIDS, and possibly Anthony's and Eric's contracts up in September)
    - A simple outreach method could be all runners-up for Steering Group elections
    - [name=Camille] I'd love an open call if we can and that makes sense.
    - [name=Kim Ray] I can reach out Ashley Stewart directly , can write a email for direct asks.
    - [name=Yaroslav] can we use the larger BIDS email list to cast a wider audience?
- Expectations (onboarding docs: https://github.com/bids-standard/bids-specification/blob/master/Maintainers_Guide.md#why-become-a-maintainer)
     - 1-2 hours a week 
     - attend 1 bi-weekly meeting
     - technical skills not required 
- avenues for advertising: neruohackademy, brainhacks, BIDS adjacent groups (SPARC, NWB, Psych-DS, neuroblueprint https://neuroblueprint.neuroinformatics.dev/latest/index.html)

### Copenhagen Maintainers Meeting updates

(Asynchronously Eric talked with Cyril)

- Q: Is the list of attendees/invitees complete?
    - Cyril is going to put the attendees list on GitHub markdown
        - 10 maintainers and steering
        - No Peer, No Oscar
        - Maybe 6 people from EBRAINS? Cyril's having trouble getting people to RSVP properly/fully
- Q: What percent complete is booking travel and hotel?
    - 10 people are booked for hotels
    - Cyril to give hotel a list of names, and the hotel will give you your room when you show up giving them your name
- Q: Are meals, incidental expenses, and ground transportation reimbursements possible (per diem, etc.)?
    - Cyril checking with Ariel, that question had not come up to Cyril  before today
- Ground transportation off flight
    - [Getting there](https://github.com/openneuropet/outreach/blob/main/BIDS_maintainers2025/location.md)
- Tuesday, June 10 agenda item(s): EBRAINS needs to learn schema and see the BIDS ecosystem
    - BIDS2OPENMIND collaborations
    - Cyril writing down the agenda in GitHub or on the draft Google Doc agenda
