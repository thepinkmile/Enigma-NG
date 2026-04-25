# SN74LVC1G08 - Single 2-input positive-AND gate

## Source Reference

- Source PDF: [TI-sn74lvc1g08-datasheet.pdf](TI-sn74lvc1g08-datasheet.pdf)
- Source path: `design\Datasheets\TI-sn74lvc1g08-datasheet.pdf`
- Generated markdown: `TI-sn74lvc1g08-datasheet.md`
- Review note: manually checked against the source PDF; curated summary added and the raw page-by-page extraction is preserved below.

## Part Identity and Ordering

- Texas Instruments `SN74LVC1G08`, single 2-input positive-AND gate.
- Device-information packages called out on page 1:
  - SOT-23 (5), 2.9 mm x 1.6 mm.
  - SC70 (5), 2.0 mm x 1.25 mm.
  - X2SON / DPW (4), 0.8 mm x 0.8 mm.
  - SON (6), 1.45 mm x 1.0 mm.
  - SON (6), 1.0 mm x 1.0 mm.
- The orderable addendum includes current orderables such as `SN74LVC1G08DBVR`, `SN74LVC1G08DBVT`, `SN74LVC1G08DCKR`, and `SN74LVC1G08DRLR`, with package-specific tape options and markings.

## Pin / Pad Designations

- Common logical signals are:
  - `A` input
  - `B` input
  - `Y` output
  - `GND`
  - `VCC`
- Package pin numbering differs by footprint; page 3 provides the package-specific pin-function table.
- `NC` is present on the 6-pin `DRY` / `DSF` variants.

## Ratings and Operating Conditions

- Operating supply range: 1.65 V to 5.5 V.
- Feature callouts include 5.5 V tolerant inputs, down translation to `VCC`, `tpd` about 3.6 ns at 3.3 V, `ICC` 10 uA max, and +/-24 mA output drive at 3.3 V.
- Absolute maximum highlights: `VCC` and `VI` from -0.5 V to +6.5 V, output clamp and input clamp current up to 50 mA, continuous current through `VCC` or `GND` up to 100 mA, `TJ(max)` 150 deg C.
- ESD ratings called out on page 4: 2000 V HBM and 1000 V CDM.

## Package and Mechanical Notes

- Package coverage spans SOT-23, SC70, DRL, DRY, YZP, DSF, and DPW styles in the full datasheet and addendum.
- The DPW / X2SON option is the smallest footprint and is explicitly highlighted in the feature list.

## Formulas / Logic Content

- Primary logic relationship: `Y = A * B` in positive logic.
- No special analog design equations are central to the datasheet.

## Applications and Reference Design Content

- The PDF includes a typical application using the device as a high-drive logic / LED buffer.
- Design guidance covers rise/fall-time limits, load-current limits, and layout / ringing considerations for fast CMOS edges.

## Searchability Note

- The raw page-by-page extraction below is intentionally preserved for local text search.
- Package-specific orderable tables are extensive and remain easier to inspect in the addendum pages of the PDF.

## Page-by-page extracted content

### Page 1

#### Extracted tables

Table 1:

```text
DEVICENAME | PACKAGE | BODYSIZE
SN74LVC1G08 | SOT-23(5) | 2.9mmx1.6mm
 | SC70(5) | 2.0mmx1.25mm
 | X2SON(4) | 0.8mmx0.8mm
 | SON(6) | 1.45mmx1.0mm
 | SON(6) | 1.0mmx1.0mm
```

#### Raw extracted text

```text
Y = A * B or Y = + A B
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
SN74LVC1G08
SCES217Z - APRIL 1999 - REVISED MAY 2019
SN74LVC1G08Single2-InputPositive-ANDGate
1
1 Features
1* Available in the Ultra Small 0.64-mm2
Package (DPW) With 0.5-mm Pitch
* Supports 5-V VCC Operation
* Inputs Accept Voltages to 5.5 V
* Provides Down Translation to VCC
* Max tpd of 3.6 ns at 3.3 V
* Low Power Consumption, 10-uA Max ICC
* +/-24-mA Output Drive at 3.3 V
* Ioff Supports Live Insertion, Partial-Power-Down
Mode, and Back Drive Protection
* Latch-Up Performance Exceeds 100 mA
Per JESD 78, Class II
* ESD Protection Exceeds JESD 22
- 2000-V Human-Body Model (A114-A)
- 200-V Machine Model (A115-A)
- 1000-V Charged-Device Model (C101)
2 Applications
* ATCA Solutions
* Active Noise Cancellation (ANC)
* Barcode Scanner
* Blood Pressure Monitor
* CPAP Machine
* Cable Solutions
* DLP 3D Machine Vision, Hyperspectral Imaging,
Optical Networking, and Spectroscopy
* E-Book
* Embedded PC
* Field Transmitter: Temperature or Pressure
Sensor
* Fingerprint Biometrics
* HVAC: Heating, Ventilating, and Air Conditioning
* Network-Attached Storage (NAS)
* Server Motherboard and PSU
* Software Defined Radio (SDR)
* TV: High-Definition (HDTV), LCD, and Digital
* Video Communications System
* Wireless Data Access Card, Headset, Keyboard,
Mouse, and LAN Card
* X-ray: Baggage Scanner, Medical, and Dental
3 Description
This single 2-input positive-AND gate is designed for
1.65-V to 5.5-V VCC operation.
The SN74LVC1G08 device performs the Boolean
function or in positive logic.
The CMOS device has high output drive while
maintaining low static power dissipation over a broad
VCC operating range.
The SN74LVC1G08 is available in a variety of
packages, including the ultra-small DPW package
with a body size of 0.8 mm x 0.8 mm.
white space
white space
Device Information(1)
DEVICE NAME PACKAGE BODY SIZE
SN74LVC1G08
SOT-23 (5) 2.9mm x 1.6mm
SC70 (5) 2.0mm x 1.25mm
X2SON (4) 0.8mm x 0.8mm
SON (6) 1.45mm x 1.0mm
SON (6) 1.0mm x 1.0mm
(1) For all available packages, see the orderable addendum at
the end of the datasheet.
```

### Page 2

#### Raw extracted text

```text
2
SN74LVC1G08
SCES217Z - APRIL 1999 - REVISED MAY 2019 www.ti.com
Product Folder Links: SN74LVC1G08
Submit Documentation Feedback Copyright  1999-2019, Texas Instruments Incorporated
Table of Contents
1 Features .................................................................. 1
2 Applications ........................................................... 1
3 Description ............................................................. 1
4 Revision History..................................................... 2
5 Pin Configuration and Functions ......................... 3
6 Specifications......................................................... 4
6.1 Absolute Maximum Ratings ..................................... 4
6.2 ESD Ratings.............................................................. 4
6.3 Recommended Operating Conditions ...................... 5
6.4 Thermal Information .................................................. 5
6.5 Electrical Characteristics........................................... 6
6.6 Switching Characteristics, CL = 15 pF ...................... 6
6.7 Switching Characteristics, 1.8 V and 2.5 V .............. 6
6.8 Switching Characteristics, 3.3 V and 5 V ................. 7
6.9 Operating Characteristics.......................................... 7
6.10 Typical Characteristics ............................................ 7
7 Parameter Measurement Information .................. 8
8 Detailed Description ............................................ 10
8.1 Overview ................................................................. 10
8.2 Functional Block Diagram ....................................... 10
8.3 Feature Description................................................. 10
8.4 Device Functional Modes........................................ 10
9 Application and Implementation ........................ 11
9.1 Application Information............................................ 11
9.2 Typical Application ................................................. 11
10 Power Supply Recommendations ..................... 12
11 Layout................................................................... 12
11.1 Layout Guidelines ................................................. 12
11.2 Layout Example .................................................... 12
12 Device and Documentation Support ................. 13
12.1 Trademarks ........................................................... 13
12.2 Electrostatic Discharge Caution ............................ 13
12.3 Glossary ................................................................ 13
13 Mechanical, Packaging, and Orderable
Information ........................................................... 13
4 Revision History
Changes from Revision Y (April 2014) to Revision Z Page
* Added TJ(max) spec to Absolute Maximum Ratings table ..................................................................................................... 4
* Moved Tstg spec from Handling Ratings table to Absolute Maximum Ratings table. ............................................................. 4
* Renamed Handling Ratings table to ESD Ratings table ....................................................................................................... 4
Changes from Revision X (March 2014) to Revision Y Page
* Updated Handling Ratings table. ........................................................................................................................................... 4
* Added Thermal Information table. ......................................................................................................................................... 5
* Added Typical Characteristics. .............................................................................................................................................. 7
* Added Detailed Description section. .................................................................................................................................... 10
* Added Application and Implementation section. ................................................................................................................. 11
* Added Power Supply Recommendations section. .............................................................................................................. 12
* Added Layout section. ......................................................................................................................................................... 12
Changes from Revision W (July 2013) to Revision X Page
* Added Applications. ................................................................................................................................................................ 1
* Added Device Information table. ............................................................................................................................................ 1
* Moved Tstg to Handling Ratings table. .................................................................................................................................... 4
Changes from Revision V (November 2012) to Revision W Page
* Added parameter values for -40 to 125 deg C temperature ratings............................................................................................. 6
```

