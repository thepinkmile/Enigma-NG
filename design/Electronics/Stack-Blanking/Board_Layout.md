# Stack-Blanking Board V1.0 Pinout Reference

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

- **Right side (J1):** Stack-Input mating connector — mates with Stack-Input Board J2 (rear
  stacking connector) in normal use, or Cypher Board J3 for transport.
- **Left side (J2):** Stack-Output mating connector — mates with Stack-Output Board J2 (rear
  stacking connector) in normal use, or Cypher Board J4 for transport.
- **Signal routing:** all bridging traces run on inner layers L2/L3 (right-to-left, J1 → J2, and
  left-to-right, J2 → J1, for the return-direction signals).
- **Termination resistors R1–R3:** placed close to J1 (Stack-Input side).

---

## 1. J1 — Stack-Input Mating Connector (QTS-025-01-L-D-A-GP-K-TR)

> **Connector Definition Owner:** `Stack-Input/Board_Layout.md §1` (IC-STA-CHAIN, per DEC-094).
> Same signal pinout as every Stack-Input `J1`/`J2`.
> Mates with Stack-Input Board J2 (QSS-025-01-L-D-RA-K) in normal use;
> mates with Cypher Board J3 (QSS-025-01-L-D-A-GP-K) for transport / bench testing.

Fully 50-pin allocated per DEC-090/DEC-093 — see `Stack-Input/Board_Layout.md §1` for the full
canonical pin map.

At this board, the following signals from J1 are **terminated** (not routed to J2):

| Signal | Termination |
| :--- | :--- |
| TCK | R1 — 10 kΩ pull-down to GND |
| TMS | R2 — 10 kΩ pull-up to 3V3_ENIG |
| CPLD_RESET_N | R3 — 10 kΩ pull-up to 3V3_ENIG |
| 5V_MAIN | NC — no connection |

The following signals are **bridged** to J2, not terminated (see §3 Signal Bridge Summary):
`ACTUATE_REQUEST_OUT_N` (→ J2 `ACTUATE_REQUEST_REF_IN_N`), `ACTUATE_REQUEST_IN_N` (← J2
`ACTUATE_REQUEST_REF_OUT_N`).

---

## 2. J2 — Stack-Output Mating Connector (QTS-025-01-L-D-A-GP-K-TR)

> **Connector Definition Owner:** `Stack-Output/Board_Layout.md §1` (IC-REF-CHAIN, per DEC-094).
> Same signal pinout as every Stack-Output `J1`/`J2`.
> Mates with Stack-Output Board J2 (QSS-025-01-L-D-RA-K) in normal use;
> mates with Cypher Board J4 (QSS-025-01-L-D-A-GP-K) for transport / bench testing.

Fully 50-pin allocated per DEC-092/DEC-093 — see `Stack-Output/Board_Layout.md §1` for the full
canonical pin map. Bottom power region (3V3_ENIG + GND) mirrors J1 bottom.

---

## 3. Signal Bridge Summary

| Trace | J1 contact | J2 contact | Signal Block |
| :--- | :--- | :--- | :--- |
| ENC_OUT[5:0] (fwd) | J1 ENC_OUT[5:0] out | J2 ENC_IN[5:0] in | SIG-BLOCK-A → B |
| ENC_OUT[5:0] (ref) | J1 ENC_IN[5:0] in | J2 ENC_OUT[5:0] out | SIG-BLOCK-C → D |
| TTD → TTD_RETURN | J1 TTD out | J2 TTD_RETURN ×2 in | SIG-BLOCK-E → F |
| ACTUATE_REQUEST_OUT_N → REF_IN_N | J1 ACTUATE_REQUEST_OUT_N in | J2 ACTUATE_REQUEST_REF_IN_N out | First turnaround (DEC-093/DEC-096) |
| ACTUATE_REQUEST_REF_OUT_N → IN_N | J1 ACTUATE_REQUEST_IN_N out | J2 ACTUATE_REQUEST_REF_OUT_N in | Second turnaround (DEC-093/DEC-096) |
| 3V3_ENIG | J1 power section | J2 power section | SIG-BLOCK-I |
| GND | J1 power section | J2 power section | Return |

---

## Diagram Reference

See `design/Diagrams/cypher-system-layout.drawio` and renders in `design/Diagrams/renders/`
for the system-level layout showing the Stack-Blanking Board position at the rear of the last
Rotor Mini-Stack.
