# Enigma-NG Software Design: C# GUI Application

## 1. Core Framework

* **Version:** .NET 10.0 (C#)
* **UI Library:** Avalonia UI (for hardware-accelerated Skia rendering on Linux/CM5).
* **Architecture:** MVVM (Model-View-ViewModel) for clean separation between hardware I/O and the display.

## 2. Aesthetic (The "Digital Museum" Look)

* **Font:** Authentic "Typewriter" monospaced font for all data readouts.
* **Colour Palette:** "Enigma Green" (#004D40), Slate Grey, and Amber highlights.
* **Bilingual Toggle:** A one-click switch to toggle all UI text between **DEUTSCH** and **ENGLISH**.

## 3. Primary Dashboard Features

* **The Virtual Enigma:** A 3D or high-res 2D representation of the 30-rotor stack.
* **Live Power Telemetry:** Real-time Gauges for Voltage, Current (mA), and Power (W) sourced from the INA219.
* **Source Indicators:** Dynamic icons for PoE+, USB-C, and Battery (with "Time-to-Empty" countdown).
* **Thermal Monitor:** CPU and eFuse temperature tracking with bilingual "HOT" alerts.
* **The "Daily Key":** Ability to export/import the machine configuration (Rotor order, Ring settings, Plugboard patches) as a "Codebook" PDF or JSON file.

## 4. Cryptographic Visualization

* **Signal Path Trace:** A "light-trail" animation showing the 12-bit signal traveling from the Keyboard, through the Plugboard, through the 30 rotors, hitting the Reflector, and returning to the Lampboard.
* **Rotor Configurator:** Drag-and-drop interface to "program" historical wiring (I-VIII) into the CPLDs/FPGAs.

---

## 5. GUI Implementation Checklist

* [ ] Setup Avalonia .NET 10.0 Project Template.
* [ ] Implement I2C Wrapper for INA219 (Telemetry).
* [ ] Create the "Enigma Path" SVG animation logic.
* [ ] Integrate JTAG programming library for EPM240/iCE40.
* [ ] Design the Bilingual "Typewriter" UI Theme.
* [ ] Finalize the "Time-to-Empty" Battery algorithm.
