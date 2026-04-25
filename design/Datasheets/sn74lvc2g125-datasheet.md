# SN74LVC2G125 - Dual bus buffer gate with 3-state outputs

## Source Reference

- Source PDF: [sn74lvc2g125-datasheet.pdf](sn74lvc2g125-datasheet.pdf)
- Source path: `design\Datasheets\sn74lvc2g125-datasheet.pdf`
- Generated markdown: `sn74lvc2g125-datasheet.md`
- Review note: manually checked against the source PDF; curated summary added and the raw page-by-page extraction is preserved below.

## Part Identity and Ordering

- Texas Instruments `SN74LVC2G125`, dual non-inverting buffer with separate output-enable controls.
- Device-information packages called out on page 1:
  - `SN74LVC2G125DCTR` - SM8 / SSOP, 2.95 mm x 2.80 mm.
  - `SN74LVC2G125DCUR` - VSSOP, 2.30 mm x 2.00 mm.
  - `SN74LVC2G125YZPR` - DSBGA, 1.91 mm x 0.91 mm.
- The orderable addendum includes active orderables such as `SN74LVC2G125DCTR`, `SN74LVC2G125DCUR`, and related tape / reel variants.

## Pin / Pad Designations

- Buffer 1: `1OE`, `1A`, `1Y`.
- Buffer 2: `2OE`, `2A`, `2Y`.
- Power pins: `GND`, `VCC`.
- Package-specific mapping on page 4:
  - DCT / DCU: `1OE` pin 1, `1A` pin 2, `2Y` pin 3, `GND` pin 4, `2A` pin 5, `1Y` pin 6, `2OE` pin 7, `VCC` pin 8.
  - YZP ball map: `1OE=A1`, `1A=B1`, `2Y=C1`, `1Y=C2`, `2OE=B2`, `2A=D2`, `GND=D1`, `VCC=A2`.
- Outputs are disabled when the associated `OE` input is HIGH.

## Ratings and Operating Conditions

- Operating supply range: 1.65 V to 5.5 V.
- Feature callouts include 5.5 V tolerant inputs, about 4.3 ns `tpd` at 3.3 V, `ICC` 10 uA max, and +/-24 mA drive at 3.3 V.
- Absolute maximum highlights: `VCC` and `VI` from -0.5 V to +6.5 V, high-Z / power-off output voltage from -0.5 V to +6.5 V, continuous output current +/-50 mA, and `TJ` 150 deg C.
- ESD ratings called out on page 5: 2000 V HBM and 1000 V CDM.

## Package and Mechanical Notes

- Mechanical coverage spans DCT / SM8, DCU / VSSOP, and YZP / DSBGA.
- The addendum includes package markings, carrier styles, MSL, and latest orderable status information.

## Formulas / Logic Content

- Primary logic relationship: `1Y = 1A` and `2Y = 2A` when their corresponding `OE` input is LOW.
- No major analog equations are central to the datasheet.
- The PDF does note that `OE` should be tied to `VCC` through a pull-up resistor to guarantee the high-impedance state during power-up or power-down.

## Applications and Reference Design Content

- The datasheet includes a typical application schematic showing the device used as an enabled buffer feeding long PCB traces or high-impedance logic inputs.
- Design guidance covers edge-rate / ringing concerns, load-current limits, and general CMOS-input behavior.

## Searchability Note

- The raw page-by-page extraction below is intentionally preserved for local text search.
- Package addendum pages remain easier to verify in the source PDF than in plain extracted text.

## Page-by-page extracted content

### Page 1

#### Extracted tables

Table 1:

```text
PARTNUMBER | PACKAGE | BODYSIZE
SN74LVC2G125DCTR | SM8(8) | 2.95mmx2.80mm
SN74LVC2G125DCUR | VSSOP(8) | 2.30mmx2.00mm
SN74LVC2G125YZPR | DSBGA(8) | 1.91mmx0.91mm
```

#### Raw extracted text

```text
1A 1Y
1
2A
2
2Y
OE
OE
Copyright  2017, Texas Instruments Incorporated
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
SN74LVC2G125
SCES204Q - APRIL 1999 - REVISED MARCH 2017
SN74LVC2G125DualBusBufferGateWith3-StateOutputs
1
1 Features
1* ESD Protection Exceeds JESD 22
- 2000-V Human-Body Model
- 1000-V Charged-Device Model
* Available in the Texas Instruments
NanoFree(TM) Package
* Supports 5-V VCC Operation
* Inputs Accept Voltages to 5.5 V
* Max tpd of 4.3 ns at 3.3 V
* Low Power Consumption, 10-uA Max ICC
* +/-24-mA Output Drive at 3.3 V
* Typical VOLP (Output Ground Bounce)
< 0.8 V at VCC = 3.3 V, TA = 25 deg C
* Typical VOHV (Output VOH Undershoot)
> 2 V at VCC = 3.3 V, TA = 25 deg C
* Ioff Supports Live Insertion, Partial-Power-Down
Mode, and Back-Drive Protection
* Can Be Used as a Down Translator to Translate
Inputs From a Max of 5.5 V Down
to the VCC Level
* Latch-Up Performance Exceeds 100 mA Per
JESD 78, Class II
2 Applications
* Cable Modem Termination Systems
* High-Speed Data Acquisition and Generation
* Military: Radars and Sonars
* Motor Controls: High-Voltage
* Power Line Communication Modems
* SSDs: Internal or External
* Video Broadcasting and Infrastructure: Scalable
Platforms
* Video Broadcasting: IP-Based Multi-Format
Transcoders
* Video Communications Systems
3 Description
The SN74LVC2G125 device is a dual bus buffer
gate, designed for 1.65-V to 5.5-V VCC operation.
This device features dual line drivers with 3-state
outputs. The outputs are disabled when the
associated output-enable (OE) input is high.
NanoFree(TM) package technology is a major
breakthrough in IC packaging concepts, using the die
as the package.
To ensure the high-impedance state during power up
or power down, OE should be tied to VCC through a
pullup resistor; the minimum value of the resistor is
determined by the current-sinking capability of the
driver.
This device is fully specified for partial-power-down
applications using Ioff. The Ioff circuitry disables the
outputs, preventing damaging current backflow
through the device when it is powered down.
Device Information(1)
PART NUMBER PACKAGE BODY SIZE
SN74LVC2G125DCTR SM8 (8) 2.95 mm x 2.80 mm
SN74LVC2G125DCUR VSSOP (8) 2.30 mm x 2.00 mm
SN74LVC2G125YZPR DSBGA (8) 1.91 mm x 0.91 mm
(1) For all available packages, see the orderable addendum at
the end of the data sheet.
Simplified Schematic
```

### Page 2

#### Raw extracted text

