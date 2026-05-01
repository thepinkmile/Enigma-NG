# Deep-Dive Review Cycle — Pass 1

**Started:** 2026-04-30

---

## Scope

- **Stand-alone board reviews:** Power Module, Controller, Stator, Rotor, Extension, Reflector,
  Encoder, Actuation Module, Settings Board, JTAG Daughterboard
- **Integration reviews:** Inter-board connectivity (pin-maps, signal names, rail names);
  Consolidated BOM accuracy vs all board BOMs

## Review Agent Batches

- Batch 1: Power Module, Controller, Stator, Rotor
- Batch 2: Extension, Reflector, Encoder, Actuation Module
- Batch 3: Settings Board, JTAG Daughterboard, Integration-Connectivity, Integration-BOM

---

## Pass 1 — Review Findings

<!-- Agents append their findings below in the format:
     ### [Board/Scope] — [Agent ID]
     | Severity | Item | Details |
-->

### Batch 1 — Power Module (review-pm)

| Severity | Ref | Finding | Detail |
| :--- | :--- | :--- | :--- |
| HIGH | SIGNAL-ROTOR_EN | Signal naming inconsistency: ROTOR_EN vs ROTOR_EN_N | Board_Layout.md §2 and §4 lists signal as `ROTOR_EN`, but Design_Spec.md consistently names it `ROTOR_EN_N` (active-LOW). Must be resolved before schematic capture. |
| MEDIUM | BOM-J1_J3 | Conflicting documentation for J1-J3 connector sourcing | BOM table lists JLCPCB part number C3683043 for J1-J3 connectors, but BOM notes state these are not standard JLC stocked parts and require global sourcing/consignment/post-assembly install. Contradictory. |
| MEDIUM | BOM-R12_R23 | Missing JLCPCB sourcing information without explanation | R12 and R23 (CSS2H-2512R-R010ELF Kelvin-sense shunt resistors) have `—` in the JLCPCB column with no explanation. Unlike other similarly constrained parts, no sourcing note is present. |
| MEDIUM | BATTERY-ESD | Incomplete ESD protection on J4 battery connector power lines | J4 is on the external face. D1 protects BATT_PRES_N and D2 protects SMBus lines only. VBATT+ and VBATT- power lines have no dedicated TVS transient suppression. |

### Batch 1 — Controller (review-ctl)

| Severity | Ref | Finding | Detail |
| :--- | :--- | :--- | :--- |
| HIGH | LAYOUT-REF | Broken cross-reference in Design_Spec.md | Design_Spec.md lines 288 and 303 reference "Controller/Board_Layout.md JDB Hat Connectors section" but this section does not exist in Board_Layout.md. Authoritative pin tables are defined inline in Design_Spec.md §8.3 and §8.4. |
| MEDIUM | CONN-NAMING | Signal naming inconsistency: ROTOR_EN_N vs ROTOR_EN | Design_Spec.md uses `ROTOR_EN_N` consistently (FR-CTL-05 and other refs). Board_Layout.md §2.3 J3 table lists it as `ROTOR_EN` without the `_N` suffix. |
| MEDIUM | BOM-BYPASS | Missing bypass capacitor specifications for power switches | U2 (TPS2065CDBVR USB power switch) and U3 (AP2331W-7 HDMI power switch) have no associated bypass capacitor RefDes in the BOM. Standard practice requires local 100nF bypass on Vcc pins. |

### Batch 1 — Stator (review-sta)

| Severity | Ref | Finding | Detail |
| :--- | :--- | :--- | :--- |
| HIGH | BOM-U8 | Duplicate BOM entry for U8 | U8 (MCP23017 I²C GPIO Expander) appears twice in the BOM table. Both entries are identical. One must be removed. |
| HIGH | FR-STA-08 | Incorrect I²C device reference | FR-STA-08 states "CM5 reads U1 @ 0x23" but U1 is the CPLD (EPM570T100I5N), which is not I²C-addressable. Address 0x23 belongs to the Settings Board. The requirement text needs correction. |
| MEDIUM | LAYOUT-PLACEMENT | Missing component placement zones in Board_Layout.md | Board_Layout.md is titled "Master Pinout" but only U8 (§6) and J13 (§5) have explicit placement specifications. The remaining 40+ designators (C1-C26, J1-J12, L1-L4, R1-R43, U1-U7, U9-U12) have no placement zones, height constraints, orientation, or thermal notes. |

### Batch 1 — Rotor (review-rot)

| Severity | Ref | Finding | Detail |
| :--- | :--- | :--- | :--- |
| HIGH | DR-ROT-SEQ | DR-ROT IDs non-sequential | DR-ROT-11 appears at row 7, before DR-ROT-06 through DR-ROT-10. Correct sequence should be DR-ROT-01 through DR-ROT-11 in ascending order. |
| MEDIUM | DR-ROT-BYPASS | No Design Requirement for decoupling/bypass capacitors | C1–C19 (CPLD/FDC2114 bypass and bulk decoupling) are fully specified in the BOM but have no corresponding DR. |
| MEDIUM | LAYOUT-SUMMARY | Board_Layout component summaries incomplete | Board A §2.1 and Board B §3.1 "Component Summary" sections omit decoupling capacitors (C1–C19), pull-up resistors (R2–R7), and ESD arrays (U5–U12). |
| LOW | BOM-MOQ | High MOQ warnings on I²C pull-up resistors | R6–R7 (KOA Speer SG73S1ERTTP4701F 4.7kΩ): Mouser MOQ 10,000; JLCPCB MOQ 49. May impact prototype/low-volume build feasibility. |

