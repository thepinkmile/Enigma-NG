# LMQ61460-Q1 Automotive 3-V to 36-V, 6 A, Low EMI Synchronous Step-Down - Data Sheet

## Source Reference

- Source PDF: [lmq61460-q1-datasheet.pdf](lmq61460-q1-datasheet.pdf)
- Source path: `design\Datasheets\lmq61460-q1-datasheet.pdf`
- Generated markdown: `lmq61460-q1-datasheet.md`
- Page count: 57
- Extracted text characters: 118390
- Empty extraction pages: none
- Conversion method: automated local PDF text extraction with pypdf and pdfplumber

## Title and Part Identity

- Extracted title: LMQ61460-Q1 Automotive 3-V to 36-V, 6 A, Low EMI Synchronous Step-Down - Data
  Sheet
- File stem / likely part identity: `lmq61460-q1-datasheet`
- PDF metadata title: LMQ61460-Q1 Automotive 3-V to 36-V, 6 A, Low EMI Synchronous Step-Down
  Converter datasheet (Rev. C)
- PDF metadata subject: Data Sheet
- Identity clue: LMQ61460-Q1 Automotive 3-V to 36-V, 6 A, Low EMI Synchronous Step-Down
- Identity clue: Converter
- Identity clue: 1 Features
- Identity clue: AEC-Q100 qualified for automotive applications
- Identity clue: Temperature grade 1: -40 degC to +150 degC, T J
- Identity clue: Functional Safety-Capable
- Identity clue: Documentation available to aid functional safety
- Identity clue: system design

## PDF Metadata

| Field | Value |
|:---|:---|
| Title | LMQ61460-Q1 Automotive 3-V to 36-V, 6 A, Low EMI Synchronous Step-Down Converter datasheet (Rev. C) |
| Author | Texas Instruments, Incorporated [SNVSBP4,C
] |
| Subject | Data Sheet |
| Creator | AH XSL Formatter V6.5 MR1 for Windows (x64) : 6.5.4.31003 (2017/10/23 10:30JST) |
| Producer | iText 2.1.7 by 1T3XT |

## Design-Relevant Extracted Content

These sections collect extracted snippets that are likely useful during design work, then the raw page-by-page text is preserved below for local search.

### Part number and ordering information

- Page 1: - 7-uA no load current at 13.5 V IN, 3.3 VOUT / - 90% PFM efficiency at 1-mA, 13.5 V IN, 5
  VOUT / - External bias option for improved efficiency / - Pin compatible with: / - LM61460-Q1 (36
  V, 6 A)
- Page 1: resistances and an external bias input, ensures / exceptional efficiency across the entire
  load range. / Device Information / PART NUMBER PACKAGE / (1)
- Page 1: exceptional efficiency across the entire load range. / Device Information / PART NUMBER
  PACKAGE / (1) / BODY SIZE (NOM)
- Page 1: BODY SIZE (NOM) / LMQ61460-Q1 VQFN-HR (14) 4.00 mm  x  3.50 mm / (1) For all available
  packages, see the orderable addendum at / the end of the data sheet. / Conducted EMI: VOUT = 5 V,
  IOUT = 4 A
- Page 2: 13.5 Electrostatic Discharge Caution..............................49 / 13.6
  Glossary..................................................................49 / 14 Mechanical,
  Packaging, and Orderable /
  Information.................................................................... 49 / 4 Revision
  History
- Page 2: Documentation. / 6 Device Comparison Table / DEVICE ORDERABLE PART / NUMBER / REFERENCE
  PART
- Page 3: NAME NO. / BIAS 1 P / Input to internal LDO. Connect to output voltage point to improve
  efficiency. Connect an optional high-quality / 0.1-uF to 1-uF capacitor from this pin to ground
  for improved noise immunity. If output voltage is above 12 V, / connect this pin to ground.
- Page 3: FB 4 I / Output voltage feedback input to the internal control loop. Connect to output
  voltage sense point for fixed 3.3 / V or 5 V output voltage factory options. Connect to feedback
  divider tap point for adjustable output voltage. / Do not float or connect to ground. / PGOOD 5 O
- Page 18: rate also decreases the efficiency. / 9.3.9 Spread Spectrum / Spread spectrum is a
  factory option. To find which devices have spread spectrum enabled, see Section 6. The / purpose
  of spread spectrum is to eliminate peak emissions at specific frequencies by spreading these
  emissions / across a wider range of frequencies rather than a part with fixed frequency operation.
  In most systems
- Page 24: seamless transition between normal current mode operation while heavily loaded and highly
  efficient light load / operation. The other behavior, called FPWM Mode, maintains full frequency
  even when unloaded. Which mode / the device operates in depends on which factory option is
  employed, see Section 6. Note that all parts operate in / FPWM mode when synchronizing frequency
  to an external signal. / In auto mode, light load operation is employed in the device at load
  lower than approximately a tenth of the rated
- Page 26: 9.4.3.3 FPWM Mode - Light Load Operation / Like auto mode operation, FPWM mode operation
  during light load operation is selected as a factory option. / In FPWM Mode, frequency is
  maintained while lightly loaded. To maintain frequency, a limited reverse current is / allowed to
  flow through the inductor. Reverse current is limited by reverse current limit circuitry, see
  Section 8.5
- Page 49: 13.6 Glossary / TI Glossary This glossary lists and explains terms, acronyms, and
  definitions. / 14 Mechanical, Packaging, and Orderable Information / The following pages include
  mechanical, packaging, and orderable information. This information is the most / current data
  available for the designated devices. This data is subject to change without notice and revision
  of
- Page 49: TI Glossary This glossary lists and explains terms, acronyms, and definitions. / 14
  Mechanical, Packaging, and Orderable Information / The following pages include mechanical,
  packaging, and orderable information. This information is the most / current data available for
  the designated devices. This data is subject to change without notice and revision of / this
  document. For browser-based versions of this data sheet, refer to the left-hand navigation.
- Page 50: PACKAGE OPTION ADDENDUM / www.ti.com 9-Nov-2025 / PACKAGING INFORMATION
- Page 50: www.ti.com 9-Nov-2025 / PACKAGING INFORMATION / Orderable part number Status / (1) /
  Material type
- Page 50: Peak reflow / (5) / Op temp ( degC) Part marking / (6) / LMQ61460AASQRJRRQ1 Active
  Production VQFN-HR (RJR) | 14 3000 | LARGE T&R Yes SN Level-2-260C-1 YEAR -40 to 150 Q6146Q

### Pin, pad, and connection designations

- Page 1: - Adjustable switch node rise time / - Designed for rugged automotive applications / -
  Supports 42-V load dump / - 0.4-V dropout with 4-A load (typical) / - High efficiency power
  conversion at all loads
- Page 1: - 90% PFM efficiency at 1-mA, 13.5 V IN, 5 VOUT / - External bias option for improved
  efficiency / - Pin compatible with: / - LM61460-Q1 (36 V, 6 A) / 2 Applications
- Page 1: MOSFETs, up to 6 A of output current is delivered / over a wide input range of 3.0 V to 36
  V; 42-V / tolerance supports load dump for durations of 400 ms. / The device implements soft
  recovery from dropout / eliminating overshoot on the output.
- Page 1: SW node rise time, low-EMI VQFN-HR package / featuring low switch node ringing, and
  optimized / pinout for ease of use. The switching frequency can / be synchronized between 200 kHz
  and 2.2 MHz to / avoid noise sensitive frequency bands. In addition the
- Page 1: LMQ61460-Q1 / SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021 / An IMPORTANT NOTICE at the
  end of this data sheet addresses availability, warranty, changes, use in safety-critical
  applications, / intellectual property matters and other important disclaimers. PRODUCTION DATA.
- Page 1: SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021 / An IMPORTANT NOTICE at the end of this data
  sheet addresses availability, warranty, changes, use in safety-critical applications, /
  intellectual property matters and other important disclaimers. PRODUCTION DATA.
- Page 2: 5 Description (continued).................................................. 2 / 6 Device
  Comparison Table...............................................2 / 7 Pin Configuration and
  Functions...................................3 / 8
  Specifications.................................................................. 4 / 8.1 Absolute
  Maximum Ratings ....................................... 4
- Page 2: 12.1 Layout Guidelines................................................... 46 / 12.2 Layout
  Example...................................................... 48 / 13 Device and Documentation
  Support..........................49 / 13.1 Documentation
  Support.......................................... 49 / 13.2 Receiving Notification of
  Documentation Updates..49
- Page 2: 12.2 Layout Example...................................................... 48 / 13 Device
  and Documentation Support..........................49 / 13.1 Documentation
  Support.......................................... 49 / 13.2 Receiving Notification of
  Documentation Updates..49 / 13.3 Support
  Resources................................................. 49
- Page 2: 13.1 Documentation Support.......................................... 49 / 13.2 Receiving
  Notification of Documentation Updates..49 / 13.3 Support
  Resources................................................. 49 / 13.4
  Trademarks.............................................................49 / 13.5 Electrostatic
  Discharge Caution..............................49
- Page 2: - Updated the numbering format for tables, figures and cross-references throughout the
  document................... 1 / 5 Description (continued) / The device is available in a 14-pin
  VQFN-HR package with wettable flanks. Electrical characteristics are / specified over a junction
  temperature range of -40 degC to +150 degC. Find additional resources in the Related /
  Documentation.
- Page 3: 7 Pin Configuration and Functions / BIAS / CBOOT
- Page 3: 14 / PGOOD / Figure 7-1. RJR Package 14-Pin VQFN-HR Top View / Table 7-1. Pin Functions /
  PIN
- Page 3: PGOOD / Figure 7-1. RJR Package 14-Pin VQFN-HR Top View / Table 7-1. Pin Functions / PIN /
  I/O DESCRIPTION
- Page 3: Figure 7-1. RJR Package 14-Pin VQFN-HR Top View / Table 7-1. Pin Functions / PIN / I/O
  DESCRIPTION / NAME NO.
- Page 3: BIAS 1 P / Input to internal LDO. Connect to output voltage point to improve efficiency.
  Connect an optional high-quality / 0.1-uF to 1-uF capacitor from this pin to ground for improved
  noise immunity. If output voltage is above 12 V, / connect this pin to ground. / VCC 2 O Internal
  LDO output. Used as supply to internal control circuits. Do not connect to any external loads.

### Specifications, ratings, and operating conditions

- Page 1: - 0.4-V dropout with 4-A load (typical) / - High efficiency power conversion at all loads
  / - 7-uA no load current at 13.5 V IN, 3.3 VOUT / - 90% PFM efficiency at 1-mA, 13.5 V IN, 5 VOUT
  / - External bias option for improved efficiency
- Page 1: synchronous buck converter with integrated bypass / capacitors. With integrated high-side
  and low-side / MOSFETs, up to 6 A of output current is delivered / over a wide input range of 3.0
  V to 36 V; 42-V / tolerance supports load dump for durations of 400 ms.
- Page 1: MOSFETs, up to 6 A of output current is delivered / over a wide input range of 3.0 V to 36
  V; 42-V / tolerance supports load dump for durations of 400 ms. / The device implements soft
  recovery from dropout / eliminating overshoot on the output.
- Page 1: high operating frequency. / Auto-mode enables frequency foldback when / operating at light
  loads, allowing an unloaded current / consumption of only 7 uA (typical) and high light load /
  efficiency. Seamless transition between PWM and
- Page 1: the end of the data sheet. / Conducted EMI: VOUT = 5 V, IOUT = 4 A / Load Current (A) /
  Efficiency (%) / 0.0001 0.001 0.01 0.1 0.2 0.5 1 2 3 5 710
- Page 2: 6 Device Comparison Table...............................................2 / 7 Pin
  Configuration and Functions...................................3 / 8
  Specifications.................................................................. 4 / 8.1 Absolute
  Maximum Ratings ....................................... 4 / 8.2 ESD Ratings
  .............................................................. 4
- Page 2: 7 Pin Configuration and Functions...................................3 / 8
  Specifications.................................................................. 4 / 8.1 Absolute
  Maximum Ratings ....................................... 4 / 8.2 ESD Ratings
  .............................................................. 4 / 8.3 Recommended Operating
  Conditions ........................5
- Page 2: 8 Specifications.................................................................. 4 / 8.1
  Absolute Maximum Ratings ....................................... 4 / 8.2 ESD Ratings
  .............................................................. 4 / 8.3 Recommended Operating
  Conditions ........................5 / 8.4 Thermal Information
  ...................................................5
- Page 2: 8.1 Absolute Maximum Ratings ....................................... 4 / 8.2 ESD Ratings
  .............................................................. 4 / 8.3 Recommended Operating
  Conditions ........................5 / 8.4 Thermal Information
  ...................................................5 / 8.5 Electrical Characteristics
  ............................................5
- Page 2: 8.2 ESD Ratings .............................................................. 4 / 8.3
  Recommended Operating Conditions ........................5 / 8.4 Thermal Information
  ...................................................5 / 8.5 Electrical Characteristics
  ............................................5 / 8.6 Timing Characteristics
  ................................................7
- Page 2: 8.3 Recommended Operating Conditions ........................5 / 8.4 Thermal Information
  ...................................................5 / 8.5 Electrical Characteristics
  ............................................5 / 8.6 Timing Characteristics
  ................................................7 / 8.7 Systems Characteristics
  ............................................ 8
- Page 2: 8.4 Thermal Information ...................................................5 / 8.5
  Electrical Characteristics ............................................5 / 8.6 Timing
  Characteristics ................................................7 / 8.7 Systems Characteristics
  ............................................ 8 / 8.8 Typical
  Characteristics..............................................10
- Page 2: Information.................................................................... 49 / 4
  Revision History / NOTE: Page numbers for previous revisions may differ from page numbers in the
  current version. / Changes from Revision B (September 2020) to Revision C (January 2021) Page / -
  Changed front-page efficiency curve from 2.1 MHz to 400
  kHz......................................................................... 1
- Page 2: - Updated the numbering format for tables, figures and cross-references throughout the
  document................... 1 / 5 Description (continued) / The device is available in a 14-pin
  VQFN-HR package with wettable flanks. Electrical characteristics are / specified over a junction
  temperature range of -40 degC to +150 degC. Find additional resources in the Related /
  Documentation.
- Page 2: SPECTRUM / OUTPUT / VOLTAGE / SWITCHING / FREQUENCY
- Page 3: NAME NO. / BIAS 1 P / Input to internal LDO. Connect to output voltage point to improve
  efficiency. Connect an optional high-quality / 0.1-uF to 1-uF capacitor from this pin to ground
  for improved noise immunity. If output voltage is above 12 V, / connect this pin to ground.

### Dimensions, package, and mechanical information

- Page 1: - Optimized for ultra-low EMI requirements / - Meets CISPR25 class 5 standard / - Hotrod
  (TM) package minimizes switch node / ringing / - Internal bypass capacitors reduce EMI
- Page 1: The device incorporates pseudo-random spread / spectrum, integrated bypass capacitors,
  adjustable / SW node rise time, low-EMI VQFN-HR package / featuring low switch node ringing, and
  optimized / pinout for ease of use. The switching frequency can
- Page 1: exceptional efficiency across the entire load range. / Device Information / PART NUMBER
  PACKAGE / (1) / BODY SIZE (NOM)
- Page 1: PART NUMBER PACKAGE / (1) / BODY SIZE (NOM) / LMQ61460-Q1 VQFN-HR (14) 4.00 mm  x  3.50 mm
  / (1) For all available packages, see the orderable addendum at
- Page 1: BODY SIZE (NOM) / LMQ61460-Q1 VQFN-HR (14) 4.00 mm  x  3.50 mm / (1) For all available
  packages, see the orderable addendum at / the end of the data sheet. / Conducted EMI: VOUT = 5 V,
  IOUT = 4 A
- Page 2: 13.5 Electrostatic Discharge Caution..............................49 / 13.6
  Glossary..................................................................49 / 14 Mechanical,
  Packaging, and Orderable /
  Information.................................................................... 49 / 4 Revision
  History
- Page 2: - Updated the numbering format for tables, figures and cross-references throughout the
  document................... 1 / 5 Description (continued) / The device is available in a 14-pin
  VQFN-HR package with wettable flanks. Electrical characteristics are / specified over a junction
  temperature range of -40 degC to +150 degC. Find additional resources in the Related /
  Documentation.
- Page 3: 14 / PGOOD / Figure 7-1. RJR Package 14-Pin VQFN-HR Top View / Table 7-1. Pin Functions /
  PIN
- Page 5: (4) High junction temperatures degrade operating lifetimes.  Operating lifetime is
  de-rated for junction temperatures greater than 125 C. / 8.4 Thermal Information / The value of
  RJA given in this table is only valid for comparison with other packages and cannot be used for
  design / purposes. These values were calculated in accordance with JESD 51-7, and simulated on a
  4-layer JEDEC board. They do / not represent the performance obtained in an actual application.
  For example, with a 4-layer PCB, a RJA = 25C/W can be
- Page 5: JB Junction-to-board characterization parameter 19  degC/W / RJC(bot) Junction-to-case
  (bottom) thermal resistance -  degC/W / (1) For more information about traditional and new thermal
  metrics, see the Semiconductor and IC Package Thermal Metrics application / report. / (2) The
  value of R JA given in this table is only valid for comparison with other packages and cannot be
  used for design purposes. These
- Page 5: (1) For more information about traditional and new thermal metrics, see the Semiconductor
  and IC Package Thermal Metrics application / report. / (2) The value of R JA given in this table
  is only valid for comparison with other packages and cannot be used for design purposes. These /
  values were calculated in accordance with JESD 51-7, and simulated on a 4-layer JEDEC board. They
  do not represent the / performance obtained in an actual application.
- Page 12: The device has been designed for low EMI and is optimized for both above and below AM
  band operation: / - Meets CISPR25 class 5 standard / - Hotrod (TM) package minimizes switch node
  ringing / - Parallel input path minimizes parasitic inductance / - Internal bypass capacitors
  reduce EMI
- Page 33: These capacitors also suppress SW node ringing, which reduces the maximum voltage present
  on the SW node / and EMI. The two 100 nF must also be rated at 50 V with an X7R or better
  dielectric. The VQFN-HR (RJR) / package provides two input voltage pins and two power ground pins
  on opposite sides of the package. This / allows the input capacitors to be split, and placed
  optimally with respect to the internal power MOSFETs, thus / improving the effectiveness of the
  input bypassing. In this example, two 4.7- uF and two 100-nF ceramic
- Page 33: improving the effectiveness of the input bypassing. In this example, two 4.7- uF and two
  100-nF ceramic / capacitors are used, one at each VIN/PGND location. A single 10- uF can also be
  used on one side of the / package. / Many times, it is desirable and necessary to use an
  electrolytic capacitor on the input in parallel with the / ceramics. This is especially true if
  long leads or traces are used to connect the input supply to the converter. The
- Page 46: - Place the input capacitor or capacitors as close as possible input pin pairs: VIN1 to
  PGND1 and VIN2 to / PGND2. Each pair of pins are adjacent, simplifying the input capacitor
  placement. With the VQFN-HR / package, there are two VIN/PGND pairs on either side of the package.
  This provides for a symmetrical layout / and helps minimize switching noise and EMI generation.
  Use a wide VIN plane on a lower layer to connect / both of the VIN pairs together to the input
  supply.