```text
2
SN74LVC2G125
SCES204Q - APRIL 1999 - REVISED MARCH 2017 www.ti.com
Product Folder Links: SN74LVC2G125
Submit Documentation Feedback Copyright  1999-2017, Texas Instruments Incorporated
Table of Contents
1 Features .................................................................. 1
2 Applications ........................................................... 1
3 Description ............................................................. 1
4 Revision History..................................................... 2
5 Pin Configuration and Functions ......................... 4
6 Specifications......................................................... 5
6.1 Absolute Maximum Ratings ..................................... 5
6.2 ESD Ratings.............................................................. 5
6.3 Recommended Operating Conditions ...................... 6
6.4 Thermal Information .................................................. 6
6.5 Electrical Characteristics........................................... 7
6.6 Switching Characteristics: TA = -40 deg C to +85 deg C ...... 7
6.7 Switching Characteristics: TA = -40 deg C to +125 deg C .... 7
6.8 Operating Characteristics.......................................... 8
6.9 Typical Characteristics .............................................. 8
7 Parameter Measurement Information .................. 9
8 Detailed Description ............................................ 10
8.1 Overview ................................................................. 10
8.2 Functional Block Diagram ....................................... 10
8.3 Feature Description................................................. 10
8.4 Device Functional Modes........................................ 11
9 Application and Implementation ........................ 12
9.1 Application Information............................................ 12
9.2 Typical Application ................................................. 12
10 Power Supply Recommendations ..................... 13
11 Layout................................................................... 13
11.1 Layout Guidelines ................................................. 13
11.2 Layout Example .................................................... 14
12 Device and Documentation Support ................. 15
12.1 Documentation Support ........................................ 15
12.2 Receiving Notification of Documentation Updates 15
12.3 Community Resources.......................................... 15
12.4 Trademarks ........................................................... 15
12.5 Electrostatic Discharge Caution ............................ 15
12.6 Glossary ................................................................ 15
13 Mechanical, Packaging, and Orderable
Information ........................................................... 15
4 Revision History
NOTE: Page numbers for previous revisions may differ from page numbers in the current version.
Changes from Revision P (January 2016) to Revision Q Page
* Removed '200-V Machine Model' from Features for consistency with ESD ratings table. ................................................... 1
* Added orderable part numbers associated with each package. Changed US8 to VSSOP. .................................................. 1
* Updated YZP package drawing to match mechanical drawing pinout. ................................................................................. 4
* Added YZP pin identifiers to Pin Function table. Added 'buffer #' to Description for pins 2, 3, 5, and 6. Changed
'Power pin' to 'Positive supply'................................................................................................................................................ 4
* Added updated package thermal values based on new models. Changes: RJA DCT 220 -> 199.0, DCU 227 ->
217.8, YZP 102 -> 99.8. Added: RJCtop, RJB, JT, JB........................................................................................................... 6
* Added 'Balanced Push-Pull Outputs,' 'CMOS Inputs,' 'Clamp Diodes,' 'Partial Power Down, 'Over-voltage Tolerant
Inputs.' Removed bullet list................................................................................................................................................... 10
* Added improved layout guidelines and trace example image. ............................................................................................ 13
* Added Documentation Support section, Receiving Notification of Documentation Updates section, and Community
Resources section ................................................................................................................................................................ 15
Changes from Revision O (January 2015) to Revision P Page
* Added overbar for active low to 1OE and 2OE to the Simplified Schematic.......................................................................... 1
* Added TJ Junction temperature to the Absolute Maximum Ratings ...................................................................................... 5
* Added overbar for active low to 1OE and 2OE to the Functional Block Diagram................................................................ 10
Changes from Revision N (November 2013) to Revision O Page
* Added Applications, Device Information table, Pin Functions table, ESD Ratings table, Thermal Information table,
Typical Characteristics, Feature Description section, Device Functional Modes, Application and Implementation
section, Power Supply Recommendations section, Layout section, Device and Documentation Support section, and
Mechanical, Packaging, and Orderable Information section. ................................................................................................. 1
```

### Page 3

#### Raw extracted text

```text
3
SN74LVC2G125
www.ti.com SCES204Q - APRIL 1999 - REVISED MARCH 2017
Product Folder Links: SN74LVC2G125
Submit Documentation FeedbackCopyright  1999-2017, Texas Instruments Incorporated
Changes from Revision M (January 2007) to Revision N Page
* Updated Features. .................................................................................................................................................................. 1
* Updated document to new TI data sheet format. ................................................................................................................... 1
* Removed Ordering Information table. .................................................................................................................................... 1
* Changed MAX operating temperature to 125 deg C in Recommended Operating Conditions table. ......................................... 6
```

### Page 4

#### Extracted tables

Table 1:

```text
|  | 1 8 2 7 3 6 4 5 |  |
```

Table 2:

```text
| PIN |  | TYPE | DESCRIPTION
NAME | DCT,DCU | YZP |  | 
1A | 2 | B1 | I | Inputofbuffer1
2A | 5 | D2 | I | Inputofbuffer2
1OE | 1 | A1 | I | OutputEnableforbuffer1
2OE | 7 | B2 | I | OutputEnableforbuffer2
1Y | 6 | C2 | O | Outputofbuffer1
2Y | 3 | C1 | O | Outputofbuffer2
GND | 4 | D1 |  | Ground
VCC | 8 | A2 |  | Positivesupply
```

#### Raw extracted text

```text
1  2
D
C
B
A
Not to scale
GND 2A
2Y 1Y
1A 2OE
1OE VCC
See mechanical drawings for dimensions.
DCT PACKAGE
(TOP VIEW)
DCU PACKAGE
(TOP VIEW)
1 VCC81OE
2 71A 2OE
3 62Y 1Y
4 5GND 2A
3 6 1Y2Y
81 VCC1OE
5GND 4 2A
2 7 2OE1A
4
SN74LVC2G125
SCES204Q - APRIL 1999 - REVISED MARCH 2017 www.ti.com
Product Folder Links: SN74LVC2G125
Submit Documentation Feedback Copyright  1999-2017, Texas Instruments Incorporated
5 Pin Configuration and Functions
YZP Package
8-Pin DSBGA
Bottom View
See mechanical drawings for dimensions.
Pin Functions
PIN
TYPE DESCRIPTION
NAME DCT, DCU YZP
1A 2 B1 I Input of buffer 1
2A 5 D2 I Input of buffer 2
1OE 1 A1 I Output Enable for buffer 1
2OE 7 B2 I Output Enable for buffer 2
1Y 6 C2 O Output of buffer 1
2Y 3 C1 O Output of buffer 2
GND 4 D1 - Ground
VCC 8 A2 - Positive supply
```

### Page 5

#### Extracted tables

Table 1:

```text
|  |  | MIN | MAX | UNIT
V Supplyvoltage CC |  |  | 0.5 6.5 |  | V
V Inputvoltage (2) I |  |  | 0.5 6.5 |  | V
V Voltagerangeappliedtoanyoutputinthehigh-impedanceorpower-offstate(2) O |  |  | 0.5 6.5 |  | V
V Voltagerangeappliedtoanyoutputinthehighorlowstate(2)(3) O |  |  | 0.5 V +0.5 CC |  | V
I Inputclampcurrent IK |  | V <0 I | 50 |  | mA
I Outputclampcurrent OK |  | V <0 O | 50 |  | mA
I Continuousoutputcurrent O |  |  | +/-50 |  | mA
ContinuouscurrentthroughV orGND CC |  |  | +/-100 |  | mA
T Junctiontemperature J |  |  | 150 |  | deg C
T Storagetemperature stg |  |  | 65 150 |  | deg C
```

Table 2:

```text
|  |  | VALUE | UNIT
Electrostatic V (ESD) discharge |  | Humanbodymodel(HBM),perANSI/ESDA/JEDECJS-001(1) | 2000 | V
 |  | Chargeddevicemodel(CDM),perJEDECspecificationJESD22-C101(2) | 1000 |
```

#### Raw extracted text

```text
5
SN74LVC2G125
www.ti.com SCES204Q - APRIL 1999 - REVISED MARCH 2017
Product Folder Links: SN74LVC2G125
Submit Documentation FeedbackCopyright  1999-2017, Texas Instruments Incorporated
(1) Stresses beyond those listed under Absolute Maximum Ratings may cause permanent damage to the device. These are stress ratings
only, and functional operation of the device at these or any other conditions beyond those indicated under Recommended Operating
Conditions is not implied. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability.
(2) The input negative-voltage and output voltage ratings may be exceeded if the input and output clamp-current ratings are observed.
(3) The value of VCC is provided in the Recommended Operating Conditions table.
6 Specifications
6.1 Absolute Maximum Ratings
See (1)
MIN MAX UNIT
VCC Supply voltage -0.5 6.5 V
VI Input voltage (2) -0.5 6.5 V
VO Voltage range applied to any output in the high-impedance or power-off state (2) -0.5 6.5 V
VO Voltage range applied to any output in the high or low state (2) (3) -0.5 VCC + 0.5 V
IIK Input clamp current VI < 0 -50 mA
IOK Output clamp current VO < 0 -50 mA
IO Continuous output current +/-50 mA
Continuous current through VCC or GND +/-100 mA
TJ Junction temperature 150  deg C
Tstg Storage temperature -65 150  deg C
(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process.
(2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process.
6.2 ESD Ratings
VALUE UNIT
V(ESD)
Electrostatic
discharge
Human body model (HBM), per ANSI/ESDA/JEDEC JS-001 (1) 2000
V
Charged device model (CDM), per JEDEC specification JESD22-C101 (2) 1000
```

### Page 6

#### Extracted tables

Table 1:

```text
|  |  | MIN | MAX | UNIT
VCC Supplyvoltage |  | Operating | 1.65 5.5 |  | V
 |  | Dataretentiononly | 1.5 |  | 
VIH High-levelinputvoltage |  | VCC=1.65Vto1.95V | 0.65xVCC |  | V
 |  | VCC=2.3Vto2.7V | 1.7 |  | 
 |  | VCC=3Vto3.6V | 2 |  | 
 |  | VCC=4.5Vto5.5V | 0.7xVCC |  | 
VIL Low-levelinputvoltage |  | VCC=1.65Vto1.95V | 0.35xVCC |  | V
 |  | VCC=2.3Vto2.7V | 0.7 |  | 
 |  | VCC=3Vto3.6V | 0.8 |  | 
 |  | VCC=4.5Vto5.5V | 0.3xVCC |  | 
VI Inputvoltage |  |  | 0 5.5 |  | V
VO Outputvoltage |  | Highorlowstate | 0 VCC |  | V
 |  | 3-state | 0 5.5 |  | 
IOH High-leveloutputcurrent |  | VCC=1.65V | 4 |  | mA
 |  | VCC=2.3V | 8 |  | 
 |  | VCC=3V | 16 |  | 
 |  |  | 24 |  | 
 |  | VCC=4.5V | 32 |  | 
IOL Low-leveloutputcurrent |  | VCC=1.65V | 4 |  | mA
 |  | VCC=2.3V | 8 |  | 
 |  | VCC=3V | 16 |  | 
 |  |  | 24 |  | 
 |  | VCC=4.5V | 32 |  | 
t/v Inputtransitionriseorfallrate |  | VCC=1.8V+/-0.15V,2.5V+/-0.2V | 20 |  | ns/V
 |  | VCC=3.3V+/-0.3V | 10 |  | 
 |  | VCC=5V+/-0.5V | 5 |  | 
TA Operatingfree-airtemperature |  |  | 40 125 |  | deg C
```

Table 2:

```text
| THERMALMETRIC(1) |  | SN74LVC2G125 |  | UNIT
 |  | DCT(SM8) | DCU(VSSOP) | YZP(DSBGA) | 
 |  | 8PINS | 8PINS | 8PINS | 
R Junction-to-ambientthermalresistance JA |  | 199.0 | 217.8 | 99.8 | deg C/W
R Junction-to-case(top)thermalresistance JCtop |  | 89.5 | 98.3 | 1.0 | deg C/W
R Junction-to-boardthermalresistance JB |  | 118.7 | 138.7 | 29.6 | deg C/W
Junction-to-topcharacterizationparameter JT |  | 14.3 | 34.6 | 0.5 | deg C/W
Junction-to-boardcharacterizationparameter JB |  | 117.4 | 138.2 | 29.8 | deg C/W
```

#### Raw extracted text

```text
6
SN74LVC2G125
SCES204Q - APRIL 1999 - REVISED MARCH 2017 www.ti.com
Product Folder Links: SN74LVC2G125
Submit Documentation Feedback Copyright  1999-2017, Texas Instruments Incorporated
(1) All unused inputs of the device must be held at VCC or GND to ensure proper device operation. See Implications of Slow or Floating
CMOS Inputs, SCBA004.
6.3 Recommended Operating Conditions
over recommended operating free-air temperature range (unless otherwise noted) (1)
MIN MAX UNIT
VCC Supply voltage
Operating 1.65 5.5
V
Data retention only 1.5
VIH High-level input voltage
VCC = 1.65 V to 1.95 V 0.65 x VCC
V
VCC = 2.3 V to 2.7 V 1.7
VCC = 3 V to 3.6 V 2
VCC = 4.5 V to 5.5 V 0.7 x VCC
VIL Low-level input voltage
VCC = 1.65 V to 1.95 V 0.35 x VCC
V
VCC = 2.3 V to 2.7 V 0.7
VCC = 3 V to 3.6 V 0.8
VCC = 4.5 V to 5.5 V 0.3 x VCC
VI Input voltage 0 5.5 V
VO Output voltage
High or low state 0 VCC
V
3-state 0 5.5
IOH High-level output current
VCC = 1.65 V -4
mA
VCC = 2.3 V -8
VCC = 3 V
-16
-24
VCC = 4.5 V -32
IOL Low-level output current
VCC = 1.65 V 4
mA
VCC = 2.3 V 8
VCC = 3 V
16
24
VCC = 4.5 V 32
t/v Input transition rise or fall rate
VCC = 1.8 V +/- 0.15 V, 2.5 V +/- 0.2 V 20
ns/VVCC = 3.3 V +/- 0.3 V 10
VCC = 5 V +/- 0.5 V 5
TA Operating free-air temperature -40 125  deg C
(1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application
report.
6.4 Thermal Information
THERMAL METRIC (1)
SN74LVC2G125
UNITDCT (SM8) DCU (VSSOP) YZP (DSBGA)
8 PINS 8 PINS 8 PINS
RJA Junction-to-ambient thermal resistance 199.0 217.8 99.8  deg C/W
RJCtop Junction-to-case (top) thermal resistance 89.5 98.3 1.0  deg C/W
RJB Junction-to-board thermal resistance 118.7 138.7 29.6  deg C/W
JT Junction-to-top characterization parameter 14.3 34.6 0.5  deg C/W
JB Junction-to-board characterization parameter 117.4 138.2 29.8  deg C/W
```

### Page 7

#### Extracted tables

Table 1:

```text
P | ARAMETER | TESTCONDITIONS |  | VCC | TA=-4 | 0 deg Cto+85 | deg C | TA=-4 | 0 deg Cto+1 | 25 deg C | UNIT
 |  |  |  |  | MIN | TYP(1) | MAX | MIN | TYP(1) | MAX | 
VOH |  | IOH=-100uA |  | 1.65Vto5.5V | VCC-0.1 |  |  | VCC-0.1 |  |  | V
 |  | IOH=-4mA |  | 1.65V | 1.2 |  |  | 1.2 |  |  | 
 |  | IOH=-8mA |  | 1.8V | 1.4 |  |  |  |  |  | 
 |  |  |  | 2.3V | 1.9 |  |  | 1.9 |  |  | 
 |  | IOH=-16mA |  | 3V | 2.4 |  |  | 2.4 |  |  | 
 |  | IOH=-24mA |  |  | 2.3 |  |  | 2.3 |  |  | 
 |  | IOH=-32mA |  | 4.5V | 3.8 |  |  | 3.8 |  |  | 
VOL |  | IOL=100uA |  | 1.65Vto5.5V | 0.1 |  |  | 0.1 |  |  | V
 |  | IOL=4mA |  | 1.65V | 0.45 |  |  | 0.45 |  |  | 
 |  | IOL=8mA |  | 1.8V | 0.45 |  |  |  |  |  | 
 |  |  |  | 2.3V | 0.3 |  |  | 0.3 |  |  | 
 |  | IOL=16mA |  | 3V | 0.4 |  |  | 0.4 |  |  | 
 |  | IOL=24mA |  |  | 0.55 |  |  | 0.55 |  |  | 
 |  | IOL=32mA |  | 4.5V | 0.55 |  |  | 0.75 |  |  | 
II | AorOE inputs | VI=5.5VorGND |  | 0to5.5V | +/-5 |  |  | +/-5 |  |  | uA
Ioff |  | VIorVO=5.5V |  | 0 | +/-10 |  |  | +/-10 |  |  | uA
IOZ |  | VO=0to5.5V |  | 3.6V | 10 |  |  | 10 |  |  | uA
ICC |  | VI=5.5VorGND, IO=0 |  | 1.65Vto5.5V | 10 |  |  | 10 |  |  | uA
ICC |  | OneinputatVCC-0.6V, OtherinputsatVCCorGND |  | 3Vto5.5V | 500 |  |  | 500 |  |  | uA
Ci | Datainputs | VI=VCCorGND |  | 3.3V | 3.5 |  |  | 3.5 |  |  | pF
 | Controlinputs |  |  |  | 4 |  |  | 4 |  |  | 
Co |  | VO=VCCorGND |  | 3.3V | 6.5 |  |  | 6.5 |  |  | pF
```

Table 2:

```text
PARAMETER | FROM (INPUT) | TO (OUTPUT) |  |  | T | A=-40 deg C | to+85 deg C |  |  |  | UNIT
 |  |  | VCC= +/-0.1 | 1.8V 5V | VCC= +/-0. | 2.5V 2V | VCC= +/-0. | 3.3V 3V | VCC +/-0. | =5V 5V | 
 |  |  | MIN | MAX | MIN | MAX | MIN | MAX | MIN | MAX | 
tpd | A | Y | 3.3 9.1 |  | 1.5 4.8 |  | 1.4 4.3 |  | 1 3.7 |  | ns
ten | OE | Y | 4 9.9 |  | 1.9 5.6 |  | 1.2 4.7 |  | 1.2 3.8 |  | ns
tdis | OE | Y | 1.5 11.6 |  | 1 5.8 |  | 1.4 4.6 |  | 1 3.4 |  | ns
```

Table 3:

