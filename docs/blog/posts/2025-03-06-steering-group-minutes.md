---
date: 2025-03-06
slug: "Steering Group minutes"
author: anonymous
categories:
-   steering group minutes
---

## Participants

- Franco Pestilli
- Kim Ray
- Christine Rogers (maintainer)
- Eric Earl (maintainer)
- Camille Maumet

## Agenda

1. BIDS meeting `10min`
	- Dates May 12-14
    - Cyril handling travel, pending UW contracts
        * 4-5 nights hotel, [Scandic hotel likely](https://www.scandichotels.dk/hoteller/danmark/kobenhavn/scandic-sydhavnen?&cmpid=ppc_BH2d&s_kwcid=AL!7589!3!650888367006!e!!g!!scandic%20sydhavnen&gad_source=1)
    - Day 1 "Euro-Community outreach day" format - how public?
        - 6 invitees
    - Day 2-3 Maintainers focus
    - Additional Invitees for Day 1 only: from Europe
    - Cyril to start a spreadsheet for Maintainers to complete
    * to invite: Robert, Oscar, Martin N, Hanke (Yarik is reconfirming the availability), Cyril (Day 1+2), Lyuba Zehl? Dora Hermes? Guiomar Niso?
    * likely add-ons:
        * Hugo Boniface
        * Daniel Brady? (new python-validator contributor EEGManyLabs UK)
        * Cyril's list of potential invitees: 2 bids2openmind (2 women perhaps), comp'l models (from Petra's group)
        * invitees more balance: Guio Niso?, (Dora?), Julia-Katharina Pfarr (EU)?
        * In-person format all days; Hybrid would need justification and support
        * Possible invitee: Ghislain Vaillant (who is on the BEP below)?
2. BIDS BEP Approval: Cardiac MRI
    - needs approval from 3 SC members
    - see [BEP046: Cardiac MRI BIDS](https://github.com/bids-standard/bids-specification/issues/2011)
    - Process: Does Steering prefer a group meeting item vs. a Mattermost thumbs-up ask?
    - Governance?
    - stats model - like a bep but not in the spec.  https://bids-standard.github.io/stats-models/
    - 2 Yes: Yarik, Franco
    - 2 No: Cyril, Camille
    - Moving beyond Brain could merit a bigger community discussion,
    - main concern is how to validate if the community is not known to current core of BIDS
    - Franco: listing more PI contributors would help
    - Yarik : identify reviewers in the github issue
    - Draw a stronger connection to Brain data
    - Maintainers (Remi) are working on clarifying the BEP process (what happens when)

3. Franco governance question: relatinoship between the maintainer and the BEP, conflict of interest
4. 2024 Google Season of Docs
    * Maintainers would like to complete the compensation for our 2024 Writer, Damion Demeter.
    * 52% of $5k stipend lost to new Swedish taxation on INCF disbursement.
    * The project was completed successfully, new BIDS website is live, Eric could speak to mechanism.
    * Would BIDS consider contributing $2600 USD to fulfill the project compensation?
    * - Steering votes Yes
    * Yarik will use his funds.

5. INCF Fiscal Sponsorship
    - Concerns raised by maintainers:
    - I think INCF would be a good partner provided clarification on timelines and the taxation categories
        - FWIW: Yarik is reporting that Mathew affirmed that they could take care about signing on contracts like the one for [IHE_SHARAZONE](https://www.ihe-europe.net/IHE_SHARAZONE)
    - It's nice that INCF is trying, but it's just too much altogether to deal with. I would rather we try our hand at  an existing non-profit or affiliation like Numfocus for all future endeavors. I'd also go ahead and throw out Catalyst Neuro as they've intimated at being able to disperse Neuro funding across borders and projects.
    - proposed alternative: https://numfocus.org/projects-overview

## Meeting Minutes

### BIDS Copenhagen Meeting: May ~~5-7~~

- dates have changed to May 12-14
- Sunday travel, Monday small meeting and hack, tuesday/wednesday hacking. Thursday travel back
- venue: hotel - TBD (likely )
- FP request - to finalize the BIDS connectivity
- Cyril Pernet - he needs to start with his funding needs , this will also hopefully engage more EU.
- "scope" maintainers and to promote more EU engagement
- request for more diversity in invitees (women)
- 2 people form BIDS2OpenMind
- computation models experts in EU
- Oscar, Lyuba Zehl, Guiomar Niso
- SteeringCommittee: YC, CP,

### Cardiac BEP

- YH: gives :+1: Justification: MRI, supplemental to brain, we have already non-brain modalities (events, physio, working on prov etc)
- FP: gives :+1:
- CP: gives :-1: Justification: not about brain
- CM: gives :-1: Concern about not knowing how the BEP would be validated.
- Common concerns: unclear how many experts could support/review
- CP: voices concerns about this being beyond brain
- CM: views this as borderline, will it be supported by our community
- YH: if there is support behind it, which Christine has indicataed that there is
- YH: steering group might take responsibility to assist in identifying potential expert reviewers
- CP: may be it should be "outside" of BIDS as e.g. we have `/stats-modes` and new BIDS apps 2.0. YH: I think it is more appropriate for BEP, being part of BIDS.
- FP: what does the Governance say?  What do the governance docs say about conflicts/COIs between SC and Maintainer assigned to a BEP and the group developing the BEP.
- CR: given that steering committee is reluctant to approve, what are the next steps?
- CR: cardiac group is polling their own community to build the BEP to get as much support from cardiac group as possible.
- FP: this type of proposal that could be used as an edge case in future BEPs.
- CM: How do we move with this?
- CR: she will bring this back to the maintainers and comments on not knowing how to move forward with a missing BIDS committee meeting.
- EA: Remi is trying to formalize BEP process, so the requirement for 3 SC approvals to progress is a new.  BIDS has done non-brain BEPS (e.g. tabular phenotypic data, eye-tracking, physio)
- CP: these examples support brain imaging, the Cardio BEP does not yet support brain imaging
- YH: the BEP should not have to specify how its brain related.
- CM: a more clear reasoning/clarification on how the cardiac BEP relates to brain (besides "brain-heart interconnectome")
- FP: its possible that more evidence of community support from Cardiac could result with a more positive voting results. COI may also need to be addressed.

### BIDS fiscal sponsorship with INCF

- See last meeting notes
- this should be voted on by the committee
    - Christine and Eric mention google season of DOC issues where new tax laws required that the person received elss than half of what they were expectings.  there was significant financial delays in dispercement (4 months).
    - Will steering committee consider cover the remaining half of the compensation/stipend ($2600 USD). their work was developing the BIDS website which is now being used publicly
    - CM: leans to say yes but we dont know what funds BIDS has
    - YH: righT now we dont have much money but the idea is that we could get it (with INCF)
    - FP: what % of the BIDS purse is $2600?
    - We should also establish a governance procedure for this.
    - YH: if they are in the US, we could pay them from his.
    - FP: We need to establish a treasurer.
    - Steering agrees to pay (from YH)
    - CR: maintainers' main concern was payment amount, payment timing, not timely communication about payment & taxation issues where surprises came when individuals received less compensation than what was agreed upon.

## Tasks

### Steering Group:
- [ ] INCF Fiscal Sponsorship [xx - ]
- [ ] Spreadsheet for BIDS meeting invites [Cyril Pernet]
