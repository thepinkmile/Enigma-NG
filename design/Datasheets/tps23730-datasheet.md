# TPS23730 IEEE 802.3bt Type 3 PoE PD with High Efficiency DC-DC Controller datasheet (Rev. B)

## Source

- Source PDF: [tps23730-datasheet.pdf](tps23730-datasheet.pdf)
- Generated Markdown: `tps23730-datasheet.md`
- Page count: 59
- Conversion method: automated local extraction with pypdf and pdfplumber

## Extracted title and part identity

- TPS23730 IEEE 802.3bt Type 3 PoE PD with High Efficiency DC-DC Controller datasheet (Rev. B)
- tps23730 datasheet
- TPS23730
- SLVSER6B
- TLV431
- TPS23731
- TPS23734

## Extraction summary

- Pages with substantial text extraction: 58/59
- Pages with extracted tables: 37/59
- Total extracted character count: 175321
- Extraction quality flag: usable

## PDF metadata

| Field | Value |
| --- | --- |
| Title | TPS23730 IEEE 802.3bt Type 3 PoE PD with High Efficiency DC-DC Controller datasheet (Rev. B) |
| Author | Texas Instruments, Incorporated [SLVSER6,B ] |
| Subject | Data Sheet |
| Creator | AH XSL Formatter V7.0 MR5 for Windows (x64) : 7.0.6.47833 (2020-10-21T14:40+09) |
| Producer | iText 2.1.7 by 1T3XT |

## Reviewed summary

### Curated design notes

- PDF review confirmed this is the TI TPS23730 PoE PD interface plus DC-DC controller datasheet for a 45-pin 7.00 mm x 5.00 mm VQFN package.
- The simplified application on page 1 is important enough to summarize explicitly: DEN provides the PoE detection path, CLSA/CLSB set the hardware
  classification currents, APD and PPD handle adapter-priority ORing options, FRS sets the switching frequency with resistor RFRS, DTHR uses CDTR plus
  a resistor to FRS for programmable frequency dithering, and the DC-DC section supports flyback and active-clamp-forward topologies.
- Pin-function details that are easy to miss in raw extraction: DTHR sets the modulation frequency when tied to a capacitor to RTN and a resistor to
  FRS, FRS sets the free-running switch frequency, REF needs a 49.9 kOhm 1% resistor to VSS, and DEN uses a 25.5 kOhm resistor to VDD for the
  detection signature.
- The PDF does include design equations. Equation 2 gives RFRS (kOhm) = 15000 / fSW (kHz). Equation 3 gives CDTR = 3 x RFRS / (2.052 x fm), with fm in
  hertz and the guidance that fm should stay above 9 kHz for conducted-EMI measurements.
- Application/reference-design content is also significant: Figure 8-15 compares three adapter ORing locations, page 42 explains why option 2 is the
  usual adapter-priority choice, and the detailed-design example later in the datasheet uses a 250 kHz switching target with a selected 60.4 kOhm RFRS
  value.
- Core operating features from the PDF include a 100 V, 0.3 ohm internal hotswap switch, automatic MPS with auto-stretch, programmable dead time,
  soft-start plus soft-stop control, and support for up to 60 W PoE designs.
- Extraction limit: several schematics and timing plots are figure-dominant, but the equations, resistor values, and ORing guidance above are now
  captured in plain text while the raw extraction below remains locally searchable.

## Design-relevant extracted content

This section surfaces design-relevant snippets first. Full page-by-page raw extraction follows later for local search.

### Part number and ordering information

- * Redundant Power Feeds or Power Sharing adjusts its pulsed current amplitude and duration / according to PSE Type and system conditions, to / maintain power while minimizing consumption. / Device Information(1) / PART NUMBER PACKAGE BODY SIZE (NOM) / TPS23730 VQFN (45) 7.00 mm x 5.00 mm / (1) For all available packages, see the orderable addendum at
- according to PSE Type and system conditions, to / maintain power while minimizing consumption. / Device Information(1) / PART NUMBER PACKAGE BODY SIZE (NOM) / TPS23730 VQFN (45) 7.00 mm x 5.00 mm / (1) For all available packages, see the orderable addendum at / the end of the data sheet.
- Device Information(1) / PART NUMBER PACKAGE BODY SIZE (NOM) / TPS23730 VQFN (45) 7.00 mm x 5.00 mm / (1) For all available packages, see the orderable addendum at / the end of the data sheet. / T1 / tsernermehrotEfs mnaorrTF
- 12.3 Trademarks.............................................................51 / 12.4 Electrostatic Discharge Caution..............................51 / 12.5 Glossary..................................................................51 / 13 Mechanical, Packaging, and Orderable / Information.................................................................... 51 / 4 Revision History / NOTE: Page numbers for previous revisions may differ from page numbers in the current version.
- 4 Revision History / NOTE: Page numbers for previous revisions may differ from page numbers in the current version. / Changes from Revision A (September 2020) to Revision B (November 2020) Page / * Updated package type in Device Information table............................................................................................ 1 / * Updated package type in pinout drawing caption...............................................................................................3 / * Updated package type in Thermal Information table..........................................................................................6 / Changes from Revision * (May 2020) to Revision A (September 2020) Page
- Basic PoE PD functionality supported includes detection, hardware classification, and inrush current limit during / startup. DC-DC converter features include startup function and current mode control operation. The TPS23730 / device integrates a low 0.3-Ohm internal switch to minimize heat dissipation and maximize power utilization. / A number of input voltage Oring options or input voltage ranges are also supported by use of APD and PPD / inputs. / The TPS23730 device contains several protection features such as thermal shutdown, current limit foldback, and / a robust 100-V internal return switch.
- 8.4.1 PoE Overview / The following text is intended as an aid in understanding the operation of the TPS23730, but it is not a substitute / for the actual IEEE 802.3bt or 802.3at standards. The IEEE 802.3bt standard is an update to IEEE 802.3-2018, / adding Clause 145 (PoE), including power delivery using all four pairs, high-power options, additional features to / reduce standby power consumption and enhanced classification. / Generally speaking, a device compliant to IEEE 802.3-2012 is referred to as a Type 1 (Class 0-3) or 2 (Class / 4) device, and devices with higher power and enhanced classification is referred to as Type 3 (Class 5, 6) or
- 10. Must not draw more than 51 W if it has not received at least 5 classification events or received permission / through DLL. / 11. Must meet various operating and transient templates. / 12. Optionally monitor for the presence or absence of an adapter. / As a result of these requirements, the PD must be able to dynamically control its loading, and monitor TPL and / TPH for changes. TPH and TPL can also be used in cases where the design needs to know specifically if an / adapter is plugged in and operational.
- solution adds cost and complexity, but allows a product to be used if PoE is not available in a particular / installation. While most applications only require that the PD operate when both sources are present, the / TPS23730 device supports forced operation from either of the power sources. Figure 8-15 illustrates three / options for diode ORing external power into a PD. Only one option would be used in any particular design. / Option 1 applies power to the device input, option 2 applies power between the device PoE section and / the power circuit, and option 3 applies power to the output side of the converter. Each of these options / has advantages and disadvantages. A detailed discussion of the device and ORing solutions is covered in
- installation. While most applications only require that the PD operate when both sources are present, the / TPS23730 device supports forced operation from either of the power sources. Figure 8-15 illustrates three / options for diode ORing external power into a PD. Only one option would be used in any particular design. / Option 1 applies power to the device input, option 2 applies power between the device PoE section and / the power circuit, and option 3 applies power to the output side of the converter. Each of these options / has advantages and disadvantages. A detailed discussion of the device and ORing solutions is covered in / application note Advanced Adapter ORing Solutions using the TPS23753, (SLVA306).
- TPS23730 device supports forced operation from either of the power sources. Figure 8-15 illustrates three / options for diode ORing external power into a PD. Only one option would be used in any particular design. / Option 1 applies power to the device input, option 2 applies power between the device PoE section and / the power circuit, and option 3 applies power to the output side of the converter. Each of these options / has advantages and disadvantages. A detailed discussion of the device and ORing solutions is covered in / application note Advanced Adapter ORing Solutions using the TPS23753, (SLVA306). / tenrehtE
- sremrofsnarT Power / Circuit / Adapter Adapter Adapter / Option 1 Option 2 Option 3 / Figure 8-15. ORing Configurations / tenrehtE / morF
- SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020 www.ti.com / R / PPD1 / Figure 8-16. Low-Voltage Option 1 ORing / Preference of one power source presents a number of challenges. Combinations of adapter output voltage / (nominal and tolerance), power insertion point, and which source is preferred determine solution complexity. / Several factors contributing to the complexity are the natural high-voltage selection of diode ORing (the simplest
- for operation and reliability). Creating simple and seamless solutions is difficult if not impossible for many of the / combinations. However, the TPS23730 device offers several built-in features that simplify some combinations. / Several examples demonstrate the limitations inherent in ORing solutions. Diode ORing a 48-V adapter with / PoE (option 1) presents the problem that either source may have the higher voltage. A blocking switch would / be required to assure that one source dominates. A second example is combining a 12-V adapter with PoE / using option 2. The converter draws approximately four times the current at 12 V from the adapter than it does / from PoE at 48 V. Transition from adapter power to PoE may demand more current than can be supplied by the
- Several examples demonstrate the limitations inherent in ORing solutions. Diode ORing a 48-V adapter with / PoE (option 1) presents the problem that either source may have the higher voltage. A blocking switch would / be required to assure that one source dominates. A second example is combining a 12-V adapter with PoE / using option 2. The converter draws approximately four times the current at 12 V from the adapter than it does / from PoE at 48 V. Transition from adapter power to PoE may demand more current than can be supplied by the / PSE. The converter must be turned off while C capacitance charges, with a subsequent converter restart at the / IN
- from PoE at 48 V. Transition from adapter power to PoE may demand more current than can be supplied by the / PSE. The converter must be turned off while C capacitance charges, with a subsequent converter restart at the / IN / higher voltage and lower input current. A third example is use of a 24-V adapter with ORing option 1. The PD / hotswap would have to handle two times the current, and have 1/4 the resistance (be 4 times larger) to dissipate / equal power. / The most popular preferential ORing scheme is option 2 with adapter priority. The hotswap MOSFET is disabled
- higher voltage and lower input current. A third example is use of a 24-V adapter with ORing option 1. The PD / hotswap would have to handle two times the current, and have 1/4 the resistance (be 4 times larger) to dissipate / equal power. / The most popular preferential ORing scheme is option 2 with adapter priority. The hotswap MOSFET is disabled / when the adapter is used to pull APD high, blocking the PoE source from powering the output. This solution / works well with a wide range of adapter voltages, is simple, and requires few external parts. When the AC / power fails, or the adapter is removed, the hotswap switch is enabled. In the simplest implementation, the PD
- works well with a wide range of adapter voltages, is simple, and requires few external parts. When the AC / power fails, or the adapter is removed, the hotswap switch is enabled. In the simplest implementation, the PD / momentarily loses power until the PSE completes its start-up cycle. / The DEN pin can be used to disable the PoE input when ORing with option 3. This is an adapter priority / implementation. Pulling DEN low, while creating an invalid detection signature, disables the hotswap MOSFET, / and prevents the PD from redetecting. This would typically be accomplished with an optocoupler that is driven / from the secondary side of the converter. Another option 3 alternative which does not require DEN optocoupler is

### Pin, pad, and terminal designations

