# Enigma 2026 AI: Digital Cryptography Ecosystem

An advanced, modular, and historically-accurate digital recreation of the world’s most iconic encryption machines. Powered by a **Raspberry Pi Compute Module 5 (CM5)**, this system controls a hardware stack of up to 30 custom CPLD-based rotors and a physical 64-jack plugboard.

## 🚀 Project Vision
Beyond a simple Enigma clone, this terminal is a **Universal Cipher Engine**. The hardware is designed to emulate:
*   **Enigma Variants:** I, M3, M4, and Abwehr.
*   **Typex:** The 5-rotor British adaptation with simulated printer output.
*   **SIGABA:** The 15-rotor US system using complex 3-bank stepping algorithms.

---

## 🔌 Hardware Architecture

### 1. Controller Board (The Brain)
*   **Module:** Raspberry Pi CM5 (BCM2712) on a custom 4-layer 1.6mm carrier.
*   **Power Input:** Dual-source with seamless switching (LTC4412 Ideal Diode).
    *   **USB-C PD:** 5V/5A negotiated input.
    *   **Military Battery:** Fischer 102 Connector (12V-14.4V nominal).
*   **Protection:** **TPS259474L eFuse** with Latch-off safety (12V UVLO / 16V OVP / 5.5A Limit).
*   **Output Rail:** Dedicated 3.3V/5A Buck Converter for the 30-rotor stack.
*   **JTAG Master:** Embedded FT232H (Permanent USB Blaster) on internal USB 2.0.
*   **I/O Hub:** 
    *   Native USB 3.0 (90Ω Diff Pairs), HDMI (100Ω Diff Pairs), and Gigabit Ethernet.
    *   3x 20-pin SMT Headers for Keyboard/Lightboard strips (A-Z, 0-9, +, =, Shift).

### 2. Universal Rotor (The Engine)
*   **Logic:** Intel **MAX II EPM240T100C5N** CPLD.
*   **Memory:** 10 pre-loaded bidirectional wiring sets stored in UFM (User Flash Memory). 
*   **Selection:** 4-position DIP switch to select "Rotor Identity" from the internal library.
*   **Sensors:** 6-bit Single-Track Gray Code via 6x **TCRT5000L** reflective sensors on the PCB perimeter.
*   **Tri-Connector Bus:**
    *   **Power:** 2x2 Molex Micro-Fit (3.3V Parallel).
    *   **JTAG:** 2x4 Molex Micro-Fit (GND-Shielded Daisy Chain).
    *   **Enigma:** 2x6 Molex Micro-Fit (12-bit Bidirectional Relay).
*   **Signal Integrity:** **74LVC125A** buffer on every rotor for TCK/TMS regeneration.

### 3. Universal Interface (The I/O)
*   **Logic:** 2x **MAX II EPM240** (1x 6-to-64 Decoder, 1x 64-to-6 Encoder).
*   **Keyboard/Lightboard:** 37-key "Hold-to-Shift" layout with Vintage Amber LED feedback.
*   **Plugboard:** 64x 3.5mm Switching Jacks with 8-channel TVS ESD protection.
*   **Logic Pattern:** Active-Low (Internal CPLD pull-ups for keys, Sink-to-GND for LEDs).

---

## 💻 Software Implementation

### 1. Linux Kernel Driver (`enigma_core.c`)
A custom C driver providing a high-performance bridge between hardware and userspace.
*   **Interrupt Handling:** Monitors the `KEY_EVENT_INT` line from the Encoder CPLD.
*   **State Mapping:** Maps the 6-bit Input and 6-bit Return Path directly to a character device at `/dev/enigma_state`.
*   **JTAG Control:** Triggers the USB Blaster to perform a Boundary Scan (SAMPLE/PRELOAD) upon keypress.

### 2. .NET 10 GUI (The Terminal)
A modern C# application providing a rich interactive experience via HDMI.
*   **Binary File Transfer:** Supports universal file encryption by Base64 encoding binary data and streaming the resulting 6-bit blocks through the hardware Enigma process.
*   **Ethernet/UDP Interface:** Secure "Digital Field Terminal" file exchanges between hardware units via 6-bit encrypted UDP streams.
*   **Rotor Library Manager:** Visual design tool to verify custom wiring maps and flash them to the 30-rotor stack via JTAG.
*   **Historical Archive:** Database of cryptography history covering Bletchley Park, Alan Turing, SIGABA development, and technical machine variants.

---

## 🛠 Design Rules (KiCAD 9)
*   **Stackup:** 4-layer 1.6mm thickness with solid GND plane (L2) and "Checkerboard" GND pinning on all inter-board connectors.
*   **Impedance:** 90Ω Differential Pairs for USB 3.0; 100Ω for HDMI/Ethernet.
*   **Component Mounting:** 100% Surface Mount (SMT) for high-speed I/O to eliminate "stub" reflections.

---

## ⚠️ Safety Features
*   **Latch-Off eFuse:** Electronic fault protection for military battery input. System kills power upon over-voltage or over-current and requires a manual master switch cycle to reset.
*   **Soft Start Logic:** Master toggle switch drives the Enable (EN) pins of regulators rather than switching raw high-current rails to prevent arcing and inrush spikes.
*   **ESD Hardening:** TVS diodes (PESD3V3L1BA) on every exposed connector pin; 8-channel TVS arrays and 220Ω series resistors on all 64 user-facing plugboard/keyboard lines.
*   **Thermal Management:** Solid ground fills and via-stitching under CPLDs for heat dissipation and EMI shielding.

---

## 📅 Development Roadmap
1.  **Controller Board:** KiCAD 9 Schematic & Layout (Power Entry, CM5 Socket, High-Speed I/O, JTAG Master).
2.  **Universal Rotor:** Hardware Prototype (MAX II Integration, Gray Code Sensor Alignment, Buffering).
3.  **Universal Interface:** 64-Jack Plugboard and 37-key "Passive" strip design.
4.  **Firmware:** Verilog implementation for Rotor libraries and Interface Encoding/Decoding.
5.  **Driver & GUI:** Linux C-Driver development followed by the .NET 10 terminal application.