### Page 3

#### Extracted tables

Table 1:

```text
|  | 1 5 2 3 4 |  |
```

Table 2:

```text
| 1 5 2 3 4 |
```

Table 3:

```text
1
2
```

Table 4:

```text
6
5
```

Table 5:

```text
| PI | N |  | DESCRIPTION
NAME | DBV,DCK, DRL,YZP | DRY,DSF | DPW | 
A | 1 | 1 | 2 | Input
B | 2 | 2 | 1 | Input
GND | 3 | 3 | 3 | Ground
Y | 4 | 4 | 4 | Output
VCC | 5 | 6 | 5 | Powerpin
NC |  | 5 |  | Notconnected
```

#### Raw extracted text

```text
DBV PACKAGE
(TOP VIEW)
2
5
3 4 Y
1
B
GND
A VCC
DCK PACKAGE
(TOP VIEW)
3 4GND
2B
Y
1A 5 VCC
DRL PACKAGE
(TOP VIEW)
2B
1A
3 4GND Y
5 VCC
1 5
2
3
A
GND
Y
VCC
DPW PACKAGE
(TOP VIEW)
B
4
GND
DRY PACKAGE
(TOP VIEW)
B NC
A 6
5
4
2
3 Y
VCC1
YZP PACKAGE
(BOTTOM VIEW)
2B
1A
GND 43 Y
5 VCC
6
5
4
2
3
1
DSF PACKAGE
(TOP VIEW)
B
A
GND
NC
Y
VCC
3
SN74LVC1G08
www.ti.com SCES217Z - APRIL 1999 - REVISED MAY 2019
Product Folder Links: SN74LVC1G08
Submit Documentation FeedbackCopyright  1999-2019, Texas Instruments Incorporated
5 Pin Configuration and Functions
NC - No internal connection
See mechanical drawings for dimensions.
Pin Functions
PIN
DESCRIPTION
NAME DBV, DCK,
DRL, YZP DRY, DSF DPW
A 1 1 2 Input
B 2 2 1 Input
GND 3 3 3 Ground
Y 4 4 4 Output
VCC 5 6 5 Power pin
NC 5 Not connected
```

### Page 4

#### Extracted tables

Table 1:

```text
|  |  | MIN | MAX | UNIT
V Supplyvoltagerange CC |  |  | 0.5 6.5 |  | V
V Inputvoltagerange(2) I |  |  | 0.5 6.5 |  | V
V Voltagerangeappliedtoanyoutputinthehigh-impedanceorpower-offstate(2) O |  |  | 0.5 6.5 |  | V
V Voltagerangeappliedtoanyoutputinthehighorlowstate(2)(3) O |  |  | 0.5 V +0.5 CC |  | V
I Inputclampcurrent IK |  | V <0 I | 50 |  | mA
I Outputclampcurrent OK |  | V <0 O | 50 |  | mA
I Continuousoutputcurrent O |  |  | +/-50 |  | mA
ContinuouscurrentthroughV orGND CC |  |  | +/-100 |  | mA
T(max) Junctiontemperature J |  |  | 150 |  | deg C
T Storagetemperature stg |  |  | 65 150 |  | deg C
```

Table 2:

```text
|  |  | MIN | MAX | UNIT
V (ESD) | Electrostaticdischarge | Humanbodymodel(HBM),perANSI/ESDA/JEDECJS-001,all pins(1) | 0 2000 |  | V
 |  | Chargeddevicemodel(CDM),perJEDECspecification JESD22-C101,allpins(2) | 0 1000 |  |
```

#### Raw extracted text

```text
4
SN74LVC1G08
SCES217Z - APRIL 1999 - REVISED MAY 2019 www.ti.com
Product Folder Links: SN74LVC1G08
Submit Documentation Feedback Copyright  1999-2019, Texas Instruments Incorporated
(1) Stresses beyond those listed under Absolute Maximum Ratings may cause permanent damage to the device. These are stress ratings
only, and functional operation of the device at these or any other conditions beyond those indicated under Recommended Operating
Conditions is not implied. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability.
(2) The input and output negative-voltage ratings may be exceeded if the input and output current ratings are observed.
(3) The value of VCC is provided in the Recommended Operating Conditions table.
6 Specifications
6.1 Absolute Maximum Ratings (1)
over operating free-air temperature range (unless otherwise noted)
MIN MAX UNIT
VCC Supply voltage range -0.5 6.5 V
VI Input voltage range (2) -0.5 6.5 V
VO Voltage range applied to any output in the high-impedance or power-off state (2) -0.5 6.5 V
VO Voltage range applied to any output in the high or low state (2) (3) -0.5 VCC + 0.5 V
IIK Input clamp current VI < 0 -50 mA
IOK Output clamp current VO < 0 -50 mA
IO Continuous output current +/-50 mA
Continuous current through VCC or GND +/-100 mA
TJ(max) Junction temperature 150  deg C
Tstg Storage temperature -65 150  deg C
(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process.
(2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process.
6.2 ESD Ratings
MIN MAX UNIT
V(ESD) Electrostatic discharge
Human body model (HBM), per ANSI/ESDA/JEDEC JS-001, all
pins (1) 0 2000
V
Charged device model (CDM), per JEDEC specification
JESD22-C101, all pins (2) 0 1000
```

### Page 5

#### Extracted tables

Table 1:

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
I Low-leveloutputcurrent OL |  | V =1.65V CC | 4 |  | mA
 |  | V =2.3V CC | 8 |  | 
 |  | V =3V CC | 16 |  | 
 |  |  | 24 |  | 
 |  | V =4.5V CC | 32 |  | 
t/v Inputtransitionriseorfallrate |  | V =1.8V+/-0.15V,2.5V+/-0.2V CC | 20 |  | ns/V
 |  | V =3.3V+/-0.3V CC | 10 |  | 
 |  | V =5V+/-0.5V CC | 5 |  | 
T Operatingfree-airtemperature A |  |  | 40 125 |  | deg C
```

Table 2:

```text
| THERMALMETRIC(1) |  |  | SN74LV | C1G08 |  |  | UNIT
 |  | DBV | DCK | DRL | DRY | YZP | DPW | 
 |  | 5PINS | 5PINS | 5PINS | 6PINS | 5PINS | 4PINS | 
R JA Junction-to-ambientthermalresistance |  | 207.6 | 283.1 | 242.9 | 438.8 | 130 | 340 | deg C/W
R JCtop Junction-to-case(top)thermalresistance |  | 145.2 | 92.3 | 77.5 | 276.8 | 54 | 215 | deg C/W
R JB Junction-to-boardthermalresistance |  | 53.5 | 60.9 | 77.5 | 271.7 | 51 | 294 | deg C/W
JT Junction-to-topcharacterizationparameter |  | 37.5 | 1.7 | 9.6 | 83.8 | 1 | 41 | deg C/W
JB Junction-to-boardcharacterizationparameter |  | 53.1 | 60.1 | 77.3 | 271.4 | 50 | 294 | deg C/W
R JCbot Junction-to-case(bottom)thermalresistance |  |  |  |  |  |  | 250 | deg C/W
```

#### Raw extracted text

```text
5
SN74LVC1G08
www.ti.com SCES217Z - APRIL 1999 - REVISED MAY 2019
Product Folder Links: SN74LVC1G08
Submit Documentation FeedbackCopyright  1999-2019, Texas Instruments Incorporated
(1) All unused inputs of the device must be held at VCC or GND to ensure proper device operation. Refer to the TI application report,
Implications of Slow or Floating CMOS Inputs, literature number SCBA004.
6.3 Recommended Operating Conditions (1)
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
VO Output voltage 0 VCC V
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
(1) For more information about traditional and new thermal metrics, see the Semiconductor and IC package thermal metrics application
report
6.4 Thermal Information
THERMAL METRIC (1)
SN74LVC1G08
UNITDBV DCK DRL DRY YZP DPW
5 PINS 5 PINS 5 PINS 6 PINS 5 PINS 4 PINS
RJA Junction-to-ambient thermal resistance 207.6 283.1 242.9 438.8 130 340  deg C/W
RJCtop Junction-to-case (top) thermal resistance 145.2 92.3 77.5 276.8 54 215  deg C/W
RJB Junction-to-board thermal resistance 53.5 60.9 77.5 271.7 51 294  deg C/W
JT Junction-to-top characterization parameter 37.5 1.7 9.6 83.8 1 41  deg C/W
JB Junction-to-board characterization parameter 53.1 60.1 77.3 271.4 50 294  deg C/W
RJCbot Junction-to-case (bottom) thermal resistance - - - - - 250  deg C/W
```

### Page 6

#### Extracted tables

Table 1:

```text
PA | RAMETER | TESTCONDIT | IONS | VCC | 40 deg | Cto85 deg C |  | 40 deg C RECO | to125 deg C MMENDE | D | UNIT
 |  |  |  |  | MIN | TYP(1) | MAX | MIN | TYP | MAX | 
