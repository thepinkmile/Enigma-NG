# SN74LVC1G175 - Single D-type flip-flop with asynchronous clear

## Source Reference

- Source PDF: [TI-sn74lvc1g175-datasheet.pdf](TI-sn74lvc1g175-datasheet.pdf)
- Source path: `design\Datasheets\TI-sn74lvc1g175-datasheet.pdf`
- Generated markdown: `TI-sn74lvc1g175-datasheet.md`
- Review note: manually checked against the source PDF; curated summary added and the raw page-by-page extraction is preserved below.

## Part Identity and Ordering

- Texas Instruments `SN74LVC1G175`, single D-type flip-flop with asynchronous clear.
- Device-information packages called out on page 1:
  - `SN74LVC1G175DBV` - SOT-23 (6), 2.90 mm x 1.60 mm.
  - `SN74LVC1G175DCK` - SC70 (6), 2.00 mm x 1.25 mm.
  - `SN74LVC1G175DRY` - SON (6), 1.45 mm x 1.00 mm.
  - `SN74LVC1G175YZP` - DSBGA (6), 1.41 mm x 0.91 mm.
- The orderable addendum includes active orderables such as `SN74LVC1G175DBVR`, `SN74LVC1G175DBVT`, `SN74LVC1G175DCKR`, `SN74LVC1G175DRYR`, and `SN74LVC1G175YZPR`.

## Pin / Pad Designations

- Page 3 pin-function table:
  - pin 1 `CLK`
  - pin 6 `CLR`
  - pin 3 `D`
  - pin 2 `GND`
  - pin 4 `Q`
  - pin 5 `VCC`
- `CLR` is asynchronous and active low.
- On a rising clock edge, `D` is transferred to `Q` when `CLR` is high; when `CLR` is low, `Q` is forced low.

## Ratings and Operating Conditions

- Operating supply range: 1.65 V to 5.5 V, with 1.5 V data-retention condition also called out.
- Feature callouts include 5.5 V tolerant inputs, down translation to `VCC`, `tpd` about 4.3 ns at 3.3 V, `ICC` 10 uA max, and +/-24 mA output drive at 3.3 V.
- Absolute maximum highlights: `VCC`, `VI`, and power-off output voltage from
  -0.5 V to +6.5 V, continuous output current +/-50 mA, continuous current
  through `VCC` or `GND` +/-100 mA, storage temperature -65 deg C to +150 deg C.
- ESD ratings called out on page 4: 2000 V HBM and 1000 V CDM.

## Package and Mechanical Notes

- Mechanical coverage spans SOT-23, SC70, SON, and DSBGA package options.
- The addendum shows that the DSBGA (`YZP`) option is limited to -40 deg C to +85 deg C while the other listed package options are rated through +125 deg C.

## Formulas / Logic Content

- No analog equations are central to this datasheet.
- Core digital behavior is the edge-triggered transfer `D -> Q` on `CLK` rising edge with asynchronous low-clear overriding the clocked path.

## Applications and Reference Design Content

- The datasheet includes a worked 4-bit serial shift-register example built from four `SN74LVC1G175` devices.
- Design guidance covers input rise/fall requirements, load-current limits, and overvoltage-tolerant I/O usage.

## Searchability Note

- The raw page-by-page extraction below is intentionally preserved for local text search.
- Package addendum data and ball / lead drawings remain easier to confirm in the source PDF than in text alone.

## Page-by-page extracted content

### Page 1

#### Extracted tables

Table 1:

```text
PARTNUMBER | PACKAGE | BODYSIZE(NOM)
SN74LVC1G175DBV | SOT-23(6) | 2.90mmx1.60mm
SN74LVC1G175DCK | SC70(6) | 2.00mmx1.25mm
SN74LVC1G175DRY | SON(6) | 1.45mmx1.00mm
SN74LVC1G175YZP | DSBGA(6) | 1.41mmx0.91mm
```

#### Raw extracted text

```text
Q
1
6
C1
D
CLR
CLK
D
R
3
4
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
SN74LVC1G175
SCES560G - MARCH 2004 - REVISED JUNE 2015
SN74LVC1G175SingleD-TypeFlip-FlopWithAsynchronousClear
1 Features 3 Description
This single D-type flip-flop is designed for 1.65-V to
1* Available in the Texas Instruments
5.5-V VCC operation.NanoFree(TM) Package
The SN74LVC1G175 device has an asynchronous* Supports 5-V VCC Operation
clear (CLR) input. When CLR is high, data from the* Inputs Accept Voltages to 5.5 V input pin (D) is transferred to the output pin (Q) on* Supports Down Translation to VCC the clock's (CLK) rising edge. When CLR is low, Q is
* Max tpd of 4.3 ns at 3.3 V forced into the low state, regardless of the clock edge
or data on D.* Low Power Consumption, 10-uA Max ICC
NanoFree(TM) package technology is a major* +/-24-mA Output Drive at 3.3 V
breakthrough in IC packaging concepts, using the die* Ioff Supports Live Insertion, Partial-Power-Down as the package.Mode, and Back-Drive Protection
This device is fully specified for partial-power-down* Latch-Up Performance Exceeds 100 mA Per
applications using Ioff. The Ioff circuitry disables theJESD 78, Class II
outputs, preventing damaging current backflow* ESD Protection Exceeds JESD 22 through the device when it is powered down.
- 2000-V Human-Body Model (A114-A)
Device Information(1)
- 200-V Machine Model (A115-A)
PART NUMBER PACKAGE BODY SIZE (NOM)- 1000-V Charged-Device Model (C101)
SN74LVC1G175DBV SOT-23 (6) 2.90 mm x 1.60 mm
SN74LVC1G175DCK SC70 (6) 2.00 mm x 1.25 mm2 Applications
SN74LVC1G175DRY SON (6) 1.45 mm x 1.00 mm* TV/Set Top Box/Audio
SN74LVC1G175YZP DSBGA (6) 1.41 mm x 0.91 mm* EPOS (Electronic Point-of-Sale)
(1) For all available packages, see the orderable addendum at* Motor Drives the end of the data sheet.
* PC/Notebook
* Servers
* Factory Automation and Control
* Tablets
* Medical Healthcare and Fitness
* Smart Grid
* Telecom Infrastructure
* Enterprise Switching
* Projectors
* Storage
Logic Diagram (Positive Logic)
1
An IMPORTANT NOTICE at the end of this data sheet addresses availability, warranty, changes, use in safety-critical applications,
intellectual property matters and other important disclaimers. PRODUCTION DATA.
```

### Page 2

#### Raw extracted text

```text
SN74LVC1G175
SCES560G - MARCH 2004 - REVISED JUNE 2015 www.ti.com
Table of Contents
1 Features .................................................................. 1 8 Detailed Description ............................................ 10
8.1 Overview ................................................................. 102 Applications ........................................................... 1
8.2 Functional Block Diagram ....................................... 103 Description ............................................................. 1
8.3 Feature Description................................................. 104 Revision History..................................................... 2
8.4 Device Functional Modes........................................ 105 Pin Configuration and Functions ......................... 3
9 Application and Implementation ........................ 116 Specifications......................................................... 4
9.1 Application Information............................................ 116.1 Absolute Maximum Ratings ..................................... 4
9.2 Typical Application ................................................. 116.2 ESD Ratings.............................................................. 4
10 Power Supply Recommendations ..................... 126.3 Recommended Operating Conditions ...................... 4
11 Layout................................................................... 126.4 Thermal Information .................................................. 5
11.1 Layout Guidelines ................................................. 126.5 Electrical Characteristics........................................... 5
11.2 Layout Example .................................................... 136.6 Timing Requirements, -40 deg C to 85 deg C....................... 6
12 Device and Documentation Support ................. 146.7 Timing Requirements, -40 deg C to 125 deg C..................... 6
12.1 Documentation Support ........................................ 146.8 Switching Characteristics, -40 deg C to 85 deg C................. 6
12.2 Community Resources.......................................... 146.9 Switching Characteristics, -40 deg C to 85 deg C................. 6
12.3 Trademarks ........................................................... 146.10 Switching Characteristics, -40 deg C to 125 deg C............. 7
12.4 Electrostatic Discharge Caution ............................ 146.11 Operating Characteristics........................................ 7
12.5 Glossary ................................................................ 146.12 Typical Characteristics ............................................ 7
13 Mechanical, Packaging, and Orderable7 Parameter Measurement Information .................. 8
Information ........................................................... 14
4 Revision History
NOTE: Page numbers for previous revisions may differ from page numbers in the current version.
Changes from Revision F (December 2013) to Revision G Page
* Added Applications ................................................................................................................................................................. 1
* Added Device Information table ............................................................................................................................................. 1
* Added ESD Ratingss table. .................................................................................................................................................... 4
* Added Thermal Information table ........................................................................................................................................... 5
* Added Typical Characteristics. ............................................................................................................................................... 7
Changes from Revision E (June 2008) to Revision F Page
* Updated document to new TI data sheet format. ................................................................................................................... 1
* Deleted Ordering Information table. ....................................................................................................................................... 1
* Updated Features. .................................................................................................................................................................. 1
2 Submit Documentation Feedback Copyright  2004-2015, Texas Instruments Incorporated
Product Folder Links: SN74LVC1G175
```

