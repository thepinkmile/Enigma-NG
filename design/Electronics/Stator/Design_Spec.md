# Stator Board (V1.0) Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-05

The Stator Board is the mechanical and electrical backbone of the rotor stack. It provides the high-current distribution and signal routing for the 30 modular rotors.

## 1. Overview

* **Stackup:** 4-Layer / 2oz Finished Copper.
* **Layer Mapping:** L1: Signal (JTAG/routing) | L2: GND | L3: 3V3_ENIG | L4: ENC Data.
* **Role:** Master Switchboard for the 30-rotor stack and peripheral encoder boards.

### Functional & Design Requirements

#### Functional Requirements

| ID | Functional Requirement | Notes | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| FR-STA-01 | Serve as the fixed mechanical and electrical backplane for the 30-rotor stack | Provides all power, JTAG, and data connectivity to rotors | §2 Core Features; BOM J1–J3 (ERF8 rotor sockets) |
| FR-STA-02 | Distribute 3V3_ENIG power to all 30 rotor slots simultaneously | Via 2oz copper pour on L3 | §2 Core Features; §3 Encryption & JTAG Hub; BOM L1–L4 (ferrite beads) |
| FR-STA-03 | Route the JTAG chain from the Controller Board through all 30 rotor slots in sequence | Serial daisy-chain; Stator CPLD is device 1 | §3 Encryption & JTAG Hub; BOM U1 (EPM570T100I5N) |
| FR-STA-04 | Receive TTD_RETURN from the Reflector and forward to the Controller Board | Via J7 (16-pin Molex) → Link-Beta pin 26 | §3 Encryption & JTAG Hub; BOM J7, R2 (10kΩ pull-up) |
| FR-STA-05 | Interface with up to 3 Encoder boards (1 HID + 2 Plugboard) via IDC ribbon cables; route 6-bit data bus to plugboard passes at configurable signal chain positions | J4 = HID; J5 = Plugboard Pass A (configurable); J6 = Plugboard Pass B (configurable) | §3 Plugboard Routing; §4 Interconnects; BOM J4–J6 (26-pin Molex IDC) |
| FR-STA-06 | Host a CPLD as the first device in the system JTAG chain | Intel MAX II EPM570 (570 LEs required for startup-loaded reflector map registers + routing matrix) | §3 Encryption & JTAG Hub; BOM U1 (EPM570T100I5N) |
| FR-STA-07 | Connect to the Controller Board via the Link-Beta BtB connector | J8 = ERM8-020 male | §4 Interconnects; BOM J8 (ERM8-020-05.0-S-DV-K-TR) |
| FR-STA-08 | Select the active plugboard routing configuration via hardware DIP switch without JTAG reprogramming | 4-position DIP switch (SW1) providing 16 pre-defined configurations; CPLD reads SW1[3:0] at power-up and selects routing case from VHDL fabric | §3 CPLD Signal Routing Matrix; BOM SW1, R16–R19 |
| FR-STA-09 | Optionally apply a stored reflector substitution map at the reflection boundary, replacing the physical Reflector board | 6-position DIP switch (SW2); SW2[5]=1 enables internal map; SW2[4:0] selects index 0–20 from 21 involutory maps stored in CPLD UFM; SW2[5]=0 passes data to J7 normally | §3 Reflector Map Configuration; BOM SW2, R20–R25 |

#### Design Requirements

