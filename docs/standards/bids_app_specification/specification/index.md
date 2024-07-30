# BIDS execution specification

There are three domains of requirements that BIDS Applications must specify:

1.  User interface components
1.  Required application behaviors
1.  Required application outputs

BIDS contains "required", "recommended" and "optional" fields.
These are indicated throughout the document:

-   **REQUIRED**: essential to be BIDS compliant (meaning MUST as per RFC2199)
-   **RECOMMENDED**: gives a warning if not present (meaning SHOULD as per RFC2199)
-   **OPTIONAL**: no warning if missing (meaning MAY as per RFC2199)

Ultimately, through using Boutiques to define tools and their parameters,
the goal is that each tool can be interacted with as follows:

```bash
$ # Using Boutiques directly, the "exec launch" commands will run the app
$ bosh exec launch bids-app --invocation input_params.json
$ # Eventually, we envision that BIDS Application interface will also support
$ # simple, lightweight overrides to provide some of these common values via
$ # the command line directly.
$ bids-launch bids-app --input-dataset /path/to/bids /path/to/derivatives \
    --output-location /path/to/output \
    --analysis-level subject--subject-label 01 02 \
    --random-seed 0xBID5CAFE
```

In the next sections, the `bids-app` tool, a Boutiques descriptor,
and the `input_params.json`, a set of invocation parameters corresponding to this app,
will be defined.
