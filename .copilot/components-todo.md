# Enigma-NG -- Component Re-Verification Table

> Updated: 2026-04-18 (evening review sync 2)
> Canonical single-table workspace for manual component re-verification.
> Treat every populated candidate field as provisional until the row is explicitly marked `VERIFIED`.
> Do not propagate data from this file back into design docs until re-verification is complete.
> ERA datasheet: `design/Datasheets/Panasonic-ERA-datasheet.pdf`
>
> **Table consolidation:** All 107 unique component types from Consolidated_BOM.md are now tracked in one table below.
> Rows are organized by component category for easier batch verification.

---

## CURRENT REVIEW FOLLOW-UPS

| Item | Status | Notes |
| --- | --- | --- |
| Settings/Stator expander architecture revisit | TODO after current consistency pass | Revisit the Stator + Settings expander split, contiguous addressing, and HID decoder/lightboard ownership after the current review fixes are locked. User has a follow-on idea affecting the Encoder Boards. |
| Reflector/Extension chain audit follow-up | In progress | Active docs are being updated so the physical Reflector remains mandatory, Extensions stay optional in 5-rotor blocks, and rotor-chain I2C references are removed. |

### Missing local datasheets to fetch

| Component | Active refs | Notes |
| --- | --- | --- |

---

## SWITCHES & USER INPUT (9 items)

| # | Board | Ref | Specification to Verify | Candidate MPN | Candidate DigiKey | Candidate Mouser | Candidate JLCPCB | Verification | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S001 | PM + SBD | (historical) | Historical combined switch-selection row from the old unified-switch assumption | Superseded | Superseded | Superseded | Superseded | VERIFIED | Superseded by S002-S004 after the design split into dedicated Settings Board toggles + discrete LEDs and a separate rugged Power Module switch. |
| S002 | SBD | SW_B1_EN, SW_B1[0:3], SW_B2_EN, SW_B2[0:5] | SPDT latching sub-mini toggle; panel-mount; T2 actuator; B4 bushing; M2 termination; sealed base | 200MSP1T2B4M2QE | EG5525-ND | 612-200MSP1T2B4M2QE | C5491263 | VERIFIED | Settings Board panel toggles. Datasheet reviewed and MPN confirmed. System total: 12 units. |
| S003 | SBD | SW_CFG_APPLY | SPST NO momentary; board-mounted tactile switch is acceptable if mechanically actuated through the enclosure; positive tactile click; V >= 3.3V; I >= 50mA | B3F-1070 | SW406-ND | 653-B3F-1070 | C726011 | VERIFIED | User accepted the relaxed Settings Board requirement: a through-hole tactile switch behind a mechanical actuator is acceptable, so Omron B3F-1070 is now approved. Datasheet reviewed at `design/Datasheets/omron-en-b3f-switch-datasheet.pdf`. |
| S004 | PM | SW1 | Rugged metal latching power switch with RGB ring LED; 16mm panel cutout; 2.8mm pin terminals; serviceable harness to PCB spade tabs | Adafruit 4660 | 1528-4660-ND | 485-4660 | Global sourcing / consignment | VERIFIED | Power Module front-panel power switch with integrated RGB ring LED. Datasheet reviewed and MPN confirmed. |
| S005 | PM | SW2 | Momentary panel switch for `PWR_BUT`; 16mm panel cutout; NO contact; low-voltage logic only; RGB illumination acceptable for hold-signal indication | Adafruit 3350 | 1528-2546-ND | 485-3350 | Global sourcing / consignment | VERIFIED | User approved Adafruit 3350 as the SW2 part. Same 16mm rugged metal family as SW1, but momentary. LED ring may be used to indicate the 3-second held `PWR_BUT` signal / shutdown event. |
| S006 | ENC/Kbd | SW1-SW40 | Custom DPDT 6-pin momentary keyboard switch; 40 physical HID positions total (38 printable `[a-z0-9+=]` + Left/Right Shift); straight THT; 6 pins; 4 mm pin pitch; 42 x 9.7 x 18 mm nominal overall | uxcell-style seller part (MPN unspecified) | Global sourcing / consignment | Global sourcing / consignment | eBay item 365271584375 | VERIFIED | User confirmed the custom marketplace switch from eBay seller `gadgetskingdom`. Raw listing metadata was captured into `design/Datasheets/Gadgetskingdom_DPDT_Keyboard_Switch_Pseudo_Datasheet.md`. Treat as a consignment part installed during mechanical/final assembly rather than PCB assembly. |
| S007 | ROT | SW_CFG | CTS 219-6LPSTR — 6-pos DIP switch, 2.54mm THT | 219-6LPSTR | 119-219-6LPSTRCT-ND | 774-2196LPSTR | C2842671 | VERIFIED | Datasheet already present at `design/Datasheets/CTS-Switches-DIP-219-Series-Datasheet.pdf`, and the current Rotor Design_Spec already uses this exact MPN and distributor references. |
| S008 | PM | BT_SW1_1-BT_SW1_6, BT_SW2_1-BT_SW2_6 | 2.8mm (0.110in) vertical PCB-mount male blade terminal; mates with Adafruit 4660 / 3350 switch terminals for switch + RGB ring harnesses | Keystone 1211 | 36-1211-ND | 534-1211 | C3029550 | VERIFIED | User approved Keystone 1211 as the preferred THT/soldered Quick-Fit male PCB terminal. Use for both SW1 and SW2 harness tabs (12 total if both panel switches use full contact + LED wiring). |
| S009 | STA | SW3 | SPST NO momentary PCB-mount homing switch for SERVO_HOME | SS-01GL13 | SW865-ND | 653-SS-01GL13 | C3822088 | VERIFIED | Omron SS series homing switch for the Stator SERVO_HOME input. Local datasheet present at `design/Datasheets/omron-en-ss-switch-datasheet.pdf`. |

---

## LEDS & INDICATORS (2 items)

| # | Board | Ref | Specification to Verify | Candidate MPN | Candidate DigiKey | Candidate Mouser | Candidate JLCPCB | Verification | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L001 | SBD | LED_B1_EN, LED_B1[0:3], LED_B2_EN, LED_B2[0:5] | 5mm common-anode RGB through-hole LED; full RGB operation @ 5V (red 150Ω, green/blue 100Ω resistors); white diffused lens | WP154A4SEJ3VBDZGW/CA | 754-2029-ND | 604-WP154A43VBDZGWCA | C7151795 | VERIFIED | Settings Board RGB panel LEDs. Datasheet reviewed and MPN confirmed. Updated for 5V RGB upgrade (2026-04-17). System total: 12 units. |
| L002 | ENC | D1, D2 | 0402 green status LED; active-low CPLD indicators | 150060VS75000 | 732-4980-1-ND | 710-150060VS75000 | C6848499 | VERIFIED | Würth 0402 status LED for Encoder CPLD indicators. Local datasheet present at `design/Datasheets/150060VS75000-datasheet.pdf`. Mouser product resources include KiCad footprint and 3D model links. |

