# Enigma-NG Session Plan

> Canonical state: `.copilot/plan.md` in the repository root (tracked in git).
> At the start of a new session, read `.copilot/SESSION_START.md` and follow its steps,
> then this file and `.copilot/handoff.md`, then the latest relevant checkpoint(s) in `.copilot/checkpoints/`.

---

## Current Status (as of 2026-08-16 — Cypher-Output Board drafted, review in progress)

`merge-create-cypher-input` is **done** (checkpoint 185). This session (checkpoint 186) covered
two threads:

1. **`BOARD_ROLE_ID` architecture redesign (DEC-089):** widened from a 3-bit enumerated index to
   a 4-bit capability bitmask (bit0=Characters, bit1=Numbers, bit2=Special, bit3=Custom) with an
   `AND`-based compatibility rule on the Cypher Board's CPLD comparator. CPLD pin budget was freed
   by replacing the old `CFG_REFMAP[5:0]` parallel bus (removed from User Settings Module Bank 2)
   with a JTAG-based UFM write for reflector-map selection. `BOARD_ROLE_ID` migrated from the
   Cypher Board's `J6` to `J5` (which has spare pin budget). Went through several rounds of
   user-directed refinement: removed all historical/narrative wording from design docs (state
   only current facts - history belongs in the DEC log + git), removed "spare"/"reserved" pin
   labels (every pin needs a specific current allocation), and rebuilt the `J5` pin map for 180°
   rotational symmetry with an equal 8/8/8 `3V3_ENIG`/`5V_MAIN`/GND split and diagonally-opposed
   signal placement. Also moved `I2C_SDA`/`I2C_SCL` on the Cypher Board's `J6` template to a
   single adjacent pin pair (27/28).
