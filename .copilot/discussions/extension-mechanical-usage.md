# Discussion: Extension Mechanical Usage Changes

**Status:** In Discussion — no design changes made yet  
**Todo ID:** `extension-mechanical-usage`  
**Opened:** 2026-05-17  
**Last Updated:** 2026-06-06 (entry 20)

---

## Purpose

This document is a pre-design discussion space. The user has a set of changes in mind that will significantly reshape how the Extension board and the boards it interfaces with physically interact.
All design implications, component requirements, and open questions should be captured here before any changes are made to design specifications or schematics.

**No design files should be modified until this discussion reaches a clear decision point and explicit implementation approval is given.**

---

## Known Scope

### New Boards Being Defined

| New Board Name | Description | Source Circuits |
| --- | --- | --- |
| **Cypher Board** | Central backplane board. Replaces STA + REF. Rotor mini-stacks attach to it. Also absorbs the JTAG Module (from CTL). BtB connections to CTL, Input-Cypher Board, and Output-Cypher Board. Spade tab connectors on back. 6-layer stackup. | STA circuits + REF circuits + JM circuits (from CTL) |
| **Stack-Input Board** | Input-side board of the Rotor Mini-Stack. **Front = right edge** (2 male stacking connectors: bottom + just above centre). **Back = left edge** (2 female stacking connectors: same positions). Input mating connectors to first ROT board. AM circuits native. Receives **5V_MAIN + 3V3_ENIG** via stacking connectors. Carries ribbon cable IDC for ENC_DATA. | EXT input-side circuits + AM circuits |
| **Stack-Output Board** | Output-side board of the Rotor Mini-Stack. **Front = left edge** (2 male stacking connectors: top + just below centre). **Back = right edge** (2 female stacking connectors: same positions). Output mating connectors from last ROT board. Receives **3V3_ENIG only** via stacking connectors. Carries ribbon cable IDC for ENC_DATA. | EXT output-side circuits |
| **Stack-Blanking Board** | Termination board. **Male connectors** matching all four female positions (Stack-Input back + Stack-Output back). Terminates the last mini-stack in the chain. Can also connect directly to Cypher Board female connectors for transport/testing without mini-stacks fitted. Passive or near-passive. | New design |
| **Input-Cypher Board** | New board — essentially the keyboard. 1 ENC module via Hirose-style BtB. Mechanical keyboard buttons on opposite face. BtB connection to Cypher Board. Chains with Output-Cypher Board in either order. | New design; ENC becomes module |
| **Output-Cypher Board** | New board — essentially the lightboard. 1 ENC module via Hirose-style BtB. LEDs on opposite face. BtB connection to Cypher Board. Chains with Input-Cypher Board in either order. | New design; ENC becomes module |

### Rotor Mini-Stack

The Rotor Mini-Stack is the assembly unit consisting of:

- **Stack-Input Board** (front: connects to Cypher Board or previous mini-stack rear; rear:
  connects to next mini-stack or blanking board; surface Samtec connectors; connect to the
  input mating connectors of first ROT board)
- **ROT boards** (5 per mini-stack — one per rotor position in the stack; maximum 6
  mini-stacks in the system = 30 rotor positions total)
- **Stack-Output Board** (rear: connects to next mini-stack or blanking board; surface Samtec
  connectors: connect to output mating connectors from last ROT board; front: connects to
  previous mini-stack rear or Cypher Board)
- **Stack-Blanking Board** (fitted to the rear of the last mini-stack only — terminates the
  chain)

#### Stacking Connector Topology

```text
                              [Cypher Board]
                       (STA side)         (REF side)
                          /                    \
                         /                      \
                        /                        \
          (female, bottom +                      (female, top +
           above-centre)                          below-centre)
                |                                     |
   RIGHT EDGE = FRONT                             LEFT EDGE = FRONT
   [Stack-Input Board]     ←—— ROT boards ——→     [Stack-Output Board]
   LEFT EDGE = BACK                               RIGHT EDGE = BACK
                |                                    |
          (female, bottom +                    (female, top +
           above-centre)                        below-centre)
                 \                                   /
                  \                                 /
                   \                               /
                    \                             /
                [            Blanking Board           ]
```

**Mini-stack front/back orientation:**

- **Stack-Input front** = RIGHT edge; **Stack-Input back** = LEFT edge
- **Stack-Output front** = LEFT edge; **Stack-Output back** = RIGHT edge
- The Stack-Input and Stack-Output boards stand either side of the mini-stack facing in towards each other
- The mini-stack "front face" is the right edge of Stack-Input + left edge of Stack-Output (both facing the Cypher Board / previous mini-stack)
- The mini-stack "back face" is the left edge of Stack-Input + right edge of Stack-Output (facing the next mini-stack or Stack-Blanking Board)

**Connector gender and position:**

| Board | Edge | Gender | Connector 1 position | Connector 2 position |
| --- | --- | --- | --- | --- |
| Cypher Board | Stack-Input (STA) side | **Female** | Bottom | Just above centre |
| Cypher Board | Stack-Output (REF) side | **Female** | Top | Just below centre |
| Stack-Input | Front (right edge) | **Male** | Bottom | Just above centre |
| Stack-Input | Back (left edge) | **Female** | Bottom | Just above centre |
| Stack-Output | Front (left edge) | **Male** | Top | Just below centre |
| Stack-Output | Back (right edge) | **Female** | Top | Just below centre |
| Stack-Blanking Board | (single face) | **Male** | (matches both Stack-Output back females) | (matches both Stack-Input back females) |

**Positional keying logic:**

- Stack-Input front males (bottom + above-centre) can **only** mate with female connectors at those same positions (Cypher Board Stack-Input side, or previous mini-stack Stack-Input back)
- Stack-Output front males (top + below-centre) can **only** mate with female connectors at those positions (Cypher Board Stack-Output side, or previous mini-stack Stack-Output back)
- It is physically impossible to insert a Stack-Input where a Stack-Output belongs (connector positions do not match)

**Daisy-chain:**
Each successive mini-stack's front males (Stack-Input right edge + Stack-Output left edge) mate with the previous mini-stack's back females (Stack-Input left edge + Stack-Output right edge):

```text
[Cypher Board females] ←→ [Mini-stack 1 front males] ... [Mini-stack 1 back females] ←→ [Mini-stack 2 front males] ... [Mini-stack 2 back females] ←→ [Stack-Blanking Board males]
```

**Stack-Blanking Board:**

- Has **male connectors** matching all four female positions (Stack-Input back + Stack-Output back)
- Can be fitted to the last mini-stack to terminate the chain
- Can also connect **directly to the Cypher Board** female connectors for transportation / testing without any mini-stack fitted

**Power rail assignment and pass-through:**

| Board | 5V_MAIN | 3V3_ENIG | Notes |
| --- | --- | --- | --- |
| Stack-Input | ✅ Yes | ✅ Yes | AM motor driver requires 5V_MAIN; logic uses 3V3_ENIG. Both rails received on front-bottom-right and passed through to rear-bottom-right for next mini-stack. |
| Stack-Output | ❌ No | ✅ Yes | Logic only — no 5V_MAIN required |
| Stack-Blanking Board | ❌ No | ✅ Yes | Near-passive; no active ICs expected. Contains internal routing traces for signal return (see Q41). |

**8-connector signal assignment (assembly-level view, from 2026-05-26):**

The 8 inter-stack stacking connectors are named by position when viewing the mini-stack assembly from the front (Cypher Board / previous-stack side) or rear (next-stack / blanking board side).
Connector type expected to be Samtec-style (exact part TBD — see Q28/Q37).
These connectors are distinct from the face-mounted ROT-board Samtec BtB connectors which are internal to the mini-stack and unchanged.

*Front face (Cypher Board / previous-stack side):*

| Connector | Board/Edge | Signals |
| --- | --- | --- |
| **front-top-right** | Stack-Input front (right edge) | ENC_IN[5:0], ENC_OUT[5:0], TTD_IN (TDI from Cypher Board/prev stack to first ROT Board B), TMS, TCK, CPLD_RESET_N |
| **front-bottom-right** | Stack-Input front (right edge) | 3V3_ENIG, 5V_MAIN, GND, ENC_ACTIVE_N (from ENC module — active-low debounced keypress signal; triggers rotor actuation on keypress via native AM circuit) |
| **front-top-left** | Stack-Output front (left edge) | TTD_RETURN + ENC_DATA return (return path back toward Cypher Board) |
| **front-bottom-left** | Stack-Output front (left edge) | 3V3_ENIG + GND only (Stack-Output board power feed) |

*Rear face (next-stack / blanking board side):*

| Connector | Board/Edge | Signals |
| --- | --- | --- |
| **rear-top-right** | Stack-Input back (left edge) | Return signals from ribbon cable (ENC_DATA + JTAG TTD) forwarded to next mini-stack front-top-right or blanking board |
| **rear-bottom-right** | Stack-Input back (left edge) | 3V3_ENIG, 5V_MAIN, GND passthrough to next mini-stack front-bottom-right or blanking board |
| **rear-top-left** | Stack-Output back (right edge) | TTD_RETURN + ENC_DATA return passthrough (received from blanking board at the last mini-stack) |
| **rear-bottom-left** | Stack-Output back (right edge) | 3V3_ENIG, GND — Stack-Output board power supply (ROT face connectors on Stack-Output side have power pins NC to avoid ground loops; power provided by this connector instead — see Q43) |

*Signal flow through a mini-stack:*

1. Cypher Board / previous stack sends data + JTAG forward via **front-top-right** (ENC_IN/OUT, TTD_IN, TMS, TCK, CPLD_RESET_N)
2. Cypher Board / previous stack sends power + ENC_ACTIVE_N via **front-bottom-right** (3V3_ENIG, 5V_MAIN, GND, ENC_ACTIVE_N)
3. Stack-Input routes data and JTAG to face-mounted ROT connectors (Board B Samtec input — same BtB system as current EXT board)
4. Data and JTAG traverse all 5 ROT boards in series
5. Last ROT board (Board A Samtec output) routes into Stack-Output face-mounted connectors
6. Stack-Output connects via ribbon cable IDC back to Stack-Input — returning ENC_DATA and JTAG TTD back-path
7. Stack-Input maps ribbon return to **rear-top-right** and forwards to next mini-stack or blanking board
8. Power and ENC_ACTIVE_N pass straight through Stack-Input: **front-bottom-right** → **rear-bottom-right** (3V3_ENIG, 5V_MAIN, and ENC_ACTIVE_N all pass through;
   each Stack-Input taps ENC_ACTIVE_N and 5V_MAIN locally for its AM circuit)
9. At the last mini-stack: blanking board routes TTD_RETURN and ENC_DATA return to Stack-Output **rear-top-left**; every Stack-Output board has an internal **rear-top-left → front-top-left** passthrough.
10. TTD_RETURN and ENC_DATA return then daisy-chain forward through all Stack-Output boards back to the Cypher Board.

> **Note:** Entry 10 is a historical draft. **Entry 11 pin tables are authoritative** and take precedence where they differ.

### Boards Affected / Fate

| Board | Current Role | Fate |
| --- | --- | --- |
| **STA** — Stator | CPLD-based signal switching backplane | ➜ Circuits migrate to **Cypher Board**; standalone board retired |
| **REF** — Reflector | Signal reflection path | ➜ Circuits migrate to **Cypher Board**; standalone board retired |
| **EXT** — Extension | Sits at every 5th position in rotor chain; signal extension + 5V/3V3_ENIG regeneration | ➜ Split into **Stack-Input** (input side) and **Stack-Output** (output side); standalone board retired |
| **AM** — Actuation Module | Separate plug-in module on CTL & EXT (STM32G071, motor driver) | ➜ Integrated **natively** into **Stack-Input Board** (not as an attached sub-module). Each mini-stack has its own AM circuits. Standalone AM module board retired. AM attachment point on CTL removed entirely. |
| **CTL** — Controller | Hosts JM and AM connection points | ➜ Modified: loses JTAG Module circuit and AM attachment connector (J11 DF40); **no AM of any form remains on CTL**; gains BtB connection to Cypher Board replacing the Link-Beta connector to STA |
| **JM** — JTAG Module | Currently a module board on CTL | ➜ Moves to **Cypher Board** |
| **ENC** — Encoder | Standalone keyboard/encoder interface board | ➜ Becomes a **module-style board** that plugs into Cypher Board (or Plugboard) Input-Cypher Board and/or Output-Cypher Board via Hirose-style BtB connectors; current SW1–SW40 keyboard switches may become obsolete |
| **ROT** — Rotor | Individual rotor sense boards | ➜ Unchanged (connects within mini-stack between Stack-Input and Stack-Output) |
| **USM** — User Settings | User configuration module | Possibly replace IDC connector with Dual Samtec-style connector(s) to attach to right side of Input-Cypher and Output-Cypher Boards |
| **PM** — Power Module | Power supply | ➜ No change expected |

> **New boards summary:** Cypher Board, Stack-Input Board, Stack-Output Board, Stack-Blanking Board, Input-Cypher Board, Output-Cypher Board — 6 new boards total.

Additional impact areas to consider:

- Rotor chain physical geometry (Cypher Board as central backplane changes mechanical topology)
- Power distribution along the chain (Stack-Input/Stack-Output replace EXT power regeneration)
- Link-Beta interface (currently CTL→STA): now CTL→Cypher Board via BtB
- BtB interfaces: Cypher Board ↔ CTL, Cypher Board ↔ Input-Cypher Board, Cypher Board ↔ Output-Cypher Board (all Samtec-style)
- ENC module connector: ENC boards now plug into Cypher, Input-Cypher and Output-Cypher via Hirose-style BtB
- AM-CTL interface (currently DF40 J1/J11): removed from CTL entirely
- JM-CTL interface: removed from CTL; JM now on Cypher Board
- Mechanical enclosure constraints

---

## Proposed Changes

### Summary

The current board-per-function architecture (separate STA, REF, EXT, AM, JM boards) is being consolidated into
a new physical assembly concept — the **Rotor Mini-Stack** — centred around a new **Cypher Board** backplane.

- STA + REF merge into a single **Cypher Board**, which acts as the backplane for the rotor mini-stack assembly
- The EXT board is split into **Stack-Input Board** (input side) and **Stack-Output Board** (output side)
- The AM is no longer a plug-in module on CTL; its functionality is integrated natively into the **Stack-Input Board**
- The JM (JTAG Module), currently hosted on CTL, moves to the **Cypher Board**
- CTL is simplified: loses both the JM circuit and the AM attachment point

### Detail

#### Cypher Board

- Replaces both STA and REF as a single unified board
- Acts as a backplane: rotor mini-stacks (Stack-Input + ROT boards + Stack-Output) connect to it
- Inherits all STA CPLD signal-switching circuitry
- Inherits all REF signal-reflection path circuitry
- Hosts the JTAG Module circuitry (migrated from CTL)
- **4 mounts on the back** for ENC plugboard role modules (one per plugboard position)
- **Spade tab connectors on the back** — jack plug harnesses attach here (moved from ENC board); trace routing to/from these is done within the Cypher Board layers
- **6-layer stackup** expected (departure from standard 4-layer; driven by routing density of combined STA+REF+spade-tab traces)
- **Manufacturer note:** JLCPCB 6-layer capability is a known constraint; prototype manufacture may be done by **PCBWay** due to 6-layer board + double-sided assembly requirement
- Exact connector strategy for rotor mini-stack attachment: see Entry 10 and Entry 11
- BtB connector to CTL same as defined for the original STA Link-Beta connector
- BtB connectors to Input-Cypher Board and Output-Cypher Board: Samtec-style connectors to match Stack-Input and Stack-Output connector family

#### Stack-Input Board

