# Cypher-Output Board - 10-Numeric Variant Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-08-16
**Parent Document:** `design/Electronics/Cypher-Output/Design_Spec.md`

---

## 1. Overview

This document specifies the **10-Numeric** variant of the Enigma-NG Cypher-Output Board. It
mirrors the 10-Numeric Cypher-Input Board's number-pad layout 1:1 for the 10 digit positions;
the Space and Enter key positions on the paired keyboard have no corresponding lens on this
board, since they are non-cipher keys with nothing to display.

All three Cypher-Output variants (26-Char Classic, 64-Character, 10-Numeric) share an identical
circuit topology (ENC module mount, per-position LED indicator bank, Cypher Board interconnect,
board-identification strap) - see `design/Electronics/Cypher-Output/Design_Spec.md`. Only lens
count/layout, `plain-bits` allocation, and `BOARD_ROLE_ID_OUT` value differ between variants.

---

## 2. Lens Layout

* **Layout:** common number-pad grid (4 rows x 3 columns), mirroring the 10-Numeric Cypher-Input
  keyboard layout 1:1 for the 10 digit positions - see
  `Cypher-Input/Cypher_Input_10_Numeric_Design.md §2`. The Space and Enter key positions on the
  paired keyboard have no corresponding lens here (unpopulated keepout):

  ```text
  [ 7 ] [ 8 ] [ 9 ]
  [ 4 ] [ 5 ] [ 6 ]
  [ 1 ] [ 2 ] [ 3 ]
  [ - ] [ 0 ] [ - ]
  ```

* **Lens count:** 10 (digit lenses only).
* **Non-cipher positions:** None. Unlike Cypher-Input's own Space/Enter keys (which are read via
  I2C for CM5 UI clarity), there is nothing to *display* for those keys, so no lens or select
  circuitry exists at those two grid positions on this board - they are simply unpopulated
  keepout, matching the mechanical keycap layout without a corresponding illuminated indicator.

---

## 3. `plain-bits` Allocation

| Range | Assignment |
| :--- | :--- |
| PB[0:9] | 10 lens-position select outputs (digits 0-9), position-for-position matching Cypher-Input's own 10-Numeric `plain-bits` allocation |
| PB[10:63] | Unused - spare plain-bit positions |

> Provisional pending Quartus pin-planning and PCB layout on the ENC module side. See
> `Design_Spec.md §3` for the common ENC module interface and full J1 zig-zag pin map
> (`Board_Layout.md §1`). **LED colour and brightness are received entirely as a broadcast from
> Cypher-Input and never use any `plain-bits` position** - see `Design_Spec.md §1`.

---

## 4. Board Identification

* **`BOARD_ROLE_ID_OUT[3:0]` strap value:** `0b0010` (Numbers only; fixed, no switch; see
  `Cypher/Board_Layout.md §4` encoding table).

This variant has no custom-support switch - only the 64-Character variant carries one (see
`Cypher_Output_64_Char_Design.md §4`).

---

## 5. Bill of Materials (10-Numeric Variant-Specific Components)

Variant-specific components for the 10-Numeric variant. Common components shared across all
Cypher-Output variants are listed in **`design/Electronics/Cypher-Output/Design_Spec.md` §10**.

| RefDes | Specification | MPN | Manufacturer | DigiKey PN | Mouser PN | JLCPCB PN | Alt Supplier + PN | Notes | Footprint Available | Footprint Downloaded | Qty |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D1-D10 | RGB SMD LED (placeholder - MPN TBD, same part as Cypher-Input, pending confirmation) | TBD | TBD | - | - | - | - | One per lens position (10 digits); colour/brightness received entirely as a broadcast (no local generation); top face - **not populated in PCBA**, hand-soldered by the user after delivery (see `Design_Spec.md §2` Architecture) | - | - | 10 |
| R1-R10 (Red) | 0402, value TBD pending LED part confirmation | TBD | TBD | - | - | - | - | Red channel current-limit | - | - | 10 |
| R1-R10 (Green) | 0402, value TBD pending LED part confirmation | TBD | TBD | - | - | - | - | Green channel current-limit | - | - | 10 |
| R1-R10 (Blue) | 0402, value TBD pending LED part confirmation | TBD | TBD | - | - | - | - | Blue channel current-limit | - | - | 10 |
| Q1-Q10 | N-channel MOSFET, SOT-23 | 2N7002K | onsemi (or equiv.) | - | - | - | - | Per-position LED select, gated by that position's decoded `plain-bits` line; see `Design_Spec.md §4` | ✔ | - | 10 |
