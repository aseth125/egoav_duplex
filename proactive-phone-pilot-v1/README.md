# Proactive phone reminder pilot v1

Eight 30-second review previews for the cross-modal proactive reminder pilot. Each file is 720×720 H.264 video with 48 kHz stereo AAC audio.

- `deictic_*`: wearer prompt “Remind me when this rings.”
- `named_*`: wearer prompt “My phone—tell me when it rings.”
- `*_target_input`: evaluation input with the synthetic phone ring.
- `*_wrong_input`: matched negative with a two-note chime.
- `*_no_cue_input`: matched negative without a cue.
- `*_target_oracle`: review-only target version with “Your phone is ringing now.”

The reminder is armed by 6.8 s, the phone is placed by 17.33 s, the cue spans 22.4–24.8 s, and the oracle response begins at 23.0 s. Oracle files are not model inputs. Static media validation passed; human cue-classification review is still pending, so this pilot is not labeled Gold.

Use `SHA256SUMS` to verify the files.
