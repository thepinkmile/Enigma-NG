# Document No.: SPC / SK6812MINI

## Source

- **Source PDF:** [Adafruit-4960_SK6812MINI-E_REV02_EN.pdf](Adafruit-4960_SK6812MINI-E_REV02_EN.pdf)
- **Generated Markdown:** `Adafruit-4960_SK6812MINI-E_REV02_EN.md`
- **Page count:** 18
- **Conversion method:** automated local PDF text extraction with pypdf/pdfplumber

## PDF Metadata

| Field | Value |
| :--- | :--- |
| Title |  |
| Author |  |
| Subject |  |
| Creator |  |
| Producer | 福昕PDF打印机 版本 8.3.0.0331 |

## Extracted Technical Index

This markdown datasheet is meant to reduce the need to reopen the PDF during design work.
It preserves design-relevant extracted snippets first, followed by page-by-page text so the source content remains locally searchable.

### Part number and ordering information

- No reliable text snippet was automatically extracted for this category. Review the raw page text below.

### Pin, pad, and connection designations

- 5 / 、 / PIN configuration / .........................................................................4 / 6
- pixels are contained within the intelligent digital interface input. The output is driven by patented PWM / technology, which effectively guarantees high consistency of the color of the pixels. …
- from the controller to DIN of the first element, and if it is accepted it is extracted pixel to pixel. After an / internal data latch, the remaining data is passed through the internal amplifica…
- internal data latch, the remaining data is passed through the internal amplification circuit and sent out / on the DO port to the remaining pixels. The pixel is reset after the end of DIN. Using…
- on the DO port to the remaining pixels. The pixel is reset after the end of DIN. Using automatic / shaping forwarding technology makes the number of cascaded pixels without signal transmission o…
- built / - / in data shaping circuit, a pixel signal is received after wave shaping and output waveform / distortion will not guarantee a line / ;
- / 18 / 5. / PIN configuration / 4. / Mechanical Dimensions
- 2 / DOUT / Control data signal output / 3 / GND
- 4 / DIN / Control data signal input / 6. / Recommended dimensions for PCB
- V / --- / The signal / input flip / threshold
- Timing waveform / : / Connection mode: / Input code: / Name
- 14. / The method of data transmission: / Note: the D1 sends data for MCU, D2, D3, D4 for data forwarding automatic shaping cascade circuit. / Document No.: SPC / SK6812MINI / -
- 16. / The typica l application circuit: / In the practical application circuit, the signal input and output pins of the IC signal input and output pins should be conne / cte / d
- cte / d / to the signal input and output terminals. In addition, in order to make the IC chip is more stable, even the capacitance betw / een / beads is essential back;
- een / beads is essential back; / Application: used for soft lamp strip or hard light, lamp beads transmission distance is short, suggested in signal in time t / he / clock line input and output …
- - / shaped products, lamp beads transmission distance is long, because of different / wire and transmission distance, in the signal in time clock at both ends of the line on grounding protection…
- 100% / 120% / Thermal Pad Temperature (T=25°C) / Normalized Luminous Flux / 120
- The reel pack is applied in SMD LED. The LEDs are packed in cardboard boxes after packaging in normal or anti / - / electrostatic bags. cardboard boxes will be used to protect the LEDs from mech…
- 3.2. Shipment and storage / TOP SMD LED is a humidity sensor, the LED packaging in the aluminum bag is to avoid the LED in the / transport and storage of moisture absorption, in the bag with a d…
- minimal amount of dust and debris on the LED will not cause significant reduction in illumination, steps / should be taken to keep the emitter free of dust. / These include keeping the LEDs in t…

### Specifications, ratings, and operating conditions

- 18 / 02 / Revision of Specification Format / KEVIN ZHU / Change History
- 13 / 、 / Timing waveform / .......................................................................7 / 14
- circuit consists of a signal shaping amplification circuit, a built / - / in constant current circuit, and a high / precision RC oscillator. / The data protocol being used is unipolar
- shaping forwarding technology makes the number of cascaded pixels without signal transmission only / limited by signal transmission speed. / The LED has a low driving voltage (which allows for e…
- Description: / ● / Top SMD internal integrated high quality external control line serial cascade constant current IC; / ● / control circuit and the RGB chip in SMD
- Notes: / 1. All dimensions are in millimeters. / 2. Tolerance is / ± / 0.1mm unless otherwise noted
- IC / series and / current code / package / outline
- Refers to the 68 series / IC / 5/12MA current / version / 3.2x2.8x1.78mm
- Range / Unit / Power supply voltage / VDD / +3.7
- +5.5 / V / Logic input voltage / V / IN
- Test conditions / The chip / supply voltage / VDD / ---
- The data transmission time : / 13. / Timing waveform / : / Connection mode:
- 100% / 120% / Thermal Pad Temperature (T=25°C) / Normalized Luminous Flux / 120
- Criterion / 1 / Thermal / Shock / 100
- ° / C, IF: Typical / current , 1000hrs / JESD22 / -
- IV / DC=5V, Typical / current / Init. / Value\*0.7
- --- / DC=5V, Typical / current / No dead lights or obvious / damage
- - / proof grade materials or packaging to save the time there is a certain difference, the specific preservation time / to the specification book or packaging tips prevail); recommended in the u…
- NG (nozzle diameter is less than the light / beads light area) / Thermal design of the end product is of paramount importance. Please consider the heat generation of the / LED when making the sy…
- Thermal design of the end product is of paramount importance. Please consider the heat generation of the / LED when making the system design. The coefficient of temperature increase per input el…

