# Design Modification Specification: Cypher Stack + `GND_CHASSIS`

**Status:** In Discussion — no design-file implementation applied yet  
**Type:** Point-in-time, self-contained design modification description  
**Last Updated:** 2026-06-07

---

## 1. History Sources (for traceability)

This specification is synthesized from:

1. `.copilot/discussions/extension-mechanical-usage.md`
2. `.copilot/discussions/cypher-block-connectors.md`

All implementation content required for execution is embedded below.

---

## 2. Final Target Architecture

### 2.1 New boards and roles

| Board | Role |
| --- | --- |
| Cypher | Central backplane replacing STA + REF and absorbing JM circuitry |
| Stack-Input | Mini-stack input-side board with native AM circuitry |
| Stack-Output | Mini-stack output-side board |
| Stack-Blanking | Passive/near-passive chain termination board |
| Input-Cypher | Keyboard-facing board with one ENC module |
| Output-Cypher | Lightboard-facing board with one ENC module |

### 2.2 Board lifecycle intent

| Current board | Target state |
| --- | --- |
| STA | Retired; circuitry moved to Cypher |
| REF | Retired; circuitry moved to Cypher |
| EXT | Retired; split into Stack-Input + Stack-Output |
| AM (standalone module board) | Retired as standalone; circuitry moved into Stack-Input |
| JM (standalone module board) | Retired as standalone; circuitry moved into Cypher |
| CTL | Modified host role; no AM/JM host function |
| ROT | Remains active |
| USM | Remains active |
| PM | Remains active |

### 2.3 Stackup authority

- Cypher remains **6-layer**.
- Other boards keep stackups defined by active design and extension decisions.
- No rule in this specification downgrades Cypher to 4-layer.

### 2.4 Mini-stack topology and orientation

```text
               [ Stack-Blanking ]
                /               \
               /                 \
   Stack-Input BACK             Stack-Output BACK
    (left edge)                   (right edge)
          |                           |
   [Stack-Input]  ←-- ROT x5 --→  [Stack-Output]
          |                           |
   Stack-Input FRONT            Stack-Output FRONT
    (right edge)                  (left edge)
               \                 /
                \               /
             (STA side)    (REF side)
                  [  Cypher  ]
```

Front/back orientation is fixed:

- Stack-Input: **front = right edge**, **back = left edge**
- Stack-Output: **front = left edge**, **back = right edge**
- Stack-Blanking mates to the rear side of the last mini-stack.

### 2.5 Board deep-dive implementation requirements

#### Cypher

- Replaces STA + REF and absorbs JM circuitry.
- Hosts stack interfaces for Stack-Input and Stack-Output.
- Hosts interfaces for Input-Cypher and Output-Cypher.
- Retains `GND_CHASSIS` rules from this specification; no local `GND` ↔
  `GND_CHASSIS` bond.
- Cypher-side interconnect behavior must follow §4.1 exactly.

#### Stack-Input

- Carries native AM circuitry (no standalone AM module board).
- Receives and forwards `5V_MAIN`, `3V3_ENIG`, `GND`, and `ENC_ACTIVE_N` on the
  stack chain.
- Implements local taps for actuation from `SIG-BLOCK-G`.
- Implements passive base-board internal-link mating behavior from §4.2.
- Follows `SIG-BLOCK-A/D/E/G/H/I` flow rules in §4.4.

#### Stack-Output

- Carries return-path and chain-pass behavior for ENC/JTAG flows.
- Implements rear-to-front passthrough behavior required by return paths.
- Implements passive base-board internal-link mating behavior from §4.2.
- Follows `SIG-BLOCK-B/C/D/E/F/I` flow rules in §4.4.

#### Stack-Blanking

- Passive/near-passive board at chain end.
- Terminates and bridges required chain-end signal groups per §4.4.
- `SIG-BLOCK-H` (`5V_MAIN`) remains NC at chain end.
- Implements ring/caveat rules from §3 with no local `GND` ↔ `GND_CHASSIS`
  bond.

#### Input-Cypher

- Keyboard-facing board with one ENC module interface.
- Implements top/bottom-row behavior from §4.1.
- Drives data generation path feeding Cypher and mini-stack processing.
- Supports both defined character variants via component counts in §5.

#### Output-Cypher

- Lightboard-facing board with one ENC module interface.
- Implements top/bottom-row behavior from §4.1.
- Receives final decoded outputs and `ENC_ACTIVE_N` gating behavior per §4.4.
- Supports both defined character variants via component counts in §5.