- Page 46: layers with two-ounce copper and no less than one ounce. If the PCB design uses multiple
  copper layers / (recommended), thermal vias can also be connected to the inner layer
  heat-spreading ground planes. Note / that the package of this device dissipates heat through all
  pins. Wide traces must be used for all pins except / where noise considerations dictate
  minimization of area. / - Keep switch area small: Keep the copper area connecting the SW pin to
  the inductor as short and wide as

### Formulas, equations, and configurable calculations

- Page 1: MOSFETs, up to 6 A of output current is delivered / over a wide input range of 3.0 V to 36
  V; 42-V / tolerance supports load dump for durations of 400 ms. / The device implements soft
  recovery from dropout / eliminating overshoot on the output.
- Page 2: 5 Description (continued).................................................. 2 / 6 Device
  Comparison Table...............................................2 / 7 Pin Configuration and
  Functions...................................3 / 8
  Specifications.................................................................. 4 / 8.1 Absolute
  Maximum Ratings ....................................... 4
- Page 3: 7 Pin Configuration and Functions / BIAS / CBOOT
- Page 3: EN/SYNC 7 I / Precision enable input. High = on, Low = off. Can be connected to VIN.
  Precision enable allows the pin to be / used as an adjustable UVLO. See Section 10. Do not float.
  EN/SYNC also functions as a synchronization / input pin. Used to synchronize the device switching
  frequency to a system clock. Triggers on rising edge of / external clock. A capacitor can be used
  to AC couple the synchronization signal to this pin. When
- Page 4: Tstg Storage temperature -40 150  degC / (1) Stresses beyond those listed under Absolute
  Maximum Ratings may cause permanent damage to the device. These are stress ratings / only, which
  do not imply functional operation of the device at these or any other conditions beyond those
  indicated under / Recommended Operating Conditions. Exposure to absolute-maximum-rated conditions
  for extended periods may affect device / reliability.
- Page 4: reliability. / (2) A voltage of 2 V below GND and 2 V above V IN can appear on this pin
  for <= 200 ns with a duty cycle of <= 0.01%. / (3) This specification applies to voltage durations
  of 100 ns or less.  The maximum D.C. voltage should not exceed +/- 0.3 V. / (4) Do not exceed the
  voltage rating of the pin. / 8.2 ESD Ratings
- Page 5: 8.4 Thermal Information / The value of RJA given in this table is only valid for
  comparison with other packages and cannot be used for design / purposes. These values were
  calculated in accordance with JESD 51-7, and simulated on a 4-layer JEDEC board. They do / not
  represent the performance obtained in an actual application. For example, with a 4-layer PCB, a
  RJA = 25C/W can be / achieved. For design information see Maximum Ambient Temperature versus
  Output Current.
- Page 5: report. / (2) The value of R JA given in this table is only valid for comparison with
  other packages and cannot be used for design purposes. These / values were calculated in
  accordance with JESD 51-7, and simulated on a 4-layer JEDEC board. They do not represent the /
  performance obtained in an actual application. / 8.5 Electrical Characteristics
- Page 6: LDO - VCC / VCC Internal VCC voltage / VBIAS > 3.4  V, CCM Operation(3) 3.3 / V / VBIAS =
  3.1 V, Non-switching 3.1
- Page 6: V / VBIAS = 3.1 V, Non-switching 3.1 / VCC_UVLO / Internal VCC input under voltage /
  lock-out
- Page 6: VCC rising under voltage / threshold 3.6 V / VCC_UVLO_HYST / Internal VCC input under
  voltage / lock-out Hysteresis below VCC_UVLO 1.1 V
- Page 6: VCC_UVLO_HYST / Internal VCC input under voltage / lock-out Hysteresis below VCC_UVLO 1.1
  V / FEEDBACK / VFB_acc
- Page 6: fS SS / Frequency span of spread / spectrum operation - largest / deviation from center
  frequency / Spread spectrum active 2 %
- Page 6: RDS(ON)_HS Power switch on-resistance High side MOSFET RDS(ON) 41 82 mohm / RDS(ON)_LS
  Power switch on-resistance Low side MOSFET RDS(ON) 21 45 mohm / VBOOT_UVLO / Voltage on CBOOT pin
  compared / to SW which will turn off high-side
- Page 7: SYNC Modes.  Positive current / direction is out of SW pin. / FPWM operation -3 A /
  IPK_MIN_0 / Minimum peak command in Auto
- Page 7: IPK_MIN_0 / Minimum peak command in Auto / Mode / device current rating Pulse duration <
  100 ns 25 % / IPK_MIN_100 / Minimum peak command in Auto

### Reference designs, applications, and examples

- Page 1: Converter / 1 Features / - AEC-Q100 qualified for automotive applications / - Temperature
  grade 1: -40 degC to +150 degC, T J / - Functional Safety-Capable
- Page 1: - Spread spectrum reduces peak emissions / - Adjustable switch node rise time / - Designed
  for rugged automotive applications / - Supports 42-V load dump / - 0.4-V dropout with 4-A load
  (typical)
- Page 1: - Pin compatible with: / - LM61460-Q1 (36 V, 6 A) / 2 Applications / - Automotive
  infotainment and cluster: head unit, / media hub, USB charge, display
- Page 1: LMQ61460-Q1 / SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021 / An IMPORTANT NOTICE at the
  end of this data sheet addresses availability, warranty, changes, use in safety-critical
  applications, / intellectual property matters and other important disclaimers. PRODUCTION DATA.
- Page 2: Table of Contents / 1
  Features............................................................................1 / 2
  Applications.....................................................................1 / 3
  Description.......................................................................1 / 4 Revision
  History.............................................................. 2
- Page 2: 9.3 Feature Description...................................................14 / 9.4 Device
  Functional Modes..........................................23 / 10 Application and
  Implementation................................29 / 10.1 Application
  Information........................................... 29 / 10.2 Typical
  Application..................................................29
- Page 2: 9.4 Device Functional Modes..........................................23 / 10 Application
  and Implementation................................29 / 10.1 Application
  Information........................................... 29 / 10.2 Typical
  Application..................................................29 / 11 Power Supply
  Recommendations..............................45
- Page 2: 10 Application and Implementation................................29 / 10.1 Application
  Information........................................... 29 / 10.2 Typical
  Application..................................................29 / 11 Power Supply
  Recommendations..............................45 / 12
  Layout...........................................................................46
- Page 2: 12 Layout...........................................................................46 /
  12.1 Layout Guidelines................................................... 46 / 12.2 Layout
  Example...................................................... 48 / 13 Device and Documentation
  Support..........................49 / 13.1 Documentation
  Support.......................................... 49
- Page 2: Changes from Revision B (September 2020) to Revision C (January 2021) Page / - Changed
  front-page efficiency curve from 2.1 MHz to 400
  kHz......................................................................... 1 / - Updated the
  Application Curves to reflect 6-A
  trim...........................................................................................35
  / Changes from Revision A (May 2020) to Revision B (September 2020) Page / - Changed device status
  from Advance Information to Production
  Data.............................................................. 1
- Page 5: (2) Under no conditions should the output voltage be allowed to fall below zero volts. /
  (3) Maximum continuous DC current may be derated when operating with high switching frequency,
  high ambient temperature, or both. / See the application section for details. / (4) High junction
  temperatures degrade operating lifetimes.  Operating lifetime is de-rated for junction
  temperatures greater than 125 C. / 8.4 Thermal Information
- Page 5: The value of RJA given in this table is only valid for comparison with other packages and
  cannot be used for design / purposes. These values were calculated in accordance with JESD 51-7,
  and simulated on a 4-layer JEDEC board. They do / not represent the performance obtained in an
  actual application. For example, with a 4-layer PCB, a RJA = 25C/W can be / achieved. For design
  information see Maximum Ambient Temperature versus Output Current. / THERMAL METRIC (1) (2)
- Page 5: JB Junction-to-board characterization parameter 19  degC/W / RJC(bot) Junction-to-case
  (bottom) thermal resistance -  degC/W / (1) For more information about traditional and new thermal
  metrics, see the Semiconductor and IC Package Thermal Metrics application / report. / (2) The
  value of R JA given in this table is only valid for comparison with other packages and cannot be
  used for design purposes. These
- Page 5: (2) The value of R JA given in this table is only valid for comparison with other packages
  and cannot be used for design purposes. These / values were calculated in accordance with JESD
  51-7, and simulated on a 4-layer JEDEC board. They do not represent the / performance obtained in
  an actual application. / 8.5 Electrical Characteristics / Limits apply over the recommended
  operating junction temperature range of -40 degC to +150 degC, unless otherwise stated.
- Page 8: (1) Parameter specified using design, statistical analysis, and production testing of
  correlated parameters; not tested in production. / 8.7 Systems Characteristics / The following
  values are specified by design provided that the component values in the typical application
  circuit are used. / Limits apply over the junction temperature range of -40 degC to +150 degC,
  unless otherwise noted. Minimum and Maximum limits / are derived using test, design or statistical
  correlation. Typical values represent the most likely parametric norm at TJ = 25 degC,
- Page 9: The following values are specified by design provided that the component values in the
  typical application circuit are used. / Limits apply over the junction temperature range of -40
  degC to +150 degC, unless otherwise noted. Minimum and Maximum limits / are derived using test,
  design or statistical correlation. Typical values represent the most likely parametric norm at TJ
  = 25 degC,

## Page-by-Page Extracted Text

### Page 1

```text
LMQ61460-Q1 Automotive 3-V to 36-V, 6 A, Low EMI Synchronous Step-Down
Converter
1 Features
- AEC-Q100 qualified for automotive applications
- Temperature grade 1: -40 degC to +150 degC, T J
- Functional Safety-Capable
- Documentation available to aid functional safety
system design
- Optimized for ultra-low EMI requirements
- Meets CISPR25 class 5 standard
- Hotrod (TM) package minimizes switch node
ringing
- Internal bypass capacitors reduce EMI
- Parallel input path minimizes parasitic
inductance
- Spread spectrum reduces peak emissions
- Adjustable switch node rise time
- Designed for rugged automotive applications
- Supports 42-V load dump
- 0.4-V dropout with 4-A load (typical)
- High efficiency power conversion at all loads
- 7-uA no load current at 13.5 V IN, 3.3 VOUT
- 90% PFM efficiency at 1-mA, 13.5 V IN, 5 VOUT
- External bias option for improved efficiency
- Pin compatible with:
- LM61460-Q1 (36 V, 6 A)
2 Applications
- Automotive infotainment and cluster: head unit,
media hub, USB charge, display
- Automotive ADAS and body electronics
3 Description
The LMQ61460-Q1 is a high-performance, DC-DC
synchronous buck converter with integrated bypass
capacitors. With integrated high-side and low-side
MOSFETs, up to 6 A of output current is delivered
over a wide input range of 3.0 V to 36 V; 42-V
tolerance supports load dump for durations of 400 ms.
The device implements soft recovery from dropout
eliminating overshoot on the output.
The device is specifically designed for minimal EMI.
The device incorporates pseudo-random spread
spectrum, integrated bypass capacitors, adjustable
SW node rise time, low-EMI VQFN-HR package
featuring low switch node ringing, and optimized
pinout for ease of use. The switching frequency can
be synchronized between 200 kHz and 2.2 MHz to
avoid noise sensitive frequency bands. In addition the
frequency can be selected for improved efficiency at
low operating frequency or smaller solution size at
high operating frequency.
Auto-mode enables frequency foldback when
operating at light loads, allowing an unloaded current
consumption of only 7 uA (typical) and high light load
efficiency. Seamless transition between PWM and
PFM modes, along with very low MOSFET ON
resistances and an external bias input, ensures
exceptional efficiency across the entire load range.
Device Information
PART NUMBER PACKAGE
(1)
BODY SIZE (NOM)
LMQ61460-Q1 VQFN-HR (14) 4.00 mm  x  3.50 mm
(1) For all available packages, see the orderable addendum at
the end of the data sheet.
Conducted EMI: VOUT = 5 V, IOUT = 4 A
Load Current (A)
Efficiency (%)
0.0001 0.001 0.01 0.1 0.2 0.5 1 2 3 5 710
60%
65%
70%
75%
80%
85%
90%
95%
100%
LM61
VIN = 8 V
VIN = 13.5 V
VIN = 24 V Efficiency: VOUT = 5 V, FSW = 400 kHz
www.ti.com
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021
Copyright (c) 2021 Texas Instruments Incorporated Submit Document Feedback 1
Product Folder Links: LMQ61460-Q1
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021
An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in
safety-critical applications,
intellectual property matters and other important disclaimers. PRODUCTION DATA.
```

### Page 2

```text
Table of Contents
1 Features............................................................................1
2 Applications.....................................................................1
3 Description.......................................................................1
4 Revision History.............................................................. 2
5 Description (continued).................................................. 2
6 Device Comparison Table...............................................2
7 Pin Configuration and Functions...................................3
8 Specifications.................................................................. 4
8.1 Absolute Maximum Ratings ....................................... 4
8.2 ESD Ratings .............................................................. 4
8.3 Recommended Operating Conditions ........................5
8.4 Thermal Information ...................................................5
8.5 Electrical Characteristics ............................................5
8.6 Timing Characteristics ................................................7
8.7 Systems Characteristics ............................................ 8
8.8 Typical Characteristics..............................................10
9 Detailed Description......................................................12
9.1 Overview...................................................................12
9.2 Functional Block Diagram.........................................13
9.3 Feature Description...................................................14
9.4 Device Functional Modes..........................................23
10 Application and Implementation................................29
10.1 Application Information........................................... 29
10.2 Typical Application..................................................29
11 Power Supply Recommendations..............................45
12 Layout...........................................................................46
12.1 Layout Guidelines................................................... 46
12.2 Layout Example...................................................... 48
13 Device and Documentation Support..........................49
13.1 Documentation Support.......................................... 49
13.2 Receiving Notification of Documentation Updates..49
13.3 Support Resources................................................. 49
13.4 Trademarks.............................................................49
13.5 Electrostatic Discharge Caution..............................49
13.6 Glossary..................................................................49
14 Mechanical, Packaging, and Orderable
Information.................................................................... 49
4 Revision History
NOTE: Page numbers for previous revisions may differ from page numbers in the current version.
Changes from Revision B (September 2020) to Revision C (January 2021) Page
- Changed front-page efficiency curve from 2.1 MHz to 400
kHz......................................................................... 1
- Updated the Application Curves to reflect 6-A
trim...........................................................................................35
Changes from Revision A (May 2020) to Revision B (September 2020) Page
- Changed device status from Advance Information to Production
Data.............................................................. 1
- Updated the numbering format for tables, figures and cross-references throughout the
document................... 1
5 Description (continued)
The device is available in a 14-pin VQFN-HR package with wettable flanks. Electrical characteristics
are
specified over a junction temperature range of -40 degC to +150 degC. Find additional resources in
the Related
Documentation.
6 Device Comparison Table
DEVICE ORDERABLE PART
NUMBER
REFERENCE PART
NUMBER
LIGHT LOAD
MODE
SPREAD
SPECTRUM
OUTPUT
VOLTAGE
SWITCHING
FREQUENCY
LMQ61460-
Q1
LMQ61460AASQRJRRQ1 LMQ61460AAS-Q1 Auto Mode Yes Adjustable Adjustable
LMQ61460AFSQRJRRQ1 LMQ61460AFS-Q1 FPWM Yes Adjustable Adjustable
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021 www.ti.com
2 Submit Document Feedback Copyright (c) 2021 Texas Instruments Incorporated
Product Folder Links: LMQ61460-Q1
```

### Page 3

```text
7 Pin Configuration and Functions
BIAS
CBOOT
RBOOTEN/
SYNC
VIN1 VIN2
PGND1
PGND2
SW
FB
AGND
VCC
RT
1
2
3
4
6
5
7
8
9
10
11
12
13
14
PGOOD
Figure 7-1. RJR Package 14-Pin VQFN-HR Top View
Table 7-1. Pin Functions
PIN
I/O DESCRIPTION
NAME NO.
BIAS 1 P
Input to internal LDO. Connect to output voltage point to improve efficiency. Connect an optional
high-quality
0.1-uF to 1-uF capacitor from this pin to ground for improved noise immunity. If output voltage is
above 12 V,
connect this pin to ground.
VCC 2 O Internal LDO output. Used as supply to internal control circuits. Do not connect to any
external loads.
Connect a high-quality 1-uF capacitor from this pin to AGND.
AGND 3 G Analog ground for internal circuitry. Feedback and VCC are measured with respect to this
pin. Must connect
AGND to both PGND1 and PGND2 on PCB.
FB 4 I
Output voltage feedback input to the internal control loop. Connect to output voltage sense point
for fixed 3.3
V or 5 V output voltage factory options. Connect to feedback divider tap point for adjustable output
voltage.
Do not float or connect to ground.
PGOOD 5 O
Open-drain power-good status output. Pull this pin up to a suitable voltage supply through a current
limiting
resistor. High = power OK, low = fault. PGOOD output goes low when EN = low, VIN > 1 V. It can be
open or
grounded if not used.
RT 6 I/O Connect this pin to ground through a resistor with value between 5.76 kohm and 66.5 kohm to
set switching
frequency between 200 kHz and 2200 kHz. Do not float or connect to ground.
EN/SYNC 7 I
Precision enable input. High = on, Low = off. Can be connected to VIN. Precision enable allows the
pin to be
used as an adjustable UVLO. See Section 10. Do not float. EN/SYNC also functions as a
synchronization
input pin. Used to synchronize the device switching frequency to a system clock. Triggers on rising
edge of
external clock. A capacitor can be used to AC couple the synchronization signal to this pin. When
synchronized to external clock, the device functions in forced PWM and disables the PFM light load
efficiency mode. See Section 9.
VIN1 8 P Input supply to the converter. Connect a high-quality bypass capacitor or capacitors from
this pin to PGND1.
Low impedance connection must be provided to VIN2.
PGND1 9 G Power ground to internal low-side MOSFET. Connect to system ground. Low impedance
connection must be
provided to PGND2. Connect a high-quality bypass capacitor or capacitors from this pin to VIN1.
SW 10 O Switch node of the converter. Connect to output inductor.
PGND2 11 G Power ground to internal low-side MOSFET. Connect to system ground. Low impedance
connection must be
provided to PGND1. Connect a high-quality bypass capacitor or capacitors from this pin to VIN2.
VIN2 12 P Input supply to the converter. Connect a high-quality bypass capacitor or capacitors from
this pin to PGND2.
Low impedance connection must be provided to VIN1.
RBOOT 13 I/O Connect to CBOOT through a resistor. This resistance must be between 0 ohm and open and
determines SW
node rise time.
CBOOT 14 I/O High-side driver upper supply rail. Connect a 100-nF capacitor between SW pin and
CBOOT. An internal
diode connects to VCC and allows CBOOT to charge while SW node is low.
www.ti.com
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021
Copyright (c) 2021 Texas Instruments Incorporated Submit Document Feedback 3
Product Folder Links: LMQ61460-Q1
```

### Page 4