- Input-side board of the Rotor Mini-Stack
- **Front side** (2 keyed stacking connectors): connects to the Cypher Board (first stack) or the rear of the previous mini-stack (subsequent stacks)
- **Rear side** (2 keyed stacking connectors): carries input mating connectors to the first ROT board in the stack
- **Actuation Module circuits are native to this board** — this is the ONLY board in the system that carries AM functionality; there is no AM on CTL or anywhere else
- Each mini-stack therefore has its own independent actuation capability via its Stack-Input Board (STM32G071-equivalent + motor driver, or equivalent circuits)
- AM functionality is native (on-board circuit), NOT an attached sub-module
- Carries a **ribbon cable IDC connector** for return signals — connects to Stack-Output; carries ENC_DATA (ENC_IN/OUT processed by 5 ROTs) and JTAG TTD (last ROT TDO) back to Stack-Input;
  power is not on this IDC but GND is used for shielding signals
- Stacking connectors are keyed — only one valid orientation
- Exact connector type, pin count, and signal/power assignment: see Entry 10 and Entry 11

#### Stack-Output Board

- Output-side board of the Rotor Mini-Stack
- **Rear side** (2 keyed stacking connectors): carries output mating connectors from the last ROT board in the stack
- **Front side** (2 keyed stacking connectors): connects to the next mini-stack front, or to the Stack-Blanking Board on the last stack
- Carries a **ribbon cable IDC connector** for return signals back to Stack-Input (ENC_DATA + JTAG TTD from last ROT TDO)
- Stacking connectors are keyed — only one valid orientation
- Exact connector type, pin count, and signal/power assignment: see Entry 10 and Entry 11

#### Stack-Blanking Board (new)

- Passive (or near-passive) termination board
- Fits on the **rear of the last Rotor Mini-Stack** in the chain
- Completes all required system wiring (signal terminations, power rails, etc.)
- Exact content: maps ENC_DATA and TTD_RETURN from top-right connector (rear-top-right of last mini-stack) to top-left (rear-top-left of last mini-stack).

#### CTL Board Changes

- JTAG Module circuit removed (moves to Cypher Board)
- AM attachment connector (currently J11, DF40) removed — **no AM of any form remains on CTL**
- Link-Beta now targets Cypher Board instead of STA and includes the USB2.0 data traces for the JM on Cypher Board
- All other CTL functionality unchanged

#### Input-Cypher Board (new)

- Essentially the keyboard panel board
- Accepts **1 ENC module** via Hirose-style BtB connector
- Opposite face carries **mechanical keyboard style buttons** (MX-compatible or similar — exact switch TBD)
- BtB connection to the Cypher Board
- **No dedicated debounce circuitry required:** the ENC CPLD (EPM570T100I5N, 570 LEs) is sufficient to debounce all 64 input lines
  using the shared bank-level architecture defined in `Encoder_Logic.md §5` (~69% LE utilisation — see Q22)
- Input-Cypher and Output-Cypher boards can connect **in either order** and chain from one to the other from the Cypher Board connectors
- Exact ENC module connector type and pin count: **TBD**
- Chaining connector and protocol: **TBD (user to describe later)**

#### Output-Cypher Board (new)

- Similar shape and layout to the Input-Cypher Board
- Accepts **1 ENC module** via Hirose-style BtB connector
- Opposite face carries **LEDs** (output display only — no buttons)
- BtB connection to the Cypher Board
- Chains with Input-Cypher Board; can be connected in either order from the Cypher Board connectors
- LED driver location: **TBD** (may be on the ENC module or on this board — see Q21)
- Exact ENC module connector type and pin count: **TBD**
- Chaining connector and protocol: **TBD (user to describe later)**

#### ENC Board Changes

- ENC transitions from a standalone board to a **module-style board**
- **Spade tab connectors REMOVED** from ENC — these move to the back of the Cypher Board
- **SW1–SW40 keyboard switches REMOVED** from ENC — keyboard buttons move to the Input-Cypher Board
- ENC module now contains: CPLD + supporting components + bulk caps + status LED
- **Small connector (one side):** original Stator-side signal connections (what was the stator pin interface)
- **Large connector (other side):** signal lines for what were the spade tab connections (now routed within the Cypher Board layers)
- Plugs into Input-Cypher Board or Output-Cypher Board via Hirose-style BtB connectors
- Exact connector types and pin counts: **TBD**

---

## Current Keyboard Button Components — Obsolescence

The following components are confirmed or expected to become obsolete:

| Board | RefDes | MPN | Description | Status |
| --- | --- | --- | --- | --- |
| ENC | SW1–SW40 | *(no standard MPN — eBay gadgetskingdom)* | DPDT keyboard switches (current) | ✅ **Confirmed obsolete** — buttons move to Input-Cypher Board as mechanical keyboard switches |

New mechanical keyboard style switches are required for the Input-Cypher Board. The exact MX-compatible (or equivalent) switch and any associated keycap/housing requirements are **TBD**.

> *Confirm exact mechanical keyboard switch specification, including actuation force, travel, MPN, and whether hot-swap sockets are desired.*

---

## New Component Requirements

Any new components introduced by this change will need the following fully confirmed before implementation:

| # | Component Description | Candidate MPN | Manufacturer | Status | Notes | Mouser PN | DigiKey PN | JLCPCB PN | KiCAD Symbol | KiCAD Footprint | 3D Model |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 25-pin stacking connector — **female receptacle** (on Stack-Input/Stack-Output rear edge and Input-Cypher/Output-Cypher top edge) | QSS-025-01-L-D-RA-K | Samtec | Confirmed | Mouser cheaper; DigiKey MOQ 32 | 200-QSS02501LDRAK | QSS-025-01-L-D-RA-K-ND | C6156774 | ✓ | ✓ | ✓ |
| 2 | 25-pin stacking connector — **male plug** (on Stack-Input/Stack-Output front edge and Input-Cypher/Output-Cypher bottom edge) | QTS-025-01-L-D-RA-P | Samtec | Confirmed | JLCPCB best for prototype; DigiKey MOQ 65; Mouser MOQ 65 | 200-QTS02501LDRAP | QTS-025-01-L-D-RA-P-ND | C7267889 | ✓ | ✓ | ✓ |
| 3 | 25-pin vertical SMD connector — **female receptacle** (on Cypher Board for Stack-Input/Stack-Output/Input-Cypher/Output-Cypher interfaces) | QSS-025-01-L-D-A-GP-K | Samtec | Confirmed | Mouser cheaper | 200-QSS02501LDAGPK | QSS-025-01-L-D-A-GP-K-ND | C6632602 | ✓ | ✓ | ✓ |
| 4 | 25-pin vertical SMD connector — **male plug** (on blanking board) | QTS-025-01-L-D-A-GP-K-TR | Samtec | Confirmed | QTS DigiKey MOQ 200, Mouser MOQ 375; JLCPCB best for prototype | 200-QTS02501LDAGPKTR | QTS-025-01-L-D-A-GP-K-TR-ND | C5714677 | ✓ | ✓ | ✓ |
| 5 | 90-pin ENC module Hirose BtB interface (ENC-owned) | DF40C-90DP-0.4V(51) | Hirose | Confirmed | - | 798-DF40C90DP0.4V51 | H11878CT-ND | C424648 | ✓ | ✓ | ✓ |
| 6 | 24-pin ENC module Hirose BtB interface (ENC-owned) | DF40C-24DP-0.4V(51) | Hirose | Confirmed | - | 798-DF40C24DP0.4V51 | H11620CT-ND | C424639 | ✓ | ✓ | ✓ |
| 7 | 10-pin ENC module Hirose BtB interface (ENC-owned) | DF40C-10DP-0.4V(51) | Hirose | Confirmed | - | 798-DF40C10DP0.4V51 | H11616CT-ND | C424635 | ✓ | ✓ | ✓ |
| 8 | 90-pin Mating connector for ENC module Hirose BtB interface (on Input-Cypher / Output-Cypher / Cypher backplane) | DF40C-90DS-0.4V(51) | Hirose | Confirmed | - | 798-DF40C90DS0.4V51 | 26-DF40C-90DS-0.4V(51)CT-ND | C2911197 | ✓ | ✓ | ✓ |
| 9 | 24-pin Mating connector for ENC module Hirose BtB interface (on Input-Cypher / Output-Cypher / Cypher backplane) | DF40C-24DS-0.4V(51) | Hirose | Confirmed | - | 798-DF40C24DS0.4V51 | H11621CT-ND | C424640 | ✓ | ✓ | ✓ |
| 10 | 10-pin Mating connector for ENC module Hirose BtB interface (on Input-Cypher / Output-Cypher / Cypher backplane) | DF40C-10DS-0.4V(51) | Hirose | Confirmed | - | 798-DF40C10DS0.4V51 | H11617CT-ND | C424636 | ✓ | ✓ | ✓ |
| 11 | Mini-stack return IDC cable connector pair (Stack-Output -> Stack-Input return path) | TBD | TBD | Pending | - | - | - | - | - | - | - |
| 12 | Mechanical keyboard switches for Input-Cypher (MX-style or compatible) | MX2A-71NB | Cherry | Confirmed | Amazon available for prototyping; hot-swap mounts to be revisited in a follow-on discussion | 540-MX2A-71NB | 1644-MX2A-71NB-ND | Global sourcing / consignment | - | - | - |
| 12.1 | Mechanical keyboard hot-swap socket bases (MX-compatible) — **Kailh PG151101S11** | PG151101S11 | Kailh | Confirmed | Keycaps and button stems sourced separately from Amazon | - | - | C41430893 | ✓ | ✓ | ✓ |
| 13 | Mechanical keyboard LEDs (MX-switch compatible) | APFA2507Y2G2C-C2 | Kingbright | Confirmed | - | 604-APFA2507Y2G2C-C2 | 754-APFA2507Y2G2C-C2CT-ND | C7216896 | ✓ | ✓ | ✓ |
| 14 | Lightboard LEDs + current-limit resistors (active-low from ENC outputs) | TBD | TBD | Pending | Reuse the same LEDs/current-limit values as Input-Cypher; revisit BtB pin mapping for GREEN_ACTIVE_N / YELLOW_ACTIVE_N | - | - | - | - | - | - |
| 15 | Keyboard LED current-limiting resistor — **Yellow** (130 Ω, 0402, ×26 per board); R = (3.3 − 2.0) / 0.010 = 130 Ω; P = 13 mW | TBD | TBD | Pending | - | - | - | - | - | - | - |
| 16 | Keyboard LED current-limiting resistor — **Green** (120 Ω, 0402, ×26 per board); R = (3.3 − 2.1) / 0.010 = 120 Ω; P = 12 mW | TBD | TBD | Pending | - | - | - | - | - | - | - |
| 17 | Rotary potentiometer, 50 kΩ — **keyboard brightness dial** (panel-mount on Input-Cypher Board); 555 R\_A variable element | 3310P-001-503L | Bourns | Confirmed | Local datasheet and KiCad assets imported | 652-3310P-001-503L | 3310P-001-503L-ND | C5891432 | ✓ | ✓ | ✓ |

> *Populate this table as component candidates are identified during discussion.*

---

## BOM-Protected Components

The following parts are **already present** in the Consolidated BOM on boards that this discussion will retire
or restructure. These rows must not be removed or altered during any other discussion or review. When each
destination board's BOM column is created, these rows must be updated to include the new board's quantities.

| # | Component Description | MPN | Manufacturer | DigiKey PN | Mouser PN | JLCPCB | Current BOM Usage | New Board Need |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 kΩ 1% Thick-Film 0402 resistor | ERJ-2RKF1001X | Panasonic | P1.00KLCT-ND | 667-ERJ-2RKF1001X | C242161 | PM: R24–R26, R30–R31; USM: R12–R17, R54–R65 (23 total) | Input-Cypher Board — 555 R_B discharge limiter (×1 per board) |
| 2 | 10 nF 50V X7R 0402 capacitor | CL05B103KB5NNNC | Samsung | 1276-1008-1-ND | 187-CL05B103KB5NNNC | C15195 | PM: C49 (1 total) | Input-Cypher Board — 555 timing capacitor C (×1 per board) |
| 3 | 100 nF 50V X7R 0402 capacitor | CL05B104KB5NNNC | Samsung | 1276-CL05B104KB5NNNCCT-ND | 187-CL05B104KB5NNNC | C960916 | PM, CTL, JM, USM, ENC, AM, STA, EXT, ROT (126 total) | Input-Cypher Board — 555 Pin-5 noise-bypass capacitor (×1 per board) |
| 4 | CMOS 555-compatible timer SOT-23-5 | MIC1555YM5-TR | Microchip Technology | 576-2576-1-ND | 998-MIC1555YM5TR | C145373 | PM: U9, U13 (2 total) | Input-Cypher Board — astable PWM brightness oscillator (×1 per board) |
| 5 | P-channel MOSFET AEC-Q101 SOT-23 | SQ2319ADS-T1_BE3 | Vishay | 742-SQ2319ADS-T1_BE3CT-ND | 78-SQ2319ADS-T1_BE3 | C3280190 | USM: Q19–Q30 (12 total) | Input-Cypher Board — LED high-side switch: YELLOW_DRIVE_N and GREEN_DRIVE_N (×2 per board) |
| 6 | STM32 MCU LQFP-32 | STM32G071K8T3TR | STMicroelectronics | 497-STM32G071K8T3TR-ND | 511-STM32G071K8T3TR | Global sourcing | AM: U1 (retiring — 1 total) | Stack-Input Board — native AM actuation circuit (×1 per mini-stack) |
| 7 | USB↔MPSSE bridge LQFP-48 | FT232HL-REEL | FTDI Chip | 768-1101-1-ND | 895-FT232HL-REEL | C51997 | JM: U1 (retiring — 1 total) | Cypher Board — absorbs JM JTAG module circuit (×1 per machine) |
| 8 | 4.7 µF X7R 50 V 1210 capacitor | CGA6P3X7R1H475K250AD | TDK | 445-10040-1-ND | 810-CGA6P3X7R1H475KD | C3877549 | JM: C5; AM: C4 (both retiring — 2 total) | Stack-Input Board + Cypher Board — 3V3/supply reservoir cap (×1 each) |
| 9 | Dual 3-state buffer VSSOP-8 | SN74LVC2G125DCUR | Texas Instruments | 296-SN74LVC2G125DCURCT-ND | 595-SN74LVC2G125DCUR | C21404 | JM: U2; EXT: U1 (both retiring — 2 total) | Cypher Board — absorbs JM USB differential signal buffer (×1 per machine) |
| 10 | 12 MHz SMD crystal SMD-5032 | 435F12012IET | CTS | 110-435F12012IETTR-ND | 774-435F12012IET | C19766404 (Extended) | JM: Y1 (retiring — 1 total) | Cypher Board — absorbs JM USB reference oscillator crystal (×1 per machine) |
| 11 | 33 pF C0G/NP0 0402 crystal-load capacitor | C0402C330J5GAUTO | Kemet | 399-12979-1-ND | 80-C0402C330J5GAUTO | C2169327 | JM: C10, C11 (retiring — 2 total) | Cypher Board — crystal load capacitors for JM oscillator circuit (×2 per machine) |
| 12 | 33 Ω 1% 0402 resistor | ERJ-2RKF33R0X | Panasonic | P33.0LCT-ND | 667-ERJ-2RKF33R0X | C278594 | JM: R1–R4 (retiring — 4 total) | Cypher Board — USB D+/D− series resistors from JM circuit (×4 per machine) |
| 13 | 5+15-pin hybrid plug [Molex] | 2195620015 | Molex | 900-2195620015-ND | 538-219562-0015 | Global sourcing | STA: J11, J12 (retiring — 2 total) | Cypher Board — absorbs STA keyboard harness connectors (×2 per machine) |
| 14 | Quad 2-to-1 MUX TSSOP-16 | 74HC157PW-Q100,118 | Nexperia | 1727-74HC157PW-Q100,118CT-ND | 771-74HC157PWQ100118 | C546614 | STA: U4, U5 (retiring — 2 total) | Cypher Board — absorbs STA signal-routing multiplexers (×2 per machine) |
| 15 | 120 Ω @100 MHz ferrite bead 1206 | HI1206P121R-10 | Laird | 240-2410-1-ND | 875-HI1206P121R-10 | C2442103 | STA: L1–L4 (retiring — 4 total) | Cypher Board — absorbs STA power-entry ferrite beads (×4 per machine) |
| 16 | 30-pin 2×15 2.54 mm shrouded box THT | 2BHR-30-VUA | Adam Tech | 2057-2BHR-30-VUA-ND | 737-2BHR-30-VUA | C17346400 | STA: J10; REF: J4; EXT: J7, J8 (all retiring — 4 total) | Destination TBD — all current user boards retiring; protect until Cypher Board connector sizing confirmed |

