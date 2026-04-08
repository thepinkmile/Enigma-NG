# Encoder Module (V1.0) Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-05

## 1. Overview

A multi-purpose Human Interface Device (HID). Comprised of 2 Altera MAX II CPLDs and dual banks of 64 spade
connectors ensuring this board can be used as a single plugboard pass, or a dual function keyboard and lightboard.
When utilised for a plugboard, 2 of these boards will be required, enabling the plugboard to be connected in 2 possible
locations (e.g. the original Enigma machine had this connected both between the Keyboard and first rotor for input and
between the first rotor and lightboard (a.k.a. lampboard) for the output).
When used for the dual function of keyboard and lightboard, one half of the board acts as the keyboard input encoder and
provides the 6-bit digital input to the system and the other half acts as the lightboard decoder and consumes the final
6-bit digital output to highlight the relevant character light.
Regardless of the physical plugboard, keyboard or lightboard features, this board will be the same for all devices
(e.g. a 26 character set plugboard is the same as a 64 character set plugboard, with the only difference being the
number of Keys, Lights or Plug Jacks connected to the spade terminals).

### Functional & Design Requirements

#### Functional Requirements

| ID | Functional Requirement | Notes | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| FR-ENC-01 | Sense and encode 64-key keyboard and plugboard jack states with sufficient resolution for per-character detection | Must detect individual keypresses and plugboard patch states without ghosting or chatter | §3 Dual-Role Architecture; BOM U1, U2 (EPM240T100I5N) |
| FR-ENC-02 | Transmit encoded character (or 'base-64 binary' in the case of binary file encoding) data to the Stator Board via IDC ribbon cable | 26-pin IDC interface | §4 Interconnects; BOM J2 (26-pin shrouded header) |
| FR-ENC-03 | Accept JTAG programming for the on-board CPLD from the Stator JTAG chain | Encoder CPLDs are devices 2–7 in the chain | §5 JTAG Chain Integrity; BOM U1, U2 (EPM240T100I5N) |
| ~~FR-ENC-04~~ | ~~Moved to Mechanical/Plugboard/Design_Spec.md~~ | ~~—~~ | ~~—~~ |
| FR-ENC-05 | Operate from 3V3_ENIG power supplied via the Stator ribbon cable | No local voltage regulation (LDO/switcher) required; local bulk and decoupling capacitor network per Global_Routing_Spec. | §2 Power Requirements; BOM J2 (pin 1/pin 26 = 3V3_ENIG) |

#### Design Requirements

| ID | Design Requirement | Specification | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| DR-ENC-01 | PCB stackup | 4-layer, 2oz finished copper (JLC04161H-7628) | §9 PCB Specs |
| DR-ENC-02 | CPLD | Intel MAX II EPM240T100I5N (TQFP-100) | §3 Dual-Role Architecture; BOM U1, U2 (EPM240T100I5N) |
| DR-ENC-03 | Stator interface connector | 26-pin Molex IDC (mates with Stator J4, J5, or J6) | §4 Interconnects; BOM J2 (26-pin 2×13 shrouded) |
| ~~DR-ENC-04~~ | ~~Moved to Mechanical/Plugboard/Design_Spec.md~~ | ~~—~~ | ~~—~~ |
| DR-ENC-05 | Supply voltage | 3.3V via the 3V3_ENIG power rail | §2 Power Requirements; BOM J2 (Data Link) |

## 2. Power Requirements

* **Core:** The Encoder Board receives its 3V3_ENIG power rail from the IDC cable connection from the Stator (pin 1 & 26). This could be connected to any of J4–J6 of the Stator Board.
* Decoupling and bulk entry capacitor requirements per `design/Standards/Global_Routing_Spec.md §3`.

## 3. Dual-Role Architecture

This board can be used to provide functionality for both the HID component or the plugboard (a single pass of it at least).
The encoder is essentially made up of an Encoder (which takes 64 inputs and encodes it to a 6-bit output), and a Decoder (which takes a 6-bit input and decodes it to 1 of 64 outputs).
So a single pass (or cable) for a plugboard plug, would used both encode and decode (decode data in, then transmit through the relevant plug, then back through the encode side).
However, the keyboard only requires the Encode side and the Lightboard only requires the Decode side, so these will likely be created as a singl component with a shared single board.

* **Logic:** 2x Intel MAX II EPM240T100I5N CPLDs.
* **I/O Capacity:** Each CPLD provides 80 User I/O pins in a 100-pin TQFP package.
* **Roles:**
  * **HID Mode:**
    * **Keyboard:** Maps 64 mechanical plungers to the parallel data bus.
    * **Lightboard:** Maps parallel return data bus to the Lightboard (Lampboard) and CM5 for GUI feedback.
  * **Plugboard Mode:** Maps 64 "Stecker" jacks for reciprocal encryption.

