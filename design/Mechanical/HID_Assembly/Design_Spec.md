# HID Assembly — Mechanical Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v0.1.0 (migrated from Keyboard/Design_Spec.md)
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-17

---

## 1. Overview

A mechanical keyboard and lightboard assembly using a QWERTY-derived 40-position HID layout to
access the system's 64-character code space. Each keyboard switch is wired to one spade terminal on
the Encoder Board. The Encoder PCB is co-located with the keyboard panel within this assembly.

---

## 2. Keyboard Switches

* **Keyboard Switches (×40):** DPDT 6-pin momentary push-button switches, one per physical HID key
  position.
  * Mounted in the keyboard panel (mechanical chassis); connect to the Encoder PCB via a
    field-installable spade-terminal harness.
  * **Pole 1 — COM1 + NO1** provides the active-low key path: COM1 → assigned Encoder input
    **BT65–BT128**, NO1 → local **GND** return. Pressing the key pulls the Encoder input LOW.
  * **Pole 2 pins (3×)** are unused electrically and may be retained only for mechanical anchoring;
    **no connection to the Encoder electrical netlist**.
  * **NC1** → not connected.
  * Keys connect only to the keyboard side of the Encoder board; there is no direct switch
    connection to the Lightboard.
  * Part: uxcell-style DPDT 2-pole 6-pin push button switch — purchased from seller
    `gadgetskingdom` (eBay item `365271584375`, 2 per pack). See
    `design/Datasheets/Gadgetskingdom_DPDT_Keyboard_Switch_Pseudo_Datasheet.md`.

---

## 3. Key Panel Layout

The HID assembly uses a **40-position physical layout** that preserves a conventional
QWERTY-inspired operator experience while still exposing the machine's full 64-character logical
alphabet.

* **Printable key positions (×38):** dedicated keycaps for `[a-z0-9+=]`.
* **Modifier key positions (×2):** one **Left Shift** key and one **Right Shift** key.
* **Bottom-row arrangement:** the two Shift keys flank the bottom row so either hand can access the
  uppercase alphabetic plane.
* **Uppercase behaviour:** there are **no separate uppercase-only key positions**. Holding either
  Shift key while pressing an alphabetic key yields the corresponding uppercase code (`A-Z`).
* **Lightboard mirroring:** the visible character layout on the lightboard mirrors the same
  QWERTY-derived printable positions instead of adding dedicated uppercase-only legends.

> For signal polarity, RC debounce circuit, Schmitt trigger configuration, Shift key state-machine
> logic, and LED drive specification, see `design/Electronics/Encoder/Design_Spec.md §6 Key Mapping`.

---

## 4. Mechanical Key Lever Interface

Each key has a mechanical lever extending downward from the key body to contact the depression bar
of the Rotor Actuation Assembly.

> See `design/Mechanical/Rotor_Actuation_Assembly/Design_Spec.md` for the depression bar and pivot
> lever mechanism that translates keypresses into rotor steps.

---

## 5. Cross-References

| Document | Description |
| :--- | :--- |
| `design/Electronics/Encoder/Design_Spec.md` | Encoder PCB spade terminal pinout, CPLD I/O allocation, key mapping electrical spec |
| `design/Mechanical/Rotor_Actuation_Assembly/Design_Spec.md` | Depression bar, pivot lever, and rotor stepping mechanism |