### Page 3

#### Extracted tables

Table 1:

```text
PIN |  |  | I/O | DESCRIPTION
NAME | NO. |  |  | 
CLK | 1 |  | I | ClockInput
CLR | 6 |  | I | ClearDataInput
D | 3 |  | I | DataInput
GND | 2 |  |  | Ground
Q | 4 |  | O | Output
V CC | 5 |  |  | Power
```

#### Raw extracted text

```text
GND V CC
CLK 6
5
4
2
3D Q
CLR1
2GND VCC
1
5
CLK
D 43 Q
6 CLR
2GND VCC5
3 4D Q
61CLK CLR
Q3 4D
2GND 5
1CLK
VCC
6 CLR
SN74LVC1G175
www.ti.com SCES560G - MARCH 2004 - REVISED JUNE 2015
5 Pin Configuration and Functions
DBV Package DCK Package6-Pin SOT-23 6-Pin SC70Top View Top View
DRY Package YZP Package6-Pin SON 6-Pin DSBGATop View Bottom View
See mechanical drawings for dimensions.
Pin Functions
PIN
I/O DESCRIPTION
NAME NO.
CLK 1 I Clock Input
CLR 6 I Clear Data Input
D 3 I Data Input
GND 2 - Ground
Q 4 O Output
VCC 5 - Power
Copyright  2004-2015, Texas Instruments Incorporated Submit Documentation Feedback 3
Product Folder Links: SN74LVC1G175
```

### Page 4

#### Extracted tables

Table 1:

```text
|  |  | MIN | MAX | UNIT
V Supplyvoltage CC |  |  | 0.5 6.5 |  | V
V Inputvoltage I |  |  | 0.5 6.5 |  | V
V Voltageappliedtoanyoutputinthehigh-impedanceorpower-offstate(2) O |  |  | 0.5 6.5 |  | V
V Voltageappliedtoanyoutputinthehighorlowstate(2)(3) O |  |  | 0.5 V +0.5 CC |  | V
I Inputclampcurrent IK |  | V <0 I | 50 |  | mA
I Outputclampcurrent OK |  | V <0 O | 50 |  | mA
I Continuousoutputcurrent O |  |  | +/-50 |  | mA
ContinuouscurrentthroughV orGND CC |  |  | +/-100 |  | mA
T Storagetemperature stg |  |  | 65 150 |  | deg C
```

Table 2:

```text
|  |  | VALUE | UNIT
Electrostatic V (ESD) discharge |  | Human-bodymodel(HBM),perANSI/ESDA/JEDECJS-001(1) | 2000 | V
 |  | Charged-devicemodel(CDM),perJEDECspecificationJESD22-C101(2) | 1000 |
```

Table 3:

```text
|  |  | MIN | MAX | UNIT
V Supplyvoltage CC |  | Operating | 1.65 5.5 |  | V
 |  | Dataretentiononly | 1.5 |  | 
V High-levelinputvoltage IH |  | V =1.65Vto1.95V CC | 0.65xV CC |  | V
 |  | V =2.3Vto2.7V CC | 1.7 |  | 
 |  | V =3Vto3.6V CC | 2 |  | 
 |  | V =4.5Vto5.5V CC | 0.7xV CC |  | 
V Low-levelinputvoltage IL |  | V =1.65Vto1.95V CC | 0.35xV CC |  | V
 |  | V =2.3Vto2.7V CC | 0.7 |  | 
 |  | V =3Vto3.6V CC | 0.8 |  | 
 |  | V =4.5Vto5.5V CC | 0.3xV CC |  | 
V Inputvoltage I |  |  | 0 5.5 |  | V
V Outputvoltage O |  |  | 0 V CC |  | V
I High-leveloutputcurrent OH |  | V =1.65V CC | 4 |  | mA
 |  | V =2.3V CC | 8 |  | 
 |  | V =3V CC | 16 |  | 
 |  |  | 24 |  | 
 |  | V =4.5V CC | 32 |  |
```

#### Raw extracted text

```text
SN74LVC1G175
SCES560G - MARCH 2004 - REVISED JUNE 2015 www.ti.com
6 Specifications
6.1 Absolute Maximum Ratings
over operating free-air temperature range (unless otherwise noted) (1)
MIN MAX UNIT
VCC Supply voltage -0.5 6.5 V
VI Input voltage -0.5 6.5 V
VO Voltage applied to any output in the high-impedance or power-off state (2) -0.5 6.5 V
VO Voltageapplied to any output in the high or low state (2) (3) -0.5 VCC + 0.5 V
IIK Input clamp current VI < 0 -50 mA
IOK Output clamp current VO < 0 -50 mA
IO Continuous output current +/-50 mA
Continuous current through VCC or GND +/-100 mA
Tstg Storage temperature -65 150  deg C
(1) Stresses beyond those listed under Absolute Maximum Ratings may cause permanent damage to the device. These are stress ratings
only, and functional operation of the device at these or any other conditions beyond those indicated under Recommended Operating
Conditions is not implied. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability.
(2) The input negative-voltage and output voltage ratings may be exceeded if the input and output current ratings are observed.
(3) The value of VCC is provided in the Recommended Operating Conditions table.
6.2 ESD Ratings
VALUE UNIT
Human-body model (HBM), per ANSI/ESDA/JEDEC JS-001 (1) 2000ElectrostaticV(ESD) Vdischarge Charged-device model (CDM), per JEDEC specification JESD22-C101 (2) 1000
(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process.
(2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process.
6.3 Recommended Operating Conditions
over operating free-air temperature range (unless otherwise noted) (1)
MIN MAX UNIT
Operating 1.65 5.5
VCC Supply voltage V
Data retention only 1.5
VCC = 1.65 V to 1.95 V 0.65 x VCC
VCC = 2.3 V to 2.7 V 1.7
VIH High-level input voltage V
VCC = 3 V to 3.6 V 2
VCC = 4.5 V to 5.5 V 0.7 x VCC
VCC = 1.65 V to 1.95 V 0.35 x VCC
VCC = 2.3 V to 2.7 V 0.7
VIL Low-level input voltage V
VCC = 3 V to 3.6 V 0.8
VCC = 4.5 V to 5.5 V 0.3 x VCC
VI Input voltage 0 5.5 V
VO Output voltage 0 VCC V
VCC = 1.65 V -4
VCC = 2.3 V -8
IOH High-level output current -16 mA
VCC = 3 V
-24
VCC = 4.5 V -32
(1) All unused inputs of the device must be held at VCC or GND to ensure proper device operation. Refer to the TI application report,
Implications of Slow or Floating CMOS Inputs, SCBA004.
4 Submit Documentation Feedback Copyright  2004-2015, Texas Instruments Incorporated
Product Folder Links: SN74LVC1G175
```

### Page 5

#### Extracted tables

Table 1:

```text
|  |  | MIN | MAX | UNIT
I Low-leveloutputcurrent OL |  | V =1.65V CC | 4 |  | mA
 |  | V =2.3V CC | 8 |  | 
 |  | V =3V CC | 16 |  | 
 |  |  | 24 |  | 
 |  | V =4.5V CC | 32 |  | 
t/v Inputtransitionriseorfallrate |  | V =1.8V+/-0.15V,2.5V+/-0.2V CC | 20 |  | ns/V
 |  | V =3.3V+/-0.3V CC | 10 |  | 
 |  | V =5V+/-0.5V CC | 10 |  | 
T Operatingfree-airtemperature A |  |  | 40 125 |  | deg C
```

Table 2:

```text
| THERMALMETRIC(1) |  | SN74LV | C1G175 |  | UNIT
 |  | DBV(SOT-23) | DCK(SC70) | DRY(SON) | YZP(DSBGA) | 
 |  | 6PINS | 6PINS | 6PINS | 6PINS | 
R Junction-to-ambientthermalresistance JA |  | 165 | 259 | 234 | 123 | deg C/W
```

Table 3:

