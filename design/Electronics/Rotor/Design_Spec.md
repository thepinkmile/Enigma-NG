# Rotor Detailed Design

**Status:** Draft
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-04

## 1. Overview

The Enigma-NG uses a 30-rotor stack. Unlike the original mechanical rotors, these are **Smart Digital Rotors** where the internal scrambled wiring is emulated by a dedicated logic chip on each module.
The outer rotating mechanism works like the outer ring of a bearing around the central static ring (this is the rotor PCB and enclosure).
There are also sensors used to detect the current position of the outer ring using a single-track grey encoder.

## 2. Core Design

### 2.1 Position Sensing (The "Zero-Wear" System)

* **Sensor:** [AS5600 Magnetic Encoder](https://www.ams-osram.com).
* **Decision:** We avoid mechanical wipers/brushes (the main failure point of original Enigmas) in favour of contactless magnetic sensing.
* **Precision:** 6-bit resolution allows the CM5 to detect if a rotor is "between" characters and flag a mechanical jam.

### 2.2 Logic & Transposition

* **Logic:** The **Intel MAX II EPM240T100C5N CPLD** emulates the 64x64 cross-wiring.
* **Decoupling Rule:** Use **8x 0.1µF X7R** local decoupling capacitors per EPM240T100C5N IC (one per VCC pin).
* **Role:** Performs the instantaneous dual 6-bit parallel transposition (substitution cipher) for the forward and backward signal paths.
* **Memory:** Stores the 26-position wiring table for any historical rotor (I-VIII, Beta, Gamma) selectable via the CM5.
* **Latency:** Sub-10ns transposition time, ensuring the entire 30-rotor "trip" happens well within one CPU clock cycle.
* **Configuration:** CM5 loads the "Rotor Type" (e.g., Rotor I, II, III) into the CPLD's SRAM at boot via the JTAG Chain.

### 2.3 Mechanical Details

* **Mounting:** Each rotor PCB has two **M2.5 alignment holes**.
* **Retention:** Once slotted into the Stator, a **threaded rod** (mimicking the original Enigma spindle) passes through the center of all 30 rotors to lock them into a single, rigid block.
* **Hot-Swappable:** The Samtec Edge-Rate connectors are rated for high mating cycles, allowing individual rotors to be pulled for "repair" or reconfiguration without tools.

## 3. Electrical Requirements

### 3.1 Power Management

* **Input:** 3.3V/**50mA per rotor** (sourced from the **Power Module** 3V3_ENIG rail, routed through Controller Board → Stator Board → Rotor stack via Link-Beta).
  See `design/Power_Budgets.md` for full budget — 30 rotors draw 1.50A typical; the 150mA/rotor figure previously used was a conservative overestimate.
* **Filtering:** Local **10uF X7R** bulk entry bank on each rotor; upstream rail filtering uses the **Stator ferrite bead bank** to suppress stack switching noise.
* **Bulk Entry Bank Rule:** Use **5x 10uF X7R 50V** capacitors near the power-entry pins in a **Symmetrical Star/Spoke pattern**.

### 3.2 Communication Bus

* **The Data Path:** 12-bit parallel bus (D0-D11) passes through every rotor in a daisy-chain or star-bus configuration.
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
  stackup (h=0.087mm, t=0.035mm, Eᵣ=4.4). See `design/Electronics/JTAG_Integrity.md` and DEC-016.
* **Shielding:** 4-layer PCB with solid GND plane (L2) to isolate digital switching from the high-accuracy magnetic encoder.

### 3.4 PCB Fabrication (JLCPCB Specs)

* **Layers:** 4-Layer (JLC04161H-7628).
* **Finish:** ENIG (Gold) for the edge-rate connector pads.
* **Aesthetics:** Dark Green Solder Mask with Typewriter font labeling (e.g., "WALZE I").

---

## 4. Bill of Materials

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C1-C8 | Decoupling (8 per CPLD) | 0.1µF X7R 10V | 0402 | 81-GRM155R71A104KE1D | 311-1424-1-ND | C49678 |
| C9-C13 | Bulk entry decoupling bank (star/spoke) | 10uF X7R 50V | 1206 | 187-CL31B106KBHNNNE | 1276-6767-1-ND | CL31B106KBHNNNE |
| J1 | Edge-rate connector (MALE header — ERM8-020-05.0-S-DV-K-TR, 40-pin) | Samtec ERM8 | 0.8mm pitch | 200-ERM8020050SDVKTR | SAM12065-ND | N/A — customer-supplied |
| U1 | Intel MAX II CPLD | EPM240T100C5N | TQFP-100 | 989-EPM240T100C5N | 544-EPM240T100C5N-ND | C123470 |
| U2 | Magnetic encoder | AS5600 | DFN-8 | 985-AS5600-ASOM | 620-1984-1-ND | C123471 |

> **Design decision history:** See `design/Design_Log.md` for all formal design decisions (DEC-xxx) applicable to this board.
