# Specification AC72ABD AC77ABD AC82ABD AC85ABD AC90ABD - Bourns(R) Mini-Breaker TCO Devices

## Source Reference

- Source PDF: [Bourns-AC72ABD-datasheet.pdf](Bourns-AC72ABD-datasheet.pdf)
- Source path: `design\Datasheets\Bourns-AC72ABD-datasheet.pdf`
- Generated markdown: `Bourns-AC72ABD-datasheet.md`
- Page count: 6
- Extracted text characters: 19588
- Empty extraction pages: none
- Conversion method: automated local PDF text extraction with pypdf and pdfplumber

## Title and Part Identity

- Extracted title: Specification AC72ABD AC77ABD AC82ABD AC85ABD AC90ABD - Bourns(R) Mini-Breaker
  TCO Devices
- File stem / likely part identity: `Bourns-AC72ABD-datasheet`
- PDF metadata title: AC Series Breaker (Thermal Cutoff Device)
- PDF metadata subject: Bourns(R) Mini-Breaker TCO Devices
- Identity clue: n Miniature Thermal Cutoff (TCO) device
- Identity clue: n High current capacity, low impedance
- Identity clue: n Overtemperature and overcurrent protection
- Identity clue: for lithium polymer and prismatic cells
- Identity clue: n Controls abnormal, excessive current
- Identity clue: virtually instantaneously, up to rated limits
- Identity clue: n Wide range of temperature options
- Identity clue: Battery cell protection for:

## PDF Metadata

| Field | Value |
|:---|:---|
| Title | AC Series Breaker (Thermal Cutoff Device) |
| Author | Bourns, Inc. |
| Subject | Bourns(R) Mini-Breaker TCO Devices |
| Creator | Adobe InDesign 21.1 (Macintosh) |
| Producer | Adobe PDF Library 18.0 |

## Reviewed summary

### Curated design notes

- PDF review confirmed that this file is the Bourns AC Series Breaker family datasheet, with the AC72ABD variant called out by filename and the
  AC72ABD/AC77ABD/AC82ABD/AC85ABD/AC90ABD options all covered by the source PDF.
- The part is a 2-terminal battery-pack thermal cutoff / mini-breaker for notebook, tablet, and smartphone cell protection. The circuit diagram shows
  a normally closed series element that opens after a thermal/current trip.
- Ordering-code meaning from the PDF: AC = series, 72/77/82/85/90 = nominal trip temperature in deg C, A = Cu-alloy high-current arm, 1 or B = with or
  without projection, and D = black body color.
- Key ratings from page 1: AC72ABD trip temperature 72 deg C +/- 5 deg C, reset temperature 40 deg C minimum, DC 9 V / 35 A contact rating for 6000
  cycles, DC 5 V / 80 A maximum breaking current for 100 cycles, DC 28 V / 35 A maximum voltage, 3.5 V minimum holding voltage at 25 deg C for 1
  minute, 200 mA maximum leakage current at 25 deg C, and 2 mOhm maximum resistance (1 mOhm typical).
- Product-structure text on page 2 identifies the internal arm, terminal, cover, contact, cover plate, projection, bimetal disc, and PTC projection
  features. Page 3 states that wiring should use Ni-tab resistance or laser welding and that the device is not intended for reflow soldering.
- Mechanical and handling limits that were only loosely captured by the raw extraction are: body moment <= 10 N, body twist torque <= 1.5 cN-m, body
  bending force <= 20 N, terminal twist torque <= 0.6 cN-m, terminal force <= 2 N, terminal bend <= 45 deg at the root, and terminal twist <= 20 deg
  with the body affixed.
- Extraction limit: the current-vs-temperature curves and handling figures are image-based in the source PDF, so the curated notes above summarize the
  important limits while the raw extraction below preserves the searchable vendor text.

## Design-Relevant Extracted Content

These sections collect extracted snippets that are likely useful during design work, then the raw page-by-page text is preserved below for local search.

### Part number and ordering information

- Page 1: n Controls abnormal, excessive current / virtually instantaneously, up to rated limits / n
  Wide range of temperature options / Applications / Battery cell protection for:
- Page 3: CIRCUIT / AFTER OPENING / Typical Part Marking / Wiring Recommendations

### Pin, pad, and connection designations

- Page 1: Arm Material / A = Cu Alloy High Current Type / Terminal Type / 1 = With Projection / B =
  Without Projection
- Page 1: Users should verify actual device performance in their specific applications. / The
  products described herein and this document are subject to specific legal disclaimers as set forth
  on the last page of this document, and at www.bourns.com/docs/legal/disclaimer.pdf. / Terminal
  modifications including bending and extending are available upon request. / CALIFORNIA WARNING:
  Can expose you to lead, a carcinogen and reproductive toxicant. / See www.P65Warnings.ca.gov