```text
PARAMETER | FROM (INPUT) | TO (OUTPUT) |  |  | T | A=-40 deg C | to+125 deg | C |  |  | UNIT
 |  |  | VCC= +/-0.1 | 1.8V 5V | VCC= +/-0. | 2.5V 2V | VCC= +/-0. | 3.3V 3V | VCC +/-0. | =5V 5V | 
 |  |  | MIN | MAX | MIN | MAX | MIN | MAX | MIN | MAX | 
tpd | A | Y | 3.3 10.1 |  | 1.5 5.8 |  | 1.4 5.3 |  | 1 4.2 |  | ns
ten | OE | Y | 4 10.9 |  | 1.9 6.6 |  | 1.2 5.7 |  | 1.2 4.3 |  | ns
tdis | OE | Y | 1.5 12.6 |  | 1 6.8 |  | 1.4 5.6 |  | 1 3.9 |  | ns
```

#### Raw extracted text

```text
7
SN74LVC2G125
www.ti.com SCES204Q - APRIL 1999 - REVISED MARCH 2017
Product Folder Links: SN74LVC2G125
Submit Documentation FeedbackCopyright  1999-2017, Texas Instruments Incorporated
(1) All typical values are at VCC = 3.3 V, TA = 25 deg C.
6.5 Electrical Characteristics
over recommended operating free-air temperature range (unless otherwise noted)
PARAMETER TEST CONDITIONS VCC
TA = -40 deg C to +85 deg C TA = -40 deg C to +125 deg C
UNIT
MIN TYP (1) MAX MIN TYP (1) MAX
VOH
IOH = -100 uA 1.65 V to 5.5 V VCC - 0.1 VCC - 0.1
V
IOH = -4 mA 1.65 V 1.2 1.2
IOH = -8 mA
1.8 V 1.4
2.3 V 1.9 1.9
IOH = -16 mA
3 V
2.4 2.4
IOH = -24 mA 2.3 2.3
IOH = -32 mA 4.5 V 3.8 3.8
VOL
IOL = 100 uA 1.65 V to 5.5 V 0.1 0.1
V
IOL = 4 mA 1.65 V 0.45 0.45
IOL = 8 mA
1.8 V 0.45
2.3 V 0.3 0.3
IOL = 16 mA
3 V
0.4 0.4
IOL = 24 mA 0.55 0.55
IOL = 32 mA 4.5 V 0.55 0.75
II
A or OE
inputs VI = 5.5 V or GND 0 to 5.5 V +/-5 +/-5 uA
Ioff VI or VO = 5.5 V 0 +/-10 +/-10 uA
IOZ VO = 0 to 5.5 V 3.6 V 10 10 uA
ICC VI = 5.5 V or GND, IO = 0 1.65 V to 5.5 V 10 10 uA
ICC
One input at VCC - 0.6 V,
Other inputs at VCC or GND 3 V to 5.5 V 500 500 uA
Ci
Data inputs
VI = VCC or GND 3.3 V
3.5 3.5
pF
Control inputs 4 4
Co VO = VCC or GND 3.3 V 6.5 6.5 pF
6.6 Switching Characteristics: TA = -40 deg C to +85 deg C
over recommended operating free-air temperature range (unless otherwise noted) (see Figure 3)
PARAMETER FROM
(INPUT)
TO
(OUTPUT)
TA = -40 deg C to +85 deg C
UNITVCC = 1.8 V
+/- 0.15 V
VCC = 2.5 V
+/- 0.2 V
VCC = 3.3 V
+/- 0.3 V
VCC = 5 V
+/- 0.5 V
MIN MAX MIN MAX MIN MAX MIN MAX
tpd A Y 3.3 9.1 1.5 4.8 1.4 4.3 1 3.7 ns
ten OE Y 4 9.9 1.9 5.6 1.2 4.7 1.2 3.8 ns
tdis OE Y 1.5 11.6 1 5.8 1.4 4.6 1 3.4 ns
6.7 Switching Characteristics: TA = -40 deg C to +125 deg C
over recommended operating free-air temperature range (unless otherwise noted) (see Figure 3)
PARAMETER FROM
(INPUT)
TO
(OUTPUT)
TA = -40 deg C to +125 deg C
UNITVCC = 1.8 V
+/- 0.15 V
VCC = 2.5 V
+/- 0.2 V
VCC = 3.3 V
+/- 0.3 V
VCC = 5 V
+/- 0.5 V
MIN MAX MIN MAX MIN MAX MIN MAX
tpd A Y 3.3 10.1 1.5 5.8 1.4 5.3 1 4.2 ns
ten OE Y 4 10.9 1.9 6.6 1.2 5.7 1.2 4.3 ns
tdis OE Y 1.5 12.6 1 6.8 1.4 5.6 1 3.9 ns
```

### Page 8

#### Extracted tables

Table 1:

```text
| PARAMETER |  | TEST CONDITIONS | V =1.8V CC | V =2.5V CC | V =3.3V CC | V =5V CC | UNIT
 |  |  |  | TYP | TYP | TYP | TYP | 
Powerdissipation C pd capacitance |  | Outputsenabled | f=10MHz | 19 | 19 | 20 | 22 | pF
 |  | Outputsdisabled |  | 2 | 2 | 2 | 3 |
```

Table 2:

```text
2.5 TPD 2 sn 1.5 - DPT 1 0.5 0 -100 -50 0 50 100 150 Temperature - deg C D001 Figure1.TPDAcrossTemperatureat3.3VV CC | 5 TPD 4 sn 3 - DPT 2 1 0 0 1 2 3 4 5 6 Vcc - V D002 Figure2.TPDAcrossV at25 deg C CC
```

Table 3:

```text
TPD |  |  |  |
```

Table 4:

```text
|  |  |  |  | TPD
```

#### Raw extracted text

```text
Temperature -  deg  C
TPD - ns
-100 -50 0 50 100 150
0
0.5
1
1.5
2
2.5
D001
TPD
Vcc - V
TPD - ns
0 1 2 3 4 5 6
0
1
2
3
4
5
D002
TPD
8
SN74LVC2G125
SCES204Q - APRIL 1999 - REVISED MARCH 2017 www.ti.com
Product Folder Links: SN74LVC2G125
Submit Documentation Feedback Copyright  1999-2017, Texas Instruments Incorporated
6.8 Operating Characteristics
TA = 25 deg
PARAMETER TEST
CONDITIONS
VCC = 1.8 V VCC = 2.5 V VCC = 3.3 V VCC = 5 V
UNIT
TYP TYP TYP TYP
Cpd
Power dissipation
capacitance
Outputs enabled
f = 10 MHz
19 19 20 22
pF
Outputs disabled 2 2 2 3
6.9 Typical Characteristics
Figure 1. TPD Across Temperature at 3.3 V VCC Figure 2. TPD Across VCC at 25 deg C
```

### Page 9

#### Extracted tables

Table 1:

```text
TEST | S1
```

Table 2:

```text
INPUTS |  | V M | V LOAD | C L | R L | V D
V I | t/t r f |  |  |  |  | 
V CC V CC 3 V V CC | 2 ns 2 ns 2.5 ns 2.5 ns | V /2 CC V /2 CC 1.5 V V /2 CC | 2 xV CC 2 xV CC 6 V 2 xV CC | 30 pF 30 pF 50 pF 50 pF | 1 kW 500W 500W 500W | 0.15 V 0.15 V 0.3 V 0.3 V
```

Table 3:

```text
t
W
```

#### Raw extracted text

