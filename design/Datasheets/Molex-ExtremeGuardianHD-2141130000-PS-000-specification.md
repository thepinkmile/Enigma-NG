# Molex EXTreme Guardian HD board-to-board system specification

## Source Reference

- Source PDF:
  [Molex-ExtremeGuardianHD-2141130000-PS-000-specification.pdf](Molex-ExtremeGuardianHD-2141130000-PS-000-specification.pdf)
- Source path: `design\Datasheets\Molex-ExtremeGuardianHD-2141130000-PS-000-specification.pdf`
- Generated markdown: `Molex-ExtremeGuardianHD-2141130000-PS-000-specification.md`
- Page count: 19
- Extracted text characters: 23961
- Empty extraction pages: none
- Conversion method: automated local PDF text extraction with pypdf and pdfplumber

## Reviewed Summary

- Scope: system spec covering RA plug (214113 / 219562), vertical receptacle (214114 / 219563), and RA receptacle (214115 / 219564) families.
- Geometry: mixed power and HDS signal modules; power modules are called out at 5.15 mm or 5.78 mm pitch, with PCB hole / pad guidance in section 7.
- Electrical: HDS signal modules 120 V, power modules <32 V at 5.15 mm pitch or 125 V at 5.78 mm pitch; signal contacts 4.5 A; insulation resistance 5000 Mohm min; dielectric test 1500 VDC / 1 min.
- Temperature: power -40 to +125 degC including rise; signal -40 to +105 degC including rise.
- Materials / finish: RoHS-compliant housings, copper-alloy terminals, gold on mating surfaces, tin on tails, nickel underplate overall.

## Extraction Notes

- The PDF is a long product specification; this summary highlights the items most useful for connector selection while the full qualification tables remain searchable below.

## Page-by-Page Extracted Text

### Page 1

```text
PRODUCT SPECIFICATION

THIS DOCUMENT CONTAINS INFORMATION THAT IS PROPRIETARY TO MOLEX ELECTRONIC TECHNOLOGIES, LLC AND
SHOULD NOT BE USED WITHOUT WRITTEN PERMISSION
REVISION
DESCRIPTION  EXTREME GUARDIAN HD BOARD-TO-BOARD
INTERCONNECT SYSTEM
CHANGE NO. 792793
REVISED BY LZABJANOVSKI DATE 2024/07/01 DOC TYPE DOC TYPE DESCRIPTION DOC PART SERIES
REV APPR BY JAYK1 DATE 2024/07/26 PS  PRODUCT SPECIFICATION WORD 000 214113
INITIAL RELEASE CUSTOMER DOCUMENT NUMBER REVISION SHEET
INITIAL DRWN LZABJANOVSKI DATE 2020/04/22
2141130000-PS A8 1 OF 19
INITIAL APPR BPISZCZOR DATE 2020/05/01

TEMPLATE: 2090580003-PPS-A      Rev A2        2020 / 04 / 05

EXTreme Guardian HD Board-To-Board Interconnect System

R/A Plug Power and Signal R/A Plug Power

Series: 214113, 219562 Series: 214113, 219562
Vertical Receptacle Power and Signal Vertical Receptacle Power

Series: 214114, 219563 Series: 214114, 219563
R/A Receptacle Power and Signal R/A Receptacle Power

Series: 214115, 219564 Series: 214115, 219564
```

### Page 2

```text
PRODUCT SPECIFICATION

THIS DOCUMENT CONTAINS INFORMATION THAT IS PROPRIETARY TO MOLEX ELECTRONIC TECHNOLOGIES, LLC AND
SHOULD NOT BE USED WITHOUT WRITTEN PERMISSION
REVISION
DESCRIPTION  EXTREME GUARDIAN HD BOARD-TO-BOARD
INTERCONNECT SYSTEM
CHANGE NO. 792793
REVISED BY LZABJANOVSKI DATE 2024/07/01 DOC TYPE DOC TYPE DESCRIPTION DOC PART SERIES
REV APPR BY JAYK1 DATE 2024/07/26 PS  PRODUCT SPECIFICATION WORD 000 214113
INITIAL RELEASE CUSTOMER DOCUMENT NUMBER REVISION SHEET
INITIAL DRWN LZABJANOVSKI DATE 2020/04/22
2141130000-PS A8 2 OF 19
INITIAL APPR BPISZCZOR DATE 2020/05/01

TEMPLATE: 2090580003-PPS-A      Rev A2        2020 / 04 / 05

TABLE OF CONTENTS

1.0 SCOPE

2.0 PRODUCT DESCRIPTION
2.1 Product Name and Series Numbers
2.2 Dimensions, Materials, Plating's, and Markings
2.3 Safety Agency Approvals

3.0 APPLICABLE DOCUMENTS AND SPECIFICATIONS
3.1. Molex Documents

4.0 ELECTRICAL PERFORMANCE RATINGS
4.1 Voltage
4.2 Current
4.3 Temperature
4.4 Durability

5.0 QUALIFICATION

6.0 PERFORMANCE
6.1 Electrical Performance
6.2 Mechanical Performance
6.3 Environmental Performance

7.0 PRINTED CIRCUIT BOARD SPECIFICATION
7.1 Plated Through Hole Specification
7.2 Pad Lay-out
7.3 Nominal Wipe Lengths
7.4 Soldering Profile
7.5 Typical Mating Sequence

8.0 TEST SEQUENCE PER EIA-364-1000.01
```

