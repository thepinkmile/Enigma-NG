# 74HC157-Q100 / 74HCT157-Q100 - Quad 2-input multiplexer

## Source Reference

- Source PDF: [74HC_HCT157_Q100-datasheet.pdf](74HC_HCT157_Q100-datasheet.pdf)
- Source path: `design\Datasheets\74HC_HCT157_Q100-datasheet.pdf`
- Generated markdown: `74HC_HCT157_Q100-datasheet.md`
- Review note: manually checked against the source PDF; curated summary added and the raw page-by-page extraction is preserved below.

## Part Identity and Ordering

- Nexperia automotive Grade 1 logic family covering `74HC157-Q100` and `74HCT157-Q100`.
- Device function: quad 2-input multiplexer with common select `S` and active-low enable `E`.
- Reviewed ordering identities from the PDF:
  - `74HC157D-Q100`, `74HCT157D-Q100` - SO16, SOT109-1.
  - `74HC157PW-Q100`, `74HCT157PW-Q100` - TSSOP16, SOT403-1.
  - `74HC157BQ-Q100`, `74HCT157BQ-Q100` - DHVQFN16, SOT763-1.

## Pin / Pad Designations

- `S` pin 1: common data select input.
- `1I0` to `4I0` pins 2, 5, 11, 14: source-0 inputs.
- `1I1` to `4I1` pins 3, 6, 10, 13: source-1 inputs.
- `1Y` to `4Y` pins 4, 7, 9, 12: outputs.
- `GND` pin 8 and `VCC` pin 16.
- `E` pin 15: active-low enable; `E = H` forces all `nY = L`, `E = L` enables the selected path.
- DHVQFN16 exposed center pad is not a required electrical ground pin; if soldered, keep it floating or tie it to GND per the PDF note.

## Ratings and Operating Conditions

- `74HC157-Q100` supply range: 2.0 V to 6.0 V.
- `74HCT157-Q100` supply range: 4.5 V to 5.5 V.
- Ambient operating range: -40 deg C to +125 deg C.
- Absolute maximum highlights: `VCC` -0.5 V to +7 V, `IIK`/`IOK` up to +/-20 mA, output current up to +/-25 mA, `ICC` up to 50 mA.
- Total power dissipation: 500 mW, with package-specific derating above the stated temperatures.

## Package and Mechanical Notes

- SO16 body width: 3.9 mm.
- TSSOP16 body width: 4.4 mm.
- DHVQFN16 body: 2.5 x 3.5 x 0.85 mm.
- The DHVQFN option includes side-wettable flanks for AOI-friendly solder inspection.

## Formulas / Logic Content

- No standalone analog design equations are called out in the reviewed PDF.
- The key logic relationship is the function table on PDF page 3: `S` selects source 0 or source 1 while `E` disables the outputs when HIGH.

## Applications and Design Content

- Automotive AEC-Q100 Grade 1 qualified logic for multiplexing two data sources onto four outputs.
- Input clamp diodes allow resistor-limited interfacing to voltages above `VCC`.

## Searchability Note

- The raw page-by-page extraction below is intentionally preserved for local text search.
- Package drawing dimensions remain easier to confirm in the source PDF than in plain extracted text.

## Page-by-Page Extracted Text

### Page 1

```text
74HC157-Q100; 74HCT157-Q100
Quad 2-input multiplexer
Rev. 4 - 28 May 2024 Product data sheet
1.  General description
The 74HC157-Q100; 74HCT157-Q100 is a quad 2-input multiplexer. The device features select
(S) and enable E inputs. A HIGH on S selects data source 1, a LOW data source 0. A HIGH on E
forces all the outputs (1Y to 4Y) LOW. Inputs include clamp diodes. This enables the use of current
limiting resistors to interface inputs to voltages in excess of VCC.
This product has been qualified to the Automotive Electronics Council (AEC) standard Q100
(Grade 1) and is suitable for use in automotive applications.
2.  Features and benefits
- Automotive product qualification in accordance with AEC-Q100 (Grade 1)
- Specified from -40  degC to +85  degC and from -40  degC to +125  degC
- Wide supply voltage range from 2.0 V to 6.0 V
- CMOS low power dissipation
- High noise immunity
- Latch-up performance exceeds 100 mA per JESD 78 Class II Level B
- Complies with JEDEC standards:
- JESD8C (2.7 V to 3.6 V)
- JESD7A (2.0 V to 6.0 V)
- Input levels:
- For 74HC157-Q100: CMOS level
- For 74HCT157-Q100: TTL level
- Non-inverting data path
- ESD protection:
- HBM: ANSI/ESDA/JEDEC JS-001 class 2 exceeds 2000 V
- CDM: ANSI/ESDA/JEDEC JS-002 class C3 exceeds 1000 V
- Multiple package options
- DHVQFN package with Side-Wettable Flanks enabling Automatic Optical Inspection (AOI) of
solder joints
3.  Ordering information
Table 1. Ordering information
PackageType number
Temperature range Name Description Version
74HC157D-Q100
74HCT157D-Q100
-40  degC to +125  degC SO16 plastic small outline package; 16 leads;
body width 3.9 mm
SOT109-1
74HC157PW-Q100
74HCT157PW-Q100
-40  degC to +125  degC TSSOP16 plastic thin shrink small outline package;
16 leads; body width 4.4 mm
SOT403-1
74HC157BQ-Q100
74HCT157BQ-Q100
-40  degC to +125  degC DHVQFN16 plastic dual in-line compatible thermal
enhanced very thin quad flat package; no leads;
16 terminals; body 2.5  x  3.5  x  0.85 mm
SOT763-1
```

