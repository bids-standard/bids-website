---

date: 2025-04-17
slug: "Steering Group minutes"
author: anonymous
categories:

-   steering group minutes

---

## Agenda

1.  Guest: Maryanne Martone (SPARC)

1.  Copenhagen maintainer meeting

1.  Follow up on cardiac BEP

1.  BEP045 (Physio)
    > email from BEP045 (Physio), is input needed from steering?

1.  Maintainers Updates \[name= all maintainers]

<!-- more -->

## Agenda

-   Yaroslav Halchenko
-   Dora Hermes
-   Kim Ray
-   Eric Earl (Maintainer rep)
-   Maryanne Martone (SPARC)
-   Tom Gillespie (SPARC)

## Meeting Minutes

### SPARC

-   originally noted and some pointers in <https://github.com/bids-standard/bids-2-devel/issues/62>

-   History
    -   Originated in 2018

    -   Physiology, microscopy, etc.

    -   NWB was not mature then

    -   Found BIDS useful and thorough but not enough for physio, micro, etc data

    -   raw, derived, and primary data

    -   on population, specimen, subject, sample: <https://github.com/SciCrunch/sparc-curation/blob/master/docs/participants.org>

    -   Tom Gillespie instrumental in implementing version 2 of SPARC

    -   Just released SDS 3.0 (`MIS` = minimal information standard)

        -   includes an SDS viewer to allow seeing the over structure of a dataset (graph based)

        -   allows for "flexible hierarchy"?

            -   reorders the hierarchy categories to subject level

        -   Sample, Subject, and manifests

    -   Study > Subjects > Protocols > Subject Groups

    -   SDS allows nesting of datasets to support interoperability, but they cannot have the same IDs/naming schema

    -   conversion/renaming/moving process of data into SDS is often a source of error
        -   solution: validation during upload to SPARC database

    -   allows to adding additional "standards" a particular dataset conforms to (e.g. RE-JOIN/HEAL) and providing additional jsonschemas for specific files.
        -   note (Yarik): somewhat relates to <https://github.com/bids-standard/bids-2-devel/issues/74> ("BIDS Extensions")

-   SPARC was always meant to be multi-modal

-   Tries to be "Flexible" to accommodate different requirements of multiple "actors" in a consortia

-   EX: SDS allowing embedding of BIDS: /.dss (ad-hoc prescription of a dataset standard)

-   Have an extensive list of "modalities/data types", which also have strong accent on genetic data and also "computational models"

    -   then metadata records reflect "Ten simple rules" (TSR), googled into <https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1009917>

-   Questions Yarik planned to ask but didn't

    -   Any specific rules or "mapping" regex or alike for the file names?

    -   Any software/libraries to deal with SDS formatted datasets?

    -   If not NWB -- what file format for electrophys data?

    -   Given current state of NWB, BIDS and various BEPS -- would you consider just going after BIDS?

        -   What aspects of SPARC to bring in?

    -   There is a validator (and also mentioned in <https://github.com/con/validation/issues/1>), but how "detailed" validator is, what aspects does it validate?

-   Yarik: I think we should aim to translate such presentations into specific *actionable* items on how to improve BIDS

-   e.g. here the idea from SDS to provide custom jsonschemas for extra validation of some .json files. that somewhat relates to an issue where I added a comment now: <https://github.com/bids-standard/bids-2-devel/issues/74#issuecomment-2813819345>

### Copenhagen Meeting

maintainers need to get travel information to Cyril ASAP - goal is this week or next.

### Follow up on cardiac BEP

### BEP045 (Physio)

### Maintainers Updates

1.  Getting BEP status updates in the next 2-4 weeks.
1.  Would like to talk about the potential Virtual BIDS Town Hall this year.

## Tasks

\==Importance== (1 - 5) / Name

### Steering Group

-   [ ] BIDS townhall

### Maintainers

-   [ ] Send travel info to Cyril
