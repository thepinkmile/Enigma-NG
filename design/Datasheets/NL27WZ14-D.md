# NL27WZ14 - Dual Schmitt-trigger inverter

## Source Reference

- Source PDF: [NL27WZ14-D.pdf](NL27WZ14-D.pdf)
- Source path: `design\Datasheets\NL27WZ14-D.pdf`
- Generated markdown: `NL27WZ14-D.md`
- Review note: manually checked against the source PDF; curated summary added and the raw page-by-page extraction is preserved below.

## Part Identity and Ordering

- onsemi `NL27WZ14`, dual Schmitt-trigger inverter.
- Reviewed orderable parts from the datasheet:
  - `NL27WZ14DFT2G`, `NL27WZ14DFT4G`, `NL27WZ14DFT2G-Q` - SC-88.
  - `NL27WZ14DBVT1G` - SC-74.
  - `NL27WZ14MU1TCG` - UDFN6, 1.45 x 1.0 mm, 0.5 mm pitch.
  - `NL27WZ14MU3TCG` - UDFN6, 1.0 x 1.0 mm, 0.35 mm pitch.
- `-Q` suffix denotes automotive / control-change managed, AEC-Q100 qualified, PPAP-capable ordering.

## Pin / Pad Designations

- Logic symbol: two independent inverters, `A1 -> Y1` and `A2 -> Y2`.
- Pinout shown on page 2:
  - pin 1 `A1`
  - pin 2 `GND`
  - pin 3 `A2`
  - pin 4 `Y2`
  - pin 5 `VCC`
  - pin 6 `Y1`
- The same logical pin set is used across the SC-88, SC-74, and UDFN6 variants reviewed in the PDF.

## Ratings and Operating Conditions

- Operating supply range: 1.65 V to 5.5 V.
- Typical propagation delay: 3.2 ns at `VCC = 5 V`.
- Inputs / outputs are overvoltage tolerant to 5.5 V.
- Sink current callout: 32 mA at 4.5 V.
- Absolute maximum highlights: `VCC` and `VIN` from -0.5 V to +6.5 V, `IOUT` +/-50 mA, storage temperature -65 deg C to +150 deg C.
- Thermal resistance examples from page 2: about 377 deg C/W (SC-88), 320 deg C/W (SC-74), 154 deg C/W (UDFN6).

## Package and Mechanical Notes

- Package families in the reviewed PDF: SC-88, SC-74, and two UDFN6 footprints.
- The ordering section includes the package-specific orientation / tape-and-reel notes.

## Formulas and Equations Present in the PDF

- Power dissipation capacitance note includes the standard CMOS dynamic-current relationships:
  - `ICC(OPR) = CPD * VCC * fin + ICC`
  - `PD = CPD * VCC^2 * fin + ICC * VCC`
- The raw extraction below preserves the surrounding `CPD` table and AC/DC electrical tables for search.

## Applications and Design Content

- Core use case is level-compatible Schmitt-trigger signal cleanup / inversion over a wide 1.65 V to 5.5 V supply range.
- The datasheet is compact and mostly focused on logic, ratings, and package options rather than a long reference-design section.

## Searchability Note

- The raw page-by-page extraction below is intentionally preserved for local text search.
- Mechanical outline pages and marking-diagram pages are more legible in the source PDF than in plain extracted text.

## Page-by-page extracted content

### Page 1

#### Extracted tables

Table 1:

```text
1
1
```

#### Raw extracted text

```text
Share Feedback DATA SHEET
Your Opinion Matters www.onsemi.com
Dual SchmittTrigger
MARKING
DIAGRAMS
Inverter
6
SC-88
NL27WZ14
DF SUFFIX
XXXM(cid:2)
1 CASE 419B-02 (cid:2)
The NL27WZ14 is a high performance dual inverter with 1
Schmitt-Trigger inputs operating from a 1.65 to 5.5 V supply.
Features 6 SC-74 XXXM(cid:2)
*
Designed for 1.65 V to 5.5 V V Operation CASE 318F-05 (cid:2)
CC 1
*
3.2 ns t PD at V CC = 5 V (Typ) 1
*
Inputs/Outputs Overvoltage Tolerant up to 5.5 V
* UDFN6
I
OFF
Supports Partial Power Down Protection
1.45x1.0, 0.5P XM
* Sink 32 mA at 4.5 V 1 CASE 517AQ
*
Available in SC-88, SC-74 and UDFN6 Packages
*
Chip Complexity < 100 FETs UDFN6
* 1x1, 0.35P XM
-Q Suffix for Automotive and Other Applications Requiring Unique
CASE 517BX
1
Site and Control Change Requirements; AEC-Q100 Qualified and
PPAP Capable X, XXX = Specific Device Code
*
These Devices are Pb-Free, Halogen Free/BFR Free and are RoHS M = Date Code*
Compliant (cid:2) = Pb-Free Package
(Note: Microdot may be in either location)
* Date Code orientation and/or position may
A1 1 Y1 vary depending upon manufacturing location.
A2 1 Y2
ORDERING INFORMATION
See detailed ordering and shipping information in the package
Figure 1. Logic Symbol
dimensions section on page 6 of this data sheet.
 Semiconductor Components Industries, LLC, 2013 1 Publication Order Number:
December, 2025 - Rev. 20 NL27WZ14/D
```

### Page 2

#### Extracted tables

Table 1:

```text
Pin | Function
1 | A1
2 | GND
3 | A2
4 | Y2
5 | VCC
6 | Y1
```

Table 2:

```text
A Input | Y Output
L | H
H | L
```

Table 3:

```text
Symbol | Characteristics | Value | Units
VCC | DC Supply Voltage | 0.5 to +6.5 | V
VIN | DC Input Voltage | 0.5 to +6.5 | V
VOUT | DC Output Voltage Active-Mode (High or Low State) Tri-State Mode (Note 1) Power-Down Mode (VCC = 0 V) | 0.5 to VCC +0.5 -0.5 to +6.5 -0.5 to +6.5 | V
IIK | DC Input Diode Current, VIN < GND | 50 | mA
IOK | DC Output Diode Current, VOUT < GND | 50 | mA
IOUT | DC Output Source/Sink Current | +/-50 | mA
ICC or IGND | DC Supply Current per Supply Pin or Ground Pin | +/-100 | mA
TSTG | Storage Temperature Range | 65 to +150 | deg C
TL | Lead Temperature, 1 mm from Case for 10 secs | 260 | deg C
TJ | Junction Temperature under Bias | +150 | deg C
(cid:2) JA | Thermal Resistance (Note 2) SC-88 SC-74 UDFN6 | 377 320 154 | deg C/W
PD | Power Dissipation in Still Air SC-88 SC-74 UDFN6 | 332 390 812 | mW
MSL | Moisture Sensitivity | Level 1 | 
FR | Flamebility Rating Oxygen Index: 28 to 34 | UL 94-V-0 @ 0.125 in |
```

