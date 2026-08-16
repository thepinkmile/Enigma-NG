# Checkpoint 180 — Cypher-Input Board Draft: Two Variants, I2C Board Identification

**Date:** 2026-08-06
**Session work:** Cypher-Input Board draft created and iteratively corrected across several
rounds of user feedback. Documents two board variants (26-Char Classic, 64-Char Extended)
sharing one circuit topology. New I2C board-identification scheme introduced (PCA9534A, one
address per keyboard variant). Four system-wide I2C address tables updated. Three related todo
detail files updated to target follow-on work.

---

## Status

`merge-create-cypher-input` remains **in_progress** - not marked done. Blocking open items
below must be resolved first (user has explicitly said not to mark this done prematurely).

---

## Files created

| File | Description |
| --- | --- |
| `design/Electronics/Cypher-Input/Design_Spec.md` | Full design specification for both variants - FR/DR requirements, ENC module interface, board-ID/non-cipher key I/O, keyswitch panel, LED indicator circuit, brightness control, interconnects, PCB fab, BOM (dual Qty columns) |
| `design/Electronics/Cypher-Input/Board_Layout.md` | Pinout reference - J1/J2/J3 ENC module mount tables (with per-variant PB[] usage notes), J4 Cypher Board interconnect usage table |

## Files modified

| File | Change |
| --- | --- |
| `design/Electronics/Electrical_Design.md` | I2C address table: added 0x38 (Cypher-Input Extended), 0x39 (Cypher-Input Classic) |
| `design/Electronics/System_Architecture.md` | Same addition |
| `design/Electronics/Boards_Overview.md` | Same addition; also fixed pre-existing `PCA9534A`/`PCA9534APWR` naming inconsistency (standardised to bare `PCA9534A` in this reference table, matching the `MCP23017` convention used for other expanders) |
| `design/Electronics/Controller/Design_Spec.md §4.1` | Same addition |
| `.copilot/todos/merge-create-cypher-input.md` | Status pending → in_progress; full variant/I2C context added; two open items flagged (JTAG chain-through wiring, possible second-connector gap) |
| `.copilot/todos/merge-create-cypher-output.md` | Notes updated: needs own PCA9534A address from 0x3A-0x3E reserved block; shares non-passthrough I2C bus with Cypher-Input; same LED/resistor sourcing applies |
| `.copilot/todos/merge-cypher-board-j3j6-pinouts.md` | Note added: `I2C_SCL_PASS`/`I2C_SDA_PASS` on J5/J6 are no longer a pure Plugboard-only passthrough - reconcile when this todo is picked up |
| `.copilot/todos/index.md` | `merge-create-cypher-input` status → in_progress |
| `.copilot/todos/todos.sql` | Same status update |

---

## Key design decisions this session

| Decision | Detail |
| --- | --- |
| Two board variants, one document | **26-Char Classic** (QWERTZ, 26 letters only, no Shift/digits/symbols/Space/Enter, mimics original German Enigma) and **64-Char Extended** (42 keys: 26 letters + 10 digits + 2 base64-extra symbols `+`/`/` + 2 Shift + Space + Enter). Documented in one Design_Spec.md with dual BOM Qty columns, mirroring the Rotor board's ROT-26/ROT-64 pattern. Component types identical between variants; only key count/layout, LED/resistor/socket quantities, `plain-bits` allocation, and I2C address differ. |
| Character set composition | 64-char cipher alphabet = RFC 4648 base64 (`A-Z`, `a-z`, `0-9`, `+`, `/`), realised via 26 physical letter keys (doubled via Shift for case) + 10 digit keys + 2 symbol keys = 64 values, on 40 cipher-path plain-bit signals. Space and Enter are UI-only, not part of the cipher alphabet - resolved via a separate I2C GPIO expander rather than the ENC module plain-bits bus. |
| Board-type identification via I2C | Every Cypher-Input variant (and eventually Cypher-Output and any custom keyboard) carries a PCA9534A GPIO expander (U4) at a variant-specific, system-unique I2C address, so the system can identify which keyboard is physically connected purely by which address responds. MCP23017 was rejected for this role - its fixed `0100xxx` address prefix (0x20-0x27) would be entirely consumed by existing Stator/Cypher and USM expanders, leaving no room. PCA9534A's `0111xxx` prefix (0x38-0x3F) gives a separate, mostly-free block. |
| I2C address assignments | 0x38 = Cypher-Input 64-Char Extended (also reads Space/Enter, 2 of 8 GPIO used). 0x39 = Cypher-Input 26-Char Classic (board-ID only, no Space/Enter on this variant). 0x3A-0x3E reserved for further keyboard variants/custom boards (Cypher-Output needs its own address from this range when designed - 0x39 is taken by the Classic keyboard variant, not reserved for Cypher-Output as originally proposed mid-session). |
| I2C_SCL_PASS/I2C_SDA_PASS is not a pure passthrough | Per user direction, these pins on the Cypher Board interconnect (J4 on Cypher-Input, mating Cypher J5) connect directly to this board's own U4 GPIO expander - not reserved solely for "Plugboard-local expansion logic" as originally documented on the Cypher Board. Cypher-Output's future expander will share the same bus. |
| Component sourcing corrections | LED (Kingbright APFA2507Y2G2C-C2) and both LED current-limit resistors (Yageo AT0402CRD07130RL/AT0402CRD07120RL) already had confirmed MPNs and supplier PNs explicitly given in the source discussion (rows 14/16/17) - initial draft had used incorrect/fabricated codes for these, corrected this session. Per user instruction, sourcing new (not-yet-used-anywhere) components is explicitly the user's job, not the agent's - only reuse of already-approved parts elsewhere in the system, or parts explicitly given in the source discussion, are populated with MPN/supplier PNs. |
| Dielectric change accepted | 555 timing capacitor (C1) changed from C0G/NP0 to X7R to reuse an already-approved system part (Samsung CL05B103KB5NNNC, same as Power Module C49) - user confirmed this was already their intended suggestion. |

---

## Blocking open items (must resolve before `merge-create-cypher-input` is done)

1. **JTAG chain-through wiring on J4** - how `JTAG_TDI_FWD` (pin 15) relates to this board's ENC
   module JTAG TDI/TDO (J2), and how `JTAG_TDO_RET`/`JTAG_TMS_RET`/`JTAG_TCK_RET`/
   `CPLD_RESET_N_RET` (pins 36/44/48/40) are used on this board. **User will define this first in
   the next session** - complex discussion, not yet started.
2. **Possible second-connector gap** - the original todo notes described a second connector
   ("top edge: QSS-025-01-L-D-RA-K female connectors") distinct from the Cypher Board
   interconnect, possibly implying an undesigned Plugboard interface (per Entry 19's original
   "Plugboard and top edge...use female receptacles" framing). Current draft only implements a
   single J4 connector to the Cypher Board. **User will look at this gap after the JTAG
   definition work in the next session.**

---

## Next Session Start Point

Follow `.copilot/SESSION_START.md`, then read this checkpoint (180) and resume with the JTAG
chain-through wiring definition for Cypher-Input's J4 interconnect (`merge-create-cypher-input`,
still in_progress). After that is resolved, revisit the possible second-connector/Plugboard gap
noted above before considering this todo done.