VOH |  | IOH=-100uA |  | 1.65Vto5.5V | VCC -0.1 |  |  | VCC -0.15 |  |  | V
 |  | IOH=-4mA |  | 1.65V | 1.2 |  |  | 1.2 |  |  | 
 |  | IOH=-8mA |  | 2.3V | 1.9 |  |  | 1.9 |  |  | 
 |  | IOH=-16mA |  | 3V | 2.4 |  |  | 2.4 |  |  | 
 |  | IOH=-24mA |  |  | 2.3 |  |  | 2.3 |  |  | 
 |  | IOH=-32mA |  | 4.5V | 3.8 |  |  | 3.8 |  |  | 
VOL |  | IOL=100uA |  | 1.65Vto5.5V | 0.1 |  |  | 0.1 |  |  | V
 |  | IOL=4mA |  | 1.65V | 0.45 |  |  | 0.45 |  |  | 
 |  | IOL=8mA |  | 2.3V | 0.3 |  |  | 0.3 |  |  | 
 |  | IOL=16mA |  | 3V | 0.4 |  |  | 0.4 |  |  | 
 |  | IOL=24mA |  |  | 0.55 |  |  | 0.55 |  |  | 
 |  | IOL=32mA |  | 4.5V | 0.55 |  |  | 0.55 |  |  | 
II | AorB inputs | VI=5.5VorGND |  | 0to5.5V | +/-5 |  |  | +/-5 |  |  | uA
Ioff |  | VIorVO=5.5V |  | 0 | +/-10 |  |  | +/-10 |  |  | uA
ICC |  | VI=5.5VorGND, IO=0 |  | 1.65Vto5.5V | 10 |  |  | 10 |  |  | uA
ICC |  | OneinputatVCC-0.6V, OtherinputsatVCCorGND |  | 3Vto5.5V | 500 |  |  | 500 |  |  | uA
Ci |  | VI=VCCorGND |  | 3.3V | 4 |  |  | 4 |  |  | pF
```

Table 2:

```text
PARAMETER | FROM (INPUT) | TO (OUTPUT) |  |  |  | 40 deg Ct | o85 deg C |  |  |  | UNIT
 |  |  | V = CC +/-0. | 1.8V 15V | V = CC +/-0 | 2.5V .2V | V = CC +/-0. | 3.3V 3V | V = CC +/-0. | 5V 5V | 
 |  |  | MIN | MAX | MIN | MAX | MIN | MAX | MIN | MAX | 
t pd | AorB | Y | 1.5 7.2 |  | 0.7 4.4 |  | 0.8 3.6 |  | 0.8 3.4 |  | ns
```

Table 3:

```text
PARAMETER | FROM (INPUT) | TO (OUTPUT) | 40 deg Ct | o85 deg C | 40 deg Ct | o125 deg C | 40 deg Ct | o85 deg C | 40 deg Ct | o125 deg C MENDED 2.5V 2V MAX | UNIT
 |  |  |  |  | RECOM | MENDED |  |  | RECOM |  | 
 |  |  | VCC= +/-0. | 1.8V 15V | VCC= +/-0. | 1.8V 15V | VCC= +/-0. | 2.5V 2V | VCC= +/-0. |  | 
 |  |  | MIN | MAX | MIN | MAX | MIN | MAX | MIN |  | 
tpd | AorB | Y | 2.4 8 |  | 2.4 10 |  | 1.1 5.5 |  | 1.1 7 |  | ns
```

#### Raw extracted text

```text
6
SN74LVC1G08
SCES217Z - APRIL 1999 - REVISED MAY 2019 www.ti.com
Product Folder Links: SN74LVC1G08
Submit Documentation Feedback Copyright  1999-2019, Texas Instruments Incorporated
(1) All typical values are at VCC = 3.3 V, TA = 25 deg C.
6.5 Electrical Characteristics
over recommended operating free-air temperature range (unless otherwise noted)
PARAMETER TEST CONDITIONS VCC
-40 deg C to 85 deg C -40 deg C to 125 deg C
RECOMMENDED UNIT
MIN TYP (1) MAX MIN TYP MAX
VOH
IOH = -100 uA 1.65 V to 5.5 V VCC - 0.1 VCC - 0.15
V
IOH = -4 mA 1.65 V 1.2 1.2
IOH = -8 mA 2.3 V 1.9 1.9
IOH = -16 mA
3 V
2.4 2.4
IOH = -24 mA 2.3 2.3
IOH = -32 mA 4.5 V 3.8 3.8
VOL
IOL = 100 uA 1.65 V to 5.5 V 0.1 0.1
V
IOL = 4 mA 1.65 V 0.45 0.45
IOL = 8 mA 2.3 V 0.3 0.3
IOL = 16 mA
3 V
0.4 0.4
IOL = 24 mA 0.55 0.55
IOL = 32 mA 4.5 V 0.55 0.55
II
A or B
inputs VI = 5.5 V or GND 0 to 5.5 V +/-5 +/-5 uA
Ioff VI or VO = 5.5 V 0 +/-10 +/-10 uA
ICC VI = 5.5 V or GND, IO = 0 1.65 V to 5.5 V 10 10 uA
ICC
One input at VCC - 0.6 V,
Other inputs at VC C or GND 3 V to 5.5 V 500 500 uA
Ci VI = VCC or GND 3.3 V 4 4 pF
6.6 Switching Characteristics, CL = 15 pF
over recommended operating free-air temperature range (unless otherwise noted) (see Figure 3)
PARAMETER FROM
(INPUT)
TO
(OUTPUT)
-40 deg C to 85 deg C
UNITVCC = 1.8 V
+/- 0.15 V
VCC = 2.5 V
+/- 0.2 V
VCC = 3.3 V
+/- 0.3 V
VCC = 5 V
+/- 0.5 V
MIN MAX MIN MAX MIN MAX MIN MAX
tpd A or B Y 1.5 7.2 0.7 4.4 0.8 3.6 0.8 3.4 ns
(1) On products compliant to MIL-PRF-38535, this parameter is not production tested.
6.7 Switching Characteristics, 1.8 V and 2.5 V (1)
over recommended operating free-air temperature range, (unless otherwise noted) (see Figure 4)
PARAMETER FROM
(INPUT)
TO
(OUTPUT)
-40 deg C to 85 deg C
-40 deg C to 125 deg C
-40 deg C to 85 deg C
-40 deg C to 125 deg C
UNIT
RECOMMENDED RECOMMENDED
VCC = 1.8 V
+/- 0.15 V
VCC = 1.8 V
+/- 0.15 V
VCC = 2.5 V
+/- 0.2 V
VCC = 2.5 V
+/- 0.2 V
MIN MAX MIN MAX MIN MAX MIN MAX
tpd A or B Y 2.4 8 2.4 10 1.1 5.5 1.1 7 ns
```

### Page 7

#### Extracted tables

Table 1:

```text
PARAMETER | FROM (INPUT) | TO (OUTPUT) | 40 deg Ct | o85 deg C | 40 deg Ct | o125 deg C | 40 deg Ct | o85 deg C | 40 deg Ct | o125 deg C | UNIT
 |  |  |  |  | RECOM | MENDED |  |  | RECOM | MENDED | 
 |  |  | VCC= +/-0. | 3.3V 3V | VCC= +/-0. | 3.3V 3V | VCC +/-0. | =5V 5V | VCC +/-0 | =5V .5V | 
 |  |  | MIN | MAX | MIN | MAX | MIN | MAX | MIN | MAX | 
tpd | AorB | Y | 1 4.5 |  | 1 6 |  | 1 4 |  | 1 5 |  | ns
```

Table 2:

```text
| PARAMETER |  | TEST CONDITIONS | V =1.8V CC | V =2.5V CC | V =3.3V CC | V =5V CC | UNIT
 |  |  |  | TYP | TYP | TYP | TYP | 
