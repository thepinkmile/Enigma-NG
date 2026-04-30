# Checkpoint 081 — Pass 1 review cycle: all fixes applied and verified, ready for Pass 2

## Status

Review cycle Pass 1 complete. All 42 findings resolved. All user decisions actioned.
No git commit yet — awaiting explicit user approval.

## What was done

### New review cycle launched

A new additive electronics deep-dive review cycle was started (review-report.md recreated).
Three batches of review agents ran against all 11 board specs plus integration reviews.

### Pass 1 review findings and fixes — full summary

Total findings: **42** across all boards.

**Fix agent run 1 (fix-pass1)** — 20 fixes applied across 14 files:
- ROTOR_EN → ROTOR_EN_N across Power_Module and Controller board layouts and design specs
- Removed broken cross-references from Controller Design_Spec (J12/J13 "Full Pin Table" refs)
- Removed duplicate U8 BOM row from Stator Design_Spec
- Corrected Stator FR-STA-08 I²C address reference
- Reordered DR-ROT-11 to correct sequential position in Rotor Design_Spec
- Added DEC-045 and DEC-043 cross-references to Extension Design_Spec and Board_Layout
- Removed duplicate R1 BOM row from Reflector Design_Spec
- ACTUATE_REQUEST → ACTUATE_REQUEST_N and ACTUATION_HOME → ACTUATION_HOME_N in both
  Electronics and Software Actuation Module design specs
- Added Thermal & ESD §7 to Actuation_Module and Settings Board design specs
- Fixed ESD statement in JTAG Daughterboard; added inverted stackup cross-reference note
- Standardised JTAG Daughterboard Board_Layout JTAG trace impedance note
- Corrected Extension and Reflector BOM description rows in Consolidated_BOM.md

**User decisions received (D-1 through D-7)** and acted on:

| Decision | Item | Resolution |
| :--- | :--- | :--- |
| D-1 | AM pull-up R6 | Remove R6; use STM32 firmware internal pull-up (PUPDR = 0b01) |
| D-2 | Power Module TVS | Add Bourns SMBJ18A-Q TVS on VBATT+ at J4 |
| D-3 | JDB crystal | CTS 435F12012IET (12MHz, 20pF, ±20ppm, −40 to +85°C; JLCPCB C19766404) |
| D-4 | JDB RESET# naming | Rename to RESET_N throughout |
| D-5 | JDB DR-SEQ gaps | Renumber DR-JDB IDs 01–16 sequentially; update all cross-references |
| D-6 | CTL BOM-BYPASS | Add 100nF bypass caps C26/C27 for U2/U3 (Samsung CL05B104KB5NNNC / C1525) |
| D-7 | MEDIUM/LOW items | Individual sub-items actioned — see below |

**Additional design changes (during decision processing):**

- DEC-043 supersession note added to Design_Log.md clarifying it supersedes QUE-002 pin count
- QUE-002 amended to note it is superseded by DEC-043
- agent-directives.md updated: review agents must read Global_Routing_Spec.md before board specs
- Stator Board_Layout updated: U5/U6 (mux), U7 (Settings-board I²C), and U8 JTAG header sections
  added as functional feature entries
- Two new markdown datasheets generated: `design/Datasheets/bourns-smbj-q-datasheet.md` and
  `design/Datasheets/CTS-crystals-435-datasheet.md`

**D-7 sub-item resolutions:**

| Sub-item | Resolution |
| :--- | :--- |
| 7a JDB C9002 pre-order | Added consignment note: "pre-order part at JLCPCB" → then superseded by D-3 crystal change |
| 7b CSS2H-2512R-R010ELF | Confirmed invalid MPN; sourcing note updated to consignment-only (DigiKey/Mouser) |
| 7c Bypass caps U2/U3 | Covered by D-6 resolution |
| 7d Board_Layout scope | Confirmed: high-level functional features only; passives out of scope |
| 7e Global bypass cap rule | Added §3.2 to Global_Routing_Spec.md; Samsung CL05B104KB5NNNC standard part |
| 7f Rotor ESD arrays U5–U12 | Added U5/U6/U7/U8 (Board A) and U9/U10/U11/U12 (Board B) to Rotor Board_Layout §2.1/§3.1 |
| 7g Extension J2/J5 ESD | Confirmed §5 exemption statement present in Extension Design_Spec |
| 7h QUE-002 crystal | QUE-002 amended in Design_Log to record supersession by DEC-043; pin count resolved |
| 7i JDB J5/U1 connector mismatch | Investigated: J5 is programming header; U1 FT232H has SSOP-28. No mating needed. Added DEC-043 cross-reference note |
| 7j Stackup string format | Standardised to `4-Layer / 2oz Copper (JLC04161H-7628)` across Reflector and Extension docs |
| 7k Global bulk cap rule | Global_Routing_Spec.md §3.1 confirmed as authority; individual boards updated with cross-reference |
| 7l MOQ suppression rule | General blanket MOQ rule added to agent-directives.md Review Suppression section |