- Page 2: AC90ABD(Low 85  degC average / ARM / TERMINAL / COVER / CONTACT
- Page 2: ARM / BASE / TERMINAL / BASE / AVAILABLE WITH AND WITHOUT PROJECTIONS.
- Page 3: Wiring Recommendations / This is not a surface mount device for reflow soldering.
  Therefore, Ni tab wiring should be accomplished by either resistance or laser welding. / Solder
  connections should be avoided. / Standard Packaging Specifications / Plastic
  Bag..................................................................................................................................................................................1,000
  pcs.
- Page 3: SPECIAL CODE / (D = BLACK BODY COLOR) / TERMINAL TYPE / 1 = WITH PROJECTION / B = WITHOUT
  PROJECTION
- Page 4: Caution when using Breaker / Before using the breaker, please fully read the DESIGN AND
  HANDLING CAUTIONS stated below to avoid breaker performance deterioration / and/or damage to the
  breaker body or terminal. / DESIGN CAUTIONS / 1. Use within the electrical ratings specified in
  this data sheet. If used over the rating of voltage or current, ON-OFF life might be impacted
- Page 4: 4. If the breaker is affixed with an adhesive (resin, etc.) before proceeding, fully test,
  evaluate and verify that the adhesive presents no / negative effects on the breaker. / 5. After
  the breaker is mounted, affix it so that the breaker body and terminals will not move. If not
  affixed properly, breaker resistance could / increase or contact could open due to stress during
  handling or vibration/shock during transportation. / 6. Mount the breaker body and terminals in a
  straight and flat direction. If the body and terminals are mounted in a twisted condition, breaker
- Page 4: negative effects on the breaker. / 5. After the breaker is mounted, affix it so that the
  breaker body and terminals will not move. If not affixed properly, breaker resistance could /
  increase or contact could open due to stress during handling or vibration/shock during
  transportation. / 6. Mount the breaker body and terminals in a straight and flat direction. If the
  body and terminals are mounted in a twisted condition, breaker / resistance could increase or
  create body damage.
- Page 4: 5. After the breaker is mounted, affix it so that the breaker body and terminals will not
  move. If not affixed properly, breaker resistance could / increase or contact could open due to
  stress during handling or vibration/shock during transportation. / 6. Mount the breaker body and
  terminals in a straight and flat direction. If the body and terminals are mounted in a twisted
  condition, breaker / resistance could increase or create body damage. / 7. If breaker is to be
  resin-molded, test and evaluate the application to determine whether the breaker can be used
  effectively.
- Page 5: 1. Since the breaker body is composed of plastic parts, do not clamp or dent with tools as
  this could cause a resistance increase or body / damage. / 2. Breaker terminals are thin
  copper-alloy with right angle edges. Handle carefully to avoid injury to fingers. Handling while
  wearing finger / cots and using tweezers is recommended. / 3. When welding breaker terminals or
  mounting the breaker on a cell or PCM board, be careful to avoid placing excessive stress on the
- Page 5: 2. Breaker terminals are thin copper-alloy with right angle edges. Handle carefully to
  avoid injury to fingers. Handling while wearing finger / cots and using tweezers is recommended. /
  3. When welding breaker terminals or mounting the breaker on a cell or PCM board, be careful to
  avoid placing excessive stress on the / breaker body and terminals. Excessive stress may cause a
  resistance increase or body damage. Please refer to the following cautions: / a) Do not apply more
  than 10 N moment to the breaker body (refer to Figure 1)
- Page 5: cots and using tweezers is recommended. / 3. When welding breaker terminals or mounting
  the breaker on a cell or PCM board, be careful to avoid placing excessive stress on the / breaker
  body and terminals. Excessive stress may cause a resistance increase or body damage. Please refer
  to the following cautions: / a) Do not apply more than 10 N moment to the breaker body (refer to
  Figure 1) / b) Do not apply more than 1.5 cN-m twist torque to the breaker body (refer to Figure
  2)
- Page 5: b) Do not apply more than 1.5 cN-m twist torque to the breaker body (refer to Figure 2) /
  c) Do not apply more than 20 N bending force to the breaker body (refer to Figure 3) / d) Do not
  apply more than 0.6 cN-m twist torque to the breaker terminals (refer to Figure 4) / e) Do not
  apply more than 2 N force to the breaker terminals (refer to Figure 5) / f) Do not bend terminals
  more than 45  deg at root (refer to Figure 6)
- Page 5: c) Do not apply more than 20 N bending force to the breaker body (refer to Figure 3) / d)
  Do not apply more than 0.6 cN-m twist torque to the breaker terminals (refer to Figure 4) / e) Do
  not apply more than 2 N force to the breaker terminals (refer to Figure 5) / f) Do not bend
  terminals more than 45  deg at root (refer to Figure 6) / g) Do not twist terminals more than 20
  deg with the breaker body affixed.
- Page 5: d) Do not apply more than 0.6 cN-m twist torque to the breaker terminals (refer to Figure
  4) / e) Do not apply more than 2 N force to the breaker terminals (refer to Figure 5) / f) Do not
  bend terminals more than 45  deg at root (refer to Figure 6) / g) Do not twist terminals more than
  20  deg with the breaker body affixed. / 4. In breaker body welding, normally there is direct
  welding (Figure 7) and series welding (Figure 8). In either case, use a suitable jig so that

### Specifications, ratings, and operating conditions

- Page 1: Features / n Miniature Thermal Cutoff (TCO) device / n High current capacity, low
  impedance / n Overtemperature and overcurrent protection
- Page 1: Features / n Miniature Thermal Cutoff (TCO) device / n High current capacity, low
  impedance / n Overtemperature and overcurrent protection / for lithium polymer and prismatic cells
- Page 1: n Miniature Thermal Cutoff (TCO) device / n High current capacity, low impedance / n
  Overtemperature and overcurrent protection / for lithium polymer and prismatic cells / n Controls
  abnormal, excessive current
- Page 1: n Overtemperature and overcurrent protection / for lithium polymer and prismatic cells / n
  Controls abnormal, excessive current / virtually instantaneously, up to rated limits / n Wide
  range of temperature options
