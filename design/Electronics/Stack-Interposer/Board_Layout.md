# Stack-Interposer Board V1.0 Pinout Reference

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-07-25

> **Board_Layout.md is a visualisation-only document.** Design narrative, specifications, and
> component rationale belong in `Design_Spec.md`. This file contains connector pinout references
> and board orientation notes only.

---

## Orientation Convention

- The Stack-Interposer Board lies **horizontally** at the base of the Rotor Mini-Stack.
- The **Stack-Output Board** stands vertically on the **left side** — J1 (Stack-Output side)
  faces upward on that edge.
- The **Stack-Input Board** stands vertically on the **right side** — J2 (Stack-Input side)
  faces upward on that edge.
- Both J1 and J2 are straight/vertical connectors on the top surface of this board (no
  right-angle). The right-angle connectors on the Stack-Output and Stack-Input bottom edges mate
  downward into J1 and J2 respectively.

---

## 1. J1 — Stack-Output Mating Connector (TMMH-115-01-L-D-ES)

> **Connector Definition Owner:** this document (Stack-Interposer `Board_Layout.md §1`).
> Mates with Stack-Output Board J6 (SQT-115-01-L-D-RA right-angle female on Stack-Output bottom edge).
> MPN: TMMH-115-01-L-D-ES (Samtec 30-position 2×15 straight/vertical male).

All J1 contacts connect directly to the corresponding J2 contacts (pin n → pin n).
No signals are terminated or modified at this board.

---

## 2. J2 — Stack-Input Mating Connector (TMMH-115-01-L-D-ES)

> **Connector Definition Owner:** this document (Stack-Interposer `Board_Layout.md §2`).
> Mates with Stack-Input Board J6 (SQT-115-01-L-D-RA right-angle female on Stack-Input bottom edge).
> MPN: TMMH-115-01-L-D-ES (Samtec 30-position 2×15 straight/vertical male).

All J2 contacts connect directly to the corresponding J1 contacts (pin n → pin n).
No signals are terminated or modified at this board.

---

## 3. Pin Map — 2×15 Connector (applies to both J1 and J2)

The same signal assignment applies to both J1 and J2. Passive continuity: J1 pin n is connected
directly to J2 pin n by a trace on L2 or L3. Signal naming is from the perspective of the
Stack-Output Board (J1 side):

| Row 1 signal | Pin (Row 1, odd) | Pin (Row 2, even) | Row 2 signal |
| :--- | ---: | ---: | :--- |
| ENC_DATA[0] (SIG-BLOCK-A fwd) | 1 | 2 | GND |
| GND | 3 | 4 | ENC_DATA[1] (SIG-BLOCK-A fwd) |
| ENC_DATA[2] (SIG-BLOCK-A fwd) | 5 | 6 | GND |
| GND | 7 | 8 | ENC_DATA[3] (SIG-BLOCK-A fwd) |
| ENC_DATA[4] (SIG-BLOCK-A fwd) | 9 | 10 | GND |
| GND | 11 | 12 | ENC_DATA[5] (SIG-BLOCK-A fwd) |
| TTD (SIG-BLOCK-E) | 13 | 14 | GND |
| GND | 15 | 16 | GND |
| GND | 17 | 18 | TTD (SIG-BLOCK-E) |
| ENC_DATA[5] (SIG-BLOCK-D return) | 19 | 20 | GND |
| GND | 21 | 22 | ENC_DATA[4] (SIG-BLOCK-D return) |
| ENC_DATA[3] (SIG-BLOCK-D return) | 23 | 24 | GND |
| GND | 25 | 26 | ENC_DATA[2] (SIG-BLOCK-D return) |
| ENC_DATA[1] (SIG-BLOCK-D return) | 27 | 28 | GND |
| GND | 29 | 30 | ENC_DATA[0] (SIG-BLOCK-D return) |

> **Note:** Signal grouping and GND interleaving rationale is documented in
> `Stack-Interposer/Design_Spec.md §3`. SIG-BLOCK-A occupies pins 1–12 (top half),
> SIG-BLOCK-D occupies pins 19–30 (bottom half), both interleaved with GND.
> TTD (SIG-BLOCK-E) appears on pins 13 and 18 with guard GND on pins 14–17 between them.
>
> **Routing note (DR-SINT-04):** The pin mapping is pin-to-pin (J1 pin n → J2 pin n). However,
> because J1 and J2 both face upward with their pin-1 ends facing each other, the physical trace
> routes on L2/L3 will need to be laid out as if mirrored — traces will cross as they run across
> the board. Rows are preserved (row 1 → row 1, row 2 → row 2). This is a PCB routing
> constraint only; the electrical mapping is unchanged. See `Design_Spec.md §3`.

---

## Diagram Reference

See `design/Diagrams/cypher-system-layout.drawio` — page **"Mini-Stack Front View"** — and
`design/Diagrams/renders/03-Mini-Stack-Front-View.png` for the front-elevation view of the
Rotor Mini-Stack showing the Stack-Interposer Board position at the base.
