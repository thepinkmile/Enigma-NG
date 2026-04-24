# Checkpoint 037 — Remove .copilot/ from git tracking
## Date
2026-04-14
## Session
<sanitized-session-id>
## Overview
The `.copilot/` directory was already listed in `.gitignore` (line 7) but had been
force-added to git tracking in earlier sessions using `git add -f`. This checkpoint
removes all 51 tracked files recursively from the git index so the directory is
no longer version-controlled. Local files are fully preserved.
## Commits
| SHA | Description |
|-----|-------------|
| `261d6fa` | checkpoint 036: Settings Board layout, BOM audit, switch unification |
| `e84ec8e` | remove .copilot/ from git tracking (gitignored — local only) |
## Work Done
- Confirmed `.copilot/` is listed in `.gitignore` line 7
- Ran `git rm -r --cached .copilot/` — removed 51 files from index, local files untouched
- Committed removal as `e84ec8e`
- Stored session memory: "The `.copilot/` directory is in `.gitignore` and must NEVER be
  committed to git. Never use `git add -f .copilot/`."
## Rule Going Forward
**NEVER** use `git add -f .copilot/` or any force-add of the `.copilot/` directory.
The `.copilot/` folder is local-only project state (plan, checkpoints, agent prompts).
It is gitignored for good reason. Checkpoint "sync" means updating the local files
only — it does NOT mean committing them to git.
## Corrected Checkpoint Procedure
The checkpoint procedure in `plan.md` has been updated to clarify:
- "sync" = update local `.copilot/` files only
- Do NOT commit `.copilot/` to git
## State at this Checkpoint
All boards complete. Deep-dive review R1 running (background agent).
See checkpoint 036 for full design state.
## Next Steps
1. Await deep-dive review R1 results; apply fixes; repeat until 2 clean passes.
2. User to source Marquardt 1800 SPDT MPN and other TBD parts.
3. KiCad setup documentation (low priority).
