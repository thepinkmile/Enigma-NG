# LTC3350 - High Current Supercapacitor Backup Controller and System Monitor

## Source Reference

- Source PDF: [ltc3350-datasheet.pdf](ltc3350-datasheet.pdf)
- Source path: `design\Datasheets\ltc3350-datasheet.pdf`
- Generated markdown: `ltc3350-datasheet.md`
- Page count: 46
- Extracted text characters: 124476
- Empty extraction pages: none
- Conversion method: automated local PDF text extraction with pypdf and pdfplumber

## Title and Part Identity

- Extracted title: LTC3350 - High Current Supercapacitor Backup Controller and System Monitor
- File stem / likely part identity: `ltc3350-datasheet`
- PDF metadata title: LTC3350 (Rev. D)
- PDF metadata subject: High Current Supercapacitor Backup Controller and System Monitor
- Identity clue: LTC3350
- Identity clue: Rev. DFor more information www.analog.com
- Identity clue: Document Feedback
- Identity clue: TYPICAL APPLICATION
- Identity clue: FEATURES DESCRIPTION
- Identity clue: High Current Supercapacitor Backup
- Identity clue: Controller and System Monitor
- Identity clue: The LT C(R)3350 is a backup power controller that can charge

## PDF Metadata

| Field | Value |
|:---|:---|
| Title | LTC3350 (Rev. D) |
| Author | Analog Devices, Inc. |
| Subject | High Current Supercapacitor Backup Controller and System Monitor |
| Creator | Adobe InDesign 16.3 (Macintosh) |
| Producer | Adobe PDF Library 15.0 |

## Design-Relevant Extracted Content

These sections collect extracted snippets that are likely useful during design work, then the raw page-by-page text is preserved below for local search.

### Part number and ordering information

- Page 3: 12 / ORDER INFORMATION / LEAD FREE FINISH TAPE AND REEL PART MARKING* PACKAGE DESCRIPTION
  TEMPERATURE RANGE / LTC3350EUHF#PBF LTC3350EUHF#TRPBF 3350 38-Lead (5mm  x  7mm) Plastic QFN -40
  degC to 125 degC / LTC3350IUHF#PBF LTC3350IUHF#TRPBF 3350 38-Lead (5mm  x  7mm) Plastic QFN -40
  degC to 125 degC
- Page 3: LTC3350IUHF#WPBF LTC3350IUHF#WTRPBF 3350 38-Lead (5mm  x  7mm) Plastic QFN -40 degC to 125
  degC / Contact the factory for parts specified with wider operating temperature ranges. *The
  temperature grade is identified by a label on the shipping container . / Tape and reel
  specifications. Some packages are available in 500 unit reels through designated sales channels
  with #TRMPBF suffix. / **Versions of this part are available with controlled manufacturing to
  support the quality and reliability requirements of automotive applications. These / models are
  designated with a #W suffix. Only the automotive grade products shown are available for use in
  automotive applications. Contact your
- Page 3: Tape and reel specifications. Some packages are available in 500 unit reels through
  designated sales channels with #TRMPBF suffix. / **Versions of this part are available with
  controlled manufacturing to support the quality and reliability requirements of automotive
  applications. These / models are designated with a #W suffix. Only the automotive grade products
  shown are available for use in automotive applications. Contact your / local Analog Devices
  account representative for specific product ordering information and to obtain the specific
  Automotive Reliability reports for / these models.
- Page 3: **Versions of this part are available with controlled manufacturing to support the quality
  and reliability requirements of automotive applications. These / models are designated with a #W
  suffix. Only the automotive grade products shown are available for use in automotive applications.
  Contact your / local Analog Devices account representative for specific product ordering
  information and to obtain the specific Automotive Reliability reports for / these models.
- Page 20: The LTC3350 has a limit checking function that will check / each measured value against
  I2C/SMBus programmable / limits. This feature is optional, and all the limits are dis - / abled by
  default. The limit checking is designed to simplify / system monitoring, eliminating the need to
  continuously
- Page 21: feedback reference defaults to 1.2V; it may be changed / in the vcapfb_dac register . /
  All other digital features are optional and used for moni- / toring. The ADC automatically runs
  and stores conver- / sions to registers (e.g., meas_vcap ). Capacitance and
- Page 25: limited to a maximum of 2.7V and this may lead to an / unacceptably low capacitor
  lifetime. / An alternative option would be to keep V CELL(MAX) at a / voltage that leads to
  reasonably long lifetime and increase / the capacitor utilization ratio of the supercapacitor
  stack.
- Page 28: to limit the internal power dissipation of the LTC3350. / Schottky Diode Selection /
  Optional Schottky diodes can be placed in parallel with the top / and bottom MOSFET switches.
  These diodes clamp SW dur- / ing the non-overlap times between conduction of the top and
- Page 45: 42 / D 08/21 Added AEC-Q100 Qualified for Automotive Applications statement. / Added #W
  models in Ordering Information table. / 1 / 2
- Page 46: TYPICAL APPLICATION / 12V PCle Backup Controller / PART NUMBER DESCRIPTION COMMENTS /
  Power Management / LTC3128 3A Monolithic Buck-Boost Supercapacitor Charger

### Pin, pad, and connection designations

- Page 2: Absolute Maximum Ratings .............................. 3 / Order Information
  ..........................................3 / Pin Configuration
  .......................................... 3 / Electrical Characteristics
  ................................. 4 / Typical Performance Characteristics ................... 7
- Page 2: Electrical Characteristics ................................. 4 / Typical Performance
  Characteristics ................... 7 / Pin Functions
  ..............................................10 / Block Diagram
  .............................................13 / Timing Diagram
  ...........................................14
- Page 3: 3 / Rev. DFor more information www.analog.com / PIN CONFIGURATIONABSOLUTE MAXIMUM RATINGS
  / VIN, VOUTSP, VOUTSN ...............................-0.3V to 40V / VCAP
  .......................................................... -0.3V to 22V
- Page 3: 38-LEAD (5mm  x  7mm) PLASTIC QFN / TJMAX = 125 degC, JA = 34 degC/W / EXPOSED PAD (PIN
  39) IS PGND, MUST BE SOLDERED TO PCB / 17 18 19 / 38 37 36 35 34 33 32
- Page 3: AUTOMOTIVE PRODUCTS** / LTC3350IUHF#WPBF LTC3350IUHF#WTRPBF 3350 38-Lead (5mm  x  7mm)
  Plastic QFN -40 degC to 125 degC / Contact the factory for parts specified with wider operating
  temperature ranges. *The temperature grade is identified by a label on the shipping container . /
  Tape and reel specifications. Some packages are available in 500 unit reels through designated
  sales channels with #TRMPBF suffix. / **Versions of this part are available with controlled
  manufacturing to support the quality and reliability requirements of automotive applications.
  These
- Page 3: Contact the factory for parts specified with wider operating temperature ranges. *The
  temperature grade is identified by a label on the shipping container . / Tape and reel
  specifications. Some packages are available in 500 unit reels through designated sales channels
  with #TRMPBF suffix. / **Versions of this part are available with controlled manufacturing to
  support the quality and reliability requirements of automotive applications. These / models are
  designated with a #W suffix. Only the automotive grade products shown are available for use in
  automotive applications. Contact your / local Analog Devices account representative for specific
  product ordering information and to obtain the specific Automotive Reliability reports for
- Page 3: **Versions of this part are available with controlled manufacturing to support the quality
  and reliability requirements of automotive applications. These / models are designated with a #W
  suffix. Only the automotive grade products shown are available for use in automotive applications.
  Contact your / local Analog Devices account representative for specific product ordering
  information and to obtain the specific Automotive Reliability reports for / these models.
- Page 4: VPEAK Peak Inductor Current Sense Voltage l 51 58 65 mV / VREV Reverse Inductor Current
  Sense Voltage Step-Down Mode l 3.867 7 10 mV / IICAP ICAP Pin Current Step-Down Mode, VSNSC = 32mV
  / Step-Up Mode, VSNSC = 32mV / 30
- Page 6: V / V / IGPI General Purpose Input Pin Leakage Current Buffered Input 1 uA / RGPI GPI Pin
  Resistance Buffer Disabled 2.5 Mohm / Measurement System Error
- Page 6: V / IGPI General Purpose Input Pin Leakage Current Buffered Input 1 uA / RGPI GPI Pin
  Resistance Buffer Disabled 2.5 Mohm / Measurement System Error / VERR Measurement Error (Note 5)
  VIN = 0V
- Page 6: RSHNT Shunt Resistance 0.5 ohm / DVCAPMAX Maximum Capacitor Voltage with Shunts Enabled  2
  or More Capacitors in Stack 3.6 V / Programming Pins / VITST ITST Voltage RTST = 121ohm 1.185
  1.197 1.209 V / I2C/SMBus - SDA, SCL, SMBALERT
- Page 9: Rev. DFor more information www.analog.com / TYPICAL PERFORMANCE CHARACTERISTICS / IQ vs
  VIN, Pulse Skipping GPI Code vs Temperature / DRVCC Current vs Boost Inductor / Current
- Page 10: 10 / Rev. D For more information www.analog.com / PIN FUNCTIONS / SCL (Pin 1): Clock Pin
  for the I2C/SMBus Serial Port. / SDA (Pin 2):  Bidirectional Data Pin for the I 2C/SMBus
- Page 10: Rev. D For more information www.analog.com / PIN FUNCTIONS / SCL (Pin 1): Clock Pin for
  the I2C/SMBus Serial Port. / SDA (Pin 2):  Bidirectional Data Pin for the I 2C/SMBus / Serial
  Port.
- Page 10: PIN FUNCTIONS / SCL (Pin 1): Clock Pin for the I2C/SMBus Serial Port. / SDA (Pin 2):
  Bidirectional Data Pin for the I 2C/SMBus / Serial Port. / SMBALERT (Pin 3):  Interrupt Output.
  This open-drain
- Page 10: SCL (Pin 1): Clock Pin for the I2C/SMBus Serial Port. / SDA (Pin 2):  Bidirectional Data
  Pin for the I 2C/SMBus / Serial Port. / SMBALERT (Pin 3):  Interrupt Output. This open-drain /
  output is pulled low when an alarm threshold is exceeded,

### Specifications, ratings, and operating conditions

- Page 1: TYPICAL APPLICATION / FEATURES DESCRIPTION / High Current Supercapacitor Backup /
  Controller and System Monitor / The LT C(R)3350 is a backup power controller that can charge
- Page 1: and monitor a series stack of one to four supercapacitors. / The LTC3350's synchronous
  step-down controller drives / N-channel MOSFETs for constant current/constant volt - / age
  charging with programmable input current limit. In / addition, the step-down converter can run in
  reverse as
- Page 1: The LTC3350's synchronous step-down controller drives / N-channel MOSFETs for constant
  current/constant volt - / age charging with programmable input current limit. In / addition, the
  step-down converter can run in reverse as / a step-up converter to deliver power from the superca
  -
- Page 1: pacitor stack to the backup supply rail. Internal balancers / eliminate the need for
  external balance resistors and each / capacitor has a shunt regulator for overvoltage protection.
  / The LTC3350 monitors system voltages, currents, stack / capacitance and stack ESR which can all
  be read over
- Page 1: eliminate the need for external balance resistors and each / capacitor has a shunt
  regulator for overvoltage protection. / The LTC3350 monitors system voltages, currents, stack /
  capacitance and stack ESR which can all be read over / the I 2C/SMBus. The dual ideal diode
  controller uses
- Page 1: The LTC3350 is available in a low profile 38-lead 5mm  x / 7mm  x  0.75mm QFN surface
  mount package. / High Current Supercapacitor Charger and Backup Supply / APPLICATIONS / n High
  Efficiency Synchronous Step-Down CC/CV
- Page 1: n Step-Up Mode in Backup Provides Greater / Utilization of Stored Energy in
  Supercapacitors / n 14-Bit ADC for Monitoring System Voltages/ / Currents, Capacitance and ESR / n
  Active Overvoltage Protection Shunts
- Page 1: Utilization of Stored Energy in Supercapacitors / n 14-Bit ADC for Monitoring System
  Voltages/ / Currents, Capacitance and ESR / n Active Overvoltage Protection Shunts / n Internal
  Active Balancers-No Balance Resistors
- Page 1: n 14-Bit ADC for Monitoring System Voltages/ / Currents, Capacitance and ESR / n Active
  Overvoltage Protection Shunts / n Internal Active Balancers-No Balance Resistors / n VIN: 4.5V to
  35V, VCAP(n): Up to 5V per Capacitor ,
- Page 1: n Internal Active Balancers-No Balance Resistors / n VIN: 4.5V to 35V, VCAP(n): Up to 5V
  per Capacitor , / Charge/Backup Current: 10+A / n Programmable Input Current Limit Prioritizes
  System / Load Over Capacitor Charge Current
- Page 1: n VIN: 4.5V to 35V, VCAP(n): Up to 5V per Capacitor , / Charge/Backup Current: 10+A / n
  Programmable Input Current Limit Prioritizes System / Load Over Capacitor Charge Current / n Dual
  Ideal Diode PowerPath(TM) Controller
- Page 1: Charge/Backup Current: 10+A / n Programmable Input Current Limit Prioritizes System / Load
  Over Capacitor Charge Current / n Dual Ideal Diode PowerPath(TM) Controller / n All N-FET Charger
  Controller and PowerPath Controller
- Page 1: n Compact 38-Lead 5mm  x  7mm QFN Package / n AEC-Q100 Qualified for Automotive
  Applications / n High Current 12V Ride-Through UPS / n Servers/Mass Storage/High Availability
  Systems / Backup Operation
- Page 2: Typical Application  ........................................1 /
  Description.................................................. 1 / Absolute Maximum Ratings
  .............................. 3 / Order Information ..........................................3 /
  Pin Configuration .......................................... 3
- Page 2: Order Information ..........................................3 / Pin Configuration
  .......................................... 3 / Electrical Characteristics
  ................................. 4 / Typical Performance Characteristics ................... 7 /
  Pin Functions ..............................................10
- Page 2: Pin Functions ..............................................10 / Block Diagram
  .............................................13 / Timing Diagram
  ...........................................14 /
  Operation................................................... 14 / Introduction
  ............................................................14

### Dimensions, package, and mechanical information

- Page 1: input and supercapacitors to the backup system supply. / The LTC3350 is available in a low
  profile 38-lead 5mm  x / 7mm  x  0.75mm QFN surface mount package. / High Current Supercapacitor
  Charger and Backup Supply / APPLICATIONS
- Page 1: n Dual Ideal Diode PowerPath(TM) Controller / n All N-FET Charger Controller and PowerPath
  Controller / n Compact 38-Lead 5mm  x  7mm QFN Package / n AEC-Q100 Qualified for Automotive
  Applications / n High Current 12V Ride-Through UPS
- Page 2: Register Descriptions ....................................33 / Typical Applications
  ......................................39 / Package Description
  ..................................... 44 / Revision History
  .......................................... 45 / Typical Application
  .......................................46
- Page 3: 39 / PGND / UHF PACKAGE / 38-LEAD (5mm  x  7mm) PLASTIC QFN / TJMAX = 125 degC, JA = 34
  degC/W
- Page 3: 12 / ORDER INFORMATION / LEAD FREE FINISH TAPE AND REEL PART MARKING* PACKAGE DESCRIPTION
  TEMPERATURE RANGE / LTC3350EUHF#PBF LTC3350EUHF#TRPBF 3350 38-Lead (5mm  x  7mm) Plastic QFN -40
  degC to 125 degC / LTC3350IUHF#PBF LTC3350IUHF#TRPBF 3350 38-Lead (5mm  x  7mm) Plastic QFN -40
  degC to 125 degC
- Page 3: LTC3350IUHF#WPBF LTC3350IUHF#WTRPBF 3350 38-Lead (5mm  x  7mm) Plastic QFN -40 degC to 125
  degC / Contact the factory for parts specified with wider operating temperature ranges. *The
  temperature grade is identified by a label on the shipping container . / Tape and reel
  specifications. Some packages are available in 500 unit reels through designated sales channels
  with #TRMPBF suffix. / **Versions of this part are available with controlled manufacturing to
  support the quality and reliability requirements of automotive applications. These / models are
  designated with a #W suffix. Only the automotive grade products shown are available for use in
  automotive applications. Contact your
- Page 7: temperature range. Note that the maximum ambient temperature / consistent with these
  specifications is determined by specific operating / conditions in conjunction with board layout,
  the rated package thermal / impedance and other environmental factors. The junction temperature /
  (TJ, in  degC) is calculated from the ambient temperature (TA, in  degC) and
- Page 7: power dissipation (PD, in Watts) according to the formula: / TJ = TA + (PD - JA) / where
  JA = 34 degC/W for the UHF package. / Note 3: The LTC3350 includes overtemperature protection that
  is intended / to protect the device during momentary overload conditions. Junction
- Page 22: pulled from the trace connecting the two sense resistors. / Note that the backup current
  will flow through RSNSI2. The / RSNSI2 package should be sized accordingly to handle the / power
  dissipation. / Figure 3.
- Page 29: Electrical Characteristics. For example, the IG supplied by / the INTVCC LDO is limited
  to less than 42mA from a 35V / supply in the QFN package at a 70 degC ambient temperature: / T J =
  70 degC + (35V)(4mA + 42mA)(34 degC/W) = 125 degC / To prevent the maximum junction temperature
  from being
- Page 44: 44 / Rev. D For more information www.analog.com / PACKAGE DESCRIPTION / 5.00 +/-0.10 /
  NOTE:
- Page 44: 5.00 +/-0.10 / NOTE: / 1. DRAWING CONFORMS TO JEDEC PACKAGE / OUTLINE M0-220 VARIATION
  WHKD / 2. DRAWING NOT TO SCALE
- Page 44: NOTE: / 1. DRAWING CONFORMS TO JEDEC PACKAGE / OUTLINE M0-220 VARIATION WHKD / 2. DRAWING
  NOT TO SCALE / 3. ALL DIMENSIONS ARE IN MILLIMETERS
- Page 44: 1. DRAWING CONFORMS TO JEDEC PACKAGE / OUTLINE M0-220 VARIATION WHKD / 2. DRAWING NOT TO
  SCALE / 3. ALL DIMENSIONS ARE IN MILLIMETERS / PIN 1
- Page 44: OUTLINE M0-220 VARIATION WHKD / 2. DRAWING NOT TO SCALE / 3. ALL DIMENSIONS ARE IN
  MILLIMETERS / PIN 1 / TOP MARK
- Page 44: 7.50 +/-0.05 / 0.25 +/-0.05 / PACKAGE / OUTLINE / 4. DIMENSIONS OF EXPOSED PAD ON BOTTOM
  OF PACKAGE DO NOT INCLUDE

### Formulas, equations, and configurable calculations

- Page 1: n High Current 12V Ride-Through UPS / n Servers/Mass Storage/High Availability Systems /
  Backup Operation / VIN / PFI OUTFB
- Page 2: Absolute Maximum Ratings .............................. 3 / Order Information
  ..........................................3 / Pin Configuration
  .......................................... 3 / Electrical Characteristics
  ................................. 4 / Typical Performance Characteristics ................... 7
- Page 2: Block Diagram .............................................13 / Timing Diagram
  ...........................................14 /
  Operation................................................... 14 / Introduction
  ............................................................14 / Bidirectional Switching
  Controller- Step-Down
- Page 2: Ideal Diodes ............................................................16 / Gate Drive
  Supply (DRVCC)  ....................................17 / Undervoltage Lockout (UVLO)
  ...............................17 / RT Oscillator and Switching Frequency .................. 17 /
  Input Overvoltage Protection  .................................17
- Page 2: General Purpose Input ............................................20 / Applications
  Information ................................ 21 / Digital Configuration
  ...............................................21 / Capacitor Configuration
  ..........................................21 / Capacitor Shunt Regulator Programming
  ...............21
- Page 2: Applications Information ................................ 21 / Digital Configuration
  ...............................................21 / Capacitor Configuration
  ..........................................21 / Capacitor Shunt Regulator Programming
  ...............21 / Setting Input and Charge Currents .........................21
- Page 2: Top MOSFET Driver Supply (CB, DB) .......................29 / INTVCC/DRVCC and IC Power
  Dissipation ...............29 / Minimum On-Time Considerations..........................30 / Ideal
  Diode MOSFET Selection ............................... 30 / PCB Layout Considerations
  ....................................30
- Page 2: Minimum On-Time Considerations..........................30 / Ideal Diode MOSFET Selection
  ............................... 30 / PCB Layout Considerations
  ....................................30 / Register Map
  ..............................................32 / Register Descriptions
  ....................................33
- Page 3: 3 / Rev. DFor more information www.analog.com / PIN CONFIGURATIONABSOLUTE MAXIMUM RATINGS
  / VIN, VOUTSP, VOUTSN ...............................-0.3V to 40V / VCAP
  .......................................................... -0.3V to 22V