| ID | Design Requirement | Specification | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| DR-STA-01 | PCB stackup | 4-layer, 2oz finished copper (JLC04161H-7628) | §7 PCB Fabrication & Stackup |
| DR-STA-02 | Layer mapping | L1 = Signal (JTAG/routing), L2 = GND, L3 = 3V3_ENIG, L4 = ENC Data | §1 Overview |
| DR-STA-03 | Rotor interface (per slot) | J1 = ERF8-005 (JTAG), J2 = ERF8-005 (Power), J3 = ERF8-010 (ENC); 1 slot set | §4 Interconnects; BOM J1–J3 (ERF8-005/ERF8-010) |
| DR-STA-04 | Encoder interface | J4/J5/J6 = 26-pin Molex IDC (HID encoder ports, one per encoder board) | §4 Interconnects; BOM J4–J6 (Molex 26-pin) |
| DR-STA-05 | TTD_RETURN input | J7 = 16-pin Molex; TTD_RETURN on pin 15 (from Reflector J4) | §3 Encryption & JTAG Hub; BOM J7 (16-pin Molex) |
| DR-STA-06 | Link-Beta connector | J8 = ERM8-020-05.0-S-DV-K-TR (40-pin male, 0.8 mm pitch) to Controller J2 | §4 Interconnects; BOM J8 (ERM8-020-05.0-S-DV-K-TR) |
| DR-STA-07 | CPLD | Intel MAX II EPM570T100I5N (TQFP-100); 570 LEs; same footprint as EPM240 (drop-in); 570 LEs required for startup-loaded 64-char reflector map (384 FFs) + routing matrix logic | §3 Encryption & JTAG Hub; BOM U1 (EPM570T100I5N) |
| DR-STA-08 | Power monitoring | INA219 current sensor; shunt R1 = CSS2H-2512R-R010ELF (10mΩ 2512 Kelvin), rated ≥2.11 A | §5 Power Telemetry; BOM U2 (INA219AIDR), R1 (CSS2H 10mΩ shunt) |
| DR-STA-09 | Maximum 3V3_ENIG load | 2.11 A worst-case (30 rotors + Stator CPLD + all encoders) | §2 Core Features; §5 Power Telemetry |
| DR-STA-10 | Routing configuration selection | SW1 = 4-position DIP switch, 2.54mm THT (binary index 0–15); 4× 10kΩ pull-down resistors R16–R19 on SW1 inputs | §3 CPLD Signal Routing Matrix; BOM SW1, R16–R19 |
| DR-STA-11 | Reflector map selection | SW2 = 6-position DIP switch, 2.54mm THT; SW2[4:0] = map index 0–20; SW2[5] = internal reflector enable; 6× 10kΩ pull-down resistors R20–R25 on SW2 inputs | §3 Reflector Map Configuration; BOM SW2, R20–R25 |

## 2. Core Features

* **Modular Slots:** 1× Samtec ERF8 female socket set (3 connectors: ERF8-005 JTAG, ERF8-005 Power, ERF8-010 ENC\_DATA) mating with the ERM8 male headers on the Rotor.
* **Power Tree:** A 2oz copper pour for the `3V3_ENIG` rail to handle the **2.11A worst-case** load without voltage sag (see `design/Electronics/Power_Budgets.md`).
  The 5A figure previously quoted was a conservative design margin; the LDO hard limit is 3.0A.

### GND_CHASSIS Single-Point Bond

Per `design/Standards/Global_Routing_Spec.md §5`, each PCB in the Enigma-NG system must have a documented single-point GND_CHASSIS bond at its power entry connector.

**Stator GND_CHASSIS bond point:** The GND_CHASSIS connection is made at the LINK-BETA connector
(J8, ERM8-020, power input from Controller Board).
A single 0 Ω bond resistor (or direct via) in a dedicated keepout zone connects the signal/power GND plane
to the chassis copper pour at this entry point. No additional chassis bonds are made on this board to avoid ground loops.

## 3. Encryption & JTAG Hub

* **CPLD:** Intel MAX II EPM570T100I5N CPLD (Logic Router & Reflector).

### CPLD Signal Routing Matrix

The Stator CPLD (U1) is the bidirectional ENC_DATA routing hub for the full encryption cycle.
It has three bidirectional ENC_DATA connector interfaces — J4 (HID), J3 (Rotor 1), and J7
(Reflector/Extension) — plus two configurable plugboard pass interfaces (J5 Plugboard A, J6
Plugboard B).

The encryption signal passes through the CPLD at three defined interception points:

| Step | CPLD receives from | Optional plugboard insertion | CPLD drives to |
| :--- | :--- | :--- | :--- |
| **1 — Forward entry** | J4 ENC_OUT[0:5] — Keyboard keystroke | Pre-Rotor 1 position — J5 or J6 | J3 ENC_IN[0:5] → Rotor 1 (starts forward pass through rotor stack) |
| **2 — Reflector return** | J7 ENC_OUT[0:5] — reflected signal returned from Reflector chain | At Reflector boundary — J5 or J6 | J7 ENC_IN[0:5] → Reflector chain → Rotor 30 (starts return pass back through rotor stack) |
| **3 — Final exit** | J3 ENC_OUT[0:5] — Rotor 1 return-pass output | Post-Rotor 1 return position — J5 or J6 | J4 ENC_IN[0:5] → Lightboard |

