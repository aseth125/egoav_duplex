# Cross-modal proactive reminders

This directory contains the evidence artifacts behind
[`../cross_modal_proactive_reminder_design.html`](../cross_modal_proactive_reminder_design.html).

- `metadata-census.json` separates the current 20 episodes, the 1,577
  downloaded short clips, and the full metadata corpus. Counts are mining
  supply rather than accepted yield.
- `pilot-audit.json` records candidate-level visual evidence, exact media
  clocks, proposed arm/cue windows, audio collisions, decisions, and remaining
  release gates.
- [`pilot/`](pilot/) is the review page for the first phone pilot. It links to
  six evaluation inputs, two oracle previews, and the machine-readable render
  and validation artifacts.

Current result: the 30-second phone scene has eight rendered review variants.
Deterministic render-integrity and speech checks pass; human cue-class and
acoustic-plausibility listening, an independent visual review, and the missing
counterfactual conditions remain open. No item is Gold.