#### Raw extracted text

```text
NL27WZ14
www.onsemi.com
2
 (SC-88/SC-74)
VCC
A1 Y1
GND
IN A2 Y2
1
2
3
6
5
4
PIN ASSIGNMENT
1
2
3A 2
A1
GND
4
5V CC
Y2
Pin Function
FUNCTION TABLE
L
A Input Y Output
H
HL
6Y 1
UDFN6
1
2
3
6
5
4
Y1
A2
A1
Y2
GND VCC
Figure 2. Pinout (Top View)
MAXIMUM RATINGS
Symbol Characteristics Value Units
VCC DC Supply Voltage -0.5 to +6.5 V
VIN DC Input Voltage -0.5 to +6.5 V
VOUT DC Output Voltage Active -Mode (High or Low State)
Tri-State Mode (Note 1)
Power-Down Mode (VCC = 0 V)
-0.5 to VCC +0.5
-0.5 to +6.5
-0.5 to +6.5
V
IIK DC Input Diode Current, VIN < GND -50 mA
IOK DC Output Diode Current, VOUT < GND -50 mA
IOUT DC Output Source/Sink Current +/-50 mA
ICC or IGND DC Supply Current per Supply Pin or Ground Pin +/-100 mA
TSTG Storage Temperature Range -65 to +150  deg C
TL Lead Temperature, 1 mm from Case for 10 secs 260  deg C
TJ Junction Temperature under Bias +150  deg C
/C0113JA Thermal Resistance (Note 2) SC -88
SC-74
UDFN6
377
320
154
 deg C/W
PD Power Dissipation in Still Air SC -88
SC-74
UDFN6
332
390
812
mW
MSL Moisture Sensitivity Level 1 -
FR Flamebility Rating Oxygen Index: 28 to 34 UL 94-V-0 @ 0.125
in
-
Share FeedbackYour Opinion Matters
```

### Page 3

#### Extracted tables

Table 1:

```text
VESD | ESD Withstand Voltage (Note 3) Human Body Model Charged Device Model | 2000 1000 | V
ILATCHUP | Latchup Performance (Note 4) | +/-100 | mA
```

Table 2:

```text
Symbol | Parameter | Min | Max | Unit
VCC | Positive DC Supply Voltage | 1.65 | 5.5 | V
VIN | DC Input Voltage | 0 | 5.5 | V
VOUT | DC Output Voltage Active-Mode (High or Low State) Tri-State Mode (Note 1) Power-Down Mode (VCC = 0 V) | 0 0 0 | VCC 5.5 5.5 | V
TA | Operating Temperature Range | 55 | +125 | deg C
tr , tf | Input Transition Rise or Fall Rate VCC = 1.65 V to 1.95 V VCC = 2.3 V to 2.7 V VCC = 3.0 V to 3.6 V VCC = 4.5 V to 5.5 V | 0 0 0 0 | No Limit No Limit No Limit No Limit | ns
```

Table 3:

```text
Symbol | Parameter | Condition | VCC (V) | TA = 25 deg C |  |  | 40 deg C (cid:2) TA (cid:2) 85 deg C |  | 55 deg C (cid:2) TA (cid:2) 125 deg C |  | Unit
 |  |  |  | Min | Typ | Max | Min | Max | Min | Max | 
VT+ | Positive In- put Thresh- old Voltage |  | 1.65 |  | 1.0 | 1.4 |  | 1.4 |  | 1.4 | V
 |  |  | 2.3 |  | 1.5 | 1.8 |  | 1.8 |  | 1.8 | 
 |  |  | 2.7 |  | 1.7 | 2.0 |  | 2.0 |  | 2.0 | 
 |  |  | 3.0 |  | 1.9 | 2.2 |  | 2.2 |  | 2.2 | 
 |  |  | 4.5 |  | 2.7 | 3.1 |  | 3.1 |  | 3.1 | 
 |  |  | 5.5 |  | 3.3 | 3.6 |  | 3.6 |  | 3.6 | 
VT | Negative Input Threshold Voltage |  | 1.65 | 0.2 | 0.5 |  | 0.2 |  | 0.2 |  | V
 |  |  | 2.3 | 0.4 | 0.75 |  | 0.4 |  | 0.4 |  | 
 |  |  | 2.7 | 0.5 | 0.87 |  | 0.5 |  | 0.5 |  | 
 |  |  | 3.0 | 0.6 | 1.0 |  | 0.6 |  | 0.6 |  | 
 |  |  | 4.5 | 1.0 | 1.5 |  | 1.0 |  | 1.0 |  | 
 |  |  | 5.5 | 1.2 | 1.9 |  | 1.2 |  | 1.2 |  | 
VH | Input Hysteresis Voltage |  | 1.65 | 0.1 | 0.48 | 0.9 | 0.1 | 0.9 | 0.1 | 0.9 | V
 |  |  | 2.3 | 0.25 | 0.75 | 1.1 | 0.25 | 1.1 | 0.25 | 1.1 | 
 |  |  | 2.7 | 0.3 | 0.83 | 1.15 | 0.3 | 1.15 | 0.3 | 1.15 | 
 |  |  | 3.0 | 0.4 | 0.93 | 1.2 | 0.4 | 1.2 | 0.4 | 1.2 | 
 |  |  | 4.5 | 0.6 | 1.2 | 1.5 | 0.6 | 1.5 | 0.6 | 1.5 | 
 |  |  | 5.5 | 0.7 | 1.4 | 1.7 | 0.7 | 1.7 | 0.7 | 1.7 |
```

#### Raw extracted text

