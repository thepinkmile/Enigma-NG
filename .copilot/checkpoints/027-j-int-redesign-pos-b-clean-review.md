# Checkpoint 027 — J_INT Redesign, POS_B Naming, Full Deep-Dive Clean

**Session:** bb01fc15-4ce2-4b66-94c1-db3fabe7b119
**Date:** 2026-04-13

---

## Overview

This checkpoint covers the completion of Item D (J_INT internal interconnect redesign) and a
subsequent full deep-dive review cycle (two consecutive clean passes). All connector MPNs from
the master parts list are now confirmed and committed. The design is in a clean, verified state
ready for passive components sourcing.

---

## Work Done This Checkpoint

### Item D — J_INT Redesign (commit `fca8237`)

Replaced the non-existent Würth 61201221721 (2×11 22-pin keyed IDC box header) with four
single-row 2.54mm THT headers totalling 22 pins:

| Header | Board A gender | Board B gender | Pins | Signals |
|--------|---------------|---------------|------|---------|
| H_SW3 | PH1-07-UA (male) | RS1-07-G (female) | 7 | SW3[0:5], GND |
| H_PWR | RS1-05-G (female) | PH1-05-UA (male) | 5 | 3V3_ENIG×4, GND |
| H_JTAG | RS1-05-G (female) | PH1-05-UA (male) | 5 | TCK, GND, TMS, GND, TDO |
| H_SENS | PH1-05-UA (male) | RS1-05-G (female) | 5 | SDA, SCL, POS_B[0:2] |

**Keying mechanism:** Mixed-gender layout — H_SW3/H_SENS are male on Board A, H_PWR/H_JTAG
are female on Board A; inverses on Board B. The 7-pin H_SW3 footprint is unique, making
incorrect assembly geometrically impossible.

**Mechanical benefit:** 4 distributed headers add rigidity to the two-board rotor assembly.

**Assembly:** All headers manually soldered post-JLCPCB SMT on the inner (bottom) face. All
SMT components are on the outer (top) face — JLCPCB single-side SMT only. Boards mate
bottom-to-bottom; tops face outward.

**New parts:**
- PH1-07-UA: Mouser 737-PH1-07-UA, DigiKey 2057-PH1-07-UA-ND, JLCPCB C3331618
- RS1-07-G: Mouser 737-RS1-07-G, DigiKey 2057-RS1-07-G-ND, JLCPCB C3321543

**Updated counts in Consolidated BOM:**
- PH1-05-UA: ROT(×1)=3, ROT Total=90, JDB=1, System Total=91
- RS1-05-G: CTL=1, ROT(×1)=3, ROT Total=90, System Total=91
- PH1-07-UA: ROT(×1)=1, ROT Total=30, System Total=30 (new)
- RS1-07-G: ROT(×1)=1, ROT Total=30, System Total=30 (new)

### POS_B Signal Renaming

`ENC_B[0:2]` renamed to `POS_B[0:2]` throughout. These are the 3-bit Track B position output
from FDC2114 U3 on Board B (N=64 only). They travel via H_SENS back to Board A's CPLD for
6-bit Gray code decode. Not used for N=26 builds (U3 not populated).

### Files Updated by fca8237:
- `design/Electronics/Rotor/Design_Spec.md` — §3.4 J_INT section fully replaced, FR-ROT-10,
  DR-ROT-11, Board A/B BOM rows
- `design/Electronics/Rotor/Board_Layout.md` — ASCII art, component tables, cross-section
- `design/Electronics/Consolidated_BOM.md` — new rows, updated counts, §11 datasheet entries
- `design/Mechanical/Rotor/Design_Spec.md` — §6 header assembly instructions updated
- `design/Electronics/Extension/Design_Spec.md` — Molex 22-23-2161 → BHR-16-VUA
- `design/Electronics/Reflector/Design_Spec.md` — Molex 22-23-2161 → BHR-16-VUA

### Full Deep-Dive Review Cycle (commit `77ea120`)

10 findings fixed in Round 1, all in `Design_Log.md`:
- DEC-028 references to old "2×11 IDC box header" / "22-pin IDC" updated
- Stale Molex 22-23-2261/2161 MPNs in DEC entries for Stator J4-J7, Encoder J2, Reflector J4,
  Extension J7/J8 corrected to Amphenol T821126A1S100CEU / Adam Tech BHR-16-VUA
- One residual stale "IDC box header" reference in Rotor Design_Spec overview fixed

Rounds 2 & 3: Zero findings, zero markdownlint warnings — **two consecutive clean passes**.

---

## Connector MPN Summary (All Confirmed)