```text
8 Specifications
8.1 Absolute Maximum Ratings
Over the recommended operating junction temperature range of -40C to +150C (unless otherwise
noted)(1)
PARAMETER MIN MAX UNIT
Input Voltage
VIN1, VIN2 to AGND, PGND -0.3 42 V
RBOOT to SW -0.3 5.5 V
CBOOT to SW -0.3 5.5 V
BIAS to AGND, PGND -0.3 16 V
EN/SYNC to AGND, PGND -0.3 42 V
RT to AGND, PGND -0.3 5.5 V
FB to AGND, PGND -0.3 16 V
PGOOD to AGND, PGND 0 20 V
PGND to AGND(3) -1 2 V
Output Voltage
SW to AGND, PGND(2) -0.3 VIN+0.3 V
VCC to AGND, PGND -0.3 5.5 V
Current PGOOD sink current(4) 10 mA
TJ Junction temperature -40 150  degC
Tstg Storage temperature -40 150  degC
(1) Stresses beyond those listed under Absolute Maximum Ratings may cause permanent damage to the
device. These are stress ratings
only, which do not imply functional operation of the device at these or any other conditions beyond
those indicated under
Recommended Operating Conditions. Exposure to absolute-maximum-rated conditions for extended periods
may affect device
reliability.
(2) A voltage of 2 V below GND and 2 V above V IN can appear on this pin for <= 200 ns with a duty
cycle of <= 0.01%.
(3) This specification applies to voltage durations of 100 ns or less.  The maximum D.C. voltage
should not exceed +/- 0.3 V.
(4) Do not exceed the voltage rating of the pin.
8.2 ESD Ratings
VALUE UNIT
V(ESD) Electrostatic discharge
Human body model (HBM), per AEC Q100-002(1)
Device HBM Classification Level 2 +/-2000
V
Charged device model (CDM), per AEC Q100-011
Device CDM Classification Level C5 +/-750
(1) AEC Q100-002 indicates that HBM stressing shall be in accordance with the ANSI/ESDA/JEDEC JS-001
specification.
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021 www.ti.com
4 Submit Document Feedback Copyright (c) 2021 Texas Instruments Incorporated
Product Folder Links: LMQ61460-Q1
```

### Page 5

```text
8.3 Recommended Operating Conditions
Over the recommended operating junction temperature range of -40 degC to 150 degC (unless otherwise
noted) (1)
MIN NOM MAX UNIT
Input voltage Input voltage range after start-up 3 36 V
Output voltage Output voltage range for adjustable version (2) 1 0.95 * VIN V
Frequency Frequency adjustment range 200 2200 kHz
Sync frequency Synchronization frequency range 200 2200 kHz
Load current Output DC current range (3) 0 6 A
Temperature Operating junction temperature TJ range (4) -40 150  degC
(1) Recommended operating conditions indicate conditions for which the device is intended to be
functional, but do not ensure specific
performance limits. For ensured specifications, see the Electrical Characteristics.
(2) Under no conditions should the output voltage be allowed to fall below zero volts.
(3) Maximum continuous DC current may be derated when operating with high switching frequency, high
ambient temperature, or both.
See the application section for details.
(4) High junction temperatures degrade operating lifetimes.  Operating lifetime is de-rated for
junction temperatures greater than 125 C.
8.4 Thermal Information
The value of RJA given in this table is only valid for comparison with other packages and cannot be
used for design
purposes. These values were calculated in accordance with JESD 51-7, and simulated on a 4-layer
JEDEC board. They do
not represent the performance obtained in an actual application. For example, with a 4-layer PCB, a
RJA = 25C/W can be
achieved. For design information see Maximum Ambient Temperature versus Output Current.
THERMAL METRIC (1) (2)
LMQ61460-Q1
UNITRJR (QFN)
14 PINS
RJA Junction-to-ambient thermal resistance 59  degC/W
RJC(top) Junction-to-case (top) thermal resistance 19  degC/W
RJB Junction-to-board thermal resistance 19.2  degC/W
JT Junction-to-top characterization parameter 1.4  degC/W
JB Junction-to-board characterization parameter 19  degC/W
RJC(bot) Junction-to-case (bottom) thermal resistance -  degC/W
(1) For more information about traditional and new thermal metrics, see the Semiconductor and IC
Package Thermal Metrics application
report.
(2) The value of R JA given in this table is only valid for comparison with other packages and
cannot be used for design purposes. These
values were calculated in accordance with JESD 51-7, and simulated on a 4-layer JEDEC board. They do
not represent the
performance obtained in an actual application.
8.5 Electrical Characteristics
Limits apply over the recommended operating junction temperature range of -40 degC to +150 degC,
unless otherwise stated.
Minimum and Maximum limits are specified through test, design or statistical correlation. Typical
values represent the most
likely parametric norm at TJ = 25 degC, and are provided for reference purposes only. Unless
otherwise stated the following
conditions apply: VIN = 13.5 V.  VIN1 shorted to VIN2 = VIN.  VOUT is converter output voltage.
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
SUPPLY VOLTAGE AND CURRENT
VIN_OPERATE Input operating voltage(3) Needed to start up 3.95
V
Once operating 3.0
VIN_OPERATE_H Hysteresis(3) 1 V
IQ
Operating quiescent current (not
switching); measured at VIN pin(1) VFB = +5%, VBIAS = 5 V 0.6 6 uA
IBIAS
Current into BIAS pin (not
switching, maximum at TJ =
125 degC)(1)
VFB = +5%, VBIAS = 5 V, Auto
Mode 24 31.2 uA
ISD
Shutdown quiescent current;
measured at VIN pin EN = 0 V, TJ = 25C 0.6 6 uA
www.ti.com
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021
Copyright (c) 2021 Texas Instruments Incorporated Submit Document Feedback 5
Product Folder Links: LMQ61460-Q1
```

### Page 6

```text
Limits apply over the recommended operating junction temperature range of -40 degC to +150 degC,
unless otherwise stated.
Minimum and Maximum limits are specified through test, design or statistical correlation. Typical
values represent the most
likely parametric norm at TJ = 25 degC, and are provided for reference purposes only. Unless
otherwise stated the following
conditions apply: VIN = 13.5 V.  VIN1 shorted to VIN2 = VIN.  VOUT is converter output voltage.
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
ENABLE
VEN
Enable input threshold voltage -
rising 1.263 V
VEN-ACC
Enable input threshold voltage -
rising deviation from typical -8.1 8.1 %
VEN-HYST
Enable threshold hysteresis as
percentage of VEN  (TYP) 24 28 32 %
VEN-WAKE Enable wake-up threshold 0.4 V
IEN Enable pin input current VIN = EN = 13.5 V 2.3 uA
VEN_SYNC
Edge height necessary to sync
using EN/SYNC pin Rise/fall time <30 ns 2.4 V
LDO - VCC
VCC Internal VCC voltage
VBIAS > 3.4  V, CCM Operation(3) 3.3
V
VBIAS = 3.1 V, Non-switching 3.1
VCC_UVLO
Internal VCC input under voltage
lock-out
VCC rising under voltage
threshold 3.6 V
VCC_UVLO_HYST
Internal VCC input under voltage
lock-out Hysteresis below VCC_UVLO 1.1 V
FEEDBACK
VFB_acc
Initial reference voltage accuracy
for 5-V, 3.3-V and adjustable (1 V
FB) versions
VIN = 3.3 V to 36 V, TJ = 25C,
FPWM Mode -1 1 %
IFB Input current from FB to AGND Adjustable versions only, FB = 1
V 10 nA
OSCILLATOR
fADJ
Minimum adjustable frequency by
RT or SYNC RT = 66.5 kohm 0.18 0.2 0.22 MHz
Adjustable frequency by RT or
SYNC with 400 kHz setting RT = 33.2 kohm 0.36 0.4 0.44 MHz
Maximum adjustable frequency
by RT or SYNC RT = 5.76 kohm 1.98 2.2 2.42 MHz
fS SS
Frequency span of spread
spectrum operation - largest
deviation from center frequency
Spread spectrum active 2 %
fPSS
Spread spectrum pattern
frequency(3)
Spread spectrum active, fSW =
2.1 MHz 1.5 Hz
MODE/SYNC PIN
MOSFETS
RDS(ON)_HS Power switch on-resistance High side MOSFET RDS(ON) 41 82 mohm
RDS(ON)_LS Power switch on-resistance Low side MOSFET RDS(ON) 21 45 mohm
VBOOT_UVLO
Voltage on CBOOT pin compared
to SW which will turn off high-side
switch
2.1 V
CURRENT LIMITS
IL-HS High side switch current limit(2) Duty Cycle approaches 0% 8.9 10.3 11.5 A
IL-LS Low side switch current limit 6.1 7.1 8.1 A
IL-ZC
Zero-cross current limit.  Positive
current direction is out of SW pin Auto Mode, static measurement 0.25 A
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021 www.ti.com
6 Submit Document Feedback Copyright (c) 2021 Texas Instruments Incorporated
Product Folder Links: LMQ61460-Q1
```

### Page 7

```text
Limits apply over the recommended operating junction temperature range of -40 degC to +150 degC,
unless otherwise stated.
Minimum and Maximum limits are specified through test, design or statistical correlation. Typical
values represent the most
likely parametric norm at TJ = 25 degC, and are provided for reference purposes only. Unless
otherwise stated the following
conditions apply: VIN = 13.5 V.  VIN1 shorted to VIN2 = VIN.  VOUT is converter output voltage.
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
IL-NEG
Negative current limit FPWM and
SYNC Modes.  Positive current
direction is out of SW pin.
FPWM operation -3 A
IPK_MIN_0
Minimum peak command in Auto
Mode / device current rating Pulse duration < 100 ns 25 %
IPK_MIN_100
Minimum peak command in Auto
Mode / device current rating Pulse duration > 1 us 12.5 %
VHICCUP
Ratio of FB voltage to in-
regulation FB voltage Not during soft start 40 %
POWER GOOD
PGDOV PGOOD upper threshold - rising % of VOUT setting 105 107 110 %
PGDU V PGOOD lower threshold - falling % of VOUT setting 92 94 96.5 %
PGDHYST
PGOOD upper threshold (rising &
falling) % of VOUT setting 1.3 %
VIN(PGD_VALID)
Input voltage for proper
PGOOD function 1.0 V
VPGD(LOW)
Low level PGOOD function output
voltage
46 uA pullup to PGOOD pin, VIN
= 1.0 V, EN = 0 V 0.4
V1 mA pullup to PGOOD pin, VIN =
13.5 V, EN = 0 V 0.4
2 mA pullup to PGOOD pin, VIN =
13.5 V, EN = 3.3 V 0.4
RPGD RDS(ON) of PGOOD output
1 mA pullup to PGOOD pin, EN =
0 V 17 40 ohm
1 mA pullup to PGOOD pin, EN =
3.3 V 40 90 ohm
IOV
Pull down current at the SW node
under over voltage condition 0.5 mA
THERMAL SHUTDOWN
TSD_R
Thermal shutdown rising
threshold(3) 158 168 180 C
TSD_HYST Thermal shutdown hysteresis(3) 10 C
(1) This is the current used by the device while not switching, open loop, with FB pulled to +5% of
nominal.  It does not represent the total
input current to the system while regulating. For additional information, reference the System
Characteristics Table and Section 9.3.14.
(2) High side current limit is a function of duty factor.  High side current limit value is highest
at small duty factor and less at higher duty
factors.
(3) Parameter specified by design, statistical analysis, and production testing of correlated
parameters.
8.6 Timing Characteristics
Limits apply over the recommended operating junction temperature range of -40 degC to +150 degC,
unless otherwise stated.
Minimum and Maximum limits are specified through test, design or statistical correlation. Typical
values represent the most
likely parametric norm at TJ = 25 degC, and are provided for reference purposes only. Unless
otherwise stated the following
conditions apply: VIN = 13.5 V.
PARAMETER TEST CONDITION MIN TYP MAX UNIT
SWITCH NODE
tON_MIN Minimum HS switch on time VIN = 20 V, IOUT = 2 A, RBOOT
short to CBOOT 55 70 ns
tON_MAX Maximum HS switch on time 9 us
tOFF_MIN Minimum LS switch on time VIN = 4.0 V, IOUT = 1 A, RBOOT
short to CBOOT 65 85 ns
www.ti.com
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021
Copyright (c) 2021 Texas Instruments Incorporated Submit Document Feedback 7
Product Folder Links: LMQ61460-Q1
```

### Page 8

```text
Limits apply over the recommended operating junction temperature range of -40 degC to +150 degC,
unless otherwise stated.
Minimum and Maximum limits are specified through test, design or statistical correlation. Typical
values represent the most
likely parametric norm at TJ = 25 degC, and are provided for reference purposes only. Unless
otherwise stated the following
conditions apply: VIN = 13.5 V.
PARAMETER TEST CONDITION MIN TYP MAX UNIT
tSS
Time from first SW pulse to VREF at
90% VIN >= 4.2 V 3.5 5 7 ms
tSS2
Time from first SW pulse to release
of FPWM lockout if output not in
regulation
VIN >= 4.2 V 9.5 13 17 ms
tW
Short circuit wait time ("Hiccup"
time) 80 ms
ENABLE
tEN Turn-on delay(1) CVCC = 1 uF, time from EN high to
first SW pulse if output starts at 0 V 0.7 ms
tB
Blanking of EN after rising or falling
edges(1) 4 28 us
tSYNC_EDGE
Enable sync signal hold time after
edge for edge recognition 100 ns
SYNC
POWER GOOD
tPGDFLT(rise) Delay time to PGOOD high signal 1.5 2 2.5 ms
tPGDFLT(fall)
Glitch filter time constant for
PGOOD function 120 us
(1) Parameter specified using design, statistical analysis, and production testing of correlated
parameters; not tested in production.
8.7 Systems Characteristics
The following values are specified by design provided that the component values in the typical
application circuit are used.
Limits apply over the junction temperature range of -40 degC to +150 degC, unless otherwise noted.
Minimum and Maximum limits
are derived using test, design or statistical correlation. Typical values represent the most likely
parametric norm at TJ = 25 degC,
and are provided for reference purposes only. Unless otherwise stated the following conditions
apply: VIN = 13.5 V.  VIN1
shorted to VIN2 = VIN.  VOUT is output setting. These parameters are not tested in production.
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
EFFICIENCY
5V_2p1MHz Typical 2.1 MHz efficiency
VOUT = 5 V, IOUT = 4 A, RBOOT = 0 ohm 93
%VOUT = 5 V, IOUT = 100 uA,
RBOOT = 0 ohm, RFBT = 1 Mohm 73
3p3V_2p1MHz Typical 2.1 MHz efficiency
VOUT = 3.3 V, IOUT = 4 A,
RBOOT = 0 ohm 91
%
VOUT = 3.3 V, IOUT = 100 uA,
RBOOT = 0 ohm, RFBT = 1 Mohm 71
5V_400kHz Typical 400 kHz efficiency
VOUT = 5 V, IOUT = 4 A, RBOOT = 0 ohm 95
%VOUT = 5 V, IOUT = 100 uA,
RBOOT = 0 ohm, RFBT = 1 Mohm 76
RANGE OF OPERATION
VVIN_MIN1
VIN for full functionality at reduced
load, after start-up. VOUT set to 3.3 V 3.0 V
VVIN_MIN2
VIN for full functionality at 100% of
maximum rated load, after start-up. VOUT set to 3.3 V 3.95 V
IQ-VIN Operating quiescent current(1)
VOUT = 3.3 V, IOUT = 0 A, Auto
mode, RFBT = 1 Mohm 7
uA
VOUT = 5 V, IOUT = 0 A, Auto mode,
RFBT = 1 Mohm 10
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021 www.ti.com
8 Submit Document Feedback Copyright (c) 2021 Texas Instruments Incorporated
Product Folder Links: LMQ61460-Q1
```

### Page 9

```text
The following values are specified by design provided that the component values in the typical
application circuit are used.
Limits apply over the junction temperature range of -40 degC to +150 degC, unless otherwise noted.
Minimum and Maximum limits
are derived using test, design or statistical correlation. Typical values represent the most likely
parametric norm at TJ = 25 degC,
and are provided for reference purposes only. Unless otherwise stated the following conditions
apply: VIN = 13.5 V.  VIN1
shorted to VIN2 = VIN.  VOUT is output setting. These parameters are not tested in production.
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
VDROP1
Input to output voltage differential to
maintain regulation accuracy
without inductor DCR drop
VOUT = 3.3 V, IOUT = 4 A, -3% output
accuracy at 25C 0.4
V
VOUT = 3.3 V, IOUT = 4 A, -3% output
accuracy at 125C 0.55
VDROP2
Input to output voltage differential to
maintain fSW >= 1.85MHz, without
DCR drop
VOUT = 3.3 V, IOUT = 4 A, -3%
regulation accuracy at 25C 0.8
V
VOUT = 3.3 V, IOUT = 4 A, -3%
regulation accuracy at 125C 1.2
DMAX Maximum switch duty cycle
fSW =1.85 MHz 87 %
While in frequency fold back 98 %
RBOOT
tRISE SW node rise time
RBOOT = 0 ohm, IOUT = 2 A (10% to
80%) 2.15 ns
RBOOT = 100 ohm, IOUT = 2 A (10% to
80%) 2.7 ns
(1) See detailed description for the meaning of this specification and how it can be calculated.
www.ti.com
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021
Copyright (c) 2021 Texas Instruments Incorporated Submit Document Feedback 9
Product Folder Links: LMQ61460-Q1
```

### Page 10

```text
8.8 Typical Characteristics
Unless otherwise specified, VIN = 13.5 V and fSW = 2100 kHz.
Temperature ( degC)
Quiescent Current (uA)
-50 -25 0 25 50 75 100 125 150
0.5
0.75
1
1.25
1.5
SNVS
VFB = 1 V
Figure 8-1. Non-Switching Input Supply Current
Input Voltage (V)
Shutdown Current (nA)
0 5 10 15 20 25 30 35 40
0
500
1000
1500
2000
2500
3000
3500
4000
SNVS
-40C
25C
150C
VEN = 0 V
Figure 8-2. Shutdown Supply Current
Temperature ( degC)
Voltage (V)
-50 -25 0 25 50 75 100 125 150
0.99
0.994
0.998
1.002
1.006
1.01
snvs
Figure 8-3. Feedback Voltage
Temperature ( degC)
Current (A)
-50 -25 0 25 50 75 100 125 150
5
6
7
8
9
10
11
SNVS
HS
LS Figure 8-4. LMQ61460-Q1 High-Side and Low-Side Current
Limits
Temperature ( degC)
Frequency (kHz)
-50 -25 0 25 50 75 100 125 150
0
250
500
750
1000
1250
1500
1750
2000
2250
2500
2750
3000
3250
3500
SNVS
FREQ = 200 kHz
FREQ = 400 kHz
FREQ = 2.2 MHz
Figure 8-5. Switching Frequency
Temperature ( degC)
RDS-ON (m-Ohm)
-50 -25 0 25 50 75 100 125 150
10
20
30
40
50
60
70
SNVS
HS Switch
LS Switch Figure 8-6. High-Side and Low-Side Switches RDS_ON
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021 www.ti.com
10 Submit Document Feedback Copyright (c) 2021 Texas Instruments Incorporated
Product Folder Links: LMQ61460-Q1
```

### Page 11

```text
8.8 Typical Characteristics (continued)
Unless otherwise specified, VIN = 13.5 V and fSW = 2100 kHz.
Temperature ( degC)
Enable Threshold (V)
-50 -25 0 25 50 75 100 125 150
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1
1.1
1.2
1.3
1.4
snvs
VEN Rising
VEN Falling
VEN_WAKE Rising
VEN_WAKE Falling
Figure 8-7. Enable Thresholds
Temperature ( degC)
PGOOD Threshold (%)
-50 -25 0 25 50 75 100 125 150
80
85
90
95
100
105
110
115
SNVS
OV Tripping
OV Recovery
UV Recovery
UV Tripping Figure 8-8. PGOOD Thresholds
www.ti.com
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021
Copyright (c) 2021 Texas Instruments Incorporated Submit Document Feedback 11
Product Folder Links: LMQ61460-Q1
```

