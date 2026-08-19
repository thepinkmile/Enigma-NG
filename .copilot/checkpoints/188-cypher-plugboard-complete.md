# Checkpoint 188 — Cypher-Plugboard Board Complete

**Date:** 2026-08-19

## Summary

`merge-create-plugboard` is now **done**. This session created the full Cypher-Plugboard Board
design (renamed from the originally-planned "Plugboard Board" for file-explorer grouping
consistency with the rest of the Cypher family), then corrected two rounds of real design issues
surfaced during user review.

## 1. Board created: `design/Electronics/Cypher-Plugboard/`

5 files, mirroring the Cypher-Input/Cypher-Output common+variant structure:

- `Design_Spec.md` - common electrical spec (HID-chain termination mirroring Stack-Blanking,
  power passthrough, mechanical construction).
- `Board_Layout.md` - `J1`/`J2` pinout reference (reusing the Cypher Board's own J5/J6 HID
  interconnect templates).
- `Cypher_Plugboard_64_Char_Design.md` - 7 rows, 64 positions / 128 jacks (`J3`-`J130`): digits
  row (10) + 3 uppercase rows (9/9/9, `+` appended to the short row) + 3 lowercase rows (9/9/9,
  `/` appended to the short row) - a deliberately symmetrical layout per user direction.
- `Cypher_Plugboard_26_Char_Design.md` - 3 rows, 26 positions / 52 jacks (`J3`-`J54`): natural
  9/9/8 split, uppercase only.
- `Cypher_Plugboard_10_Numeric_Design.md` - 2 rows, 10 positions / 20 jacks (`J3`-`J22`): 5/5
  split.

Each "plug" position is 2 jack sockets (one per plugboard pass) placed side-by-side horizontally,
not stacked - user-directed to minimise overall panel/enclosure height.

## 2. Electrical scope (mirrors Stack-Blanking)

Per DEC-088, this board carries **no plugboard-signal-specific pins** on either connector - it is
a pure JTAG-spoke terminator (R1-R3, 10 kOhm, on TCK/TMS/`CPLD_RESET_N`) plus power continuity.
`TTD_HID_IN`/`TTD_HID_PASS`/`TTD_HID_OUT` and the LED broadcast/`BOARD_ROLE_ID` signals are all
left NC - confirmed correct by the user: each HID board (Cypher-Input, Cypher-Output) already
provides its own local TDI pull-up close to its own CPLD via the generic Encoder Module's R3
(`Encoder_Module/Design_Spec.md §5` JTAG Chain Integrity), and the system always requires both a
Cypher-Input and a Cypher-Output board connected (no valid single-HID-board configuration).

## 3. Jack socket sourced: Switchcraft 12A

Confirmed by the user with datasheet in hand (`design/Datasheets/Switchcraft-12A-datasheet.pdf`):
Switchcraft 12A ("E12A"), 6.35mm (1/4") 2-conductor switched panel-mount jack, DigiKey `SC1089-ND`,
Mouser `502-12A`. No JLCPCB PN - manually assembled, not part of the JLCPCB PCBA order.
3/8-32 UNEF-2A threaded bushing; 3 terminals (`Tip`, `Tip-Shunt` normally-closed switch contact,
`Sleeve`). Wiring updated to reflect this: `Tip`+`Tip-Shunt` tied to one spade jumper (decode-role
terminal), `Sleeve` to a second spade jumper (encode-role terminal), both running to the Cypher
Board's own `J20+` spade bank.

## 4. Major mechanical correction: PCB is a thin connector strip only; jacks mount to a machined enclosure

The first draft incorrectly assumed the jack field and its character silkscreen lived on this
board's own PCB. The user corrected this: **the PCB is a thin strip along the top edge only**,
just large enough for `J1`/`J2`/R1-R3 - identical across all three variants. **The entire jack
field mounts directly to a machined metal enclosure**, not the PCB, with every jack's threaded
bushing making direct mechanical/electrical contact with that enclosure. This keeps the whole
external jack field on a continuous `GND_CHASSIS` network, consistent with the rest of the
system's external connectors - dissipating through the single `GND_CHASSIS`-to-GND bond that
remains on the Power Module only (per `design/Standards/Global_Routing_Spec.md §5`). Character
labels are engraved/printed on the metal enclosure, not PCB silkscreen. The enclosure is sized per
variant (scaling with row count); the PCB strip itself is identical regardless of variant.

Added `FR-PLB-06` (chassis-bonding requirement) and `DR-PLB-09` (chassis bonding mechanism);
rewrote §2 Architecture, §4 Plugboard Jack Field, §6 PCB Fabrication, §7 Thermal & ESD, §8
Branding, the mermaid diagram, and `Board_Layout.md`'s orientation convention to match. Updated
all three variant files' overview paragraphs (removed the stale "shared board outline sized for
64-Character, with keepout" framing - each variant's enclosure is now independently sized).

## 5. `merge-cypher-board-j3j6-pinouts` status update

While closing out this todo, confirmed and noted in that todo's own file: the **J5/J6 portion is
now fully resolved** (both are fully 50-pin allocated in `Cypher/Board_Layout.md §4`, including
this session's `TTD_HID_*` rename and the Cypher-Output I2C passthrough fix) - remaining scope is
**J3/J4 only** (still only 26/24 of 50 contacts defined on the main rotor-stack-side connectors).
Also corrected a stale 2026-08-06 assumption in that todo's notes that Cypher-Output "will need"
its own I2C GPIO expander address - superseded by the confirmed no-I2C-bus design.

## Status

- `merge-create-plugboard`: **done**.
- Todo detail file archived to `.recycle-bin/merge-create-plugboard.md`.
- **Next session: `merge-cypher-board-j3j6-pinouts`** (J3/J4 only) or `merge-ctl-dock-usb-
  allocation` → `merge-update-ctl-board` - see `plan.md`/`handoff.md` for the full next-steps
  list. Session paused here due to token budget; user's subscription renews in ~2 weeks.