At each step the CPLD either passes the signal transparently (no plugboard) or routes it through
Plugboard Pass A (J5) or B (J6) before forwarding. The active insertion positions are determined by
the VHDL routing case statement selected at power-up from the SW1 DIP switch index.

#### DIP Switch Configuration (SW1)

SW1 provides a 4-bit binary index (0–15) selecting the active routing case from 16 configurations
synthesised into the CPLD fabric. No JTAG reprogramming is required to change configuration —
only a single JTAG flash at initial programming. SW1[1:0] (switches 1 & 2) encode J5 position;
SW1[3:2] (switches 3 & 4) encode J6 position. Pull-down resistors R16–R19 hold each input at
logic-0 when the corresponding switch is open.

| SW1 Index (SW4:SW3:SW2:SW1) | J5 (Plugboard A) insertion point | J6 (Plugboard B) insertion point | Historical reference |
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

#### Reflector Map Configuration (SW2)

SW2 is a 6-position DIP switch on the reflector-facing side of the Stator, read at power-up.
It controls whether the Stator CPLD applies an internal reflector substitution map at the
reflection boundary (replacing the physical Reflector board) or passes data through J7 normally.

| Bit | SW2 position | Function |
| :--- | :--- | :--- |
| `[5]` | Switch 6 | **Internal reflector enable**: 1 = apply stored map; 0 = pass through to J7 (physical Reflector) |
| `[4:0]` | Switches 5–1 | **Map index** (0–20): selects which involutory map to load from UFM at power-up |

Pull-down resistors R20–R25 hold each input at logic-0 when the corresponding switch is open
(default = SW2[5]=0, physical Reflector mode, all indices default to 0).

When SW2[5]=0, J7 ENC_IN/OUT operate normally and SW2[4:0] is ignored (no UFM load on power-up).
When SW2[5]=1, the CPLD serially reads the indexed map from UFM into internal flip-flop registers
at power-up (~40 µs). At the reflection boundary (Step 2 in the routing matrix), the CPLD applies
the loaded map combinationally instead of forwarding to J7. J7 ENC_IN/OUT remain electrically
present but are not driven or sampled by the CPLD in this mode.

SW1 (routing matrix) and SW2 (reflector mode) are fully independent; all 16 SW1 configurations
are valid regardless of the SW2 setting.

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
* **Ferrite Bead Rule:**Use **4x ferrite beads** (one per 3V3_ENIG rotor feed) between Link-Beta entry and rotor power distribution to isolate switching transients from Controller logic.
* **Current Margin Check:** Rotor rail is budgeted at **1.50A typical** (30 rotors × 50mA — see `design/Electronics/Power_Budgets.md`);
  with 4 parallel feeds this is ~**375mA per bead** nominal sharing,
  well within the **3.5A** bead rating. Total 3V3_ENIG worst case including all CPLDs and encoders: 2.11A (30% headroom vs 3.0A LDO).
* **JTAG Return:** Includes 10kΩ pull-up on TTD_RETURN at the Link-Beta exit (R2).
* **JTAG Pull Resistors (×4, placed near Stator CPLD U1):**
  * **TMS:** 10kΩ pull-up to 3V3_ENIG (R3) — ensures JTAG TAP resets to Test-Logic-Reset on power-up and when controller is idle.
  * **TDI:** 10kΩ pull-up to 3V3_ENIG (R4) — holds TDI at logic-1 (BYPASS) when not actively driven by the Controller.
  * **TCK:** 10kΩ pull-down to GND (R5) — prevents spurious clocking when TCK line is floating.
  * **SYS_RESET_N:** 10kΩ pull-up to 3V3_ENIG (R6) — active-low signal; pull-up ensures CPLD remains
    out of reset by default.
* **JTAG Trace Width Rule:** All JTAG signal traces on L1 (TCK, TMS, TDI, TDO, SYS_RESET_N) shall
  be routed at **0.127 mm (5 mil)** width over the L2 GND plane, targeting **50 Ω controlled
  impedance**. See `design/Electronics/Investigations/JTAG_Integrity.md` and DEC-016.
