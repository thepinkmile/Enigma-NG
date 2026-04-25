# Stator Board (V1.0) Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-25

The Stator Board is the mechanical and electrical backbone of the rotor stack. It provides the high-current distribution and signal routing for the 30 modular rotors.

## 1. Overview

* **Stackup:** 4-Layer / 2oz Finished Copper.
* **Layer Mapping:** L1: Signal (JTAG/routing) | L2: GND | L3: 3V3_ENIG | L4: ENC Data.
* **Role:** Removable vertical daughterboard and master switchboard for the 30-rotor stack and peripheral encoder boards.

### Functional & Design Requirements

#### Functional Requirements

| ID | Functional Requirement | Notes | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| FR-STA-01 | Serve as the removable mechanical and electrical backplane for the 30-rotor stack | Provides all power, JTAG, and data connectivity to rotors | §2 Core Features; BOM J1–J3 (ERF8 rotor sockets) |
| FR-STA-02 | Distribute 3V3_ENIG power to all 30 rotor slots simultaneously | Via 2oz copper pour on L3 | §2 Core Features; §3 Encryption & JTAG Hub; BOM L1–L4 (ferrite beads) |
| FR-STA-03 | Route the JTAG chain from the Controller Board through all 30 rotor slots in sequence | Serial daisy-chain; Stator CPLD is device 1 | §3 Encryption & JTAG Hub; BOM U1 (EPM570T100I5N) |
| FR-STA-04 | Receive TTD_RETURN from the Reflector and forward to the Controller Board | Via J10 (Adam Tech `BHR-16-VUA` 16-pin reflector / extension port) into the `J5` logic dock return path | §3 Encryption & JTAG Hub; BOM J10, R2 (10kΩ pull-up) |
| FR-STA-05 | Interface with up to 6 Encoder Modules via IDC ribbon cables; route a single 6-bit `ENC_DATA[5:0]` service bus through one HID encode path, one HID decode path, and two configurable plugboard passes | Bank 1 = `KBD_ENC` + `LBD_DEC`; Bank 2 = `PLG_PASS1_DEC` + `PLG_PASS1_ENC`; Bank 3 = `PLG_PASS2_DEC` + `PLG_PASS2_ENC`; Stator owns the fixed per-port aliases | §3 Plugboard Routing; §4 Interconnects; BOM J4–J9 (20-pin IDC) |
| FR-STA-06 | Host a CPLD as the first device in the system JTAG chain | Intel MAX II EPM570 (570 LEs required for startup-loaded reflector map registers + routing matrix) | §3 Encryption & JTAG Hub; BOM U1 (EPM570T100I5N) |
| FR-STA-07 | Connect to the Controller Board via two hybrid blind-mate dock connectors | `J11` = 5V-biased power dock; `J12` = 3V3/JTAG/I2C dock | §4 Interconnects; BOM J11, J12 |
| FR-STA-08 | Select the active plugboard routing configuration from the Settings Board user-intent bus via I²C; CM5 may override it with GUI-selected presets | Settings Board `CFG_ROUTE[3:0]` provides 16 routing configurations; CM5 reads U_EXP_SW_IN @ 0x23, decides whether to forward user intent or apply an override, writes final `CFG_ROUTE[3:0]` to U_EXP4 GPA[3:0] @ 0x22, and pulses `CFG_APPLY_N` to reload the Stator CPLD | §3 Configuration Bank 1 (Routing); §4.2 I²C-1 Bus Devices; BOM U_EXP4, R16–R19 |
| FR-STA-09 | Select and apply a stored reflector substitution map at the reflection boundary while retaining the mandatory physical Reflector board as the electrical turnaround | Settings Board `CFG_REFMAP[5:0]` provides a 6-bit reflector-map selection; CM5 may override it with GUI-selected presets; final `CFG_REFMAP[5:0]` is driven to the CPLD by U_EXP4 GPB[5:0] @ 0x22 | §3 Configuration Bank 2 (Reflector Mapping); §4.2 I²C-1 Bus Devices; BOM U_EXP4, R21–R26 |
| FR-STA-10 | Provide I²C GPIO expansion for CM5 virtual keypress injection, ENC service-bus monitoring, SYS_RESET_N management, and CPLD configuration driving | Via three MCP23017 expanders: U_EXP1 @ 0x20, U_EXP2 @ 0x21, U_EXP4 @ 0x22 on shared I²C-1 bus | §4 I²C Devices; BOM U_EXP1, U_EXP2, U_EXP4 |
| FR-STA-11 | **Retired** — servo PWM output moved to the Controller | Controller-local direct CM5 PWM now owns the servo interface | DEC-038; `Controller/Design_Spec.md` |
| FR-STA-12 | **Retired** — SERVO_HOME sensing moved to the Controller | Controller-local home switch now owns the 0° reference sensing | DEC-038; `Controller/Design_Spec.md` |
| FR-STA-13 | Select between the physical keyboard 6-bit source bus and CM5 virtual key data before the cipher pipeline | External 6-bit 2:1 mux at the `KBD_ENC` (`J4`) entry point; `KEY_CM5_ACTIVE` chooses the source, `CM5_KEY_DATA[5:0]` carries the CM5 value, and the mux enable pin(s) are tied LOW so the selected path is always driven while the board is powered | §3 External Keyboard Source Mux |
| FR-STA-14 | Connect to Settings Board via I²C-1 bus for user-intent configuration, `CFG_APPLY_N`, and LED status output | J13 = 6-pin JST PH 2.0mm connector (`3V3_ENIG`, `5V_MAIN`, `GND`, `SDA`, `SCL`, `GND`); Settings Board expanders 0x23 (user-intent input), 0x24 (Bank 1 LED), and 0x25 (Bank 2 LED) share the Stator I²C-1 bus | §4.2 I²C-1 Bus Devices; BOM J13 |