### Page 3

```text
PRODUCT SPECIFICATION

THIS DOCUMENT CONTAINS INFORMATION THAT IS PROPRIETARY TO MOLEX ELECTRONIC TECHNOLOGIES, LLC AND
SHOULD NOT BE USED WITHOUT WRITTEN PERMISSION
REVISION
DESCRIPTION  EXTREME GUARDIAN HD BOARD-TO-BOARD
INTERCONNECT SYSTEM
CHANGE NO. 792793
REVISED BY LZABJANOVSKI DATE 2024/07/01 DOC TYPE DOC TYPE DESCRIPTION DOC PART SERIES
REV APPR BY JAYK1 DATE 2024/07/26 PS  PRODUCT SPECIFICATION WORD 000 214113
INITIAL RELEASE CUSTOMER DOCUMENT NUMBER REVISION SHEET
INITIAL DRWN LZABJANOVSKI DATE 2020/04/22
2141130000-PS A8 3 OF 19
INITIAL APPR BPISZCZOR DATE 2020/05/01

TEMPLATE: 2090580003-PPS-A      Rev A2        2020 / 04 / 05

1.0  SCOPE

The specification covers the performance requirements and test methods of Guardian.
board to board interconnect systems.

2.0  PRODUCT DESCRIPTION

2.1 This specification covers the following board to board configurations:

214113-XXXX RA Plug Side Assembly
214114-XXXX Vertical Receptacle Side Assembly
214115-XXXX RA Receptacle Side Assembly
219562-XXXX RA Plug Side Assembly
219563-XXXX Vertical Receptacle Side Assembly
219564-XXXX RA Receptacle Side Assembly

Right Angle (RA) Plug assembly mates to RA Receptacle assembly (Coplanar configuration)

Right Angle (RA) Plug assembly mates to Vertical Receptacle assembly (Backplane configuration)

2.2 DIMENSIONS, MATERIALS, PLATINGS AND MARKINGS

Dimensions: See individual sales drawings for additional dimensions. For dimensions not identified
on
the sales drawing, please refer to the latest 3D customer model for reference dimensions.
Material: RoHS compliant materials.
(LCP or equivalent plastic for housings and guide modules, copper alloy for terminals).
Plating: Gold on mating surfaces and tin on PC tail with nickel under-plating overall.

2.3  SAFETY AGENCY APPROVALS

2.3.1   File Number:  152514 (LR 19980)

2.3.2 UL File Number:  E29179
```

### Page 4