### Dimensions, package, and mechanical information

- 4 / 、 / Mechanical Dimensions / ...............................................................4 / 5
- 6 / 、 / Recommended dimensions for PCB ...........................................4 / 7 / 、
- PIN configuration / 4. / Mechanical Dimensions / : / Notes:
- : / Notes: / 1. All dimensions are in millimeters. / 2. Tolerance is / ±
- Control data signal input / 6. / Recommended dimensions for PCB / 角 / 1 VDD
- series and / current code / package / outline / The default is to
- current code / package / outline / The default is to / integrate the RGB
- version / 3.2x2.8x1.78mm / package / outline / 8.
- 3.2x2.8x1.78mm / package / outline / 8. / Electrical parameters
- The reel pack is applied in SMD LED. The LEDs are packed in cardboard boxes after packaging in normal or anti / - / electrostatic bags. cardboard boxes will be used to protect the LEDs from mech…
- minimal amount of dust and debris on the LED will not cause significant reduction in illumination, steps / should be taken to keep the emitter free of dust. / These include keeping the LEDs in t…
- Avoid using organic solvent, it is recommended that isopropyl be used as a solvent for cleaning the LEDs. / When using other solvents, it should be confirmed beforehand whether the solvents will…
- determine whether the bag material on / - / line operation; And the material after opening the package should be strictly / controlled in the table 1 as specified by the maximum temperature and …
- by adverse water within the lead; / 3.5. Definition of humidity card / Open the package after the TOP SMD LED bag inside the humidity card color instructions are as follows: / A. If the moisture…
- dehumidified material can be re / - / packaged to re / - / start the calculation time;
- ℃ / oven baking for less than 12 hours, To remove the product in the detection and aging process exposed to / moisture in the air to avoid the product in the protective treatment, the package in…
- <6 minutes max. / <6 minutes max. / Note: All temperatures refer to topside of the package, measured on the package body surface. / Document No.: SPC / SK6812MINI / ->
- 18 / / 18 / 4.1 Moisture Proof Package / 4.0 Electrostatic Discharge & Surge Current : / Electrostatic discharge (ESD) or surge current (EOS)

### Formulas, equations, and configurable calculations

- 5 / 、 / PIN configuration / .........................................................................4 / 6
- / 18 / 5. / PIN configuration / 4. / Mechanical Dimensions
- --- / KHZ / The duty ratio of 67% / (data 1) / DOUT transmission
- ° / C / 60% RH; / (Note: The label date is the same and the packing is not leaked. Discoloration under the premise of use; for different / moisture / -
- determine whether the bag material on / - / line operation; And the material after opening the package should be strictly / controlled in the table 1 as specified by the maximum temperature and …
- Note that this general guideline is offered as a starting point and may require adjustment for certain PCB designs an / d / Configurations of reflow soldering equipment. / Temperature (°C) / Tim…
- NG (nozzle diameter is less than the light / beads light area) / Thermal design of the end product is of paramount importance. Please consider the heat generation of the / LED when making the sy…
- LED when making the system design. The coefficient of temperature increase per input electric power is / affected by the thermal resistance of the circuit board and density of LED placement on t…
- C, refers to the product / pin at the operating temperature) / 3.9 Heat Generation: / Document No.: SPC / SK6812MINI / -

### Reference designs, applications, and examples

- 2 / 、 / Main Application Field / ...............................................................3 / 3
- 16 / 、 / The typica l application circuit / ....................................................9 / 17
- Appendix 1 / 、 / TOP SMD LED Application Notes...............................13~18 / Document No.: SPC / SK6812MINI / -
- integrated in the LED above. / 2. / Main Application Field / : / ●
- ...... ..B0) / 16. / The typica l application circuit: / In the practical application circuit, the signal input and output pins of the IC signal input and output pins should be conne / cte
- 16. / The typica l application circuit: / In the practical application circuit, the signal input and output pins of the IC signal input and output pins should be conne / cte / d
- een / beads is essential back; / Application: used for soft lamp strip or hard light, lamp beads transmission distance is short, suggested in signal in time t / he / clock line input and output …
- he / clock line input and output end of each connected in series protection resistors, R1=R0 of about 500 ohms. / Application: for module or general special / - / shaped products, lamp beads tra…
- Appendix 1 / 、 / TOP SMD LED Application Notes / 1 / .

## Page-by-Page Extracted Content

### Page 1