#### Design Requirements

| ID | Design Requirement | Specification | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| DR-STA-01 | PCB stackup | 4-layer, 2oz finished copper (JLC04161H-7628) | §7 PCB Fabrication & Stackup |
| DR-STA-02 | Layer mapping | L1 = Signal (JTAG/routing), L2 = GND, L3 = 3V3_ENIG, L4 = ENC Data | §1 Overview |
| DR-STA-03 | Rotor interface (per slot) | J1 = ERF8-005 (JTAG), J2 = ERF8-005 (Power), J3 = ERF8-010 (ENC); 1 slot set | §4 Interconnects; BOM J1–J3 (ERF8-005/ERF8-010) |
| DR-STA-04 | Encoder interface | J4/J5/J6/J7/J8/J9 = 20-pin 2×10 IDC (6 fixed-role encoder ports in 3 banks of 2) carrying generic Encoder `ENC_DATA[5:0]` plus Stator-owned aliases | §4 Interconnects; BOM J4–J9 |
| DR-STA-05 | TTD_RETURN input | J10 = Adam Tech `BHR-16-VUA` 16-pin 2×8 shrouded header; `TTD_RETURN` on pin 15 (from Reflector J4) | §3 Encryption & JTAG Hub; BOM J10 |
| DR-STA-06 | Controller dock connectors | `J11/J12` = Molex `2195620015` hybrid plugs mating with Controller `2195630015` receptacles | §4 Interconnects; BOM J11, J12 |
| DR-STA-07 | CPLD | Intel MAX II EPM570T100I5N (TQFP-100); 570 LEs; same footprint as EPM240 (drop-in); 570 LEs required for startup-loaded 64-char reflector map (384 FFs) + routing matrix logic | §3 Encryption & JTAG Hub; BOM U1 (EPM570T100I5N) |
| DR-STA-08 | Power monitoring | INA219 current sensor; shunt R1 = CSS2H-2512R-R010ELF (10mΩ 2512 Kelvin), sized for the 2.05 A worst-case typical stack load | §5 Power Telemetry; BOM U2 (INA219AIDR), R1 (CSS2H 10mΩ shunt) |
| DR-STA-09 | Maximum 3V3_ENIG load | 2.05 A worst-case typical (30 rotors + Stator CPLD + all encoders) | §2 Core Features; §5 Power Telemetry |
| DR-STA-10 | Routing configuration selection | Logical `CFG_ROUTE[3:0]` inputs are driven by U_EXP4 GPA[3:0]; 4× 10kΩ pull-down resistors R16–R19 retained on CPLD inputs as power-up safe defaults (hold 0 when U_EXP4 is uninitialised) | §3 Configuration Bank 1 (Routing); BOM U_EXP4, R16–R19 |
| DR-STA-11 | Reflector map selection | Logical `CFG_REFMAP[5:0]` inputs are driven by U_EXP4 GPB[5:0]; 6× 10kΩ pull-down resistors R21–R26 retained on CPLD inputs as power-up safe defaults | §3 Configuration Bank 2 (Reflector Mapping); BOM U_EXP4, R21–R26 |
| DR-STA-12 | I²C GPIO expanders | U_EXP1 = MCP23017T-E/SO @ 0x20; U_EXP2 = MCP23017T-E/SO @ 0x21; U_EXP4 = MCP23017T-E/SO @ 0x22; SOIC-28 package; on shared I²C-1 bus | BOM U_EXP1, U_EXP2, U_EXP4 |
| DR-STA-13 | **Retired** — I²C PWM driver | Servo PWM generation moved to direct CM5 GPIO on the Controller | DEC-038; `Controller/Design_Spec.md` |
| DR-STA-14 | **Retired** — Servo connector | Servo connector ownership moved to the Controller | DEC-038; `Controller/Design_Spec.md` |
| DR-STA-15 | **Retired** — SERVO_HOME switch | Servo home-switch ownership moved to the Controller | DEC-038; `Controller/Design_Spec.md` |
| DR-STA-16 | U_EXP4 specification | U_EXP4 = MCP23017T-E/SO @ 0x22; SOIC-28; A2=LOW, A1=HIGH, A0=LOW; GPA[3:0] = `CFG_ROUTE[3:0]` outputs; GPA[4] = active-low `CFG_APPLY_N` Stator-only apply/reset output; GPB[5:0] = `CFG_REFMAP[5:0]` outputs | BOM U_EXP4 |
| DR-STA-17 | J13 connector | J13 = 6-pin JST PH 2.0mm B6B-PH-K-S(LF)(SN); pins: `3V3_ENIG`, `5V_MAIN`, `GND`, `SDA`, `SCL`, `GND`; connects to Settings Board J_I2C via 6-wire harness. `5V_MAIN` is derived from the Controller-fed `J11` branch. | BOM J13 |
| DR-STA-18 | `CFG_APPLY_N` signal | `CFG_APPLY_N` = active-low Stator-only apply/reset pulse from U_EXP4 GPA[4]; combined with `SYS_RESET_N` through U3 (`SN74LVC1G08DBVR`) so either signal can assert the Stator CPLD reset path; forcing `CFG_APPLY_N` LOW reloads `CFG_ROUTE[3:0]` and `CFG_REFMAP[5:0]` without resetting the wider system | BOM U_EXP4, U3; §3 Configuration Bank 1 (Routing) |

