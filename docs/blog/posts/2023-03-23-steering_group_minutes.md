---
date: 2023-03-23
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
    “Model” / “Resultset” directory proposal
   </td>
   <td>
    <a href="https://github.com/bids-standard/bids-specification/pull/1280">
     <span class="underline">
      https://github.com/bids-standard/bids-specification/pull/1280
     </span>
    </a>
   </td>
  </tr>
  <tr class="even">
   <td>
    BIDS Derivatives retreat June 21st - 23rd
   </td>
   <td>
    <a href="https://openneuropet.github.io/bidsderivativemeeting/">
     <span class="underline">
      https://openneuropet.github.io/bidsderivativemeeting/
     </span>
    </a>
   </td>
  </tr>
  <tr class="odd">
   <td>
    Summary of the PET-BIDS derivatives meeting
   </td>
   <td>
    <a href="https://docs.google.com/document/d/1yzsd1J9GT-aA0DWhdlgNr5LCu6_gvbjLyfvYq2FuxlY/edit#heading=h.mqkmyp254xh6">
     <span class="underline">
      BIDS Extension Proposal 23 (BEP023): PET Preprocessing Derivatives
     </span>
    </a>
   </td>
  </tr>
  <tr class="even">
   <td>
    Meeting with the DICOM team
   </td>
   <td>
    Yaroslav sent a follow up email offering to join DICOM committee meeting
   </td>
  </tr>
  <tr class="odd">
   <td>
    <p>
     Stefan: Here are three issues that could benefit from steering input (in particular those familiar with ephys experience)
    </p>
    <ul>
     <li>
      <blockquote>
       <p>
        https://github.com/bids-standard/bids-specification/pull/1441
       </p>
      </blockquote>
      <blockquote>
       <p>
        https://github.com/bids-standard/bids-specification/issues/1436
       </p>
      </blockquote>
      <blockquote>
       <p>
        https://github.com/bids-standard/bids-specification/issues/1446
       </p>
      </blockquote>
     </li>
    </ul>
   </td>
   <td>
   </td>
  </tr>
 </tbody>
</table>

## Notes

"Model" / "Resultset" directory proposal derivatives [pull
request](https://github.com/bids-standard/bids-specification/pull/1280)

New proposal of models (for example dti models) where derivatives may be
created from this model thus creating parameters and derivatives of a
model that have overlapping meta-data.

Proposed Solution:

-   add a 'results' directory that contains the files of the model with
    metadata describing those files. Is it okay to add an additional
    nested directory like this?

-   MFP (model fit parameter) and MDP (model derived parameter) suffixes

Concern:

-   this appears to be very dwi specific, should the suffixes be dwi
    specific?
-   Why is datatype not under model label in the [pull
    request](https://github.com/bids-standard/bids-specification/pull/1280)
    example?
-   Is the proposed organization of data aligned with user community? -
    should we request input from community to determine where these
    results should be stored
-   [https://github.com/bids-standard/bids-specification/issues/751\#issuecomment-820800800](https://github.com/bids-standard/bids-specification/issues/751#issuecomment-820800800)
-   How does this apply to more general data modalities? Like mEEG,
    SPECT - more use cases beyond dMRI would be helpful
-   "BIDS-like derivatives in other modalities:
    [https://data.donders.ru.nl/collections/di/dccn/DSC\_3031000.00\_191?0](https://data.donders.ru.nl/collections/di/dccn/DSC_3031000.00_191?0), see also
    [https://github.com/Donders-Institute/infant-cluster-effectsize](https://github.com/Donders-Institute/infant-cluster-effectsize)
    (for the scripts that generate the result)
-   Other ideas: tarballs instead of directories, HDF5 files instead of
    directories.


BIDS Derivatives Retreat

-   For general derivatives group (not just pet)
-   See link for more information

Summary of the PET-BIDS derivatives meeting

-   Meeting happened 2 weeks ago (March 10th)
-   Mostly an onboarding meeting for the importance and relevance of
    PET-BIDS derivatives
-   Raw PET data is now part of BIDS, now the second half of the white
    paper will address the derivatives aspect of PET
-   The PET users are more clinically oriented, more diverse user
    groups, less agreement within the community in data standards
-   The community is between two ideas: a more restrictive approach with
    data types allowed, or free datatypes with detailed provenance

Meeting with the DICOM team

-   We need to formalize our current state of affairs, see which terms
    align/ dont align
-   We need to follow up on email from Kim on Feb 14 asking to present
    at a dicom committee meeting.
