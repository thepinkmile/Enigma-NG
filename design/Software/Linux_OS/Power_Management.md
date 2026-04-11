# Linux OS: Power Management

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Last Updated:** 2026-04-05

## Overview

The CM5 (Raspberry Pi Compute Module 5) must respond to two hardware power events:

1. **PWR_GD (GPIO 27)** — first hardware event; MCP121T-450E voltage supervisor deasserts (goes LOW) when 5V_MAIN < 4.5V (~10 ms after mains loss).
   Acts as primary interrupt trigger in the interim implementation (gpio-shutdown device tree overlay).
2. **LTC3350 BACKUP signal** — fires when 5V_MAIN drops to 4.40V (R14=26.7kΩ; see Power_Module/Design_Spec.md DR-PM-08), engaging supercap hold-up.
   This is the preferred interrupt source for the final custom Linux driver implementation (see DEC-025). Provides the full >=21.7-second hold-up window for graceful shutdown.

> **Implementation note:** The final interrupt-driven shutdown driver is deferred to the Software PoC stage (see **DEC-025**). Until then, the
> PWR_GD gpio-shutdown overlay (Phase 2 below) is the active hardware protection path. The Phase 1 pseudocode is retained for reference only.

## Hardware Signals

| Signal | GPIO | Pull-up | Source | Trigger |
| --- | --- | --- | --- | --- |
| PWR_GD | GPIO 27 (BCM) | R3 10kΩ to 3V3_ENIG (Controller board) | MCP121T-450E U8 | Active HIGH: 5V_MAIN ≥ 4.5V (HIGH = power good, LOW = fault event) |
| LTC3350 ALERT | I²C (0x09 address) | R7/R8 4.7kΩ on SDA/SCL | LTC3350 U3 | BACKUP bit set when 5V_MAIN < 4.40V (R14=26.7kΩ; see Power_Module/Design_Spec.md PM-06 fix) |

## Option C: Recommended Implementation

### Phase 1 — LTC3350 BACKUP Interrupt Driver (Deferred — DEC-025)

> **Deferred to Software PoC Stage.** The final implementation uses a custom Linux kernel driver
> that registers the LTC3350 BACKUP signal as a hardware interrupt. This approach eliminates polling
> latency and is the preferred production mechanism. Development is deferred until the physical
> hardware is available for integration testing. See **DEC-025** in design/Design_Log.md.

**Intended behaviour (reference only):**

The driver will:

1. Register an interrupt handler on the LTC3350 ALERT/BACKUP pin.
2. On interrupt, read LTC3350 STATUS register (I2C 0x09, register 0x01) to confirm BACKUP bit (bit 3) is set.
3. Invoke kernel_power_off() or equivalent clean shutdown path.
4. Log the event to the kernel ring buffer for post-mortem analysis.

No polling loop, no userspace daemon, and no POLL_HZ parameter are required. The interrupt response
latency is determined by the kernel IRQ subsystem (typically < 1 ms), giving the full >=21.7-second
supercap hold-up window for OS shutdown.

**I2C parameters (for driver development reference):**

| Parameter | Value |
| --- | --- |
| I2C address | 0x09 |
| STATUS register | 0x01 |
| BACKUP bit | bit 3 (value 0x08) |
| ALERT pin | Active-low open-drain; connect to GPIO with pull-up |

### Phase 2 — PWR_GD GPIO Hard Backstop (Backup)

If the I²C daemon fails to catch the BACKUP event (e.g., I²C bus error, daemon crash), the PWR_GD GPIO provides a last-resort interrupt that triggers an emergency sync-and-halt.

#### Device Tree Configuration

Add to `/boot/firmware/config.txt`:

```ini
# PWR_GD emergency shutdown backstop — GPIO 27 is active-high (good=high); gpio-shutdown triggers on falling edge (fault=low)
dtoverlay=gpio-shutdown,gpio_pin=27,active_low=1,gpio_pull=up
```

GPIO 27 is the assigned PWR_GD input (see Controller Board Design_Spec §6).
The `gpio_pull=up` parameter enables the CM5 internal weak pull-up as a secondary pull-up alongside the external R3 (10kΩ).

The `gpio-shutdown` overlay triggers `systemctl poweroff` on a falling edge of the specified GPIO.
With the external R3 and MCP121T open-drain output, the signal is normally HIGH (5V_MAIN stable) and goes LOW only when 5V_MAIN drops below 4.5V.

#### Alternative: Manual device tree node

For more control (e.g., custom pre-shutdown actions), use a gpio-keys node instead:

```dts
/ {
    enigma_pwr_fail: enigma-pwr-fail {
        compatible = "gpio-keys";
        pwr-good {
            label = "PWR_GD";
            gpios = <&gpio 27 GPIO_ACTIVE_LOW>; /* GPIO 27 is active-high (good=high); gpio-shutdown triggers on falling edge (fault=low) */
            linux,code = <KEY_POWER>;
            debounce-interval = <50>; /* ms */
        };
    };
};
```

Handle `KEY_POWER` in `/etc/systemd/logind.conf`:

```ini
[Login]
HandlePowerKey=poweroff
```

## Shutdown Timing Budget

| Event | Time from power loss | Action |
| --- | --- | --- |
| Mains fails / PoE drops | t = 0 | Input source lost |
| PWR_GD deasserts | ~10ms | MCP121T fires; 5V_MAIN < 4.5V; PWR_GD goes LOW |
| 5V_MAIN < 4.40V — LTC3350 BACKUP asserted (supercaps take over) | ~shortly after PWR_GD | Hold-up engaged; ≥21.7s window begins |
| PWR_GD interrupt triggers gpio-shutdown (interim) / BACKUP interrupt triggers custom driver (deferred — DEC-025) | PWR_GD: ~10 ms from power loss; BACKUP: ~shortly after | OS begins graceful shutdown |
| OS syncs filesystems, halts | ~10–15s | ROTOR_EN de-asserted; CM5 PMIC halted |
| Supercaps depleted / system off | ≥21.7s from power loss | 5V_MAIN → 0V |

## Dependencies

- Python package: `smbus2` (`pip3 install smbus2`)
- Python package: `systemd` (`pip3 install systemd-python`) for sd_notify
- I²C enabled on CM5 (`dtparam=i2c_arm=on` in config.txt)
- `enigma-power-monitor.service` installed and enabled (`systemctl enable enigma-power-monitor`)

## SW1 RGB LED State Machine

The CM5 controls the SW1 RGB LED via four GPIOs once firmware initialises. The hardware handoff
sequence and colour states are defined below.

### Boot Handoff Sequence

1. **Power on (CM5 not yet booted):** `SW_LED_CTRL` (GPIO 20) is floating/low (CM5 GPIO in input mode).
   Hardware path active: MIC1555 (U11) oscillator drives Q_HW → BAT54 diodes → SW_LED_R + SW_LED_G
   simultaneously → 1Hz orange flash on SW1. Identical orange heartbeat to the Controller status LED.

2. **CM5 kernel boots, systemd target reached:** Power monitor service starts.
   Before asserting `SW_LED_CTRL`, pre-set SW_LED_R/G/B GPIOs to desired initial state (orange solid:
   GPIO 17 HIGH, GPIO 18 HIGH, GPIO 19 LOW).

3. **CM5 drives `SW_LED_CTRL` HIGH (GPIO 20):** Hardware Q_HW gate disabled → MIC1555 path cut.
   CM5 now has exclusive control of SW_LED_R/G/B.

4. **Power source detection:** Read POE_STAT (GPIO 24), USB_STAT (GPIO 21), BATT_PRES_N (GPIO 23)
   and set LED colour per table below.

### LED Colour Table

| State | GPIO 17 (R) | GPIO 18 (G) | GPIO 19 (B) | Colour | Control |
| --- | --- | --- | --- | --- | --- |
| Booting (pre-CM5) | 1Hz PWM | 1Hz PWM | Off | 🟠 Orange flash | Hardware (MIC1555) |
| CM5 ready, USB-C active | Off | On | Off | 🟢 Solid green | CM5 GPIO |
| CM5 ready, PoE active | Off | Off | On | 🔵 Solid blue | CM5 GPIO |
| CM5 ready, Battery active | On | On | Off | 🟠 Solid orange | CM5 GPIO |
| Supercap hold-up (mains fail) | PWM 2Hz | PWM 2Hz | Off | 🟠 Fast orange flash | CM5 GPIO |
| Fault / eFuse latched | On | Off | Off | 🔴 Solid red | CM5 GPIO |
| Graceful shutdown in progress | PWM 1Hz | Off | Off | 🔴 Slow red flash | CM5 GPIO |

### SW_LED_CTRL GPIO Initialisation (Device Tree / Python)

Add to the power monitor daemon startup sequence:

```python
import RPi.GPIO as GPIO

SW_LED_R    = 17
SW_LED_G    = 18
SW_LED_B    = 19
SW_LED_CTRL = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup([SW_LED_R, SW_LED_G, SW_LED_B, SW_LED_CTRL], GPIO.OUT, initial=GPIO.LOW)

# Pre-set orange before taking control
GPIO.output(SW_LED_R, GPIO.HIGH)
GPIO.output(SW_LED_G, GPIO.HIGH)

# Take control from hardware oscillator
GPIO.output(SW_LED_CTRL, GPIO.HIGH)

# Now detect power source and set correct colour
def set_led(r, g, b):
    GPIO.output(SW_LED_R, r)
    GPIO.output(SW_LED_G, g)
    GPIO.output(SW_LED_B, b)

poe_active  = not GPIO.input(24)  # Active-low: LOW = PoE live
usb_active  = not GPIO.input(21)  # USB_STAT active low
batt_active = not GPIO.input(23)  # BATT_PRES_N active low

if usb_active:
    set_led(0, 1, 0)   # Green — USB-C
elif poe_active:
    set_led(0, 0, 1)   # Blue — PoE
elif batt_active:
    set_led(1, 1, 0)   # Orange — Battery
else:
    set_led(1, 0, 0)   # Red — No known source (fault)
```

## INA219 Rotor Stack Current Monitor

The Stator board carries an INA219 (U2, I2C address **0x45**) monitoring the 3V3_ENIG current to the rotor stack via a **10mΩ CSS2H-2512R-R010ELF shunt resistor**
(R1 on Stator, 2512 Kelvin-sense; PM R23 is the second system CSS2H instance — total build qty: **3**).

### Hardware Parameters

| Parameter | Value | Notes |
| --- | --- | --- |
| I2C address | 0x45 | Set by A0/A1 pin strapping on Stator INA219 |
| Shunt resistance | **0.010 Ω (10mΩ)** | CSS2H-2512R-R010ELF; hardcoded in firmware — do not change without updating Stator BOM |
| PGA range | ±80mV | Covers 0–8A range (3A LDO max → 30mV drop) |
| ADC resolution | 12-bit | |
| Current LSB | **4mA** | = 80mV full-scale / 2^11 steps / 0.010Ω |
| Calibration register | **0x0400** (1024 decimal) | CAL = 0.04096 / (Current_LSB × R_SHUNT) = 0.04096 / (0.004 × 0.010) |

### Firmware Note

> ⚠️ The INA219 calibration register must be written on every power-up before any current readings are taken.
> Write smbus2 value **0x0004** (byte-swapped from logical 0x0400 = 1024; smbus2 transmits LSB first so INA219 receives 0x0400 = 1024 as intended). If this is skipped, the `Current_Register` will read zero regardless of actual current.

```python
INA219_ADDR    = 0x45        # Rotor stack monitor on Stator board
REG_CONFIG     = 0x00
REG_CAL        = 0x05
REG_SHUNT_V    = 0x01
REG_CURRENT    = 0x04

R_SHUNT        = 0.010       # 10mΩ CSS2H-2512R-R010ELF — hardcoded; do not change without updating Stator BOM
CURRENT_LSB    = 0.004       # 4mA per LSB

# INA219 config: 32V bus range, PGA /2 (±80mV shunt), 12-bit, continuous
# Register value 0x299F byte-swapped for smbus2 little-endian transmission
CONFIG_VALUE   = 0x9F29

bus.write_word_data(INA219_ADDR, REG_CONFIG, CONFIG_VALUE)
bus.write_word_data(INA219_ADDR, REG_CAL, 0x0004)  # CAL = 1024 (big-endian swap)

def read_rotor_current_mA():
    raw = bus.read_word_data(INA219_ADDR, REG_CURRENT)
    raw = ((raw & 0xFF) << 8) | ((raw >> 8) & 0xFF)  # swap bytes (smbus2 LE → INA219 BE)
    if raw > 32767: raw -= 65536   # signed 16-bit
    return raw * CURRENT_LSB * 1000  # convert to mA
```

> **Cross-ref:** See `Stator/Design_Spec.md §5. Power Telemetry` for shunt resistor spec
> and `design/Electronics/Power_Budgets.md` for expected current range (2.11A worst-case typical).

The **INA219 Power Module Monitor** (for 5V_MAIN) is at I2C address **0x40** on the Power Module board (separate device, different rail).

## INA219 5V_MAIN Power Module Monitor

Monitors the 5V_MAIN power rail on the Power Module board. See `Power_Module/Design_Spec.md §3 Telemetry` for hardware details.

### Hardware Parameters