---

## 3. Grounding and Shielding Requirements

### 3.1 Ground-domain model

- `GND` = logic/power reference domain.
- `GND_CHASSIS` = chassis/shield domain.

### 3.2 Single-point bond (global, retained)

- Exactly one galvanic `GND` ↔ `GND_CHASSIS` bond exists.
- Bond location: **Power Module** only, at the defined power-entry boundary.
- No local bonds on any other board.

### 3.3 Chassis ring geometry (to be codified in GRS)

Required default geometry:

- `GND_CHASSIS` perimeter ring width: **2.5 mm**
- Isolation moat width: **1.5 mm**
- Total edge keep-out before inner logic zone: **4.0 mm**

```text
             ◄──────────── 4.0mm Keep-Out ──────────────►
[BOARD EDGE] ──► [2.5mm GND_CHASSIS] ──► [1.5mm MOAT] ──► [INNER LOGIC ZONE]
```

### 3.4 Connector-zone caveat (part of same GRS entry)

Where an external connector is located, local ring relief/break is allowed when
signal pins cannot be terminated inside the ring/moat keep-out region.

```text
       [GND_CHASSIS PLATED HOLE] ──► (Clamped to Metal Enclosure Frame)
                  │
 ┌────────────────┴────────┐              ┌────────────────────────┐
 │   PCB GND_CHASSIS Ring  │              │  PCB GND_CHASSIS Ring  │
 ├─────────────────────────┤  [OPEN GAP]  ├────────────────────────┤
 │     ISOLATION MOAT      │  (No Moat)   │     ISOLATION MOAT     │
 └─────────────────────────┘ ┌──────────┐ └────────────────────────┘
                             │  Conn.   │ ◄── Logic GND & Traces
                             └──────────┘     Extend Fully To Edge
```

### 3.5 Anti-loop constraints

- Ring relief must not create a second `GND` ↔ `GND_CHASSIS` bond.
- Copper topology must avoid ring-loop closure behavior that increases antenna
  effects.

---

## 4. Interconnect and Signal Definitions (Authoritative)

## 4.1 Cypher-owned Input/Output interconnect pin map

| Top row signal | Top pin | Bottom pin | Bottom row signal |
| --- | ---: | ---: | --- |
| 3V3_ENIG | 1 | 2 | 3V3_ENIG |
| JTAG_TCK_FWD | 3 | 4 | ENC_DATA_BOT[5] |
| ENC_ACTIVE_INPUT_N *(ENC_ACTIVE_N)* | 5 | 6 | GND |
| JTAG_TMS_FWD | 7 | 8 | ENC_DATA_BOT[4] |
| GND | 9 | 10 | GND |
| CPLD_RESET_N_FWD | 11 | 12 | ENC_DATA_BOT[3] |
| GND | 13 | 14 | GND |
| JTAG_TDI_FWD | 15 | 16 | ENC_DATA_BOT[2] |
| GND | 17 | 18 | GND |
| GREEN_PWM_N *(inter-board only)* | 19 | 20 | ENC_DATA_BOT[1] |
| BOARD_ROLE_ID_TOP | 21 | 22 | GND |
| I2C_SCL_PASS | 23 | 24 | ENC_DATA_BOT[0] |
| **GND_WEDGE** | 25 | 26 | **GND_WEDGE** |
| ENC_DATA_TOP[0] | 27 | 28 | I2C_SDA_PASS |
| GND | 29 | 30 | BOARD_ROLE_ID_BOT |
| ENC_DATA_TOP[1] | 31 | 32 | YELLOW_PWM_N *(inter-board only)* |
| GND | 33 | 34 | GND |
| ENC_DATA_TOP[2] | 35 | 36 | JTAG_TDO_RET |
| GND | 37 | 38 | GND |
| ENC_DATA_TOP[3] | 39 | 40 | CPLD_RESET_N_RET |
| GND | 41 | 42 | GND |
| ENC_DATA_TOP[4] | 43 | 44 | JTAG_TMS_RET |
| GND | 45 | 46 | ENC_ACTIVE_OUTPUT_N *(ENC_ACTIVE_N)* |
| ENC_DATA_TOP[5] | 47 | 48 | JTAG_TCK_RET |
| 3V3_ENIG | 49 | 50 | 3V3_ENIG |

Notes:

