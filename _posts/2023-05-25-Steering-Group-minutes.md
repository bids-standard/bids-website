---
title: Steering Group minutes
author:
display: true
---

# Steering Group minutes 2023/05/25

Date: Thursday, May 25th, 2023

<!--more-->


<table>
 <thead>
  <tr class="header">
   <th>
    <strong>
     Topic
    </strong>
   </th>
   <th>
    <strong>
     Relevant Links
    </strong>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr class="odd">
   <td>
    NSF POSE Workshop
   </td>
   <td>
    <a href="https://bidsstandard.slack.com/files/U02Q9B87D9P/F057GT2JDEU/data-metadata-standards-draft_v6.docx">
     <span class="underline">
      https://bidsstandard.slack.com/files/U02Q9B87D9P/F057GT2JDEU/data-metadata-standards-draft_v6.docx
     </span>
    </a>
   </td>
  </tr>
  <tr class="even">
   <td>
    BIDS workshop prep questions
   </td>
   <td>
    <p>
     1. What is your vision for derivatives? (a vision is the non technical expression of what you want it to do, e.g. I can see output X being reused across labs for Y or output X can be easily reused by ML experts)
    </p>
    <p>
     2. There is 2 views on derivatives: A. it should store the outcome of a pipeline + share code B. it should document every steps, and thus store every step.
    </p>
    <p>
     --&gt; what is your view?
    </p>
    <p>
     --&gt; to help developing BEP derivatives, would it be useful to have a framework/guidelines considering the focus of derivatives i.e. reusage?
    </p>
    <p>
     3. Given your involvement in BIDS and derivatives, what is/are the current roadblocks to advance your project?
    </p>
   </td>
  </tr>
  <tr class="odd">
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr class="even">
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr class="odd">
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr class="even">
   <td>
   </td>
   <td>
   </td>
  </tr>
 </tbody>
</table>



[[https://utexas.zoom.us/my/kimray]{.underline}](https://utexas.zoom.us/my/kimray)

**Present:** Cyril Pernet, Ariel Rokem, Guiomar Niso, Yaroslav
Halchenko, Stefan Appelhoff, Kimberly Ray

**Guest:** Guy Jones


BIDS Meeting Notes:

**Guest Guy Jones: discuss adding badges to the BIDS compliant datasets
on Scientific Data Journal website.**

Guy's Feedback:

May not have a badge in a classic sense, but possible a notification on
a set of
[**[collections]{.underline}**](https://www.nature.com/sdata/collections)

All this requires is a list of compliant dois that could be added to a
group

This would allow for changes to be made at any time, even
retrospectively

Collections can be searchable on the journal website.

Cyril: What are the tools that Scientific Data uses to check that BIDS
data are compliant?

Reviewers seem to be a first point of identification for BIDS on a less
official level.

It does not appear that there is an official way that Scientific Data
confirms for BIDS validity. However the use of BIDS tools can facilitate
this.

Guy: Some fields have tools that produce a "validation receipt" that
demonstrates the validity of the dataset. A printout of the validator
could do that.

BIDS validator could be used, however the validator outputs are not
consistent. Scientific data could provide different levels (A,B,C
grading) to indicate if a dataset has certain BIDS errors or is missing
necessary metadata or files. For example datasets on OpenNeuro may be in
BIDS but may still contain errors.

If OpenNeuro mandated that all datasets be BIDS compliant, then that
could be one route for ensuring validity.

Scientific Data could consider a trial where the authors required a
certificate of compliance. This could be an option (check box) during
the manuscript submission period. This could be the easiest, but may not
be a perfect solution because it\'s based on the user.

For other data modalities (e.g. genetics, etc), typically the journal
just encourages it to be shared on a repository. There are not many
efforts like BIDS, for standards themselves.

Nature Neuro may be another target journal that Guy could connect us
with to expand this mechanism.

ACTION ITEM: add a button that produces a PDF of the BIDS validation
results.

Should this PDF include a file listing to make sure that the dataset has
not been altered.

Add a list of BIDS ignore files:

> [[https://github.com/bids-standard/bids-validator/issues/1676]{.underline}](https://github.com/bids-standard/bids-validator/issues/1676)
>
> [[https://github.com/bids-standard/bids-validator/issues/1677]{.underline}](https://github.com/bids-standard/bids-validator/issues/1677)

Should we reach out to the new **Imaging Neuroscience** journal while
they are still developing their platform?

Potentially reach out to someone on their [[editorial
board]{.underline}](https://janeway.imaging-neuroscience.org/editorialteam/)
- possible Thomas Yeo, Damian Fair

**NSF POSE WORKSHOP**

A funding mechanism for conferences and workshops. (note: Proposals
under \$100k are reviewed internally)

They intend to do a workshop on open source models for data and metadata
standards.

Timing: First quarter of 2024 - Ariel is planning a submission that
includes interdisciplinary colleagues at UW, proposal due mid June

BIDS Steering Committee may be included on a list of invited speakers
(not required to attend).

Could this be a line of funding for BEPS? - the goal is not
neuro-focused, BIDS has good practices to share, but a proposal would
need to be interdisciplinary.

Are there cross sectional topics that could be considered? E.g. other
modalities, or repositories, provenance. what other standards are out
there? Physics, astronomy, CERN

**BIDS workshop prep questions**

Goal of the questions is to help focus the upcoming workshop, identify
areas of agreement.

Suggested Meeting discussion point: what level of analysis steps should
be included and how should those steps/data be reported and/or stored.
This would allow reproducibility of results

Other questions to address:

OHBM BIDS Townhall:

BIDS should be considered as a part of the Best practices, Cyril will
contact the Program committee about establishing a yearly townhall spot
guaranteed

Add to the next agenda website updates - who has done it and how do we
update in the future?
