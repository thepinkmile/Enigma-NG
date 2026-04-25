# AP2331 - 0.2A SINGLE CHANNEL CURRENT-LIMITED LOAD SWITCH

## Source Reference

- Source PDF: [AP2331-datasheet.pdf](AP2331-datasheet.pdf)
- Source path: `design\Datasheets\AP2331-datasheet.pdf`
- Generated markdown: `AP2331-datasheet.md`
- Page count: 12
- Extracted text characters: 19733
- Empty extraction pages: none
- Conversion method: automated local PDF text extraction with pypdf and pdfplumber

## Title and Part Identity

- Extracted title: AP2331 - 0.2A SINGLE CHANNEL CURRENT-LIMITED LOAD SWITCH
- File stem / likely part identity: `AP2331-datasheet`
- PDF metadata title: AP2331
- PDF metadata subject: 0.2A SINGLE CHANNEL CURRENT-LIMITED LOAD SWITCH
- Identity clue: AP2331
- Identity clue: 0.2A SINGLE CHANNEL CURRENT-LIMITED LOAD SWITCH
- Identity clue: The AP2331 is a single channel current -limited integrated high- side
- Identity clue: power switcher optimized for hot-swap applications. The devices have
- Identity clue: fast short-circuit response time for improved overall system robustness
- Identity clue: and provide a complete protection solution for application subject to
- Identity clue: heavy capacitive loads and the prospect of short circuit. It offers
- Identity clue: reverse-current blocking, over -current, over -temperature and short

## PDF Metadata

| Field | Value |
|:---|:---|
| Title | AP2331 |
| Author | Diodes Incorporated |
| Subject | 0.2A SINGLE CHANNEL CURRENT-LIMITED LOAD SWITCH |
| Creator | Acrobat PDFMaker 11 for Word |
| Producer | Adobe PDF Library 11.0 |

## Reviewed summary

### Curated design notes

- PDF review confirmed the source is a 12-page Diodes Incorporated datasheet for the AP2331 single-channel current-limited high-side load switch.
- Orderable variants called out by the PDF are AP2331SA-7 (SOT23), AP2331W-7 (SC59), and AP2331FJ-7 (U-DFN2020-3).
- Functional connections are simple and consistent across packages: pin 1 = GND, pin 2 = OUT, and pin 3 = IN. The typical application circuit uses a
  2.7 V to 5.2 V supply with 0.1 uF bypass capacitors on both IN and OUT.
- Key operating data from the PDF includes 2.7 V to 5.2 V input range, 0.2 A rated output current, 0.3/0.4/0.5 A overload current limit, 100/250/350
  mOhm RDS(ON) at VIN = 5 V and IOUT = 0.2 A, 2.35 V minimum / 2.65 V maximum UVLO rising threshold, 5.3 V typical output OVP trip, 0.7 ms typical
  turn-on time, and 150 deg C typical thermal shutdown.
- The application section adds the design calculations: PD = RDS(ON) x I^2 and TJ = PD x RthetaJA + TA. It also states that the reverse-current
  limiter is always active and that the output discharge path uses an internal 800 ohm NMOS when VIN falls below UVLO.
- Mechanical coverage is present in the PDF package pages for SOT23, SC59, and U-DFN2020-3, including suggested pad layouts and package-specific
  identification markings.
- Extraction limit: the pin-assignment sketches and the typical-performance plots remain figure-driven, so the searchable raw extraction below is the
  best local text representation of those graphics.

## Design-Relevant Extracted Content

These sections collect extracted snippets that are likely useful during design work, then the raw page-by-page text is preserved below for local search.

### Part number and ordering information

- Page 8: PD = Total Power Dissipation / Ordering Information / AP 2331 X - 7 / 7 : Tape & Reel
- Page 8: FJ : DFN2020 / Part Number Package Code Packaging / (Note 10) / 7" Tape and Reel
- Page 8: (Note 10) / 7" Tape and Reel / Quantity Part Number Suffix / AP2331SA-7 SA SOT23 3000/Tape
  & Reel -7 / AP2331W-7 W SC59 3000/Tape & Reel -7
- Page 8: http://www.diodes.com/datasheets/ap02001.pdf. / Marking Information / (1) SOT23
- Page 9: AP2331 / Marking Information / (3)   U-DFN2020-3
- Page 9: AP2331FJ-7 U-DFN2020-3 FJ / Package Information / Please see AP02002 at
  http://www.diodes.com/datasheets/ap02002.pdf for the latest version.
- Page 10: AP2331 / Package Information (cont.) / Please see AP02002 at
  http://www.diodes.com/datasheets/ap02002.pdf for the latest version. / (3) U-DFN2020-3
- Page 12: indirectly, any claim of personal injury or death associated with such unintended or
  unauthorized application. / Products described herein may be covered by one or more United States,
  international or foreign patents pending.  Product nam es and markings / noted herein may also be
  covered by one or more United States, international or foreign trademarks.

### Pin, pad, and connection designations

- Page 1: - Printers, Docking Stations, HUBs / - Smart Phones, e-Readers / Pin Assignments / Notes:
  1. No purposely added lead. Fully EU Directive 2002/95/EC (RoHS) & 2011/65/EU (RoHS 2) complia nt.
- Page 2: 0.1uF / Pin Descriptions / Pin Name Pin Number Functionss / GND 1 GND
- Page 2: Pin Descriptions / Pin Name Pin Number Functionss / GND 1 GND / OUT 2 Switch Output Pin
- Page 2: Pin Name Pin Number Functionss / GND 1 GND / OUT 2 Switch Output Pin / IN 3 Voltage Input
  Pin
