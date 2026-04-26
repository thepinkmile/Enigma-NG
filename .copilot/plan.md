# Enigma-NG Session Plan
> Canonical state: `.copilot/plan.md` in the repository root (tracked in git).
> At the start of a new session, read this file, `.copilot/handoff.md`, and the latest relevant
> checkpoint(s) in `.copilot/checkpoints/`.

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

Recent locked work:

- `7829f8a` — `Normalize design document refdes`
- `1c2a505` — `Reset doc metadata versions`
- `4e36234` — `Close encoder split review`
- the current working tree carries the Power Module military-battery connector candidate note, the
  generated Glenair datasheet markdown, and the repo-local state sync for battery-review closeout

---
## Current Open Workstreams
| ID | Status | Scope |
|----|--------|-------|
| `extension-mechanical-usage` | pending | Review how Extensions should be used mechanically, including whether interconnect choices for the Stator / Reflector / Extension chain should change |
| `extension-notch-pass-through` | pending | Review whether Extensions need additional servo circuitry to pass through notch rotations |
| `coupon-testing-review` | pending | Add and review board-level coupons and PAS-oriented test coverage so production boards do not retain test-only hardware |
| `rerun-deep-reviews` | pending | Rerun deep review agents only after the next material design-doc change set |

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
3. `.copilot/checkpoints/064-battery-connector-candidate.md`
4. `.copilot/checkpoints/063-encoder-active-sideband.md`
5. `.copilot/checkpoints/062-encoder-split-review-closed.md`
6. `.copilot/checkpoints/061-encoder-epm570-and-logic-spec.md`

Then proceed into the next design-review task from the active `design/` docs rather than treating
`.copilot/` content as design truth.

---
## Critical Notes
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
  `Y` keying is confirmed standard battery keying, and the remaining connector questions must be
  rechecked during the final deep-dive and manual review before the design is marked complete V1.

### Refdes / naming state
- Controller internal connectors are now normalized to numeric refs (`J9`-`J15`) in the active docs.
- Stator Settings-board connector refdes is `J13`.
- Settings Board component refs are now numeric in the active docs and BOM (`J1`, `U1`-`U3`,
  `Q1`-`Q6`, `SW1`-`SW11`, `D1`-`D12`, `R1`-`R53`, `C1`-`C4`).

### Component / MPN discipline
- Never change a component MPN without a matching local datasheet review in `design/Datasheets/`.
- Never modify confirmed supplier part numbers without checking with the user first.
- Do not treat package-family differences as blocking while the project remains pre-schematic /
  pre-layout unless the user explicitly says packaging now matters.

### Repo-local state rules
- `.copilot/` is tracked in git and must be kept in sync with meaningful design-state changes.
- Every checkpoint must update the checkpoint file, `.copilot/checkpoints/index.md`,
  `.copilot/plan.md`, and any related handoff content together.
