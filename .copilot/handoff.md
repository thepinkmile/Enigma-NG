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

## 2026-04-19 audit result

The old component re-verification and session working notes were audited and removed because their
design-bearing content is already captured in the live docs above.

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

1. Review how Extensions should be used mechanically, including whether interconnect choices for the
   Stator / Reflector / Extension chain should change.
2. Review whether the Encoder Board should split into separate Keyboard and Lightboard physical
   assemblies.
3. Review whether Extensions need additional servo circuitry to pass through notch rotations.
