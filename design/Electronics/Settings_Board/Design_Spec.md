# Settings Board (V1.0) Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-XX

---

## 1. Overview

The Settings Board is a panel-mount PCB providing user-accessible hardware configuration switches
for the Enigma-NG system. It replaces the DIP switches previously located on the Stator Board with
12 sub-miniature SPDT toggle switches plus 12 discrete RGB status LEDs, mounted through the right
side of the enclosure top face near the rotors. A momentary CFG_APPLY pushbutton triggers CPLD
configuration re-latch via the CM5 firmware.

The Settings Board communicates with the Stator Board exclusively via a 4-wire I²C ribbon cable
(J_I2C → Stator J_CFG), sharing the Stator I²C-1 bus. It hosts two MCP23017 GPIO expanders:

* **U_EXP_SW_IN (@ 0x26):** Reads all 12 switch states and the CFG_APPLY momentary button.
* **U_EXP_LED (@ 0x27):** Drives per-bit LED anodes and per-bank colour-rail low-side sinks.

No JTAG chain is present on this board. All configuration logic is handled by the CM5 enigma
daemon over I²C.

* **Location:** Right side of enclosure top face, near rotors.
* **Mounting:** Panel-mount switches through enclosure panel; PCB mounted behind panel.
* **Stackup:** 4-layer JLC04161H-7628 / 2oz copper.
* **Role:** User-accessible configuration panel; I²C peripheral to Stator Board.

### Functional & Design Requirements

#### Functional Requirements

| ID | Functional Requirement | Notes | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| FR-SBD-01 | Provide 12 user-accessible toggle switches with matching RGB status LEDs for hardware configuration without opening the enclosure | 5 switches for Bank 1 (plugboard routing); 7 for Bank 2 (reflector mapping); panel-mount through enclosure top face | §3 Switch Bank Descriptions; §4 I²C Devices |
| FR-SBD-02 | Allow CM5 firmware to override hardware switch settings on a per-bank basis | Bank enable switch (SW_B1_EN / SW_B2_EN): HIGH = switch-defined active; LOW = CM5-defined override | §5 LED Control Logic; Stator/Design_Spec.md FR-STA-08/09 |
| FR-SBD-03 | Provide visual feedback via RGB LED illumination showing configuration source and active bit state | Green = switch-defined active; Red = CM5-defined override; per-bank shared colour rails + per-bit individual LED anode drive with per-colour cathode-return resistors | §5 LED Control Logic |
| FR-SBD-04 | Provide a momentary CFG_APPLY pushbutton that triggers CPLD configuration re-latch | CM5 daemon polls U_EXP_SW_IN GPB[7]; active-low; 10kΩ pull-up + 100nF X7R 0402 debounce cap | §6 CFG_APPLY Button |
| FR-SBD-05 | Connect to the Stator Board via a 4-wire I²C ribbon cable (3V3_ENIG, GND, SDA, SCL) | J_I2C = 4-pin JST PH 2.0mm connector; shares Stator I²C-1 bus | §7 Interconnects; BOM J_I2C |

#### Design Requirements

