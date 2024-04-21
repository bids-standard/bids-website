---
date: 2023-02-09
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
     Community projects board
    </p>
    <ul>
     <li>
      <blockquote>
       <p>
        Under ‘get involved’ on homepage
       </p>
      </blockquote>
     </li>
    </ul>
   </td>
   <td>
   </td>
  </tr>
  <tr class="even">
   <td>
    <p>
     Task definition:
    </p>
    <ul>
     <li>
      <blockquote>
       <p>
        Task addition for all other modalities besides fMRI
       </p>
      </blockquote>
     </li>
     <li>
      <blockquote>
       <p>
        Clarification of tasks in appendix
       </p>
      </blockquote>
     </li>
    </ul>
   </td>
   <td>
    <p>
     Task addition PRs:
    </p>
    <p>
     <a href="https://github.com/bids-standard/bids-specification/pull/1185">
      <span class="underline">
       Anat
      </span>
     </a>
     - merged
    </p>
    <p>
     <a href="https://github.com/bids-standard/bids-specification/pull/1196">
      <span class="underline">
       PET
      </span>
     </a>
     - merged
    </p>
    <p>
    </p>
    <p>
     <a href="https://github.com/bids-standard/bids-specification/issues/1314">
      <span class="underline">
       Task clarification
      </span>
     </a>
     - merged
    </p>
   </td>
  </tr>
  <tr class="odd">
   <td>
    <p>
     BIDS derivatives meeting
    </p>
    <ul>
     <li>
      <blockquote>
       <p>
        organized by OpenNeuroPET project
       </p>
      </blockquote>
     </li>
     <li>
      <blockquote>
       <p>
        end of march PET BIDS derivatives
       </p>
      </blockquote>
     </li>
     <li>
      <blockquote>
       <p>
        General BIDS derivatives - 3rd week of June in Copenhagen - invites to follow for all BEP leads + maintainers (‘we’ openneuro PET have some budget for this ; applying for more)
       </p>
      </blockquote>
     </li>
    </ul>
   </td>
   <td>
   </td>
  </tr>
  <tr class="even">
   <td>
    <p>
     Update governance (added by Rémi):
    </p>
    <p>
     Rémi and Eric met to talk about several things.
    </p>
    <ul>
     <li>
      <blockquote>
       <p>
        Ask “Does the Governance website and documentation state how it itself should be amended?”
       </p>
      </blockquote>
     </li>
     <li>
      <blockquote>
       <p>
        Propose governance for an Advisory Group members’ (lead of merged BEP) commitment:
       </p>
      </blockquote>
      <ul>
       <li>
        <blockquote>
         <p>
          Cannot ask them to commit for life
         </p>
        </blockquote>
       </li>
       <li>
        <blockquote>
         <p>
          maybe 2 year minimum plus designating a successor, or some such thing
         </p>
        </blockquote>
       </li>
      </ul>
     </li>
     <li>
      <blockquote>
       <p>
        Draft email for consent of completed BEP leads for them to be part of the Advisory group or to nominate someone(s) else
       </p>
      </blockquote>
     </li>
    </ul>
   </td>
   <td>
    <p>
     <a href="https://bids.neuroimaging.io/governance.html">
      <span class="underline">
       https://bids.neuroimaging.io/governance.html
      </span>
     </a>
    </p>
    <p>
     <a href="https://docs.google.com/document/d/18PpfSgcHckqejTZsRZlEDlJ_yD3JiwSQ8kCjVXorg6U/edit">
      <span class="underline">
       https://docs.google.com/document/d/18PpfSgcHckqejTZsRZlEDlJ_yD3JiwSQ8kCjVXorg6U/edit
      </span>
     </a>
    </p>
   </td>
  </tr>
  <tr class="odd">
   <td>
    Chris Rorden also got in touch with the DICOM working groups recently to bring up similar issues he raised in the last Steering Committee Meeting. (KIM RAY)
   </td>
   <td>
    <p>
     <a href="https://docs.google.com/document/d/1cxv1o4FVALb9sZPX7Jr2XIAyvP6zBd5xQV5BzISFZ7Q/edit?usp=sharing">
      <span class="underline">
       https://docs.google.com/document/d/1cxv1o4FVALb9sZPX7Jr2XIAyvP6zBd5xQV5BzISFZ7Q/edit?usp=sharing
      </span>
     </a>
    </p>
    <p>
     Copy of email chain from Chris with DICOM working groups.
    </p>
   </td>
  </tr>
 </tbody>
