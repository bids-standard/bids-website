---
date: 2024-02-22
slug: Steering Group minutes
author: anonymous
categories:
-   steering group minutes
---

<!-- more -->

<table>
 <colgroup>
  <col style="width: 47%"/>
  <col style="width: 52%"/>
 </colgroup>
 <thead>
  <tr class="header">
   <th>
    <strong>
     Topic
    </strong>
   </th>
   <th>
    <strong>
     Relevant Links and to do
    </strong>
   </th>
  </tr>
  <tr class="odd">
   <th>
    BEP for dimensionality reduction-based networks
   </th>
   <th>
    Peer Herholz
   </th>
  </tr>
  <tr class="header">
   <th>
    Avoiding BEP being stuck
   </th>
   <th>
    Issue with Atlas BEP - circulate the idea of revising BEP
development - one point missing in those discussions is how to get
unstuck if conflict (CP: item voting is my favorite option, we just
need the mechanism for it - like we do to elect this group)
   </th>
  </tr>
  <tr class="odd">
   <th>
    Cooperation with DICOM standard
   </th>
   <th>
    YOH pointed David Clunie to our
    <a href="https://docs.google.com/spreadsheets/u/0/d/1wcal4qi2z14bSKm7lTuqyzb3FdvmCDfXHl0iMhIFeaE/edit">
     <u>
      DICOMs
deficits table
     </u>
    </a>
    , he forwarded to WG-16 to consider at the next
meeting.
   </th>
  </tr>
  <tr class="header">
   <th>
    Updates on plan for website
   </th>
   <th>
    <a href="https://docs.google.com/document/d/1miuxSWHcSq0CQ-aufe8Ho0IJpJOirUogCd2HNOi5FHY/edit#heading=h.li30raxumiv7">
     <u>
      BIDS
Online Presence Working Group: Working Document
     </u>
    </a>
   </th>
  </tr>
  <tr class="odd">
   <th>
    BIDS 2.0 going forward!
   </th>
   <th>
   </th>
  </tr>
  <tr class="header">
   <th>
    BEP guidelines updating (Camille &amp; Remi)
   </th>
   <th>
    <a href="https://github.com/bids-standard/bids-extensions/pull/28">
     <u>
      https://github.com/bids-standard/bids-extensions/pull/28
     </u>
    </a>
   </th>
  </tr>
 </thead>
 <tbody>
 </tbody>
</table>

**Present:** Yarik, Kim, Ariel, Cyril, Eric, Christine, Camille

**Apologies:** Dora

**Guest:** Peer Herholz

## BIDS Meeting Notes

### Plan for website

-   Eric is chairing the BIDS Online Presence Working Group
-   Eric owes the open letter to the Steering Group
-   May use google season of docs (need to sign up for the program, starts April 2nd for applications)
-   Will reach out to INCF to reconnect as the admin for google season of docs
-   Mentors identified: Eric, Christine, and Remi (outlined in doc linked in agenda)
-   Eric will reach out to the group to schedule a follow up meeting.
-   Yaroslav reminded the group that he has \$5k CAD to compensate for work on this project

BEP39 for dimensionality reduction-based networks

[[https://docs.google.com/presentation/d/1SLvZ7um3RQAiDr6KeK8eO_mNoQ0qHl_bzx_gqIS169Y/edit#slide=id.g152266b1f78_0_45]](https://docs.google.com/presentation/d/1SLvZ7um3RQAiDr6KeK8eO_mNoQ0qHl_bzx_gqIS169Y/edit#slide=id.g152266b1f78_0_45)

-   May need to introduce new terminology (something akin to an
  \'index', param-mixing, param-components, something akin to
  \'model')
-   Eric suggests instead of \'index' potentially like
  [[\*\_aslcontext.tsv]](https://bids-specification.readthedocs.io/en/stable/appendices/arterial-spin-labeling.html#_aslcontexttsv-three-possible-cases)

    -   [[https://bids-specification.readthedocs.io/en/stable/appendices/arterial-spin-labeling.html#\_aslcontexttsv-three-possible-cases]](https://bids-specification.readthedocs.io/en/stable/appendices/arterial-spin-labeling.html#_aslcontexttsv-three-possible-cases)

-   \<modality\>map : discussion determined _modality_ is a suffix

      -  Related discussion

  [[https://github.com/bids-standard/bids-2-devel/issues/58#issuecomment-1711758273]](https://github.com/bids-standard/bids-2-devel/issues/58#issuecomment-1711758273)

-   \'model-ICA_description.json' : suggestion to rename file as
    \'dataset_dscription.json' and include \'DatasetType: model" and
    model-ICA_mfp.json similarly to \'task-xxx_bold.json

-   Current state is to build up and extend \'spatiotemporal decompositions' introduced in BEP 012
-   Interoperability : BIDS-Prov
-   [[https://github.com/bids-standard/BEP028_BIDSprov/blob/master/examples/from_parsers/spm/spm_default_batch.jsonld#L65-L77]](https://github.com/bids-standard/BEP028_BIDSprov/blob/master/examples/from_parsers/spm/spm_default_batch.jsonld#L65-L77)
-   Software parameters is similar to BIDS-prov's Parameters
    description (what is the specific file?)

### Stalled BEPS

Should there be a mechanism for addressing conflicts that halt BEP
progress?

Suggestion:

1. a voting system similar to how the steering group is elected.

How would we want to implement something like this while addressing concerns of FAIRness?

2. BEP leader determines how to move forward.

3. Could a technical committee make these decisions? (maintainers +
steering group) - if there is quorum possibility to vote one way or the
other**

When do we modify the schema to address new ideas?

### DICOM

### BIDS 2.0

### BEP guidelines updating