## 4. Interconnects

* **Data Link (J2):** 26-pin (2×13) 2.54mm shrouded box header with polarisation key.
  > **Connector Definition Owner:** `Stator/Board_Layout.md — J4–J6`.
  > See `design/Electronics/Stator/Board_Layout.md` — J4–J6 for the full pin table.
* **Status LEDs (×2):** One active-low debug LED per CPLD. CPLD output LOW = LED ON.
  330Ω current-limiting resistor per LED; ~4mA drive current at 3.3V.
* **Plugboard Jack Sockets:** See `design/Mechanical/Plugboard/Design_Spec.md`.
* **Keyboard Switches:** See `design/Mechanical/Keyboard/Design_Spec.md`.
* **PCB Spade Terminal Banks (2× banks of 64):** 6.35mm (¼″) straight vertical PCB-mount male blade tabs.
  * **Bank 1 (BT1–BT64):** Maps to CPLD 1.
  * **Bank 2 (BT65–BT128):** Maps to CPLD 2.
  * On the PCB, the two banks are horizontally aligned and vertically stacked so that corresponding pins are correlated,
    enabling correct plugboard wiring (where pin pairing matters). When used as a HID keyboard or lightboard,
    pin correlation is not functionally significant.
* **Diagnostic Probe Bank (J3):** 2×8 ENIG-finished bare PCB test pad array at 2.54mm pitch.
  Not a separate connector — bare gold pads probed directly with logic analyser clips or ICT fixtures.
  Mirrors the Data Link signals: Row 1 = 3V3_ENIG, GND, ENC_IN[0:5]; Row 2 = 3V3_ENIG, GND, ENC_OUT[0:5].
  See `Encoder/Board_Layout.md` Diagnostic Bank section for full pad map.
  Part number: N/A (PCB footprint only — no mating connector required).

## 5. JTAG Chain Integrity

* **Entry/Exit:** JTAG chain enters and exits via the IDC ribbon cable connection (J2) to the Stator Board.
* **Local Chain:** The Encoder Board contains 2 devices in its JTAG chain: CPLD 1 (U1) and CPLD 2 (U2). CPLD 1 TDO feeds CPLD 2 TDI.
* **Trace Width:** All JTAG signal traces on L1 shall be routed at **0.127 mm (5 mil)** over the L2 GND plane, targeting **50 Ω controlled impedance** per DEC-016. See `design/Electronics/Investigations/JTAG_Integrity.md`.
* **Pull Resistors (×4, placed near CPLDs):**
  * **TMS:** 10kΩ pull-up to 3V3_ENIG (R3) — ensures JTAG TAP resets to Test-Logic-Reset on power-up.
  * **TDI:** 10kΩ pull-up to 3V3_ENIG (R4) — holds TDI at logic-1 (BYPASS) when not driven.
  * **TCK:** 10kΩ pull-down to GND (R5) — prevents spurious clocking when TCK is floating.
  * **SYS_RESET_N:** 10kΩ pull-up to 3V3_ENIG (R6) — active-low; pull-up ensures CPLDs remain out of reset by default.
  * TCK, TMS, and SYS_RESET_N are broadcast nets shared between both CPLDs.
* **Termination:**
  * **Inter-CPLD (R7, 33Ω):** Series resistor placed within 2 mm of CPLD 1 TDO, on the trace to CPLD 2 TDI.
    Source impedance ≈ 53 Ω, matched to the 50 Ω intra-board PCB trace.
    See `design/Electronics/Investigations/JTAG_Integrity.md` Option D.
  * **Cable Output (R8, 75Ω):** Series resistor placed within 2 mm of CPLD 2 TDO, before J2 pin 13. Source impedance ≈ 95 Ω, targeting the ~100 Ω IDC ribbon cable impedance.
* **Programming:** Supports "In-System Sources and Probes" debugging via the CM5 GUI.

## 6. Key Mapping (64-Way QWERTY for Keyboard)

Key mapping implementation detail — including QWERTY layout, hardware RC de-bounce circuit,
Shift key state-machine logic, and LED drive — has been migrated to the Mechanical Keyboard
specification.

> See `design/Mechanical/Keyboard/Design_Spec.md §3 Key Mapping` for the full key mapping
> specification.

## 7. Plugboard Jack-Sensing

Plugboard jack-sensing implementation detail — including CPLD insertion-detect logic, switch contact
signal behaviour, sub-microsecond detection latency, and harness assembly — has been migrated to the
Mechanical Plugboard specification.

> See `design/Mechanical/Plugboard/Design_Spec.md §4 Plugboard Jack-Sensing` for the full
> jack-sensing specification.

## 8. Thermal & ESD

* **ESD:** TPD4E001 arrays near the JTAG and Micro-Fit headers.
* **Thermal:** Vias under the Intel MAX II EPM240T100I5N CPLD "PowerPad" (if applicable) for heat dissipation.

