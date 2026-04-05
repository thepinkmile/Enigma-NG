# Extension Board Layout Visualisations

**Status:** Draft
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-05

---

## Component Areas

```text
TOP VIEW (L1) - 4-Layer / 2oz Copper / ENIG
 _____________________________________________________________________________
|                                                                             |
|   [ J1: EXTENSION PORT IN ] <--- 16-pin 2×8 shrouded, from previous stage  |
|                                                                             |
|   [ BULK DECOUPLING ] <--- 5x 10uF X7R star/spoke near J1                  |
|                                                                             |
|   [ ROTOR INTERFACE CONNECTORS ] <--- 3 connectors per rotor slot (×5)     |
|   (Samtec CLP female sockets — positionally identical to Stator J2–J4)     |
|                                                                             |
|   [ DIAGNOSTIC BANK ] <--- 2x8 ENIG Gold Probe Pads                        |
|                                                                             |
|   [ J2: EXTENSION PORT OUT ] <--- 16-pin 2×8 shrouded, to next stage       |
|                                                                             |
|   [ DATA PLATE ] <--- Inverted White Silkscreen on L4                      |
|_____________________________________________________________________________|
```

---

## J1 — Extension Port IN (16-Pin 2×8)

> **Connector Definition Owner:** `Stator/Board_Layout.md — J5`.
> This board uses the mating connector on J1. See BOM for part number.
> Authoritative pinout: Pin 1 = 3V3_ENIG, Pin 2 = SYS_RESET_N, Pins 3–8 = ENC_IN[0:5],
> Pins 9–14 = ENC_OUT[0:5], Pin 15 = TDO_RETURN, Pin 16 = GND.

---

## J2 — Extension Port OUT (16-Pin 2×8)

> **Connector Definition Owner:** `Stator/Board_Layout.md — J5`.
> This board uses the mating connector on J2. Carries the same signals as J1, passed through.
> See BOM for part number.

---

## J3–J8 — Rotor Interface Connectors (Specification Pending)

> **Connector Definition Owner:** `Rotor/Board_Layout.md — Rotor Interface Connectors`.
> This board hosts the mating connectors for 5 rotor positions (3 connectors per position = 15 connectors total).
> Mechanical finalisation and part numbers are pending. Must be positionally identical to Stator J2–J4.

---

## Diagnostic Bank (J9)

2×8 ENIG Gold probe pad bank for mid-stack signal validation. 2.54mm pitch. Not a separate connector;
probed directly with logic analyser clips.