```text
PRODUCT SPECIFICATION

THIS DOCUMENT CONTAINS INFORMATION THAT IS PROPRIETARY TO MOLEX ELECTRONIC TECHNOLOGIES, LLC AND
SHOULD NOT BE USED WITHOUT WRITTEN PERMISSION
REVISION
DESCRIPTION  EXTREME GUARDIAN HD BOARD-TO-BOARD
INTERCONNECT SYSTEM
CHANGE NO. 792793
REVISED BY LZABJANOVSKI DATE 2024/07/01 DOC TYPE DOC TYPE DESCRIPTION DOC PART SERIES
REV APPR BY JAYK1 DATE 2024/07/26 PS  PRODUCT SPECIFICATION WORD 000 214113
INITIAL RELEASE CUSTOMER DOCUMENT NUMBER REVISION SHEET
INITIAL DRWN LZABJANOVSKI DATE 2020/04/22
2141130000-PS A8 4 OF 19
INITIAL APPR BPISZCZOR DATE 2020/05/01

TEMPLATE: 2090580003-PPS-A      Rev A2        2020 / 04 / 05

3.0 APPLICABLE DOCUMENTS AND SPECIFICATIONS

3.1 See sales drawings and the other sections of this specifications for the necessary referenced
documents and specifications.

4.0 ELECTRICAL PERFORMANCE RATINGS

4.1 VOLTAGE

HDS Signal Module:  120 Volts
  Power Module:   5.15mm Pitch <32 volts
        5.78mm Pitch 125 volts

Connector Rating per UL-1977
Connector voltage rating meets the connector approval level defined by UL 1977 , Sect. 11 for
spacing
per table 11.1.  Example: 1.2 mm for <= 250 volt; 3.2 mm for >= 250 volt.

Exception taken for spacing less than those specified are permitted if the device complies with the
requirements in the dielectric voltage withstanding test per Sect. 17.

Application Voltage Guideline
For application voltage requirements please refer to UL-60950 or other applicable standards, the
creepage & clearance also needs to be determined based upon pads/traces on the PCB.

4.2 CURRENT **

HDS Signal Contact:    4.5 Amps

Power Contacts:
Test Method Amps Circuit Size
Copper Coupons 80 1 Circuit
Copper Coupons 60 8 Circuit
Copper Planes (PCB) 130 1 Circuit
Copper Planes (PCB) 90 8 Circuit

** Tested in accordance with EIA-364-70.
5.15mm pitch connectors were used in testing.

Ratings are based on a 30 degC maximum temperature rise limit over ambient (room temperature).
Current rating is application dependent and below charts are intended as a guideline. Appropriate de
-
rating is required depending on factors such as higher ambient temperature, gross heating from
adjacent modules or components and other factors that influence connector performance .

Copper coupon and copper plane results are given to show multiple setups and allow customers to
determine which is closer to their individual applications.  When trying to maximize current in your
application it is important to look at factors such as PCB copper cross section, current per
compliant
pin (for press-fit connectors), and other components that impact performance.
```

### Page 5

```text
PRODUCT SPECIFICATION

THIS DOCUMENT CONTAINS INFORMATION THAT IS PROPRIETARY TO MOLEX ELECTRONIC TECHNOLOGIES, LLC AND
SHOULD NOT BE USED WITHOUT WRITTEN PERMISSION
REVISION
DESCRIPTION  EXTREME GUARDIAN HD BOARD-TO-BOARD
INTERCONNECT SYSTEM
CHANGE NO. 792793
REVISED BY LZABJANOVSKI DATE 2024/07/01 DOC TYPE DOC TYPE DESCRIPTION DOC PART SERIES
REV APPR BY JAYK1 DATE 2024/07/26 PS  PRODUCT SPECIFICATION WORD 000 214113
INITIAL RELEASE CUSTOMER DOCUMENT NUMBER REVISION SHEET
INITIAL DRWN LZABJANOVSKI DATE 2020/04/22
2141130000-PS A8 5 OF 19
INITIAL APPR BPISZCZOR DATE 2020/05/01

TEMPLATE: 2090580003-PPS-A      Rev A2        2020 / 04 / 05

Copper Planes (PCB) were constructed with 10 layers and 2 oz copper on each layer.
```

### Page 6

```text
PRODUCT SPECIFICATION

THIS DOCUMENT CONTAINS INFORMATION THAT IS PROPRIETARY TO MOLEX ELECTRONIC TECHNOLOGIES, LLC AND
SHOULD NOT BE USED WITHOUT WRITTEN PERMISSION
REVISION
DESCRIPTION  EXTREME GUARDIAN HD BOARD-TO-BOARD
INTERCONNECT SYSTEM
CHANGE NO. 792793
REVISED BY LZABJANOVSKI DATE 2024/07/01 DOC TYPE DOC TYPE DESCRIPTION DOC PART SERIES
REV APPR BY JAYK1 DATE 2024/07/26 PS  PRODUCT SPECIFICATION WORD 000 214113
INITIAL RELEASE CUSTOMER DOCUMENT NUMBER REVISION SHEET
INITIAL DRWN LZABJANOVSKI DATE 2020/04/22
2141130000-PS A8 6 OF 19
INITIAL APPR BPISZCZOR DATE 2020/05/01

TEMPLATE: 2090580003-PPS-A      Rev A2        2020 / 04 / 05
```

### Page 7

