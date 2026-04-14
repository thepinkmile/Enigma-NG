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
12 illuminated RGB rocker switches, mounted through the right side of the enclosure top face near
the rotors. A momentary CFG_APPLY pushbutton triggers CPLD configuration re-latch via the CM5
firmware.

The Settings Board communicates with the Stator Board exclusively via a 4-wire I²C ribbon cable
(J_I2C → Stator J_CFG), sharing the Stator I²C-1 bus. It hosts two MCP23017 GPIO expanders:

* **U_EXP_SW_IN (@ 0x26):** Reads all 12 switch states and the CFG_APPLY momentary button.
* **U_EXP_LED (@ 0x27):** Drives per-bit LED cathodes and per-bank colour-rail NPN transistors.

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
| FR-SBD-01 | Provide 12 user-accessible illuminated RGB rocker switches for hardware configuration without opening the enclosure | 5 switches for Bank 1 (plugboard routing); 7 for Bank 2 (reflector mapping); panel-mount through enclosure top face | §3 Switch Bank Descriptions; §4 I²C Devices |
| FR-SBD-02 | Allow CM5 firmware to override hardware switch settings on a per-bank basis | Bank enable switch (SW_B1_EN / SW_B2_EN): HIGH = switch-defined active; LOW = CM5-defined override | §5 LED Control Logic; Stator/Design_Spec.md FR-STA-08/09 |
| FR-SBD-03 | Provide visual feedback via RGB LED illumination showing configuration source and active bit state | Green = switch-defined active; Red = CM5-defined override; per-bank shared colour rail + per-bit individual LED cathode control | §5 LED Control Logic |
| FR-SBD-04 | Provide a momentary CFG_APPLY pushbutton that triggers CPLD configuration re-latch | CM5 daemon polls U_EXP_SW_IN GPB[7]; active-low; 10kΩ pull-up + 100nF X7R 0402 debounce cap | §6 CFG_APPLY Button |
| FR-SBD-05 | Connect to the Stator Board via a 4-wire I²C ribbon cable (3V3_ENIG, GND, SDA, SCL) | J_I2C = 4-pin JST PH 2.0mm connector; shares Stator I²C-1 bus | §7 Interconnects; BOM J_I2C |

#### Design Requirements

| ID | Design Requirement | Specification | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| DR-SBD-01 | PCB stackup | 4-layer, 2oz finished copper (JLCPCB JLC04161H-7628) | §8 PCB Fabrication |
| DR-SBD-02 | Switch type | 12× panel-mount illuminated RGB rocker switches (SPDT, integrated R/G LED); MPN TBD | §3 Switch Bank Descriptions; BOM SW_B1_EN, SW_B1[0:3], SW_B2_EN, SW_B2[0:5] |
| DR-SBD-03 | Switch input expander | U_EXP_SW_IN = MCP23017T-E/SO @ 0x26; SOIC-28; A2=HIGH, A1=HIGH, A0=LOW | §4 I²C Devices — U_EXP_SW_IN; BOM U_EXP_SW_IN |
| DR-SBD-04 | LED output expander | U_EXP_LED = MCP23017T-E/SO @ 0x27; SOIC-28; A2=HIGH, A1=HIGH, A0=HIGH | §4 I²C Devices — U_EXP_LED; BOM U_EXP_LED |
| DR-SBD-05 | LED colour-rail transistors | 4× MMBT3906 SOT-23 PNP (Q_BNK1_G, Q_BNK1_R, Q_BNK2_G, Q_BNK2_R); base driven from U_EXP_LED GPIO via 1kΩ base-limiting resistor; GPIO LOW = transistor ON (PNP sourcing topology) | §5 LED Control Logic; BOM Q_BNK1_G, Q_BNK1_R, Q_BNK2_G, Q_BNK2_R |
| DR-SBD-06 | CFG_APPLY button | SW_CFG_APPLY = SPST momentary pushbutton, active-low; 10kΩ pull-up to 3V3_ENIG (R_CA1) + 100nF X7R 0402 debounce cap to GND (C_CA1; RC τ = 1ms); connected to U_EXP_SW_IN GPB[7] | §6 CFG_APPLY Button; BOM SW_CFG_APPLY, R_CA1, C_CA1 |
| DR-SBD-07 | I²C connector | J_I2C = 4-pin JST PH 2.0mm B4B-PH-K-S(LF)(SN); pins: 3V3_ENIG, GND, SDA, SCL; ribbon cable to Stator J_CFG | §7 Interconnects; BOM J_I2C |
| DR-SBD-08 | Switch input pull-downs | 12× 10kΩ 0603 pull-down resistors on all switch signal inputs to U_EXP_SW_IN (GPA[0:4], GPB[0:6]); HIGH = switch-defined active when switch closed | §4 I²C Devices — U_EXP_SW_IN; BOM R_SW1–R_SW12 |

---

## 2. Core Features

* **12 Panel-Mount RGB Rocker Switches:** SPDT illuminated switches with integrated R/G LED,
  mounted through the enclosure top face. Bank 1 (5 switches): plugboard routing config.
  Bank 2 (7 switches): reflector map config.
