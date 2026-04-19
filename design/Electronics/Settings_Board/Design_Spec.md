# Settings Board (V1.0) Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-17

---

## 1. Overview

The Settings Board is a panel-mount PCB providing user-accessible hardware configuration switches
for the Enigma-NG system. It replaces the DIP switches previously located on the Stator Board with
12 sub-miniature SPDT toggle switches plus 12 discrete RGB status LEDs, mounted through the right
side of the enclosure top face near the rotors. A momentary CFG_APPLY pushbutton triggers CPLD
configuration re-latch via the CM5 firmware.

The Settings Board communicates with the Stator Board exclusively via a 6-wire I²C harness
(J_I2C → Stator J_CFG), sharing the Stator I²C-1 bus. It hosts three MCP23017 GPIO expanders:

* **U_EXP_SW_IN (@ 0x23):** Reads all 12 switch states and the CFG_APPLY momentary button.
* **U_LED_B1 (@ 0x24):** Drives Bank 1 LED anodes (5 LEDs) and RGB bank-rail low-side switches.
* **U_LED_B2 (@ 0x25):** Drives Bank 2 LED anodes (7 LEDs) and RGB bank-rail low-side switches.

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
| FR-SBD-04 | Provide a momentary CFG_APPLY pushbutton that triggers CPLD configuration re-latch | CM5 daemon polls U_EXP_SW_IN GPB[7]; active-low; 10kΩ pull-up + 100nF X7R 0402 debounce cap. A board-mounted tactile switch actuated through the enclosure is acceptable; the switch itself need not be panel-mount. | §6 CFG_APPLY Button |
| FR-SBD-05 | Connect to the Stator Board via a 6-wire I²C harness (`3V3_ENIG`, `5V_MAIN`, 2× `GND`, `SDA`, `SCL`) | J_I2C = 6-pin JST PH 2.0mm connector; shares Stator I²C-1 bus; `5V_MAIN` powers the indicator LEDs | §7 Interconnects; BOM J_I2C |

#### Design Requirements

| ID | Design Requirement | Specification | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| DR-SBD-01 | PCB stackup | 4-layer, 2oz finished copper (JLCPCB JLC04161H-7628) | §8 PCB Fabrication |
| DR-SBD-02 | Switch + indicator type | 12× E-Switch 200MSP1T2B4M2QE panel-mount SPDT latching toggle switches plus 12× Kingbright WP154A4SEJ3VBDZGW/CA common-anode RGB through-hole LEDs; one LED per switch position | §3 Switch Bank Descriptions; BOM SW_B1_EN, SW_B1[0:3], SW_B2_EN, SW_B2[0:5], LED_B1_EN, LED_B1[0:3], LED_B2_EN, LED_B2[0:5] |
| DR-SBD-03 | Switch input expander | U_EXP_SW_IN = MCP23017T-E/SO @ 0x23; SOIC-28; contiguous after the Stator expander block | §4 I²C Devices — U_EXP_SW_IN; BOM U_EXP_SW_IN |
| DR-SBD-04 | LED control expanders | U_LED_B1 = MCP23017T-E/SO @ 0x24 (Bank 1); U_LED_B2 = MCP23017T-E/SO @ 0x25 (Bank 2); SOIC-28; per-switch anodes plus shared RGB bank rails | §4 I²C Devices — U_LED_B1, U_LED_B2; §5 LED Control Logic; BOM U_LED_B1, U_LED_B2 |
| DR-SBD-05 | LED colour-rail transistors | 6× BSS138 SOT-23 N-channel MOSFETs (`Q_BNK1_R/G/B`, `Q_BNK2_R/G/B`); gate driven via 1kΩ resistor; GPIO HIGH = transistor ON | §5 LED Control Logic; BOM Q_BNK1_R, Q_BNK1_G, Q_BNK1_B, Q_BNK2_R, Q_BNK2_G, Q_BNK2_B |
| DR-SBD-06 | LED power supply | `5V_MAIN` from the Stator via J_I2C pin 2; full RGB operation at 5V uses 150Ω red and 100Ω green/blue series resistors | §7 Interconnects — J_I2C; BOM R_LED_R/G/B |
| DR-SBD-07 | CFG_APPLY button | SW_CFG_APPLY = Omron B3F-1070 or equivalent SPST NO through-hole tactile switch, active-low; mounted on the Settings Board and actuated through the enclosure by a mechanical plunger/cap; 10kΩ pull-up to 3V3_ENIG + 100nF debounce cap; U_EXP_SW_IN GPB[7] | §6 CFG_APPLY Button; BOM SW_CFG_APPLY, R_CA1, C_CA1 |
| DR-SBD-08 | I²C connector | J_I2C = 6-pin JST PH 2.0mm B6B-PH-K-S(LF)(SN); pins: `3V3_ENIG`, `5V_MAIN`, `GND`, `SDA`, `SCL`, `GND`; harness to Stator J_CFG | §7 Interconnects; BOM J_I2C |
| DR-SBD-09 | Switch input pull-downs | 12× 10kΩ 0603 pull-down resistors on all switch inputs to U_EXP_SW_IN (GPA[0:4], GPB[0:6]); HIGH when closed | §4 I²C Devices — U_EXP_SW_IN; BOM R_SW1–R_SW12 |

