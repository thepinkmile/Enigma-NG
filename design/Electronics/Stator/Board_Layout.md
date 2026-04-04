# Stator V1.0 Master Pinout

## J5 — Reflector / Extension Link (16-pin, 2×8, 2.54mm Shrouded Box Header)

Provides a direct power and data link to the Reflector (end-of-stack loopback) board,
bypassing the full rotor stack to avoid cumulative contact resistance on the power rail
and to provide a short TDO return path for the JTAG chain.

| Pin | Signal | Direction | Notes |
| :--- | :--- | :--- | :--- |
| 1 | 3V3_ENIG | PM → Reflector | 3.3V logic power direct from Power Module LDO (bypasses rotor stack) |
| 2 | GND | — | Power return |
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
**Mating connector on Reflector:** J1 — same 16-pin 2×8 shrouded box header.
**Power current capacity:** 1 pin × 1A = 1A maximum to Reflector. Reflector estimated draw ≤200mA — adequate with >4× margin.

## J2-J4: SATELLITE LINKS (40-PIN)

* **Pins 1-4:** 3V3_ENIG / GND Power
* **Pins 5-18:** ENC_IN [0:5] (Symmetrical GND shielding)
* **Pins 21-32:** ENC_OUT [0:5] (Symmetrical GND shielding)
* **Pins 33-40:** JTAG IN/OUT Loop (Shielded TCK/TMS/TDI/TDO)

## LINK-BETA (80-PIN ERF8) Explicit Mapping

* **Pins 1-9:** JTAG + Reset (GND|TCK|GND|TMS|GND|TDI|GND|RST|GND)
* **Pins 10-20:** Ground isolation bank
* **Pins 21-24:** 5V_MAIN (pins 21-22) / GND (pins 23-24) — previously 3V3_SYSTEM, reassigned per DEC-001
* **Pins 25-26:** ETH_LED_LINK / ETH_LED_ACT
* **Pins 27-30:** GND
* **Pins 31-34:** Status I/O / PWR_GD / I2C_return
* **Pins 35-38:** I2C1 (SDA/SCL) telemetry chain
* **Pins 39-44:** 3V3_ENIG input from Power Module (via Controller pass-through)
* **Pins 41-46:** ENC_IN [0:5] (sniffer from Controller)
* **Pins 47-52:** ENC_OUT [0:5] (sniffer to Controller)
* **Pins 54-60:** 3V3_ENIG output to Stator power tree
* **Pins 49-80:** 5V_MAIN / additional GND (not typically used by Stator logic)

## Telemetry Layout

```text
[ LINK-BETA (ERF8) ] --(3V3_ENIG)--> [ 20mΩ SHUNT ] --(CLEAN 3V3)--> [ ROTOR BUS ]
              |                         |
              +-- (I2C-1) -- [ INA219 ]-+
```
