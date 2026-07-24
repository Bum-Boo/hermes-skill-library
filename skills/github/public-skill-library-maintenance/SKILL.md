---
name: public-skill-library-maintenance
description: "Use when adding or publishing reusable skills in a public repository; sanitize content, validate metadata, update the catalog, test installation, and verify GitHub readback."
version: 1.0.0
author: bumboo / Hermes Skill Library contributors
license: MIT
metadata:
  hermes:
    tags: [skills, github, publishing, security]
    related_skills: [wsl-github-release-workflows, verification-before-completion]
---

# Public Skill Library Maintenance

## Add or update a skill

1. Confirm the skill is reusable and does not encode one user's private policy as a universal rule.
2. Use one focused directory containing a valid `SKILL.md` with name, trigger-oriented description, version, author, license, tags, and related skills.
3. Generalize machine paths, account names, profile names, chat IDs, service names, and customer-specific procedures.
4. Update the purpose-based collection README, root catalog, and root README.
5. Reject duplicate names, broken collection references, and stale install instructions.

## Security gate

Scan tracked content for credentials, private keys, token-shaped values, private IDs, customer data, absolute user paths, browser profile details, and internal endpoints. Manually inspect warning-word matches; documentation may mention `TOKEN` or `SECRET` without containing a value.

## Validation

- parse all frontmatter and enforce folder/name consistency;
- parse the catalog and verify every listed skill exists;
- verify every skill belongs to at least one collection when that is repository policy;
- install all skills and each changed collection into temporary directories;
- compare installed skill counts and names with source;
- inspect Git diff before commit.

After an approved push, verify the remote commit and raw README/catalog content. Publication is incomplete until remote readback succeeds.