- Page 4: IOUTFB OUTFB Input Leakage Current VOUTFB = 1.2V l -50 50 nA / VOUTBST VOUT Voltage in
  Step-Up Mode VIN = 0V l 4.5 35 V / VUVLO INTVCC Undervoltage Lockout Rising Threshold / Falling
  Threshold / l
- Page 4: 4.45 V / V / VDRVUVLO DRVCC Undervoltage Lockout Rising Threshold / Falling Threshold / l
- Page 4: 4.35 V / V / VDUVLO VIN - VCAP Differential Undervoltage Lockout Rising Threshold /
  Falling Threshold / l
- Page 7: LTC3350I is guaranteed over the -40 degC to 125 degC operating junction / temperature
  range. Note that the maximum ambient temperature / consistent with these specifications is
  determined by specific operating / conditions in conjunction with board layout, the rated package
  thermal / impedance and other environmental factors. The junction temperature
- Page 7: conditions in conjunction with board layout, the rated package thermal / impedance and
  other environmental factors. The junction temperature / (TJ, in  degC) is calculated from the
  ambient temperature (TA, in  degC) and / power dissipation (PD, in Watts) according to the
  formula: / TJ = TA + (PD - JA)
- Page 7: impedance and other environmental factors. The junction temperature / (TJ, in  degC) is
  calculated from the ambient temperature (TA, in  degC) and / power dissipation (PD, in Watts)
  according to the formula: / TJ = TA + (PD - JA) / where JA = 34 degC/W for the UHF package.
- Page 7: to protect the device during momentary overload conditions. Junction / temperature will
  exceed 125 C when overtemperature protection is active. / Continuous operation above the specified
  maximum operating junction / temperature may impair device reliability. / Note 4: Dynamic supply
  current is higher due to the gate charge being

### Reference designs, applications, and examples

- Page 1: Rev. DFor more information www.analog.com / Document Feedback / TYPICAL APPLICATION /
  FEATURES DESCRIPTION / High Current Supercapacitor Backup
- Page 1: 7mm  x  0.75mm QFN surface mount package. / High Current Supercapacitor Charger and Backup
  Supply / APPLICATIONS / n High Efficiency Synchronous Step-Down CC/CV / Charging of One to Four
  Series Supercapacitors
- Page 1: n All N-FET Charger Controller and PowerPath Controller / n Compact 38-Lead 5mm  x  7mm
  QFN Package / n AEC-Q100 Qualified for Automotive Applications / n High Current 12V Ride-Through
  UPS / n Servers/Mass Storage/High Availability Systems
- Page 1: 2V/DIV / 400ms/DIV / BACK PAGE APPLICATION CIRCUIT / 0V / 3350 TA01a
- Page 2: TABLE OF CONTENTS / Features ..................................................... 1 /
  Applications ................................................ 1 / Typical Application
  ........................................1 /
  Description.................................................. 1
- Page 2: Features ..................................................... 1 / Applications
  ................................................ 1 / Typical Application
  ........................................1 /
  Description.................................................. 1 / Absolute Maximum Ratings
  .............................. 3
- Page 2: Die Temperature Sensor .........................................20 / General Purpose Input
  ............................................20 / Applications Information
  ................................ 21 / Digital Configuration
  ...............................................21 / Capacitor Configuration
  ..........................................21
- Page 2: Register Map ..............................................32 / Register Descriptions
  ....................................33 / Typical Applications
  ......................................39 / Package Description
  ..................................... 44 / Revision History
  .......................................... 45
- Page 2: Package Description ..................................... 44 / Revision History
  .......................................... 45 / Typical Application
  .......................................46 / Related Parts
  ..............................................46
- Page 3: Contact the factory for parts specified with wider operating temperature ranges. *The
  temperature grade is identified by a label on the shipping container . / Tape and reel
  specifications. Some packages are available in 500 unit reels through designated sales channels
  with #TRMPBF suffix. / **Versions of this part are available with controlled manufacturing to
  support the quality and reliability requirements of automotive applications. These / models are
  designated with a #W suffix. Only the automotive grade products shown are available for use in
  automotive applications. Contact your / local Analog Devices account representative for specific
  product ordering information and to obtain the specific Automotive Reliability reports for
- Page 3: Tape and reel specifications. Some packages are available in 500 unit reels through
  designated sales channels with #TRMPBF suffix. / **Versions of this part are available with
  controlled manufacturing to support the quality and reliability requirements of automotive
  applications. These / models are designated with a #W suffix. Only the automotive grade products
  shown are available for use in automotive applications. Contact your / local Analog Devices
  account representative for specific product ordering information and to obtain the specific
  Automotive Reliability reports for / these models.
- Page 7: temperature may impair device reliability. / Note 4: Dynamic supply current is higher due
  to the gate charge being / delivered at the switching frequency. See the Applications Information
  / section. / Note 5: Measurement error is the magnitude of the difference between the
- Page 7: 2V/DIV / 400ms/DIV / BACK PAGE APPLICATION CIRCUIT / 0V / 3350 G01
- Page 7: 5V/DIV / 20ms/DIV / APPLICATION CIRCUIT 6 / 0V / 3350 G02
- Page 7: ICHARGE / VSHUNT = 2.7V / TA = 25 degC, Application Circuit 4 unless otherwise noted.
- Page 8: TYPICAL PERFORMANCE CHARACTERISTICS / VCAP vs Temperature Efficiency in Boost Mode Load
  Regulation in Boost Mode / TA = 25 degC, Application Circuit 4 unless otherwise noted. / VIN (V) /
  11

## Page-by-Page Extracted Text

### Page 1

```text
LTC3350
1
Rev. DFor more information www.analog.com
Document Feedback
TYPICAL APPLICATION
FEATURES DESCRIPTION
High Current Supercapacitor Backup
Controller and System Monitor
The LT C(R)3350 is a backup power controller that can charge
and monitor a series stack of one to four supercapacitors.
The LTC3350's synchronous step-down controller drives
N-channel MOSFETs for constant current/constant volt -
age charging with programmable input current limit. In
addition, the step-down converter can run in reverse as
a step-up converter to deliver power from the superca -
pacitor stack to the backup supply rail. Internal balancers
eliminate the need for external balance resistors and each
capacitor has a shunt regulator for overvoltage protection.
The LTC3350 monitors system voltages, currents, stack
capacitance and stack ESR which can all be read over
the I 2C/SMBus. The dual ideal diode controller uses
N-channel MOSFETs for low loss power paths from the
input and supercapacitors to the backup system supply.
The LTC3350 is available in a low profile 38-lead 5mm  x
7mm  x  0.75mm QFN surface mount package.
High Current Supercapacitor Charger and Backup Supply
APPLICATIONS
 n High Efficiency Synchronous Step-Down CC/CV
Charging of One to Four Series Supercapacitors
 n Step-Up Mode in Backup Provides Greater
Utilization of Stored Energy in Supercapacitors
 n 14-Bit ADC for Monitoring System Voltages/
Currents, Capacitance and ESR
 n Active Overvoltage Protection Shunts
 n Internal Active Balancers-No Balance Resistors
 n VIN: 4.5V to 35V, VCAP(n): Up to 5V per Capacitor ,
Charge/Backup Current: 10+A
 n Programmable Input Current Limit Prioritizes System
Load Over Capacitor Charge Current
 n Dual Ideal Diode PowerPath(TM) Controller
 n All N-FET Charger Controller and PowerPath Controller
 n Compact 38-Lead 5mm  x  7mm QFN Package
 n AEC-Q100 Qualified for Automotive Applications
 n High Current 12V Ride-Through UPS
 n Servers/Mass Storage/High Availability Systems
Backup Operation
VIN
PFI OUTFB
OUTFET
TGATE
SW
BGATE
ICAP
VCAP
CAP4
CAP3
CAP2
CAP1
CAPRTN
CAPFB
INFET VOUTSP VOUTSN
ICHG (STEP-DOWN) IBACKUP
VCAP < VOUT
(STEP-UP)
VCAP > VOUT
(DIRECT
CONNECT)
VOUT
L TC3350
10F
VCAP
10F
10F
10F
3350 TA01a
I2C
VIN
2V/DIV
VCAP
2V/DIV
VOUT
2V/DIV
400ms/DIV
BACK PAGE APPLICATION CIRCUIT
0V
3350 TA01a
PBACKUP = 25W
VOUT
VCAP
VIN
All registered trademarks and trademarks are the property of their respective owners.
Patents pending.
```

### Page 2

```text
LTC3350
2
Rev. D For more information www.analog.com
TABLE OF CONTENTS
Features ..................................................... 1
Applications ................................................ 1
Typical Application  ........................................1
Description.................................................. 1
Absolute Maximum Ratings .............................. 3
Order Information ..........................................3
Pin Configuration .......................................... 3
Electrical Characteristics ................................. 4
Typical Performance Characteristics ................... 7
Pin Functions ..............................................10
Block Diagram .............................................13
Timing Diagram ...........................................14
Operation................................................... 14
Introduction ............................................................14
Bidirectional Switching Controller- Step-Down
Mode ...................................................................... 14
Bidirectional Switching Controller- Step-Up
Mode ...................................................................... 15
Ideal Diodes ............................................................16
Gate Drive Supply (DRVCC)  ....................................17
Undervoltage Lockout (UVLO)  ...............................17
RT Oscillator and Switching Frequency .................. 17
Input Overvoltage Protection  .................................17
VCAP DAC  ...............................................................17
Power-Fail (PF) Comparator.................................... 17
Charge Status Indication......................................... 17
Capacitor Voltage Balancer  ....................................17
Capacitor Shunt Regulators ....................................18
I2C/SMBus and SMBALERT ....................................18
Analog-to-Digital Converter ....................................18
Capacitance and ESR Measurement  ...................... 18
Monitor Status Register ..........................................19
Charge Status Register ...........................................20
Limit Checking and Alarms .....................................20
Die Temperature Sensor .........................................20
General Purpose Input ............................................20
Applications Information ................................ 21
Digital Configuration ...............................................21
Capacitor Configuration ..........................................21
Capacitor Shunt Regulator Programming ...............21
Setting Input and Charge Currents .........................21
Low Current Charging and High Current Backup ....22
Setting VCAP Voltage ...............................................22
Power-Fail Comparator Input Voltage Threshold   ...22
Setting VOUT Voltage in Backup Mode ....................23
Compensation .........................................................24
Minimum VCAP Voltage in Backup Mode .................24
Optimizing Supercapacitor Energy Storage
Capacity ..................................................................25
Capacitor Selection Procedure  ...............................26
Inductor Selection...................................................26
COUT and CCAP Capacitance ....................................27
Power MOSFET Selection .......................................28
Schottky Diode Selection ........................................28
Top MOSFET Driver Supply (CB, DB) .......................29
INTVCC/DRVCC and IC Power Dissipation ...............29
Minimum On-Time Considerations..........................30
Ideal Diode MOSFET Selection ............................... 30
PCB Layout Considerations ....................................30
Register Map ..............................................32
Register Descriptions ....................................33
Typical Applications ......................................39
Package Description ..................................... 44
Revision History .......................................... 45
Typical Application .......................................46
Related Parts ..............................................46
```

### Page 3

```text
LTC3350
3
Rev. DFor more information www.analog.com
PIN CONFIGURATIONABSOLUTE MAXIMUM RATINGS
VIN, VOUTSP, VOUTSN ...............................-0.3V to 40V
VCAP .......................................................... -0.3V to 22V
CAP4-CAP3, CAP3-CAP2, CAP2-CAP1,
CAP1-CAPRTN ..........................................-0.3V to 5.5V
DRVCC, OUTFB, CAPFB, SMBALERT, CAPGD,
PFO, GPI, SDA, SCL ..................................-0.3V to 5.5V
BST .........................................................-0.3V to 45.5V
PFI ............................................................. -0.3V to 20V
CAP_SLCT0, CAP_SLCT1 ................................-0.3 to 3V
BST to SW ................................................ -0.3V to 5.5V
VOUTSP to VOUTSN, ICAP to VCAP ......... -0.3V to 0.3V
IINTVCC .................................................................100mA
ICAP(1,2,3,4), ICAPRTN ............................................600mA
ICAPGD, IPFO , ISMBALERT .........................................10mA
Operating Junction Temperature Range
(Notes 2, 3) ..............................................-40 degC to 125 degC
Storage Temperature Range .................. -65 degC to 150 degC
(Note 1)
13 14 15 16
TOP VIEW
39
PGND
UHF PACKAGE
38-LEAD (5mm  x  7mm) PLASTIC QFN
TJMAX = 125 degC, JA = 34 degC/W
EXPOSED PAD (PIN 39) IS PGND, MUST BE SOLDERED TO PCB
17 18 19
38 37 36 35 34 33 32
24
25
26
27
28
29
30
31
8
7
6
5
4
3
2
1SCL
SDA
SMBALERT
CAPGD
VC
CAPFB
OUTFB
SGND
RT
GPI
ITST
CAPRTN
VOUTSP
VOUTSN
INTVCC
DRVCC
BGATE
BST
TGATE
SW
VCC2P5
ICAP
VCAP
OUTFET
PFO
PFI
CAP_SLCT1
CAP_SLCT0
VIN
INFET
VOUTM5
CAP1
CAP2
CAP3
CAP4
CFP
CFN
VCAPP5
23
22
21
20
9
10
11
12
ORDER INFORMATION
LEAD FREE FINISH TAPE AND REEL PART MARKING* PACKAGE DESCRIPTION TEMPERATURE RANGE
LTC3350EUHF#PBF LTC3350EUHF#TRPBF 3350 38-Lead (5mm  x  7mm) Plastic QFN -40 degC to 125 degC
LTC3350IUHF#PBF LTC3350IUHF#TRPBF 3350 38-Lead (5mm  x  7mm) Plastic QFN -40 degC to 125 degC
AUTOMOTIVE PRODUCTS**
LTC3350IUHF#WPBF LTC3350IUHF#WTRPBF 3350 38-Lead (5mm  x  7mm) Plastic QFN -40 degC to 125 degC
Contact the factory for parts specified with wider operating temperature ranges. *The temperature
grade is identified by a label on the shipping container .
Tape and reel specifications. Some packages are available in 500 unit reels through designated sales
channels with #TRMPBF suffix.
**Versions of this part are available with controlled manufacturing to support the quality and
reliability requirements of automotive applications. These
models are designated with a #W suffix. Only the automotive grade products shown are available for
use in automotive applications. Contact your
local Analog Devices account representative for specific product ordering information and to obtain
the specific Automotive Reliability reports for
these models.
```

### Page 4

```text
LTC3350
4
Rev. D For more information www.analog.com
ELECTRICAL CHARACTERISTICS The l denotes the specifications which apply over the specified
operating junction temperature range, otherwise specifications are at TA = 25 degC (Note 2). VIN =
VOUT = 12V, VDRVCC = VINTVCC unless
otherwise noted.
SYMBOL PARAMETER CONDITIONS MIN TYP MAX UNITS
Switching Regulator
VIN Input Supply Voltage l 4.5 35 V
IQ  Input Quiescent Current (Note 4) 4 mA
VCAPFBHI Maximum Regulated VCAP Feedback Voltage VCAPDAC Full Scale (1111b)
l
1.188
1.176
1.200
1.200
1.212
1.224
V
V
VCAPFBLO Minimum Regulated VCAP Feedback Voltage VCAPDAC Zero Scale (0000b) 0.628 0.638 0.647 V
ICAPFB CAPFB Input Leakage Current VCAPFB = 1.2V l -50 50 nA
VOUTFB Regulated VOUT Feedback Voltage
l
1.188
1.176
1.200
1.200
1.212
1.224
V
V
VOUTFB(TH) OUTFET Turn-Off Threshold Falling Threshold 1.27 1.3 1.33 V
IOUTFB OUTFB Input Leakage Current VOUTFB = 1.2V l -50 50 nA
VOUTBST VOUT Voltage in Step-Up Mode VIN = 0V l 4.5 35 V
VUVLO INTVCC Undervoltage Lockout Rising Threshold
Falling Threshold
l
l

3.85
4.3
4
4.45 V
V
VDRVUVLO DRVCC Undervoltage Lockout Rising Threshold
Falling Threshold
l
l

3.75
4.2
3.9
4.35 V
V
VDUVLO VIN - VCAP Differential Undervoltage Lockout Rising Threshold
Falling Threshold
l
l
145
55
185
90
225
125
mV
mV
VOVLO VIN Overvoltage Lockout Rising Threshold
Falling Threshold
l
l
37.7
36.3
38.6
37.2
39.5
38.1
V
V
VVCAPP5 Charge Pump Output Voltage Relative to VCAP,  0V <= VCAP <= 20V 5 V
Input Current Sense Amplifier
VSNSI Regulated Input Current Sense Voltage
(VOUTSP - VOUTSN)

l
31.36
31.04
32.00
32.00
32.64
32.96
mV
mV
Charge Current Sense Amplifier
VSNSC Regulated Charge Current Sense Voltage
(ICAP - VCAP)
VCAP = 10V
l
31.36
31.04
32.00
32.00
32.64
32.96
mV
mV
VCMC Common Mode Range (ICAP , VCAP) 0 20 V
VPEAK Peak Inductor Current Sense Voltage l 51 58 65 mV
VREV Reverse Inductor Current Sense Voltage Step-Down Mode l 3.867 7 10 mV
IICAP ICAP Pin Current Step-Down Mode, VSNSC = 32mV
Step-Up Mode, VSNSC = 32mV
30
135
uA
uA
Error Amplifier
gMV VCAP Voltage Loop T ransconductance 1 mmho
gMC Charge Current Loop T ransconductance 64 umho
gMI Input Current Loop T ransconductance 64 umho
gMO VOUT Voltage Loop T ransconductance 400 umho
Oscillator
fSW Switching Frequency RT = 107k
l
495
490
500
500
505
510
kHz
kHz
Maximum Programmable Frequency RT = 53.6k 1 MHz
Minimum Programmable Frequency RT = 267k 200 kHz
```

### Page 5

```text
LTC3350
5
Rev. DFor more information www.analog.com
ELECTRICAL CHARACTERISTICS The l denotes the specifications which apply over the specified
operating junction temperature range, otherwise specifications are at TA = 25 degC (Note 2). VIN =
VOUT = 12V, VDRVCC = VINTVCC unless
otherwise noted.
SYMBOL PARAMETER CONDITIONS MIN TYP MAX UNITS
DCMAX Maximum Duty Cycle Step-Down Mode
Step-Up Mode
97
87
98
93
99.5 %
%
Gate Drivers
RUP-TG TGATE Pull-Up On-Resistance 2 ohm
RDOWN-TG TGATE Pull-Down On-Resistance 0.6 ohm
RUP-BG BGATE Pull-Up On-Resistance 2 ohm
RDOWN-BG BGATE Pull-Down On-Resistance 0.6 ohm
tr-TG TGATE 10% to 90% Rise Time CLOAD = 3.3nF 18 25 ns
tf-TG TGATE 10% to 90% Fall Time CLOAD = 3.3nF 8 15 ns
tr-BG BGATE 10% to 90% Rise Time CLOAD = 3.3nF 18 25 ns
tf-BG BGATE 10% to 90% Fall Time CLOAD = 3.3nF 8 15 ns
tNO Non-Overlap Time 50 ns
tON(MIN)    85 ns
INTVCC Linear Regulator
VINTVCC Internal VCC Voltage       5.2V <= VIN <= 35V 5 V
VINTVCC Load Regulation IINTVCC = 50mA -1.5 -2.5 %
PowerPath/Ideal Diodes
VFTO Forward Turn-On Voltage 65 mV
VFR Forward Regulation 30 mV
VRTO Reverse Turn Off -30 mV
tIF(ON) INFET Rise Time INFET - VIN > 3V, CINFET = 3.3nF 560 us
tIF(OFF) INFET Fall Time INFET - VIN < 1V, CINFET = 3.3nF 1.5 us
tOF(ON) OUTFET Rise Time OUTFET - VCAP > 3V, COUTFET = 3.3nF 0.13 us
tOF(OFF) OUTFET Fall Time OUTFET - VCAP < 1V, COUTFET = 3.3nF 0.26 us
Power-Fail Comparator
VPFI(TH) PFI Input Threshold (Falling Edge)       l 1.147 1.17 1.193 V
VPFI(HYS) PFI Hysteresis 30 mV
IPFI PFI Input Leakage Current VPFI = 0.5V l -50 50 nA
VPFO PFO Output Low Voltage ISINK = 5mA 200 mV
IPFO PFO High-Z Leakage Current VPFO = 5V l 1 uA
PFI Falling to PFO Low Delay 85 ns
PFI Rising to PFO High Delay 0.4 us
CAPGD
VCAPFB(TH) CAPGD Rising Threshold as % of Regulated VCAP
Feedback Voltage
Vcapfb_dac = Full Scale (1111b) l 90 92 94 %
VCAPFB(HYS) CAPGD Hysteresis at CAPFB as a % of Regulated
VCAP Feedback Voltage
Vcapfb_dac = Full Scale (1111b) 1.25 %
VCAPGD CAPGD Output Low Voltage ISINK = 5mA 200 mV
ICAPGD CAPGD High-Z Leakage Current VCAPGD = 5V l 1 uA
```

