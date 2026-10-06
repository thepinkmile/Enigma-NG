# Cypher-Plugboard Board (V1.0) Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-10-05

## 1. Overview

The Cypher-Plugboard Board terminates the Cypher HID interconnect chain beneath whichever board (either
Cypher-Input or Cypher-Output, either order) occupies the bottom-most position of the local
2-board HID stack - mirroring the Stack-Blanking Board's end-of-chain role for the 30-rotor
mini-stack chain. This specification documents **three board variants** sharing an identical
electrical circuit (HID-chain termination, power passthrough); only the jack field's row count,
character layout, and jack quantity differ between them, mirroring the Cypher-Input/Cypher-Output
variant split. Variant-specific detail lives in a dedicated document per variant:

- `design/Electronics/Cypher-Plugboard/Cypher_Plugboard_26_Char_Design.md`
- `design/Electronics/Cypher-Plugboard/Cypher_Plugboard_64_Char_Design.md`
- `design/Electronics/Cypher-Plugboard/Cypher_Plugboard_10_Numeric_Design.md`

**Electrically, per DEC-088 and DEC-103, this board is deliberately simple:** it carries no
plugboard-signal-specific pins at all, no `BOARD_ROLE_ID` strap, and (since DEC-103 retargeted its
former JTAG connector to the User Settings Module) **no active components of its own at all** -
JTAG spoke termination now lives on the User Settings Module instead (see
`User_Settings_Module/Design_Spec.md §4`). **This board's PCB is a thin strip along the top edge
only** - just large enough to carry the two interconnect connectors (`J1`/`J2`). The physical
plugboard patch jacks are **not** mounted on this PCB at all - they mount directly to a **machined
metal enclosure** that this PCB strip attaches to, and are **not** electrically connected to this
board's own circuitry - each jack terminal is wired via a discrete jumper cable directly back to
the Cypher Board's own spade terminal bank (`J20+`, see `Cypher/Design_Spec.md §6`), bypassing
this board's own PCB and both interconnect connectors entirely. This board's only electrical role
is to provide `GND` continuity and a clean dead-end for every other signal reaching it on either
connector (including `3V3_ENIG`, which is received but left NC - nothing on this board consumes
it).

