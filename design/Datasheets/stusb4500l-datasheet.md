# Datasheet - STUSB4500L - Standalone USB Type-C(TM) sink port controller

## Source

- Source PDF: [stusb4500l-datasheet.pdf](stusb4500l-datasheet.pdf)
- Generated Markdown: `stusb4500l-datasheet.md`
- Page count: 31
- Conversion method: automated local extraction with pypdf and pdfplumber

## Extracted title and part identity

- Datasheet - STUSB4500L - Standalone USB Type-C(TM) sink port controller
- stusb4500l datasheet
- STUSB4500L
- DS13102
- CC1DB
- CC2DB
- STUSB4500LQTR
- STUSB4500LBJR

## Extraction summary

- Pages with substantial text extraction: 31/31
- Pages with extracted tables: 31/31
- Total extracted character count: 61338
- Extraction quality flag: usable

## PDF metadata

| Field | Value |
| --- | --- |
| Title | Datasheet - STUSB4500L - Standalone USB Type-C(TM) sink port controller |
| Author | STMICROELECTRONICS |
| Subject |  |
| Creator | C2 v4.2.0220 build 670 - c2_rendition_config : Techlit_Active |
| Producer | Antenna House PDF Output Library 7.0.1600; modified using iText 2.1.7 by 1T3XT |

## Design-relevant extracted content

This section surfaces design-relevant snippets first. Full page-by-page raw extraction follows later for local search.

### Part number and ordering information

- Applications / Product summary / STUSB4500LQTR * Printers, camcorders, cameras / Order code / * IoT, drones, accessories and battery powered devices / STUSB4500LBJR / * Computer accessories (keyboards, mouse)
- Package WLCSP-25 * Any 5 V Type-C sink device / (2.6x2.6x0.5) / Description / Marking 4500L / The STUSB4500L is a USB Type-C controller that addresses 5 V-only sink devices / up to 3 A (15 W max.). / This device supports dead battery mode and is suited for sink devices powered
- BUS / by closing the input switch. The available current advertised by the SOURCE is / reported to the application in order to align the sinking current. Port status can be / optionally monitored by the software through I2C interface. / Thanks to its 20 V technology, it implements high voltage features to protect the CC / pins against short-circuits to V . / BUS
- Product status link / STUSB4500L / Product summary | / Order code | STUSB4500LQTR / | STUSB4500LBJR / Description | Standalone USB Type-C controller (auto-run mode) / Package | QFN-24 EP (4x4)
- Description | Standalone USB Type-C controller (auto-run mode) / Package | QFN-24 EP (4x4) / | WLCSP-25 (2.6x2.6x0.5) / Marking | 4500L / | DS13102 - Rev 6 - February 2022 www.st.com For further information contact your local STMicroelectronics sales office. | / 1 Functional description / The STUSB4500L is a USB Type-C(TM) IC controller addressing 5 V sink applications. It supports dead battery
- When possible, please prefer VDD supply only, and connect it to VBUS in order to minimize application power / consumption. In this case, VSYS is not used and must be connected to GND. / 6.1.2 Connection to MCU or application processor / The STUSB4500L connection to an MCU or an application processor is optional. However, an I2C interface with / an interrupt allows a simple connection to most of MCU and SOC of the market. / When a connection through the I2C interface is implemented, it provides an extensive functionality during the / system operation. For instance, it may be used to:
- SCL / MCU / Alert / OPTIONAL / PE_DNG0 / STUSB4500L / Typical application
- PE_DNG0 / STUSB4500L / Typical application / (Optional) / U_stusb4500L / VDD24 / 3Not_Used
- ALERT19 / STUSB4500L / GND / Note: The STUSB4500L can be connected to an application processor using I2C interface. This connection is optional. / DS13102 - Rev 6 page 16/31 / 23 21 | VREG_2V7 VDD VREG_1V2 VBUS_VS_DISCH VSYS RP_3A VBUS_EN_SNK Not_Used A_B_SIDE GND DISCH CC1DB CC1 GPIO CC2 RP_1A5 ADDR1 CC2DB RESET ADDR0 SCL PE_DNG ATTACH SDA ALERT / 3
- 20 V open drain outputs (VBUS_EN_SNK, DISCH, RP_3A) | | | | | | / VOL | Low level output voltage | Ioh = 3 mA | | | 0.4 | V / | DS13102 - Rev 6 page 19/31 | / 8 Package information / In order to meet environmental requirements, ST offers these devices in different grades of ECOPACK packages, / depending on their level of environmental compliance. ECOPACK specifications, grade definitions and product / status are available at: www.st.com. ECOPACK is an ST trademark.
- In order to meet environmental requirements, ST offers these devices in different grades of ECOPACK packages, / depending on their level of environmental compliance. ECOPACK specifications, grade definitions and product / status are available at: www.st.com. ECOPACK is an ST trademark. / 8.1 QFN-24 EP (4x4) package information / Figure 10. QFN-24 EP (4x4) package information / P LAN E / S E ATIN G
- depending on their level of environmental compliance. ECOPACK specifications, grade definitions and product / status are available at: www.st.com. ECOPACK is an ST trademark. / 8.1 QFN-24 EP (4x4) package information / Figure 10. QFN-24 EP (4x4) package information / P LAN E / S E ATIN G / 0.08 C
- A1 / A / STUSB4500L / Package information / DS13102 - Rev 6 page 20/31 / | | E / | 0.08 | C
- L 0.30 0.40 0.50 0.012 0.016 0.020 / Figure 11. QFN-24 EP (4x4) recommended footprint / STUSB4500L / QFN-24 EP (4x4) package information / DS13102 - Rev 6 page 21/31 / Ref. | mm | | | Inches | | / | Min. | Typ | Max. | Min. | Typ. | Max.
- K | 0.15 | | | 0.006 | | / L | 0.30 | 0.40 | 0.50 | 0.012 | 0.016 | 0.020 / | DS13102 - Rev 6 page 21/31 | / 8.2 WLCSP (2.6x2.6x0.5) 25 bumps package information / Figure 12. WLCSP (2.6x2.6x0.5) package outline / STUSB4500L / WLCSP (2.6x2.6x0.5) 25 bumps package information
- 8.2 WLCSP (2.6x2.6x0.5) 25 bumps package information / Figure 12. WLCSP (2.6x2.6x0.5) package outline / STUSB4500L / WLCSP (2.6x2.6x0.5) 25 bumps package information / DS13102 - Rev 6 page 22/31 / | DS13102 - Rev 6 page 22/31 | / Table 18. WLCSP (2.6x2.6x0.5) package mechanical data
- ccc 0.05 / ddd 0.015 / Note: WLCSP stands for wafer level chip scale package. The typical ball diameter before mounting is 0.25 mm. The / terminal A1 corner must be identified on the top surface by using a laser marking dot. / Figure 13. WLCSP (2.6x2.6x0.5) recommended footprint / STUSB4500L / WLCSP (2.6x2.6x0.5) 25 bumps package information
- terminal A1 corner must be identified on the top surface by using a laser marking dot. / Figure 13. WLCSP (2.6x2.6x0.5) recommended footprint / STUSB4500L / WLCSP (2.6x2.6x0.5) 25 bumps package information / DS13102 - Rev 6 page 23/31 / Symbol | mm | | / | Min. | Typ. | Max.

### Pin, pad, and terminal designations