### Page 6

```text
LTC3350
6
Rev. D For more information www.analog.com
ELECTRICAL CHARACTERISTICS The l denotes the specifications which apply over the specified
operating junction temperature range, otherwise specifications are at TA = 25 degC (Note 2). VIN =
VOUT = 12V, VDRVCC = VINTVCC unless
otherwise noted.
SYMBOL PARAMETER CONDITIONS MIN TYP MAX UNITS
Analog-to-Digital Converter
VRES Measurement Resolution 16 Bits
VGPI General Purpose Input Voltage Range Unbuffered
Buffered
0
0
5
3.5
V
V
IGPI General Purpose Input Pin Leakage Current Buffered Input 1 uA
RGPI GPI Pin Resistance Buffer Disabled 2.5 Mohm
Measurement System Error
VERR Measurement Error (Note 5) VIN = 0V
VIN = 30V
100
1.5
mV
%
VOUTSP = 5V
VOUTSP = 30V
100
1.5
mV
%
VCAP = 0V
VCAP = 10V
100
1.5
mV
%
VGPI = 0V, Unbuffered
VGPI = 3.5V, Unbuffered
2
1
mV
%
VCAP1 = 0V
VCAP1 = 2V
2
1
mV
%
VCAP2 = 0V
VCAP2 = 2V
2
1
mV
%
VCAP3 = 0V
VCAP3 = 2V
2
1
mV
%
VCAP4 = 0V
VCAP4 = 2V
2
1
mV
%
VSNSI = 0mV
VSNSI = 32mV
200
2
uV
%
VSNSC = 0mV
VSNSC = 32mV
200
2
uV
%
CAP1 to CAP4
RSHNT Shunt Resistance 0.5 ohm
DVCAPMAX Maximum Capacitor Voltage with Shunts Enabled  2 or More Capacitors in Stack 3.6 V
Programming Pins
VITST ITST Voltage RTST = 121ohm 1.185 1.197 1.209 V
I2C/SMBus - SDA, SCL, SMBALERT
IIL,SDA,SCL Input Leakage Low -1 1 uA
IIH,SDA,SCL Input Leakage High -1 1 uA
VIH Input High Threshold 1.5 V
VIL Input  Low Threshold 0.8 V
fSCL SCL Clock Frequency 400 kHz
tLOW Low Period of SCL Clock 1.3 us
tHIGH High Period of SCL Clock 0.6 us
tBUF Bus Free Time Between Start and Stop Conditions 1.3 us
tHD,STA Hold Time, After (Repeated) Start Condition 0.6 us
tSU,STA Setup Time After a Repeated Start Condition 0.6 us
```

### Page 7

```text
LTC3350
7
Rev. DFor more information www.analog.com
ELECTRICAL CHARACTERISTICS The l denotes the specifications which apply over the specified
operating junction temperature range, otherwise specifications are at TA = 25 degC (Note 2). VIN =
VOUT = 12V, VDRVCC = VINTVCC unless
otherwise noted.
SYMBOL PARAMETER CONDITIONS MIN TYP MAX UNITS
tSU,STO Stop Condition Set-Up Time 0.6 us
tHD,DATO Output Data Hold Time 0 900 ns
tHD,DATI Input Data Hold Time 0 ns
tSU,DAT Data Set-Up Time 100 ns
tSP Input Spike Suppression Pulse Width 50 ns
VSMBALERT SMBALERT Output Low Voltage ISINK = 1mA 200 mV
ISMBALERT SMBALERT High-Z Leakage Current VSMBALERT = 5V l 1 uA
Note 1: Stresses beyond those listed under Absolute Maximum Ratings
may cause permanent damage to the device. Exposure to any Absolute
Maximum Rating condition for extended periods may affect device
reliability and lifetime.
Note 2: The LTC3350 is tested under pulsed load conditions such that
TJ  TA. The LTC3350E is guaranteed to meet specifications from
0 degC to 125 degC junction temperature. Specifications over the -40 degC to
125 degC operating junction temperature range are assured by design,
characterization and correlation with statistical process controls. The
LTC3350I is guaranteed over the -40 degC to 125 degC operating junction
temperature range. Note that the maximum ambient temperature
consistent with these specifications is determined by specific operating
conditions in conjunction with board layout, the rated package thermal
impedance and other environmental factors. The junction temperature
(TJ, in  degC) is calculated from the ambient temperature (TA, in  degC) and
power dissipation (PD, in Watts) according to the formula:
TJ = TA + (PD - JA)
where JA = 34 degC/W for the UHF package.
Note 3: The LTC3350 includes overtemperature protection that is intended
to protect the device during momentary overload conditions. Junction
temperature will exceed 125 C when overtemperature protection is active.
Continuous operation above the specified maximum operating junction
temperature may impair device reliability.
Note 4: Dynamic supply current is higher due to the gate charge being
delivered at the switching frequency. See the Applications Information
section.
Note 5: Measurement error is the magnitude of the difference between the
actual measured value and the ideal value. VSNSI is the voltage between
VOUTSP and VOUTSN, representing input current. VSNSC is the voltage
between ICAP and VCAP , representing charge current. Error for VSNSI and
VSNSC is expressed in uV , a conversion to an equivalent current may be
made by dividing by the sense resistors, RSNSI and RSNSC, respectively.
TYPICAL PERFORMANCE CHARACTERISTICS
Supercapacitor Backup Operation HV Electrolytic Backup Operation Shunt Operation Using VCAP2
VIN
2V/DIV
VCAP
2V/DIV
VOUT
2V/DIV
400ms/DIV
BACK PAGE APPLICATION CIRCUIT
0V
3350 G01
PBACKUP = 25W
VIN
5V/DIV
VCAP
5V/DIV
VOUT
5V/DIV
20ms/DIV
APPLICATION CIRCUIT 6
0V
3350 G02
PBACKUP = 25W
VCAP2 (V)
2.64
CURRENT (A)
3
4
5
2.67 2.69
3350 G03
2
1
2.65 2.66 2.68
ICAP2
2.70 2.71
0
-1
ICHARGE
VSHUNT = 2.7V
TA = 25 degC, Application Circuit 4 unless otherwise noted.
```

### Page 8

```text
LTC3350
8
Rev. D For more information www.analog.com
IIN and ICHARGE vs VIN ICHARGE vs VCAP
Charger Efficiency vs VCAP
ICHARGE vs VCAP
IIN and ICHARGE vs IOUT VCAP vs vcapfb_dac
TYPICAL PERFORMANCE CHARACTERISTICS
VCAP vs Temperature Efficiency in Boost Mode Load Regulation in Boost Mode
TA = 25 degC, Application Circuit 4 unless otherwise noted.
VIN (V)
11
CURRENT (A)
2.9
3.5
36
3350 G04
2.3
1.7
16 21 26 31
IIN
4.1
125 degC
25 degC
-40 degC
IOUT = 1A
VCAP = 6V
ICHARGE
VCAP (V)
0
ICHARGE (A)
2.50
3.75
8
3350 G06
1.25
0
2 4 6
5.00
VIN = 12V
VIN = 24V
VIN = 35V
IIN(MAX) = 2A
IOUT = 1A
VCAP (V)
0
EFFICIENCY (%)
50
75
7.2
3350 G08
25
0
1.8 3.6 5.4
100
VIN = 12V
VIN = 24V
VIN = 35V
IIN(MAX) = 2A
IOUT = 0A
VCAP (V)
0
ICHARGE (A)
2.50
3.75
8
3350 G05
1.25
0
2 4 6
5.00
VIN = 12V
VIN = 24V
VIN = 35V
IIN(MAX) = 2A
IOUT = 0A
IOUT (A)
0
CURRENT (A)
2.50
3.75
3.00
3350 G07
1.25
0
0.75 1.50 2.25
IIN
5.00
VIN = 12V
VIN = 24V
VIN = 35V
IIN(MAX) = 2A
ICHARGE
vcapfb_dac (CODE)
0 1 2 3 4 5 6 7 8 9 10 11 12 1413
VCAP (V)5.50
6.75
15
3350 G09
4.25
3.00
8.00
ICHARGE = 2A
TEMPERATURE ( degC)
-40
VCAP (V)
7.200
7.205
130
3350 G10
7.195
7.190
7.185
-6 28 62 96
7.210
capfb_dac = 15
ICHARGE = 2A
IOUT (A)
25
EFFICIENCY (%)
50
75
100
10-3 10-2 10-1 100 101
3350 G11
0
VCAP = 2V
VCAP = 3V
VCAP = 4V
APPLICATION CIRCUIT 5
IOUT (A)
4.981
VOUT (BOOST) (V)
4.988
4.994
5.000
10-3 10-2 10-1 100 101
3350 G12
4.975
VCAP = 2V
VCAP = 3V
VCAP = 4V
APPLICATION CIRCUIT 5
```

### Page 9

```text
LTC3350
9
Rev. DFor more information www.analog.com
TYPICAL PERFORMANCE CHARACTERISTICS
IQ vs VIN, Pulse Skipping GPI Code vs Temperature
DRVCC Current vs Boost Inductor
Current
INTVCC vs Charge Current INTVCC vs Temperature
TA = 25 degC, Application Circuit 4 unless otherwise noted.
VIN (V)
10
IQ (mA)4.60
4.75
35
3350 G13
4.45
4.30
15 20 25 30
4.90
125 degC
25 degC
-40 degC
TEMPERATURE ( degC)
-40
CODE
5470
5475
130
3350 G14
5460
5465
5455
-6 28 62 96
5480 VGPI = 1V
IL (A)
0
IDRVCC (mA)5.0
7.5
6
3350 G15
2.5
0
1.5 3 4.5
10.0
125 degC
25 degC
-40 degC
VCAP = 4V
APPLICATION CIRCUIT 5
ICHARGE (A)
0
INTVCC (V)
4.875
4.938
4
3350 G16
4.813
4.750
1 2 3
5.000
VIN = 12V
125 degC
25 degC
-40 degC
TEMPERATURE ( degC)
-40
INTVCC (V)
4.875
4.938
130
3350 G17
4.813
4.750
-6 28 62 96
5.000
```

### Page 10

```text
LTC3350
10
Rev. D For more information www.analog.com
PIN FUNCTIONS
SCL (Pin 1): Clock Pin for the I2C/SMBus Serial Port.
SDA (Pin 2):  Bidirectional Data Pin for the I 2C/SMBus
Serial Port.
SMBALERT (Pin 3):  Interrupt Output. This open-drain
output is pulled low when an alarm threshold is exceeded,
and will remain low until the acknowledgement of the
part's response to an SMBus ARA.
CAPGD (Pin 4): Capacitor Power Good. This open-drain
output is pulled low when CAPFB is below 92% of its
regulation point.
VC (PIN 5): Control Voltage Pin. This is the compensation
node for the charge current, input current, supercapacitor
stack voltage and output voltage control loops. An RC
network is connected between VC and SGND. Nominal
voltage range for this pin is 1V to 3V.
CAPFB (Pin 6): Capacitor Stack Feedback Pin. This pin
closes the feedback loop for constant voltage regulation.
An external resistor divider between VCAP and SGND with
the center tap connected to CAPFB programs the final
supercapacitor stack voltage. This pin is nominally equal
to the output of the V CAP DAC when the synchronous
controller is in constant voltage mode while charging.
OUTFB (Pin 7):  Step-Up Mode Feedback Pin. This pin
closes the feedback loop for voltage regulation of V OUT
during input power failure using the synchronous
controller in step-up mode. An external resistor divider
between VOUT and SGND with the center tap connected to
OUTFB programs the minimum backup supply rail voltage
when input power is unavailable. This pin is nominally
1.2V when in backup and the synchronous controller is
not in current limit. To disable step-up mode tie OUTFB
to INTVCC.
SGND (Pin 8): Signal Ground. All small-signal and com-
pensation components should be connected to this pin,
which in turn connects to PGND at one point. This pin
should also Kelvin to the bottom plate of the capacitor
stack.
RT (Pin 9): Timing Resistor . The switching frequency of
the synchronous controller is set by placing a resistor , RT,
from this pin to SGND. This resistor is always required.
If not present the synchronous controller will not start.
GPI (Pin 10): General Purpose Input. The voltage on this
pin is digitized directly by the ADC. For high impedance
inputs an internal buffer can be selected and used to drive
the ADC. The GPI pin can be connected to a negative
temperature coefficient (NTC) thermistor to monitor the
temperature of the supercapacitor stack. A low drift bias
resistor is required from INTVCC to GPI and a thermistor
is required from GPI to ground. Connect GPI to SGND if
not used. The digitized voltage on this pin can be read in
the meas_gpi register .
ITST (Pin 11):  Programming Pin for Capacitance Test
Current. This current is used to partially discharge the
capacitor stack at a precise rate for capacitance measure-
ment. This pin servos to 1.2V during a capacitor measure-
ment. A resistor , RTST, from this pin to SGND programs
the test current. RTST must be at least 121ohm.
CAPRTN (Pin 12): Capacitor Stack Shunt Return Pin. This
pin is connected to the grounded bottom plate of the first
super capacitor in the stack through a shunt resistor .
CAP1 (Pin 13): First Supercapacitor Pin. The top plate of
the first supercapacitor and the bottom plate of the second
supercapacitor are connected to this pin through a shunt
resistor . CAP1 and CAPRTN are used to measure the volt-
age across the first super capacitor and to shunt current
around the capacitor to provide balancing and prevent
overvoltage. The voltage between this pin and CAPRTN
is digitized and can be read in the meas_vcap1 register .
CAP2 (Pin 14): Second Supercapacitor Pin. The top plate
of the second supercapacitor and the bottom plate of the
third supercapacitor are connected to this pin through a
```

### Page 11

```text
LTC3350
11
Rev. DFor more information www.analog.com
PIN FUNCTIONS
shunt resistor . CAP2 and CAP1 are used to measure the
voltage across the second supercapacitor and to shunt
current around the capacitor to provide balancing and pre-
vent overvoltage. If not used this pin should be shorted to
CAP1. The voltage between this pin and CAP1 is digitized
and can be read in the meas_vcap2 register .
CAP3 (Pin 15): Third Supercapacitor Pin. The top plate of
the third supercapacitor and the bottom plate of the fourth
supercapacitor are connected to this pin through a shunt
resistor . CAP3 and CAP2 are used to measure the volt -
age across the third supercapacitor and to shunt current
around the capacitor to provide balancing and prevent
overvoltage. If not used this pin should be shorted to
CAP2. The voltage between this pin and CAP2 is digitized
and can be read in the meas_vcap3 register .
CAP4 (Pin 16): Fourth Supercapacitor Pin. The top plate of
the fourth supercapacitor is connected to this pin through
a shunt resistor . CAP4 and CAP3 are used to measure the
voltage on the capacitor and to shunt current around the
supercapacitor to provide balancing and prevent overvolt-
age. If not used this pin should be shorted to CAP3. The
voltage between this pin and CAP3 is digitized and can
be read in the meas_vcap4 register . The capacitance test
current set by the ITST pin is pulled from this pin.
CFP (Pin 17):  VCAPP5 Charge Pump Flying Capacitor
Positive Terminal. Place a 0.1uF between CFP and CFN.
CFN (Pin 18):  VCAPP5 Charge Pump Flying Capacitor
Negative Terminal. Place a 0.1uF between CFP and CFN.
VCAPP5 (Pin 19):  Charge Pump Output. The internal
charge pump drives this pin to VCAP + INTV CC which is
used as the high side rail for the OUTFET gate drive and
charge current sense amplifier . Connect a 0.1uF capacitor
from VCAPP5 to VCAP .
OUTFET (Pin 20): Output Ideal Diode Gate Drive Output.
This pin controls the gate of an external N-channel
MOSFET used as an ideal diode between VOUT and VCAP.
The gate drive receives power from the internal charge
pump output VCAPP5. The source of the N-channel
MOSFET should be connected to VCAP and the drain
should be connected to VOUTSN. If the output ideal diode
MOSFET is not used, OUTFET should be left floating.
VCAP (Pin 21): Supercapacitor Stack Voltage and Charge
Current Sense Amplifier Negative Input. Connect this pin
to the top of the supercapacitor stack. The voltage at this
pin is digitized and can be read in the meas_vcap register .
ICAP (Pin 22): Charge Current Sense Amplifier Positive
Input. The ICAP and VCAP pins measure the voltage
across the sense resistor , RSNSC, to provide instantaneous
current signals for the control loops and ESR measure -
ment system. The maximum charge current is 32mV /
RSNSC.
VCC2P5 (Pin 23) : Internal 2.5V Regulator Output. This
regulator provides power to the internal logic circuitry.
Decouple this pin to ground with a minimum 1uF low ESR
tantalum or ceramic capacitor .
SW (Pin 24): Switch Node Connection to the Inductor . The
negative terminal of the boot-strap capacitor , CB, is con-
nected to this pin. The voltage on this pin is also used as
the source reference for the top side N-channel MOSFET
gate drive. In step-down mode, the voltage swing on
this pin is from a diode (external) forward voltage below
ground to V OUT. In step-up mode the voltage swing is
from ground to a diode forward voltage above VOUT.
TGATE (Pin 25):  Top Gate Driver Output. This pin is
the output of a floating gate driver for the top external
N-channel MOSFET . The voltage swing at this pin is
ground to VOUT + DRVCC.
BST (Pin 26): TGATE Driver Supply Input. The positive
terminal of the boot-strap capacitor , CB, is connected to
this pin. This pin swings from a diode voltage drop below
DRVCC up to VOUT + DRVCC.
BGATE (Pin 27):  Bottom Gate Driver Output. This pin
drives the bottom external N-channel MOSFET between
PGND and DRVCC.
```

### Page 12

```text
LTC3350
12
Rev. D For more information www.analog.com
PIN FUNCTIONS
DRVCC (Pin 28) : Power Rail for Bottom Gate Driver .
Connect to INTVCC or to an external supply. Decouple this
pin to ground with a minimum 2.2uF low ESR tantalum or
ceramic capacitor . Do not exceed 5.5V on this pin.
INTVCC (Pin 29): Internal 5V Regulator Output. The con-
trol circuits and gate drivers (when connected to DRVCC)
are powered from this supply. If not connected to DRVCC,
decouple this pin to ground with a minimum 1uF low ESR
tantalum or ceramic capacitor .
VOUTSN (Pin 30):  Input Current Limiting Amplifier
Negative Input. A sense resistor , RSNSI, between VOUTSP
and VOUTSN sets the input current limit. The maximum
input current is 32mV/RSNSI. An RC network across the
sense resistor can be used to modify loop compensation.
To disable input current limit, connect this pin to VOUTSP .
VOUTSP (Pin 31):  Backup System Supply Voltage and
Input Current Limiting Amplifier Positive Input. The volt-
age across the VOUTSP and VOUTSN pins are used to
regulate input current. This pin also serves as the power
supply for the IC. The voltage at this pin is digitized and
can be read in the meas_vout register .
VOUTM5 (Pin 32): VOUT - 5V Regulator . This pin is regu-
lated to 5V below V OUT or to ground if V OUT < 5V. This
rail provides power to the input current sense amplifier .
Decouple this pin with at least 1uF to VOUT.
INFET (Pin 33): Input Ideal Diode Gate Drive Output. This
pin controls the gate of an external N-channel MOSFET
used as an ideal diode between V IN and VOUT. The gate
drive receives power from an internal charge pump. The
source of the N-channel MOSFET should be connected
to VIN and the drain should be connected to VOUTSP . If
the input ideal diode MOSFET is not used, INFET should
be left floating.
VIN (Pin 34): External DC Power Source Input. Decouple
this pin with at least 0.1uF to ground. The voltage at this
pin is digitized and can be read in the meas_vin register .
CAP_SLCT0, CAP_SLCT1 (Pins 35, 36): CAP_SLCT0 and
CAP_SLCT1 set the number of super-capacitors used.
Refer to Table 1 in the Applications Information section.
PFI (Pin 37): Power-Fail Comparator Input. When the volt-
age at this pin drops below 1.17V, PFO is pulled low and
step-up mode is enabled.
PFO (Pin 38): Power-Fail Status Output. This open-drain
output is pulled low when a power fault has occurred.
PGND (Exposed Pad Pin 39): Power Ground. The exposed
pad must be connected to a continuous ground plane on
the second layer of the printed circuit board by several
vias directly under the LTC3350 for rated thermal perfor-
mance. It must be tied to the SGND pin.
```

### Page 13