### Page 2

```text
Nexperia 74HC157-Q100; 74HCT157-Q100
Quad 2-input multiplexer
4.  Functional diagram
1Y
1I1
1I0
2Y
2I1
2I0
3Y
3I1
3I0

mna484
4Y
4I1
4I0
S
E
Fig. 1. Logic diagram
mna481
S1
15
12974
131410116532
E
1Y
1I11I0
2Y
2I12I0
3Y
3I13I0
4Y
4I14I0
Fig. 2. logic symbol
mna483
MULTIPLEXER
OUTPUTSSELECTOR
1Y
2Y
3Y
4Y 12
9
7
4
S
13
151
14
10
11
6
5
3
2
E
1I0
1I1
2I0
2I1
3I0
3I1
4I0
4I1
Fig. 3. Logic symbol
mna482
12
9
7
1 G1
15 EN
1 MUX
1
4
13
14
10
11
6
5
3
2
Fig. 4. IEC logic symbol
74HC_HCT157_Q100 All information provided in this document is subject to legal disclaimers. (c)
Nexperia B.V. 2024. All rights reserved
Product data sheet Rev. 4 - 28 May 2024 2 / 15
```

### Page 3

```text
Nexperia 74HC157-Q100; 74HCT157-Q100
Quad 2-input multiplexer
5.  Pinning information
5.1.  Pinning
D package
SOT109-1 (SO16)
S VCC
1I0 E
1I1 4I0
1Y 4I1
2I0 4Y
2I1 3I0
2Y 3I1
GND 3Y
aaa-035777
1
2
3
4
5
6
7
8
10
9
12
11
14
13
16
15

PW package
SOT403-1 (TSSOP16)
S VCC
1I0 E
1I1 4I0
1Y 4I1
2I0 4Y
2I1 3I0
2Y 3I1
GND 3Y
aaa-035776
1
2
3
4
5
6
7
8
10
9
12
11
14
13
16
15

aaa-035778
BQ package
SOT763-1 (DHVQFN16)
2Y 3I1
2I1 3I0
2I0 4Y
GND(1)
1Y 4I1
1I1 4I0
1I0 E
GND
3Y
S
VCC
Transparent top view
7 10
6 11
5 12
4 13
3 14
2 15
8
9
1
16
terminal 1
index area
(1) This is not a ground pin. There is no electrical or mechanical requirement to solder
the pad. In case soldered, the solder land should remain floating or connected to GND.
5.2.  Pin description
Table 2. Pin description
Symbol Pin Description
S 1 common data select input
1I0 to 4I0 2, 5, 11, 14 data inputs from source 0
1I1 to 4I1 3, 6, 10, 13 data inputs from source 1
1Y to 4Y 4, 7, 9, 12 multiplexer outputs
GND 8 ground (0 V)
E 15 enable input (active LOW)
VCC 16 supply voltage
6.  Functional description
Table 3. Function table
H = HIGH voltage level; L = LOW voltage level; X = don't care.
Input Output
E S nI0 nI1 nY
H X X X L
L L L X L
L L H X H
L H X L L
L H X H H
74HC_HCT157_Q100 All information provided in this document is subject to legal disclaimers. (c)
Nexperia B.V. 2024. All rights reserved
Product data sheet Rev. 4 - 28 May 2024 3 / 15
```

