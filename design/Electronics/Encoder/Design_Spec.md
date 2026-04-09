# Encoder Module (V1.0) Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-05

## 1. Overview

A multi-purpose Human Interface Device (HID) and plugboard interface board. Each board consists of
**two completely independent halves** on the same PCB — a **Decode Half** (CPLD A: receives a 6-bit
character code and asserts one of 64 output lines) and an **Encode Half** (CPLD B: reads one of 64
input lines and produces a 6-bit character code). The two halves share no PCB copper other than the
single J2 IDC header, which carries power, both 6-bit data buses, and the JTAG chain.

### Plugboard Use (2 boards required)

When used as a plugboard, two Encoder boards are required — one per pass through the substitution
network. Each board provides one full pass: CPLD A decodes the incoming 6-bit character to one of 64
lines; those lines connect via wiring harness to 64 panel-mount jack sockets; a crossover cable between
any two jacks routes the signal to a different character's Sleeve terminal; CPLD B encodes the resulting
line back to a 6-bit output.

With no cable in a jack, the socket's normally-closed (N/C) switch contact shorts the Switch terminal
to the Sleeve terminal, passing the signal through unsubstituted (identity mapping). Up to 32 crossover
cables may be installed simultaneously (64 jacks ÷ 2 per cable).

The Stator CPLD routes the 6-bit data bus between the rotor stack and the encoder ports (J4/J5/J6),
enabling plugboard passes to be placed at any configurable point in the encryption signal chain:

| Historical Reference | Pass 1 position | Pass 2 position |
| :--- | :--- | :--- |
| Original Enigma (pre-war) | After Keyboard / before Rotor 1 | After last Rotor / before Lightboard |
| Later Enigma models | At Reflector | — (single pass only) |
| Enigma-NG (configurable) | Any position via Stator CPLD | Any position via Stator CPLD |

See `design/Electronics/Stator/Design_Spec.md §3` for the Stator CPLD routing details and J4/J5/J6
port assignments.

### HID Use (1 board, both halves independent)

When used as the HID interface (Keyboard + Lightboard), both halves operate independently:

- **Decode Half (CPLD A):** Receives 6-bit ENC_IN from Stator → asserts one of 64 lamp-drive output
  lines (Lightboard). Connected to lamp assemblies via BT1–64 spade terminals.
- **Encode Half (CPLD B):** Reads one of 64 key-press input lines (Keyboard) → encodes to 6-bit
  ENC_OUT to Stator. Connected to keyboard switches via BT65–128 spade terminals.

Regardless of use case (plugboard or HID), the physical PCB is identical — the functional role of
each half is determined entirely by the mechanical assembly and Stator CPLD configuration.

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
| DR-ENC-01 | PCB stackup | 4-layer, 2oz finished copper (JLC04161H-7628) | §9 PCB Fabrication & Stackup |
| DR-ENC-02 | CPLD | Intel MAX II EPM240T100I5N (TQFP-100) | §3 Dual-Role Architecture; BOM U1, U2 (EPM240T100I5N) |
| DR-ENC-03 | Stator interface connector | 26-pin Molex IDC (mates with Stator J4, J5, or J6) | §4 Interconnects; BOM J2 (26-pin 2×13 shrouded) |
| ~~DR-ENC-04~~ | ~~Moved to Mechanical/Plugboard/Design_Spec.md~~ | ~~—~~ | ~~—~~ |
| DR-ENC-05 | Supply voltage | 3.3V via the 3V3_ENIG power rail | §2 Power Requirements; BOM J2 (Data Link) |

## 2. Power Requirements

- **Core:** The Encoder Board receives its 3V3_ENIG power rail from the IDC cable connection from the Stator (pin 1 & 26). This could be connected to any of J4–J6 of the Stator Board.
- Decoupling and bulk entry capacitor requirements per `design/Standards/Global_Routing_Spec.md §3`.

## 3. Dual-Role Architecture

The board's two halves are electrically independent on the PCB. Each half contains one Intel MAX II
EPM240T100I5N CPLD and one bank of 64 spade terminals. The J2 IDC header is the only physical
connection between them (power, data buses, JTAG).

### Half Definitions

| Half | CPLD | Spade bank | 6-bit bus | Function |
| :--- | :--- | :--- | :--- | :--- |
| **Decode Half** | U1 (CPLD A) | BT1–64 | ENC_IN[0:5] ← Stator | Decodes 6-bit input → asserts 1 of 64 output lines |
| **Encode Half** | U2 (CPLD B) | BT65–128 | ENC_OUT[0:5] → Stator | Reads 1 of 64 input lines → encodes to 6-bit output |

