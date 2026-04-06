# Linux OS: Power Management

**Status:** Draft
**Project:** Enigma-NG
**Author:** Izzyonstage & GitHub Copilot
**Version:** v1.0.0
**Last Updated:** 2026-04-05

## Overview

The CM5 (Raspberry Pi Compute Module 5) must respond to two hardware power events:

1. **LTC3350 BACKUP trigger (I²C polling)** — primary early-warning mechanism; the BACKUP bit is set when 5V_MAIN falls below 4.40V
   (R14=26.7kΩ; see Power_Module/Design_Spec.md DR-PM-08), triggering a graceful shutdown with the full ≥14.5-second supercap hold-up window available.
2. **PWR_GD (GPIO 27 interrupt)** — secondary hard-backstop from MCP121T-450E voltage supervisor; deasserts (goes LOW) when 5V_MAIN < 4.5V.
   Triggers an emergency sync-and-halt if the I²C daemon fails to catch the BACKUP event.

The recommended approach is **Option C**: poll the LTC3350 via I²C for the BACKUP alert as the primary early-warning mechanism,
with the PWR_GD GPIO as a hard backstop interrupt. This gives the CM5 the full 14.5-second hold-up window to perform a graceful shutdown.

## Hardware Signals

| Signal | GPIO | Pull-up | Source | Trigger |
| --- | --- | --- | --- | --- |
| PWR_GD | GPIO 27 (BCM) | R3 10kΩ to 3V3_ENIG (Controller board) | MCP121T-450E U8 | Active HIGH: 5V_MAIN ≥ 4.5V (HIGH = power good, LOW = fault event) |
| LTC3350 ALERT | I²C (0x09 address) | R7/R8 4.7kΩ on SDA/SCL | LTC3350 U3 | BACKUP bit set when 5V_MAIN < 4.40V (R14=26.7kΩ; see Power_Module/Design_Spec.md PM-06 fix) |

## Option C: Recommended Implementation

### Phase 1 — LTC3350 I²C Polling Daemon (Primary)

A systemd service (`enigma-power-monitor.service`) polls the LTC3350 BACKUP register every 500ms. When the BACKUP condition is detected, it initiates a graceful systemctl poweroff immediately.

The LTC3350 I²C address is 0x09. The BACKUP status is in register 0x01 (STATUS register), bit 3 (BACKUP bit).

Pseudocode for the monitoring daemon:

```python
#!/usr/bin/env python3
"""enigma-power-monitor: LTC3350 backup-mode watchdog."""
import smbus2, time, subprocess, logging, systemd.daemon

BUS      = 1         # I2C bus number on CM5
ADDR     = 0x09      # LTC3350 I2C address
REG_STATUS = 0x01    # LTC3350 STATUS register
BACKUP_BIT = (1 << 3)
POLL_HZ  = 2         # polls per second

logging.basicConfig(level=logging.INFO,
    format='%(asctime)s enigma-power-monitor %(levelname)s: %(message)s')

bus = smbus2.SMBus(BUS)
systemd.daemon.notify('READY=1')
logging.info("Power monitor started — polling LTC3350 at %dHz", POLL_HZ)

while True:
    try:
        status = bus.read_word_data(ADDR, REG_STATUS)
        if status & BACKUP_BIT:
            logging.critical("LTC3350 BACKUP asserted — initiating graceful shutdown")
            subprocess.run(['systemctl', 'poweroff'], check=True)
            break
    except OSError as e:
        logging.warning("I2C read error: %s", e)
    time.sleep(1.0 / POLL_HZ)
```

**systemd unit file** (`/etc/systemd/system/enigma-power-monitor.service`):

```ini
[Unit]
Description=Enigma-NG Power Monitor (LTC3350 backup watchdog)
After=multi-user.target
DefaultDependencies=no
Before=shutdown.target

[Service]
Type=notify
ExecStart=/usr/local/bin/enigma-power-monitor.py
Restart=on-failure
RestartSec=2

[Install]
WantedBy=multi-user.target
```

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
| 5V_MAIN < 4.40V — LTC3350 BACKUP asserted (supercaps take over) | ~shortly after PWR_GD | Hold-up engaged; 14.5s window begins |
| Daemon detects LTC3350 BACKUP asserted and initiates `systemctl poweroff` | ~50ms from power loss | OS begins graceful shutdown |
| OS syncs filesystems, halts | ~10–15s | ROTOR_EN de-asserted; CM5 PMIC halted |
| Supercaps depleted / system off | ≥14.5s from power loss | 5V_MAIN → 0V |

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

The Stator board carries an INA219 (U2, I2C address **0x45**) monitoring the 3V3_ENIG current to the rotor stack via a **10mΩ CSS2H-2512R-R010ELF shunt resistor** (R1 on Stator, 2512 Kelvin-sense; PM R23 is the second system CSS2H instance — total build qty: 2).

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
> Use **CAL = 0x0400** (1024). If this is skipped, the `Current_Register` will read zero regardless of actual current.

```python
INA219_ADDR    = 0x45        # Rotor stack monitor on Stator board
REG_CONFIG     = 0x00
REG_CAL        = 0x05
REG_SHUNT_V    = 0x01
REG_CURRENT    = 0x04

R_SHUNT        = 0.010       # 10mΩ CSS2H-2512R-R010ELF — hardcoded; do not change without updating Stator BOM
CURRENT_LSB    = 0.004       # 4mA per LSB

# INA219 config: 32V bus range, PGA /2 (±80mV shunt), 12-bit, continuous
CONFIG_VALUE   = 0x219F

bus.write_word_data(INA219_ADDR, REG_CONFIG, CONFIG_VALUE)
bus.write_word_data(INA219_ADDR, REG_CAL, 0x0400)  # CAL = 1024

def read_rotor_current_mA():
    raw = bus.read_word_data(INA219_ADDR, REG_CURRENT)
    if raw > 32767: raw -= 65536   # signed 16-bit
    return raw * CURRENT_LSB * 1000  # convert to mA
```

> **Cross-ref:** See `Controller/Design_Spec.md §4` for shunt resistor spec and `design/Electronics/Power_Budgets.md` for expected current range (2.20A worst-case typical).

The **INA219 Power Module Monitor** (for 5V_MAIN) is at I2C address **0x40** on the Power Module board (separate device, different rail).

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
