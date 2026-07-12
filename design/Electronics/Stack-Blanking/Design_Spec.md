# Stack-Blanking Board (V1.0) Design Specification

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v.0.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-07-12

## 1. Overview

The Stack-Blanking Board is a passive signal-routing board that terminates the end of the Rotor
Mini-Stack chain. It fits on the rear face of the last Rotor Mini-Stack, mating with Stack-Input
Board J2 (rear stacking connector) and Stack-Output Board J2 (rear stacking connector).

| Responsibility | Description |
| :--- | :--- |
| **Signal bridging** | Routes SIG-BLOCK-A (ENC_DATA forward) → SIG-BLOCK-B (return), SIG-BLOCK-C (ENC reflector) → SIG-BLOCK-D (return), and SIG-BLOCK-E (TTD outbound) → SIG-BLOCK-F (TTD_RETURN) across the two connectors |
| **Chain termination** | Provides idle-state bias resistors for all signals that dead-end at this board: ENC_ACTIVE_N, TCK, TMS, CPLD_RESET_N, ACTUATE_REQUEST_N |
| **EMC shielding** | 4-layer board with GND pour on L1 (top) and L4 (bottom); all signal routing on inner layers L2/L3 |

The board carries two vertical male Samtec QTS-025 connectors, one on each side. In normal
operation J1 mates with Stack-Input Board J2 and J2 mates with Stack-Output Board J2. For
transport or bench testing without any Rotor Mini-Stacks fitted, J1 and J2 can be plugged
directly into Cypher Board J3 and J4 respectively to complete the signal loop.

> **Minimum system configuration:** At least 1 Rotor Mini-Stack is required during cipher
> operation. The direct Cypher Board connection is for transport and bench testing only.

### Functional Requirements

| ID | Functional Requirement | Notes | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| FR-SBLK-01 | Terminate the Rotor Mini-Stack chain at the rear of the last mini-stack | J1 mates with Stack-Input J2; J2 mates with Stack-Output J2 | §4 Interconnects; BOM J1, J2 |
| FR-SBLK-02 | Bridge SIG-BLOCK-A to SIG-BLOCK-B — ENC data forward end-of-chain turnaround | ENC_OUT[5:0] from J1 (Stack-Input J2 OUT) routed to J2 ENC_IN[5:0] IN (Stack-Output J2) | §3 Signal Routing |
| FR-SBLK-03 | Bridge SIG-BLOCK-C to SIG-BLOCK-D — ENC reflector data return into last mini-stack | ENC_OUT[5:0] from J2 (Stack-Output J2 OUT) routed to J1 ENC_IN[5:0] IN (Stack-Input J2) | §3 Signal Routing |
| FR-SBLK-04 | Bridge SIG-BLOCK-E to SIG-BLOCK-F — rename TTD as TTD_RETURN at chain end | TTD from J1 (Stack-Input J2 OUT) routed to J2 TTD_RETURN ×2 IN (Stack-Output J2) | §3 Signal Routing |
| FR-SBLK-05 | Terminate JTAG spoke signals (TCK, TMS, CPLD_RESET_N) at end of chain | Idle-state bias resistors R2–R4; per existing JTAG design intent (DEC-016) | §3 Termination; BOM R2–R4 |
| FR-SBLK-06 | Terminate ENC_ACTIVE_N (SIG-BLOCK-G) at end of chain | Pull-up R1 to 3V3_ENIG | §3 Termination; BOM R1 |
| FR-SBLK-07 | Terminate ACTUATE_REQUEST_N at end of chain | Pull-up R5 to 3V3_ENIG; no next mini-stack to trigger | §3 Termination; BOM R5 |
| FR-SBLK-08 | Leave 5V_MAIN (SIG-BLOCK-H) pins NC — no 5V_MAIN required on this board | SIG-BLOCK-H terminates at chain end | §3 Signal Routing |
| FR-SBLK-09 | Compatible with Cypher Board J3/J4 for transport and bench testing without mini-stacks | J1/J2 vertical male connectors mate with Cypher Board vertical female QSS-025 J3/J4 | §4 Interconnects |

