# Enigma-NG Session Plan

> Canonical state: `.copilot/plan.md` in the repository root (tracked in git).
> At the start of a new session, read this file, `.copilot/handoff.md`,
> `.copilot/agent-directives.md`, and the latest relevant checkpoint(s) in `.copilot/checkpoints/`.

---

## Overview

The repository is now in an updated repo-local handoff state after the latest documentation cleanup
phase.

The current active design docs now reflect:

- board-local ownership cleanup between Controller, Stator, and Settings Board
- removal of stale diagnostics / probe wording from active design specs and board layouts
- normalized board-layout heading numbering so `§` is reserved for cross-document references
- Reflector simplified-layout cleanup, including removal of the duplicate Data Plate label
- Stator Settings-board connector normalization from `J_CFG` to `J13`
- wiki-sync exclusion of `design/Datasheets`
- numeric component refdes normalization across active design docs and the consolidated BOM
- document metadata version headers reset to `v.0.1.0` because the project is still in design phase
- local PDF datasheets now have markdown companions under `design/Datasheets/`, with reviewed
  design-doc references retargeted from PDF links to the markdown versions
- Encoder Modules now target the common `EPM570T100I5N`, with encode-role debounce moved into CPLD
  logic and detailed logic requirements captured in `design/Software/CPLD_Logic/Encoder_Logic.md`
- the Encoder board split review is now closed around the `EPM570` / weak-pull-up /
  programming-defined-role baseline, with the rationale captured in the active design docs and
  `DEC-041`
- the Stator ↔ Encoder 20-pin contract now assigns **pin 8** to the HID-local active-low
  `ENC_ACTIVE_N` sideband, with `KBD_ENC` driving activity, `LBD_DEC` using it for blanking, and
  the Stator muxing / monitoring the selected activity source under `DEC-042`
- the Power Module battery-connector review now has a dedicated candidate-note document at
  `design/Electronics/Power_Module/Millitary_Battery_Connection_Option.md`, capturing the
  Glenair `807-216-00ZNU6-6DY` / Heilind / consignment-only option plus the preferred PM interposer
  and prototype-adapter-board direction pending connector confirmation
- the Glenair drawing PDF and 807 NW catalogue PDF now have a combined markdown extraction at
  `design/Datasheets/Glenair-807-216-datasheet.md`, linked from the Power Module battery option note
- the Glenair candidate's `Y` keying is now treated as confirmed standard battery keying for the
  connector family rather than as an open question
- the battery-connector review workstream is now closed at the candidate-document stage; the chosen
  connector still requires explicit confirmation during the final deep-dive and manual review before
  the design is treated as a complete Version 1 release
- the battery connector option note now also records the ODU AMC NP family as an alternate
  military-style connector lead pending sales feedback and further review
- the former direct Controller servo path has now been replaced in the active docs by a shared
  **Actuation Module (AM)** architecture: one AM on the Controller plus one on each Extension
- Extension-boundary carry is now documented as **mechanical within a 5-rotor group** and
  **locally regenerated across each Extension boundary** via active-low `ACTUATE_REQUEST`
- the Reflector / Extension service harness has been widened from **16-pin** to **20-pin**
  `BHR-20-VUA` so grouped `5V_MAIN` can reach Extension-local actuation hardware
- `design/Design_Log.md` now records this architecture as **DEC-043**

Recent locked work:

- `7829f8a` — `Normalize design document refdes`
- `1c2a505` — `Reset doc metadata versions`
- `4e36234` — `Close encoder split review`
- the current working tree carries the Power Module military-battery connector candidate note, the
  generated Glenair datasheet markdown, and the repo-local state sync for battery-review closeout
- **Pass 1 review cycle complete** — 42 findings resolved across all 11 boards + integration;
  all user decisions D-1 through D-7 actioned; new datasheets for Bourns SMBJ18A-Q and
  CTS 435F12012IET generated; two new markdown datasheets; all files lint-clean

---

## Current Open Workstreams

| ID | Status | Scope |
| ---- | -------- | ------- |
| `review-cycle-pass2` | **complete** | Pass 2 board + integration reviews complete; all findings F-42–F-66 resolved or deferred; audit trail appended to review-report.md; checkpoint 083 created; awaiting "Let's lock this in" |
| `bom-description-strip` | **complete** | All 11 board spec Component columns stripped; Consolidated_BOM.md 205 Description/Usage cells stripped + 4 new Rotor N=26 rows + Section 2 ROT-A/B→ROT-26/64 rename + 5 qty corrections; all_boards_bom.json 201 descriptions stripped + Rotor board field rename; all files lint-clean; checkpoint 090 written; awaiting "Let's lock this in" |
| `extension-mechanical-usage` | pending | Mechanical Extension usage is now aligned to local AM-based carry regeneration, but detailed switch / linkage geometry still needs later mechanical design |
| `coupon-testing-review` | pending | Add and review board-level coupons and PAS-oriented test coverage so production boards do not retain test-only hardware |
| `battery-connector-final-review` | pending | Re-confirm the chosen military battery connector details during the final deep-dive/manual review, especially the 6-pin contact assignment, `BATT_PRES_N` position, reserved contact behavior, cable selection, and interposer fit |
| `general-pin-mapping-schematic-capture` | pending | Create one shared schematic-capture workstream for unresolved exact package pin/pad assignments, AM service-header preservation, and bias-network details across the AM STM32, Stator mux U7, and the Encoder / Stator / Rotor CPLD packages, aligned with the planned KiCAD project and shared library setup |
| `rerun-deep-reviews` | pending | Run the final cross-discipline deep-review cycle only near Version 1 closeout, after the electrical, mechanical, and software design work is complete and each board has a full KiCAD project with production Gerbers exported |

---

## Board Design Status

