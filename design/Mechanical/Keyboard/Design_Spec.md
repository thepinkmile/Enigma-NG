# Keyboard (V1.0) Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-07

## 1. Overview

A mechanical keyboard assembly with one switch per character. Each switch is wired to one spade terminal on the Encoder Board.

## 2. Keyboard Switches

* **Keyboard Switches (×64):** DPDT 6-pin momentary push-button switches, one per key position.
  * Mounted in the keyboard panel (mechanical chassis); connect to the Encoder PCB via a field-installable spade-terminal harness.
  * **Pole 1 — COM1 + NO1** → key-press signal path to CPLD input (Row 3 spade bank BT129–BT192 COM, BT193–BT256 NO).
  * **Pole 2 pins (3×)** → mechanically soldered to PCB for physical key anchoring only; **no electrical connection**.
  * **NC1** → not connected.
  * Keys connect only to the keyboard side of the Encoder board; there is no direct switch connection to the Lightboard.
  * Part: DPDT 2-pole 6-pin push button switch — purchased (gadgetkingdom, eBay, 2 per pack).

## 3. Key Mapping (64-Way QWERTY)

The Encoder CPLD maps 64 mechanical key inputs to the parallel 6-bit data bus. Key assignments follow
a standard QWERTY layout extended with numbers, symbols, and modifier keys.

* **Layout:** Standard QWERTY + Numbers + Symbols + Shift (64 keys total).
* **Debouncing:** Hardware RC de-bounce circuit per input line: 10 kΩ pull-up resistor to 3V3_ENIG +
  100 nF X7R capacitor to GND on each key input line.
  > ⚠️ **Open item:** EPM240T100I5N Schmitt trigger input capability and internal weak pull-up strength
  > to be verified by hardware test on development board before finalising external pull-up value.
* **Shift Logic:** The Left Shift and Right Shift keys act as logic-level triggers for the CPLD state
  machine, toggling between the lower and upper character planes of the 64-way key map.
* **LED Drive:** The Encoder CPLDs directly drive the **Shift Status LEDs** and the 64-character lamp
  matrix output via MOSFET arrays.

> **Cross-reference:** For Encoder PCB spade terminal pinout and CPLD I/O allocation, see
> `design/Electronics/Encoder/Design_Spec.md §4 Interconnects` and `§3 Dual-Role Architecture`.