### Signal Flow — Plugboard Mode

```text
ENC_IN[0:5] (from Stator J4/J5/J6, via J2 pin 2–7)
       ↓
  CPLD A (U1) — Decode: 6-bit → 1-of-64 lines asserted HIGH
       ↓ ↓ ↓ ↓ ↓ ↓ ... × 64 lines (BT1–64 → jack Tip+Switch via harness)
  [ 64 panel-mount jack sockets ]
  — No cable: N/C Switch→Sleeve shorts line straight through (identity) —
  — Cable A↔B: crossover cable routes line A to Sleeve B and vice versa —
       ↓ ↓ ↓ ↓ ↓ ↓ ... × 64 lines (jack Sleeve via harness → BT65–128)
  CPLD B (U2) — Encode: 1-of-64 lines → 6-bit output
       ↓
  ENC_OUT[0:5] (to Stator J4/J5/J6, via J2 pin 19–24)
```

### Signal Flow — HID Mode

```text
Decode Half (Lightboard):          Encode Half (Keyboard):
ENC_IN[0:5] ← Stator               64 key-press lines ← Keyboard switches
       ↓                                    ↓
  CPLD A (U1)                        CPLD B (U2)
       ↓                                    ↓
64 lamp-drive lines → BT1–64       BT65–128 ← key signals
       ↓                                    ↓
  Lightboard lamps                   ENC_OUT[0:5] → Stator
```

### I/O Capacity

Each CPLD provides 80 user I/O pins (TQFP-100). 64 pins are used for the spade terminal bank,
leaving headroom for JTAG, status LEDs, power, and any future expansion.

## 4. Interconnects

- **Data Link (J2):** 26-pin (2×13) 2.54mm shrouded box header with polarisation key.
  > **Connector Definition Owner:** `Stator/Board_Layout.md — J4–J6`.
  > See `design/Electronics/Stator/Board_Layout.md` — J4–J6 for the full pin table.
- **Status LEDs (×2):** One active-low debug LED per CPLD. CPLD output LOW = LED ON.
  330Ω current-limiting resistor per LED; ~4mA drive current at 3.3V.
- **Plugboard Jack Sockets:** See `design/Mechanical/Plugboard/Design_Spec.md`.
- **Keyboard Switches:** See `design/Mechanical/Keyboard/Design_Spec.md`.
- **PCB Spade Terminal Banks (2× banks of 64, 128 total):** 6.35mm (¼″) straight vertical PCB-mount male blade tabs.
  - **Bank 1 (BT1–BT64) — Decode Half outputs:** CPLD A (U1) decoder output lines. In plugboard mode:
    wired via harness to the Tip and Switch terminals of the 64 jack sockets. In HID lightboard mode:
    wired to lamp-drive lines. CPLD A drives these lines; no pull-up resistors required on this bank.
  - **Bank 2 (BT65–BT128) — Encode Half inputs:** CPLD B (U2) encoder input lines. In plugboard mode:
    wired via harness to the Sleeve terminals of the 64 jack sockets. In HID keyboard mode: wired to
    keyboard switch output lines (active-low, 10kΩ pull-up + RC filter per line).
  - The two banks are vertically stacked so that character N on Bank 1 (BT_N) aligns with character N
    on Bank 2 (BT_{N+64}), enabling correct plugboard harness assembly.
- **Jack Socket Wiring (Plugboard Mode):**
  Each of the 64 panel-mount jack sockets has three terminals. The wiring harness connects them as follows:

  | Jack terminal | Wired to | Notes |
  | :--- | :--- | :--- |
  | Tip | BT1–64 (Decode Half / CPLD A output) | Both Tip and Switch carry the same CPLD A signal |
  | Switch (N/C) | BT1–64 (same node as Tip) | N/C contact: shorts Switch→Sleeve when no plug present |
  | Sleeve | BT65–128 (Encode Half / CPLD B input) | CPLD B reads this line |

  **Identity mapping (no cable):** The jack's N/C contact shorts Switch to Sleeve, passing CPLD A's
  signal directly to CPLD B for the same character — no substitution occurs.

  **Substitution (crossover cable A↔B):** The cable is wired Tip-at-end-A → Sleeve-at-end-B. This
  routes CPLD A's character-A signal to CPLD B's character-B input (A→B), and simultaneously routes
  CPLD A's character-B signal to CPLD B's character-A input (B→A). Substitution is therefore
  **reciprocal and passive** — no CPLD logic is required for the routing itself.

  **Maximum 32 cables** may be installed simultaneously (64 jacks ÷ 2 jacks per cable).

  > **Note:** Physical harness assembly, jack panel layout, and cable construction are mechanical design
  > items. See `design/Mechanical/Plugboard/Design_Spec.md` for full harness specification.
  > Insertion detection (Switch contact opens when plug inserted) monitoring path is an **open item**
  > — to be defined in Mechanical/Plugboard/Design_Spec.md.