```text
NL27WZ14
www.onsemi.com
3
VESD ESD Withstand Voltage (Note 3) Human Body Model
Charged Device Model
2000
1000
V
ILATCHUP Latchup Performance (Note 4) +/-100 mA
Stresses exceeding those listed in the Maximum Ratings table may damage the device. If any of these limits are exceeded, device functionality
should not be assumed, damage may occur and reliability may be affected.
1. Applicable to devices with outputs that may be tri -stated.
2. Measured with minimum pad spacing on an FR4 board, using 10 mm -by-1 inch, 2 ounce copper trace no air flow per JESD51-7.
3. HBM tested to ANSI/ESDA/JEDEC JS -001-2017. CDM tested to EIA/JESD22-C101-F. JEDEC recommends that ESD qualification to
EIA/JESD22-A115-A (Machine Model) be discontinued per JEDEC/JEP172A.
4. Tested to EIA/JESD78 Class II.
RECOMMENDED OPERATING CONDITIONS
Symbol Parameter Min Max Unit
VCC Positive DC Supply Voltage 1.65 5.5 V
VIN DC Input Voltage 0 5.5 V
VOUT DC Output Voltage Active -Mode (High or Low State)
Tri-State Mode (Note 1)
Power-Down Mode (VCC = 0 V)
0
0
0
VCC
5.5
5.5
V
TA Operating Temperature Range -55 +125  deg C
tr , tf Input Transition Rise or Fall Rate V CC = 1.65 V to 1.95 V
VCC = 2.3 V to 2.7 V
VCC = 3.0 V to 3.6 V
VCC = 4.5 V to 5.5 V
0
0
0
0
No Limit
No Limit
No Limit
No Limit
ns
Functional operation above the stresses listed in the Recommended Operating Ranges is not implied. Extended exposure to stresses beyond
the Recommended Operating Ranges limits may affect device reliability.
DC ELECTRICAL CHARACTERISTICS
TA = 25  deg C -40  deg C /C0051 TA /C0051 85  deg C -55 deg C /C0051 TA /C0051 125 deg C
Symbol Parameter Condition VCC (V) Min Typ Max Min Max Min Max Unit
VT+ Positive In-
put Thresh-
old Voltage
 1.65 - 1.0 1.4 - 1.4 - 1.4 V
2.3 - 1.5 1.8 - 1.8 - 1.8
2.7 - 1.7 2.0 - 2.0 - 2.0
3.0 - 1.9 2.2 - 2.2 - 2.2
4.5 - 2.7 3.1 - 3.1 - 3.1
5.5 - 3.3 3.6 - 3.6 - 3.6
VT- Negative
Input
Threshold
Voltage
 1.65 0.2 0.5 - 0.2 - 0.2 - V
2.3 0.4  0.75 - 0.4 - 0.4 -
2.7 0.5 0.87 - 0.5 - 0.5 -
3.0 0.6 1.0 - 0.6 - 0.6 -
4.5 1.0 1.5 - 1.0 - 1.0 -
5.5 1.2 1.9 - 1.2 - 1.2 -
VH Input
Hysteresis
Voltage
 1.65 0.1 0.48 0.9 0.1 0.9 0.1 0.9 V
2.3 0.25 0.75 1.1 0.25 1.1 0.25 1.1
2.7 0.3 0.83 1.15 0.3 1.15 0.3 1.15
3.0 0.4 0.93 1.2 0.4 1.2 0.4 1.2
4.5 0.6 1.2 1.5 0.6 1.5 0.6 1.5
5.5 0.7 1.4 1.7 0.7 1.7 0.7 1.7
Share FeedbackYour Opinion Matters
```

### Page 4

#### Extracted tables

Table 1:

```text
Symbol | Parameter | Condition | VCC (V) | TA = 25 deg C |  |  | 40 deg C (cid:2) TA (cid:2) 85 deg C |  | 55 deg C (cid:2) TA (cid:2) 125 deg C |  | Unit
 |  |  |  | Min | Typ | Max | Min | Max | Min | Max | 
VOH | High-Level Output Voltage VIN = VIH or VIL | IOH = -100 (cid:3)A | 1.65 to 5.5 | VCC - 0.1 | VCC |  | VCC - 0.1 |  | VCC - 0.1 |  | V
 |  | IOH = -4 mA | 1.65 | 1.29 | 1.52 |  | 1.29 |  | 1.29 |  | 
 |  | IOH = -8 mA | 2.3 | 1.9 | 2.1 |  | 1.9 |  | 1.9 |  | 
 |  | IOH = -12 mA | 2.7 | 2.2 | 2.4 |  | 2.2 |  | 2.2 |  | 
 |  | IOH = -16 mA | 3.0 | 2.4 | 2.7 |  | 2.4 |  | 2.4 |  | 
 |  | IOH = -24 mA | 3.0 | 2.3 | 2.5 |  | 2.3 |  | 2.3 |  | 
 |  | IOH = -32 mA | 4.5 | 3.8 | 4 |  | 3.8 |  | 3.8 |  | 
VOL | Low-Level Output Voltage VIN = VIH or VIL | IOL = 100 (cid:3)A | 1.65 to 5.5 |  |  | 0.1 |  | 0.1 |  | 0.1 | V
 |  | IOL = 4 mA | 1.65 |  | 0.08 | 0.24 |  | 0.24 |  | 0.24 | 
 |  | IOL = 8 mA | 2.3 |  | 0.2 | 0.3 |  | 0.3 |  | 0.3 | 
 |  | IOL = 12 mA | 2.7 |  | 0.22 | 0.4 |  | 0.4 |  | 0.4 | 
 |  | IOL = 16 mA | 3.0 |  | 0.28 | 0.4 |  | 0.4 |  | 0.4 | 
 |  | IOL = 24 mA | 3.0 |  | 0.38 | 0.55 |  | 0.55 |  | 0.55 | 
 |  | IOL = 32 mA | 4.5 |  | 0.42 | 0.55 |  | 0.55 |  | 0.55 | 
IIN | Input Leak- age Current | VIN = 5.5 V or GND | 1.65 to 5.5 |  |  | +/-0.1 |  | +/-1.0 |  | +/-1.0 | (cid:3)A
IOFF | Power Off Leakage Current | VIN = 5.5 V or VOUT = 5.5 V | 0 |  |  | 1 |  | 10 |  | 10 | (cid:3)A
ICC | Quiescent Supply Current | VIN = 5.5 V or GND | 5.5 |  |  | 1 |  | 10 |  | 10 | (cid:3)A
```

Table 2:

```text
I I Symbol I I | II I I I I I Parameter II I I I I I | I I I Condition I I I | II I I VCC (V) II I I | TA = 25 deg C II I I I I I I I II I II I |  |  | 40 deg C (cid:2) TA (cid:2) 85 deg C II I I I I I II I II I I III |  | 55 deg C (cid:2) TA (cid:2) 125 deg C I I I I I I I II I II |  | I I Unit I I
 |  |  |  | Min II I | Typ II I | Max II I | Min II I I I | Max I I I I | Min I I | Max II I II | 
tPLH, tPHL | Propagation Delay, A to Y (Figures 3 and 4) | RL = 1 M(cid:4), CL = 15 pF | 1.65 to 1.95 |  | 7.1 | 13 |  | 14.5 |  | 15.5 | ns
 |  | RL = 1 M(cid:4), CL = 15 pF | 2.3 to 2.7 |  | 4.3 | 7.4 |  | 8.1 |  | 9.1 | 
 |  |  | 3.0 to 3.6 |  | 3.3 | 5 |  | 5.5 |  | 6.5 | 
 |  |  | 4.5 to 5.5 |  | 2.7 | 4.1 |  | 4.5 |  | 5.5 | 
 |  | RL = 500 (cid:4), CL = 50 pF | 3.0 to 3.6 |  | 4 | 6 |  | 6.6 |  | 7.6 | 
 |  |  | 4.5 to 5.5 |  | 3.2 | 4.9 |  | 5.4 |  | 6.4 |
```