```text
PARAMETER |  | TESTCONDITIONS | VCC | 40 | deg Cto85 deg C |  | 40 deg | Cto125 deg C |  | UNIT
 |  |  |  | MIN | TYP(1) | MAX | MIN | TYP(1) | MAX | 
VOH | IOH=-100uA |  | 1.65Vto5.5V | VCC -0.1 |  |  | VCC -0.1 |  |  | V
 | IOH=-4mA |  | 1.65V | 1.2 |  |  | 1.2 |  |  | 
 | IOH=-8mA |  | 2.3V | 1.9 |  |  | 1.9 |  |  | 
 | IOH=-16mA |  | 3V | 2.4 |  |  | 2.4 |  |  | 
 | IOH=-24mA |  |  | 2.3 |  |  | 2.3 |  |  | 
 | IOH=-32mA |  | 4.5V | 3.8 |  |  | 3.8 |  |  | 
VOL | IOL=100uA |  | 1.65Vto5.5V | 0.1 |  |  | 0.1 |  |  | V
 | IOL=4mA |  | 1.65V | 0.45 |  |  | 0.45 |  |  | 
 | IOL=8mA |  | 2.3V | 0.3 |  |  | 0.3 |  |  | 
 | IOL=16mA |  | 3V | 0.4 |  |  | 0.4 |  |  | 
 | IOL=24mA |  |  | 0.55 |  |  | 0.55 |  |  | 
 | IOL=32mA |  | 4.5V | 0.55 |  |  | 0.55 |  |  | 
II | VI=5.5VorGND |  | 0to5.5V | +/-1 |  |  | +/-1 |  |  | uA
Ioff | VIorVO=5.5V |  | 0 | +/-10 |  |  | +/-10 |  |  | uA
ICC | VI=5.5VorGND,IO=0 |  | 1.65Vto5.5V | 10 |  |  | 10 |  |  | uA
ICC | OneinputatVCC -0.6V, OtherinputsatVCCorGND |  | 3Vto5.5V | 500 |  |  | 500 |  |  | uA
Ci | VI=VCCorGND |  | 3.3V | 3 |  |  | 3 |  |  | pF
```

#### Raw extracted text

```text
SN74LVC1G175
www.ti.com SCES560G - MARCH 2004 - REVISED JUNE 2015
Recommended Operating Conditions (continued)
over operating free-air temperature range (unless otherwise noted)(1)
MIN MAX UNIT
VCC = 1.65 V 4
VCC = 2.3 V 8
IOL Low-level output current 16 mA
VCC = 3 V
24
VCC = 4.5 V 32
VCC = 1.8 V +/- 0.15 V, 2.5 V +/- 0.2 V 20
t/v Input transition rise or fall rate VCC = 3.3 V +/- 0.3 V 10 ns/V
VCC = 5 V +/- 0.5 V 10
TA Operating free-air temperature -40 125  deg C
6.4 Thermal Information
SN74LVC1G175
THERMAL METRIC (1) DBV (SOT-23) DCK (SC70) DRY (SON) YZP (DSBGA) UNIT
6 PINS 6 PINS 6 PINS 6 PINS
RJA Junction-to-ambient thermal resistance 165 259 234 123  deg C/W
(1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application
report, SPRA953.
6.5 Electrical Characteristics
over recommended operating free-air temperature range (unless otherwise noted)
-40 deg C to 85 deg C -40 deg C to 125 deg C
PARAMETER TEST CONDITIONS VCC UNIT
MIN TYP (1) MAX MIN TYP (1) MAX
IOH = -100 uA 1.65 V to 5.5 V VCC - 0.1 VCC - 0.1
IOH = -4 mA 1.65 V 1.2 1.2
IOH = -8 mA 2.3 V 1.9 1.9
VOH V
IOH = -16 mA 2.4 2.4
3 V
IOH = -24 mA 2.3 2.3
IOH = -32 mA 4.5 V 3.8 3.8
IOL = 100 uA 1.65 V to 5.5 V 0.1 0.1
IOL = 4 mA 1.65 V 0.45 0.45
IOL = 8 mA 2.3 V 0.3 0.3
VOL V
IOL = 16 mA 0.4 0.4
3 V
IOL = 24 mA 0.55 0.55
IOL = 32 mA 4.5 V 0.55 0.55
II VI = 5.5 V or GND 0 to 5.5 V +/-1 +/-1 uA
Ioff VI or VO = 5.5 V 0 +/-10 +/-10 uA
ICC VI = 5.5 V or GND, IO = 0 1.65 V to 5.5 V 10 10 uA
One input at VCC - 0.6 V,ICC 3 V to 5.5 V 500 500 uAOther inputs at VCC or GND
Ci VI = VCC or GND 3.3 V 3 3 pF
(1) All typical values are at VCC = 3.3 V, TA = 25 deg C.
Copyright  2004-2015, Texas Instruments Incorporated Submit Documentation Feedback 5
Product Folder Links: SN74LVC1G175
```

### Page 6

#### Extracted tables

Table 1:

```text
|  |  |  |  |  |  | 40 deg Ct | o85 deg C |  |  |  | UNIT
 |  |  |  | VCC= +/-0.1 | 1.8V 5V | VCC= +/-0. | 2.5V 2V | VCC= +/-0. | 3.3V 3V | VCC= +/-0. | 5V 5V | 
 |  |  |  | MIN | MAX | MIN | MAX | MIN | MAX | MIN | MAX | 
fclock Clockfrequency |  |  |  | 100 |  | 125 |  | 150 |  | 175 |  | MHz
tw Pulseduration |  | CLR | Low | 5.6 |  | 3 |  | 2.8 |  | 2.5 |  | ns
 |  | CLK | Highorlow | 3.5 |  | 3 |  | 2.8 |  | 2.5 |  | 
tsu Setuptime,beforeCLK |  | Data |  | 3 |  | 2.5 |  | 2 |  | 1.5 |  | ns
 |  | CLRinactive |  | 0 |  | 0 |  | 0.5 |  | 0.5 |  | 
th Holdtime,dataafterCLK |  |  |  | 0 |  | 0 |  | 0.5 |  | 0.5 |  | ns
```

Table 2:

```text
|  |  |  |  |  |  | 40 deg Ct | o125 deg C |  |  |  | UNIT
 |  |  |  | VCC= +/-0.1 | 1.8V 5V | VCC= +/-0. | 2.5V 2V | VCC= +/-0. | 3.3V 3V | VCC= +/-0. | 5V 5V | 
 |  |  |  | MIN | MAX | MIN | MAX | MIN | MAX | MIN | MAX | 
fclock Clockfrequency |  |  |  | 100 |  | 125 |  | 150 |  | 175 |  | MHz
tw Pulseduration |  | CLR | Low | 5.6 |  | 3 |  | 2.8 |  | 2.5 |  | ns
 |  | CLK | Highorlow | 3.5 |  | 3 |  | 2.8 |  | 2.5 |  | 
tsu Setuptime,beforeCLK |  | Data |  | 3 |  | 2.5 |  | 2 |  | 1.5 |  | ns
 |  | CLRinactive |  | 0.5 |  | 0.5 |  | 0.7 |  | 0.7 |  | 
th Holdtime,dataafterCLK |  |  |  | 0.5 |  | 0.5 |  | 0.7 |  | 0.7 |  | ns
```

Table 3:

```text
PARAMETER | FROM (INPUT) | TO (OUTPUT) |  |  |  | 40 deg Ct | o85 deg C |  |  |  | UNIT
 |  |  | VCC= +/-0.1 | 1.8V 5V | VCC= +/-0. | 2.5V 2V | VCC= +/-0. | 3.3V 3V | VCC +/-0 | =5V .5V | 
 |  |  | MIN | MAX | MIN | MAX | MIN | MAX | MIN | MAX | 
fmax |  |  | 100 |  | 125 |  | 150 |  | 175 |  | MHz
tpd | CLK | Q | 2.5 12.9 |  | 2 6.5 |  | 1.4 4.6 |  | 1 3 |  | ns
 | CLR |  | 2.5 12.4 |  | 2 6 |  | 1.2 4.3 |  | 1 3.2 |  |
```

Table 4:

```text
PARAMETER | FROM (INPUT) | TO (OUTPUT) |  |  |  | 40 deg Ct | o85 deg C |  |  |  | UNIT
 |  |  | VCC= +/-0.1 | 1.8V 5V | VCC= +/-0. | 2.5V 2V | VCC= +/-0. | 3.3V 3V | VCC +/-0 | =5V .5V | 
 |  |  | MIN | MAX | MIN | MAX | MIN | MAX | MIN | MAX | 
fmax |  |  | 100 |  | 125 |  | 150 |  | 175 |  | MHz
tpd | CLK | Q | 2.7 13.4 |  | 2.2 7.1 |  | 1.6 5.7 |  | 1.5 4 |  | ns
 | CLR |  | 2.7 12.9 |  | 2.2 7 |  | 1.5 5.8 |  | 1.3 4.1 |  |
```

#### Raw extracted text

