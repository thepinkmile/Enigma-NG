# Enigma-NG Session Plan

> Canonical state: `.copilot/plan.md` in the repository root (tracked in git).
> At the start of a new session, read `.copilot/SESSION_START.md` and follow its steps,
> then this file and `.copilot/handoff.md`, then the latest relevant checkpoint(s) in `.copilot/checkpoints/`.

---

## Current Status (as of 2026-07-05 — design discussion merge in progress)

The design discussion merge is now underway. The Cypher Board and Stack-Input Board design files
have been created. The merge todo hierarchy is established and tracked.

Latest checkpoint: `.copilot/checkpoints/177-cypher-system-board-design-cypher-stack-input-created.md`

### Completed merge sub-tasks

| Sub-task | Result |
| --- | --- |
| `merge-grs-6layer-stackup` | GRS §2.3.4 added (PCBWay 6-layer; Cypher Board) |
| `merge-create-cypher-board` | `design/Electronics/Cypher/` created (Design_Spec + Board_Layout) |
| `merge-create-stack-input` | `design/Electronics/Stack-Input/` created (Design_Spec + Board_Layout) |

### Current merge focus

**Next sub-task: `merge-create-stack-output`** — output-side board of the Rotor Mini-Stack.
Source: EXT output-side circuits. Use FR-EXT-xx/DR-EXT-xx IDs where applicable; new
FR-SOUT-xx/DR-SOUT-xx for Stack-Output-specific requirements.

After Stack-Output:
- `merge-create-stack-blanking` — termination board for last mini-stack
- `merge-create-stack-interposer` — passive interposer between Stack-Output and Stack-Input
- `merge-create-cypher-input` / `merge-create-cypher-output` — keyboard and lightboard panels
- `merge-update-ctl-board` — blocked by `merge-ctl-dock-usb-allocation` (USB D+/D- pin alloc)
- `merge-update-top-level-docs` → `merge-remove-old-boards` → review chain

## Board Design Status

| Board | Status | Notes |
|-------|--------|-------|
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
|-------|---------|
| Cypher Board stackup | 6-layer PCBWay (GRS §2.3.4); JLCPCB not suitable |
| CFG_ROUTE table | 13 valid configurations 0–12; 13–15 reserved; rules embedded in Cypher Design_Spec |
| Actuation | Solenoid replaces servo; dual homing switches (retracted + extended) |
| ACTUATE_REQUEST_N | Separate signal from ENC_ACTIVE_N on stacking connectors |
| Stack-Input J4 power | J4 carries power to ROT 1; no ground-loop restriction (single J1 entry) |

## Library Status

| File | Status |
|------|--------|
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
Then read checkpoint 177 and resume with `merge-create-stack-output`.