| ID | Design Requirement | Specification | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| DR-SBD-01 | PCB stackup | 4-layer, 2oz finished copper (JLCPCB JLC04161H-7628) | §8 PCB Fabrication |
| DR-SBD-02 | Switch + indicator type | 12× E-Switch 200MSP1T2B4M2QE panel-mount SPDT latching toggle switches plus 12× Kingbright WP154A4SEJ3VBDZGW/CA common-anode RGB through-hole LEDs; one LED per switch position | §3 Switch Bank Descriptions; BOM SW_B1_EN, SW_B1[0:3], SW_B2_EN, SW_B2[0:5], LED_B1_EN, LED_B1[0:3], LED_B2_EN, LED_B2[0:5] |
| DR-SBD-03 | Switch input expander | U_EXP_SW_IN = MCP23017T-E/SO @ 0x26; SOIC-28; A2=HIGH, A1=HIGH, A0=LOW | §4 I²C Devices — U_EXP_SW_IN; BOM U_EXP_SW_IN |
| DR-SBD-04 | LED output expander | U_EXP_LED = MCP23017T-E/SO @ 0x27; SOIC-28; A2=HIGH, A1=HIGH, A0=HIGH | §4 I²C Devices — U_EXP_LED; BOM U_EXP_LED |
| DR-SBD-05 | LED colour-rail transistors | 4× BSS138 SOT-23 N-channel MOSFETs (Q_BNK1_G, Q_BNK1_R, Q_BNK2_G, Q_BNK2_R); gate driven from U_EXP_LED GPIO via 1kΩ gate resistor; GPIO HIGH = transistor ON (low-side sink topology) | §5 LED Control Logic; BOM Q_BNK1_G, Q_BNK1_R, Q_BNK2_G, Q_BNK2_R |
| DR-SBD-06 | CFG_APPLY button | SW_CFG_APPLY = SPST momentary pushbutton, active-low; 10kΩ pull-up to 3V3_ENIG (R_CA1) + 100nF X7R 0402 debounce cap to GND (C_CA1; RC τ = 1ms); connected to U_EXP_SW_IN GPB[7] | §6 CFG_APPLY Button; BOM SW_CFG_APPLY, R_CA1, C_CA1 |
| DR-SBD-07 | I²C connector | J_I2C = 4-pin JST PH 2.0mm B4B-PH-K-S(LF)(SN); pins: 3V3_ENIG, GND, SDA, SCL; ribbon cable to Stator J_CFG | §7 Interconnects; BOM J_I2C |
| DR-SBD-08 | Switch input pull-downs | 12× 10kΩ 0603 pull-down resistors on all switch signal inputs to U_EXP_SW_IN (GPA[0:4], GPB[0:6]); HIGH = switch-defined active when switch closed | §4 I²C Devices — U_EXP_SW_IN; BOM R_SW1–R_SW12 |

---

## 2. Core Features

* **12 Panel-Mount Toggle Switches + 12 RGB LEDs:** E-Switch 200 series SPDT toggles provide the
  configuration inputs; one discrete Kingbright common-anode RGB LED is mounted beside each switch.
  Bank 1 (5 positions): plugboard routing config. Bank 2 (7 positions): reflector map config.
* **MCP23017 Dual-Expander Architecture:** U_EXP_SW_IN reads all switch states; U_EXP_LED drives
  all LED illumination. Separate expanders prevent LED drive state from interfering with switch
  read-back.
* **Per-Bank Enable Control:** Each bank has a dedicated enable switch (SW_B1_EN, SW_B2_EN). When
  HIGH, the physical switch positions define the configuration. When LOW, the CM5 firmware defines
  the configuration.
* **RGB LED Feedback:** Green = switch-defined active; Red = CM5-defined override. Per-bit anode
  control illuminates only set bits. Shared per-bank colour rails simplify wiring (4 low-side sink
  MOSFETs total). Blue die is left unconnected.
* **CFG_APPLY Button:** Momentary pushbutton triggers configuration re-latch cycle via CM5 daemon.
  CM5 reads switch state, writes U_EXP4 on Stator, and pulses STATOR_CFG_RDY.
* **I²C-Only Interface:** 4-wire ribbon cable to Stator (3V3_ENIG, GND, SDA, SCL) — no parallel
  signal wiring.

### GND_CHASSIS Single-Point Bond

Per `design/Standards/Global_Routing_Spec.md §5`, the Settings Board GND_CHASSIS bond point is at
J_I2C pin 2 (GND entry). A single 0 Ω bond resistor (or direct via) connects the signal GND plane
to the chassis copper pour at this entry point. No additional chassis bonds are made on this board
to avoid ground loops.

---

## 3. Switch Bank Descriptions

### Bank 1 — Plugboard Routing (SW_B1_EN + SW_B1[0:3])

Bank 1 provides a 4-bit binary index (SW_B1[3:0], 0–15) selecting the active routing case from 16
configurations synthesised into the Stator CPLD fabric. SW_B1[1:0] encode J5 (Plugboard A)
insertion position; SW_B1[3:2] encode J6 (Plugboard B) insertion position.

SW_B1_EN is the bank enable switch: HIGH = Bank 1 is switch-defined (CM5 forwards physical switch
readings to U_EXP4 on the Stator). LOW = Bank 1 is CM5-defined (CM5 writes its own configuration
to U_EXP4 GPA[0:3]).

Pull-down resistors (10kΩ, one per switch signal) hold each input at logic-0 when the
corresponding switch is open. On the Stator, R16–R26 provide the corresponding pull-downs on the
CPLD input pins to maintain a safe all-zero default before CM5 initialises U_EXP4.

