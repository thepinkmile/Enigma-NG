# Cypher-Output Board - 64-Character Variant Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-08-16
**Parent Document:** `design/Electronics/Cypher-Output/Design_Spec.md`

---

## 1. Overview

This document specifies the **64-Character** variant of the Enigma-NG Cypher-Output Board. It
mirrors the 64-Character Cypher-Input Board's QWERTY-style layout 1:1 for the 40 cipher-path
lens positions. Space and Enter are non-cipher keys on the paired keyboard with nothing to
display, so - like the 10-Numeric variant - they have no corresponding lens on this board. This
is the only Cypher-Output variant that carries the custom-support switch (SW1, see §4), and its
lens set is broad enough to display the output of **any** Cypher-Input variant (see
`Design_Spec.md §1` for the compatibility rule).

All three Cypher-Output variants (26-Char Classic, 64-Character, 10-Numeric) share an identical
circuit topology (ENC module mount, per-position LED indicator bank, Cypher Board interconnect,
board-identification strap) - see `design/Electronics/Cypher-Output/Design_Spec.md`. Only lens
count/layout, `plain-bits` allocation, and `BOARD_ROLE_ID_OUT` value (plus the custom-support
switch, unique to this variant) differ between variants.

---

## 2. Lens Layout

* **Layout:** QWERTY-style, mirroring the 64-Character Cypher-Input keyboard layout 1:1 for the
  40 cipher-path lens positions - see `Cypher-Input/Cypher_Input_64_Char_Design.md §2`. The two
  Shift key positions and the Space/Enter key positions on the paired keyboard have no
  corresponding lens here (unpopulated keepout) - Shift has no cipher output of its own to
  display (it only changes which physical letter/digit lens lights, per Cypher-Input's own
  colour-switching behaviour - see `Cypher-Input/Cypher_Input_64_Char_Design.md §5`), and
  Space/Enter are non-cipher keys with nothing to display.

> **Placeholder layout (provisional):** mirrors the placeholder layout in
> `Cypher-Input/Cypher_Input_64_Char_Design.md §2`, to be superseded once the user's own mock
> layout and renders are added to the repository.

```text
  1   2   3   4   5   6   7   8   9   0   +   /
    Q   W   E   R   T   Y   U   I   O   P
      A   S   D   F   G   H   J   K   L
          Z   X   C   V   B   N   M
```

* **Lens count:** 40 (26 letters + 10 digits + 2 base64-extra symbols; no Shift, Space, or Enter
  lens positions).

---

## 3. `plain-bits` Allocation

| Range | Assignment |
| :--- | :--- |
| PB[0:25] | 26 letter lens positions, position-for-position matching Cypher-Input's own 64-Character `plain-bits` allocation |
| PB[26:35] | 10 digit lens positions (case-invariant) |
| PB[36:37] | 2 base64-extra symbol lens positions: `+` and `/` |
| PB[38:39] | Unused - Cypher-Input's own PB[38:39] carry the 2 Shift keys, which have no corresponding lens position on this board (see §2) |
| PB[40:63] | Unused - spare plain-bit positions |

> Provisional pending Quartus pin-planning and PCB layout on the ENC module side. See
> `Design_Spec.md §3` for the common ENC module interface and full J1 zig-zag pin map
> (`Board_Layout.md §1`). **LED colour and brightness are received entirely as a broadcast from
> Cypher-Input and never use any `plain-bits` position** - see `Design_Spec.md §1`.

---

## 4. Board Identification and Custom-Support Switch

* **`BOARD_ROLE_ID_OUT[3:0]` strap value:** `0b0111` (Characters + Numbers + Special) by default;
  `0b1111` (adds Custom, bit3) when SW1 is switched to its custom-support position - see
  `Cypher/Board_Layout.md §4` encoding table and `Cypher/Design_Spec.md §3a` for the compatibility
  rule this affects.

### SW1 - Custom-Support Switch Circuit

A single user-accessible panel-mount SPDT switch controls `BOARD_ROLE_ID_OUT[3]` (bit3, Custom):

