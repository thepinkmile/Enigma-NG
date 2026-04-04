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
* **Stecker Jack Sockets (×64):** 6.35mm (¼″) mono switched panel-mount jack sockets, one per character position.
  * Mounted in the plugboard panel; connect to the PCB via a field-installable spade-terminal harness.
  * **Tip terminal** → ENC signal path (CPLD I/O bus, Row 1 spade bank BT1–BT64).
  * **Switch contact** → insertion-detect interrupt line to CPLD (Row 2 spade bank BT65–BT128).
  * **Sleeve** → chassis GND direct (no spade required).
  * Part: 6.35mm (¼″) mono switched panel-mount jack — purchased (SaiBuy.Ltd, eBay item 334364197440, £1.66/unit × 64).
* **PCB Spade Terminal Banks (×128):** 6.35mm (¼″) straight vertical PCB-mount male blade tabs, 2 per jack (128 total).
  * **BT1–BT64:** Row 1 — ENC signal paths (Tip connections).
  * **BT65–BT128:** Row 2 — Insertion-detect lines (Switch contact connections).
  * Arranged in two parallel rows of 64, pitched to accept a standard 6.35mm female crimp spade harness.
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

* **Logic:** The CPLD monitors 64 insertion-detect lines (BT65–BT128, Switch contacts) from the Stecker jack sockets.
* **Signal:** Each jack Switch contact is normally closed (connected to Tip) when no plug is inserted; the contact opens on plug insertion, pulling the CPLD input low via an internal or external pull-up.
* **Latency:** Sub-microsecond detection of Stecker cable insertion, updating the internal encryption matrix instantly.
* **Harness:** 64× 2-wire assemblies (Tip + Switch), each terminated with 6.35mm female crimp spade terminals, connecting the panel-mount jacks to BT1–BT128 on the PCB.

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
| BT1-128 | PCB spade blade terminals (2 per jack, 128 total) | 6.35mm (¼″) straight vertical PCB-mount male blade tab — Row 1 (BT1-64): ENC Tip signal; Row 2 (BT65-128): Switch insertion-detect | Through-hole vertical | 534-1285 | A33376-ND | — |
| J1 (×64) | Stecker jack sockets | 6.35mm (¼″) mono switched panel-mount jack — Tip → ENC signal; Switch contact → insertion-detect; Sleeve → GND. **Already purchased.** | Panel-mount | — (eBay: SaiBuy.Ltd item 334364197440, £1.66/unit) | — | — |
| J2 | Data Link Connector | 16-pin 2x8 shrouded | 2.54mm | 538-22-23-2161 | WM2907-ND | ??? |
| J3 | Diagnostic looped probe pads | 2x8 ENIG Gold | 2.54mm | ??? | ??? | ??? |
| SW1-64 | Keyboard Switches | Cherry MX style | 3-pin | ??? | ??? | ??? |
| U1, U2 | Intel MAX II CPLD | EPM240T100C5N | TQFP-100 | 989-EPM240T100C5N | 544-EPM240T100C5N-ND | C123470 |
| U3 | LDO Regulator | TLV755P | SOT-23 | 595-TLV755PDBVR | 296-TLV755PDBVRCT-ND | C291923 |
