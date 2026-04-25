# Encoder Module (V1.0) Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-20

## 1. Overview

The Encoder Module is a **single-sided generic 64-line interface board**. Each PCB contains one
Intel MAX II CPLD, one bank of 64 spade terminals, one 20-pin IDC data-link connector, and the
shared JTAG chain connection on that same cable. The same PCB is reused in six system roles:

- `KBD_ENC` — keyboard encode module
- `LBD_DEC` — lightboard decode module
- `PLG_PASS1_DEC` — plugboard pass 1 decode module
- `PLG_PASS1_ENC` — plugboard pass 1 encode module
- `PLG_PASS2_DEC` — plugboard pass 2 decode module
- `PLG_PASS2_ENC` — plugboard pass 2 encode module

The **20-pin ribbon pinout does not change**. Role is determined by CPLD image and assembly
population, not by connector rewiring. The board itself exposes only the generic `ENC_DATA[5:0]`
service bus on `J2`; role-specific signal names are owned by the Stator.

### Plugboard Use (4 modules required)

Each plugboard pass is implemented as a paired decode / encode module set:

```text
Stator alias `ENC_OUT_PLGx[5:0]`
       ↓
PLG_PASSx_DEC `ENC_DATA[5:0]`  ->  64 passive jack lines  ->  PLG_PASSx_ENC `ENC_DATA[5:0]`
                                                                     ↓
                                                        Stator alias `ENC_IN_PLGx[5:0]`
```

With no patch cable inserted, the jack's normally-closed contact preserves identity mapping. The
full Plugboard Assembly contains two such passes.

### HID Use (2 modules required)

The HID path is split mechanically and electrically:

- **`KBD_ENC`:** reads the keyboard switch matrix subset and returns 6-bit `ENC_DATA[5:0]` to the
  Stator (`ENC_IN_KBD[5:0]` on the Stator side).
- **`LBD_DEC`:** receives 6-bit `ENC_DATA[5:0]` from the Stator (`ENC_OUT_LBD[5:0]` on the Stator
  side) and asserts one of up to 64 output lines for the lightboard.

### Functional & Design Requirements

#### Functional Requirements

| ID | Functional Requirement | Notes | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| FR-ENC-01 | Sense and encode the 64-character logical HID repertoire plus the 64-node plugboard interface with sufficient resolution for per-character detection | HID keyboard mode uses a 40-position physical layout (`[a-z0-9+=]` plus Left/Right Shift), while plugboard roles retain the full 64-line capacity | §3 Single-Module Architecture; §6 Key Mapping; BOM U1 (EPM240T100I5N) |
| FR-ENC-02 | Transmit or receive the 6-bit service bus to/from the Stator Board via IDC ribbon cable | 20-pin IDC interface; local connector always exposes generic `ENC_DATA[5:0]` | §4 Interconnects; BOM J2 |
| FR-ENC-03 | Accept JTAG programming for the on-board CPLD from the Stator JTAG chain | One CPLD per module; six modules occupy six chain positions ahead of the rotor stack | §5 JTAG Chain Integrity; BOM U1 |
| FR-ENC-04 | Operate from 3V3_ENIG power supplied via the Stator ribbon cable | No local voltage regulation required; local bulk and decoupling capacitor network per `design/Standards/Global_Routing_Spec.md §3`. | §2 Power Requirements; BOM J2 |

#### Design Requirements

| ID | Design Requirement | Specification | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| DR-ENC-01 | PCB stackup | 4-layer, 2oz finished copper (JLC04161H-7628) | §9 PCB Fabrication & Stackup |
| DR-ENC-02 | CPLD | Intel MAX II EPM240T100I5N (TQFP-100) | §3 Single-Module Architecture; BOM U1 |
| DR-ENC-03 | Stator interface connector | 20-pin 2×10 IDC (mates with one Stator encoder port) | §4 Interconnects; BOM J2 |
| DR-ENC-04 | Supply voltage | 3.3V via the 3V3_ENIG power rail | §2 Power Requirements; BOM J2 |

