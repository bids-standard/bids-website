---
hide:
-   toc
---

# BIDS extension proposals

You can contribute to ongoing BIDS Extension Proposals (BEPs).

Below is a table of currently-active BEPs.

Note that all of the extension ideas that are not backwards compatible and thus will have to wait for BIDS 2.0 are listed on the
[Issues page of the bids-2-devel GitHub repository](https://github.com/bids-standard/bids-2-devel/issues).

{{ MACROS___generate_beps_table(file="beps.yml") }}

## Completed BEPs

When an extension reaches maturity it is merged into the main body of the specification.
Below is a table of BEPs that have been merged.

The references of the final publication for those BEPS
can be found in the BIDS [specification](https://bids-specification.readthedocs.io/en/latest/01-introduction.html#datatype-specific-publications).

<!-- MERMAID GANTT CHART STARTS -->
```mermaid
gantt
    title completed BEP timeline
    dateFormat YYYY-MM
    tickInterval 6month
    axisFormat %b-%Y
    section BEP001
            Google doc    :2017-02, 2020-06
            Pull request  :2020-06, 2021-02
    section BEP002
            Google doc    :2016-09, 2018-10
            Pull request  :2018-10, 2023-08
    section BEP003
            Google doc    :2016-02, 2018-12
            Pull request  :2018-12, 2020-06
    section BEP005
            Google doc    :2017-05, 2020-10
            Pull request  :2020-10, 2021-02
    section BEP006
            Google doc    :2017-06, 2018-12
            Pull request  :2018-12, 2019-03
    section BEP007
            Google doc    :2017-07, 2018-04
    section BEP008
            Google doc    :2016-03, 2018-04
    section BEP009
            Google doc    :2016-03, 2020-10
            Pull request  :2020-10, 2021-04
    section BEP010
            Google doc    :2017-04, 2018-12
            Pull request  :2018-12, 2019-03
    section BEP018
            Google doc    :2017-09, 2019-07
            Pull request  :2019-07, 2020-04
    section BEP027
            Google doc    :2019-05, 2023-09
            Pull request  :2023-09, 2023-12
    section BEP029
            Google doc    :2019-11, 2022-01
            Pull request  :2022-01, 2023-03
    section BEP030
            Google doc    :2020-04, 2021-05
            Pull request  :2021-05, 2022-10
    section BEP031
            Google doc    :2020-06, 2021-09
            Pull request  :2021-09, 2022-02
```
<!-- MERMAID GANTT CHART ENDS -->

{{ MACROS___generate_beps_table(file="beps_completed.yml", type="completed") }}

<br>

Some proposals that set out to extend the BIDS specification have instead lead to other outcomes such as:

-   becoming tools for handling BIDS
-   having been merged into other BEPs
-   having been dropped from consideration

See the table below:

{{ MACROS___generate_beps_table(file="beps_other.yml", type="other") }}