## 2. Core Features

* **Modular Slots:** 1× Samtec ERF8 female socket set (3 connectors: ERF8-005 JTAG, ERF8-005 Power, ERF8-010 ENC\_DATA) mating with the ERM8 male headers on the Rotor.
* **Power Tree:** A 2oz copper pour for the `3V3_ENIG` rail to handle the **2.05A worst-case typical** load without voltage sag (see `design/Electronics/Power_Budgets.md`).
  The 5A figure previously quoted was a conservative design margin; the LDO hard limit is 3.0A.

### GND_CHASSIS Single-Point Bond

Per `design/Standards/Global_Routing_Spec.md §5`, the Stator implements a local `GND_CHASSIS` net
tied to its mounting holes and any deliberate enclosure-contact features, but it does **not**
implement a local GND-to-GND_CHASSIS bond. The system's only galvanic GND ↔ GND_CHASSIS bond is
defined on the Power Module at the common power-entry point immediately before the eFuse, so
`J4/J5` dock-entry GND remains signal/power return only and must not be bridged locally to
chassis on the Stator.

## 3. Encryption & JTAG Hub

* **CPLD:** Intel MAX II EPM570T100I5N CPLD (Logic Router & Reflector).

### CPLD Signal Routing Matrix

The Stator CPLD (U1) is the bidirectional ENC_DATA routing hub for the full encryption cycle.
It has four fixed external ENC_DATA service interfaces:

* `J4` = `KBD_ENC` (keyboard encode source)
* `J5` = `LBD_DEC` (lightboard decode destination)
* `J3` = Rotor 1 ENC connector
* `J10` = Reflector / Extension return connector

It also owns two configurable plugboard passes, each implemented as a paired decode/encode module:

* `J6` + `J7` = Plugboard Pass 1
* `J8` + `J9` = Plugboard Pass 2

The encryption signal passes through the CPLD at three defined interception points:

| Step | CPLD receives from | Optional plugboard insertion | CPLD drives to |
| :--- | :--- | :--- | :--- |
| **1 — Forward entry** | `J4 ENC_IN_KBD[5:0]` — keyboard keystroke | Pre-Rotor 1 position — Pass 1 and/or Pass 2 | `J3 ENC_OUT_ROT[5:0]` → Rotor 1 (starts forward pass through rotor stack) |
| **2 — Reflector return** | `J10 ENC_IN_REF[5:0]` — reflected signal returned from Reflector chain | At Reflector boundary — Pass 1 and/or Pass 2 | `J10 ENC_OUT_REF[5:0]` → Reflector chain → Rotor 30 (starts return pass back through rotor stack) |
| **3 — Final exit** | `J3 ENC_IN_ROT[5:0]` — Rotor 1 return-pass output | Post-Rotor 1 return position — Pass 1 and/or Pass 2 | `J5 ENC_OUT_LBD[5:0]` → Lightboard |

At each step the CPLD either passes the signal transparently (no plugboard) or routes it through
Plugboard Pass 1 (`J6` decode -> passive jackfield -> `J7` encode) and/or Plugboard Pass 2
(`J8` decode -> passive jackfield -> `J9` encode) before forwarding. `J4`-`J9` use Stator-owned
service aliases that map onto the remote Encoder board's generic `ENC_DATA[5:0]` pins. `J3` and
`J10` aliases are Stator-local names only; the downstream Rotor / Extension / Reflector chain keeps
its own generic `ENC_IN[5:0]` and `ENC_OUT[5:0]` definitions. The active insertion positions are
determined by the VHDL routing case statement selected by U_EXP4 GPA[3:0] written by the CM5 daemon
(see §3 Panel Switch Configuration and DEC-032).