### Design Requirements

| ID | Design Requirement | Specification | Satisfied By / Cross-Ref |
| :--- | :--- | :--- | :--- |
| DR-SBLK-01 | PCB stackup | 4-layer per `design/Standards/Global_Routing_Spec.md §2.3.1`; GND pour on L1 (top) and L4 (bottom) for shielding; signal routing on L2 and L3 only | §5 PCB Fabrication & Stackup |
| DR-SBLK-02 | Stack-Input mating connector (J1 — right side) | J1 = QTS-025-01-L-D-A-GP-K-TR (Samtec 50-contact vertical male SMT); same pinout as Cypher Board `Board_Layout.md §2` (J3); mates with Stack-Input J2 (QSS-025-01-L-D-RA-K right-angle female) in normal use, or Cypher Board J3 (QSS-025-01-L-D-A-GP-K vertical female) for transport | §4 Interconnects; BOM J1 |
| DR-SBLK-03 | Stack-Output mating connector (J2 — left side) | J2 = QTS-025-01-L-D-A-GP-K-TR (Samtec 50-contact vertical male SMT); same pinout as Cypher Board `Board_Layout.md §3` (J4); mates with Stack-Output J2 (QSS-025-01-L-D-RA-K right-angle female) in normal use, or Cypher Board J4 (QSS-025-01-L-D-A-GP-K vertical female) for transport | §4 Interconnects; BOM J2 |
| DR-SBLK-04 | Signal routing layers | All signal traces on L2 and L3 only; no signal traces on L1 or L4; GND pours on L1 and L4 must be uninterrupted except for pad fanout vias | §5 PCB Fabrication & Stackup |
| DR-SBLK-05 | Termination resistors | R1–R5: 10 kΩ 1% 0402; placed within 3mm of J1; R1 (ENC_ACTIVE_N pull-up), R2 (TCK pull-down), R3 (TMS pull-up), R4 (CPLD_RESET_N pull-up), R5 (ACTUATE_REQUEST_N pull-up) | §3 Termination; BOM R1–R5 |
| DR-SBLK-06 | 5V_MAIN NC | All 5V_MAIN contact positions on J1 and J2 are NC; no trace connection to 5V_MAIN | §3 Signal Routing |
| DR-SBLK-07 | 3V3_ENIG continuity | 3V3_ENIG and GND are connected between J1 and J2 (power continuity across the board); 3V3_ENIG also supplies pull-up resistors R1/R3/R4/R5 | §3 Signal Routing |
| DR-SBLK-08 | Mounting holes | MH1–MH4: M3 PTH (3.2mm drill) tied to GND_CHASSIS per GRS §4. No BOM entry. | §5 PCB Fabrication; GRS §4.3 |

### Component Block Diagram

```mermaid
flowchart LR
  subgraph J1side["J1 — Stack-Input Side (right)"]
    J1["J1 QTS-025 vertical male\nmates with Stack-Input J2\nor Cypher Board J3 (transport)"]
  end

  subgraph J2side["J2 — Stack-Output Side (left)"]
    J2["J2 QTS-025 vertical male\nmates with Stack-Output J2\nor Cypher Board J4 (transport)"]
  end

  subgraph term["Termination (all at J1)"]
    R1["R1 10kΩ pull-up\nENC_ACTIVE_N → 3V3_ENIG"]
    R2["R2 10kΩ pull-down\nTCK → GND"]
    R3["R3 10kΩ pull-up\nTMS → 3V3_ENIG"]
    R4["R4 10kΩ pull-up\nCPLD_RESET_N → 3V3_ENIG"]
    R5["R5 10kΩ pull-up\nACTUATE_REQUEST_N → 3V3_ENIG"]
  end

  J1 -- "SIG-BLOCK-A: ENC_OUT[5:0]" --> J2
  J2 -- "SIG-BLOCK-C: ENC_OUT[5:0]" --> J1
  J1 -- "SIG-BLOCK-E→F: TTD → TTD_RETURN" --> J2
  J1 -- "3V3_ENIG + GND" --> J2
  J1 --> R1
  J1 --> R2
  J1 --> R3
  J1 --> R4
  J1 --> R5
```