### Page 4

```text
Nexperia 74HC157-Q100; 74HCT157-Q100
Quad 2-input multiplexer
7.  Limiting values
Table 4. Limiting values
In accordance with the Absolute Maximum Rating System (IEC 60134). Voltages are referenced to GND
(ground = 0 V).
Symbol Parameter Conditions Min Max Unit
VCC supply voltage -0.5 +7 V
IIK input clamping current VI < -0.5 V or VI > VCC + 0.5 V - +/-20 mA
IOK output clamping current VO < -0.5 V or VO > VCC + 0.5 V - +/-20 mA
IO output current VO = -0.5 V to VCC + 0.5 V - +/-25 mA
ICC supply current - +50 mA
IGND ground current -50 - mA
Tstg storage temperature -65 +150  degC
Ptot total power dissipation Tamb = -40  degC to +125  degC [1] - 500 mW
[1] For SOT109-1 (SO16) package: Ptot derates linearly with 12.4 mW/K above 110  degC.
For SOT403-1 (TSSOP16) package: Ptot derates linearly with 8.5 mW/K above 91  degC.
For SOT763-1 (DHVQFN16) package: Ptot derates linearly with 11.2 mW/K above 106  degC.
8.  Recommended operating conditions
Table 5. Recommended operating conditions
Voltages are referenced to GND (ground = 0 V)
74HC157-Q100 74HCT157-Q100Symbol Parameter Conditions
Min Typ Max Min Typ Max
Unit
VCC supply voltage 2.0 5.0 6.0 4.5 5.0 5.5 V
VI input voltage 0 - VCC 0 - VCC V
VO output voltage 0 - VCC 0 - VCC V
Tamb ambient temperature -40 +25 +125 -40 +25 +125  degC
VCC = 2.0 V - - 625 - - - ns/V
VCC = 4.5 V - 1.67 139 - 1.67 139 ns/V
t/V input transition rise and fall rate
VCC = 6.0 V - - 83 - - - ns/V
74HC_HCT157_Q100 All information provided in this document is subject to legal disclaimers. (c)
Nexperia B.V. 2024. All rights reserved
Product data sheet Rev. 4 - 28 May 2024 4 / 15
```

### Page 5

```text
Nexperia 74HC157-Q100; 74HCT157-Q100
Quad 2-input multiplexer
9.  Static characteristics
Table 6. Static characteristics
At recommended operating conditions; voltages are referenced to GND (ground = 0 V).
Tamb = 25  degC Tamb = -40  degC
to +85  degC
Tamb = -40  degC
to +125  degC
Symbol Parameter Conditions
Min Typ Max Min Max Min Max
Unit
74HC157-Q100
VCC = 2.0 V 1.5 1.2 - 1.5 - 1.5 - V
VCC = 4.5 V 3.15 2.4 - 3.15 - 3.15 - V
VIH HIGH-level
input voltage
VCC = 6.0 V 4.2 3.2 - 4.2 - 4.2 - V
VCC = 2.0 V - 0.8 0.5 - 0.5 - 0.5 V
VCC = 4.5 V - 2.1 1.35 - 1.35 - 1.35 V
VIL LOW-level
input voltage
VCC = 6.0 V - 2.8 1.8 - 1.8 - 1.8 V
VI = VIH or VIL
IO = -20 uA; VCC = 2.0 V 1.9 2.0 - 1.9 - 1.9 - V
IO = -20 uA; VCC = 4.5 V 4.4 4.5 - 4.4 - 4.4 - V
IO = -20 uA; VCC = 6.0 V 5.9 6.0 - 5.9 - 5.9 - V
IO = -4.0 mA; VCC = 4.5 V 3.98 4.32 - 3.84 - 3.7 - V
VOH HIGH-level
output voltage
IO = -5.2 mA; VCC = 6.0 V 5.48 5.81 - 5.34 - 5.2 - V
VI = VIH or VIL
IO = 20 uA; VCC = 2.0 V - 0 0.1 - 0.1 - 0.1 V
IO = 20 uA; VCC = 4.5 V - 0 0.1 - 0.1 - 0.1 V
IO = 20 uA; VCC = 6.0 V - 0 0.1 - 0.1 - 0.1 V
IO = 4.0 mA; VCC = 4.5 V - 0.15 0.26 - 0.33 - 0.4 V
VOL LOW-level
output voltage
IO = 5.2 mA; VCC = 6.0 V - 0.16 0.26 - 0.33 - 0.4 V
II input leakage
current
VI = VCC or GND; VCC = 6.0 V - - +/-0.1 - +/-1.0 - +/-1.0 uA
ICC supply current VI = VCC or GND; IO = 0 A;
VCC = 6.0 V
- - 8.0 - 80 - 160 uA
CI input
capacitance
- 3.5 - - - - - pF
74HC_HCT157_Q100 All information provided in this document is subject to legal disclaimers. (c)
Nexperia B.V. 2024. All rights reserved
Product data sheet Rev. 4 - 28 May 2024 5 / 15
```