- `5V_MAIN` is not on this interconnect.
- `GREEN_PWM_N` and `YELLOW_PWM_N` are inter-board only and NC at Cypher/Plugboard ends.
- `ENC_ACTIVE_INPUT_N` and `ENC_ACTIVE_OUTPUT_N` stay distinct as connector labels
  for schematic separation while remaining functionally linked to `ENC_ACTIVE_N`.

## 4.2 Mini-stack internal passive base-board 2x15 pin map

| Top row signal | Top pin (odd) | Bottom pin (even) | Bottom row signal |
| --- | ---: | ---: | --- |
| SIG_BLOCK_A_ENC_DATA[0] | 1 | 2 | GND |
| GND | 3 | 4 | SIG_BLOCK_A_ENC_DATA[1] |
| SIG_BLOCK_A_ENC_DATA[2] | 5 | 6 | GND |
| GND | 7 | 8 | SIG_BLOCK_A_ENC_DATA[3] |
| SIG_BLOCK_A_ENC_DATA[4] | 9 | 10 | GND |
| GND | 11 | 12 | SIG_BLOCK_A_ENC_DATA[5] |
| SIG_BLOCK_E_TTD | 13 | 14 | GND |
| GND | 15 | 16 | GND |
| GND | 17 | 18 | SIG_BLOCK_E_TTD |
| SIG_BLOCK_D_ENC_DATA[5] | 19 | 20 | GND |
| GND | 21 | 22 | SIG_BLOCK_D_ENC_DATA[4] |
| SIG_BLOCK_D_ENC_DATA[3] | 23 | 24 | GND |
| GND | 25 | 26 | SIG_BLOCK_D_ENC_DATA[2] |
| SIG_BLOCK_D_ENC_DATA[1] | 27 | 28 | GND |
| GND | 29 | 30 | SIG_BLOCK_D_ENC_DATA[0] |

## 4.3 Signal-block model to implement

| Block | Function | Group | Flow summary |
| --- | --- | --- | --- |
| SIG-BLOCK-A | ENC_DATA forward pass | ENC_DATA[5:0] | Cypher/Input-Cypher into mini-stack forward path |
| SIG-BLOCK-B | ENC_DATA return-to-reflector side | ENC_DATA[5:0] | Chain-end return path back through Stack-Output |
| SIG-BLOCK-C | ENC_DATA outbound from reflector side | ENC_DATA[5:0] | Cypher reflector output toward chain end |
| SIG-BLOCK-D | ENC_DATA machine return direction | ENC_DATA[5:0] | Return-direction traversal into prior stack/Cypher |
| SIG-BLOCK-E | JTAG outbound | TCK/TMS/CPLD_RESET_N/TTD + GND | Outbound chain through mini-stacks |
| SIG-BLOCK-F | JTAG return | TTD_RETURN + GND | Return chain back to module sink |
| SIG-BLOCK-G | Actuation + LED-enable distribution | ENC_ACTIVE_N | Pass-through with local Stack-Input taps |
| SIG-BLOCK-H | Actuation power distribution | 5V_MAIN | Stack-Input chain power |
| SIG-BLOCK-I | Logic/interface power distribution | 3V3_ENIG | Multi-pin power cage across interfaces |

## 4.4 Electronic flow descriptions (authoritative)

### ENC_DATA flow

1. Input-Cypher generates `ENC_DATA[5:0]` from keyboard state and forwards it to
   Cypher.
2. Cypher routes this data toward mini-stack ingress as `SIG-BLOCK-A`.
3. Within each mini-stack forward pass, data traverses rotors in the forward
   direction and exits at Stack-Output.
4. Stack-Output hands data across the passive base-board interposer back to
   Stack-Input, which forwards toward the next mini-stack rear path.
5. At chain end, Stack-Blanking bridges return-side blocks and data propagates
   back through Stack-Output chain paths toward Cypher.
6. Cypher performs reflector-side transform and emits outbound data path toward
   last-stack side (`SIG-BLOCK-C`), then through return-direction traversal
   (`SIG-BLOCK-D`) back toward Cypher/output path.
7. Final decoded output is driven toward Output-Cypher display logic.

### JTAG flow

1. Outbound JTAG chain is carried as `SIG-BLOCK-E` with `TTD`, `TCK`, `TMS`,
   and `CPLD_RESET_N` (with interleaved/guard GND strategy).
2. In each mini-stack, timing/control signals are passed with local taps and
   `TTD` traverses rotor chain links.
3. At chain end, Stack-Blanking terminates `TCK/TMS/CPLD_RESET_N`; outbound
   `TTD` is renamed `TTD_RETURN`.
