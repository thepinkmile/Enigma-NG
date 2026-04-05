# Encoder Module (V1.0) Design Specification

**Status:** Draft
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-04

## 1. Overview

A high-performance 64-node interface board.
Unlike static expanders, this module uses dual Altera MAX II CPLDs to handle real-time reciprocal encryption for the plugboard and de-bouncing for the 64-key QWERTY keyboard.

## 2. Power Requirements

* **Core:** 3.3V (Logic) powered directly from the AP22652 current-limited output on the Controller Board.
  No local LDO is fitted on the Encoder board — the 3V3_ENIG rail arrives via J2 (Data Link, pin 1 and pin 26) from the Stator, which distributes it from the Controller AP22652 output.
* **Filtering:** Dedicated 0.1µF X7R decoupling per VCC pin.
* **Rule:** Intel MAX II EPM240T100C5N uses **8x 0.1µF** local decoupling capacitors per IC (one per VCC pin).
* **Bulk Entry Bank Rule:** Use **5x 10uF X7R 50V** bulk decoupling capacitors near the Data Link power-entry pins in a **Symmetrical Star/Spoke pattern**.

## 3. Dual-Role Architecture

* **Logic:** 2x Intel MAX II EPM240T100C5N CPLDs.
* **I/O Capacity:** Each CPLD provides 80 User I/O pins in a 100-pin TQFP package.
* **Roles:**
  * **HID Mode:**
    * **Keyboard:** Maps 64 mechanical plungers to the parallel data bus.
    * **Lightboard:** Maps parallel return data bus to the Lightboard (Lampboard) and CM5 for GUI feedback.
  * **Plugboard Mode:** Maps 64 "Stecker" jacks for reciprocal encryption.

## 4. Interconnects

* **Data Link (J2):** 26-pin (2×13) 2.54mm shrouded box header with polarisation key.
  > **Connector Definition Owner:** `Stator/Board_Layout.md — J6–J8`.
  > This board uses the mating connector (see BOM for part number). The authoritative 26-pin pinout
  > is defined on the Stator; Pin 1 = 3V3_ENIG, Pins 2–7 = ENC_IN[0:5], Pin 8 = GND, Pins 9–17 = JTAG
  > (TCK/GND/TMS/GND/TDO/GND/TDI/GND/SYS_RESET_N), Pin 18 = GND, Pins 19–24 = ENC_OUT[0:5],
  > Pin 25 = GND, Pin 26 = 3V3_ENIG. See `Stator/Board_Layout.md` J6–J8 for full pin table.
* **Status LEDs (×2):** One active-low debug LED per CPLD. CPLD output LOW = LED ON.
  330Ω current-limiting resistor per LED; ~4mA drive current at 3.3V.
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
* **Keyboard Switches (×64):** DPDT 6-pin momentary push-button switches, one per key position.
  * Mounted in the keyboard panel (mechanical chassis); connect to the PCB via a field-installable spade-terminal harness.
  * **Pole 1 — COM1 + NO1** → key-press signal path to CPLD input (Row 3 spade bank BT129–BT192 COM, BT193–BT256 NO).
  * **Pole 2 pins (3×)** → mechanically soldered to PCB for physical key anchoring only; **no electrical connection**.
  * **NC1** → not connected.
  * Keys connect only to the keyboard side of the Encoder board; there is no direct switch connection to the Lightboard.
  * Part: DPDT 2-pole 6-pin push button switch — purchased (gadgetkingdom, eBay, 2 per pack).
* **PCB Spade Terminal Banks — Keyboard (×128):** 6.35mm (¼″) straight vertical PCB-mount male blade tabs, 2 per switch (128 total).
  * **BT129–BT192:** Row 3 — KEY_COM lines (switch COM1 to CPLD input reference rail).
  * **BT193–BT256:** Row 4 — KEY_NO lines (switch NO1 → CPLD key-press input, active-low via pull-up).
* **Diagnostic Probe Bank (J3):** 2×8 ENIG-finished bare PCB test pad array at 2.54mm pitch.
  Not a separate connector — bare gold pads probed directly with logic analyser clips or ICT fixtures.
  Mirrors the Data Link signals: Row 1 = 3V3_ENIG, GND, ENC_IN[0:5]; Row 2 = 3V3_ENIG, GND, ENC_OUT[0:5].
  See `Encoder/Board_Layout.md` Diagnostic Bank section for full pad map.
  Part number: N/A (PCB footprint only — no mating connector required).

