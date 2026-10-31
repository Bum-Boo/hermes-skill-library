#!/usr/bin/env python3
"""Read-only consistency check for the skill library (review artifact).

Usage: python3 -I review/check_consistency.py [REPO_ROOT]
Prints one line per finding; exit 1 if any finding.
"""
import json
import re
import sys
from pathlib import Path

import yaml

root = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent)
problems = []

# 1. frontmatter
skills = {}
for f in sorted(root.glob("skills/*/*/SKILL.md")):
    text = f.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        problems.append(f"{f}: no frontmatter")
        continue
    fm = yaml.safe_load(m.group(1))
    name = fm.get("name")
    for key in ("name", "description", "version", "license"):
        if not fm.get(key):
            problems.append(f"{f.relative_to(root)}: missing {key}")
    if name != f.parent.name:
        problems.append(f"{f.relative_to(root)}: name {name!r} != dir {f.parent.name!r}")
    if name in skills:
        problems.append(f"duplicate skill name {name}")
    skills[name] = (f.parent.relative_to(root / "skills"), fm)

for name, (_, fm) in skills.items():
    rel = ((fm.get("metadata") or {}).get("hermes") or {}).get("related_skills") or []
    ext = [r for r in rel if r not in skills]
    if ext:
        problems.append(f"{name}: related_skills not in this library: {ext}")

# 2. collections: catalog vs installer vs collection dirs vs README tables
catalog = json.loads((root / "catalog.json").read_text(encoding="utf-8"))
cat_cols = catalog["collections"]
installer = (root / "scripts/install-collection.sh").read_text(encoding="utf-8")
case_labels = re.findall(r"^  ([a-z0-9-]+)\)$", installer, re.M)
usage = re.search(r'Collections: ([^"]+)"', installer).group(1).split(", ")
dirs = sorted(p.name for p in (root / "collections").iterdir() if p.is_dir())
for label, seq in (("installer case", case_labels), ("installer usage", usage), ("collections/ dirs", dirs)):
    if set(seq) != set(cat_cols):
        problems.append(f"catalog vs {label}: only-catalog={sorted(set(cat_cols)-set(seq))} only-{label}={sorted(set(seq)-set(cat_cols))}")
for readme in sorted(root.glob("README*.md")):
    listed = set(re.findall(r"\(collections/([a-z0-9-]+)/\)", readme.read_text(encoding="utf-8")))
    missing = sorted(set(cat_cols) - listed)
    if missing:
        problems.append(f"{readme.name}: collection table missing {missing}")

# skills per collection: catalog vs installer cp lines vs collection README
blocks = dict(re.findall(r"^  ([a-z0-9-]+)\)\n(.*?)\n    ;;", installer, re.M | re.S))
for col, meta in cat_cols.items():
    cat_sk = set(meta["skills"])
    for s in cat_sk - set(skills):
        problems.append(f"catalog {col}: unknown skill {s}")
    body = blocks.get(col, "")
    inst = set(re.findall(r'skills/[a-z0-9-]+/([a-z0-9-]+)"', body))
    if "skills/gstack-safe/.\"" in body:
        inst = {n for n, (p, _) in skills.items() if p.parts[0] == "gstack-safe"}
    if inst != cat_sk:
        problems.append(f"{col}: catalog={sorted(cat_sk)} installer={sorted(inst)}")
    readme = root / "collections" / col / "README.md"
    if readme.exists():
        rd = set(re.findall(r"^- \[?`([a-z0-9-]+)`", readme.read_text(encoding="utf-8"), re.M))
        if rd != cat_sk:
            problems.append(f"collections/{col}/README.md lists {sorted(rd)} but catalog has {sorted(cat_sk)}")
in_any = set().union(*(set(m["skills"]) for m in cat_cols.values()))
for s in sorted(set(skills) - in_any):
    problems.append(f"skill {s} is in no collection")

# 3. relative markdown links
for md in sorted(root.rglob("*.md")):
    if ".git" in md.parts or "review" in md.parts:
        continue
    text = re.sub(r"```.*?```", "", md.read_text(encoding="utf-8"), flags=re.S)
    for target in re.findall(r"\]\(([^)\s]+)\)", text):
        if re.match(r"[a-z]+:", target) or target.startswith("#"):
            continue
        if not (md.parent / target.split("#")[0]).exists():
            problems.append(f"{md.relative_to(root)}: broken link {target}")

# 4. repository URL
if "Bum-Boo/hermes-skill-library" not in catalog.get("repository", ""):
    problems.append(f"catalog.json repository={catalog.get('repository')} differs from README clone URL Bum-Boo/hermes-skill-library")

for p in problems:
    print(p)
print(f"{len(problems)} finding(s)")
sys.exit(1 if problems else 0)
