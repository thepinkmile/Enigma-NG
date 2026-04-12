# Rotor Board — 64-Character Variant Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-XX
**Parent Document:** `design/Electronics/Rotor/Design_Spec.md`

---

## 1. Overview

This document specifies the 64-character (6-bit) variant of the Enigma-NG Smart Digital Rotor.
This variant supports the extended Enigma-NG character set (64 characters) and is the primary
variant for the Enigma-NG system. It is not compatible with original Enigma machines (which use
26-character rotors) but can coexist with 26-character variant rotors in a mixed stack.

Both 26-character and 64-character rotor variants share identical PCB footprints, connector
pinouts, and DIP switch mechanisms. A mixed stack is fully supported at the hardware level.

---

## 2. Character Set and Data Bus

* **Character count:** 64
* **Data bus width:** 6 bits (ENC[0:5]); all 6 bits are active on this variant
* **Encoding:** Binary, 0–63 mapping to the Enigma-NG extended character set (to be defined in
  the VHDL / software design specification; see OWI-003)
* **Connector bus:** ERM8-010 / ERF8-010 (6-bit footprint); all 12 signal pins on J3/J6 active.

---

## 3. UFM Map Storage and SW2/SW3 Selection

The CPLD UFM stores 21 forward-direction cipher maps in the common 64-entry × 6-bit format.
Each map defines a valid permutation of {0..63}.

The direction bit on SW2/SW3 allows any stored map to be applied in reverse (inverse lookup),
giving 42 effective cipher configurations per side without additional UFM storage.

### UFM Capacity

| Parameter | Value |
| :--- | :--- |
| EPM240T100I5N UFM capacity | 8,192 bits |
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

## 4. Wiring Maps

The 64-character Enigma-NG wiring tables are not derived from historical sources and will be
defined in the VHDL design specification (see OWI-003). Each map must satisfy:

1. Complete bijection (permutation) of {0..63} — no character maps to itself (derangement).
2. Forward and inverse are mathematically linked; the inverse is obtained via the SW direction
   bit — no separate inverse map needs to be stored.
3. Notch trigger position(s) for each map must be defined in the VHDL tables.

Up to 21 distinct forward maps can be stored, each usable in both forward and reverse direction.

> To use a map as a standard forward/return pair: set SW2 to index N, direction 0 (forward);
> set SW3 to index N, direction 1 (reverse). Non-matching index or direction combinations are
> valid and produce a more complex compound cipher.

---

## 5. Ring Setting (SW1)

See `Design_Spec.md §2.3` for the SW1 hardware description.
For the 64-character variant:

* The AS5600 6-bit reading maps directly to positions 0–63 (full 6-bit range is valid).
* SW1[5:0] is summed **modulo 64** with the AS5600 reading to yield the effective position.
* Notch trigger positions are defined per map in the VHDL tables (see OWI-003).

---

## 6. Prototype Build Note

Both 26-character and 64-character rotor sets will be built for the prototype. Initial wiring
maps will be generated using the STGC\_Generator tool
(`design/Electronics/Rotor/STGC_Generator.py`) and loaded into each 64-character rotor's UFM
at first JTAG programming. SW2 and SW3 are then used to select map index and direction
independently at runtime.
