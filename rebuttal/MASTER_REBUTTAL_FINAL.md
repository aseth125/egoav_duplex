# EgoDuplex — rebuttal (paste-ready), Reviewers R1, R2, R3

We thank the reviewers. We ran the requested robustness checks; across adaptive timing, overlap-verified
scoring, wider response windows, run-to-run variance, judge reliability, window sensitivity, and the
diagnostic controls, the model ranking and the human-model gap are unchanged. Ranking throughout:
human >> {Gemini-3.8-live ~ MiniCPM-o-4.5} >> Realtime-Venus >> DuplexOmni / Mini-Omni2, with Gemini
and MiniCPM-o statistically indistinguishable (stated below).

Note on provisional judging: three diagnostic CONTROL deltas (frozen-frame, half-duplex) and the
proactive false-alarm credit were scored with a provisional gemini-3.8-flash judge under the same rubric
as our GPT-6 judge; they are reported as DELTAS ONLY and are not comparable to the GPT-6 CCS table. The
GPT-6 re-run is staged. All other numbers below are judge-free re-scores or use the authoritative judge.

====================================================================
## Reviewer 1

W1 (timing / backchannel / entity leak).
- Events are keyed to the model actual played speech, not estimated reference-answer durations: the scored
  metrics take timing from output-waveform Silero-VAD (the 1 s playout cursor is diagnostic only). As a
  direct check, the VAD-derived device-firing schedule agrees with the scripted schedule at Spearman
  rho = 0.934 (Pearson 0.891; median offset 2.8 s; backchannel 0.861, semantic-interrupt 0.948).
- Credit-while-silent is rare and does not affect conclusions: only 13 of 227 backchannel turns were
  credited while the model was silent (Venus 9, MiniCPM 2, DuplexOmni 2, Gemini 0). Overlap-verified
  scoring leaves the ranking unchanged and the leader (Gemini) untouched (39.5 -> 39.5; MiniCPM 37.8 ->
  37.5; Venus 25.1 -> 24.1; DuplexOmni 17.0 -> 16.7), so the human gap only widens.
- Entity-leak follow-ups: we audited all chains; 21 of 75 non-backchannel devices contain a leaking or
  contradicting follow-up, and all 21 fall in the semantic stratum that our contamination control already
  removes from both arms. The ranking is identical with them in, all-semantic dropped, or only-the-21
  dropped. We corrected the specific figure flagged and neutralised its phrasing.

W2 (truncation). Full generations are logged past the window, so no model is truncated at generation
time. Window-level truncation rate is 1.4 to 1.7 percent on the strong models (Mini-Omni2 8.6). Scoring at
wider windows (next-turn, +2, +4, +8, unbounded) does not change the ranking; Gemini rises from 39.7 to at
most 41.0 at unbounded and stays about 26 points below human. Gemini stream interruptions fall on
non-scored proactive narration, not on scored answers.

W3 (reliability).
- Judge vs human: Cohen kappa 0.884 (strict) / 0.934 (quadratic-weighted), n = 71 across all 6 systems,
  per-model agreement uniform (no per-model bias), replacing the single-model validation.
- Variance: clustered bootstrap (10k, resampling chains). Full-set CCS with 95 percent CI: Qwen-oracle
  55.0 [50.4, 59.6], MiniCPM 39.3 [33.0, 46.0], Gemini 37.1 [31.5, 42.9], Venus 26.5 [20.1, 33.3],
  DuplexOmni 12.9 [8.0, 18.3], Mini-Omni2 8.3 [6.0, 10.7]. Human minus best model = +22.6 CCS
  [13.8, 30.2], p < 0.001. Gemini vs MiniCPM is NOT separable (we now state this). Tick-based beats
  end-to-end omni with non-overlapping CIs.
- Subtype counts and the human same-subset comparison (shared 53 chains: human 67.0 / 37.7 vs all 6
  models on the identical set) are reported.

