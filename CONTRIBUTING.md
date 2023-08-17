# CONTRIBUTING

Here are some tips in case you want to contribute to this project.

## Requirements

Install jekyll: https://jekyllrb.com/docs/installation/

If you are using a later version of Ruby yoy may encounter this error: when
trying to serve the website locally.

```bash
require: cannot load such file -- webrick (LoadError)
```

To fix this, you can install the `webrick` gem:

```bash
bundle add webrick
```

More info here: https://talk.jekyllrb.com/t/load-error-cannot-load-such-file-webrick/5417/7

# Serve locally

Run `bundle exec jekyll serve` in the root of the project.