C Powerdissipationcapacitance pd |  |  | f=10MHz | 21 | 24 | 26 | 31 | pF
```

Table 3:

```text
6 5 4 sn - DPT 3 2 1 TPD 0 -100 -50 0 50 100 150 Temperature - deg C D001 Figure1.TPDAcrossTemperatureat3.3VVcc | 8 TPD 7 6 5 sn - DPT 4 3 2 1 0 0 1 2 3 4 5 6 Vcc - V D002 Figure2.TPDAcrossVccat25 deg C
```

Table 4:

```text
|  |  |  | TPD
```

Table 5:

```text
|  |  |  |  |  | TPD
```

#### Raw extracted text

```text
Temperature -  deg  C
TPD - ns
-100 -50 0 50 100 150
0
1
2
3
4
5
6
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
6
7
8
D002
TPD
7
SN74LVC1G08
www.ti.com SCES217Z - APRIL 1999 - REVISED MAY 2019
Product Folder Links: SN74LVC1G08
Submit Documentation FeedbackCopyright  1999-2019, Texas Instruments Incorporated
(1) On products compliant to MIL-PRF-38535, this parameter is not production tested.
6.8 Switching Characteristics, 3.3 V and 5 V (1)
over recommended operating free-air temperature range, CL = 30 pF or 50 pF (unless otherwise noted) (see Figure 4)
PARAMETER FROM
(INPUT)
TO
(OUTPUT)
-40 deg C to 85 deg C
-40 deg C to 125 deg C
-40 deg C to 85 deg C
-40 deg C to 125 deg C
UNIT
RECOMMENDED RECOMMENDED
VCC = 3.3 V
+/- 0.3 V
VCC = 3.3 V
+/- 0.3 V
VCC = 5 V
+/- 0.5 V
VCC = 5 V
+/- 0.5 V
MIN MAX MIN MAX MIN MAX MIN MAX
tpd A or B Y 1 4.5 1 6 1 4 1 5 ns
6.9 Operating Characteristics
TA = 25 deg C
PARAMETER TEST
CONDITIONS
VCC = 1.8 V VCC = 2.5 V VCC = 3.3 V VCC = 5 V
UNIT
TYP TYP TYP TYP
Cpd Power dissipation capacitance f = 10 MHz 21 24 26 31 pF
6.10 Typical Characteristics
Figure 1. TPD Across Temperature at 3.3V Vcc Figure 2. TPD Across Vcc at 25 deg C
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
SN74LVC1G08
SCES217Z-APRIL1999-REVISEDMAY2019 www.ti.com
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
Figure3. LoadCircuitandVoltageWaveforms
8 SubmitDocumentationFeedback Copyright1999-2019,TexasInstrumentsIncorporated
ProductFolderLinks:SN74LVC1G08
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
SN74LVC1G08
www.ti.com SCES217Z-APRIL1999-REVISEDMAY2019
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
Figure4. LoadCircuitandVoltageWaveforms
Copyright1999-2019,TexasInstrumentsIncorporated SubmitDocumentationFeedback 9
ProductFolderLinks:SN74LVC1G08
```

### Page 10

#### Extracted tables

Table 1:

```text
INP | UTS | OUTPUT Y
A | B | 
H H L X X L |  | H L L
```

#### Raw extracted text

```text
Y = A * B or Y = + A B
10
SN74LVC1G08
SCES217Z - APRIL 1999 - REVISED MAY 2019 www.ti.com
Product Folder Links: SN74LVC1G08
Submit Documentation Feedback Copyright  1999-2019, Texas Instruments Incorporated
8 Detailed Description
8.1 Overview
The SN74LVC1G08 device contains one 2-input positive AND gate device and performs the Boolean function
. This device is fully specified for partial-power-down applications using Ioff. The Ioff circuitry
disables the outputs, preventing damaging current backflow through the device when it is powered down.
The DPW package technology is a major breakthrough in IC packaging. Its tiny 0.64 mm square footprint saves
significant board space over other package options while still retaining the traditional manufacturing friendly lead
pitch of 0.5 mm.
8.2 Functional Block Diagram
8.3 Feature Description
* Wide operating voltage range.
- Operates from 1.65 V to 5.5 V.
* Allows down voltage translation.
* Inputs accept voltages to 5.5 V.
* Ioff feature allows voltages on the inputs and outputs when VCC is 0 V.
8.4 Device Functional Modes
Table 1. Function Table
INPUTS OUTPUT
YA B
H H H
L X L
X L L
```

### Page 11

#### Raw extracted text

```text
LVC1G08
A- uC or Logic
B- uC or Logic
Basic LED Driver
A- uC or Logic
B- uC or Logic
Y- uC or Logic
AND Logic Function
LVC1G08
VCC VCC
11
SN74LVC1G08
www.ti.com SCES217Z - APRIL 1999 - REVISED MAY 2019
Product Folder Links: SN74LVC1G08
Submit Documentation FeedbackCopyright  1999-2019, Texas Instruments Incorporated
9 Application and Implementation
9.1 Application Information
The SN74LVC1G08 is a high drive CMOS device that can be used for implementing AND logic with a high output
drive, such as an LED application. It can produce 24 mA of drive current at 3.3 V making it Ideal for driving
multiple outputs and good for high speed applications up to 100 MHz. The inputs are 5.5 V tolerant allowing it to
translate down to VCC.
9.2 Typical Application
9.2.1 Design Requirements
This device uses CMOS technology and has balanced output drive. Care should be taken to avoid bus
contention because it can drive currents that would exceed maximum limits. The high drive will also create fast
edges into light loads so routing and load conditions should be considered to prevent ringing.
9.2.2 Detailed Design Procedure
1. Recommended Input Conditions
- Rise time and fall time specs. See (t/V) in the Recommended Operating Conditions table.
- Specified high and low levels. See (VIH and VIL) in the Recommended Operating Conditions table.
- Inputs are overvoltage tolerant allowing them to go as high as (VI max) in the Recommended Operating
Conditions table at any valid VCC.
2. Recommend Output Conditions
- Load currents should not exceed (IO max) per output and should not exceed total current (continuous
current through VCC or GND) for the part. These limits are located in the Absolute Maximum Ratings
table.
- Outputs should not be pulled above VCC.
```

### Page 12

#### Extracted tables

Table 1:

```text
Icc 1. Icc 2. | 8V 5V |  |  |  | 
Icc 3. Icc 5V | 3V |  |  |  |
```

#### Raw extracted text

```text
VCC
Unused Input
Input
Output Output
Input
Unused Input
Frequency - MHz
Icc - mA
-20 0 20 40 60 80
-2
0
2
4
6
8
10
D003
Icc 1.8V
Icc 2.5V
Icc 3.3V
Icc 5V
12
SN74LVC1G08
SCES217Z - APRIL 1999 - REVISED MAY 2019 www.ti.com
Product Folder Links: SN74LVC1G08
Submit Documentation Feedback Copyright  1999-2019, Texas Instruments Incorporated
Typical Application (continued)
9.2.3 Application Curves
Figure 5. Icc vs Frequency
10 Power Supply Recommendations
The power supply can be any voltage between the min and max supply voltage rating located in the
Recommended Operating Conditions table.
Each Vcc pin should have a good bypass capacitor to prevent power disturbance. For devices with a single
supply, a 0.1-uF capacitor is recommended and if there are multiple Vcc pins then 0.01-uF or 0.022-uF capacitor
is recommended for each power pin. It is ok to parallel multiple bypass capacitors to reject different frequencies
of noise. 0.1-uF and 1-uF capacitors are commonly used in parallel. The bypass capacitor should be installed as
close to the power pin as possible for best results.
11 Layout
11.1 Layout Guidelines
When using multiple bit logic devices inputs should not ever float. In many cases, functions or parts of functions
of digital logic devices are unused; for example, when only two inputs of a triple-input AND gate are used or only
3 of the 4 buffer gates are used. Such input pins should not be left unconnected because the undefined voltages
at the outside connections result in undefined operational states. Specified below are the rules that must be
observed under all circumstances. All unused inputs of digital logic devices must be connected to a high or low
bias to prevent them from floating. The logic level that should be applied to any particular unused input depends
on the function of the device. Generally they will be tied to Gnd or Vcc whichever make more sense or is more
convenient.
11.2 Layout Example
```

### Page 13

#### Raw extracted text

```text
13
SN74LVC1G08
www.ti.com SCES217Z - APRIL 1999 - REVISED MAY 2019
Product Folder Links: SN74LVC1G08
Submit Documentation FeedbackCopyright  1999-2019, Texas Instruments Incorporated
12 Device and Documentation Support
12.1 Trademarks
All trademarks are the property of their respective owners.
12.2 Electrostatic Discharge Caution
These devices have limited built-in ESD protection. The leads should be shorted together or the device placed in conductive foam
during storage or handling to prevent electrostatic damage to the MOS gates.
12.3 Glossary
SLYZ022 - TI Glossary.
This glossary lists and explains terms, acronyms, and definitions.
13 Mechanical, Packaging, and Orderable Information
The following pages include mechanical packaging and orderable information. This information is the most
current data available for the designated devices. This data is subject to change without notice and revision of
this document. For browser-based versions of this data sheet, refer to the left-hand navigation.
```

### Page 14

#### Extracted tables

Table 1:

```text
Orderable part number | Status (1) | Material type (2) | Package | Pins | Package qty | Carrier | RoHS (3) | Lead finish/ Ball material (4) | MSL rating/ Peak reflow (5) | Op temp ( deg C) | Part marking (6)
SN74LVC1G08DBVR | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | SN | Level-1-260C-UNLIM | 40 to 125 | (C085, C08F, C08J, C08K, C08R, C 08T) (C08P, C08S)
SN74LVC1G08DBVR.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | SN | Level-1-260C-UNLIM | 40 to 125 | (C085, C08F, C08J, C08K, C08R, C 08T) (C08P, C08S)
SN74LVC1G08DBVR.B | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | SN | Level-1-260C-UNLIM | 40 to 125 | (C085, C08F, C08J, C08K, C08R, C 08T) (C08P, C08S)
SN74LVC1G08DBVRE4 | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | C08 C08P
SN74LVC1G08DBVRG4 | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | C08 C08P
SN74LVC1G08DBVRG4.A | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | C08 C08P
SN74LVC1G08DBVRG4.B | Active | Production | SOT-23 (DBV) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | C08 C08P
SN74LVC1G08DBVT | Active | Production | SOT-23 (DBV) | 5 | 250 | SMALL T&R | Yes | NIPDAU | SN | Level-1-260C-UNLIM | 40 to 125 | (C085, C08F, C08J, C08K, C08R) (C08H, C08P, C08S)
SN74LVC1G08DBVT.B | Active | Production | SOT-23 (DBV) | 5 | 250 | SMALL T&R | Yes | SN | Level-1-260C-UNLIM | 40 to 125 | (C085, C08F, C08J, C08K, C08R) (C08H, C08P, C08S)
SN74LVC1G08DBVTE4 | Active | Production | SOT-23 (DBV) | 5 | 250 | SMALL T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | C08 C08P
SN74LVC1G08DBVTG4.B | Active | Production | SOT-23 (DBV) | 5 | 250 | SMALL T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | C08 C08P
 | Last Time Buy |  | SC70 (DCK) | 5 |  | Yes |  | Level-1-260C-UNLIM |  | (CEF, CEZ)
