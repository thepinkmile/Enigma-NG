# Enigma-NG Board Overview

The Enigma-NG system uses a modular, "Museum-Grade" architecture. It is divided into seven distinct modules to ensure maximum signal integrity, industrial-grade power protection, and mechanical
robustness.

## � Power Rail Glossary (Canonical naming)

* **3V3_SYSTEM**: Provided by CM5 +3.3V regulator; powers Controller logic, status lines (USB/HDMI/Ethernet), and local digital I/O.
* **3V3_ENIG**: Provided by Power Module 3.3V LDO; distributed to Stator and the Rotor stack (core encryption logic).
* **5V_MAIN**: Provided by Power Module 5V buck; powers CM5 main supplies and 5V system bus.
* **GND_CHASSIS**: Safety earth / EMI reference plane.
* **PWR_GD**: Power-good handshake line from Power Module to Controller.

## 🧮 Telemetry Sensor Responsibility

* Power Module INA219 (I2C address 0x40): monitors Power Module generated rails (5V_MAIN, 3V3_ENIG, battery input state).
* Stator INA219 (I2C address 0x45): monitors rotor stack power usage via 20mΩ shunt on the 3V3_ENIG bus.

## 📡 I2C Bus Map

* I2C1 (SCL/SDA): routed through Controller → Power Module → Stator → Rotor chain.
  * 0x0B: Smart Battery / SMBus monitoring.
  * 0x28: STUSB4500 USB PD controller on Power Module.
  * 0x40: INA219 on Power Module (input/rail generation telemetry, including 5V_MAIN and 3V3_ENIG).
  * 0x45: INA219 on Stator (rotor stack draw telemetry on the 3V3_ENIG bus).

## �📋 1. System Architecture & Status (Alphabetical)

| Board Name | Role | Stackup | Status |
| :--- | :--- | :--- | :--- |
| **Controller Board** | CM5 Brain, high-speed I/O, and UI management. | 6-Layer / 1oz | **Design Locked** |
| **Encoder Module** | Dual-use Keyboard / Plugboard / Lampboard logic using 2x Intel MAX II EPM240T100C5N CPLD. | 4-Layer / 1oz | **Design Locked** |
| **JTAG Daughterboard** | Internal FT232H-based hardware programmer. | 2-Layer / 1oz | **Design Locked** |
| **Power Module** | Input filtering, UPS reservoir, and eFuse protection. | 4-Layer / 2oz | **Design Locked** |
| **Reflector Board** | Terminating board for the rotor stack return path. | 2-Layer / 1oz | **Design Locked** |
| **Rotor Module** | Smart encryption units (30x) with MAX II EMP240T100C CPLDs. | 4-Layer / 1oz | **Architecture Set** |
| **Stator Board** | Mechanical backplane for the 30-rotor stack with CPLD for plugboard configuration mapping. | 4-Layer / 1oz | **Design Locked** |

## 🧠 2. Controller Board

The logic heart of the machine, hosting the Raspberry Pi CM5.

* **Stackup:** 6-Layer JLC06161H-2116 for 5Gbps signal integrity.
* **Aesthetics:** Dark Green mask with ENIG Gold finish and Bilingual Typewriter silkscreen.
* **Diagnostics:** 2x8 Gold-plated diagnostic bank for real-time bus monitoring.
* **UI:** 40-pin flush-edge Samtec link to the Stator/Encoder bus.

## ⌨️ 3. Encoder Module (Dual-Use)

Handles the 64-character QWERTY interface and reciprocal plugboard encoding.

* **Logic:** Dual Intel MAX II EPM240T100C5N CPLDs managing 64-node I/O.
* **Keyboard Mode:** Populated with 10mm long-stroke industrial plungers (C&K F-Series).
* **Plugboard Mode:** Populated with 64 jack-sensing 3.5mm "Stecker" sockets.

## 🔌 4. JTAG Daughterboard (Hidden)

The internal "USB Blaster" that makes the Enigma-NG self-contained.

* **Bridge:** FT232H High-Speed USB 2.0.
* **Function:** Allows the CM5 to re-program all CPLD logic devices via the GUI without any external cables or visible ports.

## 🔋 5. Power Module (The "Power Can")

The primary gateway for the system. Isolated in a **Vintage Silver Aluminium** enclosure.

* **EMI Shielding:** Nanocrystalline dual-choke filtering for CE/UKCA compliance.
* **UPS Function:** 2.5F Supercapacitor bank providing >20s "Last-Gasp" hold-time.
* **Safety:** 72°C SMD Thermal Cutoff (TCO) and TPS25980 eFuse.
* **Interface:** Shielded PoE+, USB-C PD, and Smart Battery inputs.

## 🔄 6. Reflector Board (The "Turnaround")

Located at the opposite end of the Stator from the Controller, this board manages the signal's return journey.

* **Reflector Mode:** Pairs the output of the last rotor and sends it back into the stack return path.
* **Extended Mode:** Routes the signal out to an external Plugboard encoder before returning it through the stack.

## ⚙️ 7. Rotor Module

Modular units containing the encryption logic.

* **Logic:** An Intel MAX II EPM240T100C5N CPLD per rotor.
* **Telemetry:** AS5600 Magnetic Encoders to report physical wheel position to the CM5.
* **Mechanical:** Features a 3D-printed/CNC index gear for the manual advancement pawls.

## 🛣️ 8. Stator Board

The mechanical and electrical backbone.

* **Distribution:** A backplane providing 5A power distribution and signal routing for the rotor stack.
* **Connectivity:** Bridges the Controller, Encoder, and Rotor stack into a single parallel bus.
* **Programmability** An Intel MAX II EPM240T100C5N CPLD is used to allow the GUI Application to re-configure the connection of the plugboard encoders either:
  * Before the rotor stack.
  * After the rotor stack.
  * Before and After the rotor stack.
  * Completely removed from the rotor stack.