```text
LTC3350
13
Rev. DFor more information www.analog.com
BLOCK DIAGRAM
+ -
+ - +-
30mV
30mV
INTVCC
VREF
vcapfb_dac[3:0]
Vcapfb_dac
Vcapfb_dac
VIN
CAPFB
OUTFB
VC
RT
INTVCC
INFET VOUTSP VOUTM5 VOUTSN
+
-
x37.5
+
-
x37.5IIN
ICHG
5V LDO
-5V LDO
D/A
A/D
VREF
INTVCC
INTVCC
+
-
VREF
+
-
VREF
VOUTSP
IREF
+
- +
-
OUTFET CFM
VCAPP5
CFP
VCAP
ICAP
BST
TGATE
SW
+-
CHARGE
PUMP
DRVCC
BGATE
CAP4
BIDIRECTIONAL
SWITCHING
CONTROLLER
LOGIC
VCC2P5
IIN
ICHG
VCAP
VOUT
VIN
CAP4
CAP3
CAP2
CAP1
CAPRTN
DTEMP
CAPGD
PFI
GPI
SGND
BANDGAP VREF
OSC
2.5V LDO
SHUNT
CONTROLLER
CAP3
BALANCER
SHUNT
CONTROLLER
CAP2
BALANCER
SHUNT
CONTROLLER
CAP1
BALANCER
SHUNT
CONTROLLER
CAPRTN
ITST
BALANCER
PFO
+
-
VREF
3350 BD
GPIBUF
+
-
VREF
CAPFB
MUL TIPLEXER
+
-
CAP_SLCT0
CAP_SLCT1
SMBALERT
SDA
SCL
+
-
34 33 31 32 30 20 17 18
19
21
22
26
25
24
28
27
16
15
14
13
12
11
10
8 PGND 39
1
2
3
36
35
38
37
4
23
29
9
5
7
6
```

### Page 14

```text
LTC3350
14
Rev. D For more information www.analog.com
OPERATION
TIMING DIAGRAM
Introduction
The LTC3350 is a highly integrated backup power control-
ler and system monitor . It features a bidirectional switching
controller , input and output ideal diodes, supercapacitor
shunts/balancers, a power-fail comparator , a 14-bit ADC
and I2C/SMBus programmability with status reporting.
If VIN is above an externally programmable PFI threshold
voltage, the synchronous controller operates in step-down
mode and charges a stack of supercapacitors. A program-
mable input current limit ensures that the supercapaci -
tors will automatically be charged at the highest possible
charge current that the input can support. If VIN is below
the PFI threshold, then the synchronous controller will run
in reverse as a step-up converter to deliver power from
the supercapacitor stack to VOUT.
The two ideal diode controllers drive external MOSFETs to
provide low loss power paths from VIN and VCAP to VOUT.
The ideal diodes work seamlessly with the bidirectional
controller to provide power from the supercapacitors to
VOUT without back driving VIN.
The LTC3350 provides balancing and overvoltage protec-
tion to a series stack of one to four supercapacitors. The
internal capacitor voltage balancers eliminate the need
for external balance resistors. Overvoltage protection is
provided by shunt regulators that use an internal switch
and an external resistor across each supercapacitor .
The LTC3350 monitors system voltages, currents, and
die temperature. A general purpose input (GPI) pin is
provided to measure an additional system parameter or
implement a thermistor measurement. In addition, the
LTC3350 can measure the capacitance and resistance
of the supercapacitor stack. This provides indication of
the health of the supercapacitors and, along with the
VCAP voltage measurement, provides information on the
total energy stored and the maximum power that can be
delivered.
Bidirectional Switching Controller-Step-Down Mode
The bidirectional switching controller is designed to charge
a series stack of supercapacitors (Figure 1). Charging pro-
ceeds at a constant current until the supercapacitors reach
their maximum charge voltage determined by the CAPFB
servo voltage and the resistor divider between V CAP and
CAPFB. The maximum charge current is determined by
the value of the sense resistor , RSNSC, used in series with
the inductor . The charge current loop servos the volt -
age across the sense resistor to 32mV. When charging
begins, an internal soft-start ramp will increase the charge
current from zero to full current in 2ms. The VCAP voltage
and charge current can be read from the meas_vcap and
meas_ichrg registers, respectively.
SDA
SCL
S Sr P S
tHD(SDA)
S = START ,  Sr = REPEATED START ,  P = STOP
tHD(DAT)
tSU(STA) tSU(STO)
tSU(DAT)tLOW tHD(SDA)
tSP
tBUF
tr tf trtf
tHIGH
3350 TD
Definition of Timing for F/S Mode Devices on the I2C Bus
```

### Page 15

```text
LTC3350
15
Rev. DFor more information www.analog.com
OPERATION
+
+
+
+
+-
+
-
+ -
30mV
INPUT
CURRENT
CONTROLLER
CHARGE
CURRENT
CONTROLLER
BIDIRECTIONAL
SWITCHING
CONTROLLER
STEP-DOWN MODE
VREF
IIN
VIN
VIN
L TC3350 INFET VOUTSP VOUTSN
VOUT
(TO SYSTEM)
TGATE
ICHG
BGATE
ICAP
VCAP
RSNSC
RSNSI
3350 F01
+
-
IREF
VREF
CAPACITOR
VOL TAGE
CONTROLLER
+
-
+
-
CAPFB
VC
37.5
D/A
vcapfb_dac[3:0]
+
-
Figure 1. Power Path Block Diagram-Power Available from V IN
The LTC3350 provides constant power charging (for
a fixed V IN) by limiting the input current drawn by the
switching controller in step-down mode. The input cur -
rent limit will reduce charge current to limit the voltage
across the input sense resistor , RSNSI, to 32mV. If the
combined system load plus supercapacitor charge cur -
rent is large enough to cause the switching controller to
reach the programmed input current limit, the input cur-
rent limit loop will reduce the charge current by precisely
the amount necessary to enable the external load to be
satisfied. Even if the charge current is programmed to
exceed the allowable input current, the input current will
not be violated;  the supercapacitor charger will reduce
its current as needed. Note that the part's quiescent and
gate drive currents are not included in the input current
measurement. The input current can be read from the
meas_iin register .
Bidirectional Switching Controller-Step-Up Mode
The bidirectional switching controller acts as a step-up
converter to provide power from the supercapacitors to
VOUT when input power is unavailable (Figure 2). The PFI
comparator enables step-up mode. VOUT regulation is set
by a resistor divider between VOUT and OUTFB. To disable
step-up mode tie OUTFB to INTVCC.
Step-up mode can be used in conjunction with the output
ideal diode. The VOUT regulation voltage can be set below
the capacitor stack voltage. Upon removal of input power,
power to VOUT will be provided from the supercapacitor
stack via the output ideal diode. VCAP and VOUT will fall as
the load current discharges the supercapacitor stack. The
output ideal diode will shut off when the voltage on OUTFB
falls below 1.3V and VOUT will fall a PN diode (~700mV)
below VCAP. If OUTFB falls below 1.2V when the output
```

### Page 16

```text
LTC3350
16
Rev. D For more information www.analog.com
OPERATION
+
+
+
+
+-
+
-
30mV
OUTPUT
VOL TAGE
CONTROLLER
BIDIRECTIONAL
SWITCHING
CONTROLLER
STEP-UP MODE
VREF
L TC3350VOUTSN
VOUT
(TO SYSTEM)
VCAP > VOUT
VCAP < VOUT
TGATE
OUTFET
OUTFB
BGATE
ICAP
VCAP
RSNSC
3350 F02
VC
+
-
Figure 2. Power Path Block Diagram-Power Backup
ideal diode shuts off, the synchronous controller will turn
on immediately. If OUTFB is above 1.2V when the output
ideal diode shuts off, the load current will flow through
the body diode of the output ideal diode N-channel
MOSFET for a period of time until OUTFB falls to 1.2V. The
synchronous controller will regulate OUTFB to 1.2V when
it turns on, holding up V OUT while the supercapacitors
discharge to ground.
The synchronous controller in step-up mode will run
nonsynchronously when VCAP is less than 100mV below
VOUT. It will run synchronously when V CAP falls 200mV
below VOUT.
Ideal Diodes
The LTC3350 has two ideal diode controllers that drive
external N-channel MOSFETs. The ideal diodes consist of
a precision amplifier that drives the gates of N-channel
MOSFETs whenever the voltage at VOUT is approximately
30mV (VFWD) below the voltage at V IN or V CAP. Within
the amplifier's linear range, the small-signal resistance
of the ideal diode will be quite low, keeping the forward
drop near 30mV. At higher current levels, the MOSFETs
will be in full conduction.
The input ideal diode prevents the supercapacitors from
back driving V IN during backup mode. A Fast-Off com -
parator shuts off the N-channel MOSFET if V IN falls
30mV below VOUT. The PFI comparator also shuts off the
MOSFET during power failure.
The output ideal diode provides a path for the supercapac-
itors to power VOUT when VIN is unavailable. In addition
to a Fast-Off comparator , the output ideal diode also has
a Fast-On comparator that turns on the external MOSFET
when VOUT drops 65mV  below V CAP. The output ideal
diode will shut off when OUTFB is just above regulation
allowing the synchronous controller to power V OUT in
step-up mode.
```

### Page 17

```text
LTC3350
17
Rev. DFor more information www.analog.com
OPERATION
Gate Drive Supply (DRVCC)
The bottom gate driver is powered from the DRV CC pin.
It is normally connected to the INTV CC pin. An external
LDO can also be used to power the gate drivers to mini -
mize power dissipation inside the IC. See the Applications
Information section for details.
Undervoltage Lockout (UVLO)
Internal undervoltage lockout circuits monitor both the
INTVCC and DRVCC pins. The switching controller is kept
off until INTVCC rises above 4.3V and DRVCC rises above
4.2V. Hysteresis on the UVLOs turn off the controller if
either INTVCC falls below 4V or DRVCC falls below 3.9V.
Charging is not enabled until VOUTSN is 185mV above the
supercapacitor voltage and V IN is above the PFI thresh -
old. Charging is disabled when VOUTSN falls to within
90mV of the supercapacitor voltage or V IN is below the
PFI threshold.
RT Oscillator and Switching Frequency
The RT pin is used to program the switching frequency.
A resistor , RT, from this pin to ground sets the switching
frequency according to:

fSW MHz( ) = 53.5
RT kohm( )
RT also sets the scale factor for the capacitor measure -
ment value reported in the meas_cap register , described
in the  Capacitance and ESR Measurement section of this
data sheet.
Input Overvoltage Protection
The LTC3350 has overvoltage protection on its input.
If VIN exceeds 38.6V, the switching controller will hold
the switching MOSFETs off. The controller will resume
switching if VIN falls below 37.2V. The input ideal diode
MOSFET remains on during input overvoltage.
VCAP DAC
The feedback reference for the CAPFB servo point can be
programmed using an internal 4-bit digital-to-analog con-
verter (DAC). The reference voltage can be programmed
from 0.6375V to 1.2V in 37.5mV increments. The DAC
defaults to full scale (1.2V) and is programmed via the
vcapfb_dac register .
Supercapacitors lose capacitance as they age. By initially
setting the V CAP DAC to a low setting, the final charge
voltage on the supercapacitors can be increased as they
age to maintain a constant level of stored backup energy
throughout the lifetime of the supercapacitors.
Power-Fail (PF) Comparator
The LTC3350 contains a fast power-fail (PF) comparator
which switches the part from charging to backup mode
in the event the input voltage, V IN, falls below an exter -
nally programmed threshold voltage. In backup mode, the
input ideal diode shuts off and the supercapacitors power
the load either directly through the output ideal diode or
through the synchronous controller in step-up mode.
The PF comparator threshold voltage is programmed by
an external resistor divider via the PFI pin. The output of
the PF comparator also drives the gate of an open-drain
NMOS transistor to report the status via the PFO pin.
When input power is available the PFO pin is high imped-
ance. When VIN falls below the PF comparator threshold,
PFO is pulled down to ground.
The output of the PF comparator may also be read from
the chrg_pfo bit in the chrg_status register .
Charge Status Indication
The LTC3350 includes a comparator to report the status
of the supercapacitors via an open-drain NMOS transistor
on the CAPGD pin. This pin is pulled to ground until the
CAPFB pin voltage rises to within 8% of the V CAP DAC
setting. Once the CAPFB pin is above this threshold, the
CAPGD pin goes high impedance.
The output of this comparator may also be read from the
chrg_cappg bit in the chrg_status register .
Capacitor Voltage Balancer
The LTC3350 has an integrated active stack balancer . This
balancer slowly balances all of the capacitor voltages to
within about 10mV of each other . This maximizes the life
of the supercapacitors by keeping the voltage on each as
```

### Page 18

```text
LTC3350
18
Rev. D For more information www.analog.com
OPERATION
low as possible to achieve the needed total stack volt -
age. When the difference between any two capacitor volt-
ages exceeds about 10mV, the capacitor with the largest
voltage is discharged with a resistive balancer at about
10mA until all capacitor voltages are within 10mV. The
balancers are disabled in backup mode.
Capacitor Shunt Regulators
In addition to balancing, there is a need to protect each
capacitor from overvoltage during charging. The capaci-
tors in the stack will not have exactly the same capaci -
tance due to manufacturing tolerances or uneven aging.
This will cause the capacitor voltages to increase at differ-
ent rates with the same charge current. If this mismatch
is severe enough or if the capacitors are being charged
to near their maximum voltage, it becomes necessary
to limit the voltage increase on some capacitors while
still charging the other capacitors. Up to 500mA of cur -
rent may be shunted around a capacitor whose voltage is
approaching the programmable shunt voltage. This shunt
current reduces the charge rate of that capacitor rela -
tive to the other capacitors. If a capacitor continues to
approach its shunt voltage, the charge current is reduced.
This protects the capacitor from overvoltage while still
charging the other capacitors, although at a reduced rate
of charge. The shunt voltage is programmable in the
vshunt register . Shunt voltages up to 3.6V may be pro -
grammed in 183.5uV increments. The shunt regulators
can be disabled by programming vshunt to zero (0x0000).
The default value is 0x3999, resulting in a shunt voltage
of 2.7V.
I2C/SMBus and SMBALERT
The LTC3350 contains an I 2C/SMBus port. This port
allows communication with the LTC3350 for configura -
tion and reading back telemetry data. The port supports
two SMBus formats, read word and write word. Refer
to the SMBus specification for details of these formats.
The registers accessible via this port are organized on an
8-bit address bus and each register is 16 bits wide. The
"command code" (or sub-address) of the SMBus read/
write word formats is the 8-bit address of each of these
registers. The address of the LTC3350 is 0b0001001.
The SMBALERT pin is asserted (pulled low) whenever an
enabled limit is exceeded or when an enabled status event
happens (see Limit Check and Alarms and Monitor Status
Register). The LTC3350 will deassert the SMBALERT
pin only after responding to an SMBus alert response
address (ARA), an SMBus protocol used to respond to a
SMBALERT . The host will read from the ARA (0b0001100) and
each part asserting SMBALERT will begin to respond with its
address. The responding parts arbitrate in such a way that only
the part with the lowest address responds. Only when a part
has responded with its address does it release the SMBALERT
signal. If multiple parts are asserting the SMBALERT signal
then multiple reads from the ARA are needed. For more infor-
mation refer to the SMBus specification.
Details on the registers accessible through this interface
are available in the Register Map and Register Descriptions
sections of this data sheet.
Analog-to-Digital Converter
The LTC3350 has an integrated 14-bit sigma-delta analog-
to-digital converter (ADC). This converter is automatically
multiplexed between all of the measured channels and
its results are stored in registers accessible via the I 2C/
SMBus port. There are 11 channels measured by the ADC,
each of which takes approximately 1.6ms to measure. In
addition to providing status information about the system
voltages and currents, some of these measurements are
used by the LTC3350 to balance, protect, and measure
the capacitors in the stack.
The result of the analog-to-digital conversion is stored in
a 16-bit register as a signed, two's complement number .
The lower two bits of this number are sub-bits. These bits
are ADC outputs which are too noisy to be reliably used
on any single conversion, however , they may be included
if multiple samples are averaged.
The measurements from the ADC are directly stored in the
meas_vcap1, meas_vcap2, meas_vcap3, meas_vcap4,
meas_gpi, meas_vin, meas_vcap, meas_vout, meas_iin,
meas_ichg and meas_dtemp registers.
Capacitance and ESR Measurement
The LTC3350 has the ability to measure the capaci -
tance and equivalent series resistance (ESR) of its
```

### Page 19

```text
LTC3350
19
Rev. DFor more information www.analog.com
OPERATION
supercapacitor stack. This measurement is performed
with minimal impact to the system, and can be done
while the supercapacitor backup system is online. This
measurement discharges the capacitor stack by a small
amount (200mV). If input power fails during this test, the
part will go into backup mode and the test will terminate.
The capacitance test is performed only once the super -
capacitors have finished charging. The test temporarily
disables the charger , then discharges the supercapaci -
tors by 200mV with a precision current. The  discharge
time is measured and used to calculate the capacitance
with the result of this measurement stored in the meas_
cap register . The number reported is proportional to the
capacitance of the entire stack. T wo different scales can
be set using the ctl_cap_scale bit in the ctl_reg register . If
ctl_cap_scale is set to 0 (for large value capacitor stacks),
use the following equation to convert the meas_cap value
to Farads:

CSTACK = RT
RTST
- 336uF - meas _ cap
If ctl_cap_scale is set to 1 (for small value capacitor
stacks), use the following equation to convert the meas_
cap value to Farads:

CSTACK = RT
RTST
- 3.36uF - meas _ cap
In the two previous equations RT is the resistor on the RT
pin and RTST is the resistor on the ITST pin.
The ESR test is performed immediately following the
capacitance test. The switching controller is switched on
and off several times. The changes in charge current and
stack voltage are measured. These measurements are
used to calculate the ESR relative to the charge current
sense resistor . The result of this measurement is stored
in the meas_esr register . The value reported in meas_esr
can be converted to ohms using the following equation:

RESR = RSNSC
64 - meas _ esr
where RSNSC is the charge current sense resistor in series
with the inductor .
The capacitance and capacitor ESR measurements do not
automatically run as the other measurements do. They
must be initiated by setting the ctl_strt_capesr bit in the
ctl_reg register . This bit will automatically clear once the
measurement begins. If the cap_esr_per register is set to
a non-zero value, the measurement will be repeated after
the time programmed in the cap_esr_per register . Each
LSB in the cap_esr_per register represents 10 seconds.
The capacitance and ESR measurements may fail to com-
plete for several reasons, in which case the respective
mon_cap_failed or mon_esr_failed bit will be set. The
capacitance test may fail due to a power failure or if the
200mV discharge trips the CAPGD comparator . The ESR
test will also fail if the capacitance test fails. The ESR test
uses the charger to supply a current and then measures
the supercapacitor stack voltage with and without that cur-
rent. If the ESR is greater than 1024 times RSNSC, the ESR
measurement will fail. The ESR measurement is adaptive;
it uses knowledge of the ESR from previous measurements
to program the test current. The capacitance and ESR tests
should initially be run several times when first powering up
to get the most accuracy out of the system. It is possible
for the first few measurements to give low quality results
or fail to complete and after running several times will com-
plete with a quality result. The leakage on supercapacitors
is initially very high after being charged. Many supercapaci-
tor manufacturers specify the leakage current after being
charged for 72 hours. It is expected that capacitor measure-
ments conducted prior to this time will read low.
Monitor Status Register
The LTC3350 has a monitor status register (mon_status)
which contains status bits indicating the state of the capaci-
tance and ESR monitoring system. These bits are set and
cleared by the capacitor monitor upon certain events dur-
ing a capacitor and ESR measurement, as described in the
Capacitance and ESR Measurement section.
There is a corresponding msk_mon_status regis -
ter . Writing a one to any of these bits will cause the
SMBALERT pin to pull low when the corresponding bit
in the msk_mon_status register has a rising edge. This
allows reduced polling of the LTC3350 when waiting for
a capacitance or ESR measurement to complete.
```

### Page 20