---

## IC: CPLD & PROGRAMMABLE LOGIC (2 items)

| # | Board | Ref | Specification to Verify | Candidate MPN | Candidate DigiKey | Candidate Mouser | Candidate JLCPCB | Verification | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IC001 | ENC | U1, U2 | EPM240T100I5N — Intel MAX II CPLD (TQFP-100) | EPM240T100I5N | TBD | TBD | TBD | RECHECK | 240 LEs; industrial temp; used on Encoder boards only. System total: 6 units. |
| IC002 | STA, ROT | U1 | EPM570T100I5N — Intel MAX II CPLD (TQFP-100; 570 LEs; drop-in for EPM240) | EPM570T100I5N | TBD | TBD | TBD | RECHECK | 570 LEs; industrial temp; used on Stator and Rotor boards. System total: 31 units (1 Stator + 30 Rotors). |

---

## IC: POWER MANAGEMENT (14 items)

| # | Board | Ref | Specification to Verify | Candidate MPN | Candidate DigiKey | Candidate Mouser | Candidate JLCPCB | Verification | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IC003 | PM | U7 | TPS75733KTTRG3 — 3.3 V LDO Regulator (TO-263 KTT 5-pin) | TPS75733KTTRG3 | TBD | TBD | TBD | RECHECK | 3A LDO for 3V3_ENIG system rail. |
| IC004 | PM | U5 | TPS259804ONRGER — eFuse / Hot-Swap Controller (VQFN-24) | TPS259804ONRGER | TBD | TBD | TBD | RECHECK | eFuse with silicon-fixed 16.9V OVLO. TPS259807 is the NO OVLO variant — wrong for this design. Never change 04 to 07. |
| IC005 | PM | U3, U4 | LMQ61460AFSQRJRRQ1 — 5 V Synchronous Buck Converter (VQFN-HR RJR 14-pin 4×3.5mm) | LMQ61460AFSQRJRRQ1 | TBD | TBD | TBD | RECHECK | Dual buck converters for 5V_MAIN rail. |
| IC006 | PM | U1 | LTC3350EUHF#PBF — Supercapacitor Manager (QFN-38) | LTC3350EUHF#PBF | TBD | TBD | TBD | RECHECK | Manages 2S4P 50F supercap bank with ≥33.5s hold-up. |
| IC007 | PM | U6 | TPS25751DREFR — USB PD 3.1 DRP Controller (WQFN-38) | TPS25751DREFR | TBD | TBD | TBD | RECHECK | USB-C PD negotiation controller. |
| IC008 | PM | U14 | STUSB4500LQTR — USB-C Sink Controller (QFN-24) | STUSB4500LQTR | TBD | TBD | TBD | RECHECK | USB-C sink-only controller. |
| IC009 | PM | U8, U10, U13 | LM74700QDBVRQ1 — Ideal-Diode OR-ing Controller (SOT-23-6) | LM74700QDBVRQ1 | TBD | TBD | TBD | RECHECK | OR-ing controllers for redundant power paths. |
| IC010 | PM | U8 | MCP121T-450E/LB — 4.5 V Voltage Supervisor (SC70-3) | MCP121T-450E/LB | TBD | TBD | TBD | RECHECK | Voltage supervisor for 5V_MAIN rail. |
| IC011 | CTL | U9 | TPS2372-4 — PoE PD Interface Type 4 (VQFN-20) | TPS2372-4 | TBD | TBD | TBD | RECHECK | Controller-owned PoE 802.3bt Type 4 PD controller. |
| IC012 | CTL | U10 | TPS23730RMTR — PoE ACF DC-DC Controller (WQFN-20) | TPS23730RMTR | TBD | TBD | TBD | RECHECK | Controller-owned PoE active-clamp-forward DC-DC controller. |
| IC013 | PM | U11, U15 | MIC1555YM5-TR — CMOS Timer / LED Oscillator (SOT-23-5) | MIC1555YM5-TR | TBD | TBD | TBD | RECHECK | Timer ICs for LED oscillator and monostable circuits. |
| IC014 | CTL | U_USB | TPS2065C — USB Power Distribution Switch (SOT-23-5) | TPS2065C | TBD | TBD | TBD | RECHECK | USB port current limiter. |
| IC015 | CTL | U_HDMI | AP2331W — HDMI Current Limiter (SOT-23-5) | AP2331W | TBD | TBD | TBD | RECHECK | HDMI port current limiter. Package is SOT-23-5 (not SOT-23 3-pin or SOT-25). |
| IC016 | PM | U18, U19 | SN74LVC1G14DBVRQ1 — Single Schmitt Inverter (SOT-23-5) | SN74LVC1G14DBVRQ1 | TBD | TBD | TBD | RECHECK | Schmitt trigger inverters. Always use full MPN with DBVRQ1 suffix. |

---

## IC: INTERFACE & BRIDGE (4 items)

| # | Board | Ref | Specification to Verify | Candidate MPN | Candidate DigiKey | Candidate Mouser | Candidate JLCPCB | Verification | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IC017 | PM, STA | U2 (PM), U5 (STA) | INA219AIDR — Zero-Drift Power Monitor (SOIC-8) | INA219AIDR | TBD | TBD | TBD | RECHECK | Current sense monitors. System total: 2 (PM + STA). |
| IC018 | STA, SBD | MCP23017T-E/SO (all) | MCP23017T-E/SO — I²C GPIO Expander 16-bit (SOIC-28) | MCP23017T-E/SO | MCP23017T-E/SOCT-ND | 579-MCP23017T-E/SO | C47023 | VERIFIED | Current active map: Stator `U_EXP1` @ 0x20, `U_EXP2` @ 0x21, `U_EXP4` @ 0x22; Settings Board `U_EXP_SW_IN` @ 0x23, `U_LED_B1` @ 0x24, `U_LED_B2` @ 0x25. System total: 6 units. `U_EXP_SW_OUT`, `U_EXP_LED @ 0x27`, any PM-side MCP23017, and any `0x40/0x41` MCP23017 address claims are stale artefacts — never use. Local datasheet present at `design/Datasheets/MCP23017-Datasheet.pdf`. |
| IC019 | STA | U_PWM | PCA9685BS/3 — I²C 16-ch PWM Driver (SSOP-28) | PCA9685BS/3 | TBD | TBD | TBD | VERIFIED | PWM driver @ 0x60 (A5=HIGH, A4–A0=GND). Local datasheet present at `design/Datasheets/PCA9685-datasheet.pdf`. |
| IC020 | PM | U16 | PCA9534APWR — 8-bit I²C GPIO expander (TSSOP-16) @ 0x3F | PCA9534APWR | 296-21760-1-ND | 595-PCA9534APWR | C2871127 | VERIFIED | PM-local expander for `POE_STAT`, `SYS_FAULT`, `BATT_PRES_N`, `USB_STAT`, `SW_LED_R/G/B`, and `SW_LED_CTRL`. No spare GPIOs by design. |

