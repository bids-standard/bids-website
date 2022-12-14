---
---

# BEP submission process

This document conveys the process for submitting a BEP to BIDS.

Starting place: This process assumes the BEP is ready to be opened as a pull
request to the
[`bids-specification` repository](https://github.com/bids-standard/bids-specification)
under the [`bids-standard` organization](https://github.com/bids-standard).
Please reach out to
[the Maintainers](https://github.com/bids-standard/bids-specification/blob/master/DECISION-MAKING.md#maintainers-group)
to let them know you are reaching this step in the process. They will assist the
merging of the BEP into the Specification.

## Submission deliverables

- Extension proposal
- Extension of the
  [`bids-validator`](https://github.com/bids-standard/bids-validator) to support
  the BEP
- Examples added to
  [`bids-examples`](https://github.com/bids-standard/bids-examples)
  - These examples will be used to test the validator is working properly

## Suggested deliverables

- Preprint of the new extension (if applicable - please refer to the BEP paper
  writing suggestion below)
- Press release for the
  [`bids-website`](https://github.com/bids-standard/bids-website)
  [news section](https://github.com/bids-standard/bids-website/tree/gh-pages/_posts)

## Giving collaborators additional permissions within our `bids-standard` organization

Please ensure there is a [BEP team](https://github.com/orgs/bids-standard/teams)
already created under the `bids-standard` GitHub organization. If not, please
contact one of our Maintainers (see list in
[DECISION_MAKING.md](https://github.com/bids-standard/bids-specification/blob/master/DECISION-MAKING.md)).
A Maintainer will also help invite your fellow BEP members to the GitHub team
and make sure your team has elevated permissions for your BEP.

## Submitting the extension proposal

1. Please create a new branch off of the `bids-specification` repository
2. Please name the branch following the convention: bepxxx (e.g. bep003)
3. Please label your PR’s with your bep tag. This will signal to the community
   which PR’s are for the specification or associated with a specific BEP
4. When the branch is ready to be merged, please open a pull request against the
   `master` branch to signal the BEP is ready for final reviews. We ask your
   initial pull request to the `master` branch is clean of comments and has one
   commit - adding your extension to the specification. Please let our
   Maintainers know if you need assistance
   [squashing your commits](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-request-merges#squash-and-merge-your-pull-request-commits).

The BEP lead will work with the Maintainers Group to coordinate the community
review period. The community review period is scheduled _after_ the pull request
has been opened.

## Submitting the validator extension

1. Please create a new branch off of the `bids-validator` repository
2. Please name the branch following the convention: bepxxx (e.g. bep003)
3. Please label your PR’s with your bep tag. This will clearly differentiate
   your work from those of the master branch. One may consider opening the pull
   request early to begin getting feedback. Please tag Ross Blair (@rwblair) in
   this PR. Please make sure to have a `[WIP]` in the title of the pull request
   to indicate it is a work in progress.
4. When the validator is ready to be evaluated, please remove the `[WIP]` from
   the pull request title and tag Ross Blair (@rwblair)

## Submitting the examples

1. Please create a new branch off of the `bids-examples` repository
2. Please name the branch following the convention: bepxxx (e.g. bep003)
3. Please label your PR’s with your bep tag. This will clearly differentiate
   your work from those of the master branch
4. When the examples are ready to be merged, please open a pull request against
   the master branch and tag Ross Blair (@rwblair)

## BEP paper writing suggestion

This suggestion is intended to help BEP leads work more transparently while
undergoing the BEP paper writing process. These suggestions are not required for
submitting the BEP for incorporation into the BIDS-specification.

- As the BEP paper is being put together, it may be valuable to share drafts
  with the BIDS community via the
  [bids-discussion google group](https://groups.google.com/g/bids-discussion).
  This will help you gather the most feedback from the BIDS community and
  strengthen the paper.
- The BEP paper draft can be shared directly on the BEP submission pull request.
  As the pull request is further looked over by the community, the paper can be
  enhanced during the review period.
