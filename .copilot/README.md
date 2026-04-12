# Copilot Session State

This folder contains the canonical GitHub Copilot session state for the Enigma-NG project.
It is **gitignored** and never committed to the repository.

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
