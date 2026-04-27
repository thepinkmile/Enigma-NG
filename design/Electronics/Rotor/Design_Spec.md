# Rotor Board (V1.0) Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-26

## 1. Overview

The Enigma-NG uses a 30-rotor stack. Unlike the original mechanical rotors, these are **Smart Digital Rotors**
where the internal scrambled wiring is emulated by a dedicated logic chip on each module.

Each rotor assembly consists of **two circular PCBs** (Board A and Board B), each **Ø92mm**,
inside an aluminium shroud (Ø100mm outer face, 4mm radial wall). The two boards are separated
by an ~11.8mm gap and connected by four single-row 2.54mm THT headers (H_SW3 1×7, H_PWR 1×5,
H_JTAG 1×5, H_SENS 1×5; 22 pins total; mixed gender for physical keying) on
their inner (facing) surfaces. Total rotor thickness is ~15mm, matching original Enigma rotor
proportions. These internal headers are manually assembled post-JLCPCB SMT pick-and-place.

**Board A (input side):** Carries the CPLD (U1), FDC2114 U2 (Track A encoder), SW1 (ring
setting), SW2 (forward map select), and J1–J3 (ERM8 male, input connectors).

**Board B (output side):** Carries FDC2114 U4 (Track B encoder, N=64 only), SW3 (return map
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
For N=26, all 5 STGC electrodes are on Board A only (U4 on Board B is not populated).

Two rotor variants are defined: the **26-character variant** (5-bit STGC, compatible with
original Enigma rotors I–VIII, Beta, Gamma) and the **64-character variant** (6-bit dual-track
Gray code, supporting the extended Enigma-NG character set). Both variants use identical PCB
footprints, connector pinouts, and DIP switch mechanisms for full interoperability within a
mixed stack. Variant-specific details are in
`design/Electronics/Rotor/Rotor_26_Char_Design.md` and
`design/Electronics/Rotor/Rotor_64_Char_Design.md`.

For mechanical dimensions, tolerances, shroud specification, and encoder slot geometry, see
`design/Mechanical/Rotor/Design_Spec.md`.

### GND_CHASSIS Single-Point Bond

Per `design/Standards/Global_Routing_Spec.md §5`, each rotor PCB implements a local
`GND_CHASSIS` net tied to its M2.5 alignment holes and any stationary mechanical chassis-contact
features, but it does **not** implement a local GND-to-GND_CHASSIS bond. The system's only
galvanic GND ↔ GND_CHASSIS bond remains on the Power Module at the common power-entry point
immediately before the eFuse. The rotating aluminium shroud remains electrically floating and must
not be used as a local chassis-bond point.

### Functional & Design Requirements

#### Functional Requirements

| ID | Functional Requirement | Notes | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| FR-ROT-01 | Emulate the substitution cipher wiring of a historical Enigma rotor in real-time | 21 forward maps in CPLD UFM; direction bit doubles to 42 configs; see variant design files | §2.2 Logic & Transposition; BOM U1 (EPM570T100I5N) |
| FR-ROT-02 | Detect rotor angular position using a capacitive encoder; N=64: dual-track 3+3 bit reflected Gray code (Board A and Board B); N=26: single-track 5-bit STGC (Board A only) | N=64: zero multi-bit transitions, XOR-chain decode; N=26: STGC lookup table, invalid codes flagged as fault | §2.1 Position Sensing; BOM U2/U3 (Board A), U4 (Board B, N=64 only) |
| FR-ROT-03 | Pass JTAG chain signals to the next rotor in the stack (or to the Reflector at position 30) | Serial daisy-chain; each rotor is one JTAG device | §3.3 Signal Integrity; BOM J1 (ERM8-005 JTAG in), J4 (ERF8-005 JTAG out) |
| FR-ROT-04 | Receive 3V3_ENIG power from the upstream board and forward to the downstream board | Passive power pass-through via J2/J5 | §3.1 Power Management; BOM J2 (ERM8-005 power in), J5 (ERF8-005 power out) |
| FR-ROT-05 | Apply cipher substitution at each rotor hop via CPLD; forward and return paths processed independently using SW2/SW3 selected maps | J3 ENC_IN → CPLD (SW2 map+dir) → J6 ENC_OUT; J6 ENC_IN → CPLD (SW3 map+dir) → J3 ENC_OUT; see §3.2 | §3.2 Communication Bus; BOM J3 (ERM8-010), J6 (ERF8-010) |
| FR-ROT-06 | Be individually removable for maintenance or reconfiguration without tools | Samtec ERM8/ERF8 high-cycle connectors | §2.3 Mechanical Details; BOM J1–J6 (Samtec ERM8/ERF8) |
| FR-ROT-07 | Store 21 forward cipher maps in CPLD UFM; SW2 (input side) and SW3 (output side) each independently select map index [4:0] and direction bit [5] (0=forward, 1=reverse), giving 42 effective configurations per side without reprogramming | Same mechanism and switch count for both variants | §2.2 Logic & Transposition; BOM U1 (EPM570T100I5N), SW2, SW3 |
| FR-ROT-08 | Implement ring setting via SW1 (6 switches, Board A input side only); CPLD sums SW1[5:0] with decoded position (mod N) to determine notch/turnover trigger position | Input side only; N=26 for 26-char variant, N=64 for 64-char variant | §2.3 Mechanical Details; BOM SW1; cross-ref: design/Mechanical/Rotor/Design_Spec.md |
| FR-ROT-09 | Expose effective rotor position (decoded position + SW1 ring offset, mod N) via Intel Virtual JTAG (ALTERA_VIRTUAL_JTAG megafunction, USER0 instruction) as a 6-bit UDR; readable by JDB FT232H without interrupting cipher operation | 26-char variant: bits [4:0] valid, bit [5]=0; 64-char: all 6 bits; cipher logic operates independently on CPLD system clock | §2.2 Logic & Transposition; §3.3 Signal Integrity; cross-ref: DEC-027, JDB Design_Spec |
| FR-ROT-10 | The rotor boards shall be assembled by JLCPCB SMT (one side each, outward-facing); the internal headers (H_SW3/H_PWR/H_JTAG/H_SENS) shall be manually assembled post-SMT | Mixed-gender header arrangement (H_SW3/H_SENS male on Board A, H_PWR/H_JTAG female on Board A; inverse on Board B) provides physical keying | §3.4 Connector Pinouts; BOM H_SW3/H_PWR/H_JTAG/H_SENS |

#### Design Requirements

| ID | Design Requirement | Specification | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| DR-ROT-01 | PCB stackup | 4-layer, 2oz finished copper (JLC04161H-7628) | §4 PCB Fabrication & Stackup |
| DR-ROT-02 | CPLD | Intel MAX II EPM570T100I5N (TQFP-100); 570 LEs; 21 UFM forward maps; SW2/SW3 direction bit gives 42 effective configs; character width in variant design files | §2.2 Logic & Transposition; BOM U1 (EPM570T100I5N) |
| DR-ROT-03 | Position sensor | Split dual-track capacitive encoder: FDC2114RGHR U2 on Board A (Track A, r≈44mm, bits[5:3] N=64 or STGC bits[3:0] N=26, addr 0x2A); FDC2114RGHR U3 on Board A (addr 0x2B, CH0 = STGC bit[4] — N=26 builds only; not populated for N=64); FDC2114RGHR U4 on Board B (Track B, r≈44mm, bits[2:0] N=64 only — not populated for N=26, addr 0x2B); PCB Ø=92mm; track patterns in variant design files | §2.1 Position Sensing; BOM U2/U3 (Board A), U4 (Board B, N=64 only) |
| DR-ROT-04 | Input connectors (Board A) | J1 = ERM8-005 (JTAG in), J2 = ERM8-005 (Power in), J3 = ERM8-010 (ENC in) | §3.4 Connector Pinouts; BOM J1–J3 |
| DR-ROT-05 | Output connectors (Board B) | J4 = ERF8-005 (JTAG out), J5 = ERF8-005 (Power out), J6 = ERF8-010 (ENC out) | §3.4 Connector Pinouts; BOM J4–J6 |
| DR-ROT-11 | Internal connectors (H_SW3/H_PWR/H_JTAG/H_SENS) | Four single-row 2.54mm THT headers on inner face of both boards (H_SW3: 1×7, H_PWR: 1×5, H_JTAG: 1×5, H_SENS: 1×5; total 22 pins); mixed gender between boards provides physical keying; manually assembled post-JLCPCB SMT | §3.4 Connector Pinouts; BOM H_SW3/H_PWR/H_JTAG/H_SENS |
| DR-ROT-06 | Power consumption | ≈54.2 mA typical per rotor from 3V3_ENIG (design budget: 55 mA) | §3.1 Power Management |
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

Each rotor variant populates **two Texas Instruments FDC2114RGHR** (4-channel
capacitive-to-digital converter, I²C, 3.3 V, 16-VQFN), but the second device differs by variant:

* **U2 (Board A)** — senses Track A (bits[5:3] for N=64; STGC bits[3:0] for N=26); I²C address 0x2A.
  Track A slots milled into the inner face of the shroud **dish** flange (Board A side).
* **U3 (Board A, N=26 only)** — second FDC2114 for the N=26 variant, addr 0x2B. CH0 = STGC bit[4]; CH1–CH3 unused
  (each carries a dummy LC tank — same 18 µH + 33 pF **in parallel** between INxA/INxB — per TI app note;
  GND-tie causes oscillation instability). **U3 is not populated for N=64**. N=26 variant: U2
  (addr 0x2A) reads STGC bits[3:0], U3 (addr 0x2B, Board A) reads STGC bit[4].
* **U4 (Board B, N=64 only)** — senses Track B (bits[2:0] for N=64 only); I²C address 0x2B.
  Track B slots milled into the inner face of the shroud **cover** flange (Board B side).
  **U4 is not populated for N=26 rotors.** Unused channels carry a dummy LC tank (18 µH + 33 pF
  **in parallel** between INxA/INxB) per TI app note; GND-tie causes oscillation instability.

The CPLD implements a simple I²C master and polls U2 and U3 (N=26) or U2 and U4 (N=64) at power-up and after
each detected position change. Each channel reports HIGH (solid aluminium) or LOW (milled slot).

The local FDC2114 bus requires one external pull-up on `SDA` and one on `SCL` to `3V3_ENIG`; these
are captured in the Board A BOM so the same pull-up pair serves the common local bus in both variants
(`U2` + `U3` on Board A for N=26, or `U2` on Board A plus `U4` over `H_SENS` for N=64). Per the
in-repo TI FDC2114 family datasheet power-supply recommendation, each populated FDC2114 also carries
its own local `0.1 µF` + `1 µF` `VDD` bypass pair. These support parts are separate from the still-
deferred resonant front-end / unused-channel support definition.

#### CPLD Position Decode

**N=64 (dual-track, 6-bit reflected Gray code):**
The 6 sensor readings (G[5:3] from U2 Track A, G[2:0] from U4 Track B) form a 6-bit standard
reflected Gray code. The CPLD decodes via XOR chain:

```text
B5 = G5 ; B4 = B5 XOR G4 ; B3 = B4 XOR G3
B2 = B3 XOR G2 ; B1 = B2 XOR G1 ; B0 = B1 XOR G0
```

No lookup table required. All 64 codes are valid. Zero multi-bit transitions at any position
including the 63→0 wrap. Full decode detail in `Rotor_64_Char_Design.md §7`.

**N=26 (single-track, 5-bit STGC):**
The 5 sensor readings (U2 STGC bits[3:0] and U3 STGC bit[4], both on Board A) form a 5-bit STGC code. A **combinational
lookup table** in the CPLD VHDL maps each valid code to its corresponding binary position
(0 to 25). Invalid codes flag a between-character fault. Standard Gray code is not achievable
for N=26 (not a power of 2); the lookup table is retained. Full decode detail in
`Rotor_26_Char_Design.md §7`.

The decoded binary position feeds directly into the SW1 modulo-N adder (§2.3).

Variant-specific track bit patterns and full decode tables are defined in:

* `design/Electronics/Rotor/Rotor_26_Char_Design.md` §7
* `design/Electronics/Rotor/Rotor_64_Char_Design.md` §7

#### Resonant Front-End Topology

Each active FDC2114 channel drives a resonant LC tank to detect the aluminium shroud segment. The
tank consists of an **18 µH shielded SMD inductor** and a **33 pF C0G/NP0 ±1% capacitor** connected
**in parallel** between the channel's INxA and INxB pins (single-ended mode; `CHx_FIN_SEL = 0b10`).
Nominal resonant frequency: **~6.5 MHz**.

* **Clock source:** CLKIN tied to GND — FDC2114 uses its internal oscillator (~43.35 MHz). No
  external crystal required.
* **IDRIVE baseline:** `0b01111` (register `DRIVE_CURRENT_CHx` = 0x7C00). Lab validation required;
  see `design/Procedures/Lab_Tests.md` **LT-001**.
* **Deglitch setting:** `0b101` = 10 MHz (register `MUX_CONFIG` deglitch field = 0x0005). Lab
  validation required; see `design/Procedures/Lab_Tests.md` **LT-002**.
* **Unused channels:** Each unused channel carries a **dummy LC tank** (same 18 µH + 33 pF in
  parallel between INxA/INxB). Tying unused INx pins directly to GND causes oscillation
  instability in active channels per TI application note; the dummy load is required.
* **FDC2114 firmware:** None. The FDC2114 has no user-programmable firmware. All register
  configuration is performed at runtime by the CPLD I²C master (VHDL bitstream). JTAG programs
  the CPLD only. Full I²C register table in `design/Software/CPLD_Logic/Rotor_Logic.md`.

Resonant front-end parts (`L1–L12`, `C20–C31`) are **Category B** pending part selection.

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

* **Input:** 3.3V/**~54.2mA typical per rotor** (design budget: **55mA/rotor**) sourced from the
  **Power Module** `3V3_ENIG` rail, routed through Controller Board → Stator Board → Rotor stack via
  the active Stator logic dock.
  See `design/Electronics/Power_Budgets.md` for full budget — 30 rotors draw **1.63A typical / 1.65A budget**; the 150mA/rotor figure previously used was a conservative overestimate.
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
  * All connectors carry 6 bits (ENC[5:0]) regardless of variant to maintain a common pinout
    across mixed stacks. The 26-character variant leaves ENC[5] as NC.
  * This path is entirely separate from the JTAG TTD\_RETURN signal.
* **JTAG TTD\_RETURN Path:** After the Reflector processes the cipher reversal, `TTD_RETURN` travels
  separately: Reflector J4 → Stator J10 → Controller-facing `J5` logic dock → FT232H on JDB (JTAG
  chain closure only).
* **Control:** Each rotor has a local I²C bus for position sensing (FDC2114 U2/U4 for N=64; U2/U3 for N=26). The CPLD acts as I²C master; no I²C signals are exposed on J1–J6.
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
* **TTD path policy:** The rotor-stack `TTD` path is a direct board-to-board chain. No series resistor is
  placed at each rotor hop; `TTD` exits the CPLD and continues straight to J4 pin 6. Cable-driving
  damping is reserved for the ribbon-port interfaces on the Stator / Encoder boards, while the
  Reflector retains the single 22 Ω end-of-chain damping resistor on `TTD_RETURN`.
* **Pull Resistors (R2–R5, 10kΩ, per CPLD):**
  * **TMS (R2):** 10kΩ pull-up to 3V3_ENIG — ensures JTAG TAP resets to Test-Logic-Reset on power-up.
  * **TDI (R3):** 10kΩ pull-up to 3V3_ENIG — holds TDI at logic-1 (BYPASS) when not actively driven.
  * **TCK (R4):** 10kΩ pull-down to GND — prevents spurious clocking when TCK is floating.
  * **SYS\_RESET\_N (R5):** 10kΩ pull-up to 3V3_ENIG — active-low; pull-up holds CPLD out of reset by default.
  These are present on every rotor board. With 30 rotors, 30 sets of pull resistors exist in the full stack;
  this is intentional and consistent with making each rotor independently safe in any stack position.
* **Shielding:** 4-layer PCB with solid GND plane (L2) to isolate digital switching from the high-accuracy capacitive encoder.

### 3.4 Connector Pinouts (Rotor Interface — Authority Document)
>
> This section is the **authoritative pinout definition** for all Rotor-to-Stator connectors.
> All other boards (Stator) cross-reference this section. See DEC-018 for ownership rationale.
>
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
>
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
>
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
>
#### J4 — JTAG Interface Output (ERF8-005, 10-pin 2×5, 0.8mm pitch, FEMALE socket)

Mates with the next rotor's J1 (ERM8-005 male header) or Reflector J1.

| Pin | Row A | Pin | Row B |
| :--- | :--- | :--- | :--- |
| 1 | GND | 2 | TCK |
| 3 | GND | 4 | TMS |
| 5 | GND | 6 | TTD |
| 7 | GND | 8 | SYS\_RESET\_N |
| 9 | GND | 10 | spare/GND |

> Pin 6 = TTD (CPLD TDO output — feeds next stage's J1 pin 6 TTD input). Pin 10 = spare/GND (no TTD_RETURN path here; return travels via Reflector → Extension Port → Stator J10).
>
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
>
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
>
#### J_INT — Board A ↔ Board B Internal Interconnect (4× single-row 2.54mm THT headers, 22 pins total)

Fitted on the **inner (facing) surface** of both Board A and Board B. Physical keying is achieved
by **mixed gender** — Board A carries H_SW3 and H_SENS as male (PH1-UA) and H_PWR and H_JTAG as
female (RS1-G); Board B carries the inverse. The unique 7-pin footprint of H_SW3 makes incorrect
board orientation geometrically impossible. All 4 headers are **manually soldered/assembled AFTER
JLCPCB SMT pick-and-place** and are NOT part of the JLCPCB SMT order.

Placement: equally spaced around the inner face at a radius halfway between the outer Samtec
connectors and the PCB edge, to maximise mechanical rigidity of the two-board assembly.

> **Assembly note:** Four connectors per rotor assembly (30 rotors × 4 = 120 total connectors
> across the full stack; 60 on Board A, 60 on Board B).
>
##### H_SW3 — Return Map Select (1×7, 7-pin)

Board A: **PH1-07-UA** (male) · Board B: **RS1-07-G** (female)

| Pin | Signal | Direction | Notes |
| :--- | :--- | :--- | :--- |
| 1 | SW3[0] | B→A | DIP SW3 bit 0 state |
| 2 | SW3[1] | B→A | DIP SW3 bit 1 state |
| 3 | SW3[2] | B→A | DIP SW3 bit 2 state |
| 4 | SW3[3] | B→A | DIP SW3 bit 3 state |
| 5 | SW3[4] | B→A | Map select bit 4 (Board B SW3 → Board A CPLD) |
| 6 | SW3[5] | B→A | Map direction bit (Board B SW3 → Board A CPLD) |
| 7 | GND | — | Ground reference |

> **SW3 bit coverage note:** All 6 SW3 DIP switch bits reach the CPLD on Board A via H_SW3:
> pins 1–4 carry SW3[3:0]; pins 5–6 carry SW3[4:5].
>
##### H_PWR — Power Distribution (1×5, 5-pin)

Board A: **RS1-05-G** (female) · Board B: **PH1-05-UA** (male)

| Pin | Signal | Direction | Notes |
| :--- | :--- | :--- | :--- |
| 1 | 3V3_ENIG | A→B | Power |
| 2 | 3V3_ENIG | A→B | Power |
| 3 | 3V3_ENIG | A→B | Power |
| 4 | 3V3_ENIG | A→B | Power |
| 5 | GND | — | Ground |

##### H_JTAG — JTAG Pass-Through (1×5, 5-pin)

Board A: **RS1-05-G** (female) · Board B: **PH1-05-UA** (male)

Compact internal transfer of the four JTAG/reset nets plus one shared ground between Board A and Board B.

| Pin | Signal | Direction | Notes |
| :--- | :--- | :--- | :--- |
| 1 | TCK | A→B | JTAG clock |
| 2 | GND | — | Shared signal return |
| 3 | TMS | A→B | JTAG mode select |
| 4 | SYS_RESET_N | A→B | Active-low reset forwarded to Board B and onward to J4 pin 8 |
| 5 | TTD | A→B | JTAG serial data (Board A J1 pin 6 input → Board B J4 pin 6 output path) |

##### H_SENS — Board B Sensor Interface (1×5, 5-pin)

Board A: **PH1-05-UA** (male) · Board B: **RS1-05-G** (female)

Carries the local I²C link used by the Board A CPLD to poll FDC2114 U4 on Board B. U4 measurement
results return over I²C; no dedicated POS_B parallel readback wires are required. The remaining pins
are reserved so the same 1×5 keyed header footprint can be retained across both rotor variants.

| Pin | Signal | Direction | Notes |
| :--- | :--- | :--- | :--- |
| 1 | SDA | A→B | I²C data (CPLD master → U4 FDC2114 on Board B) |
| 2 | SCL | A→B | I²C clock (CPLD master → U4 FDC2114 on Board B) |
| 3 | NC / Reserved | — | Reserved for future Board B sensor-side support; not used in the current design |
| 4 | NC / Reserved | — | Reserved for future Board B sensor-side support; not used in the current design |
| 5 | NC / Reserved | — | Reserved for future Board B sensor-side support; not used in the current design |

> **Variant note:** N=64 builds populate U4 on Board B and use only SDA/SCL on this header. N=26
> builds do not populate U4; pins 3–5 remain reserved/unused in both variants.
>
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
| C14 | U2 FDC2114 local `VDD` bypass (datasheet-recommended) | 0.1µF X7R 50V | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 |
| C15 | U2 FDC2114 local `VDD` reservoir (datasheet-recommended) | 1µF X7R MLCC, ≥6.3V — **user-selected MPN required** | TBD — owner-selected footprint | USER-SELECT REQUIRED | USER-SELECT REQUIRED | USER-SELECT REQUIRED |
| C16 | U3 FDC2114 local `VDD` bypass (datasheet-recommended; N=26 only, not populated for N=64) | 0.1µF X7R 50V | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 |
| C17 | U3 FDC2114 local `VDD` reservoir (datasheet-recommended; N=26 only, not populated for N=64) | 1µF X7R MLCC, ≥6.3V — **user-selected MPN required** | TBD — owner-selected footprint | USER-SELECT REQUIRED | USER-SELECT REQUIRED | USER-SELECT REQUIRED |
| J1 | JTAG Interface Connector (MALE header — mates with ERF8-005 female socket on Stator) | ERM8-005-05.0-S-DV-K-TR | 10-pin (2×5) 0.8mm pitch | 200-ERM8005050SDVKTR | 612-ERM8-005-05.0-S-DV-K-TRCT-ND | C3649741 |
| J2 | Power Interface Connector (MALE header — mates with ERF8-005 female socket on Stator) | ERM8-005-05.0-S-DV-K-TR | 10-pin (2×5) 0.8mm pitch | 200-ERM8005050SDVKTR | 612-ERM8-005-05.0-S-DV-K-TRCT-ND | C3649741 |
| J3 | Encoder Data Interface Connector (MALE header — mates with ERF8-010 female socket on Stator) | ERM8-010-05.0-S-DV-K-TR | 20-pin (2×10) 0.8mm pitch | 200-ERM8010050SDVKTR | SAM8610CT-ND | C374877 |
| H_SW3 | Board A↔B internal interconnect, inner face, return map select — **manually assembled post-JLCPCB SMT** | Adam Tech PH1-07-UA — 1×7 2.54mm male pin header | Through-hole | 737-PH1-07-UA | 2057-PH1-07-UA-ND | C3331618 |
| H_PWR | Board A↔B internal interconnect, inner face, power distribution — **manually assembled post-JLCPCB SMT** | Adam Tech RS1-05-G — 1×5 2.54mm female socket | Through-hole | 737-RS1-05-G | 2057-RS1-05-G-ND | C3321119 |
| H_JTAG | Board A↔B internal interconnect, inner face, JTAG pass-through — **manually assembled post-JLCPCB SMT** | Adam Tech RS1-05-G — 1×5 2.54mm female socket | Through-hole | 737-RS1-05-G | 2057-RS1-05-G-ND | C3321119 |
| H_SENS | Board A↔B internal interconnect, inner face, Board B sensor interface (I²C + reserved pins) — **manually assembled post-JLCPCB SMT** | Adam Tech PH1-05-UA — 1×5 2.54mm male pin header | Through-hole | 737-PH1-05-UA | 2057-PH1-05-UA-ND | C5374051 |
| R2 | TMS pull-up to 3V3_ENIG | 10kΩ 1% | 0402 | 667-ERJ-2RKF1002X | P10.0KLCT-ND | C191123 |
| R3 | TDI pull-up to 3V3_ENIG | 10kΩ 1% | 0402 | 667-ERJ-2RKF1002X | P10.0KLCT-ND | C191123 |
| R4 | TCK pull-down to GND | 10kΩ 1% | 0402 | 667-ERJ-2RKF1002X | P10.0KLCT-ND | C191123 |
| R5 | SYS_RESET_N pull-up to 3V3_ENIG | 10kΩ 1% | 0402 | 667-ERJ-2RKF1002X | P10.0KLCT-ND | C191123 |
| R6-R7 | Local FDC2114 I²C bus pull-ups (`SDA`, `SCL`) to `3V3_ENIG` | **Value TBD by owner** — external I²C pull-ups for the rotor-local `U2/U3/U4` sensor bus at 3.3V | TBD — owner-selected footprint | USER-SELECT REQUIRED | USER-SELECT REQUIRED | USER-SELECT REQUIRED |
| U1 | Intel MAX II CPLD (570 LEs; startup-loads UFM map into registers at power-up) | EPM570T100I5N | TQFP-100 | 989-EPM570T100I5N | 544-2281-ND | C27319 |
| U2 | FDC2114 capacitive sensor IC — Track A (bits[5:3] N=64; STGC bits[3:0] N=26); I²C addr 0x2A | FDC2114RGHR | 16-VQFN | 595-FDC2114RGHR ⚠️ MOQ 4500 at distributors | FDC2114RGHR-ND ⚠️ MOQ 4500 | C2652079 (MOQ 2) |
| U3 | FDC2114RGHR, 4-ch Capacitive Sensor IC, Board A, addr 0x2B, CH0 = STGC bit[4] (N=26 only), CH1–CH3 tied off. NOT POPULATED for N=64. | FDC2114RGHR | 16-VQFN | 595-FDC2114RGHR ⚠️ MOQ 4500 at distributors | FDC2114RGHR-ND ⚠️ MOQ 4500 | C2652079 (MOQ 2) |
| SW1 | Ring setting DIP switch (Board A input side only; SW1[5:0] summed with decoded position for notch/turnover) | CTS 219-6LPSTR — 6-position DIP switch, 2.54mm THT | Through-hole | 774-2196LPSTR | 119-219-6LPSTRCT-ND | C2842671 |
| SW2 | Forward-pass map selection (Board A input side; bits [4:0] = map index 0–20, bit [5] = direction 0/1) | CTS 219-6LPSTR — 6-position DIP switch, 2.54mm THT | Through-hole | 774-2196LPSTR | 119-219-6LPSTRCT-ND | C2842671 |

### Board B BOM (Output Side — JLCPCB SMT outward face)

| Ref | Component | Value | Package | Mouser Part # | DigiKey Part # | JLCPCB Part # |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| C18 | U4 FDC2114 local `VDD` bypass (datasheet-recommended; N=64 only, not populated for N=26) | 0.1µF X7R 50V | 0402 | 187-CL05B104KB5NNNC | 1276-1009-1-ND | C1525 |
| C19 | U4 FDC2114 local `VDD` reservoir (datasheet-recommended; N=64 only, not populated for N=26) | 1µF X7R MLCC, ≥6.3V — **user-selected MPN required** | TBD — owner-selected footprint | USER-SELECT REQUIRED | USER-SELECT REQUIRED | USER-SELECT REQUIRED |
| L1–L4 | U2 (Board A) FDC2114 CH0–CH3 resonant inductors — **one per active channel; in parallel with C20–C23 between INxA/INxB** | 18 µH shielded SMD — Cat B, part TBD | TBD (Cat B) | TBD (Cat B) | TBD (Cat B) | TBD (Cat B) |
| L5–L8 | U3 (Board A) FDC2114 CH0–CH3 resonant inductors — includes dummy LC for CH1–CH3 — **N=26 only, not populated for N=64** | 18 µH shielded SMD — same part as L1–L4 (Cat B) | TBD (Cat B) | TBD (Cat B) | TBD (Cat B) | TBD (Cat B) |
| L9–L12 | U4 (Board B) FDC2114 CH0–CH3 resonant inductors — includes dummy LC for CH1–CH3 — **N=64 only, not populated for N=26** | 18 µH shielded SMD — same part as L1–L4 (Cat B) | TBD (Cat B) | TBD (Cat B) | TBD (Cat B) | TBD (Cat B) |
| C20–C23 | U2 (Board A) FDC2114 CH0–CH3 resonant capacitors — **in parallel with L1–L4 between INxA/INxB** | 33 pF C0G/NP0 ±1% — Cat B, part TBD | TBD (Cat B) | TBD (Cat B) | TBD (Cat B) | TBD (Cat B) |
| C24–C27 | U3 (Board A) FDC2114 CH0–CH3 resonant capacitors — includes dummy LC for CH1–CH3 — **N=26 only, not populated for N=64** | 33 pF C0G/NP0 ±1% — same part as C20–C23 (Cat B) | TBD (Cat B) | TBD (Cat B) | TBD (Cat B) | TBD (Cat B) |
| C28–C31 | U4 (Board B) FDC2114 CH0–CH3 resonant capacitors — includes dummy LC for CH1–CH3 — **N=64 only, not populated for N=26** | 33 pF C0G/NP0 ±1% — same part as C20–C23 (Cat B) | TBD (Cat B) | TBD (Cat B) | TBD (Cat B) | TBD (Cat B) |
| J4 | JTAG Interface Output Connector (FEMALE socket — mates with ERM8-005 male header on next Rotor J1 or Reflector J1) | ERF8-005-05.0-S-DV-K-TR | 10-pin (2×5) 0.8mm pitch | 200-ERF8005050SDVKTR | SAM13517CT-ND | C7273978 |
| J5 | Power Interface Output Connector (FEMALE socket — mates with ERM8-005 male header on next Rotor J2 or Reflector J2) | ERF8-005-05.0-S-DV-K-TR | 10-pin (2×5) 0.8mm pitch | 200-ERF8005050SDVKTR | SAM13517CT-ND | C7273978 |
| J6 | Encoder Data Interface Output Connector (FEMALE socket — mates with ERM8-010 male header on next Rotor J3 or Reflector J3) | ERF8-010-05.0-S-DV-K-TR | 20-pin (2×10) 0.8mm pitch | 200-ERF8010050SDVKTR | SAM8618CT-ND | C3646170 |
| H_SW3 | Board A↔B internal interconnect, inner face, return map select — **manually assembled post-JLCPCB SMT** | Adam Tech RS1-07-G — 1×7 2.54mm female socket | Through-hole | 737-RS1-07-G | 2057-RS1-07-G-ND | C3321543 |
| H_PWR | Board A↔B internal interconnect, inner face, power distribution — **manually assembled post-JLCPCB SMT** | Adam Tech PH1-05-UA — 1×5 2.54mm male pin header | Through-hole | 737-PH1-05-UA | 2057-PH1-05-UA-ND | C5374051 |
| H_JTAG | Board A↔B internal interconnect, inner face, JTAG pass-through — **manually assembled post-JLCPCB SMT** | Adam Tech PH1-05-UA — 1×5 2.54mm male pin header | Through-hole | 737-PH1-05-UA | 2057-PH1-05-UA-ND | C5374051 |
| H_SENS | Board A↔B internal interconnect, inner face, Board B sensor interface (I²C + reserved pins) — **manually assembled post-JLCPCB SMT** | Adam Tech RS1-05-G — 1×5 2.54mm female socket | Through-hole | 737-RS1-05-G | 2057-RS1-05-G-ND | C3321119 |
| U4 | FDC2114 capacitive sensor IC — Track B (bits[2:0] N=64 only); I²C addr 0x2B — **Not populated for N=26 rotor** | FDC2114RGHR | 16-VQFN | 595-FDC2114RGHR ⚠️ MOQ 4500 at distributors | FDC2114RGHR-ND ⚠️ MOQ 4500 | C2652079 (MOQ 2) |
| SW3 | Return-pass map selection (Board B output side; bits [4:0] = map index 0–20, bit [5] = direction 0/1) | CTS 219-6LPSTR — 6-position DIP switch, 2.54mm THT | Through-hole | 774-2196LPSTR | 119-219-6LPSTRCT-ND | C2842671 |

> **Support-network scope note:** `R6/R7` and `C14-C19` capture the local I²C-bias and `VDD`-bypass
> requirements for the populated FDC2114 devices. Resonant front-end parts (`L1–L12`, `C20–C31`)
> are captured above as Category B pending part selection.
