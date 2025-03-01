---
date: 2024-12-12
slug: "Steering Group minutes"
author: anonymous
categories:
-   steering group minutes
---

<!-- more -->

## Participants

-   Yaroslav Halchenko
-   Dora Hermes
-   Kim Ray
-   Ross Blair
-   Camille Maumet

## NSF POSE proposal1

-   scraped:

    -   POSE is more about not as well established projects --
        in Yarik's opinion would have been too hard to sell for phase I.
        For phase II (with I) as well unclear if would fit ok

-   more feasible replacement (June 04, 2025):
    [NIH](https://grants.nih.gov/grants/guide/rfa-files/RFA-OD-24-010.html).
    "Building Sustainable Software Tools for Open Science (R03 Clinical Trial Not Allowed)"
    Candidate development target/topic/theme:
    ["Tooling/support for BIDS Plugins"](https://github.com/bids-standard/bids-2-devel/issues/74 )

-   what should this proposal cover?

    -   extensions but not in the sense of BEP

    -   establishing common principle standards and wrapping this around tools

    -   pyBIDS?

    -   CM: suggest to not call this a BIDS extension, its too confusing with BEPs (possible rename to 'plugins').
        Happy to be in the loop.
        Also suggest to reach out to maintainers.

    -   KR: Link with Bridge, identifying gaps into the standard. May be able to propose things in the coming months.

## BEP 28 : provenance

-   BEP is being revived/revisioned

-   CM & YH will meet to discuss comments.

    -   [discussion](https://github.com/bids-standard/BEP028_BIDSprov/issues/125) halted about a year ago

    -   [spec](https://bids.neuroimaging.io/bep028)

    -   a few ongoing issues:
        -   [issues/148](https://github.com/bids-standard/BEP028_BIDSprov/issues/148)
        -   [issues/151](https://github.com/bids-standard/BEP028_BIDSprov/issues/151)
        -   and [more](https://github.com/bids-standard/BEP028_BIDSprov/issues)

-   DH: there are more researchers using prepocessed or aggregated (e.g. average, derivatives) data,
    thus BIDS-Prov will have high value.
    This is likely due to a growth of users accessing shared data (secondary data analysis)

-   Can BIDS-prov support multiple analysis pipelines of the same dataset?
    -   comparing workflows is an open problem, BIDS-prov might be a first step in BIDS being able to do this.
    -   W3C Prov comes in many ways and has many uses, something for the BEP authors to discuss (tooling language vs human language).
    -   CM: there needs to be some flexibility to adapt to differences in user needs
    -   YH: table discussion for 2025 :+1:
    -   YH: [relevant publication](https://link.springer.com/article/10.1007/s41019-020-00118-0)

## Maintainers Updates

-   Location of maintainers meeting:  suggests for it to be in EU so that its not only in the USA

-   Meeting Agenda:  What should be addressed?  (BEPs, other?)

-   Meeting Length: 2 days was too short, **3 days** may be better

-   CM: is all the BIDS funding in USA?

-   YH: majority is in US, Cyril might have some.

-   Suggested location/venue:  France, INRIA maybe (Camille can support, venue would be gratis), Copenhagen is another option.

-   RB: if EU does not work out, we can still fall back on Seattle or other US location.

-   Workshop Focus:

    -   YH: BEPS, BIDS2.0, maybe a grant proposal (Ross please share the grnt call with other maintainers)

## BIDS email

`bids.steering@gmail.com` is the new email for BIDS steering group.
