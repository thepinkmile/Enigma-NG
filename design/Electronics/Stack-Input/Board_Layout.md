# Stack-Input Board V1.0 Pinout Reference

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

- **Front face / right edge:** J1 QTS-025 male stacking connector — faces Cypher Board J3 or
  previous mini-stack rear.
- **Rear face / left edge:** J2 QSS-025 female stacking connector — faces next mini-stack or
  Stack-Blanking Board.
- **Rotor-facing face:** J3/J4/J5 ERF8 sockets — connects to first ROT board in the mini-stack.
- **Bottom edge:** J6 SQT-115 right-angle female — Stack-Interposer return link.
- **Service headers:** J7–J10, SW1, SW2 — accessible for service.
  J7 = solenoid loom; J8 = dual position switch loom; J9 = SWD programming; J10 = UART/BOOT0.

---

## 1. J1 — Front Stacking Connector (QTS-025-01-L-D-RA-P)

> **Connector Definition Owner:** this board (IC-STA-CHAIN, per DEC-094). This template is
> reused identically at every junction along the STA-side chain: Cypher `J3`, this board's own
> `J1`/`J2`, and every subsequent mini-stack's `J1`/`J2`, terminating at the Stack-Blanking Board.
> This board carries the mating male connector (QTS-025-01-L-D-RA-P); the Cypher Board
> and every other mating board carry the female receptacle (QSS-025-01-L-D-A-GP-K).

**Fully 50-pin allocated** per DEC-090/DEC-093. Pin numbering: column Cn, top pin = 2n-1, bottom
pin = 2n; center GND bar at column 13 (pins 25/26), matching the `J5`/`J6` board-agnostic
template convention. This is the canonical IC-STA-CHAIN pin map — identical at every instance of
this connector (Cypher `J3`, and every mini-stack's `J1`/`J2`).

| Top Row Signal | Top Row Pin# | Bottom Row Pin# | Bottom Row Signal |
| :--- | :---: | :---: | :--- |
| **3V3_ENIG** | 1 | 2 | **3V3_ENIG** |
| **3V3_ENIG** | 3 | 4 | **3V3_ENIG** |
| GND | 5 | 6 | GND |
| **ENC_IN[0]** | 7 | 8 | **ENC_IN[1]** |
| **ENC_IN[2]** | 9 | 10 | **ENC_IN[3]** |
| **ENC_IN[4]** | 11 | 12 | **ENC_IN[5]** |
| GND | 13 | 14 | GND |
| GND | 15 | 16 | **ACTUATE_REQUEST_IN_N** |
| GND | 17 | 18 | GND |
| GND | 19 | 20 | GND |
| **TCK** | 21 | 22 | GND |
| GND | 23 | 24 | **TMS** |
| GND (bar) | 25 | 26 | GND (bar) |
| **CPLD_RESET_N** | 27 | 28 | GND |
| GND | 29 | 30 | **TTD (TDI out)** |
| GND | 31 | 32 | GND |
| GND | 33 | 34 | GND |
| **ACTUATE_REQUEST_OUT_N** | 35 | 36 | GND |
| GND | 37 | 38 | GND |
| **ENC_OUT[5]** | 39 | 40 | **ENC_OUT[4]** |
| **ENC_OUT[3]** | 41 | 42 | **ENC_OUT[2]** |
| **ENC_OUT[1]** | 43 | 44 | **ENC_OUT[0]** |
| GND | 45 | 46 | GND |
| **5V_MAIN** | 47 | 48 | **5V_MAIN** |
| **5V_MAIN** | 49 | 50 | **5V_MAIN** |

> **This board's own wiring at J1 (front):**

| Pin | Signal | Wiring on this board |
| :--- | :--- | :--- |
| 1-4 | 3V3_ENIG | Local 3V3_ENIG entry (C1-C5 decoupling bank) |
| 16 | ACTUATE_REQUEST_IN_N | Forward pass: received from Cypher/previous mini-stack, → U1 (STM32G071) — triggers this board's solenoid actuation |
| 35 | ACTUATE_REQUEST_OUT_N | Return pass: delivers the signal received on this board's own J2 pin 16 (after routing through this mini-stack's Rotor/Stack-Output/Stack-Interposer chain in reverse) onward to the previous mini-stack or Cypher's J3, where CPLD U1 reads it as a round-trip completion check. See DEC-093, DEC-097. |
| 47-50 | 5V_MAIN | Local 5V_MAIN entry (C6-C10 decoupling bank) |
| all other pins | GND, or existing ENC data/JTAG signals (see `Design_Spec.md §3`) | — |