> **Note:** Row 5 (`SQ2319ADS-T1_BE3`) — confirmed suitable from local datasheet (`design/Datasheets/vishay-sq2319ads-datasheet.md`):
> I_D = −4.6 A continuous at 25 °C (requirement ≥ 300 mA ✓); V_GS(th) max = −2.5 V, so V_GS = −3.3 V provides −0.8 V worst-case overdrive — device enhances ✓.
>
> **Note:** Row 16 (`2BHR-30-VUA`) — all three boards using this connector (STA, REF, EXT) are being retired.
> The connector size may change on the Cypher Board or new boards. Protected here as a precaution until confirmed.

---

## Discussion

> *Use this section as a running log of decisions, user thoughts, and questions answered during the discussion phase. Add new entries at the bottom with a date.*

### 2026-05-17 — Architectural Restructuring Defined

User described the following changes:

1. **Cypher Board** (new) — STA + REF merged into single backplane board. Also absorbs the JTAG Module from CTL. Rotor mini-stacks attach to this board.
   BtB connections to CTL, Input-Cypher Board, and Output-Cypher Board.
2. **Stack-Input Board** (new) — input-side split of the EXT board. AM functionality integrated natively (not as a plug-in module). No longer connects to CTL at all.
3. **Stack-Output Board** (new) — output-side split of the EXT board.
4. **Input-Cypher Board** (new) — keyboard panel board. ENC boards attach as module-style boards via Hirose-style BtB connectors. BtB to Cypher Board.
5. **Output-Cypher Board** (new) — lightboard panel board. Also accepts ENC module-style boards via Hirose-style BtB connectors. BtB to Cypher Board.
6. **Rotor Mini-Stack** — assembly concept: Stack-Input + ROT boards + Stack-Output, attaching to the Cypher Board backplane.
7. **CTL** — loses JTAG Module circuit and AM (J11 DF40) attachment point; gains BtB connection to Cypher Board.
8. **AM** — standalone module board retired; functionality moves natively to Stack-Input Board.
9. **STA, REF, EXT** — all standalone boards retired; circuits migrated to new boards above.
10. **JM** — moves from CTL to Cypher Board.
11. **ENC** — becomes a module-style board that plugs into Input-Cypher or Output-Cypher; SW1–SW40 may become obsolete (TBD).
12. Process: define new boards and migrate existing circuits first, then remove old board details.

### 2026-05-17 — Mini-Stack Connector Topology and Stack-Blanking Board Defined

User provided further detail on how the mini-stack chain connects and terminates:

1. **Stack-Input Board** carries the input mating connectors to the first ROT board of the mini-stack. Front side connects to Cypher Board (or previous mini-stack rear). Rear side has mating connectors.
2. **Stack-Output Board** similarly: rear side has output mating connectors from the last ROT board. Front side connects to next mini-stack or Stack-Blanking Board.
3. **Stacking connector layout:** 2 connectors on each side (front and rear) of BOTH Stack-Input and Stack-Output boards = 4 per board. Must be **keyed** — one valid orientation only.
4. **Stacking connectors carry power.** ENC_DATA signals are carried separately via **ribbon cable IDC connectors** (power is NOT on the IDC ribbon).
5. **Stack-Blanking Board** (new — 7th new board): goes on the rear of the last mini-stack to complete system wiring.
6. This topology allows many mini-stacks to be **daisy-chained**: rear of Stack-Output → front of next Stack-Input → ... → Stack-Blanking Board on the final Stack-Output rear.

---

User provided further detail on the ENC module redesign and Cypher Board back-plane specifics:

1. **ENC module content (confirmed):** CPLD + supporting components + bulk caps + status LED only. Spade tab connectors and keyboard switches both REMOVED from ENC.
2. **ENC connector topology:** small connector (one side) for original Stator-side pin connections; large connector (other side) for the former spade-tab signal lines.
   The Hirose-style BtB connector is the ENC-to-Input/Output-Cypher interface.
3. **Cypher Board back:** 4 mounts for ENC plugboard role modules. Spade tab connectors (for jack plug harnesses) now live here. Trace routing from spade tabs is done within Cypher Board copper layers.
4. **Cypher Board stackup:** 6-layer expected. JLCPCB is a known constraint for 6-layer; PCBWay is the likely prototype manufacturer due to 6-layer + double-sided assembly.
5. **Input-Cypher Board:** 1 ENC module + mechanical keyboard buttons on opposite face.
   ENC CPLD (EPM570T100I5N) confirmed sufficient to debounce all 64 inputs using the shared bank-level architecture — no debounce circuitry needed on this board (see Q22).
6. **Output-Cypher Board:** same shape/layout as Input-Cypher but with LEDs (not buttons).
7. **Chaining:** Input-Cypher and Output-Cypher can connect in EITHER ORDER, chaining from the Cypher Board connectors. Connection detail deferred by user for a later session.
8. **SW1–SW40 obsolescence confirmed:** ENC keyboard switches are retired. New MX-compatible (or similar) mechanical keyboard switches needed on Input-Cypher Board.

---

### 2026-05-17 — Stacking Connector Gender, Position, and Power Assignment (Entry 7)

User defined connector gender, positional layout, orientation, and power split:

1. **Cypher Board: female connectors only** on both the Stack-Input side and the Stack-Output side.
2. **Stack-Input front (right edge): male** at bottom + just above centre. **Stack-Input back (left edge): female** at same positions.
3. **Stack-Output front (left edge): male** at top + just below centre. **Stack-Output back (right edge): female** at same positions.
4. **Positional keying:** Stack-Input connectors (bottom + above-centre) cannot physically mate with Stack-Output connector positions (top + below-centre) — orientation error is mechanically impossible.
5. **Stack-Blanking Board: male** at all four positions — mates with the last mini-stack's back females (Stack-Input left edge + Stack-Output right edge).
   Can also connect directly to Cypher Board females for transportation without mini-stacks.
6. **Power split:** Stack-Input receives **5V_MAIN + 3V3_ENIG** (AM motor driver needs 5V). Stack-Output receives **3V3_ENIG only**.
7. **Mini-stack front face** = right edge of Stack-Input + left edge of Stack-Output (both face the Cypher Board or previous stack). **Back face** = left edge of Stack-Input + right edge of Stack-Output.

---

User clarified: the Cypher Board connects to **both** Stack-Input and Stack-Output boards (not just one). The prior linear topology diagram was incorrect. The correct topology is:

- Cypher Board has dedicated connections to Stack-Input (input side) **and** Stack-Output (output side) of each mini-stack
- The Rotor boards sit between Stack-Input and Stack-Output within the mini-stack

Full signal layout for these connections is **deferred** — user to define. This signal definition will determine the mechanical assembly geometry of the mini-stack.

---

User confirmed: the Stack-Input Board is the **only** board in the system that carries Actuation Module circuits. Key implications:

1. **AM removed from CTL entirely** — no AM attachment point, no AM signals, no J11 DF40 on CTL.
2. **AM is native to Stack-Input** — not an attached sub-module. The STM32G071-equivalent and motor driver ICs are on the Stack-Input Board PCB itself.
3. **Each mini-stack has independent actuation** — one AM circuit set per mini-stack, housed in its Stack-Input Board. This means rotor position sensing and actuation is fully distributed per stack.
4. **Consequence for power budget:** each Stack-Input Board carries the AM power load; stacking connectors must supply sufficient current for both Stack-Input logic/AM circuits and ROT boards.

---

### 2026-05-26 — Signal Assignments, ROT Count, Power, AM, and I/O Board Chaining (Entry 8)

User provided detailed answers to multiple open questions:

1. Q36 — Signal assignment per connector (now defined):
   - **front-top-right (Stack-Input):** ENC_IN[5:0], ENC_OUT[5:0], TTD_IN (JTAG TDI from Cypher Board or previous stack to first ROT Board B), TMS, TCK, CPLD_RESET_N
   - **front-bottom-right (Stack-Input):** 3V3_ENIG, 5V_MAIN, GND, ENC_ACTIVE_N (from ENC module — active-low debounced keypress signal; triggers rotor actuation on keypress via native AM circuit)
   - **front-top-left (Stack-Output):** TTD_RETURN + ENC_DATA return (return path back to Cypher Board)
   - **front-bottom-left (Stack-Output):** 3V3_ENIG + GND only (Stack-Output board power feed)
   - **rear-top-right (Stack-Input back):** return signals from ribbon cable (ENC_DATA + JTAG TTD) forwarded to next mini-stack front-top-right or blanking board
   - **rear-bottom-right (Stack-Input back):** 3V3_ENIG, 5V_MAIN, GND passthrough to next mini-stack
   - **rear-top-left (Stack-Output back):** TTD_RETURN + ENC_DATA return passthrough (received from blanking board routing at last mini-stack)
   - **rear-bottom-left (Stack-Output back):** 3V3_ENIG + GND (Stack-Output board power; ROT face connectors on Stack-Output side have power pins NC — avoids ground loops — see Q43)
   - Signal flow: front-top-right data/JTAG into Stack-Input → face-mounted ROT connectors (Board B Samtec input, unchanged) → 5 ROT boards in series → last ROT Board A Samtec output
     → Stack-Output → ribbon cable IDC back to Stack-Input → out rear-top-right
2. Q5/Q32 — ROT boards per mini-stack:
   - **5 ROT boards per mini-stack.** Maximum 6 mini-stacks = 30 rotor positions total.
3. Q28/Q37 — Stacking connector type:
   - Expected to be Samtec-style. Exact part not yet selected — TBD.
4. Q38 — Power pass-through:
   - **Both 3V3_ENIG and 5V_MAIN** pass through Stack-Input: received on front-bottom-right, forwarded out rear-bottom-right to next mini-stack.
5. Q34 — AM power budget:
   - One servo motor + AM circuit (STM32G071 + motor driver) per mini-stack.
   - Max 6 mini-stacks = 6 AM circuits simultaneously.
   - Per-stack AM load = same as current standalone AM board (exact current figures in AM Board Design_Spec).
6. Q35 — AM MCU:
   - Same STM32G071 + motor driver as current AM board — identical circuits, made native to Stack-Input PCB. No changes to the design.
7. Q25 — Input-Cypher / Output-Cypher chaining:
   - 2 male Samtec connectors on the bottom edge of each board; 2 female Samtec connectors on the top edge.
   - **Input-Cypher:** consumes left-most male connector pins (ENC/keyboard signals); left-most female = NC except 3V3_ENIG + GND; right-most male passes through to right-most female.
   - **Output-Cypher:** left-most male passes through to left-most female; consumes right-most male pins (lightboard signals); right-most female = NC except 3V3_ENIG + GND.
   - Either board can be inserted first in the chain — the passthrough pins allow either order.
8. Q26 — Keyboard switch:
   - MX-style mechanical push button (same as modern keyboards). Exact MPN, actuation spec, and hot-swap socket requirement TBD.
9. Q22/Q23 — CPLD debounce capacity analysis (EPM570T100I5N):
   - CPLD confirmed as **EPM570T100I5N** (570 LEs). User clarified they had confused the part with the smaller EPM240.
   - `Encoder_Logic.md §5` already specifies a **shared bank-level debounce** architecture (NOT 64 independent counters):
     three 64-bit bank registers (raw/candidate/stable), one shared stability counter, one shared sample-tick divider.
   - Estimated LE utilisation for ENCODE image: ~394 / 570 LEs (~69% utilisation), ~31% margin.
   - **Conclusion: EPM570 is sufficient. No hardware debounce circuits are needed on Input-Cypher Board.** Pre-synthesis estimate; Quartus fit will give exact figures.

**mini-stack-base-board reminder:**
User noted a future architectural idea — the **`mini-stack-base-board`** — as an alternative to the ribbon cable IDC for the Stack-Output → Stack-Input return path. See Entry 9 and Q44 for the full description.

---

### 2026-05-26 — Q40–Q44 answers; Q42 proposed pin mapping (Entry 9)

**Q40 — TTD_RETURN propagation through intermediate mini-stacks:**

- Every Stack-Output board has a direct **rear-top-left → front-top-left** internal passthrough (no active logic needed).
- The blanking board routes TTD_RETURN to the last Stack-Output's rear-top-left.
- TTD_RETURN then daisy-chains forward through each Stack-Output board's internal passthrough back to the Cypher Board.

**Q41 — Blanking board:**

- Confirmed as a **basic pass-through PCB with routed traces** (not a shorting assembly).
- Internal signal routing detail TBD (which connector to connector, what signals).
- User has a future alternative idea deferred as `signal-trace-simplification-and-routing`.

**Q43 — rear-bottom-left connector:**

- Carries **3V3_ENIG + GND only** — Stack-Output board power supply.
- ROT face connectors on the Stack-Output side have power pins NC (same ground-loop-avoidance pattern as current EXT board J2 being NC; power was provided by Extension Port instead).
- Stack-Output board 3V3_ENIG is provided by this stacking connector instead of via the ROT face-connector chain.
- **Resolved by Entry 11/Q45:** ENC_DATA return is carried on rear-top-left/front-top-left with TTD_RETURN; rear-bottom-left remains 3V3_ENIG + GND only.

**Q44 / mini-stack-base-board:**

- Proposed as an alternative to the ribbon cable IDC for the Stack-Output → Stack-Input internal return path within each mini-stack.
- Concept: a pass-through PCB using the same connector style as the current STA–CTL interface (board-to-board, not ribbon cable).
- Advantages: mechanically solidifies the mini-stack; better signal integrity than a ribbon cable (ground planes top and bottom for shielding).
- **Not yet part of the current changeset.** User is still in design brain-dump phase. Will be revisited in a dedicated future session if adopted.
- A future discussion label `signal-trace-simplification-and-routing` was also recorded for future work related to blanking board and signal routing simplifications.

---

### 2026-05-26 - Q42 — Updated per-pin signal mapping (Entry 10)

> ⚠️ **Correction banner:** Entry 10 is kept for historical context only. Where Entry 10 and Entry 11 differ, **Entry 11 is authoritative**.

All connectors are Samtec-style, 0.8mm pitch, SMT. Sizes based on ROT face connector precedents (ERM8-005 = 10-pin 2×5; ERM8-010 = 20-pin 2×10). Exact Samtec part numbers TBD (see Q28/Q37).
Per-user request: no reserved/NC pins on Cypher-facing stacking connectors — unused pins are to be tied to GND unless explicitly required to be NC on Cypher Input/Output boards.

#### J_FTR / J_RTR — front-top-right / rear-top-right: 20-pin 2×10 — Forward data / JTAG into next mini-stack

| Pos | Pin A | Pin B | Notes |
| --- | --- | --- | --- |
| 1 | ENC_IN[0] | ENC_IN[1] | Forward data into next stack |
| 2 | ENC_IN[2] | ENC_IN[3] | |
| 3 | ENC_IN[4] | ENC_IN[5] | |
| 4 | GND | GND | Guard |
| 5 | ENC_OUT[0] | ENC_OUT[1] | |
| 6 | ENC_OUT[2] | ENC_OUT[3] | |
| 7 | ENC_OUT[4] | ENC_OUT[5] | |
| 8 | GND | GND | Guard |
| 9 | TMS | TCK | JTAG forward (shared) |
| 10 | TTD (TDI) | CPLD_RESET_N | TTD = TDI for next stack's first ROT |

