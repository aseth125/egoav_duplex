# Verified 20-episode chain corpus

This directory publishes the chain-only deliverable for 20 source episodes. Each episode has two matched variants: a clean baseline and a version with interruptions, cross-questions, question changes, refinements, topic switches, and backchannels. Both variants share the same base turns.

No audio or video was synthesized for this delivery. The timing fields describe the intended conversation schedule. Interruption onset is output-contingent: a device fires at its configured answer-relative boundary after synthesis or runtime alignment confirms that the parent answer has produced enough speech. A fixed wall-clock onset should not be inferred before that step.

`data.json` contains the complete baseline, interruption, and audit records for every episode in validation-report order. The JSONL files are convenient corpus downloads. The validation, freshness, and content-audit reports document the checks applied to the release. `checksums.sha256` verifies the files published in this directory; `canonical-checksums.sha256` preserves the canonical corpus manifest.

Regenerate the bundle with `python3 build_data.py /path/to/chain20_fresh_v1`. The build script deliberately excludes the 18 MB prior-question index because it is validation machinery rather than part of the release corpus.
