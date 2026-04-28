# Checkpoint 075 — Electronics deep-review cycle complete and committed

**Commit:** `41b6d07`
**Status:** All accumulated deep-review changes committed as single coherent set

## What was done

### CTL-M2 resolved (this session)
- Added U5, U6 (TPD4E05U06QDQARQ1) to Controller BOM: GbE ESD arrays covering all
  4 differential pairs (pair AB on U5, pair CD on U6), placed before J8 magnetics.
  Reuses existing approved part — no new component added.
- Confirmed suitability: 0.5pF/ch, ±15kV IEC 61000-4-2, supports up to 6 Gbps.
- Updated ESD Protection design note to list U4/U5/U6 roles explicitly.
- Resolved "Ethernet-entry ESD arrays" placeholder in BOM notes.

### PM bypass caps added (prior sub-session, now committed)
- C53–C57: LTC3350 INTVCC (C53), DRVCC (C54), VCC2P5 (C55) and STUSB4500
  VREG_1V2 (C56), VREG_2V7 (C57) internal-reg bypass caps.
- Reused C0805C105K5RACTU (1µF 0805) for C53/C55/C56/C57 and
  CC1206KKX7R8BB106 (10µF 1206) for C54 (satisfies ≥2.2µF DRVCC min).
- Consolidated BOM: PM 1µF 0805 count 3→7; PM 10µF 1206 count 1→2.
- BOM note updated from C21–C46 to C21–C57.

### Full accumulated change set (all boards)
- Power Module: ROTOR_EN→ROTOR_EN_N rename, TPS25751/PD topology note,
  C26–C30 expanded to individual IC rows, C53–C57 added
- Controller: U5/U6 GbE ESD arrays added (resolves CTL-M2); ROTOR_EN_N rename
- Rotor: Section 6 Thermal & ESD added, DEC-042 unshielded variant confirmed,
  ROT-04 header pin descriptions corrected, list style fixes
- Settings Board: R81–R98 (18× 1kΩ BSS138 gate pull-downs), C5/C6 (2× 10µF 0805)
- Stator: J5–J12 connector name fixes
- Extension: FR-EXT-06 ACTUATE_REQUEST pull-up corrected to 3V3_ENIG
- Design Log: DEC-045 (Samtec ERM8/ERF8 ESD requirement)
- Standards / Global_Routing_Spec: §9 hot-swap ESD exception clause
- Consolidated BOM: CL21B106KAYQNNE SBD +2, ERJ-2RKF1003X SBD +18,
  330Ω JLCPCB part corrected (C278592), TPD4E05U06 note updated

## Open items (not blocking)
- CTL-H1: explicitly deferred by user
- Rotor ESD TVS (PRTR5V0U10AZ): pending final sourcing — Section 6 placeholder retained
- Datasheet for new GbE ESD U5/U6 usage: no new datasheet needed (same part as U4)