---

## IC: SENSORS (3 items)

| # | Board | Ref | Specification to Verify | Candidate MPN | Candidate DigiKey | Candidate Mouser | Candidate JLCPCB | Verification | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IC020 | ROT | U2 Track A | FDC2114RGHR — 4-ch Capacitive Sensor IC (16-VQFN) | FDC2114RGHR | TBD | TBD | TBD | RECHECK | Board A, addr 0x2A. bits[5:3] N=64; bits[3:0] N=26. System total: 30 units. |
| IC021 | ROT | U3 Track B | FDC2114RGHR — 4-ch Capacitive Sensor IC (16-VQFN) | FDC2114RGHR | TBD | TBD | TBD | RECHECK | Board B, addr 0x2B. bits[2:0] N=64 only; NOT POPULATED for N=26. System total: 30 units. |
| IC022 | ROT | U4 STGC | FDC2114RGHR — 4-ch Capacitive Sensor IC (16-VQFN) | FDC2114RGHR | TBD | TBD | TBD | RECHECK | Board A, addr 0x2B. bit[4] N=26 only; NOT POPULATED for N=64. System total: TBD (N=26 builds only). |

---

## IC: LOGIC BUFFERS & DRIVERS (2 items)

| # | Board | Ref | Specification to Verify | Candidate MPN | Candidate DigiKey | Candidate Mouser | Candidate JLCPCB | Verification | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IC023 | EXT, JDB | U1 | SN74LVC2G125DCUR — Dual 3-State Buffer (VSSOP-8) | SN74LVC2G125DCUR | TBD | TBD | TBD | RECHECK | Re-buffers TCK/TMS every 5-rotor group. System total: 2 units (EXT + JDB). Package is VSSOP-8 (not SOT-23-6). C15281/C2688 are stale/wrong. |
| IC024 | JDB | U1 | FT232H — USB 2.0 to MPSSE Bridge (QFN-56) | FT232H | TBD | TBD | TBD | RECHECK | JTAG debug board USB-to-JTAG bridge. |

---

## IC: COMPUTE MODULE (1 item)

| # | Board | Ref | Specification to Verify | Candidate MPN | Candidate DigiKey | Candidate Mouser | Candidate JLCPCB | Verification | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IC025 | CTL | CM5 | Raspberry Pi Compute Module 5 | CM5 | TBD | TBD | Global sourcing | RECHECK | Main system compute module. |

---

## TRANSISTORS & DIODES (5 items)

| # | Board | Ref | Specification to Verify | Candidate MPN | Candidate DigiKey | Candidate Mouser | Candidate JLCPCB | Verification | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T001 | PM, SBD | Q_BNK1_R/G/B, Q_BNK2_R/G/B (SBD), Q4/Q5 (PM) | N-channel MOSFET; SOT-23; V_DS >= 30V; logic-level gate suitable for 3.3V drive | BSS138 | BSS138CT-ND | 512-BSS138 | C255592 | RECHECK | Active Settings Board implementation uses 6× BSS138s (`Q_BNK1_R/G/B`, `Q_BNK2_R/G/B`) for shared full-RGB low-side colour rails under CM5 control. System total: 8 units (6 SBD + 2 PM). Candidate MPN needs full re-verification. |
| T002 | PM | Q8, Q10, Q13 | CSD17483F4T — 30 V 10 A N-ch OR-ing MOSFET (SON-8) | CSD17483F4T | TBD | TBD | TBD | RECHECK | OR-ing MOSFETs for redundant power paths. |
| D001 | PM, CTL | D1, D2 (PM), D_USB (CTL) | BAT54 (Diotec) — Schottky Diode (SOD-323 / SOT-23) | BAT54 | TBD | TBD | TBD | RECHECK | Schottky diodes. System total: 3 units. |
| T003 | SBD | R_GATE1–R_GATE6 | 1 kΩ; 1% thick-film; 0402 | ERJ-2RKF1001X | P1.00KLBCT-ND | 667-ERJ-2RKF1001X | C25705 | RECHECK | Qty = 6. Gate resistors for the Settings Board full-RGB BSS138 low-side colour-rail MOSFETs (`Q_BNK1_R/G/B`, `Q_BNK2_R/G/B`). Same entry as R027. Candidate MPN needs full re-verification. |
| T004 | PM | BT_SW1_1-6 blade tabs | (see S008 above) | (see S008 above) | (see S008 above) | (see S008 above) | (see S008 above) | (see S008 above) | (see S008 above) |

---

## ESD PROTECTION (3 items)

| # | Board | Ref | Specification to Verify | Candidate MPN | Candidate DigiKey | Candidate Mouser | Candidate JLCPCB | Verification | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ESD001 | PM, CTL | D3 (PM), U4-U6 (CTL) | TPD4E05U06QDQARQ1 — 4-Channel ESD Array (U-DFN-10) | TPD4E05U06QDQARQ1 | TBD | TBD | TBD | RECHECK | One PM-side array remains on USB-C. The Controller owns three arrays for USB/HDMI plus Ethernet / PoE entry protection. System total: 4 units. |
| ESD002 | PM | U_ESD_PD | TPD1E10B06DYARQ1 — Single-Channel ESD (SOD-523) | TPD1E10B06DYARQ1 | TBD | TBD | TBD | RECHECK | USB PD ESD protection. |
| ESD003 | PM | U_ESD_SMB | TPD2E2U06DRLR — Dual-Channel SMBus ESD (SOT-553) | TPD2E2U06DRLR | TBD | TBD | TBD | RECHECK | SMBus ESD protection. |

