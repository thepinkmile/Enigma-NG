# Stator V1.0 Master Pinout

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Associated Hardware Revision:** Rev A
**Last Updated:** 2026-04-05

## J7— Reflector / Extension Link (16-pin, 2×8, 2.54mm Shrouded Box Header)

Provides a direct power and data link to the Reflector (end-of-stack loopback) board,
bypassing the full rotor stack to avoid cumulative contact resistance on the power rail
and to provide a short TDO return path for the JTAG chain.

> **Connector Definition Owner:** This board. All other boards using this connector cross-reference here.

| Pin | Signal | Direction | Notes |
| :--- | :--- | :--- | :--- |
| 1 | 3V3_ENIG | PM → Reflector | 3.3V logic power direct from Power Module LDO (bypasses rotor stack) |
| 2 | SYS_RESET_N | CTRL→Ext | Active-low CPLD reset broadcast (from Controller GPIO 26 via LINK-BETA) |
| 3 | ENC_IN[0] | Stator → Reflector | Encoder input bit 0 |
| 4 | ENC_IN[1] | Stator → Reflector | Encoder input bit 1 |
| 5 | ENC_IN[2] | Stator → Reflector | Encoder input bit 2 |
| 6 | ENC_IN[3] | Stator → Reflector | Encoder input bit 3 |
| 7 | ENC_IN[4] | Stator → Reflector | Encoder input bit 4 |
| 8 | ENC_IN[5] | Stator → Reflector | Encoder input bit 5 |
| 9 | ENC_OUT[0] | Reflector → Stator | Encoder output bit 0 |
| 10 | ENC_OUT[1] | Reflector → Stator | Encoder output bit 1 |
| 11 | ENC_OUT[2] | Reflector → Stator | Encoder output bit 2 |
| 12 | ENC_OUT[3] | Reflector → Stator | Encoder output bit 3 |
| 13 | ENC_OUT[4] | Reflector → Stator | Encoder output bit 4 |
| 14 | ENC_OUT[5] | Reflector → Stator | Encoder output bit 5 |
| 15 | TTD_RETURN | Reflector → Stator | JTAG TDO return path (short route, bypasses rotor stack) |
| 16 | GND | — | Signal return / shield |

**Connector:** 2×8 2.54mm shrouded box header with polarisation key (e.g. Wurth 61201621621 or equiv).
**Mating connector on Extension: J7 / Reflector: J4 — same 16-pin 2×8 shrouded box header.**
**Power current capacity:** 1 pin × 1A = 1A maximum to Extension/Reflector. Estimated draw ≤200mA — adequate with >4× margin.

## J1–J3: ROTOR INTERFACE CONNECTORS

> **Connector Definition Owner:** `Rotor/Board_Layout.md — Rotor Interface Connectors`.
> This board hosts the mating connectors. See BOM for part numbers; mechanical finalisation pending.

The connector set (ENC-IN, ENC-OUT, and PWR/JTAG — one of each per rotor position) is defined on the Rotor board.
The positional requirement stands: J1–J3 must be **positionally identical** across Stator, Extension, and Reflector
so any rotor can mate at any position without re-wiring.

## J8 — LINK-BETA (40-Pin ERM8 — To Controller Board)

> **Connector Definition Owner:** `Controller/Board_Layout.md — LINK-BETA`.
> This board uses the mating ERM8-020-05.0-S-DV-K-TR (Male) connector. See BOM for part number.

**Connector:** Samtec ERM8-020-05.0-S-DV-K-TR (Male, 40-pin). Mating ERF8-020 female on Controller Board J2.
**Power capacity:** 8 × 3V3_ENIG pins × 0.5A/pin = 4.0A total — adequate for 30-rotor worst case (2.20A typical;
LDO hard limit 3.0A). Note: L1-L4 ferrite bead 3.5A rating is the component current rating, not the system load.
**Power telemetry path:**

```text
[ LINK-BETA (ERM8-020) ] --(3V3_ENIG, pins 28-35)--> [ 20mΩ SHUNT ] --(CLEAN 3V3)--> [ ROTOR BUS ]
              |                                            |
              +------ (I2C-1) -------- [ INA219 ] --------+
```

## J4–J6: ENCODER PORTS (26-Pin, 2×13, 2.54mm Shrouded Box Header)