```text
PRODUCT SPECIFICATION

THIS DOCUMENT CONTAINS INFORMATION THAT IS PROPRIETARY TO MOLEX ELECTRONIC TECHNOLOGIES, LLC AND
SHOULD NOT BE USED WITHOUT WRITTEN PERMISSION
REVISION
DESCRIPTION  EXTREME GUARDIAN HD BOARD-TO-BOARD
INTERCONNECT SYSTEM
CHANGE NO. 792793
REVISED BY LZABJANOVSKI DATE 2024/07/01 DOC TYPE DOC TYPE DESCRIPTION DOC PART SERIES
REV APPR BY JAYK1 DATE 2024/07/26 PS  PRODUCT SPECIFICATION WORD 000 214113
INITIAL RELEASE CUSTOMER DOCUMENT NUMBER REVISION SHEET
INITIAL DRWN LZABJANOVSKI DATE 2020/04/22
2141130000-PS A8 7 OF 19
INITIAL APPR BPISZCZOR DATE 2020/05/01

TEMPLATE: 2090580003-PPS-A      Rev A2        2020 / 04 / 05

4.3 TEMPERATURE

Power Operating temperature (including T-rise from applied current) is -40o C to +125o C.
Signal Operating temperature (including T-rise from applied current) is -40o C to +105o C.

Power Temperature life tested per EIA 364-17 Method A for 1827 hours @125o C per table 8 to meet
field temperature of 105o C for 10 years life. Signal Temperature life tested per EIA 364-17 Method
A
for 288 hours @105o C per table 8 to meet field temperature of 65o C for 10 years life. See page 18
detail test sequence of EIA-364-1000.01, Group I.

4.4 DURABILITY
200 cycles**

** - Based on EIA-364-1000.01 Test Method C Section 7
```

### Page 8

```text
PRODUCT SPECIFICATION

THIS DOCUMENT CONTAINS INFORMATION THAT IS PROPRIETARY TO MOLEX ELECTRONIC TECHNOLOGIES, LLC AND
SHOULD NOT BE USED WITHOUT WRITTEN PERMISSION
REVISION
DESCRIPTION  EXTREME GUARDIAN HD BOARD-TO-BOARD
INTERCONNECT SYSTEM
CHANGE NO. 792793
REVISED BY LZABJANOVSKI DATE 2024/07/01 DOC TYPE DOC TYPE DESCRIPTION DOC PART SERIES
REV APPR BY JAYK1 DATE 2024/07/26 PS  PRODUCT SPECIFICATION WORD 000 214113
INITIAL RELEASE CUSTOMER DOCUMENT NUMBER REVISION SHEET
INITIAL DRWN LZABJANOVSKI DATE 2020/04/22
2141130000-PS A8 8 OF 19
INITIAL APPR BPISZCZOR DATE 2020/05/01

TEMPLATE: 2090580003-PPS-A      Rev A2        2020 / 04 / 05

5.0 QUALIFICATION

Laboratory condition and sample selection are in accordance with EIA-364-1000.01.
See page 17 for detail test sequence of EIA-364-1000.01

6.0 PERFORMANCE

6.1 ELECTRICAL PERFORMANCE

ITEM DESCRIPTION TEST CONDITION REQUIREMENT
6.1.1 Initial Contact Resistance
(Low Level) Per EIA-364-23 Signal:  30 mohm
Power:  0.17 mohm*
6.1.2 Voltage Drop
(@ Rated Current)
Mate connectors; apply the
rated current Per EIA-364-70 Power:  30 mV MAX
6.1.3 Insulation Resistance
Apply 500 VDC between
adjacent terminals or ground.
Per EIA-364-21
5000 Mohm MIN
6.1.4 Dielectric Withstanding
Voltage
Apply 1500 VDC for 1 minute
between adjacent terminals
or ground.
Per EIA-364-20
No Breakdown
6.1.5 Temperature Rise
Mate connectors
Measure T-Rise
@ rated current
after 96 hours.
Per EIA-364-70
30 deg C T-Rise
*Contact resistance as measured, measurement setup and technique can affect results.
```

### Page 9

```text
PRODUCT SPECIFICATION

THIS DOCUMENT CONTAINS INFORMATION THAT IS PROPRIETARY TO MOLEX ELECTRONIC TECHNOLOGIES, LLC AND
SHOULD NOT BE USED WITHOUT WRITTEN PERMISSION
REVISION
DESCRIPTION  EXTREME GUARDIAN HD BOARD-TO-BOARD
INTERCONNECT SYSTEM
CHANGE NO. 792793
REVISED BY LZABJANOVSKI DATE 2024/07/01 DOC TYPE DOC TYPE DESCRIPTION DOC PART SERIES
REV APPR BY JAYK1 DATE 2024/07/26 PS  PRODUCT SPECIFICATION WORD 000 214113
INITIAL RELEASE CUSTOMER DOCUMENT NUMBER REVISION SHEET
INITIAL DRWN LZABJANOVSKI DATE 2020/04/22
2141130000-PS A8 9 OF 19
INITIAL APPR BPISZCZOR DATE 2020/05/01

TEMPLATE: 2090580003-PPS-A      Rev A2        2020 / 04 / 05

6.2 MECHANICAL PERFORMANCE

ITEM DESCRIPTION TEST CONDITION REQUIREMENT
6.2.1 Mating Force
Single Circuit**

Mate connectors at a rate of
25.4+/-6 mm per minute.
Per EIA-364-37
P
e
Power Vert Receptacle to R/A Plug
Power R/A Receptacle to R/A Plug
1430 g/circuit Max
HDS
55 g/circuit Max
6.2.2 Un-mating Force
Single Circuit**
Mate connectors at a rate of
25.4+/-6 mm per minute.
Per EIA-364-37
Power Vert Receptacle to R/A Plug
Power R/A Receptacle to R/A Plug
389 g/circuit Min
HDS
25 g/circuit Min
6.2.3 Durability w/o
Environment
Mate connectors
 20 cycles at a
max rate of 10 cycles
per minute.
Per EIA-364-09
Maximum Change:
Signal Contact: 10.0 mohm Max
Power Contact: 0.38 mohm Max
6.2.4 Contact
Retention
Axial pullout force on the
terminal in the housing at a
rate of 25.4+/-6 mm per
minute. Per EIA-364-29
R/A Power
1360 g Min

Vert Power
755 g Min
Vert HDS Signals
368 g Min per coupon
R/A HDS Signals
545 g Min per coupon

** Mate/Unmated Data is for 1st Cycle
```