| Circuit Responsibility | Board Role | Key Component |
| :--- | :--- | :--- |
| **Cypher Left Pair Template mating** | Mates the bottom-most HID board's bottom (female) connector, per the shared Cypher Left Pair Template; GND stays fully populated for return-path continuity; every other signal received here (including `3V3_ENIG`/`5V_MAIN`) is left NC (no ENC module, no `BOARD_ROLE_ID` strap, nothing below this board to relay to) | J1 - Samtec QTS-025 family |
| **User Settings Module Hub mating** | Mates USM's own bottom Hub connector; GND stays fully populated for return-path continuity; every other signal received here (including `3V3_ENIG`) is left NC (JTAG/I2C termination and relay now live entirely on USM - see `User_Settings_Module/Design_Spec.md §4`) | J2 - Samtec QTS-025 family |
| **Plugboard jack field (mechanical only, chassis-mounted)** | Physical Switchcraft 12A 6.35mm (1/4") switched jack sockets, mounted directly to the machined metal enclosure (not this board's own PCB); wired via harness directly to the Cypher Board's own `J20+` spade bank, not through this board's own copper | J3+ (per variant - see each variant's own design file) |

**Mechanical construction:** unlike Cypher-Input/Cypher-Output (which are single PCBs mounting
horizontally, stacking vertically on top of the Cypher Board), this board is a **hybrid assembly**:
a small PCB strip (top edge only, carrying `J1`/`J2`) attached to a **machined metal
enclosure** that forms the rest of the assembly and hosts the entire jack field. The enclosure is
mounted in a **vertical orientation, like the Cypher Board itself** - so the jack field forms a
human-facing front panel with character rows running top-to-bottom, matching the ergonomics of a
traditional Enigma plugboard. Each "plug" position is **2 jack sockets** (one per plugboard pass)
placed **immediately next to each other, horizontally (left-to-right)** - not stacked vertically -
to keep the panel's overall height as small as possible. Rows are stacked vertically below one
another, with generous horizontal spacing between adjacent plug-pairs (for tidy patch-cable
routing) and generous vertical spacing between rows (so the corresponding character can be
engraved/printed on the metal enclosure face directly above each plug-pair - **not** a PCB
silkscreen, since the jack field is not on the PCB). **The PCB strip is identical across all
three variants** (fixed size, independent of jack count - it only ever carries `J1`/`J2`).
**The machined metal enclosure is sized per variant**, scaling in height with the row count (see
each variant's own design file); the 64-Character variant (the variant with the most rows) is the
tallest.

> **Chassis grounding rationale:** mounting the jacks directly to the machined metal enclosure
> means every jack's metal bushing bonds directly to that enclosure - keeping the entire external
> jack field on a continuous `GND_CHASSIS` network, consistent with the rest of the system's
> external connectors. Per `design/Standards/Global_Routing_Spec.md §5`, this board's own
> `GND_CHASSIS` net (enclosure + jack bushings) is **not** locally bonded to GND here - it
> dissipates through the system's single `GND_CHASSIS`-to-GND bond, which remains on the Power
> Module only (see §2 GND_CHASSIS Single-Point Bond, below). This is entirely separate from the
> signal-return `GND` carried on `J1`/`J2` (see §3), which stays fully populated/continuous on
> both connectors for return-path integrity, even though almost every other signal reaching this
> board is left NC.
>
> **Open mechanical item:** the exact transition between the PCB strip and the machined metal
> enclosure (fastening method, panel cutout tolerances, cable routing from the PCB strip's J1/J2
> down to the jack field) is not yet resolved - deferred to the dedicated mechanical design pass,
> consistent with the current electronics-only merge scope. The electrical connector definitions
> below (`J1` - Cypher Left Pair Template; `J2` - USM Hub Connector Template) are unaffected by
> this open item.

### Functional Requirements

| ID | Functional Requirement | Notes | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| FR-PLB-01 | Terminate the Cypher Left Pair Template's dead-end at the bottom of the local 2-board HID stack | GND stays fully populated for return-path continuity; every other signal received at `J1` (including `3V3_ENIG`/`5V_MAIN`) is left NC - this board has no ENC module and no `BOARD_ROLE_ID` strap of its own | §3 Signal Routing; BOM J1 |
| FR-PLB-02 | Carry no plugboard-signal-specific pins on either connector | Per DEC-088 - this board's own circuitry never sees plugboard cipher-path signals | §1; §3 |
| FR-PLB-03 | Host the physical plugboard jack field on a machined metal enclosure, not this board's own PCB, with no PCB trace connection to this board's own circuitry | Each jack wired via a harness jumper directly to the Cypher Board's own `J20+` spade bank | §4 Plugboard Jack Field (Mechanical); BOM J3+ (per variant) |
| FR-PLB-04 | Provide 10 (10-Numeric), 26 (26-Char Classic), or 64 (64-Character) plug positions, each with 2 jack sockets (one per plugboard pass) | Jack count and row layout vary by variant - see each variant's own design file | §4 Plugboard Jack Field (Mechanical) |
| FR-PLB-05 | Connect to whichever HID board occupies the bottom of the local stack, matching the shared Cypher Left Pair Template | J1 = Samtec QTS-025 family (male), mating with that board's bottom (female) connector | §5 Interconnects; BOM J1 |
| FR-PLB-06 | Connect to the User Settings Module's bottom Hub connector, relaying nothing further - JTAG/I2C termination lives entirely on USM | J2 = Samtec QTS-025 family (male), mating USM's own bottom (female) Hub connector | §5 Interconnects; BOM J2 |
| FR-PLB-07 | Keep the jack field's metal bushings on a continuous `GND_CHASSIS` network, consistent with the rest of the system's external connectors | Every jack bonds directly to the machined metal enclosure by its threaded bushing; no local `GND_CHASSIS`-to-GND bond on this board | §2 GND_CHASSIS Single-Point Bond; §4 Plugboard Jack Field (Mechanical) |

### Design Requirements

| ID | Design Requirement | Specification | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| DR-PLB-01 | PCB stackup | 4-layer standard per `design/Standards/Global_Routing_Spec.md §2.3.1`; PCB is a thin strip along the top edge only, carrying `J1`/`J2` only - no active components - identical across all three variants | §6 PCB Fabrication & Stackup |
| DR-PLB-02 | Cypher Left Pair Template connector | J1 (male) = QTS-025-01-L-D-RA-P; mates with whichever HID board's bottom (female, QSS-025-01-L-D-RA-K) connector sits directly above; pin-level template owned by `Cypher/Board_Layout.md §4` (its own `J5`) | §5 Interconnects; BOM J1 |
| DR-PLB-03 | USM Hub Connector Template connector | J2 (male) = QTS-025-01-L-D-RA-P; mates USM's own bottom (female, QSS-025-01-L-D-RA-K) Hub connector; pin-level template owned by `User_Settings_Module/Board_Layout.md §2` | §5 Interconnects; BOM J2 |
| DR-PLB-04 | `3V3_ENIG`/`5V_MAIN`/`BOARD_ROLE_ID_IN[3:0]`/`BOARD_ROLE_ID_OUT[3:0]`/`ENC_DATA_IN[5:0]`/`ENC_DATA_OUT[5:0]`/`ENC_ACTIVE_INPUT_N`/`ENC_ACTIVE_OUTPUT_N` at `J1` | All left NC except `3V3_ENIG`/`5V_MAIN` (received, unused) - dead-end signals with nothing below this board to relay to, and this board carries no `BOARD_ROLE_ID` strap or ENC module of its own | §3 Signal Routing |
| DR-PLB-05 | `I2C_SDA`/`I2C_SCL`/`TMS`/`TCK`/`CPLD_RESET_N`/`TDI`/`TDO` at `J2` | All left NC - no I2C device, JTAG TAP, or local logic on this board; USM's own `R1`-`R3` terminate the broadcast JTAG lines, not this board | §3 Signal Routing |
| DR-PLB-06 | `3V3_ENIG`/GND treatment | `3V3_ENIG` received at both `J1` and `J2`, left NC at both - no active components remain on this board to bias. GND received at both, kept fully populated/continuous for return-path integrity | §3 Signal Routing |
| DR-PLB-07 | Plugboard jack sockets (per variant) | Switchcraft 12A ("E12A"), 6.35mm (1/4") 2-conductor switched panel-mount phone jack (Tip, Tip-Shunt switch contact, Sleeve); 3/8-32 UNEF-2A threaded bushing, hardware (washer + hex nut) shipped unassembled; mounted directly to the machined metal enclosure (not this board's own PCB); manually assembled, not part of JLCPCB PCBA - no JLCPCB PN; quantity and RefDes range per variant | §4 Plugboard Jack Field (Mechanical); BOM J3+ (per variant) |
| DR-PLB-08 | PCB mounting holes | MH1-MH4: M3 PTH (3.2mm drill) tied to GND_CHASSIS per GRS §4, on the PCB strip only | §6 PCB Fabrication & Stackup |
| DR-PLB-09 | Jack field chassis bonding | Every jack's metal bushing bonds directly to the machined metal enclosure by mechanical contact (threaded bushing through panel cutout + nut) - no additional bonding hardware required. This board's `GND_CHASSIS` net (enclosure + jack bushings + PCB mounting holes) is **not** locally bonded to GND - the system's only `GND_CHASSIS`-to-GND bond remains on the Power Module | §2 GND_CHASSIS Single-Point Bond; §4 Plugboard Jack Field (Mechanical) |
| DR-PLB-10 | ESD protection | Not required on the PCB. J1/J2 are internal BtB connectors, not hot-swapped or externally accessible, per `design/Standards/Global_Routing_Spec.md §9`. The jack field itself carries no PCB-mounted ESD devices either (it has no PCB trace connection to protect) - patch-cable ESD events are conducted directly to the machined metal enclosure via each jack's chassis bond (DR-PLB-09) rather than into any signal path on this board. Whether any additional protection is needed at the Cypher Board's own `J20+` remains an **open item**, mirroring the equivalent open item already carried there (see `Cypher/Design_Spec.md §8`) | §7 Thermal & ESD |

### Component Block Diagram

```mermaid
flowchart TD
  subgraph cypherIface["Cypher Left Pair Template (mates the bottom-most HID board)"]
    J1["J1 male\n3V3_ENIG/5V_MAIN received (NC/unused), GND continuous (return path)\nENC_DATA/ENC_ACTIVE/BOARD_ROLE_ID received (NC - dead-end)"]
  end

  subgraph usmIface["USM Hub Connector Template (mates USM's bottom connector)"]
    J2["J2 male\n3V3_ENIG received (NC/unused), GND continuous (return path)\nI2C_SDA/SCL, TMS/TCK/CPLD_RESET_N, TDI/TDO received (NC - terminated on USM instead)"]
  end

  subgraph jackField["Plugboard Jack Field (machined metal enclosure, not this board's own PCB - no PCB trace connection)"]
    J3["J3+ Switchcraft 12A switched jacks\n(qty/layout per variant)\nmetal bushings bond to enclosure -> GND_CHASSIS"]
  end

  J3 -. "harness jumper (signal), not PCB trace" .-> cypherJ20["Cypher Board J20+ spade bank"]
```

## 2. Architecture

- **PCB:** a thin strip along the top edge only, 4-layer standard per
  `design/Standards/Global_Routing_Spec.md §2.3.1`. ENIG Gold. 2.0mm filleted corners. Just large
  enough to carry `J1`/`J2` - **no active components** - **it does not carry the jack
  field**, which mounts directly to the machined metal enclosure instead (see §4). This PCB strip
  is identical across all three variants.
- **Assembly:** Single-sided JLCPCB SMT (rear face only) for J1/J2 - a fully-automated
  pass, no manual PCBA steps.
- **Manufacturer:** JLCPCB (standard 4-layer; single-sided SMT PCBA for the PCB strip only). The
  machined metal enclosure and jack field are a separate mechanical build, not part of the JLCPCB
  PCBA order.

### GND_CHASSIS Single-Point Bond

Per `design/Standards/Global_Routing_Spec.md §5`: this board's `GND_CHASSIS` net spans both the
PCB strip's own mounting holes **and** the machined metal enclosure (including every jack's
metal bushing, bonded to the enclosure by mechanical contact - see §4). None of this is locally
bonded to GND on this assembly. The system's only galvanic GND_CHASSIS-to-GND bond remains on the
Power Module.

## 3. Signal Routing

This board carries no active components and no plugboard-signal-specific pins - every signal
reaching either connector other than GND (kept continuous for return-path integrity) is simply
left NC, including `3V3_ENIG` and (at `J1`) `5V_MAIN`.
JTAG spoke termination (`TCK`/`TMS`/`CPLD_RESET_N`) now lives entirely on the User Settings
Module (`R1`-`R3`, see `User_Settings_Module/Design_Spec.md §4`), not on this board - per
DEC-103, this board's own former JTAG connector was retargeted to mate USM directly, rather than
continuing to terminate the old HID JTAG spoke itself.

### NC / dead-end signals at `J1` (Cypher Left Pair Template)

| Signal(s) | Reason |
| :--- | :--- |
| `5V_MAIN` | No LED bank or other `5V_MAIN` consumer on this board |
| `ENC_DATA_IN[5:0]`/`ENC_DATA_OUT[5:0]`, `ENC_ACTIVE_INPUT_N`/`ENC_ACTIVE_OUTPUT_N` | No ENC module on this board; nothing below this board to relay either row to |
| `BOARD_ROLE_ID_IN[3:0]`/`BOARD_ROLE_ID_OUT[3:0]` | This board carries no `BOARD_ROLE_ID` strap of its own and is not identified by the Cypher Board's compatibility comparator; nothing below this board to relay these bits to |

### NC / dead-end signals at `J2` (USM Hub Connector Template)

| Signal(s) | Reason |
| :--- | :--- |
| `I2C_SDA`/`I2C_SCL` | No I2C device on this board |
| `TMS`/`TCK`/`CPLD_RESET_N` | Broadcast JTAG lines, terminated on the User Settings Module itself (`R1`-`R3`) - not on this board |
| `TDI`/`TDO` | No JTAG TAP of its own; USM's own Hub Connector Template leaves these NC on its `J2` side too (see `User_Settings_Module/Board_Layout.md §2`) |

### Continuity signals

| Signal(s) | Path |
| :--- | :--- |
| `3V3_ENIG` (both connectors) | Received at `J1` from whichever HID board sits directly above, and at `J2` from USM; left NC/unused at both - no active components remain on this board to bias |
| GND (both connectors) | Received at both; kept fully populated/continuous - **not** NC, since a continuous signal-return path is required through this board regardless of which other signals are unused |

## 4. Plugboard Jack Field (Mechanical)

The physical plugboard patch jacks mount directly to a **machined metal enclosure** - **not** to
this board's own PCB - and carry **no PCB trace connection** to this board's own circuitry (per
DEC-088). Each jack terminal is wired via a discrete jumper cable directly back to the Cypher
Board's own spade terminal bank (`J20+`, see `Cypher/Design_Spec.md §6`).

- **Jack type:** Switchcraft 12A ("E12A"), 6.35mm (1/4") 2-conductor switched panel-mount phone
  jack - confirmed 2026-08-19 (datasheet: `design/Datasheets/Switchcraft-12A-datasheet.pdf`).
  3/8-32 UNEF-2A threaded bushing, mounted through a cutout in the machined metal enclosure with
  the K178 washer and K180 hex nut (hardware shipped unassembled). **Manually assembled - not
  part of the JLCPCB PCBA order, no JLCPCB PN.** 3 terminals: `Tip`, `Tip-Shunt` (normally-closed
  switch contact, opens when a plug is inserted), and `Sleeve`.
- **Chassis bonding:** each jack's threaded metal bushing makes direct mechanical (and
  electrical) contact with the machined metal enclosure it mounts through - keeping every jack on
  a continuous `GND_CHASSIS` network with the rest of the enclosure and the PCB strip's own
  mounting holes. No additional bonding hardware is required beyond the jack's own mounting nut.
  See §2 GND_CHASSIS Single-Point Bond.
- **Plug arrangement:** each cipher character occupies one "plug" position, consisting of **2
  jack sockets placed immediately next to each other, horizontally (left-to-right)** - one for
  each plugboard pass (Pass 1, Pass 2). Positions are **not** stacked vertically, to keep the
  enclosure's overall height as small as possible.
- **Row layout:** character positions are arranged in rows running top-to-bottom on the vertical
  enclosure face, with the character engraved/printed on the enclosure **directly above its
  plug-pair - not a PCB silkscreen**, since the jack field is not on the PCB. Row count and
  character assignment vary by variant - see each variant's own design file §2.
- **Spacing:** generous horizontal spacing between adjacent plug-pairs (for tidy patch-cable
  routing) and generous vertical spacing between rows (for clear per-plug character labelling).
  Exact dimensions are TBD at mechanical/enclosure layout time.
- **Enclosure sizing:** the machined metal enclosure is sized per variant, scaling in height with
  the row count (see each variant's own design file); the **PCB strip itself is identical across
  all three variants** (fixed size, independent of jack count - it only ever carries `J1`/`J2`).
- **Wiring:** each jack's `Tip` and `Tip-Shunt` terminals are wired together to one spade jumper
  (matching the historical decode-board terminal role), and the `Sleeve` terminal to a second
  spade jumper (matching the historical encode-board terminal role) - both running directly to
  the corresponding spade terminals on the Cypher Board's `J20+` bank - see each variant's own
  design file for the per-position jack count and the resulting total wire-run count back to
  `J20+`.

## 5. Interconnects

### J1 - Cypher Left Pair Template

**Pin-level template owned by the Cypher Board (`Cypher/Board_Layout.md §4`, its own `J5`) - this
board owns only its own physical connector placement and gender, per that shared template.**

- **MPN:** QTS-025-01-L-D-RA-P (Samtec 50-contact 0.635mm right-angle male SMT) - same part as
  Cypher-Input/Cypher-Output's own `J1`.
- **Mates with:** whichever HID board's bottom (female, QSS-025-01-L-D-RA-K) connector sits
  directly above this board.
- **Wiring:** `3V3_ENIG` received, left NC (no active components remain on this board to
  bias). GND received, kept fully populated/continuous - not NC, maintains the signal-return
  path. `5V_MAIN`, `ENC_DATA_IN[5:0]`/`ENC_DATA_OUT[5:0]`, `ENC_ACTIVE_INPUT_N`/
  `ENC_ACTIVE_OUTPUT_N`, and `BOARD_ROLE_ID_IN[3:0]`/`BOARD_ROLE_ID_OUT[3:0]` are all received but
  left NC on this board - see §3 for the full per-signal rationale.

> **Pinout:** see `Board_Layout.md §1` for this board's own wiring; full pin numbering owned by
> `Cypher/Board_Layout.md §4`.

### J2 - USM Hub Connector Template

**Pin-level template owned by the User Settings Module (`User_Settings_Module/Board_Layout.md
§2`, its own `J2`) - this board owns only its own physical connector placement and gender, per
that shared template.**

- **MPN:** QTS-025-01-L-D-RA-P (Samtec 50-contact 0.635mm right-angle male SMT) - same part as
  this board's own `J1`.
- **Mates with:** USM's own bottom (female, QSS-025-01-L-D-RA-K) Hub connector directly above
  this board, per DEC-103.
- **Wiring:** `3V3_ENIG` received, left NC. GND received, kept fully populated/continuous - not
  NC, maintains the signal-return path. `I2C_SDA`/`I2C_SCL`, `TMS`/`TCK`/
  `CPLD_RESET_N`, and `TDI`/`TDO` are all received but left NC on this board - no I2C device or
  JTAG TAP on this board, and USM's own `R1`-`R3` already terminate the broadcast JTAG lines (see
  §3 for the full per-signal rationale).

> **Pinout:** see `Board_Layout.md §2` for this board's own wiring; full pin numbering owned by
> `User_Settings_Module/Board_Layout.md §2`.

## 6. PCB Fabrication & Stackup

- **Stackup:** 4-layer standard per `design/Standards/Global_Routing_Spec.md §2.3.1`. This PCB is
  a thin strip along the top edge only - just large enough for `J1`/`J2`, no active components -
  identical across all three variants; it does **not** extend down to cover the jack field, which
  mounts to the separate machined metal enclosure (see §4).
- **Manufacturer:** JLCPCB. Single-sided SMT PCBA (rear face only) for J1, J2. The machined
  metal enclosure and jack field are a separate mechanical build, outside the JLCPCB PCBA order.
- **Mounting Holes:** MH1-MH4, M3 PTH (3.2mm drill), tied to GND_CHASSIS per GRS §4, on the PCB
  strip itself.

## 7. Thermal & ESD

- **Thermal:** No active components. No thermal concerns.
- **ESD:** J1/J2 are internal BtB connectors, not hot-swapped or externally accessible during
  normal operation - no TVS/ESD protection required on the PCB strip, per
  `design/Standards/Global_Routing_Spec.md §9`. The jack field carries no PCB-mounted ESD devices
  either, since it has no PCB trace connection at all - patch-cable ESD events are conducted
  directly to the machined metal enclosure via each jack's chassis bond (§4), not into any signal
  path on this board. Whether any additional protection is needed at the Cypher Board's own
  `J20+` remains an **open item**, mirroring the equivalent open item already carried there (see
  `Cypher/Design_Spec.md §8`).

## 8. Branding & Traceability

- **Data Plate:** Per GRS §6 on Layer L4 (rear face of the PCB strip). Revision block:
  `STECKERBRETT [Cypher-Plugboard] V1.0` (common to all variants; variant-specific suffix TBD -
  see each variant's own design file).
- **Connector Pin-1 Markers:** J1/J2 silkscreen pin-1 markers required per GRS §7.1.
- **Character labelling:** each plug-pair's corresponding character is engraved/printed on the
  **machined metal enclosure** directly above that pair - **not** a PCB silkscreen, since the
  jack field is not on the PCB - see each variant's own design file for the exact character set
  and case (26-Char Classic: uppercase only; 64-Character: uppercase row block followed by
  lowercase row block, per §2 of that variant's own design file).

## 9. Bill of Materials

> This BOM lists only components common to **all** Plugboard variants (fixed quantity,
> independent of variant) - the two HID interconnect connectors and the JTAG spoke termination
> resistors. Variant-specific components (the plugboard jack sockets themselves, RefDes J3+) with
> their per-variant quantities are listed in each variant's own design file §3
> (`Cypher_Plugboard_26_Char_Design.md`, `Cypher_Plugboard_64_Char_Design.md`,
> `Cypher_Plugboard_10_Numeric_Design.md`).

| RefDes | Specification | MPN | Manufacturer | DigiKey PN | Mouser PN | JLCPCB PN | Alt Supplier + PN | Notes | Footprint Available | Footprint Downloaded | Qty |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| J1, J2 | 50-contact 0.635mm right-angle male SMT | QTS-025-01-L-D-RA-P | Samtec | QTS-025-01-L-D-RA-P-ND | 200-QTS02501LDRAP | C7267889 | - | J1: mates with the bottom-most HID board's bottom connector (Cypher Left Pair Template); J2: mates USM's own bottom Hub connector, per DEC-103; same part as Cypher-Input/Cypher-Output J1 | ✔ | ✔ | 2 |

> **Sourcing status:** J1/J2 have confirmed sourcing, reused directly from Cypher-Input/
> Cypher-Output's own already-approved parts. The plugboard jack socket (variant files) is now
> also confirmed - Switchcraft 12A, DigiKey SC1089-ND, Mouser 502-12A; no JLCPCB PN (manually
> assembled, not part of the JLCPCB PCBA order) - see each variant's own design file §4 BOM.