```text
SN74LVC2G125
www.ti.com SCES204Q-APRIL1999-REVISEDMARCH2017
7 Parameter Measurement Information
V
LOAD
R S1 Open
From Output L TEST S1
Under Test GND
t /t Open
C PLH PHL
(see NoteA) L R L t PLZ /t PZL V LOAD
t /t GND
PHZ PZH
LOAD CIRCUIT
INPUTS
V V V C R V
CC V t/t M LOAD L L D
I r f
1.8 V+/-0.15 V V 2 ns V /2 2 xV 30 pF 1 kW 0.15 V
CC CC CC
2.5 V+/-0.2 V V 2 ns V /2 2 xV 30 pF 500W 0.15 V
CC CC CC
3.3 V+/-0.3 V 3 V 2.5 ns 1.5 V 6 V 50 pF 500W 0.3 V
5 V+/-0.5 V V 2.5 ns V /2 2 xV 50 pF 500W 0.3 V
CC CC CC
V
I
Timing Input V
M
0 V
t
W
V I t su t h
V
Input V V I
M M Data Input V V
M M
0 V 0 V
VOLTAGE WAVEFORMS VOLTAGE WAVEFORMS
PULSE DURATION SETUPAND HOLD TIMES
Input V M V M V I C O o u n t t p r u o t l V M V M V I
0 V 0 V
t t t t
PLH PHL PZL PLZ
V Output V /2
Output V M V M OH W S av 1 e a fo t r V m 1 V M V + V LOAD
V OL (see Note L O B AD ) OL D V OL
t t
PHL PLH t t
PZH PHZ
Output V M V M V OH W S a 1 v e a O f t o u G r t m p N u D 2 t V M V OH -V D V OH
V OL (see Note B) 0 V
VOLTAGE WAVEFORMS VOLTAGE WAVEFORMS
PROPAGATION DELAYTIMES ENABLEAND DISABLE TIMES
INVERTINGAND NONINVERTING OUTPUTS LOW-AND HIGH-LEVELENABLING
NOTES: A. C includes probe and jig capacitance.
L
B. Waveform 1 is for an output with internal conditions such that the output is low, except when disabled by the output control.
Waveform 2 is for an output with internal conditions such that the output is high, except when disabled by the output control.
C. All input pulses are supplied by generators having the following characteristics: PRR10 MHz, Z = 50W.
O
D. The outputs are measured one at a time, with one transition per measurement.
E. t and t are the same as t .
PLZ PHZ dis
F. t and t are the same as t .
PZL PZH en
G.t and t are the same as t .
PLH PHL pd
H. All parameters and waveforms are not applicable to all devices.
Figure3. LoadCircuitandVoltageWaveforms
Copyright1999-2017,TexasInstrumentsIncorporated SubmitDocumentationFeedback 9
ProductFolderLinks:SN74LVC2G125
```

### Page 10

#### Raw extracted text

```text
1A 1Y
1
2A
2
2Y
OE
OE
Copyright  2017, Texas Instruments Incorporated
10
SN74LVC2G125
SCES204Q - APRIL 1999 - REVISED MARCH 2017 www.ti.com
Product Folder Links: SN74LVC2G125
Submit Documentation Feedback Copyright  1999-2017, Texas Instruments Incorporated
8 Detailed Description
8.1 Overview
The SN74LVC2G125 device contains dual buffer gate device with output enable control and performs the
Boolean function Y = A. This device is fully specified for partial-power-down applications using Ioff. The Ioff
circuitry disables the outputs, preventing damaging current backflow through the device when it is powered
down. To ensure the high-impedance state during power up or power down, OE should be tied to VCC through a
pull-up resistor; the minimum value of the resistor is determined by the current-sinking capability of the driver.
8.2 Functional Block Diagram
8.3 Feature Description
8.3.1 Balanced High-Drive CMOS Push-Pull Outputs
A balanced output allows the device to sink and source similar currents. The high drive capability of this device
creates fast edges into light loads so routing and load conditions should be considered to prevent ringing.
Additionally, the outputs of this device are capable of driving larger currents than the device can sustain without
being damaged. It is important for the power output of the device to be limited to avoid thermal runaway and
damage due to over-current. The electrical and thermal limits defined the in the Absolute Maximum Ratings must
be followed at all times.
8.3.2 Standard CMOS Inputs
Standard CMOS inputs are high impedance and are typically modelled as a resistor in parallel with the input
capacitance given in the Electrical Characteristics. The worst case resistance is calculated with the maximum
input voltage, given in the Absolute Maximum Ratings , and the maximum input leakage current, given in the
Electrical Characteristics, using ohm's law (R = V  I).
Signals applied to the inputs need to have fast edge rates, as defined by t/v in Recommended Operating
Conditions to avoid excessive currents and oscillations. If a slow or noisy input signal is required, a device with a
Schmitt-trigger input should be utilized to condition the input signal prior to the standard CMOS input.
8.3.3 Clamp Diodes
The inputs and outputs to this device have negative clamping diodes.
CAUTION
Voltages beyond the values specified in the Absolute Maximum Ratings table can
cause damage to the device. The input negative-voltage and output voltage ratings
may be exceeded if the input and output clamp-current ratings are observed.
```

### Page 11

#### Extracted tables

Table 1:

```text
Lo -IIK | gic -IOK
```

Table 2:

```text
Lo | gic
```

Table 3:

```text
INP | UTS | OUTPUT Y
OE | A | 
L H L L H X |  | H L Z
```

#### Raw extracted text

```text
GND
LogicInput Output
VCCDevice
-IIK -IOK
11
SN74LVC2G125
www.ti.com SCES204Q - APRIL 1999 - REVISED MARCH 2017
Product Folder Links: SN74LVC2G125
Submit Documentation FeedbackCopyright  1999-2017, Texas Instruments Incorporated
Feature Description (continued)
Figure 4. Electrical Placement of Clamping Diodes for Each Input and Output
8.3.4 Partial Power Down (Ioff)
The inputs and outputs for this device enter a high impedance state when the supply voltage is 0 V. The
maximum leakage into or out of any input or output pin on the device is specified by Ioff in the Electrical
Characteristics.
8.3.5 Over-voltage Tolerant Inputs
Input signals to this device can be driven above the supply voltage so long as they remain below the maximum
input voltage value specified in the Absolute Maximum Ratings .
8.4 Device Functional Modes
Table 1 lists the functional modes of the SN74LVC2G125.
Table 1. Function Table
INPUTS OUTPUT
YOE A
L H H
L L L
H X Z
```

### Page 12

#### Raw extracted text

```text
1OE
1A
2Y
GND
VCC
2OE
1Y
2A
SN74LVC2G125
Input signal 1
from system
Output 2 to long
PCB trace or
high-Z logic input
Output 1 to long
PCB trace or
high-Z logic inputInput signal 2
from system
0.1 Fu
1.65 V to 5 V
Copyright  2017, Texas Instruments Incorporated
12
SN74LVC2G125
SCES204Q - APRIL 1999 - REVISED MARCH 2017 www.ti.com
Product Folder Links: SN74LVC2G125
Submit Documentation Feedback Copyright  1999-2017, Texas Instruments Incorporated
9 Application and Implementation
NOTE
Information in the following applications sections is not part of the TI component
specification, and TI does not warrant its accuracy or completeness. TIs customers are
responsible for determining suitability of components for their purposes. Customers should
validate and test their design implementation to confirm system functionality.
9.1 Application Information
The SN74LVC2G125 device is a high drive CMOS device that can be used as a output enabled buffer with a
high output drive, such as an LED application. It can produce 24 mA of drive current at 3.3 V making it Ideal for
driving multiple outputs and good for high speed applications up to 100 MHz. The inputs are 5.5-V tolerant
allowing it to translate down to VCC.
9.2 Typical Application
Figure 5. Typical Application Schematic
9.2.1 Design Requirements
This device uses CMOS technology and has balanced output drive. Take care to avoid bus contention because it
can drive currents that would exceed maximum limits. The high drive also creates fast edges into light loads so
routing and load conditions should be considered to prevent ringing.
9.2.2 Detailed Design Procedure
1. Recommended Input Conditions:
- For rise time and fall time specifications, see (t/V) in the Recommended Operating Conditions table.
- For specified high and low levels, see (VIH and VIL) in the Recommended Operating Conditions table.
- Inputs are overvoltage tolerant allowing them to go as high as (VI max) in the Recommended Operating
Conditions table at any valid VCC.
2. Recommended Output Conditions:
- Load currents should not exceed (IO max) per output and should not exceed (Continuous current through
VCC or GND) total current for the part. These limits are located in the Absolute Maximum Ratings table.
- Outputs should not be pulled above VCC.
```

### Page 13

#### Extracted tables

Table 1:

```text
V 1.8 V CC |  |  | 
V 2.5 V CC V 3.3 V |  |  | 
CC V 5 V CC |  |  |
```

#### Raw extracted text

