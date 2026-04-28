# Settings Board (V1.0) Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-26

---

## 1. Overview

The Settings Board is a panel-mount PCB providing user-accessible hardware configuration controls
for the Enigma-NG system. It replaces the DIP switches previously located on the Stator Board with
10 sub-miniature SPDT toggle switches plus 12 discrete RGB status LEDs, mounted through the right
side of the enclosure top face near the rotors. A momentary active-low `CFG_APPLY_N` pushbutton
captures the user's configuration intent; the CM5 firmware then mirrors that request onto the
Stator-side apply/reset path.

The Settings Board communicates with the Stator Board exclusively via a 6-wire I²C harness
(J1 → Stator J13), sharing the Stator I²C-1 bus. It hosts three MCP23017 GPIO expanders:

* **U1 (@ 0x23):** Reads the 10 toggle-switch states and the `CFG_APPLY_N` momentary button.
* **U2 (@ 0x24):** Drives Bank 1 LED anodes (1 source-status LED + 4 config LEDs) and RGB bank-rail low-side switches.
* **U3 (@ 0x25):** Drives Bank 2 LED anodes (1 source-status LED + 6 config LEDs) and RGB bank-rail low-side switches.

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
| FR-SBD-01 | Provide 10 user-accessible toggle switches with matching RGB status LEDs for hardware configuration without opening the enclosure | 4 toggles for routing config, 6 for reflector-map config, plus 2 RGB source-status LEDs; panel-mount through enclosure top face | §3 Configuration Bank Descriptions; §4 I²C Devices |
| FR-SBD-02 | Allow CM5 firmware / GUI presets to override the user-intent configuration on a per-bank basis | CM5 decides authority in software, drives the final applied config on the Stator, and reflects source state back to the Settings indicators via `CFG_ROUTE_CM5_ACTIVE` / `CFG_REFMAP_CM5_ACTIVE` | §5 LED Control Logic; Stator/Design_Spec.md FR-STA-08/09 |
| FR-SBD-03 | Provide visual feedback via RGB LED illumination showing configuration source and active bit state | Green = user-intent forwarded; Red = CM5-defined override active; per-bank shared colour rails + per-bit individual LED anode drive with per-colour cathode-return resistors | §5 LED Control Logic |
| FR-SBD-04 | Provide a momentary `CFG_APPLY_N` pushbutton that requests Stator CPLD configuration reload | CM5 daemon polls U1 GPB[7]; active-low; 10kΩ pull-up + 100nF X7R 0402 debounce cap. A board-mounted tactile switch actuated through the enclosure is acceptable; the switch itself need not be panel-mount. | §6 `CFG_APPLY_N` Button |
| FR-SBD-05 | Connect to the Stator Board via a 6-wire I²C harness (`3V3_ENIG`, `5V_MAIN`, 2× `GND`, `SDA`, `SCL`) | J1 = 6-pin JST PH 2.0mm connector; shares Stator I²C-1 bus; `5V_MAIN` powers the indicator LEDs | §7 Interconnects; BOM J1 |

#### Design Requirements

| ID | Design Requirement | Specification | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| DR-SBD-01 | PCB stackup | 4-layer, 2oz finished copper (JLCPCB JLC04161H-7628) | §8 PCB Fabrication |
| DR-SBD-02 | Switch + indicator type | 10× E-Switch 200MSP1T2B4M2QE panel-mount SPDT latching toggle switches plus 12× Kingbright WP154A4SEJ3VBDZGW/CA common-anode RGB through-hole LEDs; 10 LEDs mirror config bits and 2 LEDs indicate CM5-vs-user authority | §3 Configuration Bank Descriptions; BOM SW1-SW10, D1-D12 |
| DR-SBD-03 | Switch input expander | U1 = MCP23017T-E/SO @ 0x23; SOIC-28; contiguous after the Stator expander block | §4 I²C Devices — U1; BOM U1 |
| DR-SBD-04 | LED control expanders | U2 = MCP23017T-E/SO @ 0x24 (Bank 1); U3 = MCP23017T-E/SO @ 0x25 (Bank 2); SOIC-28; per-indicator anodes plus shared RGB bank rails | §4 I²C Devices — U2, U3; §5 LED Control Logic; BOM U2, U3 |
| DR-SBD-05 | LED colour-rail transistors | 6× BSS138 SOT-23 N-channel MOSFETs (`Q1-Q6`); gate driven via 1kΩ resistor; GPIO HIGH = transistor ON | §5 LED Control Logic; BOM Q1-Q6 |
| DR-SBD-06 | LED power supply | `5V_MAIN` from the Stator via J1 pin 2; full RGB operation at 5V uses 150Ω red and 100Ω green/blue series resistors; LED anodes connect to `5V_MAIN` via per-anode PMOS high-side switches (Q19–Q30) — see DR-SBD-10 | §7 Interconnects — J1; §5 LED Control Logic; BOM R18-R53, Q7-Q30, R54-R77 |
| DR-SBD-07 | `CFG_APPLY_N` button | SW11 = Omron B3F-1070 or equivalent SPST NO through-hole tactile switch, active-low; mounted on the Settings Board and actuated through the enclosure by a mechanical plunger/cap; 10kΩ pull-up to 3V3_ENIG + 100nF debounce cap; U1 GPB[7] | §6 `CFG_APPLY_N` Button; BOM SW11, R11, C4 |
| DR-SBD-08 | I²C connector | J1 = 6-pin JST PH 2.0mm B6B-PH-K-S(LF)(SN); pins: `3V3_ENIG`, `5V_MAIN`, `GND`, `SDA`, `SCL`, `GND`; harness to Stator J13 | §7 Interconnects; BOM J1 |
| DR-SBD-09 | Switch input pull-downs | 10× 10kΩ 0603 pull-down resistors on all toggle-switch inputs to U1 (GPA[3:0], GPB[5:0]); HIGH when closed | §4 I²C Devices — U1; BOM R1-R10 |
| DR-SBD-10 | Per-anode LED high-side switch | 12× two-stage per-anode high-side switch: MCP23017 GPIO → 1 kΩ gate resistor (R54–R65) → BSS138 NMOS pre-driver (Q7–Q18); BSS138 drain pulls PMOS gate low; 47 kΩ pull-up (R66–R77) from PMOS gate to `5V_MAIN`; PMOS source at `5V_MAIN`, drain to LED anode; GPIO HIGH → LED ON (non-inverted logic); this topology isolates the MCP23017 3.3 V GPIO from direct-driving 5 V LED anodes | §5 LED Control Logic; BOM Q7-Q30, R54-R77 |

