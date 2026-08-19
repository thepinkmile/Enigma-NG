# Cypher-Plugboard Board - 26-Char Classic Variant Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-08-19
**Parent Document:** `design/Electronics/Cypher-Plugboard/Design_Spec.md`

---

## 1. Overview

This document specifies the **26-Char Classic** variant of the Enigma-NG Cypher-Plugboard Board.
It supports the classic 26-letter cipher alphabet (`A-Z`, uppercase only), mirroring
Cypher-Input's/Cypher-Output's own 26-Char Classic variant character set.

All three Cypher-Plugboard variants share an identical electrical circuit (HID-chain termination,
power passthrough) and an identical PCB strip (`J1`/`J2`/R1-R3 only - see
`design/Electronics/Cypher-Plugboard/Design_Spec.md`). Only the jack field's row count, character
layout, and jack quantity differ between variants; the jack field mounts to its own machined
metal enclosure (not the PCB), sized to this variant's own 3-row layout - it is not sized to the
64-Character variant's taller enclosure, since there is no shared board outline to keep.

## 2. Jack Field Layout

26 plug positions, each with 2 jack sockets (Pass 1, Pass 2) placed immediately next to each
other, horizontally. Arranged in **3 rows**, top-to-bottom:

| Row | Characters | Positions |
| :--- | :--- | :--- |
| 1 | `A B C D E F G H I` | 9 |
| 2 | `J K L M N O P Q R` | 9 |
| 3 | `S T U V W X Y Z` | 8 |

**Total: 26 positions, 52 jack sockets.** Unlike the 64-Character variant, there is no extra
symbol to append to the shorter third row - this variant's alphabet is exactly 26 letters, so the
natural 9/9/8 split is used as-is.

> **Character order:** plain alphabetical order, left-to-right, uppercase only (engraved/printed in
> capitals on the machined metal enclosure per parent `Design_Spec.md §8`).

## 3. RefDes Allocation

Jacks are numbered sequentially, row by row (top-to-bottom), left-to-right within each row, with
the Pass 1 jack immediately followed by its Pass 2 partner at each position:

| Row | Characters | RefDes Range | Qty |
| :--- | :--- | :--- | :--- |
| 1 | `A`-`I` | J3-J20 | 18 |
| 2 | `J`-`R` | J21-J38 | 18 |
| 3 | `S`-`Z` | J39-J54 | 16 |

**Total: J3-J54, 52 jack sockets.**

## 4. Bill of Materials

| RefDes | Specification | MPN | Manufacturer | DigiKey PN | Mouser PN | JLCPCB PN | Alt Supplier + PN | Notes | Footprint Available | Footprint Downloaded | Qty |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| J3-J54 | Switchcraft 12A ("E12A"), 6.35mm (1/4") 2-conductor switched panel-mount jack | 12A | Switchcraft | SC1089-ND | 502-12A | - | - | Plugboard patch jacks, 26 positions x 2 passes; manually assembled, not part of the JLCPCB PCBA order (no JLCPCB PN); 3/8-32 UNEF-2A threaded bushing | - | - | 52 |

> **Sourcing status:** confirmed 2026-08-19 - Switchcraft 12A, DigiKey SC1089-ND, Mouser 502-12A.
> Datasheet: `design/Datasheets/Switchcraft-12A-datasheet.pdf`.