- Page 1: n Tablet PCs / n Smart phones / AC Series Breaker (Thermal Cutoff Device) / Ratings /
  Specification AC72ABD AC77ABD AC82ABD AC85ABD AC90ABD
- Page 1: n Smart phones / AC Series Breaker (Thermal Cutoff Device) / Ratings / Specification
  AC72ABD AC77ABD AC82ABD AC85ABD AC90ABD / Trip Temperature 72  degC +/- 5  degC 77  degC +/- 5
  degC 82  degC +/- 5  degC 85  degC +/- 5  degC 90  degC +/- 5  degC
- Page 1: AC Series Breaker (Thermal Cutoff Device) / Ratings / Specification AC72ABD AC77ABD
  AC82ABD AC85ABD AC90ABD / Trip Temperature 72  degC +/- 5  degC 77  degC +/- 5  degC 82  degC +/-
  5  degC 85  degC +/- 5  degC 90  degC +/- 5  degC / Reset Temperature 40  degC min.
- Page 1: Reset Temperature 40  degC min. / Contact Rating DC9 V / 35 A, 6000 cycles / Maximum
  Breaking Current DC5 V / 80 A, 100 cycles / Maximum Voltage DC28 V / 35 A, 100 cycles / Minimum
  Holding Voltage 3.5 V @ 25  degC for 1 minute
- Page 1: Contact Rating DC9 V / 35 A, 6000 cycles / Maximum Breaking Current DC5 V / 80 A, 100
  cycles / Maximum Voltage DC28 V / 35 A, 100 cycles / Minimum Holding Voltage 3.5 V @ 25  degC for
  1 minute / Maximum Leakage Current 200 mA max. @ 25  degC
- Page 1: Maximum Breaking Current DC5 V / 80 A, 100 cycles / Maximum Voltage DC28 V / 35 A, 100
  cycles / Minimum Holding Voltage 3.5 V @ 25  degC for 1 minute / Maximum Leakage Current 200 mA
  max. @ 25  degC / Resistance 2 milliohms max. (1 milliohm typical)
- Page 1: Maximum Voltage DC28 V / 35 A, 100 cycles / Minimum Holding Voltage 3.5 V @ 25  degC for 1
  minute / Maximum Leakage Current 200 mA max. @ 25  degC / Resistance 2 milliohms max. (1 milliohm
  typical) / Agency RecognitionProduct Dimensions
- Page 1: - 90 / Arm Material / A = Cu Alloy High Current Type / Terminal Type / 1 = With Projection
- Page 1: -   The ambient temperature has dropped by 10  degC below the minimum trip temperature,
  and / -   Power to the TCO has been cycled (off/on) / Environmental Specifications / Moisture
  Sensitivity Level .........................1 / ESD Classification (HBM).......................3B
- Page 1: ** Bourns considers a product to be "halogen free" if (a) the Bromine (Br) content is 900
  ppm or less; (b) the Chlorine / (Cl) content is 900 ppm or less; and (c) the total Bromine (Br)
  and Chlorine (Cl) content is 1500 ppm or less. / Specifications are subject to change without
  notice. / Users should verify actual device performance in their specific applications. / The
  products described herein and this document are subject to specific legal disclaimers as set forth
  on the last page of this document, and at www.bourns.com/docs/legal/disclaimer.pdf.
- Page 2: Specifications are subject to change without notice. / Users should verify actual device
  performance in their specific applications. / The products described herein and this document are
  subject to specific legal disclaimers as set forth on the last page of this document, and at
  www.bourns.com/docs/legal/disclaimer.pdf.
- Page 2: Users should verify actual device performance in their specific applications. / The
  products described herein and this document are subject to specific legal disclaimers as set forth
  on the last page of this document, and at www.bourns.com/docs/legal/disclaimer.pdf. / AC Series
  Breaker (Thermal Cutoff Device) / Typical Performance / The above curves were derived from placing
  test samples in an oven at 25 C, 40 C, 60 C and so on, increasing current flow through the

### Dimensions, package, and mechanical information

- Page 1: Maximum Leakage Current 200 mA max. @ 25  degC / Resistance 2 milliohms max. (1 milliohm
  typical) / Agency RecognitionProduct Dimensions / Description / UL,
- Page 1: TUV File Number: R 50394595 / (EN 60730-2-9) / DIMENSIONS: MM / (INCHES) / How to Order

### Formulas, equations, and configurable calculations

- Page 3: 1)  The breaker must be stored in the original packaging (plastic bag or carton) with /
  the following conditions: ambient temperature of -10 to +40  degC, RH <=70 % with no / radical
  temperature change, direct sunshine, excessive vibration or shock. / 2)   Avoid storage locations
  where there is a possibility of generating corrosive gas / such as from salt breeze, chlorine,
  hudrogen sulfide, ammonium, sulfide-oxidation,
- Page 4: AC Series Breaker (Thermal Cutoff Device) / Caution when using Breaker / Before using the
  breaker, please fully read the DESIGN AND HANDLING CAUTIONS stated below to avoid breaker
  performance deterioration / and/or damage to the breaker body or terminal. / DESIGN CAUTIONS
- Page 4: negative effects on the breaker. / 5. After the breaker is mounted, affix it so that the
  breaker body and terminals will not move. If not affixed properly, breaker resistance could /
  increase or contact could open due to stress during handling or vibration/shock during
  transportation. / 6. Mount the breaker body and terminals in a straight and flat direction. If the
  body and terminals are mounted in a twisted condition, breaker / resistance could increase or
  create body damage.
