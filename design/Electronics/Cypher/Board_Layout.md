# Cypher Board V1.0 Pinout Reference

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-09-02

> **Board_Layout.md is a visualisation-only document.** Design narrative, specifications, and
> component rationale belong in `Design_Spec.md`. This file contains connector pinout references
> and board orientation notes only.

---

## Orientation Convention

- **Front face:** faces the first Rotor Mini-Stack.
- **Back face:** carries ENC module mounts (J7–J18), the CTL dock connectors (J1/J2), and the
  spade blade terminal bank (J20+) along the **bottom edge** of this face (the HID interconnect
  connectors, J5/J6, are at the top edge of the same face - general placement only, exact
  per-terminal arrangement TBD at layout - see DEC-088).
- **STA side:** the edge where J3 (Stack-Input / STA-side QSS-025 female) is mounted.
- **REF side:** the edge where J4 (Stack-Output / REF-side QSS-025 female) is mounted.

---

## 1. J1 / J2 — Controller Dock (Molex 2195620015)

> **Connector Definition Owner:** `Controller/Board_Layout.md`.
> This board uses the plug (Molex 2195620015) mating with the CTL receptacle (Molex 2195630015).

- **J1:** 5V-biased power dock. 4x 5V_MAIN blades, 1x GND blade, USB D+/D- (TBD pin allocation).
- **J2:** Logic dock. 4x 3V3_ENIG blades, 1x GND blade; JTAG (TCK, TMS, TDI, TTD_RETURN), I2C (SDA, SCL).

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

## 4. J5 / J6 — HID Board Interconnect (Cypher-Input / Cypher-Output, either order)

> **Connector Definition Owner:** this board.
> **Architecture:** Cypher-Input and Cypher-Output each carry **4 connectors** rather than a
> single interconnect: 2 male at their top edge, mounted flush with the board edge so the
> connector face sits flush with the enclosure lid's edge once cased; 2 female at their bottom
> edge, mounted protruding past the board edge far enough to span the enclosure gap and fully
> mate with the neighbouring board's flush-mounted male connector. Only **one** HID board
> connects directly to the Cypher Board at a time — whichever board is physically closest
> (its top/male pair mates here). The second HID board connects only to the first board's
> bottom/female pair, one level further down; a future Plugboard board terminates the bottom of
> that local 2-board stack. Either Cypher-Input or Cypher-Output may occupy the position closest
> to the Cypher Board — this connector pair's pinout is therefore identical regardless of which
> board is plugged in ("either order" support).
>
> **J5 (left, female, QSS-025-01-L-D-A-GP-K, vertical):** mates the top-left (right-angle male,
> QTS-025-01-L-D-RA-P) connector of whichever HID board is present. Carries 3V3_ENIG, 5V_MAIN,
> and GND (2 pins each, excluding the center GND bar), the LED colour/brightness broadcast
> signals from Cypher-Input, and the `BOARD_ROLE_ID` compatibility comparator inputs - full pin
> map below. The physical plugboard patch-jack harness does **not** route through this
> connector - it wires directly to this board's own spade terminal bank (`J20+`) instead, per
> DEC-088.
>
> **J6 (right, female, QSS-025-01-L-D-A-GP-K, vertical):** mates the top-right (right-angle male,
> QTS-025-01-L-D-RA-P) connector of whichever HID board is present. Carries GND on the center
> pin/bar (inherent to the QSS/QTS-025-GP family) plus the JTAG chain-through signals below.
> Cypher-bits/ENC_DATA and I2C passthrough signal reallocation into this connector is a separate
> follow-up not yet defined.

### J5 — Full Pin Map (Power + LED Broadcast + `BOARD_ROLE_ID` Comparator Inputs)

50 contacts: 2 center-GND-bar (1/row) + 24 usable pins/row. Pin numbering: column Cn, top pin =
2n-1, bottom pin = 2n. This is a **board-agnostic template** — how each specific board
(Cypher-Input, Cypher-Output, Plugboard) wires a given pin internally is defined in that board's
own `Design_Spec.md`.