* **JTAG Series Termination at Encoder Port Outputs (R7–R15):** 75 Ω series resistors placed within
  2 mm of each J4/J5/J6 connector pad **on the Stator PCB**, targeting 95 Ω source impedance to match the ~100 Ω IDC
  ribbon cable:
  * **R7, R8, R9:** TCK → J4, J5, J6 respectively.
  * **R10, R11, R12:** TMS → J4, J5, J6 respectively.
  * **R13:** Stator CPLD TDO → J4 TDI (HID encoder cable drive). Placed on Stator within 2 mm of J4 pin 13.
  * **R14:** J4 TDO return → J5 TDI (Plugboard A cable drive). Placed on Stator within 2 mm of J5 pin 13, on the
    trace carrying J4's TDO return signal.
  * **R15:** J5 TDO return → J6 TDI (Plugboard B cable drive). Placed on Stator within 2 mm of J6 pin 13, on the
    trace carrying J5's TDO return signal.
  * All R13–R15 are **Stator-side** resistors — no series resistors are required at the Encoder cable inputs.
* **Reset:** Pin 100 (DEV_CLRN) tied to the global SYS_RESET_N rail.

## 4. Interconnects

* **Controller Link (Link-Beta):** The **40-pin ERM8-020-05.0-S-DV-K-TR** male header on the Stator Board plugs into the matching ERF8-020 female socket on the Controller Board.
  * **Data In:** Receives JTAG, Reset from Controller.
  * **Data Out:** Transmits 12-bit Sniffer data to Controller.
  * **Power:** Receives 3V3_ENIG via the Controller pass-through for all backplane CPLDs.
  * **Cross-ref:** See `Controller/Design_Spec.md` Link-Beta mapping for explicit pin-number allocation; this Stator document mirrors that mapping for compatibility and implementation validation.
* **Encoder Interconnects:** 26-pin (2×13) 2.54mm Shrouded Box Headers (Power, ENC_DATA, JTAG).
* **Plugboard Routing — Configurable Signal Chain Positions:**
  The Stator CPLD implements a configurable routing matrix (see §3 CPLD Signal Routing Matrix) with
  three plugboard insertion positions in the full encryption cycle. The active configuration is
  selected at power-up by SW1 (4-position DIP switch, 16 pre-defined configurations — no JTAG
  reprogramming required for configuration changes). Each of the three Encoder ports plays a fixed
  or configurable role:

  | Port | Default role | Plugboard signal chain position |
  | :--- | :--- | :--- |
  | **J4** | HID — Keyboard & Lightboard | Fixed: HID interface (not used for plugboard passes) |
  | **J5** | Plugboard Pass A | Configurable: pre-Rotor 1 / At Reflector / post-Rotor 1 return (set by SW1[1:0]) |
  | **J6** | Plugboard Pass B | Configurable: pre-Rotor 1 / At Reflector / post-Rotor 1 return (set by SW1[3:2]) |

  The Stator CPLD implements all 16 configurations as synthesised VHDL case logic. See
  `design/Electronics/Stator/Board_Layout.md` and `design/Electronics/Encoder/Design_Spec.md §1`
  for further detail.
* **Reflector/Extension Interconnect:**16-pin (2x8) Vertical Shrouded Header (Power, ENC_DATA, TTD_RETURN).
  * **Routing:** Cables secured to the chassis floor with conductive EMI tape.
  * Extension boards enable daisy chaining this interconnect (to enable multi-stack rotor configurations).
  * **Cross-ref:** For matching interconnect pinouts on power (3V3_ENIG/GND), ENC_IN/ENC_OUT, and JTAG TTD_RETURN lines used for reflector loopback/plugboard mapping, See:
    * `Extension/Design_Spec.md`
    * `Reflector/Design_Spec.md`
  * **ENC_DATA (bidirectional — simultaneous):** J7 carries ENC_DATA on two separate pin groups
    simultaneously. ENC_OUT[0:5] (pins 9–14): returns the reflected signal from the Reflector chain
    to the Stator CPLD (Step 2 receive in the routing matrix). ENC_IN[0:5] (pins 3–8): carries the
    return-pass signal driven by the Stator CPLD back to the Reflector chain after optional plugboard
    insertion (Step 2 drive — starts the return pass through the rotor stack).