---

## 2. Core Features

* **12 Panel-Mount Toggle Switches + 12 RGB LEDs:** E-Switch 200 series SPDT toggles provide the
  configuration inputs; one discrete Kingbright common-anode RGB LED is mounted beside each switch.
  Bank 1 (5 positions): plugboard routing config. Bank 2 (7 positions): reflector map config.
* **Three-Expander Architecture:** U_EXP_SW_IN reads all switch states, while U_LED_B1 and U_LED_B2
  independently drive the two indicator banks. Separate expanders prevent LED drive state from
  interfering with switch read-back and keep the Settings address block contiguous after the Stator.
* **Per-Bank Enable Control:** Each bank has a dedicated enable switch (SW_B1_EN, SW_B2_EN). When
  HIGH, the physical switch positions define the configuration. When LOW, the CM5 firmware defines
  the configuration.
* **RGB LED Feedback:** Green = switch-defined active; Red = CM5-defined override. Blue remains
  available for CM5-controlled diagnostic, boot, or fault states. Per-bit anode control illuminates
  only set bits. Shared per-bank RGB rails simplify wiring (6 low-side sink MOSFETs total).
* **CFG_APPLY Button:** Momentary pushbutton triggers configuration re-latch cycle via CM5 daemon.
  CM5 reads switch state, writes U_EXP4 on Stator, and pulses STATOR_CFG_RDY.
* **I²C-Only Interface:** 6-wire harness to Stator (`3V3_ENIG`, `5V_MAIN`, `GND`, `SDA`, `SCL`, `GND`) — no parallel signal wiring.

### GND_CHASSIS Single-Point Bond

Per `design/Standards/Global_Routing_Spec.md §5`, the Settings Board does **not** implement a local
GND-to-GND_CHASSIS bond. The system's only galvanic GND ↔ GND_CHASSIS bond is defined on the Power
Module at the main power-entry boundary. J_I2C pin 3 is therefore **logic GND return only**, and
must not be repurposed as a local chassis-bond point.

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

Bank 2 selects the reflector-map index used by the Stator CPLD. The physical Reflector board remains
mandatory and always provides the electrical turnaround at the end of the rotor/extension chain.

SW_B2_EN is the bank enable switch: HIGH = Bank 2 is switch-defined. LOW = Bank 2 is CM5-defined.

| Bit | Switch | Function |
| :--- | :--- | :--- |
| `SW_B2[5:0]` | SW_B2[5:0] | **6-bit map index** (0–63): selects which involutory map to load from CPLD UFM at configuration load; indices 0–20 are currently allocated |

Pull-down resistors R21–R26 on the Stator CPLD input pins hold each input at logic-0 when U_EXP4
is uninitialised (default map index = 0).

When Bank 2 is latched, the Stator CPLD loads the selected map and applies it at the reflection
boundary while the physical Reflector board remains in the active ENC signal path.

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

