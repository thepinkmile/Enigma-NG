# Plugboard Assembly — Mechanical Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v0.1.0 (migrated from Plugboard/Design_Spec.md)
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-14

---

## 1. Overview

A plugboard with dual ¼ inch jack sockets. Each socket is connected to one of the attached Encoder
Boards.

---

## 2. Functional Requirements

| ID | Functional Requirement | Notes | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| FR-PLG-01 | Accept encoder input signal via plugboard jack interface | 6.35 mm (¼″) mono switched jack (Tip + Switch contact; Sleeve to chassis GND) | See `design/Electronics/Encoder/Design_Spec.md` for Encoder Board interconnect details |

---

## 3. Design Requirements

| ID | Design Requirement | Specification | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| DR-PLG-01 | Plugboard Plug Interface | J1 = 6.35 mm (¼″) mono switched jack (Tip + Switch contact; Sleeve to chassis GND) | BOM J1 (×64 Stecker jack sockets) |

---

## 4. Plugboard Jack-Sensing

> For signal polarity, insertion-detect logic, RC debounce circuit, Schmitt trigger configuration,
> and detection latency, see `design/Electronics/Encoder/Design_Spec.md §7 Plugboard Jack-Sensing`.

---

## 5. Physical Harness

64× 2-wire assemblies (Tip wire + Switch wire), each terminated with 6.35 mm female crimp spade
terminals. Assemblies connect the panel-mount jacks to spade banks BT1–BT128 on the Encoder PCB.

---

## 6. Cross-References

| Document | Description |
| :--- | :--- |
| `design/Electronics/Encoder/Design_Spec.md` | Encoder PCB spade terminal pinout, CPLD I/O allocation, jack-sensing electrical spec |
