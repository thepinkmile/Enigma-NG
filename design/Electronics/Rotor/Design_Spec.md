# Rotor Board (V1.0) Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-05

## 1. Overview

The Enigma-NG uses a 30-rotor stack. Unlike the original mechanical rotors, these are **Smart Digital Rotors**
where the internal scrambled wiring is emulated by a dedicated logic chip on each module.

Each rotor assembly consists of **two circular PCBs** (Board A and Board B), each **Ø92mm**,
inside an aluminium shroud (Ø100mm outer face, 4mm radial wall). The two boards are separated
by an ~11.8mm gap and connected by a keyed 2.54mm IDC box header (J_INT, 2×11, 22-pin) on
their inner (facing) surfaces. Total rotor thickness is ~15mm, matching original Enigma rotor
proportions. The IDC connector is manually assembled post-JLCPCB SMT pick-and-place.

**Board A (input side):** Carries the CPLD (U1), FDC2114 U2 (Track A encoder), SW1 (ring
setting), SW2 (forward map select), and J1–J3 (ERM8 male, input connectors).

**Board B (output side):** Carries FDC2114 U3 (Track B encoder, N=64 only), SW3 (return map
select), and J4–J6 (ERF8 female, output connectors).

The aluminium shroud is retained by **rolling-pin style cylindrical bearings** around the
circumference with **ceramic or nylon rolling elements** (electrically isolating). The shroud
must remain **electrically floating** — not connected to circuit ground. Gray code position
slots are milled into the inner faces of the shroud flanges (dish side for Track A, Board A;
cover side for Track B, Board B). Bare copper electrode pads on the PCB flat face at r≈44mm
sense the pattern capacitively. Characters are engraved on the outer cylindrical face of the
shroud at r=50mm.

The current position of the outer ring is detected using a **dual-track absolute capacitive
encoder** (N=64) or **single-track STGC encoder** (N=26). For N=64, 3+3 sensor electrodes on
Board A and Board B read a 6-bit standard reflected Gray code with zero multi-bit transitions.
For N=26, all 5 STGC electrodes are on Board A only (U3 on Board B is not populated).

Two rotor variants are defined: the **26-character variant** (5-bit STGC, compatible with
original Enigma rotors I–VIII, Beta, Gamma) and the **64-character variant** (6-bit dual-track
Gray code, supporting the extended Enigma-NG character set). Both variants use identical PCB
footprints, connector pinouts, and DIP switch mechanisms for full interoperability within a
mixed stack. Variant-specific details are in
`design/Electronics/Rotor/Rotor_26_Char_Design.md` and
`design/Electronics/Rotor/Rotor_64_Char_Design.md`.

For mechanical dimensions, tolerances, shroud specification, and encoder slot geometry, see
`design/Mechanical/Rotor/Design_Spec.md`.

### Functional & Design Requirements

#### Functional Requirements

| ID | Functional Requirement | Notes | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| FR-ROT-01 | Emulate the substitution cipher wiring of a historical Enigma rotor in real-time | 21 forward maps in CPLD UFM; direction bit doubles to 42 configs; see variant design files | §2.2 Logic & Transposition; BOM U1 (EPM570T100I5N) |
| FR-ROT-02 | Detect rotor angular position using a capacitive encoder; N=64: dual-track 3+3 bit reflected Gray code (Board A and Board B); N=26: single-track 5-bit STGC (Board A only) | N=64: zero multi-bit transitions, XOR-chain decode; N=26: STGC lookup table, invalid codes flagged as fault | §2.1 Position Sensing; BOM U2 (Board A), U3 (Board B, N=64 only) |
| FR-ROT-03 | Pass JTAG chain signals to the next rotor in the stack (or to the Reflector at position 30) | Serial daisy-chain; each rotor is one JTAG device | §3.3 Signal Integrity; BOM J1 (ERM8-005 JTAG in), J4 (ERF8-005 JTAG out) |
| FR-ROT-04 | Receive 3V3_ENIG power from the upstream board and forward to the downstream board | Passive power pass-through via J2/J5 | §3.1 Power Management; BOM J2 (ERM8-005 power in), J5 (ERF8-005 power out) |
| FR-ROT-05 | Apply cipher substitution at each rotor hop via CPLD; forward and return paths processed independently using SW2/SW3 selected maps | J3 ENC_IN → CPLD (SW2 map+dir) → J6 ENC_OUT; J6 ENC_IN → CPLD (SW3 map+dir) → J3 ENC_OUT; see §3.2 | §3.2 Communication Bus; BOM J3 (ERM8-010), J6 (ERF8-010) |
| FR-ROT-06 | Be individually removable for maintenance or reconfiguration without tools | Samtec ERM8/ERF8 high-cycle connectors | §2.3 Mechanical Details; BOM J1–J6 (Samtec ERM8/ERF8) |
| FR-ROT-07 | Store 21 forward cipher maps in CPLD UFM; SW2 (input side) and SW3 (output side) each independently select map index [4:0] and direction bit [5] (0=forward, 1=reverse), giving 42 effective configurations per side without reprogramming | Same mechanism and switch count for both variants | §2.2 Logic & Transposition; BOM U1 (EPM570T100I5N), SW2, SW3 |
| FR-ROT-08 | Implement ring setting via SW1 (6 switches, Board A input side only); CPLD sums SW1[5:0] with decoded position (mod N) to determine notch/turnover trigger position | Input side only; N=26 for 26-char variant, N=64 for 64-char variant | §2.3 Mechanical Details; BOM SW1; cross-ref: design/Mechanical/Rotor/Design_Spec.md |
| FR-ROT-09 | Expose effective rotor position (decoded position + SW1 ring offset, mod N) via Intel Virtual JTAG (ALTERA_VIRTUAL_JTAG megafunction, USER0 instruction) as a 6-bit UDR; readable by JDB FT232H without interrupting cipher operation | 26-char variant: bits [4:0] valid, bit [5]=0; 64-char: all 6 bits; cipher logic operates independently on CPLD system clock | §2.2 Logic & Transposition; §3.3 Signal Integrity; cross-ref: DEC-027, JDB Design_Spec |
| FR-ROT-10 | The rotor boards shall be assembled by JLCPCB SMT (one side each, outward-facing); the internal IDC connector (J_INT) shall be manually assembled post-SMT | Keyed IDC box header prevents incorrect orientation | §3.4 Connector Pinouts; BOM J_INT |

