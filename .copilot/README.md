# Copilot Session State

This folder contains the canonical repo-local GitHub Copilot handoff state for the Enigma-NG project.
Its contents are the source of truth for resuming work across sessions and are intended to remain
safe to version control.

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

## Maintenance

The assistant updates these files at meaningful milestones:
- After each review cycle clean pass
- When a board detailed design is marked complete
- Before ending a session (checkpoint save)
- A checkpoint is only complete once the checkpoint markdown, checkpoint index, plan, and any
  related handoff artifacts have all been written or synced into this repo-local `.copilot\` folder.

## Commit safety

No credentials or API secrets are expected here, but raw session-state material can include
local-machine metadata such as:

- user-profile paths like `%USERPROFILE%\.copilot\...`
- Copilot session UUIDs

When syncing content into this folder, normalize that metadata first so committed handoff files stay
portable across machines and users.