The active configuration is driven to the CPLD by U_EXP4 GPA[0:3] on the Stator Board via I²C.
A STATOR_CFG_RDY strobe (U_EXP4 GPA[4]) triggers CPLD re-latch after CM5 writes the final
configuration.

| SW_B1 Index (SW_B1[3]:SW_B1[2]:SW_B1[1]:SW_B1[0]) | J5 (Plugboard A) insertion point | J6 (Plugboard B) insertion point | Historical reference |
| :--- | :--- | :--- | :--- |
| 0 (0000) | None | None | No plugboard — straight through |
| 1 (0001) | Pre-Rotor 1 | None | Single pre-Rotor 1 pass |
| 2 (0010) | At Reflector | None | Later Enigma models (single reflector pass) |
| 3 (0011) | Post-Rotor 1 return | None | Single post-Rotor 1 pass |
| 4 (0100) | None | Pre-Rotor 1 | — |
| 5 (0101) | Pre-Rotor 1 | Pre-Rotor 1 | Cascaded pre-Rotor 1 |
| 6 (0110) | At Reflector | Pre-Rotor 1 | — |
| 7 (0111) | Post-Rotor 1 return | Pre-Rotor 1 | — |
| 8 (1000) | None | At Reflector | — |
| 9 (1001) | Pre-Rotor 1 | At Reflector | — |
| 10 (1010) | At Reflector | At Reflector | Cascaded at Reflector |
| 11 (1011) | Post-Rotor 1 return | At Reflector | — |
| 12 (1100) | None | Post-Rotor 1 return | — |
| 13 (1101) | Pre-Rotor 1 | Post-Rotor 1 return | Original Enigma (pre-war) |
| 14 (1110) | At Reflector | Post-Rotor 1 return | — |
| 15 (1111) | Post-Rotor 1 return | Post-Rotor 1 return | Cascaded post-Rotor 1 |

### Bank 2 — Reflector Mapping (SW_B2_EN + SW_B2[0:5])

Bank 2 controls whether the Stator CPLD applies an internal reflector substitution map at the
reflection boundary or passes data through J7 normally.

SW_B2_EN is the bank enable switch: HIGH = Bank 2 is switch-defined. LOW = Bank 2 is CM5-defined.

| Bit | Switch | Function |
| :--- | :--- | :--- |
| `SW_B2[5]` | SW_B2[5] | **Internal reflector enable**: HIGH = apply stored map; LOW = pass through to J7 (physical Reflector) |
| `SW_B2[4:0]` | SW_B2[4:0] | **Map index** (0–20): selects which involutory map to load from CPLD UFM at configuration load |

Pull-down resistors R21–R26 on the Stator CPLD input pins hold each input at logic-0 when U_EXP4
is uninitialised (default = SW_B2[5]=0, physical Reflector mode).

When SW_B2[5]=0, J7 ENC_IN/OUT operate normally and SW_B2[4:0] is ignored. When SW_B2[5]=1, the
CPLD applies the indexed map combinationally at the reflection boundary instead of forwarding to J7.

**UFM map storage:** 21 involutory reflector maps (same as defined in Stator/Design_Spec.md §3):

| Index | Map | Notes |
| :--- | :--- | :--- |
| 0 | UKW-A equivalent | Historical Enigma Reflector A (26-char; entries 26–63 = identity for 64-char variant) |
| 1 | UKW-B equivalent | Historical Enigma Reflector B — most common WWII Enigma variant |
| 2 | UKW-C equivalent | Historical Enigma Reflector C — later wartime variant |
| 3–20 | Custom | User-defined involutory maps via JTAG programming |

---

## 4. I²C Devices

All Settings Board I²C devices share the Stator I²C-1 bus via J_I2C → Stator J_CFG.

### U_EXP_SW_IN — MCP23017T-E/SO @ 0x26

Reads all 12 switch states and the CFG_APPLY momentary button.

**Address:** 0x26 — MCP23017 base 0x20; A2=HIGH, A1=HIGH, A0=LOW → 0x20 | 0b110 = 0x26