### Page 12

```text
9 Detailed Description
9.1 Overview
The LMQ61460-Q1 is a wide input, synchronous peak-current mode buck regulator designed for a wide
variety
of automotive applications. The regulator can operate over a wide range of switching frequencies
including sub-
AM band at 400 kHz and above the AM band at 2.1 MHz. This device operates over a wide range of
conversion
ratios. If minimum on-time or minimum off-time does not support the desired conversion ratio,
frequency is
reduced automatically, allowing output voltage regulation to be maintained during input voltage
transients with a
high operating-frequency setting.
The device has been designed for low EMI and is optimized for both above and below AM band
operation:
- Meets CISPR25 class 5 standard
- Hotrod (TM) package minimizes switch node ringing
- Parallel input path minimizes parasitic inductance
- Internal bypass capacitors reduce EMI
- Spread spectrum reduces peak emissions
- Adjustable SW node rise time
These features together can eliminate shielding and other expensive EMI mitigation measures.
This device is designed to minimize end-product cost and size while operating in demanding
automotive
environments. The LMQ61460-Q1 can be set to operate in the range of 200 kHz through 2.2 MHz using
its RT
pin. Operation at 2.1 MHz allows for the use of small passive components. State-of-the-art current
limit function
allows the use of inductors that are optimized for and 6-A regulators. In addition, this device has
low unloaded
current consumption, desirable for off-battery, always on applications. The low shutdown current and
high
maximum operating voltage also allows for the elimination of an external load switch and input
transient
protection. To further reduce system cost, an advanced PGOOD output is provided, which can often
eliminate
the use of an external reset or supervisory device.
The LMQ61460-Q1 devices are AEC-Q100-qualified and have electrical characteristics ensured up to a
maximum junction temperature of 150 degC.
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021 www.ti.com
12 Submit Document Feedback Copyright (c) 2021 Texas Instruments Incorporated
Product Folder Links: LMQ61460-Q1
```

### Page 13

```text
9.2 Functional Block Diagram
www.ti.com
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021
Copyright (c) 2021 Texas Instruments Incorporated Submit Document Feedback 13
Product Folder Links: LMQ61460-Q1
```

### Page 14

```text
9.3 Feature Description
9.3.1 EN/SYNC Uses for Enable and VIN UVLO
Start-up and shutdown are controlled by the EN/SYNC input and V IN UVLO. For the device to remain in
shutdown mode, apply a voltage below V EN_WAKE (.4 V) to the EN pin. In shutdown mode, the quiescent
current
drops to 0.6 uA (typical). At a voltage above V EN_WAKE and below V EN, VCC is active and the SW
node is
inactive. Once the EN voltage is above V EN, the chip begins to switch normally provided the input
voltage is
above 3 V.
The EN/SYNC pin cannot be left floating. The simplest way to enable the operation is to connect the
EN/SYNC
pin to VIN, allowing self-start-up of the device when V IN drives the internal VCC above its UVLO
level. However,
many applications benefit from the employment of an enable divider network as shown in Figure 9-1 ,
which
establishes a precision input undervoltage lockout (UVLO). This can be used for sequencing,
preventing re-
triggering the device when used with long input cables, or reducing the occurrence of deep discharge
of a
battery power source. Note that the precision enable threshold V EN has a 8.1% tolerance. Hysteresis
must be
enough to prevent re-triggering. External logic output of another IC can also be used to drive the
EN/SYNC pin,
allowing system power sequencing.
RENT
RENB
EN/SYNC
AGND
VIN
Figure 9-1. VIN SYNC Using the EN pin
Resistor values can be calculated using Equation 1.
RENB = VON  A9EN
VEN
RENT A
(1)
where
- V ON is the desired typical start-up input voltage for the circuit being designed
Note that since the EN pin can also be used as an external synchronization clock input. A blanking
time, t B, is
applied to the enable logic after a clock edge is detected. Any logic change within the blanking
time is ignored.
Blanking time is not applied when the device is in shutdown mode. The blanking time ranges from 4 us
to 28 us.
To effectively disable the output, the EN/SYNC input must stay low for longer than 28 us.
9.3.2 EN/SYNC Pin Uses for Synchronization
The LMQ61460-Q1 EN/SYNC pin can be used to synchronize the internal oscillator to an external clock.
The
internal oscillator can be synchronized by AC coupling a positive clock edge into the EN pin, as
shown in Figure
9-2. It is recommended to keep the parallel combination value of R ENT and R ENB in the 100-k ohm
range. R ENT is
required for synchronization, but R ENB can be left unmounted. Switching action can be synchronized
to an
external clock ranging from 200 kHz to 2.2 MHz. The external clock must be off before start-up to
allow proper
start-up sequencing.
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021 www.ti.com
14 Submit Document Feedback Copyright (c) 2021 Texas Instruments Incorporated
Product Folder Links: LMQ61460-Q1
```

### Page 15

```text
RENT
RENB
EN/SYNC
AGND
VIN
CSYNC
AGND
Clock
Source
Figure 9-2. Typical Implementation Allowing Synchronization Using the EN Pin
Referring to Figure 9-3, the AC-coupled voltage edge at the EN pin must exceed the SYNC amplitude
threshold,
VEN_SYNC_MIN, to trip the internal synchronization pulse detector. In addition, the minimum EN/SYNC
rising pulse
and falling pulse durations must be longer than t SYNC_EDGE(MIN) and shorter than the blanking time
t B. It is
recommended to use a 3.3-V or higher amplitude pulse signal coupled through a 1-nF capacitor, CSYNC.
VEN
EN Voltage
t0
VEN_SYNC
tSYNC_EDGE Time
tSYNC_EDGE
VEN_SYNC
Figure 9-3. Typical SYNC/EN Waveform
After a valid synchronization signal is applied for 2048 cycles, the clock frequency abruptly
changes to that of the
applied signal. Also, if the device in use has the spread-spectrum feature, the valid
synchronization signal
overrides spread spectrum, turning it off, and the clock switches to the applied clock frequency.
9.3.3 Adjustable Switching Frequency
A resistor tied from the device RT pin to AGND is used to set operating frequency. Use Equation 2 or
refer to
Figure 9-4 for resistor values. Note that a resistor value outside of the recommended range can
cause the device
to shut down. This prevents unintended operation if RT pin is shorted to ground or left open. Do not
apply a
pulsed signal to this pin to force synchronization. If synchronization is needed, refer to Section
9.3.2.
RRT(kohm) = (1 / fSW(kHz) - 3.3 x 10-5)  x  1.346 x 104 (2)
www.ti.com
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021
Copyright (c) 2021 Texas Instruments Incorporated Submit Document Feedback 15
Product Folder Links: LMQ61460-Q1
```

### Page 16

```text
Frequency (kHz)
Rt (kOhm)
200 400 600 800 1000 1200 1400 1600 1800 2000 2200
0
10
20
30
40
50
60
70
RTvs
Figure 9-4. Setting Clock Frequency
9.3.4 Clock Locking
Once a valid synchronization signal is detected, a clock locking procedure is initiated. The
LMQ61460-Q1
receives this signal over the EN/SYNC pin. After approximately 2048 pulses, the clock frequency
completes a
smooth transition to the frequency of the synchronization signal without output variation. Note that
while the
frequency is adjusted suddenly, phase is maintained so the clock cycle that lies between operation
at the default
frequency and at the synchronization frequency is of intermediate length. This eliminates very long
or very short
pulses. Once frequency is adjusted, phase is adjusted over a few tens of cycles so that rising
synchronization
edges correspond to rising SW node pulses. See Figure 9-5.
VSYNCDH
VSYNCDL
Pulse 1 Pulse 2 Pulse 3 Pulse 4
Phase lock achieved, Rising edges
align to within approximately 45 ns,
no spread spectrum
VIN
GND
Pulse
~2048
Pulse
~2049
Pulse
~2050
Pulse
~2051
SW Node
Synchronization
signal Spread Spectrum is on between pulse 1 and pulse 2048,
there is no change to operating frequency. At pulse 4,
the device transitions from Auto Mode to FPWM.
On approximately pulse 2048, spread
spectrum turns off
Also clock frequency matches the
synchronization signal and phase
locking begins
Figure 9-5. Synchronization Process
9.3.5 PGOOD Output Operation
The PGOOD function is implemented to replace a discrete reset device, reducing BOM count and cost.
The
PGOOD pin voltage goes low when the feedback voltage is outside of the specified PGOOD thresholds
(see
PGOOD Thresholds in Section 8.8). This can occur in current limit and thermal shutdown, as well as
while
disabled and during normal start-up. A glitch filter prevents false flag operation for short
excursions of the output
voltage, such as during line and load transients. Output voltage excursions shorter than t
PGDFLT_FALL do not trip
the power-good flag. Power-good operation can be best understood by referring to Figure 9-6.
The power-good output consists of an open-drain NMOS, requiring an external pullup resistor to a
suitable logic
supply or VOUT. When EN is pulled low, the flag output is also forced low. With EN low, power good
remains valid
as long as the input voltage is >= 1 V (typical).
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021 www.ti.com
16 Submit Document Feedback Copyright (c) 2021 Texas Instruments Incorporated
Product Folder Links: LMQ61460-Q1
```

### Page 17

```text
Input
Voltage Input Voltage
Output
Voltage
VPGD_UV (falling)
VPGD_HYST
VIN_OPERATE (rising)
VIN(PGD_VALID)
GND
< 18 V
VIN_OPERATE (falling)
PGOOD
PGOOD may
not be valid if
input is below
VIN(PGD_VALID)
Startup
delay
PGOOD may not
be valid if input is
below VIN(PGD_VALID)
Small glitches do not
reset tPGDFLT(rise) timer
Small glitches
do not cause
PGOOD to
signal a fault
tPGDFLT(rise)
tPGDFLT(fall)
tPGDFLT(fall)
tPGDFLT(rise)
tPGDFLT(fall)
tPGDFLT(fall)
Figure 9-6. PGOOD Timing Diagram (Excludes OV Events)
Table 9-1. Conditions That Cause PGOOD to Signal a Fault (Pull Low)
FAULT CONDITION INITIATED FAULT CONDITION ENDS (AFTER WHICH tPGDFLT(rise) MUST PASS
BEFORE PGOOD OUTPUT IS RELEASED)(1)
VOUT < VOUT-target  x  PGDUV AND t > tPGDFLT(fall)
Output voltage in regulation:
VOUT-target  x  (PGDUV + PGDHYST) < VOUT < VOUT-target  x  (PGDOV -
PGDHYST) (see PGOOD Thresholds in Section 8.8)
VOUT > VOUT-target  x  PGDOV AND t > tPGDFLT(fall) Output voltage in regulation
TJ > TSD_R TJ < TSD_F AND output voltage in regulation
EN < VEN Falling EN > VEN Rising AND output voltage in regulation
VCC < VCC_UVLO - VCC_UVLO_HYST VCC > VCC_UVLO AND output voltage in regulation
(1) As an additional operational check, PGOOD remains low during soft start, defined as until the
lesser of either full output voltage
reached or tSS2 has passed since initiation.
9.3.6 Internal LDO, VCC UVLO, and BIAS Input
The VCC pin is the output of the internal LDO used to supply the control circuits of the device. The
nominal
output is 3 V to 3.3 V. The BIAS pin is the input to the internal LDO. This input can be connected
to V OUT to
provide the lowest possible input supply current. If the BIAS voltage is less than 3.1 V, VIN1 and
VIN2 directly
powers the internal LDO.
To prevent unsafe operation, VCC has a UVLO that prevents switching if the internal voltage is too
low. See
VCC_UVLO and VCC_UVLO_HYST in Section 8.5. Note that these UVLO values and the dropout of the LDO
are used
to derive minimum VIN_OPERATE and VIN_OPERATE_H values.
9.3.7 Bootstrap Voltage and VCBOOT-UVLO (CBOOT Pin)
The driver of the High-Side (HS) switch requires bias higher than V IN. The capacitor, CBOOT,
connected
between CBOOT and SW works as a charge pump to boost voltage on the CBOOT pin to SW+VCC. A boot
diode is integrated on the device die to minimize external component count. It is recommended that a
100-nF
capacitor rated for 10-V or higher is used. The V BOOT_UVLO threshold (2.1 V typ) is designed to
maintain proper
HS switch operation. If the CBOOT capacitor voltage drops below V BOOT_UVLO, then the device
initiates a
charging sequence turning on the low-side switch before attempting to turn on the HS switch.
9.3.8 Adjustable SW Node Slew Rate
To allow optimization of EMI with respect to efficiency, the device is designed to allow a resistor
to select the
strength of the driver of the high-side FET during turn on. See Figure 9-7 . The current drawn
through the
www.ti.com
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021
Copyright (c) 2021 Texas Instruments Incorporated Submit Document Feedback 17
Product Folder Links: LMQ61460-Q1
```

### Page 18

```text
RBOOT pin (the dotted loop) is magnified and drawn through from CBOOT (the dashed line). This
current is
used to turn on the high-side power MOSEFT.
CBOOT
SW
RBOOT
VCC
VIN
HS FET
LS FET
HS
Driver
Figure 9-7. Simplified Circuit Showing How RBOOT Functions
With RBOOT short circuited to CBOOT, rise time is very fast. As a result SW node harmonics do not
"roll off"
until above 150 MHz. A boot resistor of 100 ohm corresponds to approximately 2.7 ns SW node rise,
and this 100-
ohm boot resistor virtually eliminates SW node overshoot. The slower rise time allows energy in SW
node
harmonics to roll off near 100 MHz under most conditions. Rolling off harmonics eliminates the need
for shielding
and common mode chokes in many applications. Note that rise time increases with increasing input
voltage.
Noise due to stored charge is also greatly reduced with higher RBOOT resistance. Switching with
slower slew
rate also decreases the efficiency.
9.3.9 Spread Spectrum
Spread spectrum is a factory option. To find which devices have spread spectrum enabled, see Section
6. The
purpose of spread spectrum is to eliminate peak emissions at specific frequencies by spreading these
emissions
across a wider range of frequencies rather than a part with fixed frequency operation. In most
systems
containing the chip, low frequency-conducted emissions from the first few harmonics of the switching
frequency
can be easily filtered. A more difficult design criterion is reduction of emissions at higher
harmonics which fall in
the FM band. These harmonics often couple to the environment through electric fields around the
switch node
and inductor. The device uses a +/-2% spread of frequencies which can spread energy smoothly across
the FM
and TV bands but is small enough to limit subharmonic emissions below the device switching
frequency. Peak
emissions at the switching frequency of the part are only reduced slightly, by less than 1 dB, while
peaks in the
FM band are typically reduced by more than 6 dB.
The device uses a cycle-to-cycle frequency hopping method based on a linear feedback shift register
(LFSR).
This intelligent pseudo-random generator limits cycle-to-cycle frequency changes to limit output
ripple. The
pseudo-random pattern repeats at less than 1.5 Hz, which is below the audio band.
The spread spectrum is only available while the clock of the device is free running at their natural
frequency. Any
of the following conditions overrides spread spectrum, turning it off:
- The clock is slowed during dropout.
- The clock is slowed at light load in auto mode. In FPWM mode, spread spectrum is active even if
there is no
load.
- At high input voltage/low output voltage ratio when the device operates at minimum on time the
internal clock
is slowed disabling spread spectrum. See Section 8.6.
- The clock is synchronized with an external clock.
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021 www.ti.com
18 Submit Document Feedback Copyright (c) 2021 Texas Instruments Incorporated
Product Folder Links: LMQ61460-Q1
```

### Page 19

```text
9.3.10 Soft Start and Recovery From Dropout
The device uses a reference-based soft start that prevents output voltage overshoots and large
inrush currents
during start-up. Soft start is triggered by any of the following conditions:
- Power is applied to the VIN pin of the IC, releasing UVLO.
- EN is used to turn on the device.
- Recovery from a hiccup waiting period
- Recovery from shutdown due to overtemperature protection
Once soft start is triggered, the IC takes the following actions:
- The reference used by the IC to regulate output voltage is slowly ramped. The net result is that
output voltage
takes tSS to reach 90% of its desired value.
- Operating mode is set to auto, activating diode emulation. This allows start-up without pulling
output low if
there is a voltage already present on output.
Together, these actions provide start-up with limited inrush currents and also allow the use of
larger output
capacitors and higher loading conditions that cause current to border on current limit during
start-up without
triggering hiccup. See Figure 9-8.
VEN
VOUT Set
Point
EN and Output Voltages Time
t
VOUT
V
90% of
VOUT Set
Point
0 V
tSS2
tSS
Triggering event If selected, FPWM
is enabled after
regulation but no
later than tSS2tEN
VEN
VOUT Set
Point
EN and Output Voltages Time
t
VOUT
V
90% of
VOUT Set
Point
0 V
tSS2
tSS
Triggering event If selected, FPWM
is enabled after
regulation but no
later than tSS2tEN
Soft start works with both output voltage starting from 0 V on the left curves, or if there is
already voltage on the output, as shown on
right. In either case, output voltage must reach within 10% of the desired value tSS after soft
start is initiated. During soft start, FPWM and
hiccup are disabled. Both hiccup and FPWM are enabled once output reaches regulation or tSS2,
whichever happens first.
Figure 9-8. Soft-Start Operation
Any time the output voltage falls more than a few percent, the output voltage will ramp up slowly.
This condition
is called recovery from dropout and differs from soft start in three important ways:
- The reference voltage is set to approximately 1% above what is needed to achieve the existing
output
voltage.
- Hiccup is allowed if output voltage is less than 0.4 times its set point. Note that during dropout
regulation
itself, hiccup is inhibited.
- FPWM mode is allowed during recovery from dropout. If the output voltage were to suddenly be
pulled up by
an external supply, the device can pull down on the output.
Despite being called recovery from dropout, this feature is active whenever output voltage drops to
a few percent
lower than the set point. This primarily occurs under the following conditions:
- Dropout: When there is insufficient input voltage for the desired output voltage to be generated
- Overcurrent: When there is an overcurrent event that is not severe enough to trigger hiccup
www.ti.com
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021
Copyright (c) 2021 Texas Instruments Incorporated Submit Document Feedback 19
Product Folder Links: LMQ61460-Q1
```

### Page 20

```text
VIN
VOUT Set
Point
Input and Output
Voltage
Slope
the same
as during
soft start
Time t
VOUT
V
Whether output voltage falls due to high load or low input voltage, once the condition that causes
output to fall below its set point is
removed, the output climbs at the same speed as during start-up. Even though hiccup does not trigger
due to dropout, it can in principle
be triggered during recovery if output voltage is below 0.4 times the output set point for more than
128 clock cycles.
Figure 9-9. Recovery From Dropout
VOUT
(1 A/DIV)
Time (2 ms/DIV)
IINDUCTOR
(2 V/DIV)
VIN
(5 V/DIV)
Figure 9-10. Recovery From Dropout (VOUT = 5 V, IOUT = 4 A, VIN = 13.5 V to 4 V to 13.5 V)
9.3.11 Output Voltage Setting
If the LMQ61460-Q1 has fixed 5-V or fixed 3.3-V output, simply connect FB to the output. See Section
10.1 for
layout information.
For versions of the LMQ61460-Q1 with adjustable output voltage, a feedback resistor divider network
between
the output voltage and the FB pin is used to set output voltage level. See Figure 9-11.
RFBT
RFBB
FB
AGND
VOUT
Figure 9-11. Setting Output Voltage of Adjustable Versions
The device uses a 1-V reference voltage for the feedback (FB) pin. The FB pin voltage is regulated
by the
internal controller to be the same as the reference voltage. The output voltage level is then set by
the ratio of the
resistor divider. Equation 3  can be used to determine R FBB for a desired output voltage and a
given R FBT.
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021 www.ti.com
20 Submit Document Feedback Copyright (c) 2021 Texas Instruments Incorporated
Product Folder Links: LMQ61460-Q1
```

