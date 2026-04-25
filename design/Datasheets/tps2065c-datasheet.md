# TPS20xxC and TPS20xxC-2 Current Limited, Power-Distribution Switches datasheet (Rev. H)

## Source

- Source PDF: [tps2065c-datasheet.pdf](tps2065c-datasheet.pdf)
- Generated Markdown: `tps2065c-datasheet.md`
- Page count: 50
- Conversion method: automated local extraction with pypdf and pdfplumber

## Extracted title and part identity

- TPS20xxC and TPS20xxC-2 Current Limited, Power-Distribution Switches datasheet (Rev. H)
- tps2065c datasheet
- TPS2069C-2
- TPS2041C
- TPS2061C
- TPS2065C-2
- TPS2068C
- TPS2069C

## Extraction summary

- Pages with substantial text extraction: 50/50
- Pages with extracted tables: 33/50
- Total extracted character count: 141865
- Extraction quality flag: usable

## PDF metadata

| Field | Value |
| --- | --- |
| Title | TPS20xxC and TPS20xxC-2 Current Limited, Power-Distribution Switches datasheet (Rev. H) |
| Author | Texas Instruments, Incorporated [SLVSAU6,H ] |
| Subject | Data Sheet |
| Creator | TopLeaf 8.0.011 |
| Producer | iText 2.1.7 by 1T3XT |

## Reviewed summary

### Curated design notes

- PDF review confirmed this markdown is derived from the TI TPS20xxC / TPS20xxC-2 family datasheet that includes TPS2065C and TPS2065C-2.
- The family covers fixed current-limited USB/power-distribution switches with 0.5 A, 1 A, 1.5 A, and 2 A options. TPS2065C is one of the 1.5 A
  variants in the family device table.
- The typical application diagram on page 1 shows VIN bypassed with 0.1 uF, VOUT decoupled with 150 uF, FLT pulled up through 10 kOhm, and an external
  EN or active-low EN control input. The 8-pin packages expose separate IN and OUT pins plus FLT, while the DGN PowerPAD is tied to GND for best
  thermal performance.
- Key family operating features from the PDF are +/-20% fixed current limit, 2 us fast overcurrent response, deglitched fault reporting,
  reverse-current blocking, built-in soft start, and optional output discharge on TPS20xxC parts.
- The temperature-related limits called out by the electrical tables include thermal shutdown at 135 deg C while in current limit, 155 deg C
  otherwise, and about 20 deg C hysteresis.
- Package/mechanical coverage is present for SOT-23-5 (2.90 mm x 1.60 mm), VSSOP-8 (3.00 mm x 3.00 mm), and MSOP-PowerPAD-8 (3.00 mm x 3.00 mm), with
  package-specific thermal information and orderable markings later in the PDF.
- Extraction limit: several page-1 symbols came through with font-encoding artifacts (for example uF glyphs), but the underlying design intent is
  recoverable and the raw extraction below remains searchable.

## Design-relevant extracted content

This section surfaces design-relevant snippets first. Full page-by-page raw extraction follows later for local search.

### Part number and ordering information

- shorted. The power-switch rise and fall times are / controlled to minimize current surges during turnon / and turnoff. / Device Information(1) / PART NUMBER PACKAGE BODY SIZE (NOM) / TPS20xxC, / TPS20xxC-2
- controlled to minimize current surges during turnon / and turnoff. / Device Information(1) / PART NUMBER PACKAGE BODY SIZE (NOM) / TPS20xxC, / TPS20xxC-2 / SOT-23 (5) 2.90 mm x 1.60 mm
- SOT-23 (5) 2.90 mm x 1.60 mm / VSSOP (8) 3.00 mm x 3.00 mm / MSOP-PowerPAD (8) 3.00 mm x 3.00 mm / (1) For all available packages, see the orderable addendum at / the end of the data sheet. / Typical Application Diagram / PARTNUMBER | PACKAGE | BODYSIZE(NOM)
- 12.3 Trademarks ........................................................... 25 / 12.4 Electrostatic Discharge Caution ............................ 25 / 12.5 Glossary ................................................................ 25 / 13 Mechanical, Packaging, and Orderable / Information ........................................................... 25 / 4 Revision History / NOTE: Page numbers for previous revisions may differ from page numbers in the current version.
- Changes from Revision G (July 2013) to Revision H Page / * Added ESD Ratings table, Feature Description section, Device Functional Modes, Application and Implementation / section, Power Supply Recommendations section, Layout section, Device and Documentation Support section, and / Mechanical, Packaging, and Orderable Information section ................................................................................................. 1 / * Deleted Devices table (previously Table 1) ........................................................................................................................... 4 / Changes from Revision F (August 2012) to Revision G Page / * Deleted (See Table 1) from Feature: UL Listed and CB-File No. E169910 ........................................................................... 1
- * Deleted Devices table (previously Table 1) ........................................................................................................................... 4 / Changes from Revision F (August 2012) to Revision G Page / * Deleted (See Table 1) from Feature: UL Listed and CB-File No. E169910 ........................................................................... 1 / * Changed From: PXKI To: PYKI in the DEVICE INFORMATION table SOT23-5 (DBV) column (TPS2069C) ...................... 4 / * Deleted Note 2 from : "UL listed and CB complete"............................................................................................................... 4 / Changes from Revision E (April 2012) to Revision F Page / * Added device TPS20xxC-2 ................................................................................................................................................... 1
- * Added device TPS20xxC-2 ................................................................................................................................................... 1 / * Changed Feature From: Ouput Discharge When TPS20XXC is Disabled To: Selected parts with (TPS20xxC) and / without (TPS20xxC-2) Output Discharge ............................................................................................................................... 1 / * Added devices TPS2041C, TPS2061C, TPS2065C-2, TPS2068C, and TPS2069C-2 to the Device Information table ....... 4 / * Added the TPS2069C-2 Device ............................................................................................................................................. 4 / * Added PXKI in the DEVICE INFORMATION table SOT23-5 (DBV) column (TPS2069C) .................................................... 4 / * Added devices TPS2041C, TPS2061C, TPS2065C-2, TPS2068C, and TPS2069C-2 to and removed Product Preview.... 4
- without (TPS20xxC-2) Output Discharge ............................................................................................................................... 1 / * Added devices TPS2041C, TPS2061C, TPS2065C-2, TPS2068C, and TPS2069C-2 to the Device Information table ....... 4 / * Added the TPS2069C-2 Device ............................................................................................................................................. 4 / * Added PXKI in the DEVICE INFORMATION table SOT23-5 (DBV) column (TPS2069C) .................................................... 4 / * Added devices TPS2041C, TPS2061C, TPS2065C-2, TPS2068C, and TPS2069C-2 to and removed Product Preview.... 4 / * Added Note 1 to the RECOMMENDED OPERATING CONDITIONS table........................................................................... 6 / * Added TPS2041C, TPS2061C, TPS2068C, TPS2065C-2 and TPS2069C-2 devices to IOUT in the RECOMMENDED
- * Added Note 1 to the RECOMMENDED OPERATING CONDITIONS table........................................................................... 6 / * Added TPS2041C, TPS2061C, TPS2068C, TPS2065C-2 and TPS2069C-2 devices to IOUT in the RECOMMENDED / OPERATING CONDITIONS table .......................................................................................................................................... 6 / * Added the DBV option to Power Switch RDS(on) 1.5 A rated output, 25 deg C mOhm ....................................................................... 7 / * Added the DBV option to Power Switch RDS(on) 1.5 A rated output ....................................................................................... 7 / * Changed ISO Current Limit ..................................................................................................................................................... 7 / 3
- * Added TPS2041C, TPS2061C, TPS2068C, TPS2065C-2 and TPS2069C-2 devices to IOUT in the RECOMMENDED / OPERATING CONDITIONS table .......................................................................................................................................... 6 / * Added the DBV option to Power Switch RDS(on) 1.5 A rated output, 25 deg C mOhm ....................................................................... 7 / * Added the DBV option to Power Switch RDS(on) 1.5 A rated output ....................................................................................... 7 / * Changed ISO Current Limit ..................................................................................................................................................... 7 / 3 / TPS2000C, TPS2001C, TPS2041C, TPS2051C, TPS2061C
- TPS2069C TPS2069C-2 / Submit Documentation FeedbackCopyright 2011-2016, Texas Instruments Incorporated / * Added Leakage Current ......................................................................................................................................................... 7 / * Added the DBV option to Power Switch RDS(on) 1.5 A rated output . ..................................................................................... 8 / * Changed ISO Current Limit ..................................................................................................................................................... 8 / * Added Leakage Current ......................................................................................................................................................... 8 / * Changed the second para graph of the ENABLE section .................................................................................................... 15
- * Added table Note 2, UL listed and CB complete.................................................................................................................... 4 / * Added VIH and VIL information to the ROC Table................................................................................................................... 6 / Changes from Revision B (September 2011) to Revision C Page / * Changed From: PXF1 To: PXFI and From: PSG1 To: PXGI in the DEVICE INFORMATION table MOSP-8 (DGK) / column .................................................................................................................................................................................... 4 / * Changed TPS2000C (MSOP-8) status From: Preview To: Active in Table 1 ........................................................................ 4 / * Changed the JACustom 2 A Rated DGK value from N/A to 110.3 ...................................................................................... 7
- * Changed the JACustom 2 A Rated DGK value from N/A to 110.3 ...................................................................................... 7 / * Added Figure 45 - DGK Package PCB Layout Example ..................................................................................................... 23 / Changes from Revision A (July 2011) to Revision B Page / * Added the DGK Package Information throughout the data sheet .......................................................................................... 4 / * Changed title of Figure 30 From: NEW FIG To: TPS2065C 50 Ohm Short Circuit .................................................................. 19 / Changes from Original (June 2011) to Revision A Page / * Changed the TPS2051C, TPS2065C, and TPS2069C Devices Status From: Preview To: Active ....................................... 4
- Product Folder Links: TPS2000C TPS2001C TPS2041C TPS2051C TPS2061C TPS2065C TPS2065C-2 TPS2068C / TPS2069C TPS2069C-2 / Submit Documentation Feedback Copyright 2011-2016, Texas Instruments Incorporated / (1) For the most current packaging and ordering information, see the Package Option Addendum at the end of this document, or see the TI / website at www.ti.com. / (2) "-" indicates the device is not available in this package. / 5 Device Comparison Table
- OUTPUT / DISCHARGE ENABLE BASE PART / NUMBER / PACKAGED DEVICE AND MARKING (1) / MSOP-8 (DGN) / PowerPAD(TM) / SOT23-5
- Internally connected to GND. Connect PAD to GND plane as a heatsink for the best thermal / performance. PAD may be left floating if desired. See Power Dissipation and Junction / Temperature for guidance. / MAXIMUM OPERATING CURRENT | OUTPUT DISCHARGE | ENABLE | BASEPART NUMBER | PACKAGED | DEVICEANDMA | RKING(1) / | | | | MSOP-8(DGN) PowerPAD(TM) | SOT23-5 (DBV) | VSSOP-8 (DGK) / 0.5 | Y | Low | TPS2041C | (2) | PYJI | / 0.5 | Y | High | TPS2051C | | VBYQ |
- product warranty. / 7.6 Electrical Characteristics: TJ = TA = 25 deg C / Unless otherwise noted: VIN = 5 V, VEN = VIN or VEN = GND, IOUT = 0 A. See Device Comparison Table for the rated current of / each part number. Parametrics over a wider operational range are shown in Electrical Characteristics: -40 deg C <= TJ <= 125 deg C (1). / PARAMETER TEST CONDITIONS (1) MIN TYP MAX UNIT / POWER SWITCH / RDS(on) Input - output resistance
- product warranty. / 7.7 Electrical Characteristics: -40 deg C <= TJ <= 125 deg C / Unless otherwise noted:4.5 V <= VIN <= 5.5 V, VEN = VIN or VEN = GND, IOUT = 0 A, typical values are at 5 V and 25 deg C. See / Device Comparison Table for the rated current of each part number. / PARAMETER TEST CONDITIONS (1) MIN TYP MAX UNIT / POWER SWITCH / RDS(ON) Input - output resistance

### Pin, pad, and terminal designations

- GNDFLT / RFLT / 10 k/c87 / Control Signal / VIN / 0.1 /c109F / 150 /c109F
- VIN / 0.1 /c109F / 150 /c109F / Fault Signal / Pad* / VOUT / * DGN only
- 0.1 /c109F / 150 /c109F / Fault Signal / Pad* / VOUT / * DGN only / EN or
- 1 / 1 Features / 1* Single Power Switch Family / * Pin-for-Pin With Existing TI Switch Portfolio / * Rated Currents of 0.5 A, 1 A, 1.5 A, 2 A / * +/-20% Accurate, Fixed, Constant Current Limit / * Fast Overcurrent Response: 2 us
- TPS20xxC-2 / SOT-23 (5) 2.90 mm x 1.60 mm / VSSOP (8) 3.00 mm x 3.00 mm / MSOP-PowerPAD (8) 3.00 mm x 3.00 mm / (1) For all available packages, see the orderable addendum at / the end of the data sheet. / Typical Application Diagram
- PARTNUMBER | PACKAGE | BODYSIZE(NOM) / TPS20xxC, TPS20xxC-2 | SOT-23(5) | 2.90mmx1.60mm / | VSSOP(8) | 3.00mmx3.00mm / | MSOP-PowerPAD(8) | 3.00mmx3.00mm / 2 / TPS2000C, TPS2001C, TPS2041C, TPS2051C, TPS2061C / TPS2065C, TPS2065C-2, TPS2068C, TPS2069C, TPS2069C-2
- 3 Description ............................................................. 1 / 4 Revision History..................................................... 2 / 5 Device Comparison Table..................................... 4 / 6 Pin Configuration and Functions ......................... 4 / 7 Specifications......................................................... 5 / 7.1 Absolute Maximum Ratings ...................................... 5 / 7.2 ESD Ratings.............................................................. 5
- 7.2 ESD Ratings.............................................................. 5 / 7.3 Recommended Operating Conditions....................... 6 / 7.4 Thermal Information: SOT-23 ................................... 6 / 7.5 Thermal Information: MSOP-PowerPAD .................. 6 / 7.6 Electrical Characteristics: TJ = TA = 25 deg C................. 7 / 7.7 Electrical Characteristics: -40 deg C <= TJ <= 125 deg C......... 8 / 7.8 Timing Requirements: TJ = TA = 25 deg C...................... 9
- 7.9 Typical Characteristics ............................................ 11 / 8 Detailed Description ............................................ 14 / 8.1 Overview ................................................................. 14 / 8.2 Functional Block Diagram ....................................... 14 / 8.3 Feature Description................................................. 14 / 8.4 Device Functional Modes........................................ 16 / 9 Application and Implementation ........................ 17
- 8.1 Overview ................................................................. 14 / 8.2 Functional Block Diagram ....................................... 14 / 8.3 Feature Description................................................. 14 / 8.4 Device Functional Modes........................................ 16 / 9 Application and Implementation ........................ 17 / 9.1 Application Information............................................ 17 / 9.2 Typical Application ................................................. 17
- 4 Revision History / NOTE: Page numbers for previous revisions may differ from page numbers in the current version. / Changes from Revision G (July 2013) to Revision H Page / * Added ESD Ratings table, Feature Description section, Device Functional Modes, Application and Implementation / section, Power Supply Recommendations section, Layout section, Device and Documentation Support section, and / Mechanical, Packaging, and Orderable Information section ................................................................................................. 1 / * Deleted Devices table (previously Table 1) ........................................................................................................................... 4
- * Changed title of Figure 30 From: NEW FIG To: TPS2065C 50 Ohm Short Circuit .................................................................. 19 / Changes from Original (June 2011) to Revision A Page / * Changed the TPS2051C, TPS2065C, and TPS2069C Devices Status From: Preview To: Active ....................................... 4 / * Corrected pinout numbers for the 5-PIN PACKAGE ............................................................................................................. 5 / 1GND 8 OUT / 2IN 7 OUT / 3IN 6 OUT
- 2IN 7 OUT / 3IN 6 OUT / 4EN/EN 5 FLT / PowerPAD / 4 / TPS2000C, TPS2001C, TPS2041C, TPS2051C, TPS2061C / TPS2065C, TPS2065C-2, TPS2068C, TPS2069C, TPS2069C-2
- NUMBER / PACKAGED DEVICE AND MARKING (1) / MSOP-8 (DGN) / PowerPAD(TM) / SOT23-5 / (DBV) / VSSOP-8
- 1.5 N High TPS2069C-2 PYSI / 2 Y Low TPS2000C BCMS - PXFI / 2 Y High TPS2001C VBWQ - PXGI / 6 Pin Configuration and Functions / DGN Package / 8-Pin MSOP-PowerPAD / Top View
- 2 Y High TPS2001C VBWQ - PXGI / 6 Pin Configuration and Functions / DGN Package / 8-Pin MSOP-PowerPAD / Top View / DGK Package / 8-Pin VSSOP
- 8-Pin MSOP-PowerPAD / Top View / DGK Package / 8-Pin VSSOP / Top View / Pin Functions - 8 Pins / PIN
- DGK Package / 8-Pin VSSOP / Top View / Pin Functions - 8 Pins / PIN / I/O DESCRIPTION / NAME NO.

### Specifications, ratings, and operating conditions

- TPS2000C, TPS2001C, TPS2041C, TPS2051C, TPS2061C / TPS2065C, TPS2065C-2, TPS2068C, TPS2069C, TPS2069C-2 / SLVSAU6H - JUNE 2011 - REVISED APRIL 2016 / TPS20xxCandTPS20xxC-2CurrentLimited,Power-DistributionSwitches / 1 / 1 Features / 1* Single Power Switch Family
- 1 Features / 1* Single Power Switch Family / * Pin-for-Pin With Existing TI Switch Portfolio / * Rated Currents of 0.5 A, 1 A, 1.5 A, 2 A / * +/-20% Accurate, Fixed, Constant Current Limit / * Fast Overcurrent Response: 2 us / * Deglitched Fault Reporting
- 1* Single Power Switch Family / * Pin-for-Pin With Existing TI Switch Portfolio / * Rated Currents of 0.5 A, 1 A, 1.5 A, 2 A / * +/-20% Accurate, Fixed, Constant Current Limit / * Fast Overcurrent Response: 2 us / * Deglitched Fault Reporting / * Selected Parts With (TPS20xxC) and Without
- * Pin-for-Pin With Existing TI Switch Portfolio / * Rated Currents of 0.5 A, 1 A, 1.5 A, 2 A / * +/-20% Accurate, Fixed, Constant Current Limit / * Fast Overcurrent Response: 2 us / * Deglitched Fault Reporting / * Selected Parts With (TPS20xxC) and Without / (TPS20xxC-2) Output Discharge
- * Deglitched Fault Reporting / * Selected Parts With (TPS20xxC) and Without / (TPS20xxC-2) Output Discharge / * Reverse Current Blocking / * Built-In Soft Start / * Ambient Temperature Range: -40 deg C to 85 deg C / * UL Listed and CB-File No. E169910
- switch family is intended for applications, such as / USB, where heavy capacitive loads and short circuits / are likely to be encountered. This family offers / multiple devices with fixed current-limit thresholds for / applications from 0.5 A to 2 A. / The TPS20xxC and TPS20xxC-2 family limits the / output current to a safe level by operating in a
- multiple devices with fixed current-limit thresholds for / applications from 0.5 A to 2 A. / The TPS20xxC and TPS20xxC-2 family limits the / output current to a safe level by operating in a / constant-current mode when the output load exceeds / the current limit threshold. This provides a predictable / fault current under all conditions. The fast overload
- applications from 0.5 A to 2 A. / The TPS20xxC and TPS20xxC-2 family limits the / output current to a safe level by operating in a / constant-current mode when the output load exceeds / the current limit threshold. This provides a predictable / fault current under all conditions. The fast overload / response time eases the burden on the main 5-V
- The TPS20xxC and TPS20xxC-2 family limits the / output current to a safe level by operating in a / constant-current mode when the output load exceeds / the current limit threshold. This provides a predictable / fault current under all conditions. The fast overload / response time eases the burden on the main 5-V / supply to provide regulated power when the output is
- output current to a safe level by operating in a / constant-current mode when the output load exceeds / the current limit threshold. This provides a predictable / fault current under all conditions. The fast overload / response time eases the burden on the main 5-V / supply to provide regulated power when the output is / shorted. The power-switch rise and fall times are
- response time eases the burden on the main 5-V / supply to provide regulated power when the output is / shorted. The power-switch rise and fall times are / controlled to minimize current surges during turnon / and turnoff. / Device Information(1) / PART NUMBER PACKAGE BODY SIZE (NOM)
- 4 Revision History..................................................... 2 / 5 Device Comparison Table..................................... 4 / 6 Pin Configuration and Functions ......................... 4 / 7 Specifications......................................................... 5 / 7.1 Absolute Maximum Ratings ...................................... 5 / 7.2 ESD Ratings.............................................................. 5 / 7.3 Recommended Operating Conditions....................... 6
- 5 Device Comparison Table..................................... 4 / 6 Pin Configuration and Functions ......................... 4 / 7 Specifications......................................................... 5 / 7.1 Absolute Maximum Ratings ...................................... 5 / 7.2 ESD Ratings.............................................................. 5 / 7.3 Recommended Operating Conditions....................... 6 / 7.4 Thermal Information: SOT-23 ................................... 6
- 6 Pin Configuration and Functions ......................... 4 / 7 Specifications......................................................... 5 / 7.1 Absolute Maximum Ratings ...................................... 5 / 7.2 ESD Ratings.............................................................. 5 / 7.3 Recommended Operating Conditions....................... 6 / 7.4 Thermal Information: SOT-23 ................................... 6 / 7.5 Thermal Information: MSOP-PowerPAD .................. 6
- 7 Specifications......................................................... 5 / 7.1 Absolute Maximum Ratings ...................................... 5 / 7.2 ESD Ratings.............................................................. 5 / 7.3 Recommended Operating Conditions....................... 6 / 7.4 Thermal Information: SOT-23 ................................... 6 / 7.5 Thermal Information: MSOP-PowerPAD .................. 6 / 7.6 Electrical Characteristics: TJ = TA = 25 deg C................. 7
- 7.1 Absolute Maximum Ratings ...................................... 5 / 7.2 ESD Ratings.............................................................. 5 / 7.3 Recommended Operating Conditions....................... 6 / 7.4 Thermal Information: SOT-23 ................................... 6 / 7.5 Thermal Information: MSOP-PowerPAD .................. 6 / 7.6 Electrical Characteristics: TJ = TA = 25 deg C................. 7 / 7.7 Electrical Characteristics: -40 deg C <= TJ <= 125 deg C......... 8
- 7.2 ESD Ratings.............................................................. 5 / 7.3 Recommended Operating Conditions....................... 6 / 7.4 Thermal Information: SOT-23 ................................... 6 / 7.5 Thermal Information: MSOP-PowerPAD .................. 6 / 7.6 Electrical Characteristics: TJ = TA = 25 deg C................. 7 / 7.7 Electrical Characteristics: -40 deg C <= TJ <= 125 deg C......... 8 / 7.8 Timing Requirements: TJ = TA = 25 deg C...................... 9
- 7.3 Recommended Operating Conditions....................... 6 / 7.4 Thermal Information: SOT-23 ................................... 6 / 7.5 Thermal Information: MSOP-PowerPAD .................. 6 / 7.6 Electrical Characteristics: TJ = TA = 25 deg C................. 7 / 7.7 Electrical Characteristics: -40 deg C <= TJ <= 125 deg C......... 8 / 7.8 Timing Requirements: TJ = TA = 25 deg C...................... 9 / 7.9 Typical Characteristics ............................................ 11

### Dimensions, package, and mechanical information

