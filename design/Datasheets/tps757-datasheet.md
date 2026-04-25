# Fast-Transient Response 3-A Low Dropout Voltage Regulators datasheet (Rev. E)

## Source

- Source PDF: [tps757-datasheet.pdf](tps757-datasheet.pdf)
- Generated Markdown: `tps757-datasheet.md`
- Page count: 30
- Conversion method: automated local extraction with pypdf and pdfplumber

## Extracted title and part identity

- Fast-Transient Response 3-A Low Dropout Voltage Regulators datasheet (Rev. E)
- tps757 datasheet
- C0116
- C0115
- C0110
- C0111
- C0114
- C0101

## Extraction summary

- Pages with substantial text extraction: 28/30
- Pages with extracted tables: 24/30
- Total extracted character count: 74759
- Extraction quality flag: usable

## PDF metadata

| Field | Value |
| --- | --- |
| Title | Fast-Transient Response 3-A Low Dropout Voltage Regulators datasheet (Rev. E) |
| Author | Texas Instruments, Incorporated [SLVS306,E ] |
| Subject | Data Sheet |
| Creator | SPDF |
| Producer | iText 2.1.7 by 1T3XT |

## Design-relevant extracted content

This section surfaces design-relevant snippets first. Full page-by-page raw extraction follows later for local search.

### Part number and ordering information

- /C0068Available in 1.5-V, 1.8-V, 2.5-V, and 3.3-V / Fixed-Output and Adjustable Versions / /C0068Open Drain Power-Good (PG) Status / Output (Fixed Options Only) / /C0068Dropout Voltage Typically 150 mV at 3 A / (TPS75733) / /C0068Low 125 uA Typical Quiescent Current
- /C0068Thermal Shutdown Protection / description / The TPS757xx family of 3-A low dropout (LDO) regulators contains four fixed voltage option regulators with / integrated power-good (PG / ) and an adjustable voltage option regulator. These devices are capable of supplying / 3 A of output current with a dropout of 150 mV (TPS75733). Therefore, the device is capable of performing a
- description / The TPS757xx family of 3-A low dropout (LDO) regulators contains four fixed voltage option regulators with / integrated power-good (PG / ) and an adjustable voltage option regulator. These devices are capable of supplying / 3 A of output current with a dropout of 150 mV (TPS75733). Therefore, the device is capable of performing a / 3.3-V to 2.5-V conversion. Quiescent current is 125 uA at full load and drops down to less than 1 uA when the / device is disabled. The TPS757xx is designed to have fast transient response for large load current changes.
- (programmable over the range of 1.22 V to 5 V). Output voltage tolerance is specified as a maximum of 3% over / line, load, and temperature ranges. The TPS757xx family is available in a 5-pin TO-220 (KC) and TO-263 (KTT) / packages. / AVAILABLE OPTIONS / OUTPUT VOLTAGE / TJ / (TYP)
- 1.5 V TPS75715KC TPS75715KTT / Adjustable 1.22 V to 5 V TPS75701KC TPS75701KTT / NOTE: The TPS75701 is programmable using an external resistor divider (see application / information). The KTT package is available taped and reeled. Add an R suffix to the / device type (e.g., TPS75701KTTR) to indicate tape and reel. / 2 5 / VI IN PG PG
- Adjustable 1.22 V to 5 V TPS75701KC TPS75701KTT / NOTE: The TPS75701 is programmable using an external resistor divider (see application / information). The KTT package is available taped and reeled. Add an R suffix to the / device type (e.g., TPS75701KTTR) to indicate tape and reel. / 2 5 / VI IN PG PG / 4
- GND / 3 / See application information section for capacitor selection details. / Figure 1. Typical Application Configuration (For Fixed Output Options) / 2 POST OFFICE BOX 655303 * DALLAS, TEXAS 75265 / TJ | OUTPUT VOLTAGE (TYP) | TO-220 (KC) | TO-263(KTT) / 4400 deg CC ttoo 112255 deg CC | 3.3 V | TPS75733KC | TPS75733KTT
- II//OO DDEESSCCRRIIPPTTIIOONN / NAME NO. / EN 1 I Enable input / FB/PG 5 I Feedback input voltage for adjustable device/PG output for fixed options / GND 3 Regulator ground / IN 2 I Input voltage / OUTPUT 4 O Regulated output voltage
- UVLO / TERMINAL NAME NO. | II//OO | DDEESSCCRRIIPPTTIIOONN / EN 1 | I | Enable input / FB/PG 5 | I | Feedback input voltage for adjustable device/PG output for fixed options / GND 3 | | Regulator ground / IN 2 | I | Input voltage / OUTPUT 4 | O | Regulated output voltage
- The EN terminal is an input which enables or shuts down the device. If EN is a logic high, the device will be in / shutdown mode. When EN goes to logic low, the device will be enabled. / power-good (PG) / The PG terminal for the fixed voltage option devices is an open drain, active low output that indicates the status / of V / O / (output of the LDO). When V
- O / condition) of the regulated voltage. The open drain output of the PG terminal requires a pullup resistor. / feedback (FB) / FB is an input terminal used for the adjustable-output option and must be connected to the output terminal either / directly, in order to generate the minimum output voltage of 1.22 V, or through an external feedback resistor / divider for other output voltages. The FB connection should be as short as possible. It is essential to route it in / such a way to minimize/avoid noise pickup. Adding RC networks between FB terminal and V to filter noise is
- Input voltage range, V . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . -0.3 V to 6 V / I / Voltage range at EN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . -0.3 V to 6 V / Maximum PG voltage (fixed options only) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6 V / Peak output current . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Internally limited / Continuous total power dissipation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . See Dissipation Rating Tables / Output voltage, V (OUTPUT, FB) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.5 V
- TPS75715 62 dB / rejection VI = 2.8 V, IO = 3 A / Minimum input voltage for valid PG IO(PG) = 300 uA, V(PG) <= 0.8 V 0 V / PG trip threshold voltage Fixed options only VO decreasing 89 93 %VO / PG hysteresis voltage Fixed options only Measured at VO 0.5 %VO / PG output low voltage Fixed options only VI = 2.8 V, IO(PG) = 1 mA 0.15 0.4 V / PG leakage current Fixed options only V(PG) = 5 V 1 uA
- rejection VI = 2.8 V, IO = 3 A / Minimum input voltage for valid PG IO(PG) = 300 uA, V(PG) <= 0.8 V 0 V / PG trip threshold voltage Fixed options only VO decreasing 89 93 %VO / PG hysteresis voltage Fixed options only Measured at VO 0.5 %VO / PG output low voltage Fixed options only VI = 2.8 V, IO(PG) = 1 mA 0.15 0.4 V / PG leakage current Fixed options only V(PG) = 5 V 1 uA / NOTES: 1. The adjustable option operates with a 2% tolerance over TJ = 0 to 125 deg C.
- Minimum input voltage for valid PG IO(PG) = 300 uA, V(PG) <= 0.8 V 0 V / PG trip threshold voltage Fixed options only VO decreasing 89 93 %VO / PG hysteresis voltage Fixed options only Measured at VO 0.5 %VO / PG output low voltage Fixed options only VI = 2.8 V, IO(PG) = 1 mA 0.15 0.4 V / PG leakage current Fixed options only V(PG) = 5 V 1 uA / NOTES: 1. The adjustable option operates with a 2% tolerance over TJ = 0 to 125 deg C. / 2. IO = 1 mA to 3 A
- PG trip threshold voltage Fixed options only VO decreasing 89 93 %VO / PG hysteresis voltage Fixed options only Measured at VO 0.5 %VO / PG output low voltage Fixed options only VI = 2.8 V, IO(PG) = 1 mA 0.15 0.4 V / PG leakage current Fixed options only V(PG) = 5 V 1 uA / NOTES: 1. The adjustable option operates with a 2% tolerance over TJ = 0 to 125 deg C. / 2. IO = 1 mA to 3 A / 3. If VO <= 2.5 V then VImin = 2.8 V, VImax = 5.5 V:
- PG hysteresis voltage Fixed options only Measured at VO 0.5 %VO / PG output low voltage Fixed options only VI = 2.8 V, IO(PG) = 1 mA 0.15 0.4 V / PG leakage current Fixed options only V(PG) = 5 V 1 uA / NOTES: 1. The adjustable option operates with a 2% tolerance over TJ = 0 to 125 deg C. / 2. IO = 1 mA to 3 A / 3. If VO <= 2.5 V then VImin = 2.8 V, VImax = 5.5 V: / (cid:2) (cid:4)
- FB input current | TPS75701 | FB = 1.5 V | 1 1 | uA / Power supply ripple rejection | TPS75715 | f = 100 Hz, TJ = 25 deg C, VI = 2.8 V, IO = 3 A | 62 | dB / Minimum input voltage for valid PG | | IO(PG) = 300 uA, V(PG) <= 0.8 V | 0 | V / PG trip threshold voltage | Fixed options only | VO decreasing | 89 93 | %VO / PG hysteresis voltage | Fixed options only | Measured at VO | 0.5 | %VO / PG output low voltage | Fixed options only | VI = 2.8 V, IO(PG) = 1 mA | 0.15 0.4 | V / PG leakage current | Fixed options only | V(PG) = 5 V | 1 | uA

### Pin, pad, and terminal designations

- /C0068Fast Transient Response / /C00683% Tolerance Over Specified Conditions for / Fixed-Output Versions / /C0068Available in 5-Pin TO-220 and TO-263 / Surface-Mount Packages / /C0068Thermal Shutdown Protection
- (typically 125 uA over the full range of output current). These two key specifications yield a significant / improvement in operating life for battery-powered systems. / The device is enabled when EN is connected to a low-level voltage. This LDO family also features a sleep mode; / applying a TTL high signal to EN (enable) shuts down the regulator, reducing the quiescent current to less than / 1 uA at T = 25 deg C. The power-good terminal (PG) is an active low, open drain output, which can be used to / J / implement a power-on reset or a low-battery indicator.
- improvement in operating life for battery-powered systems. / The device is enabled when EN is connected to a low-level voltage. This LDO family also features a sleep mode; / applying a TTL high signal to EN (enable) shuts down the regulator, reducing the quiescent current to less than / 1 uA at T = 25 deg C. The power-good terminal (PG) is an active low, open drain output, which can be used to / J / implement a power-on reset or a low-battery indicator. / The TPS757xx is offered in 1.5-V, 1.8-V, 2.5-V, and 3.3-V fixed-voltage versions and in an adjustable version
- implement a power-on reset or a low-battery indicator. / The TPS757xx is offered in 1.5-V, 1.8-V, 2.5-V, and 3.3-V fixed-voltage versions and in an adjustable version / (programmable over the range of 1.22 V to 5 V). Output voltage tolerance is specified as a maximum of 3% over / line, load, and temperature ranges. The TPS757xx family is available in a 5-pin TO-220 (KC) and TO-263 (KTT) / packages. / AVAILABLE OPTIONS / OUTPUT VOLTAGE
- (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:21)(cid:6) (cid:22)(cid:19)(cid:3)(cid:1)(cid:23)(cid:1)(cid:16)(cid:19)(cid:20)(cid:3)(cid:12)(cid:15)(cid:20)(cid:1) (cid:16)(cid:15)(cid:3)(cid:2)(cid:14)(cid:20)(cid:3)(cid:15) (cid:10)(cid:23)(cid:19) (cid:24)(cid:14)(cid:11)(cid:23)(cid:18)(cid:16)(cid:14)(cid:2)(cid:14)(cid:25)(cid:1) / (cid:26)(cid:14)(cid:24)(cid:1)(cid:19)(cid:17)(cid:15) (cid:16)(cid:15)(cid:17)(cid:25)(cid:24)(cid:19)(cid:1)(cid:14)(cid:16)(cid:3) / SLVS306E - NOVEMBER 2000 - REVISED FEBRUARY 2009 / functional block diagram-adjustable version / VIN VOUT / UVLO Current / Sense
- Bandgap / VIN / Reference / functional block diagram-fixed version / VIN VOUT / UVLO Current / Sense
- Reference / Falling / Edge Delay / Terminal Functions (TPS757xx) / TERMINAL / II//OO DDEESSCCRRIIPPTTIIOONN / NAME NO.
- Falling / Edge Delay / Terminal Functions (TPS757xx) / TERMINAL / II//OO DDEESSCCRRIIPPTTIIOONN / NAME NO. / EN 1 I Enable input
- GND 3 Regulator ground / IN 2 I Input voltage / OUTPUT 4 O Regulated output voltage / Thermal Pad - Connect to GND or Float / POST OFFICE BOX 655303 * DALLAS, TEXAS 75265 3 / | | R1 / UVLO
- Bandg Referen | ap / | ce / UVLO / TERMINAL NAME NO. | II//OO | DDEESSCCRRIIPPTTIIOONN / EN 1 | I | Enable input / FB/PG 5 | I | Feedback input voltage for adjustable device/PG output for fixed options / GND 3 | | Regulator ground
- GND 3 | | Regulator ground / IN 2 | I | Input voltage / OUTPUT 4 | O | Regulated output voltage / Thermal Pad | | Connect to GND or Float / (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:8)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:9)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:10)(cid:10) (cid:11)(cid:12)(cid:1)(cid:13) (cid:2)(cid:14)(cid:11)(cid:15)(cid:16) (cid:17)(cid:14)(cid:14)(cid:18) (cid:19)(cid:20)(cid:18) / (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:21)(cid:6) (cid:22)(cid:19)(cid:3)(cid:1)(cid:23)(cid:1)(cid:16)(cid:19)(cid:20)(cid:3)(cid:12)(cid:15)(cid:20)(cid:1) (cid:16)(cid:15)(cid:3)(cid:2)(cid:14)(cid:20)(cid:3)(cid:15) (cid:10)(cid:23)(cid:19) (cid:24)(cid:14)(cid:11)(cid:23)(cid:18)(cid:16)(cid:14)(cid:2)(cid:14)(cid:25)(cid:1) / (cid:26)(cid:14)(cid:24)(cid:1)(cid:19)(cid:17)(cid:15) (cid:16)(cid:15)(cid:17)(cid:25)(cid:24)(cid:19)(cid:1)(cid:14)(cid:16)(cid:3)
- detailed description / The TPS757xx family includes four fixed-output voltage regulators (1.5 V, 1.8 V, 2.5 V, and 3.3 V), and an / adjustable regulator, the TPS75701 (adjustable from 1.22 V to 5 V). The bandgap voltage is typically 1.22 V. / pin functions / enable (EN) / The EN terminal is an input which enables or shuts down the device. If EN is a logic high, the device will be in / shutdown mode. When EN goes to logic low, the device will be enabled.
- adjustable regulator, the TPS75701 (adjustable from 1.22 V to 5 V). The bandgap voltage is typically 1.22 V. / pin functions / enable (EN) / The EN terminal is an input which enables or shuts down the device. If EN is a logic high, the device will be in / shutdown mode. When EN goes to logic low, the device will be enabled. / power-good (PG) / The PG terminal for the fixed voltage option devices is an open drain, active low output that indicates the status
- The EN terminal is an input which enables or shuts down the device. If EN is a logic high, the device will be in / shutdown mode. When EN goes to logic low, the device will be enabled. / power-good (PG) / The PG terminal for the fixed voltage option devices is an open drain, active low output that indicates the status / of V / O / (output of the LDO). When V
- reaches approximately 91% of the regulated voltage, PG will go to a low / impedance state. It will go to a high-impedance state when V falls below approximately 89% (i.e. over load / O / condition) of the regulated voltage. The open drain output of the PG terminal requires a pullup resistor. / feedback (FB) / FB is an input terminal used for the adjustable-output option and must be connected to the output terminal either / directly, in order to generate the minimum output voltage of 1.22 V, or through an external feedback resistor
- O / condition) of the regulated voltage. The open drain output of the PG terminal requires a pullup resistor. / feedback (FB) / FB is an input terminal used for the adjustable-output option and must be connected to the output terminal either / directly, in order to generate the minimum output voltage of 1.22 V, or through an external feedback resistor / divider for other output voltages. The FB connection should be as short as possible. It is essential to route it in / such a way to minimize/avoid noise pickup. Adding RC networks between FB terminal and V to filter noise is
- feedback (FB) / FB is an input terminal used for the adjustable-output option and must be connected to the output terminal either / directly, in order to generate the minimum output voltage of 1.22 V, or through an external feedback resistor / divider for other output voltages. The FB connection should be as short as possible. It is essential to route it in / such a way to minimize/avoid noise pickup. Adding RC networks between FB terminal and V to filter noise is / O / not recommended because it may cause the regulator to oscillate.
- FB is an input terminal used for the adjustable-output option and must be connected to the output terminal either / directly, in order to generate the minimum output voltage of 1.22 V, or through an external feedback resistor / divider for other output voltages. The FB connection should be as short as possible. It is essential to route it in / such a way to minimize/avoid noise pickup. Adding RC networks between FB terminal and V to filter noise is / O / not recommended because it may cause the regulator to oscillate. / 4 POST OFFICE BOX 655303 * DALLAS, TEXAS 75265

### Specifications, ratings, and operating conditions