### U_EXP_SW_IN — MCP23017T-E/SO @ 0x23

Reads all 12 switch states and the CFG_APPLY momentary button.

**Address:** 0x23 — MCP23017 base 0x20; A2=LOW, A1=HIGH, A0=HIGH → 0x20 | 0b011 = 0x23

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
| GPB | [6] | SW_B2[5] | Input | 10kΩ pull-down | Bank 2 reflector config bit 5 |
| GPB | [7] | CFG_APPLY | Input | 10kΩ pull-up to 3V3_ENIG | Active-low momentary; 100nF X7R debounce cap to GND |

> All switch signal inputs (GPA[0:4], GPB[0:6]) use 10kΩ pull-down resistors: open/off switch = logic-0.
> CFG_APPLY (GPB[7]) uses 10kΩ pull-up: active button press = logic-0.
>
> Each `200MSP1T2B4M2QE` toggle is wired as an SPDT-used-as-SPST input: the centre COM lug goes
> to the named `SW_B*` signal net, the asserted throw goes to `3V3_ENIG`, and the opposite throw is
> left unconnected in Rev A. Panel orientation shall make the lever-up / marked-ON position select
> the `3V3_ENIG` throw so the asserted state always reads logic-1.

### U_LED_B1 — MCP23017T-E/SO @ 0x24

Drives Bank 1 LED anodes (5 LEDs) and RGB color-rail low-side transistor gates.

**Address:** 0x24 — MCP23017 base 0x20; A2=HIGH, A1=LOW, A0=LOW → 0x20 | 0b100 = 0x24

| Port | Pin | Signal | Direction | Description |
| :--- | :--- | :--- | :--- | :--- |
| GPA | [0] | LED_B1_EN_A | Output | Bank 1 enable LED anode; HIGH = LED source enabled |
| GPA | [1] | LED_B1_0_A | Output | Bank 1 bit 0 LED anode; HIGH = LED source enabled |
| GPA | [2] | LED_B1_1_A | Output | Bank 1 bit 1 LED anode; HIGH = LED source enabled |
| GPA | [3] | LED_B1_2_A | Output | Bank 1 bit 2 LED anode; HIGH = LED source enabled |
| GPA | [4] | LED_B1_3_A | Output | Bank 1 bit 3 LED anode; HIGH = LED source enabled |
| GPA | [5] | BNK1_R | Output | Bank 1 red cathode rail; drives gate of Q_BNK1_R; HIGH = red rail active |
| GPA | [6] | BNK1_G | Output | Bank 1 green cathode rail; drives gate of Q_BNK1_G; HIGH = green rail active |
| GPA | [7] | BNK1_B | Output | Bank 1 blue cathode rail; drives gate of Q_BNK1_B; HIGH = blue rail active |
| GPB | [0:7] | — | — | Spare (reserved future use) |

> Individual LED anode outputs drive HIGH only for the bits that should be illuminated. Each LED's
> red, green, and blue cathodes return through separate current-limiting resistors
> (`R_LED_R` = 150Ω, `R_LED_G` = 100Ω, `R_LED_B` = 100Ω) to the shared bank colour rails. LEDs are
> powered from the `5V_MAIN` feed delivered from the Controller through the Stator `J2A` / `J_CFG`
> path.

### U_LED_B2 — MCP23017T-E/SO @ 0x25

Drives Bank 2 LED anodes (7 LEDs) and RGB color-rail low-side transistor gates.

**Address:** 0x25 — MCP23017 base 0x20; A2=HIGH, A1=LOW, A0=HIGH → 0x20 | 0b101 = 0x25