* **MCP23017 Dual-Expander Architecture:** U_EXP_SW_IN reads all switch states; U_EXP_LED drives
  all LED illumination. Separate expanders prevent LED drive state from interfering with switch
  read-back.
* **Per-Bank Enable Control:** Each bank has a dedicated enable switch (SW_B1_EN, SW_B2_EN). When
  HIGH, the physical switch positions define the configuration. When LOW, the CM5 firmware defines
  the configuration.
* **RGB LED Feedback:** Green = switch-defined active; Red = CM5-defined override. Per-bit cathode
  control illuminates only set bits. Shared per-bank colour rail simplifies wiring (4 NPN
  transistors total).
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
corresponding switch is open. On the Stator, R16–R25 provide the corresponding pull-downs on the
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

Pull-down resistors R20–R25 on the Stator CPLD input pins hold each input at logic-0 when U_EXP4
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

### U_EXP_LED — MCP23017T-E/SO @ 0x27

Drives per-bit LED cathodes and per-bank colour-rail NPN transistors.

**Address:** 0x27 — A2=HIGH, A1=HIGH, A0=HIGH → 0x20 | 0b111 = 0x27

| Port | Pin | Signal | Direction | Description |
| :--- | :--- | :--- | :--- | :--- |
| GPA | [0] | SW_B1_CAT[0] | Output | Bank 1 LED cathode for SW_B1_EN; LOW = LED on |
| GPA | [1] | SW_B1_CAT[1] | Output | Bank 1 LED cathode for SW_B1[0]; LOW = LED on |
| GPA | [2] | SW_B1_CAT[2] | Output | Bank 1 LED cathode for SW_B1[1]; LOW = LED on |
| GPA | [3] | SW_B1_CAT[3] | Output | Bank 1 LED cathode for SW_B1[2]; LOW = LED on |
| GPA | [4] | SW_B1_CAT[4] | Output | Bank 1 LED cathode for SW_B1[3]; LOW = LED on |
| GPA | [5] | BNK1_G | Output | Bank 1 green colour-rail; drives base of Q_BNK1_G (NPN); HIGH = green anode active |
| GPA | [6] | BNK1_R | Output | Bank 1 red colour-rail; drives base of Q_BNK1_R (NPN); HIGH = red anode active |
| GPA | [7] | BNK2_G | Output | Bank 2 green colour-rail; drives base of Q_BNK2_G (NPN); HIGH = green anode active |
| GPB | [0] | SW_B2_CAT[0] | Output | Bank 2 LED cathode for SW_B2_EN; LOW = LED on |
| GPB | [1] | SW_B2_CAT[1] | Output | Bank 2 LED cathode for SW_B2[0]; LOW = LED on |
| GPB | [2] | SW_B2_CAT[2] | Output | Bank 2 LED cathode for SW_B2[1]; LOW = LED on |
| GPB | [3] | SW_B2_CAT[3] | Output | Bank 2 LED cathode for SW_B2[2]; LOW = LED on |
| GPB | [4] | SW_B2_CAT[4] | Output | Bank 2 LED cathode for SW_B2[3]; LOW = LED on |
| GPB | [5] | SW_B2_CAT[5] | Output | Bank 2 LED cathode for SW_B2[4]; LOW = LED on |
| GPB | [6] | SW_B2_CAT[6] | Output | Bank 2 LED cathode for SW_B2[5]; LOW = LED on |
| GPB | [7] | BNK2_R | Output | Bank 2 red colour-rail; drives base of Q_BNK2_R (NPN); HIGH = red anode active |

> Individual cathode LOW drives current through the switch LED to the shared colour-rail anode
> (via NPN transistor). Only the active colour-rail transistor is enabled at any time; switching
> the colour rail changes the illumination colour for all lit LEDs in that bank simultaneously.

---

## 5. LED Control Logic

### Colour Scheme

| Bank Enable State | Colour Rail Active | Meaning |
| :--- | :--- | :--- |
| HIGH (switch-defined active) | Green (BNKx_G transistor ON) | Configuration source = physical switches |
| LOW (CM5-defined override) | Red (BNKx_R transistor ON) | Configuration source = CM5 firmware |

### Per-Bit Illumination

* Each switch in a bank has an individual LED cathode output (SW_B1_CAT[0:4], SW_B2_CAT[0:6]).
* CM5 daemon sets each cathode LOW to illuminate that bit's LED when the corresponding bit in the
  active configuration is set (= 1).
* Unset bits (= 0) have their cathode held HIGH (LED off); only active configuration bits are
  illuminated.

### Bank Enable Switch LED

The bank enable switch (SW_B1_EN / SW_B2_EN) has its own cathode pin (SW_B1_CAT[0] /
SW_B2_CAT[0]) and is illuminated whenever the bank enable is active, providing a visual on/off
indicator for the entire bank.

### PNP Transistor Colour-Rail Circuit

Each colour rail (BNK1_G, BNK1_R, BNK2_G, BNK2_R) is driven by a MMBT3906 SOT-23 PNP transistor:

* **Emitter:** tied to 3V3_ENIG.
* **Collector:** connects to the shared LED anode rail via current-limiting resistor (value TBD —
  depends on switch LED forward voltage and current specification).
* **Base:** driven by U_EXP_LED GPIO output via 1kΩ base-limiting resistor.

When the GPIO output is LOW, the transistor turns ON, sourcing current from 3V3_ENIG through the
emitter to collector and illuminating all LEDs with LOW cathodes in that bank. GPIO HIGH = transistor
OFF = colour rail disabled.

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
| Q_BNK1_G | Bank 1 green colour-rail PNP transistor | MMBT3906 | SOT-23 | 512-MMBT3906 | MMBT3906CT-ND | C20527 |
| Q_BNK1_R | Bank 1 red colour-rail PNP transistor | MMBT3906 | SOT-23 | 512-MMBT3906 | MMBT3906CT-ND | C20527 |
| Q_BNK2_G | Bank 2 green colour-rail PNP transistor | MMBT3906 | SOT-23 | 512-MMBT3906 | MMBT3906CT-ND | C20527 |
| Q_BNK2_R | Bank 2 red colour-rail PNP transistor | MMBT3906 | SOT-23 | 512-MMBT3906 | MMBT3906CT-ND | C20527 |
| R_CA1 | CFG_APPLY pull-up resistor | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R_SW1–R_SW5 | Bank 1 switch input pull-downs (×5: SW_B1_EN + SW_B1[0:3]) | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R_SW6–R_SW12 | Bank 2 switch input pull-downs (×7: SW_B2_EN + SW_B2[0:5]) | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R_LED_ANODE | LED anode current-limiting resistors (×4, one per colour rail) | TBD Ω (depends on switch LED specs) | 0603 | TBD | TBD | TBD |
| R_BASE1–R_BASE4 | PNP base-limiting resistors (×4, one per transistor) | 1kΩ (1%) | 0402 | 667-ERJ-2RKF1002X | P1.00KLBCT-ND | C25705 |
| SW_B1_EN | Bank 1 enable rocker switch | Marquardt 1800 series SPDT latching rocker with RGB LED — MPN TBD (same variant as PM SW1) | Panel-mount | TBD | TBD | — |
| SW_B1[0] | Bank 1 routing config bit 0 rocker switch | Marquardt 1800 series SPDT latching rocker with RGB LED — MPN TBD | Panel-mount | TBD | TBD | — |
| SW_B1[1] | Bank 1 routing config bit 1 rocker switch | Marquardt 1800 series SPDT latching rocker with RGB LED — MPN TBD | Panel-mount | TBD | TBD | — |
| SW_B1[2] | Bank 1 routing config bit 2 rocker switch | Marquardt 1800 series SPDT latching rocker with RGB LED — MPN TBD | Panel-mount | TBD | TBD | — |
| SW_B1[3] | Bank 1 routing config bit 3 rocker switch | Marquardt 1800 series SPDT latching rocker with RGB LED — MPN TBD | Panel-mount | TBD | TBD | — |
| SW_B2_EN | Bank 2 enable rocker switch | Marquardt 1800 series SPDT latching rocker with RGB LED — MPN TBD | Panel-mount | TBD | TBD | — |
| SW_B2[0] | Bank 2 reflector config bit 0 rocker switch | Marquardt 1800 series SPDT latching rocker with RGB LED — MPN TBD | Panel-mount | TBD | TBD | — |
| SW_B2[1] | Bank 2 reflector config bit 1 rocker switch | Marquardt 1800 series SPDT latching rocker with RGB LED — MPN TBD | Panel-mount | TBD | TBD | — |
| SW_B2[2] | Bank 2 reflector config bit 2 rocker switch | Marquardt 1800 series SPDT latching rocker with RGB LED — MPN TBD | Panel-mount | TBD | TBD | — |
| SW_B2[3] | Bank 2 reflector config bit 3 rocker switch | Marquardt 1800 series SPDT latching rocker with RGB LED — MPN TBD | Panel-mount | TBD | TBD | — |
| SW_B2[4] | Bank 2 reflector config bit 4 rocker switch | Marquardt 1800 series SPDT latching rocker with RGB LED — MPN TBD | Panel-mount | TBD | TBD | — |
| SW_B2[5] | Bank 2 reflector config bit 5 rocker switch (internal reflector enable) | Marquardt 1800 series SPDT latching rocker with RGB LED — MPN TBD | Panel-mount | TBD | TBD | — |
| SW_CFG_APPLY | CFG_APPLY momentary pushbutton | SPST NO momentary, panel-mount (MPN TBD) | Panel-mount | TBD | TBD | — |
| U_EXP_SW_IN | MCP23017 I²C GPIO Expander (switch input reader) | MCP23017T-E/SO @ 0x26 | SOIC-28 | 579-MCP23017T-E/SO | MCP23017T-E/SOCT-ND | C47023 |
| U_EXP_LED | MCP23017 I²C GPIO Expander (LED cathode + colour rail driver) | MCP23017T-E/SO @ 0x27 | SOIC-28 | 579-MCP23017T-E/SO | MCP23017T-E/SOCT-ND | C47023 |
