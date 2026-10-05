---
name: local-audio-transcription
description: "Transcribe authorized local audio with measured inputs, incremental timestamps, honest diarization boundaries, and artifact verification."
version: 1.0.0
author: Hermes Skill Library contributors
license: MIT
metadata:
  hermes:
    category: productivity
    tags: [audio, transcription, asr, diarization, local-processing]
---

# Local Audio Transcription

Produce timestamped evidence from authorized recordings. Treat transcription, speaker diarization, correction, and meeting-minute creation as separate stages with separate completion claims.

## When to use

- A local recording needs a timestamped draft transcript.
- A long recording must be processed incrementally or in the background.
- The user needs speaker separation and its uncertainty stated accurately.
- An existing transcript needs coverage or artifact verification.

## Procedure

1. **Confirm scope and authorization.** Use only the exact recording and output location approved by the user. Do not scan unrelated folders or upload private audio to a service without approval.
2. **Measure the input.** Check that the decoder can open the file, then record duration, channels, sample rate, and codec before choosing a pipeline. File size alone is not a useful runtime estimate.
3. **Capture constraints.** Establish language, privacy boundary, available CPU/GPU, allowed cost, participant count, and desired output. Do not request credentials in chat or quietly switch from local processing to a paid API.
4. **Choose a reproducible pipeline.** Select the model and inference runtime for the measured input and hardware. Distinguish model version from library version, and record material settings such as language, beam size, and voice-activity filtering.
5. **Set runtime expectations.** For a long job, report measured audio duration and make clear that runtime is an estimate. Model download, silence skipping, thermal throttling, and decoding settings can change throughput.
6. **Persist segments incrementally.** Write each segment with start time, end time, and text; flush periodically so an interruption does not discard the entire run. Keep raw ASR output separate from later human corrections.
7. **Monitor boundedly.** Use one process monitor or completion notification rather than repeated polling loops. Estimate progress from the last persisted segment and observed throughput, labeling the estimate as approximate.
8. **Handle diarization honestly.** A known participant count can constrain clustering but does not identify names. Do not assign names from turn order, semantics, or alternating lines. Label speakers generically until identity is independently confirmed.
9. **Verify the artifact.** Require a successful process exit, parseable output, at least one useful segment, monotonically ordered timestamps, and timestamps within decoder duration. Inspect tail coverage before concluding that an early final speech timestamp means silence or missing audio.
10. **Report stage completion precisely.** Call automatic transcription a draft until corrected. State transcription, diarization, speaker naming, correction, and minutes generation separately; completing one does not imply the others.

## Output guidance

A portable segment representation contains at least:

```json
{"start": 12.4, "end": 16.8, "speaker": "SPEAKER_00", "text": "Example transcript segment."}
```

Prefer a machine-readable segment file alongside a readable transcript. Preserve the raw result when creating a corrected edition so edits remain traceable.

## Pitfalls

- Starting a multi-hour job before measuring duration.
- Treating package installation or model discovery as proof that inference works.
- Assuming the newest model is automatically the best fit for the hardware or language.
- Presenting diarization clusters as verified personal identities.
- Hiding overlapping or uncertain speech with polished guesses.
- Inferring complete coverage from process success alone.
- Creating unsolicited summaries, minutes, or attachments when only transcription was requested.

## Verification checklist

- [ ] Input scope and processing boundary are authorized
- [ ] Decoder duration and media properties are recorded
- [ ] Model, runtime, and material settings are recorded
- [ ] Segments are persisted incrementally with timestamps
- [ ] Process exit and output parsing succeed
- [ ] Timestamps are ordered and within media duration
- [ ] Tail coverage is inspected
- [ ] Diarization and speaker identity are not conflated
- [ ] Draft and corrected outputs are clearly distinguished
