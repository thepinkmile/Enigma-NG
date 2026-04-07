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

> This design spec will be developed further during the Mechanical Design phase.
