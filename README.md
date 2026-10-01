# EgoAV-Duplex — review copy

A full-duplex egocentric conversation benchmark. A camera wearer asks a
**connected chain** of questions over one continuous clip, interrupting the
assistant mid-answer the way people actually do.

**47 episodes · 208 minutes · 948 user turns · 809 scored · 620 interruptions**

## How to look at it

```
git clone https://github.com/aseth125/egoav_duplex.git
cd egoav_duplex && open index.html        # or xdg-open / just drag into a browser
```

No server needed — every path is relative. Click any row in an episode to jump
the video there; rows highlight themselves as playback crosses them.

## What you are looking at

Each episode is one chain. Per turn the page shows the question, the reference
answer, **why the turn fires when it does**, whether it is scored, the skill it
probes, and its timing label.

Three things distinguish this from a VQA set stitched into a dialogue:

- **The questions are chained.** A turn may refer back to an earlier *answer*
  (`— and that one, both hands or just the left?`). Answering out of order is
  not the same task.
- **The interruptions are timed against the assistant, not inserted.** A turn
  labelled `barge_in` has its onset inside the previous answer's spoken span,
  and that is checked, not asserted. Onsets are anchored to wall-clock evidence
  in the footage — mostly gaze shifts above the 36.7°/s threshold — so they
  cannot be slid to make the arithmetic work.
- **Most turns are not answerable from a single frame.** A captioner probe over
  240 sampled turns solves 22.8% of the turns labelled beyond-captioner against
  33.3% of the deliberately-easy controls.

## Honest caveats

- **The videos are lossy previews**, 720×720 at 15 fps, CRF 32. The masters are
  1100×1100 at 30 fps and 6.1 GB. Timing and text are identical; image quality
  is not what a model would be evaluated on.
- **The wearer's voice is synthesised** (CSM), one consistent voice per episode.
  The assistant is text only — deliberately, since what the benchmark tests is
  the model's response to the user's speech, not its own.
- **Source footage is Nymeria**, used under its research license. This repo is
  private for that reason. Do not redistribute the clips.

## Layout

```
index.html     episode index
ep/*.html      one page per episode
specs/*.json   the 47 chain specs — the actual artifact
media/*.mp4    transcoded renders
```