---

## 2. J2 — Rear Stacking Connector (QSS-025-01-L-D-RA-K)

> **Connector Definition Owner:** this board (IC-STA-CHAIN, §1 above — same template, I/O
> inverted). Mates with next mini-stack J1 (front stacking male) or Stack-Blanking Board male
> connector.

Same canonical IC-STA-CHAIN pin map as J1 (§1 above), with I/O directions inverted
(chain-through). This board's own wiring at J2 (rear):

| Pin | Signal | Wiring on this board |
| :--- | :--- | :--- |
| 1-4 | 3V3_ENIG | Power passthrough from J1 |
| 16 | ACTUATE_REQUEST_IN_N | Return pass: received from the next mini-stack or Stack-Blanking Board, routed via this mini-stack's Stack-Interposer/Stack-Output/Rotor chain (reverse order) to this board's own J1 pin 35 |
| 35 | ACTUATE_REQUEST_OUT_N | Forward pass: sourced from this mini-stack's own Rotor 1-5 chain via Stack-Output and the Stack-Interposer Board (J6); drives next mini-stack's J1 pin 16, or the Stack-Blanking Board. See DEC-093. |
| 39-44 | ENC_OUT[0:5] | Forward-path passthrough |
| 47-50 | 5V_MAIN | Power passthrough from J1 |
| all other pins | GND | Tied to GND |

---

## 3. J3 / J4 / J5 — ROT Board Output Connectors

> **Connector Definition Owner:** `Rotor/Design_Spec.md §3.4`.

| Ref | MPN | Pins | Role |
| :--- | :--- | :--- | :--- |
| J3 | ERF8-005-05.0-S-DV-K-TR | 10 (2×5, 0.8mm) | JTAG to ROT 1 |
| J4 | ERF8-005-05.0-S-DV-K-TR | 10 (2×5, 0.8mm) | Power to ROT 1 (board pins NC — power via J4 from stack) |
| J5 | ERF8-010-05.0-S-DV-K-TR | 20 (2×10, 0.8mm) | ENC data to ROT 1, plus ACTUATE_REQUEST_IN_N/OUT_N (per DEC-093 — see `Rotor/Design_Spec.md §3.4`) |

---

## 4. J6 — Stack-Interposer Return Link (SQT-115-01-L-D-RA)

> **Connector Definition Owner:** `Stack-Interposer/Board_Layout.md`.

| Ref | MPN | Pins | Role |
| :--- | :--- | :--- | :--- |
| J6 | SQT-115-01-L-D-RA | 30 (2×15, 2.54mm) | TTD_RETURN + ENC_DATA return from Stack-Output via Interposer, plus the ACTUATE_REQUEST forward-collect/return-inject hop signals (per DEC-093) |

---

## 5. J7 — Solenoid Loom (PH1-05-UA)

| Pin | Signal |
| :--- | :--- |
| 1 | 5V_MAIN |
| 2 | GND |
| 3 | SOLENOID_DRIVE |
| 4 | GND |
| 5 | 5V_MAIN |

---

## 6. J8 — Position Switch Loom — Dual (PH1-05-UA)

| Pin | Signal |
| :--- | :--- |
| 1 | ACTUATION_HOME_N (retracted position) |
| 2 | GND |
| 3 | GND |
| 4 | GND |
| 5 | ACTUATION_EXTENDED_N (fully-extended position) |

---

## 7. J9 — SWD Header (PH1-05-UA)

| Pin | Signal |
| :--- | :--- |
| 1 | 3V3_ENIG (VTref) |
| 2 | SWCLK |
| 3 | GND |
| 4 | SWDIO |
| 5 | RESET_N |

---

## 8. J10 — UART / BOOT0 Header (PH1-05-UA)

| Pin | Signal |
| :--- | :--- |
| 1 | GND |
| 2 | 3V3_ENIG |
| 3 | UART_TX |
| 4 | UART_RX |
| 5 | BOOT0 |

---

## Diagram Reference

See `design/Diagrams/cypher-system-layout.drawio` and renders in `design/Diagrams/renders/`
for the system-level layout showing the Stack-Input Board position within the Rotor Mini-Stack.