- Page 2: GND 1 GND / OUT 2 Switch Output Pin / IN 3 Voltage Input Pin / Absolute Maximum Ratings
  (@TA = +25 degC, unless otherwise specified.)
- Page 3: 8. Since the output turn-on slew rate is dependent on input supply slew rate, this limit
  is only applicable for input  supply slew rate between  VIN/0.2ms to / VIN/1ms. / 9. Device
  mounted on FR-4 substrate PCB, 2oz copper, with minimum recommended pad layout. / AP2331
- Page 7: Reverse-Current Protection / The USB specification does not allow an output device to
  source current back into the USB port. In a normal MOSFET switch, current will flow in / reverse
  direction (from the output side to the input side) when the output side voltage is higher than the
  input side. A reverse current limit feature is / implemented in the AP2331 to limit such back
  currents. Reverse current limit is always active in AP2331. Reverse current is l imited at IROCP
  level
- Page 8: AP2331W-7 W SC59 3000/Tape & Reel -7 / AP2331FJ-7 FJ U-DFN2020-3 3000/Tape & Reel -7 /
  Note: 10. Pad layout as shown on Diodes Inc. suggested pad layout document AP02001, which can be
  found on our website at / http://www.diodes.com/datasheets/ap02001.pdf.
- Page 10: (3) U-DFN2020-3 / Suggested Pad Layout / Please see AP02002 at
  http://www.diodes.com/datasheets/ap02002.pdf for the latest version. / (1) SOT23
- Page 10: A A1 A3 / Seating Plane / Pin #1 ID / R0.200 / E3
- Page 11: AP2331 / Suggested Pad Layout (cont.) / Please see AP02002 at
  http://www.diodes.com/datasheets/ap02002.pdf for the latest version. / (3) U-DFN2020-3
- Page 12: AP2331 / IMPORTANT NOTICE / DIODES INCORPORATED MAKES NO WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, WITH REGARDS TO THIS DOCUMENT,
- Page 12: final and determinative format released by Diodes Incorporated. / LIFE SUPPORT / Diodes
  Incorporated products are specifically not authorized for use as critical components in life
  support devices or system s without the express
- Page 12: LIFE SUPPORT / Diodes Incorporated products are specifically not authorized for use as
  critical components in life support devices or system s without the express / written approval of
  the Chief Executive Officer of Diodes Incorporated. As used herein:
- Page 12: written approval of the Chief Executive Officer of Diodes Incorporated. As used herein: /
  A.   Life support devices or systems are devices or systems which: / 1. are intended to implant
  into the body, or
- Page 12: 1. are intended to implant into the body, or / 2. support or sustain life and whose
  failure to perform when properly used in accordance with instructions for use provided in the /
  labeling can be reasonably expected to result in significant injury to the user.

### Specifications, ratings, and operating conditions

- Page 1: AP2331 / 0.2A SINGLE CHANNEL CURRENT-LIMITED LOAD SWITCH / Description
- Page 1: Description / The AP2331  is a single channel current -limited integrated high- side /
  power switcher optimized for hot-swap applications. The devices have / fast short-circuit response
  time for improved overall system robustness
- Page 1: and provide a complete protection solution for application subject to / heavy capacitive
  loads and the prospect of short circuit. It offers / reverse-current blocking, over -current, over
  -temperature and short - / circuit protection, as w ell as controlled rise time and under -voltage
  / lockout functionality.
- Page 1: heavy capacitive loads and the prospect of short circuit. It offers / reverse-current
  blocking, over -current, over -temperature and short - / circuit protection, as w ell as
  controlled rise time and under -voltage / lockout functionality.
- Page 1: Features / - Input Voltage Range: 2.7V - 5.2V / - Fast Short-Circuit Response Time / -
  0.4A Accurate Current Limiting
- Page 1: - Input Voltage Range: 2.7V - 5.2V / - Fast Short-Circuit Response Time / - 0.4A Accurate
  Current Limiting / - 250mohm On-Resistance / - Reverse-Current Blocking
- Page 1: - 0.4A Accurate Current Limiting / - 250mohm On-Resistance / - Reverse-Current Blocking /
  - Built-In Soft-Start with 0.7ms Typical Turn-On Time / - Over-Current Protection
- Page 1: - Reverse-Current Blocking / - Built-In Soft-Start with 0.7ms Typical Turn-On Time / -
  Over-Current Protection / - Over-Voltage Protection / - Short-Circuit and Thermal Protection
- Page 1: - Built-In Soft-Start with 0.7ms Typical Turn-On Time / - Over-Current Protection / -
  Over-Voltage Protection / - Short-Circuit and Thermal Protection / - ESD Protection: 3KV HBM, 300V
  MM
- Page 1: - Over-Current Protection / - Over-Voltage Protection / - Short-Circuit and Thermal
  Protection / - ESD Protection: 3KV HBM, 300V MM / - Ambient Temperature Range: -40 degC to +85
  degC
- Page 2: GND 1 GND / OUT 2 Switch Output Pin / IN 3 Voltage Input Pin / Absolute Maximum Ratings
  (@TA = +25 degC, unless otherwise specified.)
- Page 2: IN 3 Voltage Input Pin / Absolute Maximum Ratings (@TA = +25 degC, unless otherwise
  specified.) / Symbol Parameter Ratings Units / ESD HBM Human Body Model ESD Protection 3 KV
- Page 2: Absolute Maximum Ratings (@TA = +25 degC, unless otherwise specified.) / Symbol Parameter
  Ratings Units / ESD HBM Human Body Model ESD Protection 3 KV / ESD MM Machine Model ESD Protection
  300 V
- Page 2: ESD HBM Human Body Model ESD Protection 3 KV / ESD MM Machine Model ESD Protection 300 V /
  VIN Input Voltage Relative to GND 6.5 V / VOUT Output Voltage Relative to GND VIN +0.3 V / ILOAD
  Maximum Continuous Load Current Internal Limited A