### Page 10

```text
PRODUCT SPECIFICATION

THIS DOCUMENT CONTAINS INFORMATION THAT IS PROPRIETARY TO MOLEX ELECTRONIC TECHNOLOGIES, LLC AND
SHOULD NOT BE USED WITHOUT WRITTEN PERMISSION
REVISION
DESCRIPTION  EXTREME GUARDIAN HD BOARD-TO-BOARD
INTERCONNECT SYSTEM
CHANGE NO. 792793
REVISED BY LZABJANOVSKI DATE 2024/07/01 DOC TYPE DOC TYPE DESCRIPTION DOC PART SERIES
REV APPR BY JAYK1 DATE 2024/07/26 PS  PRODUCT SPECIFICATION WORD 000 214113
INITIAL RELEASE CUSTOMER DOCUMENT NUMBER REVISION SHEET
INITIAL DRWN LZABJANOVSKI DATE 2020/04/22
2141130000-PS A8 10 OF 19
INITIAL APPR BPISZCZOR DATE 2020/05/01

TEMPLATE: 2090580003-PPS-A      Rev A2        2020 / 04 / 05

6.2 MECHANICAL PERFORMANCE (continued)

ITEM DESCRIPTION TEST CONDITION REQUIREMENT
6.2.5
Max Insertion force into
PCB for terminals with
Compliant Pins
Insert contact at a rate of
25.4+/-6 mm per minute
MAX: 10.01 lbs./pin
(4.54 kg/circuit)
(HDS module)
MAX: 20.66 lbs./pin
(9.37 kg/pin)
(Vertical Power Receptacle)

MAX: 25.93 lbs./pin
 (11.76 kg/pin)
(R/A Power)
6.2.6
Min Retention force
from PCB for terminals
with Compliant Pins
Pull-out contacts at a rate of
25.4+/-6 mm per minute
MIN: 1.00 lbs.
(0.45 Kg/pin)
(HDS Module)
MIN: 1.28lbs./pin
 (0.58 Kg/pin)
Vertical Power Receptacle

MIN: 1.17lbs./pin
 (0.53 Kg/pin)
R/A Power
6.2.7 Solderability
 Dip Test
Molex test method
SMES-152
Solder area shall have Min of 95%
solder coverage
6.2.8 Resistance to soldering
heat from rework
Per EIA-364-61, Test
procedure for compliant pin
retention force
22.5 lbs. (10.2 Kg)
Per Power contact extraction force
from PCB
6.2.9 Resistance to soldering
heat from rework
Per EIA-364-61, Test
procedure 2
(Test Condition II)
No dimensional change
No physical damage
```

### Page 11

