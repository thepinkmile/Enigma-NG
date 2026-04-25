# TPS25980: 2.7- 24 V, 8 A, 3 mOhm Smart eFuse - Integrated Hot-swap Protection With Adjustable Transient Fault Management datasheet

## Source

- Source PDF: [TPS25980-datasheet.pdf](TPS25980-datasheet.pdf)
- Generated Markdown: `TPS25980-datasheet.md`
- Page count: 53
- Conversion method: automated local extraction with pypdf and pdfplumber

## Extracted title and part identity

- TPS25980: 2.7- 24 V, 8 A, 3 mOhm Smart eFuse - Integrated Hot-swap Protection With Adjustable Transient Fault Management datasheet
- TPS25980 datasheet
- TPS25980
- TPS259802ONRGE
- TPS259803ONRGE
- TPS259804ONRGE
- TPS259807ONRGE
- E339631

## Extraction summary

- Pages with substantial text extraction: 53/53
- Pages with extracted tables: 38/53
- Total extracted character count: 118015
- Extraction quality flag: usable

## PDF metadata

| Field | Value |
| --- | --- |
| Title | TPS25980: 2.7- 24 V, 8 A, 3 mOhm Smart eFuse - Integrated Hot-swap Protection With Adjustable Transient Fault Management datasheet |
| Author | Texas Instruments, Incorporated [SLVSFR1,*] |
| Subject | Data Sheet |
| Creator | AH XSL Formatter V7.0 MR5 for Windows (x64) : 7.0.6.47833 (2020-10-21T14:40+09) |
| Producer | iText 2.1.7 by 1T3XT |

## Design-relevant extracted content

This section surfaces design-relevant snippets first. Full page-by-page raw extraction follows later for local search.

### Part number and ordering information

- voltage surges and excessive inrush current. / Handles load transients without tripping / * Accurate current monitor output Overvoltage events are limited by internal cutoff / +/- 3% (typical at 25 deg C for I > 3 A) circuits, with multiple device options to choose the / OUT / * User configurable fault response overvoltage threshold. / Latch-off or auto-retry
- * Adjustable output slew rate (dVdt) control to function uninterrupted during line and load / * Adjustable undervoltage lockout transients without compromising on the robustness / * Overvoltage lockout (Fixed 3.7-V, 7.6-V, 16.9-V of the protection against faults. The device can be / and no-OVLO options) configured to stay latched off or retry automatically / * Integrated overtemperature protection after a fault shutdown. The number of auto-retries / * Power good indication as well as the retry delay are configurable / * Adjustable load detect and handshake timer with capacitors. This enables remote systems to
- 2 Applications are characterized for operation over a junction / temperature range of -40 deg C to 125 deg C. / * Hot-Swap, hot-plug / * Server standby rail, PCIe riser, add-on card and Device Information(1) / fan module protection / PART NUMBER PACKAGE BODY SIZE (NOM) / * Routers and switches optical module protection
- * Hot-Swap, hot-plug / * Server standby rail, PCIe riser, add-on card and Device Information(1) / fan module protection / PART NUMBER PACKAGE BODY SIZE (NOM) / * Routers and switches optical module protection / TPS25980x QFN (24) 4.0 mm x 4.0 mm / * Industrial PC
- * Routers and switches optical module protection / TPS25980x QFN (24) 4.0 mm x 4.0 mm / * Industrial PC / * Digital TV (1) For all available packages, see the orderable addendum at / the end of the data sheet. / SPuopwpelyr RVL1 E L IN D N S /U T V R T L T P O S25980 O P U G T R V P P G G / NRETRY IMON
- SPuopwpelyr RVL1 E L IN D N S /U T V R T L T P O S25980 O P U G T R V P P G G / NRETRY IMON / CIN RVL2 C*NRETRY C*R C E *L T D R S Y T _ R D T LY R IL E IM R TR ILI Y M _D G L N Y DITI d M V E d R C t *ITIME C R dVdt RIMON CL RL / * Optional components for extended functionality / Simplified Schematics / An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications, / intellectual property matters and other important disclaimers. PRODUCTION DATA.
- Simplified Schematics / An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications, / intellectual property matters and other important disclaimers. PRODUCTION DATA. / PART NUMBER | PACKAGE | BODY SIZE (NOM) / TPS25980x | QFN (24) | 4.0 mm x 4.0 mm / RVL1 RVL2 C*NRETRY C*R C E *L T D R S Y T _ R D T LY | | | LDSTRT EN/UVLO PG NRETRY IMON RETRY_DLY dVdt ILIM GNDITIMER | | VPG RPG / | C*NRETRY C*R C E *L T D R S Y T _ R D T LY | | | |
- 12.4 Trademarks.............................................................43 / 12.5 Electrostatic Discharge Caution..............................43 / 12.6 Glossary..................................................................43 / 13 Mechanical, Packaging, and Orderable / Information.................................................................... 44 / 4 Revision History / NOTE: Page numbers for previous revisions may differ from page numbers in the current version.
- DATE | REVISION | NOTES / August 2020 | * | Initial release. / 5 Device Comparison Table / PART NUMBER / OVERVOLTAGE LOCKOUT / THRESHOLD OVERCURRENT RESPONSE / TYPICAL (V)
- SLVSFR1 - AUGUST 2020 / Copyright 2022 Texas Instruments Incorporated Submit Document Feedback 3 / Product Folder Links: TPS25980 / PART NUMBER | OVERVOLTAGE LOCKOUT THRESHOLD | OVERCURRENT RESPONSE / | TYPICAL (V) | / TPS259802ONRGE | 3.7 | Circuit Breaker / TPS259803ONRGE | 7.6 | Circuit Breaker
- 0 / Time / Figure 8-2. Overvoltage Response / There are multiple device options with different fixed overvoltage thresholds to choose from, including one / without internal overvoltage protection. See the Device Comparison Table for a list of available options. / 8.3.3 Inrush Current, Overcurrent, and Short-Circuit Protection / TPS25980x devices incorporate three levels of protection against overcurrent:
- Time / Figure 8-2. Overvoltage Response / There are multiple device options with different fixed overvoltage thresholds to choose from, including one / without internal overvoltage protection. See the Device Comparison Table for a list of available options. / 8.3.3 Inrush Current, Overcurrent, and Short-Circuit Protection / TPS25980x devices incorporate three levels of protection against overcurrent: / * Adjustable slew rate (dVdt) for inrush current control
- 9.1 Application Information / The TPS25980x device is an integrated 8-A eFuse that is typically used for hot-swap and power rail protection / applications. It operates from 2.7 V to 24 V with adjustable overcurrent and undervoltage protection. It also / provides optional overvoltage with various fixed internal thresholds. The device aids in controlling the inrush / current and has the flexibility to configure the number of auto-retries and retry delay. The adjustable overcurrent / blanking timer provides the functionality to allow transient overcurrent pulses without limiting or tripping. These / devices protect source, load and internal MOSFET from potentially damaging events in systems such as PCIe
- This design example considers a 12-V system operating voltage with a tolerance of +/-10 %. The rated load / current is 6.5 A. If the current exceeds 8 A, then the device must allow overload current for 2-ms interval / before breaking the circuit and then restart. Accordingly, the TPS259804O variant is chosen. (Refer to Device / Comparison Table for device options.) Ambient temperatures may range from 20 deg C to 70 deg C. The load has a / minimum input capacitance of 1.4 mF and start-up resistive load of 10 Ohm. The downstream load is turned on only / after the PG signal is asserted. / 9.2.2.2 Setting the Current Limit Threshold: R Selection
- * LIN equals the effective inductance seen looking into the source / * CIN is the capacitance present at the input / Some of the applications may require the addition of a Transient Voltage Suppressor (TVS) to prevent transients / from exceeding the absolute maximum ratings of the device. A typical circuit implementation with optional / protection components (a ceramic capacitor, TVS and Schottky diode) is shown in Figure 10-1. / IN / EN/UVLO
- 12V / 100O1MO / 137kO / Figure 10-1. Typical Circuit Implementation With Optional Protection Components / www.ti.com / TPS25980 / SLVSFR1 - AUGUST 2020
- * / * / * / * Optional components for suppressing transients induced while / switching current through inductive elements at input/output / > 50 mils / Figure 11-1. TPS25980 Example PCB Layout
- TPS259803O | Click here | Click here | Click here | Click here | Click here / TPS259804O | Click here | Click here | Click here | Click here | Click here / TPS259807O | Click here | Click here | Click here | Click here | Click here / 13 Mechanical, Packaging, and Orderable Information / The following pages include mechanical, packaging, and orderable information. This information is the most / current data available for the designated devices. This data is subject to change without notice and revision of / this document. For browser-based versions of this data sheet, refer to the left-hand navigation.

### Pin, pad, and terminal designations