```text
Document No.: SPC / SK6812MINI
-
E Rev. No.: 02
Factory :
Lianxing industrial park
,
xiajie
village
,
Qishi
Town, Dongguan City.
guangdong province, China
Dongguan Tel: (769)82632725
Dongguan Fax: (769)82632735
东莞市欧思科光电科技有限公司
DONGGUAN OPSCO OPTOELECTRONICS CO., LTD
1
/ 18
 ELECTROSTATIC
SENSITIVE DEVICES
SK6812MINI
-
E
3.2x2.8x1.78 mm 0.2W
Intelligent external
control surface mount SMD LED (MSL:5a)
Date
Rev. No.
Changes/Reason of changes
Signature
2017
-
08
-
04
01
Initial
Document
KEVIN ZHU
2019
-
01
-
18
02
Revision of Specification Format
KEVIN ZHU
Change History
```

### Page 2

```text
Document No.: SPC / SK6812MINI
-
E Rev. No.: 02
Factory :
Lianxing industrial park
,
xiajie
village
,
Qishi
Town, Dongguan City.
guangdong province, China
Dongguan Tel: (769)82632725
Dongguan Fax: (769)82632735
东莞市欧思科光电科技有限公司
DONGGUAN OPSCO OPTOELECTRONICS CO., LTD
2
/ 18
CONTENTS
1
、
Product overview........................................................................3
2
、
Main Application Field
...............................................................3
3
、
Description
...................................................................................3
4
、
Mechanical Dimensions
...............................................................4
5
、
PIN configuration
.........................................................................4
6
、
Recommended dimensions for PCB ...........................................4
7
、
General description of product naming.......
.................................5
8
、
Electrical parameters....................................................................5
9
、
Electrical/Optical Characteristics
.................................................5
10
、
IC
The electrical parameters
......................................................6
11
、
Switching characteristics
............................................................6
12
、
The data transmission time
........................................................7
13
、
Timing waveform
.......................................................................7
14
、
The method of data transmission
................................................8
15
、
The data structure of 24bit
.......................................................... 9
16
、
The typica l application circuit
....................................................9
17
、
Standard LED Performance Graph..............................................10
18
、
Packaging Standard......................................................................11
19
、
Reliability Test..............................................................................12
Appendix 1
、
TOP SMD LED Application Notes...............................13~18
```

### Page 3

```text
Document No.: SPC / SK6812MINI
-
E Rev. No.: 02
Factory :
Lianxing industrial park
,
xiajie
village
,
Qishi
Town, Dongguan City.
guangdong province, China
Dongguan Tel: (769)82632725
Dongguan Fax: (769)82632735
东莞市欧思科光电科技有限公司
DONGGUAN OPSCO OPTOELECTRONICS CO., LTD
3
/ 18
1.
Product
O
verview
:
SK6812MINI
-
E
is a smart LED control circuit and light emitting circuit in one controlled LED source,
which has the shape of a
3528
LED chip. Each lighting element is a pixel, and the intensities of the
pixels are contained within the intelligent digital interface input. The output is driven by patented PWM
technology, which effectively guarantees high consistency of the color of the pixels. The control
circuit consists of a signal shaping amplification circuit, a built
-
in constant current circuit, and a high
precision RC oscillator.
The data protocol being used is unipolar
RZ
communication mode. The 24
-
bit data is transmitted
from the controller to DIN of the first element, and if it is accepted it is extracted pixel to pixel. After an
internal data latch, the remaining data is passed through the internal amplification circuit and sent out
on the DO port to the remaining pixels. The pixel is reset after the end of DIN. Using automatic
shaping forwarding technology makes the number of cascaded pixels without signal transmission only
limited by signal transmission speed.
The LED has a low driving voltage (which allows for environmental protection and energy saving),
high brightness, scattering angle, good consistency, low power, and long life. The control circuit is
integrated in the LED above.
2.
Main Application Field
:
●
Full color LED string light, LED full color module, LED super hard and soft lights, LED guardrail tube,
LED appearance / scene lighting
●
LED point light, LED pixel screen, LED shaped screen, a variety of electronic products, electrical
equipment etc..
3.
Description:
●
Top SMD internal integrated high quality external control line serial cascade constant current IC;
●
control circuit and the RGB chip in SMD
3528
components, to form a complete control of pixel, color
mixing uniformity and consistency
;
●
built
-
in data shaping circuit, a pixel signal is received after wave shaping and output waveform
distortion will not guarantee a line
;
●
The built
-
in power on reset and reset circuit, the power does not work;
●
gray level adjusting circuit (256 level gray scale adjustable)
;
●
red drive special treatment, color balance;
●
line data transmission;
●
plastic forward strengthening technology, the transmission distance between two points over 10M
;
●
Using a typical data transmission frequency of 800 Kbps
, when the refresh rate of 30 frames per sec
```

### Page 4

