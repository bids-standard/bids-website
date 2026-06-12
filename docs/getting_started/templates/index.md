# Templates

This section contains templates of different files you can find in a BIDS dataset,
so you can copy-paste-modify them into your own dataset.

## README.md

A clear, informative README is usually the entry point to your dataset, and makes
the data far more usable. Copy the template below to the root of your dataset and
rename it `README` or `README.md`. A dataset has exactly one README, saved as
UTF-8, with no extension or one of `.md`, `.rst`, or `.txt`. Work through it from
top to bottom, completing the sections that apply to your study and deleting both
the sections that do not and the guidance comments as you go. Write plainly enough
that the file reads well even when the Markdown is not rendered, which in practice
means short lines and no wide tables.

Let the rest of the dataset do most of the work. The README is for what the
structured files cannot hold — the study's purpose and design, how the data were
acquired, what the dataset actually contains, and anything a user must know before
analyzing it — plus the few facts important enough to repeat before preprocessing.
Where a detail already lives in `dataset_description.json`, `participants.tsv`, a
task or modality sidecar, `CHANGES`, or `LICENSE`, summarize it and point there
instead of copying it, so the two cannot drift apart.

Aim for a README that an unfamiliar reader can open and, within a minute, grasp
what was recorded, in whom, why, and whether it suits their needs. If it ever
grows unwieldy, move the overflow into a `/doc` folder listed in `.bidsignore`.

The template below can be copied into your own dataset:

<!-- use snippet to include a file
https://facelessuser.github.io/pymdown-extensions/extensions/snippets/#snippets-notation
-->

```markdown
--8<-- "templates/README.md"
```

## dataset_description.json

<!-- use snippet to include a file
https://facelessuser.github.io/pymdown-extensions/extensions/snippets/#snippets-notation
-->

```json
--8<-- "templates/dataset_description.json"
```
