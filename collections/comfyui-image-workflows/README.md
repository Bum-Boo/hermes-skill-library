# ComfyUI image workflows

ComfyUI image generation, batch execution, output verification, and troubleshooting patterns.

## Skills in this collection

- `comfyui-image-workflows`

## Install only this collection

From the repository root:

```bash
./scripts/install-collection.sh comfyui-image-workflows
hermes skills list
```

For a single Hermes profile:

```bash
./scripts/install-collection.sh comfyui-image-workflows ~/.hermes/profiles/<profile>/skills
hermes --profile <profile> skills list
```

## Usage examples

```text
Use comfyui-image-workflows to run this API-format workflow and verify saved image outputs.
```

```text
Use comfyui-image-workflows to diagnose why this ComfyUI prompt completed without saved images.
```

## Agent guidance

Load the matching `SKILL.md` before acting. Keep side effects bounded, verify outputs with current evidence, and never expose credentials or private local paths.
