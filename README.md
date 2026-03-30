# Enigma NG: Digital Cryptography Ecosystem

The Enigma-NG is an advanced "Museum-Grade", modular, and historically-accurate digital recreation of the world’s most iconic encryption machines.
Powered by a **Raspberry Pi Compute Module 5 (CM5)**, this system controls a hardware stack of up to 30 custom CPLD-based rotors and a physical 64-jack plugboard.
Powered with either USB-C Power Adapter, PoE+ or Smart Battery. It bridges 1940s mechanical heritage with 2026 high-speed digital engineering.

## 🚀 Project Vision

To create a high-fidelity, educational, and industrially robust encryption platform.
The design prioritises classroom safety, professional EMI shielding, and deep hardware visibility for students via an integrated diagnostic bank.
Beyond a simple Enigma clone, this terminal is a **Universal Cipher Engine**. The hardware is designed to emulate:

* **Enigma Variants:** I, M3, M4, and Abwehr.
* **Typex:** The 5-rotor British adaptation with simulated printer output.
* **SIGABA:** The 15-rotor US system using complex 3-bank stepping algorithms.
* **NG-26** The modern digital enigma machine designed and created by Matthew McAtamney-Greenwood.

## Tools Used

* **Visual Studio Code:** To manage the Documentation within this repository.
* **Visual Studio:** (Latest Community Edition) To develop the GUI Application.
* **KiCAD 9:** To develop the electrical components and PCB layouts.
* **OnShape:** To create and manage the mechanical designs and assemblies.
* **Yocto:** To create the custom Linux OS with built-in drivers and GUI Application.

## Core Component Overview

* **Controller:** Raspberry Pi Compute Module 5 (CM5) carrier board for monitoring and programming the system.
* **Power Module:** Triple-input priority (PoE+ > USB-C PD > Battery) with 11V–17V eFuse protection.
* **Interface:** 40-pin Samtec Right-Angle Board-to-Board (BtB) link to the Stator board.
* **Diagnostics:** 2x8 Gold-plated (ENIG) test loop bank for 12-bit data and JTAG monitoring.
* **UI:** .NET 10.0 Cross-platform GUI with live power telemetry.

---

## 🔌 Hardware Architecture

### 1. Controller Board (The Brain)

* **Module:** Raspberry Pi CM5 (BCM2712) on a custom 4-layer 1.6mm carrier.
* **Power Input:** 3-way seamless switching (LTC4412 Ideal Diode).
  * **Smart Battery:** 4-pin Molex connector (12V-14.4V nominal) with SMBus telemetry.
  * **PoE+ (802.3at):** 30W Power-over-Ethernet via isolated PD controller.
  * **USB-C PD:** 5V/5A negotiated input.
* **Protection:** **TPS259474L eFuse** (Latch-off) with 12V UVLO / 16V OVP / 5.5A Limit.
* **Output Rail:** Dedicated 3.3V/5A Buck Converter for the 30-rotor stack.
* **JTAG Master:** Embedded FT232H (Permanent USB Blaster) on internal USB 2.0.
* **Connectivity:** Native USB 3.0 (SMT), HDMI (SMT), and Gigabit Ethernet.
* **User Interface:** Illuminated Vintage Amber **Safe Shutdown Button**, Master Toggle, and Status LEDs.

### 2. Universal Rotor (The Engine)

* **Logic:** Intel **MAX II EPM240T100C5N** CPLD.
* **Dimensions:** 122mm PCB Diameter / **163mm Outer Diameter (OD)**.
* **Segments:** 64 characters with **8mm arc width** for high readability.
* **Memory:** 10 pre-loaded bidirectional wiring sets; 4-position DIP switch for "Rotor Identity" selection.
* **Sensing:** 6-bit Single-Track De Bruijn sequence via 6x **TCRT5000L** reflective sensors.
* **Tri-Connector Bus:**
  * Power (2x2), JTAG (2x4 Shielded), and Enigma (2x6 Bidirectional Relay) in a "Tripod" layout.
