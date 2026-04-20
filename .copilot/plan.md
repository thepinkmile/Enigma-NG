# Enigma-NG Session Plan

> Canonical state: `.copilot/plan.md` in the repository root (tracked in git).
> Update this file at the end of each session or at meaningful milestones.
> At the start of a new session, read this file plus `.copilot/handoff.md` and the latest relevant
> checkpoints in `.copilot/checkpoints/`.

---

## Overview

The repository is now in a **clean repo-local handoff state** after closing the manual component
verification sweep and removing redundant Copilot working notes.

Recent milestones now applied in the working tree:

- the final stale component-tracker bucket rows were removed
- the old `.copilot/components-todo.md` and `.copilot/component-types-summary.md` files were retired
- the old `.copilot/files/*.md` historical session notes were audited and removed
- `.copilot/handoff.md` now serves as the single generic repo-local handoff note
- the active `design/` documents already carry the important design facts from those retired notes

Current goal: leave the tree **commit-ready** tonight so the next session can begin from the
repo-local state directly, without repeating component-tracker or handoff-note cleanup.

### Immediate remaining work

1. Create the commit for the current design and `.copilot/` sync.
2. Start the next session from `.copilot/plan.md`, `.copilot/handoff.md`, and checkpoint 056.
3. Resume only the genuine open design-review and mechanical follow-up items.

---

## Repo-Local Handoff Layout

Use the following files as the persistent repo-local session state:

| File | Purpose |
|------|---------|
| `.copilot/plan.md` | Current project/session state, open workstreams, and next steps |
| `.copilot/handoff.md` | Generic handoff note for non-design workflow context that is still worth carrying |
| `.copilot/checkpoints/index.md` | Chronological checkpoint history |
| `.copilot/checkpoints/NNN-*.md` | Individual checkpoint snapshots |

Historical one-off working notes are no longer kept under `.copilot/files/`; if a future session
needs a persistent repo-local note, prefer folding it into `handoff.md` unless a separate artifact
is genuinely required.

---

## Current Open Workstreams

| ID | Status | Scope |
|----|--------|-------|
| `grounding-rules-cleanup` | done | Global rule locked: enclosure-connected boards use `GND_CHASSIS`; non-chassis-connected daughterboards are exempt; the only galvanic `GND` ↔ `GND_CHASSIS` bond remains on the Power Module before the eFuse |
| `rerun-deep-reviews` | in_progress | Rerun the deep review agents only after the next material design-doc change set |
| `extension-mechanical-usage` | pending | Review how Extensions should be used mechanically, including whether interconnect choices for the Stator / Reflector / Extension chain should change |
| `encoder-board-split-review` | pending | Review whether the Encoder Board should split into separate Keyboard and Lightboard physical assemblies |
| `extension-notch-pass-through` | pending | Review whether Extensions need additional servo circuitry to pass through notch rotations |

All component-review and handoff-cleanup tasks are complete for this phase.

---

## Component Verification Status

The manual component verification sweep is **closed** for the current repo-local state.

- No remaining `RECHECK` rows remain in the retired tracker.
- Verified supplier / MPN data has already been propagated into the active design docs where needed.
- The old tracker files were removed because they no longer carried unique design information.

For future part work, treat the active design docs as the source of truth:

- `design/Electronics/Consolidated_BOM.md`
- board-level `design/Electronics/*/Design_Spec.md`
- `design/Datasheets/` for local datasheet evidence

---

## Board Design Status

| Board | Status |
|-------|--------|
| Power Module | ✅ Complete |
| Stator | ✅ Complete |
| Reflector | ✅ Complete |
| Extension | ✅ Complete |
| JDB | ✅ Complete |
| Controller | ✅ Complete |
| Encoder | ✅ Complete |
| Rotor | ✅ Complete |
| Settings Board | ✅ Complete |

---

## Next Session Start Point

Start the next clean session by reading:

1. `.copilot/plan.md`
2. `.copilot/handoff.md`
3. `.copilot/checkpoints/056-component-closeout-and-handoff-consolidation.md`
4. any earlier checkpoints directly relevant to the next task

Then proceed straight into the next real design task rather than reconstructing old component
verification state.

---

## Checkpoint Procedure

Every checkpoint MUST include ALL of the following steps:

1. Write the checkpoint file to `.copilot/checkpoints/NNN-short-title.md`.
2. Update `.copilot/checkpoints/index.md`.
3. Update `.copilot/plan.md`.
4. Sync any related repo-local handoff artifacts into `.copilot/`.
5. Sanitize all repo-local handoff content for version control:
   - use repo-relative paths or `%USERPROFILE%` placeholders instead of machine-specific absolute paths
   - do not store raw usernames, credentials, or Copilot session IDs
6. Verify the repo-local checkpoint artifacts exist before declaring the checkpoint complete.

---

## Critical Notes

### Component / MPN discipline

- Never change a component MPN without a matching local datasheet review in `design/Datasheets/`.
- The correct eFuse is **TPS259804ONRGER**; **TPS259807ONRGER is wrong** for this design.
- Use **ERA** parts where the design explicitly needs thin-film / 0.1% accuracy; do not silently
  substitute them with **ERJ** thick-film parts.

### Settings Board final state

- `U_EXP_SW_IN @ 0x23`
- `U_LED_B1 @ 0x24`
- `U_LED_B2 @ 0x25`
- `J_I2C` / `J_CFG` is the 6-wire harness carrying `3V3_ENIG`, `5V_MAIN`, `GND`, `SDA`, `SCL`, `GND`
- RGB LED operation is the final 5V design: 150 ohm red, 100 ohm green, 100 ohm blue

### HID / keyboard final state

- Physical HID layout is **40 positions**
- Printable positions are `[a-z0-9+=]`
- The two modifier positions are **Left Shift** and **Right Shift**
- The logical repertoire remains the full **64-character** code space

### JTAG topology reminders

- JTAG travels through the rotor stack on the ERM8/ERF8 board-to-board connectors, not ribbon cable
- The Reflector remains the end of the chain; Reflector `R1` is the 22 ohm TDO damping resistor
- Extension `U1` (`SN74LVC2G125DCUR`) is intentional and must not be removed

### Repo-local state rules

- `.copilot/` is tracked in git and must be kept in sync with meaningful design-state changes
- `handoff.md` is the generic persistent note; avoid recreating ad hoc historical note files unless a
  separate artifact is truly needed