### Page 6

```text
Nexperia 74HC157-Q100; 74HCT157-Q100
Quad 2-input multiplexer
Tamb = 25  degC Tamb = -40  degC
to +85  degC
Tamb = -40  degC
to +125  degC
Symbol Parameter Conditions
Min Typ Max Min Max Min Max
Unit
74HCT157-Q100
VIH HIGH-level
input voltage
VCC = 4.5 V to 5.5 V 2.0 1.6 - 2.0 - 2.0 - V
VIL LOW-level
input voltage
VCC = 4.5 V to 5.5 V - 1.2 0.8 - 0.8 - 0.8 V
VI = VIH or VIL; VCC = 4.5 V
IO = -20 uA 4.4 4.5 - 4.4 - 4.4 - V
VOH HIGH-level
output voltage
IO = -4 mA 3.98 4.32 - 3.84 - 3.7 - V
VI = VIH or VIL; VCC = 4.5 V
IO = 20 uA - 0 0.1 - 0.1 - 0.1 V
VOL LOW-level
output voltage
IO = 4.0 mA - 0.15 0.26 - 0.33 - 0.4 V
II input leakage
current
VI = VCC or GND; VCC = 5.5 V - - +/-0.1 - +/-1.0 - +/-1.0 uA
ICC supply current VI = VCC or GND; IO = 0 A;
VCC = 5.5 V
- - 8.0 - 80 - 160 uA
VI = VCC - 2.1 V; IO = 0 A;
other inputs at VCC or GND;
VCC = 4.5 V to 5.5 V
per input pin; nI0, nI1 inputs - 100 360 - 450 - 490 uA
per input pin; E input - 60 216 - 270 - 294 uA
ICC additional
supply current
per input pin; S input - 100 360 - 450 - 490 uA
CI input
capacitance
- 3.5 - - - - - pF
74HC_HCT157_Q100 All information provided in this document is subject to legal disclaimers. (c)
Nexperia B.V. 2024. All rights reserved
Product data sheet Rev. 4 - 28 May 2024 6 / 15
```

### Page 7

```text
Nexperia 74HC157-Q100; 74HCT157-Q100
Quad 2-input multiplexer
10.  Dynamic characteristics
Table 7. Dynamic characteristics
Voltages are referenced to GND (ground = 0 V); CL = 50 pF unless otherwise specified; for test
circuit see Fig. 7.
Tamb = 25  degC Tamb = -40  degC
to +85  degC
Tamb = -40  degC
to +125  degC
Symbol Parameter Conditions
Min Typ Max Min Max Min Max
Unit
74HC157-Q100
nI0, nI1 to nY; see Fig. 5 [1]
VCC = 2.0 V - 36 125 - 155 - 190 ns
VCC = 4.5 V - 13 25 - 31 - 38 ns
VCC = 5 V; CL = 15 pF - 11 - - - - - ns
VCC = 6.0 V - 10 21 - 26 - 32 ns
S to nY; see Fig. 5 [1]
VCC = 2.0 V - 41 125 - 155 - 190 ns
VCC = 4.5 V - 15 25 - 31 - 38 ns
VCC = 5 V; CL = 15 pF - 12 - - - - - ns
VCC = 6.0 V - 12 21 - 26 - 32 ns
E to nY; see Fig. 6 [1]
VCC = 2.0 V - 39 115 - 145 - 175 ns
VCC = 4.5 V - 14 23 - 29 - 35 ns
VCC = 5 V; CL = 15 pF - 11 - - - - - ns
tpd propagation
delay
VCC = 6.0 V - 11 20 - 25 - 30 ns
nY; see Fig. 5 [2]
VCC = 2.0 V - 19 75 - 95 - 110 ns
VCC = 4.5 V - 7 15 - 19 - 22 ns
tt transition
time
VCC = 6.0 V - 6 13 - 16 - 19 ns
CPD power
dissipation
capacitance
CL = 50 pF; f = 1 MHz;
VI = GND to VCC
[3] - 70 - - - - - pF
74HC_HCT157_Q100 All information provided in this document is subject to legal disclaimers. (c)
Nexperia B.V. 2024. All rights reserved
Product data sheet Rev. 4 - 28 May 2024 7 / 15
```

