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

## 2026-04-26 session result
The latest repository state now includes the Encoder CPLD consolidation and logic-spec capture in
addition to the earlier documentation cleanup and datasheet migration work.

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
- local datasheet PDFs under `design/Datasheets/` now have generated markdown companions, those
  markdown datasheets were reviewed in category batches, and design-doc references were migrated
  from `.pdf` links to the corresponding `.md` datasheets
- Encoder Modules now use the common `EPM570T100I5N` part, external per-line debounce RC networks
  were retired from the active design, and role is selected by programming rather than by
  role-specific PCB population
- a new logic-spec document now exists at `design/Software/CPLD_Logic/Encoder_Logic.md` covering
  sampled 64-bit debounce, 64-to-6 encode, and 6-to-64 decode requirements for later VHDL work
- `design/Design_Log.md` now records this as **DEC-041**, which supersedes active Encoder-board
  assumptions around `EPM240T100I5N` and external RC debounce
- the active Encoder baseline now also explicitly records:
  - MAX II **weak pull-up** as the intended input-bias baseline for encode-role pins
  - internal/UFM oscillator use as the preferred debounce timebase
  - 64-character keyboard mapping as the primary `KBD_ENC` definition, with 26-character and custom
    educational keyboard mappings acknowledged as variant/follow-on work
  - generic `ENCODER MODULE` board-identification silkscreen only; role-specific silkscreen labels
    are no longer required
- the active HID connector contract now also records:
  - generic Encoder connector **pin 8 = `ENC_ACTIVE_N`**
  - `KBD_ENC` drives `ENC_ACTIVE_N` LOW only while a debounced keypress is active
  - the Stator source-select path switches both `ENC_DATA[5:0]` and the activity sideband so the
    physical keyboard and `CM5_KEY_DATA[5:0]` / `CM5_KEY_ACTIVE_N` stay aligned
  - `LBD_DEC` uses `ENC_ACTIVE_N` to blank all outputs when the selected keyboard source is idle
  - `design/Design_Log.md` records this connector and HID-blanking update as **DEC-042**
- the Power Module battery-connector review now has a dedicated candidate-note document,
  `design/Electronics/Power_Module/Millitary_Battery_Connection_Option.md`, which captures:
  - Glenair candidate `807-216-00ZNU6-6DY`
  - Heilind-only sourcing with JLCPCB **consignment-only** assembly expectation
  - the provisional 6-pin vs 5-signal mapping caution
  - confirmed `Y` keying as the standard battery keying intended to prevent mating with data-only
    ports on standard in-service devices such as STAR-PAN and STAR-PAN NG
  - the preferred PM-side **interposer / daughterboard** integration approach
  - a separate prototype-only adapter board direction using the same female receptacle
  - a linked combined markdown datasheet extraction at `design/Datasheets/Glenair-807-216-datasheet.md`
    generated from the Glenair drawing PDF and the 807 NW catalogue PDF
  - closure of the battery-connector review workstream at the candidate-document stage, with the
    remaining connector specifics to be rechecked during the final deep-dive and manual review
    before the design is considered a complete Version 1 release

## Documentation policy reminders
- Do not update document `Version` metadata unless the user explicitly requests it.
- Do not infer version bumps from the size or perceived significance of a change.
- Keep `.copilot/` synchronized with meaningful design-state changes, but treat it as handoff
  material rather than design truth.
- Connector/mechanical-drawing datasheet markdown can remain lightweight for now; fuller detail can
  wait until initial KiCAD library generation.
- Design docs should reference the markdown datasheets, but the generated datasheet markdown files
  should continue to link back to their source PDFs.

## Remaining follow-up work
These are still open design review items, but they are not yet committed design decisions:

1. Review how Extensions should be used mechanically, including whether interconnect choices for the
   Stator / Reflector / Extension chain should change.
2. Review whether Extensions need additional servo circuitry to pass through notch rotations.
3. Add and review board-level coupons and PAS-oriented test coverage.
4. Rerun deep review agents after the next material design-doc change set.
5. During the final deep-dive and manual review before declaring Version 1 complete, re-confirm the
   chosen military battery connector details, especially the remaining 6-pin contact assignment,
   `BATT_PRES_N` position, reserved/unused contact behaviour, cable selection, and interposer fit.