```text
Frequency (MHz)
I (mA)CC
0 20 40 60 80
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
D003
V 1.8 VCC
VCC 2.5 V
VCC 3.3 V
VCC 5 V
13
SN74LVC2G125
www.ti.com SCES204Q - APRIL 1999 - REVISED MARCH 2017
Product Folder Links: SN74LVC2G125
Submit Documentation FeedbackCopyright  1999-2017, Texas Instruments Incorporated
Typical Application (continued)
9.2.3 Application Curve
Figure 6. ICC vs Frequency
10 Power Supply Recommendations
The power supply can be any voltage between the min and max supply voltage rating located in the
Recommended Operating Conditions table.
Each VCC pin should have a good bypass capacitor to prevent power disturbance. For devices with a single
supply a 0.1-uF capacitor is recommended and if there are multiple VCC pins then a 0.01-uF or 0.022-uF
capacitor is recommended for each power pin. It is ok to parallel multiple bypass caps to reject different
frequencies of noise. 0.1-uF and 1-uF capacitors are commonly used in parallel. The bypass capacitor should be
installed as close to the power pin as possible for best results.
11 Layout
11.1 Layout Guidelines
When using multiple bit logic devices, inputs should not float. In many cases, functions or parts of functions of
digital logic devices are unused. Some examples are when only two inputs of a triple-input AND gate are used,
or when only 3 of the 4-buffer gates are used. Such input pins should not be left unconnected because the
undefined voltages at the outside connections result in undefined operational states.
Specified in Figure 7 are rules that must be observed under all circumstances. All unused inputs of digital logic
devices must be connected to a high or low bias to prevent them from floating. The logic level that should be
applied to any particular unused input depends on the function of the device. Generally they will be tied to GND
or VCC, whichever makes more sense or is more convenient.
Even low data rate digital signals can have high frequency signal components due to fast edge rates. When a
PCB trace turns a corner at a 90 deg  angle, a reflection can occur. A reflection occurs primarily because of the
change of width of the trace. At the apex of the turn, the trace width increases to 1.414 times the width. This
increase upsets the transmission-line characteristics, especially the distributed capacitance and self-inductance
of the trace which results in the reflection. Not all PCB traces can be straight and therefore some traces must
turn corners. Figure 8 shows progressively better techniques of rounding corners. Only the last example (BEST)
maintains constant trace width and minimizes reflections.
```

### Page 14

#### Raw extracted text

```text
WORST BETTER BEST
1W min.
W
2W
VCC
Unused Input
Input
Output Output
Input
Unused Input
14
SN74LVC2G125
SCES204Q - APRIL 1999 - REVISED MARCH 2017 www.ti.com
Product Folder Links: SN74LVC2G125
Submit Documentation Feedback Copyright  1999-2017, Texas Instruments Incorporated
11.2 Layout Example
Figure 7. Proper multi-gate input termination diagram
Figure 8. Trace Example
```

### Page 15

#### Raw extracted text

```text
15
SN74LVC2G125
www.ti.com SCES204Q - APRIL 1999 - REVISED MARCH 2017
Product Folder Links: SN74LVC2G125
Submit Documentation FeedbackCopyright  1999-2017, Texas Instruments Incorporated
12 Device and Documentation Support
12.1 Documentation Support
12.1.1 Related Documentation
For related documentation see the following:
Implications of Slow or Floating CMOS Inputs, SCBA004.
12.2 Receiving Notification of Documentation Updates
To receive notification of documentation updates, navigate to the device product folder on ti.com. In the upper
right corner, click on Alert me to register and receive a weekly digest of any product information that has
changed. For change details, review the revision history included in any revised document.
12.3 Community Resources
The following links connect to TI community resources. Linked contents are provided "AS IS" by the respective
contributors. They do not constitute TI specifications and do not necessarily reflect TI's views; see TI's Terms of
Use.
TI E2E(TM) Online Community TI's Engineer-to-Engineer (E2E) Community. Created to foster collaboration
among engineers. At e2e.ti.com, you can ask questions, share knowledge, explore ideas and help
solve problems with fellow engineers.
Design Support TI's Design Support Quickly find helpful E2E forums along with design support tools and
contact information for technical support.
12.4 Trademarks
NanoFree, E2E are trademarks of Texas Instruments.
12.5 Electrostatic Discharge Caution
This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled with
appropriate precautions. Failure to observe proper handling and installation procedures can cause damage.
ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may be more
susceptible to damage because very small parametric changes could cause the device not to meet its published specifications.
12.6 Glossary
SLYZ022 - TI Glossary.
This glossary lists and explains terms, acronyms, and definitions.
13 Mechanical, Packaging, and Orderable Information
The following pages include mechanical, packaging, and orderable information. This information is the most
current data available for the designated devices. This data is subject to change without notice and revision of
this document. For browser-based versions of this data sheet, refer to the left-hand navigation.
```

### Page 16

#### Extracted tables

Table 1:

```text
Orderable part number | Status (1) | Material type (2) | Package | Pins | Package qty | Carrier | RoHS (3) | Lead finish/ Ball material (4) | MSL rating/ Peak reflow (5) | Op temp ( deg C) | Part marking (6)
74LVC2G125DCTRE4 | Active | Production | SSOP (DCT) | 8 | 3000 | null | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | C25 (R, Z)
74LVC2G125DCTRE4.B | Active | Production | SSOP (DCT) | 8 | 3000 | null | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | C25 (R, Z)
74LVC2G125DCTRE6 | Obsolete | Production | SSOP (DCT) | 8 |  |  | Call TI | Call TI | 40 to 125 | C25 Z
74LVC2G125DCTRG4 | Active | Production | SSOP (DCT) | 8 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | C25 (R, Z)
74LVC2G125DCTRG4.B | Active | Production | SSOP (DCT) | 8 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | C25 (R, Z)
74LVC2G125DCURE4 | Active | Production | VSSOP (DCU) | 8 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | C25R
74LVC2G125DCURG4 | Active | Production | VSSOP (DCU) | 8 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | C25R
74LVC2G125DCURG4.B | Active | Production | VSSOP (DCU) | 8 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | C25R
74LVC2G125DCUTG4 | Active | Production | VSSOP (DCU) | 8 | 250 | SMALL T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | C25R
74LVC2G125DCUTG4.B | Active | Production | VSSOP (DCU) | 8 | 250 | SMALL T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | C25R
SN74LVC2G125DCT3 | Active | Production | SSOP (DCT) | 8 | 3000 | LARGE T&R | Yes | SNBI | Level-1-260C-UNLIM | 40 to 125 | C25 Z
SN74LVC2G125DCT3.B | Active | Production | SSOP (DCT) | 8 | 3000 | LARGE T&R | Yes | SNBI | Level-1-260C-UNLIM | 40 to 125 | C25 Z
SN74LVC2G125DCTR | Active | Production | SSOP (DCT) | 8 | 3000 | LARGE T&R | Yes | NIPDAU | SN | Level-1-260C-UNLIM | 40 to 125 | (2WK5, C25) (R, Z)
SN74LVC2G125DCTR.B | Active | Production | SSOP (DCT) | 8 | 3000 | LARGE T&R | Yes | SN | Level-1-260C-UNLIM | 40 to 125 | (2WK5, C25) (R, Z)
SN74LVC2G125DCU3 | Active | Production | VSSOP (DCU) | 8 | 3000 | LARGE T&R | Yes | SNBI | Level-1-260C-UNLIM | 40 to 125 | 25 CZ
SN74LVC2G125DCU3.B | Active | Production | VSSOP (DCU) | 8 | 3000 | LARGE T&R | Yes | SNBI | Level-1-260C-UNLIM | 40 to 125 | 25 CZ
SN74LVC2G125DCUR | Active | Production | VSSOP (DCU) | 8 | 3000 | LARGE T&R | Yes | NIPDAU | SN | Level-1-260C-UNLIM | 40 to 125 | (25, C25J, C25Q, C 25R) CZ
 | Active |  | VSSOP (DCU) | 8 |  | Yes |  | Level-1-260C-UNLIM |  | (25, C25J, C25Q, C 25R) CZ
```

#### Raw extracted text

