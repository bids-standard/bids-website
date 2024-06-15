# Outputs

## File formats for the application specification and report

BIDS Apps MUST be able to be called via the BIDS Application Boutiques
descriptor and corresponding input parameter dictionary files, commonly referred
to in the Boutiques parlance as "invocations", and accept any BIDS dataset.
It is RECOMMENDED that BIDS Applications produce BIDS-Derivatives-compliant datasets.

### List of relevant output-files object properties for the BIDS Application specification

| Field name                        | Requirement Level | Data type        | Description                                                                                                                                                                                              |
|-----------------------------------|-------------------|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id                                | REQUIRED          | String           | A short, unique, informative identifier containing only alphanumeric characters and underscores.  Typically used to generate variable names.  (should conform ^[0-9,_,a-z,A-Z]*$).  Example: "data_file" |
| name                              | REQUIRED          | String           | A human-readable output name.  Example: 'Supplementary input file for X task'.                                                                                                                           |
| description                       | RECOMMENDED       | String           | A plain-text description of the output-files of the BIDS Application.                                                                                                                                    |
| command-line-flag                 | OPTIONAL          | String           | Flag associated with the argument on the command-line.  Examples: -o, --output                                                                                                                           |
| file-template                     | OPTIONAL          | Array of strings | An array of strings that may contain value keys and together populate the self-contained structure of a configuration file.                                                                              |
| list                              | OPTIONAL          | Boolean          | True if output is a list of values.                                                                                                                                                                      |
| optional                          | OPTIONAL          | Boolean          | True if output may not be produced by the tool.                                                                                                                                                          |
| path-template                     | OPTIONAL          | String           | Describes the output file path relative to the execution directory.  May contain input value keys and wildcards.  Example: "xx".                                                                         |
| path-template-stripped-extensions | OPTIONAL          | List             | List of file extensions that will be stripped from the input values before being substituted in the path template.  Example: [". nii",". nii. gz"].                                                      |
| value-key                         | OPTIONAL          | String           | A string contained in command-line, substituted by the output value and/or flag at runtime.                                                                                                              |

## Execution Report & Updating Dataset Description

When generated, an execution report that completely describes the processing
that was executed and the dataset MUST comply with the BIDS Provenance Extension
Proposal (BEP28). These outputs are OPTIONAL, and if provided, should be
specified in the [`output-files`](./outputs.md) of the tool descriptor.

Similarly, the dataset_description.json file SHOULD be updated to reflect the
processing that has occurred by the BIDS Application.

## Behaviors

For a given set of arguments, the behavior of a BIDS Application will typically
vary based on the contents of the input dataset. The dataset may be
BIDS-compliant, or it may not; and it may contain the file types the BIDS App
requires, or it may not. This section describes the expected behavior under each
combination of cases, and describes RECOMMENDED exit codes on systems that
support them.

### Valid BIDS datasets

If the dataset is BIDS-compliant and contains the files required by the application,
then the application should make a best effort to perform its task to completion.

If the dataset is BIDS-compliant but does not contain the files required by the application,
then the application MAY fail immediately or when attempting to open a missing file.
In this case, it is RECOMMENDED to use exit code `66` (NOINPUT).

### Invalid BIDS datasets

If the dataset is not BIDS-compliant, then the BIDS App MAY fail immediately with exit code `16`.

If the dataset contains the required files but is not BIDS-compliant
(for example a "dirty" dataset that has more files than needed),
then the BIDS App MAY treat the dataset as valid.

### Exit codes

An exit code or [exit status](https://en.wikipedia.org/wiki/Exit_status) is an
integer indicating the reason for termination for use by the parent program or
operating system. The interpretation of exit codes varies across systems, and
programmers SHOULD follow the conventions of the systems for which they are
programming.

Most operating systems, including POSIX (Linux, Mac OSX) and Windows use 0 to
indicate success and >0 to indicate failure. POSIX systems are limited to an
unsigned byte (range: 0-255), so these recommendations are limited to that
range. Exit codes 64-78 are specified in BSD
[sysexits(3)](https://www.freebsd.org/cgi/man.cgi?query=sysexits&sektion=3), and
should be avoided unless applicable. Exit codes 2 and 126-165 may be set by
[Bash](https://www.tldp.org/LDP/abs/html/exitcodes.html), and so will be
reserved.

The following exit codes are RECOMMENDED for consistent error handling
under POSIX and Windows environments:

#### Reserved exit codes and their definitions

| Exit code | Definition                                                                                  |
|-----------|---------------------------------------------------------------------------------------------|
| 0         | SUCCESS. The program completed successfully.                                                |
| 1         | FAILURE. The program failed for unspecified reasons.                                        |
| 2         | Reserved                                                                                    |
| 16-31     | BIDS-related codes. Reserved except the following                                           |
| 16        | An input dataset failed BIDS validation.                                                    |
| 17        | Unknown analysis level.                                                                     |
| 18        | Entity-based filtering options selected no files.                                           |
| 19        | Both command-line arguments and a parameter invocation file were passed to the application. |
| 64-78     | BSD codes - Reserved except the following.                                                  |
| 64        | USAGE. The command was used incorrectly.                                                    |
| 65        | DATAERR. The input data was incorrect in some way.                                          |
| 66        | NOINPUT. The input data was missing or unreadable.                                          |
| 73        | CANTCREAT. An output file/directory cannot be created.                                      |
| 74        | IOERR. Failure during file reading/writing.                                                 |
| 75        | TEMPFAIL. Temporary failure. Another run is expected to succeed.                            |
| 126-165   | BASH codes - Reserved                                                                       |