</table>

## Notes

Suggestion to add make the [decision making
rules](https://github.com/bids-standard/bids-specification/blob/master/DECISION-MAKING.md)
more visible

Is this a suggestion to make the team more visible or funding, including
for example BEP funding like
[https://www.nature.com/articles/sdata2018110\#Ack1](https://www.nature.com/articles/sdata2018110#Ack1)?
The team, and BEP leaders, as well as funding and who is supported by
the funding

Guio: we need to revisit the BIDS funding landing page, and update the
figures. Suggested to prioritize these updates during a brain hack?

Stefan: The Maintainers team does not have capacity to redesign the
website.

ACTION: Yaroslav will submit a pull request/issue (done:
[https://github.com/bids-standard/bids-website/pull/279](https://github.com/bids-standard/bids-website/pull/279)
for starters) with table to github to add funding and a link to the
contributor/funders page and Stefan will follow up

Task definitions (Cyril): task was specific to fMRI, however it has now
been added to PET, and MRI anat, see
[pull](https://github.com/bids-standard/bids-specification/pull/1392).
However it still needs to be implemented in the BIDS validator and
examples. See issues below:

Outstanding, but WIP:
- [https://github.com/bids-standard/bids-validator/pull/1578](https://github.com/bids-standard/bids-validator/pull/1578)
- [https://github.com/bids-standard/bids-validator/issues/1564](https://github.com/bids-standard/bids-validator/issues/1564)

BIDS derivatives meeting : next week the first round of invites will be
extended, looking for more funding to support travel. Aiming for 20-30
attendees. Currently some people will have some, limited, or no
financial support for travel to the meeting.

Considerations: What is the plan for the Program ? Will there be a
hybrid option?

Current suggestions (Cyril), have people come with data and complete
examples to improve BEPS

Stefan:

- Amendment 1 - every BEP lead will join the BIDS advisory group
forever (not ideal), proposed to allow individuals to leave the
advisory group after 2 years and asked to suggest a replacement.
- Amendment 2 - we don\'t currently have a process to change the BIDS
governance, some solutions have been put forth:
[https://docs.google.com/document/d/18PpfSgcHckqejTZsRZlEDlJ\_yD3JiwSQ8kCjVXorg6U/edit](https://docs.google.com/document/d/18PpfSgcHckqejTZsRZlEDlJ_yD3JiwSQ8kCjVXorg6U/edit)
- Amendment 3 - BIDS contributors - governance states that all
contributors are equal, but this needs to be amended because many
contributors at some point are no longer active and this creates issues
when minimum % of votes are required for certain elections. WIP for
current and new wording - maintainers are working on this and the
steering group can comment and give feedback.

GUIO: Suggestion to include a list of Advisory Group members.

Robert: What is the order of amendments to be approved?

Stefan - suggests all amendments to be at once. This has been done
before, there is precedence.

Yaroslav: recommends new language to define active & inactive advisory
group members.

Chris Rorden also got in touch with the DICOM working groups - its a
good idea, however its possibly beyond the expertise of individuals in
the steering group and beyond the time constraints of the BIDS steering
group.

Alignment with BIDS and DICOM should be encouraged, but time is the
obstacle for working with DICOMs. Maybe DICOM working group 16 may be
worthwhile to interact with to inform/influence their decision making to
align with BIDS.

Can Chris facilitate this with working group 16? Perhaps Yarik can voice
steering group issues with guidance from Chris (who is likely most
familiar with issues between DICOM and BIDS).

**ACTION**: email DICOM and present BIDS to them with support form Chris.

DICOM meeting notes - https://www.dicomstandard.org/activity/wgs

Cyril: discussed with aperture on submitting data papers (including a
logo to indicate the dataset is BIDS compliant). data must be BIDS
validated, it must include a sharing statement, if its not on openneuro
then there must be a way to ensure it is BIDS validated. Cyril will make
progress on this to be approved by aperture.

Ariel: what is the status of BIDS being included in COBIDAS?

Future Guests? None identified yet.

Non-invasive stimulation - making good progress

Two Atlas BEPS
https://github.com/bids-standard/bids-specification/issues/1379