---

## CAPACITORS (15 items)

| # | Board | Ref | Specification to Verify | Candidate MPN | Candidate DigiKey | Candidate Mouser | Candidate JLCPCB | Verification | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C001 | All | Bulk 0.1µF | 0.1 µF X7R 0402 decoupling cap | TBD | TBD | TBD | TBD | RECHECK | System total: 513 units. Standard bypass cap. |
| C002 | All | Bulk 10µF | 10 µF X7R 50 V 1206 bulk decoupling | CL31B106KBHNNNE | TBD | TBD | TBD | RECHECK | System total: 185 units. |
| C003 | PM | C1-C15 | 22 µF X7R 25 V 1210 bulk cap | CL32B226KAJNNNE | TBD | TBD | TBD | RECHECK | System total: 15 units (PM only). |
| C004 | JDB | C_USB | 4.7 µF X7R 0402 entry filter | TBD | TBD | TBD | C19666 | RECHECK | JDB 5V_USB entry filter. |
| C005 | PM | C_timing | 10 µF 16 V X7R 0603 monostable timing cap | CL10B106KA8NNNC | TBD | TBD | TBD | RECHECK | MIC1555 monostable timing cap. |
| C006 | PM | C_1µF (x3) | 1 µF X7R 50 V 0805 | C0805C105K5RACTU | TBD | TBD | TBD | RECHECK | PM circuit caps. |
| C007 | PM | C_LDO | 10 µF 25 V X7R 1206 LDO input cap | C1206C106K3RACTU | TBD | TBD | TBD | RECHECK | LDO input capacitor. |
| C008 | PM | C_SS | 10 nF X7R 50 V 0402 soft-start cap | CL05B103KB5NNNC | TBD | TBD | TBD | RECHECK | Soft-start timing cap. |
| C009 | PM | C_TERM | 10 nF 100 V X7R 0402 Bob Smith termination cap | TBD | TBD | TBD | TBD | RECHECK | Bob Smith network termination. |
| C010 | PM | C_SYNC1 | 100 pF X7R 25 V 0402 SYNC SW-ringing LP filter | C0402C101K3RACAUTO | TBD | TBD | TBD | RECHECK | SYNC switching noise filter. |
| C011 | PM | C_SYNC2 | 22 nF X7R 25 V 0603 SYNC phase-delay cap | CL10B223KB8WPNC | TBD | TBD | TBD | RECHECK | SYNC phase-delay network. |
| C012 | PM | C_SC1-8 (x8) | 25 F / 2.7 V Supercapacitor | ADCR-T02R7SA256MB | 535-ADCR-T02R7SA256MB-ND | 815-ADCRT02R7SA256MB | Global sourcing only | RECHECK | Current design target is 2S4P with 8 cells total. Order 12 (8 required + 4 spare). |
| C013 | PM | C35 (x2) | 22 µF 25 V X7R 1210 5V_MAIN backup bulk cap | CL32B226KAJNNNE | TBD | TBD | TBD | RECHECK | Two in parallel for C35 per DEC-030. |
| C014 | SBD | C_debounce (x9) | 100nF; X7R; 0402; V_rated >= 10V | CL05B104KB5NNNC | 1276-1009-1-ND | 187-CL05B104KB5NNNC | C1525 | RECHECK | Switch debounce capacitors: SW_CFG_APPLY x1 plus SW_B1/B2 x8. |
| C015 | CTL | C_PoE | (PoE-specific caps) | TBD | TBD | TBD | TBD | RECHECK | Controller PoE circuitry capacitors. |

---

## RESISTORS (39 items)

