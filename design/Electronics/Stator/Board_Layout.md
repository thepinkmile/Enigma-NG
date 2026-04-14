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
| 2 | SYS_RESET_N | CTRL→Ext | Active-low CPLD reset broadcast (driven by Stator U_EXP2 GPA[7] @ 0x21 via I²C — DEC-031) |
| 3 | ENC_IN[0] | Stator → Reflector | Return-pass start: CPLD drives post-plugboard signal to Reflector chain (Step 2 drive in routing matrix) |
| 4 | ENC_IN[1] | Stator → Reflector | Return-pass start: CPLD drives post-plugboard signal to Reflector chain (Step 2 drive in routing matrix) |
| 5 | ENC_IN[2] | Stator → Reflector | Return-pass start: CPLD drives post-plugboard signal to Reflector chain (Step 2 drive in routing matrix) |
| 6 | ENC_IN[3] | Stator → Reflector | Return-pass start: CPLD drives post-plugboard signal to Reflector chain (Step 2 drive in routing matrix) |
| 7 | ENC_IN[4] | Stator → Reflector | Return-pass start: CPLD drives post-plugboard signal to Reflector chain (Step 2 drive in routing matrix) |
| 8 | ENC_IN[5] | Stator → Reflector | Return-pass start: CPLD drives post-plugboard signal to Reflector chain (Step 2 drive in routing matrix) |
| 9 | ENC_OUT[0] | Reflector → Stator | Reflected signal: returns from Reflector chain to Stator CPLD (Step 2 receive in routing matrix) |
| 10 | ENC_OUT[1] | Reflector → Stator | Reflected signal: returns from Reflector chain to Stator CPLD (Step 2 receive in routing matrix) |
| 11 | ENC_OUT[2] | Reflector → Stator | Reflected signal: returns from Reflector chain to Stator CPLD (Step 2 receive in routing matrix) |
| 12 | ENC_OUT[3] | Reflector → Stator | Reflected signal: returns from Reflector chain to Stator CPLD (Step 2 receive in routing matrix) |
| 13 | ENC_OUT[4] | Reflector → Stator | Reflected signal: returns from Reflector chain to Stator CPLD (Step 2 receive in routing matrix) |
| 14 | ENC_OUT[5] | Reflector → Stator | Reflected signal: returns from Reflector chain to Stator CPLD (Step 2 receive in routing matrix) |
| 15 | TTD_RETURN | Reflector → Stator | JTAG TDO return path (short route, bypasses rotor stack) |
| 16 | GND | — | Signal return / shield |

**Connector:** 2×8 2.54mm shrouded box header with polarisation key (e.g. Wurth 61201621621 or equiv).
**Mating connector on Extension: J7 / Reflector: J4 — same 16-pin 2×8 shrouded box header.**
**Power current capacity:** 1 pin × 1A = 1A maximum to Extension/Reflector. Estimated draw ≤200mA — adequate with >4× margin.

> **ENC_DATA bidirectionality:** ENC_IN[0:5] (pins 3–8) and ENC_OUT[0:5] (pins 9–14) carry
> simultaneous bidirectional ENC_DATA on the same connector. See `Stator/Design_Spec.md §3 CPLD
> Signal Routing Matrix` for the full step-by-step signal flow.

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
**Power capacity:** 8 × 3V3_ENIG pins × 0.5A/pin = 4.0A total — adequate for 30-rotor worst case (2.11A typical;
LDO hard limit 3.0A). Note: L1-L4 ferrite bead 3.5A rating is the component current rating, not the system load.
**Power telemetry path:**