2. **Cypher-Output Board design created** (`design/Electronics/Cypher-Output/` - all 5 files:
   common Design_Spec.md/Board_Layout.md + 3 variant files, mirroring Cypher-Input's structure).
   Key architecture: ENC module in `LBD_DEC` role decodes to a one-hot `plain-bits` lens-select
   output; **per-position discrete N-channel MOSFETs (2N7002K)** gate each lens (justified against
   direct CPLD-pin sinking via drive-strength research - see checkpoint 186); no local colour/
   brightness generation and **no I2C GPIO expander** at all (pure hardwired `BOARD_ROLE_ID_OUT`
   strap, colour/brightness received as broadcast from Cypher-Input); the 64-Character variant
   carries a **custom-support SPDT switch (SW1)** toggling `BOARD_ROLE_ID_OUT[3]` between `0b0111`
   and `0b1111`, placed in a keyless keepout zone mirroring Cypher-Input's RV1 location.

A detailed technical review of the Cypher-Output draft surfaced and fixed several real gaps:
Cypher-Input's LED bank (which lights the ENTIRE key bank simultaneously, one shared MOSFET per
colour channel) draws from `5V_MAIN`, not `3V3_ENIG`, and this **1.26A worst-case combined-channel
load was never budgeted anywhere** - added a `5V_MAIN` entry decoupling bank to Cypher-Input
(previously only `3V3_ENIG` had one) and added the load to `Power_Budgets.md`'s 5V_MAIN Load
Analysis (system total revised 9.50A → 10.76A, 89.7% of the LMQ61460-Q1's 12A capacity). Also
fixed a stale User Settings Module figure in the same table (0.24A → 0.10A, reflecting this
session's earlier Bank 2/`CFG_REFMAP` removal that hadn't been propagated), and corrected
confusing/backwards "connector ownership" wording in both HID boards' J4-J7 Interconnects
sections.

**`merge-create-cypher-output` is NOT yet complete** - the user is continuing a document review
of the Cypher-Output files next session before marking it done. Do not mark it complete until
the user explicitly confirms the review is finished.

Latest checkpoint: `.copilot/checkpoints/186-cypher-output-drafted-power-budget-fixes.md`

### Completed merge sub-tasks

| Sub-task | Result |
| --- | --- |
| `merge-grs-6layer-stackup` | GRS §2.3.4 added (PCBWay 6-layer; Cypher Board) |
| `merge-create-cypher-board` | `design/Electronics/Cypher/` created (Design_Spec + Board_Layout) |
| `merge-create-stack-input` | `design/Electronics/Stack-Input/` created (Design_Spec + Board_Layout) |
| `merge-create-stack-output` | `design/Electronics/Stack-Output/` created (Design_Spec + Board_Layout) |
| `merge-create-stack-blanking` | `design/Electronics/Stack-Blanking/` created (Design_Spec + Board_Layout) |
| `merge-create-stack-interposer` | `design/Electronics/Stack-Interposer/` created (Design_Spec + Board_Layout) |
| `merge-create-cypher-input` | `design/Electronics/Cypher-Input/` complete; 3 variants (Classic/64-Char/10-Numeric); DEC-086/087/088 applied |

### Current merge focus

**Done: `merge-create-cypher-input`** — keyboard input panel board (checkpoint 185, DEC-088).

**In progress: `merge-create-cypher-output`** — lightboard output panel board (checkpoint 186).
All 5 board files created (common Design_Spec.md/Board_Layout.md + 3 variant files). Actual
architecture implemented differs from the earlier wiring-notes draft in `.copilot/todos/merge-
create-cypher-output.md` (that file is now stale and should be treated as historical context
only, not a current spec of the design):

- **No I2C GPIO expander at all** on this board (the earlier plan assumed one, at a fresh address
  from `0x39-0x3E`) - `BOARD_ROLE_ID_OUT[3:0]` is a pure hardwired strap, and there is no other
  I2C-worthy function on this board (no keys to read, no local colour config to drive).
- **Per-position discrete N-channel MOSFETs (2N7002K, Q1-Qxx)**, not a shared 3-MOSFET-per-colour-
  channel topology like Cypher-Input - each lens position needs individual one-hot addressing
  from the ENC module's `LBD_DEC` decode output, whereas Cypher-Input lights its entire key bank
  simultaneously with one shared colour.
- `BOARD_ROLE_ID_OUT[3:0]` values: 26-Char Classic=`0b0001`, 10-Numeric=`0b0010`, 64-Character=
  `0b0111` (default) / `0b1111` (custom-support enabled via SW1, a panel-mount SPDT switch unique
  to this variant).
- 64-Character variant is **40 lens positions** (not 42) - Shift/Space/Enter have no lens.

**`merge-create-cypher-output` is NOT yet complete** - user is continuing a document review next
session. See `.copilot/checkpoints/186-cypher-output-drafted-power-budget-fixes.md` for the full
list of review findings already fixed this session (5V_MAIN power budget gap, connector-ownership
wording, LED mounting-face open item, etc.) and what remains open.

After Cypher-Output is confirmed complete:

- `merge-create-plugboard` — well-scoped by DEC-088: passive HID-chain termination (mirrors
  Stack-Blanking) + mechanical-only jack-field mounting, wired via spade harness to the Cypher
  Board
- `merge-ctl-dock-usb-allocation` → `merge-update-ctl-board`
- `merge-cypher-board-j3j6-pinouts` — check current status; the J5/J6 pin maps received extensive
  rework this session (DEC-089) and this todo may now be substantially or fully resolved - verify
  before treating it as still-open work

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
| **Cypher Board** | **Draft** | Created 2026-07-05; consolidates STA + REF + JM; J5/J6 HID interconnect redesigned 2026-08-09 (4-connector architecture, shared board-agnostic template) |
| **Stack-Input Board** | **Draft** | Created 2026-07-05; EXT input-side + native solenoid AM |
| **Stack-Output Board** | **Draft** | Created 2026-07-12; J6 updated to SQT-115-01-L-D-RA (from 2BHR-30-VUA); DEC-085 |
| **Stack-Interposer Board** | **Draft** | Created 2026-07-25; TMMH-115-01-L-D-ES J1/J2; SQT-115-01-L-D-RA mating; mirror-corrected routing note |
| **Stack-Blanking Board** | **Draft** | Created 2026-07-12; passive termination; 5× termination resistors |
| **Cypher-Input Board** | **Draft, complete** | Created 2026-08-06; three variants (26-Char Classic, 64-Character, 10-Numeric per DEC-086); JTAG/connector architecture resolved 2026-08-09; common/variant-file restructure + single I2C address per DEC-086 (2026-08-12); LED colour architecture reworked to local RGB circuit per DEC-087 (2026-08-14); Plugboard/5V_MAIN architecture resolved per DEC-088 (2026-08-16); `BOARD_ROLE_ID` widened to 4-bit capability bitmask + J5 migration per DEC-089 (2026-08-16); 5V_MAIN entry decoupling bank added for LED bank load (2026-08-16) - no blocking items remain; RGB LED part still TBD (see `merge-missing-components`) |
| **Cypher-Output Board** | **Draft, review in progress** | Created 2026-08-16 (checkpoint 186); three variants mirroring Cypher-Input (26-Char Classic, 64-Character, 10-Numeric); per-position discrete MOSFET LED select (no shared-colour-bank topology); no local I2C expander; 64-Character variant carries the custom-support switch (SW1); user reviewing before marking `merge-create-cypher-output` complete |
| **Encoder Module** | **Redesigned** | Renamed from `Electronics/Encoder/`; DF40C BtB interconnect (`J1`-`J3`) replaces legacy IDC ribbon + spade terminals; canonical connector owner for Cypher/Cypher-Input/Cypher-Output ENC mounts (2026-08-13) |

## Open Pass-10 Findings (0 remaining — all closed ✅)

All 91 Pass-10 findings are resolved. REF-P10-05 closed: 2BHR-30-VUA uses KiCAD built-in `Connector_IDC:IDC-Header_2x15_P2.54mm_Vertical`.

## Open Workstreams

### Immediate (resume here)

1. **Design Discussion Merge** (`design-discussion-merge` — in_progress)
   - `merge-create-cypher-output` — **in progress, resume here.** All 5 board files created;
     user is continuing a document review next session before marking this complete. Read
     checkpoint 186 in full before continuing. Do NOT mark this todo done until the user
     explicitly confirms the review is finished.
   - `merge-create-plugboard` — termination board for Cypher-Input/Output stack bottom; well
     -scoped by DEC-088 (passive HID termination + mechanical jack mounting); starts after
     Cypher-Output is confirmed complete
   - `merge-ctl-dock-usb-allocation` → `merge-update-ctl-board`
   - `merge-diagrams-review` — review/update stale Rotor Mini-Stack diagrams, create dedicated
     Cypher-system diagrams; blocks `merge-final-review`
   - Full sequence tracked in `.copilot/todos/design-discussion-merge.md`
2. **Pending pinout work** (`merge-cypher-board-j3j6-pinouts`)
   - Verify current status before treating as open - the Cypher Board's J5/J6 pin maps received
     extensive rework this session (DEC-089: rotational symmetry, equal 3V3/5V/GND split,
     `BOARD_ROLE_ID` migration, I2C pin move) and this todo may now be substantially or fully
     resolved

### Deferred / Blocked

- `battery-connector-final-review` — blocked: awaiting supplier response
- `jdb-ft232h-3v3-vregin` — blocked (v2.0)
- `display-addon-board`, `cpld-production-replacement`, `display-aperture` — blocked (v2.0)
- `ctl-t1-coilcraft-v2-review` — blocked (v2.0)

### Process items to review

- **Directive files hold mutable "next value" state** (`tertiary.md` — next DEC number;
  `repo-state.md` — next checkpoint number). Directives should only be written/updated by the
  repository owner; tracked state like this arguably belongs in `plan.md`/`handoff.md` instead,
  since the agent updates it every time a new DEC or checkpoint is created. See `handoff.md`
  "Process item to review" (2026-08-06) for detail. Not changing the directive files without
  explicit instruction.

## Key Design Decisions (recent — 2026-08-16 session)

| Decision | Summary |
| --- | --- |
| DEC-089: `BOARD_ROLE_ID` capability bitmask + J5 migration | Widened `BOARD_ROLE_ID` from a 3-bit enumerated index to a 4-bit capability bitmask (bit0=Characters, bit1=Numbers, bit2=Special, bit3=Custom) with an `AND`-based compatibility comparator; freed CPLD pins by replacing `CFG_REFMAP[5:0]` with a JTAG UFM write; migrated the strap from Cypher Board `J6` to `J5` (spare pin budget); rebuilt the `J5` pin map for 180° rotational symmetry with an equal 8/8/8 `3V3_ENIG`/`5V_MAIN`/GND split |
| DEC-088: Plugboard/5V_MAIN architecture | Plugboard board's electrical role is passive HID-chain termination only (no plugboard signals at all); physical patch jacks mount mechanically-only on it, wired via spade-to-spade harness directly to Cypher Board's own `J20+` spade bank (bottom edge of rear face); `J4`/`J6` left pair gains `5V_MAIN` pins |
| Cypher-Output per-position MOSFET topology (2026-08-16) | Each lens position gated by its own discrete N-channel MOSFET (2N7002K), driven directly by the ENC module's one-hot decoded `plain-bits` output - not a shared-colour-bank topology like Cypher-Input, since only one lens is ever lit at a time; justified against direct CPLD-pin sinking via MAX II drive-strength research (8/16mA rating vs. up to 30mA worst-case per-position load) |
| Cypher-Input LED bank draws from `5V_MAIN` (2026-08-16) | Previously undocumented/unbudgeted; added a `5V_MAIN` entry decoupling bank (DR-CYPI-14a) and a 1.26A worst-case line item to `Power_Budgets.md` (system total 9.50A → 10.76A, 89.7% of 12A capacity) |
| DEC-087: LED colour architecture (2026-08-14) | Colour selection moved entirely off `plain-bits` onto a local RGB circuit (U4 GPIO + mux/Shift-sense on 64-Character variant only); brightness gates a shared cathode-return switch; broadcast to Cypher-Output via left connector pair |
| DEC-086: Cypher-Input restructure (2026-08-12) | Common/variant-file split (mirrors Rotor); 10-Numeric variant added; single shared I2C address (`0x38`), `BOARD_ROLE_ID[2:0]` is the sole variant identifier (superseded by DEC-089's 4-bit widening) |
| Single-sided JLCPCB assembly (2026-08-16) | Only LEDs (+ RV1 on Cypher-Input, + SW1 on Cypher-Output's 64-Character variant) are top-face/hand-soldered; everything else rear-face/automated SMT, per `JLCPCB_Manufacturing.md §3.1`'s single-sided-only constraint |
| 64-Character variant naming (2026-08-16) | Renamed from "64-Char Extended" to "64-Character", matching the Rotor board's "64-Character Variant" convention |

### Prior decisions (2026-08-09 session)

| Decision | Summary |
| --- | --- |
| 4-connector HID board architecture | Cypher-Input/Cypher-Output each carry 4 connectors (2 male top, 2 female bottom, inset from board sides) instead of 1; left pair = power/LED broadcast/reserved 5V_MAIN, right pair = shared JTAG+signal template; lets either board attach to the Cypher Board in either order |
| Revised 37-device JTAG chain order | FT232H → Cypher-Input CPLD (1) → Cypher-Output CPLD (2) → 4x Plugboard Encoder Modules (3-6) → Cypher Board's own U1 CPLD (7) → 30x Rotor CPLDs (8-37) → `TTD_RETURN` → FT232H; all "static" CPLDs precede the "dynamic" Rotor stack; U1 moved from position 1 to 7 |
| `TTD` naming convention enforced | JTAG serial data signal named `TTD` at every hop (matches existing Rotor mini-stack convention); superseded the draft's `JTAG_TDI_FWD`/`JTAG_TDO_RET`/etc. naming |
| Full 50-pin shared connector map resolved | `ENC_DATA[5:0]`, `BOARD_ROLE_ID[2:0]`, `CPLD_RESET_N` (single pin), `ENC_ACTIVE_INPUT_N`, `I2C_SCL`/`I2C_SDA`, plus `TTD`/`TMS`/`TCK` — see `Cypher/Board_Layout.md §4` |
| `BOARD_ROLE_ID[2:0]` encoding | MSB-to-LSB: `000`=64-Char, `001`=26-Char, `010`=10-Numeric, `011`-`111` reserved |

### Prior decisions (2026-08-06 session)

| Decision | Summary |
| --- | --- |
| Cypher-Input: two variants, one document | 26-Char Classic (QWERTZ, 26 letters) and 64-Char Extended (42 keys, base64 RFC 4648) share one circuit topology; dual BOM Qty columns mirror Rotor's ROT-26/ROT-64 pattern |
| I2C board-identification scheme | PCA9534A (not MCP23017 — address space would be exhausted) at a variant-specific address so the system can identify which keyboard is connected; 0x38 = Extended, 0x39 = Classic, 0x3A-0x3E reserved for further variants |
| Sourcing responsibility | Agent may only populate MPN/supplier PNs for parts explicitly given in the source discussion or already approved elsewhere in the system BOM; sourcing genuinely new components is the user's job |

### Prior decisions (2026-07-05 session)

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
- **Design Log restructured** — `design/Design_Log/` (per-DEC files); next entry = **DEC-090** as `DEC-090_{title}.md` + `index.md` row; NEVER modify existing DEC files; NEVER create as `design/Design_Log.md`
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
Then read checkpoint 186 in full (most recent). `merge-create-cypher-output` is **in progress,
not yet complete** - all 5 board files exist (`design/Electronics/Cypher-Output/`), but the user
is continuing a document review before marking it done. **Do not mark `merge-create-cypher-
output` complete until the user explicitly confirms the review is finished** - resume by asking
what they'd like to review next, or wait for their lead.

The old wiring-notes draft in `.copilot/todos/merge-create-cypher-output.md` is now **stale** -
the actual implemented architecture differs in several ways (no I2C expander at all; per-position
discrete MOSFETs, not a shared 3-MOSFET colour-bank; `BOARD_ROLE_ID_OUT` values per DEC-089's
4-bit scheme, not the old 3-bit one). Treat checkpoint 186 as the authoritative summary of what
was actually built, not that todo file.

After Cypher-Output is confirmed complete: `merge-create-plugboard` (well-scoped by DEC-088),
then `merge-cypher-board-j3j6-pinouts` (verify current status first - may now be substantially
resolved by this session's J5/J6 pin map rework, DEC-089). RGB LED part sourcing remains deferred
to `merge-missing-components` (SK6812MINI-E candidate under evaluation, not yet approved; both
Cypher-Input and Cypher-Output need updating together if/when this is decided - see checkpoint
186). Mechanical/software sections remain out of scope until a dedicated overhaul pass after the
electronics merge completes.
