
This document conveys the process for submitting a BEP to BIDS.

This process assumes the BEP is ready to be opened as a pull
  request to the
  [`bids-specification` repository](https://github.com/bids-standard/bids-specification)
  under the [`bids-standard` organization](https://github.com/bids-standard).
  Please reach out to
  [the BIDS maintainers](https://github.com/bids-standard/bids-specification/blob/master/DECISION-MAKING.md#maintainers-group)
  to let them know you are reaching this step in the process. They will assist the
  merging of the BEP into the Specification.

## REQUIRED deliverables

1. Extension proposal
2. Extension of the
   [`bids-schema`](https://github.com/bids-standard/bids-specification/tree/master/src/schema) to support
   the BEP
3. Examples (to test the validator is working properly) added to
   [`bids-examples`](https://github.com/bids-standard/bids-examples)

## SUGGESTED deliverables

1. Preprint of the new extension (if applicable - please refer to the BEP paper
   writing suggestion below)
2. Press release for the
   [`bids-website`](https://github.com/bids-standard/bids-website)
   [news section](https://github.com/bids-standard/bids-website/tree/gh-pages/_posts)

## Giving collaborators additional permissions within our `bids-standard` organization

Please ensure there is a [BEP team](https://github.com/orgs/bids-standard/teams)
  already created under the `bids-standard` GitHub organization. If not, please
  contact one of the BIDS maintainers (see list in
  [DECISION_MAKING.md](https://github.com/bids-standard/bids-specification/blob/master/DECISION-MAKING.md)).
  A BIDS maintainer will also help invite your fellow BEP members to the GitHub team
  and to make sure your team has elevated permissions for your BEP.

## Submitting the extension proposal

1. Create a new branch off of the `bids-specification` repository
2. Name the branch following the BEP tag convention: `bep###` (e.g. `bep003`)
3. Label your pull requests with your BEP tag (this will signal to the community
   which are for the specification or associated with a specific BEP)
4. When the branch is ready to be merged, open a pull request against the
   `master` branch to signal the BEP is ready for final reviews. We ask your
   initial pull request to the `master` branch is clean of comments and has one
   commit - adding your extension to the specification. Please let the BIDS
   maintainers know if you need assistance
   [squashing your commits](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-request-merges#squash-and-merge-your-pull-request-commits).

The BEP lead(s) will work with the BIDS maintainers to coordinate the community
  review period. The community review period is scheduled _after_ the pull request
  has been opened.

## Submitting the validator extension (deprecation warning)

0. Determine if this is necessary as approved and merged changes to
   to the [schema](https://github.com/bids-standard/bids-specification/tree/master/src/schema)
   will cancel the need to complete the following steps.
1. Create a new branch off of the `bids-validator` repository
2. Name the branch following the BEP tag convention: `bep###` (e.g. `bep003`)
3. Label your pull requests with your BEP tag. This will clearly differentiate
   your work from those of the master branch. Consider opening the pull
   request early to begin getting feedback. Tag
   [Ross Blair (@rwblair)](https://github.com/rwblair)
   in this PR and make sure to have `[WIP]` in the title of the pull request
   to indicate it is a "work in progress".
4. When the validator is ready to be evaluated, please remove the `[WIP]` from
   the pull request title and tag
   [Ross Blair (@rwblair)](https://github.com/rwblair)

## Submitting the examples

1. Create a new branch off of the `bids-examples` repository
2. Name the branch following the BEP tag convention: `bep###` (e.g. `bep003`)
3. Label your pull requests with your BEP tag. This will clearly differentiate
   your work from those of the master branch
4. When the examples are ready to be merged, open a pull request against
   the master branch and tag
   [Ross Blair (@rwblair)](https://github.com/rwblair)

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
