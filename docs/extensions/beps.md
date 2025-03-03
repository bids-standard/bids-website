# BIDS extension proposals

You can contribute to ongoing BIDS Extension Proposals (BEPs).

## Draft and Proposed BEPs

Below are tables of currently-active BEPs,
and "timelines" figures of their development
to give an idea of how long each BEP has been in the works.

Note that all of the extension ideas that are not backwards compatible and thus will have to wait for BIDS 2.0 are listed on the
[Issues page of the bids-2-devel GitHub repository](https://github.com/bids-standard/bids-2-devel/issues).

### Proposed BEPs

Proposed BEPs are more mature BEPs that usually take the form of a pull request
on the BIDS specification repository.

{{ MACROS___generate_beps_table(file="beps.yml", bep_type="proposed") }}

--8<-- "tmp/proposed_BEPs_timeline.html"

### Draft

Draft BEPs are in-progress document, typically in a Google Doc.
This is dynamic and is grown and maintained at the discretion of a BEP Working Group.

{{ MACROS___generate_beps_table(file="beps.yml", bep_type="draft") }}

--8<-- "tmp/draft_BEPs_timeline.html"

## Merged BEPs

When an extension reaches maturity it is merged into the main body of the specification.
Below is a table of BEPs that have been merged.

The references of the final publication for those BEPS
can be found in the BIDS [specification](https://bids-specification.readthedocs.io/en/latest/01-introduction.html#datatype-specific-publications).

<!-- use snippet to include a file
https://facelessuser.github.io/pymdown-extensions/extensions/snippets/#snippets-notation
-->

{{ MACROS___generate_beps_table(file="beps_completed.yml", bep_type="merged") }}

--8<-- "tmp/merged_BEPs_timeline.html"

## Closed BEPs

Some proposals that set out to extend the BIDS specification have instead lead to other outcomes such as:

-   becoming tools for handling BIDS
-   having been merged into other BEPs
-   having been dropped from consideration

See the table below:

{{ MACROS___generate_beps_table(file="beps_other.yml", bep_type="closed") }}
