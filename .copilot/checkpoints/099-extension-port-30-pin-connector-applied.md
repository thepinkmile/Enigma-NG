# Checkpoint 144 — Extension Port 30-pin connector change applied

## Status: Complete — awaiting user sign-off to commit

## What was done

All edits for DEC-053 (BHR-20-VUA → 2BHR-30-VUA, 20-pin → 30-pin Extension Port) applied across
10 files. All files passed markdownlint with no violations.

### Files modified

| File | Changes |
| --- | --- |
| `design/Design_Log.md` | DEC-053 inserted (full rationale, 30-pin pinout table, current budget, part numbers, impact list) |
| `design/Electronics/Stator/Board_Layout.md` | §1 J10 fully rewritten: 30-pin table, updated heading, updated connector description, pending-review note removed |
| `design/Electronics/Stator/Design_Spec.md` | FR-STA-04, DR-STA-05, §4 interconnect (lines for pin refs, line 306), §8 ESD, BOM (J4-J9/J10 split) |
| `design/Electronics/Extension/Board_Layout.md` | ASCII art labels (J7/J8), §2/§3 headings, §2 cross-ref blockquote, §5 deferred note removed, trace table note resolved, §5.2 resolved note, §7 ESD |
| `design/Electronics/Extension/Design_Spec.md` | DR-EXT-08, DR-EXT-12, §2 connector description + DEC-043→DEC-053 follow-on, §2 power entry pin refs, §5 ESD, BOM J7/J8 |
| `design/Electronics/Reflector/Design_Spec.md` | DR-REF-03, §2 TTD_RETURN pin, §3 interconnect description, JTAG warning block (all pin refs), §3 JTAG Return line, §4 power entry note, §4 GND_CHASSIS note, §5 ESD, BOM J4 |
| `design/Electronics/Consolidated_BOM.md` | BHR-20-VUA row split: 7→7 (ENC:J2/STA:J4-J9) + new 4-unit 2BHR-30-VUA row (STA:J10/REF:J4/EXT:J7,J8) |
| `design/Electronics/System_Architecture.md` | JTAG chain diagram: pin 15 → pin 16 for TTD_RETURN |
| `design/Electronics/Investigations/JTAG_Integrity.md` | TTD_RETURN ribbon diagram (pin 15→16, ENC pin ranges), summary warning block (pin 15→16, pin ranges) |
| `design/Electronics/Rotor/Board_Layout.md` | TTD_RETURN routing note: Stator J10 pin 15 → pin 16 |

### Approved pinout (30-pin, 2×15)

| Pins | Signal |
| --- | --- |
| 1–2, 29–30 | 5V_MAIN (outer symmetric pair) |
| 3–4, 27–28 | 3V3_ENIG (inner symmetric pair) |
| 5–6, 13–14, 17–18, 25–26 | GND guard pairs |
| 7–12 | ENC_OUT_REF[5:0] |
| 15 | SYS_RESET_N |
| 16 | TTD_RETURN |
| 19–24 | ENC_IN_REF[5:0] |

### Approved part numbers — 2BHR-30-VUA

- DigiKey: `2057-2BHR-30-VUA-ND`
- Mouser: `737-2BHR-30-VUA`
- JLCPCB: `C17346400`

### Current budget (verified)

| Rail | Load | Pins | Per conductor | Limit |
| --- | --- | --- | --- | --- |
| 3V3_ENIG | 1.65 A (30×55 mA) | 4 | 0.41 A | ~1 A ✅ |
| 5V_MAIN | 2.50 A (5×500 mA) | 4 | 0.63 A | ~1 A ✅ |
| GND return | 4.15 A total | 8 | 0.52 A | ~1 A ✅ |

## Unchanged items (confirmed not to touch)

- Stator J4–J9, Encoder J2 — still BHR-20-VUA 20-pin
- All encoder ports on all boards — not Extension Port, not changed

## Next

Awaiting "Let's lock this in" to commit.