- Page 4: 10.  The breaker is not designed or warranted for flow, reflow or hand-soldering
  applications. If such application is required, you will need to / evaluate whether the breaker is
  suitable for your specific application. / 11. When mounting and after mounting the breaker, do not
  apply supersonic vibration. Vibration and heat may cause breaker resistance / to increase or may
  cause body damage. If you plan to apply supersonic vibration after mounting the breaker, you will
  need to evaluate / whether the breaker is suitable for your specific application. The breaker is
  not designed or warranted to withstand supersonic vibration.
- Page 4: evaluate whether the breaker is suitable for your specific application. / 11. When
  mounting and after mounting the breaker, do not apply supersonic vibration. Vibration and heat may
  cause breaker resistance / to increase or may cause body damage. If you plan to apply supersonic
  vibration after mounting the breaker, you will need to evaluate / whether the breaker is suitable
  for your specific application. The breaker is not designed or warranted to withstand supersonic
  vibration. / 12. Do not use the breaker in the following environments:
- Page 4: 11. When mounting and after mounting the breaker, do not apply supersonic vibration.
  Vibration and heat may cause breaker resistance / to increase or may cause body damage. If you
  plan to apply supersonic vibration after mounting the breaker, you will need to evaluate / whether
  the breaker is suitable for your specific application. The breaker is not designed or warranted to
  withstand supersonic vibration. / 12. Do not use the breaker in the following environments: / a)
  Water, oil, chemical or organic solutions
- Page 6: environmental damage.  Unless expressly and specifically approved in writing by two
  authorized Bourns representatives on a / case-by-case basis, use of any Bourns(R) products in such
  unauthorized applications might not be safe and thus is at the user's / sole risk.  Life-critical
  applications include devices identified by the U.S. Food and Drug Administration as Class III
  devices and / generally equivalent classifications outside of the United States. / Bourns
  expressly identifies those Bourns(R) standard products that are suitable for use in automotive
  applications on such
- Page 6: automotive applications.  Any reference to Bourns(R) standard product in the data sheet as
  compliant with the AEC-Q standard / or "automotive grade" does not by itself mean that Bourns has
  approved such product for use in an automotive application. / Bourns(R) standard products are not
  tested to comply with United States Federal Aviation Administration standards generally / or any
  other generally equivalent governmental organization standard applicable to products designed or
  manufactured for / use in aircraft or space applications. Bourns expressly identifi

### Reference designs, applications, and examples

- Page 1: virtually instantaneously, up to rated limits / n Wide range of temperature options /
  Applications / Battery cell protection for: / n Notebook PCs
- Page 1: (Cl) content is 900 ppm or less; and (c) the total Bromine (Br) and Chlorine (Cl) content
  is 1500 ppm or less. / Specifications are subject to change without notice. / Users should verify
  actual device performance in their specific applications. / The products described herein and this
  document are subject to specific legal disclaimers as set forth on the last page of this document,
  and at www.bourns.com/docs/legal/disclaimer.pdf. / Terminal modifications including bending and
  extending are available upon request.
- Page 2: Specifications are subject to change without notice. / Users should verify actual device
  performance in their specific applications. / The products described herein and this document are
  subject to specific legal disclaimers as set forth on the last page of this document, and at
  www.bourns.com/docs/legal/disclaimer.pdf. / AC Series Breaker (Thermal Cutoff Device)
- Page 3: (72, 77, 82, 85, 90) / SERIES DESIGNATOR / Application Temperature Range /
  ........................................... -30 ~ 100  degC / Storage Conditions
- Page 4: 6. Mount the breaker body and terminals in a straight and flat direction. If the body and
  terminals are mounted in a twisted condition, breaker / resistance could increase or create body
  damage. / 7. If breaker is to be resin-molded, test and evaluate the application to determine
  whether the breaker can be used effectively. / 8. The breaker cannot be used as a repetitive
  ON-OFF thermostat. / 9.  The breaker is not washable. Do not wash.
- Page 4: 8. The breaker cannot be used as a repetitive ON-OFF thermostat. / 9.  The breaker is not
  washable. Do not wash. / 10.  The breaker is not designed or warranted for flow, reflow or
  hand-soldering applications. If such application is required, you will need to / evaluate whether
  the breaker is suitable for your specific application. / 11. When mounting and after mounting the
  breaker, do not apply supersonic vibration. Vibration and heat may cause breaker resistance
- Page 4: 9.  The breaker is not washable. Do not wash. / 10.  The breaker is not designed or
  warranted for flow, reflow or hand-soldering applications. If such application is required, you
  will need to / evaluate whether the breaker is suitable for your specific application. / 11. When
  mounting and after mounting the breaker, do not apply supersonic vibration. Vibration and heat may
  cause breaker resistance / to increase or may cause body damage. If you plan to apply supersonic
  vibration after mounting the breaker, you will need to evaluate
- Page 4: 11. When mounting and after mounting the breaker, do not apply supersonic vibration.
  Vibration and heat may cause breaker resistance / to increase or may cause body damage. If you
  plan to apply supersonic vibration after mounting the breaker, you will need to evaluate / whether
  the breaker is suitable for your specific application. The breaker is not designed or warranted to
  withstand supersonic vibration. / 12. Do not use the breaker in the following environments: / a)
  Water, oil, chemical or organic solutions
