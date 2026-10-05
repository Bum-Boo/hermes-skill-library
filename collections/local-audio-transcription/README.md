# Local Audio Transcription

Use this collection to produce and verify timestamped draft transcripts from authorized local recordings while keeping transcription, diarization, correction, and summarization distinct.

## Included skill

- `local-audio-transcription` — measures recordings, runs a bounded and reproducible ASR workflow, persists timestamped segments, and verifies the resulting artifact.

## Install

```bash
./scripts/install-collection.sh local-audio-transcription
```

For one Hermes profile:

```bash
./scripts/install-collection.sh local-audio-transcription ~/.hermes/profiles/<profile>/skills
```

## Safety notes

- Process only authorized recordings and approved output locations.
- Do not switch to cloud or paid processing without approval.
- Treat automatic transcripts as drafts until corrected.
- Do not infer personal identities from diarization clusters or conversation structure.
