---
date: 2020-08-20
slug: Steering Group executive summary, action items, and minutes
author: Franklin Feingold
---

# Steering Group executive summary, action items, and minutes

Date: Thursday August 10, 2020

<!--more-->

### Executive Summary

We were joined by [Dave Keator](https://faculty.sites.uci.edu/davidkeator/people/), from the [NIDM](http://nidm.nidash.org/) and [ReproNim](https://www.repronim.org/) groups. We learned more about their NIDM project and specific subprojects using BIDS. One such project is [NIDM-terms](https://github.com/incf-nidash/nidm-terms). This project seeks to capture our BIDS terminology and devise a way to make it easier to manage them and query datasets based on those terms. One use case can be utilizing this collection as a resource for BEPs to interact with as they are discussing new terms to add to the specification. This can also be helpful to users wanting to learn more about our BIDS terms present in the specification. Another beneficial aspect of this project is the ability to annotate datasets.

### Action items

| Action items |
| -------- |
| N/A    |

### Minutes

We were joined by [Dave Keator](https://faculty.sites.uci.edu/davidkeator/people/), to discuss the [NIDM](http://nidm.nidash.org/) and [ReproNim](https://www.repronim.org/) initiatives.
- [NIDM-terms](https://github.com/incf-nidash/nidm-terms) is a community-driven ontology
- `isAbout` field used quite a bit
- Extracting terms from the BIDS-Specification and created jsonld representation
  - Use case: A BEP can consult this list to ensure no terms are being reused
  - Potentially working with our BIDS-schema
    - Related to the [yaml conversion of our entity table](https://github.com/bids-standard/bids-specification/pull/475)
- Determining approaches for integrating this into our processes
  - Developing tool to work with: adding existing/new terminology, add dataset annotations
  - Potentially adding new terms through a GUI application
- Tracking terms and providing definitions
  - Nice to know how a term is being used and can see how others interpret
- Easier the better!
