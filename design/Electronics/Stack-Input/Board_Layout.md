# Stack-Input Board V1.0 Pinout Reference

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-07-05

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

> **Connector Definition Owner:** Cypher Board `Board_Layout.md §2` (J3 — Stack-Input/STA-side).
> This board carries the mating male connector (QTS-025-01-L-D-RA-P);
> the Cypher Board carries the female receptacle (QSS-025-01-L-D-A-GP-K).

For the defined 26-contact top signal region (ENC data + JTAG), see `Cypher/Board_Layout.md §2`.
The remaining 24 contacts (bottom power/control region: 3V3_ENIG, 5V_MAIN, GND, ENC_ACTIVE_N,
CPLD_RESET_N, ACTUATE_REQUEST_N) are pending full 50-contact allocation:
see todo `merge-cypher-board-j3j6-pinouts`.

---

## 2. J2 — Rear Stacking Connector (QSS-025-01-L-D-RA-K)

> **Connector Definition Owner:** this board.
> Mating pinout mirrors Cypher Board `Board_Layout.md §2` (J3 signal set) with I/O inverted.
> Mates with next mini-stack J1 (front stacking male) or Stack-Blanking Board male connector.

Same 26-contact top signal region as J1 with I/O directions inverted (chain-through);
see `Cypher/Board_Layout.md §2` for the signal listing. Bottom 24-contact power/control region
(3V3_ENIG, 5V_MAIN, GND, ENC_ACTIVE_N, CPLD_RESET_N, ACTUATE_REQUEST_N output from last ROT
carry) is pending full 50-contact allocation: see todo `merge-cypher-board-j3j6-pinouts`.

---

## 3. J3 / J4 / J5 — ROT Board Output Connectors

> **Connector Definition Owner:** `Rotor/Design_Spec.md §3.4`.

| Ref | MPN | Pins | Role |
| :--- | :--- | :--- | :--- |
| J3 | ERF8-005-05.0-S-DV-K-TR | 10 (2×5, 0.8mm) | JTAG to ROT 1 |
| J4 | ERF8-005-05.0-S-DV-K-TR | 10 (2×5, 0.8mm) | Power to ROT 1 (board pins NC — power via J4 from stack) |
| J5 | ERF8-010-05.0-S-DV-K-TR | 20 (2×10, 0.8mm) | ENC data to ROT 1 |

---

## 4. J6 — Stack-Interposer Return Link (SQT-115-01-L-D-RA)

> **Connector Definition Owner:** `Stack-Interposer/Board_Layout.md`.

| Ref | MPN | Pins | Role |
| :--- | :--- | :--- | :--- |
| J6 | SQT-115-01-L-D-RA | 30 (2×15, 2.54mm) | TTD_RETURN + ENC_DATA return from Stack-Output via Interposer |

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