```text
LTC3350
20
Rev. D For more information www.analog.com
OPERATION
Details of the mon_status and msk_mon_status registers
can be found in the Register Descriptions section of this
data sheet.
Charge Status Register
The LTC3350 charger status register (chrg_status) con-
tains data about the state of the charger , switcher , shunts,
and balancers. Details of this register may be found in the
Register Description sections of this data sheet.
Limit Checking and Alarms
The LTC3350 has a limit checking function that will check
each measured value against I2C/SMBus programmable
limits. This feature is optional, and all the limits are dis -
abled by default. The limit checking is designed to simplify
system monitoring, eliminating the need to continuously
poll the LTC3350 for measurement data.
If a measured parameter goes outside of the programmed
level of an enabled limit, the associated bit in the alarm_reg
register is set high and the SMBALERT pin is pulled low.
This informs the I2C/SMBus host a limit has been exceeded.
The alarms register may then be read to determine exactly
which programmed limits have been exceeded.
A single ADC is shared between the 11 channels with about
18ms between consecutive measurements of the same
channel. In a transient condition, it is possible for these
parameters to exceed their programmed levels in between
consecutive ADC measurements without setting the alarm.
Once the LTC3350 has responded to an SMBus ARA the
SMBALERT pin is released. The part will not pull the pin
low again until another limit is exceeded. To reset a limit
that has been exceeded, it must be cleared by writing a
one to the respective bit in the clr_alarms register .
A number of the LTC3350's registers are used for limit
checking. Individual limits are enabled or disabled in the
msk_alarms registers. Once an enabled alarm's measured
value exceeds the programmed level for that alarm the
alarm is set. That alarm may be cleared by writing a one to
the appropriate bit of the clr_alarms register or by writing
a zero to the appropriate bit to the msk_alarms register . All
alarms that have been set and have not yet been cleared
may be read in the alarm_reg register .
All of the individual measured voltages have a corre -
sponding undervoltage (UV) and overvoltage (OV) alarm
level. All of the individual capacitor voltages are com -
pared to the same alarm levels, set in the cap_ov_lvl and
cap_uv_lvl registers. The input current measurement has
an overcurrent (OC) alarm programmed in the iin_oc_lvl
register . The charge current has an undercurrent alarm
programmed in the ichg_uc_lvl register .
Die Temperature Sensor
The LTC3350 has an integrated die temperature sensor
monitored by the ADC and digitized to the meas_dtemp
register . An alarm may be set on die temperature by set-
ting the dtemp_cold_lvl and/or dtemp_hot_lvl registers
and enabling their respective alarms in the msk_alarms
register . To convert the code in the meas_dtemp register
to degrees Celsius use the following:
 T DIE ( degC) = 0.028 - meas_dtemp - 251.4
General Purpose Input
The general purpose input (GPI) pin can be used to mea-
sure an additional system parameter . The voltage on this
pin is directly digitized by the ADC. For high impedance
inputs, an internal buffer may be selected and used to
drive the ADC. This buffer is enabled by setting the ctl_
gpi_buffer_en bit in the ctl_reg register . With this buffer ,
the input range is limited from 0V to 3.5V. If this buffer is
not used, the range is from 0V to 5V, however , the input
stage of the ADC will draw about 0.4uA per volt from this
pin. The ADC input is a switched capacitor amplifier run-
ning at about 1MHz, so this current draw will be at that
frequency. The pin current can be eliminated at the cost of
reduced range and increased offset by enabling the buffer .
Alarms are available for this pin voltage with levels pro -
grammed using the gpi_uv_lvl and gpi_ov_lvl registers.
These alarms are enabled using the msk_gpi_uv and
msk_gpi_ov bits in the msk_alarms register .
To monitor the temperature of the supercapacitor stack,
the GPI pin can be connected to a negative temperature
coefficient (NTC) thermistor . A low drift bias resistor is
required from INTVCC to GPI and a thermistor is required
from GPI to ground. Connect GPI to SGND if not used.
```

### Page 21

```text
LTC3350
21
Rev. DFor more information www.analog.com
APPLICATIONS INFORMATION
Digital Configuration
Although the LTC3350 has extensive digital features, only
a few are required for basic use. The shunt voltage should
be programmed via the vshunt register if a value other
than the default 2.7V is required. The capacitor voltage
feedback reference defaults to 1.2V; it may be changed
in the vcapfb_dac register .
All other digital features are optional and used for moni-
toring. The ADC automatically runs and stores conver-
sions to registers (e.g., meas_vcap ). Capacitance and
ESR measurements only run if requested, however , they
may be scheduled to repeat if desired (ctl_strt_capesr and
cap_esr_per). Each measured parameter has programma-
ble limits (e.g., vcap_uv_lvl and vcap_ov_lvl) which may
trigger an alarm and SMBALERT when enabled. These
alarms are disabled by default.
Capacitor Configuration
The LTC3350 may be used with one to four supercapaci-
tors. If less than four capacitors are used, the capacitors
must be populated from CAPRTN to CAP4, and the unused
CAP pins must be tied to the highest used CAP pin. For
example, if three capacitors are used, CAP4 should be
tied to CAP3. If only two capacitors are used, both CAP4
and CAP3 should be tied to CAP2. The number of capaci-
tors used must be programmed on the CAP_SLCT0 and
CAP_SLCT1 pins by tying the pins to VCC2P5 for a one
and ground for a zero as shown in Table 2. The value
programmed on these pins may be read back from the
num_caps register via I2C/SMBus.
Table 1.
CAP_SLCT1 CAP_SLCT0
num_caps
REGISTER VALUE
NUMBER OF
CAPACITORS
0 0 0 1
0 1 1 2
1 0 2 3
1 1 3 4
Capacitor Shunt Regulator Programming
VSHUNT is programmed via the I 2C/SMBus interface and
defaults to 2.7V at initial power-up. VSHUNT serves to limit
the voltage on any individual capacitor by turning on a
shunt around that capacitor as the voltage approaches
VSHUNT. CAPRTN, CAP1, CAP2, CAP3 and CAP4 must be
connected to the supercapacitors through resistors which
serve as ballasts for the internal shunts. The shunt cur -
rent is approximately VSHUNT divided by twice the shunt
resistance value. For a V SHUNT of 2.7V, 2.7ohm resistors
should be used for 500mA of shunt current. The shunts
have a duty cycle of up to 75%. The power dissipated in
a single shunt resistor is approximately:

PSHUNT  3VSHUNT
2
16RSHUNT
and the resistors should be sized accordingly. If the
shunts are disabled, make RSHUNT 100ohm.
Since the shunt current is less than what the switcher can
supply, the on-chip logic will automatically reduce the
charging current to allow the shunt to protect the capaci-
tor . This greatly reduces the charge rate once any one
shunt is activated. For this reason, VSHUNT should be pro-
grammed as high as possible to reduce the likelihood of it
activating during a charge cycle. Ideally, VSHUNT would be
set high enough so that any likely capacitor mismatches
would not cause the shunts to turn on. This keeps the
charger operating at the highest possible charge current
and reduces the charge time. If the shunts never turn
on, the charge cycle completes quickly and the balanc -
ers eventually equalize the voltage on the capacitors. The
shunt setting may also be used to discharge the capaci -
tors for testing, storage or other purposes.
Setting Input and Charge Currents
The maximum input current is determined by the resis -
tance across the VOUTSP and VOUTSN pins, RSNSI. The
maximum charge current is determined by the value of
the sense resistor , RSNSC, used in series with the induc -
tor . The input and charge current loops servo the voltage
across their respective sense resistor to 32mV. Therefore,
the maximum input and charge currents are:

IIN(MAX) = 32mV
RSNSI
ICHG(MAX) = 32mV
RSNSC
```

### Page 22

```text
LTC3350
22
Rev. D For more information www.analog.com
APPLICATIONS INFORMATION
The peak inductor current limit, IPEAK, is 80% higher than
the maximum charge current and is equal to:

IPEAK = 58mV
RSNSC
Note that the input current limit does not include the
part's quiescent and gate drive currents. The total cur -
rent drawn by the part will be IIN(MAX) + IQ + IG, where IQ
is the non-switching quiescent current and IG is the gate
drive current.
Low Current Charging and High Current Backup
The LTC3350 can accommodate applications requiring
low charge currents and high backup currents. In these
applications, program the desired charge current using
RSNSI. The higher current needed during backup can be
set using R SNSC. The input current limit will override
the charge current limit when the supercapacitors are
charging while the charge current limit provides sufficient
current capability for backup operation.
The charge current will be limited to I CHG(MAX) at low
VCAP (i.e., low duty cycles). As V CAP rises, the switch -
ing controller's input current will increase until it reaches
IIN(MAX). The input current will be maintained at I IN(MAX)
and the charge current will decrease as VCAP rises further .
Some applications may want to use only a portion of the
input current limit to charge the supercapacitors. T wo
input current sense resistors placed in series can be used
to accomplish this as shown in Figure 3. VOUTSP is kelvin
connected to the positive terminal of RSNSI1 and VOUTSN
is kelvin connected to the negative terminal of R SNSI2.
The load current is pulled across R SNSI1 while the input
current to the charger is pulled across RSNSI1 and RSNSI2.
The input current limit is:
 32mV = RSNSI1 - ILOAD + (RSNSI1 + RSNSI2) - IINCHG
For example, suppose that only 2A of input current is
desired to charge the supercapacitors but the system load
and charger combined can pull a total of up to 4A from the
supply.  Setting RSNSI1 = RSNSI2 = 8mohm will set a 4A cur-
rent limit for the load + charger while setting a 2A limit for
the charger .  With no system load, the charger can pull up
to 2A of input current. As the load pulls 0A to 4A of current
the charger's input current will reduce from 2A down to 0A.
The following equation can be used to determine charging
input current as a function of system load current:

IINCHG = 32mV
RSNSI1 + RSNSI2
- RSNSI1
RSNSI1 + RSNSI2
-ILOAD
The contact resistance of the negative terminal of RSNSI1
and the positive terminal of R SNSI2 as well as the resis-
tance of the trace connecting them will cause variability
in the input current limit. To minimize the error , place both
input current sense resistors close together with a large
PCB pad area between them as the system load current is
pulled from the trace connecting the two sense resistors.
Note that the backup current will flow through RSNSI2. The
RSNSI2 package should be sized accordingly to handle the
power dissipation.
Figure 3.
VIN
VIN
INFET VOUTSP
RSNSI1 RSNSI2
L TC3350
VOUTSN
IINCHG
ILOAD
VOUT (TO SYSTEM)
TGATE
BGATE
3350 F03
Setting VCAP Voltage
The LTC3350 VCAP voltage is set by an external feedback
resistor divider , as shown in Figure 4. The regulated out-
put voltage is determined by:

VCAP = 1+ RFBC1
RFBC2

CAPFBREF
where CAPFBREF is the output of the V CAP DAC, pro-
grammed in the vcapfb_dac register . Great care should be
taken to route the CAPFB line away from noise sources,
such as the SW line.
Power-Fail Comparator Input Voltage Threshold
The input voltage threshold below which the power-fail
status pin, PFO, indicates a power-fail condition and the
```

### Page 23

```text
LTC3350
23
Rev. DFor more information www.analog.com
APPLICATIONS INFORMATION
LTC3350 bidirectional controller switches to step-up
mode is programmed using a resistor divider from the
VIN pin to SGND via the PFI pin such that:

VIN = 1+ RPF1
RPF2

VPFI(TH)
where VPFI(TH) is 1.17V. Typical values for RPF1 and RPF2
are in the range of 40k to 1M. See Figure 5.
The input voltage above which the power-fail status pin
PFO is high impedance and the bidirectional controller
switches to step-down mode is:

VIN = 1+ RPF1
RPF2

VPFI(TH) + VPFI(HYS)( )
where VPFI(HYS) is the hysteresis of the PFI comparator
and is equal to 30mV.
MN1 and MP1 can be implemented with a single pack -
age N-channel and P-channel MOSFET pair such as the
Si1555DL or Si1016CX. The drain leakage current of MN1,
when its gate voltage is at ground, can introduce an offset
in the threshold. To minimize the effect of this leakage cur-
rent RPF1, RPF2 and RPF3 should be between 1k and 100k.
Setting VOUT Voltage in Backup Mode
The output voltage for the controller in step-up mode is
set by an external feedback resistor divider , as shown in
Figure 7. The regulated output voltage is determined by:

VOUT = 1+ RFBO1
RFBO2

1.2V
Great care should be taken to route the OUTFB line away
from noise sources, such as the SW line.
Figure 7. V OUT Voltage Divider and Compensation Network
Figure 4. V CAP Voltage Feedback Divider
L TC3350
CAPFB
VCAP
RFBC1
RFBC2
3350 F04
L TC3350
PFI
VIN
RPF1
RPF2
3350 F05
Figure 5. PFI Threshold Voltage Divider
Figure 6. PFI Threshold Divider with Added Hysteresis
Additional hysteresis can be added by switching in an
additional resistor , RPF3, in parallel with R PF2 when the
voltage at PFI falls below 1.17V as shown in Figure 6. The
falling VIN threshold is the same as before but the rising
VIN threshold becomes:

VIN = 1+ RPF1
RRP2
+ RPF1
RPF3

VPFI(TH) + VPFI(HYST)( )
VC
OUTFB
L TC3350
VREF RC
(OPT)
RFBO1
RFBO2
RFO
(OPT)
CFO
(OPT)
CFBO1
VOUT
CC
+
-
3350 F07
L TC3350
PFI
VDD
PFO
VIN
RPF1
RPF2
RPF3
MP1
MN1
3350 F06
```

### Page 24

```text
LTC3350
24
Rev. D For more information www.analog.com
APPLICATIONS INFORMATION
Compensation
The input current, charge current, VCAP voltage, and VOUT
voltage loops all require a 1nF to 10nF capacitor from the
VC node to ground. When using the output ideal diode and
backing up to low voltages (<8V) use 8.2nF to 10nF on
VC. When not using the output ideal diode 4.7nF to 10nF
on VC is recommended. For very high backup voltages
(>15V) 1nF to 4.7nF is recommended.
In addition to the VC node capacitor , the VOUT voltage loop
requires a phase-lead capacitor , CFBO1, for stability and
improved transient response during input power failure
(Figure 7). The product of the top divider resistor and the
phase-lead capacitor should be used to create a zero at
approximately 2kHz:

RFBO1 - CFBO1 1
2pi 2kHz( )
Choose an R FBO1 such that C FBO1 is >=  100pF to mini -
mize the effects of parasitic pin capacitance. Because the
phase-lead capacitor introduces a larger ripple at the input
of the VOUT transconductance amplifier , an additional RC
lowpass filter from the V OUT divider to the OUTFB pin
may be needed to eliminate voltage ripple spikes. The
filter time constant should be located at the switching
frequency of the synchronous controller:

RFO - CFO = 1
2pifSW
with CFO > 10pF to minimize the effects of parasitic pin
capacitance. For back up applications where the VOUT reg-
ulation voltage is low (~5V to 6V), an additional 1k to 3k
resistor , RC, in series with the VC capacitor can improve
stability and transient response.
Minimum VCAP Voltage in Backup Mode
In backup mode, power is provided to the output from the
supercapacitors either through the output ideal diode or
the synchronous controller operating in step-up mode.
The output ideal diode provides a low loss power path
from the supercapacitors to V OUT. The minimum inter -
nal (open-circuit) supercapacitor voltage will be equal to
the minimum VOUT necessary for the system to operate
plus the voltage drops due to the output ideal diode and
equivalent series resistance, RSC, of each supercapacitor
in the stack.
Example: System needs 5V to run and draws 1A during
backup. There are four supercapacitors in the stack, each
with an R SC of 45mohm. The output ideal diode forward
regulation voltage is 30mV (OUTFET R DS(ON) < 30mohm).
The minimum open-circuit supercapacitor voltage is:
 V CAP(MIN) = 5V + 0.030V + (1A - 4 - 45mohm) = 5.21V
Using the synchronous controller in step-up mode allows
the supercapacitors to be discharged to a voltage much
lower than the minimum V OUT needed to run the sys -
tem. The amount of power that the supercapacitor stack
can deliver at its minimum internal (open-circuit) voltage
should be greater than what is needed to power the output
and the step-up converter .
According to the maximum power transfer rule:

PCAP(MIN) =
VCAP(MIN)2
4 - n - RSC
> PBACKUP

In the equation above  is the efficiency of the synchro -
nous controller in step-up mode and n is the number of
supercapacitors in the stack.
Example: System needs 5V to run and draws 1A dur -
ing backup. There are four supercapacitors in the stack
(n  = 4), each with an R SC of 45mohm. The converter effi -
ciency is 90%. The minimum open-circuit supercapacitor
voltage is:

VCAP(MIN) = 4 - 4 - 45mohm - 5V - 1A
0.9 = 2.0V
In this case, the voltage seen at the terminals of the
capacitor stack is half this voltage, or 1V, according to
the maximum power transfer rule.
```

### Page 25

```text
LTC3350
25
Rev. DFor more information www.analog.com
APPLICATIONS INFORMATION
Note the minimum VCAP voltage can also be limited by the
peak inductor current limit (180% of maximum charge
current) and the maximum duty cycle in step-up mode
(~90%).
Optimizing Supercapacitor Energy Storage Capacity
In most systems the supercapacitors will provide backup
power to one or more DC/DC converters. A DC/DC con -
verter presents a constant power load to the supercapaci-
tor . When the supercapacitors are near their maximum
voltage, the loads will draw little current. As the capaci -
tors discharge, the current drawn from supercapacitors
will increase to maintain constant power to the load. The
amount of energy required in back up mode is the product
of this constant backup power , PBACKUP, and the backup
time, tBACKUP.
The energy stored in a stack of n supercapacitors available
for backup is:

1
2 nCSC CELL(MAX)
2V - CELL(MIN)
2V( )
where CSC, VCELL(MAX) and VCELL(MIN) are the capacitance,
maximum voltage and minimum voltage of a single capac-
itor in the stack, respectively. The maximum voltage on
the stack is V CAP(MAX) = n - VCELL(MAX). The minimum
voltage on the stack is VCAP(MIN) = n - VCELL(MIN).
Some of this energy will be dissipated as conduction loss
in the ESR of the supercapacitor stack. A higher backup
power requirement leads to a higher conduction loss for
a given stack ESR.
The amount of capacitance needed can be found by solv-
ing the following equation for CSC:
PBACKUP - tBACKUP = 1
4 nCSC  MAX - CELL(MAX)
2V -  MIN - CELL(MIN)
2V - 4RSC -PBACKUP
n ln  MAX - VCELL(MAX)
 MIN - VCELL(MIN)

where:

MAX = 1+ 1- 4RSC -PBACKUP
n CELL(MAX)
2V
and,
 Min = 1+ 1- 4RSC -PBACKUP
n CELL(MIN)
2V
RSC is the equivalent series resistance (ESR) of a single
supercapacitor in the stack. Note that the maximum power
transfer rule limits the minimum cell voltage to:

VCELL(MIN) =
VCAP(MIN)
n >= 4RSC - PBACKUP
n
To minimize the size of the capacitance for a given amount
of backup energy, the maximum voltage on the stack,
VCELL(MAX), can be increased. However , the voltage is
limited to a maximum of 2.7V and this may lead to an
unacceptably low capacitor lifetime.
An alternative option would be to keep V CELL(MAX) at a
voltage that leads to reasonably long lifetime and increase
the capacitor utilization ratio of the supercapacitor stack.
The capacitor utilization ratio, alphaB, can be defined as:

alphaB = CELL(MAX)
2V - CELL(MIN)
2V
CELL(MAX)
2V
If the synchronous controller in step-up mode is used
then the supercapacitors can be run down to a voltage
```

### Page 26

```text
LTC3350
26
Rev. D For more information www.analog.com
APPLICATIONS INFORMATION
set by the maximum power transfer rule to maximize the
utilization ratio. The minimum voltage in this case is:

VCELL(MIN) = 4RSC - PBACKUP
n
where  is the efficiency of the boost converter
(~90% to 96%). For the backup equation, MAX and MIN,
substitute PBACKUP/ for PBACKUP. In this case the energy
needed for backup is governed by the following equation:

PBACKUP
 tBACKUP <= 1
2 nCSC - CELL(MAX)
2V -
alphaB + alphaB
2 - 1- alphaB
2 ln 1+ alphaB
1- alphaB

Once a capacitance is found using the above equation the
maximum ESR allowed needs to be checked:

RSC <=
 1- alphaB( )n CELL(MAX)
2V
4PBACKUP
Capacitor Selection Procedure
1. Determine backup requirements PBACKUP and tBACKUP.
2. Determine maximum cell voltage that provides accept-
able capacitor lifetime.
3. Choose number of capacitors in the stack.
4. Choose a desired utilization ratio, alphaB, for the superca-
pacitor (e.g., 80%).
5. Solve for capacitance, CSC:

CSC >= 2PBACKUP - tBACKUP
n CELL(MAX)
2V
-
alphaB + alphaB
2 - 1- alphaB
2 ln
1+ alphaB( )
1- alphaB

-1
6. Find supercapacitor with sufficient capacitance CSC and
minimum RSC:

RSC <=
 1- alphaB( )n CELL(MAX)
2V
4PBACKUP
7. If a suitable capacitor is not available, iterate by choos-
ing more capacitance, a higher cell voltage, more
capacitors in the stack and/or a lower utilization ratio.
8. Make sure to take into account the lifetime degrada -
tion of ESR and capacitance, as well as the maximum
discharge current rating of the supercapacitor . A list of
supercapacitor suppliers is provided in Table 2.
Table 2. Supercapacitor Suppliers
AVX www.avx.com
Bussman www.cooperbussman.com
CAP-XX www.cap-xx.com
Illinois Capacitor www.illcap.com
Maxwell www.maxwell.com
Murata www.murata.com
NESS CAP www.nesscap.com
Tecate Group www.tecategroup.com
Inductor Selection
The switching frequency and inductor selection are interre-
lated. Higher switching frequencies allow the use of smaller
inductor and capacitor values, but generally results in
lower efficiency due to MOSFET switching and gate charge
losses. In addition, the effect of inductor value on ripple
current must also be considered. The inductor ripple cur-
rent decreases with higher inductance or higher frequency
and increases with higher VIN. Accepting larger values of
ripple current allows the use of low inductances but results
in higher output voltage ripple and greater core losses.
For the LTC3350, the best overall performance will be
attained if the inductor is chosen to be:

L = VIN(MAX)
ICHG(MAX) - fSW
for VIN(MAX) <= 2VCAP and:

L = 1- VCAP
VIN(MAX)

VCAP
0.25 -ICHG(MAX) - fSW
for VIN(MAX) >= 2VCAP, where VCAP is the final supercapaci-
tor stack voltage, VIN(MAX) is the maximum input voltage,
ICHG(MAX) is the maximum regulated charge current, and
fSW is the switching frequency. Using these equations, the
inductor ripple will be at most 25% of ICHG(MAX).
```