| Port | Pin | Signal | Direction | Description |
| :--- | :--- | :--- | :--- | :--- |
| GPA | [0] | LED_B2_EN_A | Output | Bank 2 enable LED anode; HIGH = LED source enabled |
| GPA | [1] | LED_B2_0_A | Output | Bank 2 bit 0 LED anode; HIGH = LED source enabled |
| GPA | [2] | LED_B2_1_A | Output | Bank 2 bit 1 LED anode; HIGH = LED source enabled |
| GPA | [3] | LED_B2_2_A | Output | Bank 2 bit 2 LED anode; HIGH = LED source enabled |
| GPA | [4] | LED_B2_3_A | Output | Bank 2 bit 3 LED anode; HIGH = LED source enabled |
| GPA | [5] | LED_B2_4_A | Output | Bank 2 bit 4 LED anode; HIGH = LED source enabled |
| GPA | [6] | LED_B2_5_A | Output | Bank 2 bit 5 LED anode; HIGH = LED source enabled |
| GPA | [7] | BNK2_R | Output | Bank 2 red cathode rail; drives gate of Q_BNK2_R; HIGH = red rail active |
| GPB | [0] | BNK2_G | Output | Bank 2 green cathode rail; drives gate of Q_BNK2_G; HIGH = green rail active |
| GPB | [1] | BNK2_B | Output | Bank 2 blue cathode rail; drives gate of Q_BNK2_B; HIGH = blue rail active |
| GPB | [2:7] | — | — | Spare (reserved future use) |

---

## 5. LED Control Logic

### Colour Scheme

Full RGB capability with software-selectable colors per bank:

| Bank Enable State | Primary Colour | Meaning |
| :--- | :--- | :--- |
| HIGH (switch-defined active) | Green (BNKx_G transistor ON) | Configuration source = physical switches |
| LOW (CM5-defined override) | Red (BNKx_R transistor ON) | Configuration source = CM5 firmware |
| Special modes | Blue (BNKx_B transistor ON) | Future use: diagnostic, bootloader, error states |

> Software can select any RGB color by enabling the appropriate color-rail transistor. Only one
> color is active per bank at any time, so the definitive worst-case indicator-rail budget is
> **240mA total**: Bank 1 = 5 LEDs × 20mA = 100mA max, Bank 2 = 7 LEDs × 20mA = 140mA max.

### Per-Bit Illumination

* Each switch in a bank has an individual LED anode output (U_LED_B1 drives Bank 1 anodes,
  U_LED_B2 drives Bank 2 anodes).
* CM5 daemon sets each anode HIGH to illuminate that bit's LED when the corresponding bit in the
  active configuration is set (= 1) and the correct bank colour rail is enabled.
* Unset bits (= 0) have their anode held LOW (LED off); only active configuration bits are
  illuminated.

### Bank Enable Switch LED

The bank enable switch (SW_B1_EN / SW_B2_EN) has its own LED anode pin (LED_B1_EN_A /
LED_B2_EN_A) and is illuminated whenever the bank enable is active, providing a visual on/off
indicator for the entire bank.

### Low-Side Colour-Rail Circuit

Each colour rail (BNK1_R, BNK1_G, BNK1_B, BNK2_R, BNK2_G, BNK2_B) is driven by a BSS138 SOT-23 N-channel MOSFET:

* **Source:** tied to GND.
* **Drain:** connects to the shared bank colour rail (red, green, or blue cathode return).
* **Gate:** driven by U_LED_B1 or U_LED_B2 GPIO output via 1kΩ gate resistor.

Each LED uses three dedicated series resistors: one in each red, green, and blue cathode path.
This allows the three dice to be balanced independently under nominal 5V operation.

When the GPIO output is HIGH, the transistor turns ON, sinking the selected colour rail to GND and
illuminating any LEDs in that bank whose anode outputs are HIGH. GPIO LOW = transistor OFF = colour
rail disabled.

---

## 6. CFG_APPLY Button

SW_CFG_APPLY is a board-mounted momentary tactile switch (SPST, active-low) connected to
U_EXP_SW_IN GPB[7]. The switch itself does not need to be panel-mount; the enclosure may use a
simple plunger or cap to mechanically actuate the switch through the panel opening.