Table 3:

```text
Symbol | Parameter | Condition | Typical | Unit
CIN | Input Capacitance | VCC = 5.5 V, VI = 0 V or VCC | 2.5 | pF
COUT | Output Capacitance | VCC = 5.5 V, VI = 0 V or VCC | 4.0 | pF
CPD | Power Dissipation Capacitance (Note 5) | 10 MHz, VCC = 3.3 V, VIN = 0 V or VCC 10 MHz, VCC = 5.0 V, VIN = 0 V or VCC | 11 12.5 | pF
```

#### Raw extracted text

```text
NL27WZ14
DC ELECTRICAL CHARACTERISTICS
TA = 25  deg C -40  deg C (cid:2) TA (cid:2) 85  deg C -55 deg C (cid:2) TA (cid:2) 125 deg C
Symbol Parameter Condition VCC (V) Min Typ Max Min Max Min Max Unit
VOH High-Level IOH = -100 (cid:3)A 1.65 to 5.5 VCC - 0.1 VCC - VCC - 0.1 - VCC - 0.1 - V
Output
Voltage
IOH = -4 mA 1.65 1.29 1.52 - 1.29 - 1.29 -
VIN = VIH or IOH = -8 mA 2.3 1.9 2.1 - 1.9 - 1.9 -
VIL
IOH = -12 mA 2.7 2.2 2.4 - 2.2 - 2.2 -
IOH = -16 mA 3.0 2.4 2.7 - 2.4 - 2.4 -
IOH = -24 mA 3.0 2.3 2.5 - 2.3 - 2.3 -
IOH = -32 mA 4.5 3.8 4 - 3.8 - 3.8 -
VOL Low-Level IOL = 100 (cid:3)A 1.65 to 5.5 - - 0.1 - 0.1 - 0.1 V
Output
Voltage
IOL = 4 mA 1.65 - 0.08 0.24 - 0.24 - 0.24
VIN = VIH or IOL = 8 mA 2.3 - 0.2 0.3 - 0.3 - 0.3
VIL
IOL = 12 mA 2.7 - 0.22 0.4 - 0.4 - 0.4
IOL = 16 mA 3.0 - 0.28 0.4 - 0.4 - 0.4
IOL = 24 mA 3.0 - 0.38 0.55 - 0.55 - 0.55
IOL = 32 mA 4.5 - 0.42 0.55 - 0.55 - 0.55
IIN Input Leak- VIN = 5.5 V or 1.65 to 5.5 - - +/-0.1 - +/-1.0 - +/-1.0 (cid:3)A
age Current GND
IOFF Power Off VIN = 5.5 V or 0 - - 1 - 10 - 10 (cid:3)A
Leakage VOUT = 5.5 V
Current
ICC Quiescent VIN = 5.5 V or 5.5 - - 1 - 10 - 10 (cid:3)A
Supply GND
Current
AC ELECTRICAL CHARACTERISTICS
www.onsemi.com
4
I
I
I
I
I
I
I
I
I
I
I
I
Symbol
I
I
I
I
I
I
I
I
I
I
I
I
I
I
I
Parameter
I
I
I
I
I
I
I
I
I
I
I
I
I
I
I
Condition
I
I
I
I
I
I
I
I
I
I
I
I
VCC (V)
I
I
I
I
I
I
I
I
I
I
I
I
I
I
TA = 25  deg C
I
I
I
I
I
I
I
I
I
I
I
I
-40  deg C (cid:2) TA (cid:2) 85  deg C
I
I
I
I
I
I
I
I
I
I
I
I
-55  deg C (cid:2) TA (cid:2) 125 deg C
I
I
I
I
I
I
I
I
I
Unit
I
I
I
I
I
I
Min
I
I
I
I
I
I
Typ
I
I
I
I
I
I
Max
I
I
I
I
I
I
Min
I
I
I
I
I
I
I
I
Max
I
I
I
I
I
I
I
I
Min
I
I
I
I
I
I
Max
tPLH, Propagation RL = 1 M(cid:4), 1.65 to 1.95 - 7.1 13 - 14.5 - 15.5 ns
tPHL Delay, A to Y CL = 15 pF
(Figures 3 and
4) RL = 1 M(cid:4), 2.3 to 2.7 - 4.3 7.4 - 8.1 - 9.1
CL = 15 pF
3.0 to 3.6 - 3.3 5 - 5.5 - 6.5
4.5 to 5.5 - 2.7 4.1 - 4.5 - 5.5
RL = 500 (cid:4), 3.0 to 3.6 - 4 6 - 6.6 - 7.6
CL = 50 pF
4.5 to 5.5 - 3.2 4.9 - 5.4 - 6.4
CAPACITIVE CHARACTERISTICS
Symbol Parameter Condition Typical Unit
CIN Input Capacitance VCC = 5.5 V, VI = 0 V or VCC 2.5 pF
COUT Output Capacitance VCC = 5.5 V, VI = 0 V or VCC 4.0 pF
CPD Power Dissipation Capacitance (Note 5) 10 MHz, VCC = 3.3 V, VIN = 0 V or VCC 11 pF
10 MHz, VCC = 5.0 V, VIN = 0 V or VCC 12.5
5. CPD is defined as the value of the internal equivalent capacitance which is calculated from the operating current consumption without load.
Average operating current can be obtained by the equation: ICC(OPR) = CPD  VCC  fin ) ICC. CPD is used to determine the no-load dynamic
power consumption; PD = CPD  VCC 2  fin ) ICC  VCC.
Share Feedback
Your Opinion Matters
```

### Page 5

#### Extracted tables

Table 1:

```text
Test | Switch Position | CL, pF | RL, (cid:2) | R1, (cid:2)
tPLH / tPHL | Open | See AC Characteristics Table |  | 
tPLZ / tPZL | 2 x VCC |  |  | 
 |  | See AC Characteristics Table |  | 
tPHZ / tPZH | GND |  |  | 
 |  | See AC Characteristics Table |  |
```

Table 2:

```text
DUT
```

Table 3:

```text
VCC, V | Vmi, V | Vmo, V |  | VY, V
 |  | tPLH, tPHL | tPZL, tPLZ, tPZH, tPHZ | 
1.65 to 1.95 | VCC/2 | VCC / 2 | VCC / 2 | 0.15
2.3 to 2.7 | VCC/2 | VCC / 2 | VCC / 2 | 0.15
3.0 to 3.6 | VCC/2 | VCC / 2 | VCC / 2 | 0.3
4.5 to 5.5 | VCC/2 | VCC / 2 | VCC / 2 | 0.3
```

#### Raw extracted text