* **Signal Integrity:** **74LVC125A** buffer on every rotor for TCK/TMS regeneration.

### 3. Universal Interface (Keyboard/Plugboard)

* **Logic:** 2x **MAX II EPM240** (Decoder/Encoder).
* **Keyboard:** 37-key "Hold-to-Shift" layout with Vintage Amber LED feedback.
* **Plugboard:** 64x 3.5mm Switching Jacks with 8-channel TVS ESD protection.
* **Logic Pattern:** Active-Low (Internal CPLD pull-ups for keys, Sink-to-GND for LEDs).

---

## 💻 Software Implementation

### 1. Linux Kernel Driver (`enigma_core.c`)

* **Interrupt Handling:** High-priority monitoring of the `KEY_EVENT_INT` line.
* **State Mapping:** Maps 6-bit Input/Return Path to `/dev/enigma_state`.
* **Power Telemetry:** Exposes SMBus battery data and PoE status to userspace.
* **JTAG Control:** Executes Boundary Scan (SAMPLE/PRELOAD) upon keypress trigger.

### 2. .NET 10 GUI (The Terminal)

* **Binary File Transfer:** Encrypts files via Base64 encoding/decryption through the hardware rotors.
* **Ethernet/UDP Interface:** Secure 6-bit encrypted UDP streams for remote terminal communication.
* **Power Dashboard:** Real-time monitoring of Battery (SoC/Temp), PoE+, and USB-C sources.
* **Rotor Library Manager:** Visual tool to design custom wiring and flash the 30-rotor stack.
* **Historical Archive:** Educational database of Enigma, Typex, and SIGABA variants.

---

## ⚠️ Safety & Design Rules (KiCAD 9)

* **eFuse Latch-off:** Electronic fault protection requires manual power cycle to reset.
* **Soft Start:** Master toggle drives regulator Enable (EN) pins to prevent inrush.
* **ESD Hardening:** TVS diodes on all exposed pins (JTAG, Enigma, and 64-jack lines).
* **Stackup:** 4-layer 1.6mm FR4; L2 Solid GND plane; 90Ω (USB) / 100Ω (HDMI) diff pairs.

---

## 📅 Development Roadmap

1. **Controller Board:** KiCAD 9 Schematic & Layout (Power, CM5, High-Speed I/O, JTAG Master).
2. **Universal Rotor:** Hardware Prototype (MAX II, 163mm Shell, De Bruijn Sensors).
3. **Power Injection & Support (PIS):** Passive "Mid-Span" bridge for mechanical alignment and 3.3V rail boosting.
4. **Universal Interface:** 64-Jack Plugboard and 37-key "Passive" strip design.
5. **Firmware:** Verilog for Rotor libraries and Interface Encoding/Decoding.
6. **Driver & GUI:** Linux C-Driver and .NET 10 terminal application.

## Contributions

This is an open-source development project. Contributions are welcomed from all.
When submitting an issue please ensure you provide the SHA commit hash for the version of code that exhibits your issue and provide full replication steps.
For any contributions, please create a Pull Request and ensure useful commit messages are provided.
Once a PR is accepted the changes with be squashed into the current working branch of this repository and your name will be added to the list of contributors.

<!-- readme: collaborators,contributors -start -->
<table>
	<tbody>
		<tr>
            <td align="center">
                <a href="https://github.com/thepinkmile">
                    <img src="https://avatars.githubusercontent.com/u/23457507?v=4" width="100;" alt="thepinkmile"/>
                    <br />
                    <sub><b>The Pink Mile Developer</b></sub>
                </a>
            </td>
		</tr>
	<tbody>
</table>
<!-- readme: collaborators,contributors -end -->

## Licensing

For enquiries regarding educational licensing, please contact the maintainer.
This repository is licensed under the GNU GENERAL PUBLIC LICENSE v3.
