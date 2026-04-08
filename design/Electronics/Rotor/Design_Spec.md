# Rotor Board (V1.0) Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-05

## 1. Overview

The Enigma-NG uses a 30-rotor stack. Unlike the original mechanical rotors, these are **Smart Digital Rotors**
where the internal scrambled wiring is emulated by a dedicated logic chip on each module.
The outer rotating mechanism works like the outer ring of a bearing around the central static ring (this is the rotor PCB and enclosure).
There are also sensors used to detect the current position of the outer ring using a single-track grey encoder.

### Functional & Design Requirements

#### Functional Requirements

| ID | Functional Requirement | Notes | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| FR-ROT-01 | Emulate the substitution cipher wiring of a historical Enigma rotor in real-time | Supports Rotors I–VIII, Beta, Gamma wiring tables | §2.2 Logic & Transposition; BOM U1 (EPM240T100I5N) |
| FR-ROT-02 | Detect rotor angular position using a contactless magnetic encoder | 6-bit resolution; detects between-character positions | §2.1 Position Sensing; BOM U2 (AS5600) |
| FR-ROT-03 | Pass JTAG chain signals to the next rotor in the stack (or to the Reflector at position 30) | Serial daisy-chain; each rotor is one JTAG device | §3.3 Signal Integrity; BOM J1 (ERM8-005 JTAG in), J4 (ERF8-005 JTAG out) |
| FR-ROT-04 | Receive 3V3_ENIG power from the upstream board and forward to the downstream board | Passive power pass-through via J2/J5 | §3.1 Power Management; BOM J2 (ERM8-005 power in), J5 (ERF8-005 power out) |
| FR-ROT-05 | Pass the encoder data bus through the rotor stack transparently | Via J3/J6 (ERM8-010 / ERF8-010) | §3.2 Communication Bus; BOM J3 (ERM8-010), J6 (ERF8-010) |
| FR-ROT-06 | Be individually removable for maintenance or reconfiguration without tools | Samtec ERM8/ERF8 high-cycle connectors | §2.3 Mechanical Details; BOM J1–J6 (Samtec ERM8/ERF8) |

#### Design Requirements

| ID | Design Requirement | Specification | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| DR-ROT-01 | PCB stackup | 4-layer, 2oz finished copper (JLC04161H-7628) | §4 PCB Fabrication & Stackup |
| DR-ROT-02 | CPLD | Intel MAX II EPM240T100I5N (TQFP-100); emulates 64×64 cross-wiring | §2.2 Logic & Transposition; BOM U1 (EPM240T100I5N) |
| DR-ROT-03 | Position sensor | AMS AS5600 magnetic encoder (6-bit resolution, contactless) | §2.1 Position Sensing; BOM U2 (AS5600) |
| DR-ROT-04 | Input connectors | J1 = ERM8-005 (JTAG in), J2 = ERM8-005 (Power in), J3 = ERM8-010 (ENC in) | §3.4 Connector Pinouts; BOM J1–J3 |
| DR-ROT-05 | Output connectors | J4 = ERF8-005 (JTAG out), J5 = ERF8-005 (Power out), J6 = ERF8-010 (ENC out) | §3.4 Connector Pinouts; BOM J4–J6 |
| DR-ROT-06 | Power consumption | ≤50 mA per rotor from 3V3_ENIG | §3.1 Power Management |
| DR-ROT-07 | Stack quantity | 30 rotor boards in the complete system | §1 Overview |
| DR-ROT-08 | Mechanical retention | 2× M2.5 alignment holes; retained by central threaded rod through all 30 rotors | §2.3 Mechanical Details |

## 2. Core Design

### 2.1 Position Sensing (The "Zero-Wear" System)