**Connector type:** 2×13 (26-pin) 2.54mm pitch shrouded box header with polarisation key.
**Cable:** Standard 26-wire 2.54mm IDC ribbon cable.

### Physical Placement & Silkscreen

```text
Left group:              Right group (stacked vertically):
┌──────────┐             ┌──────────┐
│    J4    │             │    J5    │
│ TASTATUR │             │STECKERBR.│
│    /     │             │    A     │
│ HID UNIT │             └──────────┘
└──────────┘             ┌──────────┐
                         │    J6    │
                         │STECKERBR.│
                         │    B     │
                         └──────────┘
```

> **Silkscreen requirement:** Each port labelled individually in bilingual typewriter style:
>
> * **J4:** `TASTATUR/LAMPENFELD` / `HID UNIT`
> * **J5:** `STECKERBRETT A` / `PLUGBOARD A`
> * **J6:** `STECKERBRETT B` / `PLUGBOARD B`

### JTAG Chain

TCK and TMS are broadcast to all three encoder ports and the rotor stack. SYS_RESET_N is broadcast
to all devices. TDI/TDO form a serial chain routed internally on the Stator PCB:

1. LINK-BETA TDI → **Stator CPLD** TDI
2. Stator CPLD TDO → **J4 (HID Encoder)** TDI *(internal Stator trace)*
3. J4 TDO → **J5 (Plugboard Encoder #1)** TDI *(internal Stator trace)*
4. J5 TDO → **J6 (Plugboard Encoder #2)** TDI *(internal Stator trace)*
5. J6 TDO → **Rotor stack** TDI (via J1–J3 PWR/JTAG connector) *(internal Stator trace)*
6. Rotor stack TDO returns via J7 Extension Port TTD_RETURN

> **Connector Definition Owner:** This board. All other boards using this connector cross-reference here.

### Pin Table (identical across J4, J5, and J6)

| Pin | Signal | Direction | Notes |
| :--- | :--- | :--- | :--- |
| 1 | 3V3_ENIG | Stator→Encoder | Power supply |
| 2 | ENC_IN[0] | Stator→Encoder | Encoder input bit 0 |
| 3 | ENC_IN[1] | Stator→Encoder | Encoder input bit 1 |
| 4 | ENC_IN[2] | Stator→Encoder | Encoder input bit 2 |
| 5 | ENC_IN[3] | Stator→Encoder | Encoder input bit 3 |
| 6 | ENC_IN[4] | Stator→Encoder | Encoder input bit 4 |
| 7 | ENC_IN[5] | Stator→Encoder | Encoder input bit 5 |
| 8 | GND | — | ENC_IN / JTAG group separator |
| 9 | TCK | Stator→Encoder | JTAG clock (broadcast to all encoder ports) |
| 10 | GND | — | TCK/TMS inter-pin shield |
| 11 | TMS | Stator→Encoder | JTAG mode select (broadcast to all encoder ports) |
| 12 | GND | — | TMS/TDO inter-pin shield |
| 13 | TDO | Encoder→Stator | JTAG data out (chains to next device via Stator) |
| 14 | GND | — | TDO/TDI inter-pin shield |
| 15 | TDI | Stator→Encoder | JTAG data in (from previous device via Stator) |
| 16 | GND | — | TDI/SYS_RESET_N shield |
| 17 | SYS_RESET_N | Stator→Encoder | Active-low CPLD reset (broadcast to all encoder ports) |
| 18 | GND | — | JTAG / ENC_OUT group separator |
| 19 | ENC_OUT[0] | Encoder→Stator | Encoder output bit 0 |
| 20 | ENC_OUT[1] | Encoder→Stator | Encoder output bit 1 |
| 21 | ENC_OUT[2] | Encoder→Stator | Encoder output bit 2 |
| 22 | ENC_OUT[3] | Encoder→Stator | Encoder output bit 3 |
| 23 | ENC_OUT[4] | Encoder→Stator | Encoder output bit 4 |
| 24 | ENC_OUT[5] | Encoder→Stator | Encoder output bit 5 |
| 25 | GND | — | ENC_OUT trailing shield / power return |
| 26 | 3V3_ENIG | Stator→Encoder | Power supply |

**Power capacity:** 2 × 3V3_ENIG pins × 1A/pin = 2.0A — adequate for Encoder board load
(~208mA: 2× EPM240T100C5N CPLDs + 2× status LEDs; >9× margin).