4. Return chain is carried as `SIG-BLOCK-F` back through Stack-Output paths to
   Cypher and then to the JTAG sink endpoint.

### Actuation and LED-enable flow

1. Cypher distributes actuation trigger as `ENC_ACTIVE_N` on `SIG-BLOCK-G`.
2. Stack-Input boards pass this signal front-to-rear while taking local taps
   for their own actuation control.
3. Cypher also forwards `ENC_ACTIVE_N` to Output-Cypher as global LED-enable
   gate behavior.
4. Chain-end behavior terminates this distribution on Stack-Blanking.
5. `ENC_ACTIVE_INPUT_N` and `ENC_ACTIVE_OUTPUT_N` remain connector-label aliases
   for schematic net separation while mapped to functional `ENC_ACTIVE_N`.

### Power flow

1. `SIG-BLOCK-H` = `5V_MAIN` for Stack-Input actuation power distribution.
2. `5V_MAIN` is distributed along Stack-Input chain only; Stack-Output does not
   consume/distribute `5V_MAIN`.
3. `SIG-BLOCK-I` = `3V3_ENIG` distributed across Stack-Input, Stack-Output,
   Stack-Blanking, and related chain interfaces using multi-pin allocation for
   integrity.
4. At chain end, Stack-Blanking keeps `SIG-BLOCK-H` as NC while maintaining
   required logic/interface continuity behavior for other groups.

---

## 5. Component and Procurement Baseline (Authoritative)

| # | Component | MPN | Mfr | Mouser | DigiKey | JLCPCB | Symbol | Footprint | 3D |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 25-pin RA female Samtec | QSS-025-01-L-D-RA-K | Samtec | 200-QSS02501LDRAK | QSS-025-01-L-D-RA-K-ND | C6156774 | ✓ | ✓ | ✓ |
| 2 | 25-pin RA male Samtec | QTS-025-01-L-D-RA-P | Samtec | 200-QTS02501LDRAP | QTS-025-01-L-D-RA-P-ND | C7267889 | ✓ | ✓ | ✓ |
| 3 | 25-pin vertical female Samtec | QSS-025-01-L-D-A-GP-K | Samtec | 200-QSS02501LDAGPK | QSS-025-01-L-D-A-GP-K-ND | C6632602 | ✓ | ✓ | ✓ |
| 4 | 25-pin vertical male Samtec | QTS-025-01-L-D-A-GP-K-TR | Samtec | 200-QTS02501LDAGPKTR | QTS-025-01-L-D-A-GP-K-TR-ND | C5714677 | ✓ | ✓ | ✓ |
| 5 | Hirose ENC 90-pin (module side) | DF40C-90DP-0.4V(51) | Hirose | 798-DF40C90DP0.4V51 | H11878CT-ND | C424648 | ✓ | ✓ | ✓ |
| 6 | Hirose ENC 24-pin (module side) | DF40C-24DP-0.4V(51) | Hirose | 798-DF40C24DP0.4V51 | H11620CT-ND | C424639 | ✓ | ✓ | ✓ |
| 7 | Hirose ENC 10-pin (module side) | DF40C-10DP-0.4V(51) | Hirose | 798-DF40C10DP0.4V51 | H11616CT-ND | C424635 | ✓ | ✓ | ✓ |
| 8 | Hirose ENC 90-pin (mating side) | DF40C-90DS-0.4V(51) | Hirose | 798-DF40C90DS0.4V51 | 26-DF40C-90DS-0.4V(51)CT-ND | C2911197 | ✓ | ✓ | ✓ |
| 9 | Hirose ENC 24-pin (mating side) | DF40C-24DS-0.4V(51) | Hirose | 798-DF40C24DS0.4V51 | H11621CT-ND | C424640 | ✓ | ✓ | ✓ |
| 10 | Hirose ENC 10-pin (mating side) | DF40C-10DS-0.4V(51) | Hirose | 798-DF40C10DS0.4V51 | H11617CT-ND | C424636 | ✓ | ✓ | ✓ |
| 11 | 30-pos RA female IDC mating connector | SQT-115-01-L-D-RA | Samtec | 200-SQT11501LDRA | SAM1246-15-ND | C7318577 | ✓ | ✓ | ✓ |
| 12 | Mechanical keyboard switch | MX2A-71NB | Cherry | 540-MX2A-71NB | 1644-MX2A-71NB-ND | Global/consignment | - | - | - |
| 13 | Mechanical keyboard hot-swap socket | PG151101S11 | Kailh | - | - | C41430893 | ✓ | ✓ | ✓ |
| 14 | Keyboard LED (bicolor) | APFA2507Y2G2C-C2 | Kingbright | 604-APFA2507Y2G2C-C2 | 754-APFA2507Y2G2C-C2CT-ND | C7216896 | ✓ | ✓ | ✓ |
| 15 | Lightboard LED (bicolor) | APFA2507Y2G2C-C2 | Kingbright | 604-APFA2507Y2G2C-C2 | 754-APFA2507Y2G2C-C2CT-ND | C7216896 | ✓ | ✓ | ✓ |
| 16 | Yellow LED resistor 130R 0402 | AT0402CRD07130RL | Yageo | 603-AT0402CRD07130RL | AT0402CRD07130RL-ND | C2142705 | - | - | - |
| 17 | Green LED resistor 120R 0402 | AT0402CRD07120RL | Yageo | 603-AT0402CRD07120RL | AT0402CRD07120RL-ND | C4286960 | - | - | - |
| 18 | Brightness potentiometer 50k | 3310P-001-503L | Bourns | 652-3310P-001-503L | 3310P-001-503L-ND | C5891432 | ✓ | ✓ | ✓ |

