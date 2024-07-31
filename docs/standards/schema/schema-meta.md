# Meta

## Context

[`meta.context`](https://github.com/bids-standard/bids-specification/blob/master/src/schema/meta/context.yaml) describes a context object that makes information available to rules

???+ "meta.context"

    ```yaml
    context:
    schema:		The BIDS specification schema
    dataset:		Properties and contents of the entire dataset
    subject:		Properties and contents of the current subject

    path:		Path of the current file
    entities:		Entities parsed from the current filename
    datatype:		Datatype of current file, for example, anat
    suffix:		Suffix of current file
    extension:	Extension of current file
    modality:		Modality of current file, for example, MRI

    sidecar:		Sidecar metadata constructed via the inheritance principle
    …
    associations:	Associated files, indexed by suffix, selected according to the inheritance principle
        events:
        aslcontext:
        bval:
        bvec:
        …
    columns:		TSV columns, indexed by column header, values are arrays with column contents
    json:		Contents of the current JSON file
    gzip:		Parsed contents of gzip header
    nifti_header:	Parsed contents of NIfTI header
    ```
