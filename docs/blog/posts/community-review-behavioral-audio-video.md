---
date: 2026-07-01
slug: "BIDS community review for BEP047: Audio and Video Behavioral Recordings"
author: Ben Dichter
categories:
-   community review
---

The BIDS community is preparing to merge the BIDS Extension Proposal 47 (BEP047), which adds support for audio, video, and still-image recordings of behaving subjects.

<!-- more -->

Behavioral experiments increasingly rely on cameras and microphones — from freely-moving animal recordings to interviews and speech tasks — yet BIDS has had no standardized way to store these files. BEP047 fills that gap. It lets audio, video, combined audio-video, and image recordings live in the `beh/` directory using the `_audio`, `_video`, `_audiovideo`, and `_image` suffixes, with sidecar JSON metadata describing the recording (device, duration, codecs, frame rate, resolution, and more). Multiple simultaneous cameras or microphones are distinguished with the `recording` entity, and repeated captures with the `run` and `split` entities.

BEP047 builds on a new, shared **media files appendix** that defines common file formats, codecs, and stream metadata. These definitions are intentionally general so they can be reused by other proposals that handle media (such as BEP044 for stimuli), keeping naming and metadata consistent across the standard.

The updated draft is available for review at:

- Behavioral audio/video recordings: [https://bids-specification--2231.org.readthedocs.build/en/2231/modality-specific-files/behavioral-experiments.html](https://bids-specification--2231.org.readthedocs.build/en/2231/modality-specific-files/behavioral-experiments.html)
- Common media files appendix: [https://bids-specification--2231.org.readthedocs.build/en/2231/appendices/media-files.html](https://bids-specification--2231.org.readthedocs.build/en/2231/appendices/media-files.html)

Note that the content of those pages may change as suggestions are accepted during the review process.

An example dataset demonstrating the proposed layout is available at:

[https://github.com/bids-standard/bids-examples/pull/523](https://github.com/bids-standard/bids-examples/pull/523)

Comments and suggestions may be submitted on GitHub at:

[https://github.com/bids-standard/bids-specification/pull/2231](https://github.com/bids-standard/bids-specification/pull/2231)

The community review will close on **[REVIEW CLOSE DATE]** at 23:59 UTC.

If no larger issues occur, all open comments and suggestions will be resolved in the following days and merged into the BEP. Afterwards, the BEP will be merged into the BIDS specification, followed by a 5-business-day long feature freeze and a new BIDS release (containing behavioral audio/video/image recordings, among other changes as documented in the BIDS changelog).

For more details on the release protocol, please see:

[https://github.com/bids-standard/bids-specification/blob/master/Release_Protocol.md](https://github.com/bids-standard/bids-specification/blob/master/Release_Protocol.md)
