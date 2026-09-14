---
name: academic-manuscript-readiness
description: "Use when preparing an evidence-backed manuscript or pre-empirical abstract without overstating source, method, or empirical readiness."
version: 1.0.0
author: bumboo / Hermes Skill Library contributors
license: MIT
metadata:
  hermes:
    tags: [research, academic-writing, evidence-audit, methods, integrity]
    related_skills: [research-intake-and-monitoring, ml-research-and-evaluation-workflows]
---

# Academic Manuscript Readiness

## Overview

Prepare an auditable submission package by keeping venue fit, source evidence, empirical status, and research integrity separate. This is not generic prose polishing: completion claims must match what was actually verified.

## Core States

Track these independently:

1. **Venue fit** — the question, contribution, and article type match the venue's current official scope.
2. **Evidence readiness** — load-bearing claims match the declared source level.
3. **Empirical readiness** — ethics, pilot, sampling, collection, analysis, and reporting gates are complete.
4. **Integrity readiness** — source traceability, authorship, AI disclosure, and required similarity screening are complete.

A strong pre-data abstract can be suitable for review while still not being submission-ready. Never collapse partial readiness into a single green status.

## Workflow

### 1. Freeze the empirical boundary

Record whether participants or data exist, which results and figures do not yet exist, and which decisions remain with a supervisor, ethics board, or research site. Keep unresolved sections explicitly pending. Never invent samples, statistics, quotations, approvals, or observed-result plots.

### 2. Verify venue fit

Use current official publisher or society sources to record:

- scope and article type;
- topic and contribution fit;
- method and reporting expectations;
- likely desk-rejection mismatches;
- submission guide, word limit, policy, and fee check dates.

Treat inaccessible pages and search snippets as pending confirmation, not full evidence.

### 3. Audit load-bearing claims

Declare an evidence level for every important claim:

- `metadata-only`;
- `metadata+abstract`;
- `full-text`;
- `full-text+location`.

A DOI proves identity, not claim content. For each claim, retain the manuscript location, source identifier, supporting page/section/table/figure, population and task boundary, support type, and paraphrase status. Do not use abstract-only evidence for detailed methods, subgroup effects, or limitations that the abstract does not contain.

### 4. Specify reproducible methods

Before data collection, define or mark pending:

- inclusion, exclusion, stopping, and pilot criteria;
- primary, secondary, and exploratory outcomes;
- power or sensitivity assumptions;
- randomization, concealment, blinding, and reliability;
- model, intervention, prompt, or task fidelity;
- held-constant time, interface, budget, and instructions;
- missingness, deviations, outliers, and multiplicity;
- effect sizes, confidence intervals, and sensitivity analyses;
- qualitative codebook and disagreement handling;
- preregistration and reproducibility-package structure.

Name the decision owner for unresolved choices instead of silently choosing values to make the method look complete.

### 5. Build honest figures

Pre-data figures may show a conceptual model, condition contrast, study procedure, or analysis pipeline. Mark theoretical paths as `proposed` or `planned`, preserve editable sources and accessibility text, and do not create graphics that imply observed effects before data exist.

### 6. Apply integrity safeguards

Use four layers:

1. claim-to-source traceability;
2. quote-versus-paraphrase labels with locations;
3. bounded phrase-overlap checks against the acquired corpus;
4. institution- or publisher-approved similarity screening where required.

A local overlap script cannot prove zero plagiarism. Prepare a venue-specific AI-use disclosure and keep humans responsible for sources, methods, interpretation, authorship, and final text.

### 7. Verify the package

Check:

- official venue evidence and retrieval dates;
- source ledger completeness and pending full texts;
- citation-to-reference and reference-to-citation consistency;
- claim wording against source boundaries;
- figure files, captions, embeddings, and planned labels;
- absence of fabricated-result patterns;
- ethics, supervisor, pilot, collection, and similarity-screening gates.

Use precise status labels such as `venue strategy drafted`, `core sources full-text reviewed`, `proposed-method figures created`, `formal similarity screening pending`, and `empirical results not collected`.

## Deliverables

A durable package normally includes:

1. manuscript master draft;
2. venue and submission strategy;
3. evidence ledger and claim-source matrix;
4. figure index and editable assets;
5. method and preregistration draft;
6. instruments, prompts, tasks, or rubric appendices;
7. integrity, authorship, and AI-disclosure note;
8. reproducibility and data-availability plan;
9. final submission checklist.

## Common Failure Modes

- treating DOI metadata as support for a detailed claim;
- selecting a venue by reputation instead of scope;
- generalizing across incompatible populations or tasks;
- presenting pilot or exploratory findings as confirmatory evidence;
- using decorative diagrams that encode no theory or procedure;
- promising plagiarism-free status from a limited local scan;
- reporting a polished pre-data draft as empirically complete.
