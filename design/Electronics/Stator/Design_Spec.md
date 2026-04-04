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
* **Decoupling Rule:** Use **8x 0.1µF X7R** local decoupling capacitors per EPM240T100C5N IC (one per VCC pin).
* **Bulk Entry Bank Rule:** Use **5x 10uF X7R 50V** bulk decoupling capacitors near the Link-Beta power-entry pins in a **Symmetrical Star/Spoke pattern**.
* **Ferrite Bead Rule:** Use **4x ferrite beads** (one per 3V3_ENIG rotor feed) between Link-Beta entry and rotor power distribution to isolate switching transients from Controller logic.
* **Current Margin Check:** Rotor rail is budgeted at up to **5A peak total**; with 4 parallel feeds this is ~**1.25A per bead** nominal sharing, leaving strong margin versus **3.5A** bead rating.
* **JTAG Return:** Includes 10kΩ pull-up on TDO_RETURN at the Link-Beta exit.
* **Reset:** Pin 100 (DEV_CLRN) tied to the global SYS_RESET_N rail.

## 3. Interconnects

* **Controller Link (Link-Beta):** The **80-pin ERM8-040-05.0-S-DV-K-TR** male header on the Stator Board plugs into the matching ERF8-040 female socket on the Controller Board.
  * **Data In:** Receives JTAG, Reset from Controller.
  * **Data Out:** Transmits 12-bit Sniffer data to Controller.
  * **Power:** Receives 3V3_ENIG via the Controller pass-through for all backplane CPLDs.
  * **Cross-ref:** See `Controller/Design_Spec.md` Link-Beta mapping for explicit pin-number allocation; this Stator document mirrors that mapping for compatibility and implementation validation.
* **Encoder Interconnects:** 40-pin (2x20) 2.54mm Shrouded Box Headers (Power, ENC_DATA, JTAG).
* **Reflector/Extension Interconnect:** 20-pin (2x10) Vertical Shrouded Header (Power, ENC_DATA, TDO_Return).
  * **Routing:** Cables secured to the chassis floor with conductive EMI tape.
  * Extension boards enable daisy chaining this interconnect (to enable multi-stack rotor configurations).
  * **Cross-ref:** For matching interconnect pinouts on power (3V3_ENIG/GND), ENC_IN/ENC_OUT, and JTAG TDO_RETURN lines used for reflector loopback/plugboard mapping, See:
    * `Extension/Design_Spec.md`
    * `Reflector/Design_Spec.md`
* **Rotor Interconnect:** (Female on input side and Male on output side)
  * **JTAG:** 2x5 2.54mm Shrouded Header (GND|TCK|GND|TMS|GND|TDI|GND|RST|GND).
  * **Power:** 2X4 2.54mm Shrouded Header (4x3V3_ENIG, 4xGND).
  * **ENC DATA:** 2x6 2.54mm Shouded Header (ENC_IN [0:5], ENC_OUT [0:5]).
* **Diagnostics:** 2x8 ENIG Gold Diagnostic Looped Probe Pad Bank (L1, Mirror of Controller).

## 4. Power Telemetry (The "Encryption Load")

* **Purpose:** Provides real-time current/voltage data for the 30-rotor stack to the CM5 GUI.
* **Sensor:** TI INA219 Zero-Drift Power Monitor (Address: 0x45) — dedicated rotor-stack usage telemetry.
* **Placement:** Inserted on L1 (Top Layer) connected to the 3V3_ENIG rail immediately before the rotor stack.
  * Minimum 15mm isolation from Intel MAX II EPM240T100C5N CPLD logic core.
* **Shunt:** 20mΩ (1%) 0805 Current Sense Resistor (Rated for 2A continuous).
* **Interface:** I2C-1 Telemetry Bus (via Link-Beta, Shared with Power Module).
* **Filtering:** 0.1µF decoupling and RC filter on IN+/IN- for noise suppression from mechanical rotors.

## 5. EMI & Mechanical

* **Shield Mount:** 10mm ENIG Gold landing strip on L1 edge bonded to GND_CHASSIS.
* **Clamping:** Dual 3.2mm PTH anchors per cable for Galvanised Steel Bar compression.
* **Diagnostics:** 2x10 ENIG Gold Looped Probe Pad Bank mirrored to Controller's Bank-Beta pinout for A-B signal verification.

---

## Bill of Materials

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C1-C8 | Decoupling (8 per CPLD) | 0.1µF (X7R) 50V | 0402 | 81-GRM155R71A104KE1D | 311-1424-1-ND | C49678 |
| C9-C13 | Bulk entry decoupling bank (star/spoke) | 10uF X7R 50V | 1206 | 187-CL31B106KBHNNNE | 1276-6767-1-ND | CL31B106KBHNNNE |
| J1 | Link-Beta Connector | ERM8-040-05.0-S-DV-K-TR | 80-pin | 200-ERM8040050SDVKTR | SAM12064-ND | C123464 |
| J2 | 40-pin Rotor & Encoder power/data | 2x20 2.54mm shrouded | through-hole | 538-22-23-2401 | WM2921-ND | ??? |
| J3 | 20-pin Reflector/Extension | 2x10 2.54mm shrouded | through-hole | 538-22-23-2201 | WM2911-ND | ??? |
| L1-L4 | Rotor rail ferrite bead bank | 120 Ohm @ 100MHz, 3.5A | 1206 | 81-BLM31PG121SN1L | 490-1056-1-ND | BLM31PG121SN1L |
| R1 | Shunt Resistor | 20mΩ (1%) 0.5W | 0805 | 667-ERJ-6ENF20R0V | P20.0MYCT-ND | C123465 |
| R2 | JTAG TDO Pull-up | 10kΩ (1%) | 0603 | 667-ERJ-3EKF1002V | P10.0KBYCT-ND | C25804 |
| U1 | 3V3_ENIG Current/Voltage Sensing | INA219AIDR | SOT-23-6 | 595-INA219AIDR | 296-INA219AIDRCT-ND | C123466 |