### Page 27

```text
LTC3350
27
Rev. DFor more information www.analog.com
Using the above equation, the inductor may be too large to
provide a fast enough transient response to hold up VOUT
when input power goes away. This occurs in cases where
the maximum VIN can be high (e.g. 25V) and the backup
voltage low (e.g. 6V). In these situations it would be best
to choose an inductor that is smaller resulting in maxi -
mum peak-to-peak ripple as high as 40% of ICHG(MAX).
Once the value for L is known, the type of inductor core
must be selected. Ferrite cores are recommended for their
very low core loss. Selection criteria should concentrate on
minimizing copper loss and preventing saturation. Ferrite core
material saturates "hard," which means that inductance col-
lapses abruptly when the peak design current is exceeded.
This causes an abrupt increase in inductor ripple current and
consequent output voltage ripple. Do not allow the core to
saturate. The saturation current for the inductor should be
at least 80% higher than the maximum regulated current,
ICHG(MAX). A list of inductor suppliers is provided in Table 3.
Table 3. Inductor Vendors
VENDOR URL
Coilcraft www.coilcraft.com
Murata www.murata.com
Sumida www.sumida.com
TDK www.tdk.com
Toko www.toko.com
Vishay www.vishay.com
Wurth Electronic www.we-online.com
COUT and CCAP Capacitance
VOUT serves as the input to the synchronous controller in
step-down mode and as the output in step-up (backup)
mode. If step-up mode is used, place 100uF of bulk (alu-
minum electrolytic, OS-CON, POSCAP) capacitance for
every 2A of backup current desired. For 5V system appli-
cations, 100uF per 1A of backup current is recommended.
In addition, a certain amount of high frequency bypass
capacitance is needed to minimize voltage ripple. The volt-
age ripple in step-up mode is:

VOUT =
1- VCAP
VOUT

1
COUT - fSW
+ VOUT
VCAP
- RESR

IOUT(BACKUP)
Maximum ripple occurs at the lowest VCAP that can supply
IOUT(BACKUP). Multilayer ceramics are recommended for
high frequency filtering.
If step-up mode is unused, then the specification for COUT
will be determined by the desired ripple voltage in step-
down mode:

VOUT =
VCAP
VOUT
1- VCAP
VOUT

ICHG(MAX)
COUT - fSW
+ ICHG(MAX) - RESR
In continuous conduction mode, the source current of the
top MOSFET is a square wave of duty cycle V CAP/VOUT.
To prevent large voltage transients, a low ESR capacitor
sized for the maximum RMS current must be used. The
maximum RMS capacitor current is given by:

IRMS  ICHG(MAX)
VCAP
VOUT
VOUT
VCAP
- 1
This formula has a maximum at V OUT = 2VCAP, where
IRMS = ICHG(MAX)/2. This simple worst-case condition is
commonly used for design because even significant devi-
ations do not offer much relief.
Medium voltage (20V to 35V) ceramic, tantalum, OS-CON,
and switcher-rated electrolytic capacitors can be used as
input capacitors. Sanyo OS-CON SVP , SVPD series, Sanyo
POSCAP TQC series, or aluminum electrolytic capacitors
from Panasonic WA series or Cornel Dublilier SPV series
in parallel with a couple of high performance ceramic
capacitors can be used as an effective means of achiev -
ing low ESR and high bulk capacitance.
VCAP serves as the input to the controller in step-up mode
and as the output in step-down mode. The purpose of the
VCAP capacitor is to filter the inductor current ripple. The
VCAP ripple (VCAP) is approximated by:

VCAP  IPP
1
8CCAP - fSW
+ RESR

where fSW is the switching frequency, CCAP is the capaci-
tance on VCAP and IPP is the ripple current in the induc-
tor . The output ripple is highest at maximum input voltage
since IPP increases with input voltage.
APPLICATIONS INFORMATION
```

### Page 28

```text
LTC3350
28
Rev. D For more information www.analog.com
APPLICATIONS INFORMATION
Because supercapacitors have low series resistance, it is
important that CCAP be sized properly so that the bulk of
the inductor current ripple flows through the filter capaci-
tor and not the supercapacitor . It is recommended that:

1
8CCAP - fSW
+ RESR

<= n - RSC
5
where n is the number of supercapacitors in the stack and
RSC is the ESR of each supercapacitor . The capacitance on
VCAP can be a combination of bulk and high frequency
capacitors. Aluminum electrolytic, OS-CON and POSCAP
capacitors are suitable for bulk capacitance while multilayer
ceramics are recommended for high frequency filtering.
Power MOSFET Selection
T wo external power MOSFETs must be selected for
the LTC3350's synchronous controller : one N-channel
MOSFET for the top switch and one N-channel MOSFET
for the bottom switch. The selection criteria of the exter-
nal N-channel power MOSFETs include maximum drain-
source voltage (V DSS), threshold voltage, on-resistance
(RDS(ON)), reverse transfer capacitance (CRSS), total gate
charge (QG), and maximum continuous drain current.
VDSS of both MOSFETs should be selected to be higher
than the maximum input supply voltage (including
transient). The peak-to-peak drive levels are set by the
DRVCC voltage. Logic-level threshold MOSFETs should
be used because DRVCC is powered from either INTVCC
(5V) or an external LDO whose output voltage must be
less than 5.5V.
MOSFET power losses are determined by R DS(ON), CRSS
and QG. The conduction loss at maximum charge current
for the top and bottom MOSFET switches are:
PCOND(TOP) = VCAP
VOUT
ICHG(MAX)2 - RDS(ON) 1+ T( )
PCOND(BOT) = 1- VCAP
VOUT

ICHG(MAX)2 - RDS(ON) 1+ T( )
The term (1+ T) is generally given for a MOSFET in the
form of a normalized RDS(ON) vs Temperature curve, but
 = 0.005/ degC can be used as an approximation for low
voltage MOSFETs.
Both MOSFET switches have conduction loss. However ,
transition loss occurs only in the top MOSFET in step-
down mode and only in the bottom MOSFET in step-up
mode. These losses are proportional to V OUT2 and can
be considerably large in high voltage applications (V OUT
> 20V). The maximum transition loss is:

PTRAN  k
2 VOUT2 -ICHG(MAX) - CRSS - fSW
where k is related to the drive current during the Miller
plateau and is approximately equal to one.
The synchronous controller can operate in both step-down
and step-up mode with different voltages on VOUT in each
mode. If V OUT is 12V in step-down mode (input power
available) and 10V in step-up mode (backup mode) then
both MOSFETs can be sized to minimize conduction loss. If
VOUT can be as high as 25V while charging and VOUT is held
to 6V in backup mode, then the MOSFETs should be sized
to minimize losses during backup mode. This may lead to
choosing a high side MOSFET with significant transition
loss which may be tolerable when input power is available
so long as thermal issues do not become a limiting factor .
The bottom MOSFET can be chosen to minimize conduc-
tion loss. If step-up mode is unused, then choosing a high
side MOSFET that that has a higher R DS(ON) device and
lower CRSS would minimize overall losses.
Another power loss related to switching MOSFET selection
is the power lost to driving the gates. The total gate charge,
QG, must be charged and discharged each switching cycle.
The power is lost to the internal LDO and gate drivers within
the LTC3350. The power lost due to charging the gates is:
 P G  (QGTOP + QGBOT) - fSW - VOUT
where QGTOP is the top MOSFET gate charge and QGBOT is
the bottom MOSFET gate charge. Whenever possible, uti-
lize MOSFET switches that minimize the total gate charge
to limit the internal power dissipation of the LTC3350.
Schottky Diode Selection
Optional Schottky diodes can be placed in parallel with the top
and bottom MOSFET switches. These diodes clamp SW dur-
ing the non-overlap times between conduction of the top and
bottom MOSFET switches. This prevents the body diodes of
```

### Page 29

```text
LTC3350
29
Rev. DFor more information www.analog.com
APPLICATIONS INFORMATION
the MOSFET switches from turning on, storing charge during
the non-overlap time and requiring a reverse recovery period
that could cost as much as 3% in efficiency at high VIN. One
or both diodes can be omitted if the efficiency loss can be
tolerated. The diode can be rated for about one-third to one-
fifth of the full load current since it is on for only a fraction
of the duty cycle. Larger diodes result in additional switching
losses due to their larger junction capacitance. In order for
the diodes to be effective, the inductance between them and
the top and bottom MOSFETs must be as small as possible.
This mandates that these components be placed next to each
other on the same layer of the PC board.
Top MOSFET Driver Supply (CB, DB)
An external bootstrap capacitor , CB, connected to the BST
pin supplies the gate drive voltage for the top MOSFET .
Capacitor CB, in Figure 8, is charged though an external
diode, DB, from DRVCC when the SW pin is low. The value
of the bootstrap capacitor , CB, needs to be 20 times that
of the total input capacitance of the top MOSFET .
With the top MOSFET on, the BST voltage is above the
system supply rail:
VBST = VOUT + VDRVCC
The reverse break down of the external diode, D B, must
be greater than VOUT(MAX) + VDRVCC(MAX).
The step-up converter can briefly run nonsynchronously
when used in conjunction with the output ideal diode.
During this time the BST to SW voltage can pump up to
voltages exceeding 5.5V if D B is a Schottky diode. Fast
switching PN diodes are recommended due to their low
leakage and junction capacitance. A Schottky diode can be
used if the step-up converter runs synchronous through-
out backup mode.
INTVCC/DRVCC and IC Power Dissipation
The LTC3350 features a low dropout linear regulator
(LDO) that supplies power to INTVCC from the VOUT sup-
ply. INTVCC powers the gate drivers (when connected to
DRVCC) and much of the LTC3350's internal circuitry. The
LDO regulates the voltage at the INTV CC pin to 5V. The
LDO can supply a maximum current of 50mA and must
be bypassed to ground with a minimum of 1uF when not
connected to DRVCC. DRVCC should have at least a 2.2uF
ceramic or low ESR electrolytic capacitor . No matter what
type of bulk capacitor is used on DRV CC, an additional
0.1uF ceramic capacitor placed directly adjacent to the
DRVCC pin is highly recommended. Good bypassing is
needed to supply the high transient currents required by
the MOSFET gate drivers.
High input voltage applications in which large MOSFETs
are being driven at high frequencies may cause the maxi-
mum junction temperature rating for the LTC3350 to be
exceeded. The INTVCC current, which is dominated by the
gate charge current, is supplied by the 5V LDO.
Power dissipation for the IC in this case is highest and
is approximately equal to (V OUT) - (IQ + I G), where I Q
is the non-switching quiescent current of ~4mA and I G
is gate charge current. The junction temperature can be
estimated by using the equations given in Note 2 of the
Electrical Characteristics. For example, the IG supplied by
the INTVCC LDO is limited to less than 42mA from a 35V
supply in the QFN package at a 70 degC ambient temperature:
T J = 70 degC + (35V)(4mA + 42mA)(34 degC/W) = 125 degC
To prevent the maximum junction temperature from being
exceeded, the INTVCC LDO current must be checked while
operating in continuous conduction mode at maximum
VOUT.
The power dissipation in the IC is drastically reduced if
DRVCC is powered from an external LDO. In this case the
power dissipation in the IC is equal to power dissipation
due to I Q and the power dissipated in the gate drivers,
(VDRVCC) - (IG). Assuming the external DRVCC LDO output
is 5V and is supplying 42mA to the gate drivers, the junc-
tion temperature rises to only 82 degC:
TJ = 70 degC + [(35V)(4mA)+(5V)(42mA)](34 degC/W) = 82 degCFigure 8. Bootstrap Capacitor/Diode and
DRV CC Connections
BST
SW
>2.2uF
3350 F07
DB
DRVCC
INTVCC
L TC3350 CB
0.1uF
1uF
OPT
```

### Page 30

```text
LTC3350
30
Rev. D For more information www.analog.com
APPLICATIONS INFORMATION
The external LDO should be powered from VOUT. It must
be enabled after the INTVCC LDO has powered up and its
output must be less than 5.5V. INTVCC should no longer
be tied to DRVCC.
Minimum On-Time Considerations
Minimum on-time, tON(MIN), is the smallest time duration
that the LTC3350 is capable of turning on the top MOSFET in
step-down mode. It is determined by internal timing delays
and the gate charge required to turn on the top MOSFET .
The minimum on-time for the LTC3350 is approximately
85ns. Low duty cycle applications may approach this mini-
mum on-time limit and care should be taken to ensure that:

tON(MIN) < VCAP
VOUT - fSW
If the duty cycle falls below what can be accommodated by
the minimum on-time, the controller will begin to skip cycles.
The charge current and VCAP voltage will continue to be regu-
lated, but the ripple voltage and current will increase.
Ideal Diode MOSFET Selection
An external N-channel MOSFET is required for the input
and output ideal diodes. Important parameters for the
selection of these MOSFETs are the maximum drain-
source voltage, V DSS, gate threshold voltage and on-
resistance (RDS(ON)).
When the input is grounded, either the supercapacitor
stack voltage or the step-up controller's backup voltage
is applied across the input ideal diode MOSFET . Therefore,
the VDSS of the input ideal diode MOSFET must withstand
the maximum voltage on V OUT in backup mode. When
the supercapacitors are at 0V, the input voltage is applied
across the output ideal diode MOSFET . Therefore, the VDSS
of the output ideal diode MOSFET must withstand the high-
est voltage on VIN.
The gate drive for both ideal diodes is 5V. This allows the
use of logic-level threshold N-channel MOSFETs.
As a general rule, select MOSFETs with a low enough RDS(ON)
to obtain the desired VDS while operating at full load current.
The LTC3350 will regulate the forward voltage drop across
the input and output ideal diode MOSFETs to 30mV if RDS(ON)
is low enough. The required RDS(ON) can be calculated by
dividing 0.030V by the load current in amps.
Achieving forward regulation will minimize power loss and
heat dissipation, but it is not a necessity. If a forward volt-
age drop of more than 30mV is acceptable, then a smaller
MOSFET can be used but must be sized compatible with the
higher power dissipation. Care should be taken to ensure
that the power dissipated is never allowed to rise above the
manufacturer's recommended maximum level.
During backup mode, the output ideal diode shuts off
when the voltage on OUTFB falls below 1.3V. For high VOUT
backup voltages (>8.4V), the output ideal diode will shut off
when VCAP is more than a diode drop (~700mV) above the
VOUT regulation point (i.e., OUTFB > 1.2V). The body diode
of the output ideal diode N-channel MOSFET will carry the
load current until VCAP drops to within a diode drop of the
VOUT regulation voltage at which point the synchronous
controller takes over . During this period the power dissi-
pation in the output ideal diode MOSFET increases sig -
nificantly. Diode conduction time is small compared to the
overall backup time but can be significant when discharging
very large supercapacitors (>600F). Care should be taken to
properly heat sink the MOSFET to limit the temperature rise.
PCB Layout Considerations
When laying out the printed circuit board, the following
guidelines should be used to ensure proper operation of
the IC. Check the following in your layout:
1. Keep MN1, MN2, D1, D2 and C OUT close together .
The high di/dt loop formed by the MOSFETs, Schottky
diodes and the VOUT capacitance, shown in Figure 9,
should have short, wide traces to minimize high fre-
quency noise and voltage stress from inductive ringing.
Figure 9. High Speed Switching Path
+
+
+
+
HIGH
FREQUENCY
CIRCULATING
PATH
MN2
MN1
VOUT
D2
D1
CCAP
3350 F09
COUT
RSNSC VCAPL1
```

### Page 31

```text
LTC3350
31
Rev. DFor more information www.analog.com
APPLICATIONS INFORMATION
Surface mount components are preferred to reduce par-
asitic inductances from component leads. Connect the
drain of the top MOSFET and cathode of the top diode
directly to the positive terminal of COUT. Connect the
source of the bottom MOSFET and anode of the bot-
tom diode directly to the negative terminal of COUT. This
capacitor provides the AC current to the MOSFETs.
2. Ground is referenced to the negative terminal of the
VCAP decoupling capacitor in step-down mode and to
the negative terminal of the VOUT decoupling capaci-
tor in step-up mode. The negative terminal of C OUT
should be as close as possible to the negative termi-
nal of CCAP by placing the capacitors next to each other
and away from the switching loop described above.
The combined IC SGND pin/PGND paddle and the
ground returns of CINTVCC and CDRVCC must return to
the combined negative terminal of COUT and CCAP.
3. Effective grounding techniques are critical for success-
ful DC/DC converter layouts. Orient power components
such that switching current paths in the ground plane do
not cross through the SGND pin and exposed pad on the
backside of the LTC3350 IC. Switching path currents can
be controlled by orienting the MOSFET switches, Schottky
diodes, the inductor , and VOUT and VCAP decoupling capac-
itors in close proximity to each other .
4. Locate VCAP and VOUT dividers near the part and away
from switching components. Kelvin the top of resistor
dividers to the positive terminals of C CAP and COUT,
respectively. The bottom of the resistive dividers
should go back to the SGND pin. The feedback resistor
connections should not be run along the high current
feeds from the COUT capacitor .
5. Route ICAP and VCAP sense lines together , keep them
short. Same with VOUTSP and VOUTSN. Filter compo-
nents should be placed near the part and not near the
sense resistors. Ensure accurate current sensing with
Kelvin connections at the sense resistors. See Figure 10.
6. The trace from the positive terminal of the input current
sense resistor , RSNSI, to the VOUTSP pin carries the
part's quiescent and gate drive currents. To maintain
accurate measurement of the input current keep this
trace short and wide by placing RSNSI near the part.
7. Locate the DRVCC and BST decoupling capacitors in
close proximity to the IC. These capacitors carry the
MOSFET drivers' high peak currents. An additional 0.1uF
ceramic capacitor placed immediately next to the DRVCC
pin can help improve noise performance substantially.
8. Locate the small-signal components away from high
frequency switching nodes (BST , SW , TG, and BG). All
of these nodes have very large and fast moving signals
and should be kept on the output side of the LTC3350.
9. The input ideal diode senses the voltage between VIN
and VOUTSP . VIN should be connected near the source
of the input ideal diode MOSFET . VOUTSP is used for
Kelvin sensing the input current. Place the input current
sense resistor , RSNSI, near the input ideal diode MOSFET
with a short, wide trace to minimize resistance between
the drain of the ideal diode MOSFET and RSNSI.
10. The output ideal diode senses the voltage between
VOUTSN and VCAP . VCAP is used for Kelvin sensing
the charge current. Place the output ideal diode near
the charge current sense resistor , RSNSC, with a short,
wide trace to minimize resistance between the source
of the ideal diode MOSFET and RSNSC.
11. The INFET and OUTFET pins for the external ideal diode
controllers have extremely limited drive current. Care
must be taken to minimize leakage to adjacent PC board
traces. 100nA of leakage from these pins will introduce
an additional offset to the ideal diodes of approximately
10mV. To minimize leakage, the INFET trace can be
guarded on the PC board by surrounding it with VOUT
connected metal. Similarly, the OUTFET trace should be
guarded by surrounding it with VCAP connected metal.
12. The VCC2P5 bypass capacitor should return to ground
away from switching and gate drive current paths.
Figure 10. Kelvin Current Sensing
3350 F10
DIRECTION OF SENSED CURRENT
RSNSC
OR
RSNSI
TO VCAP
OR
VOUTSN
TO ICAP
OR
VOUTSP
```

### Page 32

