# Cypher Board V1.0 Pinout Reference

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-10-08

> **Board_Layout.md is a visualisation-only document.** Design narrative, specifications, and
> component rationale belong in `Design_Spec.md`. This file contains connector pinout references
> and board orientation notes only.

---

## Orientation Convention

- **Front face:** faces the first Rotor Mini-Stack.
- **Back face:** carries ENC module mounts (J7–J18), the CTL dock connectors (J1/J2), and the
  spade blade terminal bank (J20+) along the **bottom edge** of this face (the HID/USM
  interconnect connectors, J5/J6, are at the top edge of the same face - general placement only,
  exact per-terminal arrangement TBD at layout - see DEC-088).
- **STA side:** the edge where J3 (Stack-Input / STA-side QSS-025 female) is mounted.
- **REF side:** the edge where J4 (Stack-Output / REF-side QSS-025 female) is mounted.

---

## 1. J1 / J2 — Controller Dock (Power-Only Molex / Signal-Only Samtec)

> **Connector Definition Owner:** `Controller/Board_Layout.md §2`/§3`.
> `J1` uses the plug (Molex 2195620015) mating with the CTL receptacle (Molex 2195630015).
> `J2` uses the right-angle male plug (Samtec QTS-025-01-L-D-RA-P) mating with the CTL vertical
> female receptacle (Samtec QSS-025-01-L-D-A-GP-K). See DEC-098.

### J1 — Power-Only Dock (Molex 2195620015)

Zero signal contacts.

| Contact type | Allocation | Notes |
| :--- | :--- | :--- |
| Power-pitch (5x, big pins) | `5 x GND` | `GND` mates first on the larger, more robust contacts |
| Signal-pitch (8x) | `8 x 5V_MAIN` | 4.5A/contact rating — 36A theoretical capacity |
| Signal-pitch (7x) | `7 x 3V3_ENIG` | 4.5A/contact rating — 31.5A theoretical capacity |

### J2 — Signal-Only Dock (Samtec QTS-025-01-L-D-RA-P)

Zero power rails. 50 contacts: 2 center-GND-bar (1/row) + 24 usable pins/row. Pin numbering:
column Cn, top pin = 2n-1, bottom pin = 2n. **Note:** the connector's internal ground wedge runs
the full connector length between the top (odd) and bottom (even) pin rows — top/bottom crosstalk
within a column is inherently shielded; the exposure to guard against is column-to-column
(same-row) adjacency, hence the `GND` separator columns below. Full pin map matches
`Controller/Board_Layout.md §3.2` exactly (this board carries the mating plug of the same net map).

| Top Row Signal | Top Pin# | Bottom Pin# | Bottom Row Signal |
| :--- | :---: | :---: | :--- |
| GND | 1 | 2 | GND |
| **PWM0[0]** | 3 | 4 | GND |
| GND | 5 | 6 | **PWM0[1]** |
| **PWM0[2]** | 7 | 8 | GND |
| GND | 9 | 10 | **PWM0[3]** |
| GND | 11 | 12 | GND |
| GND | 13 | 14 | GND |
| **GPCLK[0]** | 15 | 16 | **GPCLK[1]** |
| GND | 17 | 18 | GND |
| GND | 19 | 20 | GND |
| **USB_D_PLUS** | 21 | 22 | **USB_D_MINUS** |
| GND | 23 | 24 | GND |
| GND (bar) | 25 | 26 | GND (bar) |
| GND | 27 | 28 | GND |
| GND | 29 | 30 | GND |
| **I2C1_SDA** (Bank 1, Cypher peripherals — existing) | 31 | 32 | **I2C1_SCL** (Bank 1, existing) |
| GND | 33 | 34 | GND |
| **I2C2_SDA** (Bank 2, future — NC) | 35 | 36 | **I2C2_SCL** (Bank 2, future — NC) |
| GND | 37 | 38 | GND |
| **I2C3_SDA** (Bank 3, future — NC) | 39 | 40 | **I2C3_SCL** (Bank 3, future — NC) |
| GND | 41 | 42 | GND |
| **I2C4_SDA** (Bank 4, future — NC) | 43 | 44 | **I2C4_SCL** (Bank 4, future — NC) |
| GND | 45 | 46 | GND |
| **I2C6_SDA** (Bank 6, spare/HID-future — NC) | 47 | 48 | **I2C6_SCL** (Bank 6, spare/HID-future — NC) |
| GND | 49 | 50 | GND |

> **Note:** `I2C0` (PM-dedicated bus) is **not** present on this connector — it is routed
> exclusively via the Controller's `J3` to the Power Module. `I2C2`/`I2C3`/`I2C4`/`I2C6` are
> reserved for future expansion (see DEC-099) and are NC on this board; `PWM0[0-3]` and
> `GPCLK[0]`/`GPCLK[1]` are also reserved and are wired only to the bare test-pad loops
> (`TP1`-`TP6`, each paired with a `GND` test-pad loop `TP7`-`TP12`) defined below — see
> `Design_Spec.md DR-CYP-10`.

---

## 2. J3 — Stack-Input / STA-Side Stacking Connector (QSS-025-01-L-D-A-GP-K)

> **Connector Definition Owner:** `Stack-Input/Board_Layout.md §1` (per DEC-094 — the IC-STA-CHAIN
> template is reused identically at every Stack-Input front/rear junction along the chain).
> This board carries the female receptacle (QSS-025-01-L-D-A-GP-K); Stack-Input's front face
> carries the mating male QTS-025-01-L-D-RA-P.

**Fully 50-pin allocated** per DEC-090/DEC-093 — see `Stack-Input/Board_Layout.md §1` for the
full canonical pin map.

> **Cypher Board's own wiring at J3:** `ACTUATE_REQUEST_IN_N` (pin 16) → CPLD U1 input, driving
> first-rotor actuation per U1's programmed configuration (based on `ENC_ACTIVE_N` from
> Cypher-Input and U1's firmware, per DEC-091). `ACTUATE_REQUEST_OUT_N` (pin 35) → CPLD U1 input
> **and** R51 (10 kOhm pull-up to 3V3_ENIG, idle-bias) — this is the far-end return of the full
> round-trip signal path (DEC-093); U1 firmware compares it against the originally-issued
> `ACTUATE_REQUEST_IN_N` to verify the request successfully completed its round trip through the
> entire rotor stack, as a system self-test/diagnostic. The pull-up defines the idle/disconnected
> state (e.g. Stack-Blanking Board plugged directly into `J3`/`J4` for bench testing with no
> mini-stacks attached, where nothing actively drives this pin). See DEC-090, DEC-091, DEC-093,
> DEC-094, DEC-097.

---

## 3. J4 — Stack-Output / REF-Side Stacking Connector (QSS-025-01-L-D-A-GP-K)

> **Connector Definition Owner:** `Stack-Output/Board_Layout.md §1` (per DEC-094 — the
> IC-REF-CHAIN template is reused identically at every Stack-Output front/rear junction along the
> chain). This board carries the female receptacle (QSS-025-01-L-D-A-GP-K); Stack-Output's
> front face carries the mating male QTS-025-01-L-D-RA-P.

**Fully 50-pin allocated** per DEC-092/DEC-093 — see `Stack-Output/Board_Layout.md §1` for the
full canonical pin map.

> **Cypher Board's own wiring at J4:** `TTD_RETURN` (pin 30) mirrors `TTD`'s position on `J3`
> (pin 30) — routed via R50 (22 Ohm) to FT232H U17 TDO, per §4 Signal Turnaround. `3V3_ENIG`
> (8 pins total, matching `J3`'s power pin count on this single-rail connector) feeds the
> Stack-Output Board, which requires no `5V_MAIN` (per `Stack-Output/Design_Spec.md DR-SOUT-07`).
> `ACTUATE_REQUEST_REF_IN_N`/`ACTUATE_REQUEST_REF_OUT_N` are logically distinct nets from `J3`'s
> `ACTUATE_REQUEST_IN_N`/`ACTUATE_REQUEST_OUT_N` (same pin positions, per the board-agnostic
> template, but different roles — matching the existing `ENC_IN_REF`/`ENC_OUT_REF` vs
> `ENC_IN_ROT`/`ENC_OUT_ROT` naming precedent). `ACTUATE_REQUEST_REF_IN_N` (pin 16) → CPLD U1
> input; based on U1's firmware configuration, U1 drives `ACTUATE_REQUEST_REF_OUT_N` (pin 35) in
> response. See DEC-093 for the full end-to-end `ACTUATE_REQUEST` signal path.

---

## 4. J5 — Cypher Left Pair Template (Cypher-Input / Cypher-Output HID Interconnect)

> **Connector Definition Owner:** this board.
> Mates with whichever HID board's top (right-angle male, QTS-025-01-L-D-RA-P) connector is
> physically closest - the other HID board attaches further down the local stack via that
> board's own bottom connector, not directly to this board. Mating gap/tolerance:
> `design/Standards/Global_Routing_Spec.md §4.1a`.

- **MPN:** QSS-025-01-L-D-A-GP-K (Samtec 50-contact 0.635mm vertical female SMT)
- Carries `3V3_ENIG`/`5V_MAIN`/GND, `ENC_DATA_IN[5:0]`/`ENC_DATA_OUT[5:0]`,
  `ENC_ACTIVE_INPUT_N`/`ENC_ACTIVE_OUTPUT_N`, and `BOARD_ROLE_ID_IN[3:0]`/`BOARD_ROLE_ID_OUT[3:0]`.
  The physical plugboard patch-jack
  harness does **not** route through this connector either - it wires directly to this board's
  own spade terminal bank (`J20+`) instead, per DEC-088.

### J5 — Full Pin Map (Cypher Left Pair Template)

50 contacts: 2 center-GND-bar (1/row) + 24 usable pins/row. Pin numbering: column Cn, top pin =
2n-1, bottom pin = 2n. This is a **board-agnostic template** — how each specific board
(Cypher-Input, Cypher-Output) wires a given pin internally is defined in that board's own
`Design_Spec.md`.

| Top Row Signal | Top Row Pin# | Bottom Row Pin# | Bottom Row Signal |
| :--- | :---: | :---: | :--- |
| **3V3_ENIG** | 1 | 2 | **3V3_ENIG** |
| **5V_MAIN** | 3 | 4 | **5V_MAIN** |
| GND | 5 | 6 | GND |
| GND | 7 | 8 | **ENC_DATA_OUT[0]** |
| GND | 9 | 10 | **ENC_DATA_OUT[1]** |
| GND | 11 | 12 | **ENC_DATA_OUT[2]** |
| GND | 13 | 14 | **ENC_DATA_OUT[3]** |
| GND | 15 | 16 | **ENC_DATA_OUT[4]** |
| **BOARD_ROLE_ID_IN[0]** | 17 | 18 | **ENC_DATA_OUT[5]** |
| **BOARD_ROLE_ID_IN[1]** | 19 | 20 | **ENC_ACTIVE_OUTPUT_N** |
| **BOARD_ROLE_ID_IN[2]** | 21 | 22 | GND |
| **BOARD_ROLE_ID_IN[3]** | 23 | 24 | GND |
| GND (bar) | 25 | 26 | GND (bar) |
| GND | 27 | 28 | **BOARD_ROLE_ID_OUT[3]** |
| GND | 29 | 30 | **BOARD_ROLE_ID_OUT[2]** |
| **ENC_ACTIVE_INPUT_N** | 31 | 32 | **BOARD_ROLE_ID_OUT[1]** |
| **ENC_DATA_IN[5]** | 33 | 34 | **BOARD_ROLE_ID_OUT[0]** |
| **ENC_DATA_IN[4]** | 35 | 36 | GND |
| **ENC_DATA_IN[3]** | 37 | 38 | GND |
| **ENC_DATA_IN[2]** | 39 | 40 | GND |
| **ENC_DATA_IN[1]** | 41 | 42 | GND |
| **ENC_DATA_IN[0]** | 43 | 44 | GND |
| GND | 45 | 46 | GND |
| **5V_MAIN** | 47 | 48 | **5V_MAIN** |
| **3V3_ENIG** | 49 | 50 | **3V3_ENIG** |

> **Rotational (180°) symmetry:** this pin map is a point-symmetric pattern about the center GND
> bar (column 13, pins 25/26) - rotating the connector 180° maps every populated pin onto its
> counterpart at the mirrored column/row (column *n* maps to column 26-*n*, row flips). `3V3_ENIG`
> (column 1, both rows) opposes itself at column 25 (both rows); `5V_MAIN` (column 2, both rows)
> opposes itself at column 24 (both rows) - each rail is trivially symmetric, occupying a full
> mirrored column pair on its own. Columns 9/17 and 10/16 each pack two independent signal pairs
> onto the same column pair (one `ENC_DATA_IN`/`ENC_DATA_OUT` bit plus one `BOARD_ROLE_ID_IN`/
> `BOARD_ROLE_ID_OUT` bit, or one `BOARD_ROLE_ID_IN`/`BOARD_ROLE_ID_OUT` bit plus
> `ENC_ACTIVE_INPUT_N`/`ENC_ACTIVE_OUTPUT_N`), since no GND filler is needed once both cells of a
> mirrored pair carry real signals. Every other populated column carries one `_IN`/`_OUT` signal
> on one row with GND as its silent-partner row; its mirrored column carries the paired signal
> (same bit index, `_IN`↔`_OUT`) on the opposite row, with GND again filling the complementary
> slot - e.g. `ENC_DATA_OUT[0]` (column 4, bottom) diagonally opposes `ENC_DATA_IN[0]` (column 22,
> top); `BOARD_ROLE_ID_IN[2]` (column 11, top) diagonally opposes `BOARD_ROLE_ID_OUT[2]`
> (column 15, bottom).
>
> **Power/GND pin budget:** `3V3_ENIG` and `5V_MAIN` each occupy 4 pins (one full mirrored column
> pair per rail).
>
> **`ENC_DATA_IN[5:0]`/`ENC_DATA_OUT[5:0]` (columns 4-9, 17-22):** top row (columns 17-22) =
> `KBD_ENC` keyboard encode data, generated by Cypher-Input, relayed through whichever HID board
> is closest if that is Cypher-Output; bottom row (columns 4-9) = `LBD_DEC` lightboard decode
> data, generated by this board's own CPLD (U1) and relayed onward to Cypher-Output. See
> `Design_Spec.md §3` CPLD Signal Routing Matrix.
>
> **`ENC_ACTIVE_INPUT_N`/`ENC_ACTIVE_OUTPUT_N` (column 16 top / column 10 bottom):**
> `ENC_ACTIVE_INPUT_N` (column 16, top row) is generated by Cypher-Input and terminates at this
> board only - it is never tapped or relayed further by any intermediate HID board.
> `ENC_ACTIVE_OUTPUT_N` (column 10, bottom row) is a **separate** signal generated by this board's
> own CPLD firmware (after accounting for the cipher pipeline's propagation delay), for
> Cypher-Output to consume as its own legitimate destination - see `Design_Spec.md §3` CPLD Signal
> Routing Matrix and External Keyboard Source Mux.
>
> **`BOARD_ROLE_ID_IN[3:0]`/`BOARD_ROLE_ID_OUT[3:0]` (columns 9-12, 14-17):**
> `BOARD_ROLE_ID_IN[3:0]` is Cypher-Input's own ID, driven on the top row; `BOARD_ROLE_ID_OUT[3:0]`
> is Cypher-Output's own ID, driven on the bottom row - fixed by each board's own passthrough
> wiring convention, regardless of physical stacking order (see `Design_Spec.md §3a`). As a
> permanently-tied hardware identification strap (not a dynamic/switching signal), no additional
> GND shielding is required beyond the fixed center bar. Capability bit encoding
> (`ID[3]:ID[2]:ID[1]:ID[0]`, shared meaning on both Input and Output IDs):
>
> | Bit | Meaning |
> | :---: | :--- |
> | 0 | Characters (A-Z letters) |
> | 1 | Numbers (0-9 digits) |
> | 2 | Special (symbols, e.g. base64-extra `+`/`/`) |
> | 3 | Custom (board declares support for a non-standard capability combination) |
>
> Known values: 26-Char Classic = `0b0001`; 10-Numeric = `0b0010`; 64-Character (default) =
> `0b0111`; 64-Character (custom-support enabled via user-accessible switch) = `0b1111`. See
> `Design_Spec.md §3a` for the full compatibility rule and `HID_VARIANT_ID[3:0]` comparator
> output.

### Cypher Board's own wiring at J5

| Pin(s) | Wiring |
| :--- | :--- |
| Top row (43,41,39,37,35,33) — `ENC_DATA_IN[5:0]` | → CPLD U1 `ENC_IN_KBD[5:0]` (per `Design_Spec.md §3` Port Mapping, `KBD_ENC` role) |
| Bottom row (8,10,12,14,16,18) — `ENC_DATA_OUT[5:0]` | ← CPLD U1 `ENC_OUT_LBD[5:0]` (per `Design_Spec.md §3` Port Mapping, `LBD_DEC` role) |
| 31 — `ENC_ACTIVE_INPUT_N` | → external keyboard source mux (U4/U5), per `Design_Spec.md §3` |
| 20 — `ENC_ACTIVE_OUTPUT_N` | ← driven by this board, after the mux's selected activity state passes through CPLD firmware's propagation-delay accounting (see `Design_Spec.md §3` External Keyboard Source Mux) |
| 17,19,21,23 (top row) — `BOARD_ROLE_ID_IN[3:0]` | → CPLD U1 compatibility comparator input |
| 34,32,30,28 (bottom row) — `BOARD_ROLE_ID_OUT[3:0]` | → CPLD U1 compatibility comparator input |
| 1, 2 — `3V3_ENIG`; 3, 4 — `5V_MAIN` (also 49/50, 47/48) | Board power entry/distribution |

---

## 5. J6 — User Settings Module Hub Connector

> **Connector Definition Owner:** `User_Settings_Module/Board_Layout.md §2` (its own `J1`). Full
> 50-pin template defined there — this section only records this board's own local wiring so it
> cannot drift out of sync with the owning definition.

- **MPN:** QSS-025-01-L-D-A-GP-K (Samtec 50-contact 0.635mm vertical female SMT)
- Mates USM's own top (right-angle male, QTS-025-01-L-D-RA-P) Hub connector. Mating
  gap/tolerance: `design/Standards/Global_Routing_Spec.md §4.1a`.

This board drives / uses the Hub Connector Template as the chain's root (the `J1` end, in USM's
own naming):

| Pins | Wiring |
| :--- | :--- |
| `TDI` | ← driven from FT232H (U17) MPSSE TDI (AD1); this is the system JTAG chain's entry point |
| `TDO` | → received here (whichever HID board is Output-role, relayed back through USM) and forwarded to Mount1 (first Plugboard Encoder Module, `J8`) TDI |
| `TMS`/`TCK`/`CPLD_RESET_N` | Broadcast from the JTAG Hub (see `Design_Spec.md §3` JTAG Hub) |
| `I2C_SDA`/`I2C_SCL` | Dedicated Cypher-peripherals I2C bus (distinct from `I2C1` - shared only with USM, the HID boards, and Cypher-Plugboard) |
| `3V3_ENIG`, GND | Board power entry/distribution |

> **Chain order (see `Design_Spec.md §3` JTAG Hub for full derivation):** FT232H (U17) → `J6` TDI
> → User Settings Module → whichever HID board is Input-role (Cypher-Input CPLD) → whichever HID
> board is Output-role (Cypher-Output CPLD) → USM → `J6` TDO → Mount1 → Mount2 → Mount3 → Mount4 →
> U1 (this board's own CPLD) → `J3` → 30x Rotor CPLDs → `J4` `TTD_RETURN` → R50 → U17 TDO. All
> "static" CPLDs (Cypher-Input, Cypher-Output, 4x Plugboard Encoder Modules, this board's own U1)
> precede the "dynamic" Rotor stack in the chain. The Cypher-Input/Cypher-Output sub-chain hop is
> realised entirely within the User Settings Module and the two HID boards' own wiring, not on
> this board's own copper - see `User_Settings_Module/Design_Spec.md §4`.

---

## 6. J7–J18 — ENC Module Mounts (back face)

> **Connector Definition Owner:** `Encoder_Module/Board_Layout.md §1a-1c`. This board carries only
> the mating DF40C-xDS receptacles; the ENC module owns the DF40C-xDP plug pin-mapping standard.

Four Hirose DF40C-xDS receptacle sets. Each mount:

| Position | Connector | MPN | Pins | Role |
| :--- | :--- | :--- | :--- | :--- |
| A (left) | J7 / J10 / J13 / J16 | DF40C-90DS-0.4V(51) | 90 | plain-bits[63:0] |
| B (centre) | J8 / J11 / J14 / J17 | DF40C-24DS-0.4V(51) | 24 | cypher-bits + JTAG + ENC_ACTIVE_N |
| C (right) | J9 / J12 / J15 / J18 | DF40C-10DS-0.4V(51) | 10 | 3V3_ENIG power |

Pin assignments per connector follow the ENC Module Interface definition in
`Encoder_Module/Board_Layout.md §1a-1c` (reproduced for layout reference in `Design_Spec.md §6
J7–J18`; in case of conflict, the Encoder Module definition is authoritative).

---

## 7. J20+ — Spade Blade Terminal Bank (back face, bottom edge)

64 Keystone 1285-ST spade blade terminals required per ENC module mount position
(4 mounts = 256 terminals total). Full component details and RefDes allocation:
see `Design_Spec.md §6 J20+` and `§11 BOM`. General location is the bottom edge of the back face
(HID interconnect connectors J5/J6 are at the top edge of the same face); exact per-terminal
arrangement within that region is TBD at schematic/layout time. Wired via external spade-to-spade
jumper cables directly to the physical plugboard patch jacks, which are mounted (mechanically
only, no electrical connection) on the Plugboard board - see DEC-088.

---

## 8. TP1–TP12 — PWM/GPCLK Test Pad Loops (back face)

Bare copper test-pad loops (no component, no BOM entry) receiving the reserved `PWM0[0-3]` and
`GPCLK[0]`/`GPCLK[1]` signals from Controller `J2` (see §1). Each signal pad is paired with an
adjacent `GND` test-pad loop for convenient scope/multimeter probing. No active devices are
populated; see `Design_Spec.md DR-CYP-10`.

| RefDes | Signal | Paired GND RefDes |
| :--- | :--- | :--- |
| TP1 | `PWM0[0]` | TP7 |
| TP2 | `PWM0[1]` | TP8 |
| TP3 | `PWM0[2]` | TP9 |
| TP4 | `PWM0[3]` | TP10 |
| TP5 | `GPCLK[0]` | TP11 |
| TP6 | `GPCLK[1]` | TP12 |

Exact physical placement is TBD at schematic/layout time; general location is the back face,
away from the high-speed JTAG/ENC signal routing at J3/J4.

---

## Diagram Reference

See `design/Diagrams/cypher-system-layout.drawio` and renders in `design/Diagrams/renders/`
for the system-level layout diagram showing the Cypher Board's position within the
Rotor Mini-Stack assembly.
