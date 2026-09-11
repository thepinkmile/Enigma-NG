# DEC-099 - CM5 I2C Bank Architecture (I2C0 PM-Dedicated + I2C1-I2C6 via Cypher), MIPI0→MIPI1 Swap, PWM/GPCLK Reservation

|Field|Value|
|:---|:---|
|**Decision ID**|DEC-099|
|**Status**|Decided|
|**Date**|2026-09-04|
|**Author**|Izzyonstage & GitHub Copilot|
|**Amends**|-|
|**Related**|DEC-022, DEC-098, DEC-100|

## Context

The system previously had a single physical I²C bus ("I2C-1") shared by the Power Module, Cypher
Board peripherals, Cypher-Input, and the User Settings Module. This conflated PM telemetry/control
traffic with the encryption engine's own peripheral bus, and left five of the CM5's six available
I²C controller instances completely unused despite an upcoming discussion (Rotor-Cypher software
update mechanism) that will need at least one of them. Retiring the Actuation Module (DEC-100) also
freed CM5 GPIO 8, which happens to be one of two valid pin pairs for RP1's `I2C0` instance.

## Decision

1. **Six-bus I²C architecture:**

   | Bus | GPIO pair | Location | Routing |
   | :--- | :--- | :--- | :--- |
   | `I2C0` | GPIO8/9 (alt pin pair) | Power Module — dedicated | Controller `J3` (PM dock) |
   | `I2C1` | GPIO2/3 (primary pair) | Cypher Board — active peripherals bus (existing, unchanged wiring) | Controller `J5` (Cypher signal dock) |
   | `I2C2` | GPIO4/5 (primary pair) | Cypher Board — reserved/NC, future expansion | Controller `J5` |
   | `I2C3` | GPIO6/7 (primary pair) | Cypher Board — reserved/NC, future expansion | Controller `J5` |
   | `I2C4` | GPIO34/35 (primary pair) | Cypher Board — reserved/NC, future expansion | Controller `J5` |
   | `I2C6` | GPIO38/39 | Cypher Board — reserved/NC, spare/HID-future | Controller `J5` |

   `I2C0` deliberately does **not** appear on the Cypher signal dock (`J5`) — it is PM-only and
   routed exclusively via the existing PM telemetry connector (`J3`).

2. **GPIO relocation for existing status signals.** `I2C2`'s primary pin pair (GPIO4/5) and
   `I2C3`'s primary pin pair (GPIO6/7) collide with four already-committed Controller status
   signals. These are relocated to free GPIO numbers with no other conflicts:

   | Signal | Old GPIO | New GPIO |
   | :--- | :---: | :---: |
   | `ROTOR_EN_N` | 4 | 16 |
   | `PM_IO_INT_N` | 5 | 17 |
   | `USB_FAULT_N` | 6 | 19 |
   | `PWR_GD` | 7 | 24 |

3. **MIPI0 → MIPI1 swap for DSI1 (`J9`).** `I2C6`'s GPIO pair (38/39, `SDA0`/`SCL0`) is shared
   silicon with the MIPI0 control bus per the CM5 datasheet §2.6.1, and is only free for general
   I²C use when MIPI0 itself is unused. The Controller's DSI1 connector (`J9`) is therefore moved
   from CM5 MIPI0 to MIPI1. This is a genuine routing change, not just a label change: MIPI1's
   differential pairs sit on different physical pins of the CM5 200-pin Hirose DF40 connector
   (`MIPI1_D0_N/P` = 175/177, `MIPI1_D1_N/P` = 181/183, `MIPI1_C_N/P` = 187/189, `MIPI1_D2_N/P` =
   193/195, `MIPI1_D3_N/P` = 194/196 — per the official Raspberry Pi CM5 datasheet pinout table).
   MIPI1's own control-plane I²C sub-bus rides on the `ID_SD`/`ID_SC` pins (CM5 pins 35/36, RP1
   GPIO 0/1) rather than GPIO 38/39, so there is no new conflict from activating MIPI1 — HAT
   EEPROM auto-detection is not applicable to this custom carrier board in any case
   (`force_eeprom_read=0` already required to repurpose those pins as generic I/O per the CM5
   datasheet).

4. **PWM/GPCLK reservation.** Four PWM channels (`PWM0[0]`-`PWM0[3]`, GPIO12-15, primary pins, no
   conflict with the I²C plan) and two GPCLK channels (`GPCLK[0]` via GPIO20, `GPCLK[1]` via
   GPIO18 — the two GPCLK instances that remain conflict-free; `GPCLK[2]`/`GPCLK[3]` collide with
   the `I2C3`/`I2C4` GPIO commitments and are not used) are routed to the Cypher signal dock
   (`J5`) and terminate at six bare copper test-pad loops (`TP1`-`TP6`) on the Cypher Board, each
   paired with an adjacent `GND` test-pad loop (`TP7`-`TP12`) for probing convenience. No active
   devices are populated at this time.

   **Buffering requirement for future use:** any future production use of these PWM/GPCLK signals
   requires local buffering/re-driving at each downstream board entry point. Routing an unbuffered
   CM5 clock or PWM signal over a long, uncontrolled backplane trace is not acceptable — this exact
   failure mode was already identified and rejected for the JTAG Module's clock source (DEC-022,
   where routing CM5 `GPCLK0` to the FT232H `OSCI` pin over a long noisy trace was rejected in
   favour of a dedicated on-board crystal).

## Rationale

- Separates PM telemetry/control traffic from the encryption engine's own peripheral bus, matching
  the system's general principle of not conflating unrelated subsystems on a shared resource.
- Provisions for a known, near-term future discussion (Rotor-Cypher software updates) without
  committing to its final design now — reserved banks cost nothing until populated.
- Reuses the CM5's actual available silicon (6 I²C controllers, 4 PWM channels, up to 5 GPCLK
  instances) rather than leaving it permanently idle.
- The MIPI0→MIPI1 swap is a deliberate, explicit trade: DSI1 touchscreen support moves to a
  different (equally capable) CM5 MIPI interface in exchange for freeing a spare I²C bank.

## Impact

- `Controller/Design_Spec.md §3.1, §5, §7.5` and `Board_Layout.md §2, §3.2`: full GPIO/I²C
  reallocation table, MIPI1 pin references, PWM/GPCLK reservation.
- `Cypher/Design_Spec.md` and `Board_Layout.md`: `J2` signal dock full pin map, `TP1`-`TP12` test
  pads added.
- `Power_Module/Design_Spec.md`: I²C references updated from the ambiguous shared "I2C-1" naming
  to explicit `I2C0` (PM-dedicated).
- Contributes to closing `merge-update-ctl-board`.