- **Diagnostic Probe Bank (J3):** 2×8 ENIG-finished bare PCB test pad array at 2.54mm pitch.
  Not a separate connector — bare gold pads probed directly with logic analyser clips or ICT fixtures.
  Mirrors the Data Link signals: Row 1 = 3V3_ENIG, GND, ENC_IN[0:5]; Row 2 = 3V3_ENIG, GND, ENC_OUT[0:5].
  See `Encoder/Board_Layout.md` Diagnostic Bank section for full pad map.
  Part number: N/A (PCB footprint only — no mating connector required).

## 5. JTAG Chain Integrity

- **Entry/Exit:** JTAG chain enters and exits via the IDC ribbon cable connection (J2) to the Stator Board.
- **Local Chain:** The Encoder Board contains 2 devices in its JTAG chain: CPLD 1 (U1) and CPLD 2 (U2). CPLD 1 TDO feeds CPLD 2 TDI.
- **Trace Width:** All JTAG signal traces on L1 shall be routed at **0.127 mm (5 mil)** over the L2 GND plane, targeting **50 Ω controlled impedance** per DEC-016. See `design/Electronics/Investigations/JTAG_Integrity.md`.
- **Pull Resistors (×4, placed near CPLDs):**
  - **TMS:** 10kΩ pull-up to 3V3_ENIG (R3) — ensures JTAG TAP resets to Test-Logic-Reset on power-up.
  - **TDI:** 10kΩ pull-up to 3V3_ENIG (R4) — holds TDI at logic-1 (BYPASS) when not driven.
  - **TCK:** 10kΩ pull-down to GND (R5) — prevents spurious clocking when TCK is floating.
  - **SYS_RESET_N:** 10kΩ pull-up to 3V3_ENIG (R6) — active-low; pull-up ensures CPLDs remain out of reset by default.
  - TCK, TMS, and SYS_RESET_N are broadcast nets shared between both CPLDs.
- **Termination:**
  - **Inter-CPLD (R7, 33Ω):** Series resistor placed within 2 mm of CPLD 1 TDO, on the trace to CPLD 2 TDI.
    Source impedance ≈ 53 Ω, matched to the 50 Ω intra-board PCB trace.
    See `design/Electronics/Investigations/JTAG_Integrity.md` Option D.
  - **Cable Output (R8, 75Ω):** Series resistor placed within 2 mm of CPLD 2 TDO, before J2 pin 13. Source impedance ≈ 95 Ω, targeting the ~100 Ω IDC ribbon cable impedance.
- **Programming:** Supports "In-System Sources and Probes" debugging via the CM5 GUI.

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

- **Thermal:** Vias under the Intel MAX II EPM240T100I5N CPLD "PowerPad" (if applicable) for heat dissipation.

## 9. PCB Fabrication & Stackup

- **Layers:** 4-Layer (JLC04161H-7628).
- **Finish:** ENIG (Gold) for TQFP-100 pads.
- **Aesthetics:** Dark Green Solder Mask; Typewriter font (ALL-CAPS GERMAN).
- **Chip Placement:** CPLD #1 (Left-side 32 keys) and CPLD #2 (Right-side 32 keys) placed on the rear of the board to allow keys/lamps/sockets on the front.
- **Half Labelling (Silkscreen):** The two board halves shall be clearly labelled in silkscreen:
  **"DECODE"** (U1 side, BT1–64) and **"ENCODE"** (U2 side, BT65–128). This prevents assembly
  errors, particularly since the board is physically symmetrical.

---

