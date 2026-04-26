# Copilot Session State
This folder contains the canonical GitHub Copilot handoff state for the Enigma-NG project.
**This folder is tracked in version control** and serves as the single source of truth for
resuming work across sessions.
## Purpose
Each Copilot CLI session is assigned a new UUID-based folder under the user profile
(`%USERPROFILE%\.copilot\session-state\<uuid>`). By maintaining a canonical copy here,
the assistant can pick up exactly where it left off in any future session without needing
to hunt through user-profile paths.
## How to use (at the start of a new session)
Tell Copilot:

> "Please read `.copilot/plan.md`, `.copilot/handoff.md`, and the relevant checkpoints in
> `.copilot/checkpoints/` to align yourself with the current project state before we continue."
## Contents
| File | Description |
|------|-------------|
| `plan.md` | Current session plan — state, open workstreams, critical notes, next steps |
| `handoff.md` | Generic repo-local handoff note for persistent non-design workflow context |
| `agent-scripts/` | Repo-local helper scripts for repeatable Copilot maintenance tasks |
| `checkpoints/index.md` | Chronological list of all checkpoints |
| `checkpoints/NNN-*.md` | Individual checkpoint snapshots (history, work done, technical details) |
## Maintenance
The assistant updates these files at meaningful milestones:

- after each review cycle clean pass
- when a board detailed design is marked complete
- before ending a session (checkpoint save)
- when repo-local handoff notes need consolidation or cleanup

A checkpoint is only complete once the checkpoint markdown, checkpoint index, plan, and any
related handoff artifacts have all been written or synced into this repo-local `.copilot\` folder.
## Version Control
**This folder is tracked in git.** All checkpoint files, plan updates, and handoff-state changes
should be committed alongside design specification changes.

Content here is sanitized to be portable across machines and users:

- repo-relative paths (not machine-specific absolute paths)
- `%USERPROFILE%` placeholders for user-profile references
- no Copilot session UUIDs or credentials
