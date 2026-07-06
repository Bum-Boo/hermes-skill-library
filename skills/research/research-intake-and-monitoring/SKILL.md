---
name: research-intake-and-monitoring
description: "Use when collecting or monitoring external research/source material such as papers, feeds, PDFs, datasets, market pages, or source evidence packages before synthesis."
version: 1.0.0
author: bumboo / Hermes Skill Library contributors
license: MIT
metadata:
  hermes:
    tags: [research, intake, monitoring, sources, evidence, provenance]
    related_skills: [ml-research-and-evaluation-workflows]
---

# Research Intake and Monitoring

## Overview

This skill covers the front half of research work: finding, monitoring, downloading, extracting, and organizing source material with provenance. It prepares reliable inputs for later synthesis, writing, or analysis.

## When to Use

Use when:

- searching scholarly indexes or source websites;
- monitoring RSS/Atom/blog feeds;
- collecting official PDFs, data files, or source packets;
- building a local markdown or document knowledge base;
- preparing an evidence manifest with URLs, timestamps, filenames, and verification counts.

## Non-Triggers

Do not use this for final synthesis, manuscript writing, or opinionated conclusions until source intake is complete. Separate evidence collection from interpretation.

## Protocol

1. Define the source question and accepted source types.
2. Prefer official and primary sources over mirrors or scraped reposts.
3. Record source URLs, identifiers, timestamps, and retrieval method.
4. Download or extract only what is needed.
5. De-duplicate by stable IDs, canonical URLs, filenames, or content hashes.
6. Save an evidence manifest alongside collected files or notes.
7. Verify counts and representative file contents before reporting.
8. If recurring monitoring is requested, record last-seen state and report only changes.

## Source-Type Notes

### Scholarly papers

Capture title, authors, venue/preprint server, year, abstract, URL, and stable identifier when available. Download PDFs only when needed.

### Blogs and feeds

Track feed URL, item IDs, publish dates, and last-seen state. Avoid treating unchanged feeds as new findings.

### Official PDFs and source packets

Prefer the source institution or publisher. Use duplicate-safe filenames and record the source page, not only the file URL.

### Local knowledge bases

Preserve link structure and source note paths. Query results should cite files or URLs, not model memory alone.

## Evidence Manifest Fields

```text
source_id, title, url, retrieved_at, local_path, content_type, status, notes
```

## Common Pitfalls

1. Mixing source intake with synthesis too early.
2. Reporting download counts before checking files exist.
3. Losing provenance when copying text into notes.
4. Re-alerting unchanged feed items because state was not saved.

## Verification Checklist

- [ ] Source URLs or IDs are recorded.
- [ ] Downloaded/generated files exist.
- [ ] Counts match the manifest.
- [ ] Monitoring state is updated intentionally.
- [ ] Output distinguishes evidence from interpretation.