---

## 2. Core Features

* **10 Panel-Mount Toggle Switches + 12 RGB LEDs:** E-Switch 200 series SPDT toggles provide the
  user-intent configuration inputs; one discrete Kingbright common-anode RGB LED is mounted beside
  each config position, and one additional RGB source-status LED is provided per bank. Bank 1
  therefore has 4 config toggles + 5 LEDs total; Bank 2 has 6 config toggles + 7 LEDs total.
* **Three-Expander Architecture:** U1 reads all switch states, while U2 and U3
  independently drive the two indicator banks. Separate expanders prevent LED drive state from
  interfering with switch read-back and keep the Settings address block contiguous after the Stator.
* **Per-Bank CM5-Active Status:** Each bank has a CM5-owned logical state
  (`CFG_ROUTE_CM5_ACTIVE`, `CFG_REFMAP_CM5_ACTIVE`) reflected by the bank's source-status LED and
  shared colour rail. LOW = the CM5 is forwarding user-intent config. HIGH = the CM5 is applying a
  GUI-selected or automated override.
* **RGB LED Feedback:** Green = switch-defined active; Red = CM5-defined override. Blue remains
  available for CM5-controlled status, boot, or fault states. Per-bit anode control illuminates
  only set bits. Shared per-bank RGB rails simplify wiring (6 low-side sink MOSFETs total).
* **`CFG_APPLY_N` Button:** Momentary pushbutton requests a Stator-only configuration reload via the
  CM5 daemon. CM5 reads the user-intent switch state, writes the final config to U8 on the
  Stator, and pulses the Stator-side `CFG_APPLY_N` output low.
* **I²C-Only Interface:** 6-wire harness to Stator (`3V3_ENIG`, `5V_MAIN`, `GND`, `SDA`, `SCL`, `GND`) — no parallel signal wiring.

### GND_CHASSIS Single-Point Bond

Per `design/Standards/Global_Routing_Spec.md §5`, the Settings Board implements a local
`GND_CHASSIS` net tied to its mounting holes and any panel-contact mechanical features, but it does
**not** implement a local GND-to-GND_CHASSIS bond. The system's only galvanic GND ↔ GND_CHASSIS
bond is defined on the Power Module at the common power-entry point immediately before the eFuse.
J1 pin 3 is therefore **logic GND return only**, and must not be repurposed as a local
chassis-bond point.

---

## 3. Configuration Bank Descriptions

### Bank 1 — Plugboard Routing (`CFG_ROUTE[3:0]` + `CFG_ROUTE_CM5_ACTIVE`)

Bank 1 provides a 4-bit user-intent image of the logical `CFG_ROUTE[3:0]` bus, selecting the active
routing case from 16 configurations synthesised into the Stator CPLD fabric. `CFG_ROUTE[1:0]`
encode **Plugboard Pass 1** (`J6/J7`) insertion position; `CFG_ROUTE[3:2]` encode **Plugboard Pass
2** (`J8/J9`) insertion position.

The CM5 daemon decides whether the applied `CFG_ROUTE[3:0]` value is the forwarded Settings Board
user-intent image or a CM5-defined override. `CFG_ROUTE_CM5_ACTIVE` is the CM5-owned status state
used to colour the Bank 1 indicators: LOW = user-intent forwarded (green), HIGH = CM5-defined
override active (red).

Pull-down resistors (10kΩ, one per switch signal) hold each input at logic-0 when the
corresponding switch is open. On the Stator, R16–R19 provide the corresponding pull-downs on the
logical `CFG_ROUTE[3:0]` CPLD input pins to maintain a safe all-zero default before CM5 initialises
U8.

The final applied `CFG_ROUTE[3:0]` value is driven to the Stator CPLD by U8 GPA[3:0] via I²C.
After CM5 writes the final value, it may assert the Stator-side `CFG_APPLY_N` output low to force a
Stator-only configuration reload.