#### Design Requirements

| ID | Design Requirement | Specification | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| DR-ROT-01 | PCB stackup | 4-layer, 2oz finished copper (JLC04161H-7628) | §4 PCB Fabrication & Stackup |
| DR-ROT-02 | CPLD | Intel MAX II EPM570T100I5N (TQFP-100); 570 LEs; 21 UFM forward maps; SW2/SW3 direction bit gives 42 effective configs; character width in variant design files | §2.2 Logic & Transposition; BOM U1 (EPM570T100I5N) |
| DR-ROT-03 | Position sensor | Split dual-track capacitive encoder: FDC2114RGHR U2 on Board A (Track A, r≈44mm, bits[5:3] N=64 or STGC bits[3:0] N=26, addr 0x2A); FDC2114RGHR U3 on Board B (Track B, r≈44mm, bits[2:0] N=64 only — not populated for N=26, addr 0x2B); FDC2114RGHR U4 on Board A (addr 0x2B, CH0 = STGC bit[4] — N=26 builds only; not populated for N=64); PCB Ø=92mm; track patterns in variant design files | §2.1 Position Sensing; BOM U2 (Board A), U3 (Board B), U4 (Board A, N=26 only) |
| DR-ROT-04 | Input connectors (Board A) | J1 = ERM8-005 (JTAG in), J2 = ERM8-005 (Power in), J3 = ERM8-010 (ENC in) | §3.4 Connector Pinouts; BOM J1–J3 |
| DR-ROT-05 | Output connectors (Board B) | J4 = ERF8-005 (JTAG out), J5 = ERF8-005 (Power out), J6 = ERF8-010 (ENC out) | §3.4 Connector Pinouts; BOM J4–J6 |
| DR-ROT-11 | Internal connector (J_INT) | Keyed 2.54mm IDC box header, 2×11 (22-pin), on inner face of both boards; keyed to prevent incorrect orientation; manually assembled post-JLCPCB SMT | §3.4 Connector Pinouts; BOM J_INT |
| DR-ROT-06 | Power consumption | ≤50 mA per rotor from 3V3_ENIG | §3.1 Power Management |
| DR-ROT-07 | Stack quantity | 30 rotor boards in the complete system | §1 Overview |
| DR-ROT-08 | Mechanical retention | 2× M2.5 alignment holes; 8mm solid metal support rod (non-threaded) through all 30 rotors for alignment and connector stress relief; stack is horizontal | §2.3 Mechanical Details |
| DR-ROT-09 | Ring setting DIP switches (SW1) | 6-position DIP switch on input side only; SW1[5:0] summed mod N with CPLD STGC-decoded position to yield effective rotor position | §2.3 Mechanical Details; BOM SW1 |
| DR-ROT-10 | Map selection DIP switches (SW2 / SW3) | 6-position DIP on each face: bits [4:0] = map index (0–20 valid), bit [5] = direction (0=forward, 1=reverse); identical mechanism on both variants | §2.2 Logic & Transposition; BOM SW2, SW3 |

## 2. Core Design

### 2.1 Position Sensing (Dual-Track Capacitive Encoder)

The rotor outer ring position is detected contactlessly using a **dual-track absolute capacitive
encoder** (N=64) or **single-track STGC encoder** (N=26). All active components reside on the
rotor PCBs; the rotating aluminium shroud requires only milled slot patterns on its inner
flanges — no conductive ink, no magnets, and no mechanical contacts.

#### Physical Arrangement

* **PCB diameter:** 92 mm (45 mm radius).
* **Sensor electrodes:** Bare copper electrode pads on the PCB flat face (inner face of each
  board, facing the shroud flanges). No SMT components are placed on the electrode pads.
