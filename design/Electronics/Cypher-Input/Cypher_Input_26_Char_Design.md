# Cypher-Input Board - 26-Character Variant Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-09-21
**Parent Document:** `design/Electronics/Cypher-Input/Design_Spec.md`

---

## 1. Overview

This document specifies the **26-Char Classic** variant of the Enigma-NG Cypher-Input Board. It
mimics the original German Enigma machine keyboard: a QWERTZ layout of 26 letter keys only, with
no Shift, digit, symbol, Space, or Enter keys. This is the simplest Cypher-Input variant.

All three Cypher-Input variants (26-Char Classic, 64-Character, 10-Numeric) share an identical
circuit topology (ENC module mount, LED indicator bank, Cypher Board interconnect, USM
interconnect, board-identification strap plus a shared non-cipher-key I2C expander) - see
`design/Electronics/Cypher-Input/Design_Spec.md`. Only key count/layout, LED/resistor/socket
quantities, `plain-bits` allocation, and `BOARD_ROLE_ID` value differ between variants.

---

## 2. Key Layout and Character Set

* **Layout:** QWERTZ, 26 letter keys (A-Z), single case only (no Shift key).
* **Key count:** 26.
* **Non-cipher keys:** None (no Space or Enter on this variant).

The physical key arrangement mirrors the original German Enigma machine's three-row QWERTZ
layout (9 + 8 + 9 keys): the middle row is staggered half a key-width to the right of the top
row, and the bottom row realigns back under the top row (`P` sits under `Q`):

```text
  Q   W   E   R   T   Z   U   I   O
    A   S   D   F   G   H   J   K
  P   Y   X   C   V   B   N   M   L
```

---

## 3. `plain-bits` Allocation

| Range | Assignment |
| :--- | :--- |
| PB[0:25] | 26 letter keys, QWERTZ layout (no Shift - single case only, mimics the original Enigma) |
| PB[26:63] | Unused - spare plain-bit positions |

> Provisional pending Quartus pin-planning and PCB layout on the ENC module side. See
> `Design_Spec.md §3` for the common ENC module interface and full J4 zig-zag pin map
> (`Board_Layout.md §1`). **LED colour selection never uses any `plain-bits` position** - colour
> is sourced entirely from the User Settings Module, see §5.

---

## 4. Board Identification

* **`BOARD_ROLE_ID[3:0]` strap value:** `0b0001` (Characters only; see `Cypher/Board_Layout.md §4`
  encoding table).
* **U4 (PCA9534A) I2C address:** `0x38`, the single fixed address shared by all Cypher-Input
  variants (see `Design_Spec.md §3a`). No Space/Enter keys exist on this variant; all 8 GPIO spare.

---

## 5. LED Indicator Behaviour

Colour and illumination values (four independent styles) are stored and configured entirely on the
User Settings Module and delivered to this board on the common `J3` connector
(`RED_DRIVE_{1,2,3,4}_N`/`GREEN_DRIVE_{1,2,3,4}_N`/`BLUE_DRIVE_{1,2,3,4}_N`/
`ILLUMINATION_DRIVE_{1,2,3,4}_N` - see `Design_Spec.md §5`/§6 and
`User_Settings_Module/Design_Spec.md`). This variant has no Shift key and carries no dedicated
local colour-selection circuit of its own.

---

## 6. Bill of Materials (26-Char Variant-Specific Components)

Variant-specific components for the 26-Char Classic variant. Common components shared across all
Cypher-Input variants are listed in **`design/Electronics/Cypher-Input/Design_Spec.md` §11**.

| RefDes | Specification | MPN | Manufacturer | DigiKey PN | Mouser PN | JLCPCB PN | Alt Supplier + PN | Notes | Footprint Available | Footprint Downloaded | Qty |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D1-D26 | RGB SMD LED (placeholder - MPN TBD, pending user confirmation of a part that fits under Cherry MX2A-71NB) | TBD | TBD | - | - | - | - | One per key; colour source is the User Settings Module (see `Design_Spec.md §5`); top face - **not populated in PCBA**, hand-soldered by the user after delivery (see `Design_Spec.md §2` Architecture) | - | - | 26 |
| R1-R26 (Red) | 0402, value TBD pending LED part confirmation | TBD | TBD | - | - | - | - | Red channel current-limit | - | - | 26 |
| R1-R26 (Green) | 0402, value TBD pending LED part confirmation | TBD | TBD | - | - | - | - | Green channel current-limit | - | - | 26 |
| R1-R26 (Blue) | 0402, value TBD pending LED part confirmation | TBD | TBD | - | - | - | - | Blue channel current-limit | - | - | 26 |
| SW1-SW26 | Mechanical keyswitch hot-swap socket, THT (rear-mount) | PG151101S11 | Kailh | - | - | C41430893 (consignment) | - | Hot-swap socket for Cherry MX2A-71NB (not populated - see below) | ✔ | ✔ | 26 |

**Not part of the PCBA (sourced and installed separately):**

| Item | MPN | Manufacturer | DigiKey PN | Mouser PN | Notes | Qty |
| --- | --- | --- | --- | --- | --- | --- |
| Mechanical keyswitch | MX2A-71NB | Cherry | 1644-MX2A-71NB-ND | 540-MX2A-71NB | Snap-fit into hot-swap sockets; JLCPCB global sourcing/consignment or Amazon (prototyping) | 26 |