- Page 4: e) Strong static electric charge or electromagnetic wave / 13. The breaker is not designed
  or tested for, and should not be used in, aerospace, airplane, nuclear, military, life-saving,
  life-critical or / life-sustaining medical and other related applications where failure or
  malfunction may result in personal injury, death or severe property or / environmental damage.
- Page 5: REV. 01/26 / Specifications are subject to change without notice. / Users should verify
  actual device performance in their specific applications. / The products described herein and this
  document are subject to specific legal disclaimers as set forth on the last page of this document,
  and at www.bourns.com/docs/legal/disclaimer.pdf. / AC Series Breaker (Thermal Cutoff Device)
- Page 5: Due to possible updates to safety standards and other reasons, there may be changes in /
  specifications for this data sheet without prior notification. Therefore, before design-in for /
  your application, please contact us for the most up-to-date specifications.
- Page 6: complete before placing orders for Bourns(R) products. / The characteristics and
  parameters of a Bourns(R) product set forth in its data sheet are based on laboratory conditions,
  and / statements regarding the suitability of products for certain types of applications are based
  on Bourns' knowledge of typical / requirements in generic applications.  The characteristics and
  parameters of a Bourns(R) product in a user application may vary / from the data sheet
  characteristics and parameters due to (i) the combination of the Bourns(R) product with other
  components
- Page 6: The characteristics and parameters of a Bourns(R) product set forth in its data sheet are
  based on laboratory conditions, and / statements regarding the suitability of products for certain
  types of applications are based on Bourns' knowledge of typical / requirements in generic
  applications.  The characteristics and parameters of a Bourns(R) product in a user application may
  vary / from the data sheet characteristics and parameters due to (i) the combination of the
  Bourns(R) product with other components / in the user's application, or (ii) the environment of
  the user application itself.  The characteristics and parameters of a Bourns(R)
- Page 6: requirements in generic applications.  The characteristics and parameters of a Bourns(R)
  product in a user application may vary / from the data sheet characteristics and parameters due to
  (i) the combination of the Bourns(R) product with other components / in the user's application, or
  (ii) the environment of the user application itself.  The characteristics and parameters of a
  Bourns(R) / product also can and do vary in different applications and actual performance may vary
  over time.  Users should always verify / the actual performance of the Bourns(R) product in their
  specific devices and applications, and make their own independent
- Page 6: from the data sheet characteristics and parameters due to (i) the combination of the
  Bourns(R) product with other components / in the user's application, or (ii) the environment of
  the user application itself.  The characteristics and parameters of a Bourns(R) / product also can
  and do vary in different applications and actual performance may vary over time.  Users should
  always verify / the actual performance of the Bourns(R) product in their specific devices and
  applications, and make their own independent / judgments regarding the amount of additional test
  margin to design into their device or application to compensate for
- Page 6: in the user's application, or (ii) the environment of the user application itself.  The
  characteristics and parameters of a Bourns(R) / product also can and do vary in different
  applications and actual performance may vary over time.  Users should always verify / the actual
  performance of the Bourns(R) product in their specific devices and applications, and make their
  own independent / judgments regarding the amount of additional test margin to design into their
  device or application to compensate for / differences between laboratory and real world
  conditions.

## Page-by-Page Extracted Text

### Page 1

```text
Features
n Miniature Thermal Cutoff (TCO) device
n High current capacity, low impedance
n Overtemperature and overcurrent protection
for lithium polymer and prismatic cells
n Controls abnormal, excessive current
virtually instantaneously, up to rated limits
n Wide range of temperature options
Applications
Battery cell protection for:
n Notebook PCs
n Tablet PCs
n Smart phones
AC Series Breaker (Thermal Cutoff Device)
Ratings
Specification AC72ABD AC77ABD AC82ABD AC85ABD AC90ABD
Trip Temperature 72  degC +/- 5  degC 77  degC +/- 5  degC 82  degC +/- 5  degC 85  degC +/- 5  degC
90  degC +/- 5  degC
Reset Temperature 40  degC min.
Contact Rating DC9 V / 35 A, 6000 cycles
Maximum Breaking Current DC5 V / 80 A, 100 cycles
Maximum Voltage DC28 V / 35 A, 100 cycles
Minimum Holding Voltage 3.5 V @ 25  degC for 1 minute
Maximum Leakage Current 200 mA max. @ 25  degC
Resistance 2 milliohms max. (1 milliohm typical)
Agency RecognitionProduct Dimensions
Description
UL,
cUL
File Number: E215638
(UL 60730)
TUV File Number: R 50394595
(EN 60730-2-9)
DIMENSIONS: MM
(INCHES)
How to Order
AC  77  A  B  D

Series Designator
Trip Temperature (+/-5  degC)
- 72
- 77
- 82
- 85
- 90
Arm Material
A = Cu Alloy High Current Type
Terminal Type
1 = With Projection
B = Without Projection
Manufacturer's Internal Code
D = Black Body Color
X 2 7 2 5 KA C 9 0 A B D
1 0
A
D
A
D
Mini-breaker TCOs reset when the following conditions are met:
-   The ambient temperature has dropped by 10  degC below the minimum trip temperature, and
-   Power to the TCO has been cycled (off/on)
Environmental Specifications
Moisture Sensitivity Level .........................1
ESD Classification (HBM).......................3B
High Temperature, High Humidity
(60  degC, 90 % RH) .......................1,500 h
0.45
(.018)
DIA.
4 PLCS.
REF.
6.95 +/- 0.1
(.274 +/- .004)
NO OBJECT
2.7 +/- 0.1
(.106 +/- .004)
2.7 +/- 0.1
(.106 +/- .004)
0.25
(.010) MAX.
0.7 +/- 0.1
(.028 +/- .004)
2.5 +/- 0.1
(.098 +/- .004)
1.2 +/- 0.1
(.047 +/- .004)
2.5 +/- 0.1
(.098 +/- .004)
3.75 +/- 0.1
(.148 +/- .004)
3.95
(.156)MAX.
0.7 +/- 0.1
(.028 +/- .004)
1.6 +/- 0.1
(.063 +/- .004)
REF.
3.0 +/- 0.1
(.118 +/- .004)
REF.
0.3
(.012)R
1.10 +/- 0.05
(.043 +/- .002)
0.15 +/- 0.01
(.006 +/- .0004)
0.15 +/- 0.01
(.006 +/- .0004)
0.3 +/- 0.1
(.012 +/- .004) 0.3 +/- 0.1
(.012 +/- .004)
0.1
(.004)4 PLCS.
*    RoHS Directive 2015/863, Mar 31, 2015 and Annex.
** Bourns considers a product to be "halogen free" if (a) the Bromine (Br) content is 900 ppm or
less; (b) the Chlorine
(Cl) content is 900 ppm or less; and (c) the total Bromine (Br) and Chlorine (Cl) content is 1500
ppm or less.
Specifications are subject to change without notice.
Users should verify actual device performance in their specific applications.
The products described herein and this document are subject to specific legal disclaimers as set
forth on the last page of this document, and at www.bourns.com/docs/legal/disclaimer.pdf.
Terminal modifications including bending and extending are available upon request.
CALIFORNIA WARNING: Can expose you to lead, a carcinogen and reproductive toxicant.
See www.P65Warnings.ca.gov
Additional Information
Click these links for more information:
PRODUCT
SELECTOR
TECHNICAL
LIBRARY
INVENTORY SAMPLES CONTACT
```

