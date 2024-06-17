# User interface

A uniform user interface is essential to scalable deployment of BIDS
Applications. This section describes the common interface components that may be
relied upon by users or platforms running these applications (callers).
Command-line interfaces map between positional or flag arguments provided
through an interactive shell program (for example Bash) to a program and program
behavior. However, tools written in different languages or following different
conventions may represent and parse these arguments distinctly. For the purposes
of automated execution of diverse tools, a more useful interface is a mapping of
parameter identifiers to their values, abstracting the way they are represented
on the command-line (CLI). Boutiques is a standard developed for this mapping.
[Boutiques](https://github.com/boutiques/boutiques) provides a
[JSON schema](https://github.com/boutiques/boutiques/tree/master/boutiques/schema) and
related tools to describe, validate, execute and share command-line tools, among
other utilities. The Boutiques toolkit, named bosh, will be referred to when
discussing examples throughout this specification.

Instead of requiring specific positional arguments and flags which assign common
names to expected options (for example "subject-label") in the command-line interfaces
themselves, BIDS Applications should provide a Boutiques descriptor — a
standardized JSON file that describes the command line behavior and operation of
a tool — that map the tool-specific common arguments to these common names,
without requiring rewriting of the command-line tools. In the sections below,
the identifiers assigned in the Boutiques descriptor are described in the
"Argument ID" column of relevant tables.

The Boutiques descriptor for a program SHOULD be retrievable by calling the
application with the `--bids-exec-spec` flag and no other arguments.

## Interface descriptor

A human-readable schema for a Boutiques descriptor may be found at
[https://github.com/boutiques/boutiques/blob/0.5.25/schema/README.md](https://github.com/boutiques/boutiques/blob/0.5.25/schema/README.md).
This section attempts to summarize the salient points of that document, but the
Boutiques schema is authoritative and complete. In addition to the Boutiques
fields (see Tables 1–4, 6), BIDS conformant descriptors MUST include a custom
object (see Table 2) containing the BIDSApplicationVersion key and associated
value which indicates the version of the BIDS application specification to which
they conform, together with some additional optional fields. Descriptors SHOULD
be simply named as name.json.

## List of relevant base Boutiques properties and their role within BIDS Applications

| Field name          | Requirement Level | Data type | Description                                                                                                                                                                               |
|---------------------|-------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| command-line        | REQUIRED          | String    | A template string including the command and references to the value-keys of all possible inputs.  The ordering imposed here may be significant, in particular for non-optional arguments. |
| custom              | REQUIRED          | Object    | Object which can contain extensible metadata.  This has a single required element, as described in Table 2.                                                                               |
| inputs              | REQUIRED          | List      | List of objects which contain input parameter definitions.  Described in Table 3.                                                                                                         |
| name                | REQUIRED          | String    | The name of the BIDS Application.                                                                                                                                                         |
| output-files        | REQUIRED          | List      | List of objects which contain output parameter definitions.  Described in Table 6.                                                                                                        |
| schema-version      | REQUIRED          | String    | Boutiques schema version.  Must be "≥0. 5".  This is not to be confused with the BIDS Application schema and associated version.                                                          |
| tool-version        | REQUIRED          | String    | Version of the BIDS Application.                                                                                                                                                          |
| description         | RECOMMENDED       | String    | A plain-text description of the BIDS Application.                                                                                                                                         |
| descriptor-url      | RECOMMENDED       | String    | Link to the descriptor itself.  Likely a GitHub repo alongside the described tool, for example.                                                                                           |
| doi                 | RECOMMENDED       | String    | DOI of the descriptor returned once published via Boutiques.  (Note: This is not the DOI of the tool itself. )                                                                            |
| suggested-resources | RECOMMENDED       | Object    | Contains an execution walltime-estimate in seconds, memory usage in MB, and CPU/GPU usage in number of core threads/devices.                                                              |
| container-image     | OPTIONAL          | Object    | The name and location of a container image, such as those in Docker or Singularity formats, containing the configured application.                                                        |
| error-codes         | OPTIONAL          | List      | List of objects that contain error code information.  The reserved error conditions are described in Table 7.                                                                             |
| groups              | OPTIONAL          | List      | List of objects that contain relational information among input parameters as described in Table 4.  This is not to be confused with any other BIDS-relevant definition of groups.        |

### List of custom object properties and roles within the BIDS Application specification

The `custom` object has the following defined fields for use in the context of BIDS Applications.

| Field name              | Requirement Level | Data type | Description                                                                                                                             |
|-------------------------|-------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------|
| BIDSAppSpecVersion      | REQUIRED          | String    | The version of the BIDS application specification with which the application complies.                                                  |
| OutputDataSpecification | OPTIONAL          | List      | If output data conforms to a standard definition (for example NIDM-1. 1. 0), these data standards may be included as a list of strings. |
| `<unspecified>`         | OPTIONAL          | Any       | Any key referring to arbitrary metadata that may be relevant or of interest to the application and its users.                           |
