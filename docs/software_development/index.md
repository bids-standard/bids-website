# Developer guidelines

These guidelines are for developers of software that consumes or produces BIDS datasets: converters, validators, curation tools, viewers, libraries, and BIDS Apps.
They complement — but are not part of — the [BIDS specification][specification].
They are largely agnostic of any specific BIDS version and reflect common BIDS principles rather than the rules of a single release.

The BIDS specification is intentionally silent on filesystem-specific implementations (symbolic links, case-sensitivity of the underlying filesystem, storage backend, and similar).
BIDS-aware software, however, has to run against real datasets that live on real filesystems and are frequently managed by tools such as [git-annex] and [DataLad], mounted from cloud object stores, or bind-mounted into containers.
The recommendations below aim to keep tools interoperable across those realities.

The keywords "MUST", "MUST NOT", "SHOULD", "SHOULD NOT", and "MAY" are used as defined in [RFC 2119](https://www.ietf.org/rfc/rfc2119.txt) to grade the urgency of each guideline.

## Do not resolve symbolic links

Software MUST access files via the path at which they appear in the dataset, and MUST NOT canonicalize that path (via `realpath`, `readlink -f`, `pathlib.Path.resolve()`, `find -L`, or equivalent) before performing any path-based lookup such as sidecar discovery, entity parsing, or inheritance resolution.
Software SHOULD open a file for I/O by its as-written path and let the OS follow the link transparently; it MUST NOT read or act on the link target as if it were the file's location in the dataset.

Two independent reasons make this rule load-bearing.
The [Inheritance Principle][inheritance] requires walking *up the dataset directory tree* from a data file to collect applicable metadata; following a symlink can redirect that walk out of the BIDS hierarchy entirely, so sidecars that should apply are silently missed.
Separately, [git-annex] (and therefore [DataLad]) stores content in an object store under `.git/annex/objects/…` and exposes it via symlinks placed at dataset paths — resolving those symlinks moves the process into the object store, where none of BIDS' entity/sidecar/inheritance relationships hold.
This is the most common way in which a "reasonable-looking" canonicalization silently breaks correctness on published, DataLad-managed datasets.

Concretely: treat the input path as an opaque, lexical string, and use lexical parents (for example, `os.path.dirname`, `PurePath.parent`) to walk up the tree.

## Implement the Inheritance Principle correctly

When resolving metadata for a data file, software MUST walk *lexically* up the dataset tree and apply the [Inheritance Principle][inheritance] rules.

-   Software MUST NOT skip directory levels, and MUST NOT resolve symbolic links while identifying parents (see [previous section](#do-not-resolve-symbolic-links)).
-   Where feasible, software SHOULD rely on an [existing library](#prefer-existing-language-bindings) rather than re-implement inheritance from scratch — this is the class of rule most commonly implemented incorrectly.

The specific inheritance rules are part of the BIDS specification and may evolve between BIDS releases (major or minor); software SHOULD revisit its implementation on each new release.

## Treat input datasets as read-only

Software MUST NOT modify files in the input dataset(s), MUST NOT update their mtimes, and SHOULD NOT create files inside them — including editor/OS junk (`.DS_Store`, `Thumbs.db`, `__pycache__`, `.pytest_cache`), lockfiles, or caches.
Outputs belong in a distinct derivatives dataset (see [Emit outputs as valid BIDS derivatives](#emit-outputs-as-valid-bids-derivatives)).

Input datasets are frequently version-controlled (git/git-annex), may be mounted read-only, and may be shared concurrently with other pipelines.
In-place mutation breaks reproducibility, provenance, and multi-user use.

## Drive parsing from the BIDS schema, don't hardcode

Software SHOULD consume the machine-readable [BIDS schema][schema] (or a language binding around it, such as [bidsschematools]) rather than embedding entity tables, suffix lists, or datatype rules in code.

The set of valid entities, their ordering, valid suffixes, datatypes, and sidecar rules evolves with each release of the specification.
Hardcoded tables silently drift as the specification evolves; schema-driven code stays correct across releases.

## Respect case-sensitivity of labels

Software MUST preserve the case of all BIDS labels, entities, and filenames it reads or writes.
Software SHOULD warn — or fail with an actionable message — when it detects two labels or filenames that differ only in case within a dataset.

The BIDS specification mandates [case-collision intolerance](https://bids-specification.readthedocs.io/en/stable/common-principles.html#case-collision-intolerance) for labels and filenames *within a dataset* — this is a naming rule about dataset content, distinct from (and unrelated to) the case-sensitivity of the underlying host filesystem (which the specification is silent on).
A case-insensitive host filesystem (default on macOS APFS/HFS+ and on Windows NTFS) can, however, silently corrupt an otherwise valid dataset by collapsing labels that differ only in case — hence the warning above.

## Handle lazily-materialized content

Software SHOULD distinguish between "path missing" (dataset is malformed) and "file present but content not materialized" (dataset is fine, content needs to be fetched), and SHOULD produce an actionable message in the latter case (for example, suggesting `datalad get <path>`).

Files in a BIDS dataset may point to content that is not currently present on the local filesystem — a [git-annex] symlink whose object has not been fetched, a cloud FUSE mount, or a lazy-download layer.
Crashing with an opaque I/O error on such datasets is the most common failure mode of BIDS software on real-world storage.

## Honor spec-defined exclusions and `.bidsignore`

Software SHOULD NOT descend into `sourcedata/`, `code/`, `logs/`, `stimuli/`, or `derivatives/` directories when discovering *data* for the current pipeline, unless explicitly required or asked to.

`.bidsignore` is a mechanism established and used by the [BIDS Validator][validator] to mark additional files as intentionally out-of-spec; it is not itself part of the BIDS specification.
Software MAY honor `.bidsignore` — but if it does, it SHOULD document that behavior and make the exclusion visible to the user (for example, by logging which files were skipped and why), so that unexpected omissions can be diagnosed.

## Check `dataset_description.json` compatibility

Software SHOULD read `BIDSVersion` from `dataset_description.json` and verify compatibility before running, SHOULD distinguish `raw`, `derivative`, and `study` BIDS datasets via `DatasetType` and adapt behavior accordingly, and SHOULD NOT silently assume a dataset conforms to a specific version.

Failing loudly on version mismatch is preferable to running and producing subtly wrong output.

## Emit outputs as valid BIDS derivatives

Outputs SHOULD be written as a valid BIDS [derivatives dataset](https://bids-specification.readthedocs.io/en/stable/derivatives/introduction.html), with their own `dataset_description.json` populated with `GeneratedBy` (name, version, container image + digest, code URL) and `SourceDatasets`.
Software SHOULD NOT interleave outputs with raw input files unless explicitly requested by the user.

A dedicated derivatives dataset lets downstream tools discover, validate, and chain outputs the same way they do for raw data.

## Follow the BIDS Apps 2.0 execution specification

Command-line software for processing BIDS datasets SHOULD conform to the [BIDS Apps execution specification][execution-spec] (positional `input_dataset`, `output_dataset`, `analysis_level`; standard `--participant-label`, `--session-label`; staged execution).

Consistent CLI interfaces make apps composable with orchestrators, workflow engines, and CI systems.

## Record provenance in outputs

Software SHOULD log the exact inputs, parameters, container digest, and software versions used for each run, in a form that a downstream consumer can inspect, and SHOULD conform to [BEP028 (BIDS-Prov)][bep028] for that provenance record.
Software MUST NOT require the presence of prior provenance records for correctness — users may run tools out of order or on subsetted data.

Provenance is for reporting and reproducibility, not for enforcing a workflow.

## Validate inputs before doing real work

Software SHOULD invoke the [BIDS Validator][validator] (as a library where possible, otherwise as a CLI) at startup, and SHOULD fail early with a clear pointer to what was invalid.
Software SHOULD offer an explicit opt-out flag (for example, `--skip-validation` or `--force`) that lets the user skip validation or proceed despite validation errors, and MUST emit a visible warning when that flag is used.
Software SHOULD NOT silently paper over malformed inputs.

## Cross-platform path handling

Software MUST write dataset-relative paths embedded in metadata (JSON, TSV) in POSIX form (forward slashes), since those paths are dataset-portable identifiers rather than host filesystem paths.
When multiple related datasets (for example, raw and derivatives) are distributed together, they SHOULD be organized as a BIDS study dataset (`DatasetType: study`) so that cross-dataset references stay relative and portable.
For local filesystem I/O, software MAY use the host's native path library.

## Prefer existing language bindings

Rather than re-implementing entity parsing, sidecar discovery, and inheritance from scratch, software SHOULD use one of the maintained BIDS libraries:

-   Python: [PyBIDS], [ancp-bids], [bidsschematools]
-   MATLAB / Octave: [bids-matlab]
-   R: [bidser]
-   JavaScript / TypeScript: [bids-validator][validator]

Bugs in shared libraries get fixed once, for everyone.

## Test against realistic datasets

Software SHOULD include [bids-examples] in its test matrix, and SHOULD additionally test expected behavior against a [DataLad]-managed variant of at least one example (files present as annex symlinks, some content dropped).

The DataLad variant catches the classes of bug that the symbolic-link and lazy-materialization rules above are meant to prevent.

[specification]: https://bids-specification.readthedocs.io
[inheritance]: https://bids-specification.readthedocs.io/en/stable/common-principles.html#the-inheritance-principle
[schema]: ../standards/schema/index.md
[execution-spec]: https://bids-standard.github.io/execution-spec/
[validator]: ../tools/validator.md
[bep028]: https://bids.neuroimaging.io/bep028.html
[git-annex]: https://git-annex.branchable.com/
[datalad]: https://www.datalad.org/
[pybids]: https://github.com/bids-standard/pybids
[ancp-bids]: https://github.com/ANCPLabOldenburg/ancp-bids
[bidsschematools]: https://pypi.org/project/bidsschematools/
[bids-matlab]: https://github.com/bids-standard/bids-matlab
[bidser]: https://github.com/bbuchsbaum/bidser
[bids-examples]: https://github.com/bids-standard/bids-examples
