# BIDS Extension Proposals: A Guide

## Why contribute to BIDS?

- You can make something that is good even better without building it from
  scratch.
- You can interact with and get to know other experts in the field.
- A more substantial extension can lead to standalone publications, as evidenced
  by abundant examples:
  - MEG:
    [https://www.nature.com/articles/sdata2018110](https://www.nature.com/articles/sdata2018110)
  - EEG:
    [https://www.nature.com/articles/s41597-019-0104-8](https://www.nature.com/articles/s41597-019-0104-8)
  - iEEG:
    [https://www.nature.com/articles/s41597-019-0105-7](https://www.nature.com/articles/s41597-019-0105-7)
  - Genetics:
    [https://doi.org/10.1093/gigascience/giaa104](https://doi.org/10.1093/gigascience/giaa104)
  - PET:
    [https://doi.org/10.1177/0271678X20905433](https://doi.org/10.1177/0271678X20905433)
  - Microscopy:
    [https://doi.org/10.3389/fnins.2022.871228](https://doi.org/10.3389/fnins.2022.871228)

## Overarching principles in the design of BIDS

- Folder structure must be not only machine-readable but also easy to interpret
  by humans. In other words, readability is as important as the ability to
  programmatically traverse the folder structure.
- When it comes to file names within folders, redundancy trumps concision -- the
  files should be identifiable by their names even if removed from the folder
  structure.

# When and how to start a BIDS Extension Proposal?

- Small contributions (typos, rephrasing of a description, adding a single new
  metadata field) can be just added as a
  [Pull Request on GitHub](https://github.com/bids-standard/bids-specification)
- Larger contributions that are expected to involve longer and more involved
  discussions should be first described in a standalone document: a Google Docs
  BEP (BIDS Extension Proposal). Development on Google Docs is preferred as this
  is a low entry barrier for colleagues who do not use GitHub and/or markdown,
  allowing more people to get involved.
  1. Read the
     [BIDS governance document](https://bids.neuroimaging.io/governance.html).
  2. Familiarize yourself with the BIDS community by browsing current issues,
     discussions, and proposed changes on
     [GitHub](https://github.com/bids-standard/bids-specification/).
  3. Open an initial “issue” on the
     [GitHub](https://github.com/bids-standard/bids-specification/) issue
     tracker to gauge interest in your potential extension, and to collect
     feedback by core community members and
     [BIDS maintainers](https://github.com/bids-standard/bids-specification/blob/master/DECISION-MAKING.md#maintainers-group).
     _This is an important step before proceeding in order to make sure that
     everybody is on the same page._
  4. Communicate with the BIDS maintainers to make your BEP official. This
     entails registering the BEP with a number on the
     [website](https://bids.neuroimaging.io/get_involved.html)_._ Practically,
     to obtain a number for your BEP, follow the previous steps and then open a
     new issue on the
     [website GitHub repository](https://github.com/bids-standard/bids-website/),
     cross-linking to other already existing issues.
  5. Create a solid draft of your extension by discussing among colleagues. The
     [BIDS Extension Proposal template](https://docs.google.com/document/d/1W7--Mf3gCCb1mVfhsoRJCAKFhmf2umG1PFkyZ1jEgMw/edit#)
     provides some boilerplate and formatting conventions.
  6. List on the draft who is/are leading the effort.
  7. Share the draft (remember to
     [share a link that allows anyone to comment](https://support.google.com/docs/answer/2494822?co=GENIE.Platform%3DDesktop&hl=en))
     with the
     [bids-discussion mailing list](https://groups.google.com/forum/#!forum/bids-discussion)
     and ask for comments.
  8. Incorporate the feedback, strive for consensus.
  9. Help to merge the extension into the main specification (this will require
     converting the proposal to Markdown and sending a Pull Request at
     [https://github.com/bids-standard/bids-specification](https://github.com/bids-standard/bids-specification))
  10. If necessary, contribute a pull request to the
      [BIDS Validator](https://github.com/bids-standard/bids-validator)
      incorporating the extension.


![alt_text](images/image1.png "image_tooltip")

# Advice for extending BIDS

## Limit flexibility, consider tool developers

One of the aims of BIDS is to make reusing data easier. This means that when
proposing an extension you need to put yourself in the shoes of someone who will
receive a BIDS dataset and attempt to analyze it. Additionally, consider
developers that will try to write tools that take BIDS datasets as inputs. It’s
worth assessing how much additional code different ways of approaching your
extension will lead to.

The most common situation where the trade-off between flexibility and ease of
tool building comes up, is choosing file formats. For example, allowing multiple
different file formats to be used to represent the same data type is flexible,
but requires developers to provide support for all of them. As an example,
iEEG-BIDS and EEG-BIDS
[surveyed the community](https://bids.berkeley.edu/news/bids-megeegieeg-data-format-survey)
to find out about most common formats and selected only a few formats based on
usage and their openness.

## Get the community involved

Try to reach out to colleagues working with the type of data you are trying to
add support for. The more eyes you will get on your extension the better it will
get.

## Be consistent with the main specification

The main specification follows some general rules. For example, see the
[rules on participant labels](https://bids-specification.readthedocs.io/en/stable/02-common-principles.html#participant-names-and-other-labels).

Try not to deviate from those conventions in your extension.

## Avoid backward incompatible changes

BIDS is already incorporated in many tools - proposing a change that will render
already released BIDS datasets not BIDS compliant will cause a lot of confusion
and will force developers to update their codes. We should strive to avoid such
a situation.

Having said that, one day we will have to break backwards compatibility. If you
have an idea for a backward incompatible change please add it as an issue to the
[BIDS 2.0 GitHub repository](https://github.com/bids-standard/bids-2-devel).

## Use existing and common practices/formats

It’s likely that certain data types are commonly stored in a particular way in
your subfield. If this is the case try adopting this way unless it makes your
extension too inconsistent with the main specification. A good example of such
adoption is the
[bvec/bval file format](https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/01-magnetic-resonance-imaging-data.html#required-gradient-orientation-information)
for storing diffusion metadata.

## Try to link with other existing standards and ontologies

There are many standardization attempts out there. When proposing your extension
consider gathering inspiration and directly linking to other standards. A good
example of this is linking metadata fields to corresponding DICOM tags.

# Common pitfalls

## Relying on merging the extension on a set timeline

We have found that it is very difficult to predict how long a BIDS extension
will take to merge into the standard. One challenge that has occurred in the
past is a doctoral student requiring acceptance of their work as a requirement
for graduation. We do not recommend yoking contributions to the BIDS community
(or any volunteer-led open source community) to strict timelines to avoid the
uncertainty around domain specific community engagement, feedback from the BIDS
maintainers and broader developer community, and responding to those reviews.

## Not considering domain- or field-specific guidelines

In many neuroscience fields there have been past developments and efforts to
implement standards, either formally or informally; where possible BIDS
extension proposals should embrace these rather than trying to come up with
alternative standards. The BIDS extension proposal should therefore inventorize
and review past and existing work that may be relevant to the BEP.

## Not building up a user community to support the BEP

Merging BIDS extension proposals only happens following a community review. It
is therefore helpful to get the stakeholders on board early on (i.e., while
writing the extension proposal) rather than at the review stage. Diversity in
the team contributes to the quality of the extension proposal; we recommend that
the core team has representatives from 3 different labs, preferably also with a
mix of more junior and more senior contributors. You may also consider
requesting explicit support letters from external labs.

# How to turn on email notifications about suggestions and comments for Google Documents

1. Open the document you want to turn on the notifications for

![alt_text](images/image2.png "image_tooltip")

![alt_text](images/image3.png "image_tooltip")

![alt_text](images/image4.png "image_tooltip")