## 2. Power Requirements

- **Core:** The Encoder Module receives its 3V3_ENIG power rail from the IDC cable connection from
  the Stator (pin 1 and pin 20). This may connect to any of the six Stator encoder ports.
- Decoupling and bulk entry capacitor requirements per
  `design/Standards/Global_Routing_Spec.md §3`.

### GND_CHASSIS Single-Point Bond

Per `design/Standards/Global_Routing_Spec.md §5`, the Encoder board implements a local
`GND_CHASSIS` net tied to its mounting holes and any deliberate enclosure-contact or shield-contact
features, but it does **not** implement a local GND-to-GND_CHASSIS bond. The system's only
galvanic GND ↔ GND_CHASSIS bond remains on the Power Module at the common power-entry point
immediately before the eFuse.

## 3. Single-Module Architecture

Each Encoder Module contains one Intel MAX II EPM240T100I5N CPLD and one bank of 64 spade terminals.
The board is intentionally generic so the same PCB may be populated and programmed as either a
decoder or an encoder.

### Role Definitions

| Role | 6-bit bus used | 64-line bank use | Function |
| :--- | :--- | :--- | :--- |
| **Decode role** (`LBD_DEC`, `PLG_PASS1_DEC`, `PLG_PASS2_DEC`) | `ENC_DATA[5:0]` consumed from Stator | Board drives one of 64 lines | Decodes 6-bit input into a one-of-64 asserted output |
| **Encode role** (`KBD_ENC`, `PLG_PASS1_ENC`, `PLG_PASS2_ENC`) | `ENC_DATA[5:0]` driven back to Stator | Board reads one of 64 lines | Encodes one asserted line into a 6-bit output |

### Signal Flow — Plugboard Pass

```text
Stator alias `ENC_OUT_PLGx[5:0]`
       ↓
  Decode-role Encoder Module
       ↓
  64-line jack field
       ↓
  Encode-role Encoder Module
       ↓
Stator alias `ENC_IN_PLGx[5:0]`
```

### Signal Flow — HID

```text
Keyboard Assembly:                    Lightboard Assembly:
40 populated switch lines             Stator alias `ENC_OUT_LBD[5:0]`
            ↓                                  ↓
       KBD_ENC                             LBD_DEC
            ↓                                  ↓
Stator alias `ENC_IN_KBD[5:0]`        one-of-64 light output
```

### I/O Capacity

Each CPLD provides enough user I/O for one 64-line interface bank plus JTAG, status LED, power, and
the 6-bit ribbon interface.

## 4. Interconnects

- **Data Link (J2):** 20-pin (2×10) 2.54 mm shrouded box header with polarisation key.
  > **Connector Definition Owner:** `Stator/Board_Layout.md — J4/J5/J6/J7/J8/J9`.
  > See `design/Electronics/Stator/Board_Layout.md` for the authoritative pin table.
- **Status LED (D1):** one active-low debug LED per CPLD. CPLD output LOW = LED ON.
  330 Ω current-limiting resistor; ~4 mA drive current at 3.3 V.
