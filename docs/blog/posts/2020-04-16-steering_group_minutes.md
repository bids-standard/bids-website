---
date: 2020-04-16
slug: Steering Group executive summary, action items, and minutes
author: Franklin Feingold
---

# Steering Group executive summary, action items, and minutes

Date: Thursday April 16, 2020

<!--more-->

### Executive Summary

We were joined in this meeting by the BIDS-ASL BEP leads. We spent the majority of this meeting discussing the [BIDS-ASL](https://bids.neuroimaging.io/bep005) BEP development approach and status along with any open questions they may have. We see a natural integration between the [ASL](https://bids.neuroimaging.io/bep005) and [PET](https://bids.neuroimaging.io/bep009) BEP projects. While talking to the ASL team we found that our definition of `raw` needs to be refined and made more specific. We want to ensure that fields previously specified remain consistent, when possible. Once the raw ASL specification is merged the group will move forward with derivatives.

### Action Items

| Action item |
| ------------------------ |
| Invite Maintainers to next Steering Group meeting |
| Apply for Google season of docs |
| Clarifying how BIDS defines “raw” |

### Minutes

This meeting was primarily focused on meeting with the [BIDS-ASL](https://bids.neuroimaging.io/bep005) BEP leads to discuss their BEP and getting it over the finish line
- The ASL specification was initially pushed by physicists in the [ISMRM](https://www.ismrm.org/) community
- A few challenges toward specifying was evaluating differing sequence and scaling
- In conversations with dcm2niix team to support ASL scaling information
  - MG and BIDS-ASL will talk further - overlap with the PET BEP
- Thinking through ASL standardization vs data sharing and curation
  - Recommending simple and easy fields to fill in
- Think about sending a letter from the BIDS community to imaging vendors to strive toward standardizing file formats
- Where possible, use the same words or description of a previously specified field
  - Strive toward interoperability across modalities
- ASLcontext file similar to the sidecar json
- ASL nearly prepared to open their pull requests
- Appetite to start working through ASL Derivatives
- Maintainers are invited to the next meeting
