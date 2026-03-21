# Digital Enigma Ecosystem (CM5 Edition)

An authentic, modular, and high-performance digital recreation of the Enigma encryption machine. This system utilizes a **Raspberry Pi Compute Module 5 (CM5)** as the central controller, managing a scalable stack of up to 30 hardware rotors and a physical 64-jack plugboard interface.

## 🚀 Project Overview

The ecosystem consists of three distinct PCB designs that interconnect via a high-integrity "Tri-Connector" bus. The system supports bidirectional encryption paths (Forward/Return) and uses JTAG Boundary Scan for real-time hardware state monitoring.

### 🏗 System Architecture
*   **Controller Board:** The "Brain" (CM5 Carrier, Power Management, HDMI, Ethernet, USB 3.0, and Integrated JTAG Master).
*   **Universal Rotor:** The "Engine" (MAX II CPLD, Gray Code Absolute Encoder, and Signal Buffers).
*   **Universal Interface:** The "I/O" (Keyboard, Lightboard, and 64-Jack Plugboard translator).
*   **The Reflector:** The "Loop" (Physical JTAG return bridge and Enigma signal inversion).

---

## 🔌 Hardware Specifications

### 1. The Controller Board (Carrier)
*   **Processor:** Raspberry Pi CM5 (BCM2712).
*   **Power Input A:** USB-C PD (5V/5A negotiated).
*   **Power Input B:** Fischer 102 Connector for Military Batteries (LI-145, UBBL08, etc.).
*   **Protection:** **TPS259474L eFuse** with Latch-off safety (12V UVLO / 16V OVP / 5.5A Current Limit).
*   **Power Path:** LTC4412 Ideal Diode for seamless switching between USB and Battery sources.
*   **Regulators:** Dedicated high-current 3.3V/5A Buck Converter for the Rotor Stack.
*   **Connectivity:** Native USB 3.0 (SMT), HDMI (SMT), and Gigabit Ethernet.
*   **JTAG Master:** Embedded FT232H USB-to-JTAG bridge (Permanent USB Blaster) connected via internal USB 2.0.
*   **Switching:** Right-angle Master Toggle Switch (Enable-logic drive) and Power Selection Switch.

### 2. The Universal Rotor (x30)
*   **Logic:** Altera/Intel **MAX II EPM240T100** CPLD.
*   **Optimization:** **Mathematical Rotation Logic** (one base map + Gray code offset) to preserve UFM write endurance.
*   **Sensing:** 6-bit Single-Track Gray Code absolute encoder via 6x **TCRT5000L** reflective sensors on the PCB perimeter.
*   **Signal Integrity:** **74LVC125A** buffer on every rotor to regenerate global TCK/TMS lines across the 30-unit chain.
*   **Connectors:** Triple-connector "Tripod" layout for mechanical stability:
    *   **Power (2x2):** Molex Micro-Fit (3.3V/GND parallel bus).
    *   **JTAG (2x4):** Molex Micro-Fit (Shielded: GND-TCK-GND-TMS-GND-TDI/O-GND-RET_TDO).
    *   **Enigma (2x6):** Molex Micro-Fit (12-bit Bidirectional: 6 Forward / 6 Return local relay).

### 3. The Universal Interface (Plugboard/Keyboard/Lightboard)
*   **Logic:** 2x **MAX II EPM240T100** (1x 6-to-64 Decoder, 1x 64-to-6 Encoder).
*   **Interface:** 64x 3.5mm Switching Jacks for authentic patch-cable "stecker" usage.
*   **ESD Protection:** 8-channel TVS Diode Arrays + 220Ω series resistors on all 64 user-facing lines.
*   **Versatility:** Configurable as a Keyboard (Input), Lightboard (Output), or Plugboard (Middleware).

---

## 🛠 PCB Design Rules (KiCAD 9)

*   **Stackup:** 4-Layer FR4 (1.6mm thickness).
    *   **L1 (Top):** High-Speed Signals (USB 3.0, HDMI, JTAG).
    *   **L2:** Solid Ground Plane (Shielding & Return Path).
    *   **L3:** Power Planes (5V, 3.3V).
    *   **L4 (Bottom):** Low-Speed Sensor/Logic Signals.
*   **Impedance Control:** 
    *   **USB 3.0:** 90Ω Differential Pairs.
    *   **HDMI/Ethernet:** 100Ω Differential Pairs.
*   **Shielding:** Checkerboard Ground pattern on JTAG connectors (every signal pin flanked by GND).
*   **Component Mounting:** 100% Surface Mount (SMT) for high-speed I/O to eliminate "stub" reflections.

---

## 💻 Software & Logic
*   **OS:** Raspberry Pi OS (64-bit) with a custom C# GUI via HDMI.
*   **Position Feedback:** JTAG **Boundary Scan** (SAMPLE/PRELOAD) used to poll 30 rotor positions via the USB Blaster.
*   **Connectivity:** Ethernet/UDP support for transmitting/receiving encoded 6-bit packets between remote units.
*   **JTAG Tools:** Quartus Pro / System Console (TCL scripts) for chain management and CPLD programming.

---

## ⚠️ Safety Features
*   **Latch-Off eFuse:** Active OVP/UVLO. System kills power upon fault and requires a manual master switch cycle to reset.
*   **Thermal Management:** Via-stitching and ground fills under CPLDs for EMI shielding and heat dissipation.
*   **ESD:** TVS diodes (PESD3V3L1BA) on every exposed connector pin (JTAG, Enigma, and Jacks).