```

#### Raw extracted text

```text
PACKAGE OPTION ADDENDUM
www.ti.com 20-Apr-2026
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
SN74LVC1G08DBVR Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes NIPDAU | SN Level-1-260C-UNLIM -40 to 125 (C085, C08F, C08J,
     C08K, C08R, C
     08T)
(C08P, C08S)
SN74LVC1G08DBVR.A Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes SN Level-1-260C-UNLIM -40 to 125 (C085, C08F, C08J,
     C08K, C08R, C
     08T)
(C08P, C08S)
SN74LVC1G08DBVR.B Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes SN Level-1-260C-UNLIM -40 to 125 (C085, C08F, C08J,
     C08K, C08R, C
     08T)
(C08P, C08S)
SN74LVC1G08DBVRE4 Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 C08
C08P
SN74LVC1G08DBVRG4 Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 C08
C08P
SN74LVC1G08DBVRG4.A Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 C08
C08P
SN74LVC1G08DBVRG4.B Active Production SOT-23 (DBV) | 5 3000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 C08
C08P
SN74LVC1G08DBVT Active Production SOT-23 (DBV) | 5 250 | SMALL T&R Yes NIPDAU | SN Level-1-260C-UNLIM -40 to 125 (C085, C08F, C08J,
     C08K, C08R)
(C08H, C08P, C08S)

SN74LVC1G08DBVT.B Active Production SOT-23 (DBV) | 5 250 | SMALL T&R Yes SN Level-1-260C-UNLIM -40 to 125 (C085, C08F, C08J,
     C08K, C08R)
(C08H, C08P, C08S)

SN74LVC1G08DBVTE4 Active Production SOT-23 (DBV) | 5 250 | SMALL T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 C08
C08P
SN74LVC1G08DBVTG4.B Active Production SOT-23 (DBV) | 5 250 | SMALL T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 C08
C08P
SN74LVC1G08DCK3 Last
Time Buy
Production SC70 (DCK) | 5 3000 | LARGE T&R Yes SNBI Level-1-260C-UNLIM -40 to 125 (CEF, CEZ)
Addendum-Page 1
```

### Page 15

#### Extracted tables

Table 1:

```text
Orderable part number | Status (1) | Material type (2) | Package | Pins | Package qty | Carrier | RoHS (3) | Lead finish/ Ball material (4) | MSL rating/ Peak reflow (5) | Op temp ( deg C) | Part marking (6)
SN74LVC1G08DCK3.B | Last Time Buy | Production | SC70 (DCK) | 5 | 3000 | LARGE T&R | Yes | SNBI | Level-1-260C-UNLIM | 40 to 125 | (CEF, CEZ)
SN74LVC1G08DCKR | Active | Production | SC70 (DCK) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | SN | Level-1-260C-UNLIM | 40 to 125 | (CE5, CEF, CEJ, CE K, CER, CET) (CEH, CEP, CES)
SN74LVC1G08DCKR.A | Active | Production | SC70 (DCK) | 5 | 3000 | LARGE T&R | Yes | SN | Level-1-260C-UNLIM | 40 to 125 | (CE5, CEF, CEJ, CE K, CER, CET) (CEH, CEP, CES)
SN74LVC1G08DCKR.B | Active | Production | SC70 (DCK) | 5 | 3000 | LARGE T&R | Yes | SN | Level-1-260C-UNLIM | 40 to 125 | (CE5, CEF, CEJ, CE K, CER, CET) (CEH, CEP, CES)
SN74LVC1G08DCKRE4 | Active | Production | SC70 (DCK) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | CE5 CES
SN74LVC1G08DCKRG4 | Active | Production | SC70 (DCK) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | CE5 CES
SN74LVC1G08DCKRG4.B | Active | Production | SC70 (DCK) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | CE5 CES
SN74LVC1G08DCKT | Active | Production | SC70 (DCK) | 5 | 250 | SMALL T&R | Yes | NIPDAU | SN | Level-1-260C-UNLIM | 40 to 125 | (CE5, CEF, CEJ, CE K, CER, CET) (CEH, CEP, CES)
SN74LVC1G08DCKT.B | Active | Production | SC70 (DCK) | 5 | 250 | SMALL T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | (CE5, CEF, CEJ, CE K, CER, CET) (CEH, CEP, CES)
SN74LVC1G08DCKTE4 | Active | Production | SC70 (DCK) | 5 | 250 | SMALL T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | CE5 CES
SN74LVC1G08DCKTG4 | Active | Production | SC70 (DCK) | 5 | 250 | SMALL T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | CE5 CES
SN74LVC1G08DCKTG4.B | Active | Production | SC70 (DCK) | 5 | 250 | SMALL T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | CE5 CES
SN74LVC1G08DPWR | Active | Production | X2SON (DPW) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | M4
SN74LVC1G08DPWR.B | Active | Production | X2SON (DPW) | 5 | 3000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | M4
SN74LVC1G08DRLR | Active | Production | SOT-5X3 (DRL) | 5 | 4000 | LARGE T&R | Yes | NIPDAUAG | Level-1-260C-UNLIM | 40 to 125 | (CE7, CER)
SN74LVC1G08DRLR.A | Active | Production | SOT-5X3 (DRL) | 5 | 4000 | LARGE T&R | Yes | NIPDAUAG | Level-1-260C-UNLIM | 40 to 125 | (CE7, CER)
SN74LVC1G08DRLR.B | Active | Production | SOT-5X3 (DRL) | 5 | 4000 | LARGE T&R | Yes | NIPDAUAG | Level-1-260C-UNLIM | 40 to 125 | (CE7, CER)
 | Active |  | SOT-5X3 (DRL) | 5 |  | Yes |  | Level-1-260C-UNLIM |  | (CE7, CER)
```

#### Raw extracted text

```text
PACKAGE OPTION ADDENDUM
www.ti.com 20-Apr-2026
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
SN74LVC1G08DCK3.B Last
Time Buy
Production SC70 (DCK) | 5 3000 | LARGE T&R Yes SNBI Level-1-260C-UNLIM -40 to 125 (CEF, CEZ)
SN74LVC1G08DCKR Active Production SC70 (DCK) | 5 3000 | LARGE T&R Yes NIPDAU | SN Level-1-260C-UNLIM -40 to 125 (CE5, CEF, CEJ, CE
     K, CER, CET)
(CEH, CEP, CES)
SN74LVC1G08DCKR.A Active Production SC70 (DCK) | 5 3000 | LARGE T&R Yes SN Level-1-260C-UNLIM -40 to 125 (CE5, CEF, CEJ, CE
     K, CER, CET)
(CEH, CEP, CES)
SN74LVC1G08DCKR.B Active Production SC70 (DCK) | 5 3000 | LARGE T&R Yes SN Level-1-260C-UNLIM -40 to 125 (CE5, CEF, CEJ, CE
     K, CER, CET)
(CEH, CEP, CES)
SN74LVC1G08DCKRE4 Active Production SC70 (DCK) | 5 3000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 CE5
CES
SN74LVC1G08DCKRG4 Active Production SC70 (DCK) | 5 3000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 CE5
CES
SN74LVC1G08DCKRG4.B Active Production SC70 (DCK) | 5 3000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 CE5
CES
SN74LVC1G08DCKT Active Production SC70 (DCK) | 5 250 | SMALL T&R Yes NIPDAU | SN Level-1-260C-UNLIM -40 to 125 (CE5, CEF, CEJ, CE
     K, CER, CET)
(CEH, CEP, CES)
SN74LVC1G08DCKT.B Active Production SC70 (DCK) | 5 250 | SMALL T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 (CE5, CEF, CEJ, CE
     K, CER, CET)