- Page 2: ESD MM Machine Model ESD Protection 300 V / VIN Input Voltage Relative to GND 6.5 V / VOUT
  Output Voltage Relative to GND VIN +0.3 V / ILOAD Maximum Continuous Load Current Internal Limited
  A / TJMAX Maximum Junction Temperature 150  degC
- Page 2: VIN Input Voltage Relative to GND 6.5 V / VOUT Output Voltage Relative to GND VIN +0.3 V /
  ILOAD Maximum Continuous Load Current Internal Limited A / TJMAX Maximum Junction Temperature 150
  degC / TST Storage Temperature Range (Note 4) -65 to +150  degC

### Dimensions, package, and mechanical information

- Page 1: lockout functionality. / The device is available in SOT23, SC59 and U-DFN2020-3 packages.
  / Features
- Page 3: 8. Since the output turn-on slew rate is dependent on input supply slew rate, this limit
  is only applicable for input  supply slew rate between  VIN/0.2ms to / VIN/1ms. / 9. Device
  mounted on FR-4 substrate PCB, 2oz copper, with minimum recommended pad layout. / AP2331
- Page 7: voltage accordingly. Complete shutdown occurs only if the fault stays long enough to
  activate thermal limiting. / The different overload conditions and the corresponding response of
  the AP2331 are outlined below: / S.NO Conditions Explanation Behavior of the AP2331
- Page 8: Application information (cont.) / Power Dissipation and Junction Temperature / The low on-
  resistance of the internal MOSFET allows the small surface- mount packages to pass large current.
  Using the maximum operating / ambient temperature (TA) and RDS(ON), the power dissipation can be
  calculated by: / PD = RDS(ON)  x  I2
- Page 8: AP 2331 X - 7 / 7 : Tape & Reel / Package Packing / SA : SOT23 / W : SC59
- Page 8: FJ : DFN2020 / Part Number Package Code Packaging / (Note 10) / 7" Tape and Reel
- Page 8: 52 and 53 week / Device Package Identification Code / AP2331SA-7 SOT23 KJ
- Page 8: 52 and 53 week / Device Package Identification Code / AP2331W-7 SC59 KN
- Page 9: 3 / Device Package Identification Code / AP2331FJ-7 U-DFN2020-3 FJ
- Page 9: AP2331FJ-7 U-DFN2020-3 FJ / Package Information / Please see AP02002 at
  http://www.diodes.com/datasheets/ap02002.pdf for the latest version.
- Page 9: M 0.085 0.18 0.11 / alpha 0 deg 8 deg - / All Dimensions in mm / SC59 / Dim Min Max Typ
- Page 9: N 0.70 0.80 0.75 / alpha 0 deg 8 deg - / All Dimensions in mm / A / M
- Page 10: AP2331 / Package Information (cont.) / Please see AP02002 at
  http://www.diodes.com/datasheets/ap02002.pdf for the latest version. / (3) U-DFN2020-3
- Page 10: E3 0.138 REF / L 0.35 0.45 0.40 / All Dimensions in mm / Dimensions Value (in mm) / Z 3.4
- Page 10: L 0.35 0.45 0.40 / All Dimensions in mm / Dimensions Value (in mm) / Z 3.4 / X 0.8
- Page 10: C 2.4 / E 1.35 / Dimensions Value (in mm) / Z 3.4 / X 0.8

### Formulas, equations, and configurable calculations

- Page 3: Electrical Characteristics (@TA = +25 degC, VIN = +5V, unless otherwise specified.) /
  Symbol Parameter Test Conditions (Note 5) Min Typ Max Unit / VUVLO Input UVLO VIN rising 2.35
  2.65 V / IQ Input quiescent current Above UVLO, IOUT = 0  85 125 uA / IREV Reverse leakage current
  VIN = 0V, VOUT = 5V, IREV at VIN  0.01 0.10 uA
- Page 3: Symbol Parameter Test Conditions (Note 5) Min Typ Max Unit / VUVLO Input UVLO VIN rising
  2.35  2.65 V / IQ Input quiescent current Above UVLO, IOUT = 0  85 125 uA / IREV Reverse leakage
  current VIN = 0V, VOUT = 5V, IREV at VIN  0.01 0.10 uA / RDS(ON) Switch on-resistance VIN = 5V,
  IOUT = 0.2A 100 250 350 mohm
- Page 3: IREV Reverse leakage current VIN = 0V, VOUT = 5V, IREV at VIN  0.01 0.10 uA / RDS(ON)
  Switch on-resistance VIN = 5V, IOUT = 0.2A 100 250 350 mohm / ILIMIT Over-load current limit VIN =
  5V, VOUT = 4V 0.3 0.4 0.5 A / IOS Short-circuit current OUT shorted to ground 0.3 0.4 0.5 A /
  IROCP Reverse-current trigger point  VIN = 5.0V, VOUT = 5.2V  0.20 0.25 A
- Page 3: OVP   101%  VIN / TON Output turn-on time (Note 8) CL = 0.1uF, RLOAD = 20ohm / (UVLO to
  90% VOUT-NOM)  0.7  ms / TSHDN Thermal shutdown threshold  VIN = 2.7V to 5.2V  150   degC / THYS
  Thermal shutdown hysteresis   20   degC
- Page 4: Typical Performance Characteristics / UVLO Increasing / 1ms/div
- Page 4: 1ms/div / UVLO Decreasing / 5ms/div
- Page 7: Application information / Under-Voltage Lockout (UVLO) / Under-voltage lockout function
  (UVLO) guarantees that the internal power switch is initially off during start -up. The UVLO
  functions only when the / power supply has reached at least 2. 5V (TYP). Whenever the input
  voltage falls below approximately 2.5V, the power switch is turned off. This