| # | Board | Ref | Specification to Verify | Candidate MPN | Candidate DigiKey | Candidate Mouser | Candidate JLCPCB | Verification | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R001 | Multiple | R_10k_0603 | 10 kΩ 1% 0603 pull resistor | ERJ-3EKF1002V | TBD | 667-ERJ-3EKF1002V | C25804 | RECHECK | System total: 31 units (PM, CTL, STA, SBD). Same MPN as SBD R_SW row. |
| R002 | Multiple | R_10k_0402 | 10 kΩ 1% 0402 pull resistor | ERJ-2RKF1002X | TBD | 667-ERJ-2RKF1002X | C25744 | RECHECK | System total: 329 units (PM, STA, ENC, ROT, JDB). |
| R003 | STA | R7-R15 (75Ω 0603) | 75 Ω 1% 0603 series resistor | ERJ-3EKF75R0V | TBD | TBD | C105905 | RECHECK | Stator ribbon cable series resistors. System total: 9 units. |
| R004 | PM, ENC, ROT | R_75_0402 | 75 Ω 1% 0402 series resistor | ERJ-2RKF75R0X | TBD | 667-ERJ-2RKF75R0X | TBD | RECHECK | JTAG and ribbon cable impedance termination. System total: 37 units. |
| R005 | JDB | R_33_0402 | 33 Ω 1% 0402 series resistor | ERJ-2RKF33R0X | TBD | TBD | C25808 | RECHECK | JDB series resistors. System total: 7 units. |
| R006 | REF | R1 (TDO damping) | 22 Ω 1% 0603 JTAG end-of-chain damping | ERJ-3EKF2200V | TBD | 667-ERJ-3EKF2200V | TBD | RECHECK | End-of-chain TDO damping resistor. Package is 0603 (NOT 0402). |
| R007 | ENC | R_LED (x2) | 330 Ω 1% 0402 LED current-limit resistor | ERJ-2RKF3300X | TBD | TBD | C105872 | RECHECK | Encoder status LED resistors. System total: 6 units. |
| R008 | PM | N/A | REMOVED — RGB ring resistors are integrated into S004 (Adafruit 4660) | N/A | N/A | N/A | N/A | N/A | REMOVED: The Adafruit 4660 switch includes integrated current-limiting for its RGB ring LED. |
| R009 | PM | R_I2C (x2) | 4.7 kΩ 1% 0603 I²C pull-up | ERJ-3EKF4701V | TBD | 667-ERJ-3EKF4701V | TBD | RECHECK | I²C pull-ups on Power Module. |
| R010 | CTL | R_DIFF | 100 Ω 1% 0603 differential termination | ERJ-3EKF1000V | TBD | TBD | C25806 | RECHECK | Differential pair termination. |
| R011 | PM, STA | R_RSENSE (x2) | 10 mΩ ±1% 5 A 2512 Kelvin shunt | WSK2512R0100FEA | 541-WSK2512R0100FEACT-ND | 71-WSK2512R0100FEA | C3985410 | VERIFIED | Local Vishay WSK2512 datasheet now present and the part matches the required 2512 / 4-terminal / 10 mΩ / ±1% shunt characteristics. User confirmed this as the accepted replacement candidate for the stale CSS2H placeholder. System total: 3 units; footprint finalization is deferred until PCB layout. Mouser product resources include KiCad footprint and 3D model links. |
| R012 | CTL | R13 | 121 kΩ 1% 0603 PoE MPS current set | ERJ-3EKF1213V | TBD | 667-ERJ-3EKF1213V | TBD | RECHECK | TPS2372-4 RMPS current-set resistor on the Controller PoE front-end. |
| R013 | CTL | R11 | 301 Ω 1% 0603 charge current set | ERJ-3EKF3010V | TBD | 667-ERJ-3EKF3010V | TBD | RECHECK | TPS2372-4 gate-drive resistor on the Controller PoE front-end. |
| R014 | PM | R28 | 274 kΩ 1% 0603 MIC1555 U15 monostable | ERJ-3EKF2743V | TBD | 667-ERJ-3EKF2743V | TBD | RECHECK | MIC1555 U15 monostable timing resistor; target hold time 3.01 s. |
| R015 | PM | R17 (MIC1555 R_B) | 715 kΩ 1% 0603 MIC1555 timer R_B | ERJ-3EKF7153V | TBD | 667-ERJ-3EKF7153V | TBD | RECHECK | 1 Hz LED oscillator timing resistor. |
| R016 | PM | R_UVLO_TOP | 232 kΩ 1% 0603 thick-film eFuse UVLO | ERJ-3EKF2323V | TBD | 667-ERJ-3EKF2323V | TBD | RECHECK | LMQ61460 UVLO upper divider. |
| R017 | PM | R_UVLO_BOT | 28.7 kΩ 1% 0603 thick-film eFuse UVLO | ERJ-3EKF2872V | TBD | 667-ERJ-3EKF2872V | TBD | RECHECK | LMQ61460 UVLO lower divider. |
| R018 | PM | R3 (R_ILIM) | 210 Ω 0.1% 0603 thin-film eFuse ILIM | ERA-3ARB2100V | TBD | 667-ERA-3ARB2100V | TBD | RECHECK | eFuse current-limit accuracy is critical. DigiKey and JLCPCB PNs still need confirmation. ERA series -- NOT ERJ 1% thick-film. |
| R019 | PM | R_FSET | 86.6 kΩ 1% 0603 thick-film SYNC FSET resistor | ERJ-3EKF8662V | TBD | 667-ERJ-3EKF8662V | TBD | RECHECK | LMQ61460 switching frequency set resistor. |
| R020 | PM | R_DLY | 82.0 kΩ 1% 0402 thick-film SYNC phase-delay | ERJ-2RKF8202X | TBD | 667-ERJ-2RKF8202X | TBD | RECHECK | LMQ61460 soft-start delay resistor. |
| R021 | PM | R14 (R_TOP BACKUP) | 30.1 kΩ 0.1% 0603 thin-film supercap BACKUP | ERA-3ARB3012V | 10-ERA-3ARB3012VCT-ND | 667-ERA-3ARB3012V | C1728516 | RECHECK | LTC3350 BACKUP upper divider. Sets trigger at 4.812V per DEC-030. |
| R022 | PM | R15 (R_BOT BACKUP) | 10.0 kΩ 0.1% 0603 thin-film supercap BACKUP | ERA-3ARB103V | P10KBDCT-ND | 667-ERA-3ARB103V | C465746 | RECHECK | LTC3350 BACKUP lower divider. ERA-3ARB1002V does not exist. |
| R023 | PM | R30 (RT freq-set) | 33.2 kΩ 1% 0402 thick-film LTC3350 RT | ERA-2AEB3322X | P33.2KDCCT-ND | 667-ERA-2AEB3322X | C2087909 | RECHECK | LTC3350 RT sets 400 kHz switching per DEC-030. |
| R024 | PM | R16, R22, R29 | 10 kΩ 1% 0603 MIC1555/pull-up | ERJ-3EKF1002V | TBD | 667-ERJ-3EKF1002V | C25804 | RECHECK | MIC1555 R_A + EN pull-up + /INTB pull-up. Same candidate MPN as SBD R_SW row. |
| R025 | STA | R_SH1 (SERVO_HOME) | 10 kΩ 1% 0402 SERVO_HOME pull-up | ERJ-2RKF1002X | TBD | 667-ERJ-2RKF1002X | TBD | RECHECK | R_SH2/C_SH2 are erroneous duplicates — permanently removed; only R_SH1/C_SH1 exist. |
| R026 | SBD | R_SW pull-downs (x11) | 10 kΩ 1% 0603 switch pull-downs | ERJ-3EKF1002V | TBD | 667-ERJ-3EKF1002V | C25804 | RECHECK | Settings Board R16-R26 switch pull-downs. Same candidate MPN as PM row 14. |
| R027 | SBD | R_GATE1–R_GATE6 | 1kΩ 1% 0402; MOSFET gate resistors for 6× BSS138 low-side switches (Q_BNK1_R/G/B, Q_BNK2_R/G/B) | ERJ-2RKF1001X | P1.00KLBCT-ND | 667-ERJ-2RKF1001X | C25705 | RECHECK | 5V RGB upgrade (2026-04-17): Qty increased from 4 to 6 (added Q_BNK1_B, Q_BNK2_B for blue channels). Candidate MPN: Panasonic ERJ-2 thick-film 1% 0.1W 0402. System total: 6 units. Needs full re-verification. |
| R028 | SBD | R_LED_R1–R_LED_R12 | 150Ω 1% 0603; red channel current-limit resistor for Settings Board RGB LEDs @ 5V operation, 20mA nominal (Vf_red ≈ 2.0V) | ERJ-3EKF1500V | P150BYCT-ND | 667-ERJ-3EKF1500V | C22808 | RECHECK | 5V RGB upgrade (2026-04-17): Red LEDs operate at (5.0V - 2.0V) / 0.020A = 150Ω. Candidate MPN: Panasonic ERJ-3 thick-film 1% 0.1W 0603. System total: 12 units. Needs full re-verification. |
| R029 | SBD | R_LED_G1–R_LED_G12 | 100Ω 1% 0603; green channel current-limit resistor for Settings Board RGB LEDs @ 5V operation, 20mA nominal (Vf_green ≈ 3.0V) | ERJ-3EKF1000V | P100BYCT-ND | 667-ERJ-3EKF1000V | C22775 | RECHECK | 5V RGB upgrade (2026-04-17): Green LEDs operate at (5.0V - 3.0V) / 0.020A = 100Ω. Candidate MPN: Panasonic ERJ-3 thick-film 1% 0.1W 0603. System total: 12 units. Needs full re-verification. |
| R030 | PM | N/A | REMOVED — Ethernet activity LEDs are integrated into S004 (Adafruit 4660) RGB ring | N/A | N/A | N/A | N/A | N/A | REMOVED: Power Module does not have separate Ethernet activity LEDs. The Adafruit 4660 latching switch includes an integrated RGB ring LED that serves as the unified status indicator. |
| R031 | ENC | LED resistors (x2 per board) | (see R007 above) | (see R007 above) | (see R007 above) | (see R007 above) | (see R007 above) | (see R007 above) | (see R007 above) |
| R032 | Multiple | 75Ω JTAG | (see R004 above) | (see R004 above) | (see R004 above) | (see R004 above) | (see R004 above) | (see R004 above) | (see R004 above) |
| R033 | PM | I2C/SPI 4.7k | (see R009 above) | (see R009 above) | (see R009 above) | (see R009 above) | (see R009 above) | (see R009 above) | (see R009 above) |
| R034 | CTL | Various PoE | (TBD: organize PoE-specific resistors) | TBD | TBD | TBD | TBD | RECHECK | Additional Controller PoE circuit resistors. |
| R035 | PM | Various USB-C | (TBD: organize USB-C-specific resistors) | TBD | TBD | TBD | TBD | RECHECK | USB-C configuration resistors. |
| R036 | PM | Various LTC3350 | (TBD: organize remaining LTC3350 resistors) | TBD | TBD | TBD | TBD | RECHECK | Additional LTC3350 circuit resistors not already covered. |
| R037 | PM | Various eFuse | (TBD: organize remaining eFuse resistors) | TBD | TBD | TBD | TBD | RECHECK | Additional eFuse circuit resistors not already covered. |
| R038 | All | Various bypass | (TBD: organize remaining general-purpose resistors) | TBD | TBD | TBD | TBD | RECHECK | Remaining general-purpose circuit resistors. |
| R051 | SBD | R_LED_B1–R_LED_B12 | 100Ω 1% 0603; blue channel current-limit resistor for Settings Board RGB LEDs @ 5V operation, 20mA nominal (Vf_blue ≈ 3.0V) | ERJ-3EKF1000V | P100BYCT-ND | 667-ERJ-3EKF1000V | C22775 | RECHECK | 5V RGB upgrade (2026-04-17): Blue channel upgraded from 0Ω debug links to full 100Ω current-limiting resistors for production RGB operation. Same value as green (Vf similar). Candidate MPN: Panasonic ERJ-3 thick-film 1% 0.1W 0603. System total: 12 units. Needs full re-verification. |

