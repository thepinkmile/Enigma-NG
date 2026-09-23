# Cypher-Input Board - 64-Character Variant Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-09-21
**Parent Document:** `design/Electronics/Cypher-Input/Design_Spec.md`

---

## 1. Overview

This document specifies the **64-Character** variant of the Enigma-NG Cypher-Input Board. It
supports the extended Enigma-NG cipher alphabet: 26 letters + 10 digits + 2 base64-extra symbols
(`+`/`/`), realised via Shift for uppercase (RFC 4648 base64 alphabet: `A-Z`, `a-z`, `0-9`, `+`,
`/`). Space and Enter are present for CM5 UI input clarity but are **not** part of the cipher
alphabet.

All three Cypher-Input variants (26-Char Classic, 64-Character, 10-Numeric) share an identical
circuit topology (ENC module mount, LED indicator bank, Cypher Board interconnect, USM
interconnect, board-identification strap plus a shared non-cipher-key I2C expander) - see
`design/Electronics/Cypher-Input/Design_Spec.md`. Only key count/layout, LED/resistor/socket
quantities, `plain-bits` allocation, and `BOARD_ROLE_ID` value differ between variants.

---

## 2. Key Layout and Character Set

* **Layout:** QWERTY-style. 26 letters + 10 digits + 2 base64-extra symbols (`+`, `/`) + 2 Shift
  (Left/Right) + Space + Enter.
* **Key count:** 42 total (40 cipher-path + 2 non-cipher: Space, Enter).
* **Character set composition:** the 64-character (base64) cipher alphabet is realised as 26
  physical letter keys (doubling as uppercase via Shift = 52 letter values) + 10 physical digit
  keys (case-invariant) + 2 physical base64-extra symbol keys (case-invariant) = 64 cipher values,
  driven by 40 cipher-path signals on the ENC module `plain-bits` bus. Space and Enter are read via
  the on-board I2C GPIO expander (U4), not the `plain-bits` bus, so they never enter the cipher
  pipeline.

> **Placeholder layout (provisional):** the arrangement below is an initial placeholder only,
> to be superseded once the user's own mock layout and renders (produced with an external
> keyboard-layout tool) are added to the repository. Key positions, row groupings, and Shift/Space/
> Enter placement are all subject to change.

```text
  1   2   3   4   5   6   7   8   9   0   +   /
    Q   W   E   R   T   Y   U   I   O   P
      A   S   D   F   G   H   J   K   L
  SHIFT   Z   X   C   V   B   N   M   SHIFT
              [ SPACE ]         [ENTER]
```

---

## 3. `plain-bits` Allocation

| Range | Assignment |
| :--- | :--- |
| PB[0:25] | 26 letter keys (case realised via Shift - see Shift rows below) |
| PB[26:35] | 10 digit keys (case-invariant) |
| PB[36:37] | 2 base64-extra symbol keys: `+` and `/` (case-invariant; RFC 4648 base64 alphabet) |
| PB[38:39] | 2 Shift keys (Left/Right) |
| PB[40:63] | Unused - spare plain-bit positions |

> Provisional pending Quartus pin-planning and PCB layout on the ENC module side. See
> `Design_Spec.md §3` for the common ENC module interface and full J4 zig-zag pin map
> (`Board_Layout.md §1`). Space and Enter are **not** part of this bus - see §4 below. **LED
> colour selection never uses any `plain-bits` position** - colour is sourced entirely from the
> User Settings Module, see §5.

---

## 4. Board Identification and Non-Cipher Key I/O

* **`BOARD_ROLE_ID[3:0]` strap value:** `0b0111` (Characters + Numbers + Special; bit3 Custom
  not populated on this board - see `Cypher/Board_Layout.md §4` encoding table and
  `Cypher/Design_Spec.md §3a`).
* **U4 (PCA9534A) I2C address:** `0x38`, the single fixed address shared by all Cypher-Input
  variants (see `Design_Spec.md §3a`). Used on this variant for Space/Enter UI-only key readback
  only - see `Design_Spec.md §3a`.

---

## 5. LED Indicator Behaviour

Colour and illumination values (four independent styles) are stored and configured entirely on the
User Settings Module and delivered to this board on the common `J3` connector
(`RED_DRIVE_{1,2,3,4}_N`/`GREEN_DRIVE_{1,2,3,4}_N`/`BLUE_DRIVE_{1,2,3,4}_N`/
`ILLUMINATION_DRIVE_{1,2,3,4}_N` - see `Design_Spec.md §5`/§6 and
`User_Settings_Module/Design_Spec.md`). This variant carries no dedicated local colour-selection
circuit of its own.

LED count matches total physical keyswitches (42: 40 cipher-path + Space + Enter), so Space and
Enter also carry a colour-indicator LED even though they are not part of the cipher pipeline.

This is the only Cypher-Input variant with Shift keys. Shift is a **global** state, not a
per-key one: while either Shift key is held, all keys switch their baseline illumination from
Colour1 to Colour3 (Shift changes the `[a-z]` keys' cipher meaning to `[A-Z]`, so Colour3
indicates the board is in uppercase mode). The currently-pressed key still shows Colour2 on top
of whichever baseline (Colour1 or Colour3) is currently active. Which local circuit/CPLD
implementation realises this behaviour is not yet determined - see
`.copilot/todos/cypher-input-led-independent-rgb-pwm-review.md`.

---

## 6. Bill of Materials (64-Char Variant-Specific Components)

Variant-specific components for the 64-Character variant. Common components shared across all
Cypher-Input variants are listed in **`design/Electronics/Cypher-Input/Design_Spec.md` §11**.

| RefDes | Specification | MPN | Manufacturer | DigiKey PN | Mouser PN | JLCPCB PN | Alt Supplier + PN | Notes | Footprint Available | Footprint Downloaded | Qty |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D1-D42 | RGB SMD LED (placeholder - MPN TBD, pending user confirmation of a part that fits under Cherry MX2A-71NB) | TBD | TBD | - | - | - | - | One per key; colour source is the User Settings Module (see `Design_Spec.md §5`); top face - **not populated in PCBA**, hand-soldered by the user after delivery (see `Design_Spec.md §2` Architecture) | - | - | 42 |
| R1-R42 (Red) | 0402, value TBD pending LED part confirmation | TBD | TBD | - | - | - | - | Red channel current-limit | - | - | 42 |
| R1-R42 (Green) | 0402, value TBD pending LED part confirmation | TBD | TBD | - | - | - | - | Green channel current-limit | - | - | 42 |
| R1-R42 (Blue) | 0402, value TBD pending LED part confirmation | TBD | TBD | - | - | - | - | Blue channel current-limit | - | - | 42 |
| SW1-SW42 | Mechanical keyswitch hot-swap socket, THT (rear-mount) | PG151101S11 | Kailh | - | - | C41430893 (consignment) | - | Hot-swap socket for Cherry MX2A-71NB (not populated - see below) | ✔ | ✔ | 42 |

**Not part of the PCBA (sourced and installed separately):**

| Item | MPN | Manufacturer | DigiKey PN | Mouser PN | Notes | Qty |
| --- | --- | --- | --- | --- | --- | --- |
| Mechanical keyswitch | MX2A-71NB | Cherry | 1644-MX2A-71NB-ND | 540-MX2A-71NB | Snap-fit into hot-swap sockets; JLCPCB global sourcing/consignment or Amazon (prototyping) | 42 |