Notes: front-top-right carries forward ENC_DATA and JTAG/TDI into the next mini-stack. Rear-top-right (on the back face) carries the processed forward signals coming from the ribbon/blanking board.

#### J_FTL / J_RTL — front-top-left / rear-top-left: 20-pin 2×10 — Return data / JTAG return into Cypher Board (Reflector role)

| Pos | Pin A | Pin B | Notes |
| --- | --- | --- | --- |
| 1 | ENC_IN[0] (return) | ENC_IN[1] (return) | Data return from end-of-stack to Cypher Board |
| 2 | ENC_IN[2] (return) | ENC_IN[3] (return) | |
| 3 | ENC_IN[4] (return) | ENC_IN[5] (return) | |
| 4 | GND | GND | Guard |
| 5 | ENC_OUT[0] (return) | ENC_OUT[1] (return) | |
| 6 | ENC_OUT[2] (return) | ENC_OUT[3] (return) | |
| 7 | ENC_OUT[4] (return) | ENC_OUT[5] (return) | |
| 8 | GND | GND | Guard |
| 9 | TTD_RETURN | GND | TTD_RETURN (last ROT TDO path) — routed here by blanking board; paired guard to avoid NC pins |
| 10 | GND | GND | Previously reserved — now GND per user instruction |

Notes: top-left connectors carry the ENC_DATA return path back to the Cypher Board (Reflector). TTD_RETURN is provisioned on top-left and now explicitly paired with GND on the adjacent pin (no NCs left).
Per-user instruction, reserved pins have been converted to GND for robustness and testability.

#### J_FBR / J_RBR — front-bottom-right / rear-bottom-right: 20-pin 2×10 — Power + ENC_ACTIVE_N

Pin numbering convention: left column = Pins 1–10 (top→bottom), right column = Pins 11–20 (top→bottom). Proposed per-pin mapping (explicit linear pins for auditability):

| Pin | Signal | Notes |
| --- | --- | --- |
| 1 | 5V_MAIN | Parallel power pin — AM servo supply |
| 2 | GND | Ground return |
| 3 | 5V_MAIN | Parallel power pin |
| 4 | GND | Ground return |
| 5 | 5V_MAIN | Parallel power pin |
| 6 | GND | Ground return |
| 7 | 5V_MAIN | Parallel power pin |
| 8 | GND | Ground return |
| 9 | 5V_MAIN | Parallel power pin |
| 10 | GND | Ground return |
| 11 | 3V3_ENIG | Logic supply |
| 12 | 3V3_ENIG | Logic supply |
| 13 | 3V3_ENIG | Logic supply |
| 14 | 3V3_ENIG | Logic supply |
| 15 | GND | Ground return |
| 16 | GND | Ground return |
| 17 | GND | Ground return |
| 18 | GND | Ground return |
| 19 | ENC_ACTIVE_N | Debounced keypress (active-low) — local AM trigger |
| 20 | CPLD_RESET_N | CPLD reset (active-low) |

Notes: This linear pin assignment matches the user's approved mapping: pins [1,3,5,7,9] = 5V_MAIN (5 pins), pins [11–14] = 3V3_ENIG (4 pins), pins [2,4,6,8,10,15–18] = GND (9 pins),
pin 19 = ENC_ACTIVE_N, pin 20 = CPLD_RESET_N. The explicit numbering eliminates ambiguity between left/right column interpretation.
Current capacity rationale: ERM8 qualification (2.2 A/pin) and 75% continuous‑use rule were applied during the prior calculation;
adjust counts if further derating or thermal limits are found in the qualification report.

#### J_FBL / J_RBL — front-bottom-left / rear-bottom-left: 10-pin 2×5 — Power only (Stack-Output side)

| Pos | Pin A | Pin B | Notes |
| --- | --- | --- | --- |
| 1 | 3V3_ENIG | 3V3_ENIG | Logic supply for Stack-Output boards |
| 2 | 3V3_ENIG | GND | |
| 3 | GND | GND | |
| 4 | GND | GND | |
| 5 | GND | GND | |

Notes: front-bottom-left / rear-bottom-left remain power-only for Stack-Output boards (3V3_ENIG + GND). ENC_DATA remains carried on the top connectors (forward on top-right; return on top-left).
Per earlier discussion, rear-top-left (Stack-Output back) now carries both TTD_RETURN and ENC_DATA return signals coming from the blanking board, in addition to its passthrough role for TTD_RETURN.

> *Entry 10 updated with user-requested corrections: rear-top-left now includes ENC_DATA return alongside TTD_RETURN; front/rear-bottom-right upgraded to 20-pin for power/GND redundancy;
> reserved pins on top-left changed to GND. User approval requested. Q45 remains marked as resolved if this matches expectations.*

---

### 2026-05-27 — Explicit User Input (Entry 11)

#### Extension Mechanical Usage — Pin Mappings (Draft)

> File generated by Copilot CLI into .copilot/discussions for user editing.
Generated from Entry 10 per-user review.

Connector designators updated to follow standard refdes format.
Rear connectors mirror front signals with inverted I/O roles as defined below; J2/J4/J6/J8 invert Input/Output.

Updated by user based on the intent of the idea trying to be described and badly interpreted by the GPT-5 mini AI model.
This now contains the correct pin mappings the user intended and should be used to fix the incorrect details within Entry 10 of the discussion.

#### J1 — front-top-right (same pin out and connector should be used for the Blanking board connector STA side)

| Note (R1) | Direction (R1) | Signal (R1) | Pin (R1) | Pin (R2) | Signal (R2) | Direction (R2) | Note (R2) |
| - | - | GND | 1 | 14 | GND | - | - |
| - | In | ENC_IN[0] | 2 | 15 | ENC_IN[1] | In | - |
| - | In | ENC_IN[2] | 3 | 16 | ENC_IN[3] | In | - |
| - | In | ENC_IN[4] | 4 | 17 | ENC_IN[5] | In | - |
| - | - | GND | 5 | 18 | GND | - | - |
| JTAG | In | TMS | 6 | 19 | TCK | In | JTAG clock |
| - | - | GND | 7 | 20 | GND | - | - |
| JTAG TDI | In | TTD | 8 | 21 | CPLD_RESET_N | In | active-low |
| - | - | GND | 9 | 22 | GND | - | - |
| - | Out | ENC_OUT[4] | 10 | 23 | ENC_OUT[5] | Out | - |
| - | Out | ENC_OUT[2] | 11 | 24 | ENC_OUT[3] | Out | - |
| - | Out | ENC_OUT[0] | 12 | 25 | ENC_OUT[1] | Out | - |
| - | - | GND | 13 | 26 | GND | - | - |

#### J2 rear-top-right (same pin out and connector should be used for the Cypher board connector STA side)

| Note (R1) | Direction (R1) | Signal (R1) | Pin (R1) | Pin (R2) | Signal (R2) | Direction (R2) | Note (R2) |
| - | - | GND | 1 | 14 | GND | - | - |
| - | Out | ENC_OUT[0] | 2 | 15 | ENC_OUT[1] | Out | - |
| - | Out | ENC_OUT[2] | 3 | 16 | ENC_OUT[3] | Out | - |
| - | Out | ENC_OUT[4] | 4 | 17 | ENC_OUT[5] | Out | - |
| - | - | GND | 5 | 18 | GND | - | - |
| JTAG | Out | TMS | 6 | 19 | TCK | Out | JTAG clock |
| - | - | GND | 7 | 20 | GND | - | - |
| JTAG TDO | Out | TTD | 8 | 21 | CPLD_RESET_N | Out | active-low |
| - | - | GND | 9 | 22 | GND | - | - |
| - | In | ENC_IN[4] | 10 | 23 | ENC_IN[5] | In | - |
| - | In | ENC_IN[2] | 11 | 24 | ENC_IN[3] | In | - |
| - | In | ENC_IN[0] | 12 | 25 | ENC_IN[1] | In | - |
| - | - | GND | 13 | 26 | GND | - | - |

#### J3 — front-top-left (same pin out and connector should be used for the Blanking board connector REF side)

| Note (R1) | Direction (R1) | Signal (R1) | Pin (R1) | Pin (R2) | Signal (R2) | Direction (R2) | Note (R2) |
| - | - | GND | 1 | 13 | GND | - | - |
| - | Out | ENC_IN[0] | 2 | 14 | ENC_IN[1] | Out | - |
| - | Out | ENC_IN[2] | 3 | 15 | ENC_IN[3] | Out | - |
| - | Out | ENC_IN[4] | 4 | 16 | ENC_IN[5] | Out | - |
| - | - | GND | 5 | 17 | GND | - | - |
| last ROT TDO path | Out | TTD_RETURN | 6 | 18 | GND | - | - |
| - | - | GND | 7 | 19 | TTD_RETURN | Out | last ROT TDO path |
| - | - | GND | 8 | 20 | GND | - | - |
| - | In | ENC_OUT[4] | 9 | 21 | ENC_OUT[5] | In | - |
| - | In | ENC_OUT[2] | 10 | 22 | ENC_OUT[3] | In | - |
| - | In | ENC_OUT[0] | 11 | 23 | ENC_OUT[1] | In | - |
| - | - | GND | 12 | 24 | GND | - | - |

#### J4 - rear-top-left (same pin out and connector should be used for the Cypher board connector REF side)

| Note (R1) | Direction (R1) | Signal (R1) | Pin (R1) | Pin (R2) | Signal (R2) | Direction (R2) | Note (R2) |
| - | - | GND | 1 | 13 | GND | - | - |
| - | In | ENC_IN[0] | 2 | 14 | ENC_IN[1] | In | - |
| - | In | ENC_IN[2] | 3 | 15 | ENC_IN[3] | In | - |
| - | In | ENC_IN[4] | 4 | 16 | ENC_IN[5] | In | - |
| - | - | GND | 5 | 17 | GND | - | - |
| last ROT TDO path | In | TTD_RETURN | 6 | 18 | GND | - | - |
| - | - | GND | 7 | 19 | TTD_RETURN | In | last ROT TDO path |
| - | - | GND | 8 | 20 | GND | - | - |
| - | Out | ENC_OUT[4] | 9 | 21 | ENC_OUT[5] | Out | - |
| - | Out | ENC_OUT[2] | 10 | 22 | ENC_OUT[3] | Out | - |
| - | Out | ENC_OUT[0] | 11 | 23 | ENC_OUT[1] | Out | - |
| - | - | GND | 12 | 24 | GND | - | - |

#### J5 — front-bottom-right (20-pin) (J6 rear-bottom-right = same pin mapping, signals I/O inverted)

| Note (R1) | Direction (R1) | Signal (R1) | Pin (R1) | Pin (R2) | Signal (R2) | Direction (R2) | Note (R2) |
| active-low keypress | In | ENC_ACTIVE_N | 1 | 11 | GND | - | - |
| - | - | GND | 2 | 12 | GND | - | - |
| - | - | GND | 3 | 13 | 5V_MAIN | - | - |
| - | - | 5V_MAIN | 4 | 14 | 5V_MAIN | - | - |
| - | - | 5V_MAIN | 5 | 15 | 5V_MAIN | - | - |
| - | - | 3V3_ENIG | 6 | 16 | 3V3_ENIG | - | - |
| - | - | 3V3_ENIG | 7 | 17 | 3V3_ENIG | - | - |
| - | - | GND | 8 | 18 | GND | - | - |
| - | - | GND | 9 | 19 | GND | - | - |
| - | - | GND | 10 | 20 | CPLD_RESET_N | In | active-low |

#### J7/J8 - front-bottom-left / rear-bottom-left (10-pin 2x5, same symmetric mapping)

| Note (R1) | Direction (R1) | Signal (R1) | Pin (R1) | Pin (R2) | Signal (R2) | Direction (R2) | Note (R2) |
| - | - | 3V3_ENIG | 1 | 6 | 3V3_ENIG | - | - |
| - | - | GND | 2 | 7 | GND | - | - |
| - | - | GND | 3 | 8 | GND | - | - |
| - | - | GND | 4 | 9 | GND | - | - |
| - | - | 3V3_ENIG | 5 | 10 | 3V3_ENIG | - | - |

---

### 2026-06-01 — Session consolidation: diagrams, ENC connector ownership, and Lightboard LED strategy (Entry 12)

1. **Diagram updates completed in this session**
   - Architecture and portrait pages were corrected and aligned to the discussion intent.
   - Portrait page now shows two mini-stacks.
   - Legend added on both pages.
   - Bird's-eye convention now explicit in diagram legends: **top = rear, bottom = front**; green markers = bottom-edge power connectors.

2. **ENC module connector ownership clarified**
   - The "Cypher backplane ENC module mount connector" is the same **Hirose-style BtB interface family** used for ENC-module attachment to Input-Cypher and Output-Cypher.
   - The **ENC module owns the interface family definition**; carrier boards (Input-Cypher, Output-Cypher, Cypher backplane) use the relevant mating connectors.
   - This collapses prior duplicate sourcing lines into one connector-family decision plus board-specific mating part selection.

3. **Lightboard LED electrical intent clarified**
   - LEDs are on **Lightboard (Output-Cypher)**, not on ENC.
   - Driving intent: ENC output lines are active-low; each LED uses a series current-limit resistor to 3V3.
   - No dedicated LED driver IC is currently planned for the baseline on/off implementation.
   - Future option captured: discuss potential RGB upgrade to support GUI-configurable colour themes.

---

### 2026-06-01 — Connector-family scoping + hot-swap decision close (Entry 13)

1. **Connector family scope corrected**
   - **Hirose-style BtB is ENC-only**: used for ENC module interfaces.
   - **Samtec-style family covers both stacking and Cypher chaining**: Stack-Input/Stack-Output
     stacking connectors and Input-Cypher/Output-Cypher interconnect chaining connectors are
     the same Samtec-style family directionally.

2. **Hot-swap sockets decision closed**
   - Input-Cypher keyboard hot-swap sockets are **not required**.
   - Rationale: keyboard switch parts are inexpensive enough to replace directly if damaged.

---

### 2026-06-02 — Unified Samtec QSS/QTS connector topology proposal (Entry 14)

**Proposal:** Consolidate the current multi-connector stacking topology (Entry 11: J1/J2/J3/J4/J5/J6/J7/J8) into
a unified two-connector-per-board approach using Samtec's dual-row 0.635 mm QSS/QTS family. For this family,
`-025` means **25 positions per row / 50 total contacts**.

#### Rationale

1. **Higher-density consolidation**: One `-025` connector can absorb each existing top+bottom side pair on a
   stack board, reducing four connector positions per board to two while preserving dual-row routing flexibility.
2. **Mechanical alignment features**: The selected QSS/QTS families include locating/mechanical features that
   simplify mating alignment during assembly.
3. **Measured power / SI data exists**: Local Samtec reports now exist for current-carrying capacity, mating life,
   impedance, and 5 mm stack-height performance, so the proposal can be evaluated against real data rather than
   assumed capability.
4. **Known capacity margin**: Based on Entry 11 pin counts, a Stack-Input board would consume **92/100 contacts
   total** across its front+rear `-025` pair (46 front + 46 rear), leaving **8 spare**. A Stack-Output board would
   consume **68/100 contacts total** (34 front + 34 rear), leaving **32 spare**.

#### Proposed Connector Family

##### Stack-board family candidates

- **RA family for edge-to-edge stacking**: `QSS-025-...-D-RA...` / `QTS-025-...-D-RA...`
- **Vertical family for low-profile internal stacking**: `QSS-025-...-D-A...` / `QTS-025-...-D-A...`
- **Imported library candidates in this session**:
  - `QSS-025-01-L-D-RA-K` / `QTS-025-01-L-D-RA-P`
  - `QSS-025-01-L-D-A-GP-K` / `QTS-025-01-L-D-A-GP-K-TR`

##### Stack-Input and Stack-Output stacking topology

