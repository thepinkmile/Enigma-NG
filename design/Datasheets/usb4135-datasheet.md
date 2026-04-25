# GCT USB4135 power-only USB Type-C receptacle family spec

## Source

- Source PDF: [usb4135-datasheet.pdf](usb4135-datasheet.pdf)
- Generated Markdown: `usb4135-datasheet.md`
- Page count: 10
- Conversion method: automated local extraction with pypdf and pdfplumber

## Reviewed Summary

- Family / part: GCT USB4125 / USB4130 / USB4135 power-only USB Type-C receptacle family; the file stem targets USB4135.
- Description: USB Type-C receptacle with 6 contacts for power charging only.
- Electrical: 48 VDC rating; 3.00 A collectively on VBUS pins A9 / B9; 4.25 A collectively on GND pins A12 / B12; 1.25 A on VCONN; operating range -30 to +85 degC.
- Performance: 40 mohm max LLCR, 100 Mohm min insulation resistance, 100 VAC dielectric test, and revision A3 notes durability increased to 20k cycles.
- Use the raw section for the full qualification table and revision history across pages 1-10.

## Extraction Notes

- Native extraction was usable but very verbose; this summary pulls the key connector facts to the top.

## Page-by-page extracted content

### Page 1

#### Extracted tables

Table 1:

```text
Part Number | USB4125, USB4130, USB4135 |  |  | Rev |  | A3 |  | Date | 20/12/24
Product Description | USB Type C Receptacle, 6 contacts, For Power Charging only |  |  |  |  |  |  | Page | 1
Doc Number | USB Type C | Prepared | YR |  | Checked |  | CC | Approved | PH
```

#### Raw extracted text

```text
PRODUCT SPECIFICATION

Part
Number USB4125, USB4130, USB4135 Rev A3 Date 20/12/24
Product
Description USB Type C Receptacle, 6 contacts, For Power Charging only Page  1
Doc
Number  USB Type C Prepared YR Checked CC Approved PH

www.gct.co

USB4125

USB4130

USB4135
```

### Page 2

#### Extracted tables

Table 1:

```text
Part Number | USB4125, USB4130, USB4135 |  |  | Rev |  | A3 |  | Date | 20/12/24
Product Description | USB Type C Receptacle, 6 contacts, For Power Charging only |  |  |  |  |  |  | Page | 2
Doc Number | USB Type C | Prepared | YR |  | Checked |  | CC | Approved | PH
```

Table 2:

```text
Test No | Item | Test Condition | Requirement
6.0.1 | Examination of Product | Visual, dimensional and functional inspection as per quality plan. | Product shall meet requirements of product drawing and specification.
 | Reseating | Manually plug/unplug 3 times | No physical damage
```

#### Raw extracted text

```text
PRODUCT SPECIFICATION

Part
Number USB4125, USB4130, USB4135 Rev A3 Date 20/12/24
Product
Description USB Type C Receptacle, 6 contacts, For Power Charging only Page  2
Doc
Number  USB Type C Prepared YR Checked CC Approved PH

www.gct.co

1.0 SCOPE
This specification covers performance, tests and quality requirements for the USB Type C
Receptacles, USB4125, USB4130 and USB4135.

2.0 PRODUCT NAME AND PART NUMBER
USB Type C Receptacles, USB4125, USB4130 and USB4135.

3.0 PRODUCT SHAPE, DIMENSIONS AND MATERIAL
           Please refer to drawings.

4.0 RATINGS
           4.1 Current rating: 3.00A collectively for VBUS pins(pins A9, B9)
4.25A collectively for GND pins(pins A12, B12)
1.25A for VCONN (pin A5/B5)
           4.2 Voltage rating ...........................  48V DC
           4.3 Operating Temperature Range ......  -30 deg C to +85 deg C

5.0 TEST AND MEASUREMENT CONDITIONS
        Product is designed to meet electrical, mechanical and environmental performance requirements
           specified below. All tests are performed in ambient conditions unless otherwise specified.

6.0 PERFORMANCE
Test No Item Test Condition Requirement
6.0.1
Examination of Product Visual, dimensional and functional
inspection as per quality plan.
Product shall meet requirements
of product drawing and
specification.
Reseating Manually plug/unplug 3 times No physical damage
```

### Page 3

#### Extracted tables

Table 1:

```text
Part Number | USB4125, USB4130, USB4135 |  |  | Rev |  | A3 |  | Date | 20/12/24
Product Description | USB Type C Receptacle, 6 contacts, For Power Charging only |  |  |  |  |  |  | Page | 3
Doc Number | USB Type C | Prepared | YR |  | Checked |  | CC | Approved | PH
```

Table 2:

```text
Test No | Item | Test Condition | Requirement
6.1.1 | Low Level Contact Resistance | The low level contact resistance measurement is made from the solder tail of the receptacle to the soldering point of the plug. When measured at 20mV Max. open circuit at 100mA. Mated test contacts must be in a connector housing. In accordance with EIA-364-23, Test Condition B | 40mOhm max (initial)
6.1.2 | Insulation Resistance | Both unmated and Mated connectors, apply 100V DC for 1 minute at sea level between adjacent terminal or ground. In accordance with EIA-364-21. | 100 MOhm Min (initial).
6.1.3 | Dielectric Strength | Mate connectors, apply 100V AC (RMS) for 1 minute at sea level. In accordance with EIA-364-20. | No Breakdown
6.1.4 | Contact current rating | A current of 3 A shall be applied collectively to VBUS pins (i.e., pins A9, B9) and 1.25 A shall be applied to the VCONN pin (i.e., B5) as applicable, terminated through the corresponding GND pins (i.e., pins A12, B12). A minimum current of 0.25 A shall also be applied individually to pin A5, as applicable. | The temperature rise shall not exceed 30 deg C at the outside surface of the shell.
```

#### Raw extracted text

```text
PRODUCT SPECIFICATION

Part
Number USB4125, USB4130, USB4135 Rev A3 Date 20/12/24
Product
Description USB Type C Receptacle, 6 contacts, For Power Charging only Page  3
Doc
Number  USB Type C Prepared YR Checked CC Approved PH

www.gct.co

6.1 Electrical Performance
Test No Item Test Condition Requirement
6.1.1 Low Level Contact
Resistance
The low level contact resistance measurement is
made from the solder tail of the receptacle to the
soldering point of the plug. When measured at
20mV Max. open circuit at 100mA. Mated test
contacts must be in a connector housing. In
accordance with EIA-364-23, Test Condition B
 40mOhm max (initial)
6.1.2 Insulation Resistance
Both unmated and Mated connectors, apply
100V DC for 1 minute at sea level between
adjacent terminal or ground. In accordance with
EIA-364-21.
100 MOhm Min (initial).
6.1.3 Dielectric Strength
Mate connectors, apply
100V AC (RMS) for 1 minute at sea level. In
accordance with EIA-364-20.
No Breakdown
6.1.4 Contact current rating
A current of 3 A shall be applied collectively to
VBUS pins (i.e., pins A9, B9) and 1.25 A shall be
applied to the VCONN pin (i.e., B5) as applicable,
terminated through the corresponding GND pins
(i.e., pins A12, B12).  A minimum current of 0.25 A
shall also be applied individually to pin A5, as
applicable.
The temperature
rise shall not
exceed 30 deg C at the
outside surface of
the shell.
```

### Page 4

#### Extracted tables

Table 1:

```text
Part Number | USB4125, USB4130, USB4135 |  |  | Rev |  | A3 |  | Date | 20/12/24
Product Description | USB Type C Receptacle, 6 contacts, For Power Charging only |  |  |  |  |  |  | Page | 4
Doc Number | USB Type C | Prepared | YR |  | Checked |  | CC | Approved | PH
```

Table 2:

```text
Test No | Item | Test Condition | Requirement
6.2.1 | Mating/Un-mating Force | Mate/Un-mated at a speed of 12.5mm/min. In accordance with EIA-364-13. | Mating force: within 5N to 20N (initial). Un-Mating force: within 8N to 20N up to 30cycles, within 6N to 20N after 20,000cycles
6.2.2 | Durability | 20,000 cycles at a cycle rate 500+/- 50 per hour. In accordance with EIA-364-09. (Replace the plug after 10K cycles) | Un-Mating force: within 6N to 20N Contact resistance: 50mOhm max Dielectric Strength: no breakdown
 | Durability (Preconditioning) | 50 cycles at a cycle rate 500+/- 50 per hour In accordance with EIA-364-09. | 
6.2.3 | Vibration | EIA 364-28 Test Condition VII, Test Letter D 15 minutes in each of 3 mutually perpendicular directions. Both mating halves should be rigidly fixed so as not to contribute to the relative motion of one contact against another. The method of fixturing should be detailed in the test report | No evidence of physical damage and no discontinuity longer than 1 microsecond. Contact resistance: 50mOhm max.
6.2.4 | 4-Axis Continuity | Shall be tested for continuity under stress using a test fixture | No evidence of physical damage and no discontinuity longer than 1 microsecond.
```