| `CFG_ROUTE` Index (`CFG_ROUTE[3]:CFG_ROUTE[2]:CFG_ROUTE[1]:CFG_ROUTE[0]`) | Plugboard Pass 1 (`J6/J7`) insertion point | Plugboard Pass 2 (`J8/J9`) insertion point | Historical reference |
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

### Bank 2 — Reflector Mapping (`CFG_REFMAP[5:0]` + `CFG_REFMAP_CM5_ACTIVE`)

Bank 2 provides a 6-bit user-intent image of the logical `CFG_REFMAP[5:0]` bus used by the Stator
CPLD to select the reflector-map index. The physical Reflector board remains mandatory and always
provides the electrical turnaround at the end of the rotor/extension chain.

The CM5 daemon decides whether the applied `CFG_REFMAP[5:0]` value is the forwarded Settings Board
user-intent image or a CM5-defined override. `CFG_REFMAP_CM5_ACTIVE` is the CM5-owned status state
used to colour the Bank 2 indicators: LOW = user-intent forwarded (green), HIGH = CM5-defined
override active (red).

| Bit | Switch | Function |
| :--- | :--- | :--- |
| `CFG_REFMAP[5:0]` | SW5-SW10 | **6-bit map index** (0–63): selects which involutory map to load from CPLD UFM at configuration load; indices 0–20 are currently allocated |

Pull-down resistors R21–R26 on the Stator CPLD `CFG_REFMAP[5:0]` input pins hold each input at
logic-0 when U8 is uninitialised (default map index = 0).

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

All Settings Board I²C devices share the Stator I²C-1 bus via J1 → Stator J13.

### U1 — MCP23017T-E/SO @ 0x23

Reads the 10 toggle-switch states and the active-low `CFG_APPLY_N` momentary button.

**Address:** 0x23 — MCP23017 base 0x20; A2=LOW, A1=HIGH, A0=HIGH → 0x20 | 0b011 = 0x23

| Port | Pin | Signal | Direction | Pull | Description |
| :--- | :--- | :--- | :--- | :--- | :--- |
| GPA | [0] | CFG_ROUTE[0] | Input | 10kΩ pull-down | Routing config bit 0 |
| GPA | [1] | CFG_ROUTE[1] | Input | 10kΩ pull-down | Routing config bit 1 |
| GPA | [2] | CFG_ROUTE[2] | Input | 10kΩ pull-down | Routing config bit 2 |
| GPA | [3] | CFG_ROUTE[3] | Input | 10kΩ pull-down | Routing config bit 3 |
| GPA | [4:7] | — | Input | — | Spare (reserved future use) |
| GPB | [0] | CFG_REFMAP[0] | Input | 10kΩ pull-down | Reflector-map config bit 0 |
| GPB | [1] | CFG_REFMAP[1] | Input | 10kΩ pull-down | Reflector-map config bit 1 |
| GPB | [2] | CFG_REFMAP[2] | Input | 10kΩ pull-down | Reflector-map config bit 2 |
| GPB | [3] | CFG_REFMAP[3] | Input | 10kΩ pull-down | Reflector-map config bit 3 |
| GPB | [4] | CFG_REFMAP[4] | Input | 10kΩ pull-down | Reflector-map config bit 4 |
| GPB | [5] | CFG_REFMAP[5] | Input | 10kΩ pull-down | Reflector-map config bit 5 |
| GPB | [6] | — | Input | — | Spare (reserved future use) |
| GPB | [7] | CFG_APPLY_N | Input | 10kΩ pull-up to 3V3_ENIG | Active-low momentary; 100nF X7R debounce cap to GND |

> All toggle-switch signal inputs (GPA[3:0], GPB[5:0]) use 10kΩ pull-down resistors: open/off switch = logic-0.
> `CFG_APPLY_N` (GPB[7]) uses 10kΩ pull-up: active button press = logic-0.
>
> Each `200MSP1T2B4M2QE` toggle is wired as an SPDT-used-as-SPST input: the centre COM lug goes
> to the named `CFG_*` signal net, the asserted throw goes to `3V3_ENIG`, and the opposite throw is
> left unconnected in Rev A. Panel orientation shall make the lever-up / marked-ON position select
> the `3V3_ENIG` throw so the asserted state always reads logic-1.
>
### U2 — MCP23017T-E/SO @ 0x24

Drives Bank 1 LED high-side switch trigger signals (1 source-status LED + 4 config LEDs) via dedicated
BSS138 NMOS pre-drivers (Q7–Q11), and Bank 1 RGB colour-rail low-side transistor gates (Q1–Q3).

**Address:** 0x24 — MCP23017 base 0x20; A2=HIGH, A1=LOW, A0=LOW → 0x20 | 0b100 = 0x24

