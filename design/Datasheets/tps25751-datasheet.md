# TPS25751 USB Type-C(R) and USB PD Controller with Integrated Power Switches Optimized for Power Applications datasheet (Rev. A)

## Source

- Source PDF: [tps25751-datasheet.pdf](tps25751-datasheet.pdf)
- Generated Markdown: `tps25751-datasheet.md`
- Page count: 87
- Conversion method: automated local extraction with pypdf and pdfplumber

## Extracted title and part identity

- TPS25751 USB Type-C(R) and USB PD Controller with Integrated Power Switches Optimized for Power Applications datasheet (Rev. A)
- tps25751 datasheet
- TPS25751
- TPS25751D
- TPS25751S
- SLVSH93A
- PD3.1
- BQ25756

## Extraction summary

- Pages with substantial text extraction: 87/87
- Pages with extracted tables: 52/87
- Total extracted character count: 191237
- Extraction quality flag: usable

## PDF metadata

| Field | Value |
| --- | --- |
| Title | TPS25751 USB Type-C(R) and USB PD Controller with Integrated Power Switches Optimized for Power Applications datasheet (Rev. A) |
| Author | Texas Instruments, Incorporated [SLVSH93,A ] |
| Subject | Data Sheet |
| Creator | AH XSL Formatter V7.2 MR7 for Windows (x64) : 7.2.8.57525 (2022-08-18T17:06+09) |
| Producer | iText 2.1.7 by 1T3XT |

## Design-relevant extracted content

This section surfaces design-relevant snippets first. Full page-by-page raw extraction follows later for local search.

### Part number and ordering information

- Supports PPS source & sink / associated with competitive USB PD solutions. / Standalone PPS source control TI battery / chargers Package Information / Programmable interface for PPS sink PART NUMBER PACKAGE(1) PACKAGE SIZE(2) / * Liquid Detection / TPS25751D QFN (REF) 4.0mm x 6.0mm
- associated with competitive USB PD solutions. / Standalone PPS source control TI battery / chargers Package Information / Programmable interface for PPS sink PART NUMBER PACKAGE(1) PACKAGE SIZE(2) / * Liquid Detection / TPS25751D QFN (REF) 4.0mm x 6.0mm / Measures directly at the Type-C connector
- Measures directly at the Type-C connector / TPS25751S QFN (RSM) 4.0mm x 4.0mm / Integrated error handling and protection / * Integrated fully managed power paths (1) For all available packages, see the orderable addendum at / the end of the data sheet. / Integrated 5V, 3A, 36mOhm sourcing switch / (2) The package size (length x width) is a nominal value and
- 10.6 Electrostatic Discharge Caution..............................74 / 10.7 Glossary..................................................................74 / 11 Revision History.......................................................... 75 / 12 Mechanical, Packaging, and Orderable / Information.................................................................... 75 / TPS25751 / SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
- and loading any code patches into volatile memory in the digital core. For a high-level block diagram of the / digital core, a description of its features, and more detailed circuitry, see Digital Core. / The TPS25751 has one I2C controller to write to and read from external target devices such as a battery charger / or an optional external EEPROM memory (see I2C Interface). / The TPS25751 also integrates a thermal shutdown mechanism and runs off of accurate clocks provided by the / integrated oscillator. / 8.2 Functional Block Diagram
- supplied when VIN_3V3 is low (that is the dead-battery scenario). The ADCINx pins must be externally tied to / the LDO_3V3 pin via a resistive divider as shown in the following figure. At power-up the ADC converts the / ADCINx voltage and the digital core uses these two values to determine start-up behavior. The available start-up / configurations include options for I 2C target address of I2Ct_SCL/SDA, sink path control in dead-battery, and / default configuration. / ADC Mux and / Dividers
- GPIO5 I/O D-, general-purpose input or output, or LD2 for Liquid Detection / GPIO6 I/O General-purpose input or output / GPIO7 I/O General-purpose input or output / I2Ct_IRQ(GPIO10) O IRQ for optional I2Ct, or used as a general-purpose output / GPIO11 O General-purpose output / I2Cc_IRQ(GPIO12) I IRQ for I2Cc, or used as a general-purpose input / 8.3.9.2 I2C Interface
- GPIO5 | I/O | D-, general-purpose input or output, or LD2 for Liquid Detection / GPIO6 | I/O | General-purpose input or output / GPIO7 | I/O | General-purpose input or output / I2Ct_IRQ(GPIO10) | O | IRQ for optional I2Ct, or used as a general-purpose output / GPIO11 | O | General-purpose output / I2Cc_IRQ(GPIO12) | I | IRQ for I2Cc, or used as a general-purpose input / TPS25751
- EEPROM with a 7-bit target address of 0x50. The EEPROM must be at least 36 kilo-bytes. / Table 8-4. I2C Summary / I2C BUS TYPE TYPICAL USAGE / I2Ct Target Optionally can be connected to an external MCU. Also used to load the patch and application / configuration. / I2Cc Controller Connect to a I2C EEPROM, Battery Charger. Use the LDO_3V3 pin as the pullup voltage. Multi / controller configuration is not supported.
- 42 Submit Document Feedback Copyright 2024 Texas Instruments Incorporated / Product Folder Links: TPS25751 / I2C BUS | TYPE | TYPICAL USAGE / I2Ct | Target | Optionally can be connected to an external MCU. Also used to load the patch and application configuration. / I2Cc | Controller | Connect to a I2C EEPROM, Battery Charger. Use the LDO_3V3 pin as the pullup voltage. Multi- controller configuration is not supported. / S / P
- the 'APP ' mode, enable USB PD PHY and negotiate a contract / for the highest power contract that is offered up to 20 V. The / configuration cannot be used when a patch is loaded from / EEPROM. This option is not recommended for systems that can / boot from 5 V. This configuration is not valid to use with any / supported battery chargers. / 3 3 #2
- 5 | 5 | #2 | / 2 | 0 | #3 | / 1 | 7 | #4 | / 7 | 3 | #1 | NegotiateHighVoltage: The device always enables the sink path during the initial implicit contract regardless of the amount of current the attached source is offering. The PD controller enters the 'APP ' mode, enable USB PD PHY and negotiate a contract for the highest power contract that is offered up to 20 V. The configuration cannot be used when a patch is loaded from EEPROM. This option is not recommended for systems that can boot from 5 V. This configuration is not valid to use with any supported battery chargers. / 3 | 3 | #2 | / 4 | 0 | #3 | / 3 | 7 | #4 |
- An external EEPROM is required to download a pre-configured firmware on the TPS25751 device through the / I2C interface. / The TPS25751 firmware can be configured using the Web Tool for the application-specific PD charging / architecture requirements and data roles. The tool also provides additional optional firmware configuration that / integrates control for select Battery Charger Products (BQ). The TPS25751 I2C controller interfaces with the / Battery Chargers with pre-configured GPIO settings and I2C controller events. The Application Customization / Tool available with the TPS25751 provides details of the supported Battery Charger Products (BQ).
- guidelines are followed. Best practice is to consult with board manufacturing to verify manufacturing capabilities. / 9.4.1.1.1 Recommended Via Size / Proper via stitching is recommended to carrying current for the VBUS power paths and grounding. The / recommended minimum via size is shown below, but larger vias are an option for low density PCB designs. / A single via is capable of carrying 1A, verify the tolerance with the board manufacturing. Vias are recommended / to be tented when located close to the PD controller. / 16mil8mil
- guidelines are followed. Best practice is to consult with board manufacturing to verify manufacturing capabilities. / 9.4.2.1.1 Recommended Via Size / Proper via stitching is recommended to carrying current for the VBUS power paths and grounding. The / recommended minimum via size is shown below, but larger vias are an option for low density PCB designs. / A single via is capable of carrying 1A, verify the tolerance with the board manufacturing. Vias are recommended / to be tented when located close to the PD controller. / 8mil 16mil
- NOTE: Page numbers for previous revisions may differ from page numbers in the current version. / Changes from Revision * (October 2023) to Revision A (March 2024) Page / * Changed data sheet status from "Advance Information" to "Production Data".................................................. 1 / 12 Mechanical, Packaging, and Orderable Information / The following pages include mechanical, packaging, and orderable information. This information is the most / current data available for the designated devices. This data is subject to change without notice and revision of / this document. For browser-based versions of this data sheet, refer to the left-hand navigation.
- Changes from Revision * (October 2023) to Revision A (March 2024) Page / * Changed data sheet status from "Advance Information" to "Production Data".................................................. 1 / 12 Mechanical, Packaging, and Orderable Information / The following pages include mechanical, packaging, and orderable information. This information is the most / current data available for the designated devices. This data is subject to change without notice and revision of / this document. For browser-based versions of this data sheet, refer to the left-hand navigation. / www.ti.com
- SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024 / Copyright 2024 Texas Instruments Incorporated Submit Document Feedback 75 / Product Folder Links: TPS25751 / PACKAGE OPTION ADDENDUM / www.ti.com 6-Feb-2026 / PACKAGING INFORMATION / Orderable part number Status

### Pin, pad, and terminal designations

- Integrated 5V, 3A, 36mOhm sourcing switch / (2) The package size (length x width) is a nominal value and / (TPS25751S and TPS25751D) / includes pins, where applicable. / Integrated 20V, 5A, 16mOhm bi-directional load / switch (TPS25751D only) 5A / 5-20 V
- 10 GPIO / protection for the 5V/3A source power path / 5-20 V / 26V tolerant CC pins for robust protection when / connected to non-compliant devices PP_EXT / Control / 3.3V LDO
- 2 Applications.....................................................................1 / 3 Description.......................................................................1 / 4 Device Comparison Table...............................................3 / 5 Pin Configuration and Functions...................................4 / 6 Specifications.................................................................. 7 / 6.1 Absolute Maximum Ratings........................................ 7 / 6.2 ESD Ratings............................................................... 8
- 6.14 CC PHY Parameters...............................................16 / 6.15 Thermal Shutdown Characteristics.........................17 / 6.16 ADC Characteristics................................................17 / 6.17 Input/Output (I/O) Characteristics........................... 17 / 6.18 BC1.2 Characteristics............................................. 18 / 6.19 I2C Requirements and Characteristics................... 18 / 6.20 Typical Characteristics ...........................................20
- 7 Parameter Measurement Information..........................22 / 8 Detailed Description......................................................23 / 8.1 Overview...................................................................23 / 8.2 Functional Block Diagram.........................................23 / 8.3 Feature Description...................................................26 / 8.4 Device Functional Modes..........................................44 / 8.5 Thermal Shutdown....................................................46
- 8.1 Overview...................................................................23 / 8.2 Functional Block Diagram.........................................23 / 8.3 Feature Description...................................................26 / 8.4 Device Functional Modes..........................................44 / 8.5 Thermal Shutdown....................................................46 / 9 Application and Implementation..................................47 / 9.1 Application Information............................................. 47
- DEVICE NUMBER | 5-V SOURCE LOAD SWITCH | INTEGRATED HIGH VOLTAGE BI-DIRECTIONAL LOAD SWITCH (PPHV) | HIGH VOLTAGE GATE DRIVER FOR BI-DIRECTIONAL EXTERNAL PATH (PP_EXT) / TPS25751D | Yes | Yes | No / TPS25751S | Yes | No | Yes / 5 Pin Configuration and Functions / 37 36 35 34 33 32 31 30 29 28 27 / ADCIN1 / PPHV
- LDO_3V3 1 25 / 2 24 / ADCIN2 3 23 / Thermal Pad Thermal Pad / (GND) (DRAIN) / LDO_1V5 4 22 / GPIO0 5 21
- LD1 / GPIO4/USB_P/ / Not to Scale / Figure 5-1. Top View of the TPS25751D 38-pin QFN Package / 3V3_NIV / LCS_tC2I / 6OIPG
- ADCIN2 3 22 GPIO4/USB_P/LD1 / Thermal / LDO_1V5 4 21 GATE_VBUS / Pad / GPIO0 5 (GND) 20 GATE_VSYS / GPIO1 6 19 VSYS / GPIO2 7 18 GPIO3
- 61 / TPS25751 / SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024 www.ti.com / Figure 5-2. Top View of the TPS25751S 32-pin QFN Package / 4 Submit Document Feedback Copyright 2024 Texas Instruments Incorporated / Product Folder Links: TPS25751 / TPS25751
- Product Folder Links: TPS25751 / TPS25751 / www.ti.com SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024 / Table 5-1. TPS25751D Pin Functions / PIN / TYPE(1) RESET DESCRIPTION / NAME NO.
- TPS25751 / www.ti.com SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024 / Table 5-1. TPS25751D Pin Functions / PIN / TYPE(1) RESET DESCRIPTION / NAME NO. / ADCIN1 2 I Hi-Z Configuration Input. Connect to a resistor divider to LDO_3V3.
- NAME NO. / ADCIN1 2 I Hi-Z Configuration Input. Connect to a resistor divider to LDO_3V3. / ADCIN2 3 I Hi-Z Configuration Input. Connect to a resistor divider to LDO_3V3. / I/O for USB Type-C. Filter noise with recommended capacitor to GND / CC1 28 I/O Hi-Z / (CCCy). / I/O for USB Type-C. Filter noise with recommended capacitor to GND
- ADCIN1 2 I Hi-Z Configuration Input. Connect to a resistor divider to LDO_3V3. / ADCIN2 3 I Hi-Z Configuration Input. Connect to a resistor divider to LDO_3V3. / I/O for USB Type-C. Filter noise with recommended capacitor to GND / CC1 28 I/O Hi-Z / (CCCy). / I/O for USB Type-C. Filter noise with recommended capacitor to GND / CC2 29 I/O Hi-Z
- I/O for USB Type-C. Filter noise with recommended capacitor to GND / CC1 28 I/O Hi-Z / (CCCy). / I/O for USB Type-C. Filter noise with recommended capacitor to GND / CC2 29 I/O Hi-Z / (CCCy). / GND 11, 12, 14, 31 - - Ground. Connect to ground plane.
- CC1 28 I/O Hi-Z / (CCCy). / I/O for USB Type-C. Filter noise with recommended capacitor to GND / CC2 29 I/O Hi-Z / (CCCy). / GND 11, 12, 14, 31 - - Ground. Connect to ground plane. / GPIO0 5 GPIO Hi-Z General purpose digital I/O. Tie to ground when pin is unused.
- CC2 29 I/O Hi-Z / (CCCy). / GND 11, 12, 14, 31 - - Ground. Connect to ground plane. / GPIO0 5 GPIO Hi-Z General purpose digital I/O. Tie to ground when pin is unused. / GPIO1 6 GPIO Hi-Z General purpose digital I/O. Tie to ground when pin is unused. / GPIO2 7 GPIO Hi-Z General purpose digital I/O. Tie to ground when pin is unused. / GPIO3 19 GPIO Hi-Z General purpose digital I/O. Tie to ground when pin is unused.

### Specifications, ratings, and operating conditions

- 5-20 V / * Integrated robust power path protection / 3.3V LDO / Integrated reverse current protection, TPS25751D / undervoltage protection, overvoltage protection, 5 V 3A VBUS / 3.3V / and slew rate control the high-voltage bi- Ty V p C e- O C m N R N a p c s / h R w in d it e c & , h s e t s a , t e CC1/2 2 C VC C ONN
- * Integrated robust power path protection / 3.3V LDO / Integrated reverse current protection, TPS25751D / undervoltage protection, overvoltage protection, 5 V 3A VBUS / 3.3V / and slew rate control the high-voltage bi- Ty V p C e- O C m N R N a p c s / h R w in d it e c & , h s e t s a , t e CC1/2 2 C VC C ONN / directional power path E C O m o p b n t e t i r o d o n d ll a e e l r d Ta I2 rg C e t U p S ro B t o P c D o l p l a a o y n li e d c r y p h e y n s g i i c n a e l ,
- Integrated reverse current protection, TPS25751D / undervoltage protection, overvoltage protection, 5 V 3A VBUS / 3.3V / and slew rate control the high-voltage bi- Ty V p C e- O C m N R N a p c s / h R w in d it e c & , h s e t s a , t e CC1/2 2 C VC C ONN / directional power path E C O m o p b n t e t i r o d o n d ll a e e l r d Ta I2 rg C e t U p S ro B t o P c D o l p l a a o y n li e d c r y p h e y n s g i i c n a e l , / Integrated undervoltage and overvoltage / BQ Battery I2C GND
- 3.3V / and slew rate control the high-voltage bi- Ty V p C e- O C m N R N a p c s / h R w in d it e c & , h s e t s a , t e CC1/2 2 C VC C ONN / directional power path E C O m o p b n t e t i r o d o n d ll a e e l r d Ta I2 rg C e t U p S ro B t o P c D o l p l a a o y n li e d c r y p h e y n s g i i c n a e l , / Integrated undervoltage and overvoltage / BQ Battery I2C GND / protection and current limiting for inrush current Charger Controller / 10 GPIO
- directional power path E C O m o p b n t e t i r o d o n d ll a e e l r d Ta I2 rg C e t U p S ro B t o P c D o l p l a a o y n li e d c r y p h e y n s g i i c n a e l , / Integrated undervoltage and overvoltage / BQ Battery I2C GND / protection and current limiting for inrush current Charger Controller / 10 GPIO / protection for the 5V/3A source power path / 5-20 V
- 3 Description.......................................................................1 / 4 Device Comparison Table...............................................3 / 5 Pin Configuration and Functions...................................4 / 6 Specifications.................................................................. 7 / 6.1 Absolute Maximum Ratings........................................ 7 / 6.2 ESD Ratings............................................................... 8 / 6.3 Recommended Operating Conditions.........................8
- 4 Device Comparison Table...............................................3 / 5 Pin Configuration and Functions...................................4 / 6 Specifications.................................................................. 7 / 6.1 Absolute Maximum Ratings........................................ 7 / 6.2 ESD Ratings............................................................... 8 / 6.3 Recommended Operating Conditions.........................8 / 6.4 Recommended Capacitance.......................................9
- 5 Pin Configuration and Functions...................................4 / 6 Specifications.................................................................. 7 / 6.1 Absolute Maximum Ratings........................................ 7 / 6.2 ESD Ratings............................................................... 8 / 6.3 Recommended Operating Conditions.........................8 / 6.4 Recommended Capacitance.......................................9 / 6.5 Thermal Information..................................................10
- 6 Specifications.................................................................. 7 / 6.1 Absolute Maximum Ratings........................................ 7 / 6.2 ESD Ratings............................................................... 8 / 6.3 Recommended Operating Conditions.........................8 / 6.4 Recommended Capacitance.......................................9 / 6.5 Thermal Information..................................................10 / 6.6 Power Supply Characteristics................................... 11
- 6.2 ESD Ratings............................................................... 8 / 6.3 Recommended Operating Conditions.........................8 / 6.4 Recommended Capacitance.......................................9 / 6.5 Thermal Information..................................................10 / 6.6 Power Supply Characteristics................................... 11 / 6.7 Power Consumption..................................................11 / 6.8 PP_5V Power Switch Characteristics....................... 11
- 6.12 CC Cable Detection Parameters.............................14 / 6.13 CC VCONN Parameters......................................... 15 / 6.14 CC PHY Parameters...............................................16 / 6.15 Thermal Shutdown Characteristics.........................17 / 6.16 ADC Characteristics................................................17 / 6.17 Input/Output (I/O) Characteristics........................... 17 / 6.18 BC1.2 Characteristics............................................. 18
- 6.13 CC VCONN Parameters......................................... 15 / 6.14 CC PHY Parameters...............................................16 / 6.15 Thermal Shutdown Characteristics.........................17 / 6.16 ADC Characteristics................................................17 / 6.17 Input/Output (I/O) Characteristics........................... 17 / 6.18 BC1.2 Characteristics............................................. 18 / 6.19 I2C Requirements and Characteristics................... 18
- 8.2 Functional Block Diagram.........................................23 / 8.3 Feature Description...................................................26 / 8.4 Device Functional Modes..........................................44 / 8.5 Thermal Shutdown....................................................46 / 9 Application and Implementation..................................47 / 9.1 Application Information............................................. 47 / 9.2 Typical Application.................................................... 47
- 4 Device Comparison Table / DEVICE NUMBER 5-V SOURCE LOAD SWITCH / INTEGRATED HIGH / VOLTAGE BI-DIRECTIONAL / LOAD SWITCH (PPHV) / HIGH VOLTAGE GATE DRIVER / FOR BI-DIRECTIONAL EXTERNAL
- INTEGRATED HIGH / VOLTAGE BI-DIRECTIONAL / LOAD SWITCH (PPHV) / HIGH VOLTAGE GATE DRIVER / FOR BI-DIRECTIONAL EXTERNAL / PATH (PP_EXT) / TPS25751D Yes Yes No
- SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024 / Copyright 2024 Texas Instruments Incorporated Submit Document Feedback 3 / Product Folder Links: TPS25751 / DEVICE NUMBER | 5-V SOURCE LOAD SWITCH | INTEGRATED HIGH VOLTAGE BI-DIRECTIONAL LOAD SWITCH (PPHV) | HIGH VOLTAGE GATE DRIVER FOR BI-DIRECTIONAL EXTERNAL PATH (PP_EXT) / TPS25751D | Yes | Yes | No / TPS25751S | Yes | No | Yes / 5 Pin Configuration and Functions
- LDO_3V3 1 25 / 2 24 / ADCIN2 3 23 / Thermal Pad Thermal Pad / (GND) (DRAIN) / LDO_1V5 4 22 / GPIO0 5 21
- LDO_3V3 1 24 CC1 / ADCIN1 2 23 GPIO5/USB_N/LD2 / ADCIN2 3 22 GPIO4/USB_P/LD1 / Thermal / LDO_1V5 4 21 GATE_VBUS / Pad / GPIO0 5 (GND) 20 GATE_VSYS

### Dimensions, package, and mechanical information