* **Sensor:** [AS5600 Magnetic Encoder](https://www.ams-osram.com).
* **Decision:** We avoid mechanical wipers/brushes (the main failure point of original Enigmas) in favour of contactless magnetic sensing.
* **Precision:** 6-bit resolution allows the CM5 to detect if a rotor is "between" characters and flag a mechanical jam.

### 2.2 Logic & Transposition

* **Logic:** The **Intel MAX II EPM240T100I5N CPLD** emulates the 64x64 cross-wiring.
* Decoupling and bulk entry capacitor requirements per `design/Standards/Global_Routing_Spec.md §3`.
* **Role:**Performs the instantaneous dual 6-bit parallel transposition (substitution cipher) for the forward and backward signal paths.
* **Memory:** Stores the 26-position wiring table for any historical rotor (I-VIII, Beta, Gamma) selectable via the CM5.
* **Latency:** Sub-10ns transposition time, ensuring the entire 30-rotor "trip" happens well within one CPU clock cycle.
* **Configuration:** CM5 loads the "Rotor Type" (e.g., Rotor I, II, III) into the CPLD's SRAM at boot via the JTAG Chain.

### 2.3 Mechanical Details

* **Mounting:** Each rotor PCB has two **M2.5 alignment holes**.
* **Retention:** Once slotted into the Stator, a **threaded rod** (mimicking the original Enigma spindle) passes through the center of all 30 rotors to lock them into a single, rigid block.
* **Hot-Swappable:** The Samtec ERM8 Edge-Rate connectors are rated for high mating cycles, allowing individual rotors to be pulled for "repair" or reconfiguration without tools.
* **Connector Configuration:** Each rotor carries **3 separate ERM8 connectors** (JTAG, Power, ENC\_DATA) mating into matching ERF8 female sockets on the Stator.
  Physical separation of connector types provides keying — it is mechanically impossible to mismate a power connector into a JTAG socket.

## 3. Electrical Requirements

### 3.1 Power Management

* **Input:** 3.3V/**50mA per rotor** (sourced from the **Power Module** 3V3_ENIG rail, routed through Controller Board → Stator Board → Rotor stack via Link-Beta).
  See `design/Electronics/Power_Budgets.md` for full budget — 30 rotors draw 1.50A typical; the 150mA/rotor figure previously used was a conservative overestimate.
* **Filtering:** Local **10uF X7R** bulk entry bank on each rotor; upstream rail filtering uses the **Stator ferrite bead bank** to suppress stack switching noise.
* Decoupling and bulk entry capacitor requirements per `design/Standards/Global_Routing_Spec.md §3`.

### 3.2 Communication Bus

* **The ENC Data Path:** The 12-bit parallel cipher bus (ENC_IN[0:5] / ENC_OUT[0:5]) passes through every
  rotor as a daisy-chain: Stator → Rotor 1 → … → Rotor 30 → Reflector (cipher data only; this path is
  entirely separate from JTAG TTD_RETURN).
* **JTAG TTD_RETURN Path:** After the Reflector processes the cipher reversal, TTD_RETURN travels
  separately: Reflector J4 → Stator J7 → Link-Beta pin 26 → FT232H on JDB (JTAG chain closure only).
* **Control:** Shared I2C bus for position telemetry.
* **JTAG:** Pass-through JTAG lines allow the **USB Blaster** on the Controller Board to program the entire 30-rotor stack in one "daisy-chain" operation.

### 3.3 Signal Integrity

* **Impedance:** 50Ω single-ended traces for JTAG and data lines to prevent reflections.
* **Layer Stack (4-Layer DEC-017):**
  * **L1:** Signal (JTAG routing + data traces). JTAG traces run on L1 over L2 GND plane.
  * **L2:** GND plane (solid, contiguous) — provides reference for L1 controlled-impedance traces.
  * **L3:** 3V3_ENIG power plane — provides local decoupling reference.
  * **L4:** Signal (secondary routing + data plate silkscreen on bottom).
* **JTAG Trace Width Rule:** All JTAG signal traces on L1 shall be routed at **0.127 mm (5 mil)**
  width over the L2 GND plane, targeting **50 Ω controlled impedance** per the JLC04161H-7628
  stackup (h=0.087mm, t=0.035mm, Eᵣ=4.4). See `design/Electronics/Investigations/JTAG_Integrity.md §3.1`
  for the copper-weight note (2oz finished uses 1oz base copper t=0.035mm in the IPC-2141A formula) and DEC-016.
* **Series Termination — TDO Output (R1, 75Ω):** Placed within 2 mm of CPLD TDO pin, on the
  trace to J4 pin 6 (TTD output side). Source impedance ≈ 95 Ω, targeting the ~100 Ω inter-rotor segment on the
  Stator PCB. Consistent with Encoder R8 (DEC-016). One resistor per rotor board.
* **Pull Resistors (R2–R5, 10kΩ, per CPLD):**
  * **TMS (R2):** 10kΩ pull-up to 3V3_ENIG — ensures JTAG TAP resets to Test-Logic-Reset on power-up.
  * **TDI (R3):** 10kΩ pull-up to 3V3_ENIG — holds TDI at logic-1 (BYPASS) when not actively driven.
  * **TCK (R4):** 10kΩ pull-down to GND — prevents spurious clocking when TCK is floating.
  * **SYS\_RESET\_N (R5):** 10kΩ pull-up to 3V3_ENIG — active-low; pull-up holds CPLD out of reset by default.
  These are present on every rotor board. With 30 rotors, 30 sets of pull resistors exist in the full stack;
  this is intentional and consistent with making each rotor independently safe in any stack position.
* **Shielding:** 4-layer PCB with solid GND plane (L2) to isolate digital switching from the high-accuracy magnetic encoder.

### 3.4 Connector Pinouts (Rotor Interface — Authority Document)

> This section is the **authoritative pinout definition** for all Rotor-to-Stator connectors.
> All other boards (Stator) cross-reference this section. See DEC-018 for ownership rationale.

#### J1 — JTAG Interface (ERM8-005, 10-pin 2×5, 0.8mm pitch)

| Pin | Row A | Pin | Row B |
| :--- | :--- | :--- | :--- |
| 1 | GND | 2 | TCK |
| 3 | GND | 4 | TMS |
| 5 | GND | 6 | TTD |
| 7 | GND | 8 | SYS\_RESET\_N |
| 9 | GND | 10 | spare/GND |

> **TTD Net Name:** The JTAG serial chain data pin is designated **TTD** (JTAG Transmission Data) at pin 6
> on both input and output connectors. On J1 (input side), TTD carries incoming TDI; on J4 (output side),
> TTD carries outgoing TDO to the next rotor's TDI. This unified net name avoids the TDI/TDO direction
> confusion when viewing connector pinouts in isolation. Consistent with the T-prefix JTAG signal naming
> convention (TCK, TMS, TDI, TDO → TTD).

#### J2 — Power Interface (ERM8-005, 10-pin 2×5, 0.8mm pitch)

| Pin | Row A | Pin | Row B |
| :--- | :--- | :--- | :--- |
| 1 | 3V3\_ENIG | 2 | GND |
| 3 | 3V3\_ENIG | 4 | GND |
| 5 | 3V3\_ENIG | 6 | GND |
| 7 | 3V3\_ENIG | 8 | GND |
| 9 | 3V3\_ENIG | 10 | GND |

> 5 pins × 2.2 A/pin = **11.0 A capacity** — far exceeds the 50 mA/rotor requirement.
> 5 power + 5 GND ensures fully balanced current return paths.

#### J3 — Encoder Data Interface (ERM8-010, 20-pin 2×10, 0.8mm pitch)

| Pin | Row A | Pin | Row B |
| :--- | :--- | :--- | :--- |
| 1 | ENC\_IN\[0\] | 2 | ENC\_OUT\[0\] |
| 3 | ENC\_IN\[1\] | 4 | ENC\_OUT\[1\] |
| 5 | ENC\_IN\[2\] | 6 | ENC\_OUT\[2\] |
| 7 | ENC\_IN\[3\] | 8 | ENC\_OUT\[3\] |
| 9 | ENC\_IN\[4\] | 10 | ENC\_OUT\[4\] |
| 11 | ENC\_IN\[5\] | 12 | ENC\_OUT\[5\] |
| 13 | GND | 14 | GND |
| 15 | GND | 16 | GND |
| 17 | GND | 18 | GND |
| 19 | GND | 20 | GND |

> 12 signal pins + 8 GND fill pins. All spare pins assigned as GND for improved EMI shielding
> and signal return paths around the encoder data bus.

#### J4 — JTAG Interface Output (ERF8-005, 10-pin 2×5, 0.8mm pitch, FEMALE socket)

Mates with the next rotor's J1 (ERM8-005 male header) or Reflector J1.

| Pin | Row A | Pin | Row B |
| :--- | :--- | :--- | :--- |
| 1 | GND | 2 | TCK |
| 3 | GND | 4 | TMS |
| 5 | GND | 6 | TTD |
| 7 | GND | 8 | SYS\_RESET\_N |
| 9 | GND | 10 | spare/GND |

> Pin 6 = TTD (CPLD TDO output — feeds next stage's J1 pin 6 TTD input). Pin 10 = spare/GND (no TTD_RETURN path here; return travels via Reflector → Extension Port → Stator J7).

#### J5 — Power Interface Output (ERF8-005, 10-pin 2×5, 0.8mm pitch, FEMALE socket)

Mates with the next rotor's J2 (ERM8-005 male header) or Reflector J2.

| Pin | Row A | Pin | Row B |
| :--- | :--- | :--- | :--- |
| 1 | 3V3\_ENIG | 2 | GND |
| 3 | 3V3\_ENIG | 4 | GND |
| 5 | 3V3\_ENIG | 6 | GND |
| 7 | 3V3\_ENIG | 8 | GND |
| 9 | 3V3\_ENIG | 10 | GND |

> Power pass-through from J2 input side. 3V3_ENIG and GND rails continue to the next rotor in the stack.

#### J6 — Encoder Data Interface Output (ERF8-010, 20-pin 2×10, 0.8mm pitch, FEMALE socket)

Mates with the next rotor's J3 (ERM8-010 male header) or Reflector J3.

| Pin | Row A | Pin | Row B |
| :--- | :--- | :--- | :--- |
| 1 | ENC\_IN\[0\] | 2 | ENC\_OUT\[0\] |
| 3 | ENC\_IN\[1\] | 4 | ENC\_OUT\[1\] |
| 5 | ENC\_IN\[2\] | 6 | ENC\_OUT\[2\] |
| 7 | ENC\_IN\[3\] | 8 | ENC\_OUT\[3\] |
| 9 | ENC\_IN\[4\] | 10 | ENC\_OUT\[4\] |
| 11 | ENC\_IN\[5\] | 12 | ENC\_OUT\[5\] |
| 13 | GND | 14 | GND |
| 15 | GND | 16 | GND |
| 17 | GND | 18 | GND |
| 19 | GND | 20 | GND |

> ENC pass-through from J3 input side. Signal positions are identical — pin mapping is symmetric so the same CPLD logic applies regardless of stack position.

## 4. PCB Fabrication & Stackup

* **Layers:** 4-Layer (JLC04161H-7628).
* **Finish:** ENIG (Gold) for the edge-rate connector pads.
* **Aesthetics:** Dark Green Solder Mask with Typewriter font labeling (e.g., "WALZE I").

---

## 5. Bill of Materials

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C1-C8 | Decoupling (8 per CPLD) | 0.1µF X7R 50V | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 |
| C9-C13 | Bulk entry decoupling bank (star/spoke) | 10uF X7R 50V | 1206 | 187-CL31B106KBHNNNE | 1276-6767-1-ND | CL31B106KBHNNNE |
| J1 | JTAG Interface Connector (MALE header — mates with ERF8-005 female socket on Stator) | ERM8-005-05.0-S-DV-K-TR | 10-pin (2×5) 0.8mm pitch | 200-ERM8005050SDVKTR | 612-ERM8-005-05.0-S-DV-K-TRCT-ND | C3649741 |
| J2 | Power Interface Connector (MALE header — mates with ERF8-005 female socket on Stator) | ERM8-005-05.0-S-DV-K-TR | 10-pin (2×5) 0.8mm pitch | 200-ERM8005050SDVKTR | 612-ERM8-005-05.0-S-DV-K-TRCT-ND | C3649741 |
| J3 | Encoder Data Interface Connector (MALE header — mates with ERF8-010 female socket on Stator) | ERM8-010-05.0-S-DV-K-TR | 20-pin (2×10) 0.8mm pitch | 200-ERM8010050SDVKTR | SAM8610CT-ND | C374877 |
| J4 | JTAG Interface Output Connector (FEMALE socket — mates with ERM8-005 male header on next Rotor J1 or Reflector J1) | ERF8-005-05.0-S-DV-K-TR | 10-pin (2×5) 0.8mm pitch | 200-ERF8005050SDVKTR | SAM13517CT-ND | C7273978 |
| J5 | Power Interface Output Connector (FEMALE socket — mates with ERM8-005 male header on next Rotor J2 or Reflector J2) | ERF8-005-05.0-S-DV-K-TR | 10-pin (2×5) 0.8mm pitch | 200-ERF8005050SDVKTR | SAM13517CT-ND | C7273978 |
| J6 | Encoder Data Interface Output Connector (FEMALE socket — mates with ERM8-010 male header on next Rotor J3 or Reflector J3) | ERF8-010-05.0-S-DV-K-TR | 20-pin (2×10) 0.8mm pitch | 200-ERF8010050SDVKTR | SAM8618CT-ND | C3646170 |
| R1 | JTAG TDO output series termination (CPLD TDO → J4 pin 6, TTD output) | 75Ω 1% | 0402 | 667-ERJ-2RKF75R0X | P75.0LCT-ND | C413061 |
| R2 | TMS pull-up to 3V3_ENIG | 10kΩ 1% | 0402 | 667-ERJ-2RKF1002X | P10.0KLBCT-ND | C25744 |
| R3 | TDI pull-up to 3V3_ENIG | 10kΩ 1% | 0402 | 667-ERJ-2RKF1002X | P10.0KLBCT-ND | C25744 |
| R4 | TCK pull-down to GND | 10kΩ 1% | 0402 | 667-ERJ-2RKF1002X | P10.0KLBCT-ND | C25744 |
| R5 | SYS_RESET_N pull-up to 3V3_ENIG | 10kΩ 1% | 0402 | 667-ERJ-2RKF1002X | P10.0KLBCT-ND | C25744 |
| U1 | Intel MAX II CPLD | EPM240T100I5N | TQFP-100 | 989-EPM240T100I5N | 544-2276-ND | C40067 |
| U2 | Magnetic encoder | AS5600 | DFN-8 | 985-AS5600-ASOM | 620-1984-1-ND | C123471 |