### Page 2

```text
Specifications are subject to change without notice.
Users should verify actual device performance in their specific applications.
The products described herein and this document are subject to specific legal disclaimers as set
forth on the last page of this document, and at www.bourns.com/docs/legal/disclaimer.pdf.
AC Series Breaker (Thermal Cutoff Device)
Typical Performance
The above curves were derived from placing test samples in an oven at 25 C, 40 C, 60 C and so on,
increasing current flow through the
sample at a rate of 0.1 A/minute and recording the current value when the sample trips.
Current vs. Temperature Curves
Product Structure
Temperature ( degC)
Current (A)
0
5
10
15
20
25
30
35
40
20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100
AC72ABD(Low 67  degC average
AC77ABD(Low 72  degC average
AC82ABD(Low 77  degC average
AC85ABD(Low 80  degC average
AC90ABD(Low 85  degC average
ARM
TERMINAL
COVER
CONTACT
COVER PLATE
ARM
BASE
TERMINAL
BASE
AVAILABLE WITH AND WITHOUT PROJECTIONS.
PROJECTIONBIMETAL DISC
PTC PROJECTION
```

### Page 3

```text
Specifications are subject to change without notice.
Users should verify actual device performance in their specific applications.
The products described herein and this document are subject to specific legal disclaimers as set
forth on the last page of this document, and at www.bourns.com/docs/legal/disclaimer.pdf.
AC Series Breaker (Thermal Cutoff Device)
Circuit Diagram
NORMAL CIRCUIT
CIRCUIT
AFTER OPENING
Typical Part Marking

Wiring Recommendations
This is not a surface mount device for reflow soldering. Therefore, Ni tab wiring should be
accomplished by either resistance or laser welding.
Solder connections should be avoided.
Standard Packaging Specifications
Plastic
Bag..................................................................................................................................................................................1,000
pcs.
Inner Box
........................................................................................................................................................3,000
pcs. (3 bags per box)
Outer Box
....................................................................................................................................30,000
pcs. max. (up to 10 inner boxes)
X2725A
AC77A1D
02
DATE CODE:
MONTH (1~9, X, Y, Z)
DAY
YEAR
MACHINE NO.
ARABIC NUMERAL (01, 02, 03, ETC.) = OKAYAMA FACTORY
ALPHABET = SHIGA FACTORY
MANUFACTURER'S TRADEMARK
SPECIAL CODE
(D = BLACK BODY COLOR)
TERMINAL TYPE
1 = WITH PROJECTION
B = WITHOUT PROJECTION
MANUFACTURER'S
INTERNAL CODE
(ALPHANUMERIC CHARACTER)
ARM MATERIAL
(A = Cu ALLOY)
TRIP TEMPERATURE -  degC
(72, 77, 82, 85, 90)
SERIES DESIGNATOR
Application Temperature Range
........................................... -30 ~ 100  degC
Storage Conditions
1)  The breaker must be stored in the original packaging (plastic bag or carton) with
the following conditions: ambient temperature of -10 to +40  degC, RH <=70 % with no
radical temperature change, direct sunshine, excessive vibration or shock.
2)   Avoid storage locations where there is a possibility of generating corrosive gas
such as from salt breeze, chlorine, hudrogen sulfide, ammonium, sulfide-oxidation,
hydrogen chloride, acetate, etc.
3)  Storage period should be no longer than 24 months from date of shipment.
```

