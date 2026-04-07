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

> This design spec will be developed further during the Mechanical Design phase.
