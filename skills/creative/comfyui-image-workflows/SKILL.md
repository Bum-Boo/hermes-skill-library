---
name: comfyui-image-workflows
description: "Use when generating, batching, or troubleshooting images with ComfyUI through local or remote API-format workflows while keeping outputs, models, and secrets verifiable."
version: 1.0.0
author: bumboo / Hermes Skill Library contributors
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [comfyui, image-generation, workflows, stable-diffusion, flux, automation]
    related_skills: []
---

# ComfyUI Image Workflows

## Overview

Use this skill when an agent operates ComfyUI for image generation. It focuses on safe workflow execution: checking server readiness, validating workflow format, injecting parameters, monitoring jobs, saving outputs, and reporting only verified files.

This public skill intentionally avoids user-specific paths, private model names, account IDs, chat destinations, and paid cloud credentials.

## When to Use

Use when:

- the user asks to generate images with ComfyUI, Stable Diffusion, SDXL, Flux, or similar image workflows;
- the task uses a ComfyUI workflow JSON file;
- prompt, seed, size, model, LoRA, or output directory parameters must be injected;
- a batch of image variants is needed;
- a ComfyUI job is stuck, silent, missing outputs, or failing with node/model errors.

## Non-Triggers

Do not use this skill for unrelated image APIs that do not use ComfyUI workflows. Do not use it to expose cloud API keys, browser cookies, private model repositories, or local account paths.

## Hard Gates

- Confirm the ComfyUI server or target API is reachable before queueing work.
- Use API-format workflow JSON; editor-format graphs must be converted/exported first.
- Check required models/custom nodes before long batches when possible.
- Do not start paid cloud jobs, install large models, or modify system services without approval.
- Do not claim an image was generated until the output file exists and is readable.
- Preserve workflow, prompt, seed, and output metadata when the user may need reproducibility.

## Protocol

1. **Read the request**
   - Identify prompt, style, aspect ratio, count, negative constraints, and output expectations.
   - Ask only for missing details that materially change the workflow.

2. **Check runtime readiness**
   - Local default: test `http://127.0.0.1:8188/system_stats` or the configured host.
   - If remote/cloud is used, verify the endpoint without printing secrets.

3. **Validate workflow format**
   - API-format workflows have node objects with `class_type`.
   - Editor-format workflows often have top-level `nodes` and `links` arrays and are not directly executable by `/prompt`.

4. **Inspect controllable inputs**
   - Locate prompt text, negative prompt, seed, dimensions, sampler/steps, checkpoint, LoRA, and output nodes.
   - Keep parameter names explicit in the run record.

5. **Preflight dependencies**
   - Check model and custom node names if the server exposes object/model info.
   - If dependencies are missing, report them before queueing a batch.

6. **Queue the job**
   - Submit the API workflow to `/prompt` or an equivalent runner.
   - Capture the `prompt_id` or job handle.

7. **Monitor progress**
   - Poll history or use WebSocket progress where available.
   - For batches, prefer small chunks so partial results can be verified and recovered.

8. **Collect outputs**
   - Read `/history/<prompt_id>` or the runner result.
   - Download or locate generated files.
   - Verify file existence, non-zero size, and image dimensions when possible.

9. **Report results**
   - Include output paths, count, seed/workflow metadata, and any failed jobs.
   - Distinguish queued, completed, saved, uploaded, and verified states.

## Minimal API Concepts

Typical local endpoints:

```text
GET  /system_stats       # server and hardware status
POST /prompt             # queue API-format workflow
GET  /history/<id>       # job result and output nodes
GET  /view?...           # retrieve generated files
WS   /ws                 # optional live progress
```

## Batch Guidance

- For creative exploration, generate diverse prompt/value variants, not only seed-only duplicates.
- Keep batch size small enough that failures are easy to diagnose.
- Save a manifest with prompt, seed, workflow file, output file, and status.
- If the user is waiting in chat, report after each verified chunk rather than staying silent for a long batch.

## Troubleshooting

### Server unreachable

Check whether ComfyUI is running, whether the host/port is correct, and whether a firewall or container boundary blocks access.

### Workflow rejected

Confirm API format. If the file is editor format, open it in ComfyUI and export/save it as API format.

### Missing nodes or models

Use ComfyUI object/model info or startup logs to identify missing custom nodes, checkpoints, VAEs, ControlNets, or LoRAs. Report exact missing names.

### Prompt completed but no images were saved

Inspect the history output nodes and save-image nodes. Verify whether the workflow produces previews only, writes to a different output folder, or failed after sampling.

### Path confusion on Windows/WSL

When ComfyUI returns a Windows path but the agent runs in WSL, convert paths explicitly before joining or copying. Verify the file at the resolved path before reporting it.

## Output Format

```markdown
## ComfyUI result
- Workflow: <file or description>
- Job ID: <prompt_id or runner id>
- Status: queued / running / completed / failed
- Outputs verified: <count>
- Files:
  - <path> (<size>, <dimensions if checked>)
- Seeds/metadata: <summary>
- Warnings: <missing checks or caveats>
```

## Verification Checklist

- [ ] Runtime endpoint was checked.
- [ ] Workflow was confirmed API-format or converted.
- [ ] Required models/nodes were checked or missing checks were disclosed.
- [ ] Job handle/history was captured.
- [ ] Output files exist and are readable.
- [ ] Secrets, private paths, and account identifiers were not exposed.