### JDB Hat-Headers (committed `373a93e`)
| Ref | Part | Mouser | DigiKey | JLCPCB |
|-----|------|--------|---------|--------|
| JDB J1 | PH1-05-UA (male 1×5) | 737-PH1-05-UA | 2057-PH1-05-UA-ND | C5374051 |
| JDB J2 | PH1-10-UA (male 1×10) | 737-PH1-10-UA | 2057-PH1-10-UA-ND | C3330527 |
| CTL J_JDB_PWR | RS1-05-G (female 1×5) | 737-RS1-05-G | 2057-RS1-05-G-ND | C3321119 |
| CTL J_JDB_JTAG | RS1-10-G (female 1×10) | 737-RS1-10-G | 2057-RS1-10-G-ND | C3320525 |

### IDC Shrouded Box Headers (committed `7495a8d`)
| Usage | Part | Mouser | DigiKey | JLCPCB |
|-------|------|--------|---------|--------|
| STA J4/J5/J6, ENC J2 (26-pin 2×13) | Amphenol T821126A1S100CEU | — | — | C3013501 (RS-Online 832-3503 in desc) |
| STA J7, REF J4, EXT J7/J8 (16-pin 2×8) | Adam Tech BHR-16-VUA | 737-BHR-16-VUA | 2057-BHR-16-VUA-ND | C17692295 |

### DIP Switches (committed `d95f07d`)
| Usage | Part | Mouser | DigiKey | JLCPCB |
|-------|------|--------|---------|--------|
| STA SW1 (4-pos) | CTS 219-4LPST | 774-219-4LPST | CT2064-ND | C128947 |
| STA SW2, ROT SW1/SW2/SW3 (6-pos) | CTS 219-6LPSTR | 774-2196LPSTR | 119-219-6LPSTRCT-ND | C2842671 |

### Rotor J_INT Headers (committed `fca8237`)
| Ref | Part | Mouser | DigiKey | JLCPCB |
|-----|------|--------|---------|--------|
| Board A H_SW3 | PH1-07-UA (male 1×7) | 737-PH1-07-UA | 2057-PH1-07-UA-ND | C3331618 |
| Board B H_SW3 | RS1-07-G (female 1×7) | 737-RS1-07-G | 2057-RS1-07-G-ND | C3321543 |
| Board A H_PWR/H_JTAG | RS1-05-G (female 1×5) | 737-RS1-05-G | 2057-RS1-05-G-ND | C3321119 |
| Board B H_PWR/H_JTAG | PH1-05-UA (male 1×5) | 737-PH1-05-UA | 2057-PH1-05-UA-ND | C5374051 |
| Board A H_SENS | PH1-05-UA (male 1×5) | (as above) | | |
| Board B H_SENS | RS1-05-G (female 1×5) | (as above) | | |

---

## Commits This Checkpoint

| Hash | Description |
|------|-------------|
| `d95f07d` | Item C: CTS 219-6LPSTR DIP switch MPNs |
| `15d8bb3` | Add CTS 219-series DIP switch datasheet |
| `0ec9d90` | Fix remaining markdownlint MD013 warnings |
| `7495a8d` | Items E & F: shrouded IDC header MPNs |
| `373a93e` | Items G & H: Adam Tech PH1/RS1 hat-header pairs |
| `fca8237` | Item D: J_INT redesign, POS_B signal naming |
| `77ea120` | Review cycle R1: fix Design_Log stale connector refs |

---

## Confirmed Correct — Do NOT Re-Flag

All items in the Known-Correct List from the session plan remain valid. Additionally:
- `POS_B[0:2]` = correct Track B position signal name (not `ENC_B`)
- `Würth 61201221721` = intentionally gone; replaced by 4-header arrangement
- J_INT described as 4 headers (H_SW3/H_PWR/H_JTAG/H_SENS) = correct
- H_JTAG pinout: TCK(1), GND(2), TMS(3), GND(4), TDO(5) = correct (interleaved GND)
- Rotor JLCPCB single-side SMT = confirmed resolved; all SMT on outer face, headers on inner
  face manually post-SMT; bottom-to-bottom mating, tops facing outward
- RS-Online 832-3503 in description field (not Mouser column) for Amphenol T821126A1S100CEU = correct

---

## Deferred Items

- **Item J — Marquardt 1800 power switch (RGB LED):** MPN not yet confirmed; intentionally
  deferred. Pick up when ready.
- Passive components (resistors, capacitors, inductors, speciality values) — **next session**
- Rotor detailed design review cycle (2 clean passes) — **next session**
- KiCad project setup

---

## Next Session — Passive Components

The main remaining BOM work is verifying/sourcing MPNs for all passive components. Start from
Consolidated_BOM.md and work through each value group. After passives are complete, trigger
a fresh full deep-dive review cycle, then move to KiCad setup.
