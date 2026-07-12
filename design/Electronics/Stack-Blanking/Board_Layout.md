# Stack-Blanking Board V1.0 Pinout Reference

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

- **Right side (J1):** Stack-Input mating connector — mates with Stack-Input Board J2 (rear
  stacking connector) in normal use, or Cypher Board J3 for transport.
- **Left side (J2):** Stack-Output mating connector — mates with Stack-Output Board J2 (rear
  stacking connector) in normal use, or Cypher Board J4 for transport.
- **Signal routing:** all bridging traces run on inner layers L2/L3 (right-to-left, J1 → J2).
- **Termination resistors R1–R5:** placed close to J1 (Stack-Input side).

---

## 1. J1 — Stack-Input Mating Connector (QTS-025-01-L-D-A-GP-K-TR)

> **Connector Definition Owner:** Cypher Board `Board_Layout.md §2` (J3 — Stack-Input / STA-side).
> Same signal pinout as Cypher Board J3.
> Mates with Stack-Input Board J2 (QSS-025-01-L-D-RA-K) in normal use;
> mates with Cypher Board J3 (QSS-025-01-L-D-A-GP-K) for transport / bench testing.

For the top 26-contact signal region (ENC data + JTAG), see `Cypher/Board_Layout.md §2`.
Bottom 24-contact power/control region is pending full 50-contact allocation:
see todo `merge-cypher-board-j3j6-pinouts`.

At this board, the following signals from J1 are **terminated** (not routed to J2):

| Signal | Termination |
| :--- | :--- |
| ENC_ACTIVE_N | R1 — 10 kΩ pull-up to 3V3_ENIG |
| TCK | R2 — 10 kΩ pull-down to GND |
| TMS | R3 — 10 kΩ pull-up to 3V3_ENIG |
| CPLD_RESET_N | R4 — 10 kΩ pull-up to 3V3_ENIG |
| ACTUATE_REQUEST_N | R5 — 10 kΩ pull-up to 3V3_ENIG |
| 5V_MAIN | NC — no connection |

---

## 2. J2 — Stack-Output Mating Connector (QTS-025-01-L-D-A-GP-K-TR)

> **Connector Definition Owner:** Cypher Board `Board_Layout.md §3` (J4 — Stack-Output / REF-side).
> Same signal pinout as Cypher Board J4.
> Mates with Stack-Output Board J2 (QSS-025-01-L-D-RA-K) in normal use;
> mates with Cypher Board J4 (QSS-025-01-L-D-A-GP-K) for transport / bench testing.

For the top 24-contact signal region (ENC data return + TTD_RETURN), see `Cypher/Board_Layout.md §3`.
Bottom power region (3V3_ENIG + GND) mirrors J1 bottom.

---

## 3. Signal Bridge Summary

| Trace | J1 contact | J2 contact | Signal Block |
| :--- | :--- | :--- | :--- |
| ENC_OUT[5:0] (fwd) | J1 ENC_OUT[5:0] out | J2 ENC_IN[5:0] in | SIG-BLOCK-A → B |
| ENC_OUT[5:0] (ref) | J1 ENC_IN[5:0] in | J2 ENC_OUT[5:0] out | SIG-BLOCK-C → D |
| TTD → TTD_RETURN | J1 TTD out | J2 TTD_RETURN ×2 in | SIG-BLOCK-E → F |
| 3V3_ENIG | J1 power section | J2 power section | SIG-BLOCK-I |
| GND | J1 power section | J2 power section | Return |

---

## Diagram Reference

See `design/Diagrams/cypher-system-layout.drawio` and renders in `design/Diagrams/renders/`
for the system-level layout showing the Stack-Blanking Board position at the rear of the last
Rotor Mini-Stack.
