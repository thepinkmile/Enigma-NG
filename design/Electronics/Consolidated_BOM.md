# Consolidated Bill of Materials

<!-- markdownlint-disable MD013 MD055 MD056 -->

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-30

---

## Notes and Conventions

- Manufacturer shown in Description/Usage column as `[Manufacturer]`.
- Board codes: PM = Power Module · CTL = Controller · STA = Stator · ROT-A = Rotor Board A · ROT-B = Rotor Board B · SBD = Settings Board · EXT = Extension · REF = Reflector · ENC = Encoder · AM = Actuation Module · JDB = JTAG Daughterboard.
- **Footprint Downloaded** column: user-maintained. Replace "Pending" with tick once the footprint is added to the shared KiCAD library.
- **CSD17578Q5A replaces CSD17483F4T:** OR-ing MOSFET corrected from the incorrectly specified CSD17483F4T (1.5A FemtoFET) to CSD17578Q5A (30V 25A 5.9mΩ SON 5×6mm). DigiKey: 296-48512-1-ND, Mouser: 595-CSD17578Q5A, JLCPCB: C2871447.
- **LMQ61460AFSQRJRRQ1 Mouser PN:** `595-Q61460AFSQRJRRQ1` drops the "LM" prefix — confirmed correct Mouser convention.
- **ERJ-2RKF1001X duplicate JLCPCB codes:** PM uses `C25705`, SBD uses `C242161`; DigiKey PNs also differ. Both rows preserved as extracted from board specs.
- **Locked parts** marked with a lock symbol require owner approval before any change.

---

## Section 1 — Full Component Table