- Supports PPS source & sink / associated with competitive USB PD solutions. / Standalone PPS source control TI battery / chargers Package Information / Programmable interface for PPS sink PART NUMBER PACKAGE(1) PACKAGE SIZE(2) / * Liquid Detection / TPS25751D QFN (REF) 4.0mm x 6.0mm
- associated with competitive USB PD solutions. / Standalone PPS source control TI battery / chargers Package Information / Programmable interface for PPS sink PART NUMBER PACKAGE(1) PACKAGE SIZE(2) / * Liquid Detection / TPS25751D QFN (REF) 4.0mm x 6.0mm / Measures directly at the Type-C connector
- Measures directly at the Type-C connector / TPS25751S QFN (RSM) 4.0mm x 4.0mm / Integrated error handling and protection / * Integrated fully managed power paths (1) For all available packages, see the orderable addendum at / the end of the data sheet. / Integrated 5V, 3A, 36mOhm sourcing switch / (2) The package size (length x width) is a nominal value and
- * Integrated fully managed power paths (1) For all available packages, see the orderable addendum at / the end of the data sheet. / Integrated 5V, 3A, 36mOhm sourcing switch / (2) The package size (length x width) is a nominal value and / (TPS25751S and TPS25751D) / includes pins, where applicable. / Integrated 20V, 5A, 16mOhm bi-directional load
- 1 I2C target port 10 GPIO / An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications, / intellectual property matters and other important disclaimers. PRODUCTION DATA. / PART NUMB | ER PACKAGE(1) | PACKAGE SIZE(2) / TPS25751D | QFN (REF) | 4.0mm x 6.0mm / TPS25751S | QFN (RSM) | 4.0mm x 4.0mm / A
- 10.6 Electrostatic Discharge Caution..............................74 / 10.7 Glossary..................................................................74 / 11 Revision History.......................................................... 75 / 12 Mechanical, Packaging, and Orderable / Information.................................................................... 75 / TPS25751 / SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
- LD1 / GPIO4/USB_P/ / Not to Scale / Figure 5-1. Top View of the TPS25751D 38-pin QFN Package / 3V3_NIV / LCS_tC2I / 6OIPG
- 61 / TPS25751 / SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024 www.ti.com / Figure 5-2. Top View of the TPS25751S 32-pin QFN Package / 4 Submit Document Feedback Copyright 2024 Texas Instruments Incorporated / Product Folder Links: TPS25751 / TPS25751
- Junction-to-case (bottom DRAIN pad) / R (bot_DRAIN) 4.6 deg C/W / JC thermal resistance / (1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application / report. / 6.5.2 TPS25751S - Thermal Information / TPS25751S
- Junction-to-board characterization / 9.7 deg C/W / JB parameter / (1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application / report. / 10 Submit Document Feedback Copyright 2024 Texas Instruments Incorporated / Product Folder Links: TPS25751
- NOTE: Page numbers for previous revisions may differ from page numbers in the current version. / Changes from Revision * (October 2023) to Revision A (March 2024) Page / * Changed data sheet status from "Advance Information" to "Production Data".................................................. 1 / 12 Mechanical, Packaging, and Orderable Information / The following pages include mechanical, packaging, and orderable information. This information is the most / current data available for the designated devices. This data is subject to change without notice and revision of / this document. For browser-based versions of this data sheet, refer to the left-hand navigation.
- Changes from Revision * (October 2023) to Revision A (March 2024) Page / * Changed data sheet status from "Advance Information" to "Production Data".................................................. 1 / 12 Mechanical, Packaging, and Orderable Information / The following pages include mechanical, packaging, and orderable information. This information is the most / current data available for the designated devices. This data is subject to change without notice and revision of / this document. For browser-based versions of this data sheet, refer to the left-hand navigation. / www.ti.com
- SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024 / Copyright 2024 Texas Instruments Incorporated Submit Document Feedback 75 / Product Folder Links: TPS25751 / PACKAGE OPTION ADDENDUM / www.ti.com 6-Feb-2026 / PACKAGING INFORMATION / Orderable part number Status
- (1) / Material type / (2) / Package | Pins Package qty | Carrier RoHS / (3) / Lead finish/ / Ball material
- and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers / and other limited information may not be available for release. / Addendum-Page 1 / Orderable part number | Status (1) | Material type (2) | Package | Pins | Package qty | Carrier | RoHS (3) | Lead finish/ Ball material (4) | MSL rating/ Peak reflow (5) | Op temp ( deg C) | Part marking (6) / TPS25751DREFR | Active | Production | WQFN (REF) | 38 | 3000 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | 25751D BG / TPS25751DREFR.A | Active | Production | WQFN (REF) | 38 | 3000 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | 25751D BG / TPS25751SRSMR | Active | Production | VQFN (RSM) | 32 | 3000 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | 25751S BG
- TPS25751SRSMR | Active | Production | VQFN (RSM) | 32 | 3000 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | 25751S BG / TPS25751SRSMR.A | Active | Production | VQFN (RSM) | 32 | 3000 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | 25751S BG / TPS25751SRSMR.B | Active | Production | VQFN (RSM) | 32 | 3000 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | 25751S BG / PACKAGE OPTION ADDENDUM / www.ti.com 6-Feb-2026 / In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.
- In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis. / Addendum-Page 2 / PACKAGE MATERIALS INFORMATION / www.ti.com 2-May-2024 / TAPE AND REEL INFORMATION / REEL DIMENSIONS TAPE DIMENSIONS
- PACKAGE MATERIALS INFORMATION / www.ti.com 2-May-2024 / TAPE AND REEL INFORMATION / REEL DIMENSIONS TAPE DIMENSIONS / K0 P1 / W / B0

### Formulas, equations, and configuration calculations

- getting started information, please refer to / and simple multiple-choice questions. As a result, / www.ti.com/usb-c and E2E guide / the GUI creates the configuration image for the / * Programmable Power Supply (PPS) / users application, reducing much of the complexity / Supports PPS source & sink
- directional power path E C O m o p b n t e t i r o d o n d ll a e e l r d Ta I2 rg C e t U p S ro B t o P c D o l p l a a o y n li e d c r y p h e y n s g i i c n a e l , / Integrated undervoltage and overvoltage / BQ Battery I2C GND / protection and current limiting for inrush current Charger Controller / 10 GPIO / protection for the 5V/3A source power path / 5-20 V
- 2 Applications.....................................................................1 / 3 Description.......................................................................1 / 4 Device Comparison Table...............................................3 / 5 Pin Configuration and Functions...................................4 / 6 Specifications.................................................................. 7 / 6.1 Absolute Maximum Ratings........................................ 7 / 6.2 ESD Ratings............................................................... 8
- DEVICE NUMBER | 5-V SOURCE LOAD SWITCH | INTEGRATED HIGH VOLTAGE BI-DIRECTIONAL LOAD SWITCH (PPHV) | HIGH VOLTAGE GATE DRIVER FOR BI-DIRECTIONAL EXTERNAL PATH (PP_EXT) / TPS25751D | Yes | Yes | No / TPS25751S | Yes | No | Yes / 5 Pin Configuration and Functions / 37 36 35 34 33 32 31 30 29 28 27 / ADCIN1 / PPHV
- PIN / TYPE(1) RESET DESCRIPTION / NAME NO. / ADCIN1 2 I Hi-Z Configuration Input. Connect to a resistor divider to LDO_3V3. / ADCIN2 3 I Hi-Z Configuration Input. Connect to a resistor divider to LDO_3V3. / I/O for USB Type-C. Filter noise with recommended capacitor to GND / CC1 28 I/O Hi-Z
- TYPE(1) RESET DESCRIPTION / NAME NO. / ADCIN1 2 I Hi-Z Configuration Input. Connect to a resistor divider to LDO_3V3. / ADCIN2 3 I Hi-Z Configuration Input. Connect to a resistor divider to LDO_3V3. / I/O for USB Type-C. Filter noise with recommended capacitor to GND / CC1 28 I/O Hi-Z / (CCCy).
- Product Folder Links: TPS25751 / PIN | | TYPE(1) | RESET | DESCRIPTION / NAME | NO. | | | / ADCIN1 | 2 | I | Hi-Z | Configuration Input. Connect to a resistor divider to LDO_3V3. / ADCIN2 | 3 | I | Hi-Z | Configuration Input. Connect to a resistor divider to LDO_3V3. / CC1 | 28 | I/O | Hi-Z | I/O for USB Type-C. Filter noise with recommended capacitor to GND (CCCy). / CC2 | 29 | I/O | Hi-Z | I/O for USB Type-C. Filter noise with recommended capacitor to GND (CCCy).
- PIN | | TYPE(1) | RESET | DESCRIPTION / NAME | NO. | | | / ADCIN1 | 2 | I | Hi-Z | Configuration Input. Connect to a resistor divider to LDO_3V3. / ADCIN2 | 3 | I | Hi-Z | Configuration Input. Connect to a resistor divider to LDO_3V3. / CC1 | 28 | I/O | Hi-Z | I/O for USB Type-C. Filter noise with recommended capacitor to GND (CCCy). / CC2 | 29 | I/O | Hi-Z | I/O for USB Type-C. Filter noise with recommended capacitor to GND (CCCy). / GND | 11, 12, 14, 31 | | | Ground. Connect to ground plane.
- PIN / TYPE(1) RESET DESCRIPTION / NAME NO. / ADCIN1 2 I Hi-Z Configuration Input. Connect to a resistor divider to LDO_3V3. / ADCIN2 3 I Hi-Z Configuration Input. Connect to a resistor divider to LDO_3V3. / I/O for USB Type-C. Filter noise with recommended capacitor to GND / CC1 24 I/O Hi-Z
- TYPE(1) RESET DESCRIPTION / NAME NO. / ADCIN1 2 I Hi-Z Configuration Input. Connect to a resistor divider to LDO_3V3. / ADCIN2 3 I Hi-Z Configuration Input. Connect to a resistor divider to LDO_3V3. / I/O for USB Type-C. Filter noise with recommended capacitor to GND / CC1 24 I/O Hi-Z / (CCCy).
- Product Folder Links: TPS25751 / PIN | | TYPE(1) | RESET | DESCRIPTION / NAME | NO. | | | / ADCIN1 | 2 | I | Hi-Z | Configuration Input. Connect to a resistor divider to LDO_3V3. / ADCIN2 | 3 | I | Hi-Z | Configuration Input. Connect to a resistor divider to LDO_3V3. / CC1 | 24 | I/O | Hi-Z | I/O for USB Type-C. Filter noise with recommended capacitor to GND (CCCy). / CC2 | 25 | I/O | Hi-Z | I/O for USB Type-C. Filter noise with recommended capacitor to GND (CCCy).
- PIN | | TYPE(1) | RESET | DESCRIPTION / NAME | NO. | | | / ADCIN1 | 2 | I | Hi-Z | Configuration Input. Connect to a resistor divider to LDO_3V3. / ADCIN2 | 3 | I | Hi-Z | Configuration Input. Connect to a resistor divider to LDO_3V3. / CC1 | 24 | I/O | Hi-Z | I/O for USB Type-C. Filter noise with recommended capacitor to GND (CCCy). / CC2 | 25 | I/O | Hi-Z | I/O for USB Type-C. Filter noise with recommended capacitor to GND (CCCy). / GATE_VSYS | 20 | O | Hi-Z | Connect to the N-ch MOSFET that has source tied to VSYS.
- J / T Storage temperature -55 150 deg C / STG / (1) Operation outside the Absolute Maximum Ratings may cause permanent device damage. Absolute Maximum Ratings do not imply / functional operation of the device at these or any other conditions beyond those listed under Recommended Operating Conditions. / If used outside the Recommended Operating Conditions but within the Absolute Maximum Ratings, the device may not be fully / functional, and this may affect device reliability, functionality, performance, and shorten the device lifetime.
- T Storage temperature -55 150 deg C / STG / (1) Operation outside the Absolute Maximum Ratings may cause permanent device damage. Absolute Maximum Ratings do not imply / functional operation of the device at these or any other conditions beyond those listed under Recommended Operating Conditions. / If used outside the Recommended Operating Conditions but within the Absolute Maximum Ratings, the device may not be fully / functional, and this may affect device reliability, functionality, performance, and shorten the device lifetime. / (2) All voltage values are with respect to network GND. Connect the GND pin directly to the GND plane of the board.
- J_PPHV PP_HV switch -40 175 deg C / junction temperature / (1) All voltage values are with respect to network GND. Connect the GND pin directly to the GND plane of the board. / (2) Pulse duration <= 100 us and duty-cycle <= 1%. / 6.1.3 TPS25751S - Absolute Maximum Ratings / MIN MAX UNIT / Output voltage range 1 G G A A T T E E _ _ V V B S U YS S 2 , -0.3 40 V
- 50% at the required operating voltage, then the required external capacitor value is 10 uF. / (2) USB PD requirement (cSrcBulkShared). Keep at least 10 uF tied directly to PP5V. / (3) Capacitance includes all external capacitance to the Type-C receptacle. / (4) The device can be configured to quickly disable the sinking power path upon certain events. When such a configuration is used, a / capacitance on the higher side of the range is recommended. / (5) USB PD specification for cSnkBulkPd (100uF) is the maximum bulk capacitance allowed on a VBUS sink after a PD contract is in / place. The capacitance is sufficient for all power conversion devices deriving power from the PD Controller sink path. For systems
- capacitance on the higher side of the range is recommended. / (5) USB PD specification for cSnkBulkPd (100uF) is the maximum bulk capacitance allowed on a VBUS sink after a PD contract is in / place. The capacitance is sufficient for all power conversion devices deriving power from the PD Controller sink path. For systems / requiring greater than 100uF, VBUS surge current limiting is implemented as described in the USB3.2 specification. / Copyright 2024 Texas Instruments Incorporated Submit Document Feedback 9 / Product Folder Links: TPS25751 / | | MIN | MAX | UNIT
- PARAMETER TEST CONDITIONS MIN TYP MAX UNIT / VIN_3V3, VBUS / rising 3.6 3.9 / V VBUS UVLO threshold falling 3.5 3.8 V / VBUS_UVLO / hysteresis 0.1 / rising, V = 0 2.56 2.66 2.76

### Reference designs, applications, and examples

- TPS25751 / SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024 / TPS25751 USB Type-C(R) and USB PD Controller with Integrated Power Switches / Optimized for Power Applications / 1 Features 2 Applications / * PD Controller is certified by the USB-IF for PD3.1 * Power tools, power banks, retail and payment / PD3.1 silicon is required for certification of new * Wireless speakers, Cordless vacuum cleaner
- SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024 / TPS25751 USB Type-C(R) and USB PD Controller with Integrated Power Switches / Optimized for Power Applications / 1 Features 2 Applications / * PD Controller is certified by the USB-IF for PD3.1 * Power tools, power banks, retail and payment / PD3.1 silicon is required for certification of new * Wireless speakers, Cordless vacuum cleaner / USB PD designs * personal electronics and industrial applications
- 1 Features 2 Applications / * PD Controller is certified by the USB-IF for PD3.1 * Power tools, power banks, retail and payment / PD3.1 silicon is required for certification of new * Wireless speakers, Cordless vacuum cleaner / USB PD designs * personal electronics and industrial applications / TPS25751 TID#: 10306 * Home health care and Personal care and fitness / Article on PD2.0 vs. PD3.0 / 3 Description
- TPS25751 TID#: 10306 * Home health care and Personal care and fitness / Article on PD2.0 vs. PD3.0 / 3 Description / * Optimized for USB Type-C PD power applications / Integrated I2C control for TI battery chargers The TPS25751 is a highly integrated stand-alone USB / Type-C and Power Delivery (PD) controller optimized / * BQ25756, BQ25756E, BQ25790, BQ25792
- Integrated I2C control for TI battery chargers The TPS25751 is a highly integrated stand-alone USB / Type-C and Power Delivery (PD) controller optimized / * BQ25756, BQ25756E, BQ25790, BQ25792 / for applications supporting USB-C PD Power. The / * BQ25798, BQ25713, BQ25731 / TPS25751 integrates fully managed power paths / Web-based GUI and pre-configured firmware
- with robust protection for a complete USB-C PD / Optimized for power consumer only (sink) / solution. The TPS25751 also integrates control for / (UFP) applications / external battery charger ICs for added ease of / Optimized for power provider/power consumer / use and reduced time to market. The intuitive web
- external battery charger ICs for added ease of / Optimized for power provider/power consumer / use and reduced time to market. The intuitive web / (DRP) applications / based GUI asks the user a few simple questions on / For a more extensive selection guide and / the applications needs using clear block diagrams
- (DRP) applications / based GUI asks the user a few simple questions on / For a more extensive selection guide and / the applications needs using clear block diagrams / getting started information, please refer to / and simple multiple-choice questions. As a result, / www.ti.com/usb-c and E2E guide
- www.ti.com/usb-c and E2E guide / the GUI creates the configuration image for the / * Programmable Power Supply (PPS) / users application, reducing much of the complexity / Supports PPS source & sink / associated with competitive USB PD solutions. / Standalone PPS source control TI battery
- 1 I2C controller port BQ Battery I2C GND / Charger Controller / 1 I2C target port 10 GPIO / An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications, / intellectual property matters and other important disclaimers. PRODUCTION DATA. / PART NUMB | ER PACKAGE(1) | PACKAGE SIZE(2) / TPS25751D | QFN (REF) | 4.0mm x 6.0mm
- LDO TPS25751S 3A Type-C Rp/Rd & sta machine, VCONN switches, USB PD policy engin I2C protocol and physic Target layer I2C Controller 10 / Table of Contents / 1 Features............................................................................1 / 2 Applications.....................................................................1 / 3 Description.......................................................................1 / 4 Device Comparison Table...............................................3 / 5 Pin Configuration and Functions...................................4
- 8.3 Feature Description...................................................26 / 8.4 Device Functional Modes..........................................44 / 8.5 Thermal Shutdown....................................................46 / 9 Application and Implementation..................................47 / 9.1 Application Information............................................. 47 / 9.2 Typical Application.................................................... 47 / 9.3 Power Supply Recommendations.............................59
- 8.4 Device Functional Modes..........................................44 / 8.5 Thermal Shutdown....................................................46 / 9 Application and Implementation..................................47 / 9.1 Application Information............................................. 47 / 9.2 Typical Application.................................................... 47 / 9.3 Power Supply Recommendations.............................59 / 9.4 Layout....................................................................... 60
- 8.5 Thermal Shutdown....................................................46 / 9 Application and Implementation..................................47 / 9.1 Application Information............................................. 47 / 9.2 Typical Application.................................................... 47 / 9.3 Power Supply Recommendations.............................59 / 9.4 Layout....................................................................... 60 / 10 Device and Documentation Support..........................74
- PPHV VBUS(5) / C Capacitance on CCy pins(3) 6.3 V 200 400 480 pF / CCy / (1) Capacitance values do not include any derating factors. For example, if 5.0 uF is required and the external capacitor value reduces by / 50% at the required operating voltage, then the required external capacitor value is 10 uF. / (2) USB PD requirement (cSrcBulkShared). Keep at least 10 uF tied directly to PP5V. / (3) Capacitance includes all external capacitance to the Type-C receptacle.
- Junction-to-case (bottom DRAIN pad) / R (bot_DRAIN) 4.6 deg C/W / JC thermal resistance / (1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application / report. / 6.5.2 TPS25751S - Thermal Information / TPS25751S
- Junction-to-board characterization / 9.7 deg C/W / JB parameter / (1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application / report. / 10 Submit Document Feedback Copyright 2024 Texas Instruments Incorporated / Product Folder Links: TPS25751
- output. See Power Management for more information. / The digital core provides the engine for receiving, processing, and sending all USB-PD packets as well as / handling control of all other TPS25751 functionality. A portion of the digital core contains ROM memory, which / contains all the necessary firmware required to execute Type-C and PD applications. In addition, a section of the / ROM, called boot code, is capable of initializing the TPS25751, loading of the device configuration information, / and loading any code patches into volatile memory in the digital core. For a high-level block diagram of the / digital core, a description of its features, and more detailed circuitry, see Digital Core.

## Page-by-page extracted content

### Page 1

#### Extracted tables

Table 1:

```text
PART NUMB | ER PACKAGE(1) | PACKAGE SIZE(2)
TPS25751D | QFN (REF) | 4.0mm x 6.0mm
TPS25751S | QFN (RSM) | 4.0mm x 4.0mm
```

Table 2:

```text
A
DO TPS25751D 3A Type-C Rp/Rd & state CC1/2 machine, VCONN switches, USB PD policy engine, protocol and physical layer r 10 GPIO
```

Table 3:

```text
PP_EXT Control
LDO TPS25751S 3A Type-C Rp/Rd & sta machine, VCONN switches, USB PD policy engin I2C protocol and physic Target layer I2C Controller 10
```

#### Raw extracted text

```text
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
TPS25751 USB Type-C(R) and USB PD Controller with Integrated Power Switches
Optimized for Power Applications
1 Features 2 Applications
* PD Controller is certified by the USB-IF for PD3.1 * Power tools, power banks, retail and payment
- PD3.1 silicon is required for certification of new * Wireless speakers, Cordless vacuum cleaner
USB PD designs * personal electronics and industrial applications
- TPS25751 TID#: 10306 * Home health care and Personal care and fitness
- Article on PD2.0 vs. PD3.0
3 Description
* Optimized for USB Type-C PD power applications
- Integrated I2C control for TI battery chargers The TPS25751 is a highly integrated stand-alone USB
Type-C and Power Delivery (PD) controller optimized
* BQ25756, BQ25756E, BQ25790, BQ25792
for applications supporting USB-C PD Power. The
* BQ25798, BQ25713, BQ25731
TPS25751 integrates fully managed power paths
- Web-based GUI and pre-configured firmware
with robust protection for a complete USB-C PD
- Optimized for power consumer only (sink)
solution. The TPS25751 also integrates control for
(UFP) applications
external battery charger ICs for added ease of
- Optimized for power provider/power consumer
use and reduced time to market. The intuitive web
(DRP) applications
based GUI asks the user a few simple questions on
- For a more extensive selection guide and
the applications needs using clear block diagrams
getting started information, please refer to
and simple multiple-choice questions. As a result,
www.ti.com/usb-c and E2E guide
the GUI creates the configuration image for the
* Programmable Power Supply (PPS)
users application, reducing much of the complexity
- Supports PPS source & sink
associated with competitive USB PD solutions.
- Standalone PPS source control TI battery
chargers Package Information
- Programmable interface for PPS sink PART NUMBER PACKAGE(1) PACKAGE SIZE(2)
* Liquid Detection
TPS25751D QFN (REF) 4.0mm x 6.0mm
- Measures directly at the Type-C connector
TPS25751S QFN (RSM) 4.0mm x 4.0mm
- Integrated error handling and protection
* Integrated fully managed power paths (1) For all available packages, see the orderable addendum at
the end of the data sheet.
- Integrated 5V, 3A, 36mOhm sourcing switch
(2) The package size (length x width) is a nominal value and
(TPS25751S and TPS25751D)
includes pins, where applicable.
- Integrated 20V, 5A, 16mOhm bi-directional load
switch (TPS25751D only) 5A
5-20 V
* Integrated robust power path protection
3.3V LDO
- Integrated reverse current protection, TPS25751D
undervoltage protection, overvoltage protection, 5 V 3A VBUS
3.3V
and slew rate control the high-voltage bi- Ty V p C e- O C m N R N a p c s / h R w in d it e c & , h s e t s a , t e CC1/2 2 C VC C ONN
directional power path E C O m o p b n t e t i r o d o n d ll a e e l r d Ta I2 rg C e t U p S ro B t o P c D o l p l a a o y n li e d c r y p h e y n s g i i c n a e l ,
- Integrated undervoltage and overvoltage
BQ Battery I2C GND
protection and current limiting for inrush current Charger Controller
10 GPIO
protection for the 5V/3A source power path
5-20 V
- 26V tolerant CC pins for robust protection when
connected to non-compliant devices PP_EXT
Control
3.3V LDO
* USB Type-C(R) Power Delivery (PD) controller
TPS25751S
- 10 configurable GPIOs 5 V VBUS
3A
- BC1.2 advertisement/detection support 3.3V
- 3.3V LDO output for dead battery support Ty V p C e- O C m N R N a p c s / h R w in d it e c & , h s e t s a , t e CC1/2 2 C VC C ONN
- Power supply from 3.3V or VBUS source E C O m o p b n t e t i r o d o n d ll a e e l r d Ta I2 rg C e t U p S ro B t o P c D o l p l a a o y n li e d c r y p h e y n s g i i c n a e l ,
- 1 I2C controller port BQ Battery I2C GND
Charger Controller
- 1 I2C target port 10 GPIO
An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications,
intellectual property matters and other important disclaimers. PRODUCTION DATA.
```

### Page 2

#### Raw extracted text

```text
Table of Contents
1 Features............................................................................1
2 Applications.....................................................................1
3 Description.......................................................................1
4 Device Comparison Table...............................................3
5 Pin Configuration and Functions...................................4
6 Specifications.................................................................. 7
6.1 Absolute Maximum Ratings........................................ 7
6.2 ESD Ratings............................................................... 8
6.3 Recommended Operating Conditions.........................8
6.4 Recommended Capacitance.......................................9
6.5 Thermal Information..................................................10
6.6 Power Supply Characteristics................................... 11
6.7 Power Consumption..................................................11
6.8 PP_5V Power Switch Characteristics....................... 11
6.9 PPHV Power Switch Characteristics - TPS25751D..12
6.10 PP_EXT Power Switch Characteristics -
TPS25751S.................................................................13
6.11 Power Path Supervisory..........................................14
6.12 CC Cable Detection Parameters.............................14
6.13 CC VCONN Parameters......................................... 15
6.14 CC PHY Parameters...............................................16
6.15 Thermal Shutdown Characteristics.........................17
6.16 ADC Characteristics................................................17
6.17 Input/Output (I/O) Characteristics........................... 17
6.18 BC1.2 Characteristics............................................. 18
6.19 I2C Requirements and Characteristics................... 18
6.20 Typical Characteristics ...........................................20
7 Parameter Measurement Information..........................22
8 Detailed Description......................................................23
8.1 Overview...................................................................23
8.2 Functional Block Diagram.........................................23
8.3 Feature Description...................................................26
8.4 Device Functional Modes..........................................44
8.5 Thermal Shutdown....................................................46
9 Application and Implementation..................................47
9.1 Application Information............................................. 47
9.2 Typical Application.................................................... 47
9.3 Power Supply Recommendations.............................59
9.4 Layout....................................................................... 60
10 Device and Documentation Support..........................74
10.1 Device Support....................................................... 74
10.2 Documentation Support.......................................... 74
10.3 Receiving Notification of Documentation Updates..74
10.4 Support Resources................................................. 74
10.5 Trademarks.............................................................74
10.6 Electrostatic Discharge Caution..............................74
10.7 Glossary..................................................................74
11 Revision History.......................................................... 75
12 Mechanical, Packaging, and Orderable
Information.................................................................... 75
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
 www.ti.com
2 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 3

#### Extracted tables

Table 1:

```text
DEVICE NUMBER | 5-V SOURCE LOAD SWITCH | INTEGRATED HIGH VOLTAGE BI-DIRECTIONAL LOAD SWITCH (PPHV) | HIGH VOLTAGE GATE DRIVER FOR BI-DIRECTIONAL EXTERNAL PATH (PP_EXT)
TPS25751D | Yes | Yes | No
TPS25751S | Yes | No | Yes
```

#### Raw extracted text

```text
4 Device Comparison Table
DEVICE NUMBER 5-V SOURCE LOAD SWITCH
INTEGRATED HIGH
VOLTAGE BI-DIRECTIONAL
LOAD SWITCH (PPHV)
HIGH VOLTAGE GATE DRIVER
FOR BI-DIRECTIONAL EXTERNAL
PATH (PP_EXT)
TPS25751D Yes Yes No
TPS25751S Yes No Yes
www.ti.com
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 3
Product Folder Links: TPS25751
```

### Page 4

#### Raw extracted text

```text
5 Pin Configuration and Functions
37 36 35 34 33 32 31 30 29 28 27
ADCIN1
PPHV
8 9 10 11 12 13 14 15 16 17 18
GPIO2
38 26
LDO_3V3 1 25
2 24
ADCIN2 3 23
Thermal Pad Thermal Pad
(GND) (DRAIN)
LDO_1V5 4 22
GPIO0 5 21
GPIO1 6 20
7 19
I2Ct_SDA I2Ct_SCL I2Ct_IRQ GND GND GPIO11 GND DRAIN I2Cc_SDA I2Cc_SCL I2Cc_IRQ GPIO3
VBUS_IN
VBUS_IN
VBUS_IN
PPHV
PPHV
VIN_3V3
GPIO6 GPIO7 PP5V PP5V VBUS VBUS GND DRAIN CC2 CC1 LD2
GPIO5/USB_N/
LD1
GPIO4/USB_P/
Not to Scale
Figure 5-1. Top View of the TPS25751D 38-pin QFN Package
3V3_NIV
LCS_tC2I
6OIPG
QRI_tC2I
7OIPG
DNG
V5PP
DNG
V5PP
11OIPG
SUBV
DNG
SUBV
ADS_cC2I
2CC
LCS_cC2I
LDO_3V3 1 24 CC1
ADCIN1 2 23 GPIO5/USB_N/LD2
ADCIN2 3 22 GPIO4/USB_P/LD1
Thermal
LDO_1V5 4 21 GATE_VBUS
Pad
GPIO0 5 (GND) 20 GATE_VSYS
GPIO1 6 19 VSYS
GPIO2 7 18 GPIO3
I2Ct_SDA 8 17 I2Cc_IRQ
Not to Scale
23
9
13
01
03
11
92
21
82
31
72
41
62
51
52
61
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024 www.ti.com
Figure 5-2. Top View of the TPS25751S 32-pin QFN Package
4 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 5

#### Extracted tables

Table 1:

```text
PIN |  | TYPE(1) | RESET | DESCRIPTION
NAME | NO. |  |  | 
ADCIN1 | 2 | I | Hi-Z | Configuration Input. Connect to a resistor divider to LDO_3V3.
ADCIN2 | 3 | I | Hi-Z | Configuration Input. Connect to a resistor divider to LDO_3V3.
CC1 | 28 | I/O | Hi-Z | I/O for USB Type-C. Filter noise with recommended capacitor to GND (CCCy).
CC2 | 29 | I/O | Hi-Z | I/O for USB Type-C. Filter noise with recommended capacitor to GND (CCCy).
GND | 11, 12, 14, 31 |  |  | Ground. Connect to ground plane.
GPIO0 | 5 | GPIO | Hi-Z | General purpose digital I/O. Tie to ground when pin is unused.
GPIO1 | 6 | GPIO | Hi-Z | General purpose digital I/O. Tie to ground when pin is unused.
GPIO2 | 7 | GPIO | Hi-Z | General purpose digital I/O. Tie to ground when pin is unused.
GPIO3 | 19 | GPIO | Hi-Z | General purpose digital I/O. Tie to ground when pin is unused.
GPIO4/USB_P/LD1 | 26 | GPIO | Hi-Z | General purpose digital I/O. Tie to ground when unused. Pin can be connected to D+ for BC1.2 support. Pin can be connected for liquid detection on the Type-C connector. Tie to ground when pin is unused.
GPIO5/USB_N/LD2 | 27 | GPIO | Hi-Z | General purpose digital I/O. Tie to ground when unused. Pin can be connected to D- for BC1.2 support. Pin can be connected for liquid detection on the Type-C connector. Tie to ground when pin is unused.
GPIO6 | 37 | GPIO | Hi-Z | General purpose digital I/O. Tie to ground when pin is unused.
GPIO7 | 36 | GPIO | Hi-Z | General purpose digital I/O. Tie to ground when pin is unused.
I2Ct_SCL | 9 | I | Hi-Z | I2C target serial clock input. Tie to pullup voltage through a resistor. May be grounded if unused.
I2Ct_SDA | 8 | I/O | Hi-Z | I2C target serial data. Open-drain input/output. Tie to pullup voltage through a resistor. May be grounded if unused.
I2Ct_IRQ | 10 | O | Hi-Z | I2C target interrupt. Active low. Connect to external voltage through a pull-up resistor. Pin can be re-configured to GPIO10. Tie to ground if unused.
I2Cc_SCL | 17 | O | Hi-Z | I2C controller serial clock. Open-drain output. Tie to pullup voltage through a resistor. Can be grounded if unused.
GPIO11 | 13 | GPIO | Hi-Z | General purpose digital I/O. Tie to ground when pin is unused.
I2Cc_SDA | 16 | I/O | Hi-Z | I2C controller serial data. Open-drain input/output. Tie to pullup voltage through a resistor. Can be grounded if unused.
I2Cc_IRQ | 18 | I | Hi-Z | I2C controller interrupt. Active low. Connect to external voltage through a pull-up resistor. Do NOT tie to GND when unused. Pin can be re-configured to GPIO12.
LDO_1V5 | 4 | O |  | Output of the CORE LDO. Bypass with capacitance C to GND. Pin LDO_1V5 cannot source current to external circuits.
LDO_3V3 | 1 | O |  | Output of supply switched from VIN_3V3 or VBUS LDO. Bypass with capacitance C to GND. LDO_3V3
DRAIN | 15, 30 | N/A |  | Connects to drain of internal FET.
PP5V | 34, 35 | I |  | 5-V System Supply to VBUS, supply for CCy pins as VCONN.
PPHV | 20, 21, 22 | I/O |  | High-voltage sinking node in the system.
VBUS_IN | 23, 24, 25 | I/O |  | 5-V to 20-V input.
VBUS | 32, 33 | O |  | 5-V output from PP5V input to LDO. Bypass with capacitance C to GND. VBUS
VIN_3V3 | 38 | I |  | Supply for core circuitry and I/O. Bypass with capacitance C to GND. VIN_3V3
```

#### Raw extracted text

```text
TPS25751
www.ti.com SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
Table 5-1. TPS25751D Pin Functions
PIN
TYPE(1) RESET DESCRIPTION
NAME NO.
ADCIN1 2 I Hi-Z Configuration Input. Connect to a resistor divider to LDO_3V3.
ADCIN2 3 I Hi-Z Configuration Input. Connect to a resistor divider to LDO_3V3.
I/O for USB Type-C. Filter noise with recommended capacitor to GND
CC1 28 I/O Hi-Z
(CCCy).
I/O for USB Type-C. Filter noise with recommended capacitor to GND
CC2 29 I/O Hi-Z
(CCCy).
GND 11, 12, 14, 31 - - Ground. Connect to ground plane.
GPIO0 5 GPIO Hi-Z General purpose digital I/O. Tie to ground when pin is unused.
GPIO1 6 GPIO Hi-Z General purpose digital I/O. Tie to ground when pin is unused.
GPIO2 7 GPIO Hi-Z General purpose digital I/O. Tie to ground when pin is unused.
GPIO3 19 GPIO Hi-Z General purpose digital I/O. Tie to ground when pin is unused.
General purpose digital I/O. Tie to ground when unused. Pin can be
GPIO4/USB_P/LD1 26 GPIO Hi-Z connected to D+ for BC1.2 support. Pin can be connected for liquid detection
on the Type-C connector. Tie to ground when pin is unused.
General purpose digital I/O. Tie to ground when unused. Pin can be
GPIO5/USB_N/LD2 27 GPIO Hi-Z connected to D- for BC1.2 support. Pin can be connected for liquid detection
on the Type-C connector. Tie to ground when pin is unused.
GPIO6 37 GPIO Hi-Z General purpose digital I/O. Tie to ground when pin is unused.
GPIO7 36 GPIO Hi-Z General purpose digital I/O. Tie to ground when pin is unused.
I2C target serial clock input. Tie to pullup voltage through a resistor. May be
I2Ct_SCL 9 I Hi-Z
grounded if unused.
I2C target serial data. Open-drain input/output. Tie to pullup voltage through a
I2Ct_SDA 8 I/O Hi-Z
resistor. May be grounded if unused.
I2C target interrupt. Active low. Connect to external voltage through a pull-up
I2Ct_IRQ 10 O Hi-Z
resistor. Pin can be re-configured to GPIO10. Tie to ground if unused.
I2C controller serial clock. Open-drain output. Tie to pullup voltage through a
I2Cc_SCL 17 O Hi-Z
resistor. Can be grounded if unused.
GPIO11 13 GPIO Hi-Z General purpose digital I/O. Tie to ground when pin is unused.
I2C controller serial data. Open-drain input/output. Tie to pullup voltage
I2Cc_SDA 16 I/O Hi-Z
through a resistor. Can be grounded if unused.
I2C controller interrupt. Active low. Connect to external voltage through a
I2Cc_IRQ 18 I Hi-Z pull-up resistor. Do NOT tie to GND when unused. Pin can be re-configured
to GPIO12.
Output of the CORE LDO. Bypass with capacitance C to GND. Pin
LDO_1V5 4 O - LDO_1V5
cannot source current to external circuits.
Output of supply switched from VIN_3V3 or VBUS LDO. Bypass with
LDO_3V3 1 O -
capacitance C to GND.
LDO_3V3
DRAIN 15, 30 N/A - Connects to drain of internal FET.
PP5V 34, 35 I - 5-V System Supply to VBUS, supply for CCy pins as VCONN.
PPHV 20, 21, 22 I/O High-voltage sinking node in the system.
VBUS_IN 23, 24, 25 I/O 5-V to 20-V input.
VBUS 32, 33 O 5-V output from PP5V input to LDO. Bypass with capacitance C to GND.
VBUS
VIN_3V3 38 I - Supply for core circuitry and I/O. Bypass with capacitance C to GND.
VIN_3V3
(1) I = input, O = output, I/O = input and output, GPIO = general purpose digital input and output
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 5
Product Folder Links: TPS25751
```

### Page 6

#### Extracted tables

Table 1:

```text
PIN |  | TYPE(1) | RESET | DESCRIPTION
NAME | NO. |  |  | 
ADCIN1 | 2 | I | Hi-Z | Configuration Input. Connect to a resistor divider to LDO_3V3.
ADCIN2 | 3 | I | Hi-Z | Configuration Input. Connect to a resistor divider to LDO_3V3.
CC1 | 24 | I/O | Hi-Z | I/O for USB Type-C. Filter noise with recommended capacitor to GND (CCCy).
CC2 | 25 | I/O | Hi-Z | I/O for USB Type-C. Filter noise with recommended capacitor to GND (CCCy).
GATE_VSYS | 20 | O | Hi-Z | Connect to the N-ch MOSFET that has source tied to VSYS.
GATE_VBUS | 21 | O | Hi-Z | Connect to the N-ch MOSFET that has source tied to VBUS.
GND | 11, 12, 14 |  |  | Ground. Connect to ground plane.
GPIO0 | 5 | GPIO | Hi-Z | General purpose digital I/O. Tie to ground when pin is unused.
GPIO1 | 6 | GPIO | Hi-Z | General purpose digital I/O. Tie to ground when pin is unused.
GPIO2 | 7 | GPIO | Hi-Z | General purpose digital I/O. Tie to ground when pin is unused.
GPIO3 | 18 | GPIO | Hi-Z | General purpose digital I/O. Tie to ground when pin is unused.
GPIO4/USB_P/LD1 | 22 | GPIO | Hi-Z | General purpose digital I/O. Tie to ground when unused. Pin can be connected to D+ for BC1.2 support. Pin can be connected for liquid detection on the Type-C connector. Tie to ground when pin is unused.
GPIO5/USB_N/LD2 | 23 | GPIO | Hi-Z | General purpose digital I/O. Tie to ground when unused. Pin can be connected to D- for BC1.2 support. Pin can be connected for liquid detection on the Type-C connector. Tie to ground when pin is unused.
GPIO6 | 31 | GPIO | Hi-Z | General purpose digital I/O. Tie to ground when pin is unused.
GPIO7 | 30 | GPIO | Hi-Z | General purpose digital I/O. Tie to ground when pin is unused.
I2Ct_SCL | 9 | I | Hi-Z | I2C target serial clock input. Tie to pullup voltage through a resistor. May be grounded if unused.
I2Ct_SDA | 8 | I/O | Hi-Z | I2C target serial data. Open-drain input/output. Tie to pullup voltage through a resistor. May be grounded if unused.
I2Ct_IRQ | 10 | O | Hi-Z | I2C target interrupt. Active low. Connect to external voltage through a pull-up resistor. Pin can be re-configured to GPIO10. Tie to ground when unused.
I2Cc_SCL | 16 | O | Hi-Z | I2C controller serial clock. Open-drain output. Tie to pullup voltage through a resistor when used or unused.
GPIO11 | 13 | GPIO | Hi-Z | General purpose digital I/O. Tie to ground when pin is unused.
I2Cc_SDA | 15 | I/O | Hi-Z | I2C controller serial data. Open-drain input/output. Tie to pullup voltage through a resistor when used or unused.
I2Cc_IRQ | 17 | I | Hi-Z | I2C controller interrupt. Active low. Connect to external voltage through a pull-up resistor. Do NOT tie to GND when unused. Pin can be re-configured to GPIO12.
LDO_1V5 | 4 | O |  | Output of the CORE LDO. Bypass with capacitance C to GND. Pin LDO_1V5 cannot source current to external circuits.
LDO_3V3 | 1 | O |  | Output of supply switched from VIN_3V3 or VBUS LDO. Bypass with capacitance C to GND. LDO_3V3
PP5V | 28, 29 | I |  | 5-V System Supply to VBUS, supply for CCy pins as VCONN.
VSYS | 19 | I |  | High-voltage sinking node in the system. Pin is used to implement reverse-current-protection (RCP) for the external sinking paths controlled by GATE_VSYS.
VBUS | 26, 27 | I/O |  | 5-V to 20-V input. Bypass with capacitance C to GND. VBUS
VIN_3V3 | 32 | I |  | Supply for core circuitry and I/O. Bypass with capacitance CVIN_3V3 to GND.
```

#### Raw extracted text

```text
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024 www.ti.com
Table 5-2. TPS25751S Pin Functions
PIN
TYPE(1) RESET DESCRIPTION
NAME NO.
ADCIN1 2 I Hi-Z Configuration Input. Connect to a resistor divider to LDO_3V3.
ADCIN2 3 I Hi-Z Configuration Input. Connect to a resistor divider to LDO_3V3.
I/O for USB Type-C. Filter noise with recommended capacitor to GND
CC1 24 I/O Hi-Z
(CCCy).
I/O for USB Type-C. Filter noise with recommended capacitor to GND
CC2 25 I/O Hi-Z
(CCCy).
GATE_VSYS 20 O Hi-Z Connect to the N-ch MOSFET that has source tied to VSYS.
GATE_VBUS 21 O Hi-Z Connect to the N-ch MOSFET that has source tied to VBUS.
GND 11, 12, 14 - - Ground. Connect to ground plane.
GPIO0 5 GPIO Hi-Z General purpose digital I/O. Tie to ground when pin is unused.
GPIO1 6 GPIO Hi-Z General purpose digital I/O. Tie to ground when pin is unused.
GPIO2 7 GPIO Hi-Z General purpose digital I/O. Tie to ground when pin is unused.
GPIO3 18 GPIO Hi-Z General purpose digital I/O. Tie to ground when pin is unused.
General purpose digital I/O. Tie to ground when unused. Pin can be
GPIO4/USB_P/LD1 22 GPIO Hi-Z connected to D+ for BC1.2 support. Pin can be connected for liquid detection
on the Type-C connector. Tie to ground when pin is unused.
General purpose digital I/O. Tie to ground when unused. Pin can be
GPIO5/USB_N/LD2 23 GPIO Hi-Z connected to D- for BC1.2 support. Pin can be connected for liquid detection
on the Type-C connector. Tie to ground when pin is unused.
GPIO6 31 GPIO Hi-Z General purpose digital I/O. Tie to ground when pin is unused.
GPIO7 30 GPIO Hi-Z General purpose digital I/O. Tie to ground when pin is unused.
I2C target serial clock input. Tie to pullup voltage through a resistor. May be
I2Ct_SCL 9 I Hi-Z
grounded if unused.
I2C target serial data. Open-drain input/output. Tie to pullup voltage through a
I2Ct_SDA 8 I/O Hi-Z
resistor. May be grounded if unused.
I2C target interrupt. Active low. Connect to external voltage through a pull-up
I2Ct_IRQ 10 O Hi-Z
resistor. Pin can be re-configured to GPIO10. Tie to ground when unused.
I2C controller serial clock. Open-drain output. Tie to pullup voltage through a
I2Cc_SCL 16 O Hi-Z
resistor when used or unused.
GPIO11 13 GPIO Hi-Z General purpose digital I/O. Tie to ground when pin is unused.
I2C controller serial data. Open-drain input/output. Tie to pullup voltage
I2Cc_SDA 15 I/O Hi-Z
through a resistor when used or unused.
I2C controller interrupt. Active low. Connect to external voltage through a
I2Cc_IRQ 17 I Hi-Z pull-up resistor. Do NOT tie to GND when unused. Pin can be re-configured
to GPIO12.
Output of the CORE LDO. Bypass with capacitance C to GND. Pin
LDO_1V5 4 O - LDO_1V5
cannot source current to external circuits.
Output of supply switched from VIN_3V3 or VBUS LDO. Bypass with
LDO_3V3 1 O -
capacitance C to GND.
LDO_3V3
PP5V 28, 29 I - 5-V System Supply to VBUS, supply for CCy pins as VCONN.
High-voltage sinking node in the system. Pin is used to implement
VSYS 19 I - reverse-current-protection (RCP) for the external sinking paths controlled by
GATE_VSYS.
VBUS 26, 27 I/O 5-V to 20-V input. Bypass with capacitance C to GND.
VBUS
VIN_3V3 32 I - Supply for core circuitry and I/O. Bypass with capacitance CVIN_3V3 to GND.
(1) I = input, O = output, I/O = input and output, GPIO = general purpose digital input and output
6 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 7

#### Extracted tables

Table 1:

```text
|  | MIN | MAX | UNIT
Input voltage range (2) | PP5V | 0.3 6 |  | V
 | VIN_3V3 | 0.3 4 |  | 
 | ADCIN1, ADCIN2 | 0.3 4 |  | 
 | VBUS_IN, VBUS(4) | 0.3 28 |  | V
 | CC1, CC2 (4) | 0.5 26 |  | 
 | GPIOx | 0.3 6.0 |  | 
 | I2Cc_SDA, I2Cc_SCL, I2Cc_IRQ, I2Ct_IRQ,I2Ct_SCL, I2Ct_SDA | 0.3 4 |  | 
Output voltage range (2) | LDO_1V5(3) | 0.3 2 |  | V
 | LDO_3V3(3) | 0.3 4 |  | 
Source current | Source or sink current VBUS | internally limited |  | A
 | Positive source current on CC1, CC2 | 1 |  | 
 | Positive sink current on CC1, CC2 while VCONN switch is enabled | 1 |  | 
 | Positive sink current for I2Cc_SDA, I2Cc_SCL, I2Cc_IRQ, I2Ct_IRQ,I2Ct_SCL, I2Ct_SDA | internally limited |  | 
 | Positive source current for LDO_3V3, LDO_1V5 | internally limited |  | 
Source current | GPIOx | 0.005 |  | A
T Operating junction temperature J |  | 40 175 |  | deg C
T Storage temperature STG |  | 55 150 |  | deg C
```

Table 2:

```text
|  | MIN | MAX | UNIT
Input voltage range (1) | PPHV | 0.3 | 28 | V
V PPHV_VBUS_IN | Source-to-source voltage | 28 |  | V
Sink current | Continuous current to/from VBUS_IN to PPHV |  | 7 | A
 | Pulsed current to/from VBUS_IN to PPHV(2) |  | 10 | 
T Operating J_PPHV junction temperature | PP_HV switch | 40 175 |  | deg C
```

Table 3:

```text
|  | MIN | MAX | UNIT
Output voltage range 1 | GATE_VBUS, GATE_VSYS2 | 0.3 | 40 | V
```

#### Raw extracted text

```text
TPS25751
www.ti.com SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
6 Specifications
6.1 Absolute Maximum Ratings
6.1.1 TPS25751D and TPS25751S - Absolute Maximum Ratings
over operating free-air temperature range (unless otherwise noted)(1)
MIN MAX UNIT
PP5V -0.3 6
VIN_3V3 -0.3 4 V
ADCIN1, ADCIN2 -0.3 4
Input voltage range (2) VBUS_IN, VBUS(4) -0.3 28
CC1, CC2 (4) -0.5 26
GPIOx -0.3 6.0 V
I2Cc_SDA, I2Cc_SCL, I2Cc_IRQ,
-0.3 4
I2Ct_IRQ,I2Ct_SCL, I2Ct_SDA
LDO_1V5(3) -0.3 2
Output voltage range (2) V
LDO_3V3(3) -0.3 4
Source or sink current VBUS internally limited
Positive source current on CC1, CC2 1
Positive sink current on CC1, CC2 while VCONN
1
Source current switch is enabled A
Positive sink current for I2Cc_SDA, I2Cc_SCL,
internally limited
I2Cc_IRQ, I2Ct_IRQ,I2Ct_SCL, I2Ct_SDA
Positive source current for LDO_3V3, LDO_1V5 internally limited
Source current GPIOx 0.005 A
T Operating junction temperature -40 175  deg C
J
T Storage temperature -55 150  deg C
STG
(1) Operation outside the Absolute Maximum Ratings may cause permanent device damage. Absolute Maximum Ratings do not imply
functional operation of the device at these or any other conditions beyond those listed under Recommended Operating Conditions.
If used outside the Recommended Operating Conditions but within the Absolute Maximum Ratings, the device may not be fully
functional, and this may affect device reliability, functionality, performance, and shorten the device lifetime.
(2) All voltage values are with respect to network GND. Connect the GND pin directly to the GND plane of the board.
(3) Do not apply voltage to these pins.
(4) A TVS with a break down voltage falling between the Recommended max and the Abs max value is recommended such as TVS2200.
6.1.2 TPS25751D - Absolute Maximum Ratings
MIN MAX UNIT
Input voltage range (1) PPHV -0.3 28 V
V Source-to-source voltage 28 V
PPHV_VBUS_IN
Sink current Continuous current to/from 7 A
VBUS_IN to PPHV
Pulsed current to/from 10
VBUS_IN to PPHV(2)
T Operating
J_PPHV PP_HV switch -40 175  deg C
junction temperature
(1) All voltage values are with respect to network GND. Connect the GND pin directly to the GND plane of the board.
(2) Pulse duration <= 100 us and duty-cycle <= 1%.
6.1.3 TPS25751S - Absolute Maximum Ratings
MIN MAX UNIT
Output voltage range 1 G G A A T T E E _ _ V V B S U YS S 2 , -0.3 40 V
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 7
Product Folder Links: TPS25751
```

### Page 8

#### Extracted tables

Table 1:

```text
|  | MIN | MAX | UNIT
V GS | V - V , GATE_VBUS VBUS V - V GATE_SYS VSYS | 0.5 | 12 | V
```

Table 2:

```text
PARAMETER |  | TEST CONDITIONS | VALUE | UNIT
V (ESD) | Electrostatic discharge | Human-body model (HBM), per ANSI/ ESDA/JEDEC JS-001, all pins(1) | +/-1000 | V
 |  | Charged-device model (CDM), per ANSI/ ESDA/JEDEC JS-002, all pins(2) | +/-500 |
```

Table 3:

```text
|  |  | MIN | MAX | UNIT
V I | Input voltage range (1) | VIN_3V3 | 3.0 3.6 |  | V
 |  | PP5V | 4.9 5.5 |  | 
 |  | ADCIN1, ADCIN2,VBUS_IN, VBUS | 4 22 |  | 
 |  | PPHV | 0 22 |  | 
V IO | I/O voltage range (1) | I2Cx_SDA, I2Cx_SCL, I2Cx_IRQ, ADCIN1, ADCIN2 | 0 3.6 |  | V
 |  | GPIOx | 0 5.5 |  | 
 |  | CC1, CC2 | 0 5.5 |  | 
I O | Output current (from PP5V) | VBUS | 3 |  | A
 |  | CC1, CC2 | 315 |  | mA
I O | Output current (from LDO_3V3) | GPIOx | 1 |  | mA
T J | Operating junction temperature |  | 40 125 |  | deg C
```

Table 4:

```text
|  |  | MIN | MAX | UNIT
V I | Input voltage range (1) | VIN_3V3 | 3.0 3.6 |  | V
 |  | PP5V | 4.9 5.5 |  | 
 |  | VBUS | 4 22 |  | 
 |  | VSYS | 0 22 |  | 
V IO | I/O voltage range (1) | I2Cx_SDA, I2Cx_SCL, I2Cx_IRQ, ADCIN1, ADCIN2 | 0 3.6 |  | V
 |  | GPIOx | 0 5.5 |  | 
 |  | CC1, CC2 | 0 5.5 |  | 
I O | Output current (from PP5V) | VBUS | 3 |  | A
 |  | CC1, CC2 | 315 |  | mA
I O | Output current (from LDO_3V3) | GPIOx | 1 |  | mA
I O | Output current (from VBUS LDO) | sum of current from LDO_3V3 and GPIOx | 5 |  | mA
```

#### Raw extracted text

```text
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024 www.ti.com
6.1.3 TPS25751S - Absolute Maximum Ratings (continued)
MIN MAX UNIT
V - V ,
V GATE_VBUS VBUS -0.5 12 V
GS V - V
GATE_SYS VSYS
(1) All voltage values are with respect to network GND. Connect the GND pin directly to the GND plane of the board.
(2) Do not apply voltage to these pins.
6.2 ESD Ratings
PARAMETER TEST CONDITIONS VALUE UNIT
Human-body model (HBM), per ANSI/
+/-1000
ESDA/JEDEC JS-001, all pins(1)
V Electrostatic discharge V
(ESD)
Charged-device model (CDM), per ANSI/
+/-500
ESDA/JEDEC JS-002, all pins(2)
(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process.
(2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process.
6.3.1 TPS25751D - Recommended Operating Conditions
over operating free-air temperature range (unless otherwise noted) (1)
MIN MAX UNIT
VIN_3V3 3.0 3.6
PP5V 4.9 5.5
V I Input voltage range (1) ADCIN1, ADCIN2,VBUS_IN, V
4 22
VBUS
PPHV 0 22
I2Cx_SDA, I2Cx_SCL, I2Cx_IRQ,
0 3.6
ADCIN1, ADCIN2
V I/O voltage range (1) V
IO GPIOx 0 5.5
CC1, CC2 0 5.5
VBUS 3 A
I Output current (from PP5V)
O
CC1, CC2 315 mA
I Output current (from LDO_3V3) GPIOx 1 mA
O
T Operating junction temperature -40 125  deg C
J
(1) All voltage values are with respect to network GND. All GND pins must be connected directly to the GND plane of the board.
6.3.2 TPS25751S - Recommended Operating Conditions
over operating free-air temperature range (unless otherwise noted)(1)
MIN MAX UNIT
VIN_3V3 3.0 3.6
PP5V 4.9 5.5
V Input voltage range (1) V
I
VBUS 4 22
VSYS 0 22
I2Cx_SDA, I2Cx_SCL, I2Cx_IRQ,
0 3.6
ADCIN1, ADCIN2
V I/O voltage range (1) V
IO GPIOx 0 5.5
CC1, CC2 0 5.5
VBUS 3 A
I Output current (from PP5V)
O
CC1, CC2 315 mA
I Output current (from LDO_3V3) GPIOx 1 mA
O
sum of current from LDO_3V3 and
I Output current (from VBUS LDO) 5 mA
O GPIOx
8 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 9

#### Extracted tables

Table 1:

```text
|  | MIN | MAX | UNIT
T J | Operating junction temperature | 40 125 |  | deg C
```

Table 2:

```text
PARAMETER(1) |  | VOLTAGE RATING | MIN | NOM | MAX | UNIT
C VIN_3V3 | Capacitance on VIN_3V3 | 6.3 V | 5 10 |  |  | uF
C LDO_3V3 | Capacitance on LDO_3V3 | 6.3 V | 5 10 25 |  |  | uF
C LDO_1V5 | Capacitance on LDO_1V5 | 4 V | 4.5 12 |  |  | uF
C VBUS | Capacitance on VBUS(4) | 25 V | 1 4.7 10 |  |  | uF
C PP5V | Capacitance on PP5V | 10 V | 120(2) |  |  | uF
C (TPS25751S) VSYS | Capacitance on VSYS Sink from VBUS(5) | 25 V | 47 100 |  |  | uF
C (TPS25751D) PPHV | Capacitance on PPHV Sink from VBUS(5) | 25 V | 47 100 |  |  | uF
C CCy | Capacitance on CCy pins(3) | 6.3 V | 200 400 480 |  |  | pF
```

#### Raw extracted text

```text
TPS25751
www.ti.com SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
over operating free-air temperature range (unless otherwise noted)(1)
MIN MAX UNIT
T Operating junction temperature -40 125  deg C
J
(1) All voltage values are with respect to network GND. All GND pins must be connected directly to the GND plane of the board.
6.4 Recommended Capacitance
over operating free-air temperature range (unless otherwise noted)
PARAMETER(1) VOLTAGE RATING MIN NOM MAX UNIT
C Capacitance on VIN_3V3 6.3 V 5 10 uF
VIN_3V3
C Capacitance on LDO_3V3 6.3 V 5 10 25 uF
LDO_3V3
C Capacitance on LDO_1V5 4 V 4.5 12 uF
LDO_1V5
C Capacitance on VBUS(4) 25 V 1 4.7 10 uF
VBUS
C Capacitance on PP5V 10 V 120(2) uF
PP5V
Capacitance on VSYS Sink from
C (TPS25751S) 25 V 47 100 uF
VSYS VBUS(5)
Capacitance on PPHV Sink from
C (TPS25751D) 25 V 47 100 uF
PPHV VBUS(5)
C Capacitance on CCy pins(3) 6.3 V 200 400 480 pF
CCy
(1) Capacitance values do not include any derating factors. For example, if 5.0 uF is required and the external capacitor value reduces by
50% at the required operating voltage, then the required external capacitor value is 10 uF.
(2) USB PD requirement (cSrcBulkShared). Keep at least 10 uF tied directly to PP5V.
(3) Capacitance includes all external capacitance to the Type-C receptacle.
(4) The device can be configured to quickly disable the sinking power path upon certain events. When such a configuration is used, a
capacitance on the higher side of the range is recommended.
(5) USB PD specification for cSnkBulkPd (100uF) is the maximum bulk capacitance allowed on a VBUS sink after a PD contract is in
place. The capacitance is sufficient for all power conversion devices deriving power from the PD Controller sink path. For systems
requiring greater than 100uF, VBUS surge current limiting is implemented as described in the USB3.2 specification.
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 9
Product Folder Links: TPS25751
```

### Page 10

#### Extracted tables

Table 1:

```text
|  | TPS25751D | 
THERMAL METRIC(1) |  | QFN | UNIT
 |  | 38 PINS | 
R JA | Junction-to-ambient thermal resistance (sinking through PP_HV) | 57.4 | deg C/W
 | Junction-to-ambient thermal resistance (sourcing through PP_5V) | 46.5 | deg C/W
R (top) JC | Junction-to-case (top) thermal resistance (sinking through PP_HV) | 30.5 | deg C/W
 | Junction-to-case (top) thermal resistance (sourcing through PP_5V) | 20.3 | deg C/W
R JB | Junction-to-board thermal resistance (sinking through PP_HV) | 21.1 | deg C/W
 | Junction-to-board thermal resistance (sourcing through PP_5V) | 11.1 | deg C/W
JT | Junction-to-top characterization parameter (sinking through PP_HV) | 18.2 | deg C/W
 | Junction-to-top characterization parameter (sourcing through PP_5V) | 1.0 | deg C/W
JB | Junction-to-board characterization parameter (sinking through PP_HV) | 21.1 | deg C/W
 | Junction-to-board characterization parameter (sourcing through PP_5V) | 11.1 | deg C/W
R (bot_GND) JC | Junction-to-case (bottom GND pad) thermal resistance | 1.8 | deg C/W
R (bot_DRAIN) JC | Junction-to-case (bottom DRAIN pad) thermal resistance | 4.6 | deg C/W
```

Table 2:

```text
|  | TPS25751S | 
THERMAL METRIC(1) |  | QFN | UNIT
 |  | 32 PINS | 
R JA | Junction-to-ambient thermal resistance | 30.5 | deg C/W
R (top) JC | Junction-to-case (top) thermal resistance | 24.5 | deg C/W
R JC | Junction-to-board (bottom) thermal resistance | 2 | deg C/W
R JB | Junction-to-board thermal resistance | 9.8 | deg C/W
JT | Junction-to-top characterization parameter | 0.2 | deg C/W
JB | Junction-to-board characterization parameter | 9.7 | deg C/W
```

#### Raw extracted text

```text
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024 www.ti.com
6.5 Thermal Information
6.5.1 TPS25751D - Thermal Information
TPS25751D
THERMAL METRIC(1) QFN UNIT
38 PINS
Junction-to-ambient thermal resistance
57.4  deg C/W
(sinking through PP_HV)
R
JA
Junction-to-ambient thermal resistance
46.5  deg C/W
(sourcing through PP_5V)
Junction-to-case (top) thermal resistance
30.5  deg C/W
(sinking through PP_HV)
R (top)
JC
Junction-to-case (top) thermal resistance
20.3  deg C/W
(sourcing through PP_5V)
Junction-to-board thermal resistance
21.1  deg C/W
(sinking through PP_HV)
R
JB
Junction-to-board thermal resistance
11.1  deg C/W
(sourcing through PP_5V)
Junction-to-top characterization parameter
18.2  deg C/W
(sinking through PP_HV)

JT
Junction-to-top characterization parameter
1.0  deg C/W
(sourcing through PP_5V)
Junction-to-board characterization
21.1  deg C/W
parameter (sinking through PP_HV)

JB
Junction-to-board characterization
11.1  deg C/W
parameter (sourcing through PP_5V)
Junction-to-case (bottom GND pad)
R (bot_GND) 1.8  deg C/W
JC thermal resistance
Junction-to-case (bottom DRAIN pad)
R (bot_DRAIN) 4.6  deg C/W
JC thermal resistance
(1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application
report.
6.5.2 TPS25751S - Thermal Information
TPS25751S
THERMAL METRIC(1) QFN UNIT
32 PINS
R Junction-to-ambient thermal resistance 30.5  deg C/W
JA
R (top) Junction-to-case (top) thermal resistance 24.5  deg C/W
JC
Junction-to-board (bottom) thermal
R 2  deg C/W
JC resistance
R Junction-to-board thermal resistance 9.8  deg C/W
JB
 Junction-to-top characterization parameter 0.2  deg C/W
JT
Junction-to-board characterization
 9.7  deg C/W
JB parameter
(1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application
report.
10 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 11

#### Extracted tables

Table 1:

```text
PARAMETER |  | TEST CONDITIONS | MIN | TYP | MAX | UNIT
VIN_3V3, VBUS |  |  |  |  |  | 
V VBUS_UVLO | VBUS UVLO threshold | rising | 3.6 3.9 |  |  | V
 |  | falling | 3.5 3.8 |  |  | 
 |  | hysteresis | 0.1 |  |  | 
V VIN3V3_UVLO | Voltage required on VIN_3V3 for power on | rising, V = 0 VBUS | 2.56 2.66 2.76 |  |  | V
 |  | falling, V = 0 VBUS | 2.44 2.54 2.64 |  |  | 
 |  | hysteresis | 0.12 |  |  | 
LDO_3V3, LDO_1V5 |  |  |  |  |  | 
V LDO_3V3 | Voltage on LDO_3V3 | V = 0 V, 10 uA <= I <= VIN_3V3 LOAD 18 mA, >= 3.9 V VBUS | 3.0 3.4 3.6 |  |  | V
R LDO_3V3 | Rdson of VIN_3V3 to LDO_3V3 | I = 50 mA LDO_3V3 | 1.4 |  |  | Ohm
V LDO_1V5 | Voltage on LDO_1V5 | up to maximum internal loading condition | 1.49 1.5 1.65 |  |  | V
```

Table 2:

```text
PARAMETER |  | TEST CONDITIONS | MIN | TYP | MAX | UNIT
I VIN_3V3,ActSrc | Current into VIN_3V3 | Active Source mode: V = 5.0 V, V = 3.3 V VBUS VIN_3V3 | 3 |  |  | mA
I VIN_3V3,ActSnk | Current into VIN_3V3 | Active Sink mode: 22 V >= V >= 4.0 V, V = 3.3 V VBUS VIN_3V3 | 3 6 |  |  | mA
I VIN_3V3,IdlSrc | Current into VIN_3V3 | Idle Source mode: V = 5.0 V, V = 3.3 V VBUS VIN_3V3 | 1.0 |  |  | mA
I VIN_3V3,IdlSnk | Current into VIN_3V3 | Idle Sink mode: 22 V >= V >= 4.0 V, V = 3.3 V VBUS VIN_3V3 | 1.0 |  |  | mA
P MstbySnk | Power drawn into PP5V and VIN_3V3 in Modern Standby Sink Mode | CCm floating, V = 0.4 V, V = 5 V, V = 3.3 V, CCn PP5V VIN_3V3 V = 5.0 V, GATE_VBUS, GATE_VSYS disabled, and T VBUS J = 25 deg C | 4.1 |  |  | mW
P MstbySrc | Power drawn into PP5V and VIN_3V3 in Modern Standby Source Mode | CCm floating, CCn tied to GND through 5.1 kOhm, V = 5 PP5V V, V = 3.3 V, I = 0, T = 25 deg C VIN_3V3 VBUS J | 4.5 |  |  | mW
I PP5V,Sleep | Current into PP5V | Sleep mode: V = 0 V, V = 3.3 V PA_VBUS VIN_3V3 | 2 |  |  | uA
I VIN_3V3,Sleep | Current into VIN_3V3 | Sleep mode: V = 0 V, V = 3.3 V VBUS VIN_3V3 | 56 |  |  | uA
```

Table 3:

```text
PARAMETER |  | TEST CONDITIONS | MIN | TYP | MAX | UNIT
R PP_5V | Resistance from PP5V to VBUS | I = 3 A, T = 25 deg C LOAD J | 36 38 |  |  | mOhm
R PP_5V | Resistance from PP5V to VBUS | I = 3 A,T = 125 deg C LOAD J | 36 53 |  |  | mOhm
I PP5V_REV | VBUS to PP5V leakage current | V = 0 V, V = 5.5 V, PP5V VBUS PP_5V disabled, T <= 85 deg C, J measure I PP5V | 5 |  |  | uA
I PP5V_FWD | PP5V to VBUS leakage current | V = 5.5 V, V = 0 V, PP5V VBUS PP_5V disabled, T <= 85 deg C, J measure I VBUS | 15 |  |  | uA
I LIM5V | Current limit setting | Configure to setting 0 | 1.15 1.36 |  |  | A
I LIM5V | Current limit setting | Configure to setting 1 | 1.61 1.90 |  |  | A
I LIM5V | Current limit setting |  | 2.3 2.70 |  |  | A
I LIM5V | Current limit setting | Configure to setting 3 | 3.04 3.58 |  |  | A
I LIM5V | Current limit setting | Configure to setting 4 | 3.22 3.78 |  |  | A
```

#### Raw extracted text

```text
TPS25751
www.ti.com SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
6.6 Power Supply Characteristics
Operating under these conditions unless otherwise noted: 3.0 V <= V <= 3.6 V
VIN_3V3
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
VIN_3V3, VBUS
rising 3.6 3.9
V VBUS UVLO threshold falling 3.5 3.8 V
VBUS_UVLO
hysteresis 0.1
rising, V = 0 2.56 2.66 2.76
VBUS
Voltage required on VIN_3V3 for
V falling, V = 0 2.44 2.54 2.64 V
VIN3V3_UVLO power on VBUS
hysteresis 0.12
LDO_3V3, LDO_1V5
V = 0 V, 10 uA <= I <=
V Voltage on LDO_3V3 VIN_3V3 LOAD 3.0 3.4 3.6 V
LDO_3V3 18 mA, >= 3.9 V
VBUS
R Rdson of VIN_3V3 to LDO_3V3 I = 50 mA 1.4 Ohm
LDO_3V3 LDO_3V3
up to maximum internal loading
V Voltage on LDO_1V5 1.49 1.5 1.65 V
LDO_1V5 condition
6.7 Power Consumption
Operating under these conditions unless otherwise noted: 3.0 V <= V <= 3.6 V, no GPIO loading
VIN_3V3
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
I Current into VIN_3V3 Active Source mode: V = 5.0 V, V = 3.3 V 3 mA
VIN_3V3,ActSrc VBUS VIN_3V3
I Current into VIN_3V3 Active Sink mode: 22 V >= V >= 4.0 V, V = 3.3 V 3 6 mA
VIN_3V3,ActSnk VBUS VIN_3V3
I Current into VIN_3V3 Idle Source mode: V = 5.0 V, V = 3.3 V 1.0 mA
VIN_3V3,IdlSrc VBUS VIN_3V3
I Current into VIN_3V3 Idle Sink mode: 22 V >= V >= 4.0 V, V = 3.3 V 1.0 mA
VIN_3V3,IdlSnk VBUS VIN_3V3
Power drawn into PP5V CCm floating, V = 0.4 V, V = 5 V, V = 3.3 V,
CCn PP5V VIN_3V3
P and VIN_3V3 in Modern V = 5.0 V, GATE_VBUS, GATE_VSYS disabled, and T 4.1 mW
MstbySnk VBUS J
Standby Sink Mode = 25 deg C
Power drawn into PP5V
CCm floating, CCn tied to GND through 5.1 kOhm, V = 5
P and VIN_3V3 in Modern PP5V 4.5 mW
MstbySrc V, V = 3.3 V, I = 0, T = 25 deg C
Standby Source Mode VIN_3V3 VBUS J
I Current into PP5V Sleep mode: V = 0 V, V = 3.3 V 2 uA
PP5V,Sleep PA_VBUS VIN_3V3
I Current into VIN_3V3 Sleep mode: V = 0 V, V = 3.3 V 56 uA
VIN_3V3,Sleep VBUS VIN_3V3
6.8 PP_5V Power Switch Characteristics
Operating under these conditions unless otherwise noted: 3.0 V <= V <= 3.6 V
VIN_3V3
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
R Resistance from PP5V to VBUS I = 3 A, T = 25 deg C 36 38 mOhm
PP_5V LOAD J
R Resistance from PP5V to VBUS I = 3 A,T = 125 deg C 36 53 mOhm
PP_5V LOAD J
V = 0 V, V = 5.5 V,
PP5V VBUS
I VBUS to PP5V leakage current PP_5V disabled, T <= 85 deg C, 5 uA
PP5V_REV J
measure I
PP5V
V = 5.5 V, V = 0 V,
PP5V VBUS
I PP5V to VBUS leakage current PP_5V disabled, T <= 85 deg C, 15 uA
PP5V_FWD J
measure I
VBUS
I Current limit setting Configure to setting 0 1.15 1.36 A
LIM5V
I Current limit setting Configure to setting 1 1.61 1.90 A
LIM5V
I Current limit setting 2.3 2.70 A
LIM5V
I Current limit setting Configure to setting 3 3.04 3.58 A
LIM5V
I Current limit setting Configure to setting 4 3.22 3.78 A
LIM5V
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 11
Product Folder Links: TPS25751
```

### Page 12

#### Extracted tables

Table 1:

```text
PARAMETER |  | TEST CONDITIONS | MIN | TYP | MAX | UNIT
I VBUS | PP5V to VBUS current sense accuracy | 3.64 A >= I >= 1 A VBUS | 3.05 3.5 3.75 |  |  | A/V
V PP_5V_RCP | RCP clears and PP_5V starts turning on when V - V < VBUS PP5V V . Measure V - V PP_5V_RCP VBUS PP5V |  | 10 20 |  |  | mV
t iOS_PP_5V | Response time to VBUS short circuit | VBUS to GND through 10 mOhm, C = 0 VBUS | 1.15 |  |  | us
t PP_5V_ovp | Response time to V > V VBUS OVP4RCP | Enable PP_5V, I RpDef being drawn from PP5V, configure V to OVP4RCP setting 2, ramp V from VBUS 4V to 20 V at 100 V/ms, C = 2.5 uF, measure PP5V time from OVP detection until reverse current < 100 mA | 4.5 |  |  | us
t PP_5V_uvlo | Response time to V < PP5V V , PP_VBUS is deemed off PP5V_UVLO when V < 0.8 V VBUS | R = 100 Ohm, no external L capacitance on VBUS | 4 |  |  | us
t PP_5V_rcp | Response time to V < V + PP5V VBUS V PP_5V_RCP | V = 5.5 V, I being PP5V RpDef drawn from PP5V, enable PP_5V, configure V OVP4RCP to setting 2, ramp V VBUS from 4 V to 21.5 V at 10 V/us, measure V . PP5V C = 104 uF, C =10 PP5V VBUS uF, measure time from RCP detection until reverse current < 100 mA | 0.7 |  |  | us
t ILIM | Current clamping deglitch time |  | 5.1 |  |  | ms
t ON | From enable signal to VBUS at 90% of final value | R = 100 Ohm, V = 5 V, L PP5V C = 0 L | 2.3 3.3 4.3 |  |  | ms
t OFF | From disable signal to VBUS at 10% of final value | R = 100 Ohm, V = 5 V, L PP5V C = 0 L | 0.30 0.45 0.6 |  |  | ms
t RISE | VBUS from 10% to 90% of final value | R = 100 Ohm, V = 5 V, L PP5V C = 0 L | 1.2 1.7 2.2 |  |  | ms
t FALL | VBUS from 90% to 10% of initial value | R = 100 Ohm, V = 5 V, L PP5V C = 0 L | 0.06 0.1 0.14 |  |  | ms
```

Table 2:

```text
PARAMETER |  | TEST CONDITIONS | MIN | TYP | MAX | UNIT
V RCP | Comparator mode RCP threshold, V - V PPHV VBUS | Setting 0, 4 V <= V <= 22 VBUS V, V <= 3.63 V VIN_3V3 | 2 6 10 |  |  | mV
 |  | setting 1, 4 V <= V <= 22 VBUS V, V <= 3.63 V VIN_3V3 | 4 8 12 |  |  | mV
 |  | Setting 2, 4 V <= V <= 22 VBUS V, V <= 3.63 V VIN_3V3 | 6 10 14 |  |  | mV
 |  | Setting 3, 4 V <= V <= 22 VBUS V, V <= 3.63 V VIN_3V3 | 8 12 16 |  |  | mV
```

#### Raw extracted text

```text
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024 www.ti.com
6.8 PP_5V Power Switch Characteristics (continued)
Operating under these conditions unless otherwise noted: 3.0 V <= V <= 3.6 V
VIN_3V3
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
PP5V to VBUS current sense
I 3.64 A >= I >= 1 A 3.05 3.5 3.75 A/V
VBUS accuracy VBUS
RCP clears and PP_5V starts
V turning on when V - V < 10 20 mV
PP_5V_RCP VBUS PP5V
V . Measure V - V
PP_5V_RCP VBUS PP5V
VBUS to GND through 10
t Response time to VBUS short circuit 1.15 us
iOS_PP_5V mOhm, C = 0
VBUS
Enable PP_5V, I
RpDef
being drawn from PP5V,
configure V to
OVP4RCP
setting 2, ramp V from
VBUS
t Response time to V > V 4V to 20 V at 100 V/ms, 4.5 us
PP_5V_ovp VBUS OVP4RCP
C = 2.5 uF, measure
PP5V
time from OVP detection
until reverse current < 100
mA
Response time to V <
PP5V R = 100 Ohm, no external
t V , PP_VBUS is deemed off L 4 us
PP_5V_uvlo PP5V_UVLO capacitance on VBUS
when V < 0.8 V
VBUS
V = 5.5 V, I being
PP5V RpDef
drawn from PP5V, enable
PP_5V, configure V
OVP4RCP
to setting 2, ramp V
VBUS
Response time to V < V + from 4 V to 21.5 V at
t PP5V VBUS 0.7 us
PP_5V_rcp V 10 V/us, measure V .
PP_5V_RCP PP5V
C = 104 uF, C =10
PP5V VBUS
uF, measure time from
RCP detection until reverse
current < 100 mA
t Current clamping deglitch time 5.1 ms
ILIM
From enable signal to VBUS at 90% R = 100 Ohm, V = 5 V,
t L PP5V 2.3 3.3 4.3 ms
ON of final value C = 0
L
From disable signal to VBUS at 10% R = 100 Ohm, V = 5 V,
t L PP5V 0.30 0.45 0.6 ms
OFF of final value C = 0
L
R = 100 Ohm, V = 5 V,
t VBUS from 10% to 90% of final value L PP5V 1.2 1.7 2.2 ms
RISE C = 0
L
VBUS from 90% to 10% of initial R = 100 Ohm, V = 5 V,
t L PP5V 0.06 0.1 0.14 ms
FALL value C = 0
L
6.9 PPHV Power Switch Characteristics - TPS25751D
Operating under these conditions unless otherwise noted: 3.0 V <= V <= 3.6 V
VIN_3V3
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
Setting 0, 4 V <= V <= 22
VBUS 2 6 10 mV
V, V <= 3.63 V
VIN_3V3
setting 1, 4 V <= V <= 22
VBUS 4 8 12 mV
Comparator mode RCP threshold, V, V VIN_3V3 <= 3.63 V
V
RCP V PPHV - V VBUS Setting 2, 4 V <= V VBUS <= 22 6 10 14 mV
V, V <= 3.63 V
VIN_3V3
Setting 3, 4 V <= V <= 22
VBUS 8 12 16 mV
V, V <= 3.63 V
VIN_3V3
12 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 13

#### Extracted tables

Table 1:

```text
PARAMETER |  | TEST CONDITIONS | MIN | TYP | MAX | UNIT
SS | Soft start slew rate for GATE_VSYS, setting 0 | 4 V <= V <= 22 V, VBUS I = 100 mA, 500 pF LOAD < C < 16 nF, GATE_VSYS measure slope from 10% to 90% of final VSYS value | 0.35 0.41 0.47 |  |  | V/ms
 | Soft start slew rate for GATE_VSYS, setting 1 | 4 V <= V <= 22 V, VBUS I = 100 mA, 500 pF LOAD < C < 16 nF, GATE_VSYS measure slope from 10% to 90% of final VSYS value | 0.67 0.81 0.95 |  |  | 
 | Soft start slew rate for GATE_VSYS, setting 2 | 4 V <= V <= 22 V, VBUS I = 100 mA, 500 pF LOAD < C < 16 nF, GATE_VSYS measure slope from 10% to 90% of final VSYS value | 1.33 1.7 2.0 |  |  | 
 | Soft start slew rate for GATE_VSYS, setting 3 | 4 V <= V <= 22 V, VBUS I = 100 mA, 500 pF LOAD < C < 16 nF, GATE_VSYS measure slope from 10% to 90% of final VSYS value | 2.8 3.3 3.80 |  |  |
```

Table 2:

```text
PARAMETER |  | TEST CONDITIONS | MIN | TYP | MAX | UNIT
V RCP | Comparator mode RCP threshold, V - V VSYS VBUS | Setting 0, 4 V <= V <= 22 VBUS V, V <= 3.63 V VIN_3V3 | 2 6 10 |  |  | mV
 |  | Setting 1, 4 V <= V <= 22 VBUS V, V <= 3.63 V VIN_3V3 | 4 8 12 |  |  | mV
 |  | Setting 2, 4 V <= V <= 22 VBUS V, V <= 3.63 V VIN_3V3 | 6 10 14 |  |  | mV
 |  | Setting 3, 4 V <= V <= 22 VBUS V, V <= 3.63 V VIN_3V3 | 8 12 16 |  |  | mV
SS | Soft start slew rate for GATE_VSYS, setting 0 | 4 V <= V <= 22 V, VBUS I = 100 mA, 500 pF LOAD < C < 16 nF, GATE_VSYS measure slope from 10% to 90% of final VSYS value | 0.35 0.41 0.47 |  |  | V/ms
 | Soft start slew rate for GATE_VSYS, setting 1 | 4 V <= V <= 22 V, VBUS I = 100 mA, 500 pF LOAD < C < 16 nF, GATE_VSYS measure slope from 10% to 90% of final VSYS value | 0.67 0.81 0.91 |  |  | 
 | Soft start slew rate for GATE_VSYS, setting 2 | 4 V <= V <= 22 V, VBUS I = 100 mA, 500 pF LOAD < C < 16 nF, GATE_VSYS measure slope from 10% to 90% of final VSYS value | 1.33 1.7 1.80 |  |  | 
 | Soft start slew rate for GATE_VSYS, setting 3 | 4 V <= V <= 22 V, VBUS I = 100 mA, 500 pF LOAD < C < 16 nF, GATE_VSYS measure slope from 10% to 90% of final VSYS value | 2.8 3.3 3.80 |  |  |
```

#### Raw extracted text

```text
TPS25751
www.ti.com SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
6.9 PPHV Power Switch Characteristics - TPS25751D (continued)
Operating under these conditions unless otherwise noted: 3.0 V <= V <= 3.6 V
VIN_3V3
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
4 V <= V <= 22 V,
VBUS
I = 100 mA, 500 pF
Soft start slew rate for GATE_VSYS, LOAD
< C < 16 nF, 0.35 0.41 0.47
setting 0 GATE_VSYS
measure slope from 10% to
90% of final VSYS value
4 V <= V <= 22 V,
VBUS
I = 100 mA, 500 pF
Soft start slew rate for GATE_VSYS, LOAD
< C < 16 nF, 0.67 0.81 0.95
setting 1 GATE_VSYS
measure slope from 10% to
90% of final VSYS value
SS V/ms
4 V <= V <= 22 V,
VBUS
I = 100 mA, 500 pF
Soft start slew rate for GATE_VSYS, LOAD
< C < 16 nF, 1.33 1.7 2.0
setting 2 GATE_VSYS
measure slope from 10% to
90% of final VSYS value
4 V <= V <= 22 V,
VBUS
I = 100 mA, 500 pF
Soft start slew rate for GATE_VSYS, LOAD
< C < 16 nF, 2.8 3.3 3.80
setting 3 GATE_VSYS
measure slope from 10% to
90% of final VSYS value
6.10 PP_EXT Power Switch Characteristics - TPS25751S
Operating under these conditions unless otherwise noted: , 3.0 V <= V <= 3.6 V
VIN_3V3
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
Setting 0, 4 V <= V <= 22
VBUS 2 6 10 mV
V, V <= 3.63 V
VIN_3V3
Setting 1, 4 V <= V <= 22
VBUS 4 8 12 mV
Comparator mode RCP threshold, V, V VIN_3V3 <= 3.63 V
V
RCP V VSYS - V VBUS Setting 2, 4 V <= V VBUS <= 22 6 10 14 mV
V, V <= 3.63 V
VIN_3V3
Setting 3, 4 V <= V <= 22
VBUS 8 12 16 mV
V, V <= 3.63 V
VIN_3V3
4 V <= V <= 22 V,
VBUS
I = 100 mA, 500 pF
Soft start slew rate for GATE_VSYS, LOAD
< C < 16 nF, 0.35 0.41 0.47
setting 0 GATE_VSYS
measure slope from 10% to
90% of final VSYS value
4 V <= V <= 22 V,
VBUS
I = 100 mA, 500 pF
Soft start slew rate for GATE_VSYS, LOAD
< C < 16 nF, 0.67 0.81 0.91
setting 1 GATE_VSYS
measure slope from 10% to
90% of final VSYS value
SS V/ms
4 V <= V <= 22 V,
VBUS
I = 100 mA, 500 pF
Soft start slew rate for GATE_VSYS, LOAD
< C < 16 nF, 1.33 1.7 1.80
setting 2 GATE_VSYS
measure slope from 10% to
90% of final VSYS value
4 V <= V <= 22 V,
VBUS
I = 100 mA, 500 pF
Soft start slew rate for GATE_VSYS, LOAD
< C < 16 nF, 2.8 3.3 3.80
setting 3 GATE_VSYS
measure slope from 10% to
90% of final VSYS value
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 13
Product Folder Links: TPS25751
```

### Page 14

#### Extracted tables

Table 1:

```text
PARAMETER |  | TEST CONDITIONS | MIN | TYP | MAX | UNIT
V OVP4RCP | VBUS overvoltage protection for RCP programmable range | OVP detected when V > VBUS V OVP4RCP | 5.0 24 |  |  | V
V OVP4RCPH | Hysteresis |  | 1.75 2 2.25 |  |  | %
r OVP | Ratio of OVP4RCP input used for OVP4VSYS comparator. r x OVP V = V OVP4VSYS OVP4RCP | setting 0 | 1 |  |  | V/V
 |  | setting 1 | 0.95 |  |  | V/V
 |  | setting 2 | 0.90 |  |  | V/V
 |  | setting 3 | 0.875 |  |  | V/V
V OVP4VSYS | VBUS overvoltage protection range for VSYS protection | OVP detected when r x OVP V > V VBUS OVP4RCP | 5 27.5 |  |  | V
V OVP4VSYS | Hysteresis | VBUS falling, % of V , r setting 0 OVP4VSYS OVP | 1.75 2 2.25 |  |  | %
 |  | VBUS falling, % of V , r setting 1 OVP4VSYS OVP | 1.8 2.1 2.4 |  |  | 
 |  | VBUS falling, % of V , r setting 2 OVP4VSYS OVP | 1.9 2.2 2.5 |  |  | 
 |  | VBUS falling, % of V , r setting 3 OVP4VSYS OVP | 2 2.3 2.6 |  |  | 
V PP5V_UVLO | Voltage required on PP5V | rising | 3.9 4.1 4.3 |  |  | V
 |  | falling | 3.8 4.0 4.2 |  |  | 
 |  | hysteresis | 0.1 |  |  | 
I DSCH | VBUS discharge current | V = 22 V, measure VBUS I VBUS | 4 15 |  |  | mA
```

Table 2:

```text
PARAMETER |  | TEST CONDITIONS | MIN | TYP | MAX | UNIT
Type-C Source (Rp pullup) |  |  |  |  |  | 
V OC_3.3 | Unattached CCy open circuit voltage while Rp enabled, no load | V > 2.302 V, R = 47 kOhm LDO_3V3 CC | 1.85 |  |  | V
V OC_5 | Attached CCy open circuit voltage while Rp enabled, no load | V > 3.802 V, R = 47 kOhm PP5V CC | 2.95 |  |  | V
I Rev | Unattached reverse current on CCy | V = 5.5 V, V = 0 V, CCy CCx V < V < 3.6 LDO_3V3_UVLO LDO_3V3 V, V = 3.8 V, measure current PP5V into CCy | 10 |  |  | uA
 |  | V = 5.5 V, V = 0 V, CCy CCx V < V < 3.6 V, LDO_3V3_UVLO LDO_3V3 V = 0, T <= 85 deg C, measure PP5V J current into CCy | 10 |  |  | 
I RpDef | Current source - USB Default | 0 < V < 1.0 V, measure I CCy CCy | 64 80 96 |  |  | uA
I Rp1.5 | Current source - 1.5 A | 4.75 V < V < 5.5 V, 0 < V < PP5V CCy 1.5 V, measure I CCy | 166 180 194 |  |  | uA
I Rp3.0 | Current source - 3.0 A | 4.75 V < V < 5.5 V, 0 < V < PP5V CCy 2.45 V, measure I CCy | 304 330 356 |  |  | uA
Type-C Sink (Rd pulldown) |  |  |  |  |  | 
V SNK1 | Open/Default detection threshold when Rd applied to CCy | rising | 0.2 0.24 |  |  | V
```

#### Raw extracted text

```text
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024 www.ti.com
6.11 Power Path Supervisory
Operating under these conditions unless otherwise noted: 3.0 V <= V <= 3.6 V
VIN_3V3
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
VBUS overvoltage protection for RCP OVP detected when V >
V VBUS 5.0 24 V
OVP4RCP programmable range V
OVP4RCP
V Hysteresis 1.75 2 2.25 %
OVP4RCPH
setting 0 1 V/V
Ratio of OVP4RCP input used setting 1 0.95 V/V
r for OVP4VSYS comparator. r x
OVP OVP
V = V setting 2 0.90 V/V
OVP4VSYS OVP4RCP
setting 3 0.875 V/V
VBUS overvoltage protection range for OVP detected when r x
V OVP 5 27.5 V
OVP4VSYS VSYS protection V > V
VBUS OVP4RCP
VBUS falling, % of
1.75 2 2.25
V , r setting 0
OVP4VSYS OVP
VBUS falling, % of
1.8 2.1 2.4
V , r setting 1
OVP4VSYS OVP
V Hysteresis %
OVP4VSYS
VBUS falling, % of
1.9 2.2 2.5
V , r setting 2
OVP4VSYS OVP
VBUS falling, % of
2 2.3 2.6
V , r setting 3
OVP4VSYS OVP
rising 3.9 4.1 4.3
V Voltage required on PP5V falling 3.8 4.0 4.2 V
PP5V_UVLO
hysteresis 0.1
V = 22 V, measure
I VBUS discharge current VBUS 4 15 mA
DSCH I
VBUS
6.12 CC Cable Detection Parameters
Operating under these conditions unless otherwise noted: 3.0 V <= V <= 3.6 V
VIN_3V3
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
Type-C Source (Rp pullup)
Unattached CCy open circuit
V V > 2.302 V, R = 47 kOhm 1.85 V
OC_3.3 voltage while Rp enabled, no load LDO_3V3 CC
Attached CCy open circuit voltage
V V > 3.802 V, R = 47 kOhm 2.95 V
OC_5 while Rp enabled, no load PP5V CC
V = 5.5 V, V = 0 V,
CCy CCx
V < V < 3.6
LDO_3V3_UVLO LDO_3V3 10
V, V = 3.8 V, measure current
PP5V
Unattached reverse current on into CCy
I uA
Rev CCy V = 5.5 V, V = 0 V,
CCy CCx
V < V < 3.6 V,
LDO_3V3_UVLO LDO_3V3 10
V = 0, T <= 85 deg C, measure
PP5V J
current into CCy
I Current source - USB Default 0 < V < 1.0 V, measure I 64 80 96 uA
RpDef CCy CCy
4.75 V < V < 5.5 V, 0 < V <
I Current source - 1.5 A PP5V CCy 166 180 194 uA
Rp1.5 1.5 V, measure I
CCy
4.75 V < V < 5.5 V, 0 < V <
I Current source - 3.0 A PP5V CCy 304 330 356 uA
Rp3.0 2.45 V, measure I
CCy
Type-C Sink (Rd pulldown)
Open/Default detection threshold
V rising 0.2 0.24 V
SNK1 when Rd applied to CCy
14 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 15

#### Extracted tables

Table 1:

```text
PARAMETER |  | TEST CONDITIONS | MIN | TYP | MAX | UNIT
V SNK1 | Open/Default detection threshold when Rd applied to CCy | falling | 0.16 0.20 |  |  | V
 | Hysteresis |  | 0.04 |  |  | V
V SNK2 | Default/1.5-A detection threshold | falling | 0.62 0.68 |  |  | V
V SNK2 | Default/1.5-A detection threshold | rising | 0.63 0.66 0.69 |  |  | V
 | Hysteresis |  | 0.01 |  |  | V
V SNK3 | 1.5-A/3.0-A detection threshold when Rd applied to CCy | falling | 1.17 1.25 |  |  | V
V SNK3 | 1.5-A/3.0-A detection threshold when Rd applied to CCy | rising | 1.22 1.3 |  |  | V
 | Hysteresis |  | 0.05 |  |  | V
R SNK | Rd pulldown resistance | 0.25 V <= V <= 2.1 V, measure CCy resistance on CCy | 4.6 5.6 |  |  | kOhm
R VCONN_DIS | VCONN discharge resistance | 0V <= V <= 5.5 V, measure CCy resistance on CCy | 4.0 6.12 |  |  | kOhm
V CLAMP | Dead battery Rd clamp | V = 0 V, 64 uA < I < 96 VIN_3V3 CCy uA | 0.25 1.32 |  |  | V
 |  | V = 0 V, 166 uA < I < VIN_3V3 CCy 194 uA | 0.65 1.32 |  |  | 
 |  | V = 0 V, 304 uA < I < VIN_3V3 CCy 356 uA | 1.20 2.18 |  |  | 
R Open | Resistance from CCy to GND when configured as open | V = 0, V = 3.3 V, V VBUS VIN_3V3 CCy = 5 V, measure resistance on CCy | 500 |  |  | kOhm
 |  | V = 5 V, V = 0, V = VBUS VIN_3V3 CCy 5 V, measure resistance on CCy | 500 |  |  | kOhm
```

Table 2:

```text
PARAMETER |  | TEST CONDITIONS | MIN | TYP | MAX | UNIT
R PP_CABLE | Rdson of the VCONN path | V = 5 V, I = 250 mA, PP5V L measure resistance from PP5V to CCy | 1.2 |  |  | Ohm
I LIMVC | Short circuit current limit | Setting 0, V = 5 V, R =10 PP5V L mOhm, measure I CCy | 350 410 470 |  |  | mA
I LIMVC | Short circuit current limit | Setting 1, V = 5 V, R =10 PP5V L mOhm, measure I CCy | 540 600 660 |  |  | mA
I CC2PP5V | Reverse leakage current through VCONN FET | VCONN disabled, T <= 85 deg C, J V = 5.5 V, V = 0 V, CCy PP5V V = 5 V, LDO forced to VBUS draw from VBUS, measure I CCy | 10 |  |  | uA
V VC_OVP | Overvoltage protection threshold for PP_CABLE | V rising PP5V | 5.6 5.9 6.2 |  |  | V
V VC_RCP | Reverse current protection threshold for PP_CABLE, sourcing VCONN through CCx | V >= 4.9 V, V = V , PP5V CCy PP5V V rising CCx | 60 200 340 |  |  | mV
 |  | V >= 4.9 V, V <= 4 V, V PP5V CCy CCx rising | 210 340 470 |  |  | mV
t VCILIM | Current clamp deglitch time |  | 1.3 |  |  | ms
t PP_CABLE_FSD | Time to disable PP_CABLE after V > V or V - PP5V VC_OVP CCx V > V PP5V VC_RCP | C = 0 L | 0.5 |  |  | us
```

#### Raw extracted text

```text
TPS25751
www.ti.com SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
6.12 CC Cable Detection Parameters (continued)
Operating under these conditions unless otherwise noted: 3.0 V <= V <= 3.6 V
VIN_3V3
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
Open/Default detection threshold
falling 0.16 0.20 V
V when Rd applied to CCy
SNK1
Hysteresis 0.04 V
V Default/1.5-A detection threshold falling 0.62 0.68 V
SNK2
Default/1.5-A detection threshold rising 0.63 0.66 0.69 V
V
SNK2
Hysteresis 0.01 V
1.5-A/3.0-A detection threshold
V falling 1.17 1.25 V
SNK3 when Rd applied to CCy
1.5-A/3.0-A detection threshold
rising 1.22 1.3 V
V when Rd applied to CCy
SNK3
Hysteresis 0.05 V
0.25 V <= V <= 2.1 V, measure
R Rd pulldown resistance CCy 4.6 5.6 kOhm
SNK resistance on CCy
0V <= V <= 5.5 V, measure
R VCONN discharge resistance CCy 4.0 6.12 kOhm
VCONN_DIS resistance on CCy
V = 0 V, 64 uA < I < 96
VIN_3V3 CCy 0.25 1.32
uA
V = 0 V, 166 uA < I <
V Dead battery Rd clamp VIN_3V3 CCy 0.65 1.32 V
CLAMP 194 uA
V = 0 V, 304 uA < I <
VIN_3V3 CCy 1.20 2.18
356 uA
V = 0, V = 3.3 V, V
VBUS VIN_3V3 CCy 500 kOhm
Resistance from CCy to GND = 5 V, measure resistance on CCy
R
Open when configured as open V = 5 V, V = 0, V =
VBUS VIN_3V3 CCy 500 kOhm
5 V, measure resistance on CCy
6.13 CC VCONN Parameters
Operating under these conditions unless otherwise noted: 3.0 V <= V <= 3.6 V
VIN_3V3
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
V = 5 V, I = 250 mA,
PP5V L
R Rdson of the VCONN path measure resistance from PP5V 1.2 Ohm
PP_CABLE
to CCy
Setting 0, V = 5 V, R =10
I Short circuit current limit PP5V L 350 410 470 mA
LIMVC mOhm, measure I
CCy
Setting 1, V = 5 V, R =10
I Short circuit current limit PP5V L 540 600 660 mA
LIMVC mOhm, measure I
CCy
VCONN disabled, T <= 85 deg C,
J
Reverse leakage current V = 5.5 V, V = 0 V,
I CCy PP5V 10 uA
CC2PP5V through VCONN FET V = 5 V, LDO forced to
VBUS
draw from VBUS, measure I
CCy
Overvoltage protection
V V rising 5.6 5.9 6.2 V
VC_OVP threshold for PP_CABLE PP5V
V >= 4.9 V, V = V ,
Reverse current protection V PP5V rising CCy PP5V 60 200 340 mV
CCx
V threshold for PP_CABLE,
VC_RCP
sourcing VCONN through CCx V PP5V >= 4.9 V, V CCy <= 4 V, V CCx 210 340 470 mV
rising
t Current clamp deglitch time 1.3 ms
VCILIM
Time to disable PP_CABLE
t after V > V or V - C = 0 0.5 us
PP_CABLE_FSD PP5V VC_OVP CCx L
V > V
PP5V VC_RCP
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 15
Product Folder Links: TPS25751
```

### Page 16

#### Extracted tables

Table 1:

```text
PARAMETER |  | TEST CONDITIONS | MIN | TYP | MAX | UNIT
t PP_CABLE_off | From disable signal to CCy at 10% of final value | I = 250 mA, V = 5 V, C = L PP5V L 0 | 100 200 300 |  |  | us
t iOS_PP_CABLE | Response time to short circuit | V = 5 V, for short circuit R PP5V L = 10 mOhm | 2 |  |  | us
```

Table 2:

```text
PARAMETER |  | TEST CONDITIONS | MIN | TYP | MAX | UNIT
Transmitter |  |  |  |  |  | 
V TXHI | Transmit high voltage on CCy | Standard External load | 1.05 1.125 1.2 |  |  | V
V TXLO | Transmit low voltage on CCy | Standard External load | 75 75 |  |  | mV
Z DRIVER | Transmit output impedance while driving the CC line using CCy | measured at 750 kHz | 33 54 75 |  |  | Ohm
t Rise | Rise time. 10 % to 90 % amplitude points on CCy, minimum is under an unloaded condition. Maximum set by TX mask | C = 520 pF CCy | 300 |  |  | ns
t Fall | Fall time. 90 % to 10 % amplitude points on CCy, minimum is under an unloaded condition. Maximum set by TX mask | C = 520 pF CCy | 300 |  |  | ns
V PHY_OVP | OVP detection threshold for USB PD PHY | 0 <= V <= 3.6 V, 0 <= V <= VIN_3V3 PP5V 5.5 V, V >= 4 V. Initially V <= VBUS CC1 5.5 V and V <= 5.5 V, then V CC2 CCx rises | 5.5 8.5 |  |  | V
Receiver |  |  |  |  |  | 
Z BMCRX | Receiver input impedance on CCy | Does not include pullup or pulldown resistance from cable detect. Transmitter is Hi-Z | 1 |  |  | MOhm
C CC | Receiver capacitance on CCy(1) | Capacitance looking into the CC pin when in receiver mode | 120 |  |  | pF
V RX_SNK_R | Rising threshold on CCy for receiver comparator | Sink mode (rising) | 499 525 551 |  |  | mV
V RX_SRC_R | Rising threshold on CCy for receiver comparator | Source mode (rising) | 784 825 866 |  |  | mV
V RX_SNK_F | Falling threshold on CCy for receiver comparator | Sink mode (falling) | 230 250 270 |  |  | mV
V RX_SRC_F | Falling threshold on CCy for receiver comparator | Source mode (falling) | 523 550 578 |  |  | mV
```

#### Raw extracted text

```text
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024 www.ti.com
6.13 CC VCONN Parameters (continued)
Operating under these conditions unless otherwise noted: 3.0 V <= V <= 3.6 V
VIN_3V3
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
From disable signal to CCy at I = 250 mA, V = 5 V, C =
t L PP5V L 100 200 300 us
PP_CABLE_off 10% of final value 0
V = 5 V, for short circuit R
t Response time to short circuit PP5V L 2 us
iOS_PP_CABLE = 10 mOhm
6.14 CC PHY Parameters
Operating under these conditions unless otherwise noted: and ( 3.0 V <= V <= 3.6 V or V >= 3.9 V )
VIN_3V3 VBUS
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
Transmitter
V Transmit high voltage on CCy Standard External load 1.05 1.125 1.2 V
TXHI
V Transmit low voltage on CCy Standard External load -75 75 mV
TXLO
Transmit output impedance while
Z measured at 750 kHz 33 54 75 Ohm
DRIVER driving the CC line using CCy
Rise time. 10 % to 90 % amplitude
points on CCy, minimum is under
t C = 520 pF 300 ns
Rise an unloaded condition. Maximum CCy
set by TX mask
Fall time. 90 % to 10 % amplitude
points on CCy, minimum is under
t C = 520 pF 300 ns
Fall an unloaded condition. Maximum CCy
set by TX mask
0 <= V <= 3.6 V, 0 <= V <=
VIN_3V3 PP5V
OVP detection threshold for USB 5.5 V, V >= 4 V. Initially V <=
V VBUS CC1 5.5 8.5 V
PHY_OVP PD PHY 5.5 V and V <= 5.5 V, then V
CC2 CCx
rises
Receiver
Does not include pullup or
Z Receiver input impedance on CCy pulldown resistance from cable 1 MOhm
BMCRX
detect. Transmitter is Hi-Z
C Receiver capacitance on CCy(1) Capacitance looking into the CC 120 pF
CC pin when in receiver mode
Rising threshold on CCy for
V Sink mode (rising) 499 525 551 mV
RX_SNK_R receiver comparator
Rising threshold on CCy for
V Source mode (rising) 784 825 866 mV
RX_SRC_R receiver comparator
Falling threshold on CCy for
V Sink mode (falling) 230 250 270 mV
RX_SNK_F receiver comparator
Falling threshold on CCy for
V Source mode (falling) 523 550 578 mV
RX_SRC_F receiver comparator
(1) C includes only the internal capacitance on a CCy pin when the pin is configured to be receiving BMC data. External capacitance
CC
is needed to meet the required minimum capacitance per the USB-PD Specifications (cReceiver). Therefore, TI recommends
adding C externally.
CCy
16 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 17

#### Extracted tables

Table 1:

```text
PARAMETER |  | TEST CONDITIONS | MIN | TYP | MAX | UNIT
T SD_MAIN | Temperature shutdown threshold | Temperature rising | 145 160 175 |  |  | deg C
 |  | Hysteresis | 15 |  |  | deg C
T SD_PP5V | Temperature controlled shutdown threshold. The power paths for each port sourcing from PP5V and PP_CABLE power paths have local sensors that disables them when the temperature is exceeded | Temperature rising | 135 150 165 |  |  | deg C
 |  | Hysteresis | 10 |  |  | deg C
```

Table 2:

```text
PARAMETER |  | TEST CONDITIONS | MIN | TYP | MAX | UNIT
LSB | Least significant bit | 3.6-V max scaling, voltage divider of 3 | 14 |  |  | mV
 |  | 25.2-V max scaling, voltage divider of 21 | 98 |  |  | mV
 |  | 4.07-A max scaling | 16.5 |  |  | mA
GAIN_ERR | Gain error | 0.05 V <= V <= 3.6 ADCINx V, V <= V ADCINx LDO_3V3 | 2.7 2.7 |  |  | %
 |  | 0.05 V <= V <= 3.6 V, V GPIOx GPIOx <= V LDO_3V3 |  |  |  | 
 |  | 2.7 V <= V <= 3.6 V LDO_3V3 | 2.4 2.4 |  |  | 
 |  | 0.6 V <= V <= 22 V VBUS | 2.1 2.1 |  |  | 
 |  | 1 A <= I <= 3 A VBUS | 2.1 2.1 |  |  | 
VOS_ERR | Offset error(1) | 0.05 V <= V <= 3.6 ADCINx V, V <= V ADCINx LDO_3V3 | 4.1 4.1 |  |  | mV
 |  | 0.05 V <= V <= 3.6 V, V GPIOx GPIOx <= V LDO_3V3 |  |  |  | 
 |  | 2.7 V <= V <= 3.6 V LDO_3V3 | 4.5 4.5 |  |  | 
 |  | 0.6 V <= V <= 22 V VBUS | 4.1 4.1 |  |  | 
 |  | 1 A <= I <= 3 A VBUS | 4.5 4.5 |  |  | mA
```

Table 3:

```text
PARAMETER |  | TEST CONDITIONS | MIN | TYP | MAX | UNIT
USB_P, USB_N |  |  |  |  |  | 
GPIO_VIH | GPIOx high-Level input voltage | V = 3.3 V LDO_3V3 | 1.3 |  |  | V
GPIO_VIL | GPIOx low-level input voltage | V = 3.3 V LDO_3V3 | 0.54 |  |  | V
GPIO_HYS | GPIOx input hysteresis voltage | V = 3.3 V LDO_3V3 | 0.09 |  |  | V
GPIO_ILKG | GPIOx leakage current | V = 3.45 V GPIOx | 1 1 |  |  | uA
GPIO_RPU | GPIOx internal pullup | Pullup enabled | 50 100 150 |  |  | kOhm
GPIO_RPD | GPIOx internal pulldown | Pulldown enabled | 50 100 150 |  |  | kOhm
GPIO_DG | GPIOx input deglitch |  | 20 50 |  |  | ns
GPIO0-7 (Outputs) |  |  |  |  |  | 
GPIO_VOH | GPIOx output high voltage | V = 3.3 V, I = -2 mA LDO_3V3 GPIOx | 2.9 |  |  | V
GPIO_VOL | GPIOx output low voltage | V = 3.3 V, I = 2 mA LDO_3V3 GPIOx | 0.4 |  |  | V
```

#### Raw extracted text

```text
TPS25751
www.ti.com SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
6.15 Thermal Shutdown Characteristics
over operating free-air temperature range (unless otherwise noted)
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
Temperature rising 145 160 175  deg C
T Temperature shutdown threshold
SD_MAIN
Hysteresis 15  deg C
Temperature controlled shutdown Temperature rising 135 150 165  deg C
threshold. The power paths for
each port sourcing from PP5V
T
SD_PP5V and PP_CABLE power paths have Hysteresis 10  deg C
local sensors that disables them
when the temperature is exceeded
6.16 ADC Characteristics
Operating under these conditions unless otherwise noted: 3.0 V <= V <= 3.6 V
VIN_3V3
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
3.6-V max scaling, voltage
14 mV
divider of 3
LSB Least significant bit 25.2-V max scaling, voltage
98 mV
divider of 21
4.07-A max scaling 16.5 mA
0.05 V <= V <= 3.6
ADCINx
V, V <= V
ADCINx LDO_3V3
-2.7 2.7
0.05 V <= V <= 3.6 V, V
GPIOx GPIOx
<= V
GAIN_ERR Gain error LDO_3V3 %
2.7 V <= V <= 3.6 V -2.4 2.4
LDO_3V3
0.6 V <= V <= 22 V -2.1 2.1
VBUS
1 A <= I <= 3 A -2.1 2.1
VBUS
0.05 V <= V <= 3.6
ADCINx
V, V <= V
ADCINx LDO_3V3
-4.1 4.1
0.05 V <= V <= 3.6 V, V
GPIOx GPIOx
VOS_ERR Offset error(1) <= V LDO_3V3 mV
2.7 V <= V <= 3.6 V -4.5 4.5
LDO_3V3
0.6 V <= V <= 22 V -4.1 4.1
VBUS
1 A <= I <= 3 A -4.5 4.5 mA
VBUS
(1) The offset error is specified after the voltage divider.
6.17 Input/Output (I/O) Characteristics
Operating under these conditions unless otherwise noted: 3.0 V <= V <= 3.6 V
VIN_3V3
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
USB_P, USB_N
GPIO_VIH GPIOx high-Level input voltage V = 3.3 V 1.3 V
LDO_3V3
GPIO_VIL GPIOx low-level input voltage V = 3.3 V 0.54 V
LDO_3V3
GPIO_HYS GPIOx input hysteresis voltage V = 3.3 V 0.09 V
LDO_3V3
GPIO_ILKG GPIOx leakage current V = 3.45 V -1 1 uA
GPIOx
GPIO_RPU GPIOx internal pullup Pullup enabled 50 100 150 kOhm
GPIO_RPD GPIOx internal pulldown Pulldown enabled 50 100 150 kOhm
GPIO_DG GPIOx input deglitch 20 50 ns
GPIO0-7 (Outputs)
GPIO_VOH GPIOx output high voltage V = 3.3 V, I = -2 mA 2.9 V
LDO_3V3 GPIOx
GPIO_VOL GPIOx output low voltage V = 3.3 V, I = 2 mA 0.4 V
LDO_3V3 GPIOx
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 17
Product Folder Links: TPS25751
```

### Page 18

#### Extracted tables

Table 1:

```text
PARAMETER |  | TEST CONDITIONS | MIN | TYP | MAX | UNIT
ADCIN1, ADCIN2 |  |  |  |  |  | 
ADCIN_ILKG | ADCINx leakage current | V <= V ADCINx LDO_3V3 | 1 1 |  |  | uA
t BOOT | Time from LDO_3V3 going high until ADCINx is read for configuration |  | 10 |  |  | ms
```

Table 2:

```text
PARAMETER |  | TEST CONDITIONS | MIN | TYP | MAX | UNIT
DATA CONTACT DETECT |  |  |  |  |  | 
I DP_SRC | DCD source current | V = 3.3 V LDO_3V3 | 7 10 13 |  |  | uA
R DM_DWN | DCD pulldown resistance | V = 3.6 V USB_N | 14.25 20 24.8 |  |  | kOhm
R DP_DWN | DCD pulldown resistance | V = 3.6 V USB_P | 14.25 20 24.8 |  |  | kOhm
V LGC_HI | Threshold for no connection | V >= V , V = 3.3 V, USB_P LGC_HI LDO_3V3 R = 300 kOhm USB_P | 2 3.6 |  |  | V
V LGC_LO | Threshold for connection | V <= V , V = 3.3 V, USB_N LGC_LO LDO_3V3 R = 24.8 kOhm USB_P | 0 0.8 |  |  | V
Advertisement and Detection |  |  |  |  |  | 
V DX_ILIM | VDX_SRC current limit |  | 250 400 |  |  | uA
I DX_SNK | Sink Current | V >= 250 mV USB_P | 25 75 125 |  |  | uA
I DX_SNK | Sink Current | V >= 250 mV USB_N | 25 75 125 |  |  | uA
R DCP_DAT | Dedicated Charging Port Resistance | 0.5 V <= V <= 0.7 V, 25 uA <= I USB_P USB_N <= 175 uA | 200 |  |  | Ohm
```

Table 3:

```text
PARAMETER |  | TEST CONDITIONS | MIN | TYP | MAX | UNIT
I2Ct_IRQ |  |  |  |  |  | 
OD_VOL_IRQ | Low level output voltage | I = 2 mA OL | 0.4 |  |  | V
OD_LKG_IRQ | Leakage Current | Output is Hi-Z, V = 3.45 V I2Cx_IRQ | 1 1 |  |  | uA
I2Cc_IRQ |  |  |  |  |  | 
IRQ_VIH | High-Level input voltage | V = 3.3 V LDO_3V3 | 1.3 |  |  | V
IRQ_VIH_THRESH | High-Level input voltage threshold | V = 3.3 V LDO_3V3 | 0.72 1.3 |  |  | V
IRQ_VIL | low-level input voltage | V = 3.3 V LDO_3V3 | 0.54 |  |  | V
IRQ_VIL_THRESH | low-level input voltage threshold | V = 3.3 V LDO_3V3 | 0.54 1.08 |  |  | V
IRQ_HYS | input hysteresis voltage | V = 3.3 V LDO_3V3 | 0.09 |  |  | V
IRQ_DEG | input deglitch |  | 20 |  |  | ns
IRQ_ILKG | I2C3m_IRQ leakage current | V = 3.45 V I2C3m_IRQ | 1 1 |  |  | uA
SDA and SCL Common Characteristics (Controller, Target) |  |  |  |  |  | 
V IL | Input low signal | V = 3.3 V LDO_3V3 | 0.54 |  |  | V
I OL | Max output low current | V = 0.4 V OL | 15 |  |  | mA
I OL | Max output low current | V = 0.6 V OL | 20 |  |  | mA
t f | Fall time from 0.7 x V to 0.3 x DD V DD | V = 1.8 V, 10 pF <= C <= 400 pF DD b | 12 80 |  |  | ns
 |  | V = 3.3 V, 10 pF <= C <= 400 pF DD b | 12 150 |  |  | ns
t SP | I2C pulse width suppressed |  | 50 |  |  | ns
```

#### Raw extracted text

```text
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024 www.ti.com
6.17 Input/Output (I/O) Characteristics (continued)
Operating under these conditions unless otherwise noted: 3.0 V <= V <= 3.6 V
VIN_3V3
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
ADCIN1, ADCIN2
ADCIN_ILKG ADCINx leakage current V <= V -1 1 uA
ADCINx LDO_3V3
Time from LDO_3V3 going
t high until ADCINx is read for 10 ms
BOOT
configuration
6.18 BC1.2 Characteristics
Operating under these conditions unless otherwise noted: 3.0 V <= V <= 3.6 V
VIN_3V3
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
DATA CONTACT DETECT
I DCD source current V = 3.3 V 7 10 13 uA
DP_SRC LDO_3V3
R DCD pulldown resistance V = 3.6 V 14.25 20 24.8 kOhm
DM_DWN USB_N
R DCD pulldown resistance V = 3.6 V 14.25 20 24.8 kOhm
DP_DWN USB_P
V >= V , V = 3.3 V,
V Threshold for no connection USB_P LGC_HI LDO_3V3 2 3.6 V
LGC_HI R = 300 kOhm
USB_P
V <= V , V = 3.3 V,
V Threshold for connection USB_N LGC_LO LDO_3V3 0 0.8 V
LGC_LO R = 24.8 kOhm
USB_P
Advertisement and Detection
V VDX_SRC current limit 250 400 uA
DX_ILIM
I Sink Current V >= 250 mV 25 75 125 uA
DX_SNK USB_P
I Sink Current V >= 250 mV 25 75 125 uA
DX_SNK USB_N
0.5 V <= V <= 0.7 V, 25 uA <= I
R Dedicated Charging Port Resistance USB_P USB_N 200 Ohm
DCP_DAT <= 175 uA
6.19 I2C Requirements and Characteristics
Operating under these conditions unless otherwise noted: 3.0 V <= V <= 3.6 V
VIN_3V3
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
I2Ct_IRQ
OD_VOL_IRQ Low level output voltage I = 2 mA 0.4 V
OL
OD_LKG_IRQ Leakage Current Output is Hi-Z, V = 3.45 V -1 1 uA
I2Cx_IRQ
I2Cc_IRQ
IRQ_VIH High-Level input voltage V = 3.3 V 1.3 V
LDO_3V3
IRQ_VIH_THRESH High-Level input voltage threshold V = 3.3 V 0.72 1.3 V
LDO_3V3
IRQ_VIL low-level input voltage V = 3.3 V 0.54 V
LDO_3V3
IRQ_VIL_THRESH low-level input voltage threshold V = 3.3 V 0.54 1.08 V
LDO_3V3
IRQ_HYS input hysteresis voltage V = 3.3 V 0.09 V
LDO_3V3
IRQ_DEG input deglitch 20 ns
IRQ_ILKG I2C3m_IRQ leakage current V = 3.45 V -1 1 uA
I2C3m_IRQ
SDA and SCL Common Characteristics (Controller, Target)
V Input low signal V = 3.3 V 0.54 V
IL LDO_3V3
I Max output low current V = 0.4 V 15 mA
OL OL
I Max output low current V = 0.6 V 20 mA
OL OL
t Fall time from 0.7 x V DD to 0.3 x V DD = 1.8 V, 10 pF <= C b <= 400 pF 12 80 ns
f V DD V DD = 3.3 V, 10 pF <= C b <= 400 pF 12 150 ns
t I2C pulse width suppressed 50 ns
SP
18 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 19

#### Extracted tables

Table 1:

```text
PARAMETER |  | TEST CONDITIONS | MIN | TYP | MAX | UNIT
C b | Capacitive load for each bus line (external) |  | 400 |  |  | pF
SDA and SCL Standard Mode Characteristics (Target) |  |  |  |  |  | 
f SCLS | Clock frequency for target | V = 1.8 V or 3.3 V DD | 100 |  |  | kHz
t VD;DAT | Valid data time | Transmitting Data, V = 1.8 V or DD 3.3 V, SCL low to SDA output valid | 3.45 |  |  | us
t VD;ACK | Valid data time of ACK condition | Transmitting Data, V = 1.8 V or DD 3.3 V, ACK signal from SCL low to SDA (out) low | 3.45 |  |  | us
SDA and SCL Fast Mode Characteristics (Target) |  |  |  |  |  | 
f SCLS | Clock frequency for target | V = 1.8 V or 3.3 V DD | 100 400 |  |  | kHz
t VD;DAT | Valid data time | Transmitting data, V = 1.8 V, DD SCL low to SDA output valid | 0.9 |  |  | us
t VD;ACK | Valid data time of ACK condition | Transmitting data, V = 1.8 V or DD 3.3 V, ACK signal from SCL low to SDA (out) low | 0.9 |  |  | us
f SCLS | Clock frequency for Fast Mode Plus(1) | V = 1.8 V or 3.3 V DD | 400 800 |  |  | kHz
t VD;DAT | Valid data time | Transmitting data, V = 1.8 V or DD 3.3 V, SCL low to SDA output valid | 0.55 |  |  | us
t VD;ACK | Valid data time of ACK condition | Transmitting data, V = 1.8 V or DD 3.3 V, ACK signal from SCL low to SDA (out) low | 0.55 |  |  | us
t LOW | Clock low time | V = 3.3 V DD | 1.3 |  |  | us
t HIGH | Clock high time | V = 3.3 V DD | 0.6 |  |  | us
```

#### Raw extracted text

```text
TPS25751
www.ti.com SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
6.19 I2C Requirements and Characteristics (continued)
Operating under these conditions unless otherwise noted: 3.0 V <= V <= 3.6 V
VIN_3V3
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
Capacitive load for each bus line
C 400 pF
b (external)
SDA and SCL Standard Mode Characteristics (Target)
f Clock frequency for target V = 1.8 V or 3.3 V 100 kHz
SCLS DD
Transmitting Data, V = 1.8 V or
t Valid data time DD 3.45 us
VD;DAT 3.3 V, SCL low to SDA output valid
Transmitting Data, V = 1.8 V or
DD
t Valid data time of ACK condition 3.3 V, ACK signal from SCL low to 3.45 us
VD;ACK
SDA (out) low
SDA and SCL Fast Mode Characteristics (Target)
f Clock frequency for target V = 1.8 V or 3.3 V 100 400 kHz
SCLS DD
Transmitting data, V = 1.8 V,
DD
t Valid data time SCL 0.9 us
VD;DAT
low to SDA output valid
Transmitting data, V = 1.8 V or
DD
3.3 V, ACK
t Valid data time of ACK condition 0.9 us
VD;ACK signal from SCL low to SDA (out)
low
Clock frequency for Fast Mode
f V = 1.8 V or 3.3 V 400 800 kHz
SCLS Plus(1) DD
Transmitting data, V = 1.8 V or
DD
t Valid data time 3.3 V, SCL 0.55 us
VD;DAT
low to SDA output valid
Transmitting data, V = 1.8 V or
DD
3.3 V, ACK
t Valid data time of ACK condition 0.55 us
VD;ACK signal from SCL low to SDA (out)
low
t Clock low time V = 3.3 V 1.3 us
LOW DD
t Clock high time V = 3.3 V 0.6 us
HIGH DD
(1) Controller must control fSCLS to ensure tLOW > tVD; ACK.
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 19
Product Folder Links: TPS25751
```

### Page 20

#### Extracted tables

Table 1:

```text
50 48 46 44 ):m( 42 V5_PPR 40 38 36 34 32 -20 0 20 40 60 80 100 120 140 TJ (oC) TypG Figure 6-1. PP_5V Rdson vs. Temperature. | 1.05 1 0.95 0.9 ):( ELBAC_PPR 0.85 0.8 0.75 0.7 0.65 0.6 -20 0 20 40 60 80 100 120 140 TJ (oC) TypG Figure 6-2. PP_CABLE Rdson vs. Temperature
7.5 VPx_VBUS = 4V VPx_VBUS = 22V 7 )Vm( 6.5 PCRV 6 5.5 5 -60 -30 0 30 60 90 120 150 TJ (oC) TypG Figure 6-3. V vs. Temperature RCP | 5.8 5.78 )Vm( 5.76 PCR4PVOV 5.74 5.72 5.7 -50 0 50 100 150 TJ (oC) TypG Figure 6-4. V (Setting 2) vs. Temperature OVP4RCP
28 26 24 ):m( 22 VH_PPR 20 18 16 14 -20 0 20 40 60 80 100 120 140 160 TJ (oC) TypG Figure 6-5. R vs. Temperature for TPS25751D PPHV | 100 70 Single Pulse Duration 50 100 ms 10 ms 30 1 ms )A( 20 100 Ps 10 Ps tnerruC 10 7 ecruoS-ot-ecruoS 5 3 2 1 0.7 0.5 0.3 0.2 0.1 0.1 0.2 0.3 0.50.7 1 2 3 4 567810 20 304050 Source-to-Source Voltage (V) SOAf Figure 6-6. Safe-Operating-Area (SOA) of PPHV for TPS25751D
```

Table 2:

```text
|  |  |  |  |  | 4V 22V
 |  |  |  | VP VP | x_VBUS = x_VBUS = | 4V 22V
```

Table 3:

```text
| 10 10 1 10 | 0 m ms ms 0 P | s s |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
 | 10 | Ps |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
```

#### Raw extracted text

```text
6.20 Typical Characteristics
TJ (oC)
RPP_5V (m:)
-20 0 20 40 60 80 100 120 140
32
34
36
38
40
42
44
46
48
50
TypG
Figure 6-1. PP_5V Rdson vs. Temperature.
TJ (oC)
RPP_CABLE (:)
-20 0 20 40 60 80 100 120 140
0.6
0.65
0.7
0.75
0.8
0.85
0.9
0.95
1
1.05
TypG Figure 6-2. PP_CABLE Rdson vs. Temperature
TJ (oC)
VRCP (mV)
-60 -30 0 30 60 90 120 150
5
5.5
6
6.5
7
7.5
TypG
VPx_VBUS = 4V
VPx_VBUS = 22V
Figure 6-3. VRCP vs. Temperature
TJ (oC)
VOVP4RCP (mV)
-50 0 50 100 150
5.7
5.72
5.74
5.76
5.78
5.8
TypG Figure 6-4. VOVP4RCP (Setting 2) vs. Temperature
TJ (oC)
RPP_HV (m:)
-20 0 20 40 60 80 100 120 140 160
14
16
18
20
22
24
26
28
TypG
Figure 6-5. RPPHV vs. Temperature for TPS25751D
Source-to-Source Voltage (V)
Source-to-Source Current (A)
0.1 0.2 0.3 0.5 0.7 1 2 3 4 5 6 7 8 10 20 30 40 50
0.1
0.2
0.3
0.5
0.7
1
2
3
5
7
10
20
30
50
70
100
SOAf
Single Pulse Duration
100 ms
10 ms
1 ms
100 Ps
10 Ps
Figure 6-6. Safe-Operating-Area (SOA) of PPHV for TPS25751D
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
 www.ti.com
20 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 21

#### Extracted tables

Table 1:

```text
9.4 9.2 9 GATE_VSYS: VSYS= 0 V 8.8 )V( GATE_VSYS: VSYS= 22 V GATE_VBUS ETAGV 8.6 8.4 8.2 8 7.8 -40 -20 0 20 40 60 80 100 120 140 TJ (oC) TypG Figure 6-7. V vs. Temperature for TPS25751S GATE_VBUS_ON | 10.2 IGATE_VBUS 10.15 IGATE_VSYS 10.1 )AP( 10.05 NO_ETAGI 10 9.95 9.9 9.85 -20 0 20 40 60 80 100 120 140 TJ (oC) TypG Figure 6-8. V vs. Temperature for TPS25751S GATE_VSYS_ON
```

Table 2:

```text
| GATE_ | VSYS: | VSYS | = 0 V |  |  | 
 | GATE_ GATE_ | VSYS: VBUS | VSYS | = 22 V |  |  |
```

Table 3:

```text
|  |  |  |  |  |  | IGAT I | E_VBUS
 |  |  |  |  |  |  | GAT | E_VSYS
```

#### Raw extracted text

```text
6.20 Typical Characteristics (continued)
TJ (oC)
)V(
ETAGV
9.4
9.2
9
GATE_VSYS: VSYS= 0 V 8.8
GATE_VSYS: VSYS= 22 V
GATE_VBUS
8.6
8.4
8.2
8
7.8
-40 -20 0 20 40 60 80 100 120 140 TJ (oC)
TypG
Figure 6-7. V vs. Temperature for TPS25751S
GATE_VBUS_ON
)AP(
NO_ETAGI
TPS25751
www.ti.com SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
10.2
IGATE_VBUS
10.15 IGATE_VSYS
10.1
10.05
10
9.95
9.9
9.85
-20 0 20 40 60 80 100 120 140
TypG
Figure 6-8. V vs. Temperature for TPS25751S
GATE_VSYS_ON
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 21
Product Folder Links: TPS25751
```

### Page 22

#### Extracted tables

Table 1:

```text
P |  | S
```

#### Raw extracted text

```text
7 Parameter Measurement Information
002aac938
tf
70 %
30 %SDA
tf
70 %
30 %
S
tr
70 %
30 %
70 %
30 %
t
SCL
HD;DAT
1 / f
1 clock cycle
SCL
st
70 %
30 %
70 %
30 %
tr
t
cont.
VD;DAT
cont.
SDA
SCL
tSU;STA tHD;STA
Sr
tSP tSU;STO
tBUF
P S
tHIGH
9 clockthtHD;STA tLOW
70 %
30 %
tVD;ACK
9 clockth
tSU;DAT
Figure 7-1. I2C Target Interface Timing
tiOS_PP_5V, tiOS_PP_CABLE
ILIM5V, ILIMVC
Figure 7-2. Short-circuit Response Time for Internal Power Paths PP_5V and PP_CABLE
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
 www.ti.com
22 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 23

#### Raw extracted text

```text
8 Detailed Description
8.1 Overview
The TPS25751 is a fully-integrated USB Power Delivery (USB-PD) management device providing cable plug
and orientation detection for USB Type-C and PD receptacles. The TPS25751 communicates with the cable and
another USB Type-C and PD device at the opposite end of the cable. The device also enables integrated port
power switch for sourcing, and controls a high current port power switch for sinking.
The TPS25751 is divided into several main sections:
* USB-PD controller
* Cable plug and orientation detection circuitry
* Port power switches
* Power management circuitry
* Digital core
The USB-PD controller provides the physical layer (PHY) functionality of the USB-PD protocol. The USB-PD
data is output through either the CC1 pin or the CC2 pin, depending on the orientation of the reversible USB
Type-C cable. For a high-level block diagram of the USB-PD physical layer, a description of its features, and
more detailed circuitry, see USB-PD Physical Layer.
The cable plug and orientation detection analog circuitry automatically detects a USB Type-C cable plug
insertion the cable orientation. For a high-level block diagram of cable plug and orientation detection, a
description of its features, and more detailed circuitry, see Cable Plug and Orientation Detection.
The port power switches provide power to the VBUS pin and CC1 or CC2 pins based on the detected plug
orientation. For a high-level block diagram of the port power switches, a description of its features, and more
detailed circuitry, see Power Paths.
The power management circuitry receives and provides power to the TPS25751 internal circuitry and LDO_3V3
output. See Power Management for more information.
The digital core provides the engine for receiving, processing, and sending all USB-PD packets as well as
handling control of all other TPS25751 functionality. A portion of the digital core contains ROM memory, which
contains all the necessary firmware required to execute Type-C and PD applications. In addition, a section of the
ROM, called boot code, is capable of initializing the TPS25751, loading of the device configuration information,
and loading any code patches into volatile memory in the digital core. For a high-level block diagram of the
digital core, a description of its features, and more detailed circuitry, see Digital Core.
The TPS25751 has one I2C controller to write to and read from external target devices such as a battery charger
or an optional external EEPROM memory (see I2C Interface).
The TPS25751 also integrates a thermal shutdown mechanism and runs off of accurate clocks provided by the
integrated oscillator.
8.2 Functional Block Diagram
www.ti.com
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 23
Product Folder Links: TPS25751
```

### Page 24

#### Raw extracted text

```text
Power Supervisor
Core & Other Digital
Cable Detect, Cable Power, & USB PD PHY
ADCIN1
ADCIN2
I2Ct_SDA/SCL/IRQ
I2Cc_SDA/SCL/IRQ
GPIOx
VIN_3V3
PP5V
GND
LDO_3V3
LDO_1V5
VBUS
CC1
CC2
PPHV VBUS_IN
Figure 8-1. TPS25751D
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
 www.ti.com
24 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 25

#### Raw extracted text

```text
Power Supervisor
Core & Other Digital
Cable Detect, Cable Power, & USB PD PHY
ADCIN1
ADCIN2
I2Ct_SDA/SCL/IRQ
I2Cc_SDA/SCL/IRQ
GPIOx
VIN_3V3
VSYS
PP5V
GATE_VSYS
GND
LDO_3V3
LDO_1V5
VBUS
CC1
CC2
GATE_VBUS
Figure 8-2. TPS25751S
www.ti.com
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 25
Product Folder Links: TPS25751
```

### Page 26

#### Extracted tables

Table 1:

```text
Digital Core |
```

#### Raw extracted text

```text
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024 www.ti.com
8.3 Feature Description
8.3.1 USB-PD Physical Layer
Figure 8-3 shows the USB PD physical layer block surrounded by a simplified version of the analog plug and
orientation detection block.
IVCON
cu
F
r
a
re
st
nt
limit
PP5V
CC1 Gate Control and Current
Limit
LDO_3V3
IRp
RSNK
CC1
Digital USB-PD PHY
Core (Rx/Tx)
LDO_3V3 CC2
IRp
RSNK
CC1 Gate Control and Current
Limit
Fast
current
limit
Figure 8-3. USB-PD Physical Layer and Simplified Plug and Orientation Detection Circuitry
26 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 27

#### Raw extracted text

```text
USB-PD messages are transmitted in a USB Type-C system using a BMC signaling. The BMC signal is output
on the same pin (CC1 or CC2) that is DC biased due to the Rp (or Rd) cable attach mechanism.
8.3.1.1 USB-PD Encoding and Signaling
Figure 8-4 illustrates the high-level block diagram of the baseband USB-PD transmitter. Figure 8-5 illustrates the
high-level block diagram of the baseband USB-PD receiver.
4b5b
Encoder
BMC
Encoder
CRC
Data to PD_TX
Figure 8-4. USB-PD Baseband Transmitter Block Diagram
BMC
Decoder
SOP
Detect
4b5b
Decoder
CRC
from PD_RX
Data
Figure 8-5. USB-PD Baseband Receiver Block Diagram
8.3.1.2 USB-PD Bi-Phase Marked Coding
The USB-PD physical layer implemented in the TPS25751 is compliant to the USB-PD Specifications . The
encoding scheme used for the baseband PD signal is a version of Manchester coding called Biphase Mark
Coding (BMC). In this code, there is a transition at the start of every bit time and there is a second transition in
the middle of the bit cell when a 1 is transmitted. This coding scheme is nearly DC balanced with limited disparity
(limited to 1/2 bit over an arbitrary packet, so a very low DC level). Figure 8-6 illustrates Biphase Mark Coding.
0 1 0 1 0 1 0 0 0 0 1 1 0 0 0 1 1
Data in
BMC
1
Figure 8-6. Biphase Mark Coding Example
The USB PD baseband signal is driven onto the CC1 or CC2 pin with a tri-state driver. The tri-state driver is slew
rate to limit coupling to D+/D- and to other signal lines in the Type-C fully featured cables. When sending the
USB-PD preamble, the transmitter starts by transmitting a low level. The receiver at the other end tolerates the
loss of the first edge. The transmitter terminates the final bit by an edge to ensure the receiver clocks the final bit
of EOP.
8.3.1.3 USB-PD Transmit (TX) and Receive (Rx) Masks
The USB-PD driver meets the defined USB-PD BMC TX masks. Because a BMC coded 1 contains a signal
edge at the beginning and middle of the UI, and the BMC coded 0 contains only an edge at the beginning, the
masks are different for each. The USB-PD receiver meets the defined USB-PD BMC Rx masks. The boundaries
of the Rx outer mask are specified to accommodate a change in signal amplitude due to the ground offset
through the cable. The Rx masks are therefore larger than the boundaries of the TX outer mask. Similarly, the
boundaries of the Rx inner mask are smaller than the boundaries of the TX inner mask. Triangular time masks
are superimposed on the TX outer masks and defined at the signal transitions to require a minimum edge rate
that has minimal impact on adjacent higher speed lanes. The TX inner mask enforces the maximum limits on the
rise and fall times. Refer to the USB-PD Specifications for more details.
www.ti.com
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 27
Product Folder Links: TPS25751
```

### Page 28

#### Raw extracted text

```text
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024 www.ti.com
8.3.1.4 USB-PD BMC Transmitter
The TPS25751 transmits and receives USB-PD data over one of the CCy pins for a given CC pin pair (one
pair per USB Type-C port). The CCy pins are also used to determine the cable orientation and maintain the
cable/device attach detection. Thus, a DC bias exists on the CCy pins. The transmitter driver overdrives the CCy
DC bias while transmitting, but returns to a Hi-Z state, allowing the DC voltage to return to the CCy pin when it is
not transmitting. While either CC1 or CC2 can be used for transmitting and receiving, during a given connection
only, the one that mates with the CC pin of the plug is used, so there is no dynamic switching between CC1 and
CC2. Figure 8-7 shows the USB-PD BMC TX and RX driver block diagram.
LDO_3V3
PD_TX Level Shifter Driver
CC1
PD_RX Level Shifter CC2
Digitally
Adjustable
VREF (VRXHI, VRXLO)
USB-PD Modem
Figure 8-7. USB-PD BMC TX/Rx Block Diagram
Figure 8-8 shows the transmission of the BMC data on top of the DC bias. Note that the DC bias can be
anywhere between the minimum and maximum threshold for detecting a Sink attach. This note means that the
DC bias can be above or below the VOH of the transmitter driver.
VOH
DC Bias DC Bias
VOL
DC Bias VOH DC Bias
VOL
Figure 8-8. TX Driver Transmission with DC Bias
The transmitter drives a digital signal onto the CCy lines. The signal peak, V , is set to meet the TX masks
TXHI
defined in the USB-PD Specifications. Note that the TX mask is measured at the far-end of the cable.
When driving the line, the transmitter driver has an output impedance of Z . Z is determined by the
DRIVER DRIVER
driver resistance and the shunt capacitance of the source and is frequency dependent. Z impacts the
DRIVER
noise ingression in the cable.
28 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 29

#### Raw extracted text

```text
TPS25751
www.ti.com SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
Figure 8-9 shows the simplified circuit determining Z . It is specified such that noise at the receiver is
DRIVER
bounded.
R Z
DRIVER DRIVER
Driver
C
DRIVER
Figure 8-9. ZDRIVER Circuit
8.3.1.5 USB-PD BMC Receiver
The receiver block of the TPS25751 receives a signal that follows the allowed Rx masks defined in the USB PD
specification. The receive thresholds and hysteresis come from this mask.
Figure 8-10 shows an example of a multi-drop USB-PD connection (only the CC wire). This connection has
the typical Sink (device) to Source (host) connection, but also includes cable USB-PD Tx/Rx blocks. Only one
system can be transmitting at a time. All other systems are Hi-Z (Z ). The USB-PD Specification also
BMCRX
specifies the capacitance that can exist on the wire as well as a typical DC bias setting circuit for attach
detection.
Source Sink
System Pullup for System
Attach
Detection Connector Cable Connector
CC wire
Tx Tx
CRECEIVER
CRECEIVER
Rx Rx
CCablePlug_CC CCablePlug_CC
RD for
Attach
Detection
Rx Rx
Tx Tx
623(cid:3)3'(cid:3) 623(cid:3)3'(cid:3)
communication only communication only
(eMarker #1) (eMarker #2)
Figure 8-10. Example USB-PD Multi-Drop Configuration
8.3.1.6 Squelch Receiver
The TPS25751 has a squelch receiver to monitor for the bus idle condition as defined by the USB PD
specification.
8.3.2 Power Management
The TPS25751 power management block receives power and generates voltages to provide power to the
TPS25751 internal circuitry. These generated power rails are LDO_3V3 and LDO_1V5. LDO_3V3 can also be
used as a low power output for external EEPROM memory. The power supply path is shown in Figure 8-11.
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 29
Product Folder Links: TPS25751
```

### Page 30

#### Raw extracted text

```text
LDOLDO_1V5
LDO
VREF
VREF
VIN_3V3
LDO_3V3
VBUS
RLDO_3V3
Figure 8-11. Power Supplies
The TPS25751 is powered from either VIN_3V3 or VBUS. The normal power supply input is VIN_3V3. When
powering from VIN_3V3, current flows from VIN_3V3 to LDO_3V3 to power the core 3.3-V circuitry and I/Os. A
second LDO steps the voltage down from LDO_3V3 to LDO_1V5 to power the 1.5-V core digital circuitry. When
VIN_3V3 power is unavailable and power is available on VBUS, it is referred to as the dead-battery start-up
condition. In a dead-battery start-up condition, the TPS25751 opens the VIN_3V3 switch until the host clears
the dead-battery flag through I 2C. Therefore, the TPS25751 is powered from the VBUS input with the higher
voltage during the dead-battery start-up condition and until the dead-battery flag is cleared. When powering from
a VBUS input, the voltage on VBUS is stepped down through an LDO to LDO_3V3.
8.3.2.1 Power-On And Supervisory Functions
A power-on reset (POR) circuit monitors each supply. This POR allows active circuitry to turn on only when a
good supply is present.
8.3.2.2 VBUS LDO
The TPS25751 contains an internal high-voltage LDO which is capable of converting VBUS to 3.3 V for powering
internal device circuitry. The VBUS LDO is only used when VIN_3V3 is low (the dead-battery condition). The
VBUS LDO is powered from VBUS.
8.3.3 Power Paths
The TPS25751 has internal sourcing power paths: PP_5V and PP_CABLE. TPS25751D has a integrated
bidirectional high voltage load switch for sinking power path: PPHV. TPS25751S has a high voltage gate driver
for sink path control: PP_EXT. Each power path is described in detail in this section.
8.3.3.1 Internal Sourcing Power Paths
Figure 8-12 shows the TPS25751 internal sourcing power paths available in both TPS25751D and TPS25751S.
The TPS25751 features two internal 5-V sourcing power paths. The path from PP5V to VBUS is called PP_5V.
The path from PP5V to CCx is called PP_CABLE. Each path contains two back-to-back common drain N-FETs,
with current clamping protection, overvoltage protection, UVLO protection, and temperature sensing circuitry.
PP_5V can conduct up to 3 A continuously, while PP_CABLE can conduct up to 315 mA continuously. When
disabled, the blocking FET protects the PP5V rail from high-voltage that can appear on VBUS.
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
 www.ti.com
30 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 31

#### Extracted tables

Table 1:

```text
PP_CABLE TSD_PP5V CC1 Gate Control Fast current limit, IVCON CC2 Gate Control Temp Sensor |  |
```

#### Raw extracted text

```text
TPS25751
www.ti.com SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
3A
Fast current clamp, ILIM5V
VBUS
Temp
Sensor
PP_5V Gate Control and Sense
PP_5V
PP_CABLE
TSD_PP5V CC1 Gate Control
Fast current limit, IVCON
CC1
CC2 Gate Control
Temp
PP5V
Sensor
CC2
Figure 8-12. Port Power Switches
8.3.3.1.1 PP_5V Current Clamping
The current through the internal PP_5V path are current limited to I . The I value is configured by
LIM5V LIM5V
application firmware. When the current through the switch exceeds I , the current limiting circuit activates
LIM5V
within t and the path behaves as a constant current source. If the duration of the overcurrent event
iOS_PP_5V
exceeds t , the PP_5V switch is disabled.
ILIM
8.3.3.1.2 PP_5V Local Overtemperature Shut Down (OTSD)
When PP_5V clamps the current, the temperature of the switch begin to increase. When the local temperature
sensors of PP_5V or PP_CABLE detect that T > T , the PP_5V switch is disabled and the affected port
J SD_PP5V
enters the USB Type-C ErrorRecovery state.
8.3.3.1.3 PP_5V OVP
The overvoltage protection level is automatically configured based on the expected maximum V voltage,
BUS
which depends upon the USB PD contract. When the voltage on the VBUS pin of a port exceeds the configured
value (V ) while PP_5V is enabled, then PP_5V is disabled within t and the port enters into the
OVP4RCP PP_5V_ovp
Type-C ErrorRecovery state.
8.3.3.1.4 PP_5V UVLO
If the PP5V pin voltage falls below its undervoltage lock out threshold (V ) while PP_5V is enabled, then
PP5V_UVLO
PP_5V is disabled within t and the port that had PP_5V enabled enters into the Type-C ErrorRecovery
PP_5V_uvlo
state.
8.3.3.1.5 PP_5Vx Reverse Current Protection
If V - V > V , then the PP_5V path is automatically disabled within t . If the RCP
VBUS PP5V PP_5V_RCP PP_5V_rcp
condition clears, then the PP_5V path is automatically enabled within t .
ON
8.3.3.1.6 PP_CABLE Current Clamp
When enabled and providing VCONN power, the TPS25751 PP_CABLE power switch clamps the current to
I . When the current through the PP_CABLE switch exceeds I , the current clamping circuit activates
VCON VCON
within t and the switch behaves as a constant current source.
iOS_PP_CABLE
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 31
Product Folder Links: TPS25751
```

### Page 32

#### Extracted tables

Table 1:

```text
PP_HV |  |  |  |  | 
 |  |  | SUBV_ETAG |  |
```

#### Raw extracted text

```text
8.3.3.1.7 PP_CABLE Local Overtemperature Shut Down (OTSD)
When PP_CABLE clamps the current, the temperature of the switch begins to increase. When the local
temperature sensors of PP_5V or PP_CABLE detect that T >T , the PP_CABLE switch is disabled and
J SD_PP5V
latched off within t . The port then enters the USB Type-C ErrorRecovery state.
PP_CABLE_off
8.3.3.1.8 PP_CABLE UVLO
If the PP5V pin voltage falls below its undervoltage lock out threshold (V ), then the PP_CABLE switch
PP5V_UVLO
is automatically disabled within t .
PP_CABLE_off
8.3.3.2 TPS25751D Internal Sink Path
The TPS25751D has internal controls for internal FETs (GATE_VSYS and GATE_VBUS as shown in Figure
8-13) that require that VBUS_IN be above V before being able to enable the sink path. Figure 8-13
VBUS_UVLO
shows a diagram of the sink path. When a sink path is enabled, the circuitry includes a slew rate control loop
to ensure that external switches do not turn on too quickly (SS). The TPS25751D senses the PPHV and VBUS
voltages to control the gate voltages to enable or disable the FETs.
The sink-path control includes overvoltage protection (OVP) and reverse current protection (RCP).
PP_HV
PPHV VBUS
Gate Control and Sense
Copyright  2018, Texas Instruments Incorporated
SYSV_ETAG SUBV_ETAG
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024 www.ti.com
Figure 8-13. Internal Sink Path
8.3.3.2.1 Overvoltage Protection (OVP)
The application firmware enables the OVP and configures it based on the expected VBUS voltage. If the
voltage on VBUS surpasses the configured threshold VOVP4VSYS = VOVP4RCP/rOVP, then GATE_VSYS
is automatically disabled within tPPHV_FSD to protect the system. If the voltage on VBUS surpasses the
configured threshold VOVP4RCP, then GATE_VBUS is automatically disabled within tPPHV_OVP. When
VVBUS falls below VOVP4RCP - VOVP4RCPH, GATE_VBUS is automatically re-enabled within tPPHV_ON
because the OVP condition has cleared. This action allows two sinking power paths to be enabled
simultaneously and GATE_VBUS disables when necessary to ensure that VVBUS remains below VOVP4RCP.
While the TPS25751D is in BOOT mode in a dead-battery scenario (that is VIN_3V3 is low), it handles an
OVP condition slightly differently. As long as the OVP condition is present, GATE_VBUS and GATE_VSYS are
disabled. Once the OVP condition clears, both GATE_VBUS and GATE_VSYS are re-enabled. Because this is
a dead-battery condition, the TPS25751D draws approximately IVIN_3V3, ActSnk from VBUS during this time to
help discharge it.
32 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 33

#### Raw extracted text

```text
SUBV
TPS25751
www.ti.com SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
Power Path Supervisor
VOVP4RCP
VOVP4VSYS = VOVP4RCP / rOVP
Figure 8-14. Diagram for OVP Comparators
8.3.3.2.2 Reverse-Current Protection (RCP)
The VSYS gate control circuit monitors the PPHV and VBUS voltages and detects reverse current when the
VVSYS surpasses V by more than V . When the reverse current condition is detected, GATE_VBUS is
VBUS RCP
disabled within tPPHV_RCP. When the reverse current condition is cleared, GATE_VBUS is re-enabled within
tPPHV_ON. This action limits the amount of reverse current that can flow from PPHV to VBUS through the
external N-ch MOSFETs. In reverse current protection mode, the power switch controlled by GATE_VBUS is
allowed to behave resistively until the current reaches VRCP/ RPPHV and then blocks reverse current from
PPHV to VBUS.
I
1/RPPHV
-VRCP
V=VVBUS +/- VPPHV
VRCP/RPPHV
Copyright  2018, Texas Instruments Incorporated
Figure 8-15. Switch I-V Curve for RCP on Sink-path Switches.
8.3.3.2.3 VBUS UVLO
The TPS25751D monitors VBUS voltage and detects when it falls below VVBUS_UVLO. When the UVLO
condition is detected, GATE_VBUS is disabled within tPPHV_RCP. When the UVLO condition is cleared,
GATE_VBUS is reenabled within tPPHV_ON.
8.3.3.2.4 Discharging VBUS to Safe Voltage
The TPS25751D has an integrated active pulldown (IDSCH) on VBUS for discharging from high voltage to
VSAFE0V (0.8 V). This discharge is applied when it is in an Unattached Type-C state.
8.3.3.3 TPS25751S - External Sink Path Control PP_EXT
The TPS25751S has two N-ch gate drivers designed to control a sinking path from VBUS to VSYS. The charge
pump for these gate drivers requires VBUS to be above VVBUS_UVLO. When a sink path is enabled, the
circuitry includes a slew rate control loop to ensure that external switches do not turn on too quickly (SS). The
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 33
Product Folder Links: TPS25751
```

### Page 34

#### Extracted tables

Table 1:

```text
PP_EXT |  |  | 
 | SYSV_ | SUBV_ | 
 | ETAG | ETAG |
```

#### Raw extracted text

```text
TPS25751S senses the VSYS and VBUS voltages to control the gate voltages to enable or disable the external
FETs.
The sink-path control includes overvoltage protection (OVP), and reverse current protection (RCP). Adding
resistance in series with a GATE pin of the TPS25751S and the gate pin of the N-ch MOSFET slows down the
turnoff time when OVP or RCP occurs. Any such resistance must be minimized, and not allowed to exceed 3 Ohm.
PP_EXT
PP_EXT Gate Control and
Sense
SYSV_ETAG SUBV_ETAG
SUBV
Copyright  2018, Texas Instruments Incorporated
SYSV
Figure 8-16. PP_EXT External Sink Path Control
Figure 8-17 shows the GATE_VSYS gate driver in more detail.
SYSV
V
GATE_ON
I
GATE_ON
Charge
Pump
DNG
SYSV_ETAG
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024 www.ti.com
switch enabled when
gate driver is disabled and
V < V
VIN_3V3 VIN_3V3_UVLO
R
GATE_FSD
Regular enable/
disable
Fast
disable
I
GATE_OFF
VBUS
R
GATE_OFF_UVLO
Figure 8-17. Details of the VSYS Gate Driver
34 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 35

#### Raw extracted text

```text
8.3.3.3.1 Overvoltage Protection (OVP)
The application firmware enables the OVP and configures it based on the expected VBUS voltage. If the
voltage on VBUS surpasses the configured threshold VOVP4VSYS = VOVP4RCP/rOVP, then GATE_VSYS
is automatically disabled within tPPHV_FSD to protect the system. If the voltage on VBUS surpasses the
configured threshold VOVP4RCP, then GATE_VBUS is automatically disabled within tPPHV_OVP. When
VVBUS falls below VOVP4RCP - VOVP4RCPH, GATE_VBUS is automatically re-enabled within tPPHV_ON
because the OVP condition has cleared. This action allows two sinking power paths to be enabled
simultaneously and GATE_VBUS disables when necessary to ensure that VVBUS remains below VOVP4RCP.
While the TPS25751D is in BOOT mode in a dead-battery scenario (that is VIN_3V3 is low), it handles an
OVP condition slightly differently. As long as the OVP condition is present, GATE_VBUS and GATE_VSYS are
disabled. Once the OVP condition clears, both GATE_VBUS and GATE_VSYS are re-enabled. Because this is
a dead-battery condition, the TPS25751D draws approximately IVIN_3V3, ActSnk from VBUS during this time to
help discharge it.
SUBV
TPS25751
www.ti.com SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
Power Path Supervisor
VOVP4RCP
VOVP4VSYS = VOVP4RCP / rOVP
Figure 8-18. Diagram for OVP Comparators
8.3.3.3.1.1 Reverse-Current Protection (RCP)
The VSYS gate control circuit monitors the PPHV and VBUS voltages and detects reverse current when the
VVSYS surpasses V by more than V . When the reverse current condition is detected, GATE_VBUS is
VBUS RCP
disabled within tPPHV_RCP. When the reverse current condition is cleared, GATE_VBUS is re-enabled within
tPPHV_ON. This action limits the amount of reverse current that can flow from PPHV to VBUS through the
external N-ch MOSFETs. In reverse current protection mode, the power switch controlled by GATE_VBUS is
allowed to behave resistively until the current reaches VRCP/ RPPHV and then blocks reverse current from
PPHV to VBUS.
I
1/RPPHV
-VRCP
V=VVBUS +/- VPPHV
VRCP/RPPHV
Copyright  2018, Texas Instruments Incorporated
Figure 8-19. Switch I-V Curve for RCP on Sink-path Switches.
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 35
Product Folder Links: TPS25751
```

### Page 36

#### Extracted tables

Table 1:

```text
CC1 | CC2 | CONNECTION STATE | RESULTING ACTION
Open | Open | Nothing attached | Continue monitoring both CCy pins for attach. Power is not applied to VBUS or VCONN.
Rd | Open | Sink attached | Monitor CC1 for detach. Power is applied to VBUS but not to VCONN (CC2).
Open | Rd | Sink attached | Monitor CC2 for detach. Power is applied to VBUS but not to VCONN (CC1).
Ra | Open | Powered Cable-No UFP attached | Monitor CC2 for a Sink attach and CC1 for cable detach. Power is not applied to VBUS or VCONN (CC1).
```

#### Raw extracted text

```text
8.3.3.3.1.2 VBUS UVLO
The TPS25751D monitors VBUS voltage and detects when it falls below VVBUS_UVLO. When the UVLO
condition is detected, GATE_VBUS is disabled within tPPHV_RCP. When the UVLO condition is cleared,
GATE_VBUS is reenabled within tPPHV_ON.
8.3.3.3.1.3 Discharging VBUS to Safe Voltage
The TPS25751S has an integrated active pulldown (IDSCH) on VBUS for discharging from high voltage to
VSAFE0V (0.8 V). This discharge is applied when it is in an Unattached Type-C state.
8.3.4 Cable Plug and Orientation Detection
Figure 8-20 shows the plug and orientation detection block at each CCy pin (CC1, CC2). Each pin has identical
detection circuitry.
VREF1
VREF2
VREF3
IRpDef IRp1.5 IRp3.0
RSNK
CCy
Figure 8-20. Plug and Orientation Detection Block
8.3.4.1 Configured as a Source
When configured as a source, the TPS25751 detects when a cable or a Sink is attached using the CC1 and
CC2 pins. When in a disconnected state, the TPS25751 monitors the voltages on these pins to determine what,
if anything, is connected. See USB Type-C Specification for more information.
Table 8-1 shows the Cable Detect States for a Source.
Table 8-1. Cable Detect States for a Source
CC1 CC2 CONNECTION STATE RESULTING ACTION
Open Open Nothing attached Continue monitoring both CCy pins for attach. Power is not applied to VBUS or
VCONN.
Rd Open Sink attached Monitor CC1 for detach. Power is applied to VBUS but not to VCONN (CC2).
Open Rd Sink attached Monitor CC2 for detach. Power is applied to VBUS but not to VCONN (CC1).
Ra Open Powered Cable-No UFP
attached
Monitor CC2 for a Sink attach and CC1 for cable detach. Power is not applied to
VBUS or VCONN (CC1).
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
 www.ti.com
36 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 37

#### Extracted tables

Table 1:

```text
CC1 | CC2 | CONNECTION STATE | RESULTING ACTION
Open | Ra | Powered Cable-No UFP attached | Monitor CC1 for a Sink attach and CC2 for cable detach. Power is not applied to VBUS or VCONN (CC1).
Ra | Rd | Powered Cable-UFP Attached | Provide power on VBUS and VCONN CC1) then monitor CC2 for a Sink detach. CC1 is not monitored for a detach.
Rd | Ra | Powered Cable-UFP attached | Provide power on VBUS and VCONN (CC2) then monitor CC1 for a Sink detach. CC2 is not monitored for a detach.
Rd | Rd | Debug Accessory Mode attached | Sense either CCy pin for detach.
Ra | Ra | Audio Adapter Accessory Mode attached | Sense either CCy pin for detach.
```

#### Raw extracted text

```text
TPS25751
www.ti.com SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
Table 8-1. Cable Detect States for a Source (continued)
CC1 CC2 CONNECTION STATE RESULTING ACTION
Powered Cable-No UFP Monitor CC1 for a Sink attach and CC2 for cable detach. Power is not applied to
Open Ra
attached VBUS or VCONN (CC1).
Provide power on VBUS and VCONN CC1) then monitor CC2 for a Sink detach.
Ra Rd Powered Cable-UFP Attached
CC1 is not monitored for a detach.
Provide power on VBUS and VCONN (CC2) then monitor CC1 for a Sink detach.
Rd Ra Powered Cable-UFP attached
CC2 is not monitored for a detach.
Debug Accessory Mode
Rd Rd Sense either CCy pin for detach.
attached
Audio Adapter Accessory
Ra Ra Sense either CCy pin for detach.
Mode attached
When a TPS25751 port is configured as a Source, a current I is driven out each CCy pin and each pin is
RpDef
monitored for different states. When a Sink is attached to the pin, a pulldown resistance of Rd to GND exists.
The current I is then forced across the resistance Rd, generating a voltage at the CCy pin. The TPS25751
RpDef
applies I until it closes the switch from PP5V to VBUS, at which time application firmware can change to
RpDef
I or I .
Rp1.5A Rp3.0A
When the CCy pin is connected to an active cable VCONN input, the pulldown resistance is different (Ra). In this
case, the voltage on the CCy pin lowers the PD controller recognizes it as an active cable.
The voltage on CCy is monitored to detect a disconnection depending upon which Rp current source is active.
When a connection has been recognized and the voltage on CCy subsequently rises above the disconnect
threshold for t , the system registers a disconnection.
CC
8.3.4.2 Configured as a Sink
When a TPS25751 port is configured as a Sink, the TPS25751 presents a pulldown resistance R on each
SNK
CCy pin and waits for a Source to attach and pull up the voltage on the pin. The Sink detects an attachment by
the presence of VBUS and determines the advertised current from the Source based on the voltage on the CCy
pin.
8.3.4.3 Configured as a DRP
When a TPS25751 port is configured as a DRP, the TPS25751 alternates the CCy pins of the port between the
pulldown resistance, R , and pullup current source, I .
SNK Rp
8.3.4.4 Dead Battery Advertisement
The TPS25751 supports booting from no-battery or dead-battery conditions by receiving power from VBUS.
Type-C USB ports require a sink to present Rd on the CC pin before a USB Type-C source provides a voltage
on VBUS. TPS25751 hardware is configured to present this Rd during a dead-battery or no-battery condition.
Additional circuitry provides a mechanism to turn off this Rd once the device no longer requires power from
VBUS.
8.3.5 Overvoltage Protection (CC1, CC2)
The TPS25751 detects when the voltage on the CC1 or CC2 pin is too high or there is reverse current into
the PP5V pin and takes action to protect the system. The protective action is to disable PP_CABLE within
t and disable the USB PD transmitter.
PP_CABLE_FSD
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 37
Product Folder Links: TPS25751
```

### Page 38

#### Raw extracted text

```text
VVC_OVP
PP5V
VPHY_OVP
VPHY_OVP
CC1
CC2
VVC_RCP
max(VCC1, VCC2) - VPP5V
Control Logic
Disable PP_CABLE
and USB PD PHY
Tx
Figure 8-21. Overvoltage and Reverse Current Protection for CC1 and CC2
8.3.6 Default Behavior Configuration (ADCIN1, ADCIN2)
Note
This functionality is firmware controlled and subject to change.
The ADCINx inputs to the internal ADC control the behavior of the TPS25751 in response to VBUS being
supplied when VIN_3V3 is low (that is the dead-battery scenario).  The ADCINx pins must be externally tied to
the LDO_3V3 pin via a resistive divider as shown in the following figure. At power-up the ADC converts the
ADCINx voltage and the digital core uses these two values to determine start-up behavior. The available start-up
configurations include options for I 2C target address of I2Ct_SCL/SDA, sink path control in dead-battery, and
default configuration.
ADC Mux and
Dividers
LDO_3V3
ADCINx
Figure 8-22. ADCINx Resistor Divider
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
 www.ti.com
38 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 39

#### Extracted tables

Table 1:

```text
DIV = R / (R + R )(1) DOWN UP DOWN |  |  | Without Using R UP | ADCINx Decoded Value(2)
MIN | Target | MAX | or R DOWN | 
0 | 0.0114 | 0.0228 | tie to GND | 0
0.0229 | 0.0475 | 0.0722 | N/A | 1
0.0723 | 0.1074 | 0.1425 | N/A | 2
0.1425 | 0.1899 | 0.2372 | N/A | 3
0.2373 | 0.3022 | 0.3671 | N/A | 4
0.3672 | 0.5368 | 0.7064 | tie to LDO_1V5 | 5
0.7065 | 0.8062 | 0.9060 | N/A | 6
0.9061 | 0.9530 | 1.0 | tie to LDO_3V3 | 7
```

#### Raw extracted text

```text
TPS25751
www.ti.com SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
The device behavior is determined in several ways depending upon the decoded value of the ADCIN1 and
ADCIN2 pins. The following table shows the decoded values for different resistor divider ratios. See Pin
Strapping to Configure Default Behavior for details on how the ADCINx configurations determine default device
behavior. See I2C Address Setting for details on how ADCINx decoded values affects default I2C target address.
Table 8-2. Decoding of ADCIN1 and ADCIN2 Pins
DIV = R DOWN / (R UP + R DOWN )(1) Without Using R UP ADCINx Decoded Value(2)
MIN Target MAX or R DOWN
0 0.0114 0.0228 tie to GND 0
0.0229 0.0475 0.0722 N/A 1
0.0723 0.1074 0.1425 N/A 2
0.1425 0.1899 0.2372 N/A 3
0.2373 0.3022 0.3671 N/A 4
0.3672 0.5368 0.7064 tie to LDO_1V5 5
0.7065 0.8062 0.9060 N/A 6
0.9061 0.9530 1.0 tie to LDO_3V3 7
(1) See I2C Address Setting to see the exact meaning of I2C Address Index.
(2) See Pin Strapping to Configure Default Behavior for how to configure a given ADCINx decoded value.
8.3.7 ADC
The TPS25751 ADC is shown in Figure 8-23. The ADC is an 8-bit successive approximation ADC. The input to
the ADC is an analog input mux that supports multiple inputs from various voltages and currents in the device.
The output from the ADC is available to be read and used by application firmware.
Voltage
VBUS
Divider 2
LDO_3V3 Voltage
Divider 1
GPIO0
8 bits
GPIO2 Input ADC
Mux
ADCIN1 Buffers &
Voltage
ADCIN2 Divider 1
GPIO4
GPIO5
I_VBUS I-to-V
Copyright  2018, Texas Instruments Incorporated
Figure 8-23. SAR ADC
8.3.8 BC 1.2 (USB_P, USB_N)
The TPS25751 supports BC 1.2 as a Portable Device or Downstream Port using the hardware shown in Figure
8-24.
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 39
Product Folder Links: TPS25751
```

### Page 40

#### Extracted tables

Table 1:

```text
PIN NAME | TYPE | SPECIAL FUNCTIONALITY
GPIO0 | I/O | General-purpose input or output
GPIO1 | I/O | General-purpose input or output
GPIO2 | I/O | General-purpose input or output
GPIO3 | I/O | General-purpose input or output
GPIO4 | I/O | D+, general-purpose input or output, or LD1 for Liquid Detection
GPIO5 | I/O | D-, general-purpose input or output, or LD2 for Liquid Detection
GPIO6 | I/O | General-purpose input or output
GPIO7 | I/O | General-purpose input or output
I2Ct_IRQ(GPIO10) | O | IRQ for optional I2Ct, or used as a general-purpose output
GPIO11 | O | General-purpose output
I2Cc_IRQ(GPIO12) | I | IRQ for I2Cc, or used as a general-purpose input
```

#### Raw extracted text

```text
Figure 8-24. BC1.2 Hardware Components
8.3.9 Digital Interfaces
The TPS25751 contains several different digital interfaces which can be used for communicating with other
devices. The available interfaces include one I2C controller, one I2C target and additional GPIOs.
8.3.9.1 General GPIO
GPIOn pins can be mapped to USB Type-C, USB PD, and application-specific events to control other ICs,
interrupt a host processor, or receive input from another IC. This buffer is configurable to be a push-pull output,
a weak push-pull, or open drain output. When configured as an input, the signal can be a de-glitched digital
input . The push-pull output is a simple CMOS output with independent pull-down control allowing open-drain
connections. The weak push-pull is also a CMOS output, but with GPIO_RPU resistance in series with the drain.
The supply voltage to the output buffer is LDO_3V3 and LDO_1V5 to the input buffer. When interfacing with non
3.3-V I/O devices the output buffer can be configured as an open drain output and an external pull-up resistor
attached to the GPIO pin. The pull-up and pull-down output drivers are independently controlled from the input
and are enabled or disabled via application code in the digital core.
Table 8-3. GPIO Functionality Table
PIN NAME TYPE SPECIAL FUNCTIONALITY
GPIO0 I/O General-purpose input or output
GPIO1 I/O General-purpose input or output
GPIO2 I/O General-purpose input or output
GPIO3 I/O General-purpose input or output
GPIO4 I/O D+, general-purpose input or output, or LD1 for Liquid Detection
GPIO5 I/O D-, general-purpose input or output, or LD2 for Liquid Detection
GPIO6 I/O General-purpose input or output
GPIO7 I/O General-purpose input or output
I2Ct_IRQ(GPIO10) O IRQ for optional I2Ct, or used as a general-purpose output
GPIO11 O General-purpose output
I2Cc_IRQ(GPIO12) I IRQ for I2Cc, or used as a general-purpose input
8.3.9.2 I2C Interface
The TPS25751 features two I2C interfaces that uses an I2C I/O driver like the one shown in Figure 8-25. This I/O
consists of an open-drain output and an input comparator with de-glitching.
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
 www.ti.com
40 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 41

#### Extracted tables

Table 1:

```text
I2Ct (Target) CBL_DET Digital Core Bias CTL and USB-PD I2Cc (Controller) ADC Read | 
 | ADC Read
```

#### Raw extracted text

```text
TPS25751
www.ti.com SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
50ns
I2C_DI
Deglitch
I2C_SDA/SCL
I2C_DO
Figure 8-25. I2C Buffer
8.3.10 Digital Core
Figure 8-26 shows a simplified block diagram of the digital core.
GPIOx
I2Ct_SDA
I2C to I2Ct_SCL I2Ct
System Control (Target)
I2Ct_IRQ
CBL_DET
Digital Core Bias CTL USB PD Phy
I2Cc_SDA and USB-PD
I2C to I2Cc
Battery Charger I2Cc_SCL (Controller)
I2Cc_IRQ
OSC
ADC Read
Thermal Temp
Shutdown Sense ADC
Figure 8-26. Digital Core Block Diagram
8.3.11 I2C Interface
The TPS25751 has one I2C target interface ports: I2Ct. I2C port I2Ct is comprised of the I2Ct_SDA, I2Ct_SCL,
and I2Ct_IRQ pins. This interface provide general status information about the TPS25751, as well as the
ability to control the TPS25751 behavior, supporting communications to/from a connected device and/or cable
supporting BMC USB-PD, and providing information about connections detected at the USB-C receptacle.
When the TPS25751 is in 'APP ' mode TI recommends to use standard mode or Fast mode (that is a clock
speed no higher than 400 kHz). However, in the BOOT mode when a patch bundle is loaded Fast Mode Plus
can be used (see fSCLS).
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 41
Product Folder Links: TPS25751
```

### Page 42

#### Extracted tables

Table 1:

```text
I2C BUS | TYPE | TYPICAL USAGE
I2Ct | Target | Optionally can be connected to an external MCU. Also used to load the patch and application configuration.
I2Cc | Controller | Connect to a I2C EEPROM, Battery Charger. Use the LDO_3V3 pin as the pullup voltage. Multi- controller configuration is not supported.
```

Table 2:

```text
S
```

Table 3:

```text
P
```

#### Raw extracted text

```text
The TPS25751 has one I 2C controller interface port. I 2C is comprised of the I2C_SDA and I2C_SCL pins. This
interface can be used to read from or write to external target devices.
During boot, the TPS25751 attempts to read patch and Application Configuration data from an external
EEPROM with a 7-bit target address of 0x50. The EEPROM must be at least 36 kilo-bytes.
Table 8-4. I2C Summary
I2C BUS TYPE TYPICAL USAGE
I2Ct Target Optionally can be connected to an external MCU. Also used to load the patch and application
configuration.
I2Cc Controller Connect to a I2C EEPROM, Battery Charger. Use the LDO_3V3 pin as the pullup voltage. Multi-
controller configuration is not supported.
8.3.11.1 I2C Interface Description
The TPS25751 supports Standard and Fast mode I 2C interfaces. The bidirectional I 2C bus consists of the serial
clock (SCL) and serial data (SDA) lines. Both lines must be connected to a supply through a pullup resistor. Data
transfer can be initiated only when the bus is not busy.
A controller sending a Start condition, a high-to-low transition on the SDA input and output, while the SCL input
is high initiates I2C communication. After the Start condition, the device address byte is sent, most significant bit
(MSB) first, including the data direction bit (R/W).
After receiving the valid address byte, this device responds with an acknowledge (ACK), a low on the SDA
input/output during the high of the ACK-related clock pulse. On the I 2C bus, only one data bit is transferred
during each clock pulse. The data on the SDA line must remain stable during the high pulse of the clock period
as changes in the data line at this time are interpreted as control commands (Start or Stop). The controller sends
a Stop condition, a low-to-high transition on the SDA input and output while the SCL input is high.
Any number of data bytes can be transferred from the transmitter to receiver between the Start and the Stop
conditions. Each byte of eight bits is followed by one ACK bit. The transmitter must release the SDA line before
the receiver can send an ACK bit. The device that acknowledges must pull down the SDA line during the ACK
clock pulse, so that the SDA line is stable low during the high pulse of the ACK-related clock period. When a
target receiver is addressed, it must generate an ACK after each byte is received. Similarly, the controller must
generate an ACK after each byte that it receives from the target transmitter. Setup and hold times must be met to
ensure proper operation.
A controller receiver signals an end of data to the target transmitter by not generating an acknowledge (NACK)
after the last byte has been clocked out of the target. The controller receiver holding the SDA line high does this.
In this event, the transmitter must release the data line to enable the controller to generate a Stop condition.
Figure 8-27 shows the start and stop conditions of the transfer. Figure 8-28 shows the SDA and SCL signals for
transferring a bit. Figure 8-29 shows a data transfer sequence with the ACK or NACK at the last clock pulse.
PS
Start Condition Stop Condition
SDA
SCL
Figure 8-27. I2C Definition of Start and Stop Conditions
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
 www.ti.com
42 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 43

#### Extracted tables

Table 1:

```text
I2C ADDRESS INDEX | TARGET ADDRESS |  |  |  |  |  |  |  | AVAILABLE
(DECODED FROM ADCIN1 AND ADCIN2)(1) | BIT 7 | BIT 6 | BIT 5 | BIT 4 | BIT 3 | BIT 2 | BIT 1 | BIT 0 | DURING BOOT
#1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | R/W | Yes
#2 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | R/W | Yes
#3 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | R/W | Yes
#4 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | R/W | Yes
```

#### Raw extracted text

```text
Data Line Change
SDA
SCL
Figure 8-28. I2C Bit Transfer
SCL from
Controller
Figure 8-29. I2C Acknowledgment
8.3.11.1.1 I2C Clock Stretching
The TPS25751 features clock stretching for the I 2C protocol. The TPS25751 target I 2C port can hold the clock
line (SCL) low after receiving (or sending) a byte, indicating that it is not yet ready to process more data. The
controller communicating with the target must not finish the transmission of the current bit and must wait until the
clock line actually goes high. When the target is clock stretching, the clock line remains low.
The controller must wait until it observes the clock line transitioning high plus an additional minimum time (4 us
for standard 100-kbps I2C) before pulling the clock low again.
Any clock pulse can be stretched but typically it is the interval before or after the acknowledgment bit.
8.3.11.1.2 I2C Address Setting
The I2C controller must only use I2Ct_SCL/SDA for loading a patch bundle.
Once the boot process is complete, the port has a unique target address on the I2Ct_SCL/SDA bus as selected
by the ADCINx pins.
Table 8-5. I2C Default Target Address for I2Ct_SCL/SDA.
I2C ADDRESS INDEX
(DECODED FROM ADCIN1
AND ADCIN2)(1)
TARGET ADDRESS AVAILABLE
DURING BOOTBIT 7 BIT 6 BIT 5 BIT 4 BIT 3 BIT 2 BIT 1 BIT 0
#1 0 1 0 0 0 0 0 R/W Yes
#2 0 1 0 0 0 0 1 R/W Yes
#3 0 1 0 0 0 1 0 R/W Yes
#4 0 1 0 0 0 1 1 R/W Yes
(1) See Pin Strapping to Configure Default Behavior details about ADCIN1 and ADCIN2 decoding.
8.3.11.1.3 Unique Address Interface
The Unique Address Interface allows for complex interaction between an I 2C controller and a single TPS25751.
The I2C target sub-address is used to receive or respond to Host Interface protocol commands. Figure 8-30 and
Figure 8-31 show the write and read protocol for the I 2C target interface, and a key is included in Figure 8-32
www.ti.com
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 43
Product Folder Links: TPS25751
```

### Page 44

#### Extracted tables

Table 1:

```text
S | Unique Address | Wr | A | Register Number | A | Byte Count = N | A | Data Byte 1
```

Table 2:

```text
Data Byte 2 | A
```

Table 3:

```text
Data Byte N | A | P
```

Table 4:

```text
S | Unique Address | Wr | A | Register Number | A | Sr | Unique Address | Rd | A | Byte Count = N | A
```

Table 5:

```text
Data Byte 1 | A | Data Byte 2 | A
```

Table 6:

```text
Data Byte N | A | P
```

Table 7:

```text
S | Target Address | Wr | A | Data Byte | A | P
```

#### Raw extracted text

```text
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024 www.ti.com
to explain the terminology used. The key to the protocol diagrams is in the SMBus Specification and is repeated
here in part.
1 7 1 1 8 1 8 1 8 1
S Unique Address Wr A Register Number A Byte Count = N A Data Byte 1 A
8 1 8 1
Data Byte 2 A Data Byte N A P
Figure 8-30. I2C Unique Address Write Register Protocol
1 7 1 1 8 1 1 7 1 1 8 1
S Unique Address Wr A Register Number A Sr Unique Address Rd A Byte Count = N A
8 1 8 1 8 1
Data Byte 1 A Data Byte 2 A Data Byte N A P
1
Figure 8-31. I2C Unique Address Read Register Protocol
1 7 1 1 8 1 1
S Target Address Wr A Data Byte A P
x x
S Start condition
SR Repeated start condition
Rd Read (bit value of 1)
Wr Write (bit value of 0
X Field is required to have the value x
A Acknowledge (this bit position may be 0 for an ACK or 1 for a NACK)
P Stop condition
Controller-to-target
Target-to-controller
Continuation of protocol
Figure 8-32. I2C Read/Write Protocol Key
8.4 Device Functional Modes
8.4.1 Pin Strapping to Configure Default Behavior
During the boot procedure, the device reads the ADCINx pins and set the configurations based on the table
below. The device then attempts to load a configuration from an external EEPROM on the I2Cc bus. If no
EEPROM is detected, then the device waits for an external host to load a configuration.
When an external EEPROM is used, each device is connected to a unique EEPROM, and cannot be shared for
multiple devices. The external EEPROM is set at 7-bit target address 0x50.
44 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 45

#### Extracted tables

Table 1:

```text
ADCIN1 DECODED VALUE(2) | ADCIN2 DECODED VALUE(2) | I2C ADDRESS INDEX(1) | DEAD BATTERY CONFIGURATION
7 | 5 | #1 | AlwaysEnableSink: The device always enables the sink path regardless of the amount of current the attached source is offering. USB PD is disabled until configuration is loaded. This configuration is used with an external embedded controller. The embedded controller manages the battery charger in the system when present.
5 | 5 | #2 | 
2 | 0 | #3 | 
1 | 7 | #4 | 
7 | 3 | #1 | NegotiateHighVoltage: The device always enables the sink path during the initial implicit contract regardless of the amount of current the attached source is offering. The PD controller enters the 'APP ' mode, enable USB PD PHY and negotiate a contract for the highest power contract that is offered up to 20 V. The configuration cannot be used when a patch is loaded from EEPROM. This option is not recommended for systems that can boot from 5 V. This configuration is not valid to use with any supported battery chargers.
3 | 3 | #2 | 
4 | 0 | #3 | 
3 | 7 | #4 | 
7 | 0 | #1 | SafeMode: The device does not enable the sink path. USB PD is disabled until configuration is loaded. Note that the configuration can put the device into a source-only mode. This is recommended when the application loads the patch from EEPROM. This configuration is recommended when the PD controller manages the battery charger when present.
0 | 0 | #2 | 
6 | 0 | #3 | 
5 | 7 | #4 |
```

Table 2:

```text
| ACTIVE SOURCE MODE(1) | ACTIVE SINK MODE5 | IDLE SOURCE MODE | IDLE SINK MODE | MODERN STANDBY SOURCE MODE3 | MODERN STANDBY SINK MODE4 | SLEEP MODE2
PP_5V | enabled | disabled | enabled | disabled | enabled | disabled | disabled
```

#### Raw extracted text

```text
Table 8-6. Device Configuration using ADCIN1 and ADCIN2
ADCIN1 DECODED
VALUE(2)
ADCIN2 DECODED
VALUE(2)
I2C ADDRESS
INDEX(1) DEAD BATTERY CONFIGURATION
7 5 #1 AlwaysEnableSink: The device always enables the sink path
regardless of the amount of current the attached source is
offering. USB PD is disabled until configuration is loaded. This
configuration is used with an external embedded controller. The
embedded controller manages the battery charger in the system
when present.
5 5 #2
2 0 #3
1 7 #4
7 3 #1 NegotiateHighVoltage: The device always enables the sink path
during the initial implicit contract regardless of the amount of
current the attached source is offering. The PD controller enters
the 'APP ' mode, enable USB PD PHY and negotiate a contract
for the highest power contract that is offered up to 20 V. The
configuration cannot be used when a patch is loaded from
EEPROM. This option is not recommended for systems that can
boot from 5 V. This configuration is not valid to use with any
supported battery chargers.
3 3 #2
4 0 #3
3 7 #4
7 0 #1 SafeMode: The device does not enable the sink path. USB
PD is disabled until configuration is loaded. Note that the
configuration can put the device into a source-only mode. This
is recommended when the application loads the patch from
EEPROM. This configuration is recommended when the PD
controller manages the battery charger when present.
0 0 #2
6 0 #3
5 7 #4
(1) See Table 8-5 to see the exact meaning of I2C Address Index.
(2) See Table 8-2 for how to configure a given ADCINx decoded value.
8.4.2 Power States
The TPS25751 can operate in one of three different power states: Active, Idle, or Sleep. The Modern Standby
mode is a special case of the Idle mode. The functionality available in each state is summarized in Table
8-7. The device automatically transitions between the three power states based on the circuits that are active
and required. See Figure 8-33. In the Sleep state, the TPS25751 detects a Type-C connection. Transitioning
between the Active mode to Idle mode requires a period of time (T) without any of the following activity:
* Incoming USB PD message
* Change in CC status
* GPIO input event
* I2C transactions
* Voltage alert
* Fault alert
Sleep State
No CC connection
Active State Idle State
CC connected
New
activity
 CC detached & No activity for T
CC attached &
No new activity for T
New activity
Figure 8-33. Flow Diagram for Power States
Table 8-7. Power Consumption States
ACTIVE
SOURCE
MODE(1)
ACTIVE SINK
MODE5
IDLE SOURCE
MODE
IDLE SINK
MODE
MODERN
STANDBY
SOURCE
MODE3
MODERN
STANDBY
SINK MODE4
SLEEP MODE2
PP_5V enabled disabled enabled disabled enabled disabled disabled
www.ti.com
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 45
Product Folder Links: TPS25751
```

### Page 46

#### Extracted tables

Table 1:

```text
| ACTIVE SOURCE MODE(1) | ACTIVE SINK MODE5 | IDLE SOURCE MODE | IDLE SINK MODE | MODERN STANDBY SOURCE MODE3 | MODERN STANDBY SINK MODE4 | SLEEP MODE2
PP_HV (TPS25751D) | disabled | enabled | disabled | enabled | disabled | disabled | disabled
PP_EXT (TPS25751S) | disabled | enabled | disabled | enabled | disabled | disabled | disabled
PP_CABLE | enabled | enabled | enabled | enabled | disabled | disabled | disabled
external CC1 termination | Rd | Rp 3.0A | Rd | Rp 3.0A | open | open | open
external CC2 termination | open | open | open | open | open | open | open
```

#### Raw extracted text

```text
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024 www.ti.com
Table 8-7. Power Consumption States (continued)
MODERN
ACTIVE MODERN
ACTIVE SINK IDLE SOURCE IDLE SINK STANDBY
SOURCE STANDBY SLEEP MODE2
MODE5 MODE MODE SOURCE
MODE(1) SINK MODE4
MODE3
PP_HV
disabled enabled disabled enabled disabled disabled disabled
(TPS25751D)
PP_EXT
disabled enabled disabled enabled disabled disabled disabled
(TPS25751S)
PP_CABLE enabled enabled enabled enabled disabled disabled disabled
external CC1
Rd Rp 3.0A Rd Rp 3.0A open open open
termination
external CC2
open open open open open open open
termination
(1) This mode is used for: I .
VIN_3V3,ActSrc
(2) This mode is used for: I
VIN_3V3,Sleep
(3) This mode is used for: P
MstbySrc
(4) This mode is used for: P
MstbySnk
(5) This mode is used for: I
VIN_3V3,ActSnk
8.5 Thermal Shutdown
The TPS25751 features a central thermal shutdown as well as independent thermal sensors for each internal
power path. The central thermal shutdown monitors the overall temperature of the die and disables all functions
except for supervisory circuitry when die temperature goes above a rising temperature of T . The
SD_MAIN
temperature shutdown has a hysteresis of T and when the temperature falls back below this value,
SDH_MAIN
the device resumes normal operation.
The power path thermal shutdown monitors the temperature of each internal PP5V-to-VBUS power path and
disables both power paths and the VCONN power path when either exceeds T . Once the temperature
SD_PP5V
falls by at least T , the path can be configured to resume operation or remain disabled until re-enabled
SDH_PP5V
by firmware.
46 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 47

#### Extracted tables

Table 1:

```text
|  | TPS25751D 5A SW 3A SW CC Control and Vconn *BC1.2 I2C Controller *ADC + GPIO I2C GPIO Target
 |  | I2C Target
```

Table 2:

```text
I2C Target #1 |  |
```

Table 3:

```text
*BC1.2
*ADC + GPIO
```

Table 4:

```text
|  | I2C Controller
```

Table 5:

```text
Liquid Detection |
```

Table 6:

```text
I2C Controller Host Control | C Controller
```

Table 7:

```text
|  | I2Ct_SDA
 |  | I2Ct_SCL
 |  | I2Ct_IRQ
```

#### Raw extracted text

```text
TPS25751
www.ti.com SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
9 Application and Implementation
Note
Information in the following applications sections is not part of the TI component specification,
and TI does not warrant its accuracy or completeness. TIs customers are responsible for
determining suitability of components for their purposes, as well as validating and testing their design
implementation to confirm system functionality.
9.1 Application Information
The TPS25751 is a stand-alone Type-C PD controller for power-only USB-PD applications. Initial device
configuration is configured from an external EEPROM through a firmware configuration bundle loaded on to
the device during boot. The bundle is loaded over I2C from an external EEPROM. The TPS25751 firmware
configuration can be customized for each specific application. The firmware configuration can be generated
through the Web Tool.
The TPS25751 is ideal for single port power applications supporting the following PD architectures.
* Designs for both Power Provider (Source) and Power Consumer (Sink)
* Designs for Power Consumer (Sink)
An external EEPROM is required to download a pre-configured firmware on the TPS25751 device through the
I2C interface.
The TPS25751 firmware can be configured using the Web Tool for the application-specific PD charging
architecture requirements and data roles. The tool also provides additional optional firmware configuration that
integrates control for select Battery Charger Products (BQ). The TPS25751 I2C controller interfaces with the
Battery Chargers with pre-configured GPIO settings and I2C controller events. The Application Customization
Tool available with the TPS25751 provides details of the supported Battery Charger Products (BQ).
9.2 Typical Application
The following show the block diagrams for various applications. Note that some of these features are GPIO
usage dependent.
TPS25751D USB Type-C
Connector
5A
SW
PPHV VBUS
BAT VIN 3A VBUS
SW
PP5V
System 5V
Battery Charger CCx/Vconn
CCx/Vconn
CC Control
and Vconn
DP
I2C Target #1 *BC1.2
DM
I2Cc_SDA I2C
I I 2 2 C C c c _ _ S IR C Q L Controller *ADC + Liquid SBU1
GPIO Detection SBU2
EEPROM I2C Target #2
SSTX1/RX1
GND I2C Controller I I 2 2 C C t t _ _ S S D C A L Ta I2 rg C e t GPIO G SS N T D X2/RX2
I2Ct_IRQ
Host Control
GND
SSTX/RX USB SS Mux
Figure 9-1. TPS25751D Battery Charger & Full System Block Diagram
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 47
Product Folder Links: TPS25751
```

### Page 48

#### Extracted tables

Table 1:

```text
BAT VIN Battery Charger I2C Target #1 |  | 
 | I2C Target #1 |
```

Table 2:

```text
|  | 3A SW CC Control and Vconn *BC1.2 I2C TPS25751S Controller *ADC + GPIO I2C GPIO Target
 |  | I2C Target
```

Table 3:

```text
*BC1.2
*ADC + GPIO
```

Table 4:

```text
|  | I2C Controller
```

Table 5:

```text
Liquid Detection |
```

Table 6:

```text
|  | I2Ct_SDA
 |  | I2Ct_SCL
 |  | I2Ct_IRQ
```

Table 7:

```text
PG | I2CTarget
```

Table 8:

```text
I2Cc_SDA
I2Cc_SCL
```

Table 9:

```text
I2C Controller
GPIO
```

#### Raw extracted text

```text
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024 www.ti.com
5A
USB Type-C
SW Connector
PPEXT
BAT VIN
VBUS
3A VBUS
SW
PP5V
Battery Charger System 5V
CCx/Vconn
CCx/Vconn
CC Control
and Vconn
DP
I2C Target #1 *BC1.2
DM
I2Cc_SDA I2C TPS25751S
I I 2 2 C C c c _ _ S IR C Q L Controller *ADC + Liquid SBU1
GPIO Detection SBU2
EEPROM I2C Target #2
SSTX1/RX1
GND I2C Controller I I 2 2 C C t t _ _ S S D C A L Ta I2 rg C e t GPIO G SS N T D X2/RX2
I2Ct_IRQ
Host Control
GND
SSTX/RX USB SS Mux
Figure 9-2. TPS25751S Battery Charger & Full System Block Diagram
5A
SW
PPHV
BAT VIN
3A
Battery Charger SW
PP5V VBUS
System 5V
PG I2CTarget TPS25751D CCx USB Type-C
Vconn
Connector
GND GND
I2Cc_SDA
I2Cc_SCL I2C Controller
I2Cc_IRQ
GPIO
Figure 9-3. TPS25751D Battery Charger System Block Diagram
48 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 49

#### Extracted tables

Table 1:

```text
PG | I2C Target
```

Table 2:

```text
I2C Controller
GPIO
```

Table 3:

```text
Power Path | PD Power Source | VBUS Voltage | VBUS Current
TPS25751D - PPHV | 60W/100W | 5V - 21V (20mV Steps) | 3A/5A (50mA Steps)
TPS25751S - PPEXT | 60W/100W | 5V - 21V (20mV Steps) | 3A/5A (50mA Steps)
```

Table 4:

```text
Power Path | PD Power Sink | VBUS Voltage | VBUS Current
TPS25751D - PPHV | 60W/100W | 5V - 21V | 3A/5A
TPS25751S - PPEXT | 60W/100W | 5V - 21V | 3A/5A
```

#### Raw extracted text

```text
TPS25751S
I2C Controller
USB Type-C
Connector
SW
SW VBUS
5A
GND
CCx
Vconn
I2Cc_SDA
I2Cc_SCL
I2Cc_IRQ
Battery Charger
PPEXT
System 5V PP5V
GND
I2C Target
BAT VIN
PG
GPIO
3A
Figure 9-4. TPS25751S Battery Charger System Block Diagram
9.2.1 Design Requirements
9.2.1.1 Programmable Power Supply (PPS) - Design Requirements
Programmable Power Supply (PPS) defines a specific voltage and current (Augmented Power Data Object)
that is used in direct charging applications. A PPS source needs to meet the source voltage and current
resolution required for direct charging applications. A PPS sink requests the voltage and current required for
direct charging within the capabilities of PPS source.
Table 9-1. PPS Source 60W/100W Requirements
Power Path PD Power Source VBUS Voltage VBUS Current
TPS25751D - PPHV 60W/100W 5V - 21V (20mV Steps) 3A/5A (50mA Steps)
TPS25751S - PPEXT 60W/100W 5V - 21V (20mV Steps) 3A/5A (50mA Steps)
Table 9-2. PPS Sink 60W/100W Requirements
Power Path PD Power Sink VBUS Voltage VBUS Current
TPS25751D - PPHV 60W/100W 5V - 21V 3A/5A
TPS25751S - PPEXT 60W/100W 5V - 21V 3A/5A
9.2.1.2 Liquid Detection Design Requirements
Portable Type-C and PD applications are subject to environments that wet the Type-C connector. Liquid on
the Type-C connector leads to corrosion or system damage. Detecting liquid leverages the SBU1/2 pins on the
Type-C connector to not interfere with USB2/3 operation or PD communication.
www.ti.com
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 49
Product Folder Links: TPS25751
```

### Page 50

#### Extracted tables

Table 1:

```text
|  | VBUS |  |  | 
 |  | CCx |  |  | 
3.3V 3.3V FET Control Liquid Detection + Protection Circuit |  | USBType-C Connector SBU1 |  |  | 
 |  | SBU2 |  |  | 
 |  | GND |  |  |
```

Table 2:

```text
VBUS CCx LDO_3V3 GPIOx/y TPS25751 GPIO4 GPIO5 GND | VBUS
 | GND
```

Table 3:

```text
GPIOx/y
GPIO4
GPIO5
```

#### Raw extracted text

```text
TPS25751
LDO_3V3
GPIOx/y
GPIO4
GND
GPIO5
USB Type-C
Connector
SBU1
SBU2
GND
Liquid Detection +
Protection Circuit
VBUS
CCx
VBUS
CCx
0V - 20V
0V - 3.3V (5V
for Vconn)
0V
3.3V
FET Control
RSaV RSaCC
RSaG
3.3V
Figure 9-5. Liquid Detection Cases
9.2.1.3 BC1.2 Application Design Requirements
The PD controller taps the USB D+ and D- pins to provide BC1.2 detection and advertisement. The USB D+ and
D- are connected to the USB Host (DFP) or USB Device (UFP) from the Type-C connector for Charging Data
Port applications.
9.2.1.4 USB Data Support Design Requirements
For USB3 operation, the SSTX/RX are muxed to the Type-C connector. A SuperSpeed Mux generally has two
control signals; enable and plug orientation. The PD controller determines when a connection is detected and
drives the required GPIO to control the SuperSpeed Mux.
9.2.2 Detailed Design Procedure
9.2.2.1 Programmable Power Supply (PPS)
The TPS25751 supports Programmable Power Supply (PPS) source and sink. When the TPS25751 negotiates
a PPS contract as a source, the device enables the high-voltage power path (PPHV for D variant, PPEXT
for S variant) and communicate with the supported TI battery charger (BQ25792 and BQ25756) to supply the
negotiated voltage. TPS25751 only supports PPS within a 5V to 21V range according to PD 3.1 specification
and is enabled through the Application Customization Tool.
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
 www.ti.com
50 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 51

#### Extracted tables

Table 1:

```text
PG | I2CTarget
```

Table 2:

```text
I2Cc_SDA
I2Cc_SCL
```

Table 3:

```text
I2C Controller
GPIO
```

Table 4:

```text
PG | I2C Target
```

Table 5:

```text
I2C Controller
GPIO
```

#### Raw extracted text

```text
TPS25751D
I2C Controller
I2Cc_SDA
I2Cc_SCL
I2Cc_IRQ
Battery Charger
USB Type-C
Connector
SW
SW VBUS
5A
PPHV
GND
System 5V PP5V
GND
CCx
Vconn
VINBAT
3A
PG I2C Target
GPIO
Figure 9-6. TPS25751D PPS with Battery Charger
TPS25751S
I2C Controller
USB Type-C
Connector
SW
SW VBUS
5A
GND
CCx
Vconn
I2Cc_SDA
I2Cc_SCL
I2Cc_IRQ
Battery Charger
PPEXT
System 5V PP5V
GND
I2C Target
BAT VIN
PG
GPIO
3A
Figure 9-7. TPS25751S PPS with Battery Charger
9.2.2.2 Liquid Detection
The TPS25751 supports liquid detection using the built-in internal ADC and GPIO with external circuitry. Figure
9-8 and Figure 9-9 show the hardware implementation for liquid detection with the TPS25751. The TPD2S300
is used to protect the GPIO, ADC, and LDO_3V3 pins from over voltage conditions when there is liquid shorting
VBUS to the SBU1/2 pins. Table 9-3 shows the recommended components used to implement the external liquid
detection circuitry. When liquid is detected, the TPS25751 takes action to protect the Type-C port. Systems using
an embedded host controller, can leverage the Host Interface for additional notification and control.
www.ti.com
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 51
Product Folder Links: TPS25751
```

### Page 52

#### Extracted tables

Table 1:

```text
LDO_3V3 GPIOx GPIO4 TPS25751 GPIO5 GPIOy GND | LDO_3V3
 | GND
```

Table 2:

```text
GPIO4
GPIO5
```

Table 3:

```text
LDO_3V3 GPIOx GPIO4 TPS25751 GPIO5 GND | LDO_3V3
 | GND
```

Table 4:

```text
GPIO4
GPIO5
```

Table 5:

```text
Q_Pn (GPIO PMOS) | Q_Nn (GPIO NMOS) | Rup | Rdown
CSD25480F3 (Vgsth -0.95V or similar) | CSD15380F3 (Vgsth 1.1V or similar) | 100kOhm (5%) | 1MOhm (5%)
```

#### Raw extracted text

```text
TPS25751
Rup
Rdown
LDO_3V3
GPIOx
GPIO4
GPIOy
GND
Rup
Rdown
GPIO5
USB Type-C
Connector
SBU1
SBU2
GND
TPD2S300
C_CC1
C_CC2
CC1
CC2
Liquid Detection +
Protection Circuit
Q_P1 Q_P2
Q_N1 Q_N2
3.3V
Figure 9-8. TPS25751 Liquid Detection Block Diagram - 2 GPIO Control
TPS25751
Rup
Rdown
LDO_3V3
GPIOx
GPIO4
GND
Rup
Rdown
GPIO5
USB Type-C
Connector
SBU1
SBU2
GND
TPD2S300
C_CC1
C_CC2
CC1
CC2
Liquid Detection +
Protection Circuit
Q_P1 Q_P2
Q_N1 Q_N2
3.3V
Figure 9-9. TPS25751 Liquid Detection Block Diagram - 1 GPIO Control
Table 9-3. Component Recommendation
Q_Pn (GPIO PMOS) Q_Nn (GPIO NMOS) Rup Rdown
CSD25480F3 (Vgsth -0.95V or
similar)
CSD15380F3 (Vgsth 1.1V or
similar) 100kOhm (5%) 1MOhm (5%)
9.2.2.2.1 Liquid Detection Operation
The TPS25751 supports liquid detection by measuring the voltage level across the SBU pins of the Type-C
connector. When a short occurs across the SBU pins to another Type-C pin(s), the TPS25751 takes action to
protect the the Type-C port by disabling the power paths and notifies the embedded controller when applicable.
Once liquid has been detected, the TPS25751 continuously monitors the SBU voltage. During the SBU voltage
monitoring, if the liquid/short is no longer present the TPS25751 takes action to return to normal operation.
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
 www.ti.com
52 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 53

#### Extracted tables

Table 1:

```text
|  | VBUS |  |  | 
 |  | CCx |  |  | 
3.3V 3.3V FET Control Liquid Detection + Protection Circuit |  | USBType-C Connector SBU1 |  |  | 
 |  | SBU2 |  |  | 
 |  | GND |  |  |
```

Table 2:

```text
VBUS CCx LDO_3V3 GPIOx/y TPS25751 GPIO4 GPIO5 GND | VBUS
 | GND
```

Table 3:

```text
GPIOx/y
GPIO4
GPIO5
```

#### Raw extracted text

```text
VBUS
VBUS 0V - 20V
CCx 0V - 3.3V (5V
CCx
for Vconn)
3.3V
LDO_3V3
USBType-C RSaV RSaCC
3.3V Connector
GPIOx/y FET Control
TPS25751 SBU1
GPIO4
SBU2
GPIO5
Liquid Detection +
Protection Circuit
RSaG
GND
GND 0V
Figure 9-10. TPS25751 Liquid Detection Operation
9.2.2.3 BC1.2 Application
The TPS25751 supports BC1.2 detection and advertisement modes and are configurable through the Web Tool.
TPS25751
VBUS
CCx/Vconn
USB Type-C
GPIO4 D+ Connector
GPIO5 D-
GND
200
(cid:1)
TPS25751
www.ti.com SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
VBUS
CCx/Vconn
SW
1.2 V
CDP
Detect
SW
2.7 V
GPIO
USB
USB2.0 Mux
Host
Figure 9-11. BC1.2 Application Block Diargam
9.2.2.4 USB Data Support
The TPS25751 supports USB data speed up to USB 3.2 Gen 2. When entering USB enumeration, the
TPS25751 controls USB SuperSpeed Mux (TUSB1142) using GPIO controls. The GPIO control is configured
through using the Application Customization Tool, GPIO events are found in the Technical Reference Manual.
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 53
Product Folder Links: TPS25751
```

### Page 54

#### Extracted tables

Table 1:

```text
|  | TPS25751D 5A SW 3A SW CC Control and Vconn *BC1.2 I2C Controller *ADC + GPIO I2C GPIO Target
 |  | I2C Target
```

Table 2:

```text
BAT VIN Battery Charger I2C Target #1 |  |  | 
 | I2C Target #1 |  |
```

Table 3:

```text
*BC1.2
*ADC + GPIO
```

Table 4:

```text
|  | I2C Controller
```

Table 5:

```text
Liquid Detection |
```

Table 6:

```text
I2C Controller Host Control | I2C Controller
```

Table 7:

```text
|  | I2Ct_SDA
 |  | I2Ct_SCL
 |  | I2Ct_IRQ
```

Table 8:

```text
BAT VIN Battery Charger I2C Target #1 |  | 
 | I2C Target #1 |
```

Table 9:

```text
|  | 3A SW CC Control and Vconn *BC1.2 I2C TPS25751S Controller *ADC + GPIO I2C GPIO Target
 |  | I2C Target
```

Table 10:

```text
*BC1.2
*ADC + GPIO
```

Table 11:

```text
|  | I2C Controller
```

Table 12:

```text
Liquid Detection |
```

Table 13:

```text
I2C Controller Host Control | I2C Controller
```

Table 14:

```text
|  | I2Ct_SDA
 |  | I2Ct_SCL
 |  | I2Ct_IRQ
```

#### Raw extracted text

```text
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024 www.ti.com
TPS25751D USB Type-C
Connector
5A
SW
PPHV VBUS
BAT VIN 3A VBUS
SW
PP5V
System 5V
Battery Charger CCx/Vconn
CCx/Vconn
CC Control
and Vconn
DP
I2C Target #1 *BC1.2
DM
I2Cc_SDA I2C
I I 2 2 C C c c _ _ S IR C Q L Controller *ADC + Liquid SBU1
GPIO Detection SBU2
EEPROM I2C Target #2
SSTX1/RX1
GND I2C Controller I I 2 2 C C t t _ _ S S D C A L Ta I2 rg C e t GPIO G SS N T D X2/RX2
I2Ct_IRQ
Host Control
GND
SSTX/RX USB SS Mux
Figure 9-12. TPS25751D USB Data Support
5A
USB Type-C
SW Connector
PPEXT
BAT VIN
VBUS
3A VBUS
SW
PP5V
Battery Charger System 5V
CCx/Vconn
CCx/Vconn
CC Control
and Vconn
DP
I2C Target #1 *BC1.2
DM
I2Cc_SDA I2C TPS25751S
I I 2 2 C C c c _ _ S IR C Q L Controller *ADC + Liquid SBU1
GPIO Detection SBU2
EEPROM I2C Target #2
SSTX1/RX1
GND I2C Controller I I 2 2 C C t t _ _ S S D C A L Ta I2 rg C e t GPIO G SS N T D X2/RX2
I2Ct_IRQ
Host Control
GND
SSTX/RX USB SS Mux
Figure 9-13. TPS25751S USB Data Support
9.2.3 Application Curves
9.2.3.1 Programmable Power Supply (PPS) Application Curves
The following are captured when the TPS25751 is acting as a PPS Source. The VBUS plot shows the PPS
negotiation increasing and decreasing from 5V to 21V to 5V. The PD negotiation snap shot shows the VBUS
requested voltage increasing by 100mV.
54 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 55

#### Raw extracted text

```text
Figure 9-14. PPS PD Negotiation VBUS Increasing/Decreasing
Figure 9-15. PPS PD Negotiation Log
9.2.3.2 Liquid Detection Application Curves
The figures below show the liquid detection behavior with corrosion mitigation disabled and enabled. Liquid is
detected on both Figure 9-16 and Figure 9-17 on the SBU2 pin.
www.ti.com
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 55
Product Folder Links: TPS25751
```

### Page 56

#### Raw extracted text

```text
Figure 9-16. Liquid Detection Behavior - No Corrosion Mitigation
Figure 9-17. Liquid Detection Behavior - Corrosion Mitigation
Liquid Detection occurs in burst which can be configured. When the PD Controller checks for liquid it toggles the
SBU1/2 circuitry, and pulls down the SBU1/2 circuitry when liquid detection is disabled.
Liquid Detec
(cid:1)
on Enabled Liquid Detec
(cid:0)
on Disabled Liquid Detec
(cid:2)
on Enabled Liquid Detec
(cid:3)
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024 www.ti.com
on Disabled
SBU Toggle SBU Low SBU Toggle SBU Low
Figure 9-18. Liquid Detection and SBU1/2 Toggle
9.2.3.3 BC1.2 Application Curves
The plots below show the BC1.2 advertisement and detection with the TPS25751.
56 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 57

#### Raw extracted text

```text
Figure 9-19. BC1.2 DCP Advertisement
Figure 9-20. BC1.2 CDP Advertisement
www.ti.com
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 57
Product Folder Links: TPS25751
```

### Page 58

#### Raw extracted text

```text
Figure 9-21. BC1.2 DCP Detection
Figure 9-22. BC1.2 CDP Detection
9.2.3.4 USB Data Support Application Curves
The following show the control signals used by a USB SuperSpeed Mux. For a normal orientation, the CC1 pin is
connected. For a flipped orientation, the CC2 pin is connected.
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
 www.ti.com
58 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 59

#### Raw extracted text

```text
Figure 9-23. USB SuperSpeed Mux Control - Normal Orientation
Figure 9-24. USB SuperSpeed Mux Control - Flipped Orientation
9.3 Power Supply Recommendations
9.3.1 3.3-V Power
9.3.1.1 VIN_3V3 Input Switch
The VIN_3V3 input is the main supply of the TPS25751 device. The VIN_3V3 switch (see Power Management)
is a uni-directional switch from VIN_3V3 to LDO_3V3, not allowing current to flow backwards from LDO_3V3
to VIN_3V3. This switch is on when the 3.3-V supply is available and the dead-battery flag is cleared. The
www.ti.com
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 59
Product Folder Links: TPS25751
```

### Page 60

#### Extracted tables

Table 1:

```text
Route | Minimum Width (mils)
CC1, CC2 | 10
VIN_3V3, LDO | 10
Component GND | 16
```

#### Raw extracted text

```text
recommended capacitance C VIN_3V3 (see Recommended Capacitance) must be connected from the VIN_3V3
pin to the GND pin).
9.3.2 1.5-V Power
The internal circuitry is powered from 1.5 V. The 1.5-V LDO steps the voltage down from LDO_3V3 to 1.5 V. The
1.5-V LDO provides power to all internal low-voltage digital circuits which includes the digital core, and memory.
The 1.5-V LDO also provides power to all internal low-voltage analog circuits. Connect the recommended
capacitance CLDO_1V5 (see Recommended Capacitance) from the LDO_1V5 pin to the GND pin.
9.3.3 Recommended Supply Load Capacitance
Recommended Capacitance  lists the recommended board capacitances for the various supplies. The typical
capacitance is the nominally rated capacitance that must be placed on the board as close to the pin as possible.
The maximum capacitance must not be exceeded on pins for which it is specified. The minimum capacitance is
minimum capacitance allowing for tolerances and voltage derating ensuring proper operation.
9.4 Layout
9.4.1 TPS25751D - Layout
9.4.1.1 Layout Guidelines
Proper routing and placement maintain signal integrity for high speed signals and improve the heat dissipation
from the power paths. The combination of power and high speed data signals are easily routed if the following
guidelines are followed. Best practice is to consult with board manufacturing to verify manufacturing capabilities.
9.4.1.1.1 Recommended Via Size
Proper via stitching is recommended to carrying current for the VBUS power paths and grounding. The
recommended minimum via size is shown below, but larger vias are an option for low density PCB designs.
A single via is capable of carrying 1A, verify the tolerance with the board manufacturing. Vias are recommended
to be tented when located close to the PD controller.
16mil8mil
Figure 9-25. Recommend Minimum Via Size
9.4.1.1.2 Minimum Trace Widths
Below are the minimum trace widths for analog and digital pins. The trace width limitations are also defined by
the board manufacturing process used. Consult with manufacturing for determining the minimum trace widths
and tolerance.
Table 9-4. Minimum Trace Width
Route Minimum Width (mils)
CC1, CC2 10
VIN_3V3, LDO 10
Component GND 16
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
 www.ti.com
60 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 61

#### Extracted tables

Table 1:

```text
Route | Minimum Width (mils)
GPIO | 4
```

Table 2:

```text
6
7
19
26
27 37 36
```

Table 3:

```text
C1 4.7uF | C2 0.01uF | C3 0.01uF | C4 0.01uF
```

Table 4:

```text
33 | 33
23 24 25 |
```

Table 5:

```text
C6 100uF | C7 100uF | C8 10uF
```

Table 6:

```text
GND GND SSTXp1 SSRXp1 SSTXn1 SSRXn1 VBUS VBUS CC1 SBU2 Dp1 Dn2 Dn1 Dp2 SBU1 CC2 VBUS VBUS SSRXn2 SSTXn2 SSRXp2 SSTXp2 GND GND SHIELD SHIELD SHIELD SHIELD | B11 B10 B9 B8 | 
 | B7 B6 | 
 | B5 B4 | 
 | B3 B2 B1 | 
 | S3 | 
 | S4 |
```

Table 7:

```text
|  |  | 10
 |  |  | 17 16
```

#### Raw extracted text

```text
Table 9-4. Minimum Trace Width (continued)
Route Minimum Width (mils)
GPIO 4
9.4.1.2 Layout Example
9.4.1.2.1 TPS25751D Schematic Layout Example
Follow the differential impedances for Super / High Speed signals defined by their specifications (USB2.0). All
I/O are fanned out to provide an example for routing out all pins, not all designs utilize all of the I/O on the
TPS25751D.
P3V3
U1
VBUS GND C 4. 1 7u P F P5V C 0. 2 01uF 1 C 0 6 C 0 0 u . 3 0 F 1uF 1 C 0 7 C 0 0 u . 4 0 F 1uF 1 C 0 8 C u 0 F . 5 01uF 1 C 0 9 uF L L D D O O _ _ 3 1 V V 3 5 3 2 3 3 2 3 3 2 4 3 4 5 8 5 2 3 4 1 P V L V V V P L V V D D P P B B B B B IN 5 5 O O U U U U U V V _ S S S S S _ _ 3 3 1 _ _ _ V V I V I I 3 N N N 3 5 G G P P I I O O 5 4 / / U D U S R S B A B _ A A I _ G N N D D D D G G G G G P G P _ / / R R C C P P P P P I P M M P O A A I I I I I I I I A O O O O O D N O D N 1 I I D N N 2 2 1 0 2 6 7 3 1 1 1 5 7 2 3 3 6 1 2 3 1 1 3 4 2 9 6 6 3 5 0 0 7 7 D A A R D D A C C I I I N N N 1 2 G G G G G G G G G P P P P P P P P P I I I I I I I I I O O O O O O O O O 0 1 2 3 4 5 6 7 11
GND C C C C 2 1 2 28 9 C C C C 1 2
V V B B C U U C S S 1 A A A A A A A A A A A 1 1 A 1 5 0 2 2 3 4 6 7 8 9 1 1 J1 G S S V C D D S V S S G B B B S S S S C p n N N 1 1 U U U R R T T 1 D D X X S 1 S X X p n n p 1 1 2 2 S S S S S S S S V V S T T R R G G B B C B D D X X X X U U N N U C n p p n p n S S D D 2 2 2 2 2 2 1 1 B B B B B B B B B B B B 1 1 1 9 8 5 4 3 2 1 6 7 1 2 0 V V C B B C U U 2 S S I I I 2 I I 2 2 I 2 2 C 2 C C C C C c c t c t _ _ t _ _ _ _ S S S S I IR R D D C C Q Q A A L L R 10 6 kOhm R 2. 5 2kOhm R 2. 4 2kOhm R 10 3 kOhm R 2. 2 2kOhm R 2. 1 2kOhm 1 1 1 1 0 7 8 6 8 9 TP I I I I I I 2 2 2 2 2 2 S C C C C C C 2 c t c t c t L 5 _ _ _ _ _ _ D 7 S S I S S I O 5 R R C D C D 1 _ Q Q L A L D A 3V R 3 EFR LDO_1V5 GN P D 3V _ P P P G G G G P P P 3 P N N N N H H H AD V V V D D D D 2 3 2 3 1 1 2 1 2 2 1 0 1 1 9 4 GND C 22 12 uF C 22 13 uF GND C 0 1 .1 4 uF PPHV C 3 G 1 3 N 0 0 D pF C 3 1 3 1 0pF
S S 2 1 S S H H I I E E L L D D S S H H I I E E L L D D S S 3 4 LDO_3V3 C15 C16 C17
DX07S024JJ2R1300 10uF 10uF 10uF
GND GND
GND GND GND
4 5 6 N N N I I I D D D D N N N A G G G P 1 2 3 7
TPS25751
www.ti.com SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
U2 TVS2200DRVR
GND
Figure 9-26. TPS25751D Example Schematic
9.4.1.2.2 TPS25751D Layout Example - PCB Plots
The following TPS25751D PCB Layout figures show the recommended layout, placement, and routing.
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 61
Product Folder Links: TPS25751
```

### Page 62

#### Raw extracted text

```text
Figure 9-27. TPS25751D PCB Layout - Top Composite
Figure 9-28. TPS25751D PCB Layout - Bottom Composite
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
 www.ti.com
62 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 63

#### Raw extracted text

```text
Figure 9-29. TPS25751D PCB Layout - Top Layer Routing
Figure 9-30. TPS25751D PCB Layout - Internal Power Layer
www.ti.com
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 63
Product Folder Links: TPS25751
```

### Page 64

#### Raw extracted text

```text
Figure 9-31. TPS25751D PCB Layout - GND Layer
Figure 9-32. TPS25751D PCB Layout - Bottom Layer
9.4.1.2.2.1 TPS25751D Component Placement
LDO_1V5 (pin 4), LDO_3V3 (pin 1), and VIN_3V3 (pin 38)
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
 www.ti.com
64 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 65

#### Raw extracted text

```text
The decoupling capacitors for LDO_3V3, LDO_1V5, and VIN_3V3 (C15, C16, and C17 respectively) need to
be placed as close as possible to TPS25751D device for optimal performance. For this example to minimize
solution size, the decoupling capacitors are placed on the bottom layer with their ground pads directly
underneath the ground pad of TPS25751D. Use a maximum of one via per pin from TPS25751D to the
decoupling capacitors if placed on a different layer. Use a minimum of 10mil trace width to route these three
traces, preferably with 16mil trace width if possible.
CC1 (pin 28) and CC2 (pin 29)
CC1 (C11) and CC2 (C10) capacitors need to be placed as close as possible to their respective pins and on the
same layer as the TPS25751D device. When routing the CCx traces, DO NOT via to another layer in between
the CCx pins of the TPS25751D to the CCx capacitors. Check to make sure the CCx capacitors are not place
outside the CC trace creating an antenna, instead have the traces pass directly through the CCx capacitor pads
as shown in the example layout (refer to figure 10-14 ). Use a minimum of 10mil trace width to ensure Vconn
support (5V/0.6A).
9.4.1.2.2.2 TPS25751D PP5V
The 10uF decoupling capacitor (C9) need to be placed as close as possible to the PP5V pins of TPS25751D.
DO NOT use traces for PP5V. The PP5V power plane needs to be sized to support up to 3.6A (up to 3A for
sourcing, 600mA for Vconn). When connecting the PP5V pins (pins 34 and 35) to the 5V power plane, use a
minimum of 4 vias in parallel and close to the device to improve current sharing. Minimize the bottle necks cause
by other vias or traces, large bottle necks reduces the efficiency of the power plane.
The bulk capacitors (C6, C7, and C8) represent capacitances from the system 5V rail, these are placed further
away from TPS25751D on the same PP5V power plane. Refer to figure 10-14 and figure 10-15 for placement
and trace reference.
9.4.1.2.2.3 TPS25751D PPHV
Place the PPHV decoupling capacitors (C12, C13, and C14) as close as possible to TPS25751D, these do not
need to be on the same layer as the device. The PPHV power plane needs to be sized to support up to 5A
of current. When connecting the PPHV plane to a different layer, use a minimum of 6 vias in parallel per layer
change. It is highly recommended to have more than 6 vias if possible for layer change to improve current
sharing and efficiency.
9.4.1.2.2.4 TPS25751D VBUS
VBUS (pins 32 and 33) and VBUS_IN (pins 23, 24, and 25)
Place the VBUS decoupling capacitor (C1) as close as possible to TPS25751D, the capacitor does not need to
be on the same layer as the device. The VBUS power plane need to be sized to support up to 5A of current if
100W application is required. When connecting the VBUS pins (pins 32 and 33) plane to a different layer, use
a minimum of 3 vias per layer change. When connecting the VBUS_IN pins (pins 23, 24, and 25) plane to a
different layer, use a minimum of 6 vias per layer change. Refer to figure 10-14 and figure 10-15 for capacitors
and via placement.
At the Type-C port/connector, it is recommended to use minimum of 6 vias from the connector VBUS pins for
layer changes. Place the 10nF caps (C2, C3, C4, and C5) and the 22V TVS diode (U2) as close as possible to
the connector VBUS pins as shown in figure 10-15.
When routing the VBUS power plane from the Type-C connector to the TPS25751D VBUS pins, minimize bottle
necks caused by other vias and traces to improve current flow. The example layout shown in figure 10-17 uses
an internal layer to route the VBUS plane from the connector to TPS25751D.
9.4.1.2.2.5 TPS25751D I/O (I2C, ADCINs, GPIOs)
I2C, ADCIN1/2, and GPIO pins
Fan these traces out from the TPS25751D, use vias to connect the net to a routing layer if needed. For these
nets, use 4mil to 10mil trace width.
www.ti.com
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 65
Product Folder Links: TPS25751
```

### Page 66

#### Raw extracted text

```text
I2Cc_SDA/SCL/IRQ (pins 8, 9, and 10) and I2Ct_SCL/SDA/IRQ (pins 16, 17, and 18)
Minimize trace width changes to avoid I2C communication issues.
ADCIN1 and ADCIN2 (pins 2 and 3)
Keep the ADCINx traces away from switching elements. If a resistor divider is used, place the divider close to
LDO_3V3 or LDO_1V5.
GPIO (pins 5, 6, 7, 19, 26, 27, 37, 36, and 13)
Separate GPIO traces running in parallel by a trace width. Keep the GPIOx traces away from switching
elements.
9.4.1.2.2.6 TPS25751D DRAIN
The DRAIN pad is used to dissipate heat for the internal high voltage power path (PPHV). Connect the Drain
pins (pins 15 and 30) to the Drain pad underneath the TPS25751D device. Connect the through hole vias from
the drain pad on the top layer to a copper pour on the bottom layer to help dissipate heat. Additional vias can be
added to improve thermal dissipation.
9.4.1.2.2.7 TPS25751D GND
The GND pad is used to dissipate heat for the TPS25751D device. Connect the GND pins (pins 11, 12, 14 and
31) to the Ground pad underneath the TPS25751D device. Connect the through hole vias from the ground pad
on the top layer to a copper pour on the bottom layer to help dissipate heat. Additional vias can be added to
improve thermal dissipation.
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
 www.ti.com
66 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 67

#### Extracted tables

Table 1:

```text
Route | Minimum Width (mils)
CC1, CC2 | 10
VIN_3V3, LDO | 10
Component GND | 16
GPIO | 4
```

#### Raw extracted text

```text
TPS25751
www.ti.com SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
9.4.2 TPS25751S - Layout
9.4.2.1 Layout Guidelines
Proper routing and placement maintain signal integrity for high speed signals and improve the heat dissipation
from the power paths. The combination of power and high speed data signals are easily routed if the following
guidelines are followed. Best practice is to consult with board manufacturing to verify manufacturing capabilities.
9.4.2.1.1 Recommended Via Size
Proper via stitching is recommended to carrying current for the VBUS power paths and grounding. The
recommended minimum via size is shown below, but larger vias are an option for low density PCB designs.
A single via is capable of carrying 1A, verify the tolerance with the board manufacturing. Vias are recommended
to be tented when located close to the PD controller.
8mil 16mil
Figure 9-33. Recommend Minimum Via Size
9.4.2.1.2 Minimum Trace Widths
Below are the minimum trace widths for analog and digital pins. The trace width limitations are also defined by
the board manufacturing process used. Consult with manufacturing for determining the minimum trace widths
and tolerance.
Table 9-5. Minimum Trace Width
Route Minimum Width (mils)
CC1, CC2 10
VIN_3V3, LDO 10
Component GND 16
GPIO 4
9.4.2.2 Layout Example
9.4.2.2.1 TPS25751S Schematic Layout Example
Follow the differential impedances for Super / High Speed signals defined by their specifications (USB2.0). All
I/O are fanned out to provide an example for routing out all pins, not all designs utilize all of the I/O on the
TPS25751S.
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 67
Product Folder Links: TPS25751
```

### Page 68

#### Extracted tables

Table 1:

```text
C12 22uF | C13 22uF
```

Table 2:

```text
I I I DAP DNG DNG DNG | 
7 3 | 2
```

Table 3:

```text
6 7
18
22
23
31
30 13
```

Table 4:

```text
A2 A3 A4
A5
A6 A7 A8 A9
A10 A11 A12
S1
```

Table 5:

```text
B11 B10 B9 | 
B8 B7 B6 B5 | 
B4 | 
B3 B2 B1 | 
S3 |
```

Table 6:

```text
25 |  | 
 | C10 330pF |
```

#### Raw extracted text

```text
VBUS A B 1 1 A B 2 2 PPHV C12 C13 C14
C1 C2 C3 C4 C5 22uF 22uF 10uF 4.7uF 0.01uF 0.01uF 0.01uF 0.01uF
GND GND
P3V3
U1
V V B B C U U C S S 1 A A A A A A A A A A A 1 1 A 1 3 4 5 6 7 8 9 0 2 2 1 1 J1 G S S V C D D S V S S G B B B S S S S C p n N N 1 1 U U U R R T T 1 D D X X S 1 S X X p n n p 1 1 2 2 S S S S S S S S V V S T T R R G G B B C B D D X X X X N N U U U C n p p n p n D D S S 2 2 2 2 2 2 1 1 B B B B B B B B B B B B 1 1 1 9 8 5 4 3 2 1 6 7 1 2 0 V V C B B C U U 2 S S PP5V I I 2 I 2 2 C C C t t _ t _ _ S S IR D C Q A G L ND 1 C 0 6 0uF 1 C 0 7 0uF 1 C 0 9 uF L L D D O O _ _ 3 1 V V 3 5 2 2 2 2 3 1 2 0 6 7 8 9 8 4 9 1 V V I V L I I P P L 2 2 2 D D P P B B I C C C N 5 5 O O U U t t t V V _ S S _ _ _ _ _ 3 3 1 S S I V R V V C D 3 Q 3 5 L A G G P P I I O O 5 4 / / U G G U S A S A B T T B E _ E A A _ G _ N _ D G P D G G G G G P V V V / / C P C P P P P I P M M B S C S O C I I I I I I I I U O D O O O O D Y N O C Y N C 1 S S S 2 6 2 1 2 1 0 2 7 3 1 1 1 5 7 2 3 6 1 2 1 2 2 2 2 3 3 1 2 8 2 3 5 1 0 3 0 1 9 4 G G G G G G G G G A A D D P P P P P P P P P C C I I I I I I I I I O O O O O O O O O I I N N 0 1 2 3 4 5 6 7 11 1 2 C C C C 1 2
S S 2 1 DX S S H H 07 I I E E S L L 0 D D 24JJ2R S S 13 H H 0 I I E E 0 L L D D S S 3 4 I I 2 I 2 2 C C C c c c _ _ _ S S IR D C Q A L 1 1 1 5 6 7 I I I 2 2 2 C C C c c c _ _ _ S S IR C D Q L A G G G G N N N N D D D D 3 1 1 1 2 1 3 4 C 33 10 0pF C 3 1 3 1 0pF
GND GND TPS25751SRSMR
LDO_3V3 LDO_1V5 P3V3 GND GND
R6 R5 R4 R3 R2 R1
10kOhm 2.2kOhm2.2kOhm10kOhm 2.2kOhm2.2kOhm
LDO_3V3
GND GND GND
1C 2C
Q1 CSD87501L D1 D2
E1 E2
GATE_VBUS GATE_VSYS
VBUS C8 10uF GATE_VBUS GATE_VSYS PPHV
C15 C16 C17
10uF 10uF 10uF
4 5 6
N N N I I I
D D D D N N N A G G G P
1 2 3 7
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024 www.ti.com
U2 TVS2200DRVR
GND
Figure 9-34. TPS25751S Example Schematic
9.4.2.2.2 TPS25751S Layout Example - PCB Plots
The following TPS25751S PCB Layout figures show the recommended layout, placement, and routing.
Figure 9-35. TPS25751S PCB Layout - Top Composite
68 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 69

#### Raw extracted text

```text
Figure 9-36. TPS25751S PCB Layout - Bottom Composite
Figure 9-37. TPS25751S PCB Layout - Top Layer Routing
www.ti.com
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 69
Product Folder Links: TPS25751
```

### Page 70

#### Raw extracted text

```text
Figure 9-38. TPS25751S PCB Layout - Internal Power Layer
Figure 9-39. TPS25751S PCB Layout - GND Layer
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
 www.ti.com
70 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 71

#### Raw extracted text

```text
Figure 9-40. TPS25751S PCB Layout - Bottom Layer
9.4.2.2.2.1 TPS25751S Component Placement
LDO_1V5 (pin 4), LDO_3V3 (pin 1), and VIN_3V3 (pin 32)
The decoupling capacitors for LDO_3V3, LDO_1V5, and VIN_3V3 (C15, C16, and C17 respectively) need to
be placed as close as possible to TPS25751S device for optimal performance. For this example to minimize
solution size, the decoupling capacitors are placed on the bottom layer with their ground pads directly
underneath the ground pad of TPS25751S. Use a maximum of one via per pin from TPS25751S to the
decoupling capacitors if placed on a different layer. Use a minimum of 10mil trace width to route these three
traces, preferably with 16mil trace width if possible.
CC1 (pin 24) and CC2 (pin 25)
CC1 (C11) and CC2 (C10) capacitors need to be placed as close as possible to their respective pins and on the
same layer as the TPS25751S device. When routing the CCx traces, DO NOT via to another layer in between
the CCx pins of the TPS25751S to the CCx capacitors. Check to make sure the CCx capacitors are not place
outside the CC trace creating an antenna, instead have the traces pass directly through the CCx capacitor pads
as shown in the example layout (refer to figure 10-21). Use a minimum of 10mil trace width to ensure Vconn
support (5V/0.6A).
9.4.2.2.2.2 TPS25751S PP5V
The 10uF decoupling capacitor (C8) need to be placed as close as possible to the PP5V pins of TPS25751S.
DO NOT use traces for PP5V. The PP5V power plane needs to be sized to support up to 3.6A (up to 3A for
sourcing, 600mA for Vconn). When connecting the PP5V pins (pins 28 and 29) to the 5V power plane, use a
minimum of 4 vias in parallel and close to the device to improve current sharing. Minimize the bottle necks cause
by other vias or traces, large bottle necks reduces the efficiency of the power plane. The bulk capacitors (C6,
C7, and C9) represent capacitances from the system 5V rail, these are placed further away from TPS25751S on
the same PP5V power plane. Refer to figure 10-21 and figure 10-22 for placement and trace reference.
9.4.2.2.2.3 TPS25751S PP_EXT
Place the PP_EXT decoupling capacitors (C12, C13, and C14) as close as possible to TPS25751S, these do
not need to be on the same layer as the device. The PP_EXT power plane needs to be sized to support up to
www.ti.com
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 71
Product Folder Links: TPS25751
```

### Page 72

#### Raw extracted text

```text
5A of current. When connecting the PP_EXT plane to a different layer, use a minimum of 6 vias in parallel per
layer change. It is highly recommended to have more than 6 vias if possible for layer change to improve current
sharing and efficiency.
VSYS (pin 19)
The VSYS pin (pin 19) can be connected with a trace (recommended 6mil trace width) to any of the vias on the
PPHV plane. It is recommended to connect to a via close to the source pin of the VSYS N-ch MOSFET(pins A2,
B2, D2, and E2 of the Q1 FET in the example schematic) to improve reverse current sensing protection. Refer to
section 9.3.3.2.2 for additional information on RCP.
9.4.2.2.2.4 TPS25751S VBUS
VBUS (pins 26 and 27)
Place the VBUS decoupling capacitor (C1) as close as possible to TPS25751S, the capacitor does not need to
be on the same layer as the device. The VBUS power plane need to be sized to support up to 5A of current
if 100W application is required. When connecting the VBUS pins (pins 26 and 27) plane to a different layer,
use a minimum of 3 vias per layer change. When connecting the VBUS power plane to a different layer, use a
minimum of 6 vias per layer change. Refer to figure 10-21 and figure 10-22 for capacitors and via placement.
At the Type-C port/connector, it is recommended to use minimum of 6 vias from the connector VBUS pins for
layer changes. Place the 10nF caps (C2, C3, C4, and C5) and the 22V TVS diode (U2) as close as possible to
the connector VBUS pins as shown in figure 10-22.
When routing the VBUS power plane from the Type-C connector to the TPS25751S VBUS pins, minimize bottle
necks caused by other vias and traces to improve current flow. The example layout shown in figure 10-24 uses
an internal layer to route the VBUS plane from the connector to TPS25751S.
9.4.2.2.2.5 TPS25751S I/O
I2C, ADCIN1/2, and GPIO pins
Fan these traces out from the TPS25751S, use vias to connect the net to a routing layer if needed. For these
nets, use 4mil to 10mil trace width.
I2Cc_SDA/SCL/IRQ (pins 8, 9, and 10) and I2Ct_SCL/SDA/IRQ (pins 15, 16, and 17)
Minimize trace width changes to avoid I2C communication issues.
ADCIN1 and ADCIN2 (pins 2 and 3)
Keep the ADCINx traces away from switching elements. If a resistor divider is used, place the divider close to
LDO_3V3 or LDO_1V5.
GPIO (pins 5, 6, 7, 18, 22, 23, 31, 30, and 13)
Separate GPIO traces running in parallel by a trace width. Keep the GPIOx traces away from switching
elements.
9.4.2.2.2.6 TPS25751S PPEXT Gate Driver
GATE_VSYS (pin 20)
The GATE_VSYS pin (pin 20) can be connected with a trace (recommended 6mil trace width) to the gate pins of
the N-ch MOSFET with source tied to PPHV. It is recommended to NOT via directly to the gate pin of the N-ch
MOSFET, instead use via(s) to connect the GATE_VSYS pin from the TPS25751S to the gate pin of the N-ch
MOSFET. Refer to figure 10-21 and figure 10-22 for examples on how to connect the traces.
GATE_VBUS (pin 21)
The GATE_VBUS pin (pin 21) can be connected with a trace (recommended 6mil trace width) to the gate pins of
the N-ch MOSFET with source tied to VBUS. It is recommended to NOT via directly to the gate pin of the N-ch
MOSFET, instead use via(s) to connect the GATE_VBUS pin from the TPS25751S to the gate pin of the N-ch
MOSFET. Refer to figure 10-21 and figure 10-22 for examples on how to connect the traces.
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
 www.ti.com
72 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 73

#### Raw extracted text

```text
9.4.2.2.2.7 TPS25751S GND
The GND pad is used to dissipate heat for the TPS25751S device. Connect the GND pins (11, 12, 14 and 31)
to the Ground pad (39) underneath the TPS25751S device. Connect the through hole vias from the ground pad
on the top layer to a copper pour on the bottom layer to help dissipate heat. Additional vias can be added to
improve thermal dissipation.
www.ti.com
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 73
Product Folder Links: TPS25751
```

### Page 74

#### Raw extracted text

```text
10 Device and Documentation Support
10.1 Device Support
10.1.1 Third-Party Products Disclaimer
TI'S PUBLICATION OF INFORMATION REGARDING THIRD-PARTY PRODUCTS OR SERVICES DOES NOT
CONSTITUTE AN ENDORSEMENT REGARDING THE SUITABILITY OF SUCH PRODUCTS OR SERVICES
OR A WARRANTY, REPRESENTATION OR ENDORSEMENT OF SUCH PRODUCTS OR SERVICES, EITHER
ALONE OR IN COMBINATION WITH ANY TI PRODUCT OR SERVICE.
10.1.2 Firmware Warranty Disclaimer
IN ORDER FOR THE DEVICE TO FUNCTION IN ACCORDANCE WITH THE RELEVANT SPECIFICATIONS,
YOU WILL NEED TO DOWNLOAD THE LATEST VERSION OF THE FIRMWARE FOR THE DEVICE (SEE
SECTION ON RECEIVING NOTIFICATION OF DOCUMENTATION AND FIRMWARE UPDATES). IF YOU DO
NOT DOWNLOAD AND INCORPORATE THE LATEST VERSION OF THE FIRMWARE INTO THE DEVICE,
THEN THE DEVICE IS PROVIDED AS IS AND TI MAKES NO WARRANTY OR REPRESENTATION
WHATSOEVER IN RESPECT OF SUCH DEVICE, AND DISCLAIMS ANY AND ALL WARRANTIES AND
REPRESENTATIONS WITH RESPECT TO SUCH DEVICE. FURTHER, IF YOU DO NOT DOWNLOAD
AND INCORPORATE THE LATEST VERSION OF THE FIRMWARE INTO THE DEVICE, TI WILL NOT BE
LIABLE FOR AND SPECIFICALLY DISCLAIMS ANY DAMAGES, INCLUDING DIRECT DAMAGES, HOWEVER
CAUSED, WHETHER ARISING UNDER CONTRACT, TORT, NEGLIGENCE, OR OTHER THEORY OF
LIABILITY RELATING TO THE DEVICE, EVEN IF TI IS ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.
10.2 Documentation Support
10.2.1 Related Documentation
* USB-PD Specifications
* USB Power Delivery Specification
10.3 Receiving Notification of Documentation Updates
To receive notification of documentation updates, navigate to the device product folder on ti.com. Click on
Notifications to register and receive a weekly digest of any product information that has changed. For change
details, review the revision history included in any revised document.
10.4 Support Resources
TI E2E (TM) support forums  are an engineer's go-to source for fast, verified answers and design help - straight
from the experts. Search existing answers or ask your own question to get the quick design help you need.
Linked content is provided "AS IS" by the respective contributors. They do not constitute TI specifications and do
not necessarily reflect TI's views; see TI's Terms of Use.
10.5 Trademarks
TI E2E(TM) is a trademark of Texas Instruments.
USB Type-C(R) is a registered trademark of USB Implementers Forum.
All trademarks are the property of their respective owners.
10.6 Electrostatic Discharge Caution
This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled
with appropriate precautions. Failure to observe proper handling and installation procedures can cause damage.
ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may
be more susceptible to damage because very small parametric changes could cause the device not to meet its published
specifications.
10.7 Glossary
TI Glossary This glossary lists and explains terms, acronyms, and definitions.
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
 www.ti.com
74 Submit Document Feedback Copyright  2024 Texas Instruments Incorporated
Product Folder Links: TPS25751
```

### Page 75

#### Raw extracted text

```text
11 Revision History
NOTE: Page numbers for previous revisions may differ from page numbers in the current version.
Changes from Revision * (October 2023) to Revision A (March 2024) Page
* Changed data sheet status from "Advance Information" to "Production Data".................................................. 1
12 Mechanical, Packaging, and Orderable Information
The following pages include mechanical, packaging, and orderable information. This information is the most
current data available for the designated devices. This data is subject to change without notice and revision of
this document. For browser-based versions of this data sheet, refer to the left-hand navigation.
www.ti.com
TPS25751
SLVSH93A - OCTOBER 2023 - REVISED MARCH 2024
Copyright  2024 Texas Instruments Incorporated Submit Document Feedback 75
Product Folder Links: TPS25751
```

### Page 76

#### Extracted tables

Table 1:

```text
Orderable part number | Status (1) | Material type (2) | Package | Pins | Package qty | Carrier | RoHS (3) | Lead finish/ Ball material (4) | MSL rating/ Peak reflow (5) | Op temp ( deg C) | Part marking (6)
TPS25751DREFR | Active | Production | WQFN (REF) | 38 | 3000 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | 25751D BG
TPS25751DREFR.A | Active | Production | WQFN (REF) | 38 | 3000 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | 25751D BG
TPS25751SRSMR | Active | Production | VQFN (RSM) | 32 | 3000 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | 25751S BG
TPS25751SRSMR.A | Active | Production | VQFN (RSM) | 32 | 3000 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | 25751S BG
TPS25751SRSMR.B | Active | Production | VQFN (RSM) | 32 | 3000 | LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | 40 to 125 | 25751S BG
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
TPS25751DREFR Active Production WQFN (REF) | 38 3000 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 25751D
BG
TPS25751DREFR.A Active Production WQFN (REF) | 38 3000 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 25751D
BG
TPS25751SRSMR Active Production VQFN (RSM) | 32 3000 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 25751S
BG
TPS25751SRSMR.A Active Production VQFN (RSM) | 32 3000 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 25751S
BG
TPS25751SRSMR.B Active Production VQFN (RSM) | 32 3000 | LARGE T&R Yes NIPDAU Level-2-260C-1 YEAR -40 to 125 25751S
BG

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

Important Information and Disclaimer:The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and
makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative
and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers
and other limited information may not be available for release.
Addendum-Page 1
```

### Page 77

#### Raw extracted text

```text
PACKAGE OPTION ADDENDUM
www.ti.com 6-Feb-2026

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.

Addendum-Page 2
```

### Page 78

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
TPS25751DREFR | WQFN | REF | 38 | 3000 | 330.0 | 12.4 | 4.3 | 6.3 | 1.1 | 8.0 | 12.0 | Q2
TPS25751SRSMR | VQFN | RSM | 32 | 3000 | 330.0 | 12.4 | 4.25 | 4.25 | 1.15 | 8.0 | 12.0 | Q2
```

#### Raw extracted text

```text
PACKAGE MATERIALS INFORMATION
www.ti.com 2-May-2024
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
TPS25751DREFR WQFN REF 38 3000 330.0 12.4 4.3 6.3 1.1 8.0 12.0 Q2
TPS25751SRSMR VQFN RSM 32 3000 330.0 12.4 4.25 4.25 1.15 8.0 12.0 Q2
Pack Materials-Page 1
```

### Page 79

#### Extracted tables

Table 1:

```text
| H
```

Table 2:

```text
Device | Package Type | Package Drawing | Pins | SPQ | Length (mm) | Width (mm) | Height (mm)
TPS25751DREFR | WQFN | REF | 38 | 3000 | 367.0 | 367.0 | 35.0
TPS25751SRSMR | VQFN | RSM | 32 | 3000 | 367.0 | 367.0 | 35.0
```

#### Raw extracted text

```text
PACKAGE MATERIALS INFORMATION

www.ti.com 2-May-2024
TAPE AND REEL BOX DIMENSIONS
Width (mm)
W LH

*All dimensions are nominal
Device Package Type Package Drawing Pins SPQ Length (mm) Width (mm) Height (mm)
TPS25751DREFR WQFN REF 38 3000 367.0 367.0 35.0
TPS25751SRSMR VQFN RSM 32 3000 367.0 367.0 35.0
Pack Materials-Page 2
```

### Page 80

#### Extracted tables

Table 1:

```text
| 0.08 | C
```

Table 2:

```text
| 0.07 | C | A | B
 | 0.05 |  |  |
```

#### Raw extracted text

```text
www.ti.com
PACKAGE OUTLINE
C
38X 0.45
0.25
0.8
0.7
(0.2)
TYP
0.05
0.00
30X 0.4
2
2X 4.8
1.63
1.43
2X 2.75
2.55
2.82
2.62
38X 0.25
0.15
2.2
4X 0.45
4X
(0.2)
0.45
0.25
0.25
0.15
0.965 1.56
A 6.1
5.9
B
4.1
3.9
WQFN - 0.8 mm max heightREF0038A
PLASTIC QUAD FLATPACK - NO LEAD
4226763/C   11/2021
PIN 1 INDEX AREA
0.08 C
SEATING PLANE
1
6
20
25
7 19
38 26
X 0.3)(45
PIN 1 ID
0.07 C A B
0.05
EXPOSED
THERMAL PAD
39SYMM
PKG
40
SEE DETAIL A
NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
    per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. The package thermal pads must be soldered to the printed circuit board for optimal thermal and mechanical performance.
DETAIL A
TYPICAL
SCALE  2.800
```

### Page 81

#### Raw extracted text

```text
www.ti.com
EXAMPLE BOARD LAYOUT
30X (0.4)
30X (0.55)
38X (0.2)
(1.56)
(1.53)
(2.72)
2X
(1.075)
4X
(0.45)
4X (0.2)
(2.925) (3.2)
2X (0.55)
(R0.05) TYP
0.05 MIN
ALL AROUND
0.05 MAX
ALL AROUND
( 0.2) TYP
VIA
(3.85)2X
(2.65)
(2.075)
(0.145)(0.965)
WQFN - 0.8 mm max heightREF0038A
PLASTIC QUAD FLATPACK - NO LEAD
4226763/C   11/2021
PKG
1
6
7 19
20
25
2638
SYMM
LAND PATTERN EXAMPLE
EXPOSED METAL SHOWN
SCALE:18X
39 40
SOLDER MASK
OPENING
METAL UNDER
SOLDER MASK
NOTES: (continued)

4. This package is designed to be soldered to thermal pads on the board. For more information, see Texas Instruments literature
    number SLUA271 (www.ti.com/lit/slua271).
5. Vias are optional depending on application, refer to device data sheet. If any vias are implemented, refer to their locations shown
    on this view. It is recommended that vias under paste be filled, plugged or tented.
SOLDER MASK
OPENING
METAL UNDER
SOLDER MASK
SOLDER MASK
DEFINED
PADS 20-25 & 32-35
EXPOSED METAL
METAL
SOLDER MASK
OPENING
SOLDER MASK DETAILS
NOT TO SCALE
NON SOLDER MASK
DEFINED
EXPOSED METAL
```

### Page 82

#### Extracted tables

Table 1:

```text
39 |
```

#### Raw extracted text

```text
www.ti.com
EXAMPLE STENCIL DESIGN
2X (0.27)
30X (0.55)
38X
(0.2)
30X
(0.4)
4X
(0.45)
4X (0.2)
(2.925) (3.2)
2X (0.55)
(3.85)
4X (1.19)
6X
(0.69)
(R0.05) TYP
2X (1.66) 2X (1.56)
6X
(1.17)
2X (1.4)
WQFN - 0.8 mm max heightREF0038A
PLASTIC QUAD FLATPACK - NO LEAD
4226763/C   11/2021
NOTES: (continued)

6. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
   design recommendations.

PKG
METAL
TYP
SOLDER PASTE EXAMPLE
BASED ON 0.1 mm THICK STENCIL

EXPOSED PADS 39
78% PRINTED SOLDER COVERAGE BY AREA UNDER PACKAGE

EXPOSED PADS 40
80% PRINTED SOLDER COVERAGE BY AREA UNDER PACKAGE

SCALE:20X
SYMM
1
6
7 19
20
25
2638
39 40
METAL UNDER
SOLDER MASK
```

### Page 83

#### Raw extracted text

```text
GENERIC PACKAGE VIEW
RSM 32 VQFN - 1 mm max height
4 x 4, 0.4 mm pitch PLASTIC QUAD FLATPACK - NO LEAD
This image is a representation of the package family, actual package may vary.
Refer to the product data sheet for package details.
4224982/A
www.ti.com
```

### Page 84

#### Extracted tables

Table 1:

```text
| 0.08 | C
```

Table 2:

```text
| 0.1 | C | A | B
 | 0.05 |  |  |
```

#### Raw extracted text

```text
www.ti.com
PACKAGE OUTLINE
C
32X 0.25
0.15
2.8 0.05
32X 0.45
0.25
1 MAX
(0.2) TYP
0.05
0.00
28X 0.4
2X
2.8
2X 2.8
A 4.1
3.9
B
4.1
3.9
0.25
0.15
0.45
0.25
4X (0.45)
(0.1)
VQFN - 1 mm max heightRSM0032B
PLASTIC QUAD FLATPACK - NO LEAD
4219108/B   08/2019
PIN 1 INDEX AREA
0.08 C
SEATING PLANE
1
8 17
24
9 16
32 25
(OPTIONAL)
PIN 1 ID
0.1 C A B
0.05
EXPOSED
THERMAL PAD
DETAIL
SEE TERMINAL
SYMM
SYMM
NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
    per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. The package thermal pad must be soldered to the printed circuit board for thermal and mechanical performance.
33
SEE SIDE WALL
DETAIL
SIDE WALL DETAIL
OPTIONAL METAL THICKNESS
SCALE  3.000
DETAIL
OPTIONAL TERMINAL
TYPICAL
```

### Page 85

#### Raw extracted text

```text
www.ti.com
EXAMPLE BOARD LAYOUT
0.05 MIN
ALL AROUND
0.05 MAX
ALL AROUND
32X (0.2)
32X (0.55)
( 0.2) TYP
VIA
28X (0.4)
(3.85)
(3.85)
( 2.8)
(R0.05)
TYP
(1.15)
(1.15)
VQFN - 1 mm max heightRSM0032B
PLASTIC QUAD FLATPACK - NO LEAD
4219108/B   08/2019
SYMM
1
8
9 16
17
24
2532
SYMM
LAND PATTERN EXAMPLE
EXPOSED METAL SHOWN
SCALE:20X
33
NOTES: (continued)

4. This package is designed to be soldered to a thermal pad on the board. For more information, see Texas Instruments literature
    number SLUA271 (www.ti.com/lit/slua271).
5. Vias are optional depending on application, refer to device data sheet. If any vias are implemented, refer to their locations shown
    on this view. It is recommended that vias under paste be filled, plugged or tented.
SOLDER MASK
OPENING
METAL UNDER
SOLDER MASK
SOLDER MASK
DEFINED
EXPOSED METAL
METAL
SOLDER MASK
OPENING
SOLDER MASK DETAILS
NON SOLDER MASK
DEFINED
(PREFERRED)
EXPOSED METAL
```

### Page 86

#### Raw extracted text

```text
www.ti.com
EXAMPLE STENCIL DESIGN
32X (0.55)
32X (0.2)
28X (0.4)
(3.85)
(3.85)
4X ( 1.23)
(R0.05) TYP
(0.715)
(0.715)
VQFN - 1 mm max heightRSM0032B
PLASTIC QUAD FLATPACK - NO LEAD
4219108/B   08/2019
NOTES: (continued)

6. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
    design recommendations.
33
SYMM
METAL
TYP SOLDER PASTE EXAMPLE
BASED ON 0.1 mm THICK STENCIL

EXPOSED PAD 33:
77% PRINTED SOLDER COVERAGE BY AREA UNDER PACKAGE
SCALE:20X
SYMM
1
8
9 16
17
24
2532
```

### Page 87

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
