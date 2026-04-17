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

One of the long-term goals of this project is to introduce the ability to deliver Enigma encrypted data over the network,
and even provide the ability to deliver encrypted files using a base-64 encoding before executing the standard rotor-based encryption.
This end-goal will involve the definition of a new RFC for the "Enigma-Packet-Protocol (EnPP)", which will be a custom specification for this project's ecosystem.

## Tools Used

* **Visual Studio Code:** To manage the Documentation within this repository.
* **Visual Studio:** (Latest Community Edition) To develop the GUI Application.
* **KiCAD 9:** To develop the electrical components and PCB layouts.
* **OnShape:** To create and manage the mechanical designs and assemblies.
* **Yocto:** To create the custom Linux OS with built-in drivers and GUI Application.

## Core Component Overview

* **Controller:** Raspberry Pi Compute Module 5 (CM5) carrier board for monitoring and programming the system.
* **Power Module:** Triple-input OR-ing with documented PoE-over-USB-C priority and
  voltage-dependent USB-C/Battery precedence, plus 11V–16.9V eFuse protection.
* **Stator:** A CPLD powered component mapper and the initial starting point of the rotor stack.
* **Extension:** A block that allows extension of the rotor stack in 5-rotor increments.
* **Reflector:** A logic loopback from the end of the rotor stack. Also, uses the Stator for mapping comonents (if/when required).

## Core Requirements

* **Interface:** 80-pin Samtec BtB Link-Alpha between Power→Controller, plus 40-pin Samtec BtB Link-Beta between Controller→Stator.
* **Diagnostics:** 2x10 Gold-plated (ENIG) test loop bank for power, I2C, JTAG, and spare-signal monitoring.
* **UI:** .NET 10.0 Cross-platform GUI with:
  * Live power telemetry.
  * Historical resources.
  * 3D graphical visualiser.
  * Configuration programmer (and creator).

---

## 🔌 Hardware Architecture

### 1. Power Module (The Heart)

* **Input:** Triple-input OR-ing between PoE+ 802.3bt Type 4, USB-C 15V PD, and Battery
  11–16.4V via LM74700-Q1 + CSD17483F4T ideal-diode FETs. PoE is explicitly prioritised over
  USB-C; USB-C vs Battery precedence follows the active input voltages unless extra gating is added.
* **PoE:** Fully discrete 802.3bt Type 4 front end — TPS2372-4 (PD interface) + TPS23730 (ACF DC-DC) + Coilcraft POE600F-12LD transformer stage. Implemented 12V power stage capacity: 60W.
* **Protection:** TPS25980 eFuse — 7A ILIM, 11.0V UVLO, 16.9V OVLO, 3mΩ RON. Plus 72°C TCO thermal fuse.
* **Buck:** Dual-phase interleaved LMQ61460-Q1 (×2, 6A each, 12A combined, 400kHz DRSS, 180° SYNC). Effective ripple: 800kHz.
* **LDO:** TPS75733KTTRG3 3V3_ENIG (8.8µVRMS noise, 72dB PSRR, 3A, 2.05 A typical load at 68.3% utilisation).
* **UPS:** LTC3350 supercap manager + 8× Abracon ADCR-T02R7SA256MB (2S4P, 50 F) on 5V_MAIN bus. 50 F at 5.4V → ≥33.5 second hold-up for clean CM5 shutdown.
* **Output Rails:** 5V_MAIN (12A) and 3V3_ENIG (3A — logic, CPLDs, and rotor stack) via 80-pin Samtec ERF8 BtB to Controller Board for distribution.
* **Panel Controls:** SW1 is a rugged latching RGB power toggle (Adafruit 4660) and SW2 is a
  matching 16mm momentary RGB CM5 power button (Adafruit 3350); both are panel-mounted controls
  wired to the Power Module harness.

### 2. Controller Board (The Brain)

