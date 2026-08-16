# Cypher-Output Board - 26-Character Variant Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-08-16
**Parent Document:** `design/Electronics/Cypher-Output/Design_Spec.md`

---

## 1. Overview

This document specifies the **26-Char Classic** variant of the Enigma-NG Cypher-Output Board. It
mirrors the 26-Char Classic Cypher-Input Board's QWERTZ layout, 1:1: 26 lens positions, one per
letter, with no positions for Shift, Space, or Enter (matching the paired keyboard's own lack of
those keys). This is the simplest Cypher-Output variant.

All three Cypher-Output variants (26-Char Classic, 64-Character, 10-Numeric) share an identical
circuit topology (ENC module mount, per-position LED indicator bank, Cypher Board interconnect,
board-identification strap) - see `design/Electronics/Cypher-Output/Design_Spec.md`. Only lens
count/layout, `plain-bits` allocation, and `BOARD_ROLE_ID_OUT` value differ between variants.

---

## 2. Lens Layout

* **Layout:** QWERTZ, 26 lens positions (A-Z), mirroring the 26-Char Classic Cypher-Input
  keyboard layout 1:1 - see `Cypher-Input/Cypher_Input_26_Char_Design.md §2`.
* **Lens count:** 26.
* **Non-cipher positions:** None (no Space or Enter lens on this variant, matching the paired
  keyboard).

The physical lens arrangement mirrors the same three-row QWERTZ layout (9 + 8 + 9 positions) as
the paired 26-Char Classic keyboard, per `Mechanical/Lightboard_Assembly/Design_Spec.md §2`:

```text
  Q   W   E   R   T   Z   U   I   O
    A   S   D   F   G   H   J   K
  P   Y   X   C   V   B   N   M   L
```

---

## 3. `plain-bits` Allocation

| Range | Assignment |
| :--- | :--- |
| PB[0:25] | 26 lens-position select outputs, QWERTZ layout, position-for-position matching Cypher-Input's own 26-Char Classic `plain-bits` allocation |
| PB[26:63] | Unused - spare plain-bit positions |

> Provisional pending Quartus pin-planning and PCB layout on the ENC module side. See
> `Design_Spec.md §3` for the common ENC module interface and full J1 zig-zag pin map
> (`Board_Layout.md §1`). **LED colour and brightness are received entirely as a broadcast from
> Cypher-Input and never use any `plain-bits` position** - see `Design_Spec.md §1`.

---

## 4. Board Identification

* **`BOARD_ROLE_ID_OUT[3:0]` strap value:** `0b0001` (Characters only; fixed, no switch; see
  `Cypher/Board_Layout.md §4` encoding table).

This variant has no custom-support switch - only the 64-Character variant carries one (see
`Cypher_Output_64_Char_Design.md §4`).

---

## 5. Bill of Materials (26-Char Variant-Specific Components)

Variant-specific components for the 26-Char Classic variant. Common components shared across all
Cypher-Output variants are listed in **`design/Electronics/Cypher-Output/Design_Spec.md` §10**.

| RefDes | Specification | MPN | Manufacturer | DigiKey PN | Mouser PN | JLCPCB PN | Alt Supplier + PN | Notes | Footprint Available | Footprint Downloaded | Qty |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D1-D26 | RGB SMD LED (placeholder - MPN TBD, same part as Cypher-Input, pending confirmation) | TBD | TBD | - | - | - | - | One per lens position; colour/brightness received entirely as a broadcast (no local generation); top face - **not populated in PCBA**, hand-soldered by the user after delivery (see `Design_Spec.md §2` Architecture) | - | - | 26 |
| R1-R26 (Red) | 0402, value TBD pending LED part confirmation | TBD | TBD | - | - | - | - | Red channel current-limit | - | - | 26 |
| R1-R26 (Green) | 0402, value TBD pending LED part confirmation | TBD | TBD | - | - | - | - | Green channel current-limit | - | - | 26 |
| R1-R26 (Blue) | 0402, value TBD pending LED part confirmation | TBD | TBD | - | - | - | - | Blue channel current-limit | - | - | 26 |
| Q1-Q26 | N-channel MOSFET, SOT-23 | 2N7002K | onsemi (or equiv.) | - | - | - | - | Per-position LED select, gated by that position's decoded `plain-bits` line; see `Design_Spec.md §4` | ✔ | - | 26 |