(CEH, CEP, CES)
SN74LVC1G08DCKTE4 Active Production SC70 (DCK) | 5 250 | SMALL T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 CE5
CES
SN74LVC1G08DCKTG4 Active Production SC70 (DCK) | 5 250 | SMALL T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 CE5
CES
SN74LVC1G08DCKTG4.B Active Production SC70 (DCK) | 5 250 | SMALL T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 CE5
CES
SN74LVC1G08DPWR Active Production X2SON (DPW) | 5 3000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 M4
SN74LVC1G08DPWR.B Active Production X2SON (DPW) | 5 3000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 M4
SN74LVC1G08DRLR Active Production SOT-5X3 (DRL) | 5 4000 | LARGE T&R Yes NIPDAUAG Level-1-260C-UNLIM -40 to 125 (CE7, CER)
SN74LVC1G08DRLR.A Active Production SOT-5X3 (DRL) | 5 4000 | LARGE T&R Yes NIPDAUAG Level-1-260C-UNLIM -40 to 125 (CE7, CER)
SN74LVC1G08DRLR.B Active Production SOT-5X3 (DRL) | 5 4000 | LARGE T&R Yes NIPDAUAG Level-1-260C-UNLIM -40 to 125 (CE7, CER)
SN74LVC1G08DRLRG4 Active Production SOT-5X3 (DRL) | 5 4000 | LARGE T&R Yes NIPDAUAG Level-1-260C-UNLIM -40 to 125 (CE7, CER)
Addendum-Page 2
```

### Page 16

#### Extracted tables

Table 1:

```text
Orderable part number | Status (1) | Material type (2) | Package | Pins | Package qty | Carrier | RoHS (3) | Lead finish/ Ball material (4) | MSL rating/ Peak reflow (5) | Op temp ( deg C) | Part marking (6)
SN74LVC1G08DRY2 | Active | Production | SON (DRY) | 6 | 5000 | LARGE T&R | Yes | NIPDAU | NIPDAUAG | Level-1-260C-UNLIM | 40 to 125 | CE
SN74LVC1G08DRY2.B | Active | Production | SON (DRY) | 6 | 5000 | LARGE T&R | Yes | NIPDAUAG | Level-1-260C-UNLIM | 40 to 125 | CE
SN74LVC1G08DRYR | Active | Production | SON (DRY) | 6 | 5000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | CE
SN74LVC1G08DRYR.B | Active | Production | SON (DRY) | 6 | 5000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | CE
SN74LVC1G08DRYRG4 | Active | Production | SON (DRY) | 6 | 5000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | CE
SN74LVC1G08DRYRG4.B | Active | Production | SON (DRY) | 6 | 5000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | CE
SN74LVC1G08DSF2 | Active | Production | SON (DSF) | 6 | 5000 | LARGE T&R | Yes | NIPDAU | NIPDAUAG | Level-1-260C-UNLIM | 40 to 125 | CE
SN74LVC1G08DSF2.B | Active | Production | SON (DSF) | 6 | 5000 | LARGE T&R | Yes | NIPDAUAG | Level-1-260C-UNLIM | 40 to 125 | CE
SN74LVC1G08DSFR | Active | Production | SON (DSF) | 6 | 5000 | LARGE T&R | Yes | NIPDAU | NIPDAUAG | Level-1-260C-UNLIM | 40 to 125 | CE
SN74LVC1G08DSFR.B | Active | Production | SON (DSF) | 6 | 5000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | CE
SN74LVC1G08DSFRG4 | Active | Production | SON (DSF) | 6 | 5000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | CE
SN74LVC1G08DSFRG4.B | Active | Production | SON (DSF) | 6 | 5000 | LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | 40 to 125 | CE
SN74LVC1G08YZPR | Active | Production | DSBGA (YZP) | 5 | 3000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | 40 to 85 | (CE, CE7)
SN74LVC1G08YZPR.B | Active | Production | DSBGA (YZP) | 5 | 3000 | LARGE T&R | Yes | SNAGCU | Level-1-260C-UNLIM | 40 to 85 | (CE, CE7)
```

#### Raw extracted text

```text
PACKAGE OPTION ADDENDUM
www.ti.com 20-Apr-2026
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
SN74LVC1G08DRY2 Active Production SON (DRY) | 6 5000 | LARGE T&R Yes NIPDAU | NIPDAUAG Level-1-260C-UNLIM -40 to 125 CE
SN74LVC1G08DRY2.B Active Production SON (DRY) | 6 5000 | LARGE T&R Yes NIPDAUAG Level-1-260C-UNLIM -40 to 125 CE
SN74LVC1G08DRYR Active Production SON (DRY) | 6 5000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 CE
SN74LVC1G08DRYR.B Active Production SON (DRY) | 6 5000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 CE
SN74LVC1G08DRYRG4 Active Production SON (DRY) | 6 5000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 CE
SN74LVC1G08DRYRG4.B Active Production SON (DRY) | 6 5000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 CE
SN74LVC1G08DSF2 Active Production SON (DSF) | 6 5000 | LARGE T&R Yes NIPDAU | NIPDAUAG Level-1-260C-UNLIM -40 to 125 CE
SN74LVC1G08DSF2.B Active Production SON (DSF) | 6 5000 | LARGE T&R Yes NIPDAUAG Level-1-260C-UNLIM -40 to 125 CE
SN74LVC1G08DSFR Active Production SON (DSF) | 6 5000 | LARGE T&R Yes NIPDAU | NIPDAUAG Level-1-260C-UNLIM -40 to 125 CE
SN74LVC1G08DSFR.B Active Production SON (DSF) | 6 5000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 CE
SN74LVC1G08DSFRG4 Active Production SON (DSF) | 6 5000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 CE
SN74LVC1G08DSFRG4.B Active Production SON (DSF) | 6 5000 | LARGE T&R Yes NIPDAU Level-1-260C-UNLIM -40 to 125 CE
SN74LVC1G08YZPR Active Production DSBGA (YZP) | 5 3000 | LARGE T&R Yes SNAGCU Level-1-260C-UNLIM -40 to 85 (CE, CE7)
SN74LVC1G08YZPR.B Active Production DSBGA (YZP) | 5 3000 | LARGE T&R Yes SNAGCU Level-1-260C-UNLIM -40 to 85 (CE, CE7)

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
Addendum-Page 3
```

### Page 17

#### Raw extracted text

```text
PACKAGE OPTION ADDENDUM
www.ti.com 20-Apr-2026

Important Information and Disclaimer:The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and
makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative
and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers
and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.

 OTHER QUALIFIED VERSIONS OF SN74LVC1G08 :
* Automotive : SN74LVC1G08-Q1
* Enhanced Product : SN74LVC1G08-EP
 NOTE: Qualified Version Definitions:
* Automotive - Q100 devices qualified for high-reliability automotive applications targeting zero defects
* Enhanced Product - Supports Defense, Aerospace and Medical Applications
Addendum-Page 4
```

### Page 18

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
SN74LVC1G08DBVR | SOT-23 | DBV | 5 | 3000 | 178.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3
SN74LVC1G08DBVRG4 | SOT-23 | DBV | 5 | 3000 | 178.0 | 9.0 | 3.23 | 3.17 | 1.37 | 4.0 | 8.0 | Q3
SN74LVC1G08DBVT | SOT-23 | DBV | 5 | 250 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3
SN74LVC1G08DBVT | SOT-23 | DBV | 5 | 250 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3
SN74LVC1G08DCKR | SC70 | DCK | 5 | 3000 | 178.0 | 8.4 | 2.25 | 2.45 | 1.2 | 4.0 | 8.0 | Q3
SN74LVC1G08DCKRG4 | SC70 | DCK | 5 | 3000 | 178.0 | 9.2 | 2.4 | 2.4 | 1.22 | 4.0 | 8.0 | Q3
SN74LVC1G08DCKT | SC70 | DCK | 5 | 250 | 178.0 | 9.0 | 2.4 | 2.5 | 1.2 | 4.0 | 8.0 | Q3
SN74LVC1G08DCKTG4 | SC70 | DCK | 5 | 250 | 178.0 | 9.2 | 2.4 | 2.4 | 1.22 | 4.0 | 8.0 | Q3
SN74LVC1G08DPWR | X2SON | DPW | 5 | 3000 | 178.0 | 8.4 | 0.91 | 0.91 | 0.5 | 2.0 | 8.0 | Q3
SN74LVC1G08DRLR | SOT-5X3 | DRL | 5 | 4000 | 180.0 | 8.4 | 1.98 | 1.78 | 0.69 | 4.0 | 8.0 | Q3
SN74LVC1G08DRY2 | SON | DRY | 6 | 5000 | 180.0 | 9.5 | 1.6 | 1.15 | 0.75 | 4.0 | 8.0 | Q3
SN74LVC1G08DRYR | SON | DRY | 6 | 5000 | 180.0 | 9.5 | 1.15 | 1.6 | 0.75 | 4.0 | 8.0 | Q1
SN74LVC1G08DRYRG4 | SON | DRY | 6 | 5000 | 180.0 | 9.5 | 1.15 | 1.6 | 0.75 | 4.0 | 8.0 | Q1
SN74LVC1G08DSF2 | SON | DSF | 6 | 5000 | 180.0 | 9.5 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q3
SN74LVC1G08DSFR | SON | DSF | 6 | 5000 | 180.0 | 8.4 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2
SN74LVC1G08DSFRG4 | SON | DSF | 6 | 5000 | 180.0 | 8.4 | 1.16 | 1.16 | 0.5 | 4.0 | 8.0 | Q2
```

#### Raw extracted text

