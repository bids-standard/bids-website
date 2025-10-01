<!--- Until this PR is ready for review, you can include [WIP] in the title, or create a draft PR. -->


<!---
Below is a suggested pull request template. Feel free to add more details you feel are relevant/necessary.

-->

<!--
Please indicate after the # which issue you're closing with this PR, if applicable.
If the PR closes multiple issues, include "Closes" before each one is listed.
You can also link to other issues if necessary, e.g. "See also #1234".

https://help.github.com/articles/closing-issues-using-keywords
-->
- Closes #

<!--
Please give a brief overview of what has changed or been added in the PR.
This can include anything specific the maintainers should be looking for when they review the PR.
-->
Changes proposed in this pull request:
-

## Checklist for contributor

- [ ] PR has an interpretable title with a prefix (e.g. `[BUG]`, `[DOC]`, `[ENH]`, `[MAINT]`)\
Refer to [NumPy Development Guide](https://numpy.org/doc/stable/dev/development_workflow.html#writing-the-commit-message) for a full list
- [ ] PR links to GitHub issue with mention `Closes #XXXX`
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] Any dependent changes have been merged and published in downstream modules

<!-- To be checked off by reviewers -->
## Checklist for reviewers
_This section is for the PR reviewer_

For new features:
- [ ] Tests have been added

For bug fixes:
- [ ] There is at least one test that would fail under the original bug conditions