```text
PRODUCT SPECIFICATION

THIS DOCUMENT CONTAINS INFORMATION THAT IS PROPRIETARY TO MOLEX ELECTRONIC TECHNOLOGIES, LLC AND
SHOULD NOT BE USED WITHOUT WRITTEN PERMISSION
REVISION
DESCRIPTION  EXTREME GUARDIAN HD BOARD-TO-BOARD
INTERCONNECT SYSTEM
CHANGE NO. 792793
REVISED BY LZABJANOVSKI DATE 2024/07/01 DOC TYPE DOC TYPE DESCRIPTION DOC PART SERIES
REV APPR BY JAYK1 DATE 2024/07/26 PS  PRODUCT SPECIFICATION WORD 000 214113
INITIAL RELEASE CUSTOMER DOCUMENT NUMBER REVISION SHEET
INITIAL DRWN LZABJANOVSKI DATE 2020/04/22
2141130000-PS A8 11 OF 19
INITIAL APPR BPISZCZOR DATE 2020/05/01

TEMPLATE: 2090580003-PPS-A      Rev A2        2020 / 04 / 05

6.3 ENVIRONMENTAL PERFORMANCE
(Tested in accordance with EIA-364-1000)

ITEM DESCRIPTION TEST CONDITION REQUIREMENT
6.3.1 Vibration
(EIA-364-1000.01)
Mate connectors and vibrate
per EIA-364-28
Test condition VII D
15 minutes each axis.
Maximum Change:
Signal Contact: 10.0 mohm Max
Power Contact: 0.38 mohm Max
6.3.2 Mechanical Shock
(EIA-364-1000.01)
Mate connectors and shock at
50 g with 12 sine wave (11
milliseconds) shocks in the 3
axes (18 shocks total) Per
EIA-364-27
Maximum Change:
Signal Contact: 10.0 mohm Max
Power Contact: 0.38 mohm Max
6.3.3 Thermal Shock
(EIA-364-1000.01)
Mate connectors, expose to
10 cycles from -55 degC to 85 degC
Per EIA-364-32
Maximum Change:
Signal Contact: 10.0 mohm Max
Power Contact: 0.38 mohm Max
6.3.4 Temperature Live
(EIA-364-1000.01)
Mate Connectors, expose to
240 hours at 105 degC
Per EIA-364-17
Maximum Change:
Signal Contact: 10.0 mohm Max
Power Contact: 0.38 mohm Max
6.3.5
Cyclic Temperature
and Humidity
(EIA-364-1000.01)
Mate connectors: expose to
24 cycles from 25  degC / 80%
RH to 65  degC / 50% RH
Per EIA-364-31
Maximum Change:
Signal Contact: 10.0 mohm Max
Power Contact: 0.38 mohm Max
6.3.6 Dust
(EIA-364-1000.01)
Un-mated 1-hour duration
25 degC/50% RH dust mass of 9
g/ft3 at rate of 300 m/min.
Per EIA-364-91
Maximum Change:
Signal Contact: 10.0 mohm Max
Power Contact: 0.38 mohm Max
6.3.7 Mixed Flowing Gas
(EIA-364-1000.01)
224 hours un-mated,
112 hours mated,
Per EIA-364-65
Class II-A
Maximum Change:
Signal Contact: 10.0 mohm Max
Power Contact: 0.38 mohm Max
```

### Page 12

```text
PRODUCT SPECIFICATION

THIS DOCUMENT CONTAINS INFORMATION THAT IS PROPRIETARY TO MOLEX ELECTRONIC TECHNOLOGIES, LLC AND
SHOULD NOT BE USED WITHOUT WRITTEN PERMISSION
REVISION
DESCRIPTION  EXTREME GUARDIAN HD BOARD-TO-BOARD
INTERCONNECT SYSTEM
CHANGE NO. 792793
REVISED BY LZABJANOVSKI DATE 2024/07/01 DOC TYPE DOC TYPE DESCRIPTION DOC PART SERIES
REV APPR BY JAYK1 DATE 2024/07/26 PS  PRODUCT SPECIFICATION WORD 000 214113
INITIAL RELEASE CUSTOMER DOCUMENT NUMBER REVISION SHEET
INITIAL DRWN LZABJANOVSKI DATE 2020/04/22
2141130000-PS A8 12 OF 19
INITIAL APPR BPISZCZOR DATE 2020/05/01

TEMPLATE: 2090580003-PPS-A      Rev A2        2020 / 04 / 05

7.0 PRINTED CIRCUIT BOARD SPECIFICATION

7.1 PLATED THROUGH HOLE SPECIFICATION
1.02mm and 1.04mm (finish) dia. holes:

0.70mm and 0.72mm (finish) dia. holes - Signal segment:

Notes:
1. The finished hole size is the critical feature for proper performance of the compliant pin
terminal.
The reference drill sizes listed are recommended by Molex to achieve the finished PCB hole size.

2. Depending on the specific manufacturer's plating process a different drill size c an be used to
achieve
the required finished PCB hole size.
```

### Page 13