| Parameter | Value | Notes |
| --- | --- | --- |
| I²C address | 0x40 | A0/A1 = GND on U12 |
| Shunt resistance | 0.010 Ω (10mΩ) | CSS2H-2512R-R010ELF R23, Power Module |
| PGA range | ±160mV | Covers 0–16A; 9A worst-case → 90mV drop |
| ADC resolution | 12-bit | |
| Current LSB | 8mA | = 160mV / 2048 / 0.010Ω |
| Calibration register | 0x0200 (512) | CAL = 0.04096 / (0.008 × 0.010) |

### Firmware Note

The CONFIG and calibration registers must be written on every power-up before current readings are valid.

```python
import smbus2

BUS = smbus2.SMBus(1)
INA219_PM_ADDR = 0x40

# CONFIG register (0x00): 32V bus, PGA/4 (±160mV), 12-bit, continuous (big-endian swap)
BUS.write_word_data(INA219_PM_ADDR, 0x00, 0x9F31)  # logical 0x319F byte-swapped for smbus2
# Calibration register (0x05): set before reading current
BUS.write_word_data(INA219_PM_ADDR, 0x05, 0x0002)  # CAL = 512 (big-endian swap)

def read_5v_main_current_mA():
    """Read 5V_MAIN rail current in milliamps (INA219 U12, Power Module)."""
    raw = BUS.read_word_data(INA219_PM_ADDR, 0x04)
    raw = ((raw & 0xFF) << 8) | ((raw >> 8) & 0xFF)  # swap bytes
    if raw > 32767:
        raw -= 65536
    return raw * 8  # Current LSB = 8mA
```

> **Cross-ref:** See `Stator/Design_Spec.md §5. Power Telemetry` for the Rotor-stack INA219 (0x45) hardware spec.

## RTC Battery Configuration

The CM5 MXL7704 PMIC includes a battery charging circuit for the RTC backup battery. When a
**non-rechargeable CR2032** is fitted (as specified in `Controller/Design_Spec.md §5`), the
charging circuit must be disabled in software as a belt-and-suspenders measure alongside the
hardware Schottky diode (D1) that physically blocks the charge path at CM5 VBAT (Pin 95).

### config.txt Setting

Ensure the following line is **absent from** `/boot/firmware/config.txt` (do NOT include it):

```ini
# DO NOT add this line — it enables PMIC battery charging at 3.0V and will degrade a CR2032:
# dtparam=rtc_bbat_vchg=3000000
```

Ensure the `rtc_bbat_vchg` parameter is absent from `/boot/firmware/config.txt` — the CM5 defaults to no charging without it.

> **Note:** The following describes a non-standard alternative configuration only. For the
> Rev A production design (CR2032 + D1 Schottky), the `rtc_bbat_vchg` parameter must remain
> **absent** from `config.txt`. Do not apply the ML2032 configuration to Rev A hardware.
>
> **Note:** The hardware Schottky diode (D1, Nexperia BAT54) already physically prevents the
> PMIC from charging the CR2032 regardless of this software setting. The config.txt setting is
> a secondary safeguard. If the battery is ever changed to a rechargeable ML2032, remove D1
> from the PCB AND set `dtparam=rtc_bbat_vchg=3000000` to enable correct charging.

### RTC Time Synchronisation

The CM5 will use `systemd-timesyncd` (NTP) to synchronise the RTC on boot when network
is available. On first boot, or after battery replacement, the RTC may show an incorrect time
until network sync completes. This is expected behaviour.

To force an immediate RTC sync from the system clock (after NTP has synced):

```bash
sudo hwclock --systohc
```

To read the current RTC time:

```bash
sudo hwclock --show
```

## Open Items

- [x] PWR_GD assigned to CM5 GPIO 27 (BCM) — see Controller/Design_Spec.md §6
- [ ] Verify LTC3350 I²C address (0x09 is default; may change based on ADDR pin strapping — check schematic)
- [ ] Test hold-up timing under actual CM5 load profile (5W assumed; measure at first prototype)
- [ ] Consider adding LTC3350 charge status polling (SOC readout) for optional status LED control from software
- [ ] Confirm Marquardt 1800 series exact PN for RGB LED rocker (select at mechanical design stage for panel cutout dimensions)
- [ ] Verify BSS138 (Q_HW) gate threshold vs MIC1555 output voltage — MIC1555 output ~3V into NMOS gate; BSS138 Vgs(th) = 0.8–1.5V → fully on. Confirm at schematic capture.
- [x] SW_LED_CTRL (GPIO 20) added to Link-Alpha pin 47 wiring — completed; see Controller/Board_Layout.md LINK-ALPHA table.
- [ ] Verify CM5 VBAT (Pin 95) is correctly identified in the CM5 Hirose DF40 200-pin connector datasheet before PCB layout.
