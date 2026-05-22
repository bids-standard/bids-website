# BIDS extensions

## General

### Can we introduce new entities / metadata in a BEP?

> We need to introduce an entity to distinguish on-device preprocessing methods
> that lead to the raw data, and found entities `proc` and `rec` in the current specification.
> Can we extend one or the other,
> or should we instead create a new entity with analogous description?

The rule of thumb is:
try to reuse as much as possible existing entities or medata.
If you feel that those are too restrictive,
it may be possible to first extend the definitions of those
to better cover your use case.
If that is still not possible then you can introduce new entity or metadata.

See
[bids-specification issue #1177](https://github.com/bids-standard/bids-specification/issues/1177)
for an example of the reasoning that led to the application of an entity
previously used for functional data to anatomical MRI.

### How to turn on email notifications about suggestions and comments for Google Docs

![notifications_1](../assets/img/notifications_1.png)

![notifications_2](../assets/img/notifications_2.png)

![notifications_3](../assets/img/notifications_3.png)

## Provenance

### What is provenance?

Provenance is information about how the dataset was processed.

### What BIDS-Prov (BEP28) is about and which metadata can/should go in my BIDS-derivative BEP?

The important question to ask for each metadata is whether this metadata is important to enable reusability
(for consistent interpretation that is relevant for further processing).
If so, this metadata must go into the BIDS-derivatives.

### Should I worry that those are already covered by the BIDS-Prov BEP?

No.
This information is complementary.

### How do I know if the metadata I want to store should be put in the BIDS-derivatives BEP or in a JSON-LD file?

It will never go in JSON-LD.
BIDS-derivatives and BIDS-Prov are superpositions, they are non-overlapping.
You don't have to include BIDS-Prov.

### If I don’t use BIDS-Prov how can I describe the data workflow?

A lightweight version is to use a description.tsv file
(see common [derivatives](https://bids-specification.readthedocs.io/en/stable/05-derivatives/02-common-data-types.html))