```text
PACKAGE OPTION ADDENDUM
www.ti.com 23-Dec-2025
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
74LVC2G125DCTRE4 Active Production SSOP (DCT) | 8 3000 | null Yes NIPDAU Level-1-260C-UNLIM -40 to 125 C25
(R, Z)
74LVC2G125DCTRE4.B Active Production SSOP (DCT) | 8 3000 | null Yes NIPDAU Level-1-260C-UNLIM -40 to 125 C25
(R, Z)
74LVC2G125DCTRE6 Obsolete Production SSOP (DCT) | 8 - - Call TI Call TI -40 to 125 C25
Z
74LVC2G125DCTRG4 Active Production SSOP (DCT) | 8 3000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 C25
(R, Z)
74LVC2G125DCTRG4.B Active Production SSOP (DCT) | 8 3000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 C25
(R, Z)
74LVC2G125DCURE4 Active Production VSSOP (DCU) | 8 3000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 C25R
74LVC2G125DCURG4 Active Production VSSOP (DCU) | 8 3000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 C25R
74LVC2G125DCURG4.B Active Production VSSOP (DCU) | 8 3000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 C25R
74LVC2G125DCUTG4 Active Production VSSOP (DCU) | 8 250 | SMALL T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 C25R
74LVC2G125DCUTG4.B Active Production VSSOP (DCU) | 8 250 | SMALL T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 C25R
SN74LVC2G125DCT3 Active Production SSOP (DCT) | 8 3000 | LARGE T&R Yes SNBI Level-1-260C-UNLIM -40 to 125 C25
Z
SN74LVC2G125DCT3.B Active Production SSOP (DCT) | 8 3000 | LARGE T&R Yes SNBI Level-1-260C-UNLIM -40 to 125 C25
Z
SN74LVC2G125DCTR Active Production SSOP (DCT) | 8 3000 | LARGE T&R Yes NIPDAU | SN Level-1-260C-UNLIM -40 to 125 (2WK5, C25)
(R, Z)
SN74LVC2G125DCTR.B Active Production SSOP (DCT) | 8 3000 | LARGE T&R Yes SN Level-1-260C-UNLIM -40 to 125 (2WK5, C25)
(R, Z)
SN74LVC2G125DCU3 Active Production VSSOP (DCU) | 8 3000 | LARGE T&R Yes SNBI Level-1-260C-UNLIM -40 to 125 25
CZ
SN74LVC2G125DCU3.B Active Production VSSOP (DCU) | 8 3000 | LARGE T&R Yes SNBI Level-1-260C-UNLIM -40 to 125 25
CZ
SN74LVC2G125DCUR Active Production VSSOP (DCU) | 8 3000 | LARGE T&R Yes NIPDAU | SN Level-1-260C-UNLIM -40 to 125 (25, C25J, C25Q, C
     25R)
CZ
SN74LVC2G125DCUR.B Active Production VSSOP (DCU) | 8 3000 | LARGE T&R Yes SN Level-1-260C-UNLIM -40 to 125 (25, C25J, C25Q, C
     25R)
CZ
Addendum-Page 1
```

### Page 17

#### Extracted tables

Table 1:

```text
Orderable part number | Status (1) | Material type (2) | Package | Pins | Package qty | Carrier | RoHS (3) | Lead finish/ Ball material (4) | MSL rating/ Peak reflow (5) | Op temp ( deg C) | Part marking (6)
SN74LVC2G125DCUT | Active | Production | VSSOP (DCU) | 8 | 250 | SMALL T&R | Yes | NIPDAU | SN | Level-1-260C-UNLIM | 40 to 125 | (C25J, C25Q, C25R)
SN74LVC2G125DCUT.B | Active | Production | VSSOP (DCU) | 8 | 250 | SMALL T&R | Yes | SN | Level-1-260C-UNLIM | 40 to 125 | (C25J, C25Q, C25R)
SN74LVC2G125YZPR | Active | Production | DSBGA (YZP) | 8 | 3000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | 40 to 125 | (CM7, CMN)
SN74LVC2G125YZPR.B | Active | Production | DSBGA (YZP) | 8 | 3000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | 40 to 125 | (CM7, CMN)
```

#### Raw extracted text

```text
PACKAGE OPTION ADDENDUM
www.ti.com 23-Dec-2025
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
SN74LVC2G125DCUT Active Production VSSOP (DCU) | 8 250 | SMALL T&R Yes NIPDAU | SN Level-1-260C-UNLIM -40 to 125 (C25J, C25Q, C25R)

SN74LVC2G125DCUT.B Active Production VSSOP (DCU) | 8 250 | SMALL T&R Yes SN Level-1-260C-UNLIM -40 to 125 (C25J, C25Q, C25R)

SN74LVC2G125YZPR Active Production DSBGA (YZP) | 8 3000 | LARGE T&R Yes SNAGCU Level-1-260C-UNLIM -40 to 125 (CM7, CMN)
SN74LVC2G125YZPR.B Active Production DSBGA (YZP) | 8 3000 | LARGE T&R Yes SNAGCU Level-1-260C-UNLIM -40 to 125 (CM7, CMN)

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

 OTHER QUALIFIED VERSIONS OF SN74LVC2G125 :
Addendum-Page 2
```

### Page 18

#### Raw extracted text

```text
PACKAGE OPTION ADDENDUM
www.ti.com 23-Dec-2025
* Automotive : SN74LVC2G125-Q1
 NOTE: Qualified Version Definitions:
* Automotive - Q100 devices qualified for high-reliability automotive applications targeting zero defects
Addendum-Page 3
```

### Page 19

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
74LVC2G125DCTRG4 | SSOP | DCT | 8 | 3000 | 177.8 | 12.4 | 3.45 | 4.4 | 1.45 | 4.0 | 12.0 | Q3
74LVC2G125DCURG4 | VSSOP | DCU | 8 | 3000 | 180.0 | 8.4 | 2.25 | 3.35 | 1.05 | 4.0 | 8.0 | Q3
74LVC2G125DCUTG4 | VSSOP | DCU | 8 | 250 | 180.0 | 8.4 | 2.25 | 3.35 | 1.05 | 4.0 | 8.0 | Q3
SN74LVC2G125DCT3 | SSOP | DCT | 8 | 3000 | 180.0 | 13.0 | 3.35 | 4.5 | 1.55 | 4.0 | 12.0 | Q3
SN74LVC2G125DCTR | SSOP | DCT | 8 | 3000 | 180.0 | 12.4 | 3.15 | 4.35 | 1.55 | 4.0 | 12.0 | Q3
SN74LVC2G125DCUR | VSSOP | DCU | 8 | 3000 | 178.0 | 9.0 | 2.25 | 3.35 | 1.05 | 4.0 | 8.0 | Q3
SN74LVC2G125DCUT | VSSOP | DCU | 8 | 250 | 178.0 | 9.0 | 2.25 | 3.35 | 1.05 | 4.0 | 8.0 | Q3
SN74LVC2G125YZPR | DSBGA | YZP | 8 | 3000 | 178.0 | 9.2 | 1.02 | 2.02 | 0.63 | 4.0 | 8.0 | Q1
```

#### Raw extracted text

```text
PACKAGE MATERIALS INFORMATION
www.ti.com 19-Dec-2025
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
74LVC2G125DCTRG4 SSOP DCT 8 3000 177.8 12.4 3.45 4.4 1.45 4.0 12.0 Q3
74LVC2G125DCURG4 VSSOP DCU 8 3000 180.0 8.4 2.25 3.35 1.05 4.0 8.0 Q3
74LVC2G125DCUTG4 VSSOP DCU 8 250 180.0 8.4 2.25 3.35 1.05 4.0 8.0 Q3
SN74LVC2G125DCT3 SSOP DCT 8 3000 180.0 13.0 3.35 4.5 1.55 4.0 12.0 Q3
SN74LVC2G125DCTR SSOP DCT 8 3000 180.0 12.4 3.15 4.35 1.55 4.0 12.0 Q3
SN74LVC2G125DCUR VSSOP DCU 8 3000 178.0 9.0 2.25 3.35 1.05 4.0 8.0 Q3
SN74LVC2G125DCUT VSSOP DCU 8 250 178.0 9.0 2.25 3.35 1.05 4.0 8.0 Q3
SN74LVC2G125YZPR DSBGA YZP 8 3000 178.0 9.2 1.02 2.02 0.63 4.0 8.0 Q1
Pack Materials-Page 1
```

### Page 20

#### Extracted tables

Table 1:

```text
| H
```

Table 2:

```text
Device | Package Type | Package Drawing | Pins | SPQ | Length (mm) | Width (mm) | Height (mm)
74LVC2G125DCTRG4 | SSOP | DCT | 8 | 3000 | 183.0 | 183.0 | 20.0
74LVC2G125DCURG4 | VSSOP | DCU | 8 | 3000 | 202.0 | 201.0 | 28.0
74LVC2G125DCUTG4 | VSSOP | DCU | 8 | 250 | 202.0 | 201.0 | 28.0
SN74LVC2G125DCT3 | SSOP | DCT | 8 | 3000 | 182.0 | 182.0 | 20.0
SN74LVC2G125DCTR | SSOP | DCT | 8 | 3000 | 190.0 | 190.0 | 30.0
SN74LVC2G125DCUR | VSSOP | DCU | 8 | 3000 | 180.0 | 180.0 | 18.0
SN74LVC2G125DCUT | VSSOP | DCU | 8 | 250 | 180.0 | 180.0 | 18.0
SN74LVC2G125YZPR | DSBGA | YZP | 8 | 3000 | 220.0 | 220.0 | 35.0
```

#### Raw extracted text

```text
PACKAGE MATERIALS INFORMATION

www.ti.com 19-Dec-2025
TAPE AND REEL BOX DIMENSIONS
Width (mm)
W LH

