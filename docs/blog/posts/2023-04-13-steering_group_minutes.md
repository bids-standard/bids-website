---
date: 2023-04-13
slug: Steering Group minutes
author: anonymous
---








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
    <p>
     Stefan: Here are three issues that could benefit from steering input (in particular those familiar with ephys experience)
    </p>
    <ul>
     <li>
      <blockquote>
       <p>
        <a href="https://github.com/bids-standard/bids-specification/pull/1441">
         bids-specification 1441
        </a>
       </p>
      </blockquote>
      <blockquote>
       <p>
        <a href="https://github.com/bids-standard/bids-specification/issues/1436">
         bids-specification 1436
        </a>
       </p>
      </blockquote>
      <blockquote>
       <p>
        <a href="https://github.com/bids-standard/bids-specification/issues/1446">
         bids-specification 1446
        </a>
       </p>
      </blockquote>
     </li>
    </ul>
   </td>
   <td>
    <p>
     Cyril: (1) in
     <a href="https://bids-specification.readthedocs.io/en/latest/modality-specific-files/task-events.html">
      <span class="underline">
       https://bids-specification.readthedocs.io/en/latest/modality-specific-files/task-events.html
      </span>
     </a>
     sample is not defined, ie custom column, not sure I follow the why in issue 1441 (2)
    </p>
    <p>
     Issue 1436 -- yes let’s do that, robert also agreed on that (3) seems like there is a consensus
    </p>
   </td>
  </tr>
  <tr class="even">
   <td>
    <p>
     <strong>
      Remi Gau
     </strong>
    </p>
    <p>
     Discussed at the maintainers meeting: a PR that "standardizes" contributors info.
    </p>
    <p>
     This PR does several things: one of them is that it would start adding the list of our contributors (as 'authors') to the zenodo release of the BIDS specification that we get our DOI from.
    </p>
    <p>
     The problem is that there has not yet been an agreement on how authors/ contributors should be listed in those zenodo releases: see this old issue
    </p>
    <p>
     <a href="https://github.com/bids-standard/bids-specification/issues/66">
      <span class="underline">
       [DISCUSSION] acknowledge contributors in DOIed specs on Zenodo · Issue #66 · bids-standard/bids-specification · GitHub
      </span>
     </a>
    </p>
    <p>
     This aspect of the PR can put on hold for now but "we" (the maintainers) felt that it would be good if the steering group took a decision on this old issue (that may actually need rethinking given how much time has passed and that we have had so many new modalities and contributions since it was opened).
    </p>
   </td>
   <td>
    <p>
     <a href="https://github.com/bids-standard/bids-specification/pull/1115">
      bids-specification 1115
     </a>
    </p>
    <p>
     <a href="https://github.com/bids-standard/bids-specification/issues/66">
      bids-specification 66
     </a>
    </p>
   </td>
  </tr>
  <tr class="odd">
   <td>
    Discussion with DICOM - where are we at?
   </td>
   <td>
    Discuss next meeting
   </td>
  </tr>
  <tr class="even">
   <td>
    Discussion with journals - where are we at? (badges for BIDS datasets)
   </td>
   <td>
    <p>
     Aperture is fine with this, but they are in the middle of updating their website
    </p>
    <p>
     Should we push ahead with scientific data? (their staff are familiar with BIDS and may be a good next journal to approach)
    </p>
   </td>
  </tr>
  <tr class="odd">
   <td>
    OHBM best practice?
   </td>
   <td>
    Cyril: John Pyles has circulated the OHBM BIDS 2 doc - reviewing of the proposal?
   </td>
  </tr>
 </tbody>
</table>


## NOTES

Github pull request - [bids-specification 1441](https://github.com/bids-standard/bids-specification/pull/1441)
and [bids-specification 1457](https://github.com/bids-standard/bids-specification/pull/1457)
-   The requesters want to change from number to integer, it was likely
    in a previous version but not in the current.
-   The sample is not defined, this could be defined in the json -
-   This should be fine then

Github pull request: Formalize how channel types are shared between
modalities that use channels.tsv files. [bids-specification 436](https://github.com/bids-standard/bids-specification/issues/1436)

Github pull request: ENH: Array data in .tsv cells - [bids-specification 1446](https://github.com/bids-standard/bids-specification/issues/1446)
-   We might need an example of nesting
-   80/20 rules may need to apply here where we define rules for
    examples that occur 80% of the time.
-   Why not just repeat the rows for each channel? Example: the onset
    time for multiple channels could be listed across multiple rows
    instead of condescending them into a single row/entry (Ariel will
    suggest this in the pull request)

Github pull request: [DISCUSSION] acknowledge contributors in DOIed
specs on Zenodo - [bids-specification 66](https://github.com/bids-standard/bids-specification/issues/66)
-   What rule should be used for author order on zenodo DOI?
-   Proposal: use a random number generator for each new push of authors
    to keep order 'fair' for all, possibly include an alphabetical
    list on the BIDS website for ease of author identification
-   **Final decision: alphabetical is simple and standard, order does
    not imply importance, PR is fine.**
-   Clarify it explicitly in the text

Journals including badges to indicate BIDS compliant dataset:
-   Aperture is agreeable, their website is under development
-   Suggestions: next journal to approach could be **scientific data**
    given their familiarity with BIDS.
-   Action: email the Scientific Data editor in chief from the BIDS
    Steering Committee
-   Question standardization of implementation across journals?
    -   Guio will provide and example draft
-   Question: who/what will identify BIDS compliant datasets?
    -   BIDS validator can, however users can include many \#BIDS IGNORE
        files
    -   Either the validator will need to output bidsignore info or
        reviewers/editors will need to check the bidsignore files
        themselves.

OHBM best practice committee
-   Cyril: John Pyles has circulated the OHBM doc of BIDS 2- reviewing
    of the proposal?
    -   This will be reviewed by individuals external from BIDS
    -   There will be multiple versions , not all versions need to be
        reviewed
-   'What is BIDS' should be presented to the community, who should lead
    this presentation?
    -   Experts from each field?

Was there a podcast ([OHBM Neurosalience](https://www.youtube.com/playlist?list=PLg2e4R8SdhpdIMG7Tb9WAEZA6HRnx8Vsb))
where Peter Bandettini suggested someone talk about BIDS?
-   Originated in October 2022, sounds like a good opportunity for more
    exposure, Cyril will reply to the email thread

Next Meeting Guest:
-   possibly JB Poline regarding a new tool (could be posted as an issue
    on github?)
-   Maintainers met with the functional ultrasound group but they are
    likely too premature for this meeting.

Cyril: the BIDS retreat is looking for additional funding to increase
the support for the meeting. Who should be additionally invited?

MRTRIX team, BIDS connectivity group,
