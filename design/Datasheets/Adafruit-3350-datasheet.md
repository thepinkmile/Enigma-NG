# Adafruit 3350 rugged metal pushbutton - 16 mm 6 V RGB, momentary

## Source Reference

- Source PDF: [Adafruit-3350-datasheet.pdf](Adafruit-3350-datasheet.pdf)
- Source path: `design\Datasheets\Adafruit-3350-datasheet.pdf`
- Generated markdown: `Adafruit-3350-datasheet.md`
- Page count: 2
- Extracted text characters: 2102
- Empty extraction pages: none
- Conversion method: automated local PDF text extraction with pypdf and pdfplumber

## Title and Part Identity

- Reviewed identity: Adafruit product `3350`, rugged metal pushbutton with 16 mm panel cutout, RGB ring LED, and
  momentary contacts.
- Product text on page 1: `Rugged Metal Pushbutton - 16mm 6V RGB` / `Momentary`.
- PDF metadata title is generic (`Microsoft Word - Document7`), so the product title was taken from the visible page
  content.

## PDF Metadata

| Field | Value |
|:---|:---|
| Title | Microsoft Word - Document7 |
| Author |  |
| Subject |  |
| Creator | PScript5.dll Version 5.2.2 |
| Producer | Acrobat Distiller 10.1.16 (Windows) |

## Design-Relevant Extracted Content

These sections collect extracted snippets that are likely useful during design work, then the raw page-by-page text is preserved below for local search.

### Part number and ordering information

- Manual review: this PDF corresponds to Adafruit product ID `3350`.
- Manual review: the visible product identity is `Rugged Metal Pushbutton - 16mm 6V RGB` with momentary switch action.

### Pin, pad, and connection designations

- Manual review: the switch has two button contacts plus four LED contacts.
- Manual review: the LED side uses one common anode and three cathodes for red, green, and blue.
- Manual review: the switch portion is normally open and is electrically separate from the LED ring.

### Specifications, ratings, and operating conditions

- Manual review: LED ring is intended for `3 V to 6 V` drive with an internal resistor.
- Manual review: for 12 V or 24 V use, the page recommends adding a `1 kOhm` series resistor to each LED cathode to
  keep LED current around `20 mA`.
- Manual review: page 2 lists switch recommendation `<= 1 A / 24 VDC`, contact resistance `< 50 mOhm`, insulation
  resistance `> 1000 Mohm`, operating temperature `-20 C to +55 C`, mechanical life `> 500,000`, and electrical life
  `> 50,000`.

### Dimensions, package, and mechanical information

- Manual review: drill / panel cutout diameter is `16 mm` and supported panel thickness is `1 mm to 7 mm`.
- Manual review: product dimensions are `22.0 mm x 22.0 mm x 19.5 mm` and weight is `11.6 g`.
- Manual review: page 2 also lists operating pressure `1.5 N to 2.5 N`, operating stroke `2 mm`, and chrome-plated
  brass construction.

### Formulas, equations, and configurable calculations

- Manual review: no formal equations are included.
- Manual review: the only explicit calculation guidance is the recommendation to add a `1 kOhm` series resistor per
  LED cathode for higher-voltage operation.

### Reference designs, applications, and examples

- Manual review: page 1 explains a typical usage pattern where a microcontroller reads the switch contacts and
  PWM-drives the RGB cathodes to generate color.
- Manual review: the enclosure guidance also notes a rubber gasket to help keep water out once the button is panel
  mounted.

## Page-by-Page Extracted Text

### Page 1

```text
Rugged Metal Pushbutton - 16mm 6V RGB
Momentary
PRODUCT  ID: 3350
By popular  demand,  we now have  these  buttons  with a full color  RGB LED ring light!  These
chrome -
plated  metal  buttons  are rugged,  but certainly  not lacking  in flair.  Simply  drill  a 16mm
hole into any
material  up to 1/4" thick  and you can fit these  in place  - there's  even a rubber  gasket  to
keep water
out of the enclosure.
On the front  of the button  is a flat metal  actuator,  surrounded  by a plastic  RGB
LED ring.  On the back there  are two gold contacts  for the button  and 4 for the RGB LED ring (one
anode
and 3 cathodes  for each  red, green,  and blue).  Power  the anode  at 3-6V and light  up the red,
green,
and blue  LEDs by pulling  their  designated  contacts  to ground  as you desire  - there's  a built
in resistor!
If you want  to use this with a higher  voltage,  say 12V or 24V, simp ly add  a 1K ohm resistor  in
series
with the LED cathodes  to keep  the LED current  at around  20mA.  You can PWM the RGB pins  to make
any color  you like.

This  button  is a momentary  push button,  when you press  it the 'normally -open'  contact  shorts
to the
common  cont
act. When  you release  it, the contacts  open up again.
The switch  and LED are electrically  separated,  so to change  the color,  use a microcontroller
to both
read the contact  pins and toggle  the color  control  pins.
```

### Page 2

```text
Technical Details
o Drill  hole diameter:  16mm
o Switch  current:  not rated,  we recommend  no more than  1A / 24VDC
o Switch  contacts:  1 set normally  open
o Material:  Chrome  plated  brass
o Contact  resistance:  < 50 mOhm
o Insulation  resistance:  > 1000  Mohm
o Temperature:  -20 C to +55 C
o Mechanical  life:  > 500,000
o Electrical  life:  > 50,000
o Panel  thickness:  1-7mm
o Operating  pressure:  1.5 - 2.5 N
o Operating  stroke:  2mm
o Lamp rated  voltage:  6V
Product  Dimensions:  22.0mm  x 22.0mm  x 19.5mm  / 0.9" x 0.9" x 0.8"
Product  Weight:  11.6g  / 0.4oz

https://www.adafruit.com/product/3350 2-12-18
```