| Port | Pin | Signal | Direction | Pull | Description |
| :--- | :--- | :--- | :--- | :--- | :--- |
| GPA | [0] | SW_B1_EN | Input | 10kΩ pull-down | Bank 1 enable; HIGH = switch-defined active |
| GPA | [1] | SW_B1[0] | Input | 10kΩ pull-down | Bank 1 routing config bit 0 |
| GPA | [2] | SW_B1[1] | Input | 10kΩ pull-down | Bank 1 routing config bit 1 |
| GPA | [3] | SW_B1[2] | Input | 10kΩ pull-down | Bank 1 routing config bit 2 |
| GPA | [4] | SW_B1[3] | Input | 10kΩ pull-down | Bank 1 routing config bit 3 |
| GPA | [5:7] | — | Input | — | Spare (reserved future use) |
| GPB | [0] | SW_B2_EN | Input | 10kΩ pull-down | Bank 2 enable; HIGH = switch-defined active |
| GPB | [1] | SW_B2[0] | Input | 10kΩ pull-down | Bank 2 reflector config bit 0 |
| GPB | [2] | SW_B2[1] | Input | 10kΩ pull-down | Bank 2 reflector config bit 1 |
| GPB | [3] | SW_B2[2] | Input | 10kΩ pull-down | Bank 2 reflector config bit 2 |
| GPB | [4] | SW_B2[3] | Input | 10kΩ pull-down | Bank 2 reflector config bit 3 |
| GPB | [5] | SW_B2[4] | Input | 10kΩ pull-down | Bank 2 reflector config bit 4 |
| GPB | [6] | SW_B2[5] | Input | 10kΩ pull-down | Bank 2 reflector config bit 5 (internal reflector enable) |
| GPB | [7] | CFG_APPLY | Input | 10kΩ pull-up to 3V3_ENIG | Active-low momentary; 100nF X7R debounce cap to GND |

> All switch signal inputs (GPA[0:4], GPB[0:6]) use 10kΩ pull-down resistors: open/off switch = logic-0.
> CFG_APPLY (GPB[7]) uses 10kΩ pull-up: active button press = logic-0.
>
> Each `200MSP1T2B4M2QE` toggle is wired as an SPDT-used-as-SPST input: the centre COM lug goes
> to the named `SW_B*` signal net, the asserted throw goes to `3V3_ENIG`, and the opposite throw is
> left unconnected in Rev A. Panel orientation shall make the lever-up / marked-ON position select
> the `3V3_ENIG` throw so the asserted state always reads logic-1.

### U_EXP_LED — MCP23017T-E/SO @ 0x27

Drives per-bit LED anodes and per-bank red / green low-side sink transistors. Each LED's blue
cathode is also routed through a dedicated 0Ω debug-link footprint for prototype bring-up.

**Address:** 0x27 — A2=HIGH, A1=HIGH, A0=HIGH → 0x20 | 0b111 = 0x27

| Port | Pin | Signal | Direction | Description |
| :--- | :--- | :--- | :--- | :--- |
| GPA | [0] | LED_B1_EN_A | Output | Bank 1 LED anode enable for SW_B1_EN; HIGH = LED source enabled |
| GPA | [1] | LED_B1_0_A | Output | Bank 1 LED anode enable for SW_B1[0]; HIGH = LED source enabled |
| GPA | [2] | LED_B1_1_A | Output | Bank 1 LED anode enable for SW_B1[1]; HIGH = LED source enabled |
| GPA | [3] | LED_B1_2_A | Output | Bank 1 LED anode enable for SW_B1[2]; HIGH = LED source enabled |
| GPA | [4] | LED_B1_3_A | Output | Bank 1 LED anode enable for SW_B1[3]; HIGH = LED source enabled |
| GPA | [5] | BNK1_G | Output | Bank 1 green cathode rail; drives gate of Q_BNK1_G; HIGH = green rail active |
| GPA | [6] | BNK1_R | Output | Bank 1 red cathode rail; drives gate of Q_BNK1_R; HIGH = red rail active |
| GPA | [7] | BNK2_G | Output | Bank 2 green cathode rail; drives gate of Q_BNK2_G; HIGH = green rail active |
| GPB | [0] | LED_B2_EN_A | Output | Bank 2 LED anode enable for SW_B2_EN; HIGH = LED source enabled |
| GPB | [1] | LED_B2_0_A | Output | Bank 2 LED anode enable for SW_B2[0]; HIGH = LED source enabled |
| GPB | [2] | LED_B2_1_A | Output | Bank 2 LED anode enable for SW_B2[1]; HIGH = LED source enabled |
| GPB | [3] | LED_B2_2_A | Output | Bank 2 LED anode enable for SW_B2[2]; HIGH = LED source enabled |
| GPB | [4] | LED_B2_3_A | Output | Bank 2 LED anode enable for SW_B2[3]; HIGH = LED source enabled |
| GPB | [5] | LED_B2_4_A | Output | Bank 2 LED anode enable for SW_B2[4]; HIGH = LED source enabled |
| GPB | [6] | LED_B2_5_A | Output | Bank 2 LED anode enable for SW_B2[5]; HIGH = LED source enabled |
| GPB | [7] | BNK2_R | Output | Bank 2 red cathode rail; drives gate of Q_BNK2_R; HIGH = red rail active |

