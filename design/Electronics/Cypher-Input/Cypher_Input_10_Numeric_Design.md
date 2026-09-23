# Cypher-Input Board - 10-Numeric Variant Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-09-21
**Parent Document:** `design/Electronics/Cypher-Input/Design_Spec.md`

---

## 1. Overview

This document specifies the **10-Numeric** variant of the Enigma-NG Cypher-Input Board. It
provides a dedicated numeric-entry keyboard: 10 digit keys (0-9) arranged in a common number-pad
layout, plus Space and Enter for CM5 UI input clarity. There is no Shift key on this variant - the
digit character set has no case distinction.

All three Cypher-Input variants (26-Char Classic, 64-Character, 10-Numeric) share an identical
circuit topology (ENC module mount, LED indicator bank, Cypher Board interconnect, USM
interconnect, board-identification strap plus a shared non-cipher-key I2C expander) - see
`design/Electronics/Cypher-Input/Design_Spec.md`. Only key count/layout, LED/resistor/socket
quantities, `plain-bits` allocation, and `BOARD_ROLE_ID` value differ between variants.

---

## 2. Key Layout and Character Set

* **Layout:** common number-pad grid (4 rows x 3 columns), matching familiar calculator/numeric
  keypad ordering:

  ```text
  [ 7 ] [ 8 ] [ 9 ]
  [ 4 ] [ 5 ] [ 6 ]
  [ 1 ] [ 2 ] [ 3 ]
  [Spc] [ 0 ] [Ent]
  ```

* **Key count:** 12 total (10 digit keys, case-invariant + Space + Enter, both non-cipher).
* **Non-cipher keys:** Space and Enter, same role as on the 64-Character variant - present for
  CM5 UI input clarity only, read via the on-board I2C GPIO expander (U4), never entering the
  cipher pipeline.

---

## 3. `plain-bits` Allocation

| Range | Assignment |
| :--- | :--- |
| PB[0:9] | 10 digit keys (0-9, case-invariant) |
| PB[10:63] | Unused - spare plain-bit positions |

> Provisional pending Quartus pin-planning and PCB layout on the ENC module side. See
> `Design_Spec.md §3` for the common ENC module interface and full J4 zig-zag pin map
> (`Board_Layout.md §1`). Space and Enter are **not** part of this bus - see §4 below. **LED
> colour selection never uses any `plain-bits` position** - colour is sourced entirely from the
> User Settings Module, see §5.

---

## 4. Board Identification and Non-Cipher Key I/O

* **`BOARD_ROLE_ID[3:0]` strap value:** `0b0010` (Numbers only; see `Cypher/Board_Layout.md §4`
  encoding table).
* **U4 (PCA9534A) I2C address:** `0x38`, the single fixed address shared by all Cypher-Input
  variants (see `Design_Spec.md §3a`). 2 of 8 GPIO used for Space/Enter; 6 GPIO spare.

---

## 5. LED Indicator Behaviour

Colour and illumination values (four independent styles) are stored and configured entirely on the
User Settings Module and delivered to this board on the common `J3` connector
(`RED_DRIVE_{1,2,3,4}_N`/`GREEN_DRIVE_{1,2,3,4}_N`/`BLUE_DRIVE_{1,2,3,4}_N`/
`ILLUMINATION_DRIVE_{1,2,3,4}_N` - see `Design_Spec.md §5`/§6 and
`User_Settings_Module/Design_Spec.md`). This variant has no Shift key and carries no dedicated
local colour-selection circuit of its own.

LED count matches total physical keyswitches (12: 10 digits + Space + Enter), so Space and Enter
also carry an indicator LED even though they are not part of the cipher pipeline.

---

## 6. Bill of Materials (10-Numeric Variant-Specific Components)

Variant-specific components for the 10-Numeric variant. Common components shared across all
Cypher-Input variants are listed in **`design/Electronics/Cypher-Input/Design_Spec.md` §11**.

| RefDes | Specification | MPN | Manufacturer | DigiKey PN | Mouser PN | JLCPCB PN | Alt Supplier + PN | Notes | Footprint Available | Footprint Downloaded | Qty |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D1-D12 | RGB SMD LED (placeholder - MPN TBD, pending user confirmation of a part that fits under Cherry MX2A-71NB) | TBD | TBD | - | - | - | - | One per key (10 digits + Space + Enter); colour source is the User Settings Module (see `Design_Spec.md §5`); top face - **not populated in PCBA**, hand-soldered by the user after delivery (see `Design_Spec.md §2` Architecture) | - | - | 12 |
| R1-R12 (Red) | 0402, value TBD pending LED part confirmation | TBD | TBD | - | - | - | - | Red channel current-limit | - | - | 12 |
| R1-R12 (Green) | 0402, value TBD pending LED part confirmation | TBD | TBD | - | - | - | - | Green channel current-limit | - | - | 12 |
| R1-R12 (Blue) | 0402, value TBD pending LED part confirmation | TBD | TBD | - | - | - | - | Blue channel current-limit | - | - | 12 |
| SW1-SW12 | Mechanical keyswitch hot-swap socket, THT (rear-mount) | PG151101S11 | Kailh | - | - | C41430893 (consignment) | - | Hot-swap socket for Cherry MX2A-71NB (not populated - see below) | ✔ | ✔ | 12 |

**Not part of the PCBA (sourced and installed separately):**

| Item | MPN | Manufacturer | DigiKey PN | Mouser PN | Notes | Qty |
| --- | --- | --- | --- | --- | --- | --- |
| Mechanical keyswitch | MX2A-71NB | Cherry | 1644-MX2A-71NB-ND | 540-MX2A-71NB | Snap-fit into hot-swap sockets; JLCPCB global sourcing/consignment or Amazon (prototyping) | 12 |