- LIM / * Adjustable over-current blanking timer are a robust defense against overloads, short-circuits, / voltage surges and excessive inrush current. / Handles load transients without tripping / * Accurate current monitor output Overvoltage events are limited by internal cutoff / +/- 3% (typical at 25 deg C for I > 3 A) circuits, with multiple device options to choose the / OUT
- threshold can be set with a single external resistor. / Fast-trip response time < 400-ns typical The devices intelligently manage the overcurrent / Tested against 1 million power-into-short events response by distinguishing between transient events / Immune to line transients - no nuisance tripping and actual faults, thereby allowing the system / * Adjustable output slew rate (dVdt) control to function uninterrupted during line and load / * Adjustable undervoltage lockout transients without compromising on the robustness / * Overvoltage lockout (Fixed 3.7-V, 7.6-V, 16.9-V of the protection against faults. The device can be
- Fast-trip response time < 400-ns typical The devices intelligently manage the overcurrent / Tested against 1 million power-into-short events response by distinguishing between transient events / Immune to line transients - no nuisance tripping and actual faults, thereby allowing the system / * Adjustable output slew rate (dVdt) control to function uninterrupted during line and load / * Adjustable undervoltage lockout transients without compromising on the robustness / * Overvoltage lockout (Fixed 3.7-V, 7.6-V, 16.9-V of the protection against faults. The device can be / and no-OVLO options) configured to stay latched off or retry automatically
- SPuopwpelyr RVL1 E L IN D N S /U T V R T L T P O S25980 O P U G T R V P P G G / NRETRY IMON / CIN RVL2 C*NRETRY C*R C E *L T D R S Y T _ R D T LY R IL E IM R TR ILI Y M _D G L N Y DITI d M V E d R C t *ITIME C R dVdt RIMON CL RL / * Optional components for extended functionality / Simplified Schematics / An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications, / intellectual property matters and other important disclaimers. PRODUCTION DATA.
- 3 Description.......................................................................1 / 4 Revision History.............................................................. 2 / 5 Device Comparison Table...............................................3 / 6 Pin Configuration and Functions...................................4 / 7 Specifications.................................................................. 6 / 7.1 Absolute Maximum Ratings........................................ 6 / 7.2 ESD Ratings............................................................... 6
- 7.8 Typical Characteristics.............................................. 11 / 8 Detailed Description......................................................16 / 8.1 Overview...................................................................16 / 8.2 Functional Block Diagram.........................................16 / 8.3 Feature Description...................................................16 / 8.4 Fault Response.........................................................24 / 8.5 Device Functional Modes..........................................27
- 8.2 Functional Block Diagram.........................................16 / 8.3 Feature Description...................................................16 / 8.4 Fault Response.........................................................24 / 8.5 Device Functional Modes..........................................27 / 9 Application and Implementation..................................28 / 9.1 Application Information............................................. 28 / 9.2 Typical Application: Patient Monitoring System in
- TPS259803ONRGE | 7.6 | Circuit Breaker / TPS259804ONRGE | 16.9 | Circuit Breaker / TPS259807ONRGE | No OVLO | Circuit Breaker / 6 Pin Configuration and Functions / IN / IN / IN
- OUT OUT OUT OUT OUT / 1 18 / 2 IN 17 / Thermal Pad 1 / 3 16 / 4 15 / 5 14
- 4 15 / 5 14 / GND / Thermal Pad 2 / 6 13 / 7 8 9 0 1 1 1 2 1 / 24 23 22 21 20 19
- 24 23 22 21 20 19 / TPS25980 / SLVSFR1 - AUGUST 2020 www.ti.com / Figure 6-1. RGE 24-Pin QFN Top View / Pin Functions / PIN / TYPE DESCRIPTION
- TPS25980 / SLVSFR1 - AUGUST 2020 www.ti.com / Figure 6-1. RGE 24-Pin QFN Top View / Pin Functions / PIN / TYPE DESCRIPTION / NAME NO.
- SLVSFR1 - AUGUST 2020 www.ti.com / Figure 6-1. RGE 24-Pin QFN Top View / Pin Functions / PIN / TYPE DESCRIPTION / NAME NO. / 17, 18, 19,
- 17, 18, 19, / OUT 20, 21, 22, Power Power Output. / 23, 24 / 1, 2, 3, 16, Thermal / Power Input. The exposed pad must be soldered to input power plane uniformly to ensure / IN / Pad 1 Power proper heat dissipation and to maintain optimal current distribution through the device. / 4, 5, 14,
- 23, 24 / 1, 2, 3, 16, Thermal / Power Input. The exposed pad must be soldered to input power plane uniformly to ensure / IN / Pad 1 Power proper heat dissipation and to maintain optimal current distribution through the device. / 4, 5, 14, / GND Ground Connect to System Ground. / Pad 2
- Pad 1 Power proper heat dissipation and to maintain optimal current distribution through the device. / 4, 5, 14, / GND Ground Connect to System Ground. / Pad 2 / Active High Enable for the device. A resistor divider on this pin from input supply to GND can / EN/UVLO 6 Analog Input / be used to adjust the Undervoltage Lockout threshold. Do not leave floating.
- 4, 5, 14, / GND Ground Connect to System Ground. / Pad 2 / Active High Enable for the device. A resistor divider on this pin from input supply to GND can / EN/UVLO 6 Analog Input / be used to adjust the Undervoltage Lockout threshold. Do not leave floating. / A capacitor from this pin to GND sets the overcurrent blanking interval during which the
- Active High Enable for the device. A resistor divider on this pin from input supply to GND can / EN/UVLO 6 Analog Input / be used to adjust the Undervoltage Lockout threshold. Do not leave floating. / A capacitor from this pin to GND sets the overcurrent blanking interval during which the / output current can temporarily exceed set current limit (but lower than fast-trip threshold) / Analog / ITIMER 7 before the device overcurrent response takes action. Leave this pin open for fastest

### Specifications, ratings, and operating conditions

- TPS25980: 2.7- 24 V, 8 A, 3 mOhm Smart eFuse - Integrated Hot-swap Protection With / Adjustable Transient Fault Management / 1 Features 3 Description / * Wide input voltage range: 2.7 V to 24 V The TPS25980x family of eFuses is a highly / 30-V Absolute maximum integrated circuit protection and power management / * Low On-Resistance: R = 3-mOhm typical solution in a small package. The devices are / ON
- Adjustable Transient Fault Management / 1 Features 3 Description / * Wide input voltage range: 2.7 V to 24 V The TPS25980x family of eFuses is a highly / 30-V Absolute maximum integrated circuit protection and power management / * Low On-Resistance: R = 3-mOhm typical solution in a small package. The devices are / ON / * Circuit Breaker Response operational over a wide input voltage range. A single
- 30-V Absolute maximum integrated circuit protection and power management / * Low On-Resistance: R = 3-mOhm typical solution in a small package. The devices are / ON / * Circuit Breaker Response operational over a wide input voltage range. A single / * Adjustable current limit threshold part caters to low-voltage systems needing minimal / Range: 2 A to 8 A I*R voltage drop as well as higher voltage, high / Accuracy: +/- 8% (typical for I > 5 A) current systems needing low power dissipation. They
- * Low On-Resistance: R = 3-mOhm typical solution in a small package. The devices are / ON / * Circuit Breaker Response operational over a wide input voltage range. A single / * Adjustable current limit threshold part caters to low-voltage systems needing minimal / Range: 2 A to 8 A I*R voltage drop as well as higher voltage, high / Accuracy: +/- 8% (typical for I > 5 A) current systems needing low power dissipation. They / LIM
- ON / * Circuit Breaker Response operational over a wide input voltage range. A single / * Adjustable current limit threshold part caters to low-voltage systems needing minimal / Range: 2 A to 8 A I*R voltage drop as well as higher voltage, high / Accuracy: +/- 8% (typical for I > 5 A) current systems needing low power dissipation. They / LIM / * Adjustable over-current blanking timer are a robust defense against overloads, short-circuits,
- * Circuit Breaker Response operational over a wide input voltage range. A single / * Adjustable current limit threshold part caters to low-voltage systems needing minimal / Range: 2 A to 8 A I*R voltage drop as well as higher voltage, high / Accuracy: +/- 8% (typical for I > 5 A) current systems needing low power dissipation. They / LIM / * Adjustable over-current blanking timer are a robust defense against overloads, short-circuits, / voltage surges and excessive inrush current.
- Range: 2 A to 8 A I*R voltage drop as well as higher voltage, high / Accuracy: +/- 8% (typical for I > 5 A) current systems needing low power dissipation. They / LIM / * Adjustable over-current blanking timer are a robust defense against overloads, short-circuits, / voltage surges and excessive inrush current. / Handles load transients without tripping / * Accurate current monitor output Overvoltage events are limited by internal cutoff
- Accuracy: +/- 8% (typical for I > 5 A) current systems needing low power dissipation. They / LIM / * Adjustable over-current blanking timer are a robust defense against overloads, short-circuits, / voltage surges and excessive inrush current. / Handles load transients without tripping / * Accurate current monitor output Overvoltage events are limited by internal cutoff / +/- 3% (typical at 25 deg C for I > 3 A) circuits, with multiple device options to choose the
- * Adjustable over-current blanking timer are a robust defense against overloads, short-circuits, / voltage surges and excessive inrush current. / Handles load transients without tripping / * Accurate current monitor output Overvoltage events are limited by internal cutoff / +/- 3% (typical at 25 deg C for I > 3 A) circuits, with multiple device options to choose the / OUT / * User configurable fault response overvoltage threshold.
- * Accurate current monitor output Overvoltage events are limited by internal cutoff / +/- 3% (typical at 25 deg C for I > 3 A) circuits, with multiple device options to choose the / OUT / * User configurable fault response overvoltage threshold. / Latch-off or auto-retry / The device provides a circuit-breaker response / Number of retries (Finite or indefinite)
- Latch-off or auto-retry / The device provides a circuit-breaker response / Number of retries (Finite or indefinite) / to overcurrent conditions. The overcurrent limit / Delay between retries / (circuit-breaker threshold) and fast-trip (short-circuit) / * Robust short-circuit protection
- (circuit-breaker threshold) and fast-trip (short-circuit) / * Robust short-circuit protection / threshold can be set with a single external resistor. / Fast-trip response time < 400-ns typical The devices intelligently manage the overcurrent / Tested against 1 million power-into-short events response by distinguishing between transient events / Immune to line transients - no nuisance tripping and actual faults, thereby allowing the system / * Adjustable output slew rate (dVdt) control to function uninterrupted during line and load
- Tested against 1 million power-into-short events response by distinguishing between transient events / Immune to line transients - no nuisance tripping and actual faults, thereby allowing the system / * Adjustable output slew rate (dVdt) control to function uninterrupted during line and load / * Adjustable undervoltage lockout transients without compromising on the robustness / * Overvoltage lockout (Fixed 3.7-V, 7.6-V, 16.9-V of the protection against faults. The device can be / and no-OVLO options) configured to stay latched off or retry automatically / * Integrated overtemperature protection after a fault shutdown. The number of auto-retries
- Immune to line transients - no nuisance tripping and actual faults, thereby allowing the system / * Adjustable output slew rate (dVdt) control to function uninterrupted during line and load / * Adjustable undervoltage lockout transients without compromising on the robustness / * Overvoltage lockout (Fixed 3.7-V, 7.6-V, 16.9-V of the protection against faults. The device can be / and no-OVLO options) configured to stay latched off or retry automatically / * Integrated overtemperature protection after a fault shutdown. The number of auto-retries / * Power good indication as well as the retry delay are configurable
- 4 Revision History.............................................................. 2 / 5 Device Comparison Table...............................................3 / 6 Pin Configuration and Functions...................................4 / 7 Specifications.................................................................. 6 / 7.1 Absolute Maximum Ratings........................................ 6 / 7.2 ESD Ratings............................................................... 6 / 7.3 Recommended Operating Conditions.........................7
- 5 Device Comparison Table...............................................3 / 6 Pin Configuration and Functions...................................4 / 7 Specifications.................................................................. 6 / 7.1 Absolute Maximum Ratings........................................ 6 / 7.2 ESD Ratings............................................................... 6 / 7.3 Recommended Operating Conditions.........................7 / 7.4 Thermal Information....................................................7
- 6 Pin Configuration and Functions...................................4 / 7 Specifications.................................................................. 6 / 7.1 Absolute Maximum Ratings........................................ 6 / 7.2 ESD Ratings............................................................... 6 / 7.3 Recommended Operating Conditions.........................7 / 7.4 Thermal Information....................................................7 / 7.5 Electrical Characteristics.............................................8
- 7 Specifications.................................................................. 6 / 7.1 Absolute Maximum Ratings........................................ 6 / 7.2 ESD Ratings............................................................... 6 / 7.3 Recommended Operating Conditions.........................7 / 7.4 Thermal Information....................................................7 / 7.5 Electrical Characteristics.............................................8 / 7.6 Timing Requirements..................................................9

### Dimensions, package, and mechanical information

- 1 Features 3 Description / * Wide input voltage range: 2.7 V to 24 V The TPS25980x family of eFuses is a highly / 30-V Absolute maximum integrated circuit protection and power management / * Low On-Resistance: R = 3-mOhm typical solution in a small package. The devices are / ON / * Circuit Breaker Response operational over a wide input voltage range. A single / * Adjustable current limit threshold part caters to low-voltage systems needing minimal
- R ILIM >= 182 Ohm indefinitely due to a persistent fault. / * IEC 62368 CB Certification / The TPS25980x devices are available in a small / * Small footprint: 4-mm x 4-mm QFN package / 4 mm x 4 mm QFN package. The devices / 2 Applications are characterized for operation over a junction / temperature range of -40 deg C to 125 deg C.
- * IEC 62368 CB Certification / The TPS25980x devices are available in a small / * Small footprint: 4-mm x 4-mm QFN package / 4 mm x 4 mm QFN package. The devices / 2 Applications are characterized for operation over a junction / temperature range of -40 deg C to 125 deg C. / * Hot-Swap, hot-plug
- * Hot-Swap, hot-plug / * Server standby rail, PCIe riser, add-on card and Device Information(1) / fan module protection / PART NUMBER PACKAGE BODY SIZE (NOM) / * Routers and switches optical module protection / TPS25980x QFN (24) 4.0 mm x 4.0 mm / * Industrial PC
- * Routers and switches optical module protection / TPS25980x QFN (24) 4.0 mm x 4.0 mm / * Industrial PC / * Digital TV (1) For all available packages, see the orderable addendum at / the end of the data sheet. / SPuopwpelyr RVL1 E L IN D N S /U T V R T L T P O S25980 O P U G T R V P P G G / NRETRY IMON
- Simplified Schematics / An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications, / intellectual property matters and other important disclaimers. PRODUCTION DATA. / PART NUMBER | PACKAGE | BODY SIZE (NOM) / TPS25980x | QFN (24) | 4.0 mm x 4.0 mm / RVL1 RVL2 C*NRETRY C*R C E *L T D R S Y T _ R D T LY | | | LDSTRT EN/UVLO PG NRETRY IMON RETRY_DLY dVdt ILIM GNDITIMER | | VPG RPG / | C*NRETRY C*R C E *L T D R S Y T _ R D T LY | | | |
- 12.4 Trademarks.............................................................43 / 12.5 Electrostatic Discharge Caution..............................43 / 12.6 Glossary..................................................................43 / 13 Mechanical, Packaging, and Orderable / Information.................................................................... 44 / 4 Revision History / NOTE: Page numbers for previous revisions may differ from page numbers in the current version.
- MAX / T Junction temperature Internally Limited deg C / J / T Maximum Soldering Temperature 300 deg C / LEAD / T Storage temperature -65 150 deg C / stg
- V RETRY_DLY | Maximum RETRY_DLY Pin Voltage Range | RETRY_DLY | Internally Limited | | V / I MAX | Maximum Continuous Switch Current | IN to OUT | Internally Limited | | A / T J | Junction temperature | | Internally Limited | | deg C / T LEAD | Maximum Soldering Temperature | | 300 | | deg C / T stg | Storage temperature | | 65 150 | | deg C / | | | VALUE | UNIT / V (ESD) | Electrostatic discharge | Human body model (HBM), per ANSI/ESDA/ JEDEC JS-001, all pins(1) | +/- 2000 | V
- JB / R Junction-to-case (bottom) thermal resistance 1.6 deg C/W / JC(bot) / (1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application / report. / (2) Based on simulations conducted with the device mounted on a JEDEC 4-layer PCB (2s2p) with minimum recommended pad size (2 oz / Cu) and 3x2 via array.
- JC(bot) / (1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application / report. / (2) Based on simulations conducted with the device mounted on a JEDEC 4-layer PCB (2s2p) with minimum recommended pad size (2 oz / Cu) and 3x2 via array. / Copyright 2022 Texas Instruments Incorporated Submit Document Feedback 7 / Product Folder Links: TPS25980
- t is set for 6 ms interval. / ITIMER / 9.3.1.3 External Component Settings / By following similar design procedure as outlined in Detailed Design Procedure, the external component values / are calculated as below / * R = 210 Ohm to set 7-A current limit / ILIM
- TPS25980x eFuse provides inrush current management and also protects the system from most common faults / such as undervoltage, overvoltage and overcurrents. The combination of high current support along with low / ON-resistance makes TPS25980x eFuse an ideal protection solution for PCIe cards, Storage Interfaces and / DC Fan loads. The external component values can be calculated by following the design procedure outlined in / Detailed Design Procedure. Alternatively, a spreadsheet design tool TPS25980xx Design Calculator is available / for simplified design efforts. / TPS25980
- TPS259803O | Click here | Click here | Click here | Click here | Click here / TPS259804O | Click here | Click here | Click here | Click here | Click here / TPS259807O | Click here | Click here | Click here | Click here | Click here / 13 Mechanical, Packaging, and Orderable Information / The following pages include mechanical, packaging, and orderable information. This information is the most / current data available for the designated devices. This data is subject to change without notice and revision of / this document. For browser-based versions of this data sheet, refer to the left-hand navigation.
- TPS259804O | Click here | Click here | Click here | Click here | Click here / TPS259807O | Click here | Click here | Click here | Click here | Click here / 13 Mechanical, Packaging, and Orderable Information / The following pages include mechanical, packaging, and orderable information. This information is the most / current data available for the designated devices. This data is subject to change without notice and revision of / this document. For browser-based versions of this data sheet, refer to the left-hand navigation. / TPS25980
- SLVSFR1 - AUGUST 2020 www.ti.com / 44 Submit Document Feedback Copyright 2022 Texas Instruments Incorporated / Product Folder Links: TPS25980 / PACKAGE OPTION ADDENDUM / www.ti.com 6-Feb-2026 / PACKAGING INFORMATION / Orderable part number Status
- (1) / Material type / (2) / Package | Pins Package qty | Carrier RoHS / (3) / Lead finish/ / Ball material
- (6) Part marking: There may be an additional marking, which relates to the logo, the lot trace code information, or the environmental category of the part. / Addendum-Page 1 / Orderable part number | Status (1) | Material type (2) | Package | Pins | Package qty | Carrier | RoHS (3) | Lead finish/ Ball material (4) | MSL rating/ Peak reflow (5) | Op temp ( deg C) | Part marking (6) / TPS259802ONRGER | Active | Production | VQFN (RGE) | 24 | 3000 | LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | TP2598 02ON / TPS259802ONRGER.A | Active | Production | VQFN (RGE) | 24 | 3000 | LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | TP2598 02ON / TPS259803ONRGER | Active | Production | VQFN (RGE) | 24 | 3000 | LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | TP2598 03ON

### Formulas, equations, and configuration calculations

- 30-V Absolute maximum integrated circuit protection and power management / * Low On-Resistance: R = 3-mOhm typical solution in a small package. The devices are / ON / * Circuit Breaker Response operational over a wide input voltage range. A single / * Adjustable current limit threshold part caters to low-voltage systems needing minimal / Range: 2 A to 8 A I*R voltage drop as well as higher voltage, high / Accuracy: +/- 8% (typical for I > 5 A) current systems needing low power dissipation. They
- * Low On-Resistance: R = 3-mOhm typical solution in a small package. The devices are / ON / * Circuit Breaker Response operational over a wide input voltage range. A single / * Adjustable current limit threshold part caters to low-voltage systems needing minimal / Range: 2 A to 8 A I*R voltage drop as well as higher voltage, high / Accuracy: +/- 8% (typical for I > 5 A) current systems needing low power dissipation. They / LIM
- Range: 2 A to 8 A I*R voltage drop as well as higher voltage, high / Accuracy: +/- 8% (typical for I > 5 A) current systems needing low power dissipation. They / LIM / * Adjustable over-current blanking timer are a robust defense against overloads, short-circuits, / voltage surges and excessive inrush current. / Handles load transients without tripping / * Accurate current monitor output Overvoltage events are limited by internal cutoff
- Latch-off or auto-retry / The device provides a circuit-breaker response / Number of retries (Finite or indefinite) / to overcurrent conditions. The overcurrent limit / Delay between retries / (circuit-breaker threshold) and fast-trip (short-circuit) / * Robust short-circuit protection
- * Robust short-circuit protection / threshold can be set with a single external resistor. / Fast-trip response time < 400-ns typical The devices intelligently manage the overcurrent / Tested against 1 million power-into-short events response by distinguishing between transient events / Immune to line transients - no nuisance tripping and actual faults, thereby allowing the system / * Adjustable output slew rate (dVdt) control to function uninterrupted during line and load / * Adjustable undervoltage lockout transients without compromising on the robustness
- Fast-trip response time < 400-ns typical The devices intelligently manage the overcurrent / Tested against 1 million power-into-short events response by distinguishing between transient events / Immune to line transients - no nuisance tripping and actual faults, thereby allowing the system / * Adjustable output slew rate (dVdt) control to function uninterrupted during line and load / * Adjustable undervoltage lockout transients without compromising on the robustness / * Overvoltage lockout (Fixed 3.7-V, 7.6-V, 16.9-V of the protection against faults. The device can be / and no-OVLO options) configured to stay latched off or retry automatically
- Immune to line transients - no nuisance tripping and actual faults, thereby allowing the system / * Adjustable output slew rate (dVdt) control to function uninterrupted during line and load / * Adjustable undervoltage lockout transients without compromising on the robustness / * Overvoltage lockout (Fixed 3.7-V, 7.6-V, 16.9-V of the protection against faults. The device can be / and no-OVLO options) configured to stay latched off or retry automatically / * Integrated overtemperature protection after a fault shutdown. The number of auto-retries / * Power good indication as well as the retry delay are configurable
- * Adjustable load detect and handshake timer with capacitors. This enables remote systems to / * UL 2367 Recognition automatically recover from temporary faults while / File no. E339631 ensuring that power supplies are not stressed / R ILIM >= 182 Ohm indefinitely due to a persistent fault. / * IEC 62368 CB Certification / The TPS25980x devices are available in a small / * Small footprint: 4-mm x 4-mm QFN package
- The TPS25980x devices are available in a small / * Small footprint: 4-mm x 4-mm QFN package / 4 mm x 4 mm QFN package. The devices / 2 Applications are characterized for operation over a junction / temperature range of -40 deg C to 125 deg C. / * Hot-Swap, hot-plug / * Server standby rail, PCIe riser, add-on card and Device Information(1)
- the end of the data sheet. / SPuopwpelyr RVL1 E L IN D N S /U T V R T L T P O S25980 O P U G T R V P P G G / NRETRY IMON / CIN RVL2 C*NRETRY C*R C E *L T D R S Y T _ R D T LY R IL E IM R TR ILI Y M _D G L N Y DITI d M V E d R C t *ITIME C R dVdt RIMON CL RL / * Optional components for extended functionality / Simplified Schematics / An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications,
- intellectual property matters and other important disclaimers. PRODUCTION DATA. / PART NUMBER | PACKAGE | BODY SIZE (NOM) / TPS25980x | QFN (24) | 4.0 mm x 4.0 mm / RVL1 RVL2 C*NRETRY C*R C E *L T D R S Y T _ R D T LY | | | LDSTRT EN/UVLO PG NRETRY IMON RETRY_DLY dVdt ILIM GNDITIMER | | VPG RPG / | C*NRETRY C*R C E *L T D R S Y T _ R D T LY | | | | / | | RILIM | | | / Table of Contents
- TPS25980x | QFN (24) | 4.0 mm x 4.0 mm / RVL1 RVL2 C*NRETRY C*R C E *L T D R S Y T _ R D T LY | | | LDSTRT EN/UVLO PG NRETRY IMON RETRY_DLY dVdt ILIM GNDITIMER | | VPG RPG / | C*NRETRY C*R C E *L T D R S Y T _ R D T LY | | | | / | | RILIM | | | / Table of Contents / 1 Features............................................................................1 / 2 Applications.....................................................................1
- 3 Description.......................................................................1 / 4 Revision History.............................................................. 2 / 5 Device Comparison Table...............................................3 / 6 Pin Configuration and Functions...................................4 / 7 Specifications.................................................................. 6 / 7.1 Absolute Maximum Ratings........................................ 6 / 7.2 ESD Ratings............................................................... 6
- TPS259803ONRGE | 7.6 | Circuit Breaker / TPS259804ONRGE | 16.9 | Circuit Breaker / TPS259807ONRGE | No OVLO | Circuit Breaker / 6 Pin Configuration and Functions / IN / IN / IN
- IN / IN / GND / EN/UVLO / ITIMER LDSTRT / PG / OUT
- OUT / OUT / GND / ILIM IMON RETRY_DLY NRETRY / IN / dVdt / GND
- GND / ILIM IMON RETRY_DLY NRETRY / IN / dVdt / GND / OUT OUT OUT OUT OUT / 1 18
- 4, 5, 14, / GND Ground Connect to System Ground. / Pad 2 / Active High Enable for the device. A resistor divider on this pin from input supply to GND can / EN/UVLO 6 Analog Input / be used to adjust the Undervoltage Lockout threshold. Do not leave floating. / A capacitor from this pin to GND sets the overcurrent blanking interval during which the

### Reference designs, applications, and examples

- The TPS25980x devices are available in a small / * Small footprint: 4-mm x 4-mm QFN package / 4 mm x 4 mm QFN package. The devices / 2 Applications are characterized for operation over a junction / temperature range of -40 deg C to 125 deg C. / * Hot-Swap, hot-plug / * Server standby rail, PCIe riser, add-on card and Device Information(1)
- NRETRY IMON / CIN RVL2 C*NRETRY C*R C E *L T D R S Y T _ R D T LY R IL E IM R TR ILI Y M _D G L N Y DITI d M V E d R C t *ITIME C R dVdt RIMON CL RL / * Optional components for extended functionality / Simplified Schematics / An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications, / intellectual property matters and other important disclaimers. PRODUCTION DATA. / PART NUMBER | PACKAGE | BODY SIZE (NOM)
- CIN RVL2 C*NRETRY C*R C E *L T D R S Y T _ R D T LY R IL E IM R TR ILI Y M _D G L N Y DITI d M V E d R C t *ITIME C R dVdt RIMON CL RL / * Optional components for extended functionality / Simplified Schematics / An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications, / intellectual property matters and other important disclaimers. PRODUCTION DATA. / PART NUMBER | PACKAGE | BODY SIZE (NOM) / TPS25980x | QFN (24) | 4.0 mm x 4.0 mm
- | | RILIM | | | / Table of Contents / 1 Features............................................................................1 / 2 Applications.....................................................................1 / 3 Description.......................................................................1 / 4 Revision History.............................................................. 2 / 5 Device Comparison Table...............................................3
- 8.3 Feature Description...................................................16 / 8.4 Fault Response.........................................................24 / 8.5 Device Functional Modes..........................................27 / 9 Application and Implementation..................................28 / 9.1 Application Information............................................. 28 / 9.2 Typical Application: Patient Monitoring System in / Medical Applications....................................................28
- 8.4 Fault Response.........................................................24 / 8.5 Device Functional Modes..........................................27 / 9 Application and Implementation..................................28 / 9.1 Application Information............................................. 28 / 9.2 Typical Application: Patient Monitoring System in / Medical Applications....................................................28 / 9.3 System Examples..................................................... 35
- 8.5 Device Functional Modes..........................................27 / 9 Application and Implementation..................................28 / 9.1 Application Information............................................. 28 / 9.2 Typical Application: Patient Monitoring System in / Medical Applications....................................................28 / 9.3 System Examples..................................................... 35 / 10 Power Supply Recommendations..............................39
- 9 Application and Implementation..................................28 / 9.1 Application Information............................................. 28 / 9.2 Typical Application: Patient Monitoring System in / Medical Applications....................................................28 / 9.3 System Examples..................................................... 35 / 10 Power Supply Recommendations..............................39 / 10.1 Transient Protection................................................39
- 9.1 Application Information............................................. 28 / 9.2 Typical Application: Patient Monitoring System in / Medical Applications....................................................28 / 9.3 System Examples..................................................... 35 / 10 Power Supply Recommendations..............................39 / 10.1 Transient Protection................................................39 / 10.2 Output Short-Circuit Measurements....................... 40
- 10.2 Output Short-Circuit Measurements....................... 40 / 11 Layout...........................................................................41 / 11.1 Layout Guidelines................................................... 41 / 11.2 Layout Example...................................................... 42 / 12 Device and Documentation Support..........................43 / 12.1 Documentation Support.......................................... 43 / 12.2 Receiving Notification of Documentation Updates..43
- JB / R Junction-to-case (bottom) thermal resistance 1.6 deg C/W / JC(bot) / (1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application / report. / (2) Based on simulations conducted with the device mounted on a JEDEC 4-layer PCB (2s2p) with minimum recommended pad size (2 oz / Cu) and 3x2 via array.
- fast trip was triggered by a transient event. However, if the fault is persistent, the device will stay in current / limit causing the junction temperature to rise and eventually enter thermal shutdown. See Overtemperature / Protection (OTP) section for details on the device response to overtemperature. / In some of the systems, for example servers or telecom equipment which house multiple hot-pluggable cards / connected to a common supply backplane, there can be transients on the supply due to switching of large / currents through the inductive backplane. This can result in current spikes on adjacent cards which could / TPS25980
- TPS25980 / SLVSFR1 - AUGUST 2020 www.ti.com / The LDSTRT pin can also be used to implement a load or module detect function wherein the output power is / presented only when the load or module is plugged in. A typical use case for this function is on optical module / power supply rails in Switches/Routers or similar networking end equipment. The LDSTRT pin should be tied / to a corresponding pin on the module connector which gets pulled low by the module when it is plugged in. An / example of such a signal is ModPrsL on QSFP-DD modules.
- presented only when the load or module is plugged in. A typical use case for this function is on optical module / power supply rails in Switches/Routers or similar networking end equipment. The LDSTRT pin should be tied / to a corresponding pin on the module connector which gets pulled low by the module when it is plugged in. An / example of such a signal is ModPrsL on QSFP-DD modules. / In this scheme, initially when the TPS25980x is powered up or enabled, the output charges up and PG is / asserted. If the module is not plugged in, there is no external pull-down on the LDSTRT pin and the pin voltage / starts rising due to internal pull-up . Once the LDSTRT pin voltage exceeds V , the TPS25980x turns
- 16 < N < 64 64 / 64 < N < 256 256 / 256 < N < 1024 1024 / Table 8-5. NRETRY and RETRY_DLY Combination Examples / Auto Retry Delay 915 ms 416 ms 91.7 ms 9.3 ms 3 ms / RETRY_DLY Capacitor 22 nF 10 nF 2.2 nF 220 pF 68 pF / No. of Auto Retries NRETRY Capacitor
- H | Capacitor to GND | Short to GND | Auto-retry indefinitely with finite delay between retries as per Equation 8 / TPS25980 / SLVSFR1 - AUGUST 2020 www.ti.com / 9 Application and Implementation / Note / Information in the following applications sections is not part of the TI component specification, / and TI does not warrant its accuracy or completeness. TIs customers are responsible for
- SLVSFR1 - AUGUST 2020 www.ti.com / 9 Application and Implementation / Note / Information in the following applications sections is not part of the TI component specification, / and TI does not warrant its accuracy or completeness. TIs customers are responsible for / determining suitability of components for their purposes, as well as validating and testing their design / implementation to confirm system functionality.
- Information in the following applications sections is not part of the TI component specification, / and TI does not warrant its accuracy or completeness. TIs customers are responsible for / determining suitability of components for their purposes, as well as validating and testing their design / implementation to confirm system functionality. / 9.1 Application Information / The TPS25980x device is an integrated 8-A eFuse that is typically used for hot-swap and power rail protection / applications. It operates from 2.7 V to 24 V with adjustable overcurrent and undervoltage protection. It also

## Page-by-page extracted content

### Page 1

#### Extracted tables

Table 1:

```text
PART NUMBER | PACKAGE | BODY SIZE (NOM)
TPS25980x | QFN (24) | 4.0 mm x 4.0 mm
```

Table 2:

```text
RVL1 RVL2 C*NRETRY C*R C E *L T D R S Y T _ R D T LY |  |  | LDSTRT EN/UVLO PG NRETRY IMON RETRY_DLY dVdt ILIM GNDITIMER |  | VPG RPG
 | C*NRETRY C*R C E *L T D R S Y T _ R D T LY |  |  |  | 
 |  | RILIM |  |  |
```

#### Raw extracted text

```text
TPS25980
SLVSFR1 - AUGUST 2020
TPS25980: 2.7- 24 V, 8 A, 3 mOhm Smart eFuse - Integrated Hot-swap Protection With
Adjustable Transient Fault Management
1 Features 3 Description
* Wide input voltage range: 2.7 V to 24 V The TPS25980x family of eFuses is a highly
- 30-V Absolute maximum integrated circuit protection and power management
* Low On-Resistance: R = 3-mOhm typical solution in a small package. The devices are
ON
* Circuit Breaker Response operational over a wide input voltage range. A single
* Adjustable current limit threshold part caters to low-voltage systems needing minimal
- Range: 2 A to 8 A I*R voltage drop as well as higher voltage, high
- Accuracy: +/- 8% (typical for I > 5 A) current systems needing low power dissipation. They
LIM
* Adjustable over-current blanking timer are a robust defense against overloads, short-circuits,
voltage surges and excessive inrush current.
- Handles load transients without tripping
* Accurate current monitor output Overvoltage events are limited by internal cutoff
- +/- 3% (typical at 25  deg C for I > 3 A) circuits, with multiple device options to choose the
OUT
* User configurable fault response overvoltage threshold.
- Latch-off or auto-retry
The device provides a circuit-breaker response
- Number of retries (Finite or indefinite)
to overcurrent conditions. The overcurrent limit
- Delay between retries
(circuit-breaker threshold) and fast-trip (short-circuit)
* Robust short-circuit protection
threshold can be set with a single external resistor.
- Fast-trip response time < 400-ns typical The devices intelligently manage the overcurrent
- Tested against 1 million power-into-short events response by distinguishing between transient events
- Immune to line transients - no nuisance tripping and actual faults, thereby allowing the system
* Adjustable output slew rate (dVdt) control to function uninterrupted during line and load
* Adjustable undervoltage lockout transients without compromising on the robustness
* Overvoltage lockout (Fixed 3.7-V, 7.6-V, 16.9-V of the protection against faults. The device can be
and no-OVLO options) configured to stay latched off or retry automatically
* Integrated overtemperature protection after a fault shutdown. The number of auto-retries
* Power good indication as well as the retry delay are configurable
* Adjustable load detect and handshake timer with capacitors. This enables remote systems to
* UL 2367 Recognition automatically recover from temporary faults while
- File no. E339631 ensuring that power supplies are not stressed
- R ILIM >= 182 Ohm indefinitely due to a persistent fault.
* IEC 62368 CB Certification
The TPS25980x devices are available in a small
* Small footprint: 4-mm x 4-mm QFN package
4 mm x 4 mm QFN package. The devices
2 Applications are characterized for operation over a junction
temperature range of -40 deg C to 125 deg C.
* Hot-Swap, hot-plug
* Server standby rail, PCIe riser, add-on card and Device Information(1)
fan module protection
PART NUMBER PACKAGE BODY SIZE (NOM)
* Routers and switches optical module protection
TPS25980x QFN (24) 4.0 mm x 4.0 mm
* Industrial PC
* Digital TV (1) For all available packages, see the orderable addendum at
the end of the data sheet.
SPuopwpelyr RVL1 E L IN D N S /U T V R T L T P O S25980 O P U G T R V P P G G
NRETRY IMON
CIN RVL2 C*NRETRY C*R C E *L T D R S Y T _ R D T LY R IL E IM R TR ILI Y M _D G L N Y DITI d M V E d R C t *ITIME C R dVdt RIMON CL RL
* Optional components for extended functionality
Simplified Schematics
An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications,
intellectual property matters and other important disclaimers. PRODUCTION DATA.
```

### Page 2

#### Extracted tables

Table 1:

```text
DATE | REVISION | NOTES
August 2020 | * | Initial release.
```

#### Raw extracted text

```text
Table of Contents
1 Features............................................................................1
2 Applications.....................................................................1
3 Description.......................................................................1
4 Revision History.............................................................. 2
5 Device Comparison Table...............................................3
6 Pin Configuration and Functions...................................4
7 Specifications.................................................................. 6
7.1 Absolute Maximum Ratings........................................ 6
7.2 ESD Ratings............................................................... 6
7.3 Recommended Operating Conditions.........................7
7.4 Thermal Information....................................................7
7.5 Electrical Characteristics.............................................8
7.6 Timing Requirements..................................................9
7.7 Switching Characteristics..........................................10
7.8 Typical Characteristics.............................................. 11
8 Detailed Description......................................................16
8.1 Overview...................................................................16
8.2 Functional Block Diagram.........................................16
8.3 Feature Description...................................................16
8.4 Fault Response.........................................................24
8.5 Device Functional Modes..........................................27
9 Application and Implementation..................................28
9.1 Application Information............................................. 28
9.2 Typical Application: Patient Monitoring System in
Medical Applications....................................................28
9.3 System Examples..................................................... 35
10 Power Supply Recommendations..............................39
10.1 Transient Protection................................................39
10.2 Output Short-Circuit Measurements....................... 40
11 Layout...........................................................................41
11.1 Layout Guidelines................................................... 41
11.2 Layout Example...................................................... 42
12 Device and Documentation Support..........................43
12.1 Documentation Support.......................................... 43
12.2 Receiving Notification of Documentation Updates..43
12.3 Support Resources................................................. 43
12.4 Trademarks.............................................................43
12.5 Electrostatic Discharge Caution..............................43
12.6 Glossary..................................................................43
13 Mechanical, Packaging, and Orderable
Information.................................................................... 44
4 Revision History
NOTE: Page numbers for previous revisions may differ from page numbers in the current version.
DATE REVISION NOTES
August 2020 * Initial release.
TPS25980
SLVSFR1 - AUGUST 2020 www.ti.com
2 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS25980
```

### Page 3

#### Extracted tables

Table 1:

```text
PART NUMBER | OVERVOLTAGE LOCKOUT THRESHOLD | OVERCURRENT RESPONSE
 | TYPICAL (V) | 
TPS259802ONRGE | 3.7 | Circuit Breaker
TPS259803ONRGE | 7.6 | Circuit Breaker
TPS259804ONRGE | 16.9 | Circuit Breaker
TPS259807ONRGE | No OVLO | Circuit Breaker
```

#### Raw extracted text

```text
5 Device Comparison Table
PART NUMBER
OVERVOLTAGE LOCKOUT
THRESHOLD OVERCURRENT RESPONSE
TYPICAL (V)
TPS259802ONRGE 3.7 Circuit Breaker
TPS259803ONRGE 7.6 Circuit Breaker
TPS259804ONRGE 16.9 Circuit Breaker
TPS259807ONRGE No OVLO Circuit Breaker
www.ti.com
TPS25980
SLVSFR1 - AUGUST 2020
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 3
Product Folder Links: TPS25980
```

### Page 4

#### Extracted tables

Table 1:

```text
PIN |  | TYPE | DESCRIPTION
NAME | NO. |  | 
OUT | 17, 18, 19, 20, 21, 22, 23, 24 | Power | Power Output.
IN | 1, 2, 3, 16, Pad 1 | Thermal / Power | Power Input. The exposed pad must be soldered to input power plane uniformly to ensure proper heat dissipation and to maintain optimal current distribution through the device.
GND | 4, 5, 14, Pad 2 | Ground | Connect to System Ground.
EN/UVLO | 6 | Analog Input | Active High Enable for the device. A resistor divider on this pin from input supply to GND can be used to adjust the Undervoltage Lockout threshold. Do not leave floating.
ITIMER | 7 | Analog Output | A capacitor from this pin to GND sets the overcurrent blanking interval during which the output current can temporarily exceed set current limit (but lower than fast-trip threshold) before the device overcurrent response takes action. Leave this pin open for fastest response to overcurrent events. Refer to ITIMER Functional Mode Summary for more details.
ILIM | 8 | Analog Output | An external resistor from this pin to GND sets the output current limit threshold and fast trip threshold. Do not leave floating.
IMON | 9 | Analog Output | Analog output load current monitor. This pin sources a current proportional to the load current. This can be converted to a voltage signal by connecting an appropriate resistor from this pin to GND.
RETRY_DLY | 10 | Analog Output | A capacitor from this pin to GND sets the time period that has to elapse after a fault shutdown before the device attempts to restart automatically. Connect this pin to GND for latch-off operation (no auto-retries) after a fault. Refer to Fault Response section for more details.
NRETRY | 11 | Analog Output | A capacitor from this pin to GND sets the number of times the part attempts to restart automatically after shutdown due to fault. Connect this pin to GND if the part should retry indefinitely. Refer to Fault Response section for more details.
```

#### Raw extracted text

```text
6 Pin Configuration and Functions
IN
IN
IN
GND
EN/UVLO
ITIMER LDSTRT
PG
OUT
OUT
OUT
GND
ILIM IMON RETRY_DLY NRETRY
IN
dVdt
GND
OUT OUT OUT OUT OUT
1 18
2 IN 17
Thermal Pad 1
3 16
4 15
5 14
GND
Thermal Pad 2
6 13
7 8 9 0 1 1 1 2 1
24 23 22 21 20 19
TPS25980
SLVSFR1 - AUGUST 2020 www.ti.com
Figure 6-1. RGE 24-Pin QFN Top View
Pin Functions
PIN
TYPE DESCRIPTION
NAME NO.
17, 18, 19,
OUT 20, 21, 22, Power Power Output.
23, 24
1, 2, 3, 16, Thermal / Power Input. The exposed pad must be soldered to input power plane uniformly to ensure
IN
Pad 1 Power proper heat dissipation and to maintain optimal current distribution through the device.
4, 5, 14,
GND Ground Connect to System Ground.
Pad 2
Active High Enable for the device. A resistor divider on this pin from input supply to GND can
EN/UVLO 6 Analog Input
be used to adjust the Undervoltage Lockout threshold. Do not leave floating.
A capacitor from this pin to GND sets the overcurrent blanking interval during which the
output current can temporarily exceed set current limit (but lower than fast-trip threshold)
Analog
ITIMER 7 before the device overcurrent response takes action. Leave this pin open for fastest
Output
response to overcurrent events. Refer to ITIMER Functional Mode Summary for more
details.
Analog An external resistor from this pin to GND sets the output current limit threshold and fast trip
ILIM 8
Output threshold. Do not leave floating.
Analog output load current monitor. This pin sources a current proportional to the load
Analog
IMON 9 current. This can be converted to a voltage signal by connecting an appropriate resistor from
Output
this pin to GND.
A capacitor from this pin to GND sets the time period that has to elapse after a fault
Analog shutdown before the device attempts to restart automatically. Connect this pin to GND for
RETRY_DLY 10
Output latch-off operation (no auto-retries) after a fault. Refer to Fault Response section for more
details.
A capacitor from this pin to GND sets the number of times the part attempts to restart
Analog
NRETRY 11 automatically after shutdown due to fault. Connect this pin to GND if the part should retry
Output
indefinitely. Refer to Fault Response section for more details.
4 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS25980
```

### Page 5

#### Extracted tables

Table 1:

```text
PIN |  | TYPE | DESCRIPTION
NAME | NO. |  | 
LDSTRT | 12 | Analog Input | Load Detect/Handshake Signal. A capacitor from this pin to GND sets the time period after PG assertion within which the pin has to be pulled low for the device to remain ON. Connect to GND if the load detect/handshake feature is not used. Refer to Load Detect/Handshake (LDSTRT) section for more details. Do not leave floating.
PG | 13 | Digital Output | Active High Power Good Indication. This pin is asserted when the FET is fully enhanced and output has reached maximum voltage. It is an open drain output that requires an external pull-up resistor to an external supply. This pin remains logic low when V < V . IN UVP
dVdt | 15 | Analog Output | A capacitor from this pin to GND sets the output turn on slew rate. Leave this pin floating for the fastest slew rate during start up.
```

#### Raw extracted text

```text
TPS25980
www.ti.com SLVSFR1 - AUGUST 2020
Pin Functions (continued)
PIN
TYPE DESCRIPTION
NAME NO.
Load Detect/Handshake Signal. A capacitor from this pin to GND sets the time period after
PG assertion within which the pin has to be pulled low for the device to remain ON. Connect
LDSTRT 12 Analog Input
to GND if the load detect/handshake feature is not used. Refer to Load Detect/Handshake
(LDSTRT) section for more details. Do not leave floating.
Active High Power Good Indication. This pin is asserted when the FET is fully enhanced and
PG 13 Digital Output output has reached maximum voltage. It is an open drain output that requires an external
pull-up resistor to an external supply. This pin remains logic low when V < V .
IN UVP
Analog A capacitor from this pin to GND sets the output turn on slew rate. Leave this pin floating for
dVdt 15
Output the fastest slew rate during start up.
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 5
Product Folder Links: TPS25980
```

### Page 6

#### Extracted tables

Table 1:

```text
Parameter |  | Pin | MIN | MAX | UNIT
V IN | Maximum Input Voltage Range | IN | 0.3 30 |  | V
V OUT | Maximum Output Voltage Range | OUT | 0.8 min (30V, V + 0.3) IN |  | V
V EN/UVLO | Maximum Enable Pin Voltage Range | EN/UVLO | 0.3 7 |  | V
V LDSTRT | Maximum LDSTRT Pin Voltage Range | LDSTRT | 7 |  | V
V dVdt | Maximum dVdt Pin Voltage Range | dVdt | Internally Limited |  | V
V PG | Maximum PG Pin Voltage Range | PG | 0.3 7 |  | V
V ITIMER | Maximum ITIMER Pin Voltage Range | ITIMER | Internally Limited |  | V
V NRETRY | Maximum NRETRY Pin Voltage Range | NRETRY | Internally Limited |  | V
V RETRY_DLY | Maximum RETRY_DLY Pin Voltage Range | RETRY_DLY | Internally Limited |  | V
I MAX | Maximum Continuous Switch Current | IN to OUT | Internally Limited |  | A
T J | Junction temperature |  | Internally Limited |  | deg C
T LEAD | Maximum Soldering Temperature |  | 300 |  | deg C
T stg | Storage temperature |  | 65 150 |  | deg C
```

Table 2:

```text
|  |  | VALUE | UNIT
V (ESD) | Electrostatic discharge | Human body model (HBM), per ANSI/ESDA/ JEDEC JS-001, all pins(1) | +/- 2000 | V
 |  | Charged device model (CDM), per JEDEC specificationJESD22-C101, all pins(2) | +/- 1000 |
```

#### Raw extracted text

```text
TPS25980
SLVSFR1 - AUGUST 2020 www.ti.com
7 Specifications
7.1 Absolute Maximum Ratings
over operating free-air temperature range (unless otherwise noted)(1)
Parameter Pin MIN MAX UNIT
V Maximum Input Voltage Range IN -0.3 30 V
IN
V Maximum Output Voltage Range OUT -0.8 min (30V, V + 0.3) V
OUT IN
V Maximum Enable Pin Voltage Range EN/UVLO -0.3 7 V
EN/UVLO
V Maximum LDSTRT Pin Voltage Range LDSTRT 7 V
LDSTRT
V Maximum dVdt Pin Voltage Range dVdt Internally Limited V
dVdt
V Maximum PG Pin Voltage Range PG -0.3 7 V
PG
V Maximum ITIMER Pin Voltage Range ITIMER Internally Limited V
ITIMER
V Maximum NRETRY Pin Voltage Range NRETRY Internally Limited V
NRETRY
V Maximum RETRY_DLY Pin Voltage Range RETRY_DLY Internally Limited V
RETRY_DLY
I Maximum Continuous Switch Current IN to OUT Internally Limited A
MAX
T Junction temperature Internally Limited  deg C
J
T Maximum Soldering Temperature 300  deg C
LEAD
T Storage temperature -65 150  deg C
stg
(1) Stresses beyond those listed under Absolute Maximum Rating may cause permanent damage to the device. These are stress
ratings only, which do not imply functional operation of the device at these or any other conditions beyond those indicated under
Recommended Operating Conditions. Exposure to absolute-maximum-rated conditions for extended periods may affect device
reliability.
7.2 ESD Ratings
VALUE UNIT
Human body model (HBM), per ANSI/ESDA/
+/- 2000
JEDEC JS-001, all pins(1)
V Electrostatic discharge V
(ESD)
Charged device model (CDM), per JEDEC
+/- 1000
specificationJESD22-C101, all pins(2)
(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process.
(2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process.
6 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS25980
```

### Page 7

#### Extracted tables

Table 1:

```text
Parameter |  | Pin | MIN | MAX | UNIT
V IN | Input Voltage Range | IN | 2.7 24 |  | V
V OUT | Output Voltage Range | OUT | V + 0.3 IN |  | V
V EN/UVLO | Enable Pin Voltage Range | EN/UVLO | 6(1) |  | V
V LDSTRT | LDSTRT Pin Capacitor Voltage Rating | LDSTRT | 4 |  | V
V dVdT | dVdT Pin Capacitor Voltage Rating | dVdt | V + 4 IN |  | V
V PG | PG Pin Voltage Range | PG | 6(2) |  | V
V ITIMER | ITIMER Pin Capacitor Voltage Rating | ITIMER | 4 |  | V
V NRETRY | NRETRY Pin Capacitor Voltage Rating | NRETRY | 4 |  | V
V RETRY_DLY | RETRY_DLY Pin Capacitor Voltage Rating | RETRY_DLY | 4 |  | V
R ILIM | ILIM Pin Resistor | ILIM | 182 1650 |  | Ohm
I MAX | Continuous Switch Current | IN to OUT | 8 |  | A
T J | Junction temperature |  | 40 125 |  | deg C
```

Table 2:

```text
|  | TPS25980X | 
THERMAL METRIC(1) (2) |  | RGE (QFN) | UNIT
 |  | 24 PINS | 
R JA | Junction-to-ambient thermal resistance | 34.6 | deg C/W
R JC(top) | Junction-to-case (top) thermal resistance | 36.7 | deg C/W
R JB | Junction-to-board thermal resistance | 11.2 | deg C/W
JT | Junction-to-top characterization parameter | 3 | deg C/W
JB | Junction-to-board characterization parameter | 11.2 | deg C/W
R JC(bot) | Junction-to-case (bottom) thermal resistance | 1.6 | deg C/W
```

#### Raw extracted text

```text
TPS25980
www.ti.com SLVSFR1 - AUGUST 2020
7.3 Recommended Operating Conditions
over operating free-air temperature range (unless otherwise noted)
Parameter Pin MIN MAX UNIT
V Input Voltage Range IN 2.7 24 V
IN
V Output Voltage Range OUT V + 0.3 V
OUT IN
V Enable Pin Voltage Range EN/UVLO 6(1) V
EN/UVLO
V LDSTRT Pin Capacitor Voltage Rating LDSTRT 4 V
LDSTRT
V dVdT Pin Capacitor Voltage Rating dVdt V + 4 V
dVdT IN
V PG Pin Voltage Range PG 6(2) V
PG
V ITIMER Pin Capacitor Voltage Rating ITIMER 4 V
ITIMER
V NRETRY Pin Capacitor Voltage Rating NRETRY 4 V
NRETRY
V RETRY_DLY Pin Capacitor Voltage Rating RETRY_DLY 4 V
RETRY_DLY
R ILIM Pin Resistor ILIM 182 1650 Ohm
ILIM
I Continuous Switch Current IN to OUT 8 A
MAX
T Junction temperature -40 125  deg C
J
(1) For supply voltages below 6V, it is okay to pull up the EN pin to IN directly. For supply voltages greater than 6V, it is recommended
to use an appropriate resistor divider between IN, EN and GND to ensure the voltage at the EN pin is within the specified limits.
(2) For supply voltages below 6V, it is okay to pull up the PG pin to IN/OUT through a resistor. For supply voltages greater than 6V, it is
recommended to use a stepped down power supply to ensure the voltage at the PG pin is within the specified limits.
7.4 Thermal Information
TPS25980X
THERMAL METRIC(1) (2) RGE (QFN) UNIT
24 PINS
R Junction-to-ambient thermal resistance 34.6  deg C/W
JA
R Junction-to-case (top) thermal resistance 36.7  deg C/W
JC(top)
R Junction-to-board thermal resistance 11.2  deg C/W
JB
 Junction-to-top characterization parameter 3  deg C/W
JT
 Junction-to-board characterization parameter 11.2  deg C/W
JB
R Junction-to-case (bottom) thermal resistance 1.6  deg C/W
JC(bot)
(1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application
report.
(2) Based on simulations conducted with the device mounted on a JEDEC 4-layer PCB (2s2p) with minimum recommended pad size (2 oz
Cu) and 3x2 via array.
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 7
Product Folder Links: TPS25980
```

### Page 8

#### Extracted tables

Table 1:

```text
PARAMETER |  | TEST CONDITIONS | MIN | TYP | MAX | UNIT
INPUT SUPPLY (IN) |  |  |  |  |  | 
V IN | Input Voltage Range |  | 2.7 24 |  |  | V
I Q | IN Quiescent Current | V >= V EN UVLO(R) | 800 1200 |  |  | uA
I SD | IN Shutdown Current | V < V < V SD EN UVLO | 204 300 |  |  | uA
 |  | V < V EN SD | 3.67 20 |  |  | uA
V UVP | IN Undervoltage Protection Threshold | V Rising IN | 2.46 2.53 2.6 |  |  | V
 |  | V Falling IN | 2.35 2.42 2.49 |  |  | V
OVERVOLTAGE PROTECTION (IN) |  |  |  |  |  | 
V OVP(R) | Overvoltage Protection Threshold | TPS259802x, V Rising IN | 3.62 3.7 3.76 |  |  | V
 |  | TPS259803x, V Rising IN | 7.39 7.6 7.76 |  |  | V
 |  | TPS259804x, V Rising IN | 16.32 16.9 17.31 |  |  | V
V OVP(F) |  | TPS259802x, V Falling IN | 3.52 3.6 3.66 |  |  | V
 |  | TPS259803x, V Falling IN | 7.22 7.4 7.55 |  |  | V
 |  | TPS259804x, V Falling IN | 15.80 16.4 16.81 |  |  | V
OUTPUT CURRENT MONITOR (IMON) |  |  |  |  |  | 
G IMON | Current Monitor Gain (I :I ) IMON OUT | 3 A <= I <= min(8 A, I ) OUT LIM | 228.78 246 263.22 |  |  | uA/A
OUTPUT CURRENT LIMIT (ILIM) |  |  |  |  |  | 
I LIM | I Current Limit Threshold OUT | R ILIM = 773 Ohm, T J = 25 C | 1.76 2 2.17 |  |  | A
 |  | R ILIM = 773 Ohm, T J = -40 to 125 C | 1.53 2 2.43 |  |  | A
 |  | R ILIM = 300 Ohm, T J = 25 C | 4.75 4.98 5.23 |  |  | A
 |  | R ILIM = 300 Ohm, T J = -40 to 125 C | 4.36 4.98 5.66 |  |  | A
 |  | R ILIM = 182 Ohm, T J = 25 C | 7.77 8.13 8.54 |  |  | A
 |  | R ILIM = 182 Ohm, T J = -40 to 125 C | 7.23 8.13 9.07 |  |  | A
 |  | R = Open ILIM | 0 |  |  | A
I CB | I Circuit Breaker Threshold OUT During ILIM pin Short to GND Condition (Single point failure) | R ILIM = Short to GND, T J = 25 C | 20 |  |  | A
I SC | Short-circuit Fast Trip Threshold |  | 210 |  |  | % I LIM
ON-RESISTANCE (IN - OUT) |  |  |  |  |  | 
R ON | ON State Resistance | T = 25 C, I = 2 A J OUT | 3 |  |  | mOhm
 |  | T = -40 to 125 C, I = 2 A J OUT | 5 |  |  | mOhm
ENABLE / UNDERVOLTAGE LOCKOUT (EN/UVLO) |  |  |  |  |  | 
V UVLO(R) | EN/UVLO Pin Voltage Threshold | V Rising EN | 1.18 1.2 1.23 |  |  | V
V UVLO(F) |  | V Falling EN | 1.08 1.1 1.13 |  |  | V
V SD | EN/UVLO Pin Voltage Threshold for Lowest Shutdown Current | V Falling EN | 0.59 0.8 |  |  | V
I ENLKG | EN/UVLO Pin Leakage Current |  | 0.1 |  |  | uA
POWER GOOD INDICATION (PG) |  |  |  |  |  | 
V PGD | PG Pin Low Voltage (PG de- asserted) | V < V , V < V I = 26 uA IN UVP EN SD, PG | 651 786 |  |  | mV
 |  | V = 3.3V, I <= 5 mA IN PG | 320 |  |  | mV
 |  | V >= 5V, I <= 5 mA IN PG | 100 |  |  | mV
I PGLKG | PG Pin Leakage Current (PG asserted) | PG pulled up to 5 V through 10 kOhm | 1.7 |  |  | uA
R ON(PGA) | R When PG is asserted ON |  | 4.2 |  |  | mOhm
```

#### Raw extracted text

```text
TPS25980
SLVSFR1 - AUGUST 2020 www.ti.com
7.5 Electrical Characteristics
(Test conditions unless otherwise noted) -40 deg C <= T <= 125 deg C, V = 12 V for TPS259804x/7x, 5 V for TPS259803x, 3.3 V for
J IN
TPS259802x, V = 2 V, R = 1650 Ohm , C = Open, OUT = Open. All voltages referenced to GND.
EN/UVLO ILIM dVdT
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
INPUT SUPPLY (IN)
V Input Voltage Range 2.7 24 V
IN
I IN Quiescent Current V >= V 800 1200 uA
Q EN UVLO(R)
V < V < V 204 300 uA
SD EN UVLO
I IN Shutdown Current
SD
V < V 3.67 20 uA
EN SD
IN Undervoltage Protection V IN Rising 2.46 2.53 2.6 V
V
UVP Threshold V Falling 2.35 2.42 2.49 V
IN
OVERVOLTAGE PROTECTION (IN)
TPS259802x, V Rising 3.62 3.7 3.76 V
IN
V TPS259803x, V Rising 7.39 7.6 7.76 V
OVP(R) IN
TPS259804x, V Rising 16.32 16.9 17.31 V
IN
Overvoltage Protection Threshold
TPS259802x, V Falling 3.52 3.6 3.66 V
IN
V TPS259803x, V Falling 7.22 7.4 7.55 V
OVP(F) IN
TPS259804x, V Falling 15.80 16.4 16.81 V
IN
OUTPUT CURRENT MONITOR (IMON)
G Current Monitor Gain (I :I ) 3 A <= I <= min(8 A, I ) 228.78 246 263.22 uA/A
IMON IMON OUT OUT LIM
OUTPUT CURRENT LIMIT (ILIM)
R ILIM = 773 Ohm, T J = 25 C 1.76 2 2.17 A
R ILIM = 773 Ohm, T J = -40 to 125 C 1.53 2 2.43 A
R ILIM = 300 Ohm, T J = 25 C 4.75 4.98 5.23 A
I LIM I OUT Current Limit Threshold R ILIM = 300 Ohm, T J = -40 to 125 C 4.36 4.98 5.66 A
R ILIM = 182 Ohm, T J = 25 C 7.77 8.13 8.54 A
R ILIM = 182 Ohm, T J = -40 to 125 C 7.23 8.13 9.07 A
R = Open 0 A
ILIM
I Circuit Breaker Threshold
OUT
I CB During ILIM pin Short to GND R ILIM = Short to GND, T J = 25 C 20 A
Condition (Single point failure)
I Short-circuit Fast Trip Threshold 210 % I
SC LIM
ON-RESISTANCE (IN - OUT)
T
J
= 25 C, I
OUT
= 2 A 3 mOhm
R ON State Resistance
ON
T
J
= -40 to 125 C, I
OUT
= 2 A 5 mOhm
ENABLE / UNDERVOLTAGE LOCKOUT (EN/UVLO)
V V Rising 1.18 1.2 1.23 V
UVLO(R) EN
EN/UVLO Pin Voltage Threshold
V V Falling 1.08 1.1 1.13 V
UVLO(F) EN
EN/UVLO Pin Voltage Threshold for
V V Falling 0.59 0.8 V
SD Lowest Shutdown Current EN
I EN/UVLO Pin Leakage Current 0.1 uA
ENLKG
POWER GOOD INDICATION (PG)
V < V , V < V I = 26 uA 651 786 mV
IN UVP EN SD, PG
PG Pin Low Voltage (PG de-
V V = 3.3V, I <= 5 mA 320 mV
PGD asserted) IN PG
V >= 5V, I <= 5 mA 100 mV
IN PG
PG Pin Leakage Current (PG
I PG pulled up to 5 V through 10 kOhm 1.7 uA
PGLKG asserted)
R R When PG is asserted 4.2 mOhm
ON(PGA) ON
8 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS25980
```

### Page 9

#### Extracted tables

Table 1:

```text
PARAMETER |  | TEST CONDITIONS | MIN | TYP | MAX | UNIT
V PGTHD | V - V Threshold when PG is de- IN OUT asserted |  | 0.224 0.326 0.450 |  |  | V
AUTO-RETRY DELAY INTERVAL (RETRY_DLY) |  |  |  |  |  | 
V RETRY_DLY(R) | RETRY_DLY Oscillator Comparator Threshold |  | 1.1 |  |  | V
V RETRY_DLY(F) |  |  | 0.35 |  |  | V
V RETRY_DLY_HYS | RETRY_DLY Oscillator Hysteresis |  | 0.65 0.75 0.85 |  |  | V
I RETRY_DLY | RETRY_DLY Pin Bias Current |  | 1.7 2.05 2.5 |  |  | uA
NUMBER OF AUTO-RETRIES (NRETRY) |  |  |  |  |  | 
V NRETRY(R) | NRETRY Oscillator Comparator Threshold |  | 1.1 |  |  | V
V NRETRY(F) |  |  | 0.35 |  |  | V
V NRETRY_HYS | NRETRY Oscillator Hysteresis |  | 0.65 0.75 0.85 |  |  | V
I NRETRY | NRETRY Pin Bias Current |  | 1.7 2.05 2.5 |  |  | uA
CURRENT FAULT TIMER (ITIMER) |  |  |  |  |  | 
I ITIMER | ITIMER Discharge Current | I > I > I SC OUT LIM | 1.4 2.1 2.8 |  |  | uA
R ITIMER | ITIMER Internal Pull-up Resistance | I < I OUT LIM | 23 |  |  | kOhm
V INT | ITIMER Pin Default Voltage | I < I OUT LIM | 2.5 |  |  | V
V ITIMER | ITIMER Comparator Falling Threshold | I > I > I ITIMER Voltage Rising SC OUT LIM, | 1.53 |  |  | V
V ITIMER | ITIMER Comparator Voltage Threshold Delta | I > I > I ITIMER Voltage Falling SC OUT LIM, | 0.7 0.98 1.3 |  |  | V
LDSTRT |  |  |  |  |  | 
V LDSTRT | LDSTRT Rising Threshold | LDSTRT voltage rising | 1.1 1.21 1.3 |  |  | V
I LDSTRT | LDSTRT Charging Current | PG asserted | 1.7 2.05 2.4 |  |  | uA
R LDSTRT | LDSTRT Internal Pull-down Resistance |  | 31 |  |  | Ohm
RQOD | QOD effective resistance | IN connected to EN, OUT connected to QOD, EN! to 1V | 73.2 |  |  | mA
OVERTEMPERATURE PROTECTION |  |  |  |  |  | 
TSD | Thermal Shutdown Threshold | T Rising J | 150 |  |  | deg C
TSDHys | Thermal Shutdown Hysteresis | T Falling J | 10 |  |  | deg C
dVdt |  |  |  |  |  | 
I dVdt | dVdt Pin Charging Current |  | 2 4.6 6.33 |  |  | uA
```

Table 2:

```text
PARAMETER |  | TEST CONDITIONS | MIN | TYP | MAX | UNIT
t OVP | Overvoltage Protection Response Time (1) | V > V to V , TPS259802x IN OVLO(R) OUT | 1.5 |  |  | us
 |  | V > V to V , TPS259803x IN OVLO(R) OUT | 5 |  |  | us
 |  | V > V to V , TPS259804x IN OVLO(R) OUT | 5 |  |  | us
t SC | Short Circuit Response Time | I > 3 x I to V turned OFF OUT LIM OUT | 400 |  |  | ns
t PGD | PG Assertion/De-assertion De-glitch (2) | V > (V + 3.6V) to PG or (V - V )> G IN IN OUT V to PG PGTHD | 120 |  |  | us
```

#### Raw extracted text

```text
TPS25980
www.ti.com SLVSFR1 - AUGUST 2020
7.5 Electrical Characteristics (continued)
(Test conditions unless otherwise noted) -40 deg C <= T <= 125 deg C, V = 12 V for TPS259804x/7x, 5 V for TPS259803x, 3.3 V for
J IN
TPS259802x, V = 2 V, R = 1650 Ohm , C = Open, OUT = Open. All voltages referenced to GND.
EN/UVLO ILIM dVdT
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
V - V Threshold when PG is de-
V IN OUT 0.224 0.326 0.450 V
PGTHD asserted
AUTO-RETRY DELAY INTERVAL (RETRY_DLY)
V RETRY_DLY(R) RETRY_DLY Oscillator Comparator 1.1 V
V Threshold 0.35 V
RETRY_DLY(F)
V RETRY_DLY Oscillator Hysteresis 0.65 0.75 0.85 V
RETRY_DLY_HYS
I RETRY_DLY Pin Bias Current 1.7 2.05 2.5 uA
RETRY_DLY
NUMBER OF AUTO-RETRIES (NRETRY)
V NRETRY(R) NRETRY Oscillator Comparator 1.1 V
V Threshold 0.35 V
NRETRY(F)
V NRETRY Oscillator Hysteresis 0.65 0.75 0.85 V
NRETRY_HYS
I NRETRY Pin Bias Current 1.7 2.05 2.5 uA
NRETRY
CURRENT FAULT TIMER (ITIMER)
I ITIMER Discharge Current I > I > I 1.4 2.1 2.8 uA
ITIMER SC OUT LIM
R ITIMER Internal Pull-up Resistance I < I 23 kOhm
ITIMER OUT LIM
V ITIMER Pin Default Voltage I < I 2.5 V
INT OUT LIM
ITIMER Comparator Falling
V I > I > I ITIMER Voltage Rising 1.53 V
ITIMER Threshold SC OUT LIM,
ITIMER Comparator Voltage
V I > I > I ITIMER Voltage Falling 0.7 0.98 1.3 V
ITIMER Threshold Delta SC OUT LIM,
LDSTRT
V LDSTRT Rising Threshold LDSTRT voltage rising 1.1 1.21 1.3 V
LDSTRT
I LDSTRT Charging Current PG asserted 1.7 2.05 2.4 uA
LDSTRT
LDSTRT Internal Pull-down
R 31 Ohm
LDSTRT Resistance
IN connected to EN, OUT connected to
RQOD QOD effective resistance 73.2 mA
QOD, EN! to 1V
OVERTEMPERATURE PROTECTION
TSD Thermal Shutdown Threshold T Rising 150  deg C
J
TSDHys Thermal Shutdown Hysteresis T Falling 10  deg C
J
dVdt
I dVdt Pin Charging Current 2 4.6 6.33 uA
dVdt
7.6 Timing Requirements
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
V > V to V , TPS259802x 1.5 us
IN OVLO(R) OUT
t Overvoltage Protection Response Time (1) V > V to V , TPS259803x 5 us
OVP IN OVLO(R) OUT
V > V to V , TPS259804x 5 us
IN OVLO(R) OUT
t Short Circuit Response Time I > 3 x I to V turned OFF 400 ns
SC OUT LIM OUT
V > (V + 3.6V) to PG or (V - V )>
t PG Assertion/De-assertion De-glitch (2) G IN IN OUT 120 us
PGD V to PG
PGTHD
(1) Please refer to Fig. 8-2
(2) Please refer to Fig. 8-5
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 9
Product Folder Links: TPS25980
```

### Page 10

#### Extracted tables

Table 1:

```text
PARAMETER |  | V IN | C = Open dVdt | C = 3300pF dVdt | C = dVdt 6800pF | UNIT
SR ON | Output Rising slew rate | 2.7 V | 6.26 | 1.39 | 0.68 | V/ms
 |  | 12 V | 7.35 | 1.4 | 0.68 | 
 |  | 24 V | 7.4 | 1.4 | 0.68 | 
t D,ON | Turn on delay | 2.7 V | 1.3 | 1.49 | 1.7 | ms
 |  | 12 V | 1.24 | 2.1 | 3.01 | 
 |  | 24 V | 1.2 | 2.91 | 4.74 | 
t R | Rise time | 2.7 V | 0.67 | 1.63 | 3.35 | ms
 |  | 12 V | 1.35 | 6.99 | 14.41 | 
 |  | 24 V | 2.66 | 13.77 | 28.41 | 
t ON | Turn on time | 2.7 V | 1.97 | 3.12 | 5.05 | ms
 |  | 12 V | 2.59 | 9.09 | 17.42 | 
 |  | 24 V | 3.86 | 16.68 | 33.15 | 
t D,OFF | Turn off delay | 2.7 V | 151 | 152 | 152 | us
 |  | 12 V | 212 | 212 | 212 | 
 |  | 24 V | 262 | 262 | 262 |
```

#### Raw extracted text

```text
TPS25980
SLVSFR1 - AUGUST 2020 www.ti.com
7.7 Switching Characteristics
The output rising slew rate is internally controlled and constant across the entire operating voltage range to ensure the
turn on timing is not affected by the load conditions. The rising slew rate can be adjusted by adding capacitance from
the dVdt pin to ground. As C is increased it will slow the rising slew rate (SR). See Slew Rate and Inrush Current
dVdt
Control (dVdt) section for more details. The Turn-Off Delay and Fall Time, however, are dependent on the RC time constant
of the load capacitance (C ) and Load Resistance (R ). The Switching Characteristics are only valid for the power-up
OUT L
sequence where the supply is available in steady state condition and the load voltage is completely discharged before the
device is enabled.Typical Values are taken at T = 25 deg C unless specifically noted otherwise. R = 3.6 Ohm, C = 1 mF
J L OUT
C =
PARAMETER V C = Open C = 3300pF dVdt UNIT
IN dVdt dVdt 6800pF
2.7 V 6.26 1.39 0.68
SR Output Rising slew rate 12 V 7.35 1.4 0.68 V/ms
ON
24 V 7.4 1.4 0.68
2.7 V 1.3 1.49 1.7
t Turn on delay 12 V 1.24 2.1 3.01 ms
D,ON
24 V 1.2 2.91 4.74
2.7 V 0.67 1.63 3.35
t Rise time 12 V 1.35 6.99 14.41 ms
R
24 V 2.66 13.77 28.41
2.7 V 1.97 3.12 5.05
t Turn on time 12 V 2.59 9.09 17.42 ms
ON
24 V 3.86 16.68 33.15
2.7 V 151 152 152
t Turn off delay 12 V 212 212 212 us
D,OFF
24 V 262 262 262
10 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS25980
```

### Page 11

#### Extracted tables

Table 1:

```text
2.56 2.54 2.52 2.5 )V( PVUV 2.48 Rising 2.46 Falling 2.44 2.42 2.4 -40 -20 0 20 40 60 80 100 120 140 TJ (qC) D007 Figure 7-1. Supply UVP Threshold vs Temperature | 3.7 3.68 Rising 3.66 Falling )V( PVOV 3.64 3.62 3.6 3.58 -40 -20 0 20 40 60 80 100 120 140 TJ (qC) D001 TPS259802x Variants Figure 7-2. Supply OVP Threshold vs Temperature
7.625 7.6 7.575 Rising 7.55 Falling )V( 7.525 PVOV 7.5 7.475 7.45 7.425 7.4 7.375 -40 -20 0 20 40 60 80 100 120 140 TJ (qC) D003 TPS259803x Variants Figure 7-3. Supply OVP Threshold vs Temperature | 16.9 16.85 16.8 16.75 Rising 16.7 Falling )V( 16.65 PVOV 16.6 16.55 16.5 16.45 16.4 16.35 16.3 -40 -20 0 20 40 60 80 100 120 140 TJ (qC) D009 TPS259804x Variants Figure 7-4. Supply OVP Threshold vs Temperature
1.21 1.2 1.19 1.18 1.17 )V( 1.16 Rising OLVUV 1.15 Falling 1.14 1.13 1.12 1.11 1.1 -40 -20 0 20 40 60 80 100 120 140 TJ (qC) D008 Figure 7-5. EN/UVLO Threshold vs Temperature | 900 875 VI 2 N .7 V 850 12 V 24 V 825 800 )AP( 775 qI 750 725 700 675 650 -40 -20 0 20 40 60 80 100 120 140 TJ (qC) D002 V = 2 V, OUT = Open ENUVLO Figure 7-6. Quiescent Current vs Temperature
0.875 0.85 0.825 0.8 VI 3 N .3 V )V( 0.775 12 V 24 V )F(DSV 0.75 0.725 0.7 0.675 0.65 0.625 -40 -20 0 20 40 60 80 100 120 140 TJ (qC) D014 Figure 7-7. EN/UVLO Falling Threshold for Lowest Current Consumption | 240 235 VIN 230 2.7 V 225 12 V 220 24 V 215 210 )AP( 205 200 dsI 195 190 185 180 175 170 165 160 -40 -20 0 20 40 60 80 100 120 140 TJ(qC) D004 V = 1 V, OUT = Open ENUVLO Figure 7-8. Shut-Down Current vs Temperature
```

Table 2:

```text
|  |  |  |  |  |  | R | ising
 |  |  |  |  |  |  | F | alling
```

Table 3:

```text
|  |  |  |  |  |  |  | Rising
 |  |  |  |  |  |  |  | Falling
```

Table 4:

```text
|  |  |  |  |  |  |  | Rising
 |  |  |  |  |  |  |  | Falling
```

Table 5:

```text
|  |  |  |  |  |  |  | Rising
 |  |  |  |  |  |  |  | Falling
```

Table 6:

```text
|  |  |  |  |  |  | R | ising
 |  |  |  |  |  |  | F | alling
```

Table 7:

```text
VI | N |  |  |  |  |  |  | 
 | 2.7 V 12 V |  |  |  |  |  |  | 
 | 24 V |  |  |  |  |  |  |
```

Table 8:

```text
|  |  |  |  |  |  | V | IN
 |  |  |  |  |  |  |  | 3.3 V 12 V
 |  |  |  |  |  |  |  | 24 V
```

Table 9:

```text
VI | N 2.7 V |  |  |  |  |  |  | 
 | 12 V |  |  |  |  |  |  | 
 | 24 V |  |  |  |  |  |  |
```

#### Raw extracted text

```text
7.8 Typical Characteristics
TJ (qC)
)V(
PVUV
2.56
2.54
2.52
2.5
2.48
Rising
2.46 Falling
2.44
2.42 TJ (qC)
2.4
-40 -20 0 20 40 60 80 100 120 140
D007
Figure 7-1. Supply UVP Threshold vs Temperature
)V(
PVOV
3.7
3.68
Rising
3.66 Falling
3.64
3.62
3.6
3.58
-40 -20 0 20 40 60 80 100 120 140 D001
TPS259802x Variants
Figure 7-2. Supply OVP Threshold vs Temperature
TJ (qC)
)V(
PVOV
7.625
7.6
7.575
Rising
7.55 Falling
7.525
7.5
7.475
7.45
7.425
7.4
7.375
-40 -20 0 20 40 60 80 100 120 140
D003 TJ (qC)
TPS259803x Variants
Figure 7-3. Supply OVP Threshold vs Temperature
)V(
PVOV
16.9
16.85
16.8
16.75 Rising
16.7 Falling
16.65
16.6
16.55
16.5
16.45
16.4
16.35
16.3
-40 -20 0 20 40 60 80 100 120 140
D009
TPS259804x Variants
Figure 7-4. Supply OVP Threshold vs Temperature
TJ (qC)
)V(
OLVUV
1.21
1.2
1.19
1.18
1.17
1.16 Rising
1.15 Falling
1.14
1.13
1.12
1.11 TJ (qC)
1.1
-40 -20 0 20 40 60 80 100 120 140
D008
Figure 7-5. EN/UVLO Threshold vs Temperature
)AP(
qI
900
875 VI 2 N .7 V
850 12 V 24 V
825
800
775
750 725
700
675
650
-40 -20 0 20 40 60 80 100 120 140
D002
V = 2 V, OUT = Open
ENUVLO
Figure 7-6. Quiescent Current vs Temperature
TJ (qC)
)V(
)F(DSV
0.875
0.85
0.825
0.8 VI 3 N .3 V
0.775 12 V 24 V
0.75
0.725
0.7
0.675
0.65 TJ(qC)
0.625
-40 -20 0 20 40 60 80 100 120 140
D014
Figure 7-7. EN/UVLO Falling Threshold for Lowest
Current Consumption
)AP( dsI
TPS25980
www.ti.com SLVSFR1 - AUGUST 2020
240
235 VIN
230 2.7 V
225 12 V
220 24 V
215 210
205 200 195
190
185
180
175
170
165
160
-40 -20 0 20 40 60 80 100 120 140
D004
V = 1 V, OUT = Open
ENUVLO
Figure 7-8. Shut-Down Current vs Temperature
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 11
Product Folder Links: TPS25980
```

### Page 12

#### Extracted tables

Table 1:

```text
12 VIN 2.7 V 10 12 V 24 V 8 )AP( 6 dsI 4 2 0 -40 -20 0 20 40 60 80 100 120 140 TJ (qC) D005 V = 0 V, OUT = Open ENUVLO Figure 7-9. Deep Shut-Down Current vs Temperature | 9 8 7 6 )A( 5 MILI 4 3 2 1 0 180 360 540 720 900 1080 1260 1440 1620 1800 RILIM (:) D010 Figure 7-10. Output Current Limit (I ) vs R LIM ILIM
25 MIN 20 MAX 15 )%( 10 ycaruccA 5 0 -5 MILI -10 -15 -20 -25 2 3 4 5 6 7 8 ILIM (A) D011 Across Process, Voltage, Temperature Corners Figure 7-11. Output Current Limit (I ) Accuracy LIM | 900 IPG 850 26uA 242uA 800 750 )Vm( 700 GPV 650 600 550 500 -40 -20 0 20 40 60 80 100 120 140 TJ (qC) D015 V = 0 V IN Figure 7-12. Power Good Output Voltage (De- asserted State) vs Temperature
1.0025 1 0.9975 0.995 )V( 0.9925 REMITIV' 0.99 0.9875 0.985 0.9825 VIN 0.98 2.7 V 0.9775 1 2 2 4 V V 0.975 -40 -20 0 20 40 60 80 100 120 140 TJ (qC) D016 Figure 7-13. ITIMER Voltage Threshold Delta vs Temperature | 2.2 2.18 2.16 2.14 )AP( 2.12 2.1 REMITII 2.08 2.06 2.04 VIN 2.02 2.7 V 2 1 2 2 4 V V 1.98 -40 -20 0 20 40 60 80 100 120 140 TJ (qC) D019 Figure 7-14. ITIMER Discharge Current vs Temperature
2.16 2.14 2.12 2.1 )AP( 2.08 TRTSDLI 2.06 2.04 2.02 VIN 2.7 V 2 12 V 24 V 1.98 -40 -20 0 20 40 60 80 100 120 140 TJ (qC) D020 Figure 7-15. LDSTRT Charging Current vs Temperature | 1.215 VIN 2.7 V 1.213 12 V 24 V )V( 1.211 TRTSDLV 1.209 1.207 1.205 -40 -20 0 20 40 60 80 100 120 140 TJ (qC) D021 Figure 7-16. LDSTRT Threshold Voltage vs Temperature
```

Table 2:

```text
VIN 2 | .7 V |  |  |  |  |  |  | 
1 2 | 2 V 4 V |  |  |  |  |  |  |
```

Table 3:

```text
|  |  |  |  | MIN
 |  |  |  |  | MAX
```

Table 4:

```text
|  |  |  |  |  |  | IPG
 |  |  |  |  |  |  | 26uA 242u
```

Table 5:

```text
|  |  |  |  |  |  |  | VIN
 |  |  |  |  |  |  |  | 2.7 V 12 V
 |  |  |  |  |  |  |  | 24 V
```

Table 6:

```text
|  |  |  |  |  |  | VIN
 |  |  |  |  |  |  | 2.7 12
 |  |  |  |  |  |  | 24
```

Table 7:

```text
|  |  |  |  |  |  | V | IN
 |  |  |  |  |  |  |  | 2.7 V 12 V
 |  |  |  |  |  |  |  | 24 V
```

Table 8:

```text
|  |  |  |  |  |  | VIN 2.7 12
 |  |  |  |  |  |  | 24
```

#### Raw extracted text

```text
TJ (qC)
)AP(
dsI
12
VIN
2.7 V 10 12 V
24 V
8
6
4
2
0
-40 -20 0 20 40 60 80 100 120 140 D005
V = 0 V, OUT = Open
ENUVLO
Figure 7-9. Deep Shut-Down Current vs
RILIM (:)
Temperature
)A(
MILI
9
8
7
6
5
4
3
2
1
0
180 360 540 720 900 1080 1260 1440 1620 1800
D010
Figure 7-10. Output Current Limit (I ) vs R
LIM ILIM
ILIM (A)
)%(
ycaruccA
MILI
25
MIN
20 MAX
15
10
5
0
-5
-10
-15
-20
-25
2 3 4 5 6 7 8
D011 TJ (qC)
Across Process, Voltage, Temperature Corners
Figure 7-11. Output Current Limit (I ) Accuracy LIM
)Vm(
GPV
900
IPG
850 26uA
242uA
800
750
700
650
600
550
500
-40 -20 0 20 40 60 80 100 120 140
D015
V = 0 V
IN
Figure 7-12. Power Good Output Voltage (De-
asserted State) vs Temperature
TJ (qC)
)V(
REMITIV'
1.0025
1
0.9975
0.995
0.9925
0.99
0.9875
0.985
0.9825
VIN
0.98 2.7 V
0.9775 1 2 2 4 V V
0.975
-40 -20 0 20 40 60 80 100 120 140
D016 TJ (qC)
Figure 7-13. ITIMER Voltage Threshold Delta vs
Temperature
)AP(
REMITII
2.2
2.18
2.16
2.14
2.12
2.1
2.08
2.06
2.04
VIN
2.02 2.7 V
2 1 2 2 4 V V
1.98
-40 -20 0 20 40 60 80 100 120 140
D019
Figure 7-14. ITIMER Discharge Current vs
Temperature
TJ (qC)
)AP(
TRTSDLI
2.16
2.14
2.12
2.1
2.08
2.06
2.04
2.02 VIN 2.7 V
2 12 V
24 V
1.98
-40 -20 0 20 40 60 80 100 120 140
D020 TJ (qC)
Figure 7-15. LDSTRT Charging Current vs
Temperature
)V(
TRTSDLV
TPS25980
SLVSFR1 - AUGUST 2020 www.ti.com
1.215
VIN
2.7 V
1.213 12 V 24 V
1.211
1.209
1.207
1.205
-40 -20 0 20 40 60 80 100 120 140
D021
Figure 7-16. LDSTRT Threshold Voltage vs
Temperature
12 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS25980
```

### Page 13

#### Extracted tables

Table 1:

```text
5 4.8 )AP( 4.6 TDVDI 4.4 4.2 VI 2 N .7 V 12 V 24 V 4 -40 -20 0 20 40 60 80 100 120 140 TJ (qC) D022 Figure 7-17. DVDT Charging Current vs Temperature | 2.16 2.14 VI 2 N .7 V 12 V 2.12 24 V )AP( 2.1 YLD_YRTERI 2.08 2.06 2.04 2.02 2 1.98 -40 -20 0 20 40 60 80 100 120 140 TJ (qC) D024 Figure 7-18. RETRY_DLY Bias Current vs Temperature
0.76 0.758 VI 2 N .7 V 0.756 12 V 24 V )V( 0.754 SYH_YLD_YRTERV 0.752 0.75 0.748 0.746 0.744 0.742 0.74 -40 -20 0 20 40 60 80 100 120 140 TJ (qC) D025 Figure 7-19. RETRY_DLY Oscillator Hysteresis vs Temperature | 2.14 2.12 2.1 2.08 )AP( 2.06 YRTERNI 2.04 2.02 2 VIN 2.7 V 1.98 12 V 24 V 1.96 -40 -20 0 20 40 60 80 100 120 140 TJ (qC) D027 Figure 7-20. NRETRY Bias Current vs Temperature
0.76 VIN 0.755 3.3 V 12 V 0.75 24 V )V( 0.745 SYH_YRTERNV 0.74 0.735 0.73 0.725 0.72 -40 -20 0 20 40 60 80 100 120 140 TJ (qC) D026 Figure 7-21. NRETRY Oscillator Hysteresis vs Temperature | 1000 )sm( 500 T -4 A 0 qC 300 27 qC nwodtuhS 200 85 qC 125 qC 100 50 lamrehT 30 20 10 ot emiT 5 3 2 1 0 4 8 12 16 20 24 28 32 36 40 Power Dissipation (W) D023 Figure 7-22. Thermal Shutdown Plot - Steady State
200 TPS259807x 100 TPS259802x/03x/04x )sm( 50 nwodtuhS 30 20 lamrehT 10 5 ot 3 emiT 2 1 0.5 2 3 4 5 678 10 20 30 4050 70 100 Power Dissipation (W) D002 Figure 7-23. Thermal Shutdown Plot - Inrush/Overload |
```

Table 2:

```text
|  |  |  |  |  |  | VI | N
 |  |  |  |  |  |  |  | 2.7 V 12 V 24 V
```

Table 3:

```text
VI | N |  |  |  |  |  |  | 
 | 2.7 V 12 V |  |  |  |  |  |  | 
 | 24 V |  |  |  |  |  |  |
```

Table 4:

```text
|  |  |  |  |  |  | V | IN
 |  |  |  |  |  |  |  | 2.7 V 12 V
 |  |  |  |  |  |  |  | 24 V
```

Table 5:

```text
|  |  |  |  |  |  | V | IN
 |  |  |  |  |  |  |  | 2.7 V 12 V
 |  |  |  |  |  |  |  | 24 V
```

Table 6:

```text
|  |  |  |  |  |  | V | IN 3.3 V 12 V
 |  |  |  |  |  |  |  | 24 V
```

Table 7:

```text
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | T | 4 A 0 q q | C
 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 2 | 7 q | C
 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 8 1 | 5 25 | C qC
```

Table 8:

```text
|  |  |  |  |  |  |  |  |  | TP TP | S259 S259 | 807 802 | x x/0 | 3x | /0 | 4x
```

#### Raw extracted text

```text
TJ (qC)
)AP(
TDVDI
5
4.8
4.6
4.4
4.2 VI 2 N .7 V
12 V
24 V
4
-40 -20 0 20 40 60 80 100 120 140
D022 TJ (qC)
Figure 7-17. DVDT Charging Current vs
Temperature
)AP(
YLD_YRTERI
2.16
2.14 VI 2 N .7 V
12 V 2.12 24 V
2.1
2.08
2.06
2.04
2.02
2
1.98
-40 -20 0 20 40 60 80 100 120 140
D024
Figure 7-18. RETRY_DLY Bias Current vs
Temperature
TJ (qC)
)V(
SYH_YLD_YRTERV
0.76
0.758 VI 2 N .7 V
0.756 12 V 24 V
0.754
0.752
0.75
0.748
0.746
0.744
0.742
0.74
-40 -20 0 20 40 60 80 100 120 140
D025 TJ (qC)
Figure 7-19. RETRY_DLY Oscillator Hysteresis vs
Temperature
)AP(
YRTERNI
2.14
2.12
2.1
2.08
2.06
2.04
2.02
2 VIN 2.7 V
1.98 12 V
24 V
1.96
-40 -20 0 20 40 60 80 100 120 140
D027
Figure 7-20. NRETRY Bias Current vs Temperature
TJ (qC)
)V(
SYH_YRTERNV
0.76
VIN 0.755 3.3 V 12 V
0.75 24 V
0.745
0.74
0.735
0.73
0.725
0.72
-40 -20 0 20 40 60 80 100 120 140
D026 Power Dissipation (W)
Figure 7-21. NRETRY Oscillator Hysteresis vs
Temperature
)sm(
nwodtuhS
lamrehT
ot emiT
1000
500 T -4 A 0 qC 300 27 qC
200 85 qC 125 qC
100
50
30
20
10
5
3 2
1
0 4 8 12 16 20 24 28 32 36 40
D023
Figure 7-22. Thermal Shutdown Plot - Steady State
Power Dissipation (W)
)sm(
nwodtuhS
lamrehT
ot
emiT
TPS25980
www.ti.com SLVSFR1 - AUGUST 2020
200
TPS259807x
100 TPS259802x/03x/04x
50
30
20
10
5
3
2
1
0.5
2 3 4 5 678 10 20 30 4050 70 100
D002
Figure 7-23. Thermal Shutdown Plot - Inrush/Overload
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 13
Product Folder Links: TPS25980
```

### Page 14

#### Extracted tables

Table 1:

```text
C = 1 uF C = 220 uF C = 3.3 nF IN OUT dVdt Figure 7-24. Hotplug | C = 220 uF C = 10 nF R = Open OUT dVdt OUT Figure 7-25. Startup With EN - dVdt Limited
C = 220 uF C = 3.3 nF R = 6 Ohm OUT dVdt OUT Figure 7-26. Startup With EN Into Resistive Load - dVdt Limited | TPS259804x (16.7-V OVP variant) Figure 7-27. Overvoltage Protection
R = 182 Ohm C = 4.7 nF ILIM ITIMER Figure 7-28. Circuit Breaker With Transient Overcurrent Blanking | A. R = 182 Ohm C = 4.7 nF C = 2.2 nF, ILIM ITIMER RETRY_DLY C = 2.2 nF NRETRY Figure 7-29. Circuit Breaker - Auto-Retry
```

#### Raw extracted text

```text
TPS25980
SLVSFR1 - AUGUST 2020 www.ti.com
C = 1 uF C = 220 uF C = 3.3 nF C = 220 uF C = 10 nF R = Open
IN OUT dVdt OUT dVdt OUT
Figure 7-24. Hotplug Figure 7-25. Startup With EN - dVdt Limited
C = 220 uF C = 3.3 nF R = 6 Ohm TPS259804x (16.7-V OVP
OUT dVdt OUT
Figure 7-26. Startup With EN Into Resistive Load - variant)
dVdt Limited Figure 7-27. Overvoltage Protection
R = 182 Ohm C = 4.7 nF A. R = 182 Ohm C = 4.7 nF C = 2.2 nF,
ILIM ITIMER ILIM ITIMER RETRY_DLY
C = 2.2 nF
Figure 7-28. Circuit Breaker With Transient NRETRY
Overcurrent Blanking Figure 7-29. Circuit Breaker - Auto-Retry
14 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS25980
```

### Page 15

#### Extracted tables

Table 1:

```text
R = 182 Ohm ILIM Figure 7-30. Power Up Into Output Short-Circuit | R = 182 Ohm ILIM Figure 7-31. Output Hard Short-Circuit While ON
R = 182 Ohm ILIM Figure 7-32. Output Hard Short-Circuit While ON (Zoomed In) | R = 332 Ohm ILIM Figure 7-33. Supply Line Transient Immunity - Input Voltage Step
R = 511 Ohm ILIM Figure 7-34. Supply Line Transient Immunity - Adjacent Load Hot Unplug |
```

#### Raw extracted text

```text
TPS25980
www.ti.com SLVSFR1 - AUGUST 2020
R = 182 Ohm R = 182 Ohm
ILIM ILIM
Figure 7-30. Power Up Into Output Short-Circuit Figure 7-31. Output Hard Short-Circuit While ON
R = 182 Ohm
ILIM R = 332 Ohm
ILIM
Figure 7-32. Output Hard Short-Circuit While ON
Figure 7-33. Supply Line Transient Immunity -
(Zoomed In)
Input Voltage Step
R = 511 Ohm
ILIM
Figure 7-34. Supply Line Transient Immunity - Adjacent Load Hot Unplug
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 15
Product Folder Links: TPS25980
```

### Page 16

#### Raw extracted text

```text
TPS25980
SLVSFR1 - AUGUST 2020 www.ti.com
8 Detailed Description
8.1 Overview
The TPS25980x device is a smart eFuse with integrated power switch that is used to manage load voltage and
load current. The device starts its operation by monitoring the IN bus. When V is above the Undervoltage
IN
Protection threshold (V ) and below the Overvoltage Protection threshold (V ), the device samples the
UVP OVP
EN/UVLO pin. A high level on this pin enables the internal MOSFET to start conducting and allow current to
flow from IN to OUT. When EN/UVLO is held low, the internal MOSFET is turned off. After a successful start-up
sequence, the device now actively monitors its load current, input voltage and protects the load from harmful
overcurrent and overvoltage conditions. The device also relies on a built-in thermal sense circuit to shut down
and protect itself in case the device internal temperature (T ) exceeds the safe operating conditions.
J
8.2 Functional Block Diagram
8.3 Feature Description
The TPS25980x eFuse is a compact, feature rich power management device that provides detection, protection
and indication in the event of system faults.
16 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS25980
```

### Page 17

#### Raw extracted text

```text
TPS25980
www.ti.com SLVSFR1 - AUGUST 2020
8.3.1 Undervoltage Protection (UVLO and UVP)
The TPS25980x implements Undervoltage Protection on IN to turn off the output in case the applied voltage
becomes too low for the downstream load or the device to operate correctly. The Undervoltage Protection has
a default internal threshold of V . If needed, it is also possible to set a user defined Undervoltage Protection
UVP
threshold higher than V using the UVLO comparator on the EN/UVLO pin. Figure 8-1 and Equation 1 show
UVP
how a resistor divider from supply to GND can be used to set the UVLO set point for a given voltage supply
level.
Power
IN
Supply
RVL1
EN/UVLO
RVL2
GND
Figure 8-1. Adjustable Supply UVLO Threshold
VUVLO(R) x (RVL1 (cid:14)RVL2)
VINUVLO =
RVL2 (1)
The resistors must be sized large enough to minimize the constant leakage from supply to ground through the
resistor divider network. At the same time, keep the current through the resistor network sufficiently larger (20x)
than the leakage current on the EN/UVLO pin to minimize the error in the resistor divider ratio.
8.3.2 Overvoltage Protection (OVP)
The TPS25980x implements Overvoltage Lock-Out (OVLO) on IN to protect the output load in the event of input
overvoltage. When the input exceeds the Overvoltage Protection threshold (V ) the device turns off the
OVP(R)
output within t . As long as an overvoltage condition is present on the input, the device stays disabled and the
OVP
output will be turned off. Once the input voltage returns to the normal operating range, the device attempts to
start up normally.
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 17
Product Folder Links: TPS25980
```

### Page 18

#### Raw extracted text

```text
TPS25980
SLVSFR1 - AUGUST 2020 www.ti.com
Input Overvoltage Event Input Overvoltage Removed
V
IN OVP(R)
V
OVP(F)
0
t
OVP
OUT
dVdt Limited
0
V
PG PG
0
Time
Figure 8-2. Overvoltage Response
There are multiple device options with different fixed overvoltage thresholds to choose from, including one
without internal overvoltage protection. See the Device Comparison Table for a list of available options.
8.3.3 Inrush Current, Overcurrent, and Short-Circuit Protection
TPS25980x devices incorporate three levels of protection against overcurrent:
* Adjustable slew rate (dVdt) for inrush current control
* Adjustable overcurrent protection (with adjustable blanking timer) - Circuit Breaker to protect against soft
overload conditions
* Adjustable fast-trip response to quickly protect against severe overcurrent (short-circuit) faults
8.3.3.1 Slew Rate and Inrush Current Control (dVdt)
During hot-plug events or while trying to charge a large output capacitance, there can be a large inrush current.
If the inrush current is not controlled, it can damage the input connectors and/or cause the system power supply
to droop leading to unexpected restarts elsewhere in the system. The TPS25980x provides integrated output
slew rate (dVdt) control to manage the inrush current during start-up. The inrush current is directly proportional
to the load capacitance and rising slew rate. The following equation can be used to calculate the slew rate (SR)
required to limit the inrush current (I ) for a given load capacitance (C ):
INRUSH OUT
IINRUSH(cid:11)mA(cid:12)
SR(cid:11)V/ms(cid:12)
COUT(cid:11)PF(cid:12)
(2)
An external capacitance can be connected to the dVdt pin to control the rising slew rate and lower the inrush
current during turn on. The required C capacitance to produce a given slew rate can be calculated using the
dVdt
following formula:
4600
CdVdt (cid:11)pF(cid:12)
SR(cid:11)V/ms(cid:12)
(3)
The fastest output slew rate is achieved by leaving the dVdt pin open.
18 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS25980
```

### Page 19

#### Extracted tables

Table 1:

```text
| Overload Removed |  | 
 |  | 4V ITIMER | t ITIMER
```

#### Raw extracted text

```text
TPS25980
www.ti.com SLVSFR1 - AUGUST 2020
8.3.3.2 Circuit Breaker
The TPS25980x responds to output overcurrent conditions by turning off the output after a user adjustable
transient fault blanking interval. When the load current exceeds the programmed current limit threshold (I set
LIM
by the ILIM pin resistor R ), but lower than the fast-trip threshold (2.1 x I ), the device starts discharging
ILIM LIM
the ITIMER pin capacitor using an internal pull-down current (I ). If the load current drops below the current
ITIMER
limit threshold before the ITIMER capacitor drops by V , the circuit breaker action is not engaged and the
ITIMER
ITIMER is reset by pulling it up to V internally. This allows short transient overcurrent pulses to pass through
INT
the device without tripping the circuit. If the overcurrent condition persists, the ITIMER capacitor continues to
discharge and once it falls by V , the circuit breaker action turns off the FET immediately. The following
ITIMER
equation can be used to calculate the R value for a desired current limit threshold.
ILIM
1460
RILIM(cid:11):(cid:12)
ILIM(cid:11)A(cid:12)(cid:16)0.11
(4)
Note
Leaving the ILIM pin Open sets the current limit to zero and causes the FET to shut off as soon as
any load current is detected. Shorting the ILIM pin to ground at any point during normal operation
is detected as a fault and the part shuts down. The ILIM pin Short to GND fault detection circuit
requires a minimum amount of load current (I ) to flow through the device. This ensures robust
CB
eFuse behavior even under single point failure conditions. Refer to the Fault Response section for
details on the device behavior after a fault.
Transient Output Overload Persistent Output Overload ITIMER expired
2.1 x I
LIM Overload Removed
I OUT I LIM
Circuit Breaker
operation
0
t
ITIMER
V
INT
4V
ITIMER
ITIMER
0
V
IN
OUT
0
V
PG
PG
0
TSD
TSD
HYS
T
J
T
J
Time
Figure 8-3. Circuit Breaker Response
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 19
Product Folder Links: TPS25980
```

### Page 20

#### Extracted tables

Table 1:

```text
ITIMER Pin Connection | Timer Delay before Overcurrent response
OPEN | 0 s
Capacitor to ground | As per Equation 5
Short to GND | ITIMER Pin Fault - Part Shuts Off
```

#### Raw extracted text

```text
The duration for which load transients are allowed can be adjusted using an appropriate capacitor value from
ITIMER pin to ground. The transient overcurrent blanking interval can be calculated using Equation 5.
ITIMER ITIMER
ITIMER  =
ITIMER
C (nF)  V (V)t (ms) I ( A)
u '
P
(5)
Leave the ITIMER pin open to allow the part to break the circuit with the minimum possible delay.
Table 8-1. Device ITIMER Functional Mode Summary
ITIMER Pin Connection Timer Delay before Overcurrent response
OPEN 0 s
Capacitor to ground As per Equation 5
Short to GND ITIMER Pin Fault - Part Shuts Off
Note
1. Shorting the ITIMER pin to ground is detected as a fault and the part shuts down. This ensures
robust eFuse behavior even in case of single point failure conditions. Refer to the Fault Response
section for details on the device behavior after a fault.
2. Larger ITIMER capacitors take longer to charge during start-up and may lead to incorrect fault
assertion if the ITIMER voltage is still below the pin short detection threshold after the device has
reached steady state. To avoid this, it is recommended to limit the maximum ITIMER capacitor to the
value suggested by the equation below.
53000
GHI
ITIMER

tC <
IN
GHI  D,ON  dvdt
dvdt
V + 3.6Vt = t + C I
  u
 1
Where
* tGHI is the time taken by the device to reach steady state
* tD,ON is the device turn-on delay
* Cdvdt is the dVdt capacitance
* Idvdt is the dVdt charging current
It is possible to avoid incorrect ITIMER pin fault assertion and achieve higher ITIMER intervals if
needed by increasing the dVdt capacitor value accordingly, but at the expense of higher start-up time.
Once the part shuts down due to a Circuit Breaker fault, it can be configured to either stay latched off or restart
automatically. Refer to the Fault Response section for details.
8.3.3.3 Short-Circuit Protection
During an output short-circuit event, the current through the device increases very rapidly. When an output
short-circuit is detected, the internal fast-trip comparator turns off the output within the t SC. The comparator
employs a scalable threshold which is equal to 2.1 x I LIM. This enables the user to adjust the fast-trip threshold
as per system needs rather than using a fixed threshold which may not be suitable for all systems. After a fast
trip event, the device restarts in a current limited mode to try and restore power to the load quickly in case the
fast trip was triggered by a transient event. However, if the fault is persistent, the device will stay in current
limit causing the junction temperature to rise and eventually enter thermal shutdown. See Overtemperature
Protection (OTP) section for details on the device response to overtemperature.
In some of the systems, for example servers or telecom equipment which house multiple hot-pluggable cards
connected to a common supply backplane, there can be transients on the supply due to switching of large
currents through the inductive backplane. This can result in current spikes on adjacent cards which could
TPS25980
SLVSFR1 - AUGUST 2020 www.ti.com
20 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS25980
```

### Page 21

#### Extracted tables

Table 1:

```text
|  | t SC | t SC |  |  |  | 
 | No Fast-trip |  |  |  |  |  | 
 |  |  |  |  | t RETRY_DLY |  | 
 |  |  |  |  |  | TSD HYS |
```

#### Raw extracted text

```text
TPS25980
www.ti.com SLVSFR1 - AUGUST 2020
be potentially large enough to inadvertently trigger the fast-trip comparator of the eFuse. The TPS25980x
uses a proprietary algorithm to avoid nuisance tripping in such cases thereby facilitating un-interrupted system
operation.
Input Line Temporary Output Persistent Output Short-Circuit
Transient Short-Circuit Thermal Shutdown
Output Short-Circuit Removed
Retry Timer Elapsed
IN
0
t t
SC SC
2.1 x I
LIM
I OUT I LIM
0
No Fast-trip Fast-trip Fast-trip
V
IN
OUT
Current Limited dVdt Limited
0
Start-up Start-up
V
PG
PG
t
RETRY_DLY
0
TSD
TSD
HYS
T
J
Time
Figure 8-4. Input Line Transient and Output Short-Circuit Response
Note
To prevent the circuit breaker loop from interfering with the input line transient detection logic, TI
recommends to set the ITIMER interval higher than 100 us. Refer to Table 8-1 for more details on
ITIMER.
8.3.4 Overtemperature Protection (OTP)
The device monitors the internal die temperature (T ) at all times and shuts down the part as soon as the
J
temperature exceeds a safe operating level (TSD) thereby protecting the device from damage. The device will
not turn back on until the die cools down sufficiently, that is the die temperature falls below (TSD - TSDHys).
Thereafter, the part can be configured to either remain latched off or restart automatically. Refer to the Fault
Response section for details.
8.3.5 Analog Load Current Monitor (IMON)
The device allows the system to monitor the output load current accurately by providing an analog current on
the IMON pin which is proportional to the current through the FET. The user can connect a resistor from IMON
to ground to convert this signal to a voltage which can be fed to the input of an Analog-to-Digital Converter.
The internal amplifier on the IMON employs chopper based offset cancellation techniques to provide accurate
measurement even at lower currents over time and temperature.
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 21
Product Folder Links: TPS25980
```

### Page 22

#### Extracted tables

Table 1:

```text
V IN | Recommended V IMON(MAX)
2.7 V | 1 V
3.3 V | 1.8 V
> 5 V | 3.3 V
```

Table 2:

```text
| Slew rate (dVdt) controlled startup/Inrush current limiting |  |  |  | Current limiting VPGTHD operation 120 us |  | 
 |  |  | 120 us |  | VPGTHD |  | 
 |  |  |  |  | tITIMER |  |
```

#### Raw extracted text

```text
TPS25980
SLVSFR1 - AUGUST 2020 www.ti.com
V (cid:11)V(cid:12) G (cid:11)PA/A(cid:12)uI (cid:11)A(cid:12)uR (cid:11):(cid:12)
IMON IMON OUT IMON (6)
It is recommended to limit the maximum IMON voltage to the values mentioned in VIMON(Max) Recommended
Values . This is to ensure the IMON pin internal amplifier has sufficient headroom to operate linearly.
Table 8-2. V Recommended Values
IMON(MAX)
V Recommended V
IN IMON(MAX)
2.7 V 1 V
3.3 V 1.8 V
> 5 V 3.3 V
It is recommended to add a RC low pass filter on the IMON output to filter out any glitches and get a smooth
average current measurement. TI recommends a series resistance of 10 kOhm or higher.
8.3.6 Power Good (PG)
PG is an active high open drain output which indicates whether the FET is fully turned ON and the output voltage
has reached the maximum value. After power-up, PG is pulled low initially. The gate driver circuit starts charging
the gate capacitance from the internal charge pump. When the FET gate voltage reaches (V + 3.6V), PG is
IN
asserted after a de-glitch time (t ). During normal operation, if at any time V falls below (V - V ), PG
PGD OUT IN PGTHD
is de-asserted after a de-glitch time (t ).
PGD
Device Enabled Overcurrent Event Overcurrent Removed
EN/UVLO
VUVLO(R)
0
IN
Slew rate (dVdt) controlled
0 startup/Inrush current limiting
VIN
VPGTHD
Cur
o
r
p
e
e
n
r
t
a
li
t
m
io
i
n
ting
OUT
0
VPG
PG 120 us 120 us 120 us
0
VIN
dVdT
0
VIN + 3.6V
VGate
0
tITIMER
ILIM
IINRUSH
IOUT
0
Time
Figure 8-5. Power Good Assertion and De-assertion
22 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS25980
```

### Page 23

#### Extracted tables

Table 1:

```text
| tLDSTRT
```

Table 2:

```text
| tLDSTRT
```

#### Raw extracted text

```text
TPS25980
www.ti.com SLVSFR1 - AUGUST 2020
Note
1. When there is no supply to the device, the PG pin is expected to stay low. However, there is no
active pull-down in this condition to drive this pin all the way down to 0 V. If the PG pin is pulled up
to an independent supply which is present even if the TPS25980x is unpowered, there can be a small
voltage seen on this pin depending on the pin sink current, which in turn is a function of the pull-up
supply voltage and resistor. Minimize the sink current to keep this pin voltage low enough not to be
detected as a logic HIGH by associated external circuits in this condition.
2. The PG pin provides a mechanism to detect a possible failed MOSFET condition during start-up.
If the PG does not get asserted for an extended period of time after the device is powered up and
enabled, it might be an indication of internal MOSFET failure.
8.3.7 Load Detect/Handshake (LDSTRT)
The LDSTRT pin provides a mechanism for the downstream load circuit to indicate to the TPS25980x that the
load is present and has powered up successfully. This allows the system to have additional control over the
conditions in which power is presented to the load and disconnect the power when the load is not present or
unable to provide a valid handshake signal after an expected boot-up time.
Once the TPS25980x completes the startup sequence and the output reaches the full voltage, it asserts the
PG signal. At the same time, it also starts charging the capacitor on the LDSTRT pin (C ) with an internal
LDSTRT
current source (I ). If the LDSTRT pin voltage rises above V before the load circuit pulls it low, the
LDSTRT LDSTRT
TPS25980x detects the condition as a LDSTRT fault and turns off the FET to power down the load. The time to
trigger the LDSTRT fault can be calculated from the following equation:
CLDSTRT (nF) u VLDSTRT (V)
tLDSTRT (ms) =
ILDSTRT (PA)
(7)
During normal operation, if at any time the load circuit releases the active pull-down on the LDSTRT pin, the
capacitor C would start charging up again and eventually trigger a shutdown due to LDSTRT fault once
LDSTRT
the capacitor charges up to V .
LDSTRT
Once the TPS25980x turns off due to LDSTRT fault, it can be turned ON again in 3 ways:
* LDSTRT pin is driven low
* Input supply voltage is driven low (< V ) and then driven high (> V )
UVP(F) UVP(R)
* EN/UVLO voltage is driven low (< V ) and then driven high (> V )
SD UVLO(R)
Tie the LDSTRT pin to ground if this functionality is not needed.
IN IN
0 0
EN/UVLO EN/UVLO
0 0
VIN VIN
OUT OUT
0 0
VPG VPG
PG PG
0 0
tLDSTRT tLDSTRT
1.2 V 2.5 V
LDSTRT 0 LDSTRT pulled low by MCU LDSTRT 1.2 0 V No Handshake Signal from System MCU
Time Time
Figure 8-6. Successful LDSTRT Handshake Figure 8-7. Unsuccessful LDSTRT Handshake
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 23
Product Folder Links: TPS25980
```

### Page 24

#### Raw extracted text

```text
TPS25980
SLVSFR1 - AUGUST 2020 www.ti.com
The LDSTRT pin can also be used to implement a load or module detect function wherein the output power is
presented only when the load or module is plugged in. A typical use case for this function is on optical module
power supply rails in Switches/Routers or similar networking end equipment. The LDSTRT pin should be tied
to a corresponding pin on the module connector which gets pulled low by the module when it is plugged in. An
example of such a signal is ModPrsL on QSFP-DD modules.
In this scheme, initially when the TPS25980x is powered up or enabled, the output charges up and PG is
asserted. If the module is not plugged in, there is no external pull-down on the LDSTRT pin and the pin voltage
starts rising due to internal pull-up . Once the LDSTRT pin voltage exceeds V , the TPS25980x turns
LDSTRT
off the output power. If the module is plugged in later, the LDSTRT pin is pulled low by the module and the
TPS25980x turns on the output power.
IN
0
EN/UVLO
0
V
IN
OUT
dVdt limited
0
V
PG
PG
0
2.5 V
LDSTRT
1.2 V
Optical module not present Optical module plugged in
0
Time
Figure 8-8. Optical Module Plug-In Detection Using LDSTRT
8.4 Fault Response
The following events trigger an internal fault which causes the device to shut down:
* Overtemperature Protection
* Circuit Breaker Operation
* ITIMER pin Short to GND
* ILIM pin Short to GND
Once the device shuts down due to a fault, even if the associated external fault is subsequently cleared, the
fault stays latched internally and the output cannot turn on again until the latch is reset. The fault latch can be
externally reset by one of the following methods:
* Input supply voltage is driven low (< V )
UVP(F)
* EN/UVLO voltage is driven low (< V )
SD
The fault latch can also be reset by an internal auto-retry logic. The user can either disable the auto-retry
behavior completely (latch-off behavior) or configure the device to auto-retry indefinitely or for a limited number
of times before latching off. The auto-retry behavior is controlled by the connections on the RETRY_DLY and
NRETRY pins.
24 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS25980
```

### Page 25

#### Extracted tables

Table 1:

```text
EN/UVLO | RETRY_DLY | NRETRY | DEVICE STATE
L | X | X | Disabled
H | Short to GND | X | No auto-retry (Latch-off)
H | Open | Open | Auto-retry 4 times with minimum delay between retries and then latch-off
H | Open | Short to GND | Auto-retry indefinitely with minimum delay between retries
H | Capacitor to GND | Capacitor to GND | Auto-retry delay and count as per Equation 8 and Equation 9
H | Capacitor to GND | Open | Auto-retry 4 times with finite delay between retries as per Equation 8 and then latch-off
H | Capacitor to GND | Short to GND | Auto-retry indefinitely with finite delay between retries as per Equation 8
```

Table 2:

```text
NRETRY Calculated From Equation 9 | NRETRY Actual
0 < N < 4 | 4
4 < N < 16 | 16
16 < N < 64 | 64
64 < N < 256 | 256
256 < N < 1024 | 1024
```

Table 3:

```text
Auto Retry Delay | 915 ms | 416 ms | 91.7 ms | 9.3 ms | 3 ms
RETRY_DLY Capacitor | 22 nF | 10 nF | 2.2 nF | 220 pF | 68 pF
No. of Auto Retries | NRETRY Capacitor |  |  |  | 
4 | Open |  |  |  | 
16 | 47 nF | 22 nF | 4.7 nF | 1 nF | 220 pF
64 | 0.22 uF | 0.1 uF | 22 nF | 2.2 nF | 1 nF
256 | 1 uF | 0.47 uF | 0.1 uF | 10 nF | 4.7 nF
1024 | 3.3 uF | 1.5 uF | 0.47 uF | 33 nF | 10 nF
Infinite | Short to GND |  |  |  |
```

#### Raw extracted text

```text
Table 8-3. Pin Configurable Fault Response
EN/UVLO RETRY_DLY NRETRY DEVICE STATE
L X X Disabled
H Short to GND X No auto-retry (Latch-off)
H Open Open Auto-retry 4 times with minimum delay between retries and
then latch-off
H Open Short to GND Auto-retry indefinitely with minimum delay between retries
H Capacitor to GND Capacitor to GND Auto-retry delay and count as per Equation 8 and Equation 9
H Capacitor to GND Open Auto-retry 4 times with finite delay between retries as per
Equation 8 and then latch-off
H Capacitor to GND Short to GND Auto-retry indefinitely with finite delay between retries as per
Equation 8
To configure the part for a finite number of auto-retries with a finite auto-retry delay, first choose the capacitor
value on RETRY_DLY pin using the following equation.
 128 4 RETRY_DLY RETRY_DLY_HYS
RETRY_DLY
RETRY_DLY
C (pF) +  pF V (V)t ( s) = I ( A)
u u P P
(8)
Next, choose the capacitor value on the NRETRY pin using the following equation.
 
4 RETRY_DLY NRETRY
RETRY
NRETRY RETRY_DLY
I ( A) C (pF)N = I ( A) C (pF) + 4 pF
u P u
P u
(9)
The number of auto-retries is quantized to certain discrete levels as shown in Table 8-4 .
Table 8-4. NRETRY Quantization Levels
NRETRY Calculated From Equation 9 NRETRY Actual
0 < N < 4 4
4 < N < 16 16
16 < N < 64 64
64 < N < 256 256
256 < N < 1024 1024
Table 8-5. NRETRY and RETRY_DLY Combination Examples
Auto Retry Delay 915 ms 416 ms 91.7 ms 9.3 ms 3 ms
RETRY_DLY Capacitor 22 nF 10 nF 2.2 nF 220 pF 68 pF
No. of Auto Retries NRETRY Capacitor
4 Open
16 47 nF 22 nF 4.7 nF 1 nF 220 pF
64 0.22 uF 0.1 uF 22 nF 2.2 nF 1 nF
256 1 uF 0.47 uF 0.1 uF 10 nF 4.7 nF
1024 3.3 uF 1.5 uF 0.47 uF 33 nF 10 nF
Infinite Short to GND
A spreadsheet design tool TPS25980xx Design Calculator is also available for simplified calculations.
www.ti.com
TPS25980
SLVSFR1 - AUGUST 2020
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 25
Product Folder Links: TPS25980
```

### Page 26

#### Raw extracted text

```text
TPS25980
SLVSFR1 - AUGUST 2020 www.ti.com
Output overload followed by Thermal Shutdown
Retry Timer starts once device cools down
1st Retry Nth Retry
IN
0 t
RETRY_DLY
Thermal Shutdown Thermal Shutdown
I OUT I LIM
0
V
IN
OUT Programmed number of retries over,
Device Latches Off
0
TSD
TSD
HYS
T
J
T
J
Time
Figure 8-9. Auto-Retry After Fault
The auto-retry logic has a mechanism to reset the count to zero if two consecutive faults occur far apart in
time. This ensures that the auto-retry response to any later fault is handled as a fresh sequence and not as a
continuation of the previous fault. If the fault which triggered the shutdown and subsequent auto-retry cycle is
cleared eventually and does not occur again for a duration equal to 7 retry delay timer periods starting from the
last fault, the auto-retry logic resets the internal auto-retry count to zero.
26 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS25980
```

### Page 27

#### Extracted tables

Table 1:

```text
EN/UVLO | LDSTRT | DEVICE STATE
L | X | Disabled
H | L | ON
H | H | OFF
```

Table 2:

```text
EN/UVLO | RETRY_DLY | NRETRY | DEVICE STATE
L | X | X | Disabled
H | Short to GND | X | No auto-retry (Latch-off)
H | Open | Open | Auto-retry 4 times with minimum delay between retries and then latch-off
H | Open | Short to GND | Auto-retry indefinitely with minimum delay between retries
H | Capacitor to GND | Capacitor to GND | Auto-retry delay and count as per Equation 8 and Equation 9
H | Capacitor to GND | Open | Auto-retry 4 times with finite delay between retries as per Equation 8 and then latch-off
H | Capacitor to GND | Short to GND | Auto-retry indefinitely with finite delay between retries as per Equation 8
```

#### Raw extracted text

```text
8.5 Device Functional Modes
The TPS25980x can be pin strapped to support various configurable functional modes.
Table 8-6. LDSTRT Handshake Functional Modes
EN/UVLO LDSTRT DEVICE STATE
L X Disabled
H L ON
H H OFF
Refer to Load Detect/Handshake (LDSTRT) section for more details.
Table 8-7. Fault Response Functional Modes
EN/UVLO RETRY_DLY NRETRY DEVICE STATE
L X X Disabled
H Short to GND X No auto-retry (Latch-off)
H Open Open Auto-retry 4 times with minimum delay between retries and
then latch-off
H Open Short to GND Auto-retry indefinitely with minimum delay between retries
H Capacitor to GND Capacitor to GND Auto-retry delay and count as per Equation 8 and Equation 9
H Capacitor to GND Open Auto-retry 4 times with finite delay between retries as per
Equation 8 and then latch-off
H Capacitor to GND Short to GND Auto-retry indefinitely with finite delay between retries as per
Equation 8
Refer to Fault Response section for more details.
www.ti.com
TPS25980
SLVSFR1 - AUGUST 2020
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 27
Product Folder Links: TPS25980
```

### Page 28

#### Extracted tables

Table 1:

```text
DESIGN PARAMETER | EXAMPLE VALUE
Input voltage, V IN | 12 V
Undervoltage lockout set point, VIN UVLO | 10.8 V
Maximum load current, I OUT | 6.5 A
Current limit, I LIM | 8 A
Transient overcurrent blanking interval (t ) ITIMER | 2 ms
Load capacitance, C OUT | 1.4 mF
Load at start-up, R L(SU) | 10 Ohm
Output voltage ramp time, T dVdt | 20 ms
Maximum ambient temperature, T A | 70 deg C
```

#### Raw extracted text

```text
TPS25980
SLVSFR1 - AUGUST 2020 www.ti.com
9 Application and Implementation
Note
Information in the following applications sections is not part of the TI component specification,
and TI does not warrant its accuracy or completeness. TIs customers are responsible for
determining suitability of components for their purposes, as well as validating and testing their design
implementation to confirm system functionality.
9.1 Application Information
The TPS25980x device is an integrated 8-A eFuse that is typically used for hot-swap and power rail protection
applications. It operates from 2.7 V to 24 V with adjustable overcurrent and undervoltage protection. It also
provides optional overvoltage with various fixed internal thresholds. The device aids in controlling the inrush
current and has the flexibility to configure the number of auto-retries and retry delay. The adjustable overcurrent
blanking timer provides the functionality to allow transient overcurrent pulses without limiting or tripping. These
devices protect source, load and internal MOSFET from potentially damaging events in systems such as PCIe
cards, SSDs, HDDs, Optical Modules, Routers, Switches, Industrial PCs, Retail ePOS (Point-of-sale) terminals
and Patient Monitoring Systems.
The following design procedure can be used to select the supporting component values based on the application
requirement. Additionally, a spreadsheet design tool TPS25980xx Design Calculator is available in the web
product folder.
9.2 Typical Application: Patient Monitoring System in Medical Applications
TPS259804O
V IN IN OUT V OUT
3.3V
R VL1 LDSTRT R PG
10Y(cid:3) 100.Y(cid:3)
EN/UVLO PG
NRETRY IMON
C
NRETRY B520C-
SMCJ12A C IN 2.2nF RETRY_DLY dVdt 13-F 1. C 4 O m U F T R 1 L 0 (S Y U)
0.1uF C
12 R 5 V . L2 Y(cid:3) 0 L . D 1 S u TR F T ILIM GND ITIMER R
C IMON
dVdt 1.62.Y(cid:3)
C RETRY_DLY R ILIM C ITIMER 10nF
2.2nF 182Y(cid:3) 4.7nF
Figure 9-1. Typical Application Schematic - Input Protection for Patient Monitoring System
9.2.1 Design Requirements
Table 9-1 shows the design parameters for this application example.
Table 9-1. Design Parameters
DESIGN PARAMETER EXAMPLE VALUE
Input voltage, V 12 V
IN
Undervoltage lockout set point, VIN 10.8 V
UVLO
Maximum load current, I 6.5 A
OUT
Current limit, I 8 A
LIM
Transient overcurrent blanking interval (t ) 2 ms
ITIMER
Load capacitance, C 1.4 mF
OUT
Load at start-up, R 10 Ohm
L(SU)
Output voltage ramp time, T 20 ms
dVdt
Maximum ambient temperature, T 70  deg C
A
28 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS25980
```

### Page 29

#### Extracted tables

Table 1:

```text
DESIGN PARAMETER | EXAMPLE VALUE
Retry delay, t RETRY_DLY | 100 ms
No. of retries, N RETRY | 4
```

#### Raw extracted text

```text
TPS25980
www.ti.com SLVSFR1 - AUGUST 2020
Table 9-1. Design Parameters (continued)
DESIGN PARAMETER EXAMPLE VALUE
Retry delay, t 100 ms
RETRY_DLY
No. of retries, N 4
RETRY
9.2.2 Detailed Design Procedure
9.2.2.1 Device Selection
This design example considers a 12-V system operating voltage with a tolerance of +/-10 %. The rated load
current is 6.5 A. If the current exceeds 8 A, then the device must allow overload current for 2-ms interval
before breaking the circuit and then restart. Accordingly, the TPS259804O variant is chosen. (Refer to Device
Comparison Table for device options.) Ambient temperatures may range from 20  deg C to 70  deg C. The load has a
minimum input capacitance of 1.4 mF and start-up resistive load of 10 Ohm. The downstream load is turned on only
after the PG signal is asserted.
9.2.2.2 Setting the Current Limit Threshold: R Selection
ILIM
The R resistor at the ILIM pin sets the overload current limit, whose value can be calculated using Equation
ILIM
10.
1460
RILIM(cid:11):(cid:12)
ILIM(cid:11)A(cid:12)(cid:16)0.11
(10)
For I = 8 A, R value is calculated to be 185.04 Ohm. Choose the closest available standard value: 182
LIM ILIM
Ohm, 1%. Refering to the Electrical Characteristics table, it can be verified that the minimum current limit across
temperature for R value of 182 Ohm is 7.23 A, which is higher than the nominal rated load current (6.5 A),
ILIM
thereby ensuring stable operation under normal conditions.
9.2.2.3 Setting the Undervoltage Lockout Set Point
The undervoltage lockout (UVLO) trip point is adjusted using the external voltage divider network of R and
VL1
R connected between IN, EN/UVLO and GND pins of the device. The resistor values required for setting the
VL2
undervoltage are calculated using Equation 11.
VUVLO(R) x (RVL1 (cid:14)RVL2)
VINUVLO =
RVL2 (11)
For minimizing the input current drawn from the power supply, TI recommends to use higher values of resistance
for R and R . However, leakage currents due to external active components connected to the resistor string
VL1 VL2
can add error to these calculations. So, the resistor string current, I must be 20 times greater than the
RVL12
leakage current (I ).
ENLKG
From the device electrical specifications, UVLO rising threshold V = 1.2 V. From design requirements,
UVLO(R)
VIN = 10.8 V. First choose the value of R = 1 MOhm and use Equation 11 to calculate R = 125 kOhm.
UVLO VL1 VL2
Use the closest standard 1% resistor values: R = 1 MOhm, and R = 125 kOhm
VL1 VL2
9.2.2.4 Choosing the Current Monitoring Resistor: R
IMON
Voltage at IMON pin V is proportional to the output load current. This can be connected to an ADC of
IMON
the downstream system for monitoring the operating condition and health of the system. The R must be
IMON
selected based on the maximum load current and the maximum IMON pin voltage at full-scale load current. The
maximum IMON pin voltage must be selected based on the input voltage range of the ADC used or the value
suggested in VIMON(Max) Recommended Values, whichever is lower. R is set using Equation 12.
IMON
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 29
Product Folder Links: TPS25980
```

### Page 30

#### Raw extracted text

```text
TPS25980
SLVSFR1 - AUGUST 2020 www.ti.com
RIMON(:)
VIMONmax(V)
(cid:16)6
IOUTmax(A)u246 u10
(12)
For I = 8 A and considering the operating range of ADC to be 0 V to 3.3 V, R can be calculated as
LIM IMON
3.3
RIMON= = 1697 (cid:13)
(cid:16)6
8u243 u10
(13)
Selecting R value less than shown in Equation 13 ensures that ADC limits are not exceeded for maximum
IMON
value of load current. Choose closest available standard value: 1620 Ohm, 1 %.
9.2.2.5 Setting the Output Voltage Ramp Time (T )
dVdt
For a successful design, the junction temperature of device must be kept below the absolute maximum rating
during both dynamic (start-up) and steady state conditions. Dynamic power stresses often are an order of
magnitude greater than the static stresses, so it is important to determine the right start-up time and in-rush
current limit required with system capacitance to avoid thermal shutdown during start-up with and without load.
The required ramp-up capacitor C is calculated considering the two possible cases (see Case 1: Start-
dVdt
Up Without Load: Only Output Capacitance C Draws Current and Case 2: Start-Up With Load:Output
OUT
Capacitance C and Load Draw Current)
OUT
9.2.2.5.1 Case 1: Start-Up Without Load: Only Output Capacitance C Draws Current
OUT
During start-up, as the output capacitor charges, the voltage drop as well as the power dissipated across the
internal FET decreases. The average power dissipated in the device during start-up is calculated using equation
14
P
D(INRUSH)
= 0.5 x V
IN
x I
INRUSH
(14)
Where I is the inrush current and is determined by Equation 15
INRUSH
V
I = C u IN
INRUSH OUT
T
dVdt (15)
Equation 14 assumes that the load does not draw any current (apart from the capacitor charging current) until
the output voltage has reached its final value.
9.2.2.5.2 Case 2: Start-Up With Load: Output Capacitance C and Load Draw Current
OUT
When the load draws current during the turn-on sequence, there is additional power dissipated. Considering a
resistive load during start-up R , load current ramps up proportionally with increase in output voltage during
L(SU)
T time. Equation 16 shows the average power dissipation in the internal FET during charging time due to
dVdt
resistive load.
1 V 2
P =    x IN
D(LOAD) 61 R
L(SU) (16)
Equation 17 gives the total power dissipated in the device during start-up
P = P + P
D(STARTUP) D(INRUSH) D(LOAD)
(17)
30 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS25980
```

### Page 31

#### Extracted tables

Table 1:

```text
|  |  |  |  |  |  |  |  |  | TP TP | S259 S259 | 807 802 | x x/0 | 3x | /0 | 4 | x
```

#### Raw extracted text

```text
The power dissipation, with and without load, for selected start-up time must not exceed the start-up thermal
shutdown limits as shown in Thermal Shutdown Plot During Start-up
Power Dissipation (W)
)sm(
nwodtuhS
lamrehT
ot
emiT
TPS25980
www.ti.com SLVSFR1 - AUGUST 2020
200
TPS259807x
100 TPS259802x/03x/04x
50
30
20
10
5
3
2
1
0.5
2 3 4 5 678 10 20 30 4050 70 100
D002
Figure 9-2. Thermal Shutdown Plot During Start-up
For the design example under discussion, the output voltage has to be ramped up in 20 ms, which mandates a
slew-rate of 0.6 V/ms for a 12 V rail.
The required C capacitance on dVdt pin to set 0.6 V/ms slew rate can be calculated using Equation 18
dVdt
4600
CdVdt (cid:11)pF(cid:12) 7666 pF
SR(cid:11)V/ms(cid:12)
(18)
The dVdt capacitor is subjected to typically V + 4 V during startup. The high voltage bias leads to a drop in the
IN
effective capacitor value. So, it is suggested to choose 20% higher than the calculated value, which gives 9.2 nF.
Choose closest 10% standard value: 10 nF
The 10 nF C capacitance sets a slew-rate of 0.46 V/ms and output ramp time T of 26 ms.
dVdt dVdt
The inrush current drawn by the load capacitance C during ramp-up can be calculated using Equation 19
OUT
12 V
I = 1.4 mFu 0.65 A
INRUSH
26 ms
(19)
The inrush power dissipation can be calculated using Equation 20
P
D(INRUSH)
= 0.5 x 12 x 0.65 = 3.9 W
(20)
For 3.9 W of power loss, the thermal shutdown time of the device must be greater than the ramp-up time T
dVdt
to ensure a successful start-up. Figure 9-2 shows the start-up thermal shutdown limit. For 3.9 W of power, the
shutdown time is approximately 100 ms. So it is safe to use 26 ms as the start-up time without any load on the
output.
The additional power dissipation when a 10-Ohm load is present during start-up is calculated using Equation 21
1 122
P     u 2.4W
D(LOAD) 61 10
(21)
The total device power dissipation during start-up can be calculated using Equation 22
P 3.9 (cid:14) 2.4 6.3 W
D(STARTUP)
(22)
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 31
Product Folder Links: TPS25980
```

### Page 32

#### Raw extracted text

```text
TPS25980
SLVSFR1 - AUGUST 2020 www.ti.com
From Thermal Shutdown Plot During Start-up, the thermal shutdown time for 6.3 W is approximately 40 ms. It
is safe to have 30% margin to allow for variation of system parameters such as load, component tolerance, and
input voltage. So it is well within acceptable limits to use the 10 nF for C capacitor with start-up load of 10 Ohm.
dVdt
When C is large, there is a need to decrease the power dissipation during start-up. This can be done by
OUT
increasing the value of the C capacitor. A spreadsheet tool TPS25980xx Design Calculator available on the
dVdt
web can be used for iterative calculations.
9.2.2.6 Setting the Load Handshake (LDSTRT) Delay
To indicate a successful start-up, the load circuit must provide a handshake signal to TPS25980x by pulling
down the LDSTRT pin within the time set by the capacitor C on the LDSTRT pin. Once the PG asserts,
LDSTRT
the device sources 2-uA current into C . For a successful handshake, the load circuit must pull-down the
LDSTRT
LDSTRT pin before C charges up to 1.2 V.
LDSTRT
For the design requirement of 60-ms handshake delay, use Equation 23 to calculate C
LDSTRT
tLDSTRT 60ms
CLDSTRT ILDSTRT u 2PA u 0.1PF
VLDSTRT 1.2V
(23)
Choose closest available standard value: 0.1 uF, 10 %.
9.2.2.7 Setting the Transient Overcurrent Blanking Interval (t )
ITIMER
For the design example under discussion, overcurrent transients are allowed for 2-ms duration. This blanking
interval can be set by selecting appropriate capacitor C from ITIMER pin to ground. The value of C to
ITIMER ITIMER
set 2 ms for t can be calculated using Equation 24.
ITIMER
tITIMER (ms)
CITIMER (nF) = = 4.255 nF
0.47
(24)
Choose closest available standard value: 4.7 nF, 10 %.
9.2.2.8 Setting the Auto-Retry Delay and Number of Retries
The time delay between retries can be programmed by selecting capacitor C on RETRY_DLY pin. The
RETRY_DLY
value of C to set a 100-ms auto-retry delay can be calculated using Equation 25.
RETRY_DLY
tRETRY_DLY (Ps)
CRETRY_DLY (pF) = (cid:16)4 pF = 2131.38 pF
46.83
(25)
Choose closest available standard value: 2.2 nF, 10 %.
The number of auto-retry attempts can be set by a capacitor C on the NRETRY pin using Equation 26
NRETRY
4uCNRETRY (pF)
NRETRY =
CRETRY_DLY (pF) + 4 pF
(26)
For this design example, the requirement is to retry 4 times after the device shuts down due to a fault. Since, the
number of auto-retries can be adjusted in discrete steps as explained in Fault Response, choose C such
NRETRY
that N is less than 4. Use Equation 27 to calculate C .
RETRY NRETRY
NRETRYu (cid:11)CRETRY_DLY (pF) + 4 pF(cid:12)
CNRETRY (pF) < < 2204 pF
4
(27)
Choose closest available standard value: 2.2 nF, 10 %.
32 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS25980
```

### Page 33

#### Extracted tables

Table 1:

```text
A. C = 1.4 mF C = 10 nF R = Open OUT dVdt L(SU) Figure 9-3. Hot-Plug Start-Up Without Load on Output - dVdt Limited | A. C = 1.4 mF C = 10 nF R = 10 Ohm OUT dVdt L(SU) Figure 9-4. Hot-Plug Start-Up With Load on Output - dVdt Limited
A. R = 182 Ohm C = 4.7 nF ILIM ITIMER Figure 9-5. Circuit Breaker With Transient Overcurrent Blanking Interval of 2 ms | A. R = TBD Ohm C = 4.7 nF C = 2.2 nF, ILIM ITIMER RETRY_DLY C = 2.2 nF NRETRY Figure 9-6. Circuit Breaker - Auto-Retry 4 Times With Retry Delay of 100 ms
```

#### Raw extracted text

```text
TPS25980
www.ti.com SLVSFR1 - AUGUST 2020
9.2.3 Application Curves
A. C = 1.4 mF C = 10 nF R = Open A. C = 1.4 mF C = 10 nF R = 10 Ohm
OUT dVdt L(SU) OUT dVdt L(SU)
Figure 9-3. Hot-Plug Start-Up Without Load on Figure 9-4. Hot-Plug Start-Up With Load on Output
Output - dVdt Limited - dVdt Limited
A. R = 182 Ohm C = 4.7 nF A. R = TBD Ohm C = 4.7 nF C = 2.2 nF,
ILIM ITIMER ILIM ITIMER RETRY_DLY
C = 2.2 nF
Figure 9-5. Circuit Breaker With Transient NRETRY
Overcurrent Blanking Interval of 2 ms Figure 9-6. Circuit Breaker - Auto-Retry 4 Times
With Retry Delay of 100 ms
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 33
Product Folder Links: TPS25980
```

### Page 34

#### Extracted tables

Table 1:

```text
A. R = 182 Ohm ILIM Figure 9-7. Output Hard Short-Circuit While ON | A. R = 182 Ohm ILIM Figure 9-8. Output Hard Short-Circuit While ON (Zoomed In)
A. R = 182 Ohm ILIM Figure 9-9. Power-Up With Short-Circuit on Output | A. R = 182 Ohm ILIM Figure 9-10. Power-Up With Short-Circuit on Output - Auto-Retry 4 Times With Retry Delay of 100 ms
A. C = 0.1 uF LDSTRT Figure 9-11. Successful Load Handshake (LDSTRT) | A. C = 0.1 uF LDSTRT Figure 9-12. Unsuccessful Load Handshake (LDSTRT)
```

#### Raw extracted text

```text
TPS25980
SLVSFR1 - AUGUST 2020 www.ti.com
A. R = 182 Ohm A. R = 182 Ohm
ILIM ILIM
Figure 9-7. Output Hard Short-Circuit While ON Figure 9-8. Output Hard Short-Circuit While ON
(Zoomed In)
A. R = 182 Ohm A. R = 182 Ohm
ILIM ILIM
Figure 9-9. Power-Up With Short-Circuit on Output Figure 9-10. Power-Up With Short-Circuit on
Output - Auto-Retry 4 Times With Retry Delay of
100 ms
A. C = 0.1 uF A. C = 0.1 uF
LDSTRT LDSTRT
Figure 9-11. Successful Load Handshake (LDSTRT) Figure 9-12. Unsuccessful Load Handshake
(LDSTRT)
34 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS25980
```

### Page 35

#### Extracted tables

Table 1:

```text
DC-DC
```

#### Raw extracted text

```text
9.3 System Examples
9.3.1 Optical Module Power Rail Path Protection
Optical modules are commonly used in high-bandwidth data communication systems such as Optical Networking
equipment, Enterprise/Data-Center Switches and Routers. Several variants of optical modules are available in
the market, which differ in the form-factor and the data speed support (Gbit/s). Of these, the popular variant
Double Dense Quad Small Form-factor Pluggable (QSFP-DD) module supports speeds up to 400 Gbit/s. In
addition to the system protection during hot-plug events, the other key requirement for optical module is the tight
voltage regulation. The optical module uses 3.3 V supply and requires voltage regulation within +/-5 % for proper
operation.
A typical power tree of such system is shown in Figure 9-13. The optical line card consists of DC-DC converter,
protection device (eFuse) and power supply filters. The DC-DC converter steps-down the 12 V to 3.3 V and
maintains the 3.3 V rail within +/-2 %. The power supply filtering network uses LC components to reduce high
frequency noise injection into the optical module. The DC resistance of the inductor L causes voltage drop of
around 1.5 % which leaves us with a voltage drop budget of just 1.5 % (3.3 V * 1.5% = 50 mV) across the
protection device. Considering a maximum load current of 5.5 A per module, the maximum ON-resistance of
the protection device should be less than 9 m Ohm. TPS25980x eFuse offers ultra-low ON-resistance of 2.7 m Ohm
(typical) and 4.5 mOhm (maximum, across temperature), thereby meeting the target specification with additional
margin to spare and simplifying the overall system design.
DC-DC
VIN
12V
eFuse
IN OUT
LDSTRT
3.3V
Optical Line Card
Hot Plug / Unplug QSFP
Module
VccTx
VccRx
Vcc
ModPrsL
GND
VOUT
Figure 9-13. Power Tree Block Diagram of a Typical Optical Line Card
As shown in Figure 9-13 , ModPrsL signal acts as a handshake signal between the line card and the optical
module. ModPrsL is always pulled to ground inside the module. When the module is hot-plugged into the host
Optical Line Card connector, the ModPrsL signal pulls down the LDSTRT pin and enables the TPS25980x
eFuse to power the module. This ensures that power is applied on the port only when a module is plugged in
and disconnected when there is no module present.
www.ti.com
TPS25980
SLVSFR1 - AUGUST 2020
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 35
Product Folder Links: TPS25980
```

### Page 36

#### Extracted tables

Table 1:

```text
DESIGN PARAMETER | EXAMPLE VALUE
Input voltage, V IN | 3.3 V
Overvoltage lockout, V OVP | 3.7 V
Maximum voltage drop in the path | +/- 5 %
Maximum load current, I OUT | 5.5 A
Current limit, I LIM | 7 A
Transient overcurrent blanking interval (t ) ITIMER | 6 ms
Load capacitance, C OUT | 10 uF
Maximum ambient temperature, T A | 85 deg C
Module present detection, ModPrsL | Yes
Retry delay, t RETRY_DLY | 200 us
No. of retries, N RETRY | 4
```

#### Raw extracted text

```text
TPS25980
SLVSFR1 - AUGUST 2020 www.ti.com
TPS259802O
V IN V OUT
IN OUT
3.3V
ModPrsL LDSTRT
R
PG
100.Y(cid:3)
EN/UVLO PG
NRETRY IMON
C
NRETRY
C IN OPEN RETRY_DLY dVdt C L R L
0.1uF B520C-13-F 10uF
ILIM GND ITIMER
0.1uF R
C IMON
dVdt 1910Y(cid:3)
C RETRY_DLY R ILIM C ITIMER 3.3nF
OPEN 210Y(cid:3) 15nF
Figure 9-14. TPS259802O Configured for a 3.3-V Power Rail Path Protection in Optical Module
9.3.1.1 Design Requirements
Table 9-2 shows the design parameters for this example.
Table 9-2. Design Parameters
DESIGN PARAMETER EXAMPLE VALUE
Input voltage, V 3.3 V
IN
Overvoltage lockout, V 3.7 V
OVP
Maximum voltage drop in the path +/- 5 %
Maximum load current, I 5.5 A
OUT
Current limit, I 7 A
LIM
Transient overcurrent blanking interval (t ) 6 ms
ITIMER
Load capacitance, C 10 uF
OUT
Maximum ambient temperature, T 85  deg C
A
Module present detection, ModPrsL Yes
Retry delay, t 200 us
RETRY_DLY
No. of retries, N 4
RETRY
9.3.1.2 Device Selection
Optical modules are very sensitive to supply voltage variations and thus require input overvoltage protection.
TPS259802O variant from TPS25980x family is selected to set overvoltage protection at 3.7 V. TPS259802O
allows overcurrents for a user specified blanking interval t before breaking the circuit path. In this use case,
ITIMER
t is set for 6 ms interval.
ITIMER
9.3.1.3 External Component Settings
By following similar design procedure as outlined in Detailed Design Procedure, the external component values
are calculated as below
* R = 210 Ohm to set 7-A current limit
ILIM
* C = 15 nF to set fault blanking time of 6 ms
ITIMER
* R = 1910 Ohm to set maximum IMON pin voltage V within ADC range of 3.3 V
IMON IMON
* C capacitance is chosen as 3.3 nF
dVdt
* Leave RETRY_DLY and NRETRY pins OPEN to set minimum auto-retry delay of 200 us and number of
retries to 4
9.3.1.4 Voltage Drop
Table 9-3 shows the power path voltage drop (%) due to the eFuse in QSFP modules of different power classes.
36 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS25980
```

### Page 37

#### Extracted tables

Table 1:

```text
POWER CLASS | MAXIMUM POWER CONSUMPTION PER MODULE (W) | MAXIMUM LOAD CURRENT (A) | TYPICAL VOLTAGE DROP (%)
1 | 1.5 | 0.454 | 0.037
2 | 3.5 | 1.06 | 0.087
3 | 7 | 2.12 | 0.174
4 | 8 | 2.42 | 0.2
5 | 10 | 3.03 | 0.248
6 | 12 | 3.63 | 0.3
7 | 14 | 4.24 | 0.347
8 | 18 | 5.45 | 0.446
```

Table 2:

```text
Figure 9-15. Output Voltage Profile When Optical Module is Inserted | Figure 9-16. Output Voltage Profile When Optical Module is Plugged Out
Figure 9-17. Circuit Breaker With Transient Overcurrent Blanking Interval of 6 ms; Device Restarts in Current Limit Mode | Figure 9-18. Overload Response and Recovery
```

#### Raw extracted text

```text
Table 9-3. Voltage Drop across TPS25980x on QSFP Module Power Rail
POWER CLASS MAXIMUM POWER
CONSUMPTION PER MODULE
(W)
MAXIMUM LOAD CURRENT (A) TYPICAL VOLTAGE DROP (%)
1 1.5 0.454 0.037
2 3.5 1.06 0.087
3 7 2.12 0.174
4 8 2.42 0.2
5 10 3.03 0.248
6 12 3.63 0.3
7 14 4.24 0.347
8 18 5.45 0.446
9.3.1.5 Application Curves
Figure 9-15. Output Voltage Profile When Optical
Module is Inserted
Figure 9-16. Output Voltage Profile When Optical
Module is Plugged Out
Figure 9-17. Circuit Breaker With Transient
Overcurrent Blanking Interval of 6 ms; Device
Restarts in Current Limit Mode
Figure 9-18. Overload Response and Recovery
www.ti.com
TPS25980
SLVSFR1 - AUGUST 2020
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 37
Product Folder Links: TPS25980
```

### Page 38

#### Extracted tables

Table 1:

```text
Figure 9-19. Overvoltage Cut-off at 3.7 V with TPS259802O Device | Figure 9-20. Overvoltage Protection Response and Recovery with TPS259802O Device
```

#### Raw extracted text

```text
Figure 9-19. Overvoltage Cut-off at 3.7 V with
TPS259802O Device
Figure 9-20. Overvoltage Protection Response and
Recovery with TPS259802O Device
9.3.2 Input Protection for 12-V Rail Applications: PCIe Cards, Storage Interfaces and DC Fans
TPS25980x eFuse provides inrush current management and also protects the system from most common faults
such as undervoltage, overvoltage and overcurrents. The combination of high current support along with low
ON-resistance makes TPS25980x eFuse an ideal protection solution for PCIe cards, Storage Interfaces and
DC Fan loads. The external component values can be calculated by following the design procedure outlined in
Detailed Design Procedure. Alternatively, a spreadsheet design tool TPS25980xx Design Calculator is available
for simplified design efforts.
TPS25980
SLVSFR1 - AUGUST 2020 www.ti.com
38 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS25980
```

### Page 39

#### Extracted tables

Table 1:

```text
1MO 137kO | 100O |
```

#### Raw extracted text

```text
10 Power Supply Recommendations
The TPS25980x devices are designed for a supply voltage range of 2.7 V <= VIN <= 24 V. TI recommends an
input ceramic bypass capacitor higher than 0.1 uF if the input supply is located more than a few inches from
the device. The power supply must be rated higher than the set current limit to avoid voltage droops during
overcurrent and short-circuit conditions.
10.1 Transient Protection
In the case of a short circuit and overload current limit when the device interrupts current flow, the input
inductance generates a positive voltage spike on the input, and the output inductance generates a negative
voltage spike on the output. The peak amplitude of voltage spikes (transients) is dependent on the value of
inductance in series to the input or output of the device. Such transients can exceed the absolute maximum
ratings of the device if steps are not taken to address the issue. Typical methods for addressing transients
include:
* Minimize lead length and inductance into and out of the device.
* Use a large PCB GND plane.
* Use a Schottky diode across the output to absorb negative spikes.
* Use a low value ceramic capacitor CIN = 0.001 uF to 0.1 uF to absorb the energy and dampen the transients.
The approximate value of input capacitance can be estimated using Equation 28.
IN
SPIKE(Absolute) IN LOAD
IN
LV  = V  + I  x C
(28)
where
* VIN is the nominal supply voltage
* ILOAD is the load current
* LIN equals the effective inductance seen looking into the source
* CIN is the capacitance present at the input
Some of the applications may require the addition of a Transient Voltage Suppressor (TVS) to prevent transients
from exceeding the absolute maximum ratings of the device. A typical circuit implementation with optional
protection components (a ceramic capacitor, TVS and Schottky diode) is shown in Figure 10-1.
IN
EN/UVLO
OUT
dVdt
GND
0.1uF 220uF
3.3nF
TPS25980
182O
ILIM
PG
3.3V
100kO
511O
IMONNRETRY
56pF
LDSTRT
RETRY_DLY
4.7nF
ITIMER
56pF
1uF
12V
100O1MO
137kO
Figure 10-1. Typical Circuit Implementation With Optional Protection Components
www.ti.com
TPS25980
SLVSFR1 - AUGUST 2020
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 39
Product Folder Links: TPS25980
```

### Page 40

#### Raw extracted text

```text
10.2 Output Short-Circuit Measurements
It is difficult to obtain repeatable and similar short-circuit testing results. The following contribute to variation in
results:
* Source bypassing
* Input leads
* Board layout
* Component selection
* Output shorting method
* Relative location of the short
* Instrumentation
The actual short exhibits a certain degree of randomness because it microscopically bounces and arcs. Ensure
that configuration and methods are used to obtain realistic results.
Note
Do not expect to see waveforms exactly like the waveforms in this data sheet because every setup is
different.
TPS25980
SLVSFR1 - AUGUST 2020 www.ti.com
40 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS25980
```

### Page 41

#### Raw extracted text

```text
11 Layout
11.1 Layout Guidelines
* The IN Exposed Thermal Pad is used for Heat Dissipation. Connect to as much copper area as possible
using an array of thermal vias. The via array also helps to minimize the voltage gradient across the VIN pad
and facilitates uniform current distribution through the internal FET, which improves the current sensing and
monitoring accuracy.
* For all applications, TI recommends a ceramic decoupling capacitor of 0.01 uF or greater between IN and
GND terminals. For hot-plug applications, where input power-path inductance is negligible, this capacitor can
be eliminated or minimized.
* The optimal placement of the decoupling capacitor is closest to the IN and GND terminals of the device. Care
must be taken to minimize the loop area formed by the bypass-capacitor connection, the IN terminal, and the
GND terminal of the IC.
* High current carrying power path connections must be as short as possible and must be sized to carry at
least twice the full-load current. It is recommended to use a minimum trace width of 50 mil for the OUT power
connection.
* The GND terminal is the reference for all internal signals and must be isolated from any bounce due to large
switching currents in the system power ground plane. It is recommended to connect the device GND to a
signal ground island on the board, which in turn is connected to the system power GND plane at one point.
* Locate the support components for the following signals close to their respective connection pins - ILIM,
IMON, ITIMER, RETRY_DLY, NRETRY and dVdT with the shortest possible trace routing to reduce parasitic
effects on the respective associated functions. These traces must not have any coupling to switching signals
on the board.
* The ILIM pin is highly sensitive to capacitance and TI recommends to pay special attention to the layout to
maintain the parasitic capacitance below 30 pF for stable operation.
* Use short traces on the RETRY_DLY and NRETRY pins to ensure the auto-retry timer delay and number of
auto-retries is not altered by the additional parasitic capacitance on these pins.
* Protection devices such as TVS, snubbers, capacitors, or diodes must be placed physically close to the
device they are intended to protect. These protection devices must be routed with short traces to reduce
inductance. For example, TI recommends a protection Schottky diode to address negative transients due to
switching of inductive loads, and it must be physically close to the OUT pins.
* Use proper layout and thermal management techniques to ensure there is no significant steady state thermal
gradient between the two thermal pads on the IC. This is necessary for proper functioning of the device
overtemperature protection mechanism and successful startup under all conditions.
* Obtaining acceptable performance with alternate layout schemes is possible; the Layout Example is intended
as a guideline and shown to produce good results from electrical and thermal standpoint.
www.ti.com
TPS25980
SLVSFR1 - AUGUST 2020
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 41
Product Folder Links: TPS25980
```

### Page 42

#### Extracted tables

Table 1:

```text
VIN Plane (Top Layer) > * * |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  | > |  |  |  |  |  |  |  |  | VOUT Plane (Top Layer) |  | 
 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 5 |  |  | 
 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 0 mils * |  | 
 | * |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  | Signal GND ( |  |  |  |  |  | Top |  |  |  |  |
```

Table 2:

```text
Power GND Plane (Top Layer) | Power GND |  | Pla | ne (Top Layer) |  |  |  |  |  |  |  |  |
```

#### Raw extracted text

```text
11.2 Layout Example
VOUT Plane (Top Layer)VIN Plane (Top Layer)
Power GND Plane (Top Layer)
PCB via to Bottom Layer Blind PCB via to Inner Layer
Signal GND (Top Layer)
*
*
*
*
* Optional components for suppressing transients induced while
switching current through  inductive elements at input/output
> 50 mils
Figure 11-1. TPS25980 Example PCB Layout
TPS25980
SLVSFR1 - AUGUST 2020 www.ti.com
42 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS25980
```

### Page 43

#### Extracted tables

Table 1:

```text
PARTS | PRODUCT FOLDER | ORDER NOW | TECHNICAL DOCUMENTS | TOOLS & SOFTWARE | SUPPORT & COMMUNITY
TPS259802O | Click here | Click here | Click here | Click here | Click here
TPS259803O | Click here | Click here | Click here | Click here | Click here
TPS259804O | Click here | Click here | Click here | Click here | Click here
TPS259807O | Click here | Click here | Click here | Click here | Click here
```

#### Raw extracted text

```text
12 Device and Documentation Support
12.1 Documentation Support
12.1.1 Related Documentation
For related documentation see the following:
* TPS259804OEVM eFuse Evaluation Board
* TPS25980xx Design Calculator
12.1.1.1 Related Links
The table below lists quick access links. Categories include technical documents, support and community
resources, tools and software, and quick access to order now.
Table 12-1. Related Links
PARTS PRODUCT FOLDER ORDER NOW TECHNICAL
DOCUMENTS
TOOLS &
SOFTWARE
SUPPORT &
COMMUNITY
TPS259802O Click here Click here Click here Click here Click here
TPS259803O Click here Click here Click here Click here Click here
TPS259804O Click here Click here Click here Click here Click here
TPS259807O Click here Click here Click here Click here Click here
12.2 Receiving Notification of Documentation Updates
To receive notification of documentation updates, navigate to the device product folder on ti.com. In the upper
right corner, click on Alert me  to register and receive a weekly digest of any product information that has
changed. For change details, review the revision history included in any revised document.
12.3 Support Resources
TI E2E (TM) support forums  are an engineer's go-to source for fast, verified answers and design help - straight
from the experts. Search existing answers or ask your own question to get the quick design help you need.
Linked content is provided "AS IS" by the respective contributors. They do not constitute TI specifications and do
not necessarily reflect TI's views; see TI's Terms of Use.
12.4 Trademarks
TI E2E(TM) is a trademark of Texas Instruments.
All trademarks are the property of their respective owners.
12.5 Electrostatic Discharge Caution
This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled
with appropriate precautions. Failure to observe proper handling and installation procedures can cause damage.
ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may
be more susceptible to damage because very small parametric changes could cause the device not to meet its published
specifications.
12.6 Glossary
TI Glossary This glossary lists and explains terms, acronyms, and definitions.
www.ti.com
TPS25980
SLVSFR1 - AUGUST 2020
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 43
Product Folder Links: TPS25980
```

### Page 44

#### Raw extracted text

```text
13 Mechanical, Packaging, and Orderable Information
The following pages include mechanical, packaging, and orderable information. This information is the most
current data available for the designated devices. This data is subject to change without notice and revision of
this document. For browser-based versions of this data sheet, refer to the left-hand navigation.
TPS25980
SLVSFR1 - AUGUST 2020 www.ti.com
44 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS25980
```

### Page 45

#### Extracted tables

Table 1:

```text
Orderable part number | Status (1) | Material type (2) | Package | Pins | Package qty | Carrier | RoHS (3) | Lead finish/ Ball material (4) | MSL rating/ Peak reflow (5) | Op temp ( deg C) | Part marking (6)
TPS259802ONRGER | Active | Production | VQFN (RGE) | 24 | 3000 | LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | TP2598 02ON
TPS259802ONRGER.A | Active | Production | VQFN (RGE) | 24 | 3000 | LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | TP2598 02ON
TPS259803ONRGER | Active | Production | VQFN (RGE) | 24 | 3000 | LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | TP2598 03ON
TPS259803ONRGER.A | Active | Production | VQFN (RGE) | 24 | 3000 | LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | TP2598 03ON
TPS259804ONRGER | Active | Production | VQFN (RGE) | 24 | 3000 | LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | TP2598 04ON
TPS259804ONRGER.A | Active | Production | VQFN (RGE) | 24 | 3000 | LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | TP2598 04ON
TPS259807ONRGER | Active | Production | VQFN (RGE) | 24 | 3000 | LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | TP2598 07ON
TPS259807ONRGER.A | Active | Production | VQFN (RGE) | 24 | 3000 | LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | TP2598 07ON
```

#### Raw extracted text

```text
PACKAGE OPTION ADDENDUM
www.ti.com 6-Feb-2026
PACKAGING INFORMATION
Orderable part number Status
(1)
Material type
(2)
Package | Pins Package qty | Carrier RoHS
(3)
Lead finish/
Ball material
(4)
MSL rating/
Peak reflow
(5)
Op temp ( deg C) Part marking
(6)
TPS259802ONRGER Active Production VQFN (RGE) | 24 3000 | LARGE T&R Yes NIPDAUAG Level-2-260C-1 YEAR -40 to 125 TP2598
02ON
TPS259802ONRGER.A Active Production VQFN (RGE) | 24 3000 | LARGE T&R Yes NIPDAUAG Level-2-260C-1 YEAR -40 to 125 TP2598
02ON
TPS259803ONRGER Active Production VQFN (RGE) | 24 3000 | LARGE T&R Yes NIPDAUAG Level-2-260C-1 YEAR -40 to 125 TP2598
03ON
TPS259803ONRGER.A Active Production VQFN (RGE) | 24 3000 | LARGE T&R Yes NIPDAUAG Level-2-260C-1 YEAR -40 to 125 TP2598
03ON
TPS259804ONRGER Active Production VQFN (RGE) | 24 3000 | LARGE T&R Yes NIPDAUAG Level-2-260C-1 YEAR -40 to 125 TP2598
04ON
TPS259804ONRGER.A Active Production VQFN (RGE) | 24 3000 | LARGE T&R Yes NIPDAUAG Level-2-260C-1 YEAR -40 to 125 TP2598
04ON
TPS259807ONRGER Active Production VQFN (RGE) | 24 3000 | LARGE T&R Yes NIPDAUAG Level-2-260C-1 YEAR -40 to 125 TP2598
07ON
TPS259807ONRGER.A Active Production VQFN (RGE) | 24 3000 | LARGE T&R Yes NIPDAUAG Level-2-260C-1 YEAR -40 to 125 TP2598
07ON

(1) Status:  For more details on status, see our product life cycle.

(2) Material type:  When designated, preproduction parts are prototypes/experimental devices, and are not yet approved or released for full production. Testing and final process, including without limitation quality assurance,
reliability performance testing, and/or process qualification, may not yet be complete, and this item is subject to further changes or possible discontinuation. If available for ordering, purchases will be subject to an additional
waiver at checkout, and are intended for early internal evaluation purposes only. These items are sold without warranties of any kind.

(3) RoHS values:  Yes, No, RoHS Exempt. See the TI RoHS Statement for additional information and value definition.

(4) Lead finish/Ball material:  Parts may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead finish/Ball material values may wrap to two lines if the finish value exceeds the maximum
column width.

(5) MSL rating/Peak reflow:  The moisture sensitivity level ratings and peak solder (reflow) temperatures. In the event that a part has multiple moisture sensitivity ratings, only the lowest level per JEDEC standards is shown.
Refer to the shipping label for the actual reflow temperature that will be used to mount the part to the printed circuit board.

(6) Part marking:  There may be an additional marking, which relates to the logo, the lot trace code information, or the environmental category of the part.

Addendum-Page 1
```

### Page 46

#### Raw extracted text

```text
PACKAGE OPTION ADDENDUM
www.ti.com 6-Feb-2026
Multiple part markings will be inside parentheses. Only one part marking contained in parentheses and separated by a "~" will appear on a part. If a line is indented then it is a continuation of the previous line and the two
combined represent the entire part marking for that device.

Important Information and Disclaimer:The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and
makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative
and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers
and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.

Addendum-Page 2
```

### Page 47

#### Extracted tables

Table 1:

```text
W |
```

Table 2:

```text
B | 0
```

Table 3:

```text
Re Diam | el eter
```

Table 4:

```text
A0 | Dimension designed to accommodate the component width
B0 | Dimension designed to accommodate the component length
K0 | Dimension designed to accommodate the component thickness
W | Overall width of the carrier tape
P1 | Pitch between successive cavity centers
```

Table 5:

```text
Q1 | Q2
Q3 | Q4
```

Table 6:

```text
Q1 | Q2
Q3 | Q4
```

Table 7:

```text
Device | Package Type | Package Drawing | Pins | SPQ | Reel Diameter (mm) | Reel Width W1 (mm) | A0 (mm) | B0 (mm) | K0 (mm) | P1 (mm) | W (mm) | Pin1 Quadrant
TPS259802ONRGER | VQFN | RGE | 24 | 3000 | 330.0 | 12.4 | 4.35 | 4.35 | 1.1 | 8.0 | 12.0 | Q2
TPS259803ONRGER | VQFN | RGE | 24 | 3000 | 330.0 | 12.4 | 4.35 | 4.35 | 1.1 | 8.0 | 12.0 | Q2
TPS259804ONRGER | VQFN | RGE | 24 | 3000 | 330.0 | 12.4 | 4.35 | 4.35 | 1.1 | 8.0 | 12.0 | Q2
TPS259807ONRGER | VQFN | RGE | 24 | 3000 | 330.0 | 12.4 | 4.35 | 4.35 | 1.1 | 8.0 | 12.0 | Q2
```

#### Raw extracted text

```text
PACKAGE MATERIALS INFORMATION
www.ti.com 17-Apr-2023
TAPE AND REEL INFORMATION
REEL DIMENSIONS TAPE DIMENSIONS
K0 P1
W
B0
Reel
Diameter
Cavity A0
A0 Dimension designed to accommodate the component width
B0 Dimension designed to accommodate the component length
K0 Dimension designed to accommodate the component thickness
W Overall width of the carrier tape
P1 Pitch between successive cavity centers
Reel Width (W1)
QUADRANT ASSIGNMENTS FOR PIN 1 ORIENTATION IN TAPE
Sprocket Holes
Q1 Q2 Q1 Q2
Q3 Q4 Q3 Q4 User Direction of Feed
Pocket Quadrants
*All dimensions are nominal
Device Package Package Pins SPQ Reel Reel A0 B0 K0 P1 W Pin1
Type Drawing Diameter Width (mm) (mm) (mm) (mm) (mm) Quadrant
(mm) W1 (mm)
TPS259802ONRGER VQFN RGE 24 3000 330.0 12.4 4.35 4.35 1.1 8.0 12.0 Q2
TPS259803ONRGER VQFN RGE 24 3000 330.0 12.4 4.35 4.35 1.1 8.0 12.0 Q2
TPS259804ONRGER VQFN RGE 24 3000 330.0 12.4 4.35 4.35 1.1 8.0 12.0 Q2
TPS259807ONRGER VQFN RGE 24 3000 330.0 12.4 4.35 4.35 1.1 8.0 12.0 Q2
Pack Materials-Page 1
```

### Page 48

#### Extracted tables

Table 1:

```text
| H
```

Table 2:

```text
Device | Package Type | Package Drawing | Pins | SPQ | Length (mm) | Width (mm) | Height (mm)
TPS259802ONRGER | VQFN | RGE | 24 | 3000 | 338.0 | 355.0 | 50.0
TPS259803ONRGER | VQFN | RGE | 24 | 3000 | 338.0 | 355.0 | 50.0
TPS259804ONRGER | VQFN | RGE | 24 | 3000 | 338.0 | 355.0 | 50.0
TPS259807ONRGER | VQFN | RGE | 24 | 3000 | 338.0 | 355.0 | 50.0
```

#### Raw extracted text

```text
PACKAGE MATERIALS INFORMATION

www.ti.com 17-Apr-2023
TAPE AND REEL BOX DIMENSIONS
Width (mm)
W LH

*All dimensions are nominal
Device Package Type Package Drawing Pins SPQ Length (mm) Width (mm) Height (mm)
TPS259802ONRGER VQFN RGE 24 3000 338.0 355.0 50.0
TPS259803ONRGER VQFN RGE 24 3000 338.0 355.0 50.0
TPS259804ONRGER VQFN RGE 24 3000 338.0 355.0 50.0
TPS259807ONRGER VQFN RGE 24 3000 338.0 355.0 50.0
Pack Materials-Page 2
```

### Page 49

#### Raw extracted text

```text
GENERIC PACKAGE VIEW
Images above are just a representation of the package family, actual package may vary.
Refer to the product data sheet for package details.
RGE 24 VQFN - 1 mm max height
PLASTIC QUAD FLATPACK - NO LEAD
4204104/H
```

### Page 50

#### Extracted tables

Table 1:

```text
0.08 | C
```

Table 2:

```text
26 |
```

Table 3:

```text
0.1 | C | A | B
0.05 |  |  |
```

#### Raw extracted text

```text
www.ti.com
PACKAGE OUTLINE
C
SEE TERMINAL
DETAIL
24X 0.29
0.19
24X 0.475
0.275
1.0
0.8
(0.2) TYP
0.05
0.00
4X 2.5
(0.625)
(0.925)
1.45 0.1
0.85 0.1
2X 2.7 0.1
2X 0.5
A 4.1
3.9
B
4.1
3.9
0.29
0.19
0.475
0.275
VQFN - 1 mm max heightRGE0024M
PLASTIC QUAD FLATPACK - NO LEAD
4223975/B   03/2018
PIN 1 INDEX AREA
0.08 C
SEATING PLANE
1
6 13
18
7 12
24 19
(OPTIONAL)
PIN 1 ID
0.1 C A B
0.05
EXPOSED
THERMAL PAD
25
SYMM
SYMM
NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
    per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. The package thermal pad must be soldered to the printed circuit board for thermal and mechanical performance.
26
SCALE  3.000
DETAIL
OPTIONAL TERMINAL
TYPICAL
```

### Page 51

#### Raw extracted text

```text
EXAMPLE BOARD LAYOUT
RRGGEE00002244MM VVQQFFNN -- 11 mmmm mmaaxx hheeiigghhtt
PPLLAASSTTIICC QQUUAADD FFLLAATTPPAACCKK -- NNOO LLEEAADD
(2.7)
SYMM
24 19
24X (0.575)
1
18
(1.45) 24X (0.24) 25 (0.625)
(1.1)
(R0.05) TYP
TYP
SYMM (3.825)
(0.925)
(0.15) TYP
26 TYP
20X (0.5)
(0.85)
13
6
( 0.2) TYP
7 12
VIA
6X (1.1)
(3.825)
LAND PATTERN EXAMPLE
EXPOSED METAL SHOWN
SCALE:15X
0.07 MAX 0.07 MIN
ALL AROUND ALL AROUND
SOLDER MASK
METAL
OPENING
EXP M O E S T E A D L S O O P L E D N E IN R G MASK EXP M O E S T E A D L M SO E L T D A E L R U N M D A E S R K
NON SOLDER MASK
SOLDER MASK
DEFINED
DEFINED
(PREFERRED)
SOLDER MASK DETAILS
4223975/B 03/2018
NOTES: (continued)
4. This package is designed to be soldered to a thermal pad on the board. For more information, see Texas Instruments literature
number SLUA271 (www.ti.com/lit/slua271).
5. Vias are optional depending on application, refer to device data sheet. If any vias are implemented, refer to their locations shown
on this view. It is recommended that vias under paste be filled, plugged or tented.
www.ti.com
```

### Page 52

#### Raw extracted text

```text
www.ti.com
EXAMPLE STENCIL DESIGN
4X (0.694)
2X
(0.625)
2X
(1.3)
2X
(0.925)
2X
(0.76)
24X (0.575)
24X (0.24)
20X (0.5)
(3.825)
(3.825)
4X (1.188)
(R0.05) TYP
4223975/B   03/2018
VQFN - 1 mm max heightRGE0024M
PLASTIC QUAD FLATPACK - NO LEAD
NOTES: (continued)

6. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
   design recommendations.

25
26
SYMM
METAL
TYP
SOLDER PASTE EXAMPLE
BASED ON 0.125 mm THICK STENCIL

EXPOSED PAD 25
78% PRINTED SOLDER COVERAGE BY AREA UNDER PACKAGE
SCALE:20X
SYMM
1
6
7 12
13
18
1924
```

### Page 53

#### Raw extracted text

```text
IMPORTANT NOTICE AND DISCLAIMER
TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATASHEETS), DESIGN RESOURCES (INCLUDING REFERENCE
DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES AS IS
AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY
IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD
PARTY INTELLECTUAL PROPERTY RIGHTS.
These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate
TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable
standards, and any other safety, security, regulatory or other requirements.
These resources are subject to change without notice. TI grants you permission to use these resources only for development of an
application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license
is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you fully
indemnify TI and its representatives against any claims, damages, costs, losses, and liabilities arising out of your use of these resources.
TIs products are provided subject to TIs Terms of Sale, TIs General Quality Guidelines, or other applicable terms available either on
ti.com or provided in conjunction with such TI products. TIs provision of these resources does not expand or otherwise alter TIs applicable
warranties or warranty disclaimers for TI products. Unless TI explicitly designates a product as custom or customer-specified, TI products
are standard, catalog, general purpose devices.
TI objects to and rejects any additional or different terms you may propose.
IMPORTANT NOTICE
Copyright  2026, Texas Instruments Incorporated
Last updated 10/2025
```
