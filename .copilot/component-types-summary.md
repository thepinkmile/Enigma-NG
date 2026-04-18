# Enigma-NG Component Types Summary

> Created: 2026-04-17
> For use in systematic component re-verification

This document provides a high-level overview of all 107 unique component types in the Enigma-NG system, organized by category to facilitate batch verification.

---

## Verification Progress

| Status | Count | Percentage |
|--------|-------|------------|
| **VERIFIED** | 9 | 8.4% |
| **RECHECK** | 97 | 90.7% |
| **BLOCKED** | 1 | 0.9% |
| **Total** | 107 | 100% |

---

## Component Categories & Verification Order

### 1. SWITCHES & USER INPUT (8 items)

**Component IDs:** S001-S008

| ID | Description | Board | Status |
|----|-------------|-------|--------|
| S001 | Historical unified switch (superseded) | PM + SBD | ✅ VERIFIED |
| S002 | Settings Board SPDT toggles (×12) | SBD | ✅ VERIFIED |
| S003 | CFG_APPLY momentary pushbutton | SBD | ⏳ RECHECK |
| S004 | Power Module RGB metal switch | PM | ✅ VERIFIED |
| S005 | Controller reset button | CTL | ⏳ RECHECK |
| S006 | Keyboard matrix switches (×192) | ENC/Kbd | ⏳ RECHECK |
| S007 | Rotor DIP switches | ROT | ⏳ RECHECK |
| S008 | SW1 PCB blade terminals (×6) | PM | ⏳ RECHECK |

**Verification approach:** Start with verified items to understand datasheet format, then verify mechanical fit, electrical ratings, and panel-mount geometry for remaining items.

---

### 2. LEDS & INDICATORS (4 items)

**Component IDs:** L001-L004

| ID | Description | Board | Status |
|----|-------------|-------|--------|
| L001 | Settings Board RGB LEDs (×12) | SBD | ✅ VERIFIED |
| L002 | LED resistors (RGB) | SBD | 🚫 BLOCKED |
| L003 | Green status LED | PM | ⏳ RECHECK |
| L004 | Ethernet LED resistors | PM | ⏳ RECHECK |

**Verification approach:** L002 is blocked pending resistor value tuning; verify L003-L004 footprints and electrical specs.

---

### 3. IC: CPLD & PROGRAMMABLE LOGIC (2 items)

**Component IDs:** IC001-IC002

| ID | Description | Qty | Status |
|----|-------------|-----|--------|
| IC001 | EPM240T100I5N (Encoder) | 6 | ⏳ RECHECK |
| IC002 | EPM570T100I5N (Stator + Rotor) | 31 | ⏳ RECHECK |

**Verification approach:** Confirm TQFP-100 footprint compatibility, industrial temp range, and supplier availability.

---

### 4. IC: POWER MANAGEMENT (14 items)

**Component IDs:** IC003-IC016

Key items to verify:
- IC003: TPS75733KTTRG3 (3.3V LDO)
- IC004: TPS259804ONRGER (eFuse — CRITICAL: do NOT change 04 to 07)
- IC005: LMQ61460AFSQRJRRQ1 (5V buck converters ×2)
- IC006: LTC3350EUHF#PBF (Supercap manager)
- IC007-IC008: USB PD controllers
- IC009-IC013: Power path management ICs
- IC014-IC015: USB/HDMI current limiters
- IC016: Schmitt trigger inverters

**Verification approach:** Group by supplier (TI vs ST vs others), verify package codes match footprints, confirm electrical specs.

---

### 5. IC: INTERFACE & BRIDGE (3 items)

**Component IDs:** IC017-IC019

| ID | Description | Qty | Status |
|----|-------------|-----|--------|
| IC017 | INA219AIDR current monitors | 2 | ⏳ RECHECK |
| IC018 | MCP23017T-E/SO I²C expanders | 5 | ⏳ RECHECK |
| IC019 | PCA9685BS/3 PWM driver | 1 | ⏳ RECHECK |

**Verification approach:** Confirm I²C address range compatibility and SOIC/SSOP footprints.

---

### 6. IC: SENSORS (3 items)

**Component IDs:** IC020-IC022

All three are FDC2114RGHR capacitive sensor ICs with different I²C addresses and population rules (N=26 vs N=64).

**Verification approach:** Verify 16-VQFN footprint and address configuration requirements.

---

### 7. IC: LOGIC BUFFERS & DRIVERS (2 items)

**Component IDs:** IC023-IC024

| ID | Description | Qty | Status |
|----|-------------|-----|--------|
| IC023 | SN74LVC2G125DCUR (JTAG buffers) | 2 | ⏳ RECHECK |
| IC024 | FT232H (USB-JTAG bridge) | 1 | ⏳ RECHECK |

**Verification approach:** Confirm VSSOP-8 and QFN-56 footprints. **CRITICAL:** IC023 is VSSOP-8, NOT SOT-23-6.

---

### 8. IC: COMPUTE MODULE (1 item)