```text
Document No.: SPC / SK6812MINI
-
E Rev. No.: 02
Factory :
Lianxing industrial park
,
xiajie
village
,
Qishi
Town, Dongguan City.
guangdong province, China
Dongguan Tel: (769)82632725
Dongguan Fax: (769)82632735
东莞市欧思科光电科技有限公司
DONGGUAN OPSCO OPTOELECTRONICS CO., LTD
4
/ 18
5.
PIN configuration
4.
Mechanical Dimensions
:
Notes:
1. All dimensions are in millimeters.
2. Tolerance is
±
0.1mm unless otherwise noted
NO.
Symbol
Function description
1
VDD
Power supply LED
2
DOUT
Control data signal output
3
GND
Ground
4
DIN
Control data signal input
6.
Recommended dimensions for PCB
角
1 VDD
2 DOUT
4 DIN
3 GND
2 DOUT
4 DIN
3 GND
1 VDD
```

### Page 5

```text
Document No.: SPC / SK6812MINI
-
E Rev. No.: 02
Factory :
Lianxing industrial park
,
xiajie
village
,
Qishi
Town, Dongguan City.
guangdong province, China
Dongguan Tel: (769)82632725
Dongguan Fax: (769)82632735
东莞市欧思科光电科技有限公司
DONGGUAN OPSCO OPTOELECTRONICS CO., LTD
5
/ 18
7.
General description of product naming
①
②
③
SK
6812
MINI
-
E
①
②
③
Series
IC
series and
current code
package
outline
The default is to
integrate the RGB
chip with the IC in
the
Refers to the 68 series
IC
5/12MA current
version
3.2x2.8x1.78mm
package
outline
8.
Electrical parameters
（
Ta=25℃,VSS=0V
）
:
Parameter
Symbol
Range
Unit
Power supply voltage
VDD
+3.7
～
+5.5
V
Logic input voltage
V
IN
-
0.5
～
VDD+0.5
V
Working temperature
Topt
-
40~+85
℃
Storage temperature
Tstg
-
50~+150
℃
ES
D
pressure
(HBM)
V
ESD
4K
V
ES
D
pressure
(DM)
V
ESD
200
V
Color
SK6805MINI
-
E
5mA
SK6812MINI
-
E
12mA
Dominate
Waveleng
th(nm)
Luminance(
mcd)
luminous
flux(lm)
Dominate
Waveleng
th(nm)
Luminanc
e(mcd)
luminous
flux(lm)
红色
（
RED)
620
-
630
100
-
200
0.5
-
1.0
620
-
625
400
-
700
1.0
-
2.0
绿色
（
GREEN)
520
-
535
400
-
700
2.0
-
3.0
520
-
530
1000
-
1500
3.0
-
4.0
蓝色
（
BLUE)
460
-
475
50
-
100
0.1
-
0.5
460
-
470
200
-
400
0.5
-
1.0
9.
Electrical/Optical Characteristics
:
```

### Page 6

```text
Document No.: SPC / SK6812MINI
-
E Rev. No.: 02
Factory :
Lianxing industrial park
,
xiajie
village
,
Qishi
Town, Dongguan City.
guangdong province, China
Dongguan Tel: (769)82632725
Dongguan Fax: (769)82632735
东莞市欧思科光电科技有限公司
DONGGUAN OPSCO OPTOELECTRONICS CO., LTD
6
/ 18
10.
The
IC
electrical parameters (
unless otherwise specified
, TA=
-
20 ~ +70 ℃, VDD=4.5 ~
5.5V, VSS=0V):
Parmeter
Symb
ol
Min
Typic
al
Max
Unit
Test conditions
The chip
supply voltage
VDD
---
5.2
---
V
---
The signal
input flip
threshold
VIH
0.7*VDD
---
---
V
VDD=5.0V
VIL
---
---
0.3*VDD
V
The frequency
of PWM
FPWM
---
1.2
---
KHZ
---
Static power
consumption
IDD
---
1
---
mA
---
11.
Switching characteristics
(
VCC=5V
Ta=25 ℃):
Parameter
Symbol
Min
Typical
Max
Unit
Test conditions
The speed of data
transmission
fDIN
---
800
---
KHZ
The duty ratio of 67%
(data 1)
DOUT transmission
delay
TPLH
---
---
500
ns
DIN→DOUT
TPHL
---
---
500
ns
I
OUT
Rise/Drop
Time
Tr
---
100
---
ns
VDS=1.5
IOUT=13mA
Tf
---
100
---
ns
```

### Page 7

```text
Document No.: SPC / SK6812MINI
-
E Rev. No.: 02
Factory :
Lianxing industrial park
,
xiajie
village
,
Qishi
Town, Dongguan City.
guangdong province, China
Dongguan Tel: (769)82632725
Dongguan Fax: (769)82632735
东莞市欧思科光电科技有限公司
DONGGUAN OPSCO OPTOELECTRONICS CO., LTD
7
/18
12.
The data transmission time :
13.
Timing waveform
:
Connection mode:
Input code:
Name
Min.
Standard
value
Max.
Unit
T
Code period
1.20
--
--
µs
T0H
0
code
, high level time
0.2
0.32
0.4
µs
T0L
0
code
,
low
level time
0.8
--
--
µs
T1H
1 code
, high level time
0.58
0.64
1.0
µs
T1L
1 code
,
low
level time
0.2
--
--
µs
Trst
Reset
code
，
low level
time
>80
--
--
µs
1. The protocol uses a unipolar zeroing code. Each symbol must have a low level. Each
symbol in this protocol starts with a high level. The high time width determines the "0" or
"1" code. .
2. When writing programs, the minimum symbol period is 1.2μs.
3. The high time of
“
0
”
code and
“
1
”
code should be in accordance with the
stipulated range in the above table. The low time requirement of
“
0
”
code and
“
1
”
code is less than 20μs.
DIN
DIN
DIN
DO
DO
DO
PIX1
D1
D2
D3
D4
PIX2
PIX3
Symbol period
T1H
T1L
T0L
T0H
T
Trst
0 code
1 code
Reset code
```