```text
PACKAGE MATERIALS INFORMATION
www.ti.com 22-Apr-2026
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
SN74LVC1G08DBVR SOT-23 DBV 5 3000 178.0 8.4 3.2 3.2 1.4 4.0 8.0 Q3
SN74LVC1G08DBVRG4 SOT-23 DBV 5 3000 178.0 9.0 3.23 3.17 1.37 4.0 8.0 Q3
SN74LVC1G08DBVT SOT-23 DBV 5 250 180.0 8.4 3.2 3.2 1.4 4.0 8.0 Q3
SN74LVC1G08DBVT SOT-23 DBV 5 250 180.0 8.4 3.2 3.2 1.4 4.0 8.0 Q3
SN74LVC1G08DCKR SC70 DCK 5 3000 178.0 8.4 2.25 2.45 1.2 4.0 8.0 Q3
SN74LVC1G08DCKRG4 SC70 DCK 5 3000 178.0 9.2 2.4 2.4 1.22 4.0 8.0 Q3
SN74LVC1G08DCKT SC70 DCK 5 250 178.0 9.0 2.4 2.5 1.2 4.0 8.0 Q3
SN74LVC1G08DCKTG4 SC70 DCK 5 250 178.0 9.2 2.4 2.4 1.22 4.0 8.0 Q3
SN74LVC1G08DPWR X2SON DPW 5 3000 178.0 8.4 0.91 0.91 0.5 2.0 8.0 Q3
SN74LVC1G08DRLR SOT-5X3 DRL 5 4000 180.0 8.4 1.98 1.78 0.69 4.0 8.0 Q3
SN74LVC1G08DRY2 SON DRY 6 5000 180.0 9.5 1.6 1.15 0.75 4.0 8.0 Q3
SN74LVC1G08DRYR SON DRY 6 5000 180.0 9.5 1.15 1.6 0.75 4.0 8.0 Q1
SN74LVC1G08DRYRG4 SON DRY 6 5000 180.0 9.5 1.15 1.6 0.75 4.0 8.0 Q1
SN74LVC1G08DSF2 SON DSF 6 5000 180.0 9.5 1.16 1.16 0.5 4.0 8.0 Q3
SN74LVC1G08DSFR SON DSF 6 5000 180.0 8.4 1.16 1.16 0.5 4.0 8.0 Q2
SN74LVC1G08DSFRG4 SON DSF 6 5000 180.0 8.4 1.16 1.16 0.5 4.0 8.0 Q2
Pack Materials-Page 1
```

### Page 19

#### Extracted tables

Table 1:

```text
Device | Package Type | Package Drawing | Pins | SPQ | Reel Diameter (mm) | Reel Width W1 (mm) | A0 (mm) | B0 (mm) | K0 (mm) | P1 (mm) | W (mm) | Pin1 Quadrant
SN74LVC1G08YZPR | DSBGA | YZP | 5 | 3000 | 180.0 | 8.4 | 1.02 | 1.52 | 0.63 | 4.0 | 8.0 | Q1
```

#### Raw extracted text

```text
PACKAGE MATERIALS INFORMATION

www.ti.com 22-Apr-2026
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
SN74LVC1G08YZPR DSBGA YZP 5 3000 180.0 8.4 1.02 1.52 0.63 4.0 8.0 Q1
Pack Materials-Page 2
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
SN74LVC1G08DBVR | SOT-23 | DBV | 5 | 3000 | 208.0 | 191.0 | 35.0
SN74LVC1G08DBVRG4 | SOT-23 | DBV | 5 | 3000 | 180.0 | 180.0 | 18.0
SN74LVC1G08DBVT | SOT-23 | DBV | 5 | 250 | 210.0 | 185.0 | 35.0
SN74LVC1G08DBVT | SOT-23 | DBV | 5 | 250 | 210.0 | 185.0 | 35.0
SN74LVC1G08DCKR | SC70 | DCK | 5 | 3000 | 208.0 | 191.0 | 35.0
SN74LVC1G08DCKRG4 | SC70 | DCK | 5 | 3000 | 180.0 | 180.0 | 18.0
SN74LVC1G08DCKT | SC70 | DCK | 5 | 250 | 180.0 | 180.0 | 18.0
SN74LVC1G08DCKTG4 | SC70 | DCK | 5 | 250 | 180.0 | 180.0 | 18.0
SN74LVC1G08DPWR | X2SON | DPW | 5 | 3000 | 205.0 | 200.0 | 33.0
SN74LVC1G08DRLR | SOT-5X3 | DRL | 5 | 4000 | 202.0 | 201.0 | 28.0
SN74LVC1G08DRY2 | SON | DRY | 6 | 5000 | 184.0 | 184.0 | 19.0
SN74LVC1G08DRYR | SON | DRY | 6 | 5000 | 184.0 | 184.0 | 19.0
SN74LVC1G08DRYRG4 | SON | DRY | 6 | 5000 | 184.0 | 184.0 | 19.0
SN74LVC1G08DSF2 | SON | DSF | 6 | 5000 | 184.0 | 184.0 | 19.0
SN74LVC1G08DSFR | SON | DSF | 6 | 5000 | 210.0 | 185.0 | 35.0
SN74LVC1G08DSFRG4 | SON | DSF | 6 | 5000 | 210.0 | 185.0 | 35.0
SN74LVC1G08YZPR | DSBGA | YZP | 5 | 3000 | 182.0 | 182.0 | 20.0
```

#### Raw extracted text

```text
PACKAGE MATERIALS INFORMATION

www.ti.com 22-Apr-2026
TAPE AND REEL BOX DIMENSIONS
Width (mm)
W LH

*All dimensions are nominal
Device Package Type Package Drawing Pins SPQ Length (mm) Width (mm) Height (mm)
SN74LVC1G08DBVR SOT-23 DBV 5 3000 208.0 191.0 35.0
SN74LVC1G08DBVRG4 SOT-23 DBV 5 3000 180.0 180.0 18.0
SN74LVC1G08DBVT SOT-23 DBV 5 250 210.0 185.0 35.0
SN74LVC1G08DBVT SOT-23 DBV 5 250 210.0 185.0 35.0
SN74LVC1G08DCKR SC70 DCK 5 3000 208.0 191.0 35.0
SN74LVC1G08DCKRG4 SC70 DCK 5 3000 180.0 180.0 18.0
SN74LVC1G08DCKT SC70 DCK 5 250 180.0 180.0 18.0
SN74LVC1G08DCKTG4 SC70 DCK 5 250 180.0 180.0 18.0
SN74LVC1G08DPWR X2SON DPW 5 3000 205.0 200.0 33.0
SN74LVC1G08DRLR SOT-5X3 DRL 5 4000 202.0 201.0 28.0
SN74LVC1G08DRY2 SON DRY 6 5000 184.0 184.0 19.0
SN74LVC1G08DRYR SON DRY 6 5000 184.0 184.0 19.0
SN74LVC1G08DRYRG4 SON DRY 6 5000 184.0 184.0 19.0
SN74LVC1G08DSF2 SON DSF 6 5000 184.0 184.0 19.0
SN74LVC1G08DSFR SON DSF 6 5000 210.0 185.0 35.0
SN74LVC1G08DSFRG4 SON DSF 6 5000 210.0 185.0 35.0
SN74LVC1G08YZPR DSBGA YZP 5 3000 182.0 182.0 20.0
Pack Materials-Page 3
```

### Page 21

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

### Page 22

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

### Page 23

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

### Page 24

#### Raw extracted text

```text
GENERIC PACKAGE VIEW
Images above are just a representation of the package family, actual package may vary.
Refer to the product data sheet for package details.
DRY 6 USON - 0.6 mm max height
PLASTIC SMALL OUTLINE - NO LEAD
4207181/G
```

### Page 25

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

### Page 26

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

### Page 27

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

### Page 28

#### Extracted tables

Table 1:

```text
0.05 | C
```

Table 2:

```text
0.07 0.05 | C | B | A
 | C |  |
```

#### Raw extracted text

```text
www.ti.com
PACKAGE OUTLINE
C
6X 0.22
0.12
6X 0.45
0.35
2X
0.7
4X
0.35
0.4 MAX
0.05
0.00
B 1.05
0.95
A
1.05
0.95
(0.11) TYP
(0.1)
PIN 1 ID
4220597/B   06/2022
X2SON - 0.4 mm max heightDSF0006A
PLASTIC SMALL OUTLINE - NO LEAD
PIN 1 INDEX AREA
SEATING PLANE
0.05 C
1
3 4
6
0.07 C B A
0.05 C
SYMM
SYMM
NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
    per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. Reference JEDEC registration MO-287, variation X2AAF.
SCALE  10.000
```

### Page 29

#### Raw extracted text

```text
www.ti.com
EXAMPLE BOARD LAYOUT
0.07 MIN
ALL AROUND0.07 MAX
ALL AROUND
6X (0.6)
6X (0.17)
4X (0.35)
(0.8)
(R0.05) TYP
X2SON - 0.4 mm max heightDSF0006A
PLASTIC SMALL OUTLINE - NO LEAD
4220597/B   06/2022
SOLDER MASK
OPENING
SOLDER MASK
OPENING
NOTES: (continued)

4. For more information, see Texas Instruments literature number SLUA271 (www.ti.com/lit/slua271).
LAND PATTERN EXAMPLE
EXPOSED METAL SHOWN
SCALE:40X
SYMM
SYMM
1
3 4
6
EXPOSED METAL
METAL
NON SOLDER MASK
DEFINED
SOLDER MASK DETAILS
EXPOSED METAL
METAL UNDER
SOLDER MASK
SOLDER MASK
DEFINED
```

### Page 30

#### Raw extracted text

```text
www.ti.com
EXAMPLE STENCIL DESIGN
6X (0.6)
6X (0.15)
4X (0.35)
(0.8)
(R0.05) TYP
X2SON - 0.4 mm max heightDSF0006A
PLASTIC SMALL OUTLINE - NO LEAD
4220597/B   06/2022
4. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
    design recommendations.
SOLDER PASTE EXAMPLE
BASED ON 0.09 mm THICK STENCIL

PRINTED SOLDER COVERAGE BY AREA UNDER PACKAGE
SCALE:40X
SYMM
SYMM
1
3 4
6
```