- BUS / * Integrated V voltage monitoring / BUS / * Short-to-VBUS protections on CC pins / * High voltage capability on V pins / BUS / * Source power budget reporting: (default / 1.5 A / 3 A) current at 5 V
- * Integrated V voltage monitoring / BUS / * Short-to-VBUS protections on CC pins / * High voltage capability on V pins / BUS / * Source power budget reporting: (default / 1.5 A / 3 A) current at 5 V / * V powered:
- This device supports dead battery mode and is suited for sink devices powered / from dead battery state. It is able to operate without any external software support / for quick application power-on and immediate charging process start. At type-C / connection, the STUSB4500L seeks CC pin for SOURCE termination and monitors / V voltage in order to protect the application from an incorrect SOURCE operation. / BUS / When V is within the appropriate range, the STUSB4500L powers the application
- reported to the application in order to align the sinking current. Port status can be / optionally monitored by the software through I2C interface. / Thanks to its 20 V technology, it implements high voltage features to protect the CC / pins against short-circuits to V . / BUS / DS13102 - Rev 6 - February 2022 www.st.com / For further information contact your local STMicroelectronics sales office.
- | WLCSP-25 (2.6x2.6x0.5) / Marking | 4500L / | DS13102 - Rev 6 - February 2022 www.st.com For further information contact your local STMicroelectronics sales office. | / 1 Functional description / The STUSB4500L is a USB Type-C(TM) IC controller addressing 5 V sink applications. It supports dead battery / mode to allow a system to be powered from a VBUS power source directly. / The STUSB4500L major role is to:
- The STUSB4500L is a USB Type-C(TM) IC controller addressing 5 V sink applications. It supports dead battery / mode to allow a system to be powered from a VBUS power source directly. / The STUSB4500L major role is to: / 1. Detect the connection between two USB Type-C ports (attach detection) / 2. Establish a valid source-to-sink connection / 3. Identify the attached device: source or debug accessory / 4. Resolve cable orientation and twist connections to establish USB 3 data routing (MUX control) if any
- mode to allow a system to be powered from a VBUS power source directly. / The STUSB4500L major role is to: / 1. Detect the connection between two USB Type-C ports (attach detection) / 2. Establish a valid source-to-sink connection / 3. Identify the attached device: source or debug accessory / 4. Resolve cable orientation and twist connections to establish USB 3 data routing (MUX control) if any / 5. Configure the incoming V BUS power path
- 1. Detect the connection between two USB Type-C ports (attach detection) / 2. Establish a valid source-to-sink connection / 3. Identify the attached device: source or debug accessory / 4. Resolve cable orientation and twist connections to establish USB 3 data routing (MUX control) if any / 5. Configure the incoming V BUS power path / 6. Monitor the V BUS power path / 7. Report the available power advertised by the source
- * Debug accessory mode detection / * Customization of the device configuration through NVM to support specific applications / 1.1 Block overview / Figure 1. Functional block diagram / GND / SCL / SDA
- controller / A_B_SIDE / STUSB4500L / Functional description / DS13102 - Rev 6 page 2/31 / | DS13102 - Rev 6 page 2/31 | / 2 Inputs/outputs
- DS13102 - Rev 6 page 2/31 / | DS13102 - Rev 6 page 2/31 | / 2 Inputs/outputs / 2.1 Pinout / Figure 2. QFN-24 pin connections (top view) / 7 8 9 10 11 12 / 1 24 23 22 21 20 19
- | DS13102 - Rev 6 page 2/31 | / 2 Inputs/outputs / 2.1 Pinout / Figure 2. QFN-24 pin connections (top view) / 7 8 9 10 11 12 / 1 24 23 22 21 20 19 / 18
- 4 / 5 / 6 / Figure 3. WLCSP-25 pin connections (top view) / VBUS_VS / _ DISCH / RP_3A
- Inputs/outputs / DS13102 - Rev 6 page 3/31 / | DS13102 - Rev 6 page 3/31 | / Table 1. Pin function list / QFN CSP Name Type Description Typical connection / 1 B4 CC1DB HV AIO Dead battery enable on CC1 pin To CC1 pin if used or ground / 2 B5 CC1 HV AIO Type-C configuration channel 1 To Type-C receptacle A5
- DS13102 - Rev 6 page 3/31 / | DS13102 - Rev 6 page 3/31 | / Table 1. Pin function list / QFN CSP Name Type Description Typical connection / 1 B4 CC1DB HV AIO Dead battery enable on CC1 pin To CC1 pin if used or ground / 2 B5 CC1 HV AIO Type-C configuration channel 1 To Type-C receptacle A5 / 3 B3, C3 NU - - To ground
- | DS13102 - Rev 6 page 3/31 | / Table 1. Pin function list / QFN CSP Name Type Description Typical connection / 1 B4 CC1DB HV AIO Dead battery enable on CC1 pin To CC1 pin if used or ground / 2 B5 CC1 HV AIO Type-C configuration channel 1 To Type-C receptacle A5 / 3 B3, C3 NU - - To ground / 4 C5 CC2 HV AIO Type-C configuration channel 2 To Type-C receptacle B5
- 2 B5 CC1 HV AIO Type-C configuration channel 1 To Type-C receptacle A5 / 3 B3, C3 NU - - To ground / 4 C5 CC2 HV AIO Type-C configuration channel 2 To Type-C receptacle B5 / 5 C4 CC2DB HV AIO Dead battery enable on CC2 pin To CC2 pin if used or ground / 6 D4 RESET DI Reset input, active high From system / 7 D5 SCL DI I2C clock input To I2C master, ext. pull-up or / floating (if not used
- 6 D4 RESET DI Reset input, active high From system / 7 D5 SCL DI I2C clock input To I2C master, ext. pull-up or / floating (if not used / 8 E5 SDA DI/OD I2C data input/output, active low open drain To I2C master, ext. pull-up or / floating (if not used / 9 E4 DISCH HV AI/OD / Internal discharge path or external

### Specifications, ratings, and operating conditions

- * Dead battery mode support / * Integrated V switch gate drivers (PMOS) / BUS / * Integrated V voltage monitoring / BUS / * Short-to-VBUS protections on CC pins / * High voltage capability on V pins
- * Integrated V voltage monitoring / BUS / * Short-to-VBUS protections on CC pins / * High voltage capability on V pins / BUS / * Source power budget reporting: (default / 1.5 A / 3 A) current at 5 V / * V powered:
- * Short-to-VBUS protections on CC pins / * High voltage capability on V pins / BUS / * Source power budget reporting: (default / 1.5 A / 3 A) current at 5 V / * V powered: / BUS / Zero consumption on local battery or application
- from dead battery state. It is able to operate without any external software support / for quick application power-on and immediate charging process start. At type-C / connection, the STUSB4500L seeks CC pin for SOURCE termination and monitors / V voltage in order to protect the application from an incorrect SOURCE operation. / BUS / When V is within the appropriate range, the STUSB4500L powers the application / BUS
- BUS / When V is within the appropriate range, the STUSB4500L powers the application / BUS / by closing the input switch. The available current advertised by the SOURCE is / reported to the application in order to align the sinking current. Port status can be / optionally monitored by the software through I2C interface. / Thanks to its 20 V technology, it implements high voltage features to protect the CC
- When V is within the appropriate range, the STUSB4500L powers the application / BUS / by closing the input switch. The available current advertised by the SOURCE is / reported to the application in order to align the sinking current. Port status can be / optionally monitored by the software through I2C interface. / Thanks to its 20 V technology, it implements high voltage features to protect the CC / pins against short-circuits to V .
- by closing the input switch. The available current advertised by the SOURCE is / reported to the application in order to align the sinking current. Port status can be / optionally monitored by the software through I2C interface. / Thanks to its 20 V technology, it implements high voltage features to protect the CC / pins against short-circuits to V . / BUS / DS13102 - Rev 6 - February 2022 www.st.com
- 5. Configure the incoming V BUS power path / 6. Monitor the V BUS power path / 7. Report the available power advertised by the source / 8. Handle the high voltage protections / The STUSB4500L also provides: / * Dead battery mode / * Internal and/or external V BUS discharge paths
- VREG_1V2 / POR / VBUS_VS_DISCH / voltage / monitoring / Discharge / path
- system, ext. pull-up / 17 C2 A_B_SIDE OD Cable orientation, active low open drain USB super speed MUX select, / ext. pull-up / 18 A1 VBUS_VS_DISCH HV AI VBUS voltage monitoring and discharge / path / From VBUS, receptacle side / 19 B2 ALERT OD I2C interrupt, active low open drain To I2C master, ext. pull-up
- 15 | D1 | GPIO | OD | General purpose output, active low open drain | To system, ext. pull-up / 16 | C1 | VBUS_EN_SNK | HV OD | VBUS sink power path enable, active low open drain | To power switch or to power system, ext. pull-up / 17 | C2 | A_B_SIDE | OD | Cable orientation, active low open drain | USB super speed MUX select, ext. pull-up / 18 | A1 | VBUS_VS_DISCH | HV AI | VBUS voltage monitoring and discharge path | From VBUS, receptacle side / 19 | B2 | ALERT | OD | I2C interrupt, active low open drain | To I2C master, ext. pull-up / 20 | A2 | RP_3A | HV OD | 3 A source flag, active low open drain | To power switch or to power system, ext. pull-up / 21 | A3 | VREG_1V2 | PWR | 1.2 V internal regulator output | 1 uF typ. decoupling capacitor
- OD Open drain output / PD Pull-down / PU Pull-up / HV High voltage / PWR Power / GND Ground / 2.2 Pin description
- OD | Open drain output / PD | Pull-down / PU | Pull-up / HV | High voltage / PWR | Power / GND | Ground / Name | Description
- BUS / side. / When used as input, the discharge is internal and a serial resistor must connected to the pin to limit the discharge / current through the pin. Maximum discharge current is 500 mA. / The pin can be also used as an open drain output to control an external V discharge path when higher / BUS / discharge current is required by the application, for instance.
- current through the pin. Maximum discharge current is 500 mA. / The pin can be also used as an open drain output to control an external V discharge path when higher / BUS / discharge current is required by the application, for instance. / The pin is activated at the same time as the internal discharge path on VBUS_VS_DISCH pin. The discharge is / activated automatically during cable disconnection and error recovery state. The discharge time is programmable / by NVM (see Section 5 Start-up configuration).
- This pin is asserted when a valid source-to-sink connection is established. It is also asserted when a connection / to a debug accessory device is detected. / 2.2.8 RP_3A/RP_1A5 / These pins report by default the status of the USB source current capabilities. / Table 4. Source current capability / Pin name Value Description / Hi-Z No source attached
- to a debug accessory device is detected. / 2.2.8 RP_3A/RP_1A5 / These pins report by default the status of the USB source current capabilities. / Table 4. Source current capability / Pin name Value Description / Hi-Z No source attached / VBUS_EN_SNK
- Hi-Z No source attached / VBUS_EN_SNK / 0 Source attached / Hi-Z No source attached or source supplies default USB Type-C current at 5 V / RP_3A / 0 Source supplies 3.0 A USB Type-C current at 5 V / Hi-Z No source attached or source supplies default USB Type-C current at 5 V.

### Dimensions, package, and mechanical information

- Description Type-C controller * Toys, gaming, POS, scanner, LED lighting / (auto-run mode) * Healthcare, e-cigarettes, handheld devices / QFN-24 EP (4x4) * 5 V DC barrel, USB STD-B and micro-B replacement / Package WLCSP-25 * Any 5 V Type-C sink device / (2.6x2.6x0.5) / Description / Marking 4500L
- Order code | STUSB4500LQTR / | STUSB4500LBJR / Description | Standalone USB Type-C controller (auto-run mode) / Package | QFN-24 EP (4x4) / | WLCSP-25 (2.6x2.6x0.5) / Marking | 4500L / | DS13102 - Rev 6 - February 2022 www.st.com For further information contact your local STMicroelectronics sales office. |
- 20 V open drain outputs (VBUS_EN_SNK, DISCH, RP_3A) | | | | | | / VOL | Low level output voltage | Ioh = 3 mA | | | 0.4 | V / | DS13102 - Rev 6 page 19/31 | / 8 Package information / In order to meet environmental requirements, ST offers these devices in different grades of ECOPACK packages, / depending on their level of environmental compliance. ECOPACK specifications, grade definitions and product / status are available at: www.st.com. ECOPACK is an ST trademark.
- VOL | Low level output voltage | Ioh = 3 mA | | | 0.4 | V / | DS13102 - Rev 6 page 19/31 | / 8 Package information / In order to meet environmental requirements, ST offers these devices in different grades of ECOPACK packages, / depending on their level of environmental compliance. ECOPACK specifications, grade definitions and product / status are available at: www.st.com. ECOPACK is an ST trademark. / 8.1 QFN-24 EP (4x4) package information
- In order to meet environmental requirements, ST offers these devices in different grades of ECOPACK packages, / depending on their level of environmental compliance. ECOPACK specifications, grade definitions and product / status are available at: www.st.com. ECOPACK is an ST trademark. / 8.1 QFN-24 EP (4x4) package information / Figure 10. QFN-24 EP (4x4) package information / P LAN E / S E ATIN G
- depending on their level of environmental compliance. ECOPACK specifications, grade definitions and product / status are available at: www.st.com. ECOPACK is an ST trademark. / 8.1 QFN-24 EP (4x4) package information / Figure 10. QFN-24 EP (4x4) package information / P LAN E / S E ATIN G / 0.08 C
- A1 / A / STUSB4500L / Package information / DS13102 - Rev 6 page 20/31 / | | E / | 0.08 | C
- | | | 2E / | D2 | | / | DS13102 - Rev 6 page 20/31 | / Table 17. QFN-24 EP (4x4) package mechanical data / Ref. / mm Inches / Min. Typ Max. Min. Typ. Max.
- e 0.45 0.50 0.55 0.018 0.020 0.022 / K 0.15 - - 0.006 / L 0.30 0.40 0.50 0.012 0.016 0.020 / Figure 11. QFN-24 EP (4x4) recommended footprint / STUSB4500L / QFN-24 EP (4x4) package information / DS13102 - Rev 6 page 21/31
- L 0.30 0.40 0.50 0.012 0.016 0.020 / Figure 11. QFN-24 EP (4x4) recommended footprint / STUSB4500L / QFN-24 EP (4x4) package information / DS13102 - Rev 6 page 21/31 / Ref. | mm | | | Inches | | / | Min. | Typ | Max. | Min. | Typ. | Max.
- K | 0.15 | | | 0.006 | | / L | 0.30 | 0.40 | 0.50 | 0.012 | 0.016 | 0.020 / | DS13102 - Rev 6 page 21/31 | / 8.2 WLCSP (2.6x2.6x0.5) 25 bumps package information / Figure 12. WLCSP (2.6x2.6x0.5) package outline / STUSB4500L / WLCSP (2.6x2.6x0.5) 25 bumps package information
- L | 0.30 | 0.40 | 0.50 | 0.012 | 0.016 | 0.020 / | DS13102 - Rev 6 page 21/31 | / 8.2 WLCSP (2.6x2.6x0.5) 25 bumps package information / Figure 12. WLCSP (2.6x2.6x0.5) package outline / STUSB4500L / WLCSP (2.6x2.6x0.5) 25 bumps package information / DS13102 - Rev 6 page 22/31
- 8.2 WLCSP (2.6x2.6x0.5) 25 bumps package information / Figure 12. WLCSP (2.6x2.6x0.5) package outline / STUSB4500L / WLCSP (2.6x2.6x0.5) 25 bumps package information / DS13102 - Rev 6 page 22/31 / | DS13102 - Rev 6 page 22/31 | / Table 18. WLCSP (2.6x2.6x0.5) package mechanical data
- WLCSP (2.6x2.6x0.5) 25 bumps package information / DS13102 - Rev 6 page 22/31 / | DS13102 - Rev 6 page 22/31 | / Table 18. WLCSP (2.6x2.6x0.5) package mechanical data / Symbol / mm / Min. Typ. Max.
- bbb 0.06 / ccc 0.05 / ddd 0.015 / Note: WLCSP stands for wafer level chip scale package. The typical ball diameter before mounting is 0.25 mm. The / terminal A1 corner must be identified on the top surface by using a laser marking dot. / Figure 13. WLCSP (2.6x2.6x0.5) recommended footprint / STUSB4500L
- ddd 0.015 / Note: WLCSP stands for wafer level chip scale package. The typical ball diameter before mounting is 0.25 mm. The / terminal A1 corner must be identified on the top surface by using a laser marking dot. / Figure 13. WLCSP (2.6x2.6x0.5) recommended footprint / STUSB4500L / WLCSP (2.6x2.6x0.5) 25 bumps package information / DS13102 - Rev 6 page 23/31
- terminal A1 corner must be identified on the top surface by using a laser marking dot. / Figure 13. WLCSP (2.6x2.6x0.5) recommended footprint / STUSB4500L / WLCSP (2.6x2.6x0.5) 25 bumps package information / DS13102 - Rev 6 page 23/31 / Symbol | mm | | / | Min. | Typ. | Max.
- Table 21. Document revision history / Date Revision Changes / 10-Oct-2019 1 Initial release. / 22-Oct-2019 2 Added Figure 13. WLCSP (2.6x2.6x0.5) recommended footprint. / 29-Apr-2020 3 Added Section 3.5 High voltage protections. / 08-Jun-2020 4 Updated Figure 13. WLCSP (2.6x2.6x0.5) recommended footprint. / 15-Jun-2021 5 Updated Section Features and Section Description.

### Formulas, equations, and configuration calculations

- from dead battery state. It is able to operate without any external software support / for quick application power-on and immediate charging process start. At type-C / connection, the STUSB4500L seeks CC pin for SOURCE termination and monitors / V voltage in order to protect the application from an incorrect SOURCE operation. / BUS / When V is within the appropriate range, the STUSB4500L powers the application / BUS
- reported to the application in order to align the sinking current. Port status can be / optionally monitored by the software through I2C interface. / Thanks to its 20 V technology, it implements high voltage features to protect the CC / pins against short-circuits to V . / BUS / DS13102 - Rev 6 - February 2022 www.st.com / For further information contact your local STMicroelectronics sales office.
- * Dead battery mode / * Internal and/or external V BUS discharge paths / * Debug accessory mode detection / * Customization of the device configuration through NVM to support specific applications / 1.1 Block overview / Figure 1. Functional block diagram / GND
- Table 1. Pin function list / QFN CSP Name Type Description Typical connection / 1 B4 CC1DB HV AIO Dead battery enable on CC1 pin To CC1 pin if used or ground / 2 B5 CC1 HV AIO Type-C configuration channel 1 To Type-C receptacle A5 / 3 B3, C3 NU - - To ground / 4 C5 CC2 HV AIO Type-C configuration channel 2 To Type-C receptacle B5 / 5 C4 CC2DB HV AIO Dead battery enable on CC2 pin To CC2 pin if used or ground
- 1 B4 CC1DB HV AIO Dead battery enable on CC1 pin To CC1 pin if used or ground / 2 B5 CC1 HV AIO Type-C configuration channel 1 To Type-C receptacle A5 / 3 B3, C3 NU - - To ground / 4 C5 CC2 HV AIO Type-C configuration channel 2 To Type-C receptacle B5 / 5 C4 CC2DB HV AIO Dead battery enable on CC2 pin To CC2 pin if used or ground / 6 D4 RESET DI Reset input, active high From system / 7 D5 SCL DI I2C clock input To I2C master, ext. pull-up or
- DS13102 - Rev 6 page 4/31 / QFN | CSP | Name | Type | Description | Typical connection / 1 | B4 | CC1DB | HV AIO | Dead battery enable on CC1 pin | To CC1 pin if used or ground / 2 | B5 | CC1 | HV AIO | Type-C configuration channel 1 | To Type-C receptacle A5 / 3 | B3, C3 | NU | | | To ground / 4 | C5 | CC2 | HV AIO | Type-C configuration channel 2 | To Type-C receptacle B5 / 5 | C4 | CC2DB | HV AIO | Dead battery enable on CC2 pin | To CC2 pin if used or ground
- 1 | B4 | CC1DB | HV AIO | Dead battery enable on CC1 pin | To CC1 pin if used or ground / 2 | B5 | CC1 | HV AIO | Type-C configuration channel 1 | To Type-C receptacle A5 / 3 | B3, C3 | NU | | | To ground / 4 | C5 | CC2 | HV AIO | Type-C configuration channel 2 | To Type-C receptacle B5 / 5 | C4 | CC2DB | HV AIO | Dead battery enable on CC2 pin | To CC2 pin if used or ground / 6 | D4 | RESET | DI | Reset input, active high | From system / 7 | D5 | SCL | DI | I2C clock input | To I2C master, ext. pull-up or floating (if not used
- GND Ground / 2.2 Pin description / 2.2.1 CC1 / CC2 / CC1 and CC2 are the configuration channel pins used for connection and attachment detection, plug orientation / determination. CC1 and CC2 are HiZ during reset. / 2.2.2 CC1DB / CC2DB / CC1DB and CC2DB are enabled by dead battery mode by connecting CC1DB and CC2DB respectively to CC1
- discharge current is required by the application, for instance. / The pin is activated at the same time as the internal discharge path on VBUS_VS_DISCH pin. The discharge is / activated automatically during cable disconnection and error recovery state. The discharge time is programmable / by NVM (see Section 5 Start-up configuration). / 2.2.6 GND / Ground. / 2.2.7 ATTACH
- | DS13102 - Rev 6 page 6/31 | / 2.2.9 GPIO / This pin is an active low open drain output that can be configured by NVM as per table below (see / Section 5 Start-up configuration). / Table 5. GPIO pin configuration / NVM parameter / GPIO_CFG[1:0] Pin name Pin function Value Description
- 2.2.9 GPIO / This pin is an active low open drain output that can be configured by NVM as per table below (see / Section 5 Start-up configuration). / Table 5. GPIO pin configuration / NVM parameter / GPIO_CFG[1:0] Pin name Pin function Value Description / 00b SW_CTRL_GPIO
- A serial resistor connected to the pin must be used to limit the discharge current through the pin. Maximum / discharge current is 50 mA. / The discharge is activated automatically during cable disconnection, and error recovery state. The discharge time / is programmable by NVM (see Section 5 Start-up configuration). / 2.2.13 VREG_1V2 / This pin is used only for external decoupling of the 1.2 V internal regulator. The recommended decoupling / capacitor is: 1 uF typ. (0.5 uF min., 10 uF max.)
- Description of the features / 3 Description of the features / 3.1 CC interface / The STUSB4500L controls the connection to the configuration channel (CC) pins, CC1 and CC2, through two / main blocks: the CC line interface block and the CC control logic block. / The CC line interface block is used to: / * Set pull-down termination mode on the CC pins
- The CC line interface block is used to: / * Set pull-down termination mode on the CC pins / * Monitor the CC pin voltage values related to the attachment detection thresholds / * Protect the CC pins against overvoltage / The CC control logic block is used to: / * Execute the Type-C FSM related to the sink power role with debug accessory support / * Determine the electrical state for each CC pin related to the detected thresholds
- edge (disconnection) / * The minimum value of V is V +5% and can be shifted by fraction of 1% from V +5% to / MONUSBH BUS BUS / V +20%. The value is preset by default in the NVM (see Section 7.3 Electrical and timing characteristics) / BUS / and can be changed independently through NVM programming (see Section 5 Start-up configuration) / 3.2.2 VBUS discharge
- MONUSBH BUS BUS / V +20%. The value is preset by default in the NVM (see Section 7.3 Electrical and timing characteristics) / BUS / and can be changed independently through NVM programming (see Section 5 Start-up configuration) / 3.2.2 VBUS discharge / The monitoring block also handles the V discharge paths connected to the VBUS_VS_DISCH pin for the / BUS
- Section 3.4 Hardware fault management ). At detachment, during error recovery state, the discharge is activated / for T time. / DISUSB0V / The discharge time durations are also preset by default in the NVM (see Section 7.3 Electrical and timing / characteristics). The discharge time durations can be changed through NVM programming (see Section 5 Start / up configuration). / The V discharge feature is enabled by default in the NVM and can be disabled through NVM programming
- for T time. / DISUSB0V / The discharge time durations are also preset by default in the NVM (see Section 7.3 Electrical and timing / characteristics). The discharge time durations can be changed through NVM programming (see Section 5 Start / up configuration). / The V discharge feature is enabled by default in the NVM and can be disabled through NVM programming / BUS

### Reference designs, applications, and examples

- * Source power budget reporting: (default / 1.5 A / 3 A) current at 5 V / * V powered: / BUS / Zero consumption on local battery or application / V = [4.1 V; 22 V] / DD / * Temperature range: -40 deg C up to 105 deg C
- Product status link / Power sinking device (TID #1455) / STUSB4500L / Applications / Product summary / STUSB4500LQTR * Printers, camcorders, cameras / Order code
- up to 3 A (15 W max.). / This device supports dead battery mode and is suited for sink devices powered / from dead battery state. It is able to operate without any external software support / for quick application power-on and immediate charging process start. At type-C / connection, the STUSB4500L seeks CC pin for SOURCE termination and monitors / V voltage in order to protect the application from an incorrect SOURCE operation. / BUS
- from dead battery state. It is able to operate without any external software support / for quick application power-on and immediate charging process start. At type-C / connection, the STUSB4500L seeks CC pin for SOURCE termination and monitors / V voltage in order to protect the application from an incorrect SOURCE operation. / BUS / When V is within the appropriate range, the STUSB4500L powers the application / BUS
- connection, the STUSB4500L seeks CC pin for SOURCE termination and monitors / V voltage in order to protect the application from an incorrect SOURCE operation. / BUS / When V is within the appropriate range, the STUSB4500L powers the application / BUS / by closing the input switch. The available current advertised by the SOURCE is / reported to the application in order to align the sinking current. Port status can be
- When V is within the appropriate range, the STUSB4500L powers the application / BUS / by closing the input switch. The available current advertised by the SOURCE is / reported to the application in order to align the sinking current. Port status can be / optionally monitored by the software through I2C interface. / Thanks to its 20 V technology, it implements high voltage features to protect the CC / pins against short-circuits to V .
- Marking | 4500L / | DS13102 - Rev 6 - February 2022 www.st.com For further information contact your local STMicroelectronics sales office. | / 1 Functional description / The STUSB4500L is a USB Type-C(TM) IC controller addressing 5 V sink applications. It supports dead battery / mode to allow a system to be powered from a VBUS power source directly. / The STUSB4500L major role is to: / 1. Detect the connection between two USB Type-C ports (attach detection)
- * Dead battery mode / * Internal and/or external V BUS discharge paths / * Debug accessory mode detection / * Customization of the device configuration through NVM to support specific applications / 1.1 Block overview / Figure 1. Functional block diagram / GND
- current through the pin. Maximum discharge current is 500 mA. / The pin can be also used as an open drain output to control an external V discharge path when higher / BUS / discharge current is required by the application, for instance. / The pin is activated at the same time as the internal discharge path on VBUS_VS_DISCH pin. The discharge is / activated automatically during cable disconnection and error recovery state. The discharge time is programmable / by NVM (see Section 5 Start-up configuration).
- This pin is used only for external decoupling of the 2.7 V internal regulator. The recommended decoupling / capacitor is: 1 uF typ. (0.5 uF min., 10 uF max.) / 2.2.16 VDD / This is the main STUSB4500L power supply. Whatever the application is VBUS powered or not, VDD mandatory / connection is to USB power line (VBUS). The STUSB4500L can indeed work in dead battery mode, even for / self-powered application, in order to reduce power consumption to ZERO when the port is not attached, therefore / having no impact on application power leakage.
- 2.2.16 VDD / This is the main STUSB4500L power supply. Whatever the application is VBUS powered or not, VDD mandatory / connection is to USB power line (VBUS). The STUSB4500L can indeed work in dead battery mode, even for / self-powered application, in order to reduce power consumption to ZERO when the port is not attached, therefore / having no impact on application power leakage. / STUSB4500L / Pin description
- This is the main STUSB4500L power supply. Whatever the application is VBUS powered or not, VDD mandatory / connection is to USB power line (VBUS). The STUSB4500L can indeed work in dead battery mode, even for / self-powered application, in order to reduce power consumption to ZERO when the port is not attached, therefore / having no impact on application power leakage. / STUSB4500L / Pin description / DS13102 - Rev 6 page 8/31
- 5.1 User-defined parameters / The STUSB4500L has a set of user-defined parameters that can be customized by NVM re-programming through / the I2C interface. This feature allows the customer to change the preset configuration of the USB Type-C interface / and to define a new configuration to meet specific application requirements addressing various use cases, or / specific implementations. / The NVM re-programming overrides the initial default setting to define a new default setting that is used at / power-up or after a reset. The default setting is copied at power-up, or after a reset, from the embedded NVM into
- The STUSB4500L has a set of user-defined parameters that can be customized by NVM re-programming through / the I2C interface. This feature allows the customer to change the preset configuration of the USB Type-C interface / and to define a new configuration to meet specific application requirements addressing various use cases, or / specific implementations. / The NVM re-programming overrides the initial default setting to define a new default setting that is used at / power-up or after a reset. The default setting is copied at power-up, or after a reset, from the embedded NVM into / I2C registers. The values copied in the I2C registers are used by the STUSB4500L during the system operation.
- | | | 10b | DEBUG / | | | 11b | SINK_POWER (default) / | DS13102 - Rev 6 page 14/31 | / 6 Application / The sections below are not part of the ST product specifications. They are intended to give a generic application / overview to be used by the customer as a starting point for further implementation and customization. ST does / not warrant compliance with customer specifications. Full system implementation and validation are under the
- | | | 11b | SINK_POWER (default) / | DS13102 - Rev 6 page 14/31 | / 6 Application / The sections below are not part of the ST product specifications. They are intended to give a generic application / overview to be used by the customer as a starting point for further implementation and customization. ST does / not warrant compliance with customer specifications. Full system implementation and validation are under the / customers responsibility.
- | DS13102 - Rev 6 page 14/31 | / 6 Application / The sections below are not part of the ST product specifications. They are intended to give a generic application / overview to be used by the customer as a starting point for further implementation and customization. ST does / not warrant compliance with customer specifications. Full system implementation and validation are under the / customers responsibility. / 6.1 General information
- 6 Application / The sections below are not part of the ST product specifications. They are intended to give a generic application / overview to be used by the customer as a starting point for further implementation and customization. ST does / not warrant compliance with customer specifications. Full system implementation and validation are under the / customers responsibility. / 6.1 General information / 6.1.1 Power supplies

## Page-by-page extracted content

### Page 1

#### Extracted tables

Table 1:

```text
Product status link
STUSB4500L
```

Table 2:

```text
Product summary | 
Order code | STUSB4500LQTR
 | STUSB4500LBJR
Description | Standalone USB Type-C controller (auto-run mode)
Package | QFN-24 EP (4x4)
 | WLCSP-25 (2.6x2.6x0.5)
Marking | 4500L
```

Table 3:

```text
| DS13102 - Rev 6 - February 2022 www.st.com For further information contact your local STMicroelectronics sales office. |
```

#### Raw extracted text

```text
STUSB4500L
Datasheet
Standalone USB Type-C(TM) sink port controller
Features
* Auto-run Type-C(TM) sink controller (5 V)
* Dead battery mode support
* Integrated V switch gate drivers (PMOS)
BUS
* Integrated V voltage monitoring
BUS
* Short-to-VBUS protections on CC pins
* High voltage capability on V pins
BUS
* Source power budget reporting: (default / 1.5 A / 3 A) current at 5 V
* V powered:
BUS
- Zero consumption on local battery or application
- V = [4.1 V; 22 V]
DD
* Temperature range: -40  deg C up to 105  deg C
* ESD: 3 kV HBM - 1.5 kV CDM
* Certified:
- USB Type-C(TM) rev 1.4
Product status link
- Power sinking device (TID #1455)
STUSB4500L
Applications
Product summary
STUSB4500LQTR * Printers, camcorders, cameras
Order code
* IoT, drones, accessories and battery powered devices
STUSB4500LBJR
* Computer accessories (keyboards, mouse)
Standalone USB
Description Type-C controller * Toys, gaming, POS, scanner, LED lighting
(auto-run mode) * Healthcare, e-cigarettes, handheld devices
QFN-24 EP (4x4) * 5 V DC barrel, USB STD-B and micro-B replacement
Package WLCSP-25 * Any 5 V Type-C sink device
(2.6x2.6x0.5)
Description
Marking 4500L
The STUSB4500L is a USB Type-C controller that addresses 5 V-only sink devices
up to 3 A (15 W max.).
This device supports dead battery mode and is suited for sink devices powered
from dead battery state. It is able to operate without any external software support
for quick application power-on and immediate charging process start. At type-C
connection, the STUSB4500L seeks CC pin for SOURCE termination and monitors
V voltage in order to protect the application from an incorrect SOURCE operation.
BUS
When V is within the appropriate range, the STUSB4500L powers the application
BUS
by closing the input switch. The available current advertised by the SOURCE is
reported to the application in order to align the sinking current. Port status can be
optionally monitored by the software through I2C interface.
Thanks to its 20 V technology, it implements high voltage features to protect the CC
pins against short-circuits to V .
BUS
DS13102 - Rev 6 - February 2022 www.st.com
For further information contact your local STMicroelectronics sales office.
```

### Page 2

#### Extracted tables

Table 1:

```text
| DS13102 - Rev 6 page 2/31 |
```

#### Raw extracted text

```text
1 Functional description
The STUSB4500L is a USB Type-C(TM) IC controller addressing 5 V sink applications. It supports dead battery
mode to allow a system to be powered from a VBUS power source directly.
The STUSB4500L major role is to:
1. Detect the connection between two USB Type-C ports (attach detection)
2. Establish a valid source-to-sink connection
3. Identify the attached device: source or debug accessory
4. Resolve cable orientation and twist connections to establish USB 3 data routing (MUX control) if any
5. Configure the incoming V BUS power path
6. Monitor the V BUS power path
7. Report the available power advertised by the source
8. Handle the high voltage protections
The STUSB4500L also provides:
* Dead battery mode
* Internal and/or external V BUS discharge paths
* Debug accessory mode detection
* Customization of the device configuration through NVM to support specific applications
1.1 Block overview
Figure 1. Functional block diagram
GND
SCL
SDA
CC2
CC1
VDD
V BUS status
Internal
supplyVREG_2V7
VREG_1V2
POR
VBUS_VS_DISCH
voltage
monitoring
Discharge
path
VBUS_EN_SNK
ADDR[1 ..0]
Control
DISCH
CC1DB
CC2DB
RESET
ALERT
CC
line
access
ATTACH
RP_3A; RP_1A5
GPIO
VSYS
I2C
slave
Port C
controller
A_B_SIDE
STUSB4500L
Functional description
DS13102 - Rev 6 page 2/31
```

### Page 3

#### Extracted tables

Table 1:

```text
| DS13102 - Rev 6 page 3/31 |
```

#### Raw extracted text

```text
2 Inputs/outputs
2.1 Pinout
Figure 2. QFN-24 pin connections (top view)
7  8   9   10  11    12
1 24    23 22 21  20 19
18
17
16
15
14
13
CC1DB
CC1
CC2
CC2DB
NU
SCL
VBUS_VS_DISCH
A_B_SIDE
GPIO
RP_1A5
ADDR1RESET
SDA
DISCH
GND
ADDR0 ALERT
RP_3A
VREG_1V2
VREG_2V7
VDD
VSYS
VBUS_EN_SNK
EP
ATTACH
2
3
4
5
6
Figure 3. WLCSP-25 pin connections (top view)
VBUS_VS
_ DISCH
RP_3A
VREG
_ 1V2
VREG
_ 2V7
VDD
VSYS ALERT - CC1DB CC1
VBUS _
EN_SNK
A_B _
SIDE
- CC2DB CC2
GPIO ADDR1 ADDR0 RESET SCL
RP_1A5 ATTACH GND DISCH SDA
1 2 3 4 5
A
B
C
D
E
STUSB4500L
Inputs/outputs
DS13102 - Rev 6 page 3/31
```

### Page 4

#### Extracted tables

Table 1:

```text
QFN | CSP | Name | Type | Description | Typical connection
1 | B4 | CC1DB | HV AIO | Dead battery enable on CC1 pin | To CC1 pin if used or ground
2 | B5 | CC1 | HV AIO | Type-C configuration channel 1 | To Type-C receptacle A5
3 | B3, C3 | NU |  |  | To ground
4 | C5 | CC2 | HV AIO | Type-C configuration channel 2 | To Type-C receptacle B5
5 | C4 | CC2DB | HV AIO | Dead battery enable on CC2 pin | To CC2 pin if used or ground
6 | D4 | RESET | DI | Reset input, active high | From system
7 | D5 | SCL | DI | I2C clock input | To I2C master, ext. pull-up or floating (if not used
8 | E5 | SDA | DI/OD | I2C data input/output, active low open drain | To I2C master, ext. pull-up or floating (if not used
9 | E4 | DISCH | HV AI/OD | Internal discharge path or external discharge path enable, active low open drain | From power system (internal path) or to the discharge path switch (external path), ext. pull- up
10 | E3 | GND | GND | Ground | Ground
11 | E2 | ATTACH | OD | Attachment detection, active low open drain | To MCU if any, ext. pull-up
12 | D3 | ADDR0 | DI | I2C device address setting | Static, to ground or ext. pull-up for address selection, to ground if no connection to MCU
13 | D2 | ADDR1 | DI | I2C device address setting | Static, to ground or ext. pull-up for address selection, to ground if no connection to MCU
14 | E1 | RP_1A5 | OD | 1.5 A source flag, active low open drain | To power system, ext. pull-up
15 | D1 | GPIO | OD | General purpose output, active low open drain | To system, ext. pull-up
16 | C1 | VBUS_EN_SNK | HV OD | VBUS sink power path enable, active low open drain | To power switch or to power system, ext. pull-up
17 | C2 | A_B_SIDE | OD | Cable orientation, active low open drain | USB super speed MUX select, ext. pull-up
18 | A1 | VBUS_VS_DISCH | HV AI | VBUS voltage monitoring and discharge path | From VBUS, receptacle side
19 | B2 | ALERT | OD | I2C interrupt, active low open drain | To I2C master, ext. pull-up
20 | A2 | RP_3A | HV OD | 3 A source flag, active low open drain | To power switch or to power system, ext. pull-up
21 | A3 | VREG_1V2 | PWR | 1.2 V internal regulator output | 1 uF typ. decoupling capacitor
22 | B1 | VSYS | PWR | Power supply from system | From power system, connect to ground if not used
23 | A4 | VREG_2V7 | PWR | 2.7 V internal regulator output | 1 uF typ. decoupling capacitor
24 | A5 | VDD | HV PWR | Power supply from USB power line | From VBUS, receptacle side
EP |  | EP | GND | Exposed pad is connected to ground | To ground
```

Table 2:

```text
| DS13102 - Rev 6 page 4/31 |
```

#### Raw extracted text

```text
Table 1. Pin function list
QFN CSP Name Type Description Typical connection
1 B4 CC1DB HV AIO Dead battery enable on CC1 pin To CC1 pin if used or ground
2 B5 CC1 HV AIO Type-C configuration channel 1 To Type-C receptacle A5
3 B3, C3 NU - - To ground
4 C5 CC2 HV AIO Type-C configuration channel 2 To Type-C receptacle B5
5 C4 CC2DB HV AIO Dead battery enable on CC2 pin To CC2 pin if used or ground
6 D4 RESET DI Reset input, active high From system
7 D5 SCL DI I2C clock input To I2C master, ext. pull-up or
floating (if not used
8 E5 SDA DI/OD I2C data input/output, active low open drain To I2C master, ext. pull-up or
floating (if not used
9 E4 DISCH HV AI/OD
Internal discharge path or external
discharge path enable, active low open
drain
From power system (internal
path) or to the discharge path
switch (external path), ext. pull-
up
10 E3 GND GND Ground Ground
11 E2 ATTACH OD Attachment detection, active low open
drain
To MCU if any, ext. pull-up
12 D3 ADDR0 DI
I2C device address setting Static, to ground or ext. pull-up
for address selection,
to ground if no connection to
MCU
13 D2 ADDR1 DI
I2C device address setting Static, to ground or ext. pull-up
for address selection,
to ground if no connection to
MCU
14 E1 RP_1A5 OD 1.5 A source flag, active low open drain To power system, ext. pull-up
15 D1 GPIO OD General purpose output, active low open
drain
To system, ext. pull-up
16 C1 VBUS_EN_SNK HV OD VBUS sink power path enable, active low
open drain
To power switch or to power
system, ext. pull-up
17 C2 A_B_SIDE OD Cable orientation, active low open drain USB super speed MUX select,
ext. pull-up
18 A1 VBUS_VS_DISCH HV AI VBUS voltage monitoring and discharge
path
From VBUS, receptacle side
19 B2 ALERT OD I2C interrupt, active low open drain To I2C master, ext. pull-up
20 A2 RP_3A HV OD 3 A source flag, active low open drain To power switch or to power
system, ext. pull-up
21 A3 VREG_1V2 PWR 1.2 V internal regulator output 1 uF typ. decoupling capacitor
22 B1 VSYS PWR Power supply from system From power system, connect
to ground if not used
23 A4 VREG_2V7 PWR 2.7 V internal regulator output 1 uF typ. decoupling capacitor
24 A5 VDD HV PWR Power supply from USB power line From VBUS, receptacle side
EP - EP GND Exposed pad is connected to ground To ground
STUSB4500L
Pinout
DS13102 - Rev 6 page 4/31
```

### Page 5

#### Extracted tables

Table 1:

```text
Type | Description
D | Digital
A | Analog
O | Output pad
I | Input pad
IO | Bidirectional pad
OD | Open drain output
PD | Pull-down
PU | Pull-up
HV | High voltage
PWR | Power
GND | Ground
```

Table 2:

```text
Name | Description
SCL | I2C clock, need external pull-up
SDA | I2C data, need external pull-up
ALERT | I2C interrupt, need external pull-up
ADDR0, ADDR1 | I2C device address bits (see Section 4 I2C Interface)
```

Table 3:

```text
| DS13102 - Rev 6 page 5/31 |
```

#### Raw extracted text

```text
Table 2. Pin function descriptions
Type Description
D Digital
A Analog
O Output pad
I Input pad
IO Bidirectional pad
OD Open drain output
PD Pull-down
PU Pull-up
HV High voltage
PWR Power
GND Ground
2.2 Pin description
2.2.1 CC1 / CC2
CC1 and CC2 are the configuration channel pins used for connection and attachment detection, plug orientation
determination. CC1 and CC2 are HiZ during reset.
2.2.2 CC1DB / CC2DB
CC1DB and CC2DB are enabled by dead battery mode by connecting CC1DB and CC2DB respectively to CC1
and CC2. Thanks to this connection, the pull-down terminations on the CC pins are present by default even if the
device is not supplied (see Section 3.3  Dead battery mode).
Warning: CC1DB and CC2DB must be connected to ground when dead battery mode is not supported, then Vsys
must be used.
2.2.3 RESET
Active high reset.
2.2.4 I2C interface pins
Table 3. I2C interface pin list
Name Description
SCL I2C clock, need external pull-up
SDA I2C data, need external pull-up
ALERT I2C interrupt, need external pull-up
ADDR0, ADDR1 I2C device address bits (see Section 4  I2C Interface)
Warning: ADDR0 and ADDR1 pins must be connected to ground when there is no connection to an MCU.
STUSB4500L
Pin description
DS13102 - Rev 6 page 5/31
```

### Page 6

#### Extracted tables

Table 1:

```text
Pin name | Value | Description
VBUS_EN_SNK | Hi-Z | No source attached
 | 0 | Source attached
RP_3A | Hi-Z | No source attached or source supplies default USB Type-C current at 5 V
 | 0 | Source supplies 3.0 A USB Type-C current at 5 V
RP_1A5 | Hi-Z | No source attached or source supplies default USB Type-C current at 5 V.
 | 0 | Source supplies 1.5 A USB Type-C current at 5 V.
```

Table 2:

```text
| DS13102 - Rev 6 page 6/31 |
```

#### Raw extracted text

```text
STUSB4500L
Pin description
2.2.5 DISCH
This input/output pin can be used to implement a discharge path for highly capacitive V line on power system
BUS
side.
When used as input, the discharge is internal and a serial resistor must connected to the pin to limit the discharge
current through the pin. Maximum discharge current is 500 mA.
The pin can be also used as an open drain output to control an external V discharge path when higher
BUS
discharge current is required by the application, for instance.
The pin is activated at the same time as the internal discharge path on VBUS_VS_DISCH pin. The discharge is
activated automatically during cable disconnection and error recovery state. The discharge time is programmable
by NVM (see Section 5 Start-up configuration).
2.2.6 GND
Ground.
2.2.7 ATTACH
This pin is asserted when a valid source-to-sink connection is established. It is also asserted when a connection
to a debug accessory device is detected.
2.2.8 RP_3A/RP_1A5
These pins report by default the status of the USB source current capabilities.
Table 4. Source current capability
Pin name Value Description
Hi-Z No source attached
VBUS_EN_SNK
0 Source attached
Hi-Z No source attached or source supplies default USB Type-C current at 5 V
RP_3A
0 Source supplies 3.0 A USB Type-C current at 5 V
Hi-Z No source attached or source supplies default USB Type-C current at 5 V.
RP_1A5
0 Source supplies 1.5 A USB Type-C current at 5 V.
Note: RP_3A and RP_1A5 signals are valid when a SOURCE is attached.
DS13102 - Rev 6 page 6/31
```

### Page 7

#### Extracted tables

Table 1:

```text
NVM parameter GPIO_CFG[1:0] | Pin name | Pin function | Value | Description
00b | SW_CTRL_GPIO | Software controlled GPIO. The output state is defined by the value of I2C register bit #0 at address 2Dh | Hi-Z | When bit #0 value is 0b (at start-up)
 |  |  | 0 | When bit #0 value is 1b
01b | ERROR_RECOVERY | Hardware fault detection (see Section 3.4 Hardware fault management) | Hi-Z | No hardware fault detected
 |  |  | 0 | Hardware fault detected
10b | DEBUG | Debug accessory detection (see Section 3.6 Debug accessory mode detection) | Hi-Z | No debug accessory detected
 |  |  | 0 | Debug accessory detected
11b (default) | SINK_POWER | Indicates USB Type-C current capability advertised by the source | Hi-Z | Source supplies default or 1.5 A USB Type-C current at 5 V
 |  |  | 0 | Source supplies 3.0 A USB Type-C current at 5 V
```

Table 2:

```text
Value | Description
HiZ | CC1 pin is attached to CC line
0 | CC2 pin is attached to CC line
```

Table 3:

```text
| DS13102 - Rev 6 page 7/31 |
```

#### Raw extracted text

```text
2.2.9 GPIO
This pin is an active low open drain output that can be configured by NVM as per table below (see
Section 5  Start-up configuration).
Table 5. GPIO pin configuration
NVM parameter
GPIO_CFG[1:0] Pin name Pin function Value Description
00b SW_CTRL_GPIO
Software controlled GPIO.
The output state is defined by
the value of I2C register bit #0
at address 2Dh
Hi-Z When bit #0 value is 0b (at start-up)
0 When bit #0 value is 1b
01b ERROR_RECOVERY
Hardware fault detection
(see Section 3.4  Hardware
fault management)
Hi-Z No hardware fault detected
0 Hardware fault detected
10b DEBUG
Debug accessory detection
(see Section 3.6  Debug
accessory mode detection)
Hi-Z No debug accessory detected
0 Debug accessory detected
11b
(default)
SINK_POWER
Indicates USB Type-C current
capability advertised by the
source
Hi-Z Source supplies default or 1.5 A USB
Type-C current at 5 V
0 Source supplies 3.0 A USB Type-C
current at 5 V
2.2.10 VBUS_EN_SNK
This pin allows the incoming VBUS power from the USB Type-C receptacle to be enabled when a source is
connected according to different operating conditions stated in the table below. VBUS_EN_SNK pin is a high
voltage open drain output that allows a PMOS transistor to be directly driven to enable the VBUS power path.
2.2.11 A_B_SIDE
This output pin provides the cable orientation. It is used to establish USB SuperSpeed signal routing. This signal
is not required in case of USB 2.0 support.
Table 6. USB data MUX select
Value Description
HiZ CC1 pin is attached to CC line
0 CC2 pin is attached to CC line
2.2.12 VBUS_VS_DISCH
This input pin is used to sense VBUS presence, monitor VBUS voltage, and discharge VBUS from the USB Type-C
receptacle side.
A serial resistor connected to the pin must be used to limit the discharge current through the pin. Maximum
discharge current is 50 mA.
The discharge is activated automatically during cable disconnection, and error recovery state. The discharge time
is programmable by NVM (see Section 5  Start-up configuration).
2.2.13 VREG_1V2
This pin is used only for external decoupling of the 1.2 V internal regulator. The recommended decoupling
capacitor is: 1 uF typ. (0.5 uF min., 10 uF max.)
STUSB4500L
Pin description
DS13102 - Rev 6 page 7/31
```

### Page 8

#### Extracted tables

Table 1:

```text
| DS13102 - Rev 6 page 8/31 |
```

#### Raw extracted text

```text
2.2.14 VSYS
This is the low power supply from the system, if there is any. It can be connected directly to a single cell Lithium
battery or to the system power supply delivering 3.3 V up to 5 V. It is recommended to connect the pin to ground
when it is not used.
2.2.15 VREG_2V7
This pin is used only for external decoupling of the 2.7 V internal regulator. The recommended decoupling
capacitor is: 1 uF typ. (0.5 uF min., 10 uF max.)
2.2.16 VDD
This is the main STUSB4500L power supply. Whatever the application is VBUS powered or not, VDD mandatory
connection is to USB power line (VBUS). The STUSB4500L can indeed work in dead battery mode, even for
self-powered application, in order to reduce power consumption to ZERO when the port is not attached, therefore
having no impact on application power leakage.
STUSB4500L
Pin description
DS13102 - Rev 6 page 8/31
```

### Page 9

#### Extracted tables

Table 1:

```text
| DS13102 - Rev 6 page 9/31 |
```

#### Raw extracted text

```text
STUSB4500L
Description of the features
3 Description of the features
3.1 CC interface
The STUSB4500L controls the connection to the configuration channel (CC) pins, CC1 and CC2, through two
main blocks: the CC line interface block and the CC control logic block.
The CC line interface block is used to:
* Set pull-down termination mode on the CC pins
* Monitor the CC pin voltage values related to the attachment detection thresholds
* Protect the CC pins against overvoltage
The CC control logic block is used to:
* Execute the Type-C FSM related to the sink power role with debug accessory support
* Determine the electrical state for each CC pin related to the detected thresholds
* Evaluate the conditions related to the CC pin states and the V voltage value to transition from one state
BUS
to another in the Type-C FSM
* Advertise a valid source-to-sink connection
* Determine the identity of the attached device: source or debug accessory
* Determine cable orientation to allow external routing of the USB data
* Manage USB Type-C power capability on V : USB default, medium or high current mode
BUS
* Handle hardware faults
3.2 VBUS power path control
3.2.1 VBUS monitoring
The V monitoring block supervises from the VBUS_VS_DISCH input pin the V voltage on the USB Type-C
BUS BUS
receptacle side.
It is used to check that V is within a valid voltage range to establish a valid source-to-sink connection and to
BUS
enable safely the V power path through the VBUS_EN_SNK pin.
BUS
It allows detection of unexpected V voltage conditions such as undervoltage or overvoltage related to the valid
BUS
V voltage range. When such conditions occur, the STUSB4500L reacts as follows:
BUS
* At attachment, it prevents the source-to-sink connection to be established and the V power path to be
BUS
asserted
* After attachment, it goes into unattached state and it disables the V power path
BUS
The valid V voltage range is defined by a low limit V and a high limit V (overvoltage condition):
BUS THUSB MONUSBH
* V low limit is fixed by hardware at 3.3 V in order to detect a V rising edge (connection) or falling
THUSB BUS
edge (disconnection)
* The minimum value of V is V +5% and can be shifted by fraction of 1% from V +5% to
MONUSBH BUS BUS
V +20%. The value is preset by default in the NVM (see Section 7.3 Electrical and timing characteristics)
BUS
and can be changed independently through NVM programming (see Section 5 Start-up configuration)
3.2.2 VBUS discharge
The monitoring block also handles the V discharge paths connected to the VBUS_VS_DISCH pin for the
BUS
USB Type-C receptacle side and to the DISCH pin for the power system side. The discharge paths are activated
at the same time when disconnection is detected or when the device goes into the error recovery state (see
Section 3.4 Hardware fault management ). At detachment, during error recovery state, the discharge is activated
for T time.
DISUSB0V
The discharge time durations are also preset by default in the NVM (see Section 7.3 Electrical and timing
characteristics). The discharge time durations can be changed through NVM programming (see Section 5 Start-
up configuration).
The V discharge feature is enabled by default in the NVM and can be disabled through NVM programming
BUS
(see Section 5 Start-up configuration).
DS13102 - Rev 6 page 9/31
```

### Page 10

#### Extracted tables

Table 1:

```text
| Operating conditions | 
Value | Connection stage | VBUS monitoring conditions on VBUS_VS_DISCH pin
0 | At attachment or during operation | VBUS < VMONUSBH and VBUS > VTHUSB
Hi-Z | At detachment or during ErrorRecovery | VBUS > VMONUSBH or VBUS < VTHUSB
```

Table 2:

```text
| DS13102 - Rev 6 page 10/31 |
```

#### Raw extracted text

```text
STUSB4500L
Dead battery mode
3.2.3 VBUS power path assertion
The STUSB4500L can control the assertion of the V power path from the USB Type-C receptacle, directly or
BUS
indirectly, through the VBUS_EN_SNK pin.
The table below summarizes the operating conditions that determine the electrical value of the VBUS_EN_SNK
pin during system operation.
Table 7. VBUS_EN_SNK pin behavior depending on the operating conditions
Operating conditions
Value
Connection stage VBUS monitoring conditions on VBUS_VS_DISCH pin
VBUS < VMONUSBH
0 At attachment or during operation and
VBUS > VTHUSB
VBUS > VMONUSBH
Hi-Z At detachment or during ErrorRecovery or
VBUS < VTHUSB
Type-C state column refers to the Type-C FSM states as defined in the USB Type-C standard specification.
3.3 Dead battery mode
Dead battery mode allows systems powered by a battery to be supplied by the V when the battery is
BUS
discharged and therefore to start the battery charging process without any external support. This mode is also
used in systems that are powered through the V only.
BUS
Dead battery mode operates only if the CC1DB and CC2DB pins are connected respectively to the CC1 and
CC2 pins. Thanks to these connections, the STUSB4500L presents a pull-down termination on its CC pins and
advertises itself as a sink even if the device is not supplied.
When a source system connects to a USB Type-C port, it detects the pull-down termination, establish the
source-to-sink connection, and provide the V The STUSB4500L is then supplied thanks to the VDD pin
BUS.
connected to V on the USB Type-C receptacle side. The STUSB4500L can finalize the connection and enable
BUS
the power path on V thanks to the VBUS_EN_SNK pin to allow the system to be powered.
BUS
3.4 Hardware fault management
During system operation, the STUSB4500L handles some pre-identified hardware fault conditions. When such
conditions happen, the circuit goes into an ErrorRecovery state as defined in the USB Type-C standard
specifications.
The error recovery state is equivalent to force a detach event. When entering this state, the device de-asserts the
V power path by disabling the VBUS_EN_SNK, RP_3A and RP_1A5 pins, and it removes the terminations
BUS
from the CC pins. Then, it transitions to the unattached state.
The STUSB4500L goes into error recovery state when at least one condition listed below is met:
* If an overtemperature is detected (junction temperature above maximum T )
J
* If an overvoltage is detected on the CC pins (voltage on CC pins above V )
OVP
The detection of a hardware fault is advertised through the GPIO pin when configured in ERROR_RECOVERY
mode.
See Section 7 Electrical characteristics for threshold values.
3.5 High voltage protections
The STUSB4500L can be used in systems or connected to systems that handle high voltage on the V power
BUS
path. The device integrates an internal circuitry on the CC pins that tolerates high voltage and ensures protection
up to 22 V in case of unexpected short-circuits with the V as per figure below.
BUS
DS13102 - Rev 6 page 10/31
```

### Page 11

#### Extracted tables

Table 1:

```text
# | CC1 pin (CC2 pin) | CC2 pin (CC1 pin) | Charging current configuration | A_B_SIDE pin CC1/CC2 (CC2/CC1)
1 | Rp 3 A | Rp 1.5 A | Default | Hi-Z (0)
2 | Rp 1.5 A | Rp default | 1.5 A | Hi-Z (0)
3 | Rp 3 A | Rp default | 3.0 A | Hi-Z (0)
4 | Rp def/1.5 A/3 A | Rp def/1.5 A/3 A | Default | Hi-Z (Hi-Z)
```

Table 2:

```text
| DS13102 - Rev 6 page 11/31 |
```

#### Raw extracted text

```text
STUSB4500L
Debug accessory mode detection
Figure 4. Short-to-V
BUS
3.6 Debug accessory mode detection
The STUSB4500L detects a connection to a debug and test system (DTS) as defined in the USB Type-C
standard specification. The debug accessory detection is advertised through the GPIO pin when configured in
DEBUG mode.
A debug accessory device is detected when both the CC1 and CC2 pins are pulled up by an R resistor from
p
the connected device. The voltage levels on the CC1 and CC2 pins give the orientation and current capability
as described in the table below. The GPIO pin configured in DEBUG mode is asserted to advertise the DTS
detection and the A_B_SIDE pin indicates the orientation of the connection.
Table 8. Orientation and current capability detection in sink power role
A_B_SIDE pin
CC1 pin CC2 pin Charging current
# (CC2 pin) (CC1 pin) configuration CC1/CC2
(CC2/CC1)
1 Rp 3 A Rp 1.5 A Default Hi-Z (0)
2 Rp 1.5 A Rp default 1.5 A Hi-Z (0)
3 Rp 3 A Rp default 3.0 A Hi-Z (0)
Rp Rp
4 Default Hi-Z (Hi-Z)
def/1.5 A/3 A def/1.5 A/3 A
DS13102 - Rev 6 page 11/31
```

### Page 12

#### Extracted tables

Table 1:

```text
Bit7 | Bit6 | Bit5 | Bit4 | Bit3 | Bit2 | Bit1 | Bit0
DevADDR6 | DevADDR5 | DevADDR4 | DevADDR3 | DevADDR2 | DevADDR1 | DevADDR0 | R/W
0 | 1 | 0 | 1 | 0 | ADDR1 | ADDR0 | 0/1
```

Table 2:

```text
Bit7 | Bit6 | Bit5 | Bit4 | Bit3 | Bit2 | Bit1 | Bit0
RegADDR7 | RegADDR6 | RegADDR5 | RegADDR4 | RegADDR3 | RegADDR2 | RegADDR1 | RegADDR0
```

Table 3:

```text
Bit7 | Bit6 | Bit5 | Bit4 | Bit3 | Bit2 | Bit1 | Bit0
DATA7 | DATA6 | DATA5 | DATA4 | DATA3 | DATA2 | DATA1 | DATA0
```

Table 4:

```text
Start | Deviceaddr 7 bits | W | A | Reg address 8bits | A | Restart | Deviceaddr 7 bits | R | A | R eg data 8bits | A | Reg data 8bits | A | Reg data 8bits |  | Stop
```

Table 5:

```text
Start | Deviceaddr 7 bits | W | A | Reg address 8bits | A | Reg data 8bits | A | Reg data 8bits | A | Reg data 8bits | A | Stop
```

Table 6:

```text
| DS13102 - Rev 6 page 12/31 |
```

#### Raw extracted text

```text
4 I2C Interface
4.1 Read and write operations
The I2C interface is used to configure, control and read the operation status of the device. It is compatible with the
Philips I2C Bus(R) (version 2.1). The I2C is a slave serial interface based on two signals:
* SCL - serial clock line: input clock used to shift data
* SDA - serial data line: input/output bidirectional data transfers
A filter rejects the potential spikes on the bus data line to preserve data integrity.
The bidirectional data line supports transfers up to 400 Kbit/s (fast mode). The data are shifted to and from the
chip on the SDA line, MSB first.
The first bit must be high (START) followed by the 7-bit device address and the read/write control bit.
Four 7-bit device address are available for the STUSB4500 thanks to the external programming of DevADDR0
and DevADDR1 bits through ADDR0 and ADDR1 pins setting i.e. 0x28 or 0x29 or 0x2A or 0x2B. It allows four
STUSB4500 devices to be connected on the same I2C bus.
Table 9. Device address format
Bit7 Bit6 Bit5 Bit4 Bit3 Bit2 Bit1 Bit0
DevADDR6 DevADDR5 DevADDR4 DevADDR3 DevADDR2 DevADDR1 DevADDR0 R/W
0 1 0 1 0 ADDR1 ADDR0 0/1
Table 10. Register address format
Bit7 Bit6 Bit5 Bit4 Bit3 Bit2 Bit1 Bit0
RegADDR7 RegADDR6 RegADDR5 RegADDR4 RegADDR3 RegADDR2 RegADDR1 RegADDR0
Table 11. Register data format
Bit7 Bit6 Bit5 Bit4 Bit3 Bit2 Bit1 Bit0
DATA7 DATA6 DATA5 DATA4 DATA3 DATA2 DATA1 DATA0
Figure 5. Read operation
S tart Deviceaddr
7 bits
W A R eg address
8 bits
A R estart Deviceaddr
7 bits
R A R   eg data
8 bits
A R eg data
8 bits
A R eg data
8 bits
 S top
Master S lave
Address
n+1
Address
n+2S   tart bit = S DA fallingwhenS C L = 1
S top bit = S DA risingwhenS C L = 1
R estart bit = startaftera start
Acknowledge= S DA forcedlow duringa S C L  clock
Figure 6. Write operation
S tart Device addr
7 bits
W A R eg address
8 bits
A R eg data
8 bits
A R eg data
8 bits
A R eg data
8 bits
A S top
Address
n+1
Address
n+2S tart bit = S DA falling when S C L = 1
S top bit = S DA rising when S C L = 1
R estart bit = start after a start
STUSB4500L
I2C Interface
DS13102 - Rev 6 page 12/31
```

### Page 13

#### Extracted tables

Table 1:

```text
Symbol | Parameter | Min. | Typ. | Max. | Unit
Fscl | SCL clock frequency | 0 |  | 400 | kHz
thd,sta | Hold time (repeated) START condition | 0.6 |  |  | us
tlow | LOW period of the SCL clock | 1.3 |  |  | 
thigh | HIGH period of the SCL clock | 0.6 |  |  | 
tsu,dat | Setup time for repeated START condition | 0.6 |  |  | 
thd,dat | Data hold time | 0.04 |  | 0.9 | 
tsu,dat | Data setup time | 100 |  |  | 
tr | Rise time of both SDA and SCL signals | 20 + 0.1 Cb |  | 300 | ns
tf | Fall time of both SDA and SCL signals | 20 + 0.1 Cb |  | 300 | 
tsu,sto | Set-up time for STOP condition | 0.6 |  |  | us
tbuf | Bus free time between a STOP and START condition | 1.3 |  |  | 
Cb | Capacitive load for each bus line |  |  | 400 | pF
```

Table 2:

```text
|  |  |  |  |  |  |  |  |  |  |  | t t su,dat high |  |  |  |  |  |  |
```

Table 3:

```text
| DS13102 - Rev 6 page 13/31 |
```

#### Raw extracted text

```text
STUSB4500L
Timing specifications
4.2 Timing specifications
The device uses a standard slave I2C channel at speed up to 400 kHz.
Table 12. I2C timing parameters - VDD = 5 V
Symbol Parameter Min. Typ. Max. Unit
Fscl SCL clock frequency 0 400 kHz
Hold time (repeated) START
thd,sta
condition
0.6 -
tlow LOW period of the SCL clock 1.3 -
thigh HIGH period of the SCL clock 0.6 -
us
Setup time for repeated START
tsu,dat
condition
0.6 -
thd,dat Data hold time 0.04 0.9
-
tsu,dat Data setup time 100 -
Rise time of both SDA and SCL
tr
signals
20 + 0.1 Cb 300
ns
Fall time of both SDA and SCL
tf
signals
20 + 0.1 Cb 300
tsu,sto Set-up time for STOP condition 0.6 -
us
Bus free time between a STOP
tbuf
and START condition
1.3 -
Cb Capacitive load for each bus line - 400 pF
Figure 7. I2C timing diagram
t
f
V
ih
SDA
V
il
t
hd,sta
t t t
r su,dat high
SCL
t t t
low hd,dat su,sto
DS13102 - Rev 6 page 13/31
```

### Page 14

#### Extracted tables

Table 1:

```text
Parameter name | Parameter description | Reset value (default) | Value | Description
SHIFT_VBUS_HIGH_LIMIT | Coefficient to shift up nominal VBUS high voltage limit applicable to 5 V | 1010b (10%) | 0000b to 1111b | 0% <= VSHUSBH <= 15% of VBUS by increment of 1% Default VSHUSBH = 10%
VBUS_DISCH_TIME_TO_0V | Coefficient used to compute VBUS discharge time to 0 V | 1001b (9) | 0001b to 1111b | 1 <= TDISPAR0V <= 15 by increment of 1 Unit discharge time: 84 ms (typ.) Default coefficient TDISPAR0V = 9, discharge time TDISUSB0V= 756 ms
VBUS_DISCH_DISABLE | VBUSdischarge deactivation on VBUS_VS_DISCH and DISCH pins | 0b | 0b | VBUS discharge enabled
 |  |  | 1b | VBUS discharge disabled
GPIO_CFG[1:0] | Selects GPIO pin configuration (see Section 2.2.9 GPIO ) | 11b | 00b | SW_CTRL_GPIO
 |  |  | 01b | ERROR_RECOVERY
 |  |  | 10b | DEBUG
 |  |  | 11b | SINK_POWER (default)
```

Table 2:

```text
| DS13102 - Rev 6 page 14/31 |
```

#### Raw extracted text

```text
5 Start-up configuration
5.1 User-defined parameters
The STUSB4500L has a set of user-defined parameters that can be customized by NVM re-programming through
the I2C interface. This feature allows the customer to change the preset configuration of the USB Type-C interface
and to define a new configuration to meet specific application requirements addressing various use cases, or
specific implementations.
The NVM re-programming overrides the initial default setting to define a new default setting that is used at
power-up or after a reset. The default setting is copied at power-up, or after a reset, from the embedded NVM into
I2C registers. The values copied in the I2C registers are used by the STUSB4500L during the system operation.
The NVM re-programming is possible with a customer password. The I2C registers must be re-initialized after
each NVM re-programming to make effective the new parameters setting either through power-off and power-up
sequence, or through reset.
5.2 Default start-up configuration
The table below lists the user-defined parameters and indicates the default start-up configuration of the
STUSB4500L.
Table 13. STUSB4500L user-defined parameters and default settings
Parameter name Parameter description
Reset
value
(default)
Value Description
SHIFT_VBUS_HIGH_LIMIT
Coefficient to shift up nominal
VBUS high voltage limit applicable
to 5 V
1010b
(10%)
0000b to
1111b
0% <= VSHUSBH <= 15% of VBUS
by increment of 1%
Default VSHUSBH = 10%
VBUS_DISCH_TIME_TO_0V
Coefficient used to compute
VBUS discharge time to 0 V
1001b
(9)
0001b to
1111b
1 <= TDISPAR0V <= 15 by increment
of 1
Unit discharge time: 84 ms (typ.)
Default coefficient TDISPAR0V = 9,
discharge time TDISUSB0V= 756
ms
VBUS_DISCH_DISABLE
VBUSdischarge deactivation on
VBUS_VS_DISCH and DISCH
pins
0b
0b VBUS discharge enabled
1b VBUS discharge disabled
GPIO_CFG[1:0]
Selects GPIO pin configuration
(see Section 2.2.9  GPIO )
11b
00b SW_CTRL_GPIO
01b ERROR_RECOVERY
10b DEBUG
11b SINK_POWER (default)
STUSB4500L
Start-up configuration
DS13102 - Rev 6 page 14/31
```

### Page 15

#### Extracted tables

Table 1:

```text
Power On Reset | I2C registersloadingfromNVM | I2C access
```

Table 2:

```text
Reset | I2C registersloadingfromNVM | I2C access
```

Table 3:

```text
| DS13102 - Rev 6 page 15/31 |
```

#### Raw extracted text

```text
6 Application
The sections below are not part of the ST product specifications. They are intended to give a generic application
overview to be used by the customer as a starting point for further implementation and customization. ST does
not warrant compliance with customer specifications. Full system implementation and validation are under the
customers responsibility.
6.1 General information
6.1.1 Power supplies
The STUSB4500L can be supplied in three different ways depending on the targeted application:
* Through the VDD pin only for applications powered by V BUS that operate with dead battery mode support
* Through the VSYS pin only for AC powered applications with a system power supply delivering from 3.3 V
up to 5 V
* Through the VDD and VSYS pins either for applications powered by a battery with dead battery mode
support or for applications powered by VBUS with a system power supply delivering 3.3 V or 5 V. When both
VDD and VSYS power supplies are present, the low power supply VSYS is selected when VSYS voltage is
above 3.1 V. Otherwise VDD is selected
When possible, please prefer VDD supply only, and connect it to VBUS in order to minimize application power
consumption. In this case, VSYS is not used and must be connected to GND.
6.1.2 Connection to MCU or application processor
The STUSB4500L connection to an MCU or an application processor is optional. However, an I2C interface with
an interrupt allows a simple connection to most of MCU and SOC of the market.
When a connection through the I2C interface is implemented, it provides an extensive functionality during the
system operation. For instance, it may be used to:
1. Define the port configuration during system boot (in case the NVM parameters are not customized during
manufacturing)
2. Provide a diagnostic of the Type-C connection in real time
At power-up or after a reset, the first software access to the I2C registers of the STUSB4500L can be done only
after TLOAD as shown in the figure below. TLOAD corresponds to the time required to initialize the I2C registers with
the default values from the embedded NVM. At power-up, the loading phase starts when the voltage level on the
VREG_1V2 output pin of the 1.2 V internal regulator reaches 1.08 V to release the internal POR signal. After a
reset, the loading phase starts when the signal on the RESET pin is released.
Figure 8. I2C register initialization sequence at power-up or after a reset
Power On Reset I 2 C r egisters l oading from NVM I 2 C access
T LOAD
VSYS or VDD
VREG_1V2
POR
I 2 C (SCL,SDA)
1.08 V
Reset I 2 C r egisters l oading from NVM I 2 C access
T LOAD
VSYS or VDD
VREG_1V2
RESET
I 2 C (SCL,SDA)
At power - up After a reset
STUSB4500L
Application
DS13102 - Rev 6 page 15/31
```

### Page 16

#### Extracted tables

Table 1:

```text
23 21 | VREG_2V7 VDD VREG_1V2 VBUS_VS_DISCH VSYS RP_3A VBUS_EN_SNK Not_Used A_B_SIDE GND DISCH CC1DB CC1 GPIO CC2 RP_1A5 ADDR1 CC2DB RESET ADDR0 SCL PE_DNG ATTACH SDA ALERT
```

Table 2:

```text
3
10
```

Table 3:

```text
| B8 B7
 | B6 B5
CC2 | B4
```

Table 4:

```text
A5
A6
A7 A8 A9
```

Table 5:

```text
4 | 
 | 5
```

Table 6:

```text
| DS13102 - Rev 6 page 16/31 |
```

#### Raw extracted text

```text
6.2 Typical application
Figure 9. Implementation example
VBUS
STL9P3LLH6
R1 100K
R3 20K
J1
B12GND GND A1 USB3-C VBUS B11Rx+1 Tx+1A2 B10Rx-1 Tx-1A3
B9Vbus VbusA4
USB_DM B B8 7D Sb -2 u2 C D+ C 1 1A A 5 6 USB_D C P C1
VBUS US C B C _D 2 P B B B 5 6 4V C D b + C u 2 2 s V S D b b u - u 1 s 1 A A A 8 7 9 USB_D V M BUS B B 2 3 T T x x + -2 2 T U Y S P B E 3 C R R x x + -2 2A A 1 1 1 0 B1 GND GND A12
D2
ESDA25L
GND GND
GND
SYS_SUBV
VBUS_SYS L1
C4 Inductor
R2 USB_DP BatteryCharger 10mH 1K Cap
USB_DM 100pF VSYS VSYS
INM_ILIM
2V7 C1 R 1K 4
C 1u 2 F 1V2 1uF GND
C
1u
3
F
23VREG_2V7
GND
R
13
5
0 GND 21VREG_1V2 VBUS_VS_DISCH18 GND 22VSYS RP_3A20 ILIM_3A0 ILIM_3A0
VBUS_EN_SNK16
A_B_SIDE17
GND DISCH9 R 13 6 0 2CC1 GPIO15 ESDA25P35 D1
SCL7
6 4
S
R C
C
E C S
L
2 ET R A P D _ D 1 R A 1 5 1 1 3 4 ILIM_1A5 ILIM_1A5 R 52 1 0 0
SDA8SDA Alert
GND
GND
GND
GND
V3V3
V3V3
R7 R8 R9
10K 10K 10K SDA
SCL
MCU
Alert
OPTIONAL
PE_DNG0
STUSB4500L
Typical application
(Optional)
U_stusb4500L
VDD24
3Not_Used
10GND
1CC1DB 5CC2DB G to P fl I a O g c h a a n rd b w e a c re o n fa fig u u lt, r ed ADDR012 i i f n f s o y r s m te e m d needs to be
ATTACH11
ALERT19
STUSB4500L
GND
Note: The STUSB4500L can be connected to an application processor using I2C interface. This connection is optional.
DS13102 - Rev 6 page 16/31
```

### Page 17

#### Extracted tables

Table 1:

```text
Symbol | Parameter | Value | Unit
VDD | Supply voltage on VDD pin | 28 | V
VSYS | Supply voltage on VSYS pin | 6 | 
VCC1, VCC2 VCC1DB, VCC2DB | High voltage on CC pins | 22 | 
VVBUS_EN_SNK VVBUS_VS_DISCH VDISCH VRP_3A | High voltage on VBUS pins | 28 | 
VSCL, VSDA VALERT VRESET VATTACH VA_B_SIDE VRP_1A5 VGPIO VADDR0, VADDR1 | Operating voltage on I/O pins | 0.3 to 6 | 
TSTG | Storage temperature | 55 to 150 | deg C
TJ | Maximum junction temperature | 145 | 
ESD | HBM | 3 | kV
 | CDM | 1.5 |
```

Table 2:

```text
Symbol | Parameter | Value | Unit
VDD | Supply voltage on VDD pin | 3.3 to 6 | V
VSYS | Supply voltage on VSYS pin | 3.0 to 5.5 | 
VCC1, VCC2 VCC1DB, VCC2DB | CC pins | 0 to 5.5 | 
VVBUS_EN_SNK VVBUS_VS_DISCH VDISCH VRP_3A | High voltage pins | 0 to 22 | 
VSCL, VSDA | Operating voltage on I/O pins | 0 to 4.5 |
```

Table 3:

```text
| DS13102 - Rev 6 page 17/31 |
```

#### Raw extracted text

```text
7 Electrical characteristics
7.1 Absolute maximum ratings
All voltages are referenced to GND.
Table 14. Absolute maximum ratings
Symbol Parameter Value Unit
VDD Supply voltage on VDD pin 28
V
VSYS Supply voltage on VSYS pin 6
VCC1, VCC2
VCC1DB, VCC2DB
High voltage on CC pins 22
VVBUS_EN_SNK
VVBUS_VS_DISCH
VDISCH
VRP_3A
High voltage on VBUS pins 28
VSCL, VSDA
VALERT
VRESET
VATTACH
VA_B_SIDE
VRP_1A5
VGPIO
VADDR0, VADDR1
Operating voltage on I/O pins -0.3 to 6
TSTG Storage temperature -55 to 150
 deg C
TJ Maximum junction temperature 145
ESD
HBM 3
kV
CDM 1.5
7.2 Operating conditions
Table 15. Operating conditions
Symbol Parameter Value Unit
VDD Supply voltage on VDD pin 3.3 to 6
V
VSYS Supply voltage on VSYS pin 3.0 to 5.5
VCC1, VCC2
VCC1DB, VCC2DB
CC pins
0 to 5.5
VVBUS_EN_SNK
VVBUS_VS_DISCH
VDISCH
VRP_3A
High voltage pins 0 to 22
VSCL, VSDA Operating voltage on I/O pins 0 to 4.5
STUSB4500L
Electrical characteristics
DS13102 - Rev 6 page 17/31
```

### Page 18

#### Extracted tables

Table 1:

```text
Symbol | Parameter | Value | Unit
VALERT VRESET VATTACH VA_B_SIDE VRP_1A5 VGPIO VADDR0, VADDR1 |  |  | V
TA | Operating temperature | 40 to 105 | deg C
```

Table 2:

```text
| DS13102 - Rev 6 page 18/31 |
```

#### Raw extracted text

```text
Symbol Parameter Value Unit
VALERT
VRESET
VATTACH
VA_B_SIDE
VRP_1A5
VGPIO
VADDR0, VADDR1
V
TA Operating temperature -40 to 105  deg C
STUSB4500L
Operating conditions
DS13102 - Rev 6 page 18/31
```

### Page 19

#### Extracted tables

Table 1:

```text
Symbol | Parameter | Conditions | Min. | Typ. | Max. | Unit
IDD (SNK) | Current consumption | Device connected to VBUS VDD @ VBUS level | 110 | 160 | 210 | uA
TLOAD | I2C registers loading time from NVM | At power-up or after a reset |  |  | 30 | ms
CC1 and CC2 pins |  |  |  |  |  | 
Rd | CC pull-down resistors | 40 deg C < TA < +105 deg C | 10% | 5.1 | +10% | kOhm
RINCC | CC input impedance | Terminations off | 200 |  |  | kOhm
VTH0.2 | Detection threshold 1 | Min. IP-USB detection by sink on Rd, min CC voltage for connected sink | 0.15 | 0.20 | 0.25 | V
VTH0.66 | Detection threshold 2 | Min. I P_1.5 detection by sink on Rd | 0.61 | 0.66 | 0.71 | V
VTH1.23 | Detection threshold 3 | Min. I P_3.0 detection by sink on Rd | 1.16 | 1.23 | 1.31 | V
VTH2.6 | Detection threshold 4 | Max. CC voltage for connected sink | 2.45 | 2.60 | 2.75 | V
VOVP | Overvoltage protection on CC pins |  | 5.82 | 6 | 6.18 | V
VBUS_VS_DISCH pin monitoring and driving |  |  |  |  |  | 
VTHUSB | VBUS disconnection threshold | VDD@ 5 V | 3.2 | 3.3 | 3.4 | V
IDISUSB | VBUS discharge current | Through external resistor connected to VBUS_VS_DISCH pin |  |  | 50 | mA
TDISUSB0V | VBUS discharge time to 0 V | At detachment, during error recovery state. Coefficient TDISPAR0V programmable by NVM, Default TDISPAR0V = 9, TDISUSB0V = 756 ms | 70 *TDISPAR0V | 84 *TDISPAR0V | 100 *TDISPAR0V | ms
VMONUSBH | VBUS monitoring high voltage limit | VBUS+5% is nominal high voltage limit, Shift coefficient VSHUSBH is programmable by NVM from 0% to 15% of VBUS by step of 1% Default VSHUSBH = 10%, VMONUSBH = VBUS+15% |  | VBUS+5% +VSHUSBH |  | V
DISCH pin driving |  |  |  |  |  | 
IDISPWR | Power system discharge current | Through external resistor connected to DISCH pin |  |  | 500 | mA
Digital input/output (SCL, SDA, ALERT, RESET, ATTACH, A_B_SIDE, RP_1A5, GPIO, ADDR0, ADDR1) |  |  |  |  |  | 
VIH | High level input voltage |  | 1.2 |  |  | V
VIL | Low level input voltage |  |  |  | 0.35 | V
VOL | Low level output voltage | Ioh = 3 mA |  |  | 0.4 | V
20 V open drain outputs (VBUS_EN_SNK, DISCH, RP_3A) |  |  |  |  |  | 
VOL | Low level output voltage | Ioh = 3 mA |  |  | 0.4 | V
```

Table 2:

```text
| DS13102 - Rev 6 page 19/31 |
```

#### Raw extracted text

```text
STUSB4500L
Electrical and timing characteristics
7.3 Electrical and timing characteristics
Unless otherwise specified: V = 5 V, T = 25  deg C, all voltages are referenced to GND.
DD A
Table 16. Electrical characteristics
Symbol Parameter Conditions Min. Typ. Max. Unit
Device connected to VBUS
IDD (SNK) Current consumption 110 160 210 uA
VDD @ VBUS level
I2C registers loading time
TLOAD At power-up or after a reset 30 ms
from NVM
CC1 and CC2 pins
Rd CC pull-down resistors -40  deg C < TA < +105  deg C -10% 5.1 +10% kOhm
RINCC CC input impedance Terminations off 200 kOhm
VTH0.2 Detection threshold 1
Min. IP-USB detection by sink on Rd, min
0.15 0.20 0.25 V
CC voltage for connected sink
VTH0.66 Detection threshold 2 Min. I P_1.5 detection by sink on Rd 0.61 0.66 0.71 V
VTH1.23 Detection threshold 3 Min. I P_3.0 detection by sink on Rd 1.16 1.23 1.31 V
VTH2.6 Detection threshold 4 Max. CC voltage for connected sink 2.45 2.60 2.75 V
Overvoltage protection on
VOVP
CC pins
5.82 6 6.18 V
VBUS_VS_DISCH pin monitoring and driving
VTHUSB
VBUS disconnection
VDD@ 5 V 3.2 3.3 3.4 V
threshold
Through external resistor connected to
IDISUSB VBUS discharge current
VBUS_VS_DISCH pin
50 mA
At detachment, during error recovery
state.
TDISUSB0V
t
V
im
BU
e
S
t o
d i
0
s c
V
harge C
N
o
V
e
M
ff
,
icient TDISPAR0V programmable by
*TDIS
7
P
0
AR0V *TDIS
8
P
4
AR0V *TDI
1
S
0
P
0
AR0V
ms
Default TDISPAR0V = 9, TDISUSB0V = 756
ms
VBUS+5% is nominal high voltage limit,
Shift coefficient VSHUSBH is
programmable by NVM from 0% to 15%
VMONUSBH VBUS monitoring high of VBUS by step of 1%
VBUS+5%
V
voltage limit
Default
+VSHUSBH
VSHUSBH = 10%, VMONUSBH =
VBUS+15%
DISCH pin driving
Power system discharge Through external resistor connected to
IDISPWR
current DISCH pin
500 mA
Digital input/output (SCL, SDA, ALERT, RESET, ATTACH, A_B_SIDE, RP_1A5, GPIO, ADDR0, ADDR1)
VIH High level input voltage 1.2 V
VIL Low level input voltage 0.35 V
VOL Low level output voltage Ioh = 3 mA 0.4 V
20 V open drain outputs (VBUS_EN_SNK, DISCH, RP_3A)
VOL Low level output voltage Ioh = 3 mA 0.4 V
DS13102 - Rev 6 page 19/31
```

### Page 20

#### Extracted tables

Table 1:

```text
|  | E
```

Table 2:

```text
| 0.08 | C
```

Table 3:

```text
|  |  | 2E
 | D2 |  |
```

Table 4:

```text
| DS13102 - Rev 6 page 20/31 |
```

#### Raw extracted text

```text
8 Package information
In order to meet environmental requirements, ST offers these devices in different grades of ECOPACK packages,
depending on their level of environmental compliance. ECOPACK specifications, grade definitions and product
status are available at: www.st.com. ECOPACK is an ST trademark.
8.1 QFN-24 EP (4x4) package information
Figure 10. QFN-24 EP (4x4) package information
P LAN E
S E ATIN G
0.08 C
C
TO P  VIE W
S ID E  VIE W
B O TTO M  VIE W
P in#1  ID
D
E
e
D 2
E 2
b
K
L
A1
A
STUSB4500L
Package information
DS13102 - Rev 6 page 20/31
```

### Page 21

#### Extracted tables

Table 1:

```text
Ref. | mm |  |  | Inches |  | 
 | Min. | Typ | Max. | Min. | Typ. | Max.
A | 0.80 | 0.90 | 1.00 | 0.031 | 0.035 | 0.039
A1 | 0.00 | 0.02 | 0.05 | 0.000 | 0.001 | 0.002
b | 0.18 | 0.25 | 0.30 | 0.007 | 0.0010 | 0.012
D | 3.95 | 4.00 | 4.05 | 0.156 | 0.157 | 0.159
D2 | 2.55 | 2.70 | 2.80 | 0.100 | 0.106 | 0.110
E | 3.95 | 4.00 | 4.05 | 0.156 | 0.157 | 0.159
E2 | 2.55 | 2.70 | 2.80 | 0.100 | 0.106 | 0.110
e | 0.45 | 0.50 | 0.55 | 0.018 | 0.020 | 0.022
K | 0.15 |  |  | 0.006 |  | 
L | 0.30 | 0.40 | 0.50 | 0.012 | 0.016 | 0.020
```

Table 2:

```text
| DS13102 - Rev 6 page 21/31 |
```

#### Raw extracted text

```text
Table 17. QFN-24 EP (4x4) package mechanical data
Ref.
mm Inches
Min. Typ Max. Min. Typ. Max.
A 0.80 0.90 1.00 0.031 0.035 0.039
A1 0.00 0.02 0.05 0.000 0.001 0.002
b 0.18 0.25 0.30 0.007 0.0010 0.012
D 3.95 4.00 4.05 0.156 0.157 0.159
D2 2.55 2.70 2.80 0.100 0.106 0.110
E 3.95 4.00 4.05 0.156 0.157 0.159
E2 2.55 2.70 2.80 0.100 0.106 0.110
e 0.45 0.50 0.55 0.018 0.020 0.022
K 0.15 - - 0.006 - -
L 0.30 0.40 0.50 0.012 0.016 0.020
Figure 11. QFN-24 EP (4x4) recommended footprint
STUSB4500L
QFN-24 EP (4x4) package information
DS13102 - Rev 6 page 21/31
```

### Page 22

#### Extracted tables

Table 1:

```text
| DS13102 - Rev 6 page 22/31 |
```

#### Raw extracted text

```text
8.2 WLCSP (2.6x2.6x0.5) 25 bumps package information
Figure 12. WLCSP (2.6x2.6x0.5) package outline
STUSB4500L
WLCSP (2.6x2.6x0.5) 25 bumps package information
DS13102 - Rev 6 page 22/31
```

### Page 23

#### Extracted tables

Table 1:

```text
Symbol | mm |  | 
 | Min. | Typ. | Max.
A | 0.456 | 0.50 | 0.544
A1 | 0.179 | 195 | 0.211
A2 | 0.255 | 0.28 | 0.305
A3 | 0.022 | 0.025 | 0.028
E | 2.563 | 2.593 | 2.623
D | 2.563 | 2.593 | 2.623
E1 | 1.6 BSC |  | 
D1 | 1.6 BSC |  | 
e | 0.4 BSC |  | 
b | 0.245 |  | 0.295
n | 25 |  | 
Tolerance of form and position |  |  | 
aaa | 0.03 |  | 
bbb | 0.06 |  | 
ccc | 0.05 |  | 
ddd | 0.015 |  |
```

Table 2:

```text
| DS13102 - Rev 6 page 23/31 |
```

#### Raw extracted text

```text
Table 18. WLCSP (2.6x2.6x0.5) package mechanical data
Symbol
mm
Min. Typ. Max.
A 0.456 0.50 0.544
A1 0.179 195 0.211
A2 0.255 0.28 0.305
A3 0.022 0.025 0.028
E 2.563 2.593 2.623
D 2.563 2.593 2.623
E1 1.6 BSC
D1 1.6 BSC
e 0.4 BSC
b 0.245 0.295
n 25
Tolerance of form and position
aaa 0.03
bbb 0.06
ccc 0.05
ddd 0.015
Note: WLCSP stands for wafer level chip scale package. The typical ball diameter before mounting is 0.25 mm. The
terminal A1 corner must be identified on the top surface by using a laser marking dot.
Figure 13. WLCSP (2.6x2.6x0.5) recommended footprint
STUSB4500L
WLCSP (2.6x2.6x0.5) 25 bumps package information
DS13102 - Rev 6 page 23/31
```

### Page 24

#### Extracted tables

Table 1:

```text
Symbol | Parameter | Value | Unit
RJA | Junction-to-ambient thermal resistance | 37 | deg C/W
RJC | Junction-to-case thermal resistance | 5 |
```

Table 2:

```text
| DS13102 - Rev 6 page 24/31 |
```

#### Raw extracted text

```text
8.3 Thermal information
Table 19. Thermal information
Symbol Parameter Value Unit
RJA
Junction-to-ambient thermal
resistance 37
 deg C/W
RJC
Junction-to-case thermal
resistance 5
STUSB4500L
Thermal information
DS13102 - Rev 6 page 24/31
```

### Page 25

#### Extracted tables

Table 1:

```text
Term | Description
Accessory mode | Debug accessory mode. It is defined by the presence of pull-up resistors Rp/Rp on CC1/CC2 pins in sink power role.
DFP | Downstream facing port, specifically associated with the flow of data in a USB connection. Typically the ports on a HOST or the ports on a hub to which devices are connected. In its initial state, the DFP sources VBUS and optionally VCONN, and supports data.
DRP | Dual-role port. A port that can operate as either a source or a sink. The port role may be changed dynamically.
Sink | Port asserting Rd on the CC pins and consuming power from the VBUS.
Source | Port asserting Rp on the CC pins and providing power over the VBUS.
UFP | Upstream facing port, specifically associated with the flow of data in a USB connection. The port on a device or a hub that connects to a host or the DFP of a hub. In its initial state, the UFP sinks VBUS and supports data.
```

Table 2:

```text
| DS13102 - Rev 6 page 25/31 |
```

#### Raw extracted text

```text
9 Terms and abbreviations
Table 20. List of terms and abbreviations
Term Description
Accessory mode Debug accessory mode. It is defined by the presence of pull-up resistors Rp/Rp on
CC1/CC2 pins in sink power role.
DFP
Downstream facing port, specifically associated with the flow of data in a USB
connection. Typically the ports on a HOST or the ports on a hub to which devices
are connected. In its initial state, the DFP sources VBUS and optionally VCONN, and
supports data.
DRP Dual-role port. A port that can operate as either a source or a sink. The port role
may be changed dynamically.
Sink Port asserting Rd on the CC pins and consuming power from the VBUS.
Source Port asserting Rp on the CC pins and providing power over the VBUS.
UFP
Upstream facing port, specifically associated with the flow of data in a USB
connection. The port on a device or a hub that connects to a host or the DFP
of a hub. In its initial state, the UFP sinks VBUS and supports data.
STUSB4500L
Terms and abbreviations
DS13102 - Rev 6 page 25/31
```

### Page 26

#### Extracted tables

Table 1:

```text
Date | Revision | Changes
10-Oct-2019 | 1 | Initial release.
22-Oct-2019 | 2 | Added Figure 13. WLCSP (2.6x2.6x0.5) recommended footprint.
29-Apr-2020 | 3 | Added Section 3.5 High voltage protections.
08-Jun-2020 | 4 | Updated Figure 13. WLCSP (2.6x2.6x0.5) recommended footprint.
15-Jun-2021 | 5 | Updated Section Features and Section Description.
15-Feb-2022 | 6 | Updated Figure 9. Implementation example
```

Table 2:

```text
| DS13102 - Rev 6 page 26/31 |
```

#### Raw extracted text

```text
Revision history
Table 21. Document revision history
Date Revision Changes
10-Oct-2019 1 Initial release.
22-Oct-2019 2 Added Figure 13. WLCSP (2.6x2.6x0.5) recommended footprint.
29-Apr-2020 3 Added Section 3.5 High voltage protections.
08-Jun-2020 4 Updated Figure 13. WLCSP (2.6x2.6x0.5) recommended footprint.
15-Jun-2021 5 Updated Section Features and Section Description.
15-Feb-2022 6 Updated Figure 9. Implementation example
STUSB4500L
DS13102 - Rev 6 page 26/31
```

### Page 27

#### Extracted tables

Table 1:

```text
| DS13102 - Rev 6 page 27/31 |
```

#### Raw extracted text

```text
Contents
1 Functional description ............................................................. 2
1.1 Block overview................................................................. 2
2 Inputs/outputs ..................................................................... 3
2.1 Pinout ........................................................................ 3
2.2 Pin description ................................................................. 5
2.2.1 CC1 / CC2 ............................................................. 5
2.2.2 CC1DB / CC2DB......................................................... 5
2.2.3 RESET ................................................................ 5
2.2.4 I2C interface pins......................................................... 5
2.2.5 DISCH................................................................. 6
2.2.6 GND .................................................................. 6
2.2.7 ATTACH ............................................................... 6
2.2.8 RP_3A/RP_1A5 ......................................................... 6
2.2.9 GPIO.................................................................. 7
2.2.10 VBUS_EN_SNK ......................................................... 7
2.2.11 A_B_SIDE.............................................................. 7
2.2.12 VBUS_VS_DISCH ....................................................... 7
2.2.13 VREG_1V2 ............................................................. 7
2.2.14 VSYS ................................................................. 8
2.2.15 VREG_2V7 ............................................................. 8
2.2.16 VDD .................................................................. 8
3 Description of the features......................................................... 9
3.1 CC interface................................................................... 9
3.2 VBUS power path control........................................................ 9
3.2.1 VBUS monitoring ........................................................ 9
3.2.2 VBUS discharge ......................................................... 9
3.2.3 VBUS power path assertion ............................................... 10
3.3 Dead battery mode ............................................................ 10
3.4 Hardware fault management .................................................... 10
3.5 High voltage protections........................................................ 10
3.6 Debug accessory mode detection................................................ 11
4 I2C Interface ...................................................................... 12
4.1 Read and write operations ...................................................... 12
4.2 Timing specifications........................................................... 13
5 Start-up configuration ............................................................ 14
STUSB4500L
Contents
DS13102 - Rev 6 page 27/31
```

### Page 28

#### Extracted tables

Table 1:

```text
| DS13102 - Rev 6 page 28/31 |
```

#### Raw extracted text

```text
5.1 User-defined parameters ....................................................... 14
5.2 Default start-up configuration.................................................... 14
6 Application ....................................................................... 15
6.1 General information ........................................................... 15
6.1.1 Power supplies ......................................................... 15
6.1.2 Connection to MCU or application processor .................................. 15
6.2 Typical application............................................................. 16
7 Electrical characteristics.......................................................... 17
7.1 Absolute maximum ratings...................................................... 17
7.2 Operating conditions........................................................... 17
7.3 Electrical and timing characteristics .............................................. 19
8 Package information.............................................................. 20
8.1 QFN-24 EP (4x4) package information............................................ 20
8.2 WLCSP (2.6x2.6x0.5) 25 bumps package information............................... 22
8.3 Thermal information ........................................................... 24
9 Terms and abbreviations.......................................................... 25
Revision history ....................................................................... 26
STUSB4500L
Contents
DS13102 - Rev 6 page 28/31
```

### Page 29

#### Extracted tables

Table 1:

```text
| DS13102 - Rev 6 page 29/31 |
```

#### Raw extracted text

```text
STUSB4500L
List of tables
List of tables
Table 1. Pin function list . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
Table 2. Pin function descriptions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
Table 3. I2C interface pin list . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
Table 4. Source current capability. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
Table 5. GPIO pin configuration. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
Table 6. USB data MUX select. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
Table 7. VBUS_EN_SNK pin behavior depending on the operating conditions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
Table 8. Orientation and current capability detection in sink power role . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
Table 9. Device address format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
Table 10. Register address format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
Table 11. Register data format. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
Table 12. I2C timing parameters - VDD = 5 V. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
Table 13. STUSB4500L user-defined parameters and default settings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
Table 14. Absolute maximum ratings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
Table 15. Operating conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
Table 16. Electrical characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
Table 17. QFN-24 EP (4x4) package mechanical data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
Table 18. WLCSP (2.6x2.6x0.5) package mechanical data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
Table 19. Thermal information. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
Table 20. List of terms and abbreviations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
Table 21. Document revision history. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
DS13102 - Rev 6 page 29/31
```

### Page 30

#### Extracted tables

Table 1:

```text
| DS13102 - Rev 6 page 30/31 |
```

#### Raw extracted text

```text
STUSB4500L
List of figures
List of figures
Figure 1. Functional block diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
Figure 2. QFN-24 pin connections (top view) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
Figure 3. WLCSP-25 pin connections (top view). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
Figure 4. Short-to-V . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
BUS
Figure 5. Read operation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
Figure 6. Write operation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
Figure 7. I2C timing diagram. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
Figure 8. I2C register initialization sequence at power-up or after a reset. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
Figure 9. Implementation example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
Figure 10. QFN-24 EP (4x4) package information. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
Figure 11. QFN-24 EP (4x4) recommended footprint . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
Figure 12. WLCSP (2.6x2.6x0.5) package outline. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
Figure 13. WLCSP (2.6x2.6x0.5) recommended footprint . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
DS13102 - Rev 6 page 30/31
```

### Page 31

#### Extracted tables

Table 1:

```text
| DS13102 - Rev 6 page 31/31 |
```

#### Raw extracted text

```text
IMPORTANT NOTICE - PLEASE READ CAREFULLY
STMicroelectronics NV and its subsidiaries (ST) reserve the right to make changes, corrections, enhancements, modifications, and improvements to ST
products and/or to this document at any time without notice. Purchasers should obtain the latest relevant information on ST products before placing orders. ST
products are sold pursuant to STs terms and conditions of sale in place at the time of order acknowledgement.
Purchasers are solely responsible for the choice, selection, and use of ST products and ST assumes no liability for application assistance or the design of
Purchasers products.
No license, express or implied, to any intellectual property right is granted by ST herein.
Resale of ST products with provisions different from the information set forth herein shall void any warranty granted by ST for such product.
ST and the ST logo are trademarks of ST. For additional information about ST trademarks, please refer to www.st.com/trademarks. All other product or service
names are the property of their respective owners.
Information in this document supersedes and replaces information previously supplied in any prior versions of this document.
 2021 STMicroelectronics - All rights reserved
STUSB4500L
DS13102 - Rev 6 page 31/31
```