* **Pull-up:** 10kΩ to 3V3_ENIG (R_CA1) — idle state = logic HIGH.
* **Debounce:** 100nF X7R 0402 capacitor to GND (C_CA1; RC τ = 1ms).
* **Operation:** CM5 enigma daemon polls GPB[7] during its main loop. On detecting LOW (button
  pressed, after debounce), the daemon:
  1. Reads U_EXP_SW_IN (full 16-bit state).
  2. Evaluates bank enables for Bank 1 and Bank 2.
  3. Writes final configuration to U_EXP4 GPA[0:3] and GPB[0:5] on the Stator Board.
  4. Pulses STATOR_CFG_RDY (U_EXP4 GPA[4]) LOW then HIGH to trigger CPLD re-latch.
  5. Updates U_LED_B1 and U_LED_B2 outputs to reflect the new configuration state.

This button provides operator-initiated explicit configuration commit without relying solely on
automatic polling intervals.

---

## 7. Interconnects

### J_I2C — I²C Connector to Stator Board

| Pin | Signal | Notes |
| :--- | :--- | :--- |
| 1 | 3V3_ENIG | Power from Stator; powers Settings Board logic (MCP23017 ICs) |
| 2 | 5V_MAIN | Indicator power supply from Stator; sourced from the Controller `J2A` dock; powers LED anodes |
| 3 | GND | Logic ground return only; no local GND_CHASSIS bond on Settings Board |
| 4 | SDA | I²C data; shared Stator I²C-1 bus |
| 5 | SCL | I²C clock; shared Stator I²C-1 bus |
| 6 | GND | LED cathode ground return; high-current return path |

**Connector:** JST B6B-PH-K-S(LF)(SN) — 6-pin JST PH 2.0mm THT
(Mouser: 306-B6B-PH-K-SLFSN, DigiKey: 455-1708-ND, JLCPCB: C131342)

**Cable:** 6-wire harness (100mm recommended); matching JST PHR-6 crimp housing on both ends. Use 28AWG for pins 2 and 6 (power path) and 30AWG for pins 1, 3, 4, 5 (logic/signals).

**Mating connector on Stator:** J_CFG — same JST PH 2.0mm 6-pin part.

**Why 2× GND pins?**