```text
SN74LVC1G175
SCES560G - MARCH 2004 - REVISED JUNE 2015 www.ti.com
6.6 Timing Requirements, -40 deg C to 85 deg C
over recommended operating free-air temperature range (unless otherwise noted) (see Figure 2)
-40 deg C to 85 deg C
VCC = 1.8 V VCC = 2.5 V VCC = 3.3 V VCC = 5 V UNIT+/- 0.15 V +/- 0.2 V +/- 0.3 V +/- 0.5 V
MIN MAX MIN MAX MIN MAX MIN MAX
fclock Clock frequency 100 125 150 175 MHz
CLR Low 5.6 3 2.8 2.5
tw Pulse duration ns
CLK High or low 3.5 3 2.8 2.5
Data 3 2.5 2 1.5
tsu Setup time, before CLK ns
CLR inactive 0 0 0.5 0.5
th Hold time, data after CLK 0 0 0.5 0.5 ns
6.7 Timing Requirements, -40 deg C to 125 deg C
over recommended operating free-air temperature range (unless otherwise noted) (see Figure 2)
-40 deg C to 125 deg C
VCC = 1.8 V VCC = 2.5 V VCC = 3.3 V VCC = 5 V UNIT+/- 0.15 V +/- 0.2 V +/- 0.3 V +/- 0.5 V
MIN MAX MIN MAX MIN MAX MIN MAX
fclock Clock frequency 100 125 150 175 MHz
CLR Low 5.6 3 2.8 2.5
tw Pulse duration ns
CLK High or low 3.5 3 2.8 2.5
Data 3 2.5 2 1.5
tsu Setup time, before CLK ns
CLR inactive 0.5 0.5 0.7 0.7
th Hold time, data after CLK 0.5 0.5 0.7 0.7 ns
6.8 Switching Characteristics, -40 deg C to 85 deg C
over recommended operating free-air temperature range, CL = 15 pF (unless otherwise noted) (see Figure 2)
-40 deg C to 85 deg C
FROM TO VCC = 1.8 V VCC = 2.5 V VCC = 3.3 V VCC = 5 VPARAMETER UNIT(INPUT) (OUTPUT) +/- 0.15 V +/- 0.2 V +/- 0.3 V +/- 0.5 V
MIN MAX MIN MAX MIN MAX MIN MAX
fmax 100 125 150 175 MHz
CLK 2.5 12.9 2 6.5 1.4 4.6 1 3
tpd Q ns
CLR 2.5 12.4 2 6 1.2 4.3 1 3.2
6.9 Switching Characteristics, -40 deg C to 85 deg C
over recommended operating free-air temperature range, CL = 30 pF or 50 pF (unless otherwise noted) (see Figure 3)
-40 deg C to 85 deg C
FROM TO VCC = 1.8 V VCC = 2.5 V VCC = 3.3 V VCC = 5 VPARAMETER UNIT(INPUT) (OUTPUT) +/- 0.15 V +/- 0.2 V +/- 0.3 V +/- 0.5 V
MIN MAX MIN MAX MIN MAX MIN MAX
fmax 100 125 150 175 MHz
CLK 2.7 13.4 2.2 7.1 1.6 5.7 1.5 4
tpd Q ns
CLR 2.7 12.9 2.2 7 1.5 5.8 1.3 4.1
6 Submit Documentation Feedback Copyright  2004-2015, Texas Instruments Incorporated
Product Folder Links: SN74LVC1G175
```

### Page 7

#### Extracted tables

Table 1:

```text
PARAMETER | FROM (INPUT) | TO (OUTPUT) |  |  |  | 40 deg Ct | o125 deg C |  |  |  | UNIT
 |  |  | VCC= +/-0. | 1.8V 15V | VCC= +/-0. | 2.5V 2V | VCC= +/-0. | 3.3V 3V | VCC +/-0. | =5V 5V | 
 |  |  | MIN | MAX | MIN | MAX | MIN | MAX | MIN | MAX | 
fmax |  |  | 100 |  | 125 |  | 150 |  | 175 |  | MHz
tpd | CLK | Q | 2.7 15.4 |  | 2.2 8.1 |  | 1.6 6.7 |  | 1.5 5 |  | ns
 | CLR |  | 2.7 14.9 |  | 2.2 8 |  | 1.5 6.8 |  | 1.3 5.1 |  |
```

Table 2:

```text
| PARAMETER | TESTCONDITIONS | V =1.8V CC | V =2.5V CC | V =3.3V CC | V =5V CC | UNIT
 |  |  | TYP | TYP | TYP | TYP | 
C Powerdissipationcapacitance pd |  | f=10MHz | 18 | 19 | 19 | 21 | pF
```

Table 3:

```text
|  |  |  |  | Typical &KDUDFWHU
```

#### Raw extracted text

```text
17.5
18
18.5
19
19.5
20
20.5
21
21.5
0 1 2 3 4 5 6
Power Dissipation Capacitance (pF)
Supply Voltage [VCC] (V)
Typical
/c26/c4b/c44/c55/c44/c46/c57/c48/c55/cab
C001
SN74LVC1G175
www.ti.com SCES560G - MARCH 2004 - REVISED JUNE 2015
6.10 Switching Characteristics, -40 deg C to 125 deg C
over recommended operating free-air temperature range, CL = 30 pF or 50 pF (unless otherwise noted) (see Figure 3)
-40 deg C to 125 deg C
FROM TO VCC = 1.8 V VCC = 2.5 V VCC = 3.3 V VCC = 5 VPARAMETER UNIT(INPUT) (OUTPUT) +/- 0.15 V +/- 0.2 V +/- 0.3 V +/- 0.5 V
MIN MAX MIN MAX MIN MAX MIN MAX
fmax 100 125 150 175 MHz
CLK 2.7 15.4 2.2 8.1 1.6 6.7 1.5 5
tpd Q ns
CLR 2.7 14.9 2.2 8 1.5 6.8 1.3 5.1
6.11 Operating Characteristics
TA = 25 deg C
VCC = 1.8 V VCC = 2.5 V VCC = 3.3 V VCC = 5 V
PARAMETER TEST CONDITIONS UNIT
TYP TYP TYP TYP
Cpd Power dissipation capacitance f = 10 MHz 18 19 19 21 pF
6.12 Typical Characteristics
Figure 1. Voltage vs Capacitance
Copyright  2004-2015, Texas Instruments Incorporated Submit Documentation Feedback 7
Product Folder Links: SN74LVC1G175
```

### Page 8

#### Extracted tables

Table 1:

```text
TEST | S1
```

Table 2:

```text
V CC | INPUTS |  | V M | V LOAD | C L | R L | V D
 | V I | t/t r f |  |  |  |  | 
1.8 V+/-0.15 V 2.5 V+/-0.2 V 3.3 V+/-0.3 V 5 V+/-0.5 V | V CC V CC 3 V V CC | 2 ns 2 ns 2.5 ns 2.5 ns | V /2 CC V /2 CC 1.5 V V /2 CC | 2 xV CC 2 xV CC 6 V 2 xV CC | 15 pF 15 pF 15 pF 15 pF | 1 MW 1 MW 1 MW 1 MW | 0.15 V 0.15 V 0.3 V 0.3 V
```

Table 3:

```text
t
W
```

#### Raw extracted text

```text
SN74LVC1G175
SCES560G-MARCH2004-REVISEDJUNE2015 www.ti.com
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
1.8 V+/-0.15 V V 2 ns V /2 2 xV 15 pF 1 MW 0.15 V
CC CC CC
2.5 V+/-0.2 V V 2 ns V /2 2 xV 15 pF 1 MW 0.15 V
CC CC CC
3.3 V+/-0.3 V 3 V 2.5 ns 1.5 V 6 V 15 pF 1 MW 0.3 V
5 V+/-0.5 V V 2.5 ns V /2 2 xV 15 pF 1 MW 0.3 V
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
Figure2. LoadCircuitandVoltageWaveforms
8 SubmitDocumentationFeedback Copyright2004-2015,TexasInstrumentsIncorporated
ProductFolderLinks:SN74LVC1G175
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
SN74LVC1G175
www.ti.com SCES560G-MARCH2004-REVISEDJUNE2015
Parameter Measurement Information (continued)
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
Copyright2004-2015,TexasInstrumentsIncorporated SubmitDocumentationFeedback 9
ProductFolderLinks:SN74LVC1G175
```

### Page 10

#### Extracted tables

Table 1:

```text
| INPUTS |  | OUTPUT Q
CLR | CLK | D | 
H |  | L | L
H |  | H | H
H | HorL | X | Q 0
L | X | X | L
```

#### Raw extracted text

```text
Q
1
6
C1
D
CLR
CLK
D
R
3
4
SN74LVC1G175
SCES560G - MARCH 2004 - REVISED JUNE 2015 www.ti.com
8 Detailed Description
8.1 Overview
This single D-type flip-flop is designed for 1.65-V to 5.5-V VCC operation.
The SN74LVC1G175 device has an asynchronous clear (CLR) input. When CLR is high, data from the input pin
(D) is transferred to the output pin (Q) on the clock's (CLK) rising edge. When CLR is low, Q is forced into the
low state, regardless of the clock edge or data on D.
NanoFree(TM) package technology is a major breakthrough in IC packaging concepts, using the die as the
package.
This device is fully specified for partial-power-down applications using Ioff. The Ioff circuitry disables the outputs,
preventing damaging current backflow through the device when it is powered down.
8.2 Functional Block Diagram
8.3 Feature Description
The SN74LVC1G175 device has a wide operating VCC range of 1.65 V to 5.5 V, which allows it to be used in a
broad range of systems. The 5.5-V I/Os allow down translation and also allow voltages at the inputs when
VCC = 0.
8.4 Device Functional Modes
Table 1 lists the functional modes for SN74LVC1G175.
Table 1. Function Table
INPUTS OUTPUT
QCLR CLK D
H  L L
H  H H
H H or L X Q0
L X X L
10 Submit Documentation Feedback Copyright  2004-2015, Texas Instruments Incorporated
Product Folder Links: SN74LVC1G175
```

