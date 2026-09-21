---
name: local-artifact-recovery
description: "Recover and verify the correct prior local deliverable using provenance, content, and hash evidence."
version: 1.0.0
author: Hermes Skill Library contributors
license: MIT
metadata:
  hermes:
    category: productivity
    tags: [local-files, recovery, deliverables, provenance, deduplication]
---

# Local Artifact Recovery

Recover the correct prior local deliverable when the user remembers its purpose, authoring tool, rough date, or filename but not its exact path. Treat this as a file-provenance task: do not stop at the first plausible filename.

## When to use

- The user asks to find a file created earlier or says a better version should exist.
- Several exports have generic names such as `Portfolio.pdf`, `test.pdf`, or `final.pdf`.
- The correct artifact must be copied into a meeting, submission, or delivery folder.

## Procedure

1. **Define the evidence target.** Record the remembered purpose, approximate date, expected format, authoring tool, likely filename, and likely folders. Treat each as a clue, not proof.
2. **Separate recovery from interpretation.** Do not summarize, advise from, or deliver an artifact until its identity is sufficiently supported. If confidence remains low, report candidates and the evidence that would distinguish them.
3. **Search likely roots before broad traversal.** Start with the explicitly named folder, then user-approved project and common document roots. Search case variants and generic names separately. Stay within authorized locations.
4. **Enumerate sibling candidates.** Collect path, size, filesystem modified time, page count or equivalent format metadata, embedded creator/producer, and document creation/modification metadata when available.
5. **Use authoring provenance.** Embedded tool metadata can distinguish exports from different applications, but it does not by itself prove which one is final.
6. **Inspect content, not only filenames.** Extract text when available. For image-only or very large PDFs, render page 1 and a low-resolution contact sheet. Compare title, project list, page order, placeholders, and completeness.
7. **Rank versions with multiple signals.** Prefer a candidate only when filename, provenance, content completeness, timestamps, and the user's description align. A later filesystem timestamp may merely indicate a copy.
8. **Confirm duplicates carefully.** Byte hashes prove exact identity. Equal extracted text or similar images do not prove byte identity because compression and encoding may differ.
9. **Deliver with a descriptive filename.** Copy rather than move unless relocation was explicitly requested. Replace only the specifically authorized destination if correcting an earlier mistaken copy.
10. **Verify after copying.** Compare source and destination hashes, reopen the destination, and verify key properties such as page count and creator.

## Format-specific notes

- **Text PDF:** inspect metadata and extracted text.
- **Image-only PDF:** render page 1 plus a contact sheet; empty extracted text does not mean empty content.
- **Oversized PDF:** inspect through a suitable PDF library rather than assuming a generic reader can load it.
- **Multiple exports:** compare page counts, metadata, text, and visual summaries before selecting.

## Pitfalls

- **First-match bias:** a plausible test-named file may still be a draft.
- **Filename overconfidence:** a generic filename may hold the actual final.
- **Timestamp overconfidence:** copying can alter filesystem times.
- **Tool-memory mismatch:** verify creator/producer metadata when the remembered authoring tool matters.
- **Premature delivery:** check competing sibling versions first.
- **Correction inertia:** if the user rejects a candidate, retract the identification and widen the search using the new clue.
- **Broad scanning:** avoid unrelated, protected, or unapproved directories.
- **Destructive cleanup:** do not delete drafts or duplicates merely because a final was identified.

## Verification checklist

- [ ] Likely filename and case variants searched
- [ ] Sibling candidates enumerated
- [ ] Authoring provenance checked
- [ ] Content inspected textually or visually
- [ ] Ranking supported by more than one signal
- [ ] Source copied rather than moved unless requested
- [ ] Destination hash matches source
- [ ] Destination opens and key properties match
- [ ] Delivered filename is descriptive