* **Electrode radius:** r ≈ 44 mm from board centre on both Board A and Board B.
* **Shroud slots:** Gray code patterns are milled as slots/pockets into the inner faces of the
  aluminium shroud flanges. Solid aluminium over an electrode = high capacitance (logic 1 from
  FDC2114); milled slot over an electrode = low capacitance (logic 0).
* **Gap:** 0.5mm ±0.15mm (0.35mm min – 0.65mm max) between PCB electrode and shroud flange inner face (controlled by bearing
  precision).
* **Shroud isolation:** The shroud must remain electrically **floating** (not connected to
  circuit ground). Rolling-pin cylindrical bearings with ceramic or nylon rolling elements
  provide the required electrical isolation.

#### Sensing ICs

Two **Texas Instruments FDC2114RGHR** (4-channel capacitive-to-digital converter, I²C, 3.3 V,
16-VQFN) per rotor:

* **U2 (Board A)** — senses Track A (bits[5:3] for N=64; STGC bits[3:0] for N=26); I²C address 0x2A.
  Track A slots milled into the inner face of the shroud **dish** flange (Board A side).
* **U3 (Board B)** — senses Track B (bits[2:0] for N=64 only); I²C address 0x2B.
  Track B slots milled into the inner face of the shroud **cover** flange (Board B side).
  **U3 is not populated for N=26 rotors.** Unused channels have their IN pins tied to GND
  via 100 kΩ.
* **U4 (Board A, N=26 only)** — FDC2114RGHR, addr 0x2B. CH0 = STGC bit[4]; CH1–CH3 unused
  (IN pins tied to GND via 100 kΩ). **U4 is not populated for N=64** (where addr 0x2B is used
  by U3 on Board B instead). N=26 variant: U2 (addr 0x2A) reads STGC bits[3:0], U4 (addr 0x2B,
  Board A) reads STGC bit[4].

The CPLD implements a simple I²C master and polls U2 and U4 (N=26) or U2 and U3 (N=64) at power-up and after
each detected position change. Each channel reports HIGH (solid aluminium) or LOW (milled slot).

#### CPLD Position Decode

**N=64 (dual-track, 6-bit reflected Gray code):**
The 6 sensor readings (G[5:3] from U2 Track A, G[2:0] from U3 Track B) form a 6-bit standard
reflected Gray code. The CPLD decodes via XOR chain:

```text
B5 = G5 ; B4 = B5 XOR G4 ; B3 = B4 XOR G3
B2 = B3 XOR G2 ; B1 = B2 XOR G1 ; B0 = B1 XOR G0
```

No lookup table required. All 64 codes are valid. Zero multi-bit transitions at any position
including the 63→0 wrap. Full decode detail in `Rotor_64_Char_Design.md §7`.

**N=26 (single-track, 5-bit STGC):**
The 5 sensor readings (U2 STGC bits[3:0] and U4 STGC bit[4], both on Board A) form a 5-bit STGC code. A **combinational
lookup table** in the CPLD VHDL maps each valid code to its corresponding binary position
(0 to 25). Invalid codes flag a between-character fault. Standard Gray code is not achievable
for N=26 (not a power of 2); the lookup table is retained. Full decode detail in
`Rotor_26_Char_Design.md §7`.

The decoded binary position feeds directly into the SW1 modulo-N adder (§2.3).

Variant-specific track bit patterns and full decode tables are defined in:

* `design/Electronics/Rotor/Rotor_26_Char_Design.md` §7
* `design/Electronics/Rotor/Rotor_64_Char_Design.md` §7

### 2.2 Logic & Transposition

* **Logic:** The **Intel MAX II EPM570T100I5N CPLD** performs real-time cipher substitution for
  both the forward and return signal paths simultaneously.
* **Role:** Applies the active cipher map to incoming ENC\_IN data and outputs the substituted
  value as ENC\_OUT. The forward-pass and return-pass maps are selected independently by SW2 and
  SW3 respectively:
  * **Forward path:** J3 ENC\_IN[0:W-1] → CPLD applies SW2-selected map → J6 ENC\_OUT[0:W-1]
  * **Return path:** J6 ENC\_IN[0:W-1] → CPLD applies SW3-selected map → J3 ENC\_OUT[0:W-1]
  * W = 5 for 26-character variant; W = 6 for 64-character variant.
    Note: N denotes alphabet size (26 or 64) throughout this document; W denotes ENC bus active bit width.
* **Memory:** The CPLD UFM stores 21 forward-direction cipher maps in the common 64-entry × 6-bit format (384 bits per map, 21 maps × 384 = 8,064 bits, within the 8,192-bit UFM).
  Both rotor variants use this identical map count and selection mechanism; the actual map data
  is variant-specific. The EPM570T100I5N is required (570 LEs): a 64-character map needs
  384 flip-flops for the loaded register table plus ~80 LEs for combinational decode, totalling
  ~464 LEs — exceeding the EPM240's 240 LEs. Same TQFP-100 footprint; drop-in at PCB level.