### Page 11

#### Extracted tables

Table 1:

```text
SerialInputData | StoredA | StoredB | StoredC | StoredD
1 | 0 | 0 | 0 | 0
0 | 1 | 0 | 0 | 0
1 | 0 | 1 | 0 | 0
1 | 1 | 0 | 1 | 0
0 | 1 | 1 | 0 | 1
```

#### Raw extracted text

```text
SN74LVC1G175
GND
D
VCC = 5 V
CLK
QVCC
Serial
Input Data
Clock
Pulse
SN74LVC1G175
GND
D
CLK
QVCC
SN74LVC1G175
GND
D
CLK
QVCC
SN74LVC1G175
GND
D
CLK
QVCC
Serial
Output Data
A B C D
SN74LVC1G175
www.ti.com SCES560G - MARCH 2004 - REVISED JUNE 2015
9 Application and Implementation
NOTE
Information in the following applications sections is not part of the TI component
specification, and TI does not warrant its accuracy or completeness. TIs customers are
responsible for determining suitability of components for their purposes. Customers should
validate and test their design implementation to confirm system functionality.
9.1 Application Information
Multiple SN74LVC1G175 devices can be used in tandem to create a shift register of arbitrary length. In this
example, we use four SN74LVC1G175 devices to form a 4-bit serial shift register. By connecting all CLK inputs
to a common clock pulse and tying each output of one device to the next, we can store and load 4-bit values on
demand. We demonstrate loading the 4 bit value 1101 into memory by setting Serial Input Data to each desired
memory bit, and by sending a clock pulse for each bit, we sequentially move all stored bits from left to right
(A -> B -> C -> D)
9.2 Typical Application
Figure 4. 4-Bit Serial Shift Register
Table 2. Stored Data Values
Serial Input Data Stored A Stored B Stored C Stored D
1 0 0 0 0
0 1 0 0 0
1 0 1 0 0
1 1 0 1 0
0 1 1 0 1
9.2.1 Design Requirements
The SN74LVC1G175 device uses CMOS technology and has balanced output drive. Care must be taken to
avoid bus contention because it can drive currents that would exceed maximum limits.
The SN74LVC1G175 allows storing digital signals with a digital control signal. All input signals should remain as
close as possible to either 0 V or VCC for optimal operation.
9.2.2 Detailed Design Procedure
1. Recommended input conditions:
- For rise time and fall time specifications, see t/v in the table.
- For specified high and low levels, see VIH and VIL in the table.
- Inputs and outputs are overvoltage tolerant and can therefore go as high as 5.5 V at any valid VCC.
2. Recommended output conditions:
- Load currents should not exceed +/-50 mA.
Copyright  2004-2015, Texas Instruments Incorporated Submit Documentation Feedback 11
Product Folder Links: SN74LVC1G175
```

### Page 12

#### Extracted tables

Table 1:

```text
|  |  | tpd CL= |  |  |  | . F
 |  |  |  | tpd CL= | from C 30 pF | LRtoQ or50 p | . F
 |  |  |  |  | 40 deg C to | 125 deg C |
```

#### Raw extracted text

```text
0.00
5.00
10.00
15.00
20.00
0.00 1.00 2.00 3.00 4.00 5.00 6.00 7.00
Max tpd (ns)
Voltage (V) C001
t from CLR to Q.pd
C = 30  pF or 50 pFL
-  deg   deg 40 C to 125 C
SN74LVC1G175
SCES560G - MARCH 2004 - REVISED JUNE 2015 www.ti.com
3. Frequency selection criterion:
- The effects of frequency upon the output current should be studied in Figure 5.
- Added trace resistance and capacitance can reduce maximum frequency capability; follow the layout
practices listed in the Layout section.
9.2.3 Application Curve
Figure 5. Max tpd vs Voltage of LVC Family
10 Power Supply Recommendations
The power supply can be any voltage between the minimum and maximum supply voltage rating listed in the
table.
Each VCC terminal should have a good bypass capacitor to prevent power disturbance. For devices with a single
supply, a 0.1-uF bypass capacitor is recommended. If multiple pins are labeled VCC, then a 0.01-uF or 0.022-uF
capacitor is recommended for each VCC because the VCC pins are tied together internally. For devices with dual
supply pins operating at different voltages, for example VCC and VDD, a 0.1-uF bypass capacitor is recommended
for each supply pin. To reject different frequencies of noise, use multiple bypass capacitors in parallel. Capacitors
with values of 0.1 uF and 1 uF are commonly used in parallel. The bypass capacitor should be installed as close
to the power terminal as possible for best results.
11 Layout
11.1 Layout Guidelines
When using multiple-bit logic devices, inputs must never float.
In many cases, functions (or parts of functions) of digital logic devices are unused, for example, when only two
inputs of a triple-input AND gate are used or when only 3 of the 4 buffer gates are used. Such input pins must
not be left unconnected, because the undefined voltages at the outside connections result in undefined
operational states. Figure 6 specifies the rules that must be observed under all circumstances. All unused inputs
of digital logic devices must be connected to a high or low bias to prevent them from floating. The logic level that
must be applied to any particular unused input depends on the function of the device. Generally they are tied to
GND or VCC, whichever makes more sense or is more convenient. It is generally acceptable to float outputs,
unless the part is a transceiver. If the transceiver has an output enable pin, it disables the output section of the
part when asserted, which does not disable the input section of the I/Os. Therefore, the I/Os cannot float when
disabled.
12 Submit Documentation Feedback Copyright  2004-2015, Texas Instruments Incorporated
Product Folder Links: SN74LVC1G175
```

### Page 13

#### Raw extracted text

```text
Vcc
Unused Input
Input
Output
Input
Unused Input Output
SN74LVC1G175
www.ti.com SCES560G - MARCH 2004 - REVISED JUNE 2015
11.2 Layout Example
Figure 6. Layout Diagram
Copyright  2004-2015, Texas Instruments Incorporated Submit Documentation Feedback 13
Product Folder Links: SN74LVC1G175
```

### Page 14

#### Raw extracted text

```text
SN74LVC1G175
SCES560G - MARCH 2004 - REVISED JUNE 2015 www.ti.com
12 Device and Documentation Support
12.1 Documentation Support
12.1.1 Related Documentation
For related documentation see the following:
* Implications of Slow or Floating CMOS Inputs, SCBA004
* Selecting the Right Texas Instruments Signal Switch, SZZA030
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
NanoFree, E2E are trademarks of Texas Instruments.
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
this document. For browser based versions of this data sheet, refer to the left hand navigation.
14 Submit Documentation Feedback Copyright  2004-2015, Texas Instruments Incorporated
Product Folder Links: SN74LVC1G175
```

### Page 15

#### Extracted tables

Table 1:

```text
Orderable part number | Status (1) | Material type (2) | Package | Pins | Package qty | Carrier | RoHS (3) | Lead finish/ Ball material (4) | MSL rating/ Peak reflow (5) | Op temp ( deg C) | Part marking (6)
74LVC1G175DBVRE4 | Active | Production | SOT-23 (DBV) | 6 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | (C755, C75R)
74LVC1G175DBVRE4.B | Active | Production | SOT-23 (DBV) | 6 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | (C755, C75R)
74LVC1G175DBVRG4 | Active | Production | SOT-23 (DBV) | 6 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | (C755, C75R)
74LVC1G175DBVRG4.B | Active | Production | SOT-23 (DBV) | 6 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | (C755, C75R)
74LVC1G175DCKRG4 | Active | Production | SC70 (DCK) | 6 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | D65
74LVC1G175DCKRG4.B | Active | Production | SC70 (DCK) | 6 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | D65
74LVC1G175DCKTG4 | Active | Production | SC70 (DCK) | 6 | 250 | SMALL T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | D65
74LVC1G175DCKTG4.B | Active | Production | SC70 (DCK) | 6 | 250 | SMALL T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | D65
SN74LVC1G175DBVR | Active | Production | SOT-23 (DBV) | 6 | 3000 | LARGE T&R | Yes | NIPDAU | SN | Level-1-260C-UNLIM | 40 to 125 | (C755, C75R)
SN74LVC1G175DBVR.B | Active | Production | SOT-23 (DBV) | 6 | 3000 | LARGE T&R | Yes | SN | Level-1-260C-UNLIM | 40 to 125 | (C755, C75R)
SN74LVC1G175DBVT | Active | Production | SOT-23 (DBV) | 6 | 250 | SMALL T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | (C755, C75R)
SN74LVC1G175DBVT.B | Active | Production | SOT-23 (DBV) | 6 | 250 | SMALL T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | (C755, C75R)
SN74LVC1G175DBVTG4 | Active | Production | SOT-23 (DBV) | 6 | 250 | SMALL T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | C75R
SN74LVC1G175DBVTG4.B | Active | Production | SOT-23 (DBV) | 6 | 250 | SMALL T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | C75R
SN74LVC1G175DCKR | Active | Production | SC70 (DCK) | 6 | 3000 | LARGE T&R | Yes | NIPDAU | SN | Level-1-260C-UNLIM | 40 to 125 | (D65, D6J, D6R)
SN74LVC1G175DCKR.B | Active | Production | SC70 (DCK) | 6 | 3000 | LARGE T&R | Yes | SN | Level-1-260C-UNLIM | 40 to 125 | (D65, D6J, D6R)
SN74LVC1G175DCKT | Active | Production | SC70 (DCK) | 6 | 250 | SMALL T&R | Yes | NIPDAU | SN | Level-1-260C-UNLIM | 40 to 125 | (D65, D6J, D6R)
SN74LVC1G175DCKT.B | Active | Production | SC70 (DCK) | 6 | 250 | SMALL T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | (D65, D6J, D6R)
SN74LVC1G175DCKTG4.B | Active | Production | SC70 (DCK) | 6 | 250 | SMALL T&R |  | Call TI | Call TI | 40 to 125 | 
SN74LVC1G175DRYR | Active | Production | SON (DRY) | 6 | 5000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | D6
SN74LVC1G175DRYR.B | Active | Production | SON (DRY) | 6 | 5000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | D6
SN74LVC1G175DRYRG4.B | Active | Production | SON (DRY) | 6 | 5000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | D6
SN74LVC1G175YZPR | Active | Production | DSBGA (YZP) | 6 | 3000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | 40 to 85 | D6N
SN74LVC1G175YZPR.B | Active | Production | DSBGA (YZP) | 6 | 3000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | 40 to 85 | D6N
```

#### Raw extracted text

```text
PACKAGE OPTION ADDENDUM
www.ti.com 7-Oct-2025
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
74LVC1G175DBVRE4 Active Production SOT-23 (DBV) | 6 3000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 (C755, C75R)
74LVC1G175DBVRE4.B Active Production SOT-23 (DBV) | 6 3000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 (C755, C75R)
74LVC1G175DBVRG4 Active Production SOT-23 (DBV) | 6 3000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 (C755, C75R)
74LVC1G175DBVRG4.B Active Production SOT-23 (DBV) | 6 3000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 (C755, C75R)
74LVC1G175DCKRG4 Active Production SC70 (DCK) | 6 3000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 D65
74LVC1G175DCKRG4.B Active Production SC70 (DCK) | 6 3000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 D65
74LVC1G175DCKTG4 Active Production SC70 (DCK) | 6 250 | SMALL T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 D65
74LVC1G175DCKTG4.B Active Production SC70 (DCK) | 6 250 | SMALL T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 D65
SN74LVC1G175DBVR Active Production SOT-23 (DBV) | 6 3000 | LARGE T&R Yes NIPDAU | SN Level-1-260C-UNLIM -40 to 125 (C755, C75R)
SN74LVC1G175DBVR.B Active Production SOT-23 (DBV) | 6 3000 | LARGE T&R Yes SN Level-1-260C-UNLIM -40 to 125 (C755, C75R)
SN74LVC1G175DBVT Active Production SOT-23 (DBV) | 6 250 | SMALL T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 (C755, C75R)
SN74LVC1G175DBVT.B Active Production SOT-23 (DBV) | 6 250 | SMALL T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 (C755, C75R)
SN74LVC1G175DBVTG4 Active Production SOT-23 (DBV) | 6 250 | SMALL T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 C75R
SN74LVC1G175DBVTG4.B Active Production SOT-23 (DBV) | 6 250 | SMALL T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 C75R
SN74LVC1G175DCKR Active Production SC70 (DCK) | 6 3000 | LARGE T&R Yes NIPDAU | SN Level-1-260C-UNLIM -40 to 125 (D65, D6J, D6R)
SN74LVC1G175DCKR.B Active Production SC70 (DCK) | 6 3000 | LARGE T&R Yes SN Level-1-260C-UNLIM -40 to 125 (D65, D6J, D6R)
SN74LVC1G175DCKT Active Production SC70 (DCK) | 6 250 | SMALL T&R Yes NIPDAU | SN Level-1-260C-UNLIM -40 to 125 (D65, D6J, D6R)
SN74LVC1G175DCKT.B Active Production SC70 (DCK) | 6 250 | SMALL T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 (D65, D6J, D6R)
SN74LVC1G175DCKTG4.B Active Production SC70 (DCK) | 6 250 | SMALL T&R - Call TI Call TI -40 to 125
SN74LVC1G175DRYR Active Production SON (DRY) | 6 5000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 D6
SN74LVC1G175DRYR.B Active Production SON (DRY) | 6 5000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 D6
SN74LVC1G175DRYRG4.B Active Production SON (DRY) | 6 5000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 D6
SN74LVC1G175YZPR Active Production DSBGA (YZP) | 6 3000 | LARGE T&R Yes SNAGCU Level-1-260C-UNLIM -40 to 85 D6N
SN74LVC1G175YZPR.B Active Production DSBGA (YZP) | 6 3000 | LARGE T&R Yes SNAGCU Level-1-260C-UNLIM -40 to 85 D6N

(1) Status:  For more details on status, see our product life cycle.

(2) Material type:  When designated, preproduction parts are prototypes/experimental devices, and are not yet approved or released for full production. Testing and final process, including without limitation quality assurance,
reliability performance testing, and/or process qualification, may not yet be complete, and this item is subject to further changes or possible discontinuation. If available for ordering, purchases will be subject to an additional
waiver at checkout, and are intended for early internal evaluation purposes only. These items are sold without warranties of any kind.
Addendum-Page 1
```

### Page 16

#### Raw extracted text

```text
PACKAGE OPTION ADDENDUM
www.ti.com 7-Oct-2025

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

 OTHER QUALIFIED VERSIONS OF SN74LVC1G175 :
* Enhanced Product : SN74LVC1G175-EP
 NOTE: Qualified Version Definitions:
* Enhanced Product - Supports Defense, Aerospace and Medical Applications
Addendum-Page 2
```