## 2. Architecture

- **PCB:** 4-layer per `design/Standards/Global_Routing_Spec.md §2.3.1`. ENIG Gold.
  2.0mm filleted corners.
- **Assembly:** Single-sided; passive components only (5× 0402 resistors).
- **Manufacturer:** JLCPCB (standard 4-layer).

### GND_CHASSIS Single-Point Bond

Per GRS §5: local `GND_CHASSIS` net tied to mounting holes; no local GND to GND_CHASSIS bond.
System's only galvanic bond remains on the Power Module.

## 3. Signal Routing and Termination

### Bridged signals (J1 ↔ J2 routed traces on L2/L3)

| Signal(s) | Source at J1 | Destination at J2 | Signal Block transition |
| :--- | :--- | :--- | :--- |
| ENC_OUT[5:0] | In from Stack-Input J2 (SIG-BLOCK-A fwd) | Out to Stack-Output J2 ENC_IN[5:0] (SIG-BLOCK-B return start) | A → B |
| ENC_OUT[5:0] (reflector) | In from Stack-Output J2 (SIG-BLOCK-C) via J2 | Out to Stack-Input J2 ENC_IN[5:0] (SIG-BLOCK-D return start) | C → D |
| TTD | In from Stack-Input J2 (SIG-BLOCK-E end) | Out to Stack-Output J2 TTD_RETURN ×2 (SIG-BLOCK-F start) | E → F (renamed) |
| 3V3_ENIG, GND | J1 bottom power section | J2 bottom power section | SIG-BLOCK-I passthrough |

### Terminated signals (dead-end at this board — J1 only)

| RefDes | Signal | Termination | Rationale |
| :--- | :--- | :--- | :--- |
| R1 | ENC_ACTIVE_N (SIG-BLOCK-G) | 10 kΩ pull-up to 3V3_ENIG | Holds signal inactive (HIGH) at chain end; no next mini-stack to receive |
| R2 | TCK | 10 kΩ pull-down to GND | Prevents spurious clocking at JTAG spoke end |
| R3 | TMS | 10 kΩ pull-up to 3V3_ENIG | Holds JTAG TAP in Test-Logic-Reset at spoke end |
| R4 | CPLD_RESET_N | 10 kΩ pull-up to 3V3_ENIG | Holds CPLDs out of reset at chain end |
| R5 | ACTUATE_REQUEST_N | 10 kΩ pull-up to 3V3_ENIG | No next mini-stack; holds signal inactive at chain end |

### NC signals

| Signal | Reason |
| :--- | :--- |
| 5V_MAIN (SIG-BLOCK-H) | No 5V_MAIN required; SIG-BLOCK-H terminates at chain end with all pins NC on both J1 and J2 |

## 4. Interconnects

### J1 — Stack-Input Mating Connector (QTS-025-01-L-D-A-GP-K-TR)

**Connector definition owner: Cypher Board `Board_Layout.md §2` (J3 — Stack-Input / STA-side).**
Same signal pinout as Cypher Board J3.

- **MPN:** QTS-025-01-L-D-A-GP-K-TR (Samtec 50-contact vertical male SMT)
- **Normal use:** mates with Stack-Input Board J2 (QSS-025-01-L-D-RA-K right-angle female)
- **Transport / bench:** mates with Cypher Board J3 (QSS-025-01-L-D-A-GP-K vertical female)
- **Top 26 contacts (signal region):** per `Cypher/Board_Layout.md §2` — ENC data + JTAG
  (TCK, TMS, TTD, CPLD_RESET_N terminating or routing here); full allocation pending
  `merge-cypher-board-j3j6-pinouts`
- **Bottom 24 contacts (power/control region):** 3V3_ENIG, 5V_MAIN (NC), GND,
  ENC_ACTIVE_N (terminating), CPLD_RESET_N (terminating), ACTUATE_REQUEST_N (terminating);
  full allocation pending `merge-cypher-board-j3j6-pinouts`