| Port | Pin | Signal | Direction | Description |
| :--- | :--- | :--- | :--- | :--- |
| GPA | [0] | LED_B1_SRC_A | Output | Bank 1 source-status LED high-side switch trigger; HIGH drives Q7 gate (BSS138 ON → Q19 PMOS ON → anode at 5V) |
| GPA | [1] | LED_B1_0_A | Output | Bank 1 bit 0 LED high-side switch trigger; HIGH drives Q8 gate (BSS138 ON → Q20 PMOS ON → anode at 5V) |
| GPA | [2] | LED_B1_1_A | Output | Bank 1 bit 1 LED high-side switch trigger; HIGH drives Q9 gate (BSS138 ON → Q21 PMOS ON → anode at 5V) |
| GPA | [3] | LED_B1_2_A | Output | Bank 1 bit 2 LED high-side switch trigger; HIGH drives Q10 gate (BSS138 ON → Q22 PMOS ON → anode at 5V) |
| GPA | [4] | LED_B1_3_A | Output | Bank 1 bit 3 LED high-side switch trigger; HIGH drives Q11 gate (BSS138 ON → Q23 PMOS ON → anode at 5V) |
| GPA | [5] | BNK1_R | Output | Bank 1 red cathode rail; drives gate of Q1; HIGH = red rail active |
| GPA | [6] | BNK1_G | Output | Bank 1 green cathode rail; drives gate of Q2; HIGH = green rail active |
| GPA | [7] | BNK1_B | Output | Bank 1 blue cathode rail; drives gate of Q3; HIGH = blue rail active |
| GPB | [7:0] | — | — | Spare (reserved future use) |

> LED anode signals drive the gates of BSS138 NMOS pre-drivers (Q7–Q11) through 1 kΩ gate resistors
> (R54–R58). Each BSS138 drain pulls down the gate of a PMOS high-side switch (Q19–Q23); 47 kΩ pull-ups
> (R66–R70) hold the PMOS gates HIGH when the BSS138 is OFF, keeping the PMOS OFF and the anode
> floating. GPIO HIGH → BSS138 ON → PMOS gate ≈0 V → PMOS ON → LED anode driven to `5V_MAIN`. Each
> LED's red, green, and blue cathodes return through current-limiting resistors (`R_LED_R` = 150Ω,
> `R_LED_G` = 100Ω, `R_LED_B` = 100Ω) to the shared bank colour rails switched by Q1–Q3. On power-up,
> Hi-Z GPIO defaults leave BSS138 gates floating; behaviour is consistent with Q1–Q6 and shall be
> validated during system-level power-on testing.
>
### U3 — MCP23017T-E/SO @ 0x25

Drives Bank 2 LED high-side switch trigger signals (1 source-status LED + 6 config LEDs) via dedicated
BSS138 NMOS pre-drivers (Q12–Q18), and Bank 2 RGB colour-rail low-side transistor gates (Q4–Q6).

**Address:** 0x25 — MCP23017 base 0x20; A2=HIGH, A1=LOW, A0=HIGH → 0x20 | 0b101 = 0x25

| Port | Pin | Signal | Direction | Description |
| :--- | :--- | :--- | :--- | :--- |
| GPA | [0] | LED_B2_SRC_A | Output | Bank 2 source-status LED high-side switch trigger; HIGH drives Q12 gate (BSS138 ON → Q24 PMOS ON → anode at 5V) |
| GPA | [1] | LED_B2_0_A | Output | Bank 2 bit 0 LED high-side switch trigger; HIGH drives Q13 gate (BSS138 ON → Q25 PMOS ON → anode at 5V) |
| GPA | [2] | LED_B2_1_A | Output | Bank 2 bit 1 LED high-side switch trigger; HIGH drives Q14 gate (BSS138 ON → Q26 PMOS ON → anode at 5V) |
| GPA | [3] | LED_B2_2_A | Output | Bank 2 bit 2 LED high-side switch trigger; HIGH drives Q15 gate (BSS138 ON → Q27 PMOS ON → anode at 5V) |
| GPA | [4] | LED_B2_3_A | Output | Bank 2 bit 3 LED high-side switch trigger; HIGH drives Q16 gate (BSS138 ON → Q28 PMOS ON → anode at 5V) |
| GPA | [5] | LED_B2_4_A | Output | Bank 2 bit 4 LED high-side switch trigger; HIGH drives Q17 gate (BSS138 ON → Q29 PMOS ON → anode at 5V) |
| GPA | [6] | LED_B2_5_A | Output | Bank 2 bit 5 LED high-side switch trigger; HIGH drives Q18 gate (BSS138 ON → Q30 PMOS ON → anode at 5V) |
| GPA | [7] | BNK2_R | Output | Bank 2 red cathode rail; drives gate of Q4; HIGH = red rail active |
| GPB | [0] | BNK2_G | Output | Bank 2 green cathode rail; drives gate of Q5; HIGH = green rail active |
| GPB | [1] | BNK2_B | Output | Bank 2 blue cathode rail; drives gate of Q6; HIGH = blue rail active |
| GPB | [2:7] | — | — | Spare (reserved future use) |

> LED anode signals drive the gates of BSS138 NMOS pre-drivers (Q12–Q18) through 1 kΩ gate resistors
> (R59–R65). Each BSS138 drain pulls down the gate of a PMOS high-side switch (Q24–Q30); 47 kΩ pull-ups
> (R71–R77) hold the PMOS gates HIGH when the BSS138 is OFF. GPIO HIGH → BSS138 ON → PMOS gate ≈0 V →
> PMOS ON → LED anode driven to `5V_MAIN`. Cathodes return through current-limiting resistors to the
> shared Bank 2 colour rails switched by Q4–Q6. On power-up, Hi-Z GPIO defaults leave BSS138 gates
> floating; behaviour is consistent with Q1–Q6 and shall be validated during system-level power-on
> testing.
>

