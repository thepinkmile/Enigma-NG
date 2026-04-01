# Enigma-NG Stator Board (Backplane)

The Stator Board is the mechanical and electrical backbone of the rotor stack. It provides the high-current distribution and signal routing for the 30 modular rotors.

## 1. Board Architecture

* **Stackup:** 4-Layer / 2oz Finished Copper.
* **Layer Mapping:** L1: JTAG | L2: GND | L3: 3V3_ENIG | L4: ENIG Data.
* **Role:** Master Switchboard for the 30-rotor stack and satellite encoders.

## 1. Core Features

* **Modular Slots:** 30x [Samtec CLP Series](https://www.samtec.com) low-profile female sockets.
* **Power Tree:** A massive 2oz copper pour for the `+3V3_ENIG` rail to handle the **5A peak** load without voltage sag.

## 2. Encryption & JTAG Hub

* **CPLD:** Intel MAX II EPM240T100C5N CPLD (Logic Router).
* **JTAG Return:** Includes 10kΩ pull-up on TDO_RETURN at the Link-Beta exit.
* **Reset:** Pin 100 (DEV_CLRN) tied to the global SYS_RESET_N rail.

## 3. Interconnects

* **Controller Link (Link-Beta):** The matching **80-pin ERF8-040-05.0-S-DV-K-TR** receptacle for the Controller Board (ERM8 Male Socket).
  * **Data In:** Receives JTAG, Reset from Controller.
  * **Data Out:** Transmits 12-bit Sniffer data to Controller.
  * **Power:** Receives 3V3_ENIG via the Controller pass-through for all backplane CPLDs.
* **Encoder Interconnects:** 40-pin (2x20) 2.54mm Shrouded Box Headers (Power, ENC_DATA, JTAG).
* **Reflector/Extension Interconnect:** 20-pin (2x10) Vertical Shrouded Header (Power, ENC_DATA, TDO_Return).
  * **Routing:** Cables secured to the chassis floor with conductive EMI tape.
  * Extension boards enable daisy chaining this interconnect (to enable multi-stack rotor configurations).
* **Rotor Interconnect:** (Female on input side and Male on output side)
  * **JTAG:** 2x5 2.54mm Shrouded Header (GND|TCK|GND|TMS|GND|TDI|GND|RST|GND).
  * **Power:** 2X4 2.54mm Shrouded Header (4x3V3_ENIG, 4xGND).
  * **ENC DATA:** 2x6 2.54mm Shouded Header (ENC_IN [0:5], ENC_OUT [0:5]).
* **Diagnostics:** 2x8 ENIG Gold Diagnostic Bank (L1, Mirror of Controller).

## 4. Power Telemetry (The "Encryption Load")

* **Purpose:** Provides real-time current/voltage data for the 30-rotor stack to the CM5 GUI.
* **Sensor:** TI INA219 Zero-Drift Power Monitor (Address: 0x45).
* **Placement:** Inserted on L1 (Top Layer) connected to the 3V3_ENIG rail immediately before the rotor stack.
  * Minimum 15mm isolation from Intel MAX II EPM240T100C5N CPLD logic core.
* **Shunt:** 20mΩ (1%) 0805 Current Sense Resistor (Rated for 2A continuous).
* **Interface:** I2C-1 Telemetry Bus (via Link-Beta, Shared with Power Module).
* **Filtering:** 0.1µF decoupling and RC filter on IN+/IN- for noise suppression from mechanical rotors.

## 5. EMI & Mechanical

* **Shield Mount:** 10mm ENIG Gold landing strip on L1 edge bonded to GND_CHASSIS.
* **Clamping:** Dual 3.2mm PTH anchors per cable for Galvanised Steel Bar compression.
* **Diagnostics:** 2x10 ENIG Gold Bank mirrored to Controller's Bank-Beta pinout for A-B signal verification.

---

## Bill of Materials

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # |
| :--- | :--- | :--- | :--- | :--- | :--- |
| U2 | 3V3_ENIG Current/Voltage Sensing | INA219AIDR | ??? | [INA219](https://ti.com) | ??? |
| R10 | Shunt Resistor | 20mΩ (1%) 0.5W | 0805 | ??? | ??? |
| R11 | JTAG TDO Pull-up | 10kΩ (1%) | 0603 | ??? | ??? |
| C30 | Decoupling | 0.1µF (X7R) 50V | 0603 | ??? | ??? |
