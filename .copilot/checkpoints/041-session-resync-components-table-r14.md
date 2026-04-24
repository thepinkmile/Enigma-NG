# Checkpoint 041 — Session resync, component table normalized, R14 relaunch pending
## Date
2026-04-15
## Session
<sanitized-session-id>
## Overview
The repo-local `.copilot` state was slightly stale but still the best available sync point. This
checkpoint updates that local state so the next session starts from the current reality instead of
the pre-rate-limit snapshot. The pending R14 review did **not** fail because of review findings;
it failed due to rate limiting and needs to be relaunched from the existing R13 clean pass.

`.copilot/components-todo.md` was also normalized into a single re-verification table so the user
can manually re-check every candidate component row before anything is pushed back into the design
docs. At least one row is currently marked `SUSPECT` because its value and candidate MPN do not
agree internally.
## Work Done
### Review-cycle state refreshed
- Updated `.copilot/plan.md` so R14 is no longer shown as merely pending.
- Recorded that the previous R14 run ended due to rate limiting.
- Kept the canonical status: R13 is the current clean pass #1 of 2.
### Component re-verification table normalized
- Reframed `.copilot/components-todo.md` as the canonical **single-table** manual verification
  workspace.
- Changed the status column from `Confirmed` to `Verification` so the file is explicit about review
  state instead of implying boolean finality.
- Marked all rows as provisional (`RECHECK` / `BLOCKED` / `SUSPECT`) rather than trustworthy.
- Flagged `R_BASE (x4)` as `SUSPECT` because the row currently mixes a 1 kohm requirement with
  candidate MPN `ERJ-2RKF1002X`, which decodes as 10 kohm.
### Checkpoint index tidied
- Added a note to `.copilot/checkpoints/index.md` that historical checkpoint files 034 and 035 are
  referenced by later local material but are not present in the current repo-local snapshot.
- Added this checkpoint to the index so the resync work is discoverable.
## Commits
None. `.copilot/` is local-only session state and remains intentionally uncommitted.
## Key Technical Notes
- R14 must be treated as a **rerun after rate limiting**, not as a failed technical review.
- `.copilot/components-todo.md` is now a preparation artifact for manual validation; it is not an
  authority source for design changes until rows are explicitly verified.
- Current supercap canonical state remains: **Abracon ADCR-T02R7SA256MB, 25F/2.7V, 2S4P, 8 cells,
  50F at 5.4V, >=33.5 s hold-up**.
## Next Steps
1. Relaunch R14 using the current repo state and the established review constraints.
2. Manually re-verify rows in `.copilot/components-todo.md`.
3. Update design BOMs only after rows are explicitly confirmed.