---

## INDUCTORS & MAGNETICS (3 items)

| # | Board | Ref | Specification to Verify | Candidate MPN | Candidate DigiKey | Candidate Mouser | Candidate JLCPCB | Verification | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IND001 | PM | FB1-FB4 | Ferrite bead 120 Ω @100 MHz 4.0 A 1206 | HI1206P121R-10 | TBD | TBD | TBD | RECHECK | Laird ferrite beads. System total: 4 units. |
| IND002 | CTL | T2 | PoE ACF Isolation Transformer | POE600F-12LD | TBD | TBD | TBD | RECHECK | Controller-owned Coilcraft PoE isolation transformer. |
| IND003 | PM | L_DM1, L_DM2 | EMI Common-Mode Choke | WE-CMBNC 7448031002 | TBD | TBD | TBD | RECHECK | Würth EMI choke. System total: 2 units. |

---

## POWER INDUCTORS (1 item)

| # | Board | Ref | Specification to Verify | Candidate MPN | Candidate DigiKey | Candidate Mouser | Candidate JLCPCB | Verification | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PWR001 | PM | L_SYNC | DM Filter Inductor 10 µH 15.5 A | SRP1265A-100M | TBD | TBD | TBD | RECHECK | Bourns power inductor for SYNC buck. |

---

## CONNECTORS: BOARD-TO-BOARD (8 items)

| # | Board | Ref | Specification to Verify | Candidate MPN | Candidate DigiKey | Candidate Mouser | Candidate JLCPCB | Verification | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| J001 | PM | J1A/J1B/J1C (PM side) | 10-position; 2.5mm pitch; board-to-board plug; 6A/contact | 1123684-7 | A114780-ND | 571-1123684-7 | C3683043 | VERIFIED | PM-side plug for all three Controller↔PM dock connectors (`J1A` main rails, `J1B` PoE auxiliary, `J1C` low-speed control). |
| J002 | CTL | J1A/J1B/J1C (Controller side) | 10-position; 2.5mm pitch; board-to-board receptacle; 6A/contact | 1-1674231-1 | A119250-ND | 571-1-1674231-1 | C3683260 | VERIFIED | Controller-side receptacle for the three-way PM dock. |
| J003 | STA | J8A/J8B (Stator side) | Hybrid blind-mate plug; 5 power blades + 15 signal contacts | 2195620015 | 900-2195620015-ND | 538-219562-0015 | Global sourcing / consignment | VERIFIED | Stator-side plug for both hybrid Controller↔Stator docks. Prefer DigiKey metadata; Mouser details for this part family may be less reliable. |
| J004 | CTL | J2A/J2B (Controller side) | Hybrid blind-mate receptacle; 5 power blades + 15 signal contacts | 2195630015 | 900-2195630015-ND | 538-219563-0015 | Global sourcing / consignment | VERIFIED | Controller-side receptacle for both hybrid Stator docks. |
| J005 | ROT, REF | J1/J2 (10-pin male) | 10-pin; 2x5; 0.8mm pitch; Samtec ERM8 male header | ERM8-005-05.0-S-DV-K-TR | 612-ERM8-005-05.0-S-DV-K-TRCT-ND | 200-ERM8005050SDVKTR | C3649741 | RECHECK | Used for Rotor J1/J2 and Reflector J1/J2. System total: 64 units. |
| J006 | STA, EXT, ROT | J1/J2/J4/J5 (10-pin female) | 10-pin; 2x5; 0.8mm pitch; Samtec ERF8 female socket | ERF8-005-05.0-S-DV-K-TR | SAM13517CT-ND | 200-ERF8005050SDVKTR | C7273978 | RECHECK | Used across Stator rotor-slot sockets, Extension outputs, and Rotor Board B outputs. System total: 64 units. |
| J007 | ROT, REF | J3 (20-pin male) | 20-pin; 2x10; 0.8mm pitch; Samtec ERM8 male header | ERM8-010-05.0-S-DV-K-TR | SAM8610CT-ND | 200-ERM8010050SDVKTR | C374877 | RECHECK | Used for Rotor J3 and Reflector J3. System total: 32 units. |
| J008 | STA, EXT, ROT | J3/J6 (20-pin female) | 20-pin; 2x10; 0.8mm pitch; Samtec ERF8 female socket | ERF8-010-05.0-S-DV-K-TR | SAM8618CT-ND | 200-ERF8010050SDVKTR | C3646170 | RECHECK | Used across Stator rotor-slot sockets, Extension outputs, and Rotor Board B outputs. System total: 32 units. |

