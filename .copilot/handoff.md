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

The latest repository state now includes the Encoder CPLD consolidation and logic-spec capture,
the battery-connector candidate note, and the new shared Actuation Module architecture for
Controller + Extension actuation.

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
  - ODU AMC NP as an alternate military circular-connector lead pending sales-team feedback
  - a newly noted ODU advantage: panel-mount connector plus wiring-harness availability may avoid a
    custom PM interposer and may also simplify the prototype battery-pack / adapter build
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
- the old direct Controller-local servo model has now been retired from the active docs in favour
  of a shared **Actuation Module (AM)** service board:
  - one AM is hosted on the Controller for the main depression-bar actuation path
  - each Extension hosts one AM to regenerate group-boundary carry into the next 5-rotor group
  - the host/AM contract is intentionally minimal: grouped `5V_MAIN`, `3V3_ENIG`, `GND`, and one
    active-low `ACTUATE_REQUEST`
  - the AM owns local servo homing, one-shot request capture, servo PWM generation, and local
    `PWR` / `HOMED` / `ACT` LEDs
- the AM now reserves separate local **J5 SWD** and **J6 UART/bootloader** service headers plus local
  **SW1 NRST** and **SW2 BOOT0** tactile buttons so the selected MCU can be programmed before first use
  with either path
- the AM board-layout note now uses separate TOP / BOTTOM views to make the fitted-side versus
  manual-fit-side intent explicit
- the AM now documents a reduced daughterboard decoupling scheme rather than a full 5x bulk-entry bank:
  C2-C3 = local STM32 100nF decouplers, C4 = 4.7uF on `3V3_ENIG`, C5 = 10uF on `5V_MAIN` near the
  servo power path; this is derived from the JDB daughterboard precedent but strengthened for the servo load
- BOM audit pass: active board design-spec BOMs currently show no open `TBD` / empty-supplier placeholder
  rows apart from the intentional CM5 distributor-only entry, and the consolidated AM section now carries
  explicit per-board and Rev A total counts for the current two-module design
- the additive senior-electronics deep-review loop for BOM/support-part completeness and connector
  consistency is now complete for the current design-doc set:
  - `.copilot/review-report.md` contains the full pass-by-pass audit through Pass 17
  - Pass 16 and Pass 17 both completed **clean** by the agreed review definition
  - the resulting design/BOM fixes remain intentionally uncommitted in the working tree
  - only the previously known deferred schematic-capture and owner-selected selections remain open
  - this does **not** close the repo-local `rerun-deep-reviews` workstream; that remains the final
    pre-V1 cross-discipline review gate after electrical, mechanical, and software work are complete and
    each board has a full KiCAD project with exported production Gerbers

## 2025-05 size-down pass (checkpoint 073)

Size-down pass from the electronics deep-review cycle is fully implemented and committed (`9927b8d`).

Key changes:

- All 1206 50V 10µF bulk caps (CL31B106KBHNNNE) replaced with 0805 25V equivalents
  (Samsung CL21B106KAYQNNE) across AM, CTL, ENC, EXT, REF, ROT, STA
  — voltage margins: 7.6× on 3V3\_ENIG, 5.0× on 5V\_MAIN (both exceed 2× mandatory derating)
- Stator 0603 10kΩ resistors (R2–R41, ERJ-3EKF1002V) consolidated to 0402 ERJ-2RKF1002X
- Stator 0603 75Ω resistors (R7–R38, ERJ-3EKF75R0V) consolidated to 0402 ERJ-2RKF75R0X;
  ERJ-3EKF75R0V eliminated from system entirely
- Consolidated BOM fully updated with corrected counts and supplier codes
- `design/Standards/Global_Routing_Spec.md` §3 updated to 25V/0805 as standard bulk cap rule
  with voltage margin notes
- Samsung CL21B106KAYQNNE markdown datasheet generated and committed:
  `design/Datasheets/Samsung-1276_CL21B1-datasheet.md`
- D1/D2/D3 fixes committed (`da3df20`): AM GND ring retained (no isolation), ESD removed from
  all internal connectors, switch debounce time set to 10ms

## 2025-05 datasheet hygiene pass (checkpoint 074)

Datasheet coverage audit and hygiene pass completed and committed.

Key changes:

- `design/Electronics/Consolidated_BOM.md` §11 Samtec links fixed:
  `samtec-erm8-erf8-datasheet.md` (combined, non-existent) replaced with
  `erf8-xxx-xx.x-xxx-dv-xxxx-xx-mkt-datasheet.md` and
  `erm8-xxx-xx.x-xxx-dv-xxxx-xx-mkt-datasheet.md` (both confirmed present)
