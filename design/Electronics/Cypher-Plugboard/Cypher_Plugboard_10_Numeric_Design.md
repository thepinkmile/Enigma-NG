# Cypher-Plugboard Board - 10-Numeric Variant Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-08-19
**Parent Document:** `design/Electronics/Cypher-Plugboard/Design_Spec.md`

---

## 1. Overview

This document specifies the **10-Numeric** variant of the Enigma-NG Cypher-Plugboard Board. It
supports the 10-digit numeric-only cipher alphabet (`0-9`), mirroring Cypher-Input's/
Cypher-Output's own 10-Numeric variant character set.

All three Cypher-Plugboard variants share an identical electrical circuit (HID-chain termination,
power passthrough) and an identical PCB strip (`J1`/`J2`/R1-R3 only - see
`design/Electronics/Cypher-Plugboard/Design_Spec.md`). Only the jack field's row count, character
layout, and jack quantity differ between variants; the jack field mounts to its own machined
metal enclosure (not the PCB), sized to this variant's own 2-row layout - the smallest of the
three enclosures.

## 2. Jack Field Layout

10 plug positions, each with 2 jack sockets (Pass 1, Pass 2) placed immediately next to each
other, horizontally. Arranged in **2 rows**, top-to-bottom:

| Row | Characters | Positions |
| :--- | :--- | :--- |
| 1 | `0 1 2 3 4` | 5 |
| 2 | `5 6 7 8 9` | 5 |

**Total: 10 positions, 20 jack sockets.**

> **Character order:** plain numeric order, left-to-right, top-to-bottom.

## 3. RefDes Allocation

Jacks are numbered sequentially, row by row (top-to-bottom), left-to-right within each row, with
the Pass 1 jack immediately followed by its Pass 2 partner at each position:

| Row | Characters | RefDes Range | Qty |
| :--- | :--- | :--- | :--- |
| 1 | `0`-`4` | J3-J12 | 10 |
| 2 | `5`-`9` | J13-J22 | 10 |

**Total: J3-J22, 20 jack sockets.**

## 4. Bill of Materials

| RefDes | Specification | MPN | Manufacturer | DigiKey PN | Mouser PN | JLCPCB PN | Alt Supplier + PN | Notes | Footprint Available | Footprint Downloaded | Qty |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| J3-J22 | Switchcraft 12A ("E12A"), 6.35mm (1/4") 2-conductor switched panel-mount jack | 12A | Switchcraft | SC1089-ND | 502-12A | - | - | Plugboard patch jacks, 10 positions x 2 passes; manually assembled, not part of the JLCPCB PCBA order (no JLCPCB PN); 3/8-32 UNEF-2A threaded bushing | - | - | 20 |

> **Sourcing status:** confirmed 2026-08-19 - Switchcraft 12A, DigiKey SC1089-ND, Mouser 502-12A.
> Datasheet: `design/Datasheets/Switchcraft-12A-datasheet.pdf`.