---

## 5. LED Control Logic

### Colour Scheme

Full RGB capability with software-selectable colors per bank:

| CM5_ACTIVE State | Primary Colour | Meaning |
| :--- | :--- | :--- |
| LOW (`CFG_*_CM5_ACTIVE` deasserted) | Green (BNKx_G transistor ON) | Configuration source = Settings Board user intent |
| HIGH (`CFG_*_CM5_ACTIVE` asserted) | Red (BNKx_R transistor ON) | Configuration source = CM5 firmware / GUI override |
| Special modes | Blue (BNKx_B transistor ON) | Future use: status, bootloader, error states |

> Software can select any RGB color by enabling the appropriate color-rail transistor. Only one
> color is active per bank at any time, so the definitive worst-case indicator-rail budget is
> **240mA total**: Bank 1 = 5 LEDs × 20mA = 100mA max, Bank 2 = 7 LEDs × 20mA = 140mA max.
>
### Per-Bit Illumination

* Each bank has one always-on source-status LED anode plus individual config-bit LED anodes
  (U2 drives Bank 1 anodes, U3 drives Bank 2 anodes).
* CM5 daemon sets each anode HIGH to illuminate that bit's LED when the corresponding bit in the
  active configuration is set (= 1) and the correct bank colour rail is enabled.
* Unset bits (= 0) have their anode held LOW (LED off); only active configuration bits are
  illuminated.

### Bank Source-Status LED

The first LED in each bank (`D1` / `D6`) is a source-status indicator rather than a
switch-paired LED. Its anode is driven HIGH whenever the bank is active, while the shared RGB rail
colour communicates whether the applied configuration is user-intent forwarded (green) or
CM5-defined (red).

### Low-Side Colour-Rail Circuit

The six colour-rail sink stages on this board (`BNK1_R/G/B`, `BNK2_R/G/B`) follow the common RGB
sink-stage rule defined in `design/Standards/Global_Routing_Spec.md §3.1`.

On the Settings Board this pattern is applied as one `BSS138` low-side sink per bank colour rail,
with gates driven by `U2` / `U3`.

Each LED uses three dedicated series resistors: one in each red, green, and blue cathode path.
This allows the three dice to be balanced independently under nominal 5V operation.

When the GPIO output is HIGH, the transistor turns ON, sinking the selected colour rail to GND and
illuminating any LEDs in that bank whose anode outputs are HIGH. GPIO LOW = transistor OFF = colour
rail disabled.

---

## 6. `CFG_APPLY_N` Button

SW11 is a board-mounted momentary tactile switch (SPST, active-low) connected to
U1 GPB[7]. The switch itself does not need to be panel-mount; the enclosure may use a
simple plunger or cap to mechanically actuate the switch through the panel opening.

* **Pull-up:** 10kΩ to 3V3_ENIG (R11) — idle state = logic HIGH.
* **Debounce:** 100nF X7R 0402 capacitor to GND (C4; RC τ = 1ms).
* **Operation:** CM5 enigma daemon polls GPB[7] during its main loop. On detecting LOW (button
  pressed, after debounce), the daemon:
  1. Reads U1 (full 16-bit state).
  2. Determines whether each bank should forward Settings Board user intent or apply a CM5 override.
  3. Writes final configuration to U8 GPA[3:0] and GPB[5:0] on the Stator Board.
  4. Pulses the Stator-side `CFG_APPLY_N` output (U8 GPA[4]) LOW then HIGH to trigger a
     Stator-only configuration reload.
  5. Updates U2 and U3 outputs to reflect the new configuration source and state.

This button provides operator-initiated explicit configuration commit without relying solely on
automatic polling intervals.

---

## 7. Interconnects

### J1 — I²C Connector to Stator Board

| Pin | Signal | Notes |
| :--- | :--- | :--- |
| 1 | 3V3_ENIG | Power from Stator; powers Settings Board logic (MCP23017 ICs) |
| 2 | 5V_MAIN | Indicator power supply from Stator; powers LED anodes only |
| 3 | GND | Logic ground return only; no local GND_CHASSIS bond on Settings Board |
| 4 | SDA | I²C data; shared Stator I²C-1 bus |
| 5 | SCL | I²C clock; shared Stator I²C-1 bus |
| 6 | GND | LED cathode ground return; high-current return path |

**Connector:** JST B6B-PH-K-S(LF)(SN) — 6-pin JST PH 2.0mm THT
(Mouser: 306-B6B-PH-K-SLFSN, DigiKey: 455-1708-ND, JLCPCB: C131342)

**Cable:** 6-wire harness (100mm recommended); matching JST PHR-6 crimp housing on both ends. Use 28AWG for pins 2 and 6 (power path) and 30AWG for pins 1, 3, 4, 5 (logic/signals).

