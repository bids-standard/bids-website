---
title: Steering Group executive summary, action items, and minutes
author: Franklin Feingold
display: true
---

# Steering Group executive summary, action items, and minutes

Date: Thursday February 4, 2021

<!--more-->

### Executive Summary

The Steering Group met to discuss the latest BEP updates. [ASL](https://github.com/bids-standard/bids-specification/pull/669){:target="_blank"} and [qMRI](https://github.com/bids-standard/bids-specification/pull/690){:target="_blank"} are close to being released with PET following soon after. We spent the majority of the meeting with the leads from [BEP20: Eye Tracking](https://bids.neuroimaging.io/bep020){:target="_blank"}. They are progressing nicely and starting to finalize their specification. They are having their Eye Tracking community review prior to escalating up to the BIDS community. They are reaching a consensus within their community. This extension will help BIDS continue to extend into more diverse windows into the brain and further unlock more multimodal studies.

### Action items

N/A

### Minutes


- [ASL specification](https://github.com/bids-standard/bids-specification/pull/669){:target="_blank"}, examples, and validator are ready for release
- [qMRI specification](https://github.com/bids-standard/bids-specification/pull/690){:target="_blank"} is merged. Working on examples and validator
- After ASL and qMRI are release, we will focus on getting PET incorporated

The Steering Group was joined by [BEP20: Eye Tracking](https://bids.neuroimaging.io/bep020){:target="_blank"} leads

- The community is reviewing the BEP
  - Trying to be public about the efforts
- BEP seeks to be a solution for different types of Eye Tracking experiments
  - Big use case is naturalistic stimuli
- BEP status
  - Most people are receptive to the BEP
  - There was a preprint released that is related to the BEP effort
    - BEP leads reached out and received good feedback from the authors
    - The preprint was a bit more high-level, but is compatible with the BEP
    - Preprint focused on how to report Eye Tracking in a paper rather than how to organize and share the data
- The community is sharing data
- BEP does have a constrained scope with a clear goal
  - Core aspect: position of the area and recording that along with the stimuli map
- BIDS is an interoperable standard
  - Community focused to wrap BEP into BIDS
  - Some colleagues have had trouble getting over the Brain Imaging part of BIDS
    - Could be an impediment to adoption
  - BIDS is a practical implementation, would rather be in BIDS
- Eye Tracking with EEG, MEG, and/or MRI is becoming more common
- We can use the existing infrastructure to continue unlocking multimodal studies
- One goal is to develop BIDS-Apps for Eye Tracking
- The conversion to markdown is done
  - Encountering challenges with the validator implementation
  - Examples have been generated
- Performing a within Eye Tracking community review
  - Ensuring the community is comfortable with the BEP
- One potential issue is [time series representation conflicts](https://github.com/bids-standard/bids-specification/issues/713){:target="_blank"}
  - Coordinating with [BEP29: Virtual and physical motion](https://bids.neuroimaging.io/bep029){:target="_blank"}
  - Meeting with relevant stakeholders
- Balancing the validation with practical implementation