```text
PRODUCT SPECIFICATION

THIS DOCUMENT CONTAINS INFORMATION THAT IS PROPRIETARY TO MOLEX ELECTRONIC TECHNOLOGIES, LLC AND
SHOULD NOT BE USED WITHOUT WRITTEN PERMISSION
REVISION
DESCRIPTION  EXTREME GUARDIAN HD BOARD-TO-BOARD
INTERCONNECT SYSTEM
CHANGE NO. 792793
REVISED BY LZABJANOVSKI DATE 2024/07/01 DOC TYPE DOC TYPE DESCRIPTION DOC PART SERIES
REV APPR BY JAYK1 DATE 2024/07/26 PS  PRODUCT SPECIFICATION WORD 000 214113
INITIAL RELEASE CUSTOMER DOCUMENT NUMBER REVISION SHEET
INITIAL DRWN LZABJANOVSKI DATE 2020/04/22
2141130000-PS A8 13 OF 19
INITIAL APPR BPISZCZOR DATE 2020/05/01

TEMPLATE: 2090580003-PPS-A      Rev A2        2020 / 04 / 05

7.2 TYPICAL PCB PAD LAYOUT FOR POWER AND SIGNAL TERMINALS
(Layout for reference only. Refer to appropriate sales drawings.)

Typical Hole Layout For 5 row Signal/ HDS modules (0.70mm diameter holes)

PCB layout for HDS modules
Vertical only

PCB layout for HDS modules
R/A only
```

### Page 14

```text
PRODUCT SPECIFICATION

THIS DOCUMENT CONTAINS INFORMATION THAT IS PROPRIETARY TO MOLEX ELECTRONIC TECHNOLOGIES, LLC AND
SHOULD NOT BE USED WITHOUT WRITTEN PERMISSION
REVISION
DESCRIPTION  EXTREME GUARDIAN HD BOARD-TO-BOARD
INTERCONNECT SYSTEM
CHANGE NO. 792793
REVISED BY LZABJANOVSKI DATE 2024/07/01 DOC TYPE DOC TYPE DESCRIPTION DOC PART SERIES
REV APPR BY JAYK1 DATE 2024/07/26 PS  PRODUCT SPECIFICATION WORD 000 214113
INITIAL RELEASE CUSTOMER DOCUMENT NUMBER REVISION SHEET
INITIAL DRWN LZABJANOVSKI DATE 2020/04/22
2141130000-PS A8 14 OF 19
INITIAL APPR BPISZCZOR DATE 2020/05/01

TEMPLATE: 2090580003-PPS-A      Rev A2        2020 / 04 / 05

7.3 NOMINAL WIPE LENGTHS
Nominal wipe lengths are given below for the recommended final positions shown.

RECOMMENDED FINAL POSITIONS
```

### Page 15

```text
PRODUCT SPECIFICATION

THIS DOCUMENT CONTAINS INFORMATION THAT IS PROPRIETARY TO MOLEX ELECTRONIC TECHNOLOGIES, LLC AND
SHOULD NOT BE USED WITHOUT WRITTEN PERMISSION
REVISION
DESCRIPTION  EXTREME GUARDIAN HD BOARD-TO-BOARD
INTERCONNECT SYSTEM
CHANGE NO. 792793
REVISED BY LZABJANOVSKI DATE 2024/07/01 DOC TYPE DOC TYPE DESCRIPTION DOC PART SERIES
REV APPR BY JAYK1 DATE 2024/07/26 PS  PRODUCT SPECIFICATION WORD 000 214113
INITIAL RELEASE CUSTOMER DOCUMENT NUMBER REVISION SHEET
INITIAL DRWN LZABJANOVSKI DATE 2020/04/22
2141130000-PS A8 15 OF 19
INITIAL APPR BPISZCZOR DATE 2020/05/01

TEMPLATE: 2090580003-PPS-A      Rev A2        2020 / 04 / 05
```

### Page 16

```text
PRODUCT SPECIFICATION

THIS DOCUMENT CONTAINS INFORMATION THAT IS PROPRIETARY TO MOLEX ELECTRONIC TECHNOLOGIES, LLC AND
SHOULD NOT BE USED WITHOUT WRITTEN PERMISSION
REVISION
DESCRIPTION  EXTREME GUARDIAN HD BOARD-TO-BOARD
INTERCONNECT SYSTEM
CHANGE NO. 792793
REVISED BY LZABJANOVSKI DATE 2024/07/01 DOC TYPE DOC TYPE DESCRIPTION DOC PART SERIES
REV APPR BY JAYK1 DATE 2024/07/26 PS  PRODUCT SPECIFICATION WORD 000 214113
INITIAL RELEASE CUSTOMER DOCUMENT NUMBER REVISION SHEET
INITIAL DRWN LZABJANOVSKI DATE 2020/04/22
2141130000-PS A8 16 OF 19
INITIAL APPR BPISZCZOR DATE 2020/05/01

TEMPLATE: 2090580003-PPS-A      Rev A2        2020 / 04 / 05

7.4 SOLDERING PROFILE

(This profile is per JEDEC J-STD-020D.1 and is for guidance only. Please see      notes for
additional
information)

Notes:
1. Temperature indicated refers to the PCB surface temperature at solder tail area.
2. Connector can withstand up to 3 reflow cycles with a cool-down to room temperature in-between.
3. Actual reflow profile also depends on equipment, solder paste, PCB thick ness, and other
components on
the board. Please consult your solder paste & reflow equipment manufacturer for their
recommendations to
adopt a suitable process.

Description   Requirement
 Average Ramp Rate   3 degC/sec Max
 Preheat Temperature   150 degC Min to 200 degC Max
 Preheat Time   60 to 180 sec
 Ramp to Peak  3 degC/sec Max
 Time over Liquids (217 degC)  60 to 150 sec
 Peak Temperature  260 +0/-5 degC
 Time within 5 degC of Peak  20 to 40 sec
 Ramp - Cool Down  6 degC/sec Max
 Time 25 degC to Peak   8 min Max
```