### Page 17

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
74LVC1G175DBVRE4 | SOT-23 | DBV | 6 | 3000 | 180.0 | 8.4 | 3.23 | 3.17 | 1.37 | 4.0 | 8.0 | Q3
74LVC1G175DBVRE4 | SOT-23 | DBV | 6 | 3000 | 178.0 | 9.2 | 3.3 | 3.23 | 1.55 | 4.0 | 8.0 | Q3
74LVC1G175DBVRG4 | SOT-23 | DBV | 6 | 3000 | 178.0 | 9.2 | 3.3 | 3.23 | 1.55 | 4.0 | 8.0 | Q3
74LVC1G175DBVRG4 | SOT-23 | DBV | 6 | 3000 | 180.0 | 8.4 | 3.23 | 3.17 | 1.37 | 4.0 | 8.0 | Q3
74LVC1G175DCKRG4 | SC70 | DCK | 6 | 3000 | 178.0 | 9.2 | 2.4 | 2.4 | 1.22 | 4.0 | 8.0 | Q3
74LVC1G175DCKTG4 | SC70 | DCK | 6 | 250 | 178.0 | 9.2 | 2.4 | 2.4 | 1.22 | 4.0 | 8.0 | Q3
SN74LVC1G175DBVR | SOT-23 | DBV | 6 | 3000 | 178.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3
SN74LVC1G175DBVT | SOT-23 | DBV | 6 | 250 | 180.0 | 8.4 | 3.23 | 3.17 | 1.37 | 4.0 | 8.0 | Q3
SN74LVC1G175DBVT | SOT-23 | DBV | 6 | 250 | 178.0 | 9.2 | 3.3 | 3.23 | 1.55 | 4.0 | 8.0 | Q3
SN74LVC1G175DBVTG4 | SOT-23 | DBV | 6 | 250 | 180.0 | 8.4 | 3.23 | 3.17 | 1.37 | 4.0 | 8.0 | Q3
SN74LVC1G175DCKR | SC70 | DCK | 6 | 3000 | 178.0 | 8.4 | 2.25 | 2.45 | 1.2 | 4.0 | 8.0 | Q3
SN74LVC1G175DCKT | SC70 | DCK | 6 | 250 | 178.0 | 9.0 | 2.4 | 2.5 | 1.2 | 4.0 | 8.0 | Q3
SN74LVC1G175DRYR | SON | DRY | 6 | 5000 | 180.0 | 9.5 | 1.2 | 1.65 | 0.7 | 4.0 | 8.0 | Q1
SN74LVC1G175YZPR | DSBGA | YZP | 6 | 3000 | 178.0 | 9.2 | 1.02 | 1.52 | 0.63 | 4.0 | 8.0 | Q1
```

#### Raw extracted text

```text
PACKAGE MATERIALS INFORMATION
www.ti.com 16-Apr-2026
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
74LVC1G175DBVRE4 SOT-23 DBV 6 3000 180.0 8.4 3.23 3.17 1.37 4.0 8.0 Q3
74LVC1G175DBVRE4 SOT-23 DBV 6 3000 178.0 9.2 3.3 3.23 1.55 4.0 8.0 Q3
74LVC1G175DBVRG4 SOT-23 DBV 6 3000 178.0 9.2 3.3 3.23 1.55 4.0 8.0 Q3
74LVC1G175DBVRG4 SOT-23 DBV 6 3000 180.0 8.4 3.23 3.17 1.37 4.0 8.0 Q3
74LVC1G175DCKRG4 SC70 DCK 6 3000 178.0 9.2 2.4 2.4 1.22 4.0 8.0 Q3
74LVC1G175DCKTG4 SC70 DCK 6 250 178.0 9.2 2.4 2.4 1.22 4.0 8.0 Q3
SN74LVC1G175DBVR SOT-23 DBV 6 3000 178.0 8.4 3.2 3.2 1.4 4.0 8.0 Q3
SN74LVC1G175DBVT SOT-23 DBV 6 250 180.0 8.4 3.23 3.17 1.37 4.0 8.0 Q3
SN74LVC1G175DBVT SOT-23 DBV 6 250 178.0 9.2 3.3 3.23 1.55 4.0 8.0 Q3
SN74LVC1G175DBVTG4 SOT-23 DBV 6 250 180.0 8.4 3.23 3.17 1.37 4.0 8.0 Q3
SN74LVC1G175DCKR SC70 DCK 6 3000 178.0 8.4 2.25 2.45 1.2 4.0 8.0 Q3
SN74LVC1G175DCKT SC70 DCK 6 250 178.0 9.0 2.4 2.5 1.2 4.0 8.0 Q3
SN74LVC1G175DRYR SON DRY 6 5000 180.0 9.5 1.2 1.65 0.7 4.0 8.0 Q1
SN74LVC1G175YZPR DSBGA YZP 6 3000 178.0 9.2 1.02 1.52 0.63 4.0 8.0 Q1
Pack Materials-Page 1
```

### Page 18

#### Extracted tables

Table 1:

```text
| H
```

Table 2:

```text
Device | Package Type | Package Drawing | Pins | SPQ | Length (mm) | Width (mm) | Height (mm)
74LVC1G175DBVRE4 | SOT-23 | DBV | 6 | 3000 | 202.0 | 201.0 | 28.0
74LVC1G175DBVRE4 | SOT-23 | DBV | 6 | 3000 | 180.0 | 180.0 | 18.0
74LVC1G175DBVRG4 | SOT-23 | DBV | 6 | 3000 | 180.0 | 180.0 | 18.0
74LVC1G175DBVRG4 | SOT-23 | DBV | 6 | 3000 | 202.0 | 201.0 | 28.0
74LVC1G175DCKRG4 | SC70 | DCK | 6 | 3000 | 180.0 | 180.0 | 18.0
74LVC1G175DCKTG4 | SC70 | DCK | 6 | 250 | 180.0 | 180.0 | 18.0
SN74LVC1G175DBVR | SOT-23 | DBV | 6 | 3000 | 208.0 | 191.0 | 35.0
SN74LVC1G175DBVT | SOT-23 | DBV | 6 | 250 | 202.0 | 201.0 | 28.0
SN74LVC1G175DBVT | SOT-23 | DBV | 6 | 250 | 180.0 | 180.0 | 18.0
SN74LVC1G175DBVTG4 | SOT-23 | DBV | 6 | 250 | 202.0 | 201.0 | 28.0
SN74LVC1G175DCKR | SC70 | DCK | 6 | 3000 | 208.0 | 191.0 | 35.0
SN74LVC1G175DCKT | SC70 | DCK | 6 | 250 | 180.0 | 180.0 | 18.0
SN74LVC1G175DRYR | SON | DRY | 6 | 5000 | 189.0 | 185.0 | 36.0
SN74LVC1G175YZPR | DSBGA | YZP | 6 | 3000 | 220.0 | 220.0 | 35.0
```

#### Raw extracted text

```text
PACKAGE MATERIALS INFORMATION

www.ti.com 16-Apr-2026
TAPE AND REEL BOX DIMENSIONS
Width (mm)
W LH

*All dimensions are nominal
Device Package Type Package Drawing Pins SPQ Length (mm) Width (mm) Height (mm)
74LVC1G175DBVRE4 SOT-23 DBV 6 3000 202.0 201.0 28.0
74LVC1G175DBVRE4 SOT-23 DBV 6 3000 180.0 180.0 18.0
74LVC1G175DBVRG4 SOT-23 DBV 6 3000 180.0 180.0 18.0
74LVC1G175DBVRG4 SOT-23 DBV 6 3000 202.0 201.0 28.0
74LVC1G175DCKRG4 SC70 DCK 6 3000 180.0 180.0 18.0
74LVC1G175DCKTG4 SC70 DCK 6 250 180.0 180.0 18.0
SN74LVC1G175DBVR SOT-23 DBV 6 3000 208.0 191.0 35.0
SN74LVC1G175DBVT SOT-23 DBV 6 250 202.0 201.0 28.0
SN74LVC1G175DBVT SOT-23 DBV 6 250 180.0 180.0 18.0
SN74LVC1G175DBVTG4 SOT-23 DBV 6 250 202.0 201.0 28.0
SN74LVC1G175DCKR SC70 DCK 6 3000 208.0 191.0 35.0
SN74LVC1G175DCKT SC70 DCK 6 250 180.0 180.0 18.0
SN74LVC1G175DRYR SON DRY 6 5000 189.0 185.0 36.0
SN74LVC1G175YZPR DSBGA YZP 6 3000 220.0 220.0 35.0
Pack Materials-Page 2
```

### Page 19

#### Extracted tables

Table 1:

```text
| 0.1 | C
```

Table 2:

```text
|  | 0.1 | C | A | B
```

#### Raw extracted text

```text
www.ti.com
PACKAGE OUTLINE
C
0.22
0.08 TYP
0.15
2.4
1.8
4X 0.65
1.1
0.8
0.1
0.0 TYP
6X 0.30
0.15
NOTE 5
0.46
0.26 TYP
8
0  TYP
1.3
4X 0 -12
4X 4 -15
A
2.15
1.85
B1.4
1.1
SOT - 1.1 max heightDCK0006A
SMALL OUTLINE TRANSISTOR
4214835/D   11/2024
NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
    per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. Body dimensions do not include mold flash or protrusion. Mold flash and protrusion shall not exceed 0.15 per side.
4. Falls within JEDEC MO-203 variation AB.
1
3
4
6
2
INDEX AREA
PIN 1
NOTE 5
0.1 C A B
GAGE PLANE
SEATING PLANE
0.1 C
SCALE  5.600
```

### Page 20

#### Raw extracted text

```text
www.ti.com
EXAMPLE BOARD LAYOUT
0.07 MAX
ARROUND
0.07 MIN
ARROUND
6X (0.9)
6X (0.4)
(2.2)
4X (0.65)
(R0.05) TYP
4214835/D   11/2024
SOT - 1.1 max heightDCK0006A
SMALL OUTLINE TRANSISTOR
NOTES: (continued)

5. Publication IPC-7351 may have alternate designs.
6. Solder mask tolerances between and around signal pads can vary based on board fabrication site.

SYMM
LAND PATTERN EXAMPLE
EXPOSED METAL SHOWN
SCALE:18X
PKG
1
3 4
6
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

### Page 21

#### Raw extracted text

```text
www.ti.com
EXAMPLE STENCIL DESIGN
(2.2)
4X(0.65)
6X (0.9)
6X (0.4)
(R0.05) TYP
SOT - 1.1 max heightDCK0006A
SMALL OUTLINE TRANSISTOR
4214835/D   11/2024
NOTES: (continued)

7. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
     design recommendations.
8. Board assembly site may have different recommendations for stencil design.

SOLDER PASTE EXAMPLE
BASED ON 0.125 THICK STENCIL
SCALE:18X
SYMM
PKG
1
3 4
6
2
```

### Page 22

#### Raw extracted text

```text
GENERIC PACKAGE VIEW
Images above are just a representation of the package family, actual package may vary.
Refer to the product data sheet for package details.
DRY 6 USON - 0.6 mm max height
PLASTIC SMALL OUTLINE - NO LEAD
4207181/G
```

### Page 23