> Individual LED anode outputs drive HIGH only for the bits that should be illuminated. Each LED's
> red and green cathodes return through separate per-colour resistors to the shared bank colour
> rails. The blue cathode is routed through the per-switch 0Ω link footprint group (`R_LED_B (x12)`) to an
> isolated debug node so prototype builds can bodge or instrument the blue die without cutting
> traces. Only one colour rail is enabled at any time per bank, so all lit LEDs in that bank show
> the same colour without consuming extra GPIOs.

---

## 5. LED Control Logic

### Colour Scheme

| Bank Enable State | Colour Rail Active | Meaning |
| :--- | :--- | :--- |
| HIGH (switch-defined active) | Green (BNKx_G transistor ON) | Configuration source = physical switches |
| LOW (CM5-defined override) | Red (BNKx_R transistor ON) | Configuration source = CM5 firmware |

### Per-Bit Illumination

* Each switch in a bank has an individual LED anode output (LED_B1_EN_A / LED_B1_0_A... and
  LED_B2_EN_A / LED_B2_0_A...).
* CM5 daemon sets each anode HIGH to illuminate that bit's LED when the corresponding bit in the
  active configuration is set (= 1) and the correct bank colour rail is enabled.
* Unset bits (= 0) have their anode held LOW (LED off); only active configuration bits are
  illuminated.

### Bank Enable Switch LED

The bank enable switch (SW_B1_EN / SW_B2_EN) has its own LED anode pin (LED_B1_EN_A /
LED_B2_EN_A) and is illuminated whenever the bank enable is active, providing a visual on/off
indicator for the entire bank.

### Low-Side Colour-Rail Circuit

Each colour rail (BNK1_G, BNK1_R, BNK2_G, BNK2_R) is driven by a BSS138 SOT-23 N-channel MOSFET:

* **Source:** tied to GND.
* **Drain:** connects to the shared bank colour rail (green or red cathode return).
* **Gate:** driven by U_EXP_LED GPIO output via 1kΩ gate resistor.

Each LED uses two dedicated series resistors: one in the red cathode path and one in the green
cathode path. This allows the red and green dice to be balanced independently under nominal 3.3V
operation. The blue cathode is routed through the dedicated 0Ω debug-link footprint group (`R_LED_B (x12)`) to
an otherwise isolated local node; no blue bank driver is fitted in Rev A.

When the GPIO output is HIGH, the transistor turns ON, sinking the selected colour rail to GND and
illuminating any LEDs in that bank whose anode outputs are HIGH. GPIO LOW = transistor OFF = colour
rail disabled.

---

## 6. CFG_APPLY Button

SW_CFG_APPLY is a panel-mount momentary pushbutton (SPST, active-low) connected to U_EXP_SW_IN
GPB[7].

* **Pull-up:** 10kΩ to 3V3_ENIG (R_CA1) — idle state = logic HIGH.
* **Debounce:** 100nF X7R 0402 capacitor to GND (C_CA1; RC τ = 1ms).
* **Operation:** CM5 enigma daemon polls GPB[7] during its main loop. On detecting LOW (button
  pressed, after debounce), the daemon:
  1. Reads U_EXP_SW_IN (full 16-bit state).
  2. Evaluates bank enables for Bank 1 and Bank 2.
  3. Writes final configuration to U_EXP4 GPA[0:3] and GPB[0:5] on the Stator Board.
  4. Pulses STATOR_CFG_RDY (U_EXP4 GPA[4]) LOW then HIGH to trigger CPLD re-latch.
  5. Updates U_EXP_LED outputs to reflect the new configuration state.

This button provides operator-initiated explicit configuration commit without relying solely on
automatic polling intervals.

---

## 7. Interconnects

### J_I2C — I²C Connector to Stator Board

