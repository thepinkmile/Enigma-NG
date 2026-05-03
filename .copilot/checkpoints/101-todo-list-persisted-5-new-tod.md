# Checkpoint 163 — todo-list.md persisted: 5 new todos and deps

## Summary

Completed the outstanding work from the compacted session: persisted all 5 new todos and their deps
to `.copilot/todo-list.md` so they survive session boundaries.

## Files Changed

- **`.copilot/todo-list.md`** — Added:
  - `rotor-refdes-reallocate` row to Electronics Deferrals table and SQL reconstruction
  - `interim-electronics-review-1` through `-4` rows to Project Milestones table and SQL reconstruction
  - Updated Dependency Overview diagram to show the 4-stage review gate chain as a top-level entry
  - Updated `prototype-pcb-manufacturing` and `release-candidate-production` dependency columns to include new gates
  - Added all new `INSERT OR IGNORE` dep entries to SQL Reconstruction Reference

## New Items Summary

| ID | Section | Key deps |
| --- | --- | --- |
| `rotor-refdes-reallocate` | Electronics Deferrals | — |
| `interim-electronics-review-1` | Project Milestones | fix1–fix19 + `rotor-refdes-reallocate` |
| `interim-electronics-review-2` | Project Milestones | review-1 + `coupon-testing-review` + `review-mounting-holes` |
| `interim-electronics-review-3` | Project Milestones | review-2 + `full-pn-review` + `footprint-requests-pending` |
| `interim-electronics-review-4` | Project Milestones | `prototype-system-complete` + `compliance-testing` |

## Standing State

- `prototype-pcb-manufacturing` now also depends on `interim-electronics-review-3`
- `release-candidate-production` now also depends on `interim-electronics-review-4`
- No git commit made — awaiting "Let's lock this in"

## Active Pass 3 Fix Todos

fix1–fix19 all still pending; must complete before `interim-electronics-review-1` can close.
`rotor-refdes-reallocate` also pending before Review 1 can close.

## Directives Reminder

- PRIMARY: Never modify supplier MPNs without explicit user confirmation
- SECONDARY: Never commit without "Let's lock this in" or "Save state"
