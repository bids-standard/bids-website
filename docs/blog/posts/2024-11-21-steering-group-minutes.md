---
date: 2024-11-21
slug: "Steering Group minutes"
author: anonymous
categories:
-   steering group minutes
---

<!-- more -->

## Participants

-   Ariel Rokem (fairwell!)
-   Camille Maumet
-   Yaroslav Halchenko
-   Dora Hermes
-   Franco Pestilli
-   Kim Ray
-   Chris Markiewicz
-   James Kent
-   Ju-Chi Yu
-   Robert OostenVeld

## Robert OostenVeld, EEG file formats

- MED is a new file format, a clinical format
    - Nominally an update of the MEF3 format which is widely supported
- The file formats are a little different, there are no common readers, not yet supported by the community
- file format may be a privatized from a clinical nuerologist (MEF3, MET stat), its not a free format
- YH: since its not free, do we need to support them?
- RO: this is a newer format that is potentially being added last minute, has not yet been community vetted.
- YH:  should we establish requirement for adding a new file format?  e.g. adoption
- RO: wide adopt is a current criteria, and its not yet met.  It shouldu also add additional value, and that has not yet been established.
- CP: we should establish a procedure for adding new formats based on this request
- CM: where should the procedure be established?
- others: where other guidelines are provided on the BIDS website.
- CP: we should not support this file format because it does not meet criteria, we should share the criteria with them
- RO: suggested responding that the steering group choose not to include it now, but that it could be included in BIDS 2.0 [name=Chris Markiewics]
- Steering Group decicions:  to not include at this time.

## OSR Room

-wanting to have a BIDS opener at OHBM
    - there will be a platform for the town hall this year
        - either crowdcast or zoom, decision has not been made yet. With zoom you can do youtube streaming at the same time.
- OSR there was not a good attendance last year, they are looking for more engagement
- would like for a 20-30 minute BIDS summary.
- Who from BIDS will be at OHBM that can present?
    - Remi mentioned that BIDS townhall will likely not be during OHBM but the OSR can support this using their platform.
    - Franco will be attending, Kim Ray will attend.
    - CP:  yes BIDS will have a representative that present during the opener, the person can be identified later.
    - CamM: townhall online is more inclusive and important, can the OSR detail more about what they are expecting BIDS to present?
    - JY: not a beginner, looking for a BIDS update and where the community can contribute. They are planning about a 10-20 minute slot, but could have up to 45 mins.
    - AR: since a townhall is already being planned, a shorter presentation seems appropriate.
    - JK:  suggests to condense the BIDS townhall for the BIDS opener
    - JY:  they are planning to bring the hacking space back to the OSR
      which might have been why last year's OSR was less successful.
    - CM: when should we let OS-Sig know how long BIDS would like to present?
    - JY: December.
    - CamM: 20 minutes is reasonable
    - JY: OS-Sig will provide the platform for BIDS townhall, the platform is not yet determined but they will support.
    - CamM: we should have/create an email account - the steering group needs to have a mechanism for communication (other than slack) (Camille will do, added to the todo items).

## New Steering Group Member

- Franco Pestilli
- Welcome!
- Which accounts does Franco need to join/gain access to?
    - slack, hackmd, google drive, mattermost, github teams (owner permissions - Chris M will do this)
- share the source for maintainer updates with Franco
    - https://hackmd.io/l_wJqwrTR_Go3bWd0My19g
- NIH DCC - BIDS will need microsopy.

## 1Additional Discussion

- we decided to move to mattermost a while ago but never adopted it, let's do it now.
- AR added steering group members, should all members be allowed to be in the group?
- CM: supports all SG members, we will move forward with all steering group members.