* Pin 3 (GND): Low-current logic return for MCP23017s (~80mA total)
* Pin 6 (GND): High-current LED return (up to 240mA max, ~120mA typical)
* Separating logic and power grounds reduces noise coupling into I²C signals

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
| C_CA1 | CFG_APPLY debounce capacitor | 100nF X7R 50V | 0402 | 187-CL05B104KB5NNNC | 1276-CL05B104KB5NNNCCT-ND | C960916 |
| C_U_EXP_SW_IN | VCC decoupling cap for U_EXP_SW_IN (MCP23017 @ 0x23) | 100nF X7R 50V | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 |
| C_U_LED_B1 | VCC decoupling cap for U_LED_B1 (MCP23017 @ 0x24) | 100nF X7R 50V | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 |
| C_U_LED_B2 | VCC decoupling cap for U_LED_B2 (MCP23017 @ 0x25) | 100nF X7R 50V | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 |
| J_I2C | I²C harness connector to Stator J_CFG | JST B6B-PH-K-S(LF)(SN) — 6-pin JST PH 2.0mm | THT | 306-B6B-PH-K-SLFSN | 455-1708-ND | C131342 |
| LED_B1_EN, LED_B1[0:3] | Bank 1 discrete RGB indicator LEDs (×5) | Kingbright WP154A4SEJ3VBDZGW/CA — 5mm common-anode RGB THT LED | THT 5mm LED | 604-WP154A43VBDZGWCA | 754-2029-ND | C7151795 |
| LED_B2_EN, LED_B2[0:5] | Bank 2 discrete RGB indicator LEDs (×7) | Kingbright WP154A4SEJ3VBDZGW/CA — same part as Bank 1 | THT 5mm LED | 604-WP154A43VBDZGWCA | 754-2029-ND | C7151795 |
| Q_BNK1_R | Bank 1 red colour-rail sink MOSFET | BSS138 | SOT-23 | 512-BSS138 | BSS138CT-ND | C52895 |
| Q_BNK1_G | Bank 1 green colour-rail sink MOSFET | BSS138 | SOT-23 | 512-BSS138 | BSS138CT-ND | C52895 |
| Q_BNK1_B | Bank 1 blue colour-rail sink MOSFET | BSS138 | SOT-23 | 512-BSS138 | BSS138CT-ND | C52895 |
| Q_BNK2_R | Bank 2 red colour-rail sink MOSFET | BSS138 | SOT-23 | 512-BSS138 | BSS138CT-ND | C52895 |
| Q_BNK2_G | Bank 2 green colour-rail sink MOSFET | BSS138 | SOT-23 | 512-BSS138 | BSS138CT-ND | C52895 |
| Q_BNK2_B | Bank 2 blue colour-rail sink MOSFET | BSS138 | SOT-23 | 512-BSS138 | BSS138CT-ND | C52895 |
| R_CA1 | CFG_APPLY pull-up resistor | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KHCT-ND | C191124 |
| R_SW1–R_SW5 | Bank 1 switch input pull-downs (×5: SW_B1_EN + SW_B1[0:3]) | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KHCT-ND | C191124 |
| R_SW6–R_SW12 | Bank 2 switch input pull-downs (×7: SW_B2_EN + SW_B2[0:5]) | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KHCT-ND | C191124 |
| R_LED_R1–R_LED_R12 | Per-switch red LED series resistors (×12) | 150Ω (1%) — 5V operation, 20mA nominal | 0603 | 667-ERJ-3EKF1500V | P150HCT-ND | C400650 |
| R_LED_G1–R_LED_G12 | Per-switch green LED series resistors (×12) | 100Ω (1%) — 5V operation, 20mA nominal | 0603 | 667-ERJ-3EKF1000V | P100HCT-ND | C193336 |
| R_LED_B1–R_LED_B12 | Per-switch blue LED series resistors (×12) | 100Ω (1%) — 5V operation, 20mA nominal | 0603 | 667-ERJ-3EKF1000V | P100HCT-ND | C193336 |
| R_GATE1–R_GATE6 | MOSFET gate resistors (×6, one per transistor) | 1kΩ (1%) | 0402 | 667-ERJ-2RKF1001X | P1.00KLCT-ND | C242161 |
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
| SW_B2[5] | Bank 2 reflector config bit 5 toggle switch | E-Switch 200MSP1T2B4M2QE — same part as SW_B1_EN | Panel-mount THT toggle | 612-200MSP1T2B4M2QE | EG5525-ND | C5491263 |
| SW_CFG_APPLY | CFG_APPLY momentary pushbutton | Omron B3F-1070 — SPST NO through-hole tactile switch; board-mounted and mechanically actuated through enclosure | THT tactile | 653-B3F-1070 | SW406-ND | C726011 |
| U_EXP_SW_IN | MCP23017 I²C GPIO Expander (switch input reader) | MCP23017T-E/SO @ 0x23 | SOIC-28 | 579-MCP23017T-E/SO | MCP23017T-E/SOCT-ND | C47023 |
| U_LED_B1 | MCP23017 I²C GPIO Expander (Bank 1 LED controller) | MCP23017T-E/SO @ 0x24 | SOIC-28 | 579-MCP23017T-E/SO | MCP23017T-E/SOCT-ND | C47023 |
| U_LED_B2 | MCP23017 I²C GPIO Expander (Bank 2 LED controller) | MCP23017T-E/SO @ 0x25 | SOIC-28 | 579-MCP23017T-E/SO | MCP23017T-E/SOCT-ND | C47023 |

---

## 10. Power Budget

### 3V3_ENIG (Logic Rail)

| Component | Typical (mA) | Max (mA) | Notes |
| :--- | :---: | :---: | :--- |
| U_EXP_SW_IN (MCP23017 @ 0x23) | 25 | 50 | Switch input reader; 16 GPIO inputs |
| U_LED_B1 (MCP23017 @ 0x24) | 25 | 50 | Bank 1 LED controller; low-side MOSFET drivers |
| U_LED_B2 (MCP23017 @ 0x25) | 25 | 50 | Bank 2 LED controller; low-side MOSFET drivers |
| **Total 3V3_ENIG** | **75 mA** | **150 mA** | Well within Stator J_CFG capacity |

### 5V_MAIN (Indicator Rail Allocation)