### Page 21

```text
Usually R FBT is between 10 k ohm and 1 M ohm. 100 k ohm is recommended for R FBT for improved noise
immunity
compared to 1 Mohm and reduced current consumption compared to lower resistance values.
RFBB = VOUT  A1
RFBT
(3)
In addition, a feedforward capacitor, C FF, connected in parallel with R FBT can be required to
optimize the
transient response.
9.3.12 Overcurrent and Short Circuit Protection
The device is protected from overcurrent conditions with cycle-by-cycle current limiting on both the
high-side and
the low-side MOSFETs.
High-side MOSFET overcurrent protection is implemented by the nature of the peak-current mode
control. The
HS switch current is sensed when the HS is turned on after a short blanking time. Every switching
cycle, the HS
switch current is compared to either the minimum of a fixed current set point or the output of the
voltage
regulation loop minus slope compensation. Because the voltage loop has a maximum value and slope
compensation increases with duty cycle, HS current limit decreases with increased duty cycle when
duty cycle is
above 35%. See Figure 9-12.
Duty Cycle
Command Current (A)
0 0.2 0.4 0.6 0.8 1
0
2
4
6
8
10
12
FEAT
HS Maximum Current
Rated Maximum Output
Figure 9-12. Maximum Current Allowed Through the HS FET - Function of Duty Cycle for LMQ61460-Q1
When the LS switch is turned on, the switch current is also sensed and monitored. Like the high-side
device, the
low-side device turns off as commanded by the voltage control loop, low-side current limit. If the
LS switch
current is higher than ILS_Limit at the end of a switching cycle, the switching cycle is extended
until the LS current
reduces below the limit. The LS switch is turned off once the LS current falls below its limit, and
the HS switch is
turned on again as long as at least one clock period has passed since the last time the HS device
has turned on.
www.ti.com
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021
Copyright (c) 2021 Texas Instruments Incorporated Submit Document Feedback 21
Product Folder Links: LMQ61460-Q1
```

### Page 22

```text
iL
VSW
IL-LS
Inductor Current
t
t
0
0
SW Voltage
VIN
Typically, tSW > Clock setting
tON < tON_MAX
IL-HS
IOUT
Figure 9-13. Current Limit Waveforms
Since the current waveform assumes values between I L-HS and I L-LS, the maximum output current is
very close
to the average of these two values. Hysteretic control is used and current does not increase as
output voltage
approaches zero.
The device employs hiccup overcurrent protection if there is an extreme overload, and the following
conditions
are met for 128 consecutive switching cycles:
- Output voltage is below approximately 0.4 times the output voltage set point.
- Greater than t SS2 has passed since soft start has started; see Section 9.3.10.
- The part is not operating in dropout, which is defined as having minimum off-time controlled duty
cycle.
In hiccup mode, the device shuts itself down and attempts to soft start after t W. Hiccup mode helps
reduce the
device power dissipation under severe overcurrent conditions and short circuits. See Figure 9-14.
Once the overload is removed, the device recovers as though in soft start; see Figure 9-15.
VOUT
(2 A/DIV)
Time (20 ms/DIV)
IINDUCTOR
(500 mV/DIV)
Figure 9-14. Inductor Current Bursts During
Hiccup
VOUT
(2 A/DIV)
Time (20 ms/DIV)
IINDUCTOR
(2 V/DIV)
Figure 9-15. Short-Circuit Recovery
9.3.13 Thermal Shutdown
Thermal shutdown prevents the device from extreme junction temperatures by turning off the internal
switches
when the IC junction temperature exceeds 165 degC (typical). Thermal shutdown does not trigger below
158 degC.
After thermal shutdown occurs, hysteresis prevents the device from switching until the junction
temperature
drops to approximately 155 degC. When the junction temperature falls below 155 degC (typical), the
device attempts to
soft start.
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021 www.ti.com
22 Submit Document Feedback Copyright (c) 2021 Texas Instruments Incorporated
Product Folder Links: LMQ61460-Q1
```

### Page 23

```text
While the device is shut down due to high junction temperature, power continues to be provided to
VCC. To
prevent overheating due to a short circuit applied to VCC, the LDO that provides power for VCC has
reduced
current limit while the part is disabled due to high junction temperature. The VCC current limit is
reduced to a few
milliamperes during thermal shutdown.
9.3.14 Input Supply Current
The device is designed to have very low input supply current when regulating light loads. This is
achieved by
powering much of the internal circuitry from the output. The BIAS pin is the input to the LDO that
powers the
majority of the control circuits. By connecting the BIAS input pin to the output of the regulator, a
small amount of
current drawn from the output. This current is reduced at the input by the ratio of VOUT / VIN.

Q _ VIN Q EN B div
eff
Output VoltageI I I I I Input Voltage    K u IAS
Q _ VIN Q EN B div
eff
Output VoltageI I I I I Input Voltage    K u
(4)
where
- I Q_VIN is the current consumed by the operating (switching) buck converter while unloaded
- I Q is the current drawn from the VIN terminal. See IQ in Section 8.5
- I EN is current drawn by the EN terminal. Include this current if EN is connected to VIN. See IEN
in Section 8.5.
Note that this current drops to a very low value if connected to a voltage less than 5 V
- I BIAS is bias current drawn by the BIAS input. See IBIAS in Section 8.5
- I div is the current drawn by the feedback voltage divider used to set output voltage
-  eff is the light load efficiency of the buck converter with IQ_VIN removed from the input current
of the buck
converter. eff = 0.8 is a conservative value that can be used under normal operating conditions
9.4 Device Functional Modes
9.4.1 Shutdown Mode
The EN pin provides electrical ON and OFF control of the device. When the EN pin voltage is below
0.4 V, both
the converter and the internal LDO have no output voltage and the part is in shutdown mode. In
shutdown mode,
the quiescent current drops to typically 0.6 uA.
9.4.2 Standby Mode
The internal LDO has a lower EN threshold than the output of the converter. When the EN pin voltage
is above
1.1 V (maximum) and below the precision enable threshold for the output voltage, the internal LDO
regulates the
VCC voltage at 3.3 V typical. The precision enable circuitry is ON once VCC is above its UVLO. The
internal
power MOSFETs of the SW node remain off unless the voltage on EN pin goes above its precision enable
threshold. The device also employs UVLO protection. If the VCC voltage is below its UVLO level, the
output of
the converter is turned off.
9.4.3 Active Mode
The device is in active mode whenever the EN pin is above V EN, VIN is high enough to satisfy V
IN_OPERATE, and
no other fault conditions are present. The simplest way to enable the operation is to connect the EN
pin to V IN
which allows self start-up when the applied input voltage exceeds the minimum VIN_OPERATE.
In active mode, depending on the load current, input voltage, and output voltage, the device is in
one of six
modes:
- Continuous conduction mode (CCM) with fixed switching frequency when load current is above half of
the
inductor current ripple.
- Auto Mode - Light Load Operation: PFM when switching frequency is decreased at very light load.
- FPWM Mode - Light Load Operation: Discontinuous conduction mode (DCM) when the load current is
lower
than half of the inductor current ripple.
- Minimum on-time: At high input voltage, low output voltages the switching frequency is reduced to
maintain
regulation.
- Dropout mode: When switching frequency is reduced to minimize voltage drop out.
www.ti.com
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021
Copyright (c) 2021 Texas Instruments Incorporated Submit Document Feedback 23
Product Folder Links: LMQ61460-Q1
```

### Page 24

```text
9.4.3.1 CCM Mode
The following operating description of the device refers to Section 9.2 and to the waveforms in
Figure 9-16. In
CCM, the device supplies a regulated output voltage by turning on the internal high-side (HS) and
low-side (LS)
NMOS switches with varying duty cycle (D). During the HS switch on-time, the SW pin voltage, V SW,
swings up
to approximately V IN, and the inductor current, i L, increases with a linear slope. The HS switch
is turned off by
the control logic. During the HS switch off-time, t OFF, the LS switch is turned on. Inductor
current discharges
through the LS switch, which forces the V SW to swing below ground by the voltage drop across the LS
switch.
The converter loop adjusts the duty cycle to maintain a constant output voltage. D is defined by the
on-time of
the HS switch over the switching period:
D = TON / TSW (5)
In an ideal buck converter where losses are ignored, D is proportional to the output voltage and
inversely
proportional to the input voltage:
D = VOUT / VIN (6)
iL
VSW
ILPK
IOUT Iripple
Inductor Current
- IOUTA5DSLS
D =
t
t
0
0
SW Voltage
tON
tSWVIN
tSW
tON tOFF
VOUT
VIN

Figure 9-16. SW Voltage and Inductor Current Waveforms in Continuous Conduction Mode (CCM)
9.4.3.2 Auto Mode - Light Load Operation
The device can have two behaviors while lightly loaded. One behavior, called auto mode operation,
allows for
seamless transition between normal current mode operation while heavily loaded and highly efficient
light load
operation. The other behavior, called FPWM Mode, maintains full frequency even when unloaded. Which
mode
the device operates in depends on which factory option is employed, see Section 6. Note that all
parts operate in
FPWM mode when synchronizing frequency to an external signal.
In auto mode, light load operation is employed in the device at load lower than approximately a
tenth of the rated
maximum output current. Light-load operation employs two techniques to improve efficiency:
- Diode emulation, which allows DCM operation
- Frequency reduction
Note that while these two features operate together to create excellent light load behavior, they
operate
independently of each other.
9.4.3.2.1 Diode Emulation
Diode emulation prevents reverse current though the inductor which requires a lower frequency needed
to
regulate given a fixed peak inductor current. Diode emulation also limits ripple current as
frequency is reduced.
With a fixed peak current, as output current is reduced to zero, frequency must be reduced to near
zero to
maintain regulation.
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021 www.ti.com
24 Submit Document Feedback Copyright (c) 2021 Texas Instruments Incorporated
Product Folder Links: LMQ61460-Q1
```

### Page 25

```text
iL
VSW
ILPK
IOUT
Inductor Current
D =
t
t
0
0
SW Voltage
tON
tSW
VIN
tSW
tON tOFF tHIGHZ
VOUT
VIN
<
In auto mode, the low-side device is turned off once SW node current is near zero. As a result, once
output current is less than half of
what inductor ripple would be in CCM, the part operates in DCM which is equivalent to the statement
that diode emulation is active.
Figure 9-17. PFM Operation
The device has a minimum peak inductor current setting while in auto mode. Once current is reduced
to a low
value with fixed input voltage, on-time is constant. Regulation is then achieved by adjusting
frequency. This
mode of operation is called PFM mode regulation.
9.4.3.2.2 Frequency Reduction
The device reduces frequency whenever output voltage is high. This function is enabled whenever
Comp, an
internal signal, is low and there is an offset between the regulation set point of FB and the
voltage applied to FB.
The net effect is that there is larger output impedance while lightly loaded in auto mode than in
normal operation.
Output voltage must be approximately 1% high when the part is completely unloaded.
1% Above
Set point
VOUT Set
Point
Output Voltage
Current
Limit
VOUT
Output Current IOUT0
In auto mode, once output current drops below approximately 1/10th the rated current of the part,
output resistance increases so that
output voltage is 1% high while the buck is completely unloaded.
Figure 9-18. Steady State Output Voltage versus Output Current in Auto Mode
In PFM operation, a small DC positive offset is required on the output voltage to activate the PFM
detector. The
lower the frequency in PFM, the more DC offset is needed on VOUT. If the DC offset on VOUT is not
acceptable, a
dummy load at VOUT or FPWM Mode can be used to reduce or eliminate this offset.
www.ti.com
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021
Copyright (c) 2021 Texas Instruments Incorporated Submit Document Feedback 25
Product Folder Links: LMQ61460-Q1
```

### Page 26

```text
9.4.3.3 FPWM Mode - Light Load Operation
Like auto mode operation, FPWM mode operation during light load operation is selected as a factory
option.
In FPWM Mode, frequency is maintained while lightly loaded. To maintain frequency, a limited reverse
current is
allowed to flow through the inductor. Reverse current is limited by reverse current limit circuitry,
see Section 8.5
for reverse current limit values.
iL
VSW
ILPK
IOUT Iripple
Inductor Current
D =
t
t
0
0
SW Voltage
tON
tSW
VIN
tSW
tON tOFF
VOUT
VIN

In FPWM mode, Continuous Conduction (CCM) is possible even if IOUT is less than half of Iripple.
Figure 9-19. FPWM Mode Operation
For all devices, in FPWM mode, frequency reduction is still available if output voltage is high
enough to
command minimum on-time even while lightly loaded, allowing good behavior during faults which
involve output
being pulled up.
9.4.3.4 Minimum On-time (High Input Voltage) Operation
The device continues to regulate output voltage even if the input-to-output voltage ratio requires
an on-time less
than the minimum on-time of the chip with a given clock setting. This is accomplished using valley
current
control. At all times, the compensation circuit dictates both a maximum peak inductor current and a
maximum
valley inductor current. If for any reason, valley current is exceeded, the clock cycle is extended
until valley
current falls below that determined by the compensation circuit. If the converter is not operating
in current limit,
the maximum valley current is set above the peak inductor current, preventing valley control from
being used
unless there is a failure to regulate using peak current only. If the input-to-output voltage ratio
is too high, even
though current exceeds the peak value dictated by compensation, the high-side device cannot be
turned off
quickly enough to regulate output voltage. As a result, the compensation circuit reduces both peak
and valley
current. Once a low enough current is selected by the compensation circuit, valley current matches
that being
commanded by the compensation circuit. Under these conditions, the low-side device is kept on and
the next
clock cycle is prevented from starting until inductor current drops below the desired valley
current. Since on-time
is fixed at its minimum value, this type of operation resembles that of a device using a COT control
scheme; see
Figure 9-20.
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021 www.ti.com
26 Submit Document Feedback Copyright (c) 2021 Texas Instruments Incorporated
Product Folder Links: LMQ61460-Q1
```

### Page 27

```text
iL
VSW
ILVLY
IOUT Iripple
Inductor Current
- IOUTA5DSLS
D =
t
t
0
0
SW Voltage
tON
tSWVIN
tSW > Clock setting
tON = tON_MIN
tOFF
VOUT
VIN

In valley control mode, minimum inductor current is regulated, not peak inductor current.
Figure 9-20. Valley Current Mode Operation
9.4.3.5 Dropout
Dropout operation is defined as any input-to-output voltage ratio that requires frequency to drop to
achieve the
required duty cycle. At a given clock frequency, duty cycle is limited by minimum off-time. Once
this limit is
reached, if clock frequency were maintained, output voltage would fall. Instead of allowing the
output voltage to
drop, the device extends on-time past the end of the clock cycle until needed peak inductor current
is achieved.
The clock is allowed to start a new cycle once peak inductor current is achieved or once a
pre-determined
maximum on-time, t ON_MAX, of approximately 9 us passes. As a result, once the needed duty cycle
cannot be
achieved at the selected clock frequency due to the existence of a minimum off-time, frequency drops
to
maintain regulation. If input voltage is low enough so that output voltage cannot be regulated even
with an on-
time of t ON_MAX, output voltage drops to slightly below input voltage, V DROP1. For additional
information on
recovery from dropout, reference Figure 9-9.
iL
Output
Setting
Output Voltage
VIN0
Input
Voltage
iL
IOUT
Switching Frequency VIN0
Frequency
Setting
Input Voltage
Input Voltage
~100kHz
VDROP1 Output
Voltage
VDROP2 if
frequency =
1.85 MHz
Output voltage and frequency versus input voltage: If there is little difference between input
voltage and output voltage setting, the IC
reduces frequency to maintain regulation. If input voltage is too low to provide the desired output
voltage at approximately 110 kHz, input
voltage tracks output voltage.
Figure 9-21. Frequency and Output Voltage in Dropout
www.ti.com
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021
Copyright (c) 2021 Texas Instruments Incorporated Submit Document Feedback 27
Product Folder Links: LMQ61460-Q1
```

### Page 28

```text
iL
VSW
IOUT Iripple
Inductor Current
- IOUTA5DSLS
D =
t
t
0
0
SW Voltage
tON
tSWVIN
tSW > Clock setting
tOFF = tOFF_MIN
tON < tON_MAX
VOUT
VIN

ILPK
Switching waveforms while in dropout. Inductor current takes longer than a normal clock to reach the
desired peak value. As a result,
frequency drops. This frequency drop is limited by tON_MAX.
Figure 9-22. Dropout Waveforms
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021 www.ti.com
28 Submit Document Feedback Copyright (c) 2021 Texas Instruments Incorporated
Product Folder Links: LMQ61460-Q1
```

### Page 29

```text
10 Application and Implementation
Note
Information in the following applications sections is not part of the TI component specification,
and TI
does not warrant its accuracy or completeness. TI's customers are responsible for determining
suitability of components for their purposes, as well as validating and testing their design
implementation to confirm system functionality.
10.1 Application Information
The LMQ61460-Q1 step-down DC-to-DC converter is typically used to convert a higher DC voltage to a
lower
DC voltage with a maximum output current of 6 A. Using a 4-layer LMQ61460EVM, at 400 kHz, the device
can
sustain a continuous 6 A load up to an ambient temperature of approximately 95 degC. The following
design
procedure can be used to select components for the LMQ61460-Q1.
10.2 Typical Application
Figure 10-1 shows a typical application circuit for the device. This device is designed to function
with a wide
range of external components and system parameters. However, the internal compensation is optimized
for a
certain range of external inductance and output capacitance. As a quick start guide, Table 10-2
provides typical
component values for some of the common configurations.
PGOODEN/SYNC
RT
PGND1
AGND
VCC
CBOOT
SW
FB
BIAS
RBOOT
5 V to 36 V input
VIN1
PGND2
VIN2
RRT
CVCC
RENT
CIN_HF1 CIN_HF2
CIN-BLK
RPG
CBT COUT
RFBT
RFBB
CFF
RFF
L1 Output
Figure 10-1. Example Application Circuit
10.2.1 Design Requirements
Table 10-1 provides the parameters for our detailed design procedure example:
Table 10-1. Detailed Design Parameters
DESIGN PARAMETER EXAMPLE VALUE
Input voltage 13.5 V (5 V to 36 V)
Input voltage for constant fSW 8 V to 18 V
Output voltage 5 V
Maximum output current 0 A to 6 A
Switching frequency 400 kHz
www.ti.com
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021
Copyright (c) 2021 Texas Instruments Incorporated Submit Document Feedback 29
Product Folder Links: LMQ61460-Q1
```

### Page 30

