# BIDS apps

!!! note

    Make sure to check out the [nipreps website](https://www.nipreps.org/)
    for more information on using and creating BIDS apps.

!!! warning

    If you are developing a BIDS app,
    make sure to check the [BIDS apps specification](https://bids-standard.github.io/execution-spec/).

## For users

### How can I check a version of a container I have available locally?

For many bids-app you should be able to run something like:

```bash
docker run bids/example --version
```

Inside each BIDS App there is a `/version` file with the version number.

This file is automatically populated with tag used to trigger the build on the CI server.

## How can I download a particular version of a BIDS App?

All versions of BIDS Apps are archived on Docker Hub. To access a particular
version you should refer to a specific Docker Hub tag. For example:

```bash
docker pull bids/example:v0.0.5
```

## What do the analysis levels (`participant` and `group`) mean?

Generally, `participant` means individual level analysis (for instance: single subject).
The `group` level analysis can be thought of as the second step,
where the input becomes the output of the `participant` level analysis.

For example, generating statistic maps of each subject's brain could be considered `participant`,
while generating the average of these maps across the dataset could be considered `group`.

## For developers

### Getting started

#### Is there a BIDS App template?

Have a look at the
[example BIDS App repository](https://github.com/bids-apps/example).
A minimalist example of a BIDS App consisting of a Dockerfile
and a simple entry point script (written in this case in Python)
accepting the standard BIDS Apps command line arguments.

#### Which container should I use to start building my app?

The only minimum requirements of a BIDS App's container is its ability to run your pipeline.
So for example, if your App is mostly Python based it should be sufficient
to start with any image that has Python and include your environment dependencies.

### API

#### What should the API of my BIDS App look like?

The obligatory arguments of the API of any BIDS App are:

-   `bids_dir`
-   `output_dir`
-   `analysis_level`

with an API call that would look like this:

```bash
app_name bids_dir output_dir analysis_level
```

#### What do we do if my application does not have any use for the group level analysis?

If your pipeline has no need for group level analysis,
it is fine if it is only valid for the analysis_level argument
(see [fmriprep](https://fmriprep.readthedocs.io/en/latest/usage.html)).

#### Can I add more arguments to the API of my App?

Every BIDS App must use the mandatory arguments mentioned above,
but you are free to add more that are specific to the task your App will perform.

We recommend you follow the guidelines mentioned in the [BIDS apps specification](https://bids-standard.github.io/execution-spec/)
for more information on specifying the API of your App.

### Testing

#### Where can I can get data to test my app?

For both lightweight and full datasets to test your BIDS App, you can choose
from one of these
[example datasets](https://bids-standard.github.io/bids-starter-kit/dataset_examples.html)

#### Is it mandatory to first check the dataset validity using the BIDS-validator?

It is an extremely helpful feature to have validation of the dataset as part of your tool.
However, it's not considered mandatory.
For instance: many Apps will simply fail with an error message if the dataset is not BIDS compliant.

### Version

#### How should I version my BIDS App?

Since most BIDS Apps are just thin wrappers around existing pipelines it would
be most sensible to use the same version as the software they are wrapping.

For example in case of HCP Pipelines this would be `v3.17.0`.

#### How to tag a new release?

```bash
git tag v0.0.1
git push
```

#### I want to release a new version of a BIDS App, but the pipeline version is the same?

This can happen when only the runscript or the Dockerfile changed?
According to semantic versioning we should use the `+` signed followed by the build number.
Unfortunately Docker Hub does not support semantic versioning.
The best option is to use the `-` sign followed by the build number.
For example `v3.17.0-3`.

#### Where should I describe changes between versions?

After tagging a new release it is important to provide a list of changes
on the GitHub Releases page.

It accepts markdown syntax and allows you to explain in detail what has changed.

Here's an [example](https://github.com/bids-apps/example/releases).

### Deploying

#### How do I upload my BIDS App to the BIDS App Github org?

You can release BIDS Apps using your own or your lab's account.
However, if you want to be added to the BIDS docker hub,
please message the [BIDS maintainers](mailto:bids.maintenance+apps@gmail.com)
to have a repo created for you.

If you base your code on <https://github.com/bids-apps/example> deployment
on docker hub will happen automatically via Circle-ci.

If you want your App to show on the [BIDS website](https://bids-standard.org/tools/bids-apps.html),
you will have to update the `data/tools/apps.yml` in the
[BIDS website repository](https://github.com/bids-standard/bids-website/tree/main).

#### When is a new image deposited to Docker Hub?

Even though Docker image is being build on the CI server each time
you push a commit to the repository it is not automatically being pushed to Docker Hub.
Only if you tag a commit, push the tag to GitHub,
and the tests you configured pass a new image will be deposited in Docker Hub.
