# Checkpoint 177: Cypher System Board Design — Cypher Board + Stack-Input Board Created

**Date:** 2026-07-05
**Status:** Complete
**Scope:** Design discussion merge into main design — first three sub-tasks complete

## Summary

Full session working on the design discussion merge (`design-discussion-merge`). Created the
Cypher Board and Stack-Input Board design files, added GRS §2.3.4 for the PCBWay 6-layer
stackup, established the merge todo hierarchy, and relocated the system layout diagram.

## Work Completed

### Todo Hierarchy — Design Discussion Merge

Created `design-discussion-merge` parent todo and 16 sub-tasks covering every stage of the
Cypher system architectural merge. Persisted to `todos/todos.sql`, `todos/deps.sql`,
`todos/index.md`, and 17 per-todo detail `.md` files.

**Sub-tasks completed this session:**

| Todo | Status |
| --- | --- |
| `merge-create-cypher-board` | ✅ done |
| `merge-grs-6layer-stackup` | ✅ done |
| `merge-create-stack-input` | ✅ done |

### Diagrams Folder

- Created `design/Diagrams/` and `design/Diagrams/renders/`
- Copied `extension-mechanical-usage-diagram.drawio` → `design/Diagrams/cypher-system-layout.drawio`
- Copied PNG renders to `design/Diagrams/renders/`

### GRS §2.3.4 — PCBWay Six-Layer Stackup (Cypher Board)

Added `design/Standards/Global_Routing_Spec.md §2.3.4` defining the 6-layer PCBWay stackup
used by the Cypher Board. Layer mapping: L1 front-face signal → L2 GND → L3 CI signal →
L4 power → L5 GND → L6 back-face signal. CI trace widths TBD with PCBWay impedance tool.

### Cypher Board

New files: `design/Electronics/Cypher/Design_Spec.md` and `Board_Layout.md`

- **Consolidates:** Stator (STA) + Reflector (REF) + JTAG Module (JM) circuits
- **Enigma responsibilities:** Stator + Reflector roles in one 6-layer PCBWay board
- **FR/DR IDs:** FR-STA-xx, FR-REF-xx, FR-CYP-xx throughout
- **CFG_ROUTE plugboard routing:** 13 valid configurations (0–12); indices 13–15 reserved.
  Config 0 = None:None; Config 1 = Pre-Rotor 1 : Post-Rotor 1 Return (classic Enigma);
  Config 2 = At Reflector : None (later Enigma variants). Rules embedded in spec.
- **Connector ownership:** J3/J4 QSS-025 owned here; J5/J6 QTS-025 Entry 19 pin map defined
  in Board_Layout §4
- **Spade tabs:** Keystone 1285-ST, 64 × 4 = 256 total; RefDes J20+
- **MCP23017 register maps** (U6/U7/U8) fully inlined; no cross-references to retiring boards
- **FT232H circuit** fully inlined (no cross-reference to retiring JM spec)

### Stack-Input Board

New files: `design/Electronics/Stack-Input/Design_Spec.md` and `Board_Layout.md`

- **Circuit responsibilities:** Mini-Stack Cypher Input (EXT input-side FR/DR-EXT-xx) + native
  Solenoid Actuation (FR/DR-SIN-xx)
- **Key design decisions:**
  - ACTUATE_REQUEST_N ≠ ENC_ACTIVE_N — separate stacking connector pins
  - Cypher Board ties ACTUATE_REQUEST_N to GND for mini-stack 1; subsequent mini-stacks receive
    it from last ROT carry mechanism
  - Solenoid replaces servo; dual homing switches: ACTUATION_HOME_N (retracted) +
    ACTUATION_EXTENDED_N (fully extended); J8 pinout reflects this
  - J4 carries power to ROT 1 (no ground-loop issue; single power entry on J1)
  - AM circuits native on-board (no dock connector); J7-J10 pinouts owned by Board_Layout §5-§8
- **Connectors:** J1 QTS-025 male R/A (front); J2 QSS-025 female R/A (rear); J3/J4/J5 ERF8
  sockets to ROT 1; J6 SQT-115 interposer link
- **Added R6** (10kΩ pull-up for ACTUATION_EXTENDED_N) to BOM

### Markdownlint Cleanup

- Cypher Board spec: removed unnecessary `<!-- markdownlint-disable MD013 MD055 MD056 -->` —
  MD013 tables already handled by repo config; MD055/MD056 don't fire on well-formed tables
- GRS: fixed pre-existing MD013 line-length violation in §6

## Files Created / Modified

**New:**
- `design/Diagrams/cypher-system-layout.drawio`
- `design/Diagrams/renders/01-Rotor-Mini-Stack-Architecture.png`
- `design/Diagrams/renders/02-Mini-Stack-Vertical-Stack-Portrait.png`
- `design/Electronics/Cypher/Design_Spec.md`
- `design/Electronics/Cypher/Board_Layout.md`
- `design/Electronics/Stack-Input/Design_Spec.md`
- `design/Electronics/Stack-Input/Board_Layout.md`
- `.copilot/todos/design-discussion-merge.md` + 16 other merge todo detail files

**Modified:**
- `design/Standards/Global_Routing_Spec.md` (added §2.3.4; fixed MD013)
- `.copilot/todos/todos.sql` (17 new todos)
- `.copilot/todos/deps.sql` (36 new deps)
- `.copilot/todos/index.md` (new rows + status updates)
- `.copilot/plan.md`
- `.copilot/handoff.md`
- `.copilot/checkpoints/index.md`

## Current Merge Sub-Task Status

| Sub-task | Status |
| --- | --- |
| `merge-grs-6layer-stackup` | ✅ done |
| `merge-create-cypher-board` | ✅ done |
| `merge-create-stack-input` | ✅ done |
| `merge-cypher-board-j3j6-pinouts` | pending |
| `merge-ctl-dock-usb-allocation` | pending |
| `merge-create-stack-output` | **pending — next task** |
| `merge-create-stack-blanking` | pending |
| `merge-create-stack-interposer` | pending |
| `merge-create-cypher-input` | pending |
| `merge-create-cypher-output` | pending |
| `merge-update-ctl-board` | pending (blocked by `merge-ctl-dock-usb-allocation`) |
| `merge-update-top-level-docs` | pending |
| `merge-remove-old-boards` | pending |
| `merge-consistency-review` | pending |
| `merge-missing-components` | pending |
| `merge-final-review` | pending |

## Next Start Hint

**Resume with: `merge-create-stack-output`** — output-side board of the Rotor Mini-Stack.
Source: EXT output-side circuits. Front QTS-025 male (J3 in the mini-stack signal map), rear
QSS-025 female, ERF8 input sockets from last ROT board, interposer link connector.
FR/DR-EXT-xx IDs where applicable; new FR/DR-SOUT-xx for Stack-Output-specific requirements.
