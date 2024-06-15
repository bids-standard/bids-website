# Scope

While the BIDS format is great for standardizing datasets, analytical tools
operating on that structure can take a variety of forms, arguments, and
complexities, limiting their ability to be applied interchangeably. The BIDS
Application Specification solves this problem by creating a community-driven
standardized structure for software definitions and their execution.

This specification extends the Brain Imaging Data Structure (BIDS) Specification
to describe how software pipelines and analytic tools should interact with
BIDS-formatted datasets. These tools will be referred to as "BIDS Apps" or "BIDS
Applications", and can accept any valid BIDS dataset prior to producing some
result (including a message of inaction, as may be applicable in some cases).

## Goals

This extension is motivated by a desire to automatically and reproducibly
process neuroscientific data. It seeks to specify file types and metadata for
describing the execution of command-line programs that operate upon BIDS
datasets. Graphical and web-based interfaces are outside the scope of this
extension, though it is expected that this specification will simplify the
integration of BIDS datasets and applications into such platforms.

This is guided by the following requirements and desiderata:

-   A tool's parameters should be easily translatable to the BIDS application input specification.
-   A specification should be maximally descriptive rather than prescriptive.
-   A structured execution specification should be produced as a result of using an application.
-   The specification should be sufficiently descriptive to perfectly reproduce analyses.
-   A structured set of input parameters should be usable in place of command-line arguments.
-   It should be possible to make multiple BIDS datasets available to an application.

## Relation to BIDS

The core principles of the original BIDS-Raw specification are inherited by the
BIDS Application specification. This specification is a successor to BIDS-Apps,
which were described in Gorgolewski, et al. 2017
(doi:[10.1371/journal.pcbi.1005209](https://doi.org/10.1371/journal.pcbi.1005209)),
here referred to as BIDS-Apps 1.0. Backwards compatibility with BIDS-Apps 1.0 is
not an explicit goal, but can be achieved in many cases as is discussed in
the section [on backwards-compatibility](./inputs.md#backwards-compatibility). A summary of changes from
BIDS-Apps 1.0 is included in the [CHANGELOG](./CHANGELOG.md#[0.1.0.dev]).

This specification is seen as complementary to BIDS-Derivatives, which is part
of BIDS as of version 1.4.0, and the most recent stable version may be found at
[https://bids-specification.readthedocs.io/en/stable/05-derivatives/01-introduction.html](https://bids-specification.readthedocs.io/en/stable/05-derivatives/01-introduction.html).
It is not required that every BIDS Application produce a
BIDS-Derivatives-compliant result dataset, but any outputs that may be required
by the BIDS Application specification must be compliant with the
BIDS-Derivatives specification.

Please refer to general BIDS specification document for context and general
guidelines (definitions, units, directory structure, missing values, stimulus
and event information and so on):
[https://bids-specification.readthedocs.io/en/stable/](https://bids-specification.readthedocs.io/en/stable/)

The keywords
"MUST", "MUST NOT", "REQUIRED",
"SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED",
"MAY", and "OPTIONAL" in this document
are to be interpreted as described in [[RFC2119](https://www.ietf.org/rfc/rfc2119.txt).

The terminology that will be used is inherited from BIDS-Raw
and includes the following:

-   **Dataset** — a set of neuroimaging and behavioral data acquired for a purpose
    of a particular study. A dataset consists of data acquired from one or more
    subjects and/or sessions.

-   **Subject** — a person or animal participating in the study.
    Interchangeable with "**Participant**".

-   **Session** — a consistent logical grouping of neuroimaging and other data across subjects.

-   **Run** — an uninterrupted repetition of data acquisition that has the same
    acquisition parameters and task (however events can change from run to run due
    to different subject response or randomized nature of the stimuli).

-   **<index>** - a nonnegative integer, possibly prefixed with arbitrary
    number of 0s for consistent indentation, for example, it is 01 in run-01
    following run-<index> specification.

-   **<label>** - an alphanumeric value, possibly prefixed with arbitrary
    number of 0s for consistent indentation, for example, it is rest in task-rest
    following task-<label> specification.