*All dimensions are nominal
Device Package Type Package Drawing Pins SPQ Length (mm) Width (mm) Height (mm)
74LVC2G125DCTRG4 SSOP DCT 8 3000 183.0 183.0 20.0
74LVC2G125DCURG4 VSSOP DCU 8 3000 202.0 201.0 28.0
74LVC2G125DCUTG4 VSSOP DCU 8 250 202.0 201.0 28.0
SN74LVC2G125DCT3 SSOP DCT 8 3000 182.0 182.0 20.0
SN74LVC2G125DCTR SSOP DCT 8 3000 190.0 190.0 30.0
SN74LVC2G125DCUR VSSOP DCU 8 3000 180.0 180.0 18.0
SN74LVC2G125DCUT VSSOP DCU 8 250 180.0 180.0 18.0
SN74LVC2G125YZPR DSBGA YZP 8 3000 220.0 220.0 35.0
Pack Materials-Page 2
```

### Page 21

#### Extracted tables

Table 1:

```text
0.05 | C
```

Table 2:

```text
|  | 0.015 | C | A | B
```

#### Raw extracted text

```text
www.ti.com
PACKAGE OUTLINE
C
0.5 MAX
0.19
0.15
1.5
TYP
0.5  TYP
8X 0.25
0.21
0.5
TYP
B E A
D
4223082/A   07/2016
DSBGA - 0.5 mm max heightYZP0008
DIE SIZE BALL GRID ARRAY
NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
    per ASME Y14.5M.
2. This drawing is subject to change without notice.
BALL A1
CORNER
SEATING PLANE
BALL TYP
0.05 C
B
1 2
0.015 C A B
SYMM
SYMM
C
A
D
SCALE  8.000
D: Max =
E: Max =
1.918 mm, Min =
0.918 mm, Min =
1.858 mm
0.858 mm
```

### Page 22

#### Raw extracted text

```text
www.ti.com
EXAMPLE BOARD LAYOUT
8X ( 0.23)
(0.5) TYP
(0.5) TYP
( 0.23)
METAL
0.05 MAX ( 0.23)
SOLDER MASK
OPENING
0.05 MIN
4223082/A   07/2016
DSBGA - 0.5 mm max heightYZP0008
DIE SIZE BALL GRID ARRAY
NOTES: (continued)

3. Final dimensions may vary due to manufacturing tolerance considerations and also routing constraints.
    For more information, see Texas Instruments literature number SNVA009 (www.ti.com/lit/snva009).

SYMM
SYMM
LAND PATTERN EXAMPLE
SCALE:40X
1 2
A
B
C
D
NON-SOLDER MASK
DEFINED
(PREFERRED)
SOLDER MASK DETAILS
NOT TO SCALE
SOLDER MASK
OPENING
SOLDER MASK
DEFINED
METAL UNDER
SOLDER MASK
```

### Page 23

#### Raw extracted text

```text
www.ti.com
EXAMPLE STENCIL DESIGN
(0.5)
TYP
(0.5) TYP
8X ( 0.25) (R0.05) TYP
METAL
TYP
4223082/A   07/2016
DSBGA - 0.5 mm max heightYZP0008
DIE SIZE BALL GRID ARRAY
NOTES: (continued)

4. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release.
SYMM
SYMM
SOLDER PASTE EXAMPLE
BASED ON 0.1 mm THICK STENCIL
SCALE:40X
1 2
A
B
C
D
```

### Page 24

#### Extracted tables

Table 1:

```text
| 0.1 | C
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
4.25
3.95 TYP
1.3
1.0
6X 0.65
8X 0.30
0.15
2X
1.95
(0.15) TYP
0 - 8
0.2
0.0
0.25
GAGE PLANE
0.6
0.2
A
3.1
2.9
NOTE 3
B 3.1
2.9
NOTE 4
4220784/D   10/2025
SSOP - 1.3 mm max heightDCT0008A
SMALL OUTLINE PACKAGE
NOTES:

1. All linear dimensions are in millimeters. Dimensions in parenthesis are for reference only. Dimensioning and tolerancing
    per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. This dimension does not include mold flash, protrusions, or gate burrs. Mold flash, protrusions, or gate burrs shall not
    exceed 0.15 mm per side.
4. This dimension does not include interlead flash. Interlead flash shall not exceed 0.25 mm per side.
1 8
0.13 C A B
5
4
PIN 1 ID
AREA
SEATING PLANE
0.1 C
 SEE DETAIL A
DETAIL A
TYPICAL
SCALE  3.500
```

### Page 25

#### Raw extracted text

```text
EXAMPLE BOARD LAYOUT
DCT0008A SSOP - 1.3 mm max height
SMALL OUTLINE PACKAGE
8X (1.1)
SYMM
(R0.05)
1 TYP
8
8X (0.4)
SYMM
6X (0.65)
5
4
(3.8)
LAND PATTERN EXAMPLE
EXPOSED METAL SHOWN
SCALE:15X
S O O P L E D N E IN R G MASK METAL M SO E L T D A E L R U N M D A E S R K S O O P L E D N E IN R G MASK
EXPOSED METAL EXPOSED METAL
0.07 MAX 0.07 MIN
ALL AROUND ALL AROUND
NON SOLDER MASK SOLDER MASK
DEFINED DEFINED
SOLDER MASK DETAILS
4220784/D 10/2025
NOTES: (continued)
5. Publication IPC-7351 may have alternate designs.
6. Solder mask tolerances between and around signal pads can vary based on board fabrication site.
www.ti.com
```

### Page 26

#### Raw extracted text

```text
www.ti.com
EXAMPLE STENCIL DESIGN
(3.8)
6X (0.65)
8X (0.4)
8X (1.1)
4220784/D   10/2025
SSOP - 1.3 mm max heightDCT0008A
SMALL OUTLINE PACKAGE
NOTES: (continued)

7. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
    design recommendations.
8. Board assembly site may have different recommendations for stencil design.

SYMM
SYMM
1
4 5
8
SOLDER PASTE EXAMPLE
BASED ON 0.125 mm THICK STENCIL
SCALE:15X
```

### Page 27

#### Extracted tables

Table 1:

```text
| 0.1 | C
```

Table 2:

```text
0.08 | C A | B
```

#### Raw extracted text

```text
www.ti.com
PACKAGE OUTLINE
C
6X 0.5
2X
1.5
8X 0.25
0.17
3.2
3.0 TYP
SEATING
PLANE
0.1
0.0
0.12
GAGE PLANE
0 -6
0.9
0.6
B 2.4
2.2
NOTE 3
A
2.1
1.9
NOTE 3
0.35
0.20
(0.13) TYP
VSSOP - 0.9 mm max heightDCU0008A
SMALL OUTLINE PACKAGE
4225266/A   09/2014
1
4 5
8
0.08 C A B
PIN 1 INDEX AREA
SEE DETAIL  A
0.1 C
NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
    per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. This dimension does not include mold flash, protrusions, or gate burrs. Mold flash, protrusions, or gate burrs shall not
    exceed 0.15 mm per side.
4. Reference JEDEC registration MO-187 variation CA.

A  30
DETAIL A
TYPICAL
SCALE  6.000
```

### Page 28

#### Raw extracted text

```text
www.ti.com
EXAMPLE BOARD LAYOUT
0.05 MAX
ALL AROUND
0.05 MIN
ALL AROUND
8X (0.85)
8X (0.3)
6X (0.5)
(3.1)
(R0.05) TYP
VSSOP - 0.9 mm max heightDCU0008A
SMALL OUTLINE PACKAGE
4225266/A   09/2014
NOTES: (continued)

5. Publication IPC-7351 may have alternate designs.
6. Solder mask tolerances between and around signal pads can vary based on board fabrication site.

LAND PATTERN EXAMPLE
EXPOSED METAL SHOWN
SCALE: 25X
SYMM
SYMM
1
4 5
8
SEE SOLDER MASK
DETAILS
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

### Page 29

#### Raw extracted text

```text
www.ti.com
EXAMPLE STENCIL DESIGN
8X (0.85)
8X (0.3)
6X (0.5)
(3.1)
(R0.05) TYP
VSSOP - 0.9 mm max heightDCU0008A
SMALL OUTLINE PACKAGE
4225266/A   09/2014
NOTES: (continued)

7. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
    design recommendations.
8. Board assembly site may have different recommendations for stencil design.

SOLDER PASTE EXAMPLE
BASED ON 0.125 mm THICK STENCIL
SCALE: 25X
SYMM
SYMM
1
4 5
8
```

### Page 30

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