- Page 7: Application information / Under-Voltage Lockout (UVLO) / Under-voltage lockout function
  (UVLO) guarantees that the internal power switch is initially off during start -up. The UVLO
  functions only when the / power supply has reached at least 2. 5V (TYP). Whenever the input
  voltage falls below approximately 2.5V, the power switch is turned off. This / facilitates the
  design of hot-insertion systems where it is not possible to turn off the power switch before input
  power is removed.
- Page 7: part is powered up. / The IC senses the short circuit and immediately clamps output /
  current to a certain safe level namely ILIMIT / 2 Short-circuit or Over current / condition
- Page 7: condition that occurs when the / part is powered up and above / UVLO. / At the instance
  the overload occurs, higher current may flow for a / very short period of time before the current
  limit function can react.
- Page 7: After the current limit function has tripped (reached the over- / current trip threshold),
  the device switches into current limiting / mode and the current is clamped at ILIMIT. / 3 Gradual
  increase from nominal / operating current to ILIMIT
- Page 7: mode and the current is clamped at ILIMIT. / 3 Gradual increase from nominal / operating
  current to ILIMIT / Load increases gradually until / the current-limit threshold.
- Page 7: Load increases gradually until / the current-limit threshold. / The current rises until
  ILIMIT. Once the threshold has been / reached, the device switches into its current limiting mode
  and is / clamped at ILIMIT.
- Page 7: The current rises until ILIMIT. Once the threshold has been / reached, the device switches
  into its current limiting mode and is / clamped at ILIMIT. / Reverse-Current Protection
- Page 7: Discharge Function / When input voltage falls below UVLO, the discharge function is
  active. The output capacitor i s discharged through an internal NMOS that has a / discharge
  resistance of 800ohm. Hence, the output voltage drops down to zero. The time taken for discharge
  is dependent on the RC time constant of / the resistance and the output capacitor. Discharge time
  is calculated when UVLO falling threshold is reached to output voltage reaching 300mV.
- Page 7: When input voltage falls below UVLO, the discharge function is active. The output
  capacitor i s discharged through an internal NMOS that has a / discharge resistance of 800ohm.
  Hence, the output voltage drops down to zero. The time taken for discharge is dependent on the RC
  time constant of / the resistance and the output capacitor. Discharge time is calculated when UVLO
  falling threshold is reached to output voltage reaching 300mV. / AP2331

### Reference designs, applications, and examples

- Page 1: Description / The AP2331  is a single channel current -limited integrated high- side /
  power switcher optimized for hot-swap applications. The devices have / fast short-circuit response
  time for improved overall system robustness / and provide a complete protection solution for
  application subject to
- Page 1: power switcher optimized for hot-swap applications. The devices have / fast short-circuit
  response time for improved overall system robustness / and provide a complete protection solution
  for application subject to / heavy capacitive loads and the prospect of short circuit. It offers /
  reverse-current blocking, over -current, over -temperature and short -
- Page 1: - IEC60950-1 CB Scheme Certified / Applications / - LCD TVs & Monitors / - Set-Top Boxes,
  Residential Gateways
- Page 2: AP2331 / Typical Application Circuit / 0.1uF / IN
- Page 7: AP2331 / Application information / Under-Voltage Lockout (UVLO) / Under-voltage lockout
  function (UVLO) guarantees that the internal power switch is initially off during start -up. The
  UVLO functions only when the
- Page 8: AP2331 / Application information (cont.) / Power Dissipation and Junction Temperature /
  The low on- resistance of the internal MOSFET allows the small surface- mount packages to pass
  large current. Using the maximum operating
- Page 12: Diodes Incorporated and its subsidiaries reserve the right to make modifications,
  enhancements, improvements, corrections or other changes / without further notice to this document
  and any product described herein. Di odes Incorporated does not assume any liability arising out
  of the / application or use of this document or any product described herein; neither does Diodes
  Incorporated convey any license under its patent or / trademark rights, nor the rights of others.
  Any  Customer or user of this document or products described herein in such applications shall
  assume / all risks of such use and will agree to hold Diodes Incorporated and all the companies
  whose products are represented on Diodes Incorporated
- Page 12: without further notice to this document and any product described herein. Di odes
  Incorporated does not assume any liability arising out of the / application or use of this
  document or any product described herein; neither does Diodes Incorporated convey any license
  under its patent or / trademark rights, nor the rights of others.  Any  Customer or user of this
  document or products described herein in such applications shall assume / all risks of such use
  and will agree to hold Diodes Incorporated and all the companies whose products are represented on
  Diodes Incorporated / website, harmless against all damages.
- Page 12: Diodes Incorporated does not warrant or accept any liability whatsoever in respect of any
  products purchased through unauthorized sales channel. / Should Customers purchase or use Diodes
  Incorporated products for any unintended or unauthorized application, Customers shall indemnify
  and / hold Diodes Incorporated and its representatives harmless against all claims, damages,
  expenses, and attorney fees arising out of, directly or / indirectly, any claim of personal injury
  or death associated with such unintended or unauthorized application.
- Page 12: Should Customers purchase or use Diodes Incorporated products for any unintended or
  unauthorized application, Customers shall indemnify and / hold Diodes Incorporated and its
  representatives harmless against all claims, damages, expenses, and attorney fees arising out of,
  directly or / indirectly, any claim of personal injury or death associated with such unintended or
  unauthorized application. / Products described herein may be covered by one or more United States,
  international or foreign patents pending.  Product nam es and markings

## Page-by-Page Extracted Text

### Page 1