- BOM §11: 5 new entries added: Samsung CL21B106KAYQNNE, KAM05CR71A105KH,
  CC1206KKX7R8BB106, TDK CGA9N3X7R1E476M230KB, TDK CGA6P3X7R1H475K250AD
- `design/Datasheets/_generated_markdown_inventory.json`: 7 new `pdf_to_markdown` entries
- Orphaned `Kyocera-AVX-KGP-datasheet.{md,pdf}` deleted (KGP stack cap, zero BOM references)
- `.copilot/checkpoints/057-size-down-pass-complete.md` fully removed from git index

## 2025-05 electronics deep-review cycle complete (checkpoint 075)

All accumulated electronics deep-review findings committed as one coherent set (`41b6d07`).

Key changes:

- **Power Module:** ROTOR\_EN→ROTOR\_EN\_N rename; TPS25751/PD topology note added;
  C53–C57 internal-reg bypass caps added (LTC3350 INTVCC/DRVCC/VCC2P5,
  STUSB4500 VREG\_1V2/VREG\_2V7); BOM note updated to C21–C57;
  Consolidated BOM: PM 1µF 0805 count 3→7, PM 10µF 1206 count 1→2
- **Controller:** U5/U6 GbE ESD arrays (TPD4E05U06QDQARQ1, pair AB + pair CD)
  added — same part as U4, placed before J8 magnetics; resolves CTL-M2
- **Rotor:** Section 6 Thermal & ESD added; DEC-042 unshielded variant confirmed;
  ROT-04 header pin descriptions corrected
- **Settings Board:** R81–R98 (18× 1kΩ gate pull-downs), C5/C6 (2× 10µF 0805) added
- **Stator:** J5–J12 connector name fixes applied
- **Extension:** FR-EXT-06 ACTUATE\_REQUEST pull-up corrected to 3V3\_ENIG
- **Design Log:** DEC-045 (Samtec ERM8/ERF8 ESD for external rotor connectors)
- **Standards:** Global\_Routing\_Spec §9 hot-swap ESD exception clause added
- **Consolidated BOM:** CL21B106KAYQNNE SBD +2; ERJ-2RKF1003X SBD +18;
  330Ω JLCPCB part corrected to C278592; TPD4E05U06 note updated with U4/U5/U6 roles

Open items not yet actioned:

- **CTL-H1:** explicitly deferred by user
- **Rotor ESD TVS (PRTR5V0U10AZ):** pending final sourcing; Section 6 placeholder retained
- **Category C:** battery connector sourcing (awaiting supplier email responses)

## Next return summary

When resuming, read `.copilot/checkpoints/075-deep-review-cycle-complete-comm.md` for current state.

Next checkpoint will be **076**.


## Documentation policy reminders

- Do not update document `Version` metadata unless the user explicitly requests it.
- Do not infer version bumps from the size or perceived significance of a change.
- Keep `.copilot/` synchronized with meaningful design-state changes, but treat it as handoff
  material rather than design truth.
- Connector/mechanical-drawing datasheet markdown can remain lightweight for now; fuller detail can
  wait until initial KiCAD library generation.
- Design docs should reference the markdown datasheets, but the generated datasheet markdown files
  should continue to link back to their source PDFs.
- Part-detail lookup order is: **reviewed markdown datasheet first**, then the preserved local **PDF
  datasheet**, and only then an **online source** if the local repository material is missing or
  insufficient.
- Repo-local helper scripts that should persist across sessions belong under `.copilot/agent-scripts/`;
  the datasheet generator now lives there and `_generated_markdown_inventory.json` should be treated as
  a full datasheet index, not a partial single-run artifact.

## Remaining follow-up work

These are still open design review items, but they are not yet committed design decisions:

1. Review how Extensions should be used mechanically, including whether interconnect choices for the
   Stator / Reflector / Extension chain should change.
2. Add and review board-level coupons and PAS-oriented test coverage.
3. During later schematic capture, treat the remaining exact package pin/pad assignment work as one
   combined pin-mapping task across the AM STM32, Stator mux U7, and the Encoder / Stator / Rotor CPLD
   parts, aligned with the planned KiCAD project and shared component-library setup; this same
   workstream also preserves the chosen external `J5` / `J6` pinouts, the local `SW1` / `SW2`
   tactile pair on `NRST` / `BOOT0`, and the agreed logical signal roles while locking the exact
   STM32 pad assignment and default `BOOT0` bias network behind them.
4. During the final deep-dive and manual review before declaring Version 1 complete, re-confirm the
   chosen military battery connector details, especially the remaining 6-pin contact assignment,
   `BATT_PRES_N` position, reserved/unused contact behaviour, cable selection, and interposer fit.