---

## CONNECTORS: PIN HEADERS & SOCKETS (8 items)

| # | Board | Ref | Specification to Verify | Candidate MPN | Candidate DigiKey | Candidate Mouser | Candidate JLCPCB | Verification | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| J009 | ROT | H_SW3 (Board A male) | 1x7; 2.54mm pitch; vertical THT male pin header | PH1-07-UA | 2057-PH1-07-UA-ND | 737-PH1-07-UA | C3331618 | RECHECK | Rotor Design_Spec explicitly uses PH1-07-UA on Board A and RS1-07-G on Board B for physical keying. System total: 30 units. |
| J010 | ROT | H_SW3 (Board B female) | 1x7; 2.54mm pitch; vertical THT female socket | RS1-07-G | 2057-RS1-07-G-ND | 737-RS1-07-G | C3321543 | RECHECK | Companion part. Verify socket height and mating fit against rotor inter-board gap. System total: 30 units. |
| J011 | ROT, JDB | H_PWR / H_SENS / JDB J1 male | 1x5; 2.54mm pitch; vertical THT male pin header | PH1-05-UA | 2057-PH1-05-UA-ND | 737-PH1-05-UA | C5374051 | RECHECK | Shared across Rotor Board B H_PWR/H_JTAG, Rotor Board A H_SENS, and JDB J1. System total: 91 units. |
| J012 | ROT, CTL | H_PWR / H_JTAG / H_SENS / J_JDB_PWR female | 1x5; 2.54mm pitch; vertical THT female socket | RS1-05-G | 2057-RS1-05-G-ND | 737-RS1-05-G | C3321119 | RECHECK | Shared across Rotor Board A H_PWR/H_JTAG, Rotor Board B H_SENS, and Controller J_JDB_PWR. System total: 91 units. |
| J013 | JDB | J2 male | 1x10; 2.54mm pitch; vertical THT male pin header | PH1-10-UA | 2057-PH1-10-UA-ND | 737-PH1-10-UA | C3330527 | RECHECK | JDB Design_Spec defines this as the hat JTAG output header. |
| J014 | CTL | J_JDB_JTAG female | 1x10; 2.54mm pitch; vertical THT female socket | RS1-10-G | 2057-RS1-10-G-ND | 737-RS1-10-G | C3320525 | RECHECK | Controller Design_Spec defines this as the female mate to the JDB JTAG OUTPUT header. |
| J015 | ENC, STA | J2 (Encoder) / J4-J6 (Stator) | 26-pin; 2x13; 2.54mm pitch; vertical shrouded box header with polarisation key | T821126A1S100CEU | TBD | TBD | C3013501 | VERIFIED | IDC ribbon-cable interface. Existing docs call out RS-Online 832-3503. System total: 6 units. Local datasheet present at `design/Datasheets/T821126A1S100CEU-C3013501-datasheet.pdf`. |
| J016 | STA, EXT, REF | J7 / J7 IN / J8 OUT / J4 | 16-pin; 2x8; 2.54mm pitch; vertical shrouded box header | BHR-16-VUA | 2057-BHR-16-VUA-ND | 737-BHR-16-VUA | C17692295 | VERIFIED | Used on Stator J7, Extension J7/J8, and Reflector J4. System total: 4 units. Local datasheet now present at `design/Datasheets/bhr-xx-vua-data-sheet.pdf`; user confirmed supplier part numbers. |

---

## CONNECTORS: EXTERNAL I/O (7 items)

| # | Board | Ref | Specification to Verify | Candidate MPN | Candidate DigiKey | Candidate Mouser | Candidate JLCPCB | Verification | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| J017 | CTL | J3 | Dual-stacked USB 3.0 Type-A receptacle; right-edge external I/O; 5.0mm overhang | 48406-0003 | WM10420-ND | 538-48406-0003 | C565298 | RECHECK | Controller right-edge external I/O. |
| J018 | CTL | J4 | Full-size HDMI Type-A receptacle; right-edge external I/O; 5.0mm overhang | 2007435-1 | A141617-ND | 571-2007435-1 | C195051 | RECHECK | Controller right-edge external I/O. |
| J019 | PM | J4 | USB Type-C power input only; 6-position right-angle SMT receptacle | USB4135-GF-A | 2073-USB4135-GF-ACT-ND | 640-USB4135-GF-A | C5438410 | RECHECK | Power-only USB-C on Power Module. Mechanical wall-flush fit is explicitly called out. |
| J020 | CTL | J5 | RJ45 MagJack for PoE 802.3bt Type 4 input; long-body THT; integrated magnetics | 7499111121A | 1297-1070-5-ND | 710-7499111121A | C5523983 | RECHECK | Controller now owns the PoE / Ethernet entry point. |
| J021 | PM | J3 | 5-circuit; 1-row; 3.0mm pitch; vertical THT Molex Micro-Fit 3.0; battery connector | 43650-0519 | WM14587-ND | 538-43650-0519 | C563849 | RECHECK | Existing design notes explicitly say battery suitability still needs confirmation. |
| J022 | STA, SBD | J_CFG (STA), J_I2C (SBD) | 6-pin; 2.0mm pitch JST PH; THT vertical; keyed; >= 1A per contact | B6B-PH-K-S(LF)(SN) | 455-1708-ND | 306-B6B-PH-K-SLFSN | C131342 | VERIFIED | Active Settings/Stator link is now the 6-pin JST PH variant carrying `3V3_ENIG`, `5V_MAIN`, `GND`, `SDA`, `SCL`, `GND`. Local family datasheet now present at `design/Datasheets/JST-PH-Connector.datasheet.pdf`. |
| J023 | STA | J_SERVO | 3-pin; 2.0mm pitch JST PH; THT vertical; keyed | B3B-PH-K-S(LF)(SN) | 455-1705-ND | 306-B3BPHKSLFSNP | C131339 | VERIFIED | JST PH family connector for the servo lead. Keep aligned with the same PH-family datasheet package that also covers `B6B-PH`. |