W4 (controls). Frozen-frame and half-duplex both score below the matched full-history baseline (frozen
larger drop), consistent with dependence on historical visual evidence; provisional (gemini judge, delta
only), GPT-6 re-run staged. Clean-vs-duplex paired comparison is already reported (W2 of R2 below).

W5 (configs). Full per-model table added: 1 fps for the live/duplex arms (DuplexOmni 0.52 fps), 16 kHz in
/ 24 kHz out, per-model resolution and context caps, decoding params, version pins. Gemini proactivity
and automatic-activity-detection were server defaults, which we now disclose as the setting behind the
6.4 PR.

====================================================================
## Reviewer 2

W1 (protocol validation). Overlap is VAD-verified against the model actual speech (firing rho 0.934), and
only 13 of 227 backchannels were credited during silence (correcting them does not move the ranking). On
segmentation: the answer window already spans a backchannel, and an upper-bound re-score that credits
every fired-backchannel answer still preserves the ranking (Gemini ceiling 42.1, 24.9 below human). On
the figure grades: we clarify two named axes - backchannel-BEHAVIOR (floor-holding rate: Gemini 37.5,
MiniCPM 57.8, Venus 70, DuplexOmni 28, Mini-Omni2 100 structural) and backchannel-CONTENT (the stratum
CCS shown in the figures). We relabel the figures as content and never collapse them under one BC number.

W2 (insight beyond components / OmniInteract). Matched same-model with and without interactive turns
(clean vs duplex, identical media and questions): Qwen-oracle +0.5, Gemini -6.2, MiniCPM -0.1, Venus
+0.4, DuplexOmni +2.9, Mini-Omni2 +0.6. The Gemini drop is concentrated on the semantic-interrupt
stratum (parent-answer accuracy 20.0 -> 2.7 percent); the residual cost of mere interruption is at most
3 points for every model. The benchmark therefore isolates stopping-and-switching, which component and
turn-based evaluations do not present, and exposes an interrupt-eagerness axis (Gemini over-stops,
MiniCPM under-stops) invisible to single-skill tests. Table 1 is revised to separate specialized
egocentric-skill coverage inside chains from the mere presence of egocentric tasks.

W3 (proactive). We report the activity-at-cue (vision-requiring) subset separately: about 41 percent of
proactive cues require egocentric visual grounding (current + setup), memory-only about 37 percent,
elapsed-time about 22 percent; the vision bin is discriminative, not vacuous. We add a false-alarm /
premature / repeat axis via rendered controls (no_cue, unarmed, wrong_class, pre_arm, repeat). Provisional
(gemini judge, Venus): false-alarm 0.50, premature 0.75, repeat 0.091; the controls reveal that Venus
proactivity is arm-triggered rather than cue-discriminative (silent when unarmed, but fires regardless of
the true cue once armed, and early). Full two-model numbers to follow; GPT-6 re-run staged.

====================================================================
## Reviewer 3

W1 (validity of an interruption when the model is silent). Same as above: timing is VAD-verified against
the model actual speech, and only 13 of 227 backchannels were credited during silence; correcting them
does not change rankings.

W2 (the 10 s reminder window). A fine 1 s-grid sweep (1 to 60 s) shows 10 s lies on a plateau, not a
knife-edge: credited success is flat at 8/9/10 s and moves only 1.87 points across the whole 5 to 15 s
band, while the steep region is at 2 to 5 s where real reminders land. The ranking is window-robust
(MiniCPM >= Gemini at every deadline from 1 to 60 s).

W3 (inference details). The per-model reproducibility table (video fps, input resolution, audio rates,
streaming mode, context caps, decoding params, SDK and version pins) is added; see R1-W5.

====================================================================
## Follow-ups in progress (disclosed)
- Full two-model (Venus + MiniCPM-o) proactive-control numbers at n=36 (refining the provisional subset).
- Authoritative GPT-6 re-run of the frozen-frame / half-duplex / proactive-control deltas (worklists
  staged; provisional gemini numbers are delta proxies only).
