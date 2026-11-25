# EgoDuplex rebuttal: numbers still needed

The author responses for Reviewers bkAo (R1), sWEf (R2) and tFn3 (R3) are drafted.
Each item below is a slot in that draft that `MASTER_REBUTTAL_FINAL.md` does not fill.
Write the value on the `ANSWER:` line. Do not estimate: if a value was not measured, write `NOT MEASURED`.

## A. Blocking (asked by all three reviewers)

A1. Overlap rate. Using the output-waveform VAD segments, for each system and pooled:
    - number of interruptions whose onset falls inside model speech / total interruptions
    - number of backchannels whose onset falls inside model speech / total backchannels (is the total 227 per system, or pooled over systems?)
    - how an interruption or backchannel that arrives during silence is scored (excluded, or scored as a normal turn)
    ANSWER:

A2. Figure 6. What exactly does Figure 6 count (chains before the interactive and proactive turns were added?), and why does it differ from 1,400 turns / 200 chains = 7?
    ANSWER:

A3. Metric and subset of the re-scores. Table 3 has MiniCPM-o 40.1 > Gemini 37.4, and the bootstrap has 39.3 > 37.1, but the re-scores have Gemini above MiniCPM-o:
    - overlap-verified: Gemini 39.5 -> 39.5, MiniCPM 37.8 -> 37.5, Venus 25.1 -> 24.1, DuplexOmni 17.0 -> 16.7
    - wider windows: Gemini 39.7 -> 41.0; backchannel upper bound: Gemini 42.1
    Which score is this (CCS, Avg, other) and on which chains (all 200, the 53 shared with humans, other)? Why 39.5 in one place and 39.7 in another?
    ANSWER:

A4. Human gap. The plan has three values: +22.6 CCS [13.8, 30.2], "about 26" (67.0 - 41.0) and 24.9 (67.0 - 42.1). Which one is human minus best model, against which model, on which chains? What does "human 67.0 / 37.7" mean? Was the human study extended from 20 to 53 chains?
    ANSWER:

## B. Reviewer bkAo (R1)

B1. W3: scores of the two runs per system (or their standard deviation). The bootstrap covers chain sampling, not run-to-run variation.
    ANSWER:
B2. W3: counts. Number of backchannels, of each interruption subtype, of each reminder subtype.
    ANSWER:
B3. W3: judge agreement n = 71. Is this in addition to the original 100 responses, or a replacement?
    ANSWER:
B4. W4: frozen-frame and half-duplex controls. The deltas, the systems they cover, and a one-line definition of "half-duplex".
    ANSWER:
B5. W5: Gemini proactive audio. Was it ON or OFF under the server default?
    ANSWER:
B6. W5: MiniCPM-o context limit and cache setting.
    ANSWER:
B7. W1: entity leak. "21 of 75": 75 follow-ups counted over which chains? Were all 21 rewritten, or only the Figure 13 example?
    ANSWER:
B8. Comment: exact definition of "stopped speaking" (VAD threshold, time window).
    ANSWER:
B9. Comment: macro-average over the three top-level capabilities, per system.
    ANSWER:
B10. Comment: mean opinion score and deviation for the three TTS systems.
    ANSWER:
B11. Comment: is Avg in Table 3 computed from unrounded values (37.4 vs 37.5)? Do CCS and TCR exclude backchannels?
    ANSWER:

## C. Reviewer sWEf (R2)

C1. W3: reminder score (PR) per reminder type: vision-requiring, memory-only, elapsed-time, per system.
    ANSWER:
C2. W3: proactive controls. Unit of n = 36 (chains? cues?). One-line definition of each control: no_cue, unarmed, wrong_class, pre_arm, repeat.
    ANSWER:
C3. Comment: number of distinct environments, number of wearers, activity distribution, indoor/outdoor balance in the selected subset.
    ANSWER:
C4. Comment: reason Qwen3.5-Omni Flash Realtime and JoyAI-VL-Interaction are not evaluated.
    ANSWER:
C5. Comment: are the system prompts and judge prompts added to the appendix?
    ANSWER:

## D. Reviewer tFn3 (R3)

D1. W3: video input resolution per system.
    ANSWER:
