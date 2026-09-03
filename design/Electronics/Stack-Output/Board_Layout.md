# Stack-Output Board V1.0 Pinout Reference

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-09-02

> **Board_Layout.md is a visualisation-only document.** Design narrative, specifications, and
> component rationale belong in `Design_Spec.md`. This file contains connector pinout references
> and board orientation notes only.

---

## Orientation Convention

- **Front face / left edge:** J1 QTS-025 male stacking connector — faces Cypher Board J4 or
  previous mini-stack rear.
- **Rear face / right edge:** J2 QSS-025 female stacking connector — faces next mini-stack or
  Stack-Blanking Board.
- **Rotor-facing face:** J3/J4/J5 ERF8 sockets — connects to last ROT board output in the
  mini-stack.
- **Bottom edge:** J6 2BHR-30-VUA 30-pin THT male header — passive interposer link to
  Stack-Interposer Board.

---

## 1. J1 — Front Stacking Connector (QTS-025-01-L-D-RA-P)

> **Connector Definition Owner:** this board (IC-REF-CHAIN, per DEC-094). This template is
> reused identically at every junction along the REF-side chain: Cypher `J4`, this board's own
> `J1`/`J2`, and every subsequent mini-stack's `J1`/`J2`, terminating at the Stack-Blanking Board.
> This board carries the mating male connector (QTS-025-01-L-D-RA-P); the Cypher Board
> and every other mating board carry the female receptacle (QSS-025-01-L-D-A-GP-K).

**Fully 50-pin allocated** per DEC-092/DEC-093. Pin numbering: column Cn, top pin = 2n-1, bottom
pin = 2n; center GND bar at column 13 (pins 25/26). This is the canonical IC-REF-CHAIN pin map —
identical at every instance of this connector (Cypher `J4`, and every mini-stack's `J1`/`J2`).

| Top Row Signal | Top Row Pin# | Bottom Row Pin# | Bottom Row Signal |
| :--- | :---: | :---: | :--- |
| **3V3_ENIG** | 1 | 2 | **3V3_ENIG** |
| **3V3_ENIG** | 3 | 4 | **3V3_ENIG** |
| GND | 5 | 6 | GND |
| **ENC_IN[0] (return)** | 7 | 8 | **ENC_IN[1] (return)** |
| **ENC_IN[2] (return)** | 9 | 10 | **ENC_IN[3] (return)** |
| **ENC_IN[4] (return)** | 11 | 12 | **ENC_IN[5] (return)** |
| GND | 13 | 14 | GND |
| GND | 15 | 16 | **ACTUATE_REQUEST_REF_IN_N** |
| GND | 17 | 18 | GND |
| GND | 19 | 20 | GND |
| GND | 21 | 22 | GND |
| GND | 23 | 24 | GND |
| GND (bar) | 25 | 26 | GND (bar) |
| GND | 27 | 28 | GND |
| GND | 29 | 30 | **TTD_RETURN** |
| GND | 31 | 32 | GND |
| GND | 33 | 34 | GND |
| **ACTUATE_REQUEST_REF_OUT_N** | 35 | 36 | GND |
| GND | 37 | 38 | GND |
| **ENC_OUT[5] (return)** | 39 | 40 | **ENC_OUT[4] (return)** |
| **ENC_OUT[3] (return)** | 41 | 42 | **ENC_OUT[2] (return)** |
| **ENC_OUT[1] (return)** | 43 | 44 | **ENC_OUT[0] (return)** |
| GND | 45 | 46 | GND |
| **3V3_ENIG** | 47 | 48 | **3V3_ENIG** |
| **3V3_ENIG** | 49 | 50 | **3V3_ENIG** |

> **This board's own wiring at J1 (front):** `3V3_ENIG` (8 pins) feeds this board's own
> `3V3_ENIG` entry (C1-C5 decoupling bank per `Design_Spec.md DR-EXT-13`); no `5V_MAIN` on this
> board (`DR-SOUT-07`). `ENC_IN[5:0]`/`ENC_OUT[5:0]` (return) and `TTD_RETURN` per existing §3
> Signal Return Path wiring. `ACTUATE_REQUEST_REF_IN_N` (pin 16): passive J2→J1 passthrough
> (mirrors SIG-BLOCK-B/F direction). `ACTUATE_REQUEST_REF_OUT_N` (pin 35): passive J1→J2
> passthrough (mirrors SIG-BLOCK-C direction). No active components — this board has no CPLD/MCU.
> ESD via U4 (DEC-095). See DEC-093, DEC-095.

---

## 2. J2 — Rear Stacking Connector (QSS-025-01-L-D-RA-K)

> **Connector Definition Owner:** this board (IC-REF-CHAIN, §1 above — same template, I/O
> inverted). Mates with next mini-stack J1 (front stacking male) or Stack-Blanking Board male
> connector.

Same canonical IC-REF-CHAIN pin map as J1 (§1 above), with I/O directions inverted
(chain-through). This board's own wiring at J2 (rear): power/ENC-return/TTD_RETURN passthrough
per existing §3 Signal Return Path wiring; `ACTUATE_REQUEST_REF_IN_N`/`REF_OUT_N` passive
passthrough per DEC-095 (see note above).

---

## 3. J3 / J4 / J5 — ROT Board Input Connectors

> **Connector Definition Owner:** `Rotor/Design_Spec.md §3.4`.

| Ref | MPN | Pins | Role |
| :--- | :--- | :--- | :--- |
| J3 | ERF8-005-05.0-S-DV-K-TR | 10 (2×5, 0.8mm) | JTAG from last ROT (TTD, TCK, TMS, CPLD_RESET_N) |
| J4 | ERF8-005-05.0-S-DV-K-TR | 10 (2×5, 0.8mm) | Power from last ROT — all pins NC |
| J5 | ERF8-010-05.0-S-DV-K-TR | 20 (2×10, 0.8mm) | ENC data from last ROT, plus ACTUATE_REQUEST_OUT_N/IN_N (pins 13/14, per DEC-093 — see `Rotor/Design_Spec.md §3.4`); ESD via U9 (DEC-095) |

---

## 4. J6 — Passive Interposer Link (2BHR-30-VUA)

> **Connector Definition Owner:** `Stack-Interposer/Board_Layout.md §1`.

| Ref | MPN | Pins | Role |
| :--- | :--- | :--- | :--- |
| J6 | 2BHR-30-VUA | 30 (2×15, 2.54mm) | SIG-BLOCK-A/D ENC data + SIG-BLOCK-E TTD + SIG-BLOCK-G/H ACTUATE_REQUEST (per DEC-093) ↔ Stack-Input via Stack-Interposer Board |

---

## Diagram Reference

See `design/Diagrams/cypher-system-layout.drawio` and renders in `design/Diagrams/renders/`
for the system-level layout showing the Stack-Output Board position within the Rotor Mini-Stack.
