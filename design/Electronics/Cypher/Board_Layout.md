# Cypher Board V1.0 Pinout Reference

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

- **Front face:** faces the first Rotor Mini-Stack.
- **Back face:** carries ENC module mounts (J7–J18), spade blade terminal bank (J20+), and the
  CTL dock connectors (J1/J2).
- **STA side:** the edge where J3 (Stack-Input / STA-side QSS-025 female) is mounted.
- **REF side:** the edge where J4 (Stack-Output / REF-side QSS-025 female) is mounted.

---

## 1. J1 / J2 — Controller Dock (Molex 2195620015)

> **Connector Definition Owner:** `Controller/Board_Layout.md`.
> This board uses the plug (Molex 2195620015) mating with the CTL receptacle (Molex 2195630015).

- **J1:** 5V-biased power dock. 4x 5V_MAIN blades, 1x GND blade, USB D+/D- (TBD pin allocation).
- **J2:** Logic dock. 4x 3V3_ENIG blades, 1x GND blade; JTAG (TCK, TMS, TDI, TTD_RETURN), I2C (SDA, SCL).

---

## 2. J3 — Stack-Input / STA-Side Stacking Connector (QSS-025-01-L-D-A-GP-K)

> **Connector Definition Owner:** this board.
> Stack-Input Board front face carries the mating male QTS-025-01-L-D-RA-P.

26 contacts defined (see Design_Spec §3 Port Mapping). Pins 27–50 tied to GND.
Full 50-pin allocation pending: see todo `merge-cypher-board-j3j6-pinouts`.

| R1 Signal | Pin R1 | Pin R2 | R2 Signal |
| :--- | :---: | :---: | :--- |
| GND | 1 | 14 | GND |
| ENC_OUT[0] | 2 | 15 | ENC_OUT[1] |
| ENC_OUT[2] | 3 | 16 | ENC_OUT[3] |
| ENC_OUT[4] | 4 | 17 | ENC_OUT[5] |
| GND | 5 | 18 | GND |
| TMS | 6 | 19 | TCK |
| GND | 7 | 20 | CPLD_RESET_N |
| TTD (TDI out) | 8 | 21 | GND |
| GND | 9 | 22 | GND |
| ENC_IN[4] | 10 | 23 | ENC_IN[5] |
| ENC_IN[2] | 11 | 24 | ENC_IN[3] |
| ENC_IN[0] | 12 | 25 | ENC_IN[1] |
| GND | 13 | 26 | GND |

---

## 3. J4 — Stack-Output / REF-Side Stacking Connector (QSS-025-01-L-D-A-GP-K)

> **Connector Definition Owner:** this board.
> Stack-Output Board front face carries the mating male QTS-025-01-L-D-RA-P.

24 contacts defined (see Design_Spec §4 Signal Turnaround). Pins 25–50 tied to GND.
Full 50-pin allocation pending: see todo `merge-cypher-board-j3j6-pinouts`.

| R1 Signal | Pin R1 | Pin R2 | R2 Signal |
| :--- | :---: | :---: | :--- |
| GND | 1 | 13 | GND |
| ENC_IN[0] (return) | 2 | 14 | ENC_IN[1] (return) |
| ENC_IN[2] (return) | 3 | 15 | ENC_IN[3] (return) |
| ENC_IN[4] (return) | 4 | 16 | ENC_IN[5] (return) |
| GND | 5 | 17 | GND |
| TTD_RETURN | 6 | 18 | GND |
| GND | 7 | 19 | TTD_RETURN |
| GND | 8 | 20 | GND |
| ENC_OUT[4] (return) | 9 | 21 | ENC_OUT[5] (return) |
| ENC_OUT[2] (return) | 10 | 22 | ENC_OUT[3] (return) |
| ENC_OUT[0] (return) | 11 | 23 | ENC_OUT[1] (return) |
| GND | 12 | 24 | GND |

---

## 4. J5 / J6 — Cypher-Input and Cypher-Output Connectors (QTS-025-01-L-D-A-GP-K-TR)

> **Connector Definition Owner:** this board.
> Cypher-Input and Cypher-Output bottom edges carry the mating female QSS-025-01-L-D-RA-K.