#### Configuration Bank 1 — Plugboard Routing

Settings Board toggle switches provide a 4-bit user-intent image of the logical `CFG_ROUTE[3:0]`
bus, selecting the active routing case from 16 configurations synthesised into the CPLD fabric. No
JTAG reprogramming is required to change configuration — only a single JTAG flash at initial
programming. `CFG_ROUTE[1:0]` encode **Plugboard Pass 1** position; `CFG_ROUTE[3:2]` encode
**Plugboard Pass 2** position.

The final applied `CFG_ROUTE[3:0]` value is driven to the CPLD by U_EXP4 GPA[3:0] via I²C. The
CM5 daemon decides whether that final value is the forwarded Settings Board user-intent image or a
CM5-defined override. `CFG_ROUTE_CM5_ACTIVE` is the corresponding Settings Board indicator state:
LOW = user-intent forwarded, HIGH = CM5-defined override active. Pull-down resistors R16–R19 hold
each CPLD input at logic-0 when U_EXP4 is uninitialised (power-up safe default).

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

#### Configuration Bank 2 — Reflector Mapping

Settings Board toggle switches provide a 6-bit user-intent image of the logical `CFG_REFMAP[5:0]`
bus used by the Stator CPLD to select the reflector-map index at the reflection boundary. The
physical Reflector board remains mandatory and always provides the electrical turnaround at the end
of the rotor/extension chain; Bank 2 only selects which stored involutory map the Stator applies
before the returned signal re-enters the stack.

The final applied `CFG_REFMAP[5:0]` value is driven to the CPLD by U_EXP4 GPB[5:0] via I²C. The
CM5 daemon decides whether that final value is the forwarded Settings Board user-intent image or a
CM5-defined override. `CFG_REFMAP_CM5_ACTIVE` is the corresponding Settings Board indicator state:
LOW = user-intent forwarded, HIGH = CM5-defined override active. After writing the final config,
CM5 may assert `CFG_APPLY_N` LOW to force a Stator-only reload.

| Bit | Settings Board toggle | Function |
| :--- | :--- | :--- |
| `CFG_REFMAP[5:0]` | SW_B2[5:0] | **6-bit map index** (0–63): selects which involutory reflector map to load from UFM at configuration load; indices 0–20 are currently allocated |

Pull-down resistors R21–R26 on the Stator CPLD `CFG_REFMAP[5:0]` input pins hold each input at
logic-0 when U_EXP4 is uninitialised (default map index = 0).

When Bank 2 is latched, the CPLD serially reads the indexed map from UFM into internal flip-flop
registers (~40 µs). At the reflection boundary (Step 2 in the routing matrix), the CPLD applies the
loaded map combinationally while the mandatory Reflector board provides the physical return path on
J10. `ENC_OUT_REF[5:0]` and `ENC_IN_REF[5:0]` therefore remain part of the active signal path in all
supported configurations.

Bank 1 (routing matrix) and Bank 2 (reflector mode) are fully independent; all 16 Bank 1
configurations are valid regardless of the Bank 2 setting.

**UFM map storage:** 21 involutory (self-inverse) reflector maps; same 64-entry × 6-bit format as
Rotor UFM maps (384 bits per map; 21 × 384 = 8,064 bits ≤ 8,192-bit UFM). Maps are involutory by
definition: applying the same map twice returns the original character, preserving Enigma cipher
symmetry. Pre-loaded indices:

| Index | Map | Notes |
| :--- | :--- | :--- |
| 0 | UKW-A equivalent | Historical Enigma Reflector A (26-char; entries 26–63 = identity for 64-char variant) |
| 1 | UKW-B equivalent | Historical Enigma Reflector B — most common WWII Enigma variant |
| 2 | UKW-C equivalent | Historical Enigma Reflector C — later wartime variant |
| 3–20 | Custom | Available for user-defined involutory maps via JTAG programming |

* Decoupling and bulk entry capacitor requirements per `design/Standards/Global_Routing_Spec.md §3`.
* **Ferrite Bead Rule:** Use **4x ferrite beads** (one per 3V3_ENIG rotor feed) between the `J12` dock entry and rotor power distribution to isolate switching transients from Controller logic.
* **Current Margin Check:** Rotor rail is budgeted at **1.65A** (30 rotors × 55mA budget — see `design/Electronics/Power_Budgets.md`);
  with 4 parallel feeds this is ~**413mA per bead** nominal sharing,
  well within the **3.5A** bead rating. Total 3V3_ENIG worst case including all CPLDs and encoders: 2.05A (~32% headroom vs 3.0A LDO).
