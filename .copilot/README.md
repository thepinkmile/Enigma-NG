# Copilot Session State

This folder contains the canonical GitHub Copilot handoff state for the Enigma-NG project.
**This folder is tracked in version control** and serves as the single source of truth for
resuming work across sessions.

## Purpose

Each Copilot CLI session is assigned a new UUID-based folder under the user profile
(`%USERPROFILE%\.copilot\session-state\<uuid>\`). By maintaining a canonical copy here,
the assistant can pick up exactly where it left off in any future session without needing
to hunt through user-profile paths.

## How to use (at the start of a new session)

Tell Copilot:

> "Please read `.copilot/plan.md` and all checkpoints in `.copilot/checkpoints/` to align
> yourself with the current project state before we continue."

## Contents

| File | Description |
|------|-------------|
| `plan.md` | Current session plan — todos, board status, critical notes, next steps |
| `checkpoints/index.md` | Chronological list of all checkpoints |
| `checkpoints/NNN-*.md` | Individual checkpoint snapshots (history, work done, technical details) |
| `components-todo.md` | Component re-verification tracking table (107 unique parts) |
| `files/` | Session artifacts (design docs, changelogs, reference material) |

## Maintenance

The assistant updates these files at meaningful milestones:
- After each review cycle clean pass
- When a board detailed design is marked complete
- Before ending a session (checkpoint save)
- A checkpoint is only complete once the checkpoint markdown, checkpoint index, plan, and any
  related handoff artifacts have all been written or synced into this repo-local `.copilot\` folder.

**All changes to `.copilot/` must be committed to version control** so the handoff state is
preserved across sessions and machines.

## Version Control

**This folder is tracked in git.** All checkpoint files, plan updates, component tracking,
and session artifacts should be committed alongside design specification changes.

Content here is sanitized to be portable across machines and users:
- Repo-relative paths (not machine-specific absolute paths)
- `%USERPROFILE%` placeholders for user-profile references
- No Copilot session UUIDs or credentials
