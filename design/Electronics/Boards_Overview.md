# Enigma-NG Board Overview

**Status:** Reference
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Last Updated:** 2026-04-04

## 1. Overview

The Enigma-NG system uses a modular, "Museum-Grade" architecture. It is divided into nine distinct
board designs to ensure maximum signal integrity, industrial-grade power protection, and
mechanical robustness.

The `design/Standards/Global_Routing_Spec.md` applies to all boards in the Enigma-NG system except where a board's design spec explicitly documents an exemption from a specific rule.

## 2. Power Rail Glossary (Canonical naming)

* **3V3_ENIG**: Provided by Power Module TPS75733KTTRG3 LDO (3.3V fixed); powers all CPLDs, JTAG interface, I2C logic, rotor stack, and Controller digital I/O.
  Replaces the former 3V3_SYSTEM rail (see DEC-001).
* **5V_MAIN**: Provided by Power Module 5V buck; powers CM5 main supplies and 5V system bus.
* **GND**: Common power and signal ground reference. Shared across all boards via BtB connectors and chassis bond points.
* **GND_CHASSIS**: Safety earth / EMI reference plane.
* **PWR_GD**: Power-good handshake line from Power Module to Controller.

## 3. Telemetry Sensor Responsibility

* Power Module INA219 (I2C address 0x40): monitors 5V_MAIN current and power (10mΩ Kelvin-sense shunt R23).
* Stator INA219 (I2C address 0x45): monitors rotor stack power usage via CSS2H-2512R-R010ELF 10mΩ shunt (R1) on the 3V3_ENIG bus.

## 4. I2C Bus Map

* I2C1 (SCL/SDA): routed through Controller → Power Module → Stator → Rotor chain.
  * 0x09: LTC3350 Supercap Charger on Power Module (supercap health monitoring and charge management).
  * 0x0B: Smart Battery / SMBus monitoring.
  * 0x28: STUSB4500 USB PD controller on Power Module.
  * 0x40: INA219 on Power Module (5V_MAIN current/power telemetry).
  * 0x45: INA219 on Stator (rotor stack draw telemetry on the 3V3_ENIG bus).

## 5. System Architecture & Status (Alphabetical)

| Board Name | Role | Stackup | Status |
| :--- | :--- | :--- | :--- |
| **Controller Board** | CM5 Brain, high-speed I/O, and UI management. | 6-Layer / 2oz | **Design Locked** |
| **Encoder Module** | Dual-use Keyboard / Plugboard / Lampboard logic using 2x Intel MAX II EPM240T100I5N CPLD. | 4-Layer / 2oz | **In Review** |
| **Extension Board** | Re-buffers TCK/TMS JTAG signals between 5-rotor groups; bridges TTD_RETURN. Up to ×5 in full build; Rev A uses ×1. | 4-Layer / 2oz | **Design Locked** |
| **JTAG Daughterboard** | Internal FT232H-based hardware programmer. | 4-Layer / 2oz | **Design Locked** |
| **Power Module** | Input filtering, UPS reservoir, and eFuse protection. | 6-Layer / 2oz | **Design Locked** |
| **Reflector Board** | Terminating board for the rotor stack return path. | 4-Layer / 2oz | **Design Locked** |
| **Rotor Module** | Smart encryption units (30x) with MAX II EPM570T100I5N CPLDs. | 4-Layer / 2oz | **Architecture Set** |
| **Settings Board** | Panel-mount switch and RGB LED configuration interface on the shared Stator I2C-1 bus. | 4-Layer / 2oz | **In Review** |
| **Stator Board** | Mechanical backplane for the 30-rotor stack with CPLD for plugboard configuration mapping. | 4-Layer / 2oz | **Design Locked** |

## 6. Controller Board

The logic heart of the machine, hosting the Raspberry Pi CM5.

* **Stackup:** 6-Layer JLC06161H-2116 for 5Gbps signal integrity.
* **Aesthetics:** Dark Green mask with ENIG Gold finish and Bilingual Typewriter silkscreen.
* **Diagnostics:** Two 2×10 Gold-plated diagnostic banks (Bank-Alpha: power/status monitoring; Bank-Beta: encryption/JTAG monitoring) for real-time bus monitoring.
* **UI:** 40-pin flush-edge Samtec link to the Stator.

## 7. Encoder Module (Dual-Use)

Handles the 64-character QWERTY interface and reciprocal plugboard encoding.

* **Logic:** Dual Intel MAX II EPM240T100I5N CPLDs managing 64-node I/O.
* **Keyboard Mode:** 64 DPDT mechanical push-button switches (6-pin, momentary) mounted in the keyboard panel; connected to the PCB via 6.35mm spade-terminal harness.
* **Plugboard Mode:** 64 × 6.35mm (¼″) mono switched panel-mount jack sockets ("Stecker") connected via the same spade-terminal harness architecture.

## 8. JTAG Daughterboard (Hidden)

The internal "USB Blaster" that makes the Enigma-NG self-contained.

* **Bridge:** FT232H High-Speed USB 2.0.
* **Function:** Allows the CM5 to re-program all CPLD logic devices via the GUI without any external cables or visible ports.

## 9. Power Module (The "Power Can")

The primary gateway for the system. Isolated in a **Vintage Silver Aluminium** enclosure.

* **EMI Shielding:** Nanocrystalline dual-choke filtering for CE/UKCA compliance.
* **UPS Function:** 50F Supercapacitor bank (8× Abracon 25F/2.7V, 2S4P) providing ≥33.5 seconds "Last-Gasp" hold-time.
* **Safety:** 72°C SMD Thermal Cutoff (TCO) and TPS259804ONRGER eFuse (16.9V fixed OVLO).
* **Interface:** Shielded PoE+, USB-C PD, and Smart Battery inputs.

## 10. Reflector Board (The "Turnaround")

Located at the opposite end of the Stator from the Controller, this board manages the signal's return journey.

* **Reflector Mode:** Pairs the output of the last rotor and sends it back into the stack return path.
* **Extended Mode:** Routes the signal out to an external Plugboard encoder before returning it through the stack.

## 11. Rotor Module

Modular units containing the encryption logic.

* **Logic:** An Intel MAX II EPM570T100I5N CPLD per rotor.
* **Telemetry:** FDC2114RGHR capacitive encoders (dual-track Gray code for N=64; single-track STGC for N=26) to report rotor position to the CM5 via Virtual JTAG (DEC-027).
* **Mechanical:** Features a 3D-printed/CNC index gear for the manual advancement pawls.

## 12. Stator Board

The mechanical and electrical backbone.

* **Distribution:** A backplane providing ~2.05A worst-case typical 3V3_ENIG distribution and signal routing for the rotor stack.
* **Connectivity:** Bridges the Controller, Encoder, and Rotor stack into a single parallel bus.
* **Programmability:** An Intel MAX II EPM570T100I5N CPLD is used to allow the GUI Application to re-configure the connection of the plugboard encoders either:
  * Before the rotor stack.
  * After the rotor stack.
  * Before and After the rotor stack.
  * Completely removed from the rotor stack.

> **Design decisions:** All formal design decisions (DEC-xxx) applicable across boards are recorded in `design/Design_Log.md`.