#### Extracted tables

Table 1:

```text
C | A | B
```

#### Raw extracted text

```text
www.ti.com
PACKAGE OUTLINE
C
6X 0.25
0.15
4X
0.5
5X 0.35
0.25
2X
1
0.6 MAX
0.05
0.00
3X 0.6
0.4
0.3
B 1.05
0.95
A
1.5
1.4
(0.05) TYP (0.127) TYP
4222894/A   01/2018
USON - 0.6 mm max heightDRY0006A
PLASTIC SMALL OUTLINE - NO LEAD
PIN 1 INDEX AREA
SEATING PLANE
0.08 C
1
3 4
6
(OPTIONAL)
PIN 1 ID
0.1 C A B
0.05 C
SYMM
SYMM
NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
    per ASME Y14.5M.
2. This drawing is subject to change without notice.
SCALE  8.500
```

### Page 24

#### Raw extracted text

```text
www.ti.com
EXAMPLE BOARD LAYOUT
0.05 MIN
ALL AROUND
0.05 MAX
ALL AROUND
5X (0.3)
6X (0.2)
4X (0.5)
(0.6)
(R0.05) TYP
(0.35)
4222894/A   01/2018
USON - 0.6 mm max heightDRY0006A
PLASTIC SMALL OUTLINE - NO LEAD
SYMM
1
3 4
6
SYMM
LAND PATTERN EXAMPLE
1:1 RATIO WITH PKG SOLDER PADS
EXPOSED METAL SHOWN
SCALE:40X
NOTES: (continued)

3. For more information, see QFN/SON PCB application report in literature No. SLUA271 (www.ti.com/lit/slua271).

METALSOLDER MASK
OPENING
SOLDER MASK DETAILS
NON SOLDER MASK
DEFINED
EXPOSED
METAL
SOLDER MASK
OPENING
METAL UNDER
SOLDER MASK
SOLDER MASK
DEFINED
(PREFERRED)
EXPOSED
METAL
```

### Page 25

#### Raw extracted text

```text
www.ti.com
EXAMPLE STENCIL DESIGN
5X (0.3)
6X (0.2)
4X (0.5)
(0.6)(R0.05) TYP
(0.35)
4222894/A   01/2018
USON - 0.6 mm max heightDRY0006A
PLASTIC SMALL OUTLINE - NO LEAD
NOTES: (continued)

4. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
   design recommendations.

SOLDER PASTE EXAMPLE
BASED ON 0.075 - 0.1 mm THICK STENCIL
SCALE:40X
SYMM
1
3 4
6
SYMM
```

### Page 26

#### Extracted tables

Table 1:

```text
C | A | B
```

#### Raw extracted text

```text
www.ti.com
PACKAGE OUTLINE
C
6X 0.25
0.15
4X
0.5
6X 0.35
0.25
2X
1
0.55 MAX
0.05
0.00
3X 0.6
B 1.05
0.95
A
1.5
1.4
(0.05) TYP (0.127) TYP
4222207/B   02/2016
USON - 0.55 mm max heightDRY0006B
PLASTIC SMALL OUTLINE - NO LEAD
PIN 1 INDEX AREA
SEATING PLANE
0.08 C
1
3 4
6
(OPTIONAL)
PIN 1 ID 0.1 C A B
0.05 C
SYMM
SYMM
NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
    per ASME Y14.5M.
2. This drawing is subject to change without notice.
SCALE  8.500
```

### Page 27

#### Raw extracted text

```text
www.ti.com
EXAMPLE BOARD LAYOUT
0.05 MIN
ALL AROUND
0.05 MAX
ALL AROUND
6X (0.3)
6X (0.2)
4X (0.5)
(0.6)
(R ) TYP0.05
4222207/B   02/2016
USON - 0.55 mm max heightDRY0006B
PLASTIC SMALL OUTLINE - NO LEAD
SYMM
1
3 4
6
SYMM
LAND PATTERN EXAMPLE
1:1 RATIO WITH PKG SOLDER PADS
SCALE:40X
NOTES: (continued)

3. For more information, see QFN/SON PCB application report in literature No. SLUA271 (www.ti.com/lit/slua271).

METALSOLDER MASK
OPENING
SOLDER MASK DETAILS
NON SOLDER MASK
DEFINED
SOLDER MASK
OPENING
METAL UNDER
SOLDER MASK
SOLDER MASK
DEFINED
(PREFERRED)
```

### Page 28

#### Raw extracted text

```text
www.ti.com
EXAMPLE STENCIL DESIGN
6X (0.3)
6X (0.2)
4X (0.5)
(0.6)(R ) TYP0.05
4222207/B   02/2016
USON - 0.55 mm max heightDRY0006B
PLASTIC SMALL OUTLINE - NO LEAD
NOTES: (continued)

4. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
   design recommendations.

SOLDER PASTE EXAMPLE
BASED ON 0.075 - 0.1 mm THICK STENCIL
SCALE:40X
SYMM
1
3 4
6
SYMM
```

### Page 29

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
1.45
0.90
0.15
0.00 TYP
6X 0.50
0.25
0.6
0.3 TYP
8
0  TYP
1.9
4X 0 -15
4X 4 -15
A
3.05
2.75
B1.75
1.45
(1.1)
SOT-23 - 1.45 mm max heightDBV0006A
SMALL OUTLINE TRANSISTOR
4214840/G   08/2024
NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
    per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. Body dimensions do not include mold flash or protrusion. Mold flash and protrusion shall not exceed 0.25 per side.
4. Leads 1,2,3 may be wider than leads 4,5,6 for package orientation.
5. Refernce JEDEC MO-178.
0.2 C A B
1
3
4
52
INDEX AREA
PIN 1
6
GAGE PLANE
SEATING PLANE
0.1 C
SCALE  4.000
```

### Page 30

#### Raw extracted text

```text
www.ti.com
EXAMPLE BOARD LAYOUT
0.07 MAX
ARROUND
0.07 MIN
ARROUND
6X (1.1)
6X (0.6)
(2.6)
2X (0.95)
(R0.05) TYP
4214840/G   08/2024
SOT-23 - 1.45 mm max heightDBV0006A
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
52
6
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

### Page 31

#### Raw extracted text

```text
www.ti.com
EXAMPLE STENCIL DESIGN
(2.6)
2X(0.95)
6X (1.1)
6X (0.6)
(R0.05) TYP
SOT-23 - 1.45 mm max heightDBV0006A
SMALL OUTLINE TRANSISTOR
4214840/G   08/2024
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
52
6
```

### Page 32

#### Extracted tables

Table 1:

```text
|  | 0.015 | C | A | B
```

#### Raw extracted text

```text
www.ti.com
PACKAGE OUTLINE
C0.5 MAX
0.19
0.15
1
TYP
0.5 TYP
6X 0.25
0.21
0.5
TYP
B E A
D
4219524/A   06/2014
DSBGA - 0.5 mm max heightYZP0006
DIE SIZE BALL GRID ARRAY
NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
    per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. NanoFree
TM
 package configuration.
NanoFree Is a trademark of Texas Instruments.
BALL A1
CORNER
SEATING PLANE
BALL TYP 0.05 C
B
A
1 2
0.015 C A B
SYMM
SYMM
C
SCALE  9.000
D: Max =
E: Max =
1.418 mm, Min =
0.918 mm, Min =
1.358 mm
0.858 mm
```

### Page 33

#### Raw extracted text

```text
www.ti.com
EXAMPLE BOARD LAYOUT
6X ( ) 0.225
(0.5) TYP
(0.5) TYP
( )
METAL
0.225 0.05 MAX
SOLDER MASK
OPENING
METAL
UNDER
MASK
(
)
SOLDER MASK
OPENING
0.225
0.05 MIN
4219524/A   06/2014
DSBGA - 0.5 mm max heightYZP0006
DIE SIZE BALL GRID ARRAY
NOTES: (continued)

4. Final dimensions may vary due to manufacturing tolerance considerations and also routing constraints.
    For more information, see Texas Instruments literature number SBVA017 (www.ti.com/lit/sbva017).

SYMM
SYMM
LAND PATTERN EXAMPLE
SCALE:40X
1 2
A
B
C
NON-SOLDER MASK
DEFINED
(PREFERRED)
SOLDER MASK DETAILS
NOT TO SCALE
SOLDER MASK
DEFINED
```

### Page 34

#### Raw extracted text

```text
www.ti.com
EXAMPLE STENCIL DESIGN
(0.5)
TYP
(0.5) TYP
6X ( 0.25) (R ) TYP 0.05
METAL
TYP
4219524/A   06/2014
DSBGA - 0.5 mm max heightYZP0006
DIE SIZE BALL GRID ARRAY
NOTES: (continued)

5. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release.
SYMM
SYMM
SOLDER PASTE EXAMPLE
BASED ON 0.1 mm THICK STENCIL
SCALE:40X
1 2
A
B
C
```

### Page 35

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