* **JTAG Return:** Includes 10kΩ pull-up on TTD_RETURN at the `J12` logic-dock entry/exit boundary (R2).
* **JTAG Pull Resistors (×4, placed near Stator CPLD U1):**
  * **TMS:** 10kΩ pull-up to 3V3_ENIG (R3) — ensures JTAG TAP resets to Test-Logic-Reset on power-up and when controller is idle.
  * **TDI:** 10kΩ pull-up to 3V3_ENIG (R4) — holds TDI at logic-1 (BYPASS) when not actively driven by the Controller.
  * **TCK:** 10kΩ pull-down to GND (R5) — prevents spurious clocking when TCK line is floating.
  * **SYS_RESET_N:** 10kΩ pull-up to 3V3_ENIG (R6) — active-low signal; pull-up ensures CPLD remains
    out of reset by default.
* **JTAG Trace Width Rule:** All JTAG signal traces on L1 (TCK, TMS, TDI, TDO) shall
  be routed at **0.127 mm (5 mil)** width over the L2 GND plane, targeting **50 Ω controlled
  impedance**. See `design/Electronics/Investigations/JTAG_Integrity.md` and DEC-016.
* **JTAG Series Termination at Encoder Port Outputs:** 75 Ω series resistors placed within 2 mm of
  each encoder-port connector pad **on the Stator PCB**, targeting 95 Ω source impedance to match
  the ~100 Ω IDC ribbon cable:
  * **R7-R12:** TCK -> J4, J5, J6, J7, J8, J9 respectively.
  * **R33-R38:** TMS -> J4, J5, J6, J7, J8, J9 respectively.
  * **R27:** Stator CPLD TDO -> J4 TDI.
  * **R28:** J4 TDO return -> J5 TDI.
  * **R29:** J5 TDO return -> J6 TDI.
  * **R30:** J6 TDO return -> J7 TDI.
  * **R31:** J7 TDO return -> J8 TDI.
  * **R32:** J8 TDO return -> J9 TDI.
  * All TDI-chain resistors are **Stator-side** resistors — no series resistors are required at the
    Encoder cable inputs.
* **Reset / Apply path:** `SYS_RESET_N` remains the active-low global reset. `CFG_APPLY_N` is a
  separate active-low Stator-only apply/reset pulse driven by U_EXP4 GPA[4]. A dedicated external
  `SN74LVC1G08DBVR` 2-input AND gate combines `SYS_RESET_N` and `CFG_APPLY_N` into the Stator CPLD
  `DEV_CLRN` path so a low on either signal resets the Stator CPLD.

#### External Keyboard Source Mux

The Stator shall use an external 6-bit 2:1 mux at the `J4` keyboard-source entry point
(Step 1 — Forward entry in the routing matrix). `KEY_CM5_ACTIVE` chooses which 6-bit source is
forwarded into the cipher pipeline. The implementation uses `U4` and `U5`, both
`74HC157PW-Q100,118` quad 2:1 mux devices, with both `E` pins tied to GND so the mux path remains
enabled whenever the board is powered:

* **`KEY_CM5_ACTIVE=0` (default):** the physical keyboard 6-bit source bus is forwarded. Normal operator use.
* **`KEY_CM5_ACTIVE=1`:** `CM5_KEY_DATA[5:0]` is forwarded instead, enabling CM5 autonomous / virtual-key mode.

U_EXP2 GPA[7] is used for `SYS_RESET_N` in this implementation, which fully populates the GPA port
while leaving GPB spare/reserved for future use. The mux enable function remains hard-wired active
and `KEY_CM5_ACTIVE` continues to occupy GPA[6].

## 4. Interconnects

* **Controller Dock:** The Stator plugs into the Controller through two Molex EXTreme Guardian HD hybrid connectors.
  * **J11 (5V-biased dock):** `4 × 5V_MAIN` blades, `1 × GND` blade, signal field allocated to extra `GND` returns / guards.
  * **J12 (3V3 / logic dock):** `4 × 3V3_ENIG` blades, `1 × GND` blade, guarded `TCK`, `TMS`, `TDI`, `TTD_RETURN`, `I2C1_SDA`, and `I2C1_SCL`; all remaining signal contacts tied to `GND`.
  * **Controller mating part:** Molex `2195630015` receptacle. **Stator plug:** Molex `2195620015`.
  * **Cross-ref:** See `Controller/Design_Spec.md` §2 and `Controller/Board_Layout.md` for the active dock allocation.
  * **Reference PDFs:** [`Molex-2195630015-datasheet.pdf`](../../Datasheets/Molex-2195630015-datasheet.pdf),
    [`Molex-2195630015-drawings.pdf`](../../Datasheets/Molex-2195630015-drawings.pdf),
    [`Molex-2195620015-datasheet.pdf`](../../Datasheets/Molex-2195620015-datasheet.pdf),
    [`Molex-2195620015-drawings.pdf`](../../Datasheets/Molex-2195620015-drawings.pdf),
    [`Molex-ExtremeGuardianHD-2141130000-PS-000-specification.pdf`](../../Datasheets/Molex-ExtremeGuardianHD-2141130000-PS-000-specification.pdf)