## 5. Aesthetics

* **Silkscreen:** Bilingual German/English typewriter font.
* **Branding:** Inverted V1.0 Data Plate with Enigma Silhouette on Bottom (L4).

## 6. JTAG Chain Integrity

* **Buffering:** [74LVC1G125](https://www.ti.com) buffers on the TCK and TMS lines to maintain signal integrity across the long chain (2x I/O CPLDs + 30 Rotor FPGAs).
* **Termination:** 47Ω series resistors on the JTAG data lines to prevent reflections.
* **Trace Width Rule:** All JTAG signal traces on L1 shall be routed at **0.127 mm (5 mil)** over
  the L2 GND plane, targeting **50 Ω controlled impedance**. See
  `design/Electronics/Investigations/JTAG_Integrity.md` and DEC-016.
* **Pull Resistors (×4, placed near CPLDs):**
  * **TMS:** 10kΩ pull-up to 3V3_ENIG (R3) — ensures JTAG TAP resets to Test-Logic-Reset on power-up and when controller is idle.
  * **TDI:** 10kΩ pull-up to 3V3_ENIG (R4) — holds TDI at logic-1 (BYPASS instruction) when not actively driven.
  * **TCK:** 10kΩ pull-down to GND (R5) — prevents spurious clocking when TCK line is floating.
  * **SYS_RESET_N:** 10kΩ pull-up to 3V3_ENIG (R6) — active-low signal; pull-up ensures CPLDs remain out of reset by default.
  * One set of four is sufficient per board; TCK, TMS and SYS_RESET_N are broadcast nets
    shared between both CPLDs.
* **Series Termination — Inter-CPLD (R7, 33Ω):** Placed within 2 mm of CPLD1 TDO, on the trace
  to CPLD2 TDI. Source impedance ≈ 53 Ω, matched to the 50 Ω intra-board PCB trace.
  See `design/Electronics/Investigations/JTAG_Integrity.md` Option D.
* **Series Termination — Cable Output (R8, 75Ω):** Placed within 2 mm of CPLD2 TDO, before J2
  connector pin 13. Source impedance ≈ 95 Ω, targeting the ~100 Ω IDC ribbon cable impedance.
  Full logic swing is maintained at the Stator via the open-circuit reflection doubling effect.
* **Chain Position:** The I/O CPLDs (HID/Plugboard) sit second in the JTAG chain, after the Stator CPLD.
  Full order: FT232H → Stator CPLD → HID Encoder CPLD1→CPLD2 → Plugboard A CPLD1→CPLD2 → Plugboard B CPLD1→CPLD2 → Rotors → Reflector → TDO_RETURN.
* **Programming:** Allows for "In-System Sources and Probes" debugging via the CM5 GUI.

## 7. Key Mapping (64-Way QWERTY for Keyboard)

* **Layout:** Standard QWERTY + Numbers + Symbols + Shift.
* **Debouncing:** Digital de-bounce implemented in the CPLD VHDL/Verilog, eliminating mechanical "key chatter."
* **Implementation:** The Shift keys (Left/Right) act as logic-level triggers for the CPLD state machine.
* **LED Drive:** CPLDs directly drive the **Shift Status LEDs** and the 64-character lamp matrix (via MOSFET arrays).

## 8. Plugboard Jack-Sensing

* **Logic:** The CPLD monitors 64 insertion-detect lines (BT65–BT128, Switch contacts) from the Stecker jack sockets.
* **Signal:** Each jack Switch contact is normally closed (connected to Tip) when no plug is inserted; the contact opens on plug insertion, pulling the CPLD input low via an internal or external pull-up.
* **Latency:** Sub-microsecond detection of Stecker cable insertion, updating the internal encryption matrix instantly.
* **Harness:** 64× 2-wire assemblies (Tip + Switch), each terminated with 6.35mm female crimp spade terminals, connecting the panel-mount jacks to BT1–BT128 on the PCB.

## 9. Thermal & ESD

* **ESD:** TPD4E001 arrays near the JTAG and Micro-Fit headers.
* **Thermal:** Vias under the Intel MAX II EPM240T100C5N CPLD "PowerPad" (if applicable) for heat dissipation.

## 10. PCB Specs (JLCPCB)

* **Layers:** 4-Layer (JLC04161H-7628).
* **Finish:** ENIG (Gold) for TQFP-100 pads.
* **Aesthetics:** Dark Green Solder Mask; Typewriter font (ALL-CAPS GERMAN).
* **Chip Placement:** CPLD #1 (Left-side 32 keys) and CPLD #2 (Right-side 32 keys) placed on the rear of the board to allow keys/lamps/sockets on the front.

---

## 11. Bill of Materials

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C1-C16 | Decoupling (8 per CPLD, 2x CPLDs) | 0.1µF X7R 10V | 0402 | 81-GRM155R71A104KE1D | 311-1424-1-ND | C49678 |
| C17-C21 | Bulk entry decoupling bank (star/spoke) | 10uF X7R 50V | 1206 | 187-CL31B106KBHNNNE | 1276-6767-1-ND | CL31B106KBHNNNE |
| BT1-128 | PCB spade blade terminals (2 per jack, 128 total) | 6.35mm (¼″) straight vertical PCB-mount male blade tab — Row 1 (BT1-64): ENC Tip signal; Row 2 (BT65-128): Switch insertion-detect | Through-hole vertical | 534-1285-ST | 36-1285-ST-ND | C5370868 |
| J1 (×64) | Stecker jack sockets | 6.35mm (¼″) mono switched panel-mount jack — Tip → ENC signal; Switch contact → insertion-detect; Sleeve → GND. **Already purchased.** | Panel-mount | — (eBay: SaiBuy.Ltd item 334364197440, £1.66/unit) | — | — |
| D1, D2 | Status LED (one per CPLD, active-low) | Green SMD LED, **V_f = 2.0V @ 10mA (≈1.9V @ 4mA)** | 0402 | 710-150060VS75000 | 732-5015-1-ND | C2286 |
| J2 | Data Link Connector | 26-pin 2×13 shrouded box header, 2.54mm | 2.54mm | 538-22-23-2261 | WM2913-ND | ??? |
| J3 | Diagnostic probe pad bank (bare ENIG gold pads — logic analyser / ICT access) | 2×8 bare PCB pads | 2.54mm | N/A | N/A | N/A |
| SW1-64 | Keyboard Switches | DPDT 6-pin momentary push button — Pole 1: COM1+NO1 → key-press to CPLD; Pole 2: reserved (lamp/redundancy TBD). **Already purchased.** | Panel-mount | — (eBay: gadgetkingdom, 2 per pack) | — | — |
| BT129-192 | PCB spade blade terminals — KEY_COM (Row 3) | Keystone 1285-ST — 6.35mm straight vertical PCB-mount male blade tab. COM1 of each keyboard switch pole-1. | Through-hole vertical | 534-1285-ST | 36-1285-ST-ND | C5370868 |
| BT193-256 | PCB spade blade terminals — KEY_NO (Row 4) | Keystone 1285-ST — same part. NO1 of each keyboard switch pole-1; CPLD key-press input (active-low). | Through-hole vertical | 534-1285-ST | 36-1285-ST-ND | C5370868 |
| U1, U2 | Intel MAX II CPLD | EPM240T100C5N | TQFP-100 | 989-EPM240T100C5N | 544-EPM240T100C5N-ND | C123470 |
| R1, R2 | LED current limiting resistors | 330Ω 1% | 0402 | 667-ERJ-2RKF3300X | P330LBCT-ND | C105872 |
| R3 | TMS pull-up to 3V3_ENIG | 10kΩ 1% | 0402 | 667-ERJ-2RKF1002X | P10.0KLBCT-ND | C25744 |
| R4 | TDI pull-up to 3V3_ENIG | 10kΩ 1% | 0402 | 667-ERJ-2RKF1002X | P10.0KLBCT-ND | C25744 |
| R5 | TCK pull-down to GND | 10kΩ 1% | 0402 | 667-ERJ-2RKF1002X | P10.0KLBCT-ND | C25744 |
| R6 | SYS_RESET_N pull-up to 3V3_ENIG | 10kΩ 1% | 0402 | 667-ERJ-2RKF1002X | P10.0KLBCT-ND | C25744 |
| R8 | TDO output series R (CPLD2 TDO → J2 pin 13, ribbon cable drive) | 75Ω 1% | 0402 | 667-ERJ-2RKF75R0X | P75.0LBCT-ND | ??? |

> **Design decision history:** See `design/Design_Log.md` for all formal design decisions (DEC-xxx) applicable to this board.
