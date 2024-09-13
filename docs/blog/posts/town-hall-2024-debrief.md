---
date: 2024-07-01
slug: "BIDS Town Hall 2024: summary"
author: Rémi Gau
categories:
-   town hall
---

The BIDS community got together at OHBM for an update on what's new and what's coming
in the world of BIDS.
Here is a summary.

<!-- more -->

The slides can be found on our [Open-science Framework project](https://osf.io/5pz7c).

-   2023-2024 Milestones

-   openscience prize <!-- TODO  add link -->

-   maintainers meeting in Seattle <!-- TODO  add link -->

-   publications: Poldrack et al., (2024) <!-- TODO  add link -->

-   INCF google season of docs
    -   we have hired a technical writer
    -   Maintainer mentors.

-   Organizational updates

    -   looking for 1 new steering group member to replace Ariel Rokem's position

    -   New Working Groups:
        -   Online presence (*Eric Earl*)
        -   Governance (*Ariel Rokem*)
        -   BIDS2.0 (*Yaroslav Halchenko*)

-   Technical Updates

    -   New BIDS validator releases based on BIDS schema <!-- TODO  add link -->
    -   BIDS schema group meets every Thursday, new contributors welcome! <!-- TODO  add link -->

-   BEPorama
    -   Current BEPs are listed on BIDS website <!-- TODO  add link -->

    -   New BEPS:
        -   BEP041: Statistical Model (*Taylor Salo*) <!-- TODO  add link -->
        -   BEP042: Electromyography (*Yahya Shirazi*) <!-- TODO  add link -->
        -   BEP043: Term mapping (*Chris M*) <!-- TODO  add link -->

    -   Ongoing BEP review summary

    -   potential BEP: stimuli (to be formally established) <!-- TODO  add link -->

    -   potential BEP: "Peripheral" physiological signals <!-- TODO  add link -->

    -   BIDS Connectivity Project Updates
        -   7 BEPS
        -   **lessons learned**: there is no procedure for addressing and resolving BEP feedback,
            establishing a timeline would help to continue progress
        -   **Suggestions**: clarify roles and responsibilities of BEP leads, define timelines for BEP tasks

-   BIDS 2.0 (*Yaroslav Halchenko*)
    -   Goal: Make BIDS better
    -   Now an official Working group
    -   Will provide a migration script to update BIDS 1.0  to BIDS 2.0
    -   [BIDS 2.0 github](https://github.com/bids-standard/bids-2-devel/issues)
    -   Join the effort!

-   The BIDS Community (*Christine Rogers*)

    -   We need help with some BEPS, please reach out to leads

    -   BIDS Datasets in Open Neuro appear to show reasonable global interest

    -   BIDS diversity <!-- TODO  add link -->
        -   Gender representation 2:1 male/female
        -   BIDS Community Survey Results (n=128)
        -   [New website in development](https://bids-website.readthedocs.io)

    -   outreach goals:
        -   new users
        -   convert users to contributors
        -   Areas of Growth: inclusivity, barriers to adoption...

BIDS contributors Please update affiliations! <!-- TODO  add link -->

## Community input an discussion

> How can I get started to contribute to BEPs?

BEP lead info is listed on the BEP docs. <!-- TODO  add link -->

> Aggregating datasets is a challenge. How can BIDS support this?

BEP35 <!-- TODO  add link -->

[Neurobagel](https://neurobagel.org/) also has some potential solutions.

> BIDS 2.0. What is the timeline for that and what happens with tools that support 1.0?

Hopefully, it wouldn't break things to badly, especially if the core dependencies (meaning something like pybids and similar).

> Clinicians want to share data, but it's overwhelming to get into BIDS, and clinicians don't have time.
> Can that be made more easy ?

<!-- TODO Respond -->

> Lesion masks ergo?

Right now, it needs to go to the derivatives.

> How should we deal with multiple descriptions? Sometimes that's multiplicative.

Combine them with some character such as a `+` (which you can use ;-)) <!-- TODO  Not sure this is true -->,
but multiplied `desc` entities is not happening anytime soon.

> Dylan Nielson: Is there a tool or under development for editing BIDS trees
> (For example, remove a subject or a scan and all of its outcomes)

Looks like the asker is already making it.

> Proposed to establish a BIDS Working Group in China.
> This will be useful in some unique settings and projects that require standardization.
> For example, massive traveling brain projects.
> Language is a big barrier and there are cultural barriers as well.

> We need a roadmap

Yes, we do. But the community-driven nature of the project makes this rather complicated.
For example, a graduate student working on a BEP might graduate and move on and then development might stop.
