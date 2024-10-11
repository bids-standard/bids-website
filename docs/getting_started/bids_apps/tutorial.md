# Running a BIDS App

## Running a BIDS App locally

Running a BIDS App on a local system can be performed using Docker,
which is easy to install on all three major operating systems.
After installing and starting docker, download the relevant data,
[ds005.tar](https://drive.google.com/drive/folders/0B2JWN60ZLkgkMGlUY3B4MXZIZW8),
and untar it in a directory.

`ds005` will be our input directory in the following example.
Create an `outputs` directory as well.
To run the first stage of the example BIDS App for participant number 01,
open a console (terminal or cmd) and type:

```bash
docker run -ti --rm \
    -v /Users/srycajal/data/ds005:/bids_dataset:ro \
    -v /Users/srycajal/outputs:/outputs \
    bids/example:0.0.4 \
    /bids_dataset /outputs participant --participant_label 01
```

This command runs docker with some flags and then binds the input directory on our local machine,
for example, `/Users/srycajal/data/ds005`,
to a preset directory inside of the docker container (`/bids_dataset`).

You must use the absolute path to both of these directories.
Similarly, we bind the `outputs` directory on our local machine
for example, `/Users/srycajal/outputs` to the `/outputs` directory inside the container.
This is the path where results should be stored.

Next, the command lists the docker container to download from Docker Hub and run: `bids/example:0.0.4`.
Finally, `--participant_label 01` limits the data that will be used
to just the first subject in the dataset.
If we wanted to run all the participants,
we would simply remove `--participant_label 01`.
Or we could select a couple of participants like this: `--participant_label 01 03`.
If the BIDS App was not run before on this machine,
the docker image will be automatically downloaded from Docker Hub.

## Running a BIDS App on a cluster (HPC)

HPC clusters typically require Apptainer/Singularity rather than Docker.
Apptainer (and later versions of Singularity) contain direct support for [Docker/OCI images](https://apptainer.org/docs/user/latest/docker_and_oci.html).

```bash
apptainer build bids-example-0.0.7.sif docker://bids/example:0.0.7
```

After transferring the .img file to a cluster it can be run like any other executable:

```bash
./bids_example-0.0.7.img /bids_dataset /outputs participant --participant_label 01
```

## Helpful links

To learn more containers:

-   consult this [tutorial](https://neurohackweek.github.io/docker-for-scientists/)
-   watch the [workshop video](https://www.youtube.com/watch?v=wAATYzn8O54)

BIDS apps tutorials:

-   see this intro to [BIDS apps](https://github.com/fliem/bids_apps_intro)
