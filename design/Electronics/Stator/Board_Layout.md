# Stator V1.0 Master Pinout

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.1.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-20

## J10— Reflector / Extension Link (16-pin, 2×8, 2.54mm Shrouded Box Header)

Provides a direct power and data link to the Reflector (end-of-stack loopback) board, bypassing the
full rotor stack to avoid cumulative contact resistance on the power rail and to provide a short TDO
return path for the JTAG chain.

> **Connector Definition Owner:** This board. All other boards using this connector cross-reference
> here.

| Pin | Signal | Direction | Notes |
| :--- | :--- | :--- | :--- |
| 1 | 3V3_ENIG | PM -> Reflector | 3.3V logic power direct from Power Module LDO (bypasses rotor stack) |
| 2 | SYS_RESET_N | CTRL->Ext | Active-low CPLD reset broadcast |
| 3 | ENC_IN[0] | Stator -> Reflector | Return-pass start |
| 4 | ENC_IN[1] | Stator -> Reflector | Return-pass start |
| 5 | ENC_IN[2] | Stator -> Reflector | Return-pass start |
| 6 | ENC_IN[3] | Stator -> Reflector | Return-pass start |
| 7 | ENC_IN[4] | Stator -> Reflector | Return-pass start |
| 8 | ENC_IN[5] | Stator -> Reflector | Return-pass start |
| 9 | ENC_OUT[0] | Reflector -> Stator | Reflected signal return |
| 10 | ENC_OUT[1] | Reflector -> Stator | Reflected signal return |
| 11 | ENC_OUT[2] | Reflector -> Stator | Reflected signal return |
| 12 | ENC_OUT[3] | Reflector -> Stator | Reflected signal return |
| 13 | ENC_OUT[4] | Reflector -> Stator | Reflected signal return |
| 14 | ENC_OUT[5] | Reflector -> Stator | Reflected signal return |
| 15 | TTD_RETURN | Reflector -> Stator | JTAG TDO return path |
| 16 | GND | — | Signal return / shield |

**Connector:** 2×8 2.54mm shrouded box header with polarisation key (e.g. Wurth 61201621621 or
equivalent).  
**Mating connector on Extension: J7 / Reflector: J4 — same 16-pin 2×8 shrouded box header.**

## J1–J3: ROTOR INTERFACE CONNECTORS
>
> **Connector Definition Owner:** `Rotor/Board_Layout.md — Rotor Interface Connectors`.

The connector set (ENC-IN, ENC-OUT, and PWR/JTAG — one of each per rotor position) is defined on the
Rotor board. The positional requirement stands: J1–J3 must be **positionally identical** across
Stator, Extension, and Reflector so any rotor can mate at any position without re-wiring.

## J11 / J12 — Controller Dock (Hybrid Molex — To Controller Board)
>
> **Connector Definition Owner:** `Controller/Board_Layout.md — Controller ↔ Stator Dock`.

**Connector:** Molex `2195620015` hybrid blind-mate plug pair (`J11` / `J12`). Mating Controller
receptacles are Molex `2195630015` on `J4` / `J5`.

## J4 / J5 / J6 / J7 / J8 / J9 — ENCODER PORTS (26-Pin, 2×13, 2.54mm Shrouded Box Header)

**Connector type:** 2×13 (26-pin) 2.54mm pitch shrouded box header with polarisation key.  
**Cable:** Standard 26-wire 2.54mm IDC ribbon cable.  
**Role model:** three physical banks of two identical ports.

### Physical Placement & Silkscreen

```text
Bank 1 (HID)             Bank 2 (Plugboard Pass 1)    Bank 3 (Plugboard Pass 2)
┌────────────┐           ┌────────────┐               ┌────────────┐
│    J4     │           │    J6     │               │    J8     │
│  KBD_ENC   │           │PLG_PASS1_  │               │PLG_PASS2_  │
│            │           │    DEC     │               │    DEC     │
└────────────┘           └────────────┘               └────────────┘
┌────────────┐           ┌────────────┐               ┌────────────┐
│    J5     │           │    J7     │                │    J9     │
│  LBD_DEC   │           │PLG_PASS1_  │               │PLG_PASS2_  │
│            │           │    ENC     │               │    ENC     │
└────────────┘           └────────────┘               └────────────┘
```

> **Silkscreen requirement:** Each port labelled by fixed function, not by a generic board number.
>
### JTAG Chain

TCK and TMS are broadcast to all six encoder ports and the rotor stack. SYS_RESET_N is broadcast to
all devices. TDI/TDO form a serial chain routed internally on the Stator PCB:

1. Controller `J5` / Stator `J12` TDI -> **Stator CPLD** TDI
2. Stator CPLD TDO -> **J4 (`KBD_ENC`)** TDI
3. J4 TDO -> **J5 (`LBD_DEC`)** TDI
4. J5 TDO -> **J6 (`PLG_PASS1_DEC`)** TDI
5. J6 TDO -> **J7 (`PLG_PASS1_ENC`)** TDI
6. J7 TDO -> **J8 (`PLG_PASS2_DEC`)** TDI
7. J8 TDO -> **J9 (`PLG_PASS2_ENC`)** TDI
8. J9 TDO -> **Rotor stack** TDI (via J1–J3 PWR/JTAG connector)
9. Rotor stack TDO returns via J10 Extension Port `TTD_RETURN`

> **Connector Definition Owner:** This board. All other boards using this connector cross-reference
> here.
>
### Pin Table (identical across J4/J5/J6/J7/J8/J9)

