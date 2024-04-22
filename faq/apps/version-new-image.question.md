---
title: "When is a new image deposited to Docker Hub?"
---

Even though Docker image is being build on the CI server each time
you push a commit to the repository it is not automatically being pushed to Docker Hub.
Only if you tag a commit, push the tag to GitHub,
and the tests you configured pass a new image will be deposited in Docker Hub.
