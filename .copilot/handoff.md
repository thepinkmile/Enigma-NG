# Enigma-NG Handoff
This file is the generic repo-local handoff note for session-to-session context that is useful to
keep near the design docs but is **not** itself a source of design truth.
## Canonical design sources
Use the active `design/` documents as the authoritative record:

- `design/Design_Log.md`
- `design/Electronics/Consolidated_BOM.md`
- board-level `design/Electronics/*/Design_Spec.md`
- relevant mechanical and software `Design_Spec.md` files
- `design/Datasheets/` for preserved vendor and project-side reference material
## 2026-04-24 session result
Today's working-tree progress was a documentation-sync pass across the active design docs. The main
outcomes now present in the repo are:

- PM / Controller / Linux OS docs aligned around the `LED_nPWR`-driven SW2 hardware indicator
- SW1 red now represents **PM fault or hold-up unavailable** rather than a generic historical
  shutdown indication
- the PM eFuse latch-off recovery procedure now lives in `design/Guides/Maintenance_Guide.md`,
  with the PM design spec carrying only a cross-reference
- PM and Controller thermal sections are now board-local
- `Design_Log.md` text encoding / staged-state issue was corrected
- Linux OS power-management open items were pruned to the genuine unresolved prototype-stage work
- `README.md` was refreshed to remove stale `{TBD}` placeholders, restore missing board summaries,
  reorder the board walkthrough to follow the system flow, and mark the current board set as
  **In Review** rather than complete

## 2026-04-19 audit result
The older component re-verification and session working notes were audited and removed because
their design-bearing content is already captured in the live docs above.

Retired note sets covered:

- component verification progress and supplier closure
- Settings Board 5V RGB upgrade history
- the 40-position HID keyboard handoff

The active docs now already contain the important design facts that those notes previously carried,
including:

- final Settings Board address map and 6-wire harness definition
- 5V_MAIN-fed Settings Board RGB architecture, resistor values, and current budget
- 40-position HID keyboard layout and shift-key behavior
- finalized verified component selections and supplier references in the live BOM/specs
## Remaining follow-up work
These are still open design review items, but they are not yet committed design decisions:

1. Review battery connector alternatives.
2. Review how Extensions should be used mechanically, including whether interconnect choices for the
   Stator / Reflector / Extension chain should change.
3. Review whether the Encoder Board should split into separate Keyboard and Lightboard physical
   assemblies.
4. Review whether Extensions need additional servo circuitry to pass through notch rotations.
5. Add / review board-level coupons and PAS-oriented test coverage.
6. Rerun deep review agents after the next material design-doc change set.
