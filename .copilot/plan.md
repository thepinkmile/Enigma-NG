# Enigma-NG Session Plan
> Canonical state: `.copilot/plan.md` in the repository root (tracked in git).
> Update this file at the end of each session or at meaningful milestones.
> At the start of a new session, read this file plus `.copilot/handoff.md` and the latest relevant
> checkpoints in `.copilot/checkpoints/`.

---
## Overview
The repository is in a **clean repo-local handoff state** and the active working copy now carries
the completed Stator / Settings Board configuration-reset cleanup plus the first broad encoder-bus
documentation cleanup.

The current design state now reflects:

- `CFG_ROUTE[3:0]`, `CFG_REFMAP[5:0]`, active-low `CFG_APPLY_N`
- `CFG_ROUTE_CM5_ACTIVE` / `CFG_REFMAP_CM5_ACTIVE`
- external keyboard-source mux assumptions (`CM5_KEY_DATA[0:5]`, `KEY_SEL`, `KEY_EN`)
- generic Encoder-board `ENC_DATA[0:5]` on 20-pin IDC links
- Stator-owned encoder aliases (`ENC_IN_KBD`, `ENC_OUT_LBD`, `ENC_OUT/IN_PLG1`, `ENC_OUT/IN_PLG2`,
  `ENC_OUT/IN_ROT`, `ENC_OUT/IN_REF`)
- removal of fixed diagnostic banks from the active board set; future diagnostic access should be
  coupon-based

Recent milestones now applied in the working tree:

- Power Module and Controller docs now agree on the `LED_nPWR` / SW2 hardware-indicator design
- SW1 / SW2 LED behavior is now aligned across the PM spec and Linux OS power-management doc
- the PM eFuse latch-off recovery procedure was moved into `design/Guides/Maintenance_Guide.md`
- PM and Controller thermal sections are now board-local rather than cross-referencing each other
- `Design_Log.md` mojibake / stale staged-copy issue was corrected
- Linux OS power-management open items were reduced to the genuinely unresolved prototype-stage item(s)
- `README.md` now includes the missing board summaries, updated hardware-flow ordering, and `In Review`
  wording for the current pre-issue-1 board state
- Stator / Settings Board configuration intent, CM5 override, and apply/reset naming are now aligned
- Stator↔Encoder links are now documented as 20-pin IDC interfaces using generic `ENC_DATA[0:5]`
- fixed diagnostic banks have been removed from active board docs in favour of future coupon-based access

Current goal: leave the tree **commit-ready** tonight so the next session can begin from the
repo-local state directly, without reconstructing today's documentation work.
### Immediate remaining work
1. Finish the remaining ENC net-name cleanup details, especially any role-specific naming still to be normalised.
2. Review and select the new logic parts implied by the cleanup (keyboard-source mux and any reset/apply glue logic).
3. Create the commit for the current design and `.copilot/` sync once the design-doc pass is ready.

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
| `encoder-board-split-review` | in_progress | Replace the current dual-half Encoder board with a single generic half-board design reused as KBD_ENC, LBD_DEC, PLG_PASS1_DEC, PLG_PASS1_ENC, PLG_PASS2_DEC, and PLG_PASS2_ENC; config-reset cleanup and the first Stator-owned encoder alias pass are now applied, with remaining work focused on final ENC net normalisation and new-part selection |
| `extension-mechanical-usage` | pending | Review how Extensions should be used mechanically, including whether interconnect choices for the Stator / Reflector / Extension chain should change |
| `extension-notch-pass-through` | pending | Review whether Extensions need additional servo circuitry to pass through notch rotations |
| `coupon-testing-review` | pending | Add and review board-level coupons for PAS and manual testing across the design set, including moving diagnostic-bank style test access onto removable coupons so production boards do not retain test-only hardware |
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
- The project owner has approved the BOM part numbers already captured in the active design docs.
- Never modify an existing supplier part number (especially Mouser codes) without checking with the
  user first, even if the distributor code looks shorter than the full manufacturer MPN.
- Do not "correct" Mouser part numbers by assuming they must match the full MPN format; Mouser may
  use truncated or non-obvious catalog codes that are nevertheless the confirmed correct order code.
- Do not highlight package, footprint, or component-size differences as a blocking issue while the
  project is still pre-schematic / pre-layout unless the user explicitly says that packaging now
  matters.
- Treat package-family differences as irrelevant at this stage; revisit them only once schematic,
  PCB layout, or post-manufacturing optimization work makes footprint choice a real constraint.
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