| Board | RefDes | MPN | DigiKey | Mouser | JLCPCB | Alternative Supplier | Part Specification | Description / Usage | Footprint Available | Footprint Downloaded |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Power Module | C1-C15 | CL32B226KAJNNNE | 1276-3392-1-ND | 187-CL32B226KAJNNNE | C309062 | — | 22µF 25V X7R 1210 | Bulk decoupling [Samsung] | Yes | Pending |
| Power Module | C16-C19 | CGA9N3X7R1E476M230KB | 445-174773-1-ND | 810-A9N3X7476M23KB | C2182815 | — | 47µF 25V X7R 2220 | Large bulk decoupling [TDK] | Yes | Pending |
| Power Module | C20 | CL21B106KAYQNNE | 399-C1206C106K3RACTUCT-ND | 80-C1206C106K3R | C2168111 | — | 10µF 25V X7R 1206 | Decoupling [Samsung] | Yes | Pending |
| Power Module | C21-C23 | C0805C105K5RACTU | 399-C0805C105K5RACTUCT-ND | 80-C0805C105K5R | C3018567 | — | 1µF 50V X7R 0805 | Decoupling [Kemet] | Yes | Pending |
| Power Module | C24-C39 | CL05B104KB5NNNC | 1276-1009-1-ND | 187-CL05B104KB5NNNC | C1525 | — | 100nF 50V X7R 0402 | Bypass decoupling [Samsung] | Yes | Pending |
| Power Module | C40 | C0402C101K3RACAUTO | 399-C0402C101K3RACAUTOCT-ND | 80-C0402C101K3RAUTO | C5272912 | — | 100pF X7R 25V 0402 | Filter cap [Kemet] | Yes | Pending |
| Power Module | C_SC1-C_SC8 | ADCR-T02R7SA256MB | 535-ADCR-T02R7SA256MB-ND | 815-ADCRT02R7SA256MB | — | Global sourcing | 25F 2.7V supercap THT Radial 16x25mm | Supercapacitor bank (LTC3350) [Abracon] | Yes | Pending |
| Power Module | C41 | CL10B223KB8WPNC | 1276-6534-1-ND | 187-CL10B223KB8WPNC | C346197 | — | 22nF X7R 25V 0603 | SYNC delay cap [Samsung] | Yes | Pending |
| Power Module | C42 | CC1206KKX7R8BB106 | 311-1959-1-ND | 603-CC126KKX7R8BB106 | C70462 | — | 10µF 16V X7R 1206 | Decoupling [YAGEO] | Yes | Pending |
| Power Module | C43-C52 | CL05B104KB5NNNC | 1276-1009-1-ND | 187-CL05B104KB5NNNC | C1525 | — | 100nF 50V X7R 0402 | Bypass decoupling [Samsung] | Yes | Pending |
| Power Module | C51 | CL05B103KB5NNNC | 1276-1008-1-ND | 187-CL05B103KB5NNNC | C15195 | — | 10nF 50V X7R 0402 | Filter cap [Samsung] | Yes | Pending |
| Power Module | C53 | C0805C105K5RACTU | 399-C0805C105K5RACTUCT-ND | 80-C0805C105K5R | C3018567 | — | 1µF 50V X7R 0805 | Decoupling [Kemet] | Yes | Pending |
| Power Module | C54 | CC1206KKX7R8BB106 | 311-1959-1-ND | 603-CC126KKX7R8BB106 | C70462 | — | 10µF 16V X7R 1206 | Decoupling [YAGEO] | Yes | Pending |
| Power Module | C55-C57 | C0805C105K5RACTU | 399-C0805C105K5RACTUCT-ND | 80-C0805C105K5R | C3018567 | — | 1µF 50V X7R 0805 | Decoupling [Kemet] | Yes | Pending |
| Power Module | D1 | TPD1E10B06DYARQ1 | 296-TPD1E10B06DYARQ1CT-ND | 595-TPD1E10B06DYARQ1 | C3013901 | — | ESD SOD-523 | ESD protection diode [Texas Instruments] | Yes | Pending |
| Power Module | D2 | TPD2E2U06DRLR | 296-38361-1-ND | 595-TPD2E2U06DRLR | C1972959 | — | ESD SOT-553 | Dual ESD protection [Texas Instruments] | Yes | Pending |
| Power Module | D3 | TPD4E05U06QDQARQ1 | 296-40696-1-ND | 595-PD4E05U06QDQARQ1 | C81353 | — | 4-ch ESD ±15kV U-DFN-10 | 4-channel ESD array [Texas Instruments] | Yes | Pending |
| Power Module | D6,D7 | BAT54 | 4878-BAT54CT-ND | 637-BAT54 | C49435667 | — | Schottky SOT-23 | Schottky diode [Vishay] | Yes | Pending |
| Power Module | F1 | AC72ABD | AC72ABD-ND | 652-AC72ABD | C17468669 | — | 72°C SMD Thermal Cutoff | Thermal cutoff fuse [Bourns] | Yes | Pending |
| Power Module | J1-J3 | 1123684-7 | A114780-ND | 571-1123684-7 | C3683043 | — | 10-pos 2.5mm RA plug | Link-Alpha power/telemetry right-angle plugs [TE Connectivity] | Yes | Pending |
| Power Module | J4 | 0436500519 | WM14587-ND | 538-43650-0519 | C563849 | — | 5-pin Micro-Fit 3.0 THT vertical | Internal power connector [Molex] | Yes | Pending |
| Power Module | J5 | USB4135-GF-A | 2073-USB4135-GF-ACT-ND | 640-USB4135-GF-A | C5438410 | — | USB-C right-angle SMT | USB-C input (PD only) [GCT] | Yes | Pending |
| Power Module | L1,L2 | 7448031002 | 732-5584-ND | 710-7448031002 | C1519839 | — | 10A 2mH nanocrystalline CMC THT | Common mode choke [Würth Elektronik] | Yes | Pending |
| Power Module | L3 | SRP1265A-100M | SRP1265A-100MCT-ND | 652-SRP1265A-100M | C840531 | — | 10µH 15.5A Isat shielded SMT 13.5x12.5x6.2mm | Power inductor (buck converter) [Bourns] | Yes | Pending |
| Power Module | Q1,Q2,Q3 | CSD17578Q5A | 296-48512-1-ND | 595-CSD17578Q5A | C2871447 | — | N-ch MOSFET 30V 10A SON-8 3.3x3.3mm | OR-ing MOSFET [Texas Instruments] | Yes | Pending |
| Power Module | Q4-Q10 | BSS138 | BSS138CT-ND | 512-BSS138 | C52895 | — | N-ch MOSFET 50V 200mA SOT-23 | Logic-level N-FET [onsemi] | Yes | Pending |
| Power Module | R1 | ERJ-3EKF2323V | P232KHCT-ND | 667-ERJ-3EKF2323V | C403086 | — | 232kΩ 1% 0603 | eFuse UVLO-HI [Panasonic] | Yes | Pending |
| Power Module | R2 | ERJ-3EKF2872V | P28.7KHCT-ND | 667-ERJ-3EKF2872V | C403135 | — | 28.7kΩ 1% 0603 | eFuse UVLO-LO [Panasonic] | Yes | Pending |
| Power Module | R3 | ERA-3VEB2100V | 10-ERA-3VEB2100VCT-ND | 667-ERA-3VEB2100V | C1861624 | — | 210Ω 0.1% 0603 | eFuse ILIM [Panasonic] | Yes | Pending |
| Power Module | R6 | ERJ-3EKF1002V | P10.0KHCT-ND | 667-ERJ-3EKF1002V | C191124 | — | 10kΩ 1% 0603 | BATT_PRES_N pull-up [Panasonic] | Yes | Pending |
| Power Module | R7,R8 | ERJ-3EKF4701V | P4.70KHCT-ND | 667-ERJ-3EKF4701V | C192166 | — | 4.7kΩ 1% 0603 | I2C pull-ups [Panasonic] | Yes | Pending |
| Power Module | R9,R10,R22,R29 | ERJ-3EKF1002V | P10.0KHCT-ND | 667-ERJ-3EKF1002V | C191124 | — | 10kΩ 1% 0603 | Pull-up/down resistors [Panasonic] | Yes | Pending |
| Power Module | R11 | ERJ-3EKF3010V | P301HCT-ND | 667-ERJ-3EKF3010V | C403144 | — | 301Ω 1% 0603 | LTC3350 RICHARGE [Panasonic] | Yes | Pending |
| Power Module | R12,R23 | CSS2H-2512R-R010ELF | CSS2H-2512R-R010ELF-ND | 652-CSS2H-2512R-R010ELF | — | — | 10mΩ ±1% 5A 2512 Kelvin shunt | Current sense shunt — no JLCPCB stock [Bourns] | Yes | Pending |
| Power Module | R14 | ERA-3ARB3012V | 10-ERA-3ARB3012VCT-ND | 667-ERA-3ARB3012V | C1728516 | — | 30.1kΩ 0.1% 0603 | LTC3350 backup divider top [Panasonic] | Yes | Pending |
| Power Module | R15 | ERA-3ARB103V | P10KBDCT-ND | 667-ERA-3ARB103V | C465746 | — | 10.0kΩ 0.1% 0603 | LTC3350 backup divider bottom [Panasonic] | Yes | Pending |
| Power Module | R16 | ERJ-3EKF1002V | P10.0KHCT-ND | 667-ERJ-3EKF1002V | C191124 | — | 10.0kΩ 1% 0603 | MIC1555 R_A [Panasonic] | Yes | Pending |
| Power Module | R17 | ERJ-3EKF7153V | P715KHCT-ND | 667-ERJ-3EKF7153V | C403339 | — | 715kΩ 1% 0603 | MIC1555 R_B [Panasonic] | Yes | Pending |
| Power Module | R24 | ERJ-3EKF8662V | P86.6KHCT-ND | 667-ERJ-3EKF8662V | C403381 | — | 86.6kΩ 1% 0603 | LMQ61460A FSET [Panasonic] | Yes | Pending |
| Power Module | R25,R27 | ERJ-2RKF1002X | P10.0KLCT-ND | 667-ERJ-2RKF1002X | C191123 | — | 10kΩ 1% 0402 | SYNC/pull-down [Panasonic] | Yes | Pending |
| Power Module | R26 | ERJ-2RKF8202X | P82.0KLCT-ND | 667-ERJ-2RKF8202X | C400641 | — | 82.0kΩ 1% 0402 | SYNC R_DLY [Panasonic] | Yes | Pending |
| Power Module | R28 | ERJ-3EKF2743V | P274KHCT-ND | 667-ERJ-3EKF2743V | C403126 | — | 274kΩ 1% 0603 | MIC1555 monostable timing [Panasonic] | Yes | Pending |
| Power Module | R30 | ERA-2AEB3322X | P33.2KDCCT-ND | 667-ERA-2AEB3322X | C2087909 | — | 33.2kΩ 1% 0402 | LTC3350 RT freq-set [Panasonic] | Yes | Pending |
| Power Module | R31-R33,R37,R38 | ERJ-2RKF1001X | P1.00KLBCT-ND | 667-ERJ-2RKF1001X | C25705 | — | 1kΩ 1% 0402 | LED gate resistors [Panasonic] | Yes | Pending |
| Power Module | R34-R36,R39,R40 | ERJ-2RKF1002X | P10.0KLCT-ND | 667-ERJ-2RKF1002X | C191123 | — | 10kΩ 1% 0402 | LED gate pull-downs [Panasonic] | Yes | Pending |
| Power Module | R41,R42 | ERJ-2RKF5232X | P52.3KLCT-ND | 667-ERJ-2RKF5232X | — | Global sourcing | 52.3kΩ 1% 0402 | LMQ61460A FB_TOP [Panasonic] | Yes | Pending |
| Power Module | R43,R44 | ERJ-2RKF1002X | P10.0KLCT-ND | 667-ERJ-2RKF1002X | C191123 | — | 10kΩ 1% 0402 | LMQ61460A FB_BOT [Panasonic] | Yes | Pending |
| Power Module | R45-R48 | ERJ-2RKF1003X | P100KLCT-ND | 667-ERJ-2RKF1003X | — | Global sourcing | 100kΩ 1% 0402 | LMQ61460A EN/PG pull-ups [Panasonic] | Yes | Pending |
| Power Module | R49-R53 | ERJ-2RKF10R0X | P10.0LCT-ND | 667-ERJ-2RKF10R0X | — | Global sourcing | 10Ω 1% 0402 | Gate/filter series resistors [Panasonic] | Yes | Pending |
| Power Module | SW1 | 4660 | 1528-4660-ND | 485-4660 | — | Global sourcing | 16mm panel latching RGB metal switch | Latching power switch [Adafruit] | Yes | Pending |
| Power Module | SW2 | 3350 | 1528-2546-ND | 485-3350 | — | Global sourcing | 16mm panel momentary RGB metal switch | Momentary control switch [Adafruit] | Yes | Pending |
| Power Module | BT_SW1_1-6,BT_SW2_1-6 | 1211 | 36-1211-ND | 534-1211 | C3029550 | — | 2.8mm PCB male spade tabs THT Quick-Fit | Switch terminal tabs (x12) [Keystone Electronics] | Yes | Pending |
| Power Module | U1 | TPS259804ONRGER | 296-TPS259804ONRGERCT-ND | 595-TPS259804ONRGER | C2878936 | — | eFuse 16.9V fixed OVLO VQFN-24 4x4mm | Input eFuse — variant-locked do not change [Texas Instruments] | Yes | Pending |
| Power Module | U2A,U2B | LMQ61460AFSQRJRRQ1 | 296-LMQ61460AFSQRJRRQ1CT-ND | 595-Q61460AFSQRJRRQ1 | C1518767 | — | 5V buck x2 180° interleaved VQFN-HR 14-pin 4x3.5mm | Dual-phase 5V buck [Texas Instruments] | Yes | Pending |
| Power Module | U3 | LTC3350EUHF#PBF | 505-LTC3350EUHF#PBF-ND | 584-LTC3350EUHF#PBF | C580711 | — | Supercap manager QFN-38 5x7mm | Supercapacitor charger/backup manager [Analog Devices] | Yes | Pending |
| Power Module | U4 | TPS25751DREFR | 296-TPS25751DREFRCT-ND | 595-TPS25751DREFR | C30169739 | — | PD3.1 DRP controller WQFN-38 6x4mm | USB-C PD controller [Texas Instruments] | Yes | Pending |
| Power Module | U5 | STUSB4500LQTR | 497-STUSB4500LQCT-ND | 511-STUSB4500LQTR | C506650 | — | USB-C sink controller QFN-24 | USB-C sink fallback controller [STMicroelectronics] | Yes | Pending |
| Power Module | U6a,U6b,U6c | LM74700QDBVRQ1 | 296-LM74700QDBVRQ1CT-ND | 595-LM74700QDBVRQ1 | C2941042 | — | OR-ing controller SOT-23-6 | OR-ing diode controller (x3) [Texas Instruments] | Yes | Pending |
| Power Module | U7 | TPS75733KTTRG3 | 296-50559-1-ND | 595-TPS75733KTTRG3 | C3749924 | — | 3.3V LDO fixed TO-263 5-pin | 3V3_ENIG rail LDO [Texas Instruments] | No library — create manually | N/A |
| Power Module | U8 | MCP121T-450E/LB | MCP121T-450E/LBCT-ND | 579-MCP121T-450E/LB | C625189 | — | 4.5V voltage supervisor SC70-3 | Voltage supervisor [Microchip Technology] | No library — create manually | N/A |
| Power Module | U11,U15 | MIC1555YM5-TR | 576-2576-1-ND | 998-MIC1555YM5TR | C145373 | — | CMOS timer SOT-23-5 | Timer (monostable/oscillator) [Microchip Technology] | Yes | Pending |
| Power Module | U12 | INA219AIDR | 296-23978-1-ND | 595-INA219AIDR | C138706 | — | Current monitor I²C 0x40 SOIC-8 | Current/power monitor [Texas Instruments] | Yes | Pending |
| Power Module | U13,U14,U17 | NL27WZ14DFT2G-Q | 488-NL27WZ14DFT2G-QCT-ND | 863-NL27WZ14DFT2G-Q | C24511261 | — | Dual Schmitt-trigger inverter SC-88 | Logic inverter [onsemi] | Yes | Pending |
| Power Module | U16 | PCA9534APWR | 296-21760-1-ND | 595-PCA9534APWR | C2871127 | — | 8-bit I²C GPIO expander 0x3F TSSOP-16 | I2C GPIO expander [NXP Semiconductors] | Yes | Pending |
| Power Module | U18 | SN74LVC1G175DBVR | 296-17617-1-ND | 595-SN74LVC1G175DBVR | C128412 | — | D-type flip-flop shutdown latch SOT-23-6 | Shutdown latch [Texas Instruments] | Yes | Pending |
| Power Module | U19 | SN74LVC1G08DBVR | 296-11601-1-ND | 595-SN74LVC1G08DBVR | C7666 | — | Single AND gate SOT-23-5 | Blink gate [Texas Instruments] | Yes | Pending |
| Controller | C1-C5,C7-C11 | CL21B106KAYQNNE | 1276-CL21B106KAYQNNECT-ND | 187-CL21B106KAYQNNE | C3039694 | — | 10µF X7R 25V 0805 | Bulk decoupling [Samsung] | Yes | Pending |
| Controller | C6,C12,C24 | CL05B104KB5NNNC | 1276-1009-1-ND | 187-CL05B104KB5NNNC | C1525 | — | 100nF X7R 50V 0402 | Bypass decoupling [Samsung] | Yes | Pending |
| Controller | C25 | C0402C103K1RACAUTO | 399-C0402C103K1RACAUTOCT-ND | 80-C0402C103K1RAUTO | C19862710 | — | 10nF 100V X7R 0402 | Filter cap [Kemet] | Yes | Pending |
| Controller | BT1 | 3034TR | 36-3034CT-ND | 534-3034TR | C5213768 | — | CR2032 holder THT horizontal | RTC battery holder [Keystone Electronics] | Yes | Pending |
| Controller | D1 | BAT54 | 4878-BAT54CT-ND | 637-BAT54 | C49435667 | — | Schottky SOT-23 | Schottky diode [Vishay] | Yes | Pending |
| Controller | J1-J3 | 1-1674231-1 | A119250-ND | 571-1-1674231-1 | C3683260 | — | 10-pos 2.5mm receptacle 10-pos vert | Link-Alpha dock receptacles [TE Connectivity] | Yes | Pending |
| Controller | J4,J5 | 2195630015 | 900-2195630015-ND | 538-219563-0015 | — | Global sourcing | 5-pwr+15-sig press-fit receptacle hybrid | Link-Beta hybrid receptacles [Molex] | Yes | Pending |
| Controller | J6 | 48406-0003 | WM10420-ND | 538-48406-0003 | C565298 | — | USB 3.0 Type-A dual-stack | USB 3.0 host port [Molex] | Yes | Pending |
| Controller | J7 | 2007435-1 | A141617-ND | 571-2007435-1 | C195051 | — | HDMI Type-A full-size | HDMI output [TE Connectivity] | Yes | Pending |
| Controller | J8 | 7499111121A | 1297-1070-5-ND | 710-7499111121A | C5523983 | — | RJ45 w/ magnetics/PoE long-body THT | Ethernet + PoE port [Würth Elektronik] | Yes | Pending |
| Controller | J9 | F52Q-1A7H1-11015 | 609-F52Q-1A7H1-11015CT-ND | 649-F52Q-1A7H1-11015 | C3169095 | — | DSI1 15-pin 1.0mm ZIF | Display Serial Interface [Amphenol] | Yes | Pending |
| Controller | J10 | SM04B-SRSS-TB(LF)(SN) | 455-SM04B-SRSS-TBCT-ND | 306-SM04BSRSSTBLFSN | C160404 | — | 4-pin SH 1.0mm fan SMT | Fan connector [JST] | Yes | Pending |
| Controller | J11,J16 | ERF8-005-05.0-S-DV-K-TR | SAM13517CT-ND | 200-ERF8005050SDVKTR | C7273978 | — | 10-pin 2x5 0.8mm socket SMT | Link-Beta signal sockets [Samtec] | Yes | Pending |
| Controller | J12 | RS1-05-G | 2057-RS1-05-G-ND | 737-RS1-05-G | C3321119 | — | 1x5 2.54mm female socket THT | Debug header [Adam Tech] | Yes | Pending |
| Controller | J13 | RS1-10-G | 2057-RS1-10-G-ND | 737-RS1-10-G | C3320525 | — | 1x10 2.54mm female socket THT | Debug header [Adam Tech] | Yes | Pending |
| Controller | J14,J15 | 10164227-1004A1RLF | 609-10164227-1004A1RLFCT-ND | 649-101642271004RLF | C7435219 | — | CM5 SO-DIMM 100-pin 4mm | CM5 module socket [Amphenol] | Yes | Pending |
| Controller | MH1-MH4 | 9774040151R | 732-7089-1-ND | 710-9774040151R | C5182034 | — | M2.5x4.0mm SMT standoff | PCB standoffs [Würth Elektronik] | Yes | Pending |
| Controller | R1-R4 | ERJ-3EKF1002V | P10.0KHCT-ND | 667-ERJ-3EKF1002V | C191124 | — | 10kΩ 1% 0603 | Pull-up resistors [Panasonic] | Yes | Pending |
| Controller | U1 | CM5 | — | — | — | — | CM5 module SO-DIMM | Compute Module 5 [Raspberry Pi Ltd] | N/A | N/A |
| Controller | U2 | TPS2065CDBVR | 296-39353-1-ND | 595-TPS2065CDBVR | C353882 | — | USB power switch SOT-23-5 | USB port power switch [Texas Instruments] | Yes | Pending |
| Controller | U3 | AP2331W-7 | AP2331W-7DICT-ND | 621-AP2331W-7 | C460346 | — | HDMI power switch SOT-23-5 | HDMI 5V power switch [Diodes Inc] | Yes | Pending |
| Controller | U4-U6 | TPD4E05U06QDQARQ1 | 296-40696-1-ND | 595-PD4E05U06QDQARQ1 | C81353 | — | 4-ch ESD ±15kV 0.5pF U-DFN-10 | ESD protection arrays [Texas Instruments] | Yes | Pending |
| Stator | C1-C8,C14-C21 | CL05B104KB5NNNC | 1276-1009-1-ND | 187-CL05B104KB5NNNC | C1525 | — | 100nF X7R 50V 0402 | Bypass decoupling [Samsung] | Yes | Pending |
| Stator | C9-C13,C22-C26 | CL21B106KAYQNNE | 1276-CL21B106KAYQNNECT-ND | 187-CL21B106KAYQNNE | C3039694 | — | 10µF X7R 25V 0805 | Bulk decoupling [Samsung] | Yes | Pending |
| Stator | J1,J2 | ERF8-005-05.0-S-DV-K-TR | SAM13517CT-ND | 200-ERF8005050SDVKTR | C7273978 | — | 10-pin 2x5 0.8mm female SMT | Link-Beta signal sockets [Samtec] | Yes | Pending |
| Stator | J3 | ERF8-010-05.0-S-DV-K-TR | SAM8618CT-ND | 200-ERF8010050SDVKTR | C3646170 | — | 20-pin 2x10 0.8mm female SMT | Link-Beta power socket [Samtec] | Yes | Pending |
| Stator | J4-J10 | BHR-20-VUA | 2057-BHR-20-VUA-ND | 737-BHR-20-VUA | C17340054 | — | 20-pin 2x10 2.54mm shrouded THT | Rotor slot headers [Adam Tech] | Yes | Pending |
| Stator | J11,J12 | 2195620015 | 900-2195620015-ND | 538-219562-0015 | — | Global sourcing | 5-pwr+15-sig hybrid plug hybrid | Link-Beta hybrid plugs [Molex] | Yes | Pending |
| Stator | J13 | B6B-PH-K-S(LF)(SN) | 455-1708-ND | 306-B6B-PH-K-SLFSN | C131342 | — | 6-pin JST PH 2.0mm THT | Auxiliary connector [JST] | Yes | Pending |
| Stator | L1-L4 | HI1206P121R-10 | 240-2410-1-ND | 875-HI1206P121R-10 | C2442103 | — | 120Ω @100MHz 4.0A 1206 | Ferrite beads [Laird Performance Materials] | Yes | Pending |
| Stator | R1 | CSS2H-2512R-R010ELF | CSS2H-2512R-R010ELF-ND | 652-CSS2H-2512R-R010ELF | — | — | 10mΩ ±1% 5A 2512 Kelvin shunt | Current sense shunt — no JLCPCB stock [Bourns] | Yes | Pending |
| Stator | R2-R6,R16-R21,R25-R27,R33-R41 | ERJ-2RKF1002X | P10.0KLCT-ND | 667-ERJ-2RKF1002X | C191123 | — | 10kΩ 1% 0402 | Pull-up/down resistors [Panasonic] | Yes | Pending |
| Stator | R7-R12,R27-R32,R33-R38 | ERJ-2RKF75R0X | P75.0LCT-ND | 667-ERJ-2RKF75R0X | C413061 | — | 75Ω 1% 0402 | Signal termination resistors [Panasonic] | Yes | Pending |
| Stator | R42,R43 | ERJ-2RKF10R0X | P10.0LCT-ND | 667-ERJ-2RKF10R0X | C413044 | — | 10Ω 1% Thin-Film 0402 | Series damping resistors [Panasonic] | Yes | Pending |
| Stator | U1 | EPM570T100I5N | 544-2281-ND | 989-EPM570T100I5N | C27319 | — | MAX II 570 LEs CPLD TQFP-100 | Routing CPLD [Intel (Altera)] | Yes | Pending |
| Stator | U2 | INA219AIDR | 296-23978-1-ND | 595-INA219AIDR | C138706 | — | Current monitor I²C 0x45 SOIC-8 | Current/power monitor [Texas Instruments] | Yes | Pending |
| Stator | U3 | SN74LVC1G08DBVR | 296-11601-1-ND | 595-SN74LVC1G08DBVR | C7666 | — | Single AND gate SOT-23-5 | Logic gate [Texas Instruments] | Yes | Pending |
| Stator | U4,U5 | 74HC157PW-Q100,118 | 1727-74HC157PW-Q100,118CT-ND | 771-74HC157PWQ100118 | C546614 | — | Quad 2-to-1 mux TSSOP-16 | Signal multiplexer [Nexperia] | Yes | Pending |
| Stator | U6-U8 | MCP23017T-E/SO | MCP23017T-E/SOCT-ND | 579-MCP23017T-E/SO | C47023 | — | I²C GPIO expander SOIC-28 | GPIO expanders (0x20/0x21/0x22) [Microchip Technology] | Yes | Pending |
| Rotor (Board A) | C1-C8,C14,C16 | CL05B104KB5NNNC | 1276-1009-1-ND | 187-CL05B104KB5NNNC | C1525 | — | 100nF X7R 50V 0402 | Bypass decoupling [Samsung] | Yes | Pending |
| Rotor (Board A) | C9-C13 | CL21B106KAYQNNE | 1276-CL21B106KAYQNNECT-ND | 187-CL21B106KAYQNNE | C3039694 | — | 10µF X7R 25V 0805 | Bulk decoupling [Samsung] | Yes | Pending |
| Rotor (Board A) | C15,C17 | KAM05CR71A105KH | 478-KAM05CR71A105KHCT-ND | 581-KAM05CR71A105KH | — | Global sourcing | 1µF X7R ±10% 10V AEC-Q200 0402 | Decoupling (AEC-Q200) [Kyocera AVX] | Yes | Pending |
| Rotor (Board A) | C20-C27 | AC0402FRNPO9BN330 | 13-AC0402FRNPO9BN330CT-ND | 603-0402FRNPO9BN330 | C1852937 | — | 33pF C0G/NP0 ±1% 50V AEC-Q200 0402 | Capacitive sensor circuit caps [YAGEO] | Yes | Pending |
| Rotor (Board A) | J1,J2 | ERM8-005-05.0-S-DV-K-TR | 612-ERM8-005-05.0-S-DV-K-TRCT-ND | 200-ERM8005050SDVKTR | C3649741 | — | 10-pin 2x5 0.8mm male SMT | Input dock connectors [Samtec] | Yes | Pending |
| Rotor (Board A) | J3 | ERM8-010-05.0-S-DV-K-TR | SAM8610CT-ND | 200-ERM8010050SDVKTR | C374877 | — | 20-pin 2x10 0.8mm male SMT | Input dock connector (power/JTAG) [Samtec] | Yes | Pending |
| Rotor (Board A) | H_SW3 | PH1-07-UA | 2057-PH1-07-UA-ND | 737-PH1-07-UA | C3331618 | — | 1x7 2.54mm male THT | DIP switch header (Board A side) [Adam Tech] | Yes | Pending |
| Rotor (Board A) | H_PWR,H_JTAG | RS1-05-G | 2057-RS1-05-G-ND | 737-RS1-05-G | C3321119 | — | 1x5 2.54mm female THT | Power/JTAG inter-board headers [Adam Tech] | Yes | Pending |
| Rotor (Board A) | H_SENS | PH1-05-UA | 2057-PH1-05-UA-ND | 737-PH1-05-UA | C5374051 | — | 1x5 2.54mm male THT | Sensor inter-board header [Adam Tech] | Yes | Pending |
| Rotor (Board A) | L1-L8 | CWF1610A-180K | 118-CWF1610A-180KCT-ND | 652-CWF1610A-180K | — | Global sourcing | 18µH ±10% SRF 28MHz 0603 | Capacitive sensor inductors [Bourns] | Yes | Pending |
| Rotor (Board A) | R2-R5 | ERJ-2RKF1002X | P10.0KLCT-ND | 667-ERJ-2RKF1002X | C191123 | — | 10kΩ 1% 0402 | Pull-up/down resistors [Panasonic] | Yes | Pending |
| Rotor (Board A) | R6,R7 | SG73S1ERTTP4701F | 2019-SG73S1ERTTP4701FTR-ND | 660-SG73S1ERTTP4701F | C6483673 | — | 4.7kΩ ±1% AEC-Q200 0402 | Sensor bias resistors [KOA Speer] | Yes | Pending |
| Rotor (Board A) | SW1,SW2 | 219-6LPSTR | 119-219-6LPSTRCT-ND | 774-2196LPSTR | C2842671 | — | 6-pos DIP switch 2.54mm THT | Rotor address DIP switches [CTS] | Yes | Pending |
| Rotor (Board A) | U1 | EPM570T100I5N | 544-2281-ND | 989-EPM570T100I5N | C27319 | — | MAX II 570 LEs CPLD TQFP-100 | Rotor logic CPLD [Intel (Altera)] | Yes | Pending |
| Rotor (Board A) | U2 | FDC2114RGHR | FDC2114RGHR-ND | 595-FDC2114RGHR | C2652079 | — | 4-ch cap sensor I²C 0x2A 16-VQFN | Capacitive sensor IC (MOQ 4500 at distributors; JLCPCB MOQ 2) [Texas Instruments] | Yes | Pending |
| Rotor (Board A) | U3 (N=26 only) | FDC2114RGHR | FDC2114RGHR-ND | 595-FDC2114RGHR | C2652079 | — | 4-ch cap sensor I²C 0x2B 16-VQFN | Capacitive sensor IC — N=26 variant only (MOQ 4500 at distributors; JLCPCB MOQ 2) [Texas Instruments] | Yes | Pending |
| Rotor (Board A) | U5-U8 | TPD4E05U06QDQARQ1 | 296-40696-1-ND | 595-PD4E05U06QDQARQ1 | C81353 | — | 4-ch ESD ±15kV USON-10 | ESD protection arrays [Texas Instruments] | Yes | Pending |
| Rotor (Board B) | C18 | CL05B104KB5NNNC | 1276-1009-1-ND | 187-CL05B104KB5NNNC | C1525 | — | 100nF X7R 50V 0402 | Bypass decoupling (N=64 only) [Samsung] | Yes | Pending |
| Rotor (Board B) | C19 | KAM05CR71A105KH | 478-KAM05CR71A105KHCT-ND | 581-KAM05CR71A105KH | — | Global sourcing | 1µF X7R ±10% 10V 0402 | Decoupling (N=64 only) [Kyocera AVX] | Yes | Pending |
| Rotor (Board B) | C28-C31 | AC0402FRNPO9BN330 | 13-AC0402FRNPO9BN330CT-ND | 603-0402FRNPO9BN330 | C1852937 | — | 33pF C0G NP0 0402 | Capacitive sensor caps (N=64 only) [YAGEO] | Yes | Pending |
| Rotor (Board B) | L9-L12 | CWF1610A-180K | 118-CWF1610A-180KCT-ND | 652-CWF1610A-180K | — | Global sourcing | 18µH ±10% 0603 | Capacitive sensor inductors (N=64 only) [Bourns] | Yes | Pending |
| Rotor (Board B) | J4,J5 | ERF8-005-05.0-S-DV-K-TR | SAM13517CT-ND | 200-ERF8005050SDVKTR | C7273978 | — | 10-pin 2x5 0.8mm female SMT | Output dock connectors [Samtec] | Yes | Pending |
| Rotor (Board B) | J6 | ERF8-010-05.0-S-DV-K-TR | SAM8618CT-ND | 200-ERF8010050SDVKTR | C3646170 | — | 20-pin 2x10 0.8mm female SMT | Output dock connector (power/JTAG) [Samtec] | Yes | Pending |
| Rotor (Board B) | H_SW3 | RS1-07-G | 2057-RS1-07-G-ND | 737-RS1-07-G | C3321543 | — | 1x7 2.54mm female socket THT | DIP switch header (Board B side — mates with Board A PH1-07-UA) [Adam Tech] | Yes | Pending |
| Rotor (Board B) | H_PWR,H_JTAG | PH1-05-UA | 2057-PH1-05-UA-ND | 737-PH1-05-UA | C5374051 | — | 1x5 2.54mm male THT | Power/JTAG inter-board headers [Adam Tech] | Yes | Pending |
| Rotor (Board B) | H_SENS | RS1-05-G | 2057-RS1-05-G-ND | 737-RS1-05-G | C3321119 | — | 1x5 2.54mm female THT | Sensor inter-board header [Adam Tech] | Yes | Pending |
| Rotor (Board B) | SW3 | 219-6LPSTR | 119-219-6LPSTRCT-ND | 774-2196LPSTR | C2842671 | — | 6-pos DIP switch 2.54mm THT | Rotor address DIP switch [CTS] | Yes | Pending |
| Rotor (Board B) | U4 (N=64 only) | FDC2114RGHR | FDC2114RGHR-ND | 595-FDC2114RGHR | C2652079 | — | 4-ch cap sensor I²C 0x2B 16-VQFN | Capacitive sensor IC — N=64 variant only (MOQ 4500 at distributors; JLCPCB MOQ 2) [Texas Instruments] | Yes | Pending |
| Rotor (Board B) | U9-U12 | TPD4E05U06QDQARQ1 | 296-40696-1-ND | 595-PD4E05U06QDQARQ1 | C81353 | — | 4-ch ESD ±15kV USON-10 | ESD protection arrays [Texas Instruments] | Yes | Pending |
| Settings Board | C1-C3 | CL05B104KB5NNNC | 1276-1009-1-ND | 187-CL05B104KB5NNNC | C1525 | — | 100nF X7R 50V 0402 | Bypass decoupling [Samsung] | Yes | Pending |
| Settings Board | C4 | CL05B104KB5NNNC | 1276-1009-1-ND | 187-CL05B104KB5NNNC | C960916 | — | 100nF X7R 50V 0402 | Debounce cap (different qualified JLCPCB source C960916) [Samsung] | Yes | Pending |
| Settings Board | C5,C6 | CL21B106KAYQNNE | 1276-CL21B106KAYQNNECT-ND | 187-CL21B106KAYQNNE | C3039694 | — | 10µF 25V X5R 0805 | Bulk decoupling [Samsung] | Yes | Pending |
| Settings Board | D1-D12 | WP154A4SEJ3VBDZGW/CA | 754-2029-ND | 604-WP154A43VBDZGWCA | C7151795 | — | 5mm common-anode RGB THT | RGB LED indicators [Kingbright] | Yes | Pending |
| Settings Board | J1 | B6B-PH-K-S(LF)(SN) | 455-1708-ND | 306-B6B-PH-K-SLFSN | C131342 | — | 6-pin JST PH 2.0mm THT | I2C/power connector [JST] | Yes | Pending |
| Settings Board | Q1-Q18 | BSS138 | BSS138CT-ND | 512-BSS138 | C52895 | — | N-MOSFET 50V 200mA SOT-23 | Low-side LED drive transistors [onsemi] | Yes | Pending |
| Settings Board | Q19-Q30 | SQ2319ADS-T1_BE3 | 742-SQ2319ADS-T1_BE3CT-ND | 78-SQ2319ADS-T1_BE3 | C3280190 | — | P-MOSFET AEC-Q101 SOT-23 | High-side LED drive transistors [Vishay] | Yes | Pending |
| Settings Board | R1-R11 | ERJ-3EKF1002V | P10.0KHCT-ND | 667-ERJ-3EKF1002V | C191124 | — | 10kΩ 1% 0603 | Pull-up/down resistors [Panasonic] | Yes | Pending |
| Settings Board | R12-R17,R54-R65 | ERJ-2RKF1001X | P1.00KLCT-ND | 667-ERJ-2RKF1001X | C242161 | — | 1kΩ 1% 0402 | Gate/current limit resistors [Panasonic] | Yes | Pending |
| Settings Board | R18-R29 | ERJ-3EKF1500V | P150HCT-ND | 667-ERJ-3EKF1500V | C400650 | — | 150Ω 1% 0603 | LED current limit resistors [Panasonic] | Yes | Pending |
| Settings Board | R30-R53 | ERJ-3EKF1000V | P100HCT-ND | 667-ERJ-3EKF1000V | C193336 | — | 100Ω 1% 0603 | LED series resistors [Panasonic] | Yes | Pending |
| Settings Board | R66-R77 | SG73S1ERTTP4702D | 2019-SG73S1ERTTP4702DTR-ND | 660-SG73S1ERTTP4702D | C5915648 | — | 47kΩ ±0.5% AEC-Q200 0402 | Bias resistors (JLCPCB MOQ 40) [KOA Speer] | Yes | Pending |
| Settings Board | R78-R80 | ERJ-2RKF1002X | P10.0KLCT-ND | 667-ERJ-2RKF1002X | C191123 | — | 10kΩ 1% 0402 | MCP23017 ~RESET pull-ups [Panasonic] | Yes | Pending |
| Settings Board | R81-R98 | ERJ-2RKF1003X | P100KLCT-ND | 667-ERJ-2RKF1003X | — | Global sourcing | 100kΩ 1% 0402 | Pull-up/down resistors (no JLCPCB stock) [Panasonic] | Yes | Pending |
| Settings Board | SW1-SW10 | 200MSP1T2B4M2QE | EG5525-ND | 612-200MSP1T2B4M2QE | C5491263 | — | SPDT latching toggle panel-mount THT | Enigma rotary setting switches [E-Switch] | Yes | Pending |
| Settings Board | SW11 | B3F-1070 | SW406-ND | 653-B3F-1070 | C726011 | — | SPST NO tactile THT | Tactile pushbutton [Omron] | Yes | Pending |
| Settings Board | U1-U3 | MCP23017T-E/SO | MCP23017T-E/SOCT-ND | 579-MCP23017T-E/SO | C47023 | — | I²C GPIO expander SOIC-28 | GPIO expanders (0x23/0x24/0x25) [Microchip Technology] | Yes | Pending |
| Extension | C1-C5 | CL21B106KAYQNNE | 1276-CL21B106KAYQNNECT-ND | 187-CL21B106KAYQNNE | C3039694 | — | 10µF X7R 25V 0805 | Bulk decoupling [Samsung] | Yes | Pending |
| Extension | C6 | CL05B104KB5NNNC | 1276-1009-1-ND | 187-CL05B104KB5NNNC | C1525 | — | 100nF X7R 50V 0402 | U1 bypass [Samsung] | Yes | Pending |
| Extension | C7-C11 | CL21B106KAYQNNE | 1276-CL21B106KAYQNNECT-ND | 187-CL21B106KAYQNNE | C3039694 | — | 10µF X7R 25V 0805 | 5V_MAIN decoupling [Samsung] | Yes | Pending |
| Extension | J1,J2 | ERM8-005-05.0-S-DV-K-TR | 612-ERM8-005-05.0-S-DV-K-TRCT-ND | 200-ERM8005050SDVKTR | C3649741 | — | 10-pin 2x5 0.8mm male SMT | Input dock connectors [Samtec] | Yes | Pending |
| Extension | J3 | ERM8-010-05.0-S-DV-K-TR | SAM8610CT-ND | 200-ERM8010050SDVKTR | C374877 | — | 20-pin 2x10 0.8mm male SMT | Input dock connector (power/JTAG) [Samtec] | Yes | Pending |
| Extension | J4,J5 | ERF8-005-05.0-S-DV-K-TR | SAM13517CT-ND | 200-ERF8005050SDVKTR | C7273978 | — | 10-pin 2x5 0.8mm female SMT | Output dock connectors [Samtec] | Yes | Pending |
| Extension | J6 | ERF8-010-05.0-S-DV-K-TR | SAM8618CT-ND | 200-ERF8010050SDVKTR | C3646170 | — | 20-pin 2x10 0.8mm female SMT | Output dock connector (power/JTAG) [Samtec] | Yes | Pending |
| Extension | J7,J8 | BHR-20-VUA | 2057-BHR-20-VUA-ND | 737-BHR-20-VUA | C17340054 | — | 20-pin 2x10 2.54mm shrouded box THT | Rotor group JTAG headers [Adam Tech] | Yes | Pending |
| Extension | J9,J10 | ERF8-005-05.0-S-DV-K-TR | SAM13517CT-ND | 200-ERF8005050SDVKTR | C7273978 | — | 10-pin 2x5 0.8mm female SMT | Actuation Module dock connectors [Samtec] | Yes | Pending |
| Extension | U1 | SN74LVC2G125DCUR | 296-SN74LVC2G125DCURCT-ND | 595-SN74LVC2G125DCUR | C21404 | — | Dual 3-state buffer VSSOP-8 | JTAG TCK/TMS buffer [Texas Instruments] | Yes | Pending |
| Reflector | C1-C5 | CL21B106KAYQNNE | 1276-CL21B106KAYQNNECT-ND | 187-CL21B106KAYQNNE | C3039694 | — | 10µF X7R 25V 0805 | Bulk decoupling [Samsung] | Yes | Pending |
| Reflector | J1,J2 | ERM8-005-05.0-S-DV-K-TR | 612-ERM8-005-05.0-S-DV-K-TRCT-ND | 200-ERM8005050SDVKTR | C3649741 | — | 10-pin 2x5 0.8mm male SMT | Input dock connectors [Samtec] | Yes | Pending |
| Reflector | J3 | ERM8-010-05.0-S-DV-K-TR | SAM8610CT-ND | 200-ERM8010050SDVKTR | C374877 | — | 20-pin 2x10 0.8mm male SMT | Input dock connector (power/JTAG) [Samtec] | Yes | Pending |
| Reflector | J4 | BHR-20-VUA | 2057-BHR-20-VUA-ND | 737-BHR-20-VUA | C17340054 | — | 20-pin 2x10 2.54mm shrouded THT | Reflector JTAG header [Adam Tech] | Yes | Pending |
| Reflector | R1 | ERJ-3EKF2200V | P220HCT-ND | 667-ERJ-3EKF2200V | C403073 | — | 22Ω 1% 0603 | JTAG termination resistor [Panasonic] | Yes | Pending |
| Encoder | C1-C8 | CL05B104KB5NNNC | 1276-1009-1-ND | 187-CL05B104KB5NNNC | C1525 | — | 100nF X7R 50V 0402 | Bypass decoupling [Samsung] | Yes | Pending |
| Encoder | C9-C13 | CL21B106KAYQNNE | 1276-CL21B106KAYQNNECT-ND | 187-CL21B106KAYQNNE | C3039694 | — | 10µF X7R 25V 0805 | Bulk decoupling [Samsung] | Yes | Pending |
| Encoder | BT1-BT64 | 1285-ST | 36-1285-ST-ND | 534-1285-ST | C5370868 | — | 6.35mm PCB spade blade terminals THT vertical | Plugboard jack connection terminals (x64) [Keystone Electronics] | Yes | Pending |
| Encoder | D1 | 150060VS75000 | 732-4980-1-ND | 710-150060VS75000 | C6848499 | — | Green SMD LED Vf≈2.0V 0402 | Status LED [Würth Elektronik] | Yes | Pending |
| Encoder | J1 (off-board) | (no standard MPN) | — | — | — | eBay SaiBuy.Ltd | 6.35mm mono jack sockets panel-mount | Plugboard jack assembly parts — eBay sourcing only [generic] | N/A | N/A |
| Encoder | J2 | BHR-20-VUA | 2057-BHR-20-VUA-ND | 737-BHR-20-VUA | C17340054 | — | 20-pin 2x10 2.54mm shrouded THT | JTAG/data header [Adam Tech] | Yes | Pending |
| Encoder | SW1-SW40 (off-board) | (no standard MPN) | — | — | — | eBay gadgetskingdom | DPDT 6-pin momentary switches panel-mount | Keyboard assembly switches — eBay sourcing only [generic] | N/A | N/A |
| Encoder | R1 | ERJ-2RKF3300X | P330LCT-ND | 667-ERJ-2RKF3300X | C278592 | — | 330Ω 1% 0402 | LED current limit [Panasonic] | Yes | Pending |
| Encoder | R2-R5 | ERJ-2RKF1002X | P10.0KLCT-ND | 667-ERJ-2RKF1002X | C191123 | — | 10kΩ 1% 0402 | JTAG pull resistors [Panasonic] | Yes | Pending |
| Encoder | R6 | ERJ-2RKF75R0X | P75.0LCT-ND | 667-ERJ-2RKF75R0X | C413061 | — | 75Ω 1% 0402 | TDO series resistor [Panasonic] | Yes | Pending |
| Encoder | U1 | EPM570T100I5N | 544-2281-ND | 989-EPM570T100I5N | C27319 | — | MAX II 570 LEs CPLD TQFP-100 | Encoder logic CPLD [Intel (Altera)] | Yes | Pending |
| Actuation Module | C1 | C0805C105K5RACTU | 399-C0805C105K5RACTUCT-ND | 80-C0805C105K5R | C3018567 | — | 1µF X7R 50V 0805 | Debounce cap [Kemet] | Yes | Pending |
| Actuation Module | C2,C3,C6,C7 | CL05B104KB5NNNC | 1276-1009-1-ND | 187-CL05B104KB5NNNC | C1525 | — | 100nF X7R 50V 0402 | Bypass decoupling [Samsung] | Yes | Pending |
| Actuation Module | C4 | CGA6P3X7R1H475K250AD | 445-10040-1-ND | 810-CGA6P3X7R1H475KD | C3877549 | — | 4.7µF X7R 3V3 1210 | 3V3 reservoir cap [TDK] | Yes | Pending |
| Actuation Module | C5 | CL21B106KAYQNNE | 1276-CL21B106KAYQNNECT-ND | 187-CL21B106KAYQNNE | C3039694 | — | 10µF X7R 25V 0805 | 5V_MAIN reservoir [Samsung] | Yes | Pending |
| Actuation Module | D1-D3 | 150060VS75000 | 732-4980-1-ND | 710-150060VS75000 | C6848499 | — | Green SMD LED diagnostic 0402 | Diagnostic LEDs [Würth Elektronik] | Yes | Pending |
| Actuation Module | J1 | ERM8-005-05.0-S-DV-K-TR | 612-ERM8-005-05.0-S-DV-K-TRCT-ND | 200-ERM8005050SDVKTR | C3649741 | — | Power dock male 2x5 0.8mm SMT | Power dock connector [Samtec] | Yes | Pending |
| Actuation Module | J2 | ERM8-005-05.0-S-DV-K-TR | 612-ERM8-005-05.0-S-DV-K-TRCT-ND | 200-ERM8005050SDVKTR | C3649741 | — | Trigger dock male 2x5 0.8mm SMT | Trigger dock connector [Samtec] | Yes | Pending |
| Actuation Module | J3-J6 | PH1-05-UA | 2057-PH1-05-UA-ND | 737-PH1-05-UA | C5374051 | — | 1x5 2.54mm male THT | Manual-fit output headers [Adam Tech] | Yes | Pending |
| Actuation Module | R1-R3 | ERJ-2RKF3300X | P330LCT-ND | 667-ERJ-2RKF3300X | C278592 | — | 330Ω 1% 0402 | LED current limit [Panasonic] | Yes | Pending |
| Actuation Module | R4-R6 | ERJ-2RKF1002X | P10.0KLCT-ND | 667-ERJ-2RKF1002X | C191123 | — | 10kΩ 1% 0402 | Pull-up/protection resistors [Panasonic] | Yes | Pending |
| Actuation Module | SW1,SW2 | B3F-1070 | SW406-ND | 653-B3F-1070 | C726011 | — | SPST NO tactile THT | NRST/BOOT0 pushbuttons [Omron] | Yes | Pending |
| Actuation Module | U1 | STM32G071K8T3TR | 497-STM32G071K8T3TR-ND | 511-STM32G071K8T3TR | — | Global sourcing | Local actuation controller LQFP32 | STM32G071 MCU — JLCPCB consignment only [STMicroelectronics] | Yes | Pending |
| JTAG Daughterboard | C1-C4,C6-C9 | CL05B104KB5NNNC | 1276-1009-1-ND | 187-CL05B104KB5NNNC | C1525 | — | 100nF X7R 50V 0402 | FT232H per-pin bypass [Samsung] | Yes | Pending |
| JTAG Daughterboard | C5 | CGA6P3X7R1H475K250AD | 445-10040-1-ND | 810-CGA6P3X7R1H475KD | C3877549 | — | 4.7µF X7R 1210 | 5V_USB entry filter [TDK] | Yes | Pending |
| JTAG Daughterboard | C10,C11 | C0402C330J5GAUTO | 399-12979-1-ND | 80-C0402C330J5GAUTO | C2169327 | — | 33pF C0G/NP0 crystal load 0402 | Crystal load caps — only C0G in system [Kemet] | Yes | Pending |
| JTAG Daughterboard | J1 | PH1-05-UA | 2057-PH1-05-UA-ND | 737-PH1-05-UA | C5374051 | — | 1x5 2.54mm male INPUT header THT | Input header [Adam Tech] | Yes | Pending |
| JTAG Daughterboard | J2 | PH1-10-UA | 2057-PH1-10-UA-ND | 737-PH1-10-UA | C3330527 | — | 1x10 2.54mm male JTAG OUTPUT header THT | JTAG output header [Adam Tech] | Yes | Pending |
| JTAG Daughterboard | R2,R3 | ERJ-2RKF33R0X | P33.0LCT-ND | 667-ERJ-2RKF33R0X | C278594 | — | 33Ω 1% 0402 | TDI series damping [Panasonic] | Yes | Pending |
| JTAG Daughterboard | R3-R5 | ERJ-2RKF1002X | P10.0KLCT-ND | 667-ERJ-2RKF1002X | C191123 | — | 10kΩ 1% 0402 | RESET/TMS/TCK pull resistors [Panasonic] | Yes | Pending |
| JTAG Daughterboard | R6-R8 | ERJ-2RKF33R0X | P33.0LCT-ND | 667-ERJ-2RKF33R0X | C278594 | — | 33Ω 1% 0402 | TCK/TMS/TDI series damping [Panasonic] | Yes | Pending |
| JTAG Daughterboard | U1 | FT232HL-REEL | 768-1101-1-ND | 895-FT232HL-REEL | C51997 | — | USB 2.0 to MPSSE bridge LQFP-48 | USB-JTAG bridge IC [FTDI Chip] | Yes | Pending |
| JTAG Daughterboard | U5 | SN74LVC2G125DCUR | 296-SN74LVC2G125DCURCT-ND | 595-SN74LVC2G125DCUR | C21404 | — | Dual 3-state buffer VSSOP-8 | JTAG TCK/TMS buffer [Texas Instruments] | Yes | Pending |
| JTAG Daughterboard | Y1 | ABM8-12-B2-T | 535-9826-1-ND | 815-ABM8-12-B2-T | C596894 | — | 12MHz 20pF ±20ppm crystal SMD3225-4P | FT232H clock crystal [Abracon] | Yes | Pending |