- /C0086/C0079/C0076/C0084/C0065/C0071/C0069 /C0082/C0069/C0071/C0085/C0076/C0065/C0084/C0079/C0082/C0083 / SLVS306E - NOVEMBER 2000 - REVISED FEBRUARY 2009 / 1POST OFFICE BOX 655303 * DALLAS, TEXAS 75265 / /C00683-A Low-Dropout Voltage Regulator / /C0068Available in 1.5-V, 1.8-V, 2.5-V, and 3.3-V / Fixed-Output and Adjustable Versions / /C0068Open Drain Power-Good (PG) Status
- Fixed-Output and Adjustable Versions / /C0068Open Drain Power-Good (PG) Status / Output (Fixed Options Only) / /C0068Dropout Voltage Typically 150 mV at 3 A / (TPS75733) / /C0068Low 125 uA Typical Quiescent Current / /C0068Fast Transient Response
- Output (Fixed Options Only) / /C0068Dropout Voltage Typically 150 mV at 3 A / (TPS75733) / /C0068Low 125 uA Typical Quiescent Current / /C0068Fast Transient Response / /C00683% Tolerance Over Specified Conditions for / Fixed-Output Versions
- (TPS75733) / /C0068Low 125 uA Typical Quiescent Current / /C0068Fast Transient Response / /C00683% Tolerance Over Specified Conditions for / Fixed-Output Versions / /C0068Available in 5-Pin TO-220 and TO-263 / Surface-Mount Packages
- Fixed-Output Versions / /C0068Available in 5-Pin TO-220 and TO-263 / Surface-Mount Packages / /C0068Thermal Shutdown Protection / description / The TPS757xx family of 3-A low dropout (LDO) regulators contains four fixed voltage option regulators with
- /C0068Thermal Shutdown Protection / description / The TPS757xx family of 3-A low dropout (LDO) regulators contains four fixed voltage option regulators with / integrated power-good (PG / ) and an adjustable voltage option regulator. These devices are capable of supplying / 3 A of output current with a dropout of 150 mV (TPS75733). Therefore, the device is capable of performing a
- description / The TPS757xx family of 3-A low dropout (LDO) regulators contains four fixed voltage option regulators with / integrated power-good (PG / ) and an adjustable voltage option regulator. These devices are capable of supplying / 3 A of output current with a dropout of 150 mV (TPS75733). Therefore, the device is capable of performing a / 3.3-V to 2.5-V conversion. Quiescent current is 125 uA at full load and drops down to less than 1 uA when the / device is disabled. The TPS757xx is designed to have fast transient response for large load current changes.
- The TPS757xx family of 3-A low dropout (LDO) regulators contains four fixed voltage option regulators with / integrated power-good (PG / ) and an adjustable voltage option regulator. These devices are capable of supplying / 3 A of output current with a dropout of 150 mV (TPS75733). Therefore, the device is capable of performing a / 3.3-V to 2.5-V conversion. Quiescent current is 125 uA at full load and drops down to less than 1 uA when the / device is disabled. The TPS757xx is designed to have fast transient response for large load current changes. / t - Time - us
- integrated power-good (PG / ) and an adjustable voltage option regulator. These devices are capable of supplying / 3 A of output current with a dropout of 150 mV (TPS75733). Therefore, the device is capable of performing a / 3.3-V to 2.5-V conversion. Quiescent current is 125 uA at full load and drops down to less than 1 uA when the / device is disabled. The TPS757xx is designed to have fast transient response for large load current changes. / t - Time - us / TPS75715
- ) and an adjustable voltage option regulator. These devices are capable of supplying / 3 A of output current with a dropout of 150 mV (TPS75733). Therefore, the device is capable of performing a / 3.3-V to 2.5-V conversion. Quiescent current is 125 uA at full load and drops down to less than 1 uA when the / device is disabled. The TPS757xx is designed to have fast transient response for large load current changes. / t - Time - us / TPS75715 / LOAD TRANSIENT RESPONSE
- t - Time - us / TPS75715 / LOAD TRANSIENT RESPONSE / I - Output Current - AO / VO - Change in Output Voltage - mV / 100 / 0
- TPS75715 / LOAD TRANSIENT RESPONSE / I - Output Current - AO / VO - Change in Output Voltage - mV / 100 / 0 / 06 0 4020 80 100 140 120 160 180 200
- 250 / 40 -25 -10 5 20 35 50 65 80 95 110 125 / TJ - Junction Temperature - deg C / Dropout Voltage - mV / TPS75733 / DROPOUT VOLTAGE / vs
- TJ - Junction Temperature - deg C / Dropout Voltage - mV / TPS75733 / DROPOUT VOLTAGE / vs / JUNCTION TEMPERATURE / VDO
- (cid:26)(cid:14)(cid:24)(cid:1)(cid:19)(cid:17)(cid:15) (cid:16)(cid:15)(cid:17)(cid:25)(cid:24)(cid:19)(cid:1)(cid:14)(cid:16)(cid:3) / SLVS306E - NOVEMBER 2000 - REVISED FEBRUARY 2009 / description (continued) / Because the PMOS device behaves as a low-value resistor, the dropout voltage is low (typically 150 mV at an / output current of 3 A for the TPS75733) and is directly proportional to the output current. Additionally, since the / PMOS pass element is a voltage-driven device, the quiescent current is low and independent of output loading / (typically 125 uA over the full range of output current). These two key specifications yield a significant
- SLVS306E - NOVEMBER 2000 - REVISED FEBRUARY 2009 / description (continued) / Because the PMOS device behaves as a low-value resistor, the dropout voltage is low (typically 150 mV at an / output current of 3 A for the TPS75733) and is directly proportional to the output current. Additionally, since the / PMOS pass element is a voltage-driven device, the quiescent current is low and independent of output loading / (typically 125 uA over the full range of output current). These two key specifications yield a significant / improvement in operating life for battery-powered systems.
- description (continued) / Because the PMOS device behaves as a low-value resistor, the dropout voltage is low (typically 150 mV at an / output current of 3 A for the TPS75733) and is directly proportional to the output current. Additionally, since the / PMOS pass element is a voltage-driven device, the quiescent current is low and independent of output loading / (typically 125 uA over the full range of output current). These two key specifications yield a significant / improvement in operating life for battery-powered systems. / The device is enabled when EN is connected to a low-level voltage. This LDO family also features a sleep mode;
- Because the PMOS device behaves as a low-value resistor, the dropout voltage is low (typically 150 mV at an / output current of 3 A for the TPS75733) and is directly proportional to the output current. Additionally, since the / PMOS pass element is a voltage-driven device, the quiescent current is low and independent of output loading / (typically 125 uA over the full range of output current). These two key specifications yield a significant / improvement in operating life for battery-powered systems. / The device is enabled when EN is connected to a low-level voltage. This LDO family also features a sleep mode; / applying a TTL high signal to EN (enable) shuts down the regulator, reducing the quiescent current to less than

### Dimensions, package, and mechanical information

- /C00683% Tolerance Over Specified Conditions for / Fixed-Output Versions / /C0068Available in 5-Pin TO-220 and TO-263 / Surface-Mount Packages / /C0068Thermal Shutdown Protection / description
- /C0115/C0116/C0097/C0110/C0100/C0097/C0114/C0100 /C0119/C0097/C0114/C0114/C0097/C0110/C0116/C0121/C0046 /C0080/C0114/C0111/C0100/C0117/C0099/C0116/C0105/C0111/C0110 /C0112/C0114/C0111/C0099/C0101/C0115/C0115/C0105/C0110/C0103 /C0100/C0111/C0101/C0115 /C0110/C0111/C0116 /C0110/C0101/C0099/C0101/C0115/C0115/C0097/C0114/C0105/C0108/C0121 /C0105/C0110/C0099/C0108/C0117/C0100/C0101 / /C0116/C0101/C0115/C0116/C0105/C0110/C0103 /C0111/C0102 /C0097/C0108/C0108 /C0112/C0097/C0114/C0097/C0109/C0101/C0116/C0101/C0114/C0115/C0046 / Copyright 2009, Texas Instruments Incorporated / TO-220 (KC) PACKAGE / (TOP VIEW) / 1 / 2
- OUTPUT / FB/PG / 1 / TO-263 (KTT) PACKAGE / (TOP VIEW) / 2 / 3
- The TPS757xx is offered in 1.5-V, 1.8-V, 2.5-V, and 3.3-V fixed-voltage versions and in an adjustable version / (programmable over the range of 1.22 V to 5 V). Output voltage tolerance is specified as a maximum of 3% over / line, load, and temperature ranges. The TPS757xx family is available in a 5-pin TO-220 (KC) and TO-263 (KTT) / packages. / AVAILABLE OPTIONS / OUTPUT VOLTAGE / TJ
- 1.5 V TPS75715KC TPS75715KTT / Adjustable 1.22 V to 5 V TPS75701KC TPS75701KTT / NOTE: The TPS75701 is programmable using an external resistor divider (see application / information). The KTT package is available taped and reeled. Add an R suffix to the / device type (e.g., TPS75701KTTR) to indicate tape and reel. / 2 5 / VI IN PG PG
- implied. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability. / All voltage values are with respect to network terminal ground. / DISSIPATION RATING TABLE / PACKAGE RJC ( deg C/W) RJA ( deg C/W) / TO-220 2 58.7 / TO-263 2 38.7# / For both packages, the RJA values were computed using JEDEC high K board (2S2P)
- PACKAGE RJC ( deg C/W) RJA ( deg C/W) / TO-220 2 58.7 / TO-263 2 38.7# / For both packages, the RJA values were computed using JEDEC high K board (2S2P) / with 1 ounce internal copper plane and ground plane. There was no air flow across the / packages. / RJA was computed assuming a vertical, free standing TO-220 package with pins
- TO-263 2 38.7# / For both packages, the RJA values were computed using JEDEC high K board (2S2P) / with 1 ounce internal copper plane and ground plane. There was no air flow across the / packages. / RJA was computed assuming a vertical, free standing TO-220 package with pins / soldered to the board. There is no heatsink attached to the package. / #RJA was computed assuming a horizontally mounted TO-263 package with pins
- For both packages, the RJA values were computed using JEDEC high K board (2S2P) / with 1 ounce internal copper plane and ground plane. There was no air flow across the / packages. / RJA was computed assuming a vertical, free standing TO-220 package with pins / soldered to the board. There is no heatsink attached to the package. / #RJA was computed assuming a horizontally mounted TO-263 package with pins / soldered to the board. There is no copper pad underneath the package.
- with 1 ounce internal copper plane and ground plane. There was no air flow across the / packages. / RJA was computed assuming a vertical, free standing TO-220 package with pins / soldered to the board. There is no heatsink attached to the package. / #RJA was computed assuming a horizontally mounted TO-263 package with pins / soldered to the board. There is no copper pad underneath the package. / recommended operating conditions
- packages. / RJA was computed assuming a vertical, free standing TO-220 package with pins / soldered to the board. There is no heatsink attached to the package. / #RJA was computed assuming a horizontally mounted TO-263 package with pins / soldered to the board. There is no copper pad underneath the package. / recommended operating conditions / MIN MAX UNIT
- RJA was computed assuming a vertical, free standing TO-220 package with pins / soldered to the board. There is no heatsink attached to the package. / #RJA was computed assuming a horizontally mounted TO-263 package with pins / soldered to the board. There is no copper pad underneath the package. / recommended operating conditions / MIN MAX UNIT / Input voltage, VI || 2.8 5.5 V
- Operating virtual junction temperature, TJ -40 125 deg C / || To calculate the minimum input voltage for your maximum output current, use the following equation: VI(min) = VO(max) + VDO(max load). / POST OFFICE BOX 655303 * DALLAS, TEXAS 75265 5 / PACKAGE | RJC ( deg C/W) | RJA ( deg C/W) / TO-220 | 2 | 58.7 / TO-263 | 2 | 38.7# / | MIN MAX | UNIT
- resistances between the junction and the case (RJC ), the case to heatsink (RCS ), and the heatsink to ambient / (RSA ). Thermal resistances are measures of how effectively an object dissipates heat. Typically, the larger the / device, the more surface area available for power dissipation and the lower the objects thermal resistance. / Figure 21 illustrates these thermal resistances for (a) a TO-220 package attached to a heatsink, and (b) a / TO-263 package mounted on a JEDEC High-K board. / C / B A TJ
- (RSA ). Thermal resistances are measures of how effectively an object dissipates heat. Typically, the larger the / device, the more surface area available for power dissipation and the lower the objects thermal resistance. / Figure 21 illustrates these thermal resistances for (a) a TO-220 package attached to a heatsink, and (b) a / TO-263 package mounted on a JEDEC High-K board. / C / B A TJ / A
- C / RSA / C / TO-263 Package / TA (b) / TO-220 Package / (a)
- C / TO-263 Package / TA (b) / TO-220 Package / (a) / Figure 21. Thermal Resistances / POST OFFICE BOX 655303 * DALLAS, TEXAS 75265 13
- (cid:2) (cid:4) / T (cid:1) T (cid:7)P maxx R (cid:7) R (cid:7) R (2) / J A D JC CS SA / The RJC is specific to each regulator as determined by its package, lead frame, and die size provided in the / regulators datasheet. The RSA is a function of the type and size of heatsink. For example, black body radiator / type heatsinks, like the one attached to the TO-220 package in Figure 21(a), can have RCS values ranging / from 5 deg C/W for very large heatsinks to 50 deg C/W for very small heatsinks. The RCS is a function of how the

### Formulas, equations, and configuration calculations

- 4400 deg CC ttoo 112255 deg CC 1.8 V TPS75718KC TPS75718KTT / 1.5 V TPS75715KC TPS75715KTT / Adjustable 1.22 V to 5 V TPS75701KC TPS75701KTT / NOTE: The TPS75701 is programmable using an external resistor divider (see application / information). The KTT package is available taped and reeled. Add an R suffix to the / device type (e.g., TPS75701KTTR) to indicate tape and reel. / 2 5
- GND / 3 / See application information section for capacitor selection details. / Figure 1. Typical Application Configuration (For Fixed Output Options) / 2 POST OFFICE BOX 655303 * DALLAS, TEXAS 75265 / TJ | OUTPUT VOLTAGE (TYP) | TO-220 (KC) | TO-263(KTT) / 4400 deg CC ttoo 112255 deg CC | 3.3 V | TPS75733KC | TPS75733KTT
- SLVS306E - NOVEMBER 2000 - REVISED FEBRUARY 2009 / functional block diagram-adjustable version / VIN VOUT / UVLO Current / Sense / SHUTDOWN / ILIM
- UVLO Current / Sense / SHUTDOWN / ILIM / R1 / GND _ + / FB
- GND _ + / FB / EN / UVLO / R2 / Thermal / Shutdown External to
- Reference / functional block diagram-fixed version / VIN VOUT / UVLO Current / Sense / SHUTDOWN / ILIM
- UVLO Current / Sense / SHUTDOWN / ILIM / R1 / _ / +
- _ / + / GND / UVLO / EN R2 / Thermal / Shutdown
- Thermal Pad - Connect to GND or Float / POST OFFICE BOX 655303 * DALLAS, TEXAS 75265 3 / | | R1 / UVLO / Bandg Referen | ap / | ce / UVLO
- UVLO / Bandg Referen | ap / | ce / UVLO / TERMINAL NAME NO. | II//OO | DDEESSCCRRIIPPTTIIOONN / EN 1 | I | Enable input / FB/PG 5 | I | Feedback input voltage for adjustable device/PG output for fixed options
- SLVS306E - NOVEMBER 2000 - REVISED FEBRUARY 2009 / TPS757xx PG timing diagram / VIN1 / VUVLO / VUVLO / t / VOUT VIT+(see Note A)
- TPS757xx PG timing diagram / VIN1 / VUVLO / VUVLO / t / VOUT VIT+(see Note A) / Threshold
- ESD rating, HBM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 kV / ESD rating, CDM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 500 V / Stresses beyond those listed under absolute maximum ratings may cause permanent damage to the device. These are stress ratings only, and / functional operation of the device at these or any other conditions beyond those indicated under recommended operating conditions is not / implied. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability. / All voltage values are with respect to network terminal ground. / DISSIPATION RATING TABLE
- PACKAGE RJC ( deg C/W) RJA ( deg C/W) / TO-220 2 58.7 / TO-263 2 38.7# / For both packages, the RJA values were computed using JEDEC high K board (2S2P) / with 1 ounce internal copper plane and ground plane. There was no air flow across the / packages. / RJA was computed assuming a vertical, free standing TO-220 package with pins
- For both packages, the RJA values were computed using JEDEC high K board (2S2P) / with 1 ounce internal copper plane and ground plane. There was no air flow across the / packages. / RJA was computed assuming a vertical, free standing TO-220 package with pins / soldered to the board. There is no heatsink attached to the package. / #RJA was computed assuming a horizontally mounted TO-263 package with pins / soldered to the board. There is no copper pad underneath the package.
- packages. / RJA was computed assuming a vertical, free standing TO-220 package with pins / soldered to the board. There is no heatsink attached to the package. / #RJA was computed assuming a horizontally mounted TO-263 package with pins / soldered to the board. There is no copper pad underneath the package. / recommended operating conditions / MIN MAX UNIT
- Output voltage range, VO 1.22 5 V / Output current, IO 0 3 A / Operating virtual junction temperature, TJ -40 125 deg C / || To calculate the minimum input voltage for your maximum output current, use the following equation: VI(min) = VO(max) + VDO(max load). / POST OFFICE BOX 655303 * DALLAS, TEXAS 75265 5 / PACKAGE | RJC ( deg C/W) | RJA ( deg C/W) / TO-220 | 2 | 58.7
- (see Note 3) VO + 1 V <= VI < 5.5 V 0.1 / Load regulation (see Note 2) 0.35 %/V / Output noise voltage TPS75715 BW = 300 Hz to 50 kHz, TJ = 25 deg C, VI = 2.8 V 35 uVrms / Output current limit VO = 0 V 5.5 10 14 A / Thermal shutdown junction temperature 150 deg C / EN = VI, TJ = 25 deg C 0.1 uA / SSttaannddbbyy ccuurrrreenntt

### Reference designs, applications, and examples