| Load | Typical (mA) | Max (mA) | Notes |
| :--- | :---: | :---: | :--- |
| Bank 1 LEDs (5× @ 20mA) | 60 | 100 | Typical assumes ~12mA per LED average; max = 5 × 20mA = 100mA with one active colour rail |
| Bank 2 LEDs (7× @ 20mA) | 84 | 140 | Typical assumes ~12mA per LED average; max = 7 × 20mA = 140mA with one active colour rail |
| **Total indicator rail** | **144 mA** | **240 mA** | Definitive max = 100mA + 140mA; one active colour per bank, all 12 LEDs illuminated |

**Controller↔Stator 5V_MAIN Allocation:**

* Settings Board: 240mA max (LED load)
* Stator J_SERVO: 500mA max (servo motor)
* Combined branch load: **740mA max**
* The active Molex hybrid Stator dock remains comfortably above this branch load; the grouped `5V_MAIN`
  path is no longer constrained by the retired 40-pin Samtec contact-count limit.

---

## 11. Component Count Summary

| Category | Quantity | Notes |
| :--- | :---: | :--- |
| **Toggle Switches** | 12 | E-Switch 200MSP1T2B4M2QE — SPDT latching panel-mount |
| **RGB LEDs** | 12 | Kingbright WP154A4SEJ3VBDZGW/CA — 5mm common-anode THT |
| **MCP23017 I²C Expanders** | 3 | U_EXP_SW_IN, U_LED_B1, U_LED_B2 |
| **BSS138 MOSFETs** | 6 | Q_BNK1_R/G/B, Q_BNK2_R/G/B — low-side color-rail switches |
| **0603 LED path resistors** | 36 | 12× red (150Ω), 12× green (100Ω), 12× blue (100Ω) |
| **0603 Resistors (switch pull-down)** | 12 | 10kΩ pull-downs on all switch inputs |
| **0402 Resistors (gate)** | 6 | 1kΩ MOSFET gate resistors |
| **0603 Resistors (misc)** | 1 | R_CA1: 10kΩ CFG_APPLY pull-up |
| **0402 Capacitors (decoupling)** | 3 | 100nF X7R for 3× MCP23017s |
| **0402 Capacitors (debounce)** | 1 | C_CA1: 100nF X7R CFG_APPLY debounce |
| **JST PH Connectors** | 1 | J_I2C: 6-pin B6B-PH-K-S(LF)(SN) to Stator |
| **Pushbutton Switch** | 1 | SW_CFG_APPLY — Omron B3F-1070 SPST NO through-hole tactile switch |

**Total unique part numbers:** ~15  
**Total component count:** ~93

---

## 12. Design Notes

### LED Control Architecture

The Settings Board uses a **shared color-rail topology** to minimize MOSFET count while preserving
full RGB control under CM5 firmware:

* Each LED has an **individual anode** controlled by U_LED_B1 or U_LED_B2 GPIO
* All LEDs in a **bank share 3 cathode rails** (red, green, blue)
* **6× BSS138 MOSFETs** (3 per bank) switch each active colour rail to GND
* CM5 firmware selects the active colour per bank according to mode/state

This design uses only 6 MOSFETs for 12 RGB indicators instead of a per-LED transistor scheme.

### 5V Power Routing

Indicator power is sourced from the Controller Board's 5V_MAIN rail (TPS259804 eFuse output) and
routed from the Controller through the hybrid Stator dock and the Stator `J_CFG` harness.
The Stator Board acts as a **power pass-through hub**, forwarding 5V_MAIN to:

* J_CFG pin 2 → Settings Board indicator rail (240mA max)
* J_SERVO pin 1 → Servo motor 5V_MAIN (500mA max)

This solves two design issues in one: LED brightness and the previously open J_SERVO power source.

### I²C Address Selection

The Settings Board uses the contiguous `0x23`-`0x25` block immediately after the Stator's
`0x20`-`0x22` expanders. This keeps the shared Settings/Stator GPIO devices grouped together on the
bus and avoids conflicts with the INA219 (`0x40`) and PCA9685 (`0x60`) devices.