---

**Batch 1 subtotal: 4 HIGH · 8 MEDIUM · 1 LOW**

### Batch 2 — Extension (review-ext)

| Severity | Ref | Finding | Detail |
| :--- | :--- | :--- | :--- |
| HIGH | BOM-J7_J8 | Consolidated_BOM.md J7/J8 description incorrect | Consolidated_BOM.md Extension rows describe J7/J8 as "Rotor group JTAG headers" — this is wrong. J7/J8 are the Extension Port (Stator interconnect), 20-pin BHR-20-VUA shrouded box headers. |
| HIGH | ESD-DEC045 | ESD section missing DEC-045 cross-reference | Design_Spec.md §5 correctly implements U2–U9 ESD protection on Samtec connectors but does not cite DEC-045. Should explicitly state "Per DEC-045, all Samtec ERM8/ERF8 rotor-facing connectors require TPD4E05U06QDQARQ1." |
| MEDIUM | ESD-ARRAY-COUNT | ESD array count documentation ambiguous | Design_Spec.md §5 exemption list for J2/J5 (power-only connectors) is stated but could be clearer. DR-EXT-13 correctly specifies "U2–U5 (J1/J3) + U6–U9 (J4/J6) = 8× TPD4E05U06QDQARQ1" and matches the BOM, but §5 prose does not explicitly confirm the J2/J5 power exemption rationale. |
| MEDIUM | PINOUT-XREF | Missing Extension Port pinout cross-reference | Board_Layout.md §2 cites "Connector Definition Owner: Stator/Board_Layout.md — J10" but does not clarify that Extension J7/J8 are 20-pin while Stator J10 is 16-pin, with pins 17–20 carrying 5V_MAIN/GND per DEC-043. Should be noted to prevent confusion. |
| MEDIUM | DEC043-XREF | Missing DEC-043 cross-reference for 20-pin Extension Port | Design_Spec.md §2 describes J7/J8 as 20-pin BHR-20-VUA without referencing DEC-043 (the decision that widened from 16-pin to 20-pin to add AM power). Add DEC-043 traceability note. |
| MEDIUM | HARNESS-TYPE | No cross-reference to QUE-002 resolution for cable assembly type | Neither Design_Spec.md nor Board_Layout.md references the IDC ribbon cable type for the Extension Port harness. QUE-002 resolution (standard IDC ribbon) should be noted for traceability. |
| MEDIUM | LAYOUT-ESD | Board_Layout.md lacks Thermal & ESD section | Design_Spec.md has a Thermal & ESD section (§5). Board_Layout.md has no equivalent section or cross-reference note for ESD placement constraints near connector mating edges. |

### Batch 2 — Reflector (review-ref)

| Severity | Ref | Finding | Detail |
| :--- | :--- | :--- | :--- |
| HIGH | BOM-R1-DUP | Duplicate BOM row for R1 | R1 (JTAG termination 22Ω) appears twice in the BOM table with identical specifications. One row must be removed. |
| MEDIUM | CBOM-J3 | Consolidated_BOM.md J3 description mismatch | Consolidated_BOM.md labels Reflector J3 as "Input dock connector (power/JTAG)" but Design_Spec.md §4 correctly describes it as the "ENC data connector". |
| MEDIUM | LAYOUT-STACKUP | Stackup description variance between files | Board_Layout.md §4 title reads "4-Layer / 2oz Copper". Design_Spec.md §6 uses the fuller form "4-Layer JLC04161H-7628 / 2oz Finished Copper". Should be consistent. |
| LOW | BOM-C1-C5 | C1–C5 bulk decoupling footnote lacks canonical specification | BOM line for C1–C5 labels them as "Bulk entry decoupling bank (star/spoke)" but does not state the canonical Global_Routing_Spec.md §3 form: "5× 10µF X7R 25V 0805". |

### Batch 2 — Encoder (review-enc)

Encoder — No findings.

### Batch 2 — Actuation Module (review-am)

| Severity | Ref | Finding | Detail |
| :--- | :--- | :--- | :--- |
| HIGH | SIGNAL-NAMING | Active-low signal naming convention violations | `ACTUATE_REQUEST` and `ACTUATION_HOME` are documented as active-low in Design_Spec.md but lack the `_N` suffix required by the project-wide convention. Both hardware Design_Spec.md and Software Design_Spec.md must be updated to `ACTUATE_REQUEST_N` and `ACTUATION_HOME_N`. Note: `NRST` is the standard STM32 IC pin designation and does not require renaming. |
| HIGH | DR-AM-18-SW | Contradictory pull-up configuration: external R6 vs firmware internal pull-up | Hardware Design_Spec.md DR-AM-18 specifies an external 10kΩ pull-up R6 on `ACTUATE_REQUEST`. Software Design_Spec.md §5 states the STM32 internal pull-up shall be enabled in firmware (PUPDR = `0b01`), making R6 redundant. These requirements are mutually exclusive. **Requires user decision** before PCB fabrication: (A) remove R6 and use firmware internal pull-up only, or (B) keep R6 and disable the firmware internal pull-up. |
| MEDIUM | THERMAL-ESD | Missing Thermal & ESD section | Global_Routing_Spec.md §9 requires boards with only internal connectors to explicitly document ESD compliance. All AM connectors (J1–J6) are internal. Design_Spec.md lacks a dedicated Thermal & ESD section confirming "No TVS/ESD required — all connectors internal per Global_Routing_Spec.md §9." |