* **Map selection (SW2 / SW3):** Each 6-position DIP switch encodes:
  * Bits [4:0] — map index, selecting one of the 21 stored forward maps (indices 0–20 valid;
    21–31 reserved).
  * Bit [5] — direction: `0` = apply map forward (map[input] = output);
    `1` = apply map in reverse (find input such that map[input] = output, i.e. inverse lookup).
  * This direction bit effectively doubles the usable configurations to **42 per side** without
    requiring additional UFM storage.
  * SW2 and SW3 are independent — in normal Enigma operation they are set to a matched
    forward/inverse pair (same index, opposite directions), but the hardware does not enforce this.
* **Latency:** At power-up the CPLD serially reads the selected map(s) from UFM into internal
  flip-flop registers (~40 µs per 384-bit map at the 10 MHz UFM clock — well under 1 ms total,
  invisible to the user). At runtime, cipher substitution is applied combinationally from the
  loaded registers; typical latency is **~20–50 ns per rotor hop**. The full 30-rotor round-trip
  completes in ~1.2–3 µs — far below any practical timing constraint.
* **Configuration:** SW2 and SW3 are read at power-up only. A power cycle is required after
  changing either switch. The CPLD is programmed once via JTAG; map selection at runtime uses
  SW2/SW3 exclusively. See `design/Electronics/Rotor/Rotor_26_Char_Design.md` and
  `design/Electronics/Rotor/Rotor_64_Char_Design.md` for map data definitions and character-set
  details.
* Decoupling and bulk entry capacitor requirements per `design/Standards/Global_Routing_Spec.md §3`.

### 2.3 Mechanical Details

* **Mounting:** Each rotor PCB has two **M2.5 alignment holes**.
* **Stack Orientation:** The rotor stack is oriented **horizontally** (matching original Enigma
  machine aesthetics). In this orientation, rotor weight does not bear on the ERM8/ERF8 connector
  engagement faces.
* **Support Rod:** An **8mm solid metal support rod (non-threaded)** passes through the centre of
  all 30 rotors. The rod provides mechanical alignment and relieves stress on the ERM8/ERF8
  connectors during assembly and handling. It is not a retention mechanism; individual rotors
  remain removable by sliding them off the rod.
* **Hot-Swappable:** The Samtec ERM8 Edge-Rate connectors are rated for high mating cycles,
  allowing individual rotors to be pulled for reconfiguration without tools.
* **Connector Configuration:** Each rotor carries **3 separate ERM8 connectors** (JTAG, Power,
  ENC\_DATA) mating into matching ERF8 female sockets on the next rotor (or Stator for Rotor 1,
  Reflector for Rotor 30). Physical separation of connector types provides keying — it is
  mechanically impossible to mismate a power connector into a JTAG socket.

#### Ring Setting DIP Switches (SW1 — Input Side Only)

Each rotor carries a **6-position DIP switch (SW1)** on the input face that sets the ring
setting (Ringstellung), emulating the ring and notch position of an original Enigma rotor.

* **Location:** Input side only. SW1 is not present on or accessible from the output face.
* **Function:** The CPLD continuously sums SW1[5:0] with the decoded capacitive encoder position
  reading, modulo N (N = 26 for 26-char variant; N = 64 for 64-char variant), to produce the
  **effective position**. When this matches the notch trigger value for the active map, the CPLD
  signals the next rotor in the stack to advance one position (turnover).
* **Cross-reference:** See `design/Mechanical/Rotor/Design_Spec.md` for the
  ring gear, notch wheel, and mechanical turnover engagement mechanism.

#### Map Selection DIP Switches (SW2 / SW3)

A **6-position DIP switch** is mounted on each face of the rotor PCB for cipher map selection:

* **SW2 (input face):** Selects the map and direction for the **forward-pass** (J3 → J6).
* **SW3 (output face):** Selects the map and direction for the **return-pass** (J6 → J3).
  Completely independent of SW2.
* **Bit encoding (both SW2 and SW3):**
  * Bits [4:0] — map index: selects one of the 21 UFM forward maps (indices 0–20 valid).
  * Bit [5] — direction: `0` = forward; `1` = reverse (CPLD computes inverse lookup on the fly).
* **Effective configurations:** 21 maps × 2 directions = **42 per side**.
* **Normal operation:** SW2 and SW3 are set to the same map index with opposite directions
  (one forward, one reverse), emulating the linked forward/return wiring of an original Enigma
  rotor. The hardware does not enforce this — non-matching maps are valid.
* Both rotor variants use the **identical** SW2/SW3 footprint and encoding.

## 3. Electrical Requirements

### 3.1 Power Management