**Component ID:** IC025

Raspberry Pi CM5 — global sourcing, verify supplier availability and lead time.

---

### 9. TRANSISTORS & DIODES (5 items)

**Component IDs:** T001-T004, D001

| ID | Description | Qty | Status |
|----|-------------|-----|--------|
| T001 | BSS138 N-ch MOSFETs | 6 | ✅ VERIFIED |
| T002 | CSD17483F4T OR-ing MOSFETs | 3 | ⏳ RECHECK |
| D001 | BAT54 Schottky diodes | 3 | ⏳ RECHECK |
| T003 | Gate resistors (see R-category) | — | ✅ VERIFIED |
| T004 | Blade tabs (see S008) | — | ⏳ RECHECK |

---

### 10. ESD PROTECTION (3 items)

**Component IDs:** ESD001-ESD003

All TI ESD protection devices — verify package codes and application notes.

---

### 11. CAPACITORS (15 items)

**Component IDs:** C001-C015

Major categories:
- **Bulk bypass:** C001 (0.1µF ×513), C002 (10µF ×185), C003 (22µF ×15)
- **Specialized:** C004-C011 (timing, filters, soft-start)
- **Energy storage:** C012 (25F supercaps ×8), C013 (backup caps)
- **Switch debounce:** C014

**Verification approach:** Batch verify by Samsung/Murata families, confirm X7R dielectric and voltage ratings.

---

### 12. RESISTORS (39 items)

**Component IDs:** R001-R051

Major categories:
- **Pull-up/down:** R001-R002 (10kΩ in 0603/0402)
- **Series/termination:** R003-R006 (75Ω, 33Ω, 22Ω)
- **LED current limit:** R007-R008, L002
- **Precision analog:** R018, R021-R023 (thin-film ERA series)
- **Power management:** R012-R020
- **LED current limit:** R051 (blue-channel resistor set)

**Verification approach:** Batch verify ERJ vs ERA series, confirm 1% vs 0.1% tolerance requirements.

---

### 13. INDUCTORS & MAGNETICS (3 items)

**Component IDs:** IND001-IND003

- Ferrite beads (×4)
- PoE isolation transformer
- EMI common-mode chokes (×2)

---

### 14. POWER INDUCTORS (1 item)

**Component ID:** PWR001

Bourns SRP1265A-100M — verify current rating and saturation specs.

---

### 15. CONNECTORS: BOARD-TO-BOARD (8 items)

**Component IDs:** J001-J008

**Samtec ERM8/ERF8 family:**
- J001-J002: Link-Alpha (80-pin)
- J003-J004: Link-Beta (40-pin)
- J005-J008: Rotor stack interfaces (10-pin, 20-pin)

**Verification approach:** Confirm 0.8mm pitch, 5.0mm stack height, and mating pair compatibility.

---

### 16. CONNECTORS: PIN HEADERS & SOCKETS (8 items)

**Component IDs:** J009-J016

**Adam Tech PH1/RS1 family:**
- J009-J014: Rotor internal interconnects (1×5, 1×7, 1×10)
- J015-J016: Shrouded IDC headers (16-pin, 26-pin)

**Verification approach:** Confirm 2.54mm pitch and keying direction.

---

### 17. CONNECTORS: EXTERNAL I/O (7 items)

**Component IDs:** J017-J023

- J017: Dual USB 3.0 Type-A
- J018: HDMI Type-A
- J019: USB Type-C power-only
- J020: RJ45 MagJack
- J021: Micro-Fit 3.0 battery connector
- J022-J023: JST PH 2.0mm (4-pin, 3-pin) — ✅ VERIFIED

**Verification approach:** Verify mechanical overhang, shell geometry, and board-edge placement.

---

### 18. CONNECTORS: DISPLAY & FAN (2 items)

**Component IDs:** J024-J025

- J024: DSI1 FPC 15-pin ZIF — ✅ VERIFIED
- J025: JST SH 4-pin fan header — ✅ VERIFIED

---

### 19. CONNECTORS: PLUGBOARD & ENCODER (2 items)

**Component IDs:** J026-J027

- J026: 6.35mm panel jacks (×192) — already purchased
- J027: PCB blade terminals (×384)

**Verification approach:** Confirm harness mating and mechanical retention.

---

### 20. MISCELLANEOUS (5 items)

**Component IDs:** M001-M005

- M001: 12 MHz crystal
- M002: 72°C thermal cutoff
- M003: CR2032 battery holder
- M004: CM5 mounting standoffs (×4)
- M005: SERVO_HOME capacitor

---

## Recommended Verification Order

### Phase 1: Critical Power & Protection (High Risk)
1. **IC: POWER MANAGEMENT** (IC003-IC016) — 14 items
2. **ESD PROTECTION** (ESD001-ESD003) — 3 items
3. **TRANSISTORS & DIODES** (T002, D001) — 2 items
4. **Power inductors & magnetics** (PWR001, IND001-IND003) — 4 items