Variant counts:

- 26-char variant: 26 LEDs and 26 each of 130R/120R resistors per board.
- 64-char variant: 41 LEDs and 41 each of 130R/120R resistors per board.

MOQ notes:

- Row 16: DigiKey MOQ 10000, Mouser MOQ 10000, JLCPCB MOQ 110.
- Row 17: DigiKey MOQ 10000, JLCPCB MOQ 90, Mouser currently unavailable.

---

## 6. Active Design Modification Matrix

## 6.1 Standards-level modifications

| Target | Required change |
| --- | --- |
| `design/Standards/Global_Routing_Spec.md` | Add new `GND_CHASSIS` ring geometry rule (2.5 mm ring, 1.5 mm moat, 4.0 mm keep-out) |
| Same new GRS entry | Add connector-zone caveat for local ring relief when pin termination cannot occur inside keep-out |
| Same new GRS entry | Link explicitly to existing single-point bond rule in `Global_Routing_Spec.md §5` |
| Same new GRS entry | Explicitly call non-usage in module-board contexts (JTAG Module, Actuation Module, CM5 context) |

## 6.2 Existing active boards

| Board | Required modification in active design files |
| --- | --- |
| Power Module | Keep sole `GND` ↔ `GND_CHASSIS` bond; align wording to new GRS ring entry |
| Controller | Reference new GRS ring entry; only local connector-gap caveats (HDMI/Ethernet/USB zones) |
| Rotor (A+B) | Ensure both rotor PCBs implement `GND_CHASSIS` perimeter ring; no local bond |
| User Settings Module | Keep explicit reference to new GRS ring entry |
| Encoder | Treat as module-context moving forward for ring-propagation purposes |
| Extension/Stator/Reflector | Legacy boards in retirement path under this architecture |

## 6.3 New replacement boards

| Board | Required modification scope |
| --- | --- |
| Cypher | Implement architecture, interconnect table in §4.1, and GRS ring cross-reference with local caveats |
| Stack-Input | Implement architecture, signal blocks in §4.3, ring cross-reference with local caveats |
| Stack-Output | Implement architecture, signal blocks in §4.3, ring cross-reference with local caveats |
| Stack-Blanking | Implement passive chain-end behavior and ring cross-reference with local caveats |
| Input-Cypher | Implement §4.1 interconnect behavior and component set in §5 |
| Output-Cypher | Implement §4.1 interconnect behavior and component set in §5 |

---

## 7. Implementation Prerequisites

Before design-file implementation:

1. This unified specification is accepted as the single baseline.
2. New GRS `GND_CHASSIS` ring entry text is approved.
3. Board-level cross-reference plan is approved.
4. Rows 16–17 library assets are addressed as required by implementation scope.
5. Explicit implementation instruction is provided.

---

## 8. Cross-Reference Anchors

- Primary source history: `.copilot/discussions/extension-mechanical-usage.md`
- Grounding source history: `.copilot/discussions/cypher-block-connectors.md`
- Standards target: `design/Standards/Global_Routing_Spec.md`
- Single-point rule anchor: `design/Standards/Global_Routing_Spec.md §5`
- EMC rationale anchor: `design/Standards/Certification_Evidence.md §2.2`