**Mating connector on Stator:** J13 — same JST PH 2.0mm 6-pin part.

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
| C1 | VCC decoupling cap for U1 (MCP23017 @ 0x23) | 100nF X7R 50V | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 |
| C2 | VCC decoupling cap for U2 (MCP23017 @ 0x24) | 100nF X7R 50V | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 |
| C3 | VCC decoupling cap for U3 (MCP23017 @ 0x25) | 100nF X7R 50V | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 |
| C4 | `CFG_APPLY_N` debounce capacitor | 100nF X7R 50V | 0402 | 187-CL05B104KB5NNNC | 1276-CL05B104KB5NNNCCT-ND | C960916 |
| D1-D5 | Bank 1 discrete RGB indicator LEDs (×5: 1 source-status + 4 config bits) | Kingbright WP154A4SEJ3VBDZGW/CA — 5mm common-anode RGB THT LED | THT 5mm LED | 604-WP154A43VBDZGWCA | 754-2029-ND | C7151795 |
| D6-D12 | Bank 2 discrete RGB indicator LEDs (×7: 1 source-status + 6 config bits) | Kingbright WP154A4SEJ3VBDZGW/CA — same part as Bank 1 | THT 5mm LED | 604-WP154A43VBDZGWCA | 754-2029-ND | C7151795 |
| J1 | I²C harness connector to Stator J13 | JST B6B-PH-K-S(LF)(SN) — 6-pin JST PH 2.0mm | THT | 306-B6B-PH-K-SLFSN | 455-1708-ND | C131342 |
| Q1 | Bank 1 red colour-rail sink MOSFET | BSS138 | SOT-23 | 512-BSS138 | BSS138CT-ND | C52895 |
| Q2 | Bank 1 green colour-rail sink MOSFET | BSS138 | SOT-23 | 512-BSS138 | BSS138CT-ND | C52895 |
| Q3 | Bank 1 blue colour-rail sink MOSFET | BSS138 | SOT-23 | 512-BSS138 | BSS138CT-ND | C52895 |
| Q4 | Bank 2 red colour-rail sink MOSFET | BSS138 | SOT-23 | 512-BSS138 | BSS138CT-ND | C52895 |
| Q5 | Bank 2 green colour-rail sink MOSFET | BSS138 | SOT-23 | 512-BSS138 | BSS138CT-ND | C52895 |
| Q6 | Bank 2 blue colour-rail sink MOSFET | BSS138 | SOT-23 | 512-BSS138 | BSS138CT-ND | C52895 |
| Q7–Q11 | Bank 1 per-anode LED NMOS pre-drivers (×5, one per Bank 1 LED anode) | BSS138 — same part as Q1-Q6 | SOT-23 | 512-BSS138 | BSS138CT-ND | C52895 |
| Q12–Q18 | Bank 2 per-anode LED NMOS pre-drivers (×7, one per Bank 2 LED anode) | BSS138 — same part as Q1-Q6 | SOT-23 | 512-BSS138 | BSS138CT-ND | C52895 |
| Q19–Q30 | Per-anode LED high-side PMOS switches (×12); source at `5V_MAIN`, drain to LED anode; gate driven by Q7–Q18 BSS138 pre-drivers | Vishay SQ2319ADS-T1_BE3 — P-Ch TrenchFET SOT-23; Vds=−40V, Vgs(max)=±20V, Vgs(th)=−2.5V max, Rds(on)=145mΩ @ Vgs=−4.5V; AEC-Q101; Mouser 78-SQ2319ADS-T1_BE3; DigiKey 742-SQ2319ADS-T1_BE3CT-ND; JLCPCB C3280190 | SOT-23 | 78-SQ2319ADS-T1_BE3 | 742-SQ2319ADS-T1_BE3CT-ND | C3280190 |
| R1-R4 | Bank 1 toggle input pull-downs (×4: `CFG_ROUTE[3:0]`) | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KHCT-ND | C191124 |
| R5-R10 | Bank 2 toggle input pull-downs (×6: `CFG_REFMAP[5:0]`) | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KHCT-ND | C191124 |
| R11 | `CFG_APPLY_N` pull-up resistor | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KHCT-ND | C191124 |
| R12–R17 | MOSFET gate resistors (×6, one per transistor) | 1kΩ (1%) | 0402 | 667-ERJ-2RKF1001X | P1.00KLCT-ND | C242161 |
| R18-R29 | Per-indicator red LED series resistors (×12) | 150Ω (1%) — 5V operation, 20mA nominal | 0603 | 667-ERJ-3EKF1500V | P150HCT-ND | C400650 |
| R30-R41 | Per-indicator green LED series resistors (×12) | 100Ω (1%) — 5V operation, 20mA nominal | 0603 | 667-ERJ-3EKF1000V | P100HCT-ND | C193336 |
| R42-R53 | Per-indicator blue LED series resistors (×12) | 100Ω (1%) — 5V operation, 20mA nominal | 0603 | 667-ERJ-3EKF1000V | P100HCT-ND | C193336 |
| R54–R65 | BSS138 gate resistors for per-anode pre-drivers Q7–Q18 (×12) | 1kΩ (1%) — same part as R12-R17 | 0402 | 667-ERJ-2RKF1001X | P1.00KLCT-ND | C242161 |
| R66–R77 | PMOS gate pull-up resistors for Q19–Q30 (×12); holds PMOS gate HIGH when BSS138 OFF | KOA Speer SG73S1ERTTP4702D — 47 kΩ ±0.5% thick film anti-sulfuration 0402; AEC-Q200; DigiKey MOQ 10000, JLCPCB MOQ 40 | 0402 | 660-SG73S1ERTTP4702D | 2019-SG73S1ERTTP4702DTR-ND ⚠️ MOQ 10000 | C5915648 ⚠️ MOQ 40 |
| R78 | MCP23017 U1 `~RESET` pull-up to 3V3_ENIG | 10kΩ (1%) | 0402 | 667-ERJ-2RKF1002X | P10.0KLCT-ND | C191123 |
| R79 | MCP23017 U2 `~RESET` pull-up to 3V3_ENIG | 10kΩ (1%) | 0402 | 667-ERJ-2RKF1002X | P10.0KLCT-ND | C191123 |
| R80 | MCP23017 U3 `~RESET` pull-up to 3V3_ENIG | 10kΩ (1%) | 0402 | 667-ERJ-2RKF1002X | P10.0KLCT-ND | C191123 |
| SW1 | Bank 1 routing config bit 0 toggle switch | E-Switch 200MSP1T2B4M2QE — common Bank 1/2 config-toggle part | Panel-mount THT toggle | 612-200MSP1T2B4M2QE | EG5525-ND | C5491263 |
| SW2 | Bank 1 routing config bit 1 toggle switch | E-Switch 200MSP1T2B4M2QE — same part as SW1 | Panel-mount THT toggle | 612-200MSP1T2B4M2QE | EG5525-ND | C5491263 |
| SW3 | Bank 1 routing config bit 2 toggle switch | E-Switch 200MSP1T2B4M2QE — same part as SW1 | Panel-mount THT toggle | 612-200MSP1T2B4M2QE | EG5525-ND | C5491263 |
| SW4 | Bank 1 routing config bit 3 toggle switch | E-Switch 200MSP1T2B4M2QE — same part as SW1 | Panel-mount THT toggle | 612-200MSP1T2B4M2QE | EG5525-ND | C5491263 |
| SW5 | Bank 2 reflector config bit 0 toggle switch | E-Switch 200MSP1T2B4M2QE — same part as SW1 | Panel-mount THT toggle | 612-200MSP1T2B4M2QE | EG5525-ND | C5491263 |
| SW6 | Bank 2 reflector config bit 1 toggle switch | E-Switch 200MSP1T2B4M2QE — same part as SW1 | Panel-mount THT toggle | 612-200MSP1T2B4M2QE | EG5525-ND | C5491263 |
| SW7 | Bank 2 reflector config bit 2 toggle switch | E-Switch 200MSP1T2B4M2QE — same part as SW1 | Panel-mount THT toggle | 612-200MSP1T2B4M2QE | EG5525-ND | C5491263 |
| SW8 | Bank 2 reflector config bit 3 toggle switch | E-Switch 200MSP1T2B4M2QE — same part as SW1 | Panel-mount THT toggle | 612-200MSP1T2B4M2QE | EG5525-ND | C5491263 |
| SW9 | Bank 2 reflector config bit 4 toggle switch | E-Switch 200MSP1T2B4M2QE — same part as SW1 | Panel-mount THT toggle | 612-200MSP1T2B4M2QE | EG5525-ND | C5491263 |
| SW10 | Bank 2 reflector config bit 5 toggle switch | E-Switch 200MSP1T2B4M2QE — same part as SW1 | Panel-mount THT toggle | 612-200MSP1T2B4M2QE | EG5525-ND | C5491263 |
| SW11 | `CFG_APPLY_N` momentary pushbutton | Omron B3F-1070 — SPST NO through-hole tactile switch; board-mounted and mechanically actuated through enclosure | THT tactile | 653-B3F-1070 | SW406-ND | C726011 |
| U1 | MCP23017 I²C GPIO Expander (switch input reader) | MCP23017T-E/SO @ 0x23 | SOIC-28 | 579-MCP23017T-E/SO | MCP23017T-E/SOCT-ND | C47023 |
| U2 | MCP23017 I²C GPIO Expander (Bank 1 LED controller) | MCP23017T-E/SO @ 0x24 | SOIC-28 | 579-MCP23017T-E/SO | MCP23017T-E/SOCT-ND | C47023 |
| U3 | MCP23017 I²C GPIO Expander (Bank 2 LED controller) | MCP23017T-E/SO @ 0x25 | SOIC-28 | 579-MCP23017T-E/SO | MCP23017T-E/SOCT-ND | C47023 |