#### Raw extracted text

```text
PRODUCT SPECIFICATION

Part
Number USB4125, USB4130, USB4135 Rev A3 Date 20/12/24
Product
Description USB Type C Receptacle, 6 contacts, For Power Charging only Page  4
Doc
Number  USB Type C Prepared YR Checked CC Approved PH

www.gct.co

6.2 Mechanical Performance
Test No Item Test Condition Requirement
6.2.1 Mating/Un-mating
Force
Mate/Un-mated at a speed of 12.5mm/min.
In accordance with EIA-364-13.
Mating force: within
5N to 20N (initial).
Un-Mating force:
within 8N to 20N up
to 30cycles, within
6N to 20N after
20,000cycles
6.2.2
Durability
20,000 cycles at a
cycle rate 500+/- 50 per hour.
In accordance with EIA-364-09.
(Replace the plug after 10K cycles)
Un-Mating force:
within 6N to 20N
Contact resistance:
50mOhm max
Dielectric Strength:
no breakdown
Durability
(Preconditioning)
50 cycles at a
cycle rate 500+/- 50 per hour
In accordance with EIA-364-09. -
6.2.3 Vibration
EIA 364-28 Test Condition VII, Test Letter D
15 minutes in each of 3 mutually perpendicular
directions. Both mating halves should be rigidly
fixed so as not to contribute to the relative motion of
one contact against another. The method of
fixturing should be detailed in the test report
No evidence of
physical damage and
no discontinuity
longer than 1
microsecond.
Contact resistance:
50mOhm max.
6.2.4 4-Axis Continuity Shall be tested for continuity under stress using
a test fixture
No evidence of
physical damage and
no discontinuity
longer than 1
microsecond.
```

### Page 5

#### Extracted tables

Table 1:

```text
Part Number | USB4125, USB4130, USB4135 |  |  | Rev |  | A3 |  | Date | 20/12/24
Product Description | USB Type C Receptacle, 6 contacts, For Power Charging only |  |  |  |  |  |  | Page | 5
Doc Number | USB Type C | Prepared | YR |  | Checked |  | CC | Approved | PH
```

Table 2:

```text
Test No | Item | Test Condition | Requirement
6.3.1 | Cyclic Temperature and Humidity Test | Cycle the connector between 25 deg C +/-3 deg C at 80 % +/-3% RH and 65 deg C +/-3 deg C at 50 % +/-3% RH. Ramp times should be 0.5 hour and dwell times should be 1.0 hour. Dwell times start when the temperature and humidity have stabilized within the specified levels. Perform 24 such cycles. | Contact Resistance: 50mOhm Max.
6.3.2 | Salt Spray | Subject mated connectors to 5+/-1% salt-solution concentration, 35+/-2 deg C for 24 hours. In accordance with EIA-364-26, Test Condition B. | Shall meet visual requirements, No detrimental corrosion allowed in contact area and base metal exposed.
6.3.3 | Thermal Shock | Temperature range from -55 deg C~+85 deg C .Start from - 55 deg C. After 30 min. change to +85 deg C, change time is no more than 5min. Total 10 cycles. Test reference standard: EIA 364-32, test condition I | No physical damage. Contact Resistance (Low Level) 50m max.
6.3.4 | Solderability | Solder pot temperature: 250+/-5 deg C for 3~5 seconds. In accordance with EIA-364-52. | 95% of immersed area must show no voids, pin holes.
6.3.5 | Temperature life | 105o C without applied voltage for 120 hours. EIA-364-17, method A | Contact resistance: 50mOhm max
 | Temperature Life (preconditioning) | 105o C without applied voltage for 72 hours. EIA-364-17, method A | 
6.3.6 | Mixed flowing gas | EIA 364-65,Class II A Samples should be placed in an environmentally controlled test chamber that is monitored by a gas analyzing system for controlled concentrations of the specified gas mixture. Test coupons shall also be used and the weight gain reported. Test duration is 7 days. | Contact resistance: 50mOhm max
6.3.7 | Thermal disturbance | Cycle the connector or socket between 15 deg C +/-3 deg C and 85 deg C +/- 3 deg C, as measured on the part. Ramps should be a minimum of 2 deg C per minute, and dwell times should insure that the contacts reach the temperature extremes (a minimum of 5 minutes). Humidity is not controlled. Perform 10 such cycles. | Contact resistance: 50mOhm max
```