| Pin | Signal | Direction | Notes |
| :--- | :--- | :--- | :--- |
| 1 | 3V3_ENIG | Stator->Encoder | Power supply |
| 2 | ENC_IN[0] | Stator->Encoder | Decoder input bit 0 |
| 3 | ENC_IN[1] | Stator->Encoder | Decoder input bit 1 |
| 4 | ENC_IN[2] | Stator->Encoder | Decoder input bit 2 |
| 5 | ENC_IN[3] | Stator->Encoder | Decoder input bit 3 |
| 6 | ENC_IN[4] | Stator->Encoder | Decoder input bit 4 |
| 7 | ENC_IN[5] | Stator->Encoder | Decoder input bit 5 |
| 8 | GND | — | ENC_IN / JTAG group separator |
| 9 | TCK | Stator->Encoder | JTAG clock (broadcast to all encoder ports) |
| 10 | GND | — | TCK/TMS inter-pin shield |
| 11 | TMS | Stator->Encoder | JTAG mode select (broadcast to all encoder ports) |
| 12 | GND | — | TMS/TDO inter-pin shield |
| 13 | TDO | Encoder->Stator | JTAG data out (chains to next device via Stator) |
| 14 | GND | — | TDO/TDI inter-pin shield |
| 15 | TDI | Stator->Encoder | JTAG data in (from previous device via Stator) |
| 16 | GND | — | TDI/SYS_RESET_N shield |
| 17 | SYS_RESET_N | Stator->Encoder | Active-low CPLD reset (broadcast to all encoder ports) |
| 18 | GND | — | JTAG / ENC_OUT group separator |
| 19 | ENC_OUT[0] | Encoder->Stator | Encoder output bit 0 |
| 20 | ENC_OUT[1] | Encoder->Stator | Encoder output bit 1 |
| 21 | ENC_OUT[2] | Encoder->Stator | Encoder output bit 2 |
| 22 | ENC_OUT[3] | Encoder->Stator | Encoder output bit 3 |
| 23 | ENC_OUT[4] | Encoder->Stator | Encoder output bit 4 |
| 24 | ENC_OUT[5] | Encoder->Stator | Encoder output bit 5 |
| 25 | GND | — | ENC_OUT trailing shield / power return |
| 26 | 3V3_ENIG | Stator->Encoder | Power supply |

**Power capacity:** 2 × 3V3_ENIG pins × 1A/pin = 2.0A — adequate for one Encoder Module load
(~104mA).

---

## J_CFG — Settings Board I²C Connector

**Component:** JST B6B-PH-K-S(LF)(SN) — 6-pin JST PH 2.0mm THT (JLCPCB: C131342).  
**Placement:** Board edge facing the enclosure panel, accessible without rotor stack removal.

## U_EXP4 — MCP23017 CPLD Config Output Driver (@ 0x22)

**Component:** MCP23017T-E/SO, SOIC-28.  
**Placement:** Near Stator CPLD U1, within 15 mm of config pull-down resistors. Decoupling cap within
1 mm of VDD pin.

Drives the CPLD configuration input pins (SW1_OUT[0:3], SW2_OUT[0:5]) and STATOR_CFG_RDY strobe
under CM5 firmware control.

---

## §9 Routing — Trace Width Specifications

**Board specs:** 4-layer / 2oz finished copper (JLC04161H-7628).  
L1 = signal (JTAG/routing); L2 = GND plane; L3 = 3V3_ENIG power pour; L4 = secondary routing / data
plate.

### Trace Width Table

| Net | Peak Current | IPC Calc (2oz ext) | Design Min | **Specified Width** | Layer | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Signal (ENC_IN/OUT, SYS_RESET_N, I2C) | < 5 mA | < 0.001 mm | 0.20 mm | **0.20 mm** | L1 | 3.3 V logic signals |
| JTAG signals: TCK, TMS, TDI, TDO, TTD_RETURN (CI) | signal | — | 0.127 mm | **0.127 mm (5 mil)** | L1 (external) | 50 Ω controlled impedance over L2 GND plane |
| JTAG fan-out to encoder ports (L1, cable-drive side) | signal | — | 0.20 mm | **0.20 mm** | L1 | Traces from series resistors to encoder-port connector pads |
| 3V3_ENIG entry trace (`J12` dock -> shunt R1) | 2.05 A | 0.31 mm | 0.80 mm | **0.80 mm** | L1 | Carries full rotor-stack + encoder load |
| 3V3_ENIG fan-out (post-shunt -> L3 pour via-down) | 2.05 A | 0.31 mm | 0.80 mm | **0.80 mm** | L1 | Entry to inner power pour via thermal via cluster |
| 3V3_ENIG distribution (inner power pour) | 2.05 A | — | pour | **copper pour** | L3 | Full uninterrupted 2oz plane |
| GND return (inner GND pour) | — | — | pour | **copper pour** | L2 | Solid GND reference plane |

### Notes

* **JTAG CI traces:** 0.127 mm (5 mil) on L1 over the L2 GND plane achieves 50 Ω controlled
  impedance on the JLC04161H-7628 stackup.
* **Encoder-port terminations:** provide one TCK and one TMS series resistor per encoder port plus
  one TDI-chain series resistor for each Stator-driven cable segment in the six-module chain.
* **3V3_ENIG entry trace:** 0.80 mm remains the canonical trunk width for the 2.05 A design budget.