* **Settings Board Interconnect:** `J13` is the 6-pin JST PH 2.0mm harness from the Stator to the
  Settings Board `J_I2C` connector.
  * **Signals:** `3V3_ENIG`, `5V_MAIN`, `GND`, `SDA`, `SCL`, `GND`.
  * **Power role:** `5V_MAIN` is fanned out from the incoming `J11` branch to `J13` as a
    pass-through LED supply only.
* **Encoder Interconnects:** 20-pin (2×10) 2.54mm shrouded box headers (power, `ENC_DATA[5:0]`, JTAG).
* **Plugboard Routing — Configurable Signal Chain Positions:**
  The Stator CPLD implements a configurable routing matrix (see §3 CPLD Signal Routing Matrix) with
  three plugboard insertion positions in the full encryption cycle. The active configuration is
  selected via the Settings Board user-intent `CFG_ROUTE[3:0]` image, read by CM5
  and driven to the CPLD by U_EXP4 GPA[3:0] (16 pre-defined configurations — no JTAG
  reprogramming required for configuration changes). The six encoder ports are arranged as three
  banks of two, with one fixed HID bank and two configurable plugboard-pass banks:

  | Port | Default role | Plugboard signal chain position |
  | :--- | :--- | :--- |
  | **J4** | `KBD_ENC` | Fixed: keyboard source (not used as a plugboard pass) |
  | **J5** | `LBD_DEC` | Fixed: lightboard destination (not used as a plugboard pass) |
  | **J6 / J7** | Plugboard Pass 1 (`DEC` / `ENC`) | Configurable: pre-Rotor 1 / At Reflector / post-Rotor 1 return (set by SW_B1[1:0]) |
  | **J8 / J9** | Plugboard Pass 2 (`DEC` / `ENC`) | Configurable: pre-Rotor 1 / At Reflector / post-Rotor 1 return (set by SW_B1[3:2]) |

  The Stator CPLD implements all 16 configurations as synthesised VHDL case logic. See
  `design/Electronics/Stator/Board_Layout.md` and `design/Electronics/Encoder/Design_Spec.md §1`
  for further detail.
* **Reflector/Extension Interconnect:**16-pin (2x8) Vertical Shrouded Header (Power, SYS_RESET_N,
  ENC_DATA, TTD_RETURN).
  * **Routing:** Cables secured to the chassis floor with conductive EMI tape.
  * Extension boards enable daisy chaining this interconnect (to enable multi-stack rotor configurations).
  * **Cross-ref:** For matching interconnect pinouts on power (3V3_ENIG/GND), SYS_RESET_N,
    `ENC_OUT_REF[5:0]`, `ENC_IN_REF[5:0]`, and JTAG TTD_RETURN lines used for reflector
    loopback/plugboard mapping, See:
    * `Extension/Design_Spec.md`
    * `Reflector/Design_Spec.md`
  * **Reflector boundary aliases (bidirectional — simultaneous):** J10 carries the Stator-owned
    reflector aliases on two separate pin groups simultaneously. `ENC_IN_REF[5:0]` (pins 9–14)
    returns the reflected signal from the Reflector chain to the Stator CPLD (Step 2 receive in the
    routing matrix). `ENC_OUT_REF[5:0]` (pins 3–8) carries the return-pass signal driven by the
    Stator CPLD back to the Reflector chain after optional plugboard insertion (Step 2 drive — starts
    the return pass through the rotor stack).
* **Rotor Interconnect:** The Stator provides 1 rotor slot (Rotor 1 input side) using 3 ERF8 female sockets.
  * **JTAG:** ERF8-005-05.0-S-DV-K-TR (10-pin 2×5, 0.8mm pitch) — TCK, TMS, TTD (TDI function on input side),
    SYS\_RESET\_N with interleaved GND. **J1 pin 6 = TTD** (outgoing TDI to Rotor 1).
    Pin 10 = spare/GND (TDO does NOT return via this connector — it returns via J10 pin 15).
  * **Power:** ERF8-005-05.0-S-DV-K-TR (10-pin 2×5, 0.8mm pitch) — 5× 3V3\_ENIG, 5× GND. Same part as JTAG socket.
  * **ENC DATA (bidirectional):** ERF8-010-05.0-S-DV-K-TR (20-pin 2×10, 0.8mm pitch) —
    `ENC_OUT_ROT[5:0]` (CPLD drives to Rotor 1, forward pass — Step 1 drive);
    `ENC_IN_ROT[5:0]` (CPLD receives from Rotor 1, return pass — Step 3 receive); 8× GND fill.
  * **Cross-ref:** Authoritative pinout is defined in `Rotor/Design_Spec.md §3.4` (DEC-018 ownership).
  * **Note:** Rotor-to-rotor connections beyond Rotor 1 are direct (each Rotor J4/J5/J6 output mates with
    the next Rotor J1/J2/J3 input); Extension boards provide inter-group bridging at group boundaries in
    the serial chain (Stator → Rotor 1 → … → Rotor 30 → Reflector J1–J3).