* **Input:** 3.3V/**50mA per rotor** (sourced from the **Power Module** 3V3_ENIG rail, routed through Controller Board → Stator Board → Rotor stack via Link-Beta).
  See `design/Electronics/Power_Budgets.md` for full budget — 30 rotors draw 1.50A typical; the 150mA/rotor figure previously used was a conservative overestimate.
* **Filtering:** Local **10uF X7R** bulk entry bank on each rotor; upstream rail filtering uses the **Stator ferrite bead bank** to suppress stack switching noise.
* Decoupling and bulk entry capacitor requirements per `design/Standards/Global_Routing_Spec.md §3`.

### 3.2 Communication Bus

* **The ENC Data Path:** The cipher bus passes through every rotor in the stack (Stator → Rotor 1
  → … → Rotor 30 → Reflector forward; reverse for the return path). At **each rotor the CPLD
  applies the active cipher substitution** — data is NOT passed through transparently:
  * **Forward path:** J3 ENC\_IN[0:W-1] → CPLD applies SW2-selected map (direction per SW2[5])
    → J6 ENC\_OUT[0:W-1]
  * **Return path:** J6 ENC\_IN[0:W-1] → CPLD applies SW3-selected map (direction per SW3[5])
    → J3 ENC\_OUT[0:W-1]
  * W = 5 for 26-character variant; W = 6 for 64-character variant (N denotes alphabet size; W denotes ENC bus active bit width).
  * All connectors carry 6 bits (ENC[0:5]) regardless of variant to maintain a common pinout
    across mixed stacks. The 26-character variant leaves ENC[5] as NC.
  * This path is entirely separate from the JTAG TTD\_RETURN signal.
* **JTAG TTD\_RETURN Path:** After the Reflector processes the cipher reversal, TTD\_RETURN travels
  separately: Reflector J4 → Stator J7 → Link-Beta pin 26 → FT232H on JDB (JTAG chain closure only).
* **Control:** Each rotor has a local I²C bus for position sensing (FDC2114 U2/U3 for N=64; U2/U4 for N=26). The CPLD acts as I²C master; no I²C signals are exposed on J1–J6.
* **JTAG:** Pass-through lines allow the **USB Blaster** on the Controller Board to program the
  entire 30-rotor stack in one daisy-chain operation. Under normal operation JTAG is idle; cipher
  maps are selected via SW2/SW3 without reprogramming.

### 3.3 Signal Integrity

* **Impedance:** 50Ω single-ended traces for JTAG and data lines to prevent reflections.
* **Layer Stack (4-Layer DEC-017):**
  * **L1:** Signal (JTAG routing + data traces). JTAG traces run on L1 over L2 GND plane.
  * **L2:** GND plane (solid, contiguous) — provides reference for L1 controlled-impedance traces.
  * **L3:** 3V3_ENIG power plane — provides local decoupling reference.
  * **L4:** Signal (secondary routing + data plate silkscreen on bottom).
* **JTAG Trace Width Rule:** All JTAG signal traces on L1 shall be routed at **0.127 mm (5 mil)**
  width over the L2 GND plane, targeting **50 Ω controlled impedance** per the JLC04161H-7628
  stackup (h=0.087mm, t=0.035mm, Eᵣ=4.4). See `design/Electronics/Investigations/JTAG_Integrity.md §3.1`
  for the copper-weight note (2oz finished uses 1oz base copper t=0.035mm in the IPC-2141A formula) and DEC-016.
* **Series Termination — TDO Output (R1, 75Ω):** Placed within 2 mm of CPLD TDO pin, on the
  trace to J4 pin 6 (TTD output side). Source impedance ≈ 95 Ω, targeting the ~100 Ω inter-rotor segment on the
  Stator PCB. Consistent with Encoder R8 (DEC-016). One resistor per rotor board.
* **Pull Resistors (R2–R5, 10kΩ, per CPLD):**
  * **TMS (R2):** 10kΩ pull-up to 3V3_ENIG — ensures JTAG TAP resets to Test-Logic-Reset on power-up.
  * **TDI (R3):** 10kΩ pull-up to 3V3_ENIG — holds TDI at logic-1 (BYPASS) when not actively driven.
  * **TCK (R4):** 10kΩ pull-down to GND — prevents spurious clocking when TCK is floating.
  * **SYS\_RESET\_N (R5):** 10kΩ pull-up to 3V3_ENIG — active-low; pull-up holds CPLD out of reset by default.
  These are present on every rotor board. With 30 rotors, 30 sets of pull resistors exist in the full stack;
  this is intentional and consistent with making each rotor independently safe in any stack position.
* **Shielding:** 4-layer PCB with solid GND plane (L2) to isolate digital switching from the high-accuracy capacitive encoder.

### 3.4 Connector Pinouts (Rotor Interface — Authority Document)

> This section is the **authoritative pinout definition** for all Rotor-to-Stator connectors.
> All other boards (Stator) cross-reference this section. See DEC-018 for ownership rationale.

#### J1 — JTAG Interface (ERM8-005, 10-pin 2×5, 0.8mm pitch)

| Pin | Row A | Pin | Row B |
| :--- | :--- | :--- | :--- |
| 1 | GND | 2 | TCK |
| 3 | GND | 4 | TMS |
| 5 | GND | 6 | TTD |
| 7 | GND | 8 | SYS\_RESET\_N |
| 9 | GND | 10 | spare/GND |

> **TTD Net Name:** The JTAG serial chain data pin is designated **TTD** (JTAG Transmission Data) at pin 6
> on both input and output connectors. On J1 (input side), TTD carries incoming TDI; on J4 (output side),
> TTD carries outgoing TDO to the next rotor's TDI. This unified net name avoids the TDI/TDO direction
> confusion when viewing connector pinouts in isolation. Consistent with the T-prefix JTAG signal naming
> convention (TCK, TMS, TDI, TDO → TTD).

#### J2 — Power Interface (ERM8-005, 10-pin 2×5, 0.8mm pitch)

| Pin | Row A | Pin | Row B |
| :--- | :--- | :--- | :--- |
| 1 | 3V3\_ENIG | 2 | GND |
| 3 | 3V3\_ENIG | 4 | GND |
| 5 | 3V3\_ENIG | 6 | GND |
| 7 | 3V3\_ENIG | 8 | GND |
| 9 | 3V3\_ENIG | 10 | GND |

> 5 pins × 0.5 A/pin = **2.5 A capacity** — far exceeds the 50 mA/rotor requirement.
> 5 power + 5 GND ensures fully balanced current return paths.

#### J3 — Encoder Data Interface (ERM8-010, 20-pin 2×10, 0.8mm pitch)

| Pin | Row A | Pin | Row B |
| :--- | :--- | :--- | :--- |
| 1 | ENC\_IN\[0\] | 2 | ENC\_OUT\[0\] |
| 3 | ENC\_IN\[1\] | 4 | ENC\_OUT\[1\] |
| 5 | ENC\_IN\[2\] | 6 | ENC\_OUT\[2\] |
| 7 | ENC\_IN\[3\] | 8 | ENC\_OUT\[3\] |
| 9 | ENC\_IN\[4\] | 10 | ENC\_OUT\[4\] |
| 11 | ENC\_IN\[5\] | 12 | ENC\_OUT\[5\] |
| 13 | GND | 14 | GND |
| 15 | GND | 16 | GND |
| 17 | GND | 18 | GND |
| 19 | GND | 20 | GND |

> 12 signal pins + 8 GND fill pins. All spare pins assigned as GND for improved EMI shielding
> and signal return paths around the encoder data bus. Both ENC_IN and ENC_OUT on J3 are active simultaneously:
> ENC_IN receives forward-pass data from upstream; ENC_OUT carries the CPLD SW3-map return-pass result back upstream.
> The 26-character variant uses ENC[0:4] only; ENC[5] = NC on those boards.

#### J4 — JTAG Interface Output (ERF8-005, 10-pin 2×5, 0.8mm pitch, FEMALE socket)

Mates with the next rotor's J1 (ERM8-005 male header) or Reflector J1.

| Pin | Row A | Pin | Row B |
| :--- | :--- | :--- | :--- |
| 1 | GND | 2 | TCK |
| 3 | GND | 4 | TMS |
| 5 | GND | 6 | TTD |
| 7 | GND | 8 | SYS\_RESET\_N |
| 9 | GND | 10 | spare/GND |

> Pin 6 = TTD (CPLD TDO output — feeds next stage's J1 pin 6 TTD input). Pin 10 = spare/GND (no TTD_RETURN path here; return travels via Reflector → Extension Port → Stator J7).

#### J5 — Power Interface Output (ERF8-005, 10-pin 2×5, 0.8mm pitch, FEMALE socket)

Mates with the next rotor's J2 (ERM8-005 male header) or Reflector J2.

| Pin | Row A | Pin | Row B |
| :--- | :--- | :--- | :--- |
| 1 | 3V3\_ENIG | 2 | GND |
| 3 | 3V3\_ENIG | 4 | GND |
| 5 | 3V3\_ENIG | 6 | GND |
| 7 | 3V3\_ENIG | 8 | GND |
| 9 | 3V3\_ENIG | 10 | GND |

> Power pass-through from J2 input side. 3V3_ENIG and GND rails continue to the next rotor in the stack.

#### J6 — Encoder Data Interface Output (ERF8-010, 20-pin 2×10, 0.8mm pitch, FEMALE socket)

Mates with the next rotor's J3 (ERM8-010 male header) or Reflector J3.

| Pin | Row A | Pin | Row B |
| :--- | :--- | :--- | :--- |
| 1 | ENC\_IN\[0\] | 2 | ENC\_OUT\[0\] |
| 3 | ENC\_IN\[1\] | 4 | ENC\_OUT\[1\] |
| 5 | ENC\_IN\[2\] | 6 | ENC\_OUT\[2\] |
| 7 | ENC\_IN\[3\] | 8 | ENC\_OUT\[3\] |
| 9 | ENC\_IN\[4\] | 10 | ENC\_OUT\[4\] |
| 11 | ENC\_IN\[5\] | 12 | ENC\_OUT\[5\] |
| 13 | GND | 14 | GND |
| 15 | GND | 16 | GND |
| 17 | GND | 18 | GND |
| 19 | GND | 20 | GND |

> ENC_OUT carries the CPLD SW2-map forward-pass substitution result downstream; ENC_IN receives return-pass data from downstream for SW3-map processing.
> Both directions are applied by the CPLD — this is NOT a pass-through. The 26-character variant uses ENC[0:4] only; ENC[5] = NC on those boards.

#### J_INT — Board A ↔ Board B Internal Interconnect (2.54mm keyed IDC box header, 2×11, 22-pin)

Fitted on the **inner (facing) surface** of both Board A and Board B. Both boards carry a mating
keyed IDC box header. The connector is **keyed to prevent incorrect orientation assembly**.

> **Assembly note:** J_INT is manually soldered/assembled AFTER JLCPCB SMT pick-and-place. It is
> NOT part of the JLCPCB SMT order. Order separately (e.g. Würth 61201221721 or equivalent 2×11
> 2.54mm keyed IDC box header). Two connectors per rotor assembly (30 rotors × 2 = 60 total).

Signal allocation (22 pins, 2×11):

| Pin | Signal | Direction | Notes |
| :--- | :--- | :--- | :--- |
| 1 | 3V3_ENIG | A→B | Power |
| 2 | 3V3_ENIG | A→B | Power |
| 3 | 3V3_ENIG | A→B | Power |
| 4 | 3V3_ENIG | A→B | Power |
| 5 | GND | — | Ground |
| 6 | GND | — | Ground |
| 7 | GND | — | Ground |
| 8 | GND | — | Ground |
| 9 | TCK | A→B | JTAG clock (pass-through to U3 if used) |
| 10 | TMS | A→B | JTAG mode select |
| 11 | TDO | A→B | JTAG data out from CPLD (Board A) → J4 pin 6 (Board B) |
| 12 | ENC_B[2] | B→A | Track B bit 2 (N=64 only) |
| 13 | ENC_B[1] | B→A | Track B bit 1 (N=64 only) |
| 14 | ENC_B[0] | B→A | Track B bit 0 (N=64 only) |
| 15 | SW3[4] | B→A | Map select bit 4 (Board B SW3 → Board A CPLD) |
| 16 | SW3[5] | B→A | Map direction bit (Board B SW3 → Board A CPLD) |
| 17 | SDA | A→B | I²C data (for U3 FDC2114 on Board B) |
| 18 | SCL | A→B | I²C clock (for U3 FDC2114 on Board B) |
| 19 | SW3[0] | B→A | DIP SW3 bit 0 state |
| 20 | SW3[1] | B→A | DIP SW3 bit 1 state |
| 21 | SW3[2] | B→A | DIP SW3 bit 2 state |
| 22 | SW3[3] | B→A | DIP SW3 bit 3 state |

> **SW3 bit coverage note:** All 6 SW3 DIP switch bits reach the CPLD on Board A via J_INT:
> pins 19–22 carry SW3[0:3]; pins 15–16 carry SW3[4:5].

### 3.5 Prototype Bench-Testing Provision (Break-Off Coupons)

Each board panel includes **6 break-off PCB coupons** (one per ERx8 connector), attached by mousebite
perforations. Each coupon fans out the 0.8mm pitch Samtec pads to a standard **2.54mm pitch shrouded
IDC box header**, permitting standard ribbon cable assemblies to be used for bench testing before full
stack assembly. For final production the coupons are snapped off at the mousebite perforations.

| Coupon | Connector | IDC Header | Signal |
| :--- | :--- | :--- | :--- |
| 1 | J1 — ERM8-005 (10-pin male) | 2×5 IDC box header, 2.54mm | JTAG in |
| 2 | J2 — ERM8-005 (10-pin male) | 2×5 IDC box header, 2.54mm | Power in |
| 3 | J3 — ERM8-010 (20-pin male) | 2×10 IDC box header, 2.54mm | ENC Data in |
| 4 | J4 — ERF8-005 (10-pin female) | 2×5 IDC box header, 2.54mm | JTAG out |
| 5 | J5 — ERF8-005 (10-pin female) | 2×5 IDC box header, 2.54mm | Power out |
| 6 | J6 — ERF8-010 (20-pin female) | 2×10 IDC box header, 2.54mm | ENC Data out |

IDC part numbers and coupon PCB fanout geometry to be defined at schematic/layout phase.

## 4. PCB Fabrication & Stackup

* **Layers:** 4-Layer (JLC04161H-7628).
* **Finish:** ENIG (Gold) for the edge-rate connector pads.
* **Aesthetics:** Dark Green Solder Mask with Typewriter font labeling (e.g., "WALZE I").

---

## 5. Bill of Materials

### Board A BOM (Input Side — JLCPCB SMT outward face)

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C1-C8 | Decoupling (8 per CPLD) | 0.1µF X7R 50V | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 |
| C9-C13 | Bulk entry decoupling bank (star/spoke) | 10uF X7R 50V | 1206 | 187-CL31B106KBHNNNE | 1276-6767-1-ND | C89632 |
| J1 | JTAG Interface Connector (MALE header — mates with ERF8-005 female socket on Stator) | ERM8-005-05.0-S-DV-K-TR | 10-pin (2×5) 0.8mm pitch | 200-ERM8005050SDVKTR | 612-ERM8-005-05.0-S-DV-K-TRCT-ND | C3649741 |
| J2 | Power Interface Connector (MALE header — mates with ERF8-005 female socket on Stator) | ERM8-005-05.0-S-DV-K-TR | 10-pin (2×5) 0.8mm pitch | 200-ERM8005050SDVKTR | 612-ERM8-005-05.0-S-DV-K-TRCT-ND | C3649741 |
| J3 | Encoder Data Interface Connector (MALE header — mates with ERF8-010 female socket on Stator) | ERM8-010-05.0-S-DV-K-TR | 20-pin (2×10) 0.8mm pitch | 200-ERM8010050SDVKTR | SAM8610CT-ND | C374877 |
| J_INT | Board A↔Board B internal interconnect, keyed IDC box header, inner face — **manually assembled post-JLCPCB SMT** | 2.54mm pitch, 2×11 (22-pin) | TH | 710-61201221721 | TBD | N/A — hand assembly |
| R1 | JTAG TDO output series termination (CPLD TDO → J4 pin 6, TTD output) | 75Ω 1% | 0402 | 667-ERJ-2RKF75R0X | P75.0LCT-ND | C413061 |
| R2 | TMS pull-up to 3V3_ENIG | 10kΩ 1% | 0402 | 667-ERJ-2RKF1002X | P10.0KLBCT-ND | C25744 |
| R3 | TDI pull-up to 3V3_ENIG | 10kΩ 1% | 0402 | 667-ERJ-2RKF1002X | P10.0KLBCT-ND | C25744 |
| R4 | TCK pull-down to GND | 10kΩ 1% | 0402 | 667-ERJ-2RKF1002X | P10.0KLBCT-ND | C25744 |
| R5 | SYS_RESET_N pull-up to 3V3_ENIG | 10kΩ 1% | 0402 | 667-ERJ-2RKF1002X | P10.0KLBCT-ND | C25744 |
| U1 | Intel MAX II CPLD (570 LEs; startup-loads UFM map into registers at power-up) | EPM570T100I5N | TQFP-100 | 989-EPM570T100I5N | 544-2281-ND | C27319 |
| U2 | FDC2114 capacitive sensor IC — Track A (bits[5:3] N=64; STGC bits[3:0] N=26); I²C addr 0x2A | FDC2114RGHR | 16-VQFN | 595-FDC2114RGHR ⚠️ MOQ 4500 at distributors | FDC2114RGHR-ND ⚠️ MOQ 4500 | C2652079 (MOQ 2) |
| U4 | FDC2114RGHR, 4-ch Capacitive Sensor IC, Board A, addr 0x2B, CH0 = STGC bit[4] (N=26 only), CH1–CH3 tied off. NOT POPULATED for N=64. | FDC2114RGHR | 16-VQFN | 595-FDC2114RGHR ⚠️ MOQ 4500 at distributors | FDC2114RGHR-ND ⚠️ MOQ 4500 | C2652079 (MOQ 2) |
| SW1 | Ring setting DIP switch (Board A input side only; SW1[5:0] summed with decoded position for notch/turnover) | 6-position DIP | TBD | TBD | TBD | TBD |
| SW2 | Forward-pass map selection (Board A input side; bits [4:0] = map index 0–20, bit [5] = direction 0/1) | 6-position DIP | TBD | TBD | TBD | TBD |

### Board B BOM (Output Side — JLCPCB SMT outward face)

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| J4 | JTAG Interface Output Connector (FEMALE socket — mates with ERM8-005 male header on next Rotor J1 or Reflector J1) | ERF8-005-05.0-S-DV-K-TR | 10-pin (2×5) 0.8mm pitch | 200-ERF8005050SDVKTR | SAM13517CT-ND | C7273978 |
| J5 | Power Interface Output Connector (FEMALE socket — mates with ERM8-005 male header on next Rotor J2 or Reflector J2) | ERF8-005-05.0-S-DV-K-TR | 10-pin (2×5) 0.8mm pitch | 200-ERF8005050SDVKTR | SAM13517CT-ND | C7273978 |
| J6 | Encoder Data Interface Output Connector (FEMALE socket — mates with ERM8-010 male header on next Rotor J3 or Reflector J3) | ERF8-010-05.0-S-DV-K-TR | 20-pin (2×10) 0.8mm pitch | 200-ERF8010050SDVKTR | SAM8618CT-ND | C3646170 |
| J_INT | Board A↔Board B internal interconnect, keyed IDC box header, inner face — **manually assembled post-JLCPCB SMT** | 2.54mm pitch, 2×11 (22-pin) | TH | 710-61201221721 | TBD | N/A — hand assembly |
| U3 | FDC2114 capacitive sensor IC — Track B (bits[2:0] N=64 only); I²C addr 0x2B — **Not populated for N=26 rotor** | FDC2114RGHR | 16-VQFN | 595-FDC2114RGHR ⚠️ MOQ 4500 at distributors | FDC2114RGHR-ND ⚠️ MOQ 4500 | C2652079 (MOQ 2) |
| SW3 | Return-pass map selection (Board B output side; bits [4:0] = map index 0–20, bit [5] = direction 0/1) | 6-position DIP | TBD | TBD | TBD | TBD |