| Top Row Signal | Top Row Pin# | Bottom Row Pin# | Bottom Row Signal |
| :--- | :---: | :---: | :--- |
| **3V3_ENIG** | 1 | 2 | **3V3_ENIG** |
| **3V3_ENIG** | 3 | 4 | **3V3_ENIG** |
| **5V_MAIN** | 5 | 6 | **5V_MAIN** |
| **5V_MAIN** | 7 | 8 | **5V_MAIN** |
| GND | 9 | 10 | GND |
| GND | 11 | 12 | GND |
| GND | 13 | 14 | **RED_DRIVE_N** |
| GND | 15 | 16 | **GREEN_DRIVE_N** |
| **BOARD_ROLE_ID_IN[0]** | 17 | 18 | GND |
| **BOARD_ROLE_ID_IN[1]** | 19 | 20 | GND |
| **BOARD_ROLE_ID_IN[2]** | 21 | 22 | GND |
| **BOARD_ROLE_ID_IN[3]** | 23 | 24 | GND |
| GND (bar) | 25 | 26 | GND (bar) |
| GND | 27 | 28 | **BOARD_ROLE_ID_OUT[3]** |
| GND | 29 | 30 | **BOARD_ROLE_ID_OUT[2]** |
| GND | 31 | 32 | **BOARD_ROLE_ID_OUT[1]** |
| GND | 33 | 34 | **BOARD_ROLE_ID_OUT[0]** |
| **BRIGHTNESS_PWM_EN** | 35 | 36 | GND |
| **BLUE_DRIVE_N** | 37 | 38 | GND |
| GND | 39 | 40 | GND |
| GND | 41 | 42 | GND |
| **5V_MAIN** | 43 | 44 | **5V_MAIN** |
| **5V_MAIN** | 45 | 46 | **5V_MAIN** |
| **3V3_ENIG** | 47 | 48 | **3V3_ENIG** |
| **3V3_ENIG** | 49 | 50 | **3V3_ENIG** |

> **Power/GND pin budget rule:** `3V3_ENIG`, `5V_MAIN`, and GND (excluding the center GND bar and
> the GND pin that is the silent partner row of a signal column) are equally split at 8 pins
> each.
>
> **Rotational (180°) symmetry:** this pin map is a point-symmetric pattern about the center GND
> bar (column 13, pins 25/26) - rotating the connector 180° maps every populated pin onto its
> counterpart at the mirrored column/row (column *n* maps to column 26-*n*). `3V3_ENIG` (columns
> 1/2/24/25), `5V_MAIN` (columns 3/4/22/23), and the two fully-spare GND columns (5/6/20/21) each
> occupy identical nets on both sides of the connector. `RED_DRIVE_N`/`GREEN_DRIVE_N` (columns
> 7/8, bottom row) diagonally oppose `BLUE_DRIVE_N`/`BRIGHTNESS_PWM_EN` (columns 18/19, top row) -
> deliberately kept off the `BOARD_ROLE_ID` block's own row so the two signal groups are visually
> and electrically independent, not contiguous; `BOARD_ROLE_ID_IN[3:0]` (columns 9-12, top row)
> diagonally opposes `BOARD_ROLE_ID_OUT[3:0]` (columns 14-17, bottom row, bit order reversed by
> the rotation).
>
> **`5V_MAIN`:** board power net; final downstream consumption depends on the LED component
> selected in `merge-missing-components.md`.
>
> **LED colour/brightness broadcast:** `RED_DRIVE_N` (pin 14) and `GREEN_DRIVE_N` (pin 16) are
> generated by Cypher-Input on the bottom row; `BLUE_DRIVE_N` (pin 37) and `BRIGHTNESS_PWM_EN`
> (pin 35) are generated by Cypher-Input on the top row - all 4 signals are generated only by
> Cypher-Input (from its own §5 LED Indicator Circuit and §6 Brightness Control) and consumed
> only by Cypher-Output; the row each occupies is a physical placement choice for connector
> symmetry, not a row-ownership convention (unlike `BOARD_ROLE_ID` below). The other row of each
> of these 4 columns is GND.
>
> **`BOARD_ROLE_ID_IN[3:0]`/`BOARD_ROLE_ID_OUT[3:0]`:** `BOARD_ROLE_ID_IN[3:0]` (pins 17/19/21/23)
> is Cypher-Input's own ID, driven on the top row; `BOARD_ROLE_ID_OUT[3:0]` (pins 34/32/30/28) is
> Cypher-Output's own ID, driven on the bottom row - fixed by each board's own passthrough wiring
> convention, regardless of physical stacking order (see `Design_Spec.md §3a`). As a permanently-
> tied hardware identification strap (not a dynamic/switching signal), no additional GND shielding
> is required beyond the fixed center bar. `BOARD_ROLE_ID[3:0]` resides on this connector because
> the right-hand (`J6`) JTAG-template connector has no pin budget available for a 4-bit strap -
> see §3a `BOARD_ROLE_ID` Compatibility Comparator in `Design_Spec.md`. Capability bit encoding
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

### J6 — Full Pin Map (JTAG + ENC_DATA + Board ID + I2C + PWM)

50 contacts: 2 center-GND-bar (1/row) + 24 usable pins/row. Pin numbering: column Cn, top pin =
2n-1, bottom pin = 2n. This is a **board-agnostic template** — pin function (e.g. `TTD_HID_IN`) is
fixed by position; how each specific board (Cypher-Input, Cypher-Output, Plugboard) wires a given
pin internally is defined in that board's own `Design_Spec.md`.