```text
NL27WZ14
OPEN
Switch
2 x VCC GND Test Position CL, pF RL, (cid:2) R1, (cid:2)
tPLH / tPHL Open See AC Characteristics Table
R1 tPLZ / tPZL 2 x VCC - - -
DUT OUTPUT See AC Characteristics Table
tPHZ / tPZH GND - - -
RT RL CL*
See AC Characteristics Table
X = Dont Care
CL includes probe and jig capacitance
RT is ZOUT of pulse generator (typically 50 (cid:4))
f = 1 MHz
Figure 3. Test Circuit
tr = 3 ns tf = 3 ns VCC
90% 90%
VCC
INPUT Vmi Vmi
INPUT Vmi Vmi
GND
10% 10%
GND
tPZL tPLZ
tPHL tPLH ~VCC
VOH
OUTPUT Vmo Vmo
OUTPUT Vmo
VOL + VY
VOL VOL
tPLH tPHL tPZH tPHZ
VOH VOH
VOH - VY
OUTPUT Vmo Vmo OUTPUT Vmo
VOL
~0 V
Figure 4. Switching Waveforms
Vmo, V
VCC, V Vmi, V tPLH, tPHL tPZL, tPLZ, tPZH, tPHZ VY, V
1.65 to 1.95 VCC/2 VCC / 2 VCC / 2 0.15
2.3 to 2.7 VCC/2 VCC / 2 VCC / 2 0.15
3.0 to 3.6 VCC/2 VCC / 2 VCC / 2 0.3
4.5 to 5.5 VCC/2 VCC / 2 VCC / 2 0.3
www.onsemi.com Share Feedback
5 Your Opinion Matters
```

### Page 6

#### Extracted tables

Table 1:

```text
Device | Package | Specific Device Code | Pin1 Orientation (See below) | Shipping
NL27WZ14DFT2G | SC-88 | MA | Q4 | 3000 / Tape & Reel
NL27WZ14DFT4G | SC-88 | MA | Q4 | 10000 / Tape & Reel
NL27WZ14DFT2G-Q* | SC-88 | MA | Q4 | 3000 / Tape & Reel
NL27WZ14DBVT1G | SC-74 | MA | Q4 | 3000 / Tape & Reel
NL27WZ14MU1TCG | UDFN6, 1.45 x 1.0, 0.5P | P (Rotated 90 deg CW) | Q4 | 3000 / Tape & Reel
NL27WZ14MU3TCG | UDFN6, 1.0 x 1.0, 0.35P | 3 (Rotated 90 deg CW) | Q4 | 3000 / Tape & Reel
```

#### Raw extracted text

```text
NL27WZ14
www.onsemi.com
6
ORDERING INFORMATION
Device Package Specific Device Code
Pin1 Orientation
(See below) Shipping
 NL27WZ14DFT2G SC-88 MA Q4 3000 / Tape & Reel
 NL27WZ14DFT4G SC-88 MA Q4 10000 / Tape & Reel
 NL27WZ14DFT2G-Q* SC-88 MA Q4 3000 / Tape & Reel
 NL27WZ14DBVT1G SC-74 MA Q4 3000 / Tape & Reel
 NL27WZ14MU1TCG UDFN6, 1.45 x 1.0, 0.5P P (Rotated 90 deg  CW) Q4 3000 / Tape & Reel
 NL27WZ14MU3TCG UDFN6, 1.0 x 1.0, 0.35P 3 (Rotated 90 deg  CW) Q4 3000 / Tape & Reel
 For information on tape and reel specifications, including part orientation and tape sizes, please refer to our Tape and Reel Packaging
Specifications Brochure, BRD8011/D.
* -Q Suffix for Automotive and Other Applications Requiring Unique Site and Control Change Requirements; AEC-Q100 Qualified and PPAP
Capable.
PIN 1 ORIENTATION IN TAPE AND REEL
Share FeedbackYour Opinion Matters
```

### Page 7

#### Extracted tables

Table 1:

```text
DOCUMENT NUMBER: | 98ASB42973B | Electronic versions are uncontrolled except when accessed directly from the Document Repository. Printed versions are uncontrolled except when stamped CONTROLLED COPY in red. | 
DESCRIPTION: | SC-74 |  | PAGE 1 OF 1
```

#### Raw extracted text

```text
SC-74
CASE 318F
ISSUE P
DATE 07 OCT 2021SCALE 2:1
STYLE 1:
PIN 1. CATHODE
2. ANODE
3. CATHODE
4. CATHODE
5. ANODE
6. CATHODE
STYLE 2:
PIN 1. NO CONNECTION
2. COLLECTOR
3. EMITTER
4. NO CONNECTION
5. COLLECTOR
6. BASE
XXX M/C0071
/C0071
XXX = Specific Device Code
M = Date Code
/C0071 = Pb-Free Package
GENERIC
MARKING DIAGRAM*
STYLE 3:
PIN 1. EMITTER 1
2. BASE 1
3. COLLECTOR 2
4. EMITTER 2
5. BASE 2
6. COLLECTOR 1
STYLE 4:
PIN 1. COLLECTOR 2
2. EMITTER 1/EMITTER 2
3. COLLECTOR 1
4. EMITTER 3
5. BASE 1/BASE 2/COLLECTOR 3
6. BASE 3
STYLE 5:
PIN 1. CHANNEL 1
2. ANODE
3. CHANNEL 2
4. CHANNEL 3
5. CATHODE
6. CHANNEL 4
STYLE 6:
PIN 1. CATHODE
2. ANODE
3. CATHODE
4. CATHODE
5. CATHODE
6. CATHODE
1
6
STYLE 7:
PIN 1. SOURCE 1
2. GATE 1
3. DRAIN 2
4. SOURCE 2
5. GATE 2
6. DRAIN 1
STYLE 8:
PIN 1. EMITTER 1
2. BASE 2
3. COLLECTOR 2
4. EMITTER 2
5. BASE 1
6. COLLECTOR 1
STYLE 9:
PIN 1. EMITTER 2
2. BASE 2
3. COLLECTOR 1
4. EMITTER 1
5. BASE 1
6. COLLECTOR 2
(Note: Microdot may be in either location)
STYLE 10:
PIN 1. ANODE/CATHODE
2. BASE
3. EMITTER
4. COLLECTOR
5. ANODE
6. CATHODE
STYLE 11:
PIN 1. EMITTER
2. BASE
3. ANODE/CATHODE
4. ANODE
5. CATHODE
6. COLLECTOR
*This information is generic. Please refer to
device data sheet for actual part marking.
Pb-Free indicator, G or microdot  /C0071, may
or may not be present. Some products may
not follow the Generic Marking.
MECHANICAL CASE OUTLINE
PACKAGE DIMENSIONS
98ASB42973BDOCUMENT NUMBER:
DESCRIPTION:
Electronic versions are uncontrolled except when accessed directly from the Document Repository.
Printed  versions are uncontrolled  except when stamped  CONTROLLED COPY in red.
PAGE 1 OF 1SC-74
onsemi and                     are trademarks of Semiconductor Components Industries, LLC dba onsemi or its subsidiaries in the United States and/or other countries. onsemi reserves
the right to make changes without further notice to any products herein. onsemi makes no warranty, representation or guarantee regarding the suitability of its products for any particular
purpose, nor does onsemi assume any liability arising out of the application or use of any product or circuit, and specifically disclaims any and all liability, including without limitation
special, consequential or incidental damages. onsemi does not convey any license under its patent rights nor the rights of others.
  Semiconductor Components Industries, LLC, 2019 www.onsemi.com
```

