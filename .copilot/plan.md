# Enigma-NG Session Plan

> Canonical state: `.copilot/plan.md` in the repository root (tracked in git).
> At the start of a new session, read `.copilot/SESSION_START.md` and follow its steps,
> then this file and `.copilot/handoff.md`, then the latest relevant checkpoint(s) in `.copilot/checkpoints/`.

---

## Current Status (as of 2026-08-16 — Cypher-Input Board design complete)

The design discussion merge is ongoing. Since checkpoint 181, the Cypher-Input Board was
restructured into common + per-variant files (DEC-086: mirrors the Rotor board pattern), gained a
third **10-Numeric** variant, and collapsed its I2C board-identification scheme to a single shared
address (`0x38`) with `BOARD_ROLE_ID[2:0]` as the sole variant identifier. Separately, the generic
cipher-bank interface board was renamed and redesigned from `Electronics/Encoder/` to
`Electronics/Encoder_Module/`, replacing its legacy 20-pin IDC ribbon + spade-terminal interface
with a 3-connector Hirose DF40C BtB family (`J1`/`J2`/`J3`); it remains the canonical connector
owner referenced from the Cypher Board and Cypher-Input Board.

Most recently (checkpoint 183, DEC-087), the Cypher-Input LED indicator circuit was reworked from
the ground up: colour selection moved entirely off the ENC module's `plain-bits` bus and onto a
local, software-configurable RGB circuit (U4 GPIO + a local hardware mux/Shift-sense network on
the 64-Char Extended variant only), and brightness moved from feeding the ENC module's `GCLK0` to
gating a shared cathode-return switch. Both signals now broadcast to the future Cypher-Output
board via the left connector pair (`J4`/`J6`) instead of the JTAG chain-through pair. **The RGB
LED part itself is a placeholder (TBD)** - sourcing is explicitly deferred to `merge-missing-
components` (2026-08-15) rather than resolved ad hoc, so it can be batched with other outstanding
BOM parts; do not source this without explicit user approval.

Checkpoint 184 (2026-08-15) fixed a naming inconsistency spotted during user review of
`Board_Layout.md`: the forwarded/broadcast keypress-activity signal on the Cypher <-> Cypher-Input
`J5`/`J7` interconnect had two competing names in the docs (`ENC_ACTIVE_INPUT_N`, the original
draft name, vs. `ENC_ACTIVE_KBD_N`, an incomplete rename intended to match the Cypher Board's
internal net). Consolidated on **`ENC_ACTIVE_INPUT_N`** everywhere on both boards (user's explicit
preference, since this signal may eventually be driven from the CM5 via GPIO rather than only a
physical keyboard, so a name not tied to "KBD" is more future-proof). This is distinct from the
generic `ENC_ACTIVE_N` signal name, which remains unchanged - that name belongs to the ENC module's
own local output pin (`J2`) and is owned by `Encoder_Module/Design_Spec.md`, not the forwarded/
broadcast signal. Two "forwarded to J4" cross-references were also corrected to J5/J7, matching the
actual pin-map tables (J4 is the left/Plugboard-passthrough pair, not the JTAG-template pair the
signal actually lives on). The retiring Stator board's own stale copies of this same inconsistency
were deliberately left untouched (out of scope, pending its removal via `merge-remove-old-boards`).

`merge-create-cypher-input` is now **done** (checkpoint 185, 2026-08-16). Its only remaining
blocking item - the left-side (J4/J6) Plugboard passthrough signal definition - is resolved via
**DEC-088**: there are no Plugboard-specific signals on that connector at all. The physical
plugboard patch-jack harness wires directly from the Cypher Board's own spade terminal bank
(`J20+`, confirmed at the bottom edge of the rear face - HID connectors stay at the top edge)
to jacks mounted mechanically-only on the Plugboard board, bypassing the `J4`-`J7` HID
interconnect stack entirely. The `J4`/`J6` left pair also gained reserved/spare `5V_MAIN` pins,
in case a future LED candidate (see the SK6812MINI-E candidate note in `merge-missing-
components.md`) needs a supply above `3V3_ENIG`'s 3.3V.