### Page 8

```text
Document No.: SPC / SK6812MINI
-
E Rev. No.: 02
Factory :
Lianxing industrial park
,
xiajie
village
,
Qishi
Town, Dongguan City.
guangdong province, China
Dongguan Tel: (769)82632725
Dongguan Fax: (769)82632735
东莞市欧思科光电科技有限公司
DONGGUAN OPSCO OPTOELECTRONICS CO., LTD
8
/ 18
14.
The method of data transmission:
Note: the D1 sends data for MCU, D2, D3, D4 for data forwarding automatic shaping cascade circuit.
```

### Page 9

```text
Document No.: SPC / SK6812MINI
-
E Rev. No.: 02
Factory :
Lianxing industrial park
,
xiajie
village
,
Qishi
Town, Dongguan City.
guangdong province, China
Dongguan Tel: (769)82632725
Dongguan Fax: (769)82632735
东莞市欧思科光电科技有限公司
DONGGUAN OPSCO OPTOELECTRONICS CO., LTD
9
/ 18
15.
The data structure of 24bit:
G7
G6
G5
G4
G3
G2
G1
G0
R7
R6
R5
R4
R3
R2
R1
R0
B7
B6
B5
B4
B3
B2
B1
B0
Note: high starting, in order to send data (G7
-
G6
-
...... ..B0)
16.
The typica l application circuit:
In the practical application circuit, the signal input and output pins of the IC signal input and output pins should be conne
cte
d
to the signal input and output terminals. In addition, in order to make the IC chip is more stable, even the capacitance betw
een
beads is essential back;
Application: used for soft lamp strip or hard light, lamp beads transmission distance is short, suggested in signal in time t
he
clock line input and output end of each connected in series protection resistors, R1=R0 of about 500 ohms.
Application: for module or general special
-
shaped products, lamp beads transmission distance is long, because of different
wire and transmission distance, in the signal in time clock at both ends of the line on grounding protection resistance will
be
slightly different; to the actual use of fixed;
```

### Page 10

```text
Document No.: SPC / SK6812MINI
-
E Rev. No.: 02
Factory :
Lianxing industrial park
,
xiajie
village
,
Qishi
Town, Dongguan City.
guangdong province, China
Dongguan Tel: (769)82632725
Dongguan Fax: (769)82632735
东莞市欧思科光电科技有限公司
DONGGUAN OPSCO OPTOELECTRONICS CO., LTD
10
/ 18
17.
Standard LED Performance Graph:
20
0
40
60
80
100
20%
0.00
40%
60%
80%
100%
120%
Thermal Pad Temperature (T=25°C)
Normalized Luminous Flux
120
450
400
500
550
600
650
20%
0.00
40%
60%
80%
100%
W avelength (nm )
Relative Emission Distribution
W avelength Characteristics
700
750
800
75
90
60
45
30
15
0
0.4
0.2
0.6
0.8
1.0
0
30°
60°
90°
Typical Radiation Pattern 120°
Radiation Angle
RED
GREEN
BLUE
BLUE/
GREEN
RED
```

### Page 11

```text
Document No.: SPC / SK6812MINI
-
E Rev. No.: 02
Factory :
Lianxing industrial park
,
xiajie
village
,
Qishi
Town, Dongguan City.
guangdong province, China
Dongguan Tel: (769)82632725
Dongguan Fax: (769)82632735
东莞市欧思科光电科技有限公司
DONGGUAN OPSCO OPTOELECTRONICS CO., LTD
11
/ 18
18
.
Packaging Standard:
The reel pack is applied in SMD LED. The LEDs are packed in cardboard boxes after packaging in normal or anti
-
electrostatic bags. cardboard boxes will be used to protect the LEDs from mechanical shocks during transportation. The
boxes are not water resistant and therefore must be kept away from water and moisture.
C A T H O D E ID E N T IF IC A T IO N
C O V E R T A P E
C A R R IE R T A P E
R E E L (1 7 8x 1 2 m m )
E S D P O L Y E T H Y L E N E B A G
T A P E F E E D D IR E C T IO N
L A B E L S K E T C H IN G

S M D
P R O D U C T N O .: S K 68 12 M IN I
Q U A N T IT Y .: 15 00 P C S
L o t N o .: L W 2 0 1 5 07 090 2-10
 D A T E :2 0 16-0 8-23
C A R D B O A R D (IN N E R 4 C A R D B O A R D M A X .)
 S K 6 8 1 2 M IN I
(IN N E R 1 5 0 0 p cs L E D M A X )
C A R D B O A R D (IN N E R 1 0 B A G M A X .)
```