### Page 4

```text
Specifications are subject to change without notice.
Users should verify actual device performance in their specific applications.
The products described herein and this document are subject to specific legal disclaimers as set
forth on the last page of this document, and at www.bourns.com/docs/legal/disclaimer.pdf.
AC Series Breaker (Thermal Cutoff Device)
Caution when using Breaker
Before using the breaker, please fully read the DESIGN AND HANDLING CAUTIONS stated below to avoid
breaker performance deterioration
and/or damage to the breaker body or terminal.
DESIGN CAUTIONS
1. Use within the electrical ratings specified in this data sheet. If used over the rating of
voltage or current, ON-OFF life might be impacted
and contact may deteriorate due to breaker arm damage.
2. If used over the maximum electrical rating specified in this data sheet, the circuit may not open
safely or operate properly. Please test your
device for any abnormalities and confirm that the breaker will open the circuit safely in your
device. Any use over the maximum electrical
rating is at the sole risk of the user.
3. Mount the breaker on your device where heat is the highest in order to transfer it effectively to
the breaker.
4. If the breaker is affixed with an adhesive (resin, etc.) before proceeding, fully test, evaluate
and verify that the adhesive presents no
negative effects on the breaker.
5. After the breaker is mounted, affix it so that the breaker body and terminals will not move. If
not affixed properly, breaker resistance could
increase or contact could open due to stress during handling or vibration/shock during
transportation.
6. Mount the breaker body and terminals in a straight and flat direction. If the body and terminals
are mounted in a twisted condition, breaker
resistance could increase or create body damage.
7. If breaker is to be resin-molded, test and evaluate the application to determine whether the
breaker can be used effectively.
8. The breaker cannot be used as a repetitive ON-OFF thermostat.
9.  The breaker is not washable. Do not wash.
10.  The breaker is not designed or warranted for flow, reflow or hand-soldering applications. If
such application is required, you will need to
evaluate whether the breaker is suitable for your specific application.
11. When mounting and after mounting the breaker, do not apply supersonic vibration. Vibration and
heat may cause breaker resistance
to increase or may cause body damage. If you plan to apply supersonic vibration after mounting the
breaker, you will need to evaluate
whether the breaker is suitable for your specific application. The breaker is not designed or
warranted to withstand supersonic vibration.
12. Do not use the breaker in the following environments:
a) Water, oil, chemical or organic solutions
b) Direct sunlight, outdoor exposure, dust
c) Dew condensation, where the breaker could get wet
d) Salt breeze, chlorine, hydrogen sulfide, ammonium, sulfide-oxidation, hydrogen chloride, and
anywhere there is a possibility of
generating corrosive gas such as sulfurous acid gas
e) Strong static electric charge or electromagnetic wave
13. The breaker is not designed or tested for, and should not be used in, aerospace, airplane,
nuclear, military, life-saving, life-critical or
life-sustaining medical and other related applications where failure or malfunction may result in
personal injury, death or severe property or
environmental damage.
```

### Page 5

```text
REV. 01/26
Specifications are subject to change without notice.
Users should verify actual device performance in their specific applications.
The products described herein and this document are subject to specific legal disclaimers as set
forth on the last page of this document, and at www.bourns.com/docs/legal/disclaimer.pdf.
AC Series Breaker (Thermal Cutoff Device)
Caution when using Breaker (Continued)
HANDLING CAUTIONS
1. Since the breaker body is composed of plastic parts, do not clamp or dent with tools as this
could cause a resistance increase or body
damage.
2. Breaker terminals are thin copper-alloy with right angle edges. Handle carefully to avoid injury
to fingers. Handling while wearing finger
cots and using tweezers is recommended.
3. When welding breaker terminals or mounting the breaker on a cell or PCM board, be careful to
avoid placing excessive stress on the
breaker body and terminals. Excessive stress may cause a resistance increase or body damage. Please
refer to the following cautions:
a) Do not apply more than 10 N moment to the breaker body (refer to Figure 1)
b) Do not apply more than 1.5 cN-m twist torque to the breaker body (refer to Figure 2)
c) Do not apply more than 20 N bending force to the breaker body (refer to Figure 3)
d) Do not apply more than 0.6 cN-m twist torque to the breaker terminals (refer to Figure 4)
e) Do not apply more than 2 N force to the breaker terminals (refer to Figure 5)
f) Do not bend terminals more than 45  deg at root (refer to Figure 6)
g) Do not twist terminals more than 20  deg with the breaker body affixed.
4. In breaker body welding, normally there is direct welding (Figure 7) and series welding (Figure
8). In either case, use a suitable jig so that
stress will not exceed the limits stated above.
5. Pull-and-detach strength of the terminal welding should be to your own specification. If the
welding result is controlled by resistance,
measurement should be made at a close point to the breaker body by "DC 4-point clip method" using a
milliohm meter to ensure accuracy
(refer to Figure 9).
6. Avoid putting excessive stress as shown above in 3-a) to 3-g) when the jig is used for
welding/additional processing.
7. Confirm the resistance value after each time an additional process is applied.
Rod A
Rod B
Rod A
Figure 1 Figure 2
Figure 9
Figure 3 Figure 4
Figure 5 Figure 6 Figure 7 Figure 8
Rod B
45  deg
45  deg
45  deg
45  deg
milliohm meter
Due to possible updates to safety standards and other reasons, there may be changes in
specifications for this data sheet without prior notification. Therefore, before design-in for
your application, please contact us for the most up-to-date specifications.
```