50 contacts. Pin numbering: top row column Cn = pin 2n-1;
bottom row column Cn = pin 2n. GREEN_PWM_N and YELLOW_PWM_N are NC on this board.

| Top row signal | Top pin | Bottom pin | Bottom row signal |
| :--- | :---: | :---: | :--- |
| 3V3_ENIG | 1 | 2 | 3V3_ENIG |
| JTAG_TCK_FWD | 3 | 4 | ENC_DATA_BOT[5] |
| ENC_ACTIVE_INPUT_N | 5 | 6 | GND |
| JTAG_TMS_FWD | 7 | 8 | ENC_DATA_BOT[4] |
| GND | 9 | 10 | GND |
| CPLD_RESET_N_FWD | 11 | 12 | ENC_DATA_BOT[3] |
| GND | 13 | 14 | GND |
| JTAG_TDI_FWD | 15 | 16 | ENC_DATA_BOT[2] |
| GND | 17 | 18 | GND |
| GREEN_PWM_N (NC) | 19 | 20 | ENC_DATA_BOT[1] |
| BOARD_ROLE_ID_TOP | 21 | 22 | GND |
| I2C_SCL_PASS | 23 | 24 | ENC_DATA_BOT[0] |
| GND_WEDGE | 25 | 26 | GND_WEDGE |
| ENC_DATA_TOP[0] | 27 | 28 | I2C_SDA_PASS |
| GND | 29 | 30 | BOARD_ROLE_ID_BOT |
| ENC_DATA_TOP[1] | 31 | 32 | YELLOW_PWM_N (NC) |
| GND | 33 | 34 | GND |
| ENC_DATA_TOP[2] | 35 | 36 | JTAG_TDO_RET |
| GND | 37 | 38 | GND |
| ENC_DATA_TOP[3] | 39 | 40 | CPLD_RESET_N_RET |
| GND | 41 | 42 | GND |
| ENC_DATA_TOP[4] | 43 | 44 | JTAG_TMS_RET |
| GND | 45 | 46 | ENC_ACTIVE_OUTPUT_N |
| ENC_DATA_TOP[5] | 47 | 48 | JTAG_TCK_RET |
| 3V3_ENIG | 49 | 50 | 3V3_ENIG |

> BOARD_ROLE_ID_TOP / BOARD_ROLE_ID_BOT: driven by the Cypher-Input / Cypher-Output top connectors
> (ID_TOP = 3V3_ENIG or GND per board type). NC on the bottom connector of both boards.

---

## 5. J7–J18 — ENC Module Mounts (back face)

Four Hirose DF40C-xDS receptacle sets. Each mount:

| Position | Connector | MPN | Pins | Role |
| :--- | :--- | :--- | :--- | :--- |
| A (left) | J7 / J10 / J13 / J16 | DF40C-90DS-0.4V(51) | 90 | plain-bits[63:0] |
| B (centre) | J8 / J11 / J14 / J17 | DF40C-24DS-0.4V(51) | 24 | cypher-bits + JTAG + ENC_ACTIVE_N |
| C (right) | J9 / J12 / J15 / J18 | DF40C-10DS-0.4V(51) | 10 | 3V3_ENIG power |

Pin assignments per connector follow the ENC Module Interface definition in `Design_Spec.md §6 J7–J18`.

---

## 6. J19 — USM Harness (B6B-PH-K-S)

| Pin | Signal |
| :--- | :--- |
| 1 | 3V3_ENIG |
| 2 | 5V_MAIN |
| 3 | GND |
| 4 | SDA |
| 5 | SCL |
| 6 | GND |

---

## 7. J20+ — Spade Blade Terminal Bank (back face)

64 Keystone 1285-ST spade blade terminals required per ENC module mount position
(4 mounts = 256 terminals total). Full component details and RefDes allocation:
see `Design_Spec.md §6 J20+` and `§11 BOM`. Physical arrangement on board is TBD at
schematic time.

---

## Diagram Reference

See `design/Diagrams/cypher-system-layout.drawio` and renders in `design/Diagrams/renders/`
for the system-level layout diagram showing the Cypher Board's position within the
Rotor Mini-Stack assembly.