| Pin | Signal | Notes |
| :--- | :--- | :--- |
| 1 | 3V3_ENIG | Power from Stator; powers Settings Board logic |
| 2 | GND | Common ground; GND_CHASSIS bond point |
| 3 | SDA | I²C data; shared Stator I²C-1 bus |
| 4 | SCL | I²C clock; shared Stator I²C-1 bus |

**Connector:** JST B4B-PH-K-S(LF)(SN) — 4-pin JST PH 2.0mm THT
(Mouser: 474-B4B-PH-K-S(LF)(SN), DigiKey: 455-1721-ND, JLCPCB: TBD — C131342 is the 3-pin B3B-PH-K-S; 4-pin B4B JLCPCB PN unconfirmed)

**Cable:** 4-wire ribbon cable (100mm recommended); matching JST PHR-4 crimp housing on both ends.

**Mating connector on Stator:** J_CFG — same JST PH 2.0mm 4-pin part.

---

## 8. PCB Fabrication

* **Manufacturer:** JLCPCB
* **Layer count:** 4-layer
* **Stackup:** JLC04161H-7628
* **Board thickness:** 1.6mm
* **Copper weight:** 2oz outer (system-wide standard)
* **Surface finish:** ENIG
* **Min trace/space:** 0.1mm / 0.1mm
* **Min drill:** 0.2mm
* **JTAG chain:** None — Settings Board is not in any JTAG chain.

---