#### Raw extracted text

```text
PRODUCT SPECIFICATION

Part
Number USB4125, USB4130, USB4135 Rev A3 Date 20/12/24
Product
Description USB Type C Receptacle, 6 contacts, For Power Charging only Page  5
Doc
Number  USB Type C Prepared YR Checked CC Approved PH

www.gct.co

6.3 Environmental Performance and Others
Test No Item Test Condition Requirement
6.3.1 Cyclic Temperature
and Humidity Test
Cycle the connector between 25  deg C +/-3  deg C at 80 %
+/-3% RH and 65  deg C +/-3  deg C at 50 % +/-3% RH. Ramp
times should be 0.5 hour and dwell times should be
1.0 hour. Dwell times start when the temperature
and humidity have stabilized within the specified
levels. Perform 24 such cycles.
Contact Resistance:
50mOhm Max.
6.3.2 Salt Spray
Subject mated connectors to 5+/-1% salt-solution
concentration, 35+/-2 deg C for 24 hours. In accordance
with EIA-364-26, Test Condition B.
Shall meet visual
requirements, No
detrimental corrosion
allowed in contact
area and base metal
exposed.
6.3.3 Thermal Shock
Temperature range from -55 deg C~+85 deg C .Start from -
55 deg C. After 30 min. change to +85 deg C, change time
is no more than 5min. Total 10 cycles.
Test reference standard: EIA 364-32, test condition
I
No physical damage.
Contact Resistance
(Low Level) 50m
 max.
6.3.4 Solderability Solder pot temperature: 250+/-5 deg C for 3~5 seconds.
In accordance with EIA-364-52.
95% of immersed
area must show no
voids, pin holes.
6.3.5
Temperature life 105o C without applied voltage for 120 hours.
EIA-364-17, method A
Contact resistance:
50mOhm max
Temperature Life
(preconditioning)
105o C without applied voltage for 72 hours.
EIA-364-17, method A -
6.3.6 Mixed flowing gas
EIA 364-65,Class II A
Samples should be placed in an environmentally
controlled test chamber that is monitored by a gas
analyzing system for controlled concentrations of
the specified gas mixture. Test coupons shall also
be used and the weight gain reported.
Test duration is 7 days.
Contact resistance:
50mOhm max
6.3.7 Thermal disturbance
Cycle the connector or socket between 15  deg C +/-3  deg C
and 85  deg C +/- 3  deg C, as measured on the part. Ramps
should be a minimum of 2  deg C per minute, and dwell
times should insure that the contacts reach the
temperature extremes (a minimum of 5 minutes).
Humidity is not controlled. Perform 10 such cycles.
Contact resistance:
50mOhm max
```

### Page 6

#### Extracted tables

Table 1:

```text
Part Number | USB4125, USB4130, USB4135 |  |  | Rev |  | A3 |  | Date | 20/12/24
Product Description | USB Type C Receptacle, 6 contacts, For Power Charging only |  |  |  |  |  |  | Page | 6
Doc Number | USB Type C | Prepared | YR |  | Checked |  | CC | Approved | PH
```

Table 2:

```text
Parameter | Reference | Specification
Average temperature gradient in preheating |  | 2.5 deg C/s
Soak time | T soak | 2-3 minutes
Time above 217 deg C | T 1 | 60
Time above 230 deg C | T 2 | ss 50
Time above 250 deg C | T 3 | ss 5
Peak temperature in reflow | T peak | ss 255 deg C(-0/+5 deg C)
Temperature gradient in cooling |  | 5 deg C/s max
```

#### Raw extracted text