---

## Section 2 — MPN Quantity Summary

Per-Unit Total = one instance of every board type. Actual system totals depend on configuration (up to 30x Rotor pairs; 6x Encoder boards; all other boards x1).

| # | MPN | Manufacturer | PM | CTL | STA | ROT-A | ROT-B | SBD | EXT | REF | ENC | AM | JDB | Per-Unit Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | CL32B226KAJNNNE | Samsung | 15 | — | — | — | — | — | — | — | — | — | — | 15 |
| 2 | CGA9N3X7R1E476M230KB | TDK | 4 | — | — | — | — | — | — | — | — | — | — | 4 |
| 3 | CL21B106KAYQNNE | Samsung | 1 | 10 | 10 | 5 | — | 2 | 10 | 5 | 5 | 1 | — | 49 |
| 4 | C0805C105K5RACTU | Kemet | 7 | — | — | — | — | — | — | — | — | 1 | — | 8 |
| 5 | CL05B104KB5NNNC | Samsung | 26 | 3 | 16 | 10 | 1 | 4 | 1 | — | 8 | 4 | 8 | 81 |
| 6 | C0402C101K3RACAUTO | Kemet | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 7 | ADCR-T02R7SA256MB | Abracon | 8 | — | — | — | — | — | — | — | — | — | — | 8 |
| 8 | CL10B223KB8WPNC | Samsung | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 9 | CC1206KKX7R8BB106 | YAGEO | 2 | — | — | — | — | — | — | — | — | — | — | 2 |
| 10 | CL05B103KB5NNNC | Samsung | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 11 | TPD1E10B06DYARQ1 | Texas Instruments | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 12 | TPD2E2U06DRLR | Texas Instruments | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 13 | TPD4E05U06QDQARQ1 | Texas Instruments | 1 | 3 | — | 4 | 4 | — | — | — | — | — | — | 12 |
| 14 | BAT54 | Vishay | 2 | 1 | — | — | — | — | — | — | — | — | — | 3 |
| 15 | AC72ABD | Bourns | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 16 | 1123684-7 | TE Connectivity | 3 | — | — | — | — | — | — | — | — | — | — | 3 |
| 17 | 0436500519 | Molex | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 18 | USB4135-GF-A | GCT | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 19 | 7448031002 | Würth Elektronik | 2 | — | — | — | — | — | — | — | — | — | — | 2 |
| 20 | SRP1265A-100M | Bourns | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 21 | CSD17578Q5A | Texas Instruments | 3 | — | — | — | — | — | — | — | — | — | — | 3 |
| 22 | BSS138 | onsemi | 7 | — | — | — | — | 18 | — | — | — | — | — | 25 |
| 23 | ERJ-3EKF2323V | Panasonic | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 24 | ERJ-3EKF2872V | Panasonic | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 25 | ERA-3VEB2100V | Panasonic | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 26 | ERJ-3EKF1002V | Panasonic | 6 | 4 | — | — | — | 11 | — | — | — | — | — | 21 |
| 27 | ERJ-3EKF4701V | Panasonic | 2 | — | — | — | — | — | — | — | — | — | — | 2 |
| 28 | ERJ-3EKF3010V | Panasonic | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 29 | CSS2H-2512R-R010ELF | Bourns | 2 | — | 1 | — | — | — | — | — | — | — | — | 3 |
| 30 | ERA-3ARB3012V | Panasonic | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 31 | ERA-3ARB103V | Panasonic | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 32 | ERJ-3EKF7153V | Panasonic | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 33 | ERJ-3EKF8662V | Panasonic | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 34 | ERJ-2RKF1002X | Panasonic | 9 | — | 23 | 4 | — | 3 | — | — | 4 | 3 | 3 | 49 |
| 35 | ERJ-2RKF8202X | Panasonic | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 36 | ERJ-3EKF2743V | Panasonic | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 37 | ERA-2AEB3322X | Panasonic | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 38 | ERJ-2RKF1001X | Panasonic | 5 | — | — | — | — | 18 | — | — | — | — | — | 23 |
| 39 | ERJ-2RKF5232X | Panasonic | 2 | — | — | — | — | — | — | — | — | — | — | 2 |
| 40 | ERJ-2RKF1003X | Panasonic | 4 | — | — | — | — | 18 | — | — | — | — | — | 22 |
| 41 | ERJ-2RKF10R0X | Panasonic | 5 | — | 2 | — | — | — | — | — | — | — | — | 7 |
| 42 | 4660 | Adafruit | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 43 | 3350 | Adafruit | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 44 | 1211 | Keystone Electronics | 2 | — | — | — | — | — | — | — | — | — | — | 2 |
| 45 | TPS259804ONRGER | Texas Instruments | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 46 | LMQ61460AFSQRJRRQ1 | Texas Instruments | 2 | — | — | — | — | — | — | — | — | — | — | 2 |
| 47 | LTC3350EUHF#PBF | Analog Devices | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 48 | TPS25751DREFR | Texas Instruments | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 49 | STUSB4500LQTR | STMicroelectronics | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 50 | LM74700QDBVRQ1 | Texas Instruments | 3 | — | — | — | — | — | — | — | — | — | — | 3 |
| 51 | TPS75733KTTRG3 | Texas Instruments | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 52 | MCP121T-450E/LB | Microchip Technology | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 53 | MIC1555YM5-TR | Microchip Technology | 2 | — | — | — | — | — | — | — | — | — | — | 2 |
| 54 | INA219AIDR | Texas Instruments | 1 | — | 1 | — | — | — | — | — | — | — | — | 2 |
| 55 | NL27WZ14DFT2G-Q | onsemi | 3 | — | — | — | — | — | — | — | — | — | — | 3 |
| 56 | PCA9534APWR | NXP Semiconductors | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 57 | SN74LVC1G175DBVR | Texas Instruments | 1 | — | — | — | — | — | — | — | — | — | — | 1 |
| 58 | SN74LVC1G08DBVR | Texas Instruments | 1 | — | 1 | — | — | — | — | — | — | — | — | 2 |
| 59 | C0402C103K1RACAUTO | Kemet | — | 1 | — | — | — | — | — | — | — | — | — | 1 |
| 60 | 3034TR | Keystone Electronics | — | 1 | — | — | — | — | — | — | — | — | — | 1 |
| 61 | 1-1674231-1 | TE Connectivity | — | 3 | — | — | — | — | — | — | — | — | — | 3 |
| 62 | 2195630015 | Molex | — | 2 | — | — | — | — | — | — | — | — | — | 2 |
| 63 | 48406-0003 | Molex | — | 1 | — | — | — | — | — | — | — | — | — | 1 |
| 64 | 2007435-1 | TE Connectivity | — | 1 | — | — | — | — | — | — | — | — | — | 1 |
| 65 | 7499111121A | Würth Elektronik | — | 1 | — | — | — | — | — | — | — | — | — | 1 |
| 66 | F52Q-1A7H1-11015 | Amphenol | — | 1 | — | — | — | — | — | — | — | — | — | 1 |
| 67 | SM04B-SRSS-TB(LF)(SN) | JST | — | 1 | — | — | — | — | — | — | — | — | — | 1 |
| 68 | ERF8-005-05.0-S-DV-K-TR | Samtec | — | 2 | 2 | — | 2 | — | 4 | — | — | — | — | 10 |
| 69 | RS1-05-G | Adam Tech | — | 1 | — | 2 | 1 | — | — | — | — | — | — | 4 |
| 70 | RS1-10-G | Adam Tech | — | 1 | — | — | — | — | — | — | — | — | — | 1 |
| 71 | 10164227-1004A1RLF | Amphenol | — | 2 | — | — | — | — | — | — | — | — | — | 2 |
| 72 | 9774040151R | Würth Elektronik | — | 4 | — | — | — | — | — | — | — | — | — | 4 |
| 73 | CM5 | Raspberry Pi Ltd | — | 1 | — | — | — | — | — | — | — | — | — | 1 |
| 74 | TPS2065CDBVR | Texas Instruments | — | 1 | — | — | — | — | — | — | — | — | — | 1 |
| 75 | AP2331W-7 | Diodes Inc | — | 1 | — | — | — | — | — | — | — | — | — | 1 |
| 76 | ERF8-010-05.0-S-DV-K-TR | Samtec | — | — | 1 | — | 1 | — | 1 | — | — | — | — | 3 |
| 77 | BHR-20-VUA | Adam Tech | — | — | 7 | — | — | — | 2 | 1 | 1 | — | — | 11 |
| 78 | 2195620015 | Molex | — | — | 2 | — | — | — | — | — | — | — | — | 2 |
| 79 | B6B-PH-K-S(LF)(SN) | JST | — | — | 1 | — | — | 1 | — | — | — | — | — | 2 |
| 80 | HI1206P121R-10 | Laird Performance Materials | — | — | 4 | — | — | — | — | — | — | — | — | 4 |
| 81 | ERJ-2RKF75R0X | Panasonic | — | — | 18 | — | — | — | — | — | 1 | — | — | 19 |
| 82 | EPM570T100I5N | Intel (Altera) | — | — | 1 | 1 | — | — | — | — | 1 | — | — | 3 |
| 83 | 74HC157PW-Q100,118 | Nexperia | — | — | 2 | — | — | — | — | — | — | — | — | 2 |
| 84 | MCP23017T-E/SO | Microchip Technology | — | — | 3 | — | — | 3 | — | — | — | — | — | 6 |
| 85 | KAM05CR71A105KH | Kyocera AVX | — | — | — | 2 | 1 | — | — | — | — | — | — | 3 |
| 86 | AC0402FRNPO9BN330 | YAGEO | — | — | — | 8 | 4 | — | — | — | — | — | — | 12 |
| 87 | ERM8-005-05.0-S-DV-K-TR | Samtec | — | — | — | 2 | — | — | 2 | 2 | — | 2 | — | 8 |
| 88 | ERM8-010-05.0-S-DV-K-TR | Samtec | — | — | — | 1 | — | — | 1 | 1 | — | — | — | 3 |
| 89 | PH1-07-UA | Adam Tech | — | — | — | 1 | — | — | — | — | — | — | — | 1 |
| 90 | PH1-05-UA | Adam Tech | — | — | — | 1 | 2 | — | — | — | — | 4 | 1 | 8 |
| 91 | CWF1610A-180K | Bourns | — | — | — | 8 | 4 | — | — | — | — | — | — | 12 |
| 92 | SG73S1ERTTP4701F | KOA Speer | — | — | — | 2 | — | — | — | — | — | — | — | 2 |
| 93 | 219-6LPSTR | CTS | — | — | — | 2 | 1 | — | — | — | — | — | — | 3 |
| 94 | FDC2114RGHR | Texas Instruments | — | — | — | 2 | 1 | — | — | — | — | — | — | 3 |
| 95 | RS1-07-G | Adam Tech | — | — | — | — | 1 | — | — | — | — | — | — | 1 |
| 96 | WP154A4SEJ3VBDZGW/CA | Kingbright | — | — | — | — | — | 12 | — | — | — | — | — | 12 |
| 97 | SQ2319ADS-T1_BE3 | Vishay | — | — | — | — | — | 12 | — | — | — | — | — | 12 |
| 98 | ERJ-3EKF1500V | Panasonic | — | — | — | — | — | 12 | — | — | — | — | — | 12 |
| 99 | ERJ-3EKF1000V | Panasonic | — | — | — | — | — | 24 | — | — | — | — | — | 24 |
| 100 | SG73S1ERTTP4702D | KOA Speer | — | — | — | — | — | 12 | — | — | — | — | — | 12 |
| 101 | 200MSP1T2B4M2QE | E-Switch | — | — | — | — | — | 10 | — | — | — | — | — | 10 |
| 102 | B3F-1070 | Omron | — | — | — | — | — | 1 | — | — | — | 2 | — | 3 |
| 103 | SN74LVC2G125DCUR | Texas Instruments | — | — | — | — | — | — | 1 | — | — | — | 1 | 2 |
| 104 | ERJ-3EKF2200V | Panasonic | — | — | — | — | — | — | — | 1 | — | — | — | 1 |
| 105 | 1285-ST | Keystone Electronics | — | — | — | — | — | — | — | — | 64 | — | — | 64 |
| 106 | 150060VS75000 | Würth Elektronik | — | — | — | — | — | — | — | — | 1 | 3 | — | 4 |
| 107 | (no standard MPN) | generic | — | — | — | — | — | — | — | — | 41 | — | — | 41 |
| 108 | ERJ-2RKF3300X | Panasonic | — | — | — | — | — | — | — | — | 1 | 3 | — | 4 |
| 109 | CGA6P3X7R1H475K250AD | TDK | — | — | — | — | — | — | — | — | — | 1 | 1 | 2 |
| 110 | STM32G071K8T3TR | STMicroelectronics | — | — | — | — | — | — | — | — | — | 1 | — | 1 |
| 111 | C0402C330J5GAUTO | Kemet | — | — | — | — | — | — | — | — | — | — | 2 | 2 |
| 112 | PH1-10-UA | Adam Tech | — | — | — | — | — | — | — | — | — | — | 1 | 1 |
| 113 | ERJ-2RKF33R0X | Panasonic | — | — | — | — | — | — | — | — | — | — | 5 | 5 |
| 114 | FT232HL-REEL | FTDI Chip | — | — | — | — | — | — | — | — | — | — | 1 | 1 |
| 115 | ABM8-12-B2-T | Abracon | — | — | — | — | — | — | — | — | — | — | 1 | 1 |