---

## CONNECTORS: DISPLAY & FAN (2 items)

| # | Board | Ref | Specification to Verify | Candidate MPN | Candidate DigiKey | Candidate Mouser | Candidate JLCPCB | Verification | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| J024 | CTL | J_DSI1 | 15-pin; 1.0mm pitch ZIF/FPC; 4-lane MIPI DSI; 100 ohm differential | F52Q-1A7H1-11015 | 609-F52Q-1A7H1-11015CT-ND | 649-F52Q-1A7H1-11015 | C3169095 | VERIFIED | Datasheet reviewed: Amphenol F52Q/F52R family is 1.00mm pitch, right-angle ZIF FFC/FPC, top-contact, SMT, 0.5A / 50V. Contact-side concern is acceptable because either Type-A or Type-B FPC can be used. |
| J025 | CTL | J_FAN | 4-pin; 1.0mm pitch JST SH; SMT; keyed | SM04B-SRSS-TB(LF)(SN) | 455-SM04B-SRSS-TBCT-ND | 306-SM04BSRSSTBLFSN | C160404 | VERIFIED | Datasheet reviewed: JST SH family matches the 1.0mm pitch SMT keyed header requirement. |

---

## CONNECTORS: PLUGBOARD & ENCODER (2 items)

| # | Board | Ref | Specification to Verify | Candidate MPN | Candidate DigiKey | Candidate Mouser | Candidate JLCPCB | Verification | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| J026 | ENC | J1 (x64) | 6.35mm (1/4in) mono switched panel-mount jack; 3 terminals (Tip / Switch / Sleeve) | SaiBuy.Ltd eBay item 334364197440 | Global sourcing / consignment | Global sourcing / consignment | eBay item 334364197440 | VERIFIED | Already purchased. Pseudo datasheet captured at `design/Datasheets/SaiBuy_Ltd_6p35mm_Mono_Jack_Pseudo_Datasheet.md`. Treat as a consignment part installed during mechanical/final assembly rather than PCB assembly. System total: 192 units. |
| J027 | ENC | BT1-BT128 | 6.35mm (0.250in) straight vertical PCB-mount male blade tab | 1285-ST | 36-1285-ST-ND | 534-1285-ST | C5370868 | VERIFIED | Used as two rows of 64 blade terminals on Encoder boards. System total: 384 units. Covered by local `design/Datasheets/keystone-1211-datasheet.pdf`. Mouser product resources include KiCad footprint and 3D model links. |

---

## MISCELLANEOUS (5 items)

| # | Board | Ref | Specification to Verify | Candidate MPN | Candidate DigiKey | Candidate Mouser | Candidate JLCPCB | Verification | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M001 | JDB | Y1 | 12 MHz Crystal SMD | ABM8-12.000MHz-B2-T | 535-9826-1-ND | 815-ABM8-12-B2-T | C596894 | VERIFIED | Abracon crystal for the JTAG Daughterboard FT232H reference clock. Local datasheet present at `design/Datasheets/ABM8-Datasheet.pdf`. |
| M002 | PM | TC1 | 72°C SMD Thermal Cutoff | AC72ABD | TBD | TBD | TBD | RECHECK | Bourns thermal cutoff. |
| M003 | CTL | BT1 | CR2032 Coin Cell Holder | 3034TR | 36-3034CT-ND | 534-3034TR | C5213768 | VERIFIED | Keystone coin cell holder. `TR` is the tape-and-reel packaging suffix. Local datasheet present at `design/Datasheets/Keystone-CoinCellRetainers-datasheet.pdf`. |
| M004 | CTL | Standoffs (x4) | Würth 9774040151R M2.5 × 4.0mm SMT Brass Standoff (CM5 mount) | 9774040151R | 732-7089-1-ND | 710-9774040151R | C5182034 | VERIFIED | CM5 mounting standoffs. Local datasheet present at `design/Datasheets/9774040151R-standoff-datasheet.pdf`. Mouser product resources include a 3D model. |
| M005 | STA | C_SH1 | (SERVO_HOME cap) | TBD | TBD | TBD | TBD | RECHECK | SERVO_HOME RC network capacitor. R_SH2/C_SH2 are erroneous duplicates — permanently removed. |

---

## Summary by Verification Status

- **VERIFIED:** 18 items (S001 superseded, S002, S004, S009, L001, L002, IC018, IC019, R011, J015, J022, J023, J024, J025, J027, M001, M003, M004)
- **RECHECK:** 90 items (all others awaiting manual re-verification)
- **BLOCKED:** 0 items

---

## Component Categories

1. **SWITCHES & USER INPUT:** 8 items
2. **LEDS & INDICATORS:** 4 items
3. **IC: CPLD & PROGRAMMABLE LOGIC:** 2 items
4. **IC: POWER MANAGEMENT:** 14 items
5. **IC: INTERFACE & BRIDGE:** 3 items
6. **IC: SENSORS:** 3 items
7. **IC: LOGIC BUFFERS & DRIVERS:** 2 items
8. **IC: COMPUTE MODULE:** 1 item
9. **TRANSISTORS & DIODES:** 5 items
10. **ESD PROTECTION:** 3 items
11. **CAPACITORS:** 15 items
12. **RESISTORS:** 39 items (many cross-reference to other categories)
13. **INDUCTORS & MAGNETICS:** 3 items
14. **POWER INDUCTORS:** 1 item
15. **CONNECTORS: BOARD-TO-BOARD:** 8 items
16. **CONNECTORS: PIN HEADERS & SOCKETS:** 8 items
17. **CONNECTORS: EXTERNAL I/O:** 7 items
18. **CONNECTORS: DISPLAY & FAN:** 2 items
19. **CONNECTORS: PLUGBOARD & ENCODER:** 2 items
20. **MISCELLANEOUS:** 5 items

**Total unique component types:** 107