```text
PRODUCT SPECIFICATION

Part
Number USB4125, USB4130, USB4135 Rev A3 Date 20/12/24
Product
Description USB Type C Receptacle, 6 contacts, For Power Charging only Page  6
Doc
Number  USB Type C Prepared YR Checked CC Approved PH

www.gct.co

7.0   RESISTANCE TO INFRARED REFLOW SOLDERING HEAT
Parameter Reference Specification
Average temperature gradient in

preheating
 2.5 deg C/s
Soak time Tsoak 2-3 minutes
Time above 217 deg C T1 60
ss Time above 230 deg C T2 50
ss Time above 250 deg C T3 5
ss Peak temperature in reflow Tpeak 255 deg C(-0/+5 deg C)
Temperature gradient in cooling  -5 deg C/s max
Lead Free Process

This profile is the minimum requirement for evaluating soldering heat resistance of components. Heat
transfer method used for reflow soldering is hot air convection. The actual air temperatures used to
achieve the specified profile is higher and largely dependent on the reflow equipment.
```

### Page 7

#### Extracted tables

Table 1:

```text
Part Number | USB4125, USB4130, USB4135 |  |  | Rev |  | A3 |  | Date | 20/12/24
Product Description | USB Type C Receptacle, 6 contacts, For Power Charging only |  |  |  |  |  |  | Page | 7
Doc Number | USB Type C | Prepared | YR |  | Checked |  | CC | Approved | PH
```

Table 2:

```text
Test No | Description | Requirement
Group A-1 |  | 
6.0.1 | Examination | Visual inspection; No physical damage
6.1.1 | LLCR | 40mOhm Max all contacts
6.2.2 | Durability (preconditioning) | 50 cycles; No physical damage
6.3.5 | Temperature Life | 
6.1.1 | LLCR | 50mOhm Max all contacts
6.0.1 | Reseating | No physical damage
6.1.1 | LLCR | 50mOhm Max all contacts
6.0.1 | Examination | Visual inspection; No physical damage
Group A-2 |  | 
6.0.1 | Examination | Visual inspection; No physical damage
6.1.1 | LLCR | 40mOhm Max all contacts
6.2.2 | Durability (preconditioning) | 50 cycles; No physical damage
6.3.3 | Thermal Shock | 
6.1.1 | LLCR | 50mOhm Max all contacts
6.3.1 | Humidity | 
6.1.1 | LLCR | 50mOhm Max all contacts
6.0.1 | Reseating | No physical damage
6.1.1 | LLCR | 50mOhm Max all contacts
6.0.1 | Examination | Visual inspection; No physical damage
Group A-3 |  | 
6.0.1 | Examination | Visual inspection; No physical damage
6.1.1 | LLCR | 40mOhm Max all contacts
```

#### Raw extracted text

```text
PRODUCT SPECIFICATION

Part
Number USB4125, USB4130, USB4135 Rev A3 Date 20/12/24
Product
Description USB Type C Receptacle, 6 contacts, For Power Charging only Page  7
Doc
Number  USB Type C Prepared YR Checked CC Approved PH

www.gct.co

8.0   PRODUCT QUALIFICATION AND TEST SEQUENCE

Note: each group test needs 5pcs samples.

Test No Description  Requirement
Group A-1
6.0.1  Examination  Visual inspection; No physical damage
6.1.1  LLCR  40mOhm Max all contacts
6.2.2 Durability
(preconditioning)  50 cycles; No physical damage
6.3.5 Temperature Life
6.1.1 LLCR  50mOhm Max all contacts
6.0.1  Reseating  No physical damage
6.1.1 LLCR  50mOhm Max all contacts
6.0.1  Examination  Visual inspection; No physical damage

Group A-2
6.0.1 Examination  Visual inspection; No physical damage
6.1.1  LLCR  40mOhm Max all contacts
6.2.2  Durability
(preconditioning)  50 cycles; No physical damage
6.3.3 Thermal Shock
6.1.1 LLCR  50mOhm Max all contacts
6.3.1  Humidity
6.1.1  LLCR  50mOhm Max all contacts
6.0.1  Reseating  No physical damage
6.1.1  LLCR  50mOhm Max all contacts
6.0.1  Examination  Visual inspection; No physical damage

Group A-3
6.0.1  Examination  Visual inspection; No physical damage
6.1.1  LLCR  40mOhm Max all contacts
```

### Page 8

#### Extracted tables