### Page 12

```text
Document No.: SPC / SK6812MINI
-
E Rev. No.: 02
Factory :
Lianxing industrial park
,
xiajie
village
,
Qishi
Town, Dongguan City.
guangdong province, China
Dongguan Tel: (769)82632725
Dongguan Fax: (769)82632735
东莞市欧思科光电科技有限公司
DONGGUAN OPSCO OPTOELECTRONICS CO., LTD
12
/18
19
.
Reliability Test :
NO.
Test item
Test Conditions
Reference
Criterion
1
Thermal
Shock
100
±
5
°
C ~
-
40
°
C
±
5
°
C
30min~30min 300 cycles
MIL
-
STD
-
202G
0/22
2
High Temperature
Storage
Ta= +100
ºC 1000hrs
JEITA ED
-
4701
200 201
0/22
3
Low Temperature
Storage
Ta=
-
40
ºC 1000hrs
JEITA ED
-
4701
200 202
0/22
4
High Temperature
High Humidity
Storage
Ta=60
ºC RH=90%
1000hrs
JEITA ED
-
4701
100 103
0/22
5
Temperature
Cycle
-
55
ºC
~25
ºC
~100
ºC
~25
ºC
30min~5min~30min~5mi
n
100
cycles
JEITA ED
-
4701
100 105
0/22
6
Resistance to
Soldering Heat
Tsld
= 260
°
C, 10sec. 3
times
JEITA ED
-
4701
300 301
0/22
7
Room
temp Life
Test
25
°
C, IF: Typical
current , 1000hrs
JESD22
-
A
108D
0/22
Criteria for Judging the Damage:
Item
Symbol
Test Condition
Limit
Min
Max
Luminous
Intensity
IV
DC=5V, Typical
current
Init.
Value*0.7
---
Resistance to
Soldering Heat
---
DC=5V, Typical
current
No dead lights or obvious
damage
```

### Page 13

```text
Document No.: SPC / SK6812MINI
-
E Rev. No.: 02
Factory :
Lianxing industrial park
,
xiajie
village
,
Qishi
Town, Dongguan City.
guangdong province, China
Dongguan Tel: (769)82632725
Dongguan Fax: (769)82632735
东莞市欧思科光电科技有限公司
DONGGUAN OPSCO OPTOELECTRONICS CO., LTD
13
/ 18
Appendix 1
、
TOP SMD LED Application Notes
1
.
Features
The
Purposes of making OPSCO’s customers and users to have a clear understanding on the ways how to
use the LED
.
2
.
Description
Generally. The LED can be used the same way as other general purposed semiconductors. When using
OPSCO’s TOP SMD LED, the following precautions must be taken to protect the LED.
3
.
Cautions
3.1. Dust & Cleaning
3.2. Shipment and storage
TOP SMD LED is a humidity sensor, the LED packaging in the aluminum bag is to avoid the LED in the
transport and storage of moisture absorption, in the bag with a desiccant to absorb the moisture inside
the bag. If the LED absorbs water vapor, then in the LED over reflow, in the high temperature state, into
which the rapid expansion of gas vaporization and produce a greater internal stress, so that the material
crack, layered or damaged bonding wire , Resulting in product failure.
TOP SMD LED with a moisture
-
proof anti
-
static aluminum foil bag packaging, handling should avoid the
process of squeezing, piercing the case of bags, and do the necessary anti
-
static protective measures;
promise products on the line before the leak or broken, Please stop the use of direct use of the product; ,
Resulting in product failure;
Such as before the material has been found to prevent moisture
-
proof aluminum foil bags have been
opened, damaged, perforated can be returned to the original re
-
dehumidification, must not be on
-
line use;
The humidity level of this product is LEVEL5a.
This emitter has a silicone surface, There are many benefits to the silicone surface in terms of optical
properties and improved reliability. However, silicone is a softer material and prone to attract dust. While a
minimal amount of dust and debris on the LED will not cause significant reduction in illumination, steps
should be taken to keep the emitter free of dust.
These include keeping the LEDs in the manufacturer’s package prior to assembly and storing assemblies in
an enclosed area after installing the emitters.
Surface condition of this device may change when organic solvents such as trichloroethylene or acetone
were applied.
Avoid using organic solvent, it is recommended that isopropyl be used as a solvent for cleaning the LEDs.
When using other solvents, it should be confirmed beforehand whether the solvents will dissolve the
package and the resin of not.
Do not clean the LEDs by the ultrasonic. When it is absolutely necessary, the influence as ultrasonic
cleaning on the LEDs depends on factors such as ultrasonic power. Baking time and assembled condition.
Before cleaning, a pre
-
test should be done to confirm whether any damage to the LEDs will occur.
```

### Page 14