**Fix agent run 2 (fix-pass1-final)** — 9 confirmed fixes applied; orchestrator applied 4
post-agent corrections for wrong TVS manufacturer, incomplete MOQ suppression rule, and
residual stackup format inconsistency in Reflector Design_Spec §2.

### Files modified (cumulative — all agents + orchestrator corrections)

| File | Change summary |
| :--- | :--- |
| `.copilot/agent-directives.md` | SECONDARY DIRECTIVE; review cycle process; global read-first rule; general MOQ suppression; ROT-MOQ specific suppression |
| `.copilot/review-report.md` | Created; all Pass 1 findings and resolutions recorded |
| `design/Standards/Global_Routing_Spec.md` | §3.2 Per-IC Bypass Capacitors rule added (100nF CL05B104KB5NNNC / C1525) |
| `design/Design_Log.md` | DEC-043 supersession note added; QUE-002 amended |
| `design/Electronics/Consolidated_BOM.md` | D4 TVS (Bourns SMBJ18A-Q), C26/C27 bypass caps, Y1 crystal, AM R4/R5 range, JDB R2 row, Extension/Reflector descriptions corrected |
| `design/Electronics/Power_Module/Design_Spec.md` | D4 TVS row (Bourns SMBJ18A-Q; 652-SMBJ18A-Q; 118-SMBJ18A-QCT-ND; C1979859); sourcing notes |
| `design/Electronics/Controller/Design_Spec.md` | DR-CTL-16 added; C26/C27 BOM rows (100nF bypass for U2/U3) |
| `design/Electronics/Stator/Design_Spec.md` | Duplicate U8 row removed; FR-STA-08 I²C ref corrected; U8 address DEC-032 note |
| `design/Electronics/Stator/Board_Layout.md` | U5/U6 mux, U7 Settings-board I²C, U8 JTAG header sections added |
| `design/Electronics/Rotor/Design_Spec.md` | DR-ROT-11 reordering |
| `design/Electronics/Rotor/Board_Layout.md` | U5–U8 (Board A) and U9–U12 (Board B) ESD array rows added |
| `design/Electronics/Extension/Design_Spec.md` | DEC-045 cross-ref, DEC-043 traceability, J2/J5 ESD exemption, stackup standardised |
| `design/Electronics/Extension/Board_Layout.md` | Thermal & ESD section added |
| `design/Electronics/Reflector/Design_Spec.md` | Duplicate R1 removed; stackup string standardised in both §2 and §6 |
| `design/Electronics/Reflector/Board_Layout.md` | Stackup standardised |
| `design/Electronics/JTAG_Daughterboard/Design_Spec.md` | Y1 crystal → CTS 435F12012IET; RESET# → RESET_N; DR-JDB IDs renumbered 01–16; ESD statement fixed; stackup cross-ref note |
| `design/Electronics/JTAG_Daughterboard/Board_Layout.md` | JTAG trace impedance note clarified |
| `design/Electronics/Actuation_Module/Design_Spec.md` | DR-AM-18 removed; R6 removed; ACTUATE_REQUEST_N/_HOME_N renamed; Thermal & ESD §7 added |
| `design/Electronics/Settings_Board/Design_Spec.md` | Thermal & ESD §9; BOM → §10; Power Budget → §11 |
| `design/Software/Actuation_Module/Design_Spec.md` | No-external-pull-up statement added; signal renames |
| `design/Datasheets/bourns-smbj-q-datasheet.md` | Created — Bourns SMBJ18A-Q TVS markdown datasheet |
| `design/Datasheets/CTS-crystals-435-datasheet.md` | Created — CTS 435F12012IET crystal markdown datasheet |
| `design/Electronics/Power_Module/Board_Layout.md` | ROTOR_EN → ROTOR_EN_N (×2) |
| `design/Electronics/Controller/Board_Layout.md` | ROTOR_EN → ROTOR_EN_N |

## Next steps

- Await explicit user approval for git commit
- Then launch Pass 2 review cycle
- Pass 2 scope: same 11 boards + integration — fresh eyes after all Pass 1 fixes applied
