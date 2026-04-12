# Rotor Board — 26-Character Variant Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-XX
**Parent Document:** `design/Electronics/Rotor/Design_Spec.md`

---

## 1. Overview

This document specifies the 26-character (5-bit) variant of the Enigma-NG Smart Digital Rotor.
This variant emulates original Enigma machine rotor wiring for a 26-character alphabet (A–Z),
and is compatible with historical rotor types I–VIII, Beta, and Gamma.

Both 26-character and 64-character rotor variants share identical PCB footprints, connector
pinouts, and DIP switch mechanisms. A mixed stack is fully supported.

---

## 2. Character Set and Data Bus

* **Character count:** 26 (A–Z)
* **Data bus width:** 5 bits (ENC[0:4]); ENC[5] is NC on this variant
* **Encoding:** Binary, 0 = 'A', 1 = 'B', …, 25 = 'Z'
* **Connector bus:** ERM8-010 / ERF8-010 (6-bit footprint for cross-variant compatibility);
  ENC[5] pins are NC on all 26-character rotor boards.

---

## 3. UFM Map Storage and SW2/SW3 Selection

The CPLD UFM stores 21 forward-direction cipher maps in the common 64-entry × 6-bit format.
For the 26-character variant, each map defines a valid permutation of {0..25} in entries 0–25;
entries 26–63 are unused by this variant.

The direction bit on SW2/SW3 allows any stored map to be applied in reverse (inverse lookup),
giving 42 effective cipher configurations per side without additional UFM storage.

### UFM Capacity

| Parameter | Value |
| :--- | :--- |
| EPM570T100I5N UFM capacity | 8,192 bits |
| Map format (common to both variants) | 64 entries × 6 bits = 384 bits per map |
| Maps stored | floor(8,192 / 384) = **21 forward maps** |
| Effective configurations per side (with direction bit) | 21 × 2 = **42** |

### SW2 / SW3 Bit Encoding

| Bits | Function | Values |
| :--- | :--- | :--- |
| [4:0] | Map index | 0–20 valid; 21–31 reserved |
| [5] | Direction | 0 = forward; 1 = reverse (inverse lookup) |

SW2 and SW3 are read at power-up only; a power cycle is required after changing either switch.

---

## 4. Historical Rotor Wiring Tables

The following historical Enigma rotor wiring maps are pre-programmed into all 26-character
variant rotors at first JTAG programming. Each rotor type occupies one UFM map index (forward
wiring only; the inverse is obtained via the direction bit).

| Map Index | Rotor Name | Notes |
| :--- | :--- | :--- |
| 0 | Rotor I | Wehrmacht / Luftwaffe |
| 1 | Rotor II | Wehrmacht / Luftwaffe |
| 2 | Rotor III | Wehrmacht / Luftwaffe |
| 3 | Rotor IV | Wehrmacht |
| 4 | Rotor V | Wehrmacht |
| 5 | Rotor VI | Kriegsmarine |
| 6 | Rotor VII | Kriegsmarine |
| 7 | Rotor VIII | Kriegsmarine |
| 8 | Beta | Kriegsmarine 4-rotor (never rotates) |
| 9 | Gamma | Kriegsmarine 4-rotor (never rotates) |
| 10–20 | Custom / Reserved | Available for Enigma-NG extended use |

> To emulate e.g. Rotor I: set SW2 to index 0, direction 0 (forward) for the forward pass;
> set SW3 to index 0, direction 1 (reverse) for the return pass.
>
> The actual wiring permutation data for each historical rotor is defined in the VHDL
> design files (see OWI-003).

---

## 5. Ring Setting (SW1)

See `Design_Spec.md §2.3` for the SW1 hardware description.
For the 26-character variant:

* The AS5600 6-bit reading maps to positions 0–25 (26 valid positions). Readings of 26–63
  indicate a between-character position and are flagged as a mechanical fault via I2C telemetry.
* SW1[5:0] is summed **modulo 26** with the AS5600 reading to yield the effective position.
* Notch trigger positions are defined per map in the VHDL tables (see OWI-003).

---

## 6. Prototype Build Note

Both 26-character and 64-character rotor sets will be built for the prototype. All 10 historical
rotor maps (indices 0–9) will be programmed into each 26-character rotor at first JTAG
programming. SW2 and SW3 are then used to select rotor type and direction independently at
runtime.
