---
name: downstream-source-maintenance
description: "Use when auditing or maintaining a fork, mirror, vendored snapshot, or other codebase derived from upstream."
version: 1.0.0
author: bumboo / Hermes Skill Library contributors
license: MIT
metadata:
  hermes:
    tags: [downstream, fork, vendoring, upstream-sync, repository-audit, release-engineering]
    related_skills: [local-code-change-workflow, verification-before-completion]
---

# Downstream Source Maintenance

## Overview

Review derived codebases for both runtime correctness and maintainability. A downstream is ready only when its upstream baseline is reproducible, its changes can be advanced safely, its distribution stays on the intended channel, and inherited automation cannot publish unintended artifacts.

## Workflow

### 1. Inspect live state first

1. Record the supplied repository's default-branch SHA, visibility, fork metadata, tags, releases, and current checks.
2. Clone only when deeper diff or test work is needed, using an approved workspace.
3. Confirm local HEAD equals the live branch SHA before making current-state claims.
4. Read repository instructions before reviewing or changing code.

Conversation history is not proof of current repository contents.

### 2. Classify the downstream model

Check separately:

- hosting-platform fork metadata;
- Git common ancestry with upstream;
- declared upstream commit or tag;
- patch or replay artifacts;
- public mirror versus integration repository;
- whether future imports use ordinary commits or history rewrites.

Do not describe a squashed snapshot as a normal fork; unrelated history changes the update strategy.

### 3. Compare with a pinned baseline

Use the declared upstream commit or tag, not moving upstream `main`. Summarize changed paths and review high-risk seams first:

- authentication, credentials, quotas, and billing;
- installer, updater, package, and release identity;
- lifecycle and service management;
- authorization and message routing;
- state and session boundaries;
- publishing workflows.

### 4. Audit distribution identity

Inspect every install and update path independently: source-install documentation, bootstrap scripts, CLI or in-app updater, archive fallback, container images, manifests, tags, and package metadata. A fallback that silently replaces a downstream installation with upstream is a release blocker.

### 5. Audit inherited automation

Enumerate workflow triggers, especially schedules, releases, `workflow_run`, deployment, Pages, container publishing, and comment bots. Query checks for the exact current default-branch SHA. Report targeted local tests separately from repository CI status.

### 6. Review privacy safely

Use secret scanners but redact at the extraction boundary. Report only finding type, status, location, and commit identity—never candidate secret values. Distinguish inherited test fixtures from downstream additions while resolving verified false positives.

A force-push alone does not prove old public content disappeared; persistent refs, releases, pull-request refs, alerts, and known commits may remain.

### 7. Verify concrete findings

Run the repository's canonical test wrapper. Start with changed tests, then add narrow regression probes for suspected defects. Use temporary state and mocked or dry-run side-effect boundaries.

### 8. Recommend fixes in dependency order

1. correctness and security defects;
2. green current-main CI;
3. inherited scheduled or release automation;
4. downstream install, update, and release identity;
5. deterministic upstream replay or import process;
6. separation of downstream-specific data from upstream-hot core files;
7. branch protection and required checks.

## Common Pitfalls

- Treating hosting metadata alone as evidence that a repository is independent.
- Comparing only with moving upstream `main`.
- Trusting release-note test counts without fresh execution or exact-SHA CI evidence.
- Running broad token searches that print candidate credentials.
- Reporting an old workflow run as current because its title looks relevant.
- Preserving every upstream schedule and release job in a public mirror.
- Claiming replay support while required patch artifacts are absent.
- Calling a snapshot updateable when its updater assumes shared ancestry.

## Verification Checklist

- [ ] Live and local default-branch SHAs agree.
- [ ] Upstream baseline and ancestry model are explicit.
- [ ] Replay or update path matches the repository's history model.
- [ ] Installer and fallback URLs stay on the intended channel.
- [ ] Current-main CI is reported separately from local tests.
- [ ] Publish, deploy, release, and schedule triggers were reviewed.
- [ ] Secret findings were projected or redacted before display.
- [ ] Concrete bugs were reproduced at a safe side-effect boundary.