## 9. Bill of Materials

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C_CA1 | CFG_APPLY debounce capacitor | 100nF X7R 50V | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 |
| C_U_EXP_SW_IN | VCC decoupling cap for U_EXP_SW_IN (MCP23017 @ 0x26) | 100nF X7R 50V | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 |
| C_U_EXP_LED | VCC decoupling cap for U_EXP_LED (MCP23017 @ 0x27) | 100nF X7R 50V | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 |
| J_I2C | I²C ribbon cable connector to Stator J_CFG | JST B4B-PH-K-S(LF)(SN) — 4-pin JST PH 2.0mm | THT | 474-B4B-PH-K-S(LF)(SN) | 455-1721-ND | TBD (C131342 is 3-pin B3B; 4-pin B4B JLCPCB PN unconfirmed) |
| LED_B1_EN, LED_B1[0:3] | Bank 1 discrete RGB indicator LEDs (×5) | Kingbright WP154A4SEJ3VBDZGW/CA — 5mm common-anode RGB THT LED; red/green used in normal operation, blue routed via 0Ω debug link | THT 5mm LED | 604-WP154A43VBDZGWCA | 754-2029-ND | C7151795 |
| LED_B2_EN, LED_B2[0:5] | Bank 2 discrete RGB indicator LEDs (×7) | Kingbright WP154A4SEJ3VBDZGW/CA — same part as Bank 1 | THT 5mm LED | 604-WP154A43VBDZGWCA | 754-2029-ND | C7151795 |
| Q_BNK1_G | Bank 1 green colour-rail sink MOSFET | BSS138 | SOT-23 | 512-BSS138 | BSS138CT-ND | C255592 |
| Q_BNK1_R | Bank 1 red colour-rail sink MOSFET | BSS138 | SOT-23 | 512-BSS138 | BSS138CT-ND | C255592 |
| Q_BNK2_G | Bank 2 green colour-rail sink MOSFET | BSS138 | SOT-23 | 512-BSS138 | BSS138CT-ND | C255592 |
| Q_BNK2_R | Bank 2 red colour-rail sink MOSFET | BSS138 | SOT-23 | 512-BSS138 | BSS138CT-ND | C255592 |
| R_CA1 | CFG_APPLY pull-up resistor | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R_SW1–R_SW5 | Bank 1 switch input pull-downs (×5: SW_B1_EN + SW_B1[0:3]) | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R_SW6–R_SW12 | Bank 2 switch input pull-downs (×7: SW_B2_EN + SW_B2[0:5]) | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R_LED_R1–R_LED_R12 | Per-switch red LED series resistors (×12) | Value tuned at schematic phase for nominal 3.3V operation and desired panel brightness | 0603 | TBD | TBD | TBD |
| R_LED_G1–R_LED_G12 | Per-switch green LED series resistors (×12) | Value tuned at schematic phase for nominal 3.3V operation and desired panel brightness | 0603 | TBD | TBD | TBD |
| R_LED_B (x12) | Per-switch blue LED debug links | 0Ω link; routes each blue cathode to an isolated debug node for prototype work | 0603 | 667-ERJ-3GEY0R00V | P0.0BYCT-ND | C25807 |
| R_GATE1–R_GATE4 | MOSFET gate resistors (×4, one per transistor) | 1kΩ (1%) | 0402 | 667-ERJ-2RKF1001X | P1.00KLBCT-ND | C25705 |
| SW_B1_EN | Bank 1 enable toggle switch | E-Switch 200MSP1T2B4M2QE — SPDT latching sub-mini toggle, T2 actuator, B4 bushing, M2 termination, Q silver contacts, epoxy sealed | Panel-mount THT toggle | 612-200MSP1T2B4M2QE | EG5525-ND | C5491263 |
| SW_B1[0] | Bank 1 routing config bit 0 toggle switch | E-Switch 200MSP1T2B4M2QE — same part as SW_B1_EN | Panel-mount THT toggle | 612-200MSP1T2B4M2QE | EG5525-ND | C5491263 |
| SW_B1[1] | Bank 1 routing config bit 1 toggle switch | E-Switch 200MSP1T2B4M2QE — same part as SW_B1_EN | Panel-mount THT toggle | 612-200MSP1T2B4M2QE | EG5525-ND | C5491263 |
| SW_B1[2] | Bank 1 routing config bit 2 toggle switch | E-Switch 200MSP1T2B4M2QE — same part as SW_B1_EN | Panel-mount THT toggle | 612-200MSP1T2B4M2QE | EG5525-ND | C5491263 |
| SW_B1[3] | Bank 1 routing config bit 3 toggle switch | E-Switch 200MSP1T2B4M2QE — same part as SW_B1_EN | Panel-mount THT toggle | 612-200MSP1T2B4M2QE | EG5525-ND | C5491263 |
| SW_B2_EN | Bank 2 enable toggle switch | E-Switch 200MSP1T2B4M2QE — same part as SW_B1_EN | Panel-mount THT toggle | 612-200MSP1T2B4M2QE | EG5525-ND | C5491263 |
| SW_B2[0] | Bank 2 reflector config bit 0 toggle switch | E-Switch 200MSP1T2B4M2QE — same part as SW_B1_EN | Panel-mount THT toggle | 612-200MSP1T2B4M2QE | EG5525-ND | C5491263 |
| SW_B2[1] | Bank 2 reflector config bit 1 toggle switch | E-Switch 200MSP1T2B4M2QE — same part as SW_B1_EN | Panel-mount THT toggle | 612-200MSP1T2B4M2QE | EG5525-ND | C5491263 |
| SW_B2[2] | Bank 2 reflector config bit 2 toggle switch | E-Switch 200MSP1T2B4M2QE — same part as SW_B1_EN | Panel-mount THT toggle | 612-200MSP1T2B4M2QE | EG5525-ND | C5491263 |
| SW_B2[3] | Bank 2 reflector config bit 3 toggle switch | E-Switch 200MSP1T2B4M2QE — same part as SW_B1_EN | Panel-mount THT toggle | 612-200MSP1T2B4M2QE | EG5525-ND | C5491263 |
| SW_B2[4] | Bank 2 reflector config bit 4 toggle switch | E-Switch 200MSP1T2B4M2QE — same part as SW_B1_EN | Panel-mount THT toggle | 612-200MSP1T2B4M2QE | EG5525-ND | C5491263 |
| SW_B2[5] | Bank 2 reflector config bit 5 toggle switch (internal reflector enable) | E-Switch 200MSP1T2B4M2QE — same part as SW_B1_EN | Panel-mount THT toggle | 612-200MSP1T2B4M2QE | EG5525-ND | C5491263 |
| SW_CFG_APPLY | CFG_APPLY momentary pushbutton | SPST NO momentary, panel-mount (MPN TBD) | Panel-mount | TBD | TBD | — |
| U_EXP_SW_IN | MCP23017 I²C GPIO Expander (switch input reader) | MCP23017T-E/SO @ 0x26 | SOIC-28 | 579-MCP23017T-E/SO | MCP23017T-E/SOCT-ND | C47023 |
| U_EXP_LED | MCP23017 I²C GPIO Expander (LED anode + colour rail driver) | MCP23017T-E/SO @ 0x27 | SOIC-28 | 579-MCP23017T-E/SO | MCP23017T-E/SOCT-ND | C47023 |
