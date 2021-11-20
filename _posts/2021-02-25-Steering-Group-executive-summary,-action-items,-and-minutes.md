---
title: Steering Group executive summary, action items, and minutes
author: Franklin Feingold
display: true
---

# Steering Group executive summary, action items, and minutes

Date: Thursday February 25, 2021

<!--more-->

### Executive Summary

The Steering Group met to discuss the latest updates on the [PET extension](https://github.com/bids-standard/bids-specification/pull/633){:target="_blank"}. The extension is getting closer to completion. We spent the majority of the meeting with the [BEP031: Microscopy](https://docs.google.com/document/d/1Nlu6QVQrbOQtdtcRarsONbX5SrOubXWBvkV37LRRqrc/edit){:target="_blank"} leads. They introduced the motivation and scale of the effort. There appears to be adjacent ongoing initiatives that could be good to be aligned with. It could be beneficial to introduce a species metadata entity to tease apart the incorporation of the methodology from the species.The BEP031 leads will meet with the [Maintainers Group](https://github.com/bids-standard/bids-specification/blob/master/DECISION-MAKING.md#maintainers-group){:target="_blank"} to further discuss their lingering questions.

### Action items



| Action item |
| -------- |
| Schedule BEP031 to meet with Maintainers     |


### Minutes

- Developing the [PET extension of the BIDS-validator](https://github.com/bids-standard/bids-validator/tree/bep_009){:target="_blank"}

The Steering Group spent the rest of the meeting with the [BEP031: Microscopy](https://docs.google.com/document/d/1Nlu6QVQrbOQtdtcRarsONbX5SrOubXWBvkV37LRRqrc/edit){:target="_blank"} leads

- The motivation for this BEP was the MRI community uses microscopy to validate qMRI recordings
- Range of microscopy data: primarily 2D imaging flavors, some interest to extend into 3D imaging
  - Format: single .png, accommodate .oct for 3D imaging
  - Addressing in vivo and ex vivo
- There are other types of standards and data structures
  - [Recent preprint on bioarxiv](https://www.biorxiv.org/content/10.1101/2021.02.10.430563v2){:target="_blank"} from the SPARC group
- Detail level questions can be opened as issues in the [bids-specification repository](https://github.com/bids-standard/bids-specification){:target="_blank"} to get Maintainers thoughts
- The [Neuroscience Data Structure](https://github.com/INCF/neuroscience-data-structure/issues){:target="_blank"} group is another team thinking about this
  - Considering species, formats, and experiments
- Microscopy could be split into microscopy and mouse/animal
  - Mouse/animal would be primarily metadata additions similar to genetics and HED
  - Adding sample entity, could be a separate pull request
- For breaking down large files into smaller ones: `split` is for temporal and `chunk` could be used for spatial
- Suggest using the entity that a particular community is familiar and comfortable with
- Perhaps adding species into BIDS
  - May be through `participants.tsv`