### Page 8

```text
Nexperia 74HC157-Q100; 74HCT157-Q100
Quad 2-input multiplexer
Tamb = 25  degC Tamb = -40  degC
to +85  degC
Tamb = -40  degC
to +125  degC
Symbol Parameter Conditions
Min Typ Max Min Max Min Max
Unit
74HCT157-Q100
nI0, nI1 to nY; see Fig. 5 [1]
VCC = 4.5 V - 16 27 - 34 - 41 ns
VCC = 5 V; CL = 15 pF - 13 - - - - - ns
S to nY; see Fig. 5 [1]
VCC = 4.5 V - 22 37 - 46 - 56 ns
VCC = 5 V; CL = 15 pF - 19 - - - - - ns
E to nY; see Fig. 6 [1]
VCC = 4.5 V - 15 26 - 33 - 39 ns
tpd propagation
delay
VCC = 5 V; CL = 15 pF - 12 - - - - - ns
nY; see Fig. 5 [2]tt transition
time VCC = 4.5 V - 7 15 - 19 - 22 ns
CPD power
dissipation
capacitance
CL = 50 pF; f = 1 MHz;
VI = GND to VCC - 1.5 V
[3] - 70 - - - - - pF
[1] tpd is the same as tPLH and tPHL.
[2] tt is the same as tTHL and tTLH.
[3] CPD is used to determine the dynamic power dissipation (PD in uW).
PD = CPD  x  VCC 2  x  fi  x  N + (CL  x  VCC 2  x  fo) where:
fi = input frequency in MHz;
fo = output frequency in MHz;
CL = output load capacitance in pF;
VCC = supply voltage in V;
N = number of inputs switching;
(CL  x  VCC 2  x  fo) = sum of outputs.
10.1.  Waveforms and test circuit
001aad477
tPLHtPHL
VMVM
90 %
10 %
VM VM
output
nY
input
S, nI0, nI1
VI
GND
VOH
VOL
tTLHtTHL
Measurement points are given in Table 8.
VOL and VOH are typical voltage output levels that occur with the output load.
Fig. 5. Propagation delay input (nI0, nI1, S) to output (nYn)
74HC_HCT157_Q100 All information provided in this document is subject to legal disclaimers. (c)
Nexperia B.V. 2024. All rights reserved
Product data sheet Rev. 4 - 28 May 2024 8 / 15
```

### Page 9

```text
Nexperia 74HC157-Q100; 74HCT157-Q100
Quad 2-input multiplexer
mna485
tPHL tPLH
VM
VME input
nY output
GND
VCC
VOH
VOL
Measurement points are given in Table 8.
VOL and VOH are typical voltage output levels that occur with the output load.
Fig. 6. Propagation delay input (E) to output (nY)
Table 8. Measurement points
Input OutputType
VM VM
74HC157-Q100 0.5VCC 0.5VCC
74HCT157-Q100 1.3 V 1.3 V
001aah768

tW
tW
tr
trtf
VM
VI
negative
pulse
GND
VI
positive
pulse
GND
10 %
90 %
90 %
10 %
VM VM
VM
tf
VCC
DUT
RT
VI VO
CL
G
Test data is given in Table 9.
Definitions test circuit:
RT = Termination resistance should be equal to output impedance Zo of the pulse generator;
CL = Load capacitance including jig and probe capacitance;
RL = Load resistance;
S1 = Test selection switch
Fig. 7. Test circuit for measuring switching times
Table 9. Test data
Input LoadType
VI tr, tf CL
Test
74HC157-Q100 VCC 6.0 ns 15 pF, 50 pF tPLH, tPHL
74HCT157-Q100 3.0 V 6.0 ns 15 pF, 50 pF tPLH, tPHL
74HC_HCT157_Q100 All information provided in this document is subject to legal disclaimers. (c)
Nexperia B.V. 2024. All rights reserved
Product data sheet Rev. 4 - 28 May 2024 9 / 15
```

### Page 10

