---
title: "I want to release a new version of a BIDS App, but the pipeline version is the same?"
---

This can happen when only the runscript or the Dockerfile changed?
According to semantic versioning we should use the `+` signed followed by the build number.
Unfortunately Docker Hub does not support semantic versioning.
The best option is to use the `-` sign followed by the build number.
For example `v3.17.0-3`.