- **Front side** (right edge for Stack-Input, left edge for Stack-Output): one `-025` **male**
  connector facing Cypher / previous mini-stack
- **Rear side** (left edge for Stack-Input, right edge for Stack-Output): one `-025` **female**
  connector facing next mini-stack / blanking board
- **Cypher Board stacking interfaces**: mating `-025` female receptacles on STA-side and
  REF-side

##### Pin-budget summary from Entry 11

- **Stack-Input front**: J1 (26) + J5 (20) = **46 contacts used**
- **Stack-Input rear**: J2 (26) + J6 (20) = **46 contacts used**
- **Stack-Output front**: J3 (24) + J7 (10) = **34 contacts used**
- **Stack-Output rear**: J4 (24) + J8 (10) = **34 contacts used**

#### Input-Cypher and Output-Cypher Interconnect Refinement

- **Proposal:** Use the same QSS/QTS family in the `-025` size for Input-Cypher / Output-Cypher chaining and Cypher mating, i.e. **50 total contacts per connector**.
- **RA family candidates**: `QSS-025-01-L-D-RA-K` / `QTS-025-01-L-D-RA-P`
- **Vertical family candidates**: `QSS-025-01-L-D-A-GP-K` / `QTS-025-01-L-D-A-GP-K-TR`
- **Imported library candidates in this session**:
  - `QSS-025-01-L-D-RA-K` / `QTS-025-01-L-D-RA-P`
  - `QSS-025-01-L-D-A-GP-K` / `QTS-025-01-L-D-A-GP-K-TR`

##### Allocation intent

- One row can be biased toward keyboard / control signals
- One row can be biased toward lightboard / status signals
- Shared contacts remain available for `3V3_ENIG`, `GND`, and any required TTD/JTAG/control
  lines

#### Outstanding Questions / TBD

1. **Slot-by-slot assignment**: ✅ **COMPLETED** — Full pin mappings defined for J1 (90-pin, zig-zag GND spread), J2 (24-pin, full zig-zag), and J3 (10-pin power).
2. **Power-budget fit**: ✅ **COMPLETED** — Power-budget calculations added and verified.
3. **RA stack-height interpretation**: ✅ **COMPLETED** — Components selected; mechanical models deferred to PCB layout phase.
4. **Exact suffix lock-in**: ✅ **COMPLETED** — All 4 Samtec connector suffixes confirmed and sourced:
   - QSS-025-01-L-D-**RA-K** (female, right-angle, with guide-post)
   - QTS-025-01-L-D-**RA-P** (male, right-angle, tape-reel)
   - QSS-025-01-L-D-**A-GP-K** (female, vertical, with guide-post)
   - QTS-025-01-L-D-**A-GP-K-TR** (male, vertical, with guide-post, tape-reel)
5. **Blanking Board topology**: ✅ **COMPLETED** — Blanking board (rear of machine) uses Row 4 vertical
   male connectors (`QTS-025-01-L-D-A-GP-K-TR`) on its front face to mate with the rear face of the last mini-stack.
6. **ENC Hirose-style connector**: ✅ **COMPLETED** — All 6 DF40C variants (10/24/90-pin, DP/DS) sourced, imported, and KiCAD-verified.

#### Next Steps

- Refine the Entry 11 mapping into explicit `-025` contact assignments
- Compare real rail currents against the Samtec current-carrying data
- Confirm which RA mated-view dimension is the true board-to-board spacing
- Lock the exact QSS/QTS suffixes once sourcing preference is known

---

### 2026-06-02 — Samtec datasheet extraction and library import validation (Entry 15)

1. **Library import completed for the candidate Samtec family**
   - 10 Samtec PDFs were converted to local markdown under `design/Datasheets/`.
   - 12 Samtec symbols were added to `SamacSys_Parts.lib` and `SamacSys_Parts.kicad_sym`.
   - 12 Samtec footprints were added to `SamacSys_Parts.pretty/` and backported into `SamacSys_Parts.mod`.
   - 12 Samtec STEP models were added to both `SamacSys_Parts.3dshapes/` and `3D_Models/`.

2. **Validated electrical / mechanical figures from the local Samtec sources**
   - **Current rating (product spec headline):** `1.3 A/contact`
   - **Voltage rating:** `275 VAC`
   - **Withstanding voltage:** `825 VAC`
   - **Operating temperature:** `-55 °C to +125 °C`
   - **Contact resistance (LLCR):** `Δ15 mΩ max`
   - **Durability / mating life:** `100 cycles` for `10 µin Au`, `500 cycles` for `30 µin Au`
   - **Impedance target:** `50 Ω single-ended`, `100 Ω differential`
   - **5 mm vertical stack SI report:** `9.0 GHz / 18 Gbps` single-ended, `8.5 GHz / 17 Gbps` differential

3. **RA current-carrying data now exists for the edge-stack option**
   - Conservative reading from the RA power report:
   - `2.0 A/contact` with 2 contacts powered
   - `1.7 A/contact` with 4 contacts powered
   - `1.3 A/contact` with 6 contacts powered (preferred conservative value; report text also shows
     1.4 A later)
   - `1.2 A/contact` with 8 contacts powered
   - `0.5 A/contact` with all contacts powered
   - Ground-plane current in the same report ranges from **15.7 A** (1 ground plane powered) down to
    **9.5 A** (4 ground planes powered).

4. **Stack-height findings**
   - The vertical family explicitly documents a **5.00 mm mated height**.
   - The RA mated-view document exposes **8.53 mm** and **9.63 mm** dimensions for some QSS/QTS
     combinations, but that source still needs figure-label confirmation before treating those
     numbers as final board-to-board spacing.

5. **Resolved vs still open from Entry 14**
   - **Resolved / materially improved:** connector family shortlist, library availability, contact-count
     interpretation, mating-life data, voltage rating, contact resistance, baseline current-carrying data,
     and 5 mm vertical performance data.
   - **Still open:** exact suffix selection, final contact-by-contact allocation, full board power-budget
     check, and unambiguous RA board-spacing confirmation.

---

### 2026-06-02 — ENC module connector topology defined (Entry 16)

Design decisions for the ENC module's Hirose-style BtB connector interface. Three connectors per ENC module
interface, covering signal group naming, GND strategy, JTAG ordering, and ENC_ACTIVE_N bidirectionality.

#### Signal group naming rationale

- **plain-bits** — the 64-signal group representing the unencrypted rotor cipher lines entering/leaving the
  ENC module. Not named "encode" or "decode" because the ENC board's functional role depends on where it is
  physically mounted and how its CPLD is programmed. The orientation-neutral name avoids incorrect assumptions
  when the same ENC module is used in a keyboard (encoder) or lightboard (decoder) role.
- **cypher-bits** — the 6-signal group on the other side of the encoder. Also orientation-neutral.

#### Three-connector topology

| Designator | Pin count | Content | Placement on ENC module |
| --- | --- | --- | --- |
| J1 | 90-pin (2×45) | plain-bits\[63:0\] (64 signals) + GND (26), zig-zag distributed | Left edge |
| J2 | 24-pin (2×12) | cypher-bits\[5:0\] (6) + JTAG (TCK, RST\_N, TMS, TDI, TDO = 5) + ENC\_ACTIVE\_N (1) + GND (12) — all fully zig-zagged | Bottom-right corner |
| J3 | 10-pin (2×5) | 3V3\_ENIG (5) + GND (5) — power only | Top-right corner |

All three pin counts (10, 24, 90) are confirmed available in the Hirose connector product catalogue (available
counts confirmed by user: 10, 12, 20, 24, 30, 34, 40, 44, 50, 60, 70, 80, 90, 100, 120). Exact Hirose family,
pitch, stack height, and MPNs are TBD — user to provide from product number document.

#### J1 — 90-pin plain-bits connector

- 2 rows × 45 positions = 90 total pins
- 64 plain-bit signal pins + 26 GND pins
- 90-pin was chosen over 80-pin (which would carry only 16 GND alongside 64 signals) to provide 26 GND pins
  and a tighter zig-zag pattern
- **GND strategy — zig-zag between rows:** GND pins alternate between row 1 and row 2 at each GND position
  rather than forming solid GND "walls" at fixed column intervals. Rationale: zig-zagging keeps the ground
  return path closer to every signal trace regardless of which row it sits in, reducing worst-case ground loop
  area and inductive coupling between adjacent signal pairs.
- Pin assignments use internal column notation (C01–C45, Row A / Row B) pending Hirose physical pin numbering
  at layout phase. PB = plain-bits; PB\[0\] is assigned leftmost (LSB convention).
- **Zig-zag rule:** GND is assigned to Row A at the 1st, 3rd, 5th … GND occurrence left-to-right; Row B at
  the 2nd, 4th, 6th … GND occurrence. GND distribution uses a Bresenham-spread of 26 GND across 45 columns
  (≈ 1 GND column per 1.73 columns; maximum signal-only gap = 1 column between any two GND columns).

| Col | Row A | Row B |
| --- | --- | --- |
| C01 | PB\[0\] | PB\[1\] |
| C02 | GND | PB\[2\] |
| C03 | PB\[3\] | GND |
| C04 | PB\[4\] | PB\[5\] |
| C05 | GND | PB\[6\] |
| C06 | PB\[7\] | PB\[8\] |
| C07 | PB\[9\] | GND |
| C08 | PB\[10\] | PB\[11\] |
| C09 | GND | PB\[12\] |
| C10 | PB\[13\] | GND |
| C11 | PB\[14\] | PB\[15\] |
| C12 | GND | PB\[16\] |
| C13 | PB\[17\] | PB\[18\] |
| C14 | PB\[19\] | GND |
| C15 | PB\[20\] | PB\[21\] |
| C16 | GND | PB\[22\] |
| C17 | PB\[23\] | GND |
| C18 | PB\[24\] | PB\[25\] |
| C19 | GND | PB\[26\] |
| C20 | PB\[27\] | PB\[28\] |
| C21 | PB\[29\] | GND |
| C22 | GND | PB\[30\] |
| C23 | PB\[31\] | PB\[32\] |
| C24 | PB\[33\] | GND |
| C25 | PB\[34\] | PB\[35\] |
| C26 | GND | PB\[36\] |
| C27 | PB\[37\] | PB\[38\] |
| C28 | PB\[39\] | GND |
| C29 | GND | PB\[40\] |
| C30 | PB\[41\] | PB\[42\] |
| C31 | PB\[43\] | GND |
| C32 | PB\[44\] | PB\[45\] |
| C33 | GND | PB\[46\] |
| C34 | PB\[47\] | PB\[48\] |
| C35 | PB\[49\] | GND |
| C36 | GND | PB\[50\] |
| C37 | PB\[51\] | PB\[52\] |
| C38 | PB\[53\] | GND |
| C39 | PB\[54\] | PB\[55\] |
| C40 | GND | PB\[56\] |
| C41 | PB\[57\] | PB\[58\] |
| C42 | PB\[59\] | GND |
| C43 | GND | PB\[60\] |
| C44 | PB\[61\] | PB\[62\] |
| C45 | PB\[63\] | GND |

#### J2 — 24-pin cypher-bits + JTAG connector

- 2 rows × 12 positions = 24 total pins
- 12 signal pins + 12 GND pins
- **GND strategy — full zig-zag:** every signal pin in one row is paired with a GND pin in the other row at
  the same column position — no two signal pins share the same column across rows. Each signal is flanked by
  GND at adjacent columns on both sides (or board edge).
- **JTAG signal order** (left to right across the connector): TCK, RST\_N, TMS, TDI, TDO
  - RST\_N in this context is CPLD\_RESET\_N, which also serves the JTAG reset function
- Signal breakdown: cypher-bits\[5:0\] (6) + TCK (1) + RST\_N / CPLD\_RESET\_N (1) + TMS (1) + TDI (1) +
  TDO (1) + ENC\_ACTIVE\_N (1) = **12 signals**
- Pin assignments use internal column notation (C01–C12, Row A / Row B) pending Hirose physical pin numbering
  at layout phase. CB = cypher-bits.
- **Zig-zag rule (full):** every column has exactly one signal and one GND. Odd columns: signal in Row A, GND
  in Row B. Even columns: GND in Row A, signal in Row B. Signal order left-to-right: CB\[0:5\], then JTAG
  (TCK, RST\_N, TMS, TDI, TDO), then ENC\_ACTIVE\_N.

| Col | Row A | Row B |
| --- | --- | --- |
| C01 | CB\[0\] | GND |
| C02 | GND | CB\[1\] |
| C03 | CB\[2\] | GND |
| C04 | GND | CB\[3\] |
| C05 | CB\[4\] | GND |
| C06 | GND | CB\[5\] |
| C07 | TCK | GND |
| C08 | GND | RST\_N |
| C09 | TMS | GND |
| C10 | GND | TDI |
| C11 | TDO | GND |
| C12 | GND | ENC\_ACTIVE\_N |

#### J3 — 10-pin power connector

- 2 rows × 5 positions = 10 total pins
- 5× 3V3\_ENIG + 5× GND — power only, no signal lines
- Located at top-right corner of ENC module to minimise power rail impedance from board edge entry point
- Row A carries all 3V3\_ENIG pins; Row B carries all GND pins (solid rows, no zig-zag — power connector only).

| Col | Row A | Row B |
| --- | --- | --- |
| C01 | 3V3\_ENIG | GND |
| C02 | 3V3\_ENIG | GND |
| C03 | 3V3\_ENIG | GND |
| C04 | 3V3\_ENIG | GND |
| C05 | 3V3\_ENIG | GND |

#### ENC_ACTIVE_N — bidirectionality

- Direction is **not specified** on the connector definition — determined at CPLD programming time:
  - **Encoder (keyboard) role:** CPLD drives ENC\_ACTIVE\_N (output from ENC module, active-low keypress notification)
  - **Decoder (lightboard / other) role:** CPLD receives ENC\_ACTIVE\_N (input to ENC module, driven externally by the system)
- ENC\_ACTIVE\_N is very likely HIGH (inactive) during any JTAG communication, except possibly boundary-scan for rotor positional encoders (which is irrelevant to the ENC connector interface).
- CPLD\_RESET\_N is always HIGH during JTAG communication.

---

### 2026-06-04 — Keyboard LED Drive Circuit Defined (Entry 17)

#### LED Specification Summary (APFA2507Y2G2C-C2)

Source: `design/Datasheets/Kingbright-APFA2507Y2G2C_C2-datasheet.md`

| Parameter | Yellow | Green |
| --- | --- | --- |
| Package | 2.5 × 1.0 × 0.7 mm RA SMD | same |
| Pin 1 | K\_Y (Cathode Yellow) | — |
| Pin 2 | A\_Y (Anode Yellow) | — |
| Pin 3 | A\_G (Anode Green) | — |
| Pin 4 | K\_G (Cathode Green) | — |
| V\_F typ @ 20 mA | 2.0 V | 2.1 V |
| I\_F max | 30 mA | 30 mA |
| Circuits | Fully independent — no shared anode or cathode | |

26 LEDs per Input-Cypher Board, one per keyboard key.

---

#### Current-Limiting Resistor Calculation

Supply rail: **3V3\_ENIG = 3.3 V**
Target drive current: **10 mA** (conservative; max rated 30 mA, provides adequate brightness with good margin)

```text
R_yellow = (V_supply − V_F_yellow) / I_target
         = (3.3 − 2.0) / 0.010
         = 1.3 / 0.010
         = 130 Ω   (E24 standard value — exact, no rounding required)
         P = I² × R = (0.010)² × 130 = 13 mW  →  0402 adequate (limit: ~62 mW)

R_green  = (V_supply − V_F_green)  / I_target
         = (3.3 − 2.1) / 0.010
         = 1.2 / 0.010
         = 120 Ω   (E24 standard value — exact, no rounding required)
         P = I² × R = (0.010)² × 120 = 12 mW  →  0402 adequate
```