### Page 8

#### Extracted tables

Table 1:

```text
DOCUMENT NUMBER: | 98ASB42985B | Electronic versions are uncontrolled except when accessed directly from the Document Repository. Printed versions are uncontrolled except when stamped CONTROLLED COPY in red. | 
DESCRIPTION: | SC-88 2.00x1.25x0.90, 0.65P |  | PAGE 1 OF 2
```

#### Raw extracted text

```text
SC-88 2.00x1.25x0.90, 0.65P
CASE 419B-02
ISSUE Z
DATE 18 APR 2024
XXXM/C0071
/C0071
XXX = Specific Device Code
M = Date Code*
/C0071= Pb-Free Package
GENERIC
MARKING DIAGRAM*
1
6
STYLES ON PAGE 2
(Note: Microdot may be in either location)
*Date Code orientation and/or position may
vary depending upon manufacturing location.
*This information is generic. Please refer to
device data sheet for actual part marking.
Pb-Free indicator, G or microdot  /C0071, may
or may not be present. Some products may
not follow the Generic Marking.
MECHANICAL CASE OUTLINE
PACKAGE DIMENSIONS
98ASB42985BDOCUMENT NUMBER:
DESCRIPTION:
Electronic versions are uncontrolled except when accessed directly from the Document Repository.
Printed  versions are uncontrolled  except when stamped  CONTROLLED COPY in red.
PAGE 1 OF 2SC-88 2.00x1.25x0.90, 0.65P
onsemi and                     are trademarks of Semiconductor Components Industries, LLC dba onsemi or its subsidiaries in the United States and/or other countries. onsemi reserves
the right to make changes without further notice to any products herein. onsemi makes no warranty, representation or guarantee regarding the suitability of its products for any particular
purpose, nor does onsemi assume any liability arising out of the application or use of any product or circuit, and specifically disclaims any and all liability, including without limitation
special, consequential or incidental damages. onsemi does not convey any license under its patent rights nor the rights of others.
  Semiconductor Components Industries, LLC, 2019 www.onsemi.com
```

### Page 9

#### Extracted tables

Table 1:

```text
DOCUMENT NUMBER: | 98ASB42985B | Electronic versions are uncontrolled except when accessed directly from the Document Repository. | 
 |  | Printed versions are uncontrolled except when stamped CONTROLLED COPY in red. | 
DESCRIPTION: | SC-88 2.00x1.25x0.90, 0.65P |  | PAGE 2 OF 2
onsemi and are trademarks of Semiconductor Components Industries, LLC dba onsemi or its subsidiaries in the United States and/or other countries. onsemi reserves the right to make changes without further notice to any products herein. onsemi makes no warranty, representation or guarantee regarding the suitability of its products for any particular purpose, nor does onsemi assume any liability arising out of the application or use of any product or circuit, and specifically disclaims any and all liability, including without limitation special, consequential or incidental damages. onsemi does not convey any license under its patent rights nor the rights of others. |  |  | 
www.onsemi.com |  |  | 
2 Semiconductor Components Industries, LLC, 2019 www.onsemi.com |  |  |
```

#### Raw extracted text

