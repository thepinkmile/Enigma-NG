# Enigma-NG -- Component Re-Verification Table

> Updated: 2026-04-16
> Canonical single-table workspace for manual component re-verification.
> Treat every populated candidate field as provisional until the row is explicitly marked `VERIFIED`.
> Do not propagate data from this file back into design docs until re-verification is complete.
> ERA datasheet: `design/Datasheets/Panasonic-ERA-datasheet.pdf`

| # | Board | Ref | Specification to Verify | Candidate MPN | Candidate DigiKey | Candidate Mouser | Candidate JLCPCB | Verification | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | PM + SBD | SW1, SW_B1_EN, SW_B1[0:3], SW_B2_EN, SW_B2[0:5] | Historical combined switch-selection row from the old unified-switch assumption | Superseded | Superseded | Superseded | Superseded | VERIFIED | Superseded by rows 54-56 after the design split into dedicated Settings Board toggles + discrete LEDs and a separate rugged Power Module switch. |
| 2 | SBD | SW_CFG_APPLY | SPST NO momentary; panel-mount; positive tactile click; V >= 3.3V; I >= 50mA | TBD | TBD | TBD | TBD | RECHECK | Must fit enclosure panel cutout. |
| 3 | CTL | J_DSI1 | 15-pin; 1.0mm pitch ZIF/FPC; 4-lane MIPI DSI; verify contact side vs CM5 DSI1 cable; 100 ohm differential | F52Q-1A7H1-11015 | 609-F52Q-1A7H1-11015CT-ND | 649-F52Q-1A7H1-11015 | C3169095 | VERIFIED | Datasheet reviewed: Amphenol F52Q/F52R family is 1.00mm pitch, right-angle ZIF FFC/FPC, top-contact, SMT, 0.5A / 50V. Contact-side concern is acceptable because either Type-A or Type-B FPC can be used; final display pin mapping still depends on the chosen 10in screen at schematic phase. |
| 4 | SBD | R_LED_R (x12), R_LED_G (x12) | 0603; <= 1% tolerance; separate red and green resistor networks per switch LED under nominal 3.3V operation; values tuned for final panel brightness | TBD | TBD | TBD | TBD | BLOCKED | Architecture changed: discrete common-anode RGB LEDs now need separate red and green resistor values per switch rather than one shared rail resistor. Blue debug links are tracked separately in row 58. |
| 5 | STA + SBD | J_CFG (STA), J_I2C (SBD) | 4-pin; 2.0mm pitch JST PH; THT vertical; keyed; >= 1A per contact; mates with PHR-4 | B4B-PH-K-S(LF)(SN) | 455-1706-ND | 306-B4BPHKSLFSNPP | C131334 | VERIFIED | Datasheet reviewed: JST PH series is 2.0mm pitch; through-hole top-entry version matches this connector family and the series is rated 2A / 100V, exceeding the >=1A/contact requirement. Replaces stale DigiKey right-angle reference, invalid Mouser reference, and missing JLCPCB code. |
| 6 | PM | C_SC1-8 (x8) | 25F; 2.7V; THT radial can; -40 to +85 degC; Abracon | ADCR-T02R7SA256MB | 535-ADCR-T02R7SA256MB-ND | 815-ADCRT02R7SA256MB | Global sourcing only | RECHECK | Current design target is 2S4P with 8 cells total. Order 12 (8 required + 4 spare). |
| 7 | PM | R3 (R_ILIM) | 210 ohm; 0.1% thin-film; 0603; ERA series -- NOT ERJ 1% thick-film | ERA-3ARB2100V | TBD | 667-ERA-3ARB2100V | TBD | RECHECK | eFuse current-limit accuracy is critical. DigiKey and JLCPCB PNs still need confirmation. |
| 8 | PM | R14 (R_TOP BACKUP divider) | 30.1 kohm; 0.1% thin-film; 0603; TCR <= 15 ppm/degC; P >= 0.1W | ERA-3ARB3012V | 10-ERA-3ARB3012VCT-ND | 667-ERA-3ARB3012V | C1728516 | RECHECK | LTC3350 BACKUP upper divider. Sets trigger at 4.812V per DEC-030. |
| 9 | PM | R15 (R_BOT BACKUP divider) | 10.0 kohm; 0.1% thin-film; 0603; TCR <= 15 ppm/degC; P >= 0.1W | ERA-3ARB103V | P10KBDCT-ND | 667-ERA-3ARB103V | C465746 | RECHECK | LTC3350 BACKUP lower divider. ERA-3ARB1002V does not exist. |
| 10 | PM | R30 (RT freq-set) | 33.2 kohm; 1% thick-film; 0402; P >= 0.063W | ERA-2AEB3322X | P33.2KDCCT-ND | 667-ERA-2AEB3322X | C2087909 | RECHECK | LTC3350 RT sets 400 kHz switching per DEC-030. |
| 11 | PM | R11 | 301 ohm; 1% thick-film; 0603 | ERJ-3EKF3010V | TBD | 667-ERJ-3EKF3010V | TBD | RECHECK | TPS2372-4 gate drive resistor. |
| 12 | PM, STA | R_RSENSE (x2) | 10 mohm; 1%; 2512; 4-terminal Kelvin shunt; 5A rated | CSS2H-2512R-R010ELF | TBD | 652-CSS2H-2512R-R010ELF | TBD | RECHECK | Shared part family across LTC3350 charge current sense and Stator current monitor. |
| 13 | PM | R13 | 121 kohm; 1% thick-film; 0603 | ERJ-3EKF1213V | TBD | 667-ERJ-3EKF1213V | TBD | RECHECK | TPS2372-4 RMPS current-set resistor. |
| 14 | PM | R16, R22, R29 | 10 kohm; 1% thick-film; 0603 | ERJ-3EKF1002V | TBD | 667-ERJ-3EKF1002V | C25804 | RECHECK | MIC1555 R_A + EN pull-up + /INTB pull-up. Same candidate MPN as SBD R_SW row. |
| 15 | PM | R17 (MIC1555 R_B) | 715 kohm; 1% thick-film; 0603 | ERJ-3EKF7153V | TBD | 667-ERJ-3EKF7153V | TBD | RECHECK | 1 Hz LED oscillator timing resistor. |
| 16 | PM | R28 | 274 kohm; 1% thick-film; 0603 | ERJ-3EKF2743V | TBD | 667-ERJ-3EKF2743V | TBD | RECHECK | MIC1555 U15 monostable timing resistor; target hold time 3.01 s. |
| 17 | PM | R_UVLO_TOP | 232 kohm; 1% thick-film; 0603 | ERJ-3EKF2323V | TBD | 667-ERJ-3EKF2323V | TBD | RECHECK | LMQ61460 UVLO upper divider. |
| 18 | PM | R_UVLO_BOT | 28.7 kohm; 1% thick-film; 0603 | ERJ-3EKF2872V | TBD | 667-ERJ-3EKF2872V | TBD | RECHECK | LMQ61460 UVLO lower divider. |
| 19 | PM | R_FSET | 86.6 kohm; 1% thick-film; 0603 | ERJ-3EKF8662V | TBD | 667-ERJ-3EKF8662V | TBD | RECHECK | LMQ61460 switching frequency set resistor. |
| 20 | PM | R_DLY | 82.0 kohm; 1% thick-film; 0402 | ERJ-2RKF8202X | TBD | 667-ERJ-2RKF8202X | TBD | RECHECK | LMQ61460 soft-start delay resistor. |
| 21 | PM | 4.7 kohm pull-ups | 4.7 kohm; 1% thick-film; 0603 | ERJ-3EKF4701V | TBD | 667-ERJ-3EKF4701V | TBD | RECHECK | Used for I2C and SPI pull-up positions. |
| 22 | STA | R_SH1 (SERVO_HOME pull-up) | 10 kohm; 1% thick-film; 0402 | ERJ-2RKF1002X | TBD | 667-ERJ-2RKF1002X | TBD | RECHECK | Candidate row currently appears self-consistent, but keep it in the same manual re-check pass as the rest. |
| 23 | STA | J_SERVO | 3-pin; 2.0mm pitch JST PH; THT vertical; keyed; mates with PHR-3 | B3B-PH-K-S(LF)(SN) | 455-1705-ND | 306-B3BPHKSLFSNP | C131339 | VERIFIED | Shares the JST PH datasheet family used to verify B4B-PH-K-S(LF)(SN); through-hole top-entry PH header matches the required 3-pin servo connector. Replaces stale DigiKey, Mouser, and JLCPCB references. |
| 24 | STA, ENC, ROT, REF | R_series 75 ohm | 75 ohm; 1% thick-film; 0402 | ERJ-2RKF75R0X | TBD | 667-ERJ-2RKF75R0X | TBD | RECHECK | Used for JTAG and ribbon cable impedance termination. |
| 25 | REF | R1 (TDO damping) | 22 ohm; 1% thick-film; 0603 (NOT 0402) | ERJ-3EKF2200V | TBD | 667-ERJ-3EKF2200V | TBD | RECHECK | End-of-chain TDO damping resistor. Package size is critical. |
| 26 | CTL | J_FAN | 4-pin; 1.0mm pitch JST SH; SMT; keyed | SM04B-SRSS-TB(LF)(SN) | 455-SM04B-SRSS-TBCT-ND | 306-SM04BSRSSTBLFSN | C160404 | VERIFIED | Datasheet reviewed: JST SH family matches the 1.0mm pitch SMT keyed header requirement. Existing Controller and Consolidated_BOM references already agree on this MPN and supplier/JLC codes. |
| 27 | SBD | R_SW pull-downs (x11, R16-R26) | 10 kohm; 1% thick-film; 0603 | ERJ-3EKF1002V | TBD | 667-ERJ-3EKF1002V | C25804 | RECHECK | Switch pull-downs. Same candidate MPN as PM row 14. |
| 28 | SBD | R_GATE (x4) | 1 kohm; 1% thick-film; 0402 | ERJ-2RKF1001X | P1.00KLBCT-ND | 667-ERJ-2RKF1001X | C25705 | VERIFIED | Corrected from the stale 10 kohm Mouser decode. Used as gate resistors for the Settings Board low-side colour-rail MOSFETs. |
| 29 | SBD | Q_BNK1_G, Q_BNK1_R, Q_BNK2_G, Q_BNK2_R | N-channel MOSFET; SOT-23; V_DS >= 30V; logic-level gate suitable for 3.3V drive | BSS138 | BSS138CT-ND | 512-BSS138 | C255592 | VERIFIED | Settings Board LED topology changed to low-side colour-rail sinks for the discrete common-anode LEDs. |
| 30 | SBD | C_debounce (x9) | 100nF; X7R; 0402; V_rated >= 10V | CL05B104KB5NNNC | 1276-1009-1-ND | 187-CL05B104KB5NNNC | C1525 | RECHECK | Switch debounce capacitors: SW_CFG_APPLY x1 plus SW_B1/B2 x8. |
| 31 | PM | J1 (Link-Alpha) | 80-pin; 2x40; 0.8mm pitch; Samtec ERM8 male header; 5.0mm stack height; mates with Controller J1 ERF8-040; carries 5V_MAIN / 3V3_ENIG / I2C / telemetry over Link-Alpha | ERM8-040-05.0-S-DV-K-TR | SAM8613CT-ND | 200-ERM8040050SDVKTR | C5358550 | RECHECK | Power Module uses the male side of the Link-Alpha BtB pair. Existing docs also note this part may need consigned or hand assembly despite a recorded JLC code. |
| 32 | CTL | J1 (Link-Alpha) | 80-pin; 2x40; 0.8mm pitch; Samtec ERF8 female socket; mates with Power Module J1 ERM8-040; receives Link-Alpha power / telemetry | ERF8-040-05.0-S-DV-K-TR | SAM8621CT-ND | 200-ERF8040050SDVKTR | C3640808 | RECHECK | Controller uses the female side of the Link-Alpha BtB pair. Verify stack height and supplier availability remain consistent with enclosure assumptions. |
| 33 | STA | J8 (Link-Beta) | 40-pin; 2x20; 0.8mm pitch; Samtec ERM8 male header; 5.0mm stack height; mates with Controller J2 ERF8-020; carries JTAG / ENC routing / TTD_RETURN over Link-Beta | ERM8-020-05.0-S-DV-K-TR | SAM8611CT-ND | 200-ERM8020050SDVKTR | C138400 | RECHECK | Stator uses the male side of the Link-Beta BtB pair. Verify exact DigiKey orderable suffix if packaging matters. |
| 34 | CTL | J2 (Link-Beta) | 40-pin; 2x20; 0.8mm pitch; Samtec ERF8 female socket; mates with Stator J8 ERM8-020; flush edge placement on Controller | ERF8-020-05.0-S-DV-K-TR | SAM8619CT-ND | 200-ERF8020050SDVKTR | C6034565 | RECHECK | Controller uses the female side of the Link-Beta BtB pair. Existing docs list alternate DigiKey packaging variants; CT is the current candidate. |
| 35 | ROT + REF | J1/J2 (Rotor input + Reflector input 10-pin) | 10-pin; 2x5; 0.8mm pitch; Samtec ERM8 male header; mates with ERF8-005 female sockets on Stator / Rotor / Extension outputs; JTAG or power path depending on reference | ERM8-005-05.0-S-DV-K-TR | 612-ERM8-005-05.0-S-DV-K-TRCT-ND | 200-ERM8005050SDVKTR | C3649741 | RECHECK | Used for Rotor J1/J2 and Reflector J1/J2. Confirm one MPN is valid across all 10-pin male ERM8 applications. |
| 36 | STA + EXT + ROT | J1/J2/J4/J5 (10-pin female outputs) | 10-pin; 2x5; 0.8mm pitch; Samtec ERF8 female socket; mates with ERM8-005 male headers; used for rotor-chain JTAG and power pass-through | ERF8-005-05.0-S-DV-K-TR | SAM13517CT-ND | 200-ERF8005050SDVKTR | C7273978 | RECHECK | Used across Stator rotor-slot sockets, Extension outputs, and Rotor Board B outputs. |
| 37 | ROT + REF | J3 (Rotor input + Reflector input 20-pin) | 20-pin; 2x10; 0.8mm pitch; Samtec ERM8 male header; mates with ERF8-010 female sockets; carries ENC data bus | ERM8-010-05.0-S-DV-K-TR | SAM8610CT-ND | 200-ERM8010050SDVKTR | C374877 | RECHECK | Used for Rotor J3 and Reflector J3. Confirm one MPN is valid across all 20-pin male ERM8 applications. |
| 38 | STA + EXT + ROT | J3/J6 (20-pin female outputs) | 20-pin; 2x10; 0.8mm pitch; Samtec ERF8 female socket; mates with ERM8-010 male headers; ENC data link | ERF8-010-05.0-S-DV-K-TR | SAM8618CT-ND | 200-ERF8010050SDVKTR | C3646170 | RECHECK | Used across Stator rotor-slot sockets, Extension outputs, and Rotor Board B outputs. |
| 39 | ROT | H_SW3 (Board A male side) | 1x7; 2.54mm pitch; vertical THT male pin header; inner-face manual post-SMT assembly; mates with RS1-07-G on Rotor Board B; carries SW3[0:5] + GND | PH1-07-UA | 2057-PH1-07-UA-ND | 737-PH1-07-UA | C3331618 | RECHECK | Rotor Design_Spec explicitly uses PH1-07-UA on Board A and RS1-07-G on Board B for physical keying. |
| 40 | ROT | H_SW3 (Board B female side) | 1x7; 2.54mm pitch; vertical THT female socket; inner-face manual post-SMT assembly; mates with PH1-07-UA on Rotor Board A | RS1-07-G | 2057-RS1-07-G-ND | 737-RS1-07-G | C3321543 | RECHECK | Companion part to row 39. Verify socket height and mating fit against rotor inter-board gap. |
| 41 | ENC + STA | J2 (Encoder) / J4-J6 (Stator) | 26-pin; 2x13; 2.54mm pitch; vertical shrouded box header with polarisation key; IDC ribbon-cable interface carrying 3V3_ENIG, JTAG, ENC_IN[0:5], ENC_OUT[0:5] | T821126A1S100CEU | TBD | TBD | C3013501 | RECHECK | Existing docs call out RS-Online 832-3503 rather than Mouser/DigiKey. Verify exact distributor availability and mating IDC cable family. |
| 42 | STA + EXT + REF | J7 / J7 IN / J8 OUT / J4 | 16-pin; 2x8; 2.54mm pitch; vertical shrouded box header; reflector/extension interconnect carrying 3V3_ENIG, SYS_RESET_N, ENC_IN[0:5], ENC_OUT[0:5], TTD_RETURN, GND | BHR-16-VUA | 2057-BHR-16-VUA-ND | 737-BHR-16-VUA | C17692295 | RECHECK | Used on Stator J7, Extension J7/J8, and Reflector J4. Verify one common part is acceptable across all cable-entry orientations. |
| 43 | ROT + JDB | H_PWR / H_SENS / JDB J1 male | 1x5; 2.54mm pitch; vertical THT male pin header; used for Rotor internal keyed interconnects and JDB INPUT header | PH1-05-UA | 2057-PH1-05-UA-ND | 737-PH1-05-UA | C5374051 | RECHECK | Shared across Rotor Board B H_PWR/H_JTAG, Rotor Board A H_SENS, and JDB J1. Confirm one header family is acceptable for all these uses. |
| 44 | ROT + CTL | H_PWR / H_JTAG / H_SENS counterpart + J_JDB_PWR female | 1x5; 2.54mm pitch; vertical THT female socket; used for Rotor internal keyed interconnects and Controller J_JDB_PWR | RS1-05-G | 2057-RS1-05-G-ND | 737-RS1-05-G | C3321119 | RECHECK | Shared across Rotor Board A H_PWR/H_JTAG, Rotor Board B H_SENS, and Controller J_JDB_PWR. |
| 45 | JDB | J2 male | 1x10; 2.54mm pitch; vertical THT male pin header; JTAG OUTPUT header with interleaved GND convention; mates with Controller J_JDB_JTAG | PH1-10-UA | 2057-PH1-10-UA-ND | 737-PH1-10-UA | C3330527 | RECHECK | JDB Design_Spec defines this as the hat JTAG output header. |
| 46 | CTL | J_JDB_JTAG female | 1x10; 2.54mm pitch; vertical THT female socket; mates with JDB J2 PH1-10-UA; Controller hat-mount JTAG header | RS1-10-G | 2057-RS1-10-G-ND | 737-RS1-10-G | C3320525 | RECHECK | Controller Design_Spec defines this as the female mate to the JDB JTAG OUTPUT header. |
| 47 | CTL | J3 | Dual-stacked USB 3.0 Type-A receptacle; right-edge external I/O; 5.0mm overhang; high-speed CM5 USB 3.0 port | 48406-0003 | WM10420-ND | 538-48406-0003 | C565298 | RECHECK | Controller right-edge external I/O. Verify mechanical overhang and shield/tab footprint against enclosure cutout. |
| 48 | CTL | J4 | Full-size HDMI Type-A receptacle; right-edge external I/O; 5.0mm overhang; HDMI current-limited separately from USB | 2007435-1 | A141617-ND | 571-2007435-1 | C195051 | RECHECK | Controller right-edge external I/O. Verify shell geometry and board-edge placement remain correct. |
| 49 | PM | J4 | USB Type-C power input only; 6-position right-angle SMT receptacle; board-edge / panel-facing mount; CC1/CC2 for PD negotiation; retention pins; no USB data lines | USB4135-GF-A | 2073-USB4135-GF-ACT-ND | 640-USB4135-GF-A | C5438410 | RECHECK | Power-only USB-C on Power Module. Mechanical wall-flush fit is explicitly called out for prototype verification. |
| 50 | PM | J2 | RJ45 MagJack for PoE 802.3bt Type 4 input; long-body THT; integrated magnetics for 1GbE / PoE entry | 7499111121A | 1297-1070-5-ND | 710-7499111121A | C5523983 | RECHECK | Power Module PoE input. Verify integrated magnetics / PoE rating and footprint suitability for long-body jack. |
| 51 | PM | J3 | 5-circuit; 1-row; 3.0mm pitch; vertical THT Molex Micro-Fit 3.0; gold contacts; board lock; battery connector carrying VBATT, SMBus SDA/SCL, and presence detect | 43650-0519 | WM14587-ND | 538-43650-0519 | C563849 | RECHECK | Existing design notes explicitly say battery suitability still needs confirmation (current rating, locking, and application fit). |
| 52 | ENC / Plugboard | J1 (x64) | 6.35mm (1/4in) mono switched panel-mount jack; 3 terminals (Tip / Switch / Sleeve); N/C Switch to Sleeve identity path when no plug inserted; harnessed to BT1-128 spade banks | SaiBuy.Ltd eBay item 334364197440 | TBD | TBD | TBD | RECHECK | Already purchased; no formal manufacturer MPN captured yet. If this candidate is rejected, replacement must preserve switched-contact behavior and panel-mount geometry. |
| 53 | ENC / Plugboard | BT1-BT128 | 6.35mm (0.250in) straight vertical PCB-mount male blade tab; through-hole; mates with 6.35mm female crimp spade harness terminals | 1285-ST | 36-1285-ST-ND | 534-1285-ST | C5370868 | RECHECK | Used as two rows of 64 blade terminals on Encoder boards. Confirm tab dimensions and PCB retention versus harness force. |
| 54 | SBD | SW_B1_EN, SW_B1[0:3], SW_B2_EN, SW_B2[0:5] | SPDT latching sub-mini toggle; panel-mount; T2 actuator; B4 bushing; M2 termination; sealed base | 200MSP1T2B4M2QE | EG5525-ND | 612-200MSP1T2B4M2QE | C5491263 | VERIFIED | Datasheet reviewed from `design/Datasheets/200MSP1T2B4M2QE-200-series-datasheet.pdf`: MSP1 = SPDT ON-NONE-ON, T2 actuator, B4 non-threaded 10-48 bushing, M2 termination, Q silver contacts rated 3A @ 120VAC / 28VDC, -40 to +85C. Selected for all 12 Settings Board toggles. |
| 55 | SBD | LED_B1_EN, LED_B1[0:3], LED_B2_EN, LED_B2[0:5] | 5mm common-anode RGB through-hole LED; red + green used in normal operation; blue retained via per-switch 0Ω debug link; white diffused lens | WP154A4SEJ3VBDZGW/CA | 754-2029-ND | 604-WP154A43VBDZGWCA | C7151795 | VERIFIED | Datasheet reviewed from `design/Datasheets/WP154A4SEJ3VBDZGW-CA-datasheet.pdf`: Kingbright 5mm common-anode RGB LED, 60° viewing angle, through-hole, lead-forming / spacer guidance documented. Use separate red and green series resistors per switch under nominal 3.3V operation, with a dedicated 0Ω blue debug link footprint added for prototype work. Mouser order code copied from current sourcing notes and should be cross-checked before placing an order. |
| 56 | PM | SW1 | Rugged metal latching power switch with RGB ring LED; 16mm panel cutout; 2.8mm pin terminals; serviceable harness to PCB spade tabs | Adafruit 4660 | 1528-4660-ND | 485-4660 | Global sourcing / consignment | VERIFIED | Datasheet reviewed from `design/Datasheets/Adafruit-4660-datasheet.pdf`: PM162-K family, latching metal switch with tri-colour ring option, 2.8x0.5mm terminals, IP65, IK08, 500k mechanical cycles. Selected for the Power Module front-panel power control. |
| 57 | PM | BT_SW1_1-BT_SW1_6 | 2.8mm (0.110in) vertical PCB-mount male blade terminal; mates with Adafruit 4660 switch terminals for switch + RGB ring harness | TBD | TBD | TBD | TBD | RECHECK | Required because SW1 is now documented as a field-serviceable harnessed subassembly. Select six PCB tabs that match the switch's 2.8mm quick-connect format and retention/mechanical load requirements. |
| 58 | SBD | R_LED_B (x12) | 0Ω 0603 debug link; one per switch LED blue cathode; retains a clean bodge / measurement point without changing normal red/green operation | ERJ-3GEY0R00V | P0.0BYCT-ND | 667-ERJ-3GEY0R00V | C25807 | VERIFIED | Reuses the existing generic 0Ω 0603 bond/isolation resistor already specified elsewhere in the repository. Added to the Settings Board blue path for consistency and easier prototype debugging. |