### Page 31

#### Extracted tables

Table 1:

```text
0.05 | C
```

Table 2:

```text
| 0.1 | C |  | A | B
 | 0.05 |  | C |  |
```

#### Raw extracted text

```text
www.ti.com
PACKAGE OUTLINE
1.7
1.5
2X 0.5
2X 1
5X 0.3
0.10.6 MAX
5X 0.18
0.08
5X 0.4
0.2
0.05
0.00 TYP
5X 0.27
0.15
2X 0 -10
2X 4 -15
1.3
1.1
1.7
1.5
NOTE 3
SOT - 0.6 mm max heightDRL0005A
PLASTIC SMALL OUTLINE
4220753/E   11/2024
NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
    per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. This dimension does not include mold flash, protrusions, or gate burrs. Mold flash, protrusions, or gate burrs shall not
    exceed 0.15 mm per side.
4. Reference JEDEC registration MO-293 Variation UAAD-1
1 5
PIN 1
ID AREA
3 4
SEATING PLANE
0.05 C
SCALE  8.000
0.1 C A B
0.05 C
SYMM
SYMM
A
B
C
```

### Page 32

#### Raw extracted text

```text
www.ti.com
EXAMPLE BOARD LAYOUT
0.05 MAX
AROUND
0.05 MIN
AROUND
5X (0.67)
5X (0.3)
(1.48)
2X (0.5)
(R0.05) TYP
(1)
4220753/E   11/2024
SOT - 0.6 mm max heightDRL0005A
PLASTIC SMALL OUTLINE
NOTES: (continued)

5. Publication IPC-7351 may have alternate designs.
6. Solder mask tolerances between and around signal pads can vary based on board fabrication site.

SYMM
LAND PATTERN EXAMPLE
SCALE:30X
SYMM
1
3 4
5
SOLDER MASK
OPENING
METAL UNDER
SOLDER MASK
SOLDER MASK
DEFINED
METALSOLDER MASK
OPENING
NON SOLDER MASK
DEFINED
(PREFERRED)
SOLDERMASK DETAILS
```

### Page 33

#### Raw extracted text

```text
www.ti.com
EXAMPLE STENCIL DESIGN
(1.48)
2X (0.5)
5X (0.67)
5X (0.3)
(R0.05) TYP
(1)
SOT - 0.6 mm max heightDRL0005A
PLASTIC SMALL OUTLINE
4220753/E   11/2024
NOTES: (continued)

7. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
    design recommendations.
8. Board assembly site may have different recommendations for stencil design.
SOLDER PASTE EXAMPLE
BASED ON 0.1 mm THICK STENCIL
SCALE:30X
SYMM
SYMM
1
3 4
5
```

### Page 34

#### Raw extracted text

```text
[No text could be extracted from this page with the current local extractor.]
```

### Page 35

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
4X 0.27
0.17
3X 0.288
0.188
0.4 MAX
0.05
0.00
2X
0.48
0.239
0.139
 0.25 0.1
B 0.85
0.75
A
0.85
0.75
(0.1)
4X (0.05) (0.324)
2X (0.26)
X2SON - 0.4 mm max heightDPW0005A
PLASTIC SMALL OUTLINE - NO LEAD
4223102/D   03/2022
PIN 1 INDEX AREA
SEATING PLANE
NOTE 3
1
2
3
4
0.1 C A B
0.05 C
5
NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
    per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. The size and shape of this feature may vary.
NOTE 3
SCALE  12.000
```

### Page 36

#### Raw extracted text

```text
www.ti.com
EXAMPLE BOARD LAYOUT
0.05 MIN
ALL AROUND
TYP
(0.21) TYP
EXPOSED METAL
CLEARANCE
(0.48)
(0.78)
4X (0.42)
4X (0.22)
( 0.25)
4X (0.26)
4X (0.06)
( 0.1)
VIA
(R0.05) TYP
X2SON - 0.4 mm max heightDPW0005A
PLASTIC SMALL OUTLINE - NO LEAD
4223102/D   03/2022
SYMM
1
2
3
4
SYMM
LAND PATTERN EXAMPLE
SOLDER MASK DEFINED
SCALE:60X
SOLDER MASK
OPENING, TYP
METAL UNDER
SOLDER MASK
TYP
5
NOTES: (continued)

4. This package is designed to be soldered to a thermal pad on the board. For more information, refer to QFN/SON PCB application note
    in literature No. SLUA271 (www.ti.com/lit/slua271).
```

### Page 37

#### Raw extracted text

```text
www.ti.com
EXAMPLE STENCIL DESIGN
(0.48)
(0.78)
4X (0.42)
4X (0.22)
4X (0.26)
4X (0.06)
( 0.24)
(0.21)
TYP
(R0.05) TYP
X2SON - 0.4 mm max heightDPW0005A
PLASTIC SMALL OUTLINE - NO LEAD
4223102/D   03/2022
NOTES: (continued)

5. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
   design recommendations.

 SOLDER PASTE EXAMPLE
BASED ON 0.1 mm THICK STENCIL

EXPOSED PAD 3
92%  PRINTED SOLDER COVERAGE BY AREA UNDER PACKAGE
SCALE:100X
SYMM
1
2
3
4
SYMM
EDGE
SOLDER MASK
5
```

### Page 38

#### Raw extracted text

```text
[No text could be extracted from this page with the current local extractor.]
```

### Page 39

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
1
TYP
0.5  TYP
5X 0.25
0.21
0.5
TYP
B E A
D
4219492/A   05/2017
DSBGA - 0.5 mm max heightYZP0005
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
SCALE  8.000
D: Max =
E: Max =
1.418 mm, Min =
0.918 mm, Min =
1.358 mm
0.858 mm
```

### Page 40

#### Raw extracted text

```text
www.ti.com
EXAMPLE BOARD LAYOUT
5X ( 0.23)
(0.5) TYP
(0.5) TYP
( 0.23)
METAL
0.05 MAX ( 0.23)
SOLDER MASK
OPENING
0.05 MIN
4219492/A   05/2017
DSBGA - 0.5 mm max heightYZP0005
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

### Page 41

#### Raw extracted text

```text
www.ti.com
EXAMPLE STENCIL DESIGN
(0.5)
TYP
(0.5) TYP
5X ( 0.25) (R0.05) TYP
METAL
TYP
4219492/A   05/2017
DSBGA - 0.5 mm max heightYZP0005
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
```

### Page 42

#### Extracted tables

Table 1:

```text
| 0.1 | C
```

Table 2:

```text
|  | 00..11 | CC | AA | BB
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
2X 0.65
1.3
1.1 MAX
0.1
0.0 TYP
5X 0.33
0.15
NOTE 5
0.1 C A B
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
(0.9)
(0.15)
(0.1)
SOT - 1.1 max heightDCK0005A
SMALL OUTLINE TRANSISTOR
4214834/G   11/2024
NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing
    per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. Refernce JEDEC MO-203.
4. Support pin may differ or may not be present.
5. Lead width does not comply with JEDEC.
6. Body dimensions do not include mold flash, protrusions, or gate burrs. Mold flash, protrusions, or gate burrs shall not exceed
    0.25mm per side
0.1 C A B
1
3
4
5
2
INDEX AREA
PIN 1
NOTE 4
NOTE 5
GAGE PLANE
SEATING PLANE
0.1 C
SCALE  5.600
```

### Page 43

#### Raw extracted text

```text
www.ti.com
EXAMPLE BOARD LAYOUT
0.07 MAX
ARROUND
0.07 MIN
ARROUND
5X (0.95)
5X (0.4)
(2.2)
(1.3)
2X (0.65)
(R0.05) TYP
4214834/G   11/2024
SOT - 1.1 max heightDCK0005A
SMALL OUTLINE TRANSISTOR
NOTES: (continued)

7. Publication IPC-7351 may have alternate designs.
8. Solder mask tolerances between and around signal pads can vary based on board fabrication site.

SYMM
LAND PATTERN EXAMPLE
EXPOSED METAL SHOWN
SCALE:18X
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

### Page 44

#### Raw extracted text

```text
www.ti.com
EXAMPLE STENCIL DESIGN
(2.2)
(1.3)
2X(0.65)
5X (0.95)
5X (0.4)
(R0.05) TYP
SOT - 1.1 max heightDCK0005A
SMALL OUTLINE TRANSISTOR
4214834/G   11/2024
NOTES: (continued)

9. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate
     design recommendations.
10. Board assembly site may have different recommendations for stencil design.

SOLDER PASTE EXAMPLE
BASED ON 0.125 THICK STENCIL
SCALE:18X
SYMM
PKG
1
3 4
5
2
```

### Page 45

#### Raw extracted text

```text
[No text could be extracted from this page with the current local extractor.]
```

### Page 46

#### Raw extracted text

```text
[No text could be extracted from this page with the current local extractor.]
```

### Page 47

#### Raw extracted text

```text
[No text could be extracted from this page with the current local extractor.]
```

### Page 48

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
