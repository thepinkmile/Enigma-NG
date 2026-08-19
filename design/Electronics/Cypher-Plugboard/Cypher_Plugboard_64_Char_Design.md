# Cypher-Plugboard Board - 64-Character Variant Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-08-19
**Parent Document:** `design/Electronics/Cypher-Plugboard/Design_Spec.md`

---

## 1. Overview

This document specifies the **64-Character** variant of the Enigma-NG Cypher-Plugboard Board. It
supports the full extended cipher alphabet - `A-Za-z0-9+/` (26 uppercase letters + 26 lowercase
letters + 10 digits + 2 base64-extra symbols), mirroring Cypher-Input's/Cypher-Output's own
64-Character variant character set.

All three Cypher-Plugboard variants share an identical electrical circuit (HID-chain termination,
power passthrough) and an identical PCB strip (`J1`/`J2`/R1-R3 only - see
`design/Electronics/Cypher-Plugboard/Design_Spec.md`). Only the jack field's row count, character
layout, and jack quantity differ between variants; since the jack field mounts to a separate
machined metal enclosure (not the PCB), this is the variant with the tallest enclosure of the
three (see parent Design_Spec.md §1/§4).

## 2. Jack Field Layout

64 plug positions, each with 2 jack sockets (Pass 1, Pass 2) placed immediately next to each
other, horizontally. Arranged in **7 rows**, top-to-bottom:

| Row | Characters | Positions | Notes |
| :--- | :--- | :--- | :--- |
| 1 | `0 1 2 3 4 5 6 7 8 9` | 10 | Digits, left-to-right |
| 2 | `A B C D E F G H I` | 9 | Uppercase, first block |
| 3 | `J K L M N O P Q R` | 9 | Uppercase, second block |
| 4 | `S T U V W X Y Z +` | 9 | Uppercase, third block (8 letters) + `+` appended so all 3 uppercase rows are evenly 9 wide |
| 5 | `a b c d e f g h i` | 9 | Lowercase, first block |
| 6 | `j k l m n o p q r` | 9 | Lowercase, second block |
| 7 | `s t u v w x y z /` | 9 | Lowercase, third block (8 letters) + `/` appended so all 3 lowercase rows are evenly 9 wide |

**Total: 64 positions, 128 jack sockets.** Row 1 (digits) is the widest row at 10 positions;
rows 2-7 are evenly 9 positions each, giving a visually symmetrical panel (per user direction,
2026-08-18) rather than an uneven 9/9/8 split - `+` and `/` are appended to the last uppercase and
last lowercase row respectively to even them out.

> **Character order:** within each row, characters run in plain alphabetical/numeric order,
> left-to-right (not a QWERTY-style layout like Cypher-Input's own key arrangement) - the
> Plugboard is a technician-facing patch panel, not a keyboard.

## 3. RefDes Allocation

Jacks are numbered sequentially, row by row (top-to-bottom), left-to-right within each row, with
the Pass 1 jack immediately followed by its Pass 2 partner at each position:

| Row | Characters | RefDes Range | Qty |
| :--- | :--- | :--- | :--- |
| 1 | `0`-`9` | J3-J22 | 20 |
| 2 | `A`-`I` | J23-J40 | 18 |
| 3 | `J`-`R` | J41-J58 | 18 |
| 4 | `S`-`Z`, `+` | J59-J76 | 18 |
| 5 | `a`-`i` | J77-J94 | 18 |
| 6 | `j`-`r` | J95-J112 | 18 |
| 7 | `s`-`z`, `/` | J113-J130 | 18 |

**Total: J3-J130, 128 jack sockets.**

## 4. Bill of Materials

| RefDes | Specification | MPN | Manufacturer | DigiKey PN | Mouser PN | JLCPCB PN | Alt Supplier + PN | Notes | Footprint Available | Footprint Downloaded | Qty |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| J3-J130 | Switchcraft 12A ("E12A"), 6.35mm (1/4") 2-conductor switched panel-mount jack | 12A | Switchcraft | SC1089-ND | 502-12A | - | - | Plugboard patch jacks, 64 positions x 2 passes; manually assembled, not part of the JLCPCB PCBA order (no JLCPCB PN); 3/8-32 UNEF-2A threaded bushing | - | - | 128 |

> **Sourcing status:** confirmed 2026-08-19 - Switchcraft 12A, DigiKey SC1089-ND, Mouser 502-12A.
> Datasheet: `design/Datasheets/Switchcraft-12A-datasheet.pdf`.
