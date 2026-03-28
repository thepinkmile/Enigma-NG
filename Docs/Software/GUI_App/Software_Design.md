# Enigma-NG Software Design: C# GUI Application

## 1. Core Framework

* **Version:** .NET 10.0 (C#)
* **UI Library:** Avalonia UI (for hardware-accelerated Skia rendering on Linux/CM5).
* **Architecture:** MVVM (Model-View-ViewModel) for clean separation between hardware I/O and the display.

## 2. Primary Dashboard Features

* **The Virtual Enigma:** A 3D or high-res 2D representation of the 30-rotor stack.
* **Live Power Telemetry:** Real-time Gauges for Voltage, Current (mA), and Power (W) sourced from the INA219.
* **Source Indicators:** Dynamic icons for PoE+, USB-C, and Battery (with "Time-to-Empty" countdown).
* **Thermal Monitor:** CPU and eFuse temperature tracking with bilingual "HOT" alerts.

## 3. Cryptographic Visualization

* **Signal Path Trace:** A "light-trail" animation showing the 12-bit signal traveling from the Keyboard, through the Plugboard, through the 30 rotors, hitting the Reflector (Umkehrwalze), and returning to the Lampboard.
* **Rotor Configurator:** Drag-and-drop interface to "program" historical wiring (I-VIII) into the CPLDs/FPGAs.