## Full BOM Coverage Checklist

This checklist mirrors every active line item in `design/Electronics/Consolidated_BOM.md` component usage summary so the manual re-verification pass cannot silently skip parts.
Use the detailed table above for supplier-level working rows; any coverage item still marked `NEEDS DETAIL ROW` should be promoted into the detailed table before propagating changes into design docs.

**Active BOM summary items tracked:** 106

| Coverage ID | BOM line | Component / MPN | System Total | Detailed row | Coverage status |
| --- | ---: | --- | ---: | --- | --- |
| C001 | 29 | EPM240T100I5N — Intel MAX II CPLD (TQFP-100) | 6 | — | NEEDS DETAIL ROW |
| C002 | 30 | EPM570T100I5N — Intel MAX II CPLD (TQFP-100; 570 LEs; drop-in for EPM240; used on Stator and Rotor boards) | 31 | — | NEEDS DETAIL ROW |
| C003 | 31 | INA219AIDR — Zero-Drift Power Monitor (SOIC-8) | 2 | — | NEEDS DETAIL ROW |
| C004 | 32 | FDC2114RGHR — 4-ch Capacitive Sensor IC, U2 Track A (bits[5:3] N=64; bits[3:0] N=26), Board A, addr 0x2A (16-VQFN) | 30 | — | NEEDS DETAIL ROW |
| C005 | 33 | FDC2114RGHR — 4-ch Capacitive Sensor IC, U3 Track B (bits[2:0] N=64 only; NOT POPULATED for N=26), Board B, addr 0x2B (16-VQFN) | 30 | — | NEEDS DETAIL ROW |
| C006 | 34 | FDC2114RGHR — 4-ch Capacitive Sensor IC, U4 STGC bit[4] (N=26 only; NOT POPULATED for N=64), Board A, addr 0x2B (16-VQFN) | TBD (N=26 builds only) | — | NEEDS DETAIL ROW |
| C007 | 35 | SN74LVC2G125DCUR — Dual 3-State Buffer (VSSOP-8) | 2 | — | NEEDS DETAIL ROW |
| C008 | 36 | SN74LVC1G14DBVRQ1 — Single Schmitt Inverter (SOT-23-5) | 2 | — | NEEDS DETAIL ROW |
| C009 | 37 | FT232H — USB 2.0 to MPSSE Bridge (QFN-56) | 1 | — | NEEDS DETAIL ROW |
| C010 | 38 | CM5 — Raspberry Pi Compute Module 5 | 1 | — | NEEDS DETAIL ROW |
| C011 | 39 | TPS75733KTTRG3 — 3.3 V LDO Regulator (TO-263 KTT 5-pin) | 1 | — | NEEDS DETAIL ROW |
| C012 | 40 | TPS259804ONRGER — eFuse / Hot-Swap Controller (VQFN-24) | 1 | — | NEEDS DETAIL ROW |
| C013 | 41 | LMQ61460AFSQRJRRQ1 — 5 V Synchronous Buck Converter (VQFN-HR RJR 14-pin 4×3.5mm) | 2 | — | NEEDS DETAIL ROW |
| C014 | 42 | LTC3350EUHF#PBF — Supercapacitor Manager (QFN-38) | 1 | — | NEEDS DETAIL ROW |
| C015 | 43 | TPS25751DREFR — USB PD 3.1 DRP Controller (WQFN-38) | 1 | — | NEEDS DETAIL ROW |
| C016 | 44 | STUSB4500LQTR — USB-C Sink Controller (QFN-24) | 1 | — | NEEDS DETAIL ROW |
| C017 | 45 | LM74700QDBVRQ1 — Ideal-Diode OR-ing Controller (SOT-23-6) | 3 | — | NEEDS DETAIL ROW |
| C018 | 46 | MCP121T-450E/LB — 4.5 V Voltage Supervisor (SC70-3) | 1 | — | NEEDS DETAIL ROW |
| C019 | 47 | TPS2372-4 — PoE PD Interface Type 4 (VQFN-20) | 1 | — | NEEDS DETAIL ROW |
| C020 | 48 | TPS23730RMTR — PoE ACF DC-DC Controller (WQFN-20) | 1 | — | NEEDS DETAIL ROW |
| C021 | 49 | MIC1555YM5-TR — CMOS Timer / LED Oscillator (SOT-23-5) | 2 | — | NEEDS DETAIL ROW |
| C022 | 50 | TPS2065C — USB Power Distribution Switch (SOT-23-5) | 1 | — | NEEDS DETAIL ROW |
| C023 | 51 | AP2331W — HDMI Current Limiter (SOT-23-5) | 1 | — | NEEDS DETAIL ROW |
| C024 | 52 | TPD4E05U06QDQARQ1 — 4-Channel ESD Array (U-DFN-10) | 4 | — | NEEDS DETAIL ROW |
| C025 | 53 | TPD1E10B06DYARQ1 — Single-Channel ESD (SOD-523) | 1 | — | NEEDS DETAIL ROW |
| C026 | 54 | TPD2E2U06DRLR — Dual-Channel SMBus ESD (SOT-553) | 1 | — | NEEDS DETAIL ROW |
| C027 | 55 | CSD17483F4T — 30 V 10 A N-ch OR-ing MOSFET (SON-8) | 3 | — | NEEDS DETAIL ROW |
| C028 | 56 | BSS138 (onsemi) — 50 V N-ch Logic-Level MOSFET (SOT-23) | 6 | 29 | DETAIL ROW PRESENT |
| C029 | 57 | BAT54 (Diotec) — Schottky Diode (SOD-323 / SOT-23) | 3 | — | NEEDS DETAIL ROW |
| C030 | 58 | MCP23017T-E/SO — I²C GPIO Expander 16-bit (SOIC-28) | 5 | — | NEEDS DETAIL ROW |
| C031 | 59 | PCA9685BS/3 — I²C 16-ch PWM Driver (SSOP-28) | 1 | — | NEEDS DETAIL ROW |
| C033 | 61 | J_DSI1 — DSI1 FPC 15-pin 1.0mm ZIF connector (TBD MPN) | 1 | 3 | DETAIL ROW PRESENT |
| C034 | 63 | 0.1 µF X7R 0402 decoupling cap | 513 | — | NEEDS DETAIL ROW |
| C035 | 64 | 10 µF X7R 50 V 1206 bulk decoupling (CL31B106KBHNNNE) | 185 | — | NEEDS DETAIL ROW |
| C036 | 65 | 22 µF X7R 25 V 1210 bulk cap (CL32B226KAJNNNE) | 15 | — | NEEDS DETAIL ROW |
| C037 | 66 | 4.7 µF X7R 0402 entry filter (JDB 5V_USB, C19666) | 1 | — | NEEDS DETAIL ROW |
| C038 | 67 | 10 µF 16 V X7R 0603 monostable timing cap (CL10B106KA8NNNC) | 1 | — | NEEDS DETAIL ROW |
| C039 | 68 | 1 µF X7R 50 V 0805 (C0805C105K5RACTU) | 3 | — | NEEDS DETAIL ROW |
| C040 | 69 | 10 µF 25 V X7R 1206 LDO input cap (C1206C106K3RACTU) | 1 | — | NEEDS DETAIL ROW |
| C041 | 70 | 10 nF X7R 50 V 0402 soft-start cap (CL05B103KB5NNNC) | 1 | — | NEEDS DETAIL ROW |
| C042 | 71 | 10 nF 100 V X7R 0402 Bob Smith termination cap | 1 | — | NEEDS DETAIL ROW |
| C043 | 72 | 100 pF X7R 25 V 0402 SYNC SW-ringing LP filter (C0402C101K3RACAUTO) | 1 | — | NEEDS DETAIL ROW |
| C044 | 73 | 22 nF X7R 25 V 0603 SYNC phase-delay cap (CL10B223KB8WPNC) | 1 | — | NEEDS DETAIL ROW |
| C045 | 74 | 25 F / 2.7 V Supercapacitor (Abracon ADCR-T02R7SA256MB) | 8 | 6 | DETAIL ROW PRESENT |
| C046 | 75 | 22 µF 25 V X7R 1210 5V_MAIN backup bulk cap C35 (Samsung CL32B226KAJNNNE, 2× in parallel) | 2 | — | NEEDS DETAIL ROW |
| C047 | 77 | 10 kΩ 1% 0603 pull resistor(ERJ-3EKF1002V / C25804) | 31 | 14, 27 | DETAIL ROW PRESENT |
| C048 | 78 | 10 kΩ 1% 0402 pull resistor (ERJ-2RKF1002X / C25744) | 329 | 22 | DETAIL ROW PRESENT |
| C049 | 79 | 75 Ω 1% 0603 series resistor (ERJ-3EKF75R0V / C105905) | 9 | — | NEEDS DETAIL ROW |
| C050 | 80 | 75 Ω 1% 0402 series resistor (ERJ-2RKF75R0X) | 37 | 24 | DETAIL ROW PRESENT |
| C051 | 82 | 33 Ω 1% 0402 series resistor (ERJ-2RKF33R0X / C25808) | 7 | — | NEEDS DETAIL ROW |
| C052 | 83 | 22 Ω 0603 1% JTAG end-of-chain damping (ERJ-3EKF2200V) | 1 | 25 | DETAIL ROW PRESENT |
| C053 | 84 | 330 Ω 1% 0402 LED current-limit resistor (ERJ-2RKF3300X / C105872) | 6 | — | NEEDS DETAIL ROW |
| C054 | 85 | 330 Ω 1% 0603 Ethernet activity LED resistor (ERJ-3EKF3300V / C25803) | 2 | — | NEEDS DETAIL ROW |
| C055 | 86 | 4.7 kΩ 1% 0603 I²C pull-up (ERJ-3EKF4701V) | 2 | 21 | DETAIL ROW PRESENT |
| C056 | 87 | 100 Ω 1% 0603 differential termination (ERJ-3EKF1000V / C25806) | 1 | — | NEEDS DETAIL ROW |
| C057 | 89 | 10 mΩ ±1% 5 A 2512 Kelvin shunt (CSS2H-2512R-R010ELF) | 3 | 12 | DETAIL ROW PRESENT |
| C058 | 90 | 121 kΩ 1% 0603 PoE MPS current set (ERJ-3EKF1213V) | 1 | 13 | DETAIL ROW PRESENT |
| C059 | 91 | 301 Ω 1% 0603 charge current set (ERJ-3EKF3010V) | 1 | 11 | DETAIL ROW PRESENT |
| C060 | 92 | 274 kΩ 1% 0603 MIC1555 U15 monostable R28 (ERJ-3EKF2743V) | 1 | 16 | DETAIL ROW PRESENT |
| C061 | 93 | 715 kΩ 1% 0603 MIC1555 timer R\_B (ERJ-3EKF7153V) | 1 | 15 | DETAIL ROW PRESENT |
| C062 | 94 | 232 kΩ 1% 0603 thick-film eFuse UVLO (ERJ-3EKF2323V) | 1 | 17 | DETAIL ROW PRESENT |
| C063 | 95 | 28.7 kΩ 1% 0603 thick-film eFuse UVLO (ERJ-3EKF2872V) | 1 | 18 | DETAIL ROW PRESENT |
| C064 | 96 | 210 Ω 0.1% 0603 thin-film eFuse ILIM (ERA-3ARB2100V) | 1 | 7 | DETAIL ROW PRESENT |
| C065 | 97 | 86.6 kΩ 1% 0603 thick-film SYNC FSET resistor (ERJ-3EKF8662V) | 1 | 19 | DETAIL ROW PRESENT |
| C066 | 98 | 82.0 kΩ 1% 0402 thick-film SYNC phase-delay R\_DLY (ERJ-2RKF8202X) | 1 | 20 | DETAIL ROW PRESENT |
| C067 | 99 | 30.1 kΩ 0.1% 0603 thin-film supercap BACKUP R\_TOP (ERA-3ARB3012V — see DEC-030) | 1 | 8 | DETAIL ROW PRESENT |
| C068 | 100 | 10.0 kΩ 0.1% 0603 thin-film supercap BACKUP R\_BOT (ERA-3ARB103V) | 1 | 9 | DETAIL ROW PRESENT |
| C069 | 101 | 33.2 kΩ 1% 0402 thick-film LTC3350 RT freq-set (ERA-2AEB3322X) | 1 | 10 | DETAIL ROW PRESENT |
| C070 | 102 | 0 Ω 0603 bond / isolating resistor (ERJ-3GEY0R00V / C25807) | 14 | 58 | DETAIL ROW PRESENT |
| C071 | 103 | Ferrite bead 120 Ω @100 MHz 4.0 A 1206 (Laird HI1206P121R-10) | 4 | — | NEEDS DETAIL ROW |
| C072 | 105 | ERM8-040 80-pin Samtec BtB Male Header(Link-Alpha) | 1 | 31 | DETAIL ROW PRESENT |
| C073 | 106 | ERF8-040 80-pin Samtec BtB Female Socket (Link-Alpha) | 1 | 32 | DETAIL ROW PRESENT |
| C074 | 107 | ERM8-020 40-pin Samtec BtB Male Header (Link-Beta) | 1 | 33 | DETAIL ROW PRESENT |
| C075 | 108 | ERF8-020 40-pin Samtec BtB Female Socket (Link-Beta) | 1 | 34 | DETAIL ROW PRESENT |
| C076 | 109 | ERM8-005 10-pin Samtec Male Header 0.8 mm (Rotor interface) | 64 | 35 | DETAIL ROW PRESENT |
| C077 | 110 | ERF8-005 10-pin Samtec Female Socket 0.8 mm (Rotor interface) | 64 | 36 | DETAIL ROW PRESENT |
| C078 | 111 | ERM8-010 20-pin Samtec Male Header 0.8 mm (ENC data) | 32 | 37 | DETAIL ROW PRESENT |
| C079 | 112 | ERF8-010 20-pin Samtec Female Socket 0.8 mm (ENC data) | 32 | 38 | DETAIL ROW PRESENT |
| C080 | 113 | Adam Tech PH1-07-UA — 1×7 2.54mm male pin header, Rotor Board A H\_SW3 (Mouser 737-PH1-07-UA; DigiKey 2057-PH1-07-UA-ND; JLCPCB C3331618) | 30 | 39 | DETAIL ROW PRESENT |
| C081 | 114 | Adam Tech RS1-07-G — 1×7 2.54mm female socket, Rotor Board B H\_SW3 (Mouser 737-RS1-07-G; DigiKey 2057-RS1-07-G-ND; JLCPCB C3321543) | 30 | 40 | DETAIL ROW PRESENT |
| C082 | 115 | Amphenol T821126A1S100CEU — 26-pin 2×13 shrouded box header, 2.54mm (RS-Online 832-3503; JLCPCB C3013501) | 6 | 41 | DETAIL ROW PRESENT |
| C083 | 116 | Adam Tech BHR-16-VUA — 16-pin 2×8 shrouded box header, 2.54mm (Mouser 737-BHR-16-VUA; DigiKey 2057-BHR-16-VUA-ND; JLCPCB C17692295) | 4 | 42 | DETAIL ROW PRESENT |
| C084 | 117 | Adam Tech PH1-05-UA — 1×5 2.54mm male pin header, JDB J1/Rotor H\_PWR+H\_JTAG(BrdB)+H\_SENS(BrdA) (Mouser 737-PH1-05-UA; DigiKey 2057-PH1-05-UA-ND; JLCPCB C5374051) | 91 | 43 | DETAIL ROW PRESENT |
| C085 | 118 | Adam Tech RS1-05-G — 1×5 2.54mm female socket, CTL J\_JDB\_PWR/Rotor H\_PWR+H\_JTAG(BrdA)+H\_SENS(BrdB) (Mouser 737-RS1-05-G; DigiKey 2057-RS1-05-G-ND; JLCPCB C3321119) | 91 | 44 | DETAIL ROW PRESENT |
| C086 | 119 | Adam Tech PH1-10-UA — 1×10 2.54mm male pin header, JDB J2 JTAG OUTPUT (Mouser 737-PH1-10-UA; DigiKey 2057-PH1-10-UA-ND; JLCPCB C3330527) | 1 | 45 | DETAIL ROW PRESENT |
| C087 | 120 | Adam Tech RS1-10-G — 1×10 2.54mm female socket, Controller J_JDB_JTAG (Mouser 737-RS1-10-G; DigiKey 2057-RS1-10-G-ND; JLCPCB C3320525) | 1 | 46 | DETAIL ROW PRESENT |
| C088 | 121 | USB 3.0 Type-A Dual-Stack (Molex 48406-0003) | 1 | 47 | DETAIL ROW PRESENT |
| C089 | 122 | HDMI Type-A Full-Size (TE 2007435-1) | 1 | 48 | DETAIL ROW PRESENT |
| C090 | 123 | USB-C SMT Receptacle 6-pos (GCT USB4135-GF-A) | 1 | 49 | DETAIL ROW PRESENT |
| C091 | 124 | RJ45 MagJack (Würth 7499111121A) | 1 | 50 | DETAIL ROW PRESENT |
| C092 | 125 | Battery Connector 5-pin Micro-Fit 3.0 (Molex 43650-0519) | 1 | 51 | DETAIL ROW PRESENT |
| C093 | 127 | 12 MHz Crystal SMD(Abracon ABM8-12.000MHz-B2-T / C9002) | 1 | — | NEEDS DETAIL ROW |
| C094 | 128 | 72°C SMD Thermal Cutoff (Bourns AC72ABD) | 1 | — | NEEDS DETAIL ROW |
| C095 | 129 | CR2032 Coin Cell Holder (Keystone 3034) | 1 | — | NEEDS DETAIL ROW |
| C096 | 130 | Würth 9774040151R M2.5 × 4.0mm SMT Brass Standoff (CM5 mount) | 4 | — | NEEDS DETAIL ROW |
| C097 | 131 | PoE ACF Isolation Transformer (Coilcraft POE600F-12LD) | 1 | — | NEEDS DETAIL ROW |
| C098 | 132 | EMI Common-Mode Choke (Würth WE-CMBNC 7448031002) | 2 | — | NEEDS DETAIL ROW |
| C099 | 133 | DM Filter Inductor 10 µH 15.5 A (Bourns SRP1265A-100M) | 1 | — | NEEDS DETAIL ROW |
| C100 | 134 | Power Module RGB Metal Power Switch (Adafruit 4660) | 1 | 56 | DETAIL ROW PRESENT |
| C101 | 135 | Power Module 2.8 mm PCB Male Spade Tabs (SW1 harness) | 6 | 57 | DETAIL ROW PRESENT |
| C102 | 136 | Tactile SMT Reset Switch (SKRPACE010) | 1 | 2 | DETAIL ROW PRESENT |
| C103 | 137 | Green SMD LED 0402 (Würth 150060VS75000 / C2286) | 6 | — | NEEDS DETAIL ROW |
| C104 | 138 | 6.35 mm Mono Switched Panel-Mount Jack Socket (Stecker) | 192 | 52 | DETAIL ROW PRESENT |
| C105 | 139 | DPDT 6-pin Momentary Keyboard Switch | 192 | — | NEEDS DETAIL ROW |
| C106 | 140 | 6.35 mm PCB Blade Terminal (Keystone 1285-ST) | 384 | 53 | DETAIL ROW PRESENT |
| C107 | 142 | CTS 219-6LPSTR — 6-pos DIP switch, 2.54mm THT | 90 | — | NEEDS DETAIL ROW |
