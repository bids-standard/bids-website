---
date: 2020-11-12
slug: Steering Group executive summary, action items, and minutes
author: Franklin Feingold
---

# Steering Group executive summary, action items, and minutes

Date: Thursday November 12, 2020

<!--more-->

### Executive Summary

We began this meeting by discussing the current progress of the [ASL BEP](https://github.com/bids-standard/bids-specification/pull/669). There are a few items the BIDS Maintainers are working with the BEP leads to resolve. We hope to complete this work and continue the progress of incorporating this BEP into the standard. We decided to push the conversation on [crediting BIDS in manuscripts](https://github.com/bids-standard/bids-specification/issues/627) to our next meeting.

The majority of this meeting we were joined by Melissa Kline of the [Psych-DS](https://github.com/psych-ds/psych-DS) project. The Psych-DS project seeks to standardize behavioral experiments. Psych-DS is quite flexible and can adapt to many different use cases. One key recommendation they have is to compose well structured tsv files. A challenge they have faced is thinking through the directory structure due to the heterogeneity present in behavioral studies. They do not have many keywords and intend to stick to that approach. They would prefer to link to existing ontologies.

### Action items

| Action items |
| -------- |
| N/A |

### Minutes

- Reviewed [BIDS ASL](https://github.com/bids-standard/bids-specification/pull/669) progress
  - Few more things to iron out
  - Coordinated with BEP001 too

- Pushed the credit conversation to next meeting

- Melissa Kline joined from the [Psych-DS](https://github.com/psych-ds/psych-DS) project
  - Initiative was borne out of the ManyBabies project
  - During SIPS began the standardization of behavioral data using BIDS as the model
  - Psych-DS goal is to nudge people toward using a standard
    - Well structured tsv’s are recommended
- Challenge has been thinking through how the file structure can look. Behavioral studies are more heterogeneous than imaging studies - very little consensus among the community
  - This will make implementing an inheritance principle more difficult
- Seeking agreement on metadata terms
  - Have a schema to validate against
- Data practices can be a framework to move forward
  - Convert common raw data formats (e.g Qualtrics) to the standard Psych-DS format
    - 1st step is writing converters to get to Psych-DS
- If a dataset is Psych-DS compliant we can make certain assumptions about the data
- Push to have recommended and required keywords
  - While keeping Psych-DS flexible for the many different use cases
  - Do not have many keywords - this is not the purpose of Psych-DS
    - Prefer to point to existing ontologies
- Want to give some sort of BIDS + Psych-DS compatible recommendations
- Looking for a volunteer to write validator
- Psych-DS group is pushing toward v1.0.0
  - By design is to help simple graduate students (minimal technical experience)
- Psych-DS needs to work in the common computing environment: R
  - Have a browser and command-line validator
- Privacy is a high concern
  - Psych-DS may share metadata
  - Could separate the metadata from the data
    - There is a use for metadata stores pointing to DUA’s for the data
  - Community is unsure of what they can and cannot share
- Appetite for specific instructions to do Open Science
- Psych-DS may not be BIDS compliant, but does not block capability