Table 1:

```text
Part Number | USB4125, USB4130, USB4135 |  |  | Rev |  | A3 |  | Date | 20/12/24
Product Description | USB Type C Receptacle, 6 contacts, For Power Charging only |  |  |  |  |  |  | Page | 8
Doc Number | USB Type C | Prepared | YR |  | Checked |  | CC | Approved | PH
```

Table 2:

```text
| 6.2.2 | Durability (preconditioning) | 50 cycles; No physical damage | 
 | 6.3.5 | Temperature Life (preconditioning) |  | 
 | 6.1.1 | LLCR | 50mOhm Max all contacts | 
 | 6.2.3 | Vibration | Discontinuity less than 1us | 
 | 6.1.1 | LLCR | 50mOhm Max all contacts | 
 | 6.0.1 | Examination | Visual inspection; No physical damage | 
 | Group A-4 |  |  | 
 | 6.0.1 | Examination | Visual inspection; No physical damage | 
 | 6.1.1 | LLCR | 40mOhm Max all contacts | 
 | 6.2.2 | Durability (preconditioning) | 50 cycles; No physical damage | 
 | 6.3.5 | Temperature Life (preconditioning) |  | 
 | 6.1.1 | LLCR | 50mOhm Max all contacts | 
 | 6.3.6 | Mixed Flowing Gases |  | 
 | 6.1.1 | LLCR | 50mOhm Max all contacts | 
 | 6.3.7 | Thermal Disturbance |  | 
 | 6.1.1 | LLCR | 50mOhm Max all contacts | 
 | 6.0.1 | Reseating | No physical damage | 
 | 6.1.1 | LLCR | 50mOhm Max all contacts | 
 | 6.0.1 | Examination | Visual inspection; No physical damage | 
 | Group A-7 |  |  | 
 | 6.0.1 | Examination | Visual inspection; No physical damage | 
 | 6.1.3 | DWV | No breakdown or flashover | 
 | 6.1.1 | LLCR | 40mOhm Max all contacts | 
 | 6.2.2 | Durability (preconditioning) | No physical damage | 
 | 6.2.1 | Insertion Force | Within the range of 5N to 20N. | 
 | 6.2.1 | Extraction force | Within the range of 8N to 20N. Initial Reading | 
 | 6.2.2 | Durability | 25cycles, No physical damage |
```

#### Raw extracted text

```text
PRODUCT SPECIFICATION

Part
Number USB4125, USB4130, USB4135 Rev A3 Date 20/12/24
Product
Description USB Type C Receptacle, 6 contacts, For Power Charging only Page  8
Doc
Number  USB Type C Prepared YR Checked CC Approved PH

www.gct.co

6.2.2  Durability
(preconditioning)  50 cycles; No physical damage
6.3.5 Temperature Life
(preconditioning)
6.1.1 LLCR  50mOhm Max all contacts
6.2.3  Vibration  Discontinuity less than 1us
6.1.1  LLCR  50mOhm Max all contacts
6.0.1  Examination  Visual inspection; No physical damage

Group A-4
6.0.1  Examination  Visual inspection; No physical damage
6.1.1  LLCR  40mOhm Max all contacts
6.2.2  Durability
(preconditioning)  50 cycles; No physical damage
6.3.5 Temperature Life
(preconditioning)
6.1.1  LLCR  50mOhm Max all contacts
6.3.6 Mixed Flowing Gases
6.1.1  LLCR  50mOhm Max all contacts
6.3.7 Thermal Disturbance
6.1.1 LLCR 50mOhm Max all contacts
6.0.1  Reseating  No physical damage
6.1.1  LLCR  50mOhm Max all contacts
6.0.1  Examination  Visual inspection; No physical damage

Group A-7
6.0.1  Examination  Visual inspection; No physical damage
6.1.3  DWV  No breakdown or flashover
6.1.1  LLCR  40mOhm Max all contacts
6.2.2 Durability
(preconditioning)
No physical damage
6.2.1  Insertion Force  Within the range of 5N to 20N.
6.2.1  Extraction force  Within the range of 8N to 20N. Initial Reading
6.2.2  Durability  25cycles, No physical damage
```

### Page 9

#### Extracted tables

Table 1:

```text
Part Number | USB4125, USB4130, USB4135 |  |  | Rev |  | A3 |  | Date | 20/12/24
Product Description | USB Type C Receptacle, 6 contacts, For Power Charging only |  |  |  |  |  |  | Page | 9
Doc Number | USB Type C | Prepared | YR |  | Checked |  | CC | Approved | PH
```

Table 2:

```text
6.2.1 | Extraction force | Within: a) 33% of initial reading & b) 8N to 20N
6.2.2 | Durability | Perform 2468 cycles and then rotate the plug or socket 180 deg and then perform 2500 cycles. rotate the plug or socket 180 deg each 2500 cycles. No Physical damage. (Replace the plug after 10K cycles)
6.2.1 | Extraction force | Within the range of 6N to 20N.
6.1.1 | LLCR | 50mOhm Max all contacts
6.1.3 | DWV | No breakdown or flashover
6.1.2 | Insulation Resistance | 100 MOhm Max.
6.0.1 | Examination | Visual inspection; No physical damage
Group B-1 |  | 
6.0.1 | Examination | Visual inspection; No physical damage
6.2.4 | 4-Axis Continuity | Discontinuity less than 1us
6.0.1 | Examination | Visual inspection; No physical damage
Group B-6 |  | 
6.0.1 | Examination | Visual inspection; No physical damage
6.1.5 | Contact Current Rating | The Temperature Rise shall not exceed 30 deg C
6.0.1 | Examination | Visual inspection; No physical damage
```

#### Raw extracted text

```text
PRODUCT SPECIFICATION

Part
Number USB4125, USB4130, USB4135 Rev A3 Date 20/12/24
Product
Description USB Type C Receptacle, 6 contacts, For Power Charging only Page  9
Doc
Number  USB Type C Prepared YR Checked CC Approved PH

www.gct.co

6.2.1  Extraction force  Within: a) 33% of initial reading & b) 8N to 20N
6.2.2  Durability  Perform 2468 cycles and then rotate the plug or socket
180 deg  and then perform 2500 cycles. rotate the plug or
socket 180 deg  each 2500 cycles.
No Physical damage.
(Replace the plug after 10K cycles)
6.2.1  Extraction force  Within the range of 6N to 20N.
6.1.1  LLCR  50mOhm Max all contacts
6.1.3  DWV  No breakdown or flashover
6.1.2 Insulation Resistance 100 MOhm Max.
6.0.1  Examination  Visual inspection; No physical damage

Group B-1
6.0.1  Examination  Visual inspection; No physical damage
6.2.4 4-Axis Continuity Discontinuity less than 1us
6.0.1  Examination  Visual inspection; No physical damage

Group B-6
6.0.1  Examination  Visual inspection; No physical damage
6.1.5 Contact Current Rating The Temperature Rise shall not exceed 30 deg C
6.0.1  Examination  Visual inspection; No physical damage
```

### Page 10

#### Extracted tables

Table 1:

```text
Part Number | USB4125, USB4130, USB4135 |  |  | Rev |  | A3 |  | Date | 20/12/24
Product Description | USB Type C Receptacle, 6 contacts, For Power Charging only |  |  |  |  |  |  | Page | 10
Doc Number | USB Type C | Prepared | YR |  | Checked |  | CC | Approved | PH
```

Table 2:

```text
Revision | Information | Page | Release Date
A | Specification released. |  | 25/11/20
A1 | Change USB4125 durability from 10000 cycles to 20000 cycles | 3 | 26/05/21
A2 | Add USB4135 to the specification | 1&2 | 18/02/22
A3 | Voltage rating increased to 48Vdc - Durability increased to 20K cycles | 2, 4 & 9 | 20/12/2024
```

#### Raw extracted text

```text
PRODUCT SPECIFICATION

Part
Number USB4125, USB4130, USB4135 Rev A3 Date 20/12/24
Product
Description USB Type C Receptacle, 6 contacts, For Power Charging only Page  10
Doc
Number  USB Type C Prepared YR Checked CC Approved PH

www.gct.co

Revision details:
Revision Information Page Release Date
A Specification released. - 25/11/20
A1 Change USB4125 durability from 10000 cycles to
20000 cycles 3 26/05/21
A2 Add USB4135 to the specification 1&2 18/02/22
A3 - Voltage rating increased to 48Vdc
- Durability increased to 20K cycles 2, 4 & 9 20/12/2024
```