**Rationale:** Power failures can damage entire system; verify datasheets and electrical specs first.

---

### Phase 2: Critical Resistors (Precision-Dependent)
1. **Precision thin-film resistors** (R018, R021-R023) — 4 items
2. **Power management resistors** (R012-R020) — 9 items
3. **Current sense shunts** (R011) — 1 item

**Rationale:** Precision resistors affect LTC3350 and eFuse behavior; wrong values = unsafe operation.

---

### Phase 3: Logic & Interconnect
1. **IC: CPLD & LOGIC** (IC001-IC002, IC023-IC024) — 4 items
2. **CONNECTORS: BOARD-TO-BOARD** (J001-J008) — 8 items
3. **CONNECTORS: PIN HEADERS** (J009-J016) — 8 items

**Rationale:** Logic ICs and BtB connectors are high-volume and require consistent footprints across 30+ boards.

---

### Phase 4: Sensors & Interface
1. **IC: SENSORS** (IC020-IC022) — 3 items
2. **IC: INTERFACE & BRIDGE** (IC017-IC019) — 3 items
3. **CAPACITORS** (C001-C015) — 15 items

**Rationale:** Sensors are N=26/N=64 variant-dependent; capacitors can be batch-verified by family.

---

### Phase 5: User Interface & External I/O
1. **SWITCHES & USER INPUT** (S003, S005-S008) — 5 items
2. **CONNECTORS: EXTERNAL I/O** (J017-J021) — 5 items
3. **LEDS & INDICATORS** (L003-L004) — 2 items

**Rationale:** Mechanical fit and panel cutouts require physical mock-up validation.

---

### Phase 6: Remaining Passives & Misc
1. **RESISTORS** (all remaining) — ~25 items
2. **CONNECTORS: PLUGBOARD** (J026-J027) — 2 items
3. **MISCELLANEOUS** (M001-M005) — 5 items

**Rationale:** Low-risk items; batch verify by supplier family.

---

## Quick Reference: Verification Status by Category

| Category | Total | Verified | Recheck | Blocked |
|----------|-------|----------|---------|---------|
| Switches & Input | 8 | 2 | 6 | 0 |
| LEDs & Indicators | 4 | 1 | 2 | 1 |
| ICs: CPLD | 2 | 0 | 2 | 0 |
| ICs: Power Mgmt | 14 | 0 | 14 | 0 |
| ICs: Interface | 3 | 0 | 3 | 0 |
| ICs: Sensors | 3 | 0 | 3 | 0 |
| ICs: Logic | 2 | 0 | 2 | 0 |
| ICs: Compute | 1 | 0 | 1 | 0 |
| Transistors & Diodes | 5 | 1 | 4 | 0 |
| ESD Protection | 3 | 0 | 3 | 0 |
| Capacitors | 15 | 0 | 15 | 0 |
| Resistors | 39 | 1 | 38 | 0 |
| Inductors | 4 | 0 | 4 | 0 |
| Connectors: BtB | 8 | 0 | 8 | 0 |
| Connectors: Headers | 8 | 0 | 8 | 0 |
| Connectors: External | 7 | 2 | 5 | 0 |
| Connectors: Display | 2 | 2 | 0 | 0 |
| Connectors: Plugboard | 2 | 0 | 2 | 0 |
| Miscellaneous | 5 | 0 | 5 | 0 |
| **TOTAL** | **107** | **9** | **97** | **1** |

---

## Notes for Verification

### Critical "Do NOT Change" Items

1. **TPS259804ONRGER** (IC004) — Never change '04' to '07' (OVLO vs NO OVLO)
2. **SN74LVC2G125DCUR** (IC023) — Package is VSSOP-8 (NOT SOT-23-6)
3. **EPM570 vs EPM240** — EPM570 for Stator+Rotor; EPM240 for Encoder only
4. **ERA vs ERJ resistors** — ERA = 0.1% thin-film; ERJ = 1% thick-film

### Stale MPNs to Avoid

See `.copilot/plan.md` section "Stale Values (must NEVER reappear)" for comprehensive list.

### Datasheet Requirements

Before marking any item as VERIFIED:
1. Datasheet must exist in `design/Datasheets/`
2. Package/footprint must match exactly
3. Electrical parameters must meet or exceed design requirements
4. Variant codes must be correct (e.g., '04' in TPS259804)

---

## Component Type List (Alphabetical)

For quick lookup:

- Battery holders, blade terminals, buffers, capacitors, connectors (BtB, external, headers, JST, USB, HDMI, RJ45), CPLDs, crystals, current limiters, current monitors, diodes, ESD arrays, eFuses, expanders, ferrite beads, inductors, LEDs, LDOs, MOSFETs, PWM drivers, resistors (thick-film, thin-film, shunts), sensors (capacitive), standoffs, supercapacitors, switches (DIP, toggle, momentary, power), thermal cutoffs, timers, transformers, USB bridges.

Total: 107 unique component types across 20 categories.