### 4.2 I²C-1 Bus Devices

The devices listed below are the Stator-local devices on the shared I²C-1 bus. The authoritative
full-system I²C allocation is defined in `Controller/Design_Spec.md §4.1`.

| Address | Device | Ref | Function |
| :--- | :--- | :--- | :--- |
| 0x20 | MCP23017 | U_EXP1 | ENC service-bus monitoring (16 GPIO) |
| 0x21 | MCP23017 | U_EXP2 | `CM5_KEY_DATA[5:0]`, `KEY_CM5_ACTIVE`, `SYS_RESET_N`, spare GPIO (16 GPIO) |
| 0x22 | MCP23017 | U_EXP4 | CPLD configuration output driver: `CFG_ROUTE[3:0]` + `CFG_REFMAP[5:0]` + `CFG_APPLY_N` (16 GPIO) |
| 0x45 | INA219 | U2 | Rotor stack current/power telemetry |

## 5. Power Telemetry (The "Encryption Load")

* **Purpose:** Provides real-time current/voltage data for the 30-rotor stack to the CM5 GUI.
* **Sensor:** TI INA219 Zero-Drift Power Monitor (Address: 0x45) — dedicated rotor-stack usage telemetry.
* **Placement:** Inserted on L1 (Top Layer) connected to the 3V3_ENIG rail immediately before the rotor stack.
  * Minimum 15mm isolation from Intel MAX II EPM570T100I5N CPLD logic core.
* **Shunt:** CSS2H-2512R-R010ELF (10mΩ ±1% 5A, 2512 Kelvin-sense) rotor-stack shunt resistor. Stator R1 instance. (PM R12 + PM R23 are the first and second system CSS2H; total build qty: 3 — see `Power_Budgets.md`.)
* **Interface:** I2C-1 Telemetry Bus (via `J5`, shared with the Power Module and Settings Board).
* **Filtering:** 0.1µF decoupling and RC filter on IN+/IN- for noise suppression from mechanical rotors.

## 6. EMI & Mechanical

* **Shield Mount:** No local `GND_CHASSIS` landing strip is implemented on the Stator; any internal
  cable clamping or shielding features remain within the signal/power GND domain unless a later
  EMC-focused decision explicitly introduces a justified exception.
* **Clamping:** Dual 3.2mm PTH anchors per cable for Galvanised Steel Bar compression.

---

## 7. PCB Fabrication & Stackup

* **Manufacturer:** JLCPCB
* **Layer count:** 4-layer
* **Stackup:** JLC04161H-7628
* **Board thickness:** 1.6mm
* **Copper weight:** 2oz outer / 0.5oz inner
* **Surface finish:** ENIG
* **Min trace/space:** 0.1mm / 0.1mm
* **Min drill:** 0.2mm

## 8. Thermal & ESD

* **Thermal:** No active cooling required. Low-power passive components only. Relies on chassis airflow.
* **ESD:** TVS diode protection on external-facing signal lines. All connectors include GND guard pins per Samtec ERF8/ERM8 pinout.