```text
Nexperia 74HC157-Q100; 74HCT157-Q100
Quad 2-input multiplexer
11.  Package outline
ReferencesOutline
version
European
projection Issue date
IEC JEDEC JEITA
SOT109-1 MS-012
sot109-1_po
03-02-19
23-10-27
Note
1. Plastic or metal protrusions of 0.15 mm (0.006 inch) maximum per side are not included.
SO16: plastic small outline package; 16 leads; body width 3.9 mm SOT109-1
X
w M
q
AA1
A2
bp
D
HE
Lp
detail X
E
e
c
L
v M A
A  3
A
8
9
1
16
y
pin 1 index
0 5 mm
scale
Unit
mm
max
nom
min
1.75 0.25 0.51 0.25 10.0
1.27
A
Dimensions (inch dimensions are derived from the original mm dimensions)
A1 A2 A3 bp c D(1)
8 deg
0 deg
E(1) e HE L
1.05
Lp v
0.2
w y
0.25 0.25 0.1
5.8 0.43.80.10 0.31 0.10 9.81.25
6.2 1.274.0
inches
max
nom
min
0.069 0.010 0.020 0.010 0.394
0.05
8 deg
0 deg
0.041 0.0080.01 0.01 0.004
0.228 0.0160.150.004 0.012 0.004 0.3860.049
0.244 0.050.16
Fig. 8. Package outline SOT109-1 (SO16)
74HC_HCT157_Q100 All information provided in this document is subject to legal disclaimers. (c)
Nexperia B.V. 2024. All rights reserved
Product data sheet Rev. 4 - 28 May 2024 10 / 15
```

### Page 11

```text
Nexperia 74HC157-Q100; 74HCT157-Q100
Quad 2-input multiplexer
ReferencesOutline
version
European
projection Issue date
IEC JEDEC JEITA
SOT403-1
sot403-1_po
03-02-18
23-10-27
Unit
mm
max
nom
min
1.20 0.15 0.30 0.2 5.1
0.65
A
Dimensions (mm are the original dimensions)
Note
1. Plastic or metal protrusions of 0.15 mm maximum per side are not included.
2. Plastic interlead protrusions of 0.25 mm maximum per side are not included.
TSSOP16: plastic thin shrink small outline package; 16 leads; body width 4.4 mm SOT403-1
A1
1.05
bp c
8 deg
0 deg
e HE L
1
Lp v
0.2
w y
0.25 0.1 0.1
6.2 0.454.30.05 0.19 0.09 4.90.80
6.6 0.754.5
0 5 mm
scale
A2 A3
MO-153
w M
bp
D
e
1 8
16 9

AA1
A2
Lp
detail X
L
HE
E
c
v M A
XA
y
pin 1 index
D(1) E(2)
A3
Fig. 9. Package outline SOT403-1 (TSSOP16)
74HC_HCT157_Q100 All information provided in this document is subject to legal disclaimers. (c)
Nexperia B.V. 2024. All rights reserved
Product data sheet Rev. 4 - 28 May 2024 11 / 15
```

### Page 12

```text
Nexperia 74HC157-Q100; 74HCT157-Q100
Quad 2-input multiplexer
terminal 1
index area
0.5 1
A1 Eh b UNIT y e
0.2
c
 REFERENCES OUTLINE
VERSION
EUROPEAN
PROJECTION ISSUE DATE
 IEC  JEDEC  JEITA
mm 3.6
3.4
Dh
2.15
1.85
y1
2.6
2.4
1.15
0.85
e1
2.5 0.30
0.18
0.05
0.00 0.05 0.1
DIMENSIONS (mm are the original dimensions)
 SOT763-1 MO-241 - - - - - -
0.5
0.3
L
0.1
v
0.05
w
0 2.5 5 mm
scale
SOT763-1
DHVQFN16: plastic dual in-line compatible thermal enhanced very thin quad flat package; no leads;
16 terminals; body 2.5 x 3.5 x 0.85 mm
A(1)
max.
A
A1
c
detail X
y y1 C e
L
Eh
Dh
e
e1
b
2 7
15 10
9
8 1
16
X
D
E
C
B A
terminal 1
index area
A C
C
B v M
w M
E (1)
Note
1. Plastic or metal protrusions of 0.075 mm maximum per side are not included.
D (1)
02-10-17
03-01-27

Fig. 10. Package outline SOT763-1 (DHVQFN16)
74HC_HCT157_Q100 All information provided in this document is subject to legal disclaimers. (c)
Nexperia B.V. 2024. All rights reserved
Product data sheet Rev. 4 - 28 May 2024 12 / 15
```

### Page 13

