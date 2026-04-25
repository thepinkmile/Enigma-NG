# Adafruit 4660 16 mm illuminated metal pushbutton family

## Source Reference

- Source PDF: [Adafruit-4660-datasheet.pdf](Adafruit-4660-datasheet.pdf)
- Source path: `design\Datasheets\Adafruit-4660-datasheet.pdf`
- Generated markdown: `Adafruit-4660-datasheet.md`
- Page count: 1
- Extracted text characters: 2067
- Empty extraction pages: none
- Conversion method: automated local PDF text extraction with pypdf and pdfplumber

## Title and Part Identity

- Reviewed identity: Adafruit product `4660` appears to be a 16 mm illuminated metal pushbutton family with optional
  single-color, dual-color, or tri-color ring lighting.
- The PDF metadata title (`2018-.cdr`) is not meaningful, so identity is based on the visible drawing, ordering codes,
  and the repository file name.
- Visible family features on page 1 include 16 mm panel cutout, `1NO1NC` contacts, `IP65` protection, and optional
  momentary or latching action.

## PDF Metadata

| Field | Value |
|:---|:---|
| Title | 2018-.cdr |
| Author | Administrator |
| Subject |  |
| Creator | pdfFactory Pro www.pdffactory.com |
| Producer | pdfFactory Pro 5.05 (Windows 7 Professional x64 Chinese (Simplified)) |

## Design-Relevant Extracted Content

These sections collect extracted snippets that are likely useful during design work, then the raw page-by-page text is preserved below for local search.

### Part number and ordering information

- Manual review: the ordering matrix uses blank for momentary action and `Z` for latching action.
- Manual review: LED option codes are blank for single color, `31` dual color common cathode, `32` dual color common
  anode, `41` tri-color common cathode, and `42` tri-color common anode.
- Manual review: body finish codes are `C` chrome-plated brass, `S` stainless steel, and `A` black-plated brass.
- Manual review: listed lamp-voltage options are `AC/DC 6V`, `12V`, `24V`, `110V`, and `220V`; the PDF also notes that
  DC LED and other voltages can be made to order.

### Pin, pad, and connection designations

- Manual review: switch contacts are `1NO1NC` with `2.8 x 0.5 mm` pin terminals.
- Manual review: the LED terminal arrangement includes a common LED pin plus separate color pins (`R`, `G`, `B`) for
  dual-color / tri-color options.
- Manual review: the page states that AC/DC LED versions are non-polarized at the lamp terminals, while unidirectional
  LED versions require distinguishing anode and cathode.

### Specifications, ratings, and operating conditions

- Manual review: switch rating is `0.5 A / 220 VAC`.
- Manual review: protection class is `IP65, IK08`.
- Manual review: page 1 lists panel thickness `1 mm to 8 mm`, torque about `0.6 Nm`, mechanical life `500,000 cycles`,
  electrical life `50,000 cycles`, actuation force about `1.7 N`, and actuation travel about `3 mm`.
- Manual review: lamp data calls out approximately `40,000 hours` reference life and `1 mA to 15 mA` rated current,
  with internal-resistor options for AC/DC lamps.

### Dimensions, package, and mechanical information

- Manual review: panel cutout is `16 mm`.
- Manual review: the page includes a mechanical outline plus terminal-arrangement sketches for the switch and LED
  variants.
- Manual review: actuator / body material options listed are stainless steel, chrome-plated brass, and black-plated
  brass with `PA` base material.

### Formulas, equations, and configurable calculations

- Manual review: no explicit formulas are given.
- Manual review: the closest thing to calculation guidance is the distinction between internal-resistor AC/DC lamp
  options and unidirectional LED versions that require correct polarity handling.

### Reference designs, applications, and examples

- Manual review: no end-application example is shown, but the PDF does include lamp circuit diagrams for single-color,
  dual-color, and tri-color options.

## Page-by-Page Extracted Text

### Page 1

```text
8
8 Max
1.5 32 12.6
0.7
13
Flat Actuator+Pin Terminal+Ring illuminati on(Dual colo r and tri-color availa ble)
Switch Function
LED options
LED Color
:

:

:

Blank indicates momentary
   Z  Latching
Blank indicates single color
   31 Dual color(common cathode)
   32 Dual color(common anode)
   41 Tri- color(common cathode)
   42 Tri-color(common anode)
Single color
   Tri-color
   Dual color
LED Voltage
Body
:
:
    C  Chrome plated
          brass
     S  Stainless steel
     A  Black plated
          brass
        AC/DC  6V
        AC/DC 12V
        AC/DC 24V
AC/DC  110V
        AC/DC  220V

Panel Cutout: 16mm
Rating: 0.5A/220VAC
Contact Configuration: 1NO1NC
Protection Class: IP65,IK 08
Pin Terminal(2.8  x 0.5mm)
Switching: C(Single-break slow-motion contact))
Panel Thickness: 1~8mm
Torque: About 0.6Nm
Mechanical Life: 500,000 cycles
Electrical Life: 50,000 cycles
Actuator: Stainless steel/Chrome plated brass/Black plated brass
Body: Stainless steel/Chrome plated brass/Black plated brass
Base: PA
Actuation Forc e: About 1.7N
Actuation Travel: About 3mm
              Compliant
DimensionSpecifications
Termi nal Arrangeme nt
b:LED ()pinG d:LED (B)pin
a:LED pin
C:LED
common pinC:LED pin a:LED ()pinR
Single color Dual color and Tri- color
C- R
G
B
C+ R
G
B
Tri-color Lam p Specificati on
Unidirection Tri-color LED
With internal resistor: DC12V, DC24V   DC6V,
Without Resistor:       1.8 2 8V,       2.8V   V,        .
Common Cathode Common Anode
3~15mA
Lamp Type
LED Color
Life
Rated Voltage
Lamp
Circuit
Diagram
Rated Current
40000hours Reference()
Single Color Lam p Specification
Two-way LED lamp (AC/DC)Lamp Type
LED Color
Life
Rated Voltage
Rated Current
Dropping Way
Lamp
Circuit
Diagram
AC/DC6V, AC/DC12V, AC DC24V, AC/DC110V,AC/DC220V/
40000hours Reference()
Note:  DC LED and other voltage can be made to order.
1~15mA
Inner resistor
Using AC/DCLED lamp, the terminals have no difference
of anode and cathode.
R
a b
 Using unidirection LED lamp,need distingnish
anode and cathode,Using inner resistor,do not
need connect outer resistor.
MM
```