- controlled to minimize current surges during turnon / and turnoff. / Device Information(1) / PART NUMBER PACKAGE BODY SIZE (NOM) / TPS20xxC, / TPS20xxC-2 / SOT-23 (5) 2.90 mm x 1.60 mm
- SOT-23 (5) 2.90 mm x 1.60 mm / VSSOP (8) 3.00 mm x 3.00 mm / MSOP-PowerPAD (8) 3.00 mm x 3.00 mm / (1) For all available packages, see the orderable addendum at / the end of the data sheet. / Typical Application Diagram / PARTNUMBER | PACKAGE | BODYSIZE(NOM)
- (1) For all available packages, see the orderable addendum at / the end of the data sheet. / Typical Application Diagram / PARTNUMBER | PACKAGE | BODYSIZE(NOM) / TPS20xxC, TPS20xxC-2 | SOT-23(5) | 2.90mmx1.60mm / | VSSOP(8) | 3.00mmx3.00mm / | MSOP-PowerPAD(8) | 3.00mmx3.00mm
- 12.3 Trademarks ........................................................... 25 / 12.4 Electrostatic Discharge Caution ............................ 25 / 12.5 Glossary ................................................................ 25 / 13 Mechanical, Packaging, and Orderable / Information ........................................................... 25 / 4 Revision History / NOTE: Page numbers for previous revisions may differ from page numbers in the current version.
- Changes from Revision G (July 2013) to Revision H Page / * Added ESD Ratings table, Feature Description section, Device Functional Modes, Application and Implementation / section, Power Supply Recommendations section, Layout section, Device and Documentation Support section, and / Mechanical, Packaging, and Orderable Information section ................................................................................................. 1 / * Deleted Devices table (previously Table 1) ........................................................................................................................... 4 / Changes from Revision F (August 2012) to Revision G Page / * Deleted (See Table 1) from Feature: UL Listed and CB-File No. E169910 ........................................................................... 1
- column .................................................................................................................................................................................... 4 / * Changed TPS2000C (MSOP-8) status From: Preview To: Active in Table 1 ........................................................................ 4 / * Changed the JACustom 2 A Rated DGK value from N/A to 110.3 ...................................................................................... 7 / * Added Figure 45 - DGK Package PCB Layout Example ..................................................................................................... 23 / Changes from Revision A (July 2011) to Revision B Page / * Added the DGK Package Information throughout the data sheet .......................................................................................... 4 / * Changed title of Figure 30 From: NEW FIG To: TPS2065C 50 Ohm Short Circuit .................................................................. 19
- * Changed the JACustom 2 A Rated DGK value from N/A to 110.3 ...................................................................................... 7 / * Added Figure 45 - DGK Package PCB Layout Example ..................................................................................................... 23 / Changes from Revision A (July 2011) to Revision B Page / * Added the DGK Package Information throughout the data sheet .......................................................................................... 4 / * Changed title of Figure 30 From: NEW FIG To: TPS2065C 50 Ohm Short Circuit .................................................................. 19 / Changes from Original (June 2011) to Revision A Page / * Changed the TPS2051C, TPS2065C, and TPS2069C Devices Status From: Preview To: Active ....................................... 4
- * Changed title of Figure 30 From: NEW FIG To: TPS2065C 50 Ohm Short Circuit .................................................................. 19 / Changes from Original (June 2011) to Revision A Page / * Changed the TPS2051C, TPS2065C, and TPS2069C Devices Status From: Preview To: Active ....................................... 4 / * Corrected pinout numbers for the 5-PIN PACKAGE ............................................................................................................. 5 / 1GND 8 OUT / 2IN 7 OUT / 3IN 6 OUT
- Product Folder Links: TPS2000C TPS2001C TPS2041C TPS2051C TPS2061C TPS2065C TPS2065C-2 TPS2068C / TPS2069C TPS2069C-2 / Submit Documentation Feedback Copyright 2011-2016, Texas Instruments Incorporated / (1) For the most current packaging and ordering information, see the Package Option Addendum at the end of this document, or see the TI / website at www.ti.com. / (2) "-" indicates the device is not available in this package. / 5 Device Comparison Table
- Submit Documentation Feedback Copyright 2011-2016, Texas Instruments Incorporated / (1) For the most current packaging and ordering information, see the Package Option Addendum at the end of this document, or see the TI / website at www.ti.com. / (2) "-" indicates the device is not available in this package. / 5 Device Comparison Table / MAXIMUM / OPERATING
- OUTPUT / DISCHARGE ENABLE BASE PART / NUMBER / PACKAGED DEVICE AND MARKING (1) / MSOP-8 (DGN) / PowerPAD(TM) / SOT23-5
- 2 Y Low TPS2000C BCMS - PXFI / 2 Y High TPS2001C VBWQ - PXGI / 6 Pin Configuration and Functions / DGN Package / 8-Pin MSOP-PowerPAD / Top View / DGK Package
- DGN Package / 8-Pin MSOP-PowerPAD / Top View / DGK Package / 8-Pin VSSOP / Top View / Pin Functions - 8 Pins
- Internally connected to GND. Connect PAD to GND plane as a heatsink for the best thermal / performance. PAD may be left floating if desired. See Power Dissipation and Junction / Temperature for guidance. / MAXIMUM OPERATING CURRENT | OUTPUT DISCHARGE | ENABLE | BASEPART NUMBER | PACKAGED | DEVICEANDMA | RKING(1) / | | | | MSOP-8(DGN) PowerPAD(TM) | SOT23-5 (DBV) | VSSOP-8 (DGK) / 0.5 | Y | Low | TPS2041C | (2) | PYJI | / 0.5 | Y | High | TPS2051C | | VBYQ |
- Product Folder Links: TPS2000C TPS2001C TPS2041C TPS2051C TPS2061C TPS2065C TPS2065C-2 TPS2068C / TPS2069C TPS2069C-2 / Submit Documentation FeedbackCopyright 2011-2016, Texas Instruments Incorporated / DBV Package / 5-Pin SOT-23 / Top View / Pin Functions - 5 Pins
- Product Folder Links: TPS2000C TPS2001C TPS2041C TPS2051C TPS2061C TPS2065C TPS2065C-2 TPS2068C / TPS2069C TPS2069C-2 / Submit Documentation Feedback Copyright 2011-2016, Texas Instruments Incorporated / (1) Some package and current rating may request an ambient temperature derating of 85 deg C. / 7.3 Recommended Operating Conditions / MIN NOM MAX UNIT / VIN Input voltage, IN 4.5 5.5 V
- TPS2000C and TPS2001C 2 / TJ Operating junction temperature -40 125 deg C / IFLT Sink current into FLT 0 5 mA / (1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application / report, SPRA953. / (2) Rated at 0.5 A or 1 A. / (3) Rated at 1.5 A or 2 A.
- JB Junction-to-board characterization parameter 50.3 46.2 deg C/W / RJCbot Junction-to-case (bottom) thermal resistance - - deg C/W / RJACustom See Power DIssipation and Junction Temperature 139.3 134.9 deg C/W / (1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application / report, SPRA953. / (2) Rated at 0.5 A or 1 A. / (3) Rated at 1.5 A or 2 A.

### Formulas, equations, and configuration calculations

- 1* Single Power Switch Family / * Pin-for-Pin With Existing TI Switch Portfolio / * Rated Currents of 0.5 A, 1 A, 1.5 A, 2 A / * +/-20% Accurate, Fixed, Constant Current Limit / * Fast Overcurrent Response: 2 us / * Deglitched Fault Reporting / * Selected Parts With (TPS20xxC) and Without
- The TPS20xxC and TPS20xxC-2 family limits the / output current to a safe level by operating in a / constant-current mode when the output load exceeds / the current limit threshold. This provides a predictable / fault current under all conditions. The fast overload / response time eases the burden on the main 5-V / supply to provide regulated power when the output is
- 3 Description ............................................................. 1 / 4 Revision History..................................................... 2 / 5 Device Comparison Table..................................... 4 / 6 Pin Configuration and Functions ......................... 4 / 7 Specifications......................................................... 5 / 7.1 Absolute Maximum Ratings ...................................... 5 / 7.2 ESD Ratings.............................................................. 5
- OPERATING CONDITIONS table .......................................................................................................................................... 6 / * Added the DBV option to Power Switch RDS(on) 1.5 A rated output, 25 deg C mOhm ....................................................................... 7 / * Added the DBV option to Power Switch RDS(on) 1.5 A rated output ....................................................................................... 7 / * Changed ISO Current Limit ..................................................................................................................................................... 7 / 3 / TPS2000C, TPS2001C, TPS2041C, TPS2051C, TPS2061C / TPS2065C, TPS2065C-2, TPS2068C, TPS2069C, TPS2069C-2
- Submit Documentation FeedbackCopyright 2011-2016, Texas Instruments Incorporated / * Added Leakage Current ......................................................................................................................................................... 7 / * Added the DBV option to Power Switch RDS(on) 1.5 A rated output . ..................................................................................... 8 / * Changed ISO Current Limit ..................................................................................................................................................... 8 / * Added Leakage Current ......................................................................................................................................................... 8 / * Changed the second para graph of the ENABLE section .................................................................................................... 15 / * Added sentence to end of paragraph in the OUTPUT DISCHARGE section ...................................................................... 16
- 1.5 N High TPS2069C-2 PYSI / 2 Y Low TPS2000C BCMS - PXFI / 2 Y High TPS2001C VBWQ - PXGI / 6 Pin Configuration and Functions / DGN Package / 8-Pin MSOP-PowerPAD / Top View
- close to the IC / OUT 1 PWR Power-switch output, connect to load. / (1) Stresses beyond those listed under Absolute Maximum Ratings may cause permanent damage to the device. These are stress ratings / only, which do not imply functional operation of the device at these or any other conditions beyond those indicated under Recommended / Operating Conditions. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability. / (2) Absolute maximum ratings apply over recommended junction temperature range. / (3) Voltages are with respect to GND unless otherwise noted.
- TPS2069C TPS2069C-2 / Submit Documentation FeedbackCopyright 2011-2016, Texas Instruments Incorporated / (1) Pulsed testing techniques maintain junction temperature approximately equal to ambient temperature / (2) See Current Limit section for explanation of this parameter. / (3) These parameters are provided for reference only, and do not constitute part of TI's published device specifications for purposes of TI's / product warranty. / 7.6 Electrical Characteristics: TJ = TA = 25 deg C
- product warranty. / 7.6 Electrical Characteristics: TJ = TA = 25 deg C / Unless otherwise noted: VIN = 5 V, VEN = VIN or VEN = GND, IOUT = 0 A. See Device Comparison Table for the rated current of / each part number. Parametrics over a wider operational range are shown in Electrical Characteristics: -40 deg C <= TJ <= 125 deg C (1). / PARAMETER TEST CONDITIONS (1) MIN TYP MAX UNIT / POWER SWITCH / RDS(on) Input - output resistance
- 2-A rated output, 25 deg C DGN, DGK 72 84 mOhm / 2-A rated output, -40 deg C <= (TJ , TA) <= / 85 deg C DGN, DGK 72 98 mOhm / CURRENT LIMIT / IOS / (2) Current limit, / See Figure 6
- 85 deg C DGN, DGK 72 98 mOhm / CURRENT LIMIT / IOS / (2) Current limit, / See Figure 6 / 0.5-A rated output TPS20xxC 0.67 0.85 1.01 / A
- TPS2069C TPS2069C-2 / Submit Documentation Feedback Copyright 2011-2016, Texas Instruments Incorporated / (1) Pulsed testing techniques maintain junction temperature approximately equal to ambient temperature / (2) See Current Limit for explanation of this parameter. / (3) These parameters are provided for reference only, and do not constitute part of TI's published device specifications for purposes of TI's / product warranty. / 7.7 Electrical Characteristics: -40 deg C <= TJ <= 125 deg C
- Threshold Input rising 1 1.45 2 V / Hysteresis 0.07 0.13 0.2 V / Leakage current (VEN or VEN) = 0 V or 5.5 V -1 0 1 uA / CURRENT LIMIT / IOS / (2) Current limit, / See Figure 23
- Leakage current (VEN or VEN) = 0 V or 5.5 V -1 0 1 uA / CURRENT LIMIT / IOS / (2) Current limit, / See Figure 23 / 0.5-A rated output TPS20xxC 0.65 0.85 1.05 / A
- TPS20XXC-2 0.05 uA / IREV Reverse leakage current VOUT = 5.5 V, VIN = 0 V, measure IVOUT 0.2 20 uA / UNDERVOLTAGE LOCKOUT / VUVLO Rising threshold VIN 3.5 3.75 4 V / Hysteresis (3) VIN 0.14 V / FLT / Output low voltage, FLT IFLT = 1 mA 0.2 V
- VIN = 5 V, VOUT = 5 V, disabled TPS20XXC 300 470 800 / THERMAL SHUTDOWN / Rising threshold (TJ) / In current limit 135 / deg CNot in current limit 155 / Hysteresis (3) 20 / | PARAMETER | TESTCONDITIONS(1) | | MIN | TYP | MAX | UNIT
- THERMAL SHUTDOWN / Rising threshold (TJ) / In current limit 135 / deg CNot in current limit 155 / Hysteresis (3) 20 / | PARAMETER | TESTCONDITIONS(1) | | MIN | TYP | MAX | UNIT / POWERSWITCH | | | | | | |
- Ilkg Leakagecurrent | | VOUT=0V,VIN=5V,disabled, measureIVIN | TPS20XXC-2 | 0.05 | | | uA / IREV Reverseleakagecurrent | | VOUT=5.5V,VIN=0V,measureIVOUT | | 0.2 20 | | | uA / UNDERVOLTAGELOCKOUT | | | | | | | / VUVLO Risingthreshold | | VIN | | 3.5 3.75 4 | | | V / Hysteresis(3) | | VIN | | 0.14 | | | V / FLT | | | | | | | / Outputlowvoltage,FLT | | IFLT=1mA | | 0.2 | | | V

### Reference designs, applications, and examples

- Software / Support & / Community / An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications, / intellectual property matters and other important disclaimers. PRODUCTION DATA. / TPS2000C, TPS2001C, TPS2041C, TPS2051C, TPS2061C / TPS2065C, TPS2065C-2, TPS2068C, TPS2069C, TPS2069C-2
- * Built-In Soft Start / * Ambient Temperature Range: -40 deg C to 85 deg C / * UL Listed and CB-File No. E169910 / 2 Applications / * USB Ports and Hubs, Laptops, and Desktops / * High-Definition Digital TVs / * Set-Top Boxes
- * Short-Circuit Protection / 3 Description / The TPS20xxC and TPS20xxC-2 power-distribution / switch family is intended for applications, such as / USB, where heavy capacitive loads and short circuits / are likely to be encountered. This family offers / multiple devices with fixed current-limit thresholds for
- USB, where heavy capacitive loads and short circuits / are likely to be encountered. This family offers / multiple devices with fixed current-limit thresholds for / applications from 0.5 A to 2 A. / The TPS20xxC and TPS20xxC-2 family limits the / output current to a safe level by operating in a / constant-current mode when the output load exceeds
- MSOP-PowerPAD (8) 3.00 mm x 3.00 mm / (1) For all available packages, see the orderable addendum at / the end of the data sheet. / Typical Application Diagram / PARTNUMBER | PACKAGE | BODYSIZE(NOM) / TPS20xxC, TPS20xxC-2 | SOT-23(5) | 2.90mmx1.60mm / | VSSOP(8) | 3.00mmx3.00mm
- Submit Documentation Feedback Copyright 2011-2016, Texas Instruments Incorporated / Table of Contents / 1 Features .................................................................. 1 / 2 Applications ........................................................... 1 / 3 Description ............................................................. 1 / 4 Revision History..................................................... 2 / 5 Device Comparison Table..................................... 4
- 8.2 Functional Block Diagram ....................................... 14 / 8.3 Feature Description................................................. 14 / 8.4 Device Functional Modes........................................ 16 / 9 Application and Implementation ........................ 17 / 9.1 Application Information............................................ 17 / 9.2 Typical Application ................................................. 17 / 10 Power Supply Recommendations ..................... 21
- 8.3 Feature Description................................................. 14 / 8.4 Device Functional Modes........................................ 16 / 9 Application and Implementation ........................ 17 / 9.1 Application Information............................................ 17 / 9.2 Typical Application ................................................. 17 / 10 Power Supply Recommendations ..................... 21 / 11 Layout................................................................... 22
- 8.4 Device Functional Modes........................................ 16 / 9 Application and Implementation ........................ 17 / 9.1 Application Information............................................ 17 / 9.2 Typical Application ................................................. 17 / 10 Power Supply Recommendations ..................... 21 / 11 Layout................................................................... 22 / 11.1 Layout Guidelines ................................................. 22
- 10 Power Supply Recommendations ..................... 21 / 11 Layout................................................................... 22 / 11.1 Layout Guidelines ................................................. 22 / 11.2 Layout Example .................................................... 22 / 11.3 Power Dissipation and Junction Temperature ...... 22 / 12 Device and Documentation Support ................. 25 / 12.1 Related Links ........................................................ 25
- 4 Revision History / NOTE: Page numbers for previous revisions may differ from page numbers in the current version. / Changes from Revision G (July 2013) to Revision H Page / * Added ESD Ratings table, Feature Description section, Device Functional Modes, Application and Implementation / section, Power Supply Recommendations section, Layout section, Device and Documentation Support section, and / Mechanical, Packaging, and Orderable Information section ................................................................................................. 1 / * Deleted Devices table (previously Table 1) ........................................................................................................................... 4
- column .................................................................................................................................................................................... 4 / * Changed TPS2000C (MSOP-8) status From: Preview To: Active in Table 1 ........................................................................ 4 / * Changed the JACustom 2 A Rated DGK value from N/A to 110.3 ...................................................................................... 7 / * Added Figure 45 - DGK Package PCB Layout Example ..................................................................................................... 23 / Changes from Revision A (July 2011) to Revision B Page / * Added the DGK Package Information throughout the data sheet .......................................................................................... 4 / * Changed title of Figure 30 From: NEW FIG To: TPS2065C 50 Ohm Short Circuit .................................................................. 19
- Storage temperature, Tstg -60 150 deg C / (1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process. / (2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process. / (3) VOUT was surged on a PCB with input and output bypassing per the Typical Application Diagram on the first page (except input / capacitor was 22 uF) with no device failures. / 7.2 ESD Ratings / VALUE UNIT
- TPS2000C and TPS2001C 2 / TJ Operating junction temperature -40 125 deg C / IFLT Sink current into FLT 0 5 mA / (1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application / report, SPRA953. / (2) Rated at 0.5 A or 1 A. / (3) Rated at 1.5 A or 2 A.
- JB Junction-to-board characterization parameter 50.3 46.2 deg C/W / RJCbot Junction-to-case (bottom) thermal resistance - - deg C/W / RJACustom See Power DIssipation and Junction Temperature 139.3 134.9 deg C/W / (1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application / report, SPRA953. / (2) Rated at 0.5 A or 1 A. / (3) Rated at 1.5 A or 2 A.
- tIOS Short-circuit response time (3) / VIN = 5 V (see Figure 6), / One-half full load -> RSHORT = 50 mOhm, / Measure from application to when current falls below 120% of / final value / 2 us / SUPPLY CURRENT
- | | 1.5-Aratedoutput | TPS20xxC | 1.6 2.15 2.7 | | | / | | | TPS20xxC-2 | 1.6 2.23 2.86 | | | / | | 2-Aratedoutput | TPS20xxC | 2.3 2.9 3.6 | | | / tIOS Short-circuitresponsetime(3) | | VIN=5V(seeFigure6), One-halffullload->RSHORT=50mOhm, Measurefromapplicationtowhencurrentfallsbelow120%of finalvalue | | 2 | | | us / SUPPLYCURRENT | | | | | | | / ISD Supplycurrent,switchdisabled | | IOUT=0A | | 0.01 10 | | | uA / ISE Supplycurrent,switchenabled | | IOUT=0A | | 65 90 | | | uA
- 8.1 Overview / The TPS20xxC and TPS20xxC-2 are current-limited, power-distribution switches providing a range from 0.5 A / and 2 A of continuous load current in 5-V circuits. These parts use N-channel MOSFETs for low resistance, / maintaining voltage regulation to the load. They are designed for applications where short circuits or heavy / capacitive loads are encountered. Device features include enable, reverse blocking when disabled, output / discharge pulldown, overcurrent protection, overtemperature protection, and deglitched fault reporting. / 8.2 Functional Block Diagram

## Page-by-page extracted content

### Page 1

#### Extracted tables

Table 1:

```text
PARTNUMBER | PACKAGE | BODYSIZE(NOM)
TPS20xxC, TPS20xxC-2 | SOT-23(5) | 2.90mmx1.60mm
 | VSSOP(8) | 3.00mmx3.00mm
 | MSOP-PowerPAD(8) | 3.00mmx3.00mm
```

#### Raw extracted text

```text
OUTIN
GNDFLT
RFLT
10 k/c87
Control Signal
VIN
0.1 /c109F
150 /c109F
Fault Signal
Pad*
VOUT
* DGN only
EN or
EN
Copyright  2016, Texas Instruments Incorporated
Product
Folder
Sample &
Buy
T echnical
Documents
Tools &
Software
Support &
Community
An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications,
intellectual property matters and other important disclaimers. PRODUCTION DATA.
TPS2000C, TPS2001C, TPS2041C, TPS2051C, TPS2061C
TPS2065C, TPS2065C-2, TPS2068C, TPS2069C, TPS2069C-2
SLVSAU6H - JUNE 2011 - REVISED APRIL 2016
TPS20xxCandTPS20xxC-2CurrentLimited,Power-DistributionSwitches
1
1 Features
1* Single Power Switch Family
* Pin-for-Pin With Existing TI Switch Portfolio
* Rated Currents of 0.5 A, 1 A, 1.5 A, 2 A
* +/-20% Accurate, Fixed, Constant Current Limit
* Fast Overcurrent Response: 2 us
* Deglitched Fault Reporting
* Selected Parts With (TPS20xxC) and Without
(TPS20xxC-2) Output Discharge
* Reverse Current Blocking
* Built-In Soft Start
* Ambient Temperature Range: -40 deg C to 85 deg C
* UL Listed and CB-File No. E169910
2 Applications
* USB Ports and Hubs, Laptops, and Desktops
* High-Definition Digital TVs
* Set-Top Boxes
* Short-Circuit Protection
3 Description
The TPS20xxC and TPS20xxC-2 power-distribution
switch family is intended for applications, such as
USB, where heavy capacitive loads and short circuits
are likely to be encountered. This family offers
multiple devices with fixed current-limit thresholds for
applications from 0.5 A to 2 A.
The TPS20xxC and TPS20xxC-2 family limits the
output current to a safe level by operating in a
constant-current mode when the output load exceeds
the current limit threshold. This provides a predictable
fault current under all conditions. The fast overload
response time eases the burden on the main 5-V
supply to provide regulated power when the output is
shorted. The power-switch rise and fall times are
controlled to minimize current surges during turnon
and turnoff.
Device Information(1)
PART NUMBER PACKAGE BODY SIZE (NOM)
TPS20xxC,
TPS20xxC-2
SOT-23 (5) 2.90 mm x 1.60 mm
VSSOP (8) 3.00 mm x 3.00 mm
MSOP-PowerPAD (8) 3.00 mm x 3.00 mm
(1) For all available packages, see the orderable addendum at
the end of the data sheet.
Typical Application Diagram
```

### Page 2

#### Raw extracted text

```text
2
TPS2000C, TPS2001C, TPS2041C, TPS2051C, TPS2061C
TPS2065C, TPS2065C-2, TPS2068C, TPS2069C, TPS2069C-2
SLVSAU6H - JUNE 2011 - REVISED APRIL 2016 www.ti.com
Product Folder Links: TPS2000C TPS2001C TPS2041C TPS2051C TPS2061C TPS2065C TPS2065C-2 TPS2068C
TPS2069C TPS2069C-2
Submit Documentation Feedback Copyright  2011-2016, Texas Instruments Incorporated
Table of Contents
1 Features .................................................................. 1
2 Applications ........................................................... 1
3 Description ............................................................. 1
4 Revision History..................................................... 2
5 Device Comparison Table..................................... 4
6 Pin Configuration and Functions ......................... 4
7 Specifications......................................................... 5
7.1 Absolute Maximum Ratings ...................................... 5
7.2 ESD Ratings.............................................................. 5
7.3 Recommended Operating Conditions....................... 6
7.4 Thermal Information: SOT-23 ................................... 6
7.5 Thermal Information: MSOP-PowerPAD .................. 6
7.6 Electrical Characteristics: TJ = TA = 25 deg C................. 7
7.7 Electrical Characteristics: -40 deg C <= TJ <= 125 deg C......... 8
7.8 Timing Requirements: TJ = TA = 25 deg C...................... 9
7.9 Typical Characteristics ............................................ 11
8 Detailed Description ............................................ 14
8.1 Overview ................................................................. 14
8.2 Functional Block Diagram ....................................... 14
8.3 Feature Description................................................. 14
8.4 Device Functional Modes........................................ 16
9 Application and Implementation ........................ 17
9.1 Application Information............................................ 17
9.2 Typical Application ................................................. 17
10 Power Supply Recommendations ..................... 21
11 Layout................................................................... 22
11.1 Layout Guidelines ................................................. 22
11.2 Layout Example .................................................... 22
11.3 Power Dissipation and Junction Temperature ...... 22
12 Device and Documentation Support ................. 25
12.1 Related Links ........................................................ 25
12.2 Community Resources.......................................... 25
12.3 Trademarks ........................................................... 25
12.4 Electrostatic Discharge Caution ............................ 25
12.5 Glossary ................................................................ 25
13 Mechanical, Packaging, and Orderable
Information ........................................................... 25
4 Revision History
NOTE: Page numbers for previous revisions may differ from page numbers in the current version.
Changes from Revision G (July 2013) to Revision H Page
* Added ESD Ratings table, Feature Description section, Device Functional Modes, Application and Implementation
section, Power Supply Recommendations section, Layout section, Device and Documentation Support section, and
Mechanical, Packaging, and Orderable Information section ................................................................................................. 1
* Deleted Devices table (previously Table 1) ........................................................................................................................... 4
Changes from Revision F (August 2012) to Revision G Page
* Deleted (See Table 1) from Feature: UL Listed and CB-File No. E169910 ........................................................................... 1
* Changed From: PXKI To: PYKI in the DEVICE INFORMATION table SOT23-5 (DBV) column (TPS2069C) ...................... 4
* Deleted Note 2 from : "UL listed and CB complete"............................................................................................................... 4
Changes from Revision E (April 2012) to Revision F Page
* Added device TPS20xxC-2 ................................................................................................................................................... 1
* Changed Feature From: Ouput Discharge When TPS20XXC is Disabled To: Selected parts with (TPS20xxC) and
without (TPS20xxC-2) Output Discharge ............................................................................................................................... 1
* Added devices TPS2041C, TPS2061C, TPS2065C-2, TPS2068C, and TPS2069C-2 to the Device Information table ....... 4
* Added the TPS2069C-2 Device ............................................................................................................................................. 4
* Added PXKI in the DEVICE INFORMATION table SOT23-5 (DBV) column (TPS2069C) .................................................... 4
* Added devices TPS2041C, TPS2061C, TPS2065C-2, TPS2068C, and TPS2069C-2 to and removed Product Preview.... 4
* Added Note 1 to the RECOMMENDED OPERATING CONDITIONS table........................................................................... 6
* Added TPS2041C, TPS2061C, TPS2068C, TPS2065C-2 and TPS2069C-2 devices to IOUT in the RECOMMENDED
OPERATING CONDITIONS table .......................................................................................................................................... 6
* Added the DBV option to Power Switch RDS(on) 1.5 A rated output, 25 deg C mOhm ....................................................................... 7
* Added the DBV option to Power Switch RDS(on) 1.5 A rated output ....................................................................................... 7
* Changed ISO Current Limit ..................................................................................................................................................... 7
```

### Page 3

#### Raw extracted text

```text
3
TPS2000C, TPS2001C, TPS2041C, TPS2051C, TPS2061C
TPS2065C, TPS2065C-2, TPS2068C, TPS2069C, TPS2069C-2
www.ti.com SLVSAU6H - JUNE 2011 - REVISED APRIL 2016
Product Folder Links: TPS2000C TPS2001C TPS2041C TPS2051C TPS2061C TPS2065C TPS2065C-2 TPS2068C
TPS2069C TPS2069C-2
Submit Documentation FeedbackCopyright  2011-2016, Texas Instruments Incorporated
* Added Leakage Current ......................................................................................................................................................... 7
* Added the DBV option to Power Switch RDS(on) 1.5 A rated output . ..................................................................................... 8
* Changed ISO Current Limit ..................................................................................................................................................... 8
* Added Leakage Current ......................................................................................................................................................... 8
* Changed the second para graph of the ENABLE section .................................................................................................... 15
* Added sentence to end of paragraph in the OUTPUT DISCHARGE section ...................................................................... 16
Changes from Revision D (February 2012) to Revision E Page
* Changed the POWER DISSIPATION AND JUNCTION TEMPERATURE section. Replaced paragraph " While it is
recommended..."................................................................................................................................................................... 22
Changes from Revision C (October 2011) to Revision D Page
* Added Feature UL Listed and CB-File No. E169910 (See ) .................................................................................................. 1
* Added table Note 2, UL listed and CB complete.................................................................................................................... 4
* Added VIH and VIL information to the ROC Table................................................................................................................... 6
Changes from Revision B (September 2011) to Revision C Page
* Changed From: PXF1 To: PXFI and From: PSG1 To: PXGI in the DEVICE INFORMATION table MOSP-8 (DGK)
column .................................................................................................................................................................................... 4
* Changed TPS2000C (MSOP-8) status From: Preview To: Active in Table 1 ........................................................................ 4
* Changed the JACustom 2 A Rated DGK value from N/A to 110.3 ...................................................................................... 7
* Added Figure 45 - DGK Package PCB Layout Example ..................................................................................................... 23
Changes from Revision A (July 2011) to Revision B Page
* Added the DGK Package Information throughout the data sheet .......................................................................................... 4
* Changed title of Figure 30 From: NEW FIG To: TPS2065C 50 Ohm Short Circuit .................................................................. 19
Changes from Original (June 2011) to Revision A Page
* Changed the TPS2051C, TPS2065C, and TPS2069C Devices Status From: Preview To: Active ....................................... 4
* Corrected pinout numbers for the 5-PIN PACKAGE ............................................................................................................. 5
```

### Page 4

#### Extracted tables

Table 1:

```text
MAXIMUM OPERATING CURRENT | OUTPUT DISCHARGE | ENABLE | BASEPART NUMBER | PACKAGED | DEVICEANDMA | RKING(1)
 |  |  |  | MSOP-8(DGN) PowerPAD(TM) | SOT23-5 (DBV) | VSSOP-8 (DGK)
0.5 | Y | Low | TPS2041C | (2) | PYJI | 
0.5 | Y | High | TPS2051C |  | VBYQ | 
1 | Y | Low | TPS2061C | PXMI | PXLI | 
1 | Y | High | TPS2065C | VCAQ | VCAQ | 
1 | N | High | TPS2065C-2 | PYRI | PYQI | 
1.5 | Y | Low | TPS2068C | PXNI |  | 
1.5 | Y | High | TPS2069C | VBUQ | PYKI | 
1.5 | N | High | TPS2069C-2 | PYSI |  | 
2 | Y | Low | TPS2000C | BCMS |  | PXFI
2 | Y | High | TPS2001C | VBWQ |  | PXGI
```

Table 2:

```text
PI | N | I/O | DESCRIPTION
NAME | NO. |  | 
EN/EN | 4 | I | Enableinput,logichighturnsonpowerswitch
FLT | 5 | O | Active-lowopen-drainoutput,assertedduringovercurrent,orovertemperatureconditions
GND | 1 |  | Groundconnection
IN | 2,3 | PWR | Inputvoltageandpower-switchdrain;connecta0.1-uForgreaterceramiccapacitorfromINto GNDclosetotheIC
OUT | 6,7,8 | PWR | Power-switchoutput,connecttoload
PowerPAD (DGNOnly) | PowerPAD |  | InternallyconnectedtoGND.ConnectPADtoGNDplaneasaheatsinkforthebestthermal performance.PADmaybeleftfloatingifdesired.SeePowerDissipationandJunction Temperatureforguidance.
```

#### Raw extracted text

```text
1GND 8 OUT
2IN 7 OUT
3IN 6 OUT
4EN/EN 5 FLT
1GND 8 OUT
2IN 7 OUT
3IN 6 OUT
4EN/EN 5 FLT
PowerPAD
4
TPS2000C, TPS2001C, TPS2041C, TPS2051C, TPS2061C
TPS2065C, TPS2065C-2, TPS2068C, TPS2069C, TPS2069C-2
SLVSAU6H - JUNE 2011 - REVISED APRIL 2016 www.ti.com
Product Folder Links: TPS2000C TPS2001C TPS2041C TPS2051C TPS2061C TPS2065C TPS2065C-2 TPS2068C
TPS2069C TPS2069C-2
Submit Documentation Feedback Copyright  2011-2016, Texas Instruments Incorporated
(1) For the most current packaging and ordering information, see the Package Option Addendum at the end of this document, or see the TI
website at www.ti.com.
(2) "-" indicates the device is not available in this package.
5 Device Comparison Table
MAXIMUM
OPERATING
CURRENT
OUTPUT
DISCHARGE ENABLE BASE PART
NUMBER
PACKAGED DEVICE AND MARKING (1)
MSOP-8 (DGN)
PowerPAD(TM)
SOT23-5
(DBV)
VSSOP-8
(DGK)
0.5 Y Low TPS2041C - (2) PYJI -
0.5 Y High TPS2051C - VBYQ -
1 Y Low TPS2061C PXMI PXLI -
1 Y High TPS2065C VCAQ VCAQ -
1 N High TPS2065C-2 PYRI PYQI -
1.5 Y Low TPS2068C PXNI - -
1.5 Y High TPS2069C VBUQ PYKI -
1.5 N High TPS2069C-2 PYSI - -
2 Y Low TPS2000C BCMS - PXFI
2 Y High TPS2001C VBWQ - PXGI
6 Pin Configuration and Functions
DGN Package
8-Pin MSOP-PowerPAD
Top View
DGK Package
8-Pin VSSOP
Top View
Pin Functions - 8 Pins
PIN
I/O DESCRIPTION
NAME NO.
EN/EN 4 I Enable input, logic high turns on power switch
FLT 5 O Active-low open-drain output, asserted during overcurrent, or overtemperature conditions
GND 1 - Ground connection
IN 2, 3 PWR Input voltage and power-switch drain; connect a 0.1-uF or greater ceramic capacitor from IN to
GND close to the IC
OUT 6, 7, 8 PWR Power-switch output, connect to load
PowerPAD
(DGN Only) PowerPAD -
Internally connected to GND. Connect PAD to GND plane as a heatsink for the best thermal
performance. PAD may be left floating if desired. See Power Dissipation and Junction
Temperature for guidance.
```

### Page 5

#### Extracted tables

Table 1:

```text
PIN |  | I/O | DESCRIPTION
NAME | NO. |  | 
EN/EN | 4 | I | Enableinput,logichighturnsonpowerswitch
FLT | 3 | O | Active-lowopen-drainoutput,assertedduringovercurrent,orovertemperatureconditions
GND | 2 |  | Groundconnection
IN | 5 | PWR | Inputvoltageandpower-switchdrain;connecta0.1-uForgreaterceramiccapacitorfromINtoGND closetotheIC
OUT | 1 | PWR | Power-switchoutput,connecttoload.
```

Table 2:

```text
|  | MIN | MAX | UNIT
VoltageonIN,OUT,ENorEN,FLT (4) |  | 0.3 6 |  | V
VoltagefromINtoOUT |  | 6 6 |  | V
Maximumjunctiontemperature,T J |  | InternallyLimited |  | 
Storagetemperature,T stg |  | 60 150 |  | deg C
```

Table 3:

```text
|  |  | VALUE | UNIT
V Electrostaticdischarge (ESD) |  | Human-bodymodel(HBM),perANSI/ESDA/JEDECJS-001(1) | +/-2000 | V
 |  | Charged-devicemodel(CDM),perJEDECspecificationJESD22-C101(2) | +/-500 | 
 |  | IEC61000-4-2contactdischarge | +/-8000 | 
 |  | IEC61000-4-2air-gapdischarge(3) | +/-15000 |
```

#### Raw extracted text

```text
1OUT
2GND
3FLT 4 EN/EN
5 IN
5
TPS2000C, TPS2001C, TPS2041C, TPS2051C, TPS2061C
TPS2065C, TPS2065C-2, TPS2068C, TPS2069C, TPS2069C-2
www.ti.com SLVSAU6H - JUNE 2011 - REVISED APRIL 2016
Product Folder Links: TPS2000C TPS2001C TPS2041C TPS2051C TPS2061C TPS2065C TPS2065C-2 TPS2068C
TPS2069C TPS2069C-2
Submit Documentation FeedbackCopyright  2011-2016, Texas Instruments Incorporated
DBV Package
5-Pin SOT-23
Top View
Pin Functions - 5 Pins
PIN
I/O DESCRIPTION
NAME NO.
EN/EN 4 I Enable input, logic high turns on power switch
FLT 3 O Active-low open-drain output, asserted during overcurrent, or overtemperature conditions
GND 2 - Ground connection
IN 5 PWR Input voltage and power-switch drain; connect a 0.1-uF or greater ceramic capacitor from IN to GND
close to the IC
OUT 1 PWR Power-switch output, connect to load.
(1) Stresses beyond those listed under Absolute Maximum Ratings may cause permanent damage to the device. These are stress ratings
only, which do not imply functional operation of the device at these or any other conditions beyond those indicated under Recommended
Operating Conditions. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability.
(2) Absolute maximum ratings apply over recommended junction temperature range.
(3) Voltages are with respect to GND unless otherwise noted.
(4) See Input and Output Capacitance.
7 Specifications
7.1 Absolute Maximum Ratings
over operating free-air temperature range (unless otherwise noted) (1) (2) (3)
MIN MAX UNIT
Voltage on IN, OUT, EN or EN, FLT (4) -0.3 6 V
Voltage from IN to OUT -6 6 V
Maximum junction temperature, TJ Internally Limited
Storage temperature, Tstg -60 150  deg C
(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process.
(2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process.
(3) VOUT was surged on a PCB with input and output bypassing per the Typical Application Diagram on the first page (except input
capacitor was 22 uF) with no device failures.
7.2 ESD Ratings
VALUE UNIT
V(ESD) Electrostatic discharge
Human-body model (HBM), per ANSI/ESDA/JEDEC JS-001 (1) +/-2000
V
Charged-device model (CDM), per JEDEC specification JESD22-C101 (2) +/-500
IEC 61000-4-2 contact discharge +/-8000
IEC 61000-4-2 air-gap discharge (3) +/-15000
```

### Page 6

#### Extracted tables

Table 1:

```text
|  |  | MIN | NOM | MAX | UNIT
V Inputvoltage,IN IN |  |  | 4.5 5.5 |  |  | V
V Inputvoltage,ENorEN EN |  |  | 0 5.5 |  |  | V
V High-levelinputvoltage,ENorEN IH |  |  | 2 |  |  | V
V Low-levelinputvoltage,ENorEN IL |  |  | 0.7 |  |  | V
Continuousoutputcurrent, I OUT OUT(1) |  | TPS2041CandTPS2051C | 0.5 |  |  | A
 |  | TPS2061C,TPS2065CandTPS2065C-2 | 1 |  |  | 
 |  | TPS2068C,TPS2069CandTPS2069C-2 | 1.5 |  |  | 
 |  | TPS2000CandTPS2001C | 2 |  |  | 
T Operatingjunctiontemperature J |  |  | 40 125 |  |  | deg C
I SinkcurrentintoFLT FLT |  |  | 0 5 |  |  | mA
```

Table 2:

```text
| THERMALMETRIC(1) | TPS20xxC,T | PS20xxC-2 | UNIT
 |  | DBV(SOT-23)(2) | DBV(SOT-23)(3) | 
 |  | 5PINS | 5PINS | 
R Junction-to-ambientthermalresistance JA |  | 224.9 | 220.4 | deg C/W
R Junction-to-case(top)thermalresistance JCtop |  | 95.2 | 89.7 | deg C/W
R Junction-to-boardthermalresistance JB |  | 51.4 | 46.9 | deg C/W
Junction-to-topcharacterizationparameter JT |  | 6.6 | 5.2 | deg C/W
Junction-to-boardcharacterizationparameter JB |  | 50.3 | 46.2 | deg C/W
R Junction-to-case(bottom)thermalresistance JCbot |  |  |  | deg C/W
R Custom SeePowerDIssipationandJunctionTemperature JA |  | 139.3 | 134.9 | deg C/W
```

Table 3:

```text
| THERMALMETRIC(1) | TPS | 20xxC,TPS20xx | C-2 | UNIT
 |  | DGN (MSOP- PowerPAD)(2) | DGN (MSOP- PowerPAD)(3) | DGK (VSSOP)(4) | 
 |  | 8PINS | 8PINS | 8PINS | 
R Junction-to-ambientthermalresistance JA |  | 72.1 | 67.1 | 205.5 | deg C/W
R Junction-to-case(top)thermalresistance JC(top) |  | 87.3 | 80.8 | 94.3 | deg C/W
R Junction-to-boardthermalresistance JB |  | 42.2 | 37.2 | 126.9 | deg C/W
Junction-to-topcharacterizationparameter JT |  | 7.3 | 5.6 | 24.7 | deg C/W
Junction-to-boardcharacterizationparameter JB |  | 42 | 36.9 | 125.2 | deg C/W
R Junction-to-case(bottom)thermalresistance JC(bot) |  | 39.2 | 32.1 |  | deg C/W
R Custom SeePowerDIssipationandJunctionTemperature JA |  | 66.5 | 61.3 | 110.3 | deg C/W
```

#### Raw extracted text

```text
6
TPS2000C, TPS2001C, TPS2041C, TPS2051C, TPS2061C
TPS2065C, TPS2065C-2, TPS2068C, TPS2069C, TPS2069C-2
SLVSAU6H - JUNE 2011 - REVISED APRIL 2016 www.ti.com
Product Folder Links: TPS2000C TPS2001C TPS2041C TPS2051C TPS2061C TPS2065C TPS2065C-2 TPS2068C
TPS2069C TPS2069C-2
Submit Documentation Feedback Copyright  2011-2016, Texas Instruments Incorporated
(1) Some package and current rating may request an ambient temperature derating of 85 deg C.
7.3 Recommended Operating Conditions
MIN NOM MAX UNIT
VIN Input voltage, IN 4.5 5.5 V
VEN Input voltage, EN or EN 0 5.5 V
VIH High-level input voltage, EN or EN 2 V
VIL Low-level input voltage, EN or EN 0.7 V
IOUT
Continuous output current,
OUT (1)
TPS2041C and TPS2051C 0.5
A
TPS2061C, TPS2065C and TPS2065C-2 1
TPS2068C, TPS2069C and TPS2069C-2 1.5
TPS2000C and TPS2001C 2
TJ Operating junction temperature -40 125  deg C
IFLT Sink current into FLT 0 5 mA
(1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application
report, SPRA953.
(2) Rated at 0.5 A or 1 A.
(3) Rated at 1.5 A or 2 A.
7.4 Thermal Information: SOT-23
THERMAL METRIC (1)
TPS20xxC, TPS20xxC-2
UNITDBV (SOT-23) (2) DBV (SOT-23) (3)
5 PINS 5 PINS
RJA Junction-to-ambient thermal resistance 224.9 220.4  deg C/W
RJCtop Junction-to-case (top) thermal resistance 95.2 89.7  deg C/W
RJB Junction-to-board thermal resistance 51.4 46.9  deg C/W
JT Junction-to-top characterization parameter 6.6 5.2  deg C/W
JB Junction-to-board characterization parameter 50.3 46.2  deg C/W
RJCbot Junction-to-case (bottom) thermal resistance - -  deg C/W
RJACustom See Power DIssipation and Junction Temperature 139.3 134.9  deg C/W
(1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application
report, SPRA953.
(2) Rated at 0.5 A or 1 A.
(3) Rated at 1.5 A or 2 A.
(4) Rated at 2 A.
7.5 Thermal Information: MSOP-PowerPAD
THERMAL METRIC (1)
TPS20xxC, TPS20xxC-2
UNIT
DGN
(MSOP-
PowerPAD) (2)
DGN
(MSOP-
PowerPAD) (3)
DGK
(VSSOP) (4)
8 PINS 8 PINS 8 PINS
RJA Junction-to-ambient thermal resistance 72.1 67.1 205.5  deg C/W
RJC(top) Junction-to-case (top) thermal resistance 87.3 80.8 94.3  deg C/W
RJB Junction-to-board thermal resistance 42.2 37.2 126.9  deg C/W
JT Junction-to-top characterization parameter 7.3 5.6 24.7  deg C/W
JB Junction-to-board characterization parameter 42 36.9 125.2  deg C/W
RJC(bot) Junction-to-case (bottom) thermal resistance 39.2 32.1 -  deg C/W
RJACustom See Power DIssipation and Junction Temperature 66.5 61.3 110.3  deg C/W
```

### Page 7

#### Extracted tables

Table 1:

```text
| PARAMETER | TESTCONDITIONS(1 | ) | MIN | TYP | MAX | UNIT
POWERSWITCH |  |  |  |  |  |  | 
RDS(on) Input-outputresistance |  | 0.5-Aratedoutput,25 deg C | DBV | 97 110 |  |  | mOhm
 |  | 0.5-Aratedoutput, -40 deg C<=(TJ,TA)<=85 deg C | DBV | 96 130 |  |  | mOhm
 |  | 1-Aratedoutput,25 deg C | DBV | 96 110 |  |  | mOhm
 |  |  | DGN | 86 100 |  |  | 
 |  | 1-Aratedoutput, -40 deg C<=(TJ,TA)<=85 deg C | DBV | 96 130 |  |  | mOhm
 |  |  | DGN | 86 120 |  |  | 
 |  | 1.5-Aratedoutput,25 deg C | DBV | 76 91 |  |  | mOhm
 |  |  | DGN | 69 84 |  |  | mOhm
 |  | 1.5-Aratedoutput, -40 deg C<=(TJ,TA)<=85 deg C | DBV | 76 106 |  |  | mOhm
 |  |  | DGN | 69 98 |  |  | mOhm
 |  | 2-Aratedoutput,25 deg C | DGN,DGK | 72 84 |  |  | mOhm
 |  | 2-Aratedoutput,-40 deg C<=(TJ,TA)<= 85 deg C | DGN,DGK | 72 98 |  |  | mOhm
CURRENTLIMIT |  |  |  |  |  |  | 
Currentlimit, IOS (2) SeeFigure6 |  | 0.5-Aratedoutput | TPS20xxC | 0.67 0.85 1.01 |  |  | A
 |  | 1-Aratedoutput | TPS20xxC | 1.3 1.55 1.8 |  |  | 
 |  |  | TPS20xxC-2 | 1.18 1.53 1.88 |  |  | 
 |  | 1.5-Aratedoutput | TPS20xxC | 1.7 2.15 2.5 |  |  | 
 |  |  | TPS20xxC-2 | 1.71 2.23 2.75 |  |  | 
 |  | 2-Aratedoutput | TPS20xxC | 2.35 2.9 3.4 |  |  | 
SUPPLYCURRENT |  |  |  |  |  |  | 
ISD Supplycurrent,switchdisabled |  | IOUT=0A |  | 0.01 1 |  |  | uA
 |  | 40 deg C<=(TJ,TA)<=85 deg C,VIN=5.5V,IOUT=0A |  | 2 |  |  | 
ISE Supplycurrent,switchenabled |  | IOUT=0A |  | 60 70 |  |  | uA
 |  | 40 deg C<=(TJ,TA)<=85 deg C,VIN=5.5V,IOUT=0A |  | 85 |  |  | 
Ilkg Leakagecurrent |  | VOUT=0V,VIN=5V,disabled, measureIVIN | TPS20xxC-2 | 0.05 1 |  |  | uA
 |  | 40 deg C<=(TJ,TA)<=85 deg C,VOUT=0V, VIN=5V,disabled,measureIVIN |  | 2 |  |  | 
IREV Reverseleakagecurrent |  | VOUT=5V,VIN=0V,measureIVOUT |  | 0.1 1 |  |  | uA
 |  | 40 deg C<=(TJ,TA)<=85 deg C,VOUT=5V,VIN=0V,measure IVOUT |  | 5 |  |  | 
OUTPUTDISCHARGE |  |  |  |  |  |  | 
RPD Outputpulldownresistance(3) |  | VIN=VOUT=5V,disabled | TPS20xxC | 400 470 600 |  |  | Ohm
```

#### Raw extracted text

```text
7
TPS2000C, TPS2001C, TPS2041C, TPS2051C, TPS2061C
TPS2065C, TPS2065C-2, TPS2068C, TPS2069C, TPS2069C-2
www.ti.com SLVSAU6H - JUNE 2011 - REVISED APRIL 2016
Product Folder Links: TPS2000C TPS2001C TPS2041C TPS2051C TPS2061C TPS2065C TPS2065C-2 TPS2068C
TPS2069C TPS2069C-2
Submit Documentation FeedbackCopyright  2011-2016, Texas Instruments Incorporated
(1) Pulsed testing techniques maintain junction temperature approximately equal to ambient temperature
(2) See Current Limit section for explanation of this parameter.
(3) These parameters are provided for reference only, and do not constitute part of TI's published device specifications for purposes of TI's
product warranty.
7.6 Electrical Characteristics: TJ = TA = 25 deg C
Unless otherwise noted: VIN = 5 V, VEN = VIN or VEN = GND, IOUT = 0 A. See Device Comparison Table for the rated current of
each part number. Parametrics over a wider operational range are shown in Electrical Characteristics: -40 deg C <= TJ <= 125 deg C (1).
PARAMETER TEST CONDITIONS (1) MIN TYP MAX UNIT
POWER SWITCH
RDS(on) Input - output resistance
0.5-A rated output, 25 deg C DBV 97 110 mOhm
0.5-A rated output,
-40 deg C <= (TJ , TA) <= 85 deg C DBV 96 130 mOhm
1-A rated output, 25 deg C
DBV 96 110
mOhm
DGN 86 100
1-A rated output,
-40 deg C <= (TJ , TA) <= 85 deg C
DBV 96 130
mOhm
DGN 86 120
1.5-A rated output, 25 deg C
DBV 76 91 mOhm
DGN 69 84 mOhm
1.5-A rated output,
-40 deg C <= (TJ , TA) <= 85 deg C
DBV 76 106 mOhm
DGN 69 98 mOhm
2-A rated output, 25 deg C DGN, DGK 72 84 mOhm
2-A rated output, -40 deg C <= (TJ , TA) <=
85 deg C DGN, DGK 72 98 mOhm
CURRENT LIMIT
IOS
(2) Current limit,
See Figure 6
0.5-A rated output TPS20xxC 0.67 0.85 1.01
A
1-A rated output
TPS20xxC 1.3 1.55 1.8
TPS20xxC-2 1.18 1.53 1.88
1.5-A rated output
TPS20xxC 1.7 2.15 2.5
TPS20xxC-2 1.71 2.23 2.75
2-A rated output TPS20xxC 2.35 2.9 3.4
SUPPLY CURRENT
ISD Supply current, switch disabled
IOUT = 0 A 0.01 1
uA
-40 deg C <= (TJ , TA) <= 85 deg C, VIN = 5.5 V, IOUT = 0 A 2
ISE Supply current, switch enabled
IOUT = 0 A 60 70
uA
-40 deg C <= (TJ , TA) <= 85 deg C, VIN = 5.5 V, IOUT = 0 A 85
Ilkg Leakage current
VOUT = 0 V, VIN = 5 V, disabled,
measure IVIN
TPS20xxC-2
0.05 1
uA
-40 deg C <= (TJ , TA) <= 85 deg C, VOUT = 0 V,
VIN = 5 V, disabled, measure IVIN
2
IREV Reverse leakage current
VOUT = 5 V, VIN = 0 V, measure IVOUT 0.1 1
uA-40 deg C <= (TJ , TA) <= 85 deg C, VOUT = 5 V, VIN = 0 V, measure
IVOUT
5
OUTPUT DISCHARGE
RPD Output pulldown resistance (3) VIN = VOUT = 5 V, disabled TPS20xxC 400 470 600 Ohm
```

### Page 8

#### Extracted tables

Table 1:

```text
| PARAMETER | TESTCONDITIONS(1) |  | MIN | TYP | MAX | UNIT
POWERSWITCH |  |  |  |  |  |  | 
RDS(ON) Input-outputresistance |  | 0.5-Aratedoutput | DBV | 97 154 |  |  | mOhm
 |  | 1-Aratedoutput | DBV | 96 154 |  |  | mOhm
 |  |  | DGN | 86 140 |  |  | 
 |  | 1.5-Aratedoutput | DBV | 76 121 |  |  | mOhm
 |  |  | DGN | 69 112 |  |  | mOhm
 |  | 2-Aratedoutput | DGN,DGK | 72 112 |  |  | mOhm
ENABLEINPUT(ENorEN) |  |  |  |  |  |  | 
Threshold |  | Inputrising |  | 1 1.45 2 |  |  | V
Hysteresis |  |  |  | 0.07 0.13 0.2 |  |  | V
Leakagecurrent |  | (VENorVEN)=0Vor5.5V |  | 1 0 1 |  |  | uA
CURRENTLIMIT |  |  |  |  |  |  | 
Currentlimit, IOS (2) SeeFigure23 |  | 0.5-Aratedoutput | TPS20xxC | 0.65 0.85 1.05 |  |  | A
 |  | 1-Aratedoutput | TPS20xxC | 1.2 1.55 1.9 |  |  | 
 |  |  | TPS20xxC-2 | 1.1 1.53 1.96 |  |  | 
 |  | 1.5-Aratedoutput | TPS20xxC | 1.6 2.15 2.7 |  |  | 
 |  |  | TPS20xxC-2 | 1.6 2.23 2.86 |  |  | 
 |  | 2-Aratedoutput | TPS20xxC | 2.3 2.9 3.6 |  |  | 
tIOS Short-circuitresponsetime(3) |  | VIN=5V(seeFigure6), One-halffullload->RSHORT=50mOhm, Measurefromapplicationtowhencurrentfallsbelow120%of finalvalue |  | 2 |  |  | us
SUPPLYCURRENT |  |  |  |  |  |  | 
ISD Supplycurrent,switchdisabled |  | IOUT=0A |  | 0.01 10 |  |  | uA
ISE Supplycurrent,switchenabled |  | IOUT=0A |  | 65 90 |  |  | uA
Ilkg Leakagecurrent |  | VOUT=0V,VIN=5V,disabled, measureIVIN | TPS20XXC-2 | 0.05 |  |  | uA
IREV Reverseleakagecurrent |  | VOUT=5.5V,VIN=0V,measureIVOUT |  | 0.2 20 |  |  | uA
UNDERVOLTAGELOCKOUT |  |  |  |  |  |  | 
VUVLO Risingthreshold |  | VIN |  | 3.5 3.75 4 |  |  | V
Hysteresis(3) |  | VIN |  | 0.14 |  |  | V
FLT |  |  |  |  |  |  | 
Outputlowvoltage,FLT |  | IFLT=1mA |  | 0.2 |  |  | V
OFF-stateleakage |  | VFLT=5.5V |  | 1 |  |  | uA
tFLT FLTdeglitch |  | FLTassertionordeassertiondeglitch |  | 6 9 12 |  |  | ms
OUTPUTDISCHARGE |  |  |  |  |  |  | 
RPD Outputpulldownresistance |  | VIN=4V,VOUT=5V,disabled | TPS20XXC | 350 560 1200 |  |  | Ohm
 |  | VIN=5V,VOUT=5V,disabled | TPS20XXC | 300 470 800 |  |  | 
THERMALSHUTDOWN |  |  |  |  |  |  | 
Risingthreshold(TJ) |  | Incurrentlimit |  | 135 |  |  | deg C
 |  | Notincurrentlimit |  | 155 |  |  | 
Hysteresis(3) |  |  |  | 20 |  |  |
```

#### Raw extracted text

```text
8
TPS2000C, TPS2001C, TPS2041C, TPS2051C, TPS2061C
TPS2065C, TPS2065C-2, TPS2068C, TPS2069C, TPS2069C-2
SLVSAU6H - JUNE 2011 - REVISED APRIL 2016 www.ti.com
Product Folder Links: TPS2000C TPS2001C TPS2041C TPS2051C TPS2061C TPS2065C TPS2065C-2 TPS2068C
TPS2069C TPS2069C-2
Submit Documentation Feedback Copyright  2011-2016, Texas Instruments Incorporated
(1) Pulsed testing techniques maintain junction temperature approximately equal to ambient temperature
(2) See Current Limit for explanation of this parameter.
(3) These parameters are provided for reference only, and do not constitute part of TI's published device specifications for purposes of TI's
product warranty.
7.7 Electrical Characteristics: -40 deg C <= TJ <= 125 deg C
Unless otherwise noted:4.5 V <= VIN <= 5.5 V, VEN = VIN or VEN = GND, IOUT = 0 A, typical values are at 5 V and 25 deg C. See
Device Comparison Table for the rated current of each part number.
PARAMETER TEST CONDITIONS (1) MIN TYP MAX UNIT
POWER SWITCH
RDS(ON) Input - output resistance
0.5-A rated output DBV 97 154 mOhm
1-A rated output
DBV 96 154
mOhm
DGN 86 140
1.5-A rated output
DBV 76 121 mOhm
DGN 69 112 mOhm
2-A rated output DGN, DGK 72 112 mOhm
ENABLE INPUT (EN or EN)
Threshold Input rising 1 1.45 2 V
Hysteresis 0.07 0.13 0.2 V
Leakage current (VEN or VEN) = 0 V or 5.5 V -1 0 1 uA
CURRENT LIMIT
IOS
(2) Current limit,
See Figure 23
0.5-A rated output TPS20xxC 0.65 0.85 1.05
A
1-A rated output
TPS20xxC 1.2 1.55 1.9
TPS20xxC-2 1.1 1.53 1.96
1.5-A rated output
TPS20xxC 1.6 2.15 2.7
TPS20xxC-2 1.6 2.23 2.86
2-A rated output TPS20xxC 2.3 2.9 3.6
tIOS Short-circuit response time (3)
VIN = 5 V (see Figure 6),
One-half full load -> RSHORT = 50 mOhm,
Measure from application to when current falls below 120% of
final value
2 us
SUPPLY CURRENT
ISD Supply current, switch disabled IOUT = 0 A 0.01 10 uA
ISE Supply current, switch enabled IOUT = 0 A 65 90 uA
Ilkg Leakage current VOUT = 0 V, VIN = 5 V, disabled,
measure IVIN
TPS20XXC-2 0.05 uA
IREV Reverse leakage current VOUT = 5.5 V, VIN = 0 V, measure IVOUT 0.2 20 uA
UNDERVOLTAGE LOCKOUT
VUVLO Rising threshold VIN 3.5 3.75 4 V
Hysteresis (3) VIN 0.14 V
FLT
Output low voltage, FLT IFLT = 1 mA 0.2 V
OFF-state leakage VFLT = 5.5 V 1 uA
tFLT FLT deglitch FLT assertion or deassertion deglitch 6 9 12 ms
OUTPUT DISCHARGE
RPD Output pulldown resistance
VIN = 4 V, VOUT = 5 V, disabled TPS20XXC 350 560 1200
Ohm
VIN = 5 V, VOUT = 5 V, disabled TPS20XXC 300 470 800
THERMAL SHUTDOWN
Rising threshold (TJ)
In current limit 135
 deg CNot in current limit 155
Hysteresis (3) 20
```

### Page 9

#### Extracted tables

Table 1:

```text
|  |  |  | MIN | NOM | MAX | UNIT
ENABLEINPUT(ENorEN) |  |  |  |  |  |  | 
t Turnontime ON |  | V =5V,C =1uF,R =100Ohm,ENorEN IN L L . SeeFigure1,Figure3,andFigure4 | 0.5-Aand1-ARated | 1 1.4 1.8 |  |  | ms
 |  |  | 1.5-Aand2-ARated | 1.2 1.7 2.2 |  |  | 
t Turnofftime OFF |  | V =5V,C =1uF,R =100Ohm,ENorEN IN L L . SeeFigure1,Figure3,andFigure4 | 0.5-Aand1-ARated | 1.3 1.65 2 |  |  | ms
 |  |  | 1.5-Aand2-ARated | 1.7 2.1 2.5 |  |  | 
t Risetime,output R |  | C =1uF,R =100Ohm,V =5V.See L L IN Figure2 | 0.5-Aand1-ARated | 0.4 0.55 0.7 |  |  | ms
 |  |  | 1.5-Aand2-ARated | 0.5 0.7 1 |  |  | 
t Falltime,output F |  | C =1uF,R =100Ohm,V =5V.See L L IN Figure2 | 0.5-Aand1-ARated | 0.25 0.35 0.45 |  |  | ms
 |  |  | 1.-5Aand2-ARated | 0.3 0.43 0.55 |  |  |
```

#### Raw extracted text

```text
IOUT 120% x IOS
IOS
tIOS
0 A
V/EN
VOUT
tON
tOFF
50%
90%
10%
50%
VEN
VOUT
50%
tON
tOFF
50%
90%
10%
tR tF
10%
90%
VOUT
OUT
RL CL
9
TPS2000C, TPS2001C, TPS2041C, TPS2051C, TPS2061C
TPS2065C, TPS2065C-2, TPS2068C, TPS2069C, TPS2069C-2
www.ti.com SLVSAU6H - JUNE 2011 - REVISED APRIL 2016
Product Folder Links: TPS2000C TPS2001C TPS2041C TPS2051C TPS2061C TPS2065C TPS2065C-2 TPS2068C
TPS2069C TPS2069C-2
Submit Documentation FeedbackCopyright  2011-2016, Texas Instruments Incorporated
7.8 Timing Requirements: TJ = TA = 25 deg C
MIN NOM MAX UNIT
ENABLE INPUT (EN or EN)
tON Turnon time
VIN = 5 V, CL = 1 uF, RL = 100 Ohm, EN  or EN
.
See Figure 1, Figure 3, and Figure 4
0.5-A and 1-A Rated 1 1.4 1.8
ms
1.5-A and 2-A Rated 1.2 1.7 2.2
tOFF Turnoff time
VIN = 5 V, CL = 1 uF, RL = 100 Ohm, EN  or EN
.
See Figure 1, Figure 3, and Figure 4
0.5-A and 1-A Rated 1.3 1.65 2
ms
1.5-A and 2-A Rated 1.7 2.1 2.5
tR Rise time, output CL = 1 uF, RL = 100 Ohm, VIN = 5 V. See
Figure 2
0.5-A and 1-A Rated 0.4 0.55 0.7
ms
1.5-A and 2-A Rated 0.5 0.7 1
tF Fall time, output CL = 1 uF, RL = 100 Ohm, VIN = 5 V. See
Figure 2
0.5-A and 1-A Rated 0.25 0.35 0.45
ms
1.-5A and 2-A Rated 0.3 0.43 0.55
Figure 1. Output Rise and Fall Test Load
Figure 2. Power-On and Power-Off Timing
Figure 3. Enable Timing, Active High Enable
Figure 4. Enable Timing, Active Low Enable
Figure 5. Output Short-Circuit Parameters
```

### Page 10

#### Raw extracted text

```text
VOUT
IOUT
IOS
Decreasing
Load
Resistance
VIN
0 A
0 V
Slope = -R DS(ON)
10
TPS2000C, TPS2001C, TPS2041C, TPS2051C, TPS2061C
TPS2065C, TPS2065C-2, TPS2068C, TPS2069C, TPS2069C-2
SLVSAU6H - JUNE 2011 - REVISED APRIL 2016 www.ti.com
Product Folder Links: TPS2000C TPS2001C TPS2041C TPS2051C TPS2061C TPS2065C TPS2065C-2 TPS2068C
TPS2069C TPS2069C-2
Submit Documentation Feedback Copyright  2011-2016, Texas Instruments Incorporated
Figure 6. Output Characteristic Showing Current Limit
```

### Page 11

#### Extracted tables

Table 1:

```text
9.3 All Versions, 5 V 9.2 9.1 )sm( TLFt 9.0 8.9 8.8 -40 -20 0 20 40 60 80 100 120 140 Junction Temperature ( deg C) G019 Figure7.DeglitchPeriod(T vsTemperature FLT) | 14 VIN = 5 V 85 deg C 12 25 deg C 10 )Am( 8 -40 deg C gniknis 6 TUOI 4 125 deg C 2 0 0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0 4.5 5.0 5.5 Output Voltage (V) G020 Figure8.OutputDischargeCurrentvsOutputVoltage
3.5 2-A Rated VIN = 5 V 3.0 2.5 1.5-A Rated )A( 2.0 1-A Rated SOI 1.5 0.5-A Rated 1.0 0.5 -40 -20 0 20 40 60 80 100 120 140 Junction Temperature ( deg C) G021 Figure9.ShortCircuitCurrent(I )vsTemperature OS | 7 All Unit Types, 5 V 6 5 4 )Au( 3 VERI 2 1 0 -1 -40 -20 0 20 40 60 80 100 120 140 Junction Temperature ( deg C) G022 Figure10.ReverseLeakageCurrent(I )vsTemperature REV
1.0 Input Voltage = 5.5 V 0.8 0.6 )Au( 0.4 DSI 0.2 0.0 -0.2 -40 -20 0 20 40 60 80 100 120 140 Junction Temperature ( deg C) G023 Figure11.DisabledSupplyCurrent(I )vsTemperature SD | 1.0 All Unit Types 0.8 0.6 125 deg C )Au( 0.4 DSI 85 deg C 0.2 0.0 -40 deg C and 25 deg C -0.2 4.00 4.25 4.50 4.75 5.00 5.25 5.50 Input Voltage (V) G024 Figure12.DisabledSupplyCurrent(I )vsInputVoltage SD
```

Table 2:

```text
All V | ersions | , 5 V |  |  |  |  |  |
```

Table 3:

```text
VIN | = 5 V |  |  |  |  |  | deg C |  |  |  | 
 |  |  |  |  |  | 85 | deg C |  |  |  | 
 |  |  |  |  | C |  |  |  |  |  | 
 |  |  |  | 25 deg | C |  |  |  |  |  | 
 |  | 40 deg | C |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  | 12 | 5 deg C |  |
```

Table 4:

```text
|  |  |  |  | 2-A | Rated |  |  | VIN | = 5 V
 |  |  | 1.5-A |  | Rated |  |  |  |  | 
 |  | 1-A | Rated |  |  |  |  |  |  | 
 | 0.5-A | Rated |  |  |  |  |  |  |  |
```

Table 5:

```text
All U | nit Typ | es, 5 V |  |  |  |  |  |
```

Table 6:

```text
Input | Voltag | e = 5. | 5 V |  |  |  |  |
```

Table 7:

```text
All Unit T | ypes |  |  |  |  |  | 
 | 1 | 1 | 25 deg C |  |  |  | 
 | 8 |  | 5 deg C |  |  |  | 
 |  | 8 | 5 deg C |  |  |  | 
 | 40 deg C |  | and 25 deg C |  |  |  |
```

#### Raw extracted text

```text
-0.2
0.0
0.2
0.4
0.6
0.8
1.0
-40 -20 0 20 40 60 80 100 120 140
Junction Temperature ( deg C)
ISD (uA)
Input Voltage = 5.5 V
G023
-0.2
0.0
0.2
0.4
0.6
0.8
1.0
4.00 4.25 4.50 4.75 5.00 5.25 5.50
-40 deg C and 25 deg C
85 deg C
125 deg C
Input Voltage (V)
ISD (uA)
All Unit Types
G024
0.5
1.0
1.5
2.0
2.5
3.0
3.5
-40 -20 0 20 40 60 80 100 120 140
0.5-A Rated
1-A Rated
1.5-A Rated
2-A Rated
Junction Temperature ( deg C)
IOS (A)
VIN = 5 V
G021
-1
0
1
2
3
4
5
6
7
-40 -20 0 20 40 60 80 100 120 140
Junction Temperature ( deg C)
IREV (uA)
All Unit Types, 5 V
G022
8.8
8.9
9.0
9.1
9.2
9.3
-40 -20 0 20 40 60 80 100 120 140
Junction Temperature ( deg C)
tFLT (ms)
All Versions, 5 V
G019
0
2
4
6
8
10
12
14
0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0 4.5 5.0 5.5
-40 deg C
25 deg C
85 deg C
125 deg C
Output Voltage (V)
IOUT sinking (mA)
VIN = 5 V
G020
11
TPS2000C, TPS2001C, TPS2041C, TPS2051C, TPS2061C
TPS2065C, TPS2065C-2, TPS2068C, TPS2069C, TPS2069C-2
www.ti.com SLVSAU6H - JUNE 2011 - REVISED APRIL 2016
Product Folder Links: TPS2000C TPS2001C TPS2041C TPS2051C TPS2061C TPS2065C TPS2065C-2 TPS2068C
TPS2069C TPS2069C-2
Submit Documentation FeedbackCopyright  2011-2016, Texas Instruments Incorporated
7.9 Typical Characteristics
Figure 7. Deglitch Period (TFLT) vs Temperature Figure 8. Output Discharge Current vs Output Voltage
Figure 9. Short Circuit Current (IOS) vs Temperature Figure 10. Reverse Leakage Current (IREV) vs Temperature
Figure 11. Disabled Supply Current (ISD) vs Temperature Figure 12. Disabled Supply Current (ISD) vs Input Voltage
```

### Page 12

#### Extracted tables

Table 1:

```text
6.0 5.5 All unit types, VIN = 0 V 5.0 4.5 125 deg C 4.0 3.5 )Au( 3.0 2.5 VERI 2.0 1.5 85 deg C 25 deg C -40 deg C 1.0 0.5 0.0 -0.5 4.00 4.25 4.50 4.75 5.00 5.25 5.50 Output Voltage (V) G025 Figure13.ReverseLeakageCurrent(I )vsOutputVoltage REV | 80 All Unit Types, VIN = 5.5 V 75 70 )Au( 65 ESI 60 55 50 -40 -20 0 20 40 60 80 100 120 140 Junction Temperature ( deg C) G026 Figure14.EnabledSupplyCurrent(I )vsTemperature SE
80 75 125 deg C 85 deg C 70 65 )Au( 60 ESI 55 50 25 deg C 45 -40 deg C 40 4.00 4.25 4.50 4.75 5.00 5.25 5.50 Input Voltage (V) G027 Figure15.EnabledSupplyCurrent(I )vsInputVoltage SE | 0.475 COUT = 1 uF, RLOAD = 100 W 0.450 0.425 )sm( 0.400 1.5-A and 2-A Rated, VIN = 4.5 V ft 1.5-A and 2-A Rated, VIN = 5 V 0.375 1.5-A and 2-A Rated, VIN = 5.5 V 0.350 0.5-A and 1-A Rated, VIN = 5 V 0.325 -40 -20 0 20 40 60 80 100 120 140 Junction Temperature ( deg C) G028 Figure16.OutputFallTime(T )vsTemperature F
0.85 COUT = 1 uF, RLOAD = 100 W 0.80 1.5 A, 2 A, 5.5 V 0.75 0.70 )sm( 0.65 rt 0.5 A, 1 A, 5 V 0.60 1.5 A, 2 A, 5 V 1.5 A, 2 A, 4.5 V 0.55 0.50 -40 -20 0 20 40 60 80 100 120 140 Junction Temperature ( deg C) G029 Figure17.OutputRiseTime(T )vsTemperature R | 140 VIN = 5 V 130 120 0.5-A, 1-A Rated 110 100 ) Wm( 90 NOSDR 80 70 1.5-A, 2-A Rated 60 50 40 -40 -20 0 20 40 60 80 100 120 140 Junction Temperature ( deg C) G030 Figure18.Input-OutputResistance(R )vsTemperature DS(ON)
```

Table 2:

```text
All unit t |  | ypes, V |  |  |  | = 0 V |  |  |  |  |  |  |  |  | 
 |  | IN |  |  |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  | 1 | 25 deg C |  |  |  |  |  |  |  |  | 
 |  | 85 deg C |  |  |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  | 2 | 5 deg C |  |  | 40 deg C |  |  |
```

Table 3:

```text
All U | nit Typ | es, VIN | = 5.5 | V |  |  |  |  |
```

Table 4:

```text
| 85 deg | C |  | 12 | 5 deg C |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  | 25 deg C | 
 |  |  |  |  |  |  |  |  |  | 25 deg C | 
 |  |  |  |  | 40 | 40 | deg C |  |  |  |
```

Table 5:

```text
|  |  |  |  |  |  | CO | CO | UT = 1 | uF, R | LOAD = 1 | 00 W
 |  |  |  | 1 |  |  | 1.5-A |  | and 2 | A Rate | d, VIN = | 4.5
 |  |  |  |  | 1 |  |  |  |  |  |  | 
 |  |  |  |  |  |  | .5-A an |  | d 2-A | Rated, | VIN = 5 | V
 |  |  |  | 1.5 |  |  |  |  |  |  |  | V
 |  |  |  |  |  |  | A and |  | 2-A Ra | ted, VI | N = 5.5 | 
 |  | 0 |  |  |  |  |  |  |  |  | 5 V | 
 |  |  | 0 | .5-A an |  |  | d 1-A |  | Rated, | VIN = | 5 V |
```

Table 6:

```text
COUT |  | = 1 u |  | F, RLO | AD = 1 | 00 W |  |  |  |  |  | 5.5 V | 
 |  |  |  |  |  |  |  | 1.5 A |  | , 2 A, |  | 5.5 V | 
 |  |  |  |  | V |  |  |  |  |  |  |  | 
 |  | 0.5 A, |  | 1 A, 5 | V |  |  |  |  |  |  |  | 
 |  |  |  |  |  | 1.5 A, 2 |  | A, 5 |  | V |  |  | 
 |  |  |  |  |  |  |  |  |  | 1.5 A |  | , 2 A, | 4.5 V
```

Table 7:

```text
VIN = | 5 V |  |  |  |  |  |  |  |  |  |  | 
 | 0.5 |  | A, 1-A |  | Rated |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  | 1 | .5-A, 2 |  | A Rat | ed
```

#### Raw extracted text

```text
0.50
0.55
0.60
0.65
0.70
0.75
0.80
0.85
-40 -20 0 20 40 60 80 100 120 140
0.5 A, 1 A, 5 V 1.5 A, 2 A, 5 V
1.5 A, 2 A, 4.5 V
1.5 A, 2 A, 5.5 V
Junction Temperature ( deg C)
tr (ms)
COUT = 1 uF,  RLOAD = 100 Ohm
G029
40
50
60
70
80
90
100
110
120
130
140
-40 -20 0 20 40 60 80 100 120 140
0.5-A, 1-A Rated
1.5-A, 2-A Rated
Junction Temperature ( deg C)
RDSON (mOhm )
VIN = 5 V
G030
40
45
50
55
60
65
70
75
80
4.00 4.25 4.50 4.75 5.00 5.25 5.50
-40 deg C
25 deg C
85 deg C 125 deg C
Input Voltage (V)
ISE (uA)
G027
0.325
0.350
0.375
0.400
0.425
0.450
0.475
-40 -20 0 20 40 60 80 100 120 140
0.5-A and 1-A Rated, VIN = 5 V
1.5-A and 2-A Rated, VIN = 5 V
1.5-A and 2-A Rated, VIN = 4.5 V
1.5-A and 2-A Rated, VIN = 5.5 V
Junction Temperature ( deg C)
tf (ms)
COUT = 1 uF,  RLOAD = 100 Ohm
G028
-0.5
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
4.0
4.5
5.0
5.5
6.0
4.00 4.25 4.50 4.75 5.00 5.25 5.50
-40 deg C25 deg C85 deg C
125 deg C
Output Voltage (V)
IREV (uA)
All unit types, VIN = 0 V
G025
50
55
60
65
70
75
80
-40 -20 0 20 40 60 80 100 120 140
Junction Temperature ( deg C)
ISE (uA)
All Unit Types, VIN = 5.5 V
G026
12
TPS2000C, TPS2001C, TPS2041C, TPS2051C, TPS2061C
TPS2065C, TPS2065C-2, TPS2068C, TPS2069C, TPS2069C-2
SLVSAU6H - JUNE 2011 - REVISED APRIL 2016 www.ti.com
Product Folder Links: TPS2000C TPS2001C TPS2041C TPS2051C TPS2061C TPS2065C TPS2065C-2 TPS2068C
TPS2069C TPS2069C-2
Submit Documentation Feedback Copyright  2011-2016, Texas Instruments Incorporated
Typical Characteristics (continued)
Figure 13. Reverse Leakage Current (IREV) vs Output Voltage Figure 14. Enabled Supply Current (ISE) vs Temperature
Figure 15. Enabled Supply Current (ISE) vs Input Voltage Figure 16. Output Fall Time (TF) vs Temperature
Figure 17. Output Rise Time (TR) vs Temperature Figure 18. Input-Output Resistance (RDS(ON)) vs Temperature
```

### Page 13

#### Extracted tables

Table 1:

```text
| V | = 5 V, C = |  |  | 730 uF, TP | S2065C, I | = 1.68 A
 | IN | IN |  |  |  | E | ND
 |  |  |  | IOS |  |  |
```

#### Raw extracted text

```text
1
10
100
0 5 10 15 20 25
IOS
IPK (Shorted) (A)
Recovery Time (us)
VIN = 5 V,  CIN = 730 uF,  TPS2065C,  IEND = 1.68 A
G031
13
TPS2000C, TPS2001C, TPS2041C, TPS2051C, TPS2061C
TPS2065C, TPS2065C-2, TPS2068C, TPS2069C, TPS2069C-2
www.ti.com SLVSAU6H - JUNE 2011 - REVISED APRIL 2016
Product Folder Links: TPS2000C TPS2001C TPS2041C TPS2051C TPS2061C TPS2065C TPS2065C-2 TPS2068C
TPS2069C TPS2069C-2
Submit Documentation FeedbackCopyright  2011-2016, Texas Instruments Incorporated
Typical Characteristics (continued)
Figure 19. Recovery vs Current Peak
```

### Page 14

#### Raw extracted text

```text
Charge
Pump
Driver
UVLO
Current
Limit
Thermal
Sense
9-ms
Deglitch
IN
GND
OUT
FLT
Current
Sense
OTSD
CS
EN or
EN
Copyright  2016, Texas Instruments Incorporated
Charge
Pump
Driver
UVLO
Current
Limit
Thermal
Sense
9-ms
Deglitch
IN
GND
OUT
FLT
Current
Sense
(Disabled+
UVLO)
OTSD
CS
EN or
EN
Copyright  2016, Texas Instruments Incorporated
14
TPS2000C, TPS2001C, TPS2041C, TPS2051C, TPS2061C
TPS2065C, TPS2065C-2, TPS2068C, TPS2069C, TPS2069C-2
SLVSAU6H - JUNE 2011 - REVISED APRIL 2016 www.ti.com
Product Folder Links: TPS2000C TPS2001C TPS2041C TPS2051C TPS2061C TPS2065C TPS2065C-2 TPS2068C
TPS2069C TPS2069C-2
Submit Documentation Feedback Copyright  2011-2016, Texas Instruments Incorporated
8 Detailed Description
8.1 Overview
The TPS20xxC and TPS20xxC-2 are current-limited, power-distribution switches providing a range from 0.5 A
and 2 A of continuous load current in 5-V circuits. These parts use N-channel MOSFETs for low resistance,
maintaining voltage regulation to the load. They are designed for applications where short circuits or heavy
capacitive loads are encountered. Device features include enable, reverse blocking when disabled, output
discharge pulldown, overcurrent protection, overtemperature protection, and deglitched fault reporting.
8.2 Functional Block Diagram
Figure 20. TPS20xxC Block Diagram
Figure 21. TPS20xxC-2 Block Diagram
8.3 Feature Description
8.3.1 Undervoltage Lockout
The undervoltage lockout (UVLO) circuit disables the power switch until the input voltage reaches the UVLO
turnon threshold. Built-in hysteresis prevents unwanted ON/OFF cycling due to input voltage drop from large
current surges. FLT is high impedance when the TPS20xxC and TPS20xxC-2 are in UVLO.
```

### Page 15

#### Raw extracted text

```text
15
TPS2000C, TPS2001C, TPS2041C, TPS2051C, TPS2061C
TPS2065C, TPS2065C-2, TPS2068C, TPS2069C, TPS2069C-2
www.ti.com SLVSAU6H - JUNE 2011 - REVISED APRIL 2016
Product Folder Links: TPS2000C TPS2001C TPS2041C TPS2051C TPS2061C TPS2065C TPS2065C-2 TPS2068C
TPS2069C TPS2069C-2
Submit Documentation FeedbackCopyright  2011-2016, Texas Instruments Incorporated
Feature Description (continued)
8.3.2 Enable
The logic enable input (EN, or EN), controls the power switch, bias for the charge pump, driver, and other
circuits. The supply current is reduced to less than 1 uA when the TPS20xxC and TPS20xxC-2 are disabled.
Disabling the TPS20xxC and TPS20xxC-2 immediately clears an active FLT indication. The enable input is
compatible with both TTL and CMOS logic levels.
The turnon and turnoff times (tON, tOFF) are composed of a delay and a rise or fall time (tR, tF). The delay times
are internally controlled. The rise time is controlled by both the TPS20xxC and TPS20xxC-2 and the external
loading (especially capacitance). TPS20xxC fall time is controlled by the loading (R and C), and the output
discharge (RPD). TPS20xxC-2 does not have the output discharge (RPD), fall time is controlled by the loading (R
and C). An output load consisting of only a resistor experiences a fall time set by the TPS20xxC and TPS20xxC-
2. An output load with parallel R and C elements experiences a fall time determined by the (R x C) time constant
if it is longer than the tF TPS20xxC and TPS20xxC-2.
The enable must not be left open, and may be tied to VIN or GND depending on the device.
8.3.3 Internal Charge Pump
The device incorporates an internal charge pump and gate drive circuitry necessary to drive the N-channel
MOSFET. The charge pump supplies power to the gate driver circuit and provides the necessary voltage to pull
the gate of the MOSFET above the source. The driver incorporates circuitry that controls the rise and fall times of
the output voltage to limit large current and voltage surges on the input supply, and provides built-in soft-start
functionality. The MOSFET power switch blocks current from OUT to IN when turned off by the UVLO or
disabled.
8.3.4 Current Limit
The TPS20xxC and TPS20xxC-2 responds to overloads by limiting output current to the static IOS levels shown in
Electrical Characteristics: TJ = TA = 25 deg C. When an overload condition is present, the device maintains a
constant output current, with the output voltage determined by (IOS x RLOAD). Two possible overload conditions
can occur. The first overload condition occurs when either:
1. input voltage is first applied, enable is true, and a short circuit is present (load which draws IOUT > IOS)
2. input voltage is present and the TPS20xxC and TPS20xxC-2 are enabled into a short circuit.
The output voltage is held near zero potential with respect to ground and the TPS20xxC and TPS20xxC-2 ramps
the output current to IOS. The TPS20xxC and TPS20xxC-2 limits the current to IOS until the overload condition is
removed or the device begins to thermal cycle. This is demonstrated in Figure 26 where the device was enabled
into a short, and subsequently cycles current OFF and ON as the thermal protection engages.
The second condition is when an overload occurs while the device is enabled and fully turned on. The device
responds to the overload condition within tIOS (Figure 5 and Figure 6) when the specified overload (see Electrical
Characteristics: -40 deg C <= TJ <= 125 deg C) is applied. The response speed and shape varies with the overload level,
input circuit, and rate of application. The current limit response will vary between simply settling to IOS, or turnoff
and controlled return to IOS. Similar to the previous case, the TPS20xxC and TPS20xxC-2 limits the current to IOS
until the overload condition is removed or the device begins to thermal cycle. This is demonstrated by Figure 27,
Figure 28, and Figure 29.
The TPS20xxC and TPS20xxC-2 thermal cycles if an overload condition is present long enough to activate
thermal limiting in any of the above cases. This is due to the relatively large power dissipation [(VIN - VOUT) x IOS]
driving the junction temperature up. The device turns off when the junction temperature exceeds 135 deg C
(minimum) while in current limit. The device remains off until the junction temperature cools 20 deg C and then
restarts.
There are two kinds of current limit profiles typically available in TI switch products that are similar to the
TPS20xxC and TPS20xxC-2. Many older designs have an output I vs V characteristic similar to the plot labeled
Current Limit with Peaking in Figure 22. This type of limiting can be characterized by two parameters, the current
limit corner (IOC), and the short circuit current (IOS). IOC is often specified as a maximum value. The TPS20xxC
and TPS20xxC-2 family of parts does not present noticeable peaking in the current limit, corresponding to the
characteristic labeled Flat Current Limit in Figure 22. This is why the IOC parameter is not present in Electrical
Characteristics: -40 deg C <= TJ <= 125 deg C.
```

### Page 16

#### Raw extracted text

```text
V
OUT
IOUT
IOS
Decreasing
Load
Resistance
VIN
0 A
0 V
Slope = -RDS(ON)
V
OUT
IOUT IOS
Decreasing
Load
Resistance
VIN
0 A
0 V
Slope = -RDS(ON)
IOC
Current Limit
with Peaking
Flat Current
Limit
16
TPS2000C, TPS2001C, TPS2041C, TPS2051C, TPS2061C
TPS2065C, TPS2065C-2, TPS2068C, TPS2069C, TPS2069C-2
SLVSAU6H - JUNE 2011 - REVISED APRIL 2016 www.ti.com
Product Folder Links: TPS2000C TPS2001C TPS2041C TPS2051C TPS2061C TPS2065C TPS2065C-2 TPS2068C
TPS2069C TPS2069C-2
Submit Documentation Feedback Copyright  2011-2016, Texas Instruments Incorporated
Feature Description (continued)
Figure 22. Current Limit Profiles
8.3.5 FLT
The FLT open-drain output is asserted (active low) during an overload or overtemperature condition. A 9-ms
deglitch on both the rising and falling edges avoids false reporting at start-up and during transients. A current
limit condition shorter than the deglitch period clears the internal timer upon termination. The deglitch timer does
not integrate multiple short overloads and declare a fault. This is also true for exiting from a faulted state. An
input voltage with excessive ripple and large output capacitance may interfere with operation of FLT around IOS
as the ripple drives the TPS20xxC and TPS20xxC-2 in and out of current limit.
If the TPS20xxC and TPS20xxC-2 are in current limit and the overtemperature circuit goes active, FLT goes true
immediately (see Figure 27); however, the exiting this condition is deglitched (see Figure 29). FLT is tripped just
as the knee of the constant-current limiting is entered. Disabling the TPS20xxC and TPS20xxC-2 clears an active
FLT as soon as the switch turns off (see Figure 26). FLT is high impedance when the TPS20xxC and TPS20xxC-
2 are disabled or in undervoltage lockout (UVLO).
8.3.6 Output Discharge
A 470-Ohm (typical) output discharge dissipates stored charge and leakage current on OUT when the TPS20xxC is
in UVLO or disabled. The pulldown circuit loses bias gradually as VIN decreases, causing a rise in the discharge
resistance as VIN falls towards 0 V. The TPS20xxC-2 does not have this function. The output is be controlled by
an external loadings when the device is in ULVO or disabled.
8.4 Device Functional Modes
There are no other functional modes.
```

### Page 17

#### Extracted tables

Table 1:

```text
6/7 | /8
```

#### Raw extracted text

```text
IN
GND
FAULT
Control
Signal
4.5 V-6.5 V 0.1PF
COUT
Fault
Signal
Power
Pad
VOUT
EN
OUT
RFAULT
TPS2065CDGN
4
1/2
5
6/7/8
1
Copyright  2016, Texas Instruments Incorporated
17
TPS2000C, TPS2001C, TPS2041C, TPS2051C, TPS2061C
TPS2065C, TPS2065C-2, TPS2068C, TPS2069C, TPS2069C-2
www.ti.com SLVSAU6H - JUNE 2011 - REVISED APRIL 2016
Product Folder Links: TPS2000C TPS2001C TPS2041C TPS2051C TPS2061C TPS2065C TPS2065C-2 TPS2068C
TPS2069C TPS2069C-2
Submit Documentation FeedbackCopyright  2011-2016, Texas Instruments Incorporated
9 Application and Implementation
NOTE
Information in the following applications sections is not part of the TI component
specification, and TI does not warrant its accuracy or completeness. TIs customers are
responsible for determining suitability of components for their purposes. Customers should
validate and test their design implementation to confirm system functionality.
9.1 Application Information
The TPS20xxC and TPS20xxC-2 current-limited power switch uses N-channel MOSFETs in applications
requiring continuous load current. The device enters constant-current mode when the load exceeds the current
limit threshold.
9.2 Typical Application
Figure 23. Typical Application Schematic
9.2.1 Design Requirements
For this design example, use the following input parameters:
1. The TPS2065CDGN operates from a 5-V to +/-0.5-V input rail.
2. What is the normal operation current, for example, the maximum allowable current drawn by portable
equipment for USB 3.0 port is 900 mA, so the normal operation current is 900 mA, and the minimum current
limit of power switch must exceed 900 mA to avoid false trigger during normal operation. For the TPS2065C
device, target 1-A continuous output current application.
3. What is the maximum allowable current provided by up-stream power, the maximum current limit of power
switch that must lower it to ensure power switch can protect the up-stream power when overload is
encountered at the output of power switch. For the TPS2065C device, the maximum IOS is 1.8 A.
9.2.2 Detailed Design Procedure
To begin the design process a few parameters must be decided upon. The designer must know the following:
1. Normal input operation voltage
2. Output continuous current
3. Maximum up-stream power supply output current
9.2.2.1 Input and Output Capacitance
Input and output capacitance improves the performance of the device; the actual capacitance must be optimized
for the particular application. For all applications, TI recommends placing a 0.1-uF or greater ceramic bypass
capacitor between IN and GND, as close to the device as possible for local noise decoupling.
```

### Page 18

#### Extracted tables

Table 1:

```text
9 2.00 VIN = 5 V, COUT = 150 uF, RLOAD = 5 W , TPS2065C 8 1.75 7 1.50 Output Current 6 FLT 1.25 )V( 5 1.00 )A( edutilpmA 4 0.75 tnerruC 3 0.50 2 EN 0.25 1 0.00 Output Voltage 0 -0.25 -1 -0.50 -2m 0 2m 4m 6m 8m 10m 12m 14m 16m 18m 20m Time (s) G001 Figure24.TPS2065COutputRise/Fall5Ohm | 9 2.00 VIN = 5 V, COUT = 150 uF, RLOAD = 100 W , TPS2065C 8 1.75 Output Current 7 1.50 6 Output Voltage FLT 1.25 )V( 5 1.00 )A( edutilpmA 4 0.75 tnerruC 3 EN 0.50 2 0.25 1 0.00 0 -0.25 -1 -0.50 -2m 0 2m 4m 6m 8m 10m 12m 14m 16m 18m 20m Time (s) G002 Figure25.TPS2065COutputRise/Fall100Ohm
```

Table 2:

```text
VIN | = 5 V | , COU |  | T = 15 |  | 0 uF |  | , RLO |  | AD = 5 | W , T | PS2 | 065C | 
 |  | Ou |  | tput C |  | urren |  | t |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  |  | FL | T | 
 |  |  |  |  | EN |  |  |  |  |  |  |  |  | 
 |  |  |  | Outpu |  | t Vol |  | tage |  |  |  |  |  |
```

Table 3:

```text
VIN | = 5 V | , CO |  | UT = 1 |  | 50 uF | , RLO | AD = 1 | 00 W | , TPS |  | 206 | 5C | 
 | Outpu | t Cur |  | rent |  |  |  |  |  |  |  |  |  | 
 |  |  |  | Outpu |  | t Volt | age |  |  | F | F | LT |  | 
 |  |  |  | EN |  |  |  |  |  |  |  |  |  |
```

#### Raw extracted text

```text
-2m 0 2m 4m 6m 8m 10m 12m 14m 16m 18m 20m
-1
0
1
2
3
4
5
6
7
8
9
Output Voltage
FLT
EN
-0.50
-0.25
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00
Time (s)
Amplitude (V)
Current (A)
Output Current
VIN = 5 V,  COUT = 150 uF,  RLOAD = 5 Ohm ,  TPS2065C
G001
-2m 0 2m 4m 6m 8m 10m 12m 14m 16m 18m 20m
-1
0
1
2
3
4
5
6
7
8
9
Output Voltage FLT
EN
-0.50
-0.25
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00
Time (s)
Amplitude (V)
Current (A)
Output Current
VIN = 5 V,  COUT = 150 uF,  RLOAD = 100 Ohm ,  TPS2065C
G002
18
TPS2000C, TPS2001C, TPS2041C, TPS2051C, TPS2061C
TPS2065C, TPS2065C-2, TPS2068C, TPS2069C, TPS2069C-2
SLVSAU6H - JUNE 2011 - REVISED APRIL 2016 www.ti.com
Product Folder Links: TPS2000C TPS2001C TPS2041C TPS2051C TPS2061C TPS2065C TPS2065C-2 TPS2068C
TPS2069C TPS2069C-2
Submit Documentation Feedback Copyright  2011-2016, Texas Instruments Incorporated
Typical Application (continued)
All protection circuits such as the TPS20xxC and TPS20xxC-2 has the potential for input voltage overshoots and
output voltage undershoots.
Input voltage overshoots can be caused by either of two effects. The first cause is an abrupt application of input
voltage in conjunction with input power bus inductance and input capacitance when the IN terminal is high
impedance (before turnon). Theoretically, the peak voltage is 2x the applied. The second cause is due to the
abrupt reduction of output short-circuit current when the TPS20xxC and TPS20xxC-2 turns off and energy stored
in the input inductance drives the input voltage high. Input voltage droops may also occur with large load steps
and as the TPS20xxC and TPS20xxC-2 output is shorted. Applications with large input inductance (for example,
connecting the evaluation board to the bench power-supply through long cables) may require large input
capacitance reduce the voltage overshoot from exceeding the absolute maximum voltage of the device. The fast
current limit speed of the TPS20xxC and TPS20xxC-2 to hard output short circuits isolates the input bus from
faults. However, ceramic input capacitance in the range of 1 uF to 22 uF adjacent to the TPS20xxC and
TPS20xxC-2 input aids in both speeding the response time and limiting the transient seen on the input power
bus. Momentary input transients to 6.5 V are permitted.
Output voltage undershoot is caused by the inductance of the output power bus just after a short has occurred
and the TPS20xxC and TPS20xxC-2 has abruptly reduced OUT current. Energy stored in the inductance drives
the OUT voltage down and potentially negative as it discharges. Applications with large output inductance (such
as from a cable) benefit from use of a high-value output capacitor to control the voltage undershoot. When
implementing USB standard applications, a 120-uF minimum output capacitance is required. Typically a 150-uF
electrolytic capacitor is used, which is sufficient to control voltage undershoots. However, if the application does
not require 120 uF of capacitance, and there is potential to drive the output negative, then TI recommends a
minimum of 10-uF ceramic capacitance on the output. The voltage undershoot must be controlled to less than
1.5 V for 10 us.
9.2.3 Application Curves
Figure 24. TPS2065C Output Rise / Fall 5 Ohm Figure 25. TPS2065C Output Rise / Fall 100 Ohm
```

### Page 19

#### Extracted tables

Table 1:

```text
9 2.00 VIN = 5 V, COUT = 150 uF, RLOAD = 0 W , TPS2065C 8 1.75 7 1.50 6 1.25 FLT 5 1.00 )V( )A( Output Current edutilpmA 4 0.75 tnerruC 3 0.50 EN 2 0.25 Output Voltage 1 0.00 0 -0.25 -1 -0.50 -2m 0 2m 4m 6m 8m 10m 12m 14m 16m 18m Time (s) G003 Figure26.TPS2065CEnableintoOutputShort | 9 2.00 VIN = 5 V, COUT = 150 uF, RLOAD = 50 mW , TPS2065C 8 1.80 7 1.50 Output Current EN 6 1.20 )V( 5 1.00 )A( edutilpmA 4 FLT 0.75 tnerruC 3 0.50 2 0.25 1 0.00 0 -0.25 Output Voltage -1 -0.50 -2.5m 2.5m 7.5m 12.5m 17.5m 22.5m25m Time (s) G004 Figure27.TPS2065CPulsedShortApplied
10 26 9 24 VIN = 5 V, COUT = 0 uF, TPS2065C 8 22 Input Voltage 7 20 6 18 5 16 )V( )A( 4 14 egatloV tnerruC 3 12 Output Voltage 2 10 1 8 0 6 -1 4 Output Current -2 2 -3 0 -1u 0 1u 2u 3u 4u Time (s) G005 Figure28.TPS2065CShortApplied | 6 30 VIN = 5 V, COUT = 0 uF, RLOAD = 50 mW , TPS2065C 5 25 4 20 )V( )A( IOUT egatloV tnerruC 3 15 VOUT 2 10 tuptuO tuptuO 1 5 0 0 -1 -5 -1u 0 1u 2u 3u 4u Time (s) G006 Figure29.TPS2065CPulsed1.45-ALoad
```

Table 2:

```text
VIN | = 5 V, |  | COU | T = 150 | uF, R |  | LOAD |  | = 0 W , |  | TPS2 | 065C | 
 |  | O | utpu | t Curre | nt |  | FL |  | T |  |  |  | 
 |  |  |  |  |  | E | N |  |  |  |  |  | 
 |  | Ou | tpu | t Volta | ge |  |  |  |  |  |  |  |
```

Table 3:

```text
VIN | = 5 V, | COU | T = 15 | 0 uF, R | LOA | D = 5 | 0 mW , |  | TPS | 2065C |  | 
 |  |  |  |  |  | Outpu | t Curr |  | ent | EN |  | 
 |  |  |  |  |  |  |  |  | FLT |  |  | 
 | Outpu | t Vo | ltage |  |  |  |  |  |  |  |  |
```

Table 4:

```text
V = 5 V, | C = 0 u | F, TPS2065 |  | C |  |  |  |  | 
IN | OUT |  |  |  |  |  |  |  | 
 |  |  | I | nput Voltag |  |  | e |  | 
 |  |  |  | Output Volta |  |  | ge |  | 
 |  |  |  | Output Curre |  |  | nt |  |
```

Table 5:

```text
| VIN = | 5 V, COUT = | 0 uF, RLOA |  | D = 50 mW , | TPS2065C
 |  |  |  | IOUT |  | 
 |  |  |  | VO | UT | 
 |  |  |  |  | UT |
```

Table 6:

```text
6 2.5 VIN = 5 V, COUT = 0 uF, 5 2.0 RLOAD = 50 mW , TPS2065C 4 1.5 )V( )A( egatloV tnerruC 3 1.0 2 0.5 tuptuO tuptuO IOUT VOUT 1 0.0 0 -0.5 -1 -1.0 -100u 0 100u 200u 300u 400u 500u 600u Time (s) G007 Figure30.TPS2065C50-mOhmShortCircuit | 9 2.00 VIN = 5 V, COUT = 150 uF, RLOAD = 7.5W , TPS2065C 8 1.75 7 1.50 Output Voltage 6 1.25 )V( 5 1.00 )A( 4 EN, VIN 0.75 edutilpmA tnerruC 3 0.50 2 FLT 0.25 1 0.00 Output Current 0 -0.25 -1 -0.50 -5m -4m -3m -2m -1m 0 1m 2m 3m 4m 5m Time (s) G008 Figure31.TPS2065CPowerUp-Enabled
```

Table 7:

```text
|  |  |  |  | VIN R | = 5 V, C = 50 | OUT = 0 mW , TP |  | uF, S2065C
 |  |  |  | L | L | OAD |  |  | 
 |  | IOU |  | T |  |  |  |  | 
 |  |  | IOU | T |  |  |  |  | 
 |  |  |  |  |  |  | VOU |  | T
 |  |  |  |  |  |  |  | VOU | T
```

Table 8:

```text
VIN | = 5 V, | COUT | = 150 | uF, | RLOAD |  | = 7.5W |  | , TPS | 2065C |  | 
 |  |  | Out | put V | oltage |  |  |  |  |  |  | 
 |  | EN, | VIN |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  | FLT |  | 
 |  |  |  |  |  | O | utput |  | Curre |  |  | 
 |  |  |  |  |  |  |  |  |  | nt |  |
```

#### Raw extracted text

```text
-100u 0 100u 200u 300u 400u 500u 600u
-1
0
1
2
3
4
5
6
VOUT
-1.0
-0.5
0.0
0.5
1.0
1.5
2.0
2.5
Time (s)
Output Voltage (V)
Output Current (A)
IOUT
VIN = 5 V,  COUT = 0 uF,
RLOAD = 50 mOhm ,  TPS2065C
G007
-5m -4m -3m -2m -1m 0 1m 2m 3m 4m 5m
-1
0
1
2
3
4
5
6
7
8
9
Output Voltage
FLT
EN, VIN
-0.50
-0.25
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00
Time (s)
Amplitude (V)
Current (A)
Output Current
VIN = 5 V,  COUT = 150 uF,  RLOAD = 7.5Ohm , TPS2065C
G008
-1u 0 1u 2u 3u 4u
-3
-2
-1
0
1
2
3
4
5
6
7
8
9
10
Input Voltage
Output Voltage
0
2
4
6
8
10
12
14
16
18
20
22
24
26
Time (s)
Voltage (V)
Current (A)
Output Current
VIN = 5 V,  COUT = 0 uF,  TPS2065C
G005
VIN = 5 V,  COUT = 0 uF,  RLOAD = 50 mOhm ,  TPS2065C
-1u 0 1u 2u 3u 4u
-1
0
1
2
3
4
5
6
-5
0
5
10
15
20
25
30
Time (s)
Output Voltage (V)
Output Current (A)
IOUT
VOUT
G006
-2m 0 2m 4m 6m 8m 10m 12m 14m 16m 18m
-1
0
1
2
3
4
5
6
7
8
9
Output Voltage
FLT
EN
-0.50
-0.25
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00
Time (s)
Amplitude (V)
Current (A)
Output Current
VIN = 5 V,  COUT = 150 uF,  RLOAD = 0 Ohm ,  TPS2065C
G003
Output Voltage
-2.5m 2.5m 7.5m 12.5m 17.5m 22.5m25m
-1
0
1
2
3
4
5
6
7
8
9
FLT
EN
-0.50
-0.25
0.00
0.25
0.50
0.75
1.00
1.20
1.50
1.80
2.00
Time (s)
Amplitude (V)
Current (A)
Output Current
VIN = 5 V, COUT = 150 uF, RLOAD = 50 mOhm , TPS2065C
G004
19
TPS2000C, TPS2001C, TPS2041C, TPS2051C, TPS2061C
TPS2065C, TPS2065C-2, TPS2068C, TPS2069C, TPS2069C-2
www.ti.com SLVSAU6H - JUNE 2011 - REVISED APRIL 2016
Product Folder Links: TPS2000C TPS2001C TPS2041C TPS2051C TPS2061C TPS2065C TPS2065C-2 TPS2068C
TPS2069C TPS2069C-2
Submit Documentation FeedbackCopyright  2011-2016, Texas Instruments Incorporated
Typical Application (continued)
Figure 26. TPS2065C Enable into Output Short Figure 27. TPS2065C Pulsed Short Applied
Figure 28. TPS2065C Short Applied Figure 29. TPS2065C Pulsed 1.45-A Load
Figure 30. TPS2065C 50-mOhm Short Circuit Figure 31. TPS2065C Power Up - Enabled
```

### Page 20

#### Extracted tables

Table 1:

```text
9 2.00 VIN = 5 V, COUT = 150 uF, RLOAD = 7.5W , TPS2065C 8 1.75 7 1.50 6 1.25 )V( 5 1.00 )A( FLT edutilpmA 4 EN, VIN 0.75 tnerruC 3 0.50 2 0.25 Output Current 1 0.00 0 -0.25 Output Voltage -1 -0.50 -40m -30m -20m -10m 0 10m 20m 30m 40m Time (s) G009 Figure32.TPS2065CPowerDown-Enabled | 9 3.2 VIN = 5 V, COUT = 150 uF, RLOAD = 2.5 W , TPS2001C 2.8 7 2.4 Output Current FLT 2.0 )V( 5 1.6 )A( edutilpmA 1.2 tnerruC 3 0.8 EN 0.4 1 0.0 Output Voltage -0.4 -1 -0.8 -2m 0 2m 4m 6m 8m 10m 12m 14m 16m 18m Time (s) G010 Figure33.TPS2001CTurnoninto2.5Ohm
9 3.6 VIN = 5 V, COUT = 150 uF, RLOAD = 50 mW , TPS2001C 8 3.2 7 2.8 Output Current 6 2.4 EN FLT 5 2.0 )V( )A( edutilpmA 4 1.6 tnerruC 3 1.2 2 0.8 Output Voltage 1 0.4 0 0.0 -1 -0.4 -2m 0 2m 4m 6m 8m 10m 12m 14m 16m 18m Time (s) G011 Figure34.TPS2001CEnableintoShort | 9 3.6 VIN = 5 V, COUT = 150 uF, RLOAD = 50mW , TPS2001C 8 3.2 7 2.8 Output Current 6 EN 2.4 )V( 5 2.0 )A( edutilpmA 4 1.6 tnerruC 3 Output Voltage 1.2 2 0.8 1 FLT 0.4 0 0.0 -1 -0.4 -2.5m 0 2.5m 5m 7.5m 10m12.5m15m17.5m20m22.5m Time (s) G012 Figure35.TPS2001CPulsedOutputShort
```

Table 2:

```text
VIN = |  | 5 V, CO |  | UT = 15 | 0 uF, R | LOAD = |  |  | 7.5W , T |  | PS206 | 5C | 
 |  |  |  |  |  |  |  | F | LT |  | EN, V |  | 
 |  |  |  |  |  |  |  |  |  |  | I | N | 
 |  | Output C |  | urrent |  |  |  |  |  |  |  |  | 
 |  |  | O | utput | Voltage |  |  |  |  |  |  |  |
```

Table 3:

```text
VIN | = 5 V, | COUT |  |  | = 150 |  | uF, R | LOAD = |  | 2.5 W | , TP | S200 | 1C | 
 |  |  | O |  | utput |  | Curren | t |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  |  | FLT |  | 
 |  |  |  |  |  |  |  | EN |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  | EN |  |  |  |  | 
 |  |  |  |  | Output |  | Volta | ge |  |  |  |  |  |
```

Table 4:

```text
VIN = | 5 V, | COUT | = 150 | uF, R | LOAD |  | = 50 m |  | W , | TPS200 | 1C | 
 |  |  |  |  |  |  |  |  | O | utput Cu | rrent | 
EN |  |  |  |  |  |  |  |  |  | FLT |  | 
 |  |  |  |  |  |  |  |  | O | utput Vo | ltage |
```

Table 5:

```text
VIN | = 5 V, | COUT | = 150 | uF, R | LOAD = | 50mW | , TPS | 2001 |  | C | 
 |  |  |  |  |  | Ou | tput | Curre |  | nt | 
 |  |  |  |  |  | EN |  |  |  |  | 
 |  |  |  |  |  | Outp | ut Vo | ltage |  |  | 
 |  |  |  |  |  |  | FL |  |  |  | 
 |  |  |  |  |  |  |  | T |  |  |
```

Table 6:

```text
9 1.4 VIN = 5 V, COUT = 150 uF, RLOAD = 10 W , TPS2051C 8 1.2 Output Current 7 1.0 Output Voltage 6 0.8 )V( 5 FLT 0.6 )A( edutilpmA 4 0.4 tnerruC 3 0.2 2 0.0 1 EN -0.2 0 -0.4 -1 -0.6 -2m 0 2m 4m 6m 8m 10m 12m 14m 16m 18m Time (s) G013 Figure36.TPS2051CTurnoninto10Ohm | 9 1.6 VIN = 5 V, COUT = 150 uF, RLOAD = 50 mW , TPS2051C 8 1.4 7 1.2 Output Current 6 1.0 )V( 5 0.8 )A( edutilpmA 4 0.6 tnerruC 3 0.4 EN 2 0.2 Output Voltage 1 FLT 0.0 0 -0.2 -1 -0.4 -2m 0 2m 4m 6m 8m 10m 12m 14m 16m 18m Time (s) G014 Figure37.TPS2051CEnableintoShort
```

Table 7:

```text
|  |  | VIN = |  | 5 V, C | OUT = |  | 150 u |  | F, RLO |  | AD = 1 | 0 W | , TPS2 |  | 051C
 | Ou |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
 |  |  | tput |  | Curren | t |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  | O | utput |  | Voltag | e |  |  | 
 |  |  |  |  |  |  |  |  |  |  |  |  |  | FLT |  | 
 |  |  |  |  |  |  | E | N |  |  |  |  |  |  |  |
```

Table 8:

```text
| VI | N = 5 |  | V, CO |  |  | UT = 15 |  | 0 uF, | RLOAD |  | = 50 | mW , |  | TPS2 | 051C
 |  |  |  |  |  |  | Outpu |  | t Curr | en | t |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  |  | EN |  |  |  | 
 |  |  | Ou | tput V |  |  | oltage |  |  |  |  | F | LT |  |  |
```

#### Raw extracted text

```text
-2m 0 2m 4m 6m 8m 10m 12m 14m 16m 18m
-1
0
1
2
3
4
5
6
7
8
9
Output Voltage
FLT
EN
-0.6
-0.4
-0.2
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
Time (s)
Amplitude (V)
Current (A)
Output Current
VIN = 5 V,  COUT = 150 uF,  RLOAD = 10 Ohm ,  TPS2051C
G013
-2m 0 2m 4m 6m 8m 10m 12m 14m 16m 18m
-1
0
1
2
3
4
5
6
7
8
9
Output Voltage
FLT
EN
-0.4
-0.2
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6
Time (s)
Amplitude (V)
Current (A)
Output Current
VIN = 5 V,  COUT = 150 uF,  RLOAD = 50 mOhm ,  TPS2051C
G014
-2m 0 2m 4m 6m 8m 10m 12m 14m 16m 18m
-1
0
1
2
3
4
5
6
7
8
9
FLTEN
VIN = 5 V,  COUT = 150 uF,  RLOAD = 50 mOhm ,  TPS2001C
-0.4
0.0
0.4
0.8
1.2
1.6
2.0
2.4
2.8
3.2
3.6
Time (s)
Amplitude (V)
Current (A)
Output Current
Output Voltage
G011
Output Voltage
-2.5m 0 2.5m 5m 7.5m 10m 12.5m 15m 17.5m 20m 22.5m
-1
0
1
2
3
4
5
6
7
8
9
FLT
EN
VIN = 5 V,  COUT = 150 uF, RLOAD = 50mOhm , TPS2001C
-0.4
0.0
0.4
0.8
1.2
1.6
2.0
2.4
2.8
3.2
3.6
Time (s)
Amplitude (V)
Current (A)
Output Current
G012
-40m -30m -20m -10m 0 10m 20m 30m 40m
-1
0
1
2
3
4
5
6
7
8
9
Output Voltage
FLT
EN, VIN
-0.50
-0.25
0.00
0.25
0.50
0.75
1.00
1.25
1.50
1.75
2.00
Time (s)
Amplitude (V)
Current (A)
Output Current
VIN = 5 V,  COUT = 150 uF,  RLOAD = 7.5Ohm ,  TPS2065C
G009
-2m 0 2m 4m 6m 8m 10m 12m 14m 16m 18m
-1
1
3
5
7
9
Output Voltage
FLT
EN
-0.8
-0.4
0.0
0.4
0.8
1.2
1.6
2.0
2.4
2.8
3.2
Time (s)
Amplitude (V)
Current (A)
Output Current
VIN = 5 V,  COUT = 150 uF,  RLOAD = 2.5 Ohm ,  TPS2001C
G010
20
TPS2000C, TPS2001C, TPS2041C, TPS2051C, TPS2061C
TPS2065C, TPS2065C-2, TPS2068C, TPS2069C, TPS2069C-2
SLVSAU6H - JUNE 2011 - REVISED APRIL 2016 www.ti.com
Product Folder Links: TPS2000C TPS2001C TPS2041C TPS2051C TPS2061C TPS2065C TPS2065C-2 TPS2068C
TPS2069C TPS2069C-2
Submit Documentation Feedback Copyright  2011-2016, Texas Instruments Incorporated
Typical Application (continued)
Figure 32. TPS2065C Power Down - Enabled Figure 33. TPS2001C Turnon into 2.5 Ohm
Figure 34. TPS2001C Enable into Short Figure 35. TPS2001C Pulsed Output Short
Figure 36. TPS2051C Turnon into 10 Ohm Figure 37. TPS2051C Enable into Short
```

### Page 21

#### Extracted tables

Table 1:

```text
9 1.4 VIN = 5 V, COUT = 150 uF, RLOAD = 50mW , TPS2051C 8 1.2 7 1.0 Output Current 6 0.8 )V( 5 0.6 )A( edutilpmA 4 EN 0.4 tnerruC 3 0.2 2 FLT 0.0 1 Output Voltage -0.2 0 -0.4 -1 -0.6 -2.5m 0 2.5m 5m 7.5m 10m12.5m15m17.5m20m22.5m Time (s) G015 Figure38.TPS2051CPulsedOutputShort | 12 2.5 VIN = 5 V, COUT = 150 uF, RLOAD = 3.3 W , TPS2069C 10 2.0 8 1.5 )V( EN )A( 6 1.0 edutilpmA Output Current tnerruC 4 0.5 2 0.0 FLT Output Voltage 0 -0.5 -2 -1.0 -4m -2m 0 2m 4m 6m 8m 10m 12m 14m 16m Time (s) G016 Figure39.TPS2069CTurnoninto3.3Ohm
10 3.0 VIN = 5 V, COUT = 150 uF, RLOAD = 50 mW , TPS2069C 8 2.5 EN Output Current 6 2.0 )V( )A( 4 1.5 edutilpmA tnerruC 2 1.0 FLT 0 0.5 -2 0.0 Output Voltage -4 -0.5 -2m 0 2m 4m 6m 8m 10m 12m 14m 16m 18m Time (s) G017 Figure40.TPS2069CEnableintoShort | 10 3.0 VIN = 5 V, COUT = 150 uF, RLOAD = 50 mW , TPS2069C 8 2.5 EN 6 2.0 )V( )A( 4 1.5 edutilpmA tnerruC 2 1.0 Output Current 0 0.5 -2 0.0 Output Voltage FLT -4 -0.5 -12.5m -7.5m -2.5m 2.5m 7.5m 12.5m Time (s) G018 Figure41.TPS2069CPulsedOutputShort
```

Table 2:

```text
| VIN = 5 |  | V, C | OUT = |  | 150 uF |  | , RLO | AD = 5 |  | 0mW , | TPS2 | 051C | 
 |  |  |  |  |  |  |  |  |  | Ou | tput C | urrent |  | 
 |  |  |  | EN |  |  |  |  |  |  |  |  |  | 
 |  |  | F | LT |  |  |  |  |  |  |  |  |  | 
 |  | Out | put | Voltag |  | e |  |  |  |  |  |  |  |
```

Table 3:

```text
| V | IN = 5 | V, CO | UT = | 150 uF, |  | RLOA | D = 3 |  | .3 W , | TPS2 | 069C
E |  | N |  |  |  |  |  |  |  |  |  | 
 | E | N |  |  |  |  |  |  |  |  |  | 
 |  |  |  | Ou | tput Cu |  | rrent |  |  |  |  | 
 |  |  | Ou | tput V | oltage |  | FL | T |  |  |  |
```

Table 4:

```text
V | IN = 5 V, |  | CO | UT = 1 | 50 uF, |  | RLOA | D = 50 | mW , | TPS2 | 069C
EN |  |  |  |  |  |  |  |  |  | Ou Cu | tput rrent
 |  |  |  |  |  |  |  |  |  | FL | T
 |  | Out | put | Voltag | e |  |  |  |  |  |
```

Table 5:

```text
VIN | = 5 V, | COUT | = 150 | uF, RL | OAD = | 50 m |  | W , TP |  | S206 | 9C | 
 |  |  |  |  |  | EN |  |  |  |  |  | 
 |  |  |  |  | Out | put C |  | urrent |  |  |  | 
Out | put Vo | ltage |  |  |  | FL |  | T |  |  |  |
```

#### Raw extracted text

```text
-2m 0 2m 4m 6m 8m 10m 12m 14m 16m 18m
-4
-2
0
2
4
6
8
10
Output Voltage
FLT
EN
-0.5
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Time (s)
Amplitude (V)
Current (A)
Output
Current
VIN = 5 V,  COUT = 150 uF,  RLOAD = 50 mOhm ,  TPS2069C
G017
-12.5m -7.5m -2.5m 2.5m 7.5m 12.5m
-4
-2
0
2
4
6
8
10
Output Voltage FLT
EN
-0.5
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Time (s)
Amplitude (V)
Current (A)Output Current
VIN = 5 V,  COUT = 150 uF,  RLOAD = 50 mOhm , TPS2069C
G018
-2.5m 0 2.5m 5m 7.5m 10m 12.5m 15m 17.5m 20m 22.5m
-1
0
1
2
3
4
5
6
7
8
9
Output Voltage
FLT
EN
-0.6
-0.4
-0.2
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
Time (s)
Amplitude (V)
Current (A)
Output Current
VIN = 5 V,  COUT = 150 uF,  RLOAD = 50mOhm , TPS2051C
G015
-4m -2m 0 2m 4m 6m 8m 10m 12m 14m 16m
-2
0
2
4
6
8
10
12
Output Voltage
FLT
EN
-1.0
-0.5
0.0
0.5
1.0
1.5
2.0
2.5
Time (s)
Amplitude (V)
Current (A)
Output Current
VIN = 5 V,  COUT = 150 uF,  RLOAD = 3.3 Ohm ,  TPS2069C
G016
21
TPS2000C, TPS2001C, TPS2041C, TPS2051C, TPS2061C
TPS2065C, TPS2065C-2, TPS2068C, TPS2069C, TPS2069C-2
www.ti.com SLVSAU6H - JUNE 2011 - REVISED APRIL 2016
Product Folder Links: TPS2000C TPS2001C TPS2041C TPS2051C TPS2061C TPS2065C TPS2065C-2 TPS2068C
TPS2069C TPS2069C-2
Submit Documentation FeedbackCopyright  2011-2016, Texas Instruments Incorporated
Typical Application (continued)
Figure 38. TPS2051C Pulsed Output Short Figure 39. TPS2069C Turnon into 3.3 Ohm
Figure 40. TPS2069C Enable into Short Figure 41. TPS2069C Pulsed Output Short
10 Power Supply Recommendations
Design of the devices is for operation from an input voltage supply range of 4.5 V to 5.5 V. The current capability
of the power supply should exceed the maximum current limit of the power switch.
```

### Page 22

#### Extracted tables

Table 1:

```text
|  |  |  | 1 |  | 8 7 6 5
 |  |  |  | 1 |  | 
 |  |  |  | 2 3 4 |  | 
 |  |  |  | 2 |  | 
 |  |  |  | 3 |  | 
 |  |  |  | 4 |  |
```

Table 2:

```text
8 | 
7 | 
6 |
```

Table 3:

```text
5 |
```

#### Raw extracted text

```text
1
2
6
7
8
3
Via to Bottom Layer Signal Ground Plane
4 5
Via to Bottom Layer Signal
22
TPS2000C, TPS2001C, TPS2041C, TPS2051C, TPS2061C
TPS2065C, TPS2065C-2, TPS2068C, TPS2069C, TPS2069C-2
SLVSAU6H - JUNE 2011 - REVISED APRIL 2016 www.ti.com
Product Folder Links: TPS2000C TPS2001C TPS2041C TPS2051C TPS2061C TPS2065C TPS2065C-2 TPS2068C
TPS2069C TPS2069C-2
Submit Documentation Feedback Copyright  2011-2016, Texas Instruments Incorporated
11 Layout
11.1 Layout Guidelines
1. Place the 100-nF bypass capacitor near the IN and GND pins, and make the connections using a low
inductance trace.
2. Place at least 10-uF low ESR ceramic capacitor near the OUT and GND pins, and make the connections
using a low inductance trace.
3. The PowerPAD must be directly connected to PCB ground plane using wide and short copper trace.
11.2 Layout Example
Figure 42. Recommended Layout
11.3 Power Dissipation and Junction Temperature
It is good design practice to estimate power dissipation and maximum expected junction temperature of the
TPS20xxC and TPS20xxC-2. The system designer can control choices of package, proximity to other power
dissipating devices, and printed-circuit board (PCB) design based on these calculations. These have a direct
influence on maximum junction temperature. Other factors, such as airflow and maximum ambient temperature,
are often determined by system considerations. It is important to remember that these calculations do not include
the effects of adjacent heat sources, and enhanced or restricted air flow.
Addition of extra PCB copper area around these devices is recommended to reduce the thermal impedance and
maintain the junction temperature as low as practical. The lower junction temperatures achieved by soldering the
pad improve the efficiency and reliability of both TPS20xxC and TPS20xxC-2 parts and the system. The following
examples were used to determine the JACustom thermal impedances noted in Thermal Information: SOT-23
and Thermal Information: MSOP-PowerPAD. They were based on use of the JEDEC high-k circuit board
construction (2 signal and 2 plane) with 4, 1-oz. copper weight, layers.
While TI recommends that the DGN package PAD be soldered to circuit board copper fill and vias for low thermal
impedance, there may be cases where this is not desired. For example, use of routing area under the IC. Some
devices are available in packages without the PowerPad (DGK) specifically for this purpose. The JA for the DGN
package with the pad not soldered and no extra copper, is approximately 141 deg C/W for 0.5-A and 1-A rated parts,
and 139 deg C/W for the 1.5-A and 2-A rated parts. The JA for the DGK mounted per Figure 45 is 110.3 deg C/W. These
values may be used in Equation 1 to determine the maximum junction temperature.
```

### Page 23

#### Raw extracted text

```text
0.100 x 0.060
& 3 18 mil vias to
inner plane 2
10 mil trace
0.100 x 0.175
& 5 18 mil vias
0.185 x 0.045
& 3 18 mil vias
0.07 x 0.08
0.08 x 0.250
0.15 x 0.15
10 mil trace
50 mil trace
CIN
VIN: 0.0145in 2 area
& 2 x 0.018in vias
GND: 0.056in 2 total area
& 3 x 0.018in vias COUT
VOUT: 0.048in 2 total area
5 x 0.01in vias
0.050in trace
COUT
VIN: 0.00925in2
& 3 x 0.018in vias
VOUT: 0.041in 2 total
0.050in trace
4 x 0.01in vias
CIN
GND: 0.052in2 Total
& 3 x 0.018in vias
23
TPS2000C, TPS2001C, TPS2041C, TPS2051C, TPS2061C
TPS2065C, TPS2065C-2, TPS2068C, TPS2069C, TPS2069C-2
www.ti.com SLVSAU6H - JUNE 2011 - REVISED APRIL 2016
Product Folder Links: TPS2000C TPS2001C TPS2041C TPS2051C TPS2061C TPS2065C TPS2065C-2 TPS2068C
TPS2069C TPS2069C-2
Submit Documentation FeedbackCopyright  2011-2016, Texas Instruments Incorporated
Power Dissipation and Junction Temperature (continued)
Figure 43. DBV Package PCB Layout Example
Figure 44. DGN Package PCB Layout Example
Figure 45. DGK Package PCB Layout Example
As shown in Equation 1, the following procedure requires iteration because power loss is due to the internal
MOSFET I2 x RDS(ON), and RDS(ON) is a function of the junction temperature. As an initial estimate, use the
RDS(ON) at 125 deg C from the Typical Characteristics, and the preferred package thermal resistance for the preferred
board construction from the Thermal Information: SOT-23 table.
```

### Page 24

#### Raw extracted text

```text
24
TPS2000C, TPS2001C, TPS2041C, TPS2051C, TPS2061C
TPS2065C, TPS2065C-2, TPS2068C, TPS2069C, TPS2069C-2
SLVSAU6H - JUNE 2011 - REVISED APRIL 2016 www.ti.com
Product Folder Links: TPS2000C TPS2001C TPS2041C TPS2051C TPS2061C TPS2065C TPS2065C-2 TPS2068C
TPS2069C TPS2069C-2
Submit Documentation Feedback Copyright  2011-2016, Texas Instruments Incorporated
Power Dissipation and Junction Temperature (continued)
TJ = TA + ((IOUT
2 x RDS(ON)) x JA)
where
* IOUT = rated OUT pin current (A)
* RDS(ON) = Power switch ON-resistance at an assumed TJ (Ohm)
* TA = Maximum ambient temperature ( deg C)
* TJ = Maximum junction temperature ( deg C)
* JA = Thermal resistance ( deg C/W) (1)
If the calculated TJ is substantially different from the original assumption, estimate a new value of RDS(ON) using
the typical characteristic plot and recalculate.
If the resulting TJ is not less than 125 deg C, try a PCB construction or a package with lower JA.
```

### Page 25

#### Extracted tables

Table 1:

```text
PARTS | PRODUCTFOLDER | SAMPLE&BUY | TECHNICAL DOCUMENTS | TOOLS& SOFTWARE | SUPPORT& COMMUNITY
TPS2000C | Clickhere | Clickhere | Clickhere | Clickhere | Clickhere
TPS2001C | Clickhere | Clickhere | Clickhere | Clickhere | Clickhere
TPS2041C | Clickhere | Clickhere | Clickhere | Clickhere | Clickhere
TPS2051C | Clickhere | Clickhere | Clickhere | Clickhere | Clickhere
TPS2061C | Clickhere | Clickhere | Clickhere | Clickhere | Clickhere
TPS2065C | Clickhere | Clickhere | Clickhere | Clickhere | Clickhere
TPS2065C-2 | Clickhere | Clickhere | Clickhere | Clickhere | Clickhere
TPS2068C | Clickhere | Clickhere | Clickhere | Clickhere | Clickhere
TPS2069C | Clickhere | Clickhere | Clickhere | Clickhere | Clickhere
TPS2069C-2 | Clickhere | Clickhere | Clickhere | Clickhere | Clickhere
```

#### Raw extracted text

```text
25
TPS2000C, TPS2001C, TPS2041C, TPS2051C, TPS2061C
TPS2065C, TPS2065C-2, TPS2068C, TPS2069C, TPS2069C-2
www.ti.com SLVSAU6H - JUNE 2011 - REVISED APRIL 2016
Product Folder Links: TPS2000C TPS2001C TPS2041C TPS2051C TPS2061C TPS2065C TPS2065C-2 TPS2068C
TPS2069C TPS2069C-2
Submit Documentation FeedbackCopyright  2011-2016, Texas Instruments Incorporated
12 Device and Documentation Support
12.1 Related Links
The table below lists quick access links. Categories include technical documents, support and community
resources, tools and software, and quick access to sample or buy.
Table 1. Related Links
PARTS PRODUCT FOLDER SAMPLE & BUY TECHNICAL
DOCUMENTS
TOOLS &
SOFTWARE
SUPPORT &
COMMUNITY
TPS2000C Click here Click here Click here Click here Click here
TPS2001C Click here Click here Click here Click here Click here
TPS2041C Click here Click here Click here Click here Click here
TPS2051C Click here Click here Click here Click here Click here
TPS2061C Click here Click here Click here Click here Click here
TPS2065C Click here Click here Click here Click here Click here
TPS2065C-2 Click here Click here Click here Click here Click here
TPS2068C Click here Click here Click here Click here Click here
TPS2069C Click here Click here Click here Click here Click here
TPS2069C-2 Click here Click here Click here Click here Click here
12.2 Community Resources
The following links connect to TI community resources. Linked contents are provided "AS IS" by the respective
contributors. They do not constitute TI specifications and do not necessarily reflect TI's views; see TI's Terms of
Use.
TI E2E(TM) Online Community TI's Engineer-to-Engineer (E2E) Community. Created to foster collaboration
among engineers. At e2e.ti.com, you can ask questions, share knowledge, explore ideas and help
solve problems with fellow engineers.
Design Support TI's Design Support Quickly find helpful E2E forums along with design support tools and
contact information for technical support.
12.3 Trademarks
PowerPAD, E2E are trademarks of Texas Instruments.
All other trademarks are the property of their respective owners.
12.4 Electrostatic Discharge Caution
These devices have limited built-in ESD protection. The leads should be shorted together or the device placed in conductive foam
during storage or handling to prevent electrostatic damage to the MOS gates.
12.5 Glossary
SLYZ022 - TI Glossary.
This glossary lists and explains terms, acronyms, and definitions.
13 Mechanical, Packaging, and Orderable Information
The following pages include mechanical, packaging, and orderable information. This information is the most
current data available for the designated devices. This data is subject to change without notice and revision of
this document. For browser-based versions of this data sheet, refer to the left-hand navigation.
```

### Page 26

#### Extracted tables

Table 1:

```text
Orderable part number | Status (1) | Material type (2) | Package | Pins | Package qty | Carrier | RoHS (3) | Lead finish/ Ball material (4) | MSL rating/ Peak reflow (5) | Op temp ( deg C) | Part marking (6)
905X0205100 | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 85 | VBYQ
TPS2000CDGK | Active | Production | VSSOP (DGK) | 8 | 80 | TUBE | Yes | NIPDAUAG | SN | Level-2-260C-1 YEAR | 40 to 125 | PXFI
TPS2000CDGK.B | Active | Production | VSSOP (DGK) | 8 | 80 | TUBE | Yes | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | PXFI
TPS2000CDGKR | Active | Production | VSSOP (DGK) | 8 | 2500 | LARGE T&R | Yes | NIPDAU | SN | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | PXFI
TPS2000CDGKR.B | Active | Production | VSSOP (DGK) | 8 | 2500 | LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | PXFI
TPS2000CDGN | Active | Production | HVSSOP (DGN) | 8 | 80 | TUBE | Yes | NIPDAU | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | BCMS
TPS2000CDGN.A | Active | Production | HVSSOP (DGN) | 8 | 80 | TUBE | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | BCMS
TPS2000CDGN.B | Active | Production | HVSSOP (DGN) | 8 | 80 | TUBE | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | BCMS
TPS2000CDGNR | Active | Production | HVSSOP (DGN) | 8 | 2500 | LARGE T&R | Yes | NIPDAU | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | BCMS
TPS2000CDGNR.A | Active | Production | HVSSOP (DGN) | 8 | 2500 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | BCMS
TPS2000CDGNR.B | Active | Production | HVSSOP (DGN) | 8 | 2500 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | BCMS
TPS2001CDGK | Active | Production | VSSOP (DGK) | 8 | 80 | TUBE | Yes | NIPDAUAG | SN | Level-2-260C-1 YEAR | 40 to 125 | PXGI
TPS2001CDGK.B | Active | Production | VSSOP (DGK) | 8 | 80 | TUBE | Yes | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | PXGI
TPS2001CDGKR | Active | Production | VSSOP (DGK) | 8 | 2500 | LARGE T&R | Yes | NIPDAU | SN | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | PXGI
TPS2001CDGKR.B | Active | Production | VSSOP (DGK) | 8 | 2500 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | PXGI
TPS2001CDGN | Active | Production | HVSSOP (DGN) | 8 | 80 | TUBE | Yes | NIPDAU | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | VBWQ
TPS2001CDGN.A | Active | Production | HVSSOP (DGN) | 8 | 80 | TUBE | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | VBWQ
TPS2001CDGN.B | Active | Production | HVSSOP (DGN) | 8 | 80 | TUBE | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | VBWQ
TPS2001CDGNR | Active | Production | HVSSOP (DGN) | 8 | 2500 | LARGE T&R | Yes | NIPDAU | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | VBWQ
TPS2001CDGNR.A | Active | Production | HVSSOP (DGN) | 8 | 2500 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | VBWQ
TPS2001CDGNR.B | Active | Production | HVSSOP (DGN) | 8 | 2500 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | VBWQ
TPS2041CDBVR | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | SN | Level-2-260C-1 YEAR | 40 to 125 | PYJI
TPS2041CDBVR.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | PYJI
TPS2041CDBVR.B | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | PYJI
TPS2041CDBVRG4 | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | PYJI
TPS2041CDBVRG4.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | PYJI
TPS2041CDBVRG4.B | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | PYJI
 | Active |  | SOT-23 (DBV) | 5 |  | Yes |  | Level-2-260C-1 YEAR |  | PYJI
```

#### Raw extracted text

```text
PACKAGE OPTION ADDENDUM
www.ti.com 11-Apr-2026
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
905X0205100 Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 85 VBYQ
TPS2000CDGK Active Production VSSOP (DGK) | 8 80 | TUBE Yes NIPDAUAG | SN Level-2-260C-1 YEAR -40 to 125 PXFI
TPS2000CDGK.B Active Production VSSOP (DGK) | 8 80 | TUBE Yes NIPDAUAG Level-2-260C-1 YEAR -40 to 125 PXFI
TPS2000CDGKR Active Production VSSOP (DGK) | 8 2500 | LARGE T&R Yes NIPDAU | SN
| NIPDAUAG
Level-2-260C-1 YEAR -40 to 125 PXFI
TPS2000CDGKR.B Active Production VSSOP (DGK) | 8 2500 | LARGE T&R Yes NIPDAUAG Level-2-260C-1 YEAR -40 to 125 PXFI
TPS2000CDGN Active Production HVSSOP (DGN) | 8 80 | TUBE Yes NIPDAU | NIPDAUAG Level-2-260C-1 YEAR -40 to 125 BCMS
TPS2000CDGN.A Active Production HVSSOP (DGN) | 8 80 | TUBE Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 BCMS
TPS2000CDGN.B Active Production HVSSOP (DGN) | 8 80 | TUBE Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 BCMS
TPS2000CDGNR Active Production HVSSOP (DGN) | 8 2500 | LARGE T&R Yes NIPDAU | NIPDAUAG Level-2-260C-1 YEAR -40 to 125 BCMS
TPS2000CDGNR.A Active Production HVSSOP (DGN) | 8 2500 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 BCMS
TPS2000CDGNR.B Active Production HVSSOP (DGN) | 8 2500 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 BCMS
TPS2001CDGK Active Production VSSOP (DGK) | 8 80 | TUBE Yes NIPDAUAG | SN Level-2-260C-1 YEAR -40 to 125 PXGI
TPS2001CDGK.B Active Production VSSOP (DGK) | 8 80 | TUBE Yes NIPDAUAG Level-2-260C-1 YEAR -40 to 125 PXGI
TPS2001CDGKR Active Production VSSOP (DGK) | 8 2500 | LARGE T&R Yes NIPDAU | SN
| NIPDAUAG
Level-2-260C-1 YEAR -40 to 125 PXGI
TPS2001CDGKR.B Active Production VSSOP (DGK) | 8 2500 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 PXGI
TPS2001CDGN Active Production HVSSOP (DGN) | 8 80 | TUBE Yes NIPDAU | NIPDAUAG Level-2-260C-1 YEAR -40 to 125 VBWQ
TPS2001CDGN.A Active Production HVSSOP (DGN) | 8 80 | TUBE Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 VBWQ
TPS2001CDGN.B Active Production HVSSOP (DGN) | 8 80 | TUBE Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 VBWQ
TPS2001CDGNR Active Production HVSSOP (DGN) | 8 2500 | LARGE T&R Yes NIPDAU | NIPDAUAG Level-2-260C-1 YEAR -40 to 125 VBWQ
TPS2001CDGNR.A Active Production HVSSOP (DGN) | 8 2500 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 VBWQ
TPS2001CDGNR.B Active Production HVSSOP (DGN) | 8 2500 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 VBWQ
TPS2041CDBVR Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes NIPDAU | SN Level-2-260C-1 YEAR -40 to 125 PYJI
TPS2041CDBVR.A Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 PYJI
TPS2041CDBVR.B Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 PYJI
TPS2041CDBVRG4 Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 PYJI
TPS2041CDBVRG4.A Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 PYJI
TPS2041CDBVRG4.B Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 PYJI
TPS2041CDBVT Active Production SOT-23 (DBV) | 5 250 | SMALL T&R Yes NIPDAU | SN Level-2-260C-1 YEAR -40 to 125 PYJI
Addendum-Page 1
```

### Page 27

#### Extracted tables

Table 1:

```text
Orderable part number | Status (1) | Material type (2) | Package | Pins | Package qty | Carrier | RoHS (3) | Lead finish/ Ball material (4) | MSL rating/ Peak reflow (5) | Op temp ( deg C) | Part marking (6)
TPS2041CDBVT.A | Active | Production | SOT-23 (DBV) | 5 | 250 | SMALL T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | PYJI
TPS2041CDBVT.B | Active | Production | SOT-23 (DBV) | 5 | 250 | SMALL T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | PYJI
TPS2051CDBVR | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | SN | Level-2-260C-1 YEAR | 40 to 125 | VBYQ
TPS2051CDBVR.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | VBYQ
TPS2051CDBVR.B | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | VBYQ
TPS2051CDBVRG4 | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | VBYQ
TPS2051CDBVRG4.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | VBYQ
TPS2051CDBVRG4.B | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | VBYQ
TPS2051CDBVT | Active | Production | SOT-23 (DBV) | 5 | 250 | SMALL T&R | Yes | NIPDAU | SN | Level-2-260C-1 YEAR | 40 to 125 | VBYQ
TPS2051CDBVT.A | Active | Production | SOT-23 (DBV) | 5 | 250 | SMALL T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | VBYQ
TPS2051CDBVT.B | Active | Production | SOT-23 (DBV) | 5 | 250 | SMALL T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | VBYQ
TPS2061CDBVR | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | PXLI
TPS2061CDBVR.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | PXLI
TPS2061CDBVR.B | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | PXLI
TPS2061CDBVRG4 | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | PXLI
TPS2061CDBVRG4.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | PXLI
TPS2061CDBVRG4.B | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | PXLI
TPS2061CDBVT | Active | Production | SOT-23 (DBV) | 5 | 250 | SMALL T&R | Yes | NIPDAU | SN | Level-2-260C-1 YEAR | 40 to 125 | PXLI
TPS2061CDBVT.A | Active | Production | SOT-23 (DBV) | 5 | 250 | SMALL T&R | Yes | SN | Level-2-260C-1 YEAR | 40 to 125 | PXLI
TPS2061CDBVT.B | Active | Production | SOT-23 (DBV) | 5 | 250 | SMALL T&R | Yes | SN | Level-2-260C-1 YEAR | 40 to 125 | PXLI
TPS2061CDGN | Active | Production | HVSSOP (DGN) | 8 | 80 | TUBE | Yes | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | PXMI
TPS2061CDGN.A | Active | Production | HVSSOP (DGN) | 8 | 80 | TUBE | Yes | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | PXMI
TPS2061CDGN.B | Active | Production | HVSSOP (DGN) | 8 | 80 | TUBE | Yes | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | PXMI
TPS2061CDGNR | Active | Production | HVSSOP (DGN) | 8 | 2500 | LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | PXMI
TPS2061CDGNR.A | Active | Production | HVSSOP (DGN) | 8 | 2500 | LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | PXMI
TPS2061CDGNR.B | Active | Production | HVSSOP (DGN) | 8 | 2500 | LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | PXMI
TPS2065CDBVR | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | VCAQ
TPS2065CDBVR-2 | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | SN | Level-2-260C-1 YEAR | 40 to 125 | PYQI
TPS2065CDBVR-2.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | 40 to 125 | PYQI
TPS2065CDBVR.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | VCAQ
 | Active |  | SOT-23 (DBV) | 5 |  | Yes |  | Level-2-260C-1 YEAR |  | VCAQ
```

#### Raw extracted text

```text
PACKAGE OPTION ADDENDUM
www.ti.com 11-Apr-2026
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
TPS2041CDBVT.A Active Production SOT-23 (DBV) | 5 250 | SMALL T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 PYJI
TPS2041CDBVT.B Active Production SOT-23 (DBV) | 5 250 | SMALL T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 PYJI
TPS2051CDBVR Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes NIPDAU | SN Level-2-260C-1 YEAR -40 to 125 VBYQ
TPS2051CDBVR.A Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 VBYQ
TPS2051CDBVR.B Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 VBYQ
TPS2051CDBVRG4 Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 VBYQ
TPS2051CDBVRG4.A Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 VBYQ
TPS2051CDBVRG4.B Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 VBYQ
TPS2051CDBVT Active Production SOT-23 (DBV) | 5 250 | SMALL T&R Yes NIPDAU | SN Level-2-260C-1 YEAR -40 to 125 VBYQ
TPS2051CDBVT.A Active Production SOT-23 (DBV) | 5 250 | SMALL T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 VBYQ
TPS2051CDBVT.B Active Production SOT-23 (DBV) | 5 250 | SMALL T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 VBYQ
TPS2061CDBVR Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 PXLI
TPS2061CDBVR.A Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 PXLI
TPS2061CDBVR.B Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 PXLI
TPS2061CDBVRG4 Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 PXLI
TPS2061CDBVRG4.A Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 PXLI
TPS2061CDBVRG4.B Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 PXLI
TPS2061CDBVT Active Production SOT-23 (DBV) | 5 250 | SMALL T&R Yes NIPDAU | SN Level-2-260C-1 YEAR -40 to 125 PXLI
TPS2061CDBVT.A Active Production SOT-23 (DBV) | 5 250 | SMALL T&R Yes SN Level-2-260C-1 YEAR -40 to 125 PXLI
TPS2061CDBVT.B Active Production SOT-23 (DBV) | 5 250 | SMALL T&R Yes SN Level-2-260C-1 YEAR -40 to 125 PXLI
TPS2061CDGN Active Production HVSSOP (DGN) | 8 80 | TUBE Yes NIPDAUAG Level-2-260C-1 YEAR -40 to 125 PXMI
TPS2061CDGN.A Active Production HVSSOP (DGN) | 8 80 | TUBE Yes NIPDAUAG Level-2-260C-1 YEAR -40 to 125 PXMI
TPS2061CDGN.B Active Production HVSSOP (DGN) | 8 80 | TUBE Yes NIPDAUAG Level-2-260C-1 YEAR -40 to 125 PXMI
TPS2061CDGNR Active Production HVSSOP (DGN) | 8 2500 | LARGE T&R Yes NIPDAUAG Level-2-260C-1 YEAR -40 to 125 PXMI
TPS2061CDGNR.A Active Production HVSSOP (DGN) | 8 2500 | LARGE T&R Yes NIPDAUAG Level-2-260C-1 YEAR -40 to 125 PXMI
TPS2061CDGNR.B Active Production HVSSOP (DGN) | 8 2500 | LARGE T&R Yes NIPDAUAG Level-2-260C-1 YEAR -40 to 125 PXMI
TPS2065CDBVR Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 VCAQ
TPS2065CDBVR-2 Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes NIPDAU | SN Level-2-260C-1 YEAR -40 to 125 PYQI
TPS2065CDBVR-2.A Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes SN Level-2-260C-1 YEAR -40 to 125 PYQI
TPS2065CDBVR.A Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 VCAQ
TPS2065CDBVR.B Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 VCAQ
Addendum-Page 2
```

### Page 28

#### Extracted tables

Table 1:

```text
Orderable part number | Status (1) | Material type (2) | Package | Pins | Package qty | Carrier | RoHS (3) | Lead finish/ Ball material (4) | MSL rating/ Peak reflow (5) | Op temp ( deg C) | Part marking (6)
TPS2065CDBVRG4 | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | VCAQ
TPS2065CDBVRG4.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | VCAQ
TPS2065CDBVRG4.B | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | VCAQ
TPS2065CDBVT | Active | Production | SOT-23 (DBV) | 5 | 250 | SMALL T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | VCAQ
TPS2065CDBVT-2 | Active | Production | SOT-23 (DBV) | 5 | 250 | SMALL T&R | Yes | NIPDAU | SN | Level-2-260C-1 YEAR | 40 to 125 | PYQI
TPS2065CDBVT-2.A | Active | Production | SOT-23 (DBV) | 5 | 250 | SMALL T&R | Yes | SN | Level-2-260C-1 YEAR | 40 to 125 | PYQI
TPS2065CDBVT.A | Active | Production | SOT-23 (DBV) | 5 | 250 | SMALL T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | VCAQ
TPS2065CDBVT.B | Active | Production | SOT-23 (DBV) | 5 | 250 | SMALL T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | VCAQ
TPS2065CDGN | Active | Production | HVSSOP (DGN) | 8 | 80 | TUBE | Yes | NIPDAU | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | VCAQ
TPS2065CDGN-2 | Active | Production | HVSSOP (DGN) | 8 | 80 | TUBE | Yes | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | PYRI
TPS2065CDGN-2.A | Active | Production | HVSSOP (DGN) | 8 | 80 | TUBE | Yes | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | PYRI
TPS2065CDGN.A | Active | Production | HVSSOP (DGN) | 8 | 80 | TUBE | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | VCAQ
TPS2065CDGN.B | Active | Production | HVSSOP (DGN) | 8 | 80 | TUBE | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | VCAQ
TPS2065CDGNR | Active | Production | HVSSOP (DGN) | 8 | 2500 | LARGE T&R | Yes | NIPDAU | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | VCAQ
TPS2065CDGNR-2 | Active | Production | HVSSOP (DGN) | 8 | 2500 | LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | PYRI
TPS2065CDGNR-2.A | Active | Production | HVSSOP (DGN) | 8 | 2500 | LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | PYRI
TPS2065CDGNR.A | Active | Production | HVSSOP (DGN) | 8 | 2500 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | VCAQ
TPS2065CDGNR.B | Active | Production | HVSSOP (DGN) | 8 | 2500 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | VCAQ
TPS2068CDGN | Active | Production | HVSSOP (DGN) | 8 | 80 | TUBE | Yes | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | PXNI
TPS2068CDGN.A | Active | Production | HVSSOP (DGN) | 8 | 80 | TUBE | Yes | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | PXNI
TPS2068CDGN.B | Active | Production | HVSSOP (DGN) | 8 | 80 | TUBE | Yes | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | PXNI
TPS2068CDGNR | Active | Production | HVSSOP (DGN) | 8 | 2500 | LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | PXNI
TPS2068CDGNR.A | Active | Production | HVSSOP (DGN) | 8 | 2500 | LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | PXNI
TPS2068CDGNR.B | Active | Production | HVSSOP (DGN) | 8 | 2500 | LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | PXNI
TPS2069CDBVR | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | SN | Level-2-260C-1 YEAR | 40 to 125 | PYKI
TPS2069CDBVR.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | 40 to 125 | PYKI
TPS2069CDBVR.B | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | 40 to 125 | PYKI
TPS2069CDBVT | Active | Production | SOT-23 (DBV) | 5 | 250 | SMALL T&R | Yes | NIPDAU | SN | Level-2-260C-1 YEAR | 40 to 125 | PYKI
TPS2069CDBVT.A | Active | Production | SOT-23 (DBV) | 5 | 250 | SMALL T&R | Yes | SN | Level-2-260C-1 YEAR | 40 to 125 | PYKI
TPS2069CDBVT.B | Active | Production | SOT-23 (DBV) | 5 | 250 | SMALL T&R | Yes | SN | Level-2-260C-1 YEAR | 40 to 125 | PYKI
 | Active |  | SOT-23 (DBV) | 5 |  | Yes |  | Level-2-260C-1 YEAR |  | PYKI
```

#### Raw extracted text

```text
PACKAGE OPTION ADDENDUM
www.ti.com 11-Apr-2026
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
TPS2065CDBVRG4 Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 VCAQ
TPS2065CDBVRG4.A Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 VCAQ
TPS2065CDBVRG4.B Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 VCAQ
TPS2065CDBVT Active Production SOT-23 (DBV) | 5 250 | SMALL T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 VCAQ
TPS2065CDBVT-2 Active Production SOT-23 (DBV) | 5 250 | SMALL T&R Yes NIPDAU | SN Level-2-260C-1 YEAR -40 to 125 PYQI
TPS2065CDBVT-2.A Active Production SOT-23 (DBV) | 5 250 | SMALL T&R Yes SN Level-2-260C-1 YEAR -40 to 125 PYQI
TPS2065CDBVT.A Active Production SOT-23 (DBV) | 5 250 | SMALL T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 VCAQ
TPS2065CDBVT.B Active Production SOT-23 (DBV) | 5 250 | SMALL T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 VCAQ
TPS2065CDGN Active Production HVSSOP (DGN) | 8 80 | TUBE Yes NIPDAU | NIPDAUAG Level-2-260C-1 YEAR -40 to 125 VCAQ
TPS2065CDGN-2 Active Production HVSSOP (DGN) | 8 80 | TUBE Yes NIPDAUAG Level-2-260C-1 YEAR -40 to 125 PYRI
TPS2065CDGN-2.A Active Production HVSSOP (DGN) | 8 80 | TUBE Yes NIPDAUAG Level-2-260C-1 YEAR -40 to 125 PYRI
TPS2065CDGN.A Active Production HVSSOP (DGN) | 8 80 | TUBE Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 VCAQ
TPS2065CDGN.B Active Production HVSSOP (DGN) | 8 80 | TUBE Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 VCAQ
TPS2065CDGNR Active Production HVSSOP (DGN) | 8 2500 | LARGE T&R Yes NIPDAU | NIPDAUAG Level-2-260C-1 YEAR -40 to 125 VCAQ
TPS2065CDGNR-2 Active Production HVSSOP (DGN) | 8 2500 | LARGE T&R Yes NIPDAUAG Level-2-260C-1 YEAR -40 to 125 PYRI
TPS2065CDGNR-2.A Active Production HVSSOP (DGN) | 8 2500 | LARGE T&R Yes NIPDAUAG Level-2-260C-1 YEAR -40 to 125 PYRI
TPS2065CDGNR.A Active Production HVSSOP (DGN) | 8 2500 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 VCAQ
TPS2065CDGNR.B Active Production HVSSOP (DGN) | 8 2500 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 VCAQ
TPS2068CDGN Active Production HVSSOP (DGN) | 8 80 | TUBE Yes NIPDAUAG Level-2-260C-1 YEAR -40 to 125 PXNI
TPS2068CDGN.A Active Production HVSSOP (DGN) | 8 80 | TUBE Yes NIPDAUAG Level-2-260C-1 YEAR -40 to 125 PXNI
TPS2068CDGN.B Active Production HVSSOP (DGN) | 8 80 | TUBE Yes NIPDAUAG Level-2-260C-1 YEAR -40 to 125 PXNI
TPS2068CDGNR Active Production HVSSOP (DGN) | 8 2500 | LARGE T&R Yes NIPDAUAG Level-2-260C-1 YEAR -40 to 125 PXNI
TPS2068CDGNR.A Active Production HVSSOP (DGN) | 8 2500 | LARGE T&R Yes NIPDAUAG Level-2-260C-1 YEAR -40 to 125 PXNI
TPS2068CDGNR.B Active Production HVSSOP (DGN) | 8 2500 | LARGE T&R Yes NIPDAUAG Level-2-260C-1 YEAR -40 to 125 PXNI
TPS2069CDBVR Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes NIPDAU | SN Level-2-260C-1 YEAR -40 to 125 PYKI
TPS2069CDBVR.A Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes SN Level-2-260C-1 YEAR -40 to 125 PYKI
TPS2069CDBVR.B Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes SN Level-2-260C-1 YEAR -40 to 125 PYKI
TPS2069CDBVT Active Production SOT-23 (DBV) | 5 250 | SMALL T&R Yes NIPDAU | SN Level-2-260C-1 YEAR -40 to 125 PYKI
TPS2069CDBVT.A Active Production SOT-23 (DBV) | 5 250 | SMALL T&R Yes SN Level-2-260C-1 YEAR -40 to 125 PYKI
TPS2069CDBVT.B Active Production SOT-23 (DBV) | 5 250 | SMALL T&R Yes SN Level-2-260C-1 YEAR -40 to 125 PYKI
TPS2069CDBVTG4 Active Production SOT-23 (DBV) | 5 250 | SMALL T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 PYKI
Addendum-Page 3
```

### Page 29

#### Extracted tables

Table 1:

```text
Orderable part number | Status (1) | Material type (2) | Package | Pins | Package qty | Carrier | RoHS (3) | Lead finish/ Ball material (4) | MSL rating/ Peak reflow (5) | Op temp ( deg C) | Part marking (6)
TPS2069CDBVTG4.A | Active | Production | SOT-23 (DBV) | 5 | 250 | SMALL T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | PYKI
TPS2069CDBVTG4.B | Active | Production | SOT-23 (DBV) | 5 | 250 | SMALL T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | PYKI
TPS2069CDGN | Active | Production | HVSSOP (DGN) | 8 | 80 | TUBE | Yes | NIPDAU | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | VBUQ
TPS2069CDGN-2 | Active | Production | HVSSOP (DGN) | 8 | 80 | TUBE | Yes | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | PYSI
TPS2069CDGN-2.A | Active | Production | HVSSOP (DGN) | 8 | 80 | TUBE | Yes | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | PYSI
TPS2069CDGN.A | Active | Production | HVSSOP (DGN) | 8 | 80 | TUBE | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | VBUQ
TPS2069CDGN.B | Active | Production | HVSSOP (DGN) | 8 | 80 | TUBE | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | VBUQ
TPS2069CDGNR | Active | Production | HVSSOP (DGN) | 8 | 2500 | LARGE T&R | Yes | NIPDAU | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | VBUQ
TPS2069CDGNR-2 | Active | Production | HVSSOP (DGN) | 8 | 2500 | LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | PYSI
TPS2069CDGNR-2.A | Active | Production | HVSSOP (DGN) | 8 | 2500 | LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | 40 to 125 | PYSI
TPS2069CDGNR.A | Active | Production | HVSSOP (DGN) | 8 | 2500 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | VBUQ
TPS2069CDGNR.B | Active | Production | HVSSOP (DGN) | 8 | 2500 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | VBUQ
```

#### Raw extracted text

```text
PACKAGE OPTION ADDENDUM
www.ti.com 11-Apr-2026
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
TPS2069CDBVTG4.A Active Production SOT-23 (DBV) | 5 250 | SMALL T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 PYKI
TPS2069CDBVTG4.B Active Production SOT-23 (DBV) | 5 250 | SMALL T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 PYKI
TPS2069CDGN Active Production HVSSOP (DGN) | 8 80 | TUBE Yes NIPDAU | NIPDAUAG Level-2-260C-1 YEAR -40 to 125 VBUQ
TPS2069CDGN-2 Active Production HVSSOP (DGN) | 8 80 | TUBE Yes NIPDAUAG Level-2-260C-1 YEAR -40 to 125 PYSI
TPS2069CDGN-2.A Active Production HVSSOP (DGN) | 8 80 | TUBE Yes NIPDAUAG Level-2-260C-1 YEAR -40 to 125 PYSI
TPS2069CDGN.A Active Production HVSSOP (DGN) | 8 80 | TUBE Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 VBUQ
TPS2069CDGN.B Active Production HVSSOP (DGN) | 8 80 | TUBE Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 VBUQ
TPS2069CDGNR Active Production HVSSOP (DGN) | 8 2500 | LARGE T&R Yes NIPDAU | NIPDAUAG Level-2-260C-1 YEAR -40 to 125 VBUQ
TPS2069CDGNR-2 Active Production HVSSOP (DGN) | 8 2500 | LARGE T&R Yes NIPDAUAG Level-2-260C-1 YEAR -40 to 125 PYSI
TPS2069CDGNR-2.A Active Production HVSSOP (DGN) | 8 2500 | LARGE T&R Yes NIPDAUAG Level-2-260C-1 YEAR -40 to 125 PYSI
TPS2069CDGNR.A Active Production HVSSOP (DGN) | 8 2500 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 VBUQ
TPS2069CDGNR.B Active Production HVSSOP (DGN) | 8 2500 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 VBUQ

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

Multiple part markings will be inside parentheses. Only one part marking contained in parentheses and separated by a "~" will appear on a part. If a line is indented then it is a continuation of the previous line and the two
combined represent the entire part marking for that device.

Addendum-Page 4
```

### Page 30

#### Raw extracted text

```text
PACKAGE OPTION ADDENDUM
www.ti.com 11-Apr-2026
Important Information and Disclaimer:The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and
makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative
and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers
and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.

Addendum-Page 5
```

### Page 31

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
TPS2000CDGKR | VSSOP | DGK | 8 | 2500 | 330.0 | 12.4 | 5.3 | 3.4 | 1.4 | 8.0 | 12.0 | Q1
TPS2000CDGNR | HVSSOP | DGN | 8 | 2500 | 330.0 | 12.4 | 5.3 | 3.4 | 1.4 | 8.0 | 12.0 | Q1
TPS2001CDGKR | VSSOP | DGK | 8 | 2500 | 330.0 | 12.4 | 5.3 | 3.4 | 1.4 | 8.0 | 12.0 | Q1
TPS2001CDGNR | HVSSOP | DGN | 8 | 2500 | 330.0 | 12.4 | 5.3 | 3.3 | 1.3 | 8.0 | 12.0 | Q1
TPS2001CDGNR | HVSSOP | DGN | 8 | 2500 | 330.0 | 12.4 | 5.3 | 3.4 | 1.4 | 8.0 | 12.0 | Q1
TPS2041CDBVR | SOT-23 | DBV | 5 | 3000 | 178.0 | 9.0 | 3.23 | 3.17 | 1.37 | 4.0 | 8.0 | Q3
TPS2041CDBVR | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3
TPS2041CDBVR | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3
TPS2041CDBVRG4 | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3
TPS2041CDBVT | SOT-23 | DBV | 5 | 250 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3
TPS2051CDBVR | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3
TPS2051CDBVR | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3
TPS2051CDBVRG4 | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3
TPS2051CDBVRG4 | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3
TPS2051CDBVT | SOT-23 | DBV | 5 | 250 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3
TPS2061CDBVR | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3
```

#### Raw extracted text

```text
PACKAGE MATERIALS INFORMATION
www.ti.com 10-Apr-2026
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
TPS2000CDGKR VSSOP DGK 8 2500 330.0 12.4 5.3 3.4 1.4 8.0 12.0 Q1
TPS2000CDGNR HVSSOP DGN 8 2500 330.0 12.4 5.3 3.4 1.4 8.0 12.0 Q1
TPS2001CDGKR VSSOP DGK 8 2500 330.0 12.4 5.3 3.4 1.4 8.0 12.0 Q1
TPS2001CDGNR HVSSOP DGN 8 2500 330.0 12.4 5.3 3.3 1.3 8.0 12.0 Q1
TPS2001CDGNR HVSSOP DGN 8 2500 330.0 12.4 5.3 3.4 1.4 8.0 12.0 Q1
TPS2041CDBVR SOT-23 DBV 5 3000 178.0 9.0 3.23 3.17 1.37 4.0 8.0 Q3
TPS2041CDBVR SOT-23 DBV 5 3000 180.0 8.4 3.2 3.2 1.4 4.0 8.0 Q3
TPS2041CDBVR SOT-23 DBV 5 3000 180.0 8.4 3.2 3.2 1.4 4.0 8.0 Q3
TPS2041CDBVRG4 SOT-23 DBV 5 3000 180.0 8.4 3.2 3.2 1.4 4.0 8.0 Q3
TPS2041CDBVT SOT-23 DBV 5 250 180.0 8.4 3.2 3.2 1.4 4.0 8.0 Q3
TPS2051CDBVR SOT-23 DBV 5 3000 180.0 8.4 3.2 3.2 1.4 4.0 8.0 Q3
TPS2051CDBVR SOT-23 DBV 5 3000 180.0 8.4 3.2 3.2 1.4 4.0 8.0 Q3
TPS2051CDBVRG4 SOT-23 DBV 5 3000 180.0 8.4 3.2 3.2 1.4 4.0 8.0 Q3
TPS2051CDBVRG4 SOT-23 DBV 5 3000 180.0 8.4 3.2 3.2 1.4 4.0 8.0 Q3
TPS2051CDBVT SOT-23 DBV 5 250 180.0 8.4 3.2 3.2 1.4 4.0 8.0 Q3
TPS2061CDBVR SOT-23 DBV 5 3000 180.0 8.4 3.2 3.2 1.4 4.0 8.0 Q3
Pack Materials-Page 1
```

### Page 32

#### Extracted tables

Table 1:

```text
Device | Package Type | Package Drawing | Pins | SPQ | Reel Diameter (mm) | Reel Width W1 (mm) | A0 (mm) | B0 (mm) | K0 (mm) | P1 (mm) | W (mm) | Pin1 Quadrant
TPS2061CDBVR | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3
TPS2061CDBVR | SOT-23 | DBV | 5 | 3000 | 178.0 | 9.0 | 3.23 | 3.17 | 1.37 | 4.0 | 8.0 | Q3
TPS2061CDBVRG4 | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3
TPS2061CDBVT | SOT-23 | DBV | 5 | 250 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3
TPS2061CDBVT | SOT-23 | DBV | 5 | 250 | 178.0 | 8.4 | 3.23 | 3.17 | 1.37 | 4.0 | 8.0 | Q3
TPS2061CDGNR | HVSSOP | DGN | 8 | 2500 | 330.0 | 12.4 | 5.3 | 3.4 | 1.4 | 8.0 | 12.0 | Q1
TPS2065CDBVR | SOT-23 | DBV | 5 | 3000 | 178.0 | 9.0 | 3.23 | 3.17 | 1.37 | 4.0 | 8.0 | Q3
TPS2065CDBVR-2 | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3
TPS2065CDBVR-2 | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3
TPS2065CDBVRG4 | SOT-23 | DBV | 5 | 3000 | 178.0 | 9.0 | 3.23 | 3.17 | 1.37 | 4.0 | 8.0 | Q3
TPS2065CDBVT | SOT-23 | DBV | 5 | 250 | 178.0 | 8.4 | 3.23 | 3.17 | 1.37 | 4.0 | 8.0 | Q3
TPS2065CDBVT-2 | SOT-23 | DBV | 5 | 250 | 178.0 | 8.4 | 3.23 | 3.17 | 1.37 | 4.0 | 8.0 | Q3
TPS2065CDBVT-2 | SOT-23 | DBV | 5 | 250 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3
TPS2065CDGNR | HVSSOP | DGN | 8 | 2500 | 330.0 | 12.4 | 5.3 | 3.4 | 1.4 | 8.0 | 12.0 | Q1
TPS2065CDGNR-2 | HVSSOP | DGN | 8 | 2500 | 330.0 | 12.4 | 5.3 | 3.4 | 1.4 | 8.0 | 12.0 | Q1
TPS2068CDGNR | HVSSOP | DGN | 8 | 2500 | 330.0 | 12.4 | 5.3 | 3.4 | 1.4 | 8.0 | 12.0 | Q1
TPS2069CDBVR | SOT-23 | DBV | 5 | 3000 | 178.0 | 9.0 | 3.3 | 3.2 | 1.4 | 4.0 | 8.0 | Q3
TPS2069CDBVR | SOT-23 | DBV | 5 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3
TPS2069CDBVT | SOT-23 | DBV | 5 | 250 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3
TPS2069CDBVTG4 | SOT-23 | DBV | 5 | 250 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3
TPS2069CDGNR | HVSSOP | DGN | 8 | 2500 | 330.0 | 12.4 | 5.3 | 3.4 | 1.4 | 8.0 | 12.0 | Q1
TPS2069CDGNR | HVSSOP | DGN | 8 | 2500 | 330.0 | 12.4 | 5.3 | 3.3 | 1.3 | 8.0 | 12.0 | Q1
TPS2069CDGNR-2 | HVSSOP | DGN | 8 | 2500 | 330.0 | 12.4 | 5.3 | 3.4 | 1.4 | 8.0 | 12.0 | Q1
```

#### Raw extracted text

```text
PACKAGE MATERIALS INFORMATION

www.ti.com 10-Apr-2026
Device Package
Type
Package
Drawing
Pins SPQ Reel
Diameter
(mm)
Reel
Width
W1 (mm)
A0
(mm)
B0
(mm)
K0
(mm)
P1
(mm)
W
(mm)
Pin1
Quadrant
TPS2061CDBVR SOT-23 DBV 5 3000 180.0 8.4 3.2 3.2 1.4 4.0 8.0 Q3
TPS2061CDBVR SOT-23 DBV 5 3000 178.0 9.0 3.23 3.17 1.37 4.0 8.0 Q3
TPS2061CDBVRG4 SOT-23 DBV 5 3000 180.0 8.4 3.2 3.2 1.4 4.0 8.0 Q3
TPS2061CDBVT SOT-23 DBV 5 250 180.0 8.4 3.2 3.2 1.4 4.0 8.0 Q3
TPS2061CDBVT SOT-23 DBV 5 250 178.0 8.4 3.23 3.17 1.37 4.0 8.0 Q3
TPS2061CDGNR HVSSOP DGN 8 2500 330.0 12.4 5.3 3.4 1.4 8.0 12.0 Q1
TPS2065CDBVR SOT-23 DBV 5 3000 178.0 9.0 3.23 3.17 1.37 4.0 8.0 Q3
TPS2065CDBVR-2 SOT-23 DBV 5 3000 180.0 8.4 3.2 3.2 1.4 4.0 8.0 Q3
TPS2065CDBVR-2 SOT-23 DBV 5 3000 180.0 8.4 3.2 3.2 1.4 4.0 8.0 Q3
TPS2065CDBVRG4 SOT-23 DBV 5 3000 178.0 9.0 3.23 3.17 1.37 4.0 8.0 Q3
TPS2065CDBVT SOT-23 DBV 5 250 178.0 8.4 3.23 3.17 1.37 4.0 8.0 Q3
TPS2065CDBVT-2 SOT-23 DBV 5 250 178.0 8.4 3.23 3.17 1.37 4.0 8.0 Q3
TPS2065CDBVT-2 SOT-23 DBV 5 250 180.0 8.4 3.2 3.2 1.4 4.0 8.0 Q3
TPS2065CDGNR HVSSOP DGN 8 2500 330.0 12.4 5.3 3.4 1.4 8.0 12.0 Q1
TPS2065CDGNR-2 HVSSOP DGN 8 2500 330.0 12.4 5.3 3.4 1.4 8.0 12.0 Q1
TPS2068CDGNR HVSSOP DGN 8 2500 330.0 12.4 5.3 3.4 1.4 8.0 12.0 Q1
TPS2069CDBVR SOT-23 DBV 5 3000 178.0 9.0 3.3 3.2 1.4 4.0 8.0 Q3
TPS2069CDBVR SOT-23 DBV 5 3000 180.0 8.4 3.2 3.2 1.4 4.0 8.0 Q3
TPS2069CDBVT SOT-23 DBV 5 250 180.0 8.4 3.2 3.2 1.4 4.0 8.0 Q3
TPS2069CDBVTG4 SOT-23 DBV 5 250 180.0 8.4 3.2 3.2 1.4 4.0 8.0 Q3
TPS2069CDGNR HVSSOP DGN 8 2500 330.0 12.4 5.3 3.4 1.4 8.0 12.0 Q1
TPS2069CDGNR HVSSOP DGN 8 2500 330.0 12.4 5.3 3.3 1.3 8.0 12.0 Q1
TPS2069CDGNR-2 HVSSOP DGN 8 2500 330.0 12.4 5.3 3.4 1.4 8.0 12.0 Q1
Pack Materials-Page 2
```

### Page 33

#### Extracted tables

Table 1:

```text
| H
```

Table 2:

```text
Device | Package Type | Package Drawing | Pins | SPQ | Length (mm) | Width (mm) | Height (mm)
TPS2000CDGKR | VSSOP | DGK | 8 | 2500 | 353.0 | 353.0 | 32.0
TPS2000CDGNR | HVSSOP | DGN | 8 | 2500 | 360.0 | 162.0 | 98.0
TPS2001CDGKR | VSSOP | DGK | 8 | 2500 | 353.0 | 353.0 | 32.0
TPS2001CDGNR | HVSSOP | DGN | 8 | 2500 | 370.0 | 355.0 | 55.0
TPS2001CDGNR | HVSSOP | DGN | 8 | 2500 | 360.0 | 162.0 | 98.0
TPS2041CDBVR | SOT-23 | DBV | 5 | 3000 | 180.0 | 180.0 | 18.0
TPS2041CDBVR | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0
TPS2041CDBVR | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0
TPS2041CDBVRG4 | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0
TPS2041CDBVT | SOT-23 | DBV | 5 | 250 | 210.0 | 185.0 | 35.0
TPS2051CDBVR | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0
TPS2051CDBVR | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0
TPS2051CDBVRG4 | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0
TPS2051CDBVRG4 | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0
TPS2051CDBVT | SOT-23 | DBV | 5 | 250 | 210.0 | 185.0 | 35.0
TPS2061CDBVR | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0
TPS2061CDBVR | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0
TPS2061CDBVR | SOT-23 | DBV | 5 | 3000 | 180.0 | 180.0 | 18.0
```

#### Raw extracted text

```text
PACKAGE MATERIALS INFORMATION

www.ti.com 10-Apr-2026
TAPE AND REEL BOX DIMENSIONS
Width (mm)
W LH

*All dimensions are nominal
Device Package Type Package Drawing Pins SPQ Length (mm) Width (mm) Height (mm)
TPS2000CDGKR VSSOP DGK 8 2500 353.0 353.0 32.0
TPS2000CDGNR HVSSOP DGN 8 2500 360.0 162.0 98.0
TPS2001CDGKR VSSOP DGK 8 2500 353.0 353.0 32.0
TPS2001CDGNR HVSSOP DGN 8 2500 370.0 355.0 55.0
TPS2001CDGNR HVSSOP DGN 8 2500 360.0 162.0 98.0
TPS2041CDBVR SOT-23 DBV 5 3000 180.0 180.0 18.0
TPS2041CDBVR SOT-23 DBV 5 3000 210.0 185.0 35.0
TPS2041CDBVR SOT-23 DBV 5 3000 210.0 185.0 35.0
TPS2041CDBVRG4 SOT-23 DBV 5 3000 210.0 185.0 35.0
TPS2041CDBVT SOT-23 DBV 5 250 210.0 185.0 35.0
TPS2051CDBVR SOT-23 DBV 5 3000 210.0 185.0 35.0
TPS2051CDBVR SOT-23 DBV 5 3000 210.0 185.0 35.0
TPS2051CDBVRG4 SOT-23 DBV 5 3000 210.0 185.0 35.0
TPS2051CDBVRG4 SOT-23 DBV 5 3000 210.0 185.0 35.0
TPS2051CDBVT SOT-23 DBV 5 250 210.0 185.0 35.0
TPS2061CDBVR SOT-23 DBV 5 3000 210.0 185.0 35.0
TPS2061CDBVR SOT-23 DBV 5 3000 210.0 185.0 35.0
TPS2061CDBVR SOT-23 DBV 5 3000 180.0 180.0 18.0
Pack Materials-Page 3
```

### Page 34

#### Extracted tables

Table 1:

```text
Device | Package Type | Package Drawing | Pins | SPQ | Length (mm) | Width (mm) | Height (mm)
TPS2061CDBVRG4 | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0
TPS2061CDBVT | SOT-23 | DBV | 5 | 250 | 210.0 | 185.0 | 35.0
TPS2061CDBVT | SOT-23 | DBV | 5 | 250 | 180.0 | 180.0 | 18.0
TPS2061CDGNR | HVSSOP | DGN | 8 | 2500 | 366.0 | 364.0 | 50.0
TPS2065CDBVR | SOT-23 | DBV | 5 | 3000 | 180.0 | 180.0 | 18.0
TPS2065CDBVR-2 | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0
TPS2065CDBVR-2 | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0
TPS2065CDBVRG4 | SOT-23 | DBV | 5 | 3000 | 180.0 | 180.0 | 18.0
TPS2065CDBVT | SOT-23 | DBV | 5 | 250 | 180.0 | 180.0 | 18.0
TPS2065CDBVT-2 | SOT-23 | DBV | 5 | 250 | 180.0 | 180.0 | 18.0
TPS2065CDBVT-2 | SOT-23 | DBV | 5 | 250 | 210.0 | 185.0 | 35.0
TPS2065CDGNR | HVSSOP | DGN | 8 | 2500 | 360.0 | 162.0 | 98.0
TPS2065CDGNR-2 | HVSSOP | DGN | 8 | 2500 | 366.0 | 364.0 | 50.0
TPS2068CDGNR | HVSSOP | DGN | 8 | 2500 | 366.0 | 364.0 | 50.0
TPS2069CDBVR | SOT-23 | DBV | 5 | 3000 | 180.0 | 180.0 | 18.0
TPS2069CDBVR | SOT-23 | DBV | 5 | 3000 | 210.0 | 185.0 | 35.0
TPS2069CDBVT | SOT-23 | DBV | 5 | 250 | 210.0 | 185.0 | 35.0
TPS2069CDBVTG4 | SOT-23 | DBV | 5 | 250 | 210.0 | 185.0 | 35.0
TPS2069CDGNR | HVSSOP | DGN | 8 | 2500 | 366.0 | 364.0 | 50.0
TPS2069CDGNR | HVSSOP | DGN | 8 | 2500 | 370.0 | 355.0 | 55.0
TPS2069CDGNR-2 | HVSSOP | DGN | 8 | 2500 | 366.0 | 364.0 | 50.0
```

#### Raw extracted text

```text
PACKAGE MATERIALS INFORMATION

www.ti.com 10-Apr-2026
Device Package Type Package Drawing Pins SPQ Length (mm) Width (mm) Height (mm)
TPS2061CDBVRG4 SOT-23 DBV 5 3000 210.0 185.0 35.0
TPS2061CDBVT SOT-23 DBV 5 250 210.0 185.0 35.0
TPS2061CDBVT SOT-23 DBV 5 250 180.0 180.0 18.0
TPS2061CDGNR HVSSOP DGN 8 2500 366.0 364.0 50.0
TPS2065CDBVR SOT-23 DBV 5 3000 180.0 180.0 18.0
TPS2065CDBVR-2 SOT-23 DBV 5 3000 210.0 185.0 35.0
TPS2065CDBVR-2 SOT-23 DBV 5 3000 210.0 185.0 35.0
TPS2065CDBVRG4 SOT-23 DBV 5 3000 180.0 180.0 18.0
TPS2065CDBVT SOT-23 DBV 5 250 180.0 180.0 18.0
TPS2065CDBVT-2 SOT-23 DBV 5 250 180.0 180.0 18.0
TPS2065CDBVT-2 SOT-23 DBV 5 250 210.0 185.0 35.0
TPS2065CDGNR HVSSOP DGN 8 2500 360.0 162.0 98.0
TPS2065CDGNR-2 HVSSOP DGN 8 2500 366.0 364.0 50.0
TPS2068CDGNR HVSSOP DGN 8 2500 366.0 364.0 50.0
TPS2069CDBVR SOT-23 DBV 5 3000 180.0 180.0 18.0
TPS2069CDBVR SOT-23 DBV 5 3000 210.0 185.0 35.0
TPS2069CDBVT SOT-23 DBV 5 250 210.0 185.0 35.0
TPS2069CDBVTG4 SOT-23 DBV 5 250 210.0 185.0 35.0
TPS2069CDGNR HVSSOP DGN 8 2500 366.0 364.0 50.0
TPS2069CDGNR HVSSOP DGN 8 2500 370.0 355.0 55.0
TPS2069CDGNR-2 HVSSOP DGN 8 2500 366.0 364.0 50.0
Pack Materials-Page 4
```

### Page 35

#### Extracted tables

Table 1:

```text
Device | Package Name | Package Type | Pins | SPQ | L (mm) | W (mm) | T (um) | B (mm)
TPS2000CDGK | DGK | VSSOP | 8 | 80 | 330 | 6.55 | 500 | 2.88
TPS2000CDGK.B | DGK | VSSOP | 8 | 80 | 330 | 6.55 | 500 | 2.88
TPS2000CDGN | DGN | HVSSOP | 8 | 80 | 330 | 6.55 | 500 | 2.88
TPS2000CDGN | DGN | HVSSOP | 8 | 80 | 322 | 6.55 | 1000 | 3.01
TPS2000CDGN.A | DGN | HVSSOP | 8 | 80 | 322 | 6.55 | 1000 | 3.01
TPS2000CDGN.A | DGN | HVSSOP | 8 | 80 | 330 | 6.55 | 500 | 2.88
TPS2000CDGN.B | DGN | HVSSOP | 8 | 80 | 330 | 6.55 | 500 | 2.88
TPS2000CDGN.B | DGN | HVSSOP | 8 | 80 | 322 | 6.55 | 1000 | 3.01
TPS2001CDGK | DGK | VSSOP | 8 | 80 | 330 | 6.55 | 500 | 2.88
TPS2001CDGK.B | DGK | VSSOP | 8 | 80 | 330 | 6.55 | 500 | 2.88
TPS2001CDGN | DGN | HVSSOP | 8 | 80 | 322 | 6.55 | 1000 | 3.01
TPS2001CDGN | DGN | HVSSOP | 8 | 80 | 330 | 6.55 | 500 | 2.88
TPS2001CDGN.A | DGN | HVSSOP | 8 | 80 | 330 | 6.55 | 500 | 2.88
TPS2001CDGN.A | DGN | HVSSOP | 8 | 80 | 322 | 6.55 | 1000 | 3.01
TPS2001CDGN.B | DGN | HVSSOP | 8 | 80 | 330 | 6.55 | 500 | 2.88
TPS2001CDGN.B | DGN | HVSSOP | 8 | 80 | 322 | 6.55 | 1000 | 3.01
TPS2061CDGN | DGN | HVSSOP | 8 | 80 | 330 | 6.55 | 500 | 2.88
TPS2061CDGN.A | DGN | HVSSOP | 8 | 80 | 330 | 6.55 | 500 | 2.88
TPS2061CDGN.B | DGN | HVSSOP | 8 | 80 | 330 | 6.55 | 500 | 2.88
TPS2065CDGN | DGN | HVSSOP | 8 | 80 | 330 | 6.55 | 500 | 2.88
TPS2065CDGN | DGN | HVSSOP | 8 | 80 | 322 | 6.55 | 1000 | 3.01
TPS2065CDGN-2 | DGN | HVSSOP | 8 | 80 | 330 | 6.55 | 500 | 2.88
TPS2065CDGN-2.A | DGN | HVSSOP | 8 | 80 | 330 | 6.55 | 500 | 2.88
TPS2065CDGN.A | DGN | HVSSOP | 8 | 80 | 322 | 6.55 | 1000 | 3.01
TPS2065CDGN.A | DGN | HVSSOP | 8 | 80 | 330 | 6.55 | 500 | 2.88
TPS2065CDGN.B | DGN | HVSSOP | 8 | 80 | 330 | 6.55 | 500 | 2.88
TPS2065CDGN.B | DGN | HVSSOP | 8 | 80 | 322 | 6.55 | 1000 | 3.01
TPS2068CDGN | DGN | HVSSOP | 8 | 80 | 330 | 6.55 | 500 | 2.88
TPS2068CDGN.A | DGN | HVSSOP | 8 | 80 | 330 | 6.55 | 500 | 2.88
```

#### Raw extracted text

```text
PACKAGE MATERIALS INFORMATION

www.ti.com 10-Apr-2026
TUBE

L - Tube length
T - Tube
height
W - Tube
width
B - Alignment groove width

*All dimensions are nominal
Device Package Name Package Type Pins SPQ L (mm) W (mm) T (um) B (mm)
TPS2000CDGK DGK VSSOP 8 80 330 6.55 500 2.88
TPS2000CDGK.B DGK VSSOP 8 80 330 6.55 500 2.88
TPS2000CDGN DGN HVSSOP 8 80 330 6.55 500 2.88
TPS2000CDGN DGN HVSSOP 8 80 322 6.55 1000 3.01
TPS2000CDGN.A DGN HVSSOP 8 80 322 6.55 1000 3.01
TPS2000CDGN.A DGN HVSSOP 8 80 330 6.55 500 2.88
TPS2000CDGN.B DGN HVSSOP 8 80 330 6.55 500 2.88
TPS2000CDGN.B DGN HVSSOP 8 80 322 6.55 1000 3.01
TPS2001CDGK DGK VSSOP 8 80 330 6.55 500 2.88
TPS2001CDGK.B DGK VSSOP 8 80 330 6.55 500 2.88
TPS2001CDGN DGN HVSSOP 8 80 322 6.55 1000 3.01
TPS2001CDGN DGN HVSSOP 8 80 330 6.55 500 2.88
TPS2001CDGN.A DGN HVSSOP 8 80 330 6.55 500 2.88
TPS2001CDGN.A DGN HVSSOP 8 80 322 6.55 1000 3.01
TPS2001CDGN.B DGN HVSSOP 8 80 330 6.55 500 2.88
TPS2001CDGN.B DGN HVSSOP 8 80 322 6.55 1000 3.01
TPS2061CDGN DGN HVSSOP 8 80 330 6.55 500 2.88
TPS2061CDGN.A DGN HVSSOP 8 80 330 6.55 500 2.88
TPS2061CDGN.B DGN HVSSOP 8 80 330 6.55 500 2.88
TPS2065CDGN DGN HVSSOP 8 80 330 6.55 500 2.88
TPS2065CDGN DGN HVSSOP 8 80 322 6.55 1000 3.01
TPS2065CDGN-2 DGN HVSSOP 8 80 330 6.55 500 2.88
TPS2065CDGN-2.A DGN HVSSOP 8 80 330 6.55 500 2.88
TPS2065CDGN.A DGN HVSSOP 8 80 322 6.55 1000 3.01
TPS2065CDGN.A DGN HVSSOP 8 80 330 6.55 500 2.88
TPS2065CDGN.B DGN HVSSOP 8 80 330 6.55 500 2.88
TPS2065CDGN.B DGN HVSSOP 8 80 322 6.55 1000 3.01
TPS2068CDGN DGN HVSSOP 8 80 330 6.55 500 2.88
TPS2068CDGN.A DGN HVSSOP 8 80 330 6.55 500 2.88
Pack Materials-Page 5
```

### Page 36

#### Extracted tables

Table 1:

```text
Device | Package Name | Package Type | Pins | SPQ | L (mm) | W (mm) | T (um) | B (mm)
TPS2068CDGN.B | DGN | HVSSOP | 8 | 80 | 330 | 6.55 | 500 | 2.88
TPS2069CDGN | DGN | HVSSOP | 8 | 80 | 330 | 6.55 | 500 | 2.88
TPS2069CDGN | DGN | HVSSOP | 8 | 80 | 322 | 6.55 | 1000 | 3.01
TPS2069CDGN-2 | DGN | HVSSOP | 8 | 80 | 330 | 6.55 | 500 | 2.88
TPS2069CDGN-2.A | DGN | HVSSOP | 8 | 80 | 330 | 6.55 | 500 | 2.88
TPS2069CDGN.A | DGN | HVSSOP | 8 | 80 | 322 | 6.55 | 1000 | 3.01
TPS2069CDGN.A | DGN | HVSSOP | 8 | 80 | 330 | 6.55 | 500 | 2.88
TPS2069CDGN.B | DGN | HVSSOP | 8 | 80 | 322 | 6.55 | 1000 | 3.01
TPS2069CDGN.B | DGN | HVSSOP | 8 | 80 | 330 | 6.55 | 500 | 2.88
```

#### Raw extracted text

```text
PACKAGE MATERIALS INFORMATION

www.ti.com 10-Apr-2026
Device Package Name Package Type Pins SPQ L (mm) W (mm) T (um) B (mm)
TPS2068CDGN.B DGN HVSSOP 8 80 330 6.55 500 2.88
TPS2069CDGN DGN HVSSOP 8 80 330 6.55 500 2.88
TPS2069CDGN DGN HVSSOP 8 80 322 6.55 1000 3.01
TPS2069CDGN-2 DGN HVSSOP 8 80 330 6.55 500 2.88
TPS2069CDGN-2.A DGN HVSSOP 8 80 330 6.55 500 2.88
TPS2069CDGN.A DGN HVSSOP 8 80 322 6.55 1000 3.01
TPS2069CDGN.A DGN HVSSOP 8 80 330 6.55 500 2.88
TPS2069CDGN.B DGN HVSSOP 8 80 322 6.55 1000 3.01
TPS2069CDGN.B DGN HVSSOP 8 80 330 6.55 500 2.88
Pack Materials-Page 6
```

### Page 37

#### Extracted tables

Table 1:

```text
| 0.1 | C
```

Table 2:

```text
|  | 0.2 | C | A | B
```

#### Raw extracted text

```text
www.ti.com
PACKAGE OUTLINE
C
0.22
0.08 TYP
0.25
3.0
2.6
2X 0.95
1.9
1.45
0.90
0.15
0.00 TYP
5X 0.5
0.3
0.6
0.3 TYP
8
0  TYP
1.9
(0.1)
(0.15)
4X 0 -15
4X 4 -15
A
3.05
2.75
B1.75
1.45
(1.1)
SOT-23 - 1.45 mm max heightDBV0005A
SMALL OUTLINE TRANSISTOR
4214839/K   08/2024
NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
    per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. Refernce JEDEC MO-178.
4. Body dimensions do not include mold flash, protrusions, or gate burrs. Mold flash, protrusions, or gate burrs shall not
    exceed 0.25 mm per side.
5. Support pin may differ or may not be present.
0.2 C A B
1
3
4
5
2
INDEX AREA
PIN 1
 NOTE 5
GAGE PLANE
SEATING PLANE
0.1 C
SCALE  4.000
```

### Page 38

#### Raw extracted text

```text
www.ti.com
EXAMPLE BOARD LAYOUT
0.07 MAX
ARROUND
0.07 MIN
ARROUND
5X (1.1)
5X (0.6)
(2.6)
(1.9)
2X (0.95)
(R0.05) TYP
4214839/K   08/2024
SOT-23 - 1.45 mm max heightDBV0005A
SMALL OUTLINE TRANSISTOR
NOTES: (continued)

6. Publication IPC-7351 may have alternate designs.
7. Solder mask tolerances between and around signal pads can vary based on board fabrication site.

SYMM
LAND PATTERN EXAMPLE
EXPOSED METAL SHOWN
SCALE:15X
PKG
1
3 4
5
2
SOLDER MASK
OPENING
METAL UNDER
SOLDER MASK
SOLDER MASK
DEFINED
EXPOSED METAL
METALSOLDER MASK
OPENING
NON SOLDER MASK
DEFINED
(PREFERRED)
SOLDER MASK DETAILS
EXPOSED METAL
```

### Page 39

#### Raw extracted text

```text
www.ti.com
EXAMPLE STENCIL DESIGN
(2.6)
(1.9)
2X(0.95)
5X (1.1)
5X (0.6)
(R0.05) TYP
SOT-23 - 1.45 mm max heightDBV0005A
SMALL OUTLINE TRANSISTOR
4214839/K   08/2024
NOTES: (continued)

8. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
     design recommendations.
9. Board assembly site may have different recommendations for stencil design.

SOLDER PASTE EXAMPLE
BASED ON 0.125 mm THICK STENCIL
SCALE:15X
SYMM
PKG
1
3 4
5
2
```

### Page 40

#### Extracted tables

Table 1:

```text
| 0.1 | C
```

Table 2:

```text
| 0.13 | C | A B
```

#### Raw extracted text

```text
www.ti.com
PACKAGE OUTLINE
C
6X 0.65
2X
1.95
8X 0.38
0.25
5.05
4.75 TYP
SEATING
PLANE
0.15
0.05
0.25
GAGE PLANE
0 -8
1.1 MAX
0.23
0.13
B 3.1
2.9
NOTE 4
A
3.1
2.9
NOTE 3
0.7
0.4
VSSOP - 1.1 mm max heightDGK0008A
SMALL OUTLINE PACKAGE
4214862/A   04/2023
1
4
5
8
0.13 C A B
PIN 1 INDEX AREA
SEE DETAIL  A
0.1 C
NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
    per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. This dimension does not include mold flash, protrusions, or gate burrs. Mold flash, protrusions, or gate burrs shall not
    exceed 0.15 mm per side.
4. This dimension does not include interlead flash. Interlead flash shall not exceed 0.25 mm per side.
5. Reference JEDEC registration MO-187.

PowerPAD is a trademark of Texas Instruments.
A  20
DETAIL A
TYPICAL
SCALE  4.000
```

### Page 41

#### Raw extracted text

```text
www.ti.com
EXAMPLE BOARD LAYOUT
0.05 MAX
ALL AROUND
0.05 MIN
ALL AROUND
8X (1.4)
8X (0.45)
6X (0.65)
(4.4)
(R0.05) TYP
VSSOP - 1.1 mm max heightDGK0008A
SMALL OUTLINE PACKAGE
4214862/A   04/2023
NOTES: (continued)

  6. Publication IPC-7351 may have alternate designs.
  7. Solder mask tolerances between and around signal pads can vary based on board fabrication site.
  8. Vias are optional depending on application, refer to device data sheet. If any vias are implemented, refer to their locations shown
      on this view. It is recommended that vias under paste be filled, plugged or tented.
  9. Size of metal pad may vary due to creepage requirement.

TM
LAND PATTERN EXAMPLE
EXPOSED METAL SHOWN
SCALE: 15X
SYMM
SYMM
1
4
5
8
SEE DETAILS
15.000
METALSOLDER MASK
OPENING
METAL UNDER
SOLDER MASK
SOLDER MASK
OPENING
EXPOSED METALEXPOSED METAL
SOLDER MASK DETAILS
NON-SOLDER MASK
DEFINED
(PREFERRED)
SOLDER MASK
DEFINED
```

### Page 42

#### Raw extracted text

```text
www.ti.com
EXAMPLE STENCIL DESIGN
8X (1.4)
8X (0.45)
6X (0.65)
(4.4)
(R0.05) TYP
VSSOP - 1.1 mm max heightDGK0008A
SMALL OUTLINE PACKAGE
4214862/A   04/2023
NOTES: (continued)

11. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
      design recommendations.
12. Board assembly site may have different recommendations for stencil design.

TM
SOLDER PASTE EXAMPLE
 SCALE: 15X
SYMM
SYMM
1
4
5
8
```

### Page 43

#### Raw extracted text

```text
www.ti.com
GENERIC PACKAGE VIEW
This image is a representation of the package family, actual package may vary.
Refer to the product data sheet for package details.
PowerPAD    HVSSOP - 1.1 mm max heightDGN 8
SMALL OUTLINE PACKAGE3 x 3, 0.65 mm pitch
4225482/B
TM
```

### Page 44

#### Extracted tables

Table 1:

```text
| 0.1 | C
```

Table 2:

```text
C | A | B
```

#### Raw extracted text

```text
www.ti.com
PACKAGE OUTLINE
C
6X 0.65
2X
1.95
8X 0.37
0.26
5.05
4.75 TYP
SEATING
PLANE
0.15
0.05
0.25
GAGE PLANE
0 -8
1.1 MAX
0.23
0.13
1.60
1.34
1.92
1.66
B 3.1
2.9
NOTE 4
A
3.1
2.9
NOTE 3
0.7
0.4
HVSSOP - 1.1 mm max heightDGN0008C
SMALL OUTLINE PACKAGE
4218838/A   11/2017
1
4
5
8
0.1 C A B
PIN 1 INDEX AREA
SEE DETAIL  A
0.1 C
NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
    per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. This dimension does not include mold flash, protrusions, or gate burrs. Mold flash, protrusions, or gate burrs shall not
    exceed 0.15 mm per side.
4. This dimension does not include interlead flash. Interlead flash shall not exceed 0.25 mm per side.
5. Reference JEDEC registration MO-187.

A  20
DETAIL A
TYPICAL
SCALE  4.000
EXPOSED THERMAL PAD
1
4
5
8
9
```

### Page 45

#### Raw extracted text

```text
www.ti.com
EXAMPLE BOARD LAYOUT
0.05 MAX
ALL AROUND
0.05 MIN
ALL AROUND
8X (1.4)
8X (0.45)
6X (0.65)
(4.4)
(R0.05) TYP
(2)
NOTE 9
(3)
NOTE 9
(1.1)
(0.55)
( 0.2) TYP
VIA
(1.6)
(1.92)
HVSSOP - 1.1 mm max heightDGN0008C
SMALL OUTLINE PACKAGE
4218838/A   11/2017
NOTES: (continued)

6. Publication IPC-7351 may have alternate designs.
7. Solder mask tolerances between and around signal pads can vary based on board fabrication site.
8. Vias are optional depending on application, refer to device data sheet. If any vias are implemented, refer to their locations shown
    on this view. It is recommended that vias under paste be filled, plugged or tented.
9. Size of metal pad may vary due to creepage requirement.

LAND PATTERN EXAMPLE
EXPOSED METAL SHOWN
SCALE: 15X
SYMM
SYMM
1
4 5
8
SOLDER MASK
DEFINED PAD
METAL COVERED
BY SOLDER MASK
SEE DETAILS
9
15.000
METALSOLDER MASK
OPENING
METAL UNDER
SOLDER MASK
SOLDER MASK
OPENING
EXPOSED METALEXPOSED METAL
SOLDER MASK DETAILS
NON-SOLDER MASK
DEFINED
(PREFERRED)
SOLDER MASK
DEFINED
```

### Page 46

#### Extracted tables

Table 1:

```text
STENCIL THICKNESS | SOLDER STENCIL OPENING
0.1 | 1.79 X 2.15
0.125 | 1.60 X 1.92 (SHOWN)
0.15 | 1.46 X 1.75
0.175 | 1.35 X 1.62
```

#### Raw extracted text

```text
www.ti.com
EXAMPLE STENCIL DESIGN
8X (1.4)
8X (0.45)
6X (0.65)
(4.4)
(R0.05) TYP
(1.6)
BASED ON
0.125 THICK
STENCIL
(1.92)
BASED ON
0.125 THICK
STENCIL
HVSSOP - 1.1 mm max heightDGN0008C
SMALL OUTLINE PACKAGE
4218838/A   11/2017
1.35 X 1.620.175
1.46 X 1.750.15
1.60 X 1.92 (SHOWN)0.125
1.79 X 2.150.1
SOLDER STENCIL
OPENING
STENCIL
THICKNESS
NOTES: (continued)

10. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
      design recommendations.
11. Board assembly site may have different recommendations for stencil design.

SOLDER PASTE EXAMPLE
EXPOSED PAD 9:
100% PRINTED SOLDER COVERAGE BY AREA
SCALE: 15X
SYMM
SYMM
1
4 5
8
METAL COVERED
BY SOLDER MASK
SEE TABLE FOR
DIFFERENT OPENINGS
FOR OTHER STENCIL
THICKNESSES
```

### Page 47

#### Extracted tables

Table 1:

```text
0 | .1 | C
```

Table 2:

```text
| 0.13 | C | A | B
```

#### Raw extracted text

```text
www.ti.com
PACKAGE OUTLINE
C
6X 0.65
2X
1.95
8X 0.38
0.25
5.05
4.75 TYP
SEATING
PLANE
0.15
0.05
0.25
GAGE PLANE
0 -8
1.1 MAX
0.23
0.13
1.846
1.646
2.15
1.95
B 3.1
2.9
NOTE 4
A
3.1
2.9
NOTE 3
0.7
0.4
PowerPAD    HVSSOP - 1.1 mm max heightDGN0008G
SMALL OUTLINE PACKAGE
4225480/C   11/2024
1
4
5
8
0.13 C A B
PIN 1 INDEX AREA
SEE DETAIL  A
0.1 C
NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
    per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. This dimension does not include mold flash, protrusions, or gate burrs. Mold flash, protrusions, or gate burrs shall not
    exceed 0.15 mm per side.
4. This dimension does not include interlead flash. Interlead flash shall not exceed 0.25 mm per side.
5. Reference JEDEC registration MO-187.

PowerPAD is a trademark of Texas Instruments.
TM
A  20
DETAIL A
TYPICAL
SCALE  4.000
EXPOSED THERMAL PAD
1
4
5
8
9
```

### Page 48

#### Raw extracted text

```text
www.ti.com
EXAMPLE BOARD LAYOUT
0.05 MAX
ALL AROUND
0.05 MIN
ALL AROUND
8X (1.4)
8X (0.45)
6X (0.65)
(4.4)
(R0.05) TYP
(2)
NOTE 9
(3)
NOTE 9
(1.22)
(0.55)
( 0.2) TYP
VIA
(1.57)
(1.89)
PowerPAD    HVSSOP - 1.1 mm max heightDGN0008G
SMALL OUTLINE PACKAGE
4225480/C   11/2024
NOTES: (continued)

6. Publication IPC-7351 may have alternate designs.
7. Solder mask tolerances between and around signal pads can vary based on board fabrication site.
8. Vias are optional depending on application, refer to device data sheet. If any vias are implemented, refer to their locations shown
    on this view. It is recommended that vias under paste be filled, plugged or tented.
9. Size of metal pad may vary due to creepage requirement.

TM
LAND PATTERN EXAMPLE
EXPOSED METAL SHOWN
SCALE: 15X
SYMM
SYMM
1
4
5
8
SOLDER MASK
DEFINED PAD
METAL COVERED
BY SOLDER MASK
SEE DETAILS
9
15.000
METALSOLDER MASK
OPENING
METAL UNDER
SOLDER MASK
SOLDER MASK
OPENING
EXPOSED METALEXPOSED METAL
SOLDER MASK DETAILS
NON-SOLDER MASK
DEFINED
(PREFERRED)
SOLDER MASK
DEFINED
```

### Page 49

#### Extracted tables

Table 1:

```text
STENCIL THICKNESS | SOLDER STENCIL OPENING
0.1 | 1.76 X 2.11
0.125 | 1.57 X 1.89 (SHOWN)
0.15 | 1.43 X 1.73
0.175 | 1.33 X 1.60
```

#### Raw extracted text

```text
www.ti.com
EXAMPLE STENCIL DESIGN
8X (1.4)
8X (0.45)
6X (0.65)
(4.4)
(R0.05) TYP
(1.57)
BASED ON
0.125 THICK
STENCIL
(1.89)
BASED ON
0.125 THICK
STENCIL
PowerPAD    HVSSOP - 1.1 mm max heightDGN0008G
SMALL OUTLINE PACKAGE
4225480/C   11/2024
1.33 X 1.600.175
1.43 X 1.730.15
1.57 X 1.89 (SHOWN)0.125
1.76 X 2.110.1
SOLDER STENCIL
OPENING
STENCIL
THICKNESS
NOTES: (continued)

10. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
      design recommendations.
11. Board assembly site may have different recommendations for stencil design.

TM
SOLDER PASTE EXAMPLE
EXPOSED PAD 9:
100% PRINTED SOLDER COVERAGE BY AREA
SCALE: 15X
SYMM
SYMM
1
4 5
8
METAL COVERED
BY SOLDER MASK
SEE TABLE FOR
DIFFERENT OPENINGS
FOR OTHER STENCIL
THICKNESSES
```

### Page 50

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
