# TPS2372 High-Power PoE PD Interface with Automatic MPS and Autoclass datasheet (Rev. B)

## Source

- Source PDF: [tps2372-datasheet.pdf](tps2372-datasheet.pdf)
- Generated Markdown: `tps2372-datasheet.md`
- Page count: 44
- Conversion method: automated local extraction with pypdf and pdfplumber

## Extracted title and part identity

- TPS2372 High-Power PoE PD Interface with Automatic MPS and Autoclass datasheet (Rev. B)
- tps2372 datasheet
- TPS2372
- IEEE802.
- TPS2372-4
- TPS2372-3
- SLUSCM4B
- TPS2372-2

## Extraction summary

- Pages with substantial text extraction: 44/44
- Pages with extracted tables: 28/44
- Total extracted character count: 110349
- Extraction quality flag: usable

## PDF metadata

| Field | Value |
| --- | --- |
| Title | TPS2372 High-Power PoE PD Interface with Automatic MPS and Autoclass datasheet (Rev. B) |
| Author | Texas Instruments, Incorporated [SLUSCM4,B ] |
| Subject | Data Sheet |
| Creator | TopLeaf 9.0.005 |
| Producer | iText 2.1.7 by 1T3XT |

## Reviewed summary

### Curated design notes

- PDF review confirmed this is the TI TPS2372 high-power PoE PD interface datasheet covering the TPS2372-2, TPS2372-3, and TPS2372-4 options in a
  20-pin VQFN package.
- Pin-function content that matters during design is clearer than the raw snippets imply: VDD is the positive PoE rail, DEN uses a 24.9 kOhm resistor
  to VDD for the detection signature, CLSA/CLSB use external resistors to set the two classification currents, REF requires a 49.9 kOhm 1% resistor to
  VSS, AMPS_CTL programs the automatic-MPS pulse amplitude, MPS_DUTY selects 5.4%, 8.1%, or 12.5% duty cycle, AUTCLS enables Autoclass when pulled low
  during classification, and the exposed pad must be tied to VSS.
- High-level operating points from the PDF are 60 W Type-3 operation for TPS2372-3, 90 W Type-4 operation for TPS2372-4, a 100 V hotswap MOSFET, 1.85
  A typical current limit for TPS2372-3, and 2.2 A typical current limit for TPS2372-4.
- The application section on page 28 explicitly requires a TVS across the rectified PoE input (D1), with SMAJ58A or equivalent recommended for general
  indoor applications. The same section discusses adapter ORing and the need to limit cable-inductance transients when an auxiliary adapter is
  present.
- Application/reference design content also includes automatic MPS for low-power standby, a PG delay to let the PSE complete inrush, and Autoclass
  support so the PSE can optimize power budgeting.
- Mechanical coverage is present in the VQFN package drawing and orderable-information pages at the end of the PDF.
- Extraction limit: Figure 22 and the ORing/lighting schematics are mostly figure-based, so the curated notes above capture the design-critical
  resistor values and protection requirements while the raw extraction remains available below.

## Design-relevant extracted content

This section surfaces design-relevant snippets first. Full page-by-page raw extraction follows later for local search.

### Part number and ordering information

- The Autoclass enable input also allows advanced / system power optimization modes compliant with / IEEE802.3bt (draft) standard. / Device Information(1) / PART NUMBER PACKAGE BODY SIZE (NOM) / TPS2372 VQFN (20) 5.00 mm x 5.00 mm / (1) For all available packages, see the orderable addendum at
- system power optimization modes compliant with / IEEE802.3bt (draft) standard. / Device Information(1) / PART NUMBER PACKAGE BODY SIZE (NOM) / TPS2372 VQFN (20) 5.00 mm x 5.00 mm / (1) For all available packages, see the orderable addendum at / the end of the data sheet.
- Device Information(1) / PART NUMBER PACKAGE BODY SIZE (NOM) / TPS2372 VQFN (20) 5.00 mm x 5.00 mm / (1) For all available packages, see the orderable addendum at / the end of the data sheet. / spacer / spacer
- 11.4 Trademarks ........................................................... 35 / 11.5 Electrostatic Discharge Caution ............................ 35 / 11.6 Glossary ................................................................ 36 / 12 Mechanical, Packaging, and Orderable / Information ........................................................... 36 / 4 Revision History / Changes from Revision A (February 2018) to Revision B Page
- 4 Revision History / Changes from Revision A (February 2018) to Revision B Page / * Added TableNote to Table 2 ............................................................................................................................................... 15 / * Added dashed box with optional on it in Figure 22 .............................................................................................................. 27 / * Added PSE and POE information to Opto-isolators for TPH, TPL and BT .......................................................................... 29 / Changes from Original (October 2017) to Revision A Page / * Changed TPS2372-2 typical current limit to 1.85 A ............................................................................................................... 1
- 7.4.1 PoE Overview / The following text is intended as an aid in understanding the operation of the TPS2372 but not as a substitute for / the IEEE 802.3bt standard. The pending IEEE 802.3bt standard is an update to IEEE 802.3-2012 clause 33 / (PoE), adding 4-pair power, high-power options, additional features and enhanced classification. Generally / speaking, a device compliant to IEEE 802.3-2012 is referred to as a Type 1 (Class 0-3) or 2 (Class 4) device, / and devices with higher power and enhanced classification will be referred to as Type 3 (Class 5,6) or 4 (Class / 7,8) devices. Type 3 devices will also include Class 0-4 devices that are 4-pair capable. Standards change and
- default, 13-W current-encoded class, or one of four other choices if Type 2, one of six other choices if Type 3, / and one of eight other choices if Type 4. DLL classification occurs after power-on and the Ethernet data link has / been established. / The Autoclass function is optional for both the PSE and the PD. / Once started, the PD must present a maintain power signature (MPS) to assure the PSE that it is still present. / The PSE monitors its output for a valid MPS, and turns the port off if it loses the MPS. Loss of the MPS returns / the PSE to the idle state. Figure 15 shows the operational states as a function of PD input voltage.
- 10. Must not draw more than 51 W if it has not received at least 5 classification events or received permission / through DLL. / 11. Must meet various operating and transient templates. / 12. Optionally monitor for the presence or absence of an adapter (assume high power). / As a result of these requirements, the PD must be able to dynamically control its loading, and monitor TPL and / TPH for changes. In cases where the design needs to know specifically if an adapter is plugged in and / operational, the adapter should be individually monitored, typically with an optocoupler.
- effective maximum PD power including the effective channel losses and additional margin. This new feature was / introduced in the IEEE802.3bt standard to allow a more efficient use of the available power since only the / effectively used power needs to be budgeted. / A Type 3 or Type 4 PD may optionally support Autoclass whereas a Type 3 or Type 4 PSE may make use of it to / optimize its power management. / A PSE implementing Autoclass uses the first class event to inquire if the PD supports Autoclass, looking for the / class current to fall to class 0 current level after a time tACS, as shown in Figure 17. If it is the case, the PSE can
- DC/DC EN / IRSHDL_EN / AUTCLS / Optional / CBULK / + / 27
- 8.2.2.2 Protection, D1 / A TVS, D1, across the rectified PoE voltage per Figure 22 must be used. TI recommends a SMAJ58A, or / equivalent, is recommended for general indoor applications. If an adapter is connected from VDD to RTN, as in / ORing option 2 above, then voltage transients caused by the input cable inductance ringing with the internal PD / capacitance can occur. Adequate capacitive filtering or a TVS must limit this voltage to within the absolute / maximum ratings. Outdoor transient levels or special applications require additional protection. / PARAMETER | TESTCONDITIONS | MIN | MAX | UNIT
- 11.6 Glossary / SLYZ022 - TI Glossary. / This glossary lists and explains terms, acronyms, and definitions. / 12 Mechanical, Packaging, and Orderable Information / The following pages include mechanical, packaging, and orderable information. This information is the most / current data available for the designated devices. This data is subject to change without notice and revision of / this document. For browser-based versions of this data sheet, refer to the left-hand navigation.
- SLYZ022 - TI Glossary. / This glossary lists and explains terms, acronyms, and definitions. / 12 Mechanical, Packaging, and Orderable Information / The following pages include mechanical, packaging, and orderable information. This information is the most / current data available for the designated devices. This data is subject to change without notice and revision of / this document. For browser-based versions of this data sheet, refer to the left-hand navigation. / www.ti.com
- VQFN - 1 mm max heightRGW0020B / PLASTIC QUAD FLATPACK - NO LEAD / 4222816/A 06/2016 / OPTION 01 (0.1) / DIMENSION A / OPTION 02 (0.2) / PIN 1 INDEX AREA
- 4222816/A 06/2016 / OPTION 01 (0.1) / DIMENSION A / OPTION 02 (0.2) / PIN 1 INDEX AREA / 0.08 / SEATING PLANE
- 11 / 15 / 6 10 / 20 16(OPTIONAL) / PIN 1 ID 0.1 C A B / 0.05 / EXPOSED
- Product Folder Links: TPS2372 / Submit Documentation FeedbackCopyright 2017-2018, Texas Instruments Incorporated / DIMENSION A | / OPTION 01 | (0.1) / OPTION 02 | (0.2) / | 0.08 / 21 |
- Submit Documentation FeedbackCopyright 2017-2018, Texas Instruments Incorporated / DIMENSION A | / OPTION 01 | (0.1) / OPTION 02 | (0.2) / | 0.08 / 21 | / | 0.1 | C | A | B

### Pin, pad, and terminal designations

- CAT5 cable, this translates into 71.3 W and 51 W at / PD input. / The TPS2372 operates with enhanced features. / The Automatic MPS function enables applications / requiring very low power standby modes. The / TPS2372 automatically generates the necessary / pulsed current to maintain the PSE power. An
- requiring very low power standby modes. The / TPS2372 automatically generates the necessary / pulsed current to maintain the PSE power. An / external resistor is used to enable this functionality / and to program the MPS pulsed current amplitude. / The TPS2372 also implements a delay function to / allow the remote PSE to complete its inrush phase
- pulsed current to maintain the PSE power. An / external resistor is used to enable this functionality / and to program the MPS pulsed current amplitude. / The TPS2372 also implements a delay function to / allow the remote PSE to complete its inrush phase / before releasing the Power Good (PG) output. This / ensures that the IEEE802.3bt (draft) startup
- 2 Applications ........................................................... 1 / 3 Description ............................................................. 1 / 4 Revision History..................................................... 2 / 5 Pin Configuration and Functions ......................... 3 / 6 Specifications......................................................... 4 / 6.1 Absolute Maximum Ratings ...................................... 4 / 6.2 ESD Ratings.............................................................. 4
- 6.6 Typical Characteristics .............................................. 9 / 7 Detailed Description ............................................ 12 / 7.1 Overview ................................................................. 12 / 7.2 Functional Block Diagram ....................................... 13 / 7.3 Feature Description................................................. 13 / 7.4 Device Functional Modes........................................ 17 / 8 Application and Implementation ........................ 27
- 7.1 Overview ................................................................. 12 / 7.2 Functional Block Diagram ....................................... 13 / 7.3 Feature Description................................................. 13 / 7.4 Device Functional Modes........................................ 17 / 8 Application and Implementation ........................ 27 / 8.1 Application Information............................................ 27 / 8.2 Typical Application .................................................. 27
- www.ti.com SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018 / Product Folder Links: TPS2372 / Submit Documentation FeedbackCopyright 2017-2018, Texas Instruments Incorporated / 5 Pin Configuration and Functions / RGW Package / 20-Pin VQFN / Top View
- Submit Documentation FeedbackCopyright 2017-2018, Texas Instruments Incorporated / 5 Pin Configuration and Functions / RGW Package / 20-Pin VQFN / Top View / Pin Functions / PIN
- RGW Package / 20-Pin VQFN / Top View / Pin Functions / PIN / I/O DESCRIPTION / NAME NO.
- 20-Pin VQFN / Top View / Pin Functions / PIN / I/O DESCRIPTION / NAME NO. / VDD 1 I Connect to positive PoE input power rail. Bypass with 0.1 uF to VSS.
- Top View / Pin Functions / PIN / I/O DESCRIPTION / NAME NO. / VDD 1 I Connect to positive PoE input power rail. Bypass with 0.1 uF to VSS. / DEN 2 I/O Connect a 24.9 kOhm resistor from DEN to VDD to provide the PoE detection signature. Pull DEN to VSS to
- I/O DESCRIPTION / NAME NO. / VDD 1 I Connect to positive PoE input power rail. Bypass with 0.1 uF to VSS. / DEN 2 I/O Connect a 24.9 kOhm resistor from DEN to VDD to provide the PoE detection signature. Pull DEN to VSS to / disable the pass MOSFET during powered operation. / CLSA 3 O Connect a resistor from CLSA to VSS to program the first classification current. / VSS 4, 5 - Connect to negative power rail derived from PoE source.
- REF 7 O Internal 1.5 V voltage reference. Connect a 49.9kOhm_1% resistor from REF to VSS. / AMPS_CTL 8 O Automatic MPS control. Connect a resistor with appropriate power rating (to support the MPS current) from / AMPS_CTL to VSS to program the MPS current amplitude. Leave AMPS_CTL open to disable the automatic / MPS function. / MPS_DUTY 9 I MPS duty cycle select input, referenced to VSS, internally driven by a precision current source with voltage / limited to less than ~5.5V. A resistor connected to VSS determines if the MPS duty cycle selected is either / 5.4% (open), 8.1% (~60.4 kOhm) or 12.5% (short).
- limited to less than ~5.5V. A resistor connected to VSS determines if the MPS duty cycle selected is either / 5.4% (open), 8.1% (~60.4 kOhm) or 12.5% (short). / AUTCLS 10 I Autoclass enable input. Internally pulled-up to 5.5 V internal rail during classification only, pulled down in other / circumstances to minimize consumption. Pull low (to VSS) to enable the Autoclass function during / classification. Leave open otherwise. / RTN 11, 12 - Drain of PoE pass MOSFET. Return line from the load to the controller. / PG 13 O Power Good output. Open-drain, active-high output referenced to RTN.
- TPH 18 O / BT 19 O Indicates that a PSE applying an IEEE802.3bt (Type 3 or 4) mutual identification scheme has been identified. / Open-drain, active-low output referenced to RTN. / NC 20 - No connect pin. Leave open. / Pad - - The exposed thermal pad must be connected to VSS. A large fill area is required to assist in heat dissipation. / 20 / 19
- BT 19 O Indicates that a PSE applying an IEEE802.3bt (Type 3 or 4) mutual identification scheme has been identified. / Open-drain, active-low output referenced to RTN. / NC 20 - No connect pin. Leave open. / Pad - - The exposed thermal pad must be connected to VSS. A large fill area is required to assist in heat dissipation. / 20 / 19 / 18
- 7 / 8 / 9 / PIN | | I/O | DESCRIPTION / NAME | NO. | | / VDD | 1 | I | ConnecttopositivePoEinputpowerrail.Bypasswith0.1uFtoVSS. / DEN | 2 | I/O | Connecta24.9kOhmresistorfromDENtoVDDtoprovidethePoEdetectionsignature.PullDENtoVSSto disablethepassMOSFETduringpoweredoperation.
- PIN | | I/O | DESCRIPTION / NAME | NO. | | / VDD | 1 | I | ConnecttopositivePoEinputpowerrail.Bypasswith0.1uFtoVSS. / DEN | 2 | I/O | Connecta24.9kOhmresistorfromDENtoVDDtoprovidethePoEdetectionsignature.PullDENtoVSSto disablethepassMOSFETduringpoweredoperation. / CLSA | 3 | O | ConnectaresistorfromCLSAtoVSStoprogramthefirstclassificationcurrent. / VSS | 4,5 | | ConnecttonegativepowerrailderivedfromPoEsource. / CLSB | 6 | O | ConnectaresistorfromCLSBtoVSStoprogramthesecondclassificationcurrent.

### Specifications, ratings, and operating conditions

- * Supports Power Levels for Type-4 ( TPS2372-4) / 90-W and Type-3 ( TPS2372-3) 60-W Operation / * Robust 100 V Hotswap MOSFET / TPS2372-4 (typ.): 0.1-Ohm, 2.2-A Current Limit / TPS2372-3 (typ.): 0.3-Ohm, 1.85-A Current Limit / * Allocated Power Indicator Outputs / * PG Output with Inrush Completion Delay
- 90-W and Type-3 ( TPS2372-3) 60-W Operation / * Robust 100 V Hotswap MOSFET / TPS2372-4 (typ.): 0.1-Ohm, 2.2-A Current Limit / TPS2372-3 (typ.): 0.3-Ohm, 1.85-A Current Limit / * Allocated Power Indicator Outputs / * PG Output with Inrush Completion Delay / Compliant to PSE Inrush
- The Automatic MPS function enables applications / requiring very low power standby modes. The / TPS2372 automatically generates the necessary / pulsed current to maintain the PSE power. An / external resistor is used to enable this functionality / and to program the MPS pulsed current amplitude. / The TPS2372 also implements a delay function to
- TPS2372 automatically generates the necessary / pulsed current to maintain the PSE power. An / external resistor is used to enable this functionality / and to program the MPS pulsed current amplitude. / The TPS2372 also implements a delay function to / allow the remote PSE to complete its inrush phase / before releasing the Power Good (PG) output. This
- 3 Description ............................................................. 1 / 4 Revision History..................................................... 2 / 5 Pin Configuration and Functions ......................... 3 / 6 Specifications......................................................... 4 / 6.1 Absolute Maximum Ratings ...................................... 4 / 6.2 ESD Ratings.............................................................. 4 / 6.3 Recommended Operating Conditions....................... 5
- 4 Revision History..................................................... 2 / 5 Pin Configuration and Functions ......................... 3 / 6 Specifications......................................................... 4 / 6.1 Absolute Maximum Ratings ...................................... 4 / 6.2 ESD Ratings.............................................................. 4 / 6.3 Recommended Operating Conditions....................... 5 / 6.4 Thermal Information .................................................. 5
- 5 Pin Configuration and Functions ......................... 3 / 6 Specifications......................................................... 4 / 6.1 Absolute Maximum Ratings ...................................... 4 / 6.2 ESD Ratings.............................................................. 4 / 6.3 Recommended Operating Conditions....................... 5 / 6.4 Thermal Information .................................................. 5 / 6.5 Electrical Characteristics........................................... 6
- 6 Specifications......................................................... 4 / 6.1 Absolute Maximum Ratings ...................................... 4 / 6.2 ESD Ratings.............................................................. 4 / 6.3 Recommended Operating Conditions....................... 5 / 6.4 Thermal Information .................................................. 5 / 6.5 Electrical Characteristics........................................... 6 / 6.6 Typical Characteristics .............................................. 9
- 6.1 Absolute Maximum Ratings ...................................... 4 / 6.2 ESD Ratings.............................................................. 4 / 6.3 Recommended Operating Conditions....................... 5 / 6.4 Thermal Information .................................................. 5 / 6.5 Electrical Characteristics........................................... 6 / 6.6 Typical Characteristics .............................................. 9 / 7 Detailed Description ............................................ 12
- 6.2 ESD Ratings.............................................................. 4 / 6.3 Recommended Operating Conditions....................... 5 / 6.4 Thermal Information .................................................. 5 / 6.5 Electrical Characteristics........................................... 6 / 6.6 Typical Characteristics .............................................. 9 / 7 Detailed Description ............................................ 12 / 7.1 Overview ................................................................. 12
- 10.1 Layout Guidelines ................................................. 32 / 10.2 Layout Example .................................................... 32 / 10.3 EMI Containment .................................................. 34 / 10.4 Thermal Considerations and OTSD...................... 35 / 10.5 ESD....................................................................... 35 / 11 Device and Documentation Support ................. 35 / 11.1 Documentation Support ........................................ 35
- * Added dashed box with optional on it in Figure 22 .............................................................................................................. 27 / * Added PSE and POE information to Opto-isolators for TPH, TPL and BT .......................................................................... 29 / Changes from Original (October 2017) to Revision A Page / * Changed TPS2372-2 typical current limit to 1.85 A ............................................................................................................... 1 / * Changed TPS2372-3 device to production data .................................................................................................................... 1 / * Deleted advance information table notes ............................................................................................................................... 1 / * Changed current limit nominal value to 1.85 and maximum value to 2.2 .............................................................................. 6
- * Changed TPS2372-2 typical current limit to 1.85 A ............................................................................................................... 1 / * Changed TPS2372-3 device to production data .................................................................................................................... 1 / * Deleted advance information table notes ............................................................................................................................... 1 / * Changed current limit nominal value to 1.85 and maximum value to 2.2 .............................................................................. 6 / * Changed minimum value of inrush termination to 65%.......................................................................................................... 6 / * Changed typical shutdown temperature to 158 deg C.................................................................................................................. 8 / * Added TPS2372-4 to the title of Figure 10 ........................................................................................................................... 10
- * Changed minimum value of inrush termination to 65%.......................................................................................................... 6 / * Changed typical shutdown temperature to 158 deg C.................................................................................................................. 8 / * Added TPS2372-4 to the title of Figure 10 ........................................................................................................................... 10 / * Changed "current limit is changed to 1.8 A" to "current limit is changed to 1.85 A" in Internal Pass MOSFET and / Inrush Delay Enable, IRSHDL_EN subsection..................................................................................................................... 15 / * Changed "~" to "approximately" and "1.8 A" to "1.85 A" in the Advanced Startup and Converter Operation / subsectionStartup and Converter Operation subsection ...................................................................................................... 24
- VDD 1 I Connect to positive PoE input power rail. Bypass with 0.1 uF to VSS. / DEN 2 I/O Connect a 24.9 kOhm resistor from DEN to VDD to provide the PoE detection signature. Pull DEN to VSS to / disable the pass MOSFET during powered operation. / CLSA 3 O Connect a resistor from CLSA to VSS to program the first classification current. / VSS 4, 5 - Connect to negative power rail derived from PoE source. / CLSB 6 O Connect a resistor from CLSB to VSS to program the second classification current. / REF 7 O Internal 1.5 V voltage reference. Connect a 49.9kOhm_1% resistor from REF to VSS.
- disable the pass MOSFET during powered operation. / CLSA 3 O Connect a resistor from CLSA to VSS to program the first classification current. / VSS 4, 5 - Connect to negative power rail derived from PoE source. / CLSB 6 O Connect a resistor from CLSB to VSS to program the second classification current. / REF 7 O Internal 1.5 V voltage reference. Connect a 49.9kOhm_1% resistor from REF to VSS. / AMPS_CTL 8 O Automatic MPS control. Connect a resistor with appropriate power rating (to support the MPS current) from / AMPS_CTL to VSS to program the MPS current amplitude. Leave AMPS_CTL open to disable the automatic
- CLSA 3 O Connect a resistor from CLSA to VSS to program the first classification current. / VSS 4, 5 - Connect to negative power rail derived from PoE source. / CLSB 6 O Connect a resistor from CLSB to VSS to program the second classification current. / REF 7 O Internal 1.5 V voltage reference. Connect a 49.9kOhm_1% resistor from REF to VSS. / AMPS_CTL 8 O Automatic MPS control. Connect a resistor with appropriate power rating (to support the MPS current) from / AMPS_CTL to VSS to program the MPS current amplitude. Leave AMPS_CTL open to disable the automatic / MPS function.
- VSS 4, 5 - Connect to negative power rail derived from PoE source. / CLSB 6 O Connect a resistor from CLSB to VSS to program the second classification current. / REF 7 O Internal 1.5 V voltage reference. Connect a 49.9kOhm_1% resistor from REF to VSS. / AMPS_CTL 8 O Automatic MPS control. Connect a resistor with appropriate power rating (to support the MPS current) from / AMPS_CTL to VSS to program the MPS current amplitude. Leave AMPS_CTL open to disable the automatic / MPS function. / MPS_DUTY 9 I MPS duty cycle select input, referenced to VSS, internally driven by a precision current source with voltage