```text
LTC3350
32
Rev. D For more information www.analog.com
REGISTER MAP
REGISTER SUB ADDR R/W BITS DESCRIPTION DEFAUL T PAGE
clr_alarms 0x00 R/W 15:0 Clear alarms register 0x0000 33
msk_alarms 0x01 R/W 15:0 Enable/mask alarms register 0x0000 33
msk_mon_status 0x02 R/W 9:0 Enable/mask monitor status alerts 0x0000 34
cap_esr_per 0x04 R/W 15:0 Capacitance/ESR measurement period 0x0000 34
vcapfb_dac 0x05 R/W 3:0 VCAP voltage reference DAC setting 0xF 34
vshunt 0x06 R/W 15:0 Capacitor shunt voltage setting 0x3999 34
cap_uv_lvl 0x07 R/W 15:0 Capacitor undervoltage alarm level 0x0000 34
cap_ov_lvl 0x08 R/W 15:0 Capacitor overvoltage alarm level 0x0000 34
gpi_uv_lvl 0x09 R/W 15:0 GPI undervoltage alarm level 0x0000 34
gpi_ov_lvl 0x0A R/W 15:0 GPI overvoltage alarm level 0x0000 34
vin_uv_lvl 0x0B R/W 15:0 VIN undervoltage alarm level 0x0000 35
vin_ov_lvl 0x0C R/W 15:0 VIN overvoltage alarm level 0x0000 35
vcap_uv_lvl 0x0D R/W 15:0 VCAP undervoltage alarm level 0x0000 35
vcap_ov_lvl 0x0E R/W 15:0 VCAP overvoltage alarm level 0x0000 35
vout_uv_lvl 0x0F R/W 15:0 VOUT undervoltage alarm level 0x0000 35
vout_ov_lvl 0x10 R/W 15:0 VOUT overvoltage alarm level 0x0000 35
iin_oc_lvl 0x11 R/W 15:0 IIN overcurrent alarm level 0x0000 35
ichg_uc_lvl 0x12 R/W 15:0 ICHG undercurrent alarm level 0x0000 35
dtemp_cold_lvl 0x13 R/W 15:0 Die temperature cold alarm level 0x0000 35
dtemp_hot_lvl 0x14 R/W 15:0 Die temperature hot alarm level 0x0000 35
esr_hi_lvl 0x15 R/W 15:0 ESR high alarm level 0x0000 35
cap_lo_lvl 0x16 R/W 15:0 Capacitance low alarm level 0x0000 35
ctl_reg 0x17 R/W 3:0 Control register 0b0000 36
num_caps 0x1A R 1:0 Number of capacitors configured - 36
chrg_status 0x1B R 11:0 Charger status register - 36
mon_status 0x1C R 9:0 Monitor status register - 37
alarm_reg 0x1D R 15:0 Active alarms register 0x0000 37
meas_cap 0x1E R 15:0 Measured capacitance value - 38
meas_esr 0x1F R 15:0 Measured ESR value - 38
meas_vcap1 0x20 R 15:0 Measured capacitor one voltage - 38
meas_vcap2 0x21 R 15:0 Measured capacitor two voltage - 38
meas_vcap3 0x22 R 15:0 Measured capacitor three voltage - 38
meas_vcap4 0x23 R 15:0 Measured capacitor four voltage - 38
meas_gpi 0x24 R 15:0 Measured GPI pin voltage - 38
meas_vin 0x25 R 15:0 Measured VIN voltage - 38
meas_vcap 0x26 R 15:0 Measured VCAP voltage - 38
meas_vout 0x27 R 15:0 Measured VOUT voltage - 38
meas_iin 0x28 R 15:0 Measured IIN current - 38
meas_ichg 0x29 R 15:0 Measured ICHG current - 38
meas_dtemp 0x2A R 15:0 Measured die temperature - 38
Registers at sub address 0x03, 0x18, 0x19, 0x2B-0xFF are unused.
```

### Page 33

```text
LTC3350
33
Rev. DFor more information www.analog.com
REGISTER DESCRIPTIONS
clr_alarms (0x00)
Clear Alarms Register: This register is used to clear alarms caused by exceeding a programmed limit.
Writing a one to any bit in this register will cause its
respective alarm to be cleared. The one written to this register is automatically cleared when its
respective alarm is cleared.
BIT(S) BIT NAME DESCRIPTION
0 clr_cap_uv Clear capacitor undervoltage alarm
1 clr_cap_ov Clear capacitor overvoltage alarm
2 clr_gpi_uv Clear GPI undervoltage alarm
3 clr_gpi_ov Clear GPI overvoltage alarm
4 clr_vin_uv Clear VIN undervoltage alarm
5 clr_vin_ov Clear VIN overvoltage alarm
6 clr_vcap_uv Clear VCAP undervoltage alarm
7 clr_vcap_ov Clear VCAP overvoltage alarm
8 clr_vout_uv Clear VOUT undervoltage alarm
9 clr_vout_ov Clear VOUT overvoltage alarm
10 clr_iin_oc Clear input overcurrent alarm
11 clr_ichg_uc Clear charge undercurrent alarm
12 clr_dtemp_cold Clear die temperature cold alarm
13 clr_dtemp_hot Clear die temperature hot alarm
14 clr_esr_hi Clear ESR high alarm
15 clr_cap_lo Clear capacitance low alarm
msk_alarms (0x01)
Mask Alarms Register: Writing a one to any bit in the Mask Alarms Register enables its respective
alarm to trigger an SMBALERT .
BIT(S) BIT NAME DESCRIPTION
0 msk_cap_uv Enable capacitor undervoltage alarm
1 msk_cap_ov Enable capacitor overvoltage alarm
2 msk_gpi_uv Enable GPI undervoltage alarm
3 msk_gpi_ov Enable GPI overvoltage alarm
4 msk_vin_uv Enable VIN undervoltage alarm
5 msk_vin_ov Enable VIN overvoltage alarm
6 msk_vcap_uv Enable VCAP undervoltage alarm
7 msk_vcap_ov Enable VCAP overvoltage alarm
8 msk_vout_uv Enable VOUT undervoltage alarm
9 msk_vout_ov Enable VOUT overvoltage alarm
10 msk_iin_oc Enable input overcurrent alarm
11 msk_ichg_uc Enable charge undercurrent alarm
12 msk_dtemp_cold Enable die temperature cold alarm
13 msk_dtemp_hot Enable die temperature hot alarm
14 msk_esr_hi Enable ESR high alarm
15 msk_cap_lo Enable capacitance low alarm
```

### Page 34

```text
LTC3350
34
Rev. D For more information www.analog.com
REGISTER DESCRIPTIONS
msk_mon_status (0x02)
Mask Monitor Status Register: Writing a one to any bit in this register enables a rising edge of its
respective bit in the mon_status register to trigger an
SMBALERT .
BIT(S) BIT NAME DESCRIPTION
0 msk_mon_capesr_active Set the SMBALERT when there is a rising edge on mon_capesr_active
1 msk_mon_capesr_scheduled Set the SMBALERT when there is a rising edge on mon_capesr_scheduled
2 msk_mon_capesr_pending Set the SMBALERT when there is a rising edge on mon_capesr_pending
3 msk_mon_cap_done Set the SMBALERT when there is a rising edge on mon_cap_done
4 msk_mon_esr_done Set the SMBALERT when there is a rising edge on mon_esr_done
5 msk_mon_cap_failed Set the SMBALERT when there is a rising edge on mon_cap_failed
6 msk_mon_esr_failed Set the SMBALERT when there is a rising edge on mon_esr_failed
7 - Reserved, write to 0
8 msk_mon_power_failed Set the SMBALERT when there is a rising edge on mon_power_failed
9 msk_mon_power_returned Set the SMBALERT when there is a rising edge on mon_power_returned
15:10 - Reserved, write to 0
cap_esr_per (0x04) 10 seconds per LSB
Capacitance and ESR Measurement Period: This register sets the period of repeated capacitance and
ESR measurements. Each LSB represents 10
seconds. Capacitance and ESR measurements will not repeat if this register is zero.
vcapfb_dac (0x05)  CAPFBREF = 37.5mV - vcapfb_dac + 637.5mV
VCAP Regulation Reference: This register is used to program the capacitor voltage feedback loop's
reference voltage. Only bits 3:0 are active.
vshunt (0x06)  183.5uV per LSB
Shunt Voltage Register: This register programs the shunt voltage for each capacitor in the stack.
The charger will limit current and the active shunts will
shunt current to prevent this voltage from being exceeded. As a capacitor voltage nears this level,
the charge current will be reduced. This should be
programmed higher than the intended final balanced individual capacitor voltage. Setting this
register to 0x0000 disables the shunt.
cap_uv_lvl (0x07)  183.5uV per LSB
Capacitor Undervoltage Level: This is an alarm threshold for each individual capacitor voltage in
the stack. If enabled, any capacitor voltage falling below
this level will trigger an alarm and an SMBALERT .
cap_ov_lvl (0x08)  183.5uV per LSB
Capacitor Overvoltage Level: This is an alarm threshold for each individual capacitor in the stack.
If enabled, any capacitor voltage rising above this level
will trigger an alarm and an SMBALERT .
gpi_uv_lvl (0x09)  183.5uV per LSB
General Purpose Input Undervoltage Level: This is an alarm threshold for the GPI pin. If enabled,
the voltage falling below this level will trigger an alarm
and an SMBALERT .
gpi_ov_lvl (0x0A)  183.5uV per LSB
General Purpose Input Overvoltage Level: This is an alarm threshold for the GPI pin. If enabled, the
voltage rising above this level will trigger an alarm and
an SMBALERT .
```

### Page 35

```text
LTC3350
35
Rev. DFor more information www.analog.com
REGISTER DESCRIPTIONS
vin_uv_lvl (0x0B)  2.21mV per LSB
VIN Undervoltage Level: This is an alarm threshold for the input voltage. If enabled, the voltage
falling below this level will trigger an alarm and an
SMBALERT .
vin_ov_lvl (0x0C)  2.21mV per LSB
VIN Overvoltage Level: This is an alarm threshold for the input voltage. If enabled, the voltage
rising above this level will trigger an alarm and an
SMBALERT .
vcap_uv_lvl (0x0D)  1.476mV per LSB
VCAP Undervoltage Level: This is an alarm threshold for the capacitor stack voltage. If enabled, the
voltage falling below this level will trigger an alarm and
an SMBALERT .
vcap_ov_lvl (0x0E)  1.476mV per LSB
VCAP Overvoltage Level: This is an alarm threshold for the capacitor stack voltage. If enabled, the
voltage rising above this level will trigger an alarm and
an SMBALERT .
vout_uv_lvl (0x0F)  2.21mV per LSB
VOUT Undervoltage Level: This is an alarm threshold for the output voltage. If enabled, the voltage
falling below this level will trigger an alarm and an
SMBALERT .
vout_ov_lvl (0x10)  2.21mV per LSB
VOUT Overvoltage Level: This is an alarm threshold for the output voltage. If enabled, the voltage
rising above this level will trigger an alarm and an
SMBALERT .
iin_oc_lvl (0x11)  1.983uV/RSNSI per LSB
Input Overcurrent Level: This is an alarm threshold for the input current. If enabled, the current
rising above this level will trigger an alarm and an
SMBALERT .
ichg_uc_lvl (0x12)  1.983uV/RSNSC per LSB
Charge Undercurrent Level: This is an alarm threshold for the charge current. If enabled, the
current falling below this level will trigger an alarm and an
SMBALERT .
dtemp_cold_lvl (0x13)  Temperature = 0.028 degC per LSB - 251.4 degC
Die Temperature Cold Level: This is an alarm threshold for the die temperature. If enabled, the die
temperature falling below this level will trigger an alarm
and an SMBALERT .
dtemp_hot_lvl (0x14)  Temperature = 0.028 degC per LSB - 251.4 degC
Die Temperature Hot Level: This is an alarm threshold for the die temperature. If enabled, the die
temperature rising above this level will trigger an alarm
and an SMBALERT .
esr_hi_lvl (0x15)  RSNSC/64 per LSB
ESR High Level: This is an alarm threshold for the measured stack ESR. If enabled, a measurement of
stack ESR exceeding this level will trigger an alarm
and an SMBALERT .
cap_lo_lvl (0x16)  336uF - RT/RTST per LSB
Capacitance Low Level: This is an alarm threshold for the measured stack capacitance. If enabled, if
the measured stack capacitance is less than this level
it will trigger an alarm and an SMBALERT . When ctl_cap_scale is set to one the constant is 3.36 -
RT/RTST.
```

### Page 36

```text
LTC3350
36
Rev. D For more information www.analog.com
REGISTER DESCRIPTIONS
ctl_reg (0x17)
Control Register: Several Control Functions are grouped into this register .
BIT(S) BIT NAME DESCRIPTION
0 ctl_strt_capesr Begin a capacitance and ESR measurement when possible; this bit clears itself
once a cycle begins.
1 ctl_gpi_buffer_en A one in this bit location enables the input buffer on the GPI pin. With a zero
in this
location the GPI pin is measured without the buffer .
2 ctl_stop_capesr Stops an active capacitance/ESR measurement.
3 ctl_cap_scale Increases capacitor measurement resolution by 100x, this is used when measuring
smaller capacitors.
15:4 - Reserved
num_caps (0x1A)
Number of Capacitors: This register shows the state of the CAP_SLCT1, CAP_SLCT0 pins. The value read
in this register is the number of capacitors
programmed minus one.
VALUE CAPACITORS
0b00 1 Capacitor Selected
0b01 2 Capacitors Selected
0b10 3 Capacitors Selected
0b11 4 Capacitors Selected

chrg_status (0x1B)
Charger Status Register: This register provides real time status information about the state of the
charger system. Each bit is active high.
BIT(S) BIT NAME DESCRIPTION
0 chrg_stepdown The synchronous controller is in step-down mode (charging)
1 chrg_stepup The synchronous controller is in step-up mode (backup)
2 chrg_cv The charger is in constant voltage mode
3 chrg_uvlo The charger is in undervoltage lockout
4 chrg_input_ilim The charger is in input current limit
5 chrg_cappg The capacitor voltage is above power good threshold
6 chrg_shnt The capacitor manager is shunting
7 chrg_bal The capacitor manager is balancing
8 chrg_dis The charger is temporarily disabled for capacitance measurement
9 chrg_ci The charger is in constant current mode
10 - Reserved
11 chrg_pfo Input voltage is below PFI threshold
15:12 - Reserved
```

### Page 37

```text
LTC3350
37
Rev. DFor more information www.analog.com
REGISTER DESCRIPTIONS
mon_status (0x1C)
Monitor Status: This register provides real time status information about the state of the
monitoring system. Each bit is active high.
BIT(S) BIT NAME DESCRIPTION
0 mon_capesr_active Capacitance/ESR measurement is in progress
1 mon_capesr_scheduled Waiting programmed time to begin a capacitance/ESR measurement
2 mon_capesr_pending Waiting for satisfactory conditions to begin a capacitance/ESR measurement
3 mon_cap_done Capacitance measurement has completed
4 mon_esr_done ESR Measurement has completed
5 mon_cap_failed The last attempted capacitance measurement was unable to complete
6 mon_esr_failed The last attempted ESR measurement was unable to complete
7 - Reserved
8 mon_power_failed This bit is set when VIN falls below the PFI threshold or the charger is unable
to
charge. It is cleared only when power returns and the charger is able to charge.
9 mon_power_returned This bit is set when the input is above the PFI threshold and the charger is
able to
charge. It is cleared only when mon_power_failed is set.
15:10 - Reserved

alarm_reg (0x1D)
Alarms Register: A one in any bit in the register indicates its respective alarm has triggered. All
bits are active high.
BIT(S) BIT NAME DESCRIPTION
0 alarm_cap_uv Capacitor undervoltage alarm
1 alarm_cap_ov Capacitor overvoltage alarm
2 alarm_gpi_uv GPI undervoltage alarm
3 alarm_gpi_ov GPI overvoltage alarm
4 alarm_vin_uv VIN undervoltage alarm
5 alarm_vin_ov VIN overvoltage alarm
6 alarm_vcap_uv VCAP undervoltage alarm
7 alarm_vcap_ov VCAP overvoltage alarm
8 alarm_vout_uv VOUT undervoltage alarm
9 alarm_vout_ov VOUT overvoltage alarm
10 alarm_iin_oc Input overcurrent alarm
11 alarm_ichg_uc Charge undercurrent alarm
12 alarm_dtemp_cold Die temperature cold alarm
13 alarm_dtemp_hot Die temperature hot alarm
14 alarm_esr_hi ESR high alarm
15 alarm_cap_lo Capacitance low alarm
```

### Page 38

```text
LTC3350
38
Rev. D For more information www.analog.com
REGISTER DESCRIPTIONS
meas_cap (0x1E)  336uF - RT/RTST per LSB
Measured capacitor stack capacitance value. When ctl_cap_scale is set to one the constant is 3.36uF
- RT/RTST.
meas_esr (0x1F)  RSNSC/64 per LSB
Measured capacitor stack equivalent series resistance (ESR) value
meas_vcap1 (0x20)  183.5uV per LSB
Measured voltage between the CAP1 and CAPRTN pins.
meas_vcap2 (0x21)  183.5uV per LSB
Measured voltage between the CAP2 and CAP1 pins.
meas_vcap3 (0x22)  183.5uV per LSB
Measured voltage between the CAP3 and CAP2 pins.
meas_vcap4 (0x23) 183.5uV per LSB
Measured voltage between the CAP4 and CAP3 pins.

meas_gpi (0x24) 183.5uV per LSB
Measurement of GPI pin voltage.
meas_vin (0x25) 2.21mV per LSB
Measured Input Voltage.
meas_vcap (0x26)  1.476mV per LSB
Measured Capacitor Stack Voltage.
meas_vout (0x27)  2.21mV per LSB
Measured Output Voltage.
meas_iin (0x28)  1.983uV/RSNSI per LSB
Measured Input Current.
meas_ichg (0x29) 1.983uV/RSNSC per LSB
Measured Charge Current.
meas_dtemp (0x2A) Temperature = 0.028 degC per LSB - 251.4 degC
Measured die temperature.
```

### Page 39

```text
LTC3350
39
Rev. DFor more information www.analog.com
Application Circuit 1. 25V to 35V, 6.4A Supercapacitor Charger with 2A Input Current Limit and 28V,
50W Backup Mode
VIN
VDD
Si1555DL
VIN
25V TO 35V
25V RISING THRESHOLD
22V FALLING THRESHOLD
INFET
MN1
SiS434DN
MN2
SiS434DN
L1
6.8uH
RSNSC
0.005/uni03A9
RCAP1 2.7/uni03A9
RCAP2 2.7/uni03A9
RCAP3 2.7/uni03A9
RCAP4 2.7/uni03A9
RCAPRTN 2.7/uni03A9
MN3
SiS434DN
RSNSI
0.016/uni03A9
VOUTM5VOUTSP
L TC3350
VOUTSN OUTFET
OUTFB
PFI
C1
0.1uF
C2
1uF
RPF1
80.6k
DB
B0540WS
CB
0.1uF
C3
4.7uF
C4
0.1uF
CCAP
47uF
RFBC1
866k
RFBC2
118k
CF
0.1uF
CCP5
0.1uF
CAP1 5F
CAP1-4: NESSCAP ESHSR-0005C0-002R7
L1: COILCRAFT XAL7070-682ME
CFBO1
120pF
COUT2
10uF
x 2
COUT1
82uF
RFBO1
665k
RFBO2
29.4k
RPF2
4.53k
RPF3
39.2k
R3
10k
R7
10k
R4
100k
C5
1uF
R6
121/uni03A9
R5
107k
CC
1.2nF
RT1
100k
R2
10k
R1
10k
VCC2P5
PFO
CAPGD
SMBALERT
SCL
SDA
PFO
CAPGD
SMBALERT
SCL
SDA
VOUT
28V
50W IN BACKUP
TGATE
SW
ICAP
VCAP
CAP_SLCT0
CAP_SLCT1
VCAPP5
3350 TA02
CFP
CAP4
CAP3
CAP2
CAP1
CFN
SGND
PGND
ITST
RTT
VC
GPI
DRVCC
INTVCC
BST
BGATE
+
CAP2 5F
+
CAP3 5F
+
CAP4 5F
+
+
CAPRTN
CAPFB
TYPICAL APPLICATIONS
```

### Page 40