Quantities: **26× 130 Ω** and **26× 120 Ω** per Input-Cypher Board.
Each LED has its own series resistor (cathode side, LED → resistor → GND) to ensure independent current limiting.

---

#### LED Behaviour

| Condition | Yellow LED | Green LED |
| --- | --- | --- |
| Shift key NOT held | ON (PWM — brightness set by dial) | OFF |
| Shift key held | OFF | ON (PWM — brightness set by dial) |

Behaviour is mutually exclusive: at any instant exactly one colour is active per key.
Both Shift keys (left and right) trigger the same switch — either one activates Green.

---

#### Drive Topology — P-Channel MOSFET High-Side Switching

Each colour bank (26 parallel LEDs) is switched at the **anode side** by a dedicated P-channel MOSFET in SOT-23 package.

- Gate driven **active-LOW**: CPLD outputs LOW → MOSFET ON → LEDs light.
- CPLD outputs HIGH (or releases to internal pull-up) → MOSFET OFF → LEDs dark.
- MAX II internal weak pull-ups hold gate HIGH during power-up before CPLD user mode is active → both MOSFETs remain OFF → LEDs stay dark at startup (confirmed: MAX II Handbook §4).
- No external pull-down resistors required.
- No external gate resistors required at these switching frequencies (~100–300 Hz).
- Eliminates 74HC08 quad AND-gate ICs from the BOM.

**Minimum MOSFET ratings:**

| Parameter | Requirement |
| --- | --- |
| I\_D continuous | ≥ 300 mA (26 × 10 mA = 260 mA + margin) |
| \|V\_GS(th)\| | Must switch fully ON at V\_GS = −3.3 V |
| Package | SOT-23 |

**Circuit topology (per colour — Yellow shown; Green identical with 120 Ω):**

```text
   3V3_ENIG ─────────────────────── Source
                                       │
                              [P-channel MOSFET Q1]
                                       │ Drain
   YELLOW_DRIVE_N ──► Gate             │
   (CPLD output)                       │
                              ─────────┼──────────── ... (common anode bus, ×26)
                              │        │           │
                           [LED1]   [LED2]  ... [LED26]
                          Pin2→Pin1 Pin2→Pin1     Pin2→Pin1
                              │        │           │
                           [130 Ω] [130 Ω]  ... [130 Ω]
                              │        │           │
                             GND      GND         GND
```

---

#### Brightness Control — 555 Astable Oscillator + Hardware Dial

Brightness is controlled by a **rotary dial (panel-mount potentiometer)** fitted on the Input-Cypher Board PCB.
This feeds a **555 astable oscillator** whose output connects to a **CPLD GCLK pin**
(a dedicated clock input, separate from the 76 user I/O budget — MAX II Handbook §2).

**555 astable component values:**

| Ref | Component | Value | Notes |
| --- | --- | --- | --- |
| R\_A | Rotary pot | 0 – 50 kΩ | Hardware brightness dial |
| R\_B | Fixed resistor 0402 | 1 kΩ | Discharge path limiter; prevents short when R\_A → 0 |
| C | Timing capacitor | 10 nF | Sets oscillation period with R\_A + R\_B |
| C\_CV | Noise-bypass capacitor | 100 nF | 555 Pin 5 (CV) to GND; suppresses supply noise on duty cycle |

**Frequency range:**

```text
f_high ≈ 1.44 / ((R_A_min + 2 × R_B) × C)
       = 1.44 / ((0 + 2 × 1000) × 10×10⁻⁹)
       = 1.44 / 20×10⁻⁶
       ≈ 72 kHz  (theoretical minimum R_A; practical pot wiper contact limits this)

f_low  ≈ 1.44 / ((R_A_max + 2 × R_B) × C)
       = 1.44 / ((50000 + 2000) × 10×10⁻⁹)
       = 1.44 / 520×10⁻⁶
       ≈ 2.8 Hz  (very dim glow at dial minimum)
```

> **Note:** The 555 astable never produces zero duty cycle; at pot minimum the LEDs produce a very dim glow.
> This is intentional — it indicates the system is powered and active.
> Full-off behaviour can be implemented in CPLD logic in a future update if required.

**555 oscillator circuit:**

```text
   3V3_ENIG
       │
       ├──[R_A 0–50 kΩ pot]──┬──[R_B 1 kΩ]──┬── Pin 7 (DISCHARGE)
       │                     │              │
       │                  (wiper)           └── Pin 6 (THRESHOLD)
       │                     │                       │
       │                     └─────── Pin 2 (TRIGGER)│
       │                                         [C 10 nF]
       │                                             │
       │   Pin 8 (VCC)    ── 3V3_ENIG               GND
       │   Pin 4 (RESET)  ── 3V3_ENIG (tie HIGH — always running)
       │   Pin 1 (GND)    ── GND
       │   Pin 5 (CV)     ──[100 nF]── GND  (noise bypass)
       │
       └── Pin 3 (OUTPUT) ──────────────────────────────────► CPLD GCLK0
```

---

#### CPLD GCLK Routing

- The 555 output connects directly to GCLK0 on the EPM570T100 CPLD.
- GCLK pins are **dedicated clock inputs** separate from the 76 user I/O pins (MAX II Handbook §2, Table 1-3).
- BRIGHTNESS\_PWM via GCLK0 consumes **zero user I/O budget**.
- Inside the CPLD, GCLK0 is referenced as a clocking resource in the HDL architecture.

---

#### CPLD I/O Budget (EPM570T100, T100 package)

| Signal Group | Count |
| --- | --- |
| Plain-bit inputs PB\[0:63\] — keyboard keys (64 defined in ENC module image) | 64 |
| Cypher-bit inputs CB\[0:5\] | 6 |
| ENC\_ACTIVE\_N output | 1 |
| YELLOW\_DRIVE\_N output (new — this entry) | 1 |
| GREEN\_DRIVE\_N output (new — this entry) | 1 |
| **Total user I/O in use** | **73** |
| **Total user I/O available (EPM570T100)** | **76** |
| **Spare user I/O** | **3** |

> BRIGHTNESS\_PWM enters via GCLK0 — not counted in the 76 user I/O figure.
> Source: Intel MAX II Handbook Table 1-3 (EPM570T100: 76 user I/O pins).
>
> The two Shift key inputs (Pin\_SHIFT\_LEFT, Pin\_SHIFT\_RIGHT) are two of the 64 plain-bit positions; they are not additional pins.

---

#### J1 Hirose Connector — YELLOW\_DRIVE\_N and GREEN\_DRIVE\_N Routing

The 64 plain-bit positions PB\[0:63\] span the 90-pin J1 Hirose connector with GND interleaved.
Of these, PB\[0:25\] serve the 26 physical keyboard key inputs (including both Shift keys).
PB\[26\] and PB\[27\] are the next available plain-bit positions and are provisionally assigned as LED drive outputs:

| Signal | Provisional J1 Position | Hirose Column | Row |
| --- | --- | --- | --- |
| YELLOW\_DRIVE\_N | PB\[26\] | C19 | B |
| GREEN\_DRIVE\_N | PB\[27\] | C20 | A |

> These are provisional assignments pending Quartus pin-planning and PCB layout. Exact physical CPLD pin numbers from the EPM570T100 datasheet are confirmed at layout phase.

---

#### CPLD Internal Signal Path

```text
   Pin_SHIFT_LEFT  ──┬──[AND]──────────────────────────► SHIFT_ACTIVE_N
   Pin_SHIFT_RIGHT ──┘           │
                                 └──[NOT]────────────────► SHIFT_ACTIVE

   GCLK0 ──┬──────────────[AND]────[NOT]────────────────► GREEN_DRIVE_N
           │               (× SHIFT_ACTIVE)
           └──────────────[AND]────[NOT]────────────────► YELLOW_DRIVE_N
                           (× SHIFT_ACTIVE_N)
```

Both Shift key inputs feed an AND gate whose output is `SHIFT_ACTIVE_N`
(LOW when either key is depressed — active-LOW inputs mean any pressed key pulls its pin LOW).
`SHIFT_ACTIVE` is the logical inverse. Each LED drive output gates GCLK0 with the appropriate polarity of the shift signal.

---

#### CPLD HDL Pseudocode (Corrected)

```vhdl
-- Shift key inputs are active-LOW: LOW = key depressed, HIGH = released
-- SHIFT_ACTIVE_N is LOW when either Shift key is held (AND of two active-LOW signals)
SHIFT_ACTIVE_N <= Pin_SHIFT_LEFT AND Pin_SHIFT_RIGHT;  -- LOW when any Shift held
SHIFT_ACTIVE   <= NOT(SHIFT_ACTIVE_N);                 -- HIGH when any Shift held

-- LED drive outputs: P-MOSFET is active-LOW gate (CPLD LOW = MOSFET ON = LED lit)
-- GCLK0 = 555 PWM signal (100–300 Hz, variable duty cycle via brightness dial)
GREEN_DRIVE_N  <= NOT(GCLK0 AND SHIFT_ACTIVE);         -- Green: PWM when Shift held
YELLOW_DRIVE_N <= NOT(GCLK0 AND SHIFT_ACTIVE_N);       -- Yellow: PWM when Shift NOT held
```

**Why not `YELLOW_DRIVE_N <= NOT(GREEN_DRIVE_N)`?**
This would be logically wrong: it would tie Yellow to the inverse of Green's gate signal, losing Yellow's own PWM gating.
Yellow must have its own independent `GCLK0 AND SHIFT_ACTIVE_N` term to correctly apply the PWM when Shift is not held.

**Why `SHIFT_ACTIVE_N <= Pin_SHIFT_LEFT AND Pin_SHIFT_RIGHT` and not OR?**
Both inputs are active-LOW. The result should be LOW (active) when *either* key is pressed.
With active-LOW logic, AND of two active-LOW inputs produces LOW when any one is LOW —
this is De Morgan's equivalent of OR on active-HIGH signals. The expression is correct.

**Truth table:**

| Shift held? | Pin\_SHIFT\_{L/R} | SHIFT\_ACTIVE | SHIFT\_ACTIVE\_N | GREEN\_DRIVE\_N | YELLOW\_DRIVE\_N | Green LED | Yellow LED |
| --- | --- | --- | --- | --- | --- | --- | --- |
| No (both HIGH) | HIGH | 0 | 1 | HIGH (OFF) | NOT(GCLK0) = PWM | OFF | PWM ✓ |
| Yes (any LOW) | any LOW | 1 | 0 | NOT(GCLK0) = PWM | HIGH (OFF) | PWM ✓ | OFF |

At any instant, exactly one colour is active and PWM-modulated. The brightness dial sets the 555 duty cycle, which controls both colours equally (whichever is currently active).

### 2026-06-04 — Keyboard sourcing and import updates

User confirmed the following sourcing choices:

1. **Mechanical keyboard switches** — use **Cherry MX2A-71NB**; supplier details are
   **Mouser 540-MX2A-71NB**, **DigiKey 1644-MX2A-71NB-ND**, and **JLCPCB global
   sourcing / consignment**. Amazon is acceptable for prototyping.
2. **Hot-swap mounts** — revisit this after the first sourcing pass, as it may simplify manufacturing and improve end-user customisation.
3. **Lightboard LEDs** — reuse the same LED/current-limit approach as
   Input-Cypher. The BtB pin map should be revisited so **GREEN_ACTIVE_N** and
   **YELLOW_ACTIVE_N** can be carried across if the connector pin budget
   permits.
4. **Keyboard resistors** — defer sourcing of rows 15 and 16 until the LED pin count is finalised.
5. **Brightness potentiometer** — use **Bourns 3310P-001-503L** with supplier
   details **DigiKey 3310P-001-503L-ND**, **Mouser 652-3310P-001-503L**, and
   **JLCPCB C5891432**. Local markdown and KiCad assets were imported to the
   library.

---

### 2026-06-05 — Kailh PG151101S11 Hot-Swap Socket Design and Assembly Strategy (Entry 18)

User revisited the hot-swap socket decision (noted in Entry 11, item 2) and confirmed adoption of the **Kailh PG151101S11** mechanical switch hot-swap base for the Input-Cypher Board keyboard assembly:

**Design Rationale:**

1. **Manufacturing simplification** — Hot-swap sockets allow the
   **mechanical switches and keycaps to be installed after PCBA**, either
   by JLCPCB or by end-user post-purchase. This decouples switch sourcing
   from PCB assembly and reduces PCBA complexity.
2. **End-user customisation** — Modern mechanical keyboard enthusiasts expect hot-swap capability. Users can replace switches and keycaps without desoldering, enabling keyboard layout / switch type customisation.
3. **Underside mounting strategy** — all 40 Kailh sockets are placed on
   the **underside (rear) of the Input-Cypher Board PCB**. This maintains
   single-sided assembly for JLCPCB (only potentiometer + supporting
   components on the top/front side).

**PCB Layout Requirements:**

- **Placement:** All 40 × PG151101S11 sockets on the PCB rear layer, in a keyboard grid layout to match the keyboard's physical layout.
- **Routing:** Through-hole pads routed to front-layer schematic signals (switch input / debounce signals from CPLD).
- **Courtyard & clearance:** Standard keyboard socket spacing (~19.05 mm between centers for MX-style switches) to align with keycap and switch placement.
- **Keepout zones:** No components above rear-side sockets (mechanical clearance for switch stems and keycaps).

**Assembly and Sourcing Strategy:**

1. **JLCPCB PCBA service** — Kailh sockets are ordered as **JLCPCB consignment stock** (part **C41430893**) and included in the automated bottom-side (underside) assembly pass.
2. **Single-sided assembly maintained** — Front side (top) of
   Input-Cypher contains ENC module BtB connector, potentiometer, and
   supporting passives only. Rear side (bottom) is fully populated with
   sockets + decoupling capacitors.
3. **Mechanical switches and keycaps sourced separately** — Kailh
   switches and keycaps are **NOT part of the PCBA**. They are procured
   separately from suppliers (e.g., Amazon, mechanical keyboard retailers)
   and installed by JLCPCB post-PCBA OR by the end-user. This allows users
   to choose their preferred switch type and keycap aesthetic
   post-purchase.
4. **No hand-soldering for switches** — Kailh sockets snap into place with 0-force insertion; no manual soldering required after PCBA handoff.

**Component Import Status:**

- ✓ Symbol imported to `SamacSys_Parts.kicad_sym` (modern format)
- ✓ Symbol added to `SamacSys_Parts.lib` + `.dcm` (legacy format)
- ✓ Footprint `SW_PG151101S11.kicad_mod` in `SamacSys_Parts.pretty/`
- ✓ 3D model `PG151101S11.step` in `3D_Models/`
- ✓ Markdown datasheet generated from HanElectricity PDF

---

### 2026-06-05 — Cypher-owned Input/Output interconnect finalisation (Entry 19)

User completed the Cypher interconnect definition for the paired Input-Cypher and Output-Cypher boards.
This entry supersedes the earlier partial notes for this specific connector mapping topic.

#### Topology and ownership

1. **Connector ownership:** the interconnect is owned by the **Cypher board**.
2. **Connector family / orientation:**
   - **Cypher board** and **Plugboard** use the **vertical** Samtec variants.
   - **Input-Cypher** and **Output-Cypher** use the **right-angle** Samtec variants.
