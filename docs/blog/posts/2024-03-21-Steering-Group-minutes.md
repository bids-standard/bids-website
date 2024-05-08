---
date: 2024-03-21
slug: "Steering Group minutes #69"
author: anonymous
categories:
-   steering group minutes
---

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
     Relevant Links and to do
    </strong>
   </th>
  </tr>
 </thead>
 <tbody>
  <tr class="odd">
   <td>
    <del>
     <strong>
      Guest
     </strong>
     Franco Pestilli
    </del>
   </td>
   <td>
   </td>
  </tr>
  <tr class="even">
   <td>
    Cooperation with DICOM standard
   </td>
   <td>
    <p>
     YOH pointed David Clunie to our
     <a href="https://docs.google.com/spreadsheets/u/0/d/1wcal4qi2z14bSKm7lTuqyzb3FdvmCDfXHl0iMhIFeaE/edit">
      <span class="underline">
       DICOMs deficits table
      </span>
     </a>
     , he forwarded to WG-16 to consider at the next meeting March Wed 13th, 2024.
    </p>
    <ul>
     <li>
      <blockquote>
       <p>
        <a href="https://github.com/bids-standard/bids-specification/issues/1515">
         <span class="underline">
          https://github.com/bids-standard/bids-specification/issues/1515
         </span>
        </a>
        (?)
       </p>
      </blockquote>
     </li>
    </ul>
   </td>
  </tr>
  <tr class="odd">
   <td>
    BIDS 2.0 going forward!
   </td>
   <td>
    <ul>
     <li>
      <blockquote>
       <p>
        <a href="https://github.com/orgs/bids-standard/projects/10">
         <span class="underline">
          https://github.com/orgs/bids-standard/projects/10
         </span>
        </a>
       </p>
      </blockquote>
     </li>
     <li>
      <blockquote>
       <p>
        <a href="https://github.com/bids-standard/bids-2-devel/issues">
         <span class="underline">
          https://github.com/bids-standard/bids-2-devel/issues
         </span>
        </a>
       </p>
      </blockquote>
      <ul>
       <li>
        <blockquote>
         <p>
          Some new since last time, e.g.
         </p>
        </blockquote>
       </li>
       <li>
        <blockquote>
         <p>
          <a href="https://github.com/bids-standard/bids-2-devel/issues/65">
           <span class="underline">
            issues/65
           </span>
          </a>
          - summarization as a flavor of inheritance
         </p>
        </blockquote>
       </li>
       <li>
        <blockquote>
         <p>
          <a href="https://github.com/bids-standard/bids-2-devel/issues/66">
           <span class="underline">
            issues/66
           </span>
          </a>
          - generalize common principles into DSS (data structure standard)
         </p>
        </blockquote>
       </li>
      </ul>
     </li>
    </ul>
   </td>
  </tr>
  <tr class="even">
   <td>
    BEP guidelines updating (Camille &amp; Rémi)
   </td>
   <td>
    <p>
     <a href="https://github.com/bids-standard/bids-extensions/pull/28">
      <span class="underline">
       https://github.com/bids-standard/bids-extensions/pull/28
      </span>
     </a>
    </p>
    <p>
     See Oscar’s vision of having BEP leads as core experts of BIDS and other domain expert be contributors (i.e. not lead BEPs)
     <a href="https://github.com/bids-standard/bids-extensions/pull/28#discussion_r1528721354">
      <span class="underline">
       https://github.com/bids-standard/bids-extensions/pull/28#discussion_r1528721354
      </span>
     </a>
    </p>
   </td>
  </tr>
  <tr class="odd">
   <td>
    BEP guidelines PR on technical committee
   </td>
   <td>
    <a href="https://github.com/bids-standard/bids-extensions/pull/29">
     <span class="underline">
      https://github.com/bids-standard/bids-extensions/pull/29
     </span>
    </a>
   </td>
  </tr>
  <tr class="even">
   <td>
    <p>
     Unsticking BEPs (may be covered by previous topics). Maintainer suggestions:
    </p>
    <ol type="1">
     <li>
      <blockquote>
       <p>
        Steering directly mediate conflicts
       </p>
      </blockquote>
     </li>
     <li>
      <blockquote>
       <p>
        "BEP delegates" a la Python
       </p>
      </blockquote>
     </li>
    </ol>
    <p>
     Rough consensus: Resolve first, formalize process later
    </p>
   </td>
   <td>
   </td>
  </tr>
 </tbody>