```text
Table 10-2. Typical External Component Values
fSW
(kHz) VOUT (V) L1 (uH) COUT (RATED) RFBT
(kohm)
RFBB
(kohm)
CBOOT
(uF)
RBOOT
(ohm)
CVCC
(uF) CFF (pF) RFF (kohm)
2100 3.3 1 3  x  22 uF ceramic 100 43.2 0.1 0 1 10 1
400 3.3 4.7 3  x  47 uF ceramic 100 43.2 0.1 0 1 4.7 1
2100 5 1.5 2  x  22 uF ceramic 100 24.9 0.1 0 1 22 1
400 5 4.7 2  x  47 uF ceramic 100 24.9 0.1 0 1 22 1
10.2.2 Detailed Design Procedure
The following design procedure applies to Figure 10-1 and Table 10-1.
10.2.2.1 Choosing the Switching Frequency
The choice of switching frequency is a compromise between conversion efficiency and overall solution
size.
Lower switching frequency implies reduced switching losses and usually results in higher system
efficiency.
However, higher switching frequency allows for the use of smaller inductors and output capacitors,
hence, a
more compact design.
When choosing operating frequency, the most important consideration is thermal limitations. This
constraint
typically dominates frequency selection. See Figure 10-2  for circuits running at 400 kHz and Figure
10-3  for
circuits running at 2.1 MHz. These curves show how much output current can be supported at a given
ambient
temperature given these switching frequencies. Note that power dissipation is layout dependent so
while these
curves are a good starting point, thermal resistance in any design will be different from the
estimates used to
generate Figure 10-2 and Figure 10-3. The maximum temperature ratings are based on the LMQ61460EVM,
which is approximately 100 mm x 80 mm in board area. Unless a larger copper area or cooling is
provided to
reduce the effective R JA, if ambient temperature is 105 degC and the switching frequency is set to
2.1 MHz, the
load current should typically be limited to 4 A.
Output Current (A)
Ambient Temperature  ( degC)
3 3.5 4 4.5 5 5.5 6
85
90
95
100
105
110
115
120
125
130
snvs
VIN = 13.5 V
VIN = 16 V
VIN = 24 V
fSW = 400 kHz PCB RJA = 25 degC/W VOUT = 5 V
Figure 10-2. Maximum Ambient Temperature
versus Output Current
Output Current (A)
Ambient Temperature ( degC)
2 2.5 3 3.5 4 4.5 5 5.5 6
65
75
85
95
105
115
125
135
snvs
VIN = 13.5 V
VIN = 16 V
VIN = 24 V
fSW = 2100 kHz PCB RJA = 25 degC/W VOUT = 5 V
Figure 10-3. Maximum Ambient Temperature
versus Output Current
Two other considerations are what maximum and minimum input voltage the part must maintain for the
frequency setting. Since the device adjusts its frequency under conditions in which regulation would
normally be
prevented by minimum on-time or minimum off-time, these constraints are only important for input
voltages
requiring constant frequency operation.
If foldback is undesirable at high input voltage, use Equation 7:
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021 www.ti.com
30 Submit Document Feedback Copyright (c) 2021 Texas Instruments Incorporated
Product Folder Links: LMQ61460-Q1
```

### Page 31

```text
fSW G  VIN(MAX2) AWON_MIN(MAX)
VOUT
(7)
If foldback at low input voltage is a concern, use Equation 8:
fSW  VINeff(MIN2) AWOFF_MIN(MAX)
VINeff(MIN2) +/- VOUT
(8)
where:
-
VINeff(MIN2) = VIN(MIN2) +/- IOUT(MAX) A(RDS(ON)_HS(MAX) + DCR(MAX))
- DCR(MAX) is the maximum DCR of the inductor
See Section 8.5 for tOFF_MIN(MAX) and RDS(ON)_HS(MAX).
The fourth constraint is the rated frequency range of the IC. See f ADJ in Section 8.5. All four
constraints above,
thermal, V IN(MAX2), V IN(MIN2), and device specified frequency range must be considered when
selecting
frequency.
Many applications require that the AM band can be avoided. These applications tend to operate at
either 400
kHz below the AM band or 2.1 MHz above the AM band. In this example, 400 kHz is chosen.
10.2.2.2 Setting the Output Voltage
The output voltage of the device is externally adjustable using a resistor divider network. The
range of
recommended output voltage is found in Section 8.3. The divider network is comprised of R FBT and R
FBB, and
closes the loop between the output voltage and the converter. The converter regulates the output
voltage by
holding the voltage on the FB pin equal to the internal reference voltage, V REF. The resistance of
the divider is a
compromise between excessive noise pickup and excessive loading of the output. Smaller values of
resistance
reduce noise sensitivity but also reduce the light-load efficiency. The recommended value for RFBT
is 100 kohm with
a maximum value of 1 M ohm. If 1 M ohm is selected for R FBT, then a feedforward capacitor must be
used across this
resistor to provide adequate loop phase margin (see Section 10.2.2.10). Once R FBT is selected,
Equation 3 is
used to select R FBB. V REF is nominally 1 V. For this 5-V example, R FBT = 100 k ohm and R FBB =
24.9 k ohm are
chosen.
10.2.2.3 Inductor Selection
The parameters for selecting the inductor are the inductance and saturation current. The inductance
is based on
the desired peak-to-peak ripple current and is normally chosen to be in the range of 20% to 40% of
the
maximum output current. Experience shows that the best value for inductor ripple current is 30% of
the
maximum load current for systems with a fixed input voltage and 25% for systems with a variable
input voltage
such as the 12 volt battery in a car. Note that when selecting the ripple current for applications
with much smaller
maximum load than the maximum available from the device, the maximum device current must still be
used.
Equation 9  can be used to determine the value of inductance. The constant K is the percentage of
inductor
current ripple. For this example, K = 0.25 was chosen and an inductance of approximately 5.25 uH was
found.
The next standard value of 4.7 uH was selected.
L= fSW A.A,OUT(MAX)
VIN A9OUT
AVOUT
VIN
(9)
The saturation current rating of the inductor must be at least as large as the high-side switch
current limit, I L-HS
(see Section 8.5). This ensures that the inductor does not saturate even during a short circuit on
the output.
When the inductor core material saturates, the inductance falls to a very low value, causing the
inductor current
to rise very rapidly. Although the valley current limit, I L-LS, is designed to reduce the risk of
current run-away, a
saturated inductor can cause the current to rise to high values very rapidly. This can lead to
component damage;
www.ti.com
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021
Copyright (c) 2021 Texas Instruments Incorporated Submit Document Feedback 31
Product Folder Links: LMQ61460-Q1
```

### Page 32

```text
do not allow the inductor to saturate. Inductors with a ferrite core material have very hard
saturation
characteristics, but usually have lower core losses than powdered iron cores. Powdered iron cores
exhibit a soft
saturation, allowing some relaxation in the current rating of the inductor. However, they have more
core losses at
frequencies typically above 1 MHz. In any case, the inductor saturation current must not be less
than the device
high-side current limit, I L-HS (see Section 8.5). To avoid subharmonic oscillation, the inductance
value must not
be less than that given in Equation 10 . The maximum inductance is limited by the minimum current
ripple
required for the current mode control to perform correctly. As a rule-of-thumb, the minimum inductor
ripple
current must be no less than about 10% of the device maximum rated current under nominal conditions.
/0.32 A VOUT
fSW
(10)
Equation 10 assumes that this design must operate with input voltage near or in dropout. If minimum
operating
voltage for this design is high enough to limit duty factor to below 50%, Equation 11 can be used in
place of
Equation 10.
/0.2 A VOUT
fSW
(11)
Note that choosing an inductor that is larger than the minimum inductance calculated using Equation
9 through
Equation 11 results in less output capacitance being needed to limit output ripple but more output
capacitance
being needed to manage large load transients. See Section 10.2.2.4.
10.2.2.4 Output Capacitor Selection
The value of the output capacitor and its ESR determine the output voltage ripple and load transient
performance. The output capacitor is usually determined by the load transient requirements rather
than the
output voltage ripple. Table 10-3 can be used to find the output capacitor and C FF selection for a
few common
applications. Note that a 1-k ohm R FF must be used in series with C FF. In this example, improved
transient
performance is desired giving 2 x 47 uF ceramic as the output capacitor and 22 pF as CFF.
Table 10-3. Recommended Output Ceramic Capacitors and CFF Values
FREQUENCY TRANSIENT
PERFORMANCE
3.3-V OUTPUT 5-V OUTPUT
CERAMIC OUTPUT CAPACITANCE CFF CERAMIC OUTPUT CAPACITANCE CFF
2.1 MHz Minimum 3 x 22 uF 10 pF 2 x 22 uF 22 pF
2.1 MHz Better Transient 2 x 47 uF 33 pF 3 x 22 uF 33 pF
400 kHz Minimum 3 x 47 uF 4.7 pF 2 x 47 uF 10 pF
400 kHz Better Transient 4 x 47 uF 33 pF 3 x 47 uF 33 pF
To minimize ceramic capacitance, a low-ESR electrolytic capacitor can be used in parallel with
minimal ceramic
capacitance. As a starting point for designing with an output electrolytic capacitor, Table 10-4
shows the
recommended output ceramic capacitance CFF values when using an electrolytic capacitor.
Table 10-4. Recommended Electrolytic and Ceramic Capacitor and CFF Values
FREQUENCY TRANSIENT
PERFORMANCE
3.3-V OUTPUT 5-V OUTPUT
COUT CFF COUT CFF
400 kHz Minimum 2 x 47 uF ceramic + 1 x 470 uF, 100 mohm electrolytic 10 pF 3 x 22 uF ceramic + 1 x
470 uF, 100 mohm
electrolytic 10 pF
400 kHz Better Transient 3 x 47 uF ceramic + 2 x 280 uF,100 mohm electrolytic 33 pF 4 x 22 uF
Ceramic + 1 x 560 uF, 100 mohm
electrolytic 22 pF
Most ceramic capacitors deliver far less capacitance than the capacitor's rating indicates. Be sure
to check any
capacitor selected for initial accuracy, temperature derating and voltage derating. Table 10-3 and
Table 10-4
have been generated assuming typical derating for 16 V, X7R Automotive grade capacitors. If lower
voltage,
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021 www.ti.com
32 Submit Document Feedback Copyright (c) 2021 Texas Instruments Incorporated
Product Folder Links: LMQ61460-Q1
```

### Page 33

```text
non-automotive grade, or lower temperature rated capacitors are used, more capacitors than listed
will likely be
needed.
10.2.2.5 Input Capacitor Selection
The ceramic input capacitors provide a low impedance source to the converter in addition to
supplying the ripple
current and isolating switching noise from other circuits. A minimum of 10 uF of ceramic capacitance
is required
on the input of the device. This must be rated for at least the maximum input voltage that the
application
requires; preferably twice the maximum input voltage. This capacitance can be increased to help
reduce input
voltage ripple and maintain the input voltage during load transients. In addition, a small case size
100-nF
ceramic capacitor must be used at each input/ground pin pair, VIN1/PGND1 and VIN2/PGND2, immediately
adjacent to the converter. This provides a high-frequency bypass for the control circuits internal
to the device.
These capacitors also suppress SW node ringing, which reduces the maximum voltage present on the SW
node
and EMI. The two 100 nF must also be rated at 50 V with an X7R or better dielectric. The VQFN-HR
(RJR)
package provides two input voltage pins and two power ground pins on opposite sides of the package.
This
allows the input capacitors to be split, and placed optimally with respect to the internal power
MOSFETs, thus
improving the effectiveness of the input bypassing. In this example, two 4.7- uF and two 100-nF
ceramic
capacitors are used, one at each VIN/PGND location. A single 10- uF can also be used on one side of
the
package.
Many times, it is desirable and necessary to use an electrolytic capacitor on the input in parallel
with the
ceramics. This is especially true if long leads or traces are used to connect the input supply to
the converter. The
moderate ESR of this capacitor can help damp any ringing on the input supply caused by the long
power leads.
The use of this additional capacitor also helps with momentary voltage dips caused by input supplies
with
unusually high impedance.
Most of the input switching current passes through the ceramic input capacitors. The approximate
worst case
RMS value of this current can be calculated from Equation 12 and must be checked against the
manufacturers'
maximum ratings.
IRMS IOUT
2
(12)
10.2.2.6 BOOT Capacitor
The device requires a bootstrap capacitor connected between the CBOOT pin and the SW pin. This
capacitor
stores energy that is used to supply the gate drivers for the high-side power MOSFET. A high-quality
(X7R)
ceramic capacitor of 100 nF and at least 10 V is required.
10.2.2.7 BOOT Resistor
A BOOT resistor can be connected between the CBOOT and RBOOT pins. Unless EMI for the application
being
designed is critical, these two pins can be shorted. A 100 ohm resistor between these pins
eliminates overshoot.
Even with 0 ohm, overshoot and ringing are minimal, less than 2 V if input capacitors are placed
correctly. A boot
resistor of 100 ohm, which corresponds to approximately 2.7 ns SW node rise time and decreases
efficiency by
approximately 0.5% at 2 MHz. To maximize efficiency, 0 ohm is chosen for this example. Under most
circumstances, selecting an RBOOT resistor value above 100 ohm is undesirable since the resulting
small
improvement in EMI is not enough to justify further decreased efficiency.
10.2.2.8 VCC
The VCC pin is the output of the internal LDO used to supply the control circuits of the converter.
This output
requires a 1- uF, 16-V ceramic capacitor connected from VCC to AGND for proper operation. In
general, avoid
loading this output with any external circuitry. However, this output can be used to supply the
pullup for the
power-good function (see Section 9.3.5). A pullup resistor with a value of 100 k ohm is a good
choice in this case.
Note, VCC will remain high when V EN_WAKE< EN < V EN. The nominal output voltage on VCC is 3.3 V. Do
not
short this output to ground or any other external voltage.
www.ti.com
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021
Copyright (c) 2021 Texas Instruments Incorporated Submit Document Feedback 33
Product Folder Links: LMQ61460-Q1
```

### Page 34

```text
10.2.2.9 BIAS
Because VOUT = 5 V in this design, the BIAS pin is tied to V OUT to reduce LDO power loss. The
output voltage is
supplying the LDO current instead of the input voltage. The power saving is I LDO  x  (V IN - V
OUT). The power
saving is more significant when V IN >> V OUT and with higher frequency operation. To prevent V OUT
noise and
transients from coupling to BIAS, a series resistor, 1 ohm to 10 ohm, can be added between V OUT and
BIAS. A
bypass capacitor with a value of 1 uF or higher can be added close to the BIAS pin to filter noise.
Note, the
maximum allowed voltage on the BIAS pin is 16 V.
10.2.2.10 CFF and RFF Selection
A feedforward capacitor, C ff, is used to improve phase margin and transient response of circuits
which have
output capacitors with low ESR. Since this capacitor can conduct noise from the output of the
circuit directly to
the FB node of the IC, a 1-k ohm resistor, R ff, must be placed in series with Cff. If the ESR zero
of the output
capacitor is below 200 kHz, no Cff should be used.
If output voltage is less than 2.5 V, Cff has little effect so can be omitted. If output voltage is
greater than 14 V, Cff
must not be used since it will introduce too much gain at higher frequencies.
10.2.2.11 External UVLO
In some cases, an input UVLO level different than that provided internal to the device is needed.
This can be
accomplished by using the circuit shown in Figure 10-4 . The input voltage at which the device turns
on is
designated VON while the turnoff voltage is V OFF. First, a value for R ENB is chosen in the range
of 10 k ohm to 100
kohm, then Equation 14 is used to calculate R ENT and V OFF. RENB is typically set based on how much
current this
voltage divider must consume. RENB can be calculated using Equation 13.
RENB = IDIVIDER A9ON
VEN A9IN
(13)
RENT
RENB
EN/SYNC
AGND
VIN
Figure 10-4. UVLO Using EN
RENT = VON
VEN
VOFF = (1 A9EN-HYST)
A1  A5ENB
VON A
(14)
where
- V ON is VIN turnon voltage
- V OFF is VIN turnoff voltage
- I DIVIDER is voltage divider current
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021 www.ti.com
34 Submit Document Feedback Copyright (c) 2021 Texas Instruments Incorporated
Product Folder Links: LMQ61460-Q1
```

### Page 35

```text
10.2.3 Application Curves
Unless otherwise specified, the following conditions apply: VIN = 13.5 V, TA = 25 degC. The circuit
is shown in Figure
10-1, with the appropriate BOM from Table 10-5.
Output Current (A)
Efficiency (%)
0.001 0.010.02 0.05 0.1 0.2 0.5 1 2 3 45 7 10
60%
65%
70%
75%
80%
85%
90%
95%
100%
LM61
VIN = 8 V
VIN = 13.5 V
VIN = 24 V
VOUT = 3.3 V FSW = 400 kHz Auto Mode
Figure 10-5. LMQ61460-Q1 Efficiency
Output Current (A)
Efficiency (%)
0 1 2 3 4 5 6 7
50%
55%
60%
65%
70%
75%
80%
85%
90%
95%
100%
LM61
VIN = 8 V
VIN = 13.5 V
VIN = 24 V
VOUT = 3.3 V FSW = 400 kHz FPWM Mode
Figure 10-6. LMQ61460-Q1 Efficiency
Output Current (A)
Efficiency (%)
0.001 0.010.02 0.05 0.1 0.2 0.5 1 2 3 45 7 10
60%
65%
70%
75%
80%
85%
90%
95%
100%
LM61
VIN = 8 V
VIN = 13.5 V
VIN = 24 V
VOUT = 3.3 V FSW = 2100 kHz AUTO Mode
Figure 10-7. LMQ61460-Q1 Efficiency
Output Current (A)
Efficiency (%)
0 1 2 3 4 5 6 7
50%
55%
60%
65%
70%
75%
80%
85%
90%
95%
100%
LM61
VIN  = 8 V
VIN  = 13.5 V
VIN  = 24 V
VOUT = 3.3 V FSW = 2100 kHz FPWM Mode
Figure 10-8. LMQ61460-Q1 Efficiency
Load Current (A)
Efficiency (%)
0.0001 0.001 0.01 0.1 0.2 0.5 1 2 3 5 710
60%
65%
70%
75%
80%
85%
90%
95%
100%
LM61
VIN = 8 V
VIN = 13.5 V
VIN = 24 V
VOUT = 5 V FSW = 400 kHz AUTO Mode
Figure 10-9. LMQ61460-Q1 Efficiency
Load Current (A)
Efficiency (%)
0 1 2 3 4 5 6 7
50%
55%
60%
65%
70%
75%
80%
85%
90%
95%
100%
LM61
VIN = 8 V
VIN = 13.5 V
VIN = 24 V
VOUT = 5 V FSW = 400 kHz FPWM Mode
Figure 10-10. LMQ61460-Q1 Efficiency
www.ti.com
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021
Copyright (c) 2021 Texas Instruments Incorporated Submit Document Feedback 35
Product Folder Links: LMQ61460-Q1
```

### Page 36