```text
www.onsemi.com
2
STYLE 1:
PIN 1. EMITTER 2
 2. BASE 2
 3. COLLECTOR 1
 4. EMITTER 1
 5. BASE 1
 6. COLLECTOR 2
STYLE 3:
CANCELLED
STYLE 2:
CANCELLED
STYLE 4:
PIN 1. CATHODE
 2. CATHODE
 3. COLLECTOR
 4. EMITTER
 5. BASE
 6. ANODE
STYLE 5:
PIN 1. ANODE
 2. ANODE
 3. COLLECTOR
 4. EMITTER
 5. BASE
 6. CATHODE
STYLE 6:
PIN 1. ANODE 2
 2. N/C
 3. CATHODE 1
 4. ANODE 1
 5. N/C
 6. CATHODE 2
STYLE 7:
PIN 1. SOURCE 2
 2. DRAIN 2
 3. GATE 1
 4. SOURCE 1
 5. DRAIN 1
 6. GATE 2
STYLE 8:
CANCELLED
STYLE 11:
PIN 1. CATHODE 2
 2. CATHODE 2
 3. ANODE 1
 4. CATHODE 1
 5. CATHODE 1
 6. ANODE 2
STYLE 9:
PIN 1. EMITTER 2
 2. EMITTER 1
 3. COLLECTOR 1
 4. BASE 1
 5. BASE 2
 6. COLLECTOR 2
STYLE 10:
PIN 1. SOURCE 2
 2. SOURCE 1
 3. GATE 1
 4. DRAIN 1
 5. DRAIN 2
 6. GATE 2
STYLE 12:
PIN 1. ANODE 2
 2. ANODE 2
 3. CATHODE 1
 4. ANODE 1
 5. ANODE 1
 6. CATHODE 2
STYLE 13:
PIN 1. ANODE
 2. N/C
 3. COLLECTOR
 4. EMITTER
 5. BASE
 6. CATHODE
STYLE 14:
PIN 1. VREF
 2. GND
 3. GND
 4. IOUT
 5. VEN
 6. VCC
STYLE 15:
PIN 1. ANODE 1
 2. ANODE 2
 3. ANODE 3
 4. CATHODE 3
 5. CATHODE 2
 6. CATHODE 1
STYLE 17:
PIN 1. BASE 1
 2. EMITTER 1
 3. COLLECTOR 2
 4. BASE 2
 5. EMITTER 2
 6. COLLECTOR 1
STYLE 16:
PIN 1. BASE 1
 2. EMITTER 2
 3. COLLECTOR 2
 4. BASE 2
 5. EMITTER 1
 6. COLLECTOR 1
STYLE 18:
PIN 1. VIN1
 2. VCC
 3. VOUT2
 4. VIN2
 5. GND
 6. VOUT1
STYLE 19:
PIN 1. I OUT
 2. GND
 3. GND
 4. V CC
 5. V EN
 6. V REF
STYLE 20:
PIN 1. COLLECTOR
 2. COLLECTOR
 3. BASE
 4. EMITTER
 5. COLLECTOR
 6. COLLECTOR
STYLE 22:
PIN 1. D1 (i)
 2. GND
 3. D2 (i)
 4. D2 (c)
 5. VBUS
 6. D1 (c)
STYLE 21:
PIN 1. ANODE 1
 2. N/C
 3. ANODE 2
 4. CATHODE 2
 5. N/C
 6. CATHODE 1
STYLE 23:
PIN 1.  Vn
 2. CH1
 3. Vp
 4. N/C
 5. CH2
 6. N/C
STYLE 24:
PIN 1. CATHODE
 2. ANODE
 3. CATHODE
 4. CATHODE
 5. CATHODE
 6. CATHODE
STYLE 25:
PIN 1. BASE 1
 2. CATHODE
 3. COLLECTOR 2
 4. BASE 2
 5. EMITTER
 6. COLLECTOR 1
STYLE 26:
PIN 1. SOURCE 1
 2. GATE 1
 3. DRAIN 2
 4. SOURCE 2
 5. GATE 2
 6. DRAIN 1
STYLE 27:
PIN 1. BASE 2
 2. BASE 1
 3. COLLECTOR 1
 4. EMITTER 1
 5. EMITTER 2
 6. COLLECTOR 2
STYLE 28:
PIN 1. DRAIN
 2. DRAIN
 3. GATE
 4. SOURCE
 5. DRAIN
 6. DRAIN
STYLE 29:
PIN 1. ANODE
 2. ANODE
 3. COLLECTOR
 4. EMITTER
 5. BASE/ANODE
 6. CATHODE
SC-88 2.00x1.25x0.90, 0.65P
CASE 419B-02
ISSUE Z
DATE 18 APR 2024
STYLE 30:
PIN 1. SOURCE 1
 2. DRAIN 2
 3. DRAIN 2
 4. SOURCE 2
 5. GATE 1
 6. DRAIN 1
Note: Please refer to datasheet for
style callout. If style type is not called
out in the datasheet refer to the device
datasheet pinout or pin assignment.
98ASB42985BDOCUMENT NUMBER:
DESCRIPTION:
Electronic versions are uncontrolled except when accessed directly from the Document Repository.
Printed  versions are uncontrolled  except when stamped  CONTROLLED COPY in red.
PAGE 2 OF 2SC-88 2.00x1.25x0.90, 0.65P
onsemi and                     are trademarks of Semiconductor Components Industries, LLC dba onsemi or its subsidiaries in the United States and/or other countries. onsemi reserves
the right to make changes without further notice to any products herein. onsemi makes no warranty, representation or guarantee regarding the suitability of its products for any particular
purpose, nor does onsemi assume any liability arising out of the application or use of any product or circuit, and specifically disclaims any and all liability, including without limitation
special, consequential or incidental damages. onsemi does not convey any license under its patent rights nor the rights of others.
  Semiconductor Components Industries, LLC, 2019 www.onsemi.com
```

### Page 10

#### Extracted tables

Table 1:

```text
A
B
```

Table 2:

```text
E E | E
E E | E
```

Table 3:

```text
DIM | MILLIMETERS | 
 | MIN | MAX
A | 0.45 | 0.55
A1 | 0.00 | 0.05
A2 | 0.07 REF | 
b | 0.20 | 0.30
D | 1.45 BSC | 
E | 1.00 BSC | 
e | 0.50 BSC | 
L | 0.30 | 0.40
L1 |  | 0.15
```

Table 4:

```text
| 0.10
```

Table 5:

```text
| 0.10 C
```

Table 6:

```text
E E
```

Table 7:

```text
| 0.05
```

Table 8:

```text
| 0.05
```

Table 9:

```text
| 0.10 | C | A | B
 | 0.05 | C |  |
```

Table 10:

```text
DOCUMENT NUMBER: | 98AON30313E | Electronic versions are uncontrolled except when accessed directly from the Document Repository. Printed versions are uncontrolled except when stamped CONTROLLED COPY in red. | 
DESCRIPTION: | UDFN6, 1.45x1.0, 0.5P |  | PAGE 1 OF 1
```

#### Raw extracted text

```text
UDFN6, 1.45x1.0, 0.5P
CASE 517AQ
ISSUE O
DATE 15 MAY 2008SCALE 4:1
NOTES:
1. DIMENSIONING AND TOLERANCING PER
ASME Y14.5M, 1994.
2. CONTROLLING DIMENSION: MILLIMETERS.
3. DIMENSION b APPLIES TO PLATED TERMINAL
AND IS MEASURED BETWEEN 0.15 AND
0.30 mm FROM THE TERMINAL TIP .
EEE
EEE
A
B
E
D
BOTTOM VIEW
b
e
6X
0.10 B
0.05
AC
C
L6X
NOTE 3
0.10 C
PIN ONE
REFERENCE
TOP VIEW
0.10 C
6X
A
A10.05 C
0.05 C
C SEATING
PLANESIDE VIEW
1 3
46
1
DIM MIN MAX
MILLIMETERS
A 0.45 0.55
A1 0.00 0.05
b 0.20 0.30
D 1.45 BSC
E 1.00 BSC
e 0.50 BSC
L 0.30 0.40
L1 --- 0.15
DIMENSIONS: MILLIMETERS
0.30
6X
1.24
0.53
PITCH
*For additional information on our Pb-Free strategy and soldering
details, please download the onsemi Soldering and Mounting
Techniques Reference Manual, SOLDERRM/D.
0.50
1
MOUNTING FOOTPRINT
PACKAGE
OUTLINE
L1
DETAIL A
L
OPTIONAL
CONSTRUCTIONS
L
EEEE
EE
DETAIL B
MOLD CMPDEXPOSED Cu
OPTIONAL
CONSTRUCTIONS
A2 0.07 REF
6X
A2
DETAIL B
DETAIL A
GENERIC
MARKING DIAGRAM*
X = Specific Device
Code
M = Date Code
XM
*This information is generic. Please refer to
device data sheet for actual part marking.
Pb-Free indicator, G or microdot  /C0071,
may or may not be present.
MECHANICAL CASE OUTLINE
PACKAGE DIMENSIONS
98AON30313EDOCUMENT NUMBER:
DESCRIPTION:
Electronic versions are uncontrolled except when accessed directly from the Document Repository.
Printed  versions are uncontrolled  except when stamped  CONTROLLED COPY in red.
PAGE 1 OF 1UDFN6, 1.45x1.0, 0.5P
onsemi and                     are trademarks of Semiconductor Components Industries, LLC dba onsemi or its subsidiaries in the United States and/or other countries. onsemi reserves
the right to make changes without further notice to any products herein. onsemi makes no warranty, representation or guarantee regarding the suitability of its products for any particular
purpose, nor does onsemi assume any liability arising out of the application or use of any product or circuit, and specifically disclaims any and all liability, including without limitation
special, consequential or incidental damages. onsemi does not convey any license under its patent rights nor the rights of others.
  Semiconductor Components Industries, LLC, 2018 www.onsemi.com
```

