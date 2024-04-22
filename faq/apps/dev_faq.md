### What do we do if our application does not have any use for the group level analysis?

If your pipeline has no need for group level analysis, it is fine if it is only
valid for the analysis_level argument (see
[fmriprep](https://fmriprep.readthedocs.io/en/latest/usage.html))

## Is it mandatory to first check the dataset validity using the BIDS-validator?

It is an extremely helpful feature to have validation of the dataset as part of
your tool. However, it's not considered mandatory. For instance: many Apps will
simply fail with an error message if the dataset is not BIDS compliant.

## How do I upload my BIDS App to the BIDS App Github org?

You can release BIDS Apps using your own or your lab's account.
However, if you want to be added to the BIDS docker hub,
please message the [BIDS maintainers](mailto:bids.maintenance+apps@gmail.com)
to have a repo created for you.

If you base your code on <https://github.com/bids-apps/example> deployment on
docker hub will happen automatically via Circle-ci.

If you want your App to show on the BIDS App website
[here](https://bids-apps.neuroimaging.io/apps/)), you will in any case have to
update the `_config.yml` in the
[BIDS App website repository](https://github.com/bids-apps/bids-apps.github.io.git).

## Versioning

### When is a new image deposited to Docker Hub?

Even though Docker image is being build on the CI server each time you push a
commit to the repository it is not automatically being pushed to Docker Hub.
Only if you tag a commit, push the tag to GitHub, and the tests you configured
pass a new image will be deposited in Docker Hub.

### How to tag a new release?

```bash
git tag v0.0.1
git push
```

### How should I version my BIDS App?

Since most BIDS Apps are just thin wrappers around existing pipelines it would
be most sensible to use the same version as the software they are wrapping. For
example in case of HCP Pipelines this would be `v3.17.0`.

### I want to release a new version of a BIDS App, but the pipeline version is the same?

This can happen when only the runscript or the Dockerfile changed?

According to semantic versioning we should use the `+` signed followed by the
build number. Unfortunately Docker Hub does not support semantic versioning. The
best option is to use the `-` sign followed by the build number. For example
`v3.17.0-3`.

### Where should I describe changes between versions?

After tagging a new release it is important to provide a list of changes on the
GitHub Releases page. It accepts markdown syntax and allows you to explain in
detail what has changed. Here's an
[example](https://github.com/bids-apps/example/releases).

### How can I check a version of a container I have available locally?

Inside each BIDS App there is a /version file with the version number. This file
is automatically populated with tag used to trigger the build on the CI server.