```text
NEW PRODUCT
AP2331

0.2A SINGLE CHANNEL CURRENT-LIMITED LOAD SWITCH

Description
The AP2331  is a single channel current -limited integrated high- side
power switcher optimized for hot-swap applications. The devices have
fast short-circuit response time for improved overall system robustness
and provide a complete protection solution for application subject to
heavy capacitive loads and the prospect of short circuit. It offers
reverse-current blocking, over -current, over -temperature and short -
circuit protection, as w ell as controlled rise time and under -voltage
lockout functionality.

The device is available in SOT23, SC59 and U-DFN2020-3 packages.

Features
- Input Voltage Range: 2.7V - 5.2V
- Fast Short-Circuit Response Time
- 0.4A Accurate Current Limiting
- 250mohm On-Resistance
- Reverse-Current Blocking
- Built-In Soft-Start with 0.7ms Typical Turn-On Time
- Over-Current Protection
- Over-Voltage Protection
- Short-Circuit and Thermal Protection
- ESD Protection: 3KV HBM, 300V MM
- Ambient Temperature Range: -40 degC to +85 degC
- Available in "Green" Molding Compound (No Br, Sb)
- Totally Lead-Free & Fully RoHS Compliant (Notes 1 & 2)
- Halogen and Antimony Free. "Green" Device (Note 3)
- UL Recognized, File Number E322375
- IEC60950-1 CB Scheme Certified

Applications
- LCD TVs & Monitors
- Set-Top Boxes, Residential Gateways
- Laptops, Desktops, Servers
- Printers, Docking Stations, HUBs
- Smart Phones, e-Readers
 Pin Assignments

Notes: 1. No purposely added lead. Fully EU Directive 2002/95/EC (RoHS) & 2011/65/EU (RoHS 2)
complia nt.
2. See http://www.diodes.com/quality/lead_free.html for more information about Diodes Incorporated's
definitions of Hal ogen- and Antimony-free, "Green"
and Lead-free.
3. Halogen- and Antimony-free "Green" products are defined as those which cont ain <900ppm bromine,
<900ppm chlorine (<1500ppm total Br + Cl) and
<1000ppm antimony compounds.

(Top View)
(Top View)
SC59
SOT23
IN
IN
GND
GND
OUT
OUT
21
GND OUT
IN
( Top View )
DFN2020-3
AP2331
Document Number: DS35529  Rev. 5 - 2
1 of 12
www.diodes.com
September 2014
(c) Diodes Incorporated
```

### Page 2

```text
NEW PRODUCT
AP2331

Typical Application Circuit
0.1uF
IN
GND
OUT
Power Supply
2.7V to 5.2V
Load
0.1uF

Pin Descriptions
Pin Name Pin Number Functionss
GND 1 GND
OUT 2 Switch Output Pin
IN 3 Voltage Input Pin

Absolute Maximum Ratings (@TA = +25 degC, unless otherwise specified.)
Symbol Parameter Ratings Units
ESD HBM Human Body Model ESD Protection 3 KV
ESD MM Machine Model ESD Protection 300 V
VIN Input Voltage Relative to GND 6.5 V
VOUT Output Voltage Relative to GND VIN +0.3 V
ILOAD Maximum Continuous Load Current Internal Limited A
TJMAX Maximum Junction Temperature 150  degC
TST Storage Temperature Range (Note 4) -65 to +150  degC
Note:    4. UL Recognized Rating from -30 degC to +70 degC (Diodes qualified TST from -65 degC to
+150 degC)

Recommended Operating Conditions (@TA = +25 degC, unless otherwise specified.)
Symbol Parameter Min Max Units
VIN Input Voltage Relative to GND 2.7 5.2 V
IOUT Output Current 0 0.2 A
TA Operating Ambient Temperature -40  +85  degC

AP2331

Document Number: DS35529  Rev. 5 - 2
2 of 12
www.diodes.com
September 2014
(c) Diodes Incorporated
```

### Page 3

```text
NEW PRODUCT
AP2331

Electrical Characteristics (@TA = +25 degC, VIN = +5V, unless otherwise specified.)
Symbol Parameter Test Conditions (Note 5) Min Typ Max Unit
VUVLO Input UVLO VIN rising 2.35  2.65 V
IQ Input quiescent current Above UVLO, IOUT = 0  85 125 uA
IREV Reverse leakage current VIN = 0V, VOUT = 5V, IREV at VIN  0.01 0.10 uA
RDS(ON) Switch on-resistance VIN = 5V, IOUT = 0.2A 100 250 350 mohm
ILIMIT Over-load current limit VIN = 5V, VOUT = 4V 0.3 0.4 0.5 A
IOS Short-circuit current OUT shorted to ground 0.3 0.4 0.5 A
IROCP Reverse-current trigger point  VIN = 5.0V, VOUT = 5.2V  0.20 0.25 A
TTRIG Deglitch time from reverse current trigger to
MOSFET turn off (Note 6) 0.5 0.7 1.0 ms
VOVP Output over-voltage trip point (Note 7) 5.3  5.6 V
TOVP Debounce time from output over-voltage to
MOSFET turn off   15  us
VREC Recovery after turn-off from ROCP and
OVP   101%  VIN
TON Output turn-on time (Note 8) CL = 0.1uF, RLOAD = 20ohm
(UVLO to 90% VOUT-NOM)  0.7  ms
TSHDN Thermal shutdown threshold  VIN = 2.7V to 5.2V  150   degC
THYS Thermal shutdown hysteresis   20   degC
JA Thermal Resistance Junction-to-Ambient
(Note 9)
SOT23  215   degC/W
SC59  255   degC/W
U-DFN2020-3  180   degC/W
Notes: 5. Pulse-testing techniques maintain junction temperature close to ambient temperature;
thermal effects must be taken into account sepa rately.
6. When reverse current triggers at IROCP = 0.20A, the reverse current is continuously clamped at
IROCP for 0.7ms deglitch time until MOSFET is turned off.
7. During output over-voltage protection, the output draws approximately 60u A current.
8. Since the output turn-on slew rate is dependent on input supply slew rate, this limit is only
applicable for input  supply slew rate between  VIN/0.2ms to
VIN/1ms.
9. Device mounted on FR-4 substrate PCB, 2oz copper, with minimum recommended pad layout.

AP2331
Document Number: DS35529  Rev. 5 - 2
3 of 12
www.diodes.com
September 2014
(c) Diodes Incorporated
```