```text
Load Current (A)
Efficiency (%)
0.001 0.010.02 0.05 0.1 0.2 0.5 1 2 3 45 7 10
60%
65%
70%
75%
80%
85%
90%
95%
100%
LM61
VIN = 8 V
VIN = 13.5 V
VIN = 24 V
VOUT = 5 V FSW = 2100 kHz AUTO Mode
Figure 10-11. LMQ61460-Q1 Efficiency
Load Current (A)
Efficiency (%)
0 1 2 3 4 5 6 7
50%
55%
60%
65%
70%
75%
80%
85%
90%
95%
100%
LM61
VIN = 8 V
VIN = 13.5 V
VIN = 24 V
VOUT = 5 V FSW = 2100 kHz FPWM Mode
Figure 10-12. LMQ61460-Q1 Efficiency
Output Current (A)
Output Voltage (V)
0 1 2 3 4 5 6 7
3.29
3.31
3.33
3.35
3.37
SNVS
VIN = 8 V
VIN = 13.5 V
VIN = 24 V
VOUT = 3.3 V FSW = 400 kHz Auto Mode
Figure 10-13. LMQ61460-Q1 Load and Line
Regulation
Output Current (A)
Output Voltage (V)
0 1 2 3 4 5 6 7
3.29
3.31
3.33
3.35
3.37
SNVS
VIN = 8 V
VIN = 13.5 V
VIN = 24 V
VOUT = 3.3 V FSW = 400 kHz FPWM Mode
Figure 10-14. LMQ61460-Q1 Load and Line
Regulation
Output Current (A)
Output Voltage (V)
0 1 2 3 4 5 6 7
3.29
3.31
3.33
3.35
3.37
SNVS
VIN = 8 V
VIN = 13.5 V
VIN = 24 V
VOUT = 3.3 V FSW = 2100 kHz AUTO Mode
Figure 10-15. LMQ61460-Q1 Load and Line
Regulation
Output Current (A)
Output Voltage (V)
0 1 2 3 4 5 6 7
3.29
3.31
3.33
3.35
3.37
SNVS
VIN = 8 V
VIN = 13.5 V
VIN = 24 V
VOUT = 3.3 V FSW = 2100 kHz FPWM Mode
Figure 10-16. LMQ61460-Q1 Load and Line
Regulation
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021 www.ti.com
36 Submit Document Feedback Copyright (c) 2021 Texas Instruments Incorporated
Product Folder Links: LMQ61460-Q1
```

### Page 37

```text
Output Current (A)
Output Voltage (V)
0 1 2 3 4 5 6 7
4.95
4.97
4.99
5.01
5.03
5.05
5.07
5.09
5.11
SNVS
VIN = 8 V
VIN = 13.5 V
VIN = 24 V
VOUT = 5 V FSW = 400 kHz AUTO Mode
Figure 10-17. LMQ61460-Q1 Load and Line
Regulation
Output Current (A)
Output Voltage (V)
0 1 2 3 4 5 6 7
4.95
4.97
4.99
5.01
5.03
5.05
5.07
5.09
5.11
SNVS
VIN = 8 V
VIN = 13.5 V
VIN = 24 V
VOUT = 5 V FSW = 400 kHz FPWM Mode
Figure 10-18. LMQ61460-Q1 Load and Line
Regulation
Output Current (A)
Output Voltage (V)
0 1 2 3 4 5 6 7
4.95
4.97
4.99
5.01
5.03
5.05
5.07
5.09
5.11
SNVS
VIN = 8 V
VIN = 13.5 V
VIN = 24 V
VOUT = 5 V FSW = 2100 kHz AUTO Mode
Figure 10-19. LMQ61460-Q1 Load and Line
Regulation
Output Current (A)
Output Voltage (V)
0 1 2 3 4 5 6 7
4.95
4.97
4.99
5.01
5.03
5.05
5.07
5.09
5.11
SNVS
VIN = 8 V
VIN = 13.5 V
VIN = 24 V
VOUT = 5 V FSW = 2100 kHz FPWM Mode
Figure 10-20. LMQ61460-Q1 Load and Line
Regulation
Input Voltage (V)
Output Voltage (V)
3 3.25 3.5 3.75 4 4.25 4.5 4.75 5
2.5
2.75
3
3.25
3.5
SNVS
IOUT = 0.01 A
IOUT = 3 A
IOUT = 6 A
VOUT = 3.3 V FSW = 400 kHz AUTO Mode
Figure 10-21. LMQ61460-Q1 Dropout Curve
Input Voltage (V)
Output Voltage (V)
3 3.25 3.5 3.75 4 4.25 4.5 4.75 5
2.5
2.75
3
3.25
3.5
SNVS
IOUT = 0.01 A
IOUT = 3 A
IOUT = 6 A
VOUT = 3.3 V FSW = 2100 kHz AUTO Mode
Figure 10-22. LMQ61460-Q1 Dropout Curve
www.ti.com
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021
Copyright (c) 2021 Texas Instruments Incorporated Submit Document Feedback 37
Product Folder Links: LMQ61460-Q1
```

### Page 38

```text
Input Voltage (V)
Output Voltage (V)
4 4.2 4.4 4.6 4.8 5 5.2 5.4 5.6 5.8 6
3
3.5
4
4.5
5
5.5
6
SNVS
IOUT = 0.01 A
IOUT = 3 A
IOUT = 6 A
VOUT = 5 V FSW = 400 kHz AUTO Mode
Figure 10-23. LMQ61460-Q1 Dropout Curve
Input Voltage (V)
Ouput Voltage (V)
4 4.2 4.4 4.6 4.8 5 5.2 5.4 5.6 5.8 6
3
3.5
4
4.5
5
5.5
6
SNVS
IOUT = 0.01 A
IOUT = 3 A
IOUT = 6 A
VOUT = 5 V FSW = 2100 kHz AUTO Mode
Figure 10-24. LMQ61460-Q1 Dropout Curve
Input Voltage (V)
Switching Frequency (Hz)
3 3.25 3.5 3.75 4 4.25 4.5
0
5E+4
1E+5
1.5E+5
2E+5
2.5E+5
3E+5
3.5E+5
4E+5
4.5E+5
5E+5
snvs
IOUT = 3 A
IOUT = 6 A
VOUT = 3.3 V FSW = 400 kHz AUTO Mode
Figure 10-25. LMQ61460-Q1 Frequency Dropout
Curve
Input Voltage (V)
Switching Frequency (Hz)
3 3.5 4 4.5 5
0
2.5E+5
5E+5
7.5E+5
1E+6
1.25E+6
1.5E+6
1.75E+6
2E+6
2.25E+6
2.5E+6
snvs
IOUT = 3 A
IOUT = 6 A
VOUT = 3.3 V FSW = 2100 kHz AUTO Mode
Figure 10-26. LMQ61460-Q1 Frequency Dropout
Curve
Input Voltage (V)
Switching Frequency (Hz)
5 5.25 5.5 5.75 6
0
5E+4
1E+5
1.5E+5
2E+5
2.5E+5
3E+5
3.5E+5
4E+5
4.5E+5
5E+5
snvs
IOUT = 3 A
IOUT = 6 A
VOUT = 5 V FSW = 400 kHz AUTO Mode
Figure 10-27. LMQ61460-Q1 Frequency Dropout
Curve
Input Voltage (V)
Switching Frequency (Hz)
5 5.5 6 6.5 7
0
2.5E+5
5E+5
7.5E+5
1E+6
1.25E+6
1.5E+6
1.75E+6
2E+6
2.25E+6
2.5E+6
snvs
IOUT = 3 A
IOUT = 6 A
VOUT = 5 V FSW = 2100 kHz AUTO Mode
Figure 10-28. LMQ61460-Q1 Frequency Dropout
Curve
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021 www.ti.com
38 Submit Document Feedback Copyright (c) 2021 Texas Instruments Incorporated
Product Folder Links: LMQ61460-Q1
```

### Page 39

```text
VOUT Ripple
VSW
(2 A/DIV)
Time (20 us/DIV)
IINDUCTOR
(10 mV/DIV)
(5 V/DIV)
VOUT = 5 V FSW = 2100 kHz AUTO Mode
IOUT = 50 mA VIN = 13.5 V
Figure 10-29. LMQ61460-Q1 Switching Waveform
and VOUT Ripple
VOUT Ripple
VSW
(2 A/DIV)
Time (2 us/DIV)
IINDUCTOR
(10 mV/DIV)
(5 V/DIV)
VOUT = 5 V FSW = 2100 kHz FPWM Mode
IOUT = 50 mA VIN = 13.5 V
Figure 10-30. LMQ61460-Q1 Switching Waveform
and VOUT Ripple
VOUT
VPG
(1 A/DIV)
Time (1 ms/DIV)
IINDUCTOR
(2 V/DIV)
(5 V/DIV)
VEN
(5 V/DIV)
VOUT = 5 V FSW = 2100 kHz AUTO Mode
IOUT = 50 mA VIN = 13.5 V
Figure 10-31. LMQ61460-Q1 Start-up with 50-mA
Load
VOUT
VPG
(1 A/DIV)
Time (1 ms/DIV)
IINDUCTOR
(2 V/DIV)
(5 V/DIV)
VEN
(5 V/DIV)
VOUT = 5 V FSW = 2100 kHz FPWM Mode
IOUT = 50 mA VIN = 13.5 V
Figure 10-32. LMQ61460-Q1 Start-up with 50-mA
Load
VOUT
VPG
(1 A/DIV)
Time (1 ms/DIV)
IINDUCTOR
(2 V/DIV)
(5 V/DIV)
VEN
(5 V/DIV)
VOUT = 3.3 V FSW = 2100 kHz FPWM Mode
IOUT = 3.25 A VIN = 13.5 V
Figure 10-33. LMQ61460-Q1 Start-up with 3.25-A
Load
VOUT
(2 A/DIV)
Time (200 us/DIV)
IINDUCTOR
(2 V/DIV)
VOUT = 5 V FSW = 2100 kHz FPWM Mode
IOUT = 5 A to Short Circuit VIN = 13.5 V
Figure 10-34. LMQ61460-Q1 Short Circuit
Protection
www.ti.com
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021
Copyright (c) 2021 Texas Instruments Incorporated Submit Document Feedback 39
Product Folder Links: LMQ61460-Q1
```

### Page 40

```text
VOUT
(2 A/DIV)
Time (20 ms/DIV)
IINDUCTOR
(2 V/DIV)
VOUT = 5 V FSW = 2100 kHz FPWM Mode
IOUT = Short Circuit to 5 A VIN = 13.5 V
Figure 10-35. LMQ61460-Q1 Short Circuit Recovery
VOUT
(2 A/DIV)
Time (20 ms/DIV)
IINDUCTOR
(500 mV/DIV)
VOUT = 5 V FSW = 2100 kHz FPWM Mode
IOUT = Short Circuit VIN = 13.5 V
Figure 10-36. LMQ61460-Q1 Short Circuit
Performance
VOUT
(1 A/DIV)
Time (2 ms/DIV)
IINDUCTOR
(2 V/DIV)
VIN
(5 V/DIV)
VOUT = 5 V FSW = 2100 kHz FPWM Mode
IOUT = 4 A VIN = 13.5 V to 4 V to 13.5 V
Figure 10-37. LMQ61460-Q1 Graceful Recovery
from Dropout
VOUT
(2 A/DIV)
Time (50 us/DIV)
IOUT
(200 mV/DIV)
VOUT = 5 V FSW = 400 kHz AUTO Mode
IOUT = 0 A to 6 A to
0 A
VIN = 13.5 V TR = TF = 6 us
Figure 10-38. LMQ61460-Q1 Load Transient
VOUT
(2 A/DIV)
Time (50 us/DIV)
IOUT
(200 mV/DIV)
VOUT = 5 V FSW = 400 kHz FPWM Mode
IOUT = 0 A to 6 A to
0 A
VIN = 13.5 V TR = TF = 6 us
Figure 10-39. LMQ61460-Q1 Load Transient
VOUT
(2 A/DIV)
Time (50 us/DIV)
IOUT
(200 mV/DIV)
VOUT = 5 V FSW = 400 kHz AUTO Mode
IOUT = 2 A to 5 A to
2 A
VIN = 13.5 V TR = TF = 3 us
Figure 10-40. LMQ61460-Q1 Load Transient
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021 www.ti.com
40 Submit Document Feedback Copyright (c) 2021 Texas Instruments Incorporated
Product Folder Links: LMQ61460-Q1
```

### Page 41

```text
VOUT
(2 A/DIV)
Time (50 us/DIV)
IOUT
(200 mV/DIV)
VOUT = 5 V FSW = 400 kHz AUTO Mode
IOUT = 50 mA to 6 A
to 50 mA
VIN = 13.5 V TR = TF = 6 us
Figure 10-41. LMQ61460-Q1 Load Transient
VOUT
(2 A/DIV)
Time (50 us/DIV)
IOUT
(200 mV/DIV)
VOUT = 3.3 V FSW = 400 kHz AUTO Mode
IOUT = 0 A to 6 A to
0 A
VIN = 13.5 V TR = TF = 6 us
Figure 10-42. LMQ61460-Q1 Load Transient
VOUT
(2 A/DIV)
Time (50 us/DIV)
IOUT
(200 mV/DIV)
VOUT = 3.3 V FSW = 400 kHz AUTO Mode
IOUT = 2 A to 4 A to
2 A
VIN = 13.5 V TR = TF = 2 us
Figure 10-43. LMQ61460-Q1 Load Transient
VOUT
(2 A/DIV)
Time (50 us/DIV)
IOUT
(200 mV/DIV)
VOUT = 5 V FSW = 2100 kHz AUTO Mode
IOUT = 0 A to 6 A to
0 A
VIN = 13.5 V TR = TF = 6 us
Figure 10-44. LMQ61460-Q1 Load Transient
VOUT
(2 A/DIV)
Time (50 us/DIV)
IOUT
(200 mV/DIV)
VOUT = 5 V FSW = 2100 kHz FPWM Mode
IOUT = 0 A to 6 A to
0 A
VIN = 13.5 V TR = TF = 6 us
Figure 10-45. LMQ61460-Q1 Load Transient
FSW = 400 kHz VOUT = 5 V IOUT = 5 A
Frequency Tested: 150 kHz to 30 MHz
Figure 10-46. Conducted EMI versus CISPR25
Limits (Yellow: Peak Signal, Blue: Average Signal)
www.ti.com
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021
Copyright (c) 2021 Texas Instruments Incorporated Submit Document Feedback 41
Product Folder Links: LMQ61460-Q1
```

### Page 42

```text
VOUT = 5 V FSW = 400 kHz IOUT = 5 A
Frequency Tested: 30 MHz to 108 MHz
Figure 10-47. Conducted EMI versus CISPR25
Limits (Yellow: Peak Signal, Blue: Average Signal)

VOUT = 5 V FSW = 400 kHz IOUT = 5 A
Frequency Tested: 150 kHz to 30 MHz
Figure 10-48. Radiated EMI Rod versus CISPR25
Limits
VOUT = 5 V FSW = 400 kHz IOUT = 5 A
Frequency Tested: 30 MHz to 300 MHz
Figure 10-49. Radiated EMI Bicon Vertical versus
CISPR25 Limits
VOUT = 5 V FSW = 400 kHz IOUT = 5 A
Frequency Tested: 30 MHz to 300 MHz
Figure 10-50. Radiated EMI Bicon Horizontal
versus CISPR25 Limits
VOUT = 5 V FSW = 400 kHz IOUT = 5 A
Frequency Tested: 300 MHz to 1 GHz
Figure 10-51. Radiated EMI Log Vertical versus
CISPR25 Limits
VOUT = 5 V FSW = 400 kHz IOUT = 5 A
Frequency Tested: 300 MHz to 1 GHz
Figure 10-52. Radiated EMI Log Horizontal versus
CISPR25 Limits
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021 www.ti.com
42 Submit Document Feedback Copyright (c) 2021 Texas Instruments Incorporated
Product Folder Links: LMQ61460-Q1
```

### Page 43

```text
IN+
IN-
CF3=2.2uF
CF4= 2.2uF
744316220
L=2.2uH
VIN
GND
CF5=2.2uF
CF6=2.2uF
CF1=470nF
CF2=470nF

Figure 10-53. Recommended Input EMI Filter
FSW = 2100 kHz VOUT = 5 V IOUT = 5 A
Frequency Tested: 150 kHz to 30 MHz
Figure 10-54. Conducted EMI versus CISPR25
Limits (Yellow: Peak Signal, Blue: Average Signal)
FSW = 2100 kHz VOUT = 5 V IOUT = 5 A
Frequency Tested: 30 MHz to 108 MHz
Figure 10-55. Conducted EMI versus CISPR25
Limits (Yellow: Peak Signal, Blue: Average Signal)
VOUT = 5 V FSW = 2.1 MHz IOUT = 4 A
Frequency Tested: 150 kHz to 30 MHz
Figure 10-56. Radiated EMI Red versus CISPR25
Limits
VOUT = 5 V FSW = 2.1 MHz IOUT = 4 A
Frequency Tested: 30 kHz to 300 MHz
Figure 10-57. Radiated EMI Bicon Vertical versus
CISPR25 Limits
VOUT = 5 V FSW = 2.1 MHz IOUT = 4 A
Frequency Tested: 30 MHz to 300 MHz
Figure 10-58. Radiated EMI Bicon Horizontal
versus CISPR25 Limits
www.ti.com
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021
Copyright (c) 2021 Texas Instruments Incorporated Submit Document Feedback 43
Product Folder Links: LMQ61460-Q1
```

### Page 44

```text
VOUT = 5 V FSW = 2.1 MHz IOUT = 4 A
Frequency Tested: 30 MHz to 1 GHz
Figure 10-59. Radiated EMI Log Vertical versus
CISPR25 Limits
VOUT = 5 V FSW = 2.1 MHz IOUT = 4 A
Frequency Tested: 300 MHz to 1 GHz
Figure 10-60. Radiated EMI Log Horizontal versus
CISPR25 Limits
IN+
IN-
CF3=2.2uF
CF4= 2.2uF
74438356010
L=1uH
VIN
GND
CF5=2.2uF
CF6=2.2uF
CF1=470nF
CF2=470nF
FSW = 2100 kHz
Figure 10-61. Recommended Input EMI Filter
Table 10-5. BOM for Typical Application Curves
VOUT FREQUENCY RFBB COUT CIN + CHF L CFF
3.3 V 2100 kHz 43.2 kohm 3 x 22 uF 2 x 4.7 uF + 2 x 100 nF 1.5 uH (MAPI
4020HT) 22 pF
5 V 2100 kHz 24.9 kohm 2 x 22 uF 2 x 4.7 uF + 2 x 100 nF 1.5 uH (MAPI
4020HT) 22 pF
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021 www.ti.com
44 Submit Document Feedback Copyright (c) 2021 Texas Instruments Incorporated
Product Folder Links: LMQ61460-Q1
```

### Page 45