### Dimensions, package, and mechanical information

- * Supports Autoclass Operation / * Supports PoE++ PSE / * -40 deg C to 125 deg C Junction Temperature Range / * 20-lead VQFN Package / 2 Applications / * IEEE 802.3bt (Draft) Compliant Devices / * Lighting
- system power optimization modes compliant with / IEEE802.3bt (draft) standard. / Device Information(1) / PART NUMBER PACKAGE BODY SIZE (NOM) / TPS2372 VQFN (20) 5.00 mm x 5.00 mm / (1) For all available packages, see the orderable addendum at / the end of the data sheet.
- Device Information(1) / PART NUMBER PACKAGE BODY SIZE (NOM) / TPS2372 VQFN (20) 5.00 mm x 5.00 mm / (1) For all available packages, see the orderable addendum at / the end of the data sheet. / spacer / spacer
- spacer / spacer / Simplified Schematic / PARTNUMBER | PACKAGE | BODYSIZE(NOM) / TPS2372 | VQFN(20) | 5.00mmx5.00mm / 2 / TPS2372
- 11.4 Trademarks ........................................................... 35 / 11.5 Electrostatic Discharge Caution ............................ 35 / 11.6 Glossary ................................................................ 36 / 12 Mechanical, Packaging, and Orderable / Information ........................................................... 36 / 4 Revision History / Changes from Revision A (February 2018) to Revision B Page
- Product Folder Links: TPS2372 / Submit Documentation FeedbackCopyright 2017-2018, Texas Instruments Incorporated / 5 Pin Configuration and Functions / RGW Package / 20-Pin VQFN / Top View / Pin Functions
- kOhm / REF (1) 48.9 49.9 50.9 / Junction temperature -40 125 deg C / (1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application / report. / 6.4 Thermal Information / THERMAL METRIC (1)
- will treat a Class 5 to 8 device like a Class 4 device, allotting 25.5W if it chooses to power the PD. A Class 4 PD / that receives a 2-event class, a Class 5 or 6 PD that receives a 4-event class, or a Class 7 or 8 PD that receives / a 5-event class, understands that the PSE has agreed to allocate the PD requested power. In the case where / there is power demotion, the PD may choose to not start, or to start while not drawing more power than initially / allocated, and request more power through the DLL after startup. The standard requires a Type 2, 3 or 4 PD to / indicate that it is underpowered if this occurs. Startup of a high-power PD at lower power than requested / implicitly requires some form of powering down sections of the application circuits.
- pairs and the voltage is measured across the resistor. Schottky diodes often have a higher reverse leakage / current than PN diodes, making this a harder requirement to meet. To compensate, use conservative design for / diode operating temperature, select lower-leakage devices where possible, and match leakage and temperatures / by using packaged bridges. / Schottky diode leakage currents and lower dynamic resistances can impact the detection signature. Setting / reasonable expectations for the temperature range over which the detection signature is accurate is the simplest / solution. Increasing RDET slightly may also help meet the requirement.
- 11.6 Glossary / SLYZ022 - TI Glossary. / This glossary lists and explains terms, acronyms, and definitions. / 12 Mechanical, Packaging, and Orderable Information / The following pages include mechanical, packaging, and orderable information. This information is the most / current data available for the designated devices. This data is subject to change without notice and revision of / this document. For browser-based versions of this data sheet, refer to the left-hand navigation.
- SLYZ022 - TI Glossary. / This glossary lists and explains terms, acronyms, and definitions. / 12 Mechanical, Packaging, and Orderable Information / The following pages include mechanical, packaging, and orderable information. This information is the most / current data available for the designated devices. This data is subject to change without notice and revision of / this document. For browser-based versions of this data sheet, refer to the left-hand navigation. / www.ti.com
- current data available for the designated devices. This data is subject to change without notice and revision of / this document. For browser-based versions of this data sheet, refer to the left-hand navigation. / www.ti.com / PACKAGE OUTLINE / C / 20X 0.38 / 0.23
- PLASTIC QUAD FLATPACK - NO LEAD / 4222816/A 06/2016 / OPTION 01 (0.1) / DIMENSION A / OPTION 02 (0.2) / PIN 1 INDEX AREA / 0.08
- THERMAL PAD / 21 / NOTES: / 1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing / per ASME Y14.5M. / 2. This drawing is subject to change without notice. / 3. The package thermal pad must be soldered to the printed circuit board for thermal and mechanical performance.
- NOTES: / 1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing / per ASME Y14.5M. / 2. This drawing is subject to change without notice. / 3. The package thermal pad must be soldered to the printed circuit board for thermal and mechanical performance. / SCALE 3.000 / 37
- 1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing / per ASME Y14.5M. / 2. This drawing is subject to change without notice. / 3. The package thermal pad must be soldered to the printed circuit board for thermal and mechanical performance. / SCALE 3.000 / 37 / TPS2372
- www.ti.com SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018 / Product Folder Links: TPS2372 / Submit Documentation FeedbackCopyright 2017-2018, Texas Instruments Incorporated / DIMENSION A | / OPTION 01 | (0.1) / OPTION 02 | (0.2) / | 0.08
- 15 / 1620 / SYMM / LAND PATTERN EXAMPLE / SCALE:15X / 21 / NOTES: (continued)

### Formulas, equations, and configuration calculations

- 1* IEEE 802.3bt (Draft) PD Solution for Type 3 or / Type 4 PoE / * Supports Power Levels for Type-4 ( TPS2372-4) / 90-W and Type-3 ( TPS2372-3) 60-W Operation / * Robust 100 V Hotswap MOSFET / TPS2372-4 (typ.): 0.1-Ohm, 2.2-A Current Limit / TPS2372-3 (typ.): 0.3-Ohm, 1.85-A Current Limit
- * Supports Power Levels for Type-4 ( TPS2372-4) / 90-W and Type-3 ( TPS2372-3) 60-W Operation / * Robust 100 V Hotswap MOSFET / TPS2372-4 (typ.): 0.1-Ohm, 2.2-A Current Limit / TPS2372-3 (typ.): 0.3-Ohm, 1.85-A Current Limit / * Allocated Power Indicator Outputs / * PG Output with Inrush Completion Delay
- 90-W and Type-3 ( TPS2372-3) 60-W Operation / * Robust 100 V Hotswap MOSFET / TPS2372-4 (typ.): 0.1-Ohm, 2.2-A Current Limit / TPS2372-3 (typ.): 0.3-Ohm, 1.85-A Current Limit / * Allocated Power Indicator Outputs / * PG Output with Inrush Completion Delay / Compliant to PSE Inrush
- * Automatic Maintain Power Signature (MPS) / Auto-adjust MPS for Type 1-2 or 3-4 PSE / Supports Ultra-Low Power Standby Modes / * Supports Autoclass Operation / * Supports PoE++ PSE / * -40 deg C to 125 deg C Junction Temperature Range / * 20-lead VQFN Package
- 2 Applications ........................................................... 1 / 3 Description ............................................................. 1 / 4 Revision History..................................................... 2 / 5 Pin Configuration and Functions ......................... 3 / 6 Specifications......................................................... 4 / 6.1 Absolute Maximum Ratings ...................................... 4 / 6.2 ESD Ratings.............................................................. 4
- 10.1 Layout Guidelines ................................................. 32 / 10.2 Layout Example .................................................... 32 / 10.3 EMI Containment .................................................. 34 / 10.4 Thermal Considerations and OTSD...................... 35 / 10.5 ESD....................................................................... 35 / 11 Device and Documentation Support ................. 35 / 11.1 Documentation Support ........................................ 35
- * Added dashed box with optional on it in Figure 22 .............................................................................................................. 27 / * Added PSE and POE information to Opto-isolators for TPH, TPL and BT .......................................................................... 29 / Changes from Original (October 2017) to Revision A Page / * Changed TPS2372-2 typical current limit to 1.85 A ............................................................................................................... 1 / * Changed TPS2372-3 device to production data .................................................................................................................... 1 / * Deleted advance information table notes ............................................................................................................................... 1 / * Changed current limit nominal value to 1.85 and maximum value to 2.2 .............................................................................. 6
- * Changed TPS2372-2 typical current limit to 1.85 A ............................................................................................................... 1 / * Changed TPS2372-3 device to production data .................................................................................................................... 1 / * Deleted advance information table notes ............................................................................................................................... 1 / * Changed current limit nominal value to 1.85 and maximum value to 2.2 .............................................................................. 6 / * Changed minimum value of inrush termination to 65%.......................................................................................................... 6 / * Changed typical shutdown temperature to 158 deg C.................................................................................................................. 8 / * Added TPS2372-4 to the title of Figure 10 ........................................................................................................................... 10
- * Changed minimum value of inrush termination to 65%.......................................................................................................... 6 / * Changed typical shutdown temperature to 158 deg C.................................................................................................................. 8 / * Added TPS2372-4 to the title of Figure 10 ........................................................................................................................... 10 / * Changed "current limit is changed to 1.8 A" to "current limit is changed to 1.85 A" in Internal Pass MOSFET and / Inrush Delay Enable, IRSHDL_EN subsection..................................................................................................................... 15 / * Changed "~" to "approximately" and "1.8 A" to "1.85 A" in the Advanced Startup and Converter Operation / subsectionStartup and Converter Operation subsection ...................................................................................................... 24
- * Added TPS2372-4 to the title of Figure 10 ........................................................................................................................... 10 / * Changed "current limit is changed to 1.8 A" to "current limit is changed to 1.85 A" in Internal Pass MOSFET and / Inrush Delay Enable, IRSHDL_EN subsection..................................................................................................................... 15 / * Changed "~" to "approximately" and "1.8 A" to "1.85 A" in the Advanced Startup and Converter Operation / subsectionStartup and Converter Operation subsection ...................................................................................................... 24 / * Changed equation 3 and equation 4 values in Automatic MPS and MPS Duty Cycle, RMPS and RMPS_DUTY....................... 30 / * Changed TPS2372-3RGWR and TPS2372-3RGWT devices to ACTIVE............................................................................ 36
- * Changed "current limit is changed to 1.8 A" to "current limit is changed to 1.85 A" in Internal Pass MOSFET and / Inrush Delay Enable, IRSHDL_EN subsection..................................................................................................................... 15 / * Changed "~" to "approximately" and "1.8 A" to "1.85 A" in the Advanced Startup and Converter Operation / subsectionStartup and Converter Operation subsection ...................................................................................................... 24 / * Changed equation 3 and equation 4 values in Automatic MPS and MPS Duty Cycle, RMPS and RMPS_DUTY....................... 30 / * Changed TPS2372-3RGWR and TPS2372-3RGWT devices to ACTIVE............................................................................ 36 / 17
- Inrush Delay Enable, IRSHDL_EN subsection..................................................................................................................... 15 / * Changed "~" to "approximately" and "1.8 A" to "1.85 A" in the Advanced Startup and Converter Operation / subsectionStartup and Converter Operation subsection ...................................................................................................... 24 / * Changed equation 3 and equation 4 values in Automatic MPS and MPS Duty Cycle, RMPS and RMPS_DUTY....................... 30 / * Changed TPS2372-3RGWR and TPS2372-3RGWT devices to ACTIVE............................................................................ 36 / 17 / 18
- www.ti.com SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018 / Product Folder Links: TPS2372 / Submit Documentation FeedbackCopyright 2017-2018, Texas Instruments Incorporated / 5 Pin Configuration and Functions / RGW Package / 20-Pin VQFN / Top View
- NAME NO. / VDD 1 I Connect to positive PoE input power rail. Bypass with 0.1 uF to VSS. / DEN 2 I/O Connect a 24.9 kOhm resistor from DEN to VDD to provide the PoE detection signature. Pull DEN to VSS to / disable the pass MOSFET during powered operation. / CLSA 3 O Connect a resistor from CLSA to VSS to program the first classification current. / VSS 4, 5 - Connect to negative power rail derived from PoE source. / CLSB 6 O Connect a resistor from CLSB to VSS to program the second classification current.
- PIN | | I/O | DESCRIPTION / NAME | NO. | | / VDD | 1 | I | ConnecttopositivePoEinputpowerrail.Bypasswith0.1uFtoVSS. / DEN | 2 | I/O | Connecta24.9kOhmresistorfromDENtoVDDtoprovidethePoEdetectionsignature.PullDENtoVSSto disablethepassMOSFETduringpoweredoperation. / CLSA | 3 | O | ConnectaresistorfromCLSAtoVSStoprogramthefirstclassificationcurrent. / VSS | 4,5 | | ConnecttonegativepowerrailderivedfromPoEsource. / CLSB | 6 | O | ConnectaresistorfromCLSBtoVSStoprogramthesecondclassificationcurrent.
- Product Folder Links: TPS2372 / Submit Documentation Feedback Copyright 2017-2018, Texas Instruments Incorporated / (1) Stresses beyond those listed under Absolute Maximum Ratings may cause permanent damage to the device. These are stress ratings / only, which do not imply functional operation of the device at these or any other conditions beyond those indicated under Recommended / Operating Conditions. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability. / (2) With I(RTN) = 0 / (3) Do not apply voltages to these pins
- VMSR Mark reset threshold VVDD falling 3 3.9 5 V / Mark state resistance 2-point measurement at 5 V and 10.1 V 6 10 12 kOhm / Leakage current VVDD = 57 V, VCLS = 0 V, measure ICLS 1 uA / tLCF_PD Long first class event timing Class 1st event time duration for new MPS 76 81.5 86 ms / tACS Autoclass signature timing AUTCLS During Class 1st event 76 81.5 87 ms / AUTCLS pullup current 13 V <= VVDD <= 21 V 30 34 38 uA / PASS DEVICE (RTN)
- RTN leakage current VVDD = VRTN = 100 V, VDEN = VVSS , measure / IRTN / 80 / Current limit / VRTN = 1.5 V TPS2372-3 1.55 1.85 2.2 / A / VRTN = 1.5 V TPS2372-4 1.9 2.2 2.5

### Reference designs, applications, and examples

- Software / Support & / Community / An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications, / intellectual property matters and other important disclaimers. PRODUCTION DATA. / TPS2372 / SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018
- * Supports PoE++ PSE / * -40 deg C to 125 deg C Junction Temperature Range / * 20-lead VQFN Package / 2 Applications / * IEEE 802.3bt (Draft) Compliant Devices / * Lighting / * Power Modules
- implement an IEEE802.3at or IEEE802.3bt (draft) / (Type 1-4) powered device (PD). The low internal / switch resistance allows the TPS2372-4 and / TPS2372-3 to support high power applications up to / 90 W and 60 W respectively. Assuming 100-meter / CAT5 cable, this translates into 71.3 W and 51 W at / PD input.
- CAT5 cable, this translates into 71.3 W and 51 W at / PD input. / The TPS2372 operates with enhanced features. / The Automatic MPS function enables applications / requiring very low power standby modes. The / TPS2372 automatically generates the necessary / pulsed current to maintain the PSE power. An
- the end of the data sheet. / spacer / spacer / Simplified Schematic / PARTNUMBER | PACKAGE | BODYSIZE(NOM) / TPS2372 | VQFN(20) | 5.00mmx5.00mm / 2
- Submit Documentation Feedback Copyright 2017-2018, Texas Instruments Incorporated / Table of Contents / 1 Features .................................................................. 1 / 2 Applications ........................................................... 1 / 3 Description ............................................................. 1 / 4 Revision History..................................................... 2 / 5 Pin Configuration and Functions ......................... 3
- 7.2 Functional Block Diagram ....................................... 13 / 7.3 Feature Description................................................. 13 / 7.4 Device Functional Modes........................................ 17 / 8 Application and Implementation ........................ 27 / 8.1 Application Information............................................ 27 / 8.2 Typical Application .................................................. 27 / 9 Power Supply Recommendations ...................... 32
- 7.3 Feature Description................................................. 13 / 7.4 Device Functional Modes........................................ 17 / 8 Application and Implementation ........................ 27 / 8.1 Application Information............................................ 27 / 8.2 Typical Application .................................................. 27 / 9 Power Supply Recommendations ...................... 32 / 10 Layout................................................................... 32
- 7.4 Device Functional Modes........................................ 17 / 8 Application and Implementation ........................ 27 / 8.1 Application Information............................................ 27 / 8.2 Typical Application .................................................. 27 / 9 Power Supply Recommendations ...................... 32 / 10 Layout................................................................... 32 / 10.1 Layout Guidelines ................................................. 32
- 9 Power Supply Recommendations ...................... 32 / 10 Layout................................................................... 32 / 10.1 Layout Guidelines ................................................. 32 / 10.2 Layout Example .................................................... 32 / 10.3 EMI Containment .................................................. 34 / 10.4 Thermal Considerations and OTSD...................... 35 / 10.5 ESD....................................................................... 35
- Tstg Storage temperature -65 150 deg C / (1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process. / (2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process. / (3) Discharges applied to circuit of Figure 22 between RJ-45, adapter, and output voltage rails, on TPS2372- 4EVM-006 Evaluation Module. / 6.2 ESD Ratings / VALUE UNIT / V(ESD) Electrostatic discharge
- kOhm / REF (1) 48.9 49.9 50.9 / Junction temperature -40 125 deg C / (1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application / report. / 6.4 Thermal Information / THERMAL METRIC (1)
- interface IEEE802.3bt Type-3 ( TPS2372-3) and Type-4 ( TPS2372-4) powered device (PD). Basic functionality / supported includes Detection, Hardware Classification, and inrush current limit (200-mA for TPS2372-3 and 335 / mA for TPS2372-4) during startup. Enhanced features include the automatic maintain power signature (MPS). / The TPS2372-3 integrates a low 0.3-Ohm internal switch to support Type-3 applications up to 60 W of continuous / power sourced by the PSE, allowing beyond 1.2 A (1.55 A minimum current limit) through the PD during normal / operation. / Likewise, the TPS2372-4 integrates a low 0.1-Ohm internal switch to support Type-4 applications up to 90 W of
- The TPS2372-3 integrates a low 0.3-Ohm internal switch to support Type-3 applications up to 60 W of continuous / power sourced by the PSE, allowing beyond 1.2 A (1.55 A minimum current limit) through the PD during normal / operation. / Likewise, the TPS2372-4 integrates a low 0.1-Ohm internal switch to support Type-4 applications up to 90 W of / continuous power sourced by the PSE, allowing up to 1.9 A through the PD during normal operation. / The TPS2372 has a built-in inrush time delay period, for a simple solution to meet the IEEE802.3bt startup / requirement.
- impedance state at all other times. This pin is an open-drain output, and it may require a pullup resistor or other / interface to the downstream load. PG may be left open if it is not used. / The PG pin can be used to inhibit downstream converter startup by keeping the soft-start pin low. Figure 14 / shows an example where PG connects to the SS pin of a DC-DC controller. Because PG is an open drain / output, it will not affect the soft-start capacitor charge time when it deasserts. Another common use of the PG pin / is to enable a converter with an active-high enable input. In this case, PG may require a pullup resistor to either / VDD, or to a bias supply, depending on the requirements of the controller enable pin.
- Product Folder Links: TPS2372 / Submit Documentation FeedbackCopyright 2017-2018, Texas Instruments Incorporated / (1) The BT output is not required to indicate how much power is allocated to the PD by a IEEE802.3bt compliant PSE. Additional / information may be provided depending on the application described in the Application Detailed Design Requirements section Opto / isolators for TPH, TPL and BT / The AUTCLS input is used to enable the Autoclass function during classification. When enabled, the class / signature during the first class event drops to class 0 current level after a time tACS of the first class event,
- recommends a resistor of 24.9 kOhm +/- 1% for RDEN. / Pulling DEN to VSS during powered operation causes the internal hotswap MOSFET and class regulator to turn / off. If the resistance connected between VDD and DEN is divided into two roughly equal portions, then the / application circuit can disable the PD by grounding the tap point between the two resistances, while / simultaneously spoiling the detection signature which prevents the PD from properly re-detecting. / 7.3.4 Internal Pass MOSFET and Inrush Delay Enable, IRSHDL_EN / RTN pin provides the negative power return path for the load. Once VVDD exceeds the UVLO threshold, the
- 3-4 6 4 51 LOW HIGH LOW / 4 7 5 62 LOW LOW LOW / 4 8 5 71 LOW LOW LOW / Table 3. Power Demotion Cases / PSE Type PD Class NUMBER OF / CLASS CYCLES / PSE

## Page-by-page extracted content

### Page 1

#### Extracted tables

Table 1:

```text
PARTNUMBER | PACKAGE | BODYSIZE(NOM)
TPS2372 | VQFN(20) | 5.00mmx5.00mm
```

#### Raw extracted text

```text
RTN
RCLSA
From Ethernet
Transformers
VDD
VSS
CLSA
From Spare Pairs
or Transformers
DEN
PG
TPL
AUTCLS
TPS2372
RCLSB
CLSB
AMPS_CTL
TPH
SS
I_in
MPS
Control
REF
LED Lighting
ControlI_in
MPS pulses
MPS pulses automatically generated if I_in is too low
BT
0.1 F
58V
RDET
RREF
RMPS
CBULK
+
MPS_DUTY
RMPS_DUTY
OUT+
IN
LEDs
OUT-
MCU
+
PHY
Light Level/
Sleep/Wake
control
IRSHDL_EN
Low Pwr
DC/DC OUT VCC
Sensor
Product
Folder
Order
Now
T echnical
Documents
Tools &
Software
Support &
Community
An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications,
intellectual property matters and other important disclaimers. PRODUCTION DATA.
TPS2372
SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018
TPS2372High-PowerPoEPDInterfacewithAutomaticMPSandAutoclass
1
1 Features
1* IEEE 802.3bt (Draft) PD Solution for Type 3 or
Type 4 PoE
* Supports Power Levels for Type-4 ( TPS2372-4)
90-W and Type-3 ( TPS2372-3) 60-W Operation
* Robust 100 V Hotswap MOSFET
- TPS2372-4 (typ.): 0.1-Ohm, 2.2-A Current Limit
- TPS2372-3 (typ.): 0.3-Ohm, 1.85-A Current Limit
* Allocated Power Indicator Outputs
* PG Output with Inrush Completion Delay
- Compliant to PSE Inrush
* Automatic Maintain Power Signature (MPS)
- Auto-adjust MPS for Type 1-2 or 3-4 PSE
- Supports Ultra-Low Power Standby Modes
* Supports Autoclass Operation
* Supports PoE++ PSE
* -40 deg C to 125 deg C Junction Temperature Range
* 20-lead VQFN Package
2 Applications
* IEEE 802.3bt (Draft) Compliant Devices
* Lighting
* Power Modules
* Dual Signature PD/Forced UPOE
* 4PPOE
* Pass-through System
* Security Cameras
* Multiband access points
* Pico-base Stations
3 Description
The TPS2372 contains all of the features needed to
implement an IEEE802.3at or IEEE802.3bt (draft)
(Type 1-4) powered device (PD). The low internal
switch resistance allows the TPS2372-4 and
TPS2372-3 to support high power applications up to
90 W and 60 W respectively. Assuming 100-meter
CAT5 cable, this translates into 71.3 W and 51 W at
PD input.
The TPS2372 operates with enhanced features.
The Automatic MPS function enables applications
requiring very low power standby modes. The
TPS2372 automatically generates the necessary
pulsed current to maintain the PSE power. An
external resistor is used to enable this functionality
and to program the MPS pulsed current amplitude.
The TPS2372 also implements a delay function to
allow the remote PSE to complete its inrush phase
before releasing the Power Good (PG) output. This
ensures that the IEEE802.3bt (draft) startup
requirements are met.
The Autoclass enable input also allows advanced
system power optimization modes compliant with
IEEE802.3bt (draft) standard.
Device Information(1)
PART NUMBER PACKAGE BODY SIZE (NOM)
TPS2372 VQFN (20) 5.00 mm x 5.00 mm
(1) For all available packages, see the orderable addendum at
the end of the data sheet.
spacer
spacer
Simplified Schematic
```

### Page 2

#### Raw extracted text

```text
2
TPS2372
SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018 www.ti.com
Product Folder Links: TPS2372
Submit Documentation Feedback Copyright  2017-2018, Texas Instruments Incorporated
Table of Contents
1 Features .................................................................. 1
2 Applications ........................................................... 1
3 Description ............................................................. 1
4 Revision History..................................................... 2
5 Pin Configuration and Functions ......................... 3
6 Specifications......................................................... 4
6.1 Absolute Maximum Ratings ...................................... 4
6.2 ESD Ratings.............................................................. 4
6.3 Recommended Operating Conditions....................... 5
6.4 Thermal Information .................................................. 5
6.5 Electrical Characteristics........................................... 6
6.6 Typical Characteristics .............................................. 9
7 Detailed Description ............................................ 12
7.1 Overview ................................................................. 12
7.2 Functional Block Diagram ....................................... 13
7.3 Feature Description................................................. 13
7.4 Device Functional Modes........................................ 17
8 Application and Implementation ........................ 27
8.1 Application Information............................................ 27
8.2 Typical Application .................................................. 27
9 Power Supply Recommendations ...................... 32
10 Layout................................................................... 32
10.1 Layout Guidelines ................................................. 32
10.2 Layout Example .................................................... 32
10.3 EMI Containment .................................................. 34
10.4 Thermal Considerations and OTSD...................... 35
10.5 ESD....................................................................... 35
11 Device and Documentation Support ................. 35
11.1 Documentation Support ........................................ 35
11.2 Receiving Notification of Documentation Updates 35
11.3 Community Resources.......................................... 35
11.4 Trademarks ........................................................... 35
11.5 Electrostatic Discharge Caution ............................ 35
11.6 Glossary ................................................................ 36
12 Mechanical, Packaging, and Orderable
Information ........................................................... 36
4 Revision History
Changes from Revision A (February 2018) to Revision B Page
* Added TableNote to Table 2 ............................................................................................................................................... 15
* Added dashed box with optional on it in Figure 22 .............................................................................................................. 27
* Added PSE and POE information to Opto-isolators for TPH, TPL and BT .......................................................................... 29
Changes from Original (October 2017) to Revision A Page
* Changed TPS2372-2 typical current limit to 1.85 A ............................................................................................................... 1
* Changed TPS2372-3 device to production data .................................................................................................................... 1
* Deleted advance information table notes ............................................................................................................................... 1
* Changed current limit nominal value to 1.85 and maximum value to 2.2 .............................................................................. 6
* Changed minimum value of inrush termination to 65%.......................................................................................................... 6
* Changed typical shutdown temperature to 158 deg C.................................................................................................................. 8
* Added TPS2372-4 to the title of Figure 10 ........................................................................................................................... 10
* Changed "current limit is changed to 1.8 A" to "current limit is changed to 1.85 A" in Internal Pass MOSFET and
Inrush Delay Enable, IRSHDL_EN subsection..................................................................................................................... 15
* Changed "~" to "approximately" and "1.8 A" to "1.85 A" in the Advanced Startup and Converter Operation
subsectionStartup and Converter Operation subsection ...................................................................................................... 24
* Changed equation 3 and equation 4 values in Automatic MPS and MPS Duty Cycle, RMPS and RMPS_DUTY....................... 30
* Changed TPS2372-3RGWR and TPS2372-3RGWT devices to ACTIVE............................................................................ 36
```

### Page 3

#### Extracted tables

Table 1:

```text
20
```

Table 2:

```text
19
```

Table 3:

```text
18
```

Table 4:

```text
17
```

Table 5:

```text
1 |
```

Table 6:

```text
| 15
```

Table 7:

```text
2 |
```

Table 8:

```text
| 14
```

Table 9:

```text
3 |
```

Table 10:

```text
| 13
```

Table 11:

```text
4 |
```

Table 12:

```text
| 12
```

Table 13:

```text
5 |
```

Table 14:

```text
| 11
```

Table 15:

```text
6
```

Table 16:

```text
7
```

Table 17:

```text
8
```

Table 18:

```text
9
```

Table 19:

```text
PIN |  | I/O | DESCRIPTION
NAME | NO. |  | 
VDD | 1 | I | ConnecttopositivePoEinputpowerrail.Bypasswith0.1uFtoVSS.
DEN | 2 | I/O | Connecta24.9kOhmresistorfromDENtoVDDtoprovidethePoEdetectionsignature.PullDENtoVSSto disablethepassMOSFETduringpoweredoperation.
CLSA | 3 | O | ConnectaresistorfromCLSAtoVSStoprogramthefirstclassificationcurrent.
VSS | 4,5 |  | ConnecttonegativepowerrailderivedfromPoEsource.
CLSB | 6 | O | ConnectaresistorfromCLSBtoVSStoprogramthesecondclassificationcurrent.
REF | 7 | O | Internal1.5Vvoltagereference.Connecta49.9kOhm_1%resistorfromREFtoVSS.
AMPS_CTL | 8 | O | AutomaticMPScontrol.Connectaresistorwithappropriatepowerrating(tosupporttheMPScurrent)from AMPS_CTLtoVSStoprogramtheMPScurrentamplitude.LeaveAMPS_CTLopentodisabletheautomatic MPSfunction.
MPS_DUTY | 9 | I | MPSdutycycleselectinput,referencedtoVSS,internallydrivenbyaprecisioncurrentsourcewithvoltage limitedtolessthan~5.5V.AresistorconnectedtoVSSdeterminesiftheMPSdutycycleselectediseither 5.4%(open),8.1%(~60.4kOhm)or12.5%(short).
AUTCLS | 10 | I | Autoclassenableinput.Internallypulled-upto5.5Vinternalrailduringclassificationonly,pulleddowninother circumstancestominimizeconsumption.Pulllow(toVSS)toenabletheAutoclassfunctionduring classification.Leaveopenotherwise.
RTN | 11,12 |  | DrainofPoEpassMOSFET.Returnlinefromtheloadtothecontroller.
PG | 13 | O | PowerGoodoutput.Open-drain,active-highoutputreferencedtoRTN.
NC | 14,15 |  | Noconnect
IRSHDL_E N | 16 | I | PSEinrushdelay(~81.5ms)enable,referencedtoRTN,internallypulled-upto5.5Vinternalrail.Leaveopen toenabletheinrushdelay.
TPL | 17 | O | PSEallocatedpoweroutputs,binarycoded.Open-drain,active-lowoutputsreferencedtoRTN.
TPH | 18 | O | 
BT | 19 | O | IndicatesthataPSEapplyinganIEEE802.3bt(Type3or4)mutualidentificationschemehasbeenidentified. Open-drain,active-lowoutputreferencedtoRTN.
NC | 20 |  | Noconnectpin.Leaveopen.
Pad |  |  | TheexposedthermalpadmustbeconnectedtoVSS.Alargefillareaisrequiredtoassistinheatdissipation.
```

#### Raw extracted text

```text
17
18
19
20
TPH
CLSB
BT
1
2
3
4
DEN
CLSA
NC
15
14
13
12
VSS
AMPS_CTL
RTN
PG
9
8
7
6
IRSHDL_EN
MPS_DUTY
VSS
NC
TPL
5
VDD
16
NC
11 RTN
10
REF
AUTCLS
3
TPS2372
www.ti.com SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018
Product Folder Links: TPS2372
Submit Documentation FeedbackCopyright  2017-2018, Texas Instruments Incorporated
5 Pin Configuration and Functions
RGW Package
20-Pin VQFN
Top View
Pin Functions
PIN
I/O DESCRIPTION
NAME NO.
VDD 1 I Connect to positive PoE input power rail. Bypass with 0.1 uF to VSS.
DEN 2 I/O Connect a 24.9 kOhm resistor from DEN to VDD to provide the PoE detection signature. Pull DEN to VSS to
disable the pass MOSFET during powered operation.
CLSA 3 O Connect a resistor from CLSA to VSS to program the first classification current.
VSS 4, 5 - Connect to negative power rail derived from PoE source.
CLSB 6 O Connect a resistor from CLSB to VSS to program the second classification current.
REF 7 O Internal 1.5 V voltage reference. Connect a 49.9kOhm_1% resistor from REF to VSS.
AMPS_CTL 8 O Automatic MPS control. Connect a resistor with appropriate power rating (to support the MPS current) from
AMPS_CTL to VSS to program the MPS current amplitude. Leave AMPS_CTL open to disable the automatic
MPS function.
MPS_DUTY 9 I MPS duty cycle select input, referenced to VSS, internally driven by a precision current source with voltage
limited to less than ~5.5V. A resistor connected to VSS determines if the MPS duty cycle selected is either
5.4% (open), 8.1% (~60.4 kOhm) or 12.5% (short).
AUTCLS 10 I Autoclass enable input. Internally pulled-up to 5.5 V internal rail during classification only, pulled down in other
circumstances to minimize consumption. Pull low (to VSS) to enable the Autoclass function during
classification. Leave open otherwise.
RTN 11, 12 - Drain of PoE pass MOSFET. Return line from the load to the controller.
PG 13 O Power Good output. Open-drain, active-high output referenced to RTN.
NC 14, 15 - No connect
IRSHDL_E
N
16 I PSE inrush delay (~81.5 ms) enable, referenced to RTN, internally pulled-up to 5.5 V internal rail. Leave open
to enable the inrush delay.
TPL 17 O PSE allocated power outputs, binary coded. Open-drain, active-low outputs referenced to RTN.
TPH 18 O
BT 19 O Indicates that a PSE applying an IEEE802.3bt (Type 3 or 4) mutual identification scheme has been identified.
Open-drain, active-low output referenced to RTN.
NC 20 - No connect pin. Leave open.
Pad - - The exposed thermal pad must be connected to VSS. A large fill area is required to assist in heat dissipation.
```

### Page 4

#### Extracted tables

Table 1:

```text
|  | MIN | MAX | UNIT
Inputvoltage | VDD,DEN | 0.3 100 |  | V
 | RTN(2) | 0.6 100 |  | 
 | IRSHDL_ENtoRTN | 0.3 6.5 |  | 
 | AUTCLS | 0.3 6.5 |  | 
Outputvoltage | CLSA,CLSB,REF,MPS_DUTY(3) | 0.3 6.5 |  | V
 | AMPS_CTL(3) | 0.3 30 |  | 
Voltage | PGtoRTN | 0.3 100 |  | V
 | TPH,TPL,BTtoRTN | 0.3 100 |  | 
Sinkingcurrent | RTN(4) | Internallylimited |  | mA
 | PG,TPH,TPL,BT | 10 |  | 
 | DEN | 1 |  | 
Sourcingcurrent | CLSA,CLSB | 65 |  | mA
 | REF | Internallylimited |  | 
 | AMPS_CTL | 50 |  | 
T J(max) | Maximumjunctiontemperature | Internallylimited |  | deg C
T stg | Storagetemperature | 65 150 |  | deg C
```

Table 2:

```text
|  |  |  | VALUE | UNIT
V Electrostaticdischarge (ESD) |  | Humanbodymodel(HBM),perANSI/ESDA/JEDECJS-001,allpins(1) | +/-2000 |  | V
 |  | Chargeddevicemodel(CDM),perJEDECspecificationJESD22-C101,all pins(2) | +/-500 |  | 
 |  | IEC61000-4-2contactdischarge(3) | +/-8000 |  | 
 |  | IEC61000-4-2air-gapdischarge(3) | +/-15000 |  |
```

#### Raw extracted text

```text
4
TPS2372
SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018 www.ti.com
Product Folder Links: TPS2372
Submit Documentation Feedback Copyright  2017-2018, Texas Instruments Incorporated
(1) Stresses beyond those listed under Absolute Maximum Ratings may cause permanent damage to the device. These are stress ratings
only, which do not imply functional operation of the device at these or any other conditions beyond those indicated under Recommended
Operating Conditions. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability.
(2) With I(RTN) = 0
(3) Do not apply voltages to these pins
(4) SOA limited to RTN = 80 V at 2.5 A.
6 Specifications
6.1 Absolute Maximum Ratings
over recommended TJ range; voltages with respect to VVSS (unless otherwise noted) (1)
MIN MAX UNIT
Input voltage
VDD, DEN -0.3 100
V
RTN (2) -0.6 100
IRSHDL_EN to RTN -0.3 6.5
AUTCLS -0.3 6.5
Output voltage
CLSA, CLSB, REF, MPS_DUTY (3) -0.3 6.5
V
AMPS_CTL (3) -0.3 30
Voltage
PG to RTN -0.3 100
V
TPH, TPL, BT to RTN -0.3 100
Sinking current
RTN (4) Internally limited
mAPG, TPH, TPL, BT 10
DEN 1
Sourcing current
CLSA, CLSB 65
mAREF Internally limited
AMPS_CTL 50
TJ(max) Maximum junction temperature Internally limited  deg C
Tstg Storage temperature -65 150  deg C
(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process.
(2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process.
(3) Discharges applied to circuit of Figure 22 between RJ-45, adapter, and output voltage rails, on TPS2372- 4EVM-006 Evaluation Module.
6.2 ESD Ratings
VALUE UNIT
V(ESD) Electrostatic discharge
Human body model (HBM), per ANSI/ESDA/JEDEC JS-001, all pins (1) +/-2000
V
Charged device model (CDM), per JEDEC specification JESD22-C101, all
pins (2) +/-500
IEC 61000-4-2 contact discharge (3) +/-8000
IEC 61000-4-2 air-gap discharge (3) +/-15000
```

### Page 5

#### Extracted tables

Table 1:

```text
|  | MIN | NOM | MAX | UNIT
Inputvoltagerange | RTN,VDD | 0 57 |  |  | V
Voltagerange | TPH,TPL,BTtoRTN | 0 57 |  |  | V
 | PGtoRTN | 0 57 |  |  | 
Sinkingcurrent | RTN(TPS2372-3) | 1.2 |  |  | A
 | RTN(TPS2372-4) | 1.85 |  |  | 
 | PG,TPH,TPL,BT | 3 |  |  | mA
Resistance | CLSA,CLSB(1) | 60 |  |  | Ohm
 | AMPS_CTL(1) | 1 |  |  | kOhm
 | REF(1) | 48.9 49.9 50.9 |  |  | 
Junctiontemperature |  | 40 125 |  |  | deg C
```

Table 2:

```text
| THERMALMETRIC(1) | TPS2372-3 | TPS2372-4 | UNIT
 |  | RGW (VQFN) | RGW (VQFN) | 
 |  | 20PINS | 20PINS | 
R Junction-to-ambientthermalresistance JA |  | 40.2 | 38.0 | deg C/W
R Junction-to-case(top)thermalresistance JC(top) |  | 34.6 | 28.1 | deg C/W
R Junction-to-boardthermalresistance JB |  | 17.9 | 16.1 | deg C/W
Junction-to-topcharacterizationparameter JT |  | 0.5 | 0.3 | deg C/W
Junction-to-boardcharacterizationparameter JB |  | 17.8 | 16.0 | deg C/W
R Junction-to-case(bottom)thermalresistance JC(bot) |  | 3.4 | 1.8 | deg C/W
```

#### Raw extracted text

```text
5
TPS2372
www.ti.com SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018
Product Folder Links: TPS2372
Submit Documentation FeedbackCopyright  2017-2018, Texas Instruments Incorporated
(1) Voltage should not be externally applied to this pin.
6.3 Recommended Operating Conditions
over operating free-air temperature range and voltages with respect to VSS (unless otherwise noted)
MIN NOM MAX UNIT
Input voltage range RTN, VDD 0 57 V
Voltage range
TPH, TPL, BT to RTN 0 57
V
PG to RTN 0 57
Sinking current
RTN ( TPS2372-3) 1.2
A
RTN ( TPS2372-4) 1.85
PG, TPH, TPL, BT 3 mA
Resistance
CLSA, CLSB (1) 60 Ohm
AMPS_CTL (1) 1
kOhm
REF (1) 48.9 49.9 50.9
Junction temperature -40 125  deg C
(1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application
report.
6.4 Thermal Information
THERMAL METRIC (1)
TPS2372-3 TPS2372-4
UNITRGW
(VQFN)
RGW
(VQFN)
20 PINS 20 PINS
RJA Junction-to-ambient thermal resistance 40.2 38.0  deg C/W
RJC(top) Junction-to-case (top) thermal resistance 34.6 28.1  deg C/W
RJB Junction-to-board thermal resistance 17.9 16.1  deg C/W
JT Junction-to-top characterization parameter 0.5 0.3  deg C/W
JB Junction-to-board characterization parameter 17.8 16.0  deg C/W
RJC(bot) Junction-to-case (bottom) thermal resistance 3.4 1.8  deg C/W
```

### Page 6

#### Extracted tables

Table 1:

```text
| PARAMETER | TESTCONDIT | IONS | MIN | TYP | MAX | UNIT
DETECTION(DEN) |  |  |  |  |  |  | 
Biascurrent |  | DENopen,V =10.1V,Measure VDD I (VDD,RTN,DEN),Notinmark SUPPLY |  | 3 4.8 14 |  |  | uA
DENleakagecurrent |  | V =V =57V DEN VDD |  | 0.5 5 |  |  | uA
Detectioncurrent |  | MeasureI (VDD,RTN,DEN),V = SUPPLY VDD 1.4V |  | 53.8 56.5 58.3 |  |  | uA
 |  | MeasureI (VDD,RTN,DEN),V = SUPPLY VDD 10.1V,Notinmark |  | 395 410 417 |  |  | 
V PD_DIS | Disablethreshold | DENfalling |  | 3 3.7 5 |  |  | V
 | Hysteresis |  |  | 75 150 250 |  |  | mV
CLASSIFICATION(CLS) |  |  |  |  |  |  | 
ClassificationA,Bsignature I CLS current |  | 13V<=V <=21V,MeasureI +I + VDD VDD DEN I RTN |  |  |  |  | 
 |  | R orR =1210Ohm CLSA CLSB |  | 2.1 2.5 2.9 |  |  | mA
 |  | R orR =249Ohm CLSA CLSB |  | 9.9 10.6 11.2 |  |  | 
 |  | R orR =140Ohm CLSA CLSB |  | 17.6 18.6 19.4 |  |  | 
 |  | R orR =90.9Ohm CLSA CLSB |  | 26.5 27.9 29.3 |  |  | 
 |  | R orR =63.4Ohm CLSA CLSB |  | 38 39.9 42 |  |  | 
I Autoclasssignaturecurrent AUTCLS |  | Aftert during1stClassevent ACS |  | 1 4 |  |  | mA
V CL_ON | Classlowerthreshold | V rising,I VDD CLS |  | 11.9 12.5 13 |  |  | V
V CL_H |  | Hysteresis |  | 1.4 1.6 1.7 |  |  | 
V CU_ON | Classupperthreshold | V rising,I VDD CLS |  | 21 22 23 |  |  | V
V CU_H |  | Hysteresis |  | 0.5 0.78 0.9 |  |  | 
V Markresetthreshold MSR |  | V falling VDD |  | 3 3.9 5 |  |  | V
Markstateresistance |  | 2-pointmeasurementat5Vand10.1V |  | 6 10 12 |  |  | kOhm
Leakagecurrent |  | V =57V,V =0V,measureI VDD CLS CLS |  | 1 |  |  | uA
t Longfirstclasseventtiming LCF_PD |  | Class1steventtimedurationfornewMPS |  | 76 81.5 86 |  |  | ms
t Autoclasssignaturetiming ACS |  | AUTCLSDuringClass1stevent |  | 76 81.5 87 |  |  | ms
AUTCLSpullupcurrent |  | 13V<=V <=21V VDD |  | 30 34 38 |  |  | uA
PASSDEVICE(RTN) |  |  |  |  |  |  | 
r Onresistance DS(on) |  |  | TPS2372-3 | 0.3 0.55 |  |  | Ohm
 |  |  | TPS2372-4 | 0.1 0.2 |  |  | 
Inputbiascurrent |  | V =V =30V,measureI VDD RTN RTN |  | 50 |  |  | uA
RTNleakagecurrent |  | V =V =100V,V =V ,measure VDD RTN DEN VSS I RTN |  | 80 |  |  | 
Currentlimit |  | V =1.5V RTN | TPS2372-3 | 1.55 1.85 2.2 |  |  | A
 |  | V =1.5V RTN | TPS2372-4 | 1.9 2.2 2.5 |  |  | 
Inrushcurrentlimit |  | V =2V, RTN V :20V->48V VDD | TPS2372-3 | 165 200 237 |  |  | mA
 |  | V =2V, RTN V :20V->48V VDD | TPS2372-4 | 275 335 395 |  |  | 
Inrushtermination t INR_DEL |  | Percentageofinrushcurrent |  | 65% 90% 99% |  |  | 
 |  | Inrushdelay |  | 78 81.5 87 |  |  | ms
Foldbackthreshold |  | V rising RTN |  | 12.5 14.5 15.5 |  |  | V
Foldbackdeglitchtime |  | V risingtowhencurrentlimitchangesto RTN inrushcurrentlimit |  | 1.35 1.65 1.95 |  |  | ms
POWERGOOD(PG) |  |  |  |  |  |  |
```

#### Raw extracted text

```text
6
TPS2372
SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018 www.ti.com
Product Folder Links: TPS2372
Submit Documentation Feedback Copyright  2017-2018, Texas Instruments Incorporated
6.5 Electrical Characteristics
Unless otherwise noted, 40 V <= VVDD <= 57 V; RDEN = 24.9 kOhm; PG, CLSA, CLSB, MPS_DUTY, AMPS_CTL, IRSHDL_EN,
TPH, TPL and BT open; VAUTCLS = VVSS; RREF = 49.9 kOhm; -40 deg C <= TJ <= 125 deg C. Positive currents are into pins. Typical values
are at 25 deg C. All voltages are with respect to VVSS unless otherwise noted.
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
DETECTION (DEN)
Bias current DEN open, VVDD = 10.1 V, Measure
ISUPPLY(VDD, RTN, DEN), Not in mark 3 4.8 14 uA
DEN leakage current VDEN = VVDD = 57 V 0.5 5 uA
Detection current
Measure ISUPPLY(VDD, RTN, DEN), VVDD =
1.4 V 53.8 56.5 58.3
uA
Measure ISUPPLY(VDD, RTN, DEN), VVDD =
10.1 V, Not in mark 395 410 417
VPD_DIS
Disable threshold DEN falling 3 3.7 5 V
Hysteresis 75 150 250 mV
CLASSIFICATION (CLS)
ICLS
Classification A,B signature
current
13 V <= VVDD <= 21 V, Measure IVDD + IDEN +
IRTN
RCLSA or RCLSB = 1210 Ohm 2.1 2.5 2.9
mA
RCLSA or RCLSB = 249 Ohm 9.9 10.6 11.2
RCLSA or RCLSB = 140 Ohm 17.6 18.6 19.4
RCLSA or RCLSB = 90.9 Ohm 26.5 27.9 29.3
RCLSA or RCLSB = 63.4 Ohm 38 39.9 42
IAUTCLS Autoclass signature current After tACS during 1st Class event 1 4 mA
VCL_ON
Class lower threshold
VVDD rising, ICLS  11.9 12.5 13
V
VCL_H Hysteresis 1.4 1.6 1.7
VCU_ON
Class upper threshold
VVDD rising, ICLS 21 22 23
V
VCU_H Hysteresis 0.5 0.78 0.9
VMSR Mark reset threshold VVDD falling 3 3.9 5 V
Mark state resistance 2-point measurement at 5 V and 10.1 V 6 10 12 kOhm
Leakage current VVDD = 57 V, VCLS = 0 V, measure ICLS 1 uA
tLCF_PD Long first class event timing Class 1st event time duration for new MPS 76 81.5 86 ms
tACS Autoclass signature timing AUTCLS During Class 1st event 76 81.5 87 ms
AUTCLS pullup current 13 V <= VVDD <= 21 V 30 34 38 uA
PASS DEVICE (RTN)
rDS(on) On resistance
TPS2372-3 0.3 0.55
Ohm
TPS2372-4 0.1 0.2
Input bias current VVDD = VRTN = 30 V, measure IRTN 50
uA
RTN leakage current VVDD = VRTN = 100 V, VDEN = VVSS , measure
IRTN
80
Current limit
VRTN = 1.5 V TPS2372-3 1.55 1.85 2.2
A
VRTN = 1.5 V TPS2372-4 1.9 2.2 2.5
Inrush current limit
VRTN = 2 V,
VVDD: 20 V -> 48 V TPS2372-3 165 200 237
mA
VRTN = 2 V,
VVDD: 20 V -> 48 V TPS2372-4 275 335 395
Inrush termination
Percentage of inrush current 65% 90% 99%
tINR_DEL Inrush delay 78 81.5 87 ms
Foldback threshold VRTN rising 12.5 14.5 15.5 V
Foldback deglitch time VRTN rising to when current limit changes to
inrush current limit 1.35 1.65 1.95 ms
POWER GOOD (PG)
```

### Page 7

#### Extracted tables

Table 1:

```text
| PARAMETER | TESTCONDIT | IONS | MIN | TYP | MAX | UNIT
Outputlowvoltage |  | MeasureV -V ,I =2mA,V =2 PG RTN PG RTN V,V :20V->48V DD |  | 0.27 0.5 |  |  | V
Leakagecurrent |  | V =57V,V =0V PG RTN |  | 10 |  |  | uA
 |  | V =10V,V =0V PG RTN |  | 1 |  |  | 
PSETYPEINDICATION(TPL,TPH,BT) |  |  |  |  |  |  | 
V Outputlowvoltage TPL |  | I =2mA,after2-,3-or5-event TPL classification,startuphascompleted, V =0V RTN |  | 0.27 0.5 |  |  | V
V Outputlowvoltage TPH |  | I =2mA,after4-or5-eventclassification, TPH startuphascompleted,V =0V RTN |  | 0.27 0.5 |  |  | 
V Outputlowvoltage BT |  | I =2mA,afterIEEE802.3btclassification, BT startuphascompleted,V =0V RTN |  | 0.27 0.5 |  |  | 
Leakagecurrent |  | V orV orV =7V,V =0V TPL TPH BT RTN |  | 1 |  |  | uA
t TPL,TPH,BTdelay TPLHBT |  | FromPG:Low->openduringstartuptoTPH and/orTPLand/orBTactive |  | 20 24 28 |  |  | ms
UVLO |  |  |  |  |  |  | 
V UVLO_R | UVLOrisingthreshold | V rising VDD |  | 36.3 38.1 40 |  |  | V
V UVLO_F | UVLOfallingthreshold | V falling VDD |  | 30.5 32 33.6 |  |  | 
V UVLO_H | UVLOhysteresis |  |  | 6.1 |  |  | V
BIASCURRENT |  |  |  |  |  |  | 
Operatingcurrent |  | 40V<=V <=57V,startuphascompleted VDD |  | 550 800 |  |  | uA
MPS |  |  |  |  |  |  | 
MPSDCsupplycurrent |  | Startuphascompleted,I =0mA RTN |  | 0.8 |  |  | mA
AMPS_CTLpulsedvoltage |  | Startuphascompleted,I <20mA, RTN R =1KOhmto12kOhm MPS |  | 23.1 24 24.9 |  |  | V
AutomaticMPSfalling currentthreshold |  | Startuphascompleted,I thresholdto RTN generateAMPS_CTLpulses |  | 18 28 38 |  |  | mA
 |  | HysteresisonRTNcurrent |  | 1 |  |  | 
MPSpulsedmodeduty cycleforType1-2PSE |  | MPSpulsedcurrentdutycycle |  | 25.8% 26.1% 26.4% |  |  | 
 |  | MPSpulsedcurrentONtime |  | 76 81.5 87 |  |  | ms
 |  | MPSpulsedcurrentOFFtime |  | 230 250 |  |  | 
MPSpulsedmodeduty cycleforType3-4PSE |  | MPSpulsedcurrentdutycycle, R >230kOhm MPS_DUTY |  | 5.2% 5.43% 5.6% |  |  | 
 |  | MPSpulsedcurrentONtime, R >230kOhm MPS_DUTY |  | 14.5 15.0 15.7 |  |  | ms
 |  | MPSpulsedcurrentdutycycle, R <8kOhm MPS_DUTY |  | 12.3% 12.5% 12.7% |  |  | 
 |  | MPSpulsedcurrentONtime, R <8kOhm MPS_DUTY |  | 36 37.5 39 |  |  | ms
 |  | MPSpulsedcurrentdutycycle, 43kOhm<R <77kOhm MPS_DUTY |  | 7.9% 8.1% 8.3% |  |  | 
 |  | MPSpulsedcurrentONtime, 43kOhm<R <77kOhm MPS_DUTY |  | 22.2 23.1 24 |  |  | ms
 |  | MPSpulsedcurrentOFFtime,R MPS_DUTY from0Ohmtoopencircuit |  | 250 263.5 277 |  |  | ms
MPS_DUTYpullupcurrent |  |  |  | 14 17 20 |  |  | uA
```

#### Raw extracted text

```text
7
TPS2372
www.ti.com SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018
Product Folder Links: TPS2372
Submit Documentation FeedbackCopyright  2017-2018, Texas Instruments Incorporated
Electrical Characteristics (continued)
Unless otherwise noted, 40 V <= VVDD <= 57 V; RDEN = 24.9 kOhm; PG, CLSA, CLSB, MPS_DUTY, AMPS_CTL, IRSHDL_EN,
TPH, TPL and BT open; VAUTCLS = VVSS; RREF = 49.9 kOhm; -40 deg C <= TJ <= 125 deg C. Positive currents are into pins. Typical values
are at 25 deg C. All voltages are with respect to VVSS unless otherwise noted.
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
Output low voltage Measure VPG - VRTN, IPG = 2 mA, VRTN = 2
V, VDD: 20 V -> 48 V 0.27 0.5 V
Leakage current
VPG = 57 V, VRTN = 0 V 10
uA
VPG = 10 V, VRTN = 0 V 1
PSE TYPE INDICATION (TPL, TPH, BT)
VTPL Output low voltage
ITPL = 2 mA, after 2-, 3- or 5-event
classification, startup has completed,
VRTN = 0 V
0.27 0.5
VVTPH Output low voltage ITPH = 2 mA, after 4- or 5-event classification,
startup has completed, VRTN = 0 V 0.27 0.5
VBT Output low voltage IBT = 2 mA, after IEEE802.3bt classification,
startup has completed, VRTN = 0 V 0.27 0.5
Leakage current VTPL or VTPH or VBT = 7 V, VRTN = 0 V 1 uA
tTPLHBT TPL, TPH, BT delay From PG: Low -> open during startup to TPH
and/or TPL and/or BT active 20 24 28 ms
UVLO
VUVLO_R UVLO rising threshold VVDD rising 36.3 38.1 40
V
VUVLO_F UVLO falling threshold VVDD falling 30.5 32 33.6
VUVLO_H UVLO hysteresis 6.1 V
BIAS CURRENT
Operating current 40 V <= VVDD <= 57 V, startup has completed 550 800 uA
MPS
MPS DC supply current Startup has completed, IRTN = 0 mA 0.8 mA
AMPS_CTL pulsed voltage Startup has completed, IRTN < 20 mA,
RMPS = 1 KOhm to 12 kOhm 23.1 24 24.9 V
Automatic MPS falling
current threshold
Startup has completed, IRTN threshold to
generate AMPS_CTL pulses 18 28 38
mA
Hysteresis on RTN current 1
MPS pulsed mode duty
cycle for Type 1-2 PSE
MPS pulsed current duty cycle 25.8% 26.1% 26.4%
MPS pulsed current ON time 76 81.5 87
ms
MPS pulsed current OFF time 230 250
MPS pulsed mode duty
cycle for Type 3-4 PSE
MPS pulsed current duty cycle,
RMPS_DUTY > 230 kOhm 5.2% 5.43% 5.6%
MPS pulsed current ON time,
RMPS_DUTY > 230 kOhm 14.5 15.0 15.7 ms
MPS pulsed current duty cycle,
RMPS_DUTY < 8 kOhm 12.3% 12.5% 12.7%
MPS pulsed current ON time,
RMPS_DUTY < 8 kOhm 36 37.5 39 ms
MPS pulsed current duty cycle,
43 kOhm < RMPS_DUTY < 77 kOhm 7.9% 8.1% 8.3%
MPS pulsed current ON time,
43 kOhm < RMPS_DUTY < 77 kOhm 22.2 23.1 24 ms
MPS pulsed current OFF time, RMPS_DUTY
from 0 Ohm to open circuit 250 263.5 277 ms
MPS_DUTY pullup current 14 17 20 uA
```

### Page 8

#### Extracted tables

Table 1:

```text
| PARAMETER | TESTCONDIT | IONS | MIN | TYP | MAX | UNIT
THERMALSHUTDOWN |  |  |  |  |  |  | 
Shutdown |  | T J |  | 140 158 |  |  | deg C
Hysteresis (1) |  |  |  | 20 |  |  | deg C
```

#### Raw extracted text

```text
8
TPS2372
SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018 www.ti.com
Product Folder Links: TPS2372
Submit Documentation Feedback Copyright  2017-2018, Texas Instruments Incorporated
Electrical Characteristics (continued)
Unless otherwise noted, 40 V <= VVDD <= 57 V; RDEN = 24.9 kOhm; PG, CLSA, CLSB, MPS_DUTY, AMPS_CTL, IRSHDL_EN,
TPH, TPL and BT open; VAUTCLS = VVSS; RREF = 49.9 kOhm; -40 deg C <= TJ <= 125 deg C. Positive currents are into pins. Typical values
are at 25 deg C. All voltages are with respect to VVSS unless otherwise noted.
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
(1) Parameters provided for reference only, and do not constitute part of TI published specifications for purposes of TI product warranty.
THERMAL SHUTDOWN
Shutdown TJ 140 158  deg C
Hysteresis (1) 20  deg C
```

### Page 9

#### Extracted tables

Table 1:

```text
|  |  | 700 TJ = -40C 650 TJ = 25C TJ = 125C )AP( 600 tnerruC 550 500 saiB 450 DDV 400 350 300 25 30 35 40 45 50 55 60 VDD-VSS Voltage (V) D002 |  |  | 
10 9 T T J J = = - 2 4 5 0 C C 8 TJ = 125C )AP( 7 tnerruC 6 5 saiB 4 DDV 3 2 1 0 0 1 2 3 4 5 6 7 8 9 10 VDD-VSS Voltage (V) D001 Figure1.DetectionBiasCurrentvsPoEVoltage | 10 9 T T J J = = - 2 4 5 0 C C 8 TJ = 125C )AP( 7 tnerruC 6 5 saiB 4 DDV 3 2 1 0 0 1 2 3 4 5 6 7 8 9 10 VDD-VSS Voltage (V) D001 |  | 700 TJ = -40C 650 TJ = 25C TJ = 125C )AP( 600 tnerruC 550 500 saiB 450 DDV 400 350 300 25 30 35 40 45 50 55 60 VDD-VSS Voltage (V) D002 |  |  | 
 | Figure1.DetectionBiasCurrentvsPoEVoltage |  | Figure2.I BiasCurrentvsVoltage VDD |  |  | 
13.5 VDD Rising (V) VDD Falling (V) 13 )V( egatloV 12.5 12 SSV-DDV 11.5 11 10.5 -50 -25 0 25 50 75 100 125 Junction Temperature (qC) D003 Figure3.ClassificationLowerThresholdvsTemperature | 13.5 VDD Rising (V) VDD Falling (V) 13 )V( egatloV 12.5 12 SSV-DDV 11.5 11 10.5 -50 -25 0 25 50 75 100 125 Junction Temperature (qC) D003 |  | 22.5 VDD Rising (V) VDD Falling (V) )V( egatloV 22 SSV-DDV 21.5 21 -50 -25 0 25 50 75 100 125 Junction Temperature (qC) D004 |  |  | 
 | Figure3.ClassificationLowerThresholdvsTemperature |  | Figure4.ClassificationUpperThresholdvsTemperature |  |  | 
4.5 )V( 4 egatloV SSV-DDV 3.5 3 -50 -25 0 25 50 75 100 125 Junction Temperature (qC) D005 Figure5.MarkResetThresholdvsTemperature | 4.5 )V( 4 egatloV SSV-DDV 3.5 3 -50 -25 0 25 50 75 100 125 Junction Temperature (qC) D005 |  | 9 8.75 ):k( ecnatsiseR 8.5 8.25 etatS 8 kraM 7.75 7.5 -50 -25 0 25 50 75 100 125 Junction Temperature (qC) D006 |  |  | 
 |  | Figure6.MarkResistancevsTemperature |  |  |  |
```

Table 2:

```text
|  |  |  |  |  |  |  | TJ = | 40C
 |  |  |  |  |  |  |  | TJ = T = | 25C 125C
 |  |  |  |  |  |  |  | J |
```

Table 3:

```text
|  |  |  |  | TJ | = -40C
 |  |  |  |  | TJ TJ | = 25C = 125C
```

Table 4:

```text
|  |  |  |  |  | VDD Ri VDD Fa | sing (V) lling (V)
```

Table 5:

```text
|  |  |  |  |  | VDD Ri VDD Fa | sing (V) lling (V)
```

#### Raw extracted text

```text
Junction Temperature (qC)
VDD-VSS Voltage (V)
-50 -25 0 25 50 75 100 125
3
3.5
4
4.5
D005
Junction Temperature (qC)
Mark State Resistance (k:)
-50 -25 0 25 50 75 100 125
7.5
7.75
8
8.25
8.5
8.75
9
D006
Junction Temperature (qC)
VDD-VSS Voltage (V)
-50 -25 0 25 50 75 100 125
10.5
11
11.5
12
12.5
13
13.5
D003
VDD Rising (V)
VDD Falling (V)
Junction Temperature (qC)
VDD-VSS Voltage (V)
-50 -25 0 25 50 75 100 125
21
21.5
22
22.5
D004
VDD Rising (V)
VDD Falling (V)
VDD-VSS Voltage (V)
VDD Bias Current (PA)
0 1 2 3 4 5 6 7 8 9 10
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
D001
TJ = -40C
TJ = 25C
TJ = 125C
VDD-VSS Voltage (V)
VDD Bias Current (PA)
25 30 35 40 45 50 55 60
300
350
400
450
500
550
600
650
700
D002
TJ = -40C
TJ = 25C
TJ = 125C
9
TPS2372
www.ti.com SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018
Product Folder Links: TPS2372
Submit Documentation FeedbackCopyright  2017-2018, Texas Instruments Incorporated
6.6 Typical Characteristics
Figure 1. Detection Bias Current vs PoE Voltage Figure 2. IVDD Bias Current vs Voltage
Figure 3. Classification Lower Threshold vs Temperature Figure 4. Classification Upper Threshold vs Temperature
Figure 5. Mark Reset Threshold vs Temperature Figure 6. Mark Resistance vs Temperature
```

### Page 10

#### Extracted tables

Table 1:

```text
|  |  | 2.2 2.15 )A( timiL 2.1 tnerruC 2.05 2 -50 -25 0 25 50 75 100 125 Junction Temperature (qC) D009 |  |  | 
0.175 ):( 0.15 ecnatsiseR 0.125 TEF ssaP 0.1 0.075 -50 -25 0 25 50 75 100 125 Junction Temperature (qC) D008 Figure7.PassFETResistancevsTemperature,TPS2372-4 | 0.175 ):( 0.15 ecnatsiseR 0.125 TEF ssaP 0.1 0.075 -50 -25 0 25 50 75 100 125 Junction Temperature (qC) D008 |  | 2.2 2.15 )A( timiL 2.1 tnerruC 2.05 2 -50 -25 0 25 50 75 100 125 Junction Temperature (qC) D009 |  |  | 
 | Figure7.PassFETResistancevsTemperature,TPS2372-4 |  | Figure8.PoECurrentLimitvsTemperature,TPS2372-4 |  |  | 
340 )Am( 335 timiL tnerruC 330 hsurnI 325 320 -50 -25 0 25 50 75 100 125 Junction Temperature (qC) D010 Figure9.PoEInrushCurrentLimitvsTemperature, TPS2372-4 | 340 )Am( 335 timiL tnerruC 330 hsurnI 325 320 -50 -25 0 25 50 75 100 125 Junction Temperature (qC) D010 |  | 91 )%( dlohserhT 90 noitanimreT 89 hsurnI 88 87 -50 -25 0 25 50 75 100 125 Junction Temperature (qC) D011 |  |  | 
 |  | Figure10.InrushTerminationThresholdvsTemperature, |  |  |  | 
 | TPS2372-4 |  | TPS2372-4 |  |  | 
84 )sm( 83 yaleD emiT 82 hsurnI 81 80 -50 -25 0 25 50 75 100 125 Junction Temperature (qC) D012 Figure11.InrushTimeDelayvsTemperature | 84 )sm( 83 yaleD emiT 82 hsurnI 81 80 -50 -25 0 25 50 75 100 125 Junction Temperature (qC) D012 |  | 38.7 38.65 )V( gnisiR 38.6 OLVU 38.55 DDV 38.5 38.45 38.4 -50 -25 0 25 50 75 100 125 Junction Temperature (qC) D013 |  |  | 
 |  | Figure12.UVLORisingThresholdvsTemperature |  |  |  |
```

#### Raw extracted text

```text
Junction Temperature (qC)
Inrush Time Delay (ms)
-50 -25 0 25 50 75 100 125
80
81
82
83
84
D012
Junction Temperature (qC)
VDD UVLO Rising (V)
-50 -25 0 25 50 75 100 125
38.4
38.45
38.5
38.55
38.6
38.65
38.7
D013
Junction Temperature (qC)
Inrush Current Limit (mA)
-50 -25 0 25 50 75 100 125
320
325
330
335
340
D010
Junction Temperature (qC)
Inrush Termination Threshold (%)
-50 -25 0 25 50 75 100 125
87
88
89
90
91
D011
Junction Temperature (qC)
Pass FET Resistance (:)
-50 -25 0 25 50 75 100 125
0.075
0.1
0.125
0.15
0.175
D008
Junction Temperature (qC)
Current Limit (A)
-50 -25 0 25 50 75 100 125
2
2.05
2.1
2.15
2.2
D009
10
TPS2372
SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018 www.ti.com
Product Folder Links: TPS2372
Submit Documentation Feedback Copyright  2017-2018, Texas Instruments Incorporated
Typical Characteristics (continued)
Figure 7. Pass FET Resistance vs Temperature, TPS2372-4 Figure 8. PoE Current Limit vs Temperature, TPS2372-4
Figure 9. PoE Inrush Current Limit vs Temperature,
TPS2372-4
Figure 10. Inrush Termination Threshold vs Temperature,
TPS2372-4
Figure 11. Inrush Time Delay vs Temperature Figure 12. UVLO Rising Threshold vs Temperature
```

### Page 11

#### Extracted tables

Table 1:

```text
| 32.15 )V( gnillaF 32.1 OLVU DDV 32.05 32 -50 -25 0 25 50 75 100 125 Junction Temperature (qC) D014
32.15 )V( gnillaF 32.1 OLVU DDV 32.05 32 -50 -25 0 25 50 75 100 125 Junction Temperature (qC) D014 Figure13.UVLOFallingThresholdvsTemperature | 32.15 )V( gnillaF 32.1 OLVU DDV 32.05 32 -50 -25 0 25 50 75 100 125 Junction Temperature (qC) D014
```

#### Raw extracted text

```text
Junction Temperature (qC)
VDD UVLO Falling (V)
-50 -25 0 25 50 75 100 125
32
32.05
32.1
32.15
D014
11
TPS2372
www.ti.com SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018
Product Folder Links: TPS2372
Submit Documentation FeedbackCopyright  2017-2018, Texas Instruments Incorporated
Typical Characteristics (continued)
Figure 13. UVLO Falling Threshold vs Temperature
```

### Page 12

#### Raw extracted text

```text
12
TPS2372
SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018 www.ti.com
Product Folder Links: TPS2372
Submit Documentation Feedback Copyright  2017-2018, Texas Instruments Incorporated
7 Detailed Description
7.1 Overview
The TPS2372 device is a 20-pin integrated circuit that contains all of the features needed to implement a single
interface IEEE802.3bt Type-3 ( TPS2372-3) and Type-4 ( TPS2372-4) powered device (PD). Basic functionality
supported includes Detection, Hardware Classification, and inrush current limit (200-mA for TPS2372-3 and 335-
mA for TPS2372-4) during startup. Enhanced features include the automatic maintain power signature (MPS).
The TPS2372-3 integrates a low 0.3-Ohm internal switch to support Type-3 applications up to 60 W of continuous
power sourced by the PSE, allowing beyond 1.2 A (1.55 A minimum current limit) through the PD during normal
operation.
Likewise, the TPS2372-4 integrates a low 0.1-Ohm internal switch to support Type-4 applications up to 90 W of
continuous power sourced by the PSE, allowing up to 1.9 A through the PD during normal operation.
The TPS2372 has a built-in inrush time delay period, for a simple solution to meet the IEEE802.3bt startup
requirement.
The TPS2372 contains several protection features such as thermal shutdown, current limit foldback, and a robust
100-V internal switch.
```

### Page 13

#### Extracted tables

Table 1:

```text
OTSD |
```

#### Raw extracted text

```text
12.5V &
10.9V
22V &
21.25V
38.1V &
 32V
VDD
1
0
S
R Q
Inrush limit
threshold
Current limit
threshold
VSS
RTN
CLSA
IRSHDL_EN
VSS DEN
800Ps
2.5V
REG.
Detection
Comp.
4V
Hotswap
MOSFET
Class
Comp.
Mark
Comp. 14.5V
UVLO
Comp.
OTSD
IRTN sense,1 if < 90% of inrush and current limit
1 = inrush
Signals referenced to VSS unless
otherwise noted
Class
Comp.
3.9V
0 = current limit
Inrush latch
1.65ms
1
0
IRTN sense
State
Eng.
Mark Comp Out
UVLO Comp Out
VSS
S
R
Q
High if over
temperauture
RTN
PG
TPH, TPL
/BT
RTN
Inrush
Timing
AUTCLS
Automatic
MPS Control
RTN
MPS
thresholdMPS_DUTY
AMPS_CTRL
VDD24V
REF
1.5V Bias
Oscillator
Class Comp Out
CLSBMark R
MPS Enable
5.5V
5.5V
13
TPS2372
www.ti.com SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018
Product Folder Links: TPS2372
Submit Documentation FeedbackCopyright  2017-2018, Texas Instruments Incorporated
7.2 Functional Block Diagram
7.3 Feature Description
7.3.1 PG Power Good (Converter Enable) Pin Interface
PG is an active high output that is pulled to RTN when the device is in inrush phase. It remains in a high
impedance state at all other times. This pin is an open-drain output, and it may require a pullup resistor or other
interface to the downstream load. PG may be left open if it is not used.
The PG pin can be used to inhibit downstream converter startup by keeping the soft-start pin low. Figure 14
shows an example where PG connects to the SS pin of a DC-DC controller. Because PG is an open drain
output, it will not affect the soft-start capacitor charge time when it deasserts. Another common use of the PG pin
is to enable a converter with an active-high enable input. In this case, PG may require a pullup resistor to either
VDD, or to a bias supply, depending on the requirements of the controller enable pin.
```

### Page 14

#### Extracted tables

Table 1:

```text
PDClass | CLASS SIGNATUREA | CLASS SIGNATUREB | MINIMUM POWERATPD (W) | MAXIMUM POWERATPD (W) | NUMBEROF CLASS CYCLES@ MAXPOWER | RESISTOR CLSA(Ohm) | RESISTOR CLSB(Ohm)
0 | 0 | 0 | 0.44 | 12.95 | 1 | 1210 | 1210
1 | 1 | 1 | 0.44 | 3.84 | 1 | 249 | 249
2 | 2 | 2 | 3.84 | 6.49 | 1 | 140 | 140
3 | 3 | 3 | 6.49 | 12.95 | 1 | 90.9 | 90.9
4 | 4 | 4 | 12.95 | 25.5 | 2,3 | 63.4 | 63.4
5 | 4 | 0 | 25.5 | 40 | 4 | 63.4 | 1210
6 | 4 | 1 | 40 | 51 | 4 | 63.4 | 249
7 | 4 | 2 | 51 | 62 | 5 | 63.4 | 140
8 | 4 | 3 | 62 | 71 | 5 | 63.4 | 90.9
```

#### Raw extracted text

```text
RTN
PG
TPS2372
SS
DC/DC
OUT
MCU
Css
Copyright  2017, Texas Instruments Incorporated
14
TPS2372
SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018 www.ti.com
Product Folder Links: TPS2372
Submit Documentation Feedback Copyright  2017-2018, Texas Instruments Incorporated
Feature Description (continued)
Figure 14. PG Interface
7.3.2 CLSA and CLSB Classification, AUTCLS
Each of the two external resistors (RCLSA and RCLSB in Figure 22) connected between the CLSA (first and second
class event) and CLSB (third and any subsequent class event) pins and VSS provide a distinct classification
signature to the PSE, and are used to define the power class requested by the PD. The controller places a
voltage of approximately 2.5 V across CLSA (first or second class event) or CLSB (all additional class events)
external resistor whenever the voltage differential between VDD and VSS lies from about 10.9 V to 22 V. The
current drawn by each resistor, combined with the internal current drain of the controller and any leakage through
the internal pass MOSFET, creates the classification signature current. Table 1 lists the external resistor values
required for each of the PD power ranges defined by IEEE802.3bt. The number of classification cycles then
determines how much power is allocated by the PSE. The maximum average power drawn by the PD, plus the
power supplied to the downstream load, should not exceed the maximum power indicated in Table 1, as well as
the maximum power allocated by the PSE based on the number of classification cycles.
Type 2 and Type 3 PSEs may perform two classification cycles if Class 4 signature is presented on the first
cycle. Likewise, Type 3 and Type 4 PSEs may perform four classification cycles if Class 4 signature is presented
on the first two cycles and Class 0 or 1 signature is presented on the third cycle. Also, Type 4 PSEs may perform
five classification cycles if Class 4 signature is presented on the first two cycles and Class 2 or 3 signature is
presented on the third cycle.
Table 1. Class Resistor Selection
PD Class CLASS
SIGNATURE A
CLASS
SIGNATURE B
MINIMUM
POWER AT PD
(W)
MAXIMUM
POWER AT PD
(W)
NUMBER OF
CLASS
CYCLES @
MAX POWER
RESISTOR
CLSA (Ohm)
RESISTOR
CLSB (Ohm)
0 0 0 0.44 12.95 1 1210 1210
1 1 1 0.44 3.84 1 249 249
2 2 2 3.84 6.49 1 140 140
3 3 3 6.49 12.95 1 90.9 90.9
4 4 4 12.95 25.5 2,3 63.4 63.4
5 4 0 25.5 40 4 63.4 1210
6 4 1 40 51 4 63.4 249
7 4 2 51 62 5 63.4 140
8 4 3 62 71 5 63.4 90.9
```

### Page 15

#### Extracted tables

Table 1:

```text
PSEType | PDClass | NUMBEROF CLASSCYCLES | PSE ALLOCATED POWERATPD (W) | TPH | TPL | BT(1)
1-2 | 0 | 1 | 12.95 | HIGH | HIGH | HIGH
1-2 | 1 | 1 | 3.84 | HIGH | HIGH | HIGH
1-2 | 2 | 1 | 6.49 | HIGH | HIGH | HIGH
1-2 | 3 | 1 | 12.95 | HIGH | HIGH | HIGH
2 | 4 | 2 | 25.5 | HIGH | LOW | HIGH
```

#### Raw extracted text

```text
15
TPS2372
www.ti.com SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018
Product Folder Links: TPS2372
Submit Documentation FeedbackCopyright  2017-2018, Texas Instruments Incorporated
(1) The BT output is not required to indicate how much power is allocated to the PD by a IEEE802.3bt compliant PSE. Additional
information may be provided depending on the application described in the Application Detailed Design Requirements section Opto-
isolators for TPH, TPL and BT
The AUTCLS input is used to enable the Autoclass function during classification. When enabled, the class
signature during the first class event drops to class 0 current level after a time tACS of the first class event,
indicating to a Type 3 or 4 PSE that it supports Autoclass.
7.3.3 DEN Detection and Enable
DEN pin implements two separate functions. A resistor (RDEN in Figure 22) connected between VDD and DEN
generates a detection signature whenever the voltage differential between VDD and VSS lies from approximately
1.4 to 10.9 V. Beyond this range, the controller disconnects this resistor to save power. The IEEE 802.3bt
standard specifies a detection signature resistance, RDEN from 23.75 kOhm to 26.25 kOhm, or 25 kOhm +/- 5%. TI
recommends a resistor of 24.9 kOhm +/- 1% for RDEN.
Pulling DEN to VSS during powered operation causes the internal hotswap MOSFET and class regulator to turn
off. If the resistance connected between VDD and DEN is divided into two roughly equal portions, then the
application circuit can disable the PD by grounding the tap point between the two resistances, while
simultaneously spoiling the detection signature which prevents the PD from properly re-detecting.
7.3.4 Internal Pass MOSFET and Inrush Delay Enable, IRSHDL_EN
RTN pin provides the negative power return path for the load. Once VVDD exceeds the UVLO threshold, the
internal pass MOSFET pulls RTN to VSS. Inrush limiting prevents the RTN current from exceeding a nominal
value of about 200 mA and 335 mA for the TPS2372-3 and TPS2372-4 respectively until the bulk capacitance
(CBULK in Figure 22) is fully charged. Two conditions must be met to reach the end of inrush phase. The first one
is when the RTN current drops below about 90% of nominal inrush current at which point the current limit is
changed to 1.85 A for TPS2372-3 and 2.2 A for TPS2372-4, while the second one, if IRSHDL_EN is open, is to
ensure a minimum inrush delay period of ~81.5 ms (tINR_DEL) from beginning of the inrush phase. The PG output
becomes high impedance to signal the downstream load that the bulk capacitance is fully charged and the inrush
period has been completed. Connecting IRSHDL_EN input to RTN pin disables the inrush delay, in which case
only the first condition applies to reach the end of inrush phase.
If RTN ever exceeds about 14.5 V for longer than ~1.65 ms, then the TPS2372 returns to inrush phase; note that
in this particular case, the second condition described above about inrush phase duration (81.5 ms) is not
applicable.
7.3.5 TPH, TPL and BT PSE Type Indicators
The state of BT, TPH and TPL is used to provide information relative to the PSE Type (1-2 or 3-4) and its
allocated power. Table 2 lists the encoding corresponding to various combinations of PSE Type, PD Class and
allocated power. Table 3 also corresponds to cases where the PSE allocated power is lower than what the PD is
requesting. The allocated power is determined by the number of classification cycles having been received.
During startup, the TPH, TPL and BT outputs are enabled typically 24 ms after PG went from low to open, to
allow the power supply to reach a stable state first. These 3 outputs will return to a high-impedance state if the
part enters thermal shutdown, or if VDD-to-VSS voltage falls below ~32 V. Note that in all these cases, as long
as VDD-to-VSS voltage remains above the mark reset threshold, the internal logic state of these 3 signals is
remembered such that these outputs will be activated accordingly after the startup has completed. This circuit
resets when the VDD-to-VSS voltage drops below the mark reset threshold. The TPH, TPL and BT pins can be
left unconnected if not used.
Table 2. TPH, TPL, BT and Allocated Power Truth Table
PSE Type PD Class NUMBER OF
CLASS CYCLES
PSE
ALLOCATED
POWER AT PD
(W)
TPH TPL BT (1)
1-2 0 1 12.95 HIGH HIGH HIGH
1-2 1 1 3.84 HIGH HIGH HIGH
1-2 2 1 6.49 HIGH HIGH HIGH
1-2 3 1 12.95 HIGH HIGH HIGH
2 4 2 25.5 HIGH LOW HIGH
```

### Page 16

#### Extracted tables

Table 1:

```text
PSEType | PDClass | NUMBEROF CLASSCYCLES | PSE ALLOCATED POWERATPD (W) | TPH | TPL | BT(1)
3-4 | 0 | 1 | 12.95 | HIGH | HIGH | LOW
3-4 | 1 | 1 | 3.84 | HIGH | HIGH | LOW
3-4 | 2 | 1 | 6.49 | HIGH | HIGH | LOW
3-4 | 3 | 1 | 12.95 | HIGH | HIGH | LOW
3-4 | 4 | 2-3 | 25.5 | HIGH | LOW | LOW
3-4 | 5 | 4 | 40 | LOW | HIGH | LOW
3-4 | 6 | 4 | 51 | LOW | HIGH | LOW
4 | 7 | 5 | 62 | LOW | LOW | LOW
4 | 8 | 5 | 71 | LOW | LOW | LOW
```

Table 2:

```text
PSEType | PDClass | NUMBEROF CLASSCYCLES | PSE ALLOCATED POWERATPD (W) | TPH | TPL | BT
3-4 | 4-8 | 1 | 12.95 | HIGH | HIGH | LOW
3-4 | 5-8 | 2,3 | 25.5 | HIGH | LOW | LOW
3-4 | 7-8 | 4 | 51 | LOW | HIGH | LOW
```

Table 3:

```text
PSEType | MPS_DUTY | MPSDuty-Cycle
1,2 |  | 26%
3,4 | ShorttoVSS | 12.5%
3,4 | Resistance(60.4Ktyp.)toVSS | 8.1%
3,4 | Open | 5.4%
```

#### Raw extracted text

```text
16
TPS2372
SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018 www.ti.com
Product Folder Links: TPS2372
Submit Documentation Feedback Copyright  2017-2018, Texas Instruments Incorporated
Table 2. TPH, TPL, BT and Allocated Power Truth Table (continued)
PSE Type PD Class NUMBER OF
CLASS CYCLES
PSE
ALLOCATED
POWER AT PD
(W)
TPH TPL BT (1)
3-4 0 1 12.95 HIGH HIGH LOW
3-4 1 1 3.84 HIGH HIGH LOW
3-4 2 1 6.49 HIGH HIGH LOW
3-4 3 1 12.95 HIGH HIGH LOW
3-4 4 2-3 25.5 HIGH LOW LOW
3-4 5 4 40 LOW HIGH LOW
3-4 6 4 51 LOW HIGH LOW
4 7 5 62 LOW LOW LOW
4 8 5 71 LOW LOW LOW
Table 3. Power Demotion Cases
PSE Type PD Class NUMBER OF
CLASS CYCLES
PSE
ALLOCATED
POWER AT PD
(W)
TPH TPL BT
3-4 4-8 1 12.95 HIGH HIGH LOW
3-4 5-8 2,3 25.5 HIGH LOW LOW
3-4 7-8 4 51 LOW HIGH LOW
7.3.6 AMPS_CTL, MPS_DUTY and Automatic MPS
To maintain PSE power, the AMPS_CTL output generates voltage pulses. This is translated into current pulses
by connecting a resistor between AMPS_CTL and VSS. These pulses are automatically generated as long as the
current through the RTN-to-VSS path is not high enough (< ~28 mA). Typical resistor value of 1.3 kOhm is
recommended, in applications where the load current may go below ~20 mA and the PSE power has to be
maintained.
If a Type 3 or 4 PSE is detected, the MPS_DUTY input can be used to select one out of three duty-cycles (5.4%,
8.1%, 12.5%). The selection is based on various system parameters, which include the amount of bulk
capacitance, the input cable impedance and the type of input bridge. Also, inserting a blocking diode (or
MOSFET) between the bulk capacitor and the TPS2372 allows the selection of a shorter MPS duty-cycle.Table 4
should be used to select a proper MPS Duty Cycle.
Table 4. MPS Duty-Cycle Selection
PSE Type MPS_DUTY MPS Duty-Cycle
1,2 - 26%
3,4 Short to VSS 12.5%
3,4 Resistance (60.4K typ.) to VSS 8.1%
3,4 Open 5.4%
```

### Page 17

#### Extracted tables

Table 1:

```text
Expecte | dPoEPDSystemConditions |  | MPS | _DUTYSelection | 
C BULK BlockingDiode | C BULK | CableLength | MPS Duty-cycle | PinTermination | I (mA) MPS
Yes | Any | 0-100m | 5.4%orlonger | Open | 18.5
No | <=60uF |  | 8.1%orlonger | 60kOhmtoVSS | 18.5
No | >60uF,<=120uF |  | 12.5% | ShorttoVSS | 18.5
No | <=120uF |  | 5.4%orlonger(1) | Open | 18.5
No | >120uF,<=300uF |  | 8.1%orlonger (1) | 60kOhmtoVSS | 18.5
```

#### Raw extracted text

```text
17
TPS2372
www.ti.com SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018
Product Folder Links: TPS2372
Submit Documentation FeedbackCopyright  2017-2018, Texas Instruments Incorporated
(1) Applicable when PSE voltage step-down events are unlikely or are not expected to exceed -0.4 V.
Table 5. System Conditions and MPS Duty-Cycle
Expected PoE PD System Conditions MPS_DUTY Selection
CBULK
Blocking Diode CBULK Cable Length MPS
Duty-cycle Pin Termination IMPS (mA)
Yes Any
0 -100m
5.4% or longer Open 18.5
No <= 60 uF 8.1% or longer 60 kOhm to VSS 18.5
No > 60 uF, <= 120 uF 12.5% Short to VSS 18.5
No <= 120 uF 5.4% or longer (1) Open 18.5
No > 120 uF, <= 300 uF 8.1% or longer (1) 60 kOhm to VSS 18.5
7.3.7 VDD Supply Voltage
VDD pin connects to the positive side of the input supply. It provides operating power to the PD controller and
allows monitoring of the input line voltage. If VVDD falls below its UVLO threshold and goes back above it, or if a
thermal shutdown resumes while VVDD is already above its UVLO threshold, the TPS2372 returns to inrush
phase.
7.3.8 VSS
VSS pin is the input supply negative rail that serves as a local ground. The exposed thermal PAD must be
connected to this pin to ensure proper operation.
7.3.9 Exposed Thermal PAD
The exposed thermal PAD is internally connected to VSS pin. It should be tied to a large VSS copper area on the
PCB to provide a low resistance thermal path to the circuit board. TI recommends maintaining a clearance of
0.025 between VSS and high-voltage signals such as VDD.
7.4 Device Functional Modes
7.4.1 PoE Overview
The following text is intended as an aid in understanding the operation of the TPS2372 but not as a substitute for
the IEEE 802.3bt standard. The pending IEEE 802.3bt standard is an update to IEEE 802.3-2012 clause 33
(PoE), adding 4-pair power, high-power options, additional features and enhanced classification. Generally
speaking, a device compliant to IEEE 802.3-2012 is referred to as a Type 1 (Class 0-3) or 2 (Class 4) device,
and devices with higher power and enhanced classification will be referred to as Type 3 (Class 5,6) or 4 (Class
7,8) devices. Type 3 devices will also include Class 0-4 devices that are 4-pair capable. Standards change and
should always be referenced when making design decisions.
The IEEE 802.3bt standard defines a method of safely powering a PD (powered device) over a cable by power
sourcing equipment (PSE), and then removing power if a PD is disconnected. The process proceeds through an
idle state and three operational states of detection, classification, and operation. There is also a fourth
operational state used by Type 3 and 4 PSEs, called "connection check", to determine if the PD has same
(single interface) or independent (dual interface or commonly referred to "dual-signature" in the IEEE802.3bt
standard) classification signature on each pairset. The PSE leaves the cable unpowered (idle state) while it
periodically looks to see if something has been plugged in; this is referred to as detection, and also includes
connection check if Type 3 or 4 PSE. The low power levels used during detection and connection check are
unlikely to damage devices not designed for PoE. If a valid PD signature is present, the PSE may inquire how
much power the PD requires; this is referred to as classification. The PSE may then power the PD if it has
adequate capacity.
```

### Page 18

#### Extracted tables

Table 1:

```text
Shut- down |  | 
 | Nor | mal Operation
```

Table 2:

```text
STANDARD | POWERLOOP RESISTANCE (MAX) | PSEOUTPUT POWER(MIN) | PSESTATICOUTPUT VOLTAGE(MIN) | PDINPUT POWER(MAX) | STATICPDINPU | TVOLTAGE
 |  |  |  |  | POWER<=13W | POWER>13W
IEEE802.3-2012 802.3at(Type1) | 20Ohm | 15.4W | 44V | 13W | 37V-57V | N/A
802.3bt(Type3) | 12.5Ohm |  | 50V |  |  | 
802.3at(Type2) 802.3bt(Type3) | 12.5Ohm | 30W | 50V | 25.5W | 37V-57V | 42.5V-57V
802.3bt(Type3) | 6.25Ohm(4-pair) | 60W | 50V | 51W | N/A | 42.5V-57V
802.3bt(Type4) | 6.25Ohm(4-pair) | 90W | 52V | 71.3W | N/A | 41.2V-57V
```

#### Raw extracted text

```text
5742373020.514.510.12.7
Detection Lower Limit
Detection
Upper LimitClassification Lower Limit
Classification
Upper LimitMust Turn Off by
-
Voltage Falling
Lower Limit -
Operating RangeMust Turn On by
-
Voltage Rising Maximum InputVoltage
Detect Classify Shut-
down
PI Voltage (V)
0
Lower Limit -
13W Op.
Mark
Class-Mark
Transition
250Ps
Transient
6.9
Normal Operation
       Normal   Operation
TPH/TPL
Reset Range
42.5
18
TPS2372
SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018 www.ti.com
Product Folder Links: TPS2372
Submit Documentation Feedback Copyright  2017-2018, Texas Instruments Incorporated
Device Functional Modes (continued)
Type 3 or Type 4 PSEs are required to do an enhanced hardware classification of Type 3 or 4 respectively. Type
2 PSEs are required to do Type 1 hardware classification plus a data-layer classification, or an enhanced Type 2
hardware classification. Type 1 PSEs are not required to do hardware or data link layer (DLL) classification. A
Type 3 or Type 4 PD must do respectively Type 3 or Type 4 hardware classification as well as DLL classification.
A Type 2 PD must do Type 2 hardware classification as well as DLL classification. The PD may return the
default, 13-W current-encoded class, or one of four other choices if Type 2, one of six other choices if Type 3,
and one of eight other choices if Type 4. DLL classification occurs after power-on and the Ethernet data link has
been established.
The Autoclass function is optional for both the PSE and the PD.
Once started, the PD must present a maintain power signature (MPS) to assure the PSE that it is still present.
The PSE monitors its output for a valid MPS, and turns the port off if it loses the MPS. Loss of the MPS returns
the PSE to the idle state. Figure 15 shows the operational states as a function of PD input voltage.
Figure 15. Operational States
The PD input, typically an RJ-45 eight-lead connector, is referred to as the power interface (PI). PD input
requirements differ from PSE output requirements to account for voltage drops and operating margin. The
standard allots the maximum loss to the cable regardless of the actual installation to simplify implementation.
IEEE 802.3-2008 was designed to run over infrastructure including ISO/IEC 11801 class C (CAT3 per TIA/EIA-
568) that may have had AWG 26 conductors. IEEE 802.3at Type 2 and IEEE 802.3bt Type 3 cabling power loss
allotments and voltage drops have been adjusted for 12.5-Ohm power loops per ISO/IEC11801 class D (CAT5 or
higher per TIA/EIA-568, typically AWG 24 conductors). Table 6 shows key operational limits broken out for the
two revisions of the standard.
Table 6. Comparison of Operational Limits
STANDARD
POWER LOOP
RESISTANCE
(MAX)
PSE OUTPUT
POWER (MIN)
PSE STATIC OUTPUT
VOLTAGE (MIN)
PD INPUT
POWER (MAX)
STATIC PD INPUT VOLTAGE
POWER <= 13 W POWER > 13 W
IEEE802.3-2012
802.3at (Type 1) 20 Ohm
15.4 W
44 V
13 W 37 V - 57 V N/A
802.3bt (Type 3) 12.5 Ohm 50 V
802.3at (Type 2)
802.3bt (Type 3)
12.5 Ohm 30 W 50 V 25.5 W 37 V - 57 V 42.5 V - 57 V
802.3bt (Type 3) 6.25 Ohm (4-pair) 60 W 50 V 51 W N/A 42.5 V - 57 V
802.3bt (Type 4) 6.25 Ohm (4-pair) 90 W 52 V 71.3 W N/A 41.2 V - 57 V
```

### Page 19

#### Raw extracted text

```text
VUVLO_R
Detection
Classification
PD Powered
Idle
VCL_ON
VCL_H
VCU_ON
VCU_H
Note:  Variable names refer to Electrical Characteristic
          Table parameters
VDD-VSS
VUVLO_H
Mark
VMSR
Functional
State
19
TPS2372
www.ti.com SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018
Product Folder Links: TPS2372
Submit Documentation FeedbackCopyright  2017-2018, Texas Instruments Incorporated
The PSE can apply voltage either between the RX and TX pairs (pins 1-2 and 3-6 for 10baseT or 100baseT), or
between the two spare pairs (4-5 and 7-8). Power application to the same pin combinations in
1000/2.5G/5G/10GbaseT systems is recognized in IEEE 802.3bt. 1000/2.5G/5G/10GbaseT systems can handle
data on all pairs, eliminating the spare pair terminology. Type 1 and 2 PSEs are allowed to apply voltage to only
one set of pairs at a time, while Type 3 and 4 PSEs may apply power to one or both sets of pairs at a time. The
PD uses input diode or active bridges to accept power from any of the possible PSE configurations. The voltage
drops associated with the input bridges create a difference between the standard limits at the PI and the
TPS2372 specifications.
A compliant Type 2, 3 or 4 PD has power management requirements not present with a Type 1 PD. These
requirements include the following:
1. Must interpret respectively Type 2, 3 or 4 hardware classification.
2. Must present hardware Class 4 during the first two classfication events, applicable to Type 2 and 4 PDs, as
well as to Type 3 PD with Class level 4 or higher.
3. If Type 3 or 4 single interface PD, it must present hardware Class in the range of 0 to 3 during the third and
any subsequent classification events.
4. Must implement DLL negotiation.
5. Must behave like a Type 1 PD for 50 ms then must draw less than 400 mA until 80 m after the PSE applies
operation voltage (power up), if Type 2 or 3 single interface PD. This covers the PSE inrush period, which is
75 ms maximum.
6. Should behave like a Type 1 PD for 50 ms then must draw less than 400 mA until 80 ms after the PSE
applies operation voltage (power up), if Type 4 single interface PD.
7. Must not draw more than 60 mA and 5 mA any time the input voltage falls below respectively 30 V and 10 V.
8. Must not draw more than 13 W if it has not received at least a Type 2 hardware classification or received
permission through DLL.
9. Must not draw more than 25.5 W if it has not received at least 4 classification events or received permission
through DLL.
10. Must not draw more than 51 W if it has not received at least 5 classification events or received permission
through DLL.
11. Must meet various operating and transient templates.
12. Optionally monitor for the presence or absence of an adapter (assume high power).
As a result of these requirements, the PD must be able to dynamically control its loading, and monitor TPL and
TPH for changes. In cases where the design needs to know specifically if an adapter is plugged in and
operational, the adapter should be individually monitored, typically with an optocoupler.
7.4.2 Threshold Voltages
The TPS2372 has a number of internal comparators with hysteresis for stable switching between the various
states. Figure 16 relates the parameters in Electrical Characteristics to the PoE states. The mode labeled Idle
between Classification and Operation implies that the DEN, CLSA, CLSB, and RTN pins are all high impedance.
The state labeled Mark, which is drawn in dashed lines, is part of the Type 2-3-4 hardware class state machine.
Figure 16. Threshold Voltages
```

### Page 20

#### Extracted tables

Table 1:

```text
|  |  |  |  |  |  | Load | enab |  | led a |  |  |  | fter St |  |  | artu |  |  |  | p dela |  |  |  |  | y |  |  | 
 |  |  |  |  |  |  | (TP | Inrus S237 |  | h 2-3) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
I |  |  |  |  |  |  |  |  |  | A | A |  |  | utocla |  |  | ss |  |  |  |  |  |  |  |  |  |  |  | 
 |  | I |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  | PI |  |  |  |  |  | t |  | t |  | ACS |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  | Class |  |  |  |  |  |  |  |  |  |  | Mark |  |  |  |  |  |  |  | 
 |  |  |  | ect |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Det |  |  |  | ect |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
```

#### Raw extracted text

```text
Time: 50ms/div
Voltage: 10V/div Current: 100mA/div
IPI
Load enabled after Startup delay
Detect
Class Mark
VVDD-VSS
VRTN-VSS
Autoclass
tACS
Inrush
(TPS2372-3)
20
TPS2372
SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018 www.ti.com
Product Folder Links: TPS2372
Submit Documentation Feedback Copyright  2017-2018, Texas Instruments Incorporated
7.4.3 PoE Startup Sequence
The waveforms of Figure 17 demonstrate detection, classification including Autoclass during the first class event,
and startup from a PSE with Type 3 Class 6 hardware classification. The key waveforms shown are V(VDD-VSS),
V(RTN-VSS) and IPI. IEEE 802.3bt requires a PSE allocating Class 6 level of power to generate a minimum of two
detection levels, four class and mark cycles, and startup from the fourth mark event. As shown below, the
required minimum duration of the first class event has been extended for Type 3 and 4 PSEs. VRTN to VSS falls
as the TPS2372 charges CBULK following application of full voltage. In Figure 19, assertion of the PG signal is
delayed and used to enable load current as seen in the IPI waveform.
Figure 17. Startup of Class 6 PD
7.4.4 Detection
The TPS2372 pulls DEN to VSS whenever V(VDD-VSS) is below the lower classification threshold. When the input
voltage rises above VCL_ON, the DEN pin goes to an open-drain condition to conserve power. While in detection,
RTN is high impedance, and almost all the internal circuits are disabled. An RDEN of 24.9 kOhm (+/-1%), presents the
correct signature. It may be a small, low-power resistor because it only sees a stress of about 5 mW. A valid PD
detection signature is an incremental resistance ( V / I ) from 23.7 kOhm to 26.3 kOhm at the PI.
The detection resistance seen by the PSE at the PI is the result of the input bridge resistance in series with the
parallel combination of RDEN and internal VDD loading. The input diode bridges incremental resistance may be
hundreds of Ohm at the low currents drawn when 2.7 V is applied to the PI. The input bridge resistance is partially
compensated by the TPS2372 effective resistance during detection.
The hardware classification protocol of IEEE 802.3bt specifies that a Type 2, 3 or 4 PSE drops its output voltage
into the detection range during the classification sequence. The PD is required to have an incorrect detection
signature in this condition, which is referred to as a mark event (see Figure 17). After the first mark event, the
TPS2372 will present a signature less than 12 kOhm until it has experienced a V(VDD-VSS) voltage below the mark
reset threshold (VMSR). This is explained more fully under Hardware Classification.
```

### Page 21

#### Raw extracted text

```text
21
TPS2372
www.ti.com SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018
Product Folder Links: TPS2372
Submit Documentation FeedbackCopyright  2017-2018, Texas Instruments Incorporated
7.4.5 Hardware Classification
Hardware classification allows a PSE to determine a PDs power requirements before powering, and helps with
power management once power is applied. Type 2, 3, and 4 hardware classification permits high power PDs to
determine whether the PSE can support its high-power operation. The number of class cycles generated by the
PSE prior to turn on indicates to the PD if it allots the power requested or if the allocated power is less than
requested, in which case there is power demotion as shown in
Table 3. A Type 2 PD always presents Class 4 in hardware to indicate that it is a 25.5W device. A Class 5 or 6
Type 3 PD presents Class 4 in hardware during the first two class events and it presents Class 0 or 1,
respectively, for all subsequent class events. A Class 7 or 8 Type 4 PD presents Class 4 in hardware during the
first two class events and it presents Class 2 or 3, respectively, for all subsequent class events. A Type 1 PSE
will treat a Class 4 to 8 device like a Class 0 device, allotting 13 W if it chooses to power the PD. A Type 2 PSE
will treat a Class 5 to 8 device like a Class 4 device, allotting 25.5W if it chooses to power the PD. A Class 4 PD
that receives a 2-event class, a Class 5 or 6 PD that receives a 4-event class, or a Class 7 or 8 PD that receives
a 5-event class, understands that the PSE has agreed to allocate the PD requested power. In the case where
there is power demotion, the PD may choose to not start, or to start while not drawing more power than initially
allocated, and request more power through the DLL after startup. The standard requires a Type 2, 3 or 4 PD to
indicate that it is underpowered if this occurs. Startup of a high-power PD at lower power than requested
implicitly requires some form of powering down sections of the application circuits.
The maximum power entries in Table 1 determine the class the PD must advertise. The PSE may disconnect a
PD if it draws more than its stated class power, which may be the hardware class or a DLL-derived power level.
The standard permits the PD to draw limited current peaks that increase the instantaneous power above the
Table 1 limit; however, the average power requirement always applies.
The TPS2372 implements one- to five-event classification. RCLSA and RCLSB resistor values define the class of
the PD. DLL communication is implemented by the Ethernet communication system in the PD and is not
implemented by the TPS2372.
The TPS2372 disables classification above VCU_ON to avoid excessive power dissipation. CLSA/B voltage is
turned off during PD thermal limiting or when DEN is active. The CLSA and CLSB outputs are inherently current-
limited, but should not be shorted to VSS for long periods of time.
Figure 18 shows how classification works for the TPS2372. Transition from state-to-state occurs when
comparator thresholds are crossed (see Figure 15 and Figure 16). These comparators have hysteresis, which
adds inherent memory to the machine. Operation begins at idle (unpowered by PSE) and proceeds with
increasing voltage from left to right. A 2- to 5-event classification follows the (heavy lined) path towards the
bottom, ending up with a latched TPL/TPH decode along the lower branch that is highlighted. Once the valid path
to the PSE detection is broken, the input voltage must transition below the mark reset threshold to start anew.
```

### Page 22

#### Extracted tables

Table 1:

```text
PoE Startup Sequence Operating Between UVLO Mark Class TPH low Ranges Rising TPL open-drain TYPE 3 PSE Hardware Class Between UVLO Ranges Falling |
```

#### Raw extracted text

```text
Detect Class
Mark Class
Mark Class Between
Ranges
Between
Ranges
Operating
TPL/TPH
open-drain
Operating
TPL low
TPH open-drain
Between
Ranges
UVLO
Rising
UVLO
Falling
UVLO
Rising
UVLO
Falling
TYPE 2 or 3 PSE
Hardware Class
Class
TYPE 1 or 3 PSE
Hardware Class
Between
Ranges
PoE Startup Sequence
Mark
Reset
Idle
Mark Class Between
Ranges
Operating
TPL/TPH low
UVLO
Rising
TYPE 4 PSE
Hardware Class
PoE Startup Sequence
Mark Class
Between
Ranges
ClassMark
Mark Class Between
Ranges
Operating
TPH low
TPL open-drain
UVLO
Rising
UVLO
Falling
TYPE 3 PSE
Hardware Class
PoE Startup Sequence
Between
Ranges
ClassMark
TYPE 3 PSE
Hardware Class
UVLO
Falling
Between
Ranges
ClassMark
Autoclass
(AUTCLS = Low)
 & (tCLS > tACS)
22
TPS2372
SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018 www.ti.com
Product Folder Links: TPS2372
Submit Documentation Feedback Copyright  2017-2018, Texas Instruments Incorporated
Figure 18. Up to Five-Event Class Internal States
```

### Page 23

#### Raw extracted text

```text
23
TPS2372
www.ti.com SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018
Product Folder Links: TPS2372
Submit Documentation FeedbackCopyright  2017-2018, Texas Instruments Incorporated
7.4.6 Autoclass
Autoclass is a classification mechanism that allows a PD to communicate its effective maximum power
consumption to the PSE. This happens in such a way that the PSE will be able to set the power budget to the
effective maximum PD power including the effective channel losses and additional margin. This new feature was
introduced in the IEEE802.3bt standard to allow a more efficient use of the available power since only the
effectively used power needs to be budgeted.
A Type 3 or Type 4 PD may optionally support Autoclass whereas a Type 3 or Type 4 PSE may make use of it to
optimize its power management.
A PSE implementing Autoclass uses the first class event to inquire if the PD supports Autoclass, looking for the
class current to fall to class 0 current level after a time tACS, as shown in Figure 17. If it is the case, the PSE can
then proceed to Autoclass measurement immediately after power up, the PD being required to draw its highest
power throughout the period bounded by the next 1.35 second to 3.65 seconds. Note that the average power is
calculated using any sliding window with a width in the range of 150 to 300 ms .
7.4.7 Inrush and Startup
IEEE 802.3bt has a startup current and time limitation, providing compatibility between a PSE of any Type and a
PD of any Type. The PSE inrush limit varies according to the allotted power. If Class 0 to 4, Class 5 to 6 or Class
7 to 8, the inrush limit is respectively from 400 mA to 450 mA, 400 mA to 900 mA or 800 mA to 900 mA. PSE
inrush limit applies for up to 75 ms after power up (applying "48 V" to the PI), after which the Type 2, 3, or 4 PSE
will support a higher output current in accordance with the allocated class. The TPS2372-3 and TPS2372-4
respectively implement a 200-mA and 335-mA inrush current, which is compatible with all PSE Types. A high-
power PD must limit its converter startup peak current. The operational current for Type 2 and 3, and preferably
Type 4, cannot exceed 400 mA for a period of 80 ms.
7.4.8 Maintain Power Signature
The MPS is an electrical signature presented by the PD to assure the PSE that it is still present after operating
voltage is applied. For a Type 1 or Type 2 PD, a valid MPS consists of a minimum dc current of 10 mA, or a 10-
mA pulsed current for at least 75 ms every 325 ms, and an AC impedance lower than 26.3 kOhm in parallel with
0.05 uF. Only Type 1 and Type 2 PSEs monitor the AC MPS. A Type 1 or Type 2 PSE that monitors only the AC
MPS may remove power from the PD.
To enable applications with stringent standby requirements, IEEE802.3bt introduced a significant change
regarding the minimum pulsed current duration to assure the PSE will maintain power. This applies to all Type 3
and Type 4 PSEs, and the pulse duration is ~10% of what is required for Type 1 and 2 PSEs. The MPS current
amplitude requirement for Class 5-8 PDs have also increased to 16 mA at the PSE end of the ethernet cable.
If the current through the RTN-to-VSS path is below ~28 mA, the TPS2372 automatically generates the MPS
pulsed current through the AMPS_CTL output pin, the current amplitude being adjustable with an external
resistor. The TPS2372 is also able to determine if the PSE is of Type 1-2 or Type 3-4, automatically adjusting the
MPS pulse duration and duty-cycle. Note that the IEEE802.3bt requirement for the PD is applicable at the PSE
end of the cable. That means that depending the cable length and other parameters including the bulk
capacitance, a longer MPS duration may be required to ensure a valid MPS. For that purpose, the TPS2372 has
3 different selections of MPS pulse duration and duty-cycle, selectable through the MPS_DUTY input pin.
When DEN is used to force the hotswap switch off, the DC MPS will not be met. A PSE that monitors the DC
MPS will remove power from the PD when this occurs.
7.4.9 Startup and Converter Operation
The internal PoE UVLO (Undervoltage Lock Out) circuit holds the hotswap switch off before the PSE provides full
voltage to the PD. This prevents the downstream converter circuits from loading the PoE input during detection
and classification. The converter circuits will discharge CBULK while the PD is unpowered. Thus V(VDD-RTN) will be
a small voltage just after full voltage is applied to the PD, as seen in Figure 17. The PSE drives the PI voltage to
the operating range once it has decided to power up the PD. When VVDD rises above the UVLO turn-on threshold
(VUVLO_R, approximately 38 V) with RTN high, the TPS2372-3 and TPS2372-4 enables the hotswap MOSFET
with inrush current limit (~200 mA for TPS2372-3 and ~335 mA for TPS2372-4) as seen in Figure 19. The PG
```

### Page 24

#### Extracted tables

Table 1:

```text
V VD | D-R |  | TN |  |  |  |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  | TPH/ |  |  | TPL e |  | nable | d | 
 | V TPH/ |  |  | TPL-RTN |  |  |  |  |  |  |  |  |  |  |  |  | 
 | V PG |  |  | RTN |  |  |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  | soft s |  |  | tart |  |  |  | 
 |  |  |  | d |  |  |  |  |  |  |  |  |  |  |  |  | 
PI p | owere |  |  | d |  |  |  |  |  |  |  |  |  |  |  |  | 
 | I |  |  |  |  |  |  |  |  |  |  |  |  | LED ena | Driv bled | er | 
 |  | I |  | nrush |  |  |  |  |  |  |  |  |  |  |  |  | 
 | (TP | (TP |  | S237 | 2-4) |  |  |  |  |  |  |  |  |  |  |  | 
I PI |  |  |  |  |  |  | MCU | turn |  | on |  |  |  |  |  |  |
```

#### Raw extracted text

```text
Time: 20ms/div
5V/div
200mA/div
IPI
Inrush
(TPS2372-4)
LED Driver
enabled
VVDD-RTN
VPG-RTN
5V/div
50V/div
PI powered
VTPH/TPL-RTN
soft start
TPH/TPL enabled
MCU turn on
24
TPS2372
SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018 www.ti.com
Product Folder Links: TPS2372
Submit Documentation Feedback Copyright  2017-2018, Texas Instruments Incorporated
pin is in low state while CBULK charges and VRTN falls from VVDD to nearly VVSS. PG output is maintained low
during that time, to avoid additional loading between VVDD and VRTN that could prevent successful PD and
subsequent converter start up. Once the inrush current falls about 10% below the inrush current limit, the PD
current limit switches to the operational level (approximately 1.85 A for TPS2372-3 and approximately 2.2 A for
TPS2372-4).
Additionally, as seen in Figure 19 once the inrush period duration has also exceeded ~81.5 ms, if IRSHDL_EN is
open (this delay does not apply if connect to RTN), PG output becomes high impedance, allowing the
downstream converter circuitry to start. In typical lighting applications, this allows a low power converter to start
powering a microcontroller, which subsequently turns ON a high power LED driver. As seen in Figure 20, the
converter soft-start introduces a slight additional delay before the transition to a higher power mode. TPH, TPL
and BT outputs are enabled within tTPLHBT following PG going from low to open.
Figure 19. Power Up and Start
```

### Page 25

#### Extracted tables

Table 1:

```text
PSE Inrus | h
```

Table 2:

```text
Release PG (Soft Start) | PD + Power Supply Fully Operational
```

#### Raw extracted text

```text
PSE Inrush
HSW cap
recharge
Release PG
(Soft Start)
PD Wait
time
Ensures interoperability with
PSE inrush limit
tinrush max
PD + Power Supply Fully
Operational
PSE
PD
Operational Mode
tinrush min
25
TPS2372
www.ti.com SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018
Product Folder Links: TPS2372
Submit Documentation FeedbackCopyright  2017-2018, Texas Instruments Incorporated
Figure 20. Power Up and Start
If VVDD-VVSS drops below the lower PoE UVLO (VUVLO_F, ~32 V), the hotswap switch is turned off, but the PG
output remains high impedance allowing the converter to continue operating until the converter's UVLO threshold
is reached.
7.4.10 PD Hotswap Operation
IEEE802.3bt includes new PSE output limiting requirements for Type 3 and 4 operation to cover higher power
and 4-pair applications. Type 2, 3 and 4 PSEs must meet an output current vs time template with specified
minimum and maximum sourcing boundaries. The peak output current per each 2-pair may be as high as 50 A
for 10 us or 1.75 A for 75 ms, and the total peak current becomes twice these values when power is delivered
over 4 pairs. This makes robust protection of the PD device even more important than it was in IEEE 802.3-2012.
The internal hotswap MOSFET is protected against output faults and input voltage steps with a current limit and
deglitched (time-delay filtered) foldback. An overload on the pass MOSFET engages the current limit, with V(RTN-
VSS) rising as a result. If V(RTN-VSS) rises above approximately 14.5 V for longer than approximately 1.65 ms, the
current limit reverts to the inrush value and PG output is forced low which turns off the converter, although there
is no minimum inrush delay period (81.5-ms) applicable in this case. The 1.65-ms deglitch feature prevents
momentary transients from causing a PD reset, provided that recovery lies within the bounds of the hotswap and
PSE protection. Figure 21 shows an example of the RTN current profile during VDD to RTN short circuit, using 5-
ohm load impedance. The hotswap MOSFET goes into current limit, causing the RTN voltage to increase. Once
VRTN exceeds 14.5 V, IRTN, which was clamped to the current limit drops to the level of inrush current limit after
1.65 ms.
The inrush current limit is also reestablished when V(VDD-VSS) drops below UVLO then rises above it.
```

### Page 26

#### Extracted tables

Table 1:

```text
V R |  |  |  |  |  | 5V |  |  |  |  |  |  |  |  | 
 | V R | TN-VS |  | > 1 S |  | 5V |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  | V R |  |  | S |  |  | 
 |  |  |  |  |  |  |  |  |  | V R | TN-VS | S |  |  | 
 |  |  |  |  |  |  |  |  | VSS |  |  |  |  |  | 
 |  |  |  |  |  |  |  | V PG | VSS |  |  |  |  |  | 
 |  |  |  | Cur |  |  |  |  |  |  |  |  | ush |  | 
 |  |  |  |  |  |  |  |  |  |  |  | Inr | ush |  | 
 |  |  |  |  | Cur | rent L |  | imit |  |  |  |  |  |  | 
 |  |  |  | (TP | (TP | S237 |  | 2-4) |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  | I PI |  |  |  |  |  |  |
```

#### Raw extracted text

```text
Time: 400us/div
5V/div
2A/div
IPI
Inrush
 VRTN-VSS > 15V
VRTN-VSS
VPG-VSS
20V/div
Current Limit
(TPS2372-4)
26
TPS2372
SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018 www.ti.com
Product Folder Links: TPS2372
Submit Documentation Feedback Copyright  2017-2018, Texas Instruments Incorporated
Figure 21. Response to PD Output Short Circuit
The PD control has thermal sensors that protect the internal hotswap MOSFET and the MPS pulsed current
driver. Conditions like startup or operation into a VDD-to-RTN short cause high power dissipation in the MOSFET.
An over-temperature shutdown (OTSD) turns off the hotswap MOSFET, the class regulator, and the MPS driver,
which are restarted after the device cools. The hotswap MOSFET will be re-enabled and the TPS2372 will return
to inrush phase when exiting from an overtemperature event. Pulling DEN to VSS during powered operation
causes the internal hotswap MOSFET to turn off.
The hotswap switch will be forced off under the following conditions:
1. V(DEN -VSS) < VPD-DIS when V(VDD-VSS) is in the operational range,
2. PD is over-temperature, or
3. V(VDD -VSS) < PoE UVLO falling threshold (approximately 32 V).
7.4.11 Startup and Power Management, PG and TPH, TPL, BT
PG (power good or converter enable) is a pin that when at low level indicates when the internal hotswap
MOSFET is in inrush phase. PG goes high impedance when inrush phase is over and can be used to enable a
downstream converter to start up. Common interfaces to the converter controller include the soft-start or enable
pins.
TPH, TPL and BT provide information relative to the PSE Type (1-2 or 3-4) and its allocated power.
The usage of TPH/TPL/BT is demonstrated in Figure 22.
The TPS2372 is also able to interoperate with non standard PoE++ PSE controllers. If powered from a PoE++
PSE controller, the TPH/TPL/BT 3-bit code becomes "Low-Low-High". This also indicates that the PoE++PSE
agreed to deliver the power requested by the TPS2372.
```

### Page 27

#### Raw extracted text

```text
TPS2372
RTN
RCLSA
From Ethernet
Pairs 1,2 VDD
VSS
CLSA
From Ethernet
Pairs 3,4
DEN
PG
TPL
RTPL
RCLSB
CLSB
AMPS_CTL
TPH
RTPH
REF BT
0.1 F
58V
49.9 K
RMPS
RREF
VDDRBT
C1
D1
PoE PD Design
VDD
MPS_DUTY
RDEN
RPG
DC/DC EN
IRSHDL_EN
AUTCLS
Optional
CBULK
+
27
TPS2372
www.ti.com SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018
Product Folder Links: TPS2372
Submit Documentation FeedbackCopyright  2017-2018, Texas Instruments Incorporated
7.4.12 Using DEN to Disable PoE
The DEN pin may be used to turn the PoE hotswap switch off by pulling it to VSS while in the operational state, or
to prevent detection when in the idle state. A low voltage on DEN forces the hotswap MOSFET off during normal
operation. Additional information is available in the Advanced Adapter ORing Solutions using the TPS23753
(SLVA306) application report.
8 Application and Implementation
NOTE
Information in the following applications sections is not part of the TI component
specification, and TI does not warrant its accuracy or completeness. TIs customers are
responsible for determining suitability of components for their purposes. Customers should
validate and test their design implementation to confirm system functionality.
8.1 Application Information
The TPS2372 has the flexibility to be implemented in IEEE802.3bt and PoE++ PDs. Therefore, it can be used in
a wide range applications such as video and VoIP telephones, multiband access points, security cameras, power
modules, LED lighting converters, and pico-base stations.
8.2 Typical Application
Figure 22. Typical Application Circuit
```

### Page 28

#### Extracted tables

Table 1:

```text
PARAMETER | TESTCONDITIONS | MIN | MAX | UNIT
POWERINTERFACE |  |  |  | 
Inputvoltage | PowerappliedthroughPoEoradapter | 0 57 |  | V
Operatingvoltage | Afterstartup | 30 57 |  | V
InputUVLO | Risinginputvoltageatdeviceterminals | 40 |  | V
 | Fallinginputvoltage | 30.5 |  | 
Detectionvoltage | Atdeviceterminals | 1.4 10.1 |  | V
Classificationvoltage | Atdeviceterminals | 11.9 23 |  | V
PDclass8 | ClasssignatureA | 38 42 |  | mA
PDclass8 | ClasssignatureB | 26.5 29.3 |  | mA
Inrushcurrentlimit |  | 275 395 |  | mA
Operatingcurent-limit |  | 1.9 2.5 |  | A
Autoclass |  | Yes |  | 
AutomaticMPS | 12.5%DutyCycleatnoload |  |  | 
Inrushdelay |  | Yes Yes |  |
```

#### Raw extracted text

```text
28
TPS2372
SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018 www.ti.com
Product Folder Links: TPS2372
Submit Documentation Feedback Copyright  2017-2018, Texas Instruments Incorporated
Typical Application (continued)
8.2.1 Design Requirements
For this design example, use the parameters in Table 7 for a PD Class 8 application.
Table 7. Design Parameters
PARAMETER TEST CONDITIONS MIN MAX UNIT
POWER INTERFACE
Input voltage Power applied through PoE or adapter 0 57 V
Operating voltage After startup 30 57 V
Input UVLO
Rising input voltage at device terminals - 40
V
Falling input voltage 30.5 -
Detection voltage At device terminals 1.4 10.1 V
Classification voltage At device terminals 11.9 23 V
PD class 8 Class signature A 38 42 mA
PD class 8 Class signature B 26.5 29.3 mA
Inrush current limit 275 395 mA
Operating curent-limit 1.9 2.5 A
Autoclass Yes
Automatic MPS 12.5% Duty Cycle at no load
Inrush delay Yes Yes
8.2.2 Detailed Design Requirements
8.2.2.1 Input Bridges and Schottky Diodes
Using Schottky diodes instead of PN junction diodes for the PoE input bridges will reduce the power dissipation
in these devices by about 30%. There are, however, some things to consider when using them. The IEEE
standard specifies a maximum backfeed voltage of 2.8 V. A 100-kOhm resistor is placed between the unpowered
pairs and the voltage is measured across the resistor. Schottky diodes often have a higher reverse leakage
current than PN diodes, making this a harder requirement to meet. To compensate, use conservative design for
diode operating temperature, select lower-leakage devices where possible, and match leakage and temperatures
by using packaged bridges.
Schottky diode leakage currents and lower dynamic resistances can impact the detection signature. Setting
reasonable expectations for the temperature range over which the detection signature is accurate is the simplest
solution. Increasing RDET slightly may also help meet the requirement.
Schottky diodes have proven less robust to the stresses of ESD transients than PN junction diodes. After
exposure to ESD, Schottky diodes may become shorted or leak. Take care to provide adequate protection in line
with the exposure levels. This protection may be as simple as ferrite beads and capacitors.
As a general recommendation, use 3-A to 5-A, 100-V rated discrete or bridge diodes for the input rectifiers.
Many high power PoE PD designs require the need for an active FET bridge recitifier in high efficiency
applications. An example of an active FET bridge rectifier design can be found in the TPS2372-4EVM-006 User's
Guide.
8.2.2.2 Protection, D1
A TVS, D1, across the rectified PoE voltage per Figure 22 must be used. TI recommends a SMAJ58A, or
equivalent, is recommended for general indoor applications. If an adapter is connected from VDD to RTN, as in
ORing option 2 above, then voltage transients caused by the input cable inductance ringing with the internal PD
capacitance can occur. Adequate capacitive filtering or a TVS must limit this voltage to within the absolute
maximum ratings. Outdoor transient levels or special applications require additional protection.
```

### Page 29

#### Raw extracted text

```text
TPx-OUT
TPx-MIN TPx
C T FWLED
TPx
TPx
I 0.46 mAI 0.46 mA, Select I 1 mACTR 1.00
V V V 48 V 0.26 V 1.1 VR 46.6 kOhmI 1 mA
/c61 /c61 /c61 /c61
/c45 /c45 /c45 /c45/c61 /c61 /c61
OUT TPx OUT
TPx OUT
TPx OUT
V V 5 0.4I 0.46 mAR 10000
/c45
/c45
/c45
/c45 /c45/c61 /c61 /c61
VDD
TPH/TPL/BT
From TPS2372
RTPx
RTPx-OUT
VOUT
ITPx
29
TPS2372
www.ti.com SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018
Product Folder Links: TPS2372
Submit Documentation FeedbackCopyright  2017-2018, Texas Instruments Incorporated
8.2.2.3 Capacitor, C1
The IEEE 802.3at standard specifies an input bypass capacitor (from VDD to VSS) of 0.05 uF to 0.12 uF. Typically
a 0.1 uF, 100 V, 10% ceramic capacitor is used.
8.2.2.4 Detection Resistor, RDEN
The IEEE 802.3at standard specifies a detection signature resistance, RDEN between 23.7 kOhm and 26.3 kOhm, or 25
kOhm +/- 5%. A resistor of 24.9 kOhm +/- 1% is recommended for RDEN.
8.2.2.5 Classification Resistors, RCLSA and RCLSB
Connect a resistor from CLSA and CLSB to VSS to program the classification current according to the IEEE
802.3bt standard. The class power assigned should correspond to the maximum average power drawn by the
PD during operation. Select RCLSA and RCLSB according to Table 1.
Choose Class 4 for RCLSA = 63.4 Ohm.
Choose Class 3 for RCLSB = 90.9 Ohm.
8.2.2.6 Opto-isolators for TPH, TPL and BT
The TPH, TPL and BT pin are active-low, open-drain outputs, which give an indication about the PSE allocated
power along with its Type. Optocouplers can interface these pins to circuitry on the secondary side of the
converter. A high-gain optocoupler and a high-impedance (for example, CMOS) receiver are recommended.
Design of the optocoupler interface can be accomplished as follows:
See Table 2 to decode PSE Type
Figure 23. TPH, TPL, and BT Interface
A. As shown in Figure 23, let VDD = 48 V, VOUT = 5 V, RTPx-OUT = 10 kOhm, VTPx = 260 mV, VTPx-OUT = 400 mV.
(1)
B. The optocoupler current transfer ratio, CTR, is needed to determine RTPx. A device with a minimum CTR of
100% at 1 mA LED bias current, ITPx, is selected. In practice, CTR will vary with temperature, LED bias
current, and aging, These variations may require some iteration using the CTR-versus-IDIODE curve on the
optocoupler data sheet.
a. The approximate forward voltage of the optocoupler diode, VFWLED, is 1.1 V from the data sheet.
b. Use .
(2)
c. Choose a 46.4 kOhm resistor.
Most applications require that only the PSEs allocated power information (TPH and TPL) is needed for the MCU
or PD load. In this case, the circuitry needed to drive the BT signal is not necessary and the BT pin can be left
floating.
```

### Page 30

#### Raw extracted text

```text
2 2MPS
RMPS
MPS
V MPS Duty Cycle 24 V 26.4%P 115 mWR 1.3 k
u u   :
AMPS _ CTL
MPS
MPS
V 24 VR 1.3 k I 18.5mA   :
30
TPS2372
SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018 www.ti.com
Product Folder Links: TPS2372
Submit Documentation Feedback Copyright  2017-2018, Texas Instruments Incorporated
Some applications such as PoE lighting can benefit from the BT signal to show that the power consumption in
standby operation may not meet regulatory requirements. In non-standard PoE applications, BT is used with TPH
and TPL to indicate a PoE++ PSE.
8.2.2.7 Automatic MPS and MPS Duty Cycle, RMPS and RMPS_DUTY
MPS_DUTY should be short circuited to VSS for 12.5% duty cycle
(3)
(4)
Choose 1.3 kOhm rated for 1/8 W
26.4% duty cycle is chosen to take into account if the PD is connected to a IEEE802.3at PSE with a longer
MPS timing specification.
For applications that require ultra-low power consumption, such as PoE Lighting, a shorter MPS duty-cycle can
be used. For example, a 5.4% MPS duty cycle can be selected by leaving the MPS_DUTY pin open. Refer to
Table 4 for MPS duty-cycle selection.
8.2.2.8 Internal Voltage Reference, RREF
Per Recommended Operating Conditions,
Choose RREF = 49.9 kOhm
8.2.2.9 Autoclass
To enable Autoclass, AUTOCLS pin should be connected to VSS.
8.2.2.10 Inrush Delay
To enable the 80-ms inrush delay, IRSHDL_EN pin should be open
```

### Page 31

#### Extracted tables

Table 1:

```text
Figure24.Startup | Figure25.StartupandPGDelay
Figure26.AutoMPS | Figure27.OvercurrentResponse
```

#### Raw extracted text

```text
31
TPS2372
www.ti.com SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018
Product Folder Links: TPS2372
Submit Documentation FeedbackCopyright  2017-2018, Texas Instruments Incorporated
8.2.3 Application Curves
Figure 24. Startup Figure 25. Startup and PG Delay
Figure 26. Auto MPS Figure 27. Overcurrent Response
```

### Page 32

#### Raw extracted text

```text
32
TPS2372
SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018 www.ti.com
Product Folder Links: TPS2372
Submit Documentation Feedback Copyright  2017-2018, Texas Instruments Incorporated
9 Power Supply Recommendations
The TPS2372 device will typically be followed by a power supply such as an isolated flyback or active clamp
forward converter or a non-isolated buck converter. The input voltage of the converter should be capable of
operating within the IEEE802.3bt recommended input voltage as shown in Table 6.
10 Layout
10.1 Layout Guidelines
The layout of the PoE front end should follow power and EMI/ESD best practice guidelines. A basic set of
recommendations include:
* Parts placement must be driven by power flow in a point-to-point manner; RJ-45, Ethernet transformer, diode
bridges, TVS and 0.1-uF capacitor, and TPS2372.
* All leads should be as short as possible with wide power traces and paired signal and return.
* There should not be any crossovers of signals from one part of the flow to another.
* Spacing consistent with safety standards like IEC60950 must be observed between the 48-V input voltage
rails and between the input and an isolated converter output.
* The TPS2372 should be located over split, local ground planes referenced to VSS for the PoE input and to
RTN for the switched output.
* Large copper fills and traces should be used on SMT power-dissipating devices, and wide traces or overlay
copper fills should be used in the power path.
* Nine vias are recommended on the Exposed Thermal Pad of the TPS2372. These should connect to all
layers of a copper plane on the PCB. Ensure 80% printed solder coverage by area.
10.2 Layout Example
Figure 28 and Figure 29 show the top and bottom layer and assemblies of the TPS2372-4EVM-006 as a
reference for optimum parts placement. A detailed PCB layout can be found in the users guide of the TPS2372-
4EVM-006 Evaluation Module (SLVUB75).
```

### Page 33

#### Raw extracted text

```text
33
TPS2372
www.ti.com SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018
Product Folder Links: TPS2372
Submit Documentation FeedbackCopyright  2017-2018, Texas Instruments Incorporated
Layout Example (continued)
Figure 28. TPS2372-4EVM-006 Top Side Layout and Component Placement
```

### Page 34

#### Raw extracted text

```text
34
TPS2372
SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018 www.ti.com
Product Folder Links: TPS2372
Submit Documentation Feedback Copyright  2017-2018, Texas Instruments Incorporated
Layout Example (continued)
Figure 29. TPS2372-4EVM-006 Bottom Side Layout and Component Placement
10.3 EMI Containment
* Use compact loops for dv/dt and di/dt circuit paths (power loops and gate drives).
* Use minimal, yet thermally adequate, copper areas for heat sinking of components tied to switching nodes
(minimize exposed radiating surface).
* Use copper ground planes (possible stitching) and top layer copper floods (surround circuitry with ground
floods).
* Use 4 layer PCB if economically feasible (for better grounding).
* Minimize the amount of copper area associated with input traces (to minimize radiated pickup).
* Use Bob Smith terminations, Bob Smith EFT capacitor, and Bob Smith plane.
* Use Bob Smith plane as ground shield on input side of PCB (creating a phantom or literal earth ground).
* Use of ferrite beads on input (allow for possible use of beads or 0-Ohm resistors).
* Maintain physical separation between input-related circuitry and power circuitry (use ferrite beads as
boundary line).
* Possible use of common-mode inductors.
* Possible use of integrated RJ-45 jacks (shielded with internal transformer and Bob Smith terminations).
* End-product enclosure considerations (shielding).
```

### Page 35

#### Extracted tables

Table 1:

```text
PARTS | PRODUCTFOLDER | SAMPLE&BUY | TECHNICAL DOCUMENTS | TOOLS& SOFTWARE | SUPPORT& COMMUNITY
TPS2372-3 | Clickhere | Clickhere | Clickhere | Clickhere | Clickhere
TPS2372-4 | Clickhere | Clickhere | Clickhere | Clickhere | Clickhere
```

#### Raw extracted text

```text
35
TPS2372
www.ti.com SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018
Product Folder Links: TPS2372
Submit Documentation FeedbackCopyright  2017-2018, Texas Instruments Incorporated
10.4 Thermal Considerations and OTSD
Sources of nearby local PCB heating should be considered during the thermal design. Typical calculations
assume that the TPS2372 is the only heat source contributing to the PCB temperature rise. It is possible for a
normally operating TPS2372 device to experience an OTSD event if it is excessively heated by a nearby device.
10.5 ESD
ESD requirements for a unit that incorporates the TPS2372 have a much broader scope and operational
implications than are used in TIs testing. Unit-level requirements should not be confused with reference design
testing that only validates the ruggedness of the TPS2372.
11 Device and Documentation Support
11.1 Documentation Support
11.1.1 Related Links
The table below lists quick access links. Categories include technical documents, support and community
resources, tools and software, and quick access to sample or buy.
Table 8. Related Links
PARTS PRODUCT FOLDER SAMPLE & BUY TECHNICAL
DOCUMENTS
TOOLS &
SOFTWARE
SUPPORT &
COMMUNITY
TPS2372-3 Click here Click here Click here Click here Click here
TPS2372-4 Click here Click here Click here Click here Click here
11.1.2 Related Documentation
For related documentation see the following:
* Advanced Adapter ORing Solutions using the TPS23753, SLVA306
11.2 Receiving Notification of Documentation Updates
To receive notification of documentation updates, navigate to the device product folder on ti.com. In the upper
right corner, click on Alert me to register and receive a weekly digest of any product information that has
changed. For change details, review the revision history included in any revised document.
11.3 Community Resources
The following links connect to TI community resources. Linked contents are provided "AS IS" by the respective
contributors. They do not constitute TI specifications and do not necessarily reflect TI's views; see TI's Terms of
Use.
TI E2E(TM) Online Community TI's Engineer-to-Engineer (E2E) Community. Created to foster collaboration
among engineers. At e2e.ti.com, you can ask questions, share knowledge, explore ideas and help
solve problems with fellow engineers.
Design Support TI's Design Support Quickly find helpful E2E forums along with design support tools and
contact information for technical support.
11.4 Trademarks
E2E is a trademark of Texas Instruments.
11.5 Electrostatic Discharge Caution
These devices have limited built-in ESD protection. The leads should be shorted together or the device placed in conductive foam
during storage or handling to prevent electrostatic damage to the MOS gates.
```

### Page 36

#### Raw extracted text

```text
36
TPS2372
SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018 www.ti.com
Product Folder Links: TPS2372
Submit Documentation Feedback Copyright  2017-2018, Texas Instruments Incorporated
11.6 Glossary
SLYZ022 - TI Glossary.
This glossary lists and explains terms, acronyms, and definitions.
12 Mechanical, Packaging, and Orderable Information
The following pages include mechanical, packaging, and orderable information. This information is the most
current data available for the designated devices. This data is subject to change without notice and revision of
this document. For browser-based versions of this data sheet, refer to the left-hand navigation.
```

### Page 37

#### Extracted tables

Table 1:

```text
DIMENSION A | 
OPTION 01 | (0.1)
OPTION 02 | (0.2)
```

Table 2:

```text
| 0.08
```

Table 3:

```text
21 |
```

Table 4:

```text
| 0.1 | C | A | B
 | 0.05 |  |  |
```

#### Raw extracted text

```text
www.ti.com
PACKAGE OUTLINE
C
20X 0.38
0.23
2.2 0.1
20X 0.65
0.45
1 MAX
(DIM A) TYP
OPT 01 SHOWN
0.05
0.00
16X 0.65
2X
2.6
2X 2.6
A 5.1
4.9
B
5.1
4.9
VQFN - 1 mm max heightRGW0020B
PLASTIC QUAD FLATPACK - NO LEAD
4222816/A 06/2016
OPTION 01 (0.1)
DIMENSION A
OPTION 02 (0.2)
PIN 1 INDEX AREA
0.08
SEATING PLANE
1
5
11
15
6 10
20 16(OPTIONAL)
PIN 1 ID 0.1 C A B
0.05
EXPOSED
THERMAL PAD
21
NOTES:
1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. The package thermal pad must be soldered to the printed circuit board for thermal and mechanical performance.
SCALE  3.000
37
TPS2372
www.ti.com SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018
Product Folder Links: TPS2372
Submit Documentation FeedbackCopyright  2017-2018, Texas Instruments Incorporated
```

### Page 38

#### Raw extracted text

```text
www.ti.com
EXAMPLE BOARD LAYOUT
(0.85)
0.07 MIN
ALL AROUND
0.07 MAX
ALL AROUND
20X (0.31)
20X (0.75)
( 0.2) TYP
VIA
16X (0.65)
(4.65)
(4.65)
(0.85)
( 2.2)
(R0.05)
TYP
VQFN - 1 mm max heightRGW0020B
PLASTIC QUAD FLATPACK - NO LEAD
4222816/A 06/2016
SYMM
1
5
6 10
11
15
1620
SYMM
LAND PATTERN EXAMPLE
SCALE:15X
21
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
METAL
SOLDER MASK
OPENING
NON SOLDER MASK
SOLDER MASK DETAILS
DEFINED
(PREFERRED)
38
TPS2372
SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018 www.ti.com
Product Folder Links: TPS2372
Submit Documentation Feedback Copyright  2017-2018, Texas Instruments Incorporated
```

### Page 39

#### Raw extracted text

```text
www.ti.com
EXAMPLE STENCIL DESIGN
(0.59) TYP
20X (0.75)
20X (0.31)
16X (0.65)
(4.65)
(4.65)
4X ( 0.98)
(0.59) TYP(R0.05) TYP
VQFN - 1 mm max heightRGW0020B
PLASTIC QUAD FLATPACK - NO LEAD
4222816/A 06/2016
NOTES: (continued)
6. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
design recommendations.
SYMM
METAL
TYP
BASED ON 0.125 mm THICK STENCIL
SOLDER PASTE EXAMPLE
EXPOSED PAD
80% PRINTED SOLDER COVERAGE BY AREA
SCALE:20X
SYMM
1
5
6 10
11
15
1620
21
39
TPS2372
www.ti.com SLUSCM4B - OCTOBER 2017 - REVISED NOVEMBER 2018
Product Folder Links: TPS2372
Submit Documentation FeedbackCopyright  2017-2018, Texas Instruments Incorporated
```

### Page 40

#### Extracted tables

Table 1:

```text
Orderable part number | Status (1) | Material type (2) | Package | Pins | Package qty | Carrier | RoHS (3) | Lead finish/ Ball material (4) | MSL rating/ Peak reflow (5) | Op temp ( deg C) | Part marking (6)
TPS2372-3RGWR | Active | Production | VQFN (RGW) | 20 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | TPS 2372-3
TPS2372-3RGWR.A | Active | Production | VQFN (RGW) | 20 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | TPS 2372-3
TPS2372-3RGWT | Active | Production | VQFN (RGW) | 20 | 250 | SMALL T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | TPS 2372-3
TPS2372-3RGWT.A | Active | Production | VQFN (RGW) | 20 | 250 | SMALL T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | TPS 2372-3
TPS2372-4RGWR | Active | Production | VQFN (RGW) | 20 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | TPS 2372-4
TPS2372-4RGWR.A | Active | Production | VQFN (RGW) | 20 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | TPS 2372-4
TPS2372-4RGWT | Active | Production | VQFN (RGW) | 20 | 250 | SMALL T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | TPS 2372-4
TPS2372-4RGWT.A | Active | Production | VQFN (RGW) | 20 | 250 | SMALL T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | TPS 2372-4
```

#### Raw extracted text

```text
PACKAGE OPTION ADDENDUM
www.ti.com 10-Nov-2025
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
TPS2372-3RGWR Active Production VQFN (RGW) | 20 3000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 TPS
2372-3
TPS2372-3RGWR.A Active Production VQFN (RGW) | 20 3000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 TPS
2372-3
TPS2372-3RGWT Active Production VQFN (RGW) | 20 250 | SMALL T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 TPS
2372-3
TPS2372-3RGWT.A Active Production VQFN (RGW) | 20 250 | SMALL T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 TPS
2372-3
TPS2372-4RGWR Active Production VQFN (RGW) | 20 3000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 TPS
2372-4
TPS2372-4RGWR.A Active Production VQFN (RGW) | 20 3000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 TPS
2372-4
TPS2372-4RGWT Active Production VQFN (RGW) | 20 250 | SMALL T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 TPS
2372-4
TPS2372-4RGWT.A Active Production VQFN (RGW) | 20 250 | SMALL T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 TPS
2372-4

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

### Page 41

#### Raw extracted text

```text
PACKAGE OPTION ADDENDUM
www.ti.com 10-Nov-2025
Multiple part markings will be inside parentheses. Only one part marking contained in parentheses and separated by a "~" will appear on a part. If a line is indented then it is a continuation of the previous line and the two
combined represent the entire part marking for that device.

Important Information and Disclaimer:The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and
makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative
and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers
and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.

Addendum-Page 2
```

### Page 42

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
TPS2372-3RGWR | VQFN | RGW | 20 | 3000 | 330.0 | 12.4 | 5.3 | 5.3 | 1.1 | 8.0 | 12.0 | Q2
TPS2372-3RGWT | VQFN | RGW | 20 | 250 | 180.0 | 12.4 | 5.3 | 5.3 | 1.1 | 8.0 | 12.0 | Q2
TPS2372-4RGWR | VQFN | RGW | 20 | 3000 | 330.0 | 12.4 | 5.3 | 5.3 | 1.1 | 8.0 | 12.0 | Q2
TPS2372-4RGWT | VQFN | RGW | 20 | 250 | 180.0 | 12.4 | 5.3 | 5.3 | 1.1 | 8.0 | 12.0 | Q2
```

#### Raw extracted text

```text
PACKAGE MATERIALS INFORMATION
www.ti.com 3-Jun-2022
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
TPS2372-3RGWR VQFN RGW 20 3000 330.0 12.4 5.3 5.3 1.1 8.0 12.0 Q2
TPS2372-3RGWT VQFN RGW 20 250 180.0 12.4 5.3 5.3 1.1 8.0 12.0 Q2
TPS2372-4RGWR VQFN RGW 20 3000 330.0 12.4 5.3 5.3 1.1 8.0 12.0 Q2
TPS2372-4RGWT VQFN RGW 20 250 180.0 12.4 5.3 5.3 1.1 8.0 12.0 Q2
Pack Materials-Page 1
```

### Page 43

#### Extracted tables

Table 1:

```text
| H
```

Table 2:

```text
Device | Package Type | Package Drawing | Pins | SPQ | Length (mm) | Width (mm) | Height (mm)
TPS2372-3RGWR | VQFN | RGW | 20 | 3000 | 367.0 | 367.0 | 35.0
TPS2372-3RGWT | VQFN | RGW | 20 | 250 | 210.0 | 185.0 | 35.0
TPS2372-4RGWR | VQFN | RGW | 20 | 3000 | 367.0 | 367.0 | 35.0
TPS2372-4RGWT | VQFN | RGW | 20 | 250 | 210.0 | 185.0 | 35.0
```

#### Raw extracted text

```text
PACKAGE MATERIALS INFORMATION

www.ti.com 3-Jun-2022
TAPE AND REEL BOX DIMENSIONS
Width (mm)
W LH

*All dimensions are nominal
Device Package Type Package Drawing Pins SPQ Length (mm) Width (mm) Height (mm)
TPS2372-3RGWR VQFN RGW 20 3000 367.0 367.0 35.0
TPS2372-3RGWT VQFN RGW 20 250 210.0 185.0 35.0
TPS2372-4RGWR VQFN RGW 20 3000 367.0 367.0 35.0
TPS2372-4RGWT VQFN RGW 20 250 210.0 185.0 35.0
Pack Materials-Page 2
```

### Page 44

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
Copyright  2025, Texas Instruments Incorporated
Last updated 10/2025
```