## 10. Bill of Materials

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C1-C16 | Decoupling (8 per CPLD, 2x CPLDs) | 0.1µF X7R 50V | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 |
| C17-C21 | Bulk entry decoupling bank (star/spoke) | 10uF X7R 50V | 1206 | 187-CL31B106KBHNNNE | 1276-6767-1-ND | C89632 |
| BT1–128 | PCB spade blade terminals — 2 rows × 64 (128 total) | Keystone 1285-ST — 6.35mm (¼″) straight vertical PCB-mount male blade tab. Row 1 (BT1–64): Decode Half — CPLD A decoder outputs; wired to jack Tip+Switch terminals (plugboard) or lamp-drive lines (HID). Row 2 (BT65–128): Encode Half — CPLD B encoder inputs; wired to jack Sleeve terminals (plugboard) or keyboard switch lines (HID). | Through-hole vertical | 534-1285-ST | 36-1285-ST-ND | C5370868 |
| J1 (×64) | Stecker jack sockets | 6.35mm (¼″) mono switched panel-mount jack — Tip+Switch → CPLD A Decode Half output (BT1–64 harness); Sleeve → CPLD B Encode Half input (BT65–128 harness); N/C contact (Switch→Sleeve) provides identity passthrough when no plug inserted. **Already purchased.** | Panel-mount | — (eBay: SaiBuy.Ltd item 334364197440, £1.66/unit) | — | — |
| D1, D2 | Status LED (one per CPLD, active-low) | Green SMD LED, **V_f = 2.0V @ 10mA (≈1.9V @ 4mA)** | 0402 | 710-150060VS75000 | 732-5015-1-ND | C2286 |
| J2 | Data Link Connector | 26-pin 2×13 shrouded box header, 2.54mm | 2.54mm | 538-22-23-2261 | WM2913-ND | N/A — Molex THT shrouded header, not stocked at JLCPCB; order from Mouser/DigiKey |
| J3 | Diagnostic probe pad bank (bare ENIG gold pads — logic analyser / ICT access) | 2×8 bare PCB pads | 2.54mm | N/A | N/A | N/A |
| SW1-64 | Keyboard Switches | DPDT 6-pin momentary push button — Pole 1: COM1+NO1 → key-press to CPLD; Pole 2: reserved (*Open item — lamp/redundancy function TBD*). **Already purchased.** | Panel-mount | — (eBay: gadgetkingdom, 2 per pack) | — | — |
| U1, U2 | Intel MAX II CPLD | EPM240T100I5N | TQFP-100 | 989-EPM240T100I5N | 544-2276-ND | C40067 |
| R1, R2 | LED current limiting resistors | 330Ω 1% | 0402 | 667-ERJ-2RKF3300X | P330LBCT-ND | C105872 |
| R3 | TMS pull-up to 3V3_ENIG | 10kΩ 1% | 0402 | 667-ERJ-2RKF1002X | P10.0KLBCT-ND | C25744 |
| R4 | TDI pull-up to 3V3_ENIG | 10kΩ 1% | 0402 | 667-ERJ-2RKF1002X | P10.0KLBCT-ND | C25744 |
| R5 | TCK pull-down to GND | 10kΩ 1% | 0402 | 667-ERJ-2RKF1002X | P10.0KLBCT-ND | C25744 |
| R6 | SYS_RESET_N pull-up to 3V3_ENIG | 10kΩ 1% | 0402 | 667-ERJ-2RKF1002X | P10.0KLBCT-ND | C25744 |
| R7 | Inter-CPLD series termination (CPLD1 TDO → CPLD2 TDI) | 33Ω 1% | 0402 | 667-ERJ-2RKF33R0X | P33.0LBCT-ND | C25808 |
| R8 | TDO output series R (CPLD2 TDO → J2 pin 13, ribbon cable drive) | 75Ω 1% | 0402 | 667-ERJ-2RKF75R0X | P75.0LCT-ND | C413061 |
| R9–R72 | CPLD B Encode Half input pull-up resistors — 64× total (one per BT65–BT128 input line). Pull-up to 3V3_ENIG; active-low logic; external 10kΩ dominates CPLD internal 50kΩ–100kΩ weak pull. Decode Half outputs (BT1–64) are CPLD A driven — no pull-ups required on that bank. | 10kΩ 1% | 0402 | 667-ERJ-2RKF1002X | P10.0KLBCT-ND | C25744 |
| C22–C85 | CPLD B Encode Half input RC noise filter caps — 64× total, paired 1:1 with R9–R72 (one cap to GND per Encode Half input line). RC τ = 1 ms; sufficient for noise immunity on harness; negligible for slow mechanical events. Decode Half outputs (BT1–64) are CPLD A driven — no RC filters required on that bank. | 100nF 50V X7R | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 |
