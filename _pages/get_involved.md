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
You could help someone else learn the benefits of BIDS, give a talk in your local organisation, or
[build a BIDS App](https://bids-apps.neuroimaging.io/){:target="_blank"}!

The only requirement is that everyone who contributes adheres to our
[BIDS Code of Conduct](https://github.com/bids-standard/bids-specification/blob/master/CODE_OF_CONDUCT.md){:target="_blank"}.

Thank you for your contributions!

## Extending the BIDS specification

The BIDS specification can be extended in a backwards compatible way and will evolve over time.
These are accomplished with BIDS Extension Proposals (BEPs), which are community-driven processes.

Do you want to extend BIDS to a new modality or set of data types?
Please draft a BIDS Extension Proposal (BEP) following the
[BIDS Extension Proposals Guide](https://docs.google.com/document/d/1pWmEEY-1-WuwBPNy5tDAxVJYQ9Een4hZJM06tQZg8X4){:target="_blank"}.

You can also contribute to ongoing BIDS Extension Proposals.
Below is a table of currently-active BEPs.
The "Extension label" column provides a direct link to the documentation.

Please find our
[latest BEP update](https://docs.google.com/presentation/d/1uvxJaGgrk58HBWRqLzJTwHjpJKFLGM7YTiNvGwvjMOA/edit?usp=sharing){:target:"_blank"}
presented in the
[Open Science Room](https://ohbm.sparkle.space/in/opensciencesig){:target:"_blank"}
at
[OHBM](https://www.humanbrainmapping.org/i4a/pages/index.cfm?pageid=4041){:target:"_blank"}.

Note that all of the extension ideas that are not backwards compatible and thus will have to wait for BIDS 2.0 are listed on the
[Issues page of the bids-2-devel GitHub repository](https://github.com/bids-standard/bids-2-devel/issues){:target="_blank"}.

{% include beps_table.html beps=site.data.beps %}

### Completed BEPs

When an extension reaches maturity it is merged into the main body of the specification.
Below is a table of BEPs that have been merged.

The references of the final publication for those BEPS
can be found in the BIDS [specification](https://bids-specification.readthedocs.io/en/latest/01-introduction.html#datatype-specific-publications).

| Extension label                                                 | Title                                      | Moderators/leads                                                     |
| --------------------------------------------------------------- | ------------------------------------------ | -------------------------------------------------------------------- |
| [BEP001](https://bids.neuroimaging.io/bep001){:target:"_blank"} | Quantitative MRI (qMRI)                    | Gilles de Hollander and Kirstie Whitaker                             |
| [BEP003](https://bids.neuroimaging.io/bep003){:target:"_blank"} | Common Derivatives                         | Chris Markiewicz                                                     |
| [BEP005](https://bids.neuroimaging.io/bep005){:target:"_blank"} | Arterial Spin Labeling (ASL)               | Henk-Jan Mutsaerts, Patricia Clement, Jan Petr, and Marco Castellaro |
| [BEP006](https://bids.neuroimaging.io/bep006){:target:"_blank"} | Electroencephalography (EEG)               | Cyril Pernet, Stefan Appelhoff, and Robert Oostenveld                |
| [BEP007](https://bids.neuroimaging.io/bep007){:target:"_blank"} | Hierarchical Event Descriptor (HED) Tags   | Chris Gorgolewski                                                    |
| [BEP008](https://bids.neuroimaging.io/bep008){:target:"_blank"} | Magnetoencephalography (MEG)               | Guiomar Niso                                                         |
| [BEP009](https://bids.neuroimaging.io/bep009){:target:"_blank"} | Positron Emission Tomography (PET)         | Melanie Ganz                                                         |
| [BEP010](https://bids.neuroimaging.io/bep010){:target:"_blank"} | intracranial Electroencephalography (iEEG) | Chris Holdgraf and Dora Hermes                                       |
| [BEP018](https://bids.neuroimaging.io/bep018){:target:"_blank"} | Genetic information                        | Cyril R Pernet, Clara Moreau, and Thomas Nichols                     |
| [BEP030](https://bids.neuroimaging.io/bep030){:target:"_blank"} | Near Infrared Spectroscopy (NIRS)          | Robert Luke and Luca Pollonini                                       |
| [BEP031](https://bids.neuroimaging.io/bep031){:target:"_blank"} | Microscopy                                 | Marie-Hélène Bourget and Julien Cohen-Adad                           |

<br>

Some proposals that set out to extend the BIDS specification have instead become tools for handling BIDS.
See the table below.

| Extension label                                                 | Title        | Moderators/leads                               | Tool name                                                                 |
| --------------------------------------------------------------- | ------------ | ---------------------------------------------- | ------------------------------------------------------------------------- |
| [BEP015](https://bids.neuroimaging.io/bep015){:target:"_blank"} | Mapping file | Eric Earl, Camille Maumet, and Vasudev Raguram | [File mapper](https://github.com/DCAN-Labs/file-mapper){:target:"_blank"} |
