# Stator V1.0 Master Pinout

## J5 — Reflector / Extension Link (16-pin, 2×8, 2.54mm Shrouded Box Header)

Provides a direct power and data link to the Reflector (end-of-stack loopback) board,
bypassing the full rotor stack to avoid cumulative contact resistance on the power rail
and to provide a short TDO return path for the JTAG chain.

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
| 15 | TDO_RETURN | Reflector → Stator | JTAG TDO return path (short route, bypasses rotor stack) |
| 16 | GND | — | Signal return / shield |

**Connector:** 2×8 2.54mm shrouded box header with polarisation key (e.g. Wurth 61201621621 or equiv).
**Mating connector on Extension/Reflector:** J1 — same 16-pin 2×8 shrouded box header.
**Power current capacity:** 1 pin × 1A = 1A maximum to Extension/Reflector. Estimated draw ≤200mA — adequate with >4× margin.

## J2–J4: ROTOR STACK ENTRY CONNECTORS (Specification Pending)

> ⚠️ **Mechanical specification pending.** The rotor interface connector set (3 connectors per rotor position:
> ENC-IN, ENC-OUT, and PWR/JTAG) has not yet been fully defined. Pin count and connector type will be confirmed
> once the mechanical design of the rotor/extension/reflector stack is finalised.
>
> **Positional requirement:** The rotor interface connector set **must be positionally identical** across all boards
> that mate with rotors — Stator (input to Rotor 1), Extension (output from previous group / input to next group),
> and Reflector (output from last rotor). This ensures any rotor can mate at any stack position without re-wiring.
>
> **Planned signal groups per connector position:**
> * **ENC-IN connector:** ENC_IN[0:5] — 6-bit data input to rotor CPLD.
> * **ENC-OUT connector:** ENC_OUT[0:5] — 6-bit data output from rotor CPLD.
> * **PWR/JTAG connector:** 3V3_ENIG (both sides) | GND | TCK | GND | TMS | GND | TDI | GND | SYS_RESET_N | GND |
>   3V3_ENIG. No TDO — TDO returns via the Extension Port (TDO_RETURN on J5).

## LINK-BETA (40-PIN ERM8-020) Explicit Mapping

**Connector:** Samtec ERM8-020-05.0-S-DV-K-TR (Male, 40-pin). Mating ERF8-020 female on Controller Board J2.

| Pin | Signal | Direction | Notes |
| :--- | :--- | :--- | :--- |
| 1 | GND | — | JTAG leading shield |
| 2 | TCK | CTRL→Stator | JTAG clock |
| 3 | GND | — | TCK/TMS inter-pin shield |
| 4 | TMS | CTRL→Stator | JTAG mode select |
| 5 | GND | — | TMS/TDI inter-pin shield |
| 6 | TDI | CTRL→Stator | JTAG data in |
| 7 | GND | — | TDI/RST inter-pin shield |
| 8 | SYS_RESET_N | CTRL→Stator | Active-low system reset; clears all CPLDs in stack |
| 9 | GND | — | JTAG trailing shield |
| 10 | GND | — | Isolation moat pin 1 |
| 11 | GND | — | Isolation moat pin 2 |
| 12 | ENC_IN[0] | CTRL→Stator | Encoder input bit 0 |
| 13 | ENC_IN[1] | CTRL→Stator | Encoder input bit 1 |
| 14 | ENC_IN[2] | CTRL→Stator | Encoder input bit 2 |
| 15 | ENC_IN[3] | CTRL→Stator | Encoder input bit 3 |
| 16 | ENC_IN[4] | CTRL→Stator | Encoder input bit 4 |
| 17 | ENC_IN[5] | CTRL→Stator | Encoder input bit 5 |
| 18 | GND | — | ENC_IN / ENC_OUT inter-group shield |
| 19 | ENC_OUT[0] | Stator→CTRL | Encoder output bit 0 |
| 20 | ENC_OUT[1] | Stator→CTRL | Encoder output bit 1 |
| 21 | ENC_OUT[2] | Stator→CTRL | Encoder output bit 2 |
| 22 | ENC_OUT[3] | Stator→CTRL | Encoder output bit 3 |
| 23 | ENC_OUT[4] | Stator→CTRL | Encoder output bit 4 |
| 24 | ENC_OUT[5] | Stator→CTRL | Encoder output bit 5 |
| 25 | GND | — | ENC_OUT / TDO_RETURN shield |
| 26 | TDO_RETURN | Stator→CTRL | JTAG TDO short-path return (bypasses rotor stack) |
| 27 | GND | — | TDO_RETURN shield |
| 28 | 3V3_ENIG | PM→Stator | Power input from Link-Alpha via Controller (2oz copper) |
| 29 | 3V3_ENIG | PM→Stator | Power input from Link-Alpha via Controller (2oz copper) |
| 30 | 3V3_ENIG | PM→Stator | Power input from Link-Alpha via Controller (2oz copper) |
| 31 | 3V3_ENIG | PM→Stator | Power input from Link-Alpha via Controller (2oz copper) |
| 32 | 3V3_ENIG | PM→Stator | Power input from Link-Alpha via Controller (2oz copper) |
| 33 | 3V3_ENIG | PM→Stator | Power input from Link-Alpha via Controller (2oz copper) |
| 34 | 3V3_ENIG | PM→Stator | Power input from Link-Alpha via Controller (2oz copper) |
| 35 | 3V3_ENIG | PM→Stator | Power input from Link-Alpha via Controller (2oz copper) |
| 36 | GND | — | Power return |
| 37 | GND | — | Power return |
| 38 | GND | — | Power return |
| 39 | GND | — | Power return |
| 40 | GND | — | Power return |

**Power input:** 8 × 3V3_ENIG pins × 0.5A/pin = 4.0A available — adequate for 30-rotor worst case (3.5A).

**Power telemetry path:**

```text
[ LINK-BETA (ERM8-020) ] --(3V3_ENIG, pins 28-35)--> [ 20mΩ SHUNT ] --(CLEAN 3V3)--> [ ROTOR BUS ]
              |                                            |
              +------ (I2C-1) -------- [ INA219 ] --------+
```

## J6–J8: ENCODER PORTS (Specification Pending)

> ⚠️ **Specification pending.** The Encoder Port connectors (one per Encoder board: HID Encoder, Plugboard #1,
> Plugboard #2) require signal requirements to be fully defined before the connector type and size can be confirmed.
> Signals will include at minimum: ENC_IN[0:5], ENC_OUT[0:5], SYS_RESET_N, 3V3_ENIG, and GND. JTAG subset
> (TCK/TMS/TDI/TDO) may also be required. Connector format to be determined.
> See `Encoder/Board_Layout.md` for the current Encoder Data Link pinout as a starting reference.