### Page 4

```text
NEW PRODUCT
AP2331

Typical Performance Characteristics

UVLO Increasing

1ms/div
UVLO Decreasing

5ms/div
Over-Load Current Limit

5ms/div
Short-Circuit Current Limit

100us/div
Deglitch Time from Reverse-Current Trigger to MOSFET Turn-Off

200us/div

Reverse-Current Limit

200us/div

550us
200mA
AP2331
Document Number: DS35529  Rev. 5 - 2
4 of 12
www.diodes.com
September 2014
(c) Diodes Incorporated
```

### Page 5

```text
NEW PRODUCT
AP2331

Typical Performance Characteristics (cont.)

Output Over-Voltage Trip Point

10ms/div

Output Turn-On Time

200us/div

-40 -20 0 20 40 60 80
AMBIENT TEMPERATURE ( C)
Fig. 1 Quiescent Supply Current vs.
Ambient Temperature
 deg
0
20
40
60
80
100
120
140
V  = 5.2VIN
V  = 5VIN
V  = 3.3VIN
V  = 2.7VIN
SUPPLY CURRENT (uA)

-40 -20 0 20 40 60 80
AMBIENT TEMPERATURE ( C)
Fig. 2 Short Circuit Current Limit vs.
Ambient Temperature
 deg
0.388
0.390
0.392
0.394
0.396
0.398
0.400
0.402
SHORT CIRCUIT CURRENT (mA)
0.404
0.406
0.408
V  = 2.7VIN
V  = 3.3VIN
V  = 5V,IN
V  = 5.2VIN
C  = 10uFL

2.5 3.0 3.5 4.0 4.5 5.0 5.5
INPUT VOLTAGE (V)
Fig. 3 Output Turn On-Time vs. Input Voltage
OUTPUT TURN ON-TIME (ms)
0.20
0.25
0.30
0.35
0.40
0.45
C  = 1uF
R  = 5
L
L ohm

V  = 5.5VIN
V  = 5VIN
V  = 3.3VIN
V  = 2.7VIN
-40 -20 0 20 40 60 80
AMBIENT TEMPERATURE ( C)
Fig. 4 Switch On-Resistance vs.
Ambient Temperature
 deg
0
50
100
150
200
250
300ON-STATE RESISTANCE (m )ohm
350
400
450
500

OVP at 5.4V

OVP recovery
at 5.1V
CL=0.1uF
Rload=20ohm
AP2331
Document Number: DS35529  Rev. 5 - 2
5 of 12
www.diodes.com
September 2014
(c) Diodes Incorporated
```

### Page 6

```text
NEW PRODUCT
AP2331

Typical Performance Characteristics (cont.)

-40 -20 0 20 40 60 80
AMBIENT TEMPERATURE ( C)
Fig. 5 Current Limit Trip Threshold vs.
Ambient Temperature
 deg
0.388
0.390
0.392
0.394
0.396
0.398
0.400
0.402SUPPLY CURRENT (uA)

0
50
100
150
200
250
300REVERSE CURRENT LIMIT (mA)
350
400
450
500
-40 -20 0 20 40 60 80
AMBIENT TEMPERATURE ( C)
Fig. 6 Reverse Current Limit vs.
Ambient Temperature
 deg
V  = 5VIN
V  = 3.3VIN
V  = 2.7VIN

AP2331
Document Number: DS35529  Rev. 5 - 2
6 of 12
www.diodes.com
September 2014
(c) Diodes Incorporated
```

### Page 7