* **Rotor Interconnect:** The Stator provides 1 rotor slot (Rotor 1 input side) using 3 ERF8 female sockets.
  * **JTAG:** ERF8-005-05.0-S-DV-K-TR (10-pin 2×5, 0.8mm pitch) — TCK, TMS, TTD (TDI function on input side),
    SYS\_RESET\_N with interleaved GND. **J1 pin 6 = TTD** (outgoing TDI to Rotor 1).
    Pin 10 = spare/GND (TDO does NOT return via this connector — it returns via J7 pin 15).
  * **Power:** ERF8-005-05.0-S-DV-K-TR (10-pin 2×5, 0.8mm pitch) — 5× 3V3\_ENIG, 5× GND. Same part as JTAG socket.
  * **ENC DATA (bidirectional):** ERF8-010-05.0-S-DV-K-TR (20-pin 2×10, 0.8mm pitch) —
    ENC_IN\[0:5\] (CPLD drives to Rotor 1, forward pass — Step 1 drive);
    ENC_OUT\[0:5\] (CPLD receives from Rotor 1, return pass — Step 3 receive); 8× GND fill.
  * **Cross-ref:** Authoritative pinout is defined in `Rotor/Design_Spec.md §3.4` (DEC-018 ownership).
  * **Note:** Rotor-to-rotor connections beyond Rotor 1 are direct (each Rotor J4/J5/J6 output mates with
    the next Rotor J1/J2/J3 input); Extension boards provide inter-group bridging at group boundaries in
    the serial chain (Stator → Rotor 1 → … → Rotor 30 → Reflector J1–J3).
* **Diagnostics:** 2x10 ENIG Gold Diagnostic Looped Probe Pad Bank (L1, Mirror of Controller).

### 4.1 Prototype Bench-Testing Provision (Break-Off Coupons)

The board panel includes **4 break-off PCB coupons** attached by mousebite perforations. Each coupon
fans out the 0.8mm pitch Samtec pads to a standard **2.54mm pitch shrouded IDC box header**, permitting
standard ribbon cable assemblies to be used for bench testing. For final production the coupons are
snapped off.

| Coupon | Connector | IDC Header | Signal |
| :--- | :--- | :--- | :--- |
| 1 | J8 — ERM8-020 (40-pin male) | 2×20 IDC box header, 2.54mm | Link-Beta (Controller) |
| 2 | J1 Slot 1 — ERF8-005 (10-pin female) | 2×5 IDC box header, 2.54mm | Rotor 1 JTAG/Power out |
| 3 | J2 Slot 1 — ERF8-005 (10-pin female) | 2×5 IDC box header, 2.54mm | Rotor 1 Power out |
| 4 | J3 Slot 1 — ERF8-010 (20-pin female) | 2×10 IDC box header, 2.54mm | Rotor 1 ENC Data out |

> Coupons 2–4 cover Rotor Slot 1 only (J1–J3 first instance); sufficient for single-rotor bench
> integration testing. IDC part numbers and coupon PCB fanout geometry to be defined at schematic/layout phase.

## 5. Power Telemetry (The "Encryption Load")

* **Purpose:** Provides real-time current/voltage data for the 30-rotor stack to the CM5 GUI.
* **Sensor:** TI INA219 Zero-Drift Power Monitor (Address: 0x45) — dedicated rotor-stack usage telemetry.
* **Placement:** Inserted on L1 (Top Layer) connected to the 3V3_ENIG rail immediately before the rotor stack.
  * Minimum 15mm isolation from Intel MAX II EPM570T100I5N CPLD logic core.
* **Shunt:** CSS2H-2512R-R010ELF (10mΩ ±1% 5A, 2512 Kelvin-sense) rotor-stack shunt resistor. Stator R1 instance. (PM R12 + PM R23 are the first and second system CSS2H; total build qty: 3 — see `Power_Budgets.md`.)
* **Interface:** I2C-1 Telemetry Bus (via Link-Beta, Shared with Power Module).
* **Filtering:** 0.1µF decoupling and RC filter on IN+/IN- for noise suppression from mechanical rotors.

## 6. EMI & Mechanical