```text
LTC3350
40
Rev. D For more information www.analog.com
Application Circuit 2. 11V to 20V, 16A Supercapacitor Charger with 6.4A Input Current Limit and 10V,
60W Backup Mode
VIN
VDD
VIN
11V TO 20V
INFET
MN1
SiR422DP
MN2
BSC026N02KS
L1
2.2uH
RSNSC
0.002/uni03A9
RCAP1 2.7/uni03A9
RCAP2 2.7/uni03A9
RCAP3 2.7/uni03A9
RCAP4 2.7/uni03A9
RCAPRTN 2.7/uni03A9
MN3
BSC046N02KS  x 2
RSNSI
0.005/uni03A9
VOUTM5VOUTSP
L TC3350
VOUTSN OUTFET
OUTFBPFI
C1
0.1uF
C2
1uF
RPF1
806k
DB
B0540WS
CB
0.47uF
C3
4.7uF
C4
0.1uF
CCAP
47uF
RFBC1
845k
RFBC2
150k
CF
0.1uF
CCP5
0.1uF
CAP1 360F
CAP1-4: NESSCAP ESHSR-0360CO-002R7
L1: VISHAY IHLP5050FDER2R2MO1
CFBO1
120pF
COUT2
22uF
x 4
COUT1
82uF
x 4
RFBO1
619k
RFBO2
89.5k
RPF2
100kR3
10k
R4
100k
C5
1uF
R6
121/uni03A9
R5
133k
CC
10nF
RT1
100k
R2
10k
R1
10k
VCC2P5
PFO
CAPGD
SMBALERT
SCL
SDA
PFO
CAPGD
SMBALERT
SCL
SDA
VOUT
10V
60W IN BACKUP
TGATE
SW
ICAP
VCAP
CAP_SLCT0
CAP_SLCT1
VCAPP5
3350 TA03
CFP
CAP4
CAP3
CAP2
CAP1
CFN
SGND
PGND
ITST
RTT
VC
GPI
DRVCC
INTVCC
BST
BGATE
+
CAP2 360F
+
CAP3 360F
+
CAP4 360F
+
+
CAPRTN
CAPFB
TYPICAL APPLICATIONS
Application Circuit 3. 11V to 20V, 5.3A LiFePO4 Battery Charger with 4.6A Input Current Limit and
12V, 48W Backup Mode
VIN
VDD
VIN
11V TO 20V
INFET
MN1
SiS438DN
MN2
BSZ060NE2LS
L1
3.3uH
RSNSC
0.006/uni03A9
RCAP1 3.6/uni03A9
RCAP2 3.6/uni03A9
RCAP3 3.6/uni03A9
RCAPRTN 3.6/uni03A9
VSHUNT = 3.6V
L1: COILCRAFT XAL7070-332ME
MN3
BSZ060NE2LS
RSNSI
0.007/uni03A9
VOUTM5VOUTSP
L TC3350
VOUTSN OUTFET
OUTFBPFI
C1
0.1uF
C2
1uF
RPF1
806k
DB
B0540WS
CB
0.1uF
C3
4.7uF
C4
0.1uF
CCAP
22uF
x 4
RFBC1
909k
RFBC2
118k
CF
0.1uF
CCP5
0.1uF
CFBO1
120pF
COUT2
2.2uF
x 2
COUT1
47uF
x 2
RFBO1
649k
RFBO2
71.5k
RPF2
100kR3
10k
R4
100k
C5
1uF
R6
10M
R5
71.5k
CC
4.7nF
RT1
100k
R2
10k
R1
10k
VCC2P5
PFO
CAPGD
SMBALERT
SCL
SDA
PFO
CAPGD
SMBALERT
SCL
SDA
VOUT
12V
48W IN BACKUP
TGATE
SW
ICAP
VCAP
CAP_SLCT1
CAP_SLCT0
VCAPP5
3350 TA04
CFP
CAP4
CAP3
CAP2
CAP1
CFN
SGND
PGND
ITST
RTT
VC
GPI
DRVCC
INTVCC
BST
BGATE
CAPRTN
CAPFB
+
+
+
```

### Page 41

```text
LTC3350
41
Rev. DFor more information www.analog.com
TYPICAL APPLICATIONS
Application Circuit 4. 11V to 35V, 4A Supercapacitor Charger with 2A Input Current Limit and 10V, 1A
Backup Mode
Application Circuit 5. 11V to 20V, 4A Supercapacitor Charger with 2A Input Current Limit and 5V, 2A
Backup Mode
VIN
VDD
VIN
11V TO 35V
INFET
MN1
SiR426DP
MN2
SiR426DP
L1
4.7uH
RSNSC
0.008/uni03A9
RCAP1 2.7/uni03A9
RCAP2 2.7/uni03A9
RCAP3 2.7/uni03A9
RCAP4 2.7/uni03A9
RCAPRTN 2.7/uni03A9
MN3
SiR426DP
RSNSI
0.016/uni03A9
VOUTM5VOUTSP
L TC3350
VOUTSN OUTFET
OUTFBPFI
C1
0.1uF
C2
1uF
RPF1
806k
DB
1N4448HWT
CB
0.1uF
C3
4.7uF
D1
DFLS240
C4
0.1uF
CCAP
47uF
RFBC1
590k
RFBC2
118k
CF
0.1uF
CCP5
0.1uF
CAP1 10F
CAP1-4: NESSCAP ESHSR-0010C0-002R7
L1: VISHAY IHLP5050FDER47MO1
CFBO1
100pF
COUT2
10uF
x 2
COUT1
82uF
RFBO1
665k
RFBO2
90.9k
RPF2
100kR3
10k
R4
100k
C5
1uF
R6
121/uni03A9
R5
107k
CC
10nF
RT1
100k
R2
10k
R1
10k
VCC2P5
PFO
CAPGD
SMBALERT
SCL
SDA
PFO
CAPGD
SMBALERT
SCL
SDA
VOUT
10V
10W IN BACKUP
TGATE
SW
ICAP
VCAP
CAP_SLCT0
CAP_SLCT1
VCAPP5
3350 TA05
CFP
CAP4
CAP3
CAP2
CAP1
CFN
SGND
PGND
ITST
RTT
VC
GPI
DRVCC
INTVCC
BST
C6
220pF
BGATE
+
CAP2 10F
+
CAP3 10F
+
CAP4 10F
+
+
CAPRTN
CAPFB
D2
DFLS240
VIN
VDD
VIN
11V TO 20V
INFET
MN1
SiR412DP
MN2
SiR426DP
MN4
SiR412DP
L1
4.7uH
RSNSC
0.008/uni03A9
RCAP1 2.7/uni03A9
RCAP2 2.7/uni03A9
RCAP3 2.7/uni03A9
RCAP4 2.7/uni03A9
RCAPRTN 2.7/uni03A9
MN3
SiR426DP
RSNSI
0.016/uni03A9
VOUTM5VOUTSP
L TC3350
VOUTSN OUTFET
OUTFBPFI
C1
0.1uF
C2
1uF
RPF1
806k
DB
1N4448HWT
CB
0.1uF
C3
4.7uF
D1
DFLS240
C4
0.1uF
CCAP
47uF
RFBC1
590k
RFBC2
118k
CF
0.1uF
CCP5
0.1uF
CAP1 10F
CAP1-4: NESSCAP ESHSR-0010C0-002R7
L1: VISHAY IHLP5050FDER47MO1
CFBO1
100pF
COUT2
10uF
x 2
COUT1
82uF
RFBO1
665k
RFBO2
210k
RPF2
100kR3
10k
R4
100k
C5
1uF
R6
121/uni03A9
R5
107k
CC
10nF
RT1
100k
R2
10k
R1
10k
VCC2P5
PFO
CAPGD
SMBALERT
SCL
SDA
PFO
CAPGD
SMBALERT
SCL
SDA
VOUT
5V
10W IN BACKUP
TGATE
SW
ICAP
VCAP
CAP_SLCT0
CAP_SLCT1
VCAPP5
3350 TA06
CFP
CAP4
CAP3
CAP2
CAP1
CFN
SGND
PGND
ITST
RTT
VC
GPI
DRVCC
INTVCC
BST
C6
220pF
BGATE
+
CAP2 10F
+
CAP3 10F
+
CAP4 10F
+
+
CAPRTN
CAPFB
D2
DFLS240
```

### Page 42

```text
LTC3350
42
Rev. D For more information www.analog.com
TYPICAL APPLICATIONS
Application Circuit 6. 11V to 15V, 2.3A Zeta-SEPIC High Voltage Capacitor Charger with 2A Input
Current Limit and 10V, 25W Backup Mode
VIN
VDD
VIN
11V TO 15V
INFET
MN1
FDMC7660S
L1
4.7uH
RSNSI
0.016/uni03A9
VOUTM5VOUTSP
L TC3350
VOUTSN OUTFET
OUTFBPFI
C1
0.1uF
C2
1uF
RPF1
158k
CB
0.1uF
CB2
4.7uF
C6
470pF
10uF
10uF
1/uni03A9MP1
Si7415DN
MN2
FDMC86520L
Q1
Si1555DL
C3
4.7uF
C4
0.1uF
C7
10uF
RSNSC
0.014/uni03A9
CAP: NICHICON UHW1V222MHD
L1, L2: COILCRAFT XAL4030-472ME
SET ctl_cap_scale TO 1
CAP
2200uF
35V
x 2
RCAPTOP
255k
RCAPBOT
24.3k
RFBC1
787k
RFBC3
604k
CFBC
820pF
RFBC2
28k
COUT
22uF
x 5
RFBO1
768k
RFBO2
100k
RPF2
20k
R3
10k
C5
1uF
R6
10M
R5
107k
CC
22nF
R2
10k
R1
10k
VCC2P5
PFO
CAPGD
SMBALERT
SCL
SDA
PFO
CAPGD
SMBALERT
SCL
SDA
VOUT
10V
25W IN BACKUP
TGATE
SW
ICAP
CAP_SLCT0
CAP_SLCT1
VCAPP5
3350 TA07
CFP
CFN
CAP4
CAP3
CAP2
CAP1
SGND
PGND
ITST
RT
VC
GPI
DRVCC
INTVCC
BST
L2
4.7uH
BGATE
CAPRTN
CAPFB
+
VCAP
In a Zeta-SEPIC application there are several differences
in the monitoring features due to differences in how the
LTC3350 is configured. The capacitor voltage is measured
differently, it is no longer measured in the meas_vcap
register , but in the meas_vcap1 register . The scale factor
for meas_vcap1 must be adjusted for the resistor divider
connected to the CAP1 pin. Also in this configuration the
precision current load (ITST) for the capacitance test can-
not be used. The load on the capacitors are the external
dividers only. A capacitance measurement may still be
done. The results in the meas_cap_register will have an
LSB in Farads of:

CLSB = -5.6 - 10-7
In 1- 0.2
VCAP

1+ RCAPTOP
RCAPBOT

RT
RL
where RL is the total resistance to ground in parallel with
the capacitor , RCAPTOP is the top divider resistor from
the capacitor to CAP1 and RCAPBOT is the bottom divider
resistor from CAP1 to ground. The above equation is for
when the ctl_cap_scale bit is set to one. ESR measure -
ments may be possible with large capacitors with larger
ESR's. However , the accuracy of the ESR measurement
in this application is significantly reduced. The ESR mea-
surement in the meas_esr register must be scaled up
by the resistor divider ratio. The voltage at the CAP1 pin
should be kept below the VSHUNT setting.
The voltage at the CAP1 pin will be above the default shunt
value (2.7V) when V CAP is greater than 31V. In order to
continue charging to 35V, the shunts should be disabled
by setting vshunt to zero (0x0000).
```

### Page 43

```text
LTC3350
43
Rev. DFor more information www.analog.com
TYPICAL APPLICATIONS
Application Circuit 7. 4.8V to 12V, 10A Supercapacitor Charger with 6.4A Input Current Limit and 5V,
30W  Backup Mode
VIN
VDD
VIN
4.8V TO 12V
50us FALLING
EDGE FIL TER
INFET
MN1
SiS452DN
MN2
SiS452DN
L1
1uH
RSNSC
0.003/uni03A9
RCAP1 2.7/uni03A9
RCAP2 2.7/uni03A9
RCAPRTN 2.7/uni03A9
MN3
SiS452DN
RSNSI
0.005/uni03A9
VOUTM5VOUTSP
L TC3350
VOUTSN OUTFET
OUTFBPFI
C1
0.1uF
C2
1uF
RPF1
30.1k
DB
B0540WS
CB
0.1uF
C3
10uF
C4
0.1uF
CCAP
47uF
RFBC1
732k
RFBC2
274k
CF
0.1uF
CCP5
0.1uF
CAP1 50F
CAP1-2: NESSCAP ESHSR-0050C0-002R7
L1: COILCRAFT XAL7030-102ME
CFBO1
100pF
COUT2
100uF
x 6
COUT1
2.2uF
x 2
RFBO1
665k
RFBO2
210k
RPF2
10k
10pF
MN4
Si1062X
1M
R3
1k
R4
100k
RC
2k
C5
1uF
R6
121/uni03A9
R5
88.7k
CC
4.7nF
RT1
100k
R2
10k
R1
10k
VCC2P5
PFO
CAPGD
SMBALERT
SCL
SDA
PFO
CAPGD
SMBALERT
SCL
SDA
VOUT
5V
30W IN BACKUP
TGATE
SW
ICAP
VCAP
CAP_SLCT0
CAP_SLCT1
VCAPP5
3350 TA08
CFP
CAP4
CAP3
CAP2
CAP1
CFN
SGND
PGND
ITST
RTT
VC
GPI
DRVCC
INTVCC
BST
BGATE
+
CAP2 50F
+
CAPRTN
CAPFB
```

### Page 44

```text
LTC3350
44
Rev. D For more information www.analog.com
PACKAGE DESCRIPTION
5.00 +/-0.10
NOTE:
1. DRAWING CONFORMS TO JEDEC PACKAGE
    OUTLINE M0-220 VARIATION WHKD
2. DRAWING NOT TO SCALE
3. ALL DIMENSIONS ARE IN MILLIMETERS
PIN 1
TOP MARK
(SEE NOTE 6)
37
1
2
38
BOTTOM VIEW-EXPOSED PAD
5.50 REF
5.15 +/-0.10
7.00 +/-0.10
0.75 +/-0.05
R = 0.125
TYP
R = 0.10
TYP
0.25 +/-0.05
(UH) QFN REF C 1107
0.50 BSC
0.200 REF
0.00 - 0.05
RECOMMENDED SOLDER PAD LAYOUT
APPL Y SOLDER MASK TO AREAS THAT ARE NOT SOLDERED
3.00 REF
3.15 +/-0.10
0.40 +/-0.10
0.70 +/-0.05
0.50 BSC
5.5 REF
3.00 REF 3.15 +/-0.05
4.10 +/-0.05
5.50 +/-0.05 5.15 +/-0.05
6.10 +/-0.05
7.50 +/-0.05
0.25 +/-0.05
PACKAGE
OUTLINE
4. DIMENSIONS OF EXPOSED PAD ON BOTTOM OF PACKAGE DO NOT INCLUDE
    MOLD FLASH. MOLD FLASH, IF PRESENT, SHALL NOT EXCEED 0.20mm ON ANY SIDE
5. EXPOSED PAD SHALL BE SOLDER PLATED
6. SHADED AREA IS ONLY A REFERENCE FOR PIN 1 LOCATION
    ON THE TOP AND BOTTOM OF PACKAGE
PIN 1 NOTCH
R = 0.30 TYP OR
0.35  x  45 deg CHAMFER
UHF Package
38-Lead Plastic QFN (5mm  x  7mm)
(Reference LTC DWG # 05-08-1701 Rev C)
```

### Page 45

```text
LTC3350
45
Rev. DFor more information www.analog.com
Information furnished by Analog Devices is believed to be accurate and reliable. However , no
responsibility is assumed by Analog
Devices for its use, nor for any infringements of patents or other rights of third parties that may
result from its use. Specifications
subject to change without notice. No license is granted by implication or otherwise under any patent
or patent rights of Analog Devices.
REVISION HISTORY
REV DATE DESCRIPTION PAGE NUMBER
A 09/14 Modified IRMS equations in COUT and CCAP Capacitance section.
Changed 5V to 6V in back-up mode under the Power MOSFET Selection section.
Changed VCAP voltage reference DAC setting.
Modified Application Circuit.
27
28
32
42
B 01/15 Remove VCMI Common Mode Range from Electrical Characteristics.
Remove Conditions on IPFO Falling and Rising.
Change Analog-to-Digital Converter section.
Change range in the General Purpose Input section to 0V to 5V.
Change MN1 to MP1 just below Figure 6.
Change M1, M2 to MN1, MN2 in the PCB Layout Considerations section.
Increase page numbers to all entries on the Register Map.
For meas_vcap change uV to mV .
Change name to Application Circuit 6.
4
5
18
20
23
30
32
38
42
C 08/15 Modified Order Information Table for temperature grade identified by label on shipping
container .
Modified Input Overvoltage Protection Section.
Add sentence at the end of the first paragraph.
Add three sentences to the end of the Capacitance and ESR Measurements section.
Replace sentence in the Limit Checking and Alarms section.
Modified Figure 3.
Add new supplier to Table 2, Supercapacitor Suppliers.
Add Note 12 in the PCB Considerations Layout section.
Change reference from RTST/RT to RT/RTST on cap_lo_lvl description.
Change reference from RTST/RT to RT/RTST on meas_cap description.
Change value of RCAPBOT to 24.3k from 20k. Also add two sentences to the end of the text.
3
17
18
19
20
22
26
31
35
38
42
D 08/21 Added AEC-Q100 Qualified for Automotive Applications statement.
Added #W models in Ordering Information table.
1
2
```

### Page 46

```text
LTC3350
46
Rev. D For more information www.analog.com
ANALOG DEVICES, INC. 2014-2021
09/21
www.analog.com
RELATED PARTS
TYPICAL APPLICATION
12V PCle Backup Controller
PART NUMBER DESCRIPTION COMMENTS
Power Management
LTC3128 3A Monolithic Buck-Boost Supercapacitor Charger
and Balancer with Accurate Input Current Limit
+/-2% Accurate Average Input Current Limit Programmable to 3A, Active Charge
Balancing, Charges 1 or 2 Capacitors, VIN Range: 1.73V to 5.5V, VOUT Range:
1.8V to 5.5V, 20-Lead (4mm  x  5mm  x  0.75mm) QFN and 24-Lead TSSOP
Packages
LTC3226 2-Cell Supercapacitor Charger with Backup
PowerPath Controller
1x/2x Multimode Charge Pump Supercapacitor Charger , Automatic Cell
Balancing, PowerPath, 2A LDO Backup Supply, Automatic Main/Backup
Switchover , 2.5V to 5.5V, 16-Lead 3mm  x  3mm QFN Package
LTC3355 20V, 1A Buck DC/DC with Integrated SCAP Charger
and Backup Regulator
VIN: 3V to 20V, VOUT: 2.7V to 5V, 1A Main Buck Regulator , 5A Boost Backup
Regulator Powered from Single Supercapacitor , Overvoltage Protection,
20-Lead 4mm  x  4mm QFN Package.
LTC3625 1A High Efficiency 2-Cell Supercapacitor Charger
with Automatic Cell Balancing
High Efficiency Step-Up/Step-Down Charging of T wo Series Supercapacitors.
Automatic Cell Balancing. Programmable Charging Current to 500mA (Single
Inductor), 1A (Dual Inductor). 12-Lead 3mm  x  4mm DFN Package
LTC4110 Battery Backup System Manager Complete Backup Battery Manager for Li-Ion/Polymer , Lead
Acid, NiMH/
NiCd Batteries and Supercapacitors. Input Supply Range: 4.5V to 19V,
Programmable Charge Current Up to 3A, 38-Lead 5mm  x  7mm QFN Package.
LTC4425 Linear SuperCap Charger with Current-Limited Ideal
Diode and V/I Monitor
Constant-Current/Constant-Voltage Linear Charger for 2-Cell Series
Supercapacitor Stack. VIN: Li-Ion/Polymer Battery, a USB Port, or a 2.7V to
5.5V Current-Limited Supply. 2A Charge Current, Automatic Cell Balancing,
Shutdown Current <2uA. 12-Pin 3mm  x  3mm DFN or 12-Lead MSOP Package
VIN
VDD
VIN
11V TO 20V
INFET
MN1
SiS438DN
MN2
BSZ060NE2LS
MN4
SiS438DN
L1
3.3uH
RSNSC
0.006/uni03A9
RCAP1 2.7/uni03A9
RCAP2 2.7/uni03A9
RCAP3 2.7/uni03A9
RCAP4 2.7/uni03A9
RCAPRTN 2.7/uni03A9
MN3
BSZ060NE2LS
RSNSI
0.016/uni03A9
VOUTM5VOUTSP
L TC3350
VOUTSN OUTFET
OUTFBPFI
C1
0.1uF
C2
1uF
RPF1
806k
DB
1N4448HWT
CB
0.1uF
C3
4.7uF
C4
0.1uF
CCAP
22uF
x 4
RFBC1
866k
RFBC2
118k
CF
0.1uF
CCP5
0.1uF
CAP1 10F
CFBO1
120pF
COUT2
2.2uF
x 2
COUT1
47uF
x 2
RFBO1
649k
RFBO2
162k
RPF2
100kR3
10k
R4
100k
C5
1uF
R6
121/uni03A9
R5
71.5k
CC
10nF
RT1
100k
R2
10k
R1
10k
VCC2P5
PFO
CAPGD
SMBALERT
SCL
SDA
PFO
CAPGD
SMBALERT
SCL
SDA
VOUT
6V
25W IN BACKUP
TGATE
SW
ICAP
VCAP
CAP_SLCT0
CAP_SLCT1
VCAPP5
3350 TA09
CFP
CAP4
CAP3
CAP2
CAP1
CFN
GND
PGND
ITST
RTT
VC
GPI
DRVCC
INTVCC
BST
BGATE
+
CAP2 10F
+
CAP3 10F
+
CAP4 10F
+
CAPRTN
CAPFB
CAP1-4: NESSCAP ESHSR-0010C0-002R7
L1: COILCRAFT XAL7030-332ME
```
