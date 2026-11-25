# EgoDuplex rebuttal: numbers still needed

The author responses for Reviewers bkAo (R1), sWEf (R2) and tFn3 (R3) are drafted.
Each item below is a slot in that draft that `MASTER_REBUTTAL_FINAL.md` does not fill.
Write the value on the `ANSWER:` line. Do not estimate: if a value was not measured, write `NOT MEASURED`.

> Fill provenance: values below are from `/ai4rl/fsx/aseth125/rebuttal_v1/RESULTS_SOFAR.md` and the
> per-arm reports. Judge-dependent control numbers are the **gemini-3.8-flash** provisional judge unless
> noted; a 32-way **Claude** panel independently reproduced the directions (cross-judge).

## A. Blocking (asked by all three reviewers)

A1. Overlap rate. Using the output-waveform VAD segments, for each system and pooled:
    - number of interruptions whose onset falls inside model speech / total interruptions
    - number of backchannels whose onset falls inside model speech / total backchannels (is the total 227 per system, or pooled over systems?)
    - how an interruption or backchannel that arrives during silence is scored (excluded, or scored as a normal turn)
    ANSWER: Backchannels: the total **227 is POOLED** over systems (per-system n = Gemini 40, MiniCPM-o 45, Venus 40, DuplexOmni 50, Mini-Omni2 52, Qwen-oracle 0). Backchannels whose onset falls inside model speech = **214/227 pooled**; the 13 silent-onset ones by system are Venus 9/40, MiniCPM 2/45, DuplexOmni 2/50, Gemini 0/40, Mini-Omni2 0/52. Scoring of an event arriving during silence: in the REPORTED pipeline it is scored as a normal turn (and could receive vacuous credit) — our overlap-verified re-score converts those 13 to no-credit (score 1), which does not change the ranking. INTERRUPTIONS: a per-interruption "onset-inside-speech" fraction was **NOT separately tabulated**; instead the firing-schedule agreement of a VAD-driven vs the scripted schedule is rho=0.934 (n=109 fired devices, 60 chains). A clean interruption-overlap count is NOT MEASURED (re-run W1b logic on interruption devices to get it).

A2. Figure 6. What exactly does Figure 6 count (chains before the interactive and proactive turns were added?), and why does it differ from 1,400 turns / 200 chains = 7?
    ANSWER: NOT DETERMINABLE from the rebuttal data (needs the Figure 6 source/caption, which is not in the artifacts I have). Flag for the author to fill from the figure-generation script.

A3. Metric and subset of the re-scores. Table 3 has MiniCPM-o 40.1 > Gemini 37.4, and the bootstrap has 39.3 > 37.1, but the re-scores have Gemini above MiniCPM-o:
    - overlap-verified: Gemini 39.5 -> 39.5, MiniCPM 37.8 -> 37.5, Venus 25.1 -> 24.1, DuplexOmni 17.0 -> 16.7
    - wider windows: Gemini 39.7 -> 41.0; backchannel upper bound: Gemini 42.1
    Which score is this (CCS, Avg, other) and on which chains (all 200, the 53 shared with humans, other)? Why 39.5 in one place and 39.7 in another?
    ANSWER: All of these are **CCS on the FULL set (all 200 chains)**, not the shared-53. The **39.5** figure is the overall-CCS micro-average over CONTENT+PROACTIVE+DEVICE events reproduced by the overlap-verified harness (it matches the published value to the decimal: Gemini 39.47, MiniCPM 37.75, Venus 25.14, DuplexOmni 16.96, Qwen 55.66, Mini-Omni2 15.05). The **39.7** figure is CCS computed only over the judged content-answer windows in the window-sensitivity harness; the ~0.2 difference is the event set (overall vs content-only), not a different metric. IMPORTANT INCONSISTENCY TO RESOLVE: the overlap/window harnesses put Gemini > MiniCPM, while Table 3 (MiniCPM 40.1 > Gemini 37.4) and the bootstrap (39.3 > 37.1) put MiniCPM > Gemini. The two are within noise — the bootstrap shows Gemini vs MiniCPM is **statistically indistinguishable** (CIs overlap, p=0.51) — so the ordering flips with the exact CCS event set. Recommend standardizing on ONE CCS definition (the Table-3 one) for all re-score tables, and reporting Gemini~MiniCPM as a tie rather than ordering them.