---

## 10. Power Budget

### 3V3_ENIG (Logic Rail)

| Component | Typical (mA) | Max (mA) | Notes |
| :--- | :---: | :---: | :--- |
| U1 (MCP23017 @ 0x23) | 25 | 50 | Switch input reader; 16 GPIO inputs |
| U2 (MCP23017 @ 0x24) | 25 | 50 | Bank 1 LED controller; low-side MOSFET drivers |
| U3 (MCP23017 @ 0x25) | 25 | 50 | Bank 2 LED controller; low-side MOSFET drivers |
| **Total 3V3_ENIG** | **75 mA** | **150 mA** | Well within Stator J13 capacity |

### 5V_MAIN (Indicator Rail Allocation)

| Load | Typical (mA) | Max (mA) | Notes |
| :--- | :---: | :---: | :--- |
| Bank 1 LEDs (5× @ 20mA) | 60 | 100 | Typical assumes ~12mA per LED average; max = 5 × 20mA = 100mA with one active colour rail |
| Bank 2 LEDs (7× @ 20mA) | 84 | 140 | Typical assumes ~12mA per LED average; max = 7 × 20mA = 140mA with one active colour rail |
| **Total indicator rail** | **144 mA** | **240 mA** | Definitive max = 100mA + 140mA; one active colour per bank, all 12 LEDs illuminated |

