---
layout: post
title: What is a BIDS App?
---

A BIDS App is a container image capturing a neuroimaging pipeline that takes a
BIDS formatted dataset as input.
[BIDS (Brain Imaging Data Structure)](https://bids.neuroimaging.io) is an
emerging standard for organizing and describing neuroimaging datasets. Each BIDS
App has the same core set of command line arguments, making them easy to run and
integrate into automated platforms. BIDS Apps are constructed in a way that does
not depend on any software outside of the image other than the container engine.

BIDS Apps rely upon two technologies for container computing:

- [Docker](https://docker.com) for building, hosting as well as running
  containers on local hardware (running Windows, Mac OS X or Linux) or in the
  cloud.

- [Apptainer](https://apptainer.org/) - for running containers on HPCs.

BIDS Apps are deposited in the Docker Hub repository, making them openly
accessible. Each app is versioned and all of the historical versions are
available to download. By reporting the BIDS App name and version in a
manuscript, authors can provide others with the ability to exactly replicate
their analysis workflow.

Docker is used for its excellent documentation, maturity, and the Docker Hub
service for storage and distribution of the images. Docker containers are easily
run on personal computers and cloud services. However, the Docker Engine is
rarely available in HPCs. Apptainer is a unique container technology designed
from the ground up, with the encapsulation of binary dependencies and HPC use in
mind. Its main advantage over Docker is that it does not require root access for
container execution and thus is safe to use on multi-tenant systems. In
addition, it does not require recent Linux kernel functionalities (such as
namespaces, cgroups and capabilities), making it easy to install on legacy
systems.

## To learn more about BIDS apps

- read the [journal article](https://doi.org/10.1371/journal.pcbi.1005209)
- see the
  [poster presented at OHBM 2017](https://doi.org/10.5281/zenodo.6417361)
- read the guidelines mentioned in the
[BIDS extension proposal 027](https://bids.neuroimaging.io/bep027)
  for more advanced about BIDS Apps.

## To learn more about BIDS

If you Have a question, comment, or suggestion?

1. Read some introductory material, most likely the very basic problems have
   already been addressed!

- [BIDS Starter Kit](https://github.com/bids-standard/bids-starter-kit) for
  tutorials, wikis, templates, ...

2. Post your question in one of several channels where BIDS members are active

- the [NeuroStars](https://neurostars.org/tags/bids) discourse forum
- the [BrainHack Mattermost](https://mattermost.brainhack.org), for instant
  messaging (see also this
  [news item](https://bids.neuroimaging.io/2020/06/24/Join-the-BIDS-community-on-the-BrainHack-Mattermost.html))
- the [Google group](https://groups.google.com/forum/#!forum/bids-discussion),
  for broader discussions surrounding BIDS
- the
  [specification repository issue page](https://github.com/bids-standard/bids-specification/issues),
  if you found inconsistencies, typos, or other issues with the BIDS
  specification itself