A4. Human gap. The plan has three values: +22.6 CCS [13.8, 30.2], "about 26" (67.0 - 41.0) and 24.9 (67.0 - 42.1). Which one is human minus best model, against which model, on which chains? What does "human 67.0 / 37.7" mean? Was the human study extended from 20 to 53 chains?
    ANSWER: Use ONLY **+22.6 CCS [13.8, 30.2], p<0.001** = human minus the best model (Gemini, 44.3) on the **identical 53 shared chains** (67.0 - 44.3 = 22.7, bootstrap-corrected to 22.6). The "about 26" and "24.9" values are APPLES-TO-ORANGES (human on the shared-53 vs Gemini's full-200 window-CCS 41.0 / BC-upper-bound 42.1) and should NOT be used. "human 67.0 / 37.7" = the human arm scores **CCS 67.0 and strict-CCS 37.7** on the 53 shared chains (human on its own full 71-chain set: 69.0 / 40.8). Human-study extent: the arm covers **71 chains, 53 shared** with the model evaluation; I cannot confirm it was literally "extended from 20" (current data is 53/71) — flag the "20" as possibly outdated.

## B. Reviewer bkAo (R1)

B1. W3: scores of the two runs per system (or their standard deviation). The bootstrap covers chain sampling, not run-to-run variation.
    ANSWER: NOT MEASURED. The head-to-head table was a single greedy run (seed 17); the reported CIs are clustered bootstrap over CHAINS only, not run-to-run. A second seed was not run for the head-to-head arm. (The formal pipeline reports judge self-consistency 0.972, which is judge reproducibility, not model run-to-run variance.)

B2. W3: counts. Number of backchannels, of each interruption subtype, of each reminder subtype.
    ANSWER: Backchannels = 227 scored turns (pooled; per-system 40/45/40/50/52/0). Semantic-interrupt devices = 49 (firing-rho set); proactive reminder cues per model = 164 (Gemini) / 160 (MiniCPM), split into 4 types: ACTIVITY_CURRENT 34, ACTIVITY_SETUP 34/31, ELAPSED_TIME 36, MEMORY_TASK 60/59. Full per-interruption-subtype dataset counts are in docs/BENCHMARK500_STATISTICS_FOR_FIGURE.json (4 semantic subtypes x 200; 8 backchannel phrases x 5) — a complete subtype x count table is PARTIALLY tabulated; pull the remaining per-subtype totals from that file.

B3. W3: judge agreement n = 71. Is this in addition to the original 100 responses, or a replacement?
    ANSWER: It is a NEW, broader validation that supersedes the single-model 100: human-vs-judge agreement on 71 model turns spanning ALL 6 systems (kappa 0.884 strict / 0.934 weighted, uniform per-model). The original 100 were from one model only; n=71 is the all-systems replacement (report both, lead with n=71).

B4. W4: frozen-frame and half-duplex controls. The deltas, the systems they cover, and a one-line definition of "half-duplex".
    ANSWER: Content-correctness accuracy baseline 0.143 -> frozen-frame 0.089 (-0.054), half-duplex 0.125 (-0.018) under the gemini judge; the independent 32-way Claude panel reproduces the direction (base 0.136 -> frozen 0.045 / half 0.068), both agreeing frozen hurts more. System covered: Realtime-Venus-Omni (local), 18 shared duplex chains, content component only (provisional, delta-only; GPT-6 re-run staged). Half-duplex = the SAME model/weights run so it cannot listen while it is speaking (its input audio is suppressed during its own speech), isolating duplex capability from backbone quality.

B5. W5: Gemini proactive audio. Was it ON or OFF under the server default?
    ANSWER: OFF. `proactivity.proactive_audio` was left unset -> server default = False (the model responds to every detected turn and cannot withhold audio); `automatic_activity_detection` was also unset (server default = VAD enabled). This server-default configuration is what underlies the 6.4 PR.

B6. W5: MiniCPM-o context limit and cache setting.
    ANSWER: MiniCPM-o 4.5 was run via the per-second streaming runner with NO fixed audio-context cap (the 30 s whisper pad/trim cap belongs to Mini-Omni2, a distinct baseline, not MiniCPM-o). DuplexOmni uses a 32k-token sliding window. The specific MiniCPM-o cache-management setting was NOT separately logged beyond per-second streaming -> report "per-second streaming, no fixed cap"; exact cache flag NOT MEASURED.

B7. W1: entity leak. "21 of 75": 75 follow-ups counted over which chains? Were all 21 rewritten, or only the Figure 13 example?
    ANSWER: 75 = non-backchannel runtime devices over the 70 duplex chains of the audited suite; 21 of these contained a leaking/contradicting follow-up (6 Tier-A contradiction, 15 Tier-B reveal). Neutralized phrasings were written for ALL 21 (the Figure 13 item is the worked example shown). Because all 21 fall in the semantic stratum already removed by the contamination control, scoring is unchanged with them in, all-semantic dropped, or only-the-21 dropped (ranking identical).

B8. Comment: exact definition of "stopped speaking" (VAD threshold, time window).
    ANSWER: A turn "held the floor" (did NOT stop) iff the model was speaking at the event onset AND stop_latency_ms >= 400 ms; it "stopped speaking" iff its output speech ended within 400 ms of the event onset. Speech boundaries are from Silero-VAD (threshold 0.5, min_speech 100 ms, min_silence 250 ms, speech_pad 30 ms, 16 kHz) on the model output waveform.

B9. Comment: macro-average over the three top-level capabilities, per system.
    ANSWER: NOT MEASURED (a per-system macro-average over the three top-level capability groups was not computed; derivable from the per-stratum table if the three groupings are defined).

B10. Comment: mean opinion score and deviation for the three TTS systems.
    ANSWER: NOT MEASURED (no human-listener MOS study was run for the TTS systems).

B11. Comment: is Avg in Table 3 computed from unrounded values (37.4 vs 37.5)? Do CCS and TCR exclude backchannels?
    ANSWER: NOT DETERMINABLE from the rebuttal data (Table 3's internal Avg computation and whether CCS/TCR exclude backchannels require the Table-3 generation script, which I do not have). Flag for the author. (Note: the overlap-verified overall-CCS harness computes CCS over CONTENT+PROACTIVE+DEVICE, i.e. it does include device/backchannel events — if Table 3 differs, that is part of the A3 definition mismatch.)

## C. Reviewer sWEf (R2)

C1. W3: reminder score (PR) per reminder type: vision-requiring, memory-only, elapsed-time, per system.
    ANSWER: PARTIAL. Share of cues needing egocentric vision = ~41% (ACTIVITY_CURRENT+SETUP), memory-only ~37% (MEMORY_TASK), elapsed-time ~22%. Credited (>=2) rates available: MiniCPM-o is highest on the vision-requiring ACTIVITY_CURRENT bin (47.1% credited, 17.6% full); Gemini is near-zero across all four classes. A complete per-type x per-system PR table is only partly computed (strongest signals above); recompute from R2W3_proactive per-class scores for the full grid.

C2. W3: proactive controls. Unit of n = 36 (chains? cues?). One-line definition of each control: no_cue, unarmed, wrong_class, pre_arm, repeat.
    ANSWER: n = 36 CUE-EVENTS (each rendered under all 6 conditions = 216 clips/model). Definitions: target = positive control (real cue after arming -> should fire); no_cue = the triggering sound removed (should stay silent); unarmed = the arming instruction removed (model never told to remind -> should stay silent); wrong_class = the cue sound swapped for a different sound class (should not fire the armed reminder); pre_arm = the cue occurs before the arming instruction (should not fire); repeat = the cue duplicated (should fire once, not repeat). Full-n36 gemini-judge results: false-alarm Venus 0.62 / MiniCPM 0.61; premature(pre_arm) Venus 0.861 / MiniCPM 0.667; repeat Venus 0.129 / MiniCPM 0.429; target-fire Venus 0.639 / MiniCPM 0.861; unarmed 0.083 / 0.167. Both arm-triggered not cue-discriminative.

C3. Comment: number of distinct environments, number of wearers, activity distribution, indoor/outdoor balance in the selected subset.
    ANSWER: NOT MEASURED in the rebuttal artifacts (dataset-provenance stats; pull from the source dataset docs / selection manifest).

C4. Comment: reason Qwen3.5-Omni Flash Realtime and JoyAI-VL-Interaction are not evaluated.
    ANSWER: NOT DETERMINED from the artifacts (author to state; typical reasons: no accessible streaming/duplex endpoint at eval time). Flag.

C5. Comment: are the system prompts and judge prompts added to the appendix?
    ANSWER: The judge rubric is available (metrics_v1 judge_prompts variant_1/2/3) and per-run system prompts are in the run configs; they are NOT yet in the appendix. Action item: append the 3 judge variants + the per-task system prompts (not a measured number).

## D. Reviewer tFn3 (R3)

D1. W3: video input resolution per system.
    ANSWER: Gemini-3.8-live = JPEG re-encoded to width 768 (aspect preserved); MiniCPM-o 4.5 and Realtime-Venus (fork) <= 448x448; Qwen3-Omni = 288x288 (min 32x32); DuplexOmni ~256x256 (65,536-pixel budget); Mini-Omni2 = fixed CLIP ViT-B/32 (224x224), one embedding per oracle turn. Frame rate: 1 fps for the live/duplex arms, except DuplexOmni at 0.52 fps (1 frame / 1.92 s). Audio: 16 kHz PCM16 mono in, 24 kHz out for all.