```text
NEW PRODUCT
AP2331

Application information
Under-Voltage Lockout (UVLO)
Under-voltage lockout function (UVLO) guarantees that the internal power switch is initially off
during start -up. The UVLO functions only when the
power supply has reached at least 2. 5V (TYP). Whenever the input voltage falls below approximately
2.5V, the power switch is turned off. This
facilitates the design of hot-insertion systems where it is not possible to turn off the power
switch before input power is removed.

Over-Current and Short-Circuit Protection
An internal sensing FET is employed to check for over  current conditions. Unlike current -sense
resistors, sense FETs do not increase the series
resistance of the current path. When an over  current condition is detected, the devic e maintains a
constant output current and reduces the output
voltage accordingly. Complete shutdown occurs only if the fault stays long enough to activate
thermal limiting.

The different overload conditions and the corresponding response of the AP2331 are outlined below:

S.NO Conditions Explanation Behavior of the AP2331
1 Short-circuit condition at start-up
Output is shorted before input
voltage is applied or before the
part is powered up.
The IC senses the short circuit and immediately clamps output
current to a certain safe level namely ILIMIT
2 Short-circuit or Over current
condition
Short-Circuit or Overload
condition that occurs when the
part is powered up and above
UVLO.
 At the instance the overload occurs, higher current may flow for a
very short period of time before the current limit function can react.
 After the current limit function has tripped (reached the over-
current trip threshold), the device switches into current limiting
mode and the current is clamped at ILIMIT.
3 Gradual increase from nominal
operating current to ILIMIT
Load increases gradually until
the current-limit threshold.
The current rises until ILIMIT. Once the threshold has been
reached, the device switches into its current limiting mode and is
clamped at ILIMIT.

Reverse-Current Protection
The USB specification does not allow an output device to source current back into the USB port. In a
normal MOSFET switch, current will flow in
reverse direction (from the output side to the input side) when the output side voltage is higher
than the input side. A reverse current limit feature is
implemented in the AP2331 to limit such back currents. Reverse current limit is always active in
AP2331. Reverse current is l imited at IROCP level
and when the fault exists for more than 700us, output device is disabled and shut down. This is
called the "Deglitch time from reverse current trigger
to MOSFET turn off." Recovery from IROCP occurs when the output voltage falls to 101% of input
voltage.

Over-Voltage Protection
The device has an output over-voltage protection that triggers when the output voltage reaches 5.3V
(MIN). When this fault condition stays on
for longer than 15us, (This is called the "Debounce time from output over voltage to MOSFET turn
off") output device is disabled and shut down.
Recovery from ROVP occurs when the output voltage falls to 101% of input voltage.

Thermal Protection
Thermal protection prevents the IC from damage when the die temperature exceeds safe margins. This
mainly occurs when heavy-overload or short-
circuit faults are present for extended periods of time. The AP2331 implements a thermal sensing to
monitor the operating junction  temperature of
the power distribution switch. Once the die temperature rises to approximately +150 degC, the
Thermal protection feature gets activated as follows: The
internal thermal sense circuitry turns the power switch off thus preventing the power switch from
damage. Hysteresis in the t hermal sense circuit
allows the device to cool down to approximately + 20 degC before the output is t urned back on. This
built -in thermal hysteresis feature is an excellent
feature, as it avoids undesirable oscillations of the thermal protection circuit.  The switch
continues to cycle in this manner until the load fault is
removed, resulting in a pulsed output.

Discharge Function
When input voltage falls below UVLO, the discharge function is active. The output capacitor i s
discharged through an internal NMOS that has a
discharge resistance of 800ohm. Hence, the output voltage drops down to zero. The time taken for
discharge is dependent on the RC time constant of
the resistance and the output capacitor. Discharge time is calculated when UVLO falling threshold is
reached to output voltage reaching 300mV.

AP2331
Document Number: DS35529  Rev. 5 - 2
7 of 12
www.diodes.com
September 2014
(c) Diodes Incorporated
```

### Page 8

```text
NEW PRODUCT
AP2331

Application information (cont.)
Power Dissipation and Junction Temperature
The low on- resistance of the internal MOSFET allows the small surface- mount packages to pass large
current. Using the maximum operating
ambient temperature (TA) and RDS(ON), the power dissipation can be calculated by:
PD = RDS(ON)  x  I2
Finally, calculate the junction temperature:
TJ = PD x RJA + TA
Where:
TA= Ambient Temperature  degC
RJA = Thermal Resistance
PD = Total Power Dissipation

Ordering Information
AP 2331 X - 7
7 : Tape & Reel
Package Packing
SA : SOT23
W : SC59
FJ : DFN2020

Part Number Package Code Packaging
(Note 10)
7" Tape and Reel
Quantity Part Number Suffix
AP2331SA-7 SA SOT23 3000/Tape & Reel -7
AP2331W-7 W SC59 3000/Tape & Reel -7
AP2331FJ-7 FJ U-DFN2020-3 3000/Tape & Reel -7
Note: 10. Pad layout as shown on Diodes Inc. suggested pad layout document AP02001, which can be
found on our website at
http://www.diodes.com/datasheets/ap02001.pdf.

Marking Information
(1) SOT23

1 2
3
XX Y W  X
( Top View )
XX : Identification code
W : Week : A~Z : 1~26 week;
X : A~Z : Internal code
Y : Year 0~9
a~z : 27~52 week; z represents
52 and 53 week

Device Package Identification Code
AP2331SA-7 SOT23 KJ

(2) SC59
1 2
3
XX Y W  X
( Top View )
XX : Identification code
W : Week : A~Z : 1~26 week;
X : A~Z : Internal code
Y : Year 0~9
a~z : 27~52 week; z represents
52 and 53 week

Device Package Identification Code
AP2331W-7 SC59 KN

AP2331
Document Number: DS35529  Rev. 2 - 2
8 of 12
www.diodes.com
September 2014
(c) Diodes Incorporated
```

### Page 9

```text
NEW PRODUCT
AP2331

Marking Information
(3)   U-DFN2020-3

( Top View )
XX : Identification code
W : Week : A~Z : 1~26 week;
X : A~Z : Internal code
Y : Year 0~9
a~z : 27~52 week; z represents
52 and 53 week
1
1
GND
GND
OUT
OUT
IN
IN
DFN
DFN
2020
2020
-
-
3
3
XX
XX
Y
Y
W
W
X
X
2
2
3
3

Device Package Identification Code
AP2331FJ-7 U-DFN2020-3 FJ

Package Information
Please see AP02002 at http://www.diodes.com/datasheets/ap02002.pdf for the latest version.

(1) SOT23

(2) SC59

SOT23
Dim Min Max Typ
A 0.37 0.51 0.40
B 1.20 1.40 1.30
C 2.30 2.50 2.40
D 0.89 1.03 0.915
F 0.45 0.60 0.535
G 1.78 2.05 1.83
H 2.80 3.00 2.90
J 0.013 0.10 0.05
K 0.903 1.10 1.00
K1 - - 0.400
L 0.45 0.61 0.55
M 0.085 0.18 0.11
alpha 0 deg 8 deg -
All Dimensions in mm
SC59
Dim Min Max Typ
A 0.35 0.50 0.38
B 1.50 1.70 1.60
C 2.70 3.00 2.80
D - - 0.95
G - - 1.90
H 2.90 3.10 3.00
J 0.013 0.10 0.05
K 1.00 1.30 1.10
L 0.35 0.55 0.40
M 0.10 0.20 0.15
N 0.70 0.80 0.75
alpha 0 deg 8 deg -
All Dimensions in mm
A
M
J L
D
F
B C
H
K
G
K1
A
M
J LD
B C
H
K
G
N
AP2331
Document Number: DS35529  Rev. 5 - 2
9 of 12
www.diodes.com
September 2014
(c) Diodes Incorporated
```

