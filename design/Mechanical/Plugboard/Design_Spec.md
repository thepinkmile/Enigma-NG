# Plugboard (V1.0) Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-07

## 1. Overview

A plugboard with dual ¼ inch jack sockets. Each socket is connected to one of the attached Encoder Boards.

## 2. Functional Requirements

| ID | Functional Requirement | Notes | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| FR-PLG-01 | Accept encoder input signal via plugboard jack interface | 6.35 mm (¼″) mono switched jack (Tip + Switch contact; Sleeve to chassis GND) | See Encoder/Design_Spec.md for Encoder Board interconnect details |

## 3. Design Requirements

| ID | Design Requirement | Specification | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| DR-PLG-01 | Plugboard Plug Interface | J1 = 6.35 mm (¼″) mono switched jack (Tip + Switch contact; Sleeve to chassis GND) | BOM J1 (×64 Stecker jack sockets) |

## 4. Plugboard Jack-Sensing

The Encoder CPLD monitors the 64 Stecker jack sockets for plug insertion state and updates the
encryption matrix in real time.

* **Logic:** The CPLD monitors 64 insertion-detect lines (spade bank BT65–BT128, Switch contacts)
  sourced from the 6.35 mm mono switched jack sockets.
* **Signal:** Lines are **active-low**. An external **10 kΩ pull-up to 3V3_ENIG** (R9–R72 on the
  Encoder PCB) holds each CPLD input HIGH when no plug is inserted; this dominates the CPLD internal
  weak pull-up (50 kΩ–100 kΩ), providing a well-defined idle-high state and improved harness noise
  immunity. A **100 nF RC filter capacitor** (C22–C85) is paired with each pull-up (RC τ = 1 ms),
  further attenuating harness-coupled noise. On plug insertion the switch contact closes to GND,
  pulling the CPLD input LOW. Inputs are configured as **3.3 V Schmitt trigger inputs** (confirmed);
  cable insertion is a slow mechanical event well within the Schmitt hysteresis window.
  The CPLD detects the falling edge and marks the corresponding channel as patched.
* **Latency:** Sub-microsecond detection of Stecker cable insertion; the internal encryption matrix
  is updated within one CPLD clock cycle.
* **Harness:** 64× 2-wire assemblies (Tip wire + Switch wire), each terminated with 6.35 mm female
  crimp spade terminals. Assemblies connect the panel-mount jacks to spade banks BT1–BT128 on the
  Encoder PCB.

> **Cross-reference:** For Encoder PCB spade terminal pinout, CPLD I/O allocation, and jack BOM
> details, see `design/Electronics/Encoder/Design_Spec.md §4 Interconnects` and `§3 Dual-Role Architecture`.