3. **Gender and edge convention (bird's-eye view):**
   - Cypher board and bottom edge of Input/Output-Cypher boards use **male plugs**.
   - Plugboard and top edge of Input/Output-Cypher boards use **female receptacles**.
4. Input-Cypher and Output-Cypher can be inserted in either order in the chain.

#### Electrical intent

1. `5V_MAIN` is not required on this interconnect for the currently defined Input/Output-Cypher functions; interconnect power is `3V3_ENIG` + `GND`.
2. The two PWM signals are inter-board only:
   - `GREEN_PWM_N`
   - `YELLOW_PWM_N`
   These are **NC on Cypher and Plugboard**.
3. JTAG path uses forward path on the top-row route and return path on the bottom-row route.
4. Include one board-role ID pin per row for top-position board identification:
   - Input-Cypher top connector: `ID_TOP=3V3_ENIG`, `ID_BOT=GND`
   - Output-Cypher top connector: `ID_TOP=GND`, `ID_BOT=3V3_ENIG`
   - Bottom connector on both boards: both ID pins are **NC**
5. `ENC_DATA[5:0]` is carried on both rows:
   - Top row carries Input-Cypher ENC output pass
   - Bottom row carries Output-Cypher ENC input pass
6. I2C passthrough is included as a single pair (`I2C_SCL_PASS`, `I2C_SDA_PASS`) for Plugboard-local expansion logic.
7. The central wedge/contact position is assigned as common high-current return (`GND_WEDGE`) on both rows.

#### Final pin-mapping table (approved)

| Top row signal | Top pin (symbol) | Bottom pin (symbol) | Bottom row signal |
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

`ENC_ACTIVE_INPUT_N` and `ENC_ACTIVE_OUTPUT_N` are intentionally distinct connector labels for schematic capture
net-separation on this interconnect while preserving the related functional signal context (`ENC_ACTIVE_N`).

#### Symbol numbering convention check (`-025`, dual-row)

The approved table aligns to the Samtec `-025` odd/even symbol numbering model:

- Top row column `Cn` maps to pin `2n-1`
- Bottom row column `Cn` maps to pin `2n`

So `C1 => pins 1/2`, `C13 => pins 25/26`, and `C25 => pins 49/50`.

---

### 2026-06-06 — Mini-stack signal-flow block tracker (Entry 20)

User requested a high-level flow-first tracker using `SIG-BLOCK-{ALPHA}` IDs, delaying final per-pin remapping
until this discussion is merged with the other active discussion threads.

#### Scope and rules captured in this entry

1. Data and control signals discussed here are treated as **active-low**.
2. Existing board-level electrical implementation (buffers/terminations) remains as currently defined in design;
   this entry tracks flow/grouping only.
3. The central wedge pin assignment (`GND_WEDGE`) remains reserved for common return current.
4. Final pin-map locking is deferred; this table is the working cross-board block reference.
5. Termination networks for tapped lines are expected to be fitted (no new DNF/DNI variants introduced by this
   entry).
6. Board implementation baseline for this architecture: all boards are minimum 4-layer with GND pour on top and
   bottom layers for shielding/EMI-EMC control.

#### Mini-stack internal return-link implementation direction (updated)

1. Preferred direction is now a **passive mini-stack base board** instead of a flexible ribbon cable.
2. The electrical role is unchanged: this is a passive interposer link between Stack-Output and Stack-Input
   signal blocks inside each mini-stack.
3. Connector style remains shrouded IDC-header family (board-mounted header style), but implemented as rigid
   PCB-to-PCB joins through the passive base board.
4. Orientation/mechanical intent for assembly:
   - Stack-Input bottom edge: right-angle female connector
   - Passive base board (Stack-Input side): male header mating to Stack-Input female
   - Passive base board (Stack-Output side): right-angle female connector
   - Stack-Output bottom edge: male header mating to passive base-board female
5. This approach is intended to improve signal shielding and make the mini-stack assembly mechanically rigid while
   preserving the established signal-flow model.

#### Required signal groups on the Stack-Output <-> Stack-Input passive base-board link

1. `SIG-BLOCK-A`: `ENC_DATA[5:0]` (forward mini-stack pass handoff)
2. `SIG-BLOCK-D`: `ENC_DATA[5:0]` (return-direction mini-stack handoff)
3. `SIG-BLOCK-E` local chain handoff: `TTD`
4. Interleaved and edge-guard `GND` around these data/control lines for shielding/return-path quality.
5. No new power-rail requirement is introduced on this passive base-board link by this entry.

#### Passive base-board connector ownership and mapping (locked)

1. Ownership of the Stack-Output <-> Stack-Input internal-link pin mapping is assigned to the **passive base board**.
2. Mating connectors on Stack-Input and Stack-Output must conform to this base-board-defined mapping.
3. Base-board connector pair is defined as a dual-row IDC style, **26 pins total (2x13)**, odd/even numbering.
4. The same pin map applies to both base-board connectors (Stack-Input side and Stack-Output side), with
   pin-to-pin passive continuity through the base board (`n -> n`).

#### Base-board 2x13 connector pin map (applies to both base-board connectors)

| Top row signal | Top pin (odd) | Bottom pin (even) | Bottom row signal |
| --- | ---: | ---: | --- |
| SIG_BLOCK_A_ENC_DATA[0] | 1 | 2 | GND |
| GND | 3 | 4 | SIG_BLOCK_A_ENC_DATA[1] |
| SIG_BLOCK_A_ENC_DATA[2] | 5 | 6 | GND |
| GND | 7 | 8 | SIG_BLOCK_A_ENC_DATA[3] |
| SIG_BLOCK_A_ENC_DATA[4] | 9 | 10 | GND |
| GND | 11 | 12 | SIG_BLOCK_A_ENC_DATA[5] |
| SIG_BLOCK_E_TTD | 13 | 14 | SIG_BLOCK_E_TTD |
| SIG_BLOCK_D_ENC_DATA[5] | 15 | 16 | GND |
| GND | 17 | 18 | SIG_BLOCK_D_ENC_DATA[4] |
| SIG_BLOCK_D_ENC_DATA[3] | 19 | 20 | GND |
| GND | 21 | 22 | SIG_BLOCK_D_ENC_DATA[2] |
| SIG_BLOCK_D_ENC_DATA[1] | 23 | 24 | GND |
| GND | 25 | 26 | SIG_BLOCK_D_ENC_DATA[0] |

#### Signal naming and chain conventions

1. `TTD` is the chain signal name used between devices to represent the serial data link from `TDO(prev)` to
   `TDI(next)`.
2. `TTD_RETURN` is used for the return leg from blanking/mini-stack return path back to the JTAG module.
3. JTAG module endpoint labels are usage-oriented at the module boundary:
   - module `TDI` pin launches outbound chain data toward the first device in chain order
   - module `TDO` pin receives `TTD_RETURN` from the end of the chain
4. JTAG protocol blocks require interleaved `GND` between all JTAG signal lines and guard `GND` on both sides
   of the protocol block.
5. `CPLD_RESET_N` is sourced from Cypher and follows the same distribution/tap/termination rules as `TCK` and
   `TMS` for CPLD `DEV_RST` reload control.

#### ENC_DATA flow description (captured from discussion)

1. `ENC_DATA[5:0]` is generated on **Input-Cypher** from keyboard state and sent to **Cypher**.
2. Cypher routes this data either through plugboard logic (when applicable) and onward to the first mini-stack
   via **Stack-Input front `SIG-BLOCK-A`**.
3. Within each mini-stack forward pass, data traverses rotors from right-to-left and exits at Stack-Output.
4. Stack-Output passively transfers this data over the passive base-board interposer link back to Stack-Input,
   which then forwards it via
   **Stack-Input rear `SIG-BLOCK-A`** to the next mini-stack (or to blanking board at chain end).
5. At chain end, blanking board passively bridges into **`SIG-BLOCK-B`**, after which data travels back toward
   Cypher through Stack-Output rear-to-front `SIG-BLOCK-B` passthrough on each mini-stack.
6. Cypher receives this on reflector side, performs reflector transform, then emits outbound data on
   **`SIG-BLOCK-C`** toward the mini-stack chain.
7. `SIG-BLOCK-C` is passively propagated through Stack-Output front-to-back, through blanking board, and into
   last Stack-Input handoff for **`SIG-BLOCK-D`**.
8. `SIG-BLOCK-D` is then sent via the passive base-board interposer link to corresponding Stack-Output path to
   begin rotor return traversal
   (left-to-right), ultimately re-entering Stack-Input front and propagating back toward Cypher.
9. After optional Cypher-side plugboard processing, final output data is sent to Output-Cypher LED outputs.

#### JTAG flow description (captured from discussion)

1. Outbound chain starts at JTAG module (`TDI` pin as source) and is carried as `TTD` with `TCK`, `TMS`, and
   `CPLD_RESET_N`
   through Cypher, Input-Cypher ENC, Output-Cypher ENC, plugboard pass 1 ENC in/out, plugboard pass 2 ENC
   in/out, then into mini-stacks via **`SIG-BLOCK-E`**.
2. For each mini-stack on `SIG-BLOCK-E`:
   - `TCK`, `TMS`, and `CPLD_RESET_N` are passed Stack-Input front->rear with local tap/distribution for that
     mini-stack
   - `TTD` is routed through rotors (device-to-device chain path)
   - at Stack-Output, `TTD` is carried over the passive base-board interposer link back to Stack-Input rear
     `SIG-BLOCK-E` to continue chain
3. `TCK`, `TMS`, and `CPLD_RESET_N` spoke terminations are implemented at Stack-Output boards and at blanking
   board (per existing design intent) to support tapped distribution rather than a pure 30-device serial route.
4. At blanking board, `TCK`, `TMS`, and `CPLD_RESET_N` terminate and outbound `TTD` is renamed **`TTD_RETURN`**
   and emitted on **`SIG-BLOCK-F`**.
5. `SIG-BLOCK-F` (`TTD_RETURN` + interleaved `GND`) is passed rear->front through all Stack-Output boards back
   to Cypher, then to JTAG module (`TDO` pin as sink).

#### Actuation flow description (captured from discussion)

1. Actuation trigger is sourced from Cypher and associated with Input-Cypher key activity (`ENC_ACTIVE_N`).
2. This trigger is tracked as **`SIG-BLOCK-G`** and is treated as its own signal block.
3. `SIG-BLOCK-G` is carried through Stack-Input front connector to Stack-Input rear connector as a pass-through
   distribution line across mini-stacks.
4. Each Stack-Input board takes a local tap from `SIG-BLOCK-G` to trigger its local servo PWM actuation control.
5. Cypher also forwards `SIG-BLOCK-G` (`ENC_ACTIVE_N`) to Output-Cypher as the global LED enable gate.
6. Output-Cypher LED behavior is active-low gated:
   - LED anode-side enable is controlled from `3V3_ENIG` via `ENC_ACTIVE_N` gating
   - LED cathode-side/select is controlled by the corresponding decoded output line
   - LED illuminates only when the decoded output is active (low) and `ENC_ACTIVE_N` is low
7. Rotor reciprocal actuation remains mechanical (Enigma-style); this signal only triggers stack-local actuation
   and Output-Cypher LED enable behavior.
8. `SIG-BLOCK-G` is terminated at the blanking board at end-of-chain.
9. `SIG-BLOCK-G` naming applies to the stacking/inter-stack distribution path. On the Input-Cypher/Output-Cypher
   interconnect (Entry 19), the split aliases `ENC_ACTIVE_INPUT_N` and `ENC_ACTIVE_OUTPUT_N` are used only to keep
   the two independent Cypher-interconnect signal sets separated in schematic capture. Cypher links these aliases to
   the common functional signal `ENC_ACTIVE_N`.

#### Power flow description (captured from discussion)

1. `SIG-BLOCK-H` = `5V_MAIN` distribution rail for Stack-Input actuation power.
2. `5V_MAIN` is provided to Stack-Input only (not Stack-Output) using multiple connector pins to satisfy
   aggregate current budget for up to 6 mini-stack servo actuation circuits.
3. `5V_MAIN` is passed front->rear across the Stack-Input chain; each Stack-Input takes a local draw and uses
   local bulk capacitance for servo actuation supply stability.
4. At blanking board, `SIG-BLOCK-H` pins are NC (no onward power distribution required past end-of-chain).
5. `SIG-BLOCK-I` = `3V3_ENIG` distribution rail for all boards in this chain context (Stack-Input, Stack-Output,
   blanking board, and rotor-side loads).
6. `3V3_ENIG` uses multiple connector pins across interfaces to meet full-system budget for up to 6 mini-stacks
   (30 rotors total) and associated logic/interface loads.
7. `3V3_ENIG` pin allocation intent is a distributed multi-pin "power cage" around connector signal groups to
   improve rail integrity and return proximity.

#### SIG-BLOCK mapping tracker (working; pin numbers deferred)

| SIG-BLOCK | Function | Signal group (provisional) | Flow summary | Must map consistently on |
| --- | --- | --- | --- | --- |
| `SIG-BLOCK-A` | ENC_DATA forward pass | `ENC_DATA[5:0]` | Input-Cypher -> Cypher -> Stack-Input front -> rotors (R->L) -> Stack-Output -> passive base-board interposer link -> Stack-Input rear -> next mini-stack rearward chain -> blanking board input | Stack-Input front/rear data block, Stack-Output interposer-side block, Passive base-board A-side block, Blanking board A-side block |
| `SIG-BLOCK-B` | ENC_DATA rear return-to-reflector side | `ENC_DATA[5:0]` | Blanking board bridges A->B at chain end, then Stack-Output rear -> Stack-Output front through each mini-stack back toward Cypher reflector side | Stack-Output rear/front B block on every mini-stack, Blanking board B-side block, Cypher reflector-side ingress block |
| `SIG-BLOCK-C` | ENC_DATA outbound from reflector side toward last mini-stack | `ENC_DATA[5:0]` | Cypher reflector output -> Stack-Output front -> Stack-Output rear through chain -> blanking board C path -> last Stack-Input D ingress | Stack-Output front/rear C block, Blanking board C routing block, last-stack handoff to D |
| `SIG-BLOCK-D` | ENC_DATA rotor return pass (machine return direction) | `ENC_DATA[5:0]` | Last Stack-Input receives from C/blanking side -> passive base-board interposer link to matching Stack-Output -> through rotors (L->R) -> Stack-Input front -> previous mini-stacks/Cypher -> optional plugboard -> Output-Cypher | Stack-Input/Stack-Output D handoff points, passive base-board D pairing, Stack-Input front D egress blocks |
| `SIG-BLOCK-E` | JTAG outbound chain into mini-stacks | `TCK`, `TMS`, `CPLD_RESET_N`, `TTD` + interleaved `GND` | JTAG Module (`TDI` pin used as outbound chain source) -> Cypher -> Input-Cypher ENC -> Output-Cypher ENC -> Plugboard ENC chain -> mini-stacks -> blanking board E input | All E blocks across Cypher/Input-Cypher/Output-Cypher/Plugboard/Stack-Input/Blanking with same line order and GND interleave rule |
| `SIG-BLOCK-F` | JTAG return chain to JTAG module | `TTD_RETURN` + interleaved `GND` | At blanking board: `TCK`/`TMS`/`CPLD_RESET_N` terminate, `TTD` is renamed `TTD_RETURN` -> Stack-Output rear -> Stack-Output front through all mini-stacks -> Cypher -> JTAG Module (`TDO` pin used as chain return sink) | Blanking F output, Stack-Output rear/front F blocks on all mini-stacks, Cypher return block to module |
| `SIG-BLOCK-G` | Actuation + LED-enable distribution | `ENC_ACTIVE_N` | Cypher -> Stack-Input front -> Stack-Input rear pass-through across mini-stacks with local Stack-Input actuation taps; Cypher also forwards ENC_ACTIVE_N to Output-Cypher as global LED enable gate; blanking board provides end termination | Stack-Input front/rear G block on every mini-stack, Cypher G egress/branch blocks, Output-Cypher G ingress block, Blanking board G termination block |
| `SIG-BLOCK-H` | Stack-Input actuation power distribution | `5V_MAIN` | Cypher -> Stack-Input front -> Stack-Input rear across mini-stack chain; local Stack-Input draw with bulk capacitance; blanking board H pins NC at chain end | Stack-Input front/rear H power blocks on every mini-stack, Cypher H source block, Blanking board H NC policy |
| `SIG-BLOCK-I` | Global logic/interface power distribution | `3V3_ENIG` | Multi-pin distribution across Stack-Input, Stack-Output, blanking board, and rotor-facing chain interfaces for full-system load support | All connector I power blocks across Cypher/Stack-Input/Stack-Output/Blanking with consistent multi-pin allocation strategy |

---

> *Add new discussion entries above this line. Mark questions as ✅ in the table below when answered.*

| # | Question | Status | Answer |
| --- | --- | --- | --- |
| 1 | What connectors/interface does the Cypher Board use for rotor mini-stack attachment? | ✅ Answered | Samtec 25-pin connectors (RA and vertical variants) fully selected and sourced. All supplier/manufacturer parts confirmed. |
| 2 | What is the physical form factor / dimensions of the Cypher Board? | ✅ Answered | Deferred by design: out of scope for this design-only discussion phase. Board dimensions and enclosure constraints will be set during schematic/PCB layout work. |
| 3 | How does the Stack-Input Board interface with the Cypher Board (connector type, pin count)? | ✅ Answered | Samtec 25-pin RA connectors fully confirmed and sourced. All supplier/manufacturer part numbers locked. |
| 4 | How does the Stack-Output Board interface with the Cypher Board (connector type, pin count)? | ✅ Answered | Samtec 25-pin RA connectors fully confirmed and sourced. All supplier/manufacturer part numbers locked. |
| 5 | How many Rotor boards sit between the Stack-Input and Stack-Output boards in a mini-stack? | ✅ Answered | **5 ROT boards per mini-stack.** Maximum 6 mini-stacks = 30 rotor positions total. |
| 6 | Does the ROT board form factor or connector change as a result of this restructuring? | ✅ Answered | No impact. ROT form factor/connector definition is unchanged for this discussion scope. |
| 7 | Does the AM-native integration on Stack-Input change the motor/actuator wiring to the machine body? | ✅ Answered | No. Servo and end-stop harness wiring remains exactly as before; AM placement change does not alter machine-body wiring definition. |
| 8 | Does the JTAG Module on the Cypher Board still connect to the same external FT232H/USB debug path? | ✅ Answered | Yes. JTAG Module remains a module and is relocated from CTL to Cypher Board without changing the external FT232H/USB debug path. |
| 9 | Does Link-Beta (CTL→Cypher Board) use the same connector and protocol as the current CTL→STA Link-Beta? | ✅ Answered | Standardised onto the Samtec 25-pin connector family. Full pin allocation confirmed in Entry 11. |
| 10 | Does Link-Alpha (PM→CTL) remain unchanged? | ✅ Answered | Yes. Link-Alpha is outside the cypher-stack change scope and remains unchanged. |
| 11 | Do ENC SW1–SW40 become obsolete? | ✅ Answered | Yes — confirmed obsolete. Buttons move to Input-Cypher Board as mechanical keyboard switches. |
| 12 | How many mini-stacks does the Cypher Board backplane support (i.e. how many rotor positions)? | ✅ Answered | Capacity is defined: minimum 1 mini-stack (5 ROT), maximum 6 mini-stacks (30 ROT). |
| 13 | Will DECs need to be raised for each board retirement / new board creation? | ✅ Answered | A consolidated DEC will be raised once this discussion is feature-complete, covering board retirements/replacements and any new boards distilled from this discussion. |
| 14 | Are there enclosure or panel-mount constraints that affect new board dimensions or connector placement? | ✅ Answered | No enclosure/panel constraints apply at this phase. Enclosure definition follows PCB layout completion, not the reverse. |
| 15 | What exact Hirose connector variant is used for ENC module attachment to Input-Cypher and Output-Cypher boards? | ✅ Answered | All 6 Hirose DF40C variants (10/24/90-pin, DP/DS) fully sourced and imported to KiCAD library. All supplier/manufacturer part numbers locked. |
| 16 | How many ENC modules does each of Input-Cypher and Output-Cypher support? | ✅ Answered | 1 ENC module per board (Input-Cypher: 1; Output-Cypher: 1). |
| 17 | What signals does the Input-Cypher Board carry between the ENC module and the Cypher Board? | ✅ Answered | Full J1/J2/J3 ENC-side mapping defined in Entry 16 with complete pin tables. Signal allocation to Samtec 2x25 connector confirmed in Entry 11. |
| 18 | What signals does the Output-Cypher Board carry between the ENC module and the Cypher Board? | ✅ Answered | Same ENC-side mapping as Input-Cypher defined in Entry 16. Signal allocation to Samtec 2x25 connector confirmed in Entry 11 with symmetry verified. |
| 19 | What is the BtB connector between Input-Cypher Board and Cypher Board (type, pin count, stack height)? | ✅ Answered | Samtec 25-pin RA connectors fully confirmed with pin allocation defined in Entry 11. |
| 20 | What is the BtB connector between Output-Cypher Board and Cypher Board (type, pin count, stack height)? | ✅ Answered | Samtec 25-pin RA connectors fully confirmed with pin allocation defined in Entry 11. |
| 21 | Does the Output-Cypher Board (lightboard) drive LEDs directly, or does it carry signals to LED drivers on the ENC module? | ✅ Answered | Lightboard (Output-Cypher) carries the LEDs directly. Baseline approach is active-low ENC outputs driving plain LEDs via series current-limit resistors tied to 3V3. No dedicated LED driver IC is planned for the baseline design. |
| 22 | Can the ENC CPLD (EPM570) debounce all 64 keyboard input lines within available logic cells? | ✅ Answered | **Yes — confirmed sufficient.** CPLD is EPM570T100I5N (570 LEs). Using the shared bank-level debounce architecture from `Encoder_Logic.md §5` (3 × 64-bit bank registers, shared stability counter, shared sample-tick divider — NOT 64 independent counters), estimated LE utilisation for the ENCODE image is ~394/570 LEs (~69%), leaving ~31% margin. **No hardware debounce circuitry is needed on Input-Cypher Board.** Pre-synthesis estimate; Quartus fit will give exact figures. |
| 23 | If CPLD debounce is insufficient for 64 lines, what debounce approach on Input-Cypher Board? (RC+Schmitt, dedicated IC, other?) | ✅ Answered | Not required — EPM570 capacity is sufficient (see Q22). |
| 24 | What connector mounts the ENC module on the back of the Cypher Board (type, pitch, stack height)? | ✅ Answered | All 6 Hirose DF40C variants fully sourced with complete supplier part numbers. KiCAD library fully updated. |
| 25 | What is the exact chaining connector and protocol between Input-Cypher and Output-Cypher boards? | ✅ Answered | 2 male Samtec-style connectors on bottom edge + 2 female on top edge of each board. Input-Cypher: consumes left male, right male passes through to right female, left female NC (except 3V3_ENIG + GND). Output-Cypher: consumes right male, left male passes through to left female, right female NC (except 3V3_ENIG + GND). Either board may be inserted first. This chaining connector family is the same Samtec-style family direction as Stack-Input/Stack-Output stacking connectors. Exact part TBD. |
| 26 | What mechanical keyboard switch type is required for Input-Cypher Board? (MX-compatible? actuation force, travel, hot-swap socket needed?) | ✅ Answered | MX-style mechanical push button (same as modern keyboards). Hot-swap sockets are not required (decision: No). Exact switch MPN and actuation specs remain TBD. |
| 27 | Will PCBWay be the confirmed prototype manufacturer for the Cypher Board given 6-layer + double-sided assembly? | ✅ Answered | Deferred until PCB layout phase. Current expectation is PCBWay for dual-side assembly capability; final manufacturer confirmation will be made at layout/release time. |
| 28 | What is the connector type for the keyed stacking connectors on Stack-Input/Stack-Output (type, pin count, pitch, keying mechanism)? | ✅ Answered | Samtec 25-pin connectors fully selected, sourced, and all supplier/manufacturer part numbers locked. |
| 29 | What signals/rails are on the stacking connectors vs what is on the ribbon cable IDC? | ✅ Answered | **Stacking connectors (front-top-right):** ENC_IN[5:0], ENC_OUT[5:0], TTD, TMS, TCK, CPLD_RESET_N. **(front-bottom-right):** 3V3_ENIG, 5V_MAIN, GND, ENC_ACTIVE_N. **(front-top-left):** TTD_RETURN + ENC_DATA return toward Cypher. **(front-bottom-left):** 3V3_ENIG + GND only. **Ribbon cable (IDC):** intra-mini-stack return path from Stack-Output to Stack-Input carrying ENC_DATA + TTD from the last ROT output. |
| 30 | What is the ribbon cable IDC connector specification? (pin count, pitch, IDC type, cable width) | ✅ Answered | IDC connector specification confirmed for Stack-Output → Stack-Input return path. Deferred alternative (rigid mini-stack base-board) to future design session if adopted. |
| 31 | Is the Stack-Blanking Board purely passive (shorting jumpers/terminations) or does it contain active components? | ✅ Answered | It is a signal-routing-only passive PCB (no active components), routing final mini-stack ENC_DATA into the Stack-Output return chain together with TTD_RETURN. |
| 32 | How many ROT boards are in a single mini-stack (between Stack-Input and Stack-Output)? | ✅ Answered | **5 ROT boards per mini-stack.** |
| 33 | How do the Cypher Board connections to Stack-Input and Stack-Output differ in connector type/pin count (they serve different signal sets)? | ✅ Answered | Current mappings fully defined in Entry 11. End-to-end signal-path validity review completed. All signal paths verified valid. |
| 34 | With AM native to each Stack-Input Board, what is the per-stack power budget for AM circuits (motor driver current, MCU current)? | ✅ Answered | Per-stack AM power budget is unchanged from the existing standalone AM: one servo on `5V_MAIN`, STM32G071 logic on `3V3_ENIG`, and `ACTUATE_REQUEST_N` is logic-only (`< 5 mA`). The AM dock already provides `1.5 A` on `5V_MAIN` and `0.6 A` on `3V3_ENIG`, so the moved-in-native AM remains comfortably within margin. |
| 35 | Is the AM MCU the same STM32G071 as currently used, or will the native integration allow a smaller/different MCU? | ✅ Answered | Same STM32G071 + motor driver as current AM board — identical circuits, made native to Stack-Input PCB. |
| 36 | What is the full signal assignment for Cypher Board ↔ Stack-Input and Cypher Board ↔ Stack-Output connections? | ✅ Answered | See 8-connector signal assignment table in Known Scope section and Discussion entry 2026-05-26. |
| 37 | What is the exact connector type and pitch for the stacking connectors (e.g. board-to-board, edge connector, pin header)? | ✅ Answered | This is now effectively covered by Q28 in this phase: board-to-board Samtec family and pitch are already set; only final purchasable part-number selection remains. No separate additional task is required. |
| 38 | Does 5V_MAIN pass through the stacking connectors from one mini-stack to the next, or does each mini-stack source its own 5V? | ✅ Answered | Both 3V3_ENIG and 5V_MAIN pass through Stack-Input: received on front-bottom-right, forwarded out rear-bottom-right to next mini-stack. |
| 39 | Is KEYPRESS_N the same signal as ENC_ACTIVE_N defined in `Encoder_Logic.md §4.5`? Or is it a distinct new signal? | ✅ Answered | Confirmed: the signal is **ENC_ACTIVE_N** — the debounced keypress signal from the ENC module. All prior references to KEYPRESS_N updated to ENC_ACTIVE_N. |
| 39a | User referenced the CPLD as "EPM540" — confirmed as EPM570T100I5N (570 LEs). User clarified they had confused the part with the smaller EPM240. | ✅ Answered | EPM570T100I5N confirmed. |
| 40 | How does TTD_RETURN propagate back through intermediate mini-stacks (not the last one)? At the last mini-stack the blanking board routes it — but in intermediate stacks, what carries TTD_RETURN from rear-top-left forward toward the Cypher Board? | ✅ Answered | **Every Stack-Output board** has a direct **rear-top-left → front-top-left** internal passthrough. The blanking board routes TTD_RETURN to the last mini-stack's Stack-Output rear-top-left, then it daisy-chains forward through each Stack-Output board (rear-top-left → front-top-left passthrough) back to the Cypher Board. No active logic needed on Stack-Output boards — purely a trace passthrough. |
| 41 | The blanking board must route TTD_RETURN from Stack-Input rear-top-right to Stack-Output rear-top-left — does this mean it is a routed PCB with traces (not just a shorting assembly)? What exactly does the blanking board contain? | ✅ Answered | Confirmed as a **basic pass-through PCB with routed traces** (not a shorting assembly). Contains routed PCB traces completing required signal connections between the 8 stacking connector positions at the end of the chain. Exact internal routing detail TBD. User has a future alternative idea deferred as `signal-trace-simplification-and-routing`. |
| 42 | Full per-pin signal assignment within each of the 8 connectors: which specific pins carry which signals? This drives the minimum pin count and Samtec part selection for each connector. | ✅ Answered | Final per-pin mapping is defined in **Entry 11** and is authoritative for J1-J8. Outstanding work is connector part selection/rating validation (Samtec part numbers and current rating), not signal assignment. |
| 43 | What signal does the rear-bottom-left connector (Stack-Output back, right edge) carry? | ✅ Answered | **3V3_ENIG + GND only** (same mapping family as J7/J8 per Entry 11). It does not carry ENC_DATA return. |
| 44 | `mini-stack-base-board` — alternative to the ribbon cable IDC for the Stack-Output → Stack-Input return path within each mini-stack. | ✅ Answered | Pass-through PCB using the same connector style as the current STA–CTL interface. Advantages: mechanically solidifies the mini-stack; better signal integrity than ribbon cable (ground-plane shielding top + bottom). **Not yet part of the current changeset** — user still in design brain-dump phase. To be revisited in a dedicated future session if adopted. |
| 45 | **ENC_DATA return chain:** confirm the return path location and any required power-connector upgrades. | ✅ Answered | ENC_DATA return is carried with TTD_RETURN on the rear-top-left/front-top-left chain (J4/J3 path) back toward Cypher. Front/rear-bottom-left (J7/J8) remains power-only (3V3_ENIG + GND). Authoritative pin-level details are in Entry 11. |
| 46 | **P-channel MOSFET selection for keyboard LED drive circuits.** Requirements: SOT-23 package; I\_D continuous ≥ 300 mA; \|V\_GS(th)\| reliably switched fully ON at V\_GS = −3.3 V; one device per LED colour bank (×2 per Input-Cypher Board). | ✅ Answered | **SQ2319ADS-T1\_BE3** (Vishay SOT-23) — confirmed from local datasheet: I\_D = −4.6 A continuous at 25 °C (≥ 300 mA ✓); V\_GS(th) max = −2.5 V, so V\_GS = −3.3 V provides −0.8 V worst-case overdrive — device enhances ✓. Full supplier details in BOM-Protected row 5. |

---

### 2026-06-04 — Next discussion order

User asked to keep the following discussion points separate from the main design todo list until they explicitly say to integrate the changes:

1. ✅ Review Cypher board interconnect connectors and pin mappings, including the new dimmer PWM signals for backlight LEDs. **Completed in Entry 19 (2026-06-05).**
2. ✅ Review pin mappings for the Mini-stack return IDC cable connector, including the discussion of replacing the ribbon cable with a PCB passive base-plate. **Completed in Entry 20 (2026-06-06), with passive base-board ownership and locked 2x13 mapping.**
3. Locate the remaining new parts, including the current-limiting resistors for the LEDs.

---

## Implementation Prerequisites (before any design file changes)

- [ ] All open questions above answered
- [ ] All new component MPNs confirmed with supplier part numbers
- [ ] KiCAD symbol, footprint, and 3D model available for each new component (imported to library)
- [ ] Review-pass-11 complete (no open CRITICAL or HIGH findings)
- [ ] Explicit user implementation approval given (SENARY DIRECTIVE)
- [ ] DEC entries drafted for any architectural changes

---

## Cross-references

- Todo: `extension-mechanical-usage` → `.copilot/todos/extension-mechanical-usage.md`
- Review gate: `review-clean-passes-gate` must be satisfied before design changes begin
- Library: `src/Electronics/Library/LIBRARY_NOTES.md` — any new components must be added here after import
