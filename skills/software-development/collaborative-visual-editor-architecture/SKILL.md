---
name: collaborative-visual-editor-architecture
description: "Design and verify multi-user visual editors with explicit collaboration, persistence, execution, and authorization boundaries."
version: 1.0.0
author: Hermes Skill Library contributors
license: MIT
metadata:
  hermes:
    category: software-development
    tags: [collaboration, visual-editor, node-graph, websocket, architecture]
---

# Collaborative Visual Editor Architecture

## When to use

Use for shared node graphs, whiteboards, visual workflows, and canvas-based tools where several people must edit the same live artifact. A shared library, exported file, screen share, and multi-user execution queue are different products; establish which one the user means before choosing technology. When users must join a session and directly connect nodes in an existing tool, do not redirect them to exchanging files or rebuilding a merely similar canvas.

## Investigation sequence

1. **Identify the real host.** Record the application and version, editor surface, authentication model, compute topology, and whether the request is research, a prototype, or an approved deployment. Prior notes are not proof of current runtime state.
2. **Inspect native extension points first.** Prefer official editor, graph, and plugin APIs. For third-party candidates, inspect source, license, issue history, recent activity, and actual support for independent rooms instead of trusting a feature list.
3. **Inventory graph operations.** Cover node create/delete/move, links and slots, widgets, groups, copy/paste, undo/redo, uploads, metadata, and workflow load. If public hooks are incomplete, propose a narrowly pinned adapter or fork and state its upgrade burden.
4. **Separate three planes.** Collaboration owns rooms, canonical graph operations, and presence. Persistence owns snapshots, revisions, and restore. Execution owns validated immutable snapshots, queues, progress, and outputs. An execution server's progress socket is not automatically a collaborative graph protocol.
5. **Choose concurrency to fit the requirement.** A small online group may need only a server-authoritative ordered operation stream with invariant checks and replay. Consider CRDTs for offline-first or large-scale merging, but still validate link endpoints, slot types, deletion, and undo on the server. Presence and cursors are ephemeral, not saved graph state.
6. **Authorize every operation server-side.** Define viewer, editor, runner, and administrator roles. Authenticate socket handshakes, validate room membership, support revocation, bound payloads, and block dangerous backend routes. Disabled UI controls are not access control. Keep paid nodes, uploads, package installation, and execution permissions separate from ordinary editing.
7. **Execute named immutable revisions.** Apply per-user or per-room queue and cancellation rules, and record the initiating actor and result. Failed execution must not mutate the saved graph.

## Minimum validation

- Two distinct users concurrently add, connect, move, delete, and edit nodes; both converge and reload to the same graph.
- Same-node edits, deletion versus link creation, simultaneous connections to one input, import, undo, connection loss, and replay preserve graph invariants or surface an explicit conflict.
- Room A cannot observe Room B state, presence, or jobs. Viewers cannot edit, and editors cannot execute unless granted. Direct HTTP and socket requests cannot bypass UI restrictions.
- Save and reload round-trip the editor format, while execution submits only the engine format. Failed jobs do not change saved revisions. Revision restore and output attribution work.
- Prototype versions are pinned, and frontend or extension upgrades are tested independently.

## Reporting

Give a short verdict, a diagram or list of system boundaries, one concrete first experiment, and a separate risks and unknowns section. Label static source review, working local tests, and live deployment as distinct evidence levels. If research spans multiple languages, identify which authoritative and non-authoritative sources were actually read; translations are not independent corroboration.

## Safety boundaries

- Do not expose inference, storage, or administration services directly to the public internet by default.
- Do not accept client-generated authorization claims or trust room identifiers without server validation.
- Do not install arbitrary extensions or execute paid workloads as part of an architecture spike.
- Do not describe an untested design as a working implementation.
