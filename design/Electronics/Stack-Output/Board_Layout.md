# Stack-Output Board V1.0 Pinout Reference

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-07-12

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

> **Connector Definition Owner:** Cypher Board `Board_Layout.md §3` (J4 — Stack-Output/REF-side).
> This board carries the mating male connector (QTS-025-01-L-D-RA-P);
> the Cypher Board carries the female receptacle (QSS-025-01-L-D-A-GP-K).

For the defined 24-contact top signal region (ENC data return + TTD_RETURN), see
`Cypher/Board_Layout.md §3`.
The remaining contacts (bottom power region: 3V3_ENIG + GND) are pending full 50-contact
allocation: see todo `merge-cypher-board-j3j6-pinouts`.

---

## 2. J2 — Rear Stacking Connector (QSS-025-01-L-D-RA-K)

> **Connector Definition Owner:** Cypher Board `Board_Layout.md §3` (J4 — Stack-Output / REF-side).
> Same signal pinout as Cypher Board J4; right-angle variant for board-edge mounting.
> Mates with next mini-stack J1 (front stacking male) or Stack-Blanking Board male connector.

Same 24-contact top signal region as Cypher Board J4; see `Cypher/Board_Layout.md §3` for the
signal listing. Bottom power region (3V3_ENIG + GND passthrough) mirrors J1 and is pending full
50-contact allocation: see todo `merge-cypher-board-j3j6-pinouts`.

---

## 3. J3 / J4 / J5 — ROT Board Input Connectors

> **Connector Definition Owner:** `Rotor/Design_Spec.md §3.4`.

| Ref | MPN | Pins | Role |
| :--- | :--- | :--- | :--- |
| J3 | ERF8-005-05.0-S-DV-K-TR | 10 (2×5, 0.8mm) | JTAG from last ROT (TTD, TCK, TMS, CPLD_RESET_N) |
| J4 | ERF8-005-05.0-S-DV-K-TR | 10 (2×5, 0.8mm) | Power from last ROT — all pins NC |
| J5 | ERF8-010-05.0-S-DV-K-TR | 20 (2×10, 0.8mm) | ENC data from last ROT |

---

## 4. J6 — Passive Interposer Link (2BHR-30-VUA)

> **Connector Definition Owner:** `Stack-Interposer/Board_Layout.md` (TBD — board not yet created).

| Ref | MPN | Pins | Role |
| :--- | :--- | :--- | :--- |
| J6 | 2BHR-30-VUA | 30 (2×15, 2.54mm) | SIG-BLOCK-A/D ENC data + SIG-BLOCK-E TTD ↔ Stack-Input via Stack-Interposer Board |

---

## Diagram Reference

See `design/Diagrams/cypher-system-layout.drawio` and renders in `design/Diagrams/renders/`
for the system-level layout showing the Stack-Output Board position within the Rotor Mini-Stack.