```text
Nexperia 74HC157-Q100; 74HCT157-Q100
Quad 2-input multiplexer
12.  Abbreviations
Table 10. Abbreviations
Acronym Description
ANSI American National Standards Institute
CDM Charged Device Model
CMOS Complementary Metal Oxide Semiconductor
DUT Device Under Test
ESD ElectroStatic Discharge
ESDA ElectroStatic Discharge Association
HBM Human Body Model
JEDEC Joint Electron Device Engineering Council
TTL Transistor-Transistor Logic
13.  Revision history
Table 11. Revision history
Document ID Release date Data sheet status Change notice Supersedes
74HC_HCT157_Q100 v.4 20240528 Product data sheet - 74HC_HCT157_Q100 v.3
Modifications: - Fig. 8, Fig. 9: Aligned SO and TSSOP package outline drawings to JEDEC MS-012 and
MO-153.
- Section 2: ESD specification updated according to the latest JEDEC standard.
74HC_HCT157_Q100 v.3 20200724 Product data sheet - 74HC_HCT157_Q100 v.2
Modifications: - The format of this data sheet has been redesigned to comply with the identity
guidelines of
Nexperia.
- Legal texts have been adapted to the new company name where appropriate.
- Section 1 and Section 2 updated.
- Table 4: Derating values for Ptot total power dissipation have been updated.
74HC_HCT157_Q100 v.2 20150121 Product data sheet - 74HC_HCT157_Q100 v.1
Modifications: - Table 7: Power dissipation capacitance condition for 74HCT157 is corrected.
74HC_HCT157_Q100 v.1 20120802 Product data sheet - -
74HC_HCT157_Q100 All information provided in this document is subject to legal disclaimers. (c)
Nexperia B.V. 2024. All rights reserved
Product data sheet Rev. 4 - 28 May 2024 13 / 15
```

### Page 14