**Settings Board 5V_MAIN Allocation:**

* Settings Board indicator rail: **240mA max**
* This board uses `5V_MAIN` only for LED anode power.

---

## 11. Component Count Summary

| Category | Quantity | Notes |
| :--- | :---: | :--- |
| **Toggle Switches** | 10 | E-Switch 200MSP1T2B4M2QE — SPDT latching panel-mount |
| **RGB LEDs** | 12 | Kingbright WP154A4SEJ3VBDZGW/CA — 5mm common-anode THT |
| **MCP23017 I²C Expanders** | 3 | U1, U2, U3 |
| **BSS138 MOSFETs (colour-rail low-side)** | 6 | Q1/G/B, Q4/G/B — shared colour-rail cathode switches |
| **BSS138 MOSFETs (per-anode pre-driver)** | 12 | Q7–Q18 — one per LED anode; drives PMOS high-side gate |
| **PMOS MOSFETs (per-anode high-side switch)** | 12 | Q19–Q30 — Vishay SQ2319ADS-T1_BE3; source at 5V_MAIN, drain to LED anode |
| **0603 LED path resistors** | 36 | 12× red (150Ω), 12× green (100Ω), 12× blue (100Ω) |
| **0603 Resistors (switch pull-down)** | 10 | 10kΩ pull-downs on all toggle-switch inputs |
| **0402 Resistors (colour-rail gate)** | 6 | R12–R17: 1kΩ colour-rail MOSFET gate resistors |
| **0402 Resistors (per-anode gate)** | 12 | R54–R65: 1kΩ BSS138 pre-driver gate resistors |
| **0402 Resistors (PMOS pull-up)** | 12 | R66–R77: KOA Speer SG73S1ERTTP4702D 47 kΩ ±0.5% PMOS gate pull-ups |
| **0603 Resistors (misc)** | 1 | R11: 10kΩ `CFG_APPLY_N` pull-up |
| **0402 Capacitors (decoupling)** | 3 | 100nF X7R for 3× MCP23017s |
| **0402 Capacitors (debounce)** | 1 | C4: 100nF X7R `CFG_APPLY_N` debounce |
| **JST PH Connectors** | 1 | J1: 6-pin B6B-PH-K-S(LF)(SN) to Stator |
| **Pushbutton Switch** | 1 | SW11 — Omron B3F-1070 SPST NO through-hole tactile switch |

**Total unique part numbers:** ~18
**Total component count:** ~125

---

## 12. Design Notes

### LED Control Architecture

The Settings Board uses a **hybrid topology**: shared colour-rail low-side switches for RGB selection
combined with per-anode high-side switches for individual LED illumination control:

* **Colour-rail low-side stage (Q1–Q6):** 6× BSS138 N-channel MOSFETs switch each RGB cathode rail to
  GND — 3 per bank (red, green, blue). MCP23017 GPIO drives gate directly through 1 kΩ resistors
  (R12–R17). GPIO HIGH = transistor ON = colour rail active.

* **Per-anode high-side stage (Q7–Q30):** 12× two-stage circuits (one per LED anode) consisting of:
  1. BSS138 NMOS pre-driver (Q7–Q18) — gate driven by MCP23017 GPIO through 1 kΩ resistor (R54–R65)
  2. PMOS high-side switch (Q19–Q30) — gate held HIGH by 47 kΩ pull-up (R66–R77) to `5V_MAIN`;
     BSS138 drain pulls gate LOW to enable PMOS. PMOS source at `5V_MAIN`, drain to LED anode.

  GPIO HIGH → BSS138 ON → PMOS gate ≈0 V → PMOS ON → LED anode at `5V_MAIN`. Logic is non-inverted;
  no firmware inversion required.

* **Root cause note:** Kingbright WP154A4SEJ3VBDZGW/CA LEDs have typical Vf = 3.3 V (blue/green).
  The MCP23017 GPIO output maximum is 3.3 V and cannot source current into a 5 V-supply anode directly.
  The two-stage high-side topology resolves this without requiring firmware changes or rail compromise.

* **Power-up behaviour:** MCP23017 Hi-Z default leaves BSS138 gates floating (consistent with Q1–Q6).
  Validate that LED anodes remain de-energised on power-up during system-level testing.

### 5V Power Routing

Indicator power is provided on `J1` pin 2 as `5V_MAIN` from the Stator `J13` harness.

On the Settings Board, this rail powers the LED anodes only (240mA max) and is not used by the
logic supply, which remains on `3V3_ENIG`.

### I²C Address Selection

The Settings Board uses the contiguous `0x23`-`0x25` block immediately after the Stator's
`0x20`-`0x22` expanders. This keeps the shared Settings/Stator GPIO devices grouped together on the
bus. The authoritative full-system I²C allocation is defined in `Controller/Design_Spec.md §4.1`.
