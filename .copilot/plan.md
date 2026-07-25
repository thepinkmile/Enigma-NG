# Enigma-NG Session Plan

> Canonical state: `.copilot/plan.md` in the repository root (tracked in git).
> At the start of a new session, read `.copilot/SESSION_START.md` and follow its steps,
> then this file and `.copilot/handoff.md`, then the latest relevant checkpoint(s) in `.copilot/checkpoints/`.

---

## Current Status (as of 2026-07-25 — design discussion merge in progress)

The design discussion merge is ongoing. The Stack-Interposer Board design files have been created,
connector decisions locked (TMMH-115-01-L-D-ES for J1/J2; SQT-115-01-L-D-RA for J6 on both
Stack-Output and Stack-Input), and the KiCAD library has been updated with all required components.
A front-elevation diagram page (Mini-Stack Front View) has been added to the draw.io diagram set.

Latest checkpoint: `.copilot/checkpoints/179-stack-interposer-board-design-complete.md`

### Completed merge sub-tasks

| Sub-task | Result |
| --- | --- |
| `merge-grs-6layer-stackup` | GRS §2.3.4 added (PCBWay 6-layer; Cypher Board) |
| `merge-create-cypher-board` | `design/Electronics/Cypher/` created (Design_Spec + Board_Layout) |
| `merge-create-stack-input` | `design/Electronics/Stack-Input/` created (Design_Spec + Board_Layout) |
| `merge-create-stack-output` | `design/Electronics/Stack-Output/` created (Design_Spec + Board_Layout) |
| `merge-create-stack-blanking` | `design/Electronics/Stack-Blanking/` created (Design_Spec + Board_Layout) |
| `merge-create-stack-interposer` | `design/Electronics/Stack-Interposer/` created (Design_Spec + Board_Layout) |

### Current merge focus

**Next sub-task: `merge-create-cypher-input`** — keyboard input panel board.
ENC module BtB interface (DF40C family), mechanical keyboard switches (MX2A-71NB + PG151101S11
hot-swap sockets), LED circuit (APFA2507Y2G2C-C2 with 555 PWM brightness, P-MOSFET switch).
See `.copilot/discussions/cypher-system-discussion/extension-mechanical-usage.md` Entries 16–17.

After Cypher-Input:

- `merge-create-cypher-output` — lightboard output panel
- `merge-ctl-dock-usb-allocation` → `merge-update-ctl-board`
- `merge-cypher-board-j3j6-pinouts` — full 50-contact allocation for J3/J4/J5/J6

## Board Design Status

| Board | Status | Notes |
| --- | --- | --- |
| Power Module (PM) | In Review | All P10 findings closed |
| Controller Board (CTL) | In Review | T1 decision complete (DEC-067); all P10 closed; JM/AM removal pending (`merge-update-ctl-board`) |
| Stator | **Retiring** | Circuits migrated to Cypher Board |
| Rotor (26-char) | In Review | All P10 findings closed |
| Rotor (64-char) | In Review | All P10 findings closed |
| Reflector | **Retiring** | Circuits migrated to Cypher Board |
| Extension Board (EXT) | **Retiring** | Circuits split into Stack-Input + Stack-Output |
| JTAG Module (JM) | **Retiring** | Circuits migrated to Cypher Board |
| User Settings Module (USM) | In Review | All P10 findings closed |
| Encoder (ENC) | In Review | Module redesign pending |
| Actuation Module (AM) | **Retiring** | Circuits migrated native to Stack-Input Board |
| **Cypher Board** | **Draft** | Created 2026-07-05; consolidates STA + REF + JM |
| **Stack-Input Board** | **Draft** | Created 2026-07-05; EXT input-side + native solenoid AM |
| **Stack-Output Board** | **Draft** | Created 2026-07-12; J6 updated to SQT-115-01-L-D-RA (from 2BHR-30-VUA); DEC-085 |
| **Stack-Interposer Board** | **Draft** | Created 2026-07-25; TMMH-115-01-L-D-ES J1/J2; SQT-115-01-L-D-RA mating; mirror-corrected routing note |
| **Stack-Blanking Board** | **Draft** | Created 2026-07-12; passive termination; 5× termination resistors |