- **Keyboard Switches:** see `design/Mechanical/Keyboard_Assembly/Design_Spec.md`.
- **Lightboard Harness:** see `design/Mechanical/Lightboard_Assembly/Design_Spec.md`.
- **Plugboard Jack Sockets:** see `design/Mechanical/Plugboard_Assembly/Design_Spec.md`.
- **PCB Spade Terminal Bank (BT1–BT64):** 6.35 mm (1/4") straight vertical PCB-mount male blade
  tabs.
  - **Decode role:** wired to lightboard lamps or to plugboard jack Tip + Switch terminals.
  - **Encode role:** wired to keyboard switch outputs or to plugboard jack Sleeve terminals.
  - Initial Rev A HID assemblies may populate only **26** or **40** positions, but the PCB retains
    all 64 terminals for future custom layouts.

## 5. JTAG Chain Integrity

- **Entry/Exit:** JTAG enters and exits via the IDC ribbon cable connection (J2) to the Stator.
- **Local Chain:** one JTAG device per Encoder Module: U1 only.
- **Trace Width:** all JTAG signal traces on L1 shall be routed at **0.127 mm (5 mil)** over the L2
  GND plane, targeting **50 Ω controlled impedance** per DEC-016. See
  `design/Electronics/Investigations/JTAG_Integrity.md`.
- **Pull Resistors (×4, placed near U1):**
  - **TMS:** 10 kΩ pull-up to 3V3_ENIG (R2)
  - **TDI:** 10 kΩ pull-up to 3V3_ENIG (R3)
  - **TCK:** 10 kΩ pull-down to GND (R4)
  - **SYS_RESET_N:** 10 kΩ pull-up to 3V3_ENIG (R5)
- **Termination:**
  - **Cable Output (R6, 75 Ω):** series resistor placed within 2 mm of U1 TDO, before J2 pin 13.
- **Programming:** Supports in-system debugging via the CM5 GUI.

## 6. Key Mapping (64-Character Code Space with 40-Position HID Layout)

The encode-role Encoder Module maps the HID assembly's physical switch positions to the parallel
6-bit data bus while preserving the machine's 64-character logical repertoire.

- **Layout:** QWERTY-derived 40-position HID panel consisting of 38 printable keys
  (`[a-z0-9+=]`) plus Left Shift and Right Shift.
- **Logical repertoire:** the system still exposes 64 unique character codes:
  26 lowercase letters + 26 uppercase letters + 10 digits + `+` + `=`.
- **Signal polarity:** encode-role lines are **active-low**. The external 10 kΩ pull-up to
  3V3_ENIG holds each CPLD input HIGH when a key is not pressed. Key press closes the switch
  contact to GND, pulling the CPLD input LOW.
- **Debouncing:** the encode-role population uses a hardware RC debounce circuit per input line:
  10 kΩ pull-up resistor to 3V3_ENIG + 100 nF X7R capacitor to GND on each used input line
  (RC time constant τ = 1 ms).
- **Shift Logic:** Left Shift and Right Shift act as logic-level triggers for the CPLD state
  machine. When either Shift key is held, alphabetic key positions map to `A-Z` instead of `a-z`.
  Digits and `+` / `=` remain unchanged.
- **Lightboard mapping:** the decode-role lightboard module mirrors the same QWERTY-derived
  printable positions. Uppercase alphabetic outputs illuminate the corresponding alphabetic lamp
  position rather than a separate uppercase-only physical position.

> For keyboard switch mechanical specification and panel assembly, see
> `design/Mechanical/Keyboard_Assembly/Design_Spec.md`.
>
## 7. Plugboard Jack-Sensing

The board split does **not** remove the requirement for plugboard insertion-state awareness, but it
does move the implementation decision to the per-pass harness / schematic phase. Any sensing scheme
must preserve the generic one-CPLD module footprint and the unchanged 20-pin IDC pinout.

> For jack panel layout and harness assembly, see
> `design/Mechanical/Plugboard_Assembly/Design_Spec.md`.
>
## 8. Thermal & ESD

- **Thermal:** vias under the Intel MAX II EPM240T100I5N CPLD power pins / thermal area as required
  by layout review.

## 9. PCB Fabrication & Stackup

- **Layers:** 4-layer (JLC04161H-7628).
- **Finish:** ENIG.
- **Aesthetics:** dark green solder mask; typewriter font (all-caps German where applicable).
- **Placement:** one CPLD centred behind the 64-line terminal bank; J2 kept on the service edge for
  direct ribbon access.
- **Role Labelling (Silkscreen):** the PCB must identify the allowed service roles:
  `ENCODER MODULE`, `ENCODE USE`, and `DECODE USE`.

---

## 10. Bill of Materials

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C1-C8 | Decoupling (8 per CPLD) | 0.1µF X7R 50V | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 |
| C9-C13 | Bulk entry decoupling bank (star/spoke) | 10uF X7R 50V | 1206 | 187-CL31B106KBHNNNE | 1276-6767-1-ND | C89632 |
| BT1-BT64 | PCB spade blade terminals — one row × 64 | Keystone 1285-ST — 6.35 mm (1/4") straight vertical PCB-mount male blade tab. Used as either 64 driven outputs (decode role) or 64 sensed inputs (encode role). | Through-hole vertical | 534-1285-ST | 36-1285-ST-ND | C5370868 |
| J1 (x64 per plugboard pass) | Stecker jack sockets | 6.35 mm (1/4") mono switched panel-mount jack — off-board mechanical part used only by plugboard assemblies | Panel-mount | — (eBay: SaiBuy.Ltd item 334364197440, £1.66/unit) | — | — |
| D1 | Status LED (active-low) | Green SMD LED, **V_f = 2.0V @ 10mA (≈1.9V @ 4mA)** | 0402 | 710-150060VS75000 | 732-4980-1-ND | C6848499 |
| J2 | Data Link Connector | Adam Tech BHR-20-VUA / 2BHR-20-VUA — 20-pin 2×10 2.54mm shrouded box header | 2.54mm | 737-BHR-20-VUA | 2057-BHR-20-VUA-ND | C17340054 |
| SW1-SW40 | Keyboard switches | uxcell-style DPDT 6-pin momentary push button — assembly-level part used only by the Keyboard Assembly | Panel-mount | — (eBay: gadgetskingdom item 365271584375, 2 per pack) | — | — |
| U1 | Intel MAX II CPLD | EPM240T100I5N | TQFP-100 | 989-EPM240T100I5N | 544-2276-ND | C40067 |
| R1 | LED current limiting resistor | 330Ω 1% | 0402 | 667-ERJ-2RKF3300X | P330LCT-ND | C278592 |
| R2 | TMS pull-up to 3V3_ENIG | 10kΩ 1% | 0402 | 667-ERJ-2RKF1002X | P10.0KLCT-ND | C191123 |
| R3 | TDI pull-up to 3V3_ENIG | 10kΩ 1% | 0402 | 667-ERJ-2RKF1002X | P10.0KLCT-ND | C191123 |
| R4 | TCK pull-down to GND | 10kΩ 1% | 0402 | 667-ERJ-2RKF1002X | P10.0KLCT-ND | C191123 |
| R5 | SYS_RESET_N pull-up to 3V3_ENIG | 10kΩ 1% | 0402 | 667-ERJ-2RKF1002X | P10.0KLCT-ND | C191123 |
| R6 | TDO output series R (U1 TDO -> J2 pin 13, ribbon cable drive) | 75Ω 1% | 0402 | 667-ERJ-2RKF75R0X | P75.0LCT-ND | C413061 |
| R7-R70 (encode-role only) | Input pull-up resistors — 64× total, one per BT1-BT64 input line | 10kΩ 1% | 0402 | 667-ERJ-2RKF1002X | P10.0KLCT-ND | C191123 |
| C14-C77 (encode-role only) | Input RC noise filter caps — 64× total, paired 1:1 with R7-R70 | 100nF 50V X7R | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 |

**Quantity notes:**

- **Common fitted PCB population:** C1-C13, BT1-BT64, D1, J2, U1, and R1-R6 are fitted on every
  Encoder Module (**6 boards total**).
- **Encode-role-only population:** R7-R70 and C14-C77 are fitted on `KBD_ENC`, `PLG_PASS1_ENC`, and
  `PLG_PASS2_ENC` only (**3 boards total = 192 resistors + 192 capacitors system-wide**).
- **Assembly-level off-board parts:** J1 plugboard jacks are **64 per plugboard pass (128 system
  total)**. SW1-SW40 keyboard switches are **40 per Keyboard Assembly (40 system total)**.
