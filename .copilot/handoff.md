# Enigma-NG Handoff
This file is the generic repo-local handoff note for session-to-session context that is useful to
keep near the design docs but is **not** itself a source of design truth.

## Canonical design sources
Use the active `design/` documents as the authoritative record:

- `design/Design_Log.md`
- `design/Electronics/Consolidated_BOM.md`
- board-level `design/Electronics/*/Design_Spec.md`
- board-level `design/Electronics/*/Board_Layout.md`
- relevant mechanical and software `Design_Spec.md` files
- `design/Datasheets/` for preserved vendor and project-side reference material

## 2026-04-25 session result
The latest documentation review and cleanup phase is now reflected in the repository state.

Main outcomes:

- stale `probe` / `diagnostic` wording was removed from active design specs and board layouts
- board-layout headings were normalized so section numbering is file-local and `§` stays reserved
  for cross-document references
- the Reflector simplified layout was corrected to remove the duplicate Data Plate label
- Controller / Stator / Settings wording was cleaned up so I2C ownership, pass-through behavior,
  and servo ownership live in the correct documents
- the Stator Settings-board connector refdes was normalized from `J_CFG` to `J13`
- `.github/workflows/wiki-sync.yml` was updated to exclude `design/Datasheets`
- active component refdes were normalized to numeric refs across the design docs and consolidated
  BOM; this was committed as `7829f8a` (`Normalize design document refdes`)
- all markdown document metadata `Version` headers were reset to `v.0.1.0` by explicit user
  direction because the project is still in design phase

## Documentation policy reminders
- Do not update document `Version` metadata unless the user explicitly requests it.
- Do not infer version bumps from the size or perceived significance of a change.
- Keep `.copilot/` synchronized with meaningful design-state changes, but treat it as handoff
  material rather than design truth.

## Remaining follow-up work
These are still open design review items, but they are not yet committed design decisions:

1. Review battery connector alternatives.
2. Continue the Encoder board split review and any resulting architecture cleanup.
3. Review how Extensions should be used mechanically, including whether interconnect choices for the
   Stator / Reflector / Extension chain should change.
4. Review whether Extensions need additional servo circuitry to pass through notch rotations.
5. Add and review board-level coupons and PAS-oriented test coverage.
6. Rerun deep review agents after the next material design-doc change set.