Also this session: a repo-wide documentation cleanup pass on Cypher-Input (`BOARD_ROLE_ID`/I2C
wording corrections, historical-language removal, "64-Character" variant naming consistency,
moving the 64-Character-only colour-select mux circuit out of the common Design_Spec into its own
variant file, and restructuring the board's assembly plan so only LEDs + RV1 are top-face/
hand-soldered - everything else is rear-face/automated single-sided JLCPCB SMT, per the
constraint in `design/Production/JLCPCB_Manufacturing.md §3.1`). See checkpoint 185 for the full
list.

**Explicitly out of scope for now:** `Mechanical/Keyboard_Assembly`, `Lightboard_Assembly`, and
`Plugboard_Assembly` design specs still describe the pre-Cypher standalone-board/IDC-ribbon
architecture and are stale relative to the current Cypher-Input/Cypher-Output/Plugboard designs.
Per explicit user direction, mechanical and software sections will get a full overhaul only once
the electronics design is fully merged with all current discussions — do not touch them before
then.

Latest checkpoint: `.copilot/checkpoints/185-cypher-input-complete-plugboard-5v-main-dec088.md`

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
All blocking items resolved:

1. **JTAG chain-through wiring** — resolved. Full 37-device chain order defined: FT232H →
   Cypher-Input CPLD → Cypher-Output CPLD → 4x Plugboard Encoder Modules → Cypher Board's own U1
   CPLD → 30x Rotor CPLDs → `TTD_RETURN` → FT232H. `TTD` naming convention applied consistently
   (no more `_FWD`/`_RET` suffixes).
2. **Second-connector/Plugboard gap** — resolved (DEC-088). No Plugboard signals live on the
   `J4`/`J6` left pair at all - the physical plugboard patch-jack harness wires directly to the
   Cypher Board's own spade terminal bank (`J20+`) instead, bypassing the HID interconnect stack.
   The left pair carries 3V3_ENIG/GND, LED colour/brightness broadcast (DEC-087), and reserved
   `5V_MAIN` pins (DEC-088) only.

All other signals previously carried on the old single connector (`ENC_DATA[5:0]`,
`BOARD_ROLE_ID[2:0]`, `I2C_SCL`/`I2C_SDA`, `ENC_ACTIVE_INPUT_N`) were also resolved into the new
connector's 50-pin map.

See `.copilot/checkpoints/185-cypher-input-complete-plugboard-5v-main-dec088.md` for full detail.