### Page 6

```text
Legal Disclaimer Notice
This legal disclaimer applies to purchasers and users of Bourns(R) products manufactured by or on
behalf of Bourns, Inc. and its
affiliates (collectively, "Bourns").
Unless otherwise expressly indicated in writing, Bourns(R) products and data sheets relating thereto
are subject to change
without notice.  Users should check for and obtain the latest relevant information and verify that
such information is current and
complete before placing orders for Bourns(R) products.
The characteristics and parameters of a Bourns(R) product set forth in its data sheet are based on
laboratory conditions, and
statements regarding the suitability of products for certain types of applications are based on
Bourns' knowledge of typical
requirements in generic applications.  The characteristics and parameters of a Bourns(R) product in
a user application may vary
from the data sheet characteristics and parameters due to (i) the combination of the Bourns(R)
product with other components
in the user's application, or (ii) the environment of the user application itself.  The
characteristics and parameters of a Bourns(R)
product also can and do vary in different applications and actual performance may vary over time.
Users should always verify
the actual performance of the Bourns(R) product in their specific devices and applications, and make
their own independent
judgments regarding the amount of additional test margin to design into their device or application
to compensate for
differences between laboratory and real world conditions.
Unless Bourns has explicitly designated an individual Bourns(R) product as meeting the requirements
of a particular industry
standard (e.g., IATF 16949) or a particular qualification (e.g., UL listed or recognized), Bourns is
not responsible for any failure
of an individual Bourns(R) product to meet the requirements of such industry standard or particular
qualification.  Users of
Bourns(R) products are responsible for ensuring compliance with safety-related requirements and
standards applicable to their
devices or applications.
Bourns(R) products are not recommended, authorized or intended for use in nuclear, lifesaving,
life-critical or life-sustaining ap-
plications, nor in any other applications where failure or malfunction may result in personal
injury, death, or severe property or
environmental damage.  Unless expressly and specifically approved in writing by two authorized
Bourns representatives on a
case-by-case basis, use of any Bourns(R) products in such unauthorized applications might not be
safe and thus is at the user's
sole risk.  Life-critical applications include devices identified by the U.S. Food and Drug
Administration as Class III devices and
generally equivalent classifications outside of the United States.
Bourns expressly identifies those Bourns(R) standard products that are suitable for use in
automotive applications on such
products' data sheets in the section entitled "Applications."  Unless expressly and specifically
approved in writing by two
authorized Bourns representatives on a case-by-case basis, use of any other Bourns(R) standard
products in an automotive
application might not be safe and thus is not recommended, authorized or intended and is at the
user's sole risk.  If Bourns
expressly identifies a sub-category of automotive application in the data sheet for its standard
products (such as infotainment
or lighting), such identification means that Bourns has reviewed its standard product and has
determined that if such Bourns(R)
standard product is considered for potential use in automotive applications, it should only be used
in such sub-category of
automotive applications.  Any reference to Bourns(R) standard product in the data sheet as compliant
with the AEC-Q standard
or "automotive grade" does not by itself mean that Bourns has approved such product for use in an
automotive application.
Bourns(R) standard products are not tested to comply with United States Federal Aviation
Administration standards generally
or any other generally equivalent governmental organization standard applicable to products designed
or manufactured for
use in aircraft or space applications. Bourns expressly identifi
es Bourns(R) standard products that are suitable for use in aircraft
or space applications on such products' data sheets in the section entitled "Applications."  Unless
expressly and specifically
approved in writing by two authorized Bourns representatives on a case-by-case basis, use of any
other Bourns(R) standard
product in an aircraft or space application might not be safe and thus is not recommended,
authorized or intended and is at the
user's sole risk.
The use and level of testing applicable to Bourns(R) custom products shall be negotiated on a
case-by-case basis by Bourns and
the user for which such Bourns(R) custom products are specially designed.  Absent a written
agreement between Bourns and the
user regarding the use and level of such testing, the above provisions applicable to Bourns(R)
standard products shall also apply
to such Bourns(R) custom products.
Users shall not sell, transfer, export or re-export any Bourns(R) products or technology for use in
activities which involve the
design, development, production, use or stockpiling of nuclear, chemical or biological weapons or
missiles, nor shall they use
Bourns(R) products or technology in any facility which engages in activities relating to such
devices.  The foregoing restrictions
apply to all uses and applications that violate national or international prohibitions, including
embargos or international
regulations.  Further, Bourns(R) products and Bourns technology and technical data may not under any
circumstance be
exported or re-exported to countries subject to international sanctions or embargoes.  Bourns(R)
products may not, without prior
authorization from Bourns and/or the U.S. Government, be resold, transferred, or re-exported to any
party not eligible
to receive U.S. commodities, software, and technical data.
To the maximum extent permitted by applicable law, Bourns disclaims (i) any and all liability for
special, punitive, consequential,
incidental or indirect damages or lost revenues or lost profits, and (ii) any and all implied
warranties, including implied warranties
of fitness for particular purpose, non-infringement and merchantability.
For your convenience, copies of this Legal Disclaimer Notice with German, Spanish, Japanese,
Traditional Chinese and Simplified Chinese
bilingual versions are available at:
Web Page: http://www.bourns.com/legal/disclaimers-terms-and-policies
PDF: http://www.bourns.com/docs/Legal/disclaimer.pdf
C1753 12/14/23R
```
