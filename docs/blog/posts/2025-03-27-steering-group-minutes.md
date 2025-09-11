---
date: 2025-03-27
slug: "Steering Group minutes"
author: anonymous
categories:
-   steering group minutes
---

## Participants

- Yaroslav Halchenko
- Dora Hermes
- Camille Maumet
- Kim Ray
- Chris Markiewicz
- Franco Pestilli

## Agenda

1. Copenhagen maintainer meeting
2. Follow up on cardiac BEP
3. BEP045 (Physio)
    > email from BEP045 (Physio), is input needed from steering?
4. Maintainers Updates [name= all maintainers]
    - MEDD draft written. Does steering have a group account? Or who is sending?
    - New maintainer: Julia-Katharina Pfarr
    - Conflict of interest on BEPs
    - Status updates for BEPs being solicited

## Meeting Minutes

### Copenhagen Meeting

- Chris M - waiting on purchase order from Copenhagen (could be any time) but still no guarantee on whether the full procedure will be feasible in the timeframe.
- timing is getting quite tight
- Camille M - suggests planning a meeting for next year in France that pairs well with OHBM. This will help with future maintainers meetings.
- Current status, 'wait and see' for if/when contracts get approved and if its too late to still have the meeting.

### Follow up on cardiac BEP

- Camille M - where is this standing currently?
- Chris M - discussed in maintainers meeting, medical imaging BEP was encouraged to do a more focus BEP
- maintainers feel that the brain aspect of the BEP is within scope, but the cardiac specific piece might out of scope, this could be kept at arms length.
- Dora:  Are the BEP leads close to brain imaging or imaging adjacent?
- Chris M:  there are some neuroimaging researchers listed on the BEP contributors list, we are not familiar with the lead.
- Camille M : is this stuck because of the previous vote?  how can we get this un-stuck and respond to the BEP leads?
- Chris M: we try to have a BIDS maintainer leads to advocate for the BEP, Christine took this role for the previous vote.  Cardiac BEP contributors would like to have confidence that the BEP will likely be approved before putting all of the work in.
- How can we get Steering group attention for these type of items that need voting: (so that steering is not being asked to vote on something they have 5 minutes notice to)
    - mattermost tagging
    - email (BIDS steering email bids.steering@gmail.com)
    - request for 1-2 weeks notice depending on the time needed to give an informed vote
    - this should be added into a governance document.
- Chris M can work with Christine to put together an email for bids steering group.
- Dora mentions wanting some philosophy support the need for the BEP, and why it should be part of BIDS.
- Franco, this is key to the dicsusion where BIDS needs to determine to what degree they want to extend BIDS beyond the brain and if we have the bandwidth to do so.
- Dora - physio has SPARC (https://www.biorxiv.org/content/10.1101/2021.02.10.430563v2inspired by BIDS) which is related but makes more sense for non-brain studies, so we should better understand the need for this BEP
- Franco - do we have a network outside of BIDS? (eg SPARC/GA4GH) that we could contact when BEP requests come in that might not be best for BIDS but may fit better with other standards.
- Yaroslav - we have a related issue for this https://github.com/bids-standard/bids-2-devel/issues/62
- Camille - a resource for searching for standards https://fairsharing.org/search?fairsharingRegistry=Standard
- Chris - how do we join this community in a meaningful way? the Steering group may not have the expertise now, but could in the future so how do we work with this?
- Yarik - Idea to have BIDS "modules" that can have a different process than BEPS. This could be applicable for 'other body' parts that are outside the expertise of the core BIDS community. Here we could instead as BIDS module leads to submit a list of people/groups they think would be relevant to review the proposed standard.

### BEP045 (Physio)

- bids steering recieved an email from them that needs a reply.
- YH: we should look at the BEP, see what they are doing, see if they need guidance
- Chris M: Rémi has been working on this BEP, but he not able to continue supporting the BEP.
- KR: suggests responding to Mary asking for a more formal email comparable to what we are asking for the Cardiac BEP that include more information so that Steering can vote on if it should move forward.
- YH: suggests clarifying that derivatives part of the BEP might need to be separate.  https://github.com/bids-standard/bids-website/pull/640
- YH: sends github response suggesting to split BEP, following Rémi's prior suggestion: https://github.com/bids-standard/bids-specification/issues/1675#issuecomment-2758164848

### Maintainers Updates

- MEDD format (.medd extension?) draft email written.
    - Who is sending? Should be steering, since it's a steering decision. Is there a common email, or will one person take the lead?
    - Camille to ask Dora if she can send the email, Franco to update the text, Chris to add guidelines to BIDS website
    - Guidelines
        - Currently spread across [BEP guidelines](https://bids.neuroimaging.io/extensions/guidelines.html), aimed at BEP leads. Should we split into a generic "BIDS contribution guidelines" and a targeted BEP-specific guidelines?
- Julia-Katharina Pfarr: Postdoc (?) w/ JB Poline. Worked on eyetracking BEP.
- COI on BEPs
    a) Hard to avoid. Maintainers best suited to shepherd a BEP are those closest to the data types and thus community.
    b) We're working on a BEP status pipeline and dashboard for transparency. Hopefully this can address the general concern and identify specific concerns that can be discussed?
    c) If process needs to be discussed, a synchronous steering+maintainers meeting makes sense. Probably should block 1.5-2 hours to avoid rush. Copenhagen would be ideal, if it happens.
- BEP health checks
    - Contacting BEP leads for status and blockers in prep for town hall.

## Tasks

==Importance== (1 - 5) / Name

### Steering Group:
- [ ] ==1==  Connect with SPARC to see how its related to BIDS [ Dora ]
- [ ] ==1== Reply to physio BEP, suggesting to follow Rémi's guidance [Yaroslav sends github response echoing Rémi]
- [ ]  ==5== Steering Group please send out MEDD email from bids.steering email address [Camille, but maybe Dora since she is more familiar with MEDD]
