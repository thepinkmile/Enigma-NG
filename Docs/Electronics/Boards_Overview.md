# Enigma-NG Board Overview

The Enigma-NG system uses a modular, "Museum-Grade" architecture. It is divided into seven distinct modules to ensure maximum signal integrity, industrial-grade power protection, and mechanical robustness.

### 📋 System Architecture & Status (Alphabetical)


| Board Name | Role | Stackup | Status |
| :--- | :--- | :--- | :--- |
| **Controller Board** | CM5 Brain, high-speed I/O, and UI management. | 6-Layer / 1oz | **Design Locked** |
| **Encoder Module** | Dual-use Keyboard / Plugboard / Lampboard logic. | 4-Layer / 1oz | **Architecture Set** |
| **JTAG Daughterboard**| Internal FT232H-based hardware programmer. | 2-Layer / 1oz | **Design Locked** |
| **Power Module** | Input filtering, UPS reservoir, and eFuse protection. | 4-Layer / 2oz | **Design Locked** |
| **Reflector Board** | Terminating board for the rotor stack return path. | 2-Layer / 1oz | **Architecture Set** |
| **Rotor Module** | Smart encryption units (30x) with iCE40 FPGAs. | 4-Layer / 1oz | **Architecture Set** |
| **Stator Board** | Mechanical backplane for the 30-rotor stack. | 4-Layer / 1oz | **Architecture Set** |

---

### 🧠 1. Controller Board
The logic heart of the machine, hosting the Raspberry Pi CM5.
*   **Stackup:** 6-Layer JLC06161H-2116 for 5Gbps signal integrity.
*   **Aesthetics:** Dark Green mask with ENIG Gold finish and Bilingual Typewriter silkscreen.
*   **Diagnostics:** 2x8 Gold-plated diagnostic bank for real-time bus monitoring.
*   **UI:** 40-pin flush-edge Samtec link to the Stator/Encoder bus.

### ⌨️ 2. Encoder Module (Dual-Use)
Handles the 64-character QWERTY interface and reciprocal plugboard encoding.
*   **Logic:** Dual **EPM240T100 CPLDs** managing 64-node I/O.
*   **Keyboard Mode:** Populated with 10mm long-stroke industrial plungers (C&K F-Series).
*   **Plugboard Mode:** Populated with 64 jack-sensing 3.5mm "Stecker" sockets.

### 🔌 3. JTAG Daughterboard (Hidden)
The internal "USB Blaster" that makes the Enigma-NG self-contained.
*   **Bridge:** FT232H High-Speed USB 2.0.
*   **Function:** Allows the CM5 to re-program all 32 logic devices (37x CPLDs) via the GUI without any external cables or visible ports.

### 🔋 4. Power Module (The "Power Can")
The primary gateway for the system. Isolated in a **Vintage Silver Aluminium** enclosure.
*   **EMI Shielding:** Nanocrystalline dual-choke filtering for CE/UKCA/DefStan compliance.
*   **UPS Function:** 2.5F Supercapacitor bank providing >20s "Last-Gasp" hold-time.
*   **Safety:** 72°C SMD Thermal Cutoff (TCO) and TPS259474L eFuse.
*   **Interface:** Shielded PoE+, USB-C PD, and Smart Battery inputs.

### 🔄 5. Reflector Board (The "Turnaround")
Located at the opposite end of the Stator from the Controller, this board manages the signal's return journey.
*   **Reflector Mode:** Pairs the output of the last rotor and sends it back into the stack return path.
*   **Extended Mode:** Routes the signal out to an external Plugboard encoder before returning it through the stack.

### ⚙️ 6. Rotor Module
Modular units containing the encryption logic.
*   **Logic:** Altera EPM240T100C CPLD per rotor.
*   **Telemetry:** **AS5600 Magnetic Encoders** to report physical wheel position to the CM5.
*   **Mechanical:** Features a 3D-printed/CNC index gear for the manual advancement pawls.

### 🛣️ 7. Stator Board
The mechanical and electrical backbone.
*   **Distribution:** A 30-slot backplane providing 5A power distribution and signal routing.
*   **Connectivity:** Bridges the Controller, Encoder, and Rotor stack into a single parallel bus.
*   **Programmability** An Altera EPM240T100C is used to allow the GUI Application to re-configure the connection of the plugboard encoders either before, after or completely removed from the rotor stack.