```text
Document No.: SPC / SK6812MINI
-
E Rev. No.: 02
Factory :
Lianxing industrial park
,
xiajie
village
,
Qishi
Town, Dongguan City.
guangdong province, China
Dongguan Tel: (769)82632725
Dongguan Fax: (769)82632735
东莞市欧思科光电科技有限公司
DONGGUAN OPSCO OPTOELECTRONICS CO., LTD
14
/ 18
3.3. Storage before unsealing
In order to avoid the moisture barrier caused by the reliability of the failure problem, need to do LED products SMT
pre
-
storage and moisture
-
proof measures;
If the moisture
-
proof bag is not open, the TOP SMD element will be stored for less than 2 months at <30
°
C / 60% RH;
(Note: The label date is the same and the packing is not leaked. Discoloration under the premise of use; for different
moisture
-
proof grade materials or packaging to save the time there is a certain difference, the specific preservation time
to the specification book or packaging tips prevail); recommended in the unassembled do not open the moisture before
the bag;
Moisture proof
Workshop lifespan after open the packaging
Time
condition
LEVEL1
unlimited
≦
30
℃
/85 % RH
LEVEL2
1 year
≦
30
℃
/60 % RH
LEVEL2a
4
Weeks
≦
30
℃
/60 % RH
LEVEL3
168
Hours
≦
30
℃
/60 % RH
LEVEL4
72
Hours
≦
30
℃
/60 % RH
LEVEL5
48
Hours
≦
30
℃
/60 % RH
LEVEL5a
24
Hours
≦
30
℃
/60 % RH
LEVEL6
Take
off and use immediately
≦
30
℃
/60 % RH
Chart 1:Definition of material’s MSL prescribed by IPC/JEDECJ
-
STD
-
020E
3.4. Control after the packing bag is opened
After opening the moisture
-
proof bag, please read the moisture
-
proof bag inside the humidity indicator card in the
moisture
-
proof beads into pink to confirm moisture in the moisture bag is too much, according to the color of the ball to
determine whether the bag material on
-
line operation; And the material after opening the package should be strictly
controlled in the table 1 as specified by the maximum temperature and humidity and operating time allowed, as long as
the material exposed in the environment described in Table 1, the need to accumulate its use in the workshop time.
Open the bag and paste the material on the PCB board, should be completed within 0.5H welding work, do not
recommend the material attached to the PCB, a long time stay in the workshop does not carry out SMT work; Caused
by adverse water within the lead;
3.5. Definition of humidity card
Open the package after the TOP SMD LED bag inside the humidity card color instructions are as follows:
A. If the moisture card 10% of the moisture
-
proof beads into pink, other files for the blue, this situation, LED can b
e used
directly;
B. If the humidity card moisture
-
proof beads 10%, 20% at all become pink, in fact, the file is blue, this situation, t
he need
for low
-
temperature components dehumidification;
C. If the humidity card moisture
-
proof beads 10%, 20%, 30% more than three are turned pink, in this case, the customer
needs to return the material to our company for high humidity dehumidification, re
-
packaging before use;
```

### Page 15

```text
Document No.: SPC / SK6812MINI
-
E Rev. No.: 02
Factory :
Lianxing industrial park
,
xiajie
village
,
Qishi
Town, Dongguan City.
guangdong province, China
Dongguan Tel: (769)82632725
Dongguan Fax: (769)82632735
东莞市欧思科光电科技有限公司
DONGGUAN OPSCO OPTOELECTRONICS CO., LTD
15
/18
3.6. Unwanted material moisture
-
proof storage and moisture
-
proof control of finished material
Humidity indicator DO not change color
Humidity indicator tums pink in 10% 20%
Humidity indicator tums pink in 10% 20% 30%
If a roll of SMDs is not used at once and the plant temperature and humidity are within the defined conditions (<30
°
C /
60% RH), the exposure time of the element in the air does not exceed 2H, the remaining material should be carried
out together with the desiccant Vacuum sealed, otherwise, the material must be low
-
wet baking dehumidification;
dehumidified material can be re
-
packaged to re
-
start the calculation time;
Perform moisture control on SMDs components that have been assembled
A. After the components have been assembled to the PCB board no longer need to go through the high temperature
process or reflow process, it will not be special treatment;
B. Do not need to do the necessary dehumidification work before making the appropriate protection process, bake in 70
℃
±
5
℃
oven baking for less than 12 hours, To remove the product in the detection and aging process exposed to
moisture in the air to avoid the product in the protective treatment, the package in the material surface of the moisture
will slowly invade the product, will cause product failure;
C. For products that require secondary SMT process or high temperature, they should be subjected to the necessary
moisture treatment before secondary welding, after exposure to (<30
°
C / 60% RH) , The maximum length of not more
than 2H, Connaught second high temperature process separated by a long time, then a welding material must be
necessary dehumidification work (70
℃
±
5
℃
oven baking no less than 12 hours), and then pumping Vacuum storage;
or the first product stored in the oven or with a desiccant container, the second high
-
temperature process before doing
dehumidification work (70
℃
±
5
℃
in the oven baking no less than 12 hours) , To ensure that products in the high
temperature before the process is not damp;
Low
-
temperature baking conditions: 70
°
C
±
5
°
C baking not less than 12 hours high temperature baking conditions:
130
°
C
±
5
°
C baking not less than 6 hours (lamp beads must be split into particles)
```