| Board | Status |
| ------- | -------- |
| Power Module | In Review (Pass 2 fixes applied) |
| Stator | In Review (Pass 2 fixes applied) |
| Reflector | In Review (Pass 2 fixes applied) |
| Extension | In Review (Pass 2 fixes applied) |
| JDB | In Review (Pass 2 fixes applied) |
| Controller | In Review (Pass 2 fixes applied) |
| Encoder | In Review |
| Rotor | In Review (Pass 2 fixes applied) |
| Settings Board | In Review (Pass 2 fixes applied) |
| Actuation Module | In Review (Pass 2 fixes applied) |

---

## Next Session Start Point

Start the next clean session by reading:

1. `.copilot/plan.md`
2. `.copilot/handoff.md`
3. `.copilot/todo-list.md` — canonical deferred-work and open-action tracker for the project
4. `.copilot/checkpoints/099-bt-to-j-rename-todo-list-created.md` (latest checkpoint)

BOM restructure and RefDes cleanup (BOM phase) is complete pending commit authorisation.
Before next steps:

- Await user "Let's lock this in" to commit outstanding BOM / RefDes changes
- After commit: decide on next workstream (Pass 3 review, KiCAD library prep, Settings Board rename, etc.)

Read `.copilot/review-report.md` for the running audit trail.

---

## Critical Notes

> Standing operational rules (PRIMARY DIRECTIVE, data-lookup order, version-metadata policy,
> BOM authority, review suppression) are in `.copilot/agent-directives.md`. Read that file at
> session start.
>
> All deferred items, TBDs, and open certification actions are tracked in `.copilot/todo-list.md`.
> Do not re-derive them from a repo grep — update that file when new items are found or items are closed.

### Documentation policy

- Use the active `design/` documents as the source of truth for design state.
- `.copilot/` files are session/handoff artifacts only; they are not design documents.
- Do not change document `Version` metadata unless the user explicitly requests it.
- The current metadata baseline for active docs is `v.0.1.0`.
- Design-doc datasheet references should point at the reviewed markdown datasheets, while each
  generated datasheet markdown file keeps its own source-PDF link.
- Active Encoder baseline: `EPM570T100I5N`, digital debounce in CPLD logic, and role selected by
  programming rather than role-specific RC population.
- Active HID-side Encoder connector contract: pin 8 is `ENC_ACTIVE_N`, idle state is HIGH, and the
  signal is intentionally local to the keyboard / lightboard path rather than the wider cipher path.
- Active PM battery review state: Glenair `807-216-00ZNU6-6DY` is the documented candidate path,
  `Y` keying is confirmed standard battery keying, ODU AMC NP is logged as an alternate vendor lead,
  and the remaining connector questions must be rechecked during the final deep-dive and manual
  review before the design is marked complete V1.
- Active actuation baseline: use the shared **Actuation Module (AM)** on the Controller and on each
  Extension; CM5 GPIO 8 is now `ACTUATE_REQUEST_N`, the Controller no longer owns direct servo PWM,
  and the Reflector / Extension link is now a 20-pin `BHR-20-VUA` service harness so `5V_MAIN` can
  feed Extension-local actuation.
- The AM now reserves separate local **J5 SWD** and **J6 UART/bootloader** headers plus local **SW1
  NRST** and **SW2 BOOT0** tactile buttons so the final MCU can be programmed before first use without
  depending on the host board.
- AM layout visual now uses separate TOP (L1 enclosed/component side) and BOTTOM (L4 service/exterior
  side) views. AM decoupling now follows a reduced daughterboard pattern: STM32 local 100nF decouplers,
  4.7uF on `3V3_ENIG`, and 10uF on `5V_MAIN` near the servo path, rather than a full 5x bulk-entry bank.
- BOM audit: active board BOMs currently show no open `TBD` / empty-supplier placeholders apart from the
  intentional CM5 distributor-only row; the consolidated BOM AM section now includes explicit per-board
  and Rev A total counts for the current two-module design.
- The non-mechanical Extension notch pass-through review is now considered closed in repo-local state:
  the architectural answer is the shared AM baseline, and only later mechanical linkage/detail work remains.
- The AM firmware specification now lives under
  `design/Software/Actuation_Module/Design_Spec.md`; the electronics AM spec keeps only a brief
  cross-reference to that software document.
- Pass 2 electronics review complete. All findings F-42–F-66 resolved or deferred per user decisions.
  Awaiting user "Let's lock this in" confirmation before committing. Pass 3 will follow after the
  `Settings_Board` → `User_Settings_Module` rename commit.
- This does **not** close the repo-local `rerun-deep-reviews` workstream. That workstream remains the
  final pre-V1 cross-discipline review gate to be rerun only after electrical, mechanical, and software
  work are complete and each board has a full KiCAD project plus exported production Gerbers.
- A later shared schematic-capture workstream still needs to lock exact package pin/pad assignments for
  the AM STM32, Stator mux U7, and the Encoder / Stator / Rotor CPLD parts; treat that as one combined
  pin-mapping task so it can align with the planned KiCAD project and shared component-library setup.

### Refdes / naming state

- Controller internal connectors are now normalized to numeric refs (`J9`-`J15`) in the active docs.
- Stator Settings-board connector refdes is `J13`.
- Settings Board component refs are now numeric in the active docs and BOM (`J1`, `U1`-`U3`,
  `Q1`-`Q6`, `SW1`-`SW11`, `D1`-`D12`, `R1`-`R53`, `C1`-`C4`).

### Repo-local state rules

- `.copilot/` is tracked in git and must be kept in sync with meaningful design-state changes.
- Every checkpoint must update the checkpoint file, `.copilot/checkpoints/index.md`,
  `.copilot/plan.md`, and any related handoff content together.
