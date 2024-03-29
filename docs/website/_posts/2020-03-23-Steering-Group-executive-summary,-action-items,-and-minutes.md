---
title: Steering Group executive summary, action items, and minutes
author: Franklin Feingold
display: true
---

# Steering Group executive summary, action items, and minutes

Date: Thursday March 5, 2020

Attended: Franklin Feingold, Melanie Ganz, Guiomar Niso, Robert Oostenveld

<!--more-->

### Executive Summary

We reviewed the action items from the previous two meetings. We discussed the framework for the BIDS community slides and how this information can be formatted and designed for future extensions and derived versions. We will draft an approach for organizing BIDS related meetings to pilot at NRM and OHBM in June.

We also have a [list of channels](https://docs.google.com/spreadsheets/d/16SAGK3zG93WM2EWuoZDcRIC7ygPc5b7PDNGpFyC3obA/edit#gid=0){:target="_blank"} to share BIDS related information on. The have a plan for handling non-BIDS related information on our channels is to share on our [google group](https://groups.google.com/forum/#!forum/bids-discussion){:target="_blank"}.

The attending members of the Steering Group gave approval for moving forward with completing the [Genetic Information BEP](https://github.com/bids-standard/bids-specification/pull/395){:target="_blank"}. This will solidify the process for incorporating BEPs moving forward. The process will be: 1) merging in the BEP constructed examples to [BIDS-examples](https://github.com/bids-standard/bids-examples){:target="_blank"}, 2) merge the validator extension into [BIDS-validator](https://github.com/bids-standard/bids-validator){:target="_blank"}, and 3) merge the BEP into [BIDS-specification](https://github.com/bids-standard/bids-specification){:target="_blank"}

The Steering Group gave direction on handling author lists on Zenodo - make it a single author: “BIDS Contributors Group” as defined in the [governance document](https://docs.google.com/document/d/1R-J2lL9V_wIkYhye4zH-feyl4P4J8NyO40rIYyY141o/edit){:target="_blank"}.

### Action Items

| Action Item |
| -------- |
| GN: draft tweets for OHBMX twitter presentation    |
| Write INCF to determine if they have a list of related standard initiatives |
| Initialize Google Slides to start iterating on our BIDS community slides |
| Draft specification vs ecosystem for website-about section |
| Guidelines for organizing a BIDS information session |
| Draft BIDS interest group information and process |
| Codify rules for making a repository under the BIDS standard GitHub organization |
| Share Steering Meeting: executive summary, action items, and minutes to bids-website |

### Minutes

- Reviewed [previous meeting action items](https://bids.neuroimaging.io/2020/03/12/Steering-Group-executive-summary,-action-items,-and-minutes.html#action-items){:target="_blank"}
  - A [survey](https://docs.google.com/forms/d/e/1FAIpQLSfGjTA-U_1LECRsbuBQ9X7kdi34aEdxTMoWCwwkEgou-qpb4A/viewform){:target="_blank"} with an accompanying [blog post](https://bids.neuroimaging.io/2020/03/20/engage-with-the-bids-ecosystem.html){:target="_blank"} was drafted to evaluate how the community would like to engage with each other, what barriers may exist that makes engaging more challenging, and ways that we can engage colleagues that do not know about BIDS.
  - Points to consider when designing the infrastructure to support BIDS slides
    - An important feature is that the BIDS slides will be a living and breathing document shared via Google slides.
    - Google slides gives us the ability to: version control, seamless updating capability, and persistent links.
    - Discussed preserving and separating the core presentation from the derived versions. Ensuring the references of where they have been used.
      -  Event link or other event details

    - Drafting guidelines for how to organize a BIDS event
    - Pilot at NRM and OHBM (June 2020)

    - Compiling a [list of channels](https://docs.google.com/spreadsheets/d/16SAGK3zG93WM2EWuoZDcRIC7ygPc5b7PDNGpFyC3obA/edit#gid=0){:target="_blank"} to share BIDS news. Currently for version releases and community feedback calls on BEPs.


- Attending Steering Group members gave approval to move forward with finalizing the [Genetic Information extension](https://github.com/bids-standard/bids-specification/pull/395){:target="_blank"} and merging into the specification. This will trigger a [v1.3.0 release](https://github.com/bids-standard/bids-specification/pull/435){:target="_blank"} (according to our [release guidelines](https://github.com/bids-standard/bids-specification/blob/master/Release_Guideline.md){:target="_blank"}).

  - For future BEPs, they will submit their examples to [BIDS-examples](https://github.com/bids-standard/bids-examples){:target="_blank"} for review by the Steering Group and confirm the [validator](https://github.com/bids-standard/bids-validator){:target="_blank"} has been extended properly. The BEP leads can leave it as a draft PR. It was determined that opening the PR from a branch of the [BIDS specification repository](https://github.com/bids-standard/bids-specification){:target="_blank"} should be done allowing us to render the extension via ReadTheDocs.
    - Genetic Information was in the BEP lead's fork of BIDS-examples (after the meeting a [PR was opened](https://github.com/bids-standard/bids-examples/pull/178){:target="_blank"}).

- Regarding the [Zenodo authorship](https://github.com/bids-standard/bids-specification/issues/66){:target="_blank"} discussion, the Steering Group considered for the list to either be  first/last+alphabetical order in the middle or a single authored “[BIDS Contributors Group](https://bids.neuroimaging.io/governance.html#bids-contributors-group){:target="_blank"}”.
  - Decision toward “BIDS Contributors Group” similar to how ADNI does it.


- The Steering Group discussed where to share non-BIDS related information.
  - The consensus was to share on the [bids-discussion](https://groups.google.com/forum/#!forum/bids-discussion){:target="_blank"} Google group channel.

- We brainstormed what may be the related initiatives to keep aware of. FF contacted INCF to see if they have information regarding this. Please see the [INCF blog](https://www.incf.org/blogs-list){:target="_blank"}.

- The Steering Group discussed the format for the BIDS Maintainers monthly update. This will be submitted to Slack and added to the next agenda. This will be implemented starting with the March update and will not be retroactive.