### Page 17

```text
PRODUCT SPECIFICATION

THIS DOCUMENT CONTAINS INFORMATION THAT IS PROPRIETARY TO MOLEX ELECTRONIC TECHNOLOGIES, LLC AND
SHOULD NOT BE USED WITHOUT WRITTEN PERMISSION
REVISION
DESCRIPTION  EXTREME GUARDIAN HD BOARD-TO-BOARD
INTERCONNECT SYSTEM
CHANGE NO. 792793
REVISED BY LZABJANOVSKI DATE 2024/07/01 DOC TYPE DOC TYPE DESCRIPTION DOC PART SERIES
REV APPR BY JAYK1 DATE 2024/07/26 PS  PRODUCT SPECIFICATION WORD 000 214113
INITIAL RELEASE CUSTOMER DOCUMENT NUMBER REVISION SHEET
INITIAL DRWN LZABJANOVSKI DATE 2020/04/22
2141130000-PS A8 17 OF 19
INITIAL APPR BPISZCZOR DATE 2020/05/01

TEMPLATE: 2090580003-PPS-A      Rev A2        2020 / 04 / 05

7.5 TYPICAL MATING SEQUENCE:

Second Mate -
Long Signal Blade
First Mate -
Long Power Blade
```

### Page 18

```text
PRODUCT SPECIFICATION

THIS DOCUMENT CONTAINS INFORMATION THAT IS PROPRIETARY TO MOLEX ELECTRONIC TECHNOLOGIES, LLC AND
SHOULD NOT BE USED WITHOUT WRITTEN PERMISSION
REVISION
DESCRIPTION  EXTREME GUARDIAN HD BOARD-TO-BOARD
INTERCONNECT SYSTEM
CHANGE NO. 792793
REVISED BY LZABJANOVSKI DATE 2024/07/01 DOC TYPE DOC TYPE DESCRIPTION DOC PART SERIES
REV APPR BY JAYK1 DATE 2024/07/26 PS  PRODUCT SPECIFICATION WORD 000 214113
INITIAL RELEASE CUSTOMER DOCUMENT NUMBER REVISION SHEET
INITIAL DRWN LZABJANOVSKI DATE 2020/04/22
2141130000-PS A8 18 OF 19
INITIAL APPR BPISZCZOR DATE 2020/05/01

TEMPLATE: 2090580003-PPS-A      Rev A2        2020 / 04 / 05

7.5 TYPICAL MATING SEQUENCE: (continued)

Last Mate -
Short Signal Blade
Third Mate -
Standard Power Blade and
Standard Signal Blade
```

### Page 19

```text
PRODUCT SPECIFICATION

THIS DOCUMENT CONTAINS INFORMATION THAT IS PROPRIETARY TO MOLEX ELECTRONIC TECHNOLOGIES, LLC AND
SHOULD NOT BE USED WITHOUT WRITTEN PERMISSION
REVISION
DESCRIPTION  EXTREME GUARDIAN HD BOARD-TO-BOARD
INTERCONNECT SYSTEM
CHANGE NO. 792793
REVISED BY LZABJANOVSKI DATE 2024/07/01 DOC TYPE DOC TYPE DESCRIPTION DOC PART SERIES
REV APPR BY JAYK1 DATE 2024/07/26 PS  PRODUCT SPECIFICATION WORD 000 214113
INITIAL RELEASE CUSTOMER DOCUMENT NUMBER REVISION SHEET
INITIAL DRWN LZABJANOVSKI DATE 2020/04/22
2141130000-PS A8 19 OF 19
INITIAL APPR BPISZCZOR DATE 2020/05/01

TEMPLATE: 2090580003-PPS-A      Rev A2        2020 / 04 / 05

8.0 TEST SEQUENCE GROUPS (Powers Only)

* HDS: High Density Signal (5 Row Signal Design) Data from TEN60 Qualification
```