* **SW1 = SPDT, panel-mount, top face** - placed in the keyless keepout zone that mirrors
  Cypher-Input's own RV1 "keyboard settings" panel location (per `Design_Spec.md §1`/§2), since
  this is the only variant with a user-facing configuration control on this board.
* **Wiring:** common pin -> `BOARD_ROLE_ID_OUT[3]` (Cypher Board interconnect `J4`/`J6` pin 28,
  tied both connectors - see `Board_Layout.md §4`); one throw -> GND (default position, bit3=0,
  strap value `0b0111`); other throw -> 3V3_ENIG (custom-support position, bit3=1, strap value
  `0b1111`).
* **R_CUST (0 Ohm, DNF - Do Not Fit):** wired in parallel with SW1's 3V3_ENIG throw, so a user
  building a permanently-custom lightboard variant can fit this 0 Ohm link instead of relying on
  the switch position, hardwiring bit3=1 without needing SW1 present at all. Not fitted by
  default (SW1 alone determines the strap state in the standard build).
* **Not part of the JLCPCB PCBA order** - SW1 is hand-soldered by the user after the
  bare-assembled board is delivered, the same way Cypher-Input's own RV1 is (see `Design_Spec.md
  §2` Architecture). R_CUST, if fitted, would be a rear-face (L4) component within JLCPCB's
  standard SMT pass, but is not populated by default.

---

## 5. Bill of Materials (64-Char Variant-Specific Components)

Variant-specific components for the 64-Character variant. Common components shared across all
Cypher-Output variants are listed in **`design/Electronics/Cypher-Output/Design_Spec.md` §10**.

| RefDes | Specification | MPN | Manufacturer | DigiKey PN | Mouser PN | JLCPCB PN | Alt Supplier + PN | Notes | Footprint Available | Footprint Downloaded | Qty |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D1-D40 | RGB SMD LED (placeholder - MPN TBD, same part as Cypher-Input, pending confirmation) | TBD | TBD | - | - | - | - | One per lens position (40: 26 letters + 10 digits + 2 symbols); colour/brightness received entirely as a broadcast (no local generation); top face - **not populated in PCBA**, hand-soldered by the user after delivery (see `Design_Spec.md §2` Architecture) | - | - | 40 |
| R1-R40 (Red) | 0402, value TBD pending LED part confirmation | TBD | TBD | - | - | - | - | Red channel current-limit | - | - | 40 |
| R1-R40 (Green) | 0402, value TBD pending LED part confirmation | TBD | TBD | - | - | - | - | Green channel current-limit | - | - | 40 |
| R1-R40 (Blue) | 0402, value TBD pending LED part confirmation | TBD | TBD | - | - | - | - | Blue channel current-limit | - | - | 40 |
| Q1-Q40 | N-channel MOSFET, SOT-23 | 2N7002K | onsemi (or equiv.) | - | - | - | - | Per-position LED select, gated by that position's decoded `plain-bits` line; see `Design_Spec.md §4` | ✔ | - | 40 |
| SW1 | SPDT switch, panel-mount | TBD | TBD | - | - | - | - | Custom-support strap switch for `BOARD_ROLE_ID_OUT[3]`; top face - **not populated in PCBA**, hand-soldered by the user after delivery; exact supplier part TBD at schematic capture (same sourcing approach as other panel-mount controls, e.g. Cypher-Input RV1) | - | - | 1 |
| R_CUST | 0 Ohm link, 0402, **Do Not Fit (DNF)** | TBD | TBD | - | - | - | - | Optional permanent bit3=1 hardwire, in parallel with SW1's 3V3_ENIG throw; not populated by default - see §4 | - | - | 0 (DNF) |

> **Sourcing status:** Q1-Q40 has confirmed sourcing (same part as the 26-Char Classic and
> 10-Numeric variants). **Two items remain pending exact supplier PN confirmation at schematic
> capture:** SW1 (panel-mount SPDT switch part) and R_CUST (any generic 0 Ohm 0402 link, DNF -
> lowest priority since it is not populated by default).