- 3 Description.......................................................................1 / 4 Revision History.............................................................. 2 / 5 Device Comparison Table...............................................3 / 6 Pin Configuration and Functions...................................3 / 7 Specifications.................................................................. 6 / 7.1 Absolute Maximum Ratings ....................................... 6 / 7.2 ESD Ratings .............................................................. 6
- 7.7 Typical Characteristics..............................................14 / 8 Detailed Description......................................................18 / 8.1 Overview...................................................................18 / 8.2 Functional Block Diagram.........................................19 / 8.3 Feature Description...................................................20 / 8.4 Device Functional Modes..........................................29 / 9 Application and Implementation..................................44
- 8.1 Overview...................................................................18 / 8.2 Functional Block Diagram.........................................19 / 8.3 Feature Description...................................................20 / 8.4 Device Functional Modes..........................................29 / 9 Application and Implementation..................................44 / 9.1 Application Information............................................. 44 / 9.2 Typical Application.................................................... 44
- NOTE: Page numbers for previous revisions may differ from page numbers in the current version. / Changes from Revision A (September 2020) to Revision B (November 2020) Page / * Updated package type in Device Information table............................................................................................ 1 / * Updated package type in pinout drawing caption...............................................................................................3 / * Updated package type in Thermal Information table..........................................................................................6 / Changes from Revision * (May 2020) to Revision A (September 2020) Page / * Updated the numbering format for tables, figures and cross-references throughout the document...................1
- PoE allocated power and AUX power TPH/TPL (parallel) or TPL / T2P, APDO T2P, APDO / indicator(s) (serial) / 6 Pin Configuration and Functions / 45 44 43 42 / 4 32 / 5 31
- EA_DIS / TPS23730 / www.ti.com SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020 / PAD_G / NC 10 / PAD_S / Figure 6-1. RMT Package 45-Pin VQFN Top View
- www.ti.com SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020 / PAD_G / NC 10 / PAD_S / Figure 6-1. RMT Package 45-Pin VQFN Top View / Copyright 2022 Texas Instruments Incorporated Submit Document Feedback 3 / Product Folder Links: TPS23730
- PAD_G / NC 10 / PAD_S / Figure 6-1. RMT Package 45-Pin VQFN Top View / Copyright 2022 Texas Instruments Incorporated Submit Document Feedback 3 / Product Folder Links: TPS23730 / KEY FEATURES | TPS23730 | TPS23731 | TPS23734
- 22 / TPS23730 / SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020 www.ti.com / Table 6-1. Pin Functions / PIN / I/O DESCRIPTION / NO. NAME
- TPS23730 / SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020 www.ti.com / Table 6-1. Pin Functions / PIN / I/O DESCRIPTION / NO. NAME / DC-DC controller current sense input. Connect directly to the external power current sense
- SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020 www.ti.com / Table 6-1. Pin Functions / PIN / I/O DESCRIPTION / NO. NAME / DC-DC controller current sense input. Connect directly to the external power current sense / 1 CS I/O
- I/O DESCRIPTION / NO. NAME / DC-DC controller current sense input. Connect directly to the external power current sense / 1 CS I/O / resistor. / 2 AGND - AGND is the DC-DC converter analog return. Tie to RTN and GND on the circuit board. / Used for spread spectrum frequency dithering. Connect a capacitor (determines the modulating
- 2 AGND - AGND is the DC-DC converter analog return. Tie to RTN and GND on the circuit board. / Used for spread spectrum frequency dithering. Connect a capacitor (determines the modulating / 3 DTHR O frequency) from DTHR to RTN and a resistor (determines the amount of dithering) from DTHR to / FRS. If dithering is not used, short DTHR to VB pin. / This pin controls the switching frequency of the DC-DC converter. Tie a resistor from this pin to / 4 FRS I / RTN to set the frequency.
- Used for spread spectrum frequency dithering. Connect a capacitor (determines the modulating / 3 DTHR O frequency) from DTHR to RTN and a resistor (determines the amount of dithering) from DTHR to / FRS. If dithering is not used, short DTHR to VB pin. / This pin controls the switching frequency of the DC-DC converter. Tie a resistor from this pin to / 4 FRS I / RTN to set the frequency. / Primary auxiliary power detect input. Raise 1.5 V above RTN to disable pass MOSFET, also
- 13 TPH O TPH/TPL binary code indicates the PSE allocated power output. Open-drain, active-low outputs / referenced to RTN. The default operation is with parallel binary code. Also, whenever an auxiliary / power adapter is detected via the APD input or PPD input, both TPH and TPL pull low. Serial / 14 TPL O code over TPL can also be enabled by tying SCDIS pin to VSS. In this case, TPH becomes high / impedance. / 17 REF O Internal 1.25-V voltage reference. Connect a 49.9-kOhm_1% resistor from REF to VSS. / TPL serial code disable, referenced to VSS. Leave open to select parallel TPH/TPL configuration.
- 23 VDD / Bypass with a 0.1 uF to VSS and protect with a TVS. / Connect a 25.5-kOhm resistor from DEN to VDD to provide the PoE detection signature. Pulling this / 24 DEN I/O / pin to VSS during powered operation causes the internal hotswap MOSFET to turn off. / 27, 28 VSS - Negative power rail derived from the PoE source. / 30 TEST O Used internally for test purposes only. Leave open.
- Bypass with a 0.1 uF to VSS and protect with a TVS. / Connect a 25.5-kOhm resistor from DEN to VDD to provide the PoE detection signature. Pulling this / 24 DEN I/O / pin to VSS during powered operation causes the internal hotswap MOSFET to turn off. / 27, 28 VSS - Negative power rail derived from the PoE source. / 30 TEST O Used internally for test purposes only. Leave open. / Connect a resistor from DT to AGND to set the GATE to GAT2 dead time. Tie DT to VB to disable
- Connect a resistor from DT to AGND to set the GATE to GAT2 dead time. Tie DT to VB to disable / 31 DT I / GAT2 operation. / This pin sets the SST discharge current during a soft-stop event independently from the setting / 32 I_STP I used during a regular soft-start event. Connect a resistor from this pin to AGND to set the DC/DC / soft-stop rate. / A capacitor from SST to RTN pin sets the soft-start (I charge current) and the hiccup timer (I

### Specifications, ratings, and operating conditions

- 1 Features 3 Description / * Complete IEEE 802.3bt Type 3 (Class 1-6) PoE The TPS23730 device combines a Power over / PD Solution Ethernet (PoE) powered device (PD) interface, and a / EA Gen 2 logo-ready (PoE 2 PD Controller) current-mode DC-DC controller optimized for flyback / Robust 100-V, 0.3-Ohm (typ) Hotswap MOSFET and active clamp forward (ACF) switching regulator / Supports power levels for up to 60-W operation designs . In the case of flyback configuration, the use / Allocated power indicator outputs - parallel or of primary-side regulation (PSR) is supported. The
- Soft-stop shutdown / Adjustable frequency with synchronization The PSR feature of the DC-DC controller uses / Programmable frequency dithering for EMI feedback from an auxiliary winding for control of / * Automatic Maintain Power Signature (MPS) the output voltage, eliminating the need for external / Auto-adjust to PSE type and load current with shunt regulator and optocoupler. It is optimized / auto-stretch for continuous conduction mode (CCM), and can / * Primary adapter priority input work with secondary side synchronous rectification,
- Adjustable frequency with synchronization The PSR feature of the DC-DC controller uses / Programmable frequency dithering for EMI feedback from an auxiliary winding for control of / * Automatic Maintain Power Signature (MPS) the output voltage, eliminating the need for external / Auto-adjust to PSE type and load current with shunt regulator and optocoupler. It is optimized / auto-stretch for continuous conduction mode (CCM), and can / * Primary adapter priority input work with secondary side synchronous rectification, / * -40 deg C to 125 deg C junction temperature range resulting in optimum efficiency, regulation accuracy
- * Access Points / * Pass-through System The automatic MPS enables applications with low / * Security Cameras power modes or multiple power feeds. It automatically / * Redundant Power Feeds or Power Sharing adjusts its pulsed current amplitude and duration / according to PSE Type and system conditions, to / maintain power while minimizing consumption. / Device Information(1)
- CLSB PPD BSLCR / DVC / BT CVCC DVC2 VB VB GAT2 / Voltage GNDDT COMP f c e i e rc d u b i a tr c y k TLV431 RDT 1VUR / TPS23730 / SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020 / RUV2 LINEUV I_STPEMPS RI_STP
- 4 Revision History.............................................................. 2 / 5 Device Comparison Table...............................................3 / 6 Pin Configuration and Functions...................................3 / 7 Specifications.................................................................. 6 / 7.1 Absolute Maximum Ratings ....................................... 6 / 7.2 ESD Ratings .............................................................. 6 / 7.3 Recommended Operating Conditions ........................7
- 5 Device Comparison Table...............................................3 / 6 Pin Configuration and Functions...................................3 / 7 Specifications.................................................................. 6 / 7.1 Absolute Maximum Ratings ....................................... 6 / 7.2 ESD Ratings .............................................................. 6 / 7.3 Recommended Operating Conditions ........................7 / 7.4 Thermal Information ...................................................7
- 6 Pin Configuration and Functions...................................3 / 7 Specifications.................................................................. 6 / 7.1 Absolute Maximum Ratings ....................................... 6 / 7.2 ESD Ratings .............................................................. 6 / 7.3 Recommended Operating Conditions ........................7 / 7.4 Thermal Information ...................................................7 / 7.5 Electrical Characteristics: DC-DC Controller
- 7 Specifications.................................................................. 6 / 7.1 Absolute Maximum Ratings ....................................... 6 / 7.2 ESD Ratings .............................................................. 6 / 7.3 Recommended Operating Conditions ........................7 / 7.4 Thermal Information ...................................................7 / 7.5 Electrical Characteristics: DC-DC Controller / Section ......................................................................... 8
- 7.1 Absolute Maximum Ratings ....................................... 6 / 7.2 ESD Ratings .............................................................. 6 / 7.3 Recommended Operating Conditions ........................7 / 7.4 Thermal Information ...................................................7 / 7.5 Electrical Characteristics: DC-DC Controller / Section ......................................................................... 8 / 7.6 Electrical Characteristics PoE .................................. 11
- 7.2 ESD Ratings .............................................................. 6 / 7.3 Recommended Operating Conditions ........................7 / 7.4 Thermal Information ...................................................7 / 7.5 Electrical Characteristics: DC-DC Controller / Section ......................................................................... 8 / 7.6 Electrical Characteristics PoE .................................. 11 / 7.7 Typical Characteristics..............................................14
- 7.4 Thermal Information ...................................................7 / 7.5 Electrical Characteristics: DC-DC Controller / Section ......................................................................... 8 / 7.6 Electrical Characteristics PoE .................................. 11 / 7.7 Typical Characteristics..............................................14 / 8 Detailed Description......................................................18 / 8.1 Overview...................................................................18
- 11.1 Layout Guidelines................................................... 50 / 11.2 Layout Example...................................................... 50 / 11.3 EMI Containment.................................................... 50 / 11.4 Thermal Considerations and OTSD........................ 50 / 11.5 ESD.........................................................................50 / 12 Device and Documentation Support..........................51 / 12.1 Documentation Support.......................................... 51
- 13 Mechanical, Packaging, and Orderable / Information.................................................................... 51 / 4 Revision History / NOTE: Page numbers for previous revisions may differ from page numbers in the current version. / Changes from Revision A (September 2020) to Revision B (November 2020) Page / * Updated package type in Device Information table............................................................................................ 1 / * Updated package type in pinout drawing caption...............................................................................................3
- Changes from Revision A (September 2020) to Revision B (November 2020) Page / * Updated package type in Device Information table............................................................................................ 1 / * Updated package type in pinout drawing caption...............................................................................................3 / * Updated package type in Thermal Information table..........................................................................................6 / Changes from Revision * (May 2020) to Revision A (September 2020) Page / * Updated the numbering format for tables, figures and cross-references throughout the document...................1 / * Changed status from "Advance Information" to "Production Data".....................................................................1
- PIN / I/O DESCRIPTION / NO. NAME / DC-DC controller current sense input. Connect directly to the external power current sense / 1 CS I/O / resistor. / 2 AGND - AGND is the DC-DC converter analog return. Tie to RTN and GND on the circuit board.
- power adapter is detected via the APD input or PPD input, both TPH and TPL pull low. Serial / 14 TPL O code over TPL can also be enabled by tying SCDIS pin to VSS. In this case, TPH becomes high / impedance. / 17 REF O Internal 1.25-V voltage reference. Connect a 49.9-kOhm_1% resistor from REF to VSS. / TPL serial code disable, referenced to VSS. Leave open to select parallel TPH/TPL configuration. / 18 SCDIS I / Tie to VSS to select serial code.
- Raising V above 2.5 V enables the hotswap MOSFET, activates TPH and TPL and turn / 19 PPD I PPD-VSS / class off. Tie PPD to VSS or float when not used. / 20 CLSB O Connect a resistor from CLSB to VSS to program the second classification current. / 21 CLSA O Connect a resistor from CLSA to VSS to program the first classification current. / Positive input power rail for PoE interface circuit and source of DC-DC converter start-up current. / 23 VDD

### Dimensions, package, and mechanical information

- according to PSE Type and system conditions, to / maintain power while minimizing consumption. / Device Information(1) / PART NUMBER PACKAGE BODY SIZE (NOM) / TPS23730 VQFN (45) 7.00 mm x 5.00 mm / (1) For all available packages, see the orderable addendum at / the end of the data sheet.
- Device Information(1) / PART NUMBER PACKAGE BODY SIZE (NOM) / TPS23730 VQFN (45) 7.00 mm x 5.00 mm / (1) For all available packages, see the orderable addendum at / the end of the data sheet. / T1 / tsernermehrotEfs mnaorrTF
- Simplified Application / An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications, / intellectual property matters and other important disclaimers. PRODUCTION DATA. / PACKAGE | BODY SIZE (NOM) / VQFN (45) | 7.00 mm x 5.00 mm / Table of Contents / 1 Features............................................................................1
- 12.3 Trademarks.............................................................51 / 12.4 Electrostatic Discharge Caution..............................51 / 12.5 Glossary..................................................................51 / 13 Mechanical, Packaging, and Orderable / Information.................................................................... 51 / 4 Revision History / NOTE: Page numbers for previous revisions may differ from page numbers in the current version.
- 4 Revision History / NOTE: Page numbers for previous revisions may differ from page numbers in the current version. / Changes from Revision A (September 2020) to Revision B (November 2020) Page / * Updated package type in Device Information table............................................................................................ 1 / * Updated package type in pinout drawing caption...............................................................................................3 / * Updated package type in Thermal Information table..........................................................................................6 / Changes from Revision * (May 2020) to Revision A (September 2020) Page
- NOTE: Page numbers for previous revisions may differ from page numbers in the current version. / Changes from Revision A (September 2020) to Revision B (November 2020) Page / * Updated package type in Device Information table............................................................................................ 1 / * Updated package type in pinout drawing caption...............................................................................................3 / * Updated package type in Thermal Information table..........................................................................................6 / Changes from Revision * (May 2020) to Revision A (September 2020) Page / * Updated the numbering format for tables, figures and cross-references throughout the document...................1
- Changes from Revision A (September 2020) to Revision B (November 2020) Page / * Updated package type in Device Information table............................................................................................ 1 / * Updated package type in pinout drawing caption...............................................................................................3 / * Updated package type in Thermal Information table..........................................................................................6 / Changes from Revision * (May 2020) to Revision A (September 2020) Page / * Updated the numbering format for tables, figures and cross-references throughout the document...................1 / * Changed status from "Advance Information" to "Production Data".....................................................................1
- PAD_G / NC 10 / PAD_S / Figure 6-1. RMT Package 45-Pin VQFN Top View / Copyright 2022 Texas Instruments Incorporated Submit Document Feedback 3 / Product Folder Links: TPS23730 / KEY FEATURES | TPS23730 | TPS23731 | TPS23734
- a Class 5 to 8 device like a Class 4 device, allotting 25.5W if it chooses to power the PD. A Class 4 PD that / receives a 2-event class, a Class 5 or 6 PD that receives a 4-event class, or a Class 7 or 8 PD that receives / a 5-event class, understands that the PSE has agreed to allocate the PD requested power. In the case where / there is power demotion, the PD may choose to not start, or to start while not drawing more power than initially / allocated, and request more power through the DLL after startup. The standard requires a Type 2, 3 or 4 PD / to indicate that it is underpowered if this occurs. Startup of a high-power PD at lower power than requested / implicitly requires some form of powering down sections of the application circuits.
- specifications. / 12.5 Glossary / TI Glossary This glossary lists and explains terms, acronyms, and definitions. / 13 Mechanical, Packaging, and Orderable Information / The following pages include mechanical, packaging, and orderable information. This information is the most / current data available for the designated devices. This data is subject to change without notice and revision of / this document. For browser-based versions of this data sheet, refer to the left-hand navigation.
- 12.5 Glossary / TI Glossary This glossary lists and explains terms, acronyms, and definitions. / 13 Mechanical, Packaging, and Orderable Information / The following pages include mechanical, packaging, and orderable information. This information is the most / current data available for the designated devices. This data is subject to change without notice and revision of / this document. For browser-based versions of this data sheet, refer to the left-hand navigation. / www.ti.com
- SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020 / Copyright 2022 Texas Instruments Incorporated Submit Document Feedback 51 / Product Folder Links: TPS23730 / PACKAGE OPTION ADDENDUM / www.ti.com 6-Feb-2026 / PACKAGING INFORMATION / Orderable part number Status
- (1) / Material type / (2) / Package | Pins Package qty | Carrier RoHS / (3) / Lead finish/ / Ball material
- In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis. / Addendum-Page 1 / Orderable part number | Status (1) | Material type (2) | Package | Pins | Package qty | Carrier | RoHS (3) | Lead finish/ Ball material (4) | MSL rating/ Peak reflow (5) | Op temp ( deg C) | Part marking (6) / TPS23730RMTR | Active | Production | VQFN (RMT) | 45 | 3000 | LARGE T&R | Yes | NIPDAU | Level-3-260C-168 HR | 40 to 125 | TPS23730 DB0 WA1 / TPS23730RMTR.A | Active | Production | VQFN (RMT) | 45 | 3000 | LARGE T&R | Yes | NIPDAU | Level-3-260C-168 HR | 40 to 125 | TPS23730 DB0 WA1 / TPS23730RMTRG4 | Active | Production | VQFN (RMT) | 45 | 3000 | LARGE T&R | Yes | NIPDAU | Level-3-260C-168 HR | 40 to 125 | TPS23730 DB0 WA1
- TPS23730RMTR.A | Active | Production | VQFN (RMT) | 45 | 3000 | LARGE T&R | Yes | NIPDAU | Level-3-260C-168 HR | 40 to 125 | TPS23730 DB0 WA1 / TPS23730RMTRG4 | Active | Production | VQFN (RMT) | 45 | 3000 | LARGE T&R | Yes | NIPDAU | Level-3-260C-168 HR | 40 to 125 | TPS23730 DB0 WA1 / TPS23730RMTRG4.A | Active | Production | VQFN (RMT) | 45 | 3000 | LARGE T&R | Yes | NIPDAU | Level-3-260C-168 HR | 40 to 125 | TPS23730 DB0 WA1 / PACKAGE OPTION ADDENDUM / www.ti.com 6-Feb-2026 / Addendum-Page 2
- www.ti.com 6-Feb-2026 / Addendum-Page 2 / PACKAGE MATERIALS INFORMATION / www.ti.com 18-Jun-2025 / TAPE AND REEL INFORMATION / REEL DIMENSIONS TAPE DIMENSIONS
- PACKAGE MATERIALS INFORMATION / www.ti.com 18-Jun-2025 / TAPE AND REEL INFORMATION / REEL DIMENSIONS TAPE DIMENSIONS / K0 P1 / W / B0
- Reel / Diameter / Cavity A0 / A0 Dimension designed to accommodate the component width / B0 Dimension designed to accommodate the component length / K0 Dimension designed to accommodate the component thickness / W Overall width of the carrier tape

### Formulas, equations, and configuration calculations

- PD Solution Ethernet (PoE) powered device (PD) interface, and a / EA Gen 2 logo-ready (PoE 2 PD Controller) current-mode DC-DC controller optimized for flyback / Robust 100-V, 0.3-Ohm (typ) Hotswap MOSFET and active clamp forward (ACF) switching regulator / Supports power levels for up to 60-W operation designs . In the case of flyback configuration, the use / Allocated power indicator outputs - parallel or of primary-side regulation (PSR) is supported. The / serial encoding selectable PoE interface supports the IEEE 802.3bt standard for / * Integrated PWM controller for flyback or Active applications needing up to 51 W or less at PD input.
- Allocated power indicator outputs - parallel or of primary-side regulation (PSR) is supported. The / serial encoding selectable PoE interface supports the IEEE 802.3bt standard for / * Integrated PWM controller for flyback or Active applications needing up to 51 W or less at PD input. / Clamp Forward configuration / Programmable spread spectrum frequency dithering / Flyback control with primary-side regulation (SSFD) is provided to minimize the size and cost of / * Supports CCM operation EMI filter. Advanced Startup with adjustable soft-start
- Clamp Forward configuration / Programmable spread spectrum frequency dithering / Flyback control with primary-side regulation (SSFD) is provided to minimize the size and cost of / * Supports CCM operation EMI filter. Advanced Startup with adjustable soft-start / * +/-1.5% (typ, 5-V output) load regulation helps to use minimal bias capacitor while simplifying / (0-100% load range) - with Sync FET converter startup and hiccup design, also ensuring / Also supports secondary-side regulation that IEEE 802.3bt startup requirements are met.
- * +/-1.5% (typ, 5-V output) load regulation helps to use minimal bias capacitor while simplifying / (0-100% load range) - with Sync FET converter startup and hiccup design, also ensuring / Also supports secondary-side regulation that IEEE 802.3bt startup requirements are met. / Soft-start control with advanced startup and / The soft-stop feature minimizes stress on switching / hiccup mode overload protection / power FETs , allowing FET BOM cost reduction.
- * Access Points / * Pass-through System The automatic MPS enables applications with low / * Security Cameras power modes or multiple power feeds. It automatically / * Redundant Power Feeds or Power Sharing adjusts its pulsed current amplitude and duration / according to PSE Type and system conditions, to / maintain power while minimizing consumption. / Device Information(1)
- 3 Description.......................................................................1 / 4 Revision History.............................................................. 2 / 5 Device Comparison Table...............................................3 / 6 Pin Configuration and Functions...................................3 / 7 Specifications.................................................................. 6 / 7.1 Absolute Maximum Ratings ....................................... 6 / 7.2 ESD Ratings .............................................................. 6
- 11.1 Layout Guidelines................................................... 50 / 11.2 Layout Example...................................................... 50 / 11.3 EMI Containment.................................................... 50 / 11.4 Thermal Considerations and OTSD........................ 50 / 11.5 ESD.........................................................................50 / 12 Device and Documentation Support..........................51 / 12.1 Documentation Support.......................................... 51
- PoE allocated power and AUX power TPH/TPL (parallel) or TPL / T2P, APDO T2P, APDO / indicator(s) (serial) / 6 Pin Configuration and Functions / 45 44 43 42 / 4 32 / 5 31
- 12 BT O identified. Open-drain, active-low output referenced to RTN. BT state remains unchanged if an / auxiliary power adapter is detected via APD or PPD input. BT is also disabled if SCDIS is low. / 13 TPH O TPH/TPL binary code indicates the PSE allocated power output. Open-drain, active-low outputs / referenced to RTN. The default operation is with parallel binary code. Also, whenever an auxiliary / power adapter is detected via the APD input or PPD input, both TPH and TPL pull low. Serial / 14 TPL O code over TPL can also be enabled by tying SCDIS pin to VSS. In this case, TPH becomes high / impedance.
- 14 TPL O code over TPL can also be enabled by tying SCDIS pin to VSS. In this case, TPH becomes high / impedance. / 17 REF O Internal 1.25-V voltage reference. Connect a 49.9-kOhm_1% resistor from REF to VSS. / TPL serial code disable, referenced to VSS. Leave open to select parallel TPH/TPL configuration. / 18 SCDIS I / Tie to VSS to select serial code. / Raising V above 2.5 V enables the hotswap MOSFET, activates TPH and TPL and turn
- Bypass with a 0.1 uF to VSS and protect with a TVS. / Connect a 25.5-kOhm resistor from DEN to VDD to provide the PoE detection signature. Pulling this / 24 DEN I/O / pin to VSS during powered operation causes the internal hotswap MOSFET to turn off. / 27, 28 VSS - Negative power rail derived from the PoE source. / 30 TEST O Used internally for test purposes only. Leave open. / Connect a resistor from DT to AGND to set the GATE to GAT2 dead time. Tie DT to VB to disable
- 30 TEST O Used internally for test purposes only. Leave open. / Connect a resistor from DT to AGND to set the GATE to GAT2 dead time. Tie DT to VB to disable / 31 DT I / GAT2 operation. / This pin sets the SST discharge current during a soft-stop event independently from the setting / 32 I_STP I used during a regular soft-start event. Connect a resistor from this pin to AGND to set the DC/DC / soft-stop rate.
- 31 DT I / GAT2 operation. / This pin sets the SST discharge current during a soft-stop event independently from the setting / 32 I_STP I used during a regular soft-start event. Connect a resistor from this pin to AGND to set the DC/DC / soft-stop rate. / A capacitor from SST to RTN pin sets the soft-start (I charge current) and the hiccup timer (I / SSC SSD
- This pin sets the SST discharge current during a soft-stop event independently from the setting / 32 I_STP I used during a regular soft-start event. Connect a resistor from this pin to AGND to set the DC/DC / soft-stop rate. / A capacitor from SST to RTN pin sets the soft-start (I charge current) and the hiccup timer (I / SSC SSD / 33 SST I/O discharge current) for the DC-DC converter. Connect a capacitor from this pin to RTN to set the / DC/DC startup rate.
- SSC SSD / 33 SST I/O discharge current) for the DC-DC converter. Connect a capacitor from this pin to RTN to set the / DC/DC startup rate. / Converter error amplifier inverting (feedback) input. If flyback configuration with primary-side / regulation, it is typically driven by a voltage divider and capacitor from the auxiliary winding, / 34 FB I / working with CP pin, FB also being connected to the COMP compensation network. If optocoupler
- 7, 8, 9 | RTN | | RTN is the output of the PoE hotswap and the reference ground for the DC-DC controller. / 11 | EMPS | I | Automatic MPS enable input, referenced to RTN, internally pulled-up to 5-V internal rail. Tie to RTN to disable automatic MPS. / 12 | BT | O | Indicates that a PSE applying an IEEE802.3bt (Type 3 or 4) mutual identification scheme has been identified. Open-drain, active-low output referenced to RTN. BT state remains unchanged if an auxiliary power adapter is detected via APD or PPD input. BT is also disabled if SCDIS is low. / 13 | TPH | O | TPH/TPL binary code indicates the PSE allocated power output. Open-drain, active-low outputs referenced to RTN. The default operation is with parallel binary code. Also, whenever an auxiliary power adapter is detected via the APD input or PPD input, both TPH and TPL pull low. Serial code over TPL can also be enabled by tying SCDIS pin to VSS. In this case, TPH becomes high impedance. / 14 | TPL | O | / 17 | REF | O | Internal 1.25-V voltage reference. Connect a 49.9-kOhm_1% resistor from REF to VSS. / 18 | SCDIS | I | TPL serial code disable, referenced to VSS. Leave open to select parallel TPH/TPL configuration. Tie to VSS to select serial code.
- 13 | TPH | O | TPH/TPL binary code indicates the PSE allocated power output. Open-drain, active-low outputs referenced to RTN. The default operation is with parallel binary code. Also, whenever an auxiliary power adapter is detected via the APD input or PPD input, both TPH and TPL pull low. Serial code over TPL can also be enabled by tying SCDIS pin to VSS. In this case, TPH becomes high impedance. / 14 | TPL | O | / 17 | REF | O | Internal 1.25-V voltage reference. Connect a 49.9-kOhm_1% resistor from REF to VSS. / 18 | SCDIS | I | TPL serial code disable, referenced to VSS. Leave open to select parallel TPH/TPL configuration. Tie to VSS to select serial code. / 19 | PPD | I | Raising V above 2.5 V enables the hotswap MOSFET, activates TPH and TPL and turn PPD-VSS class off. Tie PPD to VSS or float when not used. / 20 | CLSB | O | Connect a resistor from CLSB to VSS to program the second classification current. / 21 | CLSA | O | Connect a resistor from CLSA to VSS to program the first classification current.
- 20 | CLSB | O | Connect a resistor from CLSB to VSS to program the second classification current. / 21 | CLSA | O | Connect a resistor from CLSA to VSS to program the first classification current. / 23 | VDD | | Positive input power rail for PoE interface circuit and source of DC-DC converter start-up current. Bypass with a 0.1 uF to VSS and protect with a TVS. / 24 | DEN | I/O | Connect a 25.5-kOhm resistor from DEN to VDD to provide the PoE detection signature. Pulling this pin to VSS during powered operation causes the internal hotswap MOSFET to turn off. / 27, 28 | VSS | | Negative power rail derived from the PoE source. / 30 | TEST | O | Used internally for test purposes only. Leave open. / 31 | DT | I | Connect a resistor from DT to AGND to set the GATE to GAT2 dead time. Tie DT to VB to disable GAT2 operation.

### Reference designs, applications, and examples

- Supports power levels for up to 60-W operation designs . In the case of flyback configuration, the use / Allocated power indicator outputs - parallel or of primary-side regulation (PSR) is supported. The / serial encoding selectable PoE interface supports the IEEE 802.3bt standard for / * Integrated PWM controller for flyback or Active applications needing up to 51 W or less at PD input. / Clamp Forward configuration / Programmable spread spectrum frequency dithering / Flyback control with primary-side regulation (SSFD) is provided to minimize the size and cost of
- * Primary adapter priority input work with secondary side synchronous rectification, / * -40 deg C to 125 deg C junction temperature range resulting in optimum efficiency, regulation accuracy / and step load response over multiple outputs. / 2 Applications / The DC-DC controller features slope compensation / * Video and VoIP Telephones / and blanking. Typical switching frequency is 250 kHz.
- * Video and VoIP Telephones / and blanking. Typical switching frequency is 250 kHz. / * Access Points / * Pass-through System The automatic MPS enables applications with low / * Security Cameras power modes or multiple power feeds. It automatically / * Redundant Power Feeds or Power Sharing adjusts its pulsed current amplitude and duration / according to PSE Type and system conditions, to
- TPS23730 / SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020 / RUV2 LINEUV I_STPEMPS RI_STP / Simplified Application / An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications, / intellectual property matters and other important disclaimers. PRODUCTION DATA. / PACKAGE | BODY SIZE (NOM)
- SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020 / RUV2 LINEUV I_STPEMPS RI_STP / Simplified Application / An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications, / intellectual property matters and other important disclaimers. PRODUCTION DATA. / PACKAGE | BODY SIZE (NOM) / VQFN (45) | 7.00 mm x 5.00 mm
- VQFN (45) | 7.00 mm x 5.00 mm / Table of Contents / 1 Features............................................................................1 / 2 Applications.....................................................................1 / 3 Description.......................................................................1 / 4 Revision History.............................................................. 2 / 5 Device Comparison Table...............................................3
- 8.2 Functional Block Diagram.........................................19 / 8.3 Feature Description...................................................20 / 8.4 Device Functional Modes..........................................29 / 9 Application and Implementation..................................44 / 9.1 Application Information............................................. 44 / 9.2 Typical Application.................................................... 44 / 10 Power Supply Recommendations..............................49
- 8.3 Feature Description...................................................20 / 8.4 Device Functional Modes..........................................29 / 9 Application and Implementation..................................44 / 9.1 Application Information............................................. 44 / 9.2 Typical Application.................................................... 44 / 10 Power Supply Recommendations..............................49 / 11 Layout...........................................................................50
- 8.4 Device Functional Modes..........................................29 / 9 Application and Implementation..................................44 / 9.1 Application Information............................................. 44 / 9.2 Typical Application.................................................... 44 / 10 Power Supply Recommendations..............................49 / 11 Layout...........................................................................50 / 11.1 Layout Guidelines................................................... 50
- 10 Power Supply Recommendations..............................49 / 11 Layout...........................................................................50 / 11.1 Layout Guidelines................................................... 50 / 11.2 Layout Example...................................................... 50 / 11.3 EMI Containment.................................................... 50 / 11.4 Thermal Considerations and OTSD........................ 50 / 11.5 ESD.........................................................................50
- to compensate the converter. If optocoupler feedback is enabled, the optocoupler and its network / pulled up to VB directly drives the COMP pin. / Error Amplifier disable input, referenced to AGND, internally pulled-up to 5V internal rail. Leave / 36 EA_DIS I EA_DIS open to disable the Error amplifier, to enable optocoupler feedback for example. Connect / to AGND otherwise. / 4 Submit Document Feedback Copyright 2022 Texas Instruments Incorporated / Product Folder Links: TPS23730
- 33 | SST | I/O | A capacitor from SST to RTN pin sets the soft-start (I charge current) and the hiccup timer (I SSC SSD discharge current) for the DC-DC converter. Connect a capacitor from this pin to RTN to set the DC/DC startup rate. / 34 | FB | I | Converter error amplifier inverting (feedback) input. If flyback configuration with primary-side regulation, it is typically driven by a voltage divider and capacitor from the auxiliary winding, working with CP pin, FB also being connected to the COMP compensation network. If optocoupler feedback is enabled, tie FB to VB. / 35 | COMP | I/O | Compensation output of the DC-DC convertor error amplifier or control loop input to the PWM. If the internal error amplifier is used, connect the compensation networks from this pin to the FB pin to compensate the converter. If optocoupler feedback is enabled, the optocoupler and its network pulled up to VB directly drives the COMP pin. / 36 | EA_DIS | I | Error Amplifier disable input, referenced to AGND, internally pulled-up to 5V internal rail. Leave EA_DIS open to disable the Error amplifier, to enable optocoupler feedback for example. Connect to AGND otherwise. / Table 6-1. Pin Functions (continued) / PIN / I/O DESCRIPTION
- PSR Sync enable input, referenced to AGND, internally pulled-up to 5V internal rail. PSRS works / with CP pin to support flyback architecture using primary-side regulation. Leave PSRS open if / the flyback output stage is configured with synchronous rectification and uses PSR. If diode / rectification is used, or for applications not using PSR, connect PSRS to AGND. / 40 VBG O 5-V bias rail for the switching FET gate driver circuit. For internal use only. Bypass with a 0.1-uF / ceramic capacitor to GND pin. / 41 GAT2 O Gate drive output for a second DC-DC converter switching MOSFET.
- NO. | NAME | | / 37 | VB | O | 5-V bias rail for DC/DC control circuits and the feedback optocoupler (when in use). Connect a 0.1-uF capacitor from this pin to AGND to provide bypassing. / 38 | LINEUV | I | LINEUV is used to monitor the bulk capacitor voltage to trigger a soft-stop event when an undervoltage condition is detected if APD is low. If not used, connect LINEUV to VB pin. / 39 | PSRS | I | PSR Sync enable input, referenced to AGND, internally pulled-up to 5V internal rail. PSRS works with CP pin to support flyback architecture using primary-side regulation. Leave PSRS open if the flyback output stage is configured with synchronous rectification and uses PSR. If diode rectification is used, or for applications not using PSR, connect PSRS to AGND. / 40 | VBG | O | 5-V bias rail for the switching FET gate driver circuit. For internal use only. Bypass with a 0.1-uF ceramic capacitor to GND pin. / 41 | GAT2 | O | Gate drive output for a second DC-DC converter switching MOSFET. / 42 | VCC | I/O | DC/DC converter bias voltage. The internal startup current source and converter bias winding output power this pin. Connect a 1uF minimum ceramic capacitor to RTN.
- (1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process. / (2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process. / (3) Surges per EN61000-4-2, 1999 applied between RJ-45 and output ground and between adapter input and output ground of / the TPS23730, TPS23730EVM-093 evaluation module (documentation available on the web). These were the test levels, not the / failure threshold. / 6 Submit Document Feedback Copyright 2022 Texas Instruments Incorporated / Product Folder Links: TPS23730
- JC(bot_POE) / R Junction-to-case (bottom PAD_G pad) thermal resistance 9.1 / JC(bot_DCDC) / (1) Thermal metrics are not JEDEC standard values and are based on the TPS23731EVM-095 evaluation board. / Copyright 2022 Texas Instruments Incorporated Submit Document Feedback 7 / Product Folder Links: TPS23730 / | | MIN | NOM | MAX | UNIT
- Copyright 2022 Texas Instruments Incorporated Submit Document Feedback 19 / Product Folder Links: TPS23730 / 8.3 Feature Description / See Figure 9-1 for component reference designators (R CS for example ), and Electrical Characteristics: DC-DC / Controller Section for values denoted by reference (V CSMAX for example). Electrical Characteristic values take / precedence over any numerical values used in the following sections. / 8.3.1 CLSA, CLSB Classification
- Product Folder Links: TPS23730 / 8.3 Feature Description / See Figure 9-1 for component reference designators (R CS for example ), and Electrical Characteristics: DC-DC / Controller Section for values denoted by reference (V CSMAX for example). Electrical Characteristic values take / precedence over any numerical values used in the following sections. / 8.3.1 CLSA, CLSB Classification / Each of the two external resistors (R CLSA and R CLSB in Figure 9-1 ) connected between the CLSA (first and

## Page-by-page extracted content

### Page 1

#### Extracted tables

Table 1:

```text
PACKAGE | BODY SIZE (NOM)
VQFN (45) | 7.00 mm x 5.00 mm
```

#### Raw extracted text

```text
TPS23730 IEEE 802.3bt Type 3 PoE PD with High Efficiency DC-DC Controller
1 Features 3 Description
* Complete IEEE 802.3bt Type 3 (Class 1-6) PoE The TPS23730 device combines a Power over
PD Solution Ethernet (PoE) powered device (PD) interface, and a
- EA Gen 2 logo-ready (PoE 2 PD Controller) current-mode DC-DC controller optimized for flyback
- Robust 100-V, 0.3-Ohm (typ) Hotswap MOSFET and active clamp forward (ACF) switching regulator
- Supports power levels for up to 60-W operation designs . In the case of flyback configuration, the use
- Allocated power indicator outputs - parallel or of primary-side regulation (PSR) is supported. The
serial encoding selectable PoE interface supports the IEEE 802.3bt standard for
* Integrated PWM controller for flyback or Active applications needing up to 51 W or less at PD input.
Clamp Forward configuration
Programmable spread spectrum frequency dithering
- Flyback control with primary-side regulation (SSFD) is provided to minimize the size and cost of
* Supports CCM operation EMI filter. Advanced Startup with adjustable soft-start
* +/-1.5% (typ, 5-V output) load regulation helps to use minimal bias capacitor while simplifying
(0-100% load range) - with Sync FET converter startup and hiccup design, also ensuring
- Also supports secondary-side regulation that IEEE 802.3bt startup requirements are met.
- Soft-start control with advanced startup and
The soft-stop feature minimizes stress on switching
hiccup mode overload protection
power FETs , allowing FET BOM cost reduction.
- Soft-stop shutdown
- Adjustable frequency with synchronization The PSR feature of the DC-DC controller uses
- Programmable frequency dithering for EMI feedback from an auxiliary winding for control of
* Automatic Maintain Power Signature (MPS) the output voltage, eliminating the need for external
- Auto-adjust to PSE type and load current with shunt regulator and optocoupler. It is optimized
auto-stretch for continuous conduction mode (CCM), and can
* Primary adapter priority input work with secondary side synchronous rectification,
* -40 deg C to 125 deg C junction temperature range resulting in optimum efficiency, regulation accuracy
and step load response over multiple outputs.
2 Applications
The DC-DC controller features slope compensation
* Video and VoIP Telephones
and blanking. Typical switching frequency is 250 kHz.
* Access Points
* Pass-through System The automatic MPS enables applications with low
* Security Cameras power modes or multiple power feeds. It automatically
* Redundant Power Feeds or Power Sharing adjusts its pulsed current amplitude and duration
according to PSE Type and system conditions, to
maintain power while minimizing consumption.
Device Information(1)
PART NUMBER PACKAGE BODY SIZE (NOM)
TPS23730 VQFN (45) 7.00 mm x 5.00 mm
(1) For all available packages, see the orderable addendum at
the end of the data sheet.
T1
tsernermehrotEfs mnaorrTF
ASLCR
VDD
CLSA VSS ssriraePm erorafspnSa rmT orroF
CBULK+ RDEN DEN
0.1 (cid:29)F 58V VCC
GATE CS CDTR SCR
VB CVB APD
FRS DTHR Ad4a8pVte r RFRS RTN 1DPAR
VCC
TPH
I_in
DA RDTR SST CSST RAPD2
HPTR TPL LPTR
CLSB PPD BSLCR
DVC
BT CVCC DVC2 VB VB GAT2
Voltage GNDDT COMP f c e i e rc d u b i a tr c y k TLV431 RDT 1VUR
TPS23730
SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020
RUV2 LINEUV I_STPEMPS RI_STP
Simplified Application
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
4 Revision History.............................................................. 2
5 Device Comparison Table...............................................3
6 Pin Configuration and Functions...................................3
7 Specifications.................................................................. 6
7.1 Absolute Maximum Ratings ....................................... 6
7.2 ESD Ratings .............................................................. 6
7.3 Recommended Operating Conditions ........................7
7.4 Thermal Information ...................................................7
7.5 Electrical Characteristics: DC-DC Controller
Section ......................................................................... 8
7.6 Electrical Characteristics PoE .................................. 11
7.7 Typical Characteristics..............................................14
8 Detailed Description......................................................18
8.1 Overview...................................................................18
8.2 Functional Block Diagram.........................................19
8.3 Feature Description...................................................20
8.4 Device Functional Modes..........................................29
9 Application and Implementation..................................44
9.1 Application Information............................................. 44
9.2 Typical Application.................................................... 44
10 Power Supply Recommendations..............................49
11 Layout...........................................................................50
11.1 Layout Guidelines................................................... 50
11.2 Layout Example...................................................... 50
11.3 EMI Containment.................................................... 50
11.4 Thermal Considerations and OTSD........................ 50
11.5 ESD.........................................................................50
12 Device and Documentation Support..........................51
12.1 Documentation Support.......................................... 51
12.2 Support Resources................................................. 51
12.3 Trademarks.............................................................51
12.4 Electrostatic Discharge Caution..............................51
12.5 Glossary..................................................................51
13 Mechanical, Packaging, and Orderable
Information.................................................................... 51
4 Revision History
NOTE: Page numbers for previous revisions may differ from page numbers in the current version.
Changes from Revision A (September 2020) to Revision B (November 2020) Page
* Updated package type in Device Information table............................................................................................ 1
* Updated package type in pinout drawing caption...............................................................................................3
* Updated package type in Thermal Information table..........................................................................................6
Changes from Revision * (May 2020) to Revision A (September 2020) Page
* Updated the numbering format for tables, figures and cross-references throughout the document...................1
* Changed status from "Advance Information" to "Production Data".....................................................................1
TPS23730
SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020 www.ti.com
2 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS23730
```

### Page 3

#### Extracted tables

Table 1:

```text
KEY FEATURES | TPS23730 | TPS23731 | TPS23734
Class Range | 1-6 | 1-4 | 1-4
ACF Support | Yes | No | Yes
SSFD | Yes | Yes | Yes
Soft-stop | Yes | Yes | Yes
Advanced Startup | Yes | Yes | Yes
PSR (Flyback) | Yes | Yes | Yes
Auto MPS | Yes | Yes | Yes
PPD | Yes | No | No
APD | Yes | Yes | Yes
PoE allocated power and AUX power indicator(s) | TPH/TPL (parallel) or TPL (serial) | T2P, APDO | T2P, APDO
```

Table 2:

```text
45 | 44
```

Table 3:

```text
43
```

Table 4:

```text
42
```

Table 5:

```text
41
```

Table 6:

```text
40 | 39
```

Table 7:

```text
38
```

Table 8:

```text
37 | 36
```

Table 9:

```text
1 | 
2 |
```

Table 10:

```text
| 35
 | 34
```

Table 11:

```text
3 |
```

Table 12:

```text
| 33
```

Table 13:

```text
4 |
```

Table 14:

```text
| 32
```

Table 15:

```text
5 |
```

Table 16:

```text
| 31
```

Table 17:

```text
6 | 
7 |
```

Table 18:

```text
| 30
```

Table 19:

```text
8 | 
9 |
```

Table 20:

```text
| 29
 | 28
```

Table 21:

```text
| 27
```

Table 22:

```text
10 |
```

Table 23:

```text
| 26
```

Table 24:

```text
11 |
```

Table 25:

```text
| 25
```

Table 26:

```text
12 | 
13 |
```

Table 27:

```text
| 24
 | 23
```

Table 28:

```text
14 | 15
```

Table 29:

```text
16
```

Table 30:

```text
17
```

Table 31:

```text
18
```

Table 32:

```text
19 | 20
```

Table 33:

```text
21
```

Table 34:

```text
22
```

#### Raw extracted text

```text
5 Device Comparison Table
KEY FEATURES TPS23730 TPS23731 TPS23734
Class Range 1-6 1-4 1-4
ACF Support Yes No Yes
SSFD Yes Yes Yes
Soft-stop Yes Yes Yes
Advanced Startup Yes Yes Yes
PSR (Flyback) Yes Yes Yes
Auto MPS Yes Yes Yes
PPD Yes No No
APD Yes Yes Yes
PoE allocated power and AUX power TPH/TPL (parallel) or TPL
T2P, APDO T2P, APDO
indicator(s) (serial)
6 Pin Configuration and Functions
45 44 43 42
4 32
5 31
6 30
29
VSS
NC
VDD
SCDIS
RTN
14 15 16
VCC
17
7
VSS
DEN
41
RTN
18
VBG
19 20 21
CLSA
35
34
DTHR 33
FRS
GND
CP
GATE
40 39 38
1 COMP
2 FB
3 SST
PSRS
CS
GAT2
APD
NC
LINEUV
AGND
8
9 28
27
26
11
TPL PPD
I_STP
BT
TPH
NC
EMPS
REF
12
13
22
25
24
23
37 36
TEST
NC
NC
NC CLSB
RTN
VB
NC
DT
EA_DIS
TPS23730
www.ti.com SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020
PAD_G
NC 10
PAD_S
Figure 6-1. RMT Package 45-Pin VQFN Top View
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 3
Product Folder Links: TPS23730
```

### Page 4

#### Extracted tables

Table 1:

```text
PIN |  | I/O | DESCRIPTION
NO. | NAME |  | 
1 | CS | I/O | DC-DC controller current sense input. Connect directly to the external power current sense resistor.
2 | AGND |  | AGND is the DC-DC converter analog return. Tie to RTN and GND on the circuit board.
3 | DTHR | O | Used for spread spectrum frequency dithering. Connect a capacitor (determines the modulating frequency) from DTHR to RTN and a resistor (determines the amount of dithering) from DTHR to FRS. If dithering is not used, short DTHR to VB pin.
4 | FRS | I | This pin controls the switching frequency of the DC-DC converter. Tie a resistor from this pin to RTN to set the frequency.
5 | APD | I | Primary auxiliary power detect input. Raise 1.5 V above RTN to disable pass MOSFET, also turning class off. If not used, connect APD to RTN.
7, 8, 9 | RTN |  | RTN is the output of the PoE hotswap and the reference ground for the DC-DC controller.
11 | EMPS | I | Automatic MPS enable input, referenced to RTN, internally pulled-up to 5-V internal rail. Tie to RTN to disable automatic MPS.
12 | BT | O | Indicates that a PSE applying an IEEE802.3bt (Type 3 or 4) mutual identification scheme has been identified. Open-drain, active-low output referenced to RTN. BT state remains unchanged if an auxiliary power adapter is detected via APD or PPD input. BT is also disabled if SCDIS is low.
13 | TPH | O | TPH/TPL binary code indicates the PSE allocated power output. Open-drain, active-low outputs referenced to RTN. The default operation is with parallel binary code. Also, whenever an auxiliary power adapter is detected via the APD input or PPD input, both TPH and TPL pull low. Serial code over TPL can also be enabled by tying SCDIS pin to VSS. In this case, TPH becomes high impedance.
14 | TPL | O | 
17 | REF | O | Internal 1.25-V voltage reference. Connect a 49.9-kOhm_1% resistor from REF to VSS.
18 | SCDIS | I | TPL serial code disable, referenced to VSS. Leave open to select parallel TPH/TPL configuration. Tie to VSS to select serial code.
19 | PPD | I | Raising V above 2.5 V enables the hotswap MOSFET, activates TPH and TPL and turn PPD-VSS class off. Tie PPD to VSS or float when not used.
20 | CLSB | O | Connect a resistor from CLSB to VSS to program the second classification current.
21 | CLSA | O | Connect a resistor from CLSA to VSS to program the first classification current.
23 | VDD |  | Positive input power rail for PoE interface circuit and source of DC-DC converter start-up current. Bypass with a 0.1 uF to VSS and protect with a TVS.
24 | DEN | I/O | Connect a 25.5-kOhm resistor from DEN to VDD to provide the PoE detection signature. Pulling this pin to VSS during powered operation causes the internal hotswap MOSFET to turn off.
27, 28 | VSS |  | Negative power rail derived from the PoE source.
30 | TEST | O | Used internally for test purposes only. Leave open.
31 | DT | I | Connect a resistor from DT to AGND to set the GATE to GAT2 dead time. Tie DT to VB to disable GAT2 operation.
32 | I_STP | I | This pin sets the SST discharge current during a soft-stop event independently from the setting used during a regular soft-start event. Connect a resistor from this pin to AGND to set the DC/DC soft-stop rate.
33 | SST | I/O | A capacitor from SST to RTN pin sets the soft-start (I charge current) and the hiccup timer (I SSC SSD discharge current) for the DC-DC converter. Connect a capacitor from this pin to RTN to set the DC/DC startup rate.
34 | FB | I | Converter error amplifier inverting (feedback) input. If flyback configuration with primary-side regulation, it is typically driven by a voltage divider and capacitor from the auxiliary winding, working with CP pin, FB also being connected to the COMP compensation network. If optocoupler feedback is enabled, tie FB to VB.
35 | COMP | I/O | Compensation output of the DC-DC convertor error amplifier or control loop input to the PWM. If the internal error amplifier is used, connect the compensation networks from this pin to the FB pin to compensate the converter. If optocoupler feedback is enabled, the optocoupler and its network pulled up to VB directly drives the COMP pin.
36 | EA_DIS | I | Error Amplifier disable input, referenced to AGND, internally pulled-up to 5V internal rail. Leave EA_DIS open to disable the Error amplifier, to enable optocoupler feedback for example. Connect to AGND otherwise.
```

#### Raw extracted text

```text
TPS23730
SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020 www.ti.com
Table 6-1. Pin Functions
PIN
I/O DESCRIPTION
NO. NAME
DC-DC controller current sense input. Connect directly to the external power current sense
1 CS I/O
resistor.
2 AGND - AGND is the DC-DC converter analog return. Tie to RTN and GND on the circuit board.
Used for spread spectrum frequency dithering. Connect a capacitor (determines the modulating
3 DTHR O frequency) from DTHR to RTN and a resistor (determines the amount of dithering) from DTHR to
FRS. If dithering is not used, short DTHR to VB pin.
This pin controls the switching frequency of the DC-DC converter. Tie a resistor from this pin to
4 FRS I
RTN to set the frequency.
Primary auxiliary power detect input. Raise 1.5 V above RTN to disable pass MOSFET, also
5 APD I
turning class off. If not used, connect APD to RTN.
7, 8, 9 RTN - RTN is the output of the PoE hotswap and the reference ground for the DC-DC controller.
Automatic MPS enable input, referenced to RTN, internally pulled-up to 5-V internal rail. Tie to
11 EMPS I
RTN to disable automatic MPS.
Indicates that a PSE applying an IEEE802.3bt (Type 3 or 4) mutual identification scheme has been
12 BT O identified. Open-drain, active-low output referenced to RTN. BT state remains unchanged if an
auxiliary power adapter is detected via APD or PPD input. BT is also disabled if SCDIS is low.
13 TPH O TPH/TPL binary code indicates the PSE allocated power output. Open-drain, active-low outputs
referenced to RTN. The default operation is with parallel binary code. Also, whenever an auxiliary
power adapter is detected via the APD input or PPD input, both TPH and TPL pull low. Serial
14 TPL O code over TPL can also be enabled by tying SCDIS pin to VSS. In this case, TPH becomes high
impedance.
17 REF O Internal 1.25-V voltage reference. Connect a 49.9-kOhm_1% resistor from REF to VSS.
TPL serial code disable, referenced to VSS. Leave open to select parallel TPH/TPL configuration.
18 SCDIS I
Tie to VSS to select serial code.
Raising V above 2.5 V enables the hotswap MOSFET, activates TPH and TPL and turn
19 PPD I PPD-VSS
class off. Tie PPD to VSS or float when not used.
20 CLSB O Connect a resistor from CLSB to VSS to program the second classification current.
21 CLSA O Connect a resistor from CLSA to VSS to program the first classification current.
Positive input power rail for PoE interface circuit and source of DC-DC converter start-up current.
23 VDD -
Bypass with a 0.1 uF to VSS and protect with a TVS.
Connect a 25.5-kOhm resistor from DEN to VDD to provide the PoE detection signature. Pulling this
24 DEN I/O
pin to VSS during powered operation causes the internal hotswap MOSFET to turn off.
27, 28 VSS - Negative power rail derived from the PoE source.
30 TEST O Used internally for test purposes only. Leave open.
Connect a resistor from DT to AGND to set the GATE to GAT2 dead time. Tie DT to VB to disable
31 DT I
GAT2 operation.
This pin sets the SST discharge current during a soft-stop event independently from the setting
32 I_STP I used during a regular soft-start event. Connect a resistor from this pin to AGND to set the DC/DC
soft-stop rate.
A capacitor from SST to RTN pin sets the soft-start (I charge current) and the hiccup timer (I
SSC SSD
33 SST I/O discharge current) for the DC-DC converter. Connect a capacitor from this pin to RTN to set the
DC/DC startup rate.
Converter error amplifier inverting (feedback) input. If flyback configuration with primary-side
regulation, it is typically driven by a voltage divider and capacitor from the auxiliary winding,
34 FB I
working with CP pin, FB also being connected to the COMP compensation network. If optocoupler
feedback is enabled, tie FB to VB.
Compensation output of the DC-DC convertor error amplifier or control loop input to the PWM. If
the internal error amplifier is used, connect the compensation networks from this pin to the FB pin
35 COMP I/O
to compensate the converter. If optocoupler feedback is enabled, the optocoupler and its network
pulled up to VB directly drives the COMP pin.
Error Amplifier disable input, referenced to AGND, internally pulled-up to 5V internal rail. Leave
36 EA_DIS I EA_DIS open to disable the Error amplifier, to enable optocoupler feedback for example. Connect
to AGND otherwise.
4 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS23730
```

### Page 5

#### Extracted tables

Table 1:

```text
PIN |  | I/O | DESCRIPTION
NO. | NAME |  | 
37 | VB | O | 5-V bias rail for DC/DC control circuits and the feedback optocoupler (when in use). Connect a 0.1-uF capacitor from this pin to AGND to provide bypassing.
38 | LINEUV | I | LINEUV is used to monitor the bulk capacitor voltage to trigger a soft-stop event when an undervoltage condition is detected if APD is low. If not used, connect LINEUV to VB pin.
39 | PSRS | I | PSR Sync enable input, referenced to AGND, internally pulled-up to 5V internal rail. PSRS works with CP pin to support flyback architecture using primary-side regulation. Leave PSRS open if the flyback output stage is configured with synchronous rectification and uses PSR. If diode rectification is used, or for applications not using PSR, connect PSRS to AGND.
40 | VBG | O | 5-V bias rail for the switching FET gate driver circuit. For internal use only. Bypass with a 0.1-uF ceramic capacitor to GND pin.
41 | GAT2 | O | Gate drive output for a second DC-DC converter switching MOSFET.
42 | VCC | I/O | DC/DC converter bias voltage. The internal startup current source and converter bias winding output power this pin. Connect a 1uF minimum ceramic capacitor to RTN.
43 | GATE | O | Gate drive output for the main DC-DC converter switching MOSFET
44 | CP | O | CP provides the clamp for the primary-side regulation loop. Connect this pin to the lower end of the bias winding of the flyback transformer.
45 | GND |  | .Power ground used by the flyback power FET gate driver and CP. Connect to RTN.
6, 10, 15, 16, 22, 25, 26, 29 | NC |  | No connect pin. Leave open.
47 | PAD_S |  | The exposed thermal pad must be connected to VSS. A large fill area is required to assist in heat dissipation.
46 | PAD_G |  | The exposed thermal pad must be connected to RTN. A large fill area is required to assist in heat dissipation.
```

#### Raw extracted text

```text
Table 6-1. Pin Functions (continued)
PIN
I/O DESCRIPTION
NO. NAME
37 VB O 5-V bias rail for DC/DC control circuits and the feedback optocoupler (when in use). Connect a
0.1-uF capacitor from this pin to AGND to provide bypassing.
38 LINEUV I LINEUV is used to monitor the bulk capacitor voltage to trigger a soft-stop event when an
undervoltage condition is detected if APD is low. If not used, connect LINEUV to VB pin.
39 PSRS I
PSR Sync enable input, referenced to AGND, internally pulled-up to 5V internal rail. PSRS works
with CP pin to support flyback architecture using primary-side regulation. Leave PSRS open if
the flyback output stage is configured with synchronous rectification and uses PSR. If diode
rectification is used, or for applications not using PSR, connect PSRS to AGND.
40 VBG O 5-V bias rail for the switching FET gate driver circuit. For internal use only. Bypass with a 0.1-uF
ceramic capacitor to GND pin.
41 GAT2 O Gate drive output for a second DC-DC converter switching MOSFET.
42 VCC I/O DC/DC converter bias voltage. The internal startup current source and converter bias winding
output power this pin. Connect a 1uF minimum ceramic capacitor to RTN.
43 GATE O Gate drive output for the main DC-DC converter switching MOSFET
44 CP O CP provides the clamp for the primary-side regulation loop. Connect this pin to the lower end of the
bias winding of the flyback transformer.
45 GND - .Power ground used by the flyback power FET gate driver and CP. Connect to RTN.
6, 10, 15,
16, 22, 25,
26, 29
NC - No connect pin. Leave open.
47 PAD_S - The exposed thermal pad must be connected to VSS. A large fill area is required to assist in heat
dissipation.
46 PAD_G - The exposed thermal pad must be connected to RTN. A large fill area is required to assist in heat
dissipation.
www.ti.com
TPS23730
SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 5
Product Folder Links: TPS23730
```

### Page 6

#### Extracted tables

Table 1:

```text
|  | MIN | MAX | UNIT
Input voltage | VDD, DEN, GND, AGND, RTN(2) | 0.3 100 |  | V
 | VDD to RTN | 0.3 100 |  | 
 | APD, FB, CS, EA_DIS, LINEUV, PSRS, EMPS, all to RTN | 0.3 6.5 |  | 
Input voltage | PPD, SCDIS(3) | 0.3 6.5 |  | V
Voltage | FRS(3), COMP, VB(3), VBG(3), I_STP(3), DTHR(3), SST(3), DT(3), BT, all to RTN | 0.3 6.5 |  | V
 | VCC to RTN | 0.3 19 |  | 
 | GATE(3) , GAT2(3), all to RTN | 0.3 VCC+0.3 |  | 
 | CP to GND | 0.3 60 |  | 
 | GND, AGND, all to RTN | 0.3 0.3 |  | 
 | REF(3) , CLSA(3), CLSB(3) | 0.3 6.5 |  | 
 | TPH, TPL, all to RTN | 0.3 19 |  | 
Sourcing current | VB, VBG, VCC | Internally limited |  | mA
 | COMP | Internally limited |  | 
 | REF | Internally limited |  | 
Sourcing current | CLSA, CLSB | 65 |  | mA
Sinking current | RTN | Internally limited |  | mA
 | DEN | 1 |  | 
 | COMP | Internally limited |  | 
Sinking current | TPH, TPL, BT | 10 |  | mA
Peak sourcing current | CP | 2 |  | A
Peak sinking current | CP | 0.7 |  | A
T J(max) | Maximum junction temperature | Internally Limited |  | deg C
T stg | Storage temperature | 65 150 |  | deg C
```

Table 2:

```text
|  |  | VALUE | UNIT
V (ESD) | Electrostatic discharge | Human-body model (HBM), per ANSI/ESDA/JEDEC JS-001(1) | +/-2000 | V
 |  | Charged-device model (CDM), per JEDEC specification JESD22-C101(2) | +/-500 | 
 |  | IEC 61000-4-2 contact discharge(3) | +/-8000 | 
 |  | IEC 61000-4-2 air-gap discharge(3) | +/-15000 |
```

#### Raw extracted text

```text
TPS23730
SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020 www.ti.com
7 Specifications
7.1 Absolute Maximum Ratings
Voltage are with respect to V (unless otherwise noted)(1)
SS
MIN MAX UNIT
VDD, DEN, GND, AGND, RTN(2) -0.3 100
Input voltage VDD to RTN -0.3 100 V
APD, FB, CS, EA_DIS, LINEUV, PSRS, EMPS, all to RTN -0.3 6.5
Input voltage PPD, SCDIS(3) -0.3 6.5 V
FRS(3), COMP, VB(3), VBG(3), I_STP(3), DTHR(3), SST(3), DT(3), BT,
-0.3 6.5
all to RTN
VCC to RTN -0.3 19
GATE(3) , GAT2(3), all to RTN -0.3 VCC+0.3
Voltage V
CP to GND -0.3 60
GND, AGND, all to RTN -0.3 0.3
REF(3) , CLSA(3), CLSB(3) -0.3 6.5
TPH, TPL, all to RTN -0.3 19
VB, VBG, VCC Internally limited
Sourcing current COMP Internally limited mA
REF Internally limited
Sourcing current CLSA, CLSB 65 mA
RTN Internally limited
Sinking current DEN 1 mA
COMP Internally limited
Sinking current TPH, TPL, BT 10 mA
Peak sourcing
CP 2 A
current
Peak sinking current CP 0.7 A
T Maximum junction temperature Internally Limited  deg C
J(max)
T Storage temperature -65 150  deg C
stg
(1) Stresses beyond those listed under Absolute Maximum Ratings may cause permanent damage to the device. These are stress
ratings only, which do not imply functional operation of the device at these or any other conditions beyond those indicated under
Recommended Operating Conditions. Exposure to absolute-maximum-rated conditions for extended periods may affect device
reliability.
(2) I = 0 for V > 80 V.
RTN RTN
(3) Do not apply voltage to these pins.
7.2 ESD Ratings
VALUE UNIT
Human-body model (HBM), per ANSI/ESDA/JEDEC JS-001(1) +/-2000
Charged-device model (CDM), per JEDEC specification JESD22-C101(2) +/-500
V Electrostatic discharge V
(ESD) IEC 61000-4-2 contact discharge(3) +/-8000
IEC 61000-4-2 air-gap discharge(3) +/-15000
(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process.
(2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process.
(3) Surges per EN61000-4-2, 1999 applied between RJ-45 and output ground and between adapter input and output ground of
the TPS23730, TPS23730EVM-093 evaluation module (documentation available on the web). These were the test levels, not the
failure threshold.
6 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS23730
```

### Page 7

#### Extracted tables

Table 1:

```text
|  | MIN | NOM | MAX | UNIT
Input voltage range | VDD, RTN, GND, AGND | 0 60 |  |  | V
 | VCC to RTN | 0 16 |  |  | 
 | APD, EA_DIS, LINEUV, PSRS, FB, all to RTN | 0 VB |  |  | 
 | CS to RTN | 0 2 |  |  | 
 | CP to GND | 0 45 |  |  | 
Input voltage range | PPD | 0 5 |  |  | V
Voltage range | COMP, BT, all to RTN | VB |  |  | V
Voltage range | TPH, TPL, all to RTN | 0 VCC |  |  | V
Sinking current | RTN | 1.2 |  |  | A
Sinking current | TPH, TPL, BT | 3 |  |  | mA
Sourcing current | VCC | 20 |  |  | mA
 | VB | 5 |  |  | 
Capacitance | VB, VBG(1) | 0.08 0.1 1 |  |  | uF
 | VCC | 0.7 1 100 |  |  | 
Resistance | I_STOP | 16.5 499 |  |  | KOhm
Resistance | CLSA, CLSB(1) | 30 |  |  | Ohm
 | REF(1) | 48.9 49.9 50.9 |  |  | kOhm
 | Synchronization pulse width input (when used) | 35 |  |  | ns
T J | Operating junction temperature | 40 125 |  |  | deg C
```

Table 2:

```text
|  | TPS23730 | 
THERMAL METRIC |  | RMT (VQFN) | UNIT
 |  | 45 PINS | 
R (1) JA | Junction-to-ambient thermal resistance | 38.5 | deg C/W
R JC(top) | Junction-to-case (top) thermal resistance | 23.6 | 
R (1) JB | Junction-to-board thermal resistance | 19.3 | 
(1) JT | Junction-to-top characterization parameter | 6.8 | 
(1) JB | Junction-to-board characterization parameter | 19.3 | 
R JC(bot_POE) | Junction-to-case (bottom PAD_S pad) thermal resistance | 3.9 | 
R JC(bot_DCDC) | Junction-to-case (bottom PAD_G pad) thermal resistance | 9.1 |
```

#### Raw extracted text

```text
TPS23730
www.ti.com SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020
7.3 Recommended Operating Conditions
Voltage with respect to V (unless otherwise noted)
SS
MIN NOM MAX UNIT
VDD, RTN, GND, AGND 0 60
VCC to RTN 0 16
Input voltage range APD, EA_DIS, LINEUV, PSRS, FB, all to RTN 0 VB V
CS to RTN 0 2
CP to GND 0 45
Input voltage range PPD 0 5 V
Voltage range COMP, BT, all to RTN VB V
Voltage range TPH, TPL, all to RTN 0 VCC V
Sinking current RTN 1.2 A
Sinking current TPH, TPL, BT 3 mA
VCC 20
Sourcing current mA
VB 5
VB, VBG(1) 0.08 0.1 1
Capacitance uF
VCC 0.7 1 100
Resistance I_STOP 16.5 499 KOhm
CLSA, CLSB(1) 30 Ohm
Resistance
REF(1) 48.9 49.9 50.9 kOhm
Synchronization pulse width input (when used) 35 ns
T Operating junction temperature -40 125  deg C
J
(1) Voltage should not be externally applied to this pin.
7.4 Thermal Information
TPS23730
THERMAL METRIC RMT (VQFN) UNIT
45 PINS
R (1) Junction-to-ambient thermal resistance 38.5
JA
R Junction-to-case (top) thermal resistance 23.6
JC(top)
R (1) Junction-to-board thermal resistance 19.3
JB
 (1) Junction-to-top characterization parameter 6.8  deg C/W
JT
 (1) Junction-to-board characterization parameter 19.3
JB
R Junction-to-case (bottom PAD_S pad) thermal resistance 3.9
JC(bot_POE)
R Junction-to-case (bottom PAD_G pad) thermal resistance 9.1
JC(bot_DCDC)
(1) Thermal metrics are not JEDEC standard values and are based on the TPS23731EVM-095 evaluation board.
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 7
Product Folder Links: TPS23730
```

### Page 8

#### Extracted tables

Table 1:

```text
PARAMETER |  | TEST CONDITIONS | MIN | TYP | MAX | UNIT
DC-DC SUPPLY (VCC) |  |  |  |  |  | 
V CUVLO_ R | Undervoltage lockout | V rising VCC | 8 8.25 8.5 |  |  | V
V CUVLO_F |  | V falling, V = V VCC FB RTN | 5.85 6.1 6.35 |  |  | V
V CUVLO_ H |  | Hysteresis(1) | 2 2.15 2.3 |  |  | V
I RUN | Operating current | V = 10 V, V = V , R = 24.9 kOhm, CP with VCC FB RTN DT 2-kOhm pull up to 30 V | 1.2 2 2.4 |  |  | mA
I VC_ST | Startup source current | V = 2.5 V APD |  |  |  | 
 |  | V >= 28 V, V = 11.7 V VDD VCC | 21.5 30 34 |  |  | mA
 |  | V = 10.2 V, V = 8.6 V VDD VCC | 1 6 17.5 |  |  | 
 |  | V = 10.2 V, V = 6.8 V VDD VCC | 8 16 32 |  |  | 
t ST | Startup time, C = 1 uF VCC | V = 10.2 V, V (0) = 0 V, measure time until VDD VCC V CUVLO_R | 0.25 0.7 1.15 |  |  | ms
 |  | V = 35 V, V (0) = 0 V, measure time until VDD VCC V CUVLO_R | 0.24 0.35 0.48 |  |  | ms
V VC_ST | VCC startup voltage | Measure V during startup, I = 0 mA VCC VCC | 11 12.5 14 |  |  | V
 |  | Measure V during startup, I = 21.5 mA VCC VCC | 11 12.5 14 |  |  | 
V VC_SSTP | VCC soft-stop voltage | V < V , Measure V during soft-stop, I LINEUV LIUVF VCC VCC = 0 mA | 11 12.5 14 |  |  | V
 |  | V < V , Measure V during soft-stop, I LINEUV LIUVF VCC VCC = 21.5 mA | 11 12.5 14 |  |  | 
V B |  |  |  |  |  | 
 | Voltage | V = V , 8.5 V <= V <= 16 V, 0 <= I <= 5 mA FB RTN VCC VB | 4.75 5.0 5.25 |  |  | V
DC-DC TIMING (FRS) |  |  |  |  |  | 
f SW | Switching frequency | V = V , Measure at GATE FB RTN | 223 248 273 |  |  | kHz
D MAX | Duty cycle | V = V , R = 24.9 kOhm, Measure at GATE FB RTN DT | 74.5% 78.5% 82.5% |  |  | 
V SYNC | Synchronization | Input threshold | 2 2.2 2.4 |  |  | V
FREQUENCY DITHERING RAMP GENERATOR (DTHR) |  |  |  |  |  | 
I DTRCH | Charging (sourcing) current | 0.5 V < V < 1.5 V DTHR | 3 x I FRS |  |  | uA
 |  |  | 47.2 49.6 52.1 |  |  | uA
I DTRDC | Discharging (sinking) current | 0.5 V < V < 1.5 V DTHR | 3 x I FRS |  |  | uA
 |  |  | 47.2 49.6 52.1 |  |  | uA
V DTUT | Dithering upper threshnold | V rising until I > 0 DTHR DTHR | 1.41 1.513 1.60 |  |  | V
V DTLT | Dithering lower threshold | V falling until I < 0 DTHR DTHR | 0.43 0.487 0.54 |  |  | V
V DTPP | Dithering pk-pk amplitude |  | 1.005 1.026 1.046 |  |  | V
ERROR AMPLIFIER (FB, COMP) |  |  |  |  |  | 
V REFC | Feedback regulation voltage |  | 1.723 1.75 1.777 |  |  | V
I FB_LK | FB leakage current (source or sink) | V = 1.75 V FB | 0.5 |  |  | uA
G BW | Small signal unity gain bandwidth |  | 0.9 1.2 |  |  | MHz
A OL | Open loop voltage gain |  | 70 80 |  |  | db
V ZDC | 0% duty-cycle threshold | V falling until GATE switching stops COMP | 1.35 1.5 1.65 |  |  | V
```

#### Raw extracted text

```text
TPS23730
SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020 www.ti.com
7.5 Electrical Characteristics: DC-DC Controller Section
Unless otherwise noted, V = 48 V; R = 25.5 kOhm; R = 60.4 kOhm; R = 499 kOhm; CLSA, CLSB, TPH, TPL, BT,
VDD DEN FRS I_STP
SCDIS and PSRS open; CS, EA_DIS, APD, EMPS, AGND and GND connected to RTN; FB, LINEUV, DT and DTHR
connected to VB; PPD connected to VSS; C = C = 0.1 uF; C = 1 uF; C = 0.047 uF; R = 49.9 kOhm; 8.5 V <=
VB VBG VCC SST REF
V <= 16 V; -40 deg C <= T <= 125 deg C. Positive currents are into pins unless otherwise noted. Typical values are at 25 deg C.
VCC J
[V = V ], all voltages referred to V , V and V unless otherwise noted.
VSS RTN RTN AGND GND
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
DC-DC SUPPLY (VCC)
V
CUVLO_ V rising 8 8.25 8.5 V
VCC
R
V Undervoltage lockout V falling, V = V 5.85 6.1 6.35 V
CUVLO_F VCC FB RTN
V
CUVLO_ Hysteresis(1) 2 2.15 2.3 V
H
V = 10 V, V = V , R = 24.9 kOhm, CP with
I Operating current VCC FB RTN DT 1.2 2 2.4 mA
RUN 2-kOhm pull up to 30 V
V = 2.5 V
APD
V >= 28 V, V = 11.7 V 21.5 30 34
VDD VCC
I Startup source current
VC_ST
V = 10.2 V, V = 8.6 V 1 6 17.5 mA
VDD VCC
V = 10.2 V, V = 6.8 V 8 16 32
VDD VCC
V = 10.2 V, V (0) = 0 V, measure time until
VDD VCC 0.25 0.7 1.15 ms
V
CUVLO_R
t Startup time, C = 1 uF
ST VCC
V = 35 V, V (0) = 0 V, measure time until
VDD VCC 0.24 0.35 0.48 ms
V
CUVLO_R
Measure V during startup, I = 0 mA 11 12.5 14
VCC VCC
V VCC startup voltage V
VC_ST
Measure V during startup, I = 21.5 mA 11 12.5 14
VCC VCC
V < V , Measure V during soft-stop, I
LINEUV LIUVF VCC VCC 11 12.5 14
= 0 mA
V VCC soft-stop voltage V
VC_SSTP
V < V , Measure V during soft-stop, I
LINEUV LIUVF VCC VCC 11 12.5 14
= 21.5 mA
V
B
Voltage V = V , 8.5 V <= V <= 16 V, 0 <= I <= 5 mA 4.75 5.0 5.25 V
FB RTN VCC VB
DC-DC TIMING (FRS)
f Switching frequency V = V , Measure at GATE 223 248 273 kHz
SW FB RTN
D Duty cycle V = V , R = 24.9 kOhm, Measure at GATE 74.5% 78.5% 82.5%
MAX FB RTN DT
V Synchronization Input threshold 2 2.2 2.4 V
SYNC
FREQUENCY DITHERING RAMP GENERATOR (DTHR)
3 x I uA
FRS
I Charging (sourcing) current 0.5 V < V < 1.5 V
DTRCH DTHR
47.2 49.6 52.1 uA
3 x I uA
FRS
I Discharging (sinking) current 0.5 V < V < 1.5 V
DTRDC DTHR
47.2 49.6 52.1 uA
V Dithering upper threshnold V rising until I > 0 1.41 1.513 1.60 V
DTUT DTHR DTHR
V Dithering lower threshold V falling until I < 0 0.43 0.487 0.54 V
DTLT DTHR DTHR
V Dithering pk-pk amplitude 1.005 1.026 1.046 V
DTPP
ERROR AMPLIFIER (FB, COMP)
V Feedback regulation voltage 1.723 1.75 1.777 V
REFC
FB leakage current (source or
I V = 1.75 V 0.5 uA
FB_LK sink) FB
Small signal unity gain
G 0.9 1.2 MHz
BW bandwidth
A Open loop voltage gain 70 80 db
OL
V 0% duty-cycle threshold V falling until GATE switching stops 1.35 1.5 1.65 V
ZDC COMP
8 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS23730
```

### Page 9

#### Extracted tables

Table 1:

```text
PARAMETER |  | TEST CONDITIONS |  | MIN | TYP | MAX | UNIT
I COMPH | COMP source current | V = V , V = 3 V FB RTN COMP |  | 1 |  |  | mA
I COMPL | COMP sink current | V = V , V = 1.25 V FB VB COMP |  | 2.1 6 |  |  | mA
V COMPH | COMP high voltage | V = V , 15 kOhm from COMP to RTN FB RTN |  | 4 VB |  |  | V
V COMPL | COMP low voltage | V = V , 15 kOhm from COMP to VB FB VB |  | 1.1 |  |  | V
 | COMP input resistance, error amplifier disabled | EA_DIS open |  | 70 100 130 |  |  | kOhm
 | COMP to CS gain | V / V , 0 V < V < 0.22 V CS COMP CS |  | 0.19 0.2 0.21 |  |  | V/V
SOFT-START, SOFT-STOP (SST, I_STP) |  |  |  |  |  |  | 
I SSC | Charge current | SST charging, 6.35 V <= V <= 16 V VCC |  | 7.5 10 12.5 |  |  | uA
I SSD | Discharge current | SST discharging, 6.35 V <= V <= 16 V VCC |  | 3 4 5 |  |  | uA
V SFST | Soft-start lower threshold |  |  | 0.15 0.2 0.25 |  |  | V
V STUOF | Startup turn off threshold | V rising until VCC startup turns off SST |  | 1.99 2.1 2.21 |  |  | V
V SSOFS | Soft-start offset voltage, closed-loop mode | V = V , V rising until start of switching FB RTN SST |  | 0.2 0.25 0.3 |  |  | V
 | Soft-start offset voltage, peak current mode | V = V , V rising until start of switching, COMP VB SST EA_DIS open |  | 0.55 0.6 0.65 |  |  | V
V SSCL | Soft-start clamp |  |  | 2.3 2.6 |  |  | V
I SSD_SP | SST discharge current in soft- stop mode | R = 499 kOhm, V < V I_STP LINEUV LIUVF |  | 1.5 2 2.5 |  |  | uA
 |  | R = 16.5 kOhm, , V < V I_STP LINEUV LIUVF |  | 52.5 60.6 67.5 |  |  | 
V SSTPEN D | End of soft-stop threshold | V = V , V < V FB RTN LINEUV LIUVF |  | 0.15 0.2 0.25 |  |  | V
CURRENT SENSE (CS) |  |  |  |  |  |  | 
V CSMAX | Maximum threshold voltage | V = V , V rising FB RTN CS |  | 0.227 0.25 0.273 |  |  | V
t OFFD_IL | Current limit turn off delay | V = 0.3 V CS |  | 25 41 60 |  |  | ns
t OFFD_PW | PWM comparator turn off delay | V = 0.15 V, EA_DIS open, V = 2 V CS COMP |  | 25 41 60 |  |  | ns
 | Blanking delay | In addtition to t and t OFFD_IL OFFD_PW |  | 75 95 115 |  |  | ns
V SLOPE | Internal slope compensation voltage | V = V , Peak voltage at maximum duty cycle, FB RTN referred to CS |  | 51 66 79 |  |  | mV
I SL_EX | Peak slope compensation current | V = V , I at maximum duty cycle (ac FB RTN CS component) |  | 14 20 26 |  |  | uA
 | Bias current | DC component of CS current |  | 3 -2 -1 |  |  | uA
LINE UNDERVOLTAGE, SOFT-STOP (LINEUV) |  |  |  |  |  |  | 
V LIUVF | LINEUV falling threshold voltage | V falling LINEUV |  | 2.86 2.918 2.976 |  |  | V
V LIUVH |  | Hysteresis(1) |  | 57 82 107 |  |  | mV
 | Leakage current | V = 3 V LINEUV |  | 1 |  |  | uA
DEAD TIME (DT) |  |  |  |  |  |  | 
t DT1 | Dead time | R = 24.9 kOhm, GAT2 to DT GATE | V = V , V FB RTN PSRS = 0 V, EA_DIS open, V = V , C COMP VB GATE = 1 nF, C = 0.5 GAT2 nF, V = 10 V VCC | 40 50 62.5 |  |  | ns
t DT2 |  | R = 24.9 kOhm, GATE to DT GAT2 |  | 40 50 62.5 |  |  | 
t DT1 |  | R = 75 kOhm, GAT2 to GATE DT |  | 120 150 188 |  |  | 
t DT2 |  | R = 75 kOhm, GATE to GAT2 DT |  | 120 150 188 |  |  |
```

#### Raw extracted text

```text
TPS23730
www.ti.com SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020
7.5 Electrical Characteristics: DC-DC Controller Section (continued)
Unless otherwise noted, V = 48 V; R = 25.5 kOhm; R = 60.4 kOhm; R = 499 kOhm; CLSA, CLSB, TPH, TPL, BT,
VDD DEN FRS I_STP
SCDIS and PSRS open; CS, EA_DIS, APD, EMPS, AGND and GND connected to RTN; FB, LINEUV, DT and DTHR
connected to VB; PPD connected to VSS; C = C = 0.1 uF; C = 1 uF; C = 0.047 uF; R = 49.9 kOhm; 8.5 V <=
VB VBG VCC SST REF
V <= 16 V; -40 deg C <= T <= 125 deg C. Positive currents are into pins unless otherwise noted. Typical values are at 25 deg C.
VCC J
[V = V ], all voltages referred to V , V and V unless otherwise noted.
VSS RTN RTN AGND GND
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
I COMP source current V = V , V = 3 V 1 mA
COMPH FB RTN COMP
I COMP sink current V = V , V = 1.25 V 2.1 6 mA
COMPL FB VB COMP
V COMP high voltage V = V , 15 kOhm from COMP to RTN 4 VB V
COMPH FB RTN
V COMP low voltage V = V , 15 kOhm from COMP to VB 1.1 V
COMPL FB VB
COMP input resistance, error
EA_DIS open 70 100 130 kOhm
amplifier disabled
COMP to CS gain V / V , 0 V < V < 0.22 V 0.19 0.2 0.21 V/V
CS COMP CS
SOFT-START, SOFT-STOP (SST, I_STP)
I Charge current SST charging, 6.35 V <= V <= 16 V 7.5 10 12.5 uA
SSC VCC
I Discharge current SST discharging, 6.35 V <= V <= 16 V 3 4 5 uA
SSD VCC
V Soft-start lower threshold 0.15 0.2 0.25 V
SFST
V Startup turn off threshold V rising until VCC startup turns off 1.99 2.1 2.21 V
STUOF SST
Soft-start offset voltage,
V = V , V rising until start of switching 0.2 0.25 0.3 V
closed-loop mode FB RTN SST
V
SSOFS
Soft-start offset voltage, peak V = V , V rising until start of switching,
COMP VB SST 0.55 0.6 0.65 V
current mode EA_DIS open
V Soft-start clamp 2.3 2.6 V
SSCL
SST discharge current in soft- R I_STP = 499 kOhm, V LINEUV < V LIUVF 1.5 2 2.5
I uA
SSD_SP stop mode R = 16.5 kOhm, , V < V 52.5 60.6 67.5
I_STP LINEUV LIUVF
V
SSTPEN End of soft-stop threshold V = V , V < V 0.15 0.2 0.25 V
FB RTN LINEUV LIUVF
D
CURRENT SENSE (CS)
V Maximum threshold voltage V = V , V rising 0.227 0.25 0.273 V
CSMAX FB RTN CS
t Current limit turn off delay V = 0.3 V 25 41 60 ns
OFFD_IL CS
PWM comparator turn off
t V = 0.15 V, EA_DIS open, V = 2 V 25 41 60 ns
OFFD_PW delay CS COMP
Blanking delay In addtition to t and t 75 95 115 ns
OFFD_IL OFFD_PW
Internal slope compensation V = V , Peak voltage at maximum duty cycle,
V FB RTN 51 66 79 mV
SLOPE voltage referred to CS
Peak slope compensation V = V , I at maximum duty cycle (ac
I FB RTN CS 14 20 26 uA
SL_EX current component)
Bias current DC component of CS current -3 -2 -1 uA
LINE UNDERVOLTAGE, SOFT-STOP (LINEUV)
V LIUVF LINEUV falling threshold V LINEUV falling 2.86 2.918 2.976 V
V voltage Hysteresis(1) 57 82 107 mV
LIUVH
Leakage current V = 3 V 1 uA
LINEUV
DEAD TIME (DT)
R = 24.9 kOhm, GAT2  to
t DT 40 50 62.5
DT1 GATE
V = V , V
FB RTN PSRS
t R DT = 24.9 kOhm, GATE  to = 0 V, EA_DIS open, 40 50 62.5
DT2 GAT2  V = V , C
Dead time COMP VB GATE ns
t DT1  R DT = 75 kOhm, GAT2  to GATE n = F 1 , nF, C GAT2 = 0.5 120 150 188
V = 10 V
VCC
R = 75 kOhm, GATE  to GAT2
t DT 120 150 188
DT2
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 9
Product Folder Links: TPS23730
```

### Page 10

#### Extracted tables

Table 1:

```text
PARAMETER |  | TEST CONDITIONS | MIN | TYP | MAX | UNIT
GATE |  |  |  |  |  | 
 | Peak source current | V = V , V = 10 V, V = 0 V, pulsed FB RTN VCC GATE measurement | 0.3 0.5 0.8 |  |  | A
 | Peak sink current | V = V , V = 10 V, V = 10 V, pulsed FB RTN VCC GATE measurement | 0.6 0.9 1.45 |  |  | A
 | Rise time(2) | t , C = 1 nF, V = 10 V prr10-90 GATE VCC | 30 |  |  | ns
 | Fall time(2) | t , C = 1 nF, V = 10 V pff90-10 GATE VCC | 15 |  |  | ns
GAT2 |  |  |  |  |  | 
 | Peak source current | V = V , V = 10 V, R = 24.9 kOhm, V = 0 V, FB RTN VCC DT GAT2 pulsed measurement | 0.3 0.5 0.8 |  |  | A
 | Peak sink current | V = V , V = 10 V, R = 24.9 kOhm, V = 10 FB RTN VCC DT GAT2 V, pulsed measurement | 0.3 0.45 0.72 |  |  | A
 | Rise time(2) | t , C = 0.5 nF , V = 10 V prr10-90 GAT2 VCC | 15 |  |  | ns
 | Fall time(2) | t , C = 0.5 nF , V = 10 V pff90-10 GAT2 VCC | 15 |  |  | ns
CLAMPING FET (CP) |  |  |  |  |  | 
R DS(ON)C L | CP FET on resistance | I = 100 mA CP | 1.5 3.3 |  |  | Ohm
CLAMPING DIODE (CP) |  |  |  |  |  | 
V FCP | CP Diode forward voltage | V = 0 V, I = 15 mA PSRS CP | 0.45 0.6 0.85 |  |  | V
 | CP Leakage current | V = 0 V, V = 45 V PSRS CP | 20 |  |  | uA
AUXILIARY POWER DETECTION (APD) |  |  |  |  |  | 
V APDEN | APD threshold voltage | V rising APD | 1.42 1.5 1.58 |  |  | V
V APDH |  | Hysteresis(1) | 0.075 0.095 0.115 |  |  | V
 | Leakage current | V = 5 V APD | 1 |  |  | uA
PPD |  |  |  |  |  | 
V PPDEN | PPD threshold voltage | V > 16 V, V - V rising, PD input UVLO VDD PPD VSS disable | 2.34 2.5 2.66 |  |  | V
V PPDH |  | Hysteresis(1) | 0.47 0.5 0.53 |  |  | 
I PPD | PPD sink current | V - V = 3 V PPD VSS | 2.5 5 7.5 |  |  | uA
THERMAL SHUTDOWN |  |  |  |  |  | 
 | Turnoff temperature |  | 145 155 165 |  |  | deg C
 | Hysteresis(2) |  | 15 |  |  | deg C
```

#### Raw extracted text

```text
TPS23730
SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020 www.ti.com
7.5 Electrical Characteristics: DC-DC Controller Section (continued)
Unless otherwise noted, V = 48 V; R = 25.5 kOhm; R = 60.4 kOhm; R = 499 kOhm; CLSA, CLSB, TPH, TPL, BT,
VDD DEN FRS I_STP
SCDIS and PSRS open; CS, EA_DIS, APD, EMPS, AGND and GND connected to RTN; FB, LINEUV, DT and DTHR
connected to VB; PPD connected to VSS; C = C = 0.1 uF; C = 1 uF; C = 0.047 uF; R = 49.9 kOhm; 8.5 V <=
VB VBG VCC SST REF
V <= 16 V; -40 deg C <= T <= 125 deg C. Positive currents are into pins unless otherwise noted. Typical values are at 25 deg C.
VCC J
[V = V ], all voltages referred to V , V and V unless otherwise noted.
VSS RTN RTN AGND GND
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
GATE
V = V , V = 10 V, V = 0 V, pulsed
Peak source current FB RTN VCC GATE 0.3 0.5 0.8 A
measurement
V = V , V = 10 V, V = 10 V, pulsed
Peak sink current FB RTN VCC GATE 0.6 0.9 1.45 A
measurement
Rise time(2) t , C = 1 nF, V = 10 V 30 ns
prr10-90 GATE VCC
Fall time(2) t , C = 1 nF, V = 10 V 15 ns
pff90-10 GATE VCC
GAT2
V = V , V = 10 V, R = 24.9 kOhm, V = 0 V,
Peak source current FB RTN VCC DT GAT2 0.3 0.5 0.8 A
pulsed measurement
V = V , V = 10 V, R = 24.9 kOhm, V = 10
Peak sink current FB RTN VCC DT GAT2 0.3 0.45 0.72 A
V, pulsed measurement
Rise time(2) t , C = 0.5 nF , V = 10 V 15 ns
prr10-90 GAT2 VCC
Fall time(2) t , C = 0.5 nF , V = 10 V 15 ns
pff90-10 GAT2 VCC
CLAMPING FET (CP)
R
DS(ON)C CP FET on resistance I = 100 mA 1.5 3.3 Ohm
CP
L
CLAMPING DIODE (CP)
V CP Diode forward voltage V = 0 V, I = 15 mA 0.45 0.6 0.85 V
FCP PSRS CP
CP Leakage current V = 0 V, V = 45 V 20 uA
PSRS CP
AUXILIARY POWER DETECTION (APD)
V V rising 1.42 1.5 1.58 V
APDEN APD
APD threshold voltage
V Hysteresis(1) 0.075 0.095 0.115 V
APDH
Leakage current V = 5 V 1 uA
APD
PPD
V > 16 V, V - V rising, PD input UVLO
V VDD PPD VSS 2.34 2.5 2.66
PPDEN PPD threshold voltage disable V
V Hysteresis(1) 0.47 0.5 0.53
PPDH
I PPD sink current V - V = 3 V 2.5 5 7.5 uA
PPD PPD VSS
THERMAL SHUTDOWN
Turnoff temperature 145 155 165  deg C
Hysteresis(2) 15  deg C
(1) The hysteresis tolerance tracks the rising threshold for a given device.
(2) These parameters are provided for reference only, and do not constitute part of TI's published device specifications for purposes of TI's
product warranty.
10 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS23730
```

### Page 11

#### Extracted tables

Table 1:

```text
PARAMETER |  | TEST CONDITIONS |  | MIN | TYP | MAX | UNIT
PD DETECTION (DEN) |  |  |  |  |  |  | 
 | Detection bias current | DEN open, V = 10 V, Not in mark, Measure VDD I + I VDD RTN |  | 3.5 6.9 13.9 |  |  | uA
I lkg | DEN leakage current | V = V = 60 V, Float RTN, Measure I DEN VDD DEN |  | 0.1 5 |  |  | uA
 | Detection current | Measure I + I + I , V = 1.4 V VDD DEN RTN VDD |  | 53.5 56.5 58.6 |  |  | uA
 |  | Measure I + I + I , V = 10 V, Not in VDD DEN RTN VDD mark |  | 391 398 406.2 |  |  | uA
V PD_DIS | Hotswap disable threshold | DEN falling |  | 3 4 5 |  |  | V
PD CLASSIFICATION (CLSA, CLSB) |  |  |  |  |  |  | 
I CLS | Classification A, B signature current | R or R = 806 Ohm CLSA CLSB | 13 V <= V <= 21 V, DD Measure I + I + VDD DEN I RTN | 1.9 2.5 2.9 |  |  | mA
 |  | R or R = 130 Ohm CLSA CLSB | 13 V <= V <= 21 V, DD Measure I + I + VDD DEN I RTN | 9.9 10.6 11.3 |  |  | mA
 |  | R or R = 69.8 Ohm CLSA CLSB | 13 V <= V <= 21 V, DD Measure I + I + VDD DEN I RTN | 17.6 18.6 19.4 |  |  | mA
 |  | R or R = 46.4 Ohm CLSA CLSB | 13 V <= V <= 21 V, DD Measure I + I + VDD DEN I RTN | 26.5 27.9 29.3 |  |  | mA
 |  | R or R = 32 Ohm CLSA CLSB | 13 V <= V <= 21 V, DD Measure I + I + VDD DEN I RTN | 37.8 39.9 42 |  |  | mA
V CL_ON | Classification regulator lower threshold rising | V rising, I VDD CLS |  | 11.4 12.2 13 |  |  | V
V CL_H | Classification regulator lower threshold | Hysteresis(1) |  | 0.8 1.2 1.6 |  |  | V
V CU_OFF | Classification regulator upper threshold | V rising, I VDD CLS |  | 21 22 23 |  |  | V
V CU_H |  | Hysteresis(1) |  | 0.5 0.77 1 |  |  | V
V MSR | Mark state reset threshold | V falling VDD |  | 3 3.9 5 |  |  | V
 | Mark state resistance | 2-point measurement at 5 V and 10.1 V |  | 6 10 12 |  |  | kOhm
I lkg | Leakage current | V = 60 V, V = 0 V, V = V , Measure VDD CLS DEN VSS I CLS |  | 1 |  |  | uA
t LCF_PD | Long first class event timing | Class 1st event time duration for short MPS |  | 76 81.5 87 |  |  | ms
RTN (PASS DEVICE) |  |  |  |  |  |  | 
 | ON-resistance |  |  | 0.3 0.55 |  |  | Ohm
I LIM | Current limit | V = 1.5 V, pulsed measurement RTN |  | 1.5 1.85 2.2 |  |  | A
I IRSH | inrush current limit | V = 2 V, V : 20 V -> 48 V, measure I , RTN VDD RTN pulsed measurement |  | 100 140 180 |  |  | mA
 | Inrush current limit with nonstandard UVLO | V - V > V , V = 2 V, V : 0 V -> PPD VSS PPDEN RTN VDD 20 V, measure I , pulsed measurement RTN |  | 100 140 180 |  |  | mA
 | Inrush termination | Percentage of inrush current. |  | 80% 90% 99% |  |  | 
t INR_DEL |  | Inrush delay |  | 80 84 88 |  |  | ms
```

#### Raw extracted text

```text
TPS23730
www.ti.com SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020
7.6 Electrical Characteristics PoE
Unless otherwise noted, V = 48 V; R = 25.5 kOhm; R = 60.4 kOhm; R = 499 kOhm; CLSA, CLSB, TPH, TPL,
VDD DEN FRS I_STP
BT, SCDIS and PSRS open; CS, EA_DIS, APD, EMPS, AGND and GND connected to RTN; FB, LINEUV, DT and DTHR
connected to VB; PPD connected to VSS; C = C = 0.1 uF; C = 1 uF; C = 0.047 uF; R = 49.9 kOhm; -40 deg C <= T
VB VBG VCC SST REF J
<= 125 deg C. Positive currents are into pins unless otherwise noted. Typical values are at 25 deg C.
V = 0 V, all voltages referred to V unless otherwise noted.
VCC-RTN VSS
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
PD DETECTION (DEN)
DEN open, V = 10 V, Not in mark, Measure
Detection bias current VDD 3.5 6.9 13.9 uA
I + I
VDD RTN
I DEN leakage current V = V = 60 V, Float RTN, Measure I 0.1 5 uA
lkg DEN VDD DEN
Measure I + I + I , V = 1.4 V 53.5 56.5 58.6 uA
VDD DEN RTN VDD
Detection current Measure I + I + I , V = 10 V, Not in
VDD DEN RTN VDD 391 398 406.2 uA
mark
Hotswap disable
V DEN falling 3 4 5 V
PD_DIS threshold
PD CLASSIFICATION (CLSA, CLSB)
13 V <= V <= 21 V,
DD
R or R = 806 Ohm Measure I + I + 1.9 2.5 2.9 mA
CLSA CLSB VDD DEN
I
RTN
13 V <= V <= 21 V,
DD
R or R = 130 Ohm Measure I + I + 9.9 10.6 11.3 mA
CLSA CLSB VDD DEN
I
RTN
13 V <= V <= 21 V,
Classification A, B DD
I R or R = 69.8 Ohm Measure I + I + 17.6 18.6 19.4 mA
CLS signature current CLSA CLSB VDD DEN
I
RTN
13 V <= V <= 21 V,
DD
R or R = 46.4 Ohm Measure I + I + 26.5 27.9 29.3 mA
CLSA CLSB VDD DEN
I
RTN
13 V <= V <= 21 V,
DD
R or R = 32 Ohm Measure I + I + 37.8 39.9 42 mA
CLSA CLSB VDD DEN
I
RTN
Classification regulator
V V rising, I  11.4 12.2 13 V
CL_ON lower threshold rising VDD CLS
Classification regulator
V Hysteresis(1) 0.8 1.2 1.6 V
CL_H lower threshold
V CU_OFF Classification regulator V VDD rising, I CLS  21 22 23 V
V upper threshold Hysteresis(1) 0.5 0.77 1 V
CU_H
Mark state reset
V V falling 3 3.9 5 V
MSR threshold VDD
Mark state resistance 2-point measurement at 5 V and 10.1 V 6 10 12 kOhm
V = 60 V, V = 0 V, V = V , Measure
I Leakage current VDD CLS DEN VSS 1 uA
lkg I
CLS
Long first class event
t Class 1st event time duration for short MPS 76 81.5 87 ms
LCF_PD timing
RTN (PASS DEVICE)
ON-resistance 0.3 0.55 Ohm
I Current limit V = 1.5 V, pulsed measurement 1.5 1.85 2.2 A
LIM RTN
V = 2 V, V : 20 V -> 48 V, measure I ,
I inrush current limit RTN VDD RTN 100 140 180 mA
IRSH pulsed measurement
Inrush current limit with V - V > V , V = 2 V, V : 0 V ->
PPD VSS PPDEN RTN VDD 100 140 180 mA
nonstandard UVLO 20 V, measure I , pulsed measurement
RTN
Percentage of inrush current. 80% 90% 99%
Inrush termination
t Inrush delay 80 84 88 ms
INR_DEL
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 11
Product Folder Links: TPS23730
```

### Page 12

#### Extracted tables

Table 1:

```text
PARAMETER |  | TEST CONDITIONS |  | MIN | TYP | MAX | UNIT
 | Foldback voltage threshold | V rising RTN |  | 13.5 14.8 16.1 |  |  | V
 | Foldback deglitch time | V rising to when current limit changes to RTN inrush current limit. This applies in normal operating condition or during auto MPS mode. |  | 1.5 1.8 2.1 |  |  | ms
 | Leakage current | V = V = 100 V, V = V VDD RTN DEN VSS |  | 70 |  |  | uA
PSE TYPE INDICATION (TPL, TPH, BT) |  |  |  |  |  |  | 
V TPL | Output low voltage | I = 1 mA, after 2- or 3-event classification, TPL startup has completed, V = 0 V RTN |  | 0.27 0.5 |  |  | V
V TPH | Output low voltage | I = 1 mA, after 4-event classification, startup TPH has completed, V = 0 V RTN |  | 0.27 0.5 |  |  | V
V BT | Output low voltage | I = 2 mA, after IEEE802.3bt classification, BT startup has completed, V = 0 V RTN |  | 0.27 0.5 |  |  | V
f TPL | TPL frequency | V = 0 V, V = 5 V, after startup has SCDIS APD-RTN completed. |  | 550 625 700 |  |  | Hz
 | TPL duty cycle in PoE operation | V = 0 V, after 4-event classification, after SCDIS startup has completed |  | 24% 25% 26% |  |  | 
 | TPL duty cycle in nonstandard PoE operation | V = 0 V, after startup has completed SCDIS |  | 49% 50% 51% |  |  | 
 | TPL duty cycle in auxiliary supply operation | V = 0 V, V = 5 V, after startup has SCDIS APD-RTN completed. |  | 74% 75% 76% |  |  | 
 | Leakage current | V or V = 10 V or V = 5 V, TPL-RTN TPH-RTN BT-RTN V = 0 V RTN |  | 1 |  |  | uA
 | SCDIS pullup current | V >= V or VDD UVLO_R V = 5 V APD-RTN |  | 14 20 25 |  |  | uA
PD INPUT SUPPLY (VDD) |  |  |  |  |  |  | 
V UVLO_R | Undervoltage lockout threshold | V rising VDD |  | 35.8 37.6 39.5 |  |  | V
V UVLO_F | Undervoltage lockout threshold | V falling VDD |  | 30.5 32 33.6 |  |  | V
V UVLO_H | Undervoltage lockout threshold | Hysteresis (1) |  | 5.7 6.0 6.3 |  |  | V
I VDD_ON | Operating current | 40 V <= V <= 60 V, Startup completed, V = VDD VCC 10 V, Measure I VDD |  | 650 1040 |  |  | uA
I VDD_OFF | Off-state current | RTN, GND and VCC open, V = 30 V, Measure VDD I VDD |  | 730 |  |  | uA
MPS |  |  |  |  |  |  | 
I MPSL | MPS total VSS current for Type 1-2 PSE | EMPS open, inrush delay has completed, 0 mA <= I <= 10 mA, measure I RTN VSS |  | 10 12.5 15.5 |  |  | mA
I MPSH | MPS total VSS current for Type 3-4 PSE | EMPS open, inrush delay has completed, 0 mA <= I <= 16 mA, measure I RTN VSS |  | 16.25 19 21.5 |  |  | mA
 | MPS pulsed mode duty cycle for Type 1-2 PSE | MPS pulsed current duty-cycle | EMPS open | 26.2% 26.6% 26.9% |  |  | 
t MPSL |  | MPS pulsed current ON time | EMPS open | 76 81.5 87 |  |  | ms
 |  | MPS pulsed current OFF time | EMPS open | 225 245 |  |  | ms
```

#### Raw extracted text

```text
TPS23730
SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020 www.ti.com
7.6 Electrical Characteristics PoE (continued)
Unless otherwise noted, V = 48 V; R = 25.5 kOhm; R = 60.4 kOhm; R = 499 kOhm; CLSA, CLSB, TPH, TPL,
VDD DEN FRS I_STP
BT, SCDIS and PSRS open; CS, EA_DIS, APD, EMPS, AGND and GND connected to RTN; FB, LINEUV, DT and DTHR
connected to VB; PPD connected to VSS; C = C = 0.1 uF; C = 1 uF; C = 0.047 uF; R = 49.9 kOhm; -40 deg C <= T
VB VBG VCC SST REF J
<= 125 deg C. Positive currents are into pins unless otherwise noted. Typical values are at 25 deg C.
V = 0 V, all voltages referred to V unless otherwise noted.
VCC-RTN VSS
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
Foldback voltage
V rising 13.5 14.8 16.1 V
threshold RTN
V rising to when current limit changes to
RTN
Foldback deglitch time inrush current limit. This applies in normal 1.5 1.8 2.1 ms
operating condition or during auto MPS mode.
Leakage current V = V = 100 V, V = V 70 uA
VDD RTN DEN VSS
PSE TYPE INDICATION (TPL, TPH, BT)
I = 1 mA, after 2- or 3-event classification,
V Output low voltage TPL 0.27 0.5 V
TPL startup has completed, V = 0 V
RTN
I = 1 mA, after 4-event classification, startup
V Output low voltage TPH 0.27 0.5 V
TPH has completed, V = 0 V
RTN
I = 2 mA, after IEEE802.3bt classification,
V Output low voltage BT 0.27 0.5 V
BT startup has completed, V = 0 V
RTN
V = 0 V, V = 5 V, after startup has
f TPL frequency SCDIS APD-RTN 550 625 700 Hz
TPL completed.
TPL duty cycle in PoE V = 0 V, after 4-event classification, after
SCDIS 24% 25% 26%
operation startup has completed
TPL duty cycle
in nonstandard PoE V = 0 V, after startup has completed 49% 50% 51%
SCDIS
operation
TPL duty cycle
V = 0 V, V = 5 V, after startup has
in auxiliary supply SCDIS APD-RTN 74% 75% 76%
completed.
operation
V or V = 10 V or V = 5 V,
Leakage current TPL-RTN TPH-RTN BT-RTN 1 uA
V = 0 V
RTN
V >= V or
SCDIS pullup current VDD UVLO_R 14 20 25 uA
V = 5 V
APD-RTN
PD INPUT SUPPLY (VDD)
Undervoltage lockout
V V rising 35.8 37.6 39.5 V
UVLO_R threshold VDD
Undervoltage lockout
V V falling 30.5 32 33.6 V
UVLO_F threshold VDD
Undervoltage lockout
V Hysteresis (1) 5.7 6.0 6.3 V
UVLO_H threshold
40 V <= V <= 60 V, Startup completed, V =
I Operating current VDD VCC 650 1040 uA
VDD_ON 10 V, Measure I
VDD
RTN, GND and VCC open, V = 30 V, Measure
I Off-state current VDD 730 uA
VDD_OFF I
VDD
MPS
MPS total VSS current EMPS open, inrush delay has completed, 0 mA <=
I 10 12.5 15.5 mA
MPSL for Type 1-2 PSE I <= 10 mA, measure I
RTN VSS
MPS total VSS current EMPS open, inrush delay has completed, 0 mA <=
I 16.25 19 21.5 mA
MPSH for Type 3-4 PSE I <= 16 mA, measure I
RTN VSS
MPS pulsed current
EMPS open 26.2% 26.6% 26.9%
duty-cycle
MPS pulsed mode duty MPS pulsed current ON
t EMPS open 76 81.5 87 ms
MPSL cycle for Type 1-2 PSE time
MPS pulsed current
EMPS open 225 245 ms
OFF time
12 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS23730
```

### Page 13

#### Extracted tables

Table 1:

```text
PARAMETER |  | TEST CONDITIONS |  | MIN | TYP | MAX | UNIT
 | MPS pulsed mode duty- cycle for Type 3-4 PSE | MPS pulsed current duty-cycle, no pulse stretching | EMPS open | 2.9% 3.0% 3.1% |  |  | 
t MPSH |  | MPS pulsed current ON time, no pulse stretching | EMPS open | 7.2 7.7 8.1 |  |  | ms
 |  | MPS pulsed current OFF time | EMPS open | 238 250 265 |  |  | ms
 |  | MPS pulsed current ON time stretching limit | EMPS open | 54 57 62 |  |  | ms
THERMAL SHUTDOWN |  |  |  |  |  |  | 
 | Turnoff temperature |  |  | 148 158 168 |  |  | deg C
 | Hysteresis(2) |  |  | 15 |  |  | deg C
```

Table 2:

```text
|  | 10% |  |  | 
 |  |  |  |  | 90%
 |  | 10% |  |  |
```

#### Raw extracted text

```text
7.6 Electrical Characteristics PoE (continued)
Unless otherwise noted, V = 48 V; R = 25.5 kOhm; R = 60.4 kOhm; R = 499 kOhm; CLSA, CLSB, TPH, TPL,
VDD DEN FRS I_STP
BT, SCDIS and PSRS open; CS, EA_DIS, APD, EMPS, AGND and GND connected to RTN; FB, LINEUV, DT and DTHR
connected to VB; PPD connected to VSS; C = C = 0.1 uF; C = 1 uF; C = 0.047 uF; R = 49.9 kOhm; -40 deg C <= T
VB VBG VCC SST REF J
<= 125 deg C. Positive currents are into pins unless otherwise noted. Typical values are at 25 deg C.
V = 0 V, all voltages referred to V unless otherwise noted.
VCC-RTN VSS
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
MPS pulsed current
duty-cycle, no pulse EMPS open 2.9% 3.0% 3.1%
stretching
MPS pulsed current
t MPSH MPS pulsed mode duty- ON time, no pulse EMPS open 7.2 7.7 8.1 ms
cycle for Type 3-4 PSE stretching
MPS pulsed current
EMPS open 238 250 265 ms
OFF time
MPS pulsed current ON
EMPS open 54 57 62 ms
time stretching limit
THERMAL SHUTDOWN
Turnoff temperature 148 158 168  deg C
Hysteresis(2) 15  deg C
(1) The hysteresis tolerance tracks the rising threshold for a given device.
(2) These parameters are provided for reference only.
t
DT1
ETAG
2TAG
TPS23730
www.ti.com SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020
hi 90%
lo 10%
hi 90%
lo 10% time
t
DT2
Figure 7-1. GATE and GAT2 Timing and Phasing
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 13
Product Folder Links: TPS23730
```

### Page 14

#### Extracted tables

Table 1:

```text
12.5 10 )AP( tnerruC 7.5 saiB 5 DDV 2.5 TJ = -40qC TJ = 25qC TJ = 125qC 0 1 2 3 4 5 6 7 8 9 10 VDD-VSS Voltage (V) D001 Figure 7-2. Detection Bias Current vs Voltage | 1.9 1.89 1.88 1.87 1.86 )A( 1.85 timiL 1.84 1.83 tnerruC 1.82 1.81 1.8 1.79 1.78 1.77 1.76 1.75 -50 -25 0 25 50 75 100 125 Junction Temperature (qC) D002 Figure 7-3. PoE Current Limit vs Temperature
0.5 0.45 ):( ecnatsiseR 0.4 0.35 TEF 0.3 ssaP 0.25 0.2 -50 -25 0 25 50 75 100 125 Junction Temperature (qC) D004 Figure 7-4. Pass FET Resistance vs Temperature | 1000 950 )AP( 900 tnerruC 850 800 ylppuS 750 700 latoT 650 DDV 600 TJ = -40qC TJ = 25qC 550 TJ = 125qC 500 25 30 35 40 45 50 55 60 VDD-VSS Voltage (V) D005 Figure 7-5. VDD Supply Current vs Voltage
35 34 33 )Am( 32 31 tnerruC 30 29 28 gnicruoS 27 26 25 CCV 24 VVCC = 11.7 V 23 TJ = -40qC 22 TJ = 25qC TJ = 125qC 21 20 15 20 25 30 35 40 45 50 55 60 VDD-RTN Voltage (V) D006 Figure 7-6. Converter Startup Current vs VDD Input Voltage | 35 34 33 )Am( 32 31 tnerruC 30 29 28 gnicruoS 27 26 25 CCV 24 VVCC = 6.8 V 23 TJ = -40qC 22 TJ = 25qC TJ = 125qC 21 20 10 15 20 25 30 35 40 45 50 55 VDD-RTN Voltage (V) D007 Figure 7-7. Converter Startup Current vs VDD Input Voltage
```

Table 2:

```text
|  |  |  |  |  |  |  |  |  |  |  |  |  | T | = | 40q | C
 |  |  |  |  |  |  |  |  |  |  |  |  |  | J TJ TJ | = = | 25q 125 | C qC
```

Table 3:

```text
|  |  |  |  |  |  |  |  |  |  |  | TJ | = -40 | qC
 |  |  |  |  |  |  |  |  |  |  |  | TJ | = 25q | C
 |  |  |  |  |  |  |  |  |  |  |  | TJ | = 12 | 5qC
```

Table 4:

```text
|  |  |  |  |  |  |  |  |  |  |  |  |  | V |  | = 1 | 1.7 | V
 |  |  |  |  |  |  |  |  |  |  |  |  |  | V | CC T | = | 40 | qC
 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | J T | = | 25q | C
 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | J TJ | = | 125 | qC
```

Table 5:

```text
|  |  |  |  |  |  |  |  |  |  |  |  |  | V |  | = 6 | .8 V | 
 |  |  |  |  |  |  |  |  |  |  |  |  |  | V | CC T | = | 40q | C
 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | J T | = | 25qC | 
 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | J TJ | = | 125q | C
```

#### Raw extracted text

```text
7.7 Typical Characteristics
VDD-VSS Voltage (V)
VDD Bias Current (PA)
1 2 3 4 5 6 7 8 9 10
0
2.5
5
7.5
10
12.5
D001
TJ = -40qC
TJ = 25qC
TJ = 125qC
Figure 7-2. Detection Bias Current vs Voltage
Junction Temperature (qC)
Current Limit (A)
-50 -25 0 25 50 75 100 125
1.75
1.76
1.77
1.78
1.79
1.8
1.81
1.82
1.83
1.84
1.85
1.86
1.87
1.88
1.89
1.9
D002 Figure 7-3. PoE Current Limit vs Temperature
Junction Temperature (qC)
Pass FET Resistance (:)
-50 -25 0 25 50 75 100 125
0.2
0.25
0.3
0.35
0.4
0.45
0.5
D004
Figure 7-4. Pass FET Resistance vs Temperature
VDD-VSS Voltage (V)
VDD Total Supply Current (PA)
25 30 35 40 45 50 55 60
500
550
600
650
700
750
800
850
900
950
1000
D005
TJ = -40qC
TJ = 25qC
TJ = 125qC Figure 7-5. VDD Supply Current vs Voltage
VDD-RTN Voltage (V)
VCC Sourcing Current (mA)
15 20 25 30 35 40 45 50 55 60
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
D006
VVCC = 11.7 V
TJ = -40qC
TJ = 25qC
TJ = 125qC
Figure 7-6. Converter Startup Current vs VDD Input Voltage
VDD-RTN Voltage (V)
VCC Sourcing Current (mA)
10 15 20 25 30 35 40 45 50 55
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
D007
VVCC = 6.8 V
TJ = -40qC
TJ = 25qC
TJ = 125qC Figure 7-7. Converter Startup Current vs VDD Input Voltage
TPS23730
SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020 www.ti.com
14 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS23730
```

### Page 15

#### Extracted tables

Table 1:

```text
13 12.5 12 11.5 )V( egatloV 11 10.5 CCV 10 9.5 9 TJ = -40qC TJ = 25qC 8.5 TJ = 125qC 8 0 3 6 9 12 15 18 21 24 27 30 VCC Sourcing Current (mA) D008 Figure 7-8. Converter Startup Voltage vs Current | 65 60 55 )AP( 50 tnerruC 45 40 gnigrahcsiD 35 30 25 20 TSS 15 10 5 0 0 50 100 150 200 250 300 350 400 450 500 I_STP Programmable Resistance (k:) D009 Figure 7-9. Controller SST Soft Stop Sink Current vs Programmed Resistance
3 2.9 2.8 )Am( 2.7 2.6 tnerruC 2.5 2.4 2.3 gnitarepO 2.2 2.1 RFRS = 37.4 k: 2 RFRS = 60.4 k: CCV 1.9 RFRS = 301 k: 1.8 1.7 1.6 1.5 9 9.75 10.5 11.25 12 12.75 13.5 VCC Voltage (V) D010 Figure 7-10. Controller Bias Current vs Voltage | 450 400 )zHk( 350 RFRS = 37.4 k: RFRS = 60.4 k: ycneuqerF 300 RFRS = 301 k: 250 200 gnihctiwS 150 100 50 0 -50 -25 0 25 50 75 100 125 Junction Temperature (qC) D011 Figure 7-11. Switching Frequency vs Temperature
800 )zHk( 600 ycneuqerF 400 gnihctiwS 200 0 0 5 10 15 20 25 30 35 40 45 50 Programmable Conductance (106/RFRS (:-1) D012 Figure 7-12. Switching Frequency vs Programmed Resistance | 81 80.5 80 RFRS = 37.4 k: )%( elcyC 79.5 R R F F R R S S = = 6 3 0 0 . 1 4 k k : : 79 ytuD 78.5 mumixaM 78 77.5 77 76.5 76 -50 -25 0 25 50 75 100 125 Junction Temperature (qC) D013 Figure 7-13. Maximum Duty Cycle vs Temperature
```

Table 2:

```text
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | q | 
 |  |  |  |  |  |  |  |  |  |  |  |  | TJ | = -4 | 0 q | C
 |  |  |  |  |  |  |  |  |  |  |  |  | TJ | = 2 | 5C q | 
 |  |  |  |  |  |  |  |  |  |  |  |  | TJ | = 1 | 25 | C
```

Table 3:

```text
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | :
 |  |  |  |  |  |  |  |  |  |  |  | R | FRS | = | 37.4 | k :
 |  |  |  |  |  |  |  |  |  |  |  | R | FRS | = | 60.4 | k :
 |  |  |  |  |  |  |  |  |  |  |  | R | FRS | = | 301 | k
```

Table 4:

```text
|  |  |  |  |  |  | :
 |  |  |  |  |  | RFRS = | 37.4 k :
 |  |  |  |  |  | RFRS = R = | 60.4 k 301 k:
 |  |  |  |  |  | FRS |
```

Table 5:

```text
|  |  |  |  |  |  | :
 |  |  |  |  |  | RFRS = | 37.4 k
 |  |  |  |  |  | RFRS = | 60.4 k:
 |  |  |  |  |  | RFRS = | 301 k:
```

#### Raw extracted text

```text
7.7 Typical Characteristics (continued)
VCC Sourcing Current (mA)
)V(
egatloV
CCV
13
12.5
12
11.5
11
10.5
10
9.5
9 TJ = -40qC
TJ = 25qC
8.5 TJ = 125qC
8
0 3 6 9 12 15 18 21 24 27 30
I_STP Programmable Resistance (k:)
D008
Figure 7-8. Converter Startup Voltage vs Current
)AP(
tnerruC
gnigrahcsiD
TSS
65
60
55
50
45
40
35
30
25
20
15
10
5
0
0 50 100 150 200 250 300 350 400 450 500
D009
Figure 7-9. Controller SST Soft Stop Sink Current vs
Programmed Resistance
VCC Voltage (V)
)Am(
tnerruC
gnitarepO
CCV
3
2.9
2.8
2.7
2.6
2.5
2.4
2.3
2.2
2.1 RFRS = 37.4 k:
2 RFRS = 60.4 k:
1.9 RFRS = 301 k:
1.8
1.7
1.6
1.5
9 9.75 10.5 11.25 12 12.75 13.5
Junction Temperature (qC)
D010
Figure 7-10. Controller Bias Current vs Voltage
)zHk(
ycneuqerF
gnihctiwS
450
400
350 RFRS = 37.4 k:
RFRS = 60.4 k:
300 RFRS = 301 k:
250
200
150
100
50
0
-50 -25 0 25 50 75 100 125
D011
Figure 7-11. Switching Frequency vs Temperature
Programmable Conductance (106/RFRS (:-1)
)zHk( ycneuqerF
gnihctiwS
800
600
400
200
0
0 5 10 15 20 25 30 35 40 45 50
Junction Temperature (qC)
D012
Figure 7-12. Switching Frequency vs Programmed Resistance
)%( elcyC
ytuD
mumixaM
TPS23730
www.ti.com SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020
81
80.5
80 RFRS = 37.4 k: 79.5 R R F F R R S S = = 6 3 0 0 . 1 4 k k : :
79
78.5
78
77.5
77
76.5
76
-50 -25 0 25 50 75 100 125
D013
Figure 7-13. Maximum Duty Cycle vs Temperature
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 15
Product Folder Links: TPS23730
```

### Page 16

#### Extracted tables

Table 1:

```text
1.76 1.758 1.756 )V( egatloV 1.754 1.752 noitalugeR 1.75 1.748 1.746 BF 1.744 1.742 1.74 -50 -25 0 25 50 75 100 125 Junction Temperature (qC) D014 Figure 7-14. Feedback Regulation Voltage vs Temperature | 24 23.2 )AP( 22.4 tnerruC 21.6 20.8 noitasnepmoC 20 19.2 18.4 epolS 17.6 16.8 16 -50 -25 0 25 50 75 100 125 Junction Temperature (qC) D015 Figure 7-15. Current Slope Compensation Current vs Temperature
100 99.5 99 )sn( 98.5 doireP 98 97.5 gniknalB 97 96.5 96 95.5 95 -50 -25 0 25 50 75 100 125 Junction Temperature (qC) D016 Figure 7-16. Blanking Period vs Temperature | 550 500 450 400 )sn( 350 emiT 300 250 daeD 200 150 100 tDT1 50 tDT2 0 0 25 50 75 100 125 150 175 200 225 250 DT Programmable Resistance (k:) D017 Figure 7-17. Dead Time vs Dead Time Resistance (R ) DT
4 3.6 T T J J = = - 2 4 5 0 q q C C )Am( 3.2 TJ = 125qC tnerruC 2.8 2.4 gnicruoS 2 1.6 PMOC 1.2 0.8 0.4 0 0 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5 COMP Voltage (V) D019 Figure 7-18. Error Amplifier Source Current | 20 18 )Am( 16 14 tnerruC 12 gnikniS 10 8 PMOC 6 4 TJ = -40qC TJ = 25qC 2 TJ = 125qC 0 0 0.4 0.8 1.2 1.6 2 2.4 2.8 3.2 3.6 4 COMP Voltage (V) D020 Figure 7-19. Error Amplifier Sink Current
```

Table 2:

```text
|  |  |  |  |  |  |  |  | tDT1
 |  |  |  |  |  |  |  |  | tDT2
```

Table 3:

```text
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | TJ | = | 40q |  | C
 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | TJ | = 2 | 5q |  | C
 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | T | = 1 | 25 |  | qC
 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | J |  |  |  |
```

Table 4:

```text
|  |  |  |  |  |  |  |  |  |  |  |  |  |  | T = | 40q | C
 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | J | q | 
 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | TJ = | 25C q | 
 |  |  |  |  |  |  |  |  |  |  |  |  |  |  | TJ = | 125 | C
```

#### Raw extracted text

```text
7.7 Typical Characteristics (continued)
Junction Temperature (qC)
)V(
egatloV
noitalugeR
BF
1.76
1.758
1.756
1.754
1.752
1.75
1.748
1.746
1.744
1.742
1.74
-50 -25 0 25 50 75 100 125
Junction Temperature (qC)
D014
Figure 7-14. Feedback Regulation Voltage vs Temperature
)AP(
tnerruC
noitasnepmoC
epolS
24
23.2
22.4
21.6
20.8
20
19.2
18.4
17.6
16.8
16
-50 -25 0 25 50 75 100 125
D015
Figure 7-15. Current Slope Compensation Current vs
Temperature
Junction Temperature (qC)
)sn(
doireP
gniknalB
100
99.5
99
98.5
98
97.5
97
96.5
96
95.5
95
-50 -25 0 25 50 75 100 125
DT Programmable Resistance (k:)
D016
Figure 7-16. Blanking Period vs Temperature
)sn(
emiT
daeD
550
500
450
400
350
300
250
200
150
100
tDT1
50 tDT2
0
0 25 50 75 100 125 150 175 200 225 250
D017
Figure 7-17. Dead Time vs Dead Time Resistance (R )
DT
COMP Voltage (V)
)Am(
tnerruC
gnicruoS
PMOC
4
3.6 T T J J = = - 2 4 5 0 q q C C
3.2 TJ = 125qC
2.8
2.4
2
1.6
1.2
0.8
0.4
0
0 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5
COMP Voltage (V)
D019
Figure 7-18. Error Amplifier Source Current
)Am(
tnerruC
gnikniS
PMOC
TPS23730
SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020 www.ti.com
20
18
16
14
12
10
8
6
4 TJ = -40qC
TJ = 25qC
2 TJ = 125qC
0
0 0.4 0.8 1.2 1.6 2 2.4 2.8 3.2 3.6 4
D020
Figure 7-19. Error Amplifier Sink Current
16 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS23730
```

### Page 17

#### Extracted tables

Table 1:

```text
100 90 TJ = -40qC 80 T T J J = = 2 1 5 2 q 5 C qC 70 )Bd( 60 edutilpmA 50 40 30 niaG 20 10 0 -10 -20 100 1k 10k 100k 1M 5M Frequency (Hz) D021 Figure 7-20. Error Amplifier Gain vs Frequency | 135 TJ = -40qC 120 TJ = 25qC TJ = 125qC 105 )q( 90 nigraM 75 esahP 60 45 30 15 0 100 1k 10k 100k 1M 5M Frequency (Hz) D022 Figure 7-21. Error Amplifier Phase vs Frequency
```

Table 2:

```text
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | q |  | 
 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | T T | J = -4 J = 25 | 0 qC | C | 
 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | T | J = 12 | 5q | C |
```

Table 3:

```text
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | T | J = -4 | 0q q | C | 
 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | T T | J = 25 J = 12 | C 5q | C |
```

#### Raw extracted text

```text
7.7 Typical Characteristics (continued)
Frequency (Hz)
)Bd(
edutilpmA
niaG
100
90 TJ = -40qC
80 T T J J = = 2 1 5 2 q 5 C qC
70
60
50
40
30
20
10
0
-10
-20
100 1k 10k 100k 1M 5M
Frequency (Hz)
D021
Figure 7-20. Error Amplifier Gain vs Frequency
)q(
nigraM
esahP
TPS23730
www.ti.com SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020
135
TJ = -40qC
120 TJ = 25qC 105 TJ = 125qC
90
75
60
45
30
15
0
100 1k 10k 100k 1M 5M
D022
Figure 7-21. Error Amplifier Phase vs Frequency
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 17
Product Folder Links: TPS23730
```

### Page 18

#### Raw extracted text

```text
8 Detailed Description
8.1 Overview
The TPS23730 device is a 45-pin integrated circuit that contains all of the features needed to implement a single
interface IEEE 802.3bt Type 3 Class 1-6 and IEEE802.3at powered device (PD), combined with a current-mode
DC-DC controller optimized for flyback and active clamp forward switching regulator design.
The DC-DC controller of the TPS23730 features two complementary gate drivers with programmable dead time.
This simplifies the design of active-clamp forward converters or optimized gate drive for highly-efficient flyback
topologies. The second gate driver may be disabled if desired for self-driven synchronous flyback or for single
MOSFET topologies.
Basic PoE PD functionality supported includes detection, hardware classification, and inrush current limit during
startup. DC-DC converter features include startup function and current mode control operation. The TPS23730
device integrates a low 0.3-Ohm internal switch to minimize heat dissipation and maximize power utilization.
A number of input voltage Oring options or input voltage ranges are also supported by use of APD and PPD
inputs.
The TPS23730 device contains several protection features such as thermal shutdown, current limit foldback, and
a robust 100-V internal return switch.
TPS23730
SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020 www.ti.com
18 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS23730
```

### Page 19

#### Raw extracted text

```text
8.2 Functional Block Diagram
VDD VCC
COMP
FB t
80k(cid:13) + E/A
Vrefc
(1.75V)
10 (cid:29)A 20k(cid:13)
RTN Converter off from PD Reference
SST
disch
Regulator VB
+
t 0.3 V
Current Ramp
CS
3.3k (cid:13) Blanking GATE
Control 1 D Q + CLRB
(0 V .2 CS 5 M V AX ) t CLK
vb
EA_DIS
Timing
TPS23730
www.ti.com SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020
Vdd
Regulator
disch
0
+
LINEUV
EAD
chrg + t 0.25 V 3 2 V .9 V &
Control uvlo
Soft Stop 4 (cid:29)A disch vb
Discharge chrg
PWM
COMP
RTN RTN
t
Regulator VBG
I_STP S_stop/start ctl
20 (cid:29)A (pk)
ILIMIT
COMP DT
GAT2
vb
FRS
Oscillator
DTHR
PSRS
CP
EAD CP cntl
2V &
1.7V GND
1.25V
Detection Comp. Bias
12.2V & C C o la m s p s . 4V REF
11V Oscillator
Vdd
22V & C C o la m s p s . VSS DEN
21.2V
apdout 1.25V CLSA
Mark REG.
3.9V Comp. 1 & 4 . 1 8 V V 1. 8 8 0 m 0 s s FoldB Mark R VSS CLSB
APD C A o P m D p. S c ta o t n e t r e o n l g sect
1.5V Class Comp Out
&1.4V TPH, TPL
RTN Mark Comp Out State /BT
RTN Inrush Eng.
timing mpcl
S RTN
High if over R Q apdout, PPD
temperature Inrush latch SCDIS
OTSD
Inrush limit
PPD
37 3 .6 2 V V C & P o P m D p. C U o V m LO p. C t t u h h r r r r e e e s s n h h t o o li l l m d d it 0 1 IRTN sense 1 0 Converter OFF
2.5V
&2V
VSS
Signals r o e t f h e e re rw n i c s e e d n t o o t e V d SS unless M H O ot S sw FE ap T RTN
IRTN sense,1 if < 90% of inrush and current limit
Vdd
Av
Automatic
EMPS MPS Control
mpcl
apdout
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 19
Product Folder Links: TPS23730
```

### Page 20

#### Extracted tables

Table 1:

```text
PD CLASS | CLASS SIGNATURE A | CLASS SIGNATURE B | MINIMUM POWER AT PD (W) | MAXIMUM POWER AT PD (W) | NUMBER OF CLASS CYCLES @ MAX POWER | RESISTOR CLSA (Ohm) | RESISTOR CLSB (Ohm)
0 | 0 | 0 | 0.44 | 12.95 | 1 | 806 | 806
1 | 1 | 1 | 0.44 | 3.84 | 1 | 130 | 130
2 | 2 | 2 | 3.84 | 6.49 | 1 | 69.8 | 69.8
3 | 3 | 3 | 6.49 | 12.95 | 1 | 46.4 | 46.4
4 | 4 | 4 | 12.95 | 25.5 | 2,3 | 32 | 32
5 | 4 | 0 | 25.5 | 40 | 4 | 32 | 806
6 | 4 | 1 | 40 | 51 | 4 | 32 | 130
```

#### Raw extracted text

```text
8.3 Feature Description
See Figure 9-1 for component reference designators (R CS for example ), and Electrical Characteristics: DC-DC
Controller Section for values denoted by reference (V CSMAX for example). Electrical Characteristic values take
precedence over any numerical values used in the following sections.
8.3.1 CLSA, CLSB Classification
Each of the two external resistors (R CLSA and R CLSB in Figure 9-1 ) connected between the CLSA (first and
second class event) and CLSB (third and any subsequent class event) pins and VSS provide a distinct
classification signature to the PSE, and are used to define the power class requested by the PD. The controller
places a voltage of approximately 1.25 V across CLSA (first or second class event) or CLSB (all additional class
events) external resistor whenever the voltage differential between VDD and VSS lies from about 11 V to 22 V.
The current drawn by each resistor, combined with the internal current drain of the controller and any leakage
through the internal pass MOSFET, creates the classification signature current. Table 8-1 lists the external
resistor values required for each of the PD power ranges defined by IEEE802.3bt. The number of classification
cycles then determines how much power is allocated by the PSE. The maximum average power drawn by the
PD, plus the power supplied to the downstream load, should not exceed the maximum power indicated in Table
8-1, as well as the maximum power allocated by the PSE based on the number of classification cycles. Holding
APD high disables the classification signatures.
Type 2 and Type 3 PSEs may perform two classification cycles if Class 4 signature is presented on the first
cycle. Likewise, Type 3 and Type 4 PSEs may perform four classification cycles if Class 4 signature is presented
on the first two cycles and Class 0 or 1 signature is presented on the third cycle.
Table 8-1. Class Resistor Selection
PD CLASS CLASS
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
0 0 0 0.44 12.95 1 806 806
1 1 1 0.44 3.84 1 130 130
2 2 2 3.84 6.49 1 69.8 69.8
3 3 3 6.49 12.95 1 46.4 46.4
4 4 4 12.95 25.5 2,3 32 32
5 4 0 25.5 40 4 32 806
6 4 1 40 51 4 32 130
8.3.2 DEN Detection and Enable
DEN pin implements two separate functions. A resistor (R DEN in Figure 9-1 ) connected between VDD and
DEN generates a detection signature whenever the voltage differential between VDD and VSS lies from
approximately 1.4 to 10.9 V. Beyond this range, the controller disconnects this resistor to save power. The
IEEE 802.3bt and IEEE 802.3at standards specify a detection signature resistance, R detect from 23.75 k Ohm to
26.25 kOhm, or 25 kOhm +/- 5%. TI recommends a resistor of 25.5 kOhm +/- 1% for RDEN.
Pulling DEN to VSS during powered operation causes the internal hotswap MOSFET and class regulator
to turn off. If the resistance connected between VDD and DEN is divided into two roughly equal portions,
then the application circuit can disable the PD by grounding the tap point between the two resistances, while
simultaneously spoiling the detection signature which prevents the PD from properly re-detecting.
8.3.3 APD Auxiliary Power Detect
The APD pin is used in applications that may draw power either from the Ethernet cable or from an auxiliary
power source. When a voltage of more than about 1.5 V is applied on the APD pin relative to RTN, the
TPS23730 does the following:
* Internal pass MOSFET is turned off
* Classification current is disabled
TPS23730
SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020 www.ti.com
20 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS23730
```

### Page 21

#### Extracted tables

Table 1:

```text
PSE TYPE | PD CLASS | NUMBER OF CLASS CYCLES | PSE ALLOCATED POWER AT PD (W) | TPH(2) | TPL
1-4 | 0 | 1 | 12.95 | HIGH | HIGH
1-4 | 1 | 1 | 3.84 | HIGH | HIGH
1-4 | 2 | 1 | 6.49 | HIGH | HIGH
1-4 | 3 | 1 | 12.95 | HIGH | HIGH
```

#### Raw extracted text

```text
TPS23730
www.ti.com SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020
* The LINEUV input is disabled
* Maintain Power Signature (MPS) pulsed mode is disabled
* TPH and TPL outputs are turned on (low state) if SCDIS is open
* TPL duty-cycle becomes 75% if SCDIS level is low
This also gives adapter source priority over the PoE. A resistor divider (R -R in Figure 9-1) provides
APD1 APD2
system-level ESD protection for the APD pin, discharges leakage from the blocking diode (D in Figure 9-1) and
A
provides input voltage supervision to ensure that switch-over to the auxiliary voltage source does not occur at
excessively low voltages. If not used, connect APD to RTN.
8.3.4 PPD Power Detect
PPD permits power to come from an external low voltage adapter, for example 24 V, connected from VDD
to VSS by overriding the normal hotswap UVLO. Voltage on PPD more than 2.5 V (V ) enables the
PPDEN
hotswap MOSFET, inhibits class current, and turns on TPH and TPL. A resistor divider per Figure 8-16 provides
ESD protection, leakage discharge for the adapter ORing diode, reverse adapter protection, and input voltage
qualification. Voltage qualification assures the adapter output voltage is high enough that it can support the PD
before it begins to draw current
The PPD pin has a 5-uA internal pulldown current.
Locate the PPD pulldown resistor adjacent to the pin when used. PPD may be tied to VSS pin or left open when
not used.
8.3.5 Internal Pass MOSFET
RTN pin provides the negative power return path for the load. It is internally connected to the drain of the PoE
hotswap MOSFET, and the DC-DC controller return. RTN must be treated as a local reference plane (ground
plane) for the DC-DC controller and converter primary to maintain signal integrity.
Once V exceeds the UVLO threshold, the internal pass MOSFET pulls RTN to VSS. Inrush limiting prevents
VDD
the RTN current from exceeding a nominal value of about 140 mA until the bulk capacitance (C in Figure
BULK
9-1) is fully charged. Two conditions must be met to reach the end of inrush phase. The first one is when the
RTN current drops below about 90% of nominal inrush current at which point the current limit is changed to 1.85
A, while the second one is to ensure a minimum inrush delay period of 80 ms (t ) from beginning of the
INR_DEL
inrush phase. DC-DC converter switching is permitted once both inrush conditions are met, meaning that the
bulk capacitance is fully charged and the inrush period has been completed.
If V - V ever exceeds about 14.8 V for longer than 1.8 ms, then the PD returns to inrush limiting; note
RTN VSS
that in this particular case, the second condition described above about inrush phase duration (80 ms) is not
applicable
8.3.6 TPH, TPL and BT PSE Type Indicators
The state of TPH and TPL is used to provide information relative to the allocated power. The encoding
can be either parallel or serial (TPL only), selectable with SCDIS input. Table 8-2 lists the parallel encoding
corresponding to various combinations of PSE Type, PD Class and allocated power. The allocated power is
determined by the number of classification cycles having been received. The PSE may also allocate a lower
power than what the PD is requesting, in which case there is power demotion. The BT output also indicates if a
PSE applying an IEEE802.3bt (Type 3 or 4) mutual identification scheme has been identified.
Serial encoding can be selected by tying SCDIS to VSS. See Table 8-3 which lists the TPL serial encoding
versus allocated power. In this case, TPH becomes high impedance.
Table 8-2. TPH, TPL and Allocated Power Truth Table, with APD and PPD Low, SCDIS Open
NUMBER OF CLASS PSE ALLOCATED
PSE TYPE PD CLASS TPH(2) TPL
CYCLES POWER AT PD (W)
1-4 0 1 12.95 HIGH HIGH
1-4 1 1 3.84 HIGH HIGH
1-4 2 1 6.49 HIGH HIGH
1-4 3 1 12.95 HIGH HIGH
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 21
Product Folder Links: TPS23730
```

### Page 22

#### Extracted tables

Table 1:

```text
PSE TYPE | PD CLASS | NUMBER OF CLASS CYCLES | PSE ALLOCATED POWER AT PD (W) | TPH(2) | TPL
2 | 4 | 2 | 25.5 | HIGH | LOW
3-4 | 4 | 2-3 | 25.5 | HIGH | LOW
3-4 | 5 | 4 | 40 | LOW | HIGH
3-4 | 6 | 4 | 51 | LOW | HIGH
PoE++ | 5,6 |  |  | LOW(1) | HIGH
```

Table 2:

```text
PSE TYPE | PD CLASS | NUMBER OF CLASS CYCLES | PSE ALLOCATED POWER AT PD (W) | TPL(1)
1-4 | 0 | 1 | 12.95 | HIGH
1-4 | 1 | 1 | 3.84 | HIGH
1-4 | 2 | 1 | 6.49 | HIGH
1-4 | 3 | 1 | 12.95 | HIGH
2 | 4 | 2 | 25.5 | LOW
3-4 | 4 | 2-3 | 25.5 | LOW
3-4 | 5 | 4 | 40 | LOW_25%
3-4 | 6 | 4 | 51 | LOW_25%
PoE++ | 5,6 |  |  | LOW_50%
```

#### Raw extracted text

```text
TPS23730
SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020 www.ti.com
Table 8-2. TPH, TPL and Allocated Power Truth Table, with APD and PPD Low, SCDIS Open (continued)
NUMBER OF CLASS PSE ALLOCATED
PSE TYPE PD CLASS TPH(2) TPL
CYCLES POWER AT PD (W)
2 4 2 25.5 HIGH LOW
3-4 4 2-3 25.5 HIGH LOW
3-4 5 4 40 LOW HIGH
3-4 6 4 51 LOW HIGH
PoE++ 5,6 - - LOW(1) HIGH
(1) If PoE++ PSE, the BT output is also high.
(2) If APD or PPD is high, both TPH and TPL outputs become low.
Table 8-3. TPL Duty-Cycle and Allocated Power Truth Table, with APD and PPD Low, SCDIS Low
NUMBER OF CLASS PSE ALLOCATED
PSE TYPE PD CLASS TPL(1)
CYCLES POWER AT PD (W)
1-4 0 1 12.95 HIGH
1-4 1 1 3.84 HIGH
1-4 2 1 6.49 HIGH
1-4 3 1 12.95 HIGH
2 4 2 25.5 LOW
3-4 4 2-3 25.5 LOW
3-4 5 4 40 LOW_25%
3-4 6 4 51 LOW_25%
PoE++ 5,6 - - LOW_50%
(1) If APD or PPD is high, TPL output becomes low with 75% duty-cycle.
During startup, the TPH, TPL and BT outputs are enabled only once the DC-DC controller has reached steady-
state, the soft-start having been completed. These 3 outputs will return to a high-impedance state in any of the
following cases:
* DC-DC controller is back to soft-start mode
* DC-DC controller transitions to soft-stop mode
* DC-DC controller shuts off due to reasons including V falling below V , or the PoE hotswap is in
VCC CUVLO_F
inrush limit while APD is low
* The device enters thermal shutdown
Note that in all these cases, as long as VDD-to-VSS voltage remains above the mark reset threshold, the
internal logic state of these signals is remembered such that these outputs will be activated accordingly after the
soft-start has completed. This circuit resets when the VDD-to-VSS voltage drops below the mark reset threshold.
The TPH, TPL and BT pins can be left unconnected if not used.
8.3.7 DC-DC Controller Features
The TPS23730 device DC-DC controller implements a typical current-mode control as shown in Functional
Block Diagram. Features include oscillator, overcurrent and PWM comparators, current-sense blanker, dead
time control, soft-start, soft-stop and gate driver. In addition, an internal current-compensation ramp generator,
frequency synchronization logic, built-in frequency dithering functionality, thermal shutdown, and start-up current
source with control are provided.
The TPS23730 is optimized for isolated converters, supporting the use of PSR (flyback configuration) and
optocoupler feedback (ACF and flyback).
To support PSR, the TPS23730 includes an internal error amplifier, and the voltage feedback is from the bias
winding.
If optocoupler feedback is used, the error amplifier is disabled (by use of EA_DIS input). In this case, the
optocoupler output directly drives the COMP pin which serves as a current-demand control to the PWM.
22 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS23730
```

### Page 23

#### Extracted tables

Table 1:

```text
PSE Inrush | Operational Mode
```

Table 2:

```text
VCC Startup Source ON | End of Soft-Start, Startup source turned off PD + Power Supply Fully Operational
```

#### Raw extracted text

```text
TPS23730
www.ti.com SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020
In both cases, the COMP signal is directly fed to a 5:1 internal resistor divider and an offset of V /5 (~0.3
ZDC
V) which defines a current-demand control for the pulse width modulator (PWM). A V below V stops
COMP ZDC
converter switching, while voltages above (V + 5 x (V + V )) does not increase the requested peak
ZDC CSMAX SLOPE
current in the switching MOSFET.
The internal start-up current source and control logic implement a bootstrap-type startup. The startup current
source charges C from VDD and maintain its voltage when the converter is disabled or during the soft-start
VCC
period, while operational power must come from a converter (bias winding) output.
The bootstrap source provides reliable start-up from widely varying input voltages, and eliminates the continual
power loss of external resistors.
The peak current limit does not have duty cycle dependency unless R is used as shown in Figure 8-2 to
S
increase slope compensation. This makes it easier to design the current limit to a fixed value.
The DC-DC controller has an OTSD that can be triggered by heat sources including the VB regulator, GATE
driver, bootstrap current source, and bias currents. The controller OTSD turns off VB, the switching FET, resets
the soft-start generator, and forces the VCC control into an undervoltage state.
8.3.7.1 VCC, VB, VBG and Advanced PWM Startup
The VCC pin connects to the auxiliary bias supply for the DC-DC controller. The switching MOSFET gate driver
draws current directly from the VCC pin. VB and VBG outputs are regulated down from VCC voltage, the
former providing power to the internal control circuitry and external feedback optocoupler (when in use), and
the latter providing power to the switching FET gate predriver circuit. A startup current source from VDD to
VCC implements the converter bootstrap startup. VCC must receive power from an auxiliary source, such as an
auxiliary winding on the flyback transformer, to sustain normal operation after startup.
The startup current source is turned on during the inrush phase, charging C and maintaining its voltage,
VCC
and it is turned off only after the DC-DC soft-start cycle has been completed, which occurs when the DC-DC
converter has ramped up its output voltage and V has exceed approximately 2.1 V (V ), as shown in
SST STUOF
Figure 8-1. Internal loading on VCC, VB and VBG is initially minimal while C charges, to allow the converter
VCC
to start. Due to the high current capability of the startup source, the recommended capacitance at VCC is
relatively small, typically 1 uF in most applications.
Once V falls below its UVLO threshold (V , approximately 6.1 V), the converter shuts off and the
VCC CUVLO_F
startup current source is turned back on, initiating a new PWM startup cycle.
If however a V fall (below approximately 7.1 V) is due to a light load condition causing temporary switching
VCC
stop, the startup is immediately and for a short period turned back on to bring VCC voltage back up, with no
converter interruption.
tinrush max
PSE PSE Inrush Operational Mode
tinrush min
PD VCC Startup Source ON End of Soft-Start, Startup source
turned off
HSW cap PD + Power Supply Fully
recharge Operational
Wait Soft Start High current startup is ON for the whole soft-start
cycle to allow low VCC capacitance
Ensures interoperability with
PSE inrush limit
Figure 8-1. Advanced Startup
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 23
Product Folder Links: TPS23730
```

### Page 24

#### Raw extracted text

```text
Note that the startup current source is also turned on while in soft-stop mode.
8.3.7.2 CS, Current Slope Compensation and Blanking
The current-sense input for the DC-DC converter should be connected to the high side of the current-sense
resistor of the switching MOSFET. This voltage drives the current limit comparator and the PWM comparator
(see Block Diagram of DC-DC controller). A leading-edge blanking circuit prevents MOSFET turn-on transients
from falsely triggering either of these comparators. During the off time, and also during the blanking time that
immediately follows, the CS pin is pulled to AGND through an internal pulldown resistor.
The current limit comparator terminates the on-time portion of the switching cycle as soon as V exceeds
CS
approximately 250 mV (V ) and the leading edge blanking interval has expired. If the converter is not in
CSMAX
current limit, then either the PWM comparator or the maximum duty cycle limiting (D ) circuit terminates the
MAX
on time.
Current-mode control requires addition of a compensation ramp to the sensed inductive (transformer or inductor)
current for stability at duty cycles near and over 50%. The TPS23730 provides an internal slope compensation
circuit which generates a current that imposes a voltage ramp at the positive input of the PWM comparator to
suppress sub-harmonic oscillations. This current flows out of the CS pin. If desired, the magnitude of the slope
compensation can be increased by the addition of an external resistor R (see Figure 8-2) in series with the CS
S
pin. It works with ramp current (I = I , approximately 20 uA) that flows out of the CS pin when the MOSFET
PK SL-EX
is on. The I specification does not include the approximately 2-uA fixed current that flows out of the CS pin.
PK
The TPS23730 has a maximum duty cycle limit of 78%, permitting the design of wide input-range converters
with a lower voltage stress on the output rectifiers. While the maximum duty cycle is 78%, converters may be
designed that run at duty cycles well below this for a narrower, 36-V to 57-V range.
Most current-mode control papers and application notes define the slope compensation values in terms of
V /T (peak ramp voltage / switching period); however, Electrical Characteristics: DC-DC Controller Section
PP S
specifies the slope peak (V ) based on the maximum duty cycle. Assuming that the desired slope, V
SLOPE SLOPE-D
(in mV/period), is based on the full period, compute R per Equation 1 where V , D , and I are from
S SLOPE MAX SL-EX
Electrical Characteristics: DC-DC Controller Section with voltages in mV, current in uA, and the duty cycle is
unitless (for example, D = 0.78).
MAX
V (mV)
BV SLOPE_D:mV;F @ SLOPE W D AC
R S:3;=
I (JA)
MAX x1000
SL_EX (1)
GATE
CS
R
CS
NTR
R
S
C
S
DNGA
DNG
TPS23730
SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020 www.ti.com
Figure 8-2. Additional Slope Compensation
The TPS23730 blanker timing is precise enough that the traditional R-C filters on CS can be eliminated. This
avoids current-sense waveform distortion, which tends to get worse at light output loads. There may be some
situations or designers that prefer an R-C approach, for example if the presence of R causes increased noise,
S
due to adjacent noisy signals, to appear at CS pin. The TPS23730 provides a pulldown on CS (~400 Ohm) during
24 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS23730
```

### Page 25

#### Raw extracted text

```text
TPS23730
www.ti.com SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020
the GATE OFF-time to improve sensing when an R-C filter must be used, by reducing cycle-to-cycle carry-over
voltage on C .
S
Routing between the current-sense resistor and the CS pin should be short to minimize cross-talk from noisy
traces such as the gate drive signal and the CP signal.
8.3.7.3 COMP, FB, EA_DIS, CP, PSRS and Opto-less Feedback
The TPS23730 DC-DC controller implements current-mode control as shown in Functional Block Diagram, using
internal (via pins FB input and COMP output, with EA_DIS pulled low) or external (via COMP input, with EA_DIS
open) voltage control loop error amplifier to define the input reference voltage of the current mode control
comparator which determines the switching MOSFET peak current.
V below V causes the converter to stop switching. The maximum (peak) current is requested at
COMP ZDC
approximately (V + 5 x (V + V )). The AC gain from COMP to the PWM comparator is typically 0.2.
ZDC CSMAX SLOPE
In flyback applications and with the internal error amplifier enabled, the TPS23730 DC-DC controller can operate
with feedback from an auxiliary winding of the flyback power transformer to achieve primary side regulation
(PSR), eliminating the need for external shunt regulator and optocoupler. One noteworthy characteristic of this
PSR is that it operates with continuous (DC) feedback, enabling better optimization of the power supply, and
resulting in significantly lower noise sensitivity.
When combined with secondary-side synchronous rectification (with PSRS open), the opto-less operation of
the TPS23730 is achieved with a unique approach which basically consists in actively cancelling (through
the use of CP output) the leading-edge voltage overshoot (causing the feedback capacitor to peak-charge)
generated by the transformer winding. When combined with a correctly designed power transformer, less than
+/-1.5% load regulation (typical) over the full output current range becomes achievable in applications making
use of secondary-side synchronous rectifiers. Operation is in continuous conduction mode (CCM), also enabling
multi-output architectures.
Opto-less operation of the TPS23730 also applies (with PSRS pulled low) to single-output flyback converter
applications where a secondary-side diode rectifier is used. In typical 12-V output application and when
combined with a correctly designed power transformer, ~+/-3% load regulation over a wide (< 5% to 100%)
output current range can be achieved.
In applications where the internal error amplifier is disabled, the COMP pin receives the control voltage typically
from a TL431 or TLV431 shunt regulator driving an optocoupler, using VB pin as a pull up source, although other
configurations are possible.
8.3.7.4 FRS Frequency Setting and Synchronization
The FRS pin programs the (free-running) oscillator frequency, and may also be used to synchronize the
TPS23730 converter to a higher frequency. The internal oscillator sets the maximum duty cycle and controls the
current-compensation ramp circuit, making the ramp height independent of frequency. R must be selected
FRS
per Equation 2.
15000
R (k3)=
FRS f SW (kHz) (2)
The TPS23730 may be synchronized to an external clock to eliminate beat frequencies from a sampled system,
or to place emission spectrum away from an RF input frequency. Synchronization may be accomplished
by applying a short pulse ( > 25 ns) of magnitude V to FRS as shown in Figure 8-3. R must be
SYNC FRS
chosen so that the maximum free-running frequency is just below the desired synchronization frequency. The
synchronization pulse terminates the potential ON-time period, and the OFF-time period does not begin until the
pulse terminates. A short pulse is preferred to avoid reducing the potential ON-time.
Figure 8-3 shows examples of nonisolated and transformer-coupled synchronization circuits. RT reduces noise
susceptibility for the isolation transformer implementation. The FRS node must be protected from noise because
it is high impedance.
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 25
Product Folder Links: TPS23730
```

### Page 26

#### Raw extracted text

```text
FRS
R
SRF
Synchronization
Pulse
47pF
1000pF
T
SYNC
V
SYNC
1:1
NTR
R T
FRS
R
SRF
Synchronization
Pulse
47pF
T
SYNC
V
SYNC
NTR
TPS23730
SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020 www.ti.com
Copyright  2016,Texas Instruments Incorporated
Figure 8-3. Synchronization
8.3.7.5 DTHR and Frequency Dithering for Spread Spectrum Applications
The international standard CISPR 22 (and adopted versions) is often used as a requirement for conducted
emissions. Ethernet cables are covered as a telecommunication port under section 5.2 for conducted emissions.
Meeting EMI requirements is often a challenge, with the lower limits of Class B being especially hard. Circuit
board layout, filtering, and snubbing various nodes in the power circuit are the first layer of control techniques.
A more detailed discussion of EMI control is presented in Practical Guidelines to Designing an EMI Compliant
PoE Powered Device With Isolated Flyback, SLUA469. Additionally, IEEE 802.3at sections 33.3 and 33.4 and
IEEE 802.3bt sections 145.3 and 145.4 have requirements for noise injected onto the Ethernet cable based on
compatibility with data transmission.
A technique referred to as frequency dithering can also be used to provide additional EMI measurement
reduction. The switching frequency is modulated to spread the narrowband individual harmonics across a wider
bandwidth, thus lowering peak measurements.
Fully programmable frequency dithering is a built-in feature of the TPS23730. The oscillator frequency can be
dithered by connecting a capacitor from DTHR to RTN and a resistor from DTHR to FRS. An external capacitor,
C (Figure 9-1), is selected to define the modulation frequency f . This capacitor is being continuously
DTR m
charged and discharged between slightly less than 0.5 V and slightly above 1.5 V by a current source/sink
equivalent to ~3x the current through FRS pin. C value is defined according to:
DTR
3
WR (3)
C = FRS
DTR 2.052xf (Hz)
m (3)
f should always be higher than 9 kHz, which is the resolution bandwidth applied during conducted emission
m
measurement. Typically, f should be set to around 11 kHz to account for component variations.
m
The resistor R is used to determine f, which is the amount of dithering, and its value is determined
DTR
according to:
0.513xR (3)
R (3)= FRS
DTR %DTHR (4)
For example, a 13.2% dithering with a nominal switching frequency of 250 kHz results in frequency variation of
+/-33 kHz.
8.3.7.6 SST and Soft-Start of the Switcher
Converters require a soft-start to prevent output overshoot on startup. In PoE applications, the PD also needs
soft-start to limit its input current at turn on below the limit allocated by the power source equipment (PSE).
For flyback applications using primary-side control, the TPS23730 provides closed loop controlled soft-start,
which applies a slowly rising ramp voltage to a second control input of the error amplifier. The lower of the
reference input and soft-start ramp controls the error amplifier, allowing the output voltage to rise in a smooth
monotonic fashion.
In all other applications where secondary-side regulation is used, the TPS23730 provides a current-loop
soft-start, which controls the switching MOSFET peak current by applying a slowly rising ramp voltage to a
26 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS23730
```

### Page 27

#### Raw extracted text

```text
TPS23730
www.ti.com SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020
second PWM control input. The lower of COMP-derived current demand and soft-start ramp controls the PWM
comparator. Note that in this case there is usually a (slower) secondary-side soft-start implemented with the
typical TL431 or TLV431 error amplifier to complement the action of the primary-side soft-start.
The soft-start period of the TPS23730 is adjustable with a capacitor between SST and RTN. During soft-start,
C (Figure 9-1) is being charged from less than 0.2 V to 2.45 V by a ~10-uA current source. Once V has
SST SST
exceeded approximately 2.1 V (V ), the VCC startup is also turned off.
STUOF
The actual control range of the primary-side closed-loop soft-start capacitor voltage is between 0.25 V and 2
V nominally. Therefore, the soft-start capacitor value must be based on this control range and the required
soft-start period (t ) according to:
SS
C (nF)=
I
SSC
:JA; x t
SS
(ms)
SS (2F0.25)
(5)
The actual control range of the current-loop soft-start capacitor voltage is between 0.6 V and 1.2 V nominally.
Therefore, the soft-start capacitor value must be based on this control range and the required soft-start period
(t ) according to:
SS
C (nF)=
I
SSC
:JA; x t
SS
(ms)
SS (1.2F0.6)
(6)
Note that the VCC startup turns off only when 2.1 V is reached, allowing additional time for the secondary-side
soft-start to complete. For more details regarding the secondary-side soft start, refer to Application Information.
8.3.7.7 SST, I_STP, LINEUV and Soft-Stop of the Switcher
The soft-stop feature is provided by the TPS23730 to minimizes stress on switching power components caused
by power shutdown, allowing FET BOM cost reduction, in particular for ACF applications. Soft-stop action
consists in discharging in a controlled way the output capacitor of the converter, sending back the energy to the
input bulk capacitor.
Once the LINEUV input detects that the input power source has been removed (while APD is also low), the SST
capacitor is discharged with a constant current, ramping down the switching MOSFET peak current. The SST
discharge current (I ) is defined with R according to:
SSD_SP I_STP
1000
I (JA)=
SSD_SP R :kA;
I_STP
(7)
To accelerate the impact of the soft-stop, the internal peak current limit threshold is also immediately stepped
down to approximately 50 mV at beginning of soft-stop.
8.3.8 Switching FET Driver - GATE, GTA2, DT
GATE is the gate drive outputs for the DC-DC converter's main switching MOSFET, while GAT2 is its second
gate drive.
GATE's phase turns the main switch on when it transitions high, and off when it transitions low. It is also held low
when the converter is disabled.
GAT2's phase turns the second switch off when it transitions high, and on when it transitions low. GAT2 is also
held low when the converter is disabled. This output can drive active-clamp PMOS devices, and driven flyback
synchronous rectifiers. Connecting DT to VB also disables GAT2 in a high-impedance condition.
DT input is used to set the delay between GATE and GAT2 to prevent overlap of MOSFET on times as shown in
Figure 7-1. Both MOSFETs should be off between GAT2 going high to GATE going high, and GATE going low to
GAT2 going low. The maximum GATE ON time is reduced by the programmed dead-time period. The dead time
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 27
Product Folder Links: TPS23730
```

### Page 28

#### Raw extracted text

```text
TPS23730
SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020 www.ti.com
period is specified with 1 nF of capacitance on GATE and with 0.5-nF capacitance on GAT2. Different loading
on these pins changes the effective dead time. A resistor connected from DT to AGND sets the delay between
GATE and GAT2 following TBD figure. Note that even in situations like VCC UVLO or return to inrush phase, the
programmed dead time is maintained until the switching stops completely.
8.3.9 EMPS and Automatic MPS
To maintain PSE power in situation of very low I condition, the TPS23730 generates a pulsed current through
RTN
VSS pin with an amplitude adjusted such that its net current reaches a level high enough to maintain power.
The pulsed current amplitude (I , I ) and duration (t , t ) are automatically selected according to
MPSL MPSH MPSL MPSH
PSE Type (1-2, 3-4), to maintain PSE power while minimizing power consumption. Auto-stretch feature is also
used to cancel the impact of system conditions (bulk capacitance and PoE cable impedance) on the effective
pulsed current duration. See Figure 8-4, where the illustrated pulsed current is coming out of the VSS pin, while
I is the DC current going into the RTN pin.
LOAD
TMPS Pulse
IEEE IHold Stretching
I
Load IEEE IHold TMPS
0 mA
Unloaded power
supply
Measured IVSS
Adds only the extra current to reach IHold Stretches the pulse if necessary based on measured current
Figure 8-4. Auto MPS
Note that prior to entering the MPS mode, a light load condition is detected on RTN pin with a deglitch time
period of approximately 5 ms.
8.3.10 VDD Supply Voltage
VDD connects to the positive side of the input supply. It provides operating power to the PD controller, allows
monitoring of the input line voltage and serves as the source of DC-DC converter startup current. If V falls
VDD
below its UVLO threshold and goes back above it, or if a thermal shutdown resumes even if V remains above
VDD
its UVLO threshold, the TPS23730 returns to inrush phase.
8.3.11 RTN, AGND, GND
RTN is internally connected to the drain of the PoE hotswap MOSFET, while AGND is the quiet analog reference
for the DC-DC controller return. GND is the power ground used by the flyback power FET gate driver and CP
output, and should be tied to AGND and RTN plane. The AGND / GND / RTN net should be treated as a local
reference plane (ground plane) for the DC-DC control and converter primary. The PAD_G exposed thermal pad
is internally connected to RTN pin.
8.3.12 VSS
VSS is the PoE input-power return side. It is the reference for the PoE interface circuits, and has a current-
limited hotswap switch that connects it to RTN. VSS is clamped to a diode drop above RTN by the hotswap
switch. The PAD_S exposed thermal pad is internally connected to VSS pin. This pad must be connected to VSS
pin to ensure proper operation.
8.3.13 Exposed Thermal pads - PAD_G and PAD_S
PAD_G should be tied to a large RTN copper area on the PCB to provide a low resistance thermal path to the
circuit board.
PAD_S should be tied to a large VSS copper area on the PCB to provide a low resistance thermal path to the
circuit board. TI recommends maintaining a clearance of 0.025 between VSS and high-voltage signals such as
VDD.
28 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS23730
```

### Page 29

#### Extracted tables

Table 1:

```text
Shut- down | Norm | al Operation
```

Table 2:

```text
| Mark |
```

Table 3:

```text
| Normal Operation
```

#### Raw extracted text

```text
8.4 Device Functional Modes
8.4.1 PoE Overview
The following text is intended as an aid in understanding the operation of the TPS23730, but it is not a substitute
for the actual IEEE 802.3bt or 802.3at standards. The IEEE 802.3bt standard is an update to IEEE 802.3-2018,
adding Clause 145 (PoE), including power delivery using all four pairs, high-power options, additional features to
reduce standby power consumption and enhanced classification.
Generally speaking, a device compliant to IEEE 802.3-2012 is referred to as a Type 1 (Class 0-3) or 2 (Class
4) device, and devices with higher power and enhanced classification is referred to as Type 3 (Class 5, 6) or
4 (Class 7, 8) devices. Type 3 devices will also include Class 0-4 devices that are 4-pair capable. Standards
change and must always be referenced when making design decisions.
The IEEE 802.3at and 802.3bt standards define a method of safely powering a PD (powered device) over a
cable by power sourcing equipment (PSE), and then removing power if a PD is disconnected. The process
proceeds through an idle state and three operational states of detection, classification, and operation. There
is also a fourth operational state used by Type 3 and 4 PSEs, called "connection check", to determine if the
PD has same (single interface) or independent (dual interface or commonly referred to "dual-signature" in the
IEEE802.3bt standard) classification signature on each pairset. The PSE leaves the cable unpowered (idle state)
while it periodically looks to see if something has been plugged in; this is referred to as detection. The low power
levels used during detection and connection check are unlikely to damage devices not designed for PoE. If a
valid PD signature is present, the PSE may inquire how much power the PD requires; this is referred to as
classification. The PSE may then power the PD if it has adequate capacity.
Type 3 or Type 4 PSEs are required to do an enhanced hardware classification of Type 3 or 4 respectively. Type
2 PSEs are required to do Type 1 hardware classification plus a data-layer classification, or an enhanced Type
2 hardware classification. Type 1 PSEs are not required to do hardware or data link layer (DLL) classification. A
Type 3 or Type 4 PD must do respectively Type 3 or Type 4 hardware classification as well as DLL classification.
A Type 2 PD must do Type 2 hardware classification as well as DLL classification. The PD may return the
default, 13-W current-encoded class, or one of four other choices if Type 2, one of six other choices if Type 3,
and one of eight other choices if Type 4. DLL classification occurs after power-on and the Ethernet data link has
been established
Once started, the PD must present the maintain power signature (MPS) to assure the PSE that it is still present.
The PSE monitors its output for a valid MPS, and turns the port off if it loses the MPS. Loss of the MPS returns
the PSE to the idle state. Figure 8-5 shows the operational states as a function of PD input voltage.
n tim oiL
itc
e te
re
w o DL
2.7 10.1 14.5 20.5 30 57 37 42
noitceteD timiL
reppU
n ati o mit
sifi
c
er
Li
sw Cl a L o
noitacifissalC timiL
reppU
- y
b ffO n ru
T
g n illa F
e g
ts u a tlo MV
- timiL
rewoL
egnaR
gnitarepO
y-
n b n g tu p
T
ur n O
g e
Ri si n I m
u m e g
u st olt a ix a a tlo MV MV
Shut-
Detect Classify
down
0
PI Voltage (V)
- timiL
rewoL
.pO
W31
Mark
kraM-ssalC
noitisnarT
sP052
tneisnarT
Normal Operation
6.9
Normal Operation
LPT/HPT
egnaR
teseR
TPS23730
www.ti.com SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020
42.5
Figure 8-5. Operational States
The PD input, typically an RJ-45 eight-lead connector, is referred to as the power interface (PI). PD input
requirements differ from PSE output requirements to account for voltage drops and operating margin. The
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 29
Product Folder Links: TPS23730
```

### Page 30

#### Extracted tables

Table 1:

```text
| POWER LOOP | PSE OUTPUT | PSE STATIC OUTPUT | PD INPUT | STATIC PD INPUT VOLTAGE | 
STANDARD | RESISTANCE (MAX) | POWER (MIN) | VOLTAGE (MIN) | POWER (MAX) | POWER <= 13 W | POWER > 13 W
IEEE802.3-2012 802.3at (Type 1) | 20 Ohm | 15.4 W | 44 V | 13 W | 37 V - 57 V | N/A
802.3bt (Type 3) | 12.5 Ohm |  | 50 V |  |  | 
802.3at (Type 2) 802.3bt (Type 3) | 12.5 Ohm | 30 W | 50 V | 25.5 W | 37 V - 57 V | 42.5 V - 57 V
802.3bt (Type 3) | 6.25 Ohm (4-pair) | 60 W | 50 V | 51 W | N/A | 42.5 V - 57 V
802.3bt (Type 4) | 6.25 Ohm (4-pair) | 90 W | 52 V | 71.3 W | N/A | 41.2 V - 57 V
```

#### Raw extracted text

```text
standard allots the maximum loss to the cable regardless of the actual installation to simplify implementation.
IEEE 802.3-2008 was designed to run over infrastructure including ISO/IEC 11801 class C (CAT3 per TIA/
EIA-568) that may have had AWG 26 conductors. IEEE 802.3at Type 2 and IEEE 802.3bt Type 3 cabling power
loss allotments and voltage drops have been adjusted for 12.5- Ohm power loops per ISO/IEC11801 class D (CAT5
or higher per TIA/EIA-568, typically AWG 24 conductors). Table 8-4 shows key operational limits broken out for
the two revisions of the standard.
Table 8-4. Comparison of Operational Limits
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
The PSE can apply voltage either between the RX and TX pairs (pins 1-2 and 3-6 for 10baseT or 100baseT),
or between the two spare pairs (4-5 and 7-8). Power application to the same pin combinations in 1000/2.5G/5G/
10GbaseT systems is recognized in IEEE 802.3bt. 1000/2.5G/5G/10GbaseT systems can handle data on all
pairs, eliminating the spare pair terminology. Type 1 and 2 PSEs are allowed to apply voltage to only one set of
pairs at a time, while Type 3 and 4 PSEs may apply power to one or both sets of pairs at a time. The PD uses
input diode or active bridges to accept power from any of the possible PSE configurations. The voltage drops
associated with the input bridges create a difference between the standard limits at the PI and the TPS23730
specifications.
A compliant Type 2, 3 or 4 PD has power management requirements not present with a Type 1 PD. These
requirements include the following:
1. Must interpret respectively Type 2, 3 or 4 hardware classification.
2. Must present hardware Class 4 during the first two classfication events, applicable to Type 2 and 4 PDs, as
well as to Type 3 PD with Class level 4 or higher.
3. If Type 3 Class 5-6 or Type 4 single interface PD, it must present hardware Class in the range of 0 to 3
during the third and any subsequent classification events.
4. Must implement DLL negotiation.
5. Must draw less than 400 mA from 50 ms until 80 ms after the PSE applies operation voltage (power up), if
Type 2 or 3, single interface PD. This covers the PSE inrush period, which is 75 ms maximum.
6. Must draw less than 800 mA total and 600 mA per pairset from 50 ms until 80 ms after the PSE applies
operation voltage (power up), if Type 4 (Class 7-8) single interface PD.
7. Must not draw more than 60 mA and 5 mA any time the input voltage falls below respectively 30 V and 10 V.
8. Must not draw more than 13 W if it has not received at least a Type 2 hardware classification or received
permission through DLL.
9. Must not draw more than 25.5 W if it has not received at least 4 classification events or received permission
through DLL.
10. Must not draw more than 51 W if it has not received at least 5 classification events or received permission
through DLL.
11. Must meet various operating and transient templates.
12. Optionally monitor for the presence or absence of an adapter.
As a result of these requirements, the PD must be able to dynamically control its loading, and monitor TPL and
TPH for changes. TPH and TPL  can also be used in cases where the design needs to know specifically if an
adapter is plugged in and operational.
8.4.2 Threshold Voltages
The TPS23730 has a number of internal comparators with hysteresis for stable switching between the various
states as shown in Figure 8-5. Figure 8-6 relates the parameters in Electrical Characteristics PoE  to the PoE
TPS23730
SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020 www.ti.com
30 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS23730
```

### Page 31

#### Raw extracted text

```text
states. The mode labeled idle between classification and operation implies that the DEN, CLSA, CLSB, and RTN
pins are all high impedance. The state labeled Mark, which is drawn in dashed lines, is part of the Type 2-3-4
hardware class state machine.
VUVLO_R
Detection
Classification
PD Powered
Idle
VCL_ON
VCL_H
VCU_OFF
VCU_H
Note:  Variable names refer to Electrical Characteristic
          Table parameters
VDD-VSS
VUVLO_H
Mark
VMSR
Functional
State
Figure 8-6. Threshold Voltages
8.4.3 PoE Start-Up Sequence
The waveforms of Figure 8-7 demonstrate detection, classification, and start-up from a Type 3 or 4 PSE with
Class 6 hardware classification . The key waveforms shown are V VDD-VSS, V RTN-VSS, and I PI. IEEE802.3bt and
IEEE 802.3at require a minimum of two detection levels; however, four levels are shown in this example. Four
levels guard against misdetection of a device when plugged in during the detection sequence.
IEEE 802.3bt also requires a PSE allocating Class 6 level of power to generate four class and mark cycles, and
startup from the fourth mark event. As shown below, the required minimum duration of the first class event has
been extended for Type 3 and 4 PSEs.  VRTN to V SS falls as the TPS23730 charges C BULK following application
of full voltage. In Figure 8-9, the converter soft-start is also delayed until the end of inrush period.
www.ti.com
TPS23730
SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 31
Product Folder Links: TPS23730
```

### Page 32

#### Extracted tables

Table 1:

```text
|  |  |  |  | DC | DC |  | enab |  |  |  | led a |  |  |  | fter |  |  |  |  |  |  |  | 
 |  |  |  |  |  | Star |  | tup d |  |  |  | elay |  |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  | I |  |  | I | nrush |  |  |  |  |  |  |  |  |  |  |  | 
 |  | I PI |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  | Clas |  |  |  | s |  | M |  | ark |  |  |  |  |  |  |  | 
 |  | ect |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
Det |  | ect |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
```

#### Raw extracted text

```text
Time: 50ms/div
vid/Am001
:tnerruC
vid/V01
:egatloV
TPS23730
SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020 www.ti.com
DC-DC enabled after
Startup delay
Inrush
I
PI
V
VDD-VSS
Class Mark
Detect
V
RTN-VSS
Figure 8-7. PoE Start-Up Sequence
8.4.4 Detection
The TPS23730 is in detection mode whenever V is below the lower classification threshold. When the
VDD-V SS
input voltage rises above V , the DEN pin goes to an open-drain condition to conserve power. While in
CL_ON
detection, RTN is high impedance, almost all the internal circuits are disabled, and the DEN pin is pulled to V .
SS
An R of 25.5 kOhm (1%), presents the correct signature. It may be a small, low-power resistor because it only
DEN
sees a stress of about 5 mW. A valid PD detection signature is an incremental resistance between 23.75 kOhm and
26.25 kOhm at the PI.
The detection resistance seen by the PSE at the PI is the result of the input bridge resistance in series with
the parallel combination of R and the TPS23730 bias loading. The incremental resistance of the input diode
DEN
bridge may be hundreds of ohms at the very low currents drawn when 2.7 V is applied to the PI. The input bridge
resistance is partially cancelled by the effective resistance of the TPS23730 during detection.
8.4.5 Hardware Classification
Hardware classification allows a PSE to determine a PDs power requirements before powering, and helps with
power management once power is applied. Type 2, 3, and 4 hardware classification permits high power PDs to
determine whether the PSE can support its high-power operation. The number of class cycles generated by the
PSE prior to turn on indicates to the PD if it allots the power requested or if the allocated power is less than
requested, in which case there is power demotion.
A Type 2 PD always presents Class 4 in hardware to indicate that it is a 25.5W device. A Class 5 or 6 Type
3 PD presents Class 4 in hardware during the first two class events and it presents Class 0 or 1, respectively,
for all subsequent class events. A Class 7 or 8 Type 4 PD presents Class 4 in hardware during the first two
class events and it presents Class 2 or 3, respectively, for all subsequent class events. A Type 1 PSE will treat
32 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS23730
```

### Page 33

#### Raw extracted text

```text
a Class 4 to 8 device like a Class 0 device, allotting 13 W if it chooses to power the PD. A Type 2 PSE will treat
a Class 5 to 8 device like a Class 4 device, allotting 25.5W if it chooses to power the PD. A Class 4 PD that
receives a 2-event class, a Class 5 or 6 PD that receives a 4-event class, or a Class 7 or 8 PD that receives
a 5-event class, understands that the PSE has agreed to allocate the PD requested power. In the case where
there is power demotion, the PD may choose to not start, or to start while not drawing more power than initially
allocated, and request more power through the DLL after startup. The standard requires a Type 2, 3 or 4 PD
to indicate that it is underpowered if this occurs. Startup of a high-power PD at lower power than requested
implicitly requires some form of powering down sections of the application circuits.
The maximum power entries in Table 8-1 determine the class the PD must advertise. The PSE may disconnect
a PD if it draws more than its stated class power, which may be the hardware class or a DLL-derived power
level. The standard permits the PD to draw limited current peaks that increase the instantaneous power above
the Table 8-1 limit; however, the average power requirement always applies.
The TPS23730 implements one- to four-event classification. RCLSA and R CLSB resistor values define the class
of the PD . DLL communication is implemented by the Ethernet communication system in the PD and is not
implemented by the TPS23730.
The TPS23730 disables classification above V CU_OFF to avoid excessive power dissipation. CLSA/B voltage is
turned off during PD thermal limiting or when APD or DEN is active. The CLSA and CLSB outputs are inherently
current-limited, but should not be shorted to VSS for long periods of time.
Figure 8-8  shows how classification works for the TPS23730. Transition from state-to-state occurs when
comparator thresholds are crossed (see Figure 8-5  and Figure 8-6 ). These comparators have hysteresis,
which adds inherent memory to the machine. Operation begins at idle (unpowered by PSE) and proceeds
with increasing voltage from left to right. A 2 - to 4-event classification follows the (heavy lined) path towards the
bottom, ending up with a latched TPL/TPH decode  along the lower branch that is highlighted. Once the valid
path to the PSE detection is broken, the input voltage must transition below the mark reset threshold to start
anew.
www.ti.com
TPS23730
SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 33
Product Folder Links: TPS23730
```

### Page 34

#### Extracted tables

Table 1:

```text
PoE Startup Sequence Operating Between UVLO Mark Class TPH low Ranges Rising TPL open-drain TYPE 3 PSE Hardware Class UVLO Falling |  | 
 | Operating TPH low TPL open-drain |
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
Mark Class
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
TYPE 3 PSE
Hardware Class
Between
Ranges
Operating
TPL low
TPH open-drain
UVLO
Rising
PoE Startup Sequence
UVLO
Falling
Figure 8-8. Up to Four-Event Class Internal States
8.4.6 Maintain Power Signature (MPS)
The MPS is an electrical signature presented by the PD to assure the PSE that it is still present after operating
voltage is applied. For a Type 1 or Type 2 PD, a valid MPS consists of a minimum dc current of 10 mA, or a
10-mA pulsed current for at least 75 ms every 325 ms, and an AC impedance lower than 26.3 k Ohm in parallel with
0.05 uF. Only Type 1 and Type 2 PSEs monitor the AC MPS. A Type 1 or Type 2 PSE that monitors only the AC
MPS may remove power from the PD.
To enable applications with stringent standby requirements, IEEE802.3bt introduced a significant change
regarding the minimum pulsed current duration to assure the PSE will maintain power. This applies to all Type 3
and Type 4 PSEs, and the pulse duration is ~10% of what is required for Type 1 and 2 PSEs. The MPS current
amplitude requirement for Class 5-8 PDs have also increased to 16 mA at the PSE end of the ethernet cable.
If the current through the RTN-to-VSS path is very low, the TPS23730 automatically generates the MPS
pulsed current through the VSS pin, with an amplitude adjusted such that its net current reaches a level
high enough to maintain PSE power. The TPS23730 is also able to determine if the PSE is of Type 1-2 or
TPS23730
SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020 www.ti.com
34 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS23730
```

### Page 35

#### Raw extracted text

```text
TPS23730
www.ti.com SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020
Type 3-4, automatically adjusting the pulsed current amplitude, duration and duty-cycle, while minimizing power
consumption. Note that the IEEE802.3bt requirement for the PD is applicable at the PSE end of the cable.
That means that depending the cable length and other parameters including the bulk capacitance, a longer
pulse duration may be required to ensure a valid MPS. For that purpose, the TPS23730 provides auto-stretch
capability which is used to cancel the impact of such system conditions on the effective pulsed current duration.
See Figure 8-4.
When APD is pulled high or when DEN is pulled to VSS (forcing the hotswap switch off), the DC MPS will not be
met. A PSE that monitors the DC MPS will remove power from the PD when this occurs.
8.4.7 Advanced Start-Up and Converter Operation
The internal PoE undervoltage lockout (UVLO) circuit holds the hotswap switch off before the PSE provides
full voltage to the PD. This prevents the converter circuits from loading the PoE input during detection and
classification. The converter circuits discharges C , C , C and C while the PD is unpowered. Thus
BULK VCC VB VBG
V will be a small voltage until just after full voltage is applied to the PD, as seen in Figure 8-7.
VDD-RTN
The PSE drives the PI voltage to the operating range once it has decided to power up the PD. When V
VDD
rises above the UVLO turnon threshold (V , approximately 37.6 V) with RTN high, the TPS23730 enables
UVLO-R
the hotswap MOSFET with an approximately 140-mA (inrush) current limit. See the waveforms of Figure 8-9
for an example. Converter switching is disabled while C charges and V falls from V to nearly V ;
BULK RTN VDD VSS
however, the converter start-up circuit is allowed to charge C (the VB regulator also powers the internal
VCC
converter circuits as V rises). Once the inrush current falls about 10% below the inrush current limit, the
VCC
PD current limit switches to the operational level (approximately 1.85 A). Additionally, once the inrush period
duration has also exceeded approximately 84 ms (end of inrush phase), the converter switching is allowed to
start, once V also goes above its UVLO (approximately 8.25 V).
VCC
Continuing the start-up sequence shown in Figure 8-9, once V goes above its UVLO , the soft-start (SST)
VCC
capacitor is first discharged with controlled current (I ) below nominally 0.2 V (V ) if the discharge was not
SSD SFST
already completed, then it is gradually recharged until it reaches ~0.25 V (V in closed-loop mode) at which
SSOFS
point the converter switching is enabled, following the closed loop controlled soft-start sequence. Note that the
startup current source capability is such that it can fully maintain V during the converter soft-start without
VCC
requiring any significant C capacitance, in 48 V input applications. At the end of the soft-start period, more
VCC
specifically when SST voltage has exceeded ~2 V (V ), the startup current source is turned off. V falls
STUOF VCC
as it powers the internal circuits including the switching MOSFET gate. If the converter control-bias output rises
to support V before it falls to V (~6.1 V), a successful start-up occurs. Figure 8-9 shows a small droop
VCC CUVLO_F
in V while the output voltage rises smoothly and a successful start-up occurs.
VCC
Figure 8-10 also illustrates similar scenario if optocoupler feedback is used instead of PSR. In this case, the
converter switching is enabled when V exceeds approximately 0.6 V (V in peak current mode).
SST SSOFS
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 35
Product Folder Links: TPS23730
```

### Page 36

#### Extracted tables

Table 1:

```text
|  |  |  |  |  |  |  |  |  |  |  | TN |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  | V VDD-R |  | TN |  |  |  |  |  |  |  |  |  | 
PI |  |  |  |  |  |  |  |  |  |  |  | Conv sta |  |  | erter rts |  |  |  |  |  |  | 
 |  | powe |  |  |  |  | red |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
 |  | Inr | Inr |  |  |  | ush |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
 |  | I P |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  | I P |  |  | I |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  | V VC |  |  | C-RTN |  |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  |  |  | St |  | artup | turn |  |  |  | off, |  | 
 |  |  |  |  |  |  |  |  |  |  |  | TP | TP |  | H/TP | L ena |  |  |  | bled |  | 
 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | O |  |  |  |  |  | ge
 |  |  |  |  |  |  | V OUT |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | O |  | utput | Volta | ge
 |  | I |  |  |  |  |  |  |  |  |  | y |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  | I |  | nrush |  |  | Dela |  | y |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Sof |  |  |  | t | 
 |  |  |  |  |  |  | V S |  |  | ST |  |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Sof |  | t Star | t |
```

#### Raw extracted text

```text
TPS23730
SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020 www.ti.com
50V/div
V
VDD-RTN
Converter
PI powered
starts
Inrush
100mA/div
I
PI
V
VCC-RTN
Startup turn off,
TPH/TPL enabled
5V/div
5V/div V
OUT Output Voltage
Inrush Delay
V
1V/div SST Soft Start
Time: 20ms/div
Figure 8-9. Power Up and Start - Flyback with PSR
36 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS23730
```

### Page 37

#### Extracted tables

Table 1:

```text
|  |  |  |  |  |  |  |  |  |  |  |  | TN |  |  |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | V VDD-R |  | TN |  |  |  |  |  |  |  |  |  |  |  |  | 
PI |  |  |  |  |  |  |  |  |  |  |  |  | Con sta |  |  | verter rts |  |  |  |  |  |  |  |  |  | 
 |  |  | powe |  |  |  |  | red |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
 |  |  | Inr | Inr |  |  |  | ush |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
 |  |  | I P |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  | I P |  |  | I |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  | V VC |  |  | C-RTN |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  |  |  | S | S |  | tartup |  |  | turn |  |  | off |  |  |  | 
 |  |  |  |  |  |  |  | O |  | O | utput |  | Volta |  |  | g | e |  |  |  |  | Seco Soft S | ndary tart |  |  | 
 |  |  | V OUT |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
 |  |  | I |  |  |  |  |  |  |  |  |  | y |  |  |  |  |  |  |  |  | depe | ndent |  |  | 
 |  |  |  |  |  | I |  | nrush |  |  | Dela |  | y |  |  |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  | V SST |  |  |  |  |  |  |  |  |  |  | Pri Sof |  |  | mary I t Start | peak |  |  |
```

#### Raw extracted text

```text
TPS23730
www.ti.com SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020
50V/div
V
VDD-RTN
Converter
PI powered
starts
Inrush
100mA/div
I
PI
V
VCC-RTN
Startup turn off
5V/div
5V/div V Output Voltage Secondary
OUT
Soft Start
dependent
Inrush Delay
Primary I
peak
V
1V/div SST Soft Start
Time: 20ms/div
Figure 8-10. Power Up and Start - with Opto Feedback
The converter shuts off when V falls below its lower UVLO. This can happen when power is removed from
VCC
the PD, or during a fault on a converter output rail. When one output is shorted, all the output voltages fall
including the one that powers VCC. The control circuit discharges VCC until it hits the lower UVLO and turns
off. A restart initiates if the converter turns off and there is sufficient VDD voltage. This type of operation is
sometimes referred to as hiccup mode, which when combined with the soft-start provides robust output short
protection by providing time-average heating reduction of the output rectifier.
Figure 8-11 illustrates the situation when there is severe overload at the main output which causes VCC hiccup.
After VCC went below its UVLO due to the overload, the startup source is turned back on. Then, a new soft-start
cycle is reinitiated, the soft-start capacitor being first discharged with controlled current, introducing a short
pause before the output voltage is ramped up.
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 37
Product Folder Links: TPS23730
```

### Page 38

#### Extracted tables

Table 1:

```text
V overload OUT |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  | Turn |  | Conv off th |  | erter en re |  | start |  |  |  |  |  |  |  | 
I PI |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  |  |  | St |  | St | artup | turn o | ff
 |  |  |  |  |  |  |  |  |  |  |  |  | RTN |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  | V VCC |  |  | RTN |  |  |  |  | 
 |  |  |  |  | V UV | CC LO |  |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  | Soft |  |  |  |  |  |  |  | 
 |  |  |  | V SST |  |  |  |  |  |  | Soft |  | Start |  |  |  |  | 
 | T |  |  |  |  |  |  |  |  | O |  |  |  |  |  |  | ge | 
V OU | T |  |  |  |  |  |  |  |  |  |  | O | utput |  |  | Volta | ge |
```

#### Raw extracted text

```text
TPS23730
SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020 www.ti.com
V overload
OUT
Converter
Turn off then restart
I
PI
200mA/div
Startup turn off
V
VCC-RTN
VCC
5V/div
UVLO
1V/div V SST Soft Start
5V/div V Output Voltage
OUT
Time: 10ms/div
Figure 8-11. Restart Following Severe Overload at Main Output of PSR Flyback DC-DC Converter
Also, when a VCC fall occurs, the TPS23730 can differentiate between an overload and a light load condition.
For example a diode-rectified flyback with optocoupled feedback may have its VCC rail to fall in situation of light
load due to temporary switching stop. In this case, the output voltage has to be maintained and a soft-start would
not be acceptable. To address this case, if V falls below approximately 7.1 V due to light load, the TPS23730
VCC
turns back on the startup immediately and for a short period of time to bring VCC voltage back up, and there is
no soft-start recycling.
38 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS23730
```

### Page 39

#### Extracted tables

Table 1:

```text
I OU |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
 | I OU | T |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
V V | V V | CC-RTN |  |  |  |  |  | Star | Star | tup tu |  | rn on | then |  | off |  | 
 |  |  |  |  |  |  |  |  |  |  |  | V | CUV |  |  |  | 
 |  |  |  | St for | St for | artup shor |  | turn o t time |  | n |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  |  | VCC f | alls d |  | ue to |  | 
 |  |  |  |  |  |  |  |  |  |  |  | switch at ligh | ing in t load |  | terru |  | ption
V OU |  | T |  | Vout start |  | is ma recyc |  | intain ling |  | ed, n |  | o soft |  |  |  |  |
```

Table 2:

```text
V | CUV
```

#### Raw extracted text

```text
TPS23730
www.ti.com SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020
I
OUT
V Startup turn on then off
VCC-RTN
VCUV
Startup turn on
5V/div
for short time
VCC falls due to
switching interruption
at light load
10V/div V Vout is maintained, no soft
OUT
start recycling
Time: 10ms/div
Figure 8-12. Startup Operation if VCC Undervoltage is caused by Light Load Condition of Diode-rectified
Flyback DC-DC Converter
If V drops below the lower PoE UVLO (V , approximately 32 V), the hotswap MOSFET is turned
VDD-VSS UVLO_F
off, but the converter still runs (unless LINEUV input is pulled low). The converter stops if V falls below the
VCC
V (~6.1 V), the hotswap is in inrush current limit, the SST pin is pulled to ground, or the converter is in
CUVLO_F
thermal shutdown.
8.4.8 Line Undervoltage Protection and Converter Operation
When the input power source is removed, there are circumstances where stress may occur on the power
components. For example with ACF topology, as V gradually decreases the converter's operating duty
VDD-RTN
cycle must compensate for the lower input voltage. At minimum input voltage the duty cycle nears its maximum
value (D ), and the voltage across the clamp capacitor approaches its highest value since the transformer
MAX
must be reset in a relatively short time. This results in potentially damaging overvoltage and oscillations. Also
during next power up, due to precharged clamp capacitor, the soft-start could cause transformer saturation.
There are also situations where the output voltage capacitor may be able to back drive its secondary-side sync
MOSFET(s) after the converter switching has stopped completely, either temporarily or not. Such situation could
apply to both ACF and flyback (at power down or next soft-start) configurations.
To address this case, once the LINEUV voltage falls below V , the TPS23730 transitions to soft-stop mode.
LIUVF
It turns on temporarily the startup to maintain V , then uses the SST control to ramp down the switching
VCC
MOSFET peak current. As a result, the converter output is discharged in a controlled way, the energy of
the output capacitor being sent back to the input bulk capacitor. Also note that at beginning of soft-stop, the
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 39
Product Folder Links: TPS23730
```

### Page 40

#### Extracted tables

Table 1:

```text
| xx |
```

#### Raw extracted text

```text
TPS23730 temporarily forces the peak current to a low value (V CS maximum at approximately 50 mV), until SST
voltage becomes low enough to decrease it further. This advanced feature allows the soft-stop to immediately
start discharging the output capacitor, regardless of the output load level, minimizing any system tradeoffs for
optimum switching MOSFETs protection. See Figure 8-13.
VDD
VOUT
SST
LINEUV
CS
Power
down
xxx
Soft Stop begins
immediately at max
discharge current
xxx
xxx
x
x
Figure 8-13. Soft-Stop Operation
Once the soft-stop operation has been completed and to avoid subsequent oscillations caused by the impact of
the energy transfer on the LINEUV voltage, an internal load (~7 mA) is applied on VDD for approximately 160
ms, before the converter is allowed to restart.
8.4.9 PD Self-Protection
IEEE802.3bt includes new PSE output limiting requirements for Type 3 and 4 operation to cover higher power
and 4-pair applications. Type 2, 3 and 4 PSEs must meet an output current vs time template with specified
minimum and maximum sourcing boundaries. The peak output current per each 2-pair may be as high as
50 A for 10 us or 1.75 A for 75 ms, and the total peak current becomes twice these values when power is
delivered over 4 pairs. This makes robust protection of the PD device even more important than it was in IEEE
802.3-2012.
The PD section has the following self-protection functions.
* Hotswap switch current limit
* Hotswap switch foldback
* Hotswap thermal protection
The internal hotswap MOSFET of the TPS23730 is protected against output faults and input voltage steps with a
current limit and deglitched foldback. High stress conditions include converter output shorts, shorts from VDD to
RTN, or transients on the input line. An overload on the pass MOSFET engages the current limit, with V RTN-VSS
rising as a result. If V RTN rises above approximately 14.8 V for longer than approximately 1.8 ms, the current
limit reverts to the inrush limit, and turns the converter off, although there is no minimum inrush delay period (84
ms) applicable in this case. The 1.8-ms deglitch feature prevents momentary transients from causing a PD reset,
provided that recovery lies within the bounds of the hotswap and PSE protection. Figure 8-14 shows an example
of recovery from a 15-V PSE rising voltage step. The hotswap MOSFET goes into current limit, overshooting to
TPS23730
SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020 www.ti.com
40 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS23730
```

### Page 41

#### Extracted tables

Table 1:

```text
I PI |  |  |  |  |  |  |  |  |  |  |  | 
I PI |  |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  | C compl |  | BULK etes c | harge |  |  |  |  | 
 |  |  |  | while o |  | conve perate | rter s |  |  |  |  | 
 |  | V |  |  |  |  |  |  |  |  |  | 
 |  |  | V |  |  |  | 15V |  |  |  |  | 
 |  |  |  | VSS-RT |  | N |  |  |  |  |  | 
 |  |  |  |  |  | V VDD | VSS |  |  |  |  |
```

#### Raw extracted text

```text
TPS23730
www.ti.com SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020
a relatively low current, recovers to 1.85-A full current limit, and charges the input capacitor while the converter
continues to run. The MOSFET did not go into foldback because V was below 14.8 V after the 1.8-ms
RTN-VSS
deglitch.
I
PI
500mA/div
CBULK
completes charge
while converter
operates

V -15V
VSS-RTN
10V/div
20V/div V
VDD-VSS
Time: 400us/div
Figure 8-14. Response to PSE Step Voltage
The PD control has a thermal sensor that protects the internal hotswap MOSFET. Conditions like start-up or
operation into a VDD to RTN short cause high power dissipation in the MOSFET. An overtemperature shutdown
(OTSD) turns off the hotswap MOSFET and class regulator, which are restarted after the device cools. The PD
restarts in inrush phase when exiting from a PD overtemperature event.
Pulling DEN to VSS during powered operation causes the internal hotswap MOSFET to turn off. This feature
allows a PD with secondary-side adapter ORing to achieve adapter priority. Take care with synchronous
converter topologies that can deliver power in both directions.
The hotswap switch is forced off under the following conditions:
* V above V (approximately 1.5 V)
APD APDEN
* V <= V when V is in the operational range
DEN PD_DIS VDD-VSS
* PD over temperature
* V < PoE UVLO (approximately 32 V)
VDD-VSS
8.4.10 Thermal Shutdown - DC-DC Controller
The DC-DC controller has an OTSD that can be triggered by heat sources including the VB and VBG regulators,
GATE/GAT2 drivers, startup current source, and bias currents. The controller OTSD turns off VB, VBG, the
GATE/GAT2 drivers, and forces the VCC control into an under-voltage state.
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 41
Product Folder Links: TPS23730
```

### Page 42

#### Raw extracted text

```text
8.4.11 Adapter ORing
Many PoE-capable devices are designed to operate from either a wall adapter or PoE power. A local power
solution adds cost and complexity, but allows a product to be used if PoE is not available in a particular
installation. While most applications only require that the PD operate when both sources are present, the
TPS23730 device supports forced operation from either of the power sources. Figure 8-15 illustrates three
options for diode ORing external power into a PD. Only one option would be used in any particular design.
Option 1 applies power to the device input, option 2 applies power between the device PoE section and
the power circuit, and option 3 applies power to the output side of the converter. Each of these options
has advantages and disadvantages. A detailed discussion of the device and ORing solutions is covered in
application note Advanced Adapter ORing Solutions using the TPS23753, (SLVA306).
tenrehtE
morF
sremrofsnarT
Fu1.0 V85
R
R
NED
B/ASLC
V
DD
03732SPT
Low Voltage
DEN Output
CLSA/B
V SS
RTN
erapS
morF
ro
sriaP
sremrofsnarT Power
Circuit
Adapter Adapter Adapter
Option 1 Option 2 Option 3
Figure 8-15. ORing Configurations
tenrehtE
morF
sremrofsnarT
Fu1.0 V85
R
NED
R
B/ASLC
V
DD
CLSA/B
V
SS
erapS
morF
ro
sriaP
sremrofsnarT
DEN
PPD
D
A
Adapter
R
2DPP
TPS23730
SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020 www.ti.com
R
PPD1
Figure 8-16. Low-Voltage Option 1 ORing
Preference of one power source presents a number of challenges. Combinations of adapter output voltage
(nominal and tolerance), power insertion point, and which source is preferred determine solution complexity.
Several factors contributing to the complexity are the natural high-voltage selection of diode ORing (the simplest
42 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS23730
```

### Page 43

#### Raw extracted text

```text
TPS23730
www.ti.com SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020
method of combining sources), the current limit implicit in the PSE, PD inrush, and protection circuits (necessary
for operation and reliability). Creating simple and seamless solutions is difficult if not impossible for many of the
combinations. However, the TPS23730 device offers several built-in features that simplify some combinations.
Several examples demonstrate the limitations inherent in ORing solutions. Diode ORing a 48-V adapter with
PoE (option 1) presents the problem that either source may have the higher voltage. A blocking switch would
be required to assure that one source dominates. A second example is combining a 12-V adapter with PoE
using option 2. The converter draws approximately four times the current at 12 V from the adapter than it does
from PoE at 48 V. Transition from adapter power to PoE may demand more current than can be supplied by the
PSE. The converter must be turned off while C capacitance charges, with a subsequent converter restart at the
IN
higher voltage and lower input current. A third example is use of a 24-V adapter with ORing option 1. The PD
hotswap would have to handle two times the current, and have 1/4 the resistance (be 4 times larger) to dissipate
equal power.
The most popular preferential ORing scheme is option 2 with adapter priority. The hotswap MOSFET is disabled
when the adapter is used to pull APD high, blocking the PoE source from powering the output. This solution
works well with a wide range of adapter voltages, is simple, and requires few external parts. When the AC
power fails, or the adapter is removed, the hotswap switch is enabled. In the simplest implementation, the PD
momentarily loses power until the PSE completes its start-up cycle.
The DEN pin can be used to disable the PoE input when ORing with option 3. This is an adapter priority
implementation. Pulling DEN low, while creating an invalid detection signature, disables the hotswap MOSFET,
and prevents the PD from redetecting. This would typically be accomplished with an optocoupler that is driven
from the secondary side of the converter. Another option 3 alternative which does not require DEN optocoupler is
achievable by ensuring that the auxiliary voltage is always higher then the converter output; in this case, the PSE
power can then be maintained by use of the auto MPS function of the TPS23730.
The TPS23730 also supports the use of an option 1 adapter, for example 24-V, by use of the PPD input. See
Figure 8-16.
The IEEE standards require that the PI conductors be electrically isolated from ground and all other system
potentials not part of the PI interface. The adapter must meet a minimum 1500-Vac dielectric withstand test
between the output and all other connections for options 1 and 2. The adapter only needs this isolation for option
3 if it is not provided by the converter.
Adapter ORing diodes are shown for all the options to protect against a reverse-voltage adapter, a short on the
adapter input pins, and damage to a low-voltage adapter. ORing is sometimes accomplished with a MOSFET in
option 3.
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 43
Product Folder Links: TPS23730
```

### Page 44

#### Raw extracted text

```text
9 Application and Implementation
Note
Information in the following applications sections is not part of the TI component specification,
and TI does not warrant its accuracy or completeness. TIs customers are responsible for
determining suitability of components for their purposes, as well as validating and testing their design
implementation to confirm system functionality.
9.1 Application Information
The TPS23730 has the flexibility to support many power supply topologies that require a single PWM gate drive
or two complementary gate drives and will operate with current-mode control. Figure 9-1 provides an example of
an active clamp forward converter.
9.2 Typical Application
T1
tenrehtE
morF
sremrofsnarT
ASLCR
VDD
CLSA
VSS
sriaP
erapS
morF
sremrofsnarT
ro
+ CBULK
RDEN
DEN
0.1 (cid:29)F
58V VCC
GATE
CS
CDTR
SCR
VB
CVB
APD
FRS
DTHR
RTN
RFRS
48V
Adapter
1DPAR
VCC
TPH
I_in
DA
RDTR
SST
CSST
RAPD2
HPTR
TPL
LPTR
CLSB
PPD
BSLCR
DVC
BT
DVC2 CVCC
VB
VB
GAT2
Voltage
feedback COMP
GND DT circuitry
TLV431
RDT
1VUR
TPS23730
SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020 www.ti.com
LINEUV
RUV2
I_STP EMPS
RI_STP
Figure 9-1. Basic TPS23730 Implementation
44 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS23730
```

### Page 45

#### Extracted tables

Table 1:

```text
PARAMETER | TEST CONDITIONS | MIN | TYPICAL | MAX | UNIT
Input voltage | Power applied through PoE or adapter | 0 |  | 57 | V
Operating voltage | After startup | 30 |  | 57 | V
Adapter voltage |  | 40 |  | 57 | V
Input UVLO | Rising input voltage at device terminals |  |  | 40 | V
 | Falling input voltage | 30.5 |  |  | 
Detection voltage | At device terminals | 1.4 |  | 10.1 | V
Classification voltage | At device terminals | 11.9 |  | 23 | V
Class 4 | Class signature A | 38 |  | 42 | mA
DCDC Topology | Active Clamp Forward |  |  |  | 
Output Voltage |  |  | 12 |  | V
Output Current |  |  | 3.9 |  | A
End-to-End Efficiency | At full load |  | 91 |  | %
Switching Frequency |  |  | 250 |  | kHz
```

#### Raw extracted text

```text
TPS23730
www.ti.com SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020
9.2.1 Design Requirements
Selecting a converter topology along with a converter design procedure is beyond the scope of this application
section.
The TPS23730 has the flexibility to be used in high power density flyback topologies such as primary side
regulation synchronous or non-synchronous flyback.
Examples to help in programming the TPS23730 and additional design consideration are shown in Detailed
Design Procedure. For a more specific converter design example, refer to the TPS23730EVM-093 EVM that is
designed for the design parameters in Table 9-1.
Table 9-1. Design Parameters
PARAMETER TEST CONDITIONS MIN TYPICAL MAX UNIT
Input voltage Power applied through PoE or adapter 0 57 V
Operating voltage After startup 30 57 V
Adapter voltage 40 57 V
Rising input voltage at device terminals - 40
Input UVLO V
Falling input voltage 30.5 -
Detection voltage At device terminals 1.4 10.1 V
Classification voltage At device terminals 11.9 23 V
Class 4 Class signature A 38 42 mA
DCDC Topology Active Clamp Forward
Output Voltage 12 V
Output Current 3.9 A
End-to-End Efficiency At full load 91 %
Switching Frequency 250 kHz
9.2.1.1 Detailed Design Procedure
9.2.1.1.1 Input Bridges and Schottky Diodes
Using Schottky diodes instead of PN junction diodes for the PoE input bridges will reduce the power loss by
about 30%. These are often used to maximize the efficiency when FET bridge architectures are not used.
Schottky diode leakage current and different input bridge architectures can impact the detection signature.
Setting reasonable expectations for the temperature range over which the detection signature is accurate is the
simplest solution. Adjusting R slightly may also help meet the requirement.
DEN
A general recommendation for the input rectifiers are 2 A, 100-V rated discrete or bridge schottky diodes.
The TPS23730EVM-093 allows the option of either a discrete schottky bridge or a FET-Diode bridge for 1-2%
higher overall system efficiency.
9.2.1.1.2 Input TVS Protection
A TVS, across the rectified PoE voltage must be used. TI recommends a SMAJ58A, or a part with equal to or
better performance, for general indoor applications. If an adapter is connected from V to RTN, as in ORing
DD
option 2 above, voltage transients caused by the input cable inductance ringing with the internal PD capacitance
can occur. Adequate capacitive filtering or a TVS must limit this voltage to be within the absolute maximum
ratings. Outdoor transient levels or special applications require additional protection.
ESD events between the PD power inputs and converter output, cause large stresses in the hotswap MOSFET if
the input TVS becomes reverse biased and transient current around the TPS23730 is blocked. A SMAJ58A is a
good initial selection between RTN (cathode) and VSS (anode).
9.2.1.1.3 Input Bypass Capacitor
The IEEE 802.3bt standard specifies an input bypass capacitor (from V to V ) of 0.05 uF to 0.12 uF. Typically
DD SS
a 0.1-uF, 100-V, 10% ceramic capacitor is used.
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 45
Product Folder Links: TPS23730
```

### Page 46

#### Raw extracted text

```text
TPS23730
SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020 www.ti.com
9.2.1.1.4 Detection Resistor, R
DEN
The IEEE 802.3bt standard specifies a detection signature resistance, R from 23.7 kOhm to 26.3 kOhm, or 25 kOhm +/-
DEN
5%. Choose an R of 25.5 kOhm.
DEN
9.2.1.1.5 Classification Resistor, R and R .
CLSA CLSB
Connect a resistor from CLSA and CLSB to V to program the classification current according to the IEEE
SS
802.3bt standard. The class power assigned should correspond to the maximum average power drawn by the
PD during operation. Select R according to Table 8-1.
CLSx
For a high-power design, choose Class 6 where R = 32 Ohm and R = 130 Ohm.
CLSA CLSB
9.2.1.1.6 Dead Time Resistor, R
DT
Program the dead time with a resistor connected from DT to RTN. The required dead-time period depends on
the specific topology and parasitics. The easiest technique to obtain the optimum timing resistor is to build the
supply. A good initial value is 100 ns. Then the dead time can be tuned to achieve the best efficiency after
considering all corners of operation (load, input voltage, and temperature).
1. Choose R as follows assuming a t of 100 ns:
DT DT
t (ns) 100
R (kW) = DT = =50
DT
a. 2 2
b. Choose R = 49.9 kOhm
DT
9.2.1.1.7 APD Pin Divider Network, R , R
APD1 APD2
The APD pin can be used to disable the TPS23730 device internal hotswap MOSFET giving the adapter source
priority over the PoE source. An example calculation is provided, see SLVA306.
9.2.1.1.8 PPD Pin Divider Network, R , R
PPD1 PPD2
For this design example, passive PoE is not required so PPD is pulled down to VSS. However, the PPD pin
can be used to override the internal hotswap MOSFET UVLO (V and V ) when using low voltage
UVLO_R UVLO_H
adapters connected between V and V . The PPD pin has an internal 5-uA pulldown current source. As an
DD SS
example, consider the choice of R and R , for a 24-V adapter.
PPD1 PPD2
1. Select the start-up voltage, V approximately 75% of nominal for a 24-V adapter. Assuming that the
ADPTR-ON
adapter output is 24 V +/- 10%, this provides 15% margin below the minimum adapter operating voltage.
2. Choose V = 24 V x 0.75 = 18 V.
ADPTR-ON
3. Choose R = 3.01 kOhm.
PPD2
4. I = I + 5 uA so R can be calculated using KCL. Choose 18.7 kOhm.
RPPD1 RPPD2 PPD1
9.2.1.1.9 Setting Frequency (R ) and Synchronization
FRS
The converter switching frequency is set by connecting R from the FRS pin to AGND.
FRS
As an example:
1. Optimal switching frequency (f ) for isolated PoE applications is 250 kHz.
SW
2. Compute R per Equation 2.
FRS
3. Select 60.4 kOhm.
The TPS23730 device may be synchronized to an external clock to eliminate beat frequencies from a sampled
system, or to place emission spectrum away from an RF input frequency. Synchronization may be accomplished
by applying a short pulse (T ) of magnitude V to FRS as shown in Figure 8-3. R should be
SYNC SYNC FRS
chosen so that the maximum free-running frequency is just below the desired synchronization frequency. The
synchronization pulse terminates the potential on-time period, and the off-time period does not begin until the
pulse terminates. The pulse at the FRS pin should reach between 2.5 V and V , with a minimum width of 25 ns
B
(above 2.5 V) and rise and fall times less than 10 ns. The FRS node should be protected from noise because it
is high-impedance. An R on the order of 100 Ohm in the isolated example reduces noise sensitivity and jitter.
T
46 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS23730
```

### Page 47

#### Raw extracted text

```text
TPS23730
www.ti.com SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020
9.2.1.1.10 Bias Supply Requirements and C
VCC
Advanced startup in the TPS23730 allows for relatively low capacitance on the bias circuit. It is recommended to
use a 1-uF 10% 25-V ceramic capacitor on C .
VCC
9.2.1.1.11 TPH, TPL, and BT Interface
The TPH, TPL and BT pins are active low, open-drain outputs which give an indication about the PSE
allocated power. Optocouplers can interface these pins to circuitry on the secondary side of the converter. A
high-gain optocoupler and a high-impedance (for example, CMOS) receiver are recommended. Please see the
TPS23730EVM-093 as an example circuit. Below is an example design calculation.
1. Let V = 12-V, V = 5-V, R = 10-kOhm, V (low) = 400-mV maximum.
CC OUT TPx-OUT TPx-OUT
a. I = 0.46 mA.
TPx-OUT
2. The optocoupler CTR will be needed to determine R . A device with a minimum CTR of 300% at 5-mA
Tpx
LED bias current is selected. CTR will also vary with temperature and LED bias current. The strong variation
of CTR with diode current makes this a problem that requires some iteration using the CTR versus I
DIODE
curve on the optocoupler data sheet.
a. The approximate forward voltage of the optocoupler diode is 1.1 V from the data sheet.
b. I = 1 mA and R = 10.6 kOhm.
TPx-MIN TPx
3. Select 10.7-kOhm resistor.
9.2.1.1.12 Secondary Soft Start
Converters require a soft start on the voltage error amplifier to prevent output overshoot on start-up. Figure
9-2 shows a common implementation of a secondary-side soft start that works with the typical TLV431 error
amplifier. The soft-start components consist of D , R , and C . They serve to control the output rate-of-rise
SS SS SS
by pulling V down as C charges through R , the optocoupler, and D . This has the added advantage
COMP SS OB SS
that the TLV431 output and C are preset to the proper value as the output voltage reaches the regulated
IZ
value, preventing voltage overshoot due to the error amplifier recovery. The secondary-side error amplifier will
not become active until there is sufficient voltage on the secondary. The TPS23730 provides an adjustable
primary-side soft start, which persists long enough for secondary side voltage-loop soft start to take over. The
primary-side current-loop soft start controls the switching MOSFET peak current by applying a slowly rising
ramp voltage to a second PWM control input. The PWM is controlled by the lower of the soft-start ramp or the
COMP-derived current demand. The actual output voltage rise time is usually much shorter than the internal
soft-start period. Initially the primary soft-start ramp limits the maximum current demand as a function of time.
Either the current limit, secondary-side soft start, or output regulation assume control of the PWM before the
primary soft-start period is over. Since the VCC startup source stays on longer after converter's output voltage
is ramped up (VCC startup turns off only when 2.1 V is reached on the SS pin), a large bias winding hold up
capacitor is not necessary like in some traditional PWM controllers. Instead, this allows for a small 1-uF ceramic
capacitor to be used on VCC.
From Regulated
Output Voltage
R
R OB
SS
R
FBU
C
IZ
D
SS
C
SS R
FBL
TLV431
Figure 9-2. Error Amplifier Soft Start
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 47
Product Folder Links: TPS23730
```

### Page 48

#### Raw extracted text

```text
TPS23730
SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020 www.ti.com
9.2.1.1.13 Frequency Dithering for Conducted Emissions Control
For optimum EMI performance, C and R should be calculated as described in DTHR and Frequency
DTR DTR
Dithering for Spread Spectrum Applications.
These equations yield C = 2.2 nF and R = 235 kOhm where a 237-kOhm standard resistor can be used.
DTR DTR
48 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS23730
```

### Page 49

#### Raw extracted text

```text
10 Power Supply Recommendations
The TPS23730 converter must be designed such that the input voltage of the converter is capable of operating
within the IEEE 802.3 protocol at the recommended input voltage as shown in Table 8-4 and the minimum
operating voltage of the adapter if applicable.
www.ti.com
TPS23730
SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 49
Product Folder Links: TPS23730
```

### Page 50

#### Raw extracted text

```text
11 Layout
11.1 Layout Guidelines
The layout of the PoE front end should follow power and EMI/ESD best practice guidelines. A basic set of
recommendations include:
* Parts placement must be driven by power flow in a point-to-point manner; RJ-45, Ethernet transformer, diode
bridges, TVS and 0.1-uF capacitor, and TPS23730.
* All leads should be as short as possible with wide power traces and paired signal and return.
* There should not be any crossovers of signals from one part of the flow to another.
* Spacing consistent with safety standards like IEC60950 must be observed between the 48-V input voltage
rails and between the input and an isolated converter output.
* The TPS23730 should be located over split, local ground planes referenced to VSS for the PoE input and to
RTN for the switched output.
* Large copper fills and traces should be used on SMT power-dissipating devices, and wide traces or overlay
copper fills should be used in the power path.
* It is recommended having at least 8 vias (PAD_G) and 5 vias on (PAD_S) connecting the exposed
thermal pad through a top layer plane (2-oz. copper recommended) to a bottom VSS plane (2-oz. copper
recommended) to help with thermal dissipation.
11.2 Layout Example
A detailed PCB layout can be found in the users guide of the TPS23730EVM-093 that show the top and bottom
layer and assemblies as a reference for optimum parts placement.
11.3 EMI Containment
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
11.4 Thermal Considerations and OTSD
Sources of nearby local PCB heating should be considered during the thermal design. Typical calculations
assume that the TPS23730 is the only heat source contributing to the PCB temperature rise. It is possible for
a normally operating TPS23730 device to experience an OTSD event if it is excessively heated by a nearby
device.
11.5 ESD
ESD requirements for a unit that incorporates the TPS23730 have a much broader scope and operational
implications than are used in TIs testing. Unit-level requirements should not be confused with reference design
testing that only validates the ruggedness of the TPS23730.
TPS23730
SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020 www.ti.com
50 Submit Document Feedback Copyright  2022 Texas Instruments Incorporated
Product Folder Links: TPS23730
```

### Page 51

#### Raw extracted text

```text
12 Device and Documentation Support
12.1 Documentation Support
12.1.1 Related Documentation
For related documentation, see the following:
* IEEE Standard for Information Technology ... Part 3: Carrier sense multiple access with collision detection
(CSMA/CD) access method and physical layer specifications, IEEE Computer Society, IEEE 802.3(TM)at
(Clause 33)
* Information technology equipment - Radio disturbance characteristics - Limits and methods of
measurement, International Electrotechnical Commission, CISPR 22 Edition 5.2, 2006-03
* Advanced Adapter ORing Solutions using the TPS23753, Eric Wright, TI, SLVA306
* Practical Guidelines to Designing an EMI-Compliant PoE Powered Device With Isolated Flyback, Donald V.
Comiskey, TI, SLUA469
* TPS23730EVM-093: Evaluation Module for TPS23730
12.2 Support Resources
TI E2E (TM) support forums  are an engineer's go-to source for fast, verified answers and design help - straight
from the experts. Search existing answers or ask your own question to get the quick design help you need.
Linked content is provided "AS IS" by the respective contributors. They do not constitute TI specifications and do
not necessarily reflect TI's views; see TI's Terms of Use.
12.3 Trademarks
TI E2E(TM) is a trademark of Texas Instruments.
All trademarks are the property of their respective owners.
12.4 Electrostatic Discharge Caution
This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled
with appropriate precautions. Failure to observe proper handling and installation procedures can cause damage.
ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may
be more susceptible to damage because very small parametric changes could cause the device not to meet its published
specifications.
12.5 Glossary
TI Glossary This glossary lists and explains terms, acronyms, and definitions.
13 Mechanical, Packaging, and Orderable Information
The following pages include mechanical, packaging, and orderable information. This information is the most
current data available for the designated devices. This data is subject to change without notice and revision of
this document. For browser-based versions of this data sheet, refer to the left-hand navigation.
www.ti.com
TPS23730
SLVSER6B - MAY 2020 - REVISED NOVEMBER 2020
Copyright  2022 Texas Instruments Incorporated Submit Document Feedback 51
Product Folder Links: TPS23730
```

### Page 52

#### Extracted tables

Table 1:

```text
Orderable part number | Status (1) | Material type (2) | Package | Pins | Package qty | Carrier | RoHS (3) | Lead finish/ Ball material (4) | MSL rating/ Peak reflow (5) | Op temp ( deg C) | Part marking (6)
TPS23730RMTR | Active | Production | VQFN (RMT) | 45 | 3000 | LARGE T&R | Yes | NIPDAU | Level-3-260C-168 HR | 40 to 125 | TPS23730 DB0 WA1
TPS23730RMTR.A | Active | Production | VQFN (RMT) | 45 | 3000 | LARGE T&R | Yes | NIPDAU | Level-3-260C-168 HR | 40 to 125 | TPS23730 DB0 WA1
TPS23730RMTRG4 | Active | Production | VQFN (RMT) | 45 | 3000 | LARGE T&R | Yes | NIPDAU | Level-3-260C-168 HR | 40 to 125 | TPS23730 DB0 WA1
TPS23730RMTRG4.A | Active | Production | VQFN (RMT) | 45 | 3000 | LARGE T&R | Yes | NIPDAU | Level-3-260C-168 HR | 40 to 125 | TPS23730 DB0 WA1
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
TPS23730RMTR Active Production VQFN (RMT) | 45 3000 | LARGE T&R Yes NIPDAU Level-3-260C-168 HR -40 to 125 TPS23730
DB0 WA1
TPS23730RMTR.A Active Production VQFN (RMT) | 45 3000 | LARGE T&R Yes NIPDAU Level-3-260C-168 HR -40 to 125 TPS23730
DB0 WA1
TPS23730RMTRG4 Active Production VQFN (RMT) | 45 3000 | LARGE T&R Yes NIPDAU Level-3-260C-168 HR -40 to 125 TPS23730
DB0 WA1
TPS23730RMTRG4.A Active Production VQFN (RMT) | 45 3000 | LARGE T&R Yes NIPDAU Level-3-260C-168 HR -40 to 125 TPS23730
DB0 WA1

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

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.
Addendum-Page 1
```

### Page 53

#### Raw extracted text

```text
PACKAGE OPTION ADDENDUM
www.ti.com 6-Feb-2026

Addendum-Page 2
```

### Page 54

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
TPS23730RMTR | VQFN | RMT | 45 | 3000 | 330.0 | 16.4 | 5.25 | 7.25 | 1.45 | 8.0 | 16.0 | Q1
TPS23730RMTRG4 | VQFN | RMT | 45 | 3000 | 330.0 | 16.4 | 5.25 | 7.25 | 1.45 | 8.0 | 16.0 | Q1
```

#### Raw extracted text

```text
PACKAGE MATERIALS INFORMATION
www.ti.com 18-Jun-2025
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
TPS23730RMTR VQFN RMT 45 3000 330.0 16.4 5.25 7.25 1.45 8.0 16.0 Q1
TPS23730RMTRG4 VQFN RMT 45 3000 330.0 16.4 5.25 7.25 1.45 8.0 16.0 Q1
Pack Materials-Page 1
```

### Page 55

#### Extracted tables

Table 1:

```text
| H
```

Table 2:

```text
Device | Package Type | Package Drawing | Pins | SPQ | Length (mm) | Width (mm) | Height (mm)
TPS23730RMTR | VQFN | RMT | 45 | 3000 | 367.0 | 367.0 | 35.0
TPS23730RMTRG4 | VQFN | RMT | 45 | 3000 | 367.0 | 367.0 | 35.0
```

#### Raw extracted text

```text
PACKAGE MATERIALS INFORMATION

www.ti.com 18-Jun-2025
TAPE AND REEL BOX DIMENSIONS
Width (mm)
W LH

*All dimensions are nominal
Device Package Type Package Drawing Pins SPQ Length (mm) Width (mm) Height (mm)
TPS23730RMTR VQFN RMT 45 3000 367.0 367.0 35.0
TPS23730RMTRG4 VQFN RMT 45 3000 367.0 367.0 35.0
Pack Materials-Page 2
```

### Page 56

#### Extracted tables

Table 1:

```text
| 0.08 | C
```

Table 2:

```text
|  | 47 | 
 |  | 47 | 
 |  | 46 | 
 |  | 46 |
```

Table 3:

```text
0 | .1 | C |  | A | B
0 | .05 |  | C |  |
```

#### Raw extracted text

```text
NOTES:
1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. The package thermal pad must be soldered to the printed circuit board for optimal thermal and mechanical performance.
PACKAGE OUTLINE
4225180/A   08/2019
www.ti.com
VQFN - 1 mm max height
PLASTIC QUAD FLATPACK-NO LEAD
RMT0045A
A
0.08 C
0.1 C A B
0.05 C
B
PKG
PKG
PIN 1 INDEX AREA
5.1
4.9
7.1
6.9
1 MAX
0.05
0.00
SEATING PLANE
C
(0.1) TYP
2X
5.2
3.6
39X 0.4
45X 0.25
0.15
45X 0.5
0.3
2.9+/-0.1
2.15+/-0.1
2.1+/-0.1
3.7+/-0.1
1.3751
1.4
0.6
1.4
0.2
0.6
1.4
1
9
10
13
35
30
29
23
14 22
3645
46
47
PIN 1 ID
(OPTIONAL)
```

### Page 57

#### Extracted tables

Table 1:

```text
| 46 |  |  |  |  |  |
```

Table 2:

```text
|  | 47 |  |  |  |
```

#### Raw extracted text

```text
NOTES: (continued)
4. This package is designed to be soldered to a thermal pad on the board. For more information, see Texas Instruments literature
number SLUA271 (www.ti.com/lit/slua271).
5. Vias are optional depending on application, refer to device data sheet. If any vias are implemented, refer to their locations shown
          on this view. It is recommended that vias under paste be filled, plugged or tented.
EXAMPLE BOARD LAYOUT
4225180/A   08/2019
www.ti.com
VQFN - 1 mm max heightRMT0045A
PLASTIC QUAD FLATPACK-NO LEAD
PKG
PKG
LAND PATTERN EXAMPLE
EXPOSED METAL SHOWN
SCALE: 12X
SOLDER MASK
DEFINED
SOLDER MASK
OPENING
EXPOSED METAL
METAL UNDER
SOLDER MASK
0.05 MIN
ALL AROUND
NON- SOLDER MASK
DEFINED
(PREFERRED)
EXPOSED METAL SOLDER MASK
OPENING
METAL
0.05 MAX
ALL AROUND
SOLDER MASK DETAILS
(3.7)
(2.9)
(2.1)
(2.15)
(3.6)
(4.8)
(6.8) (5.2)
(0.6)
39X (0.4)
(1.4)
(1.4)
(0.2)
(0.595)
(1.4)
(2.205)
(0.55)
(1.375)
(2.2)
(1.2)
(0.625)
(1.6)
45X (0.2)
45X (0.6)
1
9
10
13
35
30
29
23
14 22
3645
46
47
(R0.05)
TYP
(0.2) VIA
TYP
```

### Page 58

#### Extracted tables

Table 1:

```text
|  | 47 |  |  |  |
```

#### Raw extracted text

```text
NOTES: (continued)
6.  Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
design recommendations.
EXAMPLE STENCIL DESIGN
4225180/A   08/2019
www.ti.com
VQFN - 1 mm max heightRMT0045A
PLASTIC QUAD FLATPACK-NO LEAD
SOLDER PASTE EXAMPLE
BASED ON 0.125 mm THICK STENCIL
PAD 46: 76%; PAD 47: 78%
SCALE: 12X
PKG
PKG
4X (1.27)
6X (0.94)
(3.6)
(4.8)
(6.8) (5.2)
(0.6)
39X (0.4)
(1.4)
(1.4)
(0.2)
(0.83)
(1.97)
(0.795)
(1.955)
(0.735)
(1.25)
45X (0.2)
45X (0.6)
1
9
10
13
35
30
29
23
14 22
3645
46
47
(R0.05)
TYP
METAL TYP
4X (0.96)
6X (1.05)
```

### Page 59

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