* **Shield Mount:** 10mm ENIG Gold landing strip on L1 edge bonded to GND_CHASSIS.
* **Clamping:** Dual 3.2mm PTH anchors per cable for Galvanised Steel Bar compression.
* **Diagnostics:** 2x10 ENIG Gold Looped Probe Pad Bank mirrored to Controller's Bank-Beta pinout for A-B signal verification.

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
| J4-J6 | Encoder port connectors (×3 positions: HID J4 + Plugboard A J5 + Plugboard B J6) ⚠️ **Part number does not match description — connector spec requires re-review** | 26-pin 2×13 2.54mm shrouded | through-hole | TBD | TBD | TBD |
| J7 | 16-pin Reflector/Extension port ⚠️ **Part number does not match description — connector spec requires re-review** | 2x8 2.54mm shrouded | through-hole | TBD | TBD | TBD |
| J8 | Link-Beta Connector (MALE header — mates with ERF8-020 female socket on Controller) | ERM8-020-05.0-S-DV-K-TR | 40-pin | 200-ERM8020050SDVKTR | SAM8611CT-ND (CT) / SAM8611TR-ND (T&R) / SAM8611DKR-ND (DKR) | C138400 |
| L1-L4 | Rotor rail ferrite bead bank | 120 Ω @100 MHz, 4.0A | 1206 | 875-HI1206P121R-10 | 240-2410-1-ND | C2442103 |
| R1 | Rotor-Stack Shunt Resistor (CSS2H — Stator R1; PM R12 LTC3350 RSENSE and PM R23 INA219 U12 are first and second system instances, total build qty: 3) | CSS2H-2512R-R010ELF (10mΩ ±1% 5A) | 2512 Kelvin | 652-CSS2H-2512R-R010ELF | CSS2H-2512R-R010ELF-ND | — |
| R2 | JTAG TTD_RETURN pull-up | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R3 | TMS pull-up to 3V3_ENIG | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R4 | TDI pull-up to 3V3_ENIG | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R5 | TCK pull-down to GND | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R6 | SYS_RESET_N pull-up to 3V3_ENIG | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R7 | TCK series R → J4 encoder port | 75Ω (1%) | 0603 | 667-ERJ-3EKF75R0V | P75.0BYCT-ND | C105905 |
| R8 | TCK series R → J5 encoder port | 75Ω (1%) | 0603 | 667-ERJ-3EKF75R0V | P75.0BYCT-ND | C105905 |
| R9 | TCK series R → J6 encoder port | 75Ω (1%) | 0603 | 667-ERJ-3EKF75R0V | P75.0BYCT-ND | C105905 |
| R10 | TMS series R → J4 encoder port | 75Ω (1%) | 0603 | 667-ERJ-3EKF75R0V | P75.0BYCT-ND | C105905 |
| R11 | TMS series R → J5 encoder port | 75Ω (1%) | 0603 | 667-ERJ-3EKF75R0V | P75.0BYCT-ND | C105905 |
| R12 | TMS series R → J6 encoder port | 75Ω (1%) | 0603 | 667-ERJ-3EKF75R0V | P75.0BYCT-ND | C105905 |
| R13 | TDI chain: Stator CPLD TDO → J4 TDI | 75Ω (1%) | 0603 | 667-ERJ-3EKF75R0V | P75.0BYCT-ND | C105905 |
| R14 | TDI chain: J4 TDO return → J5 TDI | 75Ω (1%) | 0603 | 667-ERJ-3EKF75R0V | P75.0BYCT-ND | C105905 |
| R15 | TDI chain: J5 TDO return → J6 TDI | 75Ω (1%) | 0603 | 667-ERJ-3EKF75R0V | P75.0BYCT-ND | C105905 |
| R16 | SW1[0] (switch 1) pull-down to GND | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R17 | SW1[1] (switch 2) pull-down to GND | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R18 | SW1[2] (switch 3) pull-down to GND | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R19 | SW1[3] (switch 4) pull-down to GND | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R20 | SW2[0] (switch 1) pull-down to GND | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R21 | SW2[1] (switch 2) pull-down to GND | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R22 | SW2[2] (switch 3) pull-down to GND | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R23 | SW2[3] (switch 4) pull-down to GND | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R24 | SW2[4] (switch 5) pull-down to GND | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| R25 | SW2[5] (switch 6 — internal reflector enable) pull-down to GND | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| SW1 | Routing configuration selector | CTS 219-4LPST — 4-position DIP switch, 2.54mm THT | Through-hole | 774-219-4LPST | CT2064-ND | C128947 |
| SW2 | Reflector map selector / internal reflector enable | CTS 219-6LPST — 6-position DIP switch, 2.54mm THT | Through-hole | 774-219-6LPST | TBD | TBD |
| U1 | Stator Management CPLD (routing matrix + optional internal reflector) | EPM570T100I5N | TQFP-100 | 989-EPM570T100I5N | 544-2281-ND | C27319 |
| U2 | 3V3_ENIG Current/Voltage Sensing | INA219AIDR | **SOIC-8** | 595-INA219AIDR | 296-23978-1-ND | C138706 |