### Page 16

```text
Document No.: SPC / SK6812MINI
-
E Rev. No.: 02
Factory :
Lianxing industrial park
,
xiajie
village
,
Qishi
Town, Dongguan City.
guangdong province, China
Dongguan Tel: (769)82632725
Dongguan Fax: (769)82632735
东莞市欧思科光电科技有限公司
DONGGUAN OPSCO OPTOELECTRONICS CO., LTD
16
/ 18
3.7
. Reflow Soldering
Characteristics
In testing, OPSCO has found S35 LEDs to be compatible with JEDEC J
-
STD
-
020W,using the parameters listed below. As a
general guideline OPSCO recommends that users follow the recommended soldering profile provided by the manufacturer
of solder paste used.
Note that this general guideline is offered as a starting point and may require adjustment for certain PCB designs an
d
Configurations of reflow soldering equipment.
Temperature (°C)
Times

 ts
(Preheat)
L
L
s
max
MIN
T 25°C to Peak
amp-up
C
ritical Zone

T
L to
T
P

Ramp down
Profile Feature
Lead
-
Based Solder
Lead
-
Free Solder
Average Ramp
-
Up Rate (Ts
max
to Tp )
3
℃
/second max.
3
℃
/second max.
Preheat: Temperature Min (Ts
min
)
100
℃
150
℃
Preheat: Temperature Min (Ts
max
)
150
℃
200
℃
Preheat: Time ( ts
min to
ts
max
)
60
-
120 seconds
60
-
180 seconds
Time Maintained Above: Temperature (T
L
)
183
℃
217
℃
Time Maintained Above: Time (t
L
)
60
-
150 seconds
60
-
150 seconds
Peak/Classification Temperature (T
P
)
215
℃
240
℃
Time Within 5
℃
of Actual Peak Temperature (
tp
)
<10 seconds
<10 seconds
Ramp
-
Down Rate
6
℃
/second max.
6
℃
/second max.
Time 25
℃
to Peak Temperature
<6 minutes max.
<6 minutes max.
Note: All temperatures refer to topside of the package, measured on the package body surface.
```

### Page 17

```text
Document No.: SPC / SK6812MINI
-
E Rev. No.: 02
Factory :
Lianxing industrial park
,
xiajie
village
,
Qishi
Town, Dongguan City.
guangdong province, China
Dongguan Tel: (769)82632725
Dongguan Fax: (769)82632735
东莞市欧思科光电科技有限公司
DONGGUAN OPSCO OPTOELECTRONICS CO., LTD
17
/18
3.8 General design requirements :
. SMT nozzle requirements: (red circle refers to the nozzle diameter)
. Material to take way: with tweezers folder material, can not press the colloid or sharp objects to
touch the colloid, the material can not be stacked;
. Products in the PCB layout design, for the soft sheet, and 0.5T below the plate, the pad direction
should be perpendicular to the direction of PCB extension to reduce the PCB board bending stress
generated in the LED pin, resulting in LED products Due to stress acting tensile failure;
OK (nozzle diameter is greater than the
light bulb area
NG (nozzle diameter is less than the light
beads light area)
Thermal design of the end product is of paramount importance. Please consider the heat generation of the
LED when making the system design. The coefficient of temperature increase per input electric power is
affected by the thermal resistance of the circuit board and density of LED placement on the board, as well as
components. It is necessary to avoid in tense heat generation and operate within the maximum rating given in
this specification. The operating current should be decided after considering the ambient maximum
temperature of LEDs
The maximum working temperature of the product is not easy to exceed 40
°
C ( ≤ 40
°
C, refers to the product
pin at the operating temperature)
3.9 Heat Generation:
```

### Page 18

```text
Document No.: SPC / SK6812MINI
-
E Rev. No.: 02
Factory :
Lianxing industrial park
,
xiajie
village
,
Qishi
Town, Dongguan City.
guangdong province, China
Dongguan Tel: (769)82632725
Dongguan Fax: (769)82632735
东莞市欧思科光电科技有限公司
DONGGUAN OPSCO OPTOELECTRONICS CO., LTD
18
/ 18
4.1 Moisture Proof Package
4.0 Electrostatic Discharge & Surge Current :
Electrostatic discharge (ESD) or surge current (EOS)
may damage LED.
Precautions such as ESD wrist strap, ESD shoe strap or antistatic gloves must be worn whenever handling of
LED.
IC device signal input and output ports must be connected in series protection resistor to prevent surge or
static shock port caused by product failure;
All devices, equipment and machinery must be properly grounded.
It is recommended to perform electrical test to screen out ESD failures at final inspection.
It is important to eliminate the possibility of surge current during circuitry design.
Cannot take any responsibility for any trouble that are caused by using the LEDs at conditions exceeding
our specifications.
The LED light output is strong enough to injure human eyes. Precautions must be taken to prevent looking
directly at the LEDs with unaided eyes for more than a few seconds.
The formal specification must be exchanged and signed by both parties before large volume purchase begins.
The appearance and specifications of the product may be modified for improvement without notice.
```