## 9. PCB Fabrication & Stackup

* **Layers:** 4-Layer (JLC04161H-7628).
* **Finish:** ENIG (Gold) for TQFP-100 pads.
* **Aesthetics:** Dark Green Solder Mask; Typewriter font (ALL-CAPS GERMAN).
* **Chip Placement:** CPLD #1 (Left-side 32 keys) and CPLD #2 (Right-side 32 keys) placed on the rear of the board to allow keys/lamps/sockets on the front.

---

## 10. Bill of Materials

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C1-C16 | Decoupling (8 per CPLD, 2x CPLDs) | 0.1µF X7R 10V | 0402 | 81-GRM155R71A104KE1D | 311-1424-1-ND | C49678 |
| C17-C21 | Bulk entry decoupling bank (star/spoke) | 10uF X7R 50V | 1206 | 187-CL31B106KBHNNNE | 1276-6767-1-ND | CL31B106KBHNNNE |
| BT1-128 | PCB spade blade terminals (2 per jack, 128 total) | 6.35mm (¼″) straight vertical PCB-mount male blade tab — Row 1 (BT1-64): ENC Tip signal; Row 2 (BT65-128): Switch insertion-detect | Through-hole vertical | 534-1285-ST | 36-1285-ST-ND | C5370868 |
| J1 (×64) | Stecker jack sockets | 6.35mm (¼″) mono switched panel-mount jack — Tip → ENC signal; Switch contact → insertion-detect; Sleeve → GND. **Already purchased.** | Panel-mount | — (eBay: SaiBuy.Ltd item 334364197440, £1.66/unit) | — | — |
| D1, D2 | Status LED (one per CPLD, active-low) | Green SMD LED, **V_f = 2.0V @ 10mA (≈1.9V @ 4mA)** | 0402 | 710-150060VS75000 | 732-5015-1-ND | C2286 |
| J2 | Data Link Connector | 26-pin 2×13 shrouded box header, 2.54mm | 2.54mm | 538-22-23-2261 | WM2913-ND | N/A — Molex THT shrouded header, not stocked at JLCPCB; order from Mouser/DigiKey |
| J3 | Diagnostic probe pad bank (bare ENIG gold pads — logic analyser / ICT access) | 2×8 bare PCB pads | 2.54mm | N/A | N/A | N/A |
| SW1-64 | Keyboard Switches | DPDT 6-pin momentary push button — Pole 1: COM1+NO1 → key-press to CPLD; Pole 2: reserved (*Open item — lamp/redundancy function TBD*). **Already purchased.** | Panel-mount | — (eBay: gadgetkingdom, 2 per pack) | — | — |
| BT129-192 | PCB spade blade terminals — KEY_COM (Row 3) | Keystone 1285-ST — 6.35mm straight vertical PCB-mount male blade tab. COM1 of each keyboard switch pole-1. | Through-hole vertical | 534-1285-ST | 36-1285-ST-ND | C5370868 |
| BT193-256 | PCB spade blade terminals — KEY_NO (Row 4) | Keystone 1285-ST — same part. NO1 of each keyboard switch pole-1; CPLD key-press input (active-low). | Through-hole vertical | 534-1285-ST | 36-1285-ST-ND | C5370868 |
| U1, U2 | Intel MAX II CPLD | EPM240T100I5N | TQFP-100 | 989-EPM240T100I5N | 544-2276-ND | C40067 |
| R1, R2 | LED current limiting resistors | 330Ω 1% | 0402 | 667-ERJ-2RKF3300X | P330LBCT-ND | C105872 |
| R3 | TMS pull-up to 3V3_ENIG | 10kΩ 1% | 0402 | 667-ERJ-2RKF1002X | P10.0KLBCT-ND | C25744 |
| R4 | TDI pull-up to 3V3_ENIG | 10kΩ 1% | 0402 | 667-ERJ-2RKF1002X | P10.0KLBCT-ND | C25744 |
| R5 | TCK pull-down to GND | 10kΩ 1% | 0402 | 667-ERJ-2RKF1002X | P10.0KLBCT-ND | C25744 |
| R6 | SYS_RESET_N pull-up to 3V3_ENIG | 10kΩ 1% | 0402 | 667-ERJ-2RKF1002X | P10.0KLBCT-ND | C25744 |
| R7 | Inter-CPLD series termination (CPLD1 TDO → CPLD2 TDI) | 33Ω 1% | 0402 | 667-ERJ-2RKF33R0X | P33.0LBCT-ND | C25808 |
| R8 | TDO output series R (CPLD2 TDO → J2 pin 13, ribbon cable drive) | 75Ω 1% | 0402 | 667-ERJ-2RKF75R0X | P75.0LBCT-ND | *Open item — verify JLCPCB part number* |