| Top Row Signal | Top Row Pin# | Bottom Row Pin# | Bottom Row Signal |
| :--- | :---: | :---: | :--- |
| GND | 1 | 2 | GND |
| **ENC_DATA[0]** | 3 | 4 | **ENC_DATA[0]** |
| **ENC_DATA[1]** | 5 | 6 | **ENC_DATA[1]** |
| **ENC_DATA[2]** | 7 | 8 | **ENC_DATA[2]** |
| **ENC_DATA[3]** | 9 | 10 | **ENC_DATA[3]** |
| **ENC_DATA[4]** | 11 | 12 | **ENC_DATA[4]** |
| **ENC_DATA[5]** | 13 | 14 | **ENC_DATA[5]** |
| GND | 15 | 16 | GND |
| GND | 17 | 18 | GND |
| GND | 19 | 20 | GND |
| GND | 21 | 22 | GND |
| **CPLD_RESET_N** | 23 | 24 | **ENC_ACTIVE_INPUT_N** |
| GND (bar) | 25 | 26 | GND (bar) |
| **I2C_SDA** | 27 | 28 | **I2C_SCL** |
| GND | 29 | 30 | GND |
| GND | 31 | 32 | GND |
| GND | 33 | 34 | GND |
| GND | 35 | 36 | **TTD_HID_PASS** |
| **TTD_HID_IN** | 37 | 38 | GND |
| GND | 39 | 40 | **TTD_HID_OUT** |
| GND | 41 | 42 | GND |
| **TMS** | 43 | 44 | **TMS** |
| GND | 45 | 46 | GND |
| **TCK** | 47 | 48 | **TCK** |
| GND | 49 | 50 | GND |

> `BOARD_ROLE_ID[3:0]` (pins 17-24) is carried on `J5` - see the `J5 — Full Pin Map` section above
> for the full encoding table and rationale.
>
> `CPLD_RESET_N` uses only the top-row pin (23) — a single instance is sufficient since it is a
> broadcast/unchained signal; the bottom-row pin at this column (24) is reassigned to
>
> `ENC_ACTIVE_INPUT_N` (this board's own internal net name — see `Design_Spec.md §3` I2C-1 Bus
> Devices / U6).

### Cypher Board's own wiring at J6

| Pin(s) | Wiring |
| :--- | :--- |
| Top row (3,5,7,9,11,13) — `ENC_DATA[5:0]` | → CPLD U1 `ENC_IN_KBD[5:0]` (per `Design_Spec.md §3` Port Mapping, `KBD_ENC` role) |
| Bottom row (4,6,8,10,12,14) — `ENC_DATA[5:0]` | → CPLD U1 `ENC_OUT_LBD[5:0]` (per `Design_Spec.md §3` Port Mapping, `LBD_DEC` role) |
| 17-22 — GND | Tied to GND |
| 23 — `CPLD_RESET_N` | Broadcast from the JTAG Hub (see `Design_Spec.md §3`) |
| 24 — `ENC_ACTIVE_INPUT_N` | → I2C GPIO expander (U6), matching the existing `ENC_ACTIVE_INPUT_N` net (GPA[6]) — so the system knows when a key has been depressed, to trigger any initial rotor actuations |
| 27/28 — `I2C_SDA`/`I2C_SCL` | Part of the I2C-1 bus (shared with U6/U7/U8 and U2) |
| 29-32 — GND | Tied to GND |
| 36 — `TTD_HID_PASS` | NC |
| 37 — `TTD_HID_IN` | TDI — driven from FT232H (U17) MPSSE TDI (AD1); this is the chain's TDI source |
| 40 — `TTD_HID_OUT` | Received here (Cypher-Output's own real TDO, the exit of the local HID sub-chain) and forwarded to Mount1 (first Plugboard Encoder Module, `J8`) TDI |
| 43/44, 47/48 | TMS / TCK — broadcast from the JTAG Hub (see `Design_Spec.md §3` JTAG Hub) |

> **Chain order (see `Design_Spec.md §3` JTAG Hub for full derivation):** FT232H (U17) → Cypher-Input
> CPLD → Cypher-Output CPLD → Mount1 → Mount2 → Mount3 → Mount4 → U1 (this board's own CPLD) →
> `J3` → 30x Rotor CPLDs → `J4` `TTD_RETURN` → R50 → U17 TDO. All "static" CPLDs (Cypher-Input,
> Cypher-Output, 4x Plugboard Encoder Modules, this board's own U1) precede the "dynamic" Rotor
> stack in the chain.

---

## 5. J7–J18 — ENC Module Mounts (back face)

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

## 6. J19 — USM Harness (B6B-PH-K-S)

| Pin | Signal |
| :--- | :--- |
| 1 | 3V3_ENIG |
| 2 | 5V_MAIN |
| 3 | GND |
| 4 | SDA |
| 5 | SCL |
| 6 | GND |

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

## Diagram Reference

See `design/Diagrams/cypher-system-layout.drawio` and renders in `design/Diagrams/renders/`
for the system-level layout diagram showing the Cypher Board's position within the
Rotor Mini-Stack assembly.