## Open Pass-10 Findings (0 remaining — all closed ✅)

All 91 Pass-10 findings are resolved. REF-P10-05 closed: 2BHR-30-VUA uses KiCAD built-in `Connector_IDC:IDC-Header_2x15_P2.54mm_Vertical`.

## Open Workstreams

### Immediate (resume here)

1. **Design Discussion Merge** (`design-discussion-merge` — in_progress)
   - `merge-create-stack-output` — **next task** (source: EXT output-side circuits)
   - `merge-create-stack-blanking`, `merge-create-stack-interposer`
   - `merge-create-cypher-input`, `merge-create-cypher-output`
   - `merge-ctl-dock-usb-allocation` → `merge-update-ctl-board`
   - Full sequence tracked in `.copilot/todos/design-discussion-merge.md`
2. **Pending pinout work** (`merge-cypher-board-j3j6-pinouts`)
   - Full 50-contact allocation for Cypher Board J3/J4/J5/J6 stacking connectors

### Deferred / Blocked

- `battery-connector-final-review` — blocked: awaiting supplier response
- `jdb-ft232h-3v3-vregin` — blocked (v2.0)
- `display-addon-board`, `cpld-production-replacement`, `display-aperture` — blocked (v2.0)
- `ctl-t1-coilcraft-v2-review` — blocked (v2.0)

## Key Design Decisions (recent — 2026-07-05 session)

| Decision | Summary |
| --- | --- |
| Cypher Board stackup | 6-layer PCBWay (GRS §2.3.4); JLCPCB not suitable |
| CFG_ROUTE table | 13 valid configurations 0–12; 13–15 reserved; rules embedded in Cypher Design_Spec |
| Actuation | Solenoid replaces servo; dual homing switches (retracted + extended) |
| ACTUATE_REQUEST_N | Separate signal from ENC_ACTIVE_N on stacking connectors |
| Stack-Input J4 power | J4 carries power to ROT 1; no ground-loop restriction (single J1 entry) |

## Library Status

| File | Status |
| --- | --- |
| `SamacSys_Parts.kicad_sym` | CL31B106KBK6PJE + 12 Samtec QSS/QTS symbols present ✅ |
| `SamacSys_Parts.lib` / `.dcm` | CL31B106KBK6PJE present; 12 Samtec symbols appended to `.lib` ✅ |
| `SamacSys_Parts.pretty/` | CL31B106KBK6PJE + 12 Samtec QSS/QTS footprints present ✅ |
| `SamacSys_Parts.mod` | CL31B106KBK6PJE + 12 Samtec QSS/QTS `$MODULE` backports present ✅ |
| `SamacSys_Parts.3dshapes/` | CL31B106KBK6PJE + 12 Samtec STEP models present ✅ |
| `3D_Models/` | CL31B106KBK6PJE + 12 Samtec STEP models present ✅ |
| `src/Electronics/Library/temp/` | Empty — all ZIPs and temp assets cleaned up ✅ |

## Critical Standing Rules

- **NEVER commit** without "Let's lock this in" or "Save state" from user in live session
- **Design Log restructured** — `design/Design_Log/` (per-DEC files); next entry = **DEC-084** as `DEC-084_{title}.md` + `index.md` row; NEVER modify existing DEC files; NEVER create as `design/Design_Log.md`
- **PRIMARY DIRECTIVE**: Never modify any MPN/supplier part numbers without explicit user confirmation
- **Last Updated** dates must be updated on every content change; **Version** is user-only
- Move unwanted files to `.recycle-bin/`; never delete permanently
- **OCTONARY**: Seed session DB from `todos/todos.sql` + `todos/deps.sql` as MANDATORY FIRST ACTION
- **review-clean-passes-gate**: when adding a new `review-pass-x`, add it as a dep on the gate
- **Board_Layout.md files are visualisation-only** — no design narrative or spec prose
- **BOM Notes are procurement-only** — no function descriptions, signal names, or design rationale
- **BOM authority**: `Consolidated_BOM.md` = system; board `Design_Spec.md` = board (per DEC-083)

## Next Session Start Point

Follow `.copilot/SESSION_START.md` — canonical bootstrap order.
Then read checkpoint 179 and resume with `merge-create-cypher-input`.
