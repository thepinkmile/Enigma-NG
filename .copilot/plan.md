# Enigma-NG Session Plan
> Canonical state: `.copilot/plan.md` in the repository root (tracked in git).
> Update this file at the end of each session or at meaningful milestones.
> At the start of a new session, read this file plus `.copilot/handoff.md` and the latest relevant
> checkpoints in `.copilot/checkpoints/`.

---
## Overview
The repository is in a **clean repo-local handoff state** and now also carries the latest
Power Module / Controller / Linux OS power-management documentation sync from 2026-04-24,
followed by a root `README.md` refresh so the top-level project summary better matches the
current board set and review-state wording.

Recent milestones now applied in the working tree:

- Power Module and Controller docs now agree on the `LED_nPWR` / SW2 hardware-indicator design
- SW1 / SW2 LED behavior is now aligned across the PM spec and Linux OS power-management doc
- the PM eFuse latch-off recovery procedure was moved into `design/Guides/Maintenance_Guide.md`
- PM and Controller thermal sections are now board-local rather than cross-referencing each other
- `Design_Log.md` mojibake / stale staged-copy issue was corrected
- Linux OS power-management open items were reduced to the genuinely unresolved prototype-stage item(s)
- `README.md` now includes the missing board summaries, updated hardware-flow ordering, and `In Review`
  wording for the current pre-issue-1 board state

Current goal: leave the tree **commit-ready** tonight so the next session can begin from the
repo-local state directly, without reconstructing today's documentation work.
### Immediate remaining work
1. Create the commit for the current design and `.copilot/` sync.
2. Start the next session from `.copilot/plan.md`, `.copilot/handoff.md`, and checkpoint 058.
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
| `battery-connector-review` | pending | Review battery connector alternatives and capture any resulting design-document updates |
| `encoder-board-split-review` | in_progress | Replace the current dual-half Encoder board with a single generic half-board design reused as KBD_ENC, LBD_DEC, PLG_PASS1_DEC, PLG_PASS1_ENC, PLG_PASS2_DEC, and PLG_PASS2_ENC; Stator grows to 6 encoder connectors in 3 banks of 2 with the existing pinout retained |
| `extension-mechanical-usage` | pending | Review how Extensions should be used mechanically, including whether interconnect choices for the Stator / Reflector / Extension chain should change |
| `extension-notch-pass-through` | pending | Review whether Extensions need additional servo circuitry to pass through notch rotations |
| `coupon-testing-review` | pending | Add and review board-level coupons for PAS and manual testing across the design set |
| `rerun-deep-reviews` | pending | Rerun the deep review agents only after the next material design-doc change set |

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
| Power Module | In Review |
| Stator | In Review |
| Reflector | In Review |
| Extension | In Review |
| JDB | In Review |
| Controller | In Review |
| Encoder | In Review |
| Rotor | In Review |
| Settings Board | In Review |

---
## Next Session Start Point
Start the next clean session by reading:

1. `.copilot/plan.md`
2. `.copilot/handoff.md`
3. `.copilot/checkpoints/058-readme-architecture-sync-and-handoff.md`
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
