# Encoder Module (V1.0) Design Specification

A high-performance 64-node interface board.
Unlike static expanders, this module uses dual Altera MAX II CPLDs to handle real-time reciprocal encryption for the plugboard and de-bouncing for the 64-key QWERTY keyboard.

## 1. Power Requirements

* **Core:** 3.3V (Logic) & 1.8V (Internal) if required by CPLD variant.
* **Filtering:** Dedicated 0.1µF X7R decoupling per VCC pin.
* **Rule:** Intel MAX II EPM240T100C5N uses **8x 0.1µF** local decoupling capacitors per IC (one per VCC pin).
* **Bulk Entry Bank Rule:** Use **5x 10uF X7R 50V** bulk decoupling capacitors near the Data Link power-entry pins in a **Symmetrical Star/Spoke pattern**.
* **Protection:** AP22652 current-limited 3.3V rail from the Controller Board.

## 2. Dual-Role Architecture

* **Logic:** 2x Intel MAX II EPM240T100C5N CPLDs.
* **I/O Capacity:** Each CPLD provides 80 User I/O pins in a 100-pin TQFP package.
* **Roles:**
  * **HID Mode:**
    * **Keyboard:** Maps 64 mechanical plungers to the parallel data bus.
    * **Lightboard:** Maps parallel return data bus to the Lightboard (Lampboard) and CM5 for GUI feedback.
  * **Plugboard Mode:** Maps 64 "Stecker" jacks for reciprocal encryption.

## 3. Interconnects

* **Data Link:** 16-pin (2x8) 2.54mm shrouded header to support:
  * 2x 3V3_ENIG power pins
  * 2x GND pins
  * 6x ENC_IN bits (0:5)
  * 6x ENC_OUT bits (0:5)
* **I/O Terminals:** 2 rows of 64 spade terminal connections (inputs and outputs), one for each of the 64-character I/O path lines.
  * These terminals connect externally to the mechanical encoder/hardward assembly via a field-installable harness.
* **Routing:** Flexible cable / harness interface secured to the chassis floor with conductive EMI tape from the Stator Board.
* **Cornering:** 2.0mm Filleted PCB corners for enclosure fit.

## 4. Aesthetics

* **Silkscreen:** Bilingual German/English typewriter font.
* **Branding:** Inverted V1.0 Data Plate with Enigma Silhouette on Bottom (L4).

## 5. JTAG Chain Integrity

* **Buffering:** [74LVC1G125](https://www.ti.com) buffers on the TCK and TMS lines to maintain signal integrity across the long chain (2x I/O CPLDs + 30 Rotor FPGAs).
* **Termination:** 47Ω series resistors on the JTAG data lines to prevent reflections.
* **Chain Position:** The I/O CPLDs sit at the start of the JTAG chain, followed by the 30 Rotor FPGAs.
* **Programming:** Allows for "In-System Sources and Probes" debugging via the CM5 GUI.

## 6. Key Mapping (64-Way QWERTY for Keyboard)

* **Layout:** Standard QWERTY + Numbers + Symbols + Shift.
* **Debouncing:** Digital de-bounce implemented in the CPLD VHDL/Verilog, eliminating mechanical "key chatter."
* **Implementation:** The Shift keys (Left/Right) act as logic-level triggers for the CPLD state machine.
* **LED Drive:** CPLDs directly drive the **Shift Status LEDs** and the 64-character lamp matrix (via MOSFET arrays).

## 7. Plugboard Jack-Sensing

* **Logic:** The CPLD monitors 64 "Interrupt" lines from the Jack-Sensing sockets.
* **Latency:** Sub-microsecond detection of "Stecker" cable insertion, updating the internal encryption matrix instantly.

## 8. Thermal & ESD

* **ESD:** TPD4E001 arrays near the JTAG and Micro-Fit headers.
* **Thermal:** Vias under the Intel MAX II EPM240T100C5N CPLD "PowerPad" (if applicable) for heat dissipation.

## 10. PCB Specs (JLCPCB)

* **Layers:** 4-Layer (JLC04161H-7628).
* **Finish:** ENIG (Gold) for TQFP-100 pads.
* **Aesthetics:** Dark Green Solder Mask; Typewriter font (ALL-CAPS GERMAN).
* **Chip Placement:** CPLD #1 (Left-side 32 keys) and CPLD #2 (Right-side 32 keys) placed on the rear of the board to allow keys/lamps/sockets on the front.

---

## Bill of Materials

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C1-C16 | Decoupling (8 per CPLD, 2x CPLDs) | 0.1µF X7R 10V | 0402 | 81-GRM155R71A104KE1D | 311-1424-1-ND | C49678 |
| C17-C21 | Bulk entry decoupling bank (star/spoke) | 10uF X7R 50V | 1206 | 187-CL31B106KBHNNNE | 1276-6767-1-ND | CL31B106KBHNNNE |
| J1 | Plugboard Jack Sockets | 3.5/4mm | Through-hole | ??? | ??? | ??? |
| J2 | Data Link Connector | 16-pin 2x8 shrouded | 2.54mm | 538-22-23-2161 | WM2907-ND | ??? |
| J3 | Diagnostic looped probe pads | 2x8 ENIG Gold | 2.54mm | ??? | ??? | ??? |
| SW1-64 | Keyboard Switches | Cherry MX style | 3-pin | ??? | ??? | ??? |
| U1, U2 | Intel MAX II CPLD | EPM240T100C5N | TQFP-100 | 989-EPM240T100C5N | 544-EPM240T100C5N-ND | C123470 |
| U3 | LDO Regulator | TLV755P | SOT-23 | 595-TLV755PDBVR | 296-TLV755PDBVRCT-ND | C291923 |
