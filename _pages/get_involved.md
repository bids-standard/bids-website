---
---

# Get involved in making BIDS better

The easiest way to contribute to BIDS is to ask questions you have about the specification on
[Neurostars](https://neurostars.org){:target="_blank"}.
If your question has a
[bids tag](https://neurostars.org/search?q=tags%3Abids){:target="_blank"}
it will be much easier for others to find the answer.

You can also get involved by _answering_ questions on
[Neurostars](https://neurostars.org/search?q=tags%3Abids){:target="_blank"}!

You can contribute to the BIDS specification by opening
[Issues](https://github.com/bids-standard/bids-specification/issues){:target="_blank"}
and proposing changes via
[Pull Requests](https://github.com/bids-standard/bids-specification/pulls){:target="_blank"}
on
[GitHub](https://github.com/bids-standard/bids-specification){:target="_blank"}.

To make improvements to the website that you are reading right now, you can also open an
[Issue](https://github.com/bids-standard/bids-website/issues){:target="_blank"}
and propose changes via Pull Requests at the
[BIDS website GitHub repository](https://github.com/bids-standard/bids-website){:target="_blank"}.

There are so many ways to help us build this community.
You could help someone else learn the benefits of BIDS, give a talk in your local organization, or
[build a BIDS App](https://bids-apps.neuroimaging.io/){:target="_blank"}!

The only requirement is that everyone who contributes adheres to our
[BIDS Code of Conduct](https://github.com/bids-standard/bids-specification/blob/master/CODE_OF_CONDUCT.md){:target="_blank"}.

Thank you for your contributions!

## Extending the BIDS specification

The BIDS specification can be extended in a backwards compatible way and will evolve over time.
These are accomplished with BIDS Extension Proposals (BEPs), which are community-driven processes.

Do you want to learn more about extending BIDS to a new modality or set of data types?
Read the [Guide](https://bids-extensions.readthedocs.io/en/latest/guide/){:target="_blank"}
and follow the [Submission Process](https://bids-extensions.readthedocs.io/en/latest/submission/){:target="_blank"}.

You can also contribute to ongoing BIDS Extension Proposals.
Below is a table of currently-active BEPs.
The "Extension label" column provides a direct link to the documentation.

Please find our
[latest BEP update](https://docs.google.com/presentation/d/1uvxJaGgrk58HBWRqLzJTwHjpJKFLGM7YTiNvGwvjMOA/edit?usp=sharing){:target:"_blank"}
presented in the Open Science Room at
[OHBM](https://www.humanbrainmapping.org/i4a/pages/index.cfm?pageid=4041){:target:"_blank"}.

Note that all of the extension ideas that are not backwards compatible and thus will have to wait for BIDS 2.0 are listed on the
[Issues page of the bids-2-devel GitHub repository](https://github.com/bids-standard/bids-2-devel/issues){:target="_blank"}.

{% include beps_table.html beps=site.data.beps %}

### Completed BEPs

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

{% include beps_completed_table.html beps=site.data.beps_completed %}

<br>

Some proposals that set out to extend the BIDS specification have instead lead to other outcomes such as:

- becoming tools for handling BIDS
- having been merged into other BEPs
- having been dropped from consideration

See the table below:

{% include beps_others_table.html beps=site.data.beps_other %}
