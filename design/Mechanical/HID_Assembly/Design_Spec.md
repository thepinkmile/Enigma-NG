# HID Assembly — Mechanical Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v0.1.0 (migrated from Keyboard/Design_Spec.md)
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-14

---

## 1. Overview

A mechanical keyboard assembly with one switch per character. Each switch is wired to one spade
terminal on the Encoder Board. The Encoder PCB is co-located with the keyboard panel within this
assembly.

---

## 2. Keyboard Switches

* **Keyboard Switches (×64):** DPDT 6-pin momentary push-button switches, one per key position.
  * Mounted in the keyboard panel (mechanical chassis); connect to the Encoder PCB via a
    field-installable spade-terminal harness.
  * **Pole 1 — COM1 + NO1** provides the active-low key path: COM1 → assigned Encoder input
    **BT65–BT128**, NO1 → local **GND** return. Pressing the key pulls the Encoder input LOW.
  * **Pole 2 pins (3×)** are unused electrically and may be retained only for mechanical anchoring;
    **no connection to the Encoder electrical netlist**.
  * **NC1** → not connected.
  * Keys connect only to the keyboard side of the Encoder board; there is no direct switch
    connection to the Lightboard.
  * Part: DPDT 2-pole 6-pin push button switch — purchased (gadgetkingdom, eBay, 2 per pack).

---

## 3. Key Panel Layout

64-key QWERTY panel layout: standard QWERTY + Numbers + Symbols + Shift (64 keys total), arranged
as a mechanical keyboard panel. Physical layout mirrors a standard QWERTY keyboard extended to the
full 64-character set.

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