```text
11 Power Supply Recommendations
The characteristics of the input supply must be compatible with Section 8.1 and Section 8.3 in this
data sheet. In
addition, the input supply must be capable of delivering the required input current to the loaded
converter. The
average input current can be estimated with Equation 15.
IIN = VIN A
VOUT A,OUT
(15)
where
-  is the efficiency
If the converter is connected to the input supply through long wires or PCB traces, special care is
required to
achieve good performance. The parasitic inductance and resistance of the input cables can have an
adverse
effect on the operation of the converter. The parasitic inductance, in combination with the low-ESR,
ceramic
input capacitors, can form an under-damped resonant circuit, resulting in overvoltage transients at
the input to
the converter or tripping UVLO. The parasitic resistance can cause the voltage at the VIN pin to dip
whenever a
load transient is applied to the output. If the application is operating close to the minimum input
voltage, this dip
can cause the converter to momentarily shutdown and reset. The best way to solve these kind of
issues is to
reduce the distance from the input supply to the converter and use an aluminum input capacitor in
parallel with
the ceramics. The moderate ESR of this type of capacitor helps damp the input resonant circuit and
reduce any
overshoot or undershoot at the input. A value in the range of 20 uF to 100 uF is usually sufficient
to provide input
damping and help hold the input voltage steady during large load transients.
In some cases, a transient voltage suppressor (TVS) is used on the input of converters. One class of
this device
has a snap-back characteristic (thyristor type). The use of a device with this type of
characteristic is not
recommended. When the TVS fires, the clamping voltage falls to a very low value. If this voltage is
less than the
output voltage of the converter, the output capacitors discharge through the device back to the
input. This
uncontrolled current flow can damage the TVS and cause large input transients.
The input voltage must not be allowed to fall below the output voltage. In this scenario, such as a
shorted input
test, the output capacitors discharge through the internal parasitic diode found between the VIN and
SW pins of
the device. During this condition, the current can become uncontrolled, possibly causing damage to
the device. If
this scenario is considered likely, then a Schottky diode between the input supply and the output
must be used.
www.ti.com
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021
Copyright (c) 2021 Texas Instruments Incorporated Submit Document Feedback 45
Product Folder Links: LMQ61460-Q1
```

### Page 46

```text
12 Layout
12.1 Layout Guidelines
The PCB layout of any DC-DC converter is critical to the optimal performance of the design. Bad PCB
layout can
disrupt the operation of an otherwise good schematic design. Even if the converter regulates
correctly, bad PCB
layout can mean the difference between a robust design and one that cannot be mass produced.
Furthermore,
the EMI performance of the converter is dependent on the PCB layout, to a great extent. In a buck
converter, the
most critical PCB feature is the loop formed by the input capacitor or capacitors and power ground,
as shown in
Figure 12-1. This loop carries large transient currents that can cause large transient voltages when
reacting with
the trace inductance. These unwanted transient voltages disrupt the proper operation of the
converter. Because
of this, the traces in this loop must be wide and short, and the loop area as small as possible to
reduce the
parasitic inductance. Figure 12-2 shows a recommended layout for the critical components for the
circuit of the
device.
- Place the input capacitor or capacitors as close as possible input pin pairs: VIN1 to PGND1 and
VIN2 to
PGND2. Each pair of pins are adjacent, simplifying the input capacitor placement. With the VQFN-HR
package, there are two VIN/PGND pairs on either side of the package. This provides for a symmetrical
layout
and helps minimize switching noise and EMI generation. Use a wide VIN plane on a lower layer to
connect
both of the VIN pairs together to the input supply.
- Place bypass capacitor for VCC close to the VCC pin and AGND pins: This capacitor must routed with
short,
wide traces to the VCC and AGND pins.
- Use wide traces for the CBOOT capacitor: Place the CBOOT capacitor as close to the device with
short, wide
traces to the CBOOT and SW pins. It is important to route the SW connection under the device through
the
gap between VIN2 and RBOOT pins, reducing exposed SW node area. If an RBOOT resistor is used, place
as close as possible to CBOOT and RBOOT pins. If high efficiency is desired, RBOOT and CBOOT pins
can
be shorted. This short must be placed as close as possible to RBOOT and CBOOT pins as possible.
- Place the feedback divider as close as possible to the FB pin of the device: Place RFBB, RFBT, and
CFF, if
used, physically close to the device. The connections to FB and AGND through RFBB must be short and
close
to those pins on the device. The connection to VOUT can be somewhat longer. However, this latter
trace must
not be routed near any noise source (such as the SW node) that can capacitively couple into the
feedback
path of the converter.
- Layer 2 of the PCB must be a ground plane: This plane acts as a noise shield and a heat
dissipation path.
Using layer 2 reduces the inclosed area in the input circulating current in the input loop, reducing
inductance.
- Provide wide paths for VIN, VOUT, and GND: These paths must be wide and direct as possible to
reduce any
voltage drops on the input or output paths of the converter and maximizes efficiency.
- Provide enough PCB area for proper heat sinking: Enough copper area must be used to ensure a low
RJA,
commensurate with the maximum load current and ambient temperature. Make the top and bottom PCB
layers with two-ounce copper and no less than one ounce. If the PCB design uses multiple copper
layers
(recommended), thermal vias can also be connected to the inner layer heat-spreading ground planes.
Note
that the package of this device dissipates heat through all pins. Wide traces must be used for all
pins except
where noise considerations dictate minimization of area.
- Keep switch area small: Keep the copper area connecting the SW pin to the inductor as short and
wide as
possible. At the same time, the total area of this node must be minimized to help reduce radiated
EMI.
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021 www.ti.com
46 Submit Document Feedback Copyright (c) 2021 Texas Instruments Incorporated
Product Folder Links: LMQ61460-Q1
```

### Page 47

```text
CIN_HF2
CIN_HF1
HS
FET
LS
FET
SW
VIN1 VIN2
PGND1 PGND2
Figure 12-1. Input Current Loop
12.1.1 Ground and Thermal Considerations
As mentioned above, TI recommends using one of the middle layers as a solid ground plane. A ground
plane
provides shielding for sensitive circuits and traces. It also provides a quiet reference potential
for the control
circuitry. The AGND and PGND pins must be connected to the ground planes using vias next to the
bypass
capacitors. PGND pins are connected directly to the source of the low-side MOSFET switch, and also
connected
directly to the grounds of the input and output capacitors. The PGND net contains noise at the
switching
frequency and can bounce due to load variations. The PGND trace, as well as the VIN and SW traces,
must be
constrained to one side of the ground planes. The other side of the ground plane contains much less
noise and
must be used for sensitive routes.
TI recommends providing adequate device heat sinking by using vias near ground and V IN to connect
to the
system ground plane or V IN strap, both of which dissipate heat. Use as much copper as possible, for
system
ground plane, on the top and bottom layers for the best heat dissipation. Use a four-layer board
with the copper
thickness for the four layers, starting from the top as: 2 oz / 1 oz / 1 oz / 2 oz. A four-layer
board with enough
copper thickness and proper layout, provides low current conduction impedance, proper shielding, and
lower
thermal resistance.
www.ti.com
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021
Copyright (c) 2021 Texas Instruments Incorporated Submit Document Feedback 47
Product Folder Links: LMQ61460-Q1
```

### Page 48

```text
12.2 Layout Example
1 2 3 4 5
6
7
8
91011
12
13
14
Top Trace/Pour
CIN2
CIN1
CIN_HF1
RFBB
RFBT
RFF
RT
REN
COUT2 COUT1
CVCC
CBOOT
RBOOT
CFF
INNER GND PLANE +/- LAYER 2
GND POUR
Inner GDN Plane
VIN Strap on Inner Layer
VIN
VIN
GND POUR
GND POUR
GND POUR
VOUT
GND POUR
VIA to Signal Layer
INDUCTOR
LMQ61460-Q1
VIA to GND
VIA to VIN Strap
VOUT
VOUT
CIN_HF2
VIA to Feedback
divider
VIAS to BIAS
Figure 12-2. Layout Example
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021 www.ti.com
48 Submit Document Feedback Copyright (c) 2021 Texas Instruments Incorporated
Product Folder Links: LMQ61460-Q1
```

### Page 49

```text
13 Device and Documentation Support
13.1 Documentation Support
13.1.1 Related Documentation
For related documentation see the following:
- Texas Instruments, Designing High Performance, Low-EMI, Automotive Power Supplies Application
Report
- Texas Instruments, LMQ61460-Q1 EVM User's Guide
- Texas Instruments, 30 W Power for Automotive Dual USB Type-C Charge Port Reference Design
- Texas Instruments, EMI Filter Components and Their Nonidealities for Automotive DC/DC Regulators
Technical Brief
- Texas Instruments, AN-2020 Thermal Design by Insight, Not Hindsight Application Report
- Texas Instruments Optimizing the Layout for the TPS54424/TPS54824 HotRod QFN Package for Thermal
Performance Application Report
- Texas Instruments, AN-2162 Simple Success With Conducted EMI From DC-DC Converters Application
Report
- Texas Instruments, Practical Thermal Design With DC/DC Power Modules Application Report
13.2 Receiving Notification of Documentation Updates
To receive notification of documentation updates, navigate to the device product folder on ti.com.
Click on
Subscribe to updates  to register and receive a weekly digest of any product information that has
changed. For
change details, review the revision history included in any revised document.
13.3 Support Resources
TI E2E (TM) support forums  are an engineer's go-to source for fast, verified answers and design
help - straight
from the experts. Search existing answers or ask your own question to get the quick design help you
need.
Linked content is provided "AS IS" by the respective contributors. They do not constitute TI
specifications and do
not necessarily reflect TI's views; see TI's Terms of Use.
13.4 Trademarks
Hotrod(TM) and TI E2E(TM) are trademarks of Texas Instruments.
All trademarks are the property of their respective owners.
13.5 Electrostatic Discharge Caution
This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated
circuits be handled
with appropriate precautions. Failure to observe proper handling and installation procedures can
cause damage.
ESD damage can range from subtle performance degradation to complete device failure. Precision
integrated circuits may
be more susceptible to damage because very small parametric changes could cause the device not to
meet its published
specifications.
13.6 Glossary
TI Glossary This glossary lists and explains terms, acronyms, and definitions.
14 Mechanical, Packaging, and Orderable Information
The following pages include mechanical, packaging, and orderable information. This information is
the most
current data available for the designated devices. This data is subject to change without notice and
revision of
this document. For browser-based versions of this data sheet, refer to the left-hand navigation.
www.ti.com
LMQ61460-Q1
SNVSBP4C - MARCH 2020 - REVISED JANUARY 2021
Copyright (c) 2021 Texas Instruments Incorporated Submit Document Feedback 49
Product Folder Links: LMQ61460-Q1
```

### Page 50

```text
PACKAGE OPTION ADDENDUM
www.ti.com 9-Nov-2025
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
Op temp ( degC) Part marking
(6)
LMQ61460AASQRJRRQ1 Active Production VQFN-HR (RJR) | 14 3000 | LARGE T&R Yes SN Level-2-260C-1 YEAR
-40 to 150 Q6146Q
AAS
LMQ61460AASQRJRRQ1.A Active Production VQFN-HR (RJR) | 14 3000 | LARGE T&R Yes SN Level-2-260C-1
YEAR -40 to 150 Q6146Q
AAS
LMQ61460AFSQRJRRQ1 Active Production VQFN-HR (RJR) | 14 3000 | LARGE T&R Yes SN Level-2-260C-1 YEAR
-40 to 150 Q6146Q
AFS
LMQ61460AFSQRJRRQ1.A Active Production VQFN-HR (RJR) | 14 3000 | LARGE T&R Yes SN Level-2-260C-1
YEAR -40 to 150 Q6146Q
AFS

(1) Status:  For more details on status, see our product life cycle.

(2) Material type:  When designated, preproduction parts are prototypes/experimental devices, and
are not yet approved or released for full production. Testing and final process, including without
limitation quality assurance,
reliability performance testing, and/or process qualification, may not yet be complete, and this
item is subject to further changes or possible discontinuation. If available for ordering, purchases
will be subject to an additional
waiver at checkout, and are intended for early internal evaluation purposes only. These items are
sold without warranties of any kind.

(3) RoHS values:  Yes, No, RoHS Exempt. See the TI RoHS Statement for additional information and
value definition.

(4) Lead finish/Ball material:  Parts may have multiple material finish options. Finish options are
separated by a vertical ruled line. Lead finish/Ball material values may wrap to two lines if the
finish value exceeds the maximum
column width.

(5) MSL rating/Peak reflow:  The moisture sensitivity level ratings and peak solder (reflow)
temperatures. In the event that a part has multiple moisture sensitivity ratings, only the lowest
level per JEDEC standards is shown.
Refer to the shipping label for the actual reflow temperature that will be used to mount the part to
the printed circuit board.

(6) Part marking:  There may be an additional marking, which relates to the logo, the lot trace code
information, or the environmental category of the part.

Multiple part markings will be inside parentheses. Only one part marking contained in parentheses
and separated by a "~" will appear on a part. If a line is indented then it is a continuation of the
previous line and the two
combined represent the entire part marking for that device.

Important Information and Disclaimer:The information provided on this page represents TI's knowledge
and belief as of the date that it is provided. TI bases its knowledge and belief on information
provided by third parties, and
makes no representation or warranty as to the accuracy of such information. Efforts are underway to
better integrate information from third parties. TI has taken and continues to take reasonable steps
to provide representative
and accurate information but may not have conducted destructive testing or chemical analysis on
incoming materials and chemicals. TI and TI suppliers consider certain information to be
proprietary, and thus CAS numbers
and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of
the TI part(s) at issue in this document sold by TI to Customer on an annual basis.
Addendum-Page 1
```

### Page 51

```text
PACKAGE OPTION ADDENDUM
www.ti.com 9-Nov-2025

OTHER QUALIFIED VERSIONS OF LMQ61460-Q1 :
- Catalog : LMQ61460
 NOTE: Qualified Version Definitions:
- Catalog - TI's standard catalog product
Addendum-Page 2
```

### Page 52

```text
TAPE AND REEL INFORMATION
*All dimensions are nominal
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
LMQ61460AASQRJRRQ1 VQFN-
HR
RJR 14 3000 330.0 12.4 3.8 4.3 1.15 8.0 12.0 Q2
LMQ61460AFSQRJRRQ1 VQFN-
HR
RJR 14 3000 330.0 12.4 3.8 4.3 1.15 8.0 12.0 Q2
PACKAGE MATERIALS INFORMATION
www.ti.com 5-Jan-2021
Pack Materials-Page 1
```

### Page 53

```text
*All dimensions are nominal
Device Package Type Package Drawing Pins SPQ Length (mm) Width (mm) Height (mm)
LMQ61460AASQRJRRQ1 VQFN-HR RJR 14 3000 367.0 367.0 38.0
LMQ61460AFSQRJRRQ1 VQFN-HR RJR 14 3000 367.0 367.0 38.0
PACKAGE MATERIALS INFORMATION
www.ti.com 5-Jan-2021
Pack Materials-Page 2
```

### Page 54

```text
AA
www.ti.com
PACKAGE OUTLINE
C1.0
0.8
0.1 MIN
0.05
0.00
2X 0.525
2X 1.15
0.35
0.25
2X 0.45
2X 1.6
2X 0.625
2X 0.5
0.08 MAX
0.1 C A B
0.05 C
4X 0.45
0.35
0.1 C A B
0.05 C
6X 0.3
0.2
0.1 C A B
0.05 C
2X 0.45
0.35
0.1 C A B
0.05 C
2X 0.45
0.35
0.45
0.35
7X 0.6
0.4
2X 0.6
0.4
2X 0.9
0.7
2.2 0.1
2X 0.7
0.5
2X 0.55
0.1 C A B
0.05 C
0.4
0.3
B 4.1
3.9
A
3.6
3.4
(0.2) TYP
VQFN-HR - 1 mm max heightRJR0014A
PLASTIC QUAD FLATPACK - NO LEAD
4223976/G   05/2025
PIN 1 INDEX AREA
SEATING PLANE
0.08 C
1
14
11
SYMM
PKG
5
6
9
10
PIN 1
ID
NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only.
Dimensioning and tolerancing
per ASME Y14.5M.
2. This drawing is subject to change without notice.
SCALE  3.200
SCALE  30.000
SECTION  A-A
SECTION A-A
TYPICAL
```

### Page 55

```text
www.ti.com
EXAMPLE BOARD LAYOUT
0.07 MIN
ALL AROUND0.07 MAX
ALL AROUND
(R0.05)
TYP
(2.4)
(0.4)
(3.2)
(1)
(0.45)
2X (1)
2X
(0.4)
7X (0.7)
6X (0.25)
(1.85)
(2.9)
4X (1)
4X (0.4)
2X (0.7)
2X
(0.35)
(0.3)
(0.625)
(0.5)
(0.525)
2X (0.8)
2X
(0.4)
4X (R0.12)
VQFN-HR - 1 mm max heightRJR0014A
PLASTIC QUAD FLATPACK - NO LEAD
4223976/G   05/2025
NOTES: (continued)

3. This package is designed to be soldered to thermal pads on the board. For more information, see
Texas Instruments literature
number SLUA271 (www.ti.com/lit/slua271).
SOLDER MASK DEFINED
1
10
14
9
6
5
11
LAND PATTERN EXAMPLE
EXPOSED METAL SHOWN
SCALE:  25X
SYMM
PKG
SEE SOLDER MASK
DETAIL
EXPOSED
METAL
METAL EDGE
SOLDER MASK
OPENING
NON SOLDER MASK
DEFINED
(PREFERRED)
SOLDER MASK DETAIL
EXPOSED
METAL
METAL UNDER
SOLDER MASK
SOLDER MASK
OPENING
```

### Page 56

```text
www.ti.com
EXAMPLE STENCIL DESIGN
(R0.05)
TYP
(3.2)
(1.85)
(0.45)
(2.9)
(0.35)
(1.65)
2X (1.1)
2X (0.4)
2X (1)
2X
(0.4)
7X (0.7)
6X (0.25)
(0.525)
(0.3)
4X (1)
4X (0.35)
2X (0.7)
2X
(0.3)
(0.625)
(0.5) 2X (0.8)
2X
(0.35)
4X (R0.17)
VQFN-HR - 1 mm max heightRJR0014A
PLASTIC QUAD FLATPACK - NO LEAD
4223976/G   05/2025
NOTES: (continued)

4. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste
release. IPC-7525 may have alternate
design recommendations.

SYMM
SOLDER PASTE EXAMPLE
BASED ON 0.1 mm THICK STENCIL
 PADS 1, 5, 9 & 11:
90% PRINTED SOLDER COVERAGE BY AREA
SCALE:  25X
EXPOSED METAL
TYP
EXPOSED
METAL
1
10
14
9
6
5
11
PKG
```

### Page 57

```text
IMPORTANT NOTICE AND DISCLAIMER
TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATASHEETS), DESIGN RESOURCES (INCLUDING
REFERENCE
DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES "AS
IS"
AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION
ANY
IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD
PARTY INTELLECTUAL PROPERTY RIGHTS.
These resources are intended for skilled developers designing with TI products. You are solely
responsible for (1) selecting the appropriate
TI products for your application, (2) designing, validating and testing your application, and (3)
ensuring your application meets applicable
standards, and any other safety, security, regulatory or other requirements.
These resources are subject to change without notice. TI grants you permission to use these
resources only for development of an
application that uses the TI products described in the resource. Other reproduction and display of
these resources is prohibited. No license
is granted to any other TI intellectual property right or to any third party intellectual property
right. TI disclaims responsibility for, and you fully
indemnify TI and its representatives against any claims, damages, costs, losses, and liabilities
arising out of your use of these resources.
TI's products are provided subject to TI's Terms of Sale, TI's General Quality Guidelines, or other
applicable terms available either on
ti.com or provided in conjunction with such TI products. TI's provision of these resources does not
expand or otherwise alter TI's applicable
warranties or warranty disclaimers for TI products. Unless TI explicitly designates a product as
custom or customer-specified, TI products
are standard, catalog, general purpose devices.
TI objects to and rejects any additional or different terms you may propose.
IMPORTANT NOTICE
Copyright (c) 2025, Texas Instruments Incorporated
Last updated 10/2025
```