</table>

**Present:** Kim Ray, Camille Maumet, Yarik Halchenko, Ariel Rokem,
Chris Markiewicz, Dora Hermes

**Apologies:**

**Guest:** Franco Pestilli

## BIDS Meeting Notes

Franco is sick, so meeting with him deferred to future meeting (possibly next time, April 4th)

### Cooperation with DICOM standard

YOH met with them to discuss issues between BIDS and DICOM

-   Dicom cannot enforce anything, and its difficult for them to suddenly make things mandatory

-   YOH will meet with GE manufacturer this Fri to discover more about "IHE Sharazone",
    which is a system that the vendors use to share example data between them to check for compatibility across.
    It seems that this is rather closed down, so hard to access and contribute to.

-   Overall, the call useful in the context that DICOM folks are now more aware of incompatibilities between BIDS and DICOM

### BIDS 2.0 going forward!

YOH

-   A replacement/substitution of inheritance principles would be useful
   (allows you to define common metadata at the top level and more specific metadata at lower levels)

    -   Proposed: limit that values cannot be overloaded

    -   Related: [[BEP036 - Phenotypic Data]](https://bids.neuroimaging.io/bep036)

    -   Does not conflict with Dora\'s use cases where EEG participants often each have different metadata
        (e.g. number of electrodes) and would not have many common metadata across subjects

    -   [[https://github.com/bids-standard/bids-2-devel/issues/65]](https://github.com/bids-standard/bids-2-devel/issues/65)

-   Discusses formalizing common principles into a standard

    -   Eg BIDS like standards: [[bids-2-devel/issues/62]](https://github.com/bids-standard/bids-2-devel/issues/62)

-   Might want to reach out to [[PsychDS]](https://psych-ds.github.io/) to create a migration path

-   For example: Allen institute has a file naming schema that we might want to adopt/incorporate

    -   [[bids-2-devel/issues/60]](https://github.com/bids-standard/bids-2-devel/issues/60)

    -   Could help Allen institute merge/adopt BIDS

-   Please add examples to this issue for consideration (issue 62?)

### BEP guidelines updating (Camille & Rémi)

-   Update the process of how people can submit new proposals for BEPS

-   The process of obtaining a BEP number is not clearly outlined

    -   Maintainers are discussing what explicit process should be outlined

    -   [[https://github.com/bids-standard/bids-extensions/pull/28]](https://github.com/bids-standard/bids-extensions/pull/28)

-   The expectation to 'become familiar' with BIDS before starting a BEP is a 'high bar' to attain

    -   Some believe that BEP leads should be BIDS experts and domain experts should be contributors

        -   Concerns exist that this approach may limit entrance to BIDS

-   Suggestions - adopt a procedure similar to debian where experts need to pass an exam to obtain an expert status

    -   Should a BEP lead already be a BIDS contributor to ensure they have some existing BIDS knowledge

-   Often BEP leads are already BIDS familiar because of the steps that they need to create the BEP

    -   Create BIDS examples in a pull request
    -   Add to schema
    -   However sometimes this familiarity is a result of going through the BEP creation process

-   CM: Current loose guidelines for establishing a BEP

    -   Maintainers have a template that they provide to individuals that are interested in creating a BEP, often the maintainers ensure that the BEP lead has contributed to BIDS previously.

    -   There has also been some approval by the steering committee

    -   Currently, BIDS maintainers are not comfortable with the new expectation that they help 'solve' many BIDS issues/concerns (instead of the community agree on solutions)

-   The committee returns to the idea of having a BEP mentor for each BEP that has BIDS/BEP experience and can help guide the BEP lead through the BEP process

    -   This could reduce zombie BEPs (when a BEP is forgotten or not actively being developed)
    -   Could also help with junior people contributing and potentially becoming BEP leads

-   Should there be a google doc or pull request first for a BEP?
