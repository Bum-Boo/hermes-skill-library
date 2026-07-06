---
name: ml-research-and-evaluation-workflows
description: "Use when managing ML research workflows: experiment organization, benchmark/evaluation runs, paper evidence, citations, figures, and reproducible reports."
version: 1.0.0
author: bumboo / Hermes Skill Library contributors
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [research, machine-learning, evaluation, experiments, papers, reproducibility]
    related_skills: [research-intake-and-monitoring]
---

# ML Research and Evaluation Workflows

## Overview

Use this skill for ML research work that spans experiments, evaluation, analysis, and evidence-backed writing. The goal is to keep claims tied to reproducible commands, data snapshots, metrics, citations, and limitations.

## When to Use

Use when:

- organizing experiments, logs, metrics, and artifacts;
- running or interpreting benchmark/evaluation jobs;
- preparing figures, tables, citations, or paper sections;
- checking whether claims are supported by evidence;
- producing a reproducible report or submission package.

## Protocol

1. Inspect current materials: repository, draft, experiment logs, datasets, configs, metrics, and existing claims.
2. Define the research question, baseline, metric, dataset split, and evaluation constraints.
3. Create a workspace for notes, figures, tables, result files, and reproducibility scripts.
4. Run small smoke tests before expensive evaluation jobs.
5. Capture commands, configs, seeds, hardware notes, package versions, stdout/stderr, and output files.
6. Tie every claim to a code path, metric, dataset, citation, result file, or explicit assumption.
7. Record partial runs and limitations honestly.
8. Before publishing or submission, verify formatting, references, artifact links, figure/table consistency, and anonymization requirements.

## Paper and Report Workflow

- Start from an outline and claim list.
- Maintain citation notes explaining why each source matters.
- Keep figures/tables reproducible from saved data whenever possible.
- Separate “observed result,” “interpretation,” and “speculation.”
- Include limitations rather than overstating incomplete experiments.

## Evaluation Checklist

For every benchmark or evaluation run, record:

- model/checkpoint;
- dataset/task and split;
- prompt/template or preprocessing;
- decoding/evaluation settings;
- seed/randomness controls;
- hardware/runtime environment;
- harness/tool version;
- result file path;
- known caveats.

## Verification Checklist

- [ ] Claims map to evidence or citations.
- [ ] Experiments are reproducible from recorded commands and configs.
- [ ] Figures/tables match generated outputs.
- [ ] Partial or failed runs are labeled honestly.
- [ ] Final report includes open TODOs and limitations.
