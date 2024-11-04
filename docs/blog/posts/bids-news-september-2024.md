---
date: 2024-09-22
slug: "BIDS News September 2024"
author: Eric Earl
categories:
-   news
---

# BIDS News September 2024

The BIDS Maintainers, Steering Group, working groups, and other contributors have been hard at work to bring the community all this news. Read on\!

<!-- more -->

## BIDS Specification version 1.10.0

The BIDS specification has released a new minor version\! The highlights are:

-   Integrating BEP022 for Magnetic Resonance Spectroscopy
-   Publishing the BIDS schema to [JavaScript Registry](https://jsr.io/@bids/schema)
-   For the full list of changes, you can read [the changelog](https://bids-specification.readthedocs.io/en/stable/CHANGES.html#v1100-2024-09-06)

## Schema-based BIDS validator deployed on validator site

A culmination of years of hard work, the schema-based validator makes maintenance of the validator and inclusion of new rules more sustainable (and very reusable).

The “schema” is a machine readable set of definitions and rules for BIDS.
The new validator now makes use of this schema by reading the different rules from it and checking if a dataset complies with them.
With this new BIDS validator, it will be easier to start validating new data types, but also to start validating derivatives, an issue that has blocked some BIDS extensions for years.
You can try it out now on the [BIDS validator website](https://bids-standard.github.io/bids-validator) and it will soon replace the “legacy” validator.

## BIDS website is currently in transition

With the support of INCF, Google Season of Docs, BIDS maintainer mentors, and a technical writer, BIDS has been able to improve its online presence.
Instead of a large collection of websites, we now have one central site and only a few separate specification/standards sites.
You can preview it at [its temporary site](https://bids-website.readthedocs.io/) now.
Expect it to replace the current BIDS website around the end of this year.

You can also provide feedback now with our [BIDS website survey](https://cryptpad.fr/form/#/2/form/view/f3b2wVPL5VK1HhvBNwtW3-4LXeEpJ9xMY+uOaoahyqQ/), open until October 1st, 2024\.

## BIDS election on the horizon

Per BIDS governance, the steering group members have a term of 3 years.
This year, Ariel Rokem's term ends. Keep an eye out for the upcoming election which BIDS contributors can vote upon. And on behalf of the community, thank you so much Ariel for your service\!

You can find more [about BIDS governance](https://bids-website.readthedocs.io/en/latest/collaboration/governance.html) here.

## Recent venues BIDS presented

BIDS continues to be featured in different venues. Our very own maintainer extraordinaire, Rémi Gau, was recently featured in a yet-to-be-released podcast. The BIDS Town Hall was featured at OHBM again this year in June. For a full recount refer to [this blog post](./town-hall-2024-debrief.md).

## BIDS Extension Proposals (BEPs)

The BEPs carry on to help us all update the standard with new and previously unestablished data types and improvements. If there's a BEP here that affects you, consider getting involved by commenting on open Google Docs or GitHub pull requests or contacting the leads listed in the BEP. Here’s some of our newest BEPs.

-   [BEP041](https://bids.neuroimaging.io/bep041): Statistical Model (Taylor Salo)
-   [BEP042](https://bids.neuroimaging.io/bep042): Electromyography (Seyed Yahya Shirazi)
-   [BEP043](https://bids.neuroimaging.io/bep043): Term mapping (Chris Markiewicz & Eric Earl)
-   [BEP044](https://bids.neuroimaging.io/bep044): Stimuli (Seyed Yahya Shirazi)

Other BEPs are listed on [the BIDS website](https://bids-website.readthedocs.io/en/latest/extensions/beps.html).

## New working groups

This year has seen two new BIDS working groups form, the [Online Presence Working Group](https://groups.google.com/g/bids-discussion/c/Wx-9wG4tGUs) and the [Code of Conduct Working Group](https://groups.google.com/g/bids-discussion/c/9SVP9r6Gz3Q).

## That’s all for now

Until next time, stay in BIDS-ness\!
