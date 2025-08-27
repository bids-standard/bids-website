---
layout: post
title: What is a BIDS App?
---

A BIDS App is a container image capturing a pipeline that takes a BIDS formatted dataset as input.

Each BIDS App has the same core set of command line arguments,
making them easy to run and integrate into automated platforms.
BIDS Apps are constructed in a way that does not depend
on any software outside of the image other than the container engine.

BIDS Apps rely upon two technologies for container computing:

-   [Docker](https://docker.com) for building, hosting as well as running
    containers on local hardware (running Windows, Mac OS X or Linux) or in the cloud.

-   [Apptainer](https://apptainer.org/) - for running containers on HPCs.

BIDS Apps are deposited in the Docker Hub repository, making them openly accessible.
Each app is versioned and all of the historical versions are available to download.
By reporting the BIDS App name and version in a manuscript,
authors can provide others with the ability to exactly replicate their analysis workflow.

Docker is used for its excellent documentation, maturity, and the Docker Hub service for storage and distribution of the images.
Docker containers are easily run on personal computers and cloud services.
However, the Docker Engine is rarely available in HPCs.
Apptainer is a unique container technology designed from the ground up,
with the encapsulation of binary dependencies and HPC use in mind.
Its main advantage over Docker is that it does not require root access
for container execution and thus is safe to use on multi-tenant systems.
In addition, it does not require recent Linux kernel functionalities
(such as namespaces, cgroups and capabilities),
making it easy to install on legacy systems.