```text
[ LINK-BETA (ERM8-020) ] --(3V3_ENIG, pins 28-35)--> [ CSS2H 10mΩ SHUNT ] --(CLEAN 3V3)--> [ ROTOR BUS ]
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
(~208mA: 2× EPM240T100I5N CPLDs + 2× status LEDs; >9× margin).

---

## J_CFG — Settings Board I²C Connector

**Component:** JST B4B-PH-K-S(LF)(SN) — 4-pin JST PH 2.0mm THT (JLCPCB PN TBD; confirm 4-pin B4B variant).
**Placement:** Board edge facing the enclosure panel, accessible without rotor stack removal.
**Silkscreen:** Label `EINSTELLUNGEN` / `SETTINGS` adjacent to connector.
**Cable:** 4-wire ribbon cable to Settings Board J_I2C (100mm recommended).

> SW1 and SW2 DIP switches have been removed. Configuration is now handled via
> panel-mount illuminated rocker switches on the Settings Board (DEC-032).
> R16–R26 pull-downs are retained on the Stator CPLD config input pins to hold
> all configuration bits at logic-0 during power-up until CM5 initialises U_EXP4.

| Pin | Signal | Description |
| :--- | :--- | :--- |
| 1 | 3V3_ENIG | Board power supply to Settings Board |
| 2 | GND | Signal return / GND_CHASSIS bond |
| 3 | SDA | I²C-1 data — shared Stator I²C-1 bus |
| 4 | SCL | I²C-1 clock — shared Stator I²C-1 bus |

---

## U_EXP4 — MCP23017 CPLD Config Output Driver (@ 0x22)

**Component:** MCP23017T-E/SO, SOIC-28.
**Placement:** Near Stator CPLD U1, within 15 mm of R16–R26 pull-down resistors. Decoupling cap within 1 mm of VDD pin.
**Address:** A2=LOW, A1=HIGH, A0=LOW → 0x22.

Drives the CPLD configuration input pins (SW1_OUT[0:3], SW2_OUT[0:5]) and STATOR_CFG_RDY strobe
under CM5 firmware control. CM5 writes the active configuration (sourced from either the Settings
Board switches or its own override) to U_EXP4 via I²C, then pulses STATOR_CFG_RDY HIGH to trigger
CPLD re-latch.

| Port | Pin | Signal | Direction | Connected to |
| :--- | :--- | :--- | :--- | :--- |
| GPA | [0] | SW1_OUT[0] | Output | CPLD config input bit 0 (via R16 pull-down) |
| GPA | [1] | SW1_OUT[1] | Output | CPLD config input bit 1 (via R17 pull-down) |
| GPA | [2] | SW1_OUT[2] | Output | CPLD config input bit 2 (via R18 pull-down) |
| GPA | [3] | SW1_OUT[3] | Output | CPLD config input bit 3 (via R19 pull-down) |
| GPA | [4] | STATOR_CFG_RDY | Output | CPLD re-latch strobe; rising edge triggers re-latch (via R20 pull-down) |
| GPA | [5:7] | — | — | Spare |
| GPB | [0] | SW2_OUT[0] | Output | CPLD reflector config bit 0 (via R21 pull-down) |
| GPB | [1] | SW2_OUT[1] | Output | CPLD reflector config bit 1 (via R22 pull-down) |
| GPB | [2] | SW2_OUT[2] | Output | CPLD reflector config bit 2 (via R23 pull-down) |
| GPB | [3] | SW2_OUT[3] | Output | CPLD reflector config bit 3 (via R24 pull-down) |
| GPB | [4] | SW2_OUT[4] | Output | CPLD reflector config bit 4 (via R25 pull-down) |
| GPB | [5] | SW2_OUT[5] | Output | CPLD internal reflector enable (via R26 pull-down) |
| GPB | [6:7] | — | — | Spare |

See `Settings_Board/Design_Spec.md` for the full CM5 firmware flow and LED control logic.
See `Stator/Design_Spec.md §3` for the CPLD configuration tables.

---

## §9 Routing — Trace Width Specifications

**Board specs:** 4-layer / 2oz finished copper (JLC04161H-7628).
L1 = signal (JTAG/routing); L2 = GND plane; L3 = 3V3_ENIG power pour; L4 = secondary routing / data plate.

**IPC-2221A basis (2oz copper, external, 10°C rise, 25°C ambient):**
For 2oz external: ~0.15 mm/A. Internal pour (L3) handles 2.11 A total without width constraints.
See Global_Routing_Spec.md §1.1 for the full current-category table.

### Trace Width Table

| Net | Peak Current | IPC Calc (2oz ext) | Design Min | **Specified Width** | Layer | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Signal (ENC_IN/OUT, SYS_RESET_N, I2C, TTD_RETURN) | < 5 mA | < 0.001 mm | 0.20 mm | **0.20 mm** | L1 | 3.3 V logic signals; all CPLD I/O and encoder data lines |
| JTAG signals: TCK, TMS, TDI, TDO (CI) | signal | — | 0.127 mm | **0.127 mm (5 mil)** | L1 (external) | 50 Ω controlled impedance over L2 GND plane; per DEC-016. External layer — no inner-layer minimum conflict. See `JTAG_Integrity.md`. |
| JTAG fan-out to encoder ports (L1, cable-drive side) | signal | — | 0.20 mm | **0.20 mm** | L1 | Traces from series resistors R7–R15 to J4/J5/J6 connector pads (post-termination section) |
| 3V3_ENIG entry trace (LINK-BETA → shunt R1) | 2.11 A | 0.33 mm | 0.80 mm | **0.80 mm** | L1 | Carries full rotor-stack + encoder load; series path through CSS2H 10 mΩ Kelvin shunt; consistent with PM §9 and Global_Routing_Spec §1.1 |
| 3V3_ENIG fan-out (post-shunt → L3 pour via-down) | 2.11 A | 0.33 mm | 0.80 mm | **0.80 mm** | L1 | Entry to inner power pour via thermal via cluster |
| 3V3_ENIG per-slot feed (L1 → each rotor ERF8-005 socket) | 57 mA | 0.009 mm | 0.80 mm | **0.80 mm** | L1 | 3V3_ENIG canonical 0.80 mm (Global_Routing_Spec §1.1); one trace per 30 rotor slots |
| 3V3_ENIG distribution (inner power pour) | 2.11 A | — | pour | **copper pour** | L3 | Full uninterrupted 2oz plane; primary 3V3_ENIG distribution |
| GND return (inner GND pour) | — | — | pour | **copper pour** | L2 | Solid GND reference plane; must be uninterrupted under all CI traces on L1 |

### Notes

* **INA219 shunt (R1, CSS2H-2512R-R010ELF, 10 mΩ):** Force and sense traces must be independent
  **0.20 mm** 4-wire Kelvin routes — dedicated sense traces on both IN+ and IN− sides of the shunt,
  never shared with the high-current force traces. Even 1 mΩ of shared trace resistance introduces
  10% measurement error on the 10 mΩ shunt value.
* **JTAG CI traces:** 0.127 mm (5 mil) on L1 over the L2 GND plane achieves 50 Ω controlled
  impedance on the JLC04161H-7628 stackup (h = 0.087 mm, t = 0.035 mm, Eᵣ = 4.4). Per DEC-016.
* **3V3_ENIG entry trace:** 0.80 mm is specified for the 2.11 A trunk path (consistent with PM §9
  which uses 0.80 mm for the LDO output at its 3.0 A hard limit). The 0.80 mm design choice provides
  a 36% current headroom margin toward the 3.0 A LDO limit while aligning with the canonical
  system-wide 3V3_ENIG trace width standard.