```text
Nexperia 74HC157-Q100; 74HCT157-Q100
Quad 2-input multiplexer
14.  Legal information
Data sheet status
Document status
[1][2]
Product
status [3]
Definition
Objective [short]
data sheet
Development This document contains data from
the objective specification for
product development.
Preliminary [short]
data sheet
Qualification This document contains data from
the preliminary specification.
Product [short]
data sheet
Production This document contains the product
specification.
[1] Please consult the most recently issued document before initiating or
completing a design.
[2] The term 'short data sheet' is explained in section "Definitions".
[3] The product status of device(s) described in this document may have
changed since this document was published and may differ in case of
multiple devices. The latest product status information is available on
the internet at https://www.nexperia.com.
Definitions
Draft - The document is a draft version only. The content is still under
internal review and subject to formal approval, which may result in
modifications or additions. Nexperia does not give any representations or
warranties as to the accuracy or completeness of information included herein
and shall have no liability for the consequences of use of such information.
Short data sheet - A short data sheet is an extract from a full data sheet
with the same product type number(s) and title. A short data sheet is
intended for quick reference only and should not be relied upon to contain
detailed and full information. For detailed and full information see the relevant
full data sheet, which is available on request via the local Nexperia sales
office. In case of any inconsistency or conflict with the short data sheet, the
full data sheet shall prevail.
Product specification - The information and data provided in a Product
data sheet shall define the specification of the product as agreed between
Nexperia and its customer, unless Nexperia and customer have explicitly
agreed otherwise in writing. In no event however, shall an agreement be
valid in which the Nexperia product is deemed to offer functions and qualities
beyond those described in the Product data sheet.
Disclaimers
Limited warranty and liability - Information in this document is believed
to be accurate and reliable. However, Nexperia does not give any
representations or warranties, expressed or implied, as to the accuracy
or completeness of such information and shall have no liability for the
consequences of use of such information. Nexperia takes no responsibility
for the content in this document if provided by an information source outside
of Nexperia.
In no event shall Nexperia be liable for any indirect, incidental, punitive,
special or consequential damages (including - without limitation - lost
profits, lost savings, business interruption, costs related to the removal
or replacement of any products or rework charges) whether or not such
damages are based on tort (including negligence), warranty, breach of
contract or any other legal theory.
Notwithstanding any damages that customer might incur for any reason
whatsoever, Nexperia's aggregate and cumulative liability towards customer
for the products described herein shall be limited in accordance with the
Terms and conditions of commercial sale of Nexperia.
Right to make changes - Nexperia reserves the right to make changes
to information published in this document, including without limitation
specifications and product descriptions, at any time and without notice. This
document supersedes and replaces all information supplied prior to the
publication hereof.
Suitability for use in automotive applications - This Nexperia product
has been qualified for use in automotive applications. Unless otherwise
agreed in writing, the product is not designed, authorized or warranted to
be suitable for use in life support, life-critical or safety-critical systems or
equipment, nor in applications where failure or malfunction of an Nexperia
product can reasonably be expected to result in personal injury, death or
severe property or environmental damage. Nexperia and its suppliers accept
no liability for inclusion and/or use of Nexperia products in such equipment or
applications and therefore such inclusion and/or use is at the customer's own
risk.
Quick reference data - The Quick reference data is an extract of the
product data given in the Limiting values and Characteristics sections of this
document, and as such is not complete, exhaustive or legally binding.
Applications - Applications that are described herein for any of these
products are for illustrative purposes only. Nexperia makes no representation
or warranty that such applications will be suitable for the specified use
without further testing or modification.
Customers are responsible for the design and operation of their applications
and products using Nexperia products, and Nexperia accepts no liability for
any assistance with applications or customer product design. It is customer's
sole responsibility to determine whether the Nexperia product is suitable
and fit for the customer's applications and products planned, as well as
for the planned application and use of customer's third party customer(s).
Customers should provide appropriate design and operating safeguards to
minimize the risks associated with their applications and products.
Nexperia does not accept any liability related to any default, damage, costs
or problem which is based on any weakness or default in the customer's
applications or products, or the application or use by customer's third party
customer(s). Customer is responsible for doing all necessary testing for the
customer's applications and products using Nexperia products in order to
avoid a default of the applications and the products or of the application or
use by customer's third party customer(s). Nexperia does not accept any
liability in this respect.
Limiting values - Stress above one or more limiting values (as defined in
the Absolute Maximum Ratings System of IEC 60134) will cause permanent
damage to the device. Limiting values are stress ratings only and (proper)
operation of the device at these or any other conditions above those
given in the Recommended operating conditions section (if present) or the
Characteristics sections of this document is not warranted. Constant or
repeated exposure to limiting values will permanently and irreversibly affect
the quality and reliability of the device.
Terms and conditions of commercial sale - Nexperia products are
sold subject to the general terms and conditions of commercial sale, as
published at http://www.nexperia.com/profile/terms, unless otherwise agreed
in a valid written individual agreement. In case an individual agreement is
concluded only the terms and conditions of the respective agreement shall
apply. Nexperia hereby expressly objects to applying the customer's general
terms and conditions with regard to the purchase of Nexperia products by
customer.
No offer to sell or license - Nothing in this document may be interpreted
or construed as an offer to sell products that is open for acceptance or the
grant, conveyance or implication of any license under any copyrights, patents
or other industrial or intellectual property rights.
Export control - This document as well as the item(s) described herein
may be subject to export control regulations. Export might require a prior
authorization from competent authorities.
Translations - A non-English (translated) version of a document is for
reference only. The English version shall prevail in case of any discrepancy
between the translated and English versions.
Trademarks
Notice: All referenced brands, product names, service names and
trademarks are the property of their respective owners.
74HC_HCT157_Q100 All information provided in this document is subject to legal disclaimers. (c)
Nexperia B.V. 2024. All rights reserved
Product data sheet Rev. 4 - 28 May 2024 14 / 15
```

### Page 15

```text
Nexperia 74HC157-Q100; 74HCT157-Q100
Quad 2-input multiplexer
Contents
1.  General description......................................................1
2.  Features and benefits .................................................. 1
3.  Ordering information....................................................1
4.  Functional diagram.......................................................2
5.  Pinning information......................................................3
5.1.  Pinning.........................................................................3
5.2.  Pin description.............................................................3
6.  Functional description................................................. 3
7.  Limiting values............................................................. 4
8.  Recommended operating conditions..........................4
9.  Static characteristics....................................................5
10.  Dynamic characteristics............................................ 7
10.1.  Waveforms and test circuit........................................ 8
11.  Package outline........................................................ 10
12.  Abbreviations............................................................13
13.  Revision history........................................................13
14.  Legal information ......................................................14
(c) Nexperia B.V. 2024. All rights reserved
For more information, please visit: http://www.nexperia.com
For sales office addresses, please send an email to: salesaddresses@nexperia.com
Date of release: 28 May 2024
74HC_HCT157_Q100 All information provided in this document is subject to legal disclaimers. (c)
Nexperia B.V. 2024. All rights reserved
Product data sheet Rev. 4 - 28 May 2024 15 / 15
```