**Next: `merge-create-cypher-output`** — lightboard output panel board. Needs its own I2C address
from the 0x39-0x3E reserved block (not `0x38`, which is Cypher-Input's); shares the
`I2C_SCL`/`I2C_SDA` bus with Cypher-Input, not a pure passthrough; needs no local colour-select
mux/Shift-sense/555 oscillator of its own (only receives Cypher-Input's broadcast LED
colour/brightness signals and applies them to its own LED bank MOSFETs); needs its own
`BOARD_ROLE_ID[2:0]` variant scheme once variant requirements are confirmed. Wiring notes already
captured in `.copilot/todos/merge-create-cypher-output.md`, synced to the DEC-088 architecture.

After Cypher-Output:

- `merge-create-plugboard` — now well-scoped by DEC-088: passive HID-chain termination (mirrors
  Stack-Blanking) + mechanical-only jack-field mounting, wired via spade harness to the Cypher
  Board
- `merge-ctl-dock-usb-allocation` → `merge-update-ctl-board`
- `merge-cypher-board-j3j6-pinouts` — full 50-contact allocation for J3/J4, plus the new reserved
  `5V_MAIN`/LED broadcast pin numbers on J5/J6 (J5/J6 signal set otherwise already defined - see
  `Cypher/Board_Layout.md §4`)

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
| **Cypher-Input Board** | **Draft, complete** | Created 2026-08-06; three variants (26-Char Classic, 64-Character, 10-Numeric per DEC-086); JTAG/connector architecture resolved 2026-08-09; common/variant-file restructure + single I2C address per DEC-086 (2026-08-12); LED colour architecture reworked to local RGB circuit per DEC-087 (2026-08-14); Plugboard/5V_MAIN architecture resolved per DEC-088 (2026-08-16) - no blocking items remain; RGB LED part still TBD (see `merge-missing-components`) |
| **Encoder Module** | **Redesigned** | Renamed from `Electronics/Encoder/`; DF40C BtB interconnect (`J1`-`J3`) replaces legacy IDC ribbon + spade terminals; canonical connector owner for Cypher/Cypher-Input/future Cypher-Output ENC mounts (2026-08-13) |

## Open Pass-10 Findings (0 remaining — all closed ✅)

All 91 Pass-10 findings are resolved. REF-P10-05 closed: 2BHR-30-VUA uses KiCAD built-in `Connector_IDC:IDC-Header_2x15_P2.54mm_Vertical`.

## Open Workstreams

### Immediate (resume here)

1. **Design Discussion Merge** (`design-discussion-merge` — in_progress)
   - `merge-create-cypher-output` — **next task** (board files not yet created; wiring notes
     for the new connector architecture already captured in its todo file, synced to DEC-088)
   - `merge-create-plugboard` — termination board for Cypher-Input/Output stack bottom; now
     well-scoped by DEC-088 (passive HID termination + mechanical jack mounting)
   - `merge-ctl-dock-usb-allocation` → `merge-update-ctl-board`
   - `merge-diagrams-review` — review/update stale Rotor Mini-Stack diagrams, create dedicated
     Cypher-system diagrams; blocks `merge-final-review`
   - Full sequence tracked in `.copilot/todos/design-discussion-merge.md`
2. **Pending pinout work** (`merge-cypher-board-j3j6-pinouts`)
   - Full 50-contact allocation for Cypher Board J3/J4 stacking connectors (J5/J6 now defined,
     see `Cypher/Board_Layout.md §4`)

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
| DEC-088: Plugboard/5V_MAIN architecture | Plugboard board's electrical role is passive HID-chain termination only (no plugboard signals at all); physical patch jacks mount mechanically-only on it, wired via spade-to-spade harness directly to Cypher Board's own `J20+` spade bank (bottom edge of rear face); `J4`/`J6` left pair gains reserved `5V_MAIN` pins |
| DEC-087: LED colour architecture (2026-08-14) | Colour selection moved entirely off `plain-bits` onto a local RGB circuit (U4 GPIO + mux/Shift-sense on 64-Character variant only); brightness gates a shared cathode-return switch; broadcast to Cypher-Output via left connector pair |
| DEC-086: Cypher-Input restructure (2026-08-12) | Common/variant-file split (mirrors Rotor); 10-Numeric variant added; single shared I2C address (`0x38`), `BOARD_ROLE_ID[2:0]` is the sole variant identifier |
| Single-sided JLCPCB assembly (2026-08-16) | Only LEDs + RV1 are top-face/hand-soldered; everything else rear-face/automated SMT, per `JLCPCB_Manufacturing.md §3.1`'s single-sided-only constraint |
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
- **Design Log restructured** — `design/Design_Log/` (per-DEC files); next entry = **DEC-089** as `DEC-089_{title}.md` + `index.md` row; NEVER modify existing DEC files; NEVER create as `design/Design_Log.md`
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
Then read checkpoint 185. `merge-create-cypher-input` is **done** - no blocking items remain.
**Recommended next task: `merge-create-cypher-output`** (lightboard/output panel board) - create
the board files applying the wiring notes already captured in `.copilot/todos/merge-create-
cypher-output.md` (JTAG/signal pin numbers, DEC-086 I2C addressing pattern, DEC-087 LED
broadcast-consumer architecture, DEC-088 Plugboard/5V_MAIN wording now synced). That board needs
no local colour-select mux/Shift-sense/555 oscillator of its own - just 3 colour MOSFETs + 1
cathode-return MOSFET driven by Cypher-Input's broadcast signals - plus its own I2C GPIO expander
(fresh address from `0x39-0x3E`, not `0x38`) and its own `BOARD_ROLE_ID[2:0]` variant scheme once
confirmed with the user. After that: `merge-create-plugboard` (now well-scoped by DEC-088), then
`merge-cypher-board-j3j6-pinouts` (final `5V_MAIN`/LED broadcast pin numbers). RGB LED part
sourcing remains deferred to `merge-missing-components` (SK6812MINI-E candidate under evaluation,
not yet approved). Mechanical/software sections remain out of scope until a dedicated overhaul
pass after the electronics merge completes.