> **Pinout:** see `Board_Layout.md §1`.

### J2 — Stack-Output Mating Connector (QTS-025-01-L-D-A-GP-K-TR)

**Connector definition owner: Cypher Board `Board_Layout.md §3` (J4 — Stack-Output / REF-side).**
Same signal pinout as Cypher Board J4.

- **MPN:** QTS-025-01-L-D-A-GP-K-TR (Samtec 50-contact vertical male SMT)
- **Normal use:** mates with Stack-Output Board J2 (QSS-025-01-L-D-RA-K right-angle female)
- **Transport / bench:** mates with Cypher Board J4 (QSS-025-01-L-D-A-GP-K vertical female)
- **Top 24 contacts (signal region):** per `Cypher/Board_Layout.md §3` — ENC data return +
  TTD_RETURN; full allocation pending `merge-cypher-board-j3j6-pinouts`
- **Bottom 10 contacts (power region):** 3V3_ENIG + GND

> **Pinout:** see `Board_Layout.md §2`.

## 5. PCB Fabrication & Stackup

- **Stackup:** 4-layer per `design/Standards/Global_Routing_Spec.md §2.3.1`.

| Layer | Function | Notes |
| :--- | :--- | :--- |
| L1 (top) | GND pour — shielding | Continuous copper pour; no signal traces |
| L2 | Signal routing | All bridging traces and 3V3_ENIG distribution |
| L3 | Signal routing | Additional routing as required |
| L4 (bottom) | GND pour — shielding | Continuous copper pour; no signal traces |

- **Manufacturer:** JLCPCB. Single-sided assembly.
- **Fillets:** 2.0mm rounded PCB corners.
- **Mounting Holes:** MH1–MH4, M3 PTH (3.2mm drill), tied to GND_CHASSIS per GRS §4. No BOM entry.
- **Signal trace width:** JTAG and ENC data traces on L2/L3 routed at CI width per
  `design/Standards/Global_Routing_Spec.md §2.3.1`, targeting 50 Ohm controlled impedance.

## 6. Thermal & ESD

- **Thermal:** No active ICs. No thermal concerns.
- **ESD:** No ESD protection devices required. This board is not accessible during live mini-stack
  insertion or rotor swap — it is fitted once to the last mini-stack and not removed during
  normal operation. Per `design/Standards/Global_Routing_Spec.md §9`.

## 7. Branding & Traceability

- **Data Plate:** Per GRS §6 on Layer L4. Revision block:
  `ABSCHLUSSBLENDE [Stack-Blanking] V1.0`.
- **Connector Pin-1 Markers:** J1 and J2 silkscreen pin-1 markers required per GRS §7.1.

## 8. Bill of Materials

| RefDes | Specification | MPN | Manufacturer | DigiKey PN | Mouser PN | JLCPCB PN | Alt Supplier + PN | Notes | Footprint Available | Footprint Downloaded | Qty |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| J1, J2 | 50-contact vertical male SMT | QTS-025-01-L-D-A-GP-K-TR | Samtec | QTS-025-01-L-D-A-GP-K-TR-ND | 200-QTS02501LDAGPKTR | C5714677 | – | J1: mates with Stack-Input J2 or Cypher J3 (transport); J2: mates with Stack-Output J2 or Cypher J4 (transport) | ✔ | ✔ | 2 |
| R1, R3, R4, R5 | 10kΩ 1% 0402 | ERJ-2RKF1002X | Panasonic | P10.0KLCT-ND | 667-ERJ-2RKF1002X | C191123 | – | R1: ENC_ACTIVE_N pull-up; R3: TMS pull-up; R4: CPLD_RESET_N pull-up; R5: ACTUATE_REQUEST_N pull-up — all to 3V3_ENIG | ✔ | ✔ | 4 |
| R2 | 10kΩ 1% 0402 | ERJ-2RKF1002X | Panasonic | P10.0KLCT-ND | 667-ERJ-2RKF1002X | C191123 | – | TCK pull-down to GND — JTAG spoke end termination | ✔ | ✔ | 1 |