### Page 11

#### Extracted tables

Table 1:

```text
A | B
```

Table 2:

```text
E E | 
E E E E |
```

Table 3:

```text
0.10 | C
```

Table 4:

```text
DIM | MILLIMETERS | 
 | MIN | MAX
A | 0.45 | 0.55
A1 | 0.00 | 0.05
A3 | 0.13 REF | 
b | 0.12 | 0.22
D | 1.00 BSC | 
E | 1.00 BSC | 
e | 0.35 BSC | 
L | 0.25 | 0.35
L1 | 0.30 | 0.40
```

Table 5:

```text
0.10 | C
```

Table 6:

```text
0.0 | 5 C
```

Table 7:

```text
0.0 | 5 C
```

Table 8:

```text
| 0.10 M | C | A | B
 | 0.05 M | C |  |
```

Table 9:

```text
DOCUMENT NUMBER: | 98AON56787E | Electronic versions are uncontrolled except when accessed directly from the Document Repository. Printed versions are uncontrolled except when stamped CONTROLLED COPY in red. | 
DESCRIPTION: | UDFN6, 1x1, 0.35P |  | PAGE 1 OF 1
```

#### Raw extracted text

```text
EE
EE
EE
UDFN6, 1x1, 0.35P
CASE 517BX
ISSUE O
DATE  18 MAY 2011SCALE 4:1
NOTES:
1. DIMENSIONING AND TOLERANCING PER
ASME Y14.5M, 1994.
2. CONTROLLING DIMENSION: MILLIMETERS.
3. DIMENSION b APPLIES TO PLATED
TERMINAL AND IS MEASURED BETWEEN
0.15 AND 0.20 MM FROM TERMINAL TIP .
4. PACKAGE DIMENSIONS EXCLUSIVE OF
BURRS AND MOLD FLASH.
*For additional information on our Pb-Free strategy and soldering
details, please download the onsemi Soldering and Mounting
Techniques Reference Manual, SOLDERRM/D.
SOLDERING FOOTPRINT*
RECOMMENDED
DIM MIN MAX
MILLIMETERS
A 0.45 0.55
A1 0.00 0.05
A3 0.13 REF
b 0.12 0.22
D 1.00 BSC
E 1.00 BSC
e 0.35 BSC
L 0.25 0.35
L1 0.30 0.40
A B
E
D
0.10 C
PIN ONE
REFERENCE
TOP VIEW0.10 C
A
A1
0.05 C
0.05 C
C SEATING
PLANESIDE VIEW
GENERIC
MARKING DIAGRAM*
X = Specific Device Code
M = Date Code
X M
1
2X
2X
A3
BOTTOM VIEW
b
e
6X
0.10 B
0.05
AC
C
L5X
NOTE 3
L1
1 3
46
M
M DIMENSIONS: MILLIMETERS
0.22
5X
0.48 6X
1.18
0.53 PITCH
0.351
PKG
OUTLINE
*This information is generic. Please refer to
device data sheet for actual part marking.
Pb-Free indicator, G or microdot  /C0071, may
or may not be present. Some products may
not follow the Generic Marking.
MECHANICAL CASE OUTLINE
PACKAGE DIMENSIONS
98AON56787EDOCUMENT NUMBER:
DESCRIPTION:
Electronic versions are uncontrolled except when accessed directly from the Document Repository.
Printed  versions are uncontrolled  except when stamped  CONTROLLED COPY in red.
PAGE 1 OF 1UDFN6, 1x1, 0.35P
onsemi and                     are trademarks of Semiconductor Components Industries, LLC dba onsemi or its subsidiaries in the United States and/or other countries. onsemi reserves
the right to make changes without further notice to any products herein. onsemi makes no warranty, representation or guarantee regarding the suitability of its products for any particular
purpose, nor does onsemi assume any liability arising out of the application or use of any product or circuit, and specifically disclaims any and all liability, including without limitation
special, consequential or incidental damages. onsemi does not convey any license under its patent rights nor the rights of others.
  Semiconductor Components Industries, LLC, 2018 www.onsemi.com
```

### Page 12

#### Raw extracted text

```text
onsemi,  , and other names, marks, and brands are registered and/or common law trademarks of Semiconductor Components Industries, LLC  dba onsemi or its affiliates
and/or subsidiaries in the United States and/or other countries. onsemi owns the rights to a number of patents, trademarks, copyrights, trade secrets, and other intellectual property.
A listing of onsemis product/patent coverage may be accessed at www.onsemi.com/site/pdf/Patent-Marking.pdf. onsemi reserves the right to make changes at any time to any
products or information herein, without notice. The information herein is provided as-is and onsemi makes no warranty, representation or guarantee regarding the accuracy of the
information, product features, availability, functionality, or suitability of its products for any particular purpose, nor does onsemi assume any liability arising out of the application or use
of any product or circuit, and specifically disclaims any and all liability, including without limitation special, consequential or incidental damages. Buyer is responsible for its products
and applications using onsemi products, including compliance with all laws, regulations and safety requirements or standards, regardless of any support or applications information
provided by onsemi. Typical parameters which may be provided in onsemi data sheets and/or specifications can and do vary in different applications and actual performance may
vary over time. All operating parameters, including Typicals must be validated for each customer application by customers technical experts. onsemi does not convey any license
under any of its intellectual property rights nor the rights of others. onsemi products are not designed, intended, or authorized for use as a critical component in life support systems
or any FDA Class 3 medical devices or medical devices with a same or similar classification in a foreign jurisdiction or any devices intended for implantation in the human body. Should
Buyer purchase or use onsemi products for any such unintended or unauthorized application, Buyer shall indemnify and hold onsemi and its officers, employees, subsidiaries, affiliates,
and distributors harmless against all claims, costs, damages, and expenses, and reasonable attorney fees arising out of, direct ly or indirectly, any claim of personal injury or death
associated with such unintended or unauthorized use, even if such claim alleges that onsemi was negligent regarding the design or manufacture of the part. onsemi is an Equal
Opportunity/Affirmative Action Employer. This literature is subject to all applicable copyright laws and is not for resale in any manner.
ADDITIONAL INFORMATION
TECHNICAL PUBLICATIONS:
Technical Library: www.onsemi.com/design/resources/technical-documentation
onsemi Website: www.onsemi.com
ONLINE SUPPORT: www.onsemi.com/support
For additional information, please contact your local Sales Representative at
www.onsemi.com/support/sales
```