* **Module:** Raspberry Pi CM5 (BCM2712) on a custom 6-layer 2oz carrier.
* **Power Input:** 3-way seamless switching (LM74700-Q1 ideal-diode on Power Module).
  * **Smart Battery:** 5-pin Molex Micro-Fit connector (11V-16.4V nominal) with SMBus telemetry + BATT_PRES_N.
  * **PoE+ (802.3bt Type 4):** Power-over-Ethernet delivered through the Power Module discrete
    TPS2372-4 + TPS23730 + POE600F-12LD path. The implemented 12V stage is sized at 60W. Single
    Ethernet cable carries both data and power.
  * **USB-C PD:** 15V USB-C PD negotiated input.
* **Protection:** Over-voltage and over-current protection provided by Power Module eFuse upstream; local reverse-polarity and ESD protection on BtB interface.
* **Rotor Rail:** The rotor stack is powered by the **3V3_ENIG** rail (TPS75733KTTRG3 LDO, 3A) generated on the Power Module; routed to rotor stack via Controller Board → Link-Beta. CM5 GPIO 16

  (ROTOR_EN) gates the LDO enable for sequenced power-up.

* **JTAG Master:** Embedded FT232H (Permanent USB Blaster) on internal USB 2.0.
* **Connectivity:** Native USB 3.0 (SMT), HDMI (SMT), and Gigabit Ethernet.

### 3. Stator Board (Nervous System)

* {TBD}

### 4. Universal Rotor (The Engine)

* **Logic:** Intel **MAX II EPM570T100I5N** CPLD.
* **Dimensions:** Ø92 mm PCB / **Ø100 mm shroud outer**.
* **Segments:** 64 characters with **8mm arc width** for high readability.
* **Memory:** 10 pre-loaded bidirectional wiring sets; 4-position DIP switch for "Rotor Identity" selection.
* **Sensing:** FDC2114RGHR capacitive encoder ICs (dual-track, 3+3 per rotor).
* **Tri-Connector Bus:**
  * Power (2x2), JTAG (2x4 Shielded), and Enigma (2x6 Bidirectional Relay) in a "Tripod" layout.
* **Signal Integrity:** **SN74LVC2G125DCUR** buffer on each Extension Board (one per 5-rotor group) for TCK/TMS regeneration.

### 5. Universal Interface (Keyboard/Plugboard)

* **Logic:** 2x Intel **MAX II EPM240T100I5N** CPLD (Decoder/Encoder).
* **Keyboard:** 64-key "Hold-to-Shift" layout with Vintage Amber LED feedback.
* **Plugboard:** 64x 6.35mm (¼″) Switching Jacks with 8-channel TVS ESD protection.
* **Logic Pattern:** Active-Low (Internal CPLD pull-ups for keys, Sink-to-GND for LEDs).

---

## 💻 Software Implementation

### 1. Linux Kernel Driver

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

### 3. VHDL Firmware (The Navigators)

* {TBD}

---

## ⚠️ Safety & Design Rules (KiCAD 9)

* **eFuse Latch-off:** Electronic fault protection requires manual power cycle to reset.
* **Soft Start:** SW1 drives the TPS25980 eFuse EN pin; the CM5 separately gates the 3V3_ENIG LDO with ROTOR_EN.
* **ESD Hardening:** TVS diodes on all exposed pins (JTAG, Enigma, and 64-jack lines).
* **Stackup:** Mixed stackup architecture: Controller Board and Power Module are 6-layer boards; the remaining electronics boards are 4-layer / 2oz designs.

---

## 📅 Development Roadmap

1. **Controller Board:** KiCAD 9 Schematic & Layout (Power, CM5, High-Speed I/O, JTAG Master).
2. **Universal Rotor:** Hardware Prototype (MAX II, Ø100mm shroud outer, FDC2114RGHR capacitive encoders).
3. **Power Injection & Support (PIS):** Passive "Mid-Span" bridge for mechanical alignment and 3.3V rail boosting.
4. **Universal Interface:** 64-Jack Plugboard and 64-key "Hold-to-Shift" layout.
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