### Page 10

```text
NEW PRODUCT
AP2331

Package Information (cont.)
Please see AP02002 at http://www.diodes.com/datasheets/ap02002.pdf for the latest version.
(3) U-DFN2020-3

Suggested Pad Layout
Please see AP02002 at http://www.diodes.com/datasheets/ap02002.pdf for the latest version.
(1) SOT23

(2) SC59

U-DFN2020-3
Dim Min Max Typ
A 0.57 0.63 0.60
A1 0 0.05 0.02
A3 - - 0.152
b 0.20 0.30 0.25
D 1.950 2.075 2.00
D2 1.10 1.30 1.20
D3 0.325 REF
e - - 0.50
E 1.950 2.075 2.00
E2 0.80 1.00 0.90
E3 0.138 REF
L 0.35 0.45 0.40
All Dimensions in mm
Dimensions Value (in mm)
Z 3.4
X 0.8
Y 1.0
C 2.4
E 1.35
Dimensions Value (in mm)
Z 3.4
X 0.8
Y 1
C 2.4
E 1.35
X E
Y
CZ
X E
Y
CZ
D
D2
E
e
b L
E2
A A1 A3
Seating Plane
Pin #1 ID
R0.200
E3
D3
L
AP2331
Document Number: DS35529  Rev. 5 - 2
10 of 12
www.diodes.com
September 2014
(c) Diodes Incorporated
```

### Page 11

```text
NEW PRODUCT
AP2331

Suggested Pad Layout (cont.)
Please see AP02002 at http://www.diodes.com/datasheets/ap02002.pdf for the latest version.
(3) U-DFN2020-3

Dimensions Value (in mm)
C 1.000
G 0.150
X 0.350
X1 0.450
X2 1.400
X3 1.724
Y 0.600
Y1 0.450
Y2 1.100
Y3 0.450
Y4 2.300
Y4
X3
X
Y
G
X1Y1
R0.200
R0.225
C
Y2
X2
Y3
R0.050
R0.200
AP2331
Document Number: DS35529  Rev. 5 - 2
11 of 12
www.diodes.com
September 2014
(c) Diodes Incorporated
```

### Page 12

```text
NEW PRODUCT
AP2331

IMPORTANT NOTICE

DIODES INCORPORATED MAKES NO WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, WITH REGARDS TO THIS
DOCUMENT,
INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE
(AND THEIR EQUIVALENTS UNDER THE LAWS OF ANY JURISDICTION).

Diodes Incorporated and its subsidiaries reserve the right to make modifications, enhancements,
improvements, corrections or other changes
without further notice to this document and any product described herein. Di odes Incorporated does
not assume any liability arising out of the
application or use of this document or any product described herein; neither does Diodes
Incorporated convey any license under its patent or
trademark rights, nor the rights of others.  Any  Customer or user of this document or products
described herein in such applications shall assume
all risks of such use and will agree to hold Diodes Incorporated and all the companies whose
products are represented on Diodes Incorporated
website, harmless against all damages.

Diodes Incorporated does not warrant or accept any liability whatsoever in respect of any products
purchased through unauthorized sales channel.
Should Customers purchase or use Diodes Incorporated products for any unintended or unauthorized
application, Customers shall indemnify and
hold Diodes Incorporated and its representatives harmless against all claims, damages, expenses, and
attorney fees arising out of, directly or
indirectly, any claim of personal injury or death associated with such unintended or unauthorized
application.

Products described herein may be covered by one or more United States, international or foreign
patents pending.  Product nam es and markings
noted herein may also be covered by one or more United States, international or foreign trademarks.

This document is written in English but may be translated into multiple languages for reference.
Only the English version of  this document is the
final and determinative format released by Diodes Incorporated.

LIFE SUPPORT

Diodes Incorporated products are specifically not authorized for use as critical components in life
support devices or system s without the express
written approval of the Chief Executive Officer of Diodes Incorporated. As used herein:

A.   Life support devices or systems are devices or systems which:

1. are intended to implant into the body, or

2. support or sustain life and whose failure to perform when properly used in accordance with
instructions for use provided in the
labeling can be reasonably expected to result in significant injury to the user.

B.   A critical component is any component in a life support device or system whose failure to
perform can be reasonably expected to cause the
failure of the life support device or to affect its safety or effectiveness.

Customers represent that they have all necessary expertise in the safety and regulatory
ramifications of their life support devices or systems, and
acknowledge and agree that they are solely responsible for all legal, regulatory and safety-related
requirements concerning their products and any
use of Diodes Incorporated products in such safety -critical, life support devices or systems,
notwithstanding any devices - or systems -related
information or support that may be provided by Diodes Incorporated.  Further, Customers must fully
indemnify Diodes Incorporated and its
representatives against any damages arising out of the use of Diodes Incorporated products in such
safety-critical, life support devices or systems.

Copyright (c) 2014, Diodes Incorporated

www.diodes.com

AP2331
Document Number: DS35529  Rev. 5 - 2
12 of 12
www.diodes.com
September 2014
(c) Diodes Incorporated
```