- VDO / IO = 3 A / VO = 3.3 V / Please be aware that an important notice concerning avail ability, standard warranty, and use in critical applications of / Texas Instruments semiconductor products and disclaimers thereto appears at the end of this data sheet. / /C0080/C0082/C0079/C0068/C0085/C0067/C0084/C0073/C0079/C0078 /C0068/C0065/C0084/C0065 /C0105/C0110/C0102/C0111/C0114/C0109/C0097/C0116/C0105/C0111/C0110 /C0105/C0115 /C0099/C0117/C0114/C0114/C0101/C0110/C0116 /C0097/C0115 /C0111/C0102 /C0112/C0117/C0098/C0108/C0105/C0099/C0097/C0116/C0105/C0111/C0110 /C0100/C0097/C0116/C0101/C0046 / /C0080/C0114/C0111/C0100/C0117/C0099/C0116/C0115 /C0099/C0111/C0110/C0102/C0111/C0114/C0109 /C0116/C0111 /C0115/C0112/C0101/C0099/C0105/C0102/C0105/C0099/C0097/C0116/C0105/C0111/C0110/C0115 /C0112/C0101/C0114 /C0116/C0104/C0101 /C0116/C0101/C0114/C0109/C0115 /C0111/C0102 /C0084/C0101/C0120/C0097/C0115 /C0073/C0110/C0115/C0116/C0114/C0117/C0109/C0101/C0110/C0116/C0115
- 4400 deg CC ttoo 112255 deg CC 1.8 V TPS75718KC TPS75718KTT / 1.5 V TPS75715KC TPS75715KTT / Adjustable 1.22 V to 5 V TPS75701KC TPS75701KTT / NOTE: The TPS75701 is programmable using an external resistor divider (see application / information). The KTT package is available taped and reeled. Add an R suffix to the / device type (e.g., TPS75701KTTR) to indicate tape and reel. / 2 5
- 47 uF / GND / 3 / See application information section for capacitor selection details. / Figure 1. Typical Application Configuration (For Fixed Output Options) / 2 POST OFFICE BOX 655303 * DALLAS, TEXAS 75265 / TJ | OUTPUT VOLTAGE (TYP) | TO-220 (KC) | TO-263(KTT)
- GND / 3 / See application information section for capacitor selection details. / Figure 1. Typical Application Configuration (For Fixed Output Options) / 2 POST OFFICE BOX 655303 * DALLAS, TEXAS 75265 / TJ | OUTPUT VOLTAGE (TYP) | TO-220 (KC) | TO-263(KTT) / 4400 deg CC ttoo 112255 deg CC | 3.3 V | TPS75733KC | TPS75733KTT
- T (cid:1) T (cid:7)P maxx R (cid:7) R (cid:7) R (2) / J A D JC CS SA / The RJC is specific to each regulator as determined by its package, lead frame, and die size provided in the / regulators datasheet. The RSA is a function of the type and size of heatsink. For example, black body radiator / type heatsinks, like the one attached to the TO-220 package in Figure 21(a), can have RCS values ranging / from 5 deg C/W for very large heatsinks to 50 deg C/W for very small heatsinks. The RCS is a function of how the / package is attached to the heatsink. For example, if a thermal compound is used to attach a heatsink to a
- regulators datasheet. The RSA is a function of the type and size of heatsink. For example, black body radiator / type heatsinks, like the one attached to the TO-220 package in Figure 21(a), can have RCS values ranging / from 5 deg C/W for very large heatsinks to 50 deg C/W for very small heatsinks. The RCS is a function of how the / package is attached to the heatsink. For example, if a thermal compound is used to attach a heatsink to a / TO-220 package, RCS of 1 deg C/W is reasonable. / Even if no external black body radiator type heatsink is attached to the package, the board on which the regulator / is mounted will provide some heatsinking through the pin solder connections. Some packages, like the TO-263
- SLVS306E - NOVEMBER 2000 - REVISED FEBRUARY 2009 / THERMAL INFORMATION / TO-220 power dissipation / The TO-220 package provides an effective means of managing power dissipation in through-hole applications. / The TO-220 package dimensions are provided in the Mechanical Data section at the end of the data sheet. A / heatsink can be used with the TO-220 package to effectively lower the junction-to-ambient thermal resistance. / To illustrate, the TPS75725 in a TO-220 package was chosen. For this example, the average input voltage is
- The TO-220 package provides an effective means of managing power dissipation in through-hole applications. / The TO-220 package dimensions are provided in the Mechanical Data section at the end of the data sheet. A / heatsink can be used with the TO-220 package to effectively lower the junction-to-ambient thermal resistance. / To illustrate, the TPS75725 in a TO-220 package was chosen. For this example, the average input voltage is / 3.3 V, the output voltage is 2.5 V, the average output current is 3 A, the ambient temperature 55 deg C, the air flow / is 150 LFM, and the operating environment is the same as documented below. Neglecting the quiescent current, / the maximum average power is:
- THERMAL INFORMATION / TO-263 power dissipation / The TO-263 package provides an effective means of managing power dissipation in surface mount / applications. The TO-263 package dimensions are provided in the Mechanical Data section at the end of the / data sheet. The addition of a copper plane directly underneath the TO-263 package enhances the thermal / performance of the package. / To illustrate, the TPS75725 in a TO-263 package was chosen. For this example, the average input voltage is
- applications. The TO-263 package dimensions are provided in the Mechanical Data section at the end of the / data sheet. The addition of a copper plane directly underneath the TO-263 package enhances the thermal / performance of the package. / To illustrate, the TPS75725 in a TO-263 package was chosen. For this example, the average input voltage is / 3.3 V, the output voltage is 2.5 V, the average output current is 3 A, the ambient temperature 55 deg C, the air flow / is 150 LFM, and the operating environment is the same as documented below. Neglecting the quiescent current, / the maximum average power is:
- (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:21)(cid:6) (cid:22)(cid:19)(cid:3)(cid:1)(cid:23)(cid:1)(cid:16)(cid:19)(cid:20)(cid:3)(cid:12)(cid:15)(cid:20)(cid:1) (cid:16)(cid:15)(cid:3)(cid:2)(cid:14)(cid:20)(cid:3)(cid:15) (cid:10)(cid:23)(cid:19) (cid:24)(cid:14)(cid:11)(cid:23)(cid:18)(cid:16)(cid:14)(cid:2)(cid:14)(cid:25)(cid:1) / (cid:26)(cid:14)(cid:24)(cid:1)(cid:19)(cid:17)(cid:15) (cid:16)(cid:15)(cid:17)(cid:25)(cid:24)(cid:19)(cid:1)(cid:14)(cid:16)(cid:3) / SLVS306E - NOVEMBER 2000 - REVISED FEBRUARY 2009 / APPLICATION INFORMATION / programming the TPS75701 adjustable LDO regulator / The output voltage of the TPS75701 adjustable regulator is programmed using an external resistor divider as / shown in Figure 28. The output voltage is calculated using:
- (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:21)(cid:6) (cid:22)(cid:19)(cid:3)(cid:1)(cid:23)(cid:1)(cid:16)(cid:19)(cid:20)(cid:3)(cid:12)(cid:15)(cid:20)(cid:1) (cid:16)(cid:15)(cid:3)(cid:2)(cid:14)(cid:20)(cid:3)(cid:15) (cid:10)(cid:23)(cid:19) (cid:24)(cid:14)(cid:11)(cid:23)(cid:18)(cid:16)(cid:14)(cid:2)(cid:14)(cid:25)(cid:1) / (cid:26)(cid:14)(cid:24)(cid:1)(cid:19)(cid:17)(cid:15) (cid:16)(cid:15)(cid:17)(cid:25)(cid:24)(cid:19)(cid:1)(cid:14)(cid:16)(cid:3) / SLVS306E - NOVEMBER 2000 - REVISED FEBRUARY 2009 / APPLICATION INFORMATION / input capacitor / For a typical application, a ceramic input bypass capacitor (0.22 uF - 1 uF) is recommended to ensure device / stability. This capacitor should be as close as possible to the input pin. Due to the impedance of the input supply,
- SLVS306E - NOVEMBER 2000 - REVISED FEBRUARY 2009 / APPLICATION INFORMATION / input capacitor / For a typical application, a ceramic input bypass capacitor (0.22 uF - 1 uF) is recommended to ensure device / stability. This capacitor should be as close as possible to the input pin. Due to the impedance of the input supply, / large transient currents will cause the input voltage to droop. If this droop causes the input voltage to drop below / the UVLO threshold, the device will turn off. Therefore, it is recommended that a larger capacitor be placed in
- requirements described in this section. Larger capacitors provide a wider range of stability and better load / transient response. / This information along with the ESR graphs, Figures 19, 20, and 29, is included to assist in selection of suitable / capacitance for the users application. When necessary to achieve low height requirements along with high / output current and/or high load capacitance, several higher ESR capacitors can be used in parallel to meet / these guidelines. / OUTPUT CAPACITANCE
- (2) Material type: When designated, preproduction parts are prototypes/experimental devices, and are not yet approved or released for full production. Testing and final process, including without limitation quality assurance, / reliability performance testing, and/or process qualification, may not yet be complete, and this item is subject to further changes or possible discontinuation. If available for ordering, purchases will be subject to an additional / waiver at checkout, and are intended for early internal evaluation purposes only. These items are sold without warranties of any kind. / (3) RoHS values: Yes, No, RoHS Exempt. See the TI RoHS Statement for additional information and value definition.
- | | 0.25 | C | A / 1 5 | | | / www.ti.com / EXAMPLE BOARD LAYOUT / 0.07 MAX / ALL AROUND0.07 MAX / ALL AROUND (1.45)
- 1 5 / IMPORTANT NOTICE AND DISCLAIMER / TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATASHEETS), DESIGN RESOURCES (INCLUDING REFERENCE / DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES AS IS / AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY / IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD / PARTY INTELLECTUAL PROPERTY RIGHTS.
- IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD / PARTY INTELLECTUAL PROPERTY RIGHTS. / These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate / TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable / standards, and any other safety, security, regulatory or other requirements. / These resources are subject to change without notice. TI grants you permission to use these resources only for development of an / application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license

## Page-by-page extracted content

### Page 1

#### Extracted tables

Table 1:

```text
1 2 3 4 5 |
```

Table 2:

```text
IO V |  |  |  |  |  |  |  |  |  |  | 
 | IO V | = 3 O = 3 | A .3 V |  |  |  |  |  |  |  |
```

Table 3:

```text
VO |  |  |  |  |  |  |  |  |  |  |  |  | 
 | VO | = 1. | 5 V |  |  |  |  |  |  |  |  |  | 
Co | Co | = 10 | 0 uF |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  | di(cid:1) | 0.75 | A | 
 |  |  |  |  |  |  |  |  |  |  | (cid:1)s |  | 
 |  |  |  |  |  |  |  |  |  | dt |  |  |
```

#### Raw extracted text

```text
/C0084/C0080/C0083/C0055/C0053/C0055/C0049/C0053/C0044 /C0084/C0080/C0083/C0055/C0053/C0055/C0049/C0056/C0044 /C0084/C0080/C0083/C0055/C0053/C0055/C0050/C0053/C0044 /C0084/C0080/C0083/C0055/C0053/C0055/C0051/C0051 /C0087/C0073/C0084/C0072 /C0080/C0079/C0087/C0069/C0082 /C0071/C0079/C0079/C0068 /C0065/C0078/C0068
/C0084/C0080/C0083/C0055/C0053/C0055/C0048/C0049 /C0070/C0065/C0083/C0084/C0262/C0084/C0082/C0065/C0078/C0083/C0073/C0069/C0078/C0084 /C0082/C0069/C0083/C0080/C0079/C0078/C0083/C0069 /C0051/C0262/C0065 /C0076/C0079/C0087/C0262/C0068/C0082/C0079/C0080/C0079/C0085/C0084
/C0086/C0079/C0076/C0084/C0065/C0071/C0069 /C0082/C0069/C0071/C0085/C0076/C0065/C0084/C0079/C0082/C0083
SLVS306E - NOVEMBER 2000 - REVISED FEBRUARY 2009
1POST OFFICE BOX 655303 * DALLAS, TEXAS 75265
/C00683-A Low-Dropout Voltage Regulator
/C0068Available in 1.5-V, 1.8-V, 2.5-V, and 3.3-V
Fixed-Output and Adjustable Versions
/C0068Open Drain Power-Good (PG) Status
Output (Fixed Options Only)
/C0068Dropout Voltage Typically 150 mV at 3 A
(TPS75733)
/C0068Low 125 uA Typical Quiescent Current
/C0068Fast Transient Response
/C00683% Tolerance Over Specified Conditions for
Fixed-Output Versions
/C0068Available in 5-Pin TO-220 and TO-263
Surface-Mount Packages
/C0068Thermal Shutdown Protection

description
The TPS757xx family of 3-A low dropout (LDO) regulators contains four fixed voltage option regulators with
integrated power-good (PG
) and an adjustable voltage option regulator. These devices are capable of supplying
3 A of output current with a dropout of 150 mV (TPS75733). Therefore, the device is capable of performing a
3.3-V to 2.5-V conversion. Quiescent current is 125 uA at full load and drops down to less than 1 uA when the
device is disabled. The TPS757xx is designed to have fast transient response for large load current changes.
t - Time - us
TPS75715
LOAD TRANSIENT RESPONSE
I    - Output Current - AO
VO - Change in Output Voltage - mV
-100
0
06 0 4020 80 100 140 120 160 180 200
0
50
-50
VO = 1.5 V
Co = 100 uF
-150 2
di
dt /C00430.75 A
/C0109s 4
100
150
0
50
100
150
200
250
-40 -25 -10 5 20 35 50 65 80 95 110 125
TJ - Junction Temperature -  deg C
- Dropout Voltage - mV
TPS75733
DROPOUT VOLTAGE
vs
JUNCTION TEMPERATURE
VDO
IO = 3 A
VO = 3.3 V
Please be aware that an important notice concerning avail ability, standard warranty, and use in critical applications of
Texas Instruments semiconductor products and disclaimers thereto appears at the end of this data sheet.
/C0080/C0082/C0079/C0068/C0085/C0067/C0084/C0073/C0079/C0078 /C0068/C0065/C0084/C0065 /C0105/C0110/C0102/C0111/C0114/C0109/C0097/C0116/C0105/C0111/C0110 /C0105/C0115 /C0099/C0117/C0114/C0114/C0101/C0110/C0116 /C0097/C0115 /C0111/C0102 /C0112/C0117/C0098/C0108/C0105/C0099/C0097/C0116/C0105/C0111/C0110 /C0100/C0097/C0116/C0101/C0046
/C0080/C0114/C0111/C0100/C0117/C0099/C0116/C0115 /C0099/C0111/C0110/C0102/C0111/C0114/C0109 /C0116/C0111 /C0115/C0112/C0101/C0099/C0105/C0102/C0105/C0099/C0097/C0116/C0105/C0111/C0110/C0115 /C0112/C0101/C0114 /C0116/C0104/C0101 /C0116/C0101/C0114/C0109/C0115 /C0111/C0102 /C0084/C0101/C0120/C0097/C0115 /C0073/C0110/C0115/C0116/C0114/C0117/C0109/C0101/C0110/C0116/C0115
/C0115/C0116/C0097/C0110/C0100/C0097/C0114/C0100 /C0119/C0097/C0114/C0114/C0097/C0110/C0116/C0121/C0046 /C0080/C0114/C0111/C0100/C0117/C0099/C0116/C0105/C0111/C0110 /C0112/C0114/C0111/C0099/C0101/C0115/C0115/C0105/C0110/C0103 /C0100/C0111/C0101/C0115 /C0110/C0111/C0116 /C0110/C0101/C0099/C0101/C0115/C0115/C0097/C0114/C0105/C0108/C0121 /C0105/C0110/C0099/C0108/C0117/C0100/C0101
/C0116/C0101/C0115/C0116/C0105/C0110/C0103 /C0111/C0102 /C0097/C0108/C0108 /C0112/C0097/C0114/C0097/C0109/C0101/C0116/C0101/C0114/C0115/C0046
Copyright   2009, Texas Instruments Incorporated
TO-220 (KC) PACKAGE
(TOP VIEW)
1
2
3
4
5
EN
IN
GND
OUTPUT
FB/PG
1
TO-263 (KTT) PACKAGE
(TOP VIEW)
2
3
4
5
EN
IN
GND
OUTPUT
FB/PG
```

### Page 2

#### Extracted tables

Table 1:

```text
TJ | OUTPUT VOLTAGE (TYP) | TO-220 (KC) | TO-263(KTT)
4400 deg CC ttoo 112255 deg CC | 3.3 V | TPS75733KC | TPS75733KTT
 | 2.5 V | TPS75725KC | TPS75725KTT
 | 1.8 V | TPS75718KC | TPS75718KTT
 | 1.5 V | TPS75715KC | TPS75715KTT
 | Adjustable 1.22 V to 5 V | TPS75701KC | TPS75701KTT
```

Table 2:

```text
| Co + 47 uF
```

#### Raw extracted text

```text
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:8)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:9)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:10)(cid:10) (cid:11)(cid:12)(cid:1)(cid:13) (cid:2)(cid:14)(cid:11)(cid:15)(cid:16) (cid:17)(cid:14)(cid:14)(cid:18) (cid:19)(cid:20)(cid:18)
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:21)(cid:6) (cid:22)(cid:19)(cid:3)(cid:1)(cid:23)(cid:1)(cid:16)(cid:19)(cid:20)(cid:3)(cid:12)(cid:15)(cid:20)(cid:1) (cid:16)(cid:15)(cid:3)(cid:2)(cid:14)(cid:20)(cid:3)(cid:15) (cid:10)(cid:23)(cid:19) (cid:24)(cid:14)(cid:11)(cid:23)(cid:18)(cid:16)(cid:14)(cid:2)(cid:14)(cid:25)(cid:1)
(cid:26)(cid:14)(cid:24)(cid:1)(cid:19)(cid:17)(cid:15) (cid:16)(cid:15)(cid:17)(cid:25)(cid:24)(cid:19)(cid:1)(cid:14)(cid:16)(cid:3)
SLVS306E - NOVEMBER 2000 - REVISED FEBRUARY 2009
description (continued)
Because the PMOS device behaves as a low-value resistor, the dropout voltage is low (typically 150 mV at an
output current of 3 A for the TPS75733) and is directly proportional to the output current. Additionally, since the
PMOS pass element is a voltage-driven device, the quiescent current is low and independent of output loading
(typically 125 uA over the full range of output current). These two key specifications yield a significant
improvement in operating life for battery-powered systems.
The device is enabled when EN is connected to a low-level voltage. This LDO family also features a sleep mode;
applying a TTL high signal to EN (enable) shuts down the regulator, reducing the quiescent current to less than
1 uA at T = 25 deg C. The power-good terminal (PG) is an active low, open drain output, which can be used to
J
implement a power-on reset or a low-battery indicator.
The TPS757xx is offered in 1.5-V, 1.8-V, 2.5-V, and 3.3-V fixed-voltage versions and in an adjustable version
(programmable over the range of 1.22 V to 5 V). Output voltage tolerance is specified as a maximum of 3% over
line, load, and temperature ranges. The TPS757xx family is available in a 5-pin TO-220 (KC) and TO-263 (KTT)
packages.
AVAILABLE OPTIONS
OUTPUT VOLTAGE
TJ
(TYP)
TO-220 (KC) TO-263(KTT)
3.3 V TPS75733KC TPS75733KTT
2.5 V TPS75725KC TPS75725KTT
--4400 deg CC ttoo 112255 deg CC 1.8 V TPS75718KC TPS75718KTT
1.5 V TPS75715KC TPS75715KTT
Adjustable 1.22 V to 5 V TPS75701KC TPS75701KTT
NOTE: The TPS75701 is programmable using an external resistor divider (see application
information). The KTT package is available taped and reeled. Add an R suffix to the
device type (e.g., TPS75701KTTR) to indicate tape and reel.
2 5
VI IN PG PG
4
OUT VO
1 uF 1
EN Co
+
47 uF
GND
3
See application information section for capacitor selection details.
Figure 1. Typical Application Configuration (For Fixed Output Options)
2 POST OFFICE BOX 655303 * DALLAS, TEXAS 75265
```

### Page 3

#### Extracted tables

Table 1:

```text
|  | R1
```

Table 2:

```text
UVLO
```

Table 3:

```text
Bandg Referen | ap
 | ce
```

Table 4:

```text
UVLO
```

Table 5:

```text
TERMINAL NAME NO. | II//OO | DDEESSCCRRIIPPTTIIOONN
EN 1 | I | Enable input
FB/PG 5 | I | Feedback input voltage for adjustable device/PG output for fixed options
GND 3 |  | Regulator ground
IN 2 | I | Input voltage
OUTPUT 4 | O | Regulated output voltage
Thermal Pad |  | Connect to GND or Float
```

#### Raw extracted text

```text
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:8)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:9)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:10)(cid:10) (cid:11)(cid:12)(cid:1)(cid:13) (cid:2)(cid:14)(cid:11)(cid:15)(cid:16) (cid:17)(cid:14)(cid:14)(cid:18) (cid:19)(cid:20)(cid:18)
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:21)(cid:6) (cid:22)(cid:19)(cid:3)(cid:1)(cid:23)(cid:1)(cid:16)(cid:19)(cid:20)(cid:3)(cid:12)(cid:15)(cid:20)(cid:1) (cid:16)(cid:15)(cid:3)(cid:2)(cid:14)(cid:20)(cid:3)(cid:15) (cid:10)(cid:23)(cid:19) (cid:24)(cid:14)(cid:11)(cid:23)(cid:18)(cid:16)(cid:14)(cid:2)(cid:14)(cid:25)(cid:1)
(cid:26)(cid:14)(cid:24)(cid:1)(cid:19)(cid:17)(cid:15) (cid:16)(cid:15)(cid:17)(cid:25)(cid:24)(cid:19)(cid:1)(cid:14)(cid:16)(cid:3)
SLVS306E - NOVEMBER 2000 - REVISED FEBRUARY 2009
functional block diagram-adjustable version
VIN VOUT
UVLO Current
Sense
SHUTDOWN
ILIM
R1
GND _ +
FB
EN
UVLO
R2
Thermal
Shutdown External to
the Device
Vref = 1.22 V
Bandgap
VIN
Reference
functional block diagram-fixed version
VIN VOUT
UVLO Current
Sense
SHUTDOWN
ILIM
R1
_
+
GND
UVLO
EN R2
Thermal
Shutdown
Vref = 1.22 V
VIN Bandgap PG
Reference
Falling
Edge Delay
Terminal Functions (TPS757xx)
TERMINAL
II//OO DDEESSCCRRIIPPTTIIOONN
NAME NO.
EN 1 I Enable input
FB/PG 5 I Feedback input voltage for adjustable device/PG output for fixed options
GND 3 Regulator ground
IN 2 I Input voltage
OUTPUT 4 O Regulated output voltage
Thermal Pad - Connect to GND or Float
POST OFFICE BOX 655303 * DALLAS, TEXAS 75265 3
```

### Page 4

#### Extracted tables

Table 1:

```text
| VIT+(see Note A) |  |  | 
 |  | VIT- (see Note A) |  |
```

#### Raw extracted text

```text
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:8)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:9)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:10)(cid:10) (cid:11)(cid:12)(cid:1)(cid:13) (cid:2)(cid:14)(cid:11)(cid:15)(cid:16) (cid:17)(cid:14)(cid:14)(cid:18) (cid:19)(cid:20)(cid:18)
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:21)(cid:6) (cid:22)(cid:19)(cid:3)(cid:1)(cid:23)(cid:1)(cid:16)(cid:19)(cid:20)(cid:3)(cid:12)(cid:15)(cid:20)(cid:1) (cid:16)(cid:15)(cid:3)(cid:2)(cid:14)(cid:20)(cid:3)(cid:15) (cid:10)(cid:23)(cid:19) (cid:24)(cid:14)(cid:11)(cid:23)(cid:18)(cid:16)(cid:14)(cid:2)(cid:14)(cid:25)(cid:1)
(cid:26)(cid:14)(cid:24)(cid:1)(cid:19)(cid:17)(cid:15) (cid:16)(cid:15)(cid:17)(cid:25)(cid:24)(cid:19)(cid:1)(cid:14)(cid:16)(cid:3)
SLVS306E - NOVEMBER 2000 - REVISED FEBRUARY 2009
TPS757xx PG timing diagram
VIN1
VUVLO
VUVLO
t
VOUT VIT+(see Note A)
Threshold
Voltage
VIT-
(see Note A)
t
PG
Output
t
NOTE: VIT -Trip voltage is typically 9% lower than the output voltage (91%VO). VIT- to VIT+ is the hysteresis voltage.
detailed description
The TPS757xx family includes four fixed-output voltage regulators (1.5 V, 1.8 V, 2.5 V, and 3.3 V), and an
adjustable regulator, the TPS75701 (adjustable from 1.22 V to 5 V). The bandgap voltage is typically 1.22 V.
pin functions
enable (EN)
The EN terminal is an input which enables or shuts down the device. If EN is a logic high, the device will be in
shutdown mode. When EN goes to logic low, the device will be enabled.
power-good (PG)
The PG terminal for the fixed voltage option devices is an open drain, active low output that indicates the status
of V
O
(output of the LDO). When V
O
reaches approximately 91% of the regulated voltage, PG will go to a low
impedance state. It will go to a high-impedance state when V falls below approximately 89% (i.e. over load
O
condition) of the regulated voltage. The open drain output of the PG terminal requires a pullup resistor.
feedback (FB)
FB is an input terminal used for the adjustable-output option and must be connected to the output terminal either
directly, in order to generate the minimum output voltage of 1.22 V, or through an external feedback resistor
divider for other output voltages. The FB connection should be as short as possible. It is essential to route it in
such a way to minimize/avoid noise pickup. Adding RC networks between FB terminal and V to filter noise is
O
not recommended because it may cause the regulator to oscillate.
4 POST OFFICE BOX 655303 * DALLAS, TEXAS 75265
```

### Page 5

#### Extracted tables

Table 1:

```text
PACKAGE | RJC ( deg C/W) | RJA ( deg C/W)
TO-220 | 2 | 58.7
TO-263 | 2 | 38.7#
```

Table 2:

```text
| MIN MAX | UNIT
Input voltage, VI || | 2.8 5.5 | V
Output voltage range, VO | 1.22 5 | V
Output current, IO | 0 3 | A
Operating virtual junction temperature, TJ | 40 125 | deg C
```

#### Raw extracted text

```text
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:8)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:9)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:10)(cid:10) (cid:11)(cid:12)(cid:1)(cid:13) (cid:2)(cid:14)(cid:11)(cid:15)(cid:16) (cid:17)(cid:14)(cid:14)(cid:18) (cid:19)(cid:20)(cid:18)
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:21)(cid:6) (cid:22)(cid:19)(cid:3)(cid:1)(cid:23)(cid:1)(cid:16)(cid:19)(cid:20)(cid:3)(cid:12)(cid:15)(cid:20)(cid:1) (cid:16)(cid:15)(cid:3)(cid:2)(cid:14)(cid:20)(cid:3)(cid:15) (cid:10)(cid:23)(cid:19) (cid:24)(cid:14)(cid:11)(cid:23)(cid:18)(cid:16)(cid:14)(cid:2)(cid:14)(cid:25)(cid:1)
(cid:26)(cid:14)(cid:24)(cid:1)(cid:19)(cid:17)(cid:15) (cid:16)(cid:15)(cid:17)(cid:25)(cid:24)(cid:19)(cid:1)(cid:14)(cid:16)(cid:3)
SLVS306E - NOVEMBER 2000 - REVISED FEBRUARY 2009
detailed description (continued)
input voltage (IN)
The V terminal is an input to the regulator.
IN
output voltage (OUTPUT)
The V terminal is an output to the regulator.
OUTPUT
(cid:1)
absolute maximum ratings over operating junction temperature range (unless otherwise noted)
Input voltage range, V . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . -0.3 V to 6 V
I
Voltage range at EN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . -0.3 V to 6 V
Maximum PG voltage (fixed options only) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6 V
Peak output current . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Internally limited
Continuous total power dissipation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . See Dissipation Rating Tables
Output voltage, V (OUTPUT, FB) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5.5 V
O
Operating junction temperature range, T . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . -40 deg C to 150 deg C
J
Storage temperature range, T . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . -65 deg C to 150 deg C
stg
ESD rating, HBM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2 kV
ESD rating, CDM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 500 V
Stresses beyond those listed under absolute maximum ratings may cause permanent damage to the device. These are stress ratings only, and
functional operation of the device at these or any other conditions beyond those indicated under recommended operating conditions is not
implied. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability.
All voltage values are with respect to network terminal ground.
DISSIPATION RATING TABLE
PACKAGE RJC ( deg C/W) RJA ( deg C/W)
TO-220 2 58.7
TO-263 2 38.7#
For both packages, the RJA values were computed using JEDEC high K board (2S2P)
with 1 ounce internal copper plane and ground plane. There was no air flow across the
packages.
RJA was computed assuming a vertical, free standing TO-220 package with pins
soldered to the board. There is no heatsink attached to the package.
#RJA was computed assuming a horizontally mounted TO-263 package with pins
soldered to the board. There is no copper pad underneath the package.
recommended operating conditions
MIN MAX UNIT
Input voltage, VI || 2.8 5.5 V
Output voltage range, VO 1.22 5 V
Output current, IO 0 3 A
Operating virtual junction temperature, TJ -40 125  deg C
|| To calculate the minimum input voltage for your maximum output current, use the following equation: VI(min) = VO(max) + VDO(max load).
POST OFFICE BOX 655303 * DALLAS, TEXAS 75265 5
```

### Page 6

#### Extracted tables

Table 1:

```text
PARAMETER |  | TEST CONDITIONS | MIN TYP MAX | UNIT
OOuuttppuutt vvoollttaaggee ((sseeee NNoottee 22)) | AAddjjuussttaabbllee vvoollttaaggee | 1.22 V <= VO <= 5.5 V, TJ = 25 deg C | VO | VV
 |  | 1.22 V <= VO <= 5.5 V | 0.97 VO 1.03 VO | 
 |  | 1.22 V <= VO <= 5.5 V, TJ = 0 to 125 deg C (see Note 1) | 0.98 VO 1.02 VO | 
 | 11..55 VV OOuuttppuutt | TJ = 25 deg C, 2.8 V < VI < 5.5 V | 1.5 | VV
 |  | 2.8 V <= VI <= 5.5 V | 1.455 1.545 | 
 | 11..88 VV OOuuttppuutt | TJ = 25 deg C, 2.8 V < VI < 5.5 V | 1.8 | VV
 |  | 2.8 V <= VI <= 5.5 V | 1.746 1.854 | 
 | 22..55 VV OOuuttppuutt | TJ = 25 deg C, 3.5 V < VI < 5.5 V | 2.5 | VV
 |  | 3.5 V <= VI <= 5.5 V | 2.425 2.575 | 
 | 33..33 VV OOuuttppuutt | TJ = 25 deg C, 4.3 V < VI < 5.5 V | 3.3 | VV
 |  | 4.3 V <= VI <= 5.5 V | 3.201 3.399 | 
QQuuiieesscceenntt ccuurrrreenntt ((GGNNDD ccuurrrreenntt)) (see Notes 2 and 3) |  | TJ = 25 deg C | 125 | uAA
 |  |  | 200 | 
OOuuttppuutt vvoollttaaggee lliinnee rreegguullaattiioonn ((VVOO//VVOO)) (see Note 3) |  | VO + 1 V <= VI <= 5.5 V, TJ = 25 deg C | 0.04 | %%//VV
 |  | VO + 1 V <= VI < 5.5 V | 0.1 | 
Load regulation (see Note 2) |  |  | 0.35 | %/V
Output noise voltage | TPS75715 | BW = 300 Hz to 50 kHz, TJ = 25 deg C, VI = 2.8 V | 35 | uVrms
Output current limit |  | VO = 0 V | 5.5 10 14 | A
Thermal shutdown junction temperature |  |  | 150 | deg C
SSttaannddbbyy ccuurrrreenntt |  | EN = VI, TJ = 25 deg C | 0.1 | uA
 |  | EN = VI | 10 | uA
FB input current | TPS75701 | FB = 1.5 V | 1 1 | uA
Power supply ripple rejection | TPS75715 | f = 100 Hz, TJ = 25 deg C, VI = 2.8 V, IO = 3 A | 62 | dB
Minimum input voltage for valid PG |  | IO(PG) = 300 uA, V(PG) <= 0.8 V | 0 | V
PG trip threshold voltage | Fixed options only | VO decreasing | 89 93 | %VO
PG hysteresis voltage | Fixed options only | Measured at VO | 0.5 | %VO
PG output low voltage | Fixed options only | VI = 2.8 V, IO(PG) = 1 mA | 0.15 0.4 | V
PG leakage current | Fixed options only | V(PG) = 5 V | 1 | uA
```

#### Raw extracted text

```text
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:8)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:9)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:10)(cid:10) (cid:11)(cid:12)(cid:1)(cid:13) (cid:2)(cid:14)(cid:11)(cid:15)(cid:16) (cid:17)(cid:14)(cid:14)(cid:18) (cid:19)(cid:20)(cid:18)
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:21)(cid:6) (cid:22)(cid:19)(cid:3)(cid:1)(cid:23)(cid:1)(cid:16)(cid:19)(cid:20)(cid:3)(cid:12)(cid:15)(cid:20)(cid:1) (cid:16)(cid:15)(cid:3)(cid:2)(cid:14)(cid:20)(cid:3)(cid:15) (cid:10)(cid:23)(cid:19) (cid:24)(cid:14)(cid:11)(cid:23)(cid:18)(cid:16)(cid:14)(cid:2)(cid:14)(cid:25)(cid:1)
(cid:26)(cid:14)(cid:24)(cid:1)(cid:19)(cid:17)(cid:15) (cid:16)(cid:15)(cid:17)(cid:25)(cid:24)(cid:19)(cid:1)(cid:14)(cid:16)(cid:3)
SLVS306E - NOVEMBER 2000 - REVISED FEBRUARY 2009
electrical characteristics over recommended operating junction temperature range (T = -40 deg C to
J
125 deg C), V
I
= V
O(typ)
+ 1 V, I
O
= 1 mA, EN = 0 V, C
o
= 100 uF (unless otherwise noted)
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
1.22 V <= VO <= 5.5 V, TJ = 25 deg C VO
1.22 V <= VO <= 5.5 V 0.97 VO 1.03 VO
AAddjjuussttaabbllee vvoollttaaggee VV
1.22 V <= VO <= 5.5 V, TJ = 0 to 125 deg C
(see Note 1)
0.98 VO 1.02 VO
TJ = 25 deg C, 2.8 V < VI < 5.5 V 1.5
11..55 VV OOuuttppuutt VV
OOuuttppuutt vvoollttaaggee
2.8 V <= VI <= 5.5 V 1.455 1.545
((sseeee NNoottee 22)) TJ = 25 deg C, 2.8 V < VI < 5.5 V 1.8
11..88 VV OOuuttppuutt VV
2.8 V <= VI <= 5.5 V 1.746 1.854
TJ = 25 deg C, 3.5 V < VI < 5.5 V 2.5
22..55 VV OOuuttppuutt VV
3.5 V <= VI <= 5.5 V 2.425 2.575
TJ = 25 deg C, 4.3 V < VI < 5.5 V 3.3
33..33 VV OOuuttppuutt VV
4.3 V <= VI <= 5.5 V 3.201 3.399
QQuuiieesscceenntt ccuurrrreenntt ((GGNNDD ccuurrrreenntt)) TJ = 25 deg C 125
uAA
(see Notes 2 and 3) 200
OOuuttppuutt vvoollttaaggee lliinnee rreegguullaattiioonn ((VVOO//VVOO)) VO + 1 V <= VI <= 5.5 V, TJ = 25 deg C 0.04
%%//VV
(see Note 3) VO + 1 V <= VI < 5.5 V 0.1
Load regulation (see Note 2) 0.35 %/V
Output noise voltage TPS75715 BW = 300 Hz to 50 kHz, TJ = 25 deg C, VI = 2.8 V 35 uVrms
Output current limit VO = 0 V 5.5 10 14 A
Thermal shutdown junction temperature 150  deg C
EN = VI, TJ = 25 deg C 0.1 uA
SSttaannddbbyy ccuurrrreenntt
EN = VI 10 uA
FB input current TPS75701 FB = 1.5 V -1 1 uA
Power supply ripple f = 100 Hz, TJ = 25 deg C,
TPS75715 62 dB
rejection VI = 2.8 V, IO = 3 A
Minimum input voltage for valid PG IO(PG) = 300 uA, V(PG) <= 0.8 V 0 V
PG trip threshold voltage Fixed options only VO decreasing 89 93 %VO
PG hysteresis voltage Fixed options only Measured at VO 0.5 %VO
PG output low voltage Fixed options only VI = 2.8 V, IO(PG) = 1 mA 0.15 0.4 V
PG leakage current Fixed options only V(PG) = 5 V 1 uA
NOTES: 1. The adjustable option operates with a 2% tolerance over TJ = 0 to 125  deg C.
2. IO = 1 mA to 3 A
3. If VO <= 2.5 V then VImin = 2.8 V, VImax = 5.5 V:
(cid:2) (cid:4)
V V (cid:6)2.8V
Lineregulation(mV) (cid:1) (cid:2) %(cid:3)V (cid:4) (cid:5) O Imax (cid:5)1000
100
If VO > 2.5 V then VImin = VO + 1 V, VImax = 5.5 V:
(cid:2) (cid:2) (cid:4)(cid:4)
V V (cid:6) V (cid:7)1V
O Imax O
Lineregulation(mV) (cid:1) (cid:2) %(cid:3)V (cid:4) (cid:5) (cid:5)1000
100
6 POST OFFICE BOX 655303 * DALLAS, TEXAS 75265
```

### Page 7

#### Extracted tables

Table 1:

```text
PARAMETER |  | TEST CONDITIONS | MIN TYP MAX | UNIT
IInnppuutt ccuurrrreenntt ((EENN)) |  | EN = VI | 1 1 | uA
 |  | EN = 0 V | 1 0 1 | uA
High level EN input voltage |  |  | 2 | V
Low level EN input voltage |  |  | 0.7 | V
VVOO | DDrrooppoouutt vvoollttaaggee,, ((33..33 VV oouuttppuutt)) ((sseeee NNoottee 44)) | IO = 3 A, VI = 3.2 V, TJ = 25 deg C | 150 | mmVV
 |  | IO = 3 A, VI = 3.2 V | 300 | 
 | Discharge transistor current | VO = 1.5 V, TJ = 25 deg C | 10 25 | mA
VVII | UVLO | TJ = 25 deg C, VI rising | 2.2 2.75 | V
 | UVLO hysteresis | TJ = 25 deg C, VI falling | 100 | mV
```

Table 2:

```text
|  | FIGURE
VVOO OOuuttppuutt vvoollttaaggee | vs Output current | 2, 3
 | vs Junction temperature | 4, 5
Ground current | vs Junction temperature | 6
Power supply ripple rejection | vs Frequency | 7
Output spectral noise density | vs Frequency | 8
zo Output impedance | vs Frequency | 9
VVDDOO DDrrooppoouutt vvoollttaaggee | vs Input voltage | 10
 | vs Junction temperature | 11
VI Minimum required input voltage | vs Output voltage | 12
Line transient response |  | 13, 15
Load transient response |  | 14, 16
VO Output voltage and enable voltage | vs Time (start-up) | 17
Equivalent series resistance | vs Output current | 19, 20
```

#### Raw extracted text

```text
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:8)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:9)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:10)(cid:10) (cid:11)(cid:12)(cid:1)(cid:13) (cid:2)(cid:14)(cid:11)(cid:15)(cid:16) (cid:17)(cid:14)(cid:14)(cid:18) (cid:19)(cid:20)(cid:18)
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:21)(cid:6) (cid:22)(cid:19)(cid:3)(cid:1)(cid:23)(cid:1)(cid:16)(cid:19)(cid:20)(cid:3)(cid:12)(cid:15)(cid:20)(cid:1) (cid:16)(cid:15)(cid:3)(cid:2)(cid:14)(cid:20)(cid:3)(cid:15) (cid:10)(cid:23)(cid:19) (cid:24)(cid:14)(cid:11)(cid:23)(cid:18)(cid:16)(cid:14)(cid:2)(cid:14)(cid:25)(cid:1)
(cid:26)(cid:14)(cid:24)(cid:1)(cid:19)(cid:17)(cid:15) (cid:16)(cid:15)(cid:17)(cid:25)(cid:24)(cid:19)(cid:1)(cid:14)(cid:16)(cid:3)
SLVS306E - NOVEMBER 2000 - REVISED FEBRUARY 2009
electrical characteristics over recommended operating junction temperature range (T = -40 deg C to
J
125 deg C), V
I
= V
O(typ)
+ 1 V, I
O
= 1 mA, EN = 0 V, C
o
= 100 uF (unless otherwise noted) (continued)
PARAMETER TEST CONDITIONS MIN TYP MAX UNIT
EN = VI -1 1 uA
IInnppuutt ccuurrrreenntt ((EENN))
EN = 0 V -1 0 1 uA
High level EN input voltage 2 V
Low level EN input voltage 0.7 V
IO = 3 A, VI = 3.2 V, TJ = 25 deg C 150
DDrrooppoouutt vvoollttaaggee,, ((33..33 VV oouuttppuutt)) ((sseeee NNoottee 44)) mmVV
VVOO IO = 3 A, VI = 3.2 V 300
Discharge transistor current VO = 1.5 V, TJ = 25 deg C 10 25 mA
UVLO TJ = 25 deg C, VI rising 2.2 2.75 V
VVII
UVLO hysteresis TJ = 25 deg C, VI falling 100 mV
NOTE 4: IN voltage equals VO(typ) - 100 mV; TPS75715, TPS75718, and TPS75725 dropout voltage limited by input voltage range limitations
(i.e., TPS75733 input voltage is set to 3.2 V for the purpose of this test).
TYPICAL CHARACTERISTICS
Table of Graphs
FIGURE
vs Output current 2, 3
VVOO OOuuttppuutt vvoollttaaggee
vs Junction temperature 4, 5
Ground current vs Junction temperature 6
Power supply ripple rejection vs Frequency 7
Output spectral noise density vs Frequency 8
zo Output impedance vs Frequency 9
vs Input voltage 10
VVDDOO DDrrooppoouutt vvoollttaaggee
vs Junction temperature 11
VI Minimum required input voltage vs Output voltage 12
Line transient response 13, 15
Load transient response 14, 16
VO Output voltage and enable voltage vs Time (start-up) 17
Equivalent series resistance vs Output current 19, 20
POST OFFICE BOX 655303 * DALLAS, TEXAS 75265 7
```

### Page 8

#### Extracted tables

Table 1:

```text
VI = 4.3 V TJ = 25 deg C |  |
```

Table 2:

```text
VI = 2.8 V TJ = 25 deg C |  |
```

Table 3:

```text
VI = | 4.3 | V |  |  |  |  |  |  |  |
```

Table 4:

```text
VI |  |  |  |  |  |  |  |  |  |  | 
 | VI | = 2.8 | V |  |  |  |  |  |  |  |
```

#### Raw extracted text

```text
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:8)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:9)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:10)(cid:10) (cid:11)(cid:12)(cid:1)(cid:13) (cid:2)(cid:14)(cid:11)(cid:15)(cid:16) (cid:17)(cid:14)(cid:14)(cid:18) (cid:19)(cid:20)(cid:18)
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:21)(cid:6) (cid:22)(cid:19)(cid:3)(cid:1)(cid:23)(cid:1)(cid:16)(cid:19)(cid:20)(cid:3)(cid:12)(cid:15)(cid:20)(cid:1) (cid:16)(cid:15)(cid:3)(cid:2)(cid:14)(cid:20)(cid:3)(cid:15) (cid:10)(cid:23)(cid:19) (cid:24)(cid:14)(cid:11)(cid:23)(cid:18)(cid:16)(cid:14)(cid:2)(cid:14)(cid:25)(cid:1)
(cid:26)(cid:14)(cid:24)(cid:1)(cid:19)(cid:17)(cid:15) (cid:16)(cid:15)(cid:17)(cid:25)(cid:24)(cid:19)(cid:1)(cid:14)(cid:16)(cid:3)
SLVS306E - NOVEMBER 2000 - REVISED FEBRUARY 2009
TYPICAL CHARACTERISTICS
TPS75733
OUTPUT VOLTAGE
vs
OUTPUT CURRENT
3.345
3.330
3.315
3.285
3.270
3.255
0 1 2 3
IO - Output Current - A
Figure 2
8 POST OFFICE BOX 655303 * DALLAS, TEXAS 75265
V
-
egatloV
tuptuO
-OV
TPS75715
OUTPUT VOLTAGE
vs
OUTPUT CURRENT
1.545
VI = 4.3 V
TJ = 25 deg C
1.530
1.515
3.3 1.5
1.485
1.470
0
IO - Output Current - A
Figure 3
V
-
egatloV
tuptuO
-OV
VI = 2.8 V
TJ = 25 deg C
1.455
1 2 3
TPS75733
OUTPUT VOLTAGE
vs
JUNCTION TEMPERATURE
TJ - Junction Temperature -  deg C
V
-
egatloV
tuptuO
-OV
TPS75715
OUTPUT VOLTAGE
vs
JUNCTION TEMPERATURE
3.345
VI = 4.3 V
3.33
3.315
3.3
3.285
3.270
3.255
-40 -25 10 5 20 35 50 65 80 95 110125
TJ - Junction Temperature -  deg C
Figure 4 Figure 5
V
-
egatloV
tuptuO
-OV
1.545
VI = 2.8 V
1.530
1.515
1.5
1.485
1.470
1.455
-40-25 -10 5 20 35 50 65 80 95 110 125
```

### Page 9

#### Extracted tables

Table 1:

```text
V I |  |  |  |  |  |  |  |  |  | 
 | V I | I = 5 O = 3 | V A |  |  |  |  |  |  |
```

Table 2:

```text
|  | VI = 4 C = | . 1 | 3 V 00 | uF |  |  |  |  |  |  |  |  |  |  | 
 | T | o J = | 2 | 5 deg C |  |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  | I |  |  |  |  |  | 
 |  |  |  |  |  |  |  |  |  |  | O = | 1 | mA |  |  | 
 |  |  |  |  |  |  | I | O = | 3 A |  |  |  |  |  |  |
```

Table 3:

```text
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | V V | I = 4.3 O = 3.3 | V V u | 
 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | C T | o = 100 J = 25 deg | F C | 
 |  |  |  |  |  |  |  |  |  |  | IO | = | 3 |  | A |  |  |  | 
 |  |  | I | O = | 1 m | A |  |  |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  | 100 |  |  |  |  |  | 1k |  |  |  |  |  | 10k |  | 00k
```

Table 4:

```text
| VI | = 4.3 | V |  |  |  |  |  |  |  |  |  |  |  |  | 
 | Co IO | = 10 = 1 m | 0 | uF A |  |  |  |  |  |  |  |  |  |  |  | 
 | TJ | = 25 | deg C |  |  |  |  | I |  | = 1 | mA |  |  |  |  | 
 |  |  |  |  |  |  |  | O |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  |  | I |  | = 3 | A |  |  |  |  | 
 |  |  |  |  |  |  |  | O |  |  |  |  |  |  |  |
```

#### Raw extracted text

```text
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:8)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:9)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:10)(cid:10) (cid:11)(cid:12)(cid:1)(cid:13) (cid:2)(cid:14)(cid:11)(cid:15)(cid:16) (cid:17)(cid:14)(cid:14)(cid:18) (cid:19)(cid:20)(cid:18)
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:21)(cid:6) (cid:22)(cid:19)(cid:3)(cid:1)(cid:23)(cid:1)(cid:16)(cid:19)(cid:20)(cid:3)(cid:12)(cid:15)(cid:20)(cid:1) (cid:16)(cid:15)(cid:3)(cid:2)(cid:14)(cid:20)(cid:3)(cid:15) (cid:10)(cid:23)(cid:19) (cid:24)(cid:14)(cid:11)(cid:23)(cid:18)(cid:16)(cid:14)(cid:2)(cid:14)(cid:25)(cid:1)
(cid:26)(cid:14)(cid:24)(cid:1)(cid:19)(cid:17)(cid:15) (cid:16)(cid:15)(cid:17)(cid:25)(cid:24)(cid:19)(cid:1)(cid:14)(cid:16)(cid:3)
SLVS306E - NOVEMBER 2000 - REVISED FEBRUARY 2009
TYPICAL CHARACTERISTICS
TPS757xx
GROUND CURRENT
vs
JUNCTION TEMPERATURE
150
125
100
75
-40 -25 -10 5 20 35 50 65 80 95 110 125
TJ - Junction Temperature -  deg C
Figure 6
POST OFFICE BOX 655303 * DALLAS, TEXAS 75265 9
Au
-
tnerruC
dnuorG
VI = 5 V
IO = 3 A
10k 100k
Figure 7
Bd
-
noitcejeR
elppiR
ylppuS
rewoP
-
RRSP
TPS75733
POWER SUPPLY RIPPLE REJECTION
vs
FREQUENCY
90
VI = 4.3 V
80 Co = 100 uF
TJ = 25 deg C
70
IO = 1 mA
60
50
40
30
20
IO = 3 A
10
0
10 100 1k 1M 10M
f - Frequency - Hz
TPS75733
OUTPUT SPECTRAL NOISE DENSITY
vs
FREQUENCY
2.5
VI = 4.3 V
VO = 3.3 V
2
Co = 100 uF
TJ = 25 deg C
1.5
IO = 3 A
IO = 1 mA
1
0.5
0
1100 100 1k 10k 100k
f - Frequency - Hz
Figure 8
zH
/Vu
-
ytisneD
esioN
lartcepS
tuptuO
TPS75733
OUTPUT IMPEDANCE
vs
FREQUENCY
f - Frequency - Hz
Figure 9
Ohm-
ecnadepmI
tuptuO
-oz
100
VI = 4.3 V
Co = 100 uF
10
IO = 1 mA
TJ = 25 deg C IO = 1 mA
1
0.1
0.01
IO = 3 A
0.001
0.0001
0.00001
10 100 1k 10k 100k 1M 10M
```

### Page 10

#### Extracted tables

Table 1:

```text
IO = 3 A |  |  |  |  |  | 
 |  |  | TJ | = 125 deg C |  | 
 | TJ = |  |  | 25 deg C |  | 
 |  | TJ = |  | 25 deg C |  | 
 | TJ = |  |  | 40 deg C |  |
```

Table 2:

```text
IO VO | = 3 = 3. | A 3 V |  |  |  |  |  |  |  |
```

Table 3:

```text
I = | 3 A |  |  |  |  |  |  |  |  |  |  | 
O |  |  |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  | deg |  |  |  |  | 
 |  |  |  |  |  | TJ | = 125 |  |  | C |  | 
 |  |  |  |  | TJ = 2 |  | 5 deg | C |  |  |  | 
 |  |  | TJ = |  | 40 deg C |  |  |  |  |  |  |
```

Table 4:

```text
VO IO | = 1.5 = 3 A | V |  |  |  |  |  |  |  |  | 
Co | = 10 | 0 uF |  |  |  |  |  |  |  |  |
```

#### Raw extracted text

```text
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:8)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:9)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:10)(cid:10) (cid:11)(cid:12)(cid:1)(cid:13) (cid:2)(cid:14)(cid:11)(cid:15)(cid:16) (cid:17)(cid:14)(cid:14)(cid:18) (cid:19)(cid:20)(cid:18)
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:21)(cid:6) (cid:22)(cid:19)(cid:3)(cid:1)(cid:23)(cid:1)(cid:16)(cid:19)(cid:20)(cid:3)(cid:12)(cid:15)(cid:20)(cid:1) (cid:16)(cid:15)(cid:3)(cid:2)(cid:14)(cid:20)(cid:3)(cid:15) (cid:10)(cid:23)(cid:19) (cid:24)(cid:14)(cid:11)(cid:23)(cid:18)(cid:16)(cid:14)(cid:2)(cid:14)(cid:25)(cid:1)
(cid:26)(cid:14)(cid:24)(cid:1)(cid:19)(cid:17)(cid:15) (cid:16)(cid:15)(cid:17)(cid:25)(cid:24)(cid:19)(cid:1)(cid:14)(cid:16)(cid:3)
SLVS306E - NOVEMBER 2000 - REVISED FEBRUARY 2009
TYPICAL CHARACTERISTICS
TPS75701
DROPOUT VOLTAGE
vs
INPUT VOLTAGE
250
200
150
100
50
0
2.5 3 3.5 4 4.5 5
VI - Input Voltage - V
Figure 10
10 POST OFFICE BOX 655303 * DALLAS, TEXAS 75265
Vm
-
egatloV
tuoporD
-ODV
250
IO = 3 A
TJ = 125 deg C
200
TJ = 25 deg C
150
TJ = -40 deg C
100
50
0
-40 -25 -10 5 20 35 50 65 80 95 110 125
TJ - Junction Temperature -  deg C
Figure 11
Vm
-
egatloV
tuoporD
-
TPS75733
DROPOUT VOLTAGE
vs
JUNCTION TEMPERATURE
ODV
IO = 3 A
VO = 3.3 V
4
3
2
1.5 2 2.5 3 3.5
Figure 12
V -
egatloV
tupnI
deriuqeR
muminiM
-
MINIMUM REQUIRED INPUT VOLTAGE
vs
OUTPUT VOLTAGE
VO - Output Voltage - V
IV
IO = 3 A
TJ = 125 deg C
TJ = 25 deg C
TJ = -40 deg C
2.8
1.75 2.25 2.75 3.25
ni egnahC
-OV
TPS75715
LINE TRANSIENT RESPONSE
0
-50
3.8
V I
0 50 100 150 200 250 300 350 400 450 500
t - Time - us

V
-
egatloV
tupnI
-
Vm
-
egatloV
tuptuO
VO = 1.5 V
IO = 3 A 50 Co = 100 uF
-100
2.8
Figure 13
```

### Page 11

#### Extracted tables

Table 1:

```text
| VO IO | = 3.3 = 3 A | V |  |  |  |  |  |  | 
 | Co | = 10 | 0 uF |  |  |  |  |  |  |
```

Table 2:

```text
V |  |  |  |  |  |  |  |  |  | 
 | V | I = 4. | 3 V |  |  |  |  |  |  | 
I T | I T | O = 1 J = 2 | 0 mA 5 deg C |  |  |  |  |  |  |
```

#### Raw extracted text

```text
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:8)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:9)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:10)(cid:10) (cid:11)(cid:12)(cid:1)(cid:13) (cid:2)(cid:14)(cid:11)(cid:15)(cid:16) (cid:17)(cid:14)(cid:14)(cid:18) (cid:19)(cid:20)(cid:18)
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:21)(cid:6) (cid:22)(cid:19)(cid:3)(cid:1)(cid:23)(cid:1)(cid:16)(cid:19)(cid:20)(cid:3)(cid:12)(cid:15)(cid:20)(cid:1) (cid:16)(cid:15)(cid:3)(cid:2)(cid:14)(cid:20)(cid:3)(cid:15) (cid:10)(cid:23)(cid:19) (cid:24)(cid:14)(cid:11)(cid:23)(cid:18)(cid:16)(cid:14)(cid:2)(cid:14)(cid:25)(cid:1)
(cid:26)(cid:14)(cid:24)(cid:1)(cid:19)(cid:17)(cid:15) (cid:16)(cid:15)(cid:17)(cid:25)(cid:24)(cid:19)(cid:1)(cid:14)(cid:16)(cid:3)
SLVS306E - NOVEMBER 2000 - REVISED FEBRUARY 2009
TYPICAL CHARACTERISTICS
TPS75715
LOAD TRANSIENT RESPONSE
t - Time - us
POST OFFICE BOX 655303 * DALLAS, TEXAS 75265 11
Vm
-
egatloV
tuptuO
ni egnahC
-OV
A
-
tnerruC
tuptuO
-
O
I
TPS75733
LINE TRANSIENT RESPONSE
150
VO = 1.5 V
100 Co = 100 uF
50
0
-50
di(cid:1)0.75A
-100 dt
(cid:1)s
4
-150 2
0
0 20 40 60 80 100 120 140 160 180 200
t - Time - us
Figure 14 Figure 15
V
-
egatloV
tupnI
-
V I
100
VO = 3.3 V
50
IO = 3 A
Co = 100 uF
0
-50
-100
5.3
4.3
0 50 100 150 200 250 300 350 400 450 500
Vm
-
egatloV
tuptuO
ni
egnahC
-OV
TPS75733
LOAD TRANSIENT RESPONSE
t - Time - us
A
-
tnerruC
tuptuO
-
I
O
VO = 3.3 V
200 Co = 100 uF
100
0
-100 d
d
t
i(cid:1)0.7
(cid:1)
5
s
A
4
2
0
0 20 40 60 80 100 120 140 160 180 200
Vm
-
egatloV
tuptuO
ni
egnahC
-OV
3.3
0
4.3
0
0 0.2 0.4 0.6 0.8 1
t - Time (Start-Up) - ms
Figure 16
V
-
egatloV
tuptuO
-OV
V
-
egatloV
elbanE
TPS75733
OUTPUT VOLTAGE AND ENABLE VOLTAGE
vs
TIME (START-UP)
VI = 4.3 V
IO = 10 mA
TJ = 25 deg C
Figure 17
```

### Page 12

#### Extracted tables

Table 1:

```text
| +
```

Table 2:

```text
u |  |  |  | 
Co = 680 F |  |  |  | 
T = 25 deg C |  |  |  | 
J |  |  |  | 
 |  |  |  | y
 |  |  | Region of Stability | 
 | R |  | egion of Instabilit | y
```

Table 3:

```text
| Co = 47 uF |  |  | 
 | deg |  |  | 
 | TJ = 25 C |  |  | 
 |  | Region of Stability |  | 
 |  | Region of Instabilit | y |
```

#### Raw extracted text

```text
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:8)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:9)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:10)(cid:10) (cid:11)(cid:12)(cid:1)(cid:13) (cid:2)(cid:14)(cid:11)(cid:15)(cid:16) (cid:17)(cid:14)(cid:14)(cid:18) (cid:19)(cid:20)(cid:18)
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:21)(cid:6) (cid:22)(cid:19)(cid:3)(cid:1)(cid:23)(cid:1)(cid:16)(cid:19)(cid:20)(cid:3)(cid:12)(cid:15)(cid:20)(cid:1) (cid:16)(cid:15)(cid:3)(cid:2)(cid:14)(cid:20)(cid:3)(cid:15) (cid:10)(cid:23)(cid:19) (cid:24)(cid:14)(cid:11)(cid:23)(cid:18)(cid:16)(cid:14)(cid:2)(cid:14)(cid:25)(cid:1)
(cid:26)(cid:14)(cid:24)(cid:1)(cid:19)(cid:17)(cid:15) (cid:16)(cid:15)(cid:17)(cid:25)(cid:24)(cid:19)(cid:1)(cid:14)(cid:16)(cid:3)
SLVS306E - NOVEMBER 2000 - REVISED FEBRUARY 2009
TYPICAL CHARACTERISTICS
To Load
VI IN
OUT
+
Co
RL
EN
GND
ESR
Figure 18. Test Circuit for Typical Regions of Stability (Figures 19 and 20) (Fixed Output Options)
TYPICAL REGION OF STABILITY
EQUIVALENT SERIES RESISTANCE
vs
OUTPUT CURRENT
10
0.01
0 3
IO - Output Current - A
Figure 19
12 POST OFFICE BOX 655303 * DALLAS, TEXAS 75265
Ohm-
ecnatsiseR
seireS
tnelaviuqE
-
RSE
TYPICAL REGION OF STABILITY
EQUIVALENT SERIES RESISTANCE
vs
OUTPUT CURRENT
10
Co = 680 uF
TJ = 25 deg C
1 1
Region of Stability
0.2
0.1
0.015
Region of Instability
0.01
1 2 0 3
IO - Output Current - A
Figure 20
Ohm-
ecnatsiseR
seireS
tnelaviuqE
-
RSE
Co = 47 uF
TJ = 25 deg C
Region of Stability
Region of Instability
1 2
Equivalent series resistance (ESR) refers to the total series resistance, including the ESR of the capacitor, any series resistance added externally,
and PWB trace resistance to Co.
```

### Page 13

#### Raw extracted text

```text
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:8)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:9)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:10)(cid:10) (cid:11)(cid:12)(cid:1)(cid:13) (cid:2)(cid:14)(cid:11)(cid:15)(cid:16) (cid:17)(cid:14)(cid:14)(cid:18) (cid:19)(cid:20)(cid:18)
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:21)(cid:6) (cid:22)(cid:19)(cid:3)(cid:1)(cid:23)(cid:1)(cid:16)(cid:19)(cid:20)(cid:3)(cid:12)(cid:15)(cid:20)(cid:1) (cid:16)(cid:15)(cid:3)(cid:2)(cid:14)(cid:20)(cid:3)(cid:15) (cid:10)(cid:23)(cid:19) (cid:24)(cid:14)(cid:11)(cid:23)(cid:18)(cid:16)(cid:14)(cid:2)(cid:14)(cid:25)(cid:1)
(cid:26)(cid:14)(cid:24)(cid:1)(cid:19)(cid:17)(cid:15) (cid:16)(cid:15)(cid:17)(cid:25)(cid:24)(cid:19)(cid:1)(cid:14)(cid:16)(cid:3)
SLVS306E - NOVEMBER 2000 - REVISED FEBRUARY 2009
THERMAL INFORMATION
The amount of heat that an LDO linear regulator generates is directly proportional to the amount of power it
dissipates during operation. All integrated circuits have a maximum allowable junction temperature (T max)
J
above which normal operation is not assured. A system designer must design the operating environment so
that the operating junction temperature (T ) does not exceed the maximum junction temperature (T max). The
J J
two main environmental variables that a designer can use to improve thermal performance are air flow and
external heatsinks. The purpose of this information is to aid the designer in determining the proper operating
environment for a linear regulator that is operating at a specific power level.
In general, the maximum expected power (P ) consumed by a linear regulator is computed as:
D(max)
(cid:2) (cid:4)
P max(cid:1) V (cid:6)V (cid:5)I (cid:7) V xI (1)
D I(avg) O(avg) O(avg) I(avg) (Q)
Where:
V is the average input voltage.
I(avg)
V is the average output voltage.
O(avg)
I is the average output current.
O(avg)
I is the quiescent current.
(Q)
For most TI LDO regulators, the quiescent current is insignificant compared to the average output current;
therefore, the term V x I can be neglected. The operating junction temperature is computed by adding
I(avg) (Q)
the ambient temperature (T ) and the increase in temperature due to the regulators power dissipation. The
A
temperature rise is computed by multiplying the maximum expected power dissipation by the sum of the thermal
resistances between the junction and the case (RJC ), the case to heatsink (RCS ), and the heatsink to ambient
(RSA ). Thermal resistances are measures of how effectively an object dissipates heat. Typically, the larger the
device, the more surface area available for power dissipation and the lower the objects thermal resistance.
Figure 21 illustrates these thermal resistances for (a) a TO-220 package attached to a heatsink, and (b) a
TO-263 package mounted on a JEDEC High-K board.
C
B A TJ
A
RJC
A
B
B TC
RCS
C
RSA
C
TO-263 Package
TA (b)
TO-220 Package
(a)
Figure 21. Thermal Resistances
POST OFFICE BOX 655303 * DALLAS, TEXAS 75265 13
```

### Page 14

#### Raw extracted text

```text
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:8)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:9)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:10)(cid:10) (cid:11)(cid:12)(cid:1)(cid:13) (cid:2)(cid:14)(cid:11)(cid:15)(cid:16) (cid:17)(cid:14)(cid:14)(cid:18) (cid:19)(cid:20)(cid:18)
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:21)(cid:6) (cid:22)(cid:19)(cid:3)(cid:1)(cid:23)(cid:1)(cid:16)(cid:19)(cid:20)(cid:3)(cid:12)(cid:15)(cid:20)(cid:1) (cid:16)(cid:15)(cid:3)(cid:2)(cid:14)(cid:20)(cid:3)(cid:15) (cid:10)(cid:23)(cid:19) (cid:24)(cid:14)(cid:11)(cid:23)(cid:18)(cid:16)(cid:14)(cid:2)(cid:14)(cid:25)(cid:1)
(cid:26)(cid:14)(cid:24)(cid:1)(cid:19)(cid:17)(cid:15) (cid:16)(cid:15)(cid:17)(cid:25)(cid:24)(cid:19)(cid:1)(cid:14)(cid:16)(cid:3)
SLVS306E - NOVEMBER 2000 - REVISED FEBRUARY 2009
THERMAL INFORMATION
Equation 2 summarizes the computation:
(cid:2) (cid:4)
T (cid:1) T (cid:7)P maxx R (cid:7) R (cid:7) R (2)
J A D JC CS SA
The RJC is specific to each regulator as determined by its package, lead frame, and die size provided in the
regulators datasheet. The RSA is a function of the type and size of heatsink. For example, black body radiator
type heatsinks, like the one attached to the TO-220 package in Figure 21(a), can have RCS values ranging
from 5 deg C/W for very large heatsinks to 50 deg C/W for very small heatsinks. The RCS is a function of how the
package is attached to the heatsink. For example, if a thermal compound is used to attach a heatsink to a
TO-220 package, RCS of 1 deg C/W is reasonable.
Even if no external black body radiator type heatsink is attached to the package, the board on which the regulator
is mounted will provide some heatsinking through the pin solder connections. Some packages, like the TO-263
and TIs TSSOP PowerPAD packages, use a copper plane underneath the package or the circuit boards
ground plane for additional heatsinking to improve their thermal performance. Computer aided thermal
modeling can be used to compute very accurate approximations of an integrated circuits thermal performance
in different operating environments (e.g., different types of circuit boards, different types and sizes of heatsinks,
and different air flows, etc.). Using these models, the three thermal resistances can be combined into one
thermal resistance between junction and ambient (RJA ). This RJA is valid only for the specific operating
environment used in the computer model.
Equation 2 simplifies into equation 3:
T
J
(cid:1) T
A
(cid:7)P
D
maxx RJA (3)
Rearranging equation 3 gives equation 4:
T -T
R (cid:1) J A (4)
JA
P max
D
Using equation 3 and the computer model generated curves shown in Figures 22 and 25, a designer can quickly
compute the required heatsink thermal resistance/board area for a given ambient temperature, power
dissipation, and operating environment.
PowerPAD is a trademark of Texas Instruments.
14 POST OFFICE BOX 655303 * DALLAS, TEXAS 75265
```

### Page 15

#### Extracted tables

Table 1:

```text
Natu |  |  | ection |  |  |  |  | 
 | Natu | ral Conv |  |  |  |  |  | 
 |  |  |  |  | M |  |  | 
 |  | Air Flow | = 150 LF |  | M |  |  | 
 |  | A | ir Flow = |  | 250 LF | M |  | LFM
 |  |  |  |  | Air Fl | ow = 500 |  | LFM
 |  | tsink |  |  |  |  |  | 
No Hea |  |  |  |  |  |  |  |
```

#### Raw extracted text

```text
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:8)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:9)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:10)(cid:10) (cid:11)(cid:12)(cid:1)(cid:13) (cid:2)(cid:14)(cid:11)(cid:15)(cid:16) (cid:17)(cid:14)(cid:14)(cid:18) (cid:19)(cid:20)(cid:18)
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:21)(cid:6) (cid:22)(cid:19)(cid:3)(cid:1)(cid:23)(cid:1)(cid:16)(cid:19)(cid:20)(cid:3)(cid:12)(cid:15)(cid:20)(cid:1) (cid:16)(cid:15)(cid:3)(cid:2)(cid:14)(cid:20)(cid:3)(cid:15) (cid:10)(cid:23)(cid:19) (cid:24)(cid:14)(cid:11)(cid:23)(cid:18)(cid:16)(cid:14)(cid:2)(cid:14)(cid:25)(cid:1)
(cid:26)(cid:14)(cid:24)(cid:1)(cid:19)(cid:17)(cid:15) (cid:16)(cid:15)(cid:17)(cid:25)(cid:24)(cid:19)(cid:1)(cid:14)(cid:16)(cid:3)
SLVS306E - NOVEMBER 2000 - REVISED FEBRUARY 2009
THERMAL INFORMATION
TO-220 power dissipation
The TO-220 package provides an effective means of managing power dissipation in through-hole applications.
The TO-220 package dimensions are provided in the Mechanical Data section at the end of the data sheet. A
heatsink can be used with the TO-220 package to effectively lower the junction-to-ambient thermal resistance.
To illustrate, the TPS75725 in a TO-220 package was chosen. For this example, the average input voltage is
3.3 V, the output voltage is 2.5 V, the average output current is 3 A, the ambient temperature 55 deg C, the air flow
is 150 LFM, and the operating environment is the same as documented below. Neglecting the quiescent current,
the maximum average power is:
P max (cid:1) (3.3-2.5)Vx3A (cid:1) 2.4W (5)
D
Substituting T max for T into equation 4 gives equation 6:
J J
RJA max (cid:1) (125-55) deg C(cid:3)2.4W (cid:1) 29 deg C(cid:3)W (6)
From Figure 22, RJA vs Heatsink Thermal Resistance, a heatsink with RSA = 22 deg C/W is required to dissipate
2.4 W. The model operating environment used in the computer model to construct Figure 22 consisted of a
standard JEDEC High-K board (2S2P) with a 1 oz. internal copper plane and ground plane. Since the package
pins were soldered to the board, 450 mm2 of the board was modeled as a heatsink. Figure 23 shows the side
view of the operating environment used in the computer model.
THERMAL RESISTANCE
vs
HEATSINK THERMAL RESISTANCE
65
55
45
35
25
15
5
25 20 15 10 5 0
RSA - Heatsink Thermal Resistance -  deg C/W
POST OFFICE BOX 655303 * DALLAS, TEXAS 75265 15
 deg
W/C
-
ecnatsiseR
lamrehT
-AJR
Natural Convection
Air Flow = 150 LFM
Air Flow = 250 LFM
Air Flow = 500 LFM
No Heatsink
Figure 22
```

### Page 16

#### Extracted tables

Table 1:

```text
| T = 55 deg C |  |  |  |  | 
A | A |  |  |  |  | M
 |  |  |  | Air Flow = 500 LF |  | M
Air Flo |  |  |  |  | FM | 
 |  | Air Flo |  | w = 250 L |  | 
Air Flow = 15 | Air Flow = 15 |  |  | 0 LFM |  | 
No Heatsin |  |  |  | Natural Conv k |  | ection
```

Table 2:

```text
ral Conv | ection
```

#### Raw extracted text

```text
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:8)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:9)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:10)(cid:10) (cid:11)(cid:12)(cid:1)(cid:13) (cid:2)(cid:14)(cid:11)(cid:15)(cid:16) (cid:17)(cid:14)(cid:14)(cid:18) (cid:19)(cid:20)(cid:18)
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:21)(cid:6) (cid:22)(cid:19)(cid:3)(cid:1)(cid:23)(cid:1)(cid:16)(cid:19)(cid:20)(cid:3)(cid:12)(cid:15)(cid:20)(cid:1) (cid:16)(cid:15)(cid:3)(cid:2)(cid:14)(cid:20)(cid:3)(cid:15) (cid:10)(cid:23)(cid:19) (cid:24)(cid:14)(cid:11)(cid:23)(cid:18)(cid:16)(cid:14)(cid:2)(cid:14)(cid:25)(cid:1)
(cid:26)(cid:14)(cid:24)(cid:1)(cid:19)(cid:17)(cid:15) (cid:16)(cid:15)(cid:17)(cid:25)(cid:24)(cid:19)(cid:1)(cid:14)(cid:16)(cid:3)
SLVS306E - NOVEMBER 2000 - REVISED FEBRUARY 2009
THERMAL INFORMATION
TO-220 power dissipation (continued)
0.21 mm 0.21 mm
1 oz. Copper
1 oz. Copper Power Plane
Ground Plane
Figure 23
From the data in Figure 22 and rearranging equation 4, the maximum power dissipation for a different heatsink
RSA and a specific ambient temperature can be computed (see Figure 24).
10
1
20 10 0
Figure 24
16 POST OFFICE BOX 655303 * DALLAS, TEXAS 75265
W
-
timiL
noitapissiD
rewoP
-
DP
POWER DISSIPATION
vs
HEATSINK THERMAL RESISTANCE
TA = 55 deg C
Air Flow = 500 LFM
Air Flow = 250 LFM
Air Flow = 150 LFM
Natural Convection
No Heatsink
RSA - Heatsink Thermal Resistance -  deg C/W
```

### Page 17

#### Extracted tables

Table 1:

```text
|  |  |  |  |  |  |  |  |  | No | Air | F | lo | w |  |  |  | 
 |  |  |  |  |  | 15 | 0 LFM |  |  |  |  |  |  |  |  |  |  | 
 | 25 | 0 |  | LF | M |  |  |  |  |  |  |  |  |  |  |  |  |
```

#### Raw extracted text

```text
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:8)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:9)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:10)(cid:10) (cid:11)(cid:12)(cid:1)(cid:13) (cid:2)(cid:14)(cid:11)(cid:15)(cid:16) (cid:17)(cid:14)(cid:14)(cid:18) (cid:19)(cid:20)(cid:18)
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:21)(cid:6) (cid:22)(cid:19)(cid:3)(cid:1)(cid:23)(cid:1)(cid:16)(cid:19)(cid:20)(cid:3)(cid:12)(cid:15)(cid:20)(cid:1) (cid:16)(cid:15)(cid:3)(cid:2)(cid:14)(cid:20)(cid:3)(cid:15) (cid:10)(cid:23)(cid:19) (cid:24)(cid:14)(cid:11)(cid:23)(cid:18)(cid:16)(cid:14)(cid:2)(cid:14)(cid:25)(cid:1)
(cid:26)(cid:14)(cid:24)(cid:1)(cid:19)(cid:17)(cid:15) (cid:16)(cid:15)(cid:17)(cid:25)(cid:24)(cid:19)(cid:1)(cid:14)(cid:16)(cid:3)
SLVS306E - NOVEMBER 2000 - REVISED FEBRUARY 2009
THERMAL INFORMATION
TO-263 power dissipation
The TO-263 package provides an effective means of managing power dissipation in surface mount
applications. The TO-263 package dimensions are provided in the Mechanical Data section at the end of the
data sheet. The addition of a copper plane directly underneath the TO-263 package enhances the thermal
performance of the package.
To illustrate, the TPS75725 in a TO-263 package was chosen. For this example, the average input voltage is
3.3 V, the output voltage is 2.5 V, the average output current is 3 A, the ambient temperature 55 deg C, the air flow
is 150 LFM, and the operating environment is the same as documented below. Neglecting the quiescent current,
the maximum average power is:
P max (cid:1) (3.3-2.5)Vx3A (cid:1) 2.4W (7)
D
Substituting T max for T into equation 4 gives equation 8:
J J
RJA max (cid:1) (125-55) deg C(cid:3)2.4W (cid:1) 29 deg C(cid:3)W (8)
From Figure 25, RJA vs Copper Heatsink Area, the ground plane needs to be 2 cm2 for the part to dissipate
2.4 W. The model operating environment used in the computer model to construct Figure 25 consisted of a
standard JEDEC High-K board (2S2P) with a 1 oz. internal copper plane and ground plane. The package is
soldered to a 2 oz. copper pad. The pad is tied through thermal vias to the 1 oz. ground plane. Figure 26 shows
the side view of the operating environment used in the computer model.
THERMAL RESISTANCE
vs
COPPER HEATSINK AREA
40
35
30
25
20
15
0 0.01 0.1 1 10 100
Copper Heatsink Area - cm2
Figure 25
POST OFFICE BOX 655303 * DALLAS, TEXAS 75265 17
 deg
W/C
-
ecnatsiseR
lamrehT
-AJR
No Air Flow
150 LFM
250 LFM
```

### Page 18

#### Extracted tables

Table 1:

```text
|  |  |  | deg C |  |  |  |  |  |  |  |  | 
 |  | TA | = 55 |  |  |  |  |  |  |  |  |  | 
 |  |  |  |  |  |  | 250 | LFM | 150 |  |  |  | 
 |  |  |  |  |  |  |  |  |  | L | F |  | M
 |  |  |  |  |  |  |  | No |  |  |  |  | 
 |  |  |  |  |  |  |  |  | Air F | l | o | w |
```

#### Raw extracted text

```text
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:8)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:9)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:10)(cid:10) (cid:11)(cid:12)(cid:1)(cid:13) (cid:2)(cid:14)(cid:11)(cid:15)(cid:16) (cid:17)(cid:14)(cid:14)(cid:18) (cid:19)(cid:20)(cid:18)
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:21)(cid:6) (cid:22)(cid:19)(cid:3)(cid:1)(cid:23)(cid:1)(cid:16)(cid:19)(cid:20)(cid:3)(cid:12)(cid:15)(cid:20)(cid:1) (cid:16)(cid:15)(cid:3)(cid:2)(cid:14)(cid:20)(cid:3)(cid:15) (cid:10)(cid:23)(cid:19) (cid:24)(cid:14)(cid:11)(cid:23)(cid:18)(cid:16)(cid:14)(cid:2)(cid:14)(cid:25)(cid:1)
(cid:26)(cid:14)(cid:24)(cid:1)(cid:19)(cid:17)(cid:15) (cid:16)(cid:15)(cid:17)(cid:25)(cid:24)(cid:19)(cid:1)(cid:14)(cid:16)(cid:3)
SLVS306E - NOVEMBER 2000 - REVISED FEBRUARY 2009
THERMAL INFORMATION
TO-263 power dissipation (continued)
2 oz. Copper Solder Pad
with 25 Thermal Vias
1 oz. Copper
Power Plane
1 oz. Copper
Ground Plane
Thermal Vias, 0.3 mm
Diameter, 1.5 mm Pitch
Figure 26
From the data in Figure 25 and rearranging equation 4, the maximum power dissipation for a different ground
plane area and a specific ambient temperature can be computed (see Figure 27).
MAXIMUM POWER DISSIPATION
vs
COPPER HEATSINK AREA
5
4
3
2
1
0 0.01 0.1 1 10 100
Figure 27
18 POST OFFICE BOX 655303 * DALLAS, TEXAS 75265
W
-
noitapissiD
rewoP
mumixaM
-
DP
TA = 55 deg C
250 LFM
150 LFM
No Air Flow
Copper Heatsink Area - cm2
```

### Page 19

#### Extracted tables

Table 1:

```text
OUTPUT R1 VOLTAGE |  | R2 | UNIT
2.5 V | 31.4 | 30.1 | kOhm
3.3 V | 51 | 30.1 | kOhm
3.6 V | 58.3 | 30.1 | kOhm
```

#### Raw extracted text

```text
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:8)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:9)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:10)(cid:10) (cid:11)(cid:12)(cid:1)(cid:13) (cid:2)(cid:14)(cid:11)(cid:15)(cid:16) (cid:17)(cid:14)(cid:14)(cid:18) (cid:19)(cid:20)(cid:18)
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:21)(cid:6) (cid:22)(cid:19)(cid:3)(cid:1)(cid:23)(cid:1)(cid:16)(cid:19)(cid:20)(cid:3)(cid:12)(cid:15)(cid:20)(cid:1) (cid:16)(cid:15)(cid:3)(cid:2)(cid:14)(cid:20)(cid:3)(cid:15) (cid:10)(cid:23)(cid:19) (cid:24)(cid:14)(cid:11)(cid:23)(cid:18)(cid:16)(cid:14)(cid:2)(cid:14)(cid:25)(cid:1)
(cid:26)(cid:14)(cid:24)(cid:1)(cid:19)(cid:17)(cid:15) (cid:16)(cid:15)(cid:17)(cid:25)(cid:24)(cid:19)(cid:1)(cid:14)(cid:16)(cid:3)
SLVS306E - NOVEMBER 2000 - REVISED FEBRUARY 2009
APPLICATION INFORMATION
programming the TPS75701 adjustable LDO regulator
The output voltage of the TPS75701 adjustable regulator is programmed using an external resistor divider as
shown in Figure 28. The output voltage is calculated using:
(cid:2) (cid:4)
V (cid:1)V (cid:5) 1(cid:7)R1 (9)
O ref R2
Where:
V = 1.224 V typ (the internal reference voltage)
ref
Resistors R1 and R2 should be chosen for approximately 40-uA divider current. Lower value resistors can be
used but offer no inherent advantage and waste more power. Higher values should be avoided as leakage
currents at FB increase the output voltage error. The recommended design procedure is to choose
R2 = 30.1kOhm to set the divider current at 40 uA and then calculate R1 using:
(cid:2) (cid:4)
V
R1(cid:1) O (cid:6)1 (cid:5)R2 (10)
V
ref
TPS75701
OUTPUT VOLTAGE
PROGRAMMING GUIDE
VI IN
1 uF OUTPUT
>=2 V VOLTAGE R1 R2 UNIT
EN OUT VO 2.5 V 31.4 30.1 kOhm
<=0.7 V
R1 Co 3.3 V 51 30.1 kOhm
FB 3.6 V 58.3 30.1 kOhm
GND
R2
Figure 28. TPS75701 Adjustable LDO Regulator Programming
regulator protection
The TPS757xx PMOS-pass transistor has a built-in back diode that conducts reverse currents when the input
voltage drops below the output voltage (e.g., during power down). Current is conducted from the output to the
input and is not internally limited. When extended reverse voltage is anticipated, external limiting may be
appropriate.
The TPS757xx also features internal current limiting and thermal protection. During normal operation, the
TPS757xx limits output current to approximately 10 A. When current limiting engages, the output voltage scales
back linearly until the overcurrent condition ends. While current limiting is designed to prevent gross device
failure, care should be taken not to exceed the power dissipation ratings of the package. If the temperature of
the device exceeds 150 deg C(typ), thermal-protection circuitry shuts it down. Once the device has cooled below
130 deg C(typ), regulator operation resumes.
POST OFFICE BOX 655303 * DALLAS, TEXAS 75265 19
```

### Page 20

#### Extracted tables

Table 1:

```text
|  |  |  | Regi | on | of | St | ab | il | ity | 
ESR min |  | x Co = C | ons | tant |  |  |  |  |  |  | 
 |  |  | tab | ility |  |  |  |  |  |  | 
Y = | Reg ESR | ion of Ins min x Co |  |  |  |  |  |  |  |  |
```

#### Raw extracted text

```text
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:6)(cid:8)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:9)(cid:5)(cid:7) (cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:10)(cid:10) (cid:11)(cid:12)(cid:1)(cid:13) (cid:2)(cid:14)(cid:11)(cid:15)(cid:16) (cid:17)(cid:14)(cid:14)(cid:18) (cid:19)(cid:20)(cid:18)
(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:4)(cid:21)(cid:6) (cid:22)(cid:19)(cid:3)(cid:1)(cid:23)(cid:1)(cid:16)(cid:19)(cid:20)(cid:3)(cid:12)(cid:15)(cid:20)(cid:1) (cid:16)(cid:15)(cid:3)(cid:2)(cid:14)(cid:20)(cid:3)(cid:15) (cid:10)(cid:23)(cid:19) (cid:24)(cid:14)(cid:11)(cid:23)(cid:18)(cid:16)(cid:14)(cid:2)(cid:14)(cid:25)(cid:1)
(cid:26)(cid:14)(cid:24)(cid:1)(cid:19)(cid:17)(cid:15) (cid:16)(cid:15)(cid:17)(cid:25)(cid:24)(cid:19)(cid:1)(cid:14)(cid:16)(cid:3)
SLVS306E - NOVEMBER 2000 - REVISED FEBRUARY 2009
APPLICATION INFORMATION
input capacitor
For a typical application, a ceramic input bypass capacitor (0.22 uF - 1 uF) is recommended to ensure device
stability. This capacitor should be as close as possible to the input pin. Due to the impedance of the input supply,
large transient currents will cause the input voltage to droop. If this droop causes the input voltage to drop below
the UVLO threshold, the device will turn off. Therefore, it is recommended that a larger capacitor be placed in
parallel with the ceramic bypass capacitor at the regulators input. The size of this capacitor depends on the
output current, response time of the main power supply, and the main power supplys distance to the regulator.
At a minimum, the capacitor should be sized to ensure that the input voltage does not drop below the minimum
UVLO threshold voltage during normal operating conditions.
output capacitor
As with most LDO regulators, the TPS757xx requires an output capacitor connected between OUT and GND
to stabilize the internal control loop. The minimum recommended capacitance value is 47 uF with an ESR
(equivalent series resistance) of at least 200 mOhm. As shown in Figure 29, most capacitor and ESR combinations
with a product of 47e-6 x 0.2 = 9.4e-6 or larger will be stable, provided the capacitor value is at least 47 uF.
Solid tantalum electrolytic and aluminum electrolytic capacitors are all suitable, provided they meet the
requirements described in this section. Larger capacitors provide a wider range of stability and better load
transient response.
This information along with the ESR graphs, Figures 19, 20, and 29, is included to assist in selection of suitable
capacitance for the users application. When necessary to achieve low height requirements along with high
output current and/or high load capacitance, several higher ESR capacitors can be used in parallel to meet
these guidelines.
OUTPUT CAPACITANCE
vs
EQUIVALENT SERIES RESISTANCE
1000
100
47
10
0.01 0.1
ESR - Equivalent Series Resistance - Ohm
20 POST OFFICE BOX 655303 * DALLAS, TEXAS 75265
Fu
-
ecnaticapaC
tuptuO
Region of Stability
ESR min x Co = Constant
Region of Instability
Y = ESRmin x Co
0.2
Figure 29
```

### Page 21

#### Extracted tables

Table 1:

```text
Orderable part number | Status (1) | Material type (2) | Package | Pins | Package qty | Carrier | RoHS (3) | Lead finish/ Ball material (4) | MSL rating/ Peak reflow (5) | Op temp ( deg C) | Part marking (6)
TPS75701KC | Active | Production | TO-220 (KC) | 5 | 50 | TUBE | Yes | SN | N/A for Pkg Type | 40 to 125 | 75701
TPS75701KC.A | Active | Production | TO-220 (KC) | 5 | 50 | TUBE | Yes | SN | N/A for Pkg Type | 40 to 125 | 75701
TPS75701KCG3 | Active | Production | TO-220 (KC) | 5 | 50 | TUBE | Yes | SN | N/A for Pkg Type | 40 to 125 | 75701
TPS75701KTTR | Active | Production | DDPAK/ TO-263 (KTT) | 5 | 500 | LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | 40 to 125 | 75701
TPS75701KTTR.A | Active | Production | DDPAK/ TO-263 (KTT) | 5 | 500 | LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | 40 to 125 | 75701
TPS75715KC | Active | Production | TO-220 (KC) | 5 | 50 | TUBE | Yes | SN | N/A for Pkg Type | 40 to 125 | 75715
TPS75715KC.A | Active | Production | TO-220 (KC) | 5 | 50 | TUBE | Yes | SN | N/A for Pkg Type | 40 to 125 | 75715
TPS75715KTTR | Active | Production | DDPAK/ TO-263 (KTT) | 5 | 500 | LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | 40 to 125 | 75715
TPS75715KTTR.A | Active | Production | DDPAK/ TO-263 (KTT) | 5 | 500 | LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | 40 to 125 | 75715
TPS75718KC | Active | Production | TO-220 (KC) | 5 | 50 | TUBE | Yes | SN | N/A for Pkg Type | 40 to 125 | 75718
TPS75718KC.A | Active | Production | TO-220 (KC) | 5 | 50 | TUBE | Yes | SN | N/A for Pkg Type | 40 to 125 | 75718
TPS75718KTTR | Active | Production | DDPAK/ TO-263 (KTT) | 5 | 500 | LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | 40 to 125 | 75718
TPS75718KTTR.A | Active | Production | DDPAK/ TO-263 (KTT) | 5 | 500 | LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | 40 to 125 | 75718
TPS75725KC | Active | Production | TO-220 (KC) | 5 | 50 | TUBE | Yes | SN | N/A for Pkg Type | 40 to 125 | 75725
TPS75725KC.A | Active | Production | TO-220 (KC) | 5 | 50 | TUBE | Yes | SN | N/A for Pkg Type | 40 to 125 | 75725
TPS75725KTTR | Active | Production | DDPAK/ TO-263 (KTT) | 5 | 500 | LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | 40 to 125 | 75725
TPS75725KTTR.A | Active | Production | DDPAK/ TO-263 (KTT) | 5 | 500 | LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | 40 to 125 | 75725
TPS75733KC | Active | Production | TO-220 (KC) | 5 | 50 | TUBE | Yes | SN | N/A for Pkg Type | 40 to 125 | 75733
TPS75733KC.A | Active | Production | TO-220 (KC) | 5 | 50 | TUBE | Yes | SN | N/A for Pkg Type | 40 to 125 | 75733
TPS75733KTTR | Active | Production | DDPAK/ TO-263 (KTT) | 5 | 500 | LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | 40 to 125 | 75733
 | Active |  | DDPAK/ TO-263 (KTT) | 5 |  | Yes |  | Level-2-260C-1 YEAR |  | 75733
```

#### Raw extracted text

```text
PACKAGE OPTION ADDENDUM
www.ti.com 11-Nov-2025
PACKAGING INFORMATION
Orderable part number Status
(1)
Material type
(2)
Package | Pins Package qty | Carrier RoHS
(3)
Lead finish/
Ball material
(4)
MSL rating/
Peak reflow
(5)
Op temp ( deg C) Part marking
(6)
TPS75701KC Active Production TO-220 (KC) | 5 50 | TUBE Yes SN N/A for Pkg Type -40 to 125 75701
TPS75701KC.A Active Production TO-220 (KC) | 5 50 | TUBE Yes SN N/A for Pkg Type -40 to 125 75701
TPS75701KCG3 Active Production TO-220 (KC) | 5 50 | TUBE Yes SN N/A for Pkg Type -40 to 125 75701
TPS75701KTTR Active Production DDPAK/
TO-263 (KTT) | 5
500 | LARGE T&R Yes SN Level-2-260C-1 YEAR -40 to 125 75701
TPS75701KTTR.A Active Production DDPAK/
TO-263 (KTT) | 5
500 | LARGE T&R Yes SN Level-2-260C-1 YEAR -40 to 125 75701
TPS75715KC Active Production TO-220 (KC) | 5 50 | TUBE Yes SN N/A for Pkg Type -40 to 125 75715
TPS75715KC.A Active Production TO-220 (KC) | 5 50 | TUBE Yes SN N/A for Pkg Type -40 to 125 75715
TPS75715KTTR Active Production DDPAK/
TO-263 (KTT) | 5
500 | LARGE T&R Yes SN Level-2-260C-1 YEAR -40 to 125 75715
TPS75715KTTR.A Active Production DDPAK/
TO-263 (KTT) | 5
500 | LARGE T&R Yes SN Level-2-260C-1 YEAR -40 to 125 75715
TPS75718KC Active Production TO-220 (KC) | 5 50 | TUBE Yes SN N/A for Pkg Type -40 to 125 75718
TPS75718KC.A Active Production TO-220 (KC) | 5 50 | TUBE Yes SN N/A for Pkg Type -40 to 125 75718
TPS75718KTTR Active Production DDPAK/
TO-263 (KTT) | 5
500 | LARGE T&R Yes SN Level-2-260C-1 YEAR -40 to 125 75718
TPS75718KTTR.A Active Production DDPAK/
TO-263 (KTT) | 5
500 | LARGE T&R Yes SN Level-2-260C-1 YEAR -40 to 125 75718
TPS75725KC Active Production TO-220 (KC) | 5 50 | TUBE Yes SN N/A for Pkg Type -40 to 125 75725
TPS75725KC.A Active Production TO-220 (KC) | 5 50 | TUBE Yes SN N/A for Pkg Type -40 to 125 75725
TPS75725KTTR Active Production DDPAK/
TO-263 (KTT) | 5
500 | LARGE T&R Yes SN Level-2-260C-1 YEAR -40 to 125 75725
TPS75725KTTR.A Active Production DDPAK/
TO-263 (KTT) | 5
500 | LARGE T&R Yes SN Level-2-260C-1 YEAR -40 to 125 75725
TPS75733KC Active Production TO-220 (KC) | 5 50 | TUBE Yes SN N/A for Pkg Type -40 to 125 75733
TPS75733KC.A Active Production TO-220 (KC) | 5 50 | TUBE Yes SN N/A for Pkg Type -40 to 125 75733
TPS75733KTTR Active Production DDPAK/
TO-263 (KTT) | 5
500 | LARGE T&R Yes SN Level-2-260C-1 YEAR -40 to 125 75733
TPS75733KTTR.A Active Production DDPAK/
TO-263 (KTT) | 5
500 | LARGE T&R Yes SN Level-2-260C-1 YEAR -40 to 125 75733
Addendum-Page 1
```

### Page 22

#### Extracted tables

Table 1:

```text
Orderable part number | Status (1) | Material type (2) | Package | Pins | Package qty | Carrier | RoHS (3) | Lead finish/ Ball material (4) | MSL rating/ Peak reflow (5) | Op temp ( deg C) | Part marking (6)
TPS75733KTTRG3 | Active | Production | DDPAK/ TO-263 (KTT) | 5 | 500 | LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | 40 to 125 | 75733
```

#### Raw extracted text

```text
PACKAGE OPTION ADDENDUM
www.ti.com 11-Nov-2025
Orderable part number Status
(1)
Material type
(2)
Package | Pins Package qty | Carrier RoHS
(3)
Lead finish/
Ball material
(4)
MSL rating/
Peak reflow
(5)
Op temp ( deg C) Part marking
(6)
TPS75733KTTRG3 Active Production DDPAK/
TO-263 (KTT) | 5
500 | LARGE T&R Yes SN Level-2-260C-1 YEAR -40 to 125 75733

(1) Status:  For more details on status, see our product life cycle.

(2) Material type:  When designated, preproduction parts are prototypes/experimental devices, and are not yet approved or released for full production. Testing and final process, including without limitation quality assurance,
reliability performance testing, and/or process qualification, may not yet be complete, and this item is subject to further changes or possible discontinuation. If available for ordering, purchases will be subject to an additional
waiver at checkout, and are intended for early internal evaluation purposes only. These items are sold without warranties of any kind.

(3) RoHS values:  Yes, No, RoHS Exempt. See the TI RoHS Statement for additional information and value definition.

(4) Lead finish/Ball material:  Parts may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead finish/Ball material values may wrap to two lines if the finish value exceeds the maximum
column width.

(5) MSL rating/Peak reflow:  The moisture sensitivity level ratings and peak solder (reflow) temperatures. In the event that a part has multiple moisture sensitivity ratings, only the lowest level per JEDEC standards is shown.
Refer to the shipping label for the actual reflow temperature that will be used to mount the part to the printed circuit board.

(6) Part marking:  There may be an additional marking, which relates to the logo, the lot trace code information, or the environmental category of the part.

Multiple part markings will be inside parentheses. Only one part marking contained in parentheses and separated by a "~" will appear on a part. If a line is indented then it is a continuation of the previous line and the two
combined represent the entire part marking for that device.

Important Information and Disclaimer:The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and
makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative
and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers
and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.

Addendum-Page 2
```

### Page 23

#### Extracted tables

Table 1:

```text
W |
```

Table 2:

```text
B | 0
```

Table 3:

```text
Re Diam | el eter
```

Table 4:

```text
A0 | Dimension designed to accommodate the component width
B0 | Dimension designed to accommodate the component length
K0 | Dimension designed to accommodate the component thickness
W | Overall width of the carrier tape
P1 | Pitch between successive cavity centers
```

Table 5:

```text
Q1 | Q2
Q3 | Q4
```

Table 6:

```text
Q1 | Q2
Q3 | Q4
```

Table 7:

```text
Device | Package Type | Package Drawing | Pins | SPQ | Reel Diameter (mm) | Reel Width W1 (mm) | A0 (mm) | B0 (mm) | K0 (mm) | P1 (mm) | W (mm) | Pin1 Quadrant
TPS75701KTTR | DDPAK/ TO-263 | KTT | 5 | 500 | 330.0 | 24.4 | 10.9 | 16.1 | 4.9 | 16.0 | 24.0 | Q2
TPS75715KTTR | DDPAK/ TO-263 | KTT | 5 | 500 | 330.0 | 24.4 | 10.9 | 16.1 | 4.9 | 16.0 | 24.0 | Q2
TPS75718KTTR | DDPAK/ TO-263 | KTT | 5 | 500 | 330.0 | 24.4 | 10.9 | 16.1 | 4.9 | 16.0 | 24.0 | Q2
TPS75725KTTR | DDPAK/ TO-263 | KTT | 5 | 500 | 330.0 | 24.4 | 10.9 | 16.1 | 4.9 | 16.0 | 24.0 | Q2
TPS75733KTTR | DDPAK/ TO-263 | KTT | 5 | 500 | 330.0 | 24.4 | 10.9 | 16.1 | 4.9 | 16.0 | 24.0 | Q2
```

#### Raw extracted text

```text
PACKAGE MATERIALS INFORMATION
www.ti.com 31-Aug-2025
TAPE AND REEL INFORMATION
REEL DIMENSIONS TAPE DIMENSIONS
K0 P1
W
B0
Reel
Diameter
Cavity A0
A0 Dimension designed to accommodate the component width
B0 Dimension designed to accommodate the component length
K0 Dimension designed to accommodate the component thickness
W Overall width of the carrier tape
P1 Pitch between successive cavity centers
Reel Width (W1)
QUADRANT ASSIGNMENTS FOR PIN 1 ORIENTATION IN TAPE
Sprocket Holes
Q1 Q2 Q1 Q2
Q3 Q4 Q3 Q4 User Direction of Feed
Pocket Quadrants
*All dimensions are nominal
Device Package Package Pins SPQ Reel Reel A0 B0 K0 P1 W Pin1
Type Drawing Diameter Width (mm) (mm) (mm) (mm) (mm) Quadrant
(mm) W1 (mm)
TPS75701KTTR DDPAK/ KTT 5 500 330.0 24.4 10.9 16.1 4.9 16.0 24.0 Q2
TO-263
TPS75715KTTR DDPAK/ KTT 5 500 330.0 24.4 10.9 16.1 4.9 16.0 24.0 Q2
TO-263
TPS75718KTTR DDPAK/ KTT 5 500 330.0 24.4 10.9 16.1 4.9 16.0 24.0 Q2
TO-263
TPS75725KTTR DDPAK/ KTT 5 500 330.0 24.4 10.9 16.1 4.9 16.0 24.0 Q2
TO-263
TPS75733KTTR DDPAK/ KTT 5 500 330.0 24.4 10.9 16.1 4.9 16.0 24.0 Q2
TO-263
Pack Materials-Page 1
```

### Page 24

#### Extracted tables

Table 1:

```text
| H
```

Table 2:

```text
Device | Package Type | Package Drawing | Pins | SPQ | Length (mm) | Width (mm) | Height (mm)
TPS75701KTTR | DDPAK/TO-263 | KTT | 5 | 500 | 356.0 | 356.0 | 45.0
TPS75715KTTR | DDPAK/TO-263 | KTT | 5 | 500 | 356.0 | 356.0 | 45.0
TPS75718KTTR | DDPAK/TO-263 | KTT | 5 | 500 | 356.0 | 356.0 | 45.0
TPS75725KTTR | DDPAK/TO-263 | KTT | 5 | 500 | 356.0 | 356.0 | 45.0
TPS75733KTTR | DDPAK/TO-263 | KTT | 5 | 500 | 356.0 | 356.0 | 45.0
```

#### Raw extracted text

```text
PACKAGE MATERIALS INFORMATION

www.ti.com 31-Aug-2025
TAPE AND REEL BOX DIMENSIONS
Width (mm)
W LH

*All dimensions are nominal
Device Package Type Package Drawing Pins SPQ Length (mm) Width (mm) Height (mm)
TPS75701KTTR DDPAK/TO-263 KTT 5 500 356.0 356.0 45.0
TPS75715KTTR DDPAK/TO-263 KTT 5 500 356.0 356.0 45.0
TPS75718KTTR DDPAK/TO-263 KTT 5 500 356.0 356.0 45.0
TPS75725KTTR DDPAK/TO-263 KTT 5 500 356.0 356.0 45.0
TPS75733KTTR DDPAK/TO-263 KTT 5 500 356.0 356.0 45.0
Pack Materials-Page 2
```

### Page 25

#### Extracted tables

Table 1:

```text
Device | Package Name | Package Type | Pins | SPQ | L (mm) | W (mm) | T (um) | B (mm)
TPS75701KC | KC | TO-220 | 5 | 50 | 546 | 31 | 11930 | 3.17
TPS75701KC.A | KC | TO-220 | 5 | 50 | 546 | 31 | 11930 | 3.17
TPS75701KCG3 | KC | TO-220 | 5 | 50 | 546 | 31 | 11930 | 3.17
TPS75715KC | KC | TO-220 | 5 | 50 | 546 | 31 | 11930 | 3.17
TPS75715KC.A | KC | TO-220 | 5 | 50 | 546 | 31 | 11930 | 3.17
TPS75718KC | KC | TO-220 | 5 | 50 | 546 | 31 | 11930 | 3.17
TPS75718KC.A | KC | TO-220 | 5 | 50 | 546 | 31 | 11930 | 3.17
TPS75725KC | KC | TO-220 | 5 | 50 | 546 | 31 | 11930 | 3.17
TPS75725KC.A | KC | TO-220 | 5 | 50 | 546 | 31 | 11930 | 3.17
TPS75733KC | KC | TO-220 | 5 | 50 | 546 | 31 | 11930 | 3.17
TPS75733KC.A | KC | TO-220 | 5 | 50 | 546 | 31 | 11930 | 3.17
```

#### Raw extracted text

```text
PACKAGE MATERIALS INFORMATION

www.ti.com 31-Aug-2025
TUBE

L - Tube length
T - Tube
height
W - Tube
width
B - Alignment groove width

*All dimensions are nominal
Device Package Name Package Type Pins SPQ L (mm) W (mm) T (um) B (mm)
TPS75701KC KC TO-220 5 50 546 31 11930 3.17
TPS75701KC.A KC TO-220 5 50 546 31 11930 3.17
TPS75701KCG3 KC TO-220 5 50 546 31 11930 3.17
TPS75715KC KC TO-220 5 50 546 31 11930 3.17
TPS75715KC.A KC TO-220 5 50 546 31 11930 3.17
TPS75718KC KC TO-220 5 50 546 31 11930 3.17
TPS75718KC.A KC TO-220 5 50 546 31 11930 3.17
TPS75725KC KC TO-220 5 50 546 31 11930 3.17
TPS75725KC.A KC TO-220 5 50 546 31 11930 3.17
TPS75733KC KC TO-220 5 50 546 31 11930 3.17
TPS75733KC.A KC TO-220 5 50 546 31 11930 3.17
Pack Materials-Page 3
```

### Page 26

#### Extracted tables

Table 1:

```text
|  | 0.25 | C | A
```

Table 2:

```text
1 5 |  |  |
```

#### Raw extracted text

```text
www.ti.com
PACKAGE OUTLINE
C
B
9.25
7.67
6.86
5.69
3.05
2.54
14.73
12.29
5X 1.02
0.64
4X 1.7
8.89
6.86 12.88
10.08
(6.275)
4.83
4.06
1.40
1.14
3.05
2.03
0.61
0.30
-3.96 3.71
6.8
2X (R1)
OPTIONAL
16.51
MAX
A10.67
9.65
(4.25)
4215009/A   01/2017
TO-220 - 16.51 mm max heightKC0005A
TO-220
 NOTES:

1. All controlling linear dimensions are in inches. Dimensions in brackets are in millimeters. Any dimension in brackets or parenthesis are for
    reference only. Dimensioning and tolerancing per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. Shape may vary per different assembly sites.
0.25 C A B
PIN 1 ID
(OPTIONAL)
1 5
OPTIONAL
CHAMFER
SCALE  0.850
NOTE 3
1 5
A A A A
```

### Page 27

#### Raw extracted text

```text
www.ti.com
EXAMPLE BOARD LAYOUT
0.07 MAX
ALL AROUND0.07 MAX
ALL AROUND (1.45)
(2)
(R0.05) TYP
4X (1.45)
4X (2)
5X ( 1.2)
(1.7) TYP
(6.8)
FULL R
TYP
TO-220 - 16.51 mm max heightKC0005A
TO-220
4215009/A   01/2017
LAND PATTERN
NON-SOLDER MASK DEFINED
SCALE:12X
PKG
PKG
METAL
TYP
SOLDER MASK
OPENING, TYP
1 5
```

### Page 28

#### Raw extracted text

```text
[No text could be extracted from this page with the current local extractor.]
```

### Page 29

#### Raw extracted text

```text
[No text could be extracted from this page with the current local extractor.]
```

### Page 30

#### Raw extracted text

```text
IMPORTANT NOTICE AND DISCLAIMER
TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATASHEETS), DESIGN RESOURCES (INCLUDING REFERENCE
DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES AS IS
AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY
IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD
PARTY INTELLECTUAL PROPERTY RIGHTS.
These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate
TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable
standards, and any other safety, security, regulatory or other requirements.
These resources are subject to change without notice. TI grants you permission to use these resources only for development of an
application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license
is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you fully
indemnify TI and its representatives against any claims, damages, costs, losses, and liabilities arising out of your use of these resources.
TIs products are provided subject to TIs Terms of Sale, TIs General Quality Guidelines, or other applicable terms available either on
ti.com or provided in conjunction with such TI products. TIs provision of these resources does not expand or otherwise alter TIs applicable
warranties or warranty disclaimers for TI products. Unless TI explicitly designates a product as custom or customer-specified, TI products
are standard, catalog, general purpose devices.
TI objects to and rejects any additional or different terms you may propose.
IMPORTANT NOTICE
Copyright  2025, Texas Instruments Incorporated
Last updated 10/2025
```
