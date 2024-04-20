---
date: 2023-03-02
slug: Steering Group minutes
author: anonymous
---

# Steering Group minutes 2023/03/02

Date: Thursday, March 2nd, 2023

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
    Peer Herholtz Guest: Discussing two Atlas BEPs
   </td>
   <td>
    <a href="https://github.com/bids-standard/bids-specification/issues/1379">
     <span class="underline">
      https://github.com/bids-standard/bids-specification/issues/1379
     </span>
    </a>
   </td>
  </tr>
 </tbody>
</table>

## NOTES

**Present:** Robert Oostenveld, Guiomar Niso, Cyril Pernet, Ariel Rokem,
Chris Markiewicz (Maintainer guest), Yaroslav Halchenko, Kim Ray
(Secretariat)

**Guest: Peer Herholtz**

Peer Herholtz - Atlas BEPs

September 2022 BIDS Connectivity Project started an Atlas BEP (led by
Peer)

Jan 2023 another community started an Atlas BEP
([flyxiaye](https://github.com/flyxiaye))

Feb 2023 both BEP leads met, Talo Salo was in attendance, to determine
how the teams should move forward

Conclusion:

- Peer's BEP focuses on storing utilizing writing analyses
- [flyxiaye](https://github.com/flyxiaye): focuses on
  how atlases should be characterized, described, and what meta-data is
  needed to navigate an atlas. (Taylor Salo mentioned this BEP doesn't
  follow the typical BEP flow, similar to template flow)
- the two BEPs appear complementary yet distinct. The teams will move
  forward and collaborate where possible.

Comments:

How much are atlas BEPs tools or extensions? If they are tools, then
perhaps they should be BIDSapps.

-   The goal of Peer's Atlas BEP is to provide a way to include
    atlas/ROI/template information in derivatives for connectivity
    analyses

Inside the specification - where does the Atlas BEP fit?

-   Could be part of BEP 17 connectivity matrices, or statistical
    models, as well as others

-   Should align with other BEPs (for example provenance BEP)

-   It's been proposed to have an atlas directory by Peer's working
    group, but agrees that the atlas can be applicable in different
    way

-   RAW is defined by something that is provided by 'hardware',
    Derivatives is data that's been derived from raw - thus atlases
    should be in derivatives?

-   Peer's Atlas BEP currently suggests storing atlases in derivatives
    or in subject level

-   Could atlas be considered as a separate subject?(Guio)

-   Example: MEG has unique file formats, EEG has many caps, but does
    this need to be stored in BIDS

-   BIDS defines standard templates at:
    [https://bids-specification.readthedocs.io/en/stable/appendices/coordinate-systems.html\#standard-template-identifiers](https://bids-specification.readthedocs.io/en/stable/appendices/coordinate-systems.html#standard-template-identifiers)

-   These things (altases, ROIs) are well defined. They should be
    formalized in BIDS, but clearly it\'s not yet agreed upon how or
    where.
