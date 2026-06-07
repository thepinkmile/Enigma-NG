# Enigma-NG Session Plan

> Canonical state: `.copilot/plan.md` in the repository root (tracked in git).
> At the start of a new session, read `.copilot/SESSION_START.md` and follow its steps,
> then this file and `.copilot/handoff.md`, then the latest relevant checkpoint(s) in `.copilot/checkpoints/`.

---

## Current Status (as of 2026-06-07 — unified Cypher/Extension design-spec discussion created)

The new consolidated point-in-time design modification file is now in place:

- `.copilot/discussions/cypher-extension-unified-discussion.md`

It consolidates architecture, grounding model, interconnect mappings, signal-flow narratives, component baseline, and active-design change tracking from both prior discussions. The immediate activity is now completeness review of this unified file before any implementation work.

Latest checkpoint: `.copilot/checkpoints/174-unified-cypher-extension-spec-created-awaiting-completeness-review.md`

### Current review focus

1. Validate the unified file is fully self-contained and does not omit detail from prior additive discussions.
2. Capture any missing details directly in the unified file.
3. After completeness sign-off, use the unified file as the single implementation baseline.

## Board Design Status

| Board | Status | Notes |
|-------|--------|-------|
| Power Module (PM) | In Review | All P10 findings closed |
| Controller Board (CTL) | In Review | T1 decision complete (DEC-067); all P10 closed |
| Stator | In Review | All P10 findings closed |
| Rotor (26-char) | In Review | All P10 findings closed |
| Rotor (64-char) | In Review | All P10 findings closed |
| Reflector | In Review | All P10 findings closed |
| Extension Board (EXT) | In Review | All P10 findings closed |
| JTAG Module (JM) | In Review | All P10 findings closed |
| User Settings Module (USM) | In Review | All P10 findings closed |
| Encoder (ENC) | In Review | All P10 findings closed |
| Actuation Module (AM) | In Review | All P10 findings closed |

## Open Pass-10 Findings (0 remaining — all closed ✅)

All 91 Pass-10 findings are resolved. REF-P10-05 closed: 2BHR-30-VUA uses KiCAD built-in `Connector_IDC:IDC-Header_2x15_P2.54mm_Vertical`.

## Open Workstreams

### Immediate (resume here)

1. **Pass-10 complete ✅** — 91 resolved, 0 partial = 91 total
2. **Review Pass 11** (`review-pass-11`) — blocked by `copilot-dir-restructure` (pending); `data-plate-standardisation` ✅ complete; `design-log-restructure` ✅ complete
   - Once pass 11 and pass 12 are both clean → `review-clean-passes-gate` can be closed
3. **Unified Cypher/Extension specification review (discussion-only, no implementation yet)**
   - Unified file created: `.copilot/discussions/cypher-extension-unified-discussion.md`
   - Pending: user-led completeness pass to identify any missing historical details
   - No design-file changes until unified file content is accepted as complete

### Deferred / Blocked

- `data-plate-standardisation` ✅ DONE (2026-05-22)
- `design-log-restructure` ✅ DONE (2026-05-22)
- `battery-connector-final-review` — blocked: awaiting supplier response
- `jdb-ft232h-3v3-vregin` — blocked (v2.0), pending FT232H Rev C availability
- `display-addon-board`, `cpld-production-replacement`, `display-aperture` — blocked (v2.0)
- `ctl-t1-coilcraft-v2-review` — blocked (v2.0)

## Key Design Decisions (recent)

| Entry | Summary |
|-------|---------|
| DEC-076 | TPS25751 I2C address conflict resolution (I2C1 0x20; EEPROM U18 at 0x50 on isolated I2Cc) |
| DEC-077 | CPLD_RESET_N renamed SYS_RESET_N across all boards |
| DEC-078 | Trace-width convention: GRS §6 standardised |
| DEC-079 | data-plate-standardisation (pending) |
| DEC-080 | Retrospective: PM and Stator Dock Connector Redesignation (Amends DEC-038) |
| DEC-081 | Retrospective: Rotor TTD No-Series-Resistor Policy (In Addition to DEC-016) |
| DEC-082 | 10µF bulk cap upgrade: 25V 0805 → 50V 1206 AEC-Q200; Samsung CL31B106KBK6PJE adopted |
| DEC-083 | `all_boards_bom.json` retired; BOM authority = Consolidated_BOM.md + board Design_Spec.md |

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

Follow `.copilot/SESSION_START.md` — it lists the canonical bootstrap order.
In brief:

1. `.copilot/SESSION_START.md` → load all directives from `.copilot/directives/` as memories
2. Seed session DB from `.copilot/todos/todos.sql` + `.copilot/todos/deps.sql`
3. This `plan.md`
4. `.copilot/handoff.md` (latest section first)
5. `.copilot/checkpoints/174-unified-cypher-extension-spec-created-awaiting-completeness-review.md`