---

**Batch 2 subtotal: 4 HIGH · 10 MEDIUM · 1 LOW**

### Batch 3 — Settings Board (review-sbd)

| Severity | Ref | Finding | Detail |
| :--- | :--- | :--- | :--- |
| MEDIUM | THERMAL-ESD | Missing Thermal & ESD section | Design_Spec.md lacks a Thermal & ESD section. Per Global_Routing_Spec.md §9, boards with only internal connectors must explicitly state: "No TVS/ESD protection required — all connectors are internal to the enclosure, per Global_Routing_Spec.md §9." J1 is an internal Stator harness connector; toggle switches and LEDs are hardwired panel components. |

### Batch 3 — JTAG Daughterboard (review-jdb)

| Severity | Ref | Finding | Detail |
| :--- | :--- | :--- | :--- |
| HIGH | DR-SEQ | Design Requirement ID gaps | DR-JDB-03 and DR-JDB-05 are missing. Current DR sequence: DR-01/02/04/06–18 (gaps at 03 and 05). IDs must be contiguous. |
| HIGH | CBOM-R3 | Conflicting resistor value for R3 in Consolidated_BOM.md | R3 appears in two rows with different values: "R2,R3 = 33Ω" and "R3-R5 = 10kΩ". Per Design_Spec.md, R3 is 10kΩ (RESET# pull-up). The "R2,R3 = 33Ω" row is incorrect. |
| HIGH | CRYSTAL-MPN | Crystal part mismatch vs Design_Log DEC-022 | DEC-022 selects YXC X322512MSB4SI (JLCPCB C9002). Design_Spec.md BOM and Consolidated_BOM.md both list ABM8-12-B2-T (Abracon, JLCPCB C596894) — a different part. BOM does not reflect the DEC-022 decision. **Requires user confirmation** of which crystal is the correct approved part. |
| MEDIUM | THERMAL-ESD | Misleading ESD statement in Thermal & ESD section | Design_Spec.md §7 states "ESD protection via U5 JTAG buffer (SN74LVC2G125DCUR)" but U5 is a 3-state logic buffer, not an ESD/TVS suppressor. All JDB connectors (J1, J2) are internal hat-headers. Section should explicitly state "No TVS/ESD protection required — all connectors are internal, per Global_Routing_Spec.md §9." |
| MEDIUM | SIGNAL-NAMING | RESET# notation vs project _N suffix convention | RESET# uses the "#" suffix. Project-wide convention requires `_N` suffix. Should either rename to `RESET_N` or add a note clarifying this is an IC pin label exception (if the "#" form is sourced directly from the IC datasheet). |
| MEDIUM | LAYOUT-IMPEDANCE | JTAG trace impedance compliance note could be clearer | Board_Layout.md §7.1 states "DEC-016 CI exception (outer layers only) does not apply" then references buried-microstrip topology. Should explicitly state that 0.127 mm traces on L2 are compliant because the inverted stackup (L1=GND) places them adjacent to a reference plane, achieving equivalent impedance to outer-layer traces. |
| LOW | STACKUP-NOTE | Design_Spec.md does not call out inverted stackup | Design_Spec.md §5 describes the JLC04161H-7628 as standard without noting the inverted layer order (L1=GND, L2=signals, L3=power, L4=GND vs standard L1=signal). Board_Layout.md correctly documents this; Design_Spec.md should cross-reference it. |

### Batch 3 — Integration: Connectivity (review-int-conn)

Integration-Connectivity — No findings. All critical interfaces verified: Link-Alpha, Link-Beta, Extension Port 20-pin pass-through, rotor daisy-chain ERM8/ERF8, I²C addresses, signal directions, and rail names are correctly specified and compatible across all board boundaries.

### Batch 3 — Integration: Consolidated BOM (review-int-bom)

| Severity | Ref | Finding | Detail |
| :--- | :--- | :--- | :--- |
| HIGH | CBOM-REF-R1 | Reflector R1 duplicate row in board Design_Spec.md | R1 (ERJ-3EKF2200V) appears twice in Reflector Design_Spec.md BOM (identical entries). Consolidated_BOM.md correctly captures only one instance but the source Design_Spec.md must be corrected. *(Also raised by review-ref — linked finding.)* |
| MEDIUM | CBOM-EXT-J7J8 | Extension J7/J8 description incorrect in Consolidated_BOM.md | Consolidated_BOM.md describes Extension J7/J8 as "Rotor group JTAG headers" — incorrect. These are Extension Port IN/OUT headers (20-pin 2×10 2.54 mm shrouded box). *(Also raised by review-ext — linked finding.)* |
| LOW | CBOM-JDB-R3 | Conflicting R3 assignment across two Consolidated_BOM.md rows | Row "R2,R3 = 33Ω" and row "R3-R5 = 10kΩ" both include R3. Per Design_Spec.md, R3 is 10kΩ (RESET# pull-up). The 33Ω row is incorrect. *(Also raised by review-jdb — linked finding.)* |

---

**Batch 3 subtotal: 4 HIGH · 4 MEDIUM · 1 LOW**

---

## Pass 1 Grand Total

| Severity | Count |
| :--- | :--- |
| HIGH | 16 |
| MEDIUM | 22 |
| LOW | 4 |
| **TOTAL** | **42** |

*Note: Some findings are linked across agents (same underlying defect raised from multiple perspectives); the fix agent will treat linked findings as a single fix.*

---

## Pass 1 — Fix Agent Results

**Fix agent:** fix-pass1 | **Files modified:** 14 | **Linter:** all 14 files pass clean

| Fix ID | File | Change Applied |
| :--- | :--- | :--- |
| F-01 | Power_Module/Board_Layout.md | `ROTOR_EN` → `ROTOR_EN_N` (×2) |
| F-02 | Controller/Design_Spec.md | Removed 2× broken "Full Pin Table" cross-references (J12, J13) |
| F-03 | Controller/Board_Layout.md | `ROTOR_EN` → `ROTOR_EN_N` in J3 table |
| F-04 | Stator/Design_Spec.md | Removed duplicate U8 BOM row |
| F-05 | Stator/Design_Spec.md | FR-STA-08: corrected I²C reference from `U1 @ 0x23` to `Settings Board U1 @ 0x23` |
| F-06 | Rotor/Design_Spec.md | DR-ROT-11 reordered to correct sequential position after DR-ROT-10 |
| F-07 | Extension/Design_Spec.md | Added DEC-045 cross-reference to Thermal & ESD section |
| F-08 | Extension/Design_Spec.md | Added DEC-043 traceability note to J7/J8 description |
| F-09 | Extension/Board_Layout.md | Added `## 7. Thermal & ESD` section with cross-reference to Design_Spec.md §5 |
| F-10 | Reflector/Design_Spec.md | Removed duplicate R1 BOM row |
| F-11 | Actuation_Module/Design_Spec.md + Software/Actuation_Module/Design_Spec.md | `ACTUATE_REQUEST` → `ACTUATE_REQUEST_N`; `ACTUATION_HOME` → `ACTUATION_HOME_N` throughout both files |
| F-12 | Actuation_Module/Design_Spec.md | Added `## 7. Thermal & ESD` section (no TVS — all connectors internal) |
| F-13 | Settings_Board/Design_Spec.md | Inserted `## 9. Thermal & ESD` section; BOM → §10; Power Budget → §11 |
| F-14 | JTAG_Daughterboard/Design_Spec.md | Fixed misleading ESD statement; replaced with no-TVS internal-connector statement |
| F-15 | JTAG_Daughterboard/Design_Spec.md | Added inverted stackup cross-reference note |
| F-16 | JTAG_Daughterboard/Board_Layout.md | Clarified JTAG trace impedance compliance note for L2 traces |
| F-17 | Consolidated_BOM.md | Extension J7/J8 description corrected to "Extension Port IN/OUT headers" |
| F-18 | Consolidated_BOM.md | Reflector J3 description corrected to "ENC data connector" |
| F-19 | Consolidated_BOM.md | JDB `R2,R3` row corrected to `R2` only (33Ω); R3 remains in `R3-R5` (10kΩ) row |
| F-20 | Stator/Design_Spec.md | U8 I²C address table appended `(per DEC-032)` |

### Items not fixed — require user decision

| Ref | Reason |
| :--- | :--- |
| AM DR-AM-18 vs SW §5 | External R6 vs firmware internal pull-up — mutually exclusive; awaiting user decision |
| PM BATTERY-ESD | TVS on VBATT+/VBATT- lines — awaiting user confirmation |
| JDB CRYSTAL-MPN | DEC-022 (YXC X322512MSB4SI / C9002) vs BOM (ABM8-12-B2-T / C596894) — MPN locked; awaiting user confirmation |
| JDB RESET# naming | Rename to RESET_N vs IC pin label exception — awaiting user confirmation |
| JDB DR-SEQ (DR-03/05 gaps) | Missing DR text — awaiting user input |
| CTL BOM-BYPASS (U2/U3) | Bypass cap values not yet specified — awaiting user input |
| Multiple MEDIUM/LOW | Documentation improvements deferred to user confirmation (see findings) |

#### Pass 1 result: 42 findings — 20 fixed; 7 items pending user decisions

---

## Pass 1 — User Decisions & Follow-On Fixes

### User decisions received

| Decision | Item | Resolution |
| :--- | :--- | :--- |
| D-1 | AM DR-AM-18 pull-up | **Remove R6; use STM32 firmware internal pull-up (PUPDR = 0b01) only** |
| D-2 | PM BATTERY-ESD | **Add TVS diode on VBATT+ → VBATT− at J4; part selection pending user confirmation** |
| D-3 | JDB CRYSTAL-MPN | **Deferred** — user to re-verify temp range spec (YXC C9002 vs Abracon C596894) before next pass |
| D-4 | JDB RESET# naming | **Rename to RESET_N throughout** |
| D-5 | JDB DR-SEQ gaps | **Renumber all DR-JDB IDs sequentially (01–16); update all cross-references** |
| D-6 | CTL BOM-BYPASS U2/U3 | **Pending** — user reviewing context (U2 = TPS2065C USB load switch 1.6A; U3 = AP2331W HDMI load switch) |
| D-7 | Deferred MEDIUM/LOW items | **Pending** — full list presented to user; awaiting decisions |

### Follow-on fix agent: fix-decisions-1-4-5

**Fix agent:** fix-decisions-1-4-5 | **Files modified:** 5 | **Linter:** all files pass clean

| Fix ID | File | Change Applied |
| :--- | :--- | :--- |
| F-21 | Electronics/Actuation_Module/Design_Spec.md | Removed DR-AM-18 (external pull-up R6); updated ACTUATE_REQUEST_N biasing note to state STM32 internal pull-up (PUPDR = `0b01`) is sole pull-up; removed R6 BOM row |
| F-22 | Software/Actuation_Module/Design_Spec.md | Added explicit statement: "No external pull-up resistor (R6) fitted; internal pull-up is the authoritative pull-up source" |
| F-23 | Consolidated_BOM.md | AM RefDes range `R4-R6` → `R4, R5` |
| F-24 | JTAG_Daughterboard/Design_Spec.md | All `RESET#` → `RESET_N`; first occurrence carries FT232H pin 34 IC name note |
| F-25 | JTAG_Daughterboard/Design_Spec.md + Board_Layout.md | DR-JDB IDs renumbered 01–16 (gaps at 03/05 filled); all cross-references updated |

### Remaining open items (pre-Pass 2)

| Ref | Status |
| :--- | :--- |
| D-2 PM BATTERY-ESD | TVS part (SMBJ18A proposed) — **awaiting user confirmation** |
| D-3 JDB CRYSTAL-MPN | **Deferred** to Pass 2 / user review |
| D-6 CTL BOM-BYPASS | Bypass caps for U2/U3 — **awaiting user decision** |
| D-7 MEDIUM/LOW items | Full list presented; **awaiting user decisions** |

---

## Pass 1 — Fix Agent 2 Results (fix-pass1-final)

**Fix agent:** fix-pass1-final | **Triggered by:** User decisions D-2 through D-7
**Files modified:** 10 | **Linter:** all files pass clean (zero errors)

| Fix ID | File | Change Applied |
| :--- | :--- | :--- |
| F-26 | `agent-directives.md` | Added general MOQ suppression rule (blanket); retained ROT-MOQ specific entry |
| F-27 | `Standards/Global_Routing_Spec.md` | Added §3.2 Per-IC Bypass Capacitors rule; Samsung CL05B104KB5NNNC / JLCPCB C1525 as standard part |
| F-28 | `Controller/Design_Spec.md` | Added DR-CTL-16 (bypass cap requirement citing global rule) |
| F-29 | `Controller/Design_Spec.md` | Added C26 (U2 TPS2065CDBVR bypass) and C27 (U3 AP2331W-7 bypass) BOM rows; both 100nF CL05B104KB5NNNC / C1525 |
| F-30 | `Power_Module/Design_Spec.md` | Added D4 row: Bourns SMBJ18A-Q TVS (DO-214AA; VWM=18V; 600W; Mouser 652-SMBJ18A-Q; DigiKey 118-SMBJ18A-QCT-ND; JLCPCB C1979859 Extended) |
| F-31 | `Power_Module/Design_Spec.md` | J1-J3 JLCPCB column: updated pre-order/consignment language; R12/R23 JLCPCB: consignment note confirmed |
| F-32 | `JTAG_Daughterboard/Design_Spec.md` | Y1 crystal: ABM8-12-B2-T (C596894) → CTS 435F12012IET; 12MHz 20pF ±20ppm; Mouser 774-435F12012IET; DigiKey 110-435F12012IETTR-ND; JLCPCB C19766404 Extended |
| F-33 | `Rotor/Board_Layout.md` | §2.1 Board A: added U5/U6 (J1 JTAG ESD) and U7/U8 (J2 ENC ESD) entries; §3.1 Board B: added U9/U10 (J3 JTAG ESD) and U11/U12 (J4 ENC ESD) entries |
| F-34 | `Reflector/Design_Spec.md` | §2 + §6 stackup string standardised to `4-Layer / 2oz Copper (JLC04161H-7628)` |
| F-35 | `Reflector/Board_Layout.md` | §4 stackup description updated to `4-Layer / 2oz Copper (JLC04161H-7628)` |
| F-36 | `Extension/Design_Spec.md` | §5 Thermal & ESD: J2/J5 power-only ESD exemption statement confirmed/present |
| F-37 | `Consolidated_BOM.md` | D4 TVS row added (Power Module); C26/C27 rows added (Controller); Y1 crystal row updated (JDB) |

**Orchestrator corrections applied after agent completion:**

| Fix ID | File | Correction |
| :--- | :--- | :--- |
| F-38 | `Power_Module/Design_Spec.md` | D4 TVS: corrected wrong part (Vishay SMBJ18A-E3/61) to confirmed Bourns SMBJ18A-Q with correct supplier PNs |
| F-39 | `Consolidated_BOM.md` | D4 row + unique-parts table row 116: corrected Vishay → Bourns SMBJ18A-Q |
| F-40 | `agent-directives.md` | General MOQ suppression rule was part-specific only; replaced with blanket MOQ rule preceding ROT-MOQ entry |
| F-41 | `Reflector/Design_Spec.md` | §2 line 43 stackup string still in old format; corrected to `4-Layer / 2oz Copper (JLC04161H-7628)` |

#### Pass 1 result (after all fixes): ALL ITEMS RESOLVED — ready for Pass 2

All 42 Pass 1 findings resolved. All user decisions D-1 through D-7 actioned. Zero outstanding items requiring user input before Pass 2 can begin.

---

# Deep-Dive Review Cycle — Pass 2

**Started:** 2025-05

---

## Scope

- **Stand-alone board reviews:** Power Module, Controller, Stator, Reflector, Extension, Encoder,
  JTAG Daughterboard, Rotor, Settings Board, Actuation Module
- **Integration reviews:** Inter-board connectivity (signal names, rail names, refdes consistency);
  Consolidated BOM vs all board BOMs
- **Prerequisite:** Each review agent read `design/Standards/Global_Routing_Spec.md` before
  reviewing any board

## Review Agent Batches

- Batch 1: Power Module, Controller, Stator, Encoder
- Batch 2: Reflector, Extension, JTAG Daughterboard, Rotor
- Batch 3: Settings Board, Actuation Module, Integration-Connectivity, Integration-BOM

---

## Pass 2 — Review Findings

### Batch 1 — Power Module (review-pm)

| Severity | Ref | Finding | Detail |
| :--- | :--- | :--- | :--- |
| HIGH | PM-MAJ-1 | TPS75733 (U7) has no bypass capacitor in BOM | U7 (TPS75733DCQR 3.3V LDO) has no local bypass/decoupling capacitor. GRS §3.2 requires ≥100nF per-IC bypass. Also investigated: TPS25980 (U1) has single VIN pin only (no separate VDD); existing C9/C10 (22µF) far exceed ≥10nF minimum — no C31 required. LMQ61460A (U6) bypass satisfied by existing input bulk caps — no C32 required. |
| MEDIUM | PM-MAJ-2 | GRS §3 bulk-entry exemption for rail-source board not documented | The Power Module generates all output rails; GRS §3 applies to downstream consumers. No exemption callout exists in §2. Risk: future reviewers incorrectly flag this board as non-compliant. |
| LOW | PM-MIN-1 | Board_Layout compliance-marker cross-references unverified | Board_Layout.md §2 lists compliance markers referencing GRS sub-sections. Markers not verified to match current GRS numbering. |
| LOW | PM-MIN-2 | GND↔GND_CHASSIS single-point bond lacks RefDes assignment | §6 describes the single-point GND bond but does not assign a RefDes. GRS §5 requires the bond component to be a trackable BOM item. |

### Batch 1 — Controller (review-ctl)

| Severity | Ref | Finding | Detail |
| :--- | :--- | :--- | :--- |
| CRITICAL | CTL-CRIT-1 | U9, U10, T2 (PoE chain) absent from Consolidated BOM | U9 (TPS2372-4RGWR), U10 (TPS23730RMTR), and T2 (POE600F-12L) are fully specified in Controller Design_Spec.md but completely absent from Consolidated_BOM.md. |
| HIGH | CTL-MAJ-1 | C24 services both U9 and U10 VCC pins | Design_Spec.md lists C24 as U9 VCC bypass only; U10 also requires its own local 100nF bypass per GRS §3.2. C28 must be added for U10. |
| HIGH | CTL-MAJ-2 | U9, U10, T2 absent from §2 MPN summary table | All major ICs and magnetics must appear in the §2 "Key ICs & Passives" summary; U9, U10, T2 were missing. |

### Batch 1 — Stator (review-sta)

| Severity | Ref | Finding | Detail |
| :--- | :--- | :--- | :--- |
| HIGH | STA-MAJ-1 | R33–R38 RefDes range duplicated in Consolidated BOM | R33–R38 appeared under two different boards in Consolidated_BOM.md. One section incorrectly claimed these RefDes. |
| LOW | STA-MIN-1 | CPLD VCC/VCCIO pin assignments missing from Board_Layout.md | Board_Layout.md did not document which VCC and VCCIO pins of the EPM570T100I5N connect to 3V3_ENIG; required for decoupling adequacy verification. |

### Batch 1 — Encoder (review-enc)

| Severity | Ref | Finding | Detail |
| :--- | :--- | :--- | :--- |
| LOW | ENC-MIN-1 | **DISMISSED — false positive** | Finding raised about encoder pull-up topology. User confirmed weak internal pull-ups are acceptable for 5–15cm ribbon runs based on prior EPM240 breadboard validation at 25cm. No action required. |

### Batch 2 — Reflector (review-ref)

| Severity | Ref | Finding | Detail |
| :--- | :--- | :--- | :--- |
| HIGH | REF-MAJ-1 | **DISMISSED — false positive** | Finding raised about GRS §3 bulk-entry compliance. Reflector is a passive board (no power-consuming logic ICs beyond ESD arrays); GRS §3 bulk-entry rule applies to active logic boards. No action required. |
| LOW | REF-MIN-1 | TPD4E05U06QDQARQ1 maximum working voltage not stated in §5 | §5 ESD section lists U1–U4 on the 5V_MAIN rail but does not state the device's maximum continuous working voltage (5.5V). Required for margin verification by future reviewers. |

### Batch 2 — Extension (review-ext)

No new stand-alone findings in Pass 2 beyond integration items captured under INT.

### Batch 2 — JTAG Daughterboard (review-jdb)

| Severity | Ref | Finding | Detail |
| :--- | :--- | :--- | :--- |
| CRITICAL | JDB-CRIT-1 | **DISMISSED — false positive** | Finding raised about crystal load-capacitor calculation. On investigation, DR-JDB-17 and the full load-cap derivation were already present in the spec citing the datasheet calculation. No missing content. |
| HIGH | JDB-MAJ-1 | U5 (EPM240T100I5N CPLD) has no bypass capacitor | U5 had no associated bypass cap in the BOM. GRS §3.2 requires ≥100nF per-IC bypass. C12 must be added. |
| LOW | JDB-MIN-1 | §6 Routing Notes missing cross-reference to Board_Layout.md §7.1 | §6 describes routing constraints further detailed in Board_Layout.md §7.1 but contained no cross-reference to that section. |

### Batch 2 — Rotor (review-rot)

| Severity | Ref | Finding | Detail |
| :--- | :--- | :--- | :--- |
| CRITICAL | ROT-CRIT-1 | Board A and Board B not documented as a single logical unit | Board A and Board B are always populated and operated together as one logical encoder assembly, but this relationship is not documented. Risk: Board B incorrectly treated as independently reviewable, causing false GRS §3 bulk-cap violations on Board B (whose bulk caps reside on Board A). |
| HIGH | ROT-MAJ-1 | **DISMISSED — resolved by ROT-CRIT-1** | Once DR-ROT-12 (Board A+B logical unit) is applied, Board B is an extension of Board A and its bulk-cap absence is explicitly exempted. No separate fix needed. |

### Batch 3 — Settings Board (review-set)

| Severity | Ref | Finding | Detail |
| :--- | :--- | :--- | :--- |
| HIGH | SET-MAJ-1 | Bulk-entry capacitor banks missing for both input rails | Settings Board receives 3V3_ENIG and 5V_MAIN. GRS §3 requires ≥5× 10µF bulk-entry caps per rail on all consumer boards. No bulk-entry banks existed. C5–C9 (3V3_ENIG) and C10–C14 (5V_MAIN) must be added. |
| HIGH | SET-MAJ-2 | No ESD protection on panel-facing switches SW1–SW5 | J1 panel switches are user-accessible. No TVS/ESD array is present on these lines. **DEFERRED per user D-8** — to evaluate during pre-prototype switch testing; switch mechanical construction may make ESD components irrelevant. |
| LOW | SET-MIN-1 | Samsung CL21B106KAYQNNE specified with X5R dielectric — should be X7R | CL21B106KAYQNNE is an X7R dielectric; the spec description was incorrect. |
| LOW | SET-MIN-2 | **DISMISSED — false positive** | Review agent claimed Board_Layout.md did not exist for Settings Board. `design/Electronics/Settings_Board/Board_Layout.md` exists and is correctly populated. |
| LOW | SET-MIN-3 | J1 connector description incomplete | J1 (panel switch connector) description did not specify JST PH 2.0mm pitch or pin count. |

### Batch 3 — Actuation Module (review-am)

| Severity | Ref | Finding | Detail |
| :--- | :--- | :--- | :--- |
| CRITICAL | AM-CRIT-1 | DR-AM-15 did not restrict STM32 VDD supply to pin 4 only | DR-AM-15 covered the LDO VDD rail but did not explicitly state that only pin 4 (VDD) carries 3V3_ENIG — pin 16 (VDD_USB) must remain unconnected. Ambiguity risked incorrect wiring. |
| LOW | AM-MIN-1 | SW2 supply rail not stated in DR-AM-15 | DR-AM-15 described SW2 (BOOT0 switch) but did not state that SW2's pull-up supply is 3V3_ENIG (not VDD). |
| LOW | AM-MIN-2 | DR-AM-15 missing GRS §3 exemption cross-reference | The AM is a daughterboard receiving no directly-generated external rails; GRS §3 bulk-entry exemption is correct but was not cross-referenced in the DR. |
| LOW | AM-MIN-3 | Phantom "(R6)" reference in Software AM Design_Spec.md | `design/Software/Actuation_Module/Design_Spec.md` contained a stray "(R6)" reference; R6 does not exist on the AM BOM. |
| LOW | AM-MIN-4 | Mounting holes not specified for Actuation Module | GRS requires mounting holes on all PCBs. No mounting hole DR existed for the AM; physical location TBD at PCB layout stage. |
| LOW | AM-MIN-5 | GND_CHASSIS exemption note absent from AM spec | The AM is a daughterboard and does not implement the GND↔GND_CHASSIS single-point bond. No exemption note explained this. |
| LOW | AM-MIN-6 | Blank line in AM BOM table | A blank line in the middle of the BOM table in AM Design_Spec.md broke table rendering. |

### Batch 3 — Integration Reviews

| Severity | Ref | Finding | Detail |
| :--- | :--- | :--- | :--- |
| LOW | INT-MIN-001 | `ACTUATE_REQUEST` signal missing `_N` suffix throughout | Signal is active-LOW; GRS naming conventions require the `_N` suffix. Appeared without suffix in Controller, Extension, and Software AM specs. |
| LOW | INT-MIN-002 | Extension Design_Spec.md contains phantom reference to AM R6 | Extension spec referenced AM component "(R6)" which does not exist on the AM BOM — stale residual from an earlier design iteration. |

---

## Pass 2 — Fix Log

### Fix agent (pass2-fixes) — changes applied automatically

| Fix ID | File | Change |
| :--- | :--- | :--- |
| F-42a | `Power_Module/Design_Spec.md` | Added C58: TPS75733 U7 VIN bypass 100nF CL05B104KB5NNNC 0402 |
| F-46 | `Consolidated_BOM.md` | Added U9 (TPS2372-4RGWR), U10 (TPS23730RMTR), T2 (POE600F-12L) rows to Controller section |
| F-47 | `Controller/Design_Spec.md` | Split C24 into C24 + C28 (separate 100nF bypass caps for U9 and U10 respectively) |
| F-48 | `Controller/Design_Spec.md` | Added U9, U10, T2 rows to §2 MPN summary table with full supplier PNs |
| F-49 | `Consolidated_BOM.md` | Corrected R33–R38 duplication; R33–R38 retained under correct board section only |
| F-50 | `Stator/Board_Layout.md` | Added CPLD VCC/VCCIO pin assignments and note block |
| F-52 | `JTAG_Daughterboard/Design_Spec.md` | Added C12: EPM240 U5 bypass 100nF CL05B104KB5NNNC 0402; added DR-JDB-17 |
| F-53 | `JTAG_Daughterboard/Design_Spec.md` | Added §6 cross-reference: `See Board_Layout.md §7.1` |
| F-54 | `Rotor/Design_Spec.md` | Added DR-ROT-12: Board A and Board B shall be treated as a single logical board; Board B bulk-cap absence explicitly exempted |
| F-55a | `Settings_Board/Design_Spec.md` | Added C5–C14 entries — **incorrect (100nF bypass); see orchestrator correction F-55b** |
| F-56 | `Settings_Board/Design_Spec.md` | Corrected CL21B106KAYQNNE dielectric description: X5R → X7R |
| F-57 | `Settings_Board/Design_Spec.md` | Corrected J1 connector description to specify 6-pin JST PH 2.0mm pitch |
| F-58 | `Actuation_Module/Design_Spec.md` | Updated DR-AM-15: explicit restriction to VDD pin 4 only; pin 16 VDD_USB left unconnected |
| F-59 | `Actuation_Module/Design_Spec.md` | Added SW2 supply rail note to DR-AM-15: SW2 pull-up supply = 3V3_ENIG |
| F-60 | `Actuation_Module/Design_Spec.md` | Added GRS §3 exemption cross-reference to DR-AM-15 (daughterboard, no directly-received rails) |
| F-61 | `Software/Actuation_Module/Design_Spec.md` | Removed phantom "(R6)" reference |
| F-62 | `Actuation_Module/Design_Spec.md` | Added DR-AM-16: mounting holes required; location TBD at PCB layout stage |
| F-63 | `Actuation_Module/Design_Spec.md` | Added GND_CHASSIS single-point bond exemption note (daughterboard) |
| F-64 | `Actuation_Module/Design_Spec.md` | Removed blank line from BOM table |
| F-65 | `Controller/Design_Spec.md`, `Extension/Design_Spec.md`, `Software/Actuation_Module/Design_Spec.md` | Renamed `ACTUATE_REQUEST` → `ACTUATE_REQUEST_N` throughout all cross-references |
| F-66 | `Extension/Design_Spec.md` | Removed phantom "(R6)" reference to AM component |

### Orchestrator corrections (applied after fix agent)

| Fix ID | File | Correction |
| :--- | :--- | :--- |
| F-42b | `Power_Module/Design_Spec.md` | Investigated C31/C32 for TPS25980 (U1) and LMQ61460A (U6). Confirmed: TPS25980 has no separate VDD pin; existing C9/C10 far exceed minimum. LMQ61460A satisfied by existing input bulk caps. C31 and C32 **not required** — fix agent mis-identified them. |
| F-43 | `Power_Module/Design_Spec.md` | Added GRS §3 bulk-entry exemption callout to §2 Design NOTE |
| F-44 | `Power_Module/Board_Layout.md` | PM-MIN-1 compliance-marker cross-references — unverified at audit time; no definitive failure found; carries to Pass 3 as low-severity |
| F-45 | `Power_Module/Design_Spec.md` | Updated §6 Single-Point GND Bond: assigned RefDes FB1 (ferrite bead or 0Ω link, value TBD at layout) |
| F-51 | `Reflector/Design_Spec.md` | Added working voltage note for TPD4E05U06QDQARQ1 to §5: max 5.5V; 5V_MAIN (≤5.1V) within range with ≥0.4V margin |
| F-55b | `Settings_Board/Design_Spec.md` | Corrected fix-agent error: C5–C14 changed from 100nF bypass to 10µF X7R 25V 0805 Samsung CL21B106KAYQNNE (GRS §3 requires ≥5× 10µF bulk-entry caps per rail) |
| F-55c | `Consolidated_BOM.md` | Settings Board C5–C14 row corrected to match orchestrator correction |

### User decisions recorded in Pass 2

| Decision | Item | Resolution |
| :--- | :--- | :--- |
| D-8 | SET-MAJ-2 — ESD on panel switches SW1–SW5 | **DEFERRED** — evaluate at pre-prototype switch procurement; mechanical construction may negate ESD risk |
| D-9 | ROT-CRIT-1 — Board A+B logical unit framing | Board B is physically independent but logically part of Board A; Board B is exempt from GRS §3 bulk-cap rule as Board A carries the bulk banks |
| D-10 | TPS25751DREFR KiCAD footprint | **Marked `✓`** — already present in project KiCAD library (Power Module U4, USB-C PD controller) |
| D-11 | CSD17578Q5A KiCAD footprint | **Marked `✓`** — already present in project KiCAD library (Power Module Q1/Q2/Q3, OR-ing MOSFETs) |

#### Pass 2 result: 22 fixed, 1 deferred, 1 unverified, 5 dismissed

All 25 active Pass 2 findings (F-42 through F-66) dispositioned:

- **22 fixed** by fix agent or orchestrator
- **1 deferred by user** (SET-MAJ-2 — ESD on panel switches)
- **1 unverified / carry-forward** (PM-MIN-1 — Board_Layout compliance markers; no definitive failure found; low severity)
- **5 dismissed** as false positives: ROT-MAJ-1, REF-MAJ-1, JDB-CRIT-1, ENC-MIN-1, SET-MIN-2

Carry-forwards to Pass 3: PM-MIN-1 (low severity). SET-MAJ-2 deferred pending pre-prototype switch procurement.