## 9. Bill of Materials

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C1-C8 | Decoupling (8 per CPLD) | 0.1µF X7R 50V | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 |
| C9-C13 | Bulk entry decoupling bank (star/spoke) | 10uF X7R 50V | 1206 | 187-CL31B106KBHNNNE | 1276-6767-1-ND | C89632 |
| J1-J3 | Rotor 1 interface sockets (1 slot × 3 connectors: JTAG ERF8-005, Power ERF8-005, ENC ERF8-010) — cross-ref Rotor/Design_Spec.md §3.4 | ERF8-005 (J1+J2) / ERF8-010 (J3) | SMT 0.8mm pitch | 200-ERF8005050SDVKTR (J1+J2) / 200-ERF8010050SDVKTR (J3) | SAM13517CT-ND (J1+J2 CT) / SAM8618CT-ND (J3 CT) | C7273978 (J1+J2) / C3646170 (J3) |
| J4-J9 | Encoder port connectors (×6 positions: `KBD_ENC`, `LBD_DEC`, `PLG_PASS1_DEC`, `PLG_PASS1_ENC`, `PLG_PASS2_DEC`, `PLG_PASS2_ENC`) | Adam Tech BHR-20-VUA / 2BHR-20-VUA — 20-pin 2×10 2.54mm shrouded | through-hole | 737-BHR-20-VUA | 2057-BHR-20-VUA-ND | C17340054 |
| J10 | 16-pin Reflector/Extension port | Adam Tech BHR-16-VUA — 16-pin 2×8 2.54mm shrouded | through-hole | 737-BHR-16-VUA | 2057-BHR-16-VUA-ND | C17692295 |
| J11, J12 | Controller dock hybrid plugs (5V-biased + 3V3/JTAG/I2C) | Molex 2195620015 | 5 power + 15 signal hybrid plug | 538-219562-0015 | 900-2195620015-ND | Global sourcing / consignment |
| J13 | Settings Board I²C connector (6-pin JST PH 2.0mm) | JST B6B-PH-K-S(LF)(SN) | THT | 306-B6B-PH-K-SLFSN | 455-1708-ND | C131342 |
| L1-L4 | Rotor rail ferrite bead bank | 120 Ω @100 MHz, 4.0A | 1206 | 875-HI1206P121R-10 | 240-2410-1-ND | C2442103 |
| R1 | Rotor-Stack Shunt Resistor (CSS2H — Stator R1; PM R12 LTC3350 RSENSE and PM R23 INA219 U12 are first and second system instances, total build qty: 3) | CSS2H-2512R-R010ELF (10mΩ ±1% 5A) | 2512 Kelvin | 652-CSS2H-2512R-R010ELF | CSS2H-2512R-R010ELF-ND | — |
| R2 | JTAG TTD_RETURN pull-up | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KHCT-ND | C191124 |
| R3 | TMS pull-up to 3V3_ENIG | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KHCT-ND | C191124 |
| R4 | TDI pull-up to 3V3_ENIG | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KHCT-ND | C191124 |
| R5 | TCK pull-down to GND | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KHCT-ND | C191124 |
| R6 | SYS_RESET_N pull-up to 3V3_ENIG | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KHCT-ND | C191124 |
| R7-R12 | TCK series resistors -> J4/J5/J6/J7/J8/J9 encoder ports (×6) | 75Ω (1%) | 0603 | 667-ERJ-3EKF75R0V | P75.0HCT-ND | C403349 |
| R33-R38 | TMS series resistors -> J4/J5/J6/J7/J8/J9 encoder ports (×6) | 75Ω (1%) | 0603 | 667-ERJ-3EKF75R0V | P75.0HCT-ND | C403349 |
| R16 | `CFG_ROUTE[0]` pull-down to GND | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KHCT-ND | C191124 |
| R17 | `CFG_ROUTE[1]` pull-down to GND | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KHCT-ND | C191124 |
| R18 | `CFG_ROUTE[2]` pull-down to GND | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KHCT-ND | C191124 |
| R19 | `CFG_ROUTE[3]` pull-down to GND | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KHCT-ND | C191124 |
| R20 | `CFG_APPLY_N` pull-up to 3V3_ENIG (keeps the Stator-only apply/reset pulse inactive HIGH until U_EXP4 actively asserts LOW) | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KHCT-ND | C191124 |
| R21-R26 | `CFG_REFMAP[5:0]` CPLD config input pull-down resistors (×6) | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KHCT-ND | C191124 |
| R27-R32 | TDI chain series resistors: CPLD->J4->J5->J6->J7->J8->J9 (×6 driven segments) | 75Ω (1%) | 0603 | 667-ERJ-3EKF75R0V | P75.0HCT-ND | C403349 |
| SW1 | Routing configuration selector | ~~Removed — relocated to Settings Board~~ | — | — | — | — |
| SW2 | Reflector map selector | ~~Removed — relocated to Settings Board~~ | — | — | — | — |
| U1 | Stator Management CPLD (routing matrix + reflector map application) | EPM570T100I5N | TQFP-100 | 989-EPM570T100I5N | 544-2281-ND | C27319 |
| U2 | 3V3_ENIG Current/Voltage Sensing | INA219AIDR | **SOIC-8** | 595-INA219AIDR | 296-23978-1-ND | C138706 |
| U3 | Stator reset/apply gate (`SYS_RESET_N` AND `CFG_APPLY_N` -> CPLD `DEV_CLRN`) | SN74LVC1G08DBVR | SOT-23-5 | 595-SN74LVC1G08DBVR | 296-11601-1-ND | C7666 |
| U4-U5 | Keyboard-source mux (`KEY_CM5_ACTIVE`; physical keyboard vs `CM5_KEY_DATA[5:0]`) | 74HC157PW-Q100,118 | TSSOP-16 | 771-74HC157PWQ100118 | 1727-74HC157PW-Q100,118CT-ND | C546614 |
| U_EXP1 | MCP23017 I²C GPIO Expander (ENC monitoring) | MCP23017T-E/SO | SOIC-28 | 579-MCP23017T-E/SO | MCP23017T-E/SOCT-ND | C47023 |
| U_EXP2 | MCP23017 I²C GPIO Expander (virtual key data, SOURCE_SEL, SYS_RESET_N) | MCP23017T-E/SO | SOIC-28 | 579-MCP23017T-E/SO | MCP23017T-E/SOCT-ND | C47023 |
| U_EXP4 | MCP23017 I²C GPIO Expander (config output driver + `CFG_APPLY_N`) | MCP23017T-E/SO @ 0x22 | SOIC-28 | 579-MCP23017T-E/SO | MCP23017T-E/SOCT-ND | C47023 |
